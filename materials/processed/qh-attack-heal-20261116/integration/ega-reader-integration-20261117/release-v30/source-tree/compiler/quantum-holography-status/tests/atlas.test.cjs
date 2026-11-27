#!/usr/bin/env node
/* Reader-task tests for the research atlas (atlas.js), run against a built page that has an atlas:

       NODE_PATH=<a node_modules folder with jsdom> node compiler/quantum-holography-status/tests/atlas.test.cjs <page.html> <atlas.json> [name filter]

   Each test loads a fresh copy of the page in jsdom with the page's scripts running, dispatches real events
   (clicks on links, keys, typing, history traversal) and checks what the reader is shown. Expected values come
   from the atlas.json the page was built from, never from the page. jsdom has no layout and no media queries:
   nothing here measures geometry (test_atlas.py checks the drawn geometry from the markup), and the narrow
   layout is the default unless a test sets the wide one. */
'use strict';
const fs = require('fs');
const assert = require('assert/strict');

let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require('jsdom')); } catch (e) {
  console.error('jsdom is not installed where Node can find it; set NODE_PATH to a node_modules folder that has it.');
  process.exit(2);
}
const [file, dataFile, only = ''] = process.argv.slice(2);
if (!file || !dataFile) { console.error('usage: atlas.test.cjs <page.html> <atlas.json> [name filter]'); process.exit(2); }
const PAGE = fs.readFileSync(file, 'utf8');
const DATA = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
const BASE = 'https://raeez.com/quantum-holography-tracker.html';

const opened = [];
function load(opts) {
  opts = opts || {};
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented: (navigation|window.scrollTo)/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
  vc.on('error', (...a) => errors.push('console.error: ' + a.join(' ')));
  vc.on('warn', (...a) => errors.push('console.warn: ' + a.join(' ')));
  const dom = new JSDOM(PAGE, {
    url: BASE + (opts.url || ''), runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) {
      w.__scrolled = [];
      w.Element.prototype.scrollIntoView = function () { w.__scrolled.push(this); };
      if (opts.wide) {
        w.matchMedia = q => ({ matches: /min-width:\s*1000px/.test(q), media: q, addListener() {}, removeListener() {},
                               addEventListener() {}, removeEventListener() {} });
      }
    }
  });
  opened.push(dom);
  return { dom, w: dom.window, d: dom.window.document, errors };
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
const settle = () => sleep(80);
async function until(cond, what) {  /* jsdom follows a link to a fragment in a later task; wait for its effect */
  for (let i = 0; i < 300; i++) { if (cond()) return; await sleep(10); }
  throw new Error('timed out waiting for ' + what);
}
function key(target, k, extra) {
  const e = new target.ownerDocument.defaultView.KeyboardEvent('keydown', Object.assign({ key: k, bubbles: true, cancelable: true }, extra || {}));
  target.dispatchEvent(e);
  return e;
}
const claimById = Object.fromEntries(DATA.claims.map(c => [c.id, c]));
const inOf = id => DATA.edges.filter(e => e.target === id).map(e => e.id).sort();
const outOf = id => DATA.edges.filter(e => e.source === id).map(e => e.id).sort();
const hub = [...DATA.claims].sort((a, b) => (inOf(b.id).length + outOf(b.id).length) - (inOf(a.id).length + outOf(a.id).length))[0].id;
const order = DATA.claims.map(c => c.id);
function selected(p) {
  const s = p.d.querySelectorAll('.atlas-claims-full .atlas-claim.is-selected');
  return s.length === 1 ? s[0].getAttribute('data-claim-id') : s.length ? 'several' : null;
}
async function open(p, id) {
  const a = p.d.querySelector(`#atlas-r-${id} th .atlas-link`);
  assert.ok(a, 'index link for ' + id);
  a.focus();
  a.click();
  await until(() => selected(p) === id, 'the selection of ' + id);
  await settle();
  return a;
}
/* The atlas's own words as a reader meets them: a space at every element boundary, labels of marks read where
   they stand. Left out: the index table (its numbers stand under its 'No.' heading), drawings, the inert words, and
   every element that carries the content owner's text (titles, statements, hypotheses, labels, summaries), whose
   words, such as 'complete', are mathematics and not the atlas's presentation. */
const SUPPLIED = '.atlas-link-title, .atlas-claim-title, .atlas-statement, .atlas-hyps, .atlas-item-hyps, .atlas-domain-summary, ' +
  '.atlas-overview, .atlas-path-summary, .atlas-path-note, .atlas-stage-desc, .atlas-stage-label, .atlas-rel-label, .atlas-rel-scope, ' +
  '.atlas-status-text, .atlas-status-own, .atlas-note-text, .atlas-claim-domain, .atlas-track, .atlas-domain-h, .atlas-comparison-h, ' +
  '.atlas-path-h, .atlas-key-own, .atlas-conventions, .atlas-claim-group-h, .atlas-row-domain, .atlas-col-domain, .atlas-domain-comps, ' +
  '.atlas-rel-names, .atlas-rel-name, .atlas-key-page-label, ' +
  /* copies the script makes of supplied text */
  '.atlas-chip-btn[data-atlas-domain], .atlas-chip-btn[data-atlas-relation], .atlas-pathbar strong, .atlas-hidden-note, .atlas-tip, ' +
  '.atlas-question-link';
