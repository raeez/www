# Data-level QA of the frozen atlas layout input (11:20 cutoff)

> Status, after the principal's steering received through root on 16 November 2026 ("tracker content should import
> [the full synthesis] and sundry"): the 11:20 atlas and the current content are only a preserved review and layout
> baseline. The content owner is composing the public successor from the complete reviewed programme synthesis. The
> findings below concern that baseline; they are not verdicts on the final tracker. They become checks to rerun on
> the final payload (HANDOFF.md, "Exact remaining integration checks").

Input, read only and unchanged: the atlas root supplied for layout and interaction integration, sha256
1b6ffa8ee2e0603b9440eb4c2f153e6b5d72f597038c95cbc67cdd41e80c519e, 886,650 bytes (verified), schema keys domains,
claims, edges, comparisons, readingPaths; 9 domains, 503 claims (303 checked, 48 conditional, 94 scoped negative,
58 remaining), 53 edges, 58 comparisons, 18 reading paths. Root's note: not final public source-fidelity approval;
scientific text and the 11:20 cutoff are preserved. This lane edits nothing in it.

Checker: `lead/qh-atlas-fidelity.py` (tested on a faithful fixture, all pass, and a faulty fixture, every check
fails as intended). Result: `lead/results/atlas-fidelity-1120.json`. No rendered atlas exists yet, so the rendering
checks AT8, AT8b and AT8c wait for root's integrated candidate.

## Passing

- AT1 ids unique and reader-safe; AT2 status codes and path kinds within the contract's vocabularies, required
  fields present; AT3 every domain, claim and comparison reference resolves; AT4 comparison lists and claims'
  comparisonIds agree both ways, and every listed claim's status code matches its list; AT5 no duplicate edge.

## Findings for root

### AQ01 Mathematics is written in three notations, and 19 strings would be refused by the page audit (severity 2; owner content owner, decision root)
- Of 4,072 reader strings, 209 use TeX delimiters, 668 carry ASCII mathematics (x_y, ^, hbar, theta, partial) and
  345 carry Unicode symbols (≥, ′, ², −, ∘, ⊗, →, ∈). Examples: "D=d_t+bar-partial_z", "E1=theta′/theta",
  "order-hbar² obstruction −[H_total,R1]".
- Rendered as written, 894 strings raise the audit warning for formulas outside TeX, and 19 strings fail the build
  under rules the baseline audit already has: internal-identifier "C1", "C0", "N12", "R1"; "E1"; version-tag "v4",
  "v5", "v6" (claim 420, "the ordered word a1 a2 u3 v4 v5 v6", and the reading path that repeats it).
- On a page whose formulas are otherwise set as mathematics, ASCII and Unicode notation reads as code beside
  typeset formulas; the principal's scope asks for the opposite.
- Decision needed: either the content owner sets the atlas mathematics in TeX before the atlas is rendered, or root
  defines a separate text format for the atlas with its own audit rules. This lane does not rewrite the text.

### AQ02 The schema id carries a version token (severity 3; owner atlas lane)
- `schema: programme-scientific-atlas-public/v1`. If the data block is embedded with this value, the candidate
  audit's data-block scan fails the build on "v1". Drop or rename the field when embedding.

### AQ03 Relations have no vocabulary and labels name edges, not relations (severity 3, contract ambiguity; owner atlas lane and root)
- 31 distinct relation values over 53 edges, mixing codes ("uses", "discharges_condition") and phrases ("checked
  application", "applies under the actual-map hypotheses"). Two relations carry two different labels each
  ("supplies_accepted_interface", "explicit_source_input"), so the label works as an edge title.
  DESIGN-CONTRACT.json describes label as "Human relation label". The legend and the text equivalent need one
  reading of these fields; the check AT5b reports the two relations.

### AQ04 Source labels cite theorem numbers without naming a document (severity 3, undecided; owner content owner, source review)
- 380 claims carry a sourceLabel such as "Theorems 6.1 and 7.1, Lemma 8.1 and Section 9". A reader cannot tell which
  document these numbers belong to, or whether it is public. Root has said source-fidelity review follows
  separately; for the page, a label must either name a public source or not be shown.

### AQ05 All reading paths are editorial (information)
- All 18 paths have kind editorial_orientation; none is a dependency path, so AT6 has nothing to check. Rendered,
  each must say in visible text that it is an editorial reading order (AT8c).

## The hardened page audit on the baseline atlas text (cycle 3b)

Every reader string of the baseline atlas (4,129 values; ids, references, codes and kinds excluded) was placed in a
paragraph and audited by the baseline, cycle-3 and cycle-3b audits (`lead/results/atlas-audit-rules-1120.json`). The
cycle-3b rules (hashes, repository addresses, private paths, Unicode normalisation, stage labels, formula text) add no
failure kind: 11 strings fail under all three for the reasons in AQ01 (C1, C0, N12, R1, E1; v4, v5, v6), and 209 more
fail under the cycle-3 and cycle-3b audits only because this probe does not render TeX (a build sets it as
mathematics). 470 strings raise the warning for formulas outside TeX (AQ01).
