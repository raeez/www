# Hybrid Post-Quantum Signatures

Author: Raeez Lorgat

---

A compliance record signed today must be verifiable in thirty years. Corporate charters, securities filings, and regulatory attestations depend on that continuing ability to authenticate the record. A sufficiently large quantum computer running Shor's algorithm could forge signatures in general institutional use, including signatures on historical records. The retained archive supplies the public keys and messages needed for such forgery.

This paper gives the design rationale for a hybrid signature that combines Ed25519, ML-DSA-65, and SLH-DSA. This AND composition requires every component to verify, and its three schemes rest on unrelated hardness assumptions. The composite remains existentially unforgeable as long as any one component does, by a combiner theorem cited here without proof. The analyzed instantiation produces an 11,229-byte signature. Its hash-based component uses a conservative assumption class at NIST security category 1, below the lattice component's category 3.

The construction also uses re-anchoring: appending a fresh witness over an old record under a successor scheme while the old one remains sound. Together, hybrid signing and re-anchoring allow signature-scheme retirement through scheduled maintenance. The need to preserve records before a quantum computer can forge them motivates deployment now.

## 1. Evidence with a thirty-year horizon

Most software systems use signatures for immediate authentication, after which an hour-long session ends and the signature can be discarded. Institutional infrastructure retains signatures as evidence that a board resolution was authorized, a compliance evaluation occurred, or a sanctions check returned clean. A tribunal established decades later may have to verify that evidence under rules adopted after the signing date.

Thirty years is longer than many deployed primitives have lasted. DES, MD5, SHA-1, RC4, and 512-bit RSA each entered and left service inside such a window. Archival signatures must therefore remain sound when some of their cryptographic assumptions fail during the retention period.

## 2. Threat model

RSA, ECDSA, and Ed25519 signatures rest on the hardness of factoring or computing discrete logarithms. Shor's algorithm solves both in polynomial time on a sufficiently large quantum computer (Shor, 1997). Contested estimates place such a machine ten to thirty years away, within the horizon over which institutional records must remain valid. Post-quantum deployment has begun: NIST SP 800-208 (2020) standardizes stateful hash-based signatures for firmware signing, and ML-DSA is entering protocol stacks. Institutional records still overwhelmingly use pre-quantum signatures, including RSA and elliptic-curve schemes.

The adversary we defend against holds the public archive and unbounded time. New records can use successor signature schemes, but existing records retain signatures under the schemes used when they were created. Forgery against a signature scheme requires only the public key and a target message, both of which an institutional archive retains indefinitely. The archive itself is therefore the attack surface. This is the signature analogue of harvest-now-decrypt-later, with no need for interception because the system deliberately retains the records. For institutional retention periods, "later" falls within the period in which the evidence must remain verifiable.

A compliance record signed in 2026 with Ed25519 attests that a specific entity passed a specific sanctions check on a specific date. The signature binds the attestation to the attester. If Ed25519 fails in 2040, an adversary can forge that historical signature as well as future ones. After fourteen years, the signature alone can no longer establish authenticity. The adversary can also produce a different record, bearing a valid signature from the same key, that attests to an arbitrary claim.

Mosca's inequality relates the retention period, migration time, and time until a cryptographically relevant quantum computer (Mosca, 2018). Some records are exposed if the retention period plus migration time exceeds the time until that computer exists. Both terms on the left are measured in decades here.

Three exposures are out of scope. Compromise of a signing key defeats any signature scheme and requires operational custody controls. Implementation side channels are independent of scheme choice. Confidentiality requires separate protection against harvest-now-decrypt-later attacks on encrypted records. This paper addresses the continued authenticity of archival evidence.

## 3. The hybrid construction

NIST has standardized two post-quantum signature families. FIPS 204 specifies ML-DSA (formerly Dilithium), a module-lattice scheme, and FIPS 205 specifies SLH-DSA (formerly SPHINCS+), a stateless hash-based scheme. Code-based and multivariate signatures remain under evaluation in NIST's additional-signature process. During the competition, classical attacks defeated candidates with rich algebraic structure, including one finalist (Section 4). The two standardized families have different mathematical foundations, performance, and risk profiles. Retaining the classical scheme and adding one from each family gives the construction three distinct sources of security.

A hybrid signature is an AND composition. Fix the component schemes, here Ed25519, ML-DSA-65, and SLH-DSA-SHA2-128s, and assign a name to the suite. Encode the record with a tag naming the suite in force. Sign that same encoding once with each component key. The composite verifies only if every component signature verifies against that encoding.

