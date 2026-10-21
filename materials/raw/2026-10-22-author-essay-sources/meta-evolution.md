# How Rules Evolve

**Raeez Lorgat, April 2026**

---

Tax rates adjust, licensing requirements tighten, and legislatures replace regulatory frameworks when they reject the old approach.

A rule system must encode how its rules change and decide which rules, if any, it places beyond amendment.

## The re-evaluation problem

When a rule changes, the status of everything evaluated under the old rule must be resolved.

Consider a jurisdiction that raises its minimum capital requirement for financial institutions from \$1 million to \$5 million. Entity $A$ was evaluated last month under the old rule and found compliant with \$3 million in capital. Under the new rule, entity $A$ is non-compliant. What is entity $A$'s status?

Legal systems apply the principle of *temporal application*, *tempus regit actum*: an act is governed by the law in force when it was performed. Both evaluations of $A$ remain true under their respective rules. Last month's evaluation records compliance then. From the new rule's effective date, $A$ is non-compliant and must raise capital, restructure, or exit. The question "What is $A$'s status?" requires a time and rule version. The system must retain both answers and their contexts.

If rule changes silently invalidated prior evaluations, audits, compliance certificates, and verifications would remain subject to revision whenever a relevant rule changed. No one could know whether an evaluation would still count as valid next month. Such a record could not serve as reliable evidence.

The default principle is that *an evaluation's validity is judged under the rules in force at evaluation, not those in force at audit*.

Legal systems provide exceptions to that default. A court may invalidate a framework from inception and immediately affect operations in flight. *Schrems II* (Court of Justice of the European Union, C-311/18, 2020) invalidated the EU-U.S. Privacy Shield. Transfers relying on it lost their legal basis immediately, before their next evaluation. Legislatures may constitutionally enact curative and retroactive tax statutes (*United States v. Carlton*, 512 U.S. 26 (1994)). Procedural rules also routinely apply to pending matters.

The record preserves the earlier evaluation of what the law said and what was decided. An invalidation or retroactive statute enters as a new, dated event, followed by a re-evaluation under the changed law. The companion paper *Lex: A Logic for Jurisdictional Rules* gives these events typed form. The system appends them without mutating the earlier record.

## Version chains

Verifying a historical evaluation requires the rules that governed it. The system therefore retains the current rule and every predecessor in a traversable *version chain*. Overwriting an old rule would remove the basis for verification.

A *version* carries its rule content, the versions it supersedes, its effective interval, and its publication time. Effective time and publication time are distinct. A rule published in March may take effect in June, while a curative statute enacted in June may be effective from January. This is the valid-time/transaction-time distinction of temporal databases (Snodgrass and Ahn 1985). The companion paper *Time in Institutional Computing* develops its use in institutional records.

A version is *active at time $t$ as of publication time $\tau$* when $t$ lies within its effective interval as recorded at $\tau$. At publication, a successor adds an entry closing its predecessor's effective interval at the successor's effective start. The earlier entry remains. The June statute and its predecessor can therefore both cover March 15th, as viewed at different publication times. Before the statute's publication, the predecessor is active on March 15th. After publication, the statute is active on March 15th.

To answer "Which version was active on March 15th?", the system reads effective intervals as of a named time. Walking backward from the current version in publication order would conflate the two coordinates.

An *evaluation record* binds the verdict to the entity, consulted facts or their commitment, governing version, and evaluation time. A regulator asking "was this entity compliant on March 15th?" must name the time as of which the law is read. March 15th itself selects the law governing the act then. The present selects the law as subsequently rewritten. The answer uses that active version and the record evaluated against it. Losing or overwriting versions makes this question unanswerable.

This paper assumes that each version after the first supersedes exactly one predecessor and has at most one successor. Versions therefore form a chain. Concurrent amendments to different parts of a rule and partial repeals require a directed acyclic graph. One version may then supersede several, or several may supersede one, with activity at $t$ resolved per part. The definitions extend to that case, which this paper does not develop.

The chain supports *delta computation*: comparing a version with its predecessor identifies exactly what changed. Only evaluations that depended on the changed portion can differ. The delta therefore identifies candidates for re-evaluation, but their verdicts determine which entities actually change status. Evaluating the candidates under both versions gives the affected set. Transitions use the same comparison at full scale.

## Replayable evaluations

Rule systems with evidentiary obligations need precise guarantees about historical evaluations. Backwards compatibility, understood as a best-effort promise that new versions preserve old behavior, leaves those guarantees unstated.

