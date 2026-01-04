#!/usr/bin/env node

/**
 * Static Site Generator for Raeez's Research Papers
 * 
 * Fetches content from Google Docs and generates beautiful static HTML.
 * Also generates an Atom feed (feed.xml) for RSS syndication.
 * 
 * Usage:
 *   npm run build              # Build all documents from cache/network
 *   npm run build -- smart-assets   # Build single document
 *   npm run build:force        # Clear cache and rebuild
 *   npm run fetch              # Fetch fresh content from Google Docs
 *   npm run fetch:apps-script  # Fetch via Apps Script (slower but reliable)
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const { JSDOM } = require('jsdom');

const docs = require('./docs.config.js');
const template = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8');

const OUTPUT_DIR = path.join(__dirname, 'dist');
const CACHE_DIR = path.join(__dirname, '.cache');

// Site metadata for feed
const SITE_CONFIG = {
  title: 'Raeez Lorgat',
  subtitle: 'Building operating systems for sovereignty',
  url: 'https://raeez.com',
  author: {
    name: 'Raeez Lorgat',
    email: 'raeez@momentum.inc',
    uri: 'https://raeez.com'
  }
};

// Apps Script URL (your existing one)
const APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwap-GYIRky-iOioo_7IaA0VvW8t_i1lXNesPlLT-hcGsJxQUeb93YR_t466iVw8wpdBQ/exec';

// Ensure directories exist
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
if (!fs.existsSync(CACHE_DIR)) fs.mkdirSync(CACHE_DIR, { recursive: true });

/**
 * Make an HTTPS request with redirect handling
 */
function httpsGet(url, options = {}) {
  return new Promise((resolve, reject) => {
    const makeRequest = (requestUrl, redirectCount = 0) => {
      if (redirectCount > 5) {
        reject(new Error('Too many redirects'));
        return;
      }
      
      https.get(requestUrl, {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
          ...options.headers
        },
        timeout: 30000
      }, (response) => {
        if (response.statusCode === 302 || response.statusCode === 301) {
          makeRequest(response.headers.location, redirectCount + 1);
          return;
        }
        
        if (response.statusCode !== 200) {
          reject(new Error(`HTTP ${response.statusCode}`));
          return;
        }
        
        let data = '';
        response.on('data', chunk => data += chunk);
        response.on('end', () => resolve(data));
      }).on('error', reject).on('timeout', () => reject(new Error('Request timeout')));
    };
    
    makeRequest(url);
  });
}

/**
 * Fetch HTML content from Google Docs via Apps Script
 */
async function fetchViaAppsScript(docId) {
  const url = `${APPS_SCRIPT_URL}?id=${docId}`;
  console.log(`  Fetching via Apps Script...`);
  
  const data = await httpsGet(url);
  
  // Check for error response
  if (data.startsWith('{') && data.includes('error')) {
    throw new Error('Apps Script returned an error');
  }
  
  return data;
}

/**
 * Fetch HTML content from Google Docs direct export
 */
async function fetchDirectExport(docId) {
  const url = `https://docs.google.com/document/d/${docId}/export?format=html`;
  console.log(`  Fetching direct export...`);
  return httpsGet(url);
}

/**
 * Get content for a document - uses cache or fetches
 */