function atlasText(p) {
  const out = [];
  (function walk(n) {
    if (n.nodeType === 3) { out.push(n.nodeValue); return; }
    if (n.nodeType !== 1) return;
    if (n.matches('table, template, script, style, annotation') || n.matches(SUPPLIED) || n.getAttribute('aria-hidden') === 'true') return;
    if (n.hasAttribute('aria-label')) out.push(' ' + n.getAttribute('aria-label') + ' ');
    for (let c = n.firstChild; c; c = c.nextSibling) walk(c);
    out.push(' ');
  })(p.d.getElementById('atlas'));
  return out.join('').replace(/\s+/g, ' ');
}
const NO_COUNT = [/%/, /\b\d+\s+of\s+\d+\b/i, /\b(progress|completed?|completion|percent)\b/i,
                  /(?<!No\. )\b\d+\s+(established|conditional|scoped|remaining|claims?|theorems?)\b/i];
/* Fails with the words around the first match, so that a finding can be traced to its element. */
function assertNoCount(text) {
  for (const r of NO_COUNT) {
    const m = r.exec(text);
    if (m) assert.fail('found ' + JSON.stringify(m[0]) + ' in: ' + JSON.stringify(text.slice(Math.max(0, m.index - 140), m.index + 60)));
  }
}

const tests = [];
const SKIP = { reason: '' };
function test(name, fn) { tests.push({ name, fn }); }
/* An observation records how the page behaves where the atlas lane is not the owner; it is never a pass. */
function observe(name, fn) { tests.push({ name, fn, observation: true }); }

test('start: the script runs, nothing is selected, the pane shows its message', async () => {
  const p = load();
  await settle();
  assert.ok(p.d.querySelector('[data-atlas-mount] .atlas-body.atlas-js'), 'atlas-js');
  assert.equal(selected(p), null);
  assert.equal(p.d.querySelector('.atlas-pane-empty').hidden, false);
  assert.deepEqual(p.errors, []);
});

test('RT2/RT3: an index link selects its claim through the address, with statement, hypotheses and every relation', async () => {
  const p = load();
  await settle();
  const a = await open(p, hub);
  assert.equal(p.w.location.hash, '#atlas-c-' + hub);
  assert.equal(selected(p), hub);
  const art = p.d.getElementById('atlas-c-' + hub);
  /* The status-language ruling: the word is chosen by the stored code, and the page status by the alias map. */
  const WORD = { checked: 'Established', conditional: 'Conditional', remaining: 'Remaining', scoped_negative: 'Scoped negative' };
  const ALIAS = { checked: 'checked', conditional: 'conditional', remaining: 'open', scoped_negative: 'refuted form' };
  const code = claimById[hub].status.code;
  assert.equal(art.querySelector('.atlas-chip-group').textContent.trim(), WORD[code]);
  assert.equal(art.getAttribute('data-qh-unit-status'), ALIAS[code]);
  assert.ok(!art.textContent.includes(claimById[hub].status.label) || claimById[hub].status.label === WORD[code],
            'the per-record label is not shown');
  assert.equal(art.querySelectorAll('.atlas-hyps li').length, claimById[hub].hypotheses.length);
  const listed = dir => Array.from(art.querySelectorAll(`.atlas-rel-block[data-dir="${dir}"] .atlas-rel`)).map(li => li.getAttribute('data-edge-id')).sort();
  assert.deepEqual(listed('in'), inOf(hub));
  assert.deepEqual(listed('out'), outOf(hub));
  const drawn = Array.from(art.querySelectorAll('.atlas-hood-edge')).map(e => [e.getAttribute('data-edge-id'), e.getAttribute('data-source'), e.getAttribute('data-target')]);
  assert.equal(drawn.length, inOf(hub).length + outOf(hub).length);
  for (const [id, s, t] of drawn) {
    const e = DATA.edges.find(x => x.id === id);
    assert.ok(e && e.source === s && e.target === t, 'diagram edge ' + id + ' keeps its direction');
  }
  const on = Array.from(p.d.querySelectorAll('.atlas-map .atlas-edge.is-on')).map(e => e.getAttribute('data-edge-id')).sort();
  assert.deepEqual(on, [...inOf(hub), ...outOf(hub)].sort(), 'the map marks exactly these relations');
  assert.ok(p.d.getElementById('atlas-r-' + hub).classList.contains('is-sel'));
  assert.equal(p.d.activeElement, art.querySelector('.atlas-claim-title'), 'focus moves to the claim heading');
  const ids = Array.from(p.d.querySelectorAll('[id]')).map(e => e.id);
  assert.equal(new Set(ids).size, ids.length, 'no duplicate id');
  assert.ok(a);
  assert.deepEqual(p.errors, []);
});

test('INV4: every edge is listed once at each end with its direction, and drawn once in the map', async () => {
  const p = load();
  await settle();
  for (const e of DATA.edges) {
    const items = Array.from(p.d.querySelectorAll(`.atlas-claim .atlas-rel[data-edge-id="${e.id}"]`));
    assert.equal(items.length, 2, e.id);
    for (const li of items) {
      assert.equal(li.getAttribute('data-source'), e.source);
      assert.equal(li.getAttribute('data-target'), e.target);
      assert.equal(li.getAttribute('data-relation'), e.relation);
    }
    assert.ok(p.d.querySelector(`#atlas-c-${e.source} .atlas-rels[data-dir="out"] [data-edge-id="${e.id}"]`), e.id + ' out of its source');
    assert.ok(p.d.querySelector(`#atlas-c-${e.target} .atlas-rels[data-dir="in"] [data-edge-id="${e.id}"]`), e.id + ' into its target');
  }
  const drawn = Array.from(p.d.querySelectorAll('.atlas-map .atlas-edge')).map(x => x.getAttribute('data-edge-id')).sort();
  assert.deepEqual(drawn, DATA.edges.map(e => e.id).sort());
});

