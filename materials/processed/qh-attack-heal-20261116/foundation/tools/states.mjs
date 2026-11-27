// Screenshots of interactive states.
//   node tools/run.mjs tools/states.mjs <page.html> <prefix>
import { fileUrl } from './cdp.mjs';
import { resolve } from 'node:path';

const wait = (ms) => new Promise((r) => setTimeout(r, ms));

export default async function (b, [pagePath, prefix]) {
  const url = fileUrl(pagePath);
  const done = [];
  async function shot(name, opts, fn) {
    const p = await b.page({ height: 900, ...opts });
    await p.goto(url + (opts.hash ? '#' + opts.hash : ''), 700);
    const info = fn ? await fn(p) : null;
    await wait(250);
    const path = resolve(`${prefix}-${name}.png`);
    await p.screenshot(path);
    done.push({ name, info, console: p.log.slice() });
    await p.close();
  }
  // Decisive section: its index and caption.
  await shot('1400-decisive-index', { width: 1400, reduced: 'reduce', hash: 'decisive' });
  // A card with mixed statuses.
  await shot('1400-q4', { width: 1400, reduced: 'reduce', hash: 'q-d-reduction-interface' });
  await shot('1400-q4-dark', { width: 1400, scheme: 'dark', reduced: 'reduce', hash: 'q-d-reduction-interface' });
  // Arrival at a related statement: its fold opens and the target shows where it stands.
  await shot('1400-target-related', { width: 1400, reduced: 'reduce', hash: 's-affine-energy-lifting' }, (p) =>
    p.eval(`(() => { const t = document.getElementById('s-affine-energy-lifting'); const c = t.querySelector('.statement-context');
      return { open: t.closest('details').open, contextShown: !!(c && c.getClientRects().length), top: Math.round(t.getBoundingClientRect().top) }; })()`));
  // Grid with its last row in view: the heading row stays under the bar.
  await shot('1400-grid-lower', { width: 1400, reduced: 'reduce' }, (p) => p.eval(`(() => {
      const rows = document.querySelectorAll('.grid tbody tr'); const last = rows[rows.length - 1];
      window.scrollTo(0, window.scrollY + last.getBoundingClientRect().top - 700);
      const th = document.querySelector('.grid thead th'); return { theadTop: Math.round(th.getBoundingClientRect().top), lastTop: Math.round(last.getBoundingClientRect().top) }; })()`));
  // A cell's card with the meaning of its status.
  await shot('1400-cell-card', { width: 1400, reduced: 'reduce' }, async (p) => {
    const r = await p.eval(`(() => { const btn = [...document.querySelectorAll('.cell-btn')].find(x => x.closest('td').getAttribute('data-status') === 'partial');
      btn.scrollIntoView({ block: 'center' }); btn.click(); const card = document.getElementById('card');
      return { open: !card.hidden, meaning: !!card.querySelector('.cell-note-meaning'), describedBy: card.getAttribute('aria-describedby'),
               described: (document.getElementById('card-text') || {}).className }; })()`);
    return r;
  });
  // Narrow: the bar while reading Open problems; the overview link stays pinned.
  await shot('375-bar-in-open', { width: 375, mobile: true, touch: true, reduced: 'reduce', hash: 'open' }, (p) => p.eval(`(() => {
      const first = document.querySelector('.nav li:first-child a').getBoundingClientRect(); const nav = document.querySelector('.nav');
      return { navScroll: nav.scrollLeft, firstLeft: Math.round(first.left), firstRight: Math.round(first.right), searchButton: !!document.querySelector('.bar [data-find-open]') }; })()`));
  // Narrow: the search control in the bar focuses the search.
  await shot('375-search-open', { width: 375, mobile: true, touch: true, reduced: 'reduce', hash: 'open' }, async (p) => {
    await p.eval(`document.querySelector('[data-find-open]').click()`);
    await wait(300);
    return p.eval(`({ focused: document.activeElement && document.activeElement.id, findTop: Math.round(document.querySelector('.find').getBoundingClientRect().top) })`);
  });
  // Narrow: a question card and the grid.
  await shot('375-q4-known', { width: 375, mobile: true, touch: true, reduced: 'reduce', hash: 'q-d-reduction-interface' }, (p) =>
    p.eval(`(() => { const k = document.querySelector('#q-d-reduction-interface .question-known'); window.scrollTo(0, window.scrollY + k.getBoundingClientRect().top - 60); return true; })()`));
  return done;
}
