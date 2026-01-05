#!/usr/bin/env node

/**
 * Static Site Generator for Raeez's Research Papers
 * 
 * Fetches content from Google Docs and generates beautiful static HTML.
 * Generates comprehensive Atom feed (feed.xml) with ALL site content.
 * 
 * Feed Features (beyond IndieWeb POSSE):
 * - Full HTML content in entries (not just summaries)
 * - All static and generated pages included
 * - Rich metadata extraction from HTML
 * - Intelligent categorization and tagging
 * - Related content discovery and linking
 * - Media enclosures for images
 * - Comprehensive author information
 * - RFC 4287 compliant with extensions
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
const crypto = require('crypto');

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
    uri: 'https://raeez.com',
    bio: 'Managing Partner at Momentum. Building programmable institutions. Former Stripe founding team. Mathematician.',
    affiliations: [
      { name: 'Momentum', uri: 'https://momentum.inc' },
      { name: 'Mass Protocol', uri: 'https://mass.money' },
      { name: 'Perimeter Institute', uri: 'https://perimeterinstitute.ca' }
    ]
  },
  categories: {
    infrastructure: { label: 'Infrastructure', description: 'Programmable institutions, jurisdictional infrastructure, and regulatory primitives' },
    'built-environment': { label: 'Built Environment', description: 'Smart buildings, prefabricated construction, and physical infrastructure' },
    mathematics: { label: 'Mathematics', description: 'Arithmetic geometry, quantum field theory, and mathematical physics' },
    research: { label: 'Research', description: 'Academic research and theoretical foundations' },
    personal: { label: 'Personal', description: 'Essays, reflections, and personal writing' },
    hidden: { label: 'Background', description: 'Context and background materials' }
  }
};

// Apps Script URL (your existing one)
const APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwap-GYIRky-iOioo_7IaA0VvW8t_i1lXNesPlLT-hcGsJxQUeb93YR_t466iVw8wpdBQ/exec';

// Ensure directories exist
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
if (!fs.existsSync(CACHE_DIR)) fs.mkdirSync(CACHE_DIR, { recursive: true });

/**
 * Escape XML special characters
 */
function escapeXml(unsafe) {
  if (!unsafe) return '';
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

/**
 * Generate content hash for update detection
 */
function generateContentHash(content) {
  return crypto.createHash('sha256').update(content).digest('hex').substring(0, 16);
}

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
 */
function isTocEntry(element) {
  const link = element.querySelector('a[href^="#"]');
  if (!link) return false;
  
  const text = element.textContent.trim();
  
  if (!/\d+\s*$/.test(text)) return false;
  if (text.length > 120) return false;
  
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
 */
function wrapTableOfContents(container, contentDoc) {
  const allElements = Array.from(container.querySelectorAll('h1, h2, h3, h4, h5, h6, p'));
  
  let tocHeading = null;
  let tocHeadingIndex = -1;
  let tocEntries = [];
  
  for (let i = 0; i < allElements.length; i++) {
    const el = allElements[i];
    if (isTocHeading(el.textContent)) {
      tocHeading = el;
      tocHeadingIndex = i;
      break;
    }
  }
  
  if (tocHeading) {
    for (let i = tocHeadingIndex + 1; i < allElements.length; i++) {
      const el = allElements[i];
      if (isTocEntry(el)) {
        tocEntries.push(el);
      } else if (tocEntries.length > 0) {
        break;
      }
    }
  }
  
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
        if (consecutiveEntries.length >= 3 && consecutiveEntries.length > bestRun.length) {
          bestRun = [...consecutiveEntries];
          bestRunStart = currentRunStart;
        }
        consecutiveEntries = [];
        currentRunStart = -1;
      }
    }
    
    if (consecutiveEntries.length >= 3 && consecutiveEntries.length > bestRun.length) {
      bestRun = consecutiveEntries;
      bestRunStart = currentRunStart;
    }
    
    if (bestRun.length >= 3) {
      tocEntries = bestRun;
      tocHeading = allElements[bestRunStart - 1];
    }
  }
  
  if (tocEntries.length >= 3) {
    const tocContainer = contentDoc.createElement('div');
    tocContainer.className = 'toc';
    
    if (tocHeading) {
      const clonedHeading = tocHeading.cloneNode(true);
      tocContainer.appendChild(clonedHeading);
      tocHeading.remove();
    }
    
    tocEntries.forEach(entry => {
      const clonedEntry = entry.cloneNode(true);
      tocContainer.appendChild(clonedEntry);
      entry.remove();
    });
    
    const firstRemainingElement = container.querySelector('h1, h2, h3, h4, h5, h6, p');
    if (firstRemainingElement) {
      firstRemainingElement.parentNode.insertBefore(tocContainer, firstRemainingElement);
    } else {
      container.appendChild(tocContainer);
    }
    
    return tocContainer;
  }
  
  return null;
}

