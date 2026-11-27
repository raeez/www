# Atlas lane: integration handoff for root

## State

- **Frozen.** The final files are listed below with their sha256. There is a guarded patch that only creates files.
- **Synthetic fixture.** Every check passes on it, in composed/c29-fixture (jsdom 23 pass, 0 skipped).
- **The 11:20 atlas** (inputs/layout-snapshot-1120: 9 domains, 503 claims, 53 edges, 58 comparisons, 18 paths) is
  only a review and layout baseline. It is not the final tracker content, and none of its text was edited.
  - On it, every check of the atlas's own behaviour passes.
  - The page audit rejects it for content findings, which belong to the content owner (listed below).
- **The final content payload has not yet been rendered.** Root composes it and runs the checks below.
- **Not ready in the principal's sense: no page image has been judged.**
  - Visual, wide and narrow layout, print (A4, Letter), light and dark, reduced motion and forced colours were not
    observed, under root's restriction.
  - The headless results in browser-dev/ predate the restriction. They are historical and are not accepted
    visual QA.

## Files to integrate (this lane's only production and test files)

| Path | sha256 | Bytes |
|---|---|---|
| compiler/quantum-holography-status/atlas.py | 3c9ba4d290f6971ebb79b3e08141191acecca128bf764bf2f4b17e76cffedcb6 | 62892 |
| compiler/quantum-holography-status/atlas.css | 5cb1f925f6f5b22fb9d3ceb5ed6d2c4d8fa412ec12c3c7bf1fc9eac39e495037 | 36315 |
| compiler/quantum-holography-status/atlas.js | 672246e70631b8cef81767576b153aa75604d3bbc6e5171eeff52efecca4d33c | 41279 |
| compiler/quantum-holography-status/tests/test_atlas.py | c8177f915abab8582d6bb30898ceda6c5d478fdbe280f67864deead89a6a1c47 | 35602 |
| compiler/quantum-holography-status/tests/atlas.test.cjs | 77fcd4cff28a36bb158bd3999fb6f8f6c50c2a0a648755b455b0ac933ebeb188 | 32197 |
| compiler/quantum-holography-status/tests/fixtures/atlas-synthetic.json | 2a5f0c7bc84e66832d6bb48edea0570ff8f28b6d049d6c16388bde4b4b6f9d32 | 10171 |

- All six are new files, absent at the baseline.
- The fixture is synthetic test data and must never be placed in content/.
- Not for commit: everything in this lane folder. That includes browser-dev/, which holds a 163 MB Chrome profile
  left by the stopped headless run.

## Apply, with the guard

    python3 <lane>/integration/check_atlas_files.py --before      # "the six atlas paths are free: apply the patch"
    git apply <lane>/integration/atlas-files.patch                 # sha256 c540a08da69750e00682c55b450d65108198d1b0292d9765385da783e8fc7740
    python3 <lane>/integration/check_atlas_files.py --after       # "all six atlas files as expected"

- check_atlas_files.py has sha256 742583541cc16555e910c65bbb44a1dfab93ad1e5063ed6a758cadfbb97e815a.
- If the files are already there, --before says not to apply again.
- Tested on a fresh repository holding only the 13 baseline files: --before, git apply, --after and a refused second
  apply.

**Retained baseline pins.** In this worktree the 13 shared tracker files are byte-identical to BASELINE.json:
`check_atlas_files.py --after --baseline <lane>/BASELINE.json` prints "baseline pins checked: 13". In an integrated
tree the foundation, interaction and content files differ by design, so --baseline applies only to this worktree.

## A separate delta for a tree that already holds the c24 set (status language, after root's intake of d0623e3b)

    python3 <lane>/integration/sets/check_atlas_delta.c24-c29.py --before    # "before: the c24 set as expected"
    git apply <lane>/integration/sets/atlas-delta.c24-c29.patch              # sha256 99a5b68015c7eef2adcec7f119f62f83eb228737592019a7366dab54c855357e
    python3 <lane>/integration/sets/check_atlas_delta.c24-c29.py --after     # "after: the c29 set as expected"

