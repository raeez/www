// The status-language ruling on a built page: every place that names a status shows the label chosen by its stored
// code (cards, grid cells and their accessible names, legend, key, filters, tally, fold lines), and no other label.
// Usage: QH_JSDOM=<jsdom> node qh-status-language.mjs --html <page> [--out <json>]   Reads only; writes only --out.
import fs from 'node:fs';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { JSDOM } = require(process.env.QH_JSDOM || 'jsdom');
const args = {};
for (let i = 2; i < process.argv.length; i += 2) args[process.argv[i].replace(/^--/, '')] = process.argv[i + 1];
const LABEL = { 'checked': 'Established', 'conditional': 'Conditional', 'open': 'Remaining', 'refuted form': 'Scoped negative',
                'published': 'Published', 'partial': 'Partial', 'not posed': 'Not posed', 'pending': 'Proposed' };
const OLD = ['Proved and independently checked', 'Open problem', 'Partly established', 'Not yet formulated', 'Refuted as first posed'];
const slugToCode = Object.fromEntries(Object.keys(LABEL).map(c => [c.replace(/ /g, '-'), c]));
const doc = new JSDOM(fs.readFileSync(args.html, 'utf8')).window.document;
const t = el => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
const codeOfMark = el => { const m = el && el.querySelector('svg.mark'); const k = m && [...m.classList].find(x => x.startsWith('mark-')); return k ? slugToCode[k.slice(5)] : null; };
const seen = [], problems = [];
function expect(where, code, label) {
  seen.push(where);
  if (!(code in LABEL)) return;
  if (label !== LABEL[code]) problems.push({ where, code, label, want: LABEL[code] });
}
doc.querySelectorAll('main article.statement[data-status]').forEach(a => expect('card chip', a.getAttribute('data-status'), t(a.querySelector('.status-chip'))));
doc.querySelectorAll('td[data-status] .cell-btn').forEach(b => { const al = b.getAttribute('aria-label') || ''; expect('grid cell name', b.closest('td').getAttribute('data-status'), al.slice(al.lastIndexOf(': ') + 2)); });
doc.querySelectorAll('td[data-status] .cell-st, .cell-line .cell-st').forEach(s => { const host = s.closest('[data-status]') || s.closest('.cell-line'); const code = host && host.getAttribute('data-status') || codeOfMark(s.closest('.cell-line')); expect('cell text', code, t(s)); });
doc.querySelectorAll('.legend li').forEach(li => expect('legend', codeOfMark(li), t(li)));
doc.querySelectorAll('.key-item dt').forEach(dt => expect('key', codeOfMark(dt), t(dt)));
doc.querySelectorAll('.row-tools .filter[data-filter]').forEach(b => expect('filter', b.getAttribute('data-filter'), t(b)));
doc.querySelectorAll('.tally a[data-filter]').forEach(a => expect('tally', a.getAttribute('data-filter'), t(a.querySelector('.count-label'))));
doc.querySelectorAll('details.fold > summary').forEach(s => expect('fold line', codeOfMark(s), t(s.querySelector('.fold-status'))));
// No old label anywhere a reader sees or hears (the section heading "Open problems" is a section name, not a status).
const visible = doc.body.textContent.replace(/\s+/g, ' ');
const names = [...doc.querySelectorAll('[aria-label],[title]')].map(e => (e.getAttribute('aria-label') || '') + ' | ' + (e.getAttribute('title') || '')).join(' ');
const leftovers = OLD.map(o => ({ label: o, visible: (visible.match(new RegExp(o + '(?!s)', 'g')) || []).length, names: (names.match(new RegExp(o + '(?!s)', 'g')) || []).length }))
  .filter(x => x.visible || x.names);
const counts = seen.reduce((m, w) => (m[w] = (m[w] || 0) + 1, m), {});
const ok = problems.length === 0 && leftovers.length === 0;
console.log(ok ? 'PASS' : 'FAIL', JSON.stringify({ checked: counts, problems: problems.slice(0, 10), problem_count: problems.length, leftovers }));
if (args.out) fs.writeFileSync(args.out, JSON.stringify({ html: args.html, pass: ok, checked: counts, problems, leftovers }, null, 1) + '\n');