/**
 * Clean and transform Google Docs HTML
 */
function cleanGoogleDocsHtml(rawHtml, filterPatterns = []) {
  const dom = new JSDOM(rawHtml);
  const doc = dom.window.document;
  
  // Remove unwanted elements
  doc.querySelectorAll('style, script, meta, link').forEach(el => el.remove());
  
  // Get body content
  const body = doc.querySelector('body');
  if (!body) return '';
  
  // Apply filter patterns
  filterPatterns.forEach(pattern => {
    body.querySelectorAll('*').forEach(el => {
      if (pattern.test(el.textContent)) {
        el.remove();
      }
    });
  });
  
  // Clean up Google Docs artifacts
  body.querySelectorAll('[id^="h."], [id^="id."]').forEach(el => {
    el.removeAttribute('id');
  });
  
  // Wrap TOC
  wrapTableOfContents(body, doc);
  
  return body.innerHTML;
}

/**
 * Apply template to content
 */
function applyTemplate(doc, content) {
  let metaHtml = doc.meta;
  
  if (doc.metaLink) {
    metaHtml += ` <a href="${doc.metaLink.url}">${doc.metaLink.text}</a>`;
  }
  
  return template
    .replace(/\{\{title\}\}/g, doc.title)
    .replace(/\{\{subtitle\}\}/g, doc.subtitle || '')
    .replace(/\{\{description\}\}/g, doc.description)
    .replace(/\{\{slug\}\}/g, doc.slug)
    .replace(/\{\{metaHtml\}\}/g, metaHtml)
    .replace(/\{\{content\}\}/g, content);
}

/**
 * Parse date from various formats
 */
function parseDateFromMeta(meta) {
  const months = {
    'january': '01', 'february': '02', 'march': '03', 'april': '04',
    'may': '05', 'june': '06', 'july': '07', 'august': '08',
    'september': '09', 'october': '10', 'november': '11', 'december': '12'
  };
  
  const monthYearMatch = meta.match(/\b(january|february|march|april|may|june|july|august|september|october|november|december)\s*,?\s*(\d{4})\b/i);
  
  if (monthYearMatch) {
    const month = months[monthYearMatch[1].toLowerCase()];
    const year = monthYearMatch[2];
    return `${year}-${month}-15T00:00:00Z`;
  }
  
  return new Date().toISOString();
}

/**
 * Extract metadata from existing HTML file
 */
