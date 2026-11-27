A3 verification of the foundation batch: read-only, no browser.

**Convergence opinion for my lens: not converged.** The batch heals my entries 01, 02, 04, 05, 09, 13, 16, 17, 18, 19, 20 and 22 on static evidence, and 10 except the on-screen tally. Six severity-3 items are still open (A4-A3-01 to A4-A3-06 below): one of my original findings, A3-A3-14, is not healed; two are new regressions; two are what remains of partly healed findings; and the cross-lane contract is out of date. Root still has to rule on 06, 07, the on-screen tally under 10, and 15; 21 needs content; 23, the page image, remains unjudged.

**Candidate checked.** `preview.html` sha256 15ff3966…c78a; `foundation.patch` 00d8169f…; `GUARD.json` 7cc0445e…. The four guarded files match their candidate hashes. I did not write `verify.yaml` (my agent type cannot write files); the block below is ready to save as `attack/A3/verify.yaml`.

**Re-run here, read-only:**
- `tools/fidelity.py`: ALL PASS (formula elements 2502 → 2503, every baseline formula present).
- `tools/contract_static.py`: ALL PASS.
- `tools/contrast_static.py`: ALL PASS.
- No `.mix` elements remain in the markup, and no status mark in either question index.

I did not re-run `atlas_test.py`, because it writes build output inside the checkout; I read its source instead.

**Static basis.** Text widths come from fontTools advances and HarfBuzz shaping of the embedded EB Garamond. At 1400 / 1024 / 768 / 480 / 375 the body is 20.80 / 20.05 / 19.54 / 18.96 / 18.75 px. Every judgment of how the page looks is unverified; each row names the view root must take with approved tools.

## Verdicts

