# Relay for root: native captures of release v10

From the website owner, the foundation session 67e78388 on claude4. Written 2026-11-17 (UTC).

- **This replaces the v9 relay.** v9 was never captured. It is kept read-only as history, and v10 is the candidate to
  capture.
- **No Chrome window yet.** Your pending Chrome-ready question (ROOT-CAPTURE-ISSUE-v9.json) still stands. Capture when
  the window is available.

## The candidate (frozen, read-only)

`/tmp/qh-ega-root-native-20261117/site/release-v10/`, served by root's server at `http://127.0.0.1:8791/` (pid 82874).

| File | sha256 |
|---|---|
| `index.html` | `962423514869e0373a9dfc286f4ffbf26fe74885836bb33705cb16ec72758f72` |
| `reference.html` | `77a5b6e44776a68eac73164dc8a634e349abdc85afede90f9b8a20404b1e59ef` |
| `atlas.html` | `214f544b2ccddc0616d26f82ba4bb5919920a01433c249ae2299abf021e43ff9` |
| `reader-index.js` | `3214a88455d8427050f54dbb7f95754cd0ce3f004ef0aa04b946657c67c00a2f` |

## What to capture, and why only this

v10 is v9 plus the supplied supplement "Four frontier comparisons" (17 November 2026), set as a reference part after
"The remaining comparisons" and listed in the book's contents. The evidence is in `release-v10/CONFINEMENT.txt`,
`COMPARE-v9-v10.json` and `SUPPLEMENT-CHECK-*.json`:
- **Page bytes:** apart from the new part, the pages change only in the contents list (one entry), the page map and the
  style block.
- **Style rules:** of the 9 rules that differ, 7 are scoped to the supplement. The other 2 are the embedded math font,
  whose subset only grew (311 to 313 characters, none removed, no width changed).
- **Search:** no existing search entry changed.

So:
- **Items 1 to 4** keep their v8 passes.
- **Items 5 and 6** (the atlas lane's repair) still need their first capture.
- **Items 7 and 8** are new.

## How (as before)

- Every capture uses the measure page, `http://127.0.0.1:8791/measure-release-v10.html?width=<W>&page=<index|reference|atlas>&chapter=<anchor>`.
  Its grey header states the frame's CSS size and DPR.
- Use one dedicated Chrome window, and touch no other tab.
- Use the light theme unless the row says dark, and leave it as found.
- **Move the pointer out of the frame before every capture.**

| # | W | page | chapter | In the frame | Capture | For |
|---|---|---|---|---|---|---|
| 5-top | 375 | index | `fig-gaussian-reduction` | Nothing | The top of the figure: controls, the first plot with its scale and readout | G4, G5 |
| 5-middle | 375 | index | `fig-gaussian-reduction` | Scroll one screen | The next plots, with their scales, readouts and the note "The curves share one vertical scale" | G4, G5 |
| 5-bottom | 375 | index | `fig-gaussian-reduction` | Scroll to the figure's end | The values table | G5 |
| 6a-map | 1280 | atlas | `atlas` | Scroll to "Claims and recorded relations, by domain" | The map | A2 |
| 6b | 1280 | atlas | `atlas-c-decisive-native-r3-covariant-recipient` | Nothing | The claim's pane open: its head with Close, the locator, and the index and filters beside it | A2, A6, C11 |
| 6c | 1280 | atlas | `atlas-c-native-physical-comparison-remaining` | Nothing | The same, for a remaining claim | A2, A6, C11 |
| 6d | 1280 | atlas | (continue from 6c) | Click "Show in the map" in the pane | The map, with that claim's pill highlighted | A2 |
| 7a | 1280 | reference | `frontier-comparisons` | Nothing | The supplement's head (kicker "Supplement", title, date) and its first section's opening | new part |
| 7b | 1280 | reference | `frontier-comparisons-the-genuine-heisenberg-action-space` | Nothing | That section's opening, with its displayed formulae | new part |
| 7c | 375 | reference | `frontier-comparisons` | Nothing | The head and opening at phone width | new part |
| 7d | 375 | reference | `frontier-comparisons-nested-currents-and-their-completion-domains` | Nothing | Long inline formulae and displays at phone width | new part |
| 7e | 1280 | reference | `frontier-comparisons` | Switch to the dark theme with the page's own control | The head and opening, dark. Then set the theme back | new part |
| 8 | 1280 | index | `contents` | Scroll to the end of the contents, the list "Atlas and reference" | "Four frontier comparisons" after "The remaining comparisons" | new entry |

## Where and how to save (as before)

- **Folder:** `/tmp/qh-ega-root-native-20261117/captures-release-v10/` (created, empty).
- **Each capture:** a JPEG named with the first 8 hex characters of its own sha256.
- **Beside each JPEG,** a JSON of the same name with:
  - `item`, `theme`, `url` and `captured_utc`;
  - `candidate`: `index`, `reference`, `atlas` and `reader_index`, with the four hashes above;
  - `measure_label`, exactly as shown;
  - `sha256`.
- **Last,** write the manifest `CAPTURE-RELAY.json`. The website owner's watch on it resumes QA, the same session
  df53cc5e, to judge the images, then returns the release decision.
