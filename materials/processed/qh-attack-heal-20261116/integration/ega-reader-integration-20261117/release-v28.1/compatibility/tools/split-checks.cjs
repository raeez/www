#!/usr/bin/env node
/* Checks of a book split into companion pages (tools/split-reference.py), on the pages themselves, in jsdom:

       NODE_PATH=<jsdom> node --max-old-space-size=8192 --expose-gc tools/split-checks.cjs <dir> <book page name>

   S1 the book page: the reference parts are not in it; an old reference address is forwarded to its page in place of
      the entry; the search, with the index, lists the chapters first and then the parts of the other pages, whose
      results lead to those pages.
   S2 reference.html: an old address shows its part; a term served as a button opens its card (status.js beside the
      reader); the bar leads back to the book.
   S3 atlas.html: a claim's address shows the atlas; its links to the book leave for the book.
   Every page: no script error. Reads the pages; writes nothing. */
'use strict';
const fs = require('fs');
const path = require('path');
const { JSDOM, VirtualConsole } = require('jsdom');
const [dir, bookName] = process.argv.slice(2);
if (!dir || !bookName) { console.error('usage: split-checks.cjs <dir> <book page name>'); process.exit(2); }
const results = [];
const check = (name, ok, detail) => { results.push(!!ok); console.log((ok ? 'ok   ' : 'FAIL ') + name + (detail ? ' — ' + detail : '')); };
const sleep = ms => new Promise(r => setTimeout(r, ms));
const text = el => (el ? el.textContent : '').replace(/\s+/g, ' ').trim();
function load(name, hash, opts) {
  opts = opts || {};
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
  let html = fs.readFileSync(path.join(dir, name), 'utf8');
  if (opts.inlineIndex) html = html.replace('<script type="application/json" id="reader-pages">', '<script>' + fs.readFileSync(path.join(dir, 'reader-index.js'), 'utf8') + '</script><script type="application/json" id="reader-pages">');
  const dom = new JSDOM(html, {
    url: 'https://example.org/' + name + (hash || ''), runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) {
      w.__scrolled = [];
      w.Element.prototype.scrollIntoView = function () { w.__scrolled.push(this); };
      w.scrollTo = function () {};
      w.__left = [];
      w.addEventListener('qh:leave', e => { w.__left.push(JSON.parse(JSON.stringify(e.detail))); e.preventDefault(); }, true);
    }
  });
  return { dom, w: dom.window, d: dom.window.document, errors };
}
const shown = p => [...p.d.querySelectorAll('main article[data-chapter], main section[data-reference]')].filter(e => !e.hasAttribute('hidden')).map(e => e.id);
function close(p) { try { p.w.close(); } catch (e) { /* closed */ } if (global.gc) global.gc(); }
(async () => {
  const map = JSON.parse(fs.readFileSync(path.join(dir, bookName), 'utf8').match(/<script type="application\/json" id="reader-pages">(.*?)<\/script>/s)[1]);
  const ref = map.pages.find(p => p.href === 'reference.html');
  const atl = map.pages.find(p => p.href === 'atlas.html');
  const oldId = ref.ids.find(i => /^s-/.test(i)) || ref.ids[0];
  const claim = atl.ids.find(i => /^atlas-c-/.test(i));

  /* S1 the book page */
  let p = load(bookName, '#' + oldId);
  await sleep(150);
  check('S1 the book page holds no reference part that was moved', !p.d.querySelector('[data-atlas-mount]') && !p.d.getElementById(oldId));
  check('S1 an old reference address on the book is forwarded to its page in place of the entry',
        JSON.stringify(p.w.__left) === JSON.stringify([{ url: 'reference.html#' + encodeURIComponent(oldId), how: 'replace' }]), JSON.stringify(p.w.__left));
  check('S1 no script error', !p.errors.length, p.errors.slice(0, 2).join(' | '));
  close(p);
  p = load(bookName, '', { inlineIndex: true });
  await sleep(150);
  p.d.querySelector('.reader-search-toggle').click();
  const q = p.d.getElementById('reader-q');
  q.value = 'vacuum';
  q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(400);
  const groups = [...p.d.querySelectorAll('#reader-results .reader-group')].map(g => g.getAttribute('data-group')).filter(g => g !== 'best');
  const firstRef = groups.findIndex(g => !/^ch\d+$/.test(g));
  const lastCh = groups.map(g => /^ch\d+$/.test(g)).lastIndexOf(true);
  check('S1 the search lists the chapters, then the parts of the other pages', firstRef > 0 && lastCh < firstRef && groups.includes('atlas'), groups.join(' '));
  const remote = [...p.d.querySelectorAll('#reader-results .reader-hit-link')].map(a => a.getAttribute('href')).filter(h => /^(reference|atlas)\.html#/.test(h));
  check('S1 results in the other pages lead to them', remote.length > 0, remote.slice(0, 3).join(' '));
  check('S1 no script error with the search', !p.errors.length, p.errors.slice(0, 2).join(' | '));
  close(p);

  /* S2 reference.html */
  p = load('reference.html', '#' + oldId);
  await sleep(150);
  const part = p.d.getElementById(oldId) && p.d.getElementById(oldId).closest('section[data-reference]');
  check('S2 an old address shows its part and reaches it', part && shown(p).join() === part.id && p.w.__scrolled.includes(p.d.getElementById(oldId)), shown(p).join(' '));
  const termPart = p.d.querySelector('button.term[data-term]') && p.d.querySelector('button.term[data-term]').closest('section[data-reference]');
  if (termPart) {
    p.d.querySelector('.reader-contents-toggle');
    const go = new p.w.CustomEvent('qh:navigate', { bubbles: true, cancelable: true, detail: { id: termPart.id } });
    p.d.dispatchEvent(go);
    p.d.querySelector('#' + termPart.id + ' button.term[data-term]').click();
    const card = p.d.getElementById('card');
    check('S2 a term served as a button opens its card (status.js beside the reader)', card && !card.hidden && text(card).length > 0, termPart.id);
  }
  const home = p.d.querySelector('.reader-home');
  check('S2 the bar leads to the book', home && home.getAttribute('href') === bookName + '#front', home && home.getAttribute('href'));
  check('S2 no script error', !p.errors.length, p.errors.slice(0, 2).join(' | '));
  close(p);

  /* S3 atlas.html */
  p = load('atlas.html', '#' + claim);
  await sleep(300);
  check('S3 a claim\'s address shows the atlas', shown(p).join() === 'atlas', shown(p).join(' '));
  const toBook = [...p.d.querySelectorAll('#atlas a[href^="' + bookName + '#"]')][0];
  if (toBook) {
    toBook.click();
    check('S3 a link to the book leaves for the book', p.w.__left.length === 1 && p.w.__left[0].url.indexOf(bookName + '#') >= 0, JSON.stringify(p.w.__left));
  }
  check('S3 no script error', !p.errors.length, p.errors.slice(0, 2).join(' | '));
  close(p);
  const failed = results.filter(x => !x).length;
  console.log(`\n${results.length - failed} of ${results.length} checks passed`);
  process.exit(failed ? 1 : 0);
})();
