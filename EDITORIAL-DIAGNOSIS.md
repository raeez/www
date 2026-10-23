# Archai editorial diagnosis — 22 October 2026

## Sources and scope
Baseline a0d011c46811837a7f5fb1d1aa60cd457b68dd00. Full archai.html article read, including contents, disclaimer, lists, definitions, equations, roadmap and glossary. Body SHA-256 source recorded in RESUME. Venue samples read: beauty.html, devfinance.html, prefabricated-construction.html. These samples establish differing narrative and technical registers without an authorship inference. Target: direct technical design prose, preserving the June 2025 design status.

## Argument and question sequence
1. Thesis: which ownership and coordination problems does Archai address, and which existing components enable it?
2. Problem: how do capital barriers, rent incentives, opaque data and collective decisions obstruct housing?
3. Principles: which legal, financial, compositional, evidence and governance constraints must the design obey?
4. Model: what is a vault, which rights are separable, and which community rules can vary?
5. Architecture: what do legal entities, contracts, governance, the Commons, evidence and arbitration each do?
6. Economics: why would residents and capital providers lock capital, how does equity accrue, and how is surplus allocated?
7. Exit: how can maturity redemption, bounded transfer and cross-vault portability preserve solvency and constrain speculation?
8. Governance: who controls local, financial and legal decisions, and which rules constrain them?
9. Legal integration: how do Mass primitives, jurisdiction modules and attestation streams support compliance?
10. Risk: what can fail, which controls address it, and who underwrites losses?
11. Tokens: which rights belong to vault assets and $ARCH, and what legal conditions constrain each?
12. Delivery: what does each of five phases build?
13–14. Diagram and glossary consolidate the specified flow and definitions.
The sequence is dependency-led and appropriate for this design paper. Keep it. The TOC repeats headings by function, not rhetorical padding.

## Quoted defects before revision
- Thesis density/abstraction: “ownership rails are archaic”, “capital + governance substrate”, “the missing enabling stack”. Replace wrappers with ownership processes and defined mechanisms.
- Rhetorical negation: “Archai is not ‘a village.’”; “not a ‘crypto project’”; “the legal wrapper is not paperwork”; “not ‘governance vibes’”. State the positive technical proposition while preserving real exclusions.
- Posture: “institutional physics”, “Transaction costs are brutal”, “speculative casino”, “the sacred object”, “real, not crypto-theater”, “network moat”. Replace with direct descriptions.
- Editorial residue: “This section closes the biggest gap in v0.1”; “The whitepaper must explicitly model this”; “But here we refine toa safer”; “We add one missing bucket”; “We make this enforceable”; “The correct framing”; “Make it concrete”; “we sharpen it”. Convert to standalone design statements without promoting proposed values to settled terms.
- Complexity: “programmable rails to automatically form and maintain … programmatically”; “programmable legal stacks / SEZ modules”; “real institutional layer”. Replace repetition and slash constructions where semantics permit.
- Unclear sentence: “SEZ Legal Stack implements: Smart should generate …”. Restore the existing Smart Asset subject from the immediately surrounding design, retaining ‘should’ requirement status.
- Mechanism buried in rhetoric: “If you promise instant liquidity, you’re lying”; “This is not anti-user; it is solvency”; “Trustees are not ‘centralization’”. Preserve liquidity and legal constraints with concrete subjects.
- Repeated meta-headings: “(crucial)”, “(clean segmentation)”, “from first principles”, “(principles, not arbitrary numbers)”, “(minimal)”. Remove commentary while keeping heading destinations and TOC alignment.
- Rhythm: most prose is already brief and interspersed with genuine enumerations. Avoid artificial variation or new anecdotes. Join only where it expresses a real dependency.

## Preservation requirements
Retain historical date; disclaimer; all proposed percentages and terms; every list member, equation byte, variable, cap and qualification; all legal status cautions; named entity examples and quotation text; citation destinations, IDs, assets, styles and scripts. Load-bearing negatives include no occupancy rights, non-transferability, finite caps, legal exclusions, and governance prohibitions. Do not fact-update June 2025 claims or invent proof.

## Coverage
Diagnosis complete before edits. Edits, whole reread, changed-claim review, syntax/assets/numeric invariants and visual inspection pending.

## Holistic composition refinement — before second pass
The entire initial revision has been reread. Central question: how can people acquire durable use and ownership of property while vaults remain solvent, legally enforceable and resistant to speculation? The tension is real: residents need access and exit while land is illiquid; capital providers need return while the design limits appreciation capture. The strongest existing delivery is the original dependency order, with concrete transitions instead of restatement. Major section movement would introduce definitions later than their use; retain the architecture.

