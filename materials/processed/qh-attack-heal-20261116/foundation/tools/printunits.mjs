// Print completeness: every research unit present in the PDF text, status chips counted by status,
// near-empty pages, on A4, Letter and two stress sizes (Legal, A5).
//   node tools/run.mjs tools/printunits.mjs <page.html> <outdir> [papers=A4,Letter,Legal,A5]
// A unit probe is a 28-character run from the middle of the unit's longest text segment outside
// formulae, so that text next to a formula (extracted out of order) does not cause a false miss.
import { execFileSync } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileUrl } from './cdp.mjs';

const SIZES = { A4: [8.27, 11.69], Letter: [8.5, 11], Legal: [8.5, 14], A5: [5.83, 8.27] };
const norm = (s) => s.normalize('NFKC').replace(/[\s­‐‑-]+/g, '').toLowerCase();

const PROBES = `(() => {
  const units = [];
  const probe = (el) => {
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (n) =>
      n.parentElement.closest('math, .statement-context, .visually-hidden') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
    let best = ''; for (let n = w.nextNode(); n; n = w.nextNode()) { const t = n.nodeValue.replace(/\\s+/g, ' ').trim(); if (t.length > best.length) best = t; }
    if (best.length < 14) return null;
    const words = best.split(' '); const mid = words.length > 6 ? words.slice(2).join(' ') : best;
    return mid.slice(0, 28);
  };
  const add = (kind, sel) => document.querySelectorAll(sel).forEach((el) => { const p = probe(el); if (p) units.push([kind, p, (el.closest('[id]') || {}).id || '']); });
  add('statement', 'main .statement-text');
  add('why', 'main .question-why');
  add('row-summary', 'main .row-summary');
  add('cell-line', 'main .cell-line .cell-text');
  add('claim', 'main .claim-text');
  add('definition', 'main .gloss dd');
  add('lead', 'main .lead p');
  add('essay', 'main .essay > p');
  return units;
})()`;

export default async function (b, [pagePath, outdir, papers = 'A4,Letter,Legal,A5']) {
  mkdirSync(outdir, { recursive: true });
  const out = { runs: [] };
  for (const paper of papers.split(',')) {
    const p = await b.page({ width: 1200, height: 900, scheme: 'light' });
    await p.goto(fileUrl(pagePath), 500);
    const units = await p.eval(PROBES);
    const expected = await p.eval(`(() => { const c = {}; document.querySelectorAll('main article.statement').forEach(s => { const k = s.getAttribute('data-status'); c[k] = (c[k] || 0) + 1; }); return c; })()`);
    const labels = await p.eval(`(() => { const m = {}; document.querySelectorAll('main article.statement .status-chip').forEach(c => { m[c.closest('article').getAttribute('data-status')] = c.textContent.trim().toUpperCase(); }); return m; })()`);
    const [w, h] = SIZES[paper];
    const path = resolve(outdir, `${paper}.pdf`);
    const { data } = await p.s('Page.printToPDF', { paperWidth: w, paperHeight: h, preferCSSPageSize: false, printBackground: false,
      displayHeaderFooter: false, marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0 });
    (await import('node:fs')).writeFileSync(path, Buffer.from(data, 'base64'));
    const text = execFileSync('pdftotext', ['-enc', 'UTF-8', path, '-']).toString();
    const hay = norm(text);
    const missing = units.filter(([, t]) => !hay.includes(norm(t)));
    const chips = {};
    for (const [st, label] of Object.entries(labels)) {
      chips[st] = (text.match(new RegExp(label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g')) || []).length;
    }
    const pages = text.split('\f').slice(0, -1);
    const blank = pages.map((pg, i) => [i + 1, pg.trim().length]).filter(([, n]) => n < 200).map(([i]) => i);
    out.runs.push({ paper, pages: pages.length, units: units.length, missing: missing.length, missingSample: missing.slice(0, 6),
                    chips, expected, chipsComplete: Object.keys(expected).every((k) => chips[k] >= expected[k]), blankPages: blank,
                    console: p.log.slice() });
    await p.close();
  }
  return out;
}
