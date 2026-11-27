// Non-browser behaviour checks of a built status page in jsdom (no layout, no painting, no real scrolling).
// Each J-check names the ledger entry it guards; R-checks guard behaviour that already worked (regressions).
// Usage: QH_JSDOM=<path to jsdom> node qh-jsdom-checks.mjs --html <preview.html> [--out <result.json>] [--only J1,J2]
// Reads the page; writes only the --out file. jsdom does not enforce the page CSP and makes no network request.
import fs from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { JSDOM, VirtualConsole } = require(process.env.QH_JSDOM || 'jsdom');
const args = {};
for (let i = 2; i < process.argv.length; i += 2) args[process.argv[i].replace(/^--/, '')] = process.argv[i + 1];
const HTML = fs.readFileSync(args.html, 'utf8');
const ONLY = args.only ? new Set(args.only.split(',')) : null;
const BASE = 'https://example.test/quantum-holography-tracker.html';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const pageErrors = [];

// One page per check. hover: emulate a hover-capable fine pointer through a matchMedia stub.
function load({ search = '', hash = '', hover = false } = {}) {
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented/.test(String(e && e.message))) pageErrors.push(String(e && e.message).slice(0, 200)); });
  vc.on('error', e => pageErrors.push(String(e).slice(0, 200)));
  const dom = new JSDOM(HTML, {
    url: BASE + search + hash, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) {
      w.matchMedia = q => ({ matches: hover ? /\(hover: hover\)/.test(q) && /\(pointer: fine\)/.test(q) : false, media: q, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
      w.HTMLElement.prototype.scrollIntoView = function () {};
      w.Element.prototype.scrollTo = function () {};
      w.scrollTo = function () {};
    }
  });
  return dom.window;
}
const textNoTex = el => { if (!el) return null; const c = el.cloneNode(true); c.querySelectorAll('annotation').forEach(n => n.remove()); return c.textContent.replace(/\s+/g, ' ').trim(); };
const desc = el => !el ? 'null' : el.localName + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '') + ' "' + ((el.getAttribute && el.getAttribute('aria-label')) || el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40) + '"';
function key(w, el, k, opts = {}) {
  const e = new w.KeyboardEvent('keydown', { key: k, bubbles: true, cancelable: true, ...opts });
  el.dispatchEvent(e);
  return e;
}
// Emulates the browser's sequential focus move after an unhandled Tab (DOM order, skipping hidden and closed content).
function tab(w, shift = false) {
  const d = w.document, from = d.activeElement || d.body;
  const e = key(w, from, 'Tab', { shiftKey: shift });
  if (e.defaultPrevented) return;
  const sel = 'a[href], button:not([disabled]), input:not([disabled]), summary, [tabindex]:not([tabindex="-1"])';
  const list = Array.from(d.querySelectorAll(sel)).filter(el => {
    if (el.closest('[hidden]')) return false;
    for (let c = el, p = el.parentElement; p; c = p, p = p.parentElement) if (p.localName === 'details' && !p.open && !(c.localName === 'summary' && c.parentNode === p)) return false;
    return true;
  });
  const i = list.indexOf(from);
  const next = shift ? list[(i < 0 ? list.length : i) - 1] : list[i + 1];
  if (next) next.focus();
}
const results = {};
function record(id, pass, observed) { results[id] = { pass, observed }; console.log(`${pass ? 'PASS' : 'FAIL'} ${id} ${JSON.stringify(observed).slice(0, 420)}`); }

