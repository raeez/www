// WCAG 2.1 contrast of rendered text (and marks) against the background behind it, in both schemes.
//   node tools/run.mjs tools/contrast.mjs <page.html>
import { fileUrl } from './cdp.mjs';

const PROBES = [
  ['body', 'body text'], ['.kicker', 'kicker'], ['.subtitle', 'subtitle'], ['.as-of', 'as of'],
  ['.contents-title', 'contents title'], ['.contents-holds', 'contents counts'], ['.contents-label', 'contents label'],
  ['.tally a', 'tally'], ['.find-hint', 'search hint'], ['.status-chip', 'status chip'],
  ['.statement-text p', 'statement text'], ['.statement-notes', 'statement notes'], ['.note-label', 'note label'],
  ['.question-num', 'question number'], ['.question-ask-label', 'question part label'], ['.question-why', 'why text'],
  ['.known-label', 'known label'], ['.row-count', 'counts'], ['.fold-title', 'related line title'],
  ['.fold-status', 'related line status'], ['.q-index-cap', 'index caption'], ['.q-index-num', 'index number'],
  ['.col-head', 'column heading'], ['.grid tbody th a', 'family name'], ['.grid-hint', 'grid hint'], ['.legend', 'legend'],
  ['.legend-key a', 'legend link'], ['.row-num', 'row number'], ['.cell-st', 'cell status'], ['.cell-body', 'cell scope'],
  ['.claim-text', 'false claim'], ['.essay-byline', 'essay byline'], ['.gloss dd', 'definition'], ['.gloss-index a', 'letter link'],
  ['.nav a', 'bar link'], ['.foot', 'footer'], ['.filters-label', 'filter label'],
  ['.mark-checked', 'mark checked', 'mark'], ['.mark-open', 'mark open', 'mark'], ['.mark-partial', 'mark partial', 'mark'],
  ['.mark-not-posed', 'mark not posed', 'mark'], ['.mark-conditional', 'mark conditional', 'mark'], ['.mark-published', 'mark published', 'mark'],
  ['.mark-refuted-form', 'mark refuted', 'mark'],
];

const EXPR = (probes) => `(() => {
  const parse = (c) => { const m = c.match(/rgba?\\(([^)]+)\\)/); if (!m) return null; const v = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r: v[0], g: v[1], b: v[2], a: v.length > 3 ? v[3] : 1 }; };
  const lum = (c) => { const f = (x) => { x /= 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
  const over = (top, bot) => ({ r: top.r * top.a + bot.r * (1 - top.a), g: top.g * top.a + bot.g * (1 - top.a), b: top.b * top.a + bot.b * (1 - top.a), a: 1 });
  const bgOf = (el) => { const layers = []; for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } }
    let base = { r: 255, g: 255, b: 255, a: 1 }; for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base); return base; };
  return ${JSON.stringify(probes)}.map(([sel, name, kind]) => {
    const el = [...document.querySelectorAll(sel)].find((e) => e.getClientRects().length);
    if (!el) return { name, missing: true };
    const cs = getComputedStyle(el); const fg = parse(cs.color); const bg = bgOf(el);
    const L1 = lum(over(fg, bg)), L2 = lum(bg); const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    const size = parseFloat(cs.fontSize), bold = +cs.fontWeight >= 600; const large = size >= 24 || (bold && size >= 18.66);
    const need = kind === 'mark' ? 3 : large ? 3 : 4.5;
    return { name, ratio: Math.round(ratio * 100) / 100, need, pass: ratio >= need, size: Math.round(size * 10) / 10 };
  });
})()`;

export default async function (b, [pagePath]) {
  const out = {};
  for (const scheme of ['light', 'dark']) {
    const p = await b.page({ width: 1400, height: 900, scheme });
    await p.goto(fileUrl(pagePath), 500);
    await p.eval(`document.querySelectorAll('details.row, details.fold, details.col-defs').forEach(d => d.open = true)`);
    out[scheme] = await p.eval(EXPR(PROBES));
    await p.close();
  }
  return out;
}
