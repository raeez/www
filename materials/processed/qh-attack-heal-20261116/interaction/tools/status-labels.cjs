#!/usr/bin/env node
/* Whether every place that names a status names it by the same words for the same stored code (jsdom, script running):

     NODE_PATH=<node_modules with jsdom> node status-labels.cjs <page.html> [<labels.json>]

   <labels.json> maps each stored code to its words ({"checked": "Established", ...}); by default the page's own status
   key gives the map (the item whose mark has the class mark-<code>). Places: a statement's status chip, a table mark's
   name and its scope card, a legend switch, a Show filter chip, a tally entry, a Status chip of the search, and the status
   key itself. Prints each disagreement and exits 1 when there is one. */
'use strict';
const fs = require('fs');
const { JSDOM, VirtualConsole } = require('jsdom');
const file = process.argv[2];
if (!file) { console.error('usage: status-labels.cjs <page.html> [<labels.json>]'); process.exit(2); }
const vc = new VirtualConsole();
const errors = [];
vc.on('jsdomError', e => { if (!/Not implemented: navigation/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
const dom = new JSDOM(fs.readFileSync(file, 'utf8'), { url: 'https://raeez.com/quantum-holography-tracker.html', runScripts: 'dangerously',
  pretendToBeVisual: true, virtualConsole: vc, beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
const norm = s => (s || '').replace(/\s+/g, ' ').trim();
function words(el) {                          /* the words of a control without its count or its mark */
  const c = el.cloneNode(true);
  c.querySelectorAll('.count, svg, .visually-hidden').forEach(n => n.remove());
  return norm(c.textContent);
}
const codeOf = cls => { const m = /(?:^|\s)mark-([\w-]+)/.exec(cls || ''); return m ? m[1].replace(/-/g, ' ') : null; };

setTimeout(() => {
  let map = null;
  if (process.argv[3]) map = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  else {
    map = {};
    d.querySelectorAll('.key-item').forEach(k => { const m = k.querySelector('.mark'); const c = m && codeOf(m.getAttribute('class')); if (c) map[c] = words(k.querySelector('dt') || k); });
  }
  const want = code => map[code] !== undefined ? map[code] : map[String(code).replace(/-/g, ' ')];
  const seen = {};
  const bad = [];
  function check(place, code, said) {
    if (!code) return;
    const expected = want(code);
    seen[place] = (seen[place] || 0) + 1;
    if (expected === undefined) bad.push(`${place}: the code "${code}" has no words in the key (said: "${said}")`);
    else if (said !== expected) bad.push(`${place} "${code}": says "${said}", the key says "${expected}"`);
  }
  d.querySelectorAll('main .statement[data-status] .status-chip').forEach(c => check('statement chip', c.closest('.statement').getAttribute('data-status'), words(c)));
  d.querySelectorAll('td.cell[data-status] .cell-btn').forEach(b => {
    const code = b.closest('td').getAttribute('data-status');
    const name = b.getAttribute('aria-label') || '';
    check('mark name', code, name.slice(name.lastIndexOf(': ') + 2));
    const head = b.closest('td').querySelector('.cell-note-head > span:not(.cell-note-where)');
    if (head) check('mark scope card', code, words(head));
  });
  d.querySelectorAll('.legend .lens[data-lens]').forEach(b => check('legend switch', b.getAttribute('data-lens'), words(b)));
  d.querySelectorAll('.row-tools .filter[data-filter]').forEach(b => check('Show filter chip', b.getAttribute('data-filter'), words(b)));
  d.querySelectorAll('.tally a[data-filter]').forEach(a => check('tally entry', a.getAttribute('data-filter'), words(a.querySelector('.count-label') || a)));
  d.querySelectorAll('.find .filter[data-status-facet]').forEach(b => check('search Status chip', b.getAttribute('data-status-facet'), words(b)));
  console.log('codes and words:', JSON.stringify(map));
  console.log('places checked:', JSON.stringify(seen));
  if (errors.length) console.log('script errors:', errors.join(' | '));
  const tally = {};
  bad.forEach(x => { tally[x] = (tally[x] || 0) + 1; });
  Object.keys(tally).sort((a, b) => tally[b] - tally[a]).forEach(x => console.log('  ' + String(tally[x]).padStart(4) + ' x ' + x));
  console.log('summary:', bad.length || errors.length ? `${bad.length} disagreement(s)${errors.length ? ', ' + errors.length + ' script error(s)' : ''}` : 'PASS');
  w.close();
  process.exit(bad.length || errors.length ? 1 : 0);
}, 400);
