"""Validate or install the issued byline edition in an authoring checkout."""

import argparse
from hashlib import sha256
import json
import os
import re
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
import reviewed_io as io

ED = Path("materials/processed/qh-attack-heal-20261116/integration/ega-reader-integration-20261117")
FILES = ("index.html", "reference.html", "atlas.html", "reader-index.js")
AUTHOR = {
    "content/quantum-holography-status/page.json",
    "compiler/quantum-holography-status/monograph.py",
    "compiler/quantum-holography-status/status.py",
}
AUDIT = "compiler/quantum-holography-status/audit.py"


def signature(raw):
    return {"sha256": sha256(raw).hexdigest(), "bytes": len(raw)}


def read(p, wanted=None):
    raw = io.read_stable(p)
    if wanted is not None:
        io.require(
            signature(raw) == {k: wanted[k] for k in ("sha256", "bytes")},
            f"Unexpected bytes in {p}",
        )
    return raw


def obj(p, wanted=None):
    return io.decode(read(p, wanted))


def keeponce(p, body):
    if p.exists():
        io.require(read(p) == body, f"Existing receipt differs in {p}")
    else:
        io.write_new(p, body)


def verify(args):
    edition = args.edition.resolve(strict=True)
    issued = args.issued.resolve(strict=True)
    ver = edition / "verification"
    root = edition.parents[len(ED.parts)]
    io.require(edition == root / ED / "release-v24", "Pass a full checkout release-v24 path")
    order = edition / "LOCAL-READY.json"
    io.require(io.sha(read(order)) == args.accepted_digest, "Wrong reviewed edition")
    ready = obj(order)
    io.require(
        ready["status"] == "READY_FOR_ISSUE" and ready["edition"] == "release-v24",
        "Incomplete issuance archive",
    )
    for rel, val in ready["receipts"].items():
        read(edition / io.relative(rel), val)
    expected = obj(edition / "EXPECTED-PUBLIC.json")
    push = obj(issued / "PUSH.json")
    pub = obj(issued / "PUBLICATION.json")
    bare = obj(issued / "BARE-READBACK.json")
    baseline = obj(ver / "V23-ISSUED-BASELINE.json")
    prev_commit = baseline["commit"]
    commit = push["commit"]
    io.require(
        re.fullmatch(r"[0-9a-f]{40}", commit) is not None, "Expected a full Git commit identifier"
    )
    io.require(
        set(expected) == set(FILES) and push["files"] == expected == ready["public_files"],
        "Issue/readiness file mismatch",
    )
    io.require(
        push["previous"] == prev_commit == ready["base_public_commit"]
        and commit == pub["commit"] == pub["pages"]["commit"]
        and pub["pages"]["status"] == "built",
        "Issue ancestry or Pages deployment mismatch",
    )
    io.require(
        set(push["changed_paths"]) == {"quantum-holography/" + n for n in FILES[:3]},
        "Expected exactly three byline pages",
    )
    route = {r["path"]: r for r in pub["public_readbacks"]}
    io.require(
        set(route)
        == {
            "",
            "quantum-holography-tracker.html",
            "quantum-holography/",
            *("quantum-holography/" + n for n in FILES),
        },
        "Missing public route",
    )
    io.require(
        all(r["exact"] and r["served_sha256"] == r["expected_sha256"] for r in route.values()),
        "A public route mismatched",
    )
    for name in FILES:
        io.require(
            route["quantum-holography/" + name]["served_sha256"] == expected[name]["sha256"],
            "Published bytes mismatch",
        )
    url = pub["url"]
    io.require(
        all(
            bare["served"].get(u) == expected["index.html"]["sha256"]
            for u in (url, url + "index.html")
        ),
        "Canonical book did not serve these bytes",
    )
    parent_src = obj(
        edition.parent / "release-v23/SOURCE-MANIFEST.json", baseline["source_manifest"]
    )
    prior = obj(edition.parent / "release-v23/MANIFEST.json", baseline["manifest"])
    prior_catalog = read(
        edition.parent / "release-v23/compatibility/current-history.json",
        baseline["current_catalog"],
    )
    hist = edition / "compatibility/current-history.json"
    static = edition / "compatibility/history.json"
    io.require(
        read(static) == prior_catalog,
        "Reproducible catalog differs from the issued v23 current catalog",
    )
    frozen = io.decode(prior_catalog)
    io.require(
        frozen["editions"][-1]["commit"] == prev_commit
        and frozen["runtime"] == prior["reader_runtime"],
        "Published v23 catalog runtime mismatch",
    )
    for name in frozen["runtime"].values():
        read(edition / "compatibility" / io.relative(name), frozen["controls"][name])
    actual_parent = (
        subprocess.check_output(
            ["git", "--no-optional-locks", "-C", frozen["repository"], "rev-parse", commit + "^"]
        )
        .decode()
        .strip()
    )
    io.require(actual_parent == prev_commit, "Git first parent mismatch")
    for n in FILES:
        blob = subprocess.check_output(
            [
                "git",
                "--no-optional-locks",
                "-C",
                frozen["repository"],
                "show",
                commit + ":" + frozen["publicPath"] + "/" + n,
            ]
        )
        io.require(signature(blob) == expected[n], "Published git object mismatch for " + n)
    source = obj(edition / "SOURCE-MANIFEST.json")
    plan = obj(ver / "NATIVE-INSTALL-PLAN.json")["files"]
    io.require(
        set(plan) == AUTHOR | {AUDIT},
        "Expected the three byline inputs and its validated native audit",
    )
    native_source = obj(ver / "NATIVE-SOURCE.json")
    read(root / "compiler/build-quantum-holography-reader.py", native_source["entrypoint"])
    io.require(
        len(source["files"]) == 56 and source["content_id"] == ready["content_id"],
        "Source identity mismatch",
    )
    for key in [
        "scientific_horizon_utc",
        "base_scientific_census_utc",
        "targeted_accessions",
        "targeted_accession",
    ]:
        io.require(source[key] == parent_src[key] == prior[key], "Scientific scope changed: " + key)
    reproduced = obj(ver / "REPRODUCTION.json")
    io.require(
        reproduced["status"] == "PASS" and reproduced["files"] == expected, "Reproduction mismatch"
    )
    for name, flag in [("NORMAL-CLI.json", False), ("FROZEN-CLI.json", True)]:
        cli = obj(ver / name)
        io.require(
            cli["edition"] == edition.name and cli["frozen"] is flag and cli["files"] == expected,
            "Native build mismatch",
        )
    raw_record = reproduced["raw"]["reader-index.js"]
    read(edition / "compatibility/controls/v24-raw-index.js", raw_record)
    row = {
        "edition": "v24",
        "commit": commit,
        "pins": expected,
        "rawIndex": {"path": "controls/v24-raw-index.js", **raw_record},
    }
    new_catalog = {**frozen, "editions": [*frozen["editions"], row]}
    new_history = io.enc(new_catalog)
    initial_history = read(hist)
    io.require(initial_history in (prior_catalog, new_history), "Unexpected native history")
    ptr = edition.parent / "CURRENT-EDITION.json"
    initial_ptr = read(ptr)
    parsed_ptr = io.decode(initial_ptr)
    after_ptr_shape = {
        "edition": "release-v24",
        "commit": commit,
        "manifest": "release-v24/MANIFEST.json",
    }
    io.require(
        signature(initial_ptr) == baseline["working_pointer"]
        or all(parsed_ptr.get(k) == v for k, v in after_ptr_shape.items()),
        "The authoring checkout moved off the exact predecessor",
    )
    changed = {}
    root_source = {}
    for rec in source["files"]:
        rel = io.relative(rec["path"]).relative_to("source-tree")
        body = read(edition / "source-tree" / rel, rec)
        site = root / rel
        io.require(site.resolve(strict=True) == site, "Redirected editable source: " + str(site))
        live = read(site)
        root_source[str(rel)] = signature(body)
        if str(rel) in plan:
            item = plan[str(rel)]
            io.require(
                signature(body) == item["to"] and signature(live) in [item["from"], item["to"]],
                "Source drift " + str(rel),
            )
            changed[site] = (live, body)
        else:
            io.require(live == body, "Unrelated editable source drift " + str(rel))
    old_pins = {
        str(io.relative(row["path"]).relative_to("source-tree")): {
            k: row[k] for k in ("sha256", "bytes")
        }
        for row in parent_src["files"]
    }
    io.require(old_pins.keys() == root_source.keys(), "Source inventory differs from v23")
    actual_changes = {name for name in root_source if root_source[name] != old_pins[name]}
    io.require(set(plan) == actual_changes, "Change set differs from archived predecessor")
    raw_index_changes = obj(ver / "AUTHOR-LINK-BYTES.json")
    io.require(
        raw_index_changes["files"] == expected
        and raw_index_changes["search_index_exact"]
        and len(raw_index_changes["pages"]) == 3,
        "Byline-only evidence mismatch",
    )
    edges = obj(ver / "FINAL-LINKS.json")
    native = obj(ver / "NATIVE-AUDIT.json")
    notation = obj(ver / "FINAL-NOTATION.json")
    io.require(
        not native["failures"]
        and not native["math_errors"]
        and notation["status"] == "PASS"
        and not edges["links"]["bad_local_links"],
        "Invalid final rendering or links",
    )
    copies = {
        ("verification/" + name): read(issued / name)
        for name in ["PUSH.json", "PUBLICATION.json", "BARE-READBACK.json"]
    }
    installed = {
        "utc": pub["utc"],
        "public_commit": commit,
        "files": {k: {"native": str(root / k), "installed": row["to"]} for k, row in plan.items()},
        "plan": signature(read(ver / "NATIVE-INSTALL-PLAN.json")),
        "reproduction": signature(read(ver / "REPRODUCTION.json")),
    }
    copies["verification/EDITABLE-INSTALLED.json"] = io.enc(installed)
    digests = {
        **{k: v["sha256"] for k, v in ready["receipts"].items()},
        "LOCAL-READY.json": args.accepted_digest,
        "compatibility/current-history.json": io.sha(new_history),
        **{k: io.sha(b) for k, b in copies.items()},
    }
    final = {
        k: prior[k]
        for k in (
            "schema",
            "scientific_horizon_utc",
            "base_scientific_census_utc",
            "targeted_accessions",
            "targeted_accession",
            "chapters",
            "search_units",
            "authored_opening_figure",
            "source_complementary_receipts",
        )
    }
    final.update(
        edition="v24",
        utc=pub["utc"],
        public_reader=url,
        commit=commit,
        base_public_commit=prev_commit,
        content_id=source["content_id"],
        native_scope="author hyperlinks",
        native_changed_files=sorted(plan),
        reviewed_passage_successors=frozen["reviewedPassageSuccessors"],
        reader_runtime=frozen["runtime"],
        native_inputs=len(source["files"]),
        full_rebuild_matches_published=expected,
        historic_locators_verified=reproduced["historic_locators_verified"],
        local_links_checked=edges["links"]["local_links_checked"],
        formulas_checked=native["math"],
        math_errors=native["math_errors"],
        prior_design_record=prior["native_visual_status"],
        native_visual_status="The bylines and navigation links on the book, reference and atlas were checked at desktop and mobile viewport widths.",
        inherited_science_manifest={"edition": "v23", **baseline["manifest"]},
        receipts=digests,
    )
    final_data = io.enc(final)
    manifest = edition / "MANIFEST.json"
    ptr_data = io.enc({**after_ptr_shape, "sha256": io.sha(final_data)})
    if manifest.exists():
        io.require(
            read(manifest) == final_data, "Existing manifest differs from the verified issue"
        )
    for rel, body in copies.items():
        f = edition / rel
        if f.exists():
            io.require(read(f) == body, "Existing issue record differs " + rel)
    if initial_ptr == ptr_data:
        io.require(
            initial_history == new_history
            and manifest.exists()
            and all(a == b for a, b in changed.values()),
            "Partially installed selected edition",
        )
        for rel, body in copies.items():
            io.require(read(edition / rel) == body, "Installed evidence differs")
        print("Verified existing", commit, "manifest", io.sha(final_data))
        return
    io.require(
        signature(initial_ptr) == baseline["working_pointer"],
        "Previous pointer shape or hash changed",
    )
    if not args.install:
        print(
            "Verified dry run:",
            len(changed),
            "editable changes, 56 sources, manifest",
            io.sha(final_data),
            "history",
            io.sha(new_history),
            "pointer",
            io.sha(ptr_data),
        )
        return
    backup = ver / "editable-install"
    backup.mkdir(exist_ok=True)

    def event(e):
        with (backup / "operations.jsonl").open("a") as f:
            f.write(json.dumps(e) + "\n")
            f.flush()
            os.fsync(f.fileno())

    swaps = []
    created_manifest = not manifest.exists()
    with io.locked_targets([str(x) for x in [*changed, hist, ptr]]) as locks:

        def replace(p, before, after):
            if before != after:
                io.exchange_guarded(p, before, after, backup / "previous", event, locks)
                swaps.append((p, before, after))
            else:
                io.require(read(p) == after, "Concurrent change to " + str(p))

        try:
            for p, (a, b) in changed.items():
                replace(p, a, b)
            replace(hist, initial_history, new_history)
            for rel, body in copies.items():
                keeponce(edition / rel, body)
            for name, expected_pin in root_source.items():
                read(root / name, expected_pin)
            keeponce(manifest, final_data)
            replace(ptr, initial_ptr, ptr_data)
            for p, a, b in swaps:
                io.require(read(p) == b, "Installed bytes changed " + str(p))
        except BaseException:
            for p, a, b in reversed(swaps):
                if read(p) == b:
                    io.exchange_guarded(p, b, a, backup / "rollback", event, locks)
            if created_manifest and manifest.is_file() and read(manifest) == final_data:
                manifest.unlink()
                io.fsync_directory(manifest.parent)
            raise
    print(
        "Installed",
        commit,
        "manifest",
        io.sha(final_data),
        "history",
        io.sha(new_history),
        "pointer",
        io.sha(ptr_data),
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("edition", type=Path)
    p.add_argument("issued", type=Path)
    p.add_argument("accepted_digest")
    p.add_argument("--install", action="store_true")
    verify(p.parse_args())