test('RT9: Back and Forward move between selections made by links', async () => {
  const p = load();
  await settle();
  await open(p, hub);
  const neighbour = DATA.edges.find(e => e.source === hub).target;
  p.d.querySelector(`#atlas-c-${hub} .atlas-rel .atlas-link[href="#atlas-c-${neighbour}"]`).click();
  await until(() => selected(p) === neighbour, 'the neighbour');
  p.w.history.back();
  await until(() => selected(p) === hub, 'Back to ' + hub);
  p.w.history.forward();
  await until(() => selected(p) === neighbour, 'Forward to ' + neighbour);
});

test('RT9: arriving with #atlas-c-<id> shows that claim and the page raises no unknown-address notice', async () => {
  const p = load({ url: '#atlas-c-' + order[2], wide: true });
  await settle();
  assert.equal(selected(p), order[2]);
  const notice = p.d.querySelector('.qh-notice');
  assert.ok(!notice || !notice.getAttribute('data-notice'), 'no notice: ' + (notice && notice.textContent));
  assert.ok(p.w.__scrolled.includes(p.d.getElementById('atlas-r-' + order[2])), 'the index row is brought into view on a wide screen');
});

test('RT9: an address that leaves the atlas leaves nothing selected; another atlas part keeps the claim', async () => {
  const p = load();
  await settle();
  await open(p, order[0]);
  const k = DATA.comparisons.find(c => [].concat(c.establishedClaimIds, c.conditionalClaimIds, c.scopedNegativeClaimIds, c.remainingClaimIds).includes(order[0]));
  if (k) {
    p.d.querySelector(`#atlas-c-${order[0]} a[href="#atlas-k-${k.id}"]`).click();
    await until(() => p.w.location.hash === '#atlas-k-' + k.id, 'the comparison address');
    await settle();
    assert.equal(p.w.location.hash, '#atlas-k-' + k.id);
    assert.equal(selected(p), order[0], 'a comparison of the atlas keeps the pane');
  }
  /* a link of the page to its own section #examples, outside the atlas (the page's navigation, whatever it is called) */
  const away = Array.from(p.d.querySelectorAll('a[href="#examples"]')).find(a => !a.closest('[data-atlas-mount]'));
  if (!away) { SKIP.reason = 'the page has no link to #examples outside the atlas'; return SKIP; }
  away.click();
  await until(() => selected(p) === null, 'the selection to clear');
  assert.equal(p.d.querySelector('.atlas-pane-empty').hidden, false);
  p.w.history.back();
  await sleep(150);
  p.w.history.back();
  await until(() => selected(p) === order[0], 'Back to the claim');
});

test('a link from a claim to a statement of the page goes through qh:navigate, which the page handles', async () => {
  const p = load();
  await settle();
  const ref = DATA.claims.find(c => c.statementRef);
  if (!ref) { SKIP.reason = 'no claim of this atlas.json has a statementRef to a statement of the page'; return SKIP; }
  await open(p, ref.id);
  let asked = null;
  p.d.addEventListener('qh:navigate', e => { asked = e.detail.id; }, true);
  const link = p.d.querySelector(`#atlas-c-${ref.id} .atlas-page-link`);
  link.click();
  await until(() => p.w.location.hash === '#s-' + ref.statementRef, 'the statement address');
  await settle();
  assert.equal(asked, 's-' + ref.statementRef);
  assert.equal(p.w.location.hash, '#s-' + ref.statementRef);
  assert.equal(p.d.activeElement && p.d.activeElement.id, 's-' + ref.statementRef, 'the page focuses the statement');
});

test('RT8/INV5: filters by words, domain and status; the count line names no number; the map dims the rest', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('atlas-q');
  q.value = 'lift';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(160);
  const rows = () => Array.from(p.d.querySelectorAll('.atlas-table tbody tr')).filter(r => !r.hidden).map(r => r.getAttribute('data-claim-ref'));
  const want = DATA.claims.filter(c => (c.title + ' ' + c.statement + ' ' + c.hypotheses.join(' ') + ' ' + (c.sourceLabel || '')).toLowerCase().includes('lift')).map(c => c.id);
  assert.deepEqual(rows(), want);
  assert.doesNotMatch(p.d.querySelector('.atlas-count').textContent, /\d/);
  p.d.querySelector('.atlas-clear').click();
  p.d.querySelector('.atlas-chip-btn[data-atlas-status="conditional"]').click();
  assert.deepEqual(rows(), DATA.claims.filter(c => c.status.code === 'conditional').map(c => c.id));
  assert.equal(p.d.querySelectorAll('.atlas-map .atlas-node.is-out').length, DATA.claims.filter(c => c.status.code !== 'conditional').length);
  assert.doesNotMatch(p.d.querySelector('.atlas-count').textContent, /\d/);
  p.d.querySelector('.atlas-chip-btn[data-atlas-domain="' + DATA.domains[1].id + '"]').click();
  assert.deepEqual(rows(), DATA.claims.filter(c => c.status.code === 'conditional' && c.domainId === DATA.domains[1].id).map(c => c.id));
  assertNoCount(atlasText(p));
});

test('RT6: arrows move through the index; Escape in the pane returns focus to the claim in the index', async () => {
  const p = load();
  await settle();
  const first = p.d.querySelector(`#atlas-r-${order[0]} th .atlas-link`);
  first.focus();
  key(first, 'ArrowDown');
  assert.equal(p.d.activeElement, p.d.querySelector(`#atlas-r-${order[1]} th .atlas-link`));
  key(p.d.activeElement, 'End');
  assert.equal(p.d.activeElement, p.d.querySelector(`#atlas-r-${order[order.length - 1]} th .atlas-link`));
  key(p.d.activeElement, 'Home');
  assert.equal(p.d.activeElement, first);
  key(first, 'ArrowUp');
  assert.equal(p.d.activeElement, p.d.getElementById('atlas-q'), 'Up from the first claim reaches the filter');
  const a = await open(p, order[1]);
  const t = p.d.activeElement;
  assert.ok(t.classList.contains('atlas-claim-title'));
  const e = key(t, 'Escape');
  assert.equal(e.defaultPrevented, true, 'the atlas handles Escape');
  assert.equal(p.d.activeElement, a);
  assert.ok(p.d.querySelector('.atlas-claims-full').classList.contains('is-closed'), 'the sheet closes on a narrow screen');
  assert.equal(selected(p), order[1], 'the selection stays');
});