async function getDocContent(doc, options = {}) {
  const cacheFile = path.join(CACHE_DIR, `${doc.id}.html`);
  const forceRefresh = options.force || false;
  const useAppsScript = options.appsScript || false;
  
  // Check cache
  if (!forceRefresh && fs.existsSync(cacheFile)) {
    const stats = fs.statSync(cacheFile);
    const age = Date.now() - stats.mtimeMs;
    const maxAge = 24 * 60 * 60 * 1000; // 24 hours
    
    if (age < maxAge) {
      console.log(`  Using cached content (${Math.round(age / 60000)} min old)`);
      return fs.readFileSync(cacheFile, 'utf8');
    }
  }
  
  // Fetch fresh content
  let data;
  try {
    if (useAppsScript) {
      data = await fetchViaAppsScript(doc.id);
    } else {
      // Try direct first, fall back to Apps Script
      try {
        data = await fetchDirectExport(doc.id);
      } catch (directError) {
        console.log(`  Direct fetch failed (${directError.message}), trying Apps Script...`);
        data = await fetchViaAppsScript(doc.id);
      }
    }
  } catch (error) {
    // If we have a cache file, use it even if expired
    if (fs.existsSync(cacheFile)) {
      console.log(`  Fetch failed, using stale cache`);
      return fs.readFileSync(cacheFile, 'utf8');
    }
    throw error;
  }
  
  // Save to cache
  fs.writeFileSync(cacheFile, data);
  console.log(`  Cached to ${path.basename(cacheFile)}`);
  
  return data;
}

/**
 * Check if an element looks like a TOC entry
 * - Has an internal anchor link (href starts with #)
 * - Text ends with a number (page number)
 * - Is relatively short (not a content paragraph)
 */
function isTocEntry(element) {
  const link = element.querySelector('a[href^="#"]');
  if (!link) return false;
  
  const text = element.textContent.trim();
  
  // Must end with a number (page number)
  if (!/\d+\s*$/.test(text)) return false;
  
  // Should be relatively short (TOC entries are typically under 120 chars)
  if (text.length > 120) return false;
  
  // Should not be a very long paragraph
  const words = text.split(/\s+/).length;
  if (words > 20) return false;
  
  return true;
}

/**
 * Check if text matches a TOC heading pattern
 */
function isTocHeading(text) {
  const normalized = text.trim().toLowerCase().replace(/[:\s]+$/, '');
  return normalized === 'table of contents' || 
         normalized === 'contents' ||
         normalized === 'toc';
}

/**
 * Detect and wrap Table of Contents in a styled container
 * Handles multiple cases:
 * 1. Explicit TOC heading followed by links
 * 2. No heading, but consecutive TOC-like entries (links ending with page numbers)
 */
function wrapTableOfContents(container, contentDoc) {
  const allElements = Array.from(container.querySelectorAll('h1, h2, h3, h4, h5, h6, p'));
  
  let tocHeading = null;
  let tocHeadingIndex = -1;
  let tocEntries = [];
  
  // Strategy 1: Look for explicit TOC heading
  for (let i = 0; i < allElements.length; i++) {
    const el = allElements[i];
    if (isTocHeading(el.textContent)) {
      tocHeading = el;
      tocHeadingIndex = i;
      break;
    }
  }
  
  // If we found a heading, collect entries after it
  if (tocHeading) {
    for (let i = tocHeadingIndex + 1; i < allElements.length; i++) {
      const el = allElements[i];
      if (isTocEntry(el)) {
        tocEntries.push(el);
      } else if (tocEntries.length > 0) {
        // Stop when we hit non-TOC content after finding some entries
        break;
      }
      // Skip non-TOC elements before first entry (like blank paragraphs)
    }
  }
  
  // Strategy 2: No heading found - look for consecutive TOC entries
  if (!tocHeading || tocEntries.length === 0) {
    let consecutiveEntries = [];
    let bestRun = [];
    let bestRunStart = -1;
    let currentRunStart = -1;
    
    for (let i = 0; i < allElements.length; i++) {
      const el = allElements[i];
      
      if (isTocEntry(el)) {
        if (consecutiveEntries.length === 0) {
          currentRunStart = i;
        }
        consecutiveEntries.push(el);
      } else {
        // End of a run - check if it's the best one
        if (consecutiveEntries.length >= 3 && consecutiveEntries.length > bestRun.length) {
          bestRun = [...consecutiveEntries];
          bestRunStart = currentRunStart;
        }
        consecutiveEntries = [];
        currentRunStart = -1;
      }
    }
    
    // Check final run
    if (consecutiveEntries.length >= 3 && consecutiveEntries.length > bestRun.length) {
      bestRun = consecutiveEntries;
      bestRunStart = currentRunStart;
    }
    
    // Use the best run if we found one
    if (bestRun.length >= 3) {
      tocEntries = bestRun;
      tocHeading = null; // We'll create one
      tocHeadingIndex = bestRunStart;
    }
  }
  
  // Need at least 3 entries to consider it a TOC
  if (tocEntries.length < 3) return;
  
  // Create TOC wrapper
  const tocNav = contentDoc.createElement('nav');
  tocNav.className = 'toc';
  tocNav.setAttribute('aria-label', 'Table of Contents');
  
  // Create title
  const tocTitle = contentDoc.createElement('h2');
  tocTitle.className = 'toc-title';
  tocTitle.textContent = 'Contents';
  tocNav.appendChild(tocTitle);
  
  // Create list
  const tocList = contentDoc.createElement('ol');
  tocList.className = 'toc-list';
  
  tocEntries.forEach(entry => {
    const li = contentDoc.createElement('li');
    li.className = 'toc-item';
    
    // Extract the link and clean up
    const link = entry.querySelector('a[href^="#"]');
    if (link) {
      const newLink = contentDoc.createElement('a');
      newLink.href = link.href;
      
      // Get text without page number
      let text = entry.textContent.trim();
      text = text.replace(/\s*\d+\s*$/, '').trim();
      newLink.textContent = text;
      
      li.appendChild(newLink);
    } else {
      li.textContent = entry.textContent.replace(/\s*\d+\s*$/, '').trim();
    }
    
    tocList.appendChild(li);
  });
  
  tocNav.appendChild(tocList);
  
  // Insert TOC and remove original elements
  const firstEntry = tocEntries[0];
  firstEntry.parentElement.insertBefore(tocNav, firstEntry);
  
  // Remove original TOC elements
  if (tocHeading) tocHeading.remove();
  tocEntries.forEach(entry => entry.remove());
}

