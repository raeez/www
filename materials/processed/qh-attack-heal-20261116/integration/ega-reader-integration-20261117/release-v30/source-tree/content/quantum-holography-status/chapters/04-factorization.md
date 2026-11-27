# Factorization and collision geometry

A small contour around the current \(J(w)\) measures its product with a second current at \(z\). If the singular term is \(\kappa/(z-w)^2\), then weighting the contour by a function \(f(z)\) gives \(\kappa f'(w)\). Both inputs now sit at \(w\), yet the result still depends on how \(f\) varies *away* from \(w\). This is why the geometric form of a chiral operation has a target on the diagonal that retains derivatives in the separation of its inputs.

With a third insertion at \(z_3\), one can draw a contour around \(z_1,z_2\) excluding \(z_3\). One can also first enclose \(z_2,z_3\). The allowed positions differ for these two operations, even before the integrals are evaluated. The geometry we need is therefore the geometry of clusters of points. It will also let us distinguish two questions. What does a field do while the clusters remain apart? What extension of their coefficient is attained when the clusters meet?

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

For three inputs return to the contour enclosing \(z_1,z_2\) alone. The first operation produces a coefficient on \(\Delta_{12}\), the locus \(z_1=z_2\). A second operation combines this coefficient with the one at \(z_3\) and lands on the small diagonal \(z_1=z_2=z_3\). The partition open \(U_\pi\) keeps distinct clusters apart during the first step. Localization and the diagonal direct-image identities then place the composite in \(P_J^{\mathrm{ch}}\). These composition maps are associative. Beilinson–Drinfeld, §3.1.2, writes them for arbitrary surjections of finite sets; the geometry explains the intermediate domains that a bare expression such as \(\mu(\mu(a,b),c)\) suppresses.

## The Lie convention and the full operator product {#lie-and-operator-product}

In the classical Beilinson–Drinfeld terminology, a nonunital **chiral algebra** is a right differential module \(A\) with a binary operation
\[
\mu\in P_2^{\mathrm{ch}}(A,A;A)
\]
satisfying skew-symmetry and the Jacobi identity in these operation spaces. It is a Lie algebra object for the chiral operations. A unit is a differential-module map \(\omega_X\to A\) whose operation with \(A\) is the canonical residue operation; see *Chiral Algebras*, §§3.3.1–3.3.3.

The ordinary Lie bracket of modes can be read from just the singular terms of a product. The geometric chiral bracket has a larger domain. Multiply a regular coefficient \(c_q(w)t^q\), \(q\ge0\), by \(t^{-q-1}\) and take a residue in \(t=z-w\). This recovers \(c_q(w)\), since no other power contributes. The chiral operation accepts precisely such Laurent multipliers. After converting from right to left differential modules and taking the punctured formal neighbourhood of the diagonal, it determines an operator-product expansion with its regular as well as singular coefficients. In local coordinates this is a map of the form
\[
a\boxtimes b\longmapsto
\sum_{n\in\mathbb Z}c_n(w)(z-w)^n,
\tag{4.6}
\]
with a finite negative tail for fixed inputs and the specified differential-module interpretation of the coefficients.

The compatibility is substantial. Beilinson–Drinfeld, Theorem 3.5.10, identifies their chiral Lie brackets with commutative and associative operator-product structures, where iterated products are required to lie in the appropriate common formal expansion space. Their commutativity is exchange of the point-labelled inputs; it does not say that all singular coefficients vanish. Their associativity includes the existence of the common target in which the two expansions can be compared. A family of unrelated Laurent formulas does not satisfy this condition merely because its first few coefficients agree.

The distinction between this associativity of the full operator product and associativity of a *map to the diagonal* already occurs at three inputs. The relevant iterated residues can be computed with a single rational function.

### Three residues and the obstruction to a diagonal multiplication {#ch04-three-residues}

Translate the third point to the origin by writing \(u=z_1-z_3,\ v=z_2-z_3\). The rational function \(F=1/[u(u-v)]\) has a pole at \(z_1=z_2\) and at \(z_1=z_3\); it has no pole at a generic point of \(z_2=z_3\). For a collision in two stages, first extract the coefficient of the inverse separation of the colliding pair. Then extract the residue in the remaining separation. To collide 1 with 2 first, set \(s=u-v\) and expand near \(s=0\) with \(v\ne0\):
\[
 F=\frac{1}{s(v+s)}
   =\frac{1}{sv}-\frac{1}{v^2}+\frac{s}{v^3}-\cdots .
\]

The coefficient of \(s^{-1}\) is \(v^{-1}\), so the second residue is \(1\). Collide 2 with 3 first and the expansion \(F=u^{-2}(1-v/u)^{-1}\) is regular in \(v\), giving \(0\). Collide 1 with 3 first and \(F=-u^{-1}v^{-1}(1-u/v)^{-1}\) gives \(-1\). With these choices of normal coordinates the three oriented contributions add to \(1+0-1=0\). The collision of the outer pair \(1,3\) supplies the third term in the residue form of Jacobi. Equating the first two iterated residues would lose it.

**Proposition (ternary diagonal operations).** For ordinary right differential modules with the fully localized source and unshifted target of (4.3), the linear spans of composites through \(12|3\) and \(1|23\) have zero intersection. Consequently a strictly associative binary operation in these spaces has zero triple products.

*Proof.* Put \(s=z_1-z_2\), \(v=z_2-z_3\), and \(h=s+v\). Suppose the same map factors through both channels. Fix a section of the fully localized input. Its intermediate image in the first channel is killed by some \(s^a\), since it involves finitely many derivatives normal to \(\Delta_{12}\). In the second channel some \(v^b\) kills its image. The difference \(h\) is invertible before the final collision in either route. For \(N=a+b-1\), expand \(1=h^{-N}(s+v)^N\) on the input. Every term has either a factor \(s^a\) or a factor \(v^b\). Compute its common image through the corresponding channel to see that it vanishes. The argument also applies to finite sums by taking direct sums of the intermediate modules. An associative composite lies in that intersection. ∎

A local vacuum whose left action is the normalized principal-part map would give the identity on a state by two successive vacuum residues. Thus a nonzero ordinary object on this carrier cannot have both that vacuum and a strictly associative binary operation. On complexes the analogous conclusion \(A\simeq0\) holds if the source is still fully localized, the small-diagonal target still unshifted, the multiplication homotopy associative, and the left action of a closed degree-zero vacuum homotopic to principal parts. The Beilinson–Drinfeld Lie operation satisfies Jacobi. Associative multiplication on configuration complexes uses the larger family of targets described below.

## Factorization includes the collision extension {#factorization-algebra}

The residue problem uses a coefficient at every configuration. With two labels we need a sheaf \(B_{\{1,2\}}\) of local sections on \(X^2\), describing both separated and coincident positions. On the distinct open it must agree with a product of independent one-point coefficients. On the diagonal its restriction must agree with one coefficient at the common position. With three labels the two identifications must commute when two points collide while the third stays away. These requirements give the two maps in the definition of a factorization algebra.

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

For example take \(B_I=\mathcal O_{X^I}\), the sheaf of regular functions. At two distinct variable sets the external tensor product is \(\mathcal O_{X^2}\) restricted to their separation open. Pulling a section \(f(z_1,z_2)\) back to the diagonal gives \(f(z,z)\). In this example multiplying a one-point function by \(1\) at a second point extends across their diagonal and restricts to the original function there. This gives the unit factorization algebra. More interesting examples retain nontrivial collision data even though their restrictions to pairwise-distinct points are external products.

The tuples \((x,y)\), \((x,x,y)\) and \((y,x)\) correspond to the same finite subset when \(x\ne y\). The diagonal and relabelling identifications explain why one often describes the compatible family as a sheaf on the **Ran space** of \(X\). At the level of points, this is the set of finite nonempty subsets of \(X\); repeated labels specify the same subset. The maps \(\Delta_\pi\) express exactly those repetitions. One may use the compatible family \((B_I,\nu_\pi)\) without treating the Ran space as an ordinary finite-dimensional variety.

**Theorem: classical factorization and chiral algebras.** The above category of unital factorization algebras is equivalent to the category of unital Beilinson–Drinfeld chiral algebras on \(X\). The factorization sheaves acquire a canonical differential-module structure, and the corresponding right differential module is \(\omega_X\otimes B_{\{1\}}\).

This is *Chiral Algebras*, Proposition 3.4.7 and Theorem 3.4.9. The forward construction uses factorization to compare sections away from diagonals and then applies the geometric residue operation to obtain (4.3). The inverse construction is controlled by a complex indexed by partitions and their diagonals: its differential combines the chiral operations, and its exactness makes the collision extensions compatible. This partition complex is the Chevalley–Cousin complex of §§3.4.10–3.4.12. The theorem is about the full compatible sheaf data, including collisions and the unit. Giving only (4.8) on a separated open set omits part of its hypothesis.

## The open locus cannot determine every extension {#collision-supported-data}

On a disk with centre \(0\), the sheaf \(\mathbb C_{\{0\}}\) supported at the centre has fibre \(\mathbb C\) there and zero stalk at every other point. All measurements on the punctured disk therefore agree for a sheaf \(F\) and for \(F\oplus\mathbb C_{\{0\}}\). Their stalks at the centre need not agree. In general, let \(D\subset Y\) be closed and let \(j:U=Y\setminus D\hookrightarrow Y\) include its complement. A sheaf or differential module \(K\) supported on \(D\) has \(j^*K=0\). The extensions of \(F|_U\) need not define factorization algebras. They must also satisfy the diagonal and unit axioms above.

A morphism of sheaves may therefore become an isomorphism on \(U\) while its kernel or cokernel remains nonzero on \(D\). Chapter 5 expresses the corresponding statement for complexes through sections supported on the collision locus.

There is a subtler ambiguity. One can fix the dimension of the stalk at the centre and still vary its attachment to nearby sections. To describe that attachment we need the complex of sections seen from a punctured neighbourhood.

### The normal link of a collision {#ch04-normal-link}

For two points on the complex line, hold their common position fixed and move their difference around zero. A small punctured disk of differences retracts onto a circle. Suppose a locally constant family of vector spaces has fibre \(E\) there and a trip around the circle returns vectors by a linear map \(C:E\to E\). The circle has one vertex and one oriented edge. A vector \(v\) assigned to that vertex returns as \(Cv\), so the cellular cochains are
\[
 E\xrightarrow{\,C-1\,}E
\]
in degrees \(0,1\). The cohomology in degree zero is \(\ker(C-1)\), the vectors unchanged by the loop. In degree one it is \(E/(C-1)E\). For a one-dimensional coefficient both groups have dimension one when \(C=1\) and both vanish when \(C=-1\).

For \(n\) distinct labelled points write \(j:\operatorname{Conf}_n(\mathbb C)\hookrightarrow\mathbb C^n\). Let \(L\) be a finite-rank complex local system in degree zero, that is, a family of vector spaces with invertible parallel transport along paths. At a boundary point \(x\), a transverse slice fixes the locations of the clusters and varies the differences inside them. The **normal link complex** \(K_x\) is the cochain complex, up to quasi-isomorphism, of the separated part of a sufficiently small transverse neighbourhood with coefficients in \(L\). Its cohomology comprises closed cochains modulo exact ones. In sheaf notation,
\[
 K_x=(Rj_*L)_x
     \simeq\bigl(\operatorname{Cone}(j_!L\longrightarrow Rj_*L)\bigr)_x .
\]
Here \(Rj_*L\) takes sections and their higher cohomology on the part of each neighbourhood lying in the open. The stalk is its value in arbitrarily small neighbourhoods of \(x\). Extension by zero \(j_!L\) has zero stalk at \(x\). Taking the cone of their comparison therefore leaves precisely \(K_x\) at \(x\).

If several distinct clusters collapse simultaneously, each has a scale circle. The separate loops must leave something in a common part of the *same* coefficient space. The criterion involves the generalized eigenspaces with eigenvalue one.

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

### Two ordered points on the sphere {#ch04-sphere-binary-collision}

For one pair on the plane the small circle of possible directions can be held fixed as the collision point moves. What happens when the collision point runs over a sphere? The circle of directions sits in its tangent plane, and these tangent planes form a nontrivial bundle. Let \(C=\mathbb P^1(\mathbb C)\simeq S^2\), let \(i:C\hookrightarrow C^2\) be the diagonal and let \(j:U=C^2\setminus i(C)\hookrightarrow C^2\). The first projection \(p:U\to C\) is a homotopy equivalence because its fibres are punctured spheres. Identify the normal to the diagonal by \((v_1,v_2)\mapsto v_2-v_1\) and write \(q:E=S(TC)\to C\) for its oriented unit tangent circle bundle. Now allow coefficients which are locally equivalent to bounded complexes of finite-dimensional vector spaces, called *perfect* complexes. Their parallel transport can carry homotopies as well as the transport on ordinary cohomology. For such a locally constant complex \(L\) on \(C\), the cochains of the normal circles fit together into the following complex on the diagonal,
\[
 \mathcal B(L)=i^*Rj_*p^*L\simeq Rq_*q^*L.
\]
In particular, \(p^*L=j^*(L\boxtimes\mathbb C)\) is a separated two-point input. On the normal circle bundle the first projection is \(q\), and the second is homotopic to \(q\) along the short normal geodesic. Thus two perfect inputs \(A,B\) give \(\mathcal B(A\otimes B)\). A constructible coefficient on \(C^2\) with open part \(p^*L\) and diagonal part \(W\) requires an attaching map \(W\to\mathcal B(L)\). If \(i\) includes the diagonal and \(P\) is the glued coefficient, the fibre of this map (its cone shifted by \([-1]\)) is \(i^!P\). It records sections and higher cohomology *supported* on the diagonal. This is the distinction between the ordinary restriction \(i^*P=W\) and the extraordinary restriction \(i^!P\).

Both strata are simply connected, so transport along ordinary loops on the base cannot detect any twisting. Nevertheless its tangent direction makes two turns around the equator in passing between hemispherical trivializations. The Euler number measuring this winding is \(2\). Even the constant coefficient on the direction bundle therefore has a nontrivial family of fibre cochains. Orient the sphere by \(\int_C\omega=1\) and let \(\vartheta\) be the positive angular form with fibre integral one. Then \(E\simeq\mathbb RP^3\), \(d\vartheta=-2q^*\omega\), and \(\gamma=\vartheta\wedge q^*\omega\) has integral one on \(E\). Take the southern horizontal frame minus the northern one along the equator, oriented as the boundary of the northern hemisphere. With this sign convention the positive generator of \(\pi_2(C)\) acts on the fibre cohomology of \(Rq_*\mathbb C\) by the degree-minus-one map \(T\theta=-2\), \(T1=0\), where \(\theta\) is the positive circle class. This is the Euler number of the tangent bundle with the indicated differential sign. For an input with cohomology in only two degrees, the class specifying how one cohomology sheaf is attached to the other is its Postnikov extension. The only possible nonzero such class on the sphere has base degree two. Since \(q^*\omega=-\frac12d\vartheta\) is exact, the pullback of this extension splits if no splitting is prescribed in advance.

Three degrees give a different answer. Give \(e_0,e_1,e_2\) degrees \(0,1,2\) and zero internal differential. For \(c=0,1\), let \(N_ce_2=e_1\), \(N_ce_1=ce_0\), \(N_ce_0=0\). On differential forms with values in these three graded fibres, \(\omega N_c\) raises form degree by two and lowers fibre degree by one. Thus \(D=d+\omega N_c\) has total degree one. Its square is zero since \(d\omega=0\) and a four-form on the sphere vanishes. This flat superconnection defines a perfect local system \(L_c\). Its ordinary cohomology sheaves in the three fibre degrees are the same for both choices of \(c\). On \(\mathcal B(L_c)\), tensoring the actions of \(N_c\) and \(T\) with the graded sign gives the following matrix from degree two to degree one:
\[
 (e_1\otimes\theta,e_2\otimes1)
 \longrightarrow (e_0\otimes\theta,e_1\otimes1),
 \qquad
 M_c=\begin{pmatrix}c&0\\2&1\end{pmatrix}.
\]
At \(c=0\) its rank is one. At \(c=1\) its determinant is one, so its rank is two. The different ranks arise from transport over a two-dimensional base even though the ordinary cohomology sheaves agree. To see the same distinction globally, pull the differential back to \(E\). Since \(d\vartheta=-2q^*\omega\), the first step from \(e_2\) can be cancelled explicitly. The remaining differential is
\[
 D\bigl(e_2+\tfrac12\vartheta e_1\bigr)=-\tfrac c2\,\gamma e_0 .
\]
Thus the dimensions of the global cohomology of \(\mathcal B(L_c)\), in degrees zero through five, are \((1,1,1,1,1,1)\) for \(c=0\) and \((1,1,0,0,1,1)\) for \(c=1\).

Even identical open and diagonal restrictions can have different attachments. Fix the constant open coefficient and \(W=\mathbb C[-3]\). A map \(W\to Rq_*\mathbb C\) is specified up to homotopy by a class in \(H^3(E;\mathbb C)\). The zero class and \([\gamma]\) agree on each individual direction circle. Taking global sections of their homotopy fibres gives dimensions \((1,1,1,1)\) and \((1,0,0,1)\) respectively in degrees \(1,3,4,5\). An all-arity unital factorization algebra on this geometry still requires compatible multiplications and a vacuum insertion. [Higher transport at the sphere collision](#atlas-c-sphere-binary-higher-transport)

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

The link tells us which nearby classes are available. It leaves a question at the collision point itself. Which of them does a section there restrict to? Fix the labelled transverse slice \(\mathbb C^3\) and let \(i\) include its origin. To impose the middle-perversity support and cosupport bounds, one works in the abelian category of perverse sheaves. In this convention a degree-zero local system on a smooth complex threefold is shifted by \([3]\), meaning its ordinary sheaf degree is now \(-3\). Subobjects and quotients in what follows are taken in this category. Put \(V=H^2K\) and \(V'=H^3K\). For this coefficient \(P_!=j_!L[3]\) is perverse. The intermediate extension \(j_{!*}L[3]\) is the extension with no nonzero subobject or quotient on the boundary. The canonical sequence is
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

The circle calculation measured what happens after continuation around a closed loop. For a connection with an irregular singularity, horizontal solutions can also grow or decay exponentially on approaching the collision. Two connections with identical loop transport can then give different cohomology at the collision. Consider three points. Take difference coordinates \(x=z_1-z_3\) and \(y=z_2-z_3\). Off the three collision lines \(xy(x-y)=0\), the slope \(u=x/y\) is defined. Pull back the two-dimensional connection whose horizontal columns satisfy
\[
dy_1=a y_2\,du,\qquad dy_2=-2u^{-3}y_2\,du .
\]
Its diagonal exponential factors are \(1\) and \(e^{1/u^2}\). The second component of a horizontal column is a multiple of \(e^{1/u^2}\), and the first is obtained by integrating \(a e^{1/u^2}du\). The Laurent series of this one-form has no \(u^{-1}du\) coefficient. Its integral around the puncture vanishes, so the ordinary analytic monodromy is trivial for every \(a\in\mathbb C\). At \(a=0\) the connection splits. To test splitting algebraically, let \(j\) include the complement of the collision lines, let \(i\) include their common origin, and put \(C_a=\operatorname{Cone}(j_!M_a\to j_*M_a)\) for the pulled-back connection \(M_a\). Use algebraic holonomic direct images and the de Rham normalization in which the constant connection on the plane gives \(\mathbb C[2]\).

The slope specifies the shape of the triple independently of its scale. On this angular curve the question is whether the equation for the first component splits algebraically. In the dual connection a rational primitive for its extension class would effect the splitting. Set \(r=y/x\). In the dual connection the differential on the exponential summand is \(Tq=q'+2rq\). The constant section of the trivial quotient has connecting class \(-a[r^{-2}dr]=-2a[dr]\), since \(T(-1/r)=r^{-2}-2\). The class \([dr]\) survives. A finite pole in a rational primitive would produce a higher pole on differentiation, while \(T\) sends a nonzero polynomial to one of positive degree. The radial factor contributes \(1\) and \(dx/x\). Duality and scalar contraction then give the dimensions of the extraordinary restriction \(H^{k}(i^!C_a)\), in degrees \(k=-1,0,1\):
\[
 (5,6,1)\quad(a=0),\qquad (4,4,0)\quad(a\ne0).
\]
This measurement decides whether the extension splits. One can also compare normalized asymptotic solutions in two sectors of approach to the irregular point. Their difference is measured by a Stokes multiplier. In the fixed graded frames the upper-minus-lower multiplier is \(2i\sqrt{\pi}\,a\). It is minus the period of the dual extension class on an upward rapid-decay contour between the two marked sectors. Changing a frame rescales the multiplier, while the costalk dimensions stay fixed.

Four points allow a different measurement. On the transverse space \(X=\mathbb A^3\) take \(s=z_2-z_1,\ x=z_3-z_1,\ y=z_4-z_1\). On the open \(j:U\hookrightarrow X\) of distinct points put \(r=x/s,\ t=y/s\). To the preceding angular connection \(N_a(r)\) attach a two-dimensional factor \(W\) with connection \(d-J\,d\log(t-r)\), where \(J^2=0\ne J\). Its monodromy around \(t=r\) is \(1+2\pi iJ\). Write \(M\) for the tensor product and \(C=\operatorname{Cone}(j_!M\to j_*M)\). The line \(L=\{x=y=s\}\) is the collision of labels \(2,3,4\), and \(i\) includes the total collision \(s=x=y=0\). Two collision flags approach \(L\), one through \(u=r-1=0\), the other through \(w=t-r=0\).

These two orders differ on a single logarithmic one-form. First let \(u\) become small compared with \(w\). The form \(\beta=d\log(1+u/w)\) is regular at \(u/w=0\), so its logarithmic residue there is zero. In the opposite order \(w/u\) tends to zero. The identity
\[
 d\log(1+u/w)=d\log(u/w)+d\log(1+w/u)
\]
then leaves \(d\log(u/w)\), since the second term has zero residue in that chart. The term \(1+u/w\) appears because the third normal divisor meeting the two flag divisors is \(u+w=0\).

To compare the resulting maps, the two limits need the same fibre coordinates. Keep the horizontal frame of \(N_a^\vee\) at \(r=1\) and transport the dual fibre of \(W\) in the same positive real chamber. Identify the two iterated restrictions by \(p=d\log u\), \(q=d\log w\). Write \(\alpha=d\log(u/w)\), \(\rho=p-q\), let \(P\) be the cochain complex on the simultaneous normal germ, and let \(T\) be the common complex for the iterated restrictions. With these choices their two maps \(F_u,F_w:P\to T\) are
\[
\begin{array}{c|ccc}
 &q&\alpha&\beta\\ \hline
 F_u&q&\rho&0\\
 F_w&q&\rho&\rho
\end{array}
\]
on logarithmic generators. Both keep the same differential \(d+J^{\mathsf t}q\wedge-\) on the dual of the two-dimensional coefficient \(W\). The comparison therefore asks whether the difference on \(\beta\) survives passage to cohomology and then to the total collision.

Let \(A\) be the unshifted algebraic de Rham complex on the angular surface \(r,t\notin\{0,1\},\ t\ne r\), with its dual coefficient. Write \(S:A\to P\) for restriction to the simultaneous normal germ and \(\lambda=d\log s\). Naturality of the localization triangle, with the boundary for extension by zero fixing the sign on both sources, gives the two maps
\[
 D_j=(1\otimes F_jS)^\vee[-1]:
 (\Lambda(\lambda)\otimes T)^\vee[-1]\longrightarrow
 (\Lambda(\lambda)\otimes A)^\vee[-1]\simeq i^!C[1],
 \qquad j=u,w .
\]
The ordinary outer star link along \(L\) supplies \(\Lambda(\lambda)\). With \(\mathrm{DR}(\mathcal O_X)=\mathbb C[3]\), ordinary degree \(m\) is dual to degree \(1-m\) in this target. For example, choose \(v\notin J^{\mathsf t}W^\vee\) with \(J^{\mathsf t}v\ne0\). A closed angular form \(g(r)v\,q\wedge d\log(t-1)\), with \(g=e=(1,-a/r)\) or \(g=f=(0,1)\) in the dual angular frame, restricts to zero under the first flag and to the nonzero class \(g(1)v\,q\wedge\rho\) under the second. Its product with \(\lambda\) detects the difference one degree lower after dualizing.

The explicit form distinguishes the two maps. To see how much of the total collision they account for, take the ranks of each map, the sum of their images, and their difference. The four entries in each tuple below are in degrees \(1,0,-1,-2\). The middle columns give image ranks on cohomology.

| Parameter | \(H^\bullet(i^!C[1])\) dimensions | Each flag | Sum of the images | \(D_w-D_u\) |
| --- | --- | --- | --- | --- |
| \(a=0\) | \((1,9,31,23)\) | \((1,4,5,2)\) | \((1,5,8,4)\) | \((0,1,3,2)\) |
| \(a\ne0\) | \((0,4,24,20)\) | \((0,2,4,2)\) | \((0,2,6,4)\) | \((0,0,2,2)\) |

The pair \((F_u,F_w)\) is split injective on the normal complex. Its dual therefore spans the image of the localization boundary from \(L\), a proper subspace of the vertex cohomology in both rows.

What happens when labels 2 and 4 meet first? Their collision is \(t=1\), or \(u+w=0\). Keep \(w\) as the scale and use \(\xi=(u+w)/w\) at this third puncture. Then \(u=w(\xi-1)\). On its punctured normal disc, \(\alpha=d\log(1-\xi)\) has a holomorphic primitive, while \(\beta=d\log\xi\) represents the positive class \(\eta\). Thus restriction \(F_c\) on cohomology takes \([p]=[d\log u]\) and \([q]=[d\log w]\) to the same class \([q]\). Two test forms separate the outcomes:
\[
 F_c[q\wedge p]=0,\qquad F_c\bigl[q\wedge d\log(t-1)\bigr]=[q\wedge\eta] .
\]
The last class pairs to \((2\pi i)^2\) with the product of the positive \(w\)- and \(\xi\)-circles, in that order. With the coefficient \(v\) above it survives modulo \(J^{\mathsf t}W^\vee\).

On the exceptional line with coordinate \(u/w\), take positive meridians at \(0,\infty,-1\) in that order. Their scalar residues on \((\alpha,\beta)\) are \((1,0),(-1,-1),(0,1)\). At infinity the positive parameter is \(w/u\), so its logarithm has differential \(-\rho\) in the earlier table. The three rows sum to zero on the angular one-forms. Each restriction also carries the constant \(1\) to \(1\). Any two rows recover both angular coefficients, and every pair retains the radial complex. Hence any two boundary images span the same image from \(L\).

For the third boundary alone the global angular images have dimensions \((1,2,2)\) for \(a=0\) and \((0,0,2)\) otherwise. In the latter case all degree-one classes reaching the simultaneous normal complex are multiples of \(\alpha\), which dies at \(\xi=0\). In both cases the two horizontal coefficients in degree two multiply \(\bar v\,q\wedge\eta\), where \(\bar v\) is the class of \(v\) modulo \(J^{\mathsf t}W^\vee\). Including \(1\) and \(\lambda\) from the outer link changes \((x,y,z)\) to \((x,x+y,y+z,z)\). The third image in degrees \(1,0,-1,-2\) therefore has ranks \((1,3,4,2)\) and \((0,0,2,2)\), respectively. Comparing these algebraic maps with independently defined sectorial specialization still requires the Stokes filtrations, sectors and their identification with the chosen markings.

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
Indeed, if \(x_1=x_3\), both cuts have a coincident pair across the cut. Conversely, if both cuts fail and \(x_1\ne x_3\), the first failure forces \(x_1=x_2\) and the second forces \(x_2=x_3\), a contradiction. Thus the first and third points can obstruct every consecutive cut while the second point lies elsewhere. This bounds where a coefficient can survive the cuts. Chapter 5 gives examples supported on the small diagonal and on all of \(\Delta_{13}\).

The full ordered collision atlas is constructed from one chart \(X^I\) for each total order on the labels. Two charts are glued where their orders agree within every set of coincident labels. The coefficient systems use extraordinary pullback along surjections with ordered fibres. Their convolution sums over all ordered decompositions \(I=A\sqcup B\), with the blocks separated. This convolution is symmetric monoidal, although an associative algebra for it may have noncommutative multiplication.

Word convolution instead uses the initial and final intervals of one fixed order and is nonsymmetric. Restricting an atlas system to its increasing chart and projecting onto those consecutive decompositions gives the cut coproduct. The projection is generally not an equivalence: at two distinct points it can discard the reverse-order summand. Consequently the two convolutions, and the factorization conditions attached to them, remain distinct.

In formulas, let \(F_n,G_n\) denote the coefficients of words of length \(n\). The consecutive-cut convolution is
\[
 (F\star G)_n=\bigoplus_{p+q=n}Rj_{p,q*}j_{p,q}^*
      (F_p\boxtimes^{\mathbf L}G_q).
\]
Here \(j_{p,q}\) is the inclusion (4.9). The external derived tensor puts the two independent coefficients on their respective blocks, restriction imposes separation, and the derived direct image retains the cohomology of the nearby separated configurations. The unit \(k_\varnothing\) is supported on the empty word. An augmented associative algebra \(A\) for this convolution has a coherent multiplication \(A\star A\to A\) and a map \(A\to k_\varnothing\). Require this augmentation to be an equivalence on the empty word.

To express factorization of \(A\), form its bar coalgebra \(BA\). Its differential records multiplication of adjacent factors and, more generally, their associativity homotopies. Its coproduct splits a word. The required factorization map for each \(p,q>0\) is the restriction of this coproduct,
\[
 (BA)_{p+q}|_{U_{p,q}}\longrightarrow
 \bigl((BA)_p\boxtimes^{\mathbf L}(BA)_q\bigr)|_{U_{p,q}},
\]
and it must be an equivalence. Conversely the associative *cobar* construction forms an algebra from a coalgebra, with differential induced by its coproduct. For coefficients reduced at the empty word, a convolution of more than \(n\) positive factors vanishes on \(n\) labels. This finite filtration gives the bar–cobar equivalence between connected augmented associative algebras and connected coaugmented coassociative coalgebras in each of the two coefficient categories, with its own convolution. [Chapter 5](05-bar-and-coherence.md#ch05-the-support-remembers-which-cuts-were-allowed)

One can now compare this associative construction with the chiral Lie bracket. Chiral Chevalley chains arrange the iterated brackets into a coalgebra on all finite-set collisions. Restrict to order-preserving surjections and project the coproduct onto the consecutive cuts. Applying associative cobar gives an associative chiral algebra of configuration complexes. A comparison with the original fields and their vacuum requires further data. To reverse the passage, the entire bar coalgebra would have to extend to every finite-set surjection with a compatible cocommutative coproduct and factorization on disjoint opens. The missing summand at two distinct labels and the additional collision open at \((x,y,x)\) explain why mere symmetry away from collisions does not give this extension. [Chapter 12](12-chiral-quantum-groups.md#ch12-associative-products-on-configurations)

On a word of three letters the two consecutive cuts give the two bracketings of the product. If their composites agree only up to homotopy, the differential in the bar construction must record that homotopy and its compatibility with the next multiplication.

::: figure fig-ordered-cut-support
