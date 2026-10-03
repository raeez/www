# Prices, Information, and Clearing Risk

## Abstract

A payment of 100 is due before securities worth 80 can produce cash. With only 20 available, the payment has an 80 funding gap. This article explains how joint prices, independent observations, trading incentives, liquidation responses, and payment timing enter different mathematical questions. The constructions provide exact identification, allocation, finite-state, and funding results under stated assumptions. They also identify incompatible quotes, hidden interactions, unstable responses, and unfunded continuations. Physical calibration, current authority, and provider performance require their own evidence.

## 1 A payment before the proceeds arrive

Consider the opening case more precisely. A clearing participant owes 100 at time 1, holds cash of 20, and receives 80 from securities at time 2. The time-1 gap remains 80, even if the later receipt is certain. This example appears in *Central Counterparty Risk in Automated Markets*, §6.1, Example 6.7 \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}\].

*Market liquidity* concerns trading without a large price change. *Funding liquidity* concerns obtaining the required settlement asset before payment is due. A liquid market can still deliver proceeds too late. A solvent position can therefore fail a particular payment schedule.

A claim specifies a right or obligation and the conditions determining its outcome. Its acquisition price, calculated payoff, and actual performance answer different questions. *The Claim as Primitive*, §1.1, separates the calculated value from the amount owed and the evidence that discharges it \[[2](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\]. Here *clearing* means computing obligations within a clearing book. Sending an instruction and receiving the resulting payment remain distinct events.

Permission also affects the relevant demand. In *One Entity in Many Jurisdictions*, §7, a one-unit second-price auction uses funded bids \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}\]. Bids of 100, 80, and 30 give a price of 80. Removing the bidder at 30 leaves that price unchanged. Removing the bidder at 80 reduces it to 30.

Adding a permitted investor class supplies no extra demand unless someone participates with funding. The comparison fixes the auction and other buyer inputs. It does not predict the net price effect of adding a jurisdiction.

## 2 What a joint price reveals

Two binary events have four possible joint outcomes. Their individual success probabilities leave their dependence unspecified. A *parlay* pays on their joint success. Its probability, together with the two individual probabilities, determines the four outcome probabilities.

Write these four probabilities as $q_{++},q_{+-},q_{-+},q_{--}$. Each sign records one event's outcome. When every cell is positive, the pair has an exact representation with two individual parameters and one interaction parameter: $$J^{\mathrm{eff}}=\frac14\log \frac{q_{++}q_{--}}{q_{+-}q_{-+}}.$$ The logarithm is natural. The individual parameters describe each event's conditional tendency, while $J^{\mathrm{eff}}$ describes the pair's effective association. This is the two-event inversion in *Parlay Identification of Ising Couplings*, §3.1, Theorem 3.1 \[[3](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\]. A zero cell remains a valid boundary probability law but lies outside this finite-parameter representation.

A coherent price system supplies a *pricing law*, denoted $Q$. A *physical law*, denoted $P$, describes how outcomes actually occur. The inversion can identify $Q$ exactly without establishing $Q=P$. Outcome observations and an explicit calibration model must support that additional connection.

Price sensitivity has a related boundary. A market's *curvature* records how its marginal prices change with inventory. For a cost defined by a scaled logarithm of summed exponentials, curvature equals payoff covariance divided by its positive liquidity parameter. Covariance measures joint variation under a specified law. Here that law is the venue's implied pricing law.

