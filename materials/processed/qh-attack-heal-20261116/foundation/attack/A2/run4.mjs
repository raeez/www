// Run 4: touch sheet at 375; print-media geometry at the A4 and Letter content widths; PDFs (A4, Letter, A4 dark).
import { writeFileSync, appendFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const URL = 'file://' + P;
const R = { steps: {} };
const save = () => writeFileSync(S + '/run4.json', JSON.stringify(R, null, 1));
const trace = (m) => appendFileSync(S + '/run4.trace', new Date().toISOString().slice(11, 19) + ' ' + m + '\n');
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 560000);
const frame = `() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 80))))`;
async function step(name, fn) { trace('start ' + name); try { R.steps[name] = await fn(); } catch (e) { R.steps[name] = { error: String(e && e.message || e) }; } trace('end ' + name); save(); }
const PRINTGEO = `(marginMm) => { const MML = 'http://www.w3.org/1998/Math/MathML'; const vw = document.documentElement.clientWidth; const m = marginMm * 96 / 25.4;
  const over = [];
  for (const el of document.querySelectorAll('main *')) { if (el.namespaceURI === MML && el.localName !== 'math') continue; const r = el.getBoundingClientRect(); if (!r.width) continue;
    if (r.right > vw + 0.5 || r.left < -0.5) { if (!el.checkVisibility()) continue; over.push({ el: __a2.d(el).slice(0, 70), left: Math.round(r.left), right: Math.round(r.right), beyondPaper: r.right > vw + m || r.left < -m }); } }
  const leaves = over.filter(o => !over.some(p => p !== o && false));
  const vis = s => [...document.querySelectorAll(s)].filter(e => e.checkVisibility()).length;
  return { contentWidthPx: vw, marginPx: Math.round(m), docScrollWidth: document.documentElement.scrollWidth, overflowCount: over.length, beyondPaper: over.filter(o => o.beyondPaper).slice(0, 12), sample: over.slice(0, 12),
    rowsClosed: [...document.querySelectorAll('details.row')].filter(d => !d.open).length, rowBodiesVisible: vis('.row-body'), knownListsVisible: vis('details.known > .statements'), colDefsVisible: vis('.col-defs > dl'),
    statementsVisible: vis('.statement'), statementsTotal: document.querySelectorAll('.statement').length,
    screenControlsVisible: Object.fromEntries(['.bar', '.find', '.row-tools', '.known-actions', '.grid-hint', '#card', '.skip', '.link-btn', '.filters', '.cell-note', '.icon', '.theme'].map(s => [s, vis(s)])),
    gridWidth: Math.round(document.querySelector('.grid').getBoundingClientRect().width), gridWrapScroll: document.querySelector('.grid-wrap').scrollWidth - document.querySelector('.grid-wrap').clientWidth }; }`;
try {
  const p = await page(b);
  // E. Touch sheet at 375.
  await p.s('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 5 });
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.size(375, 667, true); await p.go(URL); await p.ev(INSTALL);
  await step('touchSheet', async () => {
    const r = await p.ev(`() => { const hover = matchMedia('(hover: hover) and (pointer: fine)').matches; const btns = [...document.querySelectorAll('.grid tbody tr:nth-child(6) .cell-btn')];
        const btn = btns[2]; const gw = document.querySelector('.grid-wrap'); window.scrollTo(0, btn.getBoundingClientRect().top + scrollY - innerHeight + 140); btn.click();
        const c = document.getElementById('card'); const cr = c.getBoundingClientRect(), br = btn.getBoundingClientRect();
        return { hoverCapable: hover, innerWidth, sheet: c.classList.contains('sheet'), position: getComputedStyle(c).position, card: [cr.left, cr.top, cr.right, cr.bottom].map(Math.round),
                 trigger: [br.left, br.top, br.right, br.bottom].map(Math.round), coversTrigger: !(cr.right < br.left || cr.left > br.right || cr.bottom < br.top || cr.top > br.bottom), closeControl: !!c.querySelector('button') }; }`);
    await p.ev(frame); await p.shot(S + '/touch375-sheet.png'); return r; });
  await p.s('Emulation.setTouchEmulationEnabled', { enabled: false });
  // F. Print-media geometry (emulated) at the A4 and Letter content widths (16 mm side margins), all details closed.
  await p.size(1400, 900, false); await p.go(URL); await p.ev(INSTALL);
  await p.media('print', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.size(673, 950); await p.ev(frame); await p.ev(frame);
  await step('printGeoA4', () => p.ev(PRINTGEO, 16));
  await p.size(695, 950); await p.ev(frame); await p.ev(frame);
  await step('printGeoLetter', () => p.ev(PRINTGEO, 16));
  // Titles and first words of every statement, for the PDF text check.
  await step('statementKeys', () => p.ev(`() => [...document.querySelectorAll('.statement')].map(s => { const pick = (el) => { if (!el) return ''; let runs = [], cur = '';
        (function walk(n) { if (n.nodeType === 3) { cur += n.nodeValue; return; } if (n.nodeType !== 1) return; if (n.localName === 'math' || n.localName === 'svg') { runs.push(cur); cur = ''; return; } for (let c = n.firstChild; c; c = c.nextSibling) walk(c); })(el);
        runs.push(cur); return runs.map(x => x.replace(/\\s+/g, ' ').trim()).sort((a, b) => b.length - a.length)[0] || ''; };
      return { id: s.id || null, status: s.dataset.status, title: pick(s.querySelector('.statement-title')), text: pick(s.querySelector('.statement-text p')).slice(0, 80) }; })`));
  // PDFs. Count beforeprint/afterprint and details state.
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.size(1400, 900); await p.go(URL); await p.ev(INSTALL);
  const arm = `() => { window.__bp = 0; window.__ap = 0; window.__openAtBP = -1; addEventListener('beforeprint', () => { __bp++; __openAtBP = document.querySelectorAll('main details[open]').length; }); addEventListener('afterprint', () => { __ap++; }); return document.querySelectorAll('main details[open]').length; }`;
  const after = `() => ({ beforeprint: __bp, afterprint: __ap, openDetailsAtBeforePrint: __openAtBP, openDetailsNow: document.querySelectorAll('main details[open]').length, totalDetails: document.querySelectorAll('main details').length })`;
  await step('pdfA4', async () => { const open0 = await p.ev(arm); const t = Date.now(); await p.pdf(S + '/print-a4.pdf', { paperWidth: 8.2677, paperHeight: 11.6929 }); return Object.assign({ ms: Date.now() - t, openBefore: open0 }, await p.ev(after)); });
  await step('pdfLetter', async () => { const t = Date.now(); await p.pdf(S + '/print-letter.pdf', { paperWidth: 8.5, paperHeight: 11 }); return Object.assign({ ms: Date.now() - t }, await p.ev(after)); });
  await p.media('', [{ name: 'prefers-color-scheme', value: 'dark' }, { name: 'prefers-reduced-motion', value: 'reduce' }]); await p.ev(frame);
  await step('pdfA4dark', async () => { const t = Date.now(); await p.pdf(S + '/print-a4-dark.pdf', { paperWidth: 8.2677, paperHeight: 11.6929 }); return Object.assign({ ms: Date.now() - t, scheme: await p.ev(`() => getComputedStyle(document.documentElement).colorScheme`) }, await p.ev(after)); });
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
