from collections import Counter
from pathlib import Path
import difflib
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
BASELINE = "a0d011c46811837a7f5fb1d1aa60cd457b68dd00"
NAMES = ["institutional-computation-explained", "rules-evidence-and-local-decisions", "recognition-across-independent-authorities"]
PUBLIC_PATTERN = re.compile(r"~/(?:kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|/Users/[^/ ]+/(?:kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|kernel/formal|kernel/docs|kernel/mez|kernel/\.claude|centcom/")
EXTERNAL_PATTERN = re.compile(r"\b(v[0-9]+|version\s+[0-9]|prior\s+draft|previous\s+(draft|version)|superseded|post-(M|W|L|R|Z)[0-9]|phase\s+L[0-9]|to\s+our\s+knowledge|we\s+believe|essentially|basically)", re.I)

def inventory(text, ext):
    if ext == "md":
        cites = re.findall(r"\\\[.*?\\\]", text, flags=re.S)
        maths = re.findall(r"\$\$.*?\$\$|\$[^$]*?\$", text, flags=re.S)
        refs = text.split("## References", 1)[1]
        ids = re.findall(r"`[^`]+`", text)
    else:
        cites = re.findall(r"\\cite(?:\[[^\]]*\])?\{[^{}]*\}", text)
        maths = re.findall(r"\\\[.*?\\\]|\\\(.*?\\\)|\$[^$]*?\$", text, flags=re.S)
        refs = text.split(r"\begin{thebibliography}", 1)[1]
        ids = re.findall(r"\\texttt\{[^{}]*\}", text)
    return {
        "citations": Counter(cites),
        "math": Counter(maths),
        "numbers": Counter(re.findall(r"\d+(?:[.,:]\d+)*", text)),
        "references": refs,
        "identifiers": Counter(ids),
    }

def normalized_body(text, ext):
    if ext == "md":
        text = text.split("## References")[0]
        text = re.sub(r"^# .*\n|^## Abstract\n", "", text, flags=re.M)
        text = re.sub(r"^(##) \d+ ", r"\1 ", text, flags=re.M)
        text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.S)
        text = re.sub(r"\$\$.*?\$\$|\$[^$]*?\$", "MATH", text, flags=re.S)
        fmt = "markdown"
    else:
        text = text.split(r"\begin{abstract}", 1)[1].split(r"\begin{thebibliography}", 1)[0]
        text = text.replace(r"\end{abstract}", "")
        # Pandoc's reader drops labels for this enumitem option. Normalize the option only in this check's input.
        text = text.replace(r"\begin{description}[style=nextline]", r"\begin{description}")
        text = re.sub(r"\\cite(?:\[[^\]]*\])?\{[^{}]*\}", "", text)
        text = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)|\$[^$]*?\$", "MATH", text, flags=re.S)
        fmt = "latex"
    result = subprocess.run(["pandoc", "-f", fmt, "-t", "plain", "--wrap=none"], input=text, text=True, capture_output=True, check=True)
    text = result.stdout.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "–": "--", "—": "---"}))
    return re.sub(r"\s+", " ", text).strip()

report = {"baseline": BASELINE, "files": {}, "body_parity": {}, "mechanical_language_scan": {}}
patch = []
for name in NAMES:
    bodies = []
    for ext in ["md", "tex"]:
        rel = Path("content/reader-papers") / f"{name}.{ext}"
        raw_rel = Path("materials/raw/2026-09-09-accessible-papers") / rel.name
        original_bytes = (ROOT / raw_rel).read_bytes()
        baseline_bytes = subprocess.run(["git", "show", f"{BASELINE}:{raw_rel}"], cwd=ROOT, capture_output=True, check=True).stdout
        assert original_bytes == baseline_bytes, f"Raw source changed: {raw_rel}"
        original = original_bytes.decode()
        revised = (ROOT / rel).read_text()
        before, after = inventory(original, ext), inventory(revised, ext)
        for key in before:
            assert before[key] == after[key], (rel, key, before[key], after[key])
        assert not PUBLIC_PATTERN.search(revised), f"Private source reference: {rel}"
        assert not EXTERNAL_PATTERN.search(revised), f"External process wording: {rel}"
        if ext == "md":
            targets = re.findall(r"\]\(#([^)]*)\)", revised)
            anchors = set(re.findall(r"\{#([^ }]+)", revised))
            assert set(targets) <= anchors, (rel, set(targets) - anchors)
        report["files"][str(rel)] = {
            "raw_unchanged_from_baseline": True,
            "raw_sha256": hashlib.sha256(original_bytes).hexdigest(),
            "maintained_sha256": hashlib.sha256(revised.encode()).hexdigest(),
            "citation_count": sum(after["citations"].values()),
            "math_segment_count": sum(after["math"].values()),
            "number_token_count": sum(after["numbers"].values()),
            "citations_math_numbers_references_identifiers_preserved": True,
            "public_source_scan": "pass",
            "external_process_scan": "pass",
        }
        bodies.append(normalized_body(revised, ext))
        patch.extend(difflib.unified_diff(original.splitlines(True), revised.splitlines(True), fromfile="a/" + str(rel), tofile="b/" + str(rel)))
    assert bodies[0] == bodies[1], (name, "MD/TeX prose differs", "\n".join(difflib.unified_diff(bodies[0].split(), bodies[1].split(), n=5)))
    report["body_parity"][name] = "pass: complete body and section order, normalized format syntax; exact math and citation inventories checked separately"
    # Screening only. It is not certification against the official STE dictionary.
    text = (ROOT / "content/reader-papers" / (name + ".md")).read_text().split("## References")[0]
    text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$|\$[^$]*?\$", "MATH", text, flags=re.S)
    text = re.sub(r"\{[^}]*\}", "", text)
    long_sentences, long_paragraphs = [], []
    for paragraph in text.split("\n\n"):
        if paragraph.lstrip().startswith(("#", ":")):
            continue
        sentences = re.split(r"(?<=[.!?])\s+", paragraph.strip())
        for sentence in sentences:
            if len(re.findall(r"[\w]+(?:[-’'][\w]+)*", sentence)) > 25:
                long_sentences.append(sentence)
        if len(sentences) > 6:
            long_paragraphs.append(paragraph)
    assert not long_sentences and not long_paragraphs, (name, long_sentences, long_paragraphs)
    report["mechanical_language_scan"][name] = {"sentences_over_25_words": 0, "paragraphs_over_6_sentences": 0, "scope": "descriptive body prose; citations, formula payloads, headings and reading-map entries excluded; author review still required"}

(ROOT / ".editorial/editorial.diff").write_text("".join(patch))
(ROOT / ".editorial/checks.json").write_text(json.dumps(report, indent=2) + "\n")
print("PASS: six raw files match baseline byte for byte")
print("PASS: exact citation, math, numerical, reference and identifier inventories preserved in all six maintained files")
print("PASS: full MD/TeX prose and section-order parity for all three works")
print("PASS: public-source, external-process and local citation-anchor checks")
print("PASS: focused sentence/paragraph screening; not a formal STE certification")
print("Wrote .editorial/checks.json and .editorial/editorial.diff")
