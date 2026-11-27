# Foundation monograph v2: scoped successor to installed v1 (sealed 16 Nov 2026, 20:03 UTC = 17 Nov, 03:03 WIB)

v1 is unchanged and stays frozen (`../FREEZE.json`, patch 19118f08…), as root installed it. This is a delta on top of it.
All hashes are in `GUARD.json` in this folder.

## Delta

**`patch/monograph-v1-to-v2.patch`, sha256 `2b60caf7536a49e4924effed69512283b0d21b1b35f85e7ba56f85f128958a6b`.**
Apply it with `patch -p1` at the integration root, on installed v1.

It changes three files; status.py is unchanged (198727b3…):

| File | v1 (installed) | v2 |
|---|---|---|
| `compiler/quantum-holography-status/monograph.py` | cf6abfa6… | c0af80b6… |
| `compiler/quantum-holography-status/monograph.css` | 7d58f2b9… | 86aa0724… |
| `content/quantum-holography-status/page.json` | ac44a925… | 2cbfcfb6… (interface words only) |

Both apply paths were checked:
- the delta on integration's current (v1) files reproduces v2 byte for byte;
- the original pins, then v1, then the delta, give the same result.

Still inert: with no `reader-data/`, the page is byte-identical to today's (cf89f01b…).

## Repairs, each checked on the built candidate

