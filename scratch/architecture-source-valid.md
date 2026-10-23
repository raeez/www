# Part II: The Network Architecture

## Chapter 6: Beyond Geography

### What a Company Must Establish Again

The zones examined in Part I operated within sovereign legal systems. Courts, corporate registries, licensing authorities, regulators, customs services, and enforcement bodies gave their companies a framework for doing business. The quality of those institutions mattered as much as the tax incentives offered at the zone's boundary.

That arrangement leaves work to repeat when a company enters another jurisdiction. The receiving authority needs to establish the company's existence, identify its owners, understand its activities, and decide which permissions apply. Records accepted at home may require translation, certification, updating, or separate verification abroad. A successful company can therefore face substantial administrative costs when it expands.

The problem has three parts. First, the company must assemble services across different legal systems while meeting each system's requirements. Second, the cost of changing those arrangements can weaken the pressure on incumbent service providers to improve. Third, concentrating records and operations in one jurisdiction exposes the company to disruption there. Additional recognition and records elsewhere can support continuity, although physical assets and local rights remain subject to local conditions.

Better administration within one zone reduces its own costs. Recognition across borders requires an agreement with the authority on the other side.

### What a Corridor Is

A **corridor** is an agreement specifying which verifications two jurisdictions will recognize, and for which purposes. One authority might accept another registry's verification of incorporation or a specified identity check. The agreement must define the evidence, the permitted use, the degree of reliance, and the conditions for review or withdrawal.

Recognition can be asymmetric. One side may accept a verification for a narrow purpose while the other accepts a different set of records. Each authority remains responsible for deciding what its law permits. The agreement gives neither party a general right to exercise the other's powers.

What travels is **recognized standing**: evidence of registration, licenses, verified identity, compliance history, or good standing within the agreement's scope. Money and assets continue through the lawful channels and supervised institutions of the jurisdictions involved. A record of a payment instruction remains distinct from evidence that the beneficiary received value.

The agreement can reduce repeated verification. A company may hold recognized standing in several jurisdictions and use services appropriate to each activity. Where those lawful choices are practical, they can increase competitive pressure on incumbent service providers. Its records can also support continuity if one jurisdiction experiences disruption. The effect depends on which records remain available and which authorities continue to recognize them.

Negotiating a corridor requires governments and competent authorities to settle its terms. Software then applies those terms to particular records and requests. The time needed for agreement, integration, verification, and approval must be measured separately. Fast verification does not establish fast admission, licensing, or settlement.

### Shared Records and Local Rules

The architecture uses a shared way to represent the matters that regulated organizations must track. Its five primitives are **entities** (who is acting), **ownership** (who owns what), **Fiscal** (how value is recorded and its movement authorized), **identity** (who is who), and **consent** (who has agreed to what). These categories organize the records; local law determines their legal significance.

A common-law jurisdiction and a civil-law jurisdiction can exchange a record without adopting the same rules. Each may require different documents, ownership restrictions, licensing conditions, or disclosure. Shared representation makes those differences explicit enough for an authority to evaluate the record under its own requirements.

The jurisdiction's deployment runs its approved rules under its authority. A rule change needs an authorized source and an effective date. Exceptions, discretion, and disputed interpretations require a defined decision process. A program must preserve the distinction between a rule it can evaluate and a decision reserved to a regulator, court, provider, or other authorized person.

Network services use these records to support applications across connected jurisdictions, approved instructions, and comparisons of service performance. A claim records an economic right or obligation and the conditions that determine its outcome. Moxie prices and clears claims and is in testnet. Recourse, in research and design, runs dispute resolution and carries outcomes into execution. Carrying outcomes into execution means authenticated transmission to courts, custodians, and providers that hold authority. These roles belong in the architecture of a proposed deployment, with their availability and integration established for its scope. Their reach follows the agreements and permissions in force. A connection alone establishes no universal right to operate.

