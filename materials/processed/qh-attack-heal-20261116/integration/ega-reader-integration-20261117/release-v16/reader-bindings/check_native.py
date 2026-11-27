"""Exercise the deployed reader compiler on the rebinding, in memory."""
import argparse
import collections
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.dont_write_bytecode = True
from bind import (BASE_CONTENT, BASE_MANIFEST, BATCH, BINDINGS, HERE, TARGET, encoded,
                  main as check_bindings, read_json, require, sha, write_or_check)

COMPILER = BATCH / "workspace/compiler/quantum-holography-status"
sys.path.insert(0, str(COMPILER))
import monograph
import status


class Html(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = collections.Counter()
        self.hrefs = []
        self.math_count = 0

    def handle_starttag(self, tag, attributes):
        attr = dict(attributes)
        if "id" in attr:
            self.ids[attr["id"]] += 1
        if tag == "a" and "href" in attr:
            self.hrefs.append(attr["href"])
        if tag == "math":
            self.math_count += 1


def run(manifest_path, render_math):
    m = read_json(manifest_path)
    page = read_json(BASE_CONTENT / "page.json")
    b = status.Build(BASE_CONTENT, page)
    b.content = read_json(BASE_CONTENT / "content.json")
    book = monograph.Book(b, manifest_path, status.mark, page["reader"])
    # The native book resolves cross-volume links when the enclosing page is
    # assembled. Supply only IDs that exist in the real publication's staged
    # atlas and reference documents. The book must emit every one of its own IDs.
    atlas = read_json(BASE_CONTENT / "atlas.json")
    external = {f"atlas-c-{c['id']}" for c in atlas["claims"]}
    external |= {x["id"] for x in status.Terms(b.content["glossary"]).entries}
    atlas_page, reference_page = Html(), Html()
    atlas_page.feed((BATCH / "public/atlas.html").read_text())
    reference_page.feed((BATCH / "public/reference.html").read_text())
    require(all(atlas_page.ids[i] == 1 or reference_page.ids[i] == 1 for i in external),
            "Missing reference/atlas targets in delivered v15")
    anchors = "".join(f'<span id="{i}"></span>' for i in sorted(external))
    body = book.assemble(anchors, [])
    built = Html()
    built.feed(body)
    expect = {s["id"] for s in m["sections"] + m["chapters"] + m["diagrams"] + m["figures"] + m["terms"]}
    expect |= {r["rendered_anchor"] for r in m["theorems"]}
    expect |= {"index-" + r["id"] for r in m["theorems"]}
    expect |= set(book.tags.values())
    require(all(built.ids.get(s) == 1 for s in expect),
            f"Missing or repeated reader anchors: {[s for s in sorted(expect) if built.ids.get(s) != 1]}")
    require(all(x == 1 for x in built.ids.values()), "Duplicate HTML ID")
    require(not book.problems and not b.problems, f"Native problems: {book.problems + b.problems}")
    require(all(built.ids.get(i) == 1 for i, _ in book.pending_refs), "Unresolved reader cross-reference")
    require(all(built.ids.get(i) == 1 for i, _, _, _ in book.pending_defs), "Unresolved diagram node reference")
    for rec in m["theorems"]:
        require("#" + rec["rendered_anchor"] in built.hrefs, f"Missing result link: {rec['id']}")
    for rec in m["terms"]:
        require("#" + rec["definition_ref"] in built.hrefs, f"Missing glossary link: {rec['id']}")
    require(set(book.figures_placed) == {r["id"] for r in m["diagrams"] + m["figures"]},
            "Placed figure/diagram set differs")
    if render_math:
        b.math.render()
        require(not b.math.errors, f"MathML errors: {b.math.errors}")
    summary = {
        "explicit_checked_targets": len(expect), "reader_and_external_anchor_count": len(built.ids),
        "native_book_anchor_count": len(set(built.ids) - external),
        "placed_figures_and_diagrams": len(book.figures_placed), "numbered_equations": len(book.tags),
        "resolved_cross_reference_occurrences": len(book.pending_refs),
        "resolved_diagram_target_occurrences": len(book.pending_defs), "native_math_jobs": len(b.math.jobs),
        "math_errors": b.math.errors, "compiler_problems": book.problems + b.problems,
        "compiler_warnings": book.warnings + b.warnings,
    }
    return set(built.ids) - external, book.tags, summary


def main(check):
    check_bindings(True)
    old_ids, old_tags, previous = run(BASE_MANIFEST, False)
    new_ids, new_tags, current = run(TARGET, True)
    require(old_ids == new_ids, f"Native HTML ID set changed: {old_ids ^ new_ids}")
    require(old_tags == new_tags, "Numbered equation destinations changed")
    require(previous["compiler_warnings"] == current["compiler_warnings"],
            f"Reader warnings differ from the deployed source: {current['compiler_warnings']}")
    receipt = {"status": "PASS", "compiler_sha256": sha((COMPILER / "monograph.py").read_bytes()),
               "status_renderer_sha256": sha((COMPILER / "status.py").read_bytes()),
               "manifest_sha256": sha(TARGET.read_bytes()), "bindings_sha256": sha(BINDINGS.read_bytes()),
               "unchanged_native_id_count": len(new_ids), "native_v16": current,
               "coverage": "Native book, front, contents, glossary, theorem and figure output in memory. The root build will check the integrated split-site delivery."}
    check_bindings(True)
    write_or_check(HERE / "native.json", encoded(receipt), check)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    main(parser.parse_args().check)