function extractMetadataFromHtml(filepath, filename) {
  try {
    const html = fs.readFileSync(filepath, 'utf8');
    const dom = new JSDOM(html);
    const doc = dom.window.document;
    
    // Extract title
    const titleEl = doc.querySelector('title');
    let title = titleEl ? titleEl.textContent.replace(' — Raeez Lorgat', '').trim() : filename.replace('.html', '');
    
    // Try to get better title from article
    const articleTitle = doc.querySelector('.article-title, h1.page-title, h1');
    if (articleTitle) {
      title = articleTitle.textContent.trim();
    }
    
    // Extract subtitle
    let subtitle = '';
    const subtitleEl = doc.querySelector('.article-subtitle, .tagline, meta[property="og:description"]');
    if (subtitleEl) {
      subtitle = subtitleEl.textContent || subtitleEl.getAttribute('content') || '';
    }
    
    // Extract description
    let description = '';
    const descEl = doc.querySelector('meta[name="description"]');
    if (descEl) {
      description = descEl.getAttribute('content') || '';
    }
    
    // Extract date
    let date = null;
    const dateEl = doc.querySelector('.article-meta, time, meta[property="article:published_time"]');
    if (dateEl) {
      const dateText = dateEl.textContent || dateEl.getAttribute('content') || '';
      date = parseDateFromMeta(dateText);
    }
    
    // Determine modification time from file
    const stats = fs.statSync(filepath);
    const modifiedDate = stats.mtime.toISOString();
    
    // Extract full content for feed
    const articleBody = doc.querySelector('.article-body, .beats, main, article');
    let content = '';
    if (articleBody) {
      // Clean up content for feed
      const clone = articleBody.cloneNode(true);
      // Remove navigation and footer elements
      clone.querySelectorAll('nav, footer, .back-nav, .footer-nav').forEach(el => el.remove());
      content = clone.innerHTML;
    }
    
    // Extract images
    const images = [];
    doc.querySelectorAll('img').forEach(img => {
      const src = img.getAttribute('src');
      const alt = img.getAttribute('alt');
      if (src && src.startsWith('http')) {
        images.push({ url: src, alt: alt || '' });
      }
    });
    
    // Categorize based on content and filename
    const categories = categorizeContent(filename, title, content);
    
    return {
      slug: filename.replace('.html', ''),
      title,
      subtitle,
      description,
      date: date || modifiedDate,
      modified: modifiedDate,
      content,
      categories,
      images,
      hash: generateContentHash(content)
    };
  } catch (error) {
    console.error(`  Error extracting metadata from ${filename}: ${error.message}`);
    return null;
  }
}

/**
 * Intelligent categorization based on content analysis
 */
function categorizeContent(filename, title, content) {
  const categories = [];
  const slug = filename.replace('.html', '').toLowerCase();
  const combined = (title + ' ' + content).toLowerCase();
  
  // Infrastructure keywords
  if (combined.match(/\b(programmable|infrastructure|institution|protocol|jurisdiction|compliance|smart asset|mass|momentum|sez|special economic zone)\b/i)) {
    categories.push('infrastructure');
  }
  
  // Built environment keywords
  if (combined.match(/\b(building|construction|prefabricated|archai|homeos|smart building|built environment|architecture)\b/i)) {
    categories.push('built-environment');
  }
  
  // Mathematics keywords
  if (combined.match(/\b(theorem|algebra|geometry|topology|cohomology|quantum field theory|manifold|proof|lemma)\b/i)) {
    categories.push('mathematics');
  }
  
  // Research keywords
  if (combined.match(/\b(research|laboratory|licc|sensoria|coordination|paper|study)\b/i)) {
    categories.push('research');
  }
  
  // Hidden/background pages
  if (['devfinance', 'beauty', 'about', 'experience'].includes(slug)) {
    categories.push('hidden');
  }
  
  // Personal writing
  if (['beauty', 'about', 'devfinance'].includes(slug)) {
    categories.push('personal');
  }
  
  // Default to infrastructure if no category found
  if (categories.length === 0) {
    categories.push('infrastructure');
  }
  
  return categories;
}

/**
 * Discover all HTML files in output directory
 */
function discoverAllContent() {
  const files = fs.readdirSync(OUTPUT_DIR);
  const htmlFiles = files.filter(f => f.endsWith('.html') && f !== 'template.html');
  
  const allContent = [];
  
  for (const file of htmlFiles) {
    const filepath = path.join(OUTPUT_DIR, file);
    const metadata = extractMetadataFromHtml(filepath, file);
    
    if (metadata) {
      allContent.push(metadata);
    }
  }
  
  return allContent;
}

/**
 * Determine primary category for an entry
 */
function getPrimaryCategory(categories) {
  const priority = ['infrastructure', 'built-environment', 'mathematics', 'research', 'personal', 'hidden'];
  
  for (const cat of priority) {
    if (categories.includes(cat)) {
      return cat;
    }
  }
  
  return 'infrastructure';
}

/**
 * Find related content based on category overlap and keywords
 */
