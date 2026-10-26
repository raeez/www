# The Asset Virtual Machine

**Raeez Lorgat**

A share certificate records that someone owns something. It contains no record of the board's quorum at issuance or the issuing jurisdiction's prospectus requirements for the recipient's investor class. Nor does it record whether the current holder's sanctions status changed yesterday. Lawyers, compliance officers, and transfer agents answer these questions in systems the certificate does not reference. The asset carries none of the compliance requirements that govern it.

This separation requires repeated work at every boundary. When a share moves between jurisdictions, someone must reconstruct its compliance context by hand in the receiving jurisdiction. When a regulator examines a transaction, the answer to the basic question -- was this legal? -- comes from a dozen systems outside the asset.

Suppose the asset carried its compliance requirements with it.

## I.

Assets are already programmable, but programmability alone does not supply this compliance structure. An ERC-20 token can execute arbitrary code, yet that code has no structured relationship to the legal requirements governing the token. A Solidity function can consult a sanctions list as application logic alongside a transfer. The architecture does not ensure that the check ran, that it used the current list, or that it kept the result as evidence.

ERC-1400, ERC-1404, and ERC-3643 build the compliance check into the token contract itself. A transfer executes only if the token's own restriction check permits it. ERC-1400 uses a status code, ERC-1404 uses two view functions, and ERC-3643 uses an identity registry and a modular compliance contract. For the transfers those standards govern, on the one ledger where the token lives, the check cannot be skipped.

The check returns permission or refusal with a reason code. The jurisdiction is fixed in the deployment rather than supplied as a parameter of the question. A refused transfer leaves at most a reason code, with no record of what was evaluated or against which compliance state. A permitted transfer leaves a state change, with no evidence of what was evaluated to permit it.

A smart asset, in the sense meant here, carries a compliance program as a structural component, as fundamental as its ownership record. An examiner can verify ownership and confirm that every governing rule was evaluated for every recorded lifecycle event, in that event's jurisdiction and time. The examiner can also inspect the evidence, failures included.

This requires a domain-specific virtual machine composed from established mechanisms. Gas-metered termination is the EVM's own device (Wood 2014). Hash-chained tamper-evident records date to Haber and Stornetta (1991) and run at internet scale in Certificate Transparency (Laurie, Langley and Kasper 2013). Routing every privileged operation through one checked boundary is the complete-mediation principle of Saltzer and Schroeder (1975).

The contribution is an interpreter that combines these mechanisms with typed compliance verdicts, a chained receipt for every execution, and suspension for human approval. State changes with institutional consequences remain requests for the institution to execute. The following sections specify the machine and state what its evidence proves, and to whom.

## II.

When a corporation issues shares, it needs board authorization and may need shareholder approval above a threshold, depending on the jurisdiction. The shares must comply with securities regulation, and the recipients must pass KYC and sanctions screening. A cross-border offer activates further compliance domains. Tax treatment also varies by jurisdiction.

In a conventional system, separate systems check these requirements at separate times and store the results in separate databases. The share records none of it. Six months later, a transfer requires reconstruction of the compliance context from scratch.

Now suppose the share carries a program encoding the compliance requirements that applied at issuance. When the share was created, the program read the issuing entity's compliance state across the relevant domains: sanctions, securities, corporate governance, and tax. It verified that every domain was satisfactory and produced a receipt bound to the share's identity. This cryptographic record states what was checked, the results, and the compliance state at that moment.

When the share moves, the program runs again for a different jurisdiction, holder, and moment in time. It evaluates the domains relevant to that context and produces another receipt, chained to the previous one. The share accumulates a verifiable history of ownership, timing, and compliance evaluations at every lifecycle event at which the program ran.

The word "smart" has meant self-executing at least since Szabo (1997) proposed embedding contractual terms in code. For institutional assets the useful sense is stricter. The asset carries its compliance program, the program runs at every lifecycle event, and every run leaves evidence.

## III.

The virtual machine that runs these programs differs from a general-purpose runtime in three ways.

First, compliance evaluation is a primitive operation. The machine refers to the institution's compliance state, indexed by entity, jurisdiction, and domain. One instruction reads a cell: the standing of this entity, in this jurisdiction, in this domain. It returns one of five verdicts: compliant, pending, exempt, not applicable, or non-compliant. These verdicts remain distinct because they record distinct facts. A pending review and an exemption may both permit an action today, but collapsing either into "allowed" destroys a distinction an examiner later needs.

In the EVM the equivalent read requires an oracle. This instruction also crosses into the institution's compliance infrastructure and trusts the answer it receives. The crossing is a typed primitive: the machine fixes the verdict type and prices the read. It also requires the receipt to record that the read happened, what it asked, the answer, and the digest of the evidence behind it. These requirements belong to the machine rather than the program's author.

Second, writes are deferred, never immediate. An ownership transfer, for example, may require a treasury update. A program that identifies this corporate action cannot perform the write. It produces a request, which the execution receipt collects and passes to the institutional write pipeline. That pipeline applies its own authorization, sanctions screening, and audit logging before deciding whether to execute the request. Only the institution can perform the action.

