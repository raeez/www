# Acknowledgement: the first-opening correction has priority (13:13Z, 17 November; 20:13 WIB)

From the website owner, the foundation session 67e78388 on claude4 (Opus 5.5, max).
- claude4's own usage report at 13:12:55Z: "Current week (Fable): 100% used", so zero Fable remains. The week across
  all models is 96% used.
- `CLAUDE_CONFIG_DIR` is `~/.claude4`, and no secure-storage override is set.

## Done

- **The final receipt:** `/tmp/qh-reader-object-revision-check-20261117/first-opening/RECEIPT.json`.
  - Its status is `PASS_SOURCE_FIDELITY`, and it is install-eligible with no repairs required.
  - Its subject seal is the packet's, `aa6f0273…`, and its seal verifies.
- **Installed as a mutable successor of v10's inputs:** the receipt's exact scope, the three operations.
  - OPEN-AUDIENCE and OPEN-FRONT, in the manifest. Integration held manifest `9493008a…`, not the packet's base
    `342bef12…`, but its two fields hashed to the packet's `old_sha256`. Only those two fields changed, and both now
    equal the packet's proposal.
  - OPEN-CH01, in Chapter 1, which is now byte-identical to the packet's proposed file.
- **v10's input files** are kept in `content-v10-inputs/`. v10 and every older release stay frozen.
- **Site base:** `page.json` `site` is now `https://research.momentum.inc/quantum-holography`, per root. Each page's
  canonical address and a new `og:url` follow it.
- **Release v11** (the next free number) is building now. When it is built, it is checked against:
  - the packet's four HTML guards;
  - the search index, where the old Chapter 1 text must be gone;
  - every release check;
  - a comparison with v10.
  The exact local preview bundle follows in `PREVIEW-v11.md`, beside this file.

## Kept as before

- Root's servers 8791 and 8792 are untouched.
- No new worker or child has been started. QA df53cc5e and its saved reviews are untouched, and root launches QA.
- There is no commit, push, remote change or send.
- The later object, BD and source corrections and the reader projection will be integrated as successors once they are
  independently checked.
