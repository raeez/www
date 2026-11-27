#!/usr/bin/env node
/* Reading-flow tests for the monograph reader (reader.js):

       NODE_PATH=<a node_modules folder with jsdom> node compiler/quantum-holography-status/tests/reader.test.cjs [name filter]

   Each test builds a book in the served shape (the reader's DOM contract) from the structure of the reader manifest
   (fixtures/reader-book.json: parts, chapters, prerequisites, routes; no chapter text), loads it in jsdom with the
   script running, dispatches real events (clicks, keys, typing, history traversal, find-in-page) and checks what the
   reader is shown. The chapter text in these books is neutral filler. jsdom has no layout: scrolling is recorded by
   stubs of scrollIntoView and scrollTo, and nothing here measures geometry. */
'use strict';
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');

let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require('jsdom')); } catch (e) {
  console.error('jsdom is not installed where Node can find it; set NODE_PATH to a node_modules folder that has it.');
  process.exit(2);
}
const pageAt = process.argv.indexOf('--page');
const PAGE_FILE = pageAt > 0 ? process.argv[pageAt + 1] : null;
const only = PAGE_FILE ? '' : process.argv[2] || '';
/* READER_JS and STATUS_JS may name other copies of the two scripts (to check that a test fails without its behaviour). */
const SCRIPT = fs.readFileSync(process.env.READER_JS || path.join(__dirname, '..', 'reader.js'), 'utf8');
const STATUS = fs.readFileSync(process.env.STATUS_JS || path.join(__dirname, '..', 'status.js'), 'utf8');
const BOOK = JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures', 'reader-book.json'), 'utf8'));
const BASE = 'https://example.org/book.html';

/* ---------------------------------------------------------------- the served book */

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const ROMAN = ['', 'I', 'II', 'III', 'IV', 'V'];
function chapterHtml(c, i, list, o) {
  const k = c.number;
  const part = BOOK.parts.findIndex(p => p.id === c.part_id) + 1;
  const next = list[i + 1] || null;
  const prev = list[i - 1] || null;
  const other = next || list[0];
  const wrap = o.wrapSections !== false;
  const sec = (n, title, body) => wrap
    ? `<section id="${c.id}-s${n}" data-section aria-labelledby="${c.id}-s${n}-h"><h3 id="${c.id}-s${n}-h"><span class="mg-sec-no">${k}.${n}</span><span class="mg-sec-title">${title}</span></h3>${body}</section>`
    : `<h3 id="${c.id}-s${n}">${k}.${n} ${title}</h3>${body}`;
  const vacuum = [1, 6, 11].includes(k) ? ` It mentions the vacuum of the fixture.` : '';
  const figure = k === 1 ? `<figure id="fig-gaussian-reduction" data-figure="fig-gaussian-reduction" data-qh-figure="fig-gaussian-reduction" data-figure-type="authored_formula" data-chapter="ch01" data-section="ch01-s1" data-figure-chapter="ch01" data-figure-section="ch01-s1">
      <div class="figure-model"><label>a <input type="range" min="0.25" max="4" step="0.25" value="2"></label><svg viewBox="0 0 10 10"><text x="1" y="5">zetanode</text></svg></div>
      <figcaption><p data-block-title>Integrating the coupled displacement</p><p>Fixture caption words for the first figure.</p></figcaption></figure>` : '';
  return `
  <article id="${c.id}" data-chapter data-part="${c.part_id}" data-number="${k}" aria-labelledby="${c.id}-h">
    <header class="chapter-head">
      <p data-chapter-kicker><a href="#${c.part_id}-title">Part ${ROMAN[part]}</a> · Chapter ${k}</p>
      <h2 id="${c.id}-h"><span class="mg-ch-no">${k}</span><span class="mg-ch-name">${esc(c.title)}</span></h2>
      <nav data-prerequisites aria-label="Builds on"><ul>${c.prerequisites.map(p => `<li><a href="#${p}" data-ref="chapter">Chapter ${+p.slice(2)}</a></li>`).join('')}</ul></nav>
      ${wrap ? `<ol class="mg-ch-toc"><li><a href="#${c.id}-s1" data-ref="section"><span class="mg-sec-no">${k}.1</span> <span class="mg-sec-title">First section of chapter ${k}</span></a></li><li><a href="#${c.id}-s2" data-ref="section"><span class="mg-sec-no">${k}.2</span> <span class="mg-sec-title">Second section of chapter ${k}</span></a></li></ol>` : ''}
    </header>
    <div class="chapter-opening"><p>Opening paragraph of chapter ${k}, fixture text.</p></div>
    ${sec(1, `First section of chapter ${k}`, `
      <p>Text of the first section of chapter ${k}, with the token sample${k}.${vacuum}</p>
      <div data-env="definition" id="def-${c.id}"><p data-block-title><span class="env-label">Definition ${k}.1</span> (<dfn>fixture term ${k}</dfn>)</p><p>Defining words for fixture term ${k}.</p></div>
      <p id="${c.id}-refs">A reference to <a href="#def-${other.id}">fixture term ${other.number}</a>, to <a href="#thm-${other.id}">Theorem ${other.number}.2</a>, to <a href="#eq-${c.id}">(${k}.1)</a> and to <a href="#${other.id}-s2">Section ${other.number}.2</a>.</p>
      <div class="mg-eq" id="eq-${c.id}"><div class="math-display"><math display="block"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">x^{2}</annotation></semantics></math></div><span class="eq-number">(${k}.1)</span></div>
      ${figure}`)}
    ${sec(2, k === 1 ? 'Second section of chapter 1 with <math><semantics><msub><mi>x</mi><mn>1</mn></msub><annotation encoding="application/x-tex">x_1</annotation></semantics></math>' : `Second section of chapter ${k}`, `
      <div data-env="theorem" id="thm-${c.id}"><p data-block-title>Theorem ${k}.2 (Result ${k})</p><p>Hypotheses of result ${k}. Conclusion of result ${k}.</p></div>
      <div data-env="proof"><p>Proof words of chapter ${k}.</p></div>
      <p>A paragraph without an address in chapter ${k}, holding the word lantern${k}.</p>
      <p><strong>Weaving${k}.</strong> A paragraph that introduces <strong>braid${k}</strong> in bold.</p>`)}
    <nav data-chapter-end aria-label="Next">${prev ? `<a rel="prev" href="#${prev.id}">Chapter ${prev.number}</a>` : ''}${next ? `<a rel="next" href="#${next.id}">Chapter ${next.number} · ${esc(next.title)}</a>` : ''}</nav>
  </article>`;
}
const ATLAS_IDS = n => ['atlas', 'atlas-h'].concat(Array.from({ length: n }, (_, i) => 'atlas-c-' + (i + 1)));
function pagesMap(o) {
  return { book: 'book.html', title: BOOK.title, index: 'reader-index.js', pages: [
    { href: 'reference.html', parts: [{ id: 'results', title: 'Principal results' }], ids: ['results', 'results-h', 's-old-1'] },
    { href: 'atlas.html', parts: [{ id: 'atlas', title: 'Atlas' }], ids: ATLAS_IDS(o.atlasUnits == null ? 40 : o.atlasUnits) }] };
}
function book(o) {
  o = o || {};
  if (o.companion) return companionPage(o);
  const list = BOOK.chapters.filter(c => !o.chapters || o.chapters.includes(c.id));
  const labels = Object.entries(o.labels || {}).map(([k, v]) => ` data-label-${k}="${esc(v)}"`).join('');
  const count = o.chapterCount ? ` data-chapter-count="${o.chapterCount}"` : '';
  const atlasN = o.atlasUnits == null ? 40 : o.atlasUnits;
  const atlas = Array.from({ length: atlasN }, (_, n) =>
    `<li id="atlas-c-${n + 1}" data-qh-unit data-qh-unit-title="Claim ${n + 1}" data-qh-unit-place="Domain ${1 + (n % 4)}"><p>Claim ${n + 1} of the fixture atlas concerns the vacuum.</p><a href="#atlas-c-${n + 2}">next claim</a> <a href="#ch05">Chapter 5</a></li>`).join('');
  const routes = (BOOK.routes || []).map(r => `<li><a href="#${r.chapter_ids[0]}" data-route="${r.id}" data-route-chapters="${r.chapter_ids.join(' ')}">${esc(r.title)}</a></li>`).join('');
  const toc = BOOK.parts.map(p => {
    const cs = list.filter(c => c.part_id === p.id);
    if (!cs.length) return '';
    return `<li data-part="${p.id}"><span id="${p.id}-title">${esc(p.title)}</span><ol>${cs.map(c =>
      `<li><a href="#${c.id}" data-chapter-link>${c.number}. ${esc(c.title)}</a><ol><li><a href="#${c.id}-s1">${c.number}.1</a></li><li><a href="#${c.id}-s2">${c.number}.2</a></li></ol></li>`).join('')}</ol></li>`;
  }).join('');
  const redirects = o.redirects ? `<script type="application/json" id="reader-redirects">${JSON.stringify(o.redirects)}</script>` : '';
  const atlasStub = `<script>(function () {
    var mount = document.querySelector('[data-atlas-mount]');
    window.__reveals = [];
    if (!mount) return;
    mount.addEventListener('qh:reveal', function (e) { window.__reveals.push(e.detail.id); if (window.__atlasHandles && /^atlas-c-/.test(e.detail.id)) e.preventDefault(); });
    mount.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#"]'); if (!a) return;
      var id = a.getAttribute('href').slice(1); var t = document.getElementById(id);
      if (t && !mount.contains(t)) { var ask = new CustomEvent('qh:navigate', { bubbles: true, cancelable: true, detail: { id: id } }); if (!a.dispatchEvent(ask)) e.preventDefault(); }
    });
  })();</script>`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${esc(BOOK.title)}</title></head><body>
<a class="skip" href="#main">Skip to the text</a>
${o.servedBar ? `<div class="site-head"><div data-reader-bar>${o.barLinks || ''}</div></div>` : ''}
<main id="main" data-reader${labels}${count}>
  ${o.noFront ? '' : `<header id="front" data-reader-front><h1>${esc(BOOK.title)}</h1><p>${esc(BOOK.subtitle)}</p><p>${esc(BOOK.audience)}</p>
    ${o.introduction || ''}<nav data-routes aria-label="Routes"><ul>${routes}</ul></nav></header>
  <nav id="contents" data-reader-toc aria-labelledby="contents-h"><h2 id="contents-h">Contents</h2><ol>${toc}</ol>
    <ul><li><a href="#glossary">Glossary</a></li><li><a href="#atlas">Atlas</a></li></ul></nav>`}
  ${list.map((c, i) => chapterHtml(c, i, list, o)).join('\n')}
  <section id="glossary" data-reference aria-labelledby="glossary-h"><h2 id="glossary-h">Glossary</h2>
    <dl><dt id="gl-vacuum">vacuum</dt><dd>Gloss words for the vacuum. See <a href="#def-ch01">Definition 1.1</a>.</dd>
        <dt id="gl-lantern">lantern</dt><dd>Gloss words for the lantern.</dd></dl></section>
  ${o.split ? '' : `<section id="results" data-reference aria-labelledby="results-h"><h2 id="results-h">Principal results</h2>
    <div class="statement" id="s-old-1"><h3 class="statement-title">Old statement one</h3><p>Old statement text about the vacuum.</p></div></section>
  <section id="atlas" data-reference data-atlas-mount aria-labelledby="atlas-h"><h2 id="atlas-h">Atlas</h2><div class="atlas-body"><ol>${atlas}</ol></div></section>`}
  ${o.tracker ? `<section data-reference id="examples" class="section" aria-labelledby="examples-h"><h2 id="examples-h">Examples</h2>
    <details class="row" id="row-alpha"><summary><span class="row-num">1</span><span class="row-name">Row alpha</span></summary>
      <div class="statement" id="s-in-row"><h3 class="statement-title">Statement inside a row</h3><p>Row statement words.</p></div></details>
    <p id="old-para">An old paragraph with the <button type="button" class="term" data-term="term-ox" aria-haspopup="dialog" aria-expanded="false" aria-controls="card">ox</button> term.</p></section>
  <section data-reference id="terms" class="section terms-section" aria-labelledby="terms-h"><h2 id="terms-h">Terms</h2>
    <dl class="glossary"><div class="gloss" id="term-ox"><dt>ox</dt><dd>Gloss words for the ox.</dd></div></dl></section>` : ''}
</main>
${o.tracker ? '<div class="card" id="card" role="dialog" aria-modal="false" hidden><div class="card-inner"></div></div>' : ''}
${o.split ? `<script type="application/json" id="reader-pages">${JSON.stringify(pagesMap(o))}</script>` : ''}
${redirects}${atlasStub}
${o.status && !o.statusAfter ? `<script>${STATUS}</script>` : ''}
<script>${SCRIPT}</script>
${o.status && o.statusAfter ? `<script>${STATUS}</script>` : ''}
</body></html>`;
}

function companionPage(o) {
  const n = o.atlasUnits == null ? 40 : o.atlasUnits;
  const parts = o.companion === 'atlas'
    ? `<section id="atlas" data-reference data-atlas-mount aria-labelledby="atlas-h"><h2 id="atlas-h">Atlas</h2><div class="atlas-body"><ol>${Array.from({ length: n }, (_, i) =>
        `<li id="atlas-c-${i + 1}" data-qh-unit data-qh-unit-title="Claim ${i + 1}" data-qh-unit-place="Domain ${1 + (i % 4)}"><p>Claim ${i + 1} of the fixture atlas concerns the vacuum.</p><a href="#atlas-c-${i + 2}">next claim</a> <a href="book.html#ch05">Chapter 5</a></li>`).join('')}</ol></div></section>`
    : `<section id="results" data-reference aria-labelledby="results-h"><h2 id="results-h">Principal results</h2>
    <div class="statement" id="s-old-1"><h3 class="statement-title">Old statement one</h3><p>Old statement text about the vacuum. See <a href="#ch05">Chapter 5</a> and <a href="#atlas-c-2">claim 2</a>.</p></div></section>`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${esc(BOOK.title)}</title></head><body>
<main id="main" data-reader data-reader-book="book.html">${parts}</main>
<script type="application/json" id="reader-pages">${JSON.stringify(pagesMap(o))}</script>
<script>${SCRIPT}</script>
</body></html>`;
}

