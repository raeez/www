# Foundation handoff: the monograph reader shell (sealed 16 Nov 2026, 19:46 UTC = 17 Nov, 02:46 WIB)

- Lane: foundation. Worktree /Users/raeez/www-worktrees/2026-11-16-qh-max-foundation (claude-opus-5-5, max effort).
- Folder: materials/processed/qh-attack-heal-20261116/foundation/monograph.
- No commit, push or publication; no other tree written. All hashes are in GUARD.json.

## The patch

**`patch/monograph.patch`, sha256 `19118f08fb665d4819058924dab6336d3725c12b20f553d66ed2ea225921e35f`.**
Apply it with `patch -p1` at the root of the integration worktree.

It is additive:
- new files `compiler/quantum-holography-status/monograph.py` (cf6abfa6…) and `monograph.css` (7d58f2b9…);
- a hook of about 80 lines in `status.py` (2114d75b… becomes 198727b3…);
- a `reader` block of interface words in `content/quantum-holography-status/page.json` (f0a6edc5… becomes ac44a925…).

The patch applies to integration's current files and reproduces the staged files byte for byte.

**Inert without reader data** (`evidence/INERTNESS.json`): when the content folder has no `reader-data/`, the patched
and unpatched producers write the same page, byte for byte (cf89f01b…). Book mode turns on only when
`content/quantum-holography-status/reader-data/manifest.json` exists. The build script is unchanged.

**Live dependencies.** These are read at build time and not part of the patch:
- `compiler/quantum-holography-status/reader.js`, from interaction (15d25bb3… in the preview);
- `figures.py`, `figures.css` and `figures.js`, from atlas: the frozen five-models set 2b86921f…, 0c68828b… and
  bce4e549…;
- `reader-data/`: `manifest.json` (a8dd97f6…, with `diagrams[]`) and the 18 chapters it names;
- atlas.*, audit.py and status.css, as now in integration.

Without reader.js the book is served as one long page, and a warning says so. Without figures.py, figure hooks are
left out, with a warning.

## Build and candidate

The candidate was built from a frozen snapshot of the author's inputs, so the hashes, the candidate and the evidence
all agree:
- snapshot: `snapshot/20261116T194027Z/` (manifest a8dd97f6…, diagram-records c96f67df…, 18 chapter hashes in
  GUARD.json);
- input folder: `build-input/` (links to integration content, the patched page.json and the snapshot).

    /tmp/qh-tracker-build-20261116-venv/bin/python -B compiler/build-quantum-holography-status.py \
        --input <content folder with reader-data> --output <out>/book.html --audit-dir <out>/audit

- `out/book.html`: sha256 b83033f3d5e8c17b27dec6ce37b1d160fb3979fc3e35b3083efb74c39b8ae8d5, 14,060,149 bytes. The
  audit says **PASS** (0 failures).
- `out/diagram-gallery.html` draws all 13 diagram records with the page's own sheets. It is for QA only, while the
  author's hooks are still being placed.

## Evidence on this candidate (rerunnable tools in `tools/`)

- **Prose retention** (`evidence/PROSE-RETENTION.json`, `tools/check_prose.py`). Across 18 chapters, all 45,628 prose
  words reach the page in order: 0 lost. The only added words are the arXiv numbers that the page's citation rule
  writes. Display counts and authored `\tag` numbers equal the source in every chapter.
- **Diagrams** (`evidence/DIAGRAMS.json`, `tools/check_diagrams.py`):
  - all 13 accepted records render through the page's own context, with 0 problems, 0 TeX errors and 0 definition
    targets missing from the book;
  - only `fig-state-line-cap` (ch17) is placed so far, because the other 12 have no `::: figure` hook in the chapters
    yet.
- **DOM and links:**
  - ids: 4,250, none repeated;
  - internal links: 1,353, all resolving;
  - places: 18 chapter articles, 119 sections and 12 reference places;
  - result blocks: 26 theorems, 2 conditional results and 11 open problems;
  - displays: 626, with 99 authored numbers;
  - cross-references (`data-ref`): 193 chapter, 124 section and 72 equation;
  - all five atlas models and the placed diagram render.

## How the diagram records are drawn (the author's PROGRAMME-DIAGRAM-CONTRACT, c678539d…)

The renderer is `Diagram` in monograph.py, the only renderer of the static and context diagrams. It reads the
accepted records unchanged. Every `::: figure <id>` is looked up in `figures[]` (atlas renderer) or in `diagrams[]`
(this one).

- **Edge kinds.** Each has its own stroke and head, never colour alone:
  - `mathematical_map`: solid line, solid head;
  - `functor`: solid line, open chevron;
  - `construction`: long-dashed line, with the label written on the drawing;
  - `open_comparison`: dashed line in the open colour, hollow head;
  - `reading_relation`: dotted grey line. The legend calls it navigation, never a map.
- **Direction.** `direction: "undirected"` draws no head, and its list entry uses "—" ("compared with") instead of
  "→". This applies to the two open state/line/cap comparisons.
- **Status words.** The author's word is always shown. "Theorem" takes the proved mark and "Open problem" the open
  mark. "Defined map", "Reading relation" and "Convention" take no mark.
- **Record fields shown under the drawing, verbatim:**
  - `legend`, with the author's text for each kind (the five context views);
  - `status`, `hypotheses`, `equations` and `formulas` (typeset);
  - `relations`, each with its status word and mark;
  - `witness` (coordinates and conclusion), `prohibitions` (under "Not asserted") and `caption`.
