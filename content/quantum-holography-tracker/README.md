# quantum-holography-tracker: inputs and build

This folder holds the inputs of `quantum-holography-tracker.html` at the repository root.
GitHub Pages excludes the folder (`_config.yml`). The page is unlisted: it carries
`<meta name="robots" content="noindex, nofollow">` and is not named in `writing.html`,
`feed.xml`, `sitemap.xml`, `llms.txt`, `llms-full.txt` or `robots.txt`.

## Build

```bash
# from the repository root
python3 compiler/build-quantum-holography-tracker.py --input <folder>
python3 compiler/build-quantum-holography-tracker.py --allow-draft     # the stand-in below
```

The build reads one input folder, renders all TeX to MathML, links every use of a term to
its card, writes one self-contained HTML file and runs the audits. It writes the page to the
repository root only when `STATUS.md` says the words are settled and every audit passes, or
when `--allow-draft` is given; otherwise it writes `audit/rejected.html`. The audit results
are in `audit/audit.txt` and `audit/audit.json`.

Requirements: Python 3 with `beautifulsoup4` and `fonttools`, `pandoc` 3, and `node` (for
the vendored TeX renderer, `compiler/quantum-holography-tracker/vendor/temml.cjs`, MIT).
The embedded math font is a subset of Garamond-Math (SIL Open Font License), found with
`kpsewhich Garamond-Math.otf` or given with `--math-font`.

## What the page shows

- **The first screen.** The title and the subject, then the breakthroughs in rank order. Each
  row gives the headline, its status, the Achieved line as the writer states it, the work and
  sections its "Proved in" line cites, and the report sections its "Read more" line names; the
  other lines open on demand. The obstructions follow by name, then links to the rest of the
  page with the size of each part.
- **Statuses come only from the words.** A "Proved in" (or "Proof") line gives *Proved*; a
  "Checked" line gives *Checked*; an open problem is *Open*. Nothing else sets a status, and no
  status is shown for an item whose lines state none.
- **The map of results.** One row for each result: the report sections its "Read more" line
  names (with the theorems and propositions stated there, and whether each proof is on the
  page), the result with its status, and the sections of the work its "Proved in" line cites,
  joined by hairlines. Open problems have rows of their own. Relations between results are
  shown only where the words state them: a "Builds on" line, or a link from one item to
  another. The audit notes when no item states one.
- **Finding things.** A search over results, sections, statements and term cards (the Search
  button, `/` or Ctrl-K); the contents beside the report, with each result's sections marked
  and the statements of each section counted; a link on every heading and statement; a filter
  over the term cards.
- **Light and dark.** The page follows the reader's system theme; the button in the bar
  switches it, and the choice is remembered in the browser.

`stand-in/` is the 24 October 2026 report converted with
`compiler/quantum-holography-tracker/import_integrated_report.py`, without changing its
words. Its status states were assigned by the conversion and its cards have no motivation or
context; it exists to build and check the page until the settled words arrive.

## Input folder

```
words/REPORT.html   or   words/REPORT.md
words/STATUS.md
cards/TERMS.json
words/OPENING.md    or   words/OPENING.html     (optional: the opening)
cards/OPENING-TERMS.json                        (optional: the opening's cards)
words/LABELS.json                               (optional: names for the page's labels)
```

### words/STATUS.md

```
Status: settled            (or: draft; a "State:" line is read the same way)
Date: 2026-11-05           (the date of the last change to the words; the page prints it)
Hash: <sha256 of REPORT.md or REPORT.html, of TERMS.json, or of the two concatenated>
Changed: <what changed>
```

The page is written only when the first word after `Status:` or `State:` is `settled`.

### words/REPORT.md (plain Markdown)

Pandoc Markdown with TeX in `$ … $`, `$$ … $$`, `\( … \)` or `\[ … \]`. Plain structure is
enough; the build reads it as follows.

```markdown
# Title

One line: what the programme is.            (a paragraph of 45 words at most)

One line: where it stands now.              (a second short paragraph, optional)

## Headline of the status section, as a claim

### Established

*One line: what this state means.*

- **The item, as one sentence.** What holds, on what domain. Next: the next step.
- **Another item.** …

### Working
### Failing
### Stabilising
### Oscillating
### What remains

## Section headline, as a claim {#question data-toc="Short contents label"}

Prose, with $Y(a,z)$ inline and $$\int_0^1 f$$ on its own line.
```