*The Claim as Primitive*, §8.4, proves this identity for its log-partition class \[[2](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\]. An arbitrary trading curve does not reveal physical covariance.

### 2.1 An interaction created by a shared neighbour

An *Ising model* represents binary outcomes by individual terms and direct pair interactions in their log probabilities. Averaging over other events can change the interaction seen in one pair.

Take three events in a chain. Set all individual terms to zero, both neighbouring interactions to $0.3$, and the direct endpoint interaction to zero. Averaging over the middle event gives $$J^{\mathrm{eff}}=\tfrac12\log\cosh(0.6)\approx0.08507.$$ Both endpoint success probabilities are one half. Their positive effective interaction comes entirely through the middle event. More observations of that endpoint pair estimate the same effective interaction more precisely. They do not make it converge to the zero direct interaction. This is Example 4.3 of *Parlay Identification of Ising Couplings* \[[3](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\].

Proposition 4.1 supplies a sharp bound on this mediated contribution. Let $U$ and $V$ be the sums of absolute interactions connecting each endpoint to the remaining events. The difference between effective and direct interaction has magnitude at most $$\frac12\log\frac{\cosh(U+V)}{\cosh(U-V)}.$$ The remaining network can have arbitrary finite interactions. One unbiased intervening event attains the bound. Using it to infer a direct interaction requires independent evidence for $U$ and $V$. Section 5.1 gives direct-identification constructions from a positive full-vector pairwise law or a known tree with positive consistent singleton and edge probabilities.

### 2.2 Consistent pairs can form an impossible collection

Even positive pair tables need not fit one joint law. Set three binary spins' means to zero and every pair moment to $-2/5$. Each pair then has positive cells $(3,7,7,3)/20$. The proposed covariance matrix has positive eigenvalues $1/5,7/5,7/5$.

Nevertheless, every three-spin outcome satisfies $$x_1x_2+x_1x_3+x_2x_3\geq-1.$$ The proposed pair moments require an expectation of $-6/5$, which is impossible. Thus *positive semidefiniteness*, meaning nonnegative variance for every linear combination, is necessary but insufficient for binary joint compatibility.

The exact compatibility test assigns nonnegative probabilities to all complete outcomes and checks the requested moments. In this example, the smallest maximum-coordinate correction is $1/15$. Uniform probability on the six nonconstant outcomes attains it, giving pair moments $-1/3$. These results appear in §3.2, Proposition 3.4 and its following counterexample \[[3](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\].

## 3 Buying observations with a checkable allocation

An observation must identify its events, resolution rule, round, and population. Ten thousand contracts on one resolution still supply one round. The fixed-law estimates require independent rounds with the same pair law. Missing outcomes or changing selection can invalidate that premise.

Near an empty cell, the interaction estimate can become arbitrarily large. Section 6 of *Parlay Identification of Ising Couplings* therefore retains a cell confidence set when an empirical cell is empty \[[3](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\]. Adding artificial counts gives a separately labelled regularized estimate. It does not create an unregularized finite estimate or remove uncertainty.

Section 7 treats changing laws. It combines sampling error with a separately supported bound on full-cell drift across each declared observation window. Simultaneous coverage over the declared windows permits selection after observing the data. A bound on interaction drift alone is insufficient because changing individual probabilities can create pooled association. Certified outward arithmetic preserves the resulting coverage statement without proving its sampling or drift premises.

Observation bundles can reduce acquisition cost. Each modeled variance term equals its coefficient divided by its effective observation count. Suppose three estimates have positive variance coefficients $(1,3,9)$. A separate observation costs one unit, while a bundle observing all three costs two. With budget 600, buy 240 bundles and 120 extra observations of the third quantity. The counts are $(240,240,360)$, and the sum of variance terms is $$\frac1{240}+\frac3{240}+\frac9{360}=\frac1{24}.$$ Buying only 300 bundles gives the larger value $13/300$. This is the worked allocation in §5.3.1 \[[3](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\].

The general construction allows finitely many coefficient scenarios and observation bundles. It minimizes the worst scenario's sum of coefficient divided by effective count. Bundle costs are positive, all coefficients are positive, and every estimated quantity has some available observation. Counts come from a declared incidence matrix, which records what each purchase observes.

Theorem 5.5 gives an attained *dual*: a maximization whose value supplies an exact lower bound matching the purchase problem's optimum. It assigns nonnegative values to observed quantities, constrained by every bundle's cost. It also chooses a weighted average of the coefficient scenarios. The optimal effective counts are unique, though different purchase plans can produce them.

Proposition 5.6 checks a proposed allocation using its purchases, worst-scenario weights, and marginal-value inequalities. Purchased bundles meet the cost inequality with equality. All unused bundles must satisfy it too. Rational inputs and a rational witness permit exact checks. In the example, values $(1/4,3/4,1)$ certify the optimum $1/24$.

This objective sums individual variance terms. Correlated errors in a combined estimator require a different loss calculation.

Continuous purchases also differ from whole observations. Proposition 5.8 gives a rounding bound with an explicit budget reserve. That reserve sums the costs of bundles used by the continuous optimum. The budget must exceed it, and rounding guarantees a feasible approximation. Learning the coefficients while choosing observations retains a separate adaptive-inference obligation.

## 4 A price signal changes trading incentives

A strictly proper score makes truthful reporting uniquely optimal when that score is the reporter's relevant payoff. Coupling the report to another market can create an additional payoff. The complete incentive calculation must include the reporter's positions there.

*One-Way Coupling of Prediction Markets to Automated Market Makers*, §2, characterizes truthful reporting along the report-driven path \[[4](#ref-coupling){style="overflow-wrap:anywhere;hyphens:none"}\]. With fixed reserves, a differentiable strictly proper score, and an outcome-independent transfer, truthfulness for every belief requires constant transfer along the path. A one-way construction satisfies this condition.

External holdings still matter. Section 5 studies a logarithmic score held to resolution, an unchanged outcome law, and expected payoff in a common unit and horizon. It bounds reporting distortion using the aggregate outside payoff's range and sensitivity, relative to scoring liquidity. Splitting one beneficial owner's positions across accounts does not split that economic exposure.

Long trading sequences require cumulative accounting. On a finite directed graph, let each state record the economically relevant inventory and control. Each edge has a declared gain weight. A *potential* assigns a number $\phi(u)$ to each state such that $$w(u,v)\leq\phi(u)-\phi(v).$$ Summing along a closed path cancels the potential differences. Every cycle therefore has nonpositive total weight. Proposition 7.4 also proves the converse: nonpositive cycles admit such a potential. The least nonnegative potential is the maximum path weight starting at each state, including the empty path. Simple paths suffice because removing a cycle cannot reduce that weight.

The economic interpretation must specify the weights. The retained-fee application uses logarithmic reserve loss, not cash profit per trade. Each gross power-reserve trade holds its exponent fixed and charges fee $f$ times the absolute gross cash movement. Assume $0\leq f<1$. Immediate retention protects every finite inventory-restoring sequence when $f\geq1-g_\ell/g_h$. The admitted reserve exponents obey $0<g_\ell\leq g_h$, reserves stay positive, and no external reserve flows occur. A different fee route requires its own accounting.

##### A funded signal adjustment.

Section 8 gives another construction. A sponsor pays for control changes through an account whose uncommitted cash cannot become negative. Transfers are exact and atomic, with no fees or external reserve flows. In its worked example, reference inventory and cash scale are both 100. The control ranges from $0.8$ to $1.2$, and log inventory stays within $0.2$ of its reference.

Buy inventory down to $100e^{-0.1}$ at control $0.8$, then change the control to $1.2$. The required sponsor deposit is $100(e^{0.12}-e^{0.08})$, approximately $4.42098$. Selling back and restoring the control gives the trader exactly that amount. A sponsor balance of 5 funds one cycle but cannot fund a second identical cycle without replenishment.

Theorem 8.3 bounds aggregate trader cash gain by the initial sponsor balance when inventory and control close. Restoring the sponsor account too gives zero aggregate gain. Pending commitments and admitted changes between funding modes must enter any broader state model. The complete cross-mode potential construction remains open.

## 5 Liquidation changes subsequent risk

*Expected Shortfall* is the average loss in a specified worst fraction of a loss distribution. Computing it requires a loss law and a horizon. A covariance matrix alone gives an exact quadratic aggregation only under the stated common elliptical family and linear-loss assumptions. Here the centered linear projections share the same distributional shape after rescaling.

A digital payoff pays a specified amount if a condition holds. For general digital payoffs, the full joint law matters. The full portfolio calculation must count each hedge once \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}, §3\].

The physical-risk construction uses a common uncertainty set of candidate outcome laws. Its coverage of the actual law requires separate evidence. A certified numerical optimization gap bounds computational error in the specified problem. It does not establish that coverage. These distinctions govern the entropy-clearing and physical-risk certificates in §4 of *Central Counterparty Risk in Automated Markets* \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}\].

For fixed losses, the waterfall assigns losses through disjoint funded resources in a declared priority order. Theorem 6.12 gives a unique allocation and an exact condition for eliminating the book's residual. Reducing an unpaid profit claim reduces an obligation. It supplies no new cash. Netting also requires the applicable legal right \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}, §6\].

Settlement timing changes who carries risk. When title and cash move together, no exposure remains. When title moves at the trade and cash is netted later at a governed cut-off, someone carries the buyer's failure in between. Each product therefore declares a stance. A consumer account is prefunded: the buyer's cash is reserved at the trade. Institutional members can settle under guaranteed net settlement, with collateralised debit caps and liquidity sized to the largest failures. Only interposition by the central counterparty supports the full waterfall. Netting at a cut-off conserves cash exactly and moves only net amounts, with pay-ins collected before pay-outs. A covered member's failure to pay is funded first from its own resources. Surviving members' margin and customer assets never fund another's default. A cut-off is a time in a business centre, so it requires a certified clock, not a block count \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}, §6\].

### 5.1 A certificate across changing liquidation regimes

A sale can lower prices, trigger another funding requirement, and cause further sales. The causal response matrix bounds those additional sales. It uses holdings, funding responses, price impact, and common units. A correlation matrix does not supply these causal inputs.

When rules or funding conditions change, the system moves between regimes on a finite directed graph. Proposition 8.9 bounds newly dispatched sales using the admitted transition matrix plus a separate change in the liquidation target. A contraction shrinks the inherited response at each step. Bounded target changes bound increments. The proposition's lifetime bound assumes summable target-change bounds and is independent of the inventory cap \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}, §8.2\].

Testing each regime alone is insufficient because alternating responses can amplify one another. Theorem 8.13 treats finite regime graphs with nonnegative response matrices. It characterizes uniform exponential decay of every admitted matrix product, called strict exponential stability. Each regime uses a norm, a measure of response size, built from finitely many nonnegative weighted sums of absolute coordinates. The norm takes their maximum.

Every admitted transition must contract between the corresponding norms. Such norms exist exactly under strict exponential stability. Rational matrices then admit rational certificates. Failure to find one chosen shape of norm is inconclusive.

### 5.2 Averaging and retained cash floors

Passive averaging can slow an unstable response while leaving it unstable. Each first-order averaging stage adjusts toward its input over a specified positive time scale. An equilibrium keeps every stage's value constant. Proposition 9.6 examines a positive common equilibrium value with frozen coefficients. Write $\rho$ for its feedback gain. A finite cascade of these stages has one positive real growth rate whenever $\rho>1$ \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}, §9.1\].

For a constructed illustration, take $\rho=1.21$ and two stages with unit time constants. The characteristic equation $(1+s)^2-1.21=0$ gives rates $0.1$ and $-2.1$. Doubling both time constants reduces the positive rate to $0.05$. It remains positive.

This establishes local instability of the stated positive equilibrium. A collapse forecast additionally requires branch selection and the source's evolving-dynamics assumptions. Continuation across the critical impasse remains a separate question.

Settlement discipline can remove one specific feedback channel. The model requires an eligible settlement asset independent of locked pool liquidity. It excludes pool shares and the hub asset from collateral and prohibits clearing-induced liquidity withdrawals. Denomination alone does not satisfy that behavioural condition \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}, §11.1\].

Theorem 11.10 separately bounds the remaining exogenous cash tranche under exogenous-first drain priority. The shortfall must fit within that tranche, and collected fees must be nonnegative. Post-draw cash equals prior tranche cash minus the shortfall plus paid fees, independently of the next hub price. Whole-fund nondecrease in expectation additionally requires the stated conditional nondecrease assumption for the hub price and expected fees covering expected shortfalls. Any buyback consumes actual cash and must retain current required funding. The floor calculation cannot count that expenditure twice or ignore it.

## 6 The cash required to finish

Return to the payment deadline. Appendix C of *Central Counterparty Risk in Automated Markets* models a finite acyclic graph of observable states \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}\]. Each action records its immediate debit, retained cash floor, possible next observations, later cash changes, and remaining debts. A policy chooses an action using only observations already available.

