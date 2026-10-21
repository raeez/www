# Capital as a Compliance Problem

A company raising capital must establish what it can issue, who can receive it, and which approvals and obligations the transaction creates. The capitalization table supplies the quantities and ownership records that those decisions use.

An issuance can activate securities, corporate, tax, and beneficial ownership requirements together. Investor screening and the source of funds add further questions. Each domain applies its own rules to the same transaction.

The useful unit of analysis is therefore the capital event: a particular instrument, action, set of parties, and effective time. A system that understands those fields can identify the required evaluations and preserve their results. Its first task is to make the underlying record exact.

## Start with the quantities

A capitalization table records authorized shares, outstanding shares, reservations, and individual holdings. Its arithmetic must agree at every update. Under a declared reservation convention, authorized shares cover outstanding and reserved quantities. The holdings sum to the outstanding total, and every option grant draws on its designated pool.

An incorrect denominator changes more than a displayed percentage. It can change whether an issuance exceeds the authorized limit or a holding crosses a disclosure threshold. Parallel edits, transcription errors, and inconsistent conversion assumptions can therefore alter a legal determination.

The record should use exact units and declared rounding rules. Integer share counts remain integers. Decimal prices and monetary amounts retain their specified precision throughout entry, calculation, and storage. Fractional ratios need an exact representation or an explicit rounding rule at the point the terms require it. Binary floating-point approximations should never silently determine a legal threshold.

Fully diluted shares also need a stated convention. One convention counts options and warrants at their full exercisable quantity. A convertible note or SAFE, a simple agreement for future equity, needs the conversion terms and inputs that determine its projected share count. A cap-based projection declares that assumption and retains the inputs used to calculate it.

A discount-only instrument before its pricing round may have no fixed share count. The record retains it as a contingent line outside the computed total until the relevant terms and inputs determine that quantity. This keeps a precise total from concealing an unresolved conversion.

