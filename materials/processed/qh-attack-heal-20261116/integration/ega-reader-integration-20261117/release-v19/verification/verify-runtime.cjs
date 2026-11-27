'use strict';

const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM, VirtualConsole, requestInterceptor } = require('jsdom');

const sourceIdentity = '3b57dd41a75dbc10438565925bffd4cd814d88075960c2bcfed0205a720bd2c0';
const root = path.dirname(__dirname);
const source = path.join(root, 'sources', sourceIdentity);
const build = path.join(root, 'builds', sourceIdentity);
const content = path.join(source, 'source-tree', 'content', 'quantum-holography-status');
const staged = JSON.parse(fs.readFileSync(path.join(root, 'STAGED.json')));
const authors = JSON.parse(fs.readFileSync(path.join(source, 'AUTHOR-PINS.json')));
const report = JSON.parse(fs.readFileSync(path.join(build, 'release-receipt.json')));
const base = 'https://research.momentum.inc/quantum-holography/';
const index = fs.readFileSync(path.join(build, 'release', 'reader-index.js'));
const pin = (body) => ({ sha256: createHash('sha256').update(body).digest('hex'), bytes: body.length });
const pageText = new Map(report.results.map(({ page }) => [page, fs.readFileSync(path.join(build, 'release', page))]));
assert.equal(staged.signature, sourceIdentity);
assert.deepEqual(staged.author_pins, authors);
for (const [file, sha] of Object.entries(authors)) assert.equal(pin(fs.readFileSync(path.join(content, file))).sha256, sha);
assert.equal(report.status, 'PASS');
assert.deepEqual(pin(index), report.outputIndex);
for (const { page, after } of report.results) assert.deepEqual(pin(pageText.get(page)), after);

function open(page, suffix) {
  const scrolls = [], departures = [], errors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', (error) => errors.push(error.message));
  const resources = { interceptors: [requestInterceptor((request) => request.url === base + 'reader-index.js' ?
    new Response(index, { headers: { 'Content-Type': 'application/javascript' } }) : new Response('', { status: 404 }))] };
  const dom = new JSDOM(pageText.get(page).toString(), {
    url: new URL(suffix, base).href, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole, resources,
    beforeParse(window) {
      window.Element.prototype.scrollIntoView = function () { scrolls.push(this.id); };
      window.scrollTo = function () {};
      window.scrollBy = function () {};
      window.addEventListener('qh:leave', (event) => {
        departures.push(JSON.parse(JSON.stringify(event.detail)));
        event.preventDefault();
      }, true);
    }
  });
  return { window: dom.window, doc: dom.window.document, scrolls, departures, errors };
}

async function session(page, suffix, check) {
  const state = open(page, suffix);
  try {
    const result = await check(state);
    assert.deepEqual(state.errors, [], suffix + ' emitted script errors');
    return result;
  } finally {
    state.window.close();
    await new Promise((resolve) => setImmediate(resolve));
    if (global.gc) global.gc();
  }
}

function navigate({ doc, window }, id) {
  const event = new window.CustomEvent('qh:navigate', { detail: { id }, cancelable: true });
  assert.equal(doc.dispatchEvent(event), false, 'reader did not handle ' + id);
  assert.equal(window.location.hash, '#' + id);
}

const norm = (text) => text.replace(/\s+/g, ' ').trim();
const predecessor = (doc) => doc.querySelector('.reader-notice[data-notice="predecessor"]');
const search = (query) => '?q=' + encodeURIComponent(query);
const headings = [
  ['chapters/04-factorization.md', 'ch04-sphere-binary-collision'],
  ['chapters/11-states-and-lines.md', 'ch11-sourced-affine-collar'],
  ['chapters/11-states-and-lines.md', 'ch11-classical-meridian-flux'],
  ['chapters/15-hall-and-compact.md', 'ch15-k3-prepared-cubic-probes']
].map(([file, id]) => {
  const suffix = ' {#' + id + '}';
  const lines = fs.readFileSync(path.join(content, file), 'utf8').split('\n')
    .filter((line) => line.startsWith('### ') && line.endsWith(suffix));
  assert.equal(lines.length, 1, file);
  return { page: 'index.html', id, title: lines[0].slice(4, -suffix.length) };
});
const newClaims = [
  'sphere-binary-higher-transport', 'sourced-affine-meridian-transfer', 'classical-affine-meridian-flux',
  'k3-prepared-cubic-probes', 'k3-null-lifts-and-pairwise-cubics'
];
const atlas = JSON.parse(fs.readFileSync(path.join(content, 'atlas.json')));
const claims = newClaims.map((claim) => {
  const matches = atlas.claims.filter(({ id }) => id === claim);
  assert.equal(matches.length, 1, claim);
  return { page: 'atlas.html', id: 'atlas-c-' + claim, claim, title: matches[0].title, grade: matches[0].status };
});