Theorem C.4 computes the exact initial cash needed to complete every represented outcome. It works backward from terminal obligations. At each state, one permitted action must fund every successor still possible when chosen. The calculation then selects the least demanding such action. Choosing separately after learning a future outcome would understate the requirement.

##### Borrowing includes repayment.

Example C.10 permits a facility draw of 60 before a payment of 100. Repayment of 65 follows a separate receipt of 65. The least initial cash is 40:

  Event               Available cash
  ----------------- ----------------
  Initial balance                 40
  Draw 60                        100
  Pay 100                          0
  Receive 65                      65
  Repay 65                         0

Removing the later receipt raises this borrowing route's requirement to 105. If the graph permits a cash-only route, its requirement of 100 is preferable. Including facility failure as a possible branch also raises the original plan's root requirement to 100. A promised draw cannot substitute for its specified availability and receipt conditions.

An independent reserve of 30 raises the first plan's total to 70, leaving 30 at completion. Do not add a reserve again when the graph's floors already include it. Lemma C.6 preserves every checkpoint when combining fixed cash paths. Paying 100 before receiving 100 requires initial cash of 100. Reversing those events requires zero. Both paths have the same final cash change.

Several currencies or restricted assets require separate balances. Proposition C.7 computes the exact minimal resource vectors, each with a completing strategy, under fixed componentwise action eligibility. This finite frontier can have $2^n$ incomparable vectors after $n$ decisions, even with only two resources. Conversion requires an admitted action with its own rate, limits, timing, and authority. Finite enumeration does not establish an efficient compact representation.

