// Run 8: picture of the counterexample chip at 375; in-memory test of a single tab stop for the grid (tabindex -1 on its controls but one).
import { writeFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const R = { steps: {} };
const save = () => writeFileSync(S + '/run8.json', JSON.stringify(R, null, 1));
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 200000);
const frame = `() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 80))))`;
try {
  const p = await page(b);
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.size(375, 812); await p.go('file://' + P); await p.ev(INSTALL);
  R.steps.chip = await p.ev(`() => { const s = document.getElementById('s-witness-fusion-braid'); window.scrollTo(0, s.getBoundingClientRect().top + scrollY - 120); const r = s.getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom].map(Math.round); }`);
  await p.ev(frame); await p.shot(S + '/w375-failure-chip.png');
  await p.size(1400, 900); await p.ev(frame);
  R.steps.gridOneStop = await p.ev(`() => { const ctl = [...document.querySelectorAll('.grid button, .grid a[href]')]; ctl.forEach((c, i) => { if (i) c.setAttribute('tabindex', '-1'); });
      const gw = document.querySelector('.grid-wrap'); window.scrollTo(0, gw.getBoundingClientRect().top + scrollY - 200); gw.focus(); return { controls: ctl.length, first: __a2.d(ctl[0]).slice(0, 40) }; }`);
  const seq = [];
  const rec = async (label) => seq.push(label + ' -> ' + (await p.ev(`() => __a2.d(document.activeElement).slice(0, 60)`)));
  await p.key('Tab'); await p.ev(frame); await rec('Tab');
  await p.key('ArrowDown'); await p.ev(frame); await rec('ArrowDown');
  await p.key('ArrowRight'); await p.ev(frame); await rec('ArrowRight');
  await p.key('End'); await p.ev(frame); await rec('End');
  await p.key('Tab'); await p.ev(frame); await rec('Tab');
  await p.key('Tab', true); await p.ev(frame); await rec('Shift+Tab');
  R.steps.gridOneStopSequence = seq;
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
