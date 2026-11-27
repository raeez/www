// Executable DOM contract between status.py (markup, foundation lane) and status.js (interaction lane).
//   node tools/run.mjs tools/contract.mjs <page.html> [--atlas]
// Each hook is asserted on the page after its script has run; each behaviour is exercised.
// Prints JSON {pass, hooks:[...], behaviours:[...], console:[...]}.
import { fileUrl } from './cdp.mjs';

// [selector, minimum count, note]. Counts are the baseline's lower bounds (281 statements, 34 questions,
// 20 rows, 160 cells, 144 glossary entries); the candidate must keep each hook at least this often.
export const HOOKS = [
  ['html', 1, 'data-theme attribute target; localStorage key qh-theme (head script and status.js)'],
  ['button.theme', 1, 'theme toggle'],
  ['#main', 1, 'skip-link target and search root'],
  ['a.skip[href="#main"]', 1, 'skip link'],
  ['#card[role="dialog"][hidden] > .card-inner', 1, 'single floating card for terms, cells, column heads'],
  ['button.term[data-term][aria-controls="card"][aria-expanded]', 100, 'glossary term trigger; data-term names a .gloss id'],
  ['.gloss[id^="term-"] > dt + dd', 144, 'term card content source'],
  ['#terms h2', 1, 'label of the card link to the glossary'],
  ['table.grid', 1, 'grid of examples: arrow keys, Home, End'],
  ['table.grid thead button.col-head[data-col][aria-controls="card"]', 8, 'column head trigger'],
  ['.col-def[id^="col-"] > dt + dd', 8, 'column card content source'],
  ['table.grid td.cell[data-status] > button.cell-btn[data-row][aria-controls="card"] + .cell-note[hidden]', 160, 'cell trigger and its note (sibling)'],
  ['table.grid tbody th a[href^="#row-"]', 20, 'row link; its text labels the card link'],
  ['details.row[id^="row-"] > summary', 20, 'example rows; summary click writes the address'],
  ['details.row .row-name', 20, 'search title of a row'],
  ['.rows .statement[data-status]', 100, 'statements filtered by status'],
  ['.row-tools', 1, 'live region parent for the row filter'],
  ['.filter[data-filter][aria-pressed]:not(.find .filter)', 3, 'row status filter chips'],
  ['[data-expand="all"]', 1, 'Open all (label copied for question sections)'],
  ['[data-expand="none"]', 1, 'Close all'],
  ['main section.section .questions', 2, 'question lists (Open all / Close all for details.known)'],
  ['.tally a[data-filter]', 3, 'status tally: search by status'],
  ['main > .tally', 1, 'search is inserted after it when no [data-find] mount exists'],
  ['.find[role="search"] #find-q', 1, 'search built by status.js'],
  ['.nav a[href^="#"]', 6, 'bar links: aria-current and section observer'],
  ['main .statement[data-status] .statement-head .status-chip .mark', 281, 'search status label and mark'],
  ['main .statement .statement-title', 200, 'search titles'],
  ['main .question[id^="q-"] h3', 34, 'question title (h3 .anchor) and number'],
  ['main .question .question-num .question-num-label', 34, 'question number label (skipped in titles)'],
  ['main .question > .statement, main .question > .question-ask > .statement', 34, 'a question\'s own statement: direct child or inside .question-ask'],
  ['main .failure[id] .claim-text', 11, 'counterexample claim'],
  ['main .failure > .statement', 11, 'counterexample witness'],
  ['main .open-group[id] h3', 4, 'open-problem group'],
  ['main .col-def dt', 8, 'search unit'],
  ['#essay-title', 1, 'essay title'],
  ['main .essay > p:not(.essay-byline)', 20, 'essay paragraphs (search units)'],
  ['main .essay-lead', 1, 'essay lead'],
  ['main .gloss dt', 144, 'glossary search units'],
  ['.math-display, .math-long', 50, 'scrollable formulas get tabindex when wide'],
  ['section#results, section#examples, section#open', 3, 'search scopes (also decisive, frontier, failures, essay, terms when present)'],
];

