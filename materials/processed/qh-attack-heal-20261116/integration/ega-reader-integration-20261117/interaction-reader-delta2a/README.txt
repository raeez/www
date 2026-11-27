reader-delta2a: comment-only successor of reader-delta2 (root request, 2026-11-17).
One comment line in reader.js names no file any more ('the companion index' in place of the index's file name).
No code, test, tool or behaviour changes; reader-delta2 stays frozen as it was.

Apply (from the tree's root):  patch -p1 < reader-delta2a/reader.js-delta2-to-delta2a.patch
Before: reader.js 826542e53b77bf06d023ec0e21b6c5a150faf224884ea7ca615194a03c4acb61 (reader-delta2)
After:  reader.js 9ed283cc50fe1f36f7fff0c6e7d664c58d2df6bd867563356a40295c1e059eed
Checks: node --check; no file name left in reader.js; reader tests 66 of 66 (tests unchanged, c02d3060...).
Review: lead-verified only (hold).
