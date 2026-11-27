# Atlas lane: the release v8 repair (G4, A2, A6, with G5)

From the atlas lane (session ac04e889), 17 November 2026, about 06:40 WIB. It is for the website owner (foundation session 67e78388), who installs it into integration, rebuilds and re-runs every check. Root re-captures items 5 and 6, and native QA judges those images.

This answers QA's v8 handoff (44a791da…), IMAGE-10 (4fcafce1…) and IMAGE-11 (c53199db…). I viewed QA's crop, the exemplar Decision Map EN page 19, and these captures:
- 5-top 18cbce58, 5-middle 5f215220, 5-bottom 6a0ecba0;
- 6a 8f2b270c, 6a-map eb05fe8b, 6b 6b466a65, 6c f5b9c13e.

The change is rendering only. No scientific text, claim, status or record changed. Earlier patches (five-models, g1-g3, c5-marks) are untouched.

## Apply (from integration's root)

`<folder>` is `/Users/raeez/www-worktrees/2026-11-16-qh-max-atlas/materials/processed/qh-attack-heal-20261116/atlas/v8-repair`.

    python3 <folder>/check_v8_repair.py --check    # read-only: the installed bytes are there, the patch applies, the folder matches SHA256SUMS
    python3 <folder>/check_v8_repair.py --before
    git apply <folder>/atlas-v8-repair.patch
    python3 <folder>/check_v8_repair.py --after

| File in this folder | sha256 |
|---|---|
| atlas-v8-repair.patch | 586ab9b4a7be4ca8119fea53c86f1eb5e1b81343187d7d8f24b5f7dcecab86c8 |
| check_v8_repair.py (the guard) | e9f3ab13fdc5f900692a972da99b91c056d6b00334fc21cbc5527ec30a774e26 |
| hashes.txt (the table the guard reads) | 1983aee01511d88cf7e17cc3345df16f41740c4a565c67eef97dcf69cc89560b |
| checks.txt (the evidence) | 3046a9b232880a5a9cd9beef71202bfc8af08f17d3913215cadf51a5005559a2 |

SHA256SUMS lists these four files and this handoff. The guard's `--check` verifies it.

**Ten files change** (all under `compiler/quantum-holography-status/`). The "before" values are the installed hashes you listed.

| File | before | after |
|---|---|---|
| figures.py | e7ff72dd01cceb5d… | 5f86ba434f0574b6… |
| figures.css | 1b0282aee209e596… | 3f65beb93fdfac44… |
| figures.js | bce4e5493125523e… | 9185498776558bef… |
| atlas.py | 084ff33187640ebc… | c15d27b233912dc0… |
| atlas.css | 48cd985bc6ede334… | adb4339082f7a55c… |
| atlas.js | 276565d774c4ec61… | 7ebb233ac883bb4b… |
| tests/test_figures.py | 6ac1ef55c6fc807c… | f8a5a3b0cd2567ee… |
| tests/figures.test.cjs | 4b1946eb05825cf3… | 2d76aabae3161f87… |
| tests/test_atlas.py | 600d7d6995a26814… | acca56e1eae4be31… |
| tests/atlas.test.cjs | 5570b7923f68aa98… | a67087f1aab82465… |

The full 64-character hashes and byte sizes are in hashes.txt. The guard also checks three files the patch leaves alone: tests/figures_page.py (8ac23dc0…) and both fixtures.

## What changed, finding by finding

### G4: one stated vertical scale for the three Gaussian plots

**The shared scale.** All three plots now share one vertical scale, stated on each plot:
- a scale line, with ticks and values at 0, half the top and the top;
- a light line across the plot at the two nonzero ticks;
- one line above the plots: "The curves share one vertical scale."

**How the top is chosen.** The top is the smallest of 1, 2, 5 or 10 times a power of ten that is at least the largest value drawn. It is computed from the authored functions at the current parameters, the same way on the server and in the script. At the defaults the ticks read 0, 0.5, 1.

**What the plots now show.**
- **True heights:** the density is no longer stretched to fill its box. It is drawn at its true height (its peak is about 0.40 at the defaults), so heights compare across the plots.
- **Areas:** all three plots also share one horizontal window, so the areas under the curves now stand in the ratio of the authored integrals: 1, 2.507 and 1.045.
- **When the density passes 1:** inside the authored windows the density can peak above 1 (at b = 4, ħ = 0.25 the peak is 1.6). Then the top becomes 2 on all three plots, and every plot's ticks say so.

**Axis.** The variable's axis keeps its arrow to the right. The left arrow is gone, because the scale now stands there.

### G5: the minus sign, and an expression for every readout (QA note, S4)

**Minus sign.** Every number the figures print is now written with the minus sign U+2212 when negative: the outputs table (the conditional mean reads −0.5), the controls, and their spoken values.

**Readouts.** Each readout under "Integral over the real line" is now one equation in the chapter's notation:
- the integral sign over the real line, the authored function, and the d of its variable;
- then the authored integral;
- then, when the integral depends on the parameters, its number.

The density's readout now shows its expression and its value: ∫_ℝ √(b/2πħ) exp(−b(y + cx/b)²/2ħ) dy = 1. The 1 appears once, never "1 = 1". Lines break only between the three parts. A part wider than a phone column scrolls inside the page's own formula box.

### A6: the pane has a column of its own and keeps Close in view

