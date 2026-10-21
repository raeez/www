# Compounding Intelligence

**Author:** Raeez Lorgat

---

A compliance officer who has seen ten thousand cases makes better decisions than one who has seen a hundred. That improvement accumulates with experience, subject to diminishing marginal returns.

This paper describes infrastructure built around that observation. The observation corpus, the structured accumulation of institutional evidence described in the companion *Observation Corpus* paper, becomes more useful over time. Precedent grows, anomaly detection becomes better calibrated, and rule update proposals gain evidence. The value curve is sub-linear, not exponential. The thousandth observation of a familiar operation type adds less than the tenth, and the ten-thousandth adds less than the thousandth.

Sub-linear compounding describes institutional learning under diminishing marginal information. The problem is to retain that learning within the institution while preserving the authority of its rules.

## 1. The Shape of the Value Curve

Three mechanisms account for sub-linear returns.

**Diminishing marginal information.** The first hundred observations of a new operation type establish its baseline. They give typical pass rates by compliance domain, common failure modes, and expected evaluation duration. The next thousand refine that baseline with seasonal variation, edge cases, and the distribution of outcomes beyond the mean. The next ten thousand primarily confirm established patterns. Within a stable regime, information per observation declines. A regime shift, such as a statutory amendment or a change in supervisory practice, steepens the curve again. The observations that follow it are the most informative in the corpus. This is why the system keeps observing at full resolution and detects anomalies (Section 5).

**Jurisdiction diversity bounds.** A zone is one deployment of this institutional stack, running a single jurisdiction's rules or composing several. A zone with a hundred thousand observations from one jurisdiction knows that jurisdiction better than a zone with ten thousand observations from ten jurisdictions. It has less evidence about the range of compliance patterns: the domain-verdict associations that Section 4 turns into precedent. One zone has seen one rulebook applied, while the other has seen ten. The comparison concerns breadth, not depth in the home jurisdiction.

A new jurisdiction introduces patterns the corpus has not seen. Additional observations from a known jurisdiction mostly confirm existing patterns. The value of breadth grows concavely with jurisdictional diversity because jurisdictions overlap in the patterns they contribute, especially within a legal tradition. The tenth jurisdiction of a tradition adds fewer new patterns than the first. Section 6 accounts for this overlap through legal-tradition similarity weights.

**Irreducible noise.** Compliance outcomes contain stochastic variation that additional data cannot eliminate. Misfiled documents, missed deadlines, and a regulator's discretion on a particular case are idiosyncratic events rather than patterns to learn. This noise sets an asymptote, not a reversal. More observations sharpen the estimate of a pattern's rate, while the next case retains irreducible variance. Once stable patterns are established, the predictive improvement from a marginal observation tends to zero.

This characterization is a heuristic, not a theorem. Intelligence quality should exhibit diminishing returns in observation volume and benefit from jurisdictional diversity along a concave curve. A logarithmic volume term and square-root diversity term are plausible modeling choices. This paper does not derive them from a statistical model.

## 2. Why Sub-Linear Compounding Is Valuable

In most deployed systems, the alternative to sub-linear compounding is no institutional learning. Operations are evaluated against static rules. People update those rules manually from their intuitions and the cases they remember. Without systematic retrieval, anomaly detection, or evidence-based feedback, that experience remains outside the institutional record.

Even modest institutional memory supports three uses.

**Precedent retrieval.** When a familiar operation begins, the system can retrieve relevant precedent: "this operation type, in this jurisdiction, for this entity type, has historically passed these compliance domains with 98% reliability and failed this domain 15% of the time." The compliance tensor still runs and the rules still apply. The precedent directs the compliance officer's attention to domains likely to need it.

**Anomaly detection.** A compliance domain's pass rate may drop from 95% to 40% over a two-week window. The corpus detects that shift automatically, allowing investigation of a regulatory change, rule misconfiguration, new class of non-compliant operations, or upstream degradation. Without the corpus, detection waits for someone to notice a pattern in individual outcomes.

**Evidence-based rule updates.** A proposed rule change carries its supporting observation count, jurisdiction count, time period, and pattern. Governance reviewers can assess that evidence independently of the proposer's authority.

