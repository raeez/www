# Institutional Computation

## Abstract

A company secretary submits a valid filing at 16:59, but her delegation expires before the registrar accepts it at 17:01. The filing exposes a general problem: institutional programs act while authority, evidence, rights, and resources change. This article explains constructions that check authority at use, preserve the meaning of rights, and account for shared resources. It then examines which actions retain a route to the required outcome and which foreign determinations another authority can recognize. The results have explicit boundaries: finite workflow contracts, competent authority sources, faithful rules, and evidence of external performance. Worked cases connect these conditions to the technical papers that establish them.

## 1 A filing whose authority expires {#sec:filing}

Consider Cedar Works Ltd, the fictional company in *Programmable Institutions*, Section 2. Its secretary, Mira, may file a change of registered office until 17:00 on 30 September. The assumed rule requires a board resolution and an authorized secretary. Mira submits the resolution and the proposed address, 12 Kestrel Road. The program checks her delegation at 16:59, but the request reaches the registrar's acceptance step at 17:01. Under these example terms, the registrar must refuse that change \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 2\].

The relevant event is the registrar's acceptance of the change into its authoritative record. The paper calls this event a *commit*. Authority means permission for the named person, action, object, and time. An earlier successful check establishes the earlier permission. The commit needs a check covering its own time, together with the current rule and record.

Suppose the registrar accepts the same filing before expiry and every other condition holds. Its record changes from the old address to the new one. A retained evidence record, called a *receipt*, identifies both states, the delegation, the board resolution, the rule, and the acceptance time. That receipt allows an authorized reviewer to reconstruct the accepted act. The registrar remains the institution responsible for its record.

A further condition can require the registrar to judge whether the address is suitable for official service. The program then records the exact question, its evidence, permitted answers, and the role authorized to answer. This unanswered question is a *discretion hole*. The request waits for a competent answer. A timeout supplies no judgment, and an answer concerning a different address supplies no answer to this request.

This case establishes the article's central distinction. Preparing an action, satisfying its rule, holding authority, and changing an institutional record are separate events and conditions. An institutional program must preserve their relationship as work proceeds. *Programmable Institutions* makes that relationship precise for one institution's record. *One Entity in Many Jurisdictions* specifies the persons, rights, and actions that an authority evaluates. *Accession Networks* studies how independent authorities establish recognition relations \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Sections 2--4\]\[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 2\]\[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Sections 2, 4\].

## 2 Which person, which right, which action {#sec:rights}

An institutional record needs more than the company's name. One legal person can have several local registrations, each with its own authority, scope, and effective period. A subsidiary instead has its own legal identity. The formal construction records these relationships explicitly and takes their legal effect from the relevant law and instruments \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 2\].

Rights also require separate records. Registered ownership, voting power, a security interest, and participation in sale proceeds can belong to different persons. A *constituting act* is the instrument or authoritative event that creates the right. The right's record identifies that act, its beneficiary, covered assets, quantity, priority, and effective interval. Changing a beneficiary therefore requires the transition that authorizes that change.

Take the assumed share arrangement in *One Entity in Many Jurisdictions*, Section 2, "Title, participation, and security." R holds 100 identified shares and their votes. B has a right to 40 percent of the residual sale proceeds. C has priority over those proceeds up to ten currency units. If the received proceeds are 100, C receives ten, leaving 90. B receives 36 and R receives 54, so the three amounts exhaust the received 100 \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 2\].

The calculation preserves the assumed priority and participation terms. Registered votes and authority to spend R's cash require their own instruments. R's title remains recorded until an effective transfer changes it. The example describes a distribution of received proceeds under stipulated terms. It establishes no market value or external payment by itself.

Even a share split needs a declared unit. The source's two-for-one split changes 100 covered shares into 200 replacement shares. A selected entitlement of 40 old-share units remains 40. Each replacement share contributes one-fifth of an old-share unit to that entitlement, giving $200/5=40$. Keeping the old two-fifths coefficient would incorrectly give 80. The contractual participation remains 40 percent \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 2, "A split with retained participation"\].

The paper's theorem "Preservation of quantitative rights" compares the same named entitlements before and after a permitted corporate action. Its linear calculation requires fixed right identities, beneficiaries, units, and an admitted position domain. Applicable instruments supply the action's authority and rights interpretation. Agreement on a few examples cannot establish preservation over every admitted position.

The next evaluation must identify the proposed act just as carefully. An *action context* names the person, right, operation, parameters, participants, purpose, destination, time, and current rules. Permission to hold shares can coexist with a refusal to offer them publicly. The authority set must include every requirement reaching that act. Choosing fewer registration labels cannot remove an applicable requirement \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 2, "Scoped action"\].

