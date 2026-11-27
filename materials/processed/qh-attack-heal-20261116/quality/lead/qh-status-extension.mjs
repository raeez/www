// Behaviour of a statement status added to the contract ('refuted form', atlas scoped_negative) on a built page whose
// content uses it (the builder fixture refuted-form): filter, address round trip, tally link and search facet, search in
// hypotheses, accessible names, and no coercion to another status. Page script run in jsdom; no layout.
// Usage: QH_JSDOM=<jsdom> node qh-status-extension.mjs --html <page> [--status "refuted form"] [--word "finite length"] [--out <json>]
// Reads only; writes only --out.
import fs from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { JSDOM, VirtualConsole } = require(process.env.QH_JSDOM || 'jsdom');
const args = {};
for (let i = 2; i < process.argv.length; i += 2) args[process.argv[i].replace(/^--/, '')] = process.argv[i + 1];
const HTML = fs.readFileSync(args.html, 'utf8');
const STATUS = args.status || 'refuted form';
const WORD = args.word || 'finite length';
const BASE = 'https://example.test/quantum-holography-tracker.html';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const pageErrors = [];
const results = {};
const record = (id, pass, observed) => { results[id] = { pass, observed }; console.log(`${pass ? 'PASS' : 'FAIL'} ${id} ${JSON.stringify(observed).slice(0, 400)}`); };

function load(search = '') {
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented/.test(String(e && e.message))) pageErrors.push(String(e && e.message).slice(0, 200)); });
  const dom = new JSDOM(HTML, {
    url: BASE + search, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) {
      w.matchMedia = q => ({ matches: false, media: q, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
      w.HTMLElement.prototype.scrollIntoView = function () {};
      w.Element.prototype.scrollTo = function () {};
      w.scrollTo = function () {};
    }
  });
  return dom.window;
}
const rowFilter = d => [...d.querySelectorAll('.row-tools .filter[data-filter]')].find(b => b.getAttribute('data-filter') === STATUS);
const visibleRowStatuses = d => [...d.querySelectorAll('.rows .statement')].filter(s => !s.hidden).map(s => s.getAttribute('data-status'));

