A3 bounded check of the two delta patches: F1 (status-language ruling) and F2 (successor fields). Read-only, no browser.

**Convergence opinion for these two deltas: F1 is verified; F2 is not converged.** F2 has two severity-3 defects:
- **A10-A3-01:** between 561 and 1179px, the orientation groups run the full wide frame in one column, so their text lines are 95–142 characters long.
- **A10-A3-02:** with the successor page's 11 bar items, the bar's last links are cut off with no fade at 1041–1146px and 1181–1267px.

There are four severity-4 items besides (A10-A3-03 to A10-A3-06). The page image stays unjudged.

I read the ruling in full; both ruling files match the hashes root gave. I did not write `verify6.yaml` (my agent type cannot write files); the block below is ready to save.

**Re-run here (`python3 -I -B`, no `--json`):**
- `contract_static.py --candidate`: ALL PASS on the F1 page, the F2 baseline-content page and the successor page.
- `anchors.py` on F1: ALL PASS.
- `completeness.py` on F1: ALL PASS.
- `fidelity.py` on F1 against the original baseline: E6 fails, and only because of the ruled labels (A10-A3-05). E5 passes, so status codes are unchanged.
- `completeness.py` on the successor page against the current composed folder: fails, because that folder changed after the page was built (A10-A3-06).

## F1: verified
- **Every status label comes from the stored code** (page.json `status_labels`, selected in status.py through `status_label()`). Checked on every surface:
  - Card chips: 197 Established, 74 Remaining, 6 Conditional, 4 Published.
  - Table cells' accessible names, cell cards and the family "by column" lines: Established, Partial, Not posed, Remaining, Published, Scoped negative.
  - Legend, key headings, family filters and the overview status line.
  - Related-statement lines (96 Established, visually hidden; 6 Remaining; 3 Conditional) and the key line under their heading (23).
  - The stub atlas's mark labels on the successor page: Established, Scoped negative, Conditional, Remaining.
  - status.js has no status wording of its own; it reads chip text from the page.
- **No old status-label wording remains** in status.py, status.css, status-print.css, status.js, page.json or any of the three pages. Two things are not status labels:
  - The section name "Open problems" and the bar's "Open". CONTRACT records them as deliberately unchanged section wording.
  - The counterexample tag "False", which carries the refuted-form mark. Root has routed that card wording to the content owner.
- **Colours and codes unchanged.** F1 does not touch the CSS, and fidelity E5 passes.
- **The fail-closed key rule is safe.** Both the baseline content's key and the current composed content's key cover every status in use (statements: checked, conditional, open, published, refuted form; cells: checked, partial, not posed, open, published, refuted form).

## F2: verified parts
- **No change for content without the new fields.** The F1 page and the F2 baseline-content page have the same font-independent hash, 14388a28….
- **Orientation section structure:** h2 for the section, an h3 per group and for the guidance, and a description list (dt/dd) for the guidance. Spacing and type use the rhythm tokens. Print sets the groups in block flow and keeps each group whole.
- **Groups grid:** two columns of 575.8px (gap 64.5px) at 1400, two of 518.4px at 1180, and one column of 343px at 375. The broken band is A10-A3-01.
- **Summary** sits after the statement heading and before the hypotheses and text, on all 9 principal results.
- **Date line:** `<time datetime="2026-11-16T13:50:00Z">` reads "16 November 2026, 13:50 UTC", in the cover line and the footer.
- **Atlas links:** 29 statements carry an atlas claim, all 29 links resolve, and none is dead. Claim ids are at most 51 characters, so the 60-character truncation causes no anchor collisions.
- **`scientific_atlas`** is validated against `atlas.json` (path, schema, asOf).
- **status.js hooks:** no hook changed. Orientation has a bar item, so the bar's section tracking covers it. Orientation is not in the search scopes; that is recorded as a cross-lane proposal.