Authority remains divided by function. Each jurisdiction governs its deployment. Corridor parties govern their agreement. Participants adopt shared technical standards through their own decisions. The proposed research layer in Chapter 9 publishes evidence about performance without admitting or expelling governments.

### Attestations

An **attestation** is a signed, tamper-evident record of an action: who acted, when, under which rule, and with which authority. An incorporation workflow, filing, ownership change, or approval can produce attestations as it proceeds. These records form an evidentiary stream.

Producing the record during execution can reduce the work of reconstructing events later. An auditor can inspect the steps already recorded. A regulator can examine the evidence its permissions allow. A receiving authority can verify a record's origin and integrity before deciding whether to rely on it.

A verified signature links a statement to a signing credential. Its binding to an actor and that actor’s authority requires separate evidence. It does not establish that every external fact in the statement is true. Evidence quality, source authority, current status, and the scope of the assertion remain part of the assessment. Corrections and disputes need linked records so later users can understand what changed.

The same attestation may support several purposes. A supplier payment record can identify the payer and payee, the invoice, the authority for payment, and the recorded outcome. Accounting staff, tax authorities, auditors, banks, and corridor partners each use the portion relevant to their role. Additional evidence may still be necessary for delivery, tax treatment, identity, or receipt.

### Capital Corridors

Portable standing can change the cost of trade and investment. Consider a jurisdiction with capital to invest and a partner whose businesses need financing and market access. Repeated checks of identity, ownership, compliance, and legal standing add expense to each transaction. For smaller deals, those expenses can determine whether the transaction proceeds.

A recognition agreement can let the receiving authority reuse specified checks. A business seeking access to the partner market would still need the permissions required for its activity. Investors would still assess the business and its risks. The corridor reduces repeated institutional work within its agreed scope.

The opportunity should therefore be measured in transactions enabled, costs avoided, time saved, and risks retained. The number of connected jurisdictions alone cannot establish that value. Demand, complementarity, legal recognition, and the quality of the participating services determine whether a corridor is useful.

## Chapter 7: Mass — Running the Legal Entity

### The Continuing Work

A company must be formed and maintain records of its owners. Customer identification and verification depend on its activities and applicable requirements. Those records need updating as circumstances change. It must track applicable rules, authorize decisions, manage money, compute taxes, and retain evidence for inspection. Operating across jurisdictions adds overlapping requirements and additional authorities.

Lawyers, compliance staff, accountants, bankers, and administrators coordinate much of this work. Their expertise is necessary where interpretation or regulated judgment is required. Repeated collection, transfer, and reconciliation of records also consume time that software can reduce.

The design question is how to automate that work while retaining the authority, evidence, and unfinished obligations on which the next action depends.

### The Operating System

Mass is the AI-native operating system that makes legal entities, organizations, and institutions programmable. It runs their approved work end to end: formation, ownership, treasury, identity, consent, and compliance. Autonomous agents execute workflows under human supervision, keep records current, and make permitted state available through APIs.

The economic purpose is to reduce the cost and staffing needed to run a compliant organization. The one-person company is a design target: a founder should be able to direct approved operations through software while using qualified people and licensed providers where their authority is required. Actual savings depend on the work automated, the remaining review, and the costs of integration and operation.

A government can deploy the system for its registry, licensing, and other approved services under its own authority. The deployment must reflect its law, systems, providers, security requirements, and operating responsibilities. Its cost and schedule follow that scope and the agreed implementation plan.

Beneath these operations, a rule layer evaluates encoded requirements and a runtime carries out the admitted work. A workflow may compose documents, prepare filings, request approvals, check the current recorded state, and create attestations. Fixed rules and inputs can produce repeatable evaluations. Legal adequacy still depends on the rules encoded, the evidence supplied, and the authorities that approve or perform the action.

The system must keep unresolved questions visible. An unavailable fact, conflicting record, missing consent, or required discretionary decision cannot silently become permission to proceed. The responsible authority needs the relevant evidence and a clear account of what remains unfinished.

