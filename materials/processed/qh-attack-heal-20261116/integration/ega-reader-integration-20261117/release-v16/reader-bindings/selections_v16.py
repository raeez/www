"""V16 source selections for edited excerpts, and chapter summaries for the reader."""

# Each selector starts at a complete paragraph. Counts include independent
# display-math paragraphs. At binding time each prefix must be unique within
# the chapter and the full selection must stay in the original public section.
SELECTIONS = {
    "term-algebra": ("A unital associative algebra consists", 3),
    "term-module": (r"A left \(A\)-module is a vector space", 2),
    "term-coproduct": (r"Suppose \(M\) and \(N\) are representations", 4),
    "term-braiding": ("A braiding is a natural family", 3),
    "term-associator": ("In a monoidal category the associator", 2),
    "term-matching-sector-tensor": ("A fibre functor to bimodules retains", 1),
    "ch02-ising-fibre": ("A fibre functor to ordinary vector spaces must", 2),
    "term-field": (r"Let \(V\) be a complex vector space of states.", 3),
    "term-locality": (r"The products \(A(z)B(w)\) and \(B(w)A(z)\)", 2),
    "term-charged-current": (r"The contour operator \((2\pi i)^{-1}\oint", 1),
    "term-coherent-associative-algebra": (r"Let \(V\) be a graded vector space. A degree-one map", 1),
    "term-centre": (r"Let \(A\) be a unital associative algebra over", 2),
    "ch08-theorem-three-pole-evaluation": ("**Theorem (three-pole evaluation).**", 2),
    "ch08-theorem-four-pole-evaluation": ("**Theorem (four-pole evaluation).**", 2),
    "term-relative-current-complex": (r"Let \(Z_I=\bigcup_{i<j}", 2),
    "term-harmonic-mehler-collar": ("The same scalar action on a cylinder of real length", 3),
    "term-associative-chiral-algebra": ("For either convolution, an **associative chiral algebra**", 1),
    "term-contramodule": ("A **graded contramodule** is a graded vector space", 2),
    "term-ribbon-category": (r"Does the ribbon category \(\operatorname{Rep}^{\mathrm{ord}}(V)\)", 3),
    "term-brane-and-brst-differential": ("An M2 brane is a membrane with two spatial dimensions.", 3),
    "term-cap-reconstruction": ("A **cap** is a chosen filling of a boundary", 1),
    "term-collision-attaching-map": ("For the collision itself the missing morphism belongs", 1),
}
# The eleven numbered problems are separate, unabridged one-paragraph statements.
for number in range(1, 12):
    SELECTIONS[f"ch18-problem-18{number}"] = (f"**Problem 18.{number}.**", 1)

