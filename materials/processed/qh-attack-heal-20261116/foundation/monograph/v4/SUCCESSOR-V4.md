# Foundation monograph v4: the title page's balance and the measure (QA IMAGE-02, V1 and V2)

v1, v2 and v3 are unchanged and stay frozen. All hashes are in `GUARD.json` here.

## Delta

**`patch/monograph-v3-to-v4.patch`, sha256 `ee0d4a684d051158fcd1d8ed0f123e90452a848f7f1349b9177a221924ccf6a2`.**
Apply it with `patch -p1` at the integration root, on installed v3. It touches `monograph.py`, `monograph.css` and
`page.json` (three interface words); `status.py` is not touched.

- **On integration's actual files.** These are v3 plus root's publication metadata (`site`, `slug`). The delta applies
  cleanly and keeps root's metadata. It gives monograph.py 9a7c44f3…, monograph.css d7b2a217… and page.json ff336252….
- **On the sealed v3 state.** It reproduces the staged v4 byte for byte.
- **Inertness.** With no `reader-data/`, the page is still byte-identical to today's (cf89f01b…).

## Repairs

**V1 (S3, left-heavy opening, right 40% empty).**
- The title page now uses the chapters' frame: the reading column (title, subtitle, audience, byline, the author's
  introduction) and the margin column.
- The margin column holds the book at a glance:
  - "Parts", the five parts with their chapter ranges, each linked to its part in the contents (I Observables,
    representations and locality, Chapters 1–4; … V Reconstruction and open problems, Chapters 17–18);
  - the three routes.
- Placement:
  - the rail starts below the title, so the title stays the first thing seen;
  - in reading order it comes after the introduction, so the problem still comes first (O4 holds);
  - at 1180 px or less, the rail follows the introduction as a band.
- The map and the marks key follow, as before.

**V2 (S4, frequent hyphens, about 80 characters a line).**
- The measure returns to 28 body sizes (it was 31). That is about 70 characters of EB Garamond, as on the former page.
- Lead paragraphs are not hyphenated.
- Elsewhere, hyphenation takes only words of 8 letters or more, with at least 4 letters on each side of the break
  (`hyphenate-limit-chars: 8 4 4`). This applies to chapters, the introduction, the glossary and the index.

## Evidence on candidate `out/book.html`

The candidate is sha256 4b275c45…, audit **PASS**. It uses the same snapshot (20261116T201833Z) and installed lane
files as v3, so the two candidates differ only by this layout change.
- **Prose:** 46,224 words, 0 lost.
- **Formulas:** 3,323 of 3,323 on the page.
- **Front matter order:** title block and introduction, then the rail (parts, routes), then the map and the marks.

## Not judged here

I have no page image of v4. QA should look at the first screen at 1225 px and at 1440–1728 px, in both themes, and
again at 375 px (rail as a band). QA's own conditions still stand: judge after full initialization, and after the
split.
