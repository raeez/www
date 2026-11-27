A3 targeted re-verification of A4-A3-01 to A4-A3-10: read-only, no browser.

**Convergence opinion for my lens: not converged.** Eight of the ten heals are verified: 01, 02, 03, 06, 07, 08, 09 and 10. Two are only partly healed, 04 (fold status) and 05 (part numbers). This batch also added two new severity-3 communication defects:
- **A5-A3-01:** on question cards, the checked status of related statements is no longer named anywhere on the card.
- **A5-A3-02:** a bare part number in front of a plural noun reads as a count. "3 · Decisive questions" sits over 22 questions, and "6 · Counterexamples" over 11.

Root's rulings (06, 07, the on-screen tally under 10, 15), the content need (21) and the page image (23) remain open.

**Candidate checked.** `preview.html` sha256 38261852…dc61; `foundation.patch` 2ac5acfc…; `GUARD.json` cf9f4f3f…. The four guarded files match their candidate hashes. I did not write `verify2.yaml` (my agent type cannot write files); the block below is ready to save as `attack/A3/verify2.yaml`.

**Re-run here (`python3 -I -B`, no `--json`):**
- `fidelity.py`: ALL PASS.
- `contract_static.py --candidate`: ALL PASS (74 checks).
- `anchors.py`: ALL PASS (183 statement anchors).
- `completeness.py`: ALL PASS.
- `contrast_static.py`: ALL PASS.

I did not run the builds, the atlas tests or `atlas_presence.py`.

Widths below were shaped with HarfBuzz on the embedded EB Garamond. The longest heading word needs 4.683em, and the longest heading is 8.802em, both including the .02em tracking.

## Verdicts

| Item | Verdict | Static evidence | View root must take |
|---|---|---|---|
| **A4-A3-01** matrix headings | verified-healed | Rules: heading text at `--text-fig` at every width (status.css:247); 26% family column from 1000.02 to 1179.98px (:399); upright headings at ≤1000px (:400); static header on short screens at ≤1000px (:411). Heading space available, in em, against 4.683 needed: 5.31 at 1400; 4.85 at 1180; 5.89 at 1179.5; 5.47 at 1100; 5.06 at 1024; 4.93 at 1000.5. No word breaks at any of these widths. Family names take at most 2 lines everywhere above 1000px. Upright header height: 155px at 1000, 152px at 768, 147px at 375 (it was 165px). Table height: about 838px at 1400 (fits a 1400×900 window), 876px at 1180, 1,159–1,173px across the 26% band, 964px at 1000, 1,123px at 768, 1,566px at 375. Print headings are now 8.74pt and fit with 5.25em of space. | Header row of #examples at 1400, 1180, 1100, 1024, 1000.5, 1000, 768, 375 |
| **A4-A3-02** status chip | verified-healed | status.css:414. The chip is 290.0px in a 307.9px box at 375, and 289.6px in 293.0px at 360. A3-A3-14 is therefore now healed too. | #results at 375 and 360 |
| **A4-A3-03** row names | verified-healed | status.css:302: family names at body size. At 1400: 39 lines in a 255px track, one name on 3 lines; the closed list is about 1,699px (it was about 2,202px). At 768: 41 lines in 229.7px, three names on 3 lines; about 1,647px. | Closed rows at 1400 and 768 |
| **A4-A3-04** fold status | partially-healed | status.py:643: 96 checked status texts are now visually hidden; 6 "Open problem" and 3 "Conditional" stay visible. A checked line drops from about 96px to about 71px. The hidden text stays in each line's accessible name. Communication cost: see A5-A3-01. | Decisive card 1 (12 checked) and card 4 (mixed) at 1400, read by a cold reader |
| **A4-A3-05** part numbers | partially-healed | All nine heads now have a kicker line (status.py:441–442, :950, :985–988). The contents numbers match the section numbers, and contract check 74 passes. New problems: A5-A3-02 to A5-A3-05. | Consecutive section heads at 1400 and 375; a screen reader on one kicker |
| **A4-A3-06** contract and reports | verified-healed | CONTRACT.json (21:17), VERIFY.md and REPORT.md (21:19) cite 38261852…, 2ac5acfc… and cf9f4f3f…. They describe 38% / 26% / upright ≤1000px, `.few-known`, 31mm, 38em, 150mm, the allowed atlas classes, `question_anchor`, the section heads and the hidden fold status. A search for the old values (1080, 21%, 13mm, 170mm, 40em, the index caption) finds nothing. | Final diff of the frozen documents against the candidate |
| **A4-A3-07** breakpoint gaps | verified-healed | Breakpoints now at 1179.98px (:595), 1040.02px (:394) and 1000.02px (:399). Windows of 0.02px remain, which zoomed widths do not reach in practice (severity 5, not filed). | Zoomed render near 1180px |
| **A4-A3-08** overview frame | verified-healed | status.css:626–630. Reading column: 352.2–927.8 at 1280, 408.8–991.2 at 1400, 666–1254 at 1920. Contents text ends on the frame: 987–1240 at 1280, 1052–1308 at 1400, 1318–1568 at 1920. | Overview at 1280, 1400, 1920 |
| **A4-A3-09** card heads | verified-healed | status.css:584. Card heads are at most 582.4px, which is 51 characters at 29.95px. The 56-character comparison title wraps to 2 lines inside the measure. | #frontier comparison 9 at 1400 |
| **A4-A3-10** leading and spacing | verified-healed | Line-heights are now 4 tokens (status.css:23) plus 4 deliberate literals: .86, inherit, 32px, 40px. The card, key, column definitions, legend, change list and search sit on `--s1` to `--s3`; the remaining literals are horizontal gaps or the insides of controls. Print: `--lh-text` 1.42 (status-print.css:41, :48, :108), so the print line step `--lh` is 15.9pt. The 150mm formula cap is unchanged: the leading change does not move anything horizontally, and the worst case still has 0.37mm to spare (left-anchored, A4, row statement). | A4 and Letter PDF page with a row statement; half-line grid overlay |

