# Requests from the quality lane to root

## 1. Candidate patch manifests from the other lanes

This lane has not received any candidate from the foundation, interaction or atlas lanes, and it does not read
other lanes' unfrozen trees. To verify a candidate, supply a frozen manifest as set out in CONTRACT.json
(`candidate_delivery_to_quality`): candidate id, lane, `{path, before_sha256, after_sha256}` for every changed
file, the diff or the after-files, and the content and essay hashes used. Place it under
`quality/inbox/<candidate-id>/` in this worktree or give an absolute path to a frozen snapshot.

What this lane will run on each candidate, without a browser: the build and audit (`lead/` commands in
HEAL-REPORT.md), `lead/qh-static.mjs` (fidelity, anchors, public safety), `lead/qh-jsdom-checks.mjs`
(J1–J12 heal checks and R1–R9 regression guards; a candidate that changes the markup may need the selectors
in those checks mapped to its new markup, which this lane will do from the candidate's DOM contract), and
`lead/qh-audit-fixtures.py` if the audit changes. The checks key on CONTRACT.json; a candidate that changes
an anchor pattern, a data hook or the URL contract must say so in its manifest.

## 2. Browser verification that this lane cannot perform

Under root's restriction (RESTRICTION.md) the following remain open for root through an approved route, for
the baseline, for this lane's candidate and for any integrated candidate:

- Widths 1400, 1024, 768, 480 and 375 px in light and dark: no page-level horizontal overflow; overflowing
  formulas scroll and are keyboard-reachable; the new search opener in the bar fits beside the navigation.
- Visible focus on every control, including the new search opener and the card's close control; no focus
  hidden under the sticky bar; at 1024, 768, 480 and 375 px, a grid mark reached by Left, Home or Shift+Tab is
  not under the sticky row header (C16; the heal is source-verified only).
- Reduced motion; touch at 375 px (the card as a bottom sheet, its close control, a tap elsewhere; iOS Safari
  dismissal, C23).
- Print on A4 and Letter: every statement present. C01 was observed only through the prohibited route: on
  Letter, decisive question 16 and its related statement were missing from the PDF; other paginations lost
  example-row statements. A decisive check: print both papers and confirm that "A strict Lie source fails,
  while essential higher operations survive" and "A continuous Hamiltonian comparison preserving product and
  bracket" appear on the page after "QUESTION 15", for the baseline and for the candidate.
- Browser console free of errors.

## 3. Content-owner questions (content.json and essay.md are not edited here)

- C20: are these phrases mathematical qualifications or workflow residue? Essay: "retains the adopted local
  theorem above charge one". Statement `decisive-critical-existing-order`: "remains a saved constructor
  certificate", "uses a recorded exact kernel certificate", "the stored matrix arithmetic has not been
  independently replayed". The citation "(2016, author draft)" is a bibliographic status and is listed only for
  completeness. The external gate's process-language scan stays open until this is ruled.
- C18: 98 of 281 statements have no `id` (81 of 109 example statements, 6 of 9 principal results, 11 of 13
  open problems), so no link reaches them. Ids would make every statement linkable.
- C19: optional `id` fields on open-problem groups and glossary entries are now supported by the candidate;
  supplying them makes those anchors survive rewording.
- Formulas written outside TeX delimiters (audit warnings in candidate/audit/audit.txt): "W_F" (twice), "R_N"
  and "R_N=C[hbar]/(hbar^N), N≥1", "Y_f", "G0 union G_F", "q_B". They render as plain text with underscores.
- The glossary term "Universal regular \(W_3\)" is never attached because its form contains TeX (A1-A2-14).

## 4. Rulings needed from root or the atlas lane

- C21: DESIGN-CONTRACT.json cannot be checked mechanically as written: no public binding from an edge to its
  source edge, no relation vocabulary, no definition of a dependency-path step, no map from the page's statuses
  to the atlas status codes, `sourceLabel` not restricted to public references, and example values that the
  page audit would reject. CONTRACT.json lists the hooks this lane will test (Q24).
- C22: does the rule against theorem counts apply to the whole page (the cover tally and the status mixes show
  counts by status) or only to the atlas?
- A1-A2-15: which file owns status labels (content.json `status_key[].label` differs from page.json for 5 of 8
  statuses; the page uses page.json)?
