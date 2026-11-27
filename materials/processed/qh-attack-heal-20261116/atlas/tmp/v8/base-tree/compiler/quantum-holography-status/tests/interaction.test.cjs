#!/usr/bin/env node
/* Reader-task tests for the status page's script (status.js), run against a built page:

       NODE_PATH=<a node_modules folder with jsdom> node compiler/quantum-holography-status/tests/interaction.test.cjs <page.html> [name filter]

   Each test loads a fresh copy of the page in jsdom with its script running, dispatches real events (clicks, keys,
   typing, history traversal, print) and checks what the reader is shown. jsdom has no layout: scrolling is recorded
   by a stub of scrollIntoView, and nothing here measures geometry. */
'use strict';
const fs = require('fs');
const assert = require('assert/strict');

let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require('jsdom')); } catch (e) {
  console.error('jsdom is not installed where Node can find it; set NODE_PATH to a node_modules folder that has it.');
  process.exit(2);
}
const file = process.argv[2];
if (!file) { console.error('usage: interaction.test.cjs <page.html> [name filter]'); process.exit(2); }
const only = process.argv[3] || '';
const PAGE = fs.readFileSync(file, 'utf8');
const BASE = 'https://raeez.com/quantum-holography-tracker.html';

/* ---------------------------------------------------------------- harness */

const opened = []; /* every window of a test is closed after it, so no page's timers run into the next test */
function load(opts) {
  opts = opts || {};
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented: navigation/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
  vc.on('error', (...a) => errors.push('console.error: ' + a.join(' ')));
  const dom = new JSDOM(opts.html || PAGE, {
    url: BASE + (opts.url || ''),
    runScripts: opts.noScript ? undefined : 'dangerously',
    pretendToBeVisual: true,
    virtualConsole: vc,
    beforeParse(w) {
      w.__scrolled = [];
      w.Element.prototype.scrollIntoView = function () { w.__scrolled.push(this); };
      if (opts.storage === 'throw') {
        ['localStorage', 'sessionStorage'].forEach(name => Object.defineProperty(w, name, { configurable: true, get() { throw new Error('storage denied'); } }));
      }
      if (opts.storageSeed) Object.keys(opts.storageSeed).forEach(k => w.localStorage.setItem(k, opts.storageSeed[k]));
      if (opts.before) opts.before(w);
    }
  });
  const w = dom.window;
  opened.push(dom);
  return { dom, w, d: w.document, errors };
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
const settle = () => sleep(60);                      /* animation frames and short timers */
function key(target, k, extra) {
  const e = new target.ownerDocument.defaultView.KeyboardEvent('keydown', Object.assign({ key: k, bubbles: true, cancelable: true }, extra || {}));
  target.dispatchEvent(e);
  return e;
}
async function type(page, text) {
  const q = page.d.getElementById('find-q');
  const seen = () => visibleText(page.d.querySelector('.find-count') || page.d.body.ownerDocument.createElement('i')) + '|' + hits(page).length;
  const before = seen();
  q.focus();
  q.value = text;
  q.dispatchEvent(new page.w.Event('input', { bubbles: true }));
  await sleep(150);
  for (let i = 0; i < 40 && seen() === before; i++) await sleep(25);   /* a busy machine runs the search later */
  return q;
}
function visibleText(el) { return (el.textContent || '').replace(/\s+/g, ' ').trim(); }
function hits(page) { return [...page.d.querySelectorAll('#find-results .find-link')]; }
function noErrors(page) { assert.deepEqual(page.errors, [], 'script errors: ' + page.errors.join(' | ')); }

const tests = [];
function test(name, fn) { tests.push({ name, fn }); }

/* ---------------------------------------------------------------- preserved behaviour */

test('theme: the toggle switches the theme and remembers the choice on this device', async () => {
  const p = load();
  await settle();
  p.d.querySelector('.theme').click();
  const first = p.d.documentElement.getAttribute('data-theme');
  assert.ok(first === 'dark' || first === 'light');
  assert.equal(p.w.localStorage.getItem('qh-theme'), first);
  p.d.querySelector('.theme').click();
  assert.notEqual(p.d.documentElement.getAttribute('data-theme'), first);
  noErrors(p);
});

test('theme: with storage refused, the page starts and the toggle still works', async () => {
  const p = load({ storage: 'throw' });
  await settle();
  p.d.querySelector('.theme').click();
  assert.ok(p.d.documentElement.getAttribute('data-theme'));
  assert.ok(p.d.getElementById('find-q'), 'the search is built');
  noErrors(p);
});

test('glossary: a term opens its definition card and Escape closes it, returning focus to the term', async () => {
  const p = load();
  await settle();
  const term = p.d.querySelector('main .term');
  term.focus();
  term.click();
  const card = p.d.getElementById('card');
  assert.equal(card.hidden, false);
  const entry = p.d.getElementById(term.getAttribute('data-term'));
  assert.ok(visibleText(card).includes(visibleText(entry.querySelector('dt'))), 'card shows the term');
  assert.equal(term.getAttribute('aria-expanded'), 'true');
  card.querySelector('a').focus();
  key(p.d.activeElement, 'Escape');
  assert.equal(card.hidden, true);
  assert.equal(p.d.activeElement, term, 'focus returns to the term');
  assert.equal(term.getAttribute('aria-expanded'), 'false');
  noErrors(p);
});

test('table: a mark opens its scope, and arrow keys, Home and End move between marks', async () => {
  const p = load();
  await settle();
  const first = p.d.querySelector('.grid tbody .cell-btn');
  first.focus();
  key(first, 'ArrowRight');
  const second = p.d.activeElement;
  assert.ok(second.classList.contains('cell-btn') && second !== first, 'ArrowRight moves to the next mark');
  key(second, 'ArrowDown');
  assert.equal(p.d.activeElement.closest('tr').rowIndex, second.closest('tr').rowIndex + 1, 'ArrowDown moves one row');
  key(p.d.activeElement, 'End');
  const row = p.d.activeElement.closest('tr');
  assert.equal(p.d.activeElement, [...row.querySelectorAll('button, a[href]')].pop(), 'End goes to the last control of the row');
  key(p.d.activeElement, 'Home');
  assert.equal(p.d.activeElement, row.querySelector('button, a[href]'), 'Home goes to the first control of the row');
  const mark = p.d.querySelector('.grid tbody .cell-btn');
  mark.click();
  const card = p.d.getElementById('card');
  assert.equal(card.hidden, false);
  assert.ok(visibleText(card).length > 10, 'the scope is shown');
  noErrors(p);
});

test('deep link: arriving at a statement inside a closed row opens the row', async () => {
  const probe = load({ noScript: true });
  const st = probe.d.querySelector('details.row .statement[id]');
  const row = st.closest('details.row');
  const p = load({ url: '#' + st.id });
  await settle();
  assert.equal(p.d.getElementById(row.id).open, true);
  noErrors(p);
});

test('deep link: a statement hidden by ?show= is shown on arrival', async () => {
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('.rows .statement[id]')].find(s => s.getAttribute('data-status') !== 'open');
  const p = load({ url: '?show=open#' + st.id });
  await settle();
  const target = p.d.getElementById(st.id);
  assert.equal(target.hidden, false, 'the target is visible');
  assert.equal(target.closest('details.row').open, true);
  noErrors(p);
});

test('print: every disclosure opens for print and returns to the reader\'s state afterwards', async () => {
  const p = load();
  await settle();
  const details = [...p.d.querySelectorAll('main details')];
  details[0].open = true;
  const before = details.map(x => x.open);
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  assert.ok(details.every(x => x.open), 'all open while printing');
  p.w.dispatchEvent(new p.w.Event('afterprint'));
  assert.deepEqual(details.map(x => x.open), before);
  noErrors(p);
});

test('search: words from a statement in a closed row find it, and activating the result opens the row and focuses it', async () => {
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('details.row .statement')].find(s => s.querySelector('.statement-title'));
  const words = visibleText(st.querySelector('.statement-title')).split(' ').filter(x => x.length > 4).slice(0, 3).join(' ');
  const p = load();
  await settle();
  await type(p, words);
  const list = hits(p);
  assert.ok(list.length > 0, 'results for "' + words + '"');
  list[0].click();
  await settle();
  assert.ok(p.d.activeElement && p.d.activeElement.closest('details.row'), 'focus is inside a row');
  assert.equal(p.d.activeElement.closest('details.row').open, true);
  noErrors(p);
});

test('no script: every statement, definition and column scope is in the page and none is hidden', async () => {
  const p = load({ noScript: true });
  const statements = p.d.querySelectorAll('main .statement');
  assert.ok(statements.length > 0);
  assert.equal([...statements].filter(s => s.hidden || s.closest('[hidden]')).length, 0);
  assert.ok(p.d.querySelectorAll('.gloss dd').length > 0);
  const scopes = [...p.d.querySelectorAll('details.row .cell-line')];
  assert.equal(scopes.length, p.d.querySelectorAll('.grid .cell-btn').length, 'every table mark has its scope in its row');
});

/* ---------------------------------------------------------------- explicit states */

function isShown(el) {
  for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
    if (n.hidden || n.classList.contains('visually-hidden')) return false;
    if (n.localName === 'details' && !n.open && !(el.closest('summary') && el.closest('summary').parentElement === n)) return false;
  }
  return true;
}

test('filter: a row the Show filter leaves without statements says so and offers to show all', async () => {
  const p = load();
  await settle();
  p.d.querySelector('.row-tools .filter[data-filter="conditional"]').click();
  await settle();
  const empty = [...p.d.querySelectorAll('details.row[data-filter-empty]')];
  assert.ok(empty.length > 0, 'some rows have no conditional statement');
  const row = empty[0];
  row.open = true;
  const note = row.querySelector('.filter-empty');
  assert.ok(note && isShown(note) && visibleText(note).length > 10, 'the opened row explains why it shows no statement');
  const note2 = p.d.querySelector('.row-tools .filter-note');
  assert.ok(note2 && isShown(note2) && /\d/.test(visibleText(note2)), 'a visible line counts what the filter shows');
  note.querySelector('button').click();
  await settle();
  assert.equal(p.d.querySelectorAll('.rows .statement[hidden]').length, 0, 'every statement is shown again');
  assert.equal(p.w.location.search.includes('show='), false, 'the address no longer carries the filter');
  noErrors(p);
});

test('deep link: every statement has its own address after the script starts', async () => {
  const p = load();
  await settle();
  const st = [...p.d.querySelectorAll('main .statement')];
  assert.equal(st.filter(s => !s.id).length, 0, 'statements without an id');
  const ids = [...p.d.querySelectorAll('[id]')].map(e => e.id);
  assert.equal(new Set(ids).size, ids.length, 'ids are unique');
  noErrors(p);
});

test('deep link: a result for a statement that had no id gives the address of that statement, and the address reopens it', async () => {
  /* a statement the page serves without an id if there is one (the case the script must address), else any */
  const probe = load({ noScript: true });
  const titled = sel => [...probe.d.querySelectorAll(sel)].find(s => s.querySelector('.statement-title'));
  const st = titled('details.row .statement:not([id])') || titled('details.row .statement');
  const title = visibleText(st.querySelector('.statement-title'));
  const p = load();
  await settle();
  await type(p, '"' + title + '"');
  const list = hits(p);
  assert.ok(list.length > 0, 'the exact title is found');
  list[0].click();
  await settle();
  const hash = decodeURIComponent(p.w.location.hash.slice(1));
  const target = p.d.getElementById(hash);
  assert.ok(target && target.classList.contains('statement'), 'the address names the statement, not its row: #' + hash);
  assert.equal(visibleText(target.querySelector('.statement-title')), title);
  const again = load({ url: '#' + hash });
  await settle();
  const t2 = again.d.getElementById(hash);
  assert.ok(t2 && t2.closest('details.row').open, 'arrival at the address opens the row');
  noErrors(p); noErrors(again);
});

