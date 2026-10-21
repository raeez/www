# Capital as a Compliance Problem

**Raeez Lorgat, 2026**

---

**Abstract.** A capital event, such as a share issuance, transfer, or conversion, triggers evaluations in several independent regulatory domains at once. Those evaluations are only as trustworthy as the record they read. This note states the record-keeping requirements and their prior art. It supplies the missing map from instrument class and corporate action to domains and explains how those domains differ in force.

A company issuing shares creates new shares, allocates them to investors, and updates its capitalization table. With spreadsheets and paper stock certificates, someone enters numbers in a row and someone else signs a document to record the change.

The issuance also triggers obligations in several independent regulatory domains at once. The spreadsheet cannot record those simultaneous obligations.

Securities law governs registration or exemption, required disclosures, and investor accreditation. Corporate law governs board approval, the availability of authorized shares, and compliance with the corporate charter. Tax law governs the treatment of the issuer and investor, including any withholding obligation. Beneficial ownership law governs disclosure thresholds and new reporting obligations arising from the issuance.

Each domain has its own regulator, timeline, enforcement mechanism, and definition of a violation. The securities regulator does not care whether the board approved the issuance (that is the corporate law regulator's concern). The tax authority does not care whether the securities exemption was properly claimed (that is the securities regulator's concern). Each domain evaluates the same event independently and simultaneously.

Capital formation is therefore a compliance problem. Issuing shares, transferring ownership, or exercising options triggers an evaluation across multiple independent domains.

The record-keeping requirements draw on prior art. The Open Cap Table Format (Open Cap Table Coalition, 2021) specifies typed share classes and typed transaction objects for issuance, transfer, and cancellation. It also specifies vesting computed from schedule terms. Event-sourced ledgers keep an append-only log and express corrections as new entries. Double-entry bookkeeping has enforced conservation across accounts for five centuries.

These record-keeping requirements come first because every evaluation reads the record they constrain. The note then supplies the missing activation map: which domains an event activates, given its instrument class and corporate action. It also explains how those domains differ in force.

## The conservation system

Compliance evaluation requires a correct capitalization table.

A capitalization table is a conservation system. Shares are created (authorized), allocated (issued), held (outstanding), and sometimes destroyed (cancelled). Outstanding shares cannot exceed authorized shares, and the sum held by all shareholders must equal total outstanding shares. Options pools must account for every grant. These constraints must hold at every point in time.

Spreadsheets make these arithmetic invariants easy to violate. Binary floating-point arithmetic represents whole-number share counts exactly but approximates ownership percentages, per-share prices, and conversion ratios. Those approximations compound down a column. Manual data entry introduces transcription errors, while parallel updates by different people create conflicting versions. Ownership percentages can then fail to sum to 100%, outstanding shares can exceed authorized shares, and individual holdings can disagree with the total.

These inconsistencies make legal determinations unreliable or legally wrong. An erroneous total can affect whether an issuance stays within the authorized limit or a transfer crosses an ownership disclosure threshold.

The ledger must therefore check conservation constraints at every write. Share counts and monetary amounts use exact decimals, with no binary floating point on the path from entry to record. Authorized shares must equal or exceed outstanding plus reserved shares, and shareholders' holdings must sum to outstanding shares. Fully diluted shares equal outstanding shares plus everything convertible into shares, counted under a convention that forms part of the invariant.

Under that convention, options and warrants count at the full number of shares they can be exercised into. A convertible instrument counts at the share count its terms fix on the date of the write. A capped convertible note or SAFE (a simple agreement for future equity) converts at its cap.

An instrument with neither a cap nor a price has no share count yet. This includes a discount-only note or SAFE before the round that prices it. The record carries it as a declared contingent line, excluded from the total until a priced round fixes its share count. This convention makes the equality computable and exact at every write.

## The share class taxonomy

A corporation may have common shares, preferred shares, restricted stock, convertible notes and SAFEs, warrants, and options. Each type carries distinct legal characteristics that determine which compliance domains activate during issuance, transfer, and conversion.

Issuing common shares to an accredited investor differs from issuing convertible notes to a retail investor in securities analysis, tax treatment, and disclosure obligations. Corporate law requirements may also differ, depending on the charter. A single "issue shares" operation that treats every class as common stock will evaluate other classes incorrectly wherever their requirements differ.