### Dependencies and recurring themes
- Legal enforceability: §1 introduces programmable rights; §3 makes enforceable rights a requirement; §4 pairs contracts with a legal holder; §5 assigns title, service and protocol duties; §9 explains jurisdiction-specific implementation; §11 bounds the resulting financial instruments. Each return narrows from principle to authority to legal treatment.
- Use and ownership: §1 introduces staking and earning; §2 establishes exclusion; §4 defines separable rights; §6 prices the stake products and equity accrual; §7 governs exit; §11 identifies token forms. Keep definitions before economics and token forms after legal conditions.
- Anti-speculation: §2 explains current incentives; §3 names required constraints; §4 makes rights separable; §6 specifies returns; §7 sets transfer and pricing rules; §8 limits the authority to change those rules. Revise the §6–8 transitions so the reader follows return, exit, then control.
- Evidence: §2 explains opacity; §3 requires private verifiable compliance evidence; §5 identifies operating data and compliance streams; §6 uses audited/attested NAV; §8 requires evidence for decisions; §9 identifies regulator checks; §10 uses data in appraisal and underwriting. §5 and §9 must emphasize different audiences and purposes.
- Commons/underwriting: §5 assigns the treasury and proposed fee; §6 shows surplus source and reserves; §7 sends excess transfer premium to Commons; §10 specifies first-loss cover, staking pools and risk premiums; §11 scopes token participation. Retain both proposed 5–10% returns because one describes architecture and the other the allocation.
- Governance: §3 constrains decentralization; §4 parameterizes each model; §5 names role/scope; §8 allocates decisions and establishes immutable limits; §9 governs legal-module migration; §11 handles protocol-level upgrades. Replace vague repeated affirmations with the purpose specific to each return.
- Roadmap: §12 takes the preceding design from one complete vault to a network, shared underwriting, jurisdiction modules and user interfaces. Appendices consolidate without adding a fresh argument or generic conclusion.

### Specific composition actions
Make §4 open by binding the model to requirements; connect capital rights to return in §6, return to exit in §7, exit policy to decision rights in §8, legal design to residual failure modes in §10, and underwriting role to token distinctions in §11. These connections must use only facts already explicit in the manuscript. Keep the technical lists: they enumerate real distinct rights, risks, controls and phases. Remove initial-proposal origin notes where empty, but preserve numeric proposal status and exact attributed quotations.

## Final Archai coverage and acceptance
Complete source and revised whole-manuscript reads performed, including every section and transition. The final argument preserves the dependency order above. Repeated legal, evidence, governance, liquidity and underwriting ideas acquire the distinct roles recorded in the recurrence map. All changed prose claims reviewed against source through the change ledger and paragraph-level unified diff. Corrections removed an accidental restriction to financial rights in §2.4, whole-formula proportionality in §6.3, unintended legal priority in §3.1, return-as-exit-requirement in §7, narrowed control scope in §10, loss of design qualifier in §5.5, and an added investment qualification in §6.2.

Focused verification: HTML parser; ordered markup/attributes comparison (permitted differences: six br removals and 65 restored pre-existing TOC target IDs); JSON-LD parse; byte-equivalent styles/scripts/formula blocks and source quotations; all href strings unchanged; all local and fragment links resolve; unique IDs; required public-source scan zero hits; git diff --check passed. Exact figures and historical dates preserved. Metadata changes separately: one Version 0.2 label removed, twelve v0.1 process references replaced by initial-proposal wording with status retained, per accountable owner decision under external-document policy.

Source dependencies: compiler/docs.config.js maps Archai to Google Doc 12TriV64rqMidmlzEXU5HdvbhpX_Fu4bNq5UUo7-125I. Root HTML was the assigned source surface. Compiler refetch would overwrite these edits; Google Doc and feed are outside this lane, with feed integration assigned to the accountable owner. Titles and routes are unchanged.

Residuals: no publication performed. Visual inspection was blocked, not passed. Exact tool diagnostic: “Browser Use rejected this action due to browser security policy. Reason: The browser URL policy blocks this action. Browser use cannot visit the requested page because its URL is blocked by the Browser use URL policy. The agent must not attempt to achieve the same outcome via workaround, indirect execution, raw CDP or browser commands, alternate browser surfaces, or policy circumvention. Proceed only with a materially safer alternative that does not require this blocked browser action; if none exists, stop and request user input.” No alternate route attempted. Inherited wrapper July 2025 vs manuscript June 2025 dates preserved. Duplicated Unicode/plain-text equation payloads and unused beta parameter preserved; mathematical repair was not authorized. Dated external deployment/legal assertions were retained, not independently verified.

Final scope check restored the exact encodes relationship (§2.4), project-is-Vault identity definition (§4.1), and the distinction between incentives generally and finite subsidies (§11.2).