function findRelatedContent(entry, allContent) {
  const related = [];
  
  for (const other of allContent) {
    if (other.slug === entry.slug) continue;
    
    // Check category overlap
    const sharedCategories = entry.categories.filter(c => other.categories.includes(c));
    if (sharedCategories.length > 0) {
      related.push({
        slug: other.slug,
        title: other.title,
        score: sharedCategories.length
      });
    }
  }
  
  // Sort by score and return top 5
  return related.sort((a, b) => b.score - a.score).slice(0, 5);
}

/**
 * Generate comprehensive Atom feed with all site content
 */
function generateComprehensiveAtomFeed(allContent) {
  const now = new Date().toISOString();
  
  // Sort by date (newest first)
  const sortedContent = [...allContent].sort((a, b) => {
    const dateA = new Date(a.date || a.modified);
    const dateB = new Date(b.date || b.modified);
    return dateB - dateA;
  });
  
  const lastUpdated = sortedContent.length > 0 
    ? (sortedContent[0].date || sortedContent[0].modified)
    : now;
  
  let feed = `<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:content="http://purl.org/rss/1.0/modules/content/"
      xmlns:media="http://search.yahoo.com/mrss/">
  
  <!-- Site Metadata -->
  <title>${escapeXml(SITE_CONFIG.title)}</title>
  <subtitle type="text">${escapeXml(SITE_CONFIG.subtitle)}</subtitle>
  <link href="${SITE_CONFIG.url}/feed.xml" rel="self" type="application/atom+xml"/>
  <link href="${SITE_CONFIG.url}/" rel="alternate" type="text/html"/>
  <link href="${SITE_CONFIG.url}/writing.html" rel="alternate" type="text/html" title="All Writing"/>
  <id>${SITE_CONFIG.url}/</id>
  <updated>${lastUpdated}</updated>
  
  <!-- Author Information -->
  <author>
    <name>${escapeXml(SITE_CONFIG.author.name)}</name>
    <email>${SITE_CONFIG.author.email}</email>
    <uri>${SITE_CONFIG.author.uri}</uri>
  </author>
  
  <!-- Additional Metadata -->
  <rights>© ${new Date().getFullYear()} ${escapeXml(SITE_CONFIG.author.name)}. All rights reserved.</rights>
  <icon>${SITE_CONFIG.url}/favicon.ico</icon>
  <logo>${SITE_CONFIG.url}/favicon.ico</logo>
  <generator uri="https://github.com/raeez/site-builder" version="2.0">Raeez Comprehensive Site Builder</generator>
  
  <!-- Category Definitions -->
`;

  // Add category definitions
  Object.entries(SITE_CONFIG.categories).forEach(([term, info]) => {
    feed += `  <category term="${term}" label="${info.label}" scheme="${SITE_CONFIG.url}/categories/"/>\n`;
  });
  
  feed += '\n';
  
  // Add entries
  sortedContent.forEach(entry => {
    const publishDate = entry.date || entry.modified;
    const updateDate = entry.modified || entry.date;
    const entryUrl = `${SITE_CONFIG.url}/${entry.slug}.html`;
    const primaryCategory = getPrimaryCategory(entry.categories);
    const related = findRelatedContent(entry, allContent);
    
    feed += `  <!-- Entry: ${entry.slug} -->\n`;
    feed += `  <entry>\n`;
    feed += `    <title type="text">${escapeXml(entry.title)}</title>\n`;
    feed += `    <link href="${entryUrl}" rel="alternate" type="text/html"/>\n`;
    feed += `    <id>${entryUrl}</id>\n`;
    feed += `    <published>${publishDate}</published>\n`;
    feed += `    <updated>${updateDate}</updated>\n`;
    
    // Author
    feed += `    <author>\n`;
    feed += `      <name>${escapeXml(SITE_CONFIG.author.name)}</name>\n`;
    feed += `      <email>${SITE_CONFIG.author.email}</email>\n`;
    feed += `      <uri>${SITE_CONFIG.author.uri}</uri>\n`;
    feed += `    </author>\n`;
    
    // Summary
    if (entry.description) {
      feed += `    <summary type="text">${escapeXml(entry.description)}</summary>\n`;
    }
    
    // Categories
    entry.categories.forEach(cat => {
      const catInfo = SITE_CONFIG.categories[cat];
      if (catInfo) {
        feed += `    <category term="${cat}" label="${catInfo.label}" scheme="${SITE_CONFIG.url}/categories/"/>\n`;
      }
    });
    
    // Full content (beyond basic POSSE)
    if (entry.content) {
      const contentHtml = `<div class="feed-content">
  <p><em>${escapeXml(entry.subtitle || entry.description || '')}</em></p>
  ${entry.content}
  <hr/>
  <p><a href="${entryUrl}">Read the full article on raeez.com →</a></p>
</div>`;
      
      feed += `    <content type="html"><![CDATA[${contentHtml}]]></content>\n`;
    }
    
    // Media attachments
    if (entry.images && entry.images.length > 0) {
      entry.images.forEach(img => {
        feed += `    <link href="${escapeXml(img.url)}" rel="enclosure" type="image/*" title="${escapeXml(img.alt)}"/>\n`;
      });
    }
    
    // Related content links
    related.forEach(rel => {
      const relUrl = `${SITE_CONFIG.url}/${rel.slug}.html`;
      feed += `    <link href="${relUrl}" rel="related" type="text/html" title="${escapeXml(rel.title)}"/>\n`;
    });
    
    // Content hash for change detection
    feed += `    <dc:identifier>urn:sha256:${entry.hash}</dc:identifier>\n`;
    
    feed += `  </entry>\n\n`;
  });

  feed += `</feed>
`;

  return feed;
}

