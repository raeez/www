# Proposals for the foundation owner (status.py, status.css, status-print.css)

The interaction lane does not edit these files. Each proposal below is an exact patch, guarded by the hash of the file it
applies to. status.js works without any of them; with them, the same behaviour also holds without the script, and the
script's new states are styled.

## Files

| Patch | Applies to | sha256 before | sha256 after |
|---|---|---|---|
| `status-py-against-baseline.patch` (`da407d9b…c6`) | baseline `compiler/quantum-holography-status/status.py` | `7e00aab95067023c4b686723227c7f3de17ebab5759ca87e95d46f1ff8a72fc9` | `after-baseline/status.py` `8780b4ede222c0cd631f65fcb0bb9c0d586ef0a6c97d7d82dd30a11407756ee9` |
| `css-against-baseline.patch` (`76dccb05…b796`) | baseline `status.css` and `status-print.css` | `c83ccb31…a1b0`, `c1e6560a…6015` | `after-baseline/status.css` `50945cc9…8753`, `status-print.css` `3c3488c8…b16b` |
| `css-against-foundation-snapshot.patch` (`d2cb6472…76b9`) | foundation snapshot `status.css` and `status-print.css` (copied 2026-11-16T12:18Z) | `33073f8f…dda9`, `01bdf76e…8016` | `after-foundation/status.css` `91e87263…035b`, `status-print.css` `fb6a36d8…0071` |

Revised after the second review (cycle 2) and the native QA of the foundation candidate: the CSS block (edge fades for scrolling boxes, legend help, lit cells by a ring alone (no tint, no fading) so
that no mark falls below 3:1, a crosshair centre that differs from a lit cell, print resets), P3 (a mark is described
by its scope paragraph only) and the new P6 (the search's place with the page's interface words). `patch --dry-run`
applies all three patches to the baseline files.

The CSS patches only append two blocks (`status-css-block.css` to status.css, `status-print-css-block.css` to
status-print.css), so they apply to any later revision of those files: append the same blocks. The status.py hunks
are written against the baseline; the foundation's current status.py (snapshot sha256 `0bf52f9c…7a2c`) has the same
functions and needs the same edits placed in them.

## P1. Serve an address for every statement (A1-M-02, A1-A-08)

`statement_id()` gives a statement without a content id the address `s-` + `ident(title)`, de-duplicated with `-2`,
`-3` … in page order after reserving every content id. This is the rule status.js applies at run time, so links made
with or without the script are the same. Checked: with the patched status.py the served ids equal the ids status.js
gives, for all 281 statements in order (`scratch/probe-served-ids.cjs`: "served without id 0, identical ids in order
true"). Alternative: the content owner adds ids to the 98 statements (the foundation contract lists this under
content); then this hunk is unnecessary and status.js gives no ids.

## P2. Serve script-only controls hidden (A1-A-26, A2-B-21)

`.row-tools` (Show filter, Open all, Close all), the theme button and the grid hint ("Select a mark …") are served
with `data-needs-script hidden`; status.js shows them. Requires the CSS rule `[data-needs-script][hidden] { display:
none !important; }` (in the CSS block), because the author `display` rules of these elements otherwise win over the
`hidden` attribute. Checked without the script: all three hidden.

## P3. Serve what a mark and a term mean as their description (A2-B-20; revised for C2-B-15)

The scope paragraph of each `.cell-note` (not the whole note, whose head repeats the status and the column the name
already says) gets the id `<row id>-<column id>-scope` and its button `aria-describedby` to it; each glossary
`dd` gets `<term id>-def` and every term button `aria-describedby` to it. Ids are the ones status.js gives when they
are absent. Checked: 160 marks and 334 terms described; audit passes (the audit checks every `aria-describedby`).

## P4. TeX-free names for the marks (A2-B-19)

The cell button's `aria-label` uses `strip_tags(self.math_free(row name))`. The foundation snapshot already serves
TeX-free names; the hunk is given for the baseline. status.js also removes TeX delimiters from such names at start.

## P6. Serve the search's place with the page's interface words (C2-A-07)

After the tally, status.py serves `<div data-find data-needs-script hidden data-label-<key>="…">`, one attribute for
each entry of a new page.json object `"interface"` (keys: CONTRACT.json `served_hooks.label_keys`). status.js builds
the search inside it and takes its words from these attributes, so a successor that renames its parts ("families" for
"examples", say) renames the filter line, the row notes, the legend line and the placeholder with them. Without the
object the mount is served bare and the script's own words stand. Checked: the reader-task test "interface words
served with the page replace the script's own" (a served mount with a placeholder and a filter-line sentence).

## P2b. Proposal only: split the grid hint (C2-A-12)

P2 serves the whole grid hint hidden, but its second sentence ("On a narrow screen the table scrolls sideways.") is
true without the script. page.json's owner splits `grid_hint` into the script-only sentence and `grid_scroll`; status.py
serves `<p class="grid-hint"><span data-needs-script hidden>{grid_hint}</span> {grid_scroll}</p>`.

## P5. Terms served as links (native QA F6; A2-B-21)

A `<button>` lays out as an inline-block whatever its CSS says, so a multi-word term cannot break across lines and drops
whole to the next line, leaving a short line (native QA F6, shot E10). Served as a link, the term is inline and breaks
like the text around it, and without the script it leads to its definition. Exact change in the foundation's current
status.py (sha256 `b960b6683a6d71cd4e1ff82d2c0b6579b83b3d5923a30d8a8b1a3861be886713`, the term renderer `one()`):

```
-            return (f'<button type="button" class="term" data-term="{tid}" aria-haspopup="dialog" '
-                    f'aria-expanded="false" aria-controls="card">{m.group(1)}</button>')
+            return (f'<a class="term" href="#{tid}" data-term="{tid}" aria-haspopup="dialog" '
+                    f'aria-expanded="false" aria-controls="card">{m.group(1)}</a>')
```

The foundation's `.term` rule (`display: inline; border: 0; background: none; cursor: help; …`) already styles any element
with the class; a link may also want `color: inherit`. status.js needs no change: it opens the card on click or Enter
without following the link, returns focus on Escape, and its in-page link handler leaves a term link alone. Checked on
the current build with every term served as a link: reader-task test "card: a term served as a link opens its card
while the script runs, and leads to its definition without it". This removes 334 of the 502 controls that do nothing
without the script. The 160 marks and 8 column heads could link to their row line and column definition in the same way
(not patched here).
- Comments in status.css and status-print.css that name files or the build (A2-B-26).
- Forced-colours states for pressed chips, the open mark and the current bar link are in the CSS block (A2-B-22).

## Evidence for the whole set

`integration-py/` = baseline producer + `after-baseline/status.py`, `status.css`, `status-print.css` + this lane's
status.js: audit PASS, `tools/fidelity.py` PASS (statements, statuses, cells, tally identical; every baseline and
live-edition id kept), reader-task tests: see `verify/verify-all.log`. No browser was used (RESTRICTION-BROWSER.md),
so how the CSS looks is not verified.
