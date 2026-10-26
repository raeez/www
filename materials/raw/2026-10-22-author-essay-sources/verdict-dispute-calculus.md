# When Sovereigns Disagree

**Raeez Lorgat, 2026**

---

Two jurisdictions evaluate the same transaction and return different verdicts: one compliant, the other non-compliant.

Each verdict follows a different sovereign's rules, with no third standard above both. Neither verdict is evidence against the other. Signed verdicts can establish that a single authority answered the same question on the same inputs in two different ways. Anyone holding both can prove that contradiction. A cross-jurisdictional network must preserve sovereign disagreement while making attributable self-contradiction costly.

## Genuine disagreement is the design

A jurisdiction decides what its rules mean within its territory. Pakistan's securities regulator and Singapore's securities regulator apply different functions to the same inputs. Those functions encode different policy choices, risk tolerances, and histories of financial crisis. Different verdicts on the same entity can therefore be correct under each regulator's rules.

In a distributed database, two nodes returning different answers to the same query indicate a fault to repair. Applying that standard to sovereigns would erase the policy differences their separate jurisdictions preserve.

The resulting constraint is that *you cannot build a system that eliminates disagreement between sovereigns without eliminating sovereignty*.

## Self-contradiction is provable

When the same authority evaluates the same question on the same inputs and produces two different verdicts, it contradicts itself. The mechanism below establishes that fault without deciding whether it arose from incompetence or fraud.

A signed verdict is a cryptographic commitment with an exact scope: the key of jurisdiction $J$ over the statement "entity $E$ has outcome $v$ in domain $d$", together with the *pinned inputs* of the evaluation -- the version of the rule archive the evaluation ran under and the digests of the evidence it consumed -- and an evaluation index naming which evaluation this is.

The issuer cannot choose the index, and the evaluation never reads it. The index is either fixed by the question instance or derived from the statement's subject, domain, and pinned inputs. In the first form, it is the operation identifier and corridor epoch under which the evaluation was requested, as in the companion papers. In the second, it is a digest of the subject, domain, and pinned inputs. Both forms name the evaluation without determining its outcome.

The outcome is not a bit: the value set carries Non-Compliant, Pending, and Compliant in that order, with not-applicable and exempt on a separate applicability axis (the companion paper *How Compliance Composes* fixes this value set). Contradiction is outcome inequality at the same index: two verdicts under the same key, for the same subject and domain, over identical pinned inputs, with different outcomes.

Compliance status legitimately changes when evidence arrives, a license expires, or a sanctions list updates. A temporal detector would flag verdicts that change too quickly and tune its window for each jurisdiction. It would have to balance false positives from racing evaluations against false negatives from contradictions separated by a deliberate delay. Pinning the inputs removes the need for that window. The Wednesday sanctions update between Monday's verdict and Friday's is itself an input. The pinned inputs differ, so no contradiction arises.

Everything that can explain a changed outcome must be inside the signed statements. With identical pinned inputs, different outcomes at the same index yield a certificate. Different indices do not evade accountability: because evaluation is deterministic and does not read the index, at least one verdict then fails replay. As described below, such a signed replay failure breaches the issuer's commitments and floors the corridor just as a certificate does.

The companion papers anchor the index externally in the protocol's operation identifier and corridor epoch. *The Sovereign Jurisdiction Network* accepts an equivocation certificate only for conflicting signed artifacts under one zone's key at that index. *Op: A Typed Bytecode for Compliance-Carrying Operations* carries verdict uniqueness there as a typed invariant. It refuses a second local signature at an occupied index and converts a same-signer, same-index conflict between imported artifacts into a blame witness naming the signer. All three identify the same fault: one signer, one index, two conflicting artifacts.

The two signed statements form an equivocation certificate. Any holder can check the signatures and outcome inequality without a third party or access to the jurisdiction's internal reasoning. The registry supplies the key's attribution to the jurisdiction.

The claim requires four assumptions. The signature scheme is existentially unforgeable under chosen-message attack, so a verifying signature identifies the key. A registry authentically binds each signing key to its jurisdiction and records revocation, so the key identifies the signer. Verdicts have a canonical encoding, so outcome inequality at the same index is machine-decidable. Evaluation is a deterministic function of the pinned inputs, with the index excluded, so inequality establishes contradiction rather than permitted variation.

A verdict speaks for its index indefinitely, but reliance today requires an evaluation recent enough that nothing material has changed. Corridor policy therefore fixes a maximum accepted verdict age, as it does for a presented passport head (*The Compliance Passport*). This freshness bound governs reliance and plays no part in the definition of contradiction.

## What signed verdicts demand

