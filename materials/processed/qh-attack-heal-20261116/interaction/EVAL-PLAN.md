# Interaction lane: precommitted evaluation plan

Committed 2026-11-16, before any production edit. Scope: `compiler/quantum-holography-status/status.js` and new
interaction tests. HTML/CSS changes are proposals for the foundation owner, never shared edits.

Baseline: the 13-file snapshot in `BASELINE.json` (status.js sha256 `ef3581907e17…`). Immutable copies are in
`baseline-src/` and the baseline no-fonts build is `baseline-build/baseline-nofonts.html` (sha256 in `baseline-src.sha256`).

## Acceptance checks (each must pass, or remain as a named residual that blocks convergence)

| ID | Behaviour under test | Check | Pass |
|---|---|---|---|
| E1 | Build and audit | `/tmp/qh-tracker-build-20261116-venv/bin/python -B compiler/build-quantum-holography-status.py --output <lane>/preview.html --audit-dir <lane>/audit` (final run with fonts) | exit 0, `PASS`, 0 failures, `math … (errors: 0)` |
| E2 | Content and status fidelity | content.json, essay.md, page.json, README.md hashes equal BASELINE.json; statement set (data-status, title text, body text), grid cell statuses and tally counts in the candidate page equal the baseline page | identical |
| E3 | Anchors | every static id of the baseline page and of the live edition (`baseline-build/ids-origin-master.txt`) exists in the candidate; every in-page `href="#…"` resolves; no duplicate id after script start and after each tested interaction | 0 missing, 0 broken, 0 duplicates |
| E4 | Offline and CSP | audit outside-reference checks; no `fetch`/XHR/beacon/WebSocket/EventSource/eval/`new Function` in status.js; CSP meta byte-identical | clean |
| E5 | Public-script hygiene | regex scan of status.js comments and strings for process, version, draft, phase, wave, lane, swarm, attack, model/tool names, internal paths | 0 hits |
| E6 | Real event flows (jsdom 28.1.0, `node compiler/quantum-holography-status/tests/interaction.test.cjs <page>`) | every test names a reader task; events are dispatched (click, keydown, input, focus, history.back/forward, hashchange, beforeprint/afterprint) | all pass, 0 jsdom/console errors |
| E7 | Large-page cost | jsdom timings for start-up, first index, per-keystroke search on representative queries (upper bound only); structural counts of layout reads per details toggle | no layout read over the whole page per toggle; per-keystroke search bounded; timings recorded |
| E8 | Visual and print | headless Chrome on the task-owned preview: widths 1400, 1024, 768, 480, 375; light and dark; reduced motion; keyboard focus; print A4 and Letter | inspected screenshots/PDFs, 0 console errors; any gap is a stated residual for root |
| E9 | Independent verification | a returned attacker or a distinct referee re-attacks the candidate against the ledger and the new code | no unhealed valid severity 1–3 entry |

## E6 reader tasks (minimum set)

1. Search finds reader-visible text in every part: lead, status key, section intros, statements (title, text, notes), question
   and why-it-matters text, related statements, rows (summary and column scopes), counterexamples, open groups, essay, terms,
   column definitions. Accents, case, curly quotes and dashes fold; quoted phrases; TeX typed with or without braces.
2. A query containing HTML or regex characters creates no element and throws no error.
3. Activating a result opens every closed disclosure around the unit, lifts a Show filter that hides it, focuses it, and gives
   the address an anchor for it; Back returns to the search view with focus on the activated result; Forward returns to the unit.
4. Arrival at each id kind (section, row, statement in a closed row, statement hidden by `?show=`, question, related statement,
   counterexample, open group, glossary entry, column definition) reveals the target. Arrival at an unknown, malformed or empty
   hash shows an explicit state with a way forward and no error. Unknown `?in=`, `?status=`, `?show=` values are ignored visibly
   or explicitly, never silently mismatched.
5. Escape closes the card and returns focus to its trigger; Clear and Escape in the search return focus to the field; Show all
   moves focus to the first newly shown result; a focused statement hidden by the filter does not strand focus.
6. The table of examples is one tab stop; arrow keys, Home/End move between its controls; Enter/Space open a mark's scope;
   Escape returns. A keyboard reader passes the table in a bounded number of Tab presses.
7. The Show filter states its empty rows visibly and offers a way back; filter state survives reload through `?show=`.
8. Print opens every disclosure and restores the reader's state afterwards, including a second print and print during a filter.
9. Theme toggling persists; every storage access survives a throwing or absent storage.
10. Reading state: what is remembered is optional, per device, survives absent storage, and never hides content.
11. Atlas isolation: a mock `[data-atlas-mount]` subtree is not indexed, filtered or bound by page-level handlers; its
    `qh:navigate` request reveals a page anchor with history and focus return; the page announces state with `qh:state`;
    an unknown anchor first dispatches a cancelable `qh:unknown-anchor`.
12. No-JS reading: with scripts off, every statement, cell scope (in its row), definition and column definition is present
    and not hidden; no required content exists only in script output.

## Negative cases

Unknown/malformed/empty hash; empty, one-character and whitespace queries; zero results; storage that throws; absent
IntersectionObserver, matchMedia, CSS Highlight API; absent atlas mount; content lacking optional sections (decisive,
frontier, failures, essay, terms) simulated by removing them from the DOM before the script runs.

## Blockers and residual policy

A behaviour that needs markup or style changes is delivered as a guarded patch proposal with before/after hashes, and the
status.js behaviour must still work on the current markup. Layout and timing claims that jsdom cannot decide are verified in
headless Chrome or recorded as residuals for root. Convergence follows the ledger-closure rule; quiet reviewers are not evidence.

## Amendment, 2026-11-16 (after the plan was committed; the text above is unchanged)

- E7 and E8 are bound by root's browser restriction (RESTRICTION-BROWSER.md): no raw CDP, headless browser, screenshot or
  other browser surface. E7 is measured in jsdom only (an upper bound with no layout) and by structural tests; E8 is not
  performed by this lane and is a stated requirement for root. Chrome results obtained before the restriction reached this
  lane are kept and are not evidence.
- Added E10: the same reader-task tests also run on builds that use the other lanes' current producer files (hashed
  snapshots in integration*/): the foundation's markup, the same with this lane's CSS proposal, the atlas lane's renderer
  on its synthetic fixture, and the baseline producer with this lane's status.py proposal.
- Added E11: with the status.py proposal, the ids the producer serves equal the ids status.js gives (scratch/probe-served-ids.cjs).
- The principal's materials rule (2026-11-16) applies: the page image is not judged here (restriction), so no visual
  readiness is claimed; second-wave reviewers receive the brief and root's messages verbatim and load the rulebook whole.