These requirements draw on familiar methods. Bookkeeping reconciles quantities across accounts. Event sourcing derives the current position from retained events. The [Open Cap Table Format](https://open-cap-table-coalition.github.io/Open-Cap-Format-OCF/explainers/Architecture/) supplies instrument-specific transactions and structured conversion and vesting terms. The additional task is to connect each event to the institutional decisions it requires.

## Classify the instrument before accepting the action

Common shares, preferred shares, restricted stock, convertible notes, SAFEs, warrants, and options carry different terms. Issuing common shares and issuing a convertible note can activate different ownership, tax, and disclosure questions, even for the same investor.

The system needs a defined set of instrument types. Each type has its own fields, permitted actions, and compliance requirements. An instrument outside that set waits for classification. Accepting it under a default would leave the system without a defined account of which checks apply.

The same discipline governs the security's lifecycle. An active security may be eligible for transfer, subject to its other restrictions. A cancelled security has no active quantity to transfer. An expired option cannot proceed through the ordinary exercise path, and a converted note must retain the event that ended its debt position.

Software can require every operation to handle each defined state. Adding a frozen state then forces an explicit decision in every relevant handler. This verifies that the program covers the states it declares. The handler's decision still needs to implement the governing terms correctly.

Vesting illustrates the difference between terms and a stored result. For a time-based grant, the grant date, cliff, vesting period, and evaluation date determine the vested quantity. A cached percentage must reconcile to that calculation. Event-based vesting also needs the evidence establishing its milestones. An amendment changes the governing terms through an authorized event that the history retains.

## Keep the history and the current position

A transfer log and a current ownership graph answer different questions. The log records events. The graph records the holdings derived from those events.

Suppose an operator records a mistaken transfer. The correction should identify the original entry and state its effect through a typed reversal. An ordinary transfer in the opposite direction would look like new economic activity. Deleting the entry would remove the explanation for the intervening record.

The current graph applies that correction to the positions. The historical log retains both entries, their authority, and their effective times. A rescission or legal unwind likewise appears as a further event with its own basis. A correction to the record and a legal change to ownership require distinct evidence.

This separation matters when checking aggregate behavior. A raw-log cycle search can mistake a transfer and its correction for circular dealing. A current-position graph loses the timing of earlier movements. Ownership thresholds use the relevant position snapshot. Circular-flow analysis needs the timed event history and must recognize corrections as such.

Each effective ownership entry needs an attributable basis. Arithmetic can then derive aggregate holdings from those entries. Control inference involves another question: whether voting arrangements, agreements, or conduct give someone effective control. The evidence and decision rule for that relation must remain distinct from the ownership calculation.

OFAC's 50 Percent Rule provides a concrete example. It treats entities owned 50 percent or more, directly or indirectly in the aggregate, by blocked persons as blocked. Its indirect-ownership examples propagate blocking through entities that meet the threshold. [OFAC FAQ 401](https://ofac.treasury.gov/faqs/401).

On a complete, current ownership record, a calculation can repeatedly add entities whose ownership by the blocked set reaches that threshold. The calculation is exact over its inputs. Identifying the actual owners, applicable sanctions regime, and effective dates remains an evidence task.

A control finding follows a different route. OFAC expressly distinguishes control from ownership under this rule and identifies other grounds on which restrictions can apply. A classifier's inferred control relation supplies a finding for assessment. The responsible authority and applicable rule determine its consequence. [OFAC FAQ 398](https://ofac.treasury.gov/faqs/398).

## Preserve the rights behind the numbers

A percentage alone leaves important rights unspecified. Registered ownership, economic participation, votes, security interests, and rights to proceeds can belong to different people.

Consider 100 identified shares held by R. Suppose B has a contractual right to 40 percent of the residual sale proceeds. C holds priority over the first 10 currency units. On received proceeds of 100, those assumed terms allocate 10 to C, 36 to B, and 54 to R. R retains the shares and votes until an effective act changes those rights.

The example comes from [One Entity in Many Jurisdictions, “Rights, persons, and the action being considered”](https://research.momentum.inc/papers/one-entity-in-many-jurisdictions.html). It shows why the record must name each right's governing instrument, beneficiary, covered assets, quantity basis, priority, and effective period. B's proceeds entitlement supplies neither R's votes nor authority to instruct R's bank account.

Corporate actions must carry those distinctions forward. A stock split changes share units. A merger can replace a holding with shares and cash. The record needs to show how each existing right attaches to the resulting positions under its governing terms. Preserving a specified entitlement is a separate condition from preserving its market value.

A split therefore carries its ratio, record snapshot, effective time, and treatment of fractional positions. A dividend carries amount, currency, eligible positions, payment date, funding route, and rounding rule. An authorized share increase carries per-class changes and the governance act authorizing them. The authorization changes capacity. Subsequent issuances change holdings and activate their own obligations.

[Admissible Obligation Transitions, “Corporate actions”](https://research.momentum.inc/papers/moxie/admissible-obligation-transitions.html) gives the formal action profile. It binds authority, times, affected positions, and exact quantity and obligation changes. A missing curable condition leaves an action awaiting evidence. An invalid action is refused. Neither decision commits the proposed change.

## Map each event to its evaluations

Instrument class and action determine the starting set of compliance questions. The proposed issuance then supplies the parties, amounts, jurisdiction, and other context needed to resolve them.

The following matrix is a representative design profile. A filled circle means the profile evaluates that domain for the event. An open circle means activation depends on the terms or circumstances. A dash means the event adds no separate evaluation in that column under this profile. The governing law and charter determine the actual requirements, thresholds, and exemptions.

| Instrument class | Action | Securities | Governance | Tax | Beneficial ownership | AML | Sanctions |
|---|---|---|---|---|---|---|---|
| Common or preferred shares | Issuance for new money | ● | ● | ● | ● | ● | ● |
| Convertible note or SAFE | Issuance for new money | ● | ● | ● | ○ | ● | ● |
| Warrant | Issuance | ● | ● | ○ | ○ | ○ | ● |
| Restricted stock | Grant | ● | ● | ● | ● | ○ | ● |
| Option | Grant | ● | ● | ○ | ○ | — | ● |
| Option | Exercise | ● | ○ | ● | ● | ● | ● |
| Convertible note or SAFE | Conversion | ● | ● | ● | ● | — | ● |
| Preferred shares | Conversion into common | ● | ○ | ○ | ● | — | ● |
| Shares, any class | Secondary transfer | ● | ○ | ● | ● | ● | ● |
| Shares, any class | Repurchase | ● | ● | ● | ● | ● | ● |
| None | Authorized shares increase | ○ | ● | ○ | — | — | — |

AML means anti-money-laundering review. The dashes in that column assume the event itself moves no funds and preserves the diligence attached to the earlier funding event. Additional funds or changed circumstances can require another review.

A restricted stock grant and an option grant illustrate the value of the classification. The restricted stock creates an outstanding holding at grant. An option creates a right to acquire shares under its terms. Their tax and ownership questions therefore arise at different points. For qualifying restricted property, the United States section 83(b) election has a deadline of 30 days after transfer. That event date belongs in the record. [IRS Revenue Procedure 2012-29](https://www.irs.gov/irb/2012-28_IRB#RP-2012-29).

The same distinction separates shares issued for new money from a convertible note. The note's present rights and its future equity interest require different entries. Conversion then activates a new set of questions.

Every row naming a counterparty activates at least five domains in this example, outright or conditionally. The matrix makes those dependencies visible before the transaction reaches an approval or execution boundary.

## Approval, execution, and recording

Each required domain produces an attributable determination. Compliant, non-compliant, pending, exempt, and not applicable retain different meanings. Together, the records show which requirements applied, which decisions satisfied them, and what remains outstanding.

The action can proceed only when its current required conditions permit it. [One Entity in Many Jurisdictions](https://research.momentum.inc/papers/one-entity-in-many-jurisdictions.html) binds that question to the exact action and complete requirement set. Permission to hold a security does not automatically authorize its offer, pledge, transfer, or distribution of proceeds.

Some defects have a defined route to cure. Delaware law, for example, provides procedures for ratifying certain defective corporate acts and validating stock. Those procedures have their own resolutions, voting, notice, and filing requirements. The availability of ratification supplies a remedy for the specified defect. It gives a proposed act no advance exemption from its required authorization. [Delaware General Corporation Law §204](https://delcode.delaware.gov/title8/c001/sc06/#204).

Other remediation can involve a rescission process, a late filing, or an amended tax return, under the applicable rules. The record must identify the remedy, its authority, and when it takes effect. The existence of a possible remedy cannot stand in for a satisfied condition.

Sanctions evaluation must resolve applicable licenses and exemptions before deciding whether the action can proceed. A prohibited action remains blocked at execution. OFAC can impose civil penalties under a strict-liability standard, including where the person lacked knowledge of the prohibition. This makes accurate applicability, evidence, and current-use checks consequential. [OFAC's account of its liability standard](https://ofac.treasury.gov/media/936221/download?inline=).

The remedy can also depend on the authority. Under 31 C.F.R. §594.202, covered prohibited transfers of blocked property are null and void. The provision permits validation through the specified license or authorization. Its separate protection for a qualifying holder requires findings about conduct and knowledge, together with a prompt report. A report alone establishes neither of the other conditions. [31 C.F.R. §594.202(a), (c), and (d)](https://www.govinfo.gov/content/pkg/CFR-2025-title31-vol3/pdf/CFR-2025-title31-vol3-sec594-202.pdf).

Execution also needs current authority when the institution or provider acts. An approval recorded earlier retains its historical meaning after a relevant revocation. It authorizes a later action only to the extent the governing authority makes it sufficient for that use. [Op](https://research.momentum.inc/papers/op.html) supplies the execution model for these checks and external outcomes.

Recording an event that already took legal effect is a distinct operation. The register needs the effective event, its authoritative evidence, and the time of recording. A reporting or recordkeeping defect can remain visible alongside that event. This distinction allows an accurate history while keeping the permission to initiate a new transaction subject to its own conditions.

The same separation applies to dividends and redemptions. A declaration establishes the declared obligation. A payment instruction records an instruction. Provider evidence establishes the reported performance, while beneficiary receipt requires the relevant evidence of receipt. A partial payment leaves the remaining obligation in the record. Refusal or expiry of an execution request does not itself discharge that obligation.

## Apply the same discipline to a fund

A fund subscription changes the governing instruments and rules, but the record still needs exact quantities, classified actions, and attributable decisions. A capital call creates a payment obligation with its own terms and status.

The administration can use three related state machines. The fundraiser moves from draft to active to closed. An investment tracks pending payment, partial payment, payment, refund, or rejection. A capital call tracks issue, partial payment, payment, or cancellation.

Each level needs its own transition rules and conserved amounts. A partially paid call preserves both the amount received and the amount still due. A refund records a further payment and its effect on the investment under the governing terms. Closing the fundraiser leaves the records needed to administer outstanding duties.

When a new instrument type arrives, the operator must define its fields, lifecycle, and activation rows before accepting its first action. If custody must begin earlier, the unresolved classification needs an explicit suspended process under the responsible person's authority. A default class would conceal the missing decision.

The capital record then gives an investor or examiner a usable account of the transaction. It identifies the quantities before and after it, the rights affected, the approvals, and the resulting obligations. Exact accounting and complete history make those determinations checkable. Their legal correctness continues to depend on the governing rules, authoritative acts, and evidence the record identifies.
