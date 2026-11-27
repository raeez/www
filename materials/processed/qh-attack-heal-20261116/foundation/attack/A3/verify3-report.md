A3 final targeted verification of A5-A3-01 to A5-A3-06: read-only, no browser.

**Convergence opinion for my lens: not converged until A6-A3-01 is healed.** A6-A3-01 is a new severity-3 defect: in five mixed related-statement lists, the new key reads as if every listed statement were proved and checked. A5-A3-02 to A5-A3-06 are verified, so A4-A3-05 is now fully healed. A4-A3-04 closes once A6-A3-01 is fixed. The open items under root's control are unchanged: rulings on 06, 07, the on-screen tally under 10, and 15; the content need 21; and the page image, 23, which remains unjudged.

**Candidate checked.** `preview.html` sha256 fa691a6a…92a7; `foundation.patch` bca64f25…; `GUARD.json` d5b38d5d…. The four guarded files match their candidate hashes, and `status-print.css` (e1d1d00b…) is unchanged since my last pass. CONTRACT.json was updated at 21:35 and its state block names this candidate and patch. I did not write `verify3.yaml` (my agent type cannot write files); the block below is ready to save as `attack/A3/verify3.yaml`.

**Re-run here (`python3 -I -B`, no `--json`):**
- `fidelity.py`: ALL PASS.
- `contract_static.py --candidate`: 77 PASS, including the new checks: the key appears exactly when a related statement is checked, and no hidden separator holds its own spaces.
- `anchors.py`: ALL PASS.
- `completeness.py`: ALL PASS.
- `contrast_static.py`: ALL PASS.

## Verdicts

| Item | Verdict | Static evidence | View root must take |
|---|---|---|---|
| **A5-A3-01** checked key on cards | partially-healed | status.py `frontier()` adds `span.known-key` (status.css: `.known-key`); it appears on 23 of 27 cards, exactly those with a checked related statement. Head width needed: about 537px at 1400 (label 173.8 + count 90.7 + key 248.2 + gaps 24) and 518px at 375. It is one line in the 582px measure (few-related cards at ≥1180px, and every card at 561–1179px). It wraps, with the key on its own line, in the 418px related column of two-column cards and at 375 (343px). New defect in 5 mixed lists: A6-A3-01. | Decisive cards 1, 5 and 4 at 1400 and 1024; a screen-reader pass over card 5 |
| **A5-A3-02** § numbers | verified-healed | page.json `labels.part` is `§{n}`, and so is the code default. Kickers read "§3 · Decisive questions", "§6 · Counterexamples": a section sign, not a count. Screen readers say "section 3". | Parts 3 and 6 at 1400 and 375 |
| **A5-A3-03** separator spaces | verified-healed | Markup: `§2 <span … aria-hidden="true">·</span> Established`; the date line reads `2026 <span…>·</span> Contents`. Accessible text is "§2 Established". The visible text is unchanged ("§2 · Established"). Contract check passes. | Screen-reader reading of one kicker and of the date line |
| **A5-A3-04** small-cap figures | verified-healed | `.kicker .part-num { font-variant-numeric: normal }`. HarfBuzz shapes "§3" as `section.sc` + `three.sc` (0.767em) and "§9" as `section.sc` + `nine.sc`: small-cap figures at one height. The embedded subset contains `section`, `section.sc` and `one.sc` to `nine.sc`. The contents keeps lining figures (`section` + `three`, 0.88em). | Heads §1, §4, §8 at 1400 |
| **A5-A3-05** contents numeral track | verified-healed | Track is `max(1.6em, var(--contents-num))`; status.py writes `--contents-num` as the longest label in ch (`2ch` here) in all three layouts. With `§{n}`: 33.3px at 1400 (label 15.2px), 32.1px at 1024, 30px at 375. With "Part {n}": 6ch = 59.9px at 1400 against a 38.6px label, and 54px at 375 against 37.2px, so it fits. At ≥1280 this leaves a 174px title track. | The contents at 375, 1024 and 1400; one build with `labels.part = 'Part {n}'` |
| **A5-A3-06** 32% band | verified-healed | status.css: 32% from 1100 to 1179.98px. Heading space against 4.683em needed: 4.98em at 1100, 5.18 at 1140, 5.37 at 1179.5; no broken words. Family names on one line: 10/20 at 1100, 12/20 at 1140 and 1179.5 (3–4 at 26%); never more than 2 lines. Table about 1,035 / 997 / 998px. | #examples at 1100, 1140, 1179.5 |
| **A4-A3-05** | fully healed | All of A5-A3-02 to A5-A3-05 verified. Wording stays root's choice. | — |
| **A4-A3-04** | not yet fully healed | Density and accessible names are healed; A6-A3-01 remains. | — |

