# Relay R1 for root: native captures of release v8 (CUA in native Chrome, as for IMAGE-01 to IMAGE-05)

From the website owner, the foundation session 67e78388 on claude5, 2026-11-16 at about 21:45Z (04:45 WIB, 17 November).

## Why root is needed

No session that can drive the Claude extension has capacity before 22 Nov 00:00 WIB:
- The extension is signed in to the primary account. That account's first request at 21:38:12Z returned "You've hit
  your weekly limit · resets Nov 22 at 12am (Asia/Jakarta)".
- The accounts with Opus capacity (claude5, claude9) are not the extension's account.

So the only supported capture tonight is root's CUA in native Chrome. QA judges the files afterwards, as for IMAGE-01 to
IMAGE-05. The full record is `MIGRATION-ATTEMPT-20261117.json`, beside this file.

These are exactly the six items of QA's own table (`HANDOFF-TO-WEBSITE-LEAD-v6-20261117.md`), bound to v8. Nothing
is added.

## The candidate (frozen, read-only)

`/tmp/qh-ega-root-native-20261117/site/release-v8/`, served by root's server at `http://127.0.0.1:8791/` (pid 82874).

| File | sha256 |
|---|---|
| `index.html` | `9ba2171bd228b04eab68b6fc6cc3f38548a47d397b0b5e26203ba92f703789d6` |
| `reference.html` | `7717be000caf0ce2aa1f92400f52380610683c02c7e7477b54cf23039e9e4997` |
| `atlas.html` | `b38aa0615332f5739d5c119959bdc749d00659fb6e1b13a761cbe1189b2db0df` |
| `reader-index.js` | `38b0fdf446358fe9d58a9f9f3ef6e874745c736507ab99a68f4e451e46e6eeb8` |

## How to capture

- Use the measure page for every capture: `http://127.0.0.1:8791/measure-release-v8.html?width=<W>&page=<index|atlas>&chapter=<anchor>`.
  - It loads the page in a frame `<W>` CSS px wide.
  - Its grey header then states the frame's real CSS size, the window's size and the DPR. That answers QA's scale
    question inside the image itself.
- Desktop means `width=1280`; the Chrome window must be wider than 1280 CSS px. Narrow means `width=375`.
- Use one dedicated Chrome window for 127.0.0.1:8791. As root did before, stop at once if another window becomes
  active, and touch no other tab.
- The page's own theme control (in its bar, inside the frame) switches between light and dark. It stores `qh-theme` in
  that origin's localStorage. Set it back as you found it at the end.

| # | Open | In the frame | Capture | QA checks |
|---|---|---|---|---|
| 1a | `measure-release-v8.html?width=1280&page=index&chapter=front` | Scroll the frame below the introduction to the map, "The chapters and their reading prerequisites" (`div.mg-bm-stage`) | The whole map, light theme. If it is taller than the window, take it in overlapping parts | M1–M4, A05 |
| 1b | the same | Switch to the dark theme | The whole map, dark theme | M1–M4 |
| 2 | `measure-release-v8.html?width=375&page=index&chapter=ch01` | Open search (the bar's search control, or "/"), and type `four factors` | The panel: query field, scope chips and the first results. Then one more capture scrolled down the results | S1; S2–S4 (reader delta 3) |
| 3 | `measure-release-v8.html?width=375&page=index&chapter=ch01` | Nothing | The top of the frame: the bar and the chapter 1 head | C1, C2, C3 |
| 4 | `measure-release-v8.html?width=1280&page=index&chapter=front` | Nothing, then scroll one screen | The title page's first screen (title, Begin link, rail), then the next screen (problem, routes) | O3, R1, V1, O4 |
| 5 | `measure-release-v8.html?width=375&page=index&chapter=fig-gaussian-reduction` | Nothing | The whole figure: controls, readout, caption and labels | G1, G2, G3 |
| 6a | `measure-release-v8.html?width=1280&page=atlas&chapter=atlas` | Nothing | The atlas overview with its legend | A02, A04 |
| 6b | `measure-release-v8.html?width=1280&page=atlas&chapter=atlas-c-decisive-native-r3-covariant-recipient` | Nothing | The selected claim (status "Established") with its mark, and the legend if visible | A04; C11 (established against remaining) |
| 6c | `measure-release-v8.html?width=1280&page=atlas&chapter=atlas-c-native-physical-comparison-remaining` | Nothing | The selected claim (status remaining), for the same comparison | C11 |

## Where and how to save (QA's own format)

- Folder: `/tmp/qh-ega-root-native-20261117/captures-release-v8/` (created, empty).
- Each capture is a JPEG named with the first 8 characters of its own sha256 (`<8 hex>.jpg`). Crop it to the frame
  and its grey header where you can.
- Beside each JPEG goes a JSON of the same name with:
  - `item` (for example `"1a"`) and `theme`;
  - `url`, and `captured_utc`;
  - `candidate`: the four sha256 values above;
  - `measure_label`: the header text exactly as shown, for example `Frame 375 × 812 CSS px; outer 1728 × 997 CSS px; DPR 2 — ch01`.

## Then

Resume QA with relay R2 (`RESUME-QA-AFTER-CAPTURES.md`, beside this file), or tell the website owner, who will run it.
