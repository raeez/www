A3 confirmation of the A10-A3 heals in F2, and of the lead's correction to my verify6 evidence. Read-only, no browser.

**Convergence opinion: F1 and F2 are verified on static evidence, and I found no new defect.** One thing is left: the successor checks must be re-run on root's sealed composed snapshot, because the composed folder has changed twice since the lead's builds. The page image remains unjudged.

**Correction confirmed independently, and my verify6 point is withdrawn.** I wrote that F2 changes nothing for content without the new fields, because both pages hashed 14388a28…. That compared two F1 builds. The correct statement:
- The F1 page (`L/preview.html`) hashes to 14388a28… and the genuine F2 page (`L/followup/out/preview-f2.html`) to c56be5c4…, both with the font payloads replaced (that tool is not on the allowed list, so I ran its logic inline).
- Head and script are identical.
- The body differs by exactly one `&nbsp;` (the date line's separator binding); with it undone, the bodies are equal.
- The CSS differs by the new F2 rules, which have nothing to style on the baseline content, and by the removed 1040.02px fade rule.
- The copy's build script is now a real file, byte-identical to the worktree's, so the copy builds from its own producer. The successor checks import the copy's `status.py` through `sys.path`, as the lead said.

**Checks run (`python3 -I -B`, no `--json`):**
- `fidelity.py --relabel` (baseline page.json → current page.json): ALL PASS for F1 and for F2 on the baseline content.
- `contract_static.py --candidate`: ALL PASS (77) for both F2 pages.
- `anchors.py` and `completeness.py` on the F2 baseline-content page: ALL PASS.

```yaml
pass: "A3 confirmation of A10-A3-01..06 in F2 and of the lead's correction (read-only, no browser; page image unjudged)"
inputs: {f2_patch: 3f2c449364146401c292d05e72e101795dd2adf94e065ed4d902a12ce5462655, f1_page_fontless: 14388a284f97cbe6, f2_baseline_page_fontless: c56be5c40128c8dc, successor_page: 99ec6d759b2636fcb8cac58d6ae884ae99c879a932a54de5df3f3d92c3727333}
correction:
  verdict: confirmed
  evidence: >-
    F1 and F2 pages differ: head and script identical; body identical once the single '&nbsp;' after the date-line
    separator is undone; CSS differs only by the F2 rules (no orientation, summary or atlas elements on the baseline
    content to style) and the deleted (min-width: 1040.02px) rule. The producer copy's build script is a real file
    identical to the worktree's; the F2 build log says PASS. successor_checks.py imports the copy's status and audit
    modules directly.
  retracted: "verify6: 'F2 changes nothing for content without these fields (both 14388a28...)'"
  replaced_by: "On the baseline content, F2's markup differs from F1 only by the date-line binding; its CSS adds unused rules and keeps the bar's end fade at every width."
verdicts:
  - id: A10-A3-01
    verdict: verified-healed
    evidence: >-
      .pfs is held to the measure below 1180px and set in two columns on the wide frame from 1180px.
      Below 1180: one column of 570/561/547px at 1179/1024/768, about 74 characters per line (was 142/124/95).
      From 1180: two columns of 518.4px at 1180 and 575.8px at 1400.
      The left column still starts at the wide frame (x=92 at 1400), the same pattern as the glossary; accepted, not filed.
  - id: A10-A3-02
    verdict: verified-healed
    evidence: >-
      No mask-image: none rule remains; the end fade is set at every width. With 11 bar items the fade now marks the
      overflow at 1041-1146px and 1181-1267px. On the 9-item baseline bar the fade covers only the list's 24px end
      padding.
  - id: A10-A3-03
    verdict: verified-healed
    evidence: >-
      29 lines of the form p.statement-notes.statement-atlas > span.note-label > a, all reading "In the atlas"; every
      target exists. The search skips .statement-notes .note-label (status.js), and print hides .statement-atlas.
      No linked card also has its own notes line, so no card gets two stacked rules.
  - id: A10-A3-04
    verdict: verified-healed
    evidence: >-
      The separator is now followed by '&nbsp;' before its link, and the accessible text keeps a space. At 375 the
      successor line breaks before '· Contents'; line 1, 'Last updated 16 November 2026, 13:50 UTC', is about 290px of
      343px.
  - id: A10-A3-05
    verdict: verified-healed
    evidence: >-
      The relabel pairs are exactly the ruling's five. F1 and the F2 baseline-content page both pass in full. No old
      label string occurs in the research text of the remapped units (cell notes, family summaries, key
      explanations), so the mapping cannot hide a real change.
  - id: A10-A3-06
    verdict: "verified as recorded; not reproducible now"
    evidence: >-
      The re-run used content 89c382de..., atlas f02f29ec..., essay d10a1cf8..., and completeness exited 0. The
      composed folder was rewritten at 23:00:29 (content c5ce6212..., atlas d1f1d91d...). Completeness against it
      fails on one comparison statement (genuine-bulk-actions-question), whose new text adds ten words the page,
      built earlier, does not have: drift, not a renderer defect.
    residual: "Re-run the successor build and checks on root's sealed composed snapshot."
new_findings: []
convergence: "F1 and F2 verified on static evidence: no severity 1-3 finding remains in the two deltas; residual: successor checks on the sealed composed snapshot; page image unjudged."
```
