# Part II: The Network Architecture

*(Replaces WIP 0.06 Part II, "The Network State Evolution," chapters 6–9 in full.)*

---

## Chapter 6: Beyond Geography

### One Jurisdiction for Every Service

Every zone examined in Part I — Shannon, Singapore, Shenzhen, Dubai, Mauritius — operated within a single sovereign jurisdiction. That jurisdiction supplied its courts, corporate registry, licensing, regulation, customs, and enforcement. The prevailing assumption was that a company must exist under one legal system and answer to one set of authorities. Indivisible sovereignty appeared to require a single provider for all these services.

Part I identified three costs of this arrangement.

A company must choose one bundle. It weighs Singapore's courts against Dubai's logistics and accepts the weaknesses of its preferred jurisdiction, because it cannot combine their strengths. Repeated across the world economy, these compromises create a large, persistent loss that remains unmeasured.

The arrangement also weakens competitive pressure. Singapore had to compete for companies choosing where to locate. Once those companies had incorporated, hired, opened bank accounts, and established compliance histories, leaving would cost them years and substantial sums. That cost gives an incumbent jurisdiction less reason to improve. Singapore's own planners recognize the risk: Part I described their concern that success could produce complacency.

It concentrates risk in one government. When Ethiopia collapsed into civil war in 2020, the companies in its industrial parks lost everything, including the records proving their existence and years of compliant operation. Their institutional records depended on registries within the same failing jurisdiction.

Even Shannon and Singapore faced these limits. Better administration within a zone could not make its companies' standing and verified history portable across borders. That requires an agreement with another jurisdiction.

### What a Corridor Is

A **corridor** is a bilateral agreement specifying which of two jurisdictions' verifications each will recognize, and at what grade. A government may accept the other registry's verification of incorporation, or its authorities' verification of owners' identities, for named uses. Each side negotiates its recognition separately, so the agreement is asymmetric by design. It is a treaty-grade act, revocable on its terms and subject to the time governments need to negotiate.

What crosses a corridor is **recognized standing**: registration, licences, verified identity, compliance history, good standing. Money and assets continue to move through each jurisdiction's own lawful channels, supervised by each jurisdiction's own authorities. The corridor makes that proof portable across jurisdictions.

This agreement changes each of the three costs. A company can combine recognized standing in several jurisdictions: Singapore's courts, for example, with another jurisdiction's market access. Its credible alternatives make jurisdictions compete on measured service quality. If it holds standing in three jurisdictions, that standing remains provable in two when the third fails.

Building a corridor takes months or years of sovereign negotiation and depends on trust between governments. Once the agreement exists, the company brings its proof to the receiving jurisdiction for verification at machine speed. The network therefore grows at the pace of diplomacy, while verification operates at the pace of computation. Borders remain in force, and capital moves through the lawful channels described above.

### The Layered Architecture

For corridors to carry standing, the jurisdictions on each end need a common substrate — a shared way of representing the five things every regulated economy must track. The layers standardize the records needed for recognition while preserving each jurisdiction's control over its rules.

The base layer holds five primitives, the irreducible elements of economic life that every jurisdiction on earth must handle: **entities** (who is acting), **ownership** (who owns what), **fiscal instruments** (how value is held and moved), **identity** (who is who), and **consent** (who has agreed to what). A common-law island and a civil-law republic must both answer these questions, despite differences in law, politics, and development. Standardizing the representation lets them exchange answers while each retains authority over the answers it requires. Electronic mail illustrates this design: a shared format carries messages across borders while leaving their content to the parties.

In the jurisdiction layer, each government writes its tax treatment, licensing regimes, ownership restrictions, and disclosure requirements. These rules execute on its own deployment under its own authority. Two jurisdictions on the common substrate can be as different as Singapore and Mauritius are today. The common representation makes their rules legible for corridor recognition when, and only when, both governments choose it. Their laws remain distinct.

The network layer supplies the services that exist only because the nodes can interoperate: applications that reach several jurisdictions at once, settlement of obligations across corridor pairs, the publication of service-level performance that lets companies compare jurisdictions on evidence.

Authority follows the same divisions. Each jurisdiction governs its own node, the two corridor parties govern their agreement, and shared standards evolve through adoption. No central authority admits, ranks, or expels governments. Chapter 9 examines how measurement and transparency can support quality through sovereign choice and mutual accountability, the basis on which sovereigns have sustained such arrangements.

### The Attestation

Every action on the substrate produces an **attestation**: a signed, tamper-evident record of who did what, when, under which rule, and with which authority. Incorporations, filings, payments, ownership changes, and approvals therefore produce a continuous evidentiary record.