- The first `#` heading is the title; up to two short paragraphs after it are the first
  screen's two lines. Use `##` for sections and `###`, `####` inside them.
- The section whose headings name two or more states (Established, Working, Failing,
  Stabilising, Oscillating, What remains) becomes the status board at the top of the page.
  Under each state heading, an italic line defines the state; each list item, sub-heading or
  paragraph is one item; a bold lead is the item's title on the board; "Next:" starts its next
  step.
- `{#id}` on a heading gives the section its anchor; `data-toc` a shorter contents label.
- `[wording]{data-term=card-id}` links a different wording to a card;
  `::: {.statement data-kind=Theorem}` … `:::` and `::: {.proof}` … `:::` set statements and
  closed proofs.

### words/REPORT.html

An HTML fragment (no `<html>`, `<head>` or `<body>`). Write `&lt;` and `&amp;` for `<` and
`&`, also inside TeX. Mathematics is MathML, or TeX in `\( … \)` (inline) and `\[ … \]`
(display); `<span class="math inline">` and `<span class="math display">` holding TeX are
also read. The parts, in any order:

```html
<header data-role="hero">
  <p data-role="eyebrow">Geometry · quantum fields · arithmetic</p>
  <h1>Title</h1>
  <p data-role="dek">One line: what the programme is.</p>
  <p data-role="state">One line: where it stands now.</p>
</header>

<section data-role="status">
  <h2>Headline of the status section, as a claim</h2>
  <p data-role="dek">Optional one-line lead.</p>
  <dl data-role="states">
    <dt data-state="established">Established</dt><dd>One line: what this state means.</dd>
    … one pair for each of: established, working, failing, stabilising, oscillating, remains
  </dl>
  <ol>
    <li data-state="working" data-ref="section-or-heading-id">
      <h3>The item, as one sentence (24 words at most)</h3>
      <p>What exactly holds or is being built, on what domain.</p>
      <p data-role="next">The next step.</p>
    </li>
    …
  </ol>
</section>

<section id="motivation" data-toc="Short contents label">
  <p data-role="eyebrow">Optional section label</p>
  <h2>Section headline, as a claim</h2>
  <p>…</p>
  <div class="statement" data-kind="Theorem"> … </div>
  <div class="proof"> … </div>          (rendered as a closed “Proof” block)
</section>
```

- The status section moves to the top of the page, under the title. States are
  `established`, `working`, `failing`, `stabilising`, `oscillating` and `remains`. Each
  item's heading is its title on the board; the rest opens beneath it. `data-ref` links the
  item to the section that discusses it.
- Each top-level `<section>` is one entry in the contents; its `<h2>` headings (or `<h3>`,
  when a section has one `<h2>`) are the entries beneath it. `data-toc` gives a shorter label.
- Terms are linked automatically: every use of a card's `display_name` or alias, singular or
  plural, in any case. To link a different wording, write
  `<span data-term="card-id">wording</span>`. A `<dfn>` naming a card marks where the term is
  defined; the card links to it.
- Links to `#ids` that are not on the page, and links to attached files, are removed (their
  words stay) and reported. The page carries no attachments.

### words/REPORT.md (explicit form)

The parts can also be marked explicitly, as fenced divs and spans:

```markdown
::: {data-role=hero}
[Geometry · quantum fields · arithmetic]{data-role=eyebrow}

# Title

[One line: what the programme is.]{data-role=dek}
:::

::: {data-role=status}
## Headline of the status section
::: {data-state=working data-ref=motivation}
### The item, as one sentence
What exactly holds. [The next step.]{data-role=next}
:::
:::

## Section headline {#motivation data-toc="Short label"}

::: {.statement data-kind=Theorem}
…
:::
```

Use `[wording]{data-term=card-id}` to link a different wording to a card.

### words/OPENING.md (the opening)

When this file exists, it opens the page: its title replaces the report's title and title
lines, and the report's status board is not shown. The body of the report follows it.

```markdown
# Title

First paragraph of the subject, in plain words.

Second paragraph of the subject.

## Breakthroughs {#breakthroughs data-toc="Breakthroughs"}

### 1. Headline claim, at most 16 words

- **Achieved:** what is proved, as one sentence.
- **Why it matters:** …
- **Domain and hypotheses:** …
- **Proved in:** paper title, section, hypotheses.
- **Read more:** [Section label](#section-id)

### 2. …

### Decisive obstructions

#### Headline of the obstruction

- **Achieved:** … (the same five lines)

## Open problems {#open-problems data-toc="Open problems"}

### Short name of the problem

Prose.
```