**Regression checks:**
- **Search:** the key is not indexed as a statement. Question units skip `.question-known` (status.js:557), and statement units are only `main .statement` articles, which the key is not inside.
- **Accessibility and print:** see A6-A3-01 and A6-A3-02.
- **Date line:** no regression. It looks the same, and its accessible text is fixed.
- **Contract checks:** 77 PASS.
- **status.js hooks:** none affected. `.known-key`, `.kicker` and the contents' inline `--contents-num` style are not script hooks, and the CSP allows inline styles.

```yaml
pass: "A3 final targeted verification of A5-A3-01..06 (read-only, no browser; page image unjudged)"
candidate: {preview_sha256: fa691a6ab3ef46cdb8ccaa30ed1c27a84f877e2641ce3a42da4aed29c19692a7, patch_sha256: bca64f25905955ac135acd9458a76124b2ca5e13273ae143dfd47fad51f35c17, guard_sha256: d5b38d5dd7efe458ab29418196cfe235b7899575a40e79482c021f59b40385a1}
rechecks: {fidelity: "ALL PASS", contract_static: "77 PASS", anchors: "ALL PASS", completeness: "ALL PASS", contrast_static: "ALL PASS"}
verdicts:
  - {id: A5-A3-01, verdict: partially-healed, open: A6-A3-01}
  - {id: A5-A3-02, verdict: verified-healed}
  - {id: A5-A3-03, verdict: verified-healed}
  - {id: A5-A3-04, verdict: verified-healed}
  - {id: A5-A3-05, verdict: verified-healed}
  - {id: A5-A3-06, verdict: verified-healed}
  - {id: A4-A3-05, verdict: "fully healed (wording root's)"}
  - {id: A4-A3-04, verdict: "not fully healed until A6-A3-01"}
new_findings:
- id: A6-A3-01
  severity: 3
  status: valid
  lens: communication and accessibility (status accuracy in the related-statements head); regression from A5-A3-01
  target: "status.py frontier() known_key; status.css .known-key / .known-head"
  claim: The related-statements head never states a status the list contradicts.
  broken_step: >-
    [proved from markup] Five lists mix checked with other statuses: q-d-reduction-interface (3 checked, 1 conditional),
    q-d-native-stress (1 checked, 1 conditional), q-d-partner-hilbert (4 checked, 1 conditional),
    q-d-compact-igusa-source (1 open, 1 checked), q-d-interacting-curve (1 open, 1 checked). Their heads read
    "Related statements · N statements · Proved and independently checked". For assistive technology the key's mark is
    aria-hidden, so the head is heard as "2 statements, Proved and independently checked" above a list that holds an
    open problem or a conditional statement. Sighted readers see the key on the same line as the count in 3 of the 5
    at >=1180px (one-column cards: 537px needed in the 582px measure) and in all 5 at 561-1179px.
  evidence_type: line_reference
  evidence_ref: "preview.html known-heads (23 with key: 18 all-checked, 5 mixed); widths from hb-shape"
  files_read: [status.py, status.css, preview.html]
  tools_used: [python regex, hb-shape]
  confidence: medium
  blast_radius: 5 question cards; screen-reader users on every card with the key
  minimal_heal: >-
    Put aria-hidden="true" on span.known-key; each line's accessible name already carries its status. Add
    .known-key { flex-basis: 100% } so the key always stands on its own line under the label and count, read as a
    legend. The contract check counting span.known-key > svg.mark is unaffected.
  residual: none
  deciding_evidence: "Root's render of q-d-native-stress at 1400 and 1024, and a screen-reader reading of its head."
- id: A6-A3-02
  severity: 4
  status: valid
  lens: print (redundant key)
  target: "status-print.css (no .known-key rule); status-print.css:174-176 print each related statement with its own chip"
  claim: Printed question cards carry each status once.
  broken_step: "[proved from source] In print every related statement shows its own status chip, so the key in the head is redundant on paper and repeats the mixed-list reading of A6-A3-01."
  evidence_type: line_reference
  evidence_ref: "status-print.css .fold > .statement > .statement-head { display: flex }"
  files_read: [status-print.css, preview.html]
  tools_used: [Read]
  confidence: high
  blast_radius: printed question sections
  minimal_heal: "@media print { .known-key { display: none } } in status-print.css"
  residual: none
  deciding_evidence: "A4 PDF page with decisive card 5."
convergence: "Not converged for A3's lens until A6-A3-01 (severity 3) is healed; after that only root's rulings (06, 07, 10 tally, 15), content (21) and the page image (23) remain."
```
