// Run 2: grid sideways scroll at 375, nav focus at 768, vertically clipped formulas, card behaviour,
// row filter, anchor targets under the bar, dark tokens, reduced motion.
import { writeFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const URL = 'file://' + P;
const R = { steps: {} };
const save = () => writeFileSync(S + '/run2.json', JSON.stringify(R, null, 1));
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 420000);
const frame = `() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 80))))`;
async function step(name, fn) { try { R.steps[name] = await fn(); } catch (e) { R.steps[name] = { error: String(e && e.message || e) }; } save(); }
try {
  const p = await page(b);
  const light = [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }];
  await p.media('', light);
  // 1. 375: the grid scrolled sideways; what overflows the counterexample cards.
  await p.size(375, 812); await p.go(URL); await p.ev(INSTALL);
  await step('reducedMotion', () => p.ev(`() => ({ reduce: matchMedia('(prefers-reduced-motion: reduce)').matches, htmlScrollBehavior: getComputedStyle(document.documentElement).scrollBehavior,
      findFieldTransition: getComputedStyle(document.querySelector('.find-field')).transitionDuration, findLinkRule: 'n/a' })`));
  await step('grid375', async () => { const g = await p.ev(`() => { const gw = document.querySelector('.grid-wrap'); const y = gw.getBoundingClientRect().top + scrollY - 70; window.scrollTo(0, y); gw.scrollLeft = 170; return { y, scrollY }; }`);
    await p.ev(frame); await p.shot(S + '/w375-grid-scrolled.png'); return Object.assign(g, await p.ev(`() => ({ scrollY, sl: document.querySelector('.grid-wrap').scrollLeft })`)); });
  await step('witnessOverflow375', () => p.ev(`() => { const s = document.getElementById('s-witness-fusion-braid'); const r = s.getBoundingClientRect(); const cs = getComputedStyle(s);
      const inner = r.right - parseFloat(cs.borderRightWidth) - parseFloat(cs.paddingRight); const out = [];
      for (const el of s.querySelectorAll('*')) { if (el.namespaceURI === 'http://www.w3.org/1998/Math/MathML' && el.localName !== 'math') continue; const q = el.getBoundingClientRect(); if (q.right > inner + 0.5) out.push(__a2.d(el).slice(0, 70) + ' R=' + q.right.toFixed(1)); }
      const f = s.closest('.failure').getBoundingClientRect(); return { statementRight: r.right, contentRight: inner, failureRight: f.right, marginLeft: cs.marginLeft, width: r.width, viewport: innerWidth, beyond: out.slice(0, 8) }; }`));
  // 2. 768: Tab to the last link of the bar.
  await p.size(768, 1024); await p.ev(`() => { window.scrollTo(0, 0); document.activeElement && document.activeElement.blur(); return true; }`); await p.ev(frame);
  await step('navFocus768', async () => { const seq = [];
    for (let i = 1; i <= 11; i++) { await p.key('Tab'); await p.ev(frame); const fi = await p.ev(`() => { const a = document.activeElement; const n = document.querySelector('.nav'); const r = a.getBoundingClientRect(), q = n.getBoundingClientRect();
        const mask = getComputedStyle(n).maskImage || getComputedStyle(n).webkitMaskImage; return { el: __a2.d(a).slice(0, 40), left: Math.round(r.left), right: Math.round(r.right), navLeft: Math.round(q.left), navRight: Math.round(q.right),
        fadeStartsAt: Math.round(q.left + 0.88 * q.width), mask: mask, navScrollLeft: n.scrollLeft }; }`); seq.push(fi); }
    await p.shot(S + '/k768-nav-last.png'); return seq; });
  // 3. 1400: formula boxes whose content is taller than the box (overflow-y: hidden clips it).
  await p.size(1400, 900); await p.ev(`() => { window.scrollTo(0, 0); return true; }`); await p.ev(frame);
  await step('vclip1400', () => p.ev(`() => { const out = [];
      for (const b of document.querySelectorAll('.math-display, .math-long')) { if (!b.checkVisibility()) continue; const gap = b.scrollHeight - b.clientHeight; if (gap <= 1) continue;
        const ann = b.querySelector('annotation'); const host = b.closest('[id]');
        out.push({ cls: b.className, gap, sh: b.scrollHeight, ch: b.clientHeight, host: host ? host.id : null, tex: ann ? ann.textContent.slice(0, 90) : '' }); }
      out.sort((a, b) => b.gap - a.gap); return { count: out.length, worst: out.slice(0, 12) }; }`));
  await step('vclipShot', async () => {
    const info = await p.ev(`() => { let best = null; for (const b of document.querySelectorAll('.math-display, .math-long')) { if (!b.checkVisibility()) continue; const gap = b.scrollHeight - b.clientHeight; if (!best || gap > best.gap) best = { b, gap }; }
        best.b.setAttribute('data-a2-target', ''); const y = best.b.getBoundingClientRect().top + scrollY - 300; window.scrollTo(0, y); const r = best.b.getBoundingClientRect();
        return { gap: best.gap, rect: [r.left, r.top, r.right, r.bottom].map(Math.round), cls: best.b.className, tex: (best.b.querySelector('annotation') || {}).textContent }; }`);
    await p.ev(frame); await p.shot(S + '/vclip-before.png');
    await p.ev(`() => { const b = document.querySelector('[data-a2-target]'); b.style.overflow = 'visible'; return true; }`); await p.ev(frame);
    await p.shot(S + '/vclip-after.png');
    const after = await p.ev(`() => { const b = document.querySelector('[data-a2-target]'); const r = b.getBoundingClientRect(); b.style.overflow = ''; b.removeAttribute('data-a2-target'); return [r.left, r.top, r.right, r.bottom].map(Math.round); }`);
    return Object.assign(info, { rectAfter: after }); });
  // 4. Cards. (a) The card for a cell of the W-algebras row.
  await step('cardWAlgebras', async () => {
    const pre = await p.ev(`() => { const btn = document.querySelector('.cell-btn[data-row="row-w-algebras"]'); const y = btn.getBoundingClientRect().top + scrollY - 400; window.scrollTo(0, y); btn.focus(); return true; }`);
    await p.ev(frame); await p.key('Enter'); await p.ev(frame);
    const r = await p.ev(`() => { const c = document.getElementById('card'); const m = c.querySelector('.card-more'); return { hidden: c.hidden, cardMoreText: m ? m.textContent : null, cardMoreHref: m ? m.getAttribute('href') : null,
        rowName: document.querySelector('#row-w-algebras .row-name').innerText, active: __a2.d(document.activeElement).slice(0, 60), labelledby: c.getAttribute('aria-labelledby') }; }`);
    await p.shot(S + '/card-walgebras.png');
    await p.key('Escape'); await p.ev(frame); return r; });
  // (b) A column head: Enter pins its card; Tab moves on; the card stays; Escape pulls focus back.
  await step('colHeadPinned', async () => {
    await p.ev(`() => { const h = document.querySelector('.col-head[data-col="object"]'); const y = h.getBoundingClientRect().top + scrollY - 200; window.scrollTo(0, y); h.focus(); return true; }`); await p.ev(frame);
    await p.key('Enter'); await p.ev(frame);
    const st = []; const snap = (label) => p.ev(`(label) => { const c = document.getElementById('card'); const a = document.activeElement; const cr = c.getBoundingClientRect(), ar = a.getBoundingClientRect();
        const overlap = !c.hidden && !(cr.right < ar.left || cr.left > ar.right || cr.bottom < ar.top || cr.top > ar.bottom);
        return { label, cardHidden: c.hidden, cardTitle: (c.querySelector('.card-term, .cell-note-head') || {}).textContent, active: __a2.d(a).slice(0, 60), cardCoversFocused: overlap,
                 objectExpanded: document.querySelector('.col-head[data-col="object"]').getAttribute('aria-expanded') }; }`, label);
    st.push(await snap('after Enter on object'));
    for (let i = 1; i <= 10; i++) { await p.key('Tab'); await p.ev(frame); if (i === 1 || i === 7 || i === 8 || i === 10) st.push(await snap('after Tab ' + i)); }
    await p.shot(S + '/card-colhead-stale.png');
    await p.key('Escape'); await p.ev(frame); st.push(await snap('after Escape'));
    return st; });
  // (c) Latent: a glossary term inside a column definition (injected in memory) is copied into the card.
  await step('termInsideCard', async () => {
    const r = await p.ev(`() => { const dd = document.querySelector('#col-dual dd'); const g = document.querySelector('.gloss');
        const t = document.createElement('button'); t.type = 'button'; t.className = 'term'; t.setAttribute('data-term', g.id); t.textContent = 'injected term'; dd.appendChild(document.createTextNode(' ')); dd.appendChild(t);
        const h = document.querySelector('.col-head[data-col="dual"]'); const y = h.getBoundingClientRect().top + scrollY - 300; window.scrollTo(0, y);
        h.click(); const c = document.getElementById('card'); const before = c.getBoundingClientRect(); const hr = h.getBoundingClientRect();
        const inCard = c.querySelector('.term'); inCard.focus(); inCard.click();
        const after = c.getBoundingClientRect();
        return { headRect: [hr.left, hr.top, hr.bottom].map(Math.round), cardBefore: [before.left, before.top].map(Math.round), cardAfter: [after.left, after.top].map(Math.round),
                 cardAfterTitle: (c.querySelector('.card-term') || {}).textContent, active: __a2.d(document.activeElement).slice(0, 40), copiedTriggerConnected: inCard.isConnected,
                 barBottom: Math.round(document.querySelector('.bar').getBoundingClientRect().bottom) }; }`);
    await p.ev(frame); await p.key('Escape'); await p.ev(frame);
    r.afterEscapeActive = await p.ev(`() => __a2.d(document.activeElement).slice(0, 40)`);
    return r; });
  // 5. Row filter: what a reader sees after choosing one status.
  await p.go(URL); await p.ev(INSTALL);
  await step('filterConditional', () => p.ev(`() => { const f = document.querySelector('.row-tools .filter[data-filter="conditional"]'); f.click();
      const rows = [...document.querySelectorAll('details.row')]; const vis = rows.filter(d => d.checkVisibility());
      const empty = rows.filter(d => d.hasAttribute('data-filter-empty'));
      const sample = empty.slice(0, 3).map(d => ({ id: d.id, open: d.open, summaryCount: d.querySelector('.row-count').innerText.replace(/\\s+/g, ' ') }));
      const live = document.querySelector('.row-tools [role=status]'); const styled = getComputedStyle(empty[0]).display + '/' + getComputedStyle(empty[0]).opacity;
      return { rowsDisplayed: vis.length, rowsEmptyMarked: empty.length, rowsOpen: rows.filter(d => d.open).length, emptySample: sample, live: live && live.textContent, emptyRowComputed: styled }; }`));
  // 6. Anchor targets and the sticky bar (instant scroll under reduced motion).
  await step('anchors', async () => { const ids = await p.ev(`() => { const a = document.querySelector('.rows .statement[id]'); const q = document.querySelector('.question[id]'); const g = document.querySelector('.gloss[id]');
        const ch = document.querySelector('.change-link'); return [a.id, 'row-heisenberg', q.id, g.id, ch ? ch.getAttribute('href').slice(1) : null].filter(Boolean); }`);
    const out = [];
    for (const id of ids) { await p.ev(`(id) => { location.hash = id; return true; }`, id); await p.ev(frame); await p.ev(frame);
      out.push(await p.ev(`(id) => { const t = document.getElementById(id); const r = t.getBoundingClientRect(); const bar = document.querySelector('.bar').getBoundingClientRect();
          return { id, top: Math.round(r.top), barBottom: Math.round(bar.bottom), hiddenByBar: r.top < bar.bottom - 1, openRows: document.querySelectorAll('details.row[open]').length }; }`, id)); }
    return out; });
  // 7. Dark tokens at 1400 (computed), and a picture of the grid in each theme.
  await step('gridLightShot', async () => { await p.ev(`() => { location.hash = ''; const g = document.querySelector('.grid-wrap'); window.scrollTo(0, g.getBoundingClientRect().top + scrollY - 60); return true; }`); await p.ev(frame); await p.shot(S + '/grid1400-light.png'); return true; });
  await p.media('', [{ name: 'prefers-color-scheme', value: 'dark' }, { name: 'prefers-reduced-motion', value: 'reduce' }]); await p.ev(frame);
  await step('darkTokens', () => p.ev(`() => { const cs = getComputedStyle(document.documentElement); const v = n => cs.getPropertyValue(n).trim();
      return { paper: v('--paper'), ink4: v('--ink-4'), notPosed: v('--st-not-posed'), bodyBg: getComputedStyle(document.body).backgroundColor, bodyColor: getComputedStyle(document.body).color,
               markNotPosed: getComputedStyle(document.querySelector('.cell-not-posed .mark')).color, colorScheme: cs.colorScheme }; }`));
  await step('gridDarkShot', async () => { await p.shot(S + '/grid1400-dark.png'); return true; });
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
