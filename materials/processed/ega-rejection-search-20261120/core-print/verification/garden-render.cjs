'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { createHash } = require('node:crypto');
const { chromium } = require('/Users/raeez/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const [url, expectedSha, run, mode = 'screen'] = process.argv.slice(2);
if (!url || !/^[a-f0-9]{64}$/.test(expectedSha) || !/^[a-z0-9-]+$/.test(run) || !['screen', 'print'].includes(mode)) {
  throw new Error('Usage: node garden-render.cjs URL SHA256 RUN screen|print');
}

const origin = new URL(url).origin;
if (!/^http:\/\/(127\.0\.0\.1|localhost):[0-9]+$/.test(origin)) {
  throw new Error('Use the exact local preview URL');
}
const review = path.resolve(__dirname, '..');
const output = path.join(__dirname, run);
const scratch = path.join(output, 'browser-work');
fs.mkdirSync(scratch, { recursive: true });
process.env.TMPDIR = scratch;
const digest = (value) => createHash('sha256').update(value).digest('hex');

const paperTitle = 'Chiral Quantum Groups and Holography — Introduction.pdf';

async function open(context) {
  await context.route('**/*', (route) => {
    const request = new URL(route.request().url());
    return request.origin === origin ? route.continue() : route.abort();
  });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', (error) => errors.push(error.message));
  const response = await page.goto(url, { waitUntil: 'load' });
  if (!response?.ok() || digest(await response.body()) !== expectedSha) {
    throw new Error('Preview loaded a different HTML artifact');
  }
  await page.locator('#book-abstract').waitFor({ state: 'visible' });
  await page.evaluate(async () => {
    await document.fonts.ready;
    await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  });
  return { page, errors };
}

async function inspect(page) {
  return page.evaluate(async () => {
    const opening = document.querySelector('#book-abstract');
    const body = opening.querySelector('.mg-introduction-text');
    if (!body || document.querySelectorAll('#book-abstract').length !== 1) {
      throw new Error('New introduction boundary is ambiguous');
    }
    const box = (node) => {
      const rect = node.getBoundingClientRect();
      return { left: rect.left, right: rect.right, width: rect.width, height: rect.height, scrollWidth: node.scrollWidth, clientWidth: node.clientWidth };
    };
    const math = [...body.querySelectorAll('math')].map((node) => ({
      display: node.getAttribute('display') === 'block',
      tex: node.querySelector('annotation[encoding="application/x-tex"]')?.textContent,
      box: box(node.querySelector('semantics')?.firstElementChild ?? node),
      viewport: box(node.closest('.math-display,.mg-display,.math-long') ?? node),
    }));
    const previous = opening.nextElementSibling;
    const legacy = {
      classes: previous?.className,
      paragraphs: previous?.querySelectorAll(':scope > p').length,
      figure: previous?.querySelector(':scope > figure')?.id,
    };
    const links = [...opening.querySelectorAll('a[href]')].map((anchor) => {
      const href = anchor.getAttribute('href');
      const id = href.startsWith('#') ? decodeURIComponent(href.slice(1)) : null;
      const matches = id ? document.querySelectorAll('[id="' + CSS.escape(id) + '"]').length : null;
      return { href, matches, text: anchor.textContent.trim() };
    });
    const hash = async (value) => {
      const bytes = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value));
      return Array.from(new Uint8Array(bytes), (byte) => byte.toString(16).padStart(2, '0')).join('');
    };
    return {
      contentSha: await hash(body.outerHTML),
      inlineStyleHashes: await Promise.all([...document.querySelectorAll('style')].map((node) => hash(node.textContent))),
      title: document.title,
      openingTitle: opening.querySelector('h1,h2')?.textContent.trim(),
      headings: [...body.querySelectorAll('h1,h2,h3,h4,h5,h6')].map((h) => ({
        heading: h.textContent.trim(), id: h.id, level: h.tagName,
      })),
      paragraphs: body.querySelectorAll('p').length,
      lastParagraph: [...body.querySelectorAll('p')].at(-1)?.innerText.trim(),
      math,
      mathOverflow: math.filter(({ box: b, viewport }) => b.left < -1 || b.right > innerWidth + 1
        || viewport.scrollWidth > viewport.clientWidth + 1),
      mathErrors: body.querySelectorAll('merror').length,
      missingImages: [...body.querySelectorAll('img')].filter((img) => !img.complete || !img.naturalWidth)
        .map((img) => img.alt),
      links,
      legacy,
      width: { viewport: innerWidth, document: document.documentElement.scrollWidth },
    };
  });
}

async function screens(browser) {
  for (const [label, width, height] of [
    ['desktop', 1440, 1000], ['mobile', 390, 844], ['narrow', 320, 800],
  ]) {
    const context = await browser.newContext({
      viewport: { width, height }, colorScheme: 'light', reducedMotion: 'reduce', serviceWorkers: 'block',
    });
    try {
      const { page, errors } = await open(context);
      const evidence = await inspect(page);
      const section = page.locator('#book-abstract');
      await section.evaluate((node) => { node.scrollIntoView({ block: 'start' }); });
      await page.screenshot({ path: path.join(output, label + '-opening.png') });
      await section.locator('.mg-introduction-text p').last().evaluate((node) => node.scrollIntoView({ block: 'center' }));
      await page.screenshot({ path: path.join(output, label + '-conclusion.png') });
      fs.writeFileSync(path.join(output, label + '.json'), JSON.stringify({ sourceSha: expectedSha, errors, ...evidence }, null, 2) + '\n');
      console.log(JSON.stringify({ label, width: evidence.width, mathOverflow: evidence.mathOverflow.length,
        sectionHeadings: evidence.headings.length, equations: evidence.math.length, errors, legacy: evidence.legacy }));
    } finally {
      await context.close();
    }
  }
}