- **Edges and nodes in full.** A numbered list gives each edge's ends, label, kind, status and hypotheses. A node list
  gives the descriptions and formulas.
- **Context views.** For the five `context_key` views the two lists fold under the drawing (opened in print). The
  caption, legend and restrictions stay visible.
- **Node identity.** DOM ids are namespaced by figure id: `{figure}--{node}` and `{figure}--{edge}`. This follows the
  records' `node_identity_rule`, which is an implementation rule and is not shown as text.
- **Definition links.** `definition_ref` is a {chapter_id, section_id} pair, and the node links to that section. A
  target not yet on the page shows the name unlinked, with a warning; none is missing now.
- **Unknown fields.** A record field outside the contract fails the build, by name, for return to the author. Nothing
  is dropped silently. A missing title, caption, node label or edge end also fails the build.
- **Layout.**
  - Nodes are layered along the edges' direction; no edge is added, merged or reversed.
  - Rows grow with the longest label.
  - A drawing is never scaled below 0.78; a narrower figure scrolls it inside its own box, with edge cues, never the
    page.
  - Layers run left to right only where the figure is wide enough, otherwise top to bottom.

## Applications A01–A08 realized by the changed components

| | Where on the page | Evidence |
|---|---|---|
| A01 sequence | The front matter (title, map, routes, marks) leads to the contents (parts, then chapters with summaries and "Draws on" numbers, then their sections). Each chapter runs in this order: kicker, title, the author's opening (first paragraph as the lead), numbered sections, the author's closing paragraph, then the next-chapter card with that chapter's summary. | Prose retention: 0 words lost. Chapters are in manifest order. Nothing is capped. |
| A02 whole-to-local | The book map and each chapter's locator share one grid. It is titled "The chapters and their reading prerequisites", and its caption says the arcs record reading order, not mathematical implication. The locator has a key, and "Draws on" and "Used later in" lists say the same in text. The five recurring context diagrams carry the author's own legend that reading relations are not maps. | The front map draws exactly the manifest's 59 prerequisite pairs; no edge is inferred. |
| A03 same identifiers | The same chapter numbers appear in the map, contents, heads, locator, lists and cards. Section numbers n.k are the same everywhere. Authored equation numbers are unchanged, and a plain "(n.m)" links to its display (72 links). Diagram ids are verbatim, and node and edge ids are namespaced. Old ids are kept, with one exception (decision 1 below). | 0 duplicate ids; all 1,353 links resolve. |
| A04 one status vocabulary | Each result block carries the shared mark beside the author's lead-in, shown verbatim. A qualifier in the name governs the kind: the two conditional theorems are not marked as theorems. Diagram edges and relations use the same marks under the author's status words. The front has a key of the marks. | 39 lead-ins were checked against the source. Atlas squares (C5) remain the atlas lane's. |
| A05 meaningful figures | Atlas models are placed through its renderer. The author's diagrams are drawn with every node, edge, kind, status, hypothesis and restriction as written. | 5 of 5 models render; 13 of 13 diagram records render with 0 problems. |
| A06 complete prose | Displays and result blocks hold full statements, with hypotheses inside them. Bold first-use terms are kept. | As A01. |
| A07 readability and states | Measure: 31 body sizes. Layout tiers at 1181+, ≤1180, ≤860, ≤640 and ≤480 px. Reader-QA findings addressed: C8 (display scroll cue in both themes, slight scale-down of wide formulas, margin column), C9, C12/C20 (notices styled, never printed) and C18 (no 11-link scroller). The reader's states are styled. Print gives the place being read, or the whole book without the script. Labels are 12 px or larger. | **Not seen**: I viewed no page image (root's browser restriction). Visual, keyboard and print acceptance stays with native QA. |
| A08 evidence | GUARD.json, INPUTS.sha256, evidence/*.json, CONTENT-ISSUES.json, out/audit, and tools/ to rerun. | Patch apply and inertness proved. None of this is acceptance. |

## Decisions and gaps for root

1. **`#contents`.** The book's contents is `#contents`, so the old page's own contents block is now
   `#programme-contents`. An old `…#contents` link lands on the book's contents, which lists every reference place.
2. **Glossary id.** The contract names `#glossary`, but the old glossary keeps `#terms`. There is no new glossary
   until the author supplies term records.
3. **Equation references.** `data-ref="equation"` is a cross-reference kind outside the contract's list. Interaction
   can treat it as `section`.
4. **status.js and the theme.** status.js is not served on the book page (gap G5). Setting `page.json`
   `reader.with_status_js: true` serves it before reader.js. No script on the book page toggles the theme: a stored
   `qh-theme` and the system preference still apply.
5. **Working-file links.** 101 links and reference definitions to local or /tmp working files are shown as their
   words only, never as addresses. CONTENT-ISSUES.json lists every one by file and line, for the author. Web citations
   follow the page's existing rule: their words, with the arXiv number.
6. **Diagram hooks.** Twelve diagram records still need their `::: figure` lines in the chapters (author). Each will
   render at its hook with no change on my side.

## Not done, and limits

- No page image was judged, by me or by anyone else.
- jsdom is not installed locally, so reader.js was not run against this DOM. The interaction lane's harness can run
  on `out/book.html`.
- The author's 08/09/12/13 repairs, landing after snapshot 20261116T194027Z, are not in this candidate. Root's own
  build on the final content supersedes it. The patch does not depend on chapter text.
