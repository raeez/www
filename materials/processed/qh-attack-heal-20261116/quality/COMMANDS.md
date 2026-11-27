# Commands run in this lane and their results (admissible runs only)

Run from the worktree root. `Q=materials/processed/qh-attack-heal-20261116/quality`,
`PY=/tmp/qh-tracker-build-20261116-venv/bin/python` (Python 3.9.6, fontTools 4.60.2), Node 25.2.1.
`QH_JSDOM` names a jsdom 28 package directory; on this machine it is an existing install outside this
repository (path given in the handoff message). The browser runs made before root's restriction are listed in
RESTRICTION.md and are not repeated here; they are not evidence.

## Inputs

| Command | Result |
|---|---|
| sha256 of the 13 files in `$Q/BASELINE.json` against the worktree | all 13 equal; RELEASE.json prompt and manifest hashes equal |

## Builds

| Command | Result |
|---|---|
| `$PY -B compiler/build-quantum-holography-status.py --no-fonts --output $Q/baseline/preview-nofonts.html --audit-dir $Q/baseline/audit-nofonts` | exit 0, PASS, 1,828,020 bytes, math 2502 (errors 0) |
| `$PY -B compiler/build-quantum-holography-status.py --output $Q/baseline/preview.html --audit-dir $Q/baseline/audit` | exit 0, PASS, 2,198,862 bytes, 4 font faces, sha256 d1ef8041… |
| Verification minimum: `$PY -B compiler/build-quantum-holography-status.py --output $Q/preview.html --audit-dir $Q/audit` (production sources, unchanged) | exit 0, PASS, 2,198,862 bytes, sha256 598ad5f7…; equal to the baseline build except inside the font data (C28) |
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --output $Q/candidate/preview.html --audit-dir $Q/candidate/audit` | exit 0, PASS (0 failures, 14 warnings), 2,205,708 bytes, math 2506 (errors 0), sha256 c9c010d2… |
| same with `--no-fonts --output $Q/candidate/preview-nofonts.html --audit-dir $Q/candidate/audit-nofonts` | exit 0, PASS, sha256 96aa2608… |
| two candidate builds two seconds apart (`$Q/heal/build-b/repro-{1,2}.html`) | identical sha256 c9c010d2… (byte-reproducible after C28) |

## Static checks (built HTML parsed by jsdom without scripts)

`QH_JSDOM=… node $Q/lead/qh-static.mjs --html <page> --content <content dir> --baseline_manifest $Q/BASELINE.json [--baseline-html $Q/baseline/preview.html] --out <json>`

| Page | Q02 | Q03-csp | Q04 | Q05 | Q06 | Q07 | Q08 | Q08-raw-tex | Q09 | Q10 | Q15-tex-in-names |
|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | PASS | PASS | PASS | PASS | PASS | FAIL (8 names with TeX) | PASS | FAIL (essay, 4 formulas) | PASS | PASS | FAIL (8) |
| candidate | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (every baseline id present) | PASS | PASS |

Results: `$Q/lead/results/static-baseline-v2.json`, `static-baseline-preview-nofonts.html.json`, `static-candidate-final.json`.

## jsdom behaviour checks (page script run in jsdom; no layout)

`QH_JSDOM=… node $Q/lead/qh-jsdom-checks.mjs --html <page> --out <json>`

| Page | J1 | J2 | J2b | J3 | J4 | J5 | J6 | J7 | J8 | J9 | J10 | J11 | J12 | R1–R9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 9 PASS |
| candidate | PASS | PASS | PASS | PASS | PASS | PASS | PASS (stubbed geometry) | PASS | PASS | PASS | PASS | PASS | PASS | 9 PASS |

Page errors (other than jsdom's not-implemented notices): 0 on both. Results: `$Q/lead/results/jsdom-baseline.json`,
`jsdom-candidate-final.json`.

## Audit fixtures (synthetic leak pages)

`$PY -I -B $Q/lead/qh-audit-fixtures.py <producer folder> --out <json>`

| Producer | Leak fixtures flagged | Clean fixtures passed |
|---|---|---|
| baseline `compiler/quantum-holography-status` | 1 of 8 (only the head check) | 2 of 2 |
| candidate `$Q/heal/mirror/compiler/quantum-holography-status` | 8 of 8 | 2 of 2 |

## Builder `--input` fixture (C02)

Fixture `$Q/heal/fixtures/input-labels/` = content.json and essay.md copied, page.json with
`status_labels.checked` changed to "Proved and checked independently".

| Command | Result |
|---|---|
| `$PY -B compiler/build-quantum-holography-status.py --no-fonts --input <fixture> --output $Q/heal/fixtures/out/baseline-builder.html --audit-dir $Q/heal/fixtures/out/audit-baseline-builder` | new label 0 times, old label 429 times (the input folder's page.json ignored) |
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --no-fonts --input <fixture> --output $Q/heal/fixtures/out/candidate-builder.html` | new label 429 times, old label 0; audit written to `<fixture>/audit/` |

