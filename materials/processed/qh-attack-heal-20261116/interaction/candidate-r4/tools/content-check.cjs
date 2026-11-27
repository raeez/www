#!/usr/bin/env node
/* Checks of a built status page with its script running that hold for any content payload (jsdom only: no browser, no
   layout, no timing that means anything outside jsdom):

     NODE_PATH=<node_modules with jsdom> node content-check.cjs <page.html> [--must <ids-file>]... [--report <ids-file>]...
                                [--every <k>] [--expect-atlas] [--ranks <out.tsv>]

   C1 the page starts and settles without a script error.
   C2 the script leaves the served content as it is: outside atlas mounts, every statement's status, title and text, every
      cell's status and words, and the tally read the same before the script runs and after.
   C3 no id occurs twice once the script has run; every id of each --must file exists (addresses published before); each
      --report file is only counted. Statements addressed by the words of their title (the content gives them no id) are
      counted: such an address changes whenever the title's words do.
   C4 every in-page link outside an atlas mount reaches an element; links inside a mount are counted for the atlas.
   C5 search coverage: each statement, each column's scope in each row and each unit an atlas offers is found by a few of
      its own consecutive words, typed as a reader types them; the rank of its result is recorded (1 is first). A question's
      own statement and a counterexample's witness are found when the result is their question or their false claim (the
      search's unit there is the whole question, or the claim with its witness). With --every k only every k-th unit is tried.
   C6 atlas mounts: their size, whether anything is rendered in them, the units they offer; --expect-atlas fails when there
      is no mount or a mount is empty.
   C7 text coverage, whatever its shape: in every part of the page (outside atlas mounts and the interface's own controls),
      the text is gathered into its nearest blocks (any block element, divs, dt, td and th included; a table's row for a
      table), and up to --blocks n (default 12) of them are each found by a few of their own words, as the block itself,
      inside the unit that holds it, or as a unit inside it.
   Prints one line per check and the details of each failure; exits 1 when a check fails, 2 on a usage error. */
'use strict';
const fs = require('fs');

let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require('jsdom')); } catch (e) {
  console.error('jsdom is not installed where Node can find it; set NODE_PATH to a node_modules folder that has it.');
  process.exit(2);
}
const argv = process.argv.slice(2);
const opt = { must: [], report: [], every: 1, expectAtlas: false, ranks: null, file: null, blocks: 12 };
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--must') opt.must.push(argv[++i]);
  else if (a === '--report') opt.report.push(argv[++i]);
  else if (a === '--every') opt.every = Math.max(1, parseInt(argv[++i], 10) || 1);
  else if (a === '--expect-atlas') opt.expectAtlas = true;
  else if (a === '--ranks') opt.ranks = argv[++i];
  else if (a === '--blocks') opt.blocks = Math.max(0, parseInt(argv[++i], 10) || 0);
  else if (!opt.file) opt.file = a;
  else { console.error('unexpected argument ' + a); process.exit(2); }
}
if (!opt.file) { console.error('usage: content-check.cjs <page.html> [--must f]... [--report f]... [--every k] [--expect-atlas] [--ranks out.tsv]'); process.exit(2); }
const HTML = fs.readFileSync(opt.file, 'utf8');
const BASE = 'https://raeez.com/quantum-holography-tracker.html';
const MOUNT = '[data-atlas-mount]';

const results = [];
function check(name, ok, detail, extra) {
  results.push(ok);
  console.log((ok ? 'PASS ' : 'FAIL ') + name + (detail ? ': ' + detail : ''));
  if (!ok && extra && extra.length) extra.slice(0, 12).forEach(x => console.log('     ' + x));
}
function info(name, detail) { console.log('INFO ' + name + (detail ? ': ' + detail : '')); }
const sleep = ms => new Promise(r => setTimeout(r, ms));
const norm = s => (s || '').replace(/\s+/g, ' ').trim();
function textOf(el) { /* words and formulae as served: a formula by its TeX annotation, never by its rendered glyphs */
  if (!el) return '';
  let out = '';
  (function walk(n) {
    if (n.nodeType === 3) { out += n.nodeValue; return; }
    if (n.nodeType !== 1) return;
    if (n.localName === 'math') { const a = n.querySelector('annotation'); out += ' ' + (a ? a.textContent : '') + ' '; return; }
    if (n.localName === 'svg' || n.localName === 'script' || n.localName === 'style') return;
    for (let c = n.firstChild; c; c = c.nextSibling) walk(c);
  })(el);
  return norm(out);
}
const outside = el => !el.closest(MOUNT);