/**
 * Clean and transform Google Docs HTML to clean, semantic HTML
 */
function cleanGoogleDocsHtml(rawHtml, filterPatterns = []) {
  const { document: contentDoc } = new JSDOM(rawHtml).window;
  
  // Get body content
  const body = contentDoc.body;
  if (!body) return '';
  
  // Create a clean container
  const container = contentDoc.createElement('div');
  container.innerHTML = body.innerHTML;
  
  // First, detect and wrap TOC
  wrapTableOfContents(container, contentDoc);
  
  // Filter out specified patterns from non-TOC content
  filterPatterns.forEach(pattern => {
    const regex = new RegExp(pattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
    container.querySelectorAll('p, h1, h2, h3, h4, h5, h6').forEach(el => {
      // Skip TOC elements
      if (el.closest('.toc')) return;
      
      const text = el.textContent.trim();
      if (regex.test(text) && text.length < 200) {
        el.remove();
      }
    });
  });
  
  // Clean up styles and classes
  container.querySelectorAll('*').forEach(el => {
    // Preserve TOC classes
    const className = el.className;
    const isTocElement = className && (
      className.includes('toc') || 
      className.includes('toc-')
    );
    
    if (!isTocElement) {
      el.removeAttribute('class');
    }
    
    // Preserve IDs on headings (for TOC links)
    const tagName = el.tagName.toLowerCase();
    if (!['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].includes(tagName)) {
      el.removeAttribute('id');
    }
    
    const style = el.getAttribute('style');
    if (style) {
      const keepStyles = [];
      if (style.includes('text-align:center') || style.includes('text-align: center')) {
        keepStyles.push('text-align: center');
      }
      if (keepStyles.length > 0) {
        el.setAttribute('style', keepStyles.join('; '));
      } else {
        el.removeAttribute('style');
      }
    }
  });
  
  // Unwrap meaningless spans
  container.querySelectorAll('span').forEach(span => {
    const style = span.getAttribute('style') || '';
    if (!style && span.children.length === 0) {
      const text = contentDoc.createTextNode(span.textContent);
      span.replaceWith(text);
    }
  });
  
  // Remove empty paragraphs
  container.querySelectorAll('p').forEach(p => {
    if (p.textContent.trim() === '' && p.querySelectorAll('img').length === 0) {
      p.remove();
    }
  });
  
  // Convert <b> to <strong>, <i> to <em>
  container.querySelectorAll('b').forEach(b => {
    const strong = contentDoc.createElement('strong');
    strong.innerHTML = b.innerHTML;
    b.replaceWith(strong);
  });
  
  container.querySelectorAll('i').forEach(i => {
    const em = contentDoc.createElement('em');
    em.innerHTML = i.innerHTML;
    i.replaceWith(em);
  });
  
  // Clean list items
  container.querySelectorAll('li').forEach(li => {
    li.querySelectorAll('span').forEach(span => {
      if (!span.getAttribute('style')) {
        const parent = span.parentElement;
        while (span.firstChild) {
          parent.insertBefore(span.firstChild, span);
        }
        span.remove();
      }
    });
  });
  
  // Clean tables
  container.querySelectorAll('table').forEach(table => {
    table.removeAttribute('style');
    table.querySelectorAll('td, th').forEach(cell => {
      cell.removeAttribute('style');
    });
  });
  
  // Remove leading <hr> elements (the header already provides separation)
  while (container.firstElementChild && container.firstElementChild.tagName === 'HR') {
    container.firstElementChild.remove();
  }
  
  // Remove <hr> immediately after TOC (redundant visual break)
  const toc = container.querySelector('.toc');
  if (toc && toc.nextElementSibling && toc.nextElementSibling.tagName === 'HR') {
    toc.nextElementSibling.remove();
  }
  
  // Collapse consecutive <hr> elements into one
  const hrs = container.querySelectorAll('hr');
  hrs.forEach(hr => {
    while (hr.nextElementSibling && hr.nextElementSibling.tagName === 'HR') {
      hr.nextElementSibling.remove();
    }
  });
  
  // Get cleaned HTML and do final regex cleanups
  let cleanedHtml = container.innerHTML
    .replace(/<span[^>]*>\s*<\/span>/gi, '')
    .replace(/(<br\s*\/?>\s*){3,}/gi, '<br><br>')
    .replace(/&nbsp;/g, ' ')
    .replace(/\s{2,}/g, ' ')
    .replace(/<p[^>]*>\s*<\/p>/gi, '')
    .replace(/>\s+</g, '>\n<');
  
  return cleanedHtml;
}

/**
 * Generate the meta HTML with optional link
 */
function generateMetaHtml(doc) {
  if (doc.metaLink) {
    return `${doc.meta} <a href="${doc.metaLink.url}" target="_blank" rel="noopener">${doc.metaLink.text}</a>`;
  }
  return doc.meta;
}

/**
 * Apply the template to the content
 */
function applyTemplate(doc, content) {
  return template
    .replace(/\{\{title\}\}/g, doc.title)
    .replace(/\{\{subtitle\}\}/g, doc.subtitle)
    .replace(/\{\{description\}\}/g, doc.description)
    .replace(/\{\{slug\}\}/g, doc.slug)
    .replace(/\{\{metaHtml\}\}/g, generateMetaHtml(doc))
    .replace(/\{\{content\}\}/g, content);
}

/**
 * Escape XML special characters
 */
function escapeXml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

/**
 * Parse date from doc.meta string
 * Handles formats like "August 2025", "v0.35 — October 2025", "Version 0.4.0 — December 2025"
 */
function parseDateFromMeta(meta) {
  const months = {
    'january': '01', 'february': '02', 'march': '03', 'april': '04',
    'may': '05', 'june': '06', 'july': '07', 'august': '08',
    'september': '09', 'october': '10', 'november': '11', 'december': '12'
  };
  
  // Match patterns like "Month YYYY" or "Month, YYYY"
  const monthYearMatch = meta.match(/\b(january|february|march|april|may|june|july|august|september|october|november|december)\s*,?\s*(\d{4})\b/i);
  
  if (monthYearMatch) {
    const month = months[monthYearMatch[1].toLowerCase()];
    const year = monthYearMatch[2];
    return `${year}-${month}-15T00:00:00Z`; // Use middle of month
  }
  
  // Fallback to current date
  return new Date().toISOString();
}

/**
 * Determine category based on document slug/content
 */
function getDocCategory(doc) {
  const slug = doc.slug.toLowerCase();
  
  if (['smart-buildings', 'prefabricated-construction', 'archai'].includes(slug)) {
    return { term: 'built-environment', label: 'Built Environment' };
  }
  
  // Default to infrastructure for most docs
  return { term: 'infrastructure', label: 'Infrastructure' };
}

/**
 * Generate Atom feed XML
 */
function generateAtomFeed(builtDocs) {
  const now = new Date().toISOString();
  
  // Sort docs by date (newest first)
  const sortedDocs = [...builtDocs].sort((a, b) => {
    const dateA = new Date(parseDateFromMeta(a.meta));
    const dateB = new Date(parseDateFromMeta(b.meta));
    return dateB - dateA;
  });
  
  // Get most recent update time
  const lastUpdated = sortedDocs.length > 0 
    ? parseDateFromMeta(sortedDocs[0].meta)
    : now;
  
  let feed = `<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>${escapeXml(SITE_CONFIG.title)}</title>
  <subtitle>${escapeXml(SITE_CONFIG.subtitle)}</subtitle>
  <link href="${SITE_CONFIG.url}/feed.xml" rel="self" type="application/atom+xml"/>
  <link href="${SITE_CONFIG.url}" rel="alternate" type="text/html"/>
  <id>${SITE_CONFIG.url}/</id>
  <updated>${lastUpdated}</updated>
  <author>
    <name>${escapeXml(SITE_CONFIG.author.name)}</name>
    <email>${SITE_CONFIG.author.email}</email>
    <uri>${SITE_CONFIG.author.uri}</uri>
  </author>
  <rights>© ${new Date().getFullYear()} ${escapeXml(SITE_CONFIG.author.name)}</rights>
  <icon>${SITE_CONFIG.url}/favicon.ico</icon>
  <generator>Raeez Site Builder</generator>
`;

  // Add entries for each document
  sortedDocs.forEach(doc => {
    const publishDate = parseDateFromMeta(doc.meta);
    const category = getDocCategory(doc);
    const docUrl = `${SITE_CONFIG.url}/${doc.slug}.html`;
    
    // Build subtitle for content
    let contentHtml = `<p>${escapeXml(doc.description)}</p>`;
    if (doc.metaLink) {
      contentHtml += `<p><a href="${escapeXml(doc.metaLink.url)}">${escapeXml(doc.metaLink.text)}</a></p>`;
    }
    
    feed += `
  <entry>
    <title>${escapeXml(doc.title)}</title>
    <link href="${docUrl}" rel="alternate" type="text/html"/>
    <id>${docUrl}</id>
    <published>${publishDate}</published>
    <updated>${publishDate}</updated>
    <summary>${escapeXml(doc.description)}</summary>
    <category term="${category.term}" label="${category.label}"/>
    <content type="html">&lt;p&gt;&lt;em&gt;${escapeXml(doc.subtitle)}&lt;/em&gt;&lt;/p&gt;${contentHtml}</content>
  </entry>
`;
  });

  feed += `</feed>
`;

  return feed;
}

/**
 * Build a single document
 */
async function buildDocument(doc, options = {}) {
  console.log(`\n📄 ${doc.slug}`);
  
  try {
    // Get content (cached or fresh)
    const rawHtml = await getDocContent(doc, options);
    
    // Clean and transform
    console.log(`  Cleaning HTML...`);
    const cleanedContent = cleanGoogleDocsHtml(rawHtml, doc.filterPatterns || []);
    
    // Apply template
    console.log(`  Applying template...`);
    const finalHtml = applyTemplate(doc, cleanedContent);
    
    // Write output
    const outputPath = path.join(OUTPUT_DIR, `${doc.slug}.html`);
    fs.writeFileSync(outputPath, finalHtml);
    console.log(`  ✓ dist/${doc.slug}.html`);
    
    return true;
  } catch (error) {
    console.error(`  ✗ Error: ${error.message}`);
    return false;
  }
}

/**
 * Build all documents
 */
async function buildAll(options = {}) {
  console.log('╔═══════════════════════════════════════════╗');
  console.log('║   Raeez.com Static Site Generator         ║');
  console.log('╚═══════════════════════════════════════════╝');
  console.log(`\nBuilding ${docs.length} documents...`);
  
  let success = 0;
  let failed = 0;
  const builtDocs = [];
  
  for (const doc of docs) {
    const result = await buildDocument(doc, options);
    if (result) {
      success++;
      builtDocs.push(doc);
    } else {
      failed++;
    }
  }
  
  // Generate Atom feed
  console.log('\n📡 Generating Atom feed...');
  try {
    const feedXml = generateAtomFeed(builtDocs);
    const feedPath = path.join(OUTPUT_DIR, 'feed.xml');
    fs.writeFileSync(feedPath, feedXml);
    console.log(`  ✓ dist/feed.xml (${builtDocs.length} entries)`);
  } catch (error) {
    console.error(`  ✗ Feed generation failed: ${error.message}`);
  }
  
  console.log('\n════════════════════════════════════════════');
  console.log(`  ✓ ${success} built   ✗ ${failed} failed`);
  console.log('════════════════════════════════════════════\n');
  
  return failed === 0;
}

/**
 * Fetch fresh content for all documents (pre-cache)
 */
async function fetchAll(options = {}) {
  console.log('╔═══════════════════════════════════════════╗');
  console.log('║   Fetching Google Docs Content            ║');
  console.log('╚═══════════════════════════════════════════╝');
  console.log(`\nFetching ${docs.length} documents...\n`);
  
  let success = 0;
  let failed = 0;
  
  for (const doc of docs) {
    console.log(`📥 ${doc.slug}`);
    try {
      await getDocContent(doc, { force: true, ...options });
      success++;
    } catch (error) {
      console.error(`  ✗ ${error.message}`);
      failed++;
    }
  }
  
  console.log('\n════════════════════════════════════════════');
  console.log(`  ✓ ${success} fetched   ✗ ${failed} failed`);
  console.log('════════════════════════════════════════════\n');
}

/**
 * Main entry point
 */
async function main() {
  const args = process.argv.slice(2);
  
  // Parse flags
  const force = args.includes('--force');
  const appsScript = args.includes('--apps-script');
  const fetchOnly = args.includes('--fetch');
  
  // Get non-flag arguments
  const positional = args.filter(a => !a.startsWith('--'));
  
  if (force) {
    console.log('Clearing cache...');
    fs.rmSync(CACHE_DIR, { recursive: true, force: true });
    fs.mkdirSync(CACHE_DIR, { recursive: true });
  }
  
  if (fetchOnly) {
    // Just fetch, don't build
    await fetchAll({ appsScript });
    return;
  }
  
  if (positional.length > 0) {
    // Build specific document
    const slug = positional[0];
    const doc = docs.find(d => d.slug === slug);
    
    if (!doc) {
      console.error(`Document not found: ${slug}`);
      console.log('\nAvailable documents:');
      docs.forEach(d => console.log(`  - ${d.slug}`));
      process.exit(1);
    }
    
    const success = await buildDocument(doc, { force, appsScript });
    
    // Still regenerate feed even for single doc builds
    console.log('\n📡 Regenerating Atom feed...');
    const feedXml = generateAtomFeed(docs);
    const feedPath = path.join(OUTPUT_DIR, 'feed.xml');
    fs.writeFileSync(feedPath, feedXml);
    console.log(`  ✓ dist/feed.xml`);
    
    process.exit(success ? 0 : 1);
  } else {
    // Build all
    const success = await buildAll({ force, appsScript });
    process.exit(success ? 0 : 1);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
