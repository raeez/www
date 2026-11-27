# Foundation monograph v5: map titles, search field, bar and route ranges (root's and QA's native findings)

v1 to v4 are unchanged and stay frozen. All hashes are in `GUARD.json` here. This is a bounded repair, in my files only.

## Delta

**`patch/monograph-v4-to-v5.patch`, sha256 `f5ec90088ddc00e465cfa6f8dc6f15ed751cf3b106cbdb478106650a078f09a6`.**
Apply it with `patch -p1` at the integration root, on installed v4.

It touches only `monograph.py` (9a7c44f3… becomes 5f8ec6d7…) and `monograph.css` (d7b2a217… becomes 4193ccfa…).
status.py and page.json, including root's metadata, are not touched.

Checked:
- on integration's actual v4 files, and on the sealed v4 state, the delta reproduces v5 byte for byte;
- with no `reader-data/`, the page is still byte-identical to today's (cf89f01b…).

## Repairs, from the images (each inspected here)

| Finding | Image | Repair | Checked on the candidate |
|---|---|---|---|
| Map boxes cut chapter titles (chapters 5, 8, 12, 17; also 2, 9, 10, 11, 13, 16). | `map-release-v4-light-1e097e73.jpg`, QA IMAGE-04 | Each box takes its own height from its title. The title is wrapped at words, without hyphenation, as it falls at the narrowest width the map is shown (52 body sizes, about 15 characters of the box's type a line); each row takes its tallest box. The height is a `min-height`, with no clipping, so a title is never cut, and it sits centred in its box. Arrows attach at each box's own middle. The map takes the page's width (up to 76 rem), while the title page's text stays in its frame. Below 52 body sizes the map gives way to the contents. | 18 boxes, 2.7, 3.7 or 4.7 em by their titles: chapters 5, 8, 17, 2, 9 and 13 have 4 lines, chapter 12 has 3. All 22 arrowheads lie on their target box's edge, within its height. 0 lines cross a box they do not join. |
| Mobile search: the query field collapsed to a tiny "×" box between the heading and Close. | `search-release-v4-375-light-93bf1425.jpg`, QA S1 | The field row wraps. At 640 px or less the label takes its own line, and the input fills the next line beside Close. Above that, the input keeps at least 10 rem. | Rules present. Search behaviour, focus order and companion search are unchanged (CSS only). |
| The Begin link's title was cut despite free bar space. | QA IMAGE-03, O3 | On the title page, the Begin link may run to 42 rem, and its title is no longer hidden up to 1480 px. In chapters, the neighbouring titles still give way to the reader's place. | Rules present. |
| Routes were long comma lists. | QA IMAGE-03, R1 | Runs of three or more consecutive chapters are written as ranges. Every member is shown, and no other. | "Algebra and geometry, Chapters 1–8, 12, 13, 15"; "Field theory, Chapters 1–12, 14, 17"; "Arithmetic, Chapters 1–8, 12, 13, 15, 16". |
| The narrow bar showed "· Chapter 1 of 18 Bou…". | QA IMAGE-05, C1 | At 860 px or less, no separator is drawn before the hidden part name. At 640 px or less, the chapter title, which could only show a fragment there, is not drawn: the bar reads "Chapter 1 of 18". | Rules present. |
| The chapter numeral read as a Roman "I". | QA IMAGE-05, C2 | Chapter numbers (the opener, the contents, the next-chapter card, the results index) use EB Garamond's lining figures: its oldstyle 1 is a small-capital I. Parts keep their Roman numerals. | Rules present. |
| "Chapter 1 of 18" appeared twice at narrow width. | QA IMAGE-05, C3 | At 640 px or less, with the reader running, the chapter head's own "Chapter n of 18" is not drawn; the bar shows it. | Rules present. |

## Evidence on candidate `out/book.html`

The candidate is sha256 aa33ebd9…, 14,693,229 bytes, audit **PASS**. It was built from snapshot
`snapshot/20261116T204404Z` (manifest 342bef12…) and integration's installed lane files (reader.js 9ed283cc…,
status.js 70c0663a…, the C5 atlas, the five models).
- **Prose:** 46,224 words, 0 lost.
- **Formulas:** 3,323 of 3,323.
- **Diagrams:** 13 of 13 rendered and placed, with 0 problems.
- **Working-file links outside mathematics:** 0.

## Not mine, for root to route

- **Interaction:**
  - S2, the same section returned three times in search, with inconsistent notation;
  - S3, sixteen facet chips before the results;
  - G1 to G3, the figure readouts and labels.
- **Root (naming):** S4. The old programme title appears as a facet name because it is the heading of the reference
  overview, the former page's cover. Renaming it would change the former page's text, which I have left unchanged.

## Not judged here

I have no image of v5. The map should be recaptured in both themes at the image widths used before, and the search and
bar at 375 CSS px.
