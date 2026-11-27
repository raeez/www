'use strict';

const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('/Users/raeez/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const [address, bindingFile, auditFile] = process.argv.slice(2);
const origin = new URL(address).origin;
assert.match(origin, /^http:\/\/127\.0\.0\.1:\d+$/);
const binding = JSON.parse(fs.readFileSync(bindingFile, 'utf8'));
const audit = JSON.parse(fs.readFileSync(auditFile, 'utf8'));
const pin = (value) => createHash('sha256').update(value).digest('hex');
const scratch = path.join(__dirname, 'final-dom-browser-work');
fs.mkdirSync(scratch, { recursive: true });
process.env.TMPDIR = scratch;

async function main() {
  const browser = await chromium.launch({
    executablePath: '/Users/raeez/Library/Caches/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-mac-arm64/chrome-headless-shell',
    headless: true, downloadsPath: scratch, tracesDir: scratch, args: ['--disable-background-networking']
  });
  try {
    const context = await browser.newContext({
      viewport: { width: 1440, height: 1000 },
      colorScheme: 'light', reducedMotion: 'reduce', serviceWorkers: 'block'
    });
    await context.route('**/*', (route) => new URL(route.request().url()).origin === origin ? route.continue() : route.abort());
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', (error) => errors.push(error.message));
    const response = await page.goto(address, { waitUntil: 'load', timeout: 60000 });
    assert.ok(response?.ok());
    assert.equal(pin(await response.body()), binding.mounted_release_html.sha256);
    await page.locator('#book-abstract').waitFor({ state: 'visible' });
    await page.evaluate(async () => {
      await document.fonts.ready;
      await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    });
    const content = await page.locator('.mg-introduction-text').evaluate((node) => node.outerHTML);
    const inlineStyles = await page.locator('style').evaluateAll((nodes) => nodes.map((node) => node.textContent));
    const destinations = await page.evaluate((refs) => refs.map(({ fragment }) => ({
      fragment, count: document.querySelectorAll('[id="' + CSS.escape(decodeURIComponent(fragment.slice(1))) + '"]').length,
    })), audit.portableReferences);
    assert.equal(pin(content), audit.printContentSha);
    assert.equal(pin(content), audit.contentSha);
    assert.deepEqual(inlineStyles.map(pin), audit.inlineStyleHashes);
    assert.ok(destinations.every(({ count }) => count === 1));
    assert.deepEqual(errors, []);
    console.log(JSON.stringify({
      status: 'PASS',
      mounted_final_html_sha256: binding.mounted_release_html.sha256,
      expanded_final_chromium_outerhtml_sha256: pin(content),
      printed_chromium_outerhtml_sha256: audit.printContentSha,
      exact_inline_styles_sha256: inlineStyles.map(pin),
      unique_portable_link_destinations: new Set(destinations.map(({ fragment }) => fragment)).size,
      pdf_sha256: audit.pdfSha,
    }, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