/* ---------------------------------------------------------------- harness */

const opened = [];
function load(o) {
  o = o || {};
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented: navigation/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
  vc.on('error', (...a) => errors.push('console.error: ' + a.join(' ')));
  const dom = new JSDOM(o.html || book(o.book), {
    url: (o.page ? BASE.replace('book.html', o.page) : BASE) + (o.url || ''),
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    virtualConsole: vc,
    beforeParse(w) {
      w.__scrolled = [];
      w.__scrolledTo = [];
      if (o.noFind) delete w.HTMLElement.prototype.onbeforematch; /* a browser whose find cannot reach hidden-until-found text */
      w.Element.prototype.scrollIntoView = function () { w.__scrolled.push(this); };
      w.scrollTo = function (x, y) { w.__scrolledTo.push([x, y]); };
      if (o.hover) w.matchMedia = q => ({ matches: /hover: hover/.test(q), media: q, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
      if (o.storage === 'throw') {
        ['localStorage', 'sessionStorage'].forEach(name => Object.defineProperty(w, name, { configurable: true, get() { throw new Error('storage denied'); } }));
      }
      if (o.storageSeed) Object.keys(o.storageSeed).forEach(k => w.localStorage.setItem(k, o.storageSeed[k]));
      if (o.index) w.QH_READER_INDEX = o.index;
      w.__left = [];
      w.addEventListener('qh:leave', e => { w.__left.push(JSON.parse(JSON.stringify(e.detail))); e.preventDefault(); }, true);
      if (o.before) o.before(w);
    }
  });
  const w = dom.window;
  opened.push(dom);
  return { dom, w, d: w.document, errors };
}
const sleep = ms => new Promise(r => setTimeout(r, ms));
const settle = () => sleep(60);
function key(target, k, extra) {
  const e = new target.ownerDocument.defaultView.KeyboardEvent('keydown', Object.assign({ key: k, bubbles: true, cancelable: true }, extra || {}));
  target.dispatchEvent(e);
  return e;
}
function click(el, extra) {
  const e = new el.ownerDocument.defaultView.MouseEvent('click', Object.assign({ bubbles: true, cancelable: true, button: 0 }, extra || {}));
  el.dispatchEvent(e);
  return e;
}
async function traverseHistory(p, direction) {
  await new Promise((resolve, reject) => {
    function arrived() {
      clearTimeout(timeout);
      resolve();
    }
    const timeout = setTimeout(() => {
      p.w.removeEventListener('popstate', arrived);
      reject(new Error('No popstate after history.' + direction));
    }, 15000);
    p.w.addEventListener('popstate', arrived, { once: true });
    p.w.history[direction]();
  });
  await settle();
}
async function back(p) { await traverseHistory(p, 'back'); }
async function forward(p) { await traverseHistory(p, 'forward'); }
async function type(p, text) {
  const q = p.d.getElementById('reader-q');
  const line = p.d.getElementById('reader-search-status');
  const seen = () => line.textContent + '|' + p.d.querySelectorAll('#reader-results .reader-hit-link').length;
  const before = seen();
  q.focus();
  q.value = text;
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(150);
  for (let i = 0; i < 40 && seen() === before; i++) await sleep(25);
  return q;
}
const text = el => (el ? el.textContent : '').replace(/\s+/g, ' ').trim();
const plain = v => JSON.parse(JSON.stringify(v)); /* values from the page's realm, compared by their contents */
const $ = (p, s) => p.d.querySelector(s);
const $$ = (p, s) => [...p.d.querySelectorAll(s)];
const PLACES = 'main article[data-chapter], main section[data-reference]';
function shown(p) { return $$(p, PLACES).filter(el => !el.hasAttribute('hidden')).map(el => el.id); }
function hitLinks(p) { return $$(p, '#reader-results .reader-hit-link'); }
function noErrors(p) { assert.deepEqual(p.errors, [], 'script errors: ' + p.errors.join(' | ')); }

const tests = [];
function test(name, fn) { tests.push({ name, fn }); }

test('print: printed passages stay local and off-page passages open their online owner only during printing', () => {
  const p = load({ book: { split: true }, url: '#ch01' });
  const canonical = p.d.createElement('link');
  canonical.rel = 'canonical';
  canonical.href = 'https://example.org/';
  p.d.head.append(canonical);
  const original = ['#eq-ch01', '#def-ch02', 'reference.html#results', '#atlas-c-1', '#unknown',
    'celestial-residue.pdf', 'https://example.org/author', 'https://library.example/paper#section'];
  const entry = p.d.getElementById('ch01-refs');
  const links = original.map(href => {
    const a = p.d.createElement('a');
    a.setAttribute('href', href);
    entry.append(a);
    return a;
  });
  p.d.getElementById('eq-ch01').getClientRects = () => [{}];
  const state = () => links.map(a => a.getAttribute('href'));
  const print = name => p.w.dispatchEvent(new p.w.Event(name));
  const printed = ['#eq-ch01', 'https://example.org/#def-ch02', 'https://example.org/reference.html#results',
    'https://example.org/atlas.html#atlas-c-1', ...original.slice(4)];
  print('beforeprint');
  assert.deepEqual(state(), printed);
  print('beforeprint');
  assert.deepEqual(state(), printed);
  print('afterprint');
  assert.deepEqual(state(), original);
  const historyLength = p.w.history.length;
  p.w.history.replaceState(null, '', '/#ch01');
  print('beforeprint');
  assert.equal(links[1].href, 'https://example.org/?#def-ch02');
  links[2].setAttribute('href', '#new-destination');
  print('afterprint');
  assert.equal(links[1].getAttribute('href'), '#def-ch02');
  assert.equal(links[2].getAttribute('href'), '#new-destination');
  assert.equal(p.w.history.length, historyLength);
  assert.equal(p.w.location.hash, '#ch01');
  assert.deepEqual(p.errors, []);
});

/* ---------------------------------------------------------------- one place at a time */

test('start: a bare visit shows the title page and the contents, and every chapter and reference part waits hidden until found', async () => {
  const p = load();
  await settle();
  assert.equal($(p, 'main').getAttribute('data-reader-view'), 'front');
  assert.equal($(p, '#front').hasAttribute('hidden'), false);
  assert.equal($(p, '#contents').hasAttribute('hidden'), false);
  const places = $$(p, PLACES);
  assert.equal(places.length, 18 + 3);
  places.forEach(el => assert.equal(el.getAttribute('hidden'), 'until-found', el.id + ' is hidden until found'));
  const next = $(p, '.reader-bar .reader-next');
  assert.equal(next.hidden, false);
  assert.equal(next.getAttribute('href'), '#ch01');
  assert.match(next.getAttribute('aria-label'), /^Begin with chapter 1: /);
  assert.equal($(p, '.reader-bar .reader-prev').hidden, true);
  noErrors(p);
});

test('start: where the browser cannot find hidden text, the places not shown are simply hidden', async () => {
  const p = load({ noFind: true, url: '#ch04' });
  await settle();
  assert.deepEqual(shown(p), ['ch04']);
  assert.equal(p.d.getElementById('ch05').getAttribute('hidden'), '');
  assert.equal(p.d.getElementById('atlas').getAttribute('hidden'), '');
  noErrors(p);
});

test('start: the 955-claim register is never the default scroll: the atlas is shown only when it is addressed', async () => {
  const p = load({ book: { atlasUnits: 300 } });
  await settle();
  assert.equal($(p, '#atlas').getAttribute('hidden'), 'until-found');
  click($(p, '.reader-bar .reader-next'));
  assert.deepEqual(shown(p), ['ch01']);
  assert.equal($(p, '#atlas').getAttribute('hidden'), 'until-found');
  noErrors(p);
});

test('address: a chapter address shows that chapter alone, with its part, number and neighbours in the bar and the contents', async () => {
  const p = load({ url: '#ch06' });
  await settle();
  assert.deepEqual(shown(p), ['ch06']);
  assert.equal($(p, 'main').getAttribute('data-reader-view'), 'chapter');
  assert.equal(text($(p, '.reader-position-part')), 'Part II');
  assert.equal(text($(p, '.reader-position-chapter')), 'Chapter 6 of 18');
  assert.equal(text($(p, '.reader-position-title')), BOOK.chapters[5].title);
  assert.equal($(p, '.reader-prev').getAttribute('href'), '#ch05');
  assert.equal($(p, '.reader-next').getAttribute('href'), '#ch07');
  assert.match($(p, '.reader-prev').getAttribute('aria-label'), /^Previous chapter: Chapter 5, /);
  assert.equal($(p, '#contents a[href="#ch06"]').getAttribute('aria-current'), 'page');
  assert.equal($(p, '#contents').hasAttribute('hidden'), true, 'the contents wait behind the bar');
  assert.equal($(p, '#front').getAttribute('hidden'), 'until-found');
  noErrors(p);
});

test('address: an address inside a chapter (a definition, an equation, a figure by its own id) shows its chapter and reaches it', async () => {
  for (const id of ['def-ch09', 'eq-ch03', 'fig-gaussian-reduction', 'ch12-s2']) {
    const p = load({ url: '#' + id });
    await settle();
    const t = p.d.getElementById(id);
    assert.deepEqual(shown(p), [t.closest('article[data-chapter]').id], id);
    assert.ok(p.w.__scrolled.includes(t), id + ' is scrolled to');
    assert.ok(t.hasAttribute('data-revealed'), id + ' is marked');
    assert.equal(p.d.getElementById(id).id, id, 'the figure keeps its own id verbatim');
    noErrors(p);
  }
});

test('address: a retained reference part keeps its old addresses (no redirect needed)', async () => {
  const p = load({ url: '#s-old-1' });
  await settle();
  assert.deepEqual(shown(p), ['results']);
  assert.equal($(p, 'main').getAttribute('data-reader-view'), 'reference');
  assert.ok(p.w.__scrolled.includes(p.d.getElementById('s-old-1')));
  assert.equal(text($(p, '.reader-position-chapter')), 'Reference');
  noErrors(p);
});

test('address: an old address the page maps is shown at its new place, and the address is rewritten', async () => {
  const p = load({ url: '#old-thing', book: { redirects: { 'old-thing': 'thm-ch04' } } });
  await settle();
  assert.deepEqual(shown(p), ['ch04']);
  assert.equal(p.w.location.hash, '#thm-ch04');
  noErrors(p);
});

test('address: an unknown address is named, in view, with a search for its words, on the title page', async () => {
  const p = load({ url: '#def-hall-correspondence' });
  await settle();
  const n = $(p, '.reader-notice[data-notice="unknown"]');
  assert.ok(n, 'a notice');
  assert.match(text(n), /#def-hall-correspondence/);
  assert.equal($(p, 'main').getAttribute('data-reader-view'), 'front');
  const act = n.querySelector('.reader-notice-action');
  assert.match(text(act), /hall correspondence/);
  click(act);
  await sleep(150);
  assert.equal($(p, '#reader-search').hidden, false);
  assert.equal($(p, '#reader-q').value, 'hall correspondence');
  noErrors(p);
});

test('address: a component may claim an address the page does not have', async () => {
  const p = load({ url: '#atlas-claim-999', before(w) { w.document.addEventListener('qh:unknown-anchor', e => { if (e.detail.id === 'atlas-claim-999') e.preventDefault(); }); } });
  await settle();
  assert.equal($(p, '.reader-notice'), null);
  noErrors(p);
});

/* ---------------------------------------------------------------- sequential reading and history */

test('sequence: Next and Previous move by chapter with focus on the new chapter title, each a history entry, and announce the chapter', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  const seen = [];
  p.d.addEventListener('qh:chapter', e => seen.push(e.detail));
  const len = p.w.history.length;
  const next = $(p, '.reader-bar .reader-next');
  next.focus();
  click(next);
  assert.deepEqual(shown(p), ['ch04']);
  assert.equal(p.w.location.hash, '#ch04');
  assert.equal(p.w.history.length, len + 1);
  assert.equal(p.d.activeElement, p.d.getElementById('ch04-h'));
  assert.deepEqual(plain(seen), [{ id: 'ch04', number: '4', part: 'p1' }]);
  click($(p, '.reader-bar .reader-prev'));
  assert.deepEqual(shown(p), ['ch03']);
  assert.equal(p.w.history.length, len + 2);
  noErrors(p);
});

test('history: Back returns to the chapter and to the control that was used; Forward goes on again', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  const next = $(p, '.reader-bar .reader-next');
  next.focus();
  click(next);
  assert.deepEqual(shown(p), ['ch04']);
  await back(p);
  assert.deepEqual(shown(p), ['ch03']);
  assert.equal(p.d.activeElement, $(p, '.reader-bar .reader-next'), 'focus back on the control used');
  await forward(p);
  assert.deepEqual(shown(p), ['ch04']);
  noErrors(p);
});

test('history: the end of a chapter leads to the next one, and Back returns to the end link', async () => {
  const p = load({ url: '#ch07' });
  await settle();
  const end = $(p, '#ch07 [data-chapter-end] a[rel="next"]');
  end.focus();
  click(end);
  assert.deepEqual(shown(p), ['ch08']);
  await back(p);
  assert.deepEqual(shown(p), ['ch07']);
  assert.equal(p.d.activeElement, end);
  noErrors(p);
});

test('history: a typed address is followed once, and Back after it returns', async () => {
  const p = load({ url: '#ch02' });
  await settle();
  p.w.location.hash = '#ch10';
  await sleep(80);
  assert.deepEqual(shown(p), ['ch10']);
  await back(p);
  assert.deepEqual(shown(p), ['ch02']);
  noErrors(p);
});

test('history: the entry left keeps the reading position, restored on Back', async () => {
  const p = load({ url: '#ch02' });
  await settle();
  Object.defineProperty(p.w, 'pageYOffset', { configurable: true, value: 1234 });
  click($(p, '.reader-bar .reader-next'));
  const prev = p.w.history.state;
  assert.ok(prev && prev.reader && prev.reader.id === 'ch03');
  p.w.__scrolledTo.length = 0;
  await back(p);
  assert.ok(p.w.__scrolledTo.length > 0, 'the position is restored');
  noErrors(p);
});

/* ---------------------------------------------------------------- the contents */

test('contents: in a chapter the bar opens the contents at the current chapter; Escape closes them and returns focus', async () => {
  const p = load({ url: '#ch05' });
  await settle();
  const toggle = $(p, '.reader-contents-toggle');
  assert.match(text(toggle), /Chapter 5 of 18/, 'the toggle names the place');
  click(toggle);
  const toc = $(p, '#contents');
  assert.equal(toc.hasAttribute('hidden'), false);
  assert.ok(toc.hasAttribute('data-drawer'));
  assert.equal(toggle.getAttribute('aria-expanded'), 'true');
  const at = p.d.activeElement;
  assert.ok(at.closest('#contents') && at.closest('li[data-current]') === $(p, '#contents a[href="#ch05"]').closest('li'), 'focus on the current chapter or its current section in the contents');
  key(p.d.activeElement, 'Escape');
  assert.equal(toc.hasAttribute('hidden'), true);
  assert.equal(toggle.getAttribute('aria-expanded'), 'false');
  assert.equal(p.d.activeElement, toggle);
  noErrors(p);
});

test('contents: a chapter chosen in the contents is shown and the contents close', async () => {
  const p = load({ url: '#ch05' });
  await settle();
  click($(p, '.reader-contents-toggle'));
  click($(p, '#contents a[href="#ch14"]'));
  assert.deepEqual(shown(p), ['ch14']);
  assert.equal($(p, '#contents').hasAttribute('hidden'), true);
  assert.equal(p.d.activeElement, p.d.getElementById('ch14-h'));
  noErrors(p);
});

/* ---------------------------------------------------------------- cross-references keep the place */

test('reminder: a cross-reference opens the definition it names beside the text, without leaving the chapter or the entry', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  const len = p.w.history.length;
  const ref = $(p, '#ch03-refs a[href="#def-ch04"]');
  ref.focus();
  const e = click(ref);
  assert.equal(e.defaultPrevented, true);
  const peek = $(p, '#reader-peek');
  assert.equal(peek.hidden, false);
  assert.equal(peek.getAttribute('role'), 'dialog');
  assert.match(text(peek.querySelector('.reader-peek-body')), /Defining words for fixture term 4/);
  assert.match(text(peek.querySelector('.reader-peek-where')), /^Chapter 4 · 4\.1 /);
  assert.deepEqual([...peek.querySelectorAll('[id]')].map(n => n.id), ['reader-peek-where'], 'the copy carries no id of the page');
  assert.deepEqual(shown(p), ['ch03']);
  assert.equal(p.w.history.length, len);
  assert.equal(ref.getAttribute('aria-expanded'), 'true');
  key(p.d.activeElement, 'Escape');
  assert.equal(peek.hidden, true);
  assert.equal(p.d.activeElement, ref);
  noErrors(p);
});

