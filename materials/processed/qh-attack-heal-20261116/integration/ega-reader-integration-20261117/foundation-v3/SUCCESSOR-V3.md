# Foundation monograph v3: scoped successor to installed v2

v1 (`../FREEZE.json`) and v2 (`../v2/FREEZE-V2.json`) are unchanged and stay frozen. All hashes are in `GUARD.json`
here. Nothing here touches publication metadata (site, slug, home, canonical), which root applies afterwards.

## Delta

**`patch/monograph-v2-to-v3.patch`, sha256 `96aba2aa533d0518d23f3baaedb933e1bb7031d45355fefa95b111340384b4da`.**
Apply it with `patch -p1` at the integration root, on installed v2. Integration's four files were checked to be
exactly v2 (198727b3…, 2cbfcfb6…, c0af80b6…, 86aa0724…).

| File | v2 | v3 |
|---|---|---|
| `compiler/quantum-holography-status/status.py` | 198727b3… | b0bf38e6… |
| `content/quantum-holography-status/page.json` | 2cbfcfb6… | 6cd6f22a… |
| `compiler/quantum-holography-status/monograph.py` | c0af80b6… | 750a232a… |
| `compiler/quantum-holography-status/monograph.css` | 86aa0724… | 0d4ed082… |

Both apply paths were checked:
- the delta on installed v2 reproduces v3 byte for byte;
- the original pins, then v1, v2 and v3, give the same result.

Still inert: with no `reader-data/`, the page is byte-identical to today's (cf89f01b…).

## What v3 does (checked on the built candidate)

1. **`data-qh-figure` on static diagrams.** The figure element is
   `figure.mg-diagram#{id}[data-figure="{id}"][data-qh-figure="{id}"]`. All 13 diagrams and all 5 atlas figures carry it.
2. **`reader.with_status_js: true`** in page.json. Body scripts run in this order: status.js (the stood-down
   version), reader.js, atlas.js, figures.js.
3. **The six CSS rules** required by reader-v1 are appended verbatim, after its header comment. My one contradicting
   rule (`.reader-search-news` shown, `:empty` hidden) is removed, so the live region is visually hidden as reader.js
   requires.
4. **Metadata.**
   - In book mode, `<title>`, `og:title`, `description` and `og:description` come from `manifest.title` and
     `manifest.subtitle`: "Chiral Quantum Groups and Holography — Raeez Lorgat" and "Local operations, duality and
     reconstruction".
   - The book's front byline and footer give the date alone: "Raeez Lorgat · 16 November 2026".
   - The reference volume's cover keeps its exact cutoff: "16 November 2026, 16:20 UTC".
   - The former page, built without reader data, keeps its own title (the inertness proof covers this).
5. **The chapter locator, repaired.** v2 removed three rules the locator shared with the old map: the SVG sizing, the
   base arc stroke, and `.mg-dots { display: grid }`. Without them the dots fell into the vertical stack in root's
   chapter 11 screenshot. They are restored, scoped to the locator. Chapter 11's locator now has 8 arcs (5 read before,
   3 later) over a row of 18 dots.
6. **The bar.** At widths up to 1480 px, the previous and next links drop the neighbouring chapter titles and keep
   "Previous" and "Next" with their arrows. The reader's own place ("Part III · Chapter 11 of 18 States, determinant
   lines and quantum fields") then gets the room.
7. **Reference definitions are never read inside a displayed formula.** This hardens the parser; no chapter needed it.

**The chapter 11 opening display (root's screenshot `chapter11-native-v2-980c98b1.jpg`).** I cropped and enlarged the
formula region. The display is **not clipped**: `Z_λ(1) = ∫_ℝ e^{−λx²/(2ħ)} dx = √(2πħ/λ), Z_λ(x²)/Z_λ(1) = ħ/λ.` is
whole, its final fraction and full stop included. It fits the measure.

## The four "working-file links" were mathematics

All four are brackets inside formulas:
- ch11, lines 78 and 276: `…\right](0)` in displays;
- ch12, line 162: `[z,z^{-1}]((w))` inside `\(…\)`;
- ch16, line 70: `[z^{m-1}](ab)` in a display.

The renderer never transformed them: it removes formulas before it looks for link syntax, and the build reported 0
working-file links. The false positives came from my diagnostic scan, which ran over raw lines.
`tools/scan_working_links.py` now blanks out formulas and code first, and finds **0** (`evidence/WORKING-LINKS.json`).

**Formula retention** (`evidence/FORMULA-RETENTION.json`, `tools/check_formulas.py`):
- each source formula is compared with the TeX annotation Temml writes in the page;
- **3,323 of 3,323 source formulas** are on the page, 0 missing;
- all four formulas above are present, as written (both ch11 occurrences, ch12 and ch16);
- the 3 "extra" annotations are the three section headings with mathematics (`\mathfrak{sl}_3` in ch06, `W_3` and
  `W_4` in ch12), which appear again, by design, in the chapter's margin list.

## Evidence on candidate `out/book.html`

The candidate is sha256 64cddb03…, 14,678,544 bytes, audit **PASS**. It was built from snapshot
`snapshot/20261116T201833Z` (manifest 342bef12…) and integration's installed lane files:
- reader.js (reader-v1) and the stood-down status.js;
- the C5 atlas and the five figure models.

The checks:
- **prose:** 46,224 words in 18 chapters, 0 lost;
- **formulas:** 3,323 of 3,323;
- **diagrams:** 13 of 13 rendered and placed, with 0 problems;
- **reader selectors:** exactly 18 `[data-chapter]`;
- **working-file links outside mathematics:** 0.

## The three-page split (interaction's `tools/split-reference.py`; no second splitter here)

The interaction lane's post-build splitter works on this DOM as it is:
- every reference place is a top-level `<section>` in `main` with its old ids;
- the chapters are `<article>`s;
- the scripts carry the markers it looks for (`/* The reader of the monograph.`, `/* The research atlas`, and
  status.js's reader-mode comment);
- it rewrites cross-page links, `data-reader-book` and the CSP `'self'` itself.

**No renderer change is needed.** One decision for root and interaction: v2 added two more top-level reference
sections, `#results-index` (about 3k elements) and `#glossary` (about 26k elements, 718 formulas).
- With `--keep programme-overview,results-index,glossary` they stay with the book page, at about 92k elements.
- With the default `--keep programme-overview` they move to `reference.html`, with their ids and links rewritten.

My suggestion is to keep the index with the book and let the glossary go to the reference page. It is a reading aid,
not reading order, and that keeps the book page near the interaction lane's 63.5k-element target.

The book's file name comes from the output path (`--output …/index.html`); the splitter's `--book-name` must match it.

## Still open

- Native QA should re-observe the locator and the bar on this candidate, or on root's build of it.
- The author owns `term-cap-reconstruction` (pending, metadata only).
- Root and interaction own the split's `--keep` choice and the index tool run.
