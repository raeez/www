# Actions and derived centres

A boundary algebra describes products of boundary fields. Recovering operations that can act on the boundary introduces a different question: how must those operations respect multiplication, changes of position and collisions? For an ordinary associative algebra, the centre answers the first part. For a chiral algebra, compatibility includes operations supported where points meet and homotopies between different ways of approaching that locus.

Two comparison problems arise. One computes derived maps from a small exterior algebra into a vertex algebra. The other asks whether an operation on a factorizing coalgebra is determined by its value on the vacuum. Both lead to explicit rational differential forms and residues. Their conclusions concern different mapping spaces, so the map connecting those spaces must itself be constructed.

## Central operations on modules {#ch07-central-operations-on-modules}

Let \(A\) be a unital associative algebra over a characteristic-zero field \(k\). Its centre is
\[
Z(A)=\{z\in A:za=az\text{ for every }a\in A\}.
\]
For every left \(A\)-module \(M\), a central element gives an \(A\)-linear operator \(m\mapsto zm\), naturally in \(M\). Conversely, every natural endomorphism of the identity functor on \(A\)-modules arises this way. Indeed, its value on the regular module is determined by \(z=\eta_A(1)\). Naturality with respect to right multiplication by \(a\) gives \(az=za\); naturality with respect to \(A\to M, b\mapsto bm\), then gives \(\eta_M(m)=zm\).

Thus the same element acts compatibly on every representation. This explains why a centre is relevant to bulk–boundary questions: an operation that can be moved without changing its interaction with boundary observables should produce compatible operators on boundary representations. Additional geometric structure is needed to turn this motivation into a statement about a field theory.

The module interpretation also explains the derived replacement. Write \(A^e=A\otimes_k A^{\mathrm{op}}\). An \(A\)-bimodule map \(A\to A\) is determined by a central element, so
\[
Z(A)=\operatorname{Hom}_{A^e}(A,A).
\]
Replacing Hom by its derived functor gives the Hochschild cochain complex
\[
C^\bullet(A,A)\simeq R\operatorname{Hom}_{A^e}(A,A).
\]
For an ordinary algebra over \(k\), the bar resolution represents this complex by \(C^n(A,A)=\operatorname{Hom}_k(A^{\otimes n},A)\). Its first differentials are
\[
(bz)(a)=az-za,\qquad
(bf)(a_1,a_2)=a_1f(a_2)-f(a_1a_2)+f(a_1)a_2.
\]
Consequently \(HH^0(A)=Z(A)\), while \(HH^1(A)\) consists of derivations modulo inner derivations. Higher degrees retain further compatibility data.