test('RT6: with the glossary card open from the pane, Escape closes the card first and keeps the selection', async () => {
  const p = load();
  await settle();
  const c = DATA.claims.find(x => /weak module/.test(x.statement));
  if (!c) { SKIP.reason = 'no claim of this atlas.json mentions the glossary term the test opens'; return SKIP; }
  await open(p, c.id);
  const term = p.d.querySelector(`#atlas-c-${c.id} .term`);
  if (!term) { SKIP.reason = 'no glossary button in the claim: atlas.py TERMS is off, or the page glossary lacks the term'; return SKIP; }
  term.click();
  await settle();
  const card = p.d.getElementById('card');
  assert.equal(card.hidden, false, 'the page opens its card for the term');
  term.focus();
  key(term, 'Escape');
  await settle();
  assert.equal(card.hidden, true, 'the page closes the card');
  assert.equal(selected(p), c.id);
  assert.ok(!p.d.querySelector('.atlas-claims-full').classList.contains('is-closed'), 'the pane stays open');
});

test('RT5: Follow walks a path joined by recorded relations claim by claim, in stage order, and Leave ends it', async () => {
  const p = load();
  await settle();
  const path = DATA.readingPaths.find(x => x.kind === 'source_bound_dependency_path');
  if (!path) { SKIP.reason = 'this atlas.json has no path of kind source_bound_dependency_path'; return SKIP; }
  const steps = path.stages.flatMap(s => s.claimIds);
  p.d.querySelector(`#atlas-p-${path.id} .atlas-follow`).click();
  await until(() => selected(p) === steps[0], 'the first step');
  const seen = [selected(p)];
  for (let i = 1; i < steps.length; i++) {
    const next = Array.from(p.d.querySelectorAll('.atlas-pathbar .atlas-step')).find(a => +a.getAttribute('data-step') === i);
    assert.ok(next, 'a Next link to step ' + i);
    next.click();
    await until(() => selected(p) === steps[i], 'step ' + i);
    seen.push(selected(p));
  }
  assert.deepEqual(seen, steps);
  const here = Array.from(p.d.querySelectorAll(`#atlas-p-${path.id} .atlas-stage.is-here`)).map(s => s.getAttribute('data-stage'));
  assert.deepEqual(here, [String(path.stages.length - 1)]);
  const where = p.d.querySelector('.atlas-pathbar-where').textContent;
  assert.doesNotMatch(where, /\bof\b/, 'the position names no total');
  p.w.history.back();
  await until(() => selected(p) === steps[steps.length - 2], 'Back along the path');
  Array.from(p.d.querySelectorAll('.atlas-pathbar button')).pop().click();
  assert.equal(p.d.querySelector('.atlas-pathbar').hidden, true, 'Leave ends the path');
  const kinds = Array.from(p.d.querySelectorAll('.atlas-path')).map(a => [a.getAttribute('data-path-kind'), a.querySelector('.atlas-kind-tag').textContent]);
  assert.equal(new Set(kinds.map(k => k[1])).size, new Set(kinds.map(k => k[0])).size, 'each kind has its own label');
});

test('RT3: hiding a relation type in the pane hides it there only and names it', async () => {
  const p = load();
  await settle();
  await open(p, hub);
  const kinds = [...new Set(DATA.edges.filter(e => e.source === hub || e.target === hub).map(e => e.relation))];
  if (kinds.length < 2) { SKIP.reason = 'this atlas.json has fewer than two path kinds'; return SKIP; }
  const art = p.d.getElementById('atlas-c-' + hub);
  art.querySelector(`.atlas-hood-legend .atlas-chip-btn[data-atlas-relation="${kinds[0]}"]`).click();
  const n = DATA.edges.filter(e => (e.source === hub || e.target === hub) && e.relation === kinds[0]).length;
  assert.equal(art.querySelectorAll('.atlas-rel[hidden]').length, n);
  assert.equal(art.querySelectorAll('.atlas-hood-edge.is-hidden').length, n);
  assert.match(art.querySelector('.atlas-hidden-note').textContent, new RegExp(DATA.edges.find(e => e.relation === kinds[0]).label));
  assert.equal(p.d.querySelectorAll('.atlas-map .atlas-edge.is-on').length, inOf(hub).length + outOf(hub).length, 'the map is unchanged');
  await open(p, order[0]);
  assert.equal(p.d.querySelectorAll(`#atlas-c-${hub} .atlas-rel[hidden]`).length, 0, 'a claim left behind keeps every relation');
});

