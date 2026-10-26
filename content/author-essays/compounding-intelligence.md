# Compounding Intelligence

An experienced compliance officer remembers where an application is likely to fail, which evidence resolves a recurring question, and when a familiar pattern has changed. An institution should retain enough of that experience for the next officer to use it.

That requires structured records of what happened, under which rules, with what evidence, and with what result. A searchable history can direct attention to difficult cases and give proposed rule changes an inspectable basis. Its value lies in the decisions it helps people make over time.

## Experience needs a record

The [Observation Corpus](https://research.momentum.inc/papers/observation-corpus.html) describes a design for retaining evidence from institutional operations. Company formations, payments, governance decisions, licensing events, and disputes each contribute observations. The records support retrieval, comparison, and investigation.

Suppose a particular application repeatedly fails one domain check. The institution can retrieve comparable cases and see which documents were missing, which rule applied, and how the issue was resolved. A new officer can prepare for that issue before the next application reaches it. The governing rule still determines the case.

The record must distinguish an attempted operation from one that committed. In the proposed design, a transaction records both the state change and its observation, or commits neither. That guarantee covers writes passing through the specified control point. Administrative changes and other bypasses need their own controls and reconciliation.

The permanent event history and the learning relay serve different purposes. The history preserves the record. The relay delivers observations for processing and can discard consumed entries under its retention policy. Losing a temporary learning queue and losing institutional evidence are different failures.

Historical context also needs more than an event date. A later correction can change the assessment of an earlier act while leaving the original decision record intact. [Lex, §4.9](https://research.momentum.inc/papers/lex.html#revocation-and-temporal-tagging) distinguishes the evidence and rules used then, a legal assessment using a selected evidence view, and permission for a current act. Learning from cases requires preserving those distinctions. Otherwise a later fact can make an earlier decision appear unreasonable on evidence its maker never possessed.

## More observations have different kinds of value

Within a stable regime, repeated observations should eventually add less information. Early cases reveal common failure modes. Later cases refine their frequency and expose less common outcomes. This is the diminishing-return hypothesis behind “compounding intelligence.” The suggested logarithmic volume and square-root diversity curves are illustrative models, with no fitted parameters or established empirical growth law.

A hundred thousand observations from one jurisdiction may describe its routine operations well. Ten thousand observations across ten jurisdictions may reveal a wider range of patterns while providing less precision about each jurisdiction. Those numbers illustrate the distinction between depth and breadth. They establish no minimum sample size or measured advantage.

Jurisdictions also share institutions, legal traditions, and operating practices. Ten jurisdictions need not supply ten independent bodies of evidence. A useful comparison must account for that overlap.

A statutory amendment or a change in supervisory practice can make recent observations particularly informative. More cases under the old regime cannot substitute for observing the new one. This is one reason to retain dates, rule histories, and changes in how cases are classified.

Misfiled documents, missed deadlines, and case-specific judgment also limit prediction. More evidence can improve an estimate while leaving uncertainty about the next case. The practical question is whether the record helps an officer find relevant evidence or identify a change soon enough to act.

## A recurring pattern directs attention

A reusable pattern needs a defined population: an operation type, a jurisdiction, and an entity class. It also needs enough observations and stability across parts of the observation period. A pattern confined to one month may reflect a temporary event rather than a reliable expectation.

The local record can establish whether those count and stability checks pass. Evidence from another institution can broaden a pattern's support, provided the cases and rules are comparable. The number of participating institutions belongs in the evidence description. It should not substitute for examining their independence or the quality of their records.

Classification changes can create a false appearance of change. If an institution divides one operation family into two, the resulting pass rates may move even when conduct remains stable. The record must retain that reclassification, and comparisons must use a consistent partition.

This use of “precedent” means an observed pattern offered to a decision-maker. It has the status of evidence about earlier outcomes. Binding precedent and adopted law derive their force from the relevant legal system. A pattern produced by this pipeline acquires regulatory force only through the authorized process for changing the rule.

Anomaly detection asks when an established pattern changes. An exponentially weighted moving average gives recent observations more weight while retaining part of the earlier history. A sustained failure-rate increase warrants investigation. A sudden increase in evaluation time can indicate a failing service, a new requirement, or a delay in approvals. Two domains failing together may have acquired a common cause.

For example, a pass rate falling from 95% to 40% over two weeks would merit attention in a sufficiently observed, comparable population. It would not identify the cause. The threshold also trades detection speed against false alarms. An alert system that repeatedly consumes attention on harmless changes can reduce the attention available for consequential ones.

## Learning can propose a rule change

Operations produce evidence. That evidence supports a proposal. The institution with amendment authority decides whether to adopt it, and later observations help assess its consequences.

The proposed architecture keeps encoded rule inputs separate from evaluation logic. For fixed rules, recorded attestations, and configuration, the evaluator produces a deterministic result. Learning can propose an input change without silently changing the function that evaluates a case. This makes the altered rule identifiable and the earlier evaluation reproducible.

A bad rule change still affects people. Reversing it requires detection, a proposal, review, and adoption through the applicable amendment process. Entities evaluated during that interval bear its consequences. Reproducibility identifies the rule that produced the recorded evaluation result. Correction still requires an authorized act.

A replay can examine a proposal before adoption. It applies the proposed rule to recorded cases and counts mechanical differences: checks passed or failed, actions blocked or allowed, and changes to recorded eligibility. It must use the same evaluation function and the recorded external facts. Re-querying a changing source would confound a changed rule with changed evidence.

Replay holds behavior fixed. It cannot show how parties would restructure their conduct in response to the new rule. A mechanical forecast and evidence of a policy's causal effect answer different questions.

## Learn across borders with the evidence attached

An institution can compare its experience with another while retaining control of its records and decisions. The design keeps raw observations local and permits voluntary sharing of summaries under a release policy. A summary identifies its population, period, rule context, and supporting evidence.

A deviation from comparable peers can justify investigation. A change outside the institution's control may support a quasi-experimental comparison. A deliberate variation can provide stronger evidence when its design and measurement support causal inference.

Peer comparison has a particular weakness. Participating institutions select themselves into the comparison group, so its median can be biased. A small group may provide too little information to estimate dispersion. An error shared by every participant produces no deviation from the group. Agreement can conceal a common failure.

The recipient also sees a summary rather than all the underlying evidence. It may therefore be unable to detect an inflated evidence grade. Confidence, recency, and legal-tradition weights can express a recipient's treatment of a summary. Their calibration remains a substantive judgment.

The technical proposal uses weaker evidence for internal investigation and stronger evidence for amendment proposals and claims about expected effects. Any such claim must retain the study's population, assumptions, and uncertainty. Foreign experience can inform the receiving institution while the power to amend its rules remains local.

## Audit what receives attention

A system can influence governed entities before any rule changes. Its rankings help determine which cases receive investigation. An operator who understands the ranking may bury a chosen item by making other items appear more urgent, while every individual signal remains accurate.

Ordinary accuracy tests miss this attack. The complete stream must remain available for independent queries, including items that receive a low rank. The ranking also needs tests against an informed adversary trying to move a chosen item below the point of review.

The audit must distinguish the fraction of operations flagged, the fraction of flags that were wrong, and the fraction of actual violations missed. Equal flag rates can coexist with different error rates for small firms, new entities, or institutions operating under different legal traditions.

For a fixed population with reliable outcome labels, these quantities satisfy:

$$
\text{flag rate}\,(1-\text{false-flag rate})
=\text{violation rate}\,(1-\text{missed-violation rate}).
$$

The false-flag rate here measures wrong flags among flags raised. The missed-violation rate measures missed cases among actual violations. Different underlying violation rates constrain which error rates a system can equalize while detecting violations. Choosing a fairness criterion requires stating which errors matter and how they are measured.

The labels are often harder to obtain than the formula. A flag count is observable. An investigation that fails to confirm a violation may remain unresolved rather than establish a false flag. A later sanctions listing may justify review of an earlier clearance, but the applicable rule and effective time determine its significance.

A peer institution's refusal can supply evidence about a case the local institution cleared. It indicates a possible local error only when the rules, evidence, relevant times, and recognition terms make the decisions comparable. A stricter foreign rule may explain the difference. Independent corroboration can strengthen the label, and unresolved cases should retain their unresolved status.

Changes to the scorer need scrutiny of their own. The authority responsible for a rule adopts its amendments. A change to detection or ranking alters the evidence presented to that authority and the cases likely to receive attention. It needs a separate reviewer, an accountable review record, and disclosure to institutions relying on its summaries. Engineering approval alone does not answer who accepts the consequences of that change.

The [technical note](https://research.momentum.inc/papers/compounding-intelligence.html#auditing-the-layer-that-does-the-scoring) retains these audit obligations. Output errors, changes to the scoring process, and manipulation of ranking each require evidence. The design does not yet supply their measured performance.

## Preserve the record that learning depends on

Structured memory offers an inspectable basis for analysis. A reported failure rate should identify its cases, observation count, rule context, and time window. Statistical models can build on that record while retaining the ability to explain the evidence behind a recommendation.

Keeping raw records local also preserves a useful institutional boundary. It avoids the particular exposure of a shared model trained on pooled records or gradients. Shared aggregates still disclose information, and repeated releases can permit reconstruction.

The [Observation Corpus's release design](https://research.momentum.inc/papers/observation-corpus.html#sovereignty-and-sharing) uses population thresholds, cohort controls, contribution caps, and noise. It has no enforced cumulative disclosure ceiling across releases. Its mechanism calibrates noise to the sensitivity of the exact rate, then applies that noise to a bucketed value with different sensitivity. A claimed privacy parameter needs analysis of the statistic actually released.

A successor officer should inherit the cases and the means to question how the system selected them. That includes the cases ranked too low for earlier review, the rule context that governed them, and the evidence supporting later corrections.