The taxonomy must therefore be closed: a fixed set of known types, each with defined compliance characteristics. At its boundary, the system rejects an instrument that matches no type. Class and action together determine which domains evaluate the event, so an unclassified instrument has no defined evaluation. The system must refuse it.

For an accepted share issuance, the system matches the share class against the taxonomy and activates the corresponding compliance domains. Exhaustive matching covers every type in the closed set, while boundary rejection keeps other types out of the record. An unanticipated type therefore cannot silently skip evaluation.

## The security lifecycle

Individual securities are the specific instruments held by specific shareholders. Each progresses through a typed lifecycle: a closed set of states that determines which operations it permits.

An active security permits transfer, while a cancelled security prohibits it. An expired option cannot be exercised, and a converted note no longer exists as debt. The type system enforces these constraints through a closed enumeration of security states. Every operation that touches a security must pattern-match on its status and handle every variant.

Adding a status such as "frozen" for securities subject to a regulatory hold forces an explicit decision at every handler. Code that omits the new status no longer compiles. This checks totality, not correctness. A handler can still decide wrongly, but it cannot silently fail to decide or ignore a state it does not understand.

A vesting schedule is a deterministic function of the grant date, cliff, vesting period, and current date. Those terms determine the fraction vested and are the source of truth. A stored vested amount is a projection. Every read and write must reconcile it against the schedule, whose computed value governs the reconciliation. A mutable "percent vested" field that someone updates periodically without reconciliation allows the cap table to drift.

## The transfer log and the ownership graph

Ownership requires both a history of transfers and a record of current holdings.

The transfer log is an append-only record of transfer events between entities: persons and institutions. Every transfer produces an immutable entry. To correct a mistaken transfer, the system appends a typed reversal entry that references the original. It cannot delete the original or use an ordinary opposite transfer, which would be indistinguishable from new economic activity. The log only grows.

In corporate law, a share transfer that occurred remains a fact even if it is later rescinded, voided, or reversed. The rescission is a further legal event. The log records both events and erases neither.

The log determines a directed graph of net positions, where nodes are entities and edges are current economic interest. A mistaken transfer and its typed reversal cancel in this graph, which therefore shows current holdings. Aggregate analysis runs on the graph. Beneficial ownership analysis checks positions against disclosure thresholds, and control-chain analysis checks whether a path of holdings concentrates effective control in one hand. Sanctions analysis sums the interest that blocked persons hold in each node along attested holdings. Circular-flow analysis checks whether interests cycle back to their source.

Cycle detection on the raw log would treat every corrected mistake as a circular flow. An audit of the netted graph would lose the history. Keeping the objects separate gives audits the full log and aggregate analysis the current graph. Typed reversals preserve corrections in the log while making them neutral in the graph.

Each log entry is attested: someone with authority recorded the transfer and answers for it. Graph analyses differ in what they add to those entries. Aggregate ownership uses arithmetic alone to sum interests along attested holdings. For blocked persons, sanctions law makes that sum an operative fact. Blocked persons are persons whose property a sanctions regime has frozen, beginning with those it lists by name.