test('reminder: a result, an equation and a section are shown whole (statement, formula, heading and first paragraph)', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  click($(p, '#ch03-refs a[href="#thm-ch04"]'));
  assert.match(text($(p, '#reader-peek .reader-peek-body')), /Theorem 4\.2 \(Result 4\) ?Hypotheses of result 4\. Conclusion of result 4\./);
  click($(p, '#ch03-refs a[href="#eq-ch03"]'));
  assert.ok($(p, '#reader-peek .reader-peek-body math'), 'the formula itself');
  click($(p, '#ch03-refs a[href="#ch04-s2"]'));
  assert.match(text($(p, '#reader-peek .reader-peek-body')), /4\.2 Second section of chapter 4/);
  noErrors(p);
});

test('reminder: Go to moves there as a history entry, and Back returns to the chapter with focus on the cross-reference', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  const ref = $(p, '#ch03-refs a[href="#thm-ch04"]');
  ref.focus();
  click(ref);
  const go = $(p, '#reader-peek .reader-peek-go');
  assert.equal(go.getAttribute('href'), '#thm-ch04');
  click(go);
  assert.deepEqual(shown(p), ['ch04']);
  assert.equal(p.d.activeElement, p.d.getElementById('thm-ch04'));
  assert.equal($(p, '#reader-peek').hidden, true);
  await back(p);
  assert.deepEqual(shown(p), ['ch03']);
  assert.equal(p.d.activeElement, ref);
  noErrors(p);
});

test('reminder: a prerequisite shows the chapter it names (title and summary or opening) with a way to it', async () => {
  const p = load({ url: '#ch02' });
  await settle();
  const pre = $(p, '#ch02 [data-prerequisites] a[href="#ch01"]');
  click(pre);
  const body = text($(p, '#reader-peek .reader-peek-body'));
  assert.match(body, new RegExp(BOOK.chapters[0].title));
  assert.match(body, /Opening paragraph of chapter 1/);
  assert.match(text($(p, '#reader-peek .reader-peek-go')), /^Go to Chapter 1$/);
  noErrors(p);
});

test('reminder: a modified click and a link marked data-ref="none" are ordinary links', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  const ref = $(p, '#ch03-refs a[href="#def-ch04"]');
  const e = click(ref, { ctrlKey: true });
  assert.equal(e.defaultPrevented, false);
  assert.equal($(p, '#reader-peek').hidden, true);
  ref.setAttribute('data-ref', 'none');
  click(ref);
  assert.equal($(p, '#reader-peek').hidden, true);
  assert.deepEqual(shown(p), ['ch04'], 'followed as a link');
  noErrors(p);
});

test('reminder: Tab past its end goes on in the text after the cross-reference', async () => {
  const p = load({ url: '#ch03' });
  await settle();
  const ref = $(p, '#ch03-refs a[href="#def-ch04"]');
  ref.focus();
  click(ref);
  const go = $(p, '#reader-peek .reader-peek-go');
  go.focus();
  key(go, 'Tab');
  assert.equal($(p, '#reader-peek').hidden, true);
  assert.equal(p.d.activeElement, $(p, '#ch03-refs a[href="#thm-ch04"]'));
  noErrors(p);
});

test('reminder: on a fine pointer, resting on a cross-reference opens a reminder that does not take focus', async () => {
  const p = load({ url: '#ch03', hover: true });
  await settle();
  const ref = $(p, '#ch03-refs a[href="#def-ch04"]');
  const move = (x, y) => ref.dispatchEvent(new p.w.MouseEvent('mousemove', { bubbles: true, screenX: x, screenY: y }));
  move(10, 10);
  move(12, 11);
  await sleep(450);
  assert.equal($(p, '#reader-peek').hidden, false);
  assert.notEqual(p.d.activeElement, $(p, '#reader-peek-where'));
  ref.dispatchEvent(new p.w.MouseEvent('mouseout', { bubbles: true, relatedTarget: p.d.body }));
  await sleep(400);
  assert.equal($(p, '#reader-peek').hidden, true);
  noErrors(p);
});