Because every component signs the suite tag, a signature made under one suite cannot be presented as a signature made under another. The tag also identifies the components required by the verification policy in force when the record was signed. This policy lookup supports the retirement procedure in Section 6.

Forging the composite requires forging every component, so the combiner remains existentially unforgeable if any one component does. Bindel, Herath, McKague, and Stebila (2017) prove this for two components through their concatenation-combiner theorem. Iterating the pairwise combiner gives the three-component statement. We cite this reduction without proving it here. Their framework also treats key-substitution attacks and non-separability, neither of which is claimed here.

Ed25519 supplies fast, compact signatures and a longer record of public cryptanalysis than the post-quantum components. Public analysis began in 2011, building on Curve25519 from 2006 (Bernstein, Duif, Lange, Schwabe, and Yang, 2012). Retaining it preserves that classical security alongside the newer schemes. The hybrid requires at least one of the three algorithms to remain secure.

The two post-quantum families depend on different assumptions. ML-DSA-65's unforgeability rests on Module-LWE and a self-target variant of the module short-integer-solution problem (Ducas, Kiltz, Lepoint, Lyubashevsky, Schwabe, Seiler, and Stehlé, 2018). Both are module-lattice assumptions. No efficient quantum algorithm is known for either, but both are algebraic and have less history of study than the problems they replace.

SLH-DSA depends on properties of a hash construction built from SHA-256. It needs multi-target and truncated-output variants of the properties used elsewhere in deployed cryptography. These remain assumptions about a well-studied compression function's resistance to generic attack, without an algebraic problem or trapdoor. A thirty-year archive needs at least one component in that assumption class.

## 4. The hash-based anchor

Lattice-based cryptography depends on the difficulty of exploiting the structure of a lattice, ring, or module. Earlier attacks show how algebraic structure can reduce security margins.

The number field sieve exploited the ring structure of algebraic number fields. It reduced factoring cost from the quadratic sieve's L[1/2] to L[1/3], which drove key sizes from 512 to 3,072 bits. This did not break RSA outright. RSA-250, at 829 bits, is the factoring record (Boudot, Gaudry, Guillevic, Heninger, Thomé, and Zimmermann, 2020), and RSA-2048 remains unbroken classically. Shor's algorithm solves the elliptic-curve discrete-logarithm problem once a cryptographically relevant quantum computer exists.

The post-quantum competition supplied further examples. A classical key-recovery attack defeated SIKE, an isogeny-based alternate candidate, in about an hour on a single core (Castryck and Decru, 2023). Rainbow, a multivariate signature finalist, fell to a key-recovery attack running over a weekend on a laptop (Beullens, 2022). Whether module-lattice structure remains secure is open, so an institutional archive needs an independent assumption class.

Hash-based signatures use no lattice, ring, or group structure that an attacker can exploit. SLH-DSA is a stateless hash-based scheme: a Merkle tree of one-time signatures over a few-time signature layer (FORS). Its security reduces to properties of the underlying tweakable hash construction (Bernstein, Hülsing, Kölbl, Niederhagen, Rijneveld, and Schwabe, 2019). Those properties are multi-target second-preimage resistance, pseudorandomness, and, for the FORS layer, interleaved target subset resilience. Forging a signature requires defeating one of them.

The scheme requires no collision resistance. A SHA-256 collision, the failure mode that retired MD5 and SHA-1 (Section 1), does not by itself yield a forgery. FIPS 205 standardizes the "simple" instantiations, whose security analysis uses the quantum random-oracle model. Hülsing and Kudinov (2022) found and repaired a flaw in the original tweakable-hash proof. These guarantees concern the model and do not establish the corresponding properties of concrete SHA-256.

The quantum cost depends on the scheme's exposed parameters. SLH-DSA-SHA2-128s instantiates its internal functions with SHA-256 and truncates their outputs to sixteen bytes. An attacker therefore faces 128-bit targets, despite the 256-bit digest width. Grover's algorithm gives a quadratic speedup for generic search (Grover, 1996). This speedup is optimal in the black-box model (Bennett, Bernstein, Brassard, and Vazirani, 1997).

Generic preimage search against these targets thus costs on the order of 2^64 sequential quantum hash evaluations, compared with 2^128 classical evaluations. NIST assigns security category 1, corresponding to the difficulty of quantum key search on AES-128.

