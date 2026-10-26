# Source provenance

The seven accessible papers were received as part of *Research on Institutions, Claims, and Markets*, dated 8 September 2026. Their Markdown, TeX, and reference metadata were copied unchanged into `materials/raw/2026-09-09-accessible-papers/` before website conversion.

The retained snapshot includes the 3 October 2026 additions to *Claims and Continuing Obligations*, *Prices, Information, and Clearing Risk*, and *Title, Remedies, and Institutional Change*. Those additions cover venue registration and fees, settlement timing and funding, and title accounts and reconciliation. The snapshot present on 22 October 2026 is the basis for the maintained sources.

`references/reader-paper-snapshot.json` records the SHA-256 digest of every retained Markdown, TeX, and reference file. These archived files remain unchanged. Maintained editorial copies live in `content/reader-papers/`; the Markdown and TeX pairs carry the same prose and retain their respective mathematics and citation syntax.

`compiler/reader-papers.json` records the maintained Markdown and TeX SHA-256 digests, titles, and reading order. `compiler/build-reader-papers.py` checks the archived and maintained digests before rendering through `compiler/template.html`. The title moves to the article header, mathematics becomes MathML, and verified bibliography destinations can be added without changing citation text. Website metadata, reading-sequence navigation, and the writing index are presentation material.

The website publishes HTML. No PDF is imported or published by this build. Source copies and build controls are excluded from GitHub Pages.

The two fifth-level subheads in *Prices, Information, and Clearing Risk* render as third-level HTML headings beneath their second-level sections.

## Original essays

The root HTML files are the maintained local essays. Five public entries in `compiler/docs.config.js` retain their historical Google Docs identifiers and dates. Their `localHtml` paths select the maintained root files for local builds. A build copies those complete files into `compiler/dist/` without fetching their historical sources. The current contents and modification dates of those Google Docs have not been verified.

For ten original essays, the 22 October 2026 revision preserves the historical assertions, technical content, qualifications, citations and embedded assets while revising prose and composition. It does not establish current deployment status or verify dated empirical assertions. Conventional metadata retains publication dates; document-process version labels are removed. The original fourteen-entry Atom feed is retained in the source custody described below. The public feed follows the later curation.


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


## Author editions and catalogue curation — 22 October 2026

Nine author editions are maintained in `content/author-essays/` and rendered at the website root. Their seven source notes and two source HTML essays were copied byte-for-byte from the accepted research publication checkout into `materials/raw/2026-10-22-author-essay-sources/` before adaptation. `materials/processed/2026-10-22-curation/source-custody.json` records the original paths and hashes. `compiler/author-essays.json` binds each maintained edition to its archived input, title, subtitle, and original month.

*Two Harnesses and a Limit* and *Competitive Topologies and the Monopoly Problem* preserve the accepted source body text. The seven institutional essays are reader adaptations aligned to the current formal sources. Their dated reports record retained mechanisms, concrete corrections, primary references, and unresolved construction requirements. The original research notes remain available at their research URLs. This publication does not certify technical absorption or replace a formal paper.

The visible dates retain November 2025, April 2026, or August 2026 as supported by the original pages. The seven adapted notes also identify the October 2026 revision. A generic research-build fallback of 2 April 2026 does not establish an exact original publication day; no such day is asserted in the new pages or feed. The nine new feed entries carry their actual editorial update timestamp and omit the optional publication timestamp.

The catalogue features eight essays, groups seven further institutional essays and four research guides, retains six dated project or reference pieces, and points to the research catalogue plus Lex and Op. The seven reader-source pairs and bodies are unchanged by this curation. Their catalogue and feed descriptions use plain statements; their original article subtitles remain part of the accepted reader edition. Mathematics and the existing visual system are unchanged. Six existing articles receive title, subtitle, date-label, and metadata adjustments with exact body preservation.

The public feed contains twenty-two entries: fifteen full articles and seven reader summaries. It removes LICC Blueprint and six related links to it, adds the nine author editions, and synchronizes the changed article metadata. The Moxie entry drops a 15 April 2025 publication timestamp belonging to the earlier IPOS identity; the current essay establishes May 2026 without an exact day. The complete pre-curation feed is preserved byte-for-byte at `materials/raw/2026-10-22-site-curation/feed.xml`.

The principal authorized retaining *LICC Blueprint* as private planning material. Its exact adopted edition is preserved in `materials/raw/2026-10-22-private-planning/licc-blueprint.html`, SHA-256 `583a5042b75b92790328325c7beca0b5e2c25993d2afbb7fc8cf25dfe6bbfa05`. The root file is unchanged from that edition but excluded from GitHub Pages, the public compiler, feed, and catalogue. This withdrawal does not erase its prior public availability.

`materials/processed/2026-10-22-curation/` records the final catalogue, source custody, metadata changes, focused final deletions, validation, and handoff. The build continues to use the exact existing article template and stylesheet.

## Writing navigation correction — 22 October 2026

The principal’s 22 October screenshot and instruction remove Beauty and /dev/finance inc. from the main Writing list because both are already in navigation. The screenshot is preserved at `materials/raw/2026-10-22-writing-navigation-correction/writing-before.png`, SHA-256 `3e8f9d2dcfef84e91c7538be1abaa046b51b64dd82114506c545cad60b986921`. The six remaining selected essays and all navigation links, article pages, feed entries, sitemap URLs, styles, and typography are retained. The corresponding Writing list in `llms.txt` follows the same correction.

The principal’s second 22 October screenshot identifies inconsistent chronological order and title/category choices across the Writing page. It is preserved at `materials/raw/2026-10-22-writing-navigation-correction/composition-before.png`, SHA-256 `8a116c263fbc4a96b2d818c33ed1c1307228dfa779553c4ebfc9fd830cd977de`. The requested correction governs the entire catalogue composition, titles, descriptions, and chronology.

The corrected catalogue groups work by subject: Institutions and law; Computation and AI; Claims and markets; Built environment; Science; Mathematics. Entries descend by original year, with known months informing order and conceptual order for date ties. September 2026 reader articles precede April 2026 author notes and the January 2026 institutions essay. The shared formal-paper catalogue is linked once after the lists. `Programmable Institutions` retains its actual title without the added editorial suffix. Project names remain intact, with descriptions stating their subjects. Conflicting month labels in Smart Buildings (September wrapper versus October body) and LICC (December wrapper versus July byline) do not establish exact publication order; no finer dates are asserted in this catalogue.

The zone-network essay sits with institutions and law because its central subject is cross-border institutional recognition. The built-environment group contains buildings, construction, and land. Archai likewise has differing month labels (July wrapper and June manuscript title page); the catalogue retains only its established year. The LLMS catalogue also lists both Mathematics references.

## LICC institutional identity — 22 October 2026

The principal states that LICC is an institution he is founding and rejects its placement under Science. The catalogue now identifies the LICC and Sensoria pages as institutional projects. LICC uses its full name, The Laboratory for Incentivization, Coordination and Cooperation. Its page description follows its own institutional definition. The wrapper retains the established year 2025 and removes the added proposal label and disputed December precision. This correction changes catalogue and header metadata, with the institutional document and visual design preserved.