test('deep link: an address the page does not have is named, with a search for its words', async () => {
  /* an address no content will have (any page's own ids would do as well, for a term the glossary does not hold) */
  assert.equal(PAGE.includes('zqxjv-lorquim'), false, 'the address used here is absent from the page');
  const p = load({ url: '#term-zqxjv-lorquim' });
  await settle();
  const note = p.d.querySelector('.qh-notice');
  assert.ok(note && isShown(note), 'a notice is shown');
  assert.ok(visibleText(note).includes('#term-zqxjv-lorquim'), 'it names the address');
  const go = [...note.querySelectorAll('button')].find(b => /zqxjv lorquim/i.test(visibleText(b)));
  assert.ok(go, 'it offers a search for the address\'s words');
  go.click();
  await sleep(150);
  assert.equal(p.d.getElementById('find-q').value, 'zqxjv lorquim');
  assert.ok(!p.d.querySelector('#find-results').hidden || /nothing/i.test(visibleText(p.d.querySelector('.find-count'))), 'the search ran');
  noErrors(p);
  const bad = load({ url: '#%E0%A4%A' });
  await settle();
  assert.ok(bad.d.querySelector('.qh-notice'), 'a malformed address is named too');
  noErrors(bad);
  const fine = load({ url: '#examples' });
  await settle();
  const quiet = fine.d.querySelector('.qh-notice');
  assert.ok(!quiet || visibleText(quiet) === '', 'a known address shows no notice');
  noErrors(fine);
});

test('print: a second print request before the first ends still restores the reader\'s state', async () => {
  const p = load();
  await settle();
  const details = [...p.d.querySelectorAll('main details')].filter(x => !x.closest('[data-atlas-mount]'));   /* the page's own */
  const before = details.map(x => x.open);
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  p.w.dispatchEvent(new p.w.Event('afterprint'));
  assert.deepEqual(details.map(x => x.open), before);
  noErrors(p);
});

/* ---------------------------------------------------------------- atlas isolation */

const MOCK_ATLAS = '<section id="atlas-mock" class="section wide atlas" data-atlas-mount aria-labelledby="atlas-mock-h">' +
  '<header class="section-head"><h2 id="atlas-mock-h">Atlas</h2></header>' +
  '<div class="filters"><button type="button" class="filter" data-filter="checked" aria-pressed="false">Only proved</button></div>' +
  '<button type="button" class="link-btn" data-expand="all">Open all</button>' +
  '<article class="statement" data-status="checked"><div class="statement-head"><h4 class="statement-title">Atlas node zqxjv</h4></div>' +
  '<div class="statement-text"><p>Only the atlas says zqxjv.</p></div></article>' +
  '<button type="button" id="atlas-go">Go</button></section>';
function withAtlas() { return PAGE.replace('<section id="results"', MOCK_ATLAS + '<section id="results"'); }

test('atlas: the page does not index, filter or bind what is inside the atlas mount', async () => {
  const p = load({ html: withAtlas() });
  await settle();
  await type(p, 'zqxjv');
  assert.equal(hits(p).length, 0, 'atlas text is not a search unit');
  const chip = p.d.querySelector('#atlas-mock .filter');
  chip.click();
  await settle();
  assert.equal(p.d.querySelectorAll('.rows .statement[hidden]').length, 0, 'an atlas chip does not filter the rows');
  assert.equal(p.w.location.search.includes('show='), false);
  const rowsBefore = p.d.querySelectorAll('details.row[open]').length;
  p.d.querySelector('#atlas-mock [data-expand]').click();
  assert.equal(p.d.querySelectorAll('details.row[open]').length, rowsBefore, 'an atlas Open all does not open the rows');
  assert.ok(p.d.getElementById('atlas-mock').querySelector('.statement').id === '', 'no anchor is added inside the atlas');
  noErrors(p);
});

test('atlas: qh:navigate reveals a page anchor with history, focus and focus return on Back', async () => {
  const probe = load({ noScript: true });
  const st = probe.d.querySelector('details.row .statement[id]');
  const p = load({ html: withAtlas() });
  await settle();
  const states = [];
  p.d.addEventListener('qh:state', e => states.push(e.detail));
  const go = p.d.getElementById('atlas-go');
  go.focus();
  const ev = new p.w.CustomEvent('qh:navigate', { bubbles: true, cancelable: true, detail: { id: st.id } });
  const notHandled = go.dispatchEvent(ev);
  await settle();
  assert.equal(notHandled, false, 'the page handles the request');
  assert.equal(p.w.location.hash, '#' + st.id);
  const target = p.d.getElementById(st.id);
  assert.ok(target.closest('details.row').open, 'the row is opened');
  assert.equal(p.d.activeElement, target, 'focus is on the target');
  p.w.history.back();
  for (let i = 0; i < 40 && p.d.activeElement !== go; i++) await sleep(25);
  assert.equal(p.d.activeElement, go, 'Back returns focus to the atlas control');
  assert.ok(states.length > 0, 'qh:state is announced');
  noErrors(p);
});

/* ---------------------------------------------------------------- helpers for content-derived inputs */

/* Words of an element without its formulae (annotation text excluded). */
function plainText(el) {
  const c = el.cloneNode(true);
  c.querySelectorAll('math, svg, annotation').forEach(n => n.remove());
  return (c.textContent || '').replace(/\s+/g, ' ').trim();
}
/* Visible text of a result link: formulae by their symbols, never by their TeX. */
function shownText(el) {
  const c = el.cloneNode(true);
  c.querySelectorAll('annotation, svg').forEach(n => n.remove());
  return (c.textContent || '').replace(/\s+/g, ' ').trim();
}
/* n consecutive plain words from the longest text node under el (no formula or markup inside the phrase). */
function samplePhrase(el, n) {
  n = n || 4;
  const w = el.ownerDocument.createTreeWalker(el, 4);
  let best = '';
  for (let t = w.nextNode(); t; t = w.nextNode()) {
    if (t.parentElement.closest('math, svg, .status-chip, .note-label, .added-chip, .cell-col, .cell-st')) continue;
    if (t.nodeValue.length > best.length) best = t.nodeValue;
  }
  const words = best.split(' ');
  for (let i = 1; i + n <= words.length; i++) {
    const run = words.slice(i, i + n);
    if (run.every(x => /^[A-Za-z][A-Za-z-]{2,}$/.test(x))) return run.join(' ');
  }
  return null;
}
function hitFor(page, el) {
  return hits(page).find(a => {
    const t = page.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    return t && (t === el || t.contains(el));
  });
}
function countText(p) { return visibleText(p.d.querySelector('.find-count')); }

/* ---------------------------------------------------------------- search: coverage, matching, ranking, context */

test('search: words read in the lead, the status key and a section introduction are found where they are', async () => {
  const p = load();
  await settle();
  const samples = [p.d.querySelector('main > .lead > p'), p.d.querySelector('#status .key-item dd'),
                   ...p.d.querySelectorAll('main section.section > .section-intro')].filter(el => el && !el.closest('[data-atlas-mount]'));
  assert.ok(samples.length >= 3);
  for (const el of samples) {
    const phrase = samplePhrase(el);
    if (!phrase) continue;
    await type(p, '"' + phrase + '"');
    assert.ok(hitFor(p, el), 'found "' + phrase + '" in its own part (' + countText(p) + ')');
  }
  noErrors(p);
});

test('search: a counterexample result is shown as false, with its witness as the counterexample', async () => {
  const p = load();
  await settle();
  const f = p.d.querySelector('.failure');
  const phrase = samplePhrase(f.querySelector('.claim-text'), 3);
  await type(p, '"' + phrase + '"');
  const a = hitFor(p, f);
  assert.ok(a, 'the claim is found');
  const where = visibleText(a.querySelector('.find-where'));
  assert.ok(where.startsWith(visibleText(f.querySelector('.claim-tag'))), 'the result begins with the page\'s own label: ' + where);
  noErrors(p);
});

test('search: a snippet keeps the formulae around the match as formulae', async () => {
  const p = load();
  await settle();
  /* a statement whose first paragraph has a formula with a subscript or superscript after some plain words */
  const st = [...p.d.querySelectorAll('main .rows .statement[id], main .principal .statement[id]')].find(s => {
    const para = s.querySelector('.statement-text p');
    return para && para.querySelector('msub, msup, msubsup') && samplePhrase(para, 3);
  });
  assert.ok(st, 'a statement with structured formulae');
  const para = st.querySelector('.statement-text p');
  await type(p, '"' + samplePhrase(para, 3) + '"');
  const a = hitFor(p, st);
  assert.ok(a, 'found');
  const snip = a.querySelector('.find-snippet');
  assert.ok(snip && snip.querySelector('math'), 'the snippet carries MathML, not flattened symbols');
  noErrors(p);
});

test('search: the words of a status label and of a note label find the statements that carry them', async () => {
  const p = load();
  await settle();
  const label = visibleText(p.d.querySelector('.statement[data-status="open"] .status-chip'));
  const open = p.d.querySelectorAll('main .statement[data-status="open"]').length;
  await type(p, '"' + label + '"');
  const n = parseInt(countText(p), 10);
  assert.ok(n >= open, '"' + label + '" finds ' + n + ' of at least ' + open);
  const noted = [...p.d.querySelectorAll('main .statement')].find(s => s.querySelector('.statement-notes .note-label'));
  const noteLabel = visibleText(noted.querySelector('.note-label')).replace(/[:.]$/, '');
  const word = (plainText(noted.querySelector('.statement-notes')).replace(noteLabel, '').match(/[A-Za-z]{5,}/) || [])[0];
  await type(p, noteLabel + ' ' + word);
  assert.ok(hits(p).length > 0, 'note label with a word of the note: ' + noteLabel + ' ' + word);
  noErrors(p);
});

test('search: punctuation alone and a single letter search nothing and say so; a single symbol is searched', async () => {
  const p = load();
  await settle();
  for (const q of ['.', '?', '(', 'x']) {
    await type(p, q);
    assert.equal(hits(p).length, 0, q + ' lists nothing');
    assert.ok(/at least/i.test(countText(p)), q + ' says why: ' + countText(p));
  }
  const greek = [...p.d.querySelectorAll('main mi')].map(m => m.textContent).find(t => /^[α-ω]$/.test(t));
  await type(p, greek);
  assert.ok(hits(p).length > 0, 'the symbol ' + greek + ' is found');
  noErrors(p);
});

test('search: curly quotes and an unclosed quote make a phrase as straight quotes do', async () => {
  const p = load();
  await settle();
  const phrase = samplePhrase(p.d.querySelector('main .rows .statement .statement-text'), 3);
  await type(p, '"' + phrase + '"');
  const straight = hits(p).length;
  assert.ok(straight > 0);
  await type(p, '“' + phrase + '”');
  assert.equal(hits(p).length, straight, 'curly quotes');
  await type(p, '"' + phrase);
  assert.ok(hits(p).length >= straight, 'a phrase still being typed');
  noErrors(p);
});

test('search: a word is not found through the name of a TeX command, and a short word must begin a word', async () => {
  const p = load();
  await settle();
  await type(p, 'times');
  hits(p).forEach(a => assert.ok(/times/i.test(shownText(a)), 'every result shows the word: ' + shownText(a).slice(0, 80)));
  await type(p, 'ring');
  assert.ok(hits(p).length > 0);
  hits(p).forEach(a => assert.ok(/(^|[^a-z0-9])ring/i.test(shownText(a)), 'a word starting "ring": ' + shownText(a).slice(0, 80)));
  noErrors(p);
});

