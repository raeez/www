# Reader foundations handoff — 22 October 2026

Worktree: /Users/raeez/centcom-worktrees/writing-20261022-www-readers-foundations
Branch: editorial/www-readers-foundations-20261022
HEAD and pinned origin/develop: a0d011c46811837a7f5fb1d1aa60cd457b68dd00

## Deliverables

- `.editorial/editorial.diff`: compact raw-to-maintained unified diff, labels `a/content/reader-papers/...` and `b/content/reader-papers/...`; apply this to integration copies after semantic review.
- `.editorial/staged.patch`: six new-file additions, binary-capable git patch.
- `.editorial/diagnosis.md`: initial full-work quoted diagnosis and argument sequence.
- `.editorial/composition-map.md`: full thesis, question, dependency, recurrence and section-join review.
- `.editorial/checks.json`: raw and maintained SHA-256 values, exact preservation inventories and source checks.

## Exact staged ownership

- `content/reader-papers/institutional-computation-explained.md`
- `content/reader-papers/institutional-computation-explained.tex`
- `content/reader-papers/recognition-across-independent-authorities.md`
- `content/reader-papers/recognition-across-independent-authorities.tex`
- `content/reader-papers/rules-evidence-and-local-decisions.md`
- `content/reader-papers/rules-evidence-and-local-decisions.tex`

Staged stat: 6 files, 1,355 insertions (new maintained sources). No raw edits. No other staged files.

## Coverage

All three works received complete initial MD/TeX reads, diagnosis, paired edits, whole-work composition review, complete revised MD reread, and changed-claim comparison. All section joins and mapped recurring themes were reviewed. Independent full-work review covered every revised MD, every changed claim against the raw source, and full MD/TeX parity. Its scheduling precision and paragraph-length findings were repaired and checked in both formats.

Main composition change: Rules now establishes local decisions after joint witnesses and before cost optimization. This preserves its complete material and makes the feasibility dependencies explicit. The renamed grades/applicability heading retains `#a-grade-is-not-an-applicability-record`. Institutional Computation and Recognition retain their dependency order with stronger joins. Repeated themes now introduce a new act, evidence boundary, execution condition, or model limit.

## Verification

- `python3 .editorial/check_sources.py`: PASS for all six raw hashes against pinned git blobs; exact math, citation, numerical, bibliography and identifier inventories; complete normalized MD/TeX body and section-order parity; public-source/process scans; local citation anchors.
- Focused sentence/paragraph screening: zero descriptive body sentences above 25 words or paragraphs above six sentences after citations/math are removed. This screening is not a certification against the complete STE dictionary.
- `git diff --cached --check`: PASS.
- Staging inspected: exactly the six owned maintained source files.

## Residual responsibilities

Parent lane owns source provenance/hashes, HTML generation, compiler/index integration, and visual inspection. No generated artifact build, rendered inspection or publication is claimed in this lane. The parent will apply the newly arrived compiled P06 SJN result renumbering at integration; these files preserve the assigned baseline citation payloads. No summary change is required for the editorial revision itself.

## Patch fingerprints

- `editorial.diff` SHA-256 `fed5fd4fc01bf31ead679320669290bbe7c84ef3801fa56d307e319f23bba165`
- `staged.patch` SHA-256 `574de4788a107aeff7ff799a2248a2b7b2e27925bdbc29c0142534ce4af81d98`