```yaml
pass: "A3 bounded check of F1 (status language) and F2 (successor fields); read-only, no browser; page image unjudged"
inputs: {ruling_sha256: d6b665dea0a56670f3396970c699172c22def7b72502dcd0a5ad555b4620a242, patch_json_sha256: 6b7a84b8db4d20e74c776160074aef026a333c280c23be8aead331c6c4483c4c, f1_patch: 9613254535445e7ad38c6f591b403309a89f4dd87ed24b2a79f24fba143a6ad8, f2_patch: bb8262b80a6e1398844fa3ccad83edbb4be2a864c9cdde226e1dac18704697bb}
verdicts:
  - {item: F1, verdict: verified, evidence: "labels by stored code on every surface; no old status-label wording; colours/codes unchanged (fidelity E5 PASS); fail-closed key covers baseline and composed content"}
  - {item: F2, verdict: partially-verified, open: [A10-A3-01, A10-A3-02, A10-A3-03, A10-A3-04]}
  - {item: F2-no-op-on-baseline-content, verdict: verified, evidence: "font-independent hash 14388a28... for both pages"}
findings:
- id: A10-A3-01
  severity: 3
  status: valid
  lens: proportion (orientation groups measure)
  target: "F2 status.css .pfs { max-width: var(--wide) } (one column below 1180px)"
  claim: Orientation prose keeps the reading measure at every width.
  broken_step: "[computed] Below 1180px .pfs is one column but as wide as the wide frame: 1099px at 1179, 944px at 1024, 706.6px at 768. That gives about 142, 124 and 95 characters per line for the group texts (186-219 characters each). The explanation and the guidance are held to the 28-body measure; the groups are not. At >=1180px the left column starts at the wide frame (x=92 at 1400), not at the reading column (408.8): a minor alignment point, the same pattern as the glossary."
  evidence_type: line_reference
  evidence_ref: "F2 status.css .pfs rule; widths min(1216, vw - 2*gutter); 0.38em per character"
  confidence: high
  blast_radius: orientation section at 561-1179px (1024 and 768 included)
  minimal_heal: ".pfs { max-width: var(--measure) } and @media (min-width: 1180px) { .pfs { max-width: var(--wide); grid-template-columns: repeat(2, minmax(0, 1fr)) } }"
  deciding_evidence: "Root's render of #orientation at 1024 and 768."
- id: A10-A3-02
  severity: 3
  status: valid
  lens: usability (bar navigation)
  target: "F2 status.py nav item 'orientation'; status.css:417 @media (min-width: 1040.02px) { .nav { mask-image: none } }"
  claim: Every bar link is visible, or the bar shows that it scrolls.
  broken_step: >-
    [computed, HarfBuzz] The successor page's bar has 11 items (Programme, Orientation, Atlas, Results, Examples,
    Decisive questions, Comparisons, Open, Counterexamples, Essay, Terms). Space needed against space available:
    991 vs 926px at 1100, 997 vs 900px at 1181, 987 vs 867px at 1041. The overflow passes the list's 24px end padding
    at 1041-1146px and 1181-1267px. At those widths the end fade is switched off, the bar has no scrollbar, and
    "Terms" plus part of "Essay" are cut off without a cue. It fits, or the overflow stays inside the padding, at
    1147-1180px and from 1268px. The Atlas item alone (no Orientation) would cut off only at 1041-1063px and
    1181-1185px.
  evidence_type: counterexample
  evidence_ref: "hb-shape nav labels at text-sm; bar-inner arithmetic"
  confidence: medium
  blast_radius: common laptop widths 1041-1267px
  minimal_heal: "Delete status.css:417, so the end fade marks overflow at every width (it covers only the list's 24px end padding when the links fit); optionally drop the Orientation bar item (it is §1, right after the cover)."
  deciding_evidence: "Root's render of the bar at 1100 and 1200 on the composed page."
- id: A10-A3-03
  severity: 4
  status: valid
  lens: search and print (atlas link text)
  target: "F2 status.py p.statement-atlas inside each article; status.js statement-unit skip list (HEAD)"
  claim: The atlas link adds no noise to search or print.
  broken_step: "status.js indexes each statement article, skipping only .statement-head, .statement-notes .note-label and .added-chip. 'In the atlas' therefore becomes searchable text of the 29 linked statements, and a search for 'atlas' returns all 29. On paper the link prints as a bare 'In the atlas' with no target."
  evidence_type: line_reference
  evidence_ref: "status.js:537-551; preview statement-atlas x29"
  confidence: high
  blast_radius: search results for 'atlas'; printed cards
  minimal_heal: "Emit the link inside the statement notes as <span class=\"note-label\"><a href=…>In the atlas</a></span> (search already skips it), and hide it in print."
  deciding_evidence: "A search for 'atlas' in the composed page; A4 PDF of a linked statement."
- id: A10-A3-04
  severity: 4
  status: valid
  lens: typography (date line at 375)
  target: "F2 as_of_html + cover date line separator"
  claim: The date line breaks cleanly on a phone.
  broken_step: "[computed, HarfBuzz] 'Last updated 16 November 2026, 13:50 UTC · Contents' is 21.64em, 360.7px at 375 against 343px. It breaks after the separator, so line 1 ends with '·' and 'Contents' stands alone on line 2."
  evidence_type: counterexample
  evidence_ref: "hb-shape; .as-of at text-sm (16.67px)"
  confidence: high
  blast_radius: cover at <=~395px
  minimal_heal: "Bind the separator to its link: ' <span class=\"sep\" aria-hidden=\"true\">·</span>&nbsp;<a …>' (accessible text unchanged), so the line breaks before '· Contents'."
  deciding_evidence: "Root's render of the cover at 375."
- id: A10-A3-05
  severity: 4
  status: valid
  lens: verification bookkeeping
  target: "tools/fidelity.py on the F1 page"
  claim: Root's fidelity gate reads clean for F1.
  broken_step: "Against the original baseline, fidelity E6 now fails (rows; status key). I checked every row: each differs only by the old-to-new label map plus the earlier removal of the per-row status mix. It is a ruled change, not a loss, but the gate reports FIDELITY FAILURES."
  evidence_type: failing_test
  evidence_ref: "python3 -I -B tools/fidelity.py baseline/preview.html preview.html"
  confidence: high
  blast_radius: acceptance reading of the F1 delta
  minimal_heal: "Record the allowance (old->new label map) in VERIFY.md and CONTRACT, or give fidelity.py a label map for E6."
  deciding_evidence: "A label-mapped E6 run passes."
- id: A10-A3-06
  severity: 4
  status: valid
  lens: integration (input drift)
  target: "tests/successor/out/successor-followup.html vs the composed folder"
  claim: The successor checks describe the current composed preview.
  broken_step: "The page was built from content 967de4d7... and atlas 9acebb93.... The composed folder now holds content 89c382de... and atlas f02f29ec... (rewritten 22:49:45). Completeness against the current folder fails on 3 decisive statements, 2 family summaries and the essay (words not shown). This is drift, not a renderer defect; the new folder's status key still covers every status."
  evidence_type: other
  evidence_ref: "shasum of composed files; completeness.py output"
  confidence: high
  blast_radius: successor acceptance record
  minimal_heal: "Rebuild the successor preview from the sealed snapshot and re-run completeness, anchors and contract_static (no code change)."
  deciding_evidence: "completeness ALL PASS on the sealed snapshot."
convergence: "F1 verified. F2 not converged: two severity-3 defects (A10-A3-01 orientation measure at 561-1179px; A10-A3-02 bar links cut off without a cue at 1041-1146 and 1181-1267px) and four severity-4 items."
```
