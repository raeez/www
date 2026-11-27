A3 verification of A6-A3-01, A6-A3-02 and the four design decisions: read-only, no browser.

**Convergence opinion for my lens: converged on static evidence.** No severity 1–3 finding remains in this batch. All six items are verified. Four new findings are severity 4 or 5, none blocking:
- **A7-A3-01:** in print the key comes after about 49 pages of opened example rows.
- **A7-A3-02:** status.js still orders the search in the old page order (another lane's file).
- **A7-A3-03:** the atlas, now first, decides how deep the results and the matrix sit in the combined page.
- **A7-A3-04:** observation only — the solid diamond for "Proposed" weighs about as much as the checked disc.

Two items stay open: the hypotheses field, which needs content (A3-A3-21), and the page image (A3-A3-23), which remains unjudged until root's approved visual, print, keyboard and console checks.

**Candidate checked.** `preview.html` sha256 67ef592b…ad79; `foundation.patch` c0ae9e9c…; `GUARD.json` 1fddf985…. The four guarded files match their candidate hashes. `status.js` and `content.json` are unchanged. I did not write `verify4.yaml` (my agent type cannot write files); the block below is ready to save as `attack/A3/verify4.yaml`.

**Re-run here (`python3 -I -B`, no `--json`):** all five checks pass.
- `fidelity.py`: ALL PASS.
- `contract_static.py --candidate`: 77 PASS.
- `anchors.py`: ALL PASS; no anchored statement changed status.
- `completeness.py`: ALL PASS.
- `contrast_static.py`: ALL PASS.

## Verdicts

| Item | Verdict | Static evidence | View root must take |
|---|---|---|---|
| **A6-A3-01** key in the related-statements head | verified-healed | status.py `known_key` now has `aria-hidden="true"`; status.css `.known-key` has `flex-basis: 100%`. The head is two lines: label and count, then the key on its own line (248 px at 1400). Screen readers hear "Related statements, 4 statements" and then each line's own status. This closes A5-A3-01, and A4-A3-04 is now fully healed. | q-d-native-stress at 1400 and 1024; screen-reader pass |
| **A6-A3-02** key in print | verified-healed | status-print.css: `.known-key { display: none !important }`. | A4 PDF, decisive card 5 |
| **A3-A3-06** section order | verified-healed | Main, bar and contents all run: results, examples, key, decisive, frontier, open, failures, essay, terms. The key has no bar item but is §3 in the contents. Estimated with the font metrics, all disclosures closed:<br>• 1400: the lead ends at ≈1,444 px. The first result is +503 px later. The matrix is +7,760 px later, at ≈9,200 px (about 10 screens of 900 px; it was ≈36,500).<br>• 375: the lead ends at ≈1,521 px. The first result is +1,209 px later. The matrix is +10,567 px later, at ≈12,100 px (about 18 screens of 667 px; it was ≈52,200).<br>What remains (§4–§6) now reads together. | Scroll positions at 1400 and 375 in root's composed page |
| **A3-A3-07** key placement | verified-healed (decision recorded); print issue in A7-A3-01 | The key follows the matrix and its 20 closed rows; the matrix legend links to it. The question statements stay open, with the basis recorded in the ledger. | — |
| **A3-A3-10** tally | verified-healed | No `span.count` remains. The label is "Statements by status". As a legend it reads mark plus label: 2 rows at 1400, 3 at 375. The `.tally a[data-filter]` links (4), `main > .tally` and the search insertion after it are intact. The facet chips are built from the row filters, so stripping `.count` is a no-op. | Overview at 1400 and 375 |
| **A3-A3-15** marks | verified-healed | status.py MARKS: "Proposed" is a solid diamond, "Partly established" a solid triangle; the other eight marks are unchanged. In units of the 16-unit mark box: the triangle carries about 69 units² of ink, against 98.5 for the checked disc, so it reads lighter, as an order rather than a fraction. Its box centre sits 0.8 units high and its centroid 0.73 units low, about 0.8 px either way at 17 px. At 11 px it is 8.1 × 7.2 px against a 7.7 px disc. The matrix's six statuses have six shape families (disc, triangle, ring, square, dash, cross), so they stay distinct in forced colours and in print. | Matrix at 1400 and 375, monochrome print, forced colours |

## Regression checks

- **status.js:**
  - The search scopes keep their fixed old order (status.js:445). See A7-A3-02.
  - The bar's current-section marking (`aria-current`) is unaffected: the key was never in the bar or observed, and observation order does not matter.
  - The tally hooks and the search insertion are intact.
- **Print:**
  - Order is results, examples (new page), key, the questions, then essay and terms (new pages).
  - Head and keep-together breaks are intact.
  - The key's position is A7-A3-01.
- **Reader route:** overview → contents §4 or the bar → question index → card still takes two activations. The question's statement and its related statements, with the key, are visible.
- **Root's preservation conditions:** met.
  - Every statement: fidelity and completeness pass.
  - Every anchor: anchors.py passes; ids are unchanged.
  - Discoverability: the key is reachable from the contents and the matrix legend; statuses from the tally and the search.
  - Complete programme view: the matrix is §2.

```yaml
pass: "A3 verification of A6-A3-01/02 and design decisions A3-A3-06, 07, 10 (tally), 15 (read-only, no browser; page image unjudged)"
candidate: {preview_sha256: 67ef592b623b94f778f9aa8dee3c32329d6492b6bb4a6a998dcf4d7fbc07ad79, patch_sha256: c0ae9e9cc91beb4b20acfd04d1247431b41c7bddd5e30562ecfedc4e5dc2c3c3, guard_sha256: 1fddf9850f78ec85fc2222a160802f47f639e1bf87e4d916c1e3ce08e5b315f2}
rechecks: {fidelity: "ALL PASS", contract_static: "77 PASS", anchors: "ALL PASS", completeness: "ALL PASS", contrast_static: "ALL PASS"}
verdicts:
  - {id: A6-A3-01, verdict: verified-healed, closes: [A5-A3-01, A4-A3-04]}
  - {id: A6-A3-02, verdict: verified-healed}
  - {id: A3-A3-06, verdict: verified-healed, evidence: "matrix +7,760px after the lead at 1400 (was ~35,000), +10,567px at 375 (was ~50,700)"}
  - {id: A3-A3-07, verdict: verified-healed, residual: A7-A3-01}
  - {id: A3-A3-10, verdict: verified-healed}
  - {id: A3-A3-15, verdict: verified-healed, observation: A7-A3-04}
new_findings:
- id: A7-A3-01
  severity: 4
  status: valid
  lens: print (position of the key)
  target: "status.py main order {examples}{key}; status-print.css #examples break-before page; status.js opens every details before print"
  claim: On paper, the key stands near the matrix it explains.
  broken_step: >-
    [computed estimate] Print opens all 20 example rows (109 statements, 160 status-by-column lines), so the key (§3)
    prints after about 49 A4 pages of rows (11.2pt, 1.42 leading, 282pt row-statement column). Before this batch it
    printed on page 2. Nothing is left unlabelled on paper: the compact legend under the matrix prints, and every
    statement chip carries its status in words. The key's definitions are far from first use.
  evidence_type: other
  evidence_ref: "line estimate from content.json row statements and the print tokens"
  files_read: [status.py, status-print.css, content.json]
  tools_used: [python estimate]
  confidence: medium
  blast_radius: printed copies only
  minimal_heal: >-
    Either put {key} before {examples} (§2 key, §3 examples; on screen the matrix moves down by the key, about 770px
    at 1400 and 930px at 375), or keep the screen order and state the printed position in VERIFY.md for root's
    PDF check.
  residual: Root chooses the trade-off.
  deciding_evidence: "A4 and Letter PDFs: the page numbers of the matrix and the key."
- id: A7-A3-02
  severity: 4
  status: valid
  lens: search order (cross-lane, status.js)
  target: "status.js:445 SCOPES; CONTRACT cross_lane_proposals/interaction[0]"
  claim: The search's Part chips and result groups follow the page order.
  broken_step: "[proved from source] SCOPES is fixed as results, decisive, frontier, examples, failures, open, essay, terms. The page, the bar and the contents now read results, examples, decisive, frontier, open, failures. Search works, but its groups list Examples after the comparisons and Counterexamples before Open."
  evidence_type: line_reference
  evidence_ref: "status.js:445, :737, :858"
  files_read: [status.js, CONTRACT.json]
  tools_used: [grep]
  confidence: high
  blast_radius: search facets and result grouping
  minimal_heal: "Interaction lane: build SCOPES from document order, as the recorded proposal says (add atlas when present)."
  residual: Owned by the interaction lane; root integrates.
  deciding_evidence: "A search for a common word in the composed page: the order of the groups."
- id: A7-A3-03
  severity: 4
  status: valid
  lens: integration (atlas placement and the depth of the matrix)
  target: "CONTRACT atlas_mount_tested/placement (the atlas now precedes section#results)"
  claim: The matrix stays early in the composed page.
  broken_step: "The atlas (9 domains, 503 scoped claims) now precedes the results and the matrix. Its rendered height adds directly to the measured depths: about 9,200px (1400) and 12,100px (375) without the atlas. This lane cannot measure it."
  evidence_type: other
  evidence_ref: "page order; estimator values above"
  files_read: [CONTRACT.json, status.py]
  tools_used: [Read]
  confidence: medium
  blast_radius: overview to matrix distance in the integrated page
  minimal_heal: "Root measures the composed page. If the atlas is long, the atlas lane renders a compact overview with disclosure, keeping every claim reachable."
  residual: Depends on the atlas lane's layout snapshot.
  deciding_evidence: "Scroll position of #examples in root's composed candidate at 1400 and 375."
- id: A7-A3-04
  severity: 5
  status: valid
  lens: visualization (weight of the Proposed mark)
  target: "status.py MARKS['pending']"
  claim: A proposal does not look as solid as a proved result.
  broken_step: "[computed] The solid diamond with its 1.6 stroke carries about 95.5 units² of ink, against 98.5 for the checked disc, and its box is larger (13.2 against 11.2 units, about 2px at 17px). In monochrome a proposal weighs the same as a proved result. The current content has no pending statements or cells; the coming snapshot may."
  evidence_type: other
  evidence_ref: "polygon area plus stroke offset: A + P*d + pi*d^2"
  files_read: [status.py]
  tools_used: [arithmetic]
  confidence: medium
  blast_radius: future pending items
  minimal_heal: "Optional: an outline diamond with a solid centre dot, so the claim family stays distinct by fill; or keep the shape and the key's wording."
  residual: none
  deciding_evidence: "Root's view of a pending fixture next to a checked mark at 12 and 17px."
convergence: "Converged on static evidence for A3's lens: no severity 1-3 finding remains; A7-A3-01..04 are severity 4-5; open: content need A3-A3-21 and root's page-image acceptance A3-A3-23."
```
