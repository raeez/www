# Hunk index of QUALITY-ON-F1F2.diff (against the foundation's final F1+F2 bytes)

## compiler/quantum-holography-status/status.py (20 hunks)

1. `@@ -13,6 +13,7 @@`: import for _MathText
2. `@@ -99,10 +100,18 @@`: text forms: Math.add_text with deduplicated text jobs (A2-A2-02, A3-F-13)
3. `@@ -115,10 +124,14 @@`: text forms: substitute() fills text placeholders; keeps the wide-formula width hint (A3-F-01)
4. `@@ -129,7 +142,7 @@`: text forms: placeholder pattern for text jobs
5. `@@ -209,6 +222,66 @@`: text forms: _MathText and math_text, structured MathML text (A3-F-01)
6. `@@ -233,13 +306,25 @@`: glossary: explicit ids reserved first; named problems for equal ids and taken anchors (C19, A2-A2-03, A3-F-08)
7. `@@ -333,16 +418,17 @@`: rich()/plain() with markup=False (A2-A2-11)
8. `@@ -360,14 +446,27 @@`: rich()/plain() with markup=False (A2-A2-11); text forms: Build.text_form for attributes and titles (A2-A2-02)
9. `@@ -419,7 +518,10 @@`: hypotheses must be a list of non-empty texts (content contract)
10. `@@ -837,7 +939,7 @@`: column heads: name or short label set as mathematics (A3-F-07)
11. `@@ -855,7 +957,7 @@`: grid marks: accessible names from text forms (A2-A2-02, A3-F-01)
12. `@@ -864,15 +966,15 @@`: cell notes, row link title and column definitions: mathematics and text forms (A3-F-07, A2-A2-02)
13. `@@ -903,7 +1005,7 @@`: row lines: column names set as mathematics (A3-F-07)
14. `@@ -936,8 +1038,12 @@`: open groups: explicit ids; anchors taken by the section fail with a named problem (C19, A2-A2-03)
15. `@@ -956,16 +1062,15 @@`: essay: TeX as mathematics, display rule only without TeX, title as mathematics (C03, A2-A2-01, A3-F-07)
16. `@@ -996,7 +1101,10 @@`: essay.md missing: warning; glossary problems reach the build (C02, A2-A2-03)
17. `@@ -1034,7 +1142,7 @@`: contents list: the essay title as mathematics (A3-F-07 on the foundation's contents)
18. `@@ -1085,6 +1193,8 @@`: page title and description: text forms (A3-F-09)
19. `@@ -1103,8 +1213,8 @@`: page title and description: no tag stripping of formula text (A3-F-09)
20. `@@ -1157,7 +1267,7 @@`: fonts: byte-reproducible subsets (C28)

## compiler/quantum-holography-status/status.css (3 hunks)

1. `@@ -207,6 +207,8 @@`: a status outside the list (drafts only) in a neutral colour
2. `@@ -692,7 +694,7 @@`: comment reworded: no source-file name (audit A3-F-02)
3. `@@ -761,7 +763,7 @@`: comment reworded: no source-file name (audit A3-F-02)

## compiler/quantum-holography-status/status-print.css (1 hunks)

1. `@@ -1,11 +1,11 @@`: print comments reworded: no source-file names (audit A3-F-02)

## compiler/quantum-holography-status/audit.py (8 hunks)

1. `@@ -1,74 +1,174 @@`: audit rules and imports after cycle 3 (A3-F-02/03/04/10/11, A4-F-01/02/06/08, A5-F-03/04)
2. `@@ -80,8 +180,8 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)
3. `@@ -91,6 +191,173 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)
4. `@@ -109,6 +376,12 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)
5. `@@ -139,41 +412,106 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)
6. `@@ -192,6 +530,7 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)
7. `@@ -201,7 +540,8 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)
8. `@@ -211,9 +551,13 @@`: audit delta after cycle 3 (A3-F-02/03/04/05/10/11/13, A4-F-01..08, A5-F-01..04; refuted form without hypotheses fails)

