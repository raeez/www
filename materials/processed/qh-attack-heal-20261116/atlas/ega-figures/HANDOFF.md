# Five interactive figures: frozen handoff (atlas lane)

Frozen 17 November 2026, about 02:45 WIB. This replaces the earlier two-model handoff (figures-files.patch b28e07b0).

**Scope.**
- In scope: the five interactive mathematical models in `manifest.figures[]`.
- Not in scope: the static diagram records in `manifest.diagrams[]`. Foundation draws those, by root's ruling. Two contract findings for foundation are in DIAGRAM-FINDINGS.md.

**Governing inputs.**
- FIGURE-RECORD-CONTRACT.md d711aac0…
- SCIENTIFIC-VISUAL-CONTRACT.md cc340b38…
- The author's manifest a8dd97f6790f553f36a64442e6ecc0d772fe482baff8e5a9aa7e99cab305086b. A copy is at preview/manifest-snapshot.json.
- The benchmark audit's EGA-APPLICATION-CROSSWALK.md 1189905e…

## Apply

All paths are relative to `materials/processed/qh-attack-heal-20261116/atlas/ega-figures/five-models/`. Run them from the root of the tree that receives the patch.

    # a tree without figure files (root's integration tree today)
    python3 check_figures.py --before-new
    git apply figures-files.patch                 # 50dcb17fc2effa80cd404f274063de94806aac8ece9aca28704ea87d3a81e40d
    python3 check_figures.py --after

    # a tree holding the earlier set b28e07b0 (foundation's staging copy holds it)
    python3 check_figures.py --before-delta
    git apply figures-delta-from-b28e07b0.patch   # 68ff649dbb663c3557059ee5d345742f9e2ecc7e8b46961a38fa70d48ab9b3af
    python3 check_figures.py --after

- **Guard:** check_figures.py 063555c8dcd065e887d7c22c5c5e124d3b42807e2b08acf442e1b1b104a98556. It reads figures-hashes.txt and earlier-hashes.txt beside it.
- **Tested:** both routes were applied on clean trees and passed --before and --after.
- **Nothing else changes:** the patches only create these seven files or replace the earlier versions.

| File | sha256 | bytes |
|---|---|---|
| compiler/quantum-holography-status/figures.py | 2b86921f9dea8a3dad4f25d8a33c2d8ba4b2784925702bee201e730810c1f90f | 58572 |
| compiler/quantum-holography-status/figures.css | 0c68828bcf65b3c63c4533e79e5b4af13150fe09bc1ea1a5757d576518381301 | 14608 |
| compiler/quantum-holography-status/figures.js | bce4e5493125523e7cc10b3fb868a1ebd5416fb38f5c1a83494020a9d7121793 | 13814 |
| compiler/quantum-holography-status/tests/test_figures.py | 2582076e2d96d2306c4c40cb06bc19d0f68c66098ca06f6a44aadcb24c218170 | 17578 |
| compiler/quantum-holography-status/tests/figures.test.cjs | 2e843e9d01e0611584bf9adfe18986f2b6207c3bcf8a40bf94908554ed90bd12 | 9316 |
| compiler/quantum-holography-status/tests/figures_page.py | 8ac23dc036107435dc8adba1fc2c5e0a7d79e9f75fbffe6e13614f66bf30a73a | 2413 |
| compiler/quantum-holography-status/tests/fixtures/figures-synthetic.json | 1e54e9ea12b310a7fc061191407c6cc2f5c8a27bfbe37ee4c01c1596d10f3ff2 | 10907 |

## Interface (unchanged call)

- **Render:** `figures.render(record, ctx)` returns `{'html', 'problems'}`, and `figures.assets()` returns `{'css', 'js'}`. Foundation's staged `monograph.py` already calls both, unchanged.
- **ctx:**
  - Required: `ctx.rich(text, terms=False)`, the page's TeX renderer.
  - Optional: `ctx.words`, a dict that replaces any interface word listed below. It works like the reader's `data-label-*`.
