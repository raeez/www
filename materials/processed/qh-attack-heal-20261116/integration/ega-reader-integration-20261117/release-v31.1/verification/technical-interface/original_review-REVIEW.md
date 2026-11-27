# The handset blank area: diagnosis and source repair for v31.1

Session bb336ab5-d523-4bb8-bf88-c355232deaaf (claude8, claude-opus-5-5, max), 20 November 2026. Everything below is in
this `work/` folder unless a full path is given. The principal's screenshot and every inspection image stay on this
machine; nothing was posted or sent to an external service.

## Result

The blank lower region is not missing or hidden layout. It is page tiles that the phone's WebKit content process had
not yet painted after the reader scrolled. The process was still busy with the page's load: parsing a 6.5 MB page
while laying out all nineteen chapters, which the reader then hides, followed by search indexing in whole-chapter jobs.

The repair keeps the places the reader does not show from being laid out while the page loads, and builds the search
index when the search first opens. It changes four interface sources and no mathematics.

On the reported geometry in WebKit:
- the longest stretch in which the page could not paint falls from 2.91 s to 1.56 s;
- the page settles at 2.80 s instead of 4.50 s;
- the content process's memory falls from 728 MB to 474 MB.

The publisher's own acceptance battery gives identical results before and after: 16 runs, 4 viewports, both themes.
Native iPhone confirmation is still outstanding (see "Device classes").

## Device classes that actually ran

| class | status |
|---|---|
| Physical iPhone | None attached to this machine. |
| iOS Simulator | Not usable. Xcode 27.1 is installed, but its licence has not been accepted and no iOS simulator runtime is installed. I accepted no licence and downloaded nothing. |
| WebKit | Playwright WebKit 2272 (engine version 26.4): desktop WebKit on macOS with iPhone emulation (viewport, scale factor, touch, mobile user agent). This is emulation, not iOS: its tile painting does not follow the iOS UI-process path. |

The blank area did not reproduce in desktop WebKit, in screenshots or in scroll recordings made during load
(`before/video/`). That is expected for a painting fault specific to iOS, so the diagnosis rests on the screenshot's own
geometry and on measured load cost.

## The fault, from the screenshot

Source: `../screenshots/original-handset.jpeg`, 43,059 bytes, sha256 ed7344505c0fafff45db6dcbfa028ee691bdfef457ce7863d4ccd380eb6f2e63. The file is unchanged; a raw decode is at `before/original-handset.rgb`.

1. **In-app browser.** The header has a close button, the page title and the domain, so the engine is iOS WKWebView. Its content area starts at image row 79. The book's sticky bar, showing the reader's own controls (`→`, Search, theme), spans rows 79–121. So the reader had already started when the screenshot was taken.

2. **The handset is 440 points wide**: the iPhone 16/17 Pro Max class (440 × 956 points at scale 3), reduced to 360 × 782 (factor 0.818). I laid out the screenshot's two paragraphs at each candidate width (`tests/lines.cjs`). Only 440 reproduces every line start in the screenshot:
   - "Here 1 is…", "sides have the…", "around w with…", "f(z)J(z)J(w)…", "zero. The weight…", "the two fields…", "the quantity the…";
   - and the second line of the next paragraph, "in the two possible orders…". At 430 that line begins "Integration in the…"; 360, 393, 402 and 420 break differently.

   The scale is consistent: 29.26 px line pitch × 0.818 = 23.9 image px (measured 23.75), and the margin and indent also agree.

3. **The straight edge is a tile boundary.** I registered the screenshot against a WebKit rendering at 440 px (`tests/register.cjs`, `before/register/register.json`):
   - The screenshot's scroll position is document y ≈ 644 CSS px.
   - Its lower edge (image row 390, which cuts through the glyphs of "in the two possible orders…") lies at document y = 1024.4 CSS px, with a row uncertainty of 1.2 px.
   - In device pixels that is 3073. 3072 is the bottom of the sixth row of WebKit's 512-device-pixel tiles: 0.44 CSS px away.
   - Tile rows recur every 170.7 CSS px, so a chance landing within the uncertainty is about 1.4 % likely.

   Everything above the edge was painted. That is the first frame's tile coverage: an 852-px view at scroll 0 plus one tile row. Nothing below was painted after the scroll to 644.

