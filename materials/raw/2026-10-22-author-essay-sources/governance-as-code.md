# Corporate Governance Is a Protocol

**Author:** Raeez Lorgat

A board resolution is a program whose inputs are a motion, a quorum, and eligible voters. Control flow covers the notice period, convening, deliberation, and voting. A defined threshold determines whether the vote passes or fails, producing an authorized action or rejection. People execute this distributed program through steps that take days or weeks.

Corporate governance documents, including articles of incorporation, bylaws, and shareholder agreements, describe this protocol for lawyers to interpret. Authority determines who can participate, quorum how many must participate, and the voting threshold what counts as agreement. Notice periods set the advance warning required, while reserved matters specify which actions need which approvals. Together these rules determine how the corporation makes binding decisions.

Manual verification can work when all participants are human and the corporation makes a handful of governance decisions per quarter. A lawyer reads the bylaws, checks attendance, verifies the vote count, and confirms the notice period. The process is expensive and slow, but the low decision rate makes it tolerable.

Machine-speed tooling is entering corporate governance as preparation, execution, and monitoring infrastructure. A program drafts the board resolution, distributes the notice, collects the votes, and files the result. Increasingly, delegated programs receive authority to act on behalf of human principals within defined scope.

Machine participation requires a typed, verifiable specification. The program must determine the valid quorum, applicable vote threshold, approving authority, and current delegation chains without ambiguity. Formalizing those rules makes the protocol executable.

## I.

Governance combines approval steps. A board resolution requires notice, convening, quorum verification, a vote, minutes, and filing. A shareholder vote adds a record date, proxy distribution, vote collection, tabulation, and certification. A merger combines both entities' board and shareholder approvals with regulatory approval into one authorization.

These steps compose sequentially and in parallel. In a board resolution, each step completes before the next begins. In a merger, two independent governance processes run concurrently and must both complete before the merger proceeds. Operations can mix the forms: sequential board authorization can precede a shareholder vote that runs in parallel with the other entity's governance process.

Process calculi (Hoare 1985; Milner 1989) supply the vocabulary. Writing `;` for sequencing and `∥` for parallel composition that joins on completion, a board resolution is

`notice ; convene ; quorum ; vote ; minutes ; file`

and a merger of A and B is

`((board_A ; shareholders_A) ∥ (board_B ; shareholders_B)) ; regulatory ; close`

The proposed governance fragment uses sequencing, parallel join, and branches guarded by conditions determined by the time the branch is reached. For example, a regulated target requires a clearance step. The fragment excludes communication between branches, recursion, and the nondeterministic choice that complicates full process calculi.

Our design hypothesis is that the corporate actions considered here decompose into finitely many approval steps combined by these three operators. The following two jurisdictions support the hypothesis, which remains unestablished in general.

In Florida, the board holds the power to issue shares (Fla. Stat. §607.0621). By default, quorum requires a majority of the number of directors prescribed in the articles or bylaws. A majority of directors present determines the act of the board (§607.0824).

The Cayman Islands Companies Act leaves allotment to the articles. Its model articles (Schedule 1, Table A) apply by default to a company limited by shares (s.22(2)). They place allotment within the directors' general management power (reg. 66). Shares created by an increase of capital are subject to a pro-rata first offer to members (reg. 34). Amending the articles requires a special resolution (s.24). At least two-thirds of the members entitled to vote who do vote must support it. The general-meeting notice must announce the intention to propose that resolution (s.60(1)).

The Act prescribes no day count for that notice. Notice must follow the company's regulations (s.60(3)). Where the articles are silent, the model articles require at least seven days (reg. 41). The Act's five-day backstop applies only to a company with no regulation on summoning meetings (s.61). Thus the programs draw on different legal sources: statutory defaults in one case, constitutional documents backed by model articles and statutory fallback in the other. Both specify authority, approval steps, and procedural constraints on quorum, threshold, and notice over named bases.

## II.

To represent these variations, separate the governance rules from the engine that executes them. The rules form a typed, content-addressed artifact declaring the governance required for an action. The engine creates the consent artifact, collects votes, checks quorum, and reports the result. A consent artifact is the signed approval record: a board resolution, written consent, or shareholder vote.

A governance specification has three parts: declared authorities, a mapping from corporate actions to required approvals, and procedural parameters for each approval. The parameters specify quorum basis and fraction, threshold basis and fraction, and notice period. Loading checks that references resolve, each action maps to at least one declared authority, and every quorum and threshold names a declared basis. Canonical serialization gives equal specifications equal hashes.

Lawyers must be able to audit the rules against legal requirements without reading the execution engine. Procedural code obscures that comparison. A declarative rule can state board authority, quorum as a majority of prescribed seats, approval as a majority of directors present, and two days' notice for special meetings. A lawyer can compare those terms with the statute and bylaws and approve the specification.

Content addressing fixes which rules an action uses. Each specification's identity is the hash of its canonical serialization. Adding an authority, changing a threshold, or removing a notice requirement changes that identity. An amendment produces a new artifact and hash, while existing action references retain the old rules. The specification hash must appear inside the consent artifact's signed content. Substituting different rules then breaks the signature.

