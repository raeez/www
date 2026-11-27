# Actions and derived centres

An operator can annihilate the vacuum and still act on a boundary field. In a free theory on a half-space one can see this with a single contraction. Place a linear bulk field test above the boundary. Choose it so that its projection onto the boundary is zero. With empty boundary input its action is then zero. With one boundary current as input the two fields can contract, leaving a scalar multiple of the vacuum. For the normalized test below the scalar is \(\hbar\kappa\), where \(\hbar\) counts the contraction and \(\kappa\) is the current level. This operation is defined on the field complexes before taking cohomology.

Multiplication by a central element \(z\) of an ordinary algebra \(A\) sends \(1\) to \(z\). Knowing this value specifies its action on every \(A\)-module. A boundary field algebra has additional structure: operations on separated insertions have to agree with their restrictions as positions collide. The question is which families of operations obeying these compatibilities can be recovered from their values on the boundary vacuum placed at the prescribed insertion positions. The answer depends on the family and on the specified choice of its vacuum operation.

## Central operations on modules {#ch07-central-operations-on-modules}

Let \(A\) be a unital associative algebra over a characteristic-zero field \(k\). Its centre is
\[
Z(A)=\{z\in A:za=az\text{ for every }a\in A\}.
\]
For every left \(A\)-module \(M\), a central element gives an \(A\)-linear operator \(m\mapsto zm\), naturally in \(M\). Conversely, every natural endomorphism of the identity functor on \(A\)-modules arises this way. Indeed, its value on the regular module is determined by \(z=\eta_A(1)\). Naturality with respect to right multiplication by \(a\) gives \(az=za\); naturality with respect to \(A\to M, b\mapsto bm\), then gives \(\eta_M(m)=zm\).

In particular \(Z(A)\cong\operatorname{End}(\mathrm{id}_{A\text{-}\mathrm{Mod}})\), with composition on the right. A proposed central bulk action must likewise give natural operators on boundary representations. In a local field theory their naturality must also commute with restriction of supports and collision of insertions.

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

## A bulk insertion acting on a boundary current {#ch07-supported-bulk-action}

Take the abelian half-space theory with response operator \(\kappa\partial_z\), normal coordinate \(t\geq0\) and boundary coordinate \(z\). Work with regular observables whose smooth test kernels have compact support at each finite field number. Over an open set \(V\) in the boundary, choose a smooth profile of integral one supported in \(0\leq t<\varepsilon\). It gives a cochain inclusion \(i^q\) of the boundary current complex \(\mathcal A_\kappa(V)\) into the collar observables. Integration in the normal direction gives the linear projection \(p\). Its quantum extension also counts pair contractions involving the fields being integrated out,
\[
p^q=\operatorname{Sym}(p)\exp(\hbar\partial_{P_2}).
\]
Here \(P_2\) is the pairing obtained from the normal contracting homotopy. The operator \(\partial_{P_2}\) contracts one unordered pair, so its exponential is a finite sum on every polynomial observable.

Let \(U\subset V\times(a,b)\) with \(\varepsilon<a<b\), and let \(f\) be a bulk observable supported in \(U\). Its operation on a boundary input \(v\) is
\[
\beta_{U;V}(f)(v)=p^q\bigl(\operatorname{ext}_U(f)\, i^q(v)\bigr).
\]
The middle product is the factorization product after extension by zero. Its two factors have disjoint normal supports, which removes cross terms in the Batalin–Vilkovisky differential there. Both outside maps commute with the differentials. Thus \(\beta_{U;V}\) maps the bulk complex into the complex of continuous boundary endomorphisms, with differential \(D\mapsto dD-(-1)^{|D|}Dd\).

