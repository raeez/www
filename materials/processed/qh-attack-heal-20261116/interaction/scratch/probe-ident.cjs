const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const py = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const d = new JSDOM(html).window.document;
function rawText(el) {           /* text as written in the source: formulae by their TeX */
  let out = '';
  (function walk(n) {
    if (n.nodeType === 3) { out += n.nodeValue; return; }
    if (n.nodeType !== 1) return;
    if (n.localName === 'math') { const a = n.querySelector('annotation'); out += a ? a.textContent : ''; return; }
    for (let c = n.firstChild; c; c = c.nextSibling) walk(c);
  })(el);
  return out;
}
function ident(text) {
  let t = text.normalize('NFKD').replace(/[^\x00-\x7f]/g, '');
  t = t.replace(/[^A-Za-z0-9_\s-]/g, '').trim().toLowerCase();
  return t.replace(/[\s_-]+/g, '-').slice(0, 60) || 'x';
}
const ids = new Set([...d.querySelectorAll('[id]')].map(e => e.id));
const stmts = [...d.querySelectorAll('main .statement')];
let i = 0, mismatch = 0, collide = 0, noTitle = 0;
const noid = py.filter(x => !x.id);
const domNoid = stmts.filter(s => !s.id);
console.log('dom statements', stmts.length, 'dom without id', domNoid.length, 'py without id', noid.length);
domNoid.forEach((s, k) => {
  const t = s.querySelector('.statement-title');
  if (!t) { noTitle++; return; }
  const js = ident(rawText(t));
  const p = noid[k] && noid[k].slug;
  if (js !== p) { mismatch++; console.log('MISMATCH', JSON.stringify(rawText(t)), js, p); }
  if (ids.has('s-' + js)) { collide++; console.log('COLLIDE', js); }
});
console.log({ mismatch, collide, noTitle });
