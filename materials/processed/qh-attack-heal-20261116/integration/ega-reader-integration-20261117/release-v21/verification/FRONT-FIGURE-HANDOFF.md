# v21 front figure: integration handoff

For the direct technical integrator, /root/qh_first_principles_reader/index_bindings. Written 2026-11-18T07:42Z by the QH native Opus owner (session df53cc5e, claude11, claude-opus-5-5 max).

**Status: ready for integration. Native visual acceptance is not claimed.** This lane had no assigned native browser. The only connected device, a remote Windows "Browser 1", has no ownership assignment, so it was left alone as root ruled. No headless browser or synthetic screenshot was used. The figure has not yet been seen rendered. Its first native viewing belongs to the v21 candidate review.

## The design choice

There is one explanatory figure, titled "Counting quanta and measuring their exchange". It goes in the front, directly after the fourth paragraph (which ends "…with certainty in the second.") and before "How could a field produce this exchange?". At that point the reader has met a, b, both preparations, the counting result and S, and the field realisation has not yet begun.

The figure has two parts:

1. **The alternatives.** The first harmonic is drawn as a wave on a circle with one crest and two quanta, labelled a, "two quanta in the first harmonic". The second harmonic is drawn with two crests and one quantum, labelled b, "one in the second". Accent-coloured arrows join them, marked Sa=b and Sb=a.
2. **Two alternative measurements on fresh preparations.** The columns are "The sum (a+b)/√2" and "The difference (a−b)/√2".
   - Under "Counting quanta", both columns show identical half-filled bars, "half the time", for "two in the first and none in the second" and for "none in the first and one in the second".
   - Under "Measuring the exchange S", the sum has a full bar at +1 "with certainty" and an empty bar at −1. The difference is the mirror image.
   - Every bar has the same length, so a full bar means certainty and a half bar means half the time.

What the figure deliberately leaves out:

- **The disk reading.** The front keeps to one measurement, and the weights and moments are in Chapter 11. A disk figure, if one is ever made, must show fluctuating single readings with means +2 and −2, never a definite value.
- **The half-space 2S construction.**

## Files (all under /tmp/research-resume-1333/opus/v21-native/output)

| File | SHA-256 | Bytes | Use |
| --- | --- | --- | --- |
| front-figure.html | c52400bdd8b9c5fb729e53739db46fd65c872e3525b29d2e7926e4e203985302 | 11376 | The figure markup on one line, with inline SVG. Insert it without the file's final newline. |
| front-figure.css | d684b82f3fc3e0a8541dfc97c379499629028543f590191c5d0f8d112e831b1b | 5281 | The figure's CSS. |
| rendered-introduction-with-figure.html | fdad4967a533c5f0402a2405daba7f25eac2dd7afadc249268fb3d3690bbffa9 | 18289 | The production front fragment a32b373f with the figure already inserted, so it can be swapped in whole. |
| sources/rendered-introduction-a32b373f.html | a32b373f3b8ca91192a1f2e150b3f618563ac9c89c88e06f55ce7fdf1d3b86bd | 6906 | A snapshot of the production fragment used. |
| tools/make_front_figure.py | 1ce4fec3726b308da7739c70218dd2513c56874a4d340e35e10cbf0b38fb106b | | Regenerates every file above from the pinned inputs. It refuses to run on any pin mismatch. |
| preview/index.html | a746173add75a3854531925c5a8719416cc5c5b54cf1b2611d49c476b150e81c | 4967752 | A local preview only, never for release. |
| preview/harness.html | aabfbe7da3b66911d1e539d28847a5e8eac063daf650dbaa893964e9e330507e | 2809 | Frames at exact CSS widths of 1280, 820, 390, 360 and 320, in both themes, for the native pass. |

The preview is the issued v20 page with the v21 subtitle, the v21 front introduction, the figure and the CSS added. Its rail and chapters are still v20.

## Insertion locations

1. **Markup.** Insert the figure in the production front fragment, immediately after its fourth `</p>`, at character offset 4034 of a32b373f. That is between `…in the second.</p>` and `<p>How could a field produce this exchange?`. Alternatively, replace the fragment with rendered-introduction-with-figure.html. In the built index.html the figure sits inside `header#front > .mg-front-frame > .mg-front-main > div.mg-front-intro`.
2. **CSS.** Append front-figure.css inside the page's single `<style>` element, immediately before its only `</style>`. That is character offset 624001 in the issued v20 index.html. It must come after the site's `.qh-fig` rules.
3. **The other three public assets.** reference.html, atlas.html and reader-index.js need no change for the figure. Whether the search index lists the figure's title and caption is the build owner's choice. I did not add the `data-block-title` attribute that chapter figure titles carry.

## Pinned inputs

