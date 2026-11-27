// Run 5: does a print-only block layout for the question lists restore Question 16 on Letter? (style injected in memory only)
import { writeFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
const S = process.argv[2], P = process.argv[3];
const R = { steps: {} };
const save = () => writeFileSync(S + '/run5.json', JSON.stringify(R, null, 1));
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 400000);
try {
  const p = await page(b);
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.size(1400, 900); await p.go('file://' + P);
  R.steps.inject = await p.ev(`() => { const st = document.createElement('style'); st.id = 'a2-heal-test';
      st.textContent = '@media print { .questions { display: block; } .questions > .question + .question { margin-top: 16pt; } }'; document.head.appendChild(st); return true; }`);
  let t = Date.now(); await p.pdf(S + '/heal-letter.pdf', { paperWidth: 8.5, paperHeight: 11 }); R.steps.letterMs = Date.now() - t;
  t = Date.now(); await p.pdf(S + '/heal-a4.pdf', { paperWidth: 8.2677, paperHeight: 11.6929 }); R.steps.a4Ms = Date.now() - t;
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