### A Company with Standing in Several Jurisdictions

A **multi-harbored company**, in this design, holds recognized standing in several jurisdictions while coordinating its operations through a common record. It may bank in one jurisdiction, hire in another, and seek recognition of its formation elsewhere. Each activity remains subject to the rules and permissions that govern it.

The system must determine which requirements apply to the proposed action and preserve their sources. Compatible requirements may be checked together. Conflicting laws, territorial limits, or reserved decisions need resolution by the competent authorities. Selecting a supposedly stricter rule is insufficient where the rules concern different powers or impose incompatible duties.

Where a corridor permits reliance on a verification, the company can present that evidence with its history and scope. Where the corridor does not cover the proposed use, the receiving authority applies its own procedure. Recognition can expire, be withdrawn, or require updated evidence.

Identifiable owners and authorized representatives remain central to the design. Agents act for accountable parties under defined permissions. Ownership changes, delegation, revocation, and approval limits must remain available to the people and institutions entitled to inspect them.

### The API

Other products can call approved operations through an application programming interface, or API. A platform whose users need entities formed, verified, and maintained can incorporate those operations into its own service.

Payment APIs illustrate this integration pattern. A developer calls a defined operation while the underlying provider performs the work within its authority. For entity operations, the interface must similarly state its inputs, permissions, result, and remaining obligations. A successful software response must identify whether an action was prepared, submitted, approved, executed, or confirmed by an external provider.

Integration effort depends on the jurisdictions, activities, records, and existing systems involved. It also depends on the provider relationships and legal permissions needed to complete the work. These dependencies belong in the implementation plan and the service agreement.

Each product that uses the interface can bring more company activity into a shared record. That activity can support later corridor use where the necessary recognition exists. Adoption through products complements adoption through governments.

### The Five Primitives in Operation

An **entity** record identifies the actor, its current state, and the authority under which it acts. A special-purpose vehicle for real-estate investment, for example, needs records of formation, ownership, approvals, obligations, and distributions. Its software can coordinate authorized operations while keeping the required legal and provider decisions explicit.

**Ownership** records state who holds the relevant rights. Approved changes update those records and apply the encoded transfer conditions. The legal effect of a transfer depends on the instrument, registry, and law that govern the right.

**Fiscal** records govern authorized payment, escrow, withholding, and distribution instructions. Licensed banks, custodians, and other providers move value under their own obligations. The record must distinguish amounts owed, instructions sent, provider responses, and evidence of receipt.

**Identity** records a verification to a named standard, from a named source, with its date and permitted uses. Another authority can rely on it only within the applicable recognition and privacy rules. Updates and revocations must travel with the evidence needed to evaluate its current status.

**Consent** records who approved which action and under what conditions. A payment might require two named officers above a threshold. A resolution might require a specified majority of eligible, unconflicted directors. The workflow checks the relevant authority and retains the approval evidence.

Together, these records let an organization coordinate its regulated work without losing the distinctions among a decision, an instruction, and its external effect. Those distinctions also determine what the operating evidence in Part III must show.

## Chapter 8: Momentum — Starting an Economy

### The Initial Demand Problem

A new zone needs businesses, services, and workers to arrive together. Companies need banking, payments, professional support, and premises. Service providers need customers. Workers need jobs and the means to live near them. Building facilities before this demand exists can leave a zone with costs and little activity.

Part I shows how established zones worked through that problem by recruiting initial tenants, providing infrastructure, and maintaining political support. The network proposal applies a portfolio method: organize complementary operating businesses before the zone opens, so each can support the others from the start.

Momentum builds the network and organizes the businesses and partnerships needed for this method. The proposed portfolio includes corporate services, banking relationships, payments, workspace, training, and venture support. Its composition should follow local demand and legal requirements. A banking partnership depends on the licensed provider's authority and commitment.