// Structures added by the foundation lane (asserted with --candidate; the baseline has none of them).
export const NEW_HOOKS = [
  ['main > nav.contents[aria-labelledby="contents-label"] ol > li > a[href^="#"]', 9, 'contents: every built section by its heading, with counts'],
  ['main > section.questions-section.wide', 2, 'every question section uses the same card layout'],
  ['.question.compare > .question-ask > .question-ask-label + .statement', 34, 'the labelled question part; the statement stays a direct child of .question-ask'],
  ['.question-known > ul.statements.known-list > li.fold-item > details.known.fold > summary.fold-head', 105, 'related statement line (mark, title, status)'],
  ['details.known.fold > article.statement[data-status][id^="s-"]', 105, 'the related statement inside its line keeps its markup and anchor'],
  ['.statement-head > .statement-context > a[href^="#"]', 227, 'where a statement stands; shown for :target only; inside .statement-head so search skips it'],
  ['.q-index-head > .q-index-label[id]', 2, 'question index label (named landmark)'],
  ['.bar button.find-open[data-find-open]', 1, 'search control in the bar (status.js binds [data-find-open])'],
  ['.grid-legend .legend-key a[href="#status"]', 1, 'grid legend links to the key'],
  ['.cell-note > .cell-note-head + .cell-note-text', 160, 'the note follows the head (card description)'],
  ['.cell-note > .cell-note-meaning', 160, 'meaning of the cell status, after the note'],
  ['button.col-head > .col-head-text', 8, 'column heading text (turns upright at <=760px)'],
  ['section#terms.terms-section > nav.gloss-index a[href^="#term-"]', 2, 'glossary letter index'],
];

const NEW_BEHAVIOURS = `(async () => {
  const out = [];
  const t = (name, ok, detail) => out.push({ name, pass: !!ok, detail: detail === undefined ? '' : String(detail) });
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  const fold = document.querySelector('details.fold');
  fold.querySelector('summary').click(); await wait(20);
  t('a related statement line opens to its statement', fold.open && fold.querySelector('.statement-text').getClientRects().length > 0);
  fold.querySelector('summary').click(); await wait(20);
  t('and closes again', !fold.open);
  const head = fold.querySelector('.statement > .statement-head');
  t('inside a closed or open line the statement heading is drawn by the line', getComputedStyle(head).display === 'none');
  document.querySelector('.bar [data-find-open]').click(); await wait(150);
  t('the bar search control focuses the search', document.activeElement && document.activeElement.id === 'find-q');
  document.activeElement.blur();
  const ctx = document.querySelector('.statement-context');
  t('a context line is hidden while its statement is not the target', getComputedStyle(ctx).display === 'none');
  const dec = document.querySelector('#decisive [data-expand="all"]');
  t('the decisive questions get Open all from status.js', !!dec);
  return out;
})()`;

