# Quality lane: additive patch on the foundation's final F1 and F2

Staging only (`quality/compose/`); no other tree was edited. This patch supersedes, for root's composition, the earlier
`compose/patches/QUALITY-REMAINING.diff` (same hunks, against the pre-F1 snapshot) and withdraws
`compose/patches/STATUS-LANGUAGE.diff`: F1 sets the same five status labels and also removes `cell_glosses`.

## Base (exact bytes)

Root's integration as root reports it: foundation 695ff9a8 (four files), quality build wrapper 7419f94a and audit
2e857726, baseline status.js ef358190 (interaction candidate-r3 is not installed in root and is not part of this base).
Then the foundation's F1 `f1-status-language.patch` (9613254535445e7a…) and F2 `f2-successor-fields.patch`
(3f2c449364146401…), applied in a staging copy; every F2 candidate hash checked:

| File | sha256 (base of this patch) |
|---|---|
| compiler/quantum-holography-status/status.py | c7a924e6… (F2 candidate) |
| compiler/quantum-holography-status/status.css | b496f5f5… (F2 candidate) |
| compiler/quantum-holography-status/status-print.css | 8373d792… (F2 candidate) |
| content/quantum-holography-status/page.json | f0a6edc5… (F2 candidate; not touched here) |
| compiler/quantum-holography-status/audit.py | 2e857726… (quality audit, integrated) |
| compiler/quantum-holography-status/status.js | ef358190… (baseline; not touched here) |

Full hashes: `MANIFEST.json` (`base.f2.candidates`, `base.unchanged_pins`, `files`).

## Patch

`QUALITY-ON-F1F2.diff` (sha256 in `MANIFEST.json` `patch.sha256`, 2d617690…); hunk index `HUNKS.md`.

| File | Before → after | Hunks |
|---|---|---|
| status.py | c7a924e6… → 2114d75b… | 20 |
| status.css | b496f5f5… → 10a655ee… | 3 |
| status-print.css | 8373d792… → 7c42df81… | 1 |
| audit.py | 2e857726… → f84ad658… | 8 |

Guard: `sh apply.sh <tree>` refuses (exit 2) unless all four targets are at their before-hashes and the patch applies
cleanly; checks every after-hash (exit 3). Tested on a fresh copy of the base: the result equals the composed tree byte
for byte; a drifted status-print.css is refused with every file untouched.

Content of the patch (the quality fixes the foundation does not already carry): essay TeX as mathematics, including
the essay title and its entry in the contents list; text forms of formulas for grid-mark names, row-link titles and the
page title and description; column names, short labels, cell-note column names and column definitions as mathematics;
explicit glossary and open-group ids with named collisions; hypotheses must be a list of non-empty texts;
byte-reproducible font subsets; three comment rewordings and a neutral colour for a status outside the list (drafts
only); the hardened audit, in which a 'refuted form' statement without hypotheses fails the build. The one merge
conflict with F2 (F2's statement summary line beside the hypotheses validation) keeps both.

Preserved unchanged: F2's orientation block, principal summaries, atlas mount and links, as-of rendering; F1's labels
by stored code; the foundation's contents, fold markup, family row filters, unknown-status behaviour (shown as written,
build fails), missing-status-key failure and native-QA changes.

## Evidence (admissible only; no browser)

Baseline content, base vs base + patch:

| Check | F1+F2 | F1+F2 + this patch |
|---|---|---|
| Build audit (the patch's audit) | 8 failures: raw TeX in the essay | PASS |
| Build with fonts, twice | — | byte-identical (12cd41b7…) |
| Builder fixtures (essay, names, ids, columns, title, digits, status contract) | 2/19 | 19/19 |
| Audit fixtures (75 leak, 20 clean, 19 warn probes) | — | 114/114 |
| Status labels by stored code (cards, cells and their names, legend, key, filters, tally, fold lines) | consistent (F1) | consistent |
| Page body change | — | only the essay paragraphs (TeX now MathML); F2's markers identical |

Current preview (`/tmp/programme-public-current-successor-20261116/composed`: content 6d8d8205…, essay 0f35958c…,
atlas 577e3cb6…), built with the atlas lane's candidate module as a test input only (atlas.py 3c9ba4d2…, atlas.css
5cb1f925…, atlas.js 672246e7…; not part of this patch):

| Check | F1+F2 | F1+F2 + this patch |
|---|---|---|
| Build audit | 194 failures (167 raw TeX in the essay) | 27 failures, every one also present without the patch; no new kind |
| Raw TeX in reader text (qh-static Q08) | FAIL (162) | PASS |
| Every baseline anchor present, no duplicate id, no broken link (Q09) | PASS | PASS |
| No TeX in accessible names (Q15) | PASS | PASS |
| Whole-payload completeness (Q11) | PASS | PASS |
| F2 markers: orientation 61, summaries 10, atlas mounts 38, claims 716, edges 259, paths 24, as-of 5, dates 2 | — | identical |
| Status labels by stored code (295 cards, 160 cells, 113 fold lines …) | consistent | consistent |

Not rerun, as root instructed: the interaction suite (root still carries the baseline script). Earlier, with
candidate-r3 as a planned reference, it gave 82/85 with and without the quality delta (three tests read a tally count the
foundation removed).

## For the content owner and the atlas lane (facts; no reader text proposed here)

The 27 remaining failures on the current preview are content and atlas data, not renderer defects:
- mathematics written without TeX: "E3" (10, e.g. "A bare exterior E3 algebra", and the atlas claim
  bare-e3-exterior-rigidity), "T2" (9 in the page; atlas claims centre-central-coefficient-strictification,
  centre-actual-weight-two-bar, centre-binary-logarithmic-comparison-criterion), "R2" (1; atlas edge
  current-native-dg-input-to-state-diagram);
- atlas comparison d-centre-base-change names questionId decisive-centre-base-change, which is not a question on the page.

## For the README owner (Astra; facts only)

The producer README's schema and audit lines do not yet state: the statement status 'refuted form' (exact value, with a
space; atlas scoped_negative); the statement field `hypotheses` (a list of non-empty texts; TeX allowed; required for
'refuted form'); labels selected by stored code (page.json status_labels, the ruling's words); that a letter followed by
two or more digits inside \mathrm or \rm fails (write \mathrm{M}_{24}); that ASCII mathematics such as C1, E1, T2 or v4
fails as an identifier or version tag; that the internal LaTeX label scheme fails in TeX; that hashes, UUIDs, repository
addresses and private paths fail anywhere; the warning words; that column names, short labels and the essay title may
contain TeX.

## Not done here

Native-Chrome visual and print QA (the existing primary QA owner); README prose (Astra); status_key prose (content
owner); the 27 content and atlas items above; one bounded independent review of this package (pending; one reviewer
only, as root's capacity allows).