A few thousand well-structured observations already support meaningful precedent retrieval because a zone certifies precedent from its own record (Section 4). A few months of history already enable anomaly detection. The benefits begin before the corpus is large and continue as it grows.

## 3. The Feedback Loop

Institutional learning follows a feedback loop. Operations produce observations that accumulate in the corpus. The intelligence layer uses them to retrieve precedent, detect anomalies, and construct rule update proposals. Approved proposals change the compliance rules, which affect future evaluations and the observations those evaluations produce.

Each iteration makes a small change, such as one threshold in one compliance domain for one jurisdiction. Evidence from observed outcomes supports each change. Common law follows a comparable incremental process. A decision becomes precedent that later courts apply. When it produces bad outcomes, a court may distinguish or overrule it. The accumulated evidence makes the learning durable.

The architectural boundary lies between rule inputs and evaluation logic. Intelligence proposes changes to the inputs. The compliance tensor remains a deterministic function from rules, attestations, and jurisdiction configuration to verdicts, and learning never alters that function.

This separation makes a regression attributable to a specific rule input and reversible without changing evaluation logic. Subsequent observations expose worse outcomes, and a follow-up proposal can refine or revert the rule. A revert follows the same amendment path as the update it undoes. The interval therefore includes detection latency (Section 5), followed by a proposal, governance review, and adoption by the regulator whose rule it is (Section 7). Entities evaluated during that interval bear the cost. The evaluation logic remains intact, but the consequences of a bad input persist until correction. Section 7 returns to those costs.

## 4. The Precedent Construction Pipeline

A precedent is a reusable compliance pattern: stable domain-verdict associations for a specific operation type, jurisdiction, and entity type. Certification requires a minimum observation count and stability across sub-windows of the observation period. Both conditions are local, so a zone certifies precedents from its own record.

Zone count determines the confidence grade of a certified precedent. It is not a certification condition. The grade rises above the single-zone level only when federation (Section 6) supplies digests showing another zone's pattern. Outside federation, every certified precedent retains the single-zone grade.

Discovery runs whenever a zone recomputes its per-jurisdiction operational profiles (Section 5). For each operation-jurisdiction-entity triple with enough observations, it computes domain outcome summaries. Domains with very high or very low pass rates are candidates. The pipeline partitions the observation period into sub-windows and checks consistency. A pattern confined to one month fails precedent status.

Once the count and stability checks pass, the pipeline assigns a confidence grade. A pattern supported only by the local record receives the single-zone grade. Each federated partner whose digests show the same stable pattern for the same triple raises it, because evidence diversity matters as much as volume. The grade is stored with the precedent and reported on every retrieval.

The categories that define a triple can themselves change: an operation family may be re-cut or an entity-type schema revised. Apparent instability at that boundary can come from repartitioning the data. More observations cannot distinguish that artifact from a change in the world. Reclassifications are therefore recorded as events and included in the comparison windows. Stability is assessed only within a consistent partition.

When a new operation begins, applicable precedents predict which domains will need attention and estimate evaluation duration. They supply prior expectations, while the compliance tensor evaluates the operation under the rules.

The legal analogue is persuasive authority. A coordinate court's ruling, or a foreign court's ruling in the comparative use of Section 6, informs a case under the deciding court's own law. A superior court's ruling binds lower courts as law. Nothing this pipeline produces has that force. A precedent supplies evidence about outcomes. It becomes law only through a supported rule update adopted under the governance and regulatory process of Sections 3 and 7.

## 5. Anomaly Detection

Precedent identifies stable patterns. Anomaly detection checks when those patterns change. A zone maintains an operational profile for each jurisdiction: a probability distribution over operation types, compliance outcomes, evaluation durations, and failure modes. It updates that profile incrementally with exponentially weighted moving averages. Roberts (1959) introduced this control-chart statistic within statistical process control (Shewhart 1931).

Four classes of anomaly merit attention.

A **domain failure spike** occurs when a historically reliable domain begins failing at an unusual rate. It indicates regulatory change, rule misconfiguration, or a new class of non-compliant operations. A **duration anomaly** consists of operations taking significantly longer than historical norms. It indicates external service degradation, new compliance requirements, or a governance bottleneck. A **volume anomaly** is a deviation from seasonal observation rates and indicates market events, regulatory changes, or system issues. A **cross-domain correlation anomaly** occurs when two historically independent domains begin failing together, indicating a common upstream cause.

