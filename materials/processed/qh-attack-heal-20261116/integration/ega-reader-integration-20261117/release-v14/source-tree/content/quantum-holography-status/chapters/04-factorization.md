# Factorization and collision geometry

The free-current calculation has two descriptions. At distinct positions, two insertions give a product of fields. Near a collision, the same product is expressed through its singular and regular coefficients. A geometric algebra must say how these descriptions fit together, and how the answer behaves when three or more points approach one another.

The coefficients of an associative chiral algebra are complexes on configurations and their collision strata. The permitted collisions and the convolution must be specified together. The word construction retains consecutive cuts; the full ordered collision atlas retains ordered decompositions into arbitrary subsets. We will compare their geometry with the classical Beilinson–Drinfeld operation spaces, then use it to define the associative objects and their bars.

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

## Factorization includes the collision extension {#factorization-algebra}

A geometric product can instead be described by its values on finite configurations. At distinct points, independent insertions should combine as an external tensor product. As points collide, their combined object must specialize compatibly to the object attached to the resulting smaller configuration.

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

The need for collision data can be seen before any elaborate example. Let \(D\subset Y\) be a closed subvariety with complementary open inclusion \(j:U\hookrightarrow Y\). If \(K\) is a nonzero sheaf or differential module supported on \(D\), then
\[
j^*K=0.
\]
Consequently \(F\) and \(F\oplus K\) have the same restriction to \(U\). Observing the family only on the separated locus cannot distinguish them. This example does not assert that both objects satisfy the factorization-algebra axioms just stated: those axioms impose additional conditions precisely on such extensions. It shows why a separated identification requires an extension theorem before becoming a global identification.

A morphism of sheaves may therefore become an isomorphism on \(U\) while its kernel or cokernel remains nonzero on \(D\). Chapter 5 expresses the corresponding statement for complexes through sections supported on the collision locus.

These elementary facts govern the later comparison of geometric centres, current operations and collision complexes. An equivalence on separated configurations remains a positive result. Its extension across a collision is another mathematical question, with a definite support where a discrepancy can live.

## Ordered points lead to a different support {#ordered-cut-geometry}

For the word construction, retain the external label order \(1,\ldots,n\). This orders the inputs; it imposes no real order on points of the complex curve. A monotone surjection collapses consecutive labels, and the coefficient complexes carry coherent extraordinary-pullback identifications along its diagonal map. Only adjacent repetitions disappear from a word: \((x,y,x)\) with \(x\ne y\) retains the middle insertion. A consecutive cut after the \(p\)-th input separates the blocks \(\{1,\ldots,p\}\) and \(\{p+1,\ldots,n\}\). Its open set is
\[
U_{p,n-p}=
\{(x_i):x_i\ne x_j\text{ whenever }i\leq p<j\}.
\tag{4.9}
\]
Collisions within either block are allowed. These are the opens used by the consecutive-cut tensor product in Chapter 5.

At arity three there are only two cuts:
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
