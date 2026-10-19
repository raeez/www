# Publication routes — 8 September 2026

- Authority: prepare and stage minimal existing-list links and metadata for the latest seven accessible and fifteen technical papers. The principal explicitly prohibits changes to design, layout, styles, components, templates, navigation, or page hierarchy. No commit, push, deploy, or shared checkout edits.
- Worktree: `/Users/raeez/centcom-worktrees/www-papers-publish-20260908`
- Branch: `agent/www-papers-publish-20260908`
- HEAD and origin/master: `03d5145bc3c3accd295c9030abcc43f83d50583c`
- Canonical collection: `https://research.momentum.inc/`. Article HTML and PDFs remain under `/collection/reader/papers/` and `/collection/technical/papers/`. No new collection entry page.
- Source: coordinated collection INDEX in the current accepted two-layer paper delivery.
- Existing staged writing redesign in a separate worktree is preserved. Current master owns the Etingof links and site design.

## Completed

- Read applicable repository, ecosystem, reader-copy, and browser instructions.
- Verified refs and inspected current writing navigation, machine indexes, feed generation, and unpublished overlap.
- Created isolated worktree through the required helper. Its prerequisite worktreeConfig setting was absent. Enabled it and completed the initially empty index using read-tree.
- Added exact accepted 7+15 titles, descriptions, canonical HTML and PDF routes to writing.html using only the existing Infrastructure list and its original li/year/content/subtitle markup. Added one collection link to the existing research homepage.
- Updated llms.txt, llms-full.txt, and sitemap timestamps. No biography or compiler changes.
- Verified diff whitespace, sitemap XML, public-source scan, and prohibited draft-language scan.
- Inspected unchanged feed: default XML parser hits its existing large CDATA limit; `xmllint --huge --noout feed.xml` passes. No new local article was created, so no synthetic Atom entry or compiler regeneration.
- Browser runtime could not select any browser. Required troubleshooting read and browser discovery returned an empty list. Desktop and narrow visual checks remain unperformed.
- Local preview is running at `http://127.0.0.1:8768/writing.html` under terminal session 52109.
- Source-to-route check: 7 accessible HTML, 15 technical HTML, 22 PDFs; all targets exist in the accepted source delivery.
- Removed all own initial presentation changes after the principal narrowed the publication boundary: no new CSS, intro, navigation, sections, list containers, details wrapper, or changed Mathematics heading remains.
- Exact preservation check: removing the 23 inserted listing entries yields the original body byte-for-byte. The complete style block is byte-identical to HEAD; no new CSS classes or disclosure elements exist. Original essays, navigation, headings, and Etingof links remain directly visible in original order.
- Earlier independent review accepted route/title/description matches and privacy. Fresh review requested for narrowed-scope diff; previous contrast finding concerns removed presentation code and is no longer applicable.
- Owned files remain writing.html, llms.txt, llms-full.txt, and sitemap.xml. Revised diff is 4 files, 188 insertions, 5 deletions, all links/list entries and metadata. HEAD and origin/master remain pinned above.

## Remaining

- Desktop and narrow visual verification needs a connected browser.
- Confirm narrowed-scope independent review and restage the four owned files.
- Accountable root integrates the staged changes. No commit, push, deployment, or shared checkout change has occurred.

## Next command

Review staged diff for integration, then open the live local preview when a supported browser is connected.