test('search: a TeX query finds the formulae that contain it and names that it matched in a formula', async () => {
  const p = load();
  await settle();
  const ann = [...p.d.querySelectorAll('main .statement annotation')].map(a => a.textContent).find(t => /\\mathfrak\{/.test(t));
  const cmd = ann ? '\\mathfrak' : '\\otimes';
  await type(p, cmd);
  assert.ok(hits(p).length > 0, cmd + ' is found');
  hits(p).slice(0, 10).forEach(a => assert.ok(visibleText(a.querySelector('.find-where')).includes('formula'), 'named as a formula match'));
  noErrors(p);
});

test('search: a defined term typed in full puts its definition first, and the Part chips count where the matches are', async () => {
  const p = load();
  await settle();
  const g = [...p.d.querySelectorAll('.gloss')].find(x => !x.querySelector('dt math') && plainText(x.querySelector('dt')).split(' ').length >= 2);
  const term = plainText(g.querySelector('dt'));
  await type(p, '"' + term + '"');
  assert.equal(decodeURIComponent(hits(p)[0].getAttribute('href').slice(1)), g.id, 'first result is the definition of ' + term);
  const chip = p.d.querySelector('.find .filter[data-scope="terms"]');
  assert.ok(/\d/.test(visibleText(chip)), 'the Terms chip shows a count: ' + visibleText(chip));
  noErrors(p);
});

test('search: the essay title is one result, and the "why it matters" label is not a match', async () => {
  const p = load();
  await settle();
  const title = plainText(p.d.getElementById('essay-title'));
  await type(p, '"' + title + '"');
  const essayHits = hits(p).filter(a => p.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))).closest('#essay'));
  assert.equal(essayHits.length, 1, 'one essay result for its title');
  const why = visibleText(p.d.querySelector('.question-why-label'));
  await type(p, '"' + why + '"');
  assert.ok(hits(p).length < p.d.querySelectorAll('.question').length, 'the label alone does not match every question');
  noErrors(p);
});

test('search: a column\'s scope in a row is its own result, naming the column and its status', async () => {
  const p = load();
  await settle();
  const li = [...p.d.querySelectorAll('details.row .cell-line')].find(x => x.querySelector('.cell-text') && samplePhrase(x.querySelector('.cell-text'), 3));
  const phrase = samplePhrase(li.querySelector('.cell-text'), 3);
  await type(p, '"' + phrase + '"');
  const a = hits(p).find(h => h.getAttribute('href') === '#' + li.id);
  assert.ok(a, 'the scope line is the result (#' + li.id + ')');
  const where = visibleText(a.querySelector('.find-where'));
  assert.ok(where.includes(visibleText(li.querySelector('.cell-col'))) && where.includes(visibleText(li.querySelector('.cell-st'))), where);
  noErrors(p);
});

test('search: a column definition result names the column definitions as its place', async () => {
  const p = load();
  await settle();
  const def = p.d.querySelector('.col-def');
  await type(p, '"' + plainText(def.querySelector('dt')) + '"');
  const a = hitFor(p, def);
  assert.ok(a && visibleText(a.querySelector('.find-where')).includes(visibleText(p.d.querySelector('.col-defs > summary'))));
  noErrors(p);
});

test('search: the count is announced once typing pauses, not at every keystroke', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('find-q');
  const live = p.d.querySelector('.find [role="status"]');
  let updates = 0;
  new p.w.MutationObserver(() => updates++).observe(live, { childList: true, characterData: true, subtree: true });
  q.focus();
  for (const ch of 'siegel weil') {
    q.value += ch;
    q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
    await sleep(140);
  }
  await sleep(900);
  assert.ok(updates <= 2, 'announcements: ' + updates);
  assert.ok(visibleText(live).length > 0, 'the final count is announced');
  noErrors(p);
});

test('search: Enter in the field moves to the first result and leaves the address as it was', async () => {
  const p = load();
  await settle();
  const q = await type(p, 'fusion');
  const before = p.w.location.hash;
  key(q, 'Enter');
  await settle();
  assert.equal(p.d.activeElement, hits(p)[0], 'focus on the first result');
  assert.equal(p.w.location.hash, before);
  noErrors(p);
});

test('search: results are named by title and place and described by the words around the match', async () => {
  const p = load();
  await settle();
  await type(p, 'fusion');
  hits(p).slice(0, 5).forEach(a => {
    a.getAttribute('aria-labelledby').split(' ').forEach(id => assert.ok(p.d.getElementById(id), 'label part ' + id));
    const d = a.getAttribute('aria-describedby');
    if (d) assert.ok(p.d.getElementById(d));
  });
  noErrors(p);
});

test('search: ArrowDown on the last shown result reaches Show all', async () => {
  const p = load();
  await settle();
  await type(p, 'the');
  const list = hits(p);
  assert.equal(list.length, 40);
  list[39].focus();
  key(list[39], 'ArrowDown');
  assert.ok(p.d.activeElement.classList.contains('find-more'));
  p.d.activeElement.click();
  await settle();
  assert.equal(p.d.activeElement, hits(p)[40], 'Show all moves to the first newly shown result');
  noErrors(p);
});

/* ---------------------------------------------------------------- cards and the table */

test('table: the table is one stop for the Tab key, and its scroll box is not another', async () => {
  const p = load();
  await settle();
  const wrap = p.d.querySelector('.grid-wrap');
  const stops = [...wrap.querySelectorAll('a[href], button, [tabindex]')].filter(x => x.tabIndex >= 0);
  assert.equal(stops.length, 1, 'tab stops in the table: ' + stops.length);
  assert.equal(wrap.tabIndex, -1);
  const mark = p.d.querySelectorAll('.grid tbody .cell-btn')[5];
  mark.focus();
  assert.equal(mark.tabIndex, 0, 'the stop follows focus');
  assert.equal(stops[0].tabIndex, -1);
  key(mark, 'End', { ctrlKey: true });
  const controls = p.d.querySelectorAll('.grid thead button, .grid tbody th a[href], .grid tbody td button');
  assert.equal(p.d.activeElement, controls[controls.length - 1], 'Control+End reaches the last control');
  noErrors(p);
});

test('table: the mark in focus lights its row and its column, and moving on moves the light', async () => {
  const p = load();
  await settle();
  const btn = p.d.querySelectorAll('.grid tbody tr')[3].querySelectorAll('.cell-btn')[2];
  btn.focus();
  const td = btn.closest('td');
  const ci = td.cellIndex;
  assert.equal(td.getAttribute('data-cross'), 'both');
  [...p.d.querySelector('.grid').rows].forEach(r => assert.ok(r.cells[ci].hasAttribute('data-cross'), 'column lit in every row'));
  [...td.parentNode.cells].forEach(c => assert.ok(c.hasAttribute('data-cross'), 'row lit'));
  key(btn, 'ArrowRight');
  assert.ok(!td.hasAttribute('data-cross') || td.getAttribute('data-cross') === 'row', 'the previous column is no longer lit');
  assert.equal(p.d.activeElement.closest('td').getAttribute('data-cross'), 'both');
  noErrors(p);
});

test('table: each legend entry follows one status across the table, with its count', async () => {
  const p = load();
  await settle();
  const lenses = [...p.d.querySelectorAll('.legend .lens')];
  assert.ok(lenses.length >= 3, 'the legend entries are switches');
  const cells = [...p.d.querySelectorAll('.grid td.cell[data-status]')];
  lenses.forEach(b => assert.equal(b.querySelector('.count').textContent, String(cells.filter(c => c.getAttribute('data-status') === b.getAttribute('data-lens')).length)));
  const b = lenses.find(x => x.getAttribute('data-lens') === 'partial') || lenses[0];
  b.click();
  const st = b.getAttribute('data-lens');
  assert.equal(b.getAttribute('aria-pressed'), 'true');
  cells.forEach(c => assert.equal(c.hasAttribute('data-lit'), c.getAttribute('data-status') === st));
  assert.ok(/Marked \d+ of the \d+/.test(visibleText(p.d.querySelector('.grid-legend [role="status"]'))));
  b.click();
  assert.equal(p.d.querySelectorAll('.grid td[data-lit]').length, 0);
  assert.equal(p.d.querySelector('.grid').hasAttribute('data-lens'), false);
  const plain = load({ noScript: true });
  assert.equal(plain.d.querySelectorAll('.legend button').length, 0, 'without the script the legend is a plain list');
  noErrors(p);
});

test('table: each mark is described by its scope, and no name is read as TeX', async () => {
  const p = load();
  await settle();
  p.d.querySelectorAll('.grid .cell-btn').forEach(b => {
    const d = p.d.getElementById(b.getAttribute('aria-describedby'));
    assert.ok(d && b.closest('td').contains(d), 'scope of ' + b.getAttribute('aria-label'));
    assert.ok(!/\\[()[\]]/.test(b.getAttribute('aria-label')), b.getAttribute('aria-label'));
  });
  [...p.d.querySelectorAll('main .term[data-term]')].filter(t => !t.closest('[data-atlas-mount]')).forEach(t => {   /* the page's own */
    const d = p.d.getElementById(t.getAttribute('aria-describedby'));
    assert.ok(d && d.localName === 'dd', 'definition of ' + t.textContent);
  });
  noErrors(p);
});

test('card: the link to a row whose name has a formula reads as the row name', async () => {
  const p = load();
  await settle();
  const rowLink = [...p.d.querySelectorAll('.grid tbody th a')].find(a => a.querySelector('math'));
  if (!rowLink) return; /* no such row in this content */
  const cell = rowLink.closest('tr').querySelector('.cell-btn');
  cell.click();
  const more = p.d.querySelector('#card .card-more');
  assert.equal(shownText(more), shownText(rowLink));
  assert.ok(more.querySelector('math'), 'the formula is kept');
  noErrors(p);
});

test('card: a pinned card closes when focus moves on, so Escape does not send focus back to it', async () => {
  const p = load();
  await settle();
  const heads = p.d.querySelectorAll('.col-head');
  heads[0].focus();
  heads[0].click();
  assert.equal(p.d.getElementById('card').hidden, false);
  heads[1].focus();
  assert.ok(p.d.getElementById('card').hidden === false && p.d.querySelector('#card').textContent.includes(plainText(p.d.getElementById('col-' + heads[1].getAttribute('data-col')).querySelector('dt'))),
            'the card now shows the focused head');
  key(heads[1], 'Escape');
  assert.equal(p.d.activeElement, heads[1], 'Escape keeps focus where it is');
  const term = p.d.querySelector('#results .term');
  term.focus();
  term.click();
  key(term, '/');
  assert.equal(p.d.activeElement, p.d.getElementById('find-q'));
  assert.equal(p.d.getElementById('card').hidden, true, 'the card closed when focus left its term');
  key(p.d.activeElement, 'Escape');
  assert.equal(p.d.activeElement, term, 'Escape on the empty search returns to where / was pressed');
  noErrors(p);
});

/* ---------------------------------------------------------------- address, history, focus return */

test('filter: a link to a statement the Show filter hides shows it and keeps the filter and the address', async () => {
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('.rows .statement[id]')].find(s => s.getAttribute('data-status') !== 'checked');
  const p = load({ url: '?show=checked#' + st.id });
  await settle();
  const t = p.d.getElementById(st.id);
  assert.equal(t.hidden, false);
  assert.ok(t.hasAttribute('data-filter-exempt'));
  assert.ok(p.w.location.search.includes('show=checked'), 'the shared address keeps its filter: ' + p.w.location.search);
  assert.equal(p.d.querySelector('.row-tools .filter[data-filter="checked"]').getAttribute('aria-pressed'), 'true');
  noErrors(p);
});

