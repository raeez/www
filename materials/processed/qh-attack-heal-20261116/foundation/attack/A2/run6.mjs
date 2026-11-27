// Run 6: in print media at the A4/Letter content widths, which boxes (MathML descendants included) reach past the page area?
import { writeFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const R = { steps: {} };
const save = () => writeFileSync(S + '/run6.json', JSON.stringify(R, null, 1));
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 300000);
const frame = `() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 80))))`;
const SCAN = `(marginMm) => { const vw = document.documentElement.clientWidth; const m = marginMm * 96 / 25.4; const hits = new Map();
  for (const el of document.querySelectorAll('body *')) { const r = el.getBoundingClientRect(); if (!r.width && !r.height) continue;
    if (r.right <= vw + 0.5 && r.left >= -0.5) continue; if (!el.checkVisibility()) continue;
    const host = el.closest('.math-display, .math-long, .grid-wrap, .statement, .question, .section, .foot, body') || el;
    const key = host; const prev = hits.get(key) || { host: __a2.d(host).slice(0, 60), right: -1e9, left: 1e9, tex: '', sid: (el.closest('[id]') || {}).id || null, leaf: '' };
    if (r.right > prev.right) { prev.right = Math.round(r.right); prev.leaf = __a2.d(el).slice(0, 50); }
    prev.left = Math.min(prev.left, Math.round(r.left)); const ann = host.querySelector && host.querySelector('annotation'); if (ann) prev.tex = ann.textContent.slice(0, 140); hits.set(key, prev); }
  const list = [...hits.values()].sort((a, b) => b.right - a.right);
  return { contentWidthPx: vw, marginPx: Math.round(m), scrollWidth: document.documentElement.scrollWidth, count: list.length, beyondPaper: list.filter(h => h.right > vw + m || h.left < -m).length, list: list.slice(0, 15) }; }`;
try {
  const p = await page(b);
  await p.size(1400, 900); await p.go('file://' + P); await p.ev(INSTALL);
  await p.media('print', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.ev(`() => { document.querySelectorAll('main details').forEach(d => d.open = true); return true; }`);
  await p.size(673, 950); await p.ev(frame); await p.ev(frame);
  R.steps.a4 = await p.ev(SCAN, 16); save();
  await p.size(695, 950); await p.ev(frame); await p.ev(frame);
  R.steps.letter = await p.ev(SCAN, 16); save();
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
