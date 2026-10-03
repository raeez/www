# Claims and Continuing Obligations

## Abstract

A payment provider confirms 100 units against a 125-unit obligation, then stops responding. The unpaid 25 must remain recorded, but issuing another command can overpay if the first command later completes.

This article explains the mathematical records needed to calculate a claim and authorize its execution. These records attribute received value and preserve unfinished duties through interruption and program changes. Finite payoff semantics, continuing obligation journals, joint command reservations, and distributed agreement supply different parts of that construction. Their guarantees depend on declared evidence, authority, storage, scheduling, and provider contracts. A confirmed ledger decision does not establish beneficiary receipt.

## 1 The unpaid 25 {#sec:payment}

A payer owes 125 units of one asset. A provider has been instructed to make the payment. Authenticated records establish that 100 units have arrived, but its response leaves the remaining execution uncertain. The account of the obligation is simple: 100 paid, 25 outstanding. The next permitted action is less simple.

If the provider can still send the remaining 25, a fresh command for 25 creates two ways to pay the same remainder. A local timeout says only that a response did not arrive in time. The residual-child construction discussed below requires a provider-enforced closure or transfer of that execution right before assigning it to a child command. A broader replacement can instead rely on an enforced joint bound covering old and new effects, as Section [6](#sec:reservations){style="overflow-wrap:anywhere;hyphens:none"} explains.

The worked trace in *Op: Compliance-Carrying Operations*, Sections 5.9 and 6, retains both the original target and each command's assigned quantity \[[1](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}\]. After a valid split, the parent command can be recorded as matched for its assigned 100 while the original payment still has 25 outstanding. The child command carries that remainder, its reservation, and its own authority checks. An ordinary retry keeps the original command identity. It does not create a child.

For one asset and exact quantity unit, the accounting rule is $$Q=(P-R)+C+U.$$ Here $Q$ is the original target, $P$ supported payments, and $R$ linked returns. Quantity $C$ is the amount removed by an authorized cancellation or amendment, and $U$ is the outstanding target. In this example, $125=100+0+25$. A supported return of 20 would reduce net payment to 80 and reopen the outstanding amount to 45 under the governing rule. Splitting commands changes none of these totals.

Four identities keep this account intelligible. The duty identifies what is owed. The command identifies one requested action. An external occurrence identifies what the provider actually did. An assertion identifies a report about that occurrence.

Two reports of one payment cannot discharge the duty twice. Closing a command does not cancel the debt.

These distinctions preserve the obligation record after a lost response. Safe retransmission separately requires the identical canonical request and provider idempotency key. The provider must enforce duplicate protection throughout the complete possible delivery interval \[[1](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}, Section 5.13\].

Op describes the operation as a typed program: each instruction declares the kinds of values, permissions, and resources it consumes or produces. Its finite core checks required screening on every write path, tracks resources that cannot be duplicated, and retains ownership when execution suspends. A suspended program resumes only through its declared evidence interface. These structural checks exclude specified omissions. Their stronger meaning depends on the screening rule, authority, and provider contract being adequate. A well-formed program cannot make a false external premise true.

## 2 What a claim program calculates {#sec:calculation}

A claim records an economic right or obligation and the conditions determining its outcome. *The Claim as Primitive* studies a precise computational form: a finite payoff program, an evaluation schedule, and payment terms \[[2](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\]. A payoff is the amount the program determines from its admitted inputs. A position binds a quantity of that claim to the relevant parties and financial context.

The language combines constants, observations, earlier resolved values, arithmetic, comparisons, and conditional choices. A cap limits an amount. A floor supplies a minimum.

Financial types record dimensions and context, so a currency amount cannot silently become another currency merely because its numerical value matches. A currency conversion needs the declared rate, evidence, and conversion context. The program determines the amount under those declarations. It does not establish their institutional truth.

The exact expressiveness theorem in Section 4 identifies both the power and the limit of the finite language. It represents precisely the stated finite piecewise-polynomial functions: polynomial formulas selected on regions described by polynomial comparisons. Conversely, those functions can be constructed from the language. This is a characterization of a defined function class, not a claim that every imaginable financial arrangement has been encoded. Bounded historical windows and recurring schedules have their own admission conditions.

Evaluation also needs a valid dependency order. Ordinary historical references point strictly backward in the evaluation schedule. A producer is a computation supplying an input to another computation. The extension in Section 7 permits producers within the same event when a complete, checked graph of those dependencies establishes an order with no cycle. An omitted dependency can invalidate that reasoning.

The resulting amount is separate from its market price. Price concerns what participants exchange for a position under a valuation or trading model. Resolution concerns what the admitted program computes. Payment concerns performance against the resulting entitlement. A price move pays no coupon, and a resolved coupon need not yet have a payment receipt. Keeping these objects separate permits a claim to retain its payment history while its price changes.

## 3 A coupon counter can reset while money remains due {#sec:coupon}

Consider the memory-coupon construction in *The Claim as Primitive*, Sections 5 and 6.5 \[[2](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\]. A coupon is 10 units. At each scheduled observation, the trigger either fails or succeeds. Failure adds one to the count of consecutive missed coupons. Success resolves the current coupon plus the accumulated misses, then resets the count.

Starting with a zero count, the trigger sequence $0,0,1,1$ gives:

  Observation              First   Second   Third   Fourth
  ---------------------- ------- -------- ------- --------
  Trigger                      0        0       1        1
  Resolved coupon              0        0      30       10
  Miss count afterward         1        2       0        0

The third observation accounts for three coupons. Resetting the count prevents those missed coupons from entering the fourth payoff again. Proposition 5.7, *No missed coupon enters two resolved payoffs*, proves that property for the pre-issued schedule. It concerns calculation: it does not say the 30 has been paid.

Now admit one compatible payment occurrence of 35 units. Allocate 30 to the first payable entitlement and 5 to the second. The outstanding amount is 5 although the miss counter is zero. The entitlement journal retains the original 30 and 10, the payment occurrence, and both allocations. Neither another evaluation nor a process restart may reconstruct outstanding obligations from the zero counter alone.

The durable construction commits calculation state, entitlement records, payments, and command outcomes through one write authority. A retry of a committed request returns its retained result. A stale calculation checkpoint cannot overwrite a payment that arrived afterward. These properties rely on the specified atomic storage operations, authenticated state, complete request bindings, and restart rules. They do not follow merely from saving a file.

Missing observations can suspend this coupon while an unrelated ready claim resolves. Section 6.2 also identifies cases where a smaller set of observations already fixes the numerical answer. That mathematical fact does not waive the original evaluator's mandatory financial evidence. Replacing the evaluation procedure would require a separate correspondence covering evidence, work limits, suspension, and observable request history.

## 4 Changing the representation without losing the duty {#sec:carriage}

A payment can remain unfinished when its records move to a successor program. *Admissible Obligation Transitions* separates the immutable economic duty identity from the implementation representing it \[[3](#ref-aot){style="overflow-wrap:anywhere;hyphens:none"}\]. Its family interface keeps the claim's own rights, conditions, and permitted changes. The shared engine checks requests, authority, evidence, and the current state before admitting a transition.

The engine's preservation theorem starts from a valid state and assumes both the family and engine laws, including serialized execution. Newly committed refused or awaiting decisions extend the recorded history without mutating the protected private state. An exact retry returns its existing receipt. Accepted requests must preserve the family's invariant, the property its transitions are required to maintain. This permits common admission machinery without reducing unlike instruments to one balance and one settlement flag.

The carriage construction in Section 7 preserves duties through authorized splits and regroupings. A 100-unit duty has 60 discharged and 40 payable. It can acquire two positions in one successor representation without becoming two new economic claims. The correspondence must cover the predecessor completely, keep successor portions disjoint, and preserve the required rights. One serialized commit fences new execution under the old binding and activates the successor. A change of beneficiary or priority is an economic amendment requiring its own authority and laws.

Payment history matters even when quantities are small. Suppose allocation $a$ pays four units, numbered 0 through 3. A return against $a$ reopens units 0 and 1. Allocation $b$ pays those two units again.

A further one-unit return against $a$ must concern its remaining discharge, beginning with unit 2. It cannot reopen the replacement payment's units. The current balance alone cannot answer which earlier payment is being returned.

Duty portions and physical payment portions have separate histories. Reopening the duty does not release consumed physical-credit support. Allocation $b$ requires other unconsumed support with admitted evidence.

Section 7.8 represents consecutive portions as intervals while retaining their order and separate return histories. Its refinement theorem shows that expanding those intervals reproduces the corresponding individual-portion execution. This avoids enumerating every monetary quantum, the smallest permitted quantity. Cost still depends on fragmentation, history, and the size of quantity representations. One authenticated serialized store and a common write mediator remain premises.

Unresolved calculations need more than a partition of today's balance. Section 7.9 supplies a construction for authentic programs with the same instructions and matching contexts, but different positive rational position partitions. Under one exclusive write authority and declared resource limits, both computations receive the same admitted requests and compatible observation refinements. When both resolve an instance, their numerical values agree.

Only the source creates duties in the economic ledger. The successor computes a correspondence. This preserves future calculation for that class, not arbitrary program equivalence. Currency conversion, resolved-rate references, and external conversion witnesses are excluded. Later payment aliases require additional positive-outcome, quantum, and current-history checks.

Discarding records has a similarly demanding test. Section 6.2 calls two states future-equivalent only if every admitted continuation produces the same protected observations. That includes returns, corrections, refusals, and archive restoration when those operations are admitted. Keeping today's balance unchanged is insufficient.

A certificate can establish the correspondence for a complete finite supplied model, including its declared input vocabulary. Sampling a few future requests cannot establish equivalence for all requests. Adding a new operation requires rechecking the interface.

## 5 Completion must name its goal {#sec:service}

Preserving a duty does not ensure anyone completes it. A system can retain every record and still spend forever retrying or migrating. Sections 7.4--7.6 of *Admissible Obligation Transitions* make useful service a separate requirement \[[3](#ref-aot){style="overflow-wrap:anywhere;hyphens:none"}\].

A service episode names original work and a fixed completion goal. For a decision goal, an authenticated refusal may be a valid completion. For discharge, the required performance and evidence must occur. Renaming a duty or moving it to another program cannot silently replace that goal with an easier one.

The original-cohort theorem fixes a finite collection of episodes even while new work continues to arrive. Each original episode has a nonnegative integer rank: a measure of unfinished work that is zero exactly when its declared goal is recorded. Their aggregate rank starts at $R$, never increases, and decreases through productive service.

Execution must continue until completion. Whenever the aggregate rank is positive, a decrease must occur within the next $K$ transitions. Then all original goals are recorded within $KR$ transitions. An unfinished deadlock violates the continuation premise. New arrivals do not enter this original cohort or reset its count.

The argument is direct. A positive integer total can strictly decrease at most $R$ times before reaching zero. The service condition permits at most $K$ transitions per required decrease. Its force comes from the premises: a scheduling policy that merely visits each duty, without performing productive work, does not satisfy them.

The concrete bound accounts for implementation steps too. While work is unfinished, every state must have a successor. Each actual transition during unfinished work must lower the rank or preserve it while strictly lowering a bounded counter for intervening work. Migration, retry, and recovery steps all count. A bounded counter that resets without a rank decrease supplies no bound.

For a fixed finite set of reusable slots, a monitor can check repeated completion. Each episode remains attached to its slot until its goal is recorded. A slot must visibly clear before reuse, and the monitor records a fresh pulse when a round finishes. Returning a pointer to its starting position is insufficient.

The associated finite, fully observed control game identifies states from which safe recurrence can be forced. Deadlocks lose. Completed idle states need explicit transitions back to themselves. Extending that result requires a faithful model of the actual executor and observations. It establishes neither unlimited monitor capacity nor provider performance.

Provider readiness has its own dependencies. Section 12 of *The Claim as Primitive* composes jointly valid completion contracts for persistent prerequisite facts along a finite acyclic graph \[[2](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\]. For a finite graph that may contain cycles, ordinary completion contracts wait for every predecessor. Under these declared conjunctive guarantees, external seeds ensure complete readiness if and only if the seeded facts meet every directed cycle.

Without a seed, a cycle can wait forever for itself. Treating a cyclic group as one component still requires a genuine joint completion contract for that group. Combining provider readiness with the goal-service bound requires compatible authority, evidence, resources, and one declared clock.

## 6 Replacement needs cash capacity and performance capacity {#sec:reservations}

The unpaid-25 case has two resource questions. Can the payer fund every still-possible debit? Can the old and new commands together overperform the obligation? More cash can answer the first question while leaving the second unchanged.

Section 5.2 of *Admissible Obligation Transitions* gives an exact joint test \[[3](#ref-aot){style="overflow-wrap:anywhere;hyphens:none"}\]. Fix an accounting cut: the recorded point specifying which effects the balances already include. The tested scope must contain every old and candidate command sharing the affected cash or performance capacity, including in-flight effects. Let $b$ be cash after commitments outside that scope, and $u$ the duty's remaining authorized performance capacity.

A negative cash difference remains a funding deficit. Admission requires nonnegative baselines. Pending observed performance can already occupy part of the performance capacity before legal discharge is established.

The contract describes every possible continuation prefix, meaning every intermediate point as well as each endpoint. For each prefix, let $x$ be additional cash headroom consumed and $y$ additional performance headroom consumed. With one coordinate of each kind, the admission condition is $$\sup x\le b,\qquad \sup y\le u.$$ The suprema are the least upper bounds over the joint contract. Each quantity retains its own unit. Multiple accounts and duties receive separate coordinate tests.

For an exact description of admitted continuations, these inequalities are necessary and sufficient for preserving nonnegative headroom. A larger sound set supplies a sufficient test but may refuse a feasible replacement. Intermediate prefixes matter because a later refund cannot fund an earlier debit. An already-booked debit must not be subtracted again, while an occurred but unreflected effect remains in the contract.

Adding separate command ceilings gives a conservative sufficient test without statistical independence. Tighter bounds require an enforced joint constraint, such as a shared provider ceiling. Hoped-for coordination is insufficient.

The registry must replace the scope's existing reservations with its joint reservation in one atomic operation. That operation must count the quantity once, retain outside commitments, and bind the replacement to the same dependencies. Provider-enforced closure can reduce remaining exposure. Silence cannot.

## 7 Agreement can include an unfinished payment {#sec:agreement}

When several participants maintain the ledger, they must agree on the event decision and the resulting obligations. *Event-Collect BFT* constructs that common record while allowing payments to remain pending \[[4](#ref-event){style="overflow-wrap:anywhere;hyphens:none"}\]. BFT means Byzantine fault tolerance: agreement despite a bounded number of participants that may send false or inconsistent messages.

In its four-validator example, at most one validator is faulty and three signatures form a quorum, the required agreement threshold. An instruction calls for a local transfer of seven units if an event resolves yes. A block records one agreed batch of ledger changes. The preceding confirmed block fixes the encrypted instruction order. Validators can then collect event evidence while obtaining the decryption contributions for that fixed order.

Finite, signed evidence collections support a complete accepted-or-deferred decision for each candidate event. A missing response does not become proof that no event occurred. A closed collection supplies the recorded basis for deferral. A certificate is checkable evidence for a specified protocol statement. Agreement uses the chosen protocol's complete commit proof and safe leader-change rules. An intermediate preparation certificate is insufficient.

The child block commits the accepted event, clearing decision, instruction receipt, and resulting state together. Clearing computes what each party owes under the configured rule. A failed local transfer group leaves no partial group write. For external payments, the committed state instead retains observed performance, allocations, outstanding duties, reservations, and continuing commands. Provider facts enter independently of whether a later instruction succeeds.

Not every trade is matched on the ledger's own book. A licensed venue that matches its own trades can register them for clearing with its trade identifiers, and the same rules then apply. A product fee is a due like any other. It is charged in the trade's settlement currency, on the closed amount, to the payees a governed schedule names, and it stays separate from principal and customer collateral.

This is atomicity of the ledger update: the complete state changes together. External providers retain their own execution and finality rules. Dispatch follows confirmation and authority at actual use. Replay recomputes the recorded decision without sending another payment. Historical first completion also remains distinct from current performance after a return.

Agreement relies on the fault bound, deterministic validation, cryptographic contracts, and the underlying consensus protocol. Ledger progress additionally requires eventual communication recovery, retained instruction bodies and decryption service, finite evidence closure, and terminating execution. External completion requires funded resources, current authority, provider responses, fair dispatch and observation delivery, and a recovery process that makes finite progress. A ledger can therefore continue confirming truthful pending states while a provider remains unavailable.

## 8 What remains to establish {#sec:limits}

Together, these constructions specify an account in which calculated obligations survive payment failure, commands retain their remaining exposure, and program changes preserve original duties. They give exact conditional results, rather than a general certificate that an institution will perform.

Implementation refinement must connect actual messages, storage transactions, recovery behavior, and resource ownership to the mathematical transitions. Full-database rollback and competing independent stores need controls beyond a single-store transaction. Legal adequacy, source authority, physical occurrences, and provider finality require evidence from their named owners.

*Event-Collect BFT* includes no proof-assistant artifact. Its finite checks are not parametric mechanized proofs. The other cited constructions likewise retain their stated executable and mechanization boundaries. None of these four papers establishes production latency from a scheduling parameter or a synthetic trace.

## 9 Technical reading map {#sec:reading}

Payment and authorized execution.

:   *Op: Compliance-Carrying Operations*, Sections 3--4, 5.1--5.13, 6, and 7.5--7.6. Read *Payment-intent conservation* in Section 5.9 for the 125-unit example. *Finality separation* in Section 5.7 and the executable-scope discussion delimit the external claim. Section 5.13 states the separate provider retry-safety premises.

Payoff calculation and persistent entitlements.

:   *The Claim as Primitive*, Sections 2--4, Proposition 5.7 and Corollary 5.8, Sections 6--7, and Sections 11--13. The exact-expressiveness theorem fixes the language's domain. *Durable retry and conservation* in Section 6.4 states the storage result. Section 12 separately composes jointly valid provider-completion contracts, using dependency paths and named clocks.

Continuing duties and useful service.

:   *Admissible Obligation Transitions*, Section 5.2 (*Exact joint replacement bound*), Section 6.2 on complete future equivalence, and Sections 7.2--7.9. Theorem 7.7 gives original-cohort progress, Propositions 7.8--7.9 the finite monitor and game, and Theorem 7.10 the concrete step bound. Theorems 7.14 and 7.17 cover interval execution and structural continuation. Section 11 records the remaining authority, refinement, and provider obligations.

Agreement and external completion.

:   *Event-Collect BFT*, Sections 3--7 and 9, especially *Atomic event transition*, *Ledger progress*, and *Useful external progress*. Section 11 constructs certified compatible allocation within a closed batch and fixed history. Section 12 separates disclosure history and current performance. Section 14.1 states proof and implementation status. The five-round bound in Section 8 concerns its specified same-height double-certification class, not every consensus protocol.

## References

::: {#ref-op}
:::

**\[1\]** Raeez Lorgat. *Op: Compliance-Carrying Operations*. September 2026.

::: {#ref-claim}
:::

**\[2\]** Raeez Lorgat. *The Claim as Primitive*. September 2026.

::: {#ref-aot}
:::

**\[3\]** Raeez Lorgat. *Admissible Obligation Transitions*. September 2026.

::: {#ref-event}
:::

**\[4\]** Raeez Lorgat. *Event-Collect BFT*. September 2026.
