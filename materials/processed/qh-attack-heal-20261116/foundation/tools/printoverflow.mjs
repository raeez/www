// Formulas wider than their column or the page under print media, every disclosure open.
//   node tools/run.mjs tools/printoverflow.mjs <page.html> [widths=673,695,438]
// 673 and 695 px are the A4 and Letter page areas inside 16mm margins; 438 px is A5.
import { fileUrl } from './cdp.mjs';

export default async function (b, [pagePath, widths = '673,695,438']) {
  const out = {};
  for (const w of widths.split(',')) {
    const p = await b.page({ width: +w, height: 1000, scheme: 'light', media: 'print' });
    await p.goto(fileUrl(pagePath), 500);
    out[w] = await p.eval(`(() => { document.querySelectorAll('main details').forEach(d => d.open = true);
      const page = document.documentElement.clientWidth; const bad = [];
      for (const box of document.querySelectorAll('main .math-display, main .math-long')) {
        const m = box.querySelector('math'); if (!m) continue;
        const rr = m.getBoundingClientRect();
        // A display formula's <math> box is as wide as its column; its content can be wider (scrollWidth).
        let right = rr.left + Math.max(rr.width, m.scrollWidth);
        for (const k of m.querySelectorAll('semantics > *:first-child')) right = Math.max(right, k.getBoundingClientRect().right);
        const r = { right, width: right - rr.left };
        // The column the formula sits in: the nearest block that is a statement, a glossary entry, a cell line or a paragraph.
        const col = box.closest('.gloss, .statement, .cell-line, .question-why, .row-summary, .lead, .essay, .claim, dd, p') || box.parentElement;
        const c = col.getBoundingClientRect();
        if (r.right > c.right + 1 || r.right > page + 1) bad.push({ where: (box.closest('[id]') || {}).id, right: Math.round(r.right), col: Math.round(c.right), page,
          width: Math.round(r.width), beyondPage: r.right > page + 1 });
      }
      return { count: bad.length, beyondPage: bad.filter(x => x.beyondPage).length, sample: bad.slice(0, 12) }; })()`);
    await p.close();
  }
  return out;
}
