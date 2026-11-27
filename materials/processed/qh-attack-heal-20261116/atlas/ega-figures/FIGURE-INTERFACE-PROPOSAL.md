# Figure components for the reader: exact interface (v2, after root's decision of 17 Nov)

This version supersedes the "kinds" of v1 (kept below for the record).

## Root's decisions

- **Ids.** The manifest figure id is the DOM id verbatim. Ids such as fig-gaussian-reduction already carry their
  prefix; none is added.
- **Placement.** Figures are placed by the one-line hook `::: figure <figure-id>`.
- **Who draws.** Foundation parses the hook and calls the atlas lane's figures.render. Foundation draws no model
  itself.
- **Element.** Interaction finds a figure by figure[data-figure][id]. The atlas lane also writes data-qh-figure.
- **Models.** Five models are authorized. Domains of composition is not yet authorized; it needs an authored finite
  state table first.

## The element figures.render returns, for a manifest record r

    <figure class="qh-fig" id="{r.id}" data-figure="{r.id}" data-qh-figure="{r.id}" data-figure-type="{r.type}"
            data-chapter="{r.chapter_id}" data-section="{r.section_id}">
      <figcaption class="qh-fig-head">{r.title}</figcaption> ... controls, values, drawing ...
      <p class="qh-fig-caption">{r.caption}</p>
    </figure>

title and caption are rendered verbatim through ctx.rich. equation_refs are shown as the chapter's equation numbers,
for example (1.1), and link to them when the reader gives them anchors.

## The records as they now stand (type authored_formula)

1. **A parameter model**, such as fig-gaussian-reduction. It has `parameters` (name to type), `domain` (an
   inequality), `outputs` (name to formula), `permitted_controls` and `prohibited_inferences`.
   - The component offers a control only for a permitted parameter.
   - It keeps every state inside the parameter types and the domain.
   - It evaluates every output from its authored formula.
   - It shows the formula and its value under the output's own name. Every parameter is kept, including x and ħ.
   - The drawing shows exactly the outputs. For the Gaussian these are:
     - the conditional distribution of y at the chosen x: its mean, its variance, and the normalization as its area;
     - the remaining weight in x with its effective stiffness.
   - Nothing is drawn that the record prohibits, such as the mean substituted as the integral.
2. **A state model**, such as fig-local-expansions. It has `states` (id, condition, series) and `domain`.
   - The control switches only between the authored states.
   - The chosen region is drawn and the series shown.
   - The pole on z = w is drawn and given no value.
   - No truncation control is offered, since the record prohibits treating a truncation as the series.
3. **Formulas** are authored in a plain linear syntax ("a-c^2/b", "sqrt(2*pi*hbar/b)",
   "sum_(n>=0)(n+1)*w^n/z^(n+2)"). The component parses them once and typesets them (a - c²/b, √(2πħ/b),
   Σₙ≥₀ (n+1) wⁿ/zⁿ⁺²) without changing a symbol. The unparsed string is kept in the element for checking.

## Interface gaps (for the author, through root)

- **Initial value and range for each control.** The records give types ("real", "positive real; default1") but no
  ranges. Until the author supplies `initial` and `range` per parameter, the component uses a=2, b=1, c=0.5, x=1,
  ħ=1 (inside ab > c², b > 0, ħ > 0) and ranges a, c, x in [-3, 3] and b, ħ in (0, 3]. These are presentation choices
  only, and the author can replace them.
- **Reader names for outputs.** Outputs are named by their keys (effective_stiffness, ...). The component shows the
  key with spaces ("effective stiffness"), the chapter's own term. The author may supply `labels` instead.
- **Equation anchors.** For equation_refs to link, foundation needs to give the chapter's tagged equations ids, for
  example eq-1.1.

---

## v1 (superseded in part by the decisions above)