test('filter: turning the Show filter on and off returns the rows to the reader\'s own state', async () => {
  const p = load();
  await settle();
  const rows = [...p.d.querySelectorAll('details.row')];
  rows[1].open = true;
  rows[6].open = true;
  const chip = p.d.querySelector('.row-tools .filter[data-filter="published"]');
  chip.click();
  chip.click();
  assert.deepEqual(rows.map((d, i) => d.open ? i : -1).filter(i => i >= 0), [1, 6]);
  noErrors(p);
});

test('filter: focus inside a statement that the filter hides moves to its row', async () => {
  const p = load();
  await settle();
  const st = [...p.d.querySelectorAll('.rows .statement')].find(s => s.getAttribute('data-status') === 'checked');
  st.closest('details.row').open = true;
  st.setAttribute('tabindex', '-1');
  st.focus();
  p.d.querySelector('.row-tools .filter[data-filter="open"]').click();
  assert.ok(st.hidden);
  assert.equal(p.d.activeElement, st.closest('details.row').querySelector('summary'));
  noErrors(p);
});

test('address: unknown filter values are named and dropped, a one-letter query explains itself, #find-q opens the search', async () => {
  const p = load({ url: '?in=bogus&status=nope' });
  await settle();
  const note = p.d.querySelector('.qh-notice');
  assert.ok(/bogus/.test(visibleText(note)) && /nope/.test(visibleText(note)), 'named: ' + visibleText(note));
  assert.ok(!/in=|status=/.test(p.w.location.search), 'dropped from the address: ' + p.w.location.search);
  assert.ok(!/Nothing/.test(countText(p)), 'no unexplained empty result');
  const a = load({ url: '?q=a' });
  await settle();
  assert.ok(/at least/i.test(countText(a)), countText(a));
  const f = load({ url: '#find-q' });
  await settle();
  assert.equal(f.d.activeElement, f.d.getElementById('find-q'));
  const c = load({ url: '#card' });
  await settle();
  assert.ok(/#card/.test(visibleText(c.d.querySelector('.qh-notice'))), 'a hidden element is not a silent target');
  [p, a, f, c].forEach(noErrors);
});

test('address: a link to the address already shown reopens the row it names', async () => {
  const probe = load({ noScript: true });
  const row = probe.d.querySelector('details.row');
  const p = load({ url: '#' + row.id });
  await settle();
  p.d.querySelector('#examples [data-expand="none"]').click();
  assert.equal(p.d.getElementById(row.id).open, false);
  p.d.querySelector('.grid tbody th a[href="#' + row.id + '"]').click();
  assert.equal(p.d.getElementById(row.id).open, true);
  noErrors(p);
});

test('history: opening a row from a section address keeps that address for Back', async () => {
  const p = load();
  await settle();
  p.d.querySelector('.nav a[href="#examples"]').click();
  await settle();
  p.d.querySelector('details.row > summary').click();
  await settle();
  assert.ok(/^#row-/.test(p.w.location.hash));
  p.w.history.back();
  await sleep(120);
  assert.equal(p.w.location.hash, '#examples');
  noErrors(p);
});

test('history: Back after a search result returns focus to that result and closes what the result opened', async () => {
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('details.row .statement[id]')].find(s => samplePhrase(s.querySelector('.statement-text'), 3));
  const phrase = samplePhrase(st.querySelector('.statement-text'), 3);
  const p = load();
  await settle();
  await type(p, '"' + phrase + '"');
  const a = hitFor(p, p.d.getElementById(st.id));
  a.focus();
  a.click();
  await settle();
  const row = p.d.getElementById(st.id).closest('details.row');
  assert.equal(row.open, true);
  assert.equal(p.w.location.hash, '#' + st.id);
  p.w.history.back();
  await sleep(150);
  assert.equal(p.d.activeElement, hitFor(p, p.d.getElementById(st.id)), 'focus is back on the result');
  assert.equal(row.open, false, 'the row the result opened is closed again');
  p.w.history.forward();
  await sleep(150);
  assert.equal(row.open, true, 'Forward opens it again');
  noErrors(p);
});

test('history: two results in one row are two entries, each with its own address', async () => {
  /* a row with at least two statements that the page serves without an id */
  const probe = load({ noScript: true });
  const pick = sel => [...probe.d.querySelectorAll('details.row')].find(d => d.querySelectorAll(sel).length >= 2);
  const sel = pick('.statement:not([id]) .statement-title') ? '.statement:not([id]) .statement-title' : '.statement .statement-title';
  const row = pick(sel);
  const titles = [...row.querySelectorAll(sel)].map(t => plainText(t));
  const name = plainText(row.querySelector('.row-name'));
  const p = load();
  await settle();
  await type(p, '"' + name + '"');
  const inRow = hits(p).filter(a => titles.includes(plainText(a.querySelector('.find-title'))));
  assert.ok(inRow.length >= 2, 'results for the row\'s statements');
  inRow.forEach(a => {
    const t = p.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    assert.ok(t && t.matches('.statement'), 'the result\'s address names the statement, not its row: ' + a.getAttribute('href'));
  });
  const len = p.w.history.length;
  const first = inRow[0].getAttribute('href');
  const second = inRow[1].getAttribute('href');
  inRow[0].click();
  await settle();
  hitFor(p, p.d.getElementById(decodeURIComponent(second.slice(1)))).click();
  await settle();
  assert.equal(p.w.history.length, len + 2);
  p.w.history.back();
  await sleep(120);
  assert.equal(p.w.location.hash, first);
  noErrors(p);
});

test('history: a search typed just before Back is not written into the entry Back returns to', async () => {
  const p = load({ url: '#results' });
  await settle();
  p.d.querySelector('.nav a[href="#examples"]').click();
  await settle();
  await type(p, 'genus');
  p.w.history.back();
  await sleep(600);
  assert.ok(!p.w.location.search.includes('q='), p.w.location.href);
  noErrors(p);
});

test('history: a search typed just before following a link stays with the entry it was typed in', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('find-q');
  q.focus();
  q.value = 'genus';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(130);
  p.d.querySelector('.nav a[href="#terms"]').click();
  await sleep(450);
  p.w.history.back();
  await sleep(150);
  assert.equal(p.d.getElementById('find-q').value, 'genus');
  noErrors(p);
});

test('history: a result hidden by the Show filter keeps the filter in the entry left behind', async () => {
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('.rows .statement[id]')].find(s => s.getAttribute('data-status') !== 'published' && samplePhrase(s.querySelector('.statement-text'), 3));
  const phrase = samplePhrase(st.querySelector('.statement-text'), 3);
  const p = load({ url: '?show=published' });
  await settle();
  await type(p, '"' + phrase + '"');
  hitFor(p, p.d.getElementById(st.id)).click();
  await settle();
  p.w.history.back();
  await sleep(150);
  assert.ok(p.w.location.search.includes('show=published'), p.w.location.search);
  assert.equal(p.d.querySelector('.row-tools .filter[data-filter="published"]').getAttribute('aria-pressed'), 'true');
  noErrors(p);
});

test('history: a tally link is a new entry; Back returns to the page as it was', async () => {
  const p = load();
  await settle();
  p.d.querySelector('.nav a[href="#results"]').click();
  await settle();
  const len = p.w.history.length;
  const tally = p.d.querySelector('.tally a[data-filter]');
  tally.click();
  await settle();
  assert.equal(p.w.history.length, len + 1);
  assert.ok(p.w.location.search.includes('status=' + tally.getAttribute('data-filter')) && !p.w.location.hash);
  p.w.history.back();
  await sleep(150);
  assert.equal(p.w.location.hash, '#results');
  assert.equal(countText(p), '');
  assert.equal(p.d.activeElement, tally, 'focus returns to the tally link');
  noErrors(p);
});

test('history: Back after a link in the bar returns focus to that link, also when a search has changed the page above', async () => {
  const p = load();
  await settle();
  const link = p.d.querySelector('.nav a[href="#open"]');
  link.focus();
  link.click();
  await settle();
  await type(p, 'fusion'); /* results now fill the page above the link's target */
  p.w.history.back();
  await sleep(150);
  assert.equal(p.d.activeElement, link);
  noErrors(p);
});

test('history: following a term\'s card to the glossary and going Back returns focus to the term', async () => {
  const p = load();
  await settle();
  const term = p.d.querySelector('#results .term');
  term.focus();
  term.click();
  const more = p.d.querySelector('#card .card-more');
  more.focus(); /* a keyboard reader enters the card, then follows its link */
  more.click();
  await settle();
  p.w.history.back();
  await sleep(150);
  assert.equal(p.d.activeElement, term);
  noErrors(p);
});

/* ---------------------------------------------------------------- reading state */

test('reading: open disclosures are kept in the history entry and restored on reload', async () => {
  const p = load();
  await settle();
  const rows = [...p.d.querySelectorAll('details.row')];
  rows[2].open = true;
  rows[5].open = true;
  await sleep(250);
  const state = p.w.history.state;
  assert.deepEqual([...state.qh.open].filter(k => /^row-/.test(k)), [rows[2].id, rows[5].id]);
  const again = load({ before(w) {
    w.history.replaceState(state, '');
    w.performance.getEntriesByType = () => [{ type: 'reload' }];
  } });
  await settle();
  const r2 = [...again.d.querySelectorAll('details.row')];
  assert.deepEqual(r2.map((d, i) => d.open ? i : -1).filter(i => i >= 0), [2, 5]);
  noErrors(p); noErrors(again);
});

test('reading: the place where reading stopped is offered on a later visit, and Continue goes there', async () => {
  const probe = load({ noScript: true });
  const st = probe.d.querySelectorAll('details.row .statement[id]')[3];
  const p = load({ before(w) { w.document.elementFromPoint = function () { return w.document.getElementById(st.id); }; } });
  await settle();
  p.w.dispatchEvent(new p.w.Event('scroll'));
  await sleep(800);
  const saved = p.w.localStorage.getItem('qh-place');
  assert.ok(saved && JSON.parse(saved).id === st.id, 'saved: ' + saved);
  const later = load({ storageSeed: { 'qh-place': saved } });
  await settle();
  const note = later.d.querySelector('.qh-notice');
  assert.ok(visibleText(note).includes(plainText(st.querySelector('.statement-title')).slice(0, 30)), visibleText(note));
  [...note.querySelectorAll('button')][0].click();
  await settle();
  assert.equal(later.w.location.hash, '#' + st.id);
  assert.equal(later.d.activeElement, later.d.getElementById(st.id));
  assert.ok(later.d.getElementById(st.id).closest('details.row').open);
  const linked = load({ url: '#examples', storageSeed: { 'qh-place': saved } });
  await settle();
  assert.equal(visibleText(linked.d.querySelector('.qh-notice')), '', 'no offer when the address names a place');
  [p, later, linked].forEach(noErrors);
});

/* ---------------------------------------------------------------- robustness and isolation */

test('robustness: a malformed row in the page does not break search or the address target', async () => {
  const probe = load({ noScript: true });
  const st = probe.d.querySelector('details.row .statement[id]');
  const html = PAGE.replace('<div class="statements principal">', '<details class="row" id="odd-row"><summary>Odd</summary></details><div class="statements principal">');
  const p = load({ html, url: '?q=genus#' + st.id });
  await settle();
  assert.ok(p.d.getElementById(st.id).closest('details.row').open, 'the target opened');
  assert.ok(/match/.test(countText(p)), countText(p));
  noErrors(p);
});