const checks = {
  // C10: Escape that closes a hover card leaves keyboard focus where it is.
  async J1() {
    const w = load({ hover: true }); const d = w.document; await sleep(50);
    const chip = d.querySelector('.row-tools .filter'); chip.focus();
    d.querySelector('.lead .term').dispatchEvent(new w.MouseEvent('mouseover', { bubbles: true }));
    const shown = !d.getElementById('card').hidden;
    key(w, d.activeElement, 'Escape');
    const a = desc(d.activeElement);
    const input = d.getElementById('find-q'); input.focus(); input.value = 'koszul'; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
    d.querySelector('.lead .term').dispatchEvent(new w.MouseEvent('mouseover', { bubbles: true }));
    key(w, input, 'Escape');
    const b = desc(d.activeElement);
    record('J1', shown && d.activeElement === input && a.startsWith('button.filter'), { hoverCardShown: shown, focusAfterEscapeFromChip: a, focusAfterEscapeInSearch: b });
    w.close();
  },
  // C11: a pinned card follows focus; the trigger left behind is no longer marked expanded.
  async J2() {
    const w = load(); const d = w.document; await sleep(50);
    const heads = d.querySelectorAll('.grid thead .col-head');
    heads[0].focus(); heads[0].click();
    const pinnedTitle = (d.getElementById('card-title') || {}).textContent;
    for (let i = 0; i < 3 && d.activeElement !== heads[1]; i++) tab(w);
    await sleep(250);
    const c = d.getElementById('card');
    const o = { active: desc(d.activeElement), cardHidden: c.hidden, cardTitle: c.hidden ? null : (d.getElementById('card-title') || {}).textContent, expanded1: heads[0].getAttribute('aria-expanded'), expanded2: heads[1].getAttribute('aria-expanded') };
    const ok = d.activeElement === heads[1] && o.expanded1 === 'false' && (o.cardHidden || o.cardTitle === heads[1].textContent);
    record('J2', ok, { pinnedTitle, ...o });
    // Shift+Tab away from a pinned owner closes its card.
    heads[2].focus(); heads[2].click();
    tab(w, true); await sleep(50);
    const back = { cardHidden: c.hidden, expanded3: heads[2].getAttribute('aria-expanded'), active: desc(d.activeElement) };
    record('J2b', back.cardHidden || (d.getElementById('card-title') || {}).textContent === textNoTex(d.activeElement), back);
    w.close();
  },
  // C12: Down pressed right after typing lands on a live result of the new query.
  async J3() {
    const w = load(); const d = w.document; await sleep(50);
    const input = d.getElementById('find-q'); input.focus();
    input.value = 'vertex'; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(300);
    input.value = 'vertex algebra'; input.dispatchEvent(new w.Event('input', { bubbles: true }));
    key(w, input, 'ArrowDown'); await sleep(300);
    const a = d.activeElement;
    record('J3', !!a.closest('#find-results') && a.isConnected, { active: desc(a), connected: a.isConnected, count: d.querySelector('.find-count').textContent });
    w.close();
  },
  // C07: following a link to a row that Close all closed opens it again.
  async J4() {
    const w = load(); const d = w.document; await sleep(50);
    const link = d.querySelector('.grid tbody th a'); const id = link.getAttribute('href').slice(1);
    link.click(); await sleep(150);
    const open1 = d.getElementById(id).open;
    d.querySelector('#examples [data-expand="none"]').click(); await sleep(50);
    link.click(); await sleep(150);
    record('J4', open1 && d.getElementById(id).open, { id, openedFirst: open1, reopenedAfterCloseAll: d.getElementById(id).open, hash: w.location.hash });
    w.close();
  },
  // C09: an in-page link followed within 350 ms of typing keeps the search (popstate dispatched as the HTML standard does on fragment navigation; jsdom does not).
  async J5() {
    const w = load(); const d = w.document; await sleep(50);
    const input = d.getElementById('find-q'); input.focus();
    input.value = 'koszul'; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(150);
    d.querySelector('.nav a[href="#examples"]').click();
    w.dispatchEvent(new w.PopStateEvent('popstate', { state: null }));
    await sleep(600);
    const o = { input: input.value, search: w.location.search, hash: w.location.hash, count: d.querySelector('.find-count').textContent };
    record('J5', o.input === 'koszul' && /q=koszul/.test(o.search), o);
    w.close();
  },
  // C16: logic of clearing the sticky row header (rectangles stubbed; layout itself is not tested here).
  async J6() {
    const w = load(); const d = w.document; await sleep(50);
    const wrap = d.querySelector('.grid-wrap'); let left = 300; const writes = [];
    Object.defineProperty(wrap, 'scrollLeft', { configurable: true, get() { return left; }, set(v) { writes.push(v); left = v; } });
    const btn = d.querySelectorAll('.grid tbody tr')[0].querySelectorAll('.cell-btn')[0];
    const th = btn.closest('tr').querySelector('th');
    btn.getBoundingClientRect = () => ({ left: 50, right: 90, top: 0, bottom: 30, width: 40, height: 30 });
    th.getBoundingClientRect = () => ({ left: 0, right: 120, top: 0, bottom: 30, width: 120, height: 30 });
    btn.focus(); await sleep(50);
    record('J6', writes.length > 0 && left <= 300 - 70, { scrollLeftWrites: writes, finalScrollLeft: left, note: 'stubbed geometry; real layout unverified' });
    w.close();
  },
  // C06: a status filter shows its count and tells, in each example it empties, that nothing matches.
  async J7() {
    const w = load(); const d = w.document; await sleep(50);
    Array.from(d.querySelectorAll('.row-tools .filter')).find(b => b.getAttribute('data-filter') === 'published').click(); await sleep(50);
    const empty = d.querySelector('details.row[data-filter-empty]');
    const note = empty && empty.querySelector('.filter-empty-note');
    const count = d.querySelector('.row-tools [role="status"]');
    const o = { emptyRows: d.querySelectorAll('details.row[data-filter-empty]').length, note: note && !note.hidden ? note.textContent : null,
                count: count && count.textContent, countVisuallyHidden: !!(count && count.closest('.visually-hidden')) };
    // and clearing the filter removes the notes
    Array.from(d.querySelectorAll('.row-tools .filter')).find(b => b.getAttribute('data-filter') === 'published').click(); await sleep(50);
    o.notesAfterClear = Array.from(d.querySelectorAll('.filter-empty-note')).filter(n => !n.hidden).length;
    record('J7', !!o.note && !o.countVisuallyHidden && /Showing/.test(o.count || '') && o.notesAfterClear === 0, o);
    w.close();
  },
  // C08: unknown or stale scopes and statuses in the address are dropped, not shown as an unexplained empty result.
  async J8() {
    const out = {}; let ok = true;
    for (const qs of ['?in=bogus', '?status=bogus', '?status=Checked', '?q=koszul&in=bogus', '?show=bogus']) {
      const w = load({ search: qs }); const d = w.document; await sleep(500);
      const o = { count: d.querySelector('.find-count').textContent, search: w.location.search, hits: d.querySelectorAll('.find-link').length };
      out[qs] = o;
      if (/Nothing on this page/.test(o.count) || /bogus|Checked/.test(o.search)) ok = false;
      w.close();
    }
    record('J8', ok, out);
  },
  // C05: the row link in a cell card reads as the grid's row name.
  async J9() {
    const w = load(); const d = w.document; await sleep(50);
    const b = d.querySelector('.grid .cell-btn[data-row="row-w-algebras"]') || d.querySelector('.grid .cell-btn');
    b.click();
    const more = d.querySelector('#card .card-more');
    const grid = d.querySelector('.grid tbody th a[href="#' + b.getAttribute('data-row') + '"]');
    // what a reader sees: annotation text is not rendered, so it is removed on both sides
    record('J9', !!more && textNoTex(more) === textNoTex(grid) && !/\\\(|\\\)/.test(more.textContent), { cardLink: more && textNoTex(more), cardLinkTextContent: more && more.textContent.slice(0, 60), gridText: textNoTex(grid) });
    w.close();
  },
  // C13: words visible in the lead, the key and the section introductions are found.
  async J10() {
    const w = load(); const d = w.document; await sleep(50);
    const input = d.getElementById('find-q'); input.focus();
    const out = {}; let ok = true;
    for (const q of ['comultiplication', 'status marks', 'strongest status']) {
      input.value = q; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
      out[q] = d.querySelector('.find-count').textContent;
      if (/Nothing on this page/.test(out[q])) ok = false;
    }
    record('J10', ok, out);
    w.close();
  },
  // C14: a bare '/' on a control does not move focus; the bar's opener reaches the search.
  async J11() {
    const w = load(); const d = w.document; await sleep(50);
    const chip = d.querySelector('.row-tools .filter'); chip.focus();
    key(w, chip, '/');
    const afterSlash = desc(d.activeElement);
    const opener = d.querySelector('[data-find-open]');
    let viaOpener = null;
    if (opener && !opener.hidden) { opener.click(); viaOpener = desc(d.activeElement); }
    record('J11', afterSlash.startsWith('button.filter') && !!viaOpener && viaOpener.startsWith('input#find-q'), { afterSlash, openerShown: !!opener && !opener.hidden, viaOpener });
    w.close();
  },
  // C23: the card has a close control that closes it and returns focus to its trigger; Escape from inside the card does the same.
  async J12() {
    const w = load(); const d = w.document; await sleep(50);
    const term = d.querySelector('main .statement .term'); term.focus(); term.click();
    const close = d.querySelector('#card .card-close');
    const o = { opened: !d.getElementById('card').hidden, closeControl: !!close, closeName: close && close.getAttribute('aria-label') };
    if (close) { close.click(); o.closedByControl = d.getElementById('card').hidden; o.focusAfterClose = desc(d.activeElement); }
    term.click(); const link = d.querySelector('#card a[href]'); if (link) { link.focus(); key(w, link, 'Escape'); o.escapeFromCardFocus = desc(d.activeElement); }
    record('J12', o.opened && o.closeControl && o.closedByControl === true && d.activeElement === term, o);
    w.close();
  },
  // A2-A1-01: every role=status region stays rendered (not display:none) while empty, so its first message is announced.
  async J13() {
    const w = load(); const d = w.document; await sleep(50);
    const state = () => Array.from(d.querySelectorAll('[role="status"]')).map(el => el.className + '=' + w.getComputedStyle(el).display);
    const atLoad = state();
    const pub = Array.from(d.querySelectorAll('.row-tools .filter')).find(b => b.getAttribute('data-filter') === 'published');
    pub.click(); const filtered = state(); pub.click();
    const input = d.getElementById('find-q'); input.focus(); input.value = 'koszul'; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
    input.value = ''; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
    const cleared = state();
    const all = [...atLoad, ...filtered, ...cleared];
    record('J13', all.length > 0 && all.every(x => !/=none$/.test(x)), { atLoad, filtered, cleared });
    w.close();
  },
  // A2-A1-04: a pointer press on a mark does not scroll the table under it (only keyboard focus is corrected).
  async J6b() {
    const w = load(); const d = w.document; await sleep(50);
    const wrap = d.querySelector('.grid-wrap'); let left = 300; const writes = [];
    Object.defineProperty(wrap, 'scrollLeft', { configurable: true, get() { return left; }, set(v) { writes.push(v); left = v; } });
    const btn = d.querySelectorAll('.grid tbody tr')[1].querySelectorAll('.cell-btn')[0];
    btn.getBoundingClientRect = () => ({ left: 50, right: 90, top: 0, bottom: 30, width: 40, height: 30 });
    btn.closest('tr').querySelector('th').getBoundingClientRect = () => ({ left: 0, right: 120, top: 0, bottom: 30, width: 120, height: 30 });
    btn.dispatchEvent(new w.MouseEvent('mousedown', { bubbles: true })); btn.focus(); await sleep(50);
    const afterPress = writes.length;
    key(w, btn, 'ArrowDown'); await sleep(50);
    record('J6b', afterPress === 0, { writesAfterPointerFocus: afterPress, writesAfterKeyboard: writes.length - afterPress, note: 'stubbed geometry' });
    w.close();
  },
  // A2-A1-03: while a filter is on, each row summary says how many of its statements are shown; print shows full counts.
  async J7b() {
    const w = load(); const d = w.document; await sleep(50);
    const row = d.getElementById('row-heisenberg'); const words = () => row.querySelector('summary .row-count').firstChild.nodeValue;
    const before = words();
    const pub = Array.from(d.querySelectorAll('.row-tools .filter')).find(b => b.getAttribute('data-filter') === 'published');
    pub.click(); const filtered = words();
    w.dispatchEvent(new w.Event('beforeprint')); const printing = words(); w.dispatchEvent(new w.Event('afterprint')); const afterPrint = words();
    pub.click(); const cleared = words();
    record('J7b', /^0 of /.test(filtered) && printing === before && afterPrint === filtered && cleared === before, { before, filtered, printing, afterPrint, cleared });
    w.close();
  },
  // A3-V-11, A4-V-01 and A5-V-01: each edge of the bar fades only while more links lie beyond it: not when the links fit,
  // not at an edge the list has reached (logic with stubbed widths; the fades themselves are PIC-05, PIC-19, PIC-22).
  async J14() {
    const w = load(); const d = w.document; await sleep(50);
    const nav = d.querySelector('.nav'); let scroll = 800, client = 700, left = 0;
    Object.defineProperty(nav, 'scrollWidth', { configurable: true, get: () => scroll });
    Object.defineProperty(nav, 'clientWidth', { configurable: true, get: () => client });
    Object.defineProperty(nav, 'scrollLeft', { configurable: true, get: () => left, set: v => { left = v; } });
    w.dispatchEvent(new w.Event('resize')); const narrow = nav.classList.contains('nav-overflow');
    const startAtStart = nav.classList.contains('nav-overflow-start');
    left = 100; nav.dispatchEvent(new w.Event('scroll')); const atEnd = nav.classList.contains('nav-overflow');
    const startAtEnd = nav.classList.contains('nav-overflow-start');
    left = 40; nav.dispatchEvent(new w.Event('scroll')); const midway = nav.classList.contains('nav-overflow');
    const startMidway = nav.classList.contains('nav-overflow-start');
    left = 0; client = 900; w.dispatchEvent(new w.Event('resize')); const wide = nav.classList.contains('nav-overflow');
    const startWide = nav.classList.contains('nav-overflow-start');
    // A5-V-01: the left edge is marked while links lie to the left.
    record('J14', narrow && !atEnd && midway && !wide && !startAtStart && startAtEnd && startMidway && !startWide,
      { right: { atStart: narrow, atEnd, midway, fitting: wide }, left: { atStart: startAtStart, atEnd: startAtEnd, midway: startMidway, fitting: startWide },
        note: 'stubbed widths' });
    w.close();
  },
  // A3-V-12 and A3-V-13: with no filter on, the count line is announced but not shown; while filtered, a row hides its unfiltered mix.
  async J15() {
    const w = load(); const d = w.document; await sleep(50);
    const pub = Array.from(d.querySelectorAll('.row-tools .filter')).find(b => b.getAttribute('data-filter') === 'published');
    const count = d.querySelector('.row-tools [role="status"]'); const mix = d.querySelector('#row-heisenberg summary .row-count .mix');
    pub.click(); const on = { countHidden: count.classList.contains('visually-hidden'), mixHidden: mix.hidden, text: count.textContent };
    pub.click(); const off = { countHidden: count.classList.contains('visually-hidden'), mixHidden: mix.hidden, text: count.textContent,
      position: w.getComputedStyle(count).position };
    record('J15', !on.countHidden && on.mixHidden && off.countHidden && !off.mixHidden && /Showing all/.test(off.text), { on, off });
    w.close();
  },
  // A3-F-06 and A4-V-03: without the script that wires it, the card's Close control is neither shown nor focusable (an
  // inert template, or a hidden button); with the script it is in the card, visible, and closes it.
  async J16() {
    const s = new JSDOM(HTML).window; const staticClose = s.document.querySelector('#card .card-close');
    const tpl = s.document.querySelector('#card template.card-close-template');
    const withoutScript = { inDocument: !!staticClose, hidden: !!staticClose && staticClose.hidden,
      template: !!tpl && !!tpl.content.querySelector('.card-close') };
    withoutScript.present = withoutScript.inDocument || withoutScript.template;
    withoutScript.hidden = withoutScript.inDocument ? withoutScript.hidden : withoutScript.template;
    s.close();
    const w = load(); const d = w.document; await sleep(50);
    const close = d.querySelector('#card .card-close');
    const term = d.querySelector('main .statement .term'); term.focus(); term.click();
    const withScript = { hidden: !!close && close.hidden, opened: !d.getElementById('card').hidden };
    if (close) { close.click(); withScript.closed = d.getElementById('card').hidden; }
    record('J16', withoutScript.present && withoutScript.hidden && !withScript.hidden && withScript.opened && withScript.closed === true,
      { withoutScript, withScript });
    w.close();
  },
  // A4-V-03: with the foundation patch alone (--foundation-only <page>), Tab from a pinned term and from a pinned column
  // head behaves as on the baseline (--baseline <page>): no hidden control takes the card's first place.
  async J17() {
    if (!args['foundation-only'] || !args.baseline) { console.log('SKIP J17 (needs --foundation-only and --baseline)'); return; }
    const probe = file => {
      const page = fs.readFileSync(file, 'utf8'); const vc = new VirtualConsole();
      const w = new JSDOM(page, { url: BASE, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
        beforeParse(x) { x.matchMedia = q => ({ matches: false, media: q, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
                         x.HTMLElement.prototype.scrollIntoView = function () {}; x.Element.prototype.scrollTo = function () {}; x.scrollTo = function () {}; } }).window;
      return w;
    };
    const run = async file => {
      const w = probe(file); const d = w.document; await sleep(80); const o = {};
      const term = d.querySelector('main .statement .term'); term.focus(); term.click();
      const e1 = key(w, term, 'Tab'); const to1 = d.activeElement;
      o.term = { prevented: e1.defaultPrevented, focus: desc(to1), focusHidden: !!(to1 && (to1.hidden || (to1.closest && to1.closest('[hidden]')))) };
      key(w, d.activeElement, 'Escape');
      const head = d.querySelector('.col-head'); head.focus(); head.click();
      const e2 = key(w, head, 'Tab'); const to2 = d.activeElement;
      o.head = { prevented: e2.defaultPrevented, focus: desc(to2), focusHidden: !!(to2 && (to2.hidden || (to2.closest && to2.closest('[hidden]')))) };
      o.visibleClose = !!Array.from(d.querySelectorAll('#card .card-close')).find(b => !b.hidden);
      w.close(); return o;
    };
    const base = await run(args.baseline); const fo = await run(args['foundation-only']);
    const same = JSON.stringify(base.term) === JSON.stringify(fo.term) && JSON.stringify(base.head) === JSON.stringify(fo.head);
    record('J17', same && !fo.term.focusHidden && !fo.head.focusHidden && !fo.visibleClose, { baseline: base, foundationOnly: fo });
  },
  // Regression guards: behaviour that worked on the baseline must keep working.
  async R1() { // deep link into a closed row opens it
    const w = load({ hash: '#s-principal-collar-pentagon' }); const d = w.document; await sleep(150);
    const t = d.getElementById('s-principal-collar-pentagon');
    let closed = false; for (let p = t && t.parentElement; p; p = p.parentElement) if (p.localName === 'details' && !p.open) closed = true;
    record('R1', !!t && !closed, { exists: !!t, closedAncestor: closed });
    w.close();
  },
  async R2() { // a filter hiding the hash target is lifted on arrival
    const w = load({ search: '?show=open', hash: '#s-principal-collar-pentagon' }); const d = w.document; await sleep(150);
    const t = d.getElementById('s-principal-collar-pentagon');
    record('R2', !!t && !t.hidden && !t.closest('details:not([open])'), { hidden: t && t.hidden, pressed: Array.from(d.querySelectorAll('.row-tools .filter[aria-pressed="true"]')).map(b => b.getAttribute('data-filter')) });
    w.close();
  },
  async R3() { // tally link opens the search on that status with the tally's count
    const w = load(); const d = w.document; await sleep(50);
    const a = d.querySelector('.tally a[data-filter="checked"]'); const n = a.querySelector('.count').textContent;
    a.click(); await sleep(100);
    const count = d.querySelector('.find-count').textContent;
    record('R3', count === `${n} matches` && d.activeElement === d.getElementById('find-q'), { tally: n, count });
    w.close();
  },
  async R4() { // Open all in examples opens the rows and leaves the frontier's lists alone; Close all closes them
    const w = load(); const d = w.document; await sleep(50);
    d.querySelector('#examples [data-expand="all"]').click();
    const rowsOpen = d.querySelectorAll('details.row[open]').length, knownOpen = d.querySelectorAll('#frontier details.known[open]').length;
    d.querySelector('#examples [data-expand="none"]').click();
    record('R4', rowsOpen === d.querySelectorAll('details.row').length && knownOpen === 0 && d.querySelectorAll('details.row[open]').length === 0, { rowsOpen, knownOpen });
    w.close();
  },
  async R5() { // Escape in a search with a query clears it and keeps focus in the field
    const w = load(); const d = w.document; await sleep(50);
    const input = d.getElementById('find-q'); input.focus(); input.value = 'koszul'; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
    key(w, input, 'Escape'); await sleep(50);
    record('R5', input.value === '' && d.activeElement === input, { value: input.value, active: desc(d.activeElement) });
    w.close();
  },
  async R6() { // arrow keys move between grid marks
    const w = load(); const d = w.document; await sleep(50);
    const first = d.querySelector('.grid tbody .cell-btn'); first.focus();
    key(w, first, 'ArrowRight'); const right = d.activeElement;
    key(w, right, 'ArrowDown'); const down = d.activeElement;
    record('R6', right !== first && right.classList.contains('cell-btn') && down.closest('tr') !== right.closest('tr'), { right: desc(right), down: desc(down) });
    w.close();
  },
  async R7() { // Enter in the search goes to the first hit and opens it
    const w = load(); const d = w.document; await sleep(50);
    const input = d.getElementById('find-q'); input.focus(); input.value = 'collar pentagon'; input.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
    key(w, input, 'Enter'); await sleep(200);
    const t = w.location.hash && d.getElementById(w.location.hash.slice(1));
    record('R7', !!t && !t.closest('details:not([open])'), { hash: w.location.hash, search: w.location.search });
    w.close();
  },
  async R8() { // a term's card opens on focus, unpinned, and its trigger is marked expanded
    const w = load(); const d = w.document; await sleep(50);
    const term = d.querySelector('main .statement .term'); term.focus();
    const c = d.getElementById('card');
    record('R8', !c.hidden && term.getAttribute('aria-expanded') === 'true' && !!c.getAttribute('aria-labelledby'), { hidden: c.hidden, expanded: term.getAttribute('aria-expanded'), labelledby: c.getAttribute('aria-labelledby') });
    w.close();
  },
  async R9() { // print handlers open every disclosure and restore them afterwards
    const w = load(); const d = w.document; await sleep(50);
    const total = d.querySelectorAll('main details').length;
    w.dispatchEvent(new w.Event('beforeprint')); const during = d.querySelectorAll('main details[open]').length;
    w.dispatchEvent(new w.Event('afterprint')); const after = d.querySelectorAll('main details[open]').length;
    record('R9', during === total && after === 0, { total, during, after });
    w.close();
  },
};
for (const [id, fn] of Object.entries(checks)) {
  if (ONLY && !ONLY.has(id)) continue;
  try { await fn(); } catch (e) { record(id, false, { error: String(e && e.stack || e).slice(0, 300) }); }
}
results.pageErrors = pageErrors;
console.log('page errors (excluding jsdom not-implemented notices):', pageErrors.length, pageErrors.slice(0, 3));
if (args.out) fs.writeFileSync(args.out, JSON.stringify(results, null, 1) + '\n');
