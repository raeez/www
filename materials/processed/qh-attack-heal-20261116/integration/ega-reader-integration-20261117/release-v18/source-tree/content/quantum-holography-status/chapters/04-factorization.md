# Factorization and collision geometry

Let \(X\) be a smooth curve over a field of characteristic zero. The Beilinson–Drinfeld operation for two right \(\mathcal D_X\)-modules is defined on \(X^2\), with poles allowed on the diagonal and output supported there. In a normal coordinate \(t=z_1-z_2\), the double pole sends a test function \(f\) to \(\operatorname{Res}_{t=0}f(t)t^{-2}\,dt=f'(0)\). In arity three one takes iterated residues along flags of diagonals. For \(u=z_1-z_3,\ v=z_2-z_3\), the function \(1/[u(u-v)]\) gives residues \(1,0,-1\) in the three channels \(12|3,\ 23|1,\ 13|2\), with the orientations given below. The third term is required by Jacobi.

A partition determines a collision stratum. A cut determines an open set on which its two blocks are disjoint. In the word convolution only consecutive cuts occur, so the locus in \(X^3\) meeting neither cut open is the full outer diagonal \(\Delta_{13}\). The ordered collision atlas allows all ordered decompositions. Specifying these opens fixes the geometry of factorization. Extending a coefficient through their boundaries is a further problem. For a local system \(L\) on the fully distinct open, the comparison \(j_!L\to Rj_*L\) and its normal links make that problem explicit.

## Configurations and partial diagonals {#configuration-spaces}

Let \(X\) be a smooth algebraic curve over a characteristic-zero field \(k\). For a finite nonempty set \(I\), the product \(X^I\) records an \(I\)-labelled family of points. Its open configuration space is
\[
U_I=\{(x_i)\in X^I:x_i\ne x_j\text{ whenever }i\ne j\}.
\tag{4.1}
\]
Write \(j_I:U_I\hookrightarrow X^I\) for its inclusion. The **small diagonal** is the map
\[
\Delta_I:X\longrightarrow X^I,
\qquad x\longmapsto(x)_{i\in I}.
\]
Its image is the locus where all the labelled points coincide. For two labels \(i,j\), the partial diagonal \(\Delta_{ij}\) imposes only \(x_i=x_j\).

A partition of the labels specifies which points are to be treated as one cluster. Represent it by a surjection \(\pi:J\twoheadrightarrow I\), with blocks \(J_i=\pi^{-1}(i)\). Define
\[
U_\pi=\{(x_j)\in X^J:
x_j\ne x_{j'}\text{ if }\pi(j)\ne\pi(j')\}.
\tag{4.2}
\]
Points in different blocks must be distinct; points in the same block may collide. The associated diagonal map
\[
\Delta_\pi:X^I\longrightarrow X^J,
\qquad(x_i)\longmapsto(x_{\pi(j)})
\]
inserts one repeated coordinate for every label in a block. Its image is the locus where the points in each block coincide.

For \(J=\{1,2,3\}\) and blocks \(\{1,2\},\{3\}\), the open set \(U_\pi\) permits \(x_1=x_2\), but excludes \(x_1=x_3\) and \(x_2=x_3\). It is the correct domain for first combining the first two insertions while keeping their cluster separate from the third. A second partition describes the other parenthesization. To compare the resulting operations, one must first put them in a common space of maps.

## A chiral operation is a map with a collision target {#chiral-operation}

Let \(L_i\) and \(M\) be right \(\mathcal D_X\)-modules. Their external tensor product \(\boxtimes_{i\in I}L_i\) is a differential module on \(X^I\): each factor depends on its own point. Allowing singularities along the collision diagonals gives
\[
j_{I*}j_I^*\Bigl(\boxtimes_{i\in I}L_i\Bigr).
\]
For a divisor complement, this is the usual localization allowing poles along the omitted divisor. Locally, an individual section has a finite pole order; no single pole bound is imposed on the whole module. This algebraic localization is not a Laurent completion with an unspecified convergence condition.

The direct image \(\Delta_{I*}M\) is a differential module on \(X^I\) supported on the small diagonal. It includes derivatives in directions normal to that diagonal. A **chiral \(I\)-operation** is a differential-module map
\[
\mu:
j_{I*}j_I^*\Bigl(\boxtimes_{i\in I}L_i\Bigr)
\longrightarrow\Delta_{I*}M.
\tag{4.3}
\]
Thus its space is
\[
P_I^{\mathrm{ch}}((L_i);M)
=\operatorname{Hom}_{\mathcal D_{X^I}}
\left(j_{I*}j_I^*\boxtimes_iL_i,\Delta_{I*}M\right).
\tag{4.4}
\]
Both sides of the Hom belong to the same category on \(X^I\). The source permits separated inputs and their poles; the target records an output concentrated at their collision. This is the operation space of Beilinson–Drinfeld, *Chiral Algebras*, §3.1.1.

The simplest model is a residue. With a local normal coordinate \(t=z-w\), the functional associated to a pole of order \(r\) acts on a test series \(f(t)\) by
\[
\operatorname{Res}_{t=0}\frac{f(t)}{t^r}\,dt
=\frac{f^{(r-1)}(0)}{(r-1)!}.
\tag{4.5}
\]
A simple pole extracts a value; a double pole extracts a first derivative. Higher poles retain higher normal derivatives. The target in (4.3) is designed to hold this information. Substituting \(z=w\) into a singular function would not define the operation.

For three inputs, one can compose a binary operation on the first block with a second binary operation on its output and the remaining input. The partition open \(U_\pi\) keeps distinct clusters apart during the first step. Localization and the diagonal direct-image identities then place the composite in \(P_J^{\mathrm{ch}}\). These composition maps are associative. Beilinson–Drinfeld, §3.1.2, writes them for arbitrary surjections of finite sets; the geometry explains the intermediate domains that a bare expression such as \(\mu(\mu(a,b),c)\) suppresses.

## The Lie convention and the full operator product {#lie-and-operator-product}

In the classical Beilinson–Drinfeld terminology, a nonunital **chiral algebra** is a right differential module \(A\) with a binary operation
\[
\mu\in P_2^{\mathrm{ch}}(A,A;A)
\]
satisfying skew-symmetry and the Jacobi identity in these operation spaces. It is a Lie algebra object for the chiral operations. A unit is a differential-module map \(\omega_X\to A\) whose operation with \(A\) is the canonical residue operation; see *Chiral Algebras*, §§3.3.1–3.3.3.

The word “Lie” here does not mean that the theory has discarded the full operator product of Chapter 3. The chiral operation accepts sections with arbitrary allowed poles. After converting from right to left differential modules and taking the punctured formal neighbourhood of the diagonal, it determines an operator-product expansion with its regular as well as singular coefficients. In local coordinates this is a map of the form
\[
a\boxtimes b\longmapsto
\sum_{n\in\mathbb Z}c_n(w)(z-w)^n,
\tag{4.6}
\]
with a finite negative tail for fixed inputs and the specified differential-module interpretation of the coefficients.

The compatibility is substantial. Beilinson–Drinfeld, Theorem 3.5.10, identifies their chiral Lie brackets with commutative and associative operator-product structures, where iterated products are required to lie in the appropriate common formal expansion space. Their commutativity is exchange of the point-labelled inputs; it does not say that all singular coefficients vanish. Their associativity includes the existence of the common target in which the two expansions can be compared. A family of unrelated Laurent formulas does not satisfy this condition merely because its first few coefficients agree.

The comparison with our associative objects passes through a coalgebra. Apply chiral Chevalley chains to the Beilinson–Drinfeld chiral Lie algebra. Restrict the resulting collision diagram to monotone surjections, and project its coproduct to consecutive cuts. This gives a factorizing cut coalgebra. Its associative cobar is an associative chiral algebra of configuration complexes; [Chapter 5](05-bar-and-coherence.md#ch05-the-support-remembers-which-cuts-were-allowed) gives the definition. A comparison with the original fields and their vacuum is additional structure.

The reverse construction requires an extension of the whole bar coalgebra to every finite-set surjection, with a compatible cocommutative coproduct and factorization on disjoint loci. Symmetry on distinct points alone does not supply those collision maps. Thus the classical Lie–commutative correspondence supplies a construction of associative word objects, rather than an identification of the two categories. [Chapter 12](12-chiral-quantum-groups.md#ch12-associative-products-on-configurations) states the comparison with its chosen tensors.

### Three residues and the obstruction to a diagonal multiplication {#ch04-three-residues}

Take \(u=z_1-z_3\), \(v=z_2-z_3\), and \(F=1/[u(u-v)]\). Collide 1 with 2 first. Writing \(s=u-v\) gives
\[
 F=\frac{1}{s(v+s)}
   =\frac{1}{sv}-\frac{1}{v^2}+\frac{s}{v^3}-\cdots .
\]
The coefficient of \(s^{-1}\) is \(v^{-1}\), so the second residue is \(1\). Collide 2 with 3 first and the expansion \(F=u^{-2}(1-v/u)^{-1}\) is regular in \(v\), giving \(0\). Collide 1 with 3 first and \(F=-u^{-1}v^{-1}(1-u/v)^{-1}\) gives \(-1\). The outer pair contributes the term needed for the three-channel residue identity. Equating the first two iterated residues would lose it.

**Proposition (ternary diagonal operations).** For ordinary right differential modules with the fully localized source and unshifted target of (4.3), the linear spans of composites through \(12|3\) and \(1|23\) have zero intersection. Consequently a strictly associative binary operation in these spaces has zero triple products.

*Proof.* Put \(s=z_1-z_2\), \(v=z_2-z_3\), and \(h=s+v\). Suppose the same map factors through both channels. Fix a section of the fully localized input. Its intermediate image in the first channel is killed by some \(s^a\), since it involves finitely many derivatives normal to \(\Delta_{12}\). In the second channel some \(v^b\) kills its image. The difference \(h\) is invertible before the final collision in either route. For \(N=a+b-1\), expand \(1=h^{-N}(s+v)^N\) on the input. Every term has either a factor \(s^a\) or a factor \(v^b\). Compute its common image through the corresponding channel to see that it vanishes. The argument also applies to finite sums by taking direct sums of the intermediate modules. An associative composite lies in that intersection. ∎

A local vacuum whose left action is the normalized principal-part map would give the identity on a state by two successive vacuum residues. Thus a nonzero ordinary object on this carrier cannot have both that vacuum and a strictly associative binary operation. On complexes the analogous conclusion \(A\simeq0\) holds if the source is still fully localized, the small-diagonal target still unshifted, the multiplication homotopy associative, and the left action of a closed degree-zero vacuum homotopic to principal parts. The Beilinson–Drinfeld Lie operation satisfies Jacobi. Associative multiplication on configuration complexes uses the larger family of targets described below.

## Factorization includes the collision extension {#factorization-algebra}

A factorization algebra on \(X\) assigns a coefficient \(B_I\) to \(X^I\). It restricts to an external product on the open where the blocks of a partition are disjoint, and it identifies the pullback to a partition diagonal with the coefficient for the quotient set of labels.

In the classical algebraic formulation, a factorization algebra consists of quasi-coherent sheaves \(B_I\) on \(X^I\), together with two kinds of identifications. A surjection \(\pi:J\twoheadrightarrow I\) gives the diagonal identification
\[
\nu_\pi:\Delta_\pi^*B_J\xrightarrow{\sim}B_I
\tag{4.7}
\]
and the factorization identification on the block-separation open
\[
c_\pi:
\left.\boxtimes_{i\in I}B_{J_i}\right|_{U_\pi}
\xrightarrow{\sim}
\left.B_J\right|_{U_\pi}.
\tag{4.8}
\]
The diagonal identifications compose under successive collapses. The factorization identifications compose under refinements of partitions, and these two systems agree when some clusters are collapsed while others remain separated. The sheaves have no nonzero local sections supported on the union of collision diagonals. A unit is a section \(1\in B_{\{1\}}\) whose external product with every local section extends across the two-point diagonal and restricts there to that section. These are the ordinary sheaf conditions of *Chiral Algebras*, §§3.4.2–3.4.4; in derived formulations the pullbacks, equivalences and compatibilities need their derived versions.

For example, taking \(B_I=\mathcal O_{X^I}\) gives the unit factorization algebra. The factorization maps are the evident identifications of functions in separate sets of variables; the unit is the constant function \(1\). More interesting examples retain nontrivial collision data even though their restrictions to pairwise-distinct points are external products.

The full family is often described as a sheaf on the **Ran space** of \(X\). At the level of points, this is the set of finite nonempty subsets of \(X\); repeated labels specify the same subset. The maps \(\Delta_\pi\) express exactly those repetitions. One may use the compatible family \((B_I,\nu_\pi)\) without treating the Ran space as an ordinary finite-dimensional variety.

**Theorem: classical factorization and chiral algebras.** The above category of unital factorization algebras is equivalent to the category of unital Beilinson–Drinfeld chiral algebras on \(X\). The factorization sheaves acquire a canonical differential-module structure, and the corresponding right differential module is \(\omega_X\otimes B_{\{1\}}\).

This is *Chiral Algebras*, Proposition 3.4.7 and Theorem 3.4.9. The forward construction uses factorization to compare sections away from diagonals and then applies the geometric residue operation to obtain (4.3). The inverse construction is controlled by a complex indexed by partitions and their diagonals: its differential combines the chiral operations, and its exactness makes the collision extensions compatible. This partition complex is the Chevalley–Cousin complex of §§3.4.10–3.4.12. The theorem is about the full compatible sheaf data, including collisions and the unit. Giving only (4.8) on a separated open set omits part of its hypothesis.

## The open locus cannot determine every extension {#collision-supported-data}

Let \(D\subset Y\) be a closed subvariety with complementary open inclusion \(j:U\hookrightarrow Y\). If \(K\) is a nonzero sheaf or differential module supported on \(D\), then
\[
j^*K=0.
\]
Consequently \(F\) and \(F\oplus K\) have the same restriction to \(U\). For example, \(F=0\) and \(K\ne0\) have isomorphic restrictions to \(U\) and are inequivalent on \(Y\). The diagonal and unit axioms impose further constraints on which extensions define factorization algebras.

A morphism of sheaves may therefore become an isomorphism on \(U\) while its kernel or cokernel remains nonzero on \(D\). Chapter 5 expresses the corresponding statement for complexes through sections supported on the collision locus.

These elementary facts govern the later comparison of geometric centres, current operations and collision complexes. An equivalence on separated configurations remains a positive result. Its extension across a collision is another mathematical question, with a definite support where a discrepancy can live.

### The normal link of a collision {#ch04-normal-link}

Work on the complex line, with ordinary constructible sheaves of complex vector spaces. Let \(j:\operatorname{Conf}_n(\mathbb C)\hookrightarrow\mathbb C^n\) include the fully distinct ordered configurations and let \(L\) be a finite-rank local system in degree zero. The **normal link complex** at a boundary point \(x\) is the cohomology complex of \(L\) on the separated part of a sufficiently small transverse neighbourhood. Its two descriptions are
\[
 K_x=(Rj_*L)_x
     \simeq\bigl(\operatorname{Cone}(j_!L\longrightarrow Rj_*L)\bigr)_x .
\]
The equality uses the zero boundary stalk of extension by zero \(j_!L\). For one colliding pair the transverse neighbourhood is a punctured disc. If \(C\) is transport of its fibre \(E\) around the puncture, the circle has cochains \([E\xrightarrow{C-1}E]\) in degrees \(0,1\). Thus the link measures both invariant vectors and coinvariants.

**Theorem (simultaneous cluster twists).** Suppose the coincident points at \(x\) form nontrivial blocks \(S_1,\ldots,S_b\). A positive full twist of a block rotates all its points once around their common centre while leaving the other blocks apart. Let \(C_i\) be its action on a common fibre \(E\), using local base paths. Then
\[
 K_x\not\simeq0\quad\Longleftrightarrow\quad
 \bigcap_{i=1}^b\ker(C_i-1)^{\dim E}\ne0 .
\]
Conjugating the local representation does not change the criterion. The twists commute with each other and with the angular monodromies in this local product, even when the angular monodromies fail to commute among themselves.

*Proof.* In a cluster of size \(r\) translate its first point to zero, choose the difference of the first two as scale, and divide all the other differences by that scale. Up to homotopy the separated normal directions are \(S^1\times Y_r\), where \(Y_r\) parametrizes \(r-2\) ordered points of \(\mathbb C\setminus\{0,1\}\). Write \(Y_2=\mathrm{pt}\). The scale circle acts by the full twist. Disjoint discs give a product of these spaces for the different blocks. Decompose \(E\) into simultaneous generalized eigenspaces of the central twists. Any summand on which some \(C_i-1\) is invertible has a contractible circle complex. On the common generalized unit summand \(E_1\), the angular cochains have Euler characteristic
\[
 \dim(E_1)\prod_i(-1)^{|S_i|-2}(|S_i|-2)! .
\]
Indeed, forgetting the moving points one at a time gives punctured-line fibres of Euler characteristics \(-1,-2,\ldots,-(r-2)\). If \(E_1\ne0\), these angular cochains have nonzero cohomology. Adding a circle takes the two-term complex of a nilpotent endomorphism \(C_i-1\), which cannot be invertible on nonzero cohomology. Each remaining endomorphism is still nilpotent on this cochain model. Iterating preserves nonvanishing. ∎

At the partition \(12|34\), take the direct sum of two winding characters with pair twists \(C_{12}=\operatorname{diag}(1,2)\) and \(C_{34}=\operatorname{diag}(2,1)\), and trivial monodromy for the other pairs. Each pair alone has an invariant line. The two lines have zero intersection, so the link at the double collision vanishes.

There is a sharper multiplicity statement at one full collision of size \(n\ge3\). Denote its scale monodromy by \(C\), and let \(V_0=\ker(C-1)\) and \(V_1=\operatorname{coker}(C-1)\) carry their induced angular actions. Suppose the monodromy of every boundary divisor of \(\overline M_{0,n+1}\), including those at infinity, has no eigenvalue \(1\) on either coefficient. Here \(\overline M_{0,n+1}\) compactifies the directions by stable configurations of \(n+1\) marked points of a rational curve. With \(m=n-2\), the link has cohomology only in degrees \(m,m+1\), of dimension \(m!\dim\ker(C-1)\) in each. Indeed the radial circle has precisely \(V_0,V_1\) as its two direct-image sheaves. For each, the boundary circles contract the local cochains. Compactly supported and ordinary angular cohomology then agree, and punctured-line fibrations and duality concentrate both in degree \(m\). Euler characteristic gives the rank. For example, at \(n=3\) take a single unipotent Jordan block \(C\) of size \(d\ge2\), and angular generators \(2I,3I\) around the two finite punctures of \(Y_3\). The third angular multiplier is \(I/6\). Both link groups have dimension one, for every \(d\). The size of the generalized unit eigenspace detects survival, while its geometric multiplicity determines the rank under the stated angular hypothesis.

### Four charged rays and their possible attachments {#ch04-gaussian-collision}

A physical source of a rank-one coefficient is a Gaussian Wilson ray, a line carrying a fixed abelian charge and ending at the Heisenberg boundary. Use level \(k\in\mathbb C^\times\), the Cauchy propagator, radial transverse regularization, outgoing mutual subtraction and parallel-copy framing. The incoming Fock states are finite polynomials in creation modes. Pair the outgoing state of charge \(\sum_a\alpha_a\) with the functional that extracts its oscillator-free coefficient. For incoming highest-weight states of charges \(\alpha_a\), the result on the separated open in the chosen chamber is
\[
 F_{\boldsymbol\alpha}(z)=\prod_{a<b}(z_a-z_b)^{\alpha_a\alpha_b/k}.
\]
Each pair contributes its Gaussian contraction to the logarithm. Equivalently, commuting the annihilation part of one current intertwiner through the creation part of the next produces its factor. Continue from the chosen chamber along a common path with the individual coordinate frames fixed. The branches span a rank-one local system. A full twist of \(S\) winds each internal difference once, hence has multiplier
\[
 \exp\!\left(\frac{2\pi i}{k}\sum_{\{a,b\}\subset S}\alpha_a\alpha_b\right).
\]
Its comparison link survives exactly when the exponent divided by \(2\pi i\) is integral for **every** nontrivial block. Rotation of an individual ray frame has its own conformal phase. The highest-weight coefficient used here exists at nonzero outgoing charge.

Take four charges \(1,1,1,1\) at level \(2\), so the outgoing charge is \(4\). The exponents in units of \(2\pi i\) for block sizes \(2,3,4\) are \(1/2,3/2,3\). All proper collision links vanish, including the two-pair link. At the full collision the scale monodromy is \(1\). The directions \(Y_4=M_{0,5}\) parametrize five labelled points on the projective line up to fractional linear transformations, with three fixed at \(0,1,\infty\). Every boundary divisor in its stable compactification corresponds to a proper block and has monodromy \(-1\). Its circle complex contracts, so compactly supported and ordinary direction cohomology agree. Forgetting one moving point at a time bounds cohomology above degree two, and duality supplies the lower bound. The Euler characteristic \((-1)(-2)=2\) gives two direction classes in degree two. The radial circle contributes one copy in each of its degrees \(0,1\). Thus the full link \(K\) has
\[
 \dim H^2K=\dim H^3K=2,\qquad H^aK=0\quad(a\ne2,3).
\]
More generally, at integral level \(\ell\ge2\) with every charge one, the first collision with nonzero link is the full collision at the least \(n\ge2\) for which \(\ell\) divides \(\binom n2\). The same argument on \(M_{0,n+1}\) gives ranks \((n-2)!\) in degrees \(n-2,n-1\).

There is still a choice about attaching the four-point coefficient. Take the transverse slice \(\mathbb C^3\), let \(i\) include its origin, and now shift the local system by \([3]\) to use the perverse normalization. Put \(V=H^2K\) and \(V'=H^3K\). For this coefficient \(P_!=j_!L[3]\) is perverse. The intermediate extension \(j_{!*}L[3]\) is the extension with no nonzero subobject or quotient on the boundary. The canonical sequence is
\[
 0\longrightarrow i_*V\longrightarrow P_!
 \longrightarrow j_{!*}L[3]\longrightarrow0 .
\]
For each line \(W\subset V\), form the quotient \(P_W=P_!/(i_*W)\) in the perverse category. Its ordinary stalk is \(i^*P_W\simeq W[1]\). The costalk \(i^!P_W\) measures local cohomology supported at the origin. Since \(i^!P_!\simeq K[2]\), the costalk sequence gives \(H^0 i^!P_W=V/W\) and \(H^1 i^!P_W=V'\), with all other groups zero.

Every line therefore gives the same ranks and the same extension off the origin. The attaching arrow \(i^*P_W\to K[3]\) on \(H^{-1}\) has image the particular line \(W\subset V\). Indeed its image is the kernel of the boundary map \(V\to H^0i^!P_W=V/W\). An isomorphism of two such sheaves acts on the separated rank-one local system by a scalar and, by naturality of \(j_!\), must carry one embedded kernel in \(P_!\) to the other. A scalar fixes each line. Hence distinct \(W\)'s give distinct isomorphism classes parametrized by \(\mathbb P(V)\cong\mathbb P^1\). This calculation concerns extensions on the fixed labelled slice. Identifying a physical collision or an oriented Hall coefficient would require its attaching morphism and compatibility with its other collision maps.

The four rays have identical charges. What changes if their labels may be permuted? Fix the positive elementary half-braid to act by \(+i\), keeping every individual coordinate frame fixed. One description is the connection \(d-\tfrac12d\log\Delta\), with \(\Delta=\prod_{a<b}(z_a-z_b)\), on the trivial line with permutations acting trivially on its coordinate fibre. A positive half exchange changes the argument of \(\Delta\) by \(\pi\). On the centred normal slice with origin fixed by \(S_4\), this determines an \(S_4\)-action on \(V=H^2K\).

Its character can be computed on the shapes \(M_{0,5}\). Under simultaneous dilation by \(a\), a horizontal section scales by \(a^3\). Compactly supported angular cohomology is concentrated in degree two and identifies equivariantly with \(V\). The trace of a finite permutation is consequently its compactly supported Lefschetz number on the shape space. A transposition has no fixed shape, since an affine map fixing the two unswapped points fixes every point. A three-cycle has two fixed shapes, the two orderings of an equilateral triple about the fourth mark. Their dilation factors are primitive cube roots, with cube \(1\), so the trace is \(2\). Every three-cycle therefore acts as the identity on this two-dimensional space. They generate \(A_4\), and the transposition trace \(0\) distinguishes the two summands:
\[
 V\simeq{\bf1}\oplus\operatorname{sgn}.
\]
The quotient \(P_W\) extends the chosen permutation action exactly when \(W\) is stable, by naturality of its quotient map from \(P_!\). Thus precisely the trivial and the sign lines survive among the labelled \(\mathbb P^1\). The phase \(i\) measures transport on the free open. The eigenvalue \(+1\) or \(-1\) on \(H^{-1}i^*P_W=W\) measures a stabilizer acting at the collision.

There is a further choice between retaining that stabilizer and requiring ordinary inverse image from the coarse variety. Write \(\pi:X\to X/S_4\) for the finite quotient of the centred slice and \(\bar L\) for the specified line on the unordered open \(\bar j\). For an equivariant complex \(P\), the counit \(\pi^*(R\pi_*P)^{S_4}\to P\) on the stalk at \(x\) is the inclusion of its stabilizer invariants. Indeed the finite fibre is an orbit, and over \(\mathbb C\) taking invariants is exact. Stabilizers are trivial on the distinct open, and the proper collision stalks vanish. At the origin the test reduces to \(W^{S_4}\to W\), so precisely the trivial line meets this extra requirement. In fact \(P_{\bf1}\simeq\pi^*\bar j_{!*}\bar L[3]\). Taking invariant finite pushforward in the canonical sequence retains exactly \(V^{S_4}={\bf1}\), and preserves the perverse image of extension by zero in right direct image. This identifies the intermediate extension downstairs. The selection is unique within the displayed quotient family under the coarse inverse-image hypothesis. The Gaussian coefficient alone imposes no such hypothesis on a physical collision.

### An irregular collision can detect a hidden extension {#ch04-irregular-collision}

Three points give a test that ordinary monodromy misses. Take difference coordinates \(x=z_1-z_3\) and \(y=z_2-z_3\). Off the three collision lines \(xy(x-y)=0\), the slope \(u=x/y\) is defined. Pull back the two-dimensional connection whose horizontal columns satisfy
\[
dy_1=a y_2\,du,\qquad dy_2=-2u^{-3}y_2\,du .
\]
Its diagonal exponential factors are \(1\) and \(e^{1/u^2}\). For every complex \(a\) its ordinary analytic monodromy is trivial. At \(a=0\) the connection splits. To test splitting algebraically, let \(j\) include the complement of the collision lines, let \(i\) include their common origin, and put \(C_a=\operatorname{Cone}(j_!M_a\to j_*M_a)\) for the pulled-back connection \(M_a\). Use algebraic holonomic direct images and the de Rham normalization in which the constant connection on the plane gives \(\mathbb C[2]\).

The decisive calculation is on the angular curve. Set \(r=y/x\). In the dual connection the differential on the exponential summand is \(Tq=q'+2rq\). The constant section of the trivial quotient has connecting class \(-a[r^{-2}dr]=-2a[dr]\), since \(T(-1/r)=r^{-2}-2\). The class \([dr]\) survives. A finite pole in a rational primitive would produce a higher pole on differentiation, while \(T\) sends a nonzero polynomial to one of positive degree. The radial factor contributes \(1\) and \(dx/x\). Duality and scalar contraction then give the dimensions of the extraordinary restriction \(H^{k}(i^!C_a)\), in degrees \(k=-1,0,1\):
\[
 (5,6,1)\quad(a=0),\qquad (4,4,0)\quad(a\ne0).
\]
This measurement decides whether the extension splits. In the fixed graded frames the upper-minus-lower Stokes multiplier is \(2i\sqrt{\pi}\,a\). It is minus the period of the dual extension class on an upward rapid-decay contour between the two marked sectors. Changing a frame rescales the multiplier, while the costalk dimensions stay fixed.

Four points allow a different measurement. On the transverse space \(X=\mathbb A^3\) take \(s=z_2-z_1,\ x=z_3-z_1,\ y=z_4-z_1\). On the open \(j:U\hookrightarrow X\) of distinct points put \(r=x/s,\ t=y/s\). To the preceding angular connection \(N_a(r)\) attach a two-dimensional factor \(W\) with connection \(d-J\,d\log(t-r)\), where \(J^2=0\ne J\). Its monodromy around \(t=r\) is \(1+2\pi iJ\). Write \(M\) for the tensor product and \(C=\operatorname{Cone}(j_!M\to j_*M)\). The line \(L=\{x=y=s\}\) is the collision of labels \(2,3,4\), and \(i\) includes the total collision \(s=x=y=0\). Two collision flags approach \(L\), one through \(u=r-1=0\), the other through \(w=t-r=0\).

To compare them, keep the horizontal frame of \(N_a^\vee\) at \(r=1\), transport the dual fibre of \(W\) in the same positive real chamber, and identify the two flag sources by the labelled forms \(p=d\log u,\ q=d\log w\). The third normal divisor is \(u+w=0\). Near \(L\) write \(\alpha=d\log(u/w)\), \(\beta=d\log(1+u/w)\), and \(\rho=p-q\). In the normalized logarithmic models the two restriction maps \(F_u,F_w\) on the simultaneous normal coefficient \(P\) have the following values in their common flag model \(T\):
\[
\begin{array}{c|ccc}
 &q&\alpha&\beta\\ \hline
 F_u&q&\rho&0\\
 F_w&q&\rho&\rho
\end{array}
\]
Indeed \(d\log(1+u/w)\) has zero residue at \(u/w=0\). In the other chart it equals \(d\log(u/w)+d\log(1+w/u)\). The second term has zero residue there. Both maps keep the differential \(d+J^{\mathsf t}q\wedge-\) on the dual spectator.

Let \(A\) be the unshifted algebraic de Rham complex on the angular surface \(r,t\notin\{0,1\},\ t\ne r\), with its dual coefficient. Write \(S:A\to P\) for restriction to the simultaneous normal germ and \(\lambda=d\log s\). Naturality of the localization triangle, with the boundary for extension by zero fixing the sign on both sources, gives the two maps
\[
 D_j=(1\otimes F_jS)^\vee[-1]:
 (\Lambda(\lambda)\otimes T)^\vee[-1]\longrightarrow
 (\Lambda(\lambda)\otimes A)^\vee[-1]\simeq i^!C[1],
 \qquad j=u,w .
\]
The ordinary outer star link along \(L\) supplies \(\Lambda(\lambda)\). With \(\mathrm{DR}(\mathcal O_X)=\mathbb C[3]\), ordinary degree \(m\) is dual to degree \(1-m\) in this target. For example, choose \(v\notin J^{\mathsf t}W^\vee\) with \(J^{\mathsf t}v\ne0\). A closed angular form \(g(r)v\,q\wedge d\log(t-1)\), with \(g=e=(1,-a/r)\) or \(g=f=(0,1)\) in the dual angular frame, restricts to zero under the first flag and to the nonzero class \(g(1)v\,q\wedge\rho\) under the second. Its product with \(\lambda\) detects the difference one degree lower after dualizing.

The four entries in each tuple below are in degrees \(1,0,-1,-2\). The middle columns give image ranks on cohomology.

| Parameter | \(H^\bullet(i^!C[1])\) dimensions | Each flag | Sum of the images | \(D_w-D_u\) |
| --- | --- | --- | --- | --- |
| \(a=0\) | \((1,9,31,23)\) | \((1,4,5,2)\) | \((1,5,8,4)\) | \((0,1,3,2)\) |
| \(a\ne0\) | \((0,4,24,20)\) | \((0,2,4,2)\) | \((0,2,6,4)\) | \((0,0,2,2)\) |

The pair \((F_u,F_w)\) is split injective on the normal complex. Its dual therefore spans the image of the single localization boundary from \(L\), which is smaller than the entire vertex cohomology in both rows. The two orders distinguish actual algebraic maps for this connection. Identifying them with independently defined enhanced or sectorial specialization maps would also require their Stokes filtrations, sectors and comparison with this marking.

## Ordered points lead to a different support {#ordered-cut-geometry}

For the word construction, retain the external label order \(1,\ldots,n\). This orders the inputs; it imposes no real order on points of the complex curve. A monotone surjection collapses consecutive labels, and the coefficient complexes carry coherent extraordinary-pullback identifications along its diagonal map. Only adjacent repetitions disappear from a word: \((x,y,x)\) with \(x\ne y\) retains the middle insertion. A consecutive cut after the \(p\)-th input separates the blocks \(\{1,\ldots,p\}\) and \(\{p+1,\ldots,n\}\). Its open set is
\[
U_{p,n-p}=
\{(x_i):x_i\ne x_j\text{ whenever }i\leq p<j\}.
\tag{4.9}
\]
Collisions within either block are allowed. These are the opens used by the consecutive-cut tensor product in Chapter 5.

In arity three, the two consecutive cuts give
\[
U_{1,2}=X^3\setminus(\Delta_{12}\cup\Delta_{13}),
\qquad
U_{2,1}=X^3\setminus(\Delta_{13}\cup\Delta_{23}).
\]
Their common failure locus is
\[
\begin{aligned}
Z_3
&=X^3\setminus(U_{1,2}\cup U_{2,1})\\
&=(\Delta_{12}\cup\Delta_{13})
\cap(\Delta_{13}\cup\Delta_{23})
=\Delta_{13}.
\end{aligned}
\tag{4.10}
\]
Indeed, if \(x_1=x_3\), both cuts have a coincident pair across the cut. Conversely, if both cuts fail and \(x_1\ne x_3\), the first failure forces \(x_1=x_2\) and the second forces \(x_2=x_3\), a contradiction. Thus the first and third points can obstruct every consecutive cut while the second point lies elsewhere. The support is larger than the small diagonal.

The full ordered collision atlas is constructed from one chart \(X^I\) for each total order on the labels. Two charts are glued where their orders agree within every set of coincident labels. The coefficient systems use extraordinary pullback along surjections with ordered fibres. Their convolution sums over all ordered decompositions \(I=A\sqcup B\), with the blocks separated. This convolution is symmetric monoidal, although an associative algebra for it may have noncommutative multiplication.

Word convolution instead uses the initial and final intervals of one fixed order and is nonsymmetric. Restricting an atlas system to its increasing chart and projecting onto those consecutive decompositions gives the cut coproduct. The projection is generally not an equivalence: at two distinct points it can discard the reverse-order summand. Consequently the two convolutions, and the factorization conditions attached to them, remain distinct.

The bar construction of [Chapter 5](05-bar-and-coherence.md) records multiplication and its higher associativity relations as a differential on words. At a configuration with \(n\) labels, a product of more than \(n\) positive factors vanishes. This finite arity bound gives the associative bar–cobar equivalence in each of the two coefficient categories, using its own convolution.

::: figure fig-ordered-cut-support
