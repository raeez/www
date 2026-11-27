// Print one page variant to Letter and A4 and report whether every decisive/frontier card's texts are present.
//   node tools/run.mjs tools/q5check.mjs <page.html> <outdir>
import { execFileSync } from 'node:child_process';
import { resolve } from 'node:path';
import { fileUrl } from './cdp.mjs';
const norm = (s) => s.normalize('NFKC').replace(/[\s­‐‑-]+/g, '').toLowerCase();
export default async function (b, [pagePath, outdir]) {
  const res = {};
  for (const paper of ['Letter', 'A4']) {
    const p = await b.page({ width: 1200, height: 900, scheme: 'light' });
    await p.goto(fileUrl(pagePath), 500);
    // Probe: the first 40 characters (without formulae) of every statement text on the page.
    const probes = await p.eval(`[...document.querySelectorAll('main .statement-text')].map(e => {
      const w = document.createTreeWalker(e, NodeFilter.SHOW_TEXT, { acceptNode: (n) => n.parentElement.closest('math') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
      let best = ''; for (let n = w.nextNode(); n; n = w.nextNode()) { const t = n.nodeValue.replace(/\\s+/g, ' ').trim(); if (t.length > best.length) best = t; }
      return best.slice(0, 36); }).filter(t => t.length >= 16)`);
    const path = resolve(outdir, `${paper}.pdf`);
    await p.pdf(path, { paper });
    const text = norm(execFileSync('pdftotext', ['-enc', 'UTF-8', path, '-']).toString());
    const pages = +(execFileSync('pdfinfo', [path]).toString().match(/Pages:\s+(\d+)/) || [0, 0])[1];
    const missing = probes.filter((t) => !text.includes(norm(t)));
    res[paper] = { pages, probes: probes.length, missing: missing.length, sample: missing.slice(0, 4) };
    await p.close();
  }
  return res;
}
