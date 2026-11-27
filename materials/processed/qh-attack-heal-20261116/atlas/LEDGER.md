# Atlas lane: consolidated attack ledger

Sources: attacks/A1-RT.yaml (researcher tasks, 12 entries) and attacks/A1-IN.yaml (integration and reader
safety, 14 entries), first wave, independent, read-only, saved verbatim on return; root's integration note
(the foundation mount, the interaction isolation, the quality hooks) and root's browser restriction
(RESTRICTION.md). Status: valid (drives a heal), healed (heal made, verification attached), invalid
(refuted), non_core (real, outside this lane's authority: reported to root), undecided (blocks convergence).

Verification bindings refer to: U = tests/test_atlas.py (26 tests), J = tests/atlas.test.cjs (15 jsdom
reader-task tests on the composed page), B = build audit of the composed page, S = scans in INTEGRATION.md.
All were run on composed/c7-fonts (fonts embedded) and composed/c6-nofonts; results in each folder's
unittest.log and jsdom.log.

| RC | Attacks | Sev | Status | Heal | Verification |
|---|---|---|---|---|---|
| RC1 dependency-path claim exceeds what is checked | A1-RT-01, A1-IN-09 | 2 | healed (wording and rule); non_core residual: which relations are dependencies | Every claim of a stage joined to the next stage (first stage) or the stage before (others); labelled "Joined by recorded relations", never "dependency"/"proof"; each joining relation printed in its own direction, backward ones marked. | U test_paths_joined_by_recorded_relations, test_editorial_and_joined_paths_are_labelled_by_what_is_checked; J RT5 |
| RC2 neighbourhood direction; INV4 blind to reversal | A1-RT-02, A1-IN-06 | 2 | healed | Lists and diagram name only the recorded direction (full sentence per item, identical in list, pane and print); tests compare list placement, map geometry and diagram endpoints with the fixture. | U test_quality_hooks, test_map_lines_start_at_their_source_and_end_at_their_target; J INV4, RT2/RT3 |
| RC3 atlas statuses borrowed the page's marks | A1-RT-03, A1-IN-05 | 2 | healed (the proposed map of scoped_negative to the refuted mark rejected: a scoped negative is settled, not refuted) | Own square glyph family and tokens (light, dark, print); one supplied label per code; data-status-code; key shows the supplied label. The page statement's own status beside a statementRef link needs a ctx capability: dropped, the link leads to the statement. | U test_typed_vocabulary, test_statuses_and_hypotheses_are_shown_as_supplied |
| RC4 conditional without hypotheses | A1-RT-04 | 2 | healed; non_core residual: a field naming the unproved hypothesis | Error when a conditional lists none; conditional and scoped-negative entries keep their hypotheses in domain cards and comparisons. | U test_conditional_claims_name_their_hypotheses |
| RC5 run-time counts | A1-RT-05, A1-IN-08 | 2 | healed | Number-free live text; no total in the path position; scans of the whole atlas text and labels after interaction. | J RT8/INV5, final scan; U test_no_count_presented_as_progress |
| RC6 empty states imply completeness | A1-RT-06 | 3 | healed (In/From degree numbers kept: not theorem or progress counts) | Sentence in the introduction; four groups always shown, "None listed." | U test_statuses_and_hypotheses_are_shown_as_supplied |
| RC7 page search misses the atlas; tally scope | A1-RT-07 | 3 | non_core (interaction isolation and foundation tally: design choices reported to root) | Atlas words searchable through the atlas filter; my earlier status.js proposal withdrawn in favour of the interaction contract. | J "the page search leaves the atlas alone" records the behaviour |
| RC8 selection and history | A1-RT-08 | 3 | healed within the interaction contract; non_core residual: Back after a row toggle | Selection is the address; native in-page links make the entries; hashchange and qh:state are followed; nothing is written to the address or history. | J RT9 (four tests); U test_script_and_styles_make_no_request |
| RC9 Escape, term card, focus | A1-RT-09, A1-IN-13, A1-IN-14d | 3 | healed | No term inside a link; Escape left to the page while #card is shown; focus falls back to the index link, then the filter. | J RT6 (two tests) |
| RC10 print | A1-RT-10, A1-IN-10, A1-IN-14b | 3 | healed in markup and CSS; residual: print not observed (no browser) | Domain cards and every claim print; filters, pane, diagram hidden; filtered rows print; atlas CSS before the page print sheet (foundation order). | static CSS review only; print not rendered under the restriction |
| RC11 duplicate titles | A1-RT-11 | 3 | healed | Error on duplicate titles; every reference carries its index number. | U test_titles_are_unique, test_every_claim_reference_carries_its_number |
| RC12 contract statements about code | A1-RT-12, A1-IN-04, A1-IN-05, A1-IN-12 | 3 | healed | CONTRACT.json rewritten against the actual foundation, interaction and quality code. | review of CONTRACT.json against status.py (foundation) and status.js (interaction) |
| RC13 reader-safety scan gaps | A1-RT-12(1), A1-IN-01 | 2 | healed | Strings scanned as written and with _ - as spaces; id parts of internal-identifier form, hash-like runs, percentages, name:part labels refused. | U test_reader_safety_of_every_string, test_ids; S whole-document scan |
| RC14 determinism; candidate with an atlas | A1-IN-02, A1-IN-03 | 3 | healed | SOURCE_DATE_EPOCH fixed (worktree build reproducible byte for byte); integration/compose.py freezes a composition and builds it. | INTEGRATION.md build table |
| RC15 crash vs rejection; type confusion | A1-IN-07 | 3 | healed (catch-all rejected: validation made total) | Every value type-checked before use. | U test_types_are_checked_before_use |
| RC16 fragile whole-file patch | A1-IN-11 | 3 | invalid now (superseded): the foundation mount replaces the patch; the patch files stay in integration/ as history | — | — |
| RC17 run-time words outside audit and subset | A1-IN-08 | 3 | healed | Words in an inert template inside the mount. | U test_interface_words_travel_in_the_template; B audit PASS |
| RC18 quoting; network words | A1-IN-12 | 3 | healed | Double-quoted attributes; no network call, no url() but #fragment. | U test_namespace_and_attribute_quoting, test_script_and_styles_make_no_request |
| RC19 pane formulas; annotation text | A1-IN-14a, A1-IN-14c | 4 | healed | Scroller rule applied in the atlas; text walks skip annotation, svg, script, style, template. | code review; J filter tests |
| RC20 module API did not match the foundation mount | root note | 2 | healed | render(data, ctx) returning html/title/kicker/nav_label/css/js/problems; only ctx used. | U Mounted test on foundation status.py; B audit PASS |
| RC21 atlas wrote history; interaction forbids | root note | 2 | healed | Native links; qh:navigate for page anchors. | J RT9, qh:navigate test; U no-address-write test |
| RC22 quality hook names | root note | 3 | healed | data-claim-id, data-status-code, data-edge-id, data-source, data-target, data-relation, data-path-id, data-path-kind. | U test_quality_hooks |
| RC23 page-hook class names inside the atlas | foundation namespace rule | 3 | healed | mark and filter replaced; the only page hooks inside are ctx.rich's term and math classes. | U test_namespace_and_attribute_quoting |
| RC24 the word "prompt" (page forbidden vocabulary) in shipped code | own scan | 4 | healed | js_prompt renamed js_empty; whole-document scan clean. | S |
| RC25 foundation's atlas_test.py counts 'data-atlas-mount' in the whole page | own test | 3 | non_core (foundation file): with interaction's status.js the string occurs in scripts, so that count is 5 on the composed page | reported to root | U Mounted test counts the mount element instead |

No severity 1 attack was found. Every severity 2-3 item is healed, superseded or non_core with a named
owner. Undecided: none. Verification still missing: visual and print rendering in a real browser (RESTRICTION.md).

## Cycle 2 (referees) and cycle 3 (heals), 2026-11-16

Referees: the two first-wave reviewers, resumed read-only (attacks/A2-RT.yaml, attacks/A2-IN.yaml), each with root's
browser restriction verbatim; the principal's scope message and the full five-failures rulebook were forwarded whole
to the reviewer still active when they arrived, and go whole to every later reviewer. Both verdicts: continue one cycle.
Heals verified on composed/c10-fonts: build audit PASS (including the foundation reserved-class check), 35 unit
tests pass, jsdom 19 pass, 1 SKIP (glossary card: terms are off), 1 OBSERVED (row toggle, interaction-owned).

Corrections to the table above (the earlier rows stay as the record):
- RC2: the placement check is the jsdom INV4 test (with RT2/RT3), not test_quality_hooks.
- RC7: healed after all, inside the interaction contract: claims, domains, comparisons and paths are offered as
  [data-qh-unit] search units; a page-search result selects the claim through qh:reveal (jsdom test). The tally scope
  stays non_core (foundation).
- RC10: unverified, not healed: print was never rendered (restriction). Static review only.
- RC15: the value types are healed; a malformed atlas.json is non_core, owner foundation (json.loads outside a try).

| Id | Sev | Status | Heal | Verification |
|---|---|---|---|---|
| A2-RT-01 vocabulary collisions with the page | 2 | healed in part; non_core residual for root and the content owner | atlas part renamed "Comparisons in the atlas"; key sentence: the four statuses and square marks belong to the atlas; Conditional glossed as an implication with at least one hypothesis not established (agrees with the page key); colour hues deliberately shared (learnability) with shapes and the key sentence separating the vocabularies (rejected part, reason recorded); statementRef status display reported to root | unit test_atlas_statuses_are_said_to_be_the_atlas_own; Mounted test (no part name equals a page section); jsdom map-first test |
| A2-RT-02 rail arrows and join order | 3 | healed | rail without arrowheads; "Stage n is joined to stage m by", "(runs from stage n to stage m)"; heading before the join box; Follow bar shows the path kind | unit test_stage_heading_comes_before_its_joins_and_the_rail_has_no_arrow; jsdom RT5 kind test |
| A2-RT-03 "5 Remaining" reads as a count | 3 | healed | status chip first, then "No. n"; numbers in links read "No. n" (visually hidden "No."); introduction "sets out claims"; count scans walk text with a space at each element | unit test_no_count_presented_as_progress; jsdom NO_COUNT scan |
| A2-RT-04 narrow sheet keeps focus under it | 3 | healed | the sheet closes when keyboard focus leaves it for the page (the term card excepted) | jsdom RT7 focus test |
| A2-RT-05 finding claim text | 3 | healed | the filter reads title, statement, hypotheses and source only and says so; the page search reaches the claims (data-qh-unit) | jsdom RT8 filter test, page-search test |
| A2-IN-01 closed sheet reopens on qh:state | 3 | healed | reopens only on an address change or the reader's own selection | jsdom RT7 sheet test |
| A2-IN-02 focus left in a hidden claim after Back | 3 | healed | focus follows the selection when it was in the pane | jsdom RT6/RT9 focus test |
| A2-IN-03 the map scales up | 3 | healed in CSS; rendering unverified | never enlarged: lane 112px, at least 90px, scrolls in its box | unit test_the_map_is_never_enlarged |
| A2-IN-04 more than six relation types | 3 | healed | eight line styles; a ninth relation type is a problem | unit test_more_relation_types_than_line_styles_is_a_problem |
| A2-IN-05 overview after the domain cards | 3 | healed | the map with its key is the first part | unit test_the_map_and_key_come_first; jsdom map-first test |
| A2-IN-06 two legends and one word with two marks | 3 | non_core (content owner and root) with mitigation | the atlas key now follows the map, not the page key; key sentence separates the vocabularies; the choice between one mark per word and two vocabularies is in design_choices_for_root | — |
| A2-IN-07 derived ids can collide | 4 | healed | heading ids use --h; an id used twice is a problem | unit test_derived_ids_cannot_collide |
| A2-IN-08 interface words not scanned; glued template | 4 | healed | every label checked with the reader rules; template words separated by spaces | unit test_interface_words_meet_the_reader_rules |
| A2-IN-09 Escape into the hidden map | 4 | healed | focus never returns into an aria-hidden drawing | code review |
| A2-IN-10 tests that cannot fail | 4 | healed | SKIP and OBSERVED reported apart from PASS; asset FORBIDDEN scan added | unit test_shipped_script_and_styles_carry_no_forbidden_word |
| A2-IN-11 no rhythm or type scale | 4 | healed in CSS; judgement unverified | one rhythm unit; heading sizes by level; golden proportion of atlas and pane | static review; page image not rendered |
| RC26 the foundation reserved classes forbid ctx.rich's own output | 2 | non_core (foundation and interaction contracts disagree); compliant now | glossary buttons off (TERMS flag), formula boxes renamed with their behaviour reproduced in atlas.css; proposal in design_choices_for_root | build audit PASS on c10; unit test_namespace_and_attribute_quoting |

Convergence: not claimed. Every severity 1-3 item is healed, healed in part with a named non_core residual, or
non_core with an owner; the cycle-3 heals await the next independent referee pass. Visual, narrow, print and
reduced-motion rendering stay unverified under the restriction.

## Cycle 3 (referees) and cycle 4 (heals and the 11:20 layout baseline), 2026-11-16

Referees: the same two reviewers resumed read-only (attacks/A3-IN.yaml, attacks/A3-RT.yaml), holding root's browser
restriction, the principal's scope words and the five-failures rulebook whole. Heals below are on the final files
(INTEGRATION.md lists their sha256) and verified locally on composed/c18-fixture and composed/c18-baseline1120;
the independent referee verdicts on these heals are recorded in attacks/A4-IN.yaml and attacks/A4-RT.yaml when they
return. Final local verification: composed/c19-fixture and composed/c19-baseline1120 (checks-c19-*.txt), with the
foundation and interaction files current at composition (MANIFEST.json). The 11:20 atlas (inputs/layout-snapshot-1120, 9 domains, 503 claims, 53 edges, 58 comparisons, 18 paths) is a
review and layout baseline only: it is not the final tracker content, and nothing of its text was edited.

| Id | Sev | Status | Heal | Verification |
|---|---|---|---|---|
| A3-IN-01 the inert template becomes the first grid item | 2 | healed | template class atlas-wordlist, which no rule styles; .atlas-body > template { display: none !important }; atlas column and pane placed by grid-column and grid-row | unit test_interface_words_travel_in_the_template (class and every word key the script asks for); jsdom 19 pass on c18-fixture; wide layout unrendered |
| A3-IN-02 map numbers below small type, shrinking, labels broken anywhere, bands lost in print | 3 | healed in CSS and geometry; rendering unverified | numbers 13px and never shrunk on screen (the box scrolls); a long domain runs over several columns, with the fewest rows that keep the map within 1100px (11:20 baseline: 1040 x 1172, 14 columns of marks); domain names above and below; labels break at words, hyphenated; print: the map reaches 13mm into each margin, as display formulas do, and its bands print | unit test_the_map_keeps_its_own_size_on_screen, test_a_long_domain_runs_over_several_columns; residual: dark-mode band contrast unchanged (the rules between domains carry the separation) |
| A3-IN-03 printed formulas without the page's fit | 3 | healed | print: .atlas .atlas-math-display math { font-size: min(.94em, calc(150mm / var(--fw, 1))) } as status-print.css; scrollbar-width none; on screen the page's WebKit thin scrollbar; .97em at 560px and below | static comparison with status-print.css and status.css; print unrendered |
| A3-IN-04 spaces off the unit; h5 in three sizes | 4 | healed | every space between blocks on --au (the inner padding of small controls excepted, and the header comment says so); print unit 1.42, as the page's printed body; one h5 size (the pane override removed) | static review |
| A3-RT-01 the map as a view of the whole programme | 2 | healed in part | as A3-IN-02, and: one plain line style with a key sentence when relation types exceed eight (11:20 baseline: 31 types; each relation is named in both claims' lists); the selected mark is brought into view inside the map box only; titles on pointer hover; a tap selects the claim (the sheet shows it) | residual: claim titles are not drawn on the map; the index is the keyboard and screen-reader route (marks stay tabindex -1 by design); rendering unverified |
| A3-RT-02 first view and legend placement | 3 | healed | the key comes before the map; on a wide screen the pane takes its column only while it shows a claim, so the map has the full column at first view; the comparison comment gives the real breakpoints | unit test_the_map_and_key_come_first (key, then map) |
| A3-RT-03 rhythm and heading weights | 3 | healed | every heading at the page's heading weight 600, sizes 1.3 / 1.16 / 1.08 by level; the full list's domain headings at 600; block spaces on the unit | static review; page image not rendered |
| A3-RT-04 the glossary loss recorded as compliance | 3 | healed (with RC26) | the foundation mount now exempts the classes ctx.rich emits (status.py ac5b18dd, line 267) and the interaction script shares the card of a .term[data-term]: atlas.py TERMS = True, so glossary buttons are back in statements, hypotheses and plain text, never inside a link; formula boxes stay renamed | unit test_glossary_buttons_in_the_text_and_never_inside_a_link; jsdom glossary-card test runs and passes on c19-fixture (20 pass, 0 skipped) |
| A3-RT-05 proportion of the page at real scale | 3 | healed in part; placement non_core (root, foundation) | an index of more than forty claims scrolls in its own box on screen, its head in view (print shows every row); domain groups show eight claims, the rest behind "more"; whether the atlas follows the principal results, and whether its claims in full print as an appendix, are root's | unit (atlas-index-long); 11:20 baseline measured: atlas section 3.5 MB of a 5.5 MB page without fonts |

Adaptations for the 11:20 layout baseline (renderer rules, no data edited):

| Id | Finding on the baseline | Heal |
|---|---|---|
| RD1 | one status label per code: 170 failures; labels are given claim by claim | each claim shows its own label; the key lists the labels used for each status |
| RD2 | relation codes with spaces and capitals (13); one label per relation (2) | codes are words joined by _, - or spaces; each edge keeps its own label |
| RD3 | 81 ids with parts such as p1, r3, n2 | the id-part rule dropped: ids are never shown as text; the page's rules still apply to every shown string and to ids read with _ and - as spaces |
| RD4 | notation such as dbar:L_P and Xi:RHom read as labels (4) | the label rule reads LaTeX label prefixes only (thm:, prop:, lem:, eq:, ...) |
| RD5 | new optional fields: domains conventions and relatedQuestionIds, comparisons questionId and relatedQuestionIds, paths note | shown; question links go only to the page's #q- anchors and take the question's heading as their text; an unresolved id fails the build and is named |
| RD6 | 31 relation types for 8 line styles; a 175-claim domain | plain lines with a key sentence; domain columns (as A3-IN-02) |
| RD7 | errors were all-or-nothing | structural errors (shape, type, reference) draw nothing; reader findings (text rules, unknown keys, unresolved question ids) fail the build but a draft still draws, from the known fields only |

Content findings of the 11:20 baseline, for the content owner (not edited; the page audit rejects each): notation
outside TeX read as internal identifiers or version tags: claims mixed-stronger-physical-comparison hypotheses 13
and 14 ('C1'), gravity-ordinary-reduced-inverse hypothesis 1 ('C1'), centre-fixed-bound-state-witness hypothesis 0
('N12'), elliptic-exact-generating-matrix statement and hypothesis 2 ('E1'), nonrational-fixed-moment-exchange
statement ('R1'), analytic-gaussian-target-topology hypothesis 0 ('C0'), analytic-elliptic-earlier-supported-pair
statement and hypothesis 0 ('v4 v5 v6'), reading path analytic-reading-elliptic stage 7 description ('v4'); and
comparison d-centre-base-change questionId 'decisive-centre-base-change', which names no question of the page.

RC26 closed: healed with A3-RT-04 above. Open, non_core: A3-RT-05 placement and print appendix (root, foundation); A2-RT-01 and A2-IN-06 status vocabulary (content owner, root); row-toggle Back
(interaction); tally scope (foundation); malformed atlas.json traceback (foundation).

Convergence: not claimed. Visual, narrow, print and reduced-motion rendering remain unverified under root's
restriction; the final content payload has not been rendered.

## Cycle 4 (referees: attacks/A4-IN.yaml, attacks/A4-RT.yaml) and cycle 5 (heals), 2026-11-16

Both referees: continue one bounded cycle. Their verdicts on the cycle-3 heals: A3-IN-01, 03, 04 and A3-RT-03, 04
verified-healed (by reading; the look unresolved); A3-IN-02, A3-RT-01, 02, 05 healed in part; RD2, RD6 verified;
RD3, RD4, RD5, RD7 verified with residuals. Heals below are on the final files (INTEGRATION.md lists their sha256),
verified locally on composed/c21-fixture and composed/c21-baseline1120, both built with one sibling snapshot
(foundation status.py 66cc1159; interaction status.js 6f3b45e6; MANIFEST.json). The c20 compositions caught the
foundation's status.py in the middle of a change (47b60701 checked for placeholders before formulae were filled, so
every atlas formula failed the build); they are kept as a record only.

| Id | Sev | Status | Heal | Verification |
|---|---|---|---|---|
| A4-IN-01 gate scan's supplied list stale after the renames | 3 | healed | atlas.SUPPLIED_CLASSES is the one list; gate_scan.py imports it; atlas.test.cjs carries every class of it | unit test_every_supplied_text_sits_in_a_supplied_class (a sentinel word in every supplied string, none left outside the list, text or attributes); unit test_the_reader_tests_know_every_supplied_class |
| A4-IN-02 the frozen patch kept TERMS off | 3 | healed (c19; referee verified) | TERMS = True frozen in patch, guard, contract and ledger | jsdom glossary-card test runs and passes |
| A4-IN-03 a reused out dir could test a stale page | 4 | healed | run_checks.sh refuses an out dir that is not empty and takes the page from this run's exit status | checks-c21-*.txt |
| A4-IN-04 drafts draw strings that fail the reader rules | 4 | non_core (root's draft policy) | recorded in CONTRACT.json design choices | none |
| A4-IN-05 id parts shaped like identifiers reach addresses | 4 | healed as a content finding | completeness.py lists such ids for the content owner (81 on the baseline), without failing | checks/c21-baseline1120/completeness.log |
| A4-IN-06 Tab past the glossary card could land in a hidden claim | 3 | healed | only the claim the pane shows is unhidden (hidden attribute, which the page's Tab logic respects); print shows every claim | jsdom test A4-IN-06 (the term made the last control of its claim; focus never lands in a hidden claim or the closed card) |
| A4-IN-07 atlas terms not described by their definitions | 4 | non_core (interaction) | recorded in CONTRACT.json design choices | none |
| A4-RT-01 opening the pane reflows the atlas column | 3 | healed in part | the element the reader acted on (or the part at the top of the window) is put back where it was when the pane opens or closes; the full-width first view is kept, because a column reserved from arrival would make the real-scale map (1040px) scroll at first view (731px column at 1400px) | code review; layout unrendered |
| A4-RT-02 plain mode hides the relation kinds | 3 | healed | the key lists every relation in a disclosure ("The relations recorded in the atlas"); the map tip names the relations of the claim pointed at, with the other claim's number (up to six, then a note) | unit (plain-mode key lists every label); tip unrendered |
| A4-RT-03 status labels vary within a status | 3 | healed in part; meaning non_core (content owner) | the index shows each claim's own label under its group; the filter reads status labels and says so; marks are named by their group, never by a supplied label; completeness.py lists the variants per status | unit test_the_index_shows_each_claims_own_status_label; jsdom RT8 (a claim found by its own label) |
| A4-RT-04 conventions after the claims they govern | 3 | healed | conventions right after the domain summary (anchor atlas-d-<id>--conv); every claim of the domain links to them | unit test_conventions_come_first_and_each_claim_links_to_them |
| RD4 residual: label rule case-sensitive | 4 | healed | the label rule ignores case | unit (reader rules) |
| RD5 residual: question links generic without the script | 4 | non_core (foundation capability) | with the script the link carries the question heading as the page sets it, formulae included, without its links or ids | jsdom test (link text equals the question heading) |
| Tools: guard messages; section bounds; anchors; repro | - | healed | check_atlas_files.py --before says whether to apply; gate_scan and completeness end the atlas at its own closing tag; completeness --baseline lists vanished anchors in and outside the atlas; REPRO=1 compares two builds byte for byte | checks-c21-fixture.txt |

Open after cycle 5: visual, narrow, print, reduced-motion and forced-colours rendering (root's restriction); A3-RT-01
names on the map (the principal's rule V18; design choice for root); A3-RT-05 placement; A2-RT-01 vocabulary; the
non_core items above. The final content payload has not been rendered.

## Cycle 5 (referees: attacks/A5-IN.yaml, attacks/A5-RT.yaml) and cycle 6 (one heal), 2026-11-16

- Integration and safety lens (A5-IN): A4-IN-01, 03, 05 and 06, RD4, the guard messages, the section bounds and
  the completeness baseline are verified. Marks named by their group word are judged an improvement. No new
  attack. Recommendation: stop.
- Reader-task lens (A5-RT):
  - verified: A4-RT-02 (in code; the tip and the look are unrendered), A4-RT-03 (whether the labels mean different
    standings stays the content owner's), A4-RT-04, and the record fixes;
  - healed in part: A4-RT-01. Opening the pane keeps the reader's place; closing did not.
  - The full-width first view is judged the right choice.
  - No new attack. Recommendation: continue, for that one gap only.

| Id | Sev | Status | Heal | Verification |
|---|---|---|---|---|
| A4-RT-01 (closing) the reader's place when the pane closes | 3 | healed (awaiting A6-RT) | placeKeeper keeps, in order: the element acted on in the atlas column; the focused element wherever it is (never in the pane); the address target outside the atlas; else the first atlas part in view; it does not scroll if the kept element has lost its box | composed/c22-fixture: every check PASS (checks-c22-fixture.txt); layout unrendered |

Final files: atlas.js e1fcbf76... (all other files as in cycle 5). Patch b7cd6aa0..., guard 7e4ea29f....
c22-fixture and c22-baseline1120 share one sibling snapshot (foundation status.py ee0a349a, interaction status.js
9802c92e). c22-noatlas caught a later foundation status.py (b960b668) and passes.

## Cycle 6 (referee: attacks/A6-RT.yaml) and cycle 7 (one heal), 2026-11-16

- A6-RT: the cycle-6 heal helps the closing direction only in part. The focused element was chosen before the
  address target, so a sticky nav link could be the kept element, and it does not move.
- It also opened a regression in the opening direction (A6-RT-01, severity 3): Back into the atlas could keep a
  statement below the atlas that the page had focused earlier, and scroll the view away.
- Recommendation: continue, for that one function.

| Id | Sev | Status | Heal | Verification |
|---|---|---|---|---|
| A6-RT-01 and A4-RT-01 (both directions) | 3 | healed (awaiting A7-RT) | placeKeeper(opening) chooses by direction. Opening: the acted-on element, then the focused element, in the atlas column. Closing: the address target, then the focused element, outside the atlas. Both fall back to the first atlas part in view. A candidate must have a box, be in view, lie outside the pane, and have no fixed or sticky ancestor | composed/c23-fixture: every check PASS (checks-c23-fixture.txt); jsdom has no layout, so this is judged by reading |

- Final files: atlas.js 897ebd2c.... All other files are as in cycle 5.
- Patch cda01f2d..., guard a7c104bf....
- c23-fixture and c23-baseline1120 share one sibling snapshot: foundation status.py b960b668 and interaction
  status.js b627d8d4.
- c23-noatlas caught a later foundation (status.py 86747f2f) and passes.

## Cycle 7 (referee: attacks/A7-RT.yaml): both referees recommend stop, 2026-11-16

- A6-RT-01 and both directions of A4-RT-01 are verified healed, by reading. jsdom has no layout, so nothing here is
  rendered. There is no new attack.
- One severity-4 residual stays open and optional. When the pane opens by Back or Forward with nothing acted on or
  focused in the atlas column, the place kept is the top of a whole part, so a reader inside a long part can drift by
  that part's own reflow. The referee's optional heal is to keep the first card or row in view instead, or to leave
  it to native scroll anchoring where the browser has it.

**Static convergence: reached for this lane.** Both independent referees, across cycles 1-7, leave no severity 1-3
finding open in the lane's scope, and every non_core item has an owner (CONTRACT.json design_choices_for_root).

**Convergence in the principal's sense: not claimed.**
- No page image has been judged beside the best exemplars: visual, wide and narrow layout, print, light and dark,
  reduced motion and forced colours are all unobserved, under root's restriction.
- The final content payload (root's 13:50 candidate) has not been rendered.

## The 'refuted form' delta (content-contract integration), 2026-11-16

| Item | Change in the atlas | Verification |
|---|---|---|
| colour | the atlas's Scoped negative uses the page's refuted-form colour, var(--st-refuted-form), in light, dark and print; the atlas's own magenta is gone | unit (the stylesheet carries the token) |
| legend | the key shows the page's matching statement status beside Scoped negative, with the page's own mark and label from ctx ("Refuted as first posed"); no match is claimed for the other statuses; page marks appear nowhere else in the atlas | unit test_the_key_shows_the_page_status_that_matches_scoped_negative |
| hypotheses | a scoped negative claim must list the hypotheses of its scope, as a conditional claim must list its own (both are reader findings) | unit test_a_scoped_negative_claim_lists_its_scope; the 11:20 baseline has 94 scoped negatives, all with hypotheses |
| filters, search, counts, accessibility | unchanged and consistent: status chips, the label filter, group-named marks, and no counts | jsdom suite on c24-fixture (22 pass) |

- Other lanes: the parts needed of foundation (STATEMENT_STATUSES, the coercions to 'open', the card CSS),
  interaction (a test) and quality (tests) are listed in INTEGRATION.md, with line references.
- Frozen: patch d0623e3b..., guard a6707704....
- The referees' check of the delta is recorded as attacks/D1-*.yaml.

## Delta check (D1-RT, D1-IN) and the status-language ruling, 2026-11-16

- **D1-RT:** the atlas side of the refuted-form delta is verified. A8-RT-01 (sev 4) went to root and the content
  owner, and the ruling now settles it: every atlas status has its page alias, so colour and legend agree. Both
  halves of A8-RT-02 (sev 4) are healed:
  - a page that cannot show the mark of an alias gives a named finding;
  - the page colours its own mark.
- **D1-IN:** the missing search status (sev 3) is healed for all four statuses. Every claim carries
  data-qh-unit-status by alias, and the jsdom test runs on the fixture: status-filtered search keeps the claims of
  that status, names the page's word, and excludes the others. The checklist corrections are applied in
  INTEGRATION.md.
- **The status-language ruling** (content owner; root's relay), as presented by the atlas:
  - words by stored code;
  - the per-record labels are no longer shown;
  - the aliases checked, conditional, open and refuted form;
  - the page's legacy colours, with no new palette;
  - the page's mark beside each status in the key.
  - The tests were updated. Root asked for no new attack cycle, so no referee was resumed.
- **Bounded checks on root's 13:50 preview** (714 claims): see INTEGRATION.md. The atlas adds no audit failure, and
  every element is drawn with its anchor, with none lost. The content findings are for the content owner.
- **Frozen.**
  - Full set: c29, patch c540a08d..., guard 74258354....
  - Separate delta from the c24 set: atlas-delta.c24-c29.patch 99a5b680..., guard de8c6a7b....
- 2026-11-17 ~02:45 WIB — Five interactive figures frozen: ega-figures/five-models (figures-files.patch 50dcb17f…, delta from b28e07b0 68ff649d…, guard check_figures.py 063555c8…, checks.txt 5038c310…); handoff ega-figures/HANDOFF.md; diagram-contract findings for root/foundation in ega-figures/DIAGRAM-FINDINGS.md. No static diagram renderer built (foundation owns it, per root). Not committed.
- 2026-11-17 ~03:00 WIB — C5 one mark system: c5-marks/atlas-c5-marks.patch 51fbf53d… (atlas.py 084ff331…, atlas.css 48cd985b…, tests/test_atlas.py 600d7d69…; atlas.js and the jsdom tests unchanged), guard check_atlas_c5.py 0d0f7cec…; run_checks RESULT PASS; same 3,742 ids; squares 5,155 to 0. Five-model freeze unchanged. Not committed.
- 2026-11-17 ~04:00 WIB — G1–G3 Gaussian display repair: ega-figures/g1-g3/figures-g1-g3.patch a76ae286… (successor to the installed five-model set; figures.py e7ff72dd…, figures.css 1b0282ae…; figures.js unchanged), guard check_figures_g.py; checks.txt. Routed to the website lead (foundation 67e78388…) per root's transfer 738e4d95…. Not committed.
- 2026-11-17 ~04:05 WIB — G1–G3 rechecked on foundation v6 (monograph.py 605723ba…, monograph.css fc180108…): guard before/after pass, build audit 0 failures, MathML 0 errors; checks.txt 4d38d6ed…. Sent to the website lead (QH-EGA-FOUNDATION-RECOVERY-0343, foundation 67e78388) by native message with paths and hashes; C5 reported complete as installed (atlas.py 084ff331…).
- 2026-11-17 ~04:15 WIB — The website lead (foundation 67e78388) installed G1–G3 in integration and confirmed C5. Rechecked read-only from the integration root: check_figures_g.py --after and check_atlas_c5.py --after both as expected. Nothing further owed unless native QA finds a figure defect.
- 2026-11-17 ~06:45 WIB — Release v8 repair of G4, A2, A6 (with G5 and the map-edge name fix) sealed: v8-repair/atlas-v8-repair.patch 586ab9b4… against integration's installed files (figures e7ff72dd…/1b0282ae…/bce4e549…, atlas 084ff331…/48cd985b…/276565d7…), guard check_v8_repair.py e9f3ab13… (--check/--before/--after), SHA256SUMS, checks.txt 3046a9b2…, HANDOFF-V8-REPAIR.md. Integrated run_checks on a copy of integration: RESULT PASS (baseline fails only RT9's stale selector). Lane check tools completeness.py and gate_scan.py now find the atlas section by id. No page image made or judged. Not committed.
- 2026-11-17 ~07:00 WIB — The website lead installed the v8 repair in integration and built release v9 (index.html 702aca5c…, atlas.html 7b043c0b…). Rechecked read-only: check_v8_repair.py --check on integration reports the repaired bytes; v9 carries the shared Gaussian scale (0, 0.5, 1 on all three plots), the minus sign (−0.5), the locator (955 dots), the pane's column and its sticky head. Awaiting root's re-capture of items 5 and 6 and QA's verdict; nothing owed unless QA names a finding in these files.
