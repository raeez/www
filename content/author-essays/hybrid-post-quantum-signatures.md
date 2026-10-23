# Hybrid Post-Quantum Signatures

A board resolution signed today may need to establish who authorized an act thirty years from now. The same applies to a securities filing, a regulatory attestation, or a record of ownership. Their useful lives can exceed the lives of the cryptographic schemes that authenticate them.

An archive therefore needs a way to preserve evidence as those schemes age. I favor signing long-lived institutional records with several schemes built on different assumptions, then renewing their protection before those assumptions fail. Surviving components give the custodian time to maintain the archive.

## A signature has to survive its retention period

Consider a sanctions attestation signed with Ed25519 in 2026. Its signature binds the statement to a signing key. Suppose an attacker gains the ability to forge signatures under that key in 2040. The attacker can then produce a different statement with a signature that also verifies. The original signature alone can no longer distinguish the authentic record from the forgery.

A sufficiently large quantum computer running Shor's algorithm would threaten RSA and elliptic-curve signatures, including Ed25519. An attacker can retain public records and acquire stronger computational capabilities during their retention period. The archive supplies the messages and public keys.

The relevant deadline depends on how long the evidence must last and how long migration takes. A prediction of the year in which a quantum computer arrives would add little certainty. A thirty-year retention obligation already requires planning for changes in cryptographic assumptions.

Moving new records to a successor scheme leaves the old records to maintain. Their original attester may have dissolved, their supporting evidence may have been lawfully deleted, and their governing rules may have changed. Repeating the original evaluation can become impossible. Preserving the evidence of that evaluation needs its own procedure.

## Require every component to verify

The construction combines Ed25519, ML-DSA-65, and SLH-DSA-SHA2-128s. These supply a classical elliptic-curve signature, a module-lattice signature, and a stateless hash-based signature.

Each component signs the same canonical encoding of the record. That encoding includes a suite tag naming the algorithms and parameter sets. A verifier accepts the composite only when every component verifies. Signing the tag binds the record to its chosen suite and prevents its presentation as a record signed under another suite.

Forging the composite requires defeating each component. The concatenation theorem of [Bindel, Herath, McKague, and Stebila](https://www.douglas.stebila.ca/files/research/papers/PQCrypto-BHMS17-full.pdf), §4.1, supplies the two-component unforgeability result. Applying that construction twice gives the three-component argument. It depends on a component remaining unforgeable against the relevant adversary, secure binding of the keys to the signer, and correct verification. Stronger properties, including resistance to separating the components for another use, need their own analysis.

A cryptographic break of one component can leave the composite protected by another. A faulty verifier can still reject authentic records because acceptance requires all components. An archive must preserve both its security assumptions and its ability to perform the specified checks.

The [cryptographic profile in *The Sovereign Jurisdiction Network*, §8.8](https://research.momentum.inc/papers/sovereign-jurisdiction-network.html#cryptographic-continuity-and-trust-boundary) sets out this boundary. Signatures authenticate statements under their key-binding assumptions. The issuer's legal authority, the truth of its statement, and the correctness of its evaluation require separate evidence.

## Why include a hash-based signature

Ed25519 retains a mature classical component. ML-DSA uses module-lattice assumptions. Its analysis rests on Module Learning with Errors and a self-target variant of the module short-integer-solution problem. The hash-based component gives the archive a different basis for continued authentication.

SLH-DSA builds signatures from hash constructions rather than a lattice or an algebraic trapdoor. Its underlying SPHINCS+ analysis uses multi-target second-preimage resistance, pseudorandomness, and interleaved target subset resilience for its few-time signature layer. These are specific cryptographic assumptions. A generic collision in SHA-256 alone does not supply the forgery described by that analysis. The [SPHINCS+ framework](https://sphincs.org/data/sphincs%2B-paper.pdf) and [the repaired security proof](https://eprint.iacr.org/2022/346.pdf) give the relevant models.

The parameter choice matters as much as the family name. SLH-DSA-SHA2-128s uses SHA-256 with sixteen-byte values for its principal chaining and pseudorandom-function outputs. The SHA-256 name therefore does not imply 256-bit targets throughout the scheme. For an idealized 128-bit preimage target, Grover search takes on the order of $2^{64}$ quantum oracle evaluations. That estimate concerns generic search, not a measured attack on the complete signature scheme. Black-box optimality also leaves attacks on concrete hash structure outside its conclusion.

NIST places this hash-based parameter set in security category 1, while ML-DSA-65 is category 3. Category 1 is the lowest standardized category. An archive that requires the hash-based component to reach a higher category must choose larger parameters. SLH-DSA-SHA2-256s reaches category 5 and uses a 29,792-byte signature. [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) specifies these choices.

The hash-based analysis uses an idealized hash model, including quantum random-oracle analysis for the standardized simple construction. That model is distinct from a proof of the corresponding properties of concrete SHA-256. The engineering judgment is to retain different assumption classes while keeping each one's parameters and limits visible.

## The cost is explicit

The component sizes give a useful starting point for an archive budget:

| Component | Signature bytes | Public-key bytes |
| --- | ---: | ---: |
| Ed25519 | 64 | 32 |
| ML-DSA-65 | 3,309 | 1,952 |
| SLH-DSA-SHA2-128s | 7,856 | 32 |
| Total | **11,229** | **2,016** |

These are raw component fields. Suite tags and envelope encoding add overhead. [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032.html), [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), and FIPS 205 specify the component lengths.

The smaller-signature SLH-DSA parameter sets spend more work on signing. The faster SHA2-128f option uses 17,088 signature bytes. Actual signing and verification times depend on the implementation and hardware, so the archive must measure its own workload.

For records retained beside substantial legal documents, eleven kilobytes can be an acceptable cost. Signing each network packet presents a different budget. Event frequency, retention volume, latency requirements, and the cost of signature renewal determine whether the construction fits.

The continuing operational cost deserves equal attention. A signer maintains three key pairs, including their generation, custody, rotation, and eventual retirement. A verifier maintains three implementations at the exact parameter sets named by historical records. Compromise of the complete signing environment defeats this diversity. Side-channel protection and encrypted-record confidentiality remain separate requirements.

## Renew the evidence while it is still trustworthy

Re-anchoring appends a fresh witness under a successor scheme while the earlier evidence remains trustworthy. It preserves the original record and signature. The new witness attests to the retained evidence without asking the original attester to perform its evaluation again.

Later verification follows the retained renewal history and the applicable archival policy. A renewal made after the relevant protection has failed cannot establish which earlier records were authentic. Timing is part of the security condition.

[RFC 4998](https://www.rfc-editor.org/rfc/rfc4998.html#section-5) distinguishes renewal of timestamps from renewal of the underlying hash protection. Renewing a signature over retained evidence can suffice while the archival hash remains sound. If that hash weakens, renewal must rehash the archived objects and prior evidence with a suitable successor hash. Signing the old digest again would retain the old weakness.

An archive protected by one scheme must respond to a credible break before an uncertain deadline. With a verify-all composite, a cryptanalytic failure of one component can leave another protecting the records. That surviving protection gives the custodian time to renew the evidence, provided the remaining assumptions and verification machinery hold.

The initial hybrid signature supplies its own unforgeability without depending on a renewal chain. Continued preservation across scheme retirement adds the chain, its timing evidence, and its custody obligations. The archive still needs intact records, securely bound keys, functioning verifiers, and timely renewal.

Choose parameters and custody arrangements that let a successor verify, renew, and produce the record when it is challenged.