- Every paragraph between the title and the first `##` heading is the subject. A
  `## The subject` heading may mark it instead.
- `## Breakthroughs` lists the results in rank order; a leading `1.` in a headline is printed
  as its rank. A heading named "Decisive obstructions" (or "Obstructions") starts the
  obstructions, set apart in a band of their own; it can also be its own `##` section.
- Each item is a heading and a list of labelled lines. The page recognises the labels
  Achieved, Why it matters, Domain and hypotheses (or Status), Proved in and Read more, and
  prints them as written. The Achieved line shows with the headline; the others open on
  demand. The audit requires all five on every breakthrough and every obstruction, and a
  Read more link to a part of the page.
- Two further lines are optional. **Checked:** records a check of the result (the page shows
  *Checked* beside *Proved*). **Builds on:** links the items or sections the result builds on,
  for example `- **Builds on:** [Coefficient duality](#breakthroughs-1)`; the map lists them.
  An open problem takes a paragraph that starts "Builds on:" for the same purpose. The anchors
  are `#breakthroughs-1`, `#breakthroughs-2`, … and `#obstructions-1`, … in rank order, and each
  open problem's own heading anchor.
- `## Open problems`, and any other `##` section in the file, follows the obstructions as an
  unnumbered section with its own contents entry.
- The same parts can be written into REPORT.md, before the status section; then the status
  board is kept and its six counts move below the obstructions.
- `cards/OPENING-TERMS.json` has the format of TERMS.json. Its cards are added to the
  others; a card with the same id as a TERMS.json card replaces it.
- STATUS.md may give a hash line for each file (`Opening-Hash:`, `Opening-Cards-Hash:`);
  the audit reports which inputs the hashes match.

### words/LABELS.json

One object of `{key: text}`, overriding the labels in `page.json` and the state names:

```json
{"working": "Partly proved", "next": "", "status": "Results"}
```

- The keys are the state ids (`established`, `working`, `failing`, `stabilising`,
  `oscillating`, `remains`), `next`, and any label in `page.json`.
- An empty value (`""` or `null`) for `next` hides every "Next" line; for a state, it drops
  the state from the board when the state has no items.
- A status item without a "Next" line shows none.

### cards/TERMS.json

A JSON list of card objects:

```json
[
  {
    "id": "vertex-algebra",
    "display_name": "vertex algebra",
    "definition": "A <strong>vertex algebra</strong> is … \\(Y(a,z)\\) …",
    "motivation": "Why the programme needs it, in one to three sentences.",
    "context": "Where it sits: what it generalises, what it is compared with.",
    "related": ["vertex-operator", "lattice-vertex-algebra"],
    "aliases": ["vertex algebras"]
  }
]
```

| Field | Type | Rule |
|---|---|---|
| `id` | string | lowercase slug `[a-z0-9-]`, unique; the page anchor is `#term-<id>` |
| `display_name` | string | the card's title; also the name linked in the text |
| `definition` | string | the definition itself, complete without the rest of the page |
| `motivation` | string | why the term matters to the programme |
| `context` | string | where it sits among the other notions |
| `related` | list of ids | each id has a card; shown as links that open those cards |
| `aliases` | list of strings | optional; other names linked to this card |

Text fields are HTML or Markdown, with TeX as above. A card must not depend on its place
in the page ("above", "below", "this section"), cite a numbered item, link to a statement
the page does not contain, or carry file names, labels or internal codes.

## Audits

| Audit | Checks | Stops a settled build |
|---|---|---|
| terms | names marked or defined as terms without a card; emphasised phrases, capitalised names and frequent technical phrases without a card (candidates for the writer) | marked or defined without a card |
| cards | empty fields, unknown related ids, shared definitions, positional words, numbered citations, length over 180 words, a definition that does not name its term | empty fields, unknown ids |
| words | links to absent statements, attachments, TeX that failed to render, missing hero and status lines | all |
| leaks | seat and session ids, hexadecimal ids, paths, file names, LaTeX labels, question and ledger codes, model and tool names, process words | all |
| fetches | every resource loaded from another host; only the site's fonts are allowed | all |
| listing | the page named in the site's indexes; the robots meta | all |
| opening | every breakthrough and obstruction has its five lines, its Read more resolves | all |
| weight | bytes, gzip bytes and their composition | none |

The labels the page itself prints (contents, status, terms, the card labels, the state names)
are in `page.json`.