Accountants, auditors, and examiners traditionally reconstruct a company's actions from documents, samples, and interviews, at costly quarterly or annual reviews. On the substrate, each action produces its evidence as it executes. Regulators can examine existing records, and the same verifiable attestation can serve several readers: a tax authority, auditor, bank, and regulator across a corridor. Each receives what its own rules require.

The following chapters explain who produces these records, how zones begin operating, and how a research programme can use the resulting evidence.

### Capital Corridors

Portable standing also changes which investments are economic. Capital follows through lawful channels and ordinary commercial decisions.

Consider a capital-rich jurisdiction with a small home market and a population-rich jurisdiction with scarce capital. Part IV develops a specific example. Despite their complementarity, every transaction must establish identity, compliance, and legal standing again. A mid-market cross-border structuring routinely costs hundreds of thousands of dollars and the better part of half a year, preventing all but the largest deals.

A corridor lets the receiving jurisdiction reuse that verification. The hub's companies can sell, get licensed, and get paid in the partner market without re-incorporating from scratch. The partner's enterprises can demonstrate standing to the hub's investors at the standard its regulators recognize. Trade that was uneconomic becomes routine, and investors can decide on its commercial merits.

The opportunity is the large volume of trade and investment that current verification costs prevent.

---

## Chapter 7: Mass — The AI-Native Operating System

### The Work, Done by Hand

A company must be formed, identify its owners and customers, and verify new owners as they change. It must track amendments to law, move money lawfully, and compute taxes across its activities. Its decisions need authorization, records, and evidence a regulator can inspect on demand.

Lawyers, compliance staff, accountants, and bankers currently do this work by hand in each jurisdiction. Their scarce expertise makes it slow and expensive. A mid-market cross-border structuring costs hundreds of thousands of dollars in counsel and intermediary fees and takes four to six months. For most prospective participants, that cost prevents the transaction. National statistics omit the lawful, productive activity that willing counterparties abandon because its regulatory work costs more than the deal.

### What Mass Is

**Mass is the AI-native operating system for the regulated life of a company.** It creates a legal entity and then runs it: formation, identity and know-your-customer verification, compliance, treasury, tax, governance, audit — continuously, with autonomous agents executing the regulated work and people supervising it, across many jurisdictions at once. Deployed by a government, the same system runs the regulated life of the jurisdiction itself: its registry, its licensing, its regulatory supervision. The same operations support individual companies and the jurisdiction that regulates them.

Formation is widely available as a service. Keeping a company lawful requires continuing work: beneficial-ownership re-verification on rolling thirty-, sixty-, and ninety-day cycles; the tax position recomputed as transactions flow; every regulatory amendment read, interpreted, and integrated the month it lands; audit evidence assembled at year-end from records scattered across a dozen systems; and, for a company operating in several countries, all of it reconciled across every jurisdiction it touches. Mass runs these operations continuously. A rule change triggers recomputation, each jurisdiction's tax position stays current, and attestations provide the audit evidence. The system executes the work under human supervision.

Underneath, the system pairs a rule layer with a runtime. The rule layer encodes a jurisdiction's law so that each rule has one precise, machine-checkable meaning: the same action, evaluated twice, returns the same lawful-or-refused answer, and an agent cannot take an action the law has not admitted. The runtime executes the work — composes the documents, advances the filings, validates each step against the live regulatory state, and writes the attestation as it goes. **Compliance becomes a property of execution:** the system refuses an unlawful action before it occurs.

### The Multi-Harbored Company

This construction makes possible a new form of company: one coherent entity present in several jurisdictions at once.

Today, a company "in" three countries is three separate legal lives, three compliance calendars, three sets of advisors, and three versions of the truth, reconciled by hand and out of date the moment the reconciliation finishes. On Mass, the entity holds standing in each jurisdiction it harbors in, and the system works out, automatically, the strictest applicable rule across all of them for anything it does — so that the company's every action is lawful everywhere it lives, by construction. Its banking can sit where banking is best, its hiring where the talent is, its incorporation where the courts are strongest, and its conduct meets the highest bar its jurisdictions collectively set. Where two of its jurisdictions share a corridor, its standing crosses between them with the grade of recognition the two governments agreed.

Every entity on the substrate has identifiable, verified human owners. Agents act on behalf of these accountable owners at machine speed under continuous verification. The architecture enforces ownership transparency, making the same records useful to regulators and honest businesses.

### The API

Other products can call these operations through an application programming interface (API) that a developer integrates in weeks.

