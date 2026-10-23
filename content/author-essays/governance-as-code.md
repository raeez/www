# Corporate Governance Is a Protocol

A seven-seat board has two vacancies. Three directors attend a meeting and all three support a motion. Have they authorized the action?

The answer depends on what the quorum counts. A majority of filled seats requires three directors. A majority of prescribed seats requires four. The same attendance and unanimous vote can therefore produce different results under different governing documents.

Abstentions create another distinction. Five directors attend, two vote in favor, one votes against, and two abstain. The motion has a majority of votes cast. It lacks a majority of directors present.

Corporate governance turns on these details. Articles, bylaws, shareholder agreements, and statutes determine who may act, who must participate, and which approvals an action requires. Software that prepares resolutions, collects votes, or submits filings needs an exact account of those rules. A voting fraction alone leaves most of the decision unspecified.

## What a vote counts

Florida's ordinary board defaults illustrate both cases, assuming equal voting rights. Quorum requires a majority of the prescribed number of directors. Approval requires a majority of directors present when the vote occurs, with quorum present. The articles, bylaws, and statutory exceptions can change these requirements. Under the defaults, the three-director meeting lacks quorum, and the two-to-one vote among five attendees fails. [Florida Statutes §607.0824](https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0607/Sections/0607.0824.html).

