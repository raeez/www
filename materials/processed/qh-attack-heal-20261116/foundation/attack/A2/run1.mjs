// Run 1: screen layout at the required widths (light), tab inventory, keyboard sequence from the top.
import { writeFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const URL = 'file://' + P;
const R = { steps: {} };
const save = () => writeFileSync(S + '/run1.json', JSON.stringify(R, null, 1));
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 420000);
try {
  const p = await page(b);
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'no-preference' }]);
  await p.size(1400, 900);
  const t0 = Date.now(); await p.go(URL); R.loadMs = Date.now() - t0;
  await p.ev(INSTALL);
  R.steps.env = await p.ev(`() => ({ ua: navigator.userAgent, hover: matchMedia('(hover: hover) and (pointer: fine)').matches, dark: matchMedia('(prefers-color-scheme: dark)').matches,
     detailsContent: CSS.supports('selector(::details-content)'), find: !!document.querySelector('.find'), findStyle: !!document.querySelector('style[data-find-style]'),
     knownActions: document.querySelectorAll('.known-actions').length, scrollFocus: document.querySelectorAll('[data-scroll-focus]').length })`);
  R.steps.logAfterLoad = p.log.slice(); save();
  // Tab-stop inventory at 1400.
  R.steps.tabInventory1400 = await p.ev(`() => { const l = __a2.tabbables(); return { total: l.length, byKind: __a2.categorize(l),
      gridStops: l.filter(e => e.closest('.grid-wrap')).length, beforeExamples: l.filter(e => e.compareDocumentPosition(document.getElementById('examples')) & Node.DOCUMENT_POSITION_FOLLOWING).length }; }`);
  save();
  // Keyboard: Tab from the top of the page.
  await p.ev(`() => { document.activeElement && document.activeElement.blur(); window.scrollTo(0, 0); return true; }`);
  const seq = [];
  for (let i = 1; i <= 26; i++) {
    await p.key('Tab'); await p.ev(`() => new Promise(r => requestAnimationFrame(() => setTimeout(r, 30)))`);
    seq.push(Object.assign({ n: i }, await p.ev(`() => __a2.focusInfo()`)));
    if (i === 4) await p.shot(S + '/k1400-nav-focus.png');
  }
  R.steps.tabSequence1400 = seq; save();
  // Layout at each width.
  R.steps.layout = {};
  for (const [w, h] of [[1400, 900], [1024, 800], [768, 1024], [480, 900], [375, 812]]) {
    await p.size(w, h); await p.ev(`() => { window.scrollTo(0, 0); document.activeElement && document.activeElement.blur(); return true; }`); await p.settle();
    R.steps.layout[w] = await p.ev(`() => __a2.M()`); save();
    if (w === 375) await p.shot(S + '/w375-light-top.png');
  }
  // At 375: tab inventory again (home link hidden) and the grid scrolled sideways.
  R.steps.tabInventory375 = await p.ev(`() => { const l = __a2.tabbables(); return { total: l.length, byKind: __a2.categorize(l) }; }`);
  R.steps.grid375 = await p.ev(`() => { const gw = document.querySelector('.grid-wrap'); gw.scrollIntoView({ block: 'start' }); window.scrollBy(0, -60);
      gw.scrollLeft = 170; return new Promise(r => requestAnimationFrame(() => setTimeout(() => {
        const corner = document.querySelector('.grid .corner').getBoundingClientRect(); const rowTh = document.querySelector('.grid tbody th').getBoundingClientRect();
        const heads = [...document.querySelectorAll('.grid thead .col-head')].map(b => { const r = b.getBoundingClientRect(); return { col: b.dataset.col, left: Math.round(r.left), right: Math.round(r.right) }; });
        const overSticky = heads.filter(h => h.right > rowTh.left + 2 && h.left < rowTh.right - 2).map(h => h.col);
        const firstCells = [...document.querySelector('.grid tbody tr').cells].slice(1).map((c, i) => { const r = c.getBoundingClientRect(); return { i, left: Math.round(r.left), right: Math.round(r.right), hiddenUnderRowHeader: r.right <= rowTh.right + 1 }; });
        r({ scrollLeft: gw.scrollLeft, corner: [Math.round(corner.left), Math.round(corner.right)], stickyRowHeader: [Math.round(rowTh.left), Math.round(rowTh.right)],
            columnHeadsVisibleAboveRowHeaderColumn: overSticky, cellsHiddenUnderRowHeader: firstCells.filter(c => c.hiddenUnderRowHeader).length,
            cornerPosition: getComputedStyle(document.querySelector('.grid .corner')).position, cornerLeft: getComputedStyle(document.querySelector('.grid .corner')).left });
      }, 120))); }`);
  await p.shot(S + '/w375-grid-scrolled.png'); save();
  R.logEnd = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