Under the United States rule, ownership by blocked persons of fifty percent or more makes an entity a blocked person, even if it is unlisted. The rule covers direct and indirect ownership, held individually or in the aggregate (31 C.F.R. § 594.412 codifies the rule for one program; the Office of Foreign Assets Control's revised guidance of 13 August 2014 applies it across programs).

The blocked set is computed, not attested, and the computation is exact over the attested holdings. It starts with the listed persons and adds every entity in which the set so far holds an aggregate interest at the threshold. It repeats this step until nothing is added. Membership establishes sanctions applicability with the full force of the underlying attested entries, after which the fail-closed evaluation described below applies.

Control chains and concerted action require a different analysis. These inferred relations have neither an attestation nor an arithmetic derivation, and the ownership rule above does not establish control. Such a finding is a classifier's output with a classifier's error rate. It raises a flag for evaluation and cannot block the write by itself. A block is warranted by an attested fact or by arithmetic over attested facts where the law gives the result the status of fact. No authority has attested the inferred relation.

## Corporate actions as state transitions

A stock split, name change, authorized shares increase, dividend declaration, board change, or dissolution is a corporate action. These actions are the most complex mutations a capitalization table can undergo because of the compliance domains they affect.

Their mechanics are arithmetic: a stock split multiplies share counts by a ratio, and a dividend distributes a fixed amount per share. Each action also carries compliance obligations.

An authorized shares increase requires board approval (corporate governance), and shareholders may need to ratify it (corporate law). It may trigger securities registration requirements if the new shares will be offered publicly (securities law). It may also affect the entity's tax status if it changes the capital structure (tax law). The increase itself changes no holdings, so beneficial ownership analysis follows with each issuance it enables. The authorization thus has its own obligations and enables issuances with further obligations.

Representing an authorized shares increase as "update a number in the cap table" omits most of these obligations. A typed state transition can carry the new total, per-share-class changes, voting rights implications, and a link to the authorizing governance decision. These fields let the system activate the correct compliance domains for each aspect of the action.

The representation must therefore be a discriminated union: a closed set of action types, each carrying exactly the fields relevant to that type. A split carries its ratio and record date, while a dividend carries amount, currency, and record date. An authorized shares change carries per-class deltas and the new total. The action type determines which fields exist and what they mean. Together with the instrument class, it determines which compliance domains activate. The system refuses action types outside this set, as it refuses instrument classes outside the taxonomy.

## The multi-domain evaluation

The instrument class and action now determine the domains to evaluate.

A submitted share issuance requires checks across every applicable domain. The four opening domains cover securities registration or exemption, corporate governance authorization, tax treatment, and beneficial ownership thresholds. Further checks cover anti-money-laundering screening of the funds, sanctions verification of the parties, and any additional domains required by the entity's home jurisdiction.

Each domain produces its own determination: compliant, non-compliant, pending, exempt, or not applicable. Together, the determinations form a compliance vector with one entry per domain. The entity's compliance passport is an append-only record of every evaluation it has undergone. This vector supplies the passport row for the action.

The activation map below indexes these checks by instrument class and action. Each row pairs one action with the class or classes it names from the taxonomy. Grouping rows by action permits comparison across classes. Where a row names two classes or reads "shares, any class", changing class leaves the domain set unchanged for that action. The authorized shares increase names no class because it touches no instrument.

The map states the pattern of activation and is representative rather than statutory. Every threshold, exemption, and condition inside a cell is a jurisdiction parameter. A filled circle marks a domain the event always activates, and an open circle marks conditional activation. Conditions depend on the charter, regime, consideration given, or whether an offering follows. A dash marks a domain the event does not itself activate. In the anti-money-laundering column, it marks an event with no movement of funds, since diligence attached to any earlier event that moved the money.

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

The map shows three properties. First, changing the instrument class while fixing the action can change the domain set. A restricted stock grant and an option grant are the same act under the same equity plan. Restricted stock is outstanding from the day of grant, so tax evaluates then and the shares immediately count toward ownership thresholds. Under the United States rule, the holder's election to be taxed on the grant-date value falls due thirty days after grant. An option grant activates both domains only conditionally.

The same distinction applies to issuing shares or a convertible note for new money. The note carries no present ownership, so beneficial ownership activates conditionally until conversion. Second, every event naming a counterparty activates at least five domains, outright or conditionally. Multi-domain evaluation is therefore the normal condition of capital events. Third, every row with a counterparty activates sanctions, the only fail-closed column.

Sanctions is fail-closed once applicability is resolved. Applicability comes from the party's presence on a list or the aggregate interest that blocked persons hold in it. The ownership graph computes that interest from attested holdings and can establish that an unlisted party is blocked by operation of law. Licenses, humanitarian carveouts, and sovereign exemptions enter the sanctions evaluation before it returns a verdict. If that verdict finds an issuance's beneficiary non-compliant, the issuance cannot proceed, regardless of every other entry in the vector.

Every other domain in the vector leaves the cure in the parties' hands. A defective corporate act is ratified (Delaware General Corporation Law § 204), and an unregistered offering is remedied by a rescission offer. A missed ownership filing is made late, and a tax position is amended. Sanctions violations require relief from the authority. Under United States law, civil liability for a prohibited transaction attaches without regard to knowledge or intent (50 U.S.C. § 1705(b) carries no such element; § 1705(c) reserves willfulness for the criminal penalty). A transfer of blocked property in violation of the regulations is null and void from the moment it occurs.

Only the authority can relieve that consequence afterward, by license or on an innocent holder's prompt report. The parties cannot (31 C.F.R. § 594.202(a), (c), and (d), stated for one program and carried by each). Later disclosure mitigates the penalty but does not undo the violation. Liability attaches without intent, and the parties cannot cure a completed violation themselves. The domain must therefore be satisfied before the write. This is the meaning of fail-closed here.

The full multi-domain verdict binds when the action becomes binding. The governance decision authorizing an issuance must carry that verdict, and authorization requires it. The subsequent record write runs under the one fail-closed check, sanctions, and appends its audit entry in the same transaction. The audit trail thus links every record to its authorizing verdict.

An issuance that passes evaluation today might fail tomorrow if the entity's tax status changes. An issuance that fails today might succeed after the entity remediates the deficiency. Both outcomes correctly reflect compliance at the moment of authorization.

## The fund administration dimension

Fund administration applies the same structure under different rules.

A company raising capital through a SAFE faces securities compliance on the terms and tax compliance on the investment structure. Corporate governance rules govern its authority to accept investment, while beneficial ownership rules govern the resulting ownership changes. A fund raising capital through a subscription agreement for limited partnership interests faces the same domains with different requirements. A capital call to its limited partners triggers payment obligations with their own compliance requirements.

The fundraiser, investment, and capital call form a three-level hierarchy of typed state machines. The fundraiser runs from draft through active to closed. Within it, an investment has the payment lifecycle pending, partially paid, paid, refunded, rejected. A capital call inside the investment is issued, then partially paid, paid, or cancelled. Each level has its own invariants, transition rules, and compliance domains.

All three levels use typed enumerations for states, exhaustive matching for transitions, and conservation invariants for amounts. Every state change receives multi-domain evaluation. Fund administration therefore applies the same requirements to nested economic states: conservation laws, typed transitions, and multi-domain compliance.

## Forward compatibility

The taxonomy of share classes, security types, corporate actions, and investment types will grow. Legislatures will create instrument types, regulators will define categories, and markets will invent structures.

Accepting a new type requires an extension to the taxonomy. Before accepting its first instrument, the system must define the type's compliance characteristics, state its lifecycle, and complete its activation rows for each permitted action. If custody is required before classification, the system must suspend the operation until a person with authority classifies the instrument. It can never proceed under a default. Class and action determine domain activation, so an unclassified instrument has no defined evaluation to pass.

New instrument types therefore wait for classification. This ensures that every recorded instrument has a class with activation rows, and evaluation is total over everything the system holds.

## Why the capital record must be exact before it is evaluated

A share issuance touches securities law, corporate law, tax law, and beneficial ownership law simultaneously. A fund investment touches those domains and the regime governing the fund structure. The activation map arranges them in a matrix across classes and events. Every filled cell requires an evaluation against the record.

A capital formation event triggers multi-domain evaluation and updates the conservation system. It also appends to the transfer log, changes the derived ownership graph, and produces immutable audit records. Each operation depends on the recorded row. Conservation constraints, share classes, and security lifecycles make that row suitable for evaluation. The transfer log and graph, corporate action union, and fund hierarchy supply its history, relationships, and permitted transitions. With these foundations, evaluation produces determinations that are correct when made and checkable afterward by anyone who follows the audit trail.

## Limitations

This note specifies the record and activation map. It does not supply any domain's rules. Rule encodings determine what counts as an exempt offering or taxable event, and those rules vary by jurisdiction. The map is representative, not statutory: jurisdictions can attach further domains, and conditional cells resolve differently under different charters, regimes, and forms of consideration.

On the derived ownership graph, aggregate-ownership arithmetic is exact over the attested entries and establishes applicability for the fail-closed sanctions evaluation. Inferred control chains and concerted action carry an error rate. They produce flags for evaluation, not verdicts.

The guarantees are conservation checked at every write, total handling over closed taxonomies, refusal of the unclassified, and an append-only history. An exact record makes correct evaluation possible. Correctness of any particular rule encoding remains a separate obligation.
