# quantum-holography-tracker.html: the status page

Build (from the repository root):

    python3 compiler/build-quantum-holography-status.py

It reads this folder and writes `quantum-holography-tracker.html` at the repository root when every
audit passes; the audit report is written to `audit/audit.txt`. `--allow-draft` writes the page
despite failures; `--no-fonts` skips font embedding for quick layout work. Requires Python 3 with
fontTools, Node (for the vendored Temml in `compiler/quantum-holography-tracker/vendor`), and the
TeX Live fonts EB Garamond and Garamond-Math (found with `kpsewhich`; both under the SIL Open Font
Licence), which are embedded as subsets. The page makes no request to any other host.

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
statement as new in this edition. `changes` is shown under the cover as a numbered list of links, `frontier`
after the principal results, `failures` (a natural statement marked false, then its counterexample) after
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
