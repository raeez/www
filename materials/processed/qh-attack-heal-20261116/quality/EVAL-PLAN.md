# Quality lane: precommitted evaluation plan

Committed 2026-11-16 before any healing. Applies to the unchanged baseline and to every candidate.
A check is passed only by its stated evidence. A check that cannot run is reported as not run, with the reason; it is never counted as passed.

## Inputs and tools

- Builder: the maintained `compiler/build-quantum-holography-status.py` only. Never the older tracker builder.
- Build command (candidate mirrors run the mirror's copy of the same builder):
  `/tmp/qh-tracker-build-20261116-venv/bin/python -B <root>/compiler/build-quantum-holography-status.py --output <quality>/…/preview.html --audit-dir <quality>/…/audit` (`--no-fonts` for quick runs; the final run keeps fonts).
- Browser: headless Google Chrome 157 driven over the DevTools protocol by `lead/qh-cdp.mjs`, with a private profile inside `quality/`. It loads only task-owned `file://` previews. No other tabs or windows are inspected.
- DOM without layout: jsdom 28 (read-only install outside this repository, path passed by the `QH_JSDOM` environment variable).
- Evidence files are written under `quality/` only.

## Reader tasks under test

T1 Find what is established, and how firmly, from the cover tally, the key and the principal results.
T2 Read one example row across the eight parts of the theory, open a mark's scope, and reach the row's statements.
T3 Share or follow a link to one statement, row, question, counterexample, open-problem group, term or column definition.
T4 Search the page, narrow by part and status, follow a result, and come back with Back.
T5 Filter the example rows by status, including a filter that matches nothing in some rows.
T6 Do T1–T5 by keyboard only and by screen reader names; on a phone (375 px, touch); in dark mode; with reduced motion.
T7 Print the page on A4 and on Letter and read every statement, row and formula on paper.

## Checks

| Id | Check | Evidence | Pass threshold |
|---|---|---|---|
| Q01 | Build and audit | builder exit code, `audit.txt` | exit 0, `PASS`, 0 failures, `math … (errors: 0)`; final run embeds 4 font faces |
| Q02 | Reader inputs preserved | sha256 of content.json, essay.md | equal to BASELINE.json unless root supplies newer reviewed content with its hashes |
| Q03 | Offline and CSP | CSP meta string; CDP Network and console log during load and all scripted scenarios | CSP equal to CONTRACT.json; 0 requests other than the page itself and data: URIs; 0 CSP reports |
| Q04 | Public safety, whole document | `lead/qh-static.py` scan of the full HTML (visible text, attributes, scripts, metadata) | 0 hits: content `source` values or their path fragments, private paths, closed-repository names (INVARIANTS §X regex), hex hashes ≥ 32 outside data: URIs, model/tool/session names, process/version/draft/phase/wave words, progress percentages |
| Q05 | External gate | external-documents scan and public-artifact-source scan on visible text | 0 hits |
| Q06 | Status fidelity | every content statement versus its rendered article; tally counts | data-status, chip label and counts equal content and page.json labels, 281 of 281 |
| Q07 | Grid fidelity | 20 × 8 cells versus content | every cell status, label and row-mark order equal content |
| Q08 | Mathematics fidelity | TeX segments versus `<math>` annotations, in order | 2502 of 2502 equal; 0 `code.tex-error` |
| Q09 | Anchors | ids from content id patterns; all in-page hrefs; duplicates | all expected anchors present, unique, resolving; a candidate keeps every baseline anchor for unchanged content |
| Q10 | Text completeness | math-free text of each statement, note, cell scope and claim versus the DOM | 0 dropped or truncated reader texts |
| Q11 | Widths and themes | CDP at 1400, 1024, 768, 480, 375 × light, dark | 0 page-level horizontal overflow; 0 elements past the viewport edge outside designated scroll boxes; screenshots retained |
| Q12 | Formula overflow | every `.math-display`/`.math-long` at 375 and 1400 | each overflowing box scrolls and is keyboard-reachable, or sits inside a control that is itself reachable; no clipped formula without a scroll route |
| Q13 | Contrast | computed colours of rendered text, marks, focus rings, placeholders, pressed chips, light and dark | WCAG 2.1 AA: text ≥ 4.5:1 (≥ 3:1 at 24 px, or 18.66 px bold); meaningful marks, focus indicators and control boundaries ≥ 3:1 |
| Q14 | Keyboard | CDP Tab walk from page start; widget key scripts | skip link first and visible; every stop has a visible indicator; no stop hidden under the sticky bar; Escape closes the card and restores focus; grid arrows move; no trap |
| Q15 | Names and structure | CDP accessibility tree | every button, link and field named; dialog named while shown; landmark names unique; no skipped heading level |
| Q16 | Deep links | each anchor class on arrival and on hashchange | target displayed (not in a closed details, not hidden), top inside the viewport and below the sticky bar |
| Q17 | Shared views and history | `?q`, `?in`, `?status`, `?show` on arrival; search, result, Back, Forward | state restored from the address; no exception on invalid values; Back after a result returns to the search state |
| Q18 | Empty states | a filter matching nothing in a row or on the page; a search with no hits | the reader is told in visible text; no empty disclosure presented as content |
| Q19 | Touch | coarse pointer, no hover, 375 px | term, cell and column cards open by tap as a bottom sheet and close by tap outside and Escape; controls other than inline text ≥ 24 × 24 px |
| Q20 | Reduced motion | `prefers-reduced-motion: reduce` | scroll behaviour auto; no transition or animation on interaction |
| Q21 | Print A4 and Letter | CDP `Page.printToPDF` for both sizes; print-media layout probe | PDF produced; every row, related statement, filtered statement and column definition printed; no formula or grid column clipped at the paper edge; no screen chrome printed |
| Q22 | Scale | 1× page and a 3× synthetic content build in `quality/` | build passes; first search ≤ 300 ms and filter ≤ 100 ms at 1× on this machine; 3× figures reported |
| Q23 | Console | CDP console and exceptions over all scenarios | 0 errors, 0 uncaught exceptions |
| Q24 | Atlas relation fidelity | CONTRACT.json `atlas_testability_requirements` against a candidate with atlas data | every drawn edge in the data with equal endpoints, direction and relation; dependency paths connected by data edges; editorial paths labelled; text equivalent present |

## Blockers and severities

- A failure of Q01–Q10, Q16–Q18, Q21 or Q23 is an attack of severity 1–3; Q04 and Q05 hits are severity 1.
- A failure of Q11–Q15, Q19 or Q20 is severity 2 when it breaks a reader task, otherwise 3 when it misses the WCAG 2.1 AA or layout requirement, otherwise 4.
- Q24 cannot pass before an atlas candidate exists. Until then it is an open obligation, not a pass.
- Screen-reader speech (VoiceOver, NVDA) cannot be produced here. Q15 tests the accessibility tree; speech output remains a stated gap for root.
- Convergence requires every severity 1–3 entry healed with re-run evidence, refuted with evidence, or recorded as outside this lane's closure with its owner; every child agent returned; and the external gate clean.

## Amendment after root's browser restriction (2026-11-16)

Root ruled headless Chrome over raw CDP (and any browser command or alternate browser surface) out of bounds for
this task (`RESTRICTION.md`). The thresholds above are unchanged. What changes is who can run each check:

- Runnable in this lane with admissible evidence: Q01, Q02, Q03 (CSP string and no-network rules, statically),
  Q04–Q10 (static checks of the built HTML), Q17 and Q18 (DOM state in jsdom, no layout), Q22 (build-time and
  script-free measures only), Q24 (data-level checks once atlas data exists).
- Partly runnable as DOM-only jsdom checks, without layout: Q14 (focus calls, key handlers, card state),
  Q15 (ARIA names and references; no accessibility-tree computation), Q16 (details opening and hash handling;
  no scroll position), Q19 (card markup and close control; no touch geometry).
- Not runnable in this lane: Q11, Q12, Q13 (rendered colours; token arithmetic is still done), Q20 (computed
  styles), Q21 (print), Q23 (browser console). These are open obligations for root through an approved route,
  for the baseline and for every candidate.
- Results produced by the earlier browser runs do not count toward any check.

## Amendment: visual acceptance (2026-11-16, after the principal's scope was reaffirmed)

The principal's scope is a core acceptance requirement alongside usability: "upgrading it visually, giving god tier
elite rhythm, harmony, balance, proportion, god tier communication, god tier visualization of our research and the
concepts and the totality of all we are doing." The checks VQ1 to VQ7 in VISUAL-ATTACK.md are added to this plan.
VQ1 to VQ5 and VQ7 are decided on the page image through the native Chrome integration on task-owned tabs (raw
CDP and headless runs remain prohibited); computed proxies only direct the review. VQ6 also requires Q24. Under the
principal's rule on materials, no builder grades its own page: each VQ result needs an independent reviewer's
reading of the same images.