The oracle optimality bound does not by itself exclude attacks that exploit the concrete structure of SHA-256. Category 1 is also the lowest standardized level. At this instantiation, the hash-based component has the most conservative assumption class at category 1, while ML-DSA-65 is category 3. A deployment requiring the hash-based component to meet or exceed that category can raise its parameter set. SLH-DSA-SHA2-256s is category 5 with a 29,792-byte signature, changing the parameters within the same construction.

The lattice-based signature supplies a fast and reasonably compact post-quantum component. The larger, slower hash-based component preserves a fallback based on the most conservative assumption class available.

## 5. Cost

An Ed25519 signature is 64 bytes. The composite above is 11,229 bytes: 64 for Ed25519, 3,309 for ML-DSA-65, and 7,856 for SLH-DSA-SHA2-128s. Its public key is 2,016 bytes, and verification rises from microseconds to low milliseconds. SLH-DSA dominates signing time. Its small-signature "s" parameter sets cost hundreds of milliseconds of CPU per signature. The "f" sets sign an order of magnitude faster at roughly twice the signature size: 17,088 bytes for SLH-DSA-SHA2-128f.

Each signer also manages three key pairs, with generation ceremonies, custody, and rotation for all three. Each verifier maintains three implementations at the exact parameter sets selected by the suite tag for the archive's lifetime.

These costs would be prohibitive for a network protocol signing every packet. The design serves institutional records: compliance attestations stored beside regulatory documents orders of magnitude larger, and ledger digests signed once per synchronization interval. It also serves audit-trail entries signed once per event, where the pipeline already commits a database transaction at ten to a hundred milliseconds. These workloads have neither high signing frequency nor tight size constraints. Eleven kilobytes and low-millisecond verification add little to their budgets.

## 6. Why migration starts now

Deferring migration until a cryptographically relevant quantum computer exists leaves years of accumulated records exposed during the migration itself. Section 2's inequality states this timing problem. For an Ed25519-only archive, re-signing under a post-quantum scheme requires the original attester, evidence, and compliance evaluation. The attester may have ceased to exist as a legal entity, and data-protection rules may have required redaction of the evidence. The rules governing the original evaluation may also have changed. These conditions make re-signing impossible for a significant fraction of an archive spanning decades.

The archival literature provides re-anchoring, which the companion Intelligent Assets paper uses in its record-custody construction. Append a fresh witness over the old record's digest, signed under the successor scheme while the retiring scheme remains sound. This preserves the historical entry and original signature without requiring the original attester. Verification uses the policy in force at signing, identified through the suite tag in Section 3. A verifier who no longer trusts the retired scheme can follow the witness chain to a scheme it still trusts.

Each generation anchors the preceding one, so the construction can recur as schemes retire. Timestamp renewal and evidence records supply this mechanism (RFC 3161; RFC 4998), as do the ETSI long-term archive profiles (ETSI EN 319 122-1, 2016).

Re-anchoring must occur while the retiring scheme remains sound, and its failure date is unknown. An Ed25519-only archive depends on one assumption. A credible weakening therefore requires emergency re-anchoring of the entire archive before an uncertain deadline.

The hybrid distributes this dependence across three unrelated assumptions. If one component fails, every record remains unforgeable through the surviving components, so the archive needs no immediate triage. The pass that retires the failed component can run as scheduled maintenance. Verification continues unchanged: the record still verifies, with unforgeability resting on the surviving components.

Each record's base security is contained in one hybrid signature block, independent of a witness chain or timestamp authority. Re-anchoring alone does not provide that independence. The hybrid still requires maintenance over thirty years as its own components retire. Each retirement requires a re-anchoring pass, which the surviving components allow operators to schedule.

Signing with the hybrid from day one protects every record at creation and avoids retroactive migration, re-signing campaigns, and gaps in the evidentiary chain. This construction works whether a cryptographically relevant quantum computer arrives in 2035, in 2045, or never. If it never arrives, the cost remains eleven kilobytes per signature. If it arrives within the retention period, the archive's evidence survives for as long as any one of the three unrelated assumptions holds.

## 7. Assumptions and limitations

**The combiner theorem is cited, not proved.** Unforgeability of the verify-all combiner reduces to the unforgeable component (Bindel, Herath, McKague, and Stebila, 2017), extended from two components to three by iteration. Key-substitution resistance and non-separability are analyzed in that framework and are not claimed here.