Third, every execution produces a receipt, failures included. A program that runs out of gas leaves a receipt saying so. If it reverts because a compliance domain failed, the receipt names the domain and its verdict. A successful execution leaves a receipt itemizing every compliance evaluation, storage mutation, and deferred write request. Each receipt binds the digest of its predecessor, making the asset's recorded execution history tamper-evident. Section VI states what that chain proves, what it does not, and under which commitments.

## IV.

Gas bounds execution and prices operations. Termination is a hard requirement because an asset's program runs inside institutional processes with deadlines: a transfer agent, a registry, a settlement. A compliance check that could run forever would let a hostile program detain every system obliged to process the asset.

Termination follows from one stated assumption: every instruction that can be followed by another instruction costs at least c > 0 gas. Only the terminal instructions -- halt, return, revert, yield -- are free. Under that assumption, an execution with budget G executes at most G/c + 1 instructions. In the schedule below, c = 2 and G = 10,000,000, so every execution ends within 5,000,001 instructions.

The bound is per execution. A yielded program resumes on quorum as a new execution with a fresh budget, and nothing bounds how many times it may yield. The execution bound and the approval deadline of Section VI therefore give a weaker lifecycle guarantee. Every execution ends within its budget, every suspension ends within its deadline, and a lifecycle with finitely many suspensions terminates. Indefinite prolongation requires a fresh quorum at every round, each round bounded by its own deadline. These are recorded decisions by the approvers, and they detain nothing because each execution has already ended.

The gas schedule uses the following representative prices:

| Operation | Gas |
|---|---|
| Stack, arithmetic, memory, jump | 2--8 |
| Hash | 30 |
| Storage read | 200 |
| Log entry | 375 |
| Procedure call | 700 |
| Merkle proof verification | 1,000 |
| Signature verification | 3,000 |
| Storage write | 5,000 |
| Compliance read | 10,000 |
| Zero-knowledge proof verification | 50,000 |
| Institutional write request | 100,000 |

The budget for one execution is 10,000,000.

The schedule prices two scarce resources at once and is therefore monotone in neither alone. Machine effort explains the lower tiers and why zero-knowledge verification, which is pure computation, costs five times a compliance read. Institutional attention explains the highest prices. A compliance read crosses into the institution's compliance infrastructure. An institutional write request asks the institution to evaluate and possibly fulfill a mutation, priced at ten reads.

Every price is nonnegative, so one institutional operation sets a lower bound on the total cost of any execution that performs it. The meter thus gives a one-sided certificate. A total below 10,000 proves the program performed no compliance read and requested no institutional write. A total below 100,000 proves it requested no write.

A higher total does not identify the operations performed: 5,000,000 gas is equally five hundred compliance reads or fifty write requests. The meter supplies a bound and a summary. The receipt records what actually ran.

## V.

The architecture separates into two levels.

Level 1 is compliance enforcement. These programs are compiled from the asset's declared compliance requirements. An asset that declares sanctions clearance and securities compliance gets a program that reads those domains and reverts unless every verdict permits the action. Level 1 programs are bound to the asset by content digest, and the asset's identity declares those digests. An examiner can therefore check that the programs that ran are the programs the asset declares as part of its structure.

Level 2 is programmable logic: user-authored programs that run after Level 1 has verified the compliance context. A Level 2 program can read compliance state, write its own storage, emit deferred write requests, and compute arbitrarily within its budget.

Neither level can write compliance state because the instruction set contains no operation that modifies it. A program may assemble evidence of a completed review and conclude that compliance state should change. It must request the change as a deferred write, priced at the write tier and judged by the institutional write pipeline like every institutional mutation. Level 1 programs run with deferred writes disabled altogether: a gate can read and revert, nothing else. Within an execution there is no write to read back. The instruction set therefore prevents a program from manipulating compliance state to pass its own checks.

The composition root, the host process that invokes the VM, runs every Level 1 program and proceeds to Level 2 only if all succeed. This ordering is a property of the host, not of the VM. To make it checkable, a Level 2 receipt carries the digests of the Level 1 receipts produced for the same invocation. An examiner verifies that the gates passed before Level 2 ran. A Level 2 receipt without its gate receipts is itself evidence of circumvention.

## VI.

Verification must account for a dishonest operator: the party that runs executions and stores the receipt chain could prefer a different history.

Every run of any of the asset's programs, for any reason, produces a receipt. It records an execution digest, a hash binding the program's bytecode digest, caller, jurisdiction, timestamp, sequence number, and previous receipt's digest. The receipt also records the outcome: success, revert with its reason, a resource-limit halt, or yield. It records gas consumed and every compliance evaluation, including the domain, context, verdict, and digest of the evidence behind the verdict. Every storage mutation appears as a before-and-after pair, alongside every deferred write request and log entry.