SUMMARIES = {
    "ch01": r"A neutral pair of level-one Wilson rays and a sourced harmonic disk give the same normalized collar pairing. The Beilinson–Drinfeld bracket and an ordered associative convolution describe two operations on colliding fields.",
    "ch02": r"The coproduct of a bialgebra defines the diagonal action on a tensor product of modules. An Ising fibre functor takes values in bimodules over the sector algebra, where tensoring matches the two intermediate labels.",
    "ch03": r"The double pole of a Heisenberg current of level \(\kappa\) gives \([J_m,J_n]=\kappa m\delta_{m+n,0}\,\mathrm{id}\). A contour around a charged insertion measures \(J_0\). On a curve these residue operations transform as maps of differential modules.",
    "ch04": r"Iterated diagonal residues give the chiral Jacobi identity. For four labelled charge-one rays at level two, lines in the cohomology of the deepest link parametrize perverse quotients with identical stalk and costalk ranks.",
    "ch05": r"In arity \(n\) a product of more than \(n\) positive word coefficients vanishes. This bound gives connected bar–cobar duality on unbounded complexes. Consecutive cuts and general ordered decompositions have different collision supports.",
    "ch06": r"Under the smooth realization and tensor–Hom hypotheses, the affine unit is an equivalence on every unbounded source complex at nonrational shifted level. The augmentation ideal then has derived tensor-nilpotence exponent one plus the number of positive roots.",
    "ch07": r"Hochschild cochains give the derived centre of an associative algebra. For a pointed factorization coalgebra, vacuum evaluation assigns a character to an action. The geometric comparison and the derived mapping space of an exterior vertex algebra have separate hypotheses.",
    "ch08": r"For a vector space \(T\) over a field \(F\), a series in \(T((q))\) lies in \(T\otimes_F F((q))\) precisely when its coefficients span a finite-dimensional subspace of \(T\). Three- and four-pole evaluation maps compare repeated fusion on specified coefficient domains.",
    "ch09": r"The mixed differential \(d_t+\bar\partial\) produces a contact current at equal height and coincident complex position. A radial homotopy transports marked operations on the specified subcomplex of relative currents.",
    "ch10": r"Under the normalized four-point hypothesis, a unitary fusion operator relates the two four-point Virasoro channels for positive principal labels at \(c>1\). Sewing two independently completed outputs requires control of the diagonal spectral pairing in the vacuum channel.",
    "ch11": r"A mixed Gaussian moment distinguishes disk states with identical one-mode marginals. The Mehler semigroup gives their collar evolution. In quadratic gravity, comparison of the line-valued vacuum amplitude with a geometric cap requires a cutting map.",
    "ch12": r"Spectral coproducts compose levels. In rank two the divided determinant-one RTT double embeds into the normalized multipoint mode algebra modulo \(\hbar^2\). A two-current pole detects modes beyond its image.",
    "ch13": r"A realized factorization vacuum recovers a Beilinson–Drinfeld chiral algebra. Distinct lattice vertex algebras can have equivalent ribbon categories. The Ising fibre functor over the sector algebra reconstructs a 34-dimensional weak Hopf algebra.",
    "ch14": r"For the M2 particle quotient at zero Cherednik parameter and fixed \(\hbar\ne0\), the Weyl flux cocycle gives a degree-two cap on the derived tensor product. Its square is exact, and a primitive requires arbitrarily high spatial jets.",
    "ch15": r"Subobject flags define Hall convolution. For the one-loop shuffle algebra, the cobar on finite root jets is quasi-isomorphic to its exchange algebra over \(\mathbb Q[\hbar]\) in every charge. Compact K3 traces can agree while a three-point operation varies.",
    "ch16": r"A trace on the theta quotient realizes the complete Weil functional. Eventual nonnegativity for the logarithmic translates of one specified test is equivalent to the Riemann hypothesis. Finite arithmetic jets also retain integral normal derivatives.",
    "ch17": r"A supported bulk insertion acts on boundary fields. An interface on modules and a filling functional must also preserve the collision maps and the gluing pairing. For a neutral Gaussian ray pair, the squared boundary wavefunction and the sourced disk give the same normalized law.",
    "ch18": r"Eleven open problems ask for comparisons of physical adjunctions, chiral products, sewing domains, geometric caps, Hall coefficients and arithmetic collisions, and for positivity of the complete Weil functional.",
}

# The authors supplied these digests after rendering their revised chapters.
FROZEN = {
    "ch01": "1deb7b800cf6f907a67f1c32503c072619e0ef7f95e09bf8835284c08444b6a0",
    "ch02": "8c42c714f44c273c5ba2d579de2a27c5d54ff80245cfd4554765d02a9686dbba",
    "ch03": "8f52cf318f3fb4815fd957a1641a659cf072c62b9be247044667e08003abe948",
    "ch04": "49deb931bbf00ba487c13920e4a4e6d349e38715f71bc27c70fb8d6dae1d61b2",
    "ch05": "011482ae5c997a8cf090d45d39ddfe220dccfed95f5007fefe356610a018bf33",
    "ch06": "a65c9347c588cf581a47a8705e49a6f759d62e42c641237cd4e97bf1ed6c31fc",
    "ch07": "0a417020c7fc27530fbf589cba05330ede4751a5e312336249c9e40a152452f0",
    "ch08": "570f27fe303262c121ac562f969d9783e0573c1120ea54f8f23fb5d39f19afd0",
    "ch09": "5205e0e44c299ef003a15d9e3540044e8c188ea324ef6f0258a0a564d2024fd4",
    "ch10": "bc644d497890415b7f8ced151acd12f6c009d8f02c512648971ac84c66dd66f0",
    "ch11": "a20fd30aef03f0504eabd6b6340e14d99179c072a46ef0499b5c569eeafd79b2",
    "ch12": "8a5e70663ecf4868d96f0fb100fa7de20f014ad45028c196c1196e60d21fdf4c",
    "ch13": "2e6b3c8b6478f0ebb4e280cb98a7c77bfa7e3c670ccd181ba54f586d224e2898",
    "ch14": "e79695a05dfa200f8b45bc58028a75db21eae9e25e489529463610b7f8cb7179",
    "ch15": "f9f3de3469489f555128b4eac1936e64a86e6cce7060acec47b9f54bb13ee201",
    "ch16": "7fb82c7c1595affe3a1a75c075754e537a880650bf3105df66cf329e6148217c",
    "ch17": "0abc64dac2213f2cf1636b9417064da63b8dcfe0d132de7b446f9667d0161ae6",
    "ch18": "cc6ed35116e458a2638810d5bd0b63a04fdbd2981d2cfce2ba0cb98e31d57d73",
}