Stripe illustrates this route to adoption. It made payment acceptance available through a few lines of code, replacing slow integration through bank relationships. Other products could then accept payments without arranging merchant accounts themselves. Mass offers the same integration pattern for forming, verifying, and maintaining entities across borders. A financial platform serving customers across three jurisdictions can integrate these operations in weeks, replacing a multi-year build and permanent compliance staff. Its software calls for formation, verification, and continuous compliance as it would call for a payment or a map.

Each product that embeds the interface brings its users' entities onto the substrate. Those entities can later use corridors, extending the network's growth beyond direct government deployments.

### What It Does to the Cost

For a company: the regulated work that consumed a department runs as supervision of a system. A function of hundreds operates as a team on the order of ten, because the system executes and the people oversee. At single-person scale, a sole founder uses autonomous agents to operate a lawful, compliant company across jurisdictions. That founder is the formation flow's design target. Small, software-intensive firms are the fastest-growing category of new business, and their compliance overhead has restricted what they can do.

For a government: a sovereign deployment of Mass stands up in **under 90 days, for under $10 million** — against the $50 million to $500 million and the years of civil works that a conventional zone build has historically demanded, with the country's existing registries and laws as the starting configuration. The deploying jurisdiction receives a sovereign-exclusive, perpetual operational licence to the system on its territory, with the authority to operate and maintain its own rule-sets; the licence is paid for out of the operating savings the automation produces in the public administration and the corporate-services overhead it absorbs. The government owns the deployment entirely, as it owns its registry today.

### The Five Primitives in Practice

The five primitives in Chapter 6 govern distinct parts of these operations.

An **entity** on Mass holds its own current state, executes its own governance, and can prove its own existence and standing to anyone entitled to ask. For example, a special-purpose vehicle for a real-estate position starts with a full, maintained compliance state. Executable rules govern its acceptance of investment, distribution of returns, and continuous reporting, making it a durable, supervised instrument.

**Ownership** is current at every moment: the register of who owns what is the operating record itself, updated by the same actions that change it, with transfer restrictions that enforce themselves because they are part of the rule layer.

**Fiscal instruments** govern payment, escrow, withholding, and distribution as authorized operations that produce evidence during execution. Value always moves through the lawful channels and supervised institutions of each jurisdiction involved.

**Identity** is verified once to a named standard and then *carried*: a person or company proven in one context holds that proof for every context entitled to rely on it, with the system disclosing to each party exactly what that party's rules require and no more.

**Consent** makes board approvals, shareholder votes, and authorization thresholds executable rules. A payment above a specified amount requires two named officers; a resolution requires the specified majority. Execution enforces the rule and records an attestation that remains provable years later.

These records support the multi-harbored company and corridor verification. Running them as continuous operations supplies the technical basis for the operating model examined in Part III.

---

## Chapter 8: Momentum — Building Living Economies

### The Cold Start

Momentum is a company that builds and operates special economic zones. Mass is the operating system it builds them with. The operating system still needs businesses and services to make a zone viable.

Every new zone faces the problem every new marketplace faces: it starts empty, and emptiness is self-perpetuating. Companies stay away because there are no services; services stay away because there are no companies; workers stay away because there are no jobs; and the zone loses credibility and money while its political sponsors wait for results. Part I showed this pattern killing zones on three continents — and showed that even the successes spent their first years in the same trap. Shannon had four companies after two years. Jurong was "Goh's Folly" for half a decade. JAFZA opened to nineteen tenants in three years. The great zones survived the cold start through extraordinary patience that most governments cannot politically afford.

Momentum launches each zone with a portfolio of operating companies built for the purpose — corporate services, banking partnerships, payments, workspace, training, venture support — so that the zone opens with tenants, employment, transactions, and revenue on day one. Amazon initially stocked its own shelves, and ride platforms recruited and paid their first drivers. A new zone similarly needs an initial supply of services and demand for them.

The portfolio companies must survive on their own revenues in real markets. Local partnerships and hiring are requirements from the start: Part I showed how zones failed when their developers neglected the surrounding economy.

The portfolio companies also demonstrate the new jurisdiction's systems to prospective tenants from the first week: incorporations in minutes, accounts in hours, payments in seconds, and continuous compliance.

### The Three Layers of the Commercial Architecture

The relationship between a zone and the network has three layers, and each is a distinct agreement with a distinct logic.