// S1 rendering and accessible names: chips name the status in text; marks are decorative there; the mix names it.
{
  const w = load(); const d = w.document; await sleep(50);
  const arts = [...d.querySelectorAll(`main article.statement[data-status="${STATUS}"]`)];
  const chips = arts.map(a => a.querySelector('.status-chip'));
  const label = chips[0] ? chips[0].textContent.trim() : null;
  const marksHidden = chips.every(c => c && c.querySelector('svg.mark') && c.querySelector('svg.mark').getAttribute('aria-hidden') === 'true');
  const mix = d.querySelector(`.row-count .mix .mix-${STATUS.replace(/ /g, '-')}`);
  const mixName = mix ? mix.textContent.replace(/\s+/g, ' ').trim() : null;
  const b = rowFilter(d);
  const inRows = d.querySelectorAll(`.rows .statement[data-status="${STATUS}"]`).length;
  const hyp = arts.map(a => a.querySelectorAll(':scope > .statement-hypotheses li, :scope > .statement-hyp li').length);  // either markup (A8-F-01)
  // A row filter and a row mix entry exist exactly when an example row has such a statement (A7-V-04).
  // Row mixes exist only in the older markup; F2 shows statuses in fold lines instead, so a mix is required only where
  // the page uses mixes (A8-F-01).
  const mixesUsed = !!d.querySelector('.row-count .mix');
  const rowsOk = inRows ? (!!b && b.textContent.trim() === label && (!mixesUsed || (!!mixName && mixName.includes(label)))) : (!b && !mixName);
  record('S1', arts.length > 0 && !!label && marksHidden && rowsOk && hyp.every(n => n > 0),
    { statements: arts.length, inRows, chipLabel: label, marksHidden, filterName: b && b.textContent.trim(), mixName, hypotheses: hyp });
  w.close();
}
// S2 the filter shows exactly those statements, says so, and writes the address.
{
  const w = load(); const d = w.document; await sleep(50);
  const b = rowFilter(d);
  if (!b) record('S2', !d.querySelector(`.rows .statement[data-status="${STATUS}"]`), { note: 'no example row has the status, so no row filter' });
  else {
    b.click(); await sleep(20);
    const shown = visibleRowStatuses(d);
    const count = d.querySelector('.row-tools [role="status"]');
    record('S2', shown.length > 0 && shown.every(s => s === STATUS) && /show=/.test(w.location.search) &&
      new URLSearchParams(w.location.search).get('show') === STATUS && b.getAttribute('aria-pressed') === 'true',
      { shown: shown.length, statuses: [...new Set(shown)], search: w.location.search, count: count && count.textContent });
  }
  w.close();
}
// S3 the address round trip (a space in the value) restores the filter at arrival.
{
  const w = load('?show=' + encodeURIComponent(STATUS)); const d = w.document; await sleep(80);
  const b = rowFilter(d); const shown = visibleRowStatuses(d);
  if (!b) record('S3', !d.querySelector(`.rows .statement[data-status="${STATUS}"]`), { note: 'no row filter; the address value is dropped', search: w.location.search });
  else record('S3', b.getAttribute('aria-pressed') === 'true' && shown.length > 0 && shown.every(s => s === STATUS),
    { pressed: b.getAttribute('aria-pressed'), shown: shown.length });
  w.close();
}
// S4 the tally link opens the search on that status with the tally's count.
{
  const w = load(); const d = w.document; await sleep(50);
  const a = [...d.querySelectorAll('.tally a[data-filter]')].find(x => x.getAttribute('data-filter') === STATUS);
  // A pill shows its count, or (F2) none: then the statements of the status on the page are the count (A8-F-01).
  const shown = a && a.querySelector('.count');
  const n = a ? (shown ? shown.textContent : String(d.querySelectorAll(`main article.statement[data-status="${STATUS}"]`).length)) : null;
  if (a) a.click(); await sleep(120);
  const facet = [...d.querySelectorAll('.find .filter[data-status-facet]')].find(f => f.getAttribute('data-status-facet') === STATUS);
  const count = d.querySelector('.find-count');
  const want = +n === 1 ? '1 match' : `${n} matches`;
  record('S4', !!a && !!facet && facet.getAttribute('aria-pressed') === 'true' && !!count && count.textContent === want,
    { tally: n, facetPressed: facet && facet.getAttribute('aria-pressed'), count: count && count.textContent });
  w.close();
}
// S5 search reaches the words of the hypotheses and returns the scoped negative statement.
{
  const w = load('?q=' + encodeURIComponent(WORD)); const d = w.document; await sleep(150);
  const hits = [...d.querySelectorAll('.find-results .find-hit')];
  // A question's own statement is found through its question card (#q-...); any other through its own anchor.
  const ASKED = ':scope > .statement, :scope > .question-ask > .statement';
  const ids = [...d.querySelectorAll(`main article.statement[data-status="${STATUS}"]`)].map(a => {
    const q = a.closest('.question');
    return q && q.querySelector(ASKED) === a ? '#' + q.id : (a.id ? '#' + a.id : null);
  }).filter(Boolean);
  const targets = hits.map(h => (h.querySelector('a[href^="#"]') || { getAttribute: () => '' }).getAttribute('href'));
  const found = ids.filter(id => targets.includes(id));
  record('S5', ids.length > 0 && found.length === ids.length, { hits: hits.length, statements: ids, found });
  w.close();
}
// S6 no coercion: no element shows the status as open, and the open tally equals the open statements.
{
  const w = load(); const d = w.document; await sleep(50);
  const openArts = d.querySelectorAll('main article.statement[data-status="open"]').length;
  const openTally = [...d.querySelectorAll('.tally a[data-filter]')].find(x => x.getAttribute('data-filter') === 'open');
  const wrong = [...d.querySelectorAll(`main article.statement[data-status="${STATUS}"]`)].filter(a => a.classList.contains('st-open')).length;
  const openCount = openTally && openTally.querySelector('.count');  // F2's pills carry no count (A8-F-01)
  record('S6', wrong === 0 && !!openTally && (!openCount || +openCount.textContent === openArts),
    { openStatements: openArts, openTally: openCount ? openCount.textContent : 'no count on the pill', shownAsOpen: wrong });
  w.close();
}
results.pageErrors = pageErrors;
const ok = Object.entries(results).filter(([k]) => k !== 'pageErrors').every(([, v]) => v.pass) && pageErrors.length === 0;
console.log(ok ? 'ALL PASS' : 'NOT ALL PASS', 'page errors:', pageErrors.length);
if (args.out) fs.writeFileSync(args.out, JSON.stringify({ html: args.html, status: STATUS, results, all_pass: ok }, null, 1) + '\n');