test('the page search finds the atlas claims it is offered, and following a result shows the claim in the pane', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('find-q');
  if (!q) { SKIP.reason = 'the page offers no search field'; return SKIP; }
  /* A claim whose title has no formula, searched by its whole title as a phrase. */
  const target = DATA.claims.find(c => !/\\[(\[]/.test(c.title) && c.title.split(' ').length > 2) || DATA.claims[0];
  q.focus();
  q.value = '"' + target.title + '"';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(300);
  const hit = Array.from(p.d.querySelectorAll('.find-results a')).find(a => a.getAttribute('href') === '#atlas-c-' + target.id);
  assert.ok(hit, 'a result for the claim: ' + p.d.querySelector('.find-count').textContent);
  hit.click();
  await until(() => selected(p) === target.id, 'the claim selected by the search result');
  await settle();
  assert.equal(p.d.activeElement, p.d.querySelector(`#atlas-c-${target.id} .atlas-claim-title`), 'focus on the claim heading');
});

test('the page search, filtered by a status, keeps the atlas claims of that status (by the ruling\'s aliases) and names it', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('find-q');
  if (!q) { SKIP.reason = 'the page offers no search field'; return SKIP; }
  const ALIAS = { scoped_negative: 'refuted form', checked: 'checked', conditional: 'conditional', remaining: 'open' };
  const plain = c => !/\\[(\[]/.test(c.title) && c.title.split(' ').length > 2;
  let facet = null, neg = null;
  for (const code of Object.keys(ALIAS)) {
    const f = p.d.querySelector(`.filter[data-status-facet="${ALIAS[code]}"]`);
    const c = DATA.claims.find(x => x.status.code === code && plain(x));
    if (f && c) { facet = f; neg = c; break; }
  }
  if (!facet) { SKIP.reason = 'the page offers no status filter for a status of the atlas claims'; return SKIP; }
  const other = DATA.claims.find(c => ALIAS[c.status.code] !== ALIAS[neg.status.code] && plain(c));
  const hits = async (c) => {
    q.focus();
    q.value = '"' + c.title + '"';
    q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
    await sleep(300);
    return Array.from(p.d.querySelectorAll('.find-results a')).filter(a => a.getAttribute('href') === '#atlas-c-' + c.id);
  };
  if (facet.getAttribute('aria-pressed') !== 'true') facet.click();
  await sleep(200);
  const found = await hits(neg);
  assert.ok(found.length, 'the status filter keeps the atlas claim of that status');
  const word = Array.from(facet.childNodes).map(n => n.textContent).join('').replace(/\s+/g, ' ').trim();
  const item = found[0].closest('li') || found[0];
  assert.ok(item.textContent.includes(word), "the result names the page's word for the status: " + word);
  if (other) assert.equal((await hits(other)).length, 0, 'an atlas claim of another status is not kept by this filter');
});

observe('Back after a row toggle of the page (the toggle replaces the history entry)', async () => {
  const p = load();
  await settle();
  await open(p, order[0]);
  p.d.querySelector('details.row > summary').click();
  await settle();
  const hash = p.w.location.hash;
  const stillSelected = selected(p);
  await open(p, order[order.length - 1]);
  p.w.history.back();
  await settle();
  return `address after the toggle ${hash}; selection kept until the next address change: ${stillSelected}; after Back: ${selected(p)}`;
});

test('the map with its key is the first part, and the parts are named apart from the page\'s own sections', async () => {
  const p = load();
  await settle();
  const first = p.d.querySelector('.atlas-main > .atlas-part');
  assert.equal(first.id, 'atlas-overview');
  assert.ok(first.querySelector('#atlas-map') && first.querySelector('.atlas-key'), 'map and key together');
  assert.equal(p.d.querySelector('.atlas-parts a').getAttribute('href'), '#atlas-overview');
  const page = new Set(Array.from(p.d.querySelectorAll('.nav a')).map(a => a.textContent.trim()));
  const mine = Array.from(p.d.querySelectorAll('.atlas-parts a')).map(a => a.textContent.trim());
  assert.deepEqual(mine.filter(t => page.has(t) && t !== 'Atlas'), [], 'no atlas part shares a name with a section of the page');
});

test('RT8: the filter reads title, statement, hypotheses and source only, and says so', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('atlas-q');
  const rows = () => Array.from(p.d.querySelectorAll('.atlas-table tbody tr')).filter(r => !r.hidden).map(r => r.getAttribute('data-claim-ref'));
  q.value = 'listed';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(160);
  assert.deepEqual(rows(), DATA.claims.filter(c => /listed/i.test(c.title + ' ' + c.statement + ' ' + c.hypotheses.join(' ') + ' ' + (c.sourceLabel || ''))).map(c => c.id),
                   'interface words such as None listed. are not searched');
  const src = DATA.claims.find(c => c.sourceLabel);
  if (src) {
    q.value = src.sourceLabel;
    q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
    await sleep(160);
    assert.ok(rows().includes(src.id), 'the source statement is searched');
  }
  assert.ok(p.d.querySelector('.atlas-filter-note').textContent.length > 20, 'the filter says what it reads');
});

test('RT7: a sheet the reader closed stays closed when the page announces its search or filter state', async () => {
  const p = load();
  await settle();
  await open(p, order[0]);
  const full = p.d.querySelector('.atlas-claims-full');
  full.querySelector('.atlas-pane-close').click();
  assert.ok(full.classList.contains('is-closed'));
  const q = p.d.getElementById('find-q');
  if (q) {
    q.focus();
    q.value = 'lattice';
    q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
    await sleep(250);
  }
  p.d.dispatchEvent(new p.w.CustomEvent('qh:state', { detail: { hash: 'atlas-c-' + order[0] } }));
  assert.ok(full.classList.contains('is-closed'), 'still closed after the page announced its state');
  await open(p, order[1]);
  assert.ok(!full.classList.contains('is-closed'), 'selecting a claim opens it again');
});

test('RT6/RT9: Back and Forward with focus in the pane move focus to the claim shown', async () => {
  const p = load();
  await settle();
  await open(p, hub);
  const neighbour = DATA.edges.find(e => e.source === hub).target;
  p.d.querySelector(`#atlas-c-${hub} .atlas-rel .atlas-link[href="#atlas-c-${neighbour}"]`).click();
  await until(() => selected(p) === neighbour, 'the neighbour');
  assert.equal(p.d.activeElement, p.d.querySelector(`#atlas-c-${neighbour} .atlas-claim-title`));
  p.w.history.back();
  await until(() => selected(p) === hub, 'Back');
  await settle();
  assert.equal(p.d.activeElement, p.d.querySelector(`#atlas-c-${hub} .atlas-claim-title`), 'focus is on the claim shown, not in a hidden one');
});

test('RT7: on a narrow screen the sheet closes when keyboard focus leaves it for the page', async () => {
  const p = load();
  await settle();
  await open(p, order[0]);
  const full = p.d.querySelector('.atlas-claims-full');
  assert.ok(!full.classList.contains('is-closed'), 'the sheet is open');
  p.d.getElementById('atlas-q').focus();
  assert.ok(full.classList.contains('is-closed'), 'the sheet closed when focus left it');
  assert.equal(selected(p), order[0], 'the selection stays');
});

test('RT5: the Follow bar names the kind of the path it follows; stages put their heading before their joins', async () => {
  const p = load();
  await settle();
  const path = DATA.readingPaths.find(x => x.kind === 'source_bound_dependency_path');
  if (!path) { SKIP.reason = 'this atlas.json has no path of kind source_bound_dependency_path'; return SKIP; }
  p.d.querySelector(`#atlas-p-${path.id} .atlas-follow`).click();
  await until(() => selected(p) === path.stages[0].claimIds[0], 'the first step');
  assert.equal(p.d.querySelector('.atlas-pathbar .atlas-kind-tag').textContent,
               p.d.querySelector(`#atlas-p-${path.id} .atlas-kind-tag`).textContent);
  for (const stage of p.d.querySelectorAll(`#atlas-p-${path.id} .atlas-stage`)) {
    const join = stage.querySelector('.atlas-join');
    if (join) assert.ok(stage.querySelector('.atlas-stage-h').compareDocumentPosition(join) & p.w.Node.DOCUMENT_POSITION_FOLLOWING, 'heading first');
  }
});

test('a question link reads as the heading of the question it leads to', async () => {
  const p = load();
  await settle();
  const links = Array.from(p.d.querySelectorAll('#atlas a.atlas-question-link'));
  if (!links.length) { SKIP.reason = 'this atlas.json links no question of the page'; return SKIP; }
  const flat = n => { const c = n.cloneNode(true); c.querySelectorAll('annotation').forEach(x => x.remove()); return c.textContent.replace(/\s+/g, ' ').trim(); };
  for (const a of links) {
    const q = p.d.getElementById(a.getAttribute('data-question-ref'));
    assert.ok(q, 'the question exists on the page: ' + a.getAttribute('href'));
    assert.equal(flat(a), flat(q.querySelector('h3')), 'the link text is the question heading');
    assert.equal(a.querySelector('a, button, [id]'), null, 'no link, button or id inside the link');
  }
});

test('A4-IN-06: Tab past the glossary card from the last control of a claim never lands in a claim the pane hides', async () => {
  const p = load();
  await settle();
  const c = DATA.claims.find(x => /weak module/.test(x.statement));
  if (!c) { SKIP.reason = 'no claim of this atlas.json mentions the glossary term the test opens'; return SKIP; }
  await open(p, c.id);
  const article = p.d.getElementById('atlas-c-' + c.id);
  const others = Array.from(p.d.querySelectorAll('.atlas-claims-full .atlas-claim')).filter(x => x !== article);
  assert.ok(others.every(x => x.hidden) && !article.hidden, 'only the claim shown is unhidden in the pane');
  const term = article.querySelector('.term');
  if (!term) { SKIP.reason = 'no glossary button in the claim: atlas.py TERMS is off, or the page glossary lacks the term'; return SKIP; }
  /* the term becomes the last control of its claim */
  Array.from(article.querySelectorAll('a[href], button')).filter(x => term.compareDocumentPosition(x) & p.w.Node.DOCUMENT_POSITION_FOLLOWING).forEach(x => x.remove());
  term.click();
  await settle();
  const card = p.d.getElementById('card');
  assert.equal(card.hidden, false, 'the card is open');
  term.focus();
  key(term, 'Tab');
  await settle();
  const inCard = Array.from(card.querySelectorAll('a[href], button'));
  if (!inCard.length || !card.contains(p.d.activeElement)) { SKIP.reason = 'the page card offers no link to Tab through'; return SKIP; }
  const last = inCard[inCard.length - 1];
  last.focus();
  key(last, 'Tab');
  await settle();
  const at = p.d.activeElement;
  assert.ok(!at.closest('[hidden]'), 'focus is not inside a hidden element');
  assert.ok(!others.some(x => x.contains(at)), 'focus is not in a claim the pane does not show');
  assert.ok(!card.contains(at), 'focus has left the closed card');
});

test('C1: comparisons, paths and domain claims start folded; an address, a search result and print open them', async () => {
  const p = load();
  await settle();
  const folds = Array.from(p.d.querySelectorAll('#atlas details.atlas-fold'));
  assert.ok(folds.length >= DATA.comparisons.length + DATA.readingPaths.length + DATA.domains.length, 'every long part is folded');
  assert.ok(folds.every(d => !d.open), 'all folds start closed');
  const k = DATA.comparisons[0];
  p.w.location.hash = '#atlas-k-' + k.id;
  await settle();
  assert.equal(p.d.getElementById('atlas-k-' + k.id).open, true, 'the address opens its comparison');
  const conv = DATA.domains.find(d => (d.conventions || []).length);
  if (conv) {
    p.w.location.hash = '#atlas-d-' + conv.id + '--conv';
    await settle();
    assert.equal(p.d.getElementById('atlas-d-' + conv.id + '--conv').closest('details').open, true, 'a target inside a fold opens it');
  }
  const path = DATA.readingPaths[0];
  const unit = p.d.getElementById('atlas-p-' + path.id);
  unit.dispatchEvent(new p.w.CustomEvent('qh:reveal', { bubbles: true, cancelable: true, detail: { id: unit.id } }));
  assert.equal(unit.open, true, 'a search result opens its path');
  const closed = Array.from(p.d.querySelectorAll('#atlas details')).filter(d => !d.open);
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  assert.ok(closed.every(d => d.open), 'print opens every fold');
  p.w.dispatchEvent(new p.w.Event('afterprint'));
  assert.ok(closed.every(d => !d.open), 'and closes them again after');
  assert.ok(!p.d.querySelector('.atlas-js.has-pane .atlas-main[style]'), 'no layout change is written');
});

test('C16: the map is one tab stop; the arrow keys move over its claims, announce them, and Enter shows the claim', async () => {
  const p = load();
  await settle();
  const box = p.d.querySelector('.atlas-map-scroll');
  const say = p.d.querySelector('[data-atlas-map-say]');
  assert.equal(box.getAttribute('tabindex'), '0');
  box.focus();
  key(box, 'Home');
  assert.match(say.textContent, /^No\. \d+: /, 'the claim under the cursor is announced');
  const first = say.textContent;
  key(box, 'ArrowDown');
  assert.notEqual(say.textContent, first, 'the cursor moves');
  assert.equal(p.d.querySelectorAll('.atlas-node.is-cursor').length, 1, 'one mark carries the cursor');
  const n = +/^No\. (\d+)/.exec(say.textContent)[1];
  key(box, 'Enter');
  await settle();
  const sel = selected(p);
  assert.ok(sel, 'Enter selects the claim');
  assert.equal(p.d.getElementById('atlas-c-' + sel).getAttribute('data-number'), String(n));
});

test('Follow visits a path whose stages put the only claim link in the heading', async () => {
  const path = DATA.readingPaths.find(path => path.stages.length > 1 && path.stages.every(stage =>
    stage.claimIds.length === 1 && stage.label.trim() === claimById[stage.claimIds[0]].title.trim()));
  if (!path) { SKIP.reason = 'no path with only heading links'; return SKIP; }
  const p = load();
  const follow = p.d.querySelector('#atlas-p-' + path.id + ' .atlas-follow');
  assert.ok(follow, 'the entire path has a Follow link');
  follow.click();
  for (let i = 0; i < path.stages.length; i++) {
    if (i) p.d.querySelector('.atlas-pathbar [data-step-role="next"]').click();
    await until(() => selected(p) === path.stages[i].claimIds[0], 'stage ' + (i + 1));
  }
});

test('C19: Previous and Next keep the keyboard on the path bar', async () => {
  const p = load();
  await settle();
  const follow = p.d.querySelector('.atlas-path .atlas-follow, .atlas-path [data-follow]');
  if (!follow) { SKIP.reason = 'this atlas.json has no path to follow'; return SKIP; }
  follow.click();
  await settle();
  const next = p.d.querySelector('.atlas-pathbar [data-step-role="next"]');
  if (!next) { SKIP.reason = 'the path has one stage'; return SKIP; }
  next.focus();
  next.click();
  await settle();
  const at = p.d.activeElement;
  assert.ok(at && at.closest('.atlas-pathbar'), 'focus is still on the path bar');
});

test('A6: on a wide screen the pane has a column of its own while shown; Close and Escape give it back; the head with Close leads', async () => {
  const p = load({ wide: true });
  await settle();
  const body = p.d.querySelector('.atlas-body');
  const full = p.d.querySelector('.atlas-claims-full');
  assert.ok(!body.classList.contains('has-pane'), 'no column for the pane before a claim is selected');
  const a = await open(p, order[1]);
  assert.ok(body.classList.contains('has-pane'), 'the pane has its column while it shows a claim');
  const head = full.querySelector('.atlas-pane-head');
  assert.ok(head && head.querySelector('.atlas-pane-close'), 'Close is in the head');
  const shown = Array.from(full.children).filter(n => !n.hidden && !n.matches('.atlas-part-head'));
  assert.equal(shown[0], head, 'the head leads the pane');
  head.querySelector('.atlas-pane-close').click();
  assert.ok(full.classList.contains('is-closed'));
  assert.ok(!body.classList.contains('has-pane'), 'Close gives the column back');
  assert.equal(p.d.activeElement, a, 'focus returns to the claim in the index');
  assert.equal(selected(p), order[1], 'the selection stays');
  await open(p, order[2]);
  assert.ok(body.classList.contains('has-pane') && !full.classList.contains('is-closed'), 'selecting a claim opens it again');
  const e = key(p.d.querySelector('#atlas-c-' + order[2] + ' .atlas-claim-title'), 'Escape');
  assert.equal(e.defaultPrevented, true);
  assert.ok(!body.classList.contains('has-pane'), 'Escape gives the column back too');
  p.w.location.hash = '#atlas-c-' + order[3];
  await until(() => selected(p) === order[3], 'the address');
  assert.ok(body.classList.contains('has-pane'), 'an address that names a claim opens it');
  p.w.location.hash = '#atlas-index';
  await settle();
  assert.ok(body.classList.contains('has-pane'), 'another part of the atlas keeps it');
});

test('A2: the pane places the claim in a locator of the whole atlas by its number, and returns to it in the map', async () => {
  const p = load({ wide: true });
  await settle();
  const loc = p.d.querySelector('.atlas-claims-full .atlas-locator');
  assert.ok(loc, 'the locator is in the pane');
  assert.equal(loc.hidden, true, 'hidden while nothing is selected');
  assert.equal(loc.querySelectorAll('circle[data-claim-ref]').length, DATA.claims.length, 'every claim of the atlas has its dot');
  assert.equal(loc.querySelectorAll('.atlas-locator-track').length, DATA.domains.length, 'every domain has its band');
  for (const c of DATA.claims) {
    const m = /translate\(([-\d.]+) ([-\d.]+)\)/.exec(p.d.querySelector(`.atlas-map .atlas-node[data-claim-ref="${c.id}"]`).getAttribute('transform'));
    const dot = loc.querySelector(`circle[data-claim-ref="${c.id}"]`);
    assert.deepEqual([+dot.getAttribute('cx'), +dot.getAttribute('cy')], [+m[1], +m[2]], 'at its place in the map: ' + c.id);
  }
  assert.equal(loc.querySelectorAll('path, line, polyline, marker').length, 0, 'no line on the locator: no relation is implied');
  const id = order[order.length - 1];
  await open(p, id);
  assert.equal(loc.hidden, false);
  const no = loc.querySelector('.atlas-locator-no');
  assert.equal(no.textContent.trim(), p.d.getElementById('atlas-c-' + id).getAttribute('data-number'), 'marked by its number');
  assert.ok(no.querySelector('svg.mark'), 'with its status mark, as on its pill in the map');
  assert.deepEqual(Array.from(loc.querySelectorAll('circle.is-here')).map(d => d.getAttribute('data-claim-ref')), [id]);
  assert.deepEqual(Array.from(loc.querySelectorAll('.atlas-locator-track.is-here')).map(r => r.getAttribute('data-domain-ref')),
                   [claimById[id].domainId], 'its domain is marked');
  const dot = loc.querySelector(`circle[data-claim-ref="${id}"]`), ring = loc.querySelector('.atlas-locator-ring');
  assert.deepEqual([ring.getAttribute('cx'), ring.getAttribute('cy')].map(Number), [dot.getAttribute('cx'), dot.getAttribute('cy')].map(Number));
  await open(p, order[0]);
  assert.deepEqual(Array.from(loc.querySelectorAll('circle.is-here')).map(d => d.getAttribute('data-claim-ref')), [order[0]], 'it follows the selection');
  const link = loc.querySelector('a.atlas-locator-link');
  assert.equal(link.getAttribute('href'), '#atlas-map');
  link.click();
  await until(() => p.w.location.hash === '#atlas-map', 'the map address');
  await settle();
  assert.equal(selected(p), order[0], 'the selection stays');
  const node = p.d.querySelector(`.atlas-map .atlas-node[data-claim-ref="${order[0]}"]`);
  assert.ok(node.classList.contains('is-sel'), 'its pill is highlighted in the map');
  assert.equal(p.d.activeElement, p.d.querySelector('.atlas-map-scroll'), 'the map takes the keyboard');
  assert.ok(node.classList.contains('is-cursor'), 'with its cursor on the claim');
});

test('the map shows the relations of the claim selected only, and the filter dims the lines of the claims it hides', async () => {
  const p = load({ wide: true });
  await settle();
  const linesOf = id => [...inOf(id), ...outOf(id)].sort();
  const on = () => Array.from(p.d.querySelectorAll('.atlas-map .atlas-edge.is-on')).map(e => e.getAttribute('data-edge-id')).sort();
  await open(p, hub);
  assert.deepEqual(on(), linesOf(hub), 'the relations of the selected claim');
  const other = order.find(id => id !== hub && linesOf(id).length && !linesOf(id).some(e => linesOf(hub).includes(e)));
  if (!other) { SKIP.reason = 'every claim with a relation shares one with the hub'; return SKIP; }
  await open(p, other);
  assert.deepEqual(on(), linesOf(other), 'only the relations of the claim now selected');
  p.d.querySelector('.atlas-chip-btn[data-atlas-status="conditional"]').click();
  const hidden = new Set(DATA.claims.filter(c => c.status.code !== 'conditional').map(c => c.id));
  for (const e of p.d.querySelectorAll('.atlas-map .atlas-edge[data-edge-id]')) {
    const want = hidden.has(e.getAttribute('data-source')) || hidden.has(e.getAttribute('data-target'));
    assert.equal(e.classList.contains('is-out'), want, 'line ' + e.getAttribute('data-edge-id'));
  }
});

test('no number of claims, percentage or progress word anywhere in the atlas after the checks above', async () => {
  const p = load({ wide: true });
  await settle();
  await open(p, hub);
  assertNoCount(atlasText(p));
});

(async () => {
  let failed = 0;
  let skipped = 0;
  for (const t of tests) {
    if (only && !t.name.includes(only)) continue;
    try {
      const note = await t.fn();
      if (note === SKIP) { skipped++; console.log('SKIP ' + t.name + ': ' + (SKIP.reason || 'the atlas.json lacks what this test needs')); SKIP.reason = ''; continue; }
      console.log((t.observation ? 'OBSERVED ' : 'PASS ') + t.name + (t.observation ? ': ' + note : ''));
    } catch (e) { failed++; console.log('FAIL ' + t.name + '\n      ' + String(e && e.message || e).split('\n').slice(0, 6).join('\n      ')); }
    while (opened.length) { try { opened.pop().window.close(); } catch (e) { /* closed */ } }
  }
  console.log((failed ? `${failed} failed` : 'all passed') + (skipped ? `; ${skipped} skipped` : ''));
  process.exit(failed ? 1 : 0);
})();