## 3 What the acceptance step must establish {#sec:acceptance}

A delegation is a recorded grant of specified permission. The source calls it a *capability*. Its scope includes objects, actions, fields that may change, permitted judgment answers, validity, and further delegation limits. Each delegate receives a subset of the parent's authority. The same complete chain must cover every required part of the act \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 3.1\].

For Mira's filing, permission to change an address does not authorize changing the shareholder record. The operation declares every field it may write. The acceptance step checks the actual change against that declaration and the same authority chain. A temporary shareholder change followed by restoration contains two observable changes when both states are externally visible. The record must retain both. Isolated private computation can remain hidden only when it has no external observer or dispatch capability \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 3.3 and Section 4, Corollary 1\].

The rule's factual dependencies require equal care. A *dependency* is an observation that can affect the evaluation. It can be a value, a query result, or the absence of a conflicting record. The program must record all such dependencies and check them with the accepted change. A new conflicting judgment can invalidate an earlier evaluation even if every previously read document remains unchanged.

Dependency completeness concerns changes considered together. The source uses two false conditions joined by "and." Changing either condition alone leaves the result false, while changing both makes it true. Testing isolated changes would miss this dependency. Lemma 2 establishes complete dependency tracking for the paper's specified finite expression language \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 3.2\].

Under assumptions F1--F10, Theorem 1 attributes each final field difference to an accepted change with a live authority chain and receipt. Corollary 1 extends the account to every observable write, including changes later reversed. The assumptions include exclusive control of authoritative writes, faithful effect declarations, complete judgments, atomic checks, authenticated actors, and trusted record time. They also require complete authority information at each use \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 4\].

That last premise has an institutional source. A delegation can end through an external order before its printed expiry. A valid signature on the delegation cannot establish that no such event occurred.

The construction therefore requires a *coverage contract* for each required competent source. It identifies covered objects, event classes, jurisdictions, and the times covered by the evidence. It states acceptable delay, outages, conflict resolution, and legally sufficient conditions for present use. The source must meet those conditions before the act proceeds. A delayed feed leaves the uncovered interval unresolved unless the contract supplies that condition \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 6.1\].

Retained evidence must include retrievable content. A *digest* identifies exact bytes, but a future reviewer still needs those bytes and any required decryption permission. The evidence manifest records content, custodians, retention duties, and access conditions. Missing documents, missing keys, restricted disclosure, and invalid evidence produce different reconstruction results \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 6.2\].

These results establish execution relative to the encoded rule. If that rule omits a required legal condition, a perfectly reconstructed execution can still apply the wrong rule. Section 5.5 gives this counterexample explicitly. Legal validation must establish the rule's fidelity and the institution's authority for the stated act and time.

## 4 Resources already promised elsewhere {#sec:resources}

Delegation limits can fail through duplication even when every individual act has the right scope. Suppose a principal permits expenditure of 100 units and appoints ten delegates. Giving each delegate an independently spendable limit of 100 would permit aggregate expenditure of 1,000. All delegates must instead use the same underlying allowance \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.5\].

A *reservation* records capacity committed to an admitted command whose performance remains possible. The common allowance counts consumed expenditure and unresolved reservations across every descendant delegate. Two commands can reserve 40 and 60 against the 100-unit limit and then execute concurrently. Two commands cannot each reserve 100. A new account alias or service identity creates no additional allowance.

Theorem 3, "Aggregate economic attenuation," preserves these limits under the stated accounting rules. One admission boundary must own all counters and cover every command that can charge the allowance. Every possible charge is nonnegative, and its reservation must bound it under every permitted external outcome. Admission checks and reserves the amount atomically against every ancestor's limit.

Authenticated performance moves its charge from reserved to consumed use only within the admitted bound. An exact retry preserves the original command record. Each new dispatch requires current authority and complete dependency checks. Unknown performance retains its reservation until an admitted release establishes that the command cannot incur further charges \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.5\].

Cash needs its own ownership and use constraints. A *legal estate* is the body of assets and obligations to which a resource belongs under its governing arrangements. For a funding pool, use $c$ for recorded cash, $e$ for prior encumbrances, and $r$ for pending reservations. The uncommitted amount is $$f=\max\{c-e-r,0\}.$$ An additional payment requires enough free cash, permitted use, and current authority for the exact act \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 2, "Estate-specific funding"\].

The source gives an operator estate with 100 units and a client estate with zero. A client payment of 80 fails even when one person controls both estates. An effective, permitted loan of 80 can leave their balances at 20 and 80, with a separate receivable and liability. If the operator already reserved 30, only 70 remains free, so that transfer fails its funding condition.