function served(d) {
  const statements = [...d.querySelectorAll('.statement')].filter(outside).map(e => ({
    status: e.getAttribute('data-status') || '', title: textOf(e.querySelector('.statement-title')), text: textOf(e.querySelector('.statement-text')) }));
  const cells = [...d.querySelectorAll('td.cell')].filter(outside).map(e => (e.getAttribute('data-status') || '') + ' | ' + textOf(e));
  const tally = [...d.querySelectorAll('a[data-filter]')].filter(outside).filter(a => a.querySelector('.count'))
    .map(a => a.getAttribute('data-filter') + '=' + norm(a.querySelector('.count').textContent));
  return { statements, cells, tally };
}
function diff(a, b, show) {
  const out = [];
  if (a.length !== b.length) out.push(`count ${a.length} before, ${b.length} after`);
  for (let i = 0; i < Math.min(a.length, b.length) && out.length < 6; i++) if (show(a[i]) !== show(b[i])) out.push(`#${i + 1}: ${show(a[i]).slice(0, 110)}  ->  ${show(b[i]).slice(0, 110)}`);
  return out;
}
/* The rule by which the page's script makes an address from words (status.js, ident). */
function ident(text) {
  const t = text.normalize('NFKD').replace(/[^\x00-\x7f]/g, '').replace(/[^A-Za-z0-9_\s-]/g, '').trim().toLowerCase();
  return t.replace(/[\s_-]+/g, '-').slice(0, 60) || 'x';
}
function sourceText(el) {
  let out = '';
  (function walk(n) {
    if (n.nodeType === 3) { out += n.nodeValue; return; }
    if (n.nodeType !== 1) return;
    if (n.localName === 'math') { const a = n.querySelector('annotation'); out += a ? a.textContent : ''; return; }
    for (let c = n.firstChild; c; c = c.nextSibling) walk(c);
  })(el);
  return out;
}
/* A few consecutive plain words from the longest stretch of plain text in el (no formula, chip or label in the phrase). */
function phraseOf(el, n) {
  const w = el.ownerDocument.createTreeWalker(el, 4);
  const texts = [];
  for (let t = w.nextNode(); t; t = w.nextNode()) {
    if (t.parentElement.closest('math, svg, .status-chip, .note-label, .added-chip, .cell-col, .cell-st, .visually-hidden, button')) continue;
    texts.push(t.nodeValue);
  }
  texts.sort((a, b) => b.length - a.length);
  for (const text of texts) {
    const words = text.split(/\s+/).filter(Boolean);
    for (let i = words.length > n ? 1 : 0; i + n <= words.length; i++) {
      const run = words.slice(i, i + n);
      if (run.every(x => /^[A-Za-z][A-Za-z-]{2,}$/.test(x))) return run.join(' ');
    }
  }
  return null;
}

