# Foundation monograph v6: the map's attachment (root's unit finding; QA IMAGE-04 M1, M3, M4)

v1 to v5 are unchanged and stay frozen. All hashes are in `GUARD.json` here. This continues the same map repair; it
opens no new review.

## Delta

**`patch/monograph-v5-to-v6.patch`, sha256 `89670f7c55324badd440778ee166ced8ae3b19b9dda3ece9cb8ebde00f0644ea`.**
Apply it with `patch -p1` at the integration root, on installed v5. Integration was checked to hold exactly v5
(monograph.py 5f8ec6d7…, monograph.css 4193ccfa…).

It touches only `monograph.py` (5f8ec6d7… becomes 605723ba…) and `monograph.css` (4193ccfa… becomes fc180108…).

Checked:
- on integration's actual files, and on the sealed v5 state, the delta reproduces v6 byte for byte;
- with no `reader-data/`, the page is still byte-identical to today's (cf89f01b…).

## Cause, confirmed

Root's reading is right. In CSS, `em` in any property other than `font-size` resolves against the element's own
computed font size.
- In v2 to v5, each map box set `font-size: var(--text-sm)` (0.833 of the body size), so its inline `top` and
  `min-height` in em came out at 0.833 of the intended values.
- The plot's height, the SVG lines and the arrowheads use the body size.
- So every box sat higher than its lines, by an amount that grew down the figure. Line starts, line ends and
  arrowheads were detached (M1, and the "ticks without arrowheads" of M4, whose heads fell behind the boxes above).

My earlier geometric check worked in the renderer's own coordinates, so it could not see this.

## Repairs

| Finding | Repair | Checked on the candidate, in CSS's own units |
|---|---|---|
| Boxes on a different scale from their lines (root; M1) | The box keeps the body size, so its `top` and `min-height` are in the plot's units. Only its number and title are set at the smaller size. Its padding is restated at the body size, and the height estimate counts it. | The box rule and the arrowhead rule declare no `font-size`; the plot inherits the body size. **All 22 lines start on an edge of their source box and end on an edge of their target, within its height. All 22 arrowheads sit on their target's edge.** |
| Two links looped under the whole figure, 7 → 13 and 7 → 17 (M1) | A link that skips a part now leaves its source's right side like every other link. It runs along its gutter to the gap between rows beside the target's row, crosses the columns between them inside that gap (rows are shared by all columns, so no box stands there), and enters its target from the target's gutter. The two edges themselves are unchanged. | No line runs below the last row: the lowest line is at 24.5 body sizes, the lowest box bottom at 26.4. 0 lines cross a box they do not join. |
| Part I's three-line title climbed into the figure heading (M3) | The part headers are a grid on the map's own column fractions. The row is as tall as the tallest title, and the headers' rules are aligned at its foot. The figure heading has a full line of space below it. | The grid uses the same fractions as the boxes (0.06, then 1 and 0.26 alternating, then 0.06). |
| Arrowheads were small and light, and looked different on the two kinds of link (M4) | One arrowhead for every link, 8 px, in the lines' own ink, which is darker than before. | One rule for both directions. |

Unchanged: the 22 edges (the transitive reduction of the manifest's prerequisites), their direction, the caption, the
full titles (v5's wrapping and minimum heights), and the threshold below which the contents stands in for the map.

## Evidence on candidate `out/book.html`

The candidate is sha256 c254c630…, audit **PASS**. It uses the same snapshot and inputs as v5, so the two differ only
by this repair.
- **Prose:** 46,224 words, 0 lost.
- **Formulas:** 3,323 of 3,323.

## Not judged here

I have no image of v6. The map should be recaptured in both themes; it is the figure QA flagged.