A class represented by a bimodule map \(A\to A[n]\) acts on a derived left module through
\[
M\simeq A\otimes_A^L M
\longrightarrow A[n]\otimes_A^L M\simeq M[n].
\]
Here differentials have degree \(+1\), and \(V[1]^j=V^{j+1}\). The derived centre retains these operations and their coherent compositions. Hochschild cochains carry an \(E_2\)-algebra structure: products are accompanied by homotopies encoding their interchange. On cohomology this includes the cup product and the degree-minus-one Gerstenhaber bracket. An equivalence of underlying complexes alone does not identify those operations. See [Higher Algebra, §5.3.1](https://www.math.ias.edu/~lurie/papers/HA.pdf) and [Gerstenhaber’s construction](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Ger63.pdf).

For a small calculation, take \(A=k[x]/(x^2)\). The ordinary centre is all of \(A\). A derivation is determined by \(f(x)=a+bx\), but
\[
0=f(x^2)=2x f(x)=2ax
\]
forces \(a=0\). Since \(A\) is commutative, inner derivations vanish. Hence
\[
HH^0(A)=k\oplus kx,\qquad HH^1(A)=k\delta,
\qquad \delta(x)=x.
\]
The higher operation is visible even here: \( [\delta,x]=\delta(x)=x\). The centre and the degree-one class do not merely coexist as vector spaces; the bracket records how the derivation acts on the central element. A list of cohomology dimensions would omit this information.

## A factorizing actor and its pointing {#ch07-a-factorizing-actor-and-its-pointing}

Work on \(X=\mathbb A^1_k\). A differential module is a sheaf with an action of differential operators; it keeps track of how coefficients vary with position. We use coaugmented, counital coalgebras with empty coefficient \(k\). A factorizing coalgebra assigns complexes of differential modules to finite labelled configurations, including their ordered collision charts. For an ordered division \(I=A\sqcup B\), its coproduct restricts on the locus where the two blocks are disjoint to an equivalence
\[
F_I\big|_{U_{A,B}}
\simeq (F_A\boxtimes F_B)\big|_{U_{A,B}}.
\]
Successive divisions come with coassociativity homotopies and their higher compatibilities. Maps preserve these data, including the collision restrictions. The two orders \(A|B\) and \(B|A\) are distinct data unless a suitable cocommutative structure is supplied.

We call such a coalgebra an **actor** when it parametrizes operations on another object. The word does not add a multiplication to \(F\). Two tensor products occur. Disjoint convolution, written \(\star\), combines configurations by splitting their labels; its unit \(K\) is concentrated at the empty configuration. The tensor \(\otimes^!\) combines two coefficient systems at the same configuration by extraordinary pullback along the diagonal. Its unit \(J\) has the local unit coefficient at each configuration. A pointing is an actual coherent coalgebra map
\[
u:J\longrightarrow F.
\]
It specifies a vacuum operation together with all its compatibility homotopies. It contains more information than a class in the singleton cohomology. These conventions are those of the [ordered-collision coalgebra construction](#ref-ch07-01), particularly its coalgebra category and diagonal tensor.

The smallest useful test algebra has two orthogonal idempotents:
\[
B=kp_1\oplus kp_2,\qquad p_ip_j=\delta_{ij}p_i.
\]
Let \(C=C_B\) be its Chevalley coalgebra: its coefficients are built from finite partitions with a \(B\)-label on each block, and its differential merges blocks using the product of \(B\). It has multiplication \(m:C\otimes^!C\to C\) and total unit pointing \(u_B:J\to C\). The two idempotents distinguish two colours of input and output.

A character of \((F,u)\) is a coalgebra map \(g:F\to C\) together with a specified homotopy \(gu\simeq u_B\). An action is a coalgebra map \(\alpha:F\otimes^!C\to C\) together with a specified homotopy \(\alpha(u\otimes^!1_C)\simeq1_C\). There is no additional associative-action axiom involving a multiplication on \(F\). To retain the specified homotopies and homotopies between them, define the complete spaces
\[
\begin{aligned}
\mathcal X(F,u)
&=\operatorname{hofib}_{u_B}\left[
\operatorname{Map}_{\mathrm{Coalg}}(F,C)
\xrightarrow{u^*}\operatorname{Map}_{\mathrm{Coalg}}(J,C)\right],\\
\mathcal A_C(F,u)
&=\operatorname{hofib}_{1_C}\left[
\operatorname{Map}_{\mathrm{Coalg}}(F\otimes^!C,C)
\xrightarrow{(u\otimes^!1_C)^*}\operatorname{Map}_{\mathrm{Coalg}}(C,C)\right].
\end{aligned}
\]
A homotopy fibre records a point upstairs and a path from its image to the specified base point; its higher simplices record the remaining compatibilities.

There are explicit maps
\[
\Theta(g)=m(g\otimes^!1_C),\qquad
\Psi(\alpha)=\alpha(1_F\otimes^!u_B).
\]
The first turns a character into an operation by multiplication. The second evaluates an operation on the target vacuum. The unit identity gives \(\Psi\Theta\simeq1\). **Recognition** asks whether \(\Theta\Psi\simeq1\) as well, on the full action space. This requires a coherent reconstruction of the operation, not only agreement on singleton values.

A centre representing this geometric action problem would be a pointed actor \(Z_C\) with a universal action, such that
\[
\operatorname{Map}_{J/}\bigl((F,u),Z_C\bigr)
\simeq\mathcal A_C(F,u)
\]
naturally for every admitted actor. Existence is part of that assertion. The binary recognition question tests whether \(C\), with its multiplication action, has this property on a specified family of actors. It does not identify the action problem with the Hochschild complex of the two-dimensional algebra \(B\).

Derived maps can be represented using roofs
\[
P\xleftarrow{\simeq}Q\longrightarrow R,
\]
where the left arrow is a weak equivalence in the category being used. A common refinement replaces \(Q\) by another source and compares both legs. For pointed factorizing coalgebras, the pointing and the collision homotopies also belong to the diagram. For ordinary dg vertex algebras, the weak equivalences below are quasi-isomorphisms of state complexes. These two uses of roofs have different objects and weak equivalences. Comparing their mapping spaces requires a map that preserves both legs, their evaluation and their refinements.

::: figure fig-character-action-comparison

## Recognition on Chevalley coalgebras {#ch07-recognition-on-chevalley-coalgebras}

Let \(V\) be a dg chiral algebra. Its main-diagonal Chevalley coalgebra \(C_V\) is built from finite partitions of the labelled inputs, with a \(V\)-coefficient on each block. Its differential combines the internal differential of \(V\) with mergers using the chiral product. “Main-diagonal” specifies where the original one-point coefficients enter this construction; it is not a replacement by the cohomology of \(V\).

**Recognition theorem.** Suppose \(V\) is any unbounded dg chiral algebra over a characteristic-zero field on \(\mathbb A^1\), with a genuine closed horizontal unit. For every coherent coassociative pointing \(u:J\to C_V\), the maps \(\Theta\) and \(\Psi\) are inverse equivalences between \(\mathcal X(C_V,u)\) and \(\mathcal A_C(C_V,u)\). No homotopy from \(u\) to the genuine unit pointing is required. The equivalence is natural under all pointed coalgebra maps between these objects, including those that preserve no chosen presentation. [Arbitrary-pointing recognition](#ref-ch07-02).

The proof resolves the complete mapping diagrams and filters the terms by mismatches between input and output colours. The genuine unit supplies a contraction of the absolute layers. The arbitrary pointing determines the restriction map between those layers; it is retained throughout. Taking the fibre of that restriction gives the relative layer, whose contraction includes the correction joining the two absolute contractions. At each fixed configuration only finitely many partition steps occur. This finite geometric filtration proves an equivalence of the nonlinear mapping spaces even when the coefficient complexes are unbounded. Vanishing of a tangent complex at one point would not establish the same assertion.

There is also a module family. For an arbitrary unbounded complex \(M\) of right differential modules, form \(P(M)\) by assigning either a unit coefficient or an \(M\)-coefficient to each label. In a summand with several \(M\)-labels, those labels must occupy distinct positions, and an \(M\)-label is last in any equality block containing it. Restrict the external tensor of the assigned coefficients to that open, extend it by the direct-image functor, and sum over assignments. Projection to the summand with only unit coefficients gives \(P(M)\to J\).

For
\[
F=P(M)\otimes^!C_V,\qquad h:F\longrightarrow C_V,
\]
every pointing \(u\) gives the complete projected pointing \(hu\). Pullback along \(h\) identifies both character and action spaces with those of \((C_V,hu)\). Recognition therefore holds for every \(u\) in this family. No boundedness, finite generation, holonomicity or restriction on the connection of \(M\) is imposed. The proof contracts the positive \(M\)-sectors as two-sided coefficient modules, rather than requiring the pointing to preserve those sectors. [Radical reduction](#ref-ch07-03).

A nonunital chiral algebra \(W\) has a genuine unitization \(W^+=W\oplus\omega_X\), where \(\omega_X\) is the right differential-module unit on the curve. The inclusion gives \(i:C_W\to C_{W^+}\), pointed upstairs by the entire composite \(iu\).

**Unitization theorem.** Let \(W\) be an arbitrary unbounded, possibly noncommutative and nonconstant nonunital dg chiral algebra on \(\mathbb A^1_k\). Suppose its coherent pointing \(u\) admits a strict closed horizontal degree-zero state \(a:\omega_X\to W\) such that
\[
H^0(a)=H^0(u_1):\omega_X\longrightarrow H^0(W).
\]
Then restriction along \(i\) induces equivalences on both complete character and action fibres. Consequently \(\Theta\) and \(\Psi\) are inverse for \((C_W,u)\), naturally on the full stated subcategory. The displayed equality is only in ordinary cohomology. Equality of \(a\) and \(u_1\) in full derived Hom is not a hypothesis. [Unitization from an ordinary horizontal representative](#ref-ch07-04).

The strict state supplies a central chain-level multiplier on \(W^+\). Binary naturality of the pointing makes its action idempotent on every cohomology module. Localizing that multiplier and its complement gives actual chiral quasi-isomorphisms
\[
W\longrightarrow E\times N,\qquad
W^+\longrightarrow E\times N^+,
\]
in a commuting square with the two unitization inclusions. Here \(E\) is genuinely unital. The transported coherent pointings have ordinary singleton classes equal to the unit on \(E\) and zero on \(N^+\); the derived zero/unit singleton theorem promotes these particular classes to the required derived equalities. It does not replace the higher pointing cells. The split comparison then reduces both full fibres to the genuinely unital theorem. If \(H^0(u_1)=0\), both required fibres are empty.

For quasicoherent commutative dg \(\mathcal O_X\)-algebras with a compatible connection, recognition holds for every coherent pointing without this representative hypothesis. This includes all unbounded nonunital constant commutative examples, and also nonconstant examples whose ordinary singleton class has no strict horizontal representative. Thus the two results have overlapping, different domains. [Commutative algebras with connection](#ref-ch07-05).

## Ordinary exterior sources and the map they compute {#ch07-ordinary-exterior-sources-and-the-map-they-compute}

Let \(\mathcal V\) be the category of ordinary algebraic unital \(\mathbb Z\)-graded dg vertex superalgebras over \(\mathbb C\), with parity given by degree modulo two, localized at maps inducing isomorphisms on all cohomology groups of the state complex. “Ordinary algebraic” means that the state spaces and tensors are the algebraic ones; no completed state product is implicit. Write \(d\) for the internal differential and \(T\) for translation, with \(dT=Td\).

For one exterior generator \(\epsilon\) of odd degree \(a\), with \(d\epsilon=T\epsilon=0\), the source comparison is
\[
\operatorname{Map}_{\mathcal V}(\Lambda(\epsilon),B)
\simeq Z^a(B^{hT}\otimes\Omega_\bullet),\qquad
(B^{hT})^j=B^j\oplus B^{j-1},
\]
where \(D(b,b')=(db,Tb-db')\). Here \(\Omega_n\) is the algebra of polynomial differential forms on the standard \(n\)-simplex. The notation \(Z^a\) means closed total-degree-\(a\) elements. A point therefore contains a closed state and a chosen homotopy killing its translation. The components are \(H^a(B^{hT})\), and \(\pi_n=H^{a-n}(B^{hT})\) for \(n\ge1\). Every odd integer \(a\), including negative \(a\), is allowed; \(B\) can be noncommutative and unbounded. [Odd-degree exterior sources](#ref-ch07-06).

For two degree-one generators, mixed homotopies are essential. Put \(A=\Lambda(\epsilon_1,\epsilon_2)\), with zero differential and translation. Define \(N(B)_n\) as the six-tuples
\[
(e_1,e_2,u_1,u_2,\beta,\zeta)\in B\otimes\Omega_n,
\qquad |e_i|=1,\quad |u_i|=|\beta|=0,\quad |\zeta|=-1,
\]
satisfying
\[
de_i=0,\qquad du_i=Te_i,\qquad
d\beta=u_{1(0)}e_2,\qquad
d\zeta=T\beta-u_{1(0)}u_2.
\]
The zero product \(u_{(0)}v\) is the coefficient of \(z^{-1}\) in \(Y(u,z)v\); \(d\) in these equations includes the simplex differential. The \(u_i\) record translation homotopies, while \(\beta\) and \(\zeta\) record their mixed relation and its translation compatibility.

**Binary exterior-source theorem.** The specified comparison
\[
\rho_B:\operatorname{Map}_{\mathcal V}(A,B)\longrightarrow N(B)
\]
is an equivalence for every ordinary algebraic dg vertex algebra \(B\), with arbitrary translation, no commutativity assumption and no boundedness assumption. [Logarithmic quotient construction](#ref-ch07-07).

To define this map on roofs, use the free vertex algebras on those six cells with increasing locality allowances. Their differentials are exactly the displayed equations. Each sufficiently large stage evaluates on a given finite tuple. The decisive construction supplies ordinary quotients \(R_m\) with specified state quasi-isomorphisms \(R_m\to A\) and strict factorizations
\[
F_{m+2}\longrightarrow R_{m+2}\longrightarrow F_m
\]
of the actual free transition. This **exact interpolation** allows roof maps, homotopies and finite diagrams to pass through the same tuple comparison. The free stages themselves need not be quasi-isomorphic to \(A\); the quotients and strict transition factorization supply that comparison. The quotient is constructed from logarithmic rational forms. Its restricted dual has the de Rham differential together with collision residues; finite colour filtrations and a tensor resolution with \(dt=yx-xy\) compute its cohomology. The tensor resolution leaves ordered polynomial words in every charge; the subsequent Lie and symmetric-state constructions give the four exterior classes of \(A\).

For \(B=\mathbb C\), this theorem can be calculated directly. Translation and every zero product vanish. The three degree-zero coordinates \(u_1,u_2,\beta\) are closed polynomial functions on a simplex, hence constant. The coordinate \(\zeta\) vanishes because polynomial forms have no negative degree. Each \(e_i\) is a closed one-form, and its simplicial cocycle space is \(K(\mathbb C,1)\). Thus
\[
\operatorname{Map}_{\mathcal V}(A,\mathbb C)
\simeq\mathbb C^3_{\mathrm{disc}}\times K(\mathbb C^2,1).
\]
There is only one strict graded algebra map \(A\to\mathbb C\), yet the derived mapping space has these additional components and loops. They are the homotopy data carried by roofs, not further choices of the images of the degree-one generators in degree one of \(\mathbb C\).

### The genuine Heisenberg fibre reduces to automorphisms {#ch07-genuine-heisenberg-fibre}

The ordinary exterior-source theorem leaves a more specific action problem for the nonzero-level Heisenberg vertex algebra \(H=V_\kappa\), \(\kappa\ne0\). Let \(B=\Lambda(\epsilon)\), with \(|\epsilon|=1\) and \(d\epsilon=T\epsilon=0\). In the same ordinary dg vertex localization, retain the full actor-roof category and the genuine unit fibre
\[
q_B:N\operatorname{Act}_{\mathrm{roof},H}(B)\longrightarrow F,
\qquad
F=\operatorname{hofib}_{\mathrm{id}_H}
\bigl[\operatorname{Map}(B\otimes H,H)
\longrightarrow\operatorname{Map}(H,H)\bigr].
\]
Both roof legs, all admitted boundary arrows and the path specifying compatibility with the unit belong to these spaces. Energy-changing arrows are included.

The actual tuple augmentation \(\Pi:F\to\mathbb C^2_{\mathrm{disc}}\times K(\mathbb C,1)\) has weak-equivalence composite \(\Pi q_B\). It therefore computes the source and its detected image. Convolution and the actual roof translations further give
\[
F\simeq\mathbb C^2_{\mathrm{disc}}\times F^0,
\]
where \(F^0\) is the whole zero sector of the charge and constant detector. This sector is not known to be connected.

There is now a description of the remaining based fibre using actual automorphisms. Form the square-zero extension
\[
X_1=H\oplus\epsilon_1H,
\qquad |\epsilon_1|=1,
\quad \epsilon_1^2=d\epsilon_1=T\epsilon_1=0,
\]
with its canonical section and projection. Work in the genuine pointed slice \(\mathcal V_{H//H}\), which retains both the under-\(H\) and over-\(H\) homotopies. Let \(U\) be the space of its automorphisms of \(X_1\) that induce the identity on state cohomology. At the trivial action \(\alpha_0\), define
\[
\Phi=\operatorname{hofib}_0
\bigl[F_{\alpha_0}\xrightarrow{\delta}K(\mathbb C,1)\bigr],
\]
where \(F_{\alpha_0}\) is the connected component of \(\alpha_0\). The scalar section makes \(\Phi\) connected, and the genuine loop comparison gives
\[
U\simeq\Omega\Phi,
\qquad
q_B\text{ is an equivalence}
\Longleftrightarrow
F^0\text{ is connected and }U\text{ is contractible}.
\]
This is an exact reduction of the original problem; neither condition on the right is established. [Genuine fibre reduction](atlas.html#atlas-c-centre-genuine-heisenberg-fibre-reduction).

The two requirements measure different possible defects. Based loops test extra automorphisms in the component of the trivial action, but they cannot detect another component of the whole zero sector. Nor can endomorphism composition be replaced by loop addition: composition multiplies the detected scalars and has identity scalar \(1\), while loop concatenation adds scalars and has identity \(0\). The proved splitting is a statement about spaces over the scalar set, with no product decomposition for composition. [The remaining equivalence](atlas.html#atlas-c-centre-genuine-heisenberg-equivalence).

## Residues with spectators {#ch07-residues-with-spectators}

Adding fixed field insertions to the source produces rational forms with **spectators**: labelled positions \(z_1,\ldots,z_r\) that remain as parameters while auxiliary marked positions \(w_1,\ldots,w_m\) are differentiated or absorbed by residues. Three sets of nonnegative integer bounds control the poles: \(N_{ij}\) for spectator pairs, \(b_j\) for a marked point meeting spectator \(j\), and a positive odd integer \(\mu\) for marked pairs.

Here is the rational complex to which the strict vanishing results apply. Choose a subset \(S\subseteq\{1,\ldots,r\}\) of selected spectators, put \(s=|S|\), and fix the charge \(q=m+s\). A degree-\(i\) form in the marked variables contributes to total degree \(n=2s+i\). It is anti-invariant under permutations of the marked variables, acting on both coefficients and differentials. The coefficient of \(dw_I\) has the following pole bounds:
\[
\begin{array}{c|c}
\text{divisor}&\text{maximum pole order}\\ \hline
w_a=w_b&\mu+\mathbf1_{\{a,b\}\cap I\ne\varnothing}\\
w_a=z_j&b_j+\mathbf1_{a\in I}\quad(j\notin S)\\
w_a=z_j&2b_j+\mu+1+\mathbf1_{a\in I}\quad(j\in S)\\
z_i=z_j&N_{ij}\quad(|\{i,j\}\cap S|=0)\\
z_i=z_j&N_{ij}+b_i+b_j+1\quad(|\{i,j\}\cap S|=1)\\
z_i=z_j&N_{ij}+2b_i+2b_j+\mu+2\quad(|\{i,j\}\cap S|=2).
\end{array}
\]
No other poles are allowed. A total-degree-\(n\) family is \(\Phi=(\phi_S)_S\), where \(\phi_S\) is a form of degree \(n-2|S|\) in \(q-|S|\) marked variables satisfying the displayed bounds. A component is zero unless \(0\le n-2|S|\le q-|S|\). For every \(i\ne j\), \(i\in S\), \(j\notin S\), put \(S'=(S\setminus\{i\})\cup\{j\}\). The additional relation is, coefficientwise,
\[
\phi_S+\varepsilon_{S;i,j}\phi_{S'}
\quad\text{has pole order at most }N_{ij}\text{ along }z_i=z_j.
\tag{R}
\]
To define the sign, let \(\theta_1,\ldots,\theta_r\) be anticommuting symbols and write \(\theta_S\) for their product in increasing order. Using a common anticommuting symbol \(\theta\), set \(\varepsilon_{S;i,j}\in\{1,-1\}\) by
\[
\left.\theta_S\right|_{\theta_i=\theta}
=\varepsilon_{S;i,j}
\left.\theta_{S'}\right|_{\theta_j=\theta}.
\]
For \(|S|=1\), relation (R) says that \(\phi_{\{i\}}+\phi_{\{j\}}\) has pole order at most \(N_{ij}\) along \(z_i=z_j\). The relation couples the components associated with the two possible selected spectator labels.

Denote the resulting complex by \(D_{r,q}(b,N;\mu)\). Its differential is marked de Rham differentiation plus the signed residues \(\operatorname{Res}_{w=z_j}\), which convert a marked variable into a selected spectator. A residue lowers form degree by one and increases \(s\) by one, so both differential terms raise \(2s+i\) by one. The left-residue convention, extracting the indicated \(dw\) first, makes these terms anticommute.

The charge-one case explains why the charge restriction in the theorem below matters. With one spectator and \(N=0\), put \(y=w-z\). The complex is
\[
y^{-b}\mathbb C[z,y]
\xrightarrow{d_y}
y^{-b-1}\mathbb C[z,y]\,dy
\xrightarrow{\operatorname{Res}_{y=0}}
\mathbb C[z].
\]
A Laurent monomial \(y^jdy\) has the primitive \(y^{j+1}/(j+1)\) unless \(j=-1\); the allowed bound puts that primitive in the first term. The missing monomial \(dy/y\) maps to \(1\) under the residue. Hence the last two cohomology groups vanish, while \(H^0=\mathbb C[z]\). For several spectators the analogous surviving module is
\[
M_N(r)=\left(\prod_{i<j}(z_i-z_j)^{-N_{ij}}\right)
\mathbb C[z_1,\ldots,z_r].
\]
It survives at \(q=1\), independently of \(\mu\).

**Strict three-spectator theorem.** For \(r=3\), every \(b_j,N_{ij}\ge0\), every positive odd \(\mu\), and every charge \(q\ge2\),
\[
H^n(D_{3,q}(b,N;\mu))=0\qquad(n<q).
\]
This holds over the whole polynomial spectator base, including simultaneous collisions, and in every homogeneity. The conclusion \(H^n=0\) for \(q\ge2\) and \(n<q\), with positive odd \(\mu\), also holds for \(r=2\) and arbitrary nonnegative \(b,N\), and for arbitrary \(r\) when every \(b_j=0\) and \(N_{ij}\ge0\). A further total theorem gives \(H^n(D_{4,5})=0\) for \(n<5\), with \(b=(1,1,1,1)\), \(\mu=1\) and arbitrary \(N_{ij}\ge0\). [Three-spectator proof](#ref-ch07-08); [four-spectator charge-five proof](#ref-ch07-09).

For three spectators, filter by the selected count \(s\). The associated graded differential is marked de Rham differentiation. The columns at \(s=0,1,2,3\) have lower total-degree bounds \(q-1,q,q,q+2\). These are lower bounds, not assertions that a nonzero term occurs there: absent columns and nonnegative form degree raise the actual starts at small \(q\). Only the unselected column can contribute below \(q\). Its possible degree-\(q-1\) class maps injectively under the actual first residue into the constrained one-selected column, so it disappears. The filtration is finite, which gives convergence to the original total complex without a completion argument.

The column bounds require more than pole counting. They use exact image ideals, their intersections along collision strata, and the differential-module connections. Multiplication by the common spectator factor \(\prod(z_i-z_j)^{N_{ij}}\) then identifies the prescribed rational modules with their \(N=0\) versions. This is a chain isomorphism between those modules, not an assertion that the factor is a unit in the polynomial base.

There is a uniform statement for the first compatibility of pairwise data. Let \(r\ge1,m\ge0\), all \(b_j=1\), \(\mu=1\), and \(N_{ij}=0\). Over \(S=\mathbb C[z_1,\ldots,z_r,c_1,\ldots,c_m]\), set
\[
\begin{gathered}
P(X)=X^m+c_1X^{m-1}+\cdots+c_m,\qquad t_{ij}=z_j-z_i,\\
\Delta=\prod_{i<j}t_{ij}^3,\qquad G_i=P(z_i)^3,\\
F_i=\left(\prod_{a<b,\ i\notin\{a,b\}}t_{ab}^3\right)
       \prod_{j\ne i}G_j,\qquad \mathfrak a=(F_1,\ldots,F_r).
\end{gathered}
\]
For \(m=0\), take \(P=1\). The literal identity
\[
\bigcap_{i<j}(\mathfrak a,t_{ij}^3)=(\mathfrak a,\Delta)
\]
says that compatible pairwise principal parts in the specified image modules arise from a single joint source. Its proof uses the actual coefficient lattice, whose projective dimension is at most two for \(m\ge2\), and induction along collision partitions with the outside polynomial factors retained. The identity establishes this first compatibility; it does not establish the second compatibility or total vanishing for arbitrary \(r\). [First compatibility defect](#ref-ch07-10).

The strict inequality cannot be replaced by \(n\le q\) at fixed bounds. With \(r=2\), \(q=4\), \(b=(1,1)\), \(N_{12}=0\) and \(\mu=1\), the rational complex has a nonzero class in \(H^4\). Such a class may die after the pole bounds are enlarged. A fixed-bound counterexample and an eventual comparison through larger bounds are therefore different mathematical statements. [The fixed-bound residue class](#ref-ch07-11).

## The remaining comparison {#ch07-the-remaining-comparison}

The geometric action problem also has concrete higher homotopies. For arbitrary unbounded coassociative actors, the prescribed three-block pointed boundary has a filling with its original root, marks and scalar pointing retained. Its construction uses two genuine vacuum labels, their proper deletion edges and full differential-module residue maps; it cancels the action-generated residue without declaring the entire normal kernel contractible. No cocommutativity assumption is needed. [Three-block filling](#ref-ch07-12).

A separate comparison of two prescribed mixed primitives holds on the old separated locus \(z_0\ne z_1\) when the underlying \(F\) has a supplied coherent cocommutative structure. The action and pointing themselves need only be coassociative. It fills the specified closed difference and its corner restriction; it does not extend across the old collision diagonal. These hypotheses must remain distinct from those of the three-block theorem. [Separated-base primitive comparison](#ref-ch07-13).

Recognition for arbitrary pointed factorizing actors still asks for \(\Theta\) to be an equivalence with all changes of roots, collision restrictions and arbitrarily long refined words. The constructions above provide particular parts of that comparison. They do not supply the whole family. Likewise, the ordinary binary exterior-source theorem computes its stated vertex-algebra mapping space; a comparison with the geometric action space must additionally preserve the original actor, both roof legs, evaluation and every required incoming refinement. For sources with further generators and spectators, exact interpolation must still be constructed in that full scope.

These questions force attention to the spaces on which operations can be composed. A residue map defined on algebraic rational forms, a homotopy on a separated configuration and an operation on a completed space of fields have different domains. Passing between them requires the specified tensor, support and completion maps. Those maps are the subject of the next chapter.

## Source manuscripts {#ch07-source-manuscripts}

### 1. Ordered collisions and associative chiral bar–cobar duality {#ref-ch07-01}

### 2. Recognition for every pointing on a genuine-unit Chevalley actor {#ref-ch07-02}

### 3. Radical reduction for every pointing {#ref-ch07-03}

### 4. Unitization from an ordinary horizontal representative {#ref-ch07-04}

### 5. Unitization with an arbitrary commutative connection {#ref-ch07-05}

### 6. The one-generator mapping-space theorem in every odd degree {#ref-ch07-06}

### 7. An exact logarithmic quotient of the binary cell tower {#ref-ch07-07}

### 8. Strict positive-degree exactness with three spectators and arbitrary bounds {#ref-ch07-08}

### 9. Strict lower-place vanishing at four spectators and charge five {#ref-ch07-09}

### 10. The first compatibility defect for simple spectator bounds {#ref-ch07-10}

### 11. An explicit class in \(H^4(D(2;4))\) {#ref-ch07-11}

### 12. Vanishing of the actual middle-block residue {#ref-ch07-12}

### 13. Two closed ends of a middle insertion {#ref-ch07-13}
