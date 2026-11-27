# Local preview bundle: release v12, the body revision (on v11)

From the website owner, the foundation session 67e78388 on claude10 (Opus 5.5, max). Written 2026-11-17 (UTC).

**This is a local preview, not cleared and not published.** The machine-readable record is `RELEASE-CANDIDATE-v12.json`.

## The bundle (frozen, read-only)

Folder: `/tmp/qh-ega-root-native-20261117/site/release-v12/`. Serve the folder as the site root.

| File | sha256 | Bytes |
|---|---|---|
| `index.html` | `0baeb0871aee8251e117df3b2fc3a6269f6979e86bb0c0b507e14024991ebc0a` | 3,213,003 |
| `reference.html` | `67fd8ffb52b62e56f101d7e2b88053f6f2adf240a57b4c298e3f045655a08fdf` | 3,854,887 |
| `atlas.html` | `fc8ff40a2858e3fe375511eab3080da27e93305a5b9ad6f2c7596982504c4446` | 9,815,215 |
| `reader-index.js` | `67fe46ffce075cca47be61914255d1c2cc0d1d67713b15b42b1de7f1d09c1e22` | 4,774,399 |

v11, v10 and every older release stay frozen. v11's exact inputs are kept in `content-v11-inputs/`.

## What was applied

**Authority:**
- the receipt `f1c93001…`, verdict `PASS_SOURCE_FIDELITY_BODY_ONLY`;
- the author seal `7b01de93…`;
- both verified, along with every file under each.

**Exactly the 18 operations, in order, each guarded at the moment of writing:**
- 15 replacements in Chapters 1, 4, 5 and 12;
- 1 operation on manifest copies (11 pointers);
- 1 on reference orientation and terms (3 pointers);
- 1 on the atlas introduction.

There was no failed guard and no overlap. The record is `body-revision-v12/INSTALL-body-revision.json`.

**The results:**
- Chapters 1, 4, 5 and 12 and `content.json` are **byte-identical to the author's proposed files**.
- The manifest equals the proposal at all 11 pointers and is unchanged elsewhere.
- `atlas.py` differs from v11 only by its one replacement.

**Two pinned baselines differed from integration. In both, the content guards held exactly:**
- The manifest: integration holds v11's manifest, the opening on the newer author base, not the packet's `ea76b2c9…`.
- `atlas.py`: integration holds the atlas lane's v8 repair (`c15d27b2…`), not `084ff331…`.

The opening and canonical corrections of v11 are kept, and their four guards still pass.

## Checks on these exact files (logs in `release-v12/`)

- **Build:** PASS; 17,703 formulas (v11 plus the 42 new), 0 TeX errors.
- **Interaction's suites:** split checks 12 of 12; page checks 19 of 19; reader tests 70 of 70.
- **Search:** regenerated, 5,686 entries.
- **Public scan:** 0 hits; 0 bad links.
- **The packet's 21 old-output markers:** all gone from the operations' places.
  - One generic marker, "A sequence ", still occurs in atlas claim No. 650. That text is unrelated, comes from
    `atlas.json` and is unchanged since v11 (`BODY-MARKERS-NOTE.json`).
- **The frontier supplement:** still exact.
- **Compared with v11:**
  - `index.html` changed only in Chapters 1, 4, 5 and 12;
  - `reference.html` changed only in the orientation, terms, glossary and results index;
  - `atlas.html` changed only in the atlas section.

## Native captures this needs (root), then QA (root launches)

- **Width:** 1280 unless stated.
- **Measure page:** `measure-release-v12.html` is in `/tmp/qh-ega-root-native-20261117/site/`. It works when a server
  serves that folder.

| # | Page and anchor | Shows |
|---|---|---|
| B1 | `index.html#from-products-to-local-operations` | Chapter 1, the factorization paragraph (BODY-CH01-FACTOR) |
| B2 | `index.html#ch04`, then `#lie-and-operator-product` and `#ordered-cut-geometry` | Chapter 4: the opening, the BD comparison, words, the two carriers and the transition |
| B3 | `index.html#ch05-ordered-cuts-give-a-finite-geometric-bar-construction`, then `#ch05-the-support-remembers-which-cuts-were-allowed` | Chapter 5: the word category, the duality theorem, the definition, the supported algebra and the atlas support |
| B4 | `index.html#ch12-associative-products-on-configurations`, at 1280 and at 375 | Chapter 12: the carriers, definition, vacuum and the displayed BD map (a long display at phone width) |
| B5 | `reference.html#orientation`, `#results-index`, `#glossary`, `#terms` | The rebuilt orientation paragraph, the results and glossary copies, and the two tracker terms |
| B6 | `atlas.html#atlas` | The atlas introduction |

Still pending from before:
- the title page and Chapter 1 head, at 1280 and 375 (the v11 opening);
- items 5 to 8 of `CAPTURE-RELAY-FOR-ROOT-v10.md`: the Gaussian figure, the atlas repair, the supplement and its
  contents entry.

## Not done here

- **Native capture and QA judgment:** root's. The receipt requires visual verification before publication.
- **The reader projection:** waits for its own independent PASS receipt and seal.
- **Publication, push or deployment:** none.
