# When Institutional Programs Work Together

## Abstract

A funded purchase can still fail because its institutions select incompatible routes, spend the same reservation, or require unavailable information. Institutional composition requires one executable strategy that meets every condition and preserves the requested outcome. This article explains exact finite linking through funded delivery, shared capacity, information purchases, and continuing duties. Compatible local records yield a complete candidate only under the specified joining conditions. Execution then requires current authority, protected reservations, adequate source interpretations, and the provider and progress premises used in the model. Precise failure certificates identify what a proposed design lacks.

## 1 A purchase that must end in delivery {#sec:purchase}

A buyer has 120 units and needs delivery of an asset priced at 100 by the first supplier. If that supplier fails, a reserved standby supplier can deliver for 100 plus a charge of 20. The buyer must receive the asset and pay its acquisition charges. A refund by itself does not meet that goal.

These are the fictional contract terms in *Institutional Linking and Realization*, Section 11 \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}\]. Under the ordinary route, the buyer pays the first supplier immediately. If delivery fails, that payment remains unavailable throughout the required period. Replacement delivery then needs another 120, so the failure branch requires initial funding of 220. The primary success branch requires 100.

The conditional route reserves 100 in escrow for release to the first supplier upon delivery. Certified final failure returns it before the standby supplier needs payment. Starting with 120, the buyer retains 20 during reservation and regains the other 100 in time to pay the standby. Thus the conditional route needs 120 across both modeled branches.

  Required initial funding     Primary delivers   Certified primary failure
  -------------------------- ------------------ ---------------------------
  Ordinary payment                          100                         220
  Conditional escrow                        100                         120

The calculation depends on the order of actual events. A refund claim against the first supplier remains a right even when the buyer obtains a replacement asset. It contributes funding only when an eligible receipt arrives before the next debit. A pending delivery result also leaves the escrow return condition unresolved.

The standby guarantee, final-failure evidence, timely escrow return, and compatible funding pool are explicit premises. Fees, delayed returns, or standby failure require a changed calculation. The proposition proves the least funding for this finite contract profile. It does not establish a provider's offer or performance of the service.

Composition requires the supplier, escrow provider, and standby supplier to support the same acquisition under compatible conditions. One institution's valid action can leave another institution unable to perform. An institutional program records the actions permitted for this shared request and their consequences.

## 2 One request, one strategy, one completion condition {#sec:contract}

A claim records a right or obligation and the conditions that determine its outcome. An execution goal specifies which outcome must actually occur. The goal might require an admitted decision, delivery, discharged debt, or beneficiary receipt. Each condition defines a different problem. Changing a delivery goal into a refund goal changes the request.

An execution contract fixes the participating institutions, current authority, programs, dependencies, resources, observations, goal, and possible external outcomes. Authority means the named institution's permission at the relevant time and stage. A signature supplies attributable evidence whose effect depends on that permission.