Status: proposal for root to route to foundation (reader) and to the author (/root/programme_claims_inventory). It
adds no mathematics. It follows SCIENTIFIC-VISUAL-CONTRACT.md and READER-ARCHITECTURE.md
(/tmp/qh-ega-exposition-20261117/coordination) and the manifest schema qh-reader/v1. Every mathematical word a figure
shows (captions, labels, parameter restrictions, state names, theorem references) comes from the author's record and
is never paraphrased. The atlas lane writes only layout, drawing, interaction and the computations that the contract
itself states, such as the factor √(2π/b).

## 1. Who writes what

| Piece | Owner | Where |
|---|---|---|
| Chapter prose, figure placement, figure records (all text, parameters, states, diagrams) | author | chapters/*.md, reader-data/manifest.json `figures` |
| Reader page: parts, chapters, sections, navigation, theorem and definition blocks, TeX | foundation | monograph.py, monograph.css, reader.js (not edited by this lane) |
| Figure validation, static drawing (no script, print) and interaction | atlas lane | compiler/quantum-holography-status/figures.py, figures.css, figures.js and their tests |
| Atlas (second reading mode) | atlas lane | atlas.py, atlas.css, atlas.js (unchanged by this proposal) |

## 2. The hook in chapter Markdown (author writes it; foundation parses it)

A paragraph consisting of exactly one line

    ::: figure <figure-id>

places the figure with that id from manifest.json `figures` at that point in the chapter. `<figure-id>` matches
`^[a-z0-9]+(-[a-z0-9]+)*$` and is unique in the manifest. Foundation replaces the line with the HTML returned by
`figures.render(record, ctx)` (section 4). Foundation includes figures.css and figures.js once per page, after its
own stylesheet and script, as it does for the atlas. A chapter with no figure line needs neither.

## 3. Figure records (manifest.json `figures`, author-supplied)

Common fields:

| Field | Type | Meaning |
|---|---|---|
| `id` | string | stable id, as in the chapter line |
| `chapter_id` | string | the chapter that places it (`ch01` ... `ch18`) |
| `kind` | string | one of the kinds below; no other kind is drawn |
| `title` | string, optional | heading of the figure, TeX allowed |
| `caption` | string | the claim the figure makes, TeX allowed; shown under the figure, never shortened |
| `labels` | object | every visible word of the figure by key, TeX allowed (keys per kind below); a missing key is a build problem, never invented |
| `atlas_ref` | object, optional | `{ "claims": [...], "comparisons": [...], "paths": [...], "domains": [...] }` atlas ids, when root supplies them |

Kinds (the six interactive models of the visual contract, plus two static kinds):

1. `gaussian-elimination`: `params`: `{ "a": R, "b": R, "c": R }` with `R = { "min", "max", "step", "initial" }`.
   - The component keeps every state inside b > 0 and ab > c² (a control that would leave the region is held at its
     boundary, which is never reached).
   - It shows S(x, y), the factor √(2π/b), the effective coefficient a − c²/b, the eliminated fluctuation and the
     normalization, each named by `labels`.
   - `labels` keys: `form`, `factor`, `effective`, `fluctuation`, `normalization`, `a`, `b`, `c`.
   - No line y = 0 or y = −cx/b is drawn as the integral.
2. `two-expansions`: the model (z − w)⁻² is fixed by the kind.
   - `truncation`: `R` (number of terms).
   - The component shows the expansion in the selected domain (|w| < |z| or |z| < |w|), the domain itself, and the
     truncation as an approximation. The collision view draws the pole and the diagonal and gives no value at z = w.
   - `labels` keys: `inner`, `outer`, `truncation`, `diagonal`, `pole`, `series`.
3. `cohomology-jump`: the complex ℂ² → ℂ² (diag(t, 0)) in degrees 0 and 1 is fixed by the kind.
   - `states`: an ordered list of `{ "id", "t": "0" | "nonzero", "label" }`.
   - The component shows the map, H⁰ and H¹ with their dimensions (2, 2 at t = 0; 1, 1 at t ≠ 0) and the Euler
     characteristic 0.
   - `labels` keys: `h0`, `h1`, `euler`, `map`.
4. `tensor-completion`: `truncation`: `R` (size N of the finite grid).
   - The component shows the N × N truncation of the diagonal, an algebraic tensor as a finite sum of elementary
     tensors, and a completion containing the infinite diagonal. It animates no limit.
   - `labels` keys: `algebraic`, `completion`, `truncation`.
5. `adjunction`: `objects`: `{ "C", "D", "F", "G", "unit", "counit" }` (TeX).
   - `states`: an ordered list of `{ "id", "label", "caption" }` among `triangles`, `fully-faithful` and
     `equivalence`, authored.
   - The component draws F, G, η and ε and reveals each triangle identity on its own.
6. `composition-domains`: `cases`: an ordered list of `{ "id", "label", "caption", "nodes", "arrows" }` in the form of
   kind 7. The control switches only between authored cases and draws nothing between them.
7. `diagram` (static): `nodes`: `[{ "id", "tex", "col", "row" }]` on an integer grid; `arrows`: `[{ "from", "to",
   "tex", "kind", "ref", "domain", "hypotheses" }]`. The arrow kinds follow the contract:
   - `map` is a solid arrow (an actually defined map).
   - `equivalence` is a solid arrow with the equivalence mark; `ref` names the theorem and `domain` is displayed.
   - `open` is a distinct, dashed arrow labelled with `labels.open` (for example "Open problem"), its source and
     target still explicit.
   - `obstruction` is drawn with its fixed `hypotheses` and leaves neighbouring arrows drawn.
   - Colour never carries truth alone; each kind also has its own stroke and mark.
8. `programme-figure` (static, the master figure): the atlas domains and the chapter's `atlas_ref`. The same figure
   recurs in every chapter that places it, with the chapter's references emphasized and the rest quiet. It is drawn
   from atlas.json, so it shows only recorded relations.

## 4. Render contract (atlas lane)

`figures.render(record, ctx) -> { "html", "problems" }`, with ctx the reader's context (`rich` for TeX, `anchor_for`
for theorem references).

The html is one element:

    <figure class="qh-fig" id="fig-<id>" data-qh-figure="<id>" data-kind="<kind>">
      <div class="qh-fig-stage">  static SVG and values of the initial state (no script, print)  </div>
      <figcaption> caption, rendered by ctx.rich </figcaption>
    </figure>

figures.js adds the controls (range inputs and buttons, keyboard-operable, values announced politely) to every
`[data-qh-figure]` on the page. Without the script, or in print, the initial state is complete and readable.

**Problems (each fails the build, naming the figure and the field):**
- an unknown kind or field;
- a missing label key;
- an initial value outside the stated region;
- a state or case that is not authored;
- an arrow whose endpoint is not a node;
- a reader-rule hit in any text.

## 5. What the reader needs to place figures

1. Parse the one-line hook (section 2), and include figures.css and figures.js once.
2. Pass `ctx.rich` and `ctx.anchor_for` as for the atlas.
3. Keep `fig-<id>` anchors stable, so a cross-reference to a figure keeps the reader's place.

## 6. The method taken from the exemplars named by the principal (Hainan, pages 01, 02, 03 and 14)

The exemplars' method is taken over; their palette and map are not copied.
- **One master figure that evolves through the argument.** The programme figure recurs. Each chapter emphasizes only
  what its question needs, as the exemplar's network map recurs with one route emphasized and returns whole at the
  close.
- **Meaningful labelled geometry.** Labels sit beside their objects. Every arrow kind has a legend line naming what
  it means, and a caption states the figure's claim in the author's words.
- **Controlled emphasis.** One accent marks the element under discussion; everything else is quiet ink.
- **One question answered before another begins.** A figure answers the question its section asks, and the next
  figure starts from that answer.

## 7. Open points for root

- **Hook syntax.** Foundation may prefer a different syntax; any syntax with one figure id per line works.
- **Figure numbering.** Foundation decides whether figure numbers ("Figure 3.2") are written by the reader or by the
  author.
- **`atlas_ref` ids.** These come from root's stable atlas ids, when supplied.
