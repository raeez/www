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
  q.focus();
  q.value = text;
  q.dispatchEvent(new page.w.Event('input', { bubbles: true }));
  await sleep(150);
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
  const probe = load({ noScript: true });
  const st = [...probe.d.querySelectorAll('details.row .statement:not([id])')].find(s => s.querySelector('.statement-title'));
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
  const p = load({ url: '#term-poisson-bracket' });
  await settle();
  const note = p.d.querySelector('.qh-notice');
  assert.ok(note && isShown(note), 'a notice is shown');
  assert.ok(visibleText(note).includes('#term-poisson-bracket'), 'it names the address');
  const go = [...note.querySelectorAll('button')].find(b => /poisson bracket/i.test(visibleText(b)));
  assert.ok(go, 'it offers a search for the address\'s words');
  go.click();
  await sleep(150);
  assert.equal(p.d.getElementById('find-q').value, 'poisson bracket');
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
  const details = [...p.d.querySelectorAll('main details')];
  const before = details.map(x => x.open);
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  p.w.dispatchEvent(new p.w.Event('beforeprint'));
  p.w.dispatchEvent(new p.w.Event('afterprint'));
  assert.deepEqual(details.map(x => x.open), before);
  noErrors(p);
});

/* ---------------------------------------------------------------- atlas isolation */

const MOCK_ATLAS = '<section id="atlas" class="section wide atlas" data-atlas-mount aria-labelledby="atlas-h">' +
  '<header class="section-head"><h2 id="atlas-h">Atlas</h2></header>' +
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
  const chip = p.d.querySelector('#atlas .filter');
  chip.click();
  await settle();
  assert.equal(p.d.querySelectorAll('.rows .statement[hidden]').length, 0, 'an atlas chip does not filter the rows');
  assert.equal(p.w.location.search.includes('show='), false);
  const rowsBefore = p.d.querySelectorAll('details.row[open]').length;
  p.d.querySelector('#atlas [data-expand]').click();
  assert.equal(p.d.querySelectorAll('details.row[open]').length, rowsBefore, 'an atlas Open all does not open the rows');
  assert.ok(p.d.getElementById('atlas').querySelector('.statement').id === '', 'no anchor is added inside the atlas');
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
  await sleep(120);
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
                   ...p.d.querySelectorAll('main section.section > .section-intro')].filter(Boolean);
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

test('table: each mark is described by its scope, and no name is read as TeX', async () => {
  const p = load();
  await settle();
  p.d.querySelectorAll('.grid .cell-btn').forEach(b => {
    const d = p.d.getElementById(b.getAttribute('aria-describedby'));
    assert.ok(d && b.closest('td').contains(d), 'scope of ' + b.getAttribute('aria-label'));
    assert.ok(!/\\[()[\]]/.test(b.getAttribute('aria-label')), b.getAttribute('aria-label'));
  });
  p.d.querySelectorAll('main .term[data-term]').forEach(t => {
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
  const row = [...probe.d.querySelectorAll('details.row')].find(d => d.querySelectorAll('.statement:not([id]) .statement-title').length >= 2);
  const titles = [...row.querySelectorAll('.statement:not([id]) .statement-title')].map(t => plainText(t));
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
    '<td><button type="button" id="atlas-n2">n2</button></td></tr></table><a class="term" id="atlas-term" href="#atlas-h">t</a>' +
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
  const p = load({ html: withAtlas(), url: '#atlas-node-17', before(w) {
    w.document.addEventListener('qh:unknown-anchor', e => { if (/^atlas-/.test(e.detail.id)) e.preventDefault(); });
  } });
  await settle();
  assert.equal(visibleText(p.d.querySelector('.qh-notice')), '');
  noErrors(p);
});

test('atlas: text the atlas offers is searchable, and a result asks the atlas to show it', async () => {
  const offered = MOCK_ATLAS.replace('</section>', '<div id="atlas-domain-x" data-qh-unit><h3 data-qh-unit-title>Domain qwvyxz</h3>' +
    '<p>Offered words lorquim.</p></div></section>');
  const html = PAGE.replace('<section id="results"', offered + '<section id="results"')
    .replace('<li><a href="#results">', '<li><a href="#atlas">Atlas</a></li><li><a href="#results">');
  const p = load({ html });
  await settle();
  let asked = null;
  p.d.getElementById('atlas').addEventListener('qh:reveal', e => { asked = e.detail.id; e.preventDefault(); });
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
    const read = function () { w.__reads++; return 0; };
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
  }
  console.log(ran + ' tests, ' + (failed ? failed + ' failed' : 'all passed'));
  process.exit(failed ? 1 : 0);
})();