test('atlas: page listeners leave the atlas\'s own links, keys and focus alone', async () => {
  const atlas = MOCK_ATLAS.replace('</section>', '<table class="grid"><tr><td><button type="button" id="atlas-n1">n1</button></td>' +
    '<td><button type="button" id="atlas-n2">n2</button></td></tr></table><a class="term" id="atlas-term" href="#atlas-mock-h">t</a>' +
    '<input id="atlas-input"><details id="atlas-panel"><summary>panel</summary><p>x</p></details></section>');
  const p = load({ html: PAGE.replace('<section id="results"', atlas + '<section id="results"') });
  await settle();
  const ev = new p.w.MouseEvent('click', { bubbles: true, cancelable: true });
  p.d.getElementById('atlas-term').dispatchEvent(ev);
  assert.equal(ev.defaultPrevented, false, 'an atlas link is not turned into a glossary card');
  const inp = p.d.getElementById('atlas-input');
  inp.focus();
  assert.equal(key(inp, '/').defaultPrevented, false, '/ typed in the atlas stays in the atlas');
  const n1 = p.d.getElementById('atlas-n1');
  n1.focus();
  assert.equal(key(n1, 'ArrowRight').defaultPrevented, false, 'the page does not drive an atlas table');
  const mark = p.d.querySelector('#examples .grid tbody .cell-btn');
  mark.focus();
  key(mark, 'ArrowRight');
  assert.notEqual(p.d.activeElement, mark, 'the page table still moves');
  const term = p.d.querySelector('#results .term');
  term.focus();
  term.click();
  n1.focus();
  key(n1, 'Escape');
  assert.equal(p.d.activeElement, n1, 'Escape in the atlas keeps focus in the atlas');
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  assert.equal(p.d.getElementById('atlas-panel').open, false, 'printing leaves the atlas\'s own disclosures to it');
  p.w.dispatchEvent(new p.w.Event('afterprint'));
  noErrors(p);
});

test('atlas: an unknown address the atlas claims shows no notice', async () => {
  const p = load({ html: withAtlas(), url: '#atlas-mock-node-17', before(w) {
    w.document.addEventListener('qh:unknown-anchor', e => { if (/^atlas-mock-/.test(e.detail.id)) e.preventDefault(); });
  } });
  await settle();
  assert.equal(visibleText(p.d.querySelector('.qh-notice')), '');
  noErrors(p);
});

test('atlas: text the atlas offers is searchable, and a result asks the atlas to show it', async () => {
  const offered = MOCK_ATLAS.replace('</section>', '<div id="atlas-domain-x" data-qh-unit><h3 data-qh-unit-title>Domain qwvyxz</h3>' +
    '<p>Offered words lorquim.</p></div></section>');
  const html = PAGE.replace('<section id="results"', offered + '<section id="results"')
    .replace('<li><a href="#results">', '<li><a href="#atlas-mock">Atlas</a></li><li><a href="#results">');
  const p = load({ html });
  await settle();
  let asked = null;
  p.d.getElementById('atlas-mock').addEventListener('qh:reveal', e => { asked = e.detail.id; e.preventDefault(); });
  await type(p, 'lorquim');
  const list = hits(p);
  assert.equal(list.length, 1, 'the offered unit is found');
  assert.equal(list[0].getAttribute('href'), '#atlas-domain-x');
  await type(p, 'zqxjv');
  assert.equal(hits(p).length, 0, 'text the atlas does not offer stays out of the search');
  await type(p, 'lorquim');
  hits(p)[0].click();
  await settle();
  assert.equal(asked, 'atlas-domain-x', 'the atlas is asked to show its element');
  assert.equal(p.w.location.hash, '#atlas-domain-x');
  noErrors(p);
});

test('search: words typed in the order they are written put the results that hold them together first', async () => {
  const p = load();
  await settle();
  const q = p.d.getElementById('find-q');
  q.focus();
  const run = text => {                                /* Enter runs the search at once */
    q.value = text;
    q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
    key(q, 'Enter');
    q.focus();
    return hits(p);
  };
  const target = a => p.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
  const holds = (el, phrase) => !!el && new RegExp(phrase.toLowerCase().split(' ')
    .map(x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('[\\s,;:]+')).test(shownText(el).toLowerCase());
  const statements = [...p.d.querySelectorAll('main .statement')].filter(st => !st.closest('[data-atlas-mount]'));
  let tried = 0;
  for (let i = 0; i < statements.length; i += 7) {
    const st = statements[i];
    const phrase = samplePhrase(st, 4);
    if (!phrase) continue;
    tried++;
    const list = run(phrase);
    assert.ok(list.length && holds(target(list[0]), phrase), 'the first result for "' + phrase + '" holds it in its own words');
    const at = list.findIndex(a => { const t = target(a); return t === st || (t && t.matches('.question, .failure') && st.closest('.question, .failure') === t); });
    assert.ok(at >= 0, '"' + phrase + '" finds its statement');
    const group = list[at].closest('.find-group');
    list.slice(0, at).filter(a => a.closest('.find-group') === group).forEach(a =>
      assert.ok(holds(target(a), phrase), 'in its part, only results that hold "' + phrase + '" come before its statement'));
  }
  assert.ok(tried >= 10, tried + ' statements tried');
  noErrors(p);
});

test('search: each group of chips is one stop for the Tab key, with arrow keys inside', async () => {
  const p = load();
  await settle();
  p.d.getElementById('find-q').focus();
  p.d.querySelectorAll('.find .filters').forEach(g => {
    const chips = [...g.querySelectorAll('.filter')];
    assert.equal(chips.filter(c => c.tabIndex >= 0).length, 1, 'one stop in ' + g.getAttribute('aria-label'));
    chips[0].focus();
    key(chips[0], 'ArrowRight');
    assert.equal(p.d.activeElement, chips[1]);
    assert.equal(chips[1].tabIndex, 0);
    key(chips[1], 'End');
    assert.equal(p.d.activeElement, chips[chips.length - 1]);
  });
  noErrors(p);
});

test('script-only controls served hidden are shown by the script', async () => {
  const p = load({ html: PAGE.replace('<div class="row-tools">', '<div class="row-tools" data-needs-script hidden>') });
  await settle();
  assert.equal(p.d.querySelector('.row-tools').hidden, false);
  noErrors(p);
});

test('performance: formula boxes are measured as they come near the screen, not all at start-up', async () => {
  const observers = [];
  const p = load({ before(w) {
    w.__reads = 0;
    const read = function () { if (!this.closest('[data-atlas-mount]')) w.__reads++; return 0; }; /* the page's own boxes only */
    Object.defineProperty(w.HTMLElement.prototype, 'scrollWidth', { configurable: true, get: read });
    w.IntersectionObserver = function (cb) { this.cb = cb; this.list = []; observers.push(this); };
    w.IntersectionObserver.prototype.observe = function (el) { this.list.push(el); };
    w.IntersectionObserver.prototype.unobserve = function () {};
    w.IntersectionObserver.prototype.disconnect = function () {};
  } });
  await settle();
  assert.equal(p.w.__reads, 0, 'no box is measured at start-up');
  const watcher = observers.find(o => o.list.some(el => el.matches('.math-display, .math-long')));
  const boxes = watcher.list.slice(0, 3);
  watcher.cb(boxes.map(target => ({ target, isIntersecting: true })));
  assert.equal(p.w.__reads, 3, 'three boxes near the screen, three measurements');
  noErrors(p);
});

/* ---------------------------------------------------------------- second review: reader tasks */

const target = (p, a) => { try { return p.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); } catch (e) { return null; } };
const statusesIn = d => [...d.querySelectorAll('.statement')].map(s => s.getAttribute('data-status'));

test('filter: rows the reader opens or closes while the filter is on stay so, and a row\'s own Show all keeps it open', async () => {
  const p = load();
  await settle();
  const rows = [...p.d.querySelectorAll('details.row')];
  const chip = [...p.d.querySelectorAll('.row-tools .filter[data-filter]')].find(c => {
    const n = rows.filter(d => statusesIn(d).includes(c.getAttribute('data-filter'))).length;
    return n > 0 && n < rows.length;
  });
  assert.ok(chip, 'a status that some rows have and others not');
  const st = chip.getAttribute('data-filter');
  const kept = rows.find(d => statusesIn(d).includes(st));
  const emptied = rows.find(d => !statusesIn(d).includes(st));
  kept.open = true;
  emptied.open = false;
  await settle();
  chip.click();
  await settle();
  assert.equal(kept.open, true);
  assert.equal(emptied.open, false);
  kept.open = false;                                  /* the reader's own choices while the filter is on */
  emptied.open = true;
  await settle();
  chip.click();
  await settle();
  assert.equal(kept.open, false, 'a row the reader closed while filtered stays closed');
  assert.equal(emptied.open, true, 'a row the reader opened while filtered stays open');
  emptied.open = false;
  await settle();
  chip.click();
  await settle();
  emptied.open = true;                                /* the reader opens a row the filter left without statements */
  await settle();
  const note = emptied.querySelector('.filter-empty');
  assert.ok(note && isShown(note), 'the row says the filter left it empty');
  note.querySelector('button').click();
  await settle();
  assert.equal(chip.getAttribute('aria-pressed'), 'false', 'the filter is off');
  assert.equal(emptied.open, true, 'the row whose statements were asked for stays open');
  assert.ok([...emptied.querySelectorAll('.statement')].every(isShown), 'its statements are shown');
  noErrors(p);
});

test('filter: each tally link lists exactly as many results as the tally counts', async () => {
  const p = load();
  await settle();
  const links = [...p.d.querySelectorAll('.tally a[data-filter]')];
  assert.ok(links.length, 'the page has a tally');
  for (const a of links) {
    const n = +visibleText(a.querySelector('.count'));
    a.click();
    await sleep(150);
    const said = visibleText(p.d.querySelector('.find-count'));
    assert.ok(new RegExp('^' + n + ' match').test(said), a.getAttribute('data-filter') + ': the tally counts ' + n + ', the list says "' + said + '"');
    p.w.history.back();
    await sleep(150);
  }
  noErrors(p);
});

test('history: a search typed just before following a link inside the atlas stays with the entry it was typed in', async () => {
  const html = PAGE.replace('<section id="results"',
    MOCK_ATLAS.replace('</section>', '<a id="atlas-self" href="#atlas-mock-h">Atlas heading</a></section>') + '<section id="results"');
  const p = load({ html });
  await settle();
  const q = p.d.getElementById('find-q');
  q.focus();
  q.value = 'zqxjv lorquim';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(130);                                   /* the search has run; its address is not yet written */
  p.d.getElementById('atlas-self').click();
  await sleep(450);
  assert.equal(p.d.getElementById('find-q').value, 'zqxjv lorquim', 'the field keeps the search');
  assert.ok(/[?&]q=zqxjv/.test(p.w.location.search), 'the new entry carries it: ' + p.w.location.href);
  p.w.history.back();
  await sleep(200);
  assert.ok(/[?&]q=zqxjv/.test(p.w.location.search), 'the entry left behind carries it: ' + p.w.location.href);
  noErrors(p);
});

test('deep link: an address the page does not have, reached during a visit, is named in view with focus on its words', async () => {
  const p = load();
  await settle();
  const section = p.d.querySelector('main section.section[id]');
  p.w.location.hash = section.id;
  await settle();
  p.w.__scrolled.length = 0;
  p.w.location.hash = 'zqxjv-lorquim';
  await settle();
  const note = p.d.querySelector('.qh-notice');
  assert.ok(note && isShown(note) && visibleText(note).includes('#zqxjv-lorquim'), 'the notice names the address');
  assert.ok(note.contains(p.d.activeElement), 'focus is on the notice');
  assert.ok(p.w.__scrolled.some(el => note.contains(el)), 'the notice is brought into view');
  noErrors(p);
});

