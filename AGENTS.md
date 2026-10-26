# AGENTS.md — www

> Inherits `~/ecosystem/INVARIANTS.md` and `~/ecosystem/AGENTS-HARNESS.md`. Read their core contracts first.
> Load domain references only when relevant. Keep AGENTS.md and CLAUDE.md substantively aligned.
> For Claude host controls or loading, read `~/ecosystem/CLAUDE-HARNESS.md` when relevant.

---

This repository holds personal site pages, publication assets, and a document compiler.

## Read by task

Inspect the affected root HTML page and its navigation before editing it.
Read `compiler/README.md`, `compiler/package.json`, and `compiler/docs.config.js` before compiler work.
Read `compiler/build.js` and `compiler/template.html` for retrieval and generated layout behavior.
For reader papers, read `compiler/reader-papers.json`, `compiler/build-reader-papers.py`, and `references/source-provenance.md`.
Use each builder's configuration to identify its inputs and output directory.
Verify which source produces a page before editing a generated output.
Do not assume this repository and `~/raeez-site` are interchangeable.
Matching `CNAME` values do not establish which checkout owns a live deployment.

## Publication and source custody

Apply inherited external-document rules to public prose and product descriptions.
Preserve signed instruments and original evidence files byte-for-byte.
Check reader-visible source claims, dates, metadata, and local links.
Document retrieval can use external sources. Preserve provenance and inspect the configured inputs before running a compiler build.
Preserve retained raw inputs. A successful build does not establish that a remote source is current.
The compiler's deployment scripts publish externally. Local preparation does not authorize their execution.
Read `_config.yml` before changing publication exclusions. Keep instruction files, source custody, and build records outside the public site.
Keep private repository paths and credential values out of public pages and build output.

## Verification

Use focused compiler checks for behavior changes and inspect the generated page in desktop and narrow layouts.
For reader-paper generation, run `python3 compiler/build-reader-papers.py --check` from the repository root.
The compiler's `dist/feed.xml` is separate from the root `feed.xml`. Check the intended publication artifact before replacing either.
Check `writing.html`, `feed.xml`, `sitemap.xml`, and `llms.txt` when a page change affects those indexes.
For instruction-only changes, review the diff and referenced paths.
Report local output, external-source freshness, and publication status separately.
