# Foundation lane: integration checks for the composed tree and the successor payload

The 11:20 content and atlas are a layout baseline only. These checks verify the foundation renderer on whatever
content root composes: the complete current content, the original stable anchors, all families and questions, and
the relation and reading-path data of the atlas. Every check runs without a browser, reads only its inputs, and
writes only where `--json` or `--output` points.

Notation: `R` = root's composed integration tree (run commands from `R`), `L` =
`/Users/raeez/www-worktrees/2026-11-16-qh-max-foundation/materials/processed/qh-attack-heal-20261116/foundation`,
`P` = `/tmp/qh-tracker-build-20261116-venv/bin/python`, `O` = an output directory of root's choosing,
`C` = `content/quantum-holography-status` (the content folder the build reads).

## 1. Apply the foundation patch

```
python3 L/patch/apply_guarded.py R --check      # per file: would replace, already applied, or DIVERGENT; writes nothing
python3 L/patch/apply_guarded.py R              # replaces only files that still have the baseline bytes
```
A divergent file (another lane edited status.py, status.css, status-print.css or page.json) stops the whole
apply before anything is written. Merge it hunk by hunk from `L/patch/foundation.patch`: from `R`,
`patch -p1 --dry-run < L/patch/foundation.patch` shows which hunks apply cleanly. (`git apply --3way` cannot help:
these paths were untracked at the principal base, so git holds no baseline blobs for them.) Then re-run checks 2
to 9. Hashes: `L/patch/GUARD.json`; candidate bytes: `L/patch/files/`.

## 2. Build with fonts and audit

```
P -B compiler/build-quantum-holography-status.py --output O/page.html --audit-dir O/audit
```
Accept: exit 0; audit `PASS` with 0 failures; `math: N (errors: 0)`. The build reads `page.json` from the
repository's content folder, not from `--input` (A1-A2-16; proposal in CONTRACT.json).

## 3. Completeness against the content it was built from

```
P -I -B L/tools/completeness.py C O/page.html --json O/completeness.json
```
Accept: `ALL PASS`. It fails on any content field the producer does not show (a successor field such as a new
relation list fails here until the renderer shows it), any column or cell the grid does not draw, and any
statement, question card, family, grid cell, column definition, counterexample, open-problem group, glossary
entry, status key explanation, cover, lead, changes or essay text missing from its own element, or out of its
section, card, family or group. Words are compared with TeX and MathML set aside. `INFO` lines are design
facts to read, not failures: the page shows page.json's status labels where the content's status key names
them differently (five today), and novelty only for checked and pending statements (baseline rules).

Verified on the current candidate (ALL PASS, 674 content objects, 281 statements, 34 cards, 20 families,
160 cells) and on the baseline page (ALL PASS). It catches each of these deliberate breaks: a flipped status,
a removed question anchor, a changed cell status, a missing glossary entry, one dropped word in a statement,
a missing "why", one changed word in a cell note, a related statement removed from its card, a dropped
citation word, a changed definition.

## 4. Original stable anchors

```
python3 -I -B L/tools/anchors.py <reference page> O/page.html --json O/anchors.json
```
Reference: the page of the reviewed 11:20 content (`L/baseline/preview.html`, 428 ids) or root's own reference.
Accept: `ALL PASS`: every reference id present (s- 183, q- 34, row- 20, f- 11, open- 5, term- 144, col- 8 and
23 section and page ids), every reference statement anchor still on a statement. `INFO` lists the added ids and
the anchored statements whose status changed: the content owner confirms each status change.

## 5. Atlas: mount, hardening and presence of the relation and reading-path data

```
P -B L/tests/atlas/atlas_test.py                                     # 19 mount and hardening checks
P -B L/tests/refuted/refuted_test.py                                 # 17 checks: statement status 'refuted form'
python3 -I -B L/tools/atlas_presence.py C/atlas.json O/page.html --json O/atlas-presence.json
```
Accept: atlas_test, refuted_test and atlas_presence `ALL PASS`. The successor payload may carry statements with the status
'refuted form' (checked scoped negatives; atlas scoped_negative): completeness (step 3) checks them like any other status. The presence check prescribes no atlas markup. For each
domain, claim, edge, comparison and reading path it reports where the page carries the item: `shown` (its
words are in section#atlas as text, SVG text or an accessible name), `addressed` (only its id is there),
`embedded` (only in a script's data, drawn at run time), or `absent` (fails). Every edge must join two claims
of the atlas. `addressed` and `embedded` counts name exactly what the browser check must judge.
On the 11:20 snapshot with the lane's test-only stub renderer: domains shown 9; claims addressed 503; edges,
comparisons and reading paths absent (the stub draws none of them). The real atlas renderer must turn these into
shown (or embedded and then judged in the browser). Controls: a full rendering of the snapshot gives all shown;
the snapshot as embedded data gives all embedded; one comparison removed gives exactly that one absent.
Reader-visible atlas text that the page audit rejects is listed in `L/ATLAS-INTAKE.md` (content owner).

## 6. DOM contract

```
python3 -I -B L/tools/contract_static.py O/page.html --candidate
```
Accept: `ALL PASS` (77 checks: 39 existing status.js hooks, 28 foundation structures, 10 attribute checks). A
failing hook names its owner lane (CONTRACT.json `owners`). Three hooks that status.js creates at run time
are checked only in the browser (step 9).

## 7. Contrast from the colour tokens

```
python3 -I -B L/tools/contrast_static.py compiler/quantum-holography-status/status.css
```
Accept: `ALL PASS` in light and dark (text 4.5:1, marks 3:1).

## 8. External gate (public page)

On the visible text of O/page.html (audit.visible_text) and on the whole file: the external-documents pattern
and the public-artifact source pattern (the commands are in `L/VERIFY.md`, row E17). Accept: 0 hits; no
internal path, hash, tool, model or process word anywhere in the file. The build audit (step 2) enforces the
reader-text rules as well.

## 9. Browser acceptance (root's approved tools only; this lane could not perform it)

On O/page.html, judged as page images beside the best exemplars (rhythm, harmony, balance, proportion,
communication and visualization), not by proxies. The full list is in `L/VERIFY.md` ("Required QA"): widths
1400, 1280, 1180, 1024, 768, 480, 375 (and 360, 320), light and dark; reduced motion; keyboard (table one tab
stop, arrows, Home, End, focus clears the sticky heading row, folds, search control, no trap); arrival by
address (related statement, a question's own statement, a counterexample witness, a row statement); print A4
and Letter with Legal and A5 as stress (every status chip, every statement, no blank page, no formula beyond
the page area); console free of errors on load and after interactions; status.js behaviours on the final
markup; the atlas items that step 5 reports as addressed or embedded.