/* ---------------------------------------------------------------- search */

test('search: "/" opens the search with focus in the field; a figure\'s own controls keep the key', async () => {
  const p = load({ url: '#ch01' });
  await settle();
  const range = $(p, '#fig-gaussian-reduction input');
  range.focus();
  key(range, '/');
  assert.equal($(p, '#reader-search').hidden, true, 'not from inside a control');
  const h = p.d.getElementById('ch01-h');
  h.focus();
  key(h, '/');
  assert.equal($(p, '#reader-search').hidden, false);
  assert.equal(p.d.activeElement, $(p, '#reader-q'));
  assert.equal($(p, '.reader-search-toggle').getAttribute('aria-expanded'), 'true');
  noErrors(p);
});

test('search: the chapters come first, in the book\'s order, and a large reference part shows a few results and offers the rest', async () => {
  const p = load({ book: { atlasUnits: 300 } });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'vacuum');
  const groups = $$(p, '#reader-results .reader-group').map(g => g.getAttribute('data-group'));
  const order = groups.filter(g => g !== 'best');
  assert.deepEqual(order, ['ch01', 'ch06', 'ch11', 'glossary', 'results', 'atlas']);
  const firstLink = hitLinks(p)[0];
  assert.ok(!p.d.getElementById(firstLink.getAttribute('href').slice(1)).closest('#atlas'), 'the first result is not in the atlas');
  const atlasGroup = $(p, '#reader-results .reader-group[data-group="atlas"]');
  assert.equal(atlasGroup.querySelectorAll('.reader-hit-link').length, 3);
  assert.match(text(atlasGroup.querySelector('.reader-group-more')), /^100 more in Atlas$/);
  assert.match(text($(p, '#reader-search-status')), /^30\d results\.$/);
  assert.equal(text($(p, '.reader-scope[data-scope="atlas"] .reader-scope-count')), '300');
  assert.equal(text($(p, '.reader-scope[data-scope="chapters"] .reader-scope-count')), '3');
  noErrors(p);
});

test('search: a result opens its place as a history entry with focus on it; Back reopens the search with focus on that result', async () => {
  const p = load({ url: '#ch02' });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'lantern9');
  const link = hitLinks(p)[0];
  const id = link.getAttribute('href').slice(1);
  const target = p.d.getElementById(id);
  assert.ok(target && target.closest('#ch09'));
  click(link);
  assert.equal($(p, '#reader-search').hidden, true);
  assert.deepEqual(shown(p), ['ch09']);
  assert.equal(p.d.activeElement, target);
  assert.equal(p.w.location.search, '', 'the query stays with the entry it was made in');
  await back(p);
  assert.deepEqual(shown(p), ['ch02']);
  assert.equal($(p, '#reader-search').hidden, false);
  assert.equal($(p, '#reader-q').value, 'lantern9');
  assert.equal(p.d.activeElement.getAttribute('href'), '#' + id);
  assert.match(p.w.location.search, /q=lantern9/);
  noErrors(p);
});

test('search: a paragraph found without an address is given one that holds on a later visit', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'lantern14');
  const href = hitLinks(p)[0].getAttribute('href');
  assert.match(href, /^#ch14-s2-p\d+$/);
  const q = load({ url: href });
  await settle();
  const t = q.d.getElementById(href.slice(1));
  assert.ok(t, 'the address is found on a fresh visit');
  assert.match(text(t), /lantern14/);
  assert.deepEqual(shown(q), ['ch14']);
  noErrors(q);
});

test('search: a defined word or a title typed whole leads with the place it is introduced', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'fixture term 7');
  const best = $(p, '#reader-results .reader-group[data-group="best"]');
  assert.ok(best, 'a best match');
  assert.equal(best.querySelector('.reader-hit-link').getAttribute('href'), '#def-ch07');
  await type(p, 'braid12');
  const first2 = hitLinks(p)[0];
  assert.ok(first2 && p.d.getElementById(first2.getAttribute('href').slice(1)).closest('#ch12'), 'the paragraph that introduces it');
  await type(p, 'Result 5');
  assert.equal(hitLinks(p)[0].getAttribute('href'), '#thm-ch05', 'a name in brackets counts as the title');
  noErrors(p);
});

test('search: a scope lists only its part; Show more adds a hundred with focus on the first new result', async () => {
  const p = load({ book: { atlasUnits: 300 } });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'vacuum');
  click($(p, '.reader-scope[data-scope="atlas"]'));
  assert.equal($(p, '.reader-scope[data-scope="atlas"]').getAttribute('aria-pressed'), 'true');
  const groups = $$(p, '#reader-results .reader-group').map(g => g.getAttribute('data-group'));
  assert.deepEqual(groups, ['atlas']);
  assert.equal(hitLinks(p).length, 100);
  click($(p, '.reader-group-more'));
  assert.equal(hitLinks(p).length, 200);
  assert.equal(p.d.activeElement, hitLinks(p)[100]);
  noErrors(p);
});

test('search: an atlas result shows the atlas and asks the atlas to show it; the atlas keeps scroll and focus when it answers', async () => {
  const p = load({ url: '#ch02', before(w) { w.__atlasHandles = true; } });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'Claim 17');
  const link = hitLinks(p).find(a => a.getAttribute('href') === '#atlas-c-17');
  assert.ok(link, 'the claim is found');
  p.w.__scrolled.length = 0;
  click(link);
  assert.deepEqual(shown(p), ['atlas']);
  assert.deepEqual(plain(p.w.__reveals), ['atlas-c-17']);
  assert.equal(p.w.__scrolled.length, 0, 'the atlas scrolled itself');
  assert.equal($(p, '.reader-prev').getAttribute('aria-label').indexOf('Back to the text'), 0, 'a way back to the text');
  noErrors(p);
});

test('search: an address with ?q= opens the search with that query, without taking focus', async () => {
  const p = load({ url: '?q=lantern3' });
  await settle();
  await sleep(100);
  assert.equal($(p, '#reader-search').hidden, false);
  assert.equal($(p, '#reader-q').value, 'lantern3');
  assert.ok(hitLinks(p).length >= 1);
  assert.notEqual(p.d.activeElement, $(p, '#reader-q'));
  noErrors(p);
});

test('search: Escape closes the search, returns focus to where "/" was pressed and drops the query from the address', async () => {
  const p = load({ url: '#ch04' });
  await settle();
  const h = p.d.getElementById('ch04-h');
  h.focus();
  key(h, '/');
  await type(p, 'lantern4');
  await sleep(400);
  assert.match(p.w.location.search, /q=lantern4/);
  key($(p, '#reader-q'), 'Escape');
  assert.equal($(p, '#reader-search').hidden, true);
  assert.equal(p.d.activeElement, h);
  assert.equal(p.w.location.search, '');
  noErrors(p);
});

test('search: arrow keys move through the results, and Escape from a result returns to the field', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'vacuum');
  const q = $(p, '#reader-q');
  key(q, 'ArrowDown');
  const links = hitLinks(p);
  assert.equal(p.d.activeElement, links[0]);
  key(links[0], 'ArrowDown');
  assert.equal(p.d.activeElement, links[1]);
  key(links[1], 'ArrowUp');
  assert.equal(p.d.activeElement, links[0]);
  key(links[0], 'Escape');
  assert.equal(p.d.activeElement, q);
  noErrors(p);
});

/* ---------------------------------------------------------------- components, find, the place kept */

test('component: a link inside the atlas is left to the atlas; its request to show a place of the book is honoured', async () => {
  const p = load({ url: '#atlas-c-3' });
  await settle();
  const inner = $(p, '#atlas-c-3 a[href="#atlas-c-4"]');
  const e1 = click(inner);
  assert.equal(e1.defaultPrevented, false, 'the atlas follows its own address');
  const out = $(p, '#atlas-c-3 a[href="#ch05"]');
  const e2 = click(out);
  assert.equal(e2.defaultPrevented, true, 'the page answered the request');
  assert.deepEqual(shown(p), ['ch05']);
  noErrors(p);
});

test('component: every change of place is told to components (qh:state) with the view and the place', async () => {
  const p = load();
  await settle();
  const states = [];
  p.d.addEventListener('qh:state', e => states.push(e.detail));
  click($(p, '.reader-bar .reader-next'));
  assert.deepEqual(plain(states[states.length - 1]), { q: '', view: 'chapter', id: 'ch01' });
  noErrors(p);
});

test('find: the browser\'s find in a hidden chapter shows that chapter, as a history entry, and leaves the scrolling to the browser', async () => {
  const p = load({ url: '#ch02' });
  await settle();
  const len = p.w.history.length;
  p.w.__scrolled.length = 0;
  p.d.getElementById('ch15').dispatchEvent(new p.w.Event('beforematch', { bubbles: true }));
  assert.deepEqual(shown(p), ['ch15']);
  assert.equal(p.w.history.length, len + 1);
  assert.equal(p.w.location.hash, '#ch15');
  assert.equal(p.w.__scrolled.length, 0);
  await back(p);
  assert.deepEqual(shown(p), ['ch02']);
  noErrors(p);
});

test('place: the place read is kept on this device and offered on a bare visit; Continue reading goes there and Close forgets it', async () => {
  const p = load({ url: '#ch08' });
  await settle();
  p.w.dispatchEvent(new p.w.Event('pagehide'));
  const kept = JSON.parse(p.w.localStorage.getItem('qh-reader-place'));
  assert.ok(kept && /^ch08/.test(kept.id), 'kept: ' + JSON.stringify(kept));
  const q = load({ storageSeed: { 'qh-reader-place': JSON.stringify(kept) } });
  await settle();
  const n = $(q, '.reader-notice[data-notice="resume"]');
  assert.ok(n);
  assert.match(text(n), /You were reading “Chapter 8 · /);
  click(n.querySelector('a.reader-notice-action'));
  assert.deepEqual(shown(q), ['ch08']);
  assert.equal($(q, '.reader-notice'), null, 'the notice is gone');
  const r = load({ storageSeed: { 'qh-reader-place': JSON.stringify(kept) } });
  await settle();
  click($(r, '.reader-notice-close'));
  assert.equal(r.w.localStorage.getItem('qh-reader-place'), null);
  noErrors(p); noErrors(q); noErrors(r);
});

test('place: a kept place whose title no longer matches is not offered; refused storage costs nothing', async () => {
  const p = load({ storageSeed: { 'qh-reader-place': JSON.stringify({ id: 'ch08', title: 'Chapter 8 · Something else', at: 1 }) } });
  await settle();
  assert.equal($(p, '.reader-notice'), null);
  const q = load({ storage: 'throw', url: '#ch03' });
  await settle();
  click($(q, '.reader-bar .reader-next'));
  q.w.dispatchEvent(new q.w.Event('pagehide'));
  assert.deepEqual(shown(q), ['ch04']);
  noErrors(p); noErrors(q);
});

/* ---------------------------------------------------------------- routes, words, shape */

test('route: following a route makes Next follow it, and leaving it restores the book\'s order', async () => {
  const p = load();
  await settle();
  const route = BOOK.routes.find(r => r.id === 'arithmetic');
  click($(p, 'a[data-route="arithmetic"]'));
  assert.deepEqual(shown(p), [route.chapter_ids[0]]);
  p.w.location.hash = '#ch08';
  await sleep(80);
  const after8 = route.chapter_ids[route.chapter_ids.indexOf('ch08') + 1];
  assert.equal($(p, '.reader-next').getAttribute('href'), '#' + after8);
  assert.equal($(p, '.reader-route').hidden, false);
  assert.match(text($(p, '.reader-route-text')), /^Arithmetic route, step 8 of 12$/, 'a route position, not a chapter number');
  click($(p, '.reader-route-leave'));
  assert.equal($(p, '.reader-next').getAttribute('href'), '#ch09');
  assert.equal($(p, '.reader-route').hidden, true);
  noErrors(p);
});

