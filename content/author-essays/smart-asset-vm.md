# The Asset Virtual Machine

A share transfer brings several decisions together. Someone must establish the seller's title, the buyer's eligibility, the required approvals, and the rules governing the transaction. Those decisions depend on a particular jurisdiction, time, and body of evidence.

The share's record should carry that context. An asset program can identify the required checks, request decisions from the responsible institutions, and retain their answers. Each later action then adds its own evidence to the asset's history.

Consider an issuance followed, six months later, by a transfer. The issuance may require board authorization, shareholder approval, a securities exemption, investor screening, and tax determinations. The transfer raises a new question about a different holder at a different time. The original approval remains evidence of the issuance. The transfer needs its own decision.

## Carrying the checks with the asset

Token standards already make restrictions part of ordinary transfers. ERC-1400 describes transfer status codes, while ERC-1404 defines functions for detecting and explaining restrictions. ERC-3643 connects ordinary transfers to an identity registry and a modular compliance contract. These mechanisms give the contract a defined place to check eligibility. [ERC-1400](https://github.com/SecurityTokenStandard/EIP-Spec/blob/master/eip/eip-1400.md), [ERC-1404](https://github.com/ethereum/EIPs/issues/1404), [ERC-3643](https://ercs.ethereum.org/ERCS/erc-3643).

An asset virtual machine extends this approach to the record of a decision. A virtual machine is the interpreter that runs the asset's programs. Here it must record the exact question, the governing program, the evidence used, and the answer. Its execution rules must also cover rejection, a missing approval, and a failed run.

The mechanisms are established. Metering limits computation. Hash chains make recorded history tamper-evident. Complete mediation routes every protected action through the checks that govern it. The design question is how to combine them around an asset whose legal and operational authority remains with identified institutions.

The issuance program reads the relevant compliance records and produces a receipt tied to the asset. That receipt identifies the issuer, recipients, jurisdiction, evaluation time, governing programs, and evidence. When the transfer program runs, it produces another receipt for the new context. A receiving institution can inspect both decisions and determine which evidence its own rules accept.

The asset's declared requirements must accurately represent the applicable rules. A digest identifies the program named in a receipt. The institution still needs a sound translation from the governing instruments into that program.

## Keeping the decisions distinct

A compliance record can distinguish compliant, pending, exempt, not applicable, and non-compliant. Those distinctions matter to an examiner. An exemption names a legal basis and scope. A finding of non-applicability answers whether a requirement reaches the action. Pending records an unresolved question.

The execution boundary needs a separate decision about the proposed action. In [Op, “Asset programs in an embedded virtual machine”](https://research.momentum.inc/papers/op.html), that decision has three forms: admit, reject, or pending. Admission binds evidence to the exact action, while rejection carries a reason and its evidence. A pending result records what the suspended request must await.

A pending required decision keeps the action pending. An exemption can satisfy its named requirement when the exemption's conditions hold. Non-applicability requires an attributable scope determination. These records remain available after the runtime decides whether the complete action can proceed.

This also separates a declared right from permission to exercise it. A proceeds entitlement, registered title, voting power, and authority to instruct a custodian are different rights. The governing instrument and current authority determine which action each permits. [One Entity in Many Jurisdictions](https://research.momentum.inc/papers/one-entity-in-many-jurisdictions.html) develops that distinction for an exact holder, right, and proposed act.

## The institution controls the write

The asset program proposes a change. The surrounding institutional runtime, called the parent runtime, controls every durable business write.

A transfer program can calculate a quantity, assemble evidence, and request an ownership update. The parent checks the request against its admission evidence, affected parties, sanctions snapshot, asset authority, and current record. It also checks the declared response if an external effect later needs correction. The parent consumes the request into either a committed receipt or a failure receipt.

The same boundary applies to program storage that affects the durable business record. Temporary computation can prepare a result. A durable change must pass through the parent. Otherwise, an asset could alter the facts against which its own transfer is assessed.

The asset's declared record binds the digests of its gate programs. The host runs discretionary business logic only after every required gate admits the action. A gate reads the relevant records and returns its decision. It cannot change those records to obtain a favorable answer. The business program's receipt binds the gate receipts for that invocation, so an examiner can check their order and correspondence.

Authority can change between preparation and use. Resumption therefore processes relevant policy changes and revocations before further action. A request prepared yesterday needs the authority required when it is transmitted today. Where authority must hold at the external effect, the provider must honor a sufficient transaction-specific authorization or enforce a current check at that boundary. A local reservation cannot prolong a revoked authority. Op's [execution model](https://research.momentum.inc/papers/op.html) specifies these separate uses.

## A request can remain unfinished

A program can compute a coupon or redemption and ask the parent to submit a payment request. The payment provider then supplies evidence of what happened. Dispatch, provider acceptance, legal finality, and beneficiary receipt are separate facts.

The parent authenticates a provider outcome and binds it to the original request before the asset program consumes it. The saved continuation can consume that evidence once, so repeated delivery cannot resume it twice. A callback about another payment supplies no result for this one. An unsigned message or an expired local timer supplies no provider outcome.

Partial performance needs the same care. If a provider pays part of a redemption, the record retains the amount paid and the unpaid balance. It also records whether the provider can still execute the remainder. Retrying or reallocating that balance requires the appropriate authority and protection against duplicate execution. A refusal leaves the underlying entitlement to its governing terms. It does not itself pay or extinguish it.

Correction adds another event. A refund is a new payment by the recipient. A provider reversal, a legal unwind, and compensation each need their own authority and evidence. Compensation can restore a specified business condition when its contract and outcome establish that condition. It preserves the original event in the history. Op's [provider and reversal models](https://research.momentum.inc/papers/op.html) keep these outcomes separate.

## Bounding an active run

An asset program must release the systems processing it. A hostile or defective computation should consume a declared allowance and then produce a failure receipt.

Gas is an accounting unit for that allowance. Suppose a run has budget $G$, and every charged step costs at least a fixed $c>0$. The budget cannot increase during that run. It can take at most $\lfloor G/c\rfloor$ charged steps. A budget of 10,000,000 with a minimum charge of 2 therefore permits at most 5,000,000 charged steps.

Reaching a receipt requires more than counting those steps. The runtime must make local progress, bound any uncharged administrative work, and reserve enough resources to record termination. Host validation also belongs within the contract. An external wait must enter suspension so the active computation can end. These are requirements on the runtime and its implementation, rather than a consequence of selecting gas prices.

An illustrative schedule shows how computation and institutional work can share a meter:

| Operation | Illustrative gas charge |
|---|---:|
| Stack, arithmetic, memory, jump | 2–8 |
| Hash | 30 |
| Storage read | 200 |
| Log entry | 375 |
| Procedure call | 700 |
| Merkle proof verification | 1,000 |
| Signature verification | 3,000 |
| Storage change, before its request charge | 5,000 |
| Compliance read | 10,000 |
| Zero-knowledge proof verification | 50,000 |
| Institutional write request | 100,000 |

Some charges represent machine work, while others price a request for institutional evaluation. A durable storage change incurs both its operation charge and the institutional write request charge. The combined charge accounts for the parent's evaluation and the storage work. A zero-knowledge proof check can cost more computation than a compliance read, while a write request can demand more institutional work than either.

The meter supplies a useful one-sided inference. Under this schedule, a total below 10,000 excludes a compliance read or institutional write request. A total below 100,000 excludes an institutional write request. A larger total does not identify what ran: 5,000,000 could cover 500 read charges or 50 request charges. Other work consumes its own allowance. The receipt supplies the operation record.

The bound applies to each active run. A suspended program can resume with a new budget. Repeated authorized resumptions can continue indefinitely, and a step bound supplies no wall-clock deadline for a provider or approval process.

## Evidence that another party can check

Every run needs a receipt, including a rejection, trap, resource exhaustion, or suspension. A successful run records the checks and requested changes. A failed run records where it stopped and why.

The receipt binds the program digest, caller, action context, evaluation time, sequence number, and preceding receipt's digest. It retains the compliance questions and answers, evidence digests, proposed changes, outcomes, and resource use. Each committed storage change has a before-and-after record, and log entries remain in the receipt. Each successor receipt commits to that record.

A hash chain allows an examiner to detect changes beneath a known head, assuming the hash function resists collisions. An operator signature attributes the record to its signer, under the signing-key assumptions. The examiner also needs a head held outside the operator's control. A counterparty, registry, or public log can retain that commitment.

Without such a commitment, an operator can present a different, internally consistent chain. Receipts after the latest external commitment also remain outside its protection. The commitment interval therefore determines how much recent history has yet to receive that protection.

Signatures and hashes establish the integrity and attribution of recorded assertions. Independent replay checks their computational content. It needs the exact program, inputs, governing rules, authority records, and committed order of admitted evidence. The verifier recomputes the results and compares the receipts. Op's [replay construction](https://research.momentum.inc/papers/op.html) states the deterministic and cryptographic premises for that check.

The source evidence retains its own authority requirements. A receipt can identify the sanctions list or filing used in a decision. Its provenance and legal status still determine whether the institution could rely on it.

Completeness also needs a party able to insist on the record. A counterparty can require a committed head covering its transfer before it completes the transaction. It then has evidence that the signed transfer record appears in that history. Execution checks establish the record's conformity to the program. Complete mediation establishes that the protected action passed through the required checks. An event performed through an unmonitored path can leave the existing chain intact.

## Waiting for approval

A board vote or regulatory approval can take days. The program suspends with a receipt naming the required approvers, threshold, deadline, and action they would authorize. Approvals bind to that request.

When the required approval arrives, the runtime can resume the saved computation with current authority and evidence checks. An approval deadline can instead close the approval request under its governing policy. Recording that expiry requires the relevant clock event and an operating service to process it.

A provider wait follows its own rule. Expiry can record an obstruction or authorize a separate cancellation request. The original provider wait remains tied to an authenticated outcome. Silence cannot establish that an external payment failed, succeeded, or became safe to repeat.

The share's history can then answer concrete questions. It identifies the issuance authority, the evidence used for a later transfer, the reason for a refusal, and any payment still outstanding. The holder, institution, and examiner can follow the same record while each retains the authority needed to act on it.