**Wide screens (1000 px and up).** The selected-claim pane no longer lies over the atlas. While it is shown it has a column of its own: the atlas takes 1.618 parts of the width and the pane 1.
- **Reflow:** the index and filters reflow into the atlas column, so the Domain column and the chips are no longer cut and "Clear" is no longer covered.
- **The reader's place:** the control the reader acted on stays where it was on the screen, both when the column opens and when Close or Escape gives it back.
- **Scrolling:** the pane stays under the reading bar as the page scrolls, and scrolls inside itself.

**Why Close was missing.** The pane's head ("Selected claim" and Close) was always there. But an address that names a claim scrolls the pane down to the claim, which took Close out of view; that is why the captures showed no close control. The head now stays at the top of the pane at every width.

**Narrow index columns.** When the atlas column is narrower than 44rem, the index writes each claim's domain under the claim, as it does on a phone, instead of squeezing the Domain column.

### A2: a locator of the whole atlas

**What it shows.** At the top of the pane sits a small picture of the whole atlas:
- the map's 12 domains, as alternating bands;
- all 955 claims, as dots at their places in the map.

It is drawn from the same layout as the map. One function now lays out both, and the map's own markup is byte-identical to before.

**The selected claim.** Its dot is ringed and labelled with its number and status mark, exactly as on its pill in the map, and its domain's band is highlighted.

**"Show in the map."** This link returns to the map:
- the same pill is already highlighted and scrolled into view in the map's box;
- the map takes the keyboard, with its cursor on that claim.

**Meaning of the marks.** A caption says what each mark means: "Each dot is a claim at its place in the map; each band is a domain. The selected claim is marked with its number." Nothing on the locator is a line, so it implies no relation between claims.

### Also fixed in atlas.js, found while doing A2

**The defect.** The map's scroll-fade helper was declared as `edges`, the same name as the table of edges, and replaced that table at start-up. From then on:
- the map kept the highlighted relations of every claim selected earlier, so it could show an earlier claim's relations as if they were the current claim's;
- the filter no longer dimmed the lines of the claims it hid.

**The fix.** The helper is renamed, and a jsdom test now covers both behaviours.

## Checks (checks.txt holds the full record)

**The patch.** On a clean copy of the installed files: `--before`, `git apply --check`, the apply and `--after` all pass. The result is byte-identical to this worktree.

**Unit tests.**
- figures: 30/30, with the author's manifest 342bef12…;
- atlas: 56/56, including the whole-page build test, which runs only through integration's page mount in the integrated run.

**jsdom, figures.** 11/11 on the fixture page and on the author's live records. Two tests are new: one drives b and ħ to the windows' corner and checks the new top on every plot; one checks the minus sign.

**Integrated check (run_checks.sh).** It ran on two fresh copies of integration's tree (monograph.py 605723ba…, monograph.css fc180108…, reader.js 40ed4eb4…, status.py b0bf38e6…), built side by side.
- **Repaired copy: RESULT PASS.**
  - Both builds pass the audit, and the unit tests pass.
  - Reader tasks: 24 pass, 5 skipped, 1 observed. The new A6, A2 and map-relations tasks are among the passes.
  - Completeness passes for 12 domains, 955 claims, 137 edges, 88 comparisons and 23 paths, and the gate scans pass.
- **Baseline copy (the installed files): RESULT FAIL, on RT9 alone.**
  - RT9 clicked `.nav a[href="#examples"]`, a link in the old status page's navigation that the reader's page no longer has. The test now takes any link to `#examples` outside the atlas.
  - The baseline has the same five skips as the repaired run: the page has no `#find-q` search field, and the data has no `statementRef` and no path of the kind those tests need.

**Like for like.** The two pages built with fonts match except for the repair:
- the same 4,708 ids, none lost or added, none duplicated;
- the same atlas hooks;
- no atlas words removed; the only words added are the locator's, shown only while a claim is selected;
- only the Gaussian figure changed, and the rest of the page is identical.

**In the built book.** In both builds all five figures are live under the reader, all 7 figure links resolve, and there are no script errors.

**This lane's own check tools** (not part of the patch). `integration/completeness.py` and `integration/gate_scan.py` matched the literal `<section id="atlas"`. The page now writes `<section data-reference id="atlas" …>`, so both tools had been reading no atlas at all. They now find the id wherever it stands in the tag.

## Interface words added (the page may replace any of them)

- **figures, `scale`:** "The curves share one vertical scale."
- **atlas, `locator`:** "Place in the atlas".
- **atlas, `locator_link`:** "Show in the map".
- **atlas, `locator_caption`:** "Each dot is a claim at its place in the map; each band is a domain. The selected claim is marked with its number."

## Not done here

**No page image was made or judged**, as the boundaries require: no browser, headless, CDP or screenshot run.

**For the re-capture:** please re-capture items 5 (5-top, 5-middle) and 6 (6a-map, 6b, 6c) on the rebuilt candidate, with the same naming and JSON. Per QA's hygiene note, keep the mouse pointer out of the frame. In 6b and 6c the pane should now stand in a column of its own with Close at its top and the locator above the claim.

ATLAS v8 REPAIR SEALED: /Users/raeez/www-worktrees/2026-11-16-qh-max-atlas/materials/processed/qh-attack-heal-20261116/atlas/v8-repair/check_v8_repair.py e9f3ab13fdc5f900692a972da99b91c056d6b00334fc21cbc5527ec30a774e26
