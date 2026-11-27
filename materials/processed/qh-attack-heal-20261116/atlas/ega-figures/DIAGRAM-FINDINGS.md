# Diagram-contract findings for root and foundation (no implementation here)

These are from the atlas lane, 17 November 2026, about 02:45 WIB. They are findings only: foundation owns the static diagram renderer, and the atlas lane builds none.

**Read (read only):**
- foundation's staged `monograph.py` (e4bc1043…) and `monograph.css` (7698ae8d…), in materials/processed/qh-attack-heal-20261116/foundation/monograph/src/compiler/quantum-holography-status/;
- PROGRAMME-DIAGRAM-CONTRACT.md c678539d…;
- diagram-records.json c96f67df….

## 1. Construction edges use the dash that marks open comparisons

**Where.** `monograph.css:360` gives construction edges `stroke-dasharray: 9 4`, and `:344` gives them a dashed key sample. Open comparisons are also dashed: 6 5, in `--st-open`, with a hollow head.

**Why it matters.** fig-state-line-cap has two constructions (status Theorem) and two open comparisons (status Open problem) in one drawing. They then differ only by dash length, colour and head.
- The contract says: "No colour alone carries the distinction".
- SCIENTIFIC-VISUAL-CONTRACT says: "An open comparison is drawn distinctly".
- A proved construction drawn in the open problem's line language reads as unproved.

**Proposal.** Keep dashes for open comparisons only. Give constructions a line language of their own, such as a solid double line or a wavy line with an open head. Keep their literal label, which they already carry, and the record's status.

## 2. Imperative prohibitions would be printed to readers under "Not asserted"

**Where.** `monograph.py:1373` prints every `prohibitions` item verbatim under the heading "Not asserted". Five of the seven items are instructions addressed to whoever draws the figure, not mathematical statements:

- fig-character-action-comparison
  - "Do not mark either arrow as a universal equivalence."
  - "Do not identify these spaces with the ordinary exterior-source mapping space."
- fig-weil-trace-remainder
  - "Do not display the remainder as zero."
  - "Do not identify a complex-bilinear residue dual with a positive Hilbert pairing."
- fig-state-line-cap
  - "Do not merge the two source domains or finite cutoff families."

The other two items in fig-state-line-cap are statements and read correctly:
- "No map from the normalized state to the vacuum line is asserted."
- "The local based line does not assert …"

**Proposal.** The contract asks for such a limit to be returned to the author: "If a field cannot be rendered, return that limitation to the author". Root asks the author for reader wording of the five imperative items, or for a flag on which items are drawing constraints only. Until then, foundation honours them in the drawing and prints only the declarative items.

## 3. Note: addressing a node

The contract says: "A DOM node ID must be namespaced by the figure ID". Foundation's nodes carry `data-node` and no id, inside an `aria-hidden` plot. That is compatible, because no id can collide.

If a later link from the text should land on a node in a figure (A03), the form would be `id="<figure-id>--<node-id>"`. Without such an id, a link from the text cannot land on a particular node.