For an audit of a share issuance, the digest identifies the exact specification used. The regulator can compare it with the governing documents in force at the time, linking dated bylaws to the specification and its hash.

## III.

A corporation is a hierarchy of authorities with different powers, different compositions, and different procedural requirements.

The board of directors is a collective body. It decides by voting, subject to quorum and threshold requirements. An officer, such as the president or secretary, is a single authority who can make certain decisions unilaterally within delegated scope. A registered service provider is an external participant with specific filing authority. In multi-entity structures, including corporate groups and joint ventures, authorities of one entity may hold delegated power over actions of another.

These authorities form the nodes of an authority graph. Directed edges represent delegations scoped to specified matters and step types. A board can delegate signing authority for routine filings to the president. A parent company's board can delegate approval rights for specific action types to a subsidiary's board. Each edge names the matters and step types covered. A cross-entity edge also names the relationship that justifies the delegation.

The graph makes delegation chains traceable. The action of a program acting for an officer references the officer's delegation, which in turn references the board's grant. Each link is a typed edge subject to the specification's load-time resolution checks. An edge with an unresolved endpoint is rejected.

## IV.

Quorum verification requires the specification to name what it counts.

A quorum is a count over a named eligibility basis. Florida's default board quorum uses the number of directors prescribed in the articles or bylaws (Fla. Stat. §607.0824(1)). Vacant seats remain in the denominator. A seven-seat board with two vacancies and three directors present has a majority of filled seats but lacks quorum: four of seven are required. Approval instead requires a majority of directors present (§607.0824(3)). With five present and two abstaining, a two-to-one vote in favor fails.

A Cayman special resolution requires at least two-thirds of the entitled members who vote (s.60), excluding abstentions and absences. Delaware charter amendments require a majority of outstanding stock entitled to vote (8 Del. C. §242(b)(1)), so absence counts against. The specification must distinguish prescribed seats, directors present, votes cast, and shares outstanding. Stating the fraction alone leaves the rule incomplete.

A secretary verifies quorum by taking attendance. A program collecting electronic board votes needs a checkable record of eligibility at the time of the vote. A count alone cannot supply that evidence.

Each vote is an attestation: an eligible party's signed statement naming the matter, vote, and specification hash. Verification checks each signature, signer eligibility against the snapshot, and attestation timing within the governance window, after notice and before deadline. It excludes duplicate signers, then evaluates the threshold predicate over the verified set. Minutes must record who voted and how, so the attestations remain individually accountable. An aggregation that hides signers is disqualified.

The voting threshold is one more parameter over the same evidence. A simple majority, a two-thirds or three-quarters supermajority, and unanimous consent each define a different predicate on the aggregated attestations, over a basis the specification names.

Verification depends on four trust roots. First, eligibility requires the register keeper's signed, time-stamped snapshot of directors or members as of the record date. The record establishes that voters appear on the snapshot, not that the snapshot is true. Second, identity requires a layer that binds keys to people. A signature proves key possession, and quorum arithmetic cannot remove the risk of key compromise. Third, time-window checks require signed timestamps from a source the verifier trusts. Fourth, reference requires the specification hash inside each attestation's and consent artifact's signed content. A hash cited outside the signature detects nothing.

Mechanical verification establishes that attestations satisfy the specification relative to the snapshot, key bindings, and clock. The registrar remains responsible for the snapshot's honesty, and lawyers for the specification's correspondence to governing documents. Neither responsibility is discharged by a theorem.

Faster vote collection and verification increase the importance of notice periods and quorum requirements. Notice gives eligible participants time to consider the matter. Tooling might convene a "board meeting," collect votes, and report quorum in seconds, so the protocol must still enforce the prescribed notice period.

## V.

A merger joins two independent governance processes. Each entity must satisfy its own rules, authority graph, quorum, and threshold requirements before the merger proceeds.

A joint venture may need different types of approval from three entities. A recognition agreement between two jurisdictions needs each side's authorities to approve under procedures that share only the join. Regulatory and corporate approvals may also interleave: a board approves subject to regulatory clearance, while the application requires evidence of board approval.

This dependency still fits the fragment. The board's condition becomes a guard on closing, evaluated after the regulator answers. The application follows the board vote to satisfy the regulator's evidence requirement: `board ; regulatory ; close` with the guard on `close`. This is the merger expression's existing structure, with no communication between branches.

These operations use two distinct joins. The governance join is conjunction: every entity must satisfy its own approval predicate, and one entity's approval cannot substitute for another's. The compliance join is a meet over separately evaluated participant verdicts, with particular importance for sanctions. The order is NonCompliant < Pending < Compliant, and the joint verdict is the strictest. One participant's clearance cannot lift another's failure because the prohibitions attach to each party separately. *How Compliance Composes* develops this rule and its legal basis. Both joins are non-compensating. The specification declares the participants and join, leaving neither to runtime inference.

