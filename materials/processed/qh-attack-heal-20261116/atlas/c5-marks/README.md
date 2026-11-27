# C5: one mark system (atlas lane, 17 November 2026, about 03:00 WIB)

**What changed.** The atlas no longer draws its own squares (■ ⊡ ⊟ □).
- **Every place a mark appears** now shows the page's mark for the status's page alias (PAGE_STATUS), drawn by the page through `ctx.mark`: ● checked, ◎ conditional, ○ open (Remaining), × refuted form (Scoped negative). That covers:
  - the claim links in the lists;
  - the group headings;
  - the key;
  - the status filters, which the script copies from the key;
  - the index table;
  - the claim chips;
  - each of the map's 955 nodes, where the page glyph sits inside the node with the page's colour class.
- **The key** loses the sentence and the second mark that translated squares into circles. It keeps "The four statuses are those of the whole page."
- **Unchanged:** status words (chosen by the stored code), every id, every hook and the colours. The atlas's tokens were already aliases of the page's `--st-*`.
- **When the page cannot draw a mark:** if the page has no mark for an alias, the build fails and names it. Without a page at all (a context with no `mark`), no mark is drawn and the word stands.

**Apply** (from the root of root's tree; changes atlas.py, atlas.css and tests/test_atlas.py only):

    python3 <this folder>/check_atlas_c5.py --before
    git apply <this folder>/atlas-c5-marks.patch      # 51fbf53d5a0121291ee91b73b2a021951063ec120497b74556127ec2ab4018bb
    python3 <this folder>/check_atlas_c5.py --after   # guard 0d0f7cec…; hashes.txt 91720bc9…

**Evidence (checks.txt).**
- **run_checks.sh on a copy of root's tree with these files: RESULT PASS.** The parts:
  - both builds pass the audit;
  - 54 atlas unit tests pass, none skipped;
  - the jsdom reader tasks pass;
  - completeness covers all 955 claims, 137 edges, 88 comparisons and 23 paths;
  - the gate scans pass.
- **The like-for-like comparison with root's installed atlas files:**
  - the same 3,742 ids;
  - the same status words and hook counts;
  - squares go from 5,155 to 0;
  - only the 62 words of the translating sentences are gone.
- **Not judged here:** the look of the marks at reading size. That is native QA's.

**For root (not atlas):** a copy of root's tree taken after about 03:00 failed its audit on foundation's diagram attribute. The finding: `FAIL version tag … (in data-context-key): "-v1" in …programme-context-v1…`. The attribute carries the author's context_key.