async function actualHit(state, query, row) {
  const field = state.doc.getElementById('reader-q');
  const href = row.page + '#' + row.id;
  const selector = '.reader-hit-link[href="' + href + '"]';
  const oldHit = field.value === query ? null : state.doc.querySelector(selector);
  if (field.value !== query) {
    field.value = query;
    field.dispatchEvent(new state.window.Event('input', { bubbles: true }));
  }
  let hit;
  for (let turn = 0; turn < 80 && !hit; turn++) {
    const updated = state.doc.querySelector(selector);
    if (updated !== oldHit) hit = updated;
    if (!hit) await new Promise((resolve) => setTimeout(resolve, 25));
  }
  assert.ok(hit, 'query ' + query + ' did not show ' + href);
  const previous = state.departures.length;
  hit.click();
  assert.equal(state.departures.length, previous + 1);
  assert.equal(state.departures[previous].how, 'assign');
  assert.equal(new URL(state.departures[previous].url, base).href, base + href);
  assert.equal(state.window.history.state.reader.q, query);
  return { query, href };
}

function assertSharedQuery(state, query) {
  assert.equal(new URL(state.window.location.href).searchParams.get('q'), query);
  assert.equal(state.doc.getElementById('reader-q').value, query);
  assert.equal(state.doc.getElementById('reader-search').hidden, false);
}

