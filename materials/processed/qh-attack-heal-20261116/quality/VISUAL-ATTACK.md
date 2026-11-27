# Visual-system attack against the principal's design scope (lead, cycle 3)

Scope, the principal's words relayed by root: "upgrading it visually, giving god tier elite rhythm, harmony, balance,
proportion, god tier communication, god tier visualization of our research and the concepts and the totality of all
we are doing."

Evidence class: computed from the CSS, the built HTML and EB Garamond's metrics (`lead/qh-visual-metrics.py`;
results `lead/results/visual-metrics-candidate.json` and `visual-metrics-baseline.json`). These are proxies. Under the
principal's first rule the page image decides; none of this replaces it, and no page image has been judged yet (the
native Chrome integration is not connected: BLOCKER-CHROME.md). Each entry names the page-image check that decides it.
The baseline and the quality candidate share these properties unless stated; the candidate changed only controls,
the not-posed colour and print rules.

## Findings

### V01 Lines are too long at 768 to 1400 px (severity 3, valid by computation; owner foundation)
- Evidence: the column is fixed at 40rem (640 px) while the text size is 17.7 to 19.6 px; EB Garamond's average
  advance over the essay text is 0.379 em. Characters per line for prose: 86 at 1400, 92 at 1024, 96 at 768, 69 at
  480, 53 at 375. Statement text (inside the card padding): 81, 86, 89, 62, 47. The usual range for continuous
  reading is about 45 to 75.
- Page-image check: at 1400, 1024 and 768 px count the characters on five full lines of the lead, of a statement and
  of the essay.
- Heal direction (foundation): set the measure in em of the text size, or raise the text size, so that prose sits at
  about 60 to 72 characters; re-check the wide sections and the grid afterwards.

### V02 The type scale has no steps the eye can separate in the middle (severity 3, valid as a system defect; owner foundation)
- Evidence: 12 distinct sizes at 1400 px (15.3, 17.2, 19.6, 20.7, 21.9, 22.7, 23.9, 25.4, 26.2, 34.2, 34.4, 57.6).
  Seven roles sit between 20.7 and 26.2 px with adjacent ratios of 1.03 to 1.06: row name, lead and subtitle,
  statement title, principal-result title, open-group heading and the change-list title, question title. The
  section heading (34.4) and the essay title (34.2) differ by 0.6 percent and are set one above the other in the
  essay section. Further sizes are set in em (0.97, 1.02, 1.08, 3.35).
- Page-image check: the essay section's opening (section heading, essay title, byline); a decisive question card
  (card title, question statement, related statement titles); an example row opened (row name, statement titles).
  Are the levels read at a glance?
- Heal direction: one declared scale with a fixed ratio, each role mapped to a step; merge roles that are the same
  level.

### V03 Spacing and line-height are not a system, so the vertical rhythm is set case by case (severity 3, valid as a system defect; owner foundation)
- Evidence: 66 distinct spacing values in the screen CSS (65 in the baseline), 12 pixel values off a 4 px grid
  (1, 2, 3, 6, 7, 9, 10, 11, 14, 18, 22, 26), at least nine different clamp() expressions for section and block
  spacing, and 17 distinct line-heights (0.86 to 1.6, plus 32 px and 40 px).
- Page-image check: the gaps between a section heading and its first block, between statements, between question
  cards and between sections, at 1400 and 375 px. Equivalent gaps should look equal and the steps between levels
  should be clear.
- Heal direction: a spacing scale in tokens tied to the text line-height, used by every margin, padding and gap.

### V04 Heading weight runs against the hierarchy in question cards (severity 3, undecided; owner foundation)
- Evidence: a question title is 26.2 px at weight 400; the related statements under it carry titles at 22.7 px and
  weight 600. Section headings are 34.4 px at weight 400.
- Page-image check: on a decisive question card, does the card title lead, or do the bold statement titles inside
  it take the eye first?

