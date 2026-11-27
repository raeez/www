"""Reproduce the v16 manifest from the deployed v15 manifest and frozen authors' files."""
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from selections_v16 import FROZEN, SELECTIONS, SUMMARIES

HERE = Path(__file__).resolve().parent
AUTHORS = HERE.parent
BATCH = Path("/tmp/qh-v15-first-principles-build-20261118/batches/direct-v15")
BASE_CONTENT = BATCH / "workspace/content/quantum-holography-status"
BASE_MANIFEST = BASE_CONTENT / "reader-data/manifest.json"
DIAGRAMS = BASE_CONTENT / "reader-data/diagram-records.json"
INTROW = AUTHORS / "introduction.json"
TARGET = AUTHORS / "reader-data/manifest.json"
BINDINGS = HERE / "bindings.json"
PREVIOUS_TOOLS = Path("/tmp/qh-first-principles-reader-20261118/coordination/binding-tools")
sys.path.insert(0, str(PREVIOUS_TOOLS))
from sync import Chapter, check_unique, references, rendered

BASE_SHA = "4816c9017331864999cf4948d471c8e17b5e1110963d5c338e6be9c5579999dc"
INTRO_SHA = "0bd3a80cc3c58997f956821089c94cea1cc342f1a0e6f899cafad3f3d328834b"
DIAGRAM_SHA = "94ca6ef5e08d2452663ce2f5a215ef9c4c31f9149b435b35087c25318cef4f51"
RESULT_RANGE = "source_range"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_bytes())


def encoded(data):
    return rendered(data).encode("utf-8")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def frozen_digest(path, expected):
    got = sha(path.read_bytes())
    require(got == expected, f"Source digest mismatch: {path}: {got}")
    return got


def chapter_map(chapters, manifest_path):
    return {c["id"]: Chapter((manifest_path.parent / c["path"]).resolve(), c["id"])
            for c in chapters}


def span_record(ch, start, passage):
    end = start + len(passage)
    start_byte = len(ch.text[:start].encode("utf-8"))
    end_byte = start_byte + len(passage.encode("utf-8"))
    first_line = ch.text.count("\n", 0, start) + 1
    last_line = ch.text.count("\n", 0, end - 1) + 1
    require(ch.path.read_bytes()[start_byte:end_byte] == passage.encode("utf-8"),
            f"UTF-8 bytes disagree in {ch.id}, offset {start}")
    return dict(start=start, end=end, start_byte=start_byte, end_byte=end_byte,
                first_line=first_line, last_line=last_line,
                quote_sha256=sha(passage.encode("utf-8")))


def write_or_check(path, blob, check):
    if check:
        require(path.read_bytes() == blob, f"Stored output differs from reconstruction: {path}")
    elif not path.is_file() or path.read_bytes() != blob:
        path.write_bytes(blob)