/**
 * Determine category based on document slug/content (for docs.config.js documents)
 */
function getDocCategory(doc) {
  const slug = doc.slug.toLowerCase();
  
  if (['smart-buildings', 'prefabricated-construction', 'archai'].includes(slug)) {
    return 'built-environment';
  }
  
  return 'infrastructure';
}

/**
 * Build a single document
 */
async function buildDocument(doc, options = {}) {
  console.log(`\n📄 ${doc.slug}`);
  
  try {
    const rawHtml = await getDocContent(doc, options);
    
    console.log(`  Cleaning HTML...`);
    const cleanedContent = cleanGoogleDocsHtml(rawHtml, doc.filterPatterns || []);
    
    console.log(`  Applying template...`);
    const finalHtml = applyTemplate(doc, cleanedContent);
    
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
  console.log(`\nBuilding ${docs.length} documents from Google Docs...`);
  
  let success = 0;
  let failed = 0;
  
  for (const doc of docs) {
    const result = await buildDocument(doc, options);
    if (result) {
      success++;
    } else {
      failed++;
    }
  }
  
  console.log('\n════════════════════════════════════════════');
  console.log(`  ✓ ${success} built   ✗ ${failed} failed`);
  console.log('════════════════════════════════════════════');
  
  // Generate comprehensive feed
  console.log('\n📡 Generating comprehensive Atom feed...');
  console.log('   Discovering all site content...');
  
  try {
    const allContent = discoverAllContent();
    console.log(`   Found ${allContent.length} pages total`);
    
    const feedXml = generateComprehensiveAtomFeed(allContent);
    const feedPath = path.join(OUTPUT_DIR, 'feed.xml');
    fs.writeFileSync(feedPath, feedXml);
    
    console.log(`   ✓ dist/feed.xml (${allContent.length} entries)`);
    console.log('   Features:');
    console.log('     • Full HTML content in entries');
    console.log('     • All static and generated pages');
    console.log('     • Rich metadata and categorization');
    console.log('     • Related content discovery');
    console.log('     • Media enclosures');
    console.log('     • Content versioning via hashes');
  } catch (error) {
    console.error(`  ✗ Feed generation failed: ${error.message}`);
  }
  
  console.log('\n════════════════════════════════════════════');
  console.log('  Build complete!');
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
    
    // Regenerate comprehensive feed
    console.log('\n📡 Regenerating comprehensive Atom feed...');
    const allContent = discoverAllContent();
    const feedXml = generateComprehensiveAtomFeed(allContent);
    const feedPath = path.join(OUTPUT_DIR, 'feed.xml');
    fs.writeFileSync(feedPath, feedXml);
    console.log(`  ✓ dist/feed.xml (${allContent.length} entries)`);
    
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