test('history: Forward to the entry of a result puts focus on what the result led to', async () => {
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('details.row .statement[id]')].find(s => samplePhrase(s.querySelector('.statement-text') || s, 3));
  const phrase = samplePhrase(st.querySelector('.statement-text') || st, 3);
  const p = load();
  await settle();
  await type(p, '"' + phrase + '"');
  const hit = hitFor(p, p.d.getElementById(st.id));
  hit.focus();
  hit.click();
  await settle();
  assert.equal(p.d.activeElement, p.d.getElementById(st.id), 'the result leads to the statement');
  p.w.history.back();
  await sleep(150);
  assert.ok(p.d.activeElement.matches('.find-link'), 'Back returns focus to the result');
  p.w.history.forward();
  await sleep(150);
  assert.equal(p.d.activeElement, p.d.getElementById(st.id), 'Forward returns focus to the statement');
  assert.ok(isShown(p.d.getElementById(st.id)));
  noErrors(p);
});

test('table: what the keys do inside the table is said beside it and describes its region', async () => {
  const p = load();
  await settle();
  const keys = p.d.getElementById('grid-keys');
  assert.ok(keys && visibleText(keys).length > 20, 'the words are on the page');
  const host = p.d.querySelector('.grid-wrap') || p.d.querySelector('table.grid');
  assert.ok((host.getAttribute('aria-describedby') || '').split(' ').includes('grid-keys'), 'they describe the table\'s region');
  const caption = p.d.querySelector('table.grid caption');
  if (caption && caption.classList.contains('visually-hidden')) assert.ok(caption.contains(keys), 'and are read with the table\'s caption');
  noErrors(p);
});

test('table: a legend switch says what it does, and every count is a word of its own in its control\'s name', async () => {
  const p = load();
  await settle();
  const lenses = [...p.d.querySelectorAll('.legend .lens')];
  assert.ok(lenses.length, 'the legend has switches');
  lenses.forEach(b => {
    assert.ok(/\D \d+$/.test(visibleText(b)), 'status and count apart: ' + visibleText(b));
    const d = p.d.getElementById(b.getAttribute('aria-describedby'));
    assert.ok(d && visibleText(d).length > 10, 'described');
  });
  await type(p, 'the');
  const counted = [...p.d.querySelectorAll('.find .filter[data-scope]')].filter(c => visibleText(c.querySelector('.count') || c) !== '');
  assert.ok(counted.length, 'the Part chips count');
  counted.forEach(c => assert.ok(/\D \d+$/.test(visibleText(c)), 'part and count apart: ' + visibleText(c)));
  noErrors(p);
});

test('reading: an offer to continue reading is withdrawn once the reader follows a link elsewhere', async () => {
  const probe = load({ noScript: true });
  const st = probe.d.querySelectorAll('details.row .statement[id]')[3];
  const p = load({ before(w) { w.document.elementFromPoint = function () { return w.document.getElementById(st.id); }; } });
  await settle();
  p.w.dispatchEvent(new p.w.Event('scroll'));
  await sleep(800);
  const saved = p.w.localStorage.getItem('qh-place');
  const later = load({ storageSeed: { 'qh-place': saved } });
  await settle();
  assert.notEqual(visibleText(later.d.querySelector('.qh-notice')), '', 'the offer is made');
  later.d.querySelector('.nav a[href^="#"]').click();
  await settle();
  assert.equal(visibleText(later.d.querySelector('.qh-notice')), '', 'the offer is gone after a link');
  const moved = JSON.parse(saved);
  moved.title = 'zqxjv lorquim';                      /* a place whose address now names something else */
  const edition = load({ storageSeed: { 'qh-place': JSON.stringify(moved) } });
  await settle();
  assert.equal(visibleText(edition.d.querySelector('.qh-notice')), '', 'no offer for a place whose address names something else');
  [p, later, edition].forEach(noErrors);
});

test('history: Back after reaching a statement the filter hides hides it again in the entry left behind', async () => {
  const probe = load({ noScript: true });
  const chips = [...probe.d.querySelectorAll('.row-tools .filter[data-filter]')].map(c => c.getAttribute('data-filter'));
  const st = [...probe.d.querySelectorAll('.rows .statement[id]')].find(s => s.getAttribute('data-status') !== chips[0] && samplePhrase(s.querySelector('.statement-text') || s, 3));
  const phrase = samplePhrase(st.querySelector('.statement-text') || st, 3);
  const p = load({ url: '?show=' + chips[0] });
  await settle();
  const hiddenNow = () => [...p.d.querySelectorAll('.rows .statement')].filter(s => s.hidden).length;
  const before = hiddenNow();
  await type(p, '"' + phrase + '"');
  hitFor(p, p.d.getElementById(st.id)).click();
  await settle();
  assert.equal(hiddenNow(), before - 1, 'the statement reached is shown');
  p.w.history.back();
  await sleep(150);
  assert.equal(hiddenNow(), before, 'Back hides it again');
  noErrors(p);
});

test('search: a match in a status or a label is not called a match in a formula', async () => {
  const p = load();
  await settle();
  const labels = new Set([...p.d.querySelectorAll('main .statement .status-chip')].map(c => visibleText(c)).filter(Boolean));
  assert.ok(labels.size, 'the statements carry status labels');
  for (const label of labels) {
    await type(p, '"' + label + '"');
    const list = hits(p);
    assert.ok(list.length, label + ' finds the statements that carry it');
    assert.equal(list.filter(a => a.querySelector('.find-formula')).length, 0, label + ': no result says "in a formula"');
  }
  noErrors(p);
});

test('search: the scopes of a row do not come before the results that hold the words themselves', async () => {
  const p = load();
  await settle();
  const name = [...p.d.querySelectorAll('details.row .row-name')].map(plainText).find(t => /[A-Za-z]{7,}/.test(t));
  const word = name.match(/[A-Za-z]{7,}/)[0];
  await type(p, word);
  const re = new RegExp('(^|[^A-Za-z])' + word, 'i');     /* the word at the start of a word, as the search weighs it */
  const list = hits(p);
  assert.ok(list.length, word + ' finds something');
  const groups = new Map();
  list.forEach(a => { const g = a.closest('.find-group'); if (!groups.has(g)) groups.set(g, []); groups.get(g).push(a); });
  for (const links of groups.values()) {
    const borrowed = links.map(a => { const t = target(p, a); return !!t && t.matches('.cell-line') && !re.test(plainText(t)); });
    const firstBorrowed = borrowed.indexOf(true);
    if (firstBorrowed < 0) continue;
    assert.ok(borrowed.slice(firstBorrowed).every(Boolean) || links.slice(firstBorrowed).every((a, k) => borrowed[firstBorrowed + k] || !re.test(plainText(target(p, a)))),
      word + ': a scope found only by its row\'s or column\'s name comes after the results that hold the word');
  }
  noErrors(p);
});

test('search: a Greek letter\'s name finds the letter, or the name as a whole word, never words that begin with it', async () => {
  const p = load();
  await settle();
  for (const [name, letter] of [['mu', 'μ'], ['nu', 'ν'], ['chi', 'χ'], ['pi', 'π']]) {
    await type(p, name);
    hits(p).forEach(a => {
      const t = target(p, a);
      const text = (t ? t.textContent : '') + ' ' + a.textContent;
      assert.ok(text.includes(letter) || new RegExp('(^|[^A-Za-z])' + name + '([^A-Za-z]|$)', 'i').test(text), name + ': ' + visibleText(a).slice(0, 90));
    });
  }
  noErrors(p);
});

test('search: TeX typed into a word, or apart from its argument, finds what the page shows', async () => {
  const p = load();
  await settle();
  let query = null;
  let unit = null;
  for (const m of p.d.querySelectorAll('main .statement-text math')) {
    const tex = ((m.querySelector('annotation') || {}).textContent || '').trim();
    let next = m.nextSibling;
    if (!next && m.parentNode.localName === 'span') next = m.parentNode.nextSibling;
    const after = next && next.nodeType === 3 ? /^-([A-Za-z]{3,})/.exec(next.nodeValue) : null;
    if (after && /^[A-Za-z]_\{?\d\}?$/.test(tex)) { query = tex.replace(/[{}]/g, '') + '-' + after[1]; unit = m.closest('.statement'); break; }
  }
  if (query) {
    await type(p, query);
    assert.ok(hitFor(p, unit), query + ' finds the statement that shows it');
    assert.equal(visibleText(p.d.querySelector('.find-count')).includes('Nothing'), false);
  }
  const ann = [...p.d.querySelectorAll('main annotation')].map(a => /\\mathbb\{([A-Z])\}/.exec(a.textContent)).find(Boolean);
  if (ann) {
    await type(p, '\\mathbb{' + ann[1] + '}');
    const braced = countText(p);
    await type(p, '\\mathbb ' + ann[1]);
    assert.equal(countText(p), braced, '\\mathbb ' + ann[1] + ' is the same formula word as \\mathbb{' + ann[1] + '}');
  }
  assert.ok(query || ann, 'the content has a word of either kind to try');
  noErrors(p);
});

test('search: a display formula copied into a result keeps its scroll box', async () => {
  const p = load();
  await settle();
  let checked = 0;
  for (const st of [...p.d.querySelectorAll('main .statement')].filter(s => s.querySelector('math[display="block"]')).slice(0, 12)) {
    const phrase = samplePhrase(st.querySelector('.statement-text') || st, 3);
    if (!phrase) continue;
    await type(p, '"' + phrase + '"');
    const hit = hitFor(p, st) || hits(p).find(a => { const t = target(p, a); return t && t.contains(st); });
    if (!hit) continue;
    const display = new Set([...st.querySelectorAll('math[display="block"] annotation')].map(a => a.textContent));
    [...hit.querySelectorAll('.find-snippet math')].forEach(m => {
      const a = m.querySelector('annotation');
      if (a && display.has(a.textContent)) { checked++; assert.ok(m.parentNode.classList.contains('math-long'), 'a display formula sits in a scroll box'); }
    });
    if (checked >= 2) break;
  }
  assert.ok(checked > 0, 'a display formula was found in a snippet');
  noErrors(p);
});

test('table: a mark\'s name never reads as TeX, and its description is its scope', async () => {
  let html = PAGE;
  html = html.replace(/(<button type="button" class="cell-btn"[^>]*aria-label=")([^",]*)(, )/, '$1\\mathfrak{gl}_N Yangians$3');
  const p = load({ html });
  await settle();
  const btns = [...p.d.querySelectorAll('.cell-btn')];
  btns.forEach(b => assert.ok(!/\\[A-Za-z()[\]]/.test(b.getAttribute('aria-label') || ''), 'no TeX in "' + b.getAttribute('aria-label') + '"'));
  const b = btns[0];
  const ids = (b.getAttribute('aria-describedby') || '').split(' ').filter(Boolean);
  assert.equal(ids.length, 1, 'one description');
  const described = visibleText(p.d.getElementById(ids[0]));
  const note = b.closest('td').querySelector('.cell-note');
  const head = note.querySelector('.cell-note-head');
  assert.ok(described && !described.startsWith(visibleText(head)), 'the description does not repeat the status and the column: ' + described.slice(0, 80));
  const meaning = note.querySelector('.cell-note-meaning');
  assert.ok(!meaning || !described.includes(visibleText(meaning)), 'nor the meaning of the status, which is the same for every mark');
  noErrors(p);
});

