# G1–G3: the Gaussian figure's readout, caption formulas and labels (atlas lane)

Written 17 November 2026, about 04:00 WIB. This is a successor to the installed five-model set. It fixes the native findings G1–G3 in IMAGE-05-375css-iframe-release-v4-light.md (90cf8b79…).

**What changed.** No manifest or chapter file and no scientific word changed. The repairs are:

- **G1.** An authored integral over the real line that is a constant (the density's 1) is now written once, under the figure's label "Integral over the real line". It used to read "1 = 1". Every other integral is still its authored formula and its value at the parameters.
- **G2.** Where an authored caption spells one of the record's own formulas in plain text, that formula is typeset like the figure's equations.
  - In the density caption, "-cx/b" and "ħ/b" are the record's `conditional_mean` and `conditional_variance`.
  - Only the record's formulas are matched, whole and at least three characters long; every other character stays as written.
  - The change applies to the Gaussian figure only, where it was shown.
- **G3.** Inside a figure, the host page's paragraph rules no longer apply: the `p + p` first-line indent, justification and `p` margins.
  - This is done in figures.css with selectors that outrank the host's rules, whatever the order of the stylesheets.
  - The "Integral over the real line" label is now the same element as "Parameters".

**Apply** (from the root of the integration tree; the patch changes five files):

    python3 <this folder>/check_figures_g.py --before
    git apply <this folder>/figures-g1-g3.patch      # a76ae2866d5c503361d1eb40606a2847b96ad470a1b6985b4ed1349cd6e58be0
    python3 <this folder>/check_figures_g.py --after

- **Changed:** figures.py, figures.css and three test files. figures.js and figures_page.py are unchanged.
- **Hashes:** hashes.txt lists them all.
- **Tested:** the patch applied cleanly to a copy of the installed files.

**Evidence (checks.txt).**
- **Unit tests:** 28 of 28 pass, with the author's live manifest.
- **jsdom:** all pass, on the fixture page and on the live records.
- **Candidate build:** root's integration tree, copied, with the repair applied.
  - The audit raises no failure, and MathML has 0 errors.
  - G1, G2 and G3 were verified in the built markup and the page's own CSS.
  - The five figures run live under the reader with no script errors.
- **Not judged here:** the page image. Native QA checks it.
