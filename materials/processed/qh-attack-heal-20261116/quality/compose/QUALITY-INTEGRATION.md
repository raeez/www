# Quality lane: what root's integration already holds, and the remaining delta

> Superseded for root's composition by `f2-package/` (the same quality hunks against the foundation's final F1+F2
> bytes; STATUS-LANGUAGE.diff withdrawn, superseded by F1). Base correction: root carries the baseline status.js
> (ef358190…); interaction candidate-r3 below was a planned reference, not installed in root.

Staging area: `materials/processed/qh-attack-heal-20261116/quality/compose/` (this lane's only). Nothing in the
foundation, interaction, atlas or integration trees was edited; their files were read and copied.

## Base: the files root has integrated (`reference/`, pins in `reference/REFERENCE-PINS.json`)

| File | sha256 | From |
|---|---|---|
| compiler/quantum-holography-status/status.py | da6f2c36… | foundation snapshot (GUARD c9d1c8cd…, patch 695ff9a8…) |
| compiler/quantum-holography-status/status.css | b18e2224… | foundation snapshot |
| compiler/quantum-holography-status/status-print.css | 16e274ec… | foundation snapshot |
| content/quantum-holography-status/page.json | ae651ec1… | foundation snapshot |
| compiler/quantum-holography-status/status.js | ad436be6… | interaction candidate-r3 |
| compiler/build-quantum-holography-status.py | 7419f94a… | quality C02, integrated |
| compiler/quantum-holography-status/audit.py | 2e857726… | quality cycle-3 audit, integrated |
| content.json, essay.md, README.md, tex2mathml.cjs, vendor/temml.cjs, TEMML-LICENSE | baseline pins | baseline |

Built as it stands, this base fails its own integrated audit: the essay prints 8 raw TeX segments ("\(c=33\)…"),
because the foundation's essay() escapes the text. Hunk P16 below fixes it.

## Two patches, separate and inspectable (`patches/`, guard `apply-integration.sh`, manifest `INTEGRATION-MANIFEST.json`)

| Patch | sha256 | Files: before → after |
|---|---|---|
| QUALITY-REMAINING.diff | fd96ea3a… | status.py da6f2c36 → 2bd14fc7 (20 hunks); status.css b18e2224 → af207495 (3); status-print.css 16e274ec → a06c6c04 (1); audit.py 2e857726 → f84ad658 (8) |
| STATUS-LANGUAGE.diff | d15f0d23… | page.json ae651ec1 → c193b5fd (1 hunk: five status labels) |
| OPTIONAL-heading.diff | 61ee1c44… | status.py after the remaining patch: a counterexample's statement title as h3 (no skipped heading level); for the foundation to decide |
| OPTIONAL-README.diff | 5b72c1be… | README.md, earlier lane notes; the README rules for content writers belong to the content writer (A4-F-07) |

`sh apply-integration.sh <tree> [remaining|language|all]` refuses (exit 2) unless every target is at its integrated
before-hash and the patch applies cleanly, and checks every after-hash (exit 3). Tested on fresh copies of the base:
all; remaining then language; language alone; a drifted status.css is refused with every file untouched.

### QUALITY-REMAINING.diff, hunk by hunk (exact hunk headers in `patches/HUNKS.md`; the P labels below group them)

status.py (each hunk keeps the foundation's atlas mount, contents, fold markup, row-status filters, unknown-status
behaviour, hypotheses before the text and native-QA changes; a 3-way merge from the baseline, conflicts resolved to the
foundation except where named):
- P1-P5, P8, P12, P18, P19: text forms of formulas for attributes and titles (A2-A2-02, A3-F-01, A3-F-09, A3-F-13):
  `Math.add_text`, deduplicated text jobs, `_MathText`/`math_text` (C_2, T^2, q^(1/2), (p)/(q)), `Build.text_form`;
  used for the grid marks' names, the row link's title and the page title and description (no TeX source, nothing
  between angle brackets lost). Merged into the foundation's substitute(), which keeps its wide-formula width hint.
- P6, P17 (glossary), P15 (open groups): explicit ids reserved first; two equal explicit ids, an explicit id taking
  another entry's anchor, and an open-group id taking the section's anchors fail with named problems (C19, A2-A2-03,
  A3-F-08).
- P7, P8: rich(..., markup=False) and plain(markup): asterisks and [links](...) stay as written where needed (A2-A2-11).
- P9: hypotheses must be a list of non-empty texts; a string or a non-text item fails the build with a named problem
  (before, a string rendered letter by letter). The foundation's list before the text is kept.
- P11, P13, P14: column names, short labels, cell-note column names, column definitions and row-line column names
  set as mathematics (A3-F-07).
- P16 and the contents hunk: the essay through rich(terms=False, markup=False): TeX as mathematics, the short-display
  rule only without TeX, the essay title as mathematics, also in the foundation's contents list (C03, A2-A2-01,
  A3-F-07). Removes the 8 raw-TeX failures of the base.
- P17 also: a warning when essay.md is missing from the input folder.
- P20: fonts subset with recalcTimestamp=False: byte-reproducible builds (C28).

status.css: the two comments that named status.js reworded; `.st-unknown { --st: var(--ink-4) }` so that a status
outside the list (drafts only; the build fails) is drawn in a neutral colour. status-print.css: the three comments that
named status.css or status.js reworded. These comments otherwise fail the remaining audit (comments naming source files).