| Item | Verdict | Static evidence | View root must take |
|---|---|---|---|
| **A3-A3-01** measure | verified-healed | status.css:12, :55. Measure 582.4 / 561.3 / 547.0 / 441.6 / 343 px. Characters per line: 73.7 / 73.7 / 73.7 / 61.3 / 48.1 (0.380 em average). Statement text at 1400 is 536 px, about 68 characters. Body x-height at 375 is 7.6 px. | Lead and a principal statement at 1400, 1024, 768, beside index.html |
| **A3-A3-02** type scale | verified-healed | status.css:13–21, :89. One ratio: 1.2, and 1.125 at ≤560px. The essay title is r2 and h2 is r3, so the title sits below h2 at every width (ratio .833, or .889 at ≤560). 14 font-size expressions, down from 19. The off-scale `--text-fig` (.78) remains, but only in the table. | #essay at 375 and 768 |
| **A3-A3-03** rhythm | partially-healed | The gaps between blocks use `--s1` to `--s6` (14 token expressions). Still off the scale: 18 line-heights, 17 px and 24 em spacing values in search, card, key, column definitions, legend and change list. Print tokens use 1.55 leading against a print body leading of 1.42. See A4-A3-10. | A question card and the example rows at 1400 with a half-line grid overlay |
| **A3-A3-04** frames | verified-healed (at ≥1180px; see the notes after the table) | At 1400: reading column 408.8–991.2. The cards' left padding is (1216 − 582.4)/2 = 316.8, so cards start at 408.8. Two-column cards: 439.0 / 42 / 418.1, ending at 1308. One-column cards: 408.8–991.2. At 1180: reading column and cards both start at 304.95; columns 409.6 / 35.4 / 390.1. Bar and footer content now 92–1308 (status.css:120, :360). Legend and column definitions on the reading column (:267). | #decisive and #frontier at 1180 and 1400 |
| **A3-A3-05** contents gutter | verified-healed (residual in A4-A3-08) | status.css:623–624. Text runs 987–1236 at 1280 and 1052–1356 at 1400, 44 px from the window edge at both. | Overview at 1280, 1366, 1400, 1440 |
| **A3-A3-08** matrix | partially-healed; new regression A4-A3-01 | From 1214px up: at 1400 all 20 family names fit one line, the header is 62 px and the table about 842 px, so it fits a 1400 × 900 window under the 50 px bar. Between 761 and 1213px, column headings break words mid-word. At ≤760px the upright header is 165 px at 375 (it was 135). | #examples at 1400×900, 1180, 1024, 768, 375 |
| **A3-A3-09** row summaries | verified-healed; new regression A4-A3-03 | status.css:296: fixed 109 px mark track and 5em count track. "15 statements" is 90.7 px in 104 px at 1400 and 85.2 px in 97.7 px at 768, so the marks hold one x position down the list. No status counts. | Closed rows at 1400 and 768 |
| **A3-A3-10** counts | verified-healed for contents, indexes, card heads and print; on-screen tally waits for a ruling | status.py:524–535 and :675–697; index caption removed; status-print.css:53 hides the tally in print. | Root ruling on the tally |
| **A3-A3-11** labels | partially-healed; see A4-A3-04 | The fold status now sits under the title, fold titles are weight 400, and no index marks remain. Kept: the "The question" label and 34 identical "Open problem" chips; 96 repeated status lines. | Decisive card 1 at 1400 |
| **A3-A3-12** kickers | partially-healed; see A4-A3-05 | Repeated kickers are gone (status.py:431–435), but 5 of 9 sections now have no kicker. | All nine section heads at 1400 |
| **A3-A3-13** harmony | verified-healed | 15 small-caps rules, no uppercase, no pill radius (4 px only on chips you can press). Links in ink (status.css:100–101). Oldstyle figures in labels. | Beside index.html at 1400 and 375 |
| **A3-A3-14** chip wrap | **not-healed** at 375 and 360 (reported as healed) | See A4-A3-02. | #results at 375 and 360 |
| **A3-A3-16** colour | verified-healed | Links are ink. Teal is kept only for hover, focus and selection, and the matrix has no conditional cells. | Dark theme: a conditional statement next to a link |
| **A3-A3-17** dark not-posed | verified-healed | #807a73 is 3.16:1 on the dark selection tint #1f3234 and 4.05:1 on #1d1b18. | A selected not-posed cell in dark mode |
| **A3-A3-18** print | verified-healed (tight) | 116 mm at 11.2 pt gives about 77 characters; 72 in a statement, 66 in a row statement. Tightest context, a row statement on A4: the formula box spans 12.63–174.26 mm of the 178 mm page area. A formula rendered at the estimate's worst ratio (1.10 × 150 = 165 mm) spans 10.95–175.95 mm centred, or 12.63–177.63 mm left-anchored. Both fit, with 0.4 mm to spare in the worst case. | A4 and Letter PDFs showing the widest formulas inside a row statement |
| **A3-A3-19** column-name track | verified-healed | status.css:412: 9.2em, and the widest name is 8.98em. | An opened row at 1400 |
| **A3-A3-20** stripe | verified-healed | status.css:201: the stripe is now a 3 px left border; the `::before` stripe is gone. | Zoomed card corner |
| **A3-A3-22** card balance | verified-healed | 12 two-column cards (3 or more related), 15 one-column cards with 1–2 related. Estimated empty area about 18%, down from about 44%. | Decisive cards 5–9 at 1400 |
| 06, 07, 15, 10 (tally) | not healed: root rulings | — | — |
| 21 | not healed: content | — | — |
| 23 | undecided: root acceptance | — | — |
| **A3-A2-01** reserved classes | verified-healed (static) | status.py:267–272 and :300–303; atlas_test.py:76–84 with `stub_atlas_rich.py`. I did not re-run the test. | — |
| **A3-A2-02** | same as A3-A3-05: verified | — | — |
| **A3-A2-03** overview link | verified (static) | status.css:143. The `:has()` rule outranks `.nav-top`. Behaviour depends on status.js setting `aria-current`, which I could not exercise. | Render at ≤1040 with Programme as the current section |
| **A3-A2-05** print resets | verified | status-print.css:133 and :136 have the same specificity as the screen rules, (0,2,2) and (0,3,2), and come later, so they win. | Printed table |
| **A2-A1-09** contents link | verified | The date line now ends with `<a href="#contents">Contents</a>`. | — |

