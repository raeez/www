# Reader metadata rebinding

The staged reader manifest is `../reader-data/manifest.json`, SHA-256 `0e8b91d1d79e71775ffce560cdf2c939d0e58267cfa1eb4452b5902cca67161b`, 449,332 bytes. Its predecessor is the direct-v15 deployed batch's authored reader-data manifest, SHA-256 `4816c9017331864999cf4948d471c8e17b5e1110963d5c338e6be9c5579999dc`. The source file `../introduction.json` has SHA-256 `0bd3a80cc3c58997f956821089c94cea1cc342f1a0e6f899cafad3f3d328834b`. Its complete `introduction` field is reproduced exactly.

## Source selections

The chapter authors' receipts pin all 18 Markdown files. The final chapter 7 and 10 hashes incorporate the hypotheses on the pointed action and the finite-tree sewing, respectively. Per-chapter source digests and the offsets of every index quotation appear in `bindings.json`.

- All 85 definitions and 70 result excerpts match exactly one passage in the corresponding final source. Nineteen definitions and thirteen old result excerpts needed reselection. The three-pole result had retained its old first paragraph, and the updated excerpt now includes the balanced evaluation map in the following paragraph. Thus 33 excerpts changed and 122 were carried verbatim. Both the three-pole and four-pole entries include the factorwise bars and the displayed evaluation.
- All 155 records expose `source_range` as half-open Unicode code-point offsets. This is the previous convention for definitions. Result records gain the same optional field. The receipt also gives half-open UTF-8 byte offsets, inclusive line numbers and the digest of the quoted UTF-8 bytes.
- The 249 section records follow the actual source headings. The existing chapter 4 heading `ch04-irregular-collision` was absent from the deployed metadata. The deployed `term-consecutive-cut` offsets were already stale in v15. Both are corrected from the text. The reference occurrence counts were recalculated from the chapter links.
- The 18 chapter titles and order, five parts, three routes, formal result names/statuses, term labels, numbered references, figure and diagram declarations, and diagram node destinations carry forward from v15. Chapter summaries now identify the mathematical objects introduced at the respective entry points. The 13 diagram declarations agree with the separate deployed diagram-records file.

## Native check

The v15 monograph compiler assembled the final source and manifest in memory. Its 1,099 reader IDs and 99 equation destinations agree with the v15 output. The final run resolved 308 cross-reference occurrences and 94 diagram definition links, placed all 18 figures and diagrams, and rendered 7,918 math jobs with zero compiler warnings, compiler problems or MathML errors. `native.json` contains the machine-readable result. The host's integrated site build is a separate check.

To reproduce within the staged filesystem, run the following from this directory.

```sh
python3 -B bind.py --check
python3 -B check_native.py --check
```

The rebinder uses the original chapter section, span and reference counting routines. The frozen inputs, explicit edited-passage selectors and new summaries are in `selections_v16.py`. Running without `--check` regenerates only the assigned metadata and receipt outputs.
