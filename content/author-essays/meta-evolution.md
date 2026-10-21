# How Rules Evolve

A financial institution holds \$3 million in capital. Its regulator raises the minimum requirement from \$1 million to \$5 million. Last month's compliant institution now needs more capital, a different structure, or an exit.

The earlier evaluation still matters. Investors, counterparties, and supervisors may have relied on it. They need to know which rule applied, what facts supported the decision, and what the change means for work already underway.

A rule system must keep those questions answerable as the law changes. It must also handle replacements that change the categories in which an earlier decision made sense.

## Preserve the decision and its context

For the capital example, assume the new requirement takes effect prospectively without transitional relief. The institution satisfied the old threshold and fails the new one. Both results belong in its record, each with its rule, evidence, and time.

There are three different questions. What supported the recorded decision? How does the applicable law now assess the earlier event? What may the institution do today? A later law, judgment, or newly discovered fact can change the second or third answer while the first remains historically reproducible.

[Lex](https://research.momentum.inc/papers/lex.html#revocation-and-temporal-tagging) gives these questions separate forms. Historical reconstruction uses the evidence and rules actually recorded. Legal assessment names the legal time, evidence view, and governing policy. Current permission checks the intended act and the stage at which authority must hold.

Retroactive law makes the separation necessary. In *United States v. Carlton*, the Supreme Court upheld a particular retroactive tax amendment. Its reasoning addressed the legitimate legislative purpose, prompt correction, and modest period of retroactivity. The judgment supplies a concrete example of changed legal consequences for an earlier transaction. [Official judgment, pp. 30–35](https://www.govinfo.gov/content/pkg/USREPORTS-512/pdf/USREPORTS-512-26.pdf).

An immediate invalidation creates a different transition. In July 2020, *Schrems II* invalidated the EU–U.S. Privacy Shield without a grace period for transfers relying on that basis. Transfers needed another lawful basis under the applicable rules. The earlier record of reliance still had to survive. [Court of Justice judgment and summary](https://eur-lex.europa.eu/legal-content/EN/SUM/?uri=CELEX%3A62018CJ0311).

The system records an invalidation or retroactive amendment as a new authoritative event. It then records the resulting assessment with its own context. An unrelated later timestamp cannot displace an earlier act. Supersession requires the authority and procedure applicable to that change.

## Two dates, two views of the same day

A rule has an effective time and a publication time. A rule published in March may take effect in June. A curative statute published in June may apply from January.

Suppose an auditor asks which rule governed an event on March 15. The answer also needs an evidence cutoff. The record available on March 15 differs from the record available after June's enactment. The system must preserve both views.

Each rule edition therefore carries its content, predecessor, effective interval, and publication record. A successor adds the authorized change to its predecessor's interval while retaining the earlier entry. Reading the history as of a selected publication cutoff then shows what the record said at that point.

This is the distinction between valid time and transaction time in temporal databases. Institutional records add authority: the event changing an interval must identify who could make that change and on what basis.

A simple version chain gives each edition one predecessor and at most one successor. Concurrent amendments and partial repeals need a graph with activity resolved for the affected parts. The chain is a useful starting model. A complete treatment of branching legal histories needs that further construction.

Comparing successive editions identifies changed rules and the evaluations that depended on them. Those evaluations are candidates for review. Running both rules on the relevant facts establishes which verdicts actually change. A changed threshold need not change every affected institution's result.

## What replay requires

A historical decision needs a stable reference to the exact rules it used. Content addressing supplies that reference through a hash of a canonical encoding. Committed records bind the rule digest, fact-snapshot digest, result, and relevant temporal data. An independently retained anchor makes later alterations detectable under the cryptographic assumptions.

Reconstruction also requires the materials behind those digests. The reviewer needs the rule text, facts, evaluator, and any recorded external responses. With complete inputs and deterministic evaluation, the reviewer can reproduce the result or identify a discrepancy.

A digest alone cannot reproduce its missing contents. [Programmable Institutions §6.2](https://research.momentum.inc/papers/programmable-institutions.html#retained-evidence) therefore distinguishes successful verification from missing data, unavailable keys, restricted disclosure, and invalid evidence. A retained commitment can still identify what the record claimed while reconstruction remains blocked.

That distinction matters when retention duties end or law permits deletion. GDPR erasure rights, for example, have exceptions for legal obligations and legal claims. The applicable duty determines what must remain available and to whom. Lawful deletion of a required fact snapshot changes the record's reconstructibility. The system should record that change explicitly. [GDPR Article 17](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng).

Replay answers a precise question: did these recorded inputs produce this result under this evaluator? A badly translated rule can replay perfectly. A committed human judgment or oracle answer can be reproduced as an input while its underlying truth remains disputed.

Replaying an old payment record must also remain separate from sending payment instructions. Historical reconstruction reads the recorded occurrence. Any new action requires its own current authority. Otherwise, an audit could repeat the act it was meant to inspect.

## Some replacements change the question

Raising the capital threshold changes a parameter within an established framework. Replacing principles-based securities regulation with a prescriptive regime can change the categories of assessment themselves.

Three kinds of change need different treatment:

1. **Value changes** preserve the evaluator and the question. A number, date, or list entry changes. Old and new results remain directly comparable.
2. **Schema changes** alter inputs or categories. A declared mapping translates every old status within its stated domain and records which propositions it loses.
3. **Replacements** introduce a framework in which some old propositions have no counterpart. Those propositions retain their meaning within the framework that produced them.

Calling a mapping “complete” requires evidence that it covers its domain. Calling it “lossless” requires evidence that it preserves the relevant propositions. An untranslated status should remain visibly untranslated. Assigning it a convenient default would erase the distinction the migration needs to explain.

[Lex §3.3](https://research.momentum.inc/papers/lex.html#pack-evolution) describes a narrower, typed form of rule change. Its `Rewrite` requires a target derivation for every source derivation, alongside preservation and timing conditions. A replacement with an untranslated source result fails that requirement. Partial transport with explicit blocked outcomes remains a separate construction obligation.

This boundary explains why ordinary software migration language can mislead. A new framework may ask a different question. Preserving the old answer and its context can be the correct outcome even when translation fails.

## Who may change the amendment rule?

The procedures for changing rules are themselves rules. They identify who may propose an amendment, which approvals it needs, and how it takes effect. Hart called these rules of change. Ross and Suber examined the problem of a procedure amending its own authority.

Constitutions make different choices about that problem. Germany's Basic Law protects the federal structure, the Länder's participation in legislation, and the principles of Articles 1 and 20. Article V of the United States Constitution protects each state's equal Senate suffrage without that state's consent. These are particular protected matters with particular legal foundations. [German Basic Law, Article 79](https://www.gesetze-im-internet.de/gg/art_79.html), [U.S. Constitution, Article V](https://www.archives.gov/federal-register/constitution/article-v.html).

New Zealand Parliament's 2023 account describes electoral provisions protected by three-quarters of all House members or a majority of valid referendum votes. It explains that section 268 itself is outside that protection. Ordinary-majority removal is theoretically possible, while circumvention of the reserved provisions is constitutionally improper. Under the orthodox account of UK parliamentary sovereignty, Parliament can change its predecessors' laws, while conventions constrain how that power is used. [New Zealand Parliamentary Practice, §14.2.6](https://www3.parliament.nz/en/visit-and-learn/how-parliament-works/parliamentary-practice-in-new-zealand-2023-by-chapter/chapter-14-the-basis-of-parliamentary-procedure/), [UK Parliament on sovereignty](https://www.parliament.uk/site-information/glossary/parliamentary-sovereignty/) and [conventions](https://www.parliament.uk/site-information/glossary/conventions/).

For a computational rule system, the design question is concrete: can an ordinary amendment create the authority needed to remove its own amendment conditions?

One construction fixes a minimum authorization requirement outside the policy that ordinary amendments can change. The validator accepts a replacement of protected clauses only when the already-required signers authorize that exact replacement. A proposal lowering the threshold must first satisfy the existing threshold.

The [Sovereign Jurisdiction Network's protected-floor construction](https://research.momentum.inc/papers/sovereign-jurisdiction-network.html#sec:governance) states this conditional result. It assumes an institutionally grounded signature requirement fixed outside mutable policy and unforgeable signatures. Ordinary amendments then cannot manufacture the missing authorization.

Key custody determines whether that protection remains useful. Compromise of enough required keys can authorize its dissolution. Loss of enough keys to make the threshold unreachable freezes protected amendments. A recovery process needs its own valid authority. Participants can also abandon the system and establish another. Internal amendment rules govern the old system's accepted changes, while its preserved record remains evidence under its original context.

## Keep unfinished work through the transition

A rule change reaches institutions with applications, payments, disputes, and renewals already underway. A transition provision must state how each affected class of work proceeds.

It can permit an application begun under the old rules to finish on those terms. A sanctions designation or emergency suspension can instead require a halt. The applicable instrument selects the treatment. An automatic assumption of grandfathering would bypass that decision.

A suspended workflow retains its exact request, evidence, unanswered questions, resource reservations, and outstanding duties. An authorized successor transition carries those objects into the new procedure. An old answer remains in the history while its current use receives a separate check. Replacing the workflow does not itself answer a pending question or discharge an obligation.

Running old and proposed rules side by side helps expose the consequences before activation. Each evaluation names its rule. Comparison can show agreement, disagreement, or a proposition that has no counterpart in the other framework. Regulators need all three outcomes. Counting only changed verdicts would miss cases that no longer fit the new categories.

The transition ends through its declared procedure. Institutions receive the required route to reassessment, and the old edition ceases to govern the specified current activity. The historical record remains subject to its retention and evidence duties.

## Prepare for a possible successor

A regulator can test a plausible next framework before deciding to adopt it. If a shift toward prescriptive securities rules is under consideration, preparation can identify candidate mappings and run comparative evaluations.

The useful output includes the proposed translation, declared losses, examples that resist translation, and the consequences for unfinished work. General algorithms for computing every loss or detecting every incomparable proposition remain open. The preparation strategy depends on doing those checks for a defined scope.

A rejected proposal can still leave useful tests and worked examples. A different successor will need its own mapping and authorization. Forecasting the next framework is a design strategy whose value must be judged against the cost of preparing for the wrong one.

The institution with \$3 million in capital needs an answer it can act on when the new threshold begins. Its counterparties also need the earlier decision and the evidence supporting it. Governed change preserves that history, states what changed, and assigns a lawful path to the work still outstanding.

## References

Hart, H. L. A. (1961). *The Concept of Law*. Oxford University Press.

Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.

Ross, A. (1969). “On Self-Reference and a Puzzle in Constitutional Law.” *Mind*, 78(309), 1–24.

Snodgrass, R. T., and Ahn, I. (1985). “A Taxonomy of Time in Databases.” *Proceedings of the ACM SIGMOD International Conference on Management of Data*, 236–246.

Suber, P. (1990). *The Paradox of Self-Amendment: A Study of Law, Logic, Omnipotence, and Change*. Peter Lang.