Other decisions use other denominators. At a Cayman general meeting, a special resolution requires at least two-thirds under the applicable voting basis, unless the articles require more. A poll follows members' voting entitlements, which may differ from a headcount. Abstentions are excluded. Delaware's ordinary charter-amendment rule uses outstanding stock entitled to vote, subject to statutory exceptions, required class votes, and any higher charter threshold. Eligible shares left unvoted remain in that denominator. [Delaware General Corporation Law §242](https://delcode.delaware.gov/title8/c001/sc08/index.html#242).

A governance specification must distinguish prescribed seats, directors present, votes cast, and outstanding voting shares. It must also identify eligibility, voting weight, class rights, and the applicable exceptions. Two rules can use the same fraction and authorize different actions.

Notice has its own purpose and source. Florida permits regular board meetings without notice by default. Special meetings generally require at least two days' notice, unless the articles or bylaws provide otherwise. The notice identifies the date, time, and place. Faster vote collection leaves that requirement intact. Eligible directors still need the prescribed opportunity to consider the matter. [Florida Statutes §607.0822](https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0607/Sections/0607.0822.html).

For a Cayman special resolution at a meeting, notice must announce the intention to propose it. The company's regulations govern the notice period. Where applicable model articles supply the rule, they require at least seven days, with shorter notice available by the specified unanimous consent. The Act's five-day fallback concerns companies with no regulation on summoning general meetings. A separate unanimous written procedure is available where the articles authorize it. [Cayman Companies Act, sections 22, 60–61 and Table A](https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1961/1961-0003/1961-0003_2026%20Revision.pdf).

## Separate the rules from their execution

A lawyer should be able to compare the specification with the governing documents without reading the software that collects votes.

The specification declares the authorities, maps corporate actions to required approvals, and states each approval's procedural parameters. Those parameters include the eligibility basis, quorum, approval threshold, and notice period. The execution engine creates the approval record, collects signed votes, and checks the declared conditions.

Share issuance shows why the mapping matters. Florida gives the board issuance authority unless the articles reserve it to shareholders. Its statute also requires the board to determine that the consideration is adequate. Cayman allotment depends on the company's articles. Applicable model articles supply directors' management powers, subject to statutory and constitutional reservations. Unless a general meeting directs otherwise, shares created by a capital increase go first to notice-entitled members in proportion to their existing holdings. A company can exclude or modify those model provisions. The same operation can therefore require different approvals and preliminary steps. [Florida Statutes §607.0621](https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0607/Sections/0607.0621.html).

Loading a specification can check whether every referenced authority exists and every threshold names a basis. Legal review must establish that those declarations correspond to the controlling instruments. A well-formed specification can still encode the wrong rule.

Each specification receives a content address: a cryptographic hash of its canonical encoding. Changing an authority, threshold, or notice requirement changes the hash. An amendment creates a new specification while historical decisions retain their references to the text they used.

The signed approval record must contain that hash. This binds the signers to a particular motion and rule set. An audit can then connect the decision to the specification and the governing documents effective at the relevant time. A hash placed outside the signed content supplies no such binding.

Jurisdictional differences should enter through the specification wherever the engine supports their procedures. A new procedure outside that supported model requires an extension. The claim that every corporate action fits one finite model remains a design question.

## Combine approvals without replacing them

A board decision taken at a meeting can involve notice, convening, quorum verification, voting, and minutes, followed by any required filing. A shareholder process may add a record date, proxies, tabulation, and certification. A merger can require approvals from both entities and a regulator, depending on its legal route.

Sequencing and parallel composition give a compact account of these dependencies. With `;` meaning “then” and `∥` meaning “both processes must finish,” a board procedure has the form:

```text
notice ; convene ; quorum ; vote ; minutes ; file
```

A merger can have the form:

```text
((board_A ; shareholders_A) ∥ (board_B ; shareholders_B))
; regulatory ; close
```

These are workflow sketches. Their steps acquire meaning from the applicable rules. The finite fragment also permits branches whose conditions are known when execution reaches them. It excludes recursion, communication between parallel branches, and nondeterministic choice.

Conditional board approval can fit this fragment. The board approves subject to regulatory clearance. Its resolution supports the application, and closing waits for clearance. The sequence is `board ; regulatory ; close`, with the closing condition checked after the regulator answers.

A joint venture may require different approvals from three entities. A recognition agreement may require each jurisdiction to complete its own adoption procedure. Each participant supplies its own authorized act. A protocol vote among software operators cannot replace a required board, shareholder, or sovereign approval.

There are two separate combination rules here. Combining approvals requires every necessary approval to hold. Combining compliance evidence retains every applicable restriction. In the simple ordered grades NonCompliant, Pending, and Compliant, the combined applicable grade is the strictest.

The full record also retains applicability, exemptions, evidence, and reserved local decisions. A favorable result for one participant cannot remove another participant's applicable prohibition. [How Compliance Composes](https://research.momentum.inc/papers/how-compliance-composes.html) develops that richer record and the conditions governing its combination.

## Authority must still exist when used

A board decides collectively. An officer acts within delegated authority. A service provider may have a specific filing mandate. Corporate groups can also grant powers across entities where the relevant instruments permit them.

An authority graph records these relationships. Each directed connection names the grantor, delegate, matters, permitted actions, and validity conditions. A cross-entity delegation also identifies its institutional basis. A program acting for an officer can trace its authority through the officer's grant to the board's authorization.

Resolving that chain once is insufficient for a later act. A delegation can expire or be revoked while a filing waits in a queue. The final record change must check the current authority, its scope, and the facts on which permission depends. A delegate can pass on only the powers it received.

[Programmable Institutions](https://research.momentum.inc/papers/programmable-institutions.html#the-smallest-example) gives a concrete example. A secretary's delegation expires at 17:00. Preparation at 16:59 cannot authorize a record change at 17:01. The registrar checks authority when committing the change.

Some decisions also require judgment. A rule may demand satisfactory evidence, a fitness determination, or an approval by a named office. [Lex](https://research.momentum.inc/papers/lex.html) records the exact unanswered question, permitted answers, and authority entitled to answer. The signed answer binds the request, rule, and supporting context. A changed question needs the corresponding authority and compatibility checks. Waiting longer cannot supply the missing judgment.

## Preserve the evidence behind the count

A secretary can check attendance in a room. An electronic process needs evidence of who was eligible and what each person authorized.

Each vote is a signed attestation naming the matter, vote, and specification hash. Verification checks the signature, eligibility, and timing. It rejects duplicate use of the same voting entitlement. Where the rules permit proxy voting, it verifies the principal, delegated voting authority, and weight. Quorum and approval use the declared bases. The approval record retains individual attribution so an auditor can establish who voted and how. [Delaware General Corporation Law §212](https://delcode.delaware.gov/title8/c001/sc07/index.html#212).

Four dependencies determine what this verification establishes:

- The register keeper supplies a signed, dated eligibility snapshot. The snapshot must cover the relevant record date or voting time.
- Identity records bind signing keys to the eligible people or offices. Key compromise remains an identity problem.
- An accepted time source supports notice and deadline checks.
- Each signature binds the motion and exact specification, including the relevant request context.

Given those inputs, the verifier can establish that the attestations satisfy the encoded procedure. The register keeper remains responsible for the eligibility record. Legal review remains responsible for the specification's correspondence to the governing documents. A reproducible count preserves those responsibilities and makes their inputs inspectable.

Retention matters as much as identification. A hash can identify a resolution that nobody can retrieve. Independent reconstruction requires the governing text, eligibility evidence, votes, authority records, and the interpreter needed to read them. [Programmable Institutions §6.2](https://research.momentum.inc/papers/programmable-institutions.html#retained-evidence) distinguishes successful reconstruction from missing material, unavailable keys, and restricted disclosure.

## Reuse legal review where the rule stays fixed

Governance automation draws on established methods. Process calculi and workflow models describe dependencies. Rules-as-code languages such as Catala make legal rules executable. Ricardian contracts and smart legal contract templates connect machine-readable parameters to controlling prose. Delaware permits distributed electronic databases for stock ledgers, subject to its recordkeeping and paper-conversion requirements. [Delaware General Corporation Law §224](https://delcode.delaware.gov/title8/c001/sc07/index.html#224).

The practical opportunity is to reuse a checked specification across decisions governed by the same instruments. Lawyers review the statutory defaults, the entity's documents, and their translation. An amendment triggers review of the changed specification. Each later action supplies its own current authority, facts, votes, and evidence.

An entity making hundreds of decisions under one stable set of bylaws can reuse that legal analysis hundreds of times. Decisions that require judgment still reach the responsible person. Notice still gives participants time to act. The resulting record states which rules applied, who approved, what they approved, and why the action could proceed.

## References

Clack, C. D., Bakshi, V. A., and Braine, L. (2016). “Smart Contract Templates: Foundations, Design Landscape and Research Directions.” arXiv:1608.00771.

Grigg, I. (2004). “The Ricardian Contract.” *Proceedings of the First IEEE International Workshop on Electronic Contracting*.

Hoare, C. A. R. (1985). *Communicating Sequential Processes*. Prentice Hall.

Kiayias, A., and Lazos, P. (2022). “SoK: Blockchain Governance.” *Proceedings of the 4th ACM Conference on Advances in Financial Technologies*.

Merigoux, D., Chataing, N., and Protzenko, J. (2021). “Catala: A Programming Language for the Law.” *Proceedings of the ACM on Programming Languages*, 5(ICFP).

Milner, R. (1989). *Communication and Concurrency*. Prentice Hall.

van der Aalst, W. M. P. (1998). “The Application of Petri Nets to Workflow Management.” *Journal of Circuits, Systems and Computers*, 8(1), 21–66.