4. **The layout under the blank is present**, and the other candidate causes were examined:
   - In the same state at every tested geometry, `elementFromPoint` at 30, 50, 60, 75 and 90 % of the viewport finds Introduction text (`after/repro/*.json`; the publisher's front-scrolling samples agree).
   - There is no horizontal overflow at any geometry. The visual viewport equals the layout viewport at scale 1.
   - Viewport-height units cap only overlay panels, never page layout.
   - No figure, grid or breakpoint rule ends there. The edge runs through a line of text, not along an element boundary.
   - The blank colour (21, 20, 19) is the page background, so it is not an overlay.

## The cause, measured

The page is one 6.5 MB document. The v30 page that was served when the screenshot was taken has 162,168 elements,
including 10,466 MathML formulas. Read without scripts, the v31 book is 687,245 px tall at 440 px wide and 814,203 px
at 360 px.

The reader runs at the end of the body and shows one place at a time. Until then, WebKit lays out every chapter as it
parses: hundreds of thousands of pixels of text and formulas that the reader immediately hides. After the reader starts,
the served runtime also builds the search index in one job per whole chapter. Its 8 ms budget is checked only between
jobs, and Safari has no `requestIdleCallback`.

On iOS the content process paints newly scrolled tiles. While its main thread is busy, or its memory is high, those
tiles stay blank. That is the state the screenshot shows.

Load cost (desktop WebKit, iPhone emulation, dark theme). Each row is the median of three fresh loads, with requests
leaving the local server refused (`tests/settle.cjs`, `after/settle/settle.jsonl`). A "stretch" is time in which a
10 ms timer could not run, measured after the first frame.

| page set | viewport | first frame | stretches after first frame | longest stretch | settled | content process |
|---|---|---|---|---|---|---|
| v30 served (on the phone then) | 440 × 852 @3 | 2.63 s | 3.58 s | 2.87 s | 4.22 s | 713 MB |
| v31 served | 440 × 852 @3 | 2.84 s | 3.66 s | 2.91 s | 4.50 s | 728 MB |
| **v31 repaired** | 440 × 852 @3 | **1.33 s** | **2.25 s** | **1.56 s** | **2.80 s** | **474 MB** |
| v31, head mark and stylesheet rule only | 440 × 852 @3 | 1.35 s | 2.29 s | 1.57 s | 2.75 s | 535 MB |
| v31, runtime change only | 440 × 852 @3 | 2.66 s | 3.61 s | 2.86 s | 4.32 s | 662 MB |
| v31 served / repaired | 360 × 782 @3 | 2.38 / 1.16 s | 3.68 / 2.21 s | 2.92 / 1.52 s | 4.06 / 2.60 s | 735 / 478 MB |
| v31 served / repaired | 1440 × 900 @2 | 2.54 / 1.42 s | 3.45 / 2.23 s | 2.70 / 1.55 s | 4.20 / 2.86 s | 723 / 482 MB |

The stylesheet rule accounts for the time and most of the memory. Building the index on demand removes about another
60 MB and, on a phone, the train of whole-chapter tasks after load.

A timeline profile (`tests/timeline.cjs`) shows the reader script itself takes about 0.12 s. The stretch that remains
after the repair is parsing the document, the front view's layout after the script, and the embedded fonts swapping in
before `load` (see "What remains").

## The repair

The patch is `source/handset-paint.patch`: 7,772 bytes, sha256 0b60cb4f999e34c6baf814f4c5a8e31a375082d4025f53f4e69b908fb1a858e7.
- Its base is `source/a/`, copied from the sealed v31 parent (`ega-falsification-20261120/mobile-issue/native/parent/source-tree`).
- The result is `source/b/`.
- All four files are byte-identical in that parent and in the ROLE's release-v30 `source-tree`. Neither edition changed them, so the patch serves both.

| file | change |
|---|---|
| `compiler/quantum-holography-status/status.py` | The head script that already applies the stored theme now also marks the root `data-reader-js` before the body arrives. At `DOMContentLoaded` it removes the mark if no reader has started (no `main[data-reader-on]`). Without scripts the mark is never set. |
| `compiler/quantum-holography-status/monograph.css` | `html[data-reader-js] main[data-reader]:not([data-reader-on]) > :is(article[data-chapter], section[data-reference]) { content-visibility: hidden; }` (with a comment). It applies only until the reader starts. The reader marks itself running in its first statements and shows one place before anything is measured. Find-in-page, print, navigation and the reader's `hidden="until-found"` handling are therefore exactly as before. |
| `compiler/quantum-holography-status/reader-runtime/reader-book.js` | `indexWhenIdle` and its two calls (at the start and on `qh:content-changed`) are removed. The search units are built by the existing `index()` when the search opens or `qh:reader-units` asks; a comment states this. |
| `compiler/quantum-holography-status/reader-runtime/reader-companions.js` | The same change for the reference and atlas pages. |

Why this is safe:
- Browsers without `content-visibility` or `:is()` ignore the rule and behave as now.
- A reader that fails before starting leaves the whole book visible, by the fail-safe in the head script.
- Comments added to public CSS and JS contain no process or tooling vocabulary (checked against the gate list).
- The patch touches no content file, so no mathematical prose or result changed.

Result hashes:

| file | sha256 | bytes |
|---|---|---|
| `status.py` | d71fa427f74be07cb8ab0ad3a2036db48827a8b447d80dcde5014886c97d9d6d | 84,851 |
| `monograph.css` | 52cff215b141f7a9f0e303a898abb96ccd505a3189ba58d56bbd0814984d4591 | 57,715 |
| `reader-runtime/reader-book.js` | 826fa7955a8830efe51b7e62f8dc4421a5022cd09d0699baf021e047af29981e | 123,949 |
| `reader-runtime/reader-companions.js` | 356f311f234808151c2869dd47d80582553bd51585fe6def685b9ae61264c7aa | 122,588 |

Replay checks I ran (scratch copies in `source/replay-check/` and `source/replay-check-v30/`):
- the intake's exact command, `/usr/bin/patch -s -t -g 0 -F 0 -V never -p 1`, as a dry run and then for real, on both bases; it applies with zero fuzz, and every result is byte-identical to `source/b/`;
- `node --check` on both runtimes;
- a Python parse of `status.py`.

For the publisher's intake (I did not run it, because it writes a lock file inside the publisher's folder):

