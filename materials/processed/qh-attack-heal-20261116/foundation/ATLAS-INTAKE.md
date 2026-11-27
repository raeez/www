# Atlas snapshot intake (frozen 11:20 layout snapshot): foundation findings for root

Snapshot: /tmp/programme-public-content-0835-20261116/layout-snapshot-1120/atlas.json, sha256
1b6ffa8ee2e0603b9440eb4c2f153e6b5d72f597038c95cbc67cdd41e80c519e, 886,650 bytes (verified). Read only, opaque; never
modified or copied into content/. Not final public source-fidelity approval.

Shape: programme-scientific-atlas-public/v1, asOf 2026-11-16T11:20:00Z; 9 domains (id, label, summary,
relatedQuestionIds), 503 claims (id, domainId, title, statement, status {code, label}, hypotheses, comparisonIds,
sourceLabel), 53 edges, 58 comparisons, 18 reading paths (all editorial_orientation).

## Mount at full scale (tests/atlas-real/real_mount_test.py, lane stub renderer)
- Build 7.7s, 0 TeX errors; section order status -> atlas -> results; nav item and contents entry present.
- Claim ids that coincide with page statement anchors (ctx.anchor_for): 22 of 503. The atlas needs its own claim anchors.
- Domain relatedQuestionIds: 2, both resolve to page question cards (#q-d-native-interface, #q-d-supported-bulk-actions).
- Claim status codes: checked 303, scoped_negative 94, remaining 58, conditional 48 (the atlas's own vocabulary).
- Defect found in the lane's own mount hardening: the reserved-class check also rejected classes that ctx.rich() emits
  (term, math-display, math-long). Repaired in the final batch (see LEDGER.yaml A0-L-06).

## Reader-visible atlas text that the page audit rejects (for root and the content owner; no text changed here)
The page audit (audit.py FORBIDDEN) runs on all visible text. Scanned 4209 reader-visible strings of the snapshot
(titles, statements, hypotheses, status labels, source labels, edge labels and scopes, comparison titles and overviews,
path titles, summaries, notes, stage labels and descriptions), with TeX-delimited formulae removed: 19 hits in
8 claims, all mathematical symbols written as plain text outside TeX delimiters. Rendered as they are, they fail
the build audit. Remedy belongs to the content owner (write them in TeX) or the audit owner (math-aware patterns).
Full list: tests/atlas-real/out/forbidden-hits.json.

- claim analytic-elliptic-earlier-supported-pair: hypothesis: v4 (version tag); hypothesis: v5 (version tag); hypothesis: v6 (version tag); statement: v4 (version tag); statement: v5 (version tag); statement: v6 (version tag)
- claim analytic-gaussian-target-topology: hypothesis: C0 (internal identifier)
- claim centre-fixed-bound-state-witness: hypothesis: N12 (internal identifier)
- claim elliptic-exact-generating-matrix: hypothesis: E1 (possible internal identifier (or E_n written without subscript)); statement: E1 (possible internal identifier (or E_n written without subscript))
- claim gravity-ordinary-reduced-inverse: hypothesis: C1 (internal identifier)
- claim mixed-stronger-physical-comparison: hypothesis: C1 (internal identifier)
- claim nonrational-fixed-moment-exchange: statement: R1 (internal identifier)
- path analytic-reading-elliptic: stage.description: v4 (version tag); stage.description: v5 (version tag); stage.description: v6 (version tag)