- **The element:** `<figure class="qh-fig" id="<id>" data-figure="<id>" data-qh-figure="<id>" data-figure-type data-figure-model data-figure-chapter data-figure-section data-config>`.
  - The id is the manifest id verbatim, and it precedes data-figure, which is the order foundation's check expects.
- **Changes from b28e07b0:**
  - **Attribute rename.** `data-chapter` and `data-section` are renamed `data-figure-chapter` and `data-figure-section`. `reader.js` selects `[data-chapter]` and `[data-section]` as its own chapters and sections, so the old names would have made every figure a chapter.
  - **Figure title.** The title carries `data-block-title`, which is what the reader's search and reminders use as the figure's name.
  - **Unnumbered equations.** An equation anchor whose key is not a printed number (two-term-complex, tensor-map) now links under the interface word "Equation".

## What each model draws

Every word, formula, matrix, rule and state in a figure comes from the record. Prohibited inferences are respected in the drawing and are not printed. A record the component cannot honour fails the build with its problem named, and draws nothing.

- **gaussian-elimination (ch01).**
  - **Controls:** five authored controls inside their windows. A value that breaks the validity rule is refused, the authored message appears, and the previous valid tuple stays.
  - **Profiles:** three curves, none filled, each with its own authored integral (1, √(2πħ/b) and Z_y(x)).
  - **Mean:** the density carries its conditional-mean line, with the authored label attached.
  - **Removed:** the earlier ±1 standard-deviation band. It had no authored label.
- **two-expansions (ch01).**
  - **Regions:** the two authored regions in the w-plane. The chosen region is labelled with its own condition.
  - **Pole:** the pole carries its authored label, and no value is drawn at it.
  - **No truncation control.**
- **cohomology-jump (ch05).** The complex is drawn on its authored basis.
  - **Selector:** buttons for t = −1, t = 0 and t = 1.
  - **First arrow:** it ends at v₁ where the state's matrix entry is nonzero and at 0 where it is zero. Both are solid, because both are defined maps.
  - **Contraction:** where the state gives a formula, it is drawn back from v₁ to u₁ with that formula. At t = 0 it is absent, with the state's sentence.
  - **Surviving basis:** the state's surviving vectors are ringed. The same rings mark the vectors' names in a table of all three states' dimensions and Euler characteristics.
  - **Checks:** the record's arithmetic (rank, dimensions, χ, the basis) is checked and returned to the author if it disagrees.
- **infinite-rank (ch08).**
  - **Grids:** D⁽ᴺ⁾ (with the authored control N) and the identity sit side by side in the same authored 8×8 viewport. Each cell holds its entry by the authored rule.
  - **Edges:** the bracket opens only on the left. The ⋱ mark carries the accent where the rule gives 1 beyond the viewport.
  - **Table:** under the grids sit the convergence sentence and a table of rank and the two memberships, with yes/no for each.
  - **No state control:** the `state` control is permitted but unused, because both states are shown.
- **adjunction-triangles (ch06).**
  - **Key:** F, G, η and ε in the record's words, with the domain sentence. That sentence says the chapter writes Φ and Ψ for F and G.
  - **Triangles:** both triangle identities are drawn as commutative triangles, side by side, each with its authored equation and meaning.
  - **Colour coding:** arrows and symbols built from the unit carry the unit's colour. Pressing the unit or counit key picks out its arrows.
  - **Criteria:** the three authored criteria are in a table of hypothesis and equivalent statement.

**Marks.** No dashed line is used in these figures; dashes stay reserved for open comparisons. Colour never carries a distinction alone.

## How A01–A08 reach these components