async function main() {
  const hits = await session('reference.html', 'reference.html' + search(headings[0].title), async (state) => {
    const found = [];
    for (const row of [...headings, ...claims]) found.push(await actualHit(state, row.title, row));
    const refinement = claims.at(-1);
    assert.match(refinement.grade.label, /single independent derivation with exact computational checks/i);
    found.push(await actualHit(state, refinement.grade.label, refinement));
    return found;
  });

  const chapterRoutes = await session('index.html', search(headings[0].title) + '#' + headings[0].id, (state) => {
    assertSharedQuery(state, headings[0].title);
    return headings.map((row, i) => {
      if (i) navigate(state, row.id);
      assert.equal(state.window.location.hash, '#' + row.id);
      const target = state.doc.getElementById(row.id);
      assert.equal(state.doc.querySelectorAll('[id="' + row.id + '"]').length, 1);
      assert.equal(norm(target.textContent), row.title);
      assert.equal(target.closest('[hidden]'), null);
      assert.ok(state.scrolls.includes(row.id));
      assert.equal(predecessor(state.doc), null);
      return { address: row.id, title: row.title };
    });
  });

  const atlasRoutes = await session('atlas.html', 'atlas.html' + search(claims[0].title) + '#' + claims[0].id, async (state) => {
    assertSharedQuery(state, claims[0].title);
    const routes = claims.map((row, i) => {
      if (i) navigate(state, row.id);
      assert.equal(state.window.location.hash, '#' + row.id);
      const card = state.doc.getElementById(row.id);
      assert.equal(state.doc.querySelectorAll('[id="' + row.id + '"]').length, 1);
      assert.equal(card.dataset.claimId, row.claim);
      assert.equal(card.dataset.statusCode, row.grade.code);
      assert.equal(card.hidden, false);
      assert.ok(card.classList.contains('is-selected'));
      assert.equal(card.closest('[hidden]'), null);
      assert.ok(card.closest('.atlas-body').classList.contains('has-pane'));
      const title = card.querySelector('.atlas-claim-title');
      assert.equal(norm(title.textContent), row.title);
      assert.equal(state.doc.activeElement, title);
      const label = row.grade.label === 'Established' ? card.querySelector('.atlas-claim-head .atlas-chip') :
        card.querySelector('.atlas-note-source');
      assert.ok(label && !label.closest('[hidden]'));
      assert.ok(norm(label.textContent).includes(row.grade.label));
      assert.equal(predecessor(state.doc), null);
      return { address: row.id, title: row.title, grade: row.grade.label };
    });
    const refinement = claims.at(-1);
    const field = state.doc.getElementById('atlas-q');
    field.value = '"' + refinement.grade.label + '"';
    field.dispatchEvent(new state.window.Event('input', { bubbles: true }));
    await new Promise((resolve) => setTimeout(resolve, 150));
    const row = state.doc.getElementById('atlas-r-' + refinement.claim);
    assert.equal(row.hidden, false);
    assert.equal(state.doc.getElementById('atlas-r-' + claims[0].claim).hidden, true);
    return routes;
  });

  const issued = report.results.flatMap(({ page, compatibility }) => compatibility
    .filter(({ origins }) => origins.some(({ edition }) => edition === 'v18')).map((record) => ({ page, ...record })));
  const stable = issued.find(({ page, role, origins }) => page === 'index.html' && role === 'retained' &&
    origins[0].edition === 'v18' && origins[0].priorLabel.length > 60);
  assert.ok(stable, 'an exact address first issued in v18 is needed');
  const stableAddress = await session('index.html', '#' + stable.id, (state) => {
    assert.equal(state.window.location.hash, '#' + stable.id);
    assert.deepEqual(stable.targets, [stable.id]);
    assert.equal(predecessor(state.doc), null);
    assert.equal(state.doc.getElementById(stable.id).closest('[hidden]'), null);
    assert.ok(state.scrolls.includes(stable.id));
    return { address: stable.id, label: stable.origins[0].priorLabel };
  });
  const moved = issued.filter(({ role }) => role !== 'retained');
  assert.equal(moved.length, 1);
  assert.equal(moved[0].role, 'changed');
  assert.equal(moved[0].page, 'index.html');
  assert.deepEqual(moved[0].targets, ['programme']);
  assert.match(moved[0].origins.find(({ edition }) => edition === 'v18').priorLabel, /01:00 UTC/);
  const bracket = '[a_\\lambda b]+[b_\\lambda a]';
  const changedAddress = await session('index.html', search(bracket) + '#' + moved[0].id, async (state) => {
    assertSharedQuery(state, bracket);
    assert.equal(state.window.location.hash, '#' + moved[0].id);
    const notice = predecessor(state.doc);
    assert.match(notice.querySelector('.reader-notice-text').textContent, /changed passage/);
    const chooser = notice.querySelector('a[href="#programme"]');
    assert.ok(chooser);
    chooser.click();
    assert.equal(state.window.location.hash, '#programme');
    assert.equal(state.doc.getElementById('programme').closest('[hidden]'), null);
    assert.ok(state.scrolls.includes('programme'));
    await new Promise((resolve, reject) => {
      const pending = setTimeout(() => reject(new Error('Back to changed v18 locator timed out')), 3000);
      state.window.addEventListener('popstate', () => { clearTimeout(pending); resolve(); }, { once: true });
      state.window.history.back();
    });
    assert.equal(state.window.location.hash, '#' + moved[0].id);
    assert.equal(new URL(state.window.location.href).searchParams.get('q'), bracket);
    assert.ok(predecessor(state.doc));
    return { from: moved[0].id, to: 'programme', bracket, back: state.window.location.hash };
  });
  console.log(JSON.stringify({ status: 'PASS', sourceIdentity,
    files: { ...Object.fromEntries(report.results.map(({ page, after }) => [page, after])), 'reader-index.js': report.outputIndex },
    hits, chapterRoutes, atlasRoutes, stableAddress, changedAddress }, null, 2));
}

main().catch((error) => { console.error(error.stack); process.exitCode = 1; });