Choose a linear bulk test \(u\) in the eliminated polarization, with a unit-integral normal one-form above the boundary profile. Choose its compact tangential function \(\phi\) and the Dolbeault one-form \(\alpha\) of the boundary current \(v\) so that their tangential integral is one. With the current normalization of the action, \(p(u)=0\) and \(P_2(u,i(v))=\kappa\). Only one pair can contract. Consequently
\[
\beta(u)(1)=0,\qquad \beta(u)(v)=\hbar\kappa .
\]
This detects an operation on cochains at nonzero \(\hbar\kappa\). Closedness of \(u\) would be an additional condition for it to define a bulk cohomology class. There is also a composition statement. If a second insertion \(g\) and its normal homotopy stay below \(f\), then inserting \(1-i^qp^q=dH^q+H^qd\) between the two products gives a homotopy from joint insertion to successive action. Moving the supports through one another requires the contact terms described in [Chapter 9](09-mixed-boundaries.md#ch09-ordered-poles-and-their-complete-differential).

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
\begin{aligned}
\Theta(g)&=m(g\otimes^!1_C),\\
\Psi(\alpha)&=\alpha\circ(\mathrm{id}_F\otimes^!u_B):F\simeq F\otimes^!J\longrightarrow C.
\end{aligned}
\]
The first turns a character into an operation by multiplication. The second leaves the input from \(F\) free and inserts the target vacuum \(u_B\) in the other position. The unit identity gives \(\Psi\Theta\simeq1\). **Recognition** asks whether \(\Theta\Psi\simeq1\) as well, on the full action space. This requires a coherent reconstruction of the operation, not only agreement on singleton values.

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

### A genuine pointing without a horizontal vacuum representative {#ch07-horizontal-vacuum-example}

The distinction persists in an algebra with a singular operator product. Put
\[
D=\mathbb C[x,s]\otimes\Lambda(\eta,b),\qquad
|\eta|=|b|=-1,\qquad d\eta=x^2-x,\quad db=s ,
\]
with \(x,s\) closed of degree zero. Define translation by \(Tx=sx,\ T\eta=x(2x-1)b,\ Ts=Tb=0\). Then \(dT\eta=x(2x-1)s=T(d\eta)\), so this is a commutative differential vertex algebra. Evaluating \(x\) at \(i\in\{0,1\}\) and the other generators at zero gives a map \(q_i:D\to\mathbb C\). The equations \(s=0,\ x^2-x=0\) form a regular sequence. Their Koszul complex \(D\) therefore has cohomology \(\mathbb C\times\mathbb C\) in degree zero. On the ideal \(A=\ker q_0\), the other evaluation \(q_1\) is a quasi-isomorphism to \(\mathbb C\).

Now tensor \(A\) with the Heisenberg vertex algebra \(H\), whose current satisfies \(J_{(1)}J=\kappa\mathbf1\) for \(\kappa\ne0\). The nonunital algebra \(W=A\otimes H\) has the double-pole coefficient
\[
(x\otimes J)_{(1)}(x\otimes J)=\kappa x^2\otimes\mathbf1.
\]
The map \(q_1\otimes1:W\to H\) induces an equivalence on Chevalley coalgebras over the affine line. Indeed, at each finite configuration their partition filtrations are finite, and on the associated pieces the map is assembled from external products and direct images of that same quasi-isomorphism. Transport the vacuum pointing of \(C_H\) across this equivalence. Its full character and action spaces are identified by the unital recognition theorem.

What would a strict representative look like? Take its component in the Heisenberg vacuum. It would be a polynomial \(\sum_{n\geq0}p_n(z,s)x^n\) in the ideal \((x,s)\), horizontal for \(\partial_z+T\), and equal to one at \(x=1,s=0\). Horizontality gives \((\partial_z+ns)p_n=0\). For \(n>0\), the highest power of \(z\) forces \(p_n=0\). The remaining \(p_0\) belongs to \(s\mathbb C[s]\), so its value at \(s=0\) is zero. The coherent vacuum thus exists and gives recognition even though this equation for a strict singleton representative has no solution.

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

### A finite number of exterior generators {#ch07-finite-exterior-sources}