(async function main() {
  /* the page as served, without its scripts */
  const before = served(new JSDOM(HTML).window.document);

  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented: navigation/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
  vc.on('error', (...a) => errors.push('console.error: ' + a.join(' ')));
  const dom = new JSDOM(HTML, { url: BASE, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
  const w = dom.window, d = w.document;
  await sleep(400);

  /* C1 */
  check('C1 no script error while the page starts', errors.length === 0, errors.length + ' error(s)', errors);

  /* C2 */
  const after = served(d);
  const sd = diff(before.statements, after.statements, s => `${s.status} | ${s.title} | ${s.text}`);
  check('C2 statements as served', sd.length === 0, `${after.statements.length} statements outside atlas mounts`, sd);
  const cd = diff(before.cells, after.cells, x => x);
  check('C2 cells as served', cd.length === 0, `${after.cells.length} cells`, cd);
  const td = diff(before.tally, after.tally, x => x);
  check('C2 tally as served', td.length === 0, after.tally.join(', '), td);

  /* C3 */
  const count = new Map();
  d.querySelectorAll('[id]').forEach(e => count.set(e.id, (count.get(e.id) || 0) + 1));
  const dup = [...count].filter(([, n]) => n > 1).map(([id, n]) => `${id} x${n}`);
  check('C3 no id occurs twice', dup.length === 0, `${count.size} ids`, dup);
  const readIds = f => fs.readFileSync(f, 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
  for (const f of opt.must) {
    const want = readIds(f), lost = want.filter(id => !count.has(id));
    check('C3 addresses kept from ' + f.split('/').pop(), lost.length === 0, `${want.length} ids, ${lost.length} missing`, lost);
  }
  for (const f of opt.report) {
    const want = readIds(f), kept = want.filter(id => count.has(id)).length;
    info('C3 addresses of ' + f.split('/').pop(), `${kept} of ${want.length} exist; the others are named on arrival with a search for their words`);
  }
  const statements = [...d.querySelectorAll('.statement')].filter(outside);
  const staticIds = new Set([...new JSDOM(HTML).window.document.querySelectorAll('.statement[id]')].map(e => e.id));
  let worded = 0, servedWorded = 0, scriptMade = 0;
  const wordedExamples = [];
  statements.forEach(st => {
    if (!st.id) return;
    const from = st.querySelector('.statement-title') || st.querySelector('.statement-text') || st;
    const base = 's-' + ident(sourceText(from).slice(0, 400));
    if (st.id === base || (st.id.startsWith(base + '-') && /^\d+$/.test(st.id.slice(base.length + 1)))) {
      worded++;
      if (staticIds.has(st.id)) servedWorded++;
      if (wordedExamples.length < 3) wordedExamples.push(st.id);
    }
    if (!staticIds.has(st.id)) scriptMade++;
  });
  const noId = statements.filter(st => !st.id).length;
  check('C3 every statement has an address', noId === 0, `${statements.length} statements, ${noId} without an address`);
  info('C3 addresses equal to the words of their title', `${worded} of ${statements.length} statements (${servedWorded} served, ` +
       `${scriptMade} made by the script). Made from the words, they change when a title does; given as content ids (to keep an ` +
       `earlier address) they stay. integration-check I4b counts the statements without a content id. Examples: ${wordedExamples.join(', ') || 'none'}`);

  /* C4 */
  const links = [...d.querySelectorAll('a[href^="#"]')].filter(a => a.getAttribute('href').length > 1);
  const broken = [], brokenInMount = [];
  links.forEach(a => {
    let id = null;
    try { id = decodeURIComponent(a.getAttribute('href').slice(1)); } catch (e) { id = null; }
    if (id !== null && d.getElementById(id)) return;
    (outside(a) ? broken : brokenInMount).push(a.getAttribute('href') + '  (' + norm(a.textContent).slice(0, 50) + ')');
  });
  check('C4 in-page links reach an element', broken.length === 0, `${links.length} links, ${broken.length} broken outside atlas mounts`, broken);
  if (d.querySelector(MOUNT)) {
    /* A link inside a mount to an id of the atlas's own kind is the atlas's (it may claim it); one to a page id that is
       missing reaches the reader as an unknown address. Atlas ids are recognised by the prefixes the mounts' own ids use. */
    const prefixes = new Set([...d.querySelectorAll(MOUNT + ' [id]')].map(e => e.id.split('-').slice(0, 2).join('-')));
    const toPage = brokenInMount.filter(x => !prefixes.has(x.slice(1).split('-').slice(0, 2).join('-')));
    info('C4 links inside atlas mounts to atlas ids that reach nothing', String(brokenInMount.length - toPage.length));
    check('C4 links from atlas mounts to page addresses reach an element', toPage.length === 0, `${toPage.length} broken`, toPage);
  }

  /* C6 (before the search changes the page) */
  const mounts = [...d.querySelectorAll(MOUNT)];
  const mountRows = mounts.map(m => ({ id: m.id || '(no id)', elements: m.getElementsByTagName('*').length, words: norm(m.textContent).split(' ').filter(Boolean).length,
    units: m.querySelectorAll('[data-qh-unit]').length, unitsWithoutId: [...m.querySelectorAll('[data-qh-unit]')].filter(u => !u.id).length }));
  mountRows.forEach(r => info('C6 atlas mount #' + r.id, `${r.elements} elements, ${r.words} words, ${r.units} search units (${r.unitsWithoutId} without an id)`));
  if (!mounts.length) info('C6 atlas mounts', 'none in this page');
  if (opt.expectAtlas) {
    const empty = mountRows.filter(r => r.words < 20);
    check('C6 the atlas is rendered', mounts.length > 0 && empty.length === 0, mounts.length ? `${mounts.length} mount(s), ${empty.length} empty` : 'no atlas mount in the page');
  }
  const unitsNoId = mountRows.reduce((s, r) => s + r.unitsWithoutId, 0);
  if (mounts.length) check('C6 every unit an atlas offers has an address', unitsNoId === 0, `${unitsNoId} without an id`);

  /* C5 */
  const q = d.getElementById('find-q');
  if (!q) { check('C5 search coverage', false, 'the search was not built'); }
  else {
    const units = [];
    statements.forEach(el => units.push({ kind: 'statement', el }));
    [...d.querySelectorAll('.cell-lines > .cell-line')].filter(outside).forEach(el => units.push({ kind: 'scope', el }));
    mounts.forEach(m => m.querySelectorAll('[data-qh-unit]').forEach(el => units.push({ kind: 'atlas', el })));
    q.focus();
    const rows = [];
    const t0 = Date.now();
    for (let i = 0; i < units.length; i += opt.every) {
      const u = units[i];
      const phrase = phraseOf(u.el, 4) || phraseOf(u.el, 3) || phraseOf(u.el, 2);
      if (!phrase) { rows.push({ kind: u.kind, id: u.el.id, phrase: '', rank: -1, shown: 0, via: '' }); continue; }
      q.value = phrase;
      q.dispatchEvent(new w.Event('input', { bubbles: true }));
      q.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Enter', bubbles: true, cancelable: true }));
      const rankIn = () => {
        const list = [...d.querySelectorAll('#find-results .find-link')];
        const at = list.findIndex(a => {
          let t = null;
          try { t = d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); } catch (e) { t = null; }
          return t && (t === u.el || (!u.el.id && t.contains(u.el)) || (t.matches('.question, .failure') && u.el.closest('.question, .failure') === t));
        });
        const hit = at >= 0 ? list[at] : null;
        return { rank: at + 1, shown: list.length, via: hit && hit.getAttribute('href') !== '#' + u.el.id ? hit.getAttribute('href') : '' };
      };
      let r = rankIn();
      for (let more = d.querySelector('#find-results .find-more'); !r.rank && more; more = d.querySelector('#find-results .find-more')) {
        more.click();                                      /* the next results, as a reader asks for them */
        r = rankIn();
      }
      rows.push({ kind: u.kind, id: u.el.id, phrase, rank: r.rank, shown: r.shown, via: r.via || '' });
      q.focus();
    }
    const ms = Date.now() - t0;
    q.value = '';
    q.dispatchEvent(new w.Event('input', { bubbles: true }));
    const kinds = ['statement', 'scope', 'atlas'];
    const bucket = (k, f) => rows.filter(x => x.kind === k && f(x)).length;
    kinds.forEach(k => {
      const n = rows.filter(x => x.kind === k).length;
      if (!n) return;
      info('C5 ' + k + ' units', `${n} tried: first ${bucket(k, x => x.rank === 1)}, 2-5 ${bucket(k, x => x.rank >= 2 && x.rank <= 5)}, ` +
        `6-40 ${bucket(k, x => x.rank >= 6 && x.rank <= 40)}, after 40 ${bucket(k, x => x.rank > 40)}, not found ${bucket(k, x => x.rank === 0)}, ` +
        `no plain phrase to try ${bucket(k, x => x.rank === -1)}; found through their question or false claim ${bucket(k, x => x.rank > 0 && x.via)}`);
    });
    const missed = rows.filter(x => x.rank === 0);
    check('C5 search finds every unit by its own words', missed.length === 0, `${rows.length} units tried in ${ms} ms (jsdom), ${missed.length} not found`,
      missed.map(x => `${x.kind} #${x.id || '(no id)'}: "${x.phrase}"`));
    if (opt.ranks) fs.writeFileSync(opt.ranks, 'kind\tid\trank\tshown\tvia\tphrase\n' + rows.map(x => [x.kind, x.id, x.rank, x.shown, x.via, x.phrase].join('\t')).join('\n') + '\n');
  }

  /* C7 */
  if (q && opt.blocks) {
    const CHROME = '.find, .qh-notice, #card, nav, .row-tools, .grid-block, .tally, .section-head, .kicker, .essay-byline, ' +
                   '.visually-hidden, [hidden], [aria-hidden="true"], button, annotation, svg, math, script, style, ' + MOUNT;
    const BLOCKS = 'p, li, dd, dt, h3, h4, h5, h6, blockquote, figcaption, pre, summary, td, th, caption, div, article, aside, header, footer';
    const parts = [...d.querySelectorAll('main > section[id], main > header[id]')].filter(outside);
    const missed = [];
    let tried = 0;
    parts.forEach(part => {
      const seen = new Set();
      const walker = d.createTreeWalker(part, 4);
      for (let t = walker.nextNode(); t; t = walker.nextNode()) {
        const el = t.parentElement;
        if (!el || !/[A-Za-z]{3}/.test(t.nodeValue) || el.closest(CHROME)) continue;
        const row = el.closest('tr');
        const b = row && part.contains(row) ? row : el.closest(BLOCKS);
        if (b && b !== part && part.contains(b)) seen.add(b);
      }
      const blocks = [...seen].filter(b => phraseOf(b, 4) || phraseOf(b, 3));
      const step = Math.max(1, Math.ceil(blocks.length / opt.blocks));
      for (let i = 0; i < blocks.length; i += step) {
        const b = blocks[i];
        const phrase = phraseOf(b, 4) || phraseOf(b, 3);
        tried++;
        q.value = phrase;
        q.dispatchEvent(new w.Event('input', { bubbles: true }));
        q.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Enter', bubbles: true, cancelable: true }));
        const found = () => [...d.querySelectorAll('#find-results .find-link')].some(a => {
          let t = null;
          try { t = d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); } catch (e) { t = null; }
          /* the block itself, the unit that holds it, a unit inside it, or (for a disclosure's summary) what it discloses */
          return t && (t === b || t.contains(b) || b.contains(t) || (b.localName === 'summary' && b.parentElement.contains(t)));
        });
        let ok = found();
        for (let more = d.querySelector('#find-results .find-more'); !ok && more; more = d.querySelector('#find-results .find-more')) { more.click(); ok = found(); }
        if (!ok) missed.push(`#${part.id}: "${phrase}" (${b.localName}${b.className ? '.' + b.className.split(' ')[0] : ''})`);
        q.focus();
      }
    });
    q.value = '';
    q.dispatchEvent(new w.Event('input', { bubbles: true }));
    check('C7 the text of every part is found by its own words', missed.length === 0, `${tried} blocks tried in ${parts.length} parts, ${missed.length} not found`, missed);
  }

  check('C1 no script error after the checks', errors.length === 0, errors.length + ' error(s)', errors);
  console.log('summary:', results.every(Boolean) ? 'PASS' : results.filter(x => !x).length + ' failure(s)');
  w.close();
  process.exit(results.every(Boolean) ? 0 : 1);
})().catch(e => { console.error(e && e.stack || e); process.exit(2); });
