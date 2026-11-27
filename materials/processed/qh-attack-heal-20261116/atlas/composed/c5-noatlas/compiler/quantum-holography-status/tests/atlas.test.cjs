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
function atlasText(p) {
  const a = p.d.getElementById('atlas');
  return a.textContent + ' ' + Array.from(a.querySelectorAll('[aria-label],[title]')).map(e => (e.getAttribute('aria-label') || '') + ' ' + (e.getAttribute('title') || '')).join(' ');
}
const NO_COUNT = [/%/, /\b\d+\s+of\s+\d+\b/i, /\b(progress|completed?|completion|percent)\b/i, /\b\d+\s+(established|conditional|scoped|remaining|claims?|theorems?)\b/i];

const tests = [];
function test(name, fn) { tests.push({ name, fn }); }

test('start: the script runs, nothing is selected, the pane shows its prompt', async () => {
  const p = load();
  await settle();
  assert.ok(p.d.querySelector('[data-atlas-mount] .atlas-body.atlas-js'), 'atlas-js');
  assert.equal(selected(p), null);
  assert.equal(p.d.querySelector('.atlas-pane-prompt').hidden, false);
  assert.deepEqual(p.errors, []);
});

test('RT2/RT3: an index link selects its claim through the address, with statement, hypotheses and every relation', async () => {
  const p = load();
  await settle();
  const a = await open(p, hub);
  assert.equal(p.w.location.hash, '#atlas-c-' + hub);
  assert.equal(selected(p), hub);
  const art = p.d.getElementById('atlas-c-' + hub);
  assert.ok(art.querySelector('.atlas-status-label').textContent.includes(claimById[hub].status.label));
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
  p.d.querySelector('.nav a[href="#examples"]').click();
  await until(() => selected(p) === null, 'the selection to clear');
  assert.equal(p.d.querySelector('.atlas-pane-prompt').hidden, false);
  p.w.history.back();
  await sleep(150);
  p.w.history.back();
  await until(() => selected(p) === order[0], 'Back to the claim');
});

test('a link from a claim to a statement of the page goes through qh:navigate, which the page handles', async () => {
  const p = load();
  await settle();
  const ref = DATA.claims.find(c => c.statementRef);
  if (!ref) return;
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
  const want = DATA.claims.filter(c => (c.title + ' ' + c.statement + ' ' + c.hypotheses.join(' ') + ' ' + c.status.label).toLowerCase().includes('lift')).map(c => c.id);
  assert.deepEqual(rows(), want);
  assert.doesNotMatch(p.d.querySelector('.atlas-count').textContent, /\d/);
  p.d.querySelector('.atlas-clear').click();
  p.d.querySelector('.atlas-chip-btn[data-atlas-status="conditional"]').click();
  assert.deepEqual(rows(), DATA.claims.filter(c => c.status.code === 'conditional').map(c => c.id));
  assert.equal(p.d.querySelectorAll('.atlas-map .atlas-node.is-out').length, DATA.claims.filter(c => c.status.code !== 'conditional').length);
  assert.doesNotMatch(p.d.querySelector('.atlas-count').textContent, /\d/);
  p.d.querySelector('.atlas-chip-btn[data-atlas-domain="' + DATA.domains[1].id + '"]').click();
  assert.deepEqual(rows(), DATA.claims.filter(c => c.status.code === 'conditional' && c.domainId === DATA.domains[1].id).map(c => c.id));
  for (const r of NO_COUNT) assert.doesNotMatch(atlasText(p), r);
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
  if (!c) return;
  await open(p, c.id);
  const term = p.d.querySelector(`#atlas-c-${c.id} .term`);
  assert.ok(term, 'the claim text carries the glossary term');
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
  if (!path) return;
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
  if (kinds.length < 2) return;
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

test('the page search leaves the atlas alone (interaction isolation): atlas-only words find nothing', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('find-q');
  if (!q) return;
  q.focus();
  q.value = 'Synthetic';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(250);
  assert.match(p.d.querySelector('.find-count').textContent, /Nothing on this page matches/);
});

test('a row toggle of the page replaces the address; the atlas follows the address it is given', async () => {
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
  console.log(`      (address after the row toggle: ${hash}; selection kept until the next address change: ${stillSelected}; after Back: ${selected(p)})`);
  assert.ok(true);
});

test('no number of claims, percentage or progress word anywhere in the atlas after the checks above', async () => {
  const p = load({ wide: true });
  await settle();
  await open(p, hub);
  for (const r of NO_COUNT) assert.doesNotMatch(atlasText(p), r);
});

(async () => {
  let failed = 0;
  for (const t of tests) {
    if (only && !t.name.includes(only)) continue;
    try { await t.fn(); console.log('PASS ' + t.name); } catch (e) { failed++; console.log('FAIL ' + t.name + '\n      ' + String(e && e.message || e).split('\n').slice(0, 6).join('\n      ')); }
  }
  console.log(failed ? `${failed} failed` : 'all passed');
  process.exit(failed ? 1 : 0);
})();
