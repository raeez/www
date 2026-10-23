# Asset and capital adaptations: handoff

22 October 2026. Prepared in publication/20261022-www-assets, baseline a0d011c46811837a7f5fb1d1aa60cd457b68dd00. Only the two assigned Markdown files are deliverables. No HTML, CSS, index, feed, template, compiler, research source, or publication change was made. The parent owns rendering and release.

## Metadata

The exact metadata proposal is in `metadata.json`. Preserve both source titles. Both visible research pages identify April 2026. Their JSON-LD date of 2026-04-02 is a generic Makefile fallback, not evidence of an original publication day. No exact day is proposed.

## The Asset Virtual Machine

**Input:** `/Users/raeez/centcom-worktrees/www-curation-20261022-publication/materials/raw/2026-10-22-author-essay-sources/smart-asset-vm.md`.

**Source SHA-256:** `1b03b04f19f6dcf438916701c367a31ae59361195cbddbfef870718c6898a765`.

**Output:** `content/author-essays/smart-asset-vm.md`.

**Output SHA-256:** `57ba7861cb34c9d9b00834430d61df9fe00cc0f4151b58a8c9f3da73ab0033c1`.

Full source read completed. Diagnosis preceded adaptation in `DIAGNOSIS.md`. The essay keeps the issuance/transfer example and explains what the asset record must retain so holders, institutions, and examiners can follow the decision. Numbered specification sections become an argument about institutional decisions and execution evidence. No deployment, adoption, throughput, or implementation-completeness claim is introduced.

| Frozen source anchor | Retained content and exact delta |
|---|---|
| I, lines 13–23; II, 27–35 | Ordinary token restriction mechanisms and the share issuance/transfer example remain. Universal claims about other standards' missing evidence are removed. Current primary ERC sources support the narrower account. The elementary mechanisms are identified as established. |
| III, 39–47 | All five descriptive compliance statuses remain. They are separated from Op's closed Admit/Reject/Pending execution decision. Pending cannot enter the admitted branch. Applicable exemptions and non-applicability retain their evidence and scope. |
| III, 45; V, 83–91 | Every durable business write belongs to the parent runtime. Temporary computation prepares a request. Gate digests bind to the asset record, all required gates must admit before business logic, and the invocation receipt binds those gate receipts. No program-owned durable storage bypass remains. |
| IV, 51–79 | The illustrative prices, 10,000,000 budget, minimum charge 2, 10,000/100,000 exclusion examples, and 500 reads versus 50 requests remain. The bound is 5,000,000 charged steps, with recording handled separately. The 5,000 storage charge is explicitly additive to the 100,000 institutional-write request charge for a durable storage change. This is an illustrative reconciliation with parent-controlled writes, not a calibrated Op schedule. The original 5,000,001 all-instruction assertion remains in the frozen source rather than being repeated as a current result. |
| VI, 95–113 | Failure receipts, program/context/evidence binding, before/after storage records, log entries, predecessor chain, operator signatures, external commitments, uncommitted tail, and transaction-specific inclusion remain. Hashes and signatures establish integrity and attribution. Deterministic replay checks computational conformity. A committed head alone cannot prove external execution or completeness. |
| VI, 115–117; Limitations, 127–133 | Human approval binds the action, approvers, threshold, deadline and saved computation. Approval expiry needs clock/service processing. Provider waits require an authenticated outcome and cannot complete on timeout. Repeat delivery cannot resume the same continuation twice. Per-run budgets allow infinitely many separately authorized resumptions. Faithful rule compilation and evidence provenance remain explicit at their mechanisms. |

**Current formal passages used:** Op `op.tex` 257–324 (compensation), 430–541 (deferred writes and suspension), 726–889 (epochs, authority at use, failure), 916–1012 (append-only responses and provider evidence), 2314–2487 (replay), and 2755–2848 (VM interface). SVM `sovereign-virtual-machines.tex` 14229–14379 supplies the stronger finite-active-interval contract: fixed positive minimum charge, nonincreasing budget, local progress, well-founded administrative steps, terminating receipt reserve and implementation refinement. The essay explains these as runtime requirements and gives no wall-clock or eventual lifecycle guarantee. No new mathematical repair is supplied.

Declared rights, custody authority, and the exact proposed action are aligned with One Entity `one-entity-in-many-jurisdictions.tex` 305–446. The provider explanation retains refusal, partial performance, outstanding balances, execution closure, revocation and compensation as distinct facts under the Op passages above.

**Canonical research links:** `https://research.momentum.inc/papers/op.html` and `https://research.momentum.inc/papers/one-entity-in-many-jurisdictions.html`. SVM is unpublished and receives no invented public URL.

**Targeted boundary check:** Found and corrected the digest/actual-execution overclaim, missing all-gates-admit condition, and overlapping gas categories. Also made parent dispatch, once-only continuation consumption, and before/after storage evidence explicit.

**Remaining limits:** The gas figures remain illustrative. The asset essay specifies desirable behavior without asserting a conforming deployment. Law translation, current evidence, provider authority and performance, durable recording, and implementation refinement remain dependencies at the corresponding mechanisms.

## Capital as a Compliance Problem

**Input:** `/Users/raeez/centcom-worktrees/www-curation-20261022-publication/materials/raw/2026-10-22-author-essay-sources/capital-layer.md`.

**Source SHA-256:** `aad0d73844043e796e559e884f5de53b1370538cde64e79f420d78ad7cb08279`.

**Output:** `content/author-essays/capital-layer.md`.

**Output SHA-256:** `c93474ae83530367c1fc66584b9dbbefe600a50b77d276d04ece9c736e8b05af`.