test('steps: each step says where it goes, and its name says it in full', async () => {
  const p = load({ url: '#ch06' });
  await settle();
  const prev = $(p, '.reader-prev');
  assert.deepEqual([...prev.children].map(n => n.className), ['reader-step-arrow', 'reader-step-label', 'reader-step-title']);
  assert.equal(text(prev.querySelector('.reader-step-label')), 'Previous');
  assert.equal(text(prev.querySelector('.reader-step-title')), 'Chapter 5 · ' + BOOK.chapters[4].title);
  assert.equal(prev.getAttribute('data-step'), 'previous');
  assert.equal(prev.getAttribute('aria-label'), 'Previous chapter: Chapter 5, ' + BOOK.chapters[4].title);
  noErrors(p);
});

test('hooks: a figure that carries data-chapter and data-section values is neither a chapter nor a section', async () => {
  const p = load({ url: '#ch01' });
  await settle();
  const fig = p.d.getElementById('fig-gaussian-reduction');
  assert.equal(fig.hasAttribute('hidden'), false);
  assert.equal(text($(p, '.reader-position-chapter')), 'Chapter 1 of 18');
  click($(p, '.reader-next'));
  assert.deepEqual(shown(p), ['ch02'], 'Next goes to the next chapter, not to the figure');
  click($(p, '.reader-search-toggle'));
  await type(p, 'zetanode');
  assert.equal(hitLinks(p)[0].getAttribute('href'), '#fig-gaussian-reduction', 'a label drawn in the figure finds it');
  noErrors(p);
});

test('search: a formula found is addressed by the author\'s equation id, not by a new one', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'x^{2}');
  const hrefs = hitLinks(p).map(a => a.getAttribute('href'));
  assert.ok(hrefs.includes('#eq-ch01'), hrefs.slice(0, 5).join(' '));
  assert.ok(!hrefs.some(h => /^#ch\d+$/.test(h)), 'a chapter is not found by the formulae of its text: ' + hrefs.filter(h => /^#ch\d+$/.test(h)).join(' '));
  assert.equal(p.d.querySelectorAll('[id^="eq-"][id*="-p"]').length, 0, 'no address given inside an equation');
  noErrors(p);
});

test('hooks: the part named in a chapter\'s head is navigation, not a cross-reference', async () => {
  const p = load({ url: '#ch07' });
  await settle();
  click($(p, '#ch07 [data-chapter-kicker] a'));
  assert.equal($(p, '#reader-peek').hidden, true);
  assert.equal($(p, 'main').getAttribute('data-reader-view'), 'front');
  assert.ok(p.w.__scrolled.includes(p.d.getElementById('p2-title')));
  noErrors(p);
});

test('reference: an address inside a closed row of the reference opens the row and reaches it', async () => {
  const p = load({ url: '#s-in-row', book: { tracker: true } });
  await settle();
  assert.deepEqual(shown(p), ['examples']);
  assert.equal(p.d.getElementById('row-alpha').open, true);
  assert.ok(p.w.__scrolled.includes(p.d.getElementById('s-in-row')));
  noErrors(p);
});

test('reference: without the status page script, a term served as a button opens its glossary entry in a reminder', async () => {
  const p = load({ url: '#examples', book: { tracker: true } });
  await settle();
  const term = $(p, '#old-para button.term');
  term.focus();
  click(term);
  const peek = $(p, '#reader-peek');
  assert.equal(peek.hidden, false);
  assert.match(text(peek.querySelector('.reader-peek-body')), /^ox ?Gloss words for the ox\.$/);
  assert.equal(term.getAttribute('aria-controls'), 'reader-peek');
  assert.equal($(p, '.reader-peek-go').getAttribute('href'), '#term-ox');
  key(p.d.activeElement, 'Escape');
  assert.equal(peek.hidden, true);
  assert.equal(p.d.activeElement, term);
  click($(p, '.reader-search-toggle'));
  await type(p, 'ox');
  assert.equal(hitLinks(p)[0].getAttribute('href'), '#term-ox', 'the glossary entry is found by its term');
  noErrors(p);
});

test('reference: with the status page script beside the reader, its term card answers, and there is one search, one notice area and one place kept', async () => {
  const p = load({ url: '#examples', book: { tracker: true, status: true } });
  await settle();
  const term = $(p, '#old-para button.term');
  click(term);
  const card = p.d.getElementById('card');
  assert.equal(card.hidden, false, 'the status card opens');
  assert.match(text(card), /Gloss words for the ox/);
  assert.equal($(p, '#reader-peek').hidden, true, 'the reader stays out of it');
  assert.equal($$(p, '.find').length, 0, 'no second search');
  assert.equal($$(p, '.qh-notice').length, 0, 'no second notice area');
  assert.equal($$(p, '#reader-search').length, 1);
  key(p.d.body, 'Escape');
  const h = p.d.getElementById('examples-h');
  key(h, '/');
  assert.equal($(p, '#reader-search').hidden, false);
  noErrors(p);
});

test('reference: with the status page script, Back and Forward move between places once, and a row opened before leaving is open again on Back', async () => {
  const p = load({ url: '#examples', book: { tracker: true, status: true } });
  await settle();
  const row = p.d.getElementById('row-alpha');
  row.open = true;
  row.dispatchEvent(new p.w.Event('toggle'));
  await sleep(200);
  const len = p.w.history.length;
  click($(p, '.reader-contents-toggle'));
  click($(p, '#contents a[href="#ch07"]'));
  assert.deepEqual(shown(p), ['ch07']);
  assert.equal(p.w.history.length, len + 1, 'one entry');
  row.open = false;
  await back(p);
  assert.deepEqual(shown(p), ['examples']);
  assert.equal(row.open, true, 'the row is as the reader left it');
  await forward(p);
  assert.deepEqual(shown(p), ['ch07']);
  noErrors(p);
});

test('theme: the bar keeps the page\'s light and dark control, which switches the theme and remembers the choice', async () => {
  const p = load({ url: '#ch02' });
  await settle();
  const b = $(p, '.reader-bar button.theme');
  assert.ok(b, 'the control is in the bar');
  assert.equal(b.getAttribute('aria-label'), 'Switch between light and dark');
  assert.ok(b.querySelector('svg.icon[aria-hidden="true"]'));
  const root = p.d.documentElement;
  const first = root.getAttribute('data-theme');
  click(b);
  const one = root.getAttribute('data-theme');
  assert.ok(one === 'dark' || one === 'light');
  assert.notEqual(one, first);
  assert.equal(p.w.localStorage.getItem('qh-theme'), one);
  click(b);
  assert.notEqual(root.getAttribute('data-theme'), one);
  assert.equal(p.w.localStorage.getItem('qh-theme'), root.getAttribute('data-theme'));
  noErrors(p);
});

test('theme: a choice kept on this device is the page\'s; with storage refused the control still switches', async () => {
  const p = load({ url: '#ch02', storageSeed: { 'qh-theme': 'dark' } });
  await settle();
  p.d.documentElement.setAttribute('data-theme', 'dark'); /* as the page's head script restores it */
  click($(p, 'button.theme'));
  assert.equal(p.d.documentElement.getAttribute('data-theme'), 'light');
  const q = load({ url: '#ch02', storage: 'throw' });
  await settle();
  const before = q.d.documentElement.getAttribute('data-theme');
  click($(q, 'button.theme'));
  assert.notEqual(q.d.documentElement.getAttribute('data-theme'), before);
  noErrors(p); noErrors(q);
});

test('theme: beside the status page script, in either order, one press switches once', async () => {
  for (const statusAfter of [false, true]) {
    const p = load({ url: '#examples', book: { tracker: true, status: true, statusAfter } });
    await settle();
    assert.equal($$(p, 'button.theme').length, 1, 'one control');
    const before = p.d.documentElement.getAttribute('data-theme') || 'light';
    click($(p, 'button.theme'));
    const after = p.d.documentElement.getAttribute('data-theme');
    assert.notEqual(after, before, 'status.js ' + (statusAfter ? 'after' : 'before') + ' the reader');
    assert.equal(p.w.localStorage.getItem('qh-theme'), after);
    noErrors(p);
  }
});