| Input | SHA-256 |
| --- | --- |
| Landing copy, unchanged, with the first-reader PASS reported by root | 7a530f2329eba6115dc7fc6a921ad5562a9d96c9d7cbb75b1ee0055ea4d0c1c0 |
| Author figure copy, FIGURE-COPY.json | fca18e92feb0544a1a3e62273c8292435b2740232e6e5d815170602aa787025b |
| Production front fragment, rendered-introduction.html | a32b373f3b8ca91192a1f2e150b3f618563ac9c89c88e06f55ce7fdf1d3b86bd |
| Owner manifest (read, not modified) | a2513b5a5e473837aaba0c3587a014354b36520a28bf70570dc721ae9ea6de5f |
| Issued v20 index.html | 8104f3db49f6fe1db88bb6a71fc9e58e05fb1e23854890682c2bc70fea62bc3f |

The issued v20 index.html is commit 627861ecafa9844fb274dcfd55f2c0ce2ba9bd5c, served exactly according to /tmp/qh-reader-post656-20261118/technical/final/PUBLICATION.json. The v20-editable-default/public bytes are raw compiler output, and nothing here is built on or attributed to them. Their style block is byte-identical to the issued page's.

## How it fits the existing assets

- It reuses the page's own figure frame and parts: `.qh-fig`, which gives the top rule, spacing, container and print break-avoid; `.qh-fig-head` and `.qh-fig-title`; and `figcaption.qh-fig-caption`.
- Every new class starts with `qf-ex-`. That prefix and the ids `fig-front-exchange` and `fig-front-exchange-title` do not occur in the issued page.
- The figure script selects `figure[data-figure][data-config]`. This figure has neither attribute, so the script leaves it alone.
- Colours come only from the page tokens `--ink`, `--ink-2`, `--ink-3`, `--rule`, `--rule-soft` and `--accent`. Light, dark and print therefore follow the page.
  - Bars carry print-color-adjust.
  - Forced-colours mode maps the bars, rings and arrows to CanvasText.
- There are no dashed lines, because the page reserves dashes for open comparisons. The circle under each wave is a thin solid line.
- At figure widths of 26rem and below, which covers phones, a container query shrinks the circles and the gutter between the columns.
  - Expected widths, computed rather than observed, with the page gutter clamp(16px, 4vw, 40px): a 390 px viewport gives a 358 px figure, 360 px gives 328 px and 320 px gives 288 px.
  - On desktop the figure is the front measure, 28 × text-base, about 504–588 px.
  - The table is fixed-layout at 100% width, and nothing in the figure scrolls sideways.
- Its math is the production renderer's own MathML, copied byte for byte from a32b373f: a, b, S, Sa=b, Sb=a, (a±b)/√2 and ±1.

## Author copy and labels

- **The author's copy is used verbatim.** The title goes in `.qh-fig-title`, the caption in `figcaption.qh-fig-caption`, and the accessible description in a visually hidden paragraph `.qf-ex-sr`.
- **Accessibility.** The drawing, `.qf-ex-body`, is `aria-hidden`. Assistive technology therefore reads the title as the figure's name, then the description once, then the caption.
- **Labels inside the drawing** are the author's words:
  - From the landing: "two quanta in the first harmonic" and "one in the second" (paragraph 2); "two in the first and none in the second", "none in the first and one in the second" and "half the time" (paragraph 3); "with certainty" (paragraph 4 and the caption); and "The sum" and "The difference" (paragraph 3, capitalised as headings).
  - From the figure copy: "Counting quanta" from the title, and "Measuring the exchange" from the caption, followed by the author's S.
- **Optional author confirmations.** None of these blocks integration.
  - The two group headings are "Counting quanta" and "Measuring the exchange S".
  - "The sum" and "The difference" are capitalised.
  - The caption's "+1" and "−1" are plain text, verbatim, while the running text sets them as MathML.
- **No new scientific wording was written.**

## Boundary and the remaining native review

- Browser evidence is recorded verbatim in STATE.json. One remote Windows device was connected, with isLocal false. The tab that the tab-context call created was closed at once, without navigation.
- No native screenshot exists for the v20 front or for this figure.
- When an assigned native browser exists, review the v21 candidate at desktop width and at phone/narrow widths, in both themes:
  1. The first harmonic reads as one crest and the second as two, against the base circle, and the dots read as quanta.
  2. Sa=b sits over the right-pointing arrow and Sb=a under the left-pointing arrow, and the accent colour is visible.
  3. The counting bars are identical in the two columns, and each half fill is visibly half of its outlined track.
  4. In the exchange group the full bar is under +1 for the sum and under −1 for the difference, and the empty tracks are visible.
  5. Values align right, labels wrap cleanly at 390, 360 and 320 with no overlap, and nothing scrolls sideways.
  6. The title, top rule and caption match the page's other figures.
  7. A screen reader reads the description once and does not read the drawing.
- The six W-algebra table-note and responsive checks in /tmp/qh-notation-native-qa-20261118/CURRENT.json are preserved, unmodified, for the same final pass.