Durable execution must preserve the same cash and obligation identities after retries, interruptions, and returns. The correspondence concerns one settlement authority and integral amounts in one asset. Updates must commit in an order equivalent to sequential execution. It assumes truthful occurrence identities, current permissions and resource bindings, and provider records. Storage must preserve committed transactions after restart and resist operator rollback to an earlier state.

Recorded returns restore cash and reopen obligations. Those obligations must discharge before further graph progress.

A repeated receipt supplies no second cash inflow. These external premises determine whether the mathematical continuation describes an actual payment process.

## 7 Technical reading map

- *One Entity in Many Jurisdictions*, §7: "Admissibility-conditioned pricing" and "Exact accession comparison for the auction." Read the fixed buyer context and funded-bid construction together \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}\].

- *The Claim as Primitive*, §1.1 and §8.4: payment versus discharge, "Covariance in the log-partition class," and "Scope of the covariance reading" \[[2](#ref-claim){style="overflow-wrap:anywhere;hyphens:none"}\].

- *Parlay Identification of Ising Couplings*, §3.1, Theorem 3.1, and §3.2, Proposition 3.4: positive pair inversion and complete-law compatibility. Section 4, Proposition 4.1 and Example 4.3, give mediated-interaction bounds and the chain case. Section 5.3.1, Theorem 5.5 and Propositions 5.6--5.8, covers shared acquisition, exact certificates, complementary bundles, and integer rounding. Sections 6--8 state sampling, drift, boundary, and quote-error requirements \[[3](#ref-parlay){style="overflow-wrap:anywhere;hyphens:none"}\].

- *One-Way Coupling of Prediction Markets to Automated Market Makers*, §2, Theorem 2.1, and §5, Theorem 5.1: truthful reporting and outside-payoff bounds. Section 7, Theorem 7.3 and Proposition 7.4, covers retained fees and finite potentials. Its open problem concerns compatible certificates across execution modes. Section 8, Theorem 8.3, gives the funded adjustment. Section 10 retains equilibrium and calibration obligations \[[4](#ref-coupling){style="overflow-wrap:anywhere;hyphens:none"}\].

- *Central Counterparty Risk in Automated Markets*, §§3--4 and §6, Theorem 6.12: physical risk, numerical certification, and fixed-loss clearing. Section 8.2, Proposition 8.9 and Theorem 8.13, gives regime certificates. Section 9.1, Proposition 9.6, gives passive-cascade instability. Section 11.2, Theorem 11.10, gives the cash-tranche floor. Appendix C, Theorem C.4, Lemma C.6, Proposition C.7, and Example C.10, develops adapted completion cash, path composition, resource frontiers, and funded borrowing \[[5](#ref-ccp){style="overflow-wrap:anywhere;hyphens:none"}\].

## References

::: {#ref-entity}
:::

**\[1\]** R. Lorgat. *One Entity in Many Jurisdictions*. 2026.

::: {#ref-claim}
:::

**\[2\]** R. Lorgat. *The Claim as Primitive*. 2026.

::: {#ref-parlay}
:::

**\[3\]** R. Lorgat. *Parlay Identification of Ising Couplings*. 2026.

::: {#ref-coupling}
:::

**\[4\]** R. Lorgat. *One-Way Coupling of Prediction Markets to Automated Market Makers*. 2026.

::: {#ref-ccp}
:::

**\[5\]** R. Lorgat. *Central Counterparty Risk in Automated Markets*. 2026.