Before digital signatures, detecting institutional self-contradiction depended on competing testimony. A regulator could say "we never approved that" without a verifiable artifact to test the denial. A signed verdict binds the statement to its unrevoked jurisdictional key. Preserving that evidence requires signatures, retention, and independent detection.

**Every verdict is signed.** An unsigned verdict cannot be attributed to an issuer and therefore cannot establish contradiction or accountability.

**Every verdict is retained, beyond the issuer's power to edit.** Historical verdicts must survive because the issuer has an interest in concealing contradictions. An issuer-held log permits two attacks: rewriting the past or serving different, internally consistent histories to different parties. Hash chaining makes each entry commit to its predecessor under the issuer's signature. Editing the past then forks the chain, yielding two signed successors of one entry and an equivocation at the log level.

Bonded external watchers expose forks by signing the chain head and height they observe. Different histories then produce conflicting attested heads. *The Chain of Evidence* gives the hash chain, inclusion proofs, and watcher-based fork detection. *The Sovereign Jurisdiction Network* specifies watcher bonds and requires receipt-chain or watcher inclusion evidence in an equivocation certificate.

**Recipients and watchers detect contradictions automatically.** Manual comparison of thousands of verdicts is impractical, and the issuer has little incentive to find its own contradiction. Recipients check each new verdict against those they hold. Watchers' bonded head attestations expose different histories served to different parties, and watchers that attest conflicting heads forfeit their bonds. Corridor policy determines whether watchers also receive payment.

These mechanisms have established precedents. PeerReview makes a node's faults provable to third parties through signed append-only logs (Haeberlen, Kouznetsov and Druschel 2007). Fork consistency forces an untrusted log operator to maintain consistency or expose a detectable fork (Li, Krohn, Mazières and Shasha 2004). Certificate Transparency publicly monitors a trusted authority's issuance log (Laurie, Langley and Kasper 2013). Proof-of-stake accountable safety treats double-signing at the same index as a provable, punishable fault (Buterin and Griffith 2017; Buchman 2016). The beta reputation family (Jøsang and Ismail 2002) and its network forms (Kamvar, Schlosser and Garcia-Molina 2003) supply slow-accrual, sharp-loss reputation dynamics.

The first four systems treat deviation from a shared correctness standard as a fault. The two reputation systems aggregate subjective ratings without a shared standard or proof of fault. They supply precedent here only for the demotion dynamics below. Sovereigns preserve the right to differ from each other, so this construction holds each accountable for inconsistency in its own statements.

## The economics of trust demotion

A counterparty responds to proven equivocation by changing its own reliance on the jurisdiction's future assertions and the price of re-verifying them. The response cannot be punitive: an external system cannot fine or compel a sovereign.

Reliance has separate domain and corridor components. Foreign evaluations receive recognition per domain: trust in anti-money-laundering evaluations need not extend to data privacy (*Mutual Recognition*). Operational trust is a corridor level in a finite ordered set. Each level selects a policy table of transaction limits, settlement windows, and in-flight counts (*The Sovereign Jurisdiction Network*). Equivocation moves the corridor to a level with lower limits and longer windows. A reduced domain recognition grade removes face-value acceptance, requiring the receiving side to re-evaluate locally what it previously accepted.

Relying on an untrustworthy counterparty costs far more than proceeding slowly with a trustworthy one, so promotion and demotion follow different rules. Observed clean settlement permits promotion one level at a time, after the relevant threshold is met. Proven equivocation drops the corridor to its most restrictive level, or to suspension, regardless of its previous level.

A proportional demotion would cost a low-trust jurisdiction almost nothing. Its deterrent would be weakest for the parties most likely to offend, and each repetition would cost geometrically less. A common floor avoids this dependence on current standing. An established corridor falls further, reflecting the greater concern when equivocation follows a long clean record. Every offender reaches the same floor, and every regained level requires the same promotion threshold regardless of previous standing or repeated falls.

A corridor already at or near the floor loses little through the drop itself. The floor's limits instead cap counterparties' exposure and the gain from a contradictory verdict, whether the corridor is new or returning. Suspension permits nothing.

Recovery requires the same promotion thresholds as a new corridor, with no shortcut back. The rebuild horizon is the observed clean settlement those thresholds demand under each level's limits. It begins at the floor, and the limits ease with promotion. The cost of equivocation is this constrained recovery period rather than a nominal penalty.

A signature that fails to verify leaves trust unchanged. Bytes that do not verify under a jurisdiction's key are not its statement. Under the unforgeability assumption, anyone can produce such bytes. Penalizing the named key would let third parties demote a jurisdiction by broadcasting invalid signatures. Verification failure therefore means rejection without attribution.

