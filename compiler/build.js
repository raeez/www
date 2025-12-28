#!/usr/bin/env node

/**
 * Static Site Generator for Raeez's Research Papers
 *
 * Fetches content from Google Docs and generates beautiful static HTML.
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
 * Detect and wrap Table of Contents in a styled container
 */
function wrapTableOfContents(container, contentDoc) {
  // Find TOC heading
  const headings = container.querySelectorAll('h1, h2, h3');
  let tocHeading = null;

  for (const h of headings) {
    if (h.textContent.trim().toUpperCase().includes('TABLE OF CONTENTS') ||
        h.textContent.trim().toUpperCase() === 'CONTENTS') {
      tocHeading = h;
      break;
    }
  }

  if (!tocHeading) return;

  // Collect TOC entries (paragraphs with internal links following the heading)
  const tocEntries = [];
  let sibling = tocHeading.nextElementSibling;

  while (sibling) {
    const link = sibling.querySelector('a[href^="#"]');
    if (!link) break; // End of TOC
    tocEntries.push(sibling);
    sibling = sibling.nextElementSibling;
  }

  if (tocEntries.length === 0) return;

  // Create TOC wrapper
  const tocNav = contentDoc.createElement('nav');
  tocNav.className = 'toc';
  tocNav.setAttribute('aria-label', 'Table of Contents');

  // Move heading into nav
  tocHeading.className = 'toc-title';
  tocNav.appendChild(tocHeading.cloneNode(true));

  // Create list
  const tocList = contentDoc.createElement('ul');
  tocList.className = 'toc-list';

  tocEntries.forEach(entry => {
    const li = contentDoc.createElement('li');
    const link = entry.querySelector('a');
    const text = link.textContent.trim();

    // Detect indentation level from numbering (1.1, 1.1.1, etc.)
    const match = text.match(/^(\d+\.)+/);
    if (match) {
      const depth = (match[0].match(/\./g) || []).length;
      li.className = `toc-level-${Math.min(depth, 3)}`;
    }

    li.appendChild(link.cloneNode(true));
    tocList.appendChild(li);
    entry.remove();
  });

  tocNav.appendChild(tocList);
  tocHeading.replaceWith(tocNav);
}

/**
 * Clean and transform Google Docs HTML into clean article content
 */
function cleanGoogleDocsHtml(rawHtml, filterPatterns) {
  const dom = new JSDOM(rawHtml);
  const doc = dom.window.document;

  // Remove Google Docs cruft
  doc.querySelectorAll('style, script, meta, link').forEach(el => el.remove());

  // Get the body content
  const body = doc.body;
  if (!body) return '';

  // Parse content
  const contentDom = new JSDOM(`<div id="content">${body.innerHTML}</div>`);
  const contentDoc = contentDom.window.document;
  const container = contentDoc.getElementById('content');

  // Remove elements matching filter patterns (already in header)
  const elements = container.querySelectorAll('p, h1, h2, h3, h4, span');
  let skipCount = 0;
  const maxSkip = filterPatterns.length + 3;

  elements.forEach(el => {
    if (skipCount >= maxSkip) return;

    const text = el.textContent.trim().toUpperCase();
    for (const pattern of filterPatterns) {
      if (text.includes(pattern.toUpperCase())) {
        const parent = el.parentElement;
        el.remove();
        if (parent && parent.textContent.trim() === '') {
          parent.remove();
        }
        skipCount++;
        break;
      }
    }
  });

  // Wrap Table of Contents
  wrapTableOfContents(container, contentDoc);


  // Clean up styles and classes
  container.querySelectorAll('*').forEach(el => {
    el.removeAttribute('class');
      // Preserve IDs on headings (for TOC links)
    //
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

  for (const doc of docs) {
    const result = await buildDocument(doc, options);
    if (result) success++;
    else failed++;
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
