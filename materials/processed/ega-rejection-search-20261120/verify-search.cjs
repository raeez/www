'use strict';

const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const { createHash } = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const zlib = require('node:zlib');
const { JSDOM, VirtualConsole } = require('jsdom');

const baseline = '04dbd695741f1437957ff8951b87ef1d41d0f5b0';
const root = path.resolve(__dirname, '../../..');
const frozen = path.resolve(process.argv[2]);
const runtimeRoot = 'compiler/quantum-holography-status';
const variants = ['reader.js', 'reader-runtime/reader-book.js', 'reader-runtime/reader-companions.js'].map((name) => ({
  name,
  before: fs.readFileSync(path.join(frozen, 'source-tree', runtimeRoot, name), 'utf8'),
  after: fs.readFileSync(path.join(root, runtimeRoot, name), 'utf8')
}));
const hash = (bytes) => createHash('sha256').update(bytes).digest('hex');
const origin = 'http://127.0.0.1:41137/quantum-holography/';
const names = ['index.html', 'reference.html', 'atlas.html'];
const issued = (name) => execFileSync('git', ['--no-optional-locks', '-C', root, 'show',
  baseline + ':quantum-holography/' + name], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
const wrapper = 'window.QH_READER_INDEX = ';
const indexScript = (units) => wrapper + JSON.stringify({ units }) + ';\n';
const fields = ['bodyParts', 'titleParts', 'whereParts'];
const probes = [
  {
    id: 'ch04-passage-784b4e1fd421b3857233', query: 'Stokes multiplier', old: 'multiplier is 2iπa',
    tex: '2i\\sqrt{\\pi}\\,a', operator: 'msqrt', parts: ['π']
  },
  {
    id: 'ch04-passage-b5715fb385eb49c28afe', query: '\\frac{2\\pi i}{k}', old: 'exp⁡(2πik∑{a,b}⊂Sαaαb).',
    tex: '\\exp\\!\\left(\\frac{2\\pi i}{k}\\sum_{\\{a,b\\}\\subset S}\\alpha_a\\alpha_b\\right).',
    operator: 'mfrac', parts: ['2πi', 'k']
  }
];

function load(markup, page = 'index.html', units) {
  const errors = [];
  const console = new VirtualConsole();
  console.on('jsdomError', (error) => errors.push(error.message));
  const dom = new JSDOM(markup, {
    url: origin + page, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: console,
    beforeParse(window) {
      if (units) window.QH_READER_INDEX = { units };
      window.Element.prototype.scrollIntoView = function () {};
      window.scrollTo = function () {};
    }
  });
  return { dom, doc: dom.window.document, errors };
}

function exportUnits({ dom, doc }) {
  const event = new dom.window.CustomEvent('qh:reader-units', { detail: {} });
  doc.dispatchEvent(event);
  assert.ok(Array.isArray(event.detail.units));
  return JSON.parse(JSON.stringify(event.detail.units));
}

const project = (unit) => Object.fromEntries(Object.entries(unit).filter(([key]) => !fields.includes(key)));
const sizes = (s) => ({ bytes: Buffer.byteLength(s), gzipBytes: zlib.gzipSync(s).length, sha256: hash(s) });
const math = '<math><semantics><msubsup><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow>' +
  '<mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msubsup>' +
  '<annotation encoding="application/x-tex">{x+y}_{i+1}^{n-1}</annotation></semantics></math>';
const book = '<main data-reader><article id="ch01" data-chapter data-number="1"><h2>Fixture chapter</h2>' +
  '<section id="s" data-section><h3>Context ' + math + '</h3>' +
  '<p id="grouping"><strong>Grouping ' + math + '</strong> Searchable prose and ' + math + '.</p>' +
  '<p id="plain">Careful reading in prose.</p></section></article>' +
  '<section id="g" data-reference><h2>Glossary</h2><dl><dt id="term">Words</dt>' +
  '<dd>First definition ' + math + '.</dd><dd>Second definition.</dd></dl></section></main>';
const companion = '<main data-reader data-reader-book="index.html"><section id="r" data-reference>' +
  '<h2>Reference fixture</h2><p>Unrelated material.</p></section></main>';
const pageMap = '<script type="application/json" id="reader-pages">' + JSON.stringify({
  book: 'index.html', title: 'Fixture', index: 'reader-index.js',
  pages: [{ href: 'reference.html', parts: [{ id: 'r', title: 'Reference fixture' }], ids: ['r'] }]
}) + '</script>';
const fixture = (body, script) => body + pageMap + '<script>' + script + '</script>';
const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function search({ doc, dom }, query, id) {
  if (doc.getElementById('reader-search').hidden) doc.querySelector('.reader-search-toggle').click();
  const input = doc.getElementById('reader-q');
  input.value = query;
  input.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
  for (let attempt = 0; attempt < 60; attempt++) {
    const hit = [...doc.querySelectorAll('.reader-hit-link')].find((a) => a.hash === '#' + id);
    if (hit && !doc.getElementById('reader-results').hidden) return hit;
    await pause(25);
  }
  throw new Error('Missing search result: ' + id + ' for ' + query);
}

async function checkFixtures(older, newer) {
  let shared;
  for (const variant of variants) {
    const before = load(fixture(book, variant.before));
    const after = load(fixture(book, variant.after));
    const units = exportUnits(after);
    assert.deepEqual(units.map(project), exportUnits(before), variant.name);
    if (shared) assert.deepEqual(units, shared, variant.name);
    shared = units;
    const plain = units.find((row) => row.id === 'plain');
    assert.ok(plain && !('bodyParts' in plain) && !('titleParts' in plain));
    assert.ok(units.find((row) => row.id === 'term').bodyParts.some(Array.isArray));
    assert.deepEqual(before.errors.concat(after.errors), []);
    before.dom.window.close();
    after.dom.window.close();
  }
  const old = load(fixture(companion, variants[2].before), 'reference.html', older);
  const newFixture = shared.map((unit) => ({ ...unit, page: 'index.html' }));
  const current = load(fixture(companion, variants[2].after), 'reference.html', [...newer, ...newFixture]);
  for (const probe of probes) {
    const previous = await search(old, probe.query, probe.id);
    const oldSnippet = previous.querySelector('.reader-hit-text');
    assert.ok(oldSnippet.textContent.includes(probe.old) && !oldSnippet.querySelector('math'));
    const hit = await search(current, probe.query, probe.id);
    const snippet = hit.querySelector('.reader-hit-text');
    assert.equal(hit.getAttribute('href'), previous.getAttribute('href'));
    const op = snippet.querySelector(probe.operator);
    assert.equal(op.namespaceURI, 'http://www.w3.org/1998/Math/MathML');
    assert.deepEqual([...op.children].map((el) => el.textContent), probe.parts);
    assert.equal(snippet.querySelector('annotation').textContent, probe.tex);
    const labelId = snippet.id + '-label';
    assert.ok((hit.getAttribute('aria-labelledby') + ' ' + hit.getAttribute('aria-describedby')).split(/\s+/).includes(labelId));
    assert.ok(current.doc.getElementById(labelId).textContent.includes(probe.tex));
    if (probe.operator === 'msqrt') assert.equal(snippet.querySelector('mark').textContent.toLowerCase(), 'stokes');
    if (probe.operator === 'mfrac') assert.ok(op.closest('.math-long'));
  }
  const group = await search(current, 'Searchable prose', 'grouping');
  for (const selector of ['.reader-hit-title', '.reader-hit-where', '.reader-hit-text']) {
    const script = group.querySelector(selector + ' msubsup');
    assert.deepEqual([...script.children].map((el) => el.textContent), ['x+y', 'i+1', 'n−1']);
  }
  const plain = await search(current, 'careful reading', 'plain');
  assert.equal(plain.querySelector('.reader-hit-text').textContent, 'Careful reading in prose.');
  assert.ok(plain.querySelector('mark'));
  const legacy = load(fixture(companion, variants[2].after), 'reference.html', older);
  const hit = await search(legacy, probes[0].query, probes[0].id);
  assert.equal(hit.querySelector('.reader-hit-text').textContent, 'Formula in source');
  assert.deepEqual(old.errors.concat(current.errors, legacy.errors), []);
  for (const session of [old, current, legacy]) session.dom.window.close();
}

function corpus(oldUnits) {
  const newer = [];
  const assets = {};
  const pages = {};
  const seen = new Set();
  let total = 0;
  let formulaBytes = 0;
  let exact = 0;
  for (const page of names) {
    const variant = variants[page === 'index.html' ? 1 : 2];
    const original = issued(page);
    assert.equal(original.split(variant.before.trim()).length, 2, page);
    assets[page] = original.replace(variant.before.trim(), () => variant.after.trim());
    const instrumented = variant.after.replace("  main.setAttribute('data-reader-on', '');",
      "  main.setAttribute('data-reader-on', '');\n  window.checkSnippet = readSnippet;");
    assert.notEqual(instrumented, variant.after);
    const markup = original.replace(variant.before.trim(), () => instrumented.trim());
    const session = load(markup, page);
    assert.equal(typeof session.dom.window.checkSnippet, 'function', page);
    const units = exportUnits(session).map((row) => ({ ...row, page }));
    assert.deepEqual(units.map(project), oldUnits.filter((row) => row.page === page), page);
    const here = new Set();
    for (const row of units) {
      for (const field of fields) {
        for (const part of row[field] || []) {
          if (!Array.isArray(part)) continue;
          here.add(part[0]); seen.add(part[0]); total++; formulaBytes += Buffer.byteLength(part[0]);
        }
      }
    }
    for (const formula of here) {
      const node = session.dom.window.checkSnippet([[formula, false]], '', false).firstElementChild;
      assert.ok(node && node.localName === 'math', formula.slice(0, 420));
      assert.equal(node.outerHTML, formula);
      exact++;
    }
    assert.deepEqual(session.errors, []);
    pages[page] = { units: units.length, uniqueMath: here.size };
    console.error(page + ': ' + units.length + ' units and ' + here.size + ' distinct formulas replayed');
    newer.push(...units);
    session.dom.window.close();
    if (global.gc) global.gc();
  }
  return { newer, assets, pages, formulaOccurrences: total, uniqueMath: seen.size, exactReadbacks: exact,
    formulaBytes, uniqueFormulaBytes: [...seen].reduce((sum, formula) => sum + Buffer.byteLength(formula), 0) };
}

function probeCorpus(oldUnits) {
  const assets = Object.fromEntries(names.map((page) => {
    const variant = variants[page === 'index.html' ? 1 : 2];
    return [page, issued(page).replace(variant.before.trim(), () => variant.after.trim())];
  }));
  const blocks = probes.map(({ id }) => {
    const exact = new RegExp('<([a-z]+)\\b[^>]*\\sid="' + id + '"[^>]*>[\\s\\S]*?</\\1>');
    return assets['index.html'].match(exact)[0];
  });
  const source = load(fixture('<main data-reader><article id="ch04" data-chapter data-number="4"><h2>Chapter four</h2>' +
    '<section data-section id="s"><h3>Factorization</h3>' + blocks.join('') + '</section></article></main>', variants[1].after));
  const byId = new Map(exportUnits(source).map((row) => [row.id, row.bodyParts]));
  source.dom.window.close();
  return {
    newer: oldUnits.map((row) => byId.has(row.id) ? { ...row, bodyParts: byId.get(row.id) } : row),
    assets,
    pages: {}
  };
}

async function chromiumChecks(assets, units) {
  const local = path.join(__dirname, 'browser-scratch');
  fs.mkdirSync(local, { recursive: true });
  for (const variable of ['TMPDIR', 'TMP', 'TEMP', 'XDG_CACHE_HOME']) process.env[variable] = local;
  const { chromium } = require('playwright');
  const profile = fs.mkdtempSync(path.join(local, 'profile-'));
  const context = await chromium.launchPersistentContext(profile, {
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: true, viewport: { width: 390, height: 844 },
    args: ['--disable-crash-reporter', '--disable-breakpad', '--disable-background-networking', '--no-first-run']
  });
  try {
    const data = indexScript(units);
    await context.route('**/*', (route) => {
      const url = new URL(route.request().url());
      if (!url.href.startsWith(origin)) return route.abort();
      const name = path.posix.basename(url.pathname);
      if (name === 'reader-index.js') return route.fulfill({ contentType: 'text/javascript', body: data });
      if (Object.hasOwn(assets, name)) return route.fulfill({ contentType: 'text/html', body: assets[name] });
      return route.fulfill({ status: 404 });
    });
    const page = context.pages()[0];
    const userAgent = await page.evaluate(() => navigator.userAgent);
    const errors = [];
    page.on('pageerror', (error) => errors.push(error.message));
    const cdp = await context.newCDPSession(page);
    await cdp.send('Accessibility.enable');
    const verified = [];
    for (const owner of ['reference.html', 'atlas.html']) {
      for (const probe of probes) {
        await page.goto(origin + owner + '?q=' + encodeURIComponent(probe.query), { waitUntil: 'domcontentloaded' });
        const selector = '.reader-hit-link[href="index.html#' + probe.id + '"]';
        const hit = page.locator(selector).first();
        await hit.waitFor({ timeout: 60000 });
        const branch = hit.locator('.reader-hit-text ' + probe.operator);
        assert.deepEqual(await branch.evaluate((n) => [...n.children].map((el) => el.textContent)), probe.parts);
        assert.equal(await hit.locator('.reader-hit-text math annotation').first().textContent(), probe.tex);
        const { root: doc } = await cdp.send('DOM.getDocument');
        const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: doc.nodeId, selector: selector + ' .reader-hit-text math' });
        const { nodes } = await cdp.send('Accessibility.getPartialAXTree', { nodeId, fetchRelatives: true });
        const mathNode = nodes.find((node) => !node.ignored && /^(math|mathmlmath)$/i.test(node.role?.value));
        assert.ok(mathNode, JSON.stringify(nodes.map((node) => node.role?.value)));
        const roles = [];
        const queue = [mathNode.nodeId];
        while (queue.length) {
          const { nodes: children } = await cdp.send('Accessibility.getChildAXNodes', { id: queue.shift() });
          for (const child of children) {
            if (!child.ignored) roles.push(child.role?.value);
            if (child.childIds?.length) queue.push(child.nodeId);
          }
        }
        const expectedRole = probe.operator === 'msqrt' ? /square.?root/i : /fraction/i;
        assert.ok(roles.some((role) => expectedRole.test(role)), JSON.stringify(roles));
        const accessibilityLinkName = nodes.find((node) => node.role?.value === 'link')?.name?.value;
        assert.ok(accessibilityLinkName?.includes(probe.tex), accessibilityLinkName);
        const box = await hit.locator('.reader-hit-text').evaluate((el) => {
          const wide = el.querySelector('.math-long');
          return wide ? { overflowX: getComputedStyle(wide).overflowX, width: wide.clientWidth, scrollWidth: wide.scrollWidth } : null;
        });
        if (probe.operator === 'mfrac') assert.ok(['auto', 'scroll'].includes(box.overflowX));
        await hit.focus();
        await hit.press('Enter');
        await page.waitForURL('**/index.html#' + probe.id);
        await page.goBack({ waitUntil: 'domcontentloaded' });
        await hit.waitFor({ timeout: 60000 });
        assert.equal(await page.locator('#reader-q').inputValue(), probe.query);
        verified.push({ owner, id: probe.id, accessibilityRoot: mathNode.role.value, accessibilityRoles: roles,
          accessibilityLinkName, box });
      }
    }
    assert.deepEqual(errors, []);
    return { userAgent, width: 390, verified };
  } finally {
    await context.close();
  }
}

async function main() {
  const original = issued('reader-index.js');
  assert.ok(original.startsWith(wrapper) && original.endsWith(';\n'));
  const old = JSON.parse(original.slice(wrapper.length, -2)).units;
  const quick = process.argv.includes('--probes-only');
  const { newer, assets, pages, ...counts } = quick ? probeCorpus(old) : corpus(old);
  const selected = (units) => units.filter(({ id }) => probes.some((probe) => probe.id === id));
  await checkFixtures(selected(old), selected(newer));
  const report = {
    baseline,
    status: 'PASS',
    sourcePins: Object.fromEntries(variants.map(({ name, before, after }) => [name, { before: hash(before), after: hash(after) }])),
    pages,
    index: quick ? undefined : { before: sizes(original), after: sizes(indexScript(newer)), ...counts },
    jsdom: { issuedFailures: probes.length, restored: probes.length, variants: variants.length,
      groupedSubscriptsAndSuperscripts: true, ordinaryProse: true, testedLegacy: true }
  };
  if (process.argv.includes('--browser')) report.chromium = await chromiumChecks(assets, newer);
  console.log(JSON.stringify(report, null, 2));
}

main().catch((error) => {
  console.error(error.stack);
  process.exitCode = 1;
});