Detection requires sustained deviation rather than single-event outliers. Lucas and Saccucci (1990) analyze the trade between detection delay and false-alarm run length for this statistic. The conservative threshold protects operators' attention: a compliance officer receiving a hundred false alarms a month stops reading the alerts.

## 6. Federated Aggregation

Precedents and anomalies become more informative when institutions can compare evidence. That comparison must respect the sovereignty of their data. A zone owns its observations, and raw observations never leave it.

Zones share aggregated, anonymized digests with corridor partners through federated aggregation. Sharing defaults to nobody and requires an explicit opt-in. A minimum-population gate prevents small zones from sharing aggregates that reveal too much. Per-entity budgets prevent one entity's observations from dominating a shared aggregate. Raw evidence remains within the producing zone.

A receiving zone obtains typed summaries: per-jurisdiction operational profiles, compliance domain outcome summaries, and detected innovations with an evidence grade. The grade determines which responses the evidence supports.

At the weakest grade, an anomaly is a deviation from the fleet: the comparable zones whose digests the grading zone receives. A rule's flag-to-confirmed-violation ratio is compared with the fleet median using the fleet's dispersion. An absolute threshold would require advance knowledge of the right ratio for that domain. This relative deviation warrants investigation, but not a claim to a regulator. Because participation is voluntary, the fleet is self-selected and its median is a biased null model.

The fleet-relative grade has two further limits. Below a handful of comparable peers, there is no dispersion against which to judge a result, so the grade is unavailable. A deviation shared by the whole fleet also produces no fleet-relative signal. A fleet-wide error is invisible at this grade.

A higher grade requires a deviation that survives a change the zone did not choose, such as a statutory amendment elsewhere or a corridor opening. This is the usual quasi-experimental warrant (Campbell and Stanley 1963; Shadish, Cook, and Campbell 2002). The highest grade requires the zone to run a deliberate variation and measure its outcome. These grades depend on changes and outcomes, so they do not inherit the fleet-wide blind spot.

The response follows the evidence grade. The weakest permits internal tracking only. The middle permits proposing an amendment with the evidence attached. Only the strongest supports asserting that the amendment will have the predicted effect. A receiving zone sees the summary, not the evidence that produced it, and cannot detect an inflated grade for itself. It incorporates summaries into its operational profiles using a confidence discount, a legal tradition similarity weight, and a recency weight.

A replay supplies a forecast below this evidence ladder. Because evaluation is deterministic in rules, recorded attestations, and configuration (Section 3), a zone can replay a proposed rule over recorded operations before enactment. It can count the mechanical effects: changed entity compliance states, violations created and resolved, newly blocked or unblocked actions, and changes in corridor partners' traffic.

Three limits govern the forecast. Behavior is held fixed, so replay cannot observe how parties would restructure their conduct under another rule. It forecasts mechanical effects, never behavioral outcomes. Facts from external, time-varying sources are replayed as recorded rather than re-queried, so the difference reflects only what the rule change can affect. Finally, replay is faithful only if it computes the same deterministic function as live evaluation. A replay can scope a proposal's impact. It ranks below fleet deviation and never warrants asserting that an amendment will have its predicted effect.

Comparative law illustrates the authority boundary. A Singapore court can learn from a London court's handling of a similar case while applying its own law under its own authority. The London ruling is informative rather than binding. Federated aggregation follows that pattern through sovereign local memory and voluntary sharing of typed summaries, with no pooling of raw evidence or binding foreign intelligence.

## 7. Auditing the Layer That Does the Scoring

The intelligence layer never decides a case (Sections 3 and 4), but its outputs affect governed entities through two routes. Adopted rule amendments bind subsequent evaluations, and directed attention determines what gets investigated. These effects make the layer a classifier, with errors that affect some of those entities. The mechanisms above do not audit its outputs. The architecture requires an error discipline for its other components and owes the same discipline here.

The first obligation is an audit of outputs. It must separate three rates by entity class: flags, wrong flags among those raised, and real violations missed. Equal flag rates can conceal large differences in false flags and missed violations. Those latter rates describe errors that governed entities experience.

