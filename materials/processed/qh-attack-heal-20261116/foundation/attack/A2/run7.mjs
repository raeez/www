// Run 7: line length of decisive questions at 1024 and 1400; chip overflow at 375; real Escape on a trivial page.
import { writeFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const R = { steps: {} };
const save = () => writeFileSync(S + '/run7.json', JSON.stringify(R, null, 1));
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 200000);
const frame = `() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 80))))`;
const CPL = `() => { const lines = (p) => { const rg = document.createRange(); rg.selectNodeContents(p); const rects = [...rg.getClientRects()]; const tops = [...new Set(rects.map(r => Math.round(r.top)))]; return tops.length; };
  const meas = (sel) => { const ps = [...document.querySelectorAll(sel)].filter(p => p.checkVisibility()).slice(0, 12); let chars = 0, ln = 0, w = 0;
    for (const p of ps) { chars += p.textContent.replace(/\\s+/g, ' ').trim().length; ln += lines(p); w = Math.max(w, p.getBoundingClientRect().width); } return { paragraphs: ps.length, widthPx: Math.round(w), avgCharsPerLine: Math.round(chars / Math.max(1, ln)) }; };
  return { decisiveAsk: meas('.question.compare .question-ask .statement-text p'), decisiveWhy: meas('.question.compare .question-why p'), principal: meas('#results .statement-text p'), lead: meas('.lead p') }; }`;
try {
  const p = await page(b);
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  for (const w of [1024, 1400]) { await p.size(w, 900); if (w === 1024) { await p.go('file://' + P); await p.ev(INSTALL); } else await p.ev(frame); R.steps['cpl' + w] = await p.ev(CPL); save(); }
  await p.size(375, 812); await p.ev(frame);
  R.steps.chipOverflow375 = await p.ev(`() => { const out = []; for (const c of document.querySelectorAll('.status-chip')) { if (!c.checkVisibility()) continue; const s = c.closest('.statement'); const r = c.getBoundingClientRect(), q = s.getBoundingClientRect();
      if (r.right > q.right - 1) out.push({ id: s.id || null, where: (s.closest('.failure') ? 'failure' : s.closest('.question-known') ? 'decisive known' : s.closest('.question-ask') ? 'decisive ask' : s.closest('.question') ? 'frontier' : s.closest('.principal') ? 'principal' : 'other'), chipRight: Math.round(r.right), cardRight: Math.round(q.right) }); }
      return { count: out.length, byWhere: out.reduce((a, o) => (a[o.where] = (a[o.where] || 0) + 1, a), {}), sample: out.slice(0, 5) }; }`);
  await p.go('data:text/html,<p>escape test</p>');
  const t0 = Date.now(); await p.key('Escape'); R.steps.escapeTrivialPage = { keyMs: Date.now() - t0 };
  try { await p.ev(frame); R.steps.escapeTrivialPage.frameAfterEscape = 'ran'; } catch (e) { R.steps.escapeTrivialPage.frameAfterEscape = String(e.message); }
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