async function print(browser) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 1000 },
    colorScheme: 'light', reducedMotion: 'reduce', serviceWorkers: 'block',
  });
  try {
    const { page, errors } = await open(context);
    const evidence = await inspect(page);
    await page.emulateMedia({ media: 'print', colorScheme: 'light' });
    const snapshot = await page.evaluate(async () => {
      const opening = document.querySelector('#book-abstract');
      const content = opening.querySelector('.mg-introduction-text');
      const saved = opening.outerHTML;
      const styles = () => [...document.querySelectorAll('style')].map((node) => node.textContent);
      const styleText = styles();
      if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
      for (let node = opening; node !== document.body; node = node.parentElement) {
        for (const sibling of [...node.parentElement.children]) {
          if (sibling !== node) sibling.remove();
        }
      }
      await document.fonts.ready;
      if (opening.outerHTML !== saved || JSON.stringify(styles()) !== JSON.stringify(styleText)) {
        throw new Error('The section or author styles were altered during print isolation');
      }
      if (document.querySelector('.mg-front-intro') || document.querySelector('.mg-chapter')) {
        throw new Error('Print boundary includes a separately retained region');
      }
      const structuralText = (root) => {
        const clone = root.cloneNode(true);
        clone.querySelectorAll('math,script,style,svg').forEach((node) => node.replaceWith(document.createTextNode(' ')));
        const walker = document.createTreeWalker(clone, NodeFilter.SHOW_TEXT);
        let node;
        const sections = [];
        while ((node = walker.nextNode())) sections.push(node.textContent.trim());
        return sections.filter(Boolean).join(' ');
      };
      const contentHtml = content.outerHTML;
      const retainedIds = new Set([...opening.querySelectorAll('[id]')].map((node) => node.id));
      const portableReferences = [];
      const canonical = document.querySelector('link[rel="canonical"]')?.href;
      if (canonical !== 'https://raeez.com/quantum-holography/') {
        throw new Error('Unexpected canonical book reference URL');
      }
      const signature = (anchor) => {
        const style = getComputedStyle(anchor);
        return JSON.stringify({
          rects: [...anchor.getClientRects()].map((rect) => rect.toJSON()),
          font: style.font, color: style.color, decoration: style.textDecoration,
          before: getComputedStyle(anchor, '::before').content,
          after: getComputedStyle(anchor, '::after').content,
        });
      };
      for (const anchor of content.querySelectorAll('a[href^="#"]')) {
        const fragment = anchor.getAttribute('href');
        if (retainedIds.has(decodeURIComponent(fragment.slice(1)))) continue;
        const before = signature(anchor);
        anchor.setAttribute('href', new URL(fragment, canonical).href);
        if (signature(anchor) !== before) throw new Error('A portable link changed print appearance');
        portableReferences.push({ text: anchor.textContent.trim(), fragment, url: anchor.href });
      }
      return {
        html: saved, contentHtml, styles: styleText, portableReferences,
        prose: structuralText(content),
        expectedEnding: structuralText([...opening.querySelectorAll('.mg-introduction-text p')].at(-1)),
        renderedTitle: document.title,
      };
    });
    const pdf = await page.pdf({
      path: path.join(review, paperTitle),
      format: 'A4',
      preferCSSPageSize: true,
      printBackground: true,
      displayHeaderFooter: false,
      tagged: true,
      outline: true,
      timeout: 60000,
    });
    fs.writeFileSync(path.join(output, 'print-audit.json'), JSON.stringify({
      sourceSha: expectedSha,
      printSectionSha: digest(snapshot.html),
      printContentSha: digest(snapshot.contentHtml),
      portableReferences: snapshot.portableReferences,
      pdfSha: digest(pdf),
      pdfBytes: pdf.length,
      prose: snapshot.prose,
      expectedEnding: snapshot.expectedEnding,
      renderedTitle: snapshot.renderedTitle,
      errors,
      ...evidence,
      inlineStyleHashes: snapshot.styles.map(digest),
    }, null, 2) + '\n');
    console.log(JSON.stringify({ path: path.join(review, paperTitle), sha256: digest(pdf),
      equations: evidence.math.length, paragraphs: evidence.paragraphs, sections: evidence.headings.length }));
  } finally {
    await context.close();
  }
}

async function main() {
  const browser = await chromium.launch({
    executablePath: '/Users/raeez/Library/Caches/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-mac-arm64/chrome-headless-shell',
    headless: true,
    downloadsPath: scratch,
    tracesDir: scratch,
    args: ['--disable-background-networking'],
  });
  try {
    await (mode === 'print' ? print(browser) : screens(browser));
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