Four conditions make evaluations *verifiable*: alteration of a decision or its governing text becomes detectable. Versions are *content-addressed*, with each identified by a cryptographic hash of its content. Editing the text produces a different version and identifier, while existing records still name the original. Evaluation records are *committed*: they contain the version hash, fact-snapshot hash, and verdict in a log anchored outside the system's control. The same log commits effective intervals. The evaluator is *deterministic*, so the same version and facts yield the same verdict.

A fifth condition, *retention*, makes evaluations *replayable*. Whoever replays must have the version text and fact snapshot identified by the log's hashes. The log certifies those materials without containing them.

From the log alone, a third party can detect retroactive alteration of a version, effective interval, or evaluation record. With the certified version text and fact snapshot, that party can also rerun the evaluation and check its verdict. The argument has three steps. Altering version content changes its hash and breaks references to it, unless the adversary produces a hash collision. The external anchor exposes alterations to committed records or intervals. Deterministic replay then either reproduces the recorded verdict or detects a discrepancy.

Replay certifies what was evaluated, against which text, and with what result. It does not certify legal soundness: a mis-drafted rule replays perfectly. If evaluation used an external oracle or human judgment, replay reproduces only the committed answer, not its source. A successor version need not preserve prior evaluations itself. Each record remains bound by hash to the version that produced it, beyond the successor's reach.

## Refinements and replacements

A threshold change, deadline extension, or added category refines an existing framework. A replacement introduces a new regulatory approach. The distinction determines how historical evaluations can be read.

A refinement uses the old framework's terms. Raising the minimum capital requirement from \$1M to \$5M changes its value while preserving what "minimum capital requirement" means. Historical evaluations remain interpretable without translation.

Replacing principles-based securities regulation with rules-based regulation changes the categories of evaluation. A status of "compliant" under the former may have no counterpart under the latter, because the frameworks ask different questions.

Distinguish three levels of change by what the change preserves.

1. **Value changes.** The evaluator is unchanged; a parameter differs -- a number, a date, a list entry. Old and new evaluations answer the same question and are directly comparable.

2. **Schema changes.** The structure of the rule's inputs or categories changes, but a total mapping carries every old status to a new one, together with an explicit *loss set*: the propositions the mapping fails to preserve. Historical evaluations translate, and the loss set states exactly what the translation dropped.

3. **Replacements.** The approach itself changes -- "paradigm" in Kuhn's (1962) sense, and with Kuhn's consequence: some historical evaluations are *incommensurable* with the new framework. They answer a question the new framework does not ask, so no mapping carries them anywhere. They are preserved as records, interpretable under the framework that produced them and not re-derivable under the new one.

The existing machinery handles value changes. Schema changes add a mapping and its loss set. Replacements change the framework in which those two kinds of change are measured. *Meta-evolution* names this change of framework.

## The self-revision paradox

Version chains, evaluation records, and supersession also depend on rules: who may propose changes, how proposals are reviewed, and how old and new rules interact. Hart (1961) called these *rules of change*. They too require a procedure for amendment.

Ross (1969) posed the paradox of self-amendment, examined at book length by Suber (1990). A procedure for changing the rules of change applies to itself. Through a sequence of individually valid amendments, it can therefore become any procedure.

Constitutional systems respond differently. Germany's Article 79(3) of the Basic Law places human dignity and the federal and democratic order beyond amendment. Article V of the United States Constitution shields only equal state suffrage in the Senate. The United Kingdom entrenches nothing, relying on convention for continuity.

New Zealand uses single entrenchment. Section 268 of the Electoral Act 1993 protects six reserved provisions, including Parliament's three-year term and the voting age. Amending them requires three-quarters of all House members or a referendum. Section 268 itself can be amended by simple majority, so its one-layer protection also ultimately rests on convention. Entrenchment is a design choice rather than a general property of legal systems.

A rule system whose evaluations serve as evidence must protect the process that gives them continuity. Entrenching only *the system can revise itself* is insufficient. A procedure amended into "any party may change any rule at any time" still satisfies that axiom. It supplies neither continuity nor a basis for long-term commitment.

The system must instead entrench the founding act that records its origin and the minimum requirements for changing the amendment procedure: the required authority and thresholds. The founding signers remain disjoint from every signer set the amendment process can create. No sequence of individually valid amendments can therefore confer authority to remove those requirements. The process cannot create the founding signatures that authorize that change.

This construction assumes unforgeable signatures and continued custody of founding keys by their holders. A leak reaching the entrenched threshold permits valid steps that dissolve the protection. Key loss below that threshold freezes it, leaving only abandonment, discussed next. Under these assumptions, no amendment path within the system removes the entrenched floor. All other rules, thresholds, and procedures above that floor remain subject to governed change.