audit.py (2e857726 → f84ad658): everything after cycle 3: every attribute in either quoting, non-JS scripts as data,
JS strings and comments (template interpolations read as code), CSS generated content and strings, SVG images in data:
URIs anywhere, all non-technical metas, svg text; normalised and NFKC-folded text; hashes (letters and digits),
UUIDs, repository addresses and private paths by digest; stage labels with dashes and capitals; id rules; the \mathrm
and \rm digit guard and internal LaTeX labels; failure names giving the likely cause; warnings grouped by kind; and
(root's ruling) a 'refuted form' statement without hypotheses fails the build. The audit's own key warning was removed:
the foundation already fails the build when a status in use has no status_key entry.

### STATUS-LANGUAGE.diff (the Astra ruling, presentation only)

page.json status_labels: checked "Established", open "Remaining", refuted form "Scoped negative", partial "Partial",
not posed "Not posed" (conditional, published, pending "Proposed", conjecture and heuristic unchanged). Every surface takes
its label from status_label(code), so cards, grid cells and their names, legend, key, filters, tally, fold lines and the
search facets follow; colours, codes, ids and hypotheses are untouched. The atlas module (atlas lane, atlas.py
3c9ba4d2…) already selects labels by stored code with the same words (PAGE_STATUS alias map; Established, Conditional,
Scoped negative, Remaining). Not changed: the section heading "Open problems" (a section name, not a status) and
page.json cell_glosses (prose shown only for a cell status without a status_key entry).

## What the integration already holds (absorbed or superseded; no hunk)

- Foundation: the search opener in the bar (C14); 'refuted form' as a statement status with hypotheses and its colour;
  raw invalid statuses shown as written with a failing build; family-specific row filters (A7-F-01); the missing
  status-key build failure; print block flow for statements, questions, failures, glossary and cell lines, and the key
  and column definitions in two print columns (C01, A2-A2-07, A3-V-14); not-posed colour (C15: light #8a847c about
  3.7:1, dark #807a73 about 4.3:1); empty-filter row styling (C06); the phone sheet with safe-area insets (C23 layout);
  the bar's edge fade with scroll padding (supersedes A3-V-11, A4-V-01, A5-V-01, A6-V-01); fold lines in place of row
  mixes (supersedes A3-V-13); its own layout of the question sections (supersedes A3-V-03 a).
- Interaction candidate-r3: the card's Close action (supersedes C23 control, A3-F-06, A4-V-03, A3-V-15, A4-V-02);
  announcements through a separate live region (A2-A1-01, A3-V-12); the empty-row note; the search skipping the
  hypotheses label; and, by its own 85 tests, Escape and pinned-card focus (C10, C11), table keys (C16), search keys and
  indexing of lead, key and introductions (C12, C13), unknown address values named and dropped (C08), address and
  history restoration (C07, C09), card link names with formulas (C05) and mark names without TeX (C04 on the script
  side). This lane's own jsdom checks were not rerun on candidate-r3: their hooks differ.

## Evidence (admissible only; no browser)

| Check | Base (integrated) | Base + QUALITY-REMAINING | + STATUS-LANGUAGE |
|---|---|---|---|
| Build audit with the remaining audit | 13 failures (8 raw TeX, 5 comments) | PASS, 0 failures | PASS |
| Build with fonts, twice | — | — | byte-identical (460252ac…) |
| Builder fixtures (19: essay, names, ids, columns, title, digits, status contract) | confounded by the essay failure | 19/19 | 19/19 |
| Audit fixtures (114 leak, clean and warn probes) | — | 114/114 | 114/114 |
| Interaction suite (candidate-r3 interaction.test.cjs, 85 tests) | 82/85 | 82/85, the same three | 82/85, the same three |
| qh-static Q08-raw-tex | FAIL (8) | PASS | PASS |
| qh-static Q11 whole-payload completeness | status_key labels not shown | status_key labels not shown | PASS (with the owner's new status_key) |
| Status language by stored code (lead/qh-status-language.mjs) | — | FAIL (old labels) | PASS: 281 cards, 160 cell names, 160 cell texts, 6 legend, 8 key, 4 filters, 4 tally, 105 fold lines; no old label left |

The three interaction tests that fail on base and composed alike read a count inside each tally pill; the foundation
snapshot's tally pills carry no count. That is a foundation-interaction mismatch, not caused by this delta.

## The current preview (`/tmp/programme-public-current-successor-20261116/composed`, content ec6864c4…, essay 798cca68…)

Built through base + both patches (`current-preview/`, read-only copies, no atlas.json in the input):
- audit: 2 failures, both "E3" in "A bare exterior E3 algebra" (mathematics outside TeX; the content owner writes
  \(E_3\)); warnings: 2 formulas outside TeX, "draft", one process word, one identifier-like id.
- every baseline anchor present (0 lost), 0 duplicate ids, 0 broken links, every statement anchored; no raw TeX; no TeX
  in names; status language consistent on 295 cards, 160 cells, 113 fold lines.
- completeness gap (qh-static Q11): 30 reader texts are not on the page: the nine principal results' `summary` and the
  new `orientation` block (title, 4 explanation paragraphs, 4 programme families with title and text, 4 reader-guidance
  items). The integrated producer does not render these fields; root decides who renders them.
- the payload's one 'refuted form' statement sits under a decisive question, so no row filter offers it; the tally and
  search facet do (family filters, as intended).

## Not done here

Visual and print acceptance (root's native session); the README rules (content writer); the status_key prose (content
owner); the 'E3' wording and the 30 unrendered texts (content owner and renderer owner).