Each of these numbers answers a different question. An allowance bounds permitted expenditure. A cash balance records available money in its named estate. An outstanding obligation states what someone must still deliver or pay. The record requires separate evidence that the responsible party performed the obligation.

## 5 Keeping a route to completion {#sec:completion}

An action can respect its allowance and still prevent completion. *Programmable Institutions*, Section 7.7, starts with 100 units. A permitted preliminary purchase costs 60, and every remaining delivery route requires another 60. With no further funding available, the purchase leaves 40 and prevents delivery. Alternative complete delivery routes costing 90 or 80 remain viable under their stated outcomes \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.7\].

The program therefore needs a defined goal. *Safety* means that every reached state satisfies the declared restrictions. *Completion* means reaching an authorized terminal outcome within the specified remaining decisions. A refund qualifies only when the governing goal permits it. Replacing delivery with a convenient refund changes the undertaking unless the applicable terms authorize that result.

The finite construction works backward from the permitted terminal outcomes. It retains a next action when every allowed response remains safe and leaves a continuation with one fewer decision. This includes intermediate states along the response, not just its endpoint. An action with no possible response cannot count as successful through an empty check. Theorem 4 identifies exactly the actions preserving guaranteed completion under this fully observed finite contract \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.7\].

The environmental contract lists the provider responses, evidence delays, authority changes, and losses the model admits. Its completeness matters because the guarantee covers that list. An omitted provider failure cannot acquire coverage from the theorem. A response outside the contract requires a fresh analysis while existing duties remain recorded. A deadline also requires bounded response duration and a schedule, beyond a count of decisions.

Often the program does not observe the complete state. After a delayed reply, the same evidence may fit either a live delegate or a revoked delegate. The paper represents this uncertainty by a nonempty set of possible states, called a *belief*. Here belief has no probability attached.

Each modeled state retains all history that constrains later responses. The contract also specifies exactly which evidence and timing the program observes. Each new observation retains precisely the states compatible with the complete action and observation history \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.8\].

Theorem 5 applies the backward construction to these sets. The chosen action must be executable in every possible state, and every permitted response must remain safe. A guarded attempt may perform under live authority and return a local refusal under revoked authority. Both responses preserve their actual histories and remaining duties. The program can declare completion only when every state still compatible with its evidence satisfies the goal.

For the source's two-party service, one party reserves 80 units and the other reserves a service slot. The judgment must arrive within two admitted opportunities to obtain its answer. An approving judgment can arrive after the delegate loses authority. A guarded refusal preserves both reservations and duties. A separately authorized owner can transfer the unused reservation to a fresh command and perform under current authority. The refusal path fits six decisions under these mandates and competent response conditions \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.8, Example 1\].

An adverse judgment instead requires the permitted joint cancellation and its simultaneous releases and discharge. The program cannot guarantee delivery when the judgment may refuse performance. Returning money alone leaves the other party's performance claim unresolved. The permitted terminal goal must cover the actual undertaking \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 7.8, Example 1\].

## 6 Reusing a determination across authorities {#sec:recognition}

*Recognition* gives stated local effect to another authority's determination under an applicable rule or instrument. Its record identifies the original assertion, issuing authority, subject, permitted use, validity, and dependencies. The receiving authority retains each decision reserved to it. Recognized evidence can answer a specified question while leaving a separate local question pending or refused \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Sections 2 and 5\].

The source's synthetic collection workload makes the benefit concrete. Three authorities each require four common evidence answers and two local answers. Independent collection produces $3(4+2)=18$ answers. Permitted common collection produces $4+3\cdot2=10$, including all six local answers. An expired common observation requires a current replacement or leaves its question unresolved. A local refusal remains effective \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 10\].

Those counts measure stipulated collection work. Actual savings also depend on verification, coordination, maintenance, and local review. Recognition through an intermediary requires further attention to every restriction and question along the route. *Accession Networks* retains the source assertions, applicable policy clauses, current answers, and evidence of their compatible use \[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Sections 5.2 and 6.3\].

A summary can show the strongest available recognition class for each subject. Different routes may supply different subjects, so that summary need not describe one usable route. Several routes can contribute evidence when their complete evidence family satisfies the joint admission conditions. The destination's current permission remains a separate condition. Its supporting evidence and current permission require their own records.

## 7 Common filings and the terms they preserve {#sec:accession}

*Accession* means joining a common instrument through an authority's own signed filing. The filing selects permitted limits on recognition and names any counterparties the authority refuses. The instrument determines notice, effective dates, and the consequences of those choices. The publisher records their effects within its assigned role \[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Sections 2.2 and 6\].