A validly signed verdict whose disclosed bundle fails replay is attributable and floors the corridor as a certificate does. Examples include a mismatched evidence digest or a rule-archive version that fails to yield the signed outcome. The jurisdiction's own statement then fails its commitments. Key compromise requires registry revocation, which bounds what the key can sign from revocation onward. No scoring rule repairs a stolen key.

## Integrity disputes before interpretation disputes

Signed claims can raise disputes about integrity or interpretation, each requiring a different resolver.

Integrity checks whether an artifact is what it claims to be. A content-addressed evidence package either matches its digest or fails, and a match establishes unchanged content since commitment. A signature either verifies or fails, with verification attributing the statement to a key. A verdict either replays from its disclosed inputs under the stated rule version or fails. These machine checks establish provenance and preservation. None proves that the committed content was true.

Interpretation asks what authentic evidence means under the applicable legal tradition. Two authentic, unmodified documents can support contradictory legal conclusions under different rules of interpretation. A shipping document that constitutes delivery in one legal system may not do so in another. Human adjudicators who know those traditions must resolve this question.

Integrity checks come first, before a tribunal considers evidence that could fail its digest. Mechanical verification gives adjudicators a verified record and narrows their docket to contested cases, removing the need for cryptographic reconstruction.

## Contestation as a design requirement

A system producing verdicts must provide a way to contest them. The standing possibility of challenge supports confidence in uncontested verdicts without presuming that the system is infallible.

The challenge must reach a forum independent of the issuer, because adjudicating its own outputs supplies no external check on the system's correctness. The corridor instrument names that forum in advance, as a commercial contract fixes its arbitral forum before a dispute arises.

Standing belongs to the parties a verdict binds: the evaluated entity and any counterparty that relied on it. A challenge presents the signed verdict with its disclosed bundle of evidence digests, rule-archive version, and replay transcript. The forum verifies integrity before hearing argument. The issuing system supplies verdict logs, integrity verification, equivocation certificates, and corridor trust records, while judgment belongs to the forum.

The remedy preserves the append-only record. No verdict is deleted. A new signed verdict supersedes a wrong one, and its inputs include the ruling that displaced its predecessor. It occupies a new index under either form: the digest changes with the pinned inputs, and an occupied corridor index admits no second signature. If a challenge reveals two same-index verdicts, the certificate itself establishes the integrity fault. Demotion then follows the corridor's pre-agreed rules without depending on the forum's interpretive discretion.

## Deterrence

Signed, index-keyed verdicts and independently watched, append-only logs make same-index contradictions available as certificates. Any holder can verify a certificate against the key registry and canonical encoding. Certificates and validly signed replay failures floor the corridor's trust level, imposing the cost of recovery. Mechanical integrity checks precede interpretation by an independent forum.

Deterrence holds when the one-shot gain from a contradictory verdict is smaller than the cost of demotion. That cost includes friction from the limits at each level along the promotion path, heaviest at the floor and easing with promotion. It also includes local re-evaluation while recognition is withheld. These costs accumulate over the rebuild horizon and are discounted according to the jurisdiction's valuation of its future. Whether the inequality holds depends on stakes, detection lag, and discount rates. This note specifies a mechanism that makes the cost side large, but leaves open the payoff model needed to prove deterrence.

Consistency leaves two failures unresolved. A jurisdiction applying a bad rule uniformly never contradicts itself, and one consistently attesting fabricated facts can replay cleanly against those fabrications. This mechanism addresses neither case. It removes the ability to make inconsistent statements to different parties, or to the same party at different times, while retaining their reliance.

The network can therefore preserve sovereign policy differences while changing reliance on a jurisdiction that contradicts itself. Disagreement between sovereigns remains a policy fact to be priced. Signed artifacts make self-contradiction provable, and the recovery rules make it costly without imposing agreement on substantive policy.

## References

Buchman, E. (2016). *Tendermint: Byzantine Fault Tolerance in the Age of Blockchains.* MSc thesis, University of Guelph.

Buterin, V. and Griffith, V. (2017). "Casper the Friendly Finality Gadget." arXiv:1710.09437.

Haeberlen, A., Kouznetsov, P. and Druschel, P. (2007). "PeerReview: Practical Accountability for Distributed Systems." *ACM Symposium on Operating Systems Principles (SOSP 2007)*.

Jøsang, A. and Ismail, R. (2002). "The Beta Reputation System." *15th Bled Electronic Commerce Conference*.

Kamvar, S. D., Schlosser, M. T. and Garcia-Molina, H. (2003). "The EigenTrust Algorithm for Reputation Management in P2P Networks." *WWW 2003*.

Laurie, B., Langley, A. and Kasper, E. (2013). *Certificate Transparency.* RFC 6962.

Li, J., Krohn, M., Mazières, D. and Shasha, D. (2004). "Secure Untrusted Data Repository (SUNDR)." *OSDI 2004*.