Full source read completed. Diagnosis preceded adaptation. The essay's payoff is that every capital decision uses a defined instrument, action, rights record, and exact quantity history. It preserves the complete activation matrix and the practical recordkeeping argument, while placing law and authority at the action they govern.

| Frozen source anchor | Retained content and exact delta |
|---|---|
| Conservation system, 25–37 | Conservation at each update, reservations, holdings totals, option pools, exact values, fully diluted convention and unresolved contingent lines remain. Cap-based dilution is a declared projection requiring the contractual inputs, not a claim that a valuation cap alone fixes a share count. Exact fractions and rounding are stated where they matter. |
| Taxonomy, 41–47; Lifecycle, 51–57 | Closed known instrument types, rejection/suspension of unclassified instruments, typed lifecycle, explicit handling of frozen states, totality versus correctness, and schedule-derived vesting remain. The time-based example is bounded to its terms; milestone evidence and authorized amendments are made explicit. |
| Transfer log/ownership graph, 61–77 | Append-only history, typed reversal, current positions, attested ownership, threshold closure and distinct inferred-control evidence remain. Timed circular-flow analysis uses event history and recognizes corrections, rather than treating a current holdings graph as a complete movement history. OFAC ownership and control statements link to their primary FAQs. |
| Corporate actions, 81–89 | Splits, dividends, authorized capacity, per-class changes, effective times and governing approvals remain. Current One Entity's 100-share, 40%-residual, 10-unit-priority example adds the exact distinction among title, participation, votes and account authority. Current AOT supplies action admission, funding and external receipt boundaries. |
| Multi-domain evaluation, 93–129 | All eleven activation rows are text-identical to the frozen source. The profile remains representative and jurisdiction-dependent. The five descriptive statuses and counterparty-domain count remain. The section 83(b) timing example is tied to transfer, with its qualifying conditions and primary IRS source. |
| Multi-domain evaluation, 119–125 | The sanctions-only record-write rule is not presented as general transaction permission. Authorization, current execution authority, and recording an already-effective event are separated. Ratification, rescission, filing and tax remedies retain their own conditions. Sanctions ownership, strict liability and scoped nullity/relief examples remain, without the source's universal assertion that every other domain is party-curable. A prohibited or unresolved current action cannot proceed merely because a remedy exists. |
| Fund dimension, 133–139; Forward compatibility, 143–147 | Fundraiser, investment and capital-call lifecycles remain, including partial payment, refund, cancellation, conserved amounts and classification before first use. Closing or refusing an execution process does not erase an outstanding duty. |
| Closing and limitations, 151–161 | Exact records make decisions checkable. They do not independently establish the correctness or completeness of law, authority or evidence. Qualifications now occur at the mechanisms instead of repeating an opening/closing disclaimer block. |

**Current formal passages used:** One Entity `one-entity-in-many-jurisdictions.tex` 305–525 (distinct rights and exact action; retained entitlements through corporate actions) and 591–651 (current decisions and uses). AOT `moxie/admissible-obligation-transitions.tex` 1018–1079 (corporate-action fields, Awaiting/Refused, single-record atomicity and external-funding/receipt boundary). Op passages above govern authority at use, provider outcomes, partial performance and compensation.

**Canonical research links:** `https://research.momentum.inc/papers/one-entity-in-many-jurisdictions.html`, `https://research.momentum.inc/papers/moxie/admissible-obligation-transitions.html`, `https://research.momentum.inc/papers/op.html`.

**Primary source checks:** OFAC FAQs 398 and 401; OFAC's US/UK authority comparison for civil strict liability; 31 C.F.R. §594.202 in the official 2025 CFR edition (scope and relief conditions); Delaware General Corporation Law §204; IRS Revenue Procedure 2012-29; and the Open Cap Table Format architecture. The official CFR source agrees with the current legal-text page inspected. No legal or commercial facts are inferred from a missing repository record. No financing or deployment result is added.

**Remaining limits:** The matrix is a representative activation profile, not a statutory rule set. Each domain still needs applicable law, authoritative interpretation, exact rights, evidence and current authority. The essay does not assert universal legal validity, authority to dispense with a missing condition, or production implementation.

## Verification and custody

- Both frozen sources still match the corresponding current research Markdown bytes at handoff. `static-checks.json` records input/output hashes and the comparison.
- One H1 per article; original titles retained; no source author/date boilerplate in the bodies.
- Eleven capital matrix rows match the source exactly. Both tables parse through Pandoc. Three inline mathematical nodes parse in the asset essay.
- Pandoc Markdown-to-native checks exit 0 with no diagnostics. No HTML was generated in this lane.
- Private-path/closed-ecosystem and external-document wording scans have zero hits. A sentence-length scan has no descriptive sentence above 25 words after Markdown links are normalized. These scans do not certify legal or controlled-language correctness.
- All 13 distinct final URLs return HTTP 200. Both explicit fragments resolve. `link-evidence/results.json` records fetched bytes, hashes and the captured sources. The two external GitHub links identify public ERC proposals, not ecosystem repositories.
- `formal-owner-hashes.json` records the exact inspected formal sources. Original source references and dated editions remain intact in the frozen custody set.
- Render integrity and index/catalogue parity remain the parent's explicit responsibility. No browser or local-file workaround was used.

**Staging:** only `content/author-essays/smart-asset-vm.md` and `content/author-essays/capital-layer.md` are staged. Index hashes match the worktree. Staged whitespace check passed. Reports and RESUME remain unstaged. No commit or push.