test('hooks: a figure or diagram with data-figure-chapter and data-figure-section values (or the older names) is never a chapter or a section', async () => {
  const p = load({ url: '#fig-gaussian-reduction' });
  await settle();
  assert.deepEqual(shown(p), ['ch01']);
  click($(p, '.reader-contents-toggle'));
  const current = [...p.d.querySelectorAll('#contents [aria-current]')].map(a => a.getAttribute('href'));
  assert.ok(current.every(h => h === '#ch01' || /^#ch01-s\d$/.test(h)), current.join(' '));
  key(p.d.activeElement, 'Escape');
  click($(p, '.reader-next'));
  assert.deepEqual(shown(p), ['ch02']);
  noErrors(p);
});

test('titles: a number the page sets apart in a heading is neither fused with the title nor repeated', async () => {
  const p = load();
  await settle();
  const c1 = BOOK.chapters[0].title;
  const begin = $(p, '.reader-next');
  assert.equal(text(begin.querySelector('.reader-step-title')), 'Chapter 1 · ' + c1);
  assert.equal(begin.getAttribute('aria-label'), 'Begin with chapter 1: Chapter 1, ' + c1);
  click(begin);
  assert.equal(text($(p, '.reader-position-title')), c1);
  assert.equal(text($(p, '.reader-next .reader-step-title')), 'Chapter 2 · ' + BOOK.chapters[1].title);
  click($(p, '#ch01-refs a[href="#ch02-s2"]'));
  assert.match(text($(p, '#reader-peek .reader-peek-body')), /^2\.2 Second section of chapter 2(?!\d)/);
  assert.equal(text($(p, '#reader-peek .reader-peek-where')), 'Chapter 2 · 2.2 Second section of chapter 2');
  key(p.d.activeElement, 'Escape');
  click($(p, '.reader-next'));
  click($(p, '#ch02 [data-prerequisites] a[href="#ch01"]'));
  assert.equal(text($(p, '#reader-peek .reader-peek-title')), 'Chapter 1 · ' + c1);
  key(p.d.activeElement, 'Escape');
  click($(p, '.reader-search-toggle'));
  await type(p, c1);
  const first = hitLinks(p)[0];
  assert.equal(first.getAttribute('href'), '#ch01', 'the chapter comes first for its title');
  assert.equal(text(first.querySelector('.reader-hit-title')), c1, 'titled without its number');
  assert.equal(text($(p, '#reader-results .reader-group[data-group="ch01"] .reader-group-title')), c1);
  noErrors(p);
});

test('words: the page\'s own interface words replace the reader\'s', async () => {
  const p = load({ url: '#ch02', book: { labels: { contents: 'Inhalt', 'chapter-of': 'Kapitel {n} von {total}', search: 'Suche' } } });
  await settle();
  assert.equal(text($(p, '.reader-contents-word')), 'Inhalt');
  assert.equal(text($(p, '.reader-position-chapter')), 'Kapitel 2 von 18');
  assert.equal(text($(p, '.reader-search-toggle')), 'Suche');
  noErrors(p);
});

test('shape: the bar holds six controls whatever the length of the book, in a served slot when the page gives one', async () => {
  const p = load({ url: '#ch09', book: { servedBar: true } });
  await settle();
  const bar = $(p, '[data-reader-bar]');
  assert.ok(bar.classList.contains('reader-bar'));
  assert.ok(bar.closest('.site-head'), 'the served slot is used');
  const controls = [...bar.querySelectorAll('a[href], button')].filter(el => !el.closest('[hidden]') && !el.closest('#reader-search'));
  assert.deepEqual(controls.map(el => el.className), ['reader-home', 'reader-contents-toggle', 'reader-prev', 'reader-next', 'reader-search-toggle', 'theme reader-theme']);
  noErrors(p);
});

test('shape: when only some chapters are served the bar still counts the whole book, and the sequence skips the missing ones', async () => {
  const p = load({ url: '#ch05', book: { chapters: ['ch01', 'ch02', 'ch05', 'ch07'], chapterCount: 18 } });
  await settle();
  assert.equal(text($(p, '.reader-position-chapter')), 'Chapter 5 of 18');
  assert.equal($(p, '.reader-prev').getAttribute('href'), '#ch02');
  assert.equal($(p, '.reader-next').getAttribute('href'), '#ch07');
  noErrors(p);
});

test('shape: without section wrappers, headings with an address serve as the sections', async () => {
  const p = load({ url: '#ch06-s2', book: { wrapSections: false } });
  await settle();
  assert.deepEqual(shown(p), ['ch06']);
  assert.ok(p.w.__scrolled.includes(p.d.getElementById('ch06-s2')));
  click($(p, '.reader-search-toggle'));
  await type(p, 'Second section of chapter 6');
  assert.equal(hitLinks(p)[0].getAttribute('href'), '#ch06-s2');
  noErrors(p);
});

test('style: the reader adds no stylesheet and no inline style beyond its two measures', async () => {
  const p = load({ url: '#ch03', hover: true });
  await settle();
  click($(p, '#ch03-refs a[href="#def-ch04"]'));
  assert.equal(p.d.querySelectorAll('style').length, 0);
  $$(p, '[style]').forEach(el => {
    const props = Array.from({ length: el.style.length }, (_, i) => el.style[i]).filter(prop => !prop.startsWith('--'));
    assert.deepEqual(props, [], el.tagName + ' has ' + el.getAttribute('style'));
  });
  noErrors(p);
});



/* ---------------------------------------------------------------- results on a narrow screen */

test('narrow: before any result no scope is offered; with results only All, the scope pressed and the scopes holding results', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  assert.equal($(p, '.reader-search-scopes').hidden, true, 'nothing to choose before a result');
  await type(p, 'lantern3');
  assert.equal($(p, '.reader-search-scopes').hidden, false);
  const shownScopes = () => $$(p, '.reader-scope').filter(b => !b.hidden).map(b => b.getAttribute('data-scope'));
  assert.deepEqual(shownScopes(), ['all', 'chapters'], 'no scope with nothing in it');
  await type(p, 'vacuum');
  assert.deepEqual(shownScopes(), ['all', 'chapters', 'glossary', 'results', 'atlas']);
  click($(p, '.reader-scope[data-scope="glossary"]'));
  await type(p, 'lantern3');
  assert.deepEqual(shownScopes(), ['all', 'chapters', 'glossary'], 'the scope pressed stays, to be released');
  const g = $(p, '.reader-scope[data-scope="glossary"]');
  assert.equal(g.getAttribute('aria-pressed'), 'true');
  g.focus();
  key(g, 'ArrowRight');
  assert.equal(p.d.activeElement, $(p, '.reader-scope[data-scope="all"]'), 'arrows move among the scopes shown');
  noErrors(p);
});

test('narrow: a reference part is named as the page names it (its bar or contents link), in its scope, its results and the bar', async () => {
  const p = load({ book: { servedBar: true, barLinks: '<a class="mg-static" href="#results">Atlas and reference</a>' } });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'vacuum');
  assert.equal(text($(p, '.reader-scope[data-scope="results"] .reader-scope-label')), 'Atlas and reference');
  assert.equal(text($(p, '.reader-group[data-group="results"] .reader-group-where')), 'Atlas and reference');
  assert.equal(text($(p, '.reader-scope[data-scope="atlas"] .reader-scope-label')), 'Atlas', 'the contents link');
  key($(p, '#reader-q'), 'Escape');
  click($(p, '.reader-bar a.mg-static'));
  assert.equal(text($(p, '.reader-position-title')), 'Atlas and reference');
  noErrors(p);
});

test('narrow: each result says its kind; a section shows its first paragraph; its place keeps its formula', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'Second section of chapter 1');
  const sec = hitLinks(p).find(a => a.getAttribute('href') === '#ch01-s2');
  assert.ok(sec, 'the section is found');
  assert.equal(text(sec.querySelector('.reader-hit-kind')), 'Section');
  assert.match(text(sec.querySelector('.reader-hit-text')), /Theorem 1\.2|Proof words|paragraph without an address/, 'its first paragraph, as written');
  await type(p, 'Weaving1');
  const pas = hitLinks(p)[0];
  assert.equal(text(pas.querySelector('.reader-hit-kind')), 'Passage');
  assert.ok(pas.querySelector('.reader-hit-where math'), 'the section title keeps its formula');
  await type(p, 'zetanode');
  assert.equal(text(hitLinks(p)[0].querySelector('.reader-hit-kind')), 'Figure');
  noErrors(p);
});

test('narrow: an entry of a chapter\'s own contents is navigation, not a result; the section it names is, and every address stays as it was', async () => {
  const p = load();
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'First section of chapter 4');
  const hrefs = hitLinks(p).map(a => a.getAttribute('href'));
  assert.ok(hrefs.includes('#ch04-s1'), hrefs.join(' '));
  const targets = hrefs.map(h => p.d.getElementById(h.slice(1)));
  assert.ok(targets.every(t => !t.closest('.mg-ch-toc')), 'no result in the chapter\'s contents');
  const item = $(p, '#ch04 .mg-ch-toc li');
  assert.ok(item.id, 'the entry keeps its address');
  noErrors(p);
});

/* ---------------------------------------------------------------- the reference in companion pages */

async function buildIndex(o) {
  /* As the index tool does: each page's units as the reader builds them, addressed in that page. */
  const p = load({ book: Object.assign({}, o || {}) });
  await settle();
  const ev = new p.w.CustomEvent('qh:reader-units', { detail: {} });
  p.d.dispatchEvent(ev);
  const units = plain(ev.detail.units).map(x => Object.assign(x, { page: x.group === 'results' ? 'reference.html' : x.group === 'atlas' ? 'atlas.html' : 'book.html' }));
  noErrors(p);
  return { units };
}

test('search: introduction headings, mathematical passages and the separate opening keep their own destinations', async () => {
  const introduction = '<section class="mg-front-abstract" id="book-abstract"><h2 id="book-abstract-h"><span id="introduction">Introduction</span></h2>' +
    '<h3 id="opening-contours">What a contour measures</h3><p id="first-contour">What can that product put inside the contour?</p>' +
    '<nav><p>Navigation control words</p></nav><h3 id="opening-slice">A transverse slice</h3>' +
    '<div class="mg-display" id="opening-equation"><div class="math-display"><math><semantics><mi>x</mi><annotation encoding="application/x-tex">x</annotation></semantics></math></div></div></section>' +
    '<div class="mg-front-intro" id="opening-question" aria-label="The opening question"><p>Separate opening words.</p></div>';
  const index = await buildIndex({ introduction });
  const front = index.units.filter(x => x.groupKind === 'front');
  assert.equal(new Set(front.map(x => x.id)).size, front.length);
  assert.ok(front.some(x => x.id === 'introduction' && x.title === 'Introduction'));
  assert.ok(front.some(x => x.id === 'opening-contours' && x.kind === 'heading'));
  assert.ok(front.some(x => x.id === 'first-contour' && x.where === 'What a contour measures'));
  assert.ok(front.some(x => x.id === 'opening-equation' && x.tex === 'x' && x.where === 'A transverse slice'));
  assert.ok(front.every(x => !x.text.includes('Navigation control words')));
  const separate = front.find(x => x.text === 'Separate opening words.');
  assert.ok(separate && separate.id !== 'opening-question' && separate.where === 'The opening question');
  const local = load({ book: { introduction }, url: '#' + separate.id });
  await settle();
  assert.equal(text(local.d.getElementById(separate.id)), 'Separate opening words.');
  const remote = load({ html: companionPage({ companion: 'atlas' }), page: 'atlas.html', index });
  await settle();
  click($(remote, '.reader-search-toggle'));
  await type(remote, 'What can that product put inside the contour');
  const link = hitLinks(remote).find(a => a.getAttribute('href') === 'book.html#first-contour');
  assert.ok(link);
  click(link);
  assert.equal(remote.w.__left.at(-1).url, 'book.html#first-contour');
  noErrors(local); noErrors(remote);
});

test('index: the reader gives its units for the index, each with its address, place and words', async () => {
  const idx = await buildIndex();
  const byGroup = {};
  idx.units.forEach(x => { byGroup[x.group] = (byGroup[x.group] || 0) + 1; });
  assert.ok(byGroup.ch01 > 5 && byGroup.atlas === 40 && byGroup.results >= 2, JSON.stringify(byGroup));
  const ch = idx.units.find(x => x.id === 'ch03');
  assert.equal(ch.groupKind, 'chapter');
  assert.equal(ch.groupNumber, '3');
  assert.equal(ch.groupTitle, BOOK.chapters[2].title);
  const claim = idx.units.find(x => x.id === 'atlas-c-7');
  assert.equal(claim.title, 'Claim 7');
  assert.match(claim.text, /vacuum/);
});

test('environments: structural kinds and epistemic status travel with local and companion hits, including proof passages', async () => {
  const insert = [
    '<div id="cone" data-env="lemma" data-status="conditional" data-result data-kind="conditional">',
    '<p><span data-block-title>Finite descent lemma.</span> Cone construction.</p></div>',
    '<div id="factor" data-env="corollary" data-status="proved" data-result data-kind="theorem">',
    '<p><span data-block-title>Factorization corollary.</span> Unique factor.</p></div>',
    '<div id="argument" data-env="proof-sketch"><p><span data-block-title>Proof sketch.</span> Choose a generator.</p>',
    '<p>The determinant gives the final step.</p></div>'
  ].join('');
  const p = load({ html: book({ split: true, chapters: ['ch01'] }).replace('<p id="ch01-refs">', insert + '<p id="ch01-refs">') });
  const dump = new p.w.CustomEvent('qh:reader-units', { detail: {} });
  p.d.dispatchEvent(dump);
  const units = plain(dump.detail.units);
  const unit = id => units.filter(u => u.id === id);
  assert.deepEqual(unit('cone').map(u => [u.kind, u.env, u.status]), [['lemma', 'lemma', 'conditional']]);
  assert.deepEqual(unit('factor').map(u => [u.kind, u.env, u.status]), [['corollary', 'corollary', 'proved']]);
  assert.deepEqual(unit('argument').map(u => u.kind), ['proof-sketch']);
  assert.match(unit('argument-p2')[0].text, /determinant/);
  assert.equal(unit('argument')[0].text, 'Proof sketch.');
  const index = { units: units.map(u => Object.assign({ page: 'book.html' }, u)) };
  const remote = load({ page: 'reference.html', book: { companion: 'reference' }, index });
  for (const [page, prefix] of [[p, ''], [remote, 'book.html']]) {
    click($(page, '.reader-search-toggle'));
    await type(page, 'conditional lemma');
    const hit = hitLinks(page).find(a => a.getAttribute('href') === prefix + '#cone');
    assert.ok(hit);
    assert.equal(text(hit.querySelector('.reader-hit-kind')), 'Conditional lemma');
    assert.deepEqual([hit.dataset.hitEnv, hit.dataset.hitStatus], ['lemma', 'conditional']);
    assert.ok(hit.getAttribute('aria-labelledby').split(' ').every(id => page.d.getElementById(id)));
    await type(page, 'proved corollary');
    assert.ok(hitLinks(page).some(a => a.getAttribute('href') === prefix + '#factor'));
    await type(page, 'determinant');
    assert.ok(hitLinks(page).some(a => a.getAttribute('href') === prefix + '#argument-p2'));
    noErrors(page);
  }
});