## Guarded patch

| Command | Result |
|---|---|
| `$Q/heal/apply-guarded.sh $Q/heal/apply-test/all all` on a fresh copy of the 13 baseline files | all 7 changed files equal their after-hashes; tree equals the mirror |
| `apply-guarded.sh <copy> foundation` then `… interaction` | tree equals the mirror |
| `apply-guarded.sh <copy with status.js altered by one byte> all` | refused, exit 2, "before-hash mismatch"; every other file left at its before-hash |

## Static CSS cascade (C01 precondition)

Parsing status.css followed by status-print.css: inside `@media print`, `.statements`, `.questions` and
`.failures` are `display: block` and `.known > .statements` is `display: block !important`; the only grid
declarations for these containers are the screen rules. Whether this removes the print loss can only be
decided by printing, which this lane may not do.

## Cycle 3 (after the two verification reports; candidate `qh-quality-heal-c3`)

| Command | Result |
|---|---|
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --output $Q/candidate/preview.html --audit-dir $Q/candidate/audit` | exit 0, PASS, 0 failures, 2,207,578 bytes, 2515 formula jobs (2506 formulas plus 9 text forms for names), 0 TeX errors; sha256 685e0fa2…; a second build (`heal/build-b/repro-3.html`) is byte-identical |
| same with `--no-fonts` into `$Q/candidate/preview-nofonts.html` | PASS, sha256 074136e2… |
| `node $Q/lead/qh-static.mjs --html $Q/candidate/preview.html … --baseline-html $Q/baseline/preview.html` | 11 of 11 PASS (every baseline id present) |
| `node $Q/lead/qh-jsdom-checks.mjs --html $Q/candidate/preview.html` | 25 of 25 PASS (J1–J13, J2b, J6b, J7b, R1–R9); on the baseline J13 and J7b fail, J6b passes vacuously (no correction exists) |
| `$PY -I -B $Q/lead/qh-audit-fixtures.py <producer>` | candidate 32 of 32 as expected (23 leak classes fail, 5 mathematical-prose probes pass clean, 4 review warnings); baseline misses 22 of 23 leaks and fails the chains/cochains prose probe |
| `$PY -I -B $Q/lead/qh-builder-fixtures.py <builder> <work folder>` | candidate builder 6 of 6 (short essay equation as MathML; essay asterisks and links unchanged; names with \mathfrak build and read "𝔰𝔩2-modules and 𝔤ˆ at level k"; explicit glossary id keeps term-weak-module in both orders; duplicate explicit ids and an open-group id taking open-h fail with named problems); baseline builder 1 of 6 |
| guarded apply of `heal/PATCH.diff` on fresh copies | full and split (foundation, then interaction) reproduce every after-hash; a one-byte drift in status.js is refused (exit 2) with all other files at their before-hashes |
| `$PY -I -B $Q/lead/qh-visual-metrics.py <css folder> <preview>` | computed visual-system facts in `lead/results/visual-metrics-{candidate,baseline}.json`, used in VISUAL-ATTACK.md |
| native Chrome: claude-in-chrome skill loaded, `tabs_context_mcp`, `list_connected_browsers` (twice) | "Browser extension is not connected"; no connected browser; no tab created (BLOCKER-CHROME.md) |

## Cycle 3b (after the R3-V and R3-F reports; candidate `qh-quality-heal-c3b`)

`QH_PRIVATE_PROBES` names a file of private-path probe lines kept outside the repository (so no private repository name
is written in this folder); the file used is named in the handoff message.

| Command | Result |
|---|---|
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --output $Q/candidate/preview.html --audit-dir $Q/candidate/audit` | exit 0, PASS, 0 failures, 15 warnings (unchanged from c3), 2,208,615 bytes, "math: 2506 formulas (2507 rendering jobs; errors: 0)", sha256 14cd2730…; a second build (`$Q/heal/build-b/preview.html`) is byte-identical |
| same with `--no-fonts` into `$Q/candidate/preview-nofonts.html` | PASS, 1,839,197 bytes, sha256 679eb8ca…; against the c3 page only the intended changes (Close control hidden until wired, its CSS rule and script line, reworded comments) |
| `QH_PRIVATE_PROBES=<file> $PY -I -B $Q/lead/qh-audit-fixtures.py <producer folder> --out …` | candidate 81 of 81 as expected (54 leak classes fail, 10 mathematical or open-repository probes pass clean, 17 warn); baseline 10 of 81 (1 of 54 leaks, 9 of 10 clean, 0 of 17 warnings); `lead/results/audit-fixtures-c3b{,-baseline}.json` |
| `$PY -I -B $Q/lead/qh-builder-fixtures.py <builder> $Q/heal/fixtures/c3b --out …` | candidate builder 12 of 12, baseline builder 1 of 12 (6 new: names with E_8, C_2, T^2, P^1; TeX column name and short label; TeX essay title; explicit glossary id taking another entry's anchor fails with a named problem; \mathrm{T15} fails with a named problem; head title keeps "a<b and c>d") |
| `node $Q/lead/qh-static.mjs --html $Q/candidate/preview.html … --baseline-html $Q/baseline/preview.html` | 11 of 11 PASS, every baseline id present; baseline 8 of 11 (Q07, Q08-raw-tex, Q15 fail) |
| `node $Q/lead/qh-static.mjs` on the fixture pages open-id (explicit open-group and glossary ids), names, names-scripts, columns-tex, essay-title-tex | all checks PASS on each |
| `node $Q/lead/qh-jsdom-checks.mjs --html $Q/candidate/preview.html` | 28 of 28 PASS (J1–J16, J2b, J6b, J7b, R1–R9), 0 page errors; baseline fails every heal check except J6b (vacuous), passes R1–R9 |
| `python3 -I -B $Q/lead/make-guarded-patch.py $Q qh-quality-heal-c3b` (worktree root) | production files equal BASELINE.json; MANIFEST 28eb3b09…, PATCH.diff cad57a10…, foundation.diff 8872ca19…, interaction.diff b1c23e8e… |
| `sh $Q/heal/apply-guarded.sh <fresh copy> all`; `… foundation` then `… interaction`; a copy with status.js drifted | full and split reproduce the mirror byte for byte; drift refused (exit 2) with every other file at its before-hash |
| foundation patch alone on a fresh copy, built with `--no-fonts`, page script run in jsdom | audit PASS; Close control and search opener both present and hidden; 0 page errors |

## Cycle 3c (after the R3-F and R3-V cycle-3b reports; candidate `qh-quality-heal-c3c`)

The heals were prepared in a copy of the mirror while R3-F verified the frozen c3b mirror, then promoted.

| Command | Result |
|---|---|
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --output $Q/candidate/preview.html --audit-dir $Q/candidate/audit` | exit 0, PASS, 0 failures, 15 warnings (grouped by kind in audit.txt), 2,209,506 bytes, "math: 2506 formulas (2507 rendering jobs; errors: 0)", sha256 35d52b7f…; a second build is byte-identical |
| same with `--no-fonts` into `$Q/candidate/preview-nofonts.html` | PASS, 1,840,088 bytes, sha256 b0f36e76… |
| `python3 -I -B $Q/lead/make-guarded-patch.py $Q qh-quality-heal-c3c` | production files equal BASELINE.json; MANIFEST cd2d4727…, PATCH.diff b8820475…, foundation.diff 179d7ce2…, interaction.diff 09bc14ee… |
| `sh $Q/heal/apply-guarded.sh` on fresh copies: all; foundation then interaction; drifted status.js; foundation alone | full and split equal the mirror; drift refused (exit 2), every other file at its before-hash; foundation alone builds with audit PASS (`heal/apply-test/foundation-only.html`) |
| `node $Q/lead/qh-jsdom-checks.mjs --html $Q/candidate/preview.html --baseline $Q/baseline/preview-nofonts.html --foundation-only $Q/heal/apply-test/foundation-only.html` | 29 of 29 PASS (J1–J17, J2b, J6b, J7b, R1–R9), 0 page errors; J14 and J17 fail on the c3b page and the c3b foundation-only page; baseline fails every heal check except J6b and passes R1–R9 |
| `node $Q/lead/qh-static.mjs --html $Q/candidate/preview.html … --baseline-html $Q/baseline/preview.html` | 11 of 11, every baseline id present; baseline 8 of 11; fixture pages short-label, open-id, names-scripts, columns-tex all PASS |
| `QH_PRIVATE_PROBES=<file> $PY -I -B $Q/lead/qh-audit-fixtures.py <producer>` | candidate 102 of 102 (67 leak, 16 clean, 19 warn); baseline 16 of 102 (1 of 67 leaks) |
| `$PY -I -B $Q/lead/qh-builder-fixtures.py <builder> <work folder>` | candidate 13 of 13; baseline 2 of 13 |
| c3c audit on the 4,129 reader strings of the baseline atlas | 220 strings fail as under the c3 audit (209 only because the probe does not render TeX; 11 AQ01), no new failure kind; `lead/results/atlas-audit-rules-1120.json` |

## Cycle 3d (after the R3-F and R3-V cycle-3c reports; candidate `qh-quality-heal-c3d`)

The heals were prepared in a copy of the mirror while R3-F verified the frozen c3c mirror, then promoted.

| Command | Result |
|---|---|
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --output $Q/candidate/preview.html --audit-dir $Q/candidate/audit` | exit 0, PASS, 0 failures, 15 warnings, 2,210,068 bytes, 2506 formulas (2507 rendering jobs; 0 errors), sha256 5c1464c4…; a second build is byte-identical |
| same with `--no-fonts` | PASS, 1,840,650 bytes, sha256 3faab879… |
| `python3 -I -B $Q/lead/make-guarded-patch.py $Q qh-quality-heal-c3d` | MANIFEST b61ff299…, PATCH.diff 8936acb4…, foundation.diff dd5682f8…, interaction.diff 886241b4… |
| guarded apply on fresh copies: all; foundation then interaction; drifted status.js; foundation alone | full and split equal the mirror; drift refused (exit 2) with every other file at its before-hash; foundation alone builds with audit PASS (`heal/apply-test/foundation-only.html`, d392f7e2…) |
| `node $Q/lead/qh-jsdom-checks.mjs --html $Q/candidate/preview.html --baseline $Q/baseline/preview-nofonts.html --foundation-only $Q/heal/apply-test/foundation-only.html` | 29 of 29 PASS, 0 page errors; J14 now checks both edges of the bar and fails on the c3c page for the left edge; baseline passes 10 (R1–R9 and the vacuous J6b) |
| `node $Q/lead/qh-static.mjs` on the candidate and on fixture pages short-label, open-id, names-scripts, columns-tex, essay-title-tex | 11 of 11 on each |
| `QH_PRIVATE_PROBES=<file> $PY -I -B $Q/lead/qh-audit-fixtures.py <producer>` | candidate 114 of 114 (75 leak, 20 clean, 19 warn); baseline 20 of 114 (1 of 75 leaks) |
| `$PY -I -B $Q/lead/qh-builder-fixtures.py <builder> <work folder>` | candidate 14 of 14 (new: open-id); baseline 2 of 14 |

## Status-contract delta (candidate `qh-quality-heal-c3e`): 'refuted form' as a statement status, with hypotheses

| Command | Result |
|---|---|
| c3d builder on the refuted-form fixture content (`--allow-draft`) | FAIL "unknown statement status 'refuted form'"; the draft draws both statements as st-open / data-status="open" (`heal/build-next/c3d-on-refuted/page.html`) |
| `$PY -B $Q/heal/mirror/compiler/build-quantum-holography-status.py --output $Q/candidate/preview.html --audit-dir $Q/candidate/audit` | PASS, 0 failures, 15 warnings, 2,210,647 bytes, sha256 d6dc0006…; a second build is byte-identical; no-fonts 29658c1a… |
| `python3 -I -B $Q/lead/make-guarded-patch.py $Q qh-quality-heal-c3e` | MANIFEST 0d49eaf2…, PATCH.diff 38fd8710…, foundation.diff f24953df…, interaction.diff 4c33321b… |
| guarded apply: all; foundation then interaction; drifted status.js; foundation alone | full and split equal the mirror; drift refused (exit 2); foundation alone builds with audit PASS (`heal/apply-test/foundation-only.html`, 1c6388f6…) |
| `node $Q/lead/qh-jsdom-checks.mjs --html $Q/candidate/preview.html --baseline … --foundation-only …` | 29 of 29, 0 page errors |
| `node $Q/lead/qh-static.mjs` on the candidate and on `heal/fixtures/c3e/refuted-form/page.html` | 11 of 11 on both (baseline 8 of 11) |
| `QH_PRIVATE_PROBES=<file> $PY -I -B $Q/lead/qh-audit-fixtures.py <producer>` | 114 of 114 |
| `$PY -I -B $Q/lead/qh-builder-fixtures.py <builder> <work folder>` | candidate 18 of 18 (new: refuted-form, refuted-inexact, hypotheses-malformed, refuted-unscoped); baseline 2 of 18 |
| `node $Q/lead/qh-status-extension.mjs --html $Q/heal/fixtures/c3e/refuted-form/page.html` | S1-S6 PASS (rendering and names, filter, address round trip `?show=refuted+form`, tally link and facet "2 matches", search in hypotheses finds both statements, open tally unchanged), 0 page errors; on a page without such statements S1 fails |

## Integration package on the foundation's final F1+F2 (`compose/f2-package/`)

| Command | Result |
|---|---|
| F1 then F2 applied to a copy of root's integration (`compose/f1f2/tree`) | every F2 candidate hash matches (status.py c7a924e6, status.css b496f5f5, status-print.css 8373d792, page.json f0a6edc5) |
| 3-way merge of the quality delta onto F1+F2 (`compose/f1f2/merge`) | 1 conflict (F2's summary line beside the hypotheses validation), both kept |
| `python3 -I -B lead/make-f2-package.py` (from compose) | QUALITY-ON-F1F2.diff 2d617690…, MANIFEST.json |
| `sh compose/f2-package/apply.sh <copy>`; a drifted copy | equals the composed tree; drift refused (exit 2), files untouched |
| builds of F1+F2 and F1+F2 + patch (baseline content) | audit 8 failures → PASS; fonts twice byte-identical (12cd41b7…) |
| audit fixtures; builder fixtures | 114/114; 2/19 → 19/19 |
| `node lead/qh-status-language.mjs` | consistent before and after (F1 labels) |
| current preview (content 6d8d8205…, essay 0f35958c…, atlas 577e3cb6…) with the atlas lane's module as a test input | audit 194 → 27 (no new kind); Q08 162 → 0; Q09, Q15, Q11 PASS; F2 markers identical |

## A8-F-01: quality tools mapped to F2 (frozen in `compose/TOOLS-FROZEN.json`)

| Command | Result |
|---|---|
| `node lead/qh-static.mjs --html compose/f1f2/current/atlas-composed.html --content compose/f1f2/current/input --page <F2 page.json> --baseline-html baseline/preview.html` | all 11 PASS (Q06, Q08, Q10 now pass) |
| same on the F2 baseline-content page and on the c3f candidate | all PASS except Q11 (baseline status_key labels; the owner's new status_key clears it) |
| `node --max-old-space-size=8192 lead/qh-status-extension.mjs --html <page>` on the current preview, the F2 fixtures refuted-form and refuted-principal-only, and the c3e fixture | S1-S6 PASS, 0 page errors (the default heap runs out on the current preview) |