Entrenchment governs changes within the system. A community can still abandon it and build a successor. Such abandonment is a level 3 replacement. The preserved record remains interpretable under its original framework, as it does through every replacement.

## Concurrent operation during transitions

During the interval between enactment and full effect, entities evaluated under old and new versions coexist. Operations begun under the old version may also remain in flight.

Each change declares a *transition provision* for evaluations and operations that straddle it. The default permits an operation begun under the old version to finish under that version's terms. An entity partway through a multi-month authorization therefore need not restart when the rules change. A sanctions designation or emergency suspension instead declares a fail-closed transition: affected operations halt, with the halt recorded under the new version. The change declares which provision applies.

During transition, *dual operation* evaluates old and new versions concurrently and tags each evaluation with its governing version. Comparing the same entity yields agreement, disagreement, or a proposition with no counterpart in the other framework. The last outcome indicates level 3 change: the frameworks differ in what they ask. A regulator needs the rates of all three outcomes to judge whether the new rules behave as intended.

The transition ends through a governed process. Entities evaluated under the old version receive a path to re-evaluation, after which that version ceases to govern current activity. It remains part of the record. The question "Was this entity compliant in 2024?" retains a definite answer after the rules change in 2025. The version, facts or their commitments, verdict, and evidence of integrity must survive indefinitely.

The underlying data may have a shorter life. Statutes limit retention, and data-protection law grants erasure rights, as in Article 17 of the GDPR. Erasing a fact snapshot leaves an evaluation *verifiable*: its commitments still establish the decision and governing text. It ceases to be *replayable*. The system must track this change of class.

## The permanent next paradigm

Replacements are the hardest transitions, and their late announcement leaves little preparation time. Starting translation work only then risks a rushed, lossy mapping or prolonged incompatibility.

The system can instead maintain and test the most plausible next framework. If evidence points toward rules-based securities regulation, it can begin translating from the principles-based framework before any announcement. Preparation includes a draft mapping, its computed loss set, candidate incommensurable propositions, and parallel evaluation of live records.

If the forecast is wrong, the specific mappings into the anticipated framework are discarded. The work still exercises reusable methods for translation, loss-set computation, incommensurability testing, tagged dual operation, and interpretation of divergent results. An actual transition requires those methods whichever framework arrives. Preparation is useful even when the forecast fails.

## Why this matters

Rule systems use familiar software mechanisms: version control, deprecation, and migration. Their evidentiary obligation adds a requirement that ordinary software migration lacks. Deprecated APIs can be replaced in old code. Historical compliance determinations remain relied on by entities, certified by regulators, and enforced by courts, so their original frameworks must remain verifiable.

Version chains preserve institutional continuity through change. They address the question: "the rules have changed -- can you still prove that what we did under the old rules was legitimate?" Failure to retain that evidence undermines decisions made under the prior regime. Retained versions, records bound to their governing versions, and tamper-evident history let new law take effect while preserving the earlier record.

These guarantees retain their conditions. A single version lineage is assumed, with branching histories left to the graph generalization. Replay reproduces committed oracle answers and human judgments without reproducing their sources. Erasure can move a record from replayable to verifiable. Declared fail-closed changes displace the completion default, while retroactive invalidation appends a new evaluation.

The entrenched floor depends on unforgeable signatures and founding-key custody. Leaks reaching the threshold permit valid dissolution, and losses below it freeze amendment. Entrenchment applies only within the system. After wholesale abandonment, the preserved record remains.

The goal of meta-evolution is governed change to any rule, including amendment procedures above their entrenched floor, with the integrity of prior acts preserved. Version chains and hash-bound records preserve their context. Declared transition provisions and dual operation govern replacement. Founding signatures, which the amendment process cannot create, protect the minimum conditions for that process.

## References

Hart, H. L. A. (1961). *The Concept of Law.* Oxford University Press.

Kuhn, T. S. (1962). *The Structure of Scientific Revolutions.* University of Chicago Press.

Ross, A. (1969). "On Self-Reference and a Puzzle in Constitutional Law." *Mind*, 78(309), 1–24.

Snodgrass, R. T. and Ahn, I. (1985). "A Taxonomy of Time in Databases." *Proceedings of the ACM SIGMOD International Conference on Management of Data*, 236–246.

Suber, P. (1990). *The Paradox of Self-Amendment: A Study of Law, Logic, Omnipotence, and Change.* Peter Lang.
