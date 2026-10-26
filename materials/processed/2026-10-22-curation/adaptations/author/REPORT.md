# Author-essay conversion record

22 October 2026. Scope: two accepted author essays for the existing personal-site pipeline. The publication lane owns rendering, metadata integration, redirects, indexes, commits, and publication. This record and its companion JSON evidence remain unstaged.

## Sources and full reading

Both frozen HTML article bodies were read completely. The current research-worktree copies matched their frozen bytes. The complete 22 October 2026 *Corpus disposition and publication roles* and *Author essays and site placement* assessments were read. Those assessments govern placement here, not the truth of empirical claims.

Frozen source directory:

`/Users/raeez/centcom-worktrees/www-curation-20261022-publication/materials/raw/2026-10-22-author-essay-sources/`

Current comparison directory:

`/Users/raeez/momentum-research-worktrees/curation-20261022-publication/`

The accepted argument, citations, examples, qualifications, and paragraph ordering did not require a further prose revision. The conversion fixes destination-relative links, removes source author boilerplate, and places title information in the site's existing metadata arrangement. No experience or factual claim was added.

## Two Harnesses and a Limit

- Frozen source: `two-harnesses-and-a-limit.html`.
- Frozen and current source SHA-256: `195d4b26b97cb7f51dff2b6b6c3909162fefc32473a38dd747ad509abb72e09b`.
- Output: `content/author-essays/two-harnesses-and-a-limit.md`.
- Final Markdown SHA-256: `1d6097a65f19c297de0fbf47f69352d34e36f778c754f401bcf1c7468f825db9`.

The essay distinguishes safeguards around an agent from checks on the institutional changes it can make. Its reader payoff is the connection between AI safety, operator accountability, and institutional neutrality. The operator must face the checks that bind other participants.

The diagnosis was limited: the source byline duplicates site metadata, and two research-relative URLs would point to the wrong host after relocation. The title remains unchanged. The 17 substantive paragraphs remain exact, including punctuation and emphasis.

Changes:

1. Remove the source-only Raeez Lorgat byline from the body. Preserve authorship through parent-owned site metadata.
2. Add the single Markdown H1, **Two Harnesses and a Limit**.
3. Convert paragraph markup and link markup to Markdown.
4. Expand `/papers/programmable-institutions.html` and `/papers/sovereign-jurisdiction-network.html` to their existing absolute `https://research.momentum.inc/` URLs. Link labels remain exact.

The date is **August 2026**, established by the source's `article-meta` at line 564. Neither the frozen file nor its structured metadata establishes a publication day. No day should be inferred from file or commit timestamps.

Metadata proposal:

- Title: **Two Harnesses and a Limit**.
- Subtitle: **How institutional rules constrain agents and their operators**.
- Description: **How institutional rules can constrain AI agents and their operators, connecting safety with institutional neutrality.**
- Canonical author destination: `https://raeez.com/two-harnesses-and-a-limit.html`.

Preserved qualifications and source anchors:

- Line 572: the check must be sound for its invariant.
- Lines 577 and 582–585: institutional coverage, the complementary role of permission checks, actions outside the checked environment, human judgment, and the quality of the law itself.
- Lines 578–581: the operator's power, no administrative bypass, checked and recorded prospective rule changes, local law, and receiving-jurisdiction verification. The source calls the final prevention claim a design goal.

The two canonical paper URLs exist in the current research tree, and each destination's canonical metadata matches its URL. This conversion does not add a claim that these papers establish deployment, empirical safety, or complete coverage.

## Competitive Topologies and the Monopoly Problem

- Frozen source: `competitive-topologies.html`.
- Frozen and current source SHA-256: `9270cdc8fdc1a170262d10b694a0e17ccf38f8718b5e1aa31a70d9564c275411`.
- Output: `content/author-essays/competitive-topologies.md`.
- Final Markdown SHA-256: `5fe362719d298452e1bb1c4867e0cd91fc0fbe306bc7267d2a025518a00a0228`.

The essay argues that credible exit can improve institutional accountability alongside voice. It examines who can leave, who bears the costs, which public functions can be separated, and which require shared standards. That political argument remains distinct from formal work on recognition or accession.