**Notes on A3-A3-04:**
- **Breakpoint gap:** a gap between 1179 and 1180px leaves zoomed windows with neither layout (A4-A3-07).
- **Card heads:** heads of two-column and no-related cards may be 736 px wide, wider than the reading column (A4-A3-09).
- **Question column width:** in two-column cards the question column narrows to 47–50 characters, against 68 just below 1180px. That is within range; recorded only as an observation.

**status.js hooks.** Every hook in the contract is still present: the static contract check passes, and the tally, filters, the `--find-styled` property, `.status-chip`, `.row-count`, `details.known` and `main > .tally` are all intact. Behaviour could not be exercised (no jsdom, no browser).

```yaml
pass: "A3 verification of the foundation batch (read-only, no browser; page image unjudged)"
candidate: {preview_sha256: 15ff3966ca4f63ff71b060f63b89b26f3c7e44610a87226f4c3efbc7a861c78a, patch_sha256: 00d8169f25a9d08f608a8b763d8bc69e94cf7730461c0c969319ecd379d510b1, guard_sha256: 7cc0445e757187fd02916425c6f52c76ff1e90d2d08b6f747962f0bf49ecabd4}
rechecks: {fidelity: "ALL PASS", contract_static: "ALL PASS", contrast_static: "ALL PASS"}
verdicts:
  - {id: A3-A3-01, verdict: verified-healed}
  - {id: A3-A3-02, verdict: verified-healed, residual: "--text-fig .78 off-scale, table only"}
  - {id: A3-A3-03, verdict: partially-healed, residual: A4-A3-10}
  - {id: A3-A3-04, verdict: verified-healed, notes: [A4-A3-07, A4-A3-09]}
  - {id: A3-A3-05, verdict: verified-healed, residual: A4-A3-08}
  - {id: A3-A3-08, verdict: partially-healed, regression: A4-A3-01}
  - {id: A3-A3-09, verdict: verified-healed, regression: A4-A3-03}
  - {id: A3-A3-10, verdict: "verified-healed except on-screen tally (ruling)"}
  - {id: A3-A3-11, verdict: partially-healed, residual: A4-A3-04}
  - {id: A3-A3-12, verdict: partially-healed, residual: A4-A3-05}
  - {id: A3-A3-13, verdict: verified-healed}
  - {id: A3-A3-14, verdict: not-healed, misclassified_as: healed, see: A4-A3-02}
  - {id: A3-A3-16, verdict: verified-healed}
  - {id: A3-A3-17, verdict: verified-healed}
  - {id: A3-A3-18, verdict: verified-healed, note: "worst case leaves 0.4mm on A4"}
  - {id: A3-A3-19, verdict: verified-healed}
  - {id: A3-A3-20, verdict: verified-healed}
  - {id: A3-A3-22, verdict: verified-healed}
  - {id: A3-A3-06, verdict: "not healed (root ruling)"}
  - {id: A3-A3-07, verdict: "not healed (root ruling)"}
  - {id: A3-A3-15, verdict: "not healed (root ruling)"}
  - {id: A3-A3-21, verdict: "not healed (content)"}
  - {id: A3-A3-23, verdict: "undecided (root acceptance)"}
  - {id: A3-A2-01, verdict: "verified-healed (static; test not re-run)"}
  - {id: A3-A2-02, verdict: verified-healed}
  - {id: A3-A2-03, verdict: "verified (static)"}
  - {id: A3-A2-05, verdict: verified}
  - {id: A2-A1-09, verdict: verified}
new_findings:
- id: A4-A3-01
  severity: 3
  status: valid
  lens: visualization (matrix column headings); regression
  target: "status.css:234 (corner 38% at every width), :245 (.col-head font-size var(--text-xs)), :396-405 (upright headings only <=760px)"
  claim: The eight column headings (the parts of the theory) read as whole words at every width.
  broken_step: >-
    [computed, HarfBuzz] Each heading needs a mark column at least 4.683em of the heading font wide ("comparison" with .02em
    tracking) plus 8px padding. With the family column at 38% and headings at .833 x body, the space available is:
    4.55em at 1180, 4.21 at 1100, 3.89 at 1024, 3.40 at 900, 2.86 at 768. Words therefore break mid-word: 2 at 1180,
    3 at 1100, 4 at 1024 (comparison twice, operations, endpoints), 6 at 900, and 9 at 768, where 6 of 8 headings are
    hit and the header is about 5 lines (118px). Before the batch: 0 at 1024 (5.99em) and 1 at 768. At <=560px the
    upright headings use .889 x body (16.67px at 375) while family names use .78, so the sticky header is about 165px;
    with the 50px bar that is 32% of a 667px screen (about 135px before).
  evidence_type: counterexample
  evidence_ref: "hb-shape word widths (comparison 4.483em, operations 4.042, endpoints 3.848, geometry 3.564, exchange 3.454, Physical 3.064, Algebra 3.005, Module 3.039); table width min(1216, vw - 2 gutter) - 2"
  files_read: [status.css, content.json, EBGaramond-Regular.otf]
  tools_used: [hb-shape, python arithmetic]
  confidence: high
  blast_radius: matrix header at 761-1213px and <=760px (representative widths 1024 and 768)
  minimal_heal: >-
    Set .col-head { font-size: var(--text-fig) } at every screen width. Family column 38% at >=1180px (headings get
    4.85-5.31em); 26% at 1001-1179px (>=4.94em); and the <=760 upright-heading rules extended to <=1000px (header about
    152-156px at 768-1000 and about 147px at 375). Alternative: upright headings at every width <=1213px.
  residual: Height of the upright header on tablets is a judgment for the page image.
  deciding_evidence: Root's render of the #examples header row at 1180, 1024, 900, 768, 375.
- id: A4-A3-02
  severity: 3
  status: valid
  lens: proportion at 375/360 (status chip); A3-A3-14 not healed
  target: "status.css:89 (--r-1 .889 at <=560px), :208-209, :409"
  claim: Status chips stay on one line at the representative widths.
  broken_step: >-
    [computed, HarfBuzz] "Proved and independently checked" in all-small-caps is 16.26em. At 375 the label size is
    16.67px: 271.0px text + 26.7px tracking (.05em) + 13px mark + 6px gap = 316.7px, against a 307.9px content box.
    At 360 it is 316.2px against 293.0px. It fits from 390 (322.9px). The chip wraps on every checked statement (197)
    at 375 and 360.
  evidence_type: counterexample
  evidence_ref: "hb-shape --features=+c2sc,+smcp; statement padding var(--s2)+2px / var(--s2), borders 3px + 1px"
  files_read: [status.css]
  tools_used: [hb-shape]
  confidence: high
  blast_radius: about 197 status labels on small phones
  minimal_heal: "@media (max-width: 420px) { .status-chip { letter-spacing: 0 } } gives 290.0px at 375 and 289.6px at 360 (fits 293.0)."
  residual: 3.4px spare at 360.
  deciding_evidence: Root's render of #results at 375 and 360.
- id: A4-A3-03
  severity: 3
  status: valid
  lens: proportion (example row list); regression
  target: "status.css:300 (.row-name at --text-h3 = 1.2 x body), :296 (row tracks)"
  claim: Family names in the row list keep a compact, even rhythm.
  broken_step: >-
    [computed] The family name track is 255px at 1400 (240 at 1024, 230 at 768). The name moved from 1.06 x to 1.2 x
    body; the nearest scale step to 1.06 is 1.0. Total name lines at 1400 rise from 37 to 48: 8 of 20 names now take
    three lines and none fits one. The closed list grows from about 1,560px to about 2,200px (+41%). At body size the
    same track gives 39 lines.
  evidence_type: line_reference
  evidence_ref: "greedy wrap with EB Garamond advances; track = measure - 4 - 2em - 109 - 5em - 1em - 48"
  files_read: [status.css, content.json]
  tools_used: [hb-shape, python]
  confidence: high
  blast_radius: the 20-row list at >560px
  minimal_heal: ".row-name { font-size: var(--text-base) }"
  residual: none
  deciding_evidence: Root's render of the closed rows at 1400 and 768.
- id: A4-A3-04
  severity: 3
  status: valid
  lens: communication/density (related-statement lists); remainder of A3-A3-11
  target: "status.css:485-490; status.py:626-636"
  claim: Each related-statement line carries only information the reader needs.
  broken_step: >-
    [computed] The status now has its own line under each title, so 96 of 105 folds repeat "Proved and independently
    checked" as a second line. The realigned related column is 418px at 1400 (390 at 1180; 573 before), so 74 of 86
    titles in two-column cards still wrap to two lines (title track 350.5px). A fold grows from about 72px to about
    96px. A 14-item list is about 1,290px, against about 950px if the status line showed only where it differs. In
    4 cards the related column (1,130-1,348px) now outweighs the question (687-924px).
  evidence_type: line_reference
  evidence_ref: "fold height = 2 x s1 + lines x 1.3 x body + 2 + 1.3 x xs + 1; preview.html fold-status counts 96/6/3"
  files_read: [status.css, status.py, preview.html]
  tools_used: [hb-shape, python estimator]
  confidence: medium
  blast_radius: 105 folds; 12 two-column cards
  minimal_heal: "status.py fold(): add class visually-hidden to the fold-status span when the status is 'checked' (the mark still shows it; the accessible name keeps the text); conditional and open lines stay visible."
  residual: none
  deciding_evidence: Root's render of decisive card 3 (14 related) at 1400.
- id: A4-A3-05
  severity: 3
  status: valid
  lens: rhythm/communication (section heads)
  target: "status.py:431-435 (kicker subset rule); page.json kicker labels"
  claim: Section heads follow one structure.
  broken_step: >-
    [proved from markup] The rule removes 5 of 9 kickers (status, frontier, examples, open, essay) and keeps 4
    (Established, Decisive questions, Counterexamples, Glossary). The two parallel question sections now differ: a
    kicker over "Constructions that would change the programme", none over "The remaining comparisons". Section heads
    alternate between two-line and one-line forms; a kicker line is s1 + 1.55 x 17.33px, about 35px at 1400.
  evidence_type: line_reference
  evidence_ref: "preview.html section heads"
  files_read: [status.py, page.json, preview.html]
  tools_used: [python regex]
  confidence: medium
  blast_radius: all nine section heads
  minimal_heal: "One scheme: part numbers in contents order from one page.json label template, or non-repeating kickers for the five sections, or no kickers; root chooses wording."
  residual: Wording is root's.
  deciding_evidence: Root's render of consecutive section heads at 1400.
- id: A4-A3-06
  severity: 3
  status: valid
  lens: deliverable accuracy (cross-lane contract)
  target: "CONTRACT.json (19:47) and VERIFY.md (19:51), both predating the 20:37 batch"
  claim: The contract delivered to root describes the candidate.
  broken_step: >-
    [proved from source] Stale entries:
    (1) grid layout "21%; 20% <=1100px; 23% <=900px; 38% <=760px": now 38% at every screen width.
    (2) q-index-cap "visible caption over the counts column": removed.
    (3) ".question.compare[.no-known]": .few-known is missing (1-2 related, one column).
    (4) print .math-display "widened 13mm": now 31mm on a 116mm measure.
    (5) formulas "--fw ... wider than 40em ... 170mm": status.py:133 says 38em and the print cap is 150mm
    (status-print.css:118).
    (6) atlas namespace and hardening list term, math-display and math-long as reserved: not reserved
    (status.py:269-272).
    (7) the ctx entry lacks question_anchor (status.py:300-303).
    (8) VERIFY.md:43 "two columns at >=1080px": now >=1180px and only for 3 or more related statements.
  evidence_type: source_conflict
  evidence_ref: "CONTRACT.json foundation_additions_tested/*, atlas_mount_tested/{namespace,hardening,ctx}; VERIFY.md:43"
  files_read: [CONTRACT.json, VERIFY.md, status.py, status.css, status-print.css]
  tools_used: [python json walk, grep]
  confidence: high
  blast_radius: root integration and the atlas lane
  minimal_heal: Update those entries (and REPORT.md where repeated) before freezing.
  residual: none
  deciding_evidence: Diff of the frozen CONTRACT.json and VERIFY.md against the candidate.
- id: A4-A3-07
  severity: 4
  status: valid
  lens: balance (breakpoint gap)
  target: "status.css:576 (min-width: 1180px), :590 (max-width: 1179px)"
  claim: Every width has one question layout.
  broken_step: "At fractional widths between 1179 and 1180 (browser zoom) neither rule applies: one-column cards span the wide frame, about 1,100px."
  evidence_type: line_reference
  evidence_ref: media query ranges
  files_read: [status.css]
  tools_used: [Read]
  confidence: high
  blast_radius: zoomed windows near 1180px
  minimal_heal: "@media (max-width: 1179.98px), or the range form (width < 1180px)"
  residual: none
  deciding_evidence: Render at a zoom giving 1179.5px.
- id: A4-A3-08
  severity: 4
  status: valid
  lens: balance (overview frame)
  target: "status.css:619-628"
  claim: The contents ends on the page frame.
  broken_step: "[computed] From 1297px up the contents runs past the wide frame: text ends at 1356 (rule at 1360) at 1400 while the bar and wide sections end at 1308 (+52px); +13px at 1600, +73px at 1920."
  evidence_type: line_reference
  evidence_ref: "col3 = (vw - (measure + 80))/2; contents max-width 22rem + gutter"
  files_read: [status.css]
  tools_used: [arithmetic]
  confidence: high
  blast_radius: first screen at wide desktops
  minimal_heal: ".overview { max-width: calc(var(--wide) + 2 * var(--gutter)); margin-inline: auto; padding-inline: max(var(--gutter), env(safe-area-inset-left)) max(var(--gutter), env(safe-area-inset-right)) } and .overview > .contents { padding-right: 0 }. The reading column stays at 408.8 and the contents runs 1052-1308 at 1400; 1280 is unchanged."
  residual: none
  deciding_evidence: Overview at 1400 and 1920.
- id: A4-A3-09
  severity: 4
  status: valid
  lens: alignment (card heads)
  target: "status.css:579"
  claim: Card titles stay within their card's text column.
  broken_step: "[computed] At >=1180 the heads of two-column and no-related cards are up to 46rem (736px) while the no-related question column is 582.4px; 'Quantum operations with the required higher source terms' sets as one 637px line past 991.2 at 1400."
  evidence_type: line_reference
  evidence_ref: "29.95px x 0.380em per character"
  files_read: [status.css, content.json]
  tools_used: [arithmetic]
  confidence: medium
  blast_radius: 7 no-related cards and 12 two-column cards
  minimal_heal: ".question.compare > .question-head { max-width: var(--measure) } at >=1180px"
  residual: none
  deciding_evidence: #frontier comparison 9 at 1400.
- id: A4-A3-10
  severity: 4
  status: valid
  lens: rhythm (remainder of A3-A3-03)
  target: "status.css line-heights and inner spacing; status-print.css:47"
  claim: Line pitches and inner spacing follow the tokens.
  broken_step: "[computed] 18 line-heights remain (1.06-1.6, .86, 32px, 40px). Search (14/12/18/10px), card (14/16/12px), key dd (.2em), column definitions (.6/.8em), legend (6px) and change list (12px) are off the scale. In print, --lh = 1.55 x 11.2pt = 17.4pt against a body leading of 1.42 (15.9pt)."
  evidence_type: line_reference
  evidence_ref: regex inventory of status.css
  files_read: [status.css, status-print.css]
  tools_used: [python]
  confidence: medium
  blast_radius: secondary components; print cadence
  minimal_heal: "Remaining vertical spacing on --s1 to --s3; three line-height tokens (1.55 text, 1.3 compact, 1.18 display); print :root --lh: calc(var(--text-base) * 1.42)."
  residual: none
  deciding_evidence: Half-line overlay on root's renders; A4 PDF page.
convergence: "Not converged for A3's lens: six severity-3 items open (A4-A3-01 to -06; -02 is A3-A3-14 not healed), plus root rulings (06, 07, 10 tally, 15), content (21) and the unjudged page image (23)."
```