| Observed | Repair | Checked |
|---|---|---|
| Construction edges were dashed like open comparisons. | A construction is a solid double line: a rail drawn over a wider stroke, with a solid head and its label on the drawing. Only open comparisons are dashed, in the open colour with a hollow head; reading relations stay dotted grey. The legend sample is a double rule. The chapter locator's "later chapters" arcs are now dotted too, so dashes stay reserved for open comparisons. | No dash rule on constructions. The 4 construction strokes in fig-state-line-cap (2 edges × 2 orientations) each carry their rail. |
| Diagrams carried `data-chapter` and `data-section`, reader.js's selectors. | They now carry `data-figure-chapter` and `data-figure-section`, as the atlas figures do. The book map's chapter links no longer carry `data-part`. The author's `context_key` is no longer served: it held a version tag, which failed the page audit. | Exactly 18 `[data-chapter]` elements (the articles), and the 127 `[data-section]` elements are all chapter sections. No figure carries either. |
| **O1** The reading map was an untraceable hairball, showing numbers only. | The map is rebuilt as one labelled figure: a column per part, a box per chapter with its number and full title, and a line for each **direct** prerequisite only. That is 22 lines, the transitive reduction of the manifest's 59 pairs, so reachability is unchanged. Lines run down a column or through the gutters, and a line that skips a part runs along the foot, so **no line crosses a box**. One chapter under the pointer or focus lights its own lines and the chapters at their ends; the rest go quiet. A route name lights its chapters. The caption says lines are direct reading prerequisites, not mathematical implication, and that each chapter's own list names all of them. Below about 860 px the figure gives way to the contents, which lists the same with "Draws on". The chapter locator now draws only its own chapter's arcs. | 18 boxes and 22 lines; every line is an authored prerequisite. A geometric check finds 0 lines crossing a box they do not join. |
| **O2** "Reconstructi/on" broke with no hyphen. | Part titles now sit in columns about 16% of the figure's width (at least about 140 px wherever the figure shows), with no mid-word breaks (`overflow-wrap: normal`). | "Reconstruction and open problems" sits in its own column. |
| **O3** "Chapter 1 · 1Boundar…" | The chapter number is outside the `h2`: `p.mg-ch-no[aria-hidden]` before `h2#chNN-h`, so reader.js reads the title alone. Every number and title pair now has a real space between them (sections, contents, lists, cards). The bar's previous/next links may run to 26 rem. | `h2#ch01-h` reads "Boundary observables and reconstruction". The first section head reads "1.1 Reduction must retain the measurements". |
| **O4** The opening went from title to navigation without saying what the programme is. | `manifest.introduction` (the author's Markdown, set verbatim) follows the title block and comes before the map, the routes and the marks. Its first paragraph is the lead. | The introduction precedes the map. |
| Terms and theorems records were unused. | **`section#glossary[data-reference]`**: 63 verbatim definitions, in alphabetical order, each a `[data-term]` block with the term's id, marked "Defined in Chapter n, n.k Title" and linked to its `definition_ref` section. **`section#results-index[data-reference]`**: 39 results by chapter, each with its mark and status, its title linked to `rendered_anchor`, a context link to `context_ref`, and the full `statement_excerpt` (its repeated title removed). Both are set as copies, so no second result block, anchor or equation id is made. Both are listed first in the contents' reference group. The old `#terms` is unchanged. | 63 entries, all with `data-term`, and 62 ids (one held back, below). 39 index entries, all linked. The page still has exactly 39 `[data-result]` blocks, the chapter originals. |
| `figure_words` not used. | `FigureContext.words` = `manifest.figure_words`, which `figures.render` reads. | The five models render. |
| `term-cap` collides with the former page's `#term-cap`. | Neither id is renamed. The old anchor keeps its id, and the new entry shows without an id (keeping `data-term-id="term-cap"`), with a build warning. | Reported to the author in `CONTENT-ISSUES.json`: a distinct id is needed. |

## Evidence on candidate `out/book.html`

The candidate is sha256 90d7d422…, 14,679,227 bytes, audit **PASS**. It was built from snapshot
`snapshot/20261116T195917Z` (manifest 342bef12…, diagram-records 76f1a771…).

Other inputs:
- reader.js 698ca226…, the interaction lane's current file;
- the five installed atlas models, 2b86921f…, 0c68828b… and bce4e549….

The checks:
- **Prose** (`evidence/PROSE-RETENTION.json`): across 18 chapters, all 46,224 prose words reach the page, with 0 lost.
  Displays and authored `\tag` numbers equal the source.
- **Diagrams** (`evidence/DIAGRAMS.json`): all 13 records are rendered and placed, with 0 problems, 0 TeX errors and
  0 missing definition targets.
- **Ids and links:** none of the ids repeats, and every internal link resolves.
- **Gallery:** `out/diagram-gallery.html` draws all 13 diagram records for QA.

## Interface for atlas C5 (confirmed)

`AtlasContext.mark(status, label=None)` already exists in status.py. It returns the page's own `mark(status, label)`
SVG for any status in `MARKS`, and `''` otherwise:
- the SVG is `<svg class="mark mark-<status, spaces as hyphens>" viewBox="0 0 16 16" width="16" height="16">`;
- with a label it gets `role="img"`, an `aria-label` and a `<title>`; without one it is `aria-hidden`;
- the statuses are checked, pending, partial, conditional, conjecture, heuristic, open, published, not posed and
  refuted form;
- colours come from status.css `.mark-*` and the `--st-*` tokens, in both themes.

The book's result blocks and diagram statuses use the same function, so atlas marks drawn through `ctx.mark` will be
identical.

## Weight, for the interaction lane's memory finding (`evidence/WEIGHT.json`)

The candidate is 14.7 MB:

| Part | Size | Tags | Formulas |
|---|---|---|---|
| Fonts | 0.42 MB | | |
| Sheets | 0.19 MB | | |
| Scripts | 0.16 MB | | |
| Front matter and contents | 0.05 MB | | |
| 18 chapters | 2.22 MB | about 133k | 3,551 |
| Glossary | 0.40 MB | about 26k | 718 |
| Index of results | 0.06 MB | | |
| **Former page (reference volume)** | **about 11.2 MB** | | |
| of which the atlas | **8.90 MB** | **about 380k** | |
| of which examples | 1.03 MB | | |
| of which decisive questions | 0.54 MB | | |

The book is about 2.7 MB, and the former page's sections are 76% of the bytes. Serving those sections as a separate,
lazily loaded volume would be the largest single cut. My DOM needs no change for it: every reference place is a
`[data-reference]` section, the old ids are unchanged, and the contents links them by id. This is data for the
interaction lane's decision, not a competing design.

## Still open

- The page image of v2 is not judged by me (browser restriction). Native QA, now working from root's screenshots,
  should re-observe O1–O4 on this candidate or on root's build of it.
- The author owns: a distinct id for `term-cap`; the 4 remaining working-file links (`CONTENT-ISSUES.json`); and the
  final markup freeze.
- The interaction lane owns the memory and lazy-volume decision, and its reader.js handoff to integration.