In the three-authority example, A and C select full terms while B selects partial terms. B and C refuse each other. The filings produce reciprocal recognition between A and B on partial terms, and between A and C on full terms. They establish no relation between B and C. Joining the same instrument therefore permits this specific pattern of relations \[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Section 2.2\].

Theorem 4.5 proves equivalence with unconstrained bilateral negotiation under five conditions. The finite menu includes the unreserved option and combines limits by the lower class in each subject. Those limits apply reciprocally, and a fixed rule resolves declaration conflicts. Independently verifiable actual receipt opens a period for either authority to refuse the relation without requiring a reason or assent. The instrument establishes the relation by default after that period, while a refusal affects only the named pair.

The behavioral condition requires each filing to express actual willingness that is common across acceptable counterparties. Its refusals must identify exactly the unacceptable counterparties \[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Sections 4.1--4.2\].

The source's twenty-authority case uses one subject and no refusals. Every directed offer has full terms except authority 1's offer to authority 2, which has partial terms. Authority 1 files a conservative common partial cap, and everyone else files full caps. The relation between 1 and 2 remains partial under both methods. Relations between 1 and authorities 3 through 20 become partial under accession, although their bilateral terms would be full. All relations remain, but eighteen of the 190 pairs have weaker terms \[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Section 4.6, "A useful profile beyond (H5)"\].

Proposition 4.7 gives the exact content-gap criterion. Counterparty differences do not always cause a loss, because another authority's limits can already determine the weaker result. Pair-specific declarations can preserve the extra detail at their own information cost. One deposit per authority also leaves notices, updates, exceptions, certificate renewals, migration, and exit work. Proposition 4.9a accounts for these tasks over the same horizon \[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Sections 4.3--4.5\].

## 8 What remains to establish {#sec:limits}

The constructions give explicit conditions for attributed changes, preserved rights, shared allowances, finite completion, and equivalent recognition terms. Their written proofs do not establish a deployed institution's conformity. The authority and continuation paper retains open work on formal mechanization, distributed histories, external effects, legal translation, judgment governance, and information disclosure \[[2](#ref-institutions){style="overflow-wrap:anywhere;hyphens:none"}, Section 10\].

The entity paper leaves the completeness of its institutional vocabulary and the prevalence of required human judgment open. The accession paper requires separate evidence for intermediary legal effect, actual willingness, repeated use, detection, collection, and qualified service capacity. An application must supply those premises for its own authorities, resources, and operating conditions \[[1](#ref-entity){style="overflow-wrap:anywhere;hyphens:none"}, Section 8\]\[[3](#ref-accession){style="overflow-wrap:anywhere;hyphens:none"}, Sections 7.4, 7.8, and 10\].

## 9 Technical reading map {#sec:reading}

For the identity and rights model, read *One Entity in Many Jurisdictions*, Section 2. Its named results cover reuse without widening an act, action-complete admission, quantitative rights, earned claims, and estate-specific funding. Sections 5 and 10 develop recognized evidence and the synthetic collection workload. Section 8 separates written proofs, finite checks, cited mechanization, and open obligations.

For current authority, read *Programmable Institutions*, Sections 3--6. Section 3 defines requests, capabilities, judgment use, dependencies, and observable effects. Section 4 states F1--F10, Proposition 1, Theorem 1, and Corollary 1. Sections 6.1--6.2 specify source coverage and retained evidence. Then read Section 7.5, Theorem 3, for shared allowances, and Section 7.6, Proposition 2, for authority over affected rights. Sections 7.7--7.8 contain Theorems 4--5 and their complete finite environmental contracts.

Section 7.5.1 proves the bounded allocation certificate. It concerns a fixed set of divisible resources and obligations measured in one unit. Its optimality result excludes external performance, settlement, and recovery.

For recognition relations, read *Accession Networks*, Sections 2.2 and 4.1--4.3. Theorem 4.5 states equivalence under H1--H5, and Proposition 4.7 characterizes lost terms. Sections 4.5--4.6 supply lifecycle costs and the twenty-authority example. Proposition 5.5 computes coordinatewise route summaries. Section 6.3 gives their joint evidence requirements and current local decisions. Section 10 records the remaining institutional and empirical obligations.

## References

::: {#ref-entity}
:::

**\[1\]** Raeez Lorgat. *One Entity in Many Jurisdictions*. September 2026.

::: {#ref-institutions}
:::

**\[2\]** Raeez Lorgat. *Programmable Institutions*. September 2026.

::: {#ref-accession}
:::

**\[3\]** Raeez Lorgat. *Accession Networks*. September 2026.