test('environments: reference counterexamples retain witness addresses, and glossary and atlas units export their own forms', async () => {
  const example = '<div class="failure" id="counter" data-env="counterexample"><p class="claim">' +
    '<span class="claim-tag">Refuted form </span><span class="claim-text">All maps are invertible.</span></p>' +
    '<article id="witness" data-status="checked"><h4>A witness</h4><p>The kernel contains a generator.</p>' +
    '<p>The image vanishes.</p></article></div>';
  const markup = book({ tracker: true, chapters: ['ch01'], atlasUnits: 1 })
    .replace('<div class="statement" id="s-old-1">', example + '<div class="statement" id="s-old-1">')
    .replace('class="gloss" id="term-ox"', 'class="gloss" id="term-ox" data-env="definition"')
    .replace('id="atlas-c-1" data-qh-unit', 'id="atlas-c-1" data-env="proposition" data-qh-unit-status="conditional" data-qh-unit');
  function units(page) {
    const e = new page.w.CustomEvent('qh:reader-units', { detail: {} });
    page.d.dispatchEvent(e);
    return plain(e.detail.units);
  }
  const prior = units(load({ html: markup.replace('id="counter" data-env="counterexample"', 'id="counter"') }));
  const p = load({ html: markup });
  const current = units(p);
  const row = id => current.find(u => u.id === id);
  assert.deepEqual([row('counter').kind, row('counter').env, row('counter').status],
                   ['counterexample', 'counterexample', 'refuted-form']);
  assert.deepEqual([row('term-ox').kind, row('term-ox').env], ['gloss', 'definition']);
  assert.deepEqual([row('atlas-c-1').kind, row('atlas-c-1').env, row('atlas-c-1').status],
                   ['unit', 'proposition', 'conditional']);
  for (const sentence of ['The kernel contains a generator.', 'The image vanishes.']) {
    const was = prior.find(u => u.text === sentence);
    const witness = current.find(u => u.text === sentence);
    assert.ok(was && witness);
    assert.deepEqual([witness.id, witness.kind, witness.env, witness.status], [was.id, 'text', undefined, 'checked']);
  }
  click($(p, '.reader-search-toggle'));
  await type(p, 'kernel contains a generator');
  assert.ok(hitLinks(p).some(a => a.getAttribute('href') === '#' + current.find(u => u.text === 'The kernel contains a generator.').id));
  noErrors(p);
});

test('environments: a reference question sharing its card title has its own named search destination', async () => {
  const card = '<div class="question" id="q-actions"><header class="question-head">' +
    '<h3><a href="#q-actions">Actions beyond rooted models</a></h3></header><div class="question-ask">' +
    '<article class="statement" id="s-actions" data-env="open-question" data-status="open">' +
    '<p>Which other actions exist?</p><p>Fix the coefficient module.</p></article></div></div>';
  const namedCard = card.replaceAll('q-actions', 'q-other').replaceAll('s-actions', 's-own')
    .replace('<p>Which', '<h4 class="statement-title">A different question</h4><p>Which');
  const markup = book({ tracker: true, chapters: ['ch01'] }).replace('<div class="statement" id="s-old-1">',
    card + namedCard + '<div class="statement" id="s-old-1">');
  const p = load({ html: markup });
  const event = new p.w.CustomEvent('qh:reader-units', { detail: {} });
  p.d.dispatchEvent(event);
  const units = plain(event.detail.units);
  const rows = id => units.filter(u => u.id === id);
  assert.deepEqual(rows('s-actions').filter(u => u.kind === 'heading').map(u => [u.kind, u.env, u.status, u.title]),
    [['heading', 'open-question', 'open', 'Actions beyond rooted models']]);
  assert.deepEqual(rows('s-own').map(u => u.title), ['A different question']);
  assert.equal(rows('q-actions')[0].kind, 'heading');
  assert.equal(rows('s-actions-p1')[0].text, 'Which other actions exist?');
  click($(p, '.reader-search-toggle'));
  await type(p, 'open question rooted models');
  const hit = hitLinks(p).find(a => a.getAttribute('href') === '#s-actions');
  assert.ok(hit);
  assert.equal(text(hit.querySelector('.reader-hit-kind')), 'Open question');
  noErrors(p);
});

test('split: the book page holds only the book; an address of a companion page is forwarded there in place of this entry', async () => {
  const p = load({ url: '#s-old-1', book: { split: true } });
  await settle();
  assert.equal(p.d.querySelectorAll('[data-atlas-mount], #results').length, 0);
  assert.deepEqual(plain(p.w.__left), [{ url: 'reference.html#s-old-1', how: 'replace' }]);
  noErrors(p);
});

test('split: a link to a companion page leaves for it, and the entry left keeps the place for Back', async () => {
  const p = load({ url: '#ch04', book: { split: true } });
  await settle();
  click($(p, '.reader-contents-toggle'));
  const a = $(p, '#contents a[href="#atlas"]');
  a.focus();
  click(a);
  assert.deepEqual(plain(p.w.__left), [{ url: 'atlas.html#atlas', how: 'assign' }]);
  const st = p.w.history.state.reader;
  assert.equal(st.id.indexOf('ch04'), 0);
  assert.ok(st.focus, 'the control used is kept');
  noErrors(p);
});

test('split: the search reaches the companion pages through the index: chapters first, then the parts in the map\'s order', async () => {
  const index = await buildIndex({ atlasUnits: 300 });
  const p = load({ book: { split: true, atlasUnits: 300 }, index });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'vacuum');
  const groups = $$(p, '#reader-results .reader-group').map(g => g.getAttribute('data-group')).filter(g => g !== 'best');
  assert.deepEqual(groups, ['ch01', 'ch06', 'ch11', 'glossary', 'results', 'atlas']);
  const atlasLinks = [...$(p, '.reader-group[data-group="atlas"]').querySelectorAll('.reader-hit-link')];
  assert.equal(atlasLinks.length, 3);
  assert.match(atlasLinks[0].getAttribute('href'), /^atlas\.html#atlas-c-\d+$/);
  assert.equal(text($(p, '.reader-scope[data-scope="atlas"] .reader-scope-count')), '300');
  assert.equal(text($(p, '.reader-group[data-group="atlas"] .reader-group-where')), 'Atlas');
  noErrors(p);
});

test('split: a result in a companion page leaves for it with the search kept in the entry left; coming back reopens it on that result', async () => {
  const index = await buildIndex();
  const p = load({ url: '#ch02', book: { split: true }, index });
  await settle();
  click($(p, '.reader-search-toggle'));
  await type(p, 'Claim 17');
  const link = hitLinks(p).find(a => a.getAttribute('href') === 'atlas.html#atlas-c-17');
  assert.ok(link);
  click(link);
  assert.deepEqual(plain(p.w.__left), [{ url: 'atlas.html#atlas-c-17', how: 'assign' }]);
  const st = plain(p.w.history.state.reader);
  assert.equal(st.q, 'Claim 17');
  assert.equal(st.panel, 1);
  assert.equal(st.hit, 'atlas-c-17');
  assert.match(p.w.location.search, /q=Claim/);
  const back = load({ url: p.w.location.search + p.w.location.hash, book: { split: true }, index,
    before(w) { w.history.replaceState({ reader: st }, ''); } });
  await settle();
  await sleep(100);
  assert.equal($(back, '#reader-search').hidden, false);
  assert.equal(back.d.activeElement && back.d.activeElement.getAttribute('href'), 'atlas.html#atlas-c-17');
  noErrors(p); noErrors(back);
});

test('split: the index is loaded as a script when the search first opens, and its results join the list', async () => {
  const index = await buildIndex();
  const p = load({ book: { split: true } });
  await settle();
  click($(p, '.reader-search-toggle'));
  const sc = $(p, 'script[data-reader-index]');
  assert.ok(sc && sc.getAttribute('src') === 'reader-index.js', 'one script, from the map');
  await type(p, 'vacuum');
  assert.ok(!$(p, '.reader-group[data-group="atlas"]'), 'not before it has loaded');
  p.w.QH_READER_INDEX = index;
  sc.dispatchEvent(new p.w.Event('load'));
  await sleep(50);
  assert.ok($(p, '.reader-group[data-group="atlas"]'), 'the atlas results join');
  noErrors(p);
});

test('split: an index that cannot be loaded is said, and the book\'s own results remain', async () => {
  const p = load({ book: { split: true } });
  await settle();
  click($(p, '.reader-search-toggle'));
  $(p, 'script[data-reader-index]').dispatchEvent(new p.w.Event('error'));
  await type(p, 'vacuum');
  assert.match(text($(p, '#reader-search-status')), /could not be searched from here/);
  assert.ok(hitLinks(p).length > 0);
  noErrors(p);
});

test('companion: a companion page opens on its first part; its bar leads to the book\'s title page and back to the place last read', async () => {
  const p = load({ page: 'reference.html', book: { companion: 'reference' },
    storageSeed: { 'qh-reader-place': JSON.stringify({ id: 'ch08-s1', title: 'Chapter 8 · ' + BOOK.chapters[7].title + ' · 8.1 First section of chapter 8', at: 1 }) } });
  await settle();
  assert.deepEqual(shown(p), ['results']);
  assert.equal($(p, '.reader-home').getAttribute('href'), 'book.html#front');
  assert.equal(text($(p, '.reader-home')), BOOK.title);
  const ret = $(p, '.reader-prev');
  assert.equal(ret.hidden, false);
  assert.equal(ret.getAttribute('href'), 'book.html#ch08-s1');
  assert.match(ret.getAttribute('aria-label'), /^Back to the text: Chapter 8 · /);
  click($(p, '#s-old-1 a[href="#ch05"]'));
  assert.deepEqual(plain(p.w.__left), [{ url: 'book.html#ch05', how: 'assign' }]);
  click($(p, '#s-old-1 a[href="#atlas-c-2"]'));
  assert.deepEqual(plain(p.w.__left)[1], { url: 'atlas.html#atlas-c-2', how: 'assign' });
  noErrors(p);
});

test('companion: from the atlas page a link written to the book\'s page is followed as a change of page, keeping the place', async () => {
  const p = load({ page: 'atlas.html', url: '#atlas-c-3', book: { companion: 'atlas' } });
  await settle();
  assert.deepEqual(shown(p), ['atlas']);
  const out = $(p, '#atlas-c-3 a[href="book.html#ch05"]');
  click(out);
  assert.deepEqual(plain(p.w.__left), [{ url: 'https://example.org/book.html#ch05', how: 'assign' }]);
  noErrors(p);
});

/* ---------------------------------------------------------------- the built page (--page <file.html>)

   The same reading flow, checked on the page as built from the author's chapters: every served chapter by its
   address and in sequence, every in-page link resolved, reminders for the cross-references in running text, the search
   finding each chapter by its title and paragraphs by their own words, figures and equations by their ids, and the
   atlas kept out of the default view. It reads the page and changes nothing. */
