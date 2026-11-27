A3 confirmation of the A7-A3-01 and A7-A3-04 heals: read-only, no browser, so how the page looks is still unjudged.

**Convergence opinion for my lens: converged on static evidence.** Both heals are verified and I found no regression and no new finding. Still open, none of them blocking and none mine to heal: A7-A3-02 (status.js search order, interaction lane) and A7-A3-03 (atlas depth, for root and the atlas lane), both severity 4; A3-A3-21 (a content need); and A3-A3-23, the page image, which stays with root's approved visual, print, keyboard and console checks.

**Candidate checked.** preview.html sha256 f1155923…01a0; patch 21508153…; guard df0aeca7…. All four guarded files match their candidate hashes. Only status.py changed since my last pass; status.css, status-print.css, page.json and status.js are unchanged. I did not write verify5.yaml (my agent type cannot write files); the block below is ready to save as `attack/A3/verify5.yaml`.

**Re-run here (`python3 -I -B`, no `--json`):** fidelity, anchors and completeness are ALL PASS; contract_static.py `--candidate` passes all 77 checks, including "every section head carries the part number of its contents entry".

```yaml
pass: "A3 confirmation of A7-A3-01 and A7-A3-04 (read-only, no browser; page image unjudged)"
candidate: {preview_sha256: f11559230bb5d566cddc5b74034206c44eb7cbcdd5cfc0416f9f45f86e1201a0, patch_sha256: 215081535563b19a0d3ab18bbbf3706d7afa6a151d3733c37a2ef1ffa6474684, guard_sha256: df0aeca7df616a03bf45c3321af905be2fc9d9698647005d7bb5998162ba46f0}
rechecks: {fidelity: "ALL PASS", contract_static: "77 PASS", anchors: "ALL PASS", completeness: "ALL PASS"}
verdicts:
  - id: A7-A3-01
    verdict: verified-healed
    evidence: >-
      status.py main order is now results, status (the key), examples, decisive, frontier, open, failures, essay,
      terms; the contents read §1 results, §2 key, §3 examples, and the section heads carry the same numbers.
      Printed position: status-print.css starts #examples on a new page, so the key prints just before the matrix
      page (formerly about 49 A4 pages after it).
      Screen cost, estimated from font metrics with all disclosures closed: the key section is about 905px at 1400
      and about 1,087px at 375.
      Lead to matrix at 1400: +8,665px, table at about 10,100px, 11.2 screens of 900px. Last pass +7,760px;
      first assessment about +35,000px.
      Lead to matrix at 375: +11,654px, about 13,200px, 19.8 screens of 667px. Last pass +10,567px; first
      assessment about +50,700px.
      The first principal result is unchanged: +503px (1400) and +1,209px (375) after the lead.
    root_view: "A4 and Letter PDFs (key directly before the matrix page); scroll position of #examples at 1400 and 375"
  - id: A7-A3-04
    verdict: verified-healed
    evidence: >-
      The pending (Proposed) mark is now a solid diamond with no stroke, spanning 2.4-13.6 units: the disc's box
      exactly.
      Ink in units squared of the 16-unit box: disc 98.5, triangle 69.0 (70%), diamond 62.7 (64%), so the proved
      result is the strongest mark.
      Rendered sizes:
        - 11px: disc and diamond 7.7px, triangle 8.1 x 7.2px
        - 12px: disc and diamond 8.4px, triangle 8.9 x 7.8px
        - 17px: disc and diamond 11.9px, triangle 12.5 x 11.1px
      The diamond stays distinct by fill from the conjecture's outline diamond, whose outer box is 13.2 units.
      Pending appears once, in the key.
    root_view: "The key's Proposed and Conjecture items next to the checked mark at 12 and 17px, and in monochrome print"
regression_checks:
  contents_vs_heads: "Equal: §1 results, §2 key, §3 examples, §4 decisive ... (contract check passes)"
  bar: "Unchanged: programme, results, examples, decisive, frontier, open, failures, essay, terms. The key has no bar item; it is reached from the contents (§2) and the matrix legend's link."
  status_js: "No hook touched; the search is still inserted after the tally; SCOPES (no key) and the bar's current-section tracking are unaffected by the order change."
new_findings: []
convergence: "Converged on static evidence for A3's lens: A7-A3-01 and A7-A3-04 verified, no regression; open and not blocking: A7-A3-02 (status.js) and A7-A3-03 (atlas depth) for other owners, content need A3-A3-21, root's page-image acceptance A3-A3-23."
```
