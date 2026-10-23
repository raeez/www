# LICC blueprint editorial handoff - 22 October 2026

## Scope and custody
- Worktree: /Users/raeez/centcom-worktrees/writing-20261022-www-blueprint
- Branch: editorial/www-blueprint-20261022
- Baseline/HEAD/origin-develop pin: a0d011c46811837a7f5fb1d1aa60cd457b68dd00
- Sole staged file: licc-blueprint.html. No commit, push, deployment, publication, index, or feed changes.
- Source SHA-256: 4266159b38d83744c85bc6e169981d2893a5b0f11207ed6b7f80e1919bd87964
- Candidate SHA-256: a6afce65667f6330b0d1bb149ed0f5382f29832007ffcaea9847385e0fab96d2
- Staged diff stat: 1 file changed, 2 insertions(+), 2 deletions(-). The imported article body occupies one long source line.

## Complete-work coverage
Read the entire original (700 nonempty blocks), recorded quoted defects and argument/question sequence before edits, then extended the whole-work dependency/recurrence map under the principal's composition refinement. Read the entire final candidate (705 nonempty blocks) in order. Reviewed every changed source claim and all section transitions. Independent semantic preservation review passed against the final hash after correcting identified shifts.

73 original blocks changed, 5 argument/transition paragraphs added. Every other original block survives verbatim, allowing two substantive section moves and heading renumbering. The final old/new map is blueprint-edits.json; blueprint-prose.diff is the readable complete body diff. All definitions, named examples, quotations, research objects, dates, financial figures, proposed roles, qualifications and contact values remain. Superlatives and promotional descriptions were reduced as authorized.

The recommendation now appears in the summary. Institutional complementarity precedes structural choice (old 2.3 becomes 1.5; risks become 2.3). The roadmap precedes its contact directory (3.1/3.2). Recurrences now point to specific initial programs, governance, partner models and funding requirements. Each later return adds methods, conditions, named roles, or implementation detail. No numerical reconciliation or new commitment was inferred.

## Checks
- git diff --check: PASS.
- Strict HTML start/end nesting: PASS.
- 11 href values preserved exactly; both local writing.html links resolve. No original IDs existed; none removed.
- Styles, scripts and SVG payloads: byte-identical.
- All 23 tables and their row/cell structure retained. 591 td cells retained.
- All double-quoted source strings: identical multiset.
- All monetary strings: identical multiset.
- Numeric-token differences accounted for completely: removed Version 1.0 twice and old heading 2.4; added heading 1.5, repeated Years 1-3, and references to Sections 2.3 and 6.1. No source numeric value deleted or altered.
- Number-bearing table cells reviewed individually; only surrounding prose changed, plus the added 6.1 reference.
- Required private-repository/path scan: zero hits.
- Required external process/version/hedging scan: zero hits after removing both visible Version 1.0 markers. December 2025 and CONFIDENTIAL remain.
- Rendered browser QA: NOT RUN in this lane. Owner reported CUA local-file rejection and instructed no workaround or alternate transport. No rendered inspection claimed.
- No new tests required for prose; no build or deploy run.

## Inherited issues, preserved
The named source is the December 2025 LICC Founding Blueprint at the pinned baseline. Its claims remain unverified by this editorial pass.
- Summary five-year budget $47.5M differs from detailed cumulative $43.7M; summary launch capital $5.5M differs from detailed $4.485M.
- Calculated personnel totals for Years 1-5 are $1.610M/$2.700M/$3.875M/$5.130M/$6.300M, versus stated $1.71M/$2.88M/$4.20M/$5.62M/$6.90M.
- $175M divided by $2.1B is 8.33%, rather than the stated approximately 20%; no alternative denominator is supplied.
- Year-5 summary 12 faculty FTE differs from five senior faculty plus founding director in the detailed staffing assumptions.
- Summary/full-operation launch 18-24 months, hybrid formation months 12-24, and detailed formation/launch months 28-36 are unreconciled. Phase 2 refers to different activities across sections. Launch-capital timing uses another undefined origin.
- The 27 free zones are described with inconsistent UAE/Dubai scope.
- Overhead/operating-contingency calculation bases and launch/operating working-capital overlap are unspecified.
- CONFIDENTIAL marking, institutional titles, proposed partnerships, contact strategies, university naming rights and budget targets remain source assertions or proposals, not evidence of current approval or commitment.
- Static inherited HTML risks: no th/thead/caption table semantics; imported cNN classes lack matching CSS; several contact strings concatenate separate values; wide tables lack overflow containment. These were not introduced and require owner review if visual repair enters scope.

## Downstream obligations
The owner must integrate the staged patch semantically and refresh feed.xml, which contains a complete article copy. Writing title, slug and canonical URL are unchanged.

The exact baseline body also exists at /Users/raeez/raeez-site/licc-blueprint.html (equality checked). Give that owner duplicate-body.patch plus blueprint-prose.diff; preserve its surrounding site wrapper and review its metadata independently. The www patch additionally removes Version 1.0 from article-meta while retaining date/classification.

compiler/docs.config.js:55 points to the upstream Google Doc for licc-blueprint, and compiler/build.js writes compiler/dist. A later compiler rebuild/copied output can restore old prose and version metadata. Upstream Google Doc, compiler config, and feed are outside this lane's sole-file authority. No external source was mutated.

Patches: www-blueprint.patch (staged complete file diff); duplicate-body.patch (body-only diff). The initial helper script is retained only as working evidence; use the final map/diff and staged candidate for integration.