test('atlas: a unit the atlas offers may give its status and place, and the tally still lists the page\'s own statements', async () => {
  const open = PAGE.match(/<a href="#examples" data-filter="([^"]+)"/);
  const st = open ? open[1] : 'open';
  const offered = MOCK_ATLAS.replace('</section>', '<div id="atlas-domain-x" data-qh-unit data-qh-unit-status="' + st + '" data-qh-unit-place="Atlas place qwvyxz">' +
    '<h3 data-qh-unit-title>Domain qwvyxz</h3><p>Offered words lorquim.</p></div></section>');
  const html = PAGE.replace('<section id="results"', offered + '<section id="results"')
    .replace('<li><a href="#results">', '<li><a href="#atlas-mock">Atlas</a></li><li><a href="#results">');
  const p = load({ html });
  await settle();
  await type(p, 'lorquim');
  const list = hits(p);
  assert.equal(list.length, 1);
  assert.ok(visibleText(list[0]).includes('Atlas place qwvyxz'), 'the place is said: ' + visibleText(list[0]));
  assert.ok(list[0].querySelector('.find-where svg, .find-where .mark'), 'the status mark is shown');
  const chip = p.d.querySelector('.find .filter[data-status-facet="' + st + '"]');
  chip.click();
  await sleep(150);
  assert.equal(hits(p).length, 1, 'the Status filter keeps it');
  const tally = p.d.querySelector('.tally a[data-filter="' + st + '"]');
  if (tally) {
    const n = +visibleText(tally.querySelector('.count'));
    tally.click();
    await sleep(150);
    assert.ok(new RegExp('^' + n + ' match').test(visibleText(p.d.querySelector('.find-count'))), 'the tally lists the page\'s statements');
  }
  noErrors(p);
});

test('search: a broad search shows its results a hundred more at a time', async () => {
  const p = load();
  await settle();
  await type(p, 'the');
  const total = +(/(\d+) match/.exec(countText(p)) || [0, 0])[1];
  if (total <= 40) return;
  assert.equal(hits(p).length, 40);
  p.d.querySelector('#find-results .find-more').click();
  await settle();
  assert.equal(hits(p).length, Math.min(140, total));
  assert.equal(p.d.activeElement, hits(p)[40], 'focus moves to the first newly shown result');
  noErrors(p);
});

test('search: one accented letter or a minus sign alone searches nothing and says so', async () => {
  const p = load();
  await settle();
  for (const q of ['é', '−']) {
    await type(p, q);
    assert.equal(hits(p).length, 0, q);
    assert.ok(/two letters/i.test(countText(p)), q + ': ' + countText(p));
  }
  noErrors(p);
});

test('interface words served with the page replace the script\'s own', async () => {
  const words = ' data-label-placeholder="Search zqxjv families" data-label-shown="Showing {shown} of {total} zqxjv, in {rows} of {all} families."';
  const html = PAGE.replace(/(<nav class="tally"[\s\S]*?<\/nav>)/, '$1<div data-find data-needs-script hidden' + words + '></div>');
  assert.notEqual(html, PAGE, 'the page has a tally to serve the mount after');
  const p = load({ html });
  await settle();
  const q = p.d.getElementById('find-q');
  assert.equal(q.placeholder, 'Search zqxjv families');
  assert.ok(q.closest('[data-find]'), 'the search is built in the served mount');
  assert.equal(q.closest('[data-find]').hidden, false, 'the served mount is shown');
  const chip = p.d.querySelector('.row-tools .filter[data-filter]');
  chip.click();
  await settle();
  assert.ok(/zqxjv, in \d+ of \d+ families/.test(visibleText(p.d.querySelector('.filter-note'))), visibleText(p.d.querySelector('.filter-note')));
  noErrors(p);
});

/* ---------------------------------------------------------------- native QA of the foundation candidate (F6, F10, F12) */

