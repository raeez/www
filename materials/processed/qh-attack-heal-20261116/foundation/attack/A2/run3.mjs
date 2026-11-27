// Run 3: card behaviour (cell, column head, term inside a card), row filter, anchors under the bar, dark tokens.
// Escape is dispatched as a DOM KeyboardEvent (status.js reads only event.key); Tab and Enter are real key events.
import { writeFileSync, appendFileSync } from 'node:fs';
import { launch, page } from './cdp.mjs';
import { INSTALL } from './inpage.mjs';
const S = process.argv[2], P = process.argv[3];
const URL = 'file://' + P;
const R = { steps: {} };
const save = () => writeFileSync(S + '/run3.json', JSON.stringify(R, null, 1));
const trace = (m) => appendFileSync(S + '/run3.trace', new Date().toISOString().slice(11, 19) + ' ' + m + '\n');
const b = launch(S + '/chrome');
const kill = setTimeout(() => { R.timeout = true; save(); b.proc.kill('SIGKILL'); process.exit(2); }, 300000);
const frame = `() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 80))))`;
const escape = `() => { (document.activeElement || document.body).dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true, cancelable: true })); return true; }`;
async function step(name, fn) { trace('start ' + name); try { R.steps[name] = await fn(); } catch (e) { R.steps[name] = { error: String(e && e.message || e) }; } trace('end ' + name); save(); }
try {
  const p = await page(b);
  await p.media('', [{ name: 'prefers-color-scheme', value: 'light' }, { name: 'prefers-reduced-motion', value: 'reduce' }]);
  await p.size(1400, 900); await p.go(URL); await p.ev(INSTALL);
  await step('cardWAlgebras', async () => {
    await p.ev(`() => { const btn = document.querySelector('.cell-btn[data-row="row-w-algebras"]'); window.scrollTo(0, btn.getBoundingClientRect().top + scrollY - 400); btn.focus(); return true; }`);
    await p.ev(frame); await p.key('Enter'); await p.ev(frame);
    const r = await p.ev(`() => { const c = document.getElementById('card'); const m = c.querySelector('.card-more'); return { hidden: c.hidden, cardMoreText: m ? m.textContent : null, cardMoreHref: m ? m.getAttribute('href') : null,
        gridLinkTitle: document.querySelector('.grid tbody th a[href="#row-w-algebras"]').getAttribute('title'), active: __a2.d(document.activeElement).slice(0, 60) }; }`);
    await p.ev(escape); await p.ev(frame); r.afterEscape = await p.ev(`() => ({ hidden: document.getElementById('card').hidden, active: __a2.d(document.activeElement).slice(0, 60) })`); return r; });
  await step('colHeadPinned', async () => {
    await p.ev(`() => { const h = document.querySelector('.col-head[data-col="object"]'); window.scrollTo(0, h.getBoundingClientRect().top + scrollY - 200); h.focus(); return true; }`); await p.ev(frame);
    await p.key('Enter'); await p.ev(frame);
    const st = []; const snap = (label) => p.ev(`(label) => { const c = document.getElementById('card'); const a = document.activeElement; const cr = c.getBoundingClientRect(), ar = a.getBoundingClientRect();
        const overlap = !c.hidden && !(cr.right < ar.left || cr.left > ar.right || cr.bottom < ar.top || cr.top > ar.bottom);
        return { label, cardHidden: c.hidden, cardTitle: ((c.querySelector('.card-term, .cell-note-head') || {}).textContent || '').slice(0, 40), linksInCard: c.querySelectorAll('a[href], button').length,
                 active: __a2.d(a).slice(0, 60), cardCoversFocused: overlap, objectExpanded: document.querySelector('.col-head[data-col="object"]').getAttribute('aria-expanded'), activeExpanded: a.getAttribute('aria-expanded') }; }`, label);
    st.push(await snap('after Enter on object'));
    for (let i = 1; i <= 10; i++) { await p.key('Tab'); await p.ev(frame); if ([1, 7, 8, 9, 10].includes(i)) st.push(await snap('after Tab ' + i)); }
    await p.shot(S + '/card-colhead-stale.png');
    await p.ev(escape); await p.ev(frame); st.push(await snap('after Escape'));
    return st; });
  await step('termInsideCard', async () => {
    const r = await p.ev(`() => { const dd = document.querySelector('#col-dual dd'); const g = document.querySelector('.gloss');
        const t = document.createElement('button'); t.type = 'button'; t.className = 'term'; t.setAttribute('data-term', g.id); t.textContent = 'injected term'; dd.appendChild(document.createTextNode(' ')); dd.appendChild(t);
        const h = document.querySelector('.col-head[data-col="dual"]'); window.scrollTo(0, h.getBoundingClientRect().top + scrollY - 300);
        h.click(); const c = document.getElementById('card'); const before = c.getBoundingClientRect(); const hr = h.getBoundingClientRect();
        const inCard = c.querySelector('.term'); inCard.focus(); inCard.click(); const after = c.getBoundingClientRect();
        return { headRect: [hr.left, hr.top, hr.bottom].map(Math.round), cardBefore: [before.left, before.top].map(Math.round), cardAfter: [after.left, after.top].map(Math.round),
                 cardAfterTitle: (c.querySelector('.card-term') || {}).textContent, active: __a2.d(document.activeElement).slice(0, 40), copiedTriggerConnected: inCard.isConnected,
                 barBottom: Math.round(document.querySelector('.bar').getBoundingClientRect().bottom), scrollY: Math.round(scrollY) }; }`);
    await p.ev(frame); await p.shot(S + '/card-term-in-card.png');
    await p.ev(escape); await p.ev(frame); r.afterEscapeActive = await p.ev(`() => __a2.d(document.activeElement).slice(0, 40)`); return r; });
  await p.go(URL); await p.ev(INSTALL);
  await step('filterConditional', () => p.ev(`() => { const f = document.querySelector('.row-tools .filter[data-filter="conditional"]'); f.click();
      const rows = [...document.querySelectorAll('details.row')]; const empty = rows.filter(d => d.hasAttribute('data-filter-empty'));
      const sample = empty.slice(0, 2).map(d => ({ id: d.id, open: d.open, summaryCount: d.querySelector('.row-count').innerText.replace(/\\s+/g, ' ') }));
      const full = rows.filter(d => !d.hasAttribute('data-filter-empty')).slice(0, 2).map(d => ({ id: d.id, open: d.open, summaryCount: d.querySelector('.row-count').innerText.replace(/\\s+/g, ' '), shown: d.querySelectorAll('.statement:not([hidden])').length }));
      const live = document.querySelector('.row-tools [role=status]');
      return { rowsDisplayed: rows.filter(d => d.checkVisibility()).length, rowsEmptyMarked: empty.length, rowsOpen: rows.filter(d => d.open).length, emptySample: sample, nonEmptySample: full,
               live: live && live.textContent, emptyRowDisplay: empty[0] ? getComputedStyle(empty[0]).display : null, addressAfter: location.search }; }`));
  await step('anchors', async () => { const ids = await p.ev(`() => { const a = document.querySelector('.rows .statement[id]'); const q = document.querySelector('.question[id]'); const g = document.querySelector('.gloss[id]');
        const k = document.querySelector('details.known .statement[id]'); const ch = document.querySelector('.change-link'); return [a.id, 'row-heisenberg', q.id, g.id, k ? k.id : null, ch ? ch.getAttribute('href').slice(1) : null].filter(Boolean); }`);
    await p.ev(`() => { document.querySelector('.row-tools .filter[aria-pressed="true"]') && document.querySelector('.row-tools .filter[aria-pressed="true"]').click(); return true; }`);
    const out = [];
    for (const id of ids) { await p.ev(`(id) => { location.hash = id; return true; }`, id); await p.ev(frame); await p.ev(frame);
      out.push(await p.ev(`(id) => { const t = document.getElementById(id); const r = t.getBoundingClientRect(); const bar = document.querySelector('.bar').getBoundingClientRect();
          return { id, top: Math.round(r.top), barBottom: Math.round(bar.bottom), hiddenByBar: r.top < bar.bottom - 1, visible: t.checkVisibility() }; }`, id)); }
    return out; });
  await step('gridLightShot', async () => { await p.ev(`() => { history.replaceState(null, '', location.pathname); const g = document.querySelector('.grid-wrap'); window.scrollTo(0, g.getBoundingClientRect().top + scrollY - 60); return true; }`); await p.ev(frame); await p.shot(S + '/grid1400-light.png'); return true; });
  await p.media('', [{ name: 'prefers-color-scheme', value: 'dark' }, { name: 'prefers-reduced-motion', value: 'reduce' }]); await p.ev(frame);
  await step('darkTokens', () => p.ev(`() => { const cs = getComputedStyle(document.documentElement); const v = n => cs.getPropertyValue(n).trim();
      return { paper: v('--paper'), ink4: v('--ink-4'), notPosed: v('--st-not-posed'), bodyBg: getComputedStyle(document.body).backgroundColor, bodyColor: getComputedStyle(document.body).color,
               markNotPosed: getComputedStyle(document.querySelector('.cell-not-posed .mark')).color, colorScheme: cs.colorScheme }; }`));
  await step('gridDarkShot', async () => { await p.shot(S + '/grid1400-dark.png'); return true; });
  R.log = p.log.slice();
} catch (e) { R.error = String(e && e.stack || e); }
save(); clearTimeout(kill); await b.close(); process.exit(0);
