# Foundation lane: precommitted evaluation plan

Written before the first attack wave. Healing is judged only against these checks.
Baseline: BASELINE.json hashes (all 13 verified equal at lane start).
Baseline build: `baseline/preview.html` sha256 6a86e7fdbd91c03f72b78745348d6a8437ad044dfb2546637e2de490af664df2, audit PASS,
281 statements (checked 197, open 74, conditional 6, published 4), 160 cells, 144 terms, 2502 formulas, 0 TeX errors.

Writable production files: `compiler/quantum-holography-status/status.py`, `status.css`, `status-print.css`,
and `content/quantum-holography-status/page.json` (`labels` only). Everything else is read-only.

## Claims under test

The candidate page lets a cold, serious reader go from the programme overview to a question, read that
question's hypotheses, the established results toward it, and what remains to compare; it presents every
research item of the baseline with unchanged status, text and anchor; it stays one offline file under the
current CSP; and it works at the representative widths, in both themes, with reduced motion, by keyboard,
and in print on A4 and Letter.

## Checks, expected results, blockers

| ID | Check | Command or method | Pass | Blocks |
|---|---|---|---|---|
| E1 | Build and audit | `/tmp/qh-tracker-build-20261116-venv/bin/python -B compiler/build-quantum-holography-status.py --output <lane>/preview.html --audit-dir <lane>/audit` (final run with fonts) | exit 0, `PASS`, 0 failures, `math errors: 0` | yes |
| E2 | Content custody | sha256 of content.json, essay.md, README.md | equal to BASELINE.json | yes |
| E3 | page.json scope | JSON diff baseline vs candidate | only `labels` keys added or changed; `status_labels`, `novelty_labels`, `cell_glosses`, metadata unchanged | yes |
| E4 | Anchor preservation | set of `id` values in baseline preview minus candidate preview | empty set | yes |
| E5 | Status fidelity | per anchored statement `data-status`; status multiset; cell status per (row, column) | identical to baseline | yes |
| E6 | Text and math fidelity | normalized text of each statement, question, "why", row summary, cell note, column explanation, failure claim, group intro, glossary entry, lead, essay; count of `<math` elements | every baseline unit present with identical text; equal math count | yes |
| E7 | Offline and CSP | CSP meta string; audit outside-reference checks; no new network API | unchanged CSP; audit clean | yes |
| E8 | Reader route | DOM and screenshots at 1400 and 375: overview -> question index -> one question -> its hypotheses, established results, remaining comparison -> back | each step reachable by a visible control, at most 2 activations from the overview to a question; question parts identifiable without reading unrelated questions | acceptance |
| E9 | Density | `document.documentElement.scrollHeight` at 1400 and 375, page start state | materially lower than baseline with no research removed (disclosure, not deletion) | acceptance |
| E10 | Keyboard | Tab sequence from the skip link through bar, index, a question, its disclosures; Escape on card; arrow keys in grid | every control reachable, focus visible, no trap, existing grid keys work | acceptance |
| E11 | Responsive | widths 1400, 1024, 768, 480, 375, light and dark | no page-level horizontal overflow; bar does not hide anchor targets; grid scrolls in its own box | acceptance |
| E12 | Contrast and motion | token contrast ratios (text on paper, status colours on paper, both themes); `prefers-reduced-motion: reduce` | WCAG 2.1 AA (4.5:1 body text, 3:1 large text and marks); no smooth scroll or transition under reduce | acceptance |
| E13 | Print | print to PDF on A4 and Letter | succeeds; every statement title present in PDF text; no screen-only controls; no clipped formula or table | acceptance |
| E14 | Console | load and interactions in headless Chrome | no console error or exception | yes |
| E15 | DOM contract | each selector and attribute status.js uses, asserted on the candidate | every hook present with the same semantics, or a documented composed replacement | yes |
| E16 | Atlas mount | build without atlas data; build with a test-only fixture outside content/ | without data: no atlas section, no nav entry; with fixture: section renders at the documented mount, ids valid, audit clean | acceptance |
| E17 | External gate | audit FORBIDDEN list; external-documents scan regex; public-artifact-source-check regex on reader-visible text | zero hits | yes |

## Negative cases

- A statement id that changes slug or disappears (E4).
- A disclosure that hides research text with no visible control or count (E6, E8).
- A filter or search that leaves a reader at a hidden target (E10).
- Print with a closed disclosure or a scrolled formula (E13).
- Interface labels that introduce workflow, version or tool words (E17).

## Residuals allowed outside the stable core

- Visual inspection limits of headless rendering (font hinting, subpixel layout) recorded as such.
- Content needs (missing hypotheses fields, missing domain data) reported to root; not authored here.
