# Hybrid Post-Quantum Signatures — adaptation report

## Custody and full read

Starting source: `/Users/raeez/centcom-worktrees/www-curation-20261022-publication/materials/raw/2026-10-22-author-essay-sources/hybrid-post-quantum-signatures.md`.

Source SHA-256: `29a23989c629ce0f5186b4fe7b3edb2d5ba9055806fb3be9a2003e524f90fc49`.

The complete frozen source, all its references, complete related/Lambda matrix, corpus disposition, and applicable brief/policies were read. Diagnosis was recorded before drafting in `diagnosis.md`. Current research Markdown matches the frozen source byte-for-byte after the final check. The original document remains intact.

The current research owner passage was read at `papers/sovereign-jurisdiction-network.tex`, “Cryptographic continuity and trust boundary,” lines 1842–1852. Its full source hash is `17644b7f815f1cff425816addc82e01267355050e78db9a1f1e28beacd30c77f`. Current publication HTML contains the cited anchor. The unpublished Dependency-Scoped Agreement passage was checked independently as context, not linked as a public successor.

## Argument and reader payoff

A long-lived record needs protection that can survive an algorithm's retirement. The essay explains why different assumption classes and timely renewal matter, shows their exact byte cost, and identifies the custody work an institution must retain. The opening states the need directly. Qualifications appear beside the construction, parameter choice, or renewal procedure they constrain.

## Preservation and precise differences

- Source §§1–2 → “A signature has to survive its retention period”: thirty-year horizon, 2026/2040 attestation example, quantum threat and original-attester/evidence obstacles retained. Contested quantum arrival dates and blanket claims about institutional deployment were omitted. Literal “unbounded time” became an attacker retaining records while gaining stronger capabilities.
- Source §3 and SJN §8.8 → “Require every component to verify”: same canonical encoding, suite tag, all-three acceptance, secure signer/key binding, correct verifiers, one surviving unforgeable component, cited pairwise combiner, and stronger-property boundary retained. The author essay supplies no new theorem or proof. The source's unverified attribution of key-substitution analysis is not repeated.
- Source §§3–4 → “Why include a hash-based signature”: elliptic-curve/module-lattice/hash assumptions, Module-LWE and self-target module-SIS family, hash properties, idealized model, category 1 versus 3, 16-byte target caveat, qualified generic Grover estimate, and category-5 alternative retained. “All internal outputs” was narrowed to principal chaining and PRF values. The generic search estimate is expressly not a full-scheme measured forgery cost. “No collision resistance” became the bounded statement that a generic SHA-256 collision alone does not supply the analyzed forgery.
- Source §§4–5 → “The cost is explicit”: all signature and public-key lengths retained in a compact table; raw-field overhead made explicit. SHA2-128f 17,088 and SHA2-256s 29,792 retained. Fixed signing/verification times and 10–100 ms database timings lacked named benchmarks and were omitted. The workload comparison and need to measure a deployment remain.
- Source §§6–7 → “Renew the evidence while it is still trustworthy”: re-anchoring versus re-evaluation, original record retention, timely renewal, witness-chain custody, verifier availability and cryptanalytic-failure scheduling retained. RFC 4998 §5 supplies the missing distinction between timestamp renewal and hash-tree renewal. An old weakened digest is not made sound by another signature.
- Source §7/SJN §8.8 → appropriate paragraphs retain whole-environment compromise, side channels, confidentiality, legal authority, attestation truth and evaluator correctness as separate obligations.
- Repetitive abstract/conclusion and historical attack anecdotes were condensed. The complete historical note remains research background. No independent specification, theorem supersession, implementation claim, or source deletion was introduced.

## Metadata

Title: Hybrid Post-Quantum Signatures.

Subtitle: Keeping institutional records verifiable as cryptographic schemes age.

Description: A design for signing long-lived records under different cryptographic assumptions and renewing their protection over time.

Display date: April 2026. This is a source-era attribution, accepted by the parent. The frozen Markdown is undated. Earliest followed Markdown record is 11 April 2026; earliest HTML record is 14 April 2026. Generated `datePublished=2026-04-02` comes from the generic Makefile fallback and does not establish the original publication day. Exact original publication date remains unknown. The current essay adaptation is dated 22 October 2026 in internal metadata only.

## Canonical and primary references

- https://research.momentum.inc/papers/sovereign-jurisdiction-network.html#cryptographic-continuity-and-trust-boundary
- Bindel et al., §4.1: https://www.douglas.stebila.ca/files/research/papers/PQCrypto-BHMS17-full.pdf
- RFC 8032; FIPS 204 Table 2; FIPS 205 Table 2/§11: component values checked against primary sources.
- RFC 4998 §§1.2,5: renewal boundary checked against primary text.
- SPHINCS+ 2019 framework and Hülsing/Kudinov 2022 proof: authoritative indexed records verify the exact linked papers. Direct web fetching returned 502 and 403 respectively; this is a retrieval limitation, not evidence that the URLs are absent.

## Verification and remaining work

Focused independent security comparison found no material semantic blocker. Static checks parsed the complete Markdown with Pandoc, confirmed one first H1, checked every research path/fragment against current publication HTML, found no private-path or process-metadata disclosure, and reconfirmed frozen/current source equality. `static-checks.json` retains machine-readable results. No browser workaround or HTML/CSS edit was used. Parent retains rendering, layout QA, metadata integration, commit, push and publication.

Final essay SHA-256: `94ade4d568c68f55ab7897a3d681b8b02a6829b338d7dce1ad2d25945996f0b2`.