```
python3 intake_apply.py --patch <work>/source/handset-paint.patch --review <work>/REVIEW.md \
  --browser-evidence <work>/after/accept/v31-fixed-440x852-dark.json --browser-evidence <work>/after/regress/v31-fixed-440x852-dark.json \
  --browser-evidence <work>/after/repro/v31-fixed.json --browser-evidence <work>/after/settle/settle.jsonl \
  --browser-evidence <work>/before/register/register.json --candidate <work>/source/b \
  --file compiler/quantum-holography-status/monograph.css --file compiler/quantum-holography-status/status.py \
  --file compiler/quantum-holography-status/reader-runtime/reader-book.js \
  --file compiler/quantum-holography-status/reader-runtime/reader-companions.js --preview
```

## How the pages were tested

`tests/compose.py` builds the test pages from the served v31 files
(`ega-falsification-20261120/cubic-issue/build/hosted/quantum-holography/`; `index.html` matches the canonical
readback, sha256 3e6629ce…). It replaces the head script, `monograph.css` and the reader runtime with their patched
text. Each occurs verbatim exactly once in each page, so the composed pages are what the patched build serves:

| page | sha256 | bytes |
|---|---|---|
| `index.html` | afea6330… | 6,588,274 |
| `reference.html` | 5f302d95… | 5,115,331 |
| `atlas.html` | 31182306… | 11,559,151 |

All four page sets are in `sites/`. They are served locally under `/quantum-holography/` (`tests/serve.cjs`). Every
browser test refused requests that leave the local server, including the served page's analytics.

## Regression results

1. **The publisher's own battery, unmodified.** `tests/publisher-accept-reader.cjs` is a byte copy of `ega-falsification-20261120/mobile-issue/reader-directions/accept-reader.cjs` (sha256 e27a5bb1…).
   - **Runs:** served and repaired v31 in WebKit at 360 × 782, 440 × 852, 375 × 548 and 1440 × 900, in light and dark (`after/accept/`, 16 files). `tests/accept-summary.py` prints the comparison.
   - **Coverage:**
     - start and reload at the top;
     - the byline link to https://raeez.com;
     - front scrolling through the screenshot's passage;
     - direct chapter link, Next, Back and Forward;
     - contents to Chapter 19;
     - 22 figures, with the energy-exchange choice changed by tap and by Space;
     - search to a Chapter 19 result after the companion index loads;
     - the atlas deep link and the reference page;
     - the changed-passage notice for an old address, and a retained old address.
   - **Result:** every check passed in every run, and the repaired pages give the same facts as the served pages in all 8 configurations. There were no page errors, and the only refused request was the analytics script.

