from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
CHANGES = {
    "institutional-computation-explained": [
        ("This case establishes the article's central distinction. ", ""),
        ("The next evaluation must identify the proposed act just as carefully.",
         "The evaluation must also identify the exact proposed act."),
        ("The rule's factual dependencies require equal care.",
         "The acceptance step must also check the facts on which its rule depends."),
        ("Dependency completeness concerns changes considered together.",
         "Complete dependency tracking must account for changes that act together."),
        ("That last premise has an institutional source.",
         "Current authority information must come from the responsible institution."),
        ("Each of these numbers answers a different question. An allowance bounds permitted expenditure. A cash balance records available money in its named estate.",
         "An allowance bounds permitted expenditure, while a cash balance records available money in its named estate."),
        ("Its completeness matters because the guarantee covers that list. An omitted provider failure cannot acquire coverage from the theorem.",
         "The guarantee covers only the listed events and outcomes. It excludes any omitted provider failure."),
        ("The source's synthetic collection workload makes the benefit concrete.",
         "The source illustrates evidence reuse with a synthetic collection workload."),
        ("Recognition through an intermediary requires further attention to every restriction and question along the route.",
         "Recognition through an intermediary must account for every restriction and question along the route."),
        ("Its supporting evidence and current permission require their own records.",
         "The supporting evidence and that permission require separate records."),
        ("Joining the same instrument therefore permits this specific pattern of relations", "The common instrument establishes this pattern of relations"),
        ("The authority and continuation paper retains open work on formal mechanization, distributed histories, external effects, legal translation, judgment governance, and information disclosure",
         "*Programmable Institutions* retains open work on formal mechanization, distributed histories, external effects, legal translation, judgment governance, and information disclosure"),
        ("The entity paper leaves the completeness of its institutional vocabulary and the prevalence of required human judgment open.",
         "*One Entity in Many Jurisdictions* leaves the completeness of its institutional vocabulary and the prevalence of required human judgment open."),
        ("The accession paper requires separate evidence for intermediary legal effect, actual willingness, repeated use, detection, collection, and qualified service capacity.",
         "*Accession Networks* requires separate evidence for intermediary legal effect, actual willingness, repeated use, detection, collection, and qualified service capacity."),
    ],
    "rules-evidence-and-local-decisions": [
        ("Establishing which extension governs, who granted it, and what remains due requires a richer record.",
         "Establishing which extension governs, who granted it, and what remains due requires a record of authority and outstanding duties."),
        ("This example separates a calculation from its justification. The calculation compares dates. The justification identifies a rule, an authorized exception, its scope, and the evidence that connects it to the filing.",
         "The date calculation needs a justification that identifies the rule, the authorized exception, its scope, and the evidence connecting it to the filing."),
        ("begins with this recognition problem and develops the structures needed to preserve it.",
         "develops structures that retain this distinction when authorities recognize each other's results."),
        ("The selected result also does not describe every computation that occurred. The stated runtime evaluates the base, guards, and satisfied exception bodies before selecting by priority. Its effect accounting must therefore include evaluated bodies whose results do not win. An effect is an interaction such as reading evidence or requesting an authorized judgment. Choosing one final value does not erase those interactions.",
         "Evaluating a rule can have effects, such as reading evidence or requesting an authorized judgment. The stated runtime evaluates the base, guards, and satisfied exception bodies before selecting by priority. Its effect accounting must include every evaluated body, even when its result is not selected."),
        ("Legal time presents another choice of context.", "Time also needs an explicit legal context."),
        ("Some missing inputs require computation. Others require judgment.",
         "A missing input may require computation or an authority's judgment."),
        ("it specifies the kind of answer needed without pretending that an answer exists.",
         "it specifies the kind of answer needed while leaving the answer unresolved."),
        ("Its content identity matters independently of a convenient version label.",
         "Its content identity matters independently of its version label."),
        ("These distinctions allow a mathematical result about an authorization record to remain useful without treating it as a source of sovereign authority.",
         "A theorem about this authorization record supplies no sovereign authority."),
        ("Not every permissible act requires a new discretionary signature. ", ""),
        ("The last can support automatic computation when its conditions hold.",
         "The last can support automatic computation when its conditions hold, without a new discretionary signature."),
        ("A grade is not an applicability record", "Grades and applicability records"),
        ("A threshold says how much evidence-derived grade a classification requires.",
         "A threshold specifies the evidence-derived grade required for a classification."),
        ("The bit-triangle example makes the problem sharper.", "Consider the bit-triangle example."),
        ("The positive result needs additional structure.",
         "The exact compatibility result requires a particular arrangement of the local tables."),
        ("The saving follows from the specified offers and costs, not from a general promise that evidence reuse is cheaper.",
         "This saving depends on the specified offers and costs. Evidence reuse need not be cheaper in other cases."),
        ("A direct complete offer costing\u00a03 then wins.", "A direct complete offer costing\u00a03 then costs less."),
        ("A finite catalogue is a substantive assumption.", "The exact search assumes a finite catalog."),
        ("the catalogue contains every available source", "the catalog contains every available source"),
        ("The old decision remains replayable in its old context. A new decision must use the new context. This is the same distinction that protected both deadlines in the filing case.",
         "The old decision remains replayable in its old context, while a new decision must use the new context. As in the filing case, each assessment retains the context in which its evidence applied."),
        ("proves substantial results about a specified structural source calculus.",
         "proves results about a specified structural source calculus."),
        ("The useful conclusion is precise: preserved records and exact finite models support compositional decisions without erasing their conditions.",
         "Preserved records and exact finite models support compositional decisions while retaining their conditions."),
    ],
    "recognition-across-independent-authorities": [
        ("Making this arrangement reliable requires the source assertion, receiving rule, and current authority to remain separately identifiable.",
         "Reliable reuse requires the source assertion, receiving rule, and current authority to remain separately identifiable."),
        ("Finally, accession can reproduce bilateral relations", "Accession can reproduce bilateral relations"),
        ("The carrying domains and fresh questions can overlap.",
         "Domains covered by recognition can also contain fresh questions."),
        ("The resulting division of work permits reuse without repeating the source examination. South remains responsible for its own rule, decision, and resulting duties.",
         "South can therefore reuse North's examination while retaining responsibility for its own rule, decision, and resulting duties."),
        ("The record of recognition supplies the evidence for that division throughout later use.",
         "The recognition record preserves evidence of this division of work throughout later use."),
        ("The attempt resolves its terminal abort before recalculating the dependencies and preparing again.",
         "The attempt must resolve with a terminal abort before the program recalculates dependencies and prepares again."),
        ("Qualified time supplies a concrete example.",
         "The capacity limit can depend on when qualified workers are available."),
        ("This is why total staffing cannot establish timely completion.",
         "Total staffing alone cannot establish that each task has an eligible slot before its deadline."),
        ("Its assumptions matter. ", ""),
        ("Changed snapshots retain that history.",
         "The disclosure history must also account for changes to the source values."),
        ("An empty common action set supplies a precise obstruction.",
         "If that common action set is empty, no such policy exists."),
        ("Merely naming that action cannot repair the obstruction.",
         "A name alone supplies none of these conditions."),
        ("The last hypothesis concerns willingness. The public rules do not establish it.",
         "The willingness hypothesis needs evidence beyond the public rules."),
        ("One deposit per authority also leaves continuing work.",
         "Notice and later updates still require work after the deposits."),
        ("Authentic source records, faithful instrument interpretation, complete observations, durable implementation, and institutional performance remain the precise obligations of each application.",
         "Each application must establish authentic source records, faithful instrument interpretation, complete observations, durable implementation, and institutional performance."),
        ("licence", "license"),
        ("fibre", "fiber"),
    ],
}


def tex_text(value):
    value = re.sub(r"\*([^*]+)\*", lambda m: r"\emph{" + m.group(1) + "}", value)
    return value.replace("\u00a0", "~")


log = []
for name, changes in CHANGES.items():
    for suffix in ("md", "tex"):
        path = ROOT / "content" / "reader-papers" / f"{name}.{suffix}"
        text = path.read_text()
        for old, new in changes:
            if suffix == "tex":
                old, new = tex_text(old), tex_text(new)
            pattern = r"\s+".join(re.escape(s) for s in old.split())
            if old.endswith(" "):
                pattern += r"\s+"
            matches = list(re.finditer(pattern, text))
            expected_multiple = old in ("licence", "fibre")
            assert len(matches) >= 1 and (len(matches) == 1 or expected_multiple), (path.name, old, len(matches))
            text = re.sub(pattern, lambda m: new, text)
            log.append(f"{path.name}: {old!r} -> {new!r} ({len(matches)})")
        path.write_text(text)
(ROOT / ".editorial" / "applied-edits.txt").write_text("\n".join(log) + "\n")
print(f"Applied {len(log)} paired source substitutions")