Counting confirmed violations in two ways gives flag rate × (1 − false-flag rate) = base rate × (1 − missed-violation rate). The base rate is the share of a class's operations that are in fact violations. When base rates differ, a system that catches any violation cannot equalize all three rates. This is the decomposition and trade-off studied by Hardt, Price, and Srebro (2016), Chouldechova (2017), and Kleinberg, Mullainathan, and Raghavan (2017). The classes here are institutional: entity size, age, harbor-set composition, and the home jurisdiction's legal tradition. Small and newly incorporated entities have the thinnest evidence trails, so a thin-evidence heuristic will over-flag them.

The first two rates are measurable from the local record. Flags are counted directly, and an investigation that fails to confirm a violation exposes a wrong flag. The missed-violation rate needs evidence from outside that record because a wrongly cleared operation looks like any other clearance.

Retrospective labels come from three sources. A supervisor may later flag a particular cleared operation. A counterparty may later enter a sanctions list, labeling operations that cleared against it. A corridor peer may re-evaluate an operation or entity at its border and refuse what the local zone cleared. The first two sources exist in any screening system. Peer refusal is the additional label the network supplies.

A peer refusal bears on the local decision only when the corridor's recognition parameters make the rules comparable. These parameters specify which domains the receiver re-evaluates and how domain names and recognized grades map between rulebooks. The companion *Sovereign Jurisdiction Network* paper describes this parameterization. Refusal under a stricter or unmapped rule indicates jurisdictional difference, not local error. A candidate missed violation receives strong evidentiary status only when independent label sources corroborate it. The audit therefore applies Section 6's grading discipline to its own evidence.

The second obligation concerns the process. Amending a rule and amending the system that scores rules require different authority. A rule change is a legal act for the regulator whose rule it is. A detection-model change is not a legal act and does not follow that route. Yet it changes every subsequent rule recommendation, so engineering approval alone is insufficient. It needs a separate reviewer and record, with disclosure to downstream zones. Recipients of summaries cannot otherwise see that the system producing them has changed.

The third obligation concerns the ranking of outputs. Supervisory attention is finite, so rank affects which items receive investigation. An operator who understands the ranking can bury an item by making others appear urgent, without falsifying any individual signal.

Two properties limit this attack without solving it. The complete stream must remain available for independent queries so low rank never removes an item from the record. The ranking must also be tested against an adversary who knows it and tries to push a chosen item below the point of review. Accuracy on ordinary traffic does not test that maneuver.

All three obligations remain undeveloped here. Until they are met, the layer's error rates on governed entities are unmeasured, and its ranking is untested against the stated attack.

## 8. Why Structured Memory Comes First

These evidence and authority requirements explain why a statistical model is a poor foundation for institutional learning. Structured memory must come first.

**Small populations.** A zone may have a few thousand entities and a jurisdiction within it a few hundred. An operation type may yield a few dozen observations per month. Every observation matters in these small, structured, domain-specific populations. These are not internet-scale datasets. Aggregate statistics are meaningful without curve-fitting.

**Sovereignty constraints.** Training a shared model requires pooling data or gradients. Both leak information. Shared gradients can be inverted to recover source records (Zhu, Liu, and Han 2019). A trained model can expose training data through inversion or membership queries (Fredrikson, Jha, and Ristenpart 2015; Shokri, Stronati, Song, and Shmatikov 2017).

The observation corpus pools neither data nor gradients and instead shares typed statistical summaries. It therefore has no shared model to invert. Aggregate releases can still permit reconstruction (Dinur and Nissim 2003). Section 6's population floor and per-entity budgets resist that risk for each digest, but do not bound what a partner accumulates across digests. The construction has no privacy budget of the kind differential privacy uses to bound total disclosure across releases (Dwork, McSherry, Nissim, and Smith 2006; Dwork and Roth 2014). Quantified privacy remains an open obligation.

**Regulatory provenance.** A statistical model trained on regulatory data must establish the source of the data and authority for its use. The corpus contains only observations of operations the zone itself evaluated under its own authority. It records the operation, entity, rules, and authority, keeping provenance internal and inspectable.

**Inspectability.** When the corpus reports "this domain fails 30% of the time," it identifies an observation count, source zones, and time window. An operator can inspect that evidence. When an opaque classifier says "this entity is non-compliant," its basis is a parameter matrix a person cannot interpret. A regulator's question, "why did you flag this entity?", requires an answer beyond "the classifier said so". Decisions must be defensible, so inspectability is mandatory.

