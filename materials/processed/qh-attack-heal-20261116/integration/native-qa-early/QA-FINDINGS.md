# Native Chrome visual QA: foundation-lane candidate b57caa1e

2026-11-16, 13:31–13:55 UTC, primary account, native Claude-in-Chrome extension (attempt 2; see
`CONNECTION-ATTEMPT-2.json`). This is QA of the **foundation-lane candidate only**. It is not the final integrated QA:
root will supply the composed candidate later.

## What was inspected, and how

- **Page under test:** byte-identical frozen copy of `foundation/preview.html`, sha256
  `b57caa1ee3621dc7d636a42fdaa2e23beee80f5ab9b59b9bd841f1b2100cc045` (the hash named in VERIFY.md), kept at
  `candidate/preview.html`. It was compared against the baseline (the current reviewed tracker,
  `foundation/baseline/preview.html`, sha256 `6a86e7fd…4df2`, kept at `baseline/preview.html`).
- **The lane moved during this QA.** The lane rebuilt `foundation/preview.html` at 13:37:47 UTC. It is now
  `15ff3966ca4f63ff71b060f63b89b26f3c7e44610a87226f4c3efbc7a861c78a` (2,286,891 bytes), with 614 changed CSS lines (a new
  type scale and spacing tokens) and changed markup. **The new build was not inspected visually.** For each finding,
  the last column gives only a static CSS indication for the new build.