**Layer one: accession.** The jurisdiction deploys its sovereign node — its own instance of the operating system, on its own territory, under its own law — and establishes its first corridors. The commercial terms of the protocol are disclosed in the accession agreement itself, in advance: the jurisdiction knows exactly what the network charges and for what, before it joins. These disclosed terms give sovereign participants a basis for continued cooperation.

**Layer two: operation.** Momentum operates the node as a managed service for jurisdictions that want operating capability without building a technical organization first. The government holds the licence and the authority; Momentum runs the machinery to the service levels the agreement names. Jurisdictions can end the managed service on their own schedule as they build the capacity to operate the system themselves.

**Layer three: the government console and the agent store.** The government receives real-time regulatory visibility through access to attestations under its own supervisory rules. And the zone's companies receive access to the marketplace of agents and applications that automate their work: the formation flows, the compliance agents, the treasury operations, the trade tooling. The store charges a disclosed share of the value of work automated, following the commercial model of an app store.

The agreements also need physical and cultural provision: buildings that open on time, decent housing, schools, food, festivals, and a sense of local identity. Part I showed that zones which neglected these needs failed regardless of their incentives. Momentum budgets for them as infrastructure.

### How Growth Sustains Itself

Working infrastructure attracts companies whose activity justifies further infrastructure. Their early success draws attention from founders, creating opportunities that attract talent and support further successes. Returns attract capital, which finances the next investments and returns. These effects reinforce one another. In the second or third year, a well-built zone reaches the point where organic growth exceeds the developer's contribution.

The network adds a loop no isolated zone ever had: each new node makes every existing node more valuable, because each corridor extends every member's reach. The direction of current approaches provides evidence for this adoption mechanism. The pattern of this industry's first sixty years was developers courting governments. The pattern visible now is governments arriving with their own proposals — jurisdictions across Asia, the Gulf, Africa, the Caribbean, and the Americas approaching the network with sites, legislation, and timetables in hand. Part III states that record at the exact stage each engagement has reached.

---

## Chapter 9: The Research Layer

### The Missing Controlled Evidence

More than five thousand special economic zones have operated across seven decades, each intervening in institutions with measurable consequences for its population. Yet there is almost no controlled evidence of what works. Zone policy is set by analogy, anecdote, and consultancy folklore. The World Bank's own reviews, cited throughout Part I, document the consequence: the same mistakes, repeated on every continent, at a cost counted in decades and public fortunes. Practitioners know things academics never test; academics know things practitioners never read. The separation prevents research and operating experience from correcting one another.

The network could connect research with practice through its shared measurement system. Attestations record each incorporation's elapsed time, each compliance check's outcome, and each service interaction's cost across jurisdictions with comparable records. This fine-grained operating evidence makes it possible to test what a policy does.

### The Laboratory

To turn that possibility into science, this book proposes a dedicated research institution: the **Laboratory for Incentivization, Coordination and Cooperation** — LICC. Its founding framework was published in July 2025, and its detailed blueprint is drafted. Constituting it with leading academic partners is a project of the network's next phase. The following describes its design.

The laboratory has three research questions. **Incentivization:** what actually moves investment, formation, and growth — do tax holidays attract builders or tourists; which incentives select for the companies a zone wants to keep? **Coordination:** how standards, corridors, and shared services emerge among parties no one commands. **Cooperation:** how zones sustain collaboration while competing — what makes a corridor durable, what makes benefit-sharing credible. Each question concerns decisions governments must make with public funds.

Policy variations across consenting jurisdictions provide natural experiments. Governments may also choose controlled trials. Attestations supply more accurate measurement than survey-based development research has had. A policy validated in one zone can be adopted by another as executable rule-sets, and the receiving zone's data tests the finding again.

Three commitments define the laboratory's role.

**Measurement and publication.** The laboratory publishes findings and service-level facts. It holds no authority over any jurisdiction — no admission power, no ranking that gates participation, no machinery of exclusion. Jurisdictions are accountable to their own publics and to the counterparties of their own corridors; the laboratory contributes public evidence.

**Consent and ethics are constitutive.** Research involving a zone's people or businesses runs under the zone's own law and the laboratory's ethics review, with consent, with pre-registered designs, with findings published whether flattering or not. These requirements protect the people and businesses participating in research.

**Its findings are public goods.** The point of learning what works is that the next zone — in the network or out of it — does not repeat the last zone's mistakes. The laboratory publishes for the field, in the open literature, at the standard of the field's best journals. Publishing lets other zones use the lessons from seventy years of experimentation.

Independent publication subjects the network's claims to evidence that anyone can check. The architecture can then be assessed through an open experimental record. Part III begins that assessment by distinguishing the operations already running from signed work and proposals.
