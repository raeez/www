# Local preview bundle: release v11, the first-opening correction

From the website owner, the foundation session 67e78388 on claude4. Written 2026-11-17 at about 13:20Z (20:20 WIB).

**This is a local preview, not cleared and not published.** The machine-readable record is `RELEASE-CANDIDATE-v11.json`.

## The bundle (frozen, read-only)

Folder: `/tmp/qh-ega-root-native-20261117/site/release-v11/`. Serve the folder as the site root; the four files link to
each other by these names.

| File | sha256 | Bytes |
|---|---|---|
| `index.html` | `059de6ac6aa9a587748efa1b7eb09d6b064294ffe06b70bfb18a0c4fc24399a1` | 3,198,021 |
| `reference.html` | `41915202af042eb6bbb7453beae5d65bfa317133f6fd56fa238c826735bed95f` | 3,851,109 |
| `atlas.html` | `9c17cc2b287c260da0c831f9a28cae5fecebe1e8788d2ec2eef9b6a81b668f38` | 9,815,505 |
| `reader-index.js` | `1663cc4b0f2c97b394ed66fd108e279b10841d28d153e643372446bfe93e7253` | 4,764,347 |

Root's servers were not touched. At 13:1xZ, port 8791 served an earlier book at `/` (canonical `momentum-sez…`), and
port 8792 served the former tracker.

## What changed from v10

**The exact packet, and nothing else:**
- the seal `aa6f0273…`, with its receipt `PASS_SOURCE_FIDELITY`;
- the receipt's scope: three source operations;
- installed by exact replacement with hash guards (`first-opening-v11/INSTALL-first-opening.json`).

**The title page:**
- The audience line is gone.
- The introduction now opens: "The objects studied here are associative chiral algebras of configuration complexes.
  They are not Beilinson–Drinfeld chiral algebras. …".
- The boundary paragraph follows unchanged, and the paragraph "This work develops that question through associative
  chiral algebras …" is removed.

**Chapter 1:** its paragraph on associative chiral algebras now reads "The programme’s **associative chiral algebras are
not Beilinson–Drinfeld chiral algebras**. …", the packet's text.

**The address:** each page's canonical link and new `og:url` are on `https://research.momentum.inc/quantum-holography/`
(the book; `…/reference.html`; `…/atlas.html`).

**Everywhere else:** each page is identical to v10 outside the title page, Chapter 1, the canonical link and `og:url`
(`release-v11/CONFINEMENT.txt`).

## Checks on these exact files (logs in `release-v11/`)

- **The packet's four HTML guards:** all pass; no audience element remains.
- **Search, regenerated:** the old Chapter 1 text appears 0 times (v10: 1) and the new text once; the old audience
  line and the removed paragraph appear 0 times.
- **Build:** PASS; 17,661 formulas, 0 TeX errors.
- **Interaction's suites:** split checks 12 of 12; page checks 19 of 19; reader tests 70 of 70.
- **Public scan:** 0 hits; 0 bad links.
- **The frontier supplement:** still exact.

## Not done, and what it needs

- **The view changes need native capture and judgment by QA df53cc5e, launched by root:**
  - the title page at 1280 (as item 4);
  - Chapter 1's head and opening at 375 (item 3), plus the changed paragraph at 1280.
- **v10's pending items** still need their first capture: 5 and 6, the atlas repair; 7 and 8, the supplement and its
  contents entry (`CAPTURE-RELAY-FOR-ROOT-v10.md`).
- **The measure harness:** the harness pages `measure-release-v11.html` and `check-release-v11.html` are in
  `/tmp/qh-ega-root-native-20261117/site/`. They load `release-v11/…` relative to that folder, so they work only when a
  server serves that folder.
- **The older publication checkout:** `/Users/raeez/www-worktrees/2026-11-17-qh-publication` still holds the v10 files,
  with the old canonical address and no commits. It was left untouched, since root publishes through
  research.momentum.inc.
- **Later corrections:** the remaining object, BD and source corrections and the reader projection come later, as
  successors, once they are independently checked.