The receipt's own digest covers all these fields, and the next receipt binds that digest. Altering, deleting, or reordering any interior receipt therefore breaks every digest above it.

A hash chain alone proves only self-consistency. The operator could produce a different chain from scratch, correctly linked, and nothing internal to the two chains would distinguish them. Two commitments make the chain evidence. Each receipt carries the signature of the operator that produced it, making the history attributable: the operator cannot disown what it recorded.

The head of the chain is periodically committed outside the operator's control. It can be handed to the transaction's counterparty, filed with the jurisdiction's registry, or anchored in a public log. Once a head is in other hands, every receipt beneath it is fixed because a rewrite cannot reproduce the committed digest.

An examiner holding a committed head can verify the chain without trusting the operator's storage. The examiner recomputes each receipt's digest from its content and follows predecessor links and strictly increasing sequence numbers up to the committed head. The examiner checks the signatures and confirms that the program digests inside the execution digests match the compliance programs the asset declares. This check establishes integrity, order, and attribution: these executions ran, in this order, under these programs, and the operator has signed to it.

Three limitations remain. Receipts newer than the latest committed head are not yet fixed. The operator can revise them during the commitment interval, whose length is a policy decision.

A receipt proves what was evaluated and what the compliance infrastructure answered, not that the answer was true. Evidence digests identify the exact list, filing, or record used. The sanctions list's provenance, rather than the chain, vouches for the list's correctness.

Completeness remains limited: the chain proves the executions it records, not that every event requiring one was recorded. An event handled outside the machine leaves no receipt and breaks no digest. Certificate Transparency has the same limitation: a log proves only what was logged. It addresses this by having the relying party refuse what is not logged. Here the counterparty takes that role.

A counterparty that completes a transfer only against a committed head covering it holds proof that the transfer was recorded. No transfer completed on those terms can have run outside the machine. This closes the omission gap per transaction. The gap remains for an event with no party outside the operator to demand a head for it.

Some institutional workflows require human approval, such as a board vote or regulatory sign-off, and cannot complete in one step. At a multi-party approval gate, the program yields. The execution ends with a receipt recording the required approvers, threshold, and deadline, and approvals accumulate against that requirement.

Quorum resumes the program as a new execution with a fresh budget. If the deadline passes first, the suspension closes with a receipt recording the expiry, and the program does not resume. Every suspension therefore resolves within its deadline. The chain records the governance process from suspension to resolution, however many days it took.

## VII.

Financial infrastructure has historically separated the asset from the rules governing it. A share is a legal instrument whose compliance context is as much a part of it as its par value or ownership record. The machine described here makes that context part of the instrument. Requirements compile into gate programs bound to the asset's identity. These programs run at every lifecycle event and leave a receipt for every evaluation. External commitments fix the resulting history beyond the operator's control.

The machine evaluates compliance using verdicts from the institution's compliance infrastructure. It does not decide compliance, and its chain proves what was asked and answered, never that the answers were right.

## Limitations

Compilation of declared requirements into Level 1 programs is assumed faithful. A wrong gate program produces wrong gating with complete evidence: the chain proves fidelity to the program, not the program's fidelity to the law.

The chain proves the executions it records, not that every event requiring one was recorded. An event handled outside the machine leaves no trace in it. A counterparty closes this omission gap only for its own transaction by completing it against a committed head covering it. The evidentiary guarantees also depend on the commitments. Operator signatures assume the provenance of the signing keys, and everything after the newest committed head remains revisable until the next commitment.

The termination bound is per execution. Every suspension resolves within its deadline, and a lifecycle terminates given finitely many suspensions. Approvers who grant fresh quorum at every round can prolong it without bound, each round bounded by its own deadline.

Only the institution can execute the machine's requests. A Level 2 program can compute a coupon or a redemption. It produces a deferred write request that the institution's pipeline settles or refuses. This preserves the authority boundary of Section III without limiting what the program computes.

## References

Dossa, A., Ruiz, P., Vogelsteller, F. and Gosselin, S. (2018). *ERC-1400: Security Token Standard.* Ethereum improvement proposal 1400.

Haber, S. and Stornetta, W. S. (1991). "How to Time-Stamp a Digital Document." *Journal of Cryptology* 3(2), 99--111.

Laurie, B., Langley, A. and Kasper, E. (2013). *Certificate Transparency.* RFC 6962, IETF.

Lebrun, J., Malghem, T., Thizy, K., Falempin, L. and Boudjemaa, A. (2021). *ERC-3643: T-REX -- Token for Regulated EXchanges.* Ethereum improvement proposal 3643.

Saltzer, J. H. and Schroeder, M. D. (1975). "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1278--1308.

Szabo, N. (1997). "Formalizing and Securing Relationships on Public Networks." *First Monday* 2(9).

TokenSoft (2018). *ERC-1404: Simple Restricted Token Standard.* Ethereum improvement proposal 1404.

Wood, G. (2014). *Ethereum: A Secure Decentralised Generalised Transaction Ledger.* Ethereum yellow paper.