The diagnosis was limited: the source repeats its full title inside the body and its header, repeats authorship, and combines title and explanatory subtitle into one long heading. The existing expanded argument already contains the objections and domain limits identified by the site-placement matrix. It remains intact.

Changes:

1. Use the single H1 **Competitive Topologies and the Monopoly Problem**. The original title was **Competitive Topologies & The Monopoly Problem: Why Democratic Institutions Need a Theory of Competition**. The final clause becomes the proposed site subtitle below; the ampersand becomes “and.”
2. Remove the duplicate source-body H1 and the source-only author byline.
3. Retain the bold response identifier: **A Response to Eric Schmidt and Andrew Sorota's "This Is No Way to Rule a Country"**.
4. Convert paragraphs and emphasis to Markdown. Remove redundant bold markup around H2 text while retaining each heading.
5. Preserve the source's runtime `section-1` through `section-13` destinations with Pandoc heading attributes. The research `paper.js` creates these IDs in document order when a heading has no ID. No HTML is required.

The date is **November 2025**, established by the source's `article-meta` at line 565 and consistent with the dated site-placement assessment. The source supports month precision only. The expanded edition keeps this identity; the migration is not a new publication date.

Metadata proposal:

- Title: **Competitive Topologies and the Monopoly Problem**.
- Subtitle: **Why democratic institutions need a theory of competition**.
- Description: **How exit, voice, and competition between jurisdictions can improve institutional accountability.**
- Canonical author destination: `https://raeez.com/competitive-topologies.html`.

All 58 paragraphs, including the response identifier, all 13 H2 sections, all 47 emphasis spans, and the retained bold response span match the source. There are no body hyperlinks, figures, equations, tables, or source-authored HTML IDs. Literary and research citations remain in their existing text and emphasis.

The following source passages retain the matrix's substantive qualifications:

- Lines 574–575 and 594–597: definitions, Hirschman's lazy-monopoly objection, unequal exit costs, continuing public-good contributions, and the mobile legal entity distinction.
- Lines 582–587 and 591: Tiebout's hypotheses, Bewley's objection, charter-choice externalities, shared floors, SEZ central control, and functional separability.
- Lines 600–602 and 629–631: liquid democracy, quadratic voting, Pol.is, pilot evidence, concentration, collusion, and participation limits.
- Lines 606–608 and 633–635: centralized override, rule comparison and movement costs, irreversible policy consequences, and the bounded case for faster administration.
- Lines 610–613: nominal and effective control, operating authority, legal wrappers, and their limited purposes.
- Lines 615–621: prediction-market conditions, futarchy's open questions, and the distinction between cryptographic primitives and the identity layer.
- Lines 624–626 and 640: the four functional-jurisdiction failure modes, appropriate domains, shared standards, and four open problems.

No formal-paper link was inserted as proof of the political or empirical argument. The accepted source contained none. The research URL must continue to identify this expanded essay after the author-site move, including its `#section-N` destinations.

## Verification and remaining integration

`conversion-checks.json` records hashes, block counts, and exact normalized Pandoc AST equality after the declared changes. The normalization ignores heading IDs only; all text, inline emphasis, citations, links, and block order agree. A separate read-only comparison reached the same result. All Markdown was then read completely.

`public-source-checks.json` records the source-path scan and canonical-link checks. No private repository path appears. The only process-pattern match is Lessig's cited book title *Code v2*, a legitimate third-party title. The Markdown contains no raw HTML. Metadata proposals are in `metadata-proposals.json`.

The conversion used installed Pandoc 3.9 and Python's standard library. An initially attempted optional parser was unavailable; no dependency was installed. No browser inspection or browser workaround was used. No publication HTML, styles, templates, index, feed, or compiler file changed.

The parent must render the two sources through the existing template, apply the proposed metadata, preserve the month dates and legacy fragment destinations, and complete its normal visual checks. The final title/subtitle split must appear together so the original explanatory title clause is retained. Source preservation does not constitute new empirical or mathematical verification.