2. **Supplementary checks.** `tests/regress.cjs`, `after/regress/`: 440 × 852 dark, 360 × 782 light, 375 × 548 dark and 1440 × 900 light, served and repaired.
   - **Start:** the reader is on, at the title page, at y = 0, with 20 places hidden until found; there is no overflow. Only the repaired page keeps the root mark.
   - **Theme:** the toggle persists across a reload.
   - **First search:** 79 results. 0.92–1.03 s repaired against 0.84–1.02 s served (the full UI round trip); no consistent difference.
   - **Print:** the printed title-page height is unchanged.
   - **Named destinations:** all nine open in view at 66 px below the bar, identically. They are #book-abstract, #book-abstract-h, #fig-front-exchange, #ch05, the Chapter 4 theorem, #fig-energy-two-exchange, #fig-ordered-cut-support, #ch19 and #ch11-relative-phase.
   - **Without scripts:** the whole book, all 20 places shown, and #ch05 lands at the top.
   - **With the reader made to fail before starting:** the head script removes the mark, all 20 places are shown, and the page is the whole book.

3. **Reproduction sweeps.** `tests/repro.cjs`, `after/repro/`: 27 frames per page set. The geometries are:
   - 360 × 782 (the screenshot's pixels);
   - 393 × 762;
   - 375 × 548 (small, Safari toolbar);
   - 430 × 839;
   - 852 × 323 (landscape);
   - 440 × 852 (the reported handset's in-app view);
   - 440 × 810 (the same handset in Safari, toolbar shown);
   - 956 × 400 (the same handset turned);
   - 1440 × 900.

   Each frame holds the screenshot's passage at successive offsets and records:
   - the viewport and visual viewport;
   - the scroll position;
   - the boxes of the front, its frame, the Introduction and the passage;
   - the five content probes.

   All 27 geometry records are identical between served and repaired, and every probe finds content. One earlier sweep loaded no document: the script compared a relative path with an absolute root. It is kept apart in `after/invalid-empty-documents/` (see `EXCLUDED.txt`) and excluded from every finding. The script now resolves the site itself and stops unless the book and its reader loaded.

## Screenshots (private, on this machine)

- **Before (v30, the edition on the phone):** `before/before-handset-360x782-{0,1,2}.png` and `before/before-inapp-393x762-{0,1,2}.png`. The 440-px rendering used for the registration is `before/register/render.png`.
- **After, frame by frame, served and repaired:** `after/repro/v31-<geometry>-{0,1,2}.png` and `after/repro/v31-fixed-<geometry>-{0,1,2}.png`.
- **The screenshot's passage and the Chapter 4 theorem:** `after/regress/<set>-<viewport>-<theme>-landing-passage.png` and `…-ch04-theorem.png`.

At 440 × 852, the repaired page shows the screenshot's passage with the same line breaks, and the text and displays run
to the bottom of the view. The Chapter 4 theorem shows its environment, inline formulas and cross-references below the
reading bar.

## What remains, and limits

- **Native confirmation.** Confirmation on the reported handset is still outstanding: an iPhone 16/17 Pro Max class, in the same in-app browser and in Safari, opening the canonical address fresh and scrolling at once. This falls to the publisher and the operating officer after publication. Nothing here proves the edge cannot recur on iOS. The repair halves the window in which it can occur, and removes a third of the memory.
- **The remaining stretch of about 1.5 s** (desktop WebKit) after the repair has three parts:
  1. parsing one document of about 160,000 elements;
  2. the front view's layout. Its Introduction alone is 36,652 px at 360 px wide.
  3. The four embedded fonts load with `font-display: swap` and are ready only at `load`, which re-lays out the front view.

  Further reductions would change the fonts' loading, or the one-page delivery of the nineteen chapters. Both are wider decisions than a point release, and I did not make them.
- **Overlay panels.** These are the contents, the cross-reference preview and the search panel. They cap their height with `100vh`, which on iOS is the height with the toolbars retracted. They are unrelated to this fault and were left unchanged.
- **Boundaries kept.** I made no commit, push or publication, and edited nothing in the publisher's folders or any source edition. No provider or account command was run. No mathematics was touched.

## Records written for this task

- `ACK.json`: the intake acknowledgement.
- `review/FINAL-DIRECTIONS.json`: the final website directions, read in full.
- `review/V33-FOLLOWING-ASSIGNMENT.json`: receipt of the later scientific-reader design, ordered after this delivery.