test('card: a card opens when the pointer moves onto a term, not when the page scrolls a term under a resting pointer', async () => {
  const p = load({ before(w) {
    w.matchMedia = q => ({ matches: /hover: hover|pointer: fine/.test(q), media: q, onchange: null,
      addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
  } });
  await settle();
  const term = p.d.querySelector('main .term');
  const card = p.d.getElementById('card');
  const move = (el, x, y) => el.dispatchEvent(new p.w.MouseEvent('mousemove', { bubbles: true, screenX: x, screenY: y, clientX: x, clientY: y }));
  move(p.d.body, 300, 300);                          /* the pointer rests at one place */
  term.dispatchEvent(new p.w.MouseEvent('mouseover', { bubbles: true, screenX: 300, screenY: 300 }));   /* a scroll brings a term under it */
  move(term, 300, 300);                              /* and the browser reports a move at the same place */
  await settle();
  assert.equal(card.hidden, true, 'no card opens uninvited');
  move(term, 303, 301);                              /* the reader moves the pointer onto the term */
  await settle();
  assert.equal(card.hidden, false, 'a real move opens its card');
  const mouse = (el, type, related) => el.dispatchEvent(new p.w.MouseEvent(type, { bubbles: true, relatedTarget: related }));
  mouse(term, 'mouseout', card);                     /* onto the card, then back onto its term, and rest there */
  mouse(card, 'mouseover', term);
  move(card, 320, 330);
  mouse(card, 'mouseout', term);
  mouse(term, 'mouseover', card);
  move(term, 305, 302);
  await sleep(250);
  assert.equal(card.hidden, false, 'back on its term, the card stays');
  mouse(term, 'mouseout', p.d.body);                 /* off the term and back within the moment a card waits */
  await sleep(60);
  mouse(term, 'mouseover', p.d.body);
  await sleep(250);
  assert.equal(card.hidden, false, 'a quick return keeps it');
  noErrors(p);
});

test('bar: a bar that scrolls sideways names the edges where it hides links', async () => {
  let left = 0;
  const p = load({ before(w) {
    const isNav = el => !!(el.classList && el.classList.contains('nav'));
    Object.defineProperty(w.HTMLElement.prototype, 'scrollWidth', { configurable: true, get() { return isNav(this) ? 680 : 0; } });
    Object.defineProperty(w.HTMLElement.prototype, 'clientWidth', { configurable: true, get() { return isNav(this) ? 300 : 0; } });
    Object.defineProperty(w.HTMLElement.prototype, 'scrollLeft', { configurable: true, get() { return isNav(this) ? left : 0; }, set(v) { if (isNav(this)) left = v; } });
  } });
  await settle();
  const nav = p.d.querySelector('.nav');
  assert.equal(nav.getAttribute('data-edge'), null, 'nothing is measured at start-up (the served fade fits the start)');
  nav.dispatchEvent(new p.w.Event('scroll'));
  assert.equal(nav.getAttribute('data-edge'), 'end', 'at the start, more lies at the end');
  left = 120;
  nav.dispatchEvent(new p.w.Event('scroll'));
  assert.equal(nav.getAttribute('data-edge'), 'start end', 'scrolled, more lies at both edges');
  left = 380;
  nav.dispatchEvent(new p.w.Event('scroll'));
  assert.equal(nav.getAttribute('data-edge'), 'start', 'at the end, more lies at the start only');
  noErrors(p);
});

test('card: a term served as a link opens its card while the script runs, and leads to its definition without it', async () => {
  const html = PAGE.replace(/<button type="button" class="term" data-term="([^"]+)"([^>]*)>([\s\S]*?)<\/button>/g, '<a class="term" href="#$1" data-term="$1"$2>$3</a>');
  assert.notEqual(html, PAGE, 'the page has term buttons to serve as links');
  const p = load({ html });
  await settle();
  const term = p.d.querySelector('main a.term');
  const before = p.w.location.href;
  term.focus();
  term.click();
  await settle();
  const card = p.d.getElementById('card');
  assert.equal(card.hidden, false, 'the card opens');
  assert.equal(p.w.location.href, before, 'the link does not navigate while the script runs');
  key(p.d.activeElement, 'Escape');
  await settle();
  assert.equal(card.hidden, true, 'Escape closes it');
  assert.equal(p.d.activeElement, term, 'and returns to the term');
  assert.equal(term.getAttribute('role'), 'button', 'run by the script, a term link is a button that opens a card');
  const third = [...p.d.querySelectorAll('main a.term')][2];
  key(third, ' ');                                   /* Space, without focus showing the card first */
  await settle();
  assert.equal(card.hidden, false, 'Space opens its card, as on a button');
  key(third, 'Escape');
  await settle();
  const other = [...p.d.querySelectorAll('main a.term')][1];
  const modified = new p.w.MouseEvent('click', { bubbles: true, cancelable: true, ctrlKey: true });
  other.dispatchEvent(modified);
  assert.equal(modified.defaultPrevented, false, 'a modified click opens the link as a link (a new tab)');
  const plain = load({ html, noScript: true });
  const t = plain.d.querySelector('main a.term');
  assert.ok(plain.d.getElementById(t.getAttribute('href').slice(1)), 'without the script the link leads to the definition');
  noErrors(p);
});

/* ---------------------------------------------------------------- content contract: a status of two words */

/* The page as the producer would serve it with one statement of the status "refuted form" (a checked, scoped negative
   result): its card, a Show filter chip and a tally entry, made from the page's own markup for another status. */
function withStatus(st, label) {
  const dom = new JSDOM(PAGE);
  const d = dom.window.document;
  const slug = st.replace(/\s+/g, '-');
  const card = [...d.querySelectorAll('details.row .statement[data-status]')].find(s => s.getAttribute('data-status') !== st);
  const from = card.getAttribute('data-status').replace(/\s+/g, '-');
  card.setAttribute('data-status', st);
  card.setAttribute('data-test-card', '');
  card.className = card.className.replace('st-' + from, 'st-' + slug);
  const chip = card.querySelector('.status-chip');
  chip.className = chip.className.replace('chip-' + from, 'chip-' + slug);
  const mark = chip.querySelector('.mark');
  if (mark) mark.setAttribute('class', (mark.getAttribute('class') || '').replace('mark-' + from, 'mark-' + slug));
  const words = [...chip.querySelectorAll('span')].pop();
  if (words) words.textContent = label;
  const filter = d.querySelector('.row-tools .filter[data-filter]');
  const f2 = filter.cloneNode(true);
  f2.setAttribute('data-filter', st);
  f2.setAttribute('aria-pressed', 'false');
  [...f2.childNodes].filter(n => n.nodeType === 3 || (n.nodeType === 1 && n.localName === 'span')).forEach(n => n.remove());
  f2.appendChild(d.createTextNode(label));
  filter.parentNode.appendChild(f2);
  const tally = d.querySelector('.tally a[data-filter]');
  if (tally) {
    const li = tally.closest('li').cloneNode(true);
    const a = li.querySelector('a');
    a.setAttribute('data-filter', st);
    a.querySelector('.count').textContent = '1';
    const l = a.querySelector('.count-label');
    if (l) l.textContent = label;
    tally.closest('ul').appendChild(li);
  }
  const html = dom.serialize();
  dom.window.close();
  return html;
}

test('a statement status of two words (refuted form) works in the filter, the address, the tally, the search and the legend', async () => {
  const st = 'refuted form';
  const key = new JSDOM(PAGE).window.document.querySelector('.mark.mark-refuted-form');
  const label = key && key.closest('li, .key-item') ? visibleText(key.closest('li, .key-item').querySelector('span, dt') || key.closest('li')) : 'Scoped negative';
  const html = withStatus(st, label || 'Scoped negative');
  const p = load({ html });
  await settle();
  const chip = p.d.querySelector('.row-tools .filter[data-filter="refuted form"]');
  chip.click();
  await settle();
  const shown = [...p.d.querySelectorAll('details.row .statement')].filter(isShown);
  assert.deepEqual(shown, [p.d.querySelector('[data-test-card]')], 'the filter shows the statement of that status, and only it');
  assert.ok(/[?&]show=refuted(\+|%20)form/.test(p.w.location.search), 'the address names it: ' + p.w.location.search);
  const again = load({ html, url: p.w.location.search });
  await settle();
  assert.equal(again.d.querySelector('.row-tools .filter[data-filter="refuted form"]').getAttribute('aria-pressed'), 'true', 'arrival by that address applies it');
  assert.equal(visibleText(again.d.querySelector('.qh-notice')), '', 'and does not call it unknown');
  const tally = again.d.querySelector('.tally a[data-filter="refuted form"]');
  if (tally) {
    tally.click();
    await sleep(150);
    assert.ok(/^1 match/.test(visibleText(again.d.querySelector('.find-count'))), 'the tally entry lists its statement: ' + visibleText(again.d.querySelector('.find-count')));
    assert.ok(/[?&]status=refuted(\+|%20)form/.test(again.w.location.search), again.w.location.search);
  }
  const facet = again.d.querySelector('.find .filter[data-status-facet="refuted form"]');
  assert.ok(facet, 'the search has a Status chip for it');
  const p3 = load({ html });
  await settle();
  await type(p3, '"' + (label || 'Scoped negative') + '"');
  assert.ok(hitFor(p3, p3.d.querySelector('[data-test-card]')), 'its label finds it');
  const lens = p3.d.querySelector('.legend .lens[data-lens="refuted form"]');
  if (lens) {
    lens.click();
    assert.equal(p3.d.querySelectorAll('.grid td[data-lit]').length, p3.d.querySelectorAll('.grid td.cell[data-status="refuted form"]').length, 'the legend switch lights the cells of that status');
  }
  [p, again, p3].forEach(noErrors);
});

test('search: a field too narrow for the placeholder gets the short one, and a wide field keeps the full one', async () => {
  let width = 180;
  const p = load({ before(w) {
    Object.defineProperty(w.HTMLInputElement.prototype, 'clientWidth', { configurable: true, get() { return this.id === 'find-q' ? width : 0; } });
  } });
  await settle();
  p.w.dispatchEvent(new p.w.Event('load'));
  const q = p.d.getElementById('find-q');
  assert.ok(q.placeholder.length < 30, 'narrow: "' + q.placeholder + '"');
  width = 900;
  p.w.dispatchEvent(new p.w.Event('resize'));
  await sleep(250);
  assert.ok(q.placeholder.length >= 30, 'wide: "' + q.placeholder + '"');
  noErrors(p);
});

/* ---------------------------------------------------------------- third review: search */

test('search: text in a part of another shape is searchable, and its Part chip counts it', async () => {
  const part = '<section id="zsynth" class="section"><header class="section-head"><h2 id="zsynth-h">Synthesis zqxjv</h2></header>' +
    '<p>The programme synthesis lorquim ties the parts together.</p><h3>Reading path qwvyxz</h3>' +
    '<ol><li>First read the lorquim results here.</li><li>Then the comparisons follow from them.</li></ol>' +
    '<div class="relation">The relation zorbat joins two of the parts.</div>' +
    '<table><tr><td>Path plinkor first</td><td>then the rest in order</td></tr></table>' +
    '<dl><dt>Term quindle stated</dt><dd>Its meaning given in words.</dd></dl></section>';
  const html = PAGE.replace('<section id="results"', part + '<section id="results"')
    .replace('<li><a href="#results">', '<li><a href="#zsynth">Synthesis</a></li><li><a href="#results">');
  assert.notEqual(html, PAGE, 'the page has the shape the part is added to');
  const p = load({ html });
  await settle();
  await type(p, 'lorquim');
  const list = hits(p);
  assert.ok(list.length >= 2, 'its words are found: ' + list.length + ' results');
  list.forEach(a => assert.ok(target(p, a) && target(p, a).closest('#zsynth'), 'each result is in the new part'));
  const chip = p.d.querySelector('.find .filter[data-scope="zsynth"]');
  assert.ok(chip && /[1-9]\d*$/.test(visibleText(chip)), 'its Part chip counts its matches: ' + (chip && visibleText(chip)));
  await type(p, 'qwvyxz');
  assert.ok(hits(p).length >= 1, 'the heading that titles its blocks is found');
  for (const w of ['zorbat', 'plinkor', 'quindle']) {           /* text in a div, a table's row and a term of a list */
    await type(p, w);
    assert.ok(hits(p).some(a => { const x = target(p, a); return x && x.closest('#zsynth'); }), w + ' is found in the new part');
  }
  await type(p, 'lorquim');
  const address = hits(p)[0].getAttribute('href');
  const fresh = load({ html, url: address });        /* the address a result gives, on a fresh visit */
  await settle();
  assert.equal(visibleText(fresh.d.querySelector('.qh-notice')), '', 'the page does not call its own address unknown: ' + address);
  const el = fresh.d.getElementById(decodeURIComponent(address.slice(1)));
  assert.ok(el && el.hasAttribute('data-revealed'), 'the block it names is reached');
  [p, fresh].forEach(noErrors);
});

test('search: TeX typed into a word of a title finds that title', async () => {
  const p = load();
  await settle();
  const src = el => { let o = ''; (function w(n) { if (n.nodeType === 3) { o += n.nodeValue; return; } if (n.nodeType !== 1) return;
    if (n.localName === 'math') { const a = n.querySelector('annotation'); o += a ? a.textContent : ''; return; } for (let c = n.firstChild; c; c = c.nextSibling) w(c); })(el); return o; };
  let query = null, unit = null;
  const plainForm = x => x.replace(/\\[A-Za-z]+/g, '').replace(/[_^{}$]/g, '').toLowerCase();
  for (const t of p.d.querySelectorAll('main .statement-title')) {
    const words = src(t).replace(/\s+/g, ' ').trim().split(' ');
    const k = words.findIndex(x => /[A-Za-z]_\{?\d+\}?-?[A-Za-z]{3,}/.test(x));
    if (k <= 0 || !/^[A-Za-z]{3,}$/.test(words[k - 1])) continue;
    const word = words[k].replace(/[{}]/g, '').replace(/[.,;:]+$/, '');
    const st = t.closest('.statement');
    const text = st.querySelector('.statement-text');
    /* a title whose word the statement's text does not repeat: only the title can be found by it */
    if (text && plainText(text).toLowerCase().replace(/\s+/g, '').includes(plainForm(word).replace(/\s+/g, ''))) continue;
    query = words[k - 1] + ' ' + word; unit = st; break;
  }
  if (!query) return;                                 /* this content has no such title */
  await type(p, query);
  /* the statement's own result; a question's own (asked) statement is found as its question */
  const asked = !!unit.closest('.question') && /(^|\s)(question|question-ask)(\s|$)/.test(unit.parentElement.className);
  const hit = hits(p).find(a => target(p, a) === (asked ? unit.closest('.question') : unit));  /* not a row that holds it */
  assert.ok(hit, '"' + query + '" finds the statement whose title shows it');
  noErrors(p);
});

test('search: within a part, results that hold the words in their own text come before those found only through their place', async () => {
  const p = load();
  await settle();
  /* A result's own words, as the search reads them: blocks apart, formulae and the result's place (a column's name and
     status in a row, the context line of a statement) left out. */
  const BLOCKS = /^(p|div|li|dt|dd|h[1-6]|article|ul|ol|dl|summary|section|header)$/;
  const ownWords = el => {
    const c = el.cloneNode(true);
    c.querySelectorAll('.cell-col, .cell-st, .statement-context, math, svg, annotation').forEach(n => n.remove());
    let out = '';
    (function walk(n) {
      if (n.nodeType === 3) { out += n.nodeValue; return; }
      if (n.nodeType !== 1) return;
      for (let k = n.firstChild; k; k = k.nextSibling) walk(k);
      if (BLOCKS.test(n.localName)) out += ' ';
    })(c);
    return out.toLowerCase();
  };
  const own = (el, w) => new RegExp('(^|[^a-z])' + w.toLowerCase()).test(ownWords(el));
  const ownText = el => el;
  const phrases = [];
  [...p.d.querySelectorAll('details.row .row-name')].map(plainText).forEach(n => {
    const w = n.split(/[\s,]+/).filter(x => /^[A-Za-z]{5,}$/.test(x));
    for (let i = 0; i + 1 < w.length && phrases.length < 6; i++) phrases.push(w[i] + ' ' + w[i + 1]);
  });
  for (const phrase of phrases) {
    await type(p, phrase);
    const words = phrase.split(' ');
    const groups = new Map();
    hits(p).forEach(a => { const g = a.closest('.find-group'); if (!groups.has(g)) groups.set(g, []); groups.get(g).push(a); });
    for (const links of groups.values()) {
      const holds = links.map(a => { const x = target(p, a); return !!x && words.every(w => own(ownText(x), w)); });
      const firstOut = holds.indexOf(false);
      if (firstOut >= 0) assert.ok(holds.slice(firstOut).every(h => !h), '"' + phrase + '": a result found only through its place comes before one that holds the words');
    }
  }
  noErrors(p);
});

test('search: a defined term typed in any quotes puts its definition first', async () => {
  const p = load();
  await settle();
  const terms = [...p.d.querySelectorAll('main .gloss')].map(g => ({ g, dt: plainText(g.querySelector('dt')) })).filter(x => x.dt && !/[«»„“”"]/.test(x.dt));
  assert.ok(terms.length, 'the page has a glossary');
  const q = p.d.getElementById('find-q');
  q.focus();
  for (const { g, dt } of terms) {
    q.value = '«' + dt + '»';                         /* Enter runs the search at once */
    q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
    key(q, 'Enter');
    q.focus();
    const first = hits(p)[0];
    const x = first && target(p, first);
    assert.ok(x && (x === g || x.contains(g) || g.contains(x)), '«' + dt + '» puts its definition first');
  }
  noErrors(p);
});

test('search: a formula in a row\'s name is the row\'s, not a match of each of its column scopes', async () => {
  const m = /(<span class="row-name">(?:(?!<\/span>)[\s\S])*?<annotation encoding="application\/x-tex">)([^<]+)(<\/annotation>)/.exec(PAGE);
  if (!m) return;                                     /* no row name with a formula in this content */
  const html = PAGE.replace(m[0], m[1] + '\\mathfrak{zq}' + m[3]);
  const p = load({ html });
  await settle();
  await type(p, '\\mathfrak{zq}');
  const own = hits(p).filter(a => { const x = target(p, a); return x && x.matches('.cell-line'); });
  assert.equal(own.length, 0, 'no column scope is found by its row name\'s formula');
  noErrors(p);
});

test('search: the field is described by the keyboard hint only where there is a keyboard and a fine pointer', async () => {
  const touch = load();
  await settle();
  assert.equal(touch.d.getElementById('find-q').hasAttribute('aria-describedby'), false, 'not on a touch screen');
  const desk = load({ before(w) {
    w.matchMedia = q => ({ matches: /hover: hover|pointer: fine/.test(q), media: q, onchange: null,
      addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
  } });
  await settle();
  assert.equal(desk.d.getElementById('find-q').getAttribute('aria-describedby'), 'find-hint', 'with a fine pointer');
  [touch, desk].forEach(noErrors);
});

/* ---------------------------------------------------------------- run */

(async () => {
  let failed = 0;
  let ran = 0;
  for (const t of tests) {
    if (only && !t.name.includes(only)) continue;
    ran++;
    const t0 = Date.now();
    try {
      await t.fn();
      console.log('ok    ' + t.name + '  (' + (Date.now() - t0) + ' ms)');
    } catch (e) {
      failed++;
      console.log('FAIL  ' + t.name + '\n      ' + String(e && e.message || e).split('\n').slice(0, 6).join('\n      '));
    }
    opened.splice(0).forEach(dom => dom.window.close());
    if (typeof global.gc === 'function') global.gc();  /* a large page needs its memory back between tests */
  }
  console.log(ran + ' tests, ' + (failed ? failed + ' failed' : 'all passed'));
  process.exit(failed ? 1 : 0);
})();
