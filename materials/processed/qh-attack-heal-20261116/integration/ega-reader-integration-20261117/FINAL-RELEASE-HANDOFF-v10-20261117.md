# Website release handoff: release v10

- **From:** the website owner, the foundation session 67e78388 on claude4. Written 2026-11-17 (UTC).
- **Records:** `RELEASE-CANDIDATE-v10.json`, `INSTALL-foundation-v7-supplement.json`, `release-v10/` (logs and proofs),
  `qa-continuity/CAPTURE-RELAY-FOR-ROOT-v10.md`, `qa-continuity/RESUME-MESSAGE-R4-v10-20261117.txt`.
- **Supersedes:** release v9. v9 was never captured, and it stays read-only as history, as do v8 and every earlier
  release.

## Status

**Candidate. Not cleared, so do not publish.**
- Every automated check passes.
- No native capture is possible until Chrome is available. Root's Chrome-ready question is still unanswered.
- QA has not yet seen items 5 to 8.

## Staged, uncommitted: `/Users/raeez/www-worktrees/2026-11-17-qh-publication` (no commits)

The staged files are byte-identical to `/tmp/qh-ega-root-native-20261117/site/release-v10/` (read-only).

| File | sha256 | Bytes |
|---|---|---|
| `index.html` | `962423514869e0373a9dfc286f4ffbf26fe74885836bb33705cb16ec72758f72` | 3,197,685 |
| `reference.html` | `77a5b6e44776a68eac73164dc8a634e349abdc85afede90f9b8a20404b1e59ef` | 3,851,012 |
| `atlas.html` | `214f544b2ccddc0616d26f82ba4bb5919920a01433c249ae2299abf021e43ff9` | 9,815,412 |
| `reader-index.js` | `3214a88455d8427050f54dbb7f95754cd0ce3f004ef0aa04b946657c67c00a2f` | 4,764,059 |
| `.nojekyll` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |

## What changed since v9: the frontier supplement, carried exactly

- **Source:** root's content handoff `WEBSITE-CONTENT-HANDOFF.json` (Astra at maximum effort; exact approved prose;
  `formal_adoption` false; `original_targets_closed` false), with `FRONTIER-DELTA.md` at sha256 `7e97fcdd…`.
- **Installed content:** the file is installed byte-identical as
  `content/quantum-holography-status/supplements/frontier-comparisons-20261117.md`. A registry,
  `supplements.json`, names its sha256, and the build refuses the file at any other bytes.
- **Design (foundation v7, a sealed successor):** patch `v7/patch/monograph-v6-to-v7.patch`, with its guard and freeze.
  v1 to v6 are untouched.
  - It is a reference part of its own, `#frontier-comparisons`, after "The remaining comparisons". It is also listed
    in the book's contents in that place.
  - It sits under the reference's own section head, with the kicker "Supplement". It takes **no part number**, so
    every existing part keeps its number.
  - The file's title is the heading, and its first line is set as the date, `<time datetime="2026-11-17">`.
  - The four sections are unnumbered, with ids from their titles.
  - The text is in the book's measure and paragraph rhythm, with formulae typeset as in the chapters.
  - No opening phrase is turned into a numbered result.
- **Exactness, proven on the built pages (`check_supplement.py`, ALL PASS on reference.html and the combined page):**
  - heading and date as in the file;
  - 4 of 4 sections;
  - **183 of 183 formulae with identical TeX, in order**;
  - **2,105 of 2,105 words, in order, none added**;
  - the contents entry in place;
  - no duplicate id.

## Checks on these exact files (logs in `release-v10/`)

- **Build:** PASS; 17,661 formulas (v9 plus the supplement's 183), 0 TeX errors.
- **Interaction's suites:** split checks 12 of 12; page checks 19 of 19; reader tests 70 of 70.
- **Search index:** 5,675 entries, the 57 new ones all the supplement's.
- **Public files:** 0 private or attribution hits; 21,465 links and map ids, 0 bad; only the 3 canonical links are
  external.

## Where it differs from what QA judged (`release-v10/CONFINEMENT.txt`, `COMPARE-v9-v10.json`)

- **The pages** changed only in the new part, the book's contents (one entry), the page map and the style block.
- **Of the 9 differing CSS rules,** 7 are scoped to the supplement. 2 are the math font, whose subset only grew (311 to
  313 characters, none removed, no width changed).
- **No existing search entry changed.**
- Together with v9's proof (`release-v9/CONFINEMENT.txt`), this means items 1 to 4 keep their v8 passes. Items 5 and 6
  still await their first capture.

## Next, in order

| Step | Who | What |
|---|---|---|
| 1 | root | When Chrome is available: the captures in `qa-continuity/CAPTURE-RELAY-FOR-ROOT-v10.md` (5-top, 5-middle, 5-bottom, 6a-map, 6b, 6c, 6d, 7a–7e, 8; pointer out of the frame), into `captures-release-v10/`, with `CAPTURE-RELAY.json` written last. |
| 2 | website owner | The watch on that manifest wakes this session. It verifies the captures and an account's capacity by its own usage report, then resumes the same QA session df53cc5e (whole history, 2,858 lines, from claude5) with `RESUME-MESSAGE-R4-v10-20261117.txt`. |
| 3 | QA | Judges items 5 to 8, says whether items 1 to 4 stand, and writes `HANDOFF-TO-WEBSITE-LEAD-v10-20261117.md` ending in its verdict line. |
| 4 | website owner | Returns the release decision. On "CLEAR", the staged v10 files are the release. Otherwise the findings are routed, and v11 is built with v10 kept. |
| 5 | root | Only after "CLEAR": re-check the five hashes above, commit as Raeez Lorgat with no model or tool credit, push, enable GitHub Pages for `main` at the root, and open `https://momentum-sez.github.io/quantum-holography/` once. |

If this session cannot run step 2, the command is in `FINAL-RELEASE-HANDOFF-v9-20261117.md`, section "Next", with
`RESUME-MESSAGE-R4-v10-20261117.txt` as the message.