async function pageChecks(file) {
  const html = fs.readFileSync(file, 'utf8');
  const results = [];
  const check = (name, ok, detail) => { results.push(ok); console.log((ok ? 'ok   ' : 'FAIL ') + name + (detail ? ' — ' + detail : '')); };
  const p = load({ html });
  await settle();
  const main = $(p, '[data-reader]');
  check('P1 the page has [data-reader] and the reader ran', !!main && main.hasAttribute('data-reader-on'));
  const chapters = $$(p, 'article[data-chapter]');
  check('P1 chapters served', chapters.length > 0, chapters.map(c => c.id).join(' '));
  const ids = $$(p, '[id]').map(e => e.id);
  const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
  check('P1 no duplicate id', dup.length === 0, [...new Set(dup)].slice(0, 10).join(' '));
  const badHead = chapters.filter(c => !p.d.getElementById(c.id + '-h'));
  check('P1 each chapter has its title as {id}-h', badHead.length === 0, badHead.map(c => c.id).join(' '));
  const event = new p.w.CustomEvent('qh:reader-units', { detail: {} });
  p.d.dispatchEvent(event);
  const unitsByAddress = new Map();
  for (const unit of event.detail.units) {
    if (!unitsByAddress.has(unit.id)) unitsByAddress.set(unit.id, []);
    unitsByAddress.get(unit.id).push(unit);
  }
  const declarations = $$(p, 'main .mg-env, main .mg-proof');
  const badDeclaration = declarations.filter(el => {
    const label = p.d.getElementById(el.getAttribute('aria-labelledby'));
    const place = el.closest('article[data-chapter], [data-reader-front]');
    const own = (unitsByAddress.get(el.id) || []).filter(u => u.group === (place && place.id));
    return !el.id || !el.dataset.env || el.getAttribute('role') !== 'group' || !label ||
      label.closest('[data-env]') !== el || !text(label) || own.length !== 1 ||
      own[0].kind !== el.dataset.env || own[0].env !== el.dataset.env ||
      (own[0].status || null) !== (el.dataset.status || null) || !own[0].title;
  });
  check('P1 every mathematical group has one named search entry with the same form, status and destination',
        declarations.length > 0 && badDeclaration.length === 0,
        declarations.length + ' declarations; mismatches ' + badDeclaration.map(el => el.id).join(' '));
  const eqs = $$(p, '[id^="eq-"]');
  const emptyEq = eqs.filter(e => !e.querySelector('math') && !text(e));
  check('P1 every equation id holds its formula (not an empty marker)', emptyEq.length === 0, `${eqs.length} equations; empty: ` + emptyEq.map(e => e.id).slice(0, 8).join(' '));
  const figs = $$(p, 'figure[data-figure]');
  const badFig = figs.filter(f => !f.id || !f.hasAttribute('data-qh-figure'));
  check('P1 figures carry their manifest id, data-figure and data-qh-figure', badFig.length === 0, `${figs.length} figures: ` + figs.map(f => f.id).join(' '));
  check('P2 a bare visit shows the title page, every place hidden', main.getAttribute('data-reader-view') === 'front' && shown(p).length === 0, shown(p).join(' '));
  const atlas = $(p, '[data-atlas-mount]');
  check('P2 the atlas is not in the default view', !atlas || atlas.hasAttribute('hidden'));

  /* the sequence: Begin, then Next through every served chapter */
  const order = [];
  const next = $(p, '.reader-bar .reader-next');
  for (let i = 0; i < chapters.length + 1 && !next.hidden; i++) { click(next); order.push(shown(p)[0]); }
  check('P3 Begin and Next go through every served chapter in order, one at a time', JSON.stringify(order) === JSON.stringify(chapters.map(c => c.id)), order.join(' '));
  const posOk = chapters.every(c => {
    click($(p, '.reader-home'));
    const a = $(p, `#contents a[href="#${c.id}"]`);
    if (!a) return false;
    click(a);
    return shown(p).length === 1 && shown(p)[0] === c.id && text($(p, '.reader-position-chapter')).includes(c.getAttribute('data-number'));
  });
  check('P3 each chapter from the contents shows alone with its number in the bar', posOk);
  const fused = chapters.filter(c => /^\d/.test(text(p.d.querySelector('.reader-position-title'))) && false);
  click($(p, '.reader-home'));
  const beginTitle = text($(p, '.reader-next .reader-step-title'));
  const ch1 = chapters[0];
  check('P3 the bar names the first chapter as "Chapter n · title", the number not repeated in the title',
        /^Chapter \d+ · \D/.test(beginTitle) && !new RegExp('· ' + ch1.getAttribute('data-number') + '\\D').test(beginTitle), beginTitle);

  /* links */
  const links = $$(p, 'main a[href^="#"]').filter(a => a.getAttribute('href').length > 1 && !a.closest('[data-atlas-mount]'));
  const unresolved = links.filter(a => !p.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))));
  check('P4 every in-page link outside the atlas resolves', unresolved.length === 0, `${links.length} links; unresolved: ` + [...new Set(unresolved.map(a => a.getAttribute('href')))].slice(0, 12).join(' '));

  /* reminders for the cross-references in running text */
  const runningLinks = links.filter(a => a.closest('article[data-chapter]') && !a.closest('nav, [data-chapter-kicker]') && a.getAttribute('data-ref') !== 'none');
  const refs = runningLinks.slice(0, 40);
  // Exercise both readings when an equation is also the destination of an authored definition.
  const definingEquations = new Set(refs.filter(a => a.hasAttribute('data-definition-use') && a.hash.startsWith('#eq-')).map(a => a.hash));
  for (const href of definingEquations) {
    const equationLink = runningLinks.find(a => a.hash === href && !a.hasAttribute('data-definition-use'));
    if (equationLink && !refs.includes(equationLink)) refs.push(equationLink);
  }
  let peeked = 0;
  const failedPeek = [];
  for (const a of refs) {
    const ch = a.closest('article[data-chapter]');
    if (shown(p)[0] !== ch.id) { click($(p, '.reader-home')); const go = $(p, `#contents a[href="#${ch.id}"]`); if (go) click(go); }
    click(a);
    const peek = $(p, '#reader-peek');
    const id = decodeURIComponent(a.getAttribute('href').slice(1));
    const body = peek.querySelector('.reader-peek-body');
    const target = p.d.getElementById(id);
    const go = peek.querySelector('.reader-peek-go');
    let ok = !peek.hidden && text(body).length > 0;
    if (a.hasAttribute('data-definition-use') && a.getAttribute('data-ref') === 'definition') {
      const preview = body.querySelector('.reader-define-text');
      ok = ok && peek.hasAttribute('data-term') && peek.getAttribute('data-kind') === 'definition'
        && preview && preview.textContent === a.getAttribute('data-definition-preview')
        && go && go.getAttribute('href') === a.getAttribute('href') && a.getAttribute('data-definition-target') === id
        && target && (!/^eq-/.test(id) || !!target.querySelector('math'));
    } else if (/^eq-/.test(id)) {
      ok = ok && !!body.querySelector('math');
    }
    if (ok) peeked++; else failedPeek.push(a.getAttribute('href'));
    key(p.d.activeElement || p.d.body, 'Escape');
  }
  check('P5 ordinary equation reminders show their formula and authored definitions show their exact preview and destination', failedPeek.length === 0, `${peeked} of ${refs.length}; failed: ` + failedPeek.slice(0, 8).join(' '));

  /* search */
  click($(p, '.reader-search-toggle'));
  const titleMiss = [];
  for (const c of chapters) {
    const h = p.d.getElementById(c.id + '-h');
    const n = c.getAttribute('data-number');
    const first = h.firstElementChild;
    await type(p, first && text(first) === n && h.children.length > 1 ? [...h.children].slice(1).map(text).join(' ') : text(h));
    const top = hitLinks(p).slice(0, 4).map(a => a.getAttribute('href'));
    if (!top.includes('#' + c.id)) titleMiss.push(c.id);
  }
  check('P6 each chapter is found by its title among the first results', titleMiss.length === 0, titleMiss.join(' '));
  const paras = chapters.flatMap(c => $$(p, `#${c.id} [data-section] > p`)).filter(x => text(x).split(' ').length > 12);
  const sample = paras.filter((_, i) => i % Math.max(1, Math.floor(paras.length / 20)) === 0).slice(0, 20);
  const missPara = [];
  for (const para of sample) {
    let phrase = '';
    const walker = p.d.createTreeWalker(para, 4);
    for (let n = walker.nextNode(); n && !phrase; n = walker.nextNode()) {
      if (n.parentNode.closest('math, svg, .math-display, button')) continue;
      const tokens = n.nodeValue.replace(/\s+/g, ' ').trim().split(' ');
      const at = tokens.findIndex((_, i) => tokens.slice(i, i + 4).length === 4 && tokens.slice(i, i + 4).every(w => /^[\p{L}\p{N}'-]+$/u.test(w)));
      if (at >= 0) phrase = tokens.slice(at, at + 4).join(' ');
    }
    if (!phrase) continue;
    await type(p, '"' + phrase + '"');
    const found = hitLinks(p).some(a => { const t = p.d.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))); return t && (t === para || t.contains(para) || para.contains(t)); });
    if (!found) missPara.push(phrase);
  }
  check('P6 paragraphs are found by their own words, as a phrase', missPara.length === 0, `${sample.length - missPara.length} of ${sample.length}; missed: ` + missPara.slice(0, 4).join(' | '));
  const groups = $$(p, '#reader-results .reader-group').map(g => g.getAttribute('data-group')).filter(g => g !== 'best');
  const firstRef = groups.findIndex(g => !/^ch\d+$/.test(g));
  const lastCh = groups.map(g => /^ch\d+$/.test(g)).lastIndexOf(true);
  check('P6 results list the chapters before the reference', firstRef < 0 || lastCh < firstRef, groups.join(' '));
  key($(p, '#reader-q'), 'Escape');
  check('P7 no script error', p.errors.length === 0, p.errors.slice(0, 3).join(' | '));
  const sec = $$(p, '[data-section][id]')[0] || null;
  const fresh = [sec && sec.id, figs[0] && figs[0].id, atlas && (atlas.querySelector('[data-qh-unit][id]') || atlas.querySelector('[id]') || atlas).id].filter(Boolean);
  while (opened.length) { try { opened.pop().window.close(); } catch (e) { /* closed */ } }

  /* a fresh visit by address: a section, a figure, an atlas place */
  for (const id of fresh) {
    const q = load({ html, url: '#' + id });
    await settle();
    const t = q.d.getElementById(id);
    const place = t && t.closest('article[data-chapter], section[data-reference]');
    check('P8 a fresh visit to #' + id + ' shows its place and reaches it', !!place && shown(q).join() === place.id && q.w.__scrolled.includes(t) && q.errors.length === 0, shown(q).join(' '));
    while (opened.length) { try { opened.pop().window.close(); } catch (e) { /* closed */ } }
    if (global.gc) global.gc();
  }
  const failed = results.filter(x => !x).length;
  console.log(`\n${results.length - failed} of ${results.length} checks passed on ${path.basename(file)}`);
  process.exit(failed ? 1 : 0);
}

/* ---------------------------------------------------------------- runner */

if (PAGE_FILE) pageChecks(PAGE_FILE);
else (async () => {
  let failed = 0;
  let ran = 0;
  for (const t of tests) {
    if (only && !t.name.includes(only)) continue;
    ran++;
    try {
      await t.fn();
      console.log('ok   ' + t.name);
    } catch (e) {
      failed++;
      console.log('FAIL ' + t.name + '\n     ' + String(e && e.stack || e).split("\n").slice(0, 14).join("\n     "));
    }
    while (opened.length) { try { opened.pop().window.close(); } catch (e) { /* closed */ } }
    if (global.gc) global.gc();
  }
  console.log(`\n${ran - failed} of ${ran} passed`);
  process.exit(failed ? 1 : 0);
})();
