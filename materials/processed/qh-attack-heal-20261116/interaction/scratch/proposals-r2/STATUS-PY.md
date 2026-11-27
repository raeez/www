# Proposals for the foundation owner (status.py, status.css, status-print.css)

The interaction lane does not edit these files. Each proposal below is an exact patch, guarded by the hash of the file it
applies to. status.js works without any of them; with them, the same behaviour also holds without the script, and the
script's new states are styled.

## Files

| Patch | Applies to | sha256 before | sha256 after |
|---|---|---|---|
| `status-py-against-baseline.patch` | baseline `compiler/quantum-holography-status/status.py` | `7e00aab95067023c4b686723227c7f3de17ebab5759ca87e95d46f1ff8a72fc9` | see `after-baseline/status.py` |
| `css-against-baseline.patch` | baseline `status.css` and `status-print.css` | `c83ccb31…a1b0`, `c1e6560a…6015` | see `after-baseline/` |
| `css-against-foundation-snapshot.patch` | foundation snapshot `status.css` and `status-print.css` (copied 2026-11-16T12:18Z) | `33073f8f…dda9`, `01bdf76e…8016` | see `after-foundation/` |

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

## P3. Serve what a mark and a term mean as their description (A2-B-20)

Each `.cell-note` gets the id `<row id>-<column id>-scope` and its button `aria-describedby` to it; each glossary
`dd` gets `<term id>-def` and every term button `aria-describedby` to it. Ids are the ones status.js gives when they
are absent. Checked: 160 marks and 334 terms described; audit passes (the audit checks every `aria-describedby`).

## P4. TeX-free names for the marks (A2-B-19)

The cell button's `aria-label` uses `strip_tags(self.math_free(row name))`. The foundation snapshot already serves
TeX-free names; the hunk is given for the baseline. status.js also removes TeX delimiters from such names at start.

## P5. Not patched here (proposal only)

- Terms and marks as links (`a.term[href="#term-…"]`, marks linking to their row) so that no control is inert without
  the script (A2-B-21). status.js already handles `.term` and `.cell-btn` of any element type and prevents the link
  when it opens the card.
- Comments in status.css and status-print.css that name files or the build (A2-B-26).
- Forced-colours states for pressed chips, the open mark and the current bar link are in the CSS block (A2-B-22).

## Evidence for the whole set

`integration-py/` = baseline producer + `after-baseline/status.py`, `status.css`, `status-print.css` + this lane's
status.js: audit PASS, `tools/fidelity.py` PASS (statements, statuses, cells, tally identical; every baseline and
live-edition id kept), reader-task tests: see `verify/verify-all.log`. No browser was used (RESTRICTION-BROWSER.md),
so how the CSS looks is not verified.