const BEHAVIOURS = `(async () => {
  const out = [];
  const t = (name, ok, detail) => out.push({ name, pass: !!ok, detail: detail === undefined ? '' : String(detail) });
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  const card = document.getElementById('card');
  // Cell card.
  const cell = document.querySelector('.cell-btn');
  cell.click(); await wait(30);
  t('cell click opens the card with its note', !card.hidden && card.querySelector('.cell-note-head') && cell.getAttribute('aria-expanded') === 'true');
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); await wait(30);
  t('Escape closes the card', card.hidden && cell.getAttribute('aria-expanded') === 'false');
  // Term card.
  const term = document.querySelector('button.term');
  term.click(); await wait(30);
  t('term click opens its definition', !card.hidden && card.querySelector('.card-term') && card.querySelector('.card-more'));
  term.click(); await wait(30);
  t('second click closes it', card.hidden);
  // Column head card.
  const col = document.querySelector('.col-head');
  col.click(); await wait(30);
  t('column head opens its definition', !card.hidden && card.querySelector('.card-term'));
  document.body.click(); await wait(30);
  t('click elsewhere closes the card', card.hidden);
  // Row filter.
  const f = [...document.querySelectorAll('.row-tools .filter[data-filter]')].find((b) => b.getAttribute('data-filter') === 'open') ||
            document.querySelector('.row-tools .filter[data-filter]');
  const st = f.getAttribute('data-filter');
  f.click(); await wait(30);
  const rs = [...document.querySelectorAll('.rows .statement')];
  const wrong = rs.filter((s) => !s.hidden && s.getAttribute('data-status') !== st).length;
  t('row filter hides other statuses', f.getAttribute('aria-pressed') === 'true' && wrong === 0 && rs.some((s) => !s.hidden), st + ' wrong=' + wrong);
  f.click(); await wait(30);
  t('row filter off shows all', rs.every((s) => !s.hidden));
  // Open all / Close all in the examples.
  const ex = document.querySelector('#examples [data-expand="all"]');
  ex.click(); await wait(20);
  t('Open all opens every row', [...document.querySelectorAll('details.row')].every((d) => d.open));
  document.querySelector('#examples [data-expand="none"]').click(); await wait(20);
  t('Close all closes every row', [...document.querySelectorAll('details.row')].every((d) => !d.open));
  // Question sections: known toolbars or always-visible related lists.
  const knownSections = [...document.querySelectorAll('main section.section')].filter((s) => s.querySelector('.questions') && s.querySelectorAll('details.known').length >= 2);
  const toolbars = knownSections.filter((s) => s.querySelector('[data-expand]')).length;
  t('each question section with two or more related-statement disclosures has Open all / Close all', toolbars === knownSections.length, knownSections.length + ' sections');
  for (const s of knownSections) {
    s.querySelector('[data-expand="all"]').click(); await wait(10);
    const ok = [...s.querySelectorAll('details.known')].every((d) => d.open);
    s.querySelector('[data-expand="none"]').click(); await wait(10);
    const closed = [...s.querySelectorAll('details.known')].every((d) => !d.open);
    t('Open all / Close all in #' + s.id, ok && closed);
  }
  // Hash navigation into a closed disclosure opens it.
  const inside = [...document.querySelectorAll('details:not([open]) [id^="s-"]')][0];
  if (inside) {
    location.hash = inside.id; await wait(120);
    let open = true;
    for (let d = inside.parentElement; d; d = d.parentElement) if (d.localName === 'details' && !d.open) open = false;
    t('a link to a statement inside a closed disclosure opens it', open, inside.id);
    history.replaceState(null, '', location.pathname);
  } else t('a link to a statement inside a closed disclosure opens it', true, 'no statement inside a closed disclosure');
  // Print opens every disclosure and restores it.
  const before = [...document.querySelectorAll('main details')].map((d) => d.open);
  window.dispatchEvent(new Event('beforeprint')); await wait(10);
  const allOpen = [...document.querySelectorAll('main details')].every((d) => d.open);
  window.dispatchEvent(new Event('afterprint')); await wait(10);
  const restored = [...document.querySelectorAll('main details')].every((d, i) => d.open === before[i]);
  t('beforeprint opens every disclosure; afterprint restores', allOpen && restored);
  // Tally link searches by status.
  const tl = document.querySelector('.tally a[data-filter]');
  tl.click(); await wait(150);
  const input = document.getElementById('find-q');
  const hits = document.querySelectorAll('#find-results .find-link').length;
  t('tally link lists statements of its status in the search', hits > 0 && document.activeElement === input, hits + ' hits');
  input.value = ''; input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); await wait(50);
  // Search finds a statement title and jumps to it.
  const title = document.querySelector('main .principal .statement-title, main .statement-title');
  const word = (title.textContent.match(/[A-Za-z]{6,}/) || ['the'])[0];
  input.focus(); input.value = word; input.dispatchEvent(new Event('input', { bubbles: true })); await wait(200);
  t('search for a title word returns hits', document.querySelectorAll('#find-results .find-link').length > 0, word);
  input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); await wait(30);
  // Theme toggle.
  const before2 = document.documentElement.getAttribute('data-theme');
  document.querySelector('.theme').click();
  const after2 = document.documentElement.getAttribute('data-theme');
  t('theme button sets data-theme', after2 === 'dark' || after2 === 'light', before2 + ' -> ' + after2);
  document.documentElement.removeAttribute('data-theme');
  try { localStorage.removeItem('qh-theme'); } catch (e) {}
  // Grid arrow keys.
  const first = document.querySelector('.grid tbody td .cell-btn');
  first.focus();
  first.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true })); await wait(10);
  const moved = document.activeElement !== first && document.activeElement.classList.contains('cell-btn');
  t('ArrowRight moves to the next mark in the grid', moved);
  return out;
})()`;

export default async function (b, [pagePath, mode]) {
  const p = await b.page({ width: 1400, height: 900, scheme: 'light' });
  await p.goto(fileUrl(pagePath), 600);
  const hooks = [];
  for (const [sel, min, note] of HOOKS.concat(mode === '--candidate' ? NEW_HOOKS : [])) {
    const n = await p.eval(`document.querySelectorAll(${JSON.stringify(sel)}).length`);
    hooks.push({ selector: sel, count: n, min, pass: n >= min, note });
  }
  const behaviours = await p.eval(BEHAVIOURS);
  const log = p.log.slice();
  await p.close();
  if (mode === '--candidate') {
    // A fresh load: the behaviours above leave a statement as the target and a disclosure open.
    const q = await b.page({ width: 1400, height: 900, scheme: 'light' });
    await q.goto(fileUrl(pagePath), 600);
    behaviours.push(...await q.eval(NEW_BEHAVIOURS));
    log.push(...q.log);
    await q.close();
  }
  const pass = hooks.every((h) => h.pass) && behaviours.every((x) => x.pass) && log.filter((l) => l.kind !== 'log.warning').length === 0;
  return { pass, failedHooks: hooks.filter((h) => !h.pass), failedBehaviours: behaviours.filter((x) => !x.pass), hooks, behaviours, console: log };
}