With three generators the pair equations have a relation of their own. Write \(z_i=e_i,\ w_i=u_i\), and use \(b_{ij},v_{ij}\) for the entries \(\beta,\zeta\) of the ordered pair \(i<j\). Put \(L_i=(w_i)_{(0)}\) and \(V_{12}=(v_{12})_{(0)}\). The two expressions
\[
A=L_1b_{23}-L_2b_{13}+V_{12}z_3,\qquad
B'=L_1v_{23}-L_2v_{13}-V_{12}w_3
\]
satisfy \(dA=0,\ dB'=TA\). Indeed \([d,V_{12}]=-[L_1,L_2]\) by the zero-mode Jacobi identity and \((Ta)_{(0)}=0\). This cancels the commutator from the first two terms of \(dA\), and the same calculation on \(B'\) leaves \(TA\). The ternary top \(c\) and its translation companion \(s\) obey \(dc=A,\ ds=Tc-B'\). These are genuine new entries. In the pair-only source a closed logarithmic residue functional takes value one on \(A\), so it cannot be a boundary there.

**Theorem (finite exterior sources).** Let \(A_r=\Lambda(\epsilon_1,\ldots,\epsilon_r)\) with \(r\geq1\) finite, all generators of degree one, and differential and translation zero. In the ordinary algebraic localization above, \(\operatorname{Map}_{\mathcal V}(A_r,X)\) is represented by the following tuples in \(X\otimes\Omega_\bullet\), for every ordinary dg vertex target \(X\). Choose the order \(1,\ldots,r\). For each nonempty subset \(I\) take two entries \(a_I,s_I\) of degrees \(2-|I|,1-|I|\), respectively, and put \(L_I=(s_I)_{(0)}\). Sum over decompositions \(I=P\sqcup Q\) into nonempty blocks with \(\max I\in Q\). Let \(\varepsilon(P,Q)\) be the sign of listing \(P\), then \(Q\), in their increasing orders. The equations are
\[
\begin{aligned}
 d a_I&=\sum_{P,Q}\varepsilon(P,Q)L_Pa_Q,\\
 d s_I&=T a_I-\sum_{P,Q}\varepsilon(P,Q)(-1)^{1-|P|}L_Ps_Q .
\end{aligned}
\]
Singletons have empty sums. For \(r=3\) the formula gives exactly the fourteen entries above, including \(c,s\). For \(X=\mathbb C\) only the \(r\) singleton companions and \(\binom r2\) pair tops can be constants of degree zero. The singleton tops give closed one-forms on the simplex. This computes
\[
\operatorname{Map}_{\mathcal V}(A_r,\mathbb C)
\simeq \mathbb C_{\mathrm{disc}}^{\,r+\binom r2}\times K(\mathbb C^r,1).
\]

The general source comparison uses strict transition factorizations through logarithmic quotients as in the binary case. One can see why the quotient has the correct cohomology in every charge. In its tensor-word resolution write each subset letter as the decreasing sequence of its labels and filter by inversion number. For a fixed resulting word the leading differential cuts at one of its strict descents. The possible retained descents form a cube with unit coefficients on its edges and opposite signs around each square. Choosing one descent contracts that entire summand. Only the increasing words remain, one polynomial monomial in each multicharge. The Lie and symmetric-state constructions then give the exterior augmentation on the singleton states. Finiteness of the alphabet also lets one choose a single locality bound for a lifted simplex. A boundary actor with an independent spectator field has additional tensor-source refinement conditions, as the Heisenberg example illustrates.

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

A roof can be evaluated explicitly. Choose a surjective state quasi-isomorphism \(p:P\to B\), a state quasi-isomorphism \(i:H\to W\) with bounded-below direct-sum energy and locally nilpotent current zero mode, and a map \(c:P\to\operatorname{Com}(W)\) into the current commutant. The commutant consists of states killed by the nonnegative modes of the current. The two commuting images give \(a(x\otimes h)=c(x)_{(-1)}i(h)\). Inverting \(i\) and \(p\otimes1\) gives \(q_B=i^{-1}a(p\otimes1)^{-1}\). On \(1\otimes h\) the map \(a\) restricts precisely to \(i\). This supplies the unit path and explains why a change of resolution must respect both legs.

There are two component measurements. Lift \(\epsilon\) to a closed \(e\) on a surjective resolution. Translation vanishes on \(\epsilon\), so one can solve \(du=Te\) there. The degree-zero translation primitive measured in \(H/TH\) has the form \((\mathrm{ch}/\kappa)[J]+\mathrm{ct}[\mathbf1]\). The coefficients \(\mathrm{ch},\mathrm{ct}\) are respectively the charge and the constant part. A third measurement records scalar loops. Together they give an actual map \(\Pi:F\to\mathbb C^2_{\mathrm{disc}}\times K(\mathbb C,1)\) for which \(\Pi q_B\) is a weak equivalence. The quadratic self-linking measurement on a genuine action is already determined by its charge. Indeed the first self-product of the translation primitive has scalar \(\kappa(\mathrm{ch}/\kappa)^2\), equal to twice the self-linking. Convolution and the roof translations further give
\[
F\simeq\mathbb C^2_{\mathrm{disc}}\times F^0,
\]
where \(F^0\) is the whole zero sector of the charge and constant detector. Its connectedness remains open. All genuine components have the same pointed homotopy type. To see this, let \(B=\Lambda(\epsilon)\), \(X=B\otimes H\), \(j(h)=1\otimes h\) and \(\Delta\epsilon=\epsilon\otimes1+1\otimes\epsilon\). A pointed action \(\alpha:X\to H\) has a specified path \(\alpha j\simeq1_H\). Set \(C_\alpha=(1_B\otimes\alpha)(\Delta\otimes1_H):X\to X\). For a roof \(X\xleftarrow{p}S\xrightarrow{f}H\) with \(p\) a surjective quasi-isomorphism, \(C_\alpha\) is represented by the pullback of \(1_B\otimes p\) along \(\Delta\otimes1_H\), followed by \(1_B\otimes f\). Its left leg is a surjective quasi-isomorphism. On state cohomology \(\alpha\) fixes \(1\otimes H\) and kills \(\epsilon\otimes H\), since \(H\) is concentrated in degree zero. The primitive formula for \(\Delta\epsilon\) gives \(H^\bullet(C_\alpha)=1\) on both summands of \(H^\bullet(X)\), so the right leg is a quasi-isomorphism too.

The given path identifies \(C_\alpha j\simeq j\alpha j\) with \(j\). Thus \(C_\alpha\) is an equivalence under \(H\). Precomposition acts by an equivalence on the pointed mapping space \(F\) and sends the trivial action to \(\alpha\) by the counit identity. This is right convolution by \(\alpha\). Every right translation on \(\pi_0F\) is therefore bijective, so \(\pi_0F\) is a group. At the homotopy unit, interchange of loop concatenation and convolution makes \(\pi_1\) abelian, and its action on higher homotopy is trivial. Right translation carries these conclusions to every component. The number of components of \(F^0\), vanishing of the scalar-loop kernel and vanishing of the higher groups remain to be determined.

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
This is an exact reduction of the original problem; neither condition on the right is established. [Genuine fibre reduction](#atlas-c-centre-genuine-heisenberg-fibre-reduction).

The two requirements measure different possible defects. Based loops test extra automorphisms in the component of the trivial action, but they cannot detect another component of the whole zero sector. Nor can endomorphism composition be replaced by loop addition: composition multiplies the detected scalars and has identity scalar \(1\), while loop concatenation adds scalars and has identity \(0\). The proved splitting is a statement about spaces over the scalar set, with no product decomposition for composition. [The remaining equivalence](#atlas-c-centre-genuine-heisenberg-equivalence).

## Residues with spectators {#ch07-residues-with-spectators}

Adding fixed field insertions to the source produces rational forms with **spectators**: labelled positions \(z_1,\ldots,z_r\) that remain as parameters while auxiliary marked positions \(w_1,\ldots,w_m\) are differentiated or absorbed by residues. Three sets of nonnegative integer bounds control the poles: \(N_{ij}\) for spectator pairs, \(b_j\) for a marked point meeting spectator \(j\), and a positive odd integer \(\mu\) for marked pairs.

First keep just one spectator at \(z\). There is one moving point \(w\), with relative coordinate \(y=w-z\). If functions may have a pole of order at most \(b\geq0\), the complex is
\[
 y^{-b}\mathbb C[z,y]\xrightarrow{d_y}
 y^{-b-1}\mathbb C[z,y]\,dy\xrightarrow{\operatorname{Res}_{y=0}}
 \mathbb C[z].
\]
A Laurent monomial \(y^jdy\) has the allowed primitive \(y^{j+1}/(j+1)\) except when \(j=-1\). The missing form \(dy/y\) has residue \(1\). Thus \(dy/y\) is no longer a cycle in the three-term complex. The residue is onto, and the only cohomology that remains consists of the functions of the spectator \(z\) in degree zero. The residue uses up the moving point and records a coefficient at the spectator. This is what a *selected* spectator records in the general complex.

With several moving points, a residue lowers their number and their form degree by one and increases the number of selected spectators by one. Choose a subset \(S\subseteq\{1,\ldots,r\}\) of selected spectators, put \(s=|S|\), and fix the charge \(q=m+s\). A degree-\(i\) form in the marked variables contributes to total degree \(n=2s+i\). With this grading both a residue and an ordinary exterior derivative raise degree by one. Each form is anti-invariant under permutations of the marked variables, acting on both coefficients and differentials. The coefficient of \(dw_I\) has the following pole bounds:
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

At charge one the calculation with \(dy/y\) leaves, for several spectators, the module
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

The column bounds require more than pole counting. They use exact image ideals, their intersections along collision strata, and the differential-module connections. Put \(g_N=\prod_{i<j}(z_i-z_j)^{N_{ij}}\). Multiplication by \(g_N\) shifts the bounds in every selected component and in both terms of (R). It commutes with marked differentiation and left residues, and division by \(g_N\) is its inverse on the prescribed fractional modules.

For a permutation \(\sigma\) preserving \(b,N\), relabel \(z_i,\theta_i\) by \(\sigma(i)\). If \(\operatorname{inv}_S(\sigma)\) counts inversions among indices in \(S\), then \(\sigma(\theta_S)=(-1)^{\operatorname{inv}_S(\sigma)}\theta_{\sigma S}\). This exterior sign and the Koszul sign of the spectator word occur on both sides of multiplication. Reversing the spectator differences gives
\[
 \sigma(g_N\Phi)=\chi_N(\sigma)g_N\,\sigma\Phi,\qquad
 \chi_N(\sigma)=(-1)^{\sum_{i<j,\ \sigma(i)>\sigma(j)}N_{ij}}.
\]
For a word with colour-dependent bounds, group positions by colour. The factors between distinct colours are then separately symmetric, while the factors within each colour are powers of a Vandermonde. Hence on the word stabilizer \(G=\prod_c S_{m_c}\) one has \(\chi_N(\sigma)=\prod_c\operatorname{sgn}(\sigma_c)^{N(c,c)}\). Multiplication identifies \(D_{r,q}(b,N;\mu)^G\) with \((D_{r,q}(b,0;\mu)\otimes\chi_N)^G\), with the original signed action on the complex in each case. Exactness of finite-group invariants over \(\mathbb C\) carries the labelled vanishing above to these repeated-colour sectors.

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
says that compatible pairwise principal parts in the specified image modules arise from a single joint source. Its proof uses the actual coefficient lattice, whose projective dimension is at most two for \(m\ge2\), and induction along collision partitions with the outside polynomial factors retained. [First compatibility defect](#ref-ch07-10).

At \(r=4,\ b_1=\cdots=b_4=\mu=1,\ N=0\), let \(B_S\) be the image of the coefficient ideal \(\mathfrak a\) acting on the module of iterated principal parts along the collision of the labels in \(S\). For each number \(m\) of marks the signed Cousin maps give
\[
\bigoplus_{|S|=2}B_S\xrightarrow{d_1}
\bigoplus_{|S|=3}B_S\xrightarrow{d_2}
B_{\{1,2,3,4\}}\longrightarrow0,\qquad
\ker d_2/\operatorname{im}d_1=0 .
\]
Thus any relation among the four triple images at the full diagonal comes from the six pair images. At two marks the projective dimensions of these coefficient modules rule out a defect supported only at the full collision. With more marks, the only possible associated prime of a defect has a double marked root there. Factoring out the other, coprime roots reduces the calculation at that prime to the two-mark case.

Let \(C_s(m)\) denote the column with \(s\) selected spectators and \(m\) marked points, using its de Rham differential. To pass from exactness of the coefficient images to these columns, assume the logarithmic comparison for the pure column, the quartic finite-normal bound from its Spencer complex, and the degree bounds for the actual pair and triple images. Together these give \(H^i(C_1(m))=0\) for \(i<m-1\). For the total complex retain also the four-label first-residue injection on the lowest possible pure-column class. The finite selected-count filtration then gives strict vanishing \(H^n(D_{4,6})=0\) for \(n<6\), for every \(N_{ij}\ge0\). In charge seven the total vanishes below degree six, and
\[
H^6(D_{4,7})\simeq H^2(C_2(5)).
\]
Indeed, after the first residue kills the possible pure-column class, only the column with two selected spectators and five marks can contribute in degree six. The incoming and outgoing differentials there have zero source or target. Computing this six-component group, as well as extending the vanishing statements to arbitrary positive spectator bounds, requires more information.

The strict inequality cannot be replaced by \(n\le q\) at fixed bounds. With \(r=2\), \(q=4\), \(b=(1,1)\), \(N_{12}=0\) and \(\mu=1\), write \(t=z_2-z_1\). There is a class \([\Phi]\in H^4\) with \(t[\Phi]\ne0\) and \(t^2[\Phi]=0\). After identifying the fractional lattices by their common denominator, raising the spectator-pair bound by one acts by \(t\). This class survives the first increase and dies at the second. [Fixed-bound construction](#ref-ch07-11) · [Exact spectator-bound increase for the charge-four class, Theorem 4.1](#atlas-c-centre-residue-minimal-bound-increase).

## The remaining comparison {#ch07-the-remaining-comparison}

Fix a pointed coassociative coalgebra action \(\alpha:F\otimes^!C_{k^2}\to C_{k^2}\) on the two-colour coalgebra, with \(F\) factorizing and its coefficient complexes possibly unbounded. In the part of the mapping complex where input and output colours disagree, take three nonempty ordered blocks \(A|B|C\), a root \(a\in A\) and marks \(b\in B,\ p\in C\). On \(Y=U_{A,B,C}\) the blocks are mutually disjoint, but positions inside one block may collide. Put \(M=(F_A\boxtimes F_B\boxtimes F_C)|_Y\), and let \(J_Y\) be the diagonal tensor unit on \(Y\). The complex for these fixed data is the homotopy fibre of
\[
\mathbf R\!\operatorname{Hom}_{\mathcal D_Y}(M,J_Y)
\xrightarrow{\,u^*\,}\mathbf R\!\operatorname{Hom}_{\mathcal D_Y}(J_Y,J_Y),
\]
where \(u^*\) restricts along the three components of the pointing. The residue maps at two vacuum insertions and the homotopy between their scalar restrictions give a degree-minus-three primitive of the prescribed three-block discrepancy in this fibre. The construction preserves \(a,b,p\) and both vacuum labels and requires no cocommutativity. [Three-block filling](#ref-ch07-12).

A separate comparison of two prescribed mixed primitives holds on the old separated locus \(z_0\ne z_1\) when the underlying \(F\) has a supplied coherent cocommutative structure. The action and pointing themselves need only be coassociative. It fills the specified closed difference and its corner restriction; it does not extend across the old collision diagonal. These hypotheses must remain distinct from those of the three-block theorem. [Separated-base primitive comparison](#ref-ch07-13).

Recognition for arbitrary pointed factorizing actors still asks for \(\Theta\) to be an equivalence with all changes of roots, collision restrictions and arbitrarily long refined words. The three-block filling and the separated primitive comparison provide particular coherences. For each finite exterior algebra on degree-one generators the ordinary vertex mapping space is known. Comparing it with an action on an independent boundary must additionally preserve the original actor, both roof legs, evaluation and every required incoming refinement. Even a cofinal system of suitable state resolutions of the Heisenberg tensor source would suffice for the roof comparison above. Its existence is open.

The choice of boundary changes the existence question itself. Replace the two-idempotent boundary \(C\) by the Chevalley coalgebra of the Heisenberg state space \(k[x_1,x_2,\ldots]\) at \(\kappa\ne0\). Here \(J_{-n}\) multiplies by \(x_n\) and \(J_n\) acts by \(\kappa n\partial_{x_n}\), for \(n>0\). For the full category of pointed factorizing actions on this coalgebra, there are two parallel maps of actions which remain in distinct components after every map out of their target. They are built from exterior actors on two and one generators and the action associated to \(\partial_{x_1}\). The distinction survives because the vacuum forces every degree-zero one-root operation of a receiving action to be a module map, while the nonzero derivation \(\partial_{x_1}\) cannot be such a map. A representing action would be terminal, so its mapping spaces would supply a path equalizing the two composites. This proves nonrepresentability for this boundary and this action functor.

To draw the corresponding conclusion about a physical boundary, one needs to realize both maps and their actions by supported physical systems. In the other direction, suppose a physical system is universal among a specified class of bulk–boundary systems. A sufficient condition for its algebraic action to be terminal is that the supported realization induce equivalences on the full mapping spaces and that its image generate the algebraic action category by small colimits. Maps from such a colimit into the image of the universal system form a limit of contractible mapping spaces. The support and collision hypotheses belong to the realization functor itself.

### A marked action at finite quantum precision {#ch07-marked-retained-action}

There is another way for evaluation on a vacuum to lose an operation. In the four-current complex for \(\mathfrak{gl}_2\), take the current colours \(H,E,F,I\), where \(I\) is the trace, and work modulo \(\hbar^3\) over \(R_3=\mathbb C[\hbar]/(\hbar^3)\). Besides the current states, the complex has odd ghost states. Multiplying the output of a normalized closed field by a closed trace ghost produces a degree-one class. Its scalar vacuum coefficient vanishes, but the constant term of its full value on the two vacua recovers the trace ghost itself. Acting on that same output and pairing against a dual ghost coefficient are different operations. In the pairing, a trace creator on the field acts by contraction on the dual coefficient.

Keep the ghost output as well as the current state until the last pairing. Let \(u\) denote the separation between an inserted state \(x\) and a fixed, or rooted, current input \(w\). A retained kernel assigns to \(x,w\) a Laurent series in \(u\) valued in current states and in each finite-cutoff quotient of the ghost module. On one right slice a marked coefficient is represented, for the inserted input in question, by
\[
y=\sum_{i=1}^m\left(\sum_{j\geq\nu}u^jF_{ij}\right)\otimes b_i .
\]
The \(b_i\) are a finite list of right current coefficients. Every \(F_{ij}\) uses the same middle ghost cutoff and takes values in left current coefficients. The order matters. First act on \(w\) by \(b_i\), then apply the kernel at \(x\), then contract the middle ghost and act on the output by \(F_{ij}\). With the one lower bound \(\nu\), the one cutoff and the one right support for the whole series on this slice, the coefficient of a fixed output power is a finite sum. Choosing new cutoffs independently at every \(j\) would lose this argument.

At noncritical level \(K\ne-2\), let \(\Phi\) be the coefficient-defined rooted kernel and \(\mathcal Y^\sharp\) the reversed retained field. Write \(i,p,k\) for the state deformation retract, with \(d_Mk+kd_M=1-ip\), and \(h^\Lambda\) for the homotopy from the ordered field \(\mathcal Y_-\) to \(\mathcal Y^\sharp\). In the Hom complex of retained kernels the primitive is
\[
H=(\Phi-\mathcal Y^\sharp)k-h^\Lambda ip,\qquad
\delta H=\Phi-\mathcal Y^\sharp .
\]
It has zero scalar pairing and commutes with the two translations. Contracting each trace-ghost entry extends \(H\) to the trace summand of the marked source. On the positive traceless inserted summand the two evaluations use the same prescribed state operation \(\mathcal J\) and the correction \(\Xi\) obtained by differentiating a source homotopy. With these inputs the comparison holds on the Laurent domain just specified. [Retained kernels](17-holographic-reconstruction.md#ch17-retained-first-root).

An independent physical comparison would have to compute \(\mathcal J+\Xi\) from the two ordered junction products. For example, insert an \(E\)-ghost at one endpoint and an \(F\)-ghost at the other. Both orders must give the prescribed maps, after their separately defined identifications of tensor factors, including the contact where insertions \(1\) and \(3\) meet with \(2\) separated and the unit on each occupied slot. Identifying a physical adjunction further requires its unit, counit and triangle identities in specified module categories. At \(K=-2\) the retained field and its rooted exchange homotopy exist. The critical algebraic state complex admits a separate translation-compatible linear model with additional generators, including the critical quadratic current. Its marked operations still require comparison on these generators. The critical comparison, the independent physical products and the extension beyond \(R_3\) are distinct open questions.

The next chapter encounters the same domain issue in a spectral parameter \(q\). For an infinite-dimensional space \(V\) over a field \(k\), \(V\otimes_k k((q))\) contains only Laurent series whose coefficients span a finite-dimensional subspace of \(V\). Composing an operation with values in \(V((q))\) with one defined on \(V\otimes_k k((q))\) requires a bound on that span.

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

The fixed-bound construction gives the nonzero class \(\Phi=J\omega\), where \(J\) is alternating insertion. In *Exact spectator-bound increase for the charge-four class*, Propositions 1.1 and 2.1 give \(d\psi=t^2\omega\) and \(t[\omega]\ne0\). Insertion gives \(d(J\psi)=t^2\Phi\), and extraction at infinity sends \(\Phi\) back to \(\omega\), so \(t[\Phi]\ne0\). Corollary 3.2 and Theorem 4.1 give the exact annihilator \((t^2)\) and the first zero transition. [The bound transitions](#atlas-c-centre-residue-minimal-bound-increase).

### 12. Vanishing of the actual middle-block residue {#ref-ch07-12}

### 13. Two closed ends of a middle insertion {#ref-ch07-13}
