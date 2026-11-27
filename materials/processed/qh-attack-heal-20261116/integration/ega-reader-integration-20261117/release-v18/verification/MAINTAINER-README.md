# Quantum holography reader

The public edition serves the book (`index.html`), reference (`reference.html`), atlas
(`atlas.html`) and their shared search index (`reader-index.js`). [Open the reader](https://research.momentum.inc/quantum-holography/).

Edit the relevant native Markdown, JSON or compiler sources. From the repository root, build the
four public files in a fresh directory with Python 3 (`fontTools` and `brotli`), Node.js with
`jsdom`, and TeX Live with `kpsewhich`, EB Garamond and Garamond-Math available.

    qh_build=$(mktemp -d)
    python3 -B compiler/build-quantum-holography-reader.py "$qh_build/v18"

Open `$qh_build/v18/release/index.html` to verify your changes in the public reader. The combined
native preview is at `$qh_build/v18/build/combined.html`, with its audit in `$qh_build/v18/build/audit/`.

To reproduce the latest issued edition from its frozen sources and check the four published file
hashes, use a fresh output path under the same temporary root. [v18 release manifest](../../materials/processed/qh-attack-heal-20261116/integration/ega-reader-integration-20261117/release-v18/MANIFEST.json)

    python3 -B compiler/build-quantum-holography-reader.py --frozen "$qh_build/issued"

## Files

- `content.json`: the words. Written by the content writer, not edited here except to replace it
  whole with a newer settled version.
- `essay.md`: the essay, reproduced unchanged: a `# Title` line, then paragraphs separated by blank lines.
- `page.json`: interface labels, status labels and page metadata (design).

## content.json

```
{
  "title", "subtitle", "as_of" (YYYY-MM-DD),
  "lead": [paragraph, ...],
  "status_key": [{"status", "label", "explanation"}, ...],
  "principal": [STATEMENT, ...],
  "columns": [{"id", "name", "explanation", "short"?}, ...]   ids: object dual modules fusion bulk lines states dictionary
  "rows": [{"id", "name", "short"?, "summary", "cells": {column id: CELL}, "statements": [STATEMENT, ...]}, ...],
  "changes"?: {"since" (YYYY-MM-DD), "intro", "items": [{"ref": statement id, "text"}, ...]},
  "decisive"?: {"heading", "intro", "questions": [{"id", "title", "question": STATEMENT, "why", "known": [STATEMENT, ...]}, ...]},
  "frontier"?: {"heading", "intro", "questions": [{"id", "title", "question": STATEMENT, "why", "known": [STATEMENT, ...]}, ...]},
  "failures"?: {"heading", "intro", "items": [{"id", "claim", "witness": STATEMENT}, ...]},
  "open": [{"heading", "intro", "statements": [STATEMENT, ...]}, ...],
  "glossary": [{"term", "forms": [...], "definition"}, ...],
  "essay_lead": ""
}
STATEMENT = {"status", "title", "text", "novelty", "antecedents", "cite", "source": [...], "id"?, "added"?}
CELL      = {"status", "note", "source": [...]}
```

Statement statuses: checked, pending, conditional, conjecture, heuristic, open, published.
Cell statuses: checked, partial, pending, published, open, not posed, refuted form.
`id` gives a statement an anchor (`#s-<id>`), which `changes.items[].ref` names; `added: true` marks a
statement as new in this edition. `changes` is shown under the cover as a numbered list of links. `decisive`
and `frontier` follow the principal results, using the same question cards; `decisive` has its own navigation
anchor and the page labels `nav_decisive` and `decisive_kicker`. `failures` (a natural statement marked false, then its counterexample) follows
the examples. Markdown links in `cite` and `antecedents` are shown as their text, with the arXiv number when
the address has one: the page links to no other host.
Text is plain, with TeX between `\(`…`\)` or `\[`…`\]` and `*emphasis*`. The `source` fields are for
tracing and are never rendered. Glossary `forms` are matched in the text, and the first use of each
term in a block opens its definition on hover, focus or tap.

## Audit

The build fails on: an unknown status or a missing grid cell; a TeX error; any reference to another
host (no fonts, scripts, styles or images are fetched; a Content-Security-Policy forbids it); a broken
in-page link or duplicate id; and reader-visible words that name tools or models, files, internal
identifiers or workflow (the mathematics-only rule for reader-facing text).