### V05 Status colours collapse for colour-blind readers, and the small marks are then the only channel (severity 3, undecided; owner foundation)
- Evidence (CIEDE2000 after Machado et al. 2009 simulation, severity 1): deuteranopia, pending and conjecture 2.4
  (light), 0.8 (dark), 1.7 (print); conditional and published 4.2, 1.7, 4.1; checked and heuristic 1.8 (dark).
  Protanopia, checked and refuted-form 4.2 (light). Without simulation every pair is at least 11.2 apart. Each
  status has its own mark shape, so WCAG 1.4.1 is met, but marks are drawn at 11 px in the row strips and question
  indexes, 12 to 13 px in chips and legends and 17 px in the grid, with strokes of 1.6 units in a 16-unit box.
- Page-image check: zoom at 1x on the row-mark strips, the question index marks and the grid, in light and dark;
  can pending, conjecture, conditional and published be told apart by shape alone?
- Heal direction: separate the confusable pairs in lightness as well as hue, and enlarge marks where they are the
  only signal.

### V06 Visual weight of statuses is unequal (severity 4, undecided; owner foundation)
- Evidence: OKLCH chroma ranges from 0.014 to 0.136 across the ten statuses (light); "open" and "refuted form" are
  the most saturated, "published" and "not posed" nearly grey.
- Page-image check: the grid and the cover tally as a whole: what does the eye read first, and does that match what
  the page means to say about the programme?

### V07 Nothing on the page visualises the programme as a whole or the relations between results (severity 2, valid; owner atlas lane and content owner)
- Evidence: the built page has no figure other than status marks and icons (0 other SVG); its overviews are the
  status counts in the cover tally, the 20 x 8 status grid and two question indexes; 0 links run from one statement
  to another, and the 27 related-statement lists are nesting, not relations. There is no atlas, map or relation
  view (0 atlas hooks). 281 statements, 34 question cards and 144 glossary entries are reached by scrolling and
  search. The principal's scope asks for "god tier visualization of our research and the concepts and the totality".
- This is the core requested outcome that neither the baseline nor this lane's candidate delivers. Root has said the
  content owner is preparing the complete fixed-cut atlas and the atlas lane owns its modules; this lane will test
  it against CONTRACT.json (Q24) and VQ6 below.

### V08 The main overview needs sideways scrolling on a laptop screen (severity 3, undecided; owner foundation)
- Evidence: A1's font-metric estimate (cycle 1): the grid table needs about 1109 px against a 944 px box at 1024 px.
- Page-image check: at 1024 px, are all eight columns of the grid visible without scrolling?

### V09 Label tracking differs for one role (severity 4, valid; owner foundation)
- Evidence: the uppercase labels at 15.3 px use 0.14 em (kicker, question number) and 0.12 em (filters, related
  statements, search groups).

## Visual acceptance checks (precommitted; added to EVAL-PLAN.md)

| Id | Check | Evidence | Pass |
|---|---|---|---|
| VQ1 | Page image at 1400, 1024, 768, 480 and 375 px, light and dark, beside the best exemplars root names (until named: beside the baseline and the site's strongest pages) | native Chrome screenshots of task-owned tabs, judged by the lead and an independent reviewer | rhythm, harmony, balance and proportion judged on the image, each failure named with its location |
| VQ2 | Measure | characters per line counted on the image, cross-checked with the font-metric estimate | prose and statement text 60 to 75 characters at 768 px and wider |
| VQ3 | Type levels | the declared scale and the image | every heading level distinguishable at a glance; no two roles of different level within 5 percent in size |
| VQ4 | Rhythm | spacing tokens and the image | margins, paddings and gaps come from one scale; equivalent gaps look equal |
| VQ5 | Status legibility | simulated colour-vision deficiency and zoomed marks at 1x | every pair that appears together either differs by CIEDE2000 10 or more under each simulation, or is told apart by shape at its rendered size |
| VQ6 | The totality | the atlas or map view on the image, plus Q24 | one view shows the programme's domains, results and their relations with status, faithful to the data, keyboard-reachable, with a text equivalent |
| VQ7 | Print | print preview on A4 and Letter | Q21 holds and each printed page reads as composed |