**Regression checks:**
- **Part-number kickers:** one structure everywhere. The section outline and landmark names are unchanged (the number sits in a `<p>`, not the h2), and the kickers print. Problems are listed as A5-A3-02 to A5-A3-05.
- **Contents numeral track:** works at both ends. At ≤560px it is 30px plus an 18px gap, with the count under the title. At ≥1280px the title track is 200.5px, about 30 characters at 1400.
- **Hidden checked status:** the text is still read aloud, but sighted readers lose the label (A5-A3-01).
- **Spacing and leading tokens:** no defect found.
  - Within-item gaps are now half the between-item gaps in the key and column definitions (8px against 16px).
  - Search chip heights are unchanged.
  - A focused table cell still clears the sticky header: 66px + 9.5em lands at 205–214px, below the 197–205px of header and bar.
- **Print:** no regression.
- **26% band:** family names stay legible (16.66–16.96px, at most 2 lines). The cost is that 17 of 20 names wrap, and the table is about 1,167px at 1024 against about 1,002px before. A refinement is offered as A5-A3-06.
- **status.js:** no hook broke. The contract check passes, and `.fold-status`, `.kicker` and `.contents-num` are not script hooks.

```yaml
pass: "A3 targeted re-verification of A4-A3-01..10 (read-only, no browser; page image unjudged)"
candidate: {preview_sha256: 38261852da87229d0952fa6dda89abd3b519fd2c4fef3d3cf52ccfa5f735dc61, patch_sha256: 2ac5acfc0401dc014946e7fdb7c5e7051f63c65493f46c01d78c5f819ddf1b2f, guard_sha256: cf9f4f3f7c72ca268b945ed89351d864baee7906dc298a585dc7850fc4caff25}
rechecks: {fidelity: "ALL PASS", contract_static: "ALL PASS (74)", anchors: "ALL PASS", completeness: "ALL PASS", contrast_static: "ALL PASS"}
verdicts:
  - {id: A4-A3-01, verdict: verified-healed}
  - {id: A4-A3-02, verdict: verified-healed, also_heals: A3-A3-14}
  - {id: A4-A3-03, verdict: verified-healed}
  - {id: A4-A3-04, verdict: partially-healed, healed: "density (checked fold 96 -> 71px), accessible name", open: A5-A3-01}
  - {id: A4-A3-05, verdict: partially-healed, healed: "one head structure, contents numbers equal", open: [A5-A3-02, A5-A3-03, A5-A3-04, A5-A3-05]}
  - {id: A4-A3-06, verdict: verified-healed}
  - {id: A4-A3-07, verdict: verified-healed, note: "0.02px windows remain, unreachable in practice (severity 5, not filed)"}
  - {id: A4-A3-08, verdict: verified-healed}
  - {id: A4-A3-09, verdict: verified-healed}
  - {id: A4-A3-10, verdict: verified-healed, note: "150mm cap unaffected by the print leading (0.37mm worst case unchanged)"}
new_findings:
- id: A5-A3-01
  severity: 3
  status: valid
  lens: communication (what is established toward a question); regression from A4-A3-04
  target: "status.py:643 (checked fold status visually hidden); status.py known-head in frontier(); status.css .known-head"
  claim: A question card tells a sighted reader which related statements are established.
  broken_step: >-
    [proved from markup] 96 of 105 related lines now show only a 12px disc and the title. The card head reads
    "Related statements · N statements" and names no status. The disc is named only in the key (part 1) and the matrix
    legend (part 5). A cold reader who goes contents -> part 3 -> card 1 sees 12 unlabelled lines. Only the 6 open and
    3 conditional lines carry words.
  evidence_type: line_reference
  evidence_ref: "preview.html: fold-status visually-hidden x96, visible x9; known-head x27 without a status legend"
  files_read: [status.py, status.css, preview.html]
  tools_used: [python regex]
  confidence: medium
  blast_radius: all 27 cards with related statements; the reader route's established results
  minimal_heal: >-
    In the known-head, when the list has a hidden checked status, add one legend item from existing words, with no
    counts: <span class="known-key">{mark('checked')}<span>{status_label('checked')}</span></span>, styled like
    .legend (xs, ink-3, 12px mark). The search skips it because it sits inside .question-known. The 71px folds stay.
  residual: none
  deciding_evidence: "Root's render of decisive card 1 at 1400 and 375; cold-reader check that the established items are understood without the key."
- id: A5-A3-02
  severity: 3
  status: valid
  lens: communication (numbers that read as counts); regression from A4-A3-05
  target: "page.json labels.part '{n}'; status.py:441-442"
  claim: Part numbers read as numbers of parts, not as quantities.
  broken_step: >-
    [proved from markup] With the default '{n}', a bare numeral comes before the kicker words: "3 · Decisive questions"
    and "6 · Counterexamples", in small caps. A numeral before a plural noun reads as a count, on a page whose contents
    say "22 questions" and "11 counterexamples" and whose cards say "12 statements". Misread, these kickers give false
    counts (3 against 22, 6 against 11).
  evidence_type: line_reference
  evidence_ref: "preview.html section heads; contents holds"
  files_read: [page.json, status.py, preview.html]
  tools_used: [python regex]
  confidence: medium
  blast_radius: parts 3 and 6, which also feed the contents' meaning
  minimal_heal: >-
    page.json labels.part = '§{n}' (15.2px; fits the 1.6em contents track), or 'Part {n}' together with the
    A5-A3-05 track change; root chooses the wording.
  residual: Wording is root's.
  deciding_evidence: Root's render of parts 3 and 6 at 1400; cold-reader reading of the kicker.
- id: A5-A3-03
  severity: 4
  status: valid
  lens: accessibility (kicker text)
  target: "status.py:441"
  claim: The kicker's accessible text separates the number from the words.
  broken_step: >-
    [proved from markup] Markup is <span class="part-num">2</span><span class="sep" aria-hidden="true"> · </span>
    Established. The spaces sit inside the hidden span, so the accessible text, built from the inline spans, is
    "2Established" (braille shows it run together).
  evidence_type: line_reference
  evidence_ref: preview.html kicker markup
  files_read: [status.py, preview.html]
  tools_used: [python regex]
  confidence: medium
  blast_radius: 4 worded kickers
  minimal_heal: "Keep the spaces outside: <span class=\"part-num\">2</span> <span class=\"sep\" aria-hidden=\"true\">·</span> Established (as .statement-notes .sep already does)"
  residual: none
  deciding_evidence: Screen reader and braille reading of a kicker.
- id: A5-A3-04
  severity: 4
  status: valid
  lens: harmony (part numerals)
  target: "status.css:163 (.kicker font-variant-numeric: oldstyle-nums), :615 (.contents-num lining tabular)"
  claim: A part number keeps one figure style and an even height.
  broken_step: >-
    [computed, HarfBuzz] With all-small-caps and onum, kicker digits shape to one.tosf ... nine.tosf (tabular
    oldstyle). Lone kickers 1, 4, 5, 7, 8 therefore sit at three heights: 1 at x-height; 4, 5, 7 descending; 8
    ascending. The contents shows the same numbers in lining figures. Without onum, the font's small-cap figures
    (one.sc ...) are uniform and match the small caps.
  evidence_type: counterexample
  evidence_ref: "hb-shape --features=+smcp,+c2sc,+onum -> .tosf; +smcp,+c2sc -> .sc"
  files_read: [status.css, EBGaramond-Regular.otf]
  tools_used: [hb-shape]
  confidence: medium
  blast_radius: 9 section heads
  minimal_heal: ".kicker .part-num { font-variant-numeric: normal } (small-cap figures under all-small-caps)"
  residual: none
  deciding_evidence: Root's render of heads 1, 4, 8 at 1400.
- id: A5-A3-05
  severity: 4
  status: valid
  lens: proportion (contents numeral track); latent
  target: "status.css:611 (.contents a 1.6em track), the <=560 and >=1280 variants"
  claim: The documented 'part' template (CONTRACT section_heads, for example 'Part {n}') fits the contents.
  broken_step: "[computed] 'Part 2' is 38.6px against a 33.3px track at 1400 (37.7px against 30px at 375); 'Part 10' is 46.9px. The numerals lose their right alignment and run into the 18px gap. '§{n}' is 15.2px and fits."
  evidence_type: counterexample
  evidence_ref: hb-shape lnum+tnum widths
  files_read: [status.css, CONTRACT.json]
  tools_used: [hb-shape]
  confidence: high
  blast_radius: the contents, if root picks a worded template
  minimal_heal: "grid-template-columns: minmax(1.6em, max-content) minmax(0, 1fr) auto (and the 2-track variants), or document '§{n}' as the worded option"
  residual: none
  deciding_evidence: Build with labels.part 'Part {n}', render the contents at 1400 and 375.
- id: A5-A3-06
  severity: 5
  status: valid
  lens: proportion (26% band, optional)
  target: "status.css:399"
  claim: The narrowed family column is as wide as the headings allow.
  broken_step: "[computed] At 26%, 3-4 of 20 names fit one line and the table is about 1,160-1,173px tall. 32% keeps whole-word headings from 1100px (4.98em at 1100, 5.37 at 1179.5) and puts 10-12 names on one line; 32% breaks at 1024 (4.61em)."
  evidence_type: other
  evidence_ref: HarfBuzz greedy wrap
  files_read: [status.css, content.json]
  tools_used: [hb-shape]
  confidence: high
  blast_radius: matrix at 1100-1179px
  minimal_heal: "26% at 1000.02-1099.98px, 32% at 1100-1179.98px"
  residual: none
  deciding_evidence: Root's render of #examples at 1100 and 1179.
convergence: "Not converged for A3's lens: 8 of 10 heals verified, 04 and 05 partial; open severity 3: A5-A3-01 (checked status unnamed on cards), A5-A3-02 (bare part numbers read as counts); plus root rulings (06, 07, 10 tally, 15), content (21), page image (23)."
```
