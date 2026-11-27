reader-delta5: a section or chapter result shows its opening sentence, over reader-delta3 (QA note S5, release v8).

reader.js 40ed4eb4... (delta3) -> f3e45fbb616ae5b86aafa4e89e4e4dedba8eb519ec1ee490639fb92c06018c64
tests     708ef3dd... (delta3) -> 2535d0405a35e884673190b612ec7b8889c4c859cf7db0fc189e4b4bcbd6ac01
Install: sh GUARD-READER-DELTA5.sh <tree> (or patch -p1 with the two patches). No index rebuild is needed: snippets are drawn when results are shown.

Change: the snippet of a section or chapter result was its first paragraph alone, which can be a fragment ('Now take' before a display formula). It is now the place's opening as a reader meets it: the first paragraph, continued through the display formula and paragraph after it while the first sentence runs on (a sentence may end inside its formula), at most three blocks, formulae kept. Release v9's 6.5 section now shows 'Now take g = sl3(C), kappa(x,y) = Tr(xy), s in C minus Q, B = Y_{-s}.' with its formula.
Test harness: history steps now wait for the address to change (a timing flake seen once).
No other change: delta3's scopes, names, kinds, addresses and units stay as they were.

Checks: reader tests 71 of 71 (twice); mutations 22 of 22 caught; on a copy of release v9 (which ships delta3) with delta5 in all three pages: split checks 12 of 12, page checks 19 of 19.
Review: lead-verified only; no browser.