## VI.

Jurisdictional variation tests the separation between specification and engine. A new jurisdiction must be expressible without changing the engine.

The engine selects a specification by the target entity's jurisdiction and form, then reads the action's required approvals. For each approval, it creates a consent artifact, collects attestations, and checks quorum, threshold, and timing. It composes the results using the declared join, without holding governance rules of its own. Each consent artifact carries the requesting operation's identifier and the hash of the specification used to collect it.

Return to the Florida and Cayman cases as inputs to this engine. A Florida for-profit corporation issues shares through board authority, which its articles may reserve to shareholders (Fla. Stat. §607.0621). Default quorum requires a majority of prescribed directors (§607.0824(1)), while approval requires a majority of directors present (§607.0824(3)). A special meeting requires two days' notice of date, time, and place. A regular meeting requires none by default (§607.0822).

For a Cayman exempted company limited by shares amending its articles, members act in general meeting. At least two-thirds of those who vote must approve (s.60(1)), and notice must announce the proposed special resolution (s.60(1)). The notice period follows the company's regulations (s.60(3)). Where its articles are silent, the model articles require at least seven days (s.22(2); Table A, reg. 41). Five days applies only where the company has no regulation on summoning meetings (s.61).

The engine must accept these differences in authority, eligibility basis, threshold, and notice period through the specification. Both cases use the same structure: defined authorities, procedural parameters over named bases, and a mapping from actions to approvals.

Adding the Cayman Islands therefore requires a specification declaring its authority structure, procedural parameters, and reserved matters. The specification passes the existing load-time checks, receives a content address, and is selected by jurisdiction and entity form. The engine's code remains unchanged.

## VII.

Manual verification sufficed while governance participants were human and decision rates were low. Delegated participation and increasing decision volume change those requirements.

Delegated programs prepare, execute, and monitor governance. Distributing notices, collecting votes, and filing results requires them to read the protocol mechanically. Ambiguity that a secretary resolves through judgment becomes a failure mode for automation.

An entity that previously made a dozen governance decisions a year may make hundreds as software handles share issuance, director changes, and routine filings. Each operation still requires governance checks. Hundreds a year means an action every working day, making individual legal review of each decision untenable. Verification must operate at the same rate as execution.

The ingredients have established uses. On-chain governance frameworks execute quorum, threshold, and timelock logic, with code serving as a protocol-native community's constitution (Kiayias and Lazos 2022). Rules-as-code systems, including Catala (Merigoux, Chataing, and Protzenko 2021), compile statutes into executable form. Ricardian contracts (Grigg 2004) and smart legal contract templates (Clack, Bakshi, and Braine 2016) bind machine-readable parameters to controlling legal prose. This paper uses the same parallel-text construction. Workflow formalisms have modeled approval processes for decades (van der Aalst 1998). Delaware permits electronic databases, including distributed ledgers, for the stock ledger (8 Del. C. §224). Wyoming charters entities managed wholly or partly by smart contract (Wyo. Stat. §17-31-101 et seq.).

For ordinary corporations under existing law, this paper combines jurisdiction-parameterized specifications with explicit quorum and threshold bases. Each signed consent binds the specification's content-addressed identity, and multi-entity actions use a non-compensating join.

Legal documents remain authoritative. Lawyers validate the typed, content-addressed specification against the bylaws before machines use it to verify governance requirements. The specification runs in parallel with the legal text and does not supersede it.

The governing documents, facts, and jurisdiction determine the answer to "was this corporate action properly authorized?" Given the content-addressed specification, signed attestations, and eligibility snapshot, computing that answer changes the cost of verification. Lawyers validate statutory defaults once per jurisdiction and entity form. They validate each entity's bylaws and shareholder agreements once per version, with each amendment producing a new specification and hash. Subsequent decisions reuse that validation. An entity that amends its bylaws annually and acts hundreds of times under them can obtain hundreds of verifications from one validation.

## References

Clack, C. D., Bakshi, V. A., and Braine, L. (2016). "Smart Contract Templates: Foundations, Design Landscape and Research Directions." arXiv:1608.00771.

Grigg, I. (2004). "The Ricardian Contract." In *Proceedings of the First IEEE International Workshop on Electronic Contracting*.

Hoare, C. A. R. (1985). *Communicating Sequential Processes*. Prentice Hall.

Kiayias, A. and Lazos, P. (2022). "SoK: Blockchain Governance." In *Proceedings of the 4th ACM Conference on Advances in Financial Technologies (AFT)*.

Lorgat, R. *How Compliance Composes*. Companion paper in this series.

Merigoux, D., Chataing, N., and Protzenko, J. (2021). "Catala: A Programming Language for the Law." *Proceedings of the ACM on Programming Languages*, 5(ICFP).

Milner, R. (1989). *Communication and Concurrency*. Prentice Hall.

van der Aalst, W. M. P. (1998). "The Application of Petri Nets to Workflow Management." *Journal of Circuits, Systems and Computers*, 8(1), 21-66.