- **Route:** the extension refuses `file://` URLs ("Can't interact with browser-internal or unparseable URLs. Navigate to
  a web page first."). So the frozen bytes were served from `127.0.0.1:47613` only, with the served hashes verified. No
  per-site or approval prompt appeared at any step.
- **Widths:** `resize_window` reported success but never changed the viewport. The window stayed at 1728×997, and a
  second tab got 894×749. Most likely a tiling window manager re-tiles the windows; I did not change it. Exact widths
  therefore come from a plain-HTML harness (`site/frame.html`) that loads the unchanged page into iframes of a set CSS
  width. Width media queries inside an iframe use the iframe's own width. Hover and pointer media queries stay at
  desktop values, as they would in a narrow desktop window.
- **Coverage:** 1728 (native viewport; dark and light), 1400 (light), 1280 (light), 1279 (measured only),
  1024 (dark), 768 (light, side by side with the baseline), 375 (dark, side by side), 320 (dark, side by side).
- **Interactions spot-checked:** a related-statement line opened; a table mark's scope card plus Escape; the bar search
  with one typed word ("vacuum", local search only); a contents link; arrival by address at a folded statement; Tab
  from page start; the theme toggle.
- **Not covered:** print (the native tools have no print surface); reduced motion (it needs an OS setting or CDP, both
  outside this assignment); 360, 480 and 1180 specifically; the full keyboard matrix; touch devices; status.js
  behaviours beyond the spot checks above.
- **Scientific text was treated as opaque data.** Nothing here judges or changes mathematical content.

Severity: **S1** breaks reading or navigation · **S2** a material visual-communication defect on a main path ·
**S3** noticeable polish or consistency issue · **S4** minor.

## Overall judgement

Beside the baseline, the candidate is a large and real improvement in density, conceptual navigation and phone
reading:
- The page is 70% of the baseline's height at 1728 px, 83% at 768 px and 79% at 375 px, with no research removed.
- The overview gains a contents map, in the right margin on wide screens and in flow on narrow ones.
- The example table now fits whole at every width down to 320 px.
- The type is calm and consistent in both themes.

It is **not ready** at this build: three S2 defects stand (F1–F3) and several S3 issues break the harmony of an
otherwise disciplined page (F4–F10). Two of them, F2 and F10a, look addressed in the newer lane build, judging by its CSS
alone. They need visual confirmation on the composed candidate.

## Findings (most severe first)

| ID | Sev | Where | What the page shows (measured) | Evidence | Origin, owner | New build 15ff3966 (static only) |
|---|---|---|---|---|---|---|
| F1 | S2 | Overview, 1280–≈1450 px | Contents column runs flush to the viewport edge. At 1280 the grid is 280 / 720 / 280 and the contents has no right padding. Its longest line ("…8 parts of the theory") ends exactly at the edge (0 px gap), and the hairlines run off the page. At 1400 the grid is 340 / 720 / 340 and the rules still reach the edge. At 1728 there is about 150 px of margin. 1280 is a common laptop width and the first width with this layout. | `shots/E01-…`, `E01b-…` | New in candidate; foundation (status.css overview grid) | Grid unchanged; contents max-width changed to 22rem + gutter. Right padding can't be settled statically, so re-check 1280, 1366 and 1440 visually |
| F2 | S2 | Every question card (22 decisive, 12 comparisons), all widths | Hierarchy inverted. Card heading is 26.8 px at weight 400; the question's statement title 23.2 px at 600; every related-statement title 20 px at 600 on 26 px leading. A stack of up to 14 bold two-line titles outweighs the heading it serves. In the baseline those titles sat inside full cards. Folding kept the bold weight without the frame that balanced it. | `shots/E02-…` | New in candidate's folded form; foundation | `.fold-title` weight changed 600 → 400, so likely resolved; confirm visually |
| F3 | S2 | Principal results, first card (top of the page) | Display formula cut mid-expression ("Γ∞ = {±Tⁿ : n ∈"); box 588 px, content 619 px. The scroll-shadow gradient exists but can't be seen in the dark theme and is faint in light; macOS hides scrollbars until scrolling. 12 of 316 display formulas overflow at 1728 against 10 in the baseline: one more each in comparisons and the glossary, whose boxes are narrower. | `shots/E03-…` | Pre-existing behaviour, slightly worse in candidate; foundation (CSS) | Math rules unchanged; box widths change with the new measure. Re-count overflow |
| F4 | S3 | Example table, all widths | Family names and column headers are auto-hyphenated (`.col-head-text, .grid tbody th a { hyphens: auto }`). The baseline set row labels with `hyphens: manual`. 1728: "ir-rational", "ra-tional", "spec-tral". 768: headers stack three lines ("Module / com- / parison"), about 9 hyphenated names per screen. 375: 5 of 8 names hyphenated. | `shots/E04-…`, `E05-…` | New in candidate; foundation | Same rule; persists |
| F5 | S3 | Lead and prose paragraphs | Hyphen ladders: ragged-right text with `hyphens: auto` and default limits. 1728: three consecutive hyphenated lines in the first lead paragraph. 375: 5 of 9 lead lines end in hyphens. | `shots/E07-…` (lead), table and lead screenshots | Pre-existing (identical in baseline); foundation | Same rules; persists. Option: `hyphenate-limit-chars: 7 3 3` and/or `text-wrap: pretty` |
| F6 | S3 | Running text, worst on phones | Glossary terms are `button.term` (inline-block). A multi-word term can't break across lines, so it drops whole and leaves a short line, e.g. "…and changes to full" / "ordered configuration diagrams." 334 term buttons, 117 of them three or more words. | `shots/E10-…` | Pre-existing; **cross-lane**: `button.term[data-term]` is a status.js hook (interaction lane). A fix needs an inline element (link or span with a button role); CSS on a button is not enough | n/a (hook unchanged) |
| F7 | S3 | Decisive, comparisons, examples | Measure changes inside one section. Heading, intro and index sit in the 720 px column, cards in the 1296 px container. The left edge jumps about 300 px, and "Open all / Close all" floats at the far right, away from its index. In examples, the table, hint, legend and "What the columns mean" sit on the wide edge, then the "Show" chips and row list return to the 720 px column. It reads as stacked layouts, not one grid. | `shots/E09-…`, `E02-…` | New with the wide card; foundation | Not determinable statically |
| F8 | S3 | Related-statement lines | "Proved and independently checked" is repeated on every line (12× in Decisive question 1), duplicating the mark and the header count. On phones it adds a line per item (about 84 px each) and narrows titles on desktop. | `shots/E02-…`, `E10-…` | New in candidate; foundation (`fold-status`) | Markup changed; re-check |
| F9 | S3 | Essay head | Kicker "ESSAY" over heading "Essay", then the essay's own centered title. The byline is justified and indented 24.6 px, because `.essay p { text-align: justify; text-indent: 1.4em }` outranks `.essay-byline { text-align: center }`. | `shots/E08-…` | Byline pre-existing (baseline same); foundation | Same cascade; persists. Fix: `.essay .essay-byline { text-align: center; text-indent: 0 }` |
| F10 | S3 | Bar, ≤1040 px | (a) While reading the overview no link looks current: `aria-current` stays on the hidden first item and the pinned "Programme" link is unstyled (the baseline shows the pill). (b) The link scroller fades only on the right, so once scrolled, words are cut on the left ("lts", "sons"). (c) At 375 px only 144 of 680 px of links show, with a dead gap after "Programme". | 375 px screenshots | (a) new in candidate; (b, c) partly pre-existing; foundation | (a) new `:has()` rule styles the pinned link when the first item is current, so likely resolved; (b, c) unchanged |
| F11 | S4 | Overview contents vs bar | Two names per section: the bar says "Decisive questions", "Counterexamples", "Essay"; the contents says "Constructions that would change the programme", "Natural statements that fail", "Ordered composition and independent comparisons". The page kicker bridges them, but the contents shows only the heading. Showing the short label there would join the two maps. | `shots/E07-…` | Foundation (labels, status.py) | Unknown |
| F12 | S4 | Table, after a contents jump | Hover cards open when content scrolls under a resting pointer. After the contents link the pointer landed on a mark and its card opened uninvited. | (observed at 1728) | Interaction lane (status.js): hover-intent delay or require pointer movement | n/a |
| F13 | S4 | Arrival by address at a folded statement | Title shows twice in a row: the fold line, then the statement head drawn for `:target`. This is documented behaviour. | (observed at 1728) | Foundation | Unknown |
| F14 | S4 | Footer; "Show" chips | Footer repeats the name ("Raeez Lorgat · 16 November 2026" and "Raeez Lorgat · ↑ Top"). In the 720 px column the four "Show" chips wrap, leaving "Published" alone on a second line. | `shots/E09-…` | Foundation | Unknown |

**Checked and withdrawn (not defects):**
- The search field lands 5 px clear of the bar: bar bottom 51, field top 56. My first screenshot caught the scroll still settling.
- The narrow-bar scroller does have a right-edge fade mask (24 px).
- The bar's current link did reach view; a delay of about a second after programmatic scrolling is timing, not a fault.

## What works, judged against the baseline

- **Overview and conceptual navigation:**
  - At ≥1280 px the contents in the right margin balances the cover and lead and maps every part of the page with
    counts and status marks. Below 1280 px it flows after the lead (`E07`, `E06`).
  - The question index gains a "RELATED STATEMENTS" caption, and card kickers now match the bar.
  - A contents link lands with its heading clear of the bar, and the bar marks the section current.
  - Arrival by address opens the fold, shows the context line ("Decisive question 3 · …") and clears the bar.
- **Density without loss:**
  - Page height at 1728 px: 75,463 against 108,121 px. Decisive section 19,468 against 40,557. Decisive question 1:
    1,021 against 5,329. Glossary: 16,415 against 28,481 (two columns).
  - At 375 px: 112,855 against 143,380 px. At 768 px: 78,790 against 95,228 px.
- **Example table:**
  - Whole at every tested width with all eight columns: 1214 px at 1728, 705 in 707 at 768, 341 at 375, 286 at 320.
  - Two-line headers on desktop, upright headers at ≤760 px, sticky header row, banding.
  - A scope card highlights the column and row and names status, scope, meaning and family.
  - The baseline scrolls sideways at ≤768 px, and at 320 px its status chips push the page to 364 px (page-level
    horizontal scroll). The candidate has none (`E04`, `E05`).
- **Progressive disclosure:** a related-statement line opens in place inside a box ruled in its status color.
- **Both themes:** harmonious, with status colors distinguishable in each.
- **Keyboard:** the skip link shows on first Tab; focus ring is 2 px teal, offset 2 px, under `:focus-visible`.
- **Glossary:** letter index on every width.
- **Clean page:** no console message of any kind on load. No page-level horizontal overflow at 1728, 1400, 1280, 1024,
  768, 375 or 320.

## Remaining acceptance gaps for root

1. Visual QA of the composed final candidate, natively, at the same widths and in both themes. Recheck F1–F10 there,
   especially F1 at 1280, 1366 and 1440 and F2 at desktop.
2. Print (A4, Letter; Legal and A5 as stress), reduced motion, the full keyboard matrix and status.js behaviours on
   the final markup (VERIFY.md items 2, 3, 5 and 7). None were performed here.
3. The cross-lane item F6 (term buttons) and the hover-intent item F12, for the interaction lane.

## Evidence images (`shots/`, captured from task-owned tabs)

`E01` 1280 light, contents flush to the edge · `E01b` zoom of the same · `E02` 1728 dark, Decisive question 1
hierarchy · `E03` 1728 dark, clipped first formula · `E04` 768 light, table, candidate beside baseline · `E05` 375 dark,
table, candidate beside baseline · `E06` 375 dark, contents in flow beside baseline · `E07` 1728 dark, overview with
contents margin · `E08` 1728 dark, essay head and byline · `E09` 1728 dark, alignment after the table · `E10` 375 dark,
term-button short line, both builds.