- The guard check_atlas_delta.c24-c29.py has sha256 de8c6a7bed9eaff9f93ee7c3f8c883e0875ca962dd4787e74da62ee84ee1e308.
- It was tested on a fresh tree holding the baseline plus the c24 patch: before, apply, after, and then the full guard.
- The delta changes five files; the fixture is unchanged:
  - every claim is offered to the page search with its page status;
  - status words are chosen by the stored code;
  - the per-record labels are no longer shown (card, index, key, filter);
  - the key shows the page's mark beside each of the four statuses;
  - a page that cannot show a mark gives a named finding;
  - the page colours the mark itself;
  - the tests are updated.
- The immutable sets are in integration/sets/: atlas-files.c24.patch (d0623e3b), atlas-files.c25.patch,
  atlas-files.c29.patch and their guards.

## The status-language ruling (content owner; root's message of 16 Nov), as presented by the atlas

- **Source.** STATUS-LANGUAGE-RULING.md (d6b665de...) and STATUS-LANGUAGE-PATCH.json (6b7a84b8...), read whole. The
  presentation is implemented in the atlas files only; no content, code, ID, hypothesis or classification changed.
- **Words.** The visible word is chosen by the stored code: Established, Conditional, Remaining, Scoped negative.
  - The per-record status.label strings are display aliases. They are kept and checked but shown nowhere: not on
    the card chip, the index, the key or the filter.
- **Aliases** (atlas.PAGE_STATUS): checked to checked, conditional to conditional, remaining to open, scoped_negative
  to refuted form.
  - Every claim carries data-qh-unit-status with its alias, so the page's status filters keep it and its search
    result shows the page's word.
  - On the 11:20-to-13:50 preview, by page status: checked 452, conditional 79, open 58, refuted form 125.
- **Colours.** The page's legacy semantic tokens through the aliases (--st-checked, --st-conditional, --st-open,
  --st-refuted-form); no new palette.
- **Legend.** Each atlas status shows the page's own mark for its alias ("Its mark on the statement cards and in the
  table:"). The key sentence says that the four statuses are those of the whole page.
- **Accessible names.** Marks are named by the group word, and the page mark in the key is aria-hidden. The atlas has
  no counters.
- **Glosses.** The atlas key glosses are still the atlas's own words. The content owner is composing the guarded
  /status_key prose. A context capability that hands the atlas that prose (for example ctx.status_key) would let the
  key show the same explanations.

## Bounded integration checks on root's current preview (13:50 snapshot, read-only copy in inputs/preview-2224)

- **The payload.** /tmp/programme-public-current-successor-20261116/composed: content.json ec6864c4..., essay.md
  798cca68..., atlas.json 9acebb93... (recomposed by its owner at 22:24 while c26 was being built from the earlier
  90a877c8...).
- **Snapshot.** The read-only copies and SHA256SUMS are in inputs/preview-2224, and composed/c29-preview was built
  from them.
- **Sibling files.** foundation status.py 493478e6, page.json 9bc4e43e; interaction status.js 10c37e5a.