def main(check):
    frozen_digest(BASE_MANIFEST, BASE_SHA)
    frozen_digest(DIAGRAMS, DIAGRAM_SHA)
    frozen_digest(INTROW, INTRO_SHA)
    base = read_json(BASE_MANIFEST)
    v16 = copy.deepcopy(base)
    intro = read_json(INTROW)
    require(set(intro) == {"introduction"} and isinstance(intro["introduction"], str),
            "Expected exactly the author's introduction field")
    v16["introduction"] = intro["introduction"]
    old = chapter_map(base["chapters"], BASE_MANIFEST)
    new = chapter_map(base["chapters"], TARGET)
    require(set(new) == set(old) == set(FROZEN) == set(SUMMARIES), "chapter set")
    source_receipts = {}
    for c in v16["chapters"]:
        cid = c["id"]
        ch = new[cid]
        final_sha = frozen_digest(ch.path, FROZEN[cid])
        source_receipts[cid] = {"file": ch.path.name, "v15_sha256": sha(old[cid].path.read_bytes()),
                                "v16_sha256": final_sha, "bytes": len(ch.path.read_bytes())}
        c["title"] = ch.title
        c["summary"] = SUMMARIES[cid]
        require(ch.sections() == old[cid].sections(), f"Authored heading changed in {cid}")
        major = [r for r in ch.sections() if r["level"] == 2]
        c["section_ids"] = [r["id"] for r in major]
        c["sections"] = [dict(id=r["id"], title=r["title"]) for r in major]
    v16["sections"] = [r for ch in new.values() for r in ch.sections()]
    sections = {r["id"]: r for r in v16["sections"]}
    old_section_ids = {r["id"] for r in base["sections"]}
    added_sections = [r for r in v16["sections"] if r["id"] not in old_section_ids]
    require([r for r in v16["sections"] if r["id"] in old_section_ids] == base["sections"],
            "Public section order, label or enclosing chapter changed")
    require([r["id"] for r in added_sections] == ["ch04-irregular-collision"],
            "Unexpected change in deployed section metadata")
    v16["references"] = references(new, v16["sections"])

    quote_receipts = []
    used_selectors = set()
    source_drift = []
    for key, field, context_field in (("terms", "definition", "definition_ref"),
                                     ("theorems", "statement_excerpt", "context_ref")):
        for r in v16[key]:
            ident = r["id"]
            cid = r["chapter_id"]
            before = r[field]
            old_ch, ch = old[cid], new[cid]
            require(old_ch.text.count(before) == 1, f"Deployed quotation not unique: {ident}")
            prev = old_ch.text.index(before)
            prev_range = {"start": prev, "end": prev + len(before)}
            if "source_range" in r and r["source_range"] != prev_range:
                source_drift.append(dict(id=ident, stored=r["source_range"], actual=prev_range))
            exact_count = ch.text.count(before)
            if ident in SELECTIONS:
                start, passage = ch.span(*SELECTIONS[ident])
                used_selectors.add(ident)
            else:
                require(exact_count == 1, f"Missing or ambiguous carried quotation: {ident}")
                start, passage = ch.text.index(before), before
            require(ch.text.count(passage) == 1, f"New quotation not unique: {ident}")
            require(passage == ch.text[start:start + len(passage)], f"Nonverbatim {ident}")
            sec = ch.section_at(start)
            require(sec == r["section_id"] == ch.section_at(start + len(passage) - 1),
                    f"Unexpected source section or boundary for {ident}")
            require(sec == cid or sections[sec]["chapter_id"] == cid, ident)
            require(r[context_field] == sec, f"Original public context changed for {ident}")
            require(r.get("definition_is_verbatim", r.get("statement_is_verbatim")),
                    f"Expected a verbatim source binding for {ident}")
            r[field], r["section_id"], r[context_field] = passage, sec, sec
            r[RESULT_RANGE] = {"start": start, "end": start + len(passage)}
            quote_receipts.append({"id": ident, "kind": key, "chapter": cid, "section": sec,
                                   "target": r.get("rendered_anchor", sec),
                                   "v15_quote_unique_in_v16": exact_count == 1,
                                   "excerpt_changed": before != passage,
                                   "explicit_selector": SELECTIONS.get(ident),
                                   "v15_codepoints": prev_range, **span_record(ch, start, passage)})
    require(used_selectors == set(SELECTIONS), "Unknown selection ID")
    require([d["id"] for d in source_drift] == ["term-consecutive-cut"], "Unexpected v15 range drift")
    for group in ("parts", "chapters", "sections", "references", "terms", "theorems", "figures", "diagrams", "routes"):
        check_unique(v16[group], group)
        if group != "sections":
            require([r["id"] for r in v16[group]] == [r["id"] for r in base[group]], group)
    require(v16["routes"] == base["routes"] and v16["parts"] == base["parts"], "Route/part drift")
    require(v16["references"] == base["references"], "Unexpected numbered reference change")
    require(v16["diagrams"] == read_json(DIAGRAMS)["diagrams"], "Diagram metadata drift")
    for section in ("diagrams", "figures"):
        for row in v16[section]:
            ch = new[row["chapter_id"]]
            heading = sections[row["section_id"]]
            require(heading["chapter_id"] == ch.id, f"Misbound graphic {row['id']}")
            matches = list(re.finditer(r"^:::[ \t]*figure[ \t]+" + re.escape(row["id"]) +
                                       r"[ \t]*$", ch.text, re.M))
            require(len(matches) == 1, f"Graphic placements: {row['id']}")
            # A figure can be keyed to the parent section of the subsection containing its hook.
            h = next(i for i in ch.heads if i[3] == row["section_id"])
            section_end = next((i.start() for i in ch.heads
                                if i.start() > h.start() and len(i[1]) <= len(h[1])), len(ch.text))
            require(h.start() < matches[0].start() < section_end, f"Graphic outside section: {row['id']}")
            for node in row.get("nodes", []):
                dest = node["definition_ref"]
                require(sections[dest["section_id"]]["chapter_id"] == dest["chapter_id"],
                        f"Unresolved diagram node: {row['id']}/{node['id']}")
            for equation in row.get("equation_refs", []):
                require(ch.text.count(r"\tag{" + equation + "}") == 1,
                        f"Unresolved equation ({equation}) on {row['id']}")
    for c, prev in zip(v16["chapters"], base["chapters"]):
        require(all(c[k] == prev[k] for k in ("id", "part_id", "number", "path", "prerequisites", "key_terms")),
                f"Chapter route drift: {c['id']}")
    blob = encoded(v16)
    receipt = {
        "baseline_manifest": str(BASE_MANIFEST), "baseline_manifest_sha256": BASE_SHA,
        "v16_manifest_sha256": sha(blob), "v16_manifest_bytes": len(blob),
        "introduction_file_sha256": INTRO_SHA,
        "introduction_field_sha256": sha(v16["introduction"].encode("utf-8")),
        "diagram_records_sha256": DIAGRAM_SHA, "v15_binding_tool_sha256": sha((PREVIOUS_TOOLS / "sync.py").read_bytes()),
        "chapter_sources": source_receipts, "number_of_records": {
            k: len(v16[k]) for k in ("chapters", "sections", "terms", "theorems", "references", "diagrams", "figures", "routes")},
        "section_rows_restored_from_deployed_source": added_sections,
        "stale_v15_term_offsets": source_drift, "quotes": quote_receipts,
        "offsets": "start/end are half-open Unicode code-point offsets; byte offsets are UTF-8, also half-open; lines are 1-based and inclusive."
    }
    write_or_check(TARGET, blob, check)
    write_or_check(BINDINGS, encoded(receipt), check)
    print(f"{receipt['v16_manifest_sha256']}  {len(blob)} bytes, {len(quote_receipts)} unique quotations; "
          f"{sum(r['excerpt_changed'] for r in quote_receipts)} changed or extended.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    main(parser.parse_args().check)