| | Realization | View, state and evidence |
|---|---|---|
| A01 | Each figure follows the chapter's own sequence: it sits after the display it illustrates and links back to it. | In the built book, the links from figures to equations resolve, unnumbered displays included (checks.txt, in-book check). |
| A02 | Each figure is placed in its own chapter and section. The whole-programme master view belongs to foundation's diagrams (context records). | In the built book the five figures sit inside articles ch01, ch05, ch06 and ch08. No figure is taken for a chapter (18 chapters; 0 figures among them). |
| A03 | Identifiers stay the same across views: the id is verbatim and the title is the reader's name. Symbols match the chapter: u₁ and v₁ as in d_t, D⁽ᴺ⁾, and η_X with the Φ/Ψ sentence. Survivor rings mark the vectors in both drawing and table, and the unit's colour marks the same symbol in the key, the equation and the arrows. | Unit tests `test_identity_hooks_and_reader_vocabulary` and `test_two_triangles_their_arrows_and_the_key`. The jsdom cohomology test checks that rings, row and list item move together. |
| A04 | The figures add no status vocabulary. Equivalences and full faithfulness appear only as the author's criteria. | test_figures.py `Adjunction.test_criteria_and_domain` |
| A05 | Every mark is literal: solid arrows are defined maps, with nothing dashed, nothing filled, and no unlabelled band. Every label sits on its mark: the mean, the region, the pole, the arrows and the degree columns. | `test_marks_keep_their_meaning` (no stroke-dasharray, band or area). `test_labels_attached_to_their_marks`. |
| A06 | Hypotheses and domains stay visible beside each drawing: the validity domain and message, the complex's domain, V and its completion, and the categories. The authored captions are kept. | `test_every_authored_word_verbatim_and_nothing_invented`; the InfiniteRank `test_ranks_memberships_and_words`. |
| A07 | **States:** the initial state, every authored state, the refused tuple with its message, keyboard operation (native buttons and range inputs with focus rings), the static page without the script and in print (every state's text shown), forced colours, and reduced motion. **Layout:** it follows the figure's own width (container queries), and labels are never enlarged past their set size. | jsdom: 9/9 on three pages, and in the built book with reader.js (no script errors). The native look and keyboard use are for the QA owner. |
| A08 | Exact identities: file hashes, the guard, the author-manifest hash, the preview hashes and the build used for the in-book check. | five-models/checks.txt 5038c31026ecae6cdd054f5ee15167311e1138bf0376575a24ce6f6aea203ed6. None of this is product acceptance. |

## Checks (five-models/checks.txt)

- **Unit:** 25/25 tests, both in this worktree and in a copy of root's integrated compiler with its audit.py, with no test skipped. They include all five of the author's live records, and they assert that every authorized model has an authored record.
- **jsdom:** 9/9 tests on each of three pages:
  - preview/fixture.html 78072ec6…
  - preview/manifest-plain.html 7c7b24ac…
  - preview/manifest-mathml.html 63bdb281…, typeset by root's integrated renderer (MathML).
- **In-book:** a copy of foundation's staged monograph source (read only), with these files, the author's chapters and the manifest snapshot, built without errors (MathML errors: 0).
  - All five figures are placed in their chapters and become live under reader.js with no script errors.
  - The reader counts 18 chapters and treats no figure as a chapter or section.
  - All 7 figure links resolve.
  - The controls work in place.
  - The build's only figure failure was the diagram fig-state-line-cap, whose drawing belongs to foundation.
- **Not done here:** no page image was judged in this lane, under root's restriction on browser, headless and CDP rendering. The visual judgment against the exemplars belongs to native QA on the integrated candidate.

## Interface words, for the author to confirm or replace (ctx.words)

These are the only words the figures add to the records:

| Key | Word |
|---|---|
| controls | Parameters |
| outputs | Values at these parameters |
| equations | Equations |
| equation | Equation |
| integral | Integral over the real line |
| yes | yes |
| no | no |
| hypothesis | Hypothesis |
| equivalent | Equivalent statement |

## Returned to the author (no change made in the record)

- **Unlabelled band:** a band for one standard deviation would need an authored label, so it is not drawn.
- **Equation anchor keys:** fig-cohomology-jump and fig-infinite-rank key their equation_anchors by name, not by printed number. They link under "Equation".
- **Contraction arc:** in cohomology-jump the arc is drawn exactly where the state's matrix entry is nonzero. This follows the chapter: for t ≠ 0 the summand is contractible. A per-state boolean in the record would make that explicit.

## Still open (atlas lane)

- **C5:** one mark system across the atlas and the reader. It waits on foundation's agreement to the existing `ctx.mark`.
- **Master figure:** a master atlas figure linked to root's `atlas_ref`, once root supplies it.