| Check (checks-c29-preview.txt) | Result |
|---|---|
| build and audit | 21 findings, all the content owner's: 'E3' in the title of bare-e3-exterior-rigidity and in content.json, which a build without the atlas also rejects; 'T2' in centre-central-coefficient-strictification hypothesis 0, centre-actual-weight-two-bar title and statement, and centre-binary-logarithmic-comparison-criterion statement; 'R2' in the scope of edge current-native-dg-input-to-state-diagram; and comparison d-centre-base-change, whose questionId 'decisive-centre-base-change' names no question of the page |
| atlas unit tests through the mount | PASS: the atlas adds no failure to the page's own audit |
| jsdom reader tasks | 18 pass, 5 skipped for data reasons, 1 observed; the status-filtered page search passes |
| completeness | every domain (9), claim (714), edge (83), comparison (63, with 820 listed claims) and path (22) is drawn with its anchor; question links 6 of 7 (the unresolved id above) |
| stable anchors against the 11:20 draft | 0 atlas anchors lost; 0 page anchors outside the atlas lost |
| gate scans | PASS (the atlas's own words, attributes and files) |
| scale | the page is 9.0 MB without fonts; the atlas section is 6.7 MB of it; the map is 1100 x 1562 px |

**Content findings (listed, not failed), for the content owner.**
- 60 edges have their relation code as their label, so the sentence reads, for example, "construction_input",
  "proof_uses" or "uses_checked_input". Examples: native-edge-root-to-global and native-edge-marked-to-global.
- Several relation codes carry more than one label.
- 84 ids have parts shaped like internal identifiers (p1, r3, ...), and these appear in addresses.

**The 11:20 baseline findings against this candidate.**
- 'C1', 'N12', 'E1', 'R1', 'C0' and 'v4' no longer occur.
- The unresolved questionId remains.
- 'E3', 'T2' and 'R2' are new.

**Proportion (root's decision).**
- The atlas is now about three quarters of the page by bytes.
- At this scale, its placement after the principal results, and its claims in full as a print appendix, matter more
  than before (A3-RT-05).

## What the atlas needs from the other lanes

- **Foundation.** status.py must:
  - mount the atlas with render(data, AtlasContext);
  - not reserve the classes that ctx.rich emits (term, math-*).
  - The version checked is 66cc115902c6… (c21). With an older status.py that still reserves .term, the build names
    the class; then set atlas.py TERMS = False, at the cost of glossary definitions inside the atlas.
  - status.py 47b60701 (a mid-change state, caught in c20) checked for placeholders before formulae were filled, and
    failed every atlas formula.
- **Interaction.** status.js must isolate [data-atlas-mount], share the glossary card of a .term[data-term], and
  offer [data-qh-unit] search units. The version checked is 6f3b45e659c3… (c21).

## Remaining integration checks for the final payload (root's tree, exact)

1. Compose the six files with the foundation and interaction files. Put the final atlas.json at
   content/quantum-holography-status/atlas.json.
2. Run:

       REPRO=1 BASELINE_PAGE=<last published page.html> bash <lane>/integration/run_checks.sh <tree> <new out dir>

   - The out dir must be new: the script refuses one that is not empty, so no step can read a page of an earlier
     run. Nothing is written inside the tree.
   - Expected PASS lines:
     - build with fonts, build without fonts (the page audit, including the foundation reserved-class check);
     - the second build byte-identical;
     - atlas unit tests (through the foundation mount);
     - reader tasks in jsdom;
     - completeness;
     - gate scans.
   - Read three outputs as well:
     - every "atlas:" line in build-*.log: each unknown key, unresolved question id or statementRef is named;
     - completeness.log, for stable anchors (atlas anchors, and page anchors outside the atlas, that the earlier
       page had and this one lacks) and content findings;
     - jsdom.log, for every SKIP reason.
3. Run the same script on a tree whose atlas.json is the fixture. jsdom covers paths that depend on the data, and
   the 11:20 baseline lacks a statementRef, a dependency path and the test's glossary term.
4. **A payload with new fields.** If the payload adds fields (for example families), the build fails and names
   each unknown key. The draft still draws from the known fields only. The renderer then needs an explicit change
   from this lane; no field is ever dropped silently.
5. **Page content completeness is outside the atlas tools.** Foundation and quality check that every statement,
   family (#row-), question (#q-) and open group of content.json renders with its anchor.
6. **Visual checks once allowed.** View page images beside the best exemplars, at 1400, 1024, 768, 480 and 375 px,
   in light and dark, with reduced motion and forced colours, and in A4 and Letter print. Look in particular at:
   - **The first view:** the key, then the full-width map (13px numbers; domain columns; names above and below).
   - **Selecting a claim:** the pane at 1.618 : 1, the reader's place kept, the sheet below 1000px.
   - **The index:** the long index scrolling in its own box.
   - **Comparisons:** two by two, or four across.
   - **Print:** the map fitted with 13mm margins (numbers about 7pt), its bands, the formulae fitted by --fw, and
     every claim printed.
   - **The glossary card:** open from the pane and the sheet.

## Commands and results (this lane; c22-fixture and c22-baseline1120 share one sibling snapshot, foundation status.py ee0a349a and interaction status.js 9802c92e; c21 used 66cc1159 and 6f3b45e6; MANIFEST.json of each)

    python3 -B <lane>/integration/compose.py <name> [--atlas <atlas.json>] [--no-fonts]
    REPRO=1 bash <lane>/integration/run_checks.sh <lane>/composed/<name> <lane>/checks/<name> [atlas.json]

| Composition | Result |
|---|---|
| c24-fixture (final files, with the refuted-form delta; foundation status.py f9c995e9, interaction status.js ad436be6) | every check PASS (checks-c24-fixture.txt), as c21-fixture below |
| c23-fixture | every check PASS (checks-c23-fixture.txt) |
| c22-fixture | every check PASS (checks-c22-fixture.txt) |
| c21-fixture | every check PASS (checks-c21-fixture.txt), as listed below |
| c21-baseline1120 (11:20 layout baseline) | the audit rejects 31 content findings, all the content owner's, which this lane must not edit; the rest is listed below (checks-c21-baseline1120.txt) |
| c21-noatlas, c22-noatlas, c23-noatlas | audit PASS; no atlas section, mount, nav item or atlas script |
| worktree (baseline status.py, no mount) | 44 unit tests, 1 skipped by design (no AtlasContext) |

c21-fixture, check by check:

- builds with and without fonts: audit PASS;
- a second build with the same SOURCE_DATE_EPOCH: byte-identical;
- 44 unit tests through the foundation mount: PASS;
- jsdom: 22 pass, 0 skipped, 1 observed (the row toggle, which interaction owns);
- completeness: 3 domains, 13 claims, 12 edges, 2 comparisons, 2 paths and 2 question links, all drawn with their
  anchors;
- gate scans: PASS.

c21-baseline1120, check by check:

- unit tests: PASS;
- jsdom: 17 pass, 5 skipped, 1 observed. Each skip has a data reason: no statementRef, no dependency path, and no
  claim with the test's glossary term.
- completeness:
  - every domain, claim (503), edge (53), comparison (58) and path (18) is drawn with its anchor;
  - one question id names no question of the page;
  - stable anchors: 0 anchors lost against the c19 draft;
- gate scans: PASS (interface text, attributes, atlas.css, atlas.js).

## The 'refuted form' delta (content-contract integration, 2026-11-16)

The content owner's contract: legacy statement cards for checked scoped negative results use the exact status value
'refuted form'; its atlas equivalent is scoped_negative. It must never be coerced to 'open'. No scientific text is
edited by any lane.

**Done in the atlas (this set).**
- Colour: the atlas's Scoped negative uses the page's refuted-form colour, var(--st-refuted-form), in light, dark and
  print.
- Legend: the key shows the match beside Scoped negative, with the page's own mark and label, read from the page
  (ctx.mark('refuted form'), ctx.status_labels['refuted form'], currently "Refuted as first posed"). No match is
  claimed for the other statuses.
- Hypotheses: a scoped negative claim must list the hypotheses of its scope, as a conditional claim must list its
  own. Both are reader findings, so the build fails and a draft still draws. All 94 scoped negatives of the 11:20
  baseline list hypotheses. Scoped negative items keep their hypotheses in domain and comparison lists.
- Filters, search and accessibility:
  - the atlas status chips include Scoped negative;
  - the word filter reads status labels;
  - marks are named by their group;
  - the atlas shows no counts.
- Tests: unit test_the_key_shows_the_page_status_that_matches_scoped_negative and
  test_a_scoped_negative_claim_lists_its_scope.

**Needed in the other lanes.** These are current references, not patches, since those files keep changing.
- **Foundation, status.py (f9c995e9).**
  - Add 'refuted form' to STATEMENT_STATUSES (line 26). The tally (558-562), the key (580), questions (708) and
    audit.py (which imports the list and fails unknown statuses at line 58) then accept and count it.
  - Lines 383-385 append a problem and coerce an unknown statement status to 'open'. Line 643 coerces a target's
    status to 'open'. Once 'refuted form' is in the list, neither coerces it.
  - Statement cards render class st-refuted-form and chip-refuted-form (lines 394-396), and the hypotheses list is
    already supported there.
  - page.json already has the label "Refuted as first posed" and its gloss.
- **Foundation, status.css (1a281621).**
  - Add `.st-refuted-form { --st: var(--st-refuted-form); }` beside lines 206-207, plus any chip and card treatment.
    The token, the mark colour and the print token already exist.
- **Interaction, status.js (ad436be6).**
  - The statement filter facets are read from the page's filter buttons (lines 1479, 1521, 1573), and search
    reads data-status (line 1068). Both follow foundation's markup, so no code change is expected.
  - A jsdom test should show that a 'refuted form' statement is filtered, found, labelled and counted, and never
    shown as open.
- **Quality.** Independent tests that:
  - no 'refuted form' statement is coerced to open;
  - its hypotheses render;
  - the tally counts it;
  - the audit accepts it and still fails truly unknown statuses.

## Hooks for the quality lane

| Requirement | Atlas markup |
|---|---|
| nodes: [data-claim-id] + data-status-code + visible status label | article.atlas-claim#atlas-c-<id>[data-claim-id][data-status-code][data-domain-id]; chip with the group word; "Status:" with the claim's own label (.atlas-status-text); the index shows the same label (.atlas-status-own) |
| claim ids deep-linkable | #atlas-c-<id> (the claim shown is unhidden; the others carry hidden while the script runs; print shows all) |
| edges: [data-edge-id][data-source][data-target][data-relation] | li.atlas-rel in both claims' lists, path.atlas-edge in the map, path.atlas-hood-edge in the pane diagram, li in a path's join list |
| paths: [data-path-id][data-path-kind] | article.atlas-path#atlas-p-<id>; editorial paths say "Editorial order" |
| text equivalent of every drawn relation | the sentence lists of each claim; the map and diagram are aria-hidden, their marks are tabindex=-1 links |
| supplied text versus the atlas's own words | atlas.SUPPLIED_CLASSES (one list, read by gate_scan.py and the tests) |

Other references: index rows tr#atlas-r-<id>[data-claim-ref], map marks a.atlas-node[data-claim-ref], domain
cards article#atlas-d-<id>, conventions #atlas-d-<id>--conv, comparisons article#atlas-k-<id>, key items
[data-key-status] and [data-key-relation][data-key-style], question links a.atlas-question-link[data-question-ref].

## Design choices for root

The full text is in CONTRACT.json, design_choices_for_root, 17 items. The ones that need a decision:

1. **Placement at real scale.** The atlas comes after #status and before #results. On the 11:20 baseline it is
   3.5 MB of a 5.5 MB page without fonts. Should the claims in full print as an appendix?
2. **Two "Comparisons".**
   - The page nav "Comparisons" leads to #frontier, "The remaining comparisons".
   - The atlas part is "Comparisons in the atlas".
   - The atlas word Remaining stands against the page's remaining comparisons. comparisons[].questionId is the
     content owner's link between them.
3. **Status vocabulary and glosses (content owner).** On the baseline the labels vary within each status. They are
   shown claim by claim and listed as content findings.
4. **Names on the map.** The principal's rule V18 asks for "small labels beside their nodes". At 503 claims the map
   shows numbers, and gives names on hover, in the pane and in the index. Deciding this needs a page image.
5. **Requests to foundation.**
   - ctx.title_of(anchor), so that question links read their question without the script.
   - ctx.status_of(id), to show a linked statement's own status.
   - json.loads inside a try, so that a malformed atlas.json gives an audit failure, not a traceback.
   - SOURCE_DATE_EPOCH set by the builder.
6. **Request to interaction.** Describe atlas glossary terms by their definitions (aria-describedby).
7. **Root's draft policy.** Drafts draw text that fails the reader rules, as the page's own drafts do.
8. **asOf.** It is read and never shown.
9. **Back after a row toggle.** It cannot return to an earlier atlas selection, because the page replaces that
   history entry.

## Content findings of the 11:20 baseline (for the content owner; nothing edited)

- **Notation outside TeX that the page audit reads as internal identifiers or version tags:**
  - 'C1': mixed-stronger-physical-comparison, hypotheses 13 and 14; gravity-ordinary-reduced-inverse, hypothesis 1;
  - 'N12': centre-fixed-bound-state-witness, hypothesis 0;
  - 'E1': elliptic-exact-generating-matrix, statement and hypothesis 2;
  - 'R1': nonrational-fixed-moment-exchange, statement;
  - 'C0': analytic-gaussian-target-topology, hypothesis 0;
  - 'v4 v5 v6': analytic-elliptic-earlier-supported-pair, statement and hypothesis 0;
  - 'v4': the reading path analytic-reading-elliptic, stage 7 description.
- **An unresolved question id.** The comparison d-centre-base-change gives questionId 'decisive-centre-base-change',
  which names no question of the page.
- **Listed by completeness.py, not failed:**
  - 81 ids have a part shaped like an internal identifier, such as -p1 or -r3. These ids appear in addresses.
  - Status labels vary within each status: 4, 3, 3 and 2 labels.
  - Two relation codes carry two labels each.

## Attack-heal record

The full record is in LEDGER.md, attacks/A1-* to A4-*, SWARM.json and RESTRICTION.md.

- The two read-only referees were resumed for each cycle, and no other agents were used.
  - af52c6b0a1887ca57 is the reader-task lens.
  - a2472c39c51df1d18 is the integration and safety lens.
- Cycle 5: the integration referee verified every heal and recommends stop (attacks/A5-IN.yaml).
  The reader-task referee verified A4-RT-02..04 and the records, and found one gap: the reader's place when the pane
  closes (attacks/A5-RT.yaml). That gap was healed in atlas.js placeKeeper (e1fcbf76...).
- Cycle 6 (attacks/A6-RT.yaml): that heal helped the closing direction in part, and made a new regression in the
  opening one (A6-RT-01). The minimal heal, choosing by direction and only elements in view that move with the page,
  is in atlas.js 897ebd2c....
- Cycle 7 (attacks/A7-RT.yaml): verified healed by reading, and the referee recommends stop. One optional severity-4
  residual is recorded in LEDGER.md. Both referees now recommend stop. Static convergence is reached for this lane;
  convergence in the principal's sense is not claimed while page images are unjudged.
- Convergence is not claimed while page images are unjudged.

## Lane folder contents (none of it is page source)

- integration/: compose.py, run_checks.sh, gate_scan.py, completeness.py, atlas-files.patch and
  check_atlas_files.py. It also holds superseded history (status.py.patch, apply_status_patch.py,
  build_candidate.py, status.py.patched).
- composed/: frozen compositions with logs.
- checks/ and checks-*.txt: results of run_checks.
- inputs/layout-snapshot-1120: read-only copies.
- attacks/, LEDGER.md, CONTRACT.json, EVALUATION-PLAN.md, RESTRICTION.md, SWARM.json and BASELINE.json.
- baseline/, inv1-*, dev/, candidate/ (superseded), browser-dev/ and historical/: historical.
- tmp/: scratch.
- Nothing here is staged.
