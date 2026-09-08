# Accessible-paper HTML verification

Date: 9 September 2026.

The seven papers listed in `compiler/reader-papers.json` render as complete root-level HTML articles. The article template and the existing writing-page stylesheet are unchanged. The new stylesheet covers native MathML, scrollable tables, definition lists, and reading-sequence navigation. No PDF is part of this publication.

## Source and content checks

- All 21 retained Markdown, TeX, and reference-metadata files match the supplied files byte-for-byte. The build checks the seven Markdown SHA-256 digests.
- Independent source/HTML structure comparison preserves 431 paragraphs, three tables, definition lists, bibliography entries, and heading, link, emphasis, and code text in order.
- All 153 formulas retain their exact TeX annotations and inline/display modes. MathML parses without errors.
- The two fifth-level subheads in the price paper render as third-level headings. All seven pages have one first-level heading and no skipped heading levels.
- Local anchors and reading-sequence links resolve. Identifiers are unique. Structured-data titles and descriptions match the source manifest.
- The writing page, Atom feed, sitemap, and text index each contain all seven canonical HTML URLs. Existing index entries are retained.
- The source/publication scan found no private locators, prohibited attribution, PDF links, or unresolved template tokens in the new paper sources and article pages.

## Layout and syntax checks

All seven articles and the writing index passed at 1400, 1024, 768, 480, and 375 pixels: loaded fonts, visible text, title assertions, text-density thresholds, and no document-wide horizontal overflow. Screenshots cover desktop and narrow article headers, displayed equations, and tables. Visual inspection confirmed readable text, equations, and tables in the existing visual system. `layout-results.json` records all 40 viewport checks; PNG files retain the rendered views.

`python3 compiler/build-reader-papers.py --check` and `git diff --check` pass. `xmllint --huge --noout feed.xml sitemap.xml` passes. The default XML parser limit was insufficient for the pre-existing large embedded content in the feed; the large-input parse completed successfully without changing that content.

## Scope boundary

This is source-conversion and publication verification, not a mathematical proof review. Bibliography text is preserved without new outbound destinations: several cited technical sections are newer than their public HTML editions, and *Institutional Linking and Realization* has no confirmed public HTML destination. That technical-publication dependency remains separate from these seven source-faithful articles. Source copies, build controls, and these verification records are excluded from the website.
