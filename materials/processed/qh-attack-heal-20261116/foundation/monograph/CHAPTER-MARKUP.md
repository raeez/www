# Chapter markup the reader renders (interface proposal to root, for the exposition owner)

From the foundation lane, 17 November 2026. This is an interface note only. It changes no wording: the chapter
Markdown stays the authoritative text, and the renderer never rewrites a statement, caption or parameter.

The renderer accepts plain Markdown as the author is already writing it. The forms below make four things exact
that plain Markdown leaves ambiguous: where a theorem ends, what a cross-reference points to, where an interactive
model goes, and which passage is the chapter's opening and which its transition.

## 1. What already works with no change

- One `# Title` line at the top (optional; the manifest title is shown, and a different `#` title is reported).
- `## Section` and `### Subsection` headings. The renderer numbers `##` sections as chapter.section (6.1, 6.2, …)
  unless the heading already begins with a number, which is then kept as written.
- Paragraphs, `*italic*`, `**bold**`, `` `code` ``, bulleted and numbered lists, block quotes, pipe tables.
- Inline `\(...\)` and display `\[...\]` (on their own lines, or inside a paragraph). `$$...$$` is also read as display.
- Conventional lead-ins: a paragraph that begins `**Theorem 6.3 (Name).**`, `**Definition.**`, `*Proof.*` and so on
  becomes that environment. The number, when written, is kept exactly; when absent, the renderer numbers the
  environment chapter.n in one counter per chapter (Definition 6.1, Theorem 6.2, Example 6.3, …).
  A lead-in environment continues over the display formulas and lists that follow it, and over paragraphs that begin
  with a lower-case word ("where …", "and …"); it ends at the next heading, lead-in or ordinary paragraph.
  A proof ends at its ∎ or □, or at the next heading or lead-in.

Recognised environment names, with the label the reader sees:
Definition, Theorem, Proposition, Lemma, Corollary, Conditional result (also "Conditional theorem"), Conjecture,
Heuristic, Example, Counterexample, Construction, Remark, Notation, Convention, Open problem, Question, Proof.

## 2. Exact forms (recommended where a boundary or a label matters)

Pandoc fenced divs. The class is the environment name in lower case, with hyphens for spaces:

    ::: {.theorem #thm-bar-cobar title="Bar–cobar equivalence"}
    Let \(X\) be a smooth separated curve …
    \[ … \]
    Then …
    :::

    ::: {.proof of="thm-bar-cobar"}
    …
    :::

- `#id` gives the stable anchor. Use it for anything cross-referenced. Ids are kebab-case and unique in the book;
  suggested prefixes: `def-`, `thm-`, `prop-`, `lem-`, `cor-`, `cond-`, `ex-`, `cex-`, `open-`, `fig-`, `eq-`, `sec-`.
- `title="…"` is the parenthetical name (shown as "Theorem 6.3 (Bar–cobar equivalence)").
- `n="6.3"` fixes a number; otherwise the renderer numbers as in §1.
- Classes: `definition`, `theorem`, `proposition`, `lemma`, `corollary`, `conditional`, `conjecture`, `heuristic`,
  `example`, `counterexample`, `construction`, `remark`, `notation`, `convention`, `open-problem`, `question`, `proof`.

Headings take an id the same way: `## Adjunctions and their triangles {#sec-adjunction-triangles}`.
A labelled display formula takes an id on the line after its closing `\]`: `{#eq-gauss}`; it is then numbered
(1.3) at the right margin and can be cited.

## 3. Cross-references

Ordinary Markdown links to an id: `[Theorem 6.3](#thm-bar-cobar)`, `[Section 6.2](#sec-adjunction-triangles)`,
`[(1.3)](#eq-gauss)`, `[Chapter 5](#ch05)`. A plain "(1.3)" in the prose is linked to the display tagged 1.3 when the book has one. Chapter ids are the manifest ids `ch01` … `ch18`. The link text is the
author's; the renderer does not rewrite it. Every internal link must resolve; an unresolved one is reported.
A link into the atlas uses the atlas id root supplies (`#atlas-claim-…`).

## 4. Opening and transition

- The chapter opening is everything before the first `##` heading. It is set as the chapter's opening passage,
  beside the chapter's place in the book (its prerequisites and the terms it introduces, from the manifest).
- The closing passage that motivates the next chapter, if marked, is placed directly before the link to the
  next chapter:

      ::: transition
      …
      :::

  Unmarked, the chapter simply ends with its last section.

## 5. Figures (superseded by root's decision of 17 November; FIGURE-RECORD-CONTRACT.md governs)

The only placement is one line, `::: figure <figure-id>`, with the manifest figure id used verbatim as the DOM id
(it already carries its `fig-` prefix). Foundation parses the hook and calls the atlas lane's `figures.render`; the
foundation draws no model. The earlier `::: {.figure model=…}` form of this note is withdrawn.

## 6. Manifest fields the reader shows if supplied (all optional, author's wording)

- `chapters[].summary`: one or two sentences, shown in the contents and in the link to the next chapter.
- `parts[].summary`: shown under the part title in the contents (for instance the "Mathematical movement" sentences
  of READER-ARCHITECTURE.md, if the author wants them public).
- `routes`: the three prerequisite-closed routes, so the route map can draw them, as
  `[{"id": "algebra-geometry", "title": "Algebra and geometry", "chapter_ids": ["ch01", …]}, …]`.
  The route titles are the author's; the reader shows no route until this field exists.
- `chapters[].atlas_ref`: atlas ids for "In the atlas" links at the chapter's end.

## 7. Not rendered

Anything under `coordination/`. HTML comments `<!-- … -->` in a chapter are dropped.