Each component must describe its accepted requests, resource commitments, possible outcomes, and continuing duties. It must also explain what its outputs mean. Transmitting an application differs from registering it authoritatively, just as accepting a payment instruction differs from completing payment. The claim, operation, and transition papers preserve these distinctions at their respective interfaces \[[5](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}, [3](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}, [6](#ref-transitions){style="overflow-wrap:anywhere;hyphens:none"}\].

A strategy is a complete rule for choosing permitted actions as observations arrive. The same strategy must satisfy funding, authority, privacy, and completion requirements. Separate proofs that select different strategies do not establish a common solution.

Future provider outcomes remain outside the designer's control. The designer selects a supplier or a conditional payment route, then must cover every outcome that the chosen contract admits. Selecting a favorable future result within the optimization would exclude risks the strategy must handle. *Institutional Linking and Realization*, Sections 2--3, fixes this order of choices \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}\].

## 3 Actions must use available information {#sec:observations}

Suppose two possible worlds look identical to an institution. Success requires the action *left* in one world and *right* in the other. Each world has a successful action, but the institution cannot select correctly from its available information.

The finite construction assigns one decision variable to each distinct local observation. Every world with that observation uses the same variable. Theorem "Exact information-cell compilation" proves that satisfying these constraints is equivalent to a locally executable policy in the stated finite model \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 3\]. A satisfying assignment defines the action for each observation. Conversely, a permitted local policy assigns those variables and satisfies every world's requirement. An analyst's access to the full model gives the executing institution no extra observation.

An authorized observation that distinguishes the worlds can make the example feasible. So can an authorized and funded common action that succeeds in both. The institution must acquire the evidence or capability needed for its selected change.

Privacy imposes another restriction on observable behavior. An observation contract names the observer, its existing knowledge, the outputs it receives, and the private distinctions it must retain. It includes decision reasons, timing, refusals, and fees when those channels convey information. *The Sovereign Jurisdiction Network*, Section 5.5, combines local knowledge, source permissions, success, and exact privacy in one finite selector test \[[4](#ref-recognition){style="overflow-wrap:anywhere;hyphens:none"}\].

Individual privacy checks can fail under composition. Let a protected bit be $X$, and let $R$ be an independent uniform bit. Each output $X\mathbin{\oplus}R$ and $R$ is individually uniform, where $\oplus$ means addition modulo two. Together, the two outputs reveal $X$. This is the counterexample in *Institutional Linking and Realization*, Section 17.3 \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}\].

The composition condition compares each next output after every shared public history, using the actual conditional randomness law. Induction then compares complete output histories. Deleting a local record does not remove knowledge already disclosed to its recipient. These privacy conditions must hold together with the funding, authority, and success conditions.

## 4 Joining the complete choice {#sec:joining}

A finite relation is a table of permitted combinations. Separate tables can constrain route and authority, route with capital and supplier, and the observation plan. The linker seeks one assignment that belongs to every applicable table.

A certificate records that assignment and binds it to the exact request, domains, source meanings, and component choices. A separate checker can compare it directly with every original table. Authentication identifies a table's issuer and bytes. The issuer's authority and an adequate interpretation establish what its entries mean.

Pairwise agreement can leave the full request impossible. Take three binary choices $x,y,z$ and require $$x\ne y,\qquad y\ne z,\qquad z\ne x.$$ Every individual relation has entries, and every shared value has support in its neighboring relation. Three binary values cannot all differ. Consequently the full relation is empty \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 4\].

A join tree permits an exact local reduction. It arranges the constraint tables so that all tables containing any given variable form a connected subtree. Starting at the leaves, remove parent rows without matching child rows. The connectedness condition ensures that choices agree across branches.

Every full solution survives reduction because its child choices supply matching rows. Conversely, retained matches extend a surviving root row to a full assignment through the whole tree.

Theorem "Complete finite linking on a join tree" proves this criterion and witness construction \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 4.1\]. It applies the classical acyclic database join construction. *How Compliance Composes*, Section 3.4, proves extension when neighboring tables have equal projections on their shared variables \[[2](#ref-compliance){style="overflow-wrap:anywhere;hyphens:none"}\]. That theorem requires the same connectedness condition and the complete conjunction of constraints. General finite instances can use larger groups of interacting variables or exhaustive enumeration. The computational work depends on the size of those groups.

Eliminating internal choices can retain the exact feasible relation at a boundary. A replacement with the same boundary relation preserves the corresponding external feasibility tests \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Sections 5--6\]. The observation contract still governs disclosure of that relation. Learning which routes remain feasible can itself reveal private information.

## 5 Reservations define the choices that can remain local {#sec:reservations}

A joined assignment must preserve shared resources even when participants retain local choices. Two institutions share capacity of 100 integral units. Either institution can use 100 when considered alone. Giving both unrestricted local permission would allow a combined use of 200. The complete condition is $x+y\le100$.

The resource owner can reserve 60 for the first institution and 40 for the second. Every combination within $0\le x\le60$ and $0\le y\le40$ then fits the protected capacity. The owning authority must prevent duplicate issuance of either reservation. *Op: Compliance-Carrying Operations*, Section 5.11, establishes its declared exposure invariant through a common durable reservation ledger \[[3](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}\].

An independent-choice cell is a collection of local menus whose every combination satisfies the complete joint relation. The menus contain complete continuation policies, including their possible outcomes. Their product must remain admissible under the fixed request and history \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 8\]. Selecting a menu does not itself acquire its resources.

A cell is maximal when no local menu can grow while preserving that condition. In a finite relation, every admissible tuple extends to a maximal cell. Start with its singleton menus and enlarge them while their product remains admissible. The process stops because the relation is finite. Its maximal cells cover the admissible relation.