**The hash-based analysis lives in the random-oracle model.** FIPS 205's "simple" instantiations carry security proofs in the quantum random-oracle model, for multi-target properties over truncated outputs (Bernstein et al., 2019; Hülsing and Kudinov, 2022). The Grover-optimality bound is a black-box result and says nothing about the concrete structure of SHA-256.

**The security categories are asymmetric.** At the analyzed instantiation the hash-based anchor is NIST category 1 and the lattice component category 3. Raising the hash-based category requires larger parameters and more bytes within the same construction (Section 4).

**The operational requirements triple.** Each signer maintains three key pairs, and each archive maintains three verifier implementations at exact parameter sets for decades. Because every component must verify, a defect in any one verifier rejects valid records even when another component preserves unforgeability.

**Maintenance remains necessary.** Components retire over a thirty-year horizon, and each retirement requires a scheduled re-anchoring pass (Section 6).

**Scope.** The design serves archival records and is unfit for high-frequency signing, including network protocols that sign every packet. Signing-key compromise, implementation side channels, and the migration of encrypted data are out of scope (Section 2).

## References

Adams, C., Cain, P., Pinkas, D., and Zuccherato, R. (2001). "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)." RFC 3161.

Bennett, C. H., Bernstein, E., Brassard, G., and Vazirani, U. (1997). "Strengths and Weaknesses of Quantum Computing." *SIAM Journal on Computing*, 26(5), 1510-1523.

Bernstein, D. J., Duif, N., Lange, T., Schwabe, P., and Yang, B.-Y. (2012). "High-Speed High-Security Signatures." *Journal of Cryptographic Engineering*, 2(2), 77-89.

Bernstein, D. J., Hülsing, A., Kölbl, S., Niederhagen, R., Rijneveld, J., and Schwabe, P. (2019). "The SPHINCS+ Signature Framework." In *Proceedings of the ACM Conference on Computer and Communications Security (CCS)*, 2129-2146.

Beullens, W. (2022). "Breaking Rainbow Takes a Weekend on a Laptop." In *Advances in Cryptology -- CRYPTO 2022*.

Bindel, N., Herath, U., McKague, M., and Stebila, D. (2017). "Transitioning to a Quantum-Resistant Public Key Infrastructure." In *Post-Quantum Cryptography (PQCrypto 2017)*, Lecture Notes in Computer Science 10346.

Boudot, F., Gaudry, P., Guillevic, A., Heninger, N., Thomé, E., and Zimmermann, P. (2020). "Comparing the Difficulty of Factorization and Discrete Logarithm: A 240-Digit Experiment." In *Advances in Cryptology -- CRYPTO 2020*.

Castryck, W. and Decru, T. (2023). "An Efficient Key Recovery Attack on SIDH." In *Advances in Cryptology -- EUROCRYPT 2023*.

Ducas, L., Kiltz, E., Lepoint, T., Lyubashevsky, V., Schwabe, P., Seiler, G., and Stehlé, D. (2018). "CRYSTALS-Dilithium: A Lattice-Based Digital Signature Scheme." *IACR Transactions on Cryptographic Hardware and Embedded Systems*, 2018(1), 238-268.

ETSI (2016). *Electronic Signatures and Infrastructures (ESI); CAdES Digital Signatures; Part 1: Building Blocks and CAdES Baseline Signatures*. EN 319 122-1.

Gondrom, T., Brandner, R., and Pordesch, U. (2007). "Evidence Record Syntax (ERS)." RFC 4998.

Grover, L. K. (1996). "A Fast Quantum Mechanical Algorithm for Database Search." In *Proceedings of the ACM Symposium on Theory of Computing (STOC)*, 212-219.

Hülsing, A. and Kudinov, M. (2022). "Recovering the Tight Security Proof of SPHINCS+." In *Advances in Cryptology -- ASIACRYPT 2022*.

Lorgat, R. *Intelligent Assets*. Companion paper in this series.

Mosca, M. (2018). "Cybersecurity in an Era with Quantum Computers: Will We Be Ready?" *IEEE Security & Privacy*, 16(5), 38-41.

NIST (2020). *Recommendation for Stateful Hash-Based Signature Schemes*. Special Publication 800-208.

NIST (2024). *Module-Lattice-Based Digital Signature Standard*. FIPS 204.

NIST (2024). *Stateless Hash-Based Digital Signature Standard*. FIPS 205.

Shor, P. W. (1997). "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer." *SIAM Journal on Computing*, 26(5), 1484-1509.
