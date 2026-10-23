# Source provenance

The seven accessible papers were received as part of *Research on Institutions, Claims, and Markets*, dated 8 September 2026. Their Markdown, TeX, and reference metadata were copied unchanged into `materials/raw/2026-09-09-accessible-papers/` before website conversion.

The retained snapshot includes the 3 October 2026 additions to *Claims and Continuing Obligations*, *Prices, Information, and Clearing Risk*, and *Title, Remedies, and Institutional Change*. Those additions cover venue registration and fees, settlement timing and funding, and title accounts and reconciliation. The snapshot present on 22 October 2026 is the basis for the maintained sources.

`references/reader-paper-snapshot.json` records the SHA-256 digest of every retained Markdown, TeX, and reference file. These archived files remain unchanged. Maintained editorial copies live in `content/reader-papers/`; the Markdown and TeX pairs carry the same prose and retain their respective mathematics and citation syntax.

`compiler/reader-papers.json` records the maintained Markdown and TeX SHA-256 digests, titles, and reading order. `compiler/build-reader-papers.py` checks the archived and maintained digests before rendering through `compiler/template.html`. The title moves to the article header, mathematics becomes MathML, and verified bibliography destinations can be added without changing citation text. Website metadata, reading-sequence navigation, and the writing index are presentation material.

The website publishes HTML. No PDF is imported or published by this build. Source copies and build controls are excluded from GitHub Pages.

The two fifth-level subheads in *Prices, Information, and Clearing Risk* render as third-level HTML headings beneath their second-level sections.

## Original essays

The root HTML files are the maintained local essays. Six entries in `compiler/docs.config.js` retain their historical Google Docs identifiers and dates. Their `localHtml` paths select the maintained root files for local builds. A build copies those complete files into `compiler/dist/` without fetching their historical sources. The current contents and modification dates of those Google Docs have not been verified.

For ten original essays, the 22 October 2026 revision preserves the historical assertions, technical content, qualifications, citations and embedded assets while revising prose and composition. It does not establish current deployment status or verify dated empirical assertions. Conventional metadata retains publication dates; document-process version labels are removed. The Atom feed retains its existing fourteen-entry set and publication metadata; its seven full-article bodies are synchronized from maintained local pages, and its seven reader summaries remain unchanged.


## Reader-source reconciliation

The maintained pairs retain the October snapshot additions. A comparison with `momentum-research` baseline `0980d90a3d4a9ca9a455d8ab4ebbb595390607db` identified a six-sentence observation-law qualification present in its Programs source but absent from the website snapshot. It was restored after comparison with current *Institutional Linking and Realization*, §25. The exact source and insertion are recorded in `materials/processed/2026-10-22-editorial/source-scope-reconciliation.json`.

A contextual citation audit against all fifteen current formal papers and the linking supplement updated dependent section and result numbers without changing theorem claims. `materials/processed/2026-10-22-editorial/citation-locator-updates.json` records exact substitutions and compiled dependency hashes. Final source hashes are also retained in `frozen-reader-source-hashes.json` in that directory. Bibliographic dates remain the source dates.

## SEZ source custody and correction

The original `sez-in-a-box.html` at website baseline `a0d011c46811837a7f5fb1d1aa60cd457b68dd00` is preserved byte-for-byte as `materials/raw/2026-10-22-sez-source-custody/sez-in-a-box.html`: 694,004 bytes, SHA-256 `1eef9d9238627a7fe03e4f5a69dcf00a084b22e596c318a969c95beba9548a84`.

The named centcom source *Economic Zones in a Box (WIP 0.06) — book ingest + referee critique*, dated 12 June 2026, identifies invented pilot and outcome assertions in this exact October 2025 manuscript. The authorized reader correction removes that specified evidence layer, revises the conceptual architecture under current product and authority conditions, and keeps the complete historical Part I with the bounded corrections documented in its evidence record. It does not import the critique's June operating figures or treat that dated record as proof of current business status.

The current reader edition retains 15 October 2025 as its publication date and displays an update date of 22 October 2026. Its twenty-two-thousand-word argument distinguishes proposed arrangements, approved work and observed results. Original Part I blocks 0189–0466 map to final blocks 0041–0281. Appendices containing operator templates and negotiation material remain in raw custody; no new handbook or executed instrument is created.

`materials/processed/2026-10-22-editorial/sez/` holds the exact Part I before/after map, whole-text diff, source corrections, removal bases, restorations under the bounded history rule, final readable text, and checks. Its copied handoff identifies paths in the preserved editorial worktree; `evidence-manifest.json` pins the copied records. Unverified historical anecdotes, absolutes and allegations remain identified as unresolved in the internal report. Their retention is not historical verification.

## Local derivatives and layout

`materials/processed/2026-10-22-editorial/responsive-repairs.json` records three bounded CSS repairs imported from inspected shared-page copies: long-line wrapping in Archai, contained narrow tables in LICC Blueprint, and image bounds in Prefab. Non-CSS bytes remain unchanged.

The ignored `compiler/dist/momentum-monograph.html` is a local derivative of the separately maintained monograph. Its baseline text and DOM agree with the maintained source apart from cosmetic export classes and Google redirect parameters. The rebuilt derivative preserves the local URL strings and image payloads; `materials/processed/2026-10-22-editorial/monograph-derivative.json` records exact source/output hashes. The shared checkout's existing derivative was not changed.
