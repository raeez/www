from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

def tex(s):
    return re.sub(r"\*([^*]+)\*", lambda m: r"\emph{" + m[1] + "}", s).replace("\u00a0", "~")

def replace(text, old, new, suffix):
    if suffix == "tex":
        old, new = tex(old), tex(new)
    pattern = r"\s+".join(re.escape(v) for v in old.split())
    assert len(re.findall(pattern, text)) == 1, (suffix, old)
    return re.sub(pattern, lambda m: new, text)

for suffix in ("md", "tex"):
    path = ROOT / "content/reader-papers" / f"institutional-computation-explained.{suffix}"
    text = path.read_text()
    for old, new in [
        ("A delegation is a recorded grant of specified permission.",
         "Once the act is specified, the acceptance step must establish who may perform it. A delegation is a recorded grant of specified permission."),
        ("*Recognition* gives stated local effect to another authority's determination under an applicable rule or instrument.",
         "An institutional workflow may need a determination already made by another authority. *Recognition* gives that determination stated local effect under an applicable rule or instrument."),
        ("*Accession* means joining a common instrument through an authority's own signed filing.",
         "Authorities can establish recognition terms through *accession*: joining a common instrument through an authority's own signed filing."),
        ("They establish no relation between B and C. The common instrument establishes this pattern of relations",
         "They establish no relation between B and C"),
    ]:
        text = replace(text, old, new, suffix)
    path.write_text(text)

    path = ROOT / "content/reader-papers" / f"rules-evidence-and-local-decisions.{suffix}"
    text = path.read_text()
    if suffix == "md":
        start = text.index("## 6 The cheapest plan")
        middle = text.index("## 7 Recognition leaves")
        end = text.index("## 8 What the formal")
        cost = text[start:middle].replace("## 6 The cheapest", "## 7 The cheapest", 1)
        local = text[middle:end].replace("## 7 Recognition", "## 6 Recognition", 1)
    else:
        start = text.index(r"\section{The cheapest plan")
        middle = text.index(r"\section{Recognition leaves")
        end = text.index(r"\section{What the formal")
        cost, local = text[start:middle], text[middle:end]
    text = text[:start] + local + cost + text[end:]
    text = replace(text,
                   "Evidence acquisition can consume money or effort.",
                   "A cost comparison must retain these evidence and admission conditions. Evidence acquisition can consume money or effort.", suffix)
    # The source's long exception and impossibility qualifications stay beside their results.
    path.write_text(text)

    path = ROOT / "content/reader-papers" / f"recognition-across-independent-authorities.{suffix}"
    text = path.read_text()
    for old, new in [
        ("Selective disclosure permits a recipient to learn a stated result without receiving the complete source record.",
         "Evidence reuse can also reveal information about the source record. Selective disclosure permits a recipient to learn a stated result without receiving the complete source record."),
        ("An actor must choose using information it can actually observe.",
         "To satisfy privacy and permission together, an actor must choose using information it can actually observe."),
    ]:
        text = replace(text, old, new, suffix)
    # Break paragraphs only where their question changes.
    for old, new in [
        ("The underlying results concern stated mathematical models.", "\n\nThe underlying results concern stated mathematical models."),
        ("A false condition supplies no carried support.", "\n\nA false condition supplies no carried support."),
        ("Complementary admissible evidence can instead contribute", "\n\nComplementary admissible evidence can instead contribute"),
        ("The inspections can use only three slots before their deadline.", "\n\nThe inspections can use only three slots before their deadline."),
        ("A further answer", "\n\nA further answer"),
        ("Information alone permits row choices", "\n\nInformation alone permits row choices"),
        ("The permitted reservation menu is finite", "\n\nThe permitted reservation menu is finite"),
    ]:
        text = replace(text, old, new, suffix)
    path.write_text(re.sub(r"[ \t]+\n", "\n", text))

print("Applied paired composition revisions and moved local permission before cost planning")
