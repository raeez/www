reader-delta3: the search's presentation on narrow screens (native QA image 05: S2, S3, S4), over reader-delta2a.

reader.js 9ed283cc... (delta2a) -> 40ed4eb4fa623bb765c5e2b5249e0445969742b03614e878fb626462a810a0c9
tests     c02d3060... (delta2)  -> 708ef3dd098fb7fe7845456ff9c46f8fbeabdac445ba616ab4528d2005aceac9
Install: sh GUARD-READER-DELTA3.sh <tree>  (or patch -p1 with the two .patch files), then rebuild reader-index.js with this reader.

S3: the scopes are hidden until there are results; then only All, the scope pressed and the scopes holding results show; arrows move among those shown.
S4: a reference part is named as the page names it (its bar link, else its contents link, else the map, else its heading): the scope chips, the result groups and the bar. 'Atlas and reference', 'Atlas'.
S2: every result names its kind (Section, Passage, Figure, Glossary entry, Atlas entry, Heading; environments keep their own label); a section or chapter shows its first paragraph as written; a result's section is drawn from its heading, formulae kept; a unit's title is read with a number set apart kept apart (short query words now match such titles).
Not results any more: blocks whose only words are links to places of the page (a chapter's own contents list: 127 entries and 17 link-only paragraphs in release-v4). Each of their link targets is a result; every address, theirs included, is exactly as in delta2a.
No scientific text, status, unit content or cross-page address changes. CSS untouched (the query field and bar are the website lead's).

Checks: reader tests 70 of 70; mutations 21 of 21 caught; on a copy of root's release-v4 with this reader in all three pages and the index rebuilt: split checks 12 of 12, page checks 19 of 19, 'four factors' 52 results with 5 scopes (All 52, Chapters 20, Index of results 2, Glossary 1, Atlas 29).
Review: lead-verified only.