The institutional memory on which intelligence depends should be structured, inspectable, and sovereign. Statistical capabilities should build on the corpus and preserve it as their foundation.

## 9. The Case for Institutional Memory

Most institutional infrastructure evaluates operations in isolation against static rules, without reference to earlier outcomes. The compliance officer supplies the missing memory through experience accumulated over years. When she retires, that experience leaves with her.

The observation corpus retains relevant precedent, anomaly alerts, and evidence for proposed rule changes. These materials support the officer's judgment and remain available after her retirement. Institutional memory becomes durable and retrievable.

Its value compounds sub-linearly. The first year of observations contributes more than the second, and the second more than the third, while each still adds information. The tenth year can add precedent spanning regulatory cycles, market crises, and jurisdictional evolution. Years that cross regime shifts supply observations that no additional volume within a stable regime can provide.

## 10. Conclusion

Structured institutional memory improves decisions by retaining the evidence from earlier operations. Under the heuristic of Section 1, the returns diminish within a stable regime, gain from jurisdictional diversity, and rise again after regime shifts. Anomaly detection identifies those changes.

The feedback loop converts observed patterns into evidence-based proposals. Approved proposals refine the rules, which improve operations and produce evidence for further revision. Federated aggregation extends the comparison across zones through the authority model of comparative law, without pooling sovereign data.

The layer that selects and scores this evidence must itself be accountable. Section 7 leaves three obligations: audit outputs, audit detection-process changes, and retain the full stream while testing its ranking against an informed adversary. Those duties follow from the same mechanism that makes memory useful: evidence directs attention and can change the rules that govern later cases.

## References

Campbell, D. T. and Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Rand McNally.

Chouldechova, A. (2017). "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments." *Big Data*, 5(2), 153–163.

Dinur, I. and Nissim, K. (2003). "Revealing Information While Preserving Privacy." In *Proceedings of the ACM Symposium on Principles of Database Systems (PODS)*, 202–210.

Dwork, C., McSherry, F., Nissim, K., and Smith, A. (2006). "Calibrating Noise to Sensitivity in Private Data Analysis." In *Theory of Cryptography (TCC)*, Lecture Notes in Computer Science 3876, 265–284.

Dwork, C. and Roth, A. (2014). *The Algorithmic Foundations of Differential Privacy*. Foundations and Trends in Theoretical Computer Science, 9(3–4), 211–407.

Fredrikson, M., Jha, S., and Ristenpart, T. (2015). "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures." In *Proceedings of the ACM SIGSAC Conference on Computer and Communications Security (CCS)*, 1322–1333.

Hardt, M., Price, E., and Srebro, N. (2016). "Equality of Opportunity in Supervised Learning." In *Advances in Neural Information Processing Systems 29 (NeurIPS 2016)*, 3315–3323.

Kleinberg, J., Mullainathan, S., and Raghavan, M. (2017). "Inherent Trade-Offs in the Fair Determination of Risk Scores." In *8th Innovations in Theoretical Computer Science Conference (ITCS 2017)*, LIPIcs 67, 43:1–43:23.

Lorgat, R. *The Observation Corpus*. Companion paper in this series.

Lorgat, R. *The Sovereign Jurisdiction Network*. Companion paper in this series.

Lucas, J. M. and Saccucci, M. S. (1990). "Exponentially Weighted Moving Average Control Schemes: Properties and Enhancements." *Technometrics*, 32(1), 1–12.

Roberts, S. W. (1959). "Control Chart Tests Based on Geometric Moving Averages." *Technometrics*, 1(3), 239–250.

Shadish, W. R., Cook, T. D., and Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Houghton Mifflin.

Shewhart, W. A. (1931). *Economic Control of Quality of Manufactured Product*. D. Van Nostrand.

Shokri, R., Stronati, M., Song, C., and Shmatikov, V. (2017). "Membership Inference Attacks Against Machine Learning Models." In *IEEE Symposium on Security and Privacy (S&P)*, 3–18.

Zhu, L., Liu, Z., and Han, S. (2019). "Deep Leakage from Gradients." In *Advances in Neural Information Processing Systems 32 (NeurIPS 2019)*.