Maximal cells can differ, and some retain little useful choice. Maximality specifies how far menus can extend within a fixed model. Choosing among maximal designs requires the decision maker's objective.

With capacity fixed at 100, preserving every original allocation requires 101 independent-choice cells. Adding nine actual eligible units reduces the minimum to eleven \[[3](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.3\].

To see the lower bound, consider $(0,100),(10,90),\ldots,(100,0)$. Two such pairs in one cell permit a crossed choice exceeding 109. For the matching upper bound, divide $0,\ldots,100$ into eleven consecutive blocks of at most ten values. A block $[a,b]$ supplies menus $x\le b$ and $y\le100-a$. Their combined use is at most 109, and the blocks cover every original feasible pair.

This count concerns menus after compatible selection. Negotiation traffic, legal permission, and provider performance have their own conditions.

Information can also change the reservation requirement. Two mutually exclusive conditional duties of 100 require separate uninformed allowances totaling 200. A common owner can reserve 100 and issue only the applicable conditional right. The least-allowance theorem in *Op* states the exact finite observation assumptions for this comparison \[[3](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}, Section 7\].

## 6 Buying information uses a shared budget {#sec:acquisition}

Evidence and statistical observations have acquisition costs. *How Compliance Composes*, Section 8, defines finite evidence plans that pay once for shared acquisition prerequisites \[[2](#ref-compliance){style="overflow-wrap:anywhere;hyphens:none"}\]. Each plan retains the duties created by every acquisition, including acquisitions of evidence that it later leaves unused. A missing local judgment leaves a conditional plan awaiting that judgment.

*Parlay Identification of Ising Couplings*, Section 6.5, studies a different allocation problem \[[8](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\]. Suppose three estimated quantities have positive variance coefficients $(1,3,9)$. A singleton observation costs one unit. A bundle supplies an observation for all three quantities at cost two. The budget is 600, and the objective sums each coefficient divided by its effective observation count.

Buying 300 bundles gives counts $(300,300,300)$ and objective $13/300$. Buying 240 bundles and 120 additional observations of the third quantity gives counts $(240,240,360)$ for the same cost. The resulting objective is $$\frac{1}{240}+\frac{3}{240}+\frac{9}{360}=\frac{1}{24}.$$

The paper supplies an exact allocation certificate for this better plan. Its allocation theorem covers continuous purchases, positive costs, and finitely many specified positive coefficient scenarios. It determines a unique optimal count vector, although several purchase plans can produce that vector.

The sampling model must justify those effective counts. Copying one observed outcome into several records does not create independent rounds. The objective also differs from the variance of an arbitrary portfolio of correlated estimators. Integer purchases and adaptive acquisition retain the paper's separate qualifications.

An evidence purchase can serve several requirements and create duties that affect another operation in a joint institutional request. A statistical bundle can serve several estimands under one budget. Using either construction in a linked execution requires its costs, rights, sampling assumptions, and consequences to enter the same selected plan. The two optimization results retain their distinct hypotheses.

## 7 Continuing execution needs more than a current balance {#sec:continuation}

Continuation state retains unfinished computation, outstanding duties, and the state needed for its next permitted action. It includes creditors, reservations, pending commands, deadlines, and the effects of later corrections. Retained knowledge records what an observer learns from the accumulated history. Continuation state and retained knowledge are distinct parts of institutional state that can both constrain a future admission.

Two accounts with equal balances can have different payment obligations. Two histories with identical public outputs can have different private debts. A replacement must preserve the future questions that matter to the relying institution. *How Compliance Composes*, Sections 5.6--5.7, makes duties, authority, deadlines, and continuation status explicit in its boundary records and finite route comparison \[[2](#ref-compliance){style="overflow-wrap:anywhere;hyphens:none"}\].

*Admissible Obligation Transitions*, Section 6.3, gives "Future equivalence and exact quotients" for a complete deterministic interface \[[6](#ref-transitions){style="overflow-wrap:anywhere;hyphens:none"}\]. States are equivalent when every admitted future action sequence has the same protected observations. Its finite refinement procedure constructs the coarsest exact grouping. Adding an operation, such as a stay or assignment, can require a finer grouping and a new comparison.

Comparing probabilities of public output histories requires a different test. *Institutional Linking and Realization*, Section 20, compares the full laws of finite public words in a fixed finite stochastic model \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}\]. Equal public probabilities preserve that observation interface. They do not, by themselves, preserve debts or authority omitted from it.

Financial continuation also requires complete state. *Central Counterparty Risk in Automated Markets* computes exact completion cash on a finite acyclic decision graph \[[7](#ref-risk){style="overflow-wrap:anywhere;hyphens:none"}\]. The decision precedes the unknown successor, and every represented branch must remain funded. Delivered receipts, repayment duties, facility limits, and timing enter the graph. Concurrent plans using one facility require a joint state and an aggregate reservation.

## 8 A failed design can state what is missing {#sec:obstructions}

An empty joined relation establishes infeasibility for its declared finite catalog. A residual requirement describes the capability tuples that would complete fixed existing selections. It retains the relationships between fields and a completion witness for each accepted tuple \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 10\].

In the acquisition case, 120 units cannot support ordinary payment across both outcomes. A design query can identify the conditional escrow and reserved standby pair needed for the stated delivery goal. The institutions must still supply those capabilities and admit them against the current history. A computed requirement creates no new authority.

Other profiles have different exact obstructions. An integer payment problem can have a rational solution while divisibility prevents an integral one. A translation network can have inconsistent cycle sums. These tests apply to their specified integer and translation models \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Sections 13--14\].

Random selectors also face implementation limits. Three exactly equal route probabilities cannot come from a deterministic sampler with a fixed finite bound on independent fair bits. Every probability from such a sampler has denominator dividing a power of two. Pad shorter branches to the fixed bit limit. Each output then corresponds to an integer number of equally likely bit strings, which proves the denominator restriction.

Rejection sampling can produce exact thirds with almost-sure termination, but its worst-case running time is unbounded \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 18\]. An available common deterministic route can remove the need for that selector when the contract permits it \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 23\].

Each certificate must identify the model it rejects. A restricted sampler's failure does not reject every permitted controller. An interrupted search reports an unresolved result unless it has an independently checked witness or infeasibility certificate.

## 9 From a compatible plan to a completed act {#sec:realization}

Theorem "Conditional linked realization" connects a compatible plan to execution under explicit assumptions \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 25\]. Its factors must adequately describe the selected programs, goal, and every requirement and interaction. Its checked assignment must define locally executable controllers. Every random selector must satisfy its ownership, secrecy, independence, distribution, and timing contract.

The implementation must preserve modeled transitions and meet the model's progress requirements. Its correspondence must cover the complete admitted observation and outcome interfaces. A safety argument alone permits an implementation that stalls indefinitely.

Every claim about observation probabilities also requires correspondence for the complete linked observation law. The implementation and model use the same actual world, selected controller, environment response strategy, and selector contract. Fix the actual worlds, source interpretation, and response strategies independently of the certificate. The interpretation preserves the compared worlds and local observation interfaces, with one admitted response rule across each comparison. The law includes observable selection, refusal, completion, and timing. Component certificates require a composition proof preserving conditional laws after each complete visible history \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}, Section 25\].

Owners must acquire and protect the exact commitments through their reservation and decision protocols. Current authority, grounded resources, evidence, and provider service must satisfy the premises at their required stages.

Continuing duties and prior disclosures survive new admissions and replacements. *Admissible Obligation Transitions*, Section 7.7, gives a progress theorem for an original finite group of duty episodes \[[6](#ref-transitions){style="overflow-wrap:anywhere;hyphens:none"}\]. Each episode fixes its goal and an integer rank that is zero exactly when the journal records that goal. Later arrivals add no work to the original group's rank.

The total rank must never increase and must decrease productively within each fixed transition interval. The group then completes within interval length times initial rank. An elapsed-time bound additionally requires a clock bound that includes waiting.

*The Claim as Primitive*, Section 12, composes provider completion bounds when their prerequisites and contracts hold jointly \[[5](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\]. An acyclic prerequisite graph gives a maximum path-sum bound. A cyclic group needs a suitable external starting fact or a jointly valid completion contract. Rearranging the dependency graph supplies no provider service by itself.

Under these conditions, the selected strategy satisfies the conjunction of requirements for the declared finite profile and goal. This is a conditional realization theorem with separate source and provider obligations. It supplies no new unrestricted composition theorem for all institutional software.

Legal effect and external recovery retain their named authorities. *Recourse* distinguishes an award, enforcement, and receipts that support monetary satisfaction \[[9](#ref-recourse){style="overflow-wrap:anywhere;hyphens:none"}\]. A linked program can preserve a recovery claim and transmit an authorized instruction. The institution that controls the asset, payment, or legal act must supply the corresponding external result.

## 10 Technical reading map {#sec:reading-map}

*Institutional Linking and Realization* \[[1](#ref-linking){style="overflow-wrap:anywhere;hyphens:none"}\] supplies the synthesis. Read Sections 2--4 for the execution contract, information-cell compilation, and complete joining. Sections 7--11 give ordered funding, independent-choice cells, the exact capacity trade-off, residual requirements, and funded acquisition. Sections 17--23 distinguish cumulative privacy, selector implementation, public-law comparison, and deterministic future equivalence. Section 25 states "Conditional linked realization" and all implementation premises.

*How Compliance Composes* \[[2](#ref-compliance){style="overflow-wrap:anywhere;hyphens:none"}\], Sections 5.6--5.7, contains "Lossless contextual composition," "Lossless evidence-and-obligation boundary," and "Finite institutional route equivalence." Section 3.4 proves "Exact independent recombination" and "Extension on a join tree." Section 8 defines executable evidence plans and exact finite search.

*Op: Compliance-Carrying Operations* \[[3](#ref-op){style="overflow-wrap:anywhere;hyphens:none"}\], Sections 5.11 and 7, contains "Global declared exposure bound," "Least observable allowance," and "Joint and separate reservations." Section 7.3 gives "Exact resource menu cover for two groups." *The Sovereign Jurisdiction Network* \[[4](#ref-recognition){style="overflow-wrap:anywhere;hyphens:none"}\], Sections 5.4--5.5, supplies "Preservation of source obligations" and "Joined permitted-success selector."

*The Claim as Primitive* \[[5](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\], Section 3.1, gives "Entitlement preservation." Section 6.4 states "Durable retry and conservation," and Section 12 composes provider completion contracts. *Admissible Obligation Transitions* \[[6](#ref-transitions){style="overflow-wrap:anywhere;hyphens:none"}\], Sections 3.5 and 5, gives receipt meaning and "Engine-relative parametric lifecycle preservation." Sections 6.3 and 7.7 supply future equivalence and "Original-cohort progress under continuing arrivals."

*Central Counterparty Risk in Automated Markets* \[[7](#ref-risk){style="overflow-wrap:anywhere;hyphens:none"}\], Sections C.2--C.3, develops the "Finite completion model" and "Exact adapted completion cash."

*Parlay Identification of Ising Couplings* \[[8](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\], Section 6.5.1, gives "Robust shared-observation allocation" and "Exact allocation certificate."

*Recourse* \[[9](#ref-recourse){style="overflow-wrap:anywhere;hyphens:none"}\], Sections 9.7 and 10.8, supplies "Bitemporal authority and effect integrity," "Award is not recovery," and "Continuation and resource conservation."

## References

::: {#ref-linking}
:::

**\[1\]** R. Lorgat. *Institutional Linking and Realization*. September 2026.

::: {#ref-compliance}
:::

**\[2\]** R. Lorgat. *How Compliance Composes*. September 2026.

::: {#ref-op}
:::

**\[3\]** R. Lorgat. *Op: Compliance-Carrying Operations*. September 2026.

::: {#ref-recognition}
:::

**\[4\]** R. Lorgat. *The Sovereign Jurisdiction Network*. September 2026.

::: {#ref-claim}
:::

**\[5\]** R. Lorgat. *The Claim as Primitive*. September 2026.

::: {#ref-transitions}
:::

**\[6\]** R. Lorgat. *Admissible Obligation Transitions*. September 2026.

::: {#ref-risk}
:::

**\[7\]** R. Lorgat. *Central Counterparty Risk in Automated Markets*. September 2026.

::: {#ref-parlay}
:::

**\[8\]** R. Lorgat. *Parlay Identification of Ising Couplings*. September 2026.

::: {#ref-recourse}
:::

**\[9\]** R. Lorgat. *Recourse*. September 2026.