Each portfolio business must have customers, revenue, and a path to viability. Local partners and hiring connect the zone to its surrounding economy. The portfolio's purpose is to establish useful activity and demonstrate that services work, rather than fill an occupancy report with nominal entities.

### Three Agreements to Make Explicit

The commercial architecture separates accession, operation, and access to applications. Each agreement needs its own scope, rights, charges, service levels, and exit provisions.

**Accession** establishes the jurisdiction's deployment and its participation terms. The jurisdiction retains authority over its rules and chooses its corridor relationships. Charges and responsibilities need to be disclosed before it joins.

**Operation** states who runs the system. A government may use a managed service while developing its own capacity. The agreement must assign operational duties, licensed responsibilities, security obligations, data access, service standards, and transition support. Ending a service relationship does not by itself end the obligations already incurred through it.

**The government console and application marketplace** give authorized officials and businesses access to the functions they need. Supervisory access follows the jurisdiction's powers and privacy rules. Applications require defined permissions, accountable providers, and clear terms. Their commercial model must state what work is charged for and how value or usage is measured.

Software also needs a functioning place around it. Buildings, housing, utilities, transport, schools, training, and cultural activity affect whether businesses and workers remain. The lessons of the historical zones require these needs to be treated as part of development planning.

### How Growth Could Sustain Itself

Working infrastructure can attract companies whose activity supports further infrastructure. Early business success can draw founders and skilled workers. Returns can attract capital for the next investment. These relationships can reinforce one another, but they depend on demand and performance.

The network adds a further possibility: a useful corridor extends the markets and services available to participating companies. Its benefit must exceed the costs of negotiation, integration, supervision, and continued operation. Some potential connections will be more valuable than others.

The evidence of sustainable growth is therefore organic activity that persists beyond initial support. New formations, recurring revenue, firm survival, local employment, and use of corridor services all matter. Chapter 10 sets out how to distinguish these observations from proposals and announcements.

## Chapter 9: The Research Layer

### Connecting Research with Practice

Zone development offers many historical cases, but comparison is difficult. Governments choose different locations, incentives, sectors, and measures of success. A growing zone may reflect an effective policy, favorable national conditions, or the characteristics of the companies that chose it.

Shared records could improve the evidence available for research. Attestations can record the elapsed time of an incorporation, the outcome of a check, and the steps required to complete a service. Comparable definitions would let researchers examine differences across jurisdictions. They would still need to assess missing data, selection effects, measurement errors, and changes in context.

### The Proposed Laboratory

The **Laboratory for Incentivization, Coordination and Cooperation**, or LICC, is the proposed research institution in this design. Its proposed role is to turn operating evidence into published findings that jurisdictions can evaluate.

Its research questions follow its name. Incentivization concerns how policies affect investment, formation, employment, and growth. Coordination concerns how authorities agree on standards, corridors, and shared services. Cooperation concerns how parties sustain those arrangements while competing for business.

Variation across jurisdictions may support natural experiments when the design justifies the comparison. A government may also authorize a controlled trial under applicable law and ethics requirements. The research plan needs a stated question, a credible comparison, outcome definitions, and a method for handling confounding factors.

A policy that performs well in one zone becomes a candidate for adoption elsewhere. The receiving jurisdiction must evaluate the law, resources, and conditions on which the result depended. Continued measurement tests whether the result survives that change of context.

### Measurement, Consent, and Publication

The laboratory's authority would be limited to research and publication. It would hold no power to admit, govern, or exclude a jurisdiction. Governments answer to their publics and to the counterparties of their agreements.

Research involving people or businesses requires the applicable permissions, consent, and ethical review. Designs should be registered before outcomes are known. Results, limitations, adverse effects, and unsuccessful tests should be published under agreed privacy and confidentiality rules.

The findings should be public goods. A zone outside the network should be able to learn from a result where publication is permitted. Researchers must distinguish what the data show from causal claims that require further evidence.

An independent record would let the architecture be assessed on its effects. The next part specifies the operating evidence needed for that assessment.
