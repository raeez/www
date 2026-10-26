# When Sovereigns Disagree

Two jurisdictions evaluate the same transaction. One permits it and the other refuses it. Each may have applied its own rules correctly.

Cross-border cooperation has to accommodate that difference. A receiving authority can recognize foreign evidence while retaining its own law and decision. It also needs a way to respond when the same issuer makes conflicting statements about the same evaluation.

Signed records make that distinction concrete. They identify what an authority said, the question it answered, and the inputs it used. A pair of contradictory statements can then establish an attributable fault while ordinary policy disagreement remains intact.

## Fix the question before comparing answers

Pakistan's and Singapore's securities regulators apply different rules. Their conclusions can differ because their mandates, policy choices, and legal requirements differ. A network that treats every difference as a fault would need a common authority to choose the answer.

Self-contradiction presents a narrower question. Did one authority issue two different outcomes for the same question under the same complete inputs?

A signed verdict must identify the issuer, subject, domain, outcome, governing rules, evidence, and evaluation context. The context includes any authority records, key-status information, evaluation time, and ordering that can affect the answer. Collision-resistant hashes bind the exact encoded inputs. Retained copies allow another party to check them.

The verdict also needs an evaluation identifier. In a bilateral operation, the protocol fixes it with the operation key. Another possible construction derives it from the subject, domain, and pinned inputs. The issuer must have no freedom to change that identifier merely to avoid comparison. The evaluator's answer must depend on the substantive inputs rather than the identifier itself.

A historical verdict can remain authentic while exceeding the receiving institution's maximum accepted age or falling outside its current-use validity interval. Those freshness checks govern present reliance. They leave the comparison of the original statements unchanged.

The result need not be binary. An applicable evaluation can be NonCompliant, Pending, or Compliant. NotApplicable and Exempt concern applicability on a separate axis. Combining several authorities' records requires the fuller construction in [How Compliance Composes](https://research.momentum.inc/papers/how-compliance-composes.html#ca:mixed-axis), which retains the applicable grades and their accompanying determinations.

Consider a compliant verdict on Monday, a sanctions update on Wednesday, and a refusal on Friday. The changed sanctions input explains the changed answer. Comparing complete pinned inputs avoids an arbitrary rule about how quickly verdicts may change.

If two signed statements instead bind the same issuer, question, evaluation identifier, and inputs but give incompatible outcomes, the pair is an equivocation certificate. A verifier checks both signatures and the conflict. Registry evidence supplies the key's attribution to the issuer.

