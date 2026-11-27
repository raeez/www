# Relay for root: native re-capture of items 5 and 6 on release v9

From the website owner, the foundation session 67e78388, now on claude4. Written 2026-11-16 at 23:46Z (06:46 WIB,
17 November).

## The candidate (frozen, read-only)

`/tmp/qh-ega-root-native-20261117/site/release-v9/`, served by root's server at `http://127.0.0.1:8791/` (pid 82874).

| File | sha256 |
|---|---|
| `index.html` | `702aca5cd4bde739ddb12c88b93ee7a31e13386a0ca3efc68056d2fbf6b2fd36` |
| `reference.html` | `0c9363d393d0a1e940fe2be34d978aa943c7f65b6028958f6674d3c8bd9d8cf1` |
| `atlas.html` | `7b043c0bf1ef7a7b350070f224cb8ba18d0ea97cbd5ef6d2721a2eb11a94e40d` |
| `reader-index.js` | `4d6cdd5f39dc193e24b2eac5d3bf4c14abf924ddc4c6bbf977d1c81cbc1c1bc0` |

## Why only items 5 and 6

v9 is v8 plus the atlas lane's sealed repair of QA's G4, A2 and A6, with G5. Against v8 it is proven, in
`release-v9/CONFINEMENT.txt` and `COMPARE-v8-v9.json`, that:
- **`index.html`** changed only in the Gaussian figure (chapter 1 is identical outside it), the figures script and the
  style block;
- **the style block:** all 41 CSS rules that differ are scoped to the atlas or the figures;
- **the search index:** it changed only in the Gaussian figure's entry.

Items 1 to 4 (map, search, chapter 1 head, title page) therefore render as in v8, and QA's v8 passes for them stand.

## How (as for v8)

- Every capture uses the measure page, `http://127.0.0.1:8791/measure-release-v9.html?width=<W>&page=<index|atlas>&chapter=<anchor>`.
  Its grey header states the frame's CSS size and DPR.
- Use one dedicated Chrome window, and touch no other tab.
- Use the light theme, and leave it as found.
- **Move the pointer out of the frame before every capture.** This is QA's hygiene note: in several v8 images the
  pointer sat inside the frame.

| # | Open | In the frame | Capture | QA checks |
|---|---|---|---|---|
| 5-top | `measure-release-v9.html?width=375&page=index&chapter=fig-gaussian-reduction` | Nothing | The top of the figure: controls, the first plot with its scale and its readout | G4, G5 |
| 5-middle | the same | Scroll one screen down | The next plots, with their scales, readouts and the note "The curves share one vertical scale" | G4, G5 |
| 5-bottom | the same | Scroll to the figure's end | The values table | G5 |
| 6a-map | `measure-release-v9.html?width=1280&page=atlas&chapter=atlas` | Scroll to "Claims and recorded relations, by domain" | The map | A2 |
| 6b | `measure-release-v9.html?width=1280&page=atlas&chapter=atlas-c-decisive-native-r3-covariant-recipient` | Nothing | The page with the claim's pane open: the pane's head with Close, its locator of the whole atlas, and the index and filters beside it | A2, A6, C11 |
| 6c | `measure-release-v9.html?width=1280&page=atlas&chapter=atlas-c-native-physical-comparison-remaining` | Nothing | The same, for a remaining claim | A2, A6, C11 |
| 6d | Continue from 6c | Click "Show in the map" in the pane | The map, with that claim's pill highlighted | A2 |

## Where and how to save (as for v8)

- **Folder:** `/tmp/qh-ega-root-native-20261117/captures-release-v9/` (created, empty).
- **Each capture:** a JPEG named with the first 8 hex characters of its own sha256.
- **Beside each JPEG,** a JSON of the same name with:
  - `item`, `theme`, `url` and `captured_utc`;
  - `candidate`: `index`, `reference`, `atlas` and `reader_index`, with the four hashes above;
  - `measure_label`, the header text exactly as shown;
  - `sha256`.
- **When done,** write the manifest `CAPTURE-RELAY.json` in the same folder. It is the signal: the website owner's
  watch on that file resumes QA, the same session df53cc5e, to judge the images, then returns the release decision.