[Op: Compliance-Carrying Operations §3.8](https://research.momentum.inc/papers/op.html#sec:bsc) gives this result for its bilateral session. Two contradictory valid verdicts from one role at the same operation and evaluation produce a witness naming that role. The result concerns the authenticated pair. A local signing rule can seek to prevent such pairs, but imported evidence still needs an independent check.

The construction assumes unforgeable signatures, authentic key attribution and status records, canonical encoding, and deterministic evaluation of the complete pinned inputs. If identical inputs appear under different identifiers, replay can still expose an incompatible signed outcome. That check requires all the inputs and the issuer's authenticated commitments to them.

A missing file or corrupted delivery can obstruct replay without establishing issuer misconduct. The distinction is essential: a receiver must not be able to frame an issuer by supplying the wrong supporting bytes.

## Keep the statements available

A contradiction can remain hidden if each recipient sees only one statement. The records therefore need retention outside the issuer's sole control, together with a way for recipients to compare authenticated histories.

A hash chain makes each entry commit to its predecessor. Independent observers can retain signed statements of the chain's head and height. Two valid issuer-signed observations at the same corridor, epoch, and height form a fork witness when their digests differ. Different heights ordinarily show a growing record.

These observers, called watchers, supply evidence of what they received and checked. Their signatures need defined subjects and observation rules. Counting keys alone can overstate independence because one controller can hold several keys.

The [Sovereign Jurisdiction Network's watcher construction](https://research.momentum.inc/papers/sovereign-jurisdiction-network.html#sec:watchers) therefore distinguishes signing principals from control groups. Its guarantee depends on authenticated registration, the signing checks, and a bound on dishonest principals or covered control groups. Three signatures under one signing controller cannot establish the same diversity as three independently controlled principals.

Recipients compare new verdicts with those they already hold. Watchers compare histories under the declared observation policy. Detection still depends on someone obtaining the relevant records. A retained chain commits to its entries, while evidence of completeness requires the corresponding coverage checks.

These methods build on established work. PeerReview uses signed logs to make faults demonstrable to third parties. SUNDR studies detectable forks in untrusted storage. Certificate Transparency monitors certificate issuance. Accountable consensus protocols identify conflicting signatures at a shared index. Each supplies a method for making a specific deviation attributable.

A sovereign setting needs that accountability while preserving each participant's authority over its own substantive rules. The evidence identifies the issuer's inconsistency. Its consequences follow the applicable instrument and authorized decision.

## Make future reliance depend on the evidence

An institution receiving foreign verdicts controls its own reliance on them. It can require more local checking, reduce permitted exposure, or suspend new activity under its adopted rules. That response acts through the receiving institution's authority.

Reliance has separate dimensions. Recognition can differ by regulatory domain: acceptance of anti-money-laundering evidence need not extend to data privacy. Operational limits govern transaction sizes, settlement windows, and concurrent activity. A reduction in recognition can require fresh local evaluation even where some foreign evidence remains reusable.

A useful policy proposal is to let clean performance earn greater operational latitude gradually, while proven equivocation triggers a return to a restrictive floor. Each level would specify its limits and the evidence required for promotion. The corridor instrument would identify who may change treatment and how that decision takes effect.

The asymmetry has a reason. A proportional reduction costs a low-trust participant little. Repeated proportional reductions cost progressively less. A common floor instead gives every offending participant the same restrictive starting point for recovery. An established corridor loses more latitude because it had earned more.

A corridor already at the floor loses little through demotion itself. Its limits must therefore control the exposure available there. Suspension can stop new admitted activity. Existing obligations still need their recorded path to completion, authorized suspension, or remedy.

Recovery would require the same evidence thresholds as a new corridor, with no automatic restoration of former standing. The economic cost consists of slower activity, tighter limits, and repeated local checking throughout that recovery period. The policy must specify what counts as clean performance and how to measure it.

This floor and recovery schedule is a mechanism proposal. The current [Sovereign Jurisdiction Network](https://research.momentum.inc/papers/sovereign-jurisdiction-network.html#sec:governance) supplies the authority conditions for changing recognition. A destination may tighten treatment prospectively under its local rule. Loosening requires the specified ratification, notice, and current-evidence checks. A reputation score cannot replace those acts.

Two failures need different treatment. An invalid signature gives no authenticated statement by the named issuer. Rejecting it while leaving that issuer's standing unchanged prevents third parties from causing demotion with arbitrary bytes.

A validly signed commitment that demonstrably fails against its complete authenticated inputs is attributable. An adopted floor policy can assign that failure the same consequence as an equivocation certificate. Missing inputs instead leave the dependent check unresolved.

Key compromise requires its own status and recovery procedure. Historical evidence identifies the key and recorded context. Current reliance checks the applicable revocation and compromise information. Adjusting a score cannot restore control of a stolen signing key.

Watchers can also post bonds under a separate instrument. A fork witness may satisfy an evidentiary condition for liability. Drawing the bond still requires the governing liability decision, custodian mandate, and funded balance. Actual payment requires evidence that the custodian performed the instruction. The [bond construction](https://research.momentum.inc/papers/sovereign-jurisdiction-network.html#sec:governance) keeps those stages separate.

## Give contested decisions an independent forum

Integrity checks establish whether an artifact matches its commitment, whether a signature verifies, and whether a result reproduces from complete inputs. They give a tribunal a record whose origin and preservation can be examined.

Interpretation asks what that record means. A shipping document can constitute delivery under one contract or legal system and fail to establish it under another. Authentic bytes do not decide that question.

The corridor instrument should identify the forum and governing procedure before a dispute arises. An evaluated entity or relying counterparty may have standing to submit a challenge. Submission standing and reliance alone do not establish arbitration consent or authority to bind another party. Each claim needs its own effective jurisdictional basis.

[Recourse](https://research.momentum.inc/papers/recourse.html#sec:tiers) separates those matters. Its record procedure can answer a bounded question against a complete snapshot. Missing evidence produces an unresolved result. A legal question reaches an authorized adjudicator under the applicable procedure.

Routine integrity checks precede those routes. A contested assertion that the record itself is compromised requires independent review. Otherwise, the challenged mechanism would decide whether its own evidence could be trusted. The Recourse procedure sends such integrity disputes to a tribunal and preserves the parties' escalation rights.

A machine extract, an adopted contractual determination, and an arbitral award also have different effects. The extract reports evidence. A contractual determination depends on the parties' effective adoption. An award comes from the tribunal's own proceeding and authority. [Recourse §6](https://research.momentum.inc/papers/recourse.html#sec:determination) sets out those distinctions.

Correction preserves the earlier record. The competent issuer makes a new signed evaluation with the ruling among its pinned inputs. The new context receives a new evaluation identity. Earlier statements remain available for audit and challenge.

An award itself cannot rewrite a sovereign recognition decision. Any resulting record change enters through the competent authority's own act under its governing instrument. A proven contradiction can support a reliance change, while the adopted policy determines who may make that change and when.

## What makes the cost credible

A restrictive floor deters equivocation only when the expected gain is smaller than the expected cost. That comparison needs transaction stakes, detection probability and delay, the recovery schedule, and the participant's valuation of future activity.

The cost includes friction at every recovery level and local re-evaluation while recognition remains restricted. A participant expecting little future activity may assign those costs little weight. A large one-time gain may exceed them. Establishing deterrence therefore requires a payoff model and evidence for its parameters.

Consistency also leaves two substantive failures unresolved. An authority can apply a bad rule consistently. It can consistently attest fabricated facts, then replay cleanly against those fabrications. Legal review and evidence about the world remain necessary in both cases.

Sovereigns can cooperate while applying different laws. The useful commitment is narrower and checkable: each issuer binds its statements to an identifiable question and complete inputs. Recipients retain the evidence, contest its meaning through the proper forum, and change their own reliance through authorized acts.

## References

Buchman, E. (2016). *Tendermint: Byzantine Fault Tolerance in the Age of Blockchains*. MSc thesis, University of Guelph.

Buterin, V., and Griffith, V. (2017). “Casper the Friendly Finality Gadget.” arXiv:1710.09437.

Haeberlen, A., Kouznetsov, P., and Druschel, P. (2007). “PeerReview: Practical Accountability for Distributed Systems.” *ACM Symposium on Operating Systems Principles*.

Jøsang, A., and Ismail, R. (2002). “The Beta Reputation System.” *15th Bled Electronic Commerce Conference*.

Kamvar, S. D., Schlosser, M. T., and Garcia-Molina, H. (2003). “The EigenTrust Algorithm for Reputation Management in P2P Networks.” *WWW 2003*.

Laurie, B., Langley, A., and Kasper, E. (2013). *Certificate Transparency*. RFC 6962.

Li, J., Krohn, M., Mazières, D., and Shasha, D. (2004). “Secure Untrusted Data Repository (SUNDR).” *OSDI 2004*.
