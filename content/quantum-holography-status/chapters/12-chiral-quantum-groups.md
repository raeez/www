# Quantum groups and nonlinear chiral algebras

Let a two-state probe carry the defining action of \(\mathfrak{sl}_2\) on \(V=\mathbb C^2\). In its chosen basis the matrix unit \(E_{ij}\) sends \(e_j\) to \(e_i\) and kills the other basis vector. Put \(E=E_{12}\) and \(F=E_{21}\). Applying \(F\) and then \(E\) gives the projection \(EF=E_{11}\). Reversing the operations gives \(FE=E_{22}\). Multiplication in the enveloping algebra records what the probe can do in succession. How do these same operations act when two probes couple to the same infinitesimal symmetry?

If a Lie algebra element \(x\) acts on \(M\) and \(N\), its simultaneous action on the pair is
\[
 m\otimes n\longmapsto (xm)\otimes n+m\otimes(xn).
\]
Write \(\mathfrak g\) for the Lie algebra. Since \(x\) acting on the first factor commutes with any \(y\) acting on the second, the sum preserves Lie brackets. Extending the sum multiplicatively gives the coproduct of the enveloping algebra, an algebra homomorphism \(\Delta:U(\mathfrak g)\to U(\mathfrak g)\otimes U(\mathfrak g)\). An element satisfying \(\Delta x=x\otimes1+1\otimes x\) is called primitive. A product need no longer be primitive. On \(V\otimes V\) the action of \(EF\) is
\[
 \begin{aligned}
 \Delta(EF)&=EF\otimes1+1\otimes EF\\
 &\quad+E\otimes F+F\otimes E .
 \end{aligned}
\]
Indeed \(F\) first sends \(e_1\otimes e_2\) to \(e_2\otimes e_2\), and \(E\) then gives \(e_1\otimes e_2+e_2\otimes e_1\). The second term of this output comes from acting on a different probe at each step. With three probes either bracketing places \(x\) once in each of the three slots and sums the terms. This is coassociativity on the generators.

The action on combined probes was an input to this construction. Even a fixed polynomial algebra admits different choices. On \(\mathbb C[x,y,z]\) take \(x,y\) primitive. Both the primitive coproduct of \(z\) and the coproduct with one extra term \(x\otimes y\) extend to Hopf algebra structures. The ordered pair of points \((1,0,0),(0,1,0)\) then gives \(z\)-coordinates \(0\) and \(1\), respectively. The latter law changes when the probes reverse order. [The two group laws and their classification](#ch12-theorem-coproducts-on-a-fixed-weighted-polynomial-algebra)

Now give the probes marks \(a,b\) on a complex line. The rational Yangian deforms the enveloping algebra of polynomial \(\mathfrak{gl}_N\)-valued currents. Its matrix entries \(T_{ij}(s)\) collect the current modes in powers of \(s^{-1}\). In the fundamental evaluation module \(V_a=\mathbb C^N\), \(N\ge2\), the entry with indices \(i,j\) acts by
\[
 T^a_{ij}(s)=\delta_{ij}I+\frac{\lambda E_{ij}}{s-a}.
\]
{#ch12-combined-probe-exchange}
Here \(s\) is an auxiliary variable and \(\lambda\) the deformation parameter. The coproduct on the pair acts by ordered matrix multiplication, \(\sum_k T^a_{ik}(s)\otimes T^b_{kj}(s)\). To see the order, put \(A=E_{ij}\otimes I\), \(B=I\otimes E_{ij}\). Let \(P\) interchange the two basis indices *within the marked order* \(a,b\). Since \(\sum_k E_{ik}\otimes E_{kj}=AP\), the ordered action is
\[
 \begin{aligned}
 D_{a,b}(s)&=\delta_{ij}I+\frac{\lambda A}{s-a}
                +\frac{\lambda B}{s-b}\\
 &\quad+\frac{\lambda^2 AP}{(s-a)(s-b)}.
 \end{aligned}
\]
The coefficient of \(s^{-1}\) at infinity is the primitive action \(\lambda(A+B)\). The opposite coproduct, read on the same two slots, replaces \(AP\) by \(PA\). For \(i=j=1\), \(AP\) kills \(e_1\otimes e_2\) while \(PA\) sends it to \(e_2\otimes e_1\).

What carries the ordered action to the opposite one? Put \(u=a-b\) and try \(R(u)=\alpha I+\beta P\). In \(R D_{a,b}(s)=D^{\mathrm{op}}_{a,b}(s)R\), the relations \(PA=BP\) and \(PB=AP\) reduce the equation to \((\alpha\lambda-\beta u)(AP-PA)=0\) after clearing denominators and a common factor \(\lambda\). Requiring \(R\) to fix the symmetric tensors sets \(\alpha+\beta=1\). Applying the flip after this endomorphism exchanges the marked probes,
\[
 \begin{aligned}
 R(u)&=\frac{u I+\lambda P}{u+\lambda}
       \ \in\operatorname{End}(V_a\otimes V_b),\\
 c_{a,b}&=\tau_{a,b} R(u):V_a\otimes V_b\longrightarrow V_b\otimes V_a ,
 \end{aligned}
\]
where \(\tau_{a,b}\) changes the order of the factors. For example \(c_{a,b}(e_1\otimes e_2)=(u\,e_2\otimes e_1+\lambda e_1\otimes e_2)/(u+\lambda)\) in order \(b,a\). The alternating eigenvalue of \(R(u)\) is \((u-\lambda)/(u+\lambda)\). In the marked bases the checked crossing \(c_{a,b}\) has the opposite sign on that channel. The two eigenvalues of \(R(u)\) give \(R(u)R(-u)=I\) as a rational identity. For numerical \(\lambda\ne0\) and distinct marks the crossing and its inverse are defined together at \(u\ne\pm\lambda\). For formal \(\lambda\) the coefficients expand in \(\lambda/u\) off \(u=0\). [The evaluation on every current mode](#ch12-fundamental-field-modules)

Put a third probe at \(d\) and write \(v=b-d\). The remaining difference is \(a-d=u+v\). With \(R_{ij}\) acting in slots \(i,j\), the two orders of three crossings, written with the common final permutation removed, give the Yang–Baxter equation
\[
 \begin{aligned}
 &R_{12}(u)R_{13}(u+v)R_{23}(v)\\
 &\qquad=R_{23}(v)R_{13}(u+v)R_{12}(u).
 \end{aligned}
\]
To check it, remove the common scalar factors and write each matrix as \(I+\lambda P_{ij}/(a_i-a_j)\), with \((a_1,a_2,a_3)=(a,b,d)\). Terms with zero or one permutation agree. For the two three-cycles, the terms quadratic in \(\lambda\) agree because
\[
 \frac1{uv}=\frac1{u(u+v)}+\frac1{(u+v)v}.
\]
The three transpositions in either cubic term multiply to \(P_{13}\). This proves the identity on the common domain. The constant matrix \(I\) also satisfies Yang–Baxter, yet leaves the unequal \(AP\) and \(PA\) above untouched. Intertwining the coproduct tests how the symmetry acts.

Crossing a *combined* probe gives another equation. With the usual identification of the two bracketings of a vector-space tensor, it reads
\[
 c_{U,V\otimes W}=(1_V\otimes c_{U,W})(c_{U,V}\otimes1_W).
\]
The right side first moves \(U\) past \(V\), then past \(W\). In a general tensor category the associator identifies \((U\otimes V)\otimes W\) with \(U\otimes(V\otimes W)\). Inserting the associators gives the braiding hexagon. Rebracketing four probes without any crossings gives the pentagon for the associator. The [two fusion channels of three Ising spins](#ch12-ising-half-turn) give an example where rebracketing itself mixes basis vectors.

Costello, Witten and Yamazaki realise the rational crossing in perturbative four-dimensional Chern–Simons gauge theory on \(\mathbb R^2\times\mathbb C\), topological in the plane and holomorphic on the line with one-form \(dz\). Expand about the trivial connection, with fields and infinitesimal gauge transformations vanishing at spectral infinity. Take two straight fundamental Wilson lines of \(\mathfrak{gl}_N\) with fixed framing. Their projections cross in the plane while their holomorphic positions differ by \(u\). With the trace pairing, exchange of one gauge boson gives \(\hbar\sum_{ij} E_{ij}\otimes E_{ji}/u=\hbar P/u\). In the matrix relations the full fundamental crossing is proportional to \(I+\hbar P/u\). Fixing its symmetric eigenvalue to one gives \(R(u)\) above at \(\lambda=\hbar\). To act on a pair of parallel lines at the same holomorphic position, cross both with a transverse test line and sum its intermediate colour \(k\). The resulting matrix coproduct is \(\Delta T_{ij}=\sum_k T_{ik}\otimes T_{kj}\). These are operators on quantised lines in the perturbative theory. Extending a crossing to colliding chiral fields also requires their products on the diagonal. [The perturbative crossing and Wilson-line coproduct](#ref-ch12-cq13)

Take two copies of the [marked disk](11-states-and-lines.md#ch11-harmonic-disk-and-collar). Each carries a current whose double-pole coefficient is one. What is that coefficient for the sum of the two currents? Write \(H_\kappa\) for the universal Heisenberg vertex algebra on one current \(h\). Its level \(\kappa\in\mathbb C\) is the scalar multiplying the vacuum in the double pole of \(h(z)h(w)\). Thus the operator product expansions (OPEs) of two independent Heisenberg currents at levels \(\kappa_1,\kappa_2\) have singular parts
\[
h_i(z)h_i(w)\sim\frac{\kappa_i}{(z-w)^2},\qquad i=1,2,
\]
where the scalar in each numerator multiplies the vacuum. In the product of the summed current with itself, the mixed terms \(h_1(z)h_2(w)\) and \(h_2(z)h_1(w)\) are regular because the fields act in different tensor factors. On the marked disks, \(h_1(z)h_1(w)\) and \(h_2(z)h_2(w)\) each contribute one to the double-pole coefficient, giving level two. At general levels these two contributions add to \(\kappa_1+\kappa_2\). The sum therefore satisfies the defining relation of \(H_{\kappa_1+\kappa_2}\) in the tensor product. Sending \(h\) to this sum defines the vertex-algebra homomorphism
\[
H_{\kappa_1+\kappa_2}\longrightarrow
H_{\kappa_1}\otimes H_{\kappa_2},\qquad
h\longmapsto h_1\otimes1+1\otimes h_2.
\]
For the two marked disks this is a map from \(H_2\) to \(H_1\otimes H_1\). Pulling back the action of the target gives the level-two action on the pair of state spaces.

Can the scalar line serve as the tensor unit at a fixed level \(\kappa\)? A counit would be a vertex-algebra homomorphism \(\varepsilon:H_\kappa\to\mathbb C\). Write \(a_{(1)}b\) for the double-pole coefficient. In the source \(h_{(1)}h=\kappa\mathbf1\), so its image is \(\kappa\) because \(\varepsilon\) sends the vacuum to \(1\). In the target the field of the scalar \(\varepsilon(h)\) acts by constant multiplication, so its product with itself has no pole. Preserving the double-pole coefficient would thus give
\[
\kappa=\varepsilon(h_{(1)}h)
=\varepsilon(h)_{(1)}\varepsilon(h)=0.
\]
Before fixing the level, write \(K=h_{(1)}h\) for the central state. It is primitive, so the coproduct sends it to \(K\otimes\mathbf1+\mathbf1\otimes K\). Specializing the first factor to level \(\kappa_1\) and the second to level \(\kappa_2\) gives their sum times the tensor vacuum. The scalar counit sends \(K\) to zero and the vacuum to one. It can therefore descend through the relation \(K=\kappa\mathbf1\) only when \(\kappa=0\). [CQ1](#ref-ch12-cq1)

The two-disk calculation tested the double pole of a single pair of currents. For a chiral coproduct \(D\), the comparison must hold for every pair of source states \(a,b\) and every coefficient of their field product. In terms of the full fields this says
\[
D\bigl(Y(a,z)b\bigr)=Y_{\mathrm{tensor}}(Da,z)\,Db.
\]
Here \(Y(a,z)b\) is the field of \(a\) applied to \(b\) at insertion separation \(z\). On the right, forming the product in the target can require a field of the second system to pass one of the first. A field exchange must then pass a third field across the product \(Y(a,z)b\), including its pole coefficients. This is the field hexagon. The rational matrix above acts on evaluation modules, with parameter \(a-b\). To obtain a field hexagon one must supply fields and exchange on their state spaces, with a common expansion for the two composites. The [construction from a spectral form](#ch12-a-spectral-construction-of-products-and-coproducts) supplies these data. For matrix-valued fields one can then ask whether their individual current modes generate the operations obtained by integrating several fields together.

## Associative products on configurations {#ch12-associative-products-on-configurations}

Integrating the level-one current product against \(dz/(2\pi i)\) about the other insertion gives zero. Inserting the test \(z-w\) in the same contour gives the double-pole coefficient \(\mathbf1\). Thus even a binary collision can require the variation of a test function in the normal direction. A vertex algebra has weakly associative fields \(Y(a,z)\), but the corresponding Beilinson–Drinfeld chiral operation is a Lie operation. For right differential modules on a smooth curve \(X\) over a field of characteristic zero, its binary map has the form
\[
j_*j^*(A\boxtimes A)\longrightarrow\Delta_*A,
\]
where \(j\) is the complement of the diagonal and \(\Delta\) is the diagonal inclusion. Inputs may have poles; outputs retain derivatives normal to the diagonal. Treating this map as a strictly associative multiplication loses part of the collision geometry.

For example, put \(u=z_1-z_3\), \(v=z_2-z_3\), and fix the meromorphic two-form
\[
\alpha=\frac{du\wedge dv}{u(u-v)}.
\]
For an ordered pair of local coordinates \((s,t)\), expand in \(s/t\) and use the convention
\[
\operatorname{Res}_{t=0}\operatorname{Res}_{s=0}
\bigl(f(s,t)\,ds\wedge dt\bigr)
=[s^{-1}t^{-1}]f(s,t).
\]
The inner residue is taken first. Applying this convention to the fixed form \(\alpha\) gives
\[
\begin{array}{c|c|c|r}
\text{first divisor}&\text{second divisor}&(s,t)&\text{iterated residue}\\ \hline
u-v=0&v=0&(u-v,v)&1\\
v=0&u=0&(v,u)&0\\
u=0&v=0&(u,v)&-1
\end{array}
\]
For the first flag, \(\alpha=ds\wedge dt/[s(s+t)]\); for the second, the coordinate change contributes a minus sign and \(\alpha=-ds\wedge dt/[t(t-s)]\), which has no \(s^{-1}\) term. The third expansion begins with \(-s^{-1}t^{-1}ds\wedge dt\). The first two flags join consecutive positions. The third first joins positions 1 and 3 while position 2 remains separate. The sum of all three residues is zero. This is the residue form of Jacobi. A comparison with the full chiral Lie operation must account for the nonconsecutive flag. The ordered word construction below instead composes consecutive cuts; its associativity compares the two ways of cutting a word into consecutive blocks. [CQ1](#ref-ch12-cq1)

The zero in the middle row depends on the form. Keep the same flags and use the form \(du\wedge dv/(uv)\). It is regular at a generic point of \(u=v\), giving zero for the first flag. At \(v=0\) the order of the coordinates is \((v,u)\), so \(du\wedge dv=-dv\wedge du\) gives \(-1\). The last flag uses \((u,v)\) and gives \(1\). Thus the second collision also defines a nonzero operation, and the three signed residues still add to zero.

To specify a cut, start with the word \(123\). Its two binary cuts are \(1|23\) and \(12|3\). Neither produces \(13|2\). For words of length \(n\), the [category \(\mathcal W_X\) of consecutive cuts](05-bar-and-coherence.md#ch05-ordered-cuts-give-a-finite-geometric-bar-construction) has complexes on \(X^n\) with coherent extraordinary-pullback identifications along monotone collisions, together with an isolated empty coefficient. Its convolution \(\star_{\mathrm{cut}}\) sums over consecutive cuts and extends external products from the corresponding separating opens. This convolution is nonsymmetric.

The full ordered collision category uses the schemes \(\mathscr R_I\), obtained by gluing one \(X^I\)-chart for every total order, and collision maps for surjections with ordered fibres. Its convolution \(\star\) sums over all ordered decompositions into subsets and is symmetric monoidal. Restriction to the increasing chart followed by projection to consecutive summands transports a coalgebra to the word category. That projection need not be an equivalence. Both convolutions have a unit \(K\) supported at the empty configuration; a coefficient system is **positive** when its empty coefficient is zero. [CQ1](#ref-ch12-cq1)

**Definition (associative chiral algebra).** For either convolution, an associative chiral algebra is an augmented \(E_1\)-algebra \(A\) with positive augmentation ideal whose bar coalgebra \(BA\) factorizes. If \(I=S\sqcup T\) is an admissible decomposition and \(U_{S,T}\) is the open where its two blocks are disjoint, factorization requires the coproduct component to induce an equivalence
\[
(BA)_I|_{U_{S,T}}\xrightarrow{\sim}
     \bigl((BA)_S\boxtimes(BA)_T\bigr)|_{U_{S,T}} .
\]
For \(\star_{\mathrm{cut}}\) the admissible decompositions are the consecutive cuts. For \(\star\) they are all ordered decompositions into subsets. [CQ1](#ref-ch12-cq1)

In a differential graded presentation, the associative structure can be described by an \(A_\infty\) structure: a differential, multiplication, homotopies relating triple products, and higher homotopies satisfying the Stasheff identities. This is the meaning of \(E_1\) here. With the cohomological convention \(V[1]^n=V^{n+1}\), its suspended operations on \(A[1]\) have degree one. The residue coalgebra \(C(V)\) of appropriate fields gives
\[
A_V=\Omega_{\mathrm{cut}}C(V).
\]
The cobar construction assembles the ordered collision terms and their differential into the associative object. Its algebra unit is supported at the empty configuration. A vacuum marking specifies a left differential module \(G\), a horizontal map \(\mathcal O_X\to G\), and an identification \(A_{\{1\}}\cong\omega_X\otimes_{\mathcal O_X}G\). A vacuum framing also compares the configuration operations with the original simultaneous fields, preserving substitutions, translation and that vacuum.

The cuts separate positions inside one system. To act on two systems, one also needs a way to put their coefficients at the *same* positions.

**Definition (chiral coproduct).** Specify a tensor product \(\diamond\) combining systems at the same positions, together with the geometric interchange that makes \(A\diamond A'\) an algebra for the chosen convolution. An \(E_1\) chiral coproduct is an algebra map
\[
D:A\longrightarrow A\diamond A
\]
with coassociativity and a counit to the \(\diamond\)-unit, or a level-indexed family of such maps. In a derived formulation these include the indicated homotopies and their higher identities. They are not supplied by naming two binary arrows.

The familiar bialgebra identity illustrates the required interchange:
\[
\Delta\mu=(\mu\otimes\mu)
(1\otimes\tau\otimes1)(\Delta\otimes\Delta).
\]
Here \(\tau\) exchanges the middle two factors, and the unit and counit must also be compatible. In chiral geometry the corresponding square uses the actual configuration extensions and same-position tensor. Its arrows must be defined on their pole and support domains. For instance, diagonal tensor of collision coalgebras transports through bar–cobar to
\[
A\diamond A'=\Omega(BA\otimes^!BA').
\]
For this \(\diamond\), the two bar coefficients over one configuration are tensored over that configuration. A field of the second system passing a field of the first can also contribute a scalar depending on their separation. Identifying the geometric tensor with that field operation requires a map respecting both the cross contraction and the collision residues. [CQ1](#ref-ch12-cq1), [CQ2](#ref-ch12-cq2)

The construction from a Beilinson–Drinfeld chiral Lie algebra \(L\) is
\[
L\longmapsto C_{\mathrm{ch}}(L)
\longmapsto\operatorname{res}_{\mathrm{cut}}C_{\mathrm{ch}}(L)
\longmapsto\Omega_{\mathrm{cut}}\operatorname{res}_{\mathrm{cut}}C_{\mathrm{ch}}(L).
\]
Here \(C_{\mathrm{ch}}\) is the Francis–Gaitsgory chiral Chevalley-chain construction. Its coalgebra is cocommutative for the chiral tensor on Ran space and factorizes when the Lie object is supported on the singleton copy of \(X\). The operation \(\operatorname{res}_{\mathrm{cut}}\) retains only monotone collision maps and projects the all-subset coproduct onto consecutive cuts. Coassociativity survives because both iterated projections retain the same consecutive blocks; factorization survives on the cut opens. Taking associative cobar then gives the word object defined above.

This comparison is performed on the coalgebra before taking cobar. It does not identify associative bar–cobar duality with Lie–commutative duality. To recover a chiral Lie algebra in the reverse direction, the entire associative bar must extend along every finite-set surjection with a compatible cocommutative coproduct and factorization. A field comparison and a chiral coproduct require their additional vacuum and tensor data. [CQ1](#ref-ch12-cq1), [CQ3](#ref-ch12-cq3)

Return to the two coproducts on \(k[x,y,z]\), now over any characteristic-zero field. Reversing the sample inputs \((1,0,0),(0,1,0)\) gives \(z=0\) for both laws. The antisymmetric part of the coproduct detects the order dependence. Give \(x,y\) weight one and \(z\) weight two. How many coproducts can the same graded multiplication admit?

**Theorem (coproducts on a fixed weighted polynomial algebra).** Let \(k\) be a field of characteristic zero. Give \(A=k[x_1,\ldots,x_n,z]\) the augmentation at the origin, with \(x_i\) of weight one and \(z\) of weight two. All generators have cohomological degree zero and the differential vanishes. The connected graded Hopf structures on \(A\) have exactly \(\lfloor n/2\rfloor+1\) graded Hopf isomorphism classes. Each \(x_i\) is primitive. Writing \(u_i=x_i\otimes1\) and \(v_i=1\otimes x_i\), the remaining formulas are
\[
\Delta_B z=z\otimes1+1\otimes z+B(u,v),\qquad
S_B x_i=-x_i,\quad S_B z=-z+B(x,x),
\]
where \(B(u,v)=u^{\mathsf t}Bv\) is any bilinear form. The isomorphism class is determined by the rank of \(\omega=B-B^{\mathsf t}\).

*Proof.* The counit fixes the two outer terms of each coproduct. The only possible reduced term on \(z\) has bidegree \((1,1)\). Conversely, this coproduct is pullback along the polynomial law \((u,s)(v,t)=(u+v,s+t+B(u,v))\). Both triple products have cross term \(B(u,v)+B(u,w)+B(v,w)\), and the inverse is \((-u,-s+B(u,u))\). Replacing \(z\) by \(z-\tfrac12 B(x,x)\) leaves \(\tfrac12\omega(u,v)\) as its reduced coproduct. Every graded change of generators has \(x'=Px\), \(z'=cz+q(x)\), with \(P\) invertible, \(c\ne0\) and \(q\) quadratic. The polarization of \(q\) is symmetric, so \(\omega\) changes only by congruence and a nonzero scalar. Splitting off successive pairs with pairing one gives one class for each even rank from zero to \(2\lfloor n/2\rfloor\). ∎

In the two examples the antipodes send \(z\) to \(-z\) and \(-z+xy\), respectively. The defects \((\Delta-\tau\Delta)z\) are \(0\) and \(x\otimes y-y\otimes x\). The augmented multiplication, its associative bar with differential and deconcatenation, and \(\operatorname{Ext}_A^\bullet(k,k)\) coincide. Any reconstruction from these data alone would have to give the same Hopf algebra for the two coproducts distinguished by the pair calculation.

The group commutator of \((u,0)\) and \((v,0)\), taken in that order as \(ghg^{-1}h^{-1}\), is \((0,\omega(u,v))\). In the chosen source and central coordinates its values on basis pairs recover every entry of the alternating tensor. The full ordered product also gives the symmetric part for a specified coordinate \(z\). On the fixed algebra \(\operatorname{Sym}(V^*\oplus W^*)\), with \(V^*\) of weight one and \(W^*\) of weight two, both finite dimensional, the same quadratic change in each coordinate gives a classification by \(\operatorname{GL}(V)\times\operatorname{GL}(W)\)-orbits of \(\omega:\Lambda^2V\to W\). To see why the whole map matters, write \(e^{ij}=e^i\wedge e^j\) for basis covectors on \(k^4\). Both pairs \((e^{12},e^{13})\) and \((e^{12},e^{34})\) have rank-two components. Every form in the first span has a common factor \(e^1\). The second span contains the rank-four form \(e^{12}+e^{34}\).

Over \(R=k[[\hbar]]\) take the same polynomial algebra, flat over \(R\), with \(\hbar\) of weight zero and graded \(R\)-linear isomorphisms. For one weight-two generator the alternating matrix splits into blocks \(\hbar^{a_i}\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\) and a zero block. A nonzero entry of least valuation divides every entry, so the corresponding pair splits off over \(R\). Order the exponents \(0\le a_1\le\cdots\le a_r\). For \(1\le j\le r\) the coefficients of \(\omega^{\wedge j}/j!\), the size-\(2j\) Pfaffians, generate \((\hbar^{a_1+\cdots+a_j})\). These ideals are invariant under a change of basis and determine the exponents. With weight-one coordinates \(x,y\) and reduced term \(\hbar^a x\otimes y\), every \(a\ge1\) gives the additive law after setting \(\hbar=0\). After extending scalars to \(k((\hbar))\), rescaling \(z\) by \(\hbar^{-a}\) gives the Heisenberg law. That rescaling is unavailable over \(k[[\hbar]]\), where the commutator ideal is \((\hbar^a)\). The commutator first survives modulo \(\hbar^{a+1}\). For fixed \(N\ge1\), all \(a\ge N\) give the primitive law modulo \(\hbar^N\). For instance, evaluate on the ordered pair \((1,0,0),(0,1,0)\) from the preceding example, now modulo \(\hbar^2\). The added \(z\)-coordinate is \(\hbar\) for \(a=1\) and zero for \(a=2\). Thus the pair already separates two laws which agree in the special fibre and become isomorphic over the fraction field. To construct fields from such an algebra we shall use its specified coproduct.

## A spectral construction of products and coproducts {#ch12-a-spectral-construction-of-products-and-coproducts}

A Hopf coproduct tells us which components of a state act on two factors. For fields at distinct points we must also specify what happens when one component passes the other. Let \(k\) be a field of characteristic zero and \(R\) a commutative \(k\)-algebra. Take a flat Hopf algebra \(H\) in degree zero over \(R\), with bijective antipode \(\mathsf s\), and a derivation and coderivation \(T\) satisfying \(\varepsilon T=0\). Write
\[
\Delta a=a_1\otimes a_2,\qquad a(z)=e^{zT}a,
\]
with summation understood. Thus \(a(z)=\sum_{j\ge0}z^jT^ja/j!\) is a formal translate. Suppose, for example, that the crossing coefficient for two primitive generators is \(c/z\). Applying \(T\) to the first input differentiates the kernel in \(z\). Applying \(T\) to the second input gives the negative derivative. To cross a product we must also know how to distribute its two factors against the coproduct of the other input. These requirements motivate a bilinear form whose value depends on the separation.

**Definition (unitary spectral coquasitriangular form).** A unitary spectral coquasitriangular form is an \(R\)-bilinear map
\[
\rho_z:H\otimes H\longrightarrow R[z,z^{-1}]
\]
with the following identities:
\[
\begin{aligned}
\rho_z(1,a)&=\varepsilon(a)=\rho_z(a,1),\\
\rho_z(ab,c)&=\rho_z(a,c_1)\rho_z(b,c_2),\\
\rho_z(a,bc)&=\rho_z(a_1,c)\rho_z(a_2,b),\\
\rho_z(a_1,b_1)a_2(z)b_2
&=b_1a_1(z)\rho_z(a_2,b_2),\\
\rho_z(Ta,b)&=\partial_z\rho_z(a,b)=-\rho_z(a,Tb),\\
\rho_z(a_1,b_1)\rho_{-z}(b_2,a_2)
&=\varepsilon(a)\varepsilon(b).
\end{aligned}
\]
The fourth identity specifies exchange, and the last makes exchange reversible. A **level** is a Hopf automorphism \(\eta\) commuting with \(T\) and preserving \(\rho_z\). Choose a group \(\Lambda\) of levels, with multiplication given by composition of automorphisms. These data define the spectral class of chiral quantum groups considered here. [CQ2](#ref-ch12-cq2)

At level \(\eta\), give \(H\) the right coaction
\[
\delta_\eta(b)=b_2\otimes b_3\mathsf s^{-1}(\eta b_1)
=b_{(0)}\otimes b_{(1)}.
\]
Parenthesized subscripts refer to this coaction, rather than the Hopf coproduct. The field is
\[
Y_\eta(a,z)b
=a_1(z)b_{(0)}\rho_{-z}(b_{(1)},a_2).
\]
One coproduct component creates the translated state; the other contracts with the state already present. For fixed inputs each coproduct is a finite sum and each scalar contraction is Laurent polynomial. Multiplication by the formal translate can add arbitrarily high positive powers of \(z\), while the negative powers are bounded. This gives a field in \(H((z))\). Denote the resulting field algebra by \(V_\eta\).

**Example (primitive fields at two levels).** Over \(R=k\), fix \(c\in k\) and take \(H=k[x_0,x_1,\ldots]\) with each \(x_n\) primitive, \(Tx_n=x_{n+1}\), and \(\rho_z(x_m,x_n)=(-1)^n\partial_z^{m+n}(c/z)\). The two product rules extend this kernel to the polynomial algebra. For the identity level the three terms of the iterated coproduct of \(x_0\) give \(\delta_{\mathrm{id}}(x_0)=x_0\otimes1\). For the level \(\eta x_n=-x_n\) they give \(\delta_\eta(x_0)=x_0\otimes1+1\otimes2x_0\). Substitution into the field formula gives
\[
\begin{aligned}
Y_{\mathrm{id}}(x_0,z)x_0&=x_0(z)x_0,\\
Y_\eta(x_0,z)x_0&=x_0(z)x_0-\frac{2c}{z}.
\end{aligned}
\]
The sign comes from evaluating the contraction at \(-z\). On this cocommutative Hopf algebra the identity-level coaction is \(b\mapsto b\otimes1\) for every \(b\). All its identity-level fields are therefore independent of \(c\). On the pair of regular comodules with coaction \(\Delta\), interchanging \(x_0\otimes x_0\) adds \(-c\,1\otimes1/z\) to the flipped tensor. The pair of regular comodules therefore distinguishes two values of \(c\) even when the identity-level field algebras coincide. [CQ2](#ref-ch12-cq2)

**Theorem (spectral field and coproduct construction).** Under the hypotheses above, \(V_\eta\) is a quantum vertex algebra with vacuum \(1\), translation \(T\), and rational exchange
\[
\mathcal S_\eta(z)(a\otimes b)
=a_{(0)}\otimes b_{(0)}\rho_z(a_{(1)},b_{(1)}).
\]
Every finite ordered product on a fixed state has a common finite denominator. For \(V_1=V_{\eta_1}\) and \(V_2=V_{\eta_2}\), their tensor product \(\boxtimes_\rho\) has underlying module \(V_1\otimes_RV_2\) with right coaction
\[
\delta_{12}(c\otimes d)
=c_{(0)}\otimes d_{(0)}\otimes d_{(1)}c_{(1)}.
\]
The second state's \(H\)-component multiplies the first on the left. The usual tensor product of right comodules would give \(c_{(1)}d_{(1)}\) in the last slot. The fields are
\[
Y_{12}(a\otimes b,z)(c\otimes d)
=Y_1(a,z)c_{(0)}\otimes Y_2(b_{(0)},z)d\,
\rho_{-z}(c_{(1)},b_{(1)}).
\]
The maps
\[
D_{\eta_1,\eta_2}=(\eta_2\otimes1)\Delta:
V_{\eta_1\eta_2}\longrightarrow
V_{\eta_1}\boxtimes_\rho V_{\eta_2}
\]
preserve fields, vacuum, translation and coaction. They are coassociative, with counit \(\varepsilon:V_{\mathrm{id}}\to R\) at the identity level. They induce maps of residue coalgebras and their augmented associative chiral cobars. Over a field, the same constructions descend to the ordered collision schemes. [CQ2](#ref-ch12-cq2)

The cross contraction in \(Y_{12}\) is the extra factor required by interchange. Omitting it changes the product against which \(D\) is tested. The compatibility equation is the actual field identity
\[
D\bigl(Y_{\eta_1\eta_2}(a,z)b\bigr)
=Y_{12}(Da,z)Db.
\]
Write \(D=D_{\eta_1,\eta_2}\). In \(\delta_{12}D(b)\) the last tensor factor is \(b_6\mathsf s^{-1}(\eta_2b_4)\,\eta_2b_3\mathsf s^{-1}(\eta_1\eta_2b_1)\). The adjacent pair \(\mathsf s^{-1}(\eta_2b_4)\eta_2b_3\) contracts by \(\mathsf s^{-1}(u_2)u_1=\varepsilon(u)1\), giving
\[
\delta_{12}D(b)
=\eta_2b_2\otimes b_3\otimes b_4\mathsf s^{-1}(\eta_1\eta_2b_1)
=(D\otimes1)\delta_{\eta_1\eta_2}(b).
\]

On a right comodule \(M\), write \(A_z^M(u)m=m_{(0)}\rho_{-z}(m_{(1)},u)\) for contraction with \(u\). Pairing the coaction identity with \(u\) gives
\[
D A_z^{V_{\eta_1\eta_2}}(u)
=\bigl(A_z^{V_1}(u_2)\otimes A_z^{V_2}(u_1)\bigr)D.
\]
In \(Y_{12}(Da,z)\) the two contractions on \(V_1\) compose as \(A(\eta_2a_2)A(a_6\mathsf s^{-1}(\eta_2a_3))\), where \(A=A_z^{V_1}\). Since \(A(u)A(v)=A(vu)\), the pair \(\mathsf s^{-1}(\eta_2a_3)\eta_2a_2\) contracts by the same identity. This leaves the contractions on the two factors in the displayed order. The creation factors agree because \(D\) preserves multiplication and commutes with translation.

Coassociativity can be seen without commuting the levels: both triple maps send \(a\) to
\[
\eta_2\eta_3a_1\otimes\eta_3a_2\otimes a_3.
\]
The two counit identities are
\[
(1\boxtimes_\rho\varepsilon)D_{\eta,\mathrm{id}}=1,
\qquad
(\varepsilon\boxtimes_\rho1)D_{\mathrm{id},\eta}=1.
\]
This counit removes an empty system from a level coproduct. The counit of a module adjunction compares a composite of two functors with an identity functor.

::: figure fig-spectral-coproduct

Exchange has its own compatibility with multiplication. With \(Y(w)(a\otimes b)=Y(a,w)b\), the field hexagon is
\[
\mathcal S(z)(Y(w)\otimes1)
=(Y(w)\otimes1)\mathcal S_{23}(z)\mathcal S_{13}(z+w).
\]
Here \(\mathcal S_{13}(z+w)\) is expanded in nonnegative powers of \(w\); the identity takes values in \((V\otimes V)[z,z^{-1}]((w))\). Exchanging a product with a third field is thus the composite of two specified exchanges. The Yang–Baxter equation controls three exchanges, while the hexagon compares exchange with a product. Neither replaces the other.

For representations, take flat \(R\)-modules \(M\) with a counital right \(H\)-coaction and fields \(Y_M(a,z)m\in M((z))\). Require the vacuum and translation identities, common rational germs for finite ordered products and all consecutive substitutions, and the covariance equation
\[
\delta_M\bigl(Y_M(a,z)m\bigr)
=Y_M(a_{(0)},z)m_{(0)}\otimes m_{(1)}a_{(1)}(z).
\]
These are called **covariant modules of fields**. For modules \(M,N\) at levels \(\eta_1,\eta_2\), the coaction on \(M\otimes_R N\) sends \(m\otimes n\) to \(m_{(0)}\otimes n_{(0)}\otimes n_{(1)}m_{(1)}\). The state \(a\otimes b\) acts by
\[
Y_M(a,z)m_{(0)}\otimes Y_N(b_{(0)},z)n\,
\rho_{-z}(m_{(1)},b_{(1)}).
\]
Pulling it back along \(D_{\eta_1,\eta_2}\) gives a module at level \(\eta_1\eta_2\). The categories together are monoidal, graded by \(\Lambda\), with scalar unit at the identity level. [CQ2](#ref-ch12-cq2)

::: figure fig-programme-context-quantum

A rational exchange may have poles away from \(z=0\). For fundamental comodules take the convention \(R(z)=(zI-hP)/(z-h)\), the same rational matrix expression as the [evaluation-module endomorphism](#ch12-combined-probe-exchange) after setting \(u=z,\ \lambda=-h\). The symmetric eigenvalue is \(1\) and the alternating eigenvalue is \((z+h)/(z-h)\). When \(h\ne0\) the latter has a pole at \(h\) on the punctured spectral line. This calculation tests one fibre and its chosen coordinates. The obstruction to *any* compatible finite Laurent presentation uses the duals as well.

Consider the full category of finite right comodules of the rational RTT Hopf algebra defined by this matrix. Here RTT denotes the matrix relation \(RT_1T_2=T_2T_1R\). Take rank \(N\ge2\) over an extension of the rational function field \(k_0(h)\) for a characteristic-zero field \(k_0\), with the original tensor product and all iterated duals. No exact faithful strong monoidal fibre with a compatible additive formal translation frame makes every exchange and inverse Laurent-polynomial in \(z\). To see the obstruction, let \(d_p(z)\) be the determinant of the exchange between the \(p\)-fold right dual of the fundamental comodule \(V\) and \(V\). Finite Laurent support in both orientations would make each \(d_p\) a Laurent unit. The orders at zero then force \(1/(d_pd_{p+1})\) to be constant for \(p\ge2\), while at \(p=0\) the ratio is \(c z^{n^2-1}\) with \(c\ne0\) and \(n=\dim F(V)>1\) for the proposed fibre \(F\). The same rational map recovers each exchange matrix from its successor. The Zariski closures of the tails of the matrix pairs at \(z=1,2\) stabilize, forcing equality of the ratios at these two values back to the fundamental pair. But \(c\ne 2^{n^2-1}c\). With two independent spectral variables the same argument forces failure at infinitely many positive dual levels. Rational exchanges on this category and the spectral construction under its stated Laurent hypothesis remain available. Here \(h\) is invertible in the coefficient field. The intrinsic Cauchy comparison below fixes generator images in an \(\hbar\)-adic algebra of modes. [Intrinsic RTT modes](#ch12-intrinsic-rtt-modes).

A pair of commuting \(\mathfrak{so}_8\) colours gives a purely quantum test. Their first transverse jets have a quadratic residue on the celestial sphere, whose coefficient can be computed even though their tree bracket vanishes. [The celestial current product](#ch14-celestial-yangian-like)

### What a half-turn measures in the Ising model {#ch12-ising-half-turn}

One can also begin with a category of fields whose fusion and exchange have been specified and reconstruct a quantum group acting on its channel spaces. In the simple Ising Virasoro theory at \(c=1/2\), the three simple fields \(\mathbf1,\psi,\sigma\) have conformal weights \(0,1/2,1/16\). Here \(\mathbf1\) is the vacuum, \(\psi\) is the fermion and \(\sigma\) is the spin field. Fusion obeys

\[
\psi\boxtimes\psi=\mathbf1,\qquad
\psi\boxtimes\sigma=\sigma,\qquad
\sigma\boxtimes\sigma=\mathbf1\oplus\psi .
\]

A faithful additive tensor functor to finite-dimensional complex vector spaces, with the ordinary tensor unit, would give multiplicative dimensions \(d_\psi=1\) and \(d_\sigma^2=2\). The integer dimension of a nonzero finite vector space cannot satisfy the second equation. Keep instead the two labels at the ends of each fusion channel. With \(A=\bigoplus_i\mathbb C e_i\) and \(L_i\) the three simples, set

\[
e_i\,\mathcal F(M)\,e_j=\operatorname{Hom}(L_i,M\boxtimes L_j).
\]

Gluing two channels sums over a **common** intermediate label \(j\). On \(v\otimes w\), the projector is \(\sum_j ve_j\otimes e_j w\). Thus a mismatched pair of channels vanishes, even when both channel vectors are nonzero. Composition of these maps with the fusion associator therefore identifies \(\mathcal F(M)\otimes_A\mathcal F(N)\) with \(\mathcal F(M\boxtimes N)\). Their complex vector-space dimensions on \(\mathbf1,\psi,\sigma\) are \(3,3,4\). The reconstructed algebra is a ribbon weak Hopf algebra \(H\) of dimension \(3^2+3^2+4^2=34\). Its coproduct on the unit, \(\Delta(1)\), projects the ordinary tensor product onto the pairs with matching intermediate labels. This is the space on which exchange acts. [Matching endpoints](02-algebras-and-modules.md#ch02-ising-matching-ends) · [CQ9](#ref-ch12-cq9)

For three input spins with total output \(\sigma\), the first two can fuse through \(\mathbf1\) or through \(\psi\). Either channel can then fuse with the third spin to give \(\sigma\). Keep these two paths as the basis for the exchange. The two basis vectors correspond to \((\sigma\sigma)_{\mathbf1}\sigma\) and \((\sigma\sigma)_\psi\sigma\). A half-turn here means positive analytic continuation of the two insertions through angle \(\pi\) in the marked chiral blocks. In the real trivalent basis, with \(\zeta=e^{\pi i/8}\), the positive half-turn of the first pair and the change of fusion channel have matrices

\[
B_1=\begin{pmatrix}\zeta^{-1}&0\\0&\zeta^3\end{pmatrix},
\qquad
F=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

Removing the scalar \(\zeta^{-2}\) from \(B_1^2\) gives \(Z=\operatorname{diag}(1,-1)\). For the second pair it gives \(FZF=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). The two involutions anticommute and their products span the full two-by-two matrix algebra. More generally the complex algebra generated by adjacent double exchanges on \(\sigma^{\boxtimes n}\) is its entire intertwiner algebra. For instance four spins have two vacuum paths and two fermion paths, giving \(M_2(\mathbb C)\oplus M_2(\mathbb C)\). This assertion takes linear combinations of braids. In each simple output of multiplicity \(d\), individual pure braids have only \(d^2\) projective images.

Reflection inverts both half-turn phases. Their **labelled ratio** in the fermion and vacuum channels changes from \(i\) to \(-i\), while both squared phases acquire the same factor \(i\). Thus projective double exchanges lose the orientation. The twist of a framed spin, \(\zeta\) in the given orientation and \(\zeta^{-1}\) in the mirror, also distinguishes them. For the [Gaussian rays](11-states-and-lines.md#ch11-neutral-ray-pair) the channel is one dimensional. At level \(k\ne0\) the operation on charges \(a,b\) has coefficient \(z^{ab/k}\), continued from the positive real branch. The upper half-turn \(z\mapsto e^{\pi i}z\) multiplies it by \(e^{\pi iab/k}\). Parallel transport on the dual state line has the inverse factor. For \(a=b=1,\ k=2\), the operation acquires \(i\), the dual acquires \(-i\), and their evaluation has factor \(1\). The exponent \(1/2\) requires a branch even though the evaluated scalar is single-valued. [CQ9](#ref-ch12-cq9), [CQ10](#ref-ch12-cq10)

The finite-length Virasoro Ward construction also treats logarithmic modules. It uses the universal vacuum, lower-bounded generalized modules of finite length and finite-dimensional generalized weight spaces, finite support in integral weight cosets, and the \(C_1\)-cofiniteness condition. This last condition means the quotient by the span of \(v_{-1}w\) for positive-weight vertex-algebra states \(v\) is finite dimensional. On this domain the Ward operation represents logarithmic fusion at every charge. At \(c=1,25\) the resulting rigid ribbon categories admit reconstruction by complete quasi-Hopf algebras, including nonsplit objects. On their finite-sum semisimple parts the normalized descriptions have common simple labels \(V_j\) of parity \(j-1\bmod 2\). A half-turn of two odd strands is the flip times \(+i\) at \(c=1\) and times \(-i\) at \(c=25\). Their common associator makes the ratio for a braid the sign of the induced permutation of the odd strands. Every unframed pure braid therefore agrees exactly in these two presentations, while a framed turn of \(V_2\) distinguishes them. Extending that parity formula to nonsplit objects would require their logarithmic transport. [CQ9](#ref-ch12-cq9)

[Chiral Yangians and defect currents (PDF)](chiral-yangians.pdf)

### Ordered cuts of the chiral cotangent Yangian {#ch12-cotangent-yangian-cuts}

Let the first loop be a matrix \(g(u)=I+A/u+O(u^{-2})\), and send in the polynomial current \(Xu\). In the frame of this loop the current is \(g^{-1}(Xu)g=Xu+[X,A]+O(u^{-1})\). Its polynomial part reaches the second loop with the extra constant current \([X,A]\). Its negative part determines the motion of the first loop. For a product of three loops we must make this split twice.

Let \(\mathfrak g\) be a finite-dimensional Lie algebra over a field of characteristic zero. Write
\[
\mathfrak g((u^{-1}))=\mathfrak g[u]\oplus u^{-1}\mathfrak g[[u^{-1}]],
\qquad G_-=\exp\bigl(u^{-1}\mathfrak g[[u^{-1}]]\bigr).
\]
A regular function on \(G_-\) is polynomial in finitely many loop coefficients. Write \(A=\mathcal O(G_-)\) and let the subscripts \(+\) and \(-\) denote the two projections. The same decomposition of \(\operatorname{Ad}_{g^{-1}}\xi\) supplies a new polynomial current and a tangent vector at \(g\),
\[
M_g\xi=(\operatorname{Ad}_{g^{-1}}\xi)_+,\qquad
\rho_\xi(g)=-(L_g)_*(\operatorname{Ad}_{g^{-1}}\xi)_-.
\]
Zeng's level-zero chiral cotangent Yangian \(V\) is the universal vertex envelope of this action Lie algebroid. It is generated by functions \(f\in A\) of vertex weight zero and currents \(J_\xi\), \(\xi\in\mathfrak g[u]\), of vertex weight one. Functions have regular mutual OPEs and their normally ordered product is ordinary multiplication. The singular products are
\[
J_\xi(z)f(w)\sim\frac{\rho_\xi(f)(w)}{z-w},\qquad
J_\xi(z)J_\eta(w)\sim\frac{J_{[\xi,\eta]}(w)}{z-w}.
\]
At invariant level \(\widehat\kappa\) the second OPE acquires the double pole \(\widehat\kappa(\xi,\eta)/(z-w)^2\). At level zero the coproduct is a morphism to the ordinary tensor product of vertex algebras. On a function it pulls back by group multiplication. On a current it is \(J_\xi^{(1)}+J_{M_{g_1}\xi}^{(2)}\). If \(M_{g_1}\xi=\sum a_j(g_1)\eta_j\), the second term means \(\sum a_j\otimes J_{\eta_j}\). The counit evaluates functions at the identity and kills the currents. [Zeng, Definition 4.4](https://arxiv.org/html/2610.10202v2#S4.Thmtheorem4) · [Theorem 5.5 and Corollary 5.6](https://arxiv.org/html/2610.10202v2#S5.Thmtheorem5)

Here \(T^*\mathfrak g=\mathfrak g\ltimes\mathfrak g^*\), with abelian coadjoint ideal \(\mathfrak g^*\). For a homogeneous state \(v\) of vertex weight \(h\), the mode \(v_{(h-1)}\) preserves the lowest grade of a graded module. The standard Zhu algebra encodes the products of these actions. At every invariant level it is \(\operatorname{Zhu}(V_{\widehat\kappa})=A\#_\rho U(\mathfrak g[u])\), with \([\xi,f]=\rho_\xi f\). For a lift of Zeng's extended-algebroid coproduct (33), the current projects to \(\xi^{(1)}+(M_{g_1}\xi)^{(2)}\). The current–current double pole at the identity pair forces \(\widehat\kappa_0=\widehat\kappa_1+\widehat\kappa_2\) for source level \(\widehat\kappa_0\) and output levels \(\widehat\kappa_1,\widehat\kappa_2\). An equal-level lift of this coproduct requires level zero. [Zeng, Eq. (33)](https://arxiv.org/html/2610.10202v2#S5.E33) · [§5.4](https://arxiv.org/html/2610.10202v2#S5.SS4) · [Corollary 5.13](https://arxiv.org/html/2610.10202v2#S5.Thmtheorem13)

Choose an extension \(\widehat\kappa_2^{\mathrm d}\) to the full loop algebra, invariant under that algebra and \(G_-\), vanishing on pairs of negative loops. The current coproduct acquires the first-factor one-form \(h_{\widehat\kappa_2}(\xi)=-\operatorname{pr}_1^*\widehat\kappa_2^{\mathrm d}(M_g\xi,g^{-1}dg)\). Additive choices give coassociativity and exist for all invariant levels of complex reductive \(\mathfrak g\). For arbitrary \(\mathfrak g\), the zero extension in the second factor gives every \(V_{\widehat\kappa}\) a right \(V_0\)-coaction. [Zeng, Theorem 5.9 and Corollary 5.11](https://arxiv.org/html/2610.10202v2#S5.Thmtheorem9)

A one-point vacuum block on the sphere is a linear functional on the vacuum module that annihilates the action of global field modes regular away from the marked point. Which modes extend there depends on how the fields transform between the two charts. At level zero the untwisted standard sphere one-point vacuum blocks for complex reductive \(\mathfrak g\) form the convolution algebra \(\mathcal O(Z_-)^\vee\), where \(Z_-=\exp(u^{-1}\mathfrak z(\mathfrak g)[[u^{-1}]])\). For semisimple \(\mathfrak g\) this is \(\mathbb C\). The mini-twistor structure makes \(u\) a fibre coordinate of \(\mathcal O_{\mathbb P^1}(2)\). Its blocks form a closed algebra of two-chart invariant maps under the Koppinen smash product. Their images lie in the completed enveloping algebra of negative currents at infinity, and their PBW reorderings take values in its counterpart at zero. For a complex simple Lie algebra the standard and mini-twistor sphere products can be distinguished by a commutator in spectral degree \(-4\). A physical identification must match both the coordinate action and fusion. [The two sphere algebras](#ch12-cotangent-sphere-blocks) [Zeng, Corollary 6.7](https://arxiv.org/html/2610.10202v2#S6.Thmtheorem7) · [Theorem 6.11](https://arxiv.org/html/2610.10202v2#S6.Thmtheorem11)

**Proposition (ordered spectral cuts).** Attach a spectral position \(s_i\) to each of \(n\) consecutive outputs. Put \(\sigma_sg(u)=g(u+s)\), \(\tau_s\xi(u)=\xi(u+s)\), \(P_0=e\) and
\[
 P_i=(\sigma_{s_1}g_1)\cdots(\sigma_{s_i}g_i).
\]
There is a polynomial family of vertex-algebra maps \(C_{\mathbf s}:V\to V^{\otimes n}[s_1,\ldots,s_n]\) given by
\[
 C_{\mathbf s}f=f(P_n),\qquad
 C_{\mathbf s}J_\xi=\sum_{i=1}^n
        J^{(i)}_{\tau_{-s_i}M_{P_{i-1}}\xi}.
\]
The coefficients of the \(i\)th current belong to the preceding factors. Cutting the \(i\)th output again at local positions \(t_{ij}\) gives the single ordered cut at positions \(s_i+t_{ij}\). A block with no outputs is evaluated by the counit.

*Proof.* If \(g,h\in G_-\), then \(M_{gh}=M_hM_g\). Indeed, conjugation by \(h^{-1}\) preserves the negative summand, so discarding that summand after the first conjugation does not affect the final positive projection. This proves the unshifted formula at every arity.

Pullback of functions by \(\sigma_s\) defines \(S_sf=f\circ\sigma_s\). Its action on currents is \(S_sJ_\xi=J_{\tau_{-s}\xi}\). To see the sign, push the dressing vector \(\rho_\eta(g)\) forward by \(\sigma_s\). It becomes \(\rho_{\tau_s\eta}(\sigma_sg)\), so \(\rho_{\tau_{-s}\xi}(S_sf)=S_s(\rho_\xi f)\). This preserves the mixed OPE. Polynomial substitution preserves the current bracket, and pullback commutes with the differential on functions. The universal vertex envelope now gives a field automorphism \(S_s\). A second application of the splitting gives
\[
 M_{\sigma_sg}\xi=\tau_s M_g(\tau_{-s}\xi),
 \qquad \Delta S_s=(S_s\otimes S_s)\Delta .
\]
Thus \(C_{\mathbf s}=(S_{s_1}\otimes\cdots\otimes S_{s_n})\Delta^{(n)}\). Coassociativity and \(S_tS_s=S_{s+t}\) give the asserted rule for consecutive blocks. Only finitely many coefficients of \(g\) enter \(M_g\xi\) for a polynomial \(\xi\). Substitution in any fixed negative jet is polynomial in \(s\). Generation by finite vertex products gives polynomial dependence for every state. □

These cuts preserve collisions of the fields themselves. For all states \(a,b\) and every vertex separation \(x\),
\[
 C_{\mathbf s}\bigl(Y(a,x)b\bigr)
 =Y_{V^{\otimes n}}(C_{\mathbf s}a,x)\,C_{\mathbf s}b .
\]
For the mixed simple pole this identity differentiates the ordered product \(P_n\). At output \(i\) the tangent vector on the shifted loop is \(\rho_{M_{P_{i-1}}\xi}(\sigma_{s_i}g_i)\). Summing its contributions to the product gives \(\rho_\xi(P_n)\). There are two independent derivatives in this statement. Vertex translation sends a function \(f\) to the one-form \(df\). Spectral translation has generator \(D_u\) with \(D_uJ_\xi=-J_{\partial_u\xi}\) and \(\partial_{s_i}C_{\mathbf s}=D_u^{(i)}C_{\mathbf s}\). In particular \(\sum_i\partial_{s_i}C_{\mathbf s}=C_{\mathbf s}D_u\).

For a fixed tuple of spectral positions this field identity gives a map on the word configurations of §12.1. Write \(L(W)\) for the Beilinson–Drinfeld chiral Lie algebra of a local vertex algebra on the affine line and put \(F(W)=\Omega_{\mathrm{cut}}\operatorname{res}_{\mathrm{cut}}C_{\mathrm{ch}}(L(W))\). Preservation of the field residues and vertex translation gives \(L(V)\to L(V^{\otimes n})\). Chiral Chevalley chains, restriction to consecutive cuts, and cobar give
\[
 F(C_{\mathbf s}):F(V)\longrightarrow F(V^{\otimes n}).
\]
Applying \(F\) to the substitution identity gives the corresponding identity of word-algebra maps. The target carries the ordinary tensor-product fields. For the level-zero \(GL_N\) cotangent fields, the complex defined by field residues is the Beilinson–Drinfeld chiral Chevalley complex. Its regular sections at collisions identify \(F(V^{\otimes n})\) with \(F(V)^{\diamond n}\), compatibly with cuts and units. Twisting the fields by a root-lattice bicharacter changes the middle exchange in this tensor. [The charge-dependent coproduct](#ch12-coloured-cotangent)

For \(\mathfrak g=\mathfrak{gl}_N\), let \(T(u)\) be the matrix of coordinate functions, so \(T(u)(g)=g(u)\). Write \(g_i(u)=I+A_i u^{-1}+B_i u^{-2}+\cdots\). The coefficients of \(u^{-1}\) and \(u^{-2}\) in \(C_{(p,q)}T(u)\) are
\[
 A_1+A_2,\qquad B_1+B_2-pA_1-qA_2+A_1A_2 .
\]
A constant current is primitive. For a constant matrix \(X\), the next current gives
\[
 C_{(p,q)}J_{Xu}
 =J_{X(u-p)}^{(1)}+J_{X(u-q)}^{(2)}+J_{[X,A_1]}^{(2)} .
\]
Taking \(X=E_{12}\) and \(A_1=E_{21}\) makes the last label \(E_{11}-E_{22}\). The coordinate matrices also detect the order of the cut. Reversing the two factors changes the second coefficient by \([A_1,A_2]\), which is \(E_{11}-E_{22}\) for \(A_1=E_{12}\) and \(A_2=E_{21}\). [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6)

For complex simple \(\mathfrak g\), Zhu reduction gives \(Y^\circ_1(T^*\mathfrak g)\) as a bialgebra, the dense polynomial cotangent Yangian at graded evaluation \(\hbar=1\). The currents and the logarithmic coordinate functions both undergo the current substitution \(u\mapsto u-s_i\) on the \(i\)th factor. For the functions this follows by changing variables in \(\operatorname{Res}_u\langle\alpha(u),\log g(u+s_i)\rangle\,du\). Thus \(C_{(s,0)}\) reduces to the translated ordinary coproduct at the shift \(-s\) in the convention of Abedin and Niu. Their meromorphic coproduct is related to that translated coproduct by a twist. The kernel of the Zhu projection records which field states become equal in the ordinary bialgebra. [The Zhu projection and composite fields](#ch12-cotangent-zhu-kernel) [Zeng, Corollary 5.14](https://arxiv.org/html/2610.10202v2#S5.Thmtheorem14) · [Abedin–Niu, Theorems 4.2–4.3](https://arxiv.org/html/2405.19906v2#S4.ThmDef2)

The spectral cuts extend across \(s_i=s_j\) with zero principal part. A meromorphic exchange on two suitable field modules \(M,N\) would have to intertwine the ordered and opposite field actions. In the convention with the output flip removed, its first equation is
\[
 R_{M,N}(s)\,Y_{M\otimes N}(C_{(s,0)}a,x)
 =
 Y_{M\otimes N}\bigl((S_s\otimes1)\Delta^{\mathrm{op}}a,x\bigr)
 R_{M,N}(s).
\]
The current \(a=J_{Xu}\) tests the mixed term \(J_{[X,A_1]}^{(2)}\). For the two regular vacuum modules \(M=N=V\), the coefficient of \(u^{-2}\) rules out an unflipped intertwiner regular at \(s=0\) with \(R_{V,V}(0)=\mathrm{id}_{V\otimes V}\) on the entire tensor product. Such an operator would equate the two field actions at coincidence. Their vacuum creation coefficients differ by \([A_1,A_2]\). Recovering the Yangian exchange on common Zhu top spaces and satisfying the field hexagons on three modules are further requirements.

There is an exchange on a smaller family at distinct spectral positions. For \(G=SL_2\), a framed Hecke sheet at \(a\) changes the frame by the matrix \(I+X/(u-a)\), with \(X\) nonzero of rank one and \(X^2=0\). Two sheets give an ordered product of these matrices. Reversing them while keeping the product fixed generally changes both residues. Each sheet also has odd fields tangent to its own residue orbit in its local frame. An exchange of fields must carry those tangent directions as well as the product of matrices.

**Theorem (exchange of separated Hecke sheets).** Let \(a\ne b\) be two spectral positions, \(d=a-b\), and let \(G\) be a connected complex simple algebraic group. Choose a highest long-root triple \(E_\theta,H_\theta,F_\theta\) and take \(X,Y\in\operatorname{Lie}(G)\) in the orbit of \(E_\theta\). Write \(P_a(X)=\exp(X/(u-a))\) and normalize the invariant form by \(k_\theta(E_\theta,F_\theta)=1\). The opposite factorization
\[
 P_a(X)P_b(Y)=P_b(Y')P_a(X')
\]
exists if and only if \(d^2\ne k_\theta(X,Y)\), and is then unique. There the two framed, level-zero Hecke field algebras with separate tangent matter are isomorphic over the factor swap. The isomorphism intertwines their incoming currents, coordinate insertions and all their modes. Adjacent swaps satisfy the braid relation on the common domain of the two compositions. The chart map sends \((X,Y)\) in order \(a,b\) to \((Y',X')\) in order \(b,a\). The field isomorphism pulls fields on the \(b,a\) chart back to the \(a,b\) chart. On conformal-weight-zero forms with tensor factors labelled by site, this pullback is the expansion of the Abedin–Niu \(R(d)^{-1}\) at \(d=\infty\), with graded evaluation at \(\hbar=1\). Its inverse takes weight-zero forms from order \(a,b\) to order \(b,a\) by the expansion of \(R(d)\). [Framed Hecke sheets](#ch14-cotangent-faithful-sheets)

::: proof {#ch12-proof-exchange-of-separated-hecke-sheets}

**Rank-two factorization.** Consider first \(G=SL_2\). Here \(X^2=Y^2=0\), \(k_\theta(X,Y)=\operatorname{tr}(XY)\), and \(P_a(X)=I+X/(u-a)\). Clearing the two denominators gives \(X'+Y'=S=X+Y\) and \(CX'=XC\) for \(C=dI+S\). Since \(S^2=\operatorname{tr}(XY)I\), the opposite residues are \(C^{-1}YC,C^{-1}XC\). If \(C\) is singular, its image is the \(+d\) eigenline of \(S\). Both nilpotents would preserve and annihilate this line, contradicting \(d\ne0\).

For general \(G\), write \(v=u-s\). A regular incoming frame \(g=g_0(1+vA+\cdots)\) transforms the local representative \(\exp(Y/v)\), modulo right regular frames, to \(\exp(f_g(Y)/v)\), where
\[
 f_g(Y)=\frac{\operatorname{Ad}_{g_0}Y}{1+k_\theta(A,Y)}.
\]
Indeed the highest-root grading gives \(-[Y,[Y,A]]/2=k_\theta(A,Y)Y\) and \(\operatorname{ad}_Y^3=0\). A frame congruent to \(1\) modulo \(v^2\) stays regular after conjugation by \(\exp(-Y/v)\). For the frame \(\exp(\ell vA)\), cancellation of the polar part requires \(\dot Z=-k_\theta(A,Z)Z\), giving \(Z=Y/(1+\ell k_\theta(A,Y))\). A finite representative at the pole would restart the same flow regularly there. Representatives are unique since the \(v^{-1}\) term of \(\operatorname{Ad}_{\exp(-Z/v)\exp(Y/v)}\) is \(\operatorname{ad}_{Y-Z}\). Apply this formula to \(P_a(X)\) at \(b\) and \(P_b(Y')^{-1}\) at \(a\). The first denominator is \(1-k_\theta(X,Y)/d^2\), the second its reciprocal. The quotient between the two proposed products defines a map from \(\mathbf P^1\) to the affine group \(G\). It is therefore constant, and its value at infinity is \(1\).

In the local frames at \(a,b\) the two coordinates are \(X,Y'=f_{P_a(X)|_b}(Y)\). Each sees the same incoming gauge parameter restricted to its own site. The second odd field transforms by \(\partial_Y Y'\), with \(X\) held fixed. This choice matters already for \(a-b=2\), \(X=E_{12}\), \(Y=E_{21}\). Put \(E=E_{12}\), \(F=E_{21}\), \(H=[E,F]\). For the incoming label \(Eu\) and first tangent \(H\), the ordinary tangent lift includes a term \([F,[E,H]]=2H\) in the second sheet. Its image in the first reversed odd field is \(8(H+E)/3\). The reverse ordering has no cross term in its first odd slot. Consequently this exchange generally fails to commute with the auxiliary de Rham differential, which would force the ordinary tangent map.

To lift the separate change to all fields, let \(J\) be the block-lower-triangular Jacobian from the ordered word to its local site coordinates, and \(B\) its block diagonal. After canonical chiral de Rham pullback apply the exponential of the zero mode of
\[
 \begin{aligned}
 G_N&=\sum_{i,j}:c^jN^i{}_jb_i:,\\
 N&=\log(J^{-1}B).
 \end{aligned}
\]
Here \(c\) is the odd tangent and \(b\) its conjugate. This shear replaces \(Jc\) by \(Bc\) and acts also on the even momenta. For strictly lower \(N,M\), the double contraction \(\operatorname{tr}(N(x(z))M(x(w)))\) vanishes before Taylor expansion. A triangular coordinate change contracts no pair inside \(G_N\), since its \(c\) belongs to an earlier block than its \(b\). Thus these corrected pullbacks compose exactly, including on momenta. For the triangular incoming vector field \(V\), the separate Noether current equals the Cartan current \(\mathcal L_V\) minus \(G_{(dV)_{<}}\), the strictly lower part of its tangent action. Conjugating \(\mathcal L_V\) by the shear changes it only by such a ghost current. Differentiating gauge equivariance in each site's own variable identifies its diagonal odd action, hence fixes the entire correction. The two local-frame maps therefore identify the incoming currents as fields. They preserve the common scattering product and the normal product defining each coordinate insertion. In a longer word the earlier prefix acts separately on each of the two local sites, and every later prefix uses their common product. The common pullback cancels on spectator momenta as well. Both three-swap compositions now pass through the same simultaneous local coordinates on a dense open. The resulting rational identity holds wherever both compositions are regular. [Malikov–Schechtman–Vaintrob, coordinate changes and Theorem 3.7](https://arxiv.org/html/math/9803041v7#id2064)

For the matrix test, let \(L_e\) be the invariant current with polynomial label \(e\) and \(T(u)\) the scattering matrix of the two sheets. Expand \((T\xi)_+=\sum_e a_e e\) in the constant current frame. The coordinate current is \(K_\xi=\sum_e:a_e L_e:\), with the function on the left in the normal product. Write \(D\) for vertex translation along the sheet. These are the currents of the [free-field realization](#ch12-cotangent-yangian-fields).

Take \(a=2,b=0\), \(X=E\), \(Y=\left(\begin{smallmatrix}-z&1\\-z^2&z\end{smallmatrix}\right)\). In both orders \(K_{Eu}(z_1)L_F(z_2)\) has double coefficient \(h=2z\) and simple coefficient \(K_{Hu}+Dh\), with \(Dh=2\). The two nonzero iterated residues with middle insertion \(L_E\) give \(-2z^2\). At \(z=1\) the order-\(u^{-3}\) one-form \(2X DY-\operatorname{tr}((DX)Y)I\) is \(\left(\begin{smallmatrix}-4&2\\0&0\end{smallmatrix}\right)\) in the original order and \(\frac1{25}\left(\begin{smallmatrix}76&2\\32&64\end{smallmatrix}\right)\) after refactorization. The current terms compensate their difference because both orders take the constant Laurent coefficient of the same transported two-point source. [Coordinate-current coproduct](https://arxiv.org/html/2610.10202v2#S5.SS6)

Finally the degree-zero states of a sheet are all its algebraic differential forms. Put the two modules at the origin and place their separation in the spectral shift. In the logarithm of the Abedin–Niu half-matrix \(R_s(d)\), the first dual generator \(I_i^\alpha\) reads the coefficient of \(u^{-i-1}\) in \(\log P_0(X)=X/u\). The second generator acts by the Lie derivative for \(I_\alpha u^j\), which vanishes for \(j\ge2\). The surviving operator is \(d^{-1}\mathcal L_X^{(2)}+d^{-2}\mathcal L_{Xu}^{(2)}\), with \(X\) a first-slot multiplier. This generates precisely the partial tangent action above, since \(X/(u-a)=-X/d-X(u-b)/d^2\) modulo \((u-b)^2\) and the incoming variation acts by the negative gauge parameter. Reversing the two sites gives \(R_s^{21}(-d)\). Thus reverse-to-original pullback is \(R_s(d)[R_s^{21}(-d)]^{-1}=R(d)^{-1}\). Every inverse-separation coefficient is a finite polynomial before evaluation. The construction supplies a field lift on these localized framed modules. A universal chiral exchange on a larger module category remains open. [Abedin–Niu, equations (4.35)–(4.45)](https://arxiv.org/html/2405.19906v2#S4.E35) · [equation (4.88)](https://arxiv.org/html/2405.19906v2#S4.E88)

:::

### A free-field realization of the first cotangent current {#ch12-cotangent-yangian-fields}

Write \(u\) for the Yangian spectral variable and \(D\) for translation in the vertex coordinate \(z\). For a loop \(T(u)=I+X/u\), its single coefficient \(X\) ranges over the \(N\times N\) matrices. At rank two its four entries already suffice to see the first correction to a cotangent current. An infinitesimal change of the loop coordinate is a tangent vector at \(X\). The odd tangent field and its conjugate contract the derivative of a dressing vector field against another such derivative. Contracting both of them against a second current gives a function of \(X\) as the coefficient of a double pole. Translating that function from the first insertion to the second gives a one-form in the simple pole.

**Dressing fields.** Work over \(\mathbb C\) at level zero. For \(G=GL_N\), let \(P_d\) be the affine space of loops \(T=I+\sum_{r=1}^d X_r u^{-r}\), with inverse taken at \(u=\infty\). For \(\xi\in\mathfrak{gl}_N[u]\) set
\[
 M_T(\xi)=(T^{-1}\xi T)_+,\qquad v_\xi(T)=T M_T(\xi)-\xi T .
\]
The subscript retains nonnegative powers of \(u\). The expression for \(v_\xi\) has no powers below \(u^{-d}\), and \(v_\xi=-T(T^{-1}\xi T)_-\) has only negative powers. Thus each dressing field is tangent to \(P_d\). Restricting the dressing Lie action gives \([v_\xi,v_\eta]=v_{[\xi,\eta]}\) on this finite-dimensional space.

Give each matrix coordinate \(\gamma^i\) of \(P_d\) an even conjugate \(\beta_i\) and an odd pair \(\psi^i,b_i\), with singular products \(\beta_i(z)\gamma^j(w)\sim\delta_i^j/(z-w)\) and \(b_i(z)\psi^j(w)\sim\delta_i^j/(z-w)\). All other independent contractions vanish. Use the underlying vertex superalgebra \(\mathcal D_d\) of this affine chiral de Rham system. The odd derivation \(Q=\operatorname{Res}_z\sum_i:\!\beta_i\psi^i\!:\) satisfies \(Q^2=0\). For a polynomial vector field \(v\) define
\[
 \iota_v=\sum_i:v^i b_i:,\qquad \mathcal L_v=Q\iota_v .
\]
A single contraction gives \((\mathcal L_v)_{(0)} f=v(f)\) and \([\mathcal L_v{}_\lambda\iota_w]=\iota_{[v,w]}\). In the latter identity the two terms differentiate the coefficient of \(w\) along \(v\) and that of \(v\) along \(w\) with opposite signs. Applying \(Q\) gives \([\mathcal L_v{}_\lambda\mathcal L_w]=\mathcal L_{[v,w]}\). Here \([a_\lambda b]=\sum_{n\ge0}\lambda^n a_{(n)}b/n!\). The fields live in \(\mathcal D_d\) itself.

Functions of the loop restrict to \(P_d\), and the invariant-frame current \(L_\xi\) acts by \(\mathcal L_{v_\xi}\). These assignments give a representation of Zeng's zero-level universal vertex envelope. Indeed functions multiply regularly, exact one-forms go to \(Df\), and the Cartan identities give the anchor and the zero-level bracket on the constant current frame. The splitting sends \(a\xi\) to \(:a\mathcal L_{v_\xi}:\). The vertex-algebroid extension identities then determine its products on all sections. In particular the coordinate current \(K_\xi\) is \(\sum_e:a_e L_e:\), where \((T\xi)_+=\sum_e a_e e\) in the constant matrix-current basis. [Zeng, §§2.3, 3.4 and 5.6](https://arxiv.org/html/2610.10202v2)

There is also a jointly faithful family on the algebraic state space. Tensor each \(\mathcal D_d\) with the universal level-zero affine vacuum vertex algebra of the Lie algebra \(\mathfrak{gl}_N[u]\). Its currents \(j_\xi\) commute with the first factor, so \(L_\xi\mapsto\mathcal L_{v_\xi}+j_\xi\) has the same defining products. Expand a nonzero state in ordered current creation modes with polynomial coefficients in the translated loop coordinates. This is the vertex-envelope PBW basis for the free coordinate and current frames. At maximal current length, the symbol of its image in the affine-factor PBW filtration is precisely the same polynomial in the independent affine current symbols, with coordinate coefficients restricted to \(P_d\). All those coefficients involve only finitely many spectral indices. Taking \(d\) at least their maximum preserves the nonzero symbol. The augmentation \(j_\xi\mapsto0\) recovers the Cartan-field representation above. For a complex simple Lie algebra, words of smooth highest-root sheets also detect every algebraic state using the sheet momenta alone. [Detection by Hecke sheets](#ch14-cotangent-faithful-sheets) [Zeng, §2.3 and the coordinate-current PBW decomposition in §6.4](https://arxiv.org/html/2610.10202v2)

**The two contractions.** Set \(d=1\). For constant matrices \(S,C\), \(v_C(X)=[X,C]\) and \(v_{Su}(X)=X[S,X]\). If \(e\) runs over the matrix units and \(a_e=(XS)_e\) is the corresponding entry, then \(v_{Su}+\sum_e a_e v_e=0\). Nevertheless the coordinate current survives. Since \(\iota_{av}=:a\iota_v:\), the derivation rule gives
\[
 K_{Su}=-\sum_e:(Qa_e)\iota_{v_e}: .
\]
Each \(a_e\) is linear. In tangent coordinates on \(\operatorname{Mat}_N\) the resulting field is \(G_{U_S}\), where
\[
 G_U=\sum_{p,q}U^q{}_p:\psi^p b_q:,\qquad
 U_S(Z)=-[X,ZS].
\]
The constant current is \(L_C=:\!v_C^i\beta_i\!:+G_{J_C}\), with \(J_C(Z)=[Z,C]\). Two fermion contractions in \(G_{U_S}(z)G_{J_C}(w)\) give the numerator \(\chi_{S,C}(X(z))\), where
\[
 \begin{aligned}
 \chi_{S,C}
 &=\operatorname{Tr}_{\operatorname{Mat}_N}(U_SJ_C)\\
 &=N\operatorname{tr}(SXC)-\operatorname{tr}(SC)\operatorname{tr}X
   +\operatorname{tr}S\,\operatorname{tr}(XC)-\operatorname{tr}C\,\operatorname{tr}(SX).
 \end{aligned}
\]
The first trace is over tangent directions \(Z\) in the \(N^2\)-dimensional matrix space. To compute it, apply \(Z\mapsto AZB\) to \(E_{ij}\). Its \(ij\) entry is \(A_{ii}B_{jj}\), whose sum over \(i,j\) is \(\operatorname{tr}A\,\operatorname{tr}B\). This gives the second line. The single contractions have fermion coefficient \(J_CU_S-U_SJ_C-v_C(U_S)=U_{[S,C]}\). Taylor expansion of the double contraction supplies the rest of the simple pole. Thus on \(P_1\)
\[
 K_{Su}(z)L_C(w)\ \sim\
 \frac{\chi_{S,C}(w)}{(z-w)^2}+
 \frac{K_{[S,C]u}(w)+D\chi_{S,C}(w)}{z-w}.
 \tag{12.1}
\]
With \(L_C\) on the left, the double contraction already has its coefficient at \(w\) and the simple coefficient is \(K_{[C,S]u}\).

The same expression holds in the universal envelope. In the invariant frame the noncommutative Wick formula for \([L_C{}_\lambda:a_e L_e:]\) adds \(-\lambda v_e v_C(a_e)\) to its two single contractions. Summing gives \(-\sum_e v_e v_C(a_e)=\chi_{S,C}\), and the constant term is \(K_{[C,S]u}\) by conjugation covariance. The \(L_{Su}\) summand contributes its ordinary current bracket. Skew symmetry gives (12.1) with the same \(D\chi\). For \(N=2\), \(E=E_{12}, F=E_{21}\) and \(H=[E,F]\), this gives \(\chi=\chi_{E,F}=X_{22}-X_{11}\). In the skew vertex-algebroid convention \(c(K_{Eu},L_F)=-D\chi/2\).

**A contact on the ordered disk.** Put \(s=z_1-z_2\), \(w=z_2\), and use the normal density \(ds\) with \(\operatorname{Res}_s(ds/s)=1\). Write \(q\) for the quotient from Laurent series of finite pole order to principal parts. In the left differential-module trivialization of a vertex algebra \(V\), the binary chiral operation on ordered inputs is
\[
 \Phi(f;a,b)=q\big(f(s,w)Y(a,s)b\big).
 \tag{12.2}
\]
Its source permits poles on \(s=0\), and its target is the direct image of the occupied singleton along that diagonal. Normal differentiation sends \(a\) to \(Da\), since \(Y(Da,s)=\partial_sY(a,s)\). Tangential translation uses \([D,Y(a,s)]=\partial_sY(a,s)\). These identities give differential-module linearity, also after restoring the densities. The two vacuum insertions give \(\Phi(f;1,b)=q(f)b\) and \(\Phi(f;a,1)=q(f e^{sD}a)\). Write \(\delta=q(s^{-1})\), \(\delta_2=q(s^{-2})=-\partial_s\delta\). For a regular \(f\), (12.1) gives
\[
 \Phi(f;K_{Eu},L_F)=
 f(0)\chi\,\delta_2+
 \big(f(0)(K_{Hu}+D\chi)+f'(0)\chi\big)\delta .
 \tag{12.3}
\]
In particular \(f=s\) reads precisely \(\chi\). For the path
\(
 X(z)=\left(\begin{smallmatrix}0&0\\1&3+5z\end{smallmatrix}\right)
\)
the two function readings at \(z=0\) are \(3\) and \(5\), the latter after subtracting \(K_{Hu}\). The path evaluates functions and one-forms. The supported target restricts to zero off the diagonal. Ordinary Zhu reduction kills \(D\chi\) since \(\chi\) has weight zero. The class of \(\chi\) itself is a coordinate function.

**The middle current.** Keep the three labels \(A=K_{Eu}\), \(B=L_E\), \(C=L_F\), with \(x=z_1-z_3\), \(y=z_2-z_3\), both normals positively oriented about zero. In the \(13\mid2\) expansion \(|x|<|y|\), take \(\operatorname{Res}_{x=0} x\,dx\) first and then \(\operatorname{Res}_{y=0}dy\). The spectator acts from the left after the outer collision. Equations (12.1) and (12.2) give
\[
 B_{(0)}(A_{(1)}C)=(v_E\chi)(X)=2X_{21}.
 \tag{12.4}
\]
In the \(23\mid1\) expansion \(|y|<|x|\), the same test gives \(A_{(1)}(B_{(0)}C)=\chi_{E,H}=2X_{21}\). Along \(12\mid3\), the first OPE is regular because \([E,E]=0=\chi_{E,E}\). In the normal \(s=x-y\) the test \(x=s+y\) therefore has zero inner residue. The two iterated readings in (12.4) differ by this last channel. On the displayed path the common value is \(+2\).

One more coefficient measures the derivative in (12.1). Put \(p=X_{21}\) and use variables \(\lambda,\mu\) for the actions of \(A,B\). On the left \([B_\mu C]=L_H\), so \(A=K_{Eu}\) acts on \(L_H\) and the ordered double coefficient is \(\chi_{E,H}=2p\). On the right \(B=L_E\) acts on the \(K_{Hu}\) term of \([A_\lambda C]\), which uses \(\chi_{H,E}=-2p\). Since \([A_\lambda B]=0\), Jacobi compares
\[
 \begin{aligned}
 [A_\lambda[B_\mu C]]&=-2K_{Eu}+2(D+\lambda)p,\\
 [B_\mu[A_\lambda C]]&=-2K_{Eu}-2\mu p+2(D+\mu+\lambda)p .
 \end{aligned}
\]
In the second line the term \(-2\mu p\) from the current bracket is cancelled by \(2\mu p\) from translating the inner coefficient. Thus the spectator sees the same derivative of \(p\) in either order. Deleting \(D\chi\) in the inner \(13\) collision changes the second line minus the first to \(-2(D+\mu)p\). These are iterates of the supported chiral Lie operation with specified labels. Passing to an associative word object uses Chevalley chains and the consecutive-cut cobar construction.

**A derivative in two copies.** Multiply polynomial loops \(T_1T_2\), keeping the order of the factors. The invariant current coproduct sends \(L_e\) to \(L_e^{(1)}+\sum_j (M_{T_1}(e))_j L_j^{(2)}\), and sends functions to their pullbacks under multiplication. Write \(K^{(r)}_{ij}=K_{E_{ji}u^{r-1}}\) and \(K(u)=\sum_{r\ge1}K^{(r)}u^{-r}\). In \(\Delta K=K_1T_2+T_1K_2-\mathcal E\), the first one-form is
\[
 [-\mathcal E]_{u^{-3}}=
 \big(NX-\operatorname{tr}(X)I\big)DY
 +\operatorname{tr}(DX)Y-\operatorname{tr}\big((DX)Y\big)I,
 \qquad X=T_1^{(1)},\quad Y=T_2^{(1)} .
 \tag{12.5}
\]
Here the bracket means the coefficient of \(u^{-3}\). To compute it, place \(a\otimes b\) on the left of a current. Taking the constant term of \(Y(a\otimes b,s)(L_e\otimes1)\) produces \(:aL_e:\otimes b-v_e(a)\otimes Db\). On \(1\otimes L_e\) it produces \(a\otimes:bL_e:-Da\otimes v_e(b)\). A function multiplying the second current in the first tensor factor simply multiplies this latter correction. The first coordinate-current coefficient that contains both a function of \(T_1\) and a function of \(T_2\) is \(XY\) in \(T_1T_2\), paired with a constant current in \(K^{(3)}\). Terms with a function of just one copy give zero correction in these formulas. Contracting the two mixed terms against the matrix units gives
\[
 -\sum_{k,l} E_{lk}
 \left([X,E_{kl}]DY+DX[Y,E_{kl}]\right).
\]
Using \(\sum_{k,l}E_{lk}ZE_{kl}=(\operatorname{tr}Z)I\) proves (12.5). On \(P_1\times P_1\), \(X=\operatorname{diag}(1,0)\), \(Y=zE_{12}\) give \(E_{12}\) at the origin. The choice \(X=zE_{12}\), \(Y=E_{21}\) gives \(-I\). These readings distinguish the two tangential derivatives in the ordered tensor product. [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6)

The two-sheet calculation gives the first spectral coefficient of the ordered one-form. On a framed rank-two Hecke sheet, a coupling to tangent fermions and a point-split current source reproduce the same contacts. Deriving that source and its fusion from the five-dimensional bulk theory remains open. [The one-form at every spectral order](#ch12-cotangent-matrix-fusion) · [Currents on the coupled Hecke sheet](#ch14-cotangent-quantum-currents)

[A meromorphic surface defect on mini-twistor space](#ch14-cotangent-yangian-defect)

### The Zhu projection and the poles of composite fields {#ch12-cotangent-zhu-kernel}

The standard Zhu algebra of the chiral cotangent Yangian at every level is \(H=A\#_\rho U(\mathfrak a)\), where \(A=\mathcal O(G_-)\) and \(\mathfrak a=\mathfrak g[u]\). There is a basis in which one can say exactly which states have the same image. Take polynomial coordinates \(x_\alpha\) on the negative-loop group, an ordered basis \(e_i\) of the polynomial currents, and the standard vertex grading in which the functions have weight zero and \(J_{e_i}\) has weight one. Write \(q\) for the Zhu projection and \(T\) for translation in the vertex coordinate.

**Proposition.** Write a Poincaré–Birkhoff–Witt vector with the commuting coordinate modes on the left and the current labels in descending order,
\[
 W=x_{\alpha_1,(-m_1)}\cdots x_{\alpha_p,(-m_p)}
 (J_{e_{i_1}})_{(-n_1)}\cdots (J_{e_{i_r}})_{(-n_r)}\mathbf1,
 \qquad m_j,n_j\ge1 .
\]
Fix orders within each repeated label. If any \(m_j>1\), then \(q(W)=0\). Otherwise, with \(d=\sum_j(n_j-1)\),
\[
 q(W)=(-1)^d x_{\alpha_1}\cdots x_{\alpha_p}\,e_{i_r}\cdots e_{i_1}.
\]
Consequently the kernel has a basis consisting of all words with a differentiated coordinate and, for each remaining word with \(d>0\), the difference \(W-(-1)^d W^\flat\), where \(W^\flat\) replaces every \(n_j\) by one. At leading conformal weight the kernel is \(C_2(V)=\operatorname{span}\{a_{(-2)}b\}\), and the associated graded Zhu algebra is \(A\otimes\operatorname{Sym}(\mathfrak a)\) with the Poisson bracket induced by the current bracket and dressing action. [Zeng, Theorem 2.6](https://arxiv.org/html/2610.10202v2#S2.Thmtheorem6) · [Corollary 5.13](https://arxiv.org/html/2610.10202v2#S5.Thmtheorem13)

*Proof.* For a homogeneous state \(a\) of weight \(h\), Zhu's residue \(\operatorname{Res}_z(1+z)^h z^{-2-t}Y(a,z)b\) has zero image for \(t\ge0\). The case \(t=0\) is the defining circle product. Formal integration by parts applied to \(Ta\) gives the successive cases. For a function it kills all \(f_{(-m)}b\) with \(m\ge2\), while \(q(f_{(-1)}b)=f q(b)\). For a current it gives \(q(J_{\xi,(-n)}b)=-q(J_{\xi,(1-n)}b)\) for \(n\ge2\). Finally \(J_{\xi,(0)}\) induces \(\operatorname{ad}_\xi\) on \(H\), as the two derivations agree on functions and currents. The weight-one Zhu product gives \(q(J_{\xi,(-1)}b)=q(b)\xi\). Reading the word from the left proves the formula, including the reversal. The all-index-one vectors map bijectively to the ordinary PBW basis of \(H\). In the kernel differences the flat word has strictly smaller weight. Their leading terms, together with the coordinate jets, are exactly the words with a mode of index at most \(-2\). These vanish modulo \(C_2(V)\), and each \(a_{(-2)}b\) is the top-weight term of a circle product. □

Thus \(q(T^jJ_\xi)=(-1)^j j!\xi\), whereas \(q(Tf)=0\). A field whose state vanishes in Zhu can still have a pole with a nonzero coefficient there. In fact \((Tf)_{(1)}J_\xi=\rho_\xi f\). The scalar in the current double pole also retains its value as a scalar state. The associative algebra forgets which pair of fields produced it. There is no inverse even on isomorphism classes of the universal vertex algebras. The zero-level algebra has a character given by its counit. At a nonzero level, two currents have a nonzero scalar double pole, which precludes a character to the scalar vertex algebra.

The vertex presentation computes these missing poles at every arity. Set \([a_\lambda b]=\sum_{j\ge0}\lambda^j a_{(j)}b/j!\). In the constant current frame the three starting brackets are \(0\) on two functions, \([J_\xi{}_\lambda f]=\rho_\xi f\), and \([J_\xi{}_\lambda J_\eta]=J_{[\xi,\eta]}+\lambda\widehat\kappa(\xi,\eta)\). Use translation, skew-symmetry, and the noncommutative Wick formula
\[
 [a_\lambda :bc:]=:[a_\lambda b]c:+:b[a_\lambda c]:
                 +\int_0^\lambda [[a_\lambda b]_\mu c]\,d\mu .
\]
The nonnegative modes are the coefficients multiplied by their factorials. The negative mode \(a_{(-m)}b\) is \(:(T^{m-1}a)b:/(m-1)!\). Every nonzero contraction reduces the number of current letters, and each dressing derivative of a polynomial coordinate function is again a finite polynomial. This makes the recursion finite for fixed algebraic states and mode indices. [De Sole–Kac, §2](https://arxiv.org/abs/math-ph/0312042v3)

For \(GL_N\), let \(G(u)\) be the universal negative-loop matrix and write \((G e_i)_+=\sum_a B_{ia}e_a\). The coordinate currents are \(K_i=\sum_a:B_{ia}J_{e_a}:\), so the same recursion applies after substitution. The inverse matrix \(C=B^{-1}\) is finite at each spectral degree. Multiplying \(CB=1\) would invert a change of basis among ordinary vectors. Here a second normal product must pass a coordinate function through a current and can differentiate it. The inverse change of fields therefore includes a one-form,
\[
 J_{e_b}=\sum_i:C_{bi}K_i:
     -\sum_{i,a}\bigl((\rho_{e_a} B_{ia})\,T C_{bi}
                       +(\rho_{e_a} C_{bi})\,T B_{ia}\bigr).
\]
Indeed \(:f(:gJ_\xi:):=:(fg)J_\xi:+(\rho_\xi g)\,Tf+(\rho_\xi f)\,Tg\). This also explains how a double pole survives in the coordinate frame even when the constant currents have level zero. If \(N\ge2\), the double-pole coefficient of \(K_{E_{12}u}\) with \(K_{E_{11}}\) is \((N-1)x_{21}^{(1)}\), where \(x_{21}^{(1)}\) is the \(u^{-1}\) coefficient of \(G_{21}(u)\). [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6)

There is a finite way to recover a whole rational matrix coefficient at once. For inputs \(a_i,b\) of standard weights \(h_i,h_b\) put
\[
 P(\mathbf z)=\prod_{i<j}(z_i-z_j)^{h_i+h_j}\prod_i z_i^{h_i+h_b}.
\]
Nonnegative weights imply \(a_i{}_{(m)}a_j=0\) for \(m\ge h_i+h_j\). Locality then allows each field in \(P\,Y(a_1,z_1)\cdots Y(a_l,z_l)b\) to commute next to \(b\), where the indicated power of \(z_i\) removes its pole. The resulting series is regular in every variable. Against a functional supported in weight \(h\) its numerator is homogeneous of degree \(h-h_b-\sum_i h_i+\deg P\). If \(P=\sum_\nu p_\nu\mathbf z^\nu\), its coefficient of \(\mathbf z^{\mathbf j}\) is
\[
 \sum_\nu p_\nu\,
 \lambda\!\left(a_1{}_{(\nu_1-j_1-1)}\cdots
                a_l{}_{(\nu_l-j_l-1)}b\right).
\]
Dividing by \(P\) and expanding gives every ordered pole, including those of descendants. The same conclusion holds by summation for functionals supported in finitely many weights. An infinite completed state needs its own convergence or continuity hypothesis.

For instance let \([h_\lambda h]=k\lambda\) and \(W=:(Th)h:\). Then \(q(W)=-h^2\) at every \(k\). The field \(W(x)h(0)\) has singular part \(-2kh(0)x^{-3}-k(Th)(0)x^{-2}\). With an additional current at \(y\), the vacuum coefficient is
\[
 \langle W(x)h(y)h(0)\rangle
 =-2k^2\left(\frac{1}{(x-y)^3x^2}+\frac{1}{(x-y)^2x^3}\right).
\]
The cubic pole and its coefficient distinguish field data with the same Zhu image.

### The one-form in an ordered product of loops {#ch12-cotangent-matrix-fusion}

The one-form in the cotangent-current coproduct can first appear at any prescribed spectral order \(k\ge3\). It detects the order of three loops even when their third coefficients agree. Two derivatives enter the calculation. Write \(D\) for translation in the vertex coordinate \(z\) and a prime for differentiation in \(u\).

Take the level-zero chiral cotangent Yangian for \(GL_N\). For independent loops \(P,Q=I+O(u^{-1})\), the coproduct of the matrix of coordinate currents is
\[
 \Delta K=K_1Q+PK_2-\mathcal E(P,Q).
\]
The first two terms are the two places where a current can meet the product. The correction comes from multiplying the coordinate function on one factor by a current while translating the other factor. In right logarithmic derivatives put
\[
 a=P'P^{-1},\quad b=(DP)P^{-1},\quad
 c=P(Q'Q^{-1})P^{-1},\quad d=P((DQ)Q^{-1})P^{-1}.
\]
Then the whole one-form is
\[
 \mathcal E(P,Q)(PQ)^{-1}
    =(Na-\operatorname{tr}(a)I)d
      +\operatorname{tr}(b)c-\operatorname{tr}(bc)I .
\]
If the first loop varies only in \(u\) and the second also varies along the curve, the product \(ad\) remembers which loop supplied each derivative. Reversing this product changes the matrix coefficient in general. To see how the spectral derivative arises, take a matrix unit \(e\) and write \(P^{-1}eP=\sum_{j\ge0} B_j u^{-j}\). The negative part of \(u^mP^{-1}eP\) contains \(B_j\) precisely for \(0\le m<j\). Consequently \(\sum_{m\ge0}u^{-m-1}\rho_{eu^m}P=eP'-P'P^{-1}eP\). In the second loop the incoming matrix is \(P^{-1}eP\). If its term has order \(p\) and the second conjugation contributes order \(q\), the negative projection counts \(p\le m<p+q\). The spectral derivative therefore acts on \(Q\) in that term. Applying \(\sum_{k,l}E_{lk}AE_{kl}=\operatorname{tr}(A)I\) to the two resulting expressions in Zeng's coproduct gives the formula. Every spectral coefficient is a finite sum. [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6)

For \(T_1,\ldots,T_n\), let \(P_i=T_1\cdots T_i\) and \(P_0=I\). Transport the two derivatives of each loop to the first frame:
\[
 a_i=P_{i-1}(T_i'T_i^{-1})P_{i-1}^{-1},\qquad
 b_i=P_{i-1}((DT_i)T_i^{-1})P_{i-1}^{-1}.
\]
Besides the \(n\) terms obtained by putting \(K_i\) in the \(i\)-th place in \(T_1\cdots T_n\), the current coproduct contains \(-\mathcal E_n\), where
\[
 \mathcal E_n P_n^{-1}=\sum_{i<j}
 \bigl((Na_i-\operatorname{tr}(a_i)I)b_j
       +\operatorname{tr}(b_i)a_j-\operatorname{tr}(b_i a_j)I\bigr).
\]
Indeed both derivatives of a block product add after transport to its first frame. The binary correction is bilinear and commutes with simultaneous conjugation. At the join of two blocks it counts exactly the pairs with a member on each side. Both parenthesizations of the triple coproduct consequently give the same one-form. With constant spectral positions \(s_i\), each factor and its derivatives are evaluated at \(u+s_i\).

Two small loops isolate every order. For \(N\ge2\) and \(r,s\ge1\), take \(P=I+E_{12}u^{-r}\) and \(Q=I+zE_{21}u^{-s}\), so that \(DP=0\) and \(\det P=1\). The full correction in \(\Delta K\) is \(Nr E_{11}u^{-r-s-1}\). In rank two the pair \(r=2,s=1\) gives \(4E_{11}u^{-4}\). Now take the three rank-two loops
\[
 T_1=I+E_{12}/u,\qquad T_2=I+E_{21}/u,\qquad T_3=I+zE_{12}/u .
\]
Only \(T_3\) varies along the curve. The correction is \(-2(T_1T_2)'DT_3=2E_{22}u^{-3}+4E_{12}u^{-4}\). Reversing the first pair keeps \(2E_{22}u^{-3}\) and removes the fourth coefficient. The ordinary Zhu classes of these one-forms vanish because the loop functions have standard vertex weight zero.

There is another one-form when the sheets carry levels \(\kappa_i\) which add to the input level. Choose extensions \(\kappa_i^d\) for \(i>1\), invariant under the full loop Lie algebra and the negative-loop group, vanishing on two negative arguments. Use their sums on right-hand blocks, with algebraic contractions on the polynomial currents. For an invariant current \(L_\xi\) add
\[
 H(\xi)=-\sum_{i=2}^n\kappa_i^d\bigl(\xi,(DP_{i-1})P_{i-1}^{-1}\bigr)
\]
to the dressed currents. For a coordinate current \(K_\xi\) the additional term is \(H((P_n\xi)_+)\). The product rule for \(DP\,P^{-1}\), invariance of the forms and isotropy of the negative loops prove compatibility with refinement. A constant spectral shift sends a level to \(\kappa_s(\xi,\eta)=\kappa(\xi(u+s),\eta(u+s))\); the original level is retained when this equals \(\kappa\). [Zeng, Theorem 5.9](https://arxiv.org/html/2610.10202v2#S5.Thmtheorem9)

Even for \(GL_1\) the choice of extension can be measured on fields. The evaluation form \(f(0)g(0)\) on polynomials has two extensions to Laurent loops, \(f_+(0)g_+(0)\) and the constant coefficient of \(fg\). For their level-additive coproducts with second level one, \(P=1+x/u\) and \(\xi=u\), the one-forms are zero and \(-Dx\), respectively. The two coproducts agree under ordinary Zhu reduction. Recovering the derivative on quantum observables of a five-dimensional defect requires the real-direction fusion of those observables in the chosen frame.

### Two sphere algebras of the chiral cotangent Yangian {#ch12-cotangent-sphere-blocks}

Fix a complex simple Lie algebra \(\mathfrak g\) with nondegenerate invariant form \(K\). The chiral cotangent Yangian has a vertex coordinate \(z\) and a spectral coordinate \(u\). Its functions are polynomial functions on the negative-loop group \(G_-=\exp(u^{-1}\mathfrak g[[u^{-1}]])\). The currents \(J_\xi\), for \(\xi\in\mathfrak g[u]\), act on these functions by dressing. At chiral level zero, one vertex bialgebra admits two coordinate-change actions and gives two different algebras of one-point vacuum blocks on the sphere.

In the standard action every function has weight zero and every current has weight one. In the mini-twistor action the grading operator is \(L_0-E_u\), where \(E_u\) generates \(g(u)\mapsto g(a^{-1}u)\). A function of spectral degree \(d\) has weight \(-d\), and \(J_{xu^m}\) has weight \(1-m\). Both actions have \(L_{-1}=T\), the vertex translation. Spectral translation \(u\mapsto u+s\) gives the cocycle
\[
\lambda_\xi(g)=\operatorname{Res}_u K\bigl(\xi,(\partial_u g)g^{-1}\bigr)\,du.
\]
For either action the twist by \(\theta\) preserves the weights and sends \(L_1J_\xi\) to \(-\theta\lambda_\xi\). The standard Zhu product uses the standard weights and is independent of \(\theta\). The global Ward identities depend on \(\theta\). [Zeng, §§4.2–4.4 and 5.5](https://arxiv.org/html/2610.10202v2#S4.SS2)

The standard sphere block algebra is the graded completion of the center of the universal affine vertex algebra \(V_{-\theta K}(\mathfrak g)\). At \(\theta=0\) it is \(\mathbb C\). When \(\theta K\) is half the Killing form, it is the completed Feigin–Frenkel algebra of functions on Langlands-dual opers on the disc. For complex reductive \(\mathfrak g\) at \(\theta=0\), the answer is the full convolution dual of the coordinate ring of \(\exp(u^{-1}\mathfrak z(\mathfrak g)[[u^{-1}]])\). [Zeng, §6.1–6.2](https://arxiv.org/html/2610.10202v2#S6.SS1)

In the mini-twistor action \(u\) becomes a fibre coordinate of \(M=\operatorname{Tot}_{\mathbb P^1}\mathcal O(2)\). The transition between the charts is \(z=t^{-1}\), \(w=ut^{-2}\). Zeng identifies the sphere algebra with a closed algebra of maps from \(U(\mathfrak g[u,t^{\pm1}])\) to the spectral completion of \(U(u^{-1}\mathfrak g[u^{-1},t^{\pm1}])\), subject to the Ward identities on both charts. Its multiplication is the Koppinen product. Filtering a block by the polynomial degree of the coordinate states it detects gives the completed commutative associated graded
\[
\widehat{\operatorname{gr}}_P\mathscr B^{\rm MT}_\theta
 \cong
\left(\operatorname{Sym} H^1\!\left(M,
(\mathfrak g\otimes\mathcal O_M)\ltimes(\mathfrak g^*\otimes K_M)\right)^\vee\right)^{\mathfrak g}.
\]
Here the full dual carries convolution for the symmetric coalgebra. [Zeng, §§6.3–6.5](https://arxiv.org/html/2610.10202v2#S6.SS3)

The first spectral degree of this cohomology contains one copy of \(\mathfrak g\) and three of \(\mathfrak g^*\). The linear classes in degree two are adjoint copies and have no invariant functionals. Identifying each copy with its dual by \(K\), an invariant quadratic coefficient can pair two of the four copies, with repetition. There are \(4\cdot5/2=10\) such pairings because a simple Lie algebra has a one-dimensional space of invariant bilinear forms. They give all the blocks in spectral degree \(-2\), for every \(\theta\). Two of these detect the order of multiplication. Put \(x[r]=xu^{-1}t^r\) for \(r=0,2\) and let \(\{x_i\}\) be a \(K\)-orthonormal basis. Evaluation of a block map at \(1\) is multiplicative. The two quadratic elements \(\sum_i x_i[r]^2\) lift to sphere blocks by the two-chart normal form. The leading enveloping-algebra symbol of their commutator is
\[
4\sum_{i,j}x_i[0]\,x_j[2]\, [x_i,x_j]u^{-2}t^2 .
\]
The three factors belong to distinct loop modes. Pairing them with \(a,b,c\in\mathfrak g\) gives \(4K(c,[a,b])\), which detects the commutator in spectral degree \(-4\). [Zeng, Proposition 6.17 and Lemma 6.19](https://arxiv.org/html/2610.10202v2#S6.SS5)

At evaluation level \(bK\), the level pairs \(x u^m,y u^n\) only when \(m=n=0\). The mini-twistor one-point block vector spaces are canonically identified with those at level zero in the two charts, since the affine central term vanishes between an outgoing current of nonpositive mode and a vacuum creation current of negative mode. For the coefficient-of-\(u^0\) extension of the level pairing to the double, the coproduct from level \(b_1+b_2\) to levels \(b_1,b_2\) has a one-form term \(h_2(\xi)=-b_2[u^0]K(\xi,dg\,g^{-1})\). The mini-twistor operator \(L_1\) acts on one-forms by \(-2\iota_{E_u}\), so \(L_1h_2=-2b_2\lambda_\xi\). Thus the two input twists \(\theta-2b_2,\theta\) give a convolution product with output twist \(\theta\) at level \(b_1+b_2\). [Zeng, §§4.3–4.4 and 5.4](https://arxiv.org/html/2610.10202v2#S5.SS4)

For complex simple \(\mathfrak g\), the standard Zhu algebra also forgets the isomorphism class of the affine level. Write \(R=\mathbb C[u]\), let \(K_R\) be the \(R\)-valued Killing form on \(\mathfrak g[u]\), and write the scalar level as \(\varphi\circ K_R\) for \(\varphi\in R^\vee\). Two pure affine envelopes are isomorphic as standard-graded vertex algebras precisely when
\[
\varphi(f(u))=\varphi'(f(au+c))\quad(f\in R)
\qquad\text{for some }a\in\mathbb C^\times,\ c\in\mathbb C .
\]
Indeed, the identity is the unique negative loop fixed by all the dressing currents. The vertex pairing on its isotropy Lie algebra \(\mathfrak g[u]\) is the level form. An isomorphism of these fibres acts on the centroid \(R\) by an affine change of \(u\). The \(R\)-valued Killing form transforms by the same change because it is the trace of a product of adjoint actions. Conversely, affine substitution preserves both halves of the rational loop splitting and transports the dressing action and the level form. In particular, distinct evaluation scalars give pairwise nonisomorphic standard-graded envelopes with the same standard Zhu algebra. [Zeng, §§3.2 and 5.4–5.5](https://arxiv.org/html/2610.10202v2#S5.SS4)

**The spectral-cocycle extension for semisimple current algebras**

Let \(\mathfrak g\ne0\) be complex semisimple with nondegenerate invariant form \(K\). Write \(R=\mathbb C[u]\), \(\mathfrak a=\mathfrak g[u]\), and \(G_-=\exp(u^{-1}\mathfrak g[[u^{-1}]])\). The spectral cocycle changes the symmetric pairing of constant currents to \(\chi_\lambda(\xi,\eta)=\lambda_\xi\lambda_\eta\), where \(\lambda_\xi(p)=\operatorname{Res}_u K(\xi,(\partial_u p)p^{-1})\,du\). This vertex algebroid is inequivalent to every affine level and closed-three-form extension, even under arbitrary algebraic changes of the base and current frame. This gives the semisimple case of Zeng's conjecture. For the universal vertex envelopes the conclusion holds for standard-graded isomorphisms, which preserve the first truncation. [Zeng, Theorem 4.8 and the subsequent conjecture](https://arxiv.org/html/2610.10202v2#S4.SS2)

At a negative loop \(p\) let \(r:\mathfrak a\to T_pG_-\) be the dressing anchor, \(\mathfrak h=\ker r\), and \(D=\operatorname{im}r\). Suppose \(D\) is finite-dimensional. The stabilizer \(\mathfrak h\) acts by \(A_\xi=\operatorname{ad}(\xi)\) on \(D=\mathfrak a/\mathfrak h\). Lift \(\xi\in\mathfrak h\) to a section \(\tau\) such that \(d(\rho_\tau)_p|_D=0\). Such lifts exist because \(d(\rho_\xi)_p(r\eta)=-r[\xi,\eta]\) for the constant section and the first derivatives of the coefficients of \(\tau\) on \(D\) can be chosen arbitrarily. In particular \(r\,d\tau_p|_D=A_\xi\). For two such lifts the vertex pairing defines the intrinsic form
\[
 B_p(\xi,\eta)=\chi_0(\xi,\eta)(p)+\operatorname{Tr}_{D}(A_\xi A_\eta),
\]
where \(\chi_0\) denotes the pairing on constant currents. Indeed, for \(\tau=\sum_i f_i e_i\), \(\nu=\sum_j b_j e_j\), write \(\rho_i=\rho_{e_i}\). The correction to \(\chi_0\) in the frame formula is the sum over \(i,j\) of
\[
 -f_i\rho_j\rho_i b_j-b_j\rho_i\rho_j f_i-(\rho_j f_i)(\rho_i b_j).
\]
At \(p\) the first two sums each contribute \(+\sum_{ij}(\rho_j f_i)(\rho_i b_j)\), by differentiating \(\rho_\tau b_j\) and \(\rho_\nu f_i\) along \(D\). The remaining sum is the displayed trace. Hence the form is independent of the lifts. A base isomorphism transports their defining derivative condition, and the one-form correction to the pairing contracts with anchors which vanish at \(p\). It follows that every vertex-algebroid isomorphism preserves \(B_p\). [Zeng, §§2.2–2.4](https://arxiv.org/html/2610.10202v2#S2.SS4)

In the rational splitting, \(\mathfrak h=\{\xi:\operatorname{Ad}_{p^{-1}}\xi\in\mathfrak a\}\) is closed under multiplication by \(u\). At a point of finite anchor rank, its quotient \(\mathfrak a/\mathfrak h\) is finite dimensional over \(\mathbb C\). The characteristic polynomial of multiplication by \(u\) on this quotient annihilates it. Thus \(\mathfrak h\) contains a nonzero polynomial multiple of \(\mathfrak a\) and is a full \(R\)-lattice. The same argument applies at the image of the point under a proposed isomorphism, since the anchor rank is preserved. For simple \(\mathfrak g\), its centroid is exactly \(R\). Indeed, \(\mathfrak h\) spans \(\mathfrak g_{\mathbb C(u)}\) after localization and is centerless. Its centroid is therefore commutative. Each centroid map commutes with \(R\), becomes scalar over \(\mathbb C(u)\), and preserves the full free \(R\)-lattice \(\mathfrak h\), so its scalar belongs to \(R\). For semisimple \(\mathfrak g\) the stabilizer splits along the simple ideals and the centroid is the product of their copies of \(R\). On each ideal the affine pairing is a linear functional of the \(R\)-valued Killing form. The trace term also obeys \(\operatorname{Tr}(A_{f\xi}A_\eta)=\operatorname{Tr}(A_\xi A_{f\eta})\), since \(A_{f\xi}=fA_\xi\) on the \(R\)-module \(D\). Both terms vanish between distinct ideals. Thus every affine level and closed-three-form extension satisfies \(B_p(C\xi,\eta)=B_p(\xi,C\eta)\) for every centroid map \(C\). An isomorphism conjugates the full centroid and preserves this condition.

Choose a coroot \(H\) in one ideal and take \(p=((u-a)/(u-b))^H\) for \(a\ne b\), expanded at infinity. In the adjoint representation this loop has bounded pole order, so a polynomial clears all denominators in \(\operatorname{Ad}_{p^{-1}}\mathfrak a\), giving finite-dimensional \(D\). The whole line \(RH\) stabilizes \(p\), and \(\lambda_{Hf}(p)=K(H,H)(f(a)-f(b))\). Multiplication by \(u\) belongs to the centroid. The two values that it would have to equate differ by
\[
 B_p(uH,uH)-B_p(H,u^2H)
   =\lambda_{uH}(p)^2-\lambda_H(p)\lambda_{u^2H}(p)
   =K(H,H)^2(a-b)^2\ne0 .
\]
An isomorphism would carry this form to one satisfying the centroid identity at a point of the same finite anchor rank. The nonzero difference excludes it.

For reductive \(\mathfrak g\) with nonzero center, Zeng proves that the spectral-cocycle algebroid is inequivalent to every level and closed-three-form extension. [Zeng, Theorem 4.8](https://arxiv.org/html/2610.10202v2#S4.SS2)

## Rational matrix fields and the full curved dual {#ch12-rational-matrix-fields-and-the-full-curved-dual}

For the comodule obstruction the parameter \(h\) belonged to a field where it was invertible. For rational matrix *fields* we work over \(R=\mathbb C[[\hbar]]\) and keep the fibre at \(\hbar=0\). At any precision \(d\) we can expand a shifted pole modulo \(\hbar^d\). For example,
\[
\frac1{u-\hbar}=\sum_{j=0}^{d-1}\frac{\hbar^j}{u^{j+1}}\pmod{\hbar^d}.
\]
Each expression is Laurent in \(u\). Its possible pole order grows with \(d\). The determinant-one normalization of the exchange matrix is
\[
\mathsf R(u)=f(u)\left(I-\frac{\hbar P}{u}\right),\qquad
f(u+N\hbar)=f(u)(1-\hbar^2/u^2),
\]
where \(P\) exchanges the two factors of \(\mathbb C^N\otimes\mathbb C^N\), \(N\ge2\), and \(f(u)=1+O(\hbar/u)\). Its first correction is
\[
\mathsf R(u)=I-\frac{\hbar\Omega}{u}+O(\hbar^2),
\qquad\Omega=P-N^{-1}I.
\]
The exchange separates the symmetric and antisymmetric channels already modulo \(\hbar^2\). On \(v\otimes w+w\otimes v\), \(P\) acts by \(+1\); on \(v\otimes w-w\otimes v\) it acts by \(-1\). The difference, symmetric minus antisymmetric, starts with \(-2\hbar/u\). At rank two the actual normalized eigenvalues modulo \(\hbar^2\) are \(1-\hbar/(2u)\) and \(1+3\hbar/(2u)\). To find the common scalar correction, write \(f(u)=1+c\,\hbar/u+O((\hbar/u)^2)\). The ratio \(f(u+N\hbar)/f(u)\) then starts with \(1-Nc\,\hbar^2/u^2\). The determinant normalization sets this ratio equal to \(1-\hbar^2/u^2\), hence \(c=1/N\). The two matrices
\[
L(v)=I+\hbar\sum_{r\ge1}\ell^{[r-1]}v^{r-1},\qquad
C(p)=I+\hbar\sum_{r\ge1}m^{(r)}p^{-r}
\]
describe the creation and annihilation halves. In each half the RTT relation is
\[
\mathsf R(u-v)X_1(u)X_2(v)=X_2(v)X_1(u)\mathsf R(u-v).
\]
Here \(X=L\) or \(C\). For instance \(L_1\) acts on the first auxiliary copy of \(\mathbb C^N\) and \(L_2\) on the second, with both matrices taking coefficients in the same creation algebra. Thus the two products on opposite sides of the relation can differ. The mixed relation at numerical level \(K\in\mathbb C\) is
\[
\mathsf R(p-v+K\hbar/2)C_1(p)L_2(v)
=L_2(v)C_1(p)\mathsf R(p-v-K\hbar/2).
\]
Expand the mixed denominators at \(p=\infty\) in \(p^{-1},v,\hbar\), and clear the auxiliary denominator in the creation relation before taking its coefficients. The quantum determinant uses descending shifts in column order. At rank two, for either \(X=L,C\), it is
\[
 q_X(u)=X_{11}(u)X_{22}(u-\hbar)-X_{21}(u)X_{12}(u-\hbar).
\]
For general \(N\) the \(j\)th column is evaluated at \(u-(j-1)\hbar\), with the alternating sum over row permutations. Define the double \(D_K\) by setting to zero the coefficients of the three RTT differences divided by \(\hbar^2\) and of \((q_X-1)/\hbar\) for both halves. These are divisions in the defining expressions before imposing relations or reducing precision. For \(X=I+\hbar A\), the constant coefficient in \(\hbar\) of \((q_X-1)/\hbar\) is \(\operatorname{tr}A\). The undivided determinant would specialize to \(1=1\) and lose tracelessness. [CQ4](#ref-ch12-cq4)

**Theorem (rational affine field comparison).** For every \(N\ge2\) and every \(K\in\mathbb C\), the divided determinant-one double is topologically free over \(\mathbb C[[\hbar]]\). Multiplication identifies it, as a module, with the \(\hbar\)-adically completed tensor product of its creation and annihilation halves. The integral divided-state fields agree with the Etingof–Kazhdan quantum affine fields on every state and on their exchange. The classical fibre of the vertex algebra of divided states is the universal affine vacuum vertex algebra \(V_K(\mathfrak{sl}_N)\), with the trace form fixing the level. [CQ4](#ref-ch12-cq4)

The associative algebra that acts on the vacuum has a different classical fibre. Let \(\mathfrak d_{\rm pol}=\mathfrak{sl}_N[t,t^{-1}]\oplus\mathbb C\mathbf c\), with central term \(m\delta_{m+n,0}\operatorname{tr}(ab)\mathbf c\) in \([at^m,bt^n]\). Then \(D_K/\hbar D_K=U(\mathfrak d_{\rm pol})/(\mathbf c-K)\). For example \(at^0\) for \(a\ne0\) survives in this algebra and annihilates the vacuum vector. The proof first establishes the Poincaré–Birkhoff–Witt basis and the creation–annihilation factorization. It then identifies the annihilation matrix with the inverse of the operator matrix obtained from the coordinate coaction. To see why only one input of the scalar pairing is divided, write \(F\) for the determinant-one coordinate Hopf algebra, \(U\) for the completed creation algebra generated by the coefficients of \(\ell(v)=(L(v)-I)/\hbar\), and \(g\in F\). The pairing on \(F\widehat\otimes U\) has generator value
\[
 \beta_z(g,\ell_{ij}(v))=
 \frac{\rho_z(g,L_{ij}(v))-\delta_{ij}\varepsilon(g)}{\hbar}.
\]
The numerator is divisible by \(\hbar\). Dividing both inputs would require an additional power. For instance the coefficient of \(\Omega\) in \(\mathsf R(z)-I\) is already of order one in \(\hbar\). [CQ4](#ref-ch12-cq4)

The field target is
\[
M((z))^\wedge=\varprojlim_d(M/\hbar^dM)((z)).
\]
At each precision and on fixed inputs the pole order is finite. A bound uniform in the precision would be stronger. The comparison above identifies the fields on states. To recover the algebra of modes one must also account for all functions against which several fields can be integrated.

### A vacuum field of the double Yangian {#ch12-double-yangian-vacuum}

There are two different ways for a Yangian to occur in a field algebra. The matrix-extended \(W_\infty\) has ordinary local fields whose degree-zero Zhu algebra is the Yangian. The rational double supplies a quantum vertex algebra in which exchange acts on the fields themselves. In the latter construction the insertion \(z\) translates every current parameter \(u_i\) to \(u_i+z\). In Zeng’s cotangent construction the vertex coordinate is independent of the loop parameter, and vertex translation is distinct from spectral translation. [Gaiotto–Rapčák–Zhou, Theorems 6–7](https://arxiv.org/abs/2309.16929) · [Etingof–Kazhdan, Theorem 2.3](https://arxiv.org/abs/math/9808121) · [Zeng, §1](https://arxiv.org/abs/2610.10202v2)

For the general-linear double, write \(T=C=I+\hbar A\) and \(T^+=L=I-\hbar B\) in the notation above. Fix the central element at \(K\) and divide the resulting algebra by the left ideal generated by all coefficients of \(A\). Its \(\hbar\)-adic completion is the vacuum module \(V_K\), with vacuum \(\mathbf1\). The Poincaré–Birkhoff–Witt theorem identifies its underlying module with the completed creation half. Write \(T_n^+(u|z)=T^+_1(z+u_1)\cdots T^+_n(z+u_n)\) and use the same order for \(T_n\). The field of a word is

\[
Y\bigl(T_n^+(u|0)\mathbf1,z\bigr)
=T_n^+(u|z)\,T_n(u|z+K\hbar/2)^{-1}.
\]

On the vacuum the second factor acts as the identity. On an occupied state it contributes the poles. Together with the state exchange of the double, this formula gives a quantum vertex algebra for every numerical \(K\), with a single formal deformation parameter \(\hbar\). Its classical central form on \(\mathfrak{gl}_N\) is \(K(\operatorname{tr}(XY)-\operatorname{tr}X\,\operatorname{tr}Y/N)\). The scalar current has zero pairing, and imposing the divided determinant-one relations gives the \(\mathfrak{sl}_N\) family with trace form. [Jing–Kožić–Molev–Yang, Theorems 2.2 and 4.1, equations (2.24) and (4.16)–(4.19)](https://arxiv.org/abs/1603.00237v2) · [Etingof–Kazhdan, Proposition 2.4](https://arxiv.org/abs/math/9808121)

For \(N\ge2\), one off-diagonal matrix entry measures both the current bracket and its central term. Put \(x=p-v\), expand at \(p=\infty\), and specialize to the critical level \(K=-N\). The mixed action on one created state is exactly

\[
A_{12}(p)B_{21}(v)\mathbf1
=\frac{B_{11}(v)\mathbf1}{x-N\hbar/2}
 -\frac{B_{22}(v)\mathbf1}{x+N\hbar/2}
 -\frac{N\mathbf1}{x^2-N^2\hbar^2/4}.
\]

Indeed put \(x_\pm=x\pm K\hbar/2\). The mixed relation moves \(T_1(p)\) past \(T^+_2(v)\) by sending an auxiliary matrix \(M\) to \(\mathsf R(x_+)^{-1}M\mathsf R(x_-)\). At the critical level \(x_-=x_++N\hbar\). The determinant-one recurrence gives \(f(x_-)/f(x_+)=1-\hbar^2/x_+^2\), which cancels the scalar denominator from inverting \(I-\hbar P/x_+\). The expression becomes \((I+\hbar P/x_+)M(I-\hbar P/x_-)\). For \(M=B_2(v)\), the \(E_{12}\otimes E_{21}\) entries of \(PB_2\) and \(B_2P\) are \(B_{11}\) and \(B_{22}\). The same entry from the identity term gives \(-N/(x_+x_-)\) after division. In rank two the vacuum component is \(-2/(x^2-\hbar^2)\). At \(\hbar=0\) the simple pole carries \(E_{11}-E_{22}\), the bracket of the two root currents. The exact identity on this module and the critical-level failure of the original lifts into the algebra of several-point modes measure different operations. [Intrinsic RTT modes](#ch12-intrinsic-rtt-modes)

The level controls whether the scalar part of this matrix entry is rational at all orders. Project to the creation vacuum by sending each coefficient of \(B\) to zero. At any \(K\ne0\) the result is
\[
\frac{K}{x_+x_-}\,
\frac{f(x_-)}{f(x_+)(1-\hbar^2/x_+^2)}.
\]
At every fixed \(\hbar\)-precision this is a Laurent polynomial in \(x^{-1}\). After scaling \(y=x/\hbar\) and multiplying by \(\hbar^2\), the full series is the expansion of a rational function of \(y\) **exactly when \(K\in N\mathbb Z\)**. Indeed, write \(g(y)=f(\hbar y)\) and \(m(y)=1-y^{-2}\). The remaining ratio \(F(y)=g(y-K/2)/g(y+K/2)\) satisfies \(F(y+N)/F(y)=m(y-K/2)/m(y+K/2)\). For rational \(F\), the orders of its shift quotient sum to zero along each orbit \(a+N\mathbb Z\). Thus translation by \(K\) must preserve the divisor of \(m\) on these orbits. Its unique negative orbit is \(0+N\mathbb Z\), with multiplicity \(-2\), forcing \(K\in N\mathbb Z\). Conversely, at those levels the recurrence for \(g\) telescopes to a finite product. At \(K=0\) the scalar component vanishes and the simple current bracket survives.

For the determinant-one rational double, the difference variable also enters a coinvariant construction on the marked sphere. At irrational level the two-point pairing is nondegenerate. Contracting the output of the field against this pairing gives the normalized three-point block, which determines the field. Etingof and Kazhdan identify it with the matrix formula and extend the construction to rational levels by continuity. This geometric realization uses the marked coordinates. Descent of the braided fields under a general change of formal coordinate requires a compatible coordinate action. [Etingof–Kazhdan, §3.3 and Corollaries 3.3–3.4](https://arxiv.org/abs/math/9808121)

The rational orthogonal and symplectic doubles also carry quantum vertex algebras on their vacua. For \(\mathfrak{gl}_{M|N}\) with \(M\ne N\), the graded permutation gives a quantum vertex superalgebra at every level \(c\). Restricted double modules of level \(c\) carry fields of this algebra. A restricted module of the reflection algebra at level \(c\) carries a quasi-module of the vacuum algebra at \(2c\). The reflected exchanges involve both the sum and the difference of the two coordinates. More generally, for symmetrizable Cartan data Kong and Li construct a universal vacuum with a weak quantum vertex algebra structure and identify its modules with restricted modules of their double. [Butorac–Jing–Kožić, Theorem 2.2](https://arxiv.org/abs/1904.03771) · [Bagnoli–Kožić, Theorems 4.3 and 6.3](https://arxiv.org/abs/2608.12162v2) · [Kong–Li, Theorems 5.13 and 5.15](https://arxiv.org/abs/2509.16528)

For the ordinary matrix-extended vertex algebra, the precise quotient of the integral form is \(\operatorname{Zhu}(\mathcal W_\infty^{(r)})\cong Y_{\epsilon_1}(\mathfrak{gl}_r)[\epsilon_2,\mathfrak c]\). Here \(\epsilon_1\) is the Yangian parameter. The second deformation parameter and the central parameter extend its coefficient ring. The Yangian acts on Zhu top spaces. The vertex algebra also has a coassociative coproduct from the matrix Miura construction. Its proposed physical meaning is the fusion of surface defects in the twisted M2–M5 system. A quiver can supply a different positive result. For a tripled ADE quiver with canonical potential, the extended cohomological Hall algebra realizes the positive Yangian Borel, including its Cartan part, and its vertex coproduct agrees with the deformed Drinfeld coproduct. This constructs a spectral **coproduct** on Hall classes. A vacuum field requires a map in the other direction that multiplies two states at a separation. [Gaiotto–Rapčák–Zhou, §4, especially (4.41)](https://arxiv.org/abs/2309.16929) · [Jindal–Kaubrys–Latyntsev, Theorem 6.2.7](https://arxiv.org/abs/2603.21707)

The affine Yangian of \(\mathfrak{gl}_1\) has three weights \(h_1+h_2+h_3=0\). On a plane partition its commuting Cartan series \(\psi(u)\) measures the occupied boxes, while the root currents \(e(u)\) and \(f(u)\) add and remove a box. This is an action on a space of states. Rank one in the rational matrix formula above gives \(P=I\) and normalized \(\mathsf R=I\). A coweight shift changes another datum. For a type-A nilpotent orbit the corresponding finite \(W\)-algebra is a quotient of a shifted Yangian. For simply laced semisimple \(\mathfrak g\) the shifted coproducts \(Y_{\mu_1+\mu_2}\to Y_{\mu_1}\otimes Y_{\mu_2}\) associate when the middle shift in a triple is antidominant. The two composites differ already for \(\mathfrak{sl}_2\) with shifts \((0,2,0)\). These quotient and module constructions retain different parts of a field algebra. [Li–Yamazaki, §3](https://arxiv.org/abs/2003.08909) · [Brundan–Kleshchev, Theorem 10.1](https://arxiv.org/abs/math/0407012) · [Finkelberg–Kamnitzer–Pham–Rybnikov–Weekes, Theorem 4.12, Proposition 4.14 and Remark 4.15](https://arxiv.org/abs/1608.03331)

### What the rational currents generate {#ch12-intrinsic-rtt-modes}

At one position a Laurent multiplier \(z^m\) extracts the coefficient \(a_{(m)}=\operatorname{Res}_{z=0}z^mY(a,z)\,dz\). With two positions, the multiplier \(1/(x-y)\) also probes a collision away from the puncture. For two ordinary affine currents with multiplier \(1\), exchanging their zero modes leaves a single current at the merged position, namely their Lie bracket. In the quantum theory the exchange coefficient can itself have a pole while the two states still occupy separate slots. The mode algebra therefore keeps a generator for each number of positions.

**Definition (multipoint mode).** At precision \(d\ge1\), put \(R_d=\mathbb C[\hbar]/(\hbar^d)\) and \(V_d=U/\hbar^dU\), with \(U\) the divided creation algebra. An \(n\)-point mode \([f;a_1,\ldots,a_n]\) has a multiplier \(f\) regular on configurations of distinct nonzero positions and a state \(a_i\in V_d\) at each position. Integration by parts imposes \(\partial_{z_i}+T_i=0\), where \(T_i\) translates the \(i\)-th state. Concatenation multiplies the multipliers. For \(w=[f(x,y);a,b]\), let \(\mathcal S(t)\) be the rational field exchange on \(V_d\otimes_{R_d}V_d\). Its inputs can be any divided states, including translates. Write \(\mathcal S(t)(b\otimes a)=\sum_\nu h_\nu(t)b_\nu\otimes a_\nu\). Applying the state exchange and then interchanging the two positions gives
\[
 \sigma w=\sum_\nu [f(y,x)\,h_\nu(x-y);b_\nu,a_\nu].
\]
Put \(x=y+u\) at the collision. The one-point mode \(\rho w\) at \(y\) takes the \(u^{-1}\) coefficient of \(f(y+u,y)Y(a,u)b\). Impose \(w-\sigma w=\rho w\). In a longer word impose this relation at each adjacent pair, keeping the other positions and their poles in the multiplier. Write \(M_d\) for this mode algebra. The empty word is its multiplicative unit \(1\). A separate generator is the occupied point with state \(\mathbf1\) and multiplier \(z^{-1}\), denoted \(\mathsf v=[z^{-1};\mathbf1]\). The normalized algebra is \(\bar M_d=M_d/(\mathsf v-1)\), the quotient by the generated two-sided ideal.

This last identification can be tested. In the creation-first convention the classical affine commutator supplies \(K\mathsf v\,\Omega/(u-v)^2\), while the centered shifts in the mixed relation supply \(-K\Omega/(u-v)^2\). Without normalization the difference \(K(\mathsf v-1)\Omega/(u-v)^2\) is nonzero at \(K\ne0\). Thus an equality after acting on the vacuum would miss a relation inside the intrinsic algebra.

At rank two and level \(K=0\), work modulo \(\hbar^2\). For the trace-form currents put \(J_{ij}=-\ell_{ij}^{[0]}\), \(E=J_{12}\), \(F=J_{21}\) and \(H=J_{11}-J_{22}\). For \(w=[1;E,F]\) and \(u=x-y\) the two terms are
\[
\begin{aligned}
 \sigma w&=[1;F,E]+\hbar\bigl([u^{-1};H,H]+2[u^{-1};F,E]\bigr),\\
 \rho w&=[1;H]-\hbar[1;\tfrac12 H^2+EF].
\end{aligned}
\]
Each simple pole in \(\sigma w\) still carries two current states. The products \(H^2\) and \(EF\) in \(\rho w\) are taken in the divided creation algebra at the surviving point. [CQ11](#ref-ch12-cq11)

**Definition (Cauchy lift).** Let \(e_{ij}=\ell_{ij}^{[0]}\) be the matrix-current states. For a Laurent multiplier \(f\), start with \([f;e_{ij}]\). For the term with \(r\) ordered currents, multiply their matrix entries along the chain of indices from \(i\) to \(j\), summing the internal indices, and use the multiplier \(f(z_1)/\prod_{a=1}^{r-1}(z_a-z_{a+1})\) with coefficient \((-\hbar)^{r-1}\). Only \(r\le d\) remains at precision \(d\). In particular the first creation correction is

\[
-\hbar\sum_a [f(x)/(x-y);e_{ia},e_{aj}] .
\]

The negative-current lift also includes the shift of its argument by \(-K\hbar/2\). With these prescribed lifts, at rank two and **every** numerical level \(K\) there is an injective algebra homomorphism with proper image

\[
D_K/\hbar^2D_K\ \longrightarrow\ \bar M_2 .
\]

The precision is taken **after division** of the two same-half RTT relations and the centered mixed relation by \(\hbar^2\), and of each determinant defect by \(\hbar\). Thus the identities retain the constant and linear coefficients of each divided relation. Both divided determinants hold to this precision in every rank \(N\ge2\), even before identifying the local vacuum. For the determinant, the descending-column shifts give a translation of the diagonal states, which cancels their first integral trace correction. The remaining coefficient is an exchange difference whose collision residue is the ordered state product. In the mixed rank-two relation, sliding a current across both slots of its Cauchy correction keeps the spectator pole. The derivative from undoing the spectral shift cancels the central first-order correction. These computations take place inside the mode algebra. [CQ11](#ref-ch12-cq11)

The missing modes have a geometric witness. Reduce at \(\hbar=0\) and filter by number of positions. In the two-current component, the symmetrized leading multiplier of

\[
[(x-y)^{-1};e_{12},e_{21}]
\]

has \(e_{12}\otimes e_{21}\) coefficient \(1/(2(x-y))\). Products of classical single-current modes have Laurent-polynomial coefficients in \(x,y\), regular along \(x=y\) away from the punctures. The ordered Poincaré–Birkhoff–Witt symbols of higher-degree words are independent, so cancellation among such words cannot produce this two-point pole. The same independence gives injectivity of the classical current map. Freeness over \(R_2\) then lifts injectivity to the displayed precision. The pole already excludes generation of the whole normalized multipoint algebra by these lifts. [CQ11](#ref-ch12-cq11)

Does the rank-two homomorphism survive one more power of \(\hbar\)? At the critical level \(K=-2\), a single number decides the question. Use the same Cauchy lifts in the normalized mode algebra over \(\mathbb C[\hbar]/(\hbar^3)\). Take the \(p^{-1}u^0\) coefficient of the centered mixed relation, with \(p\) the annihilation parameter and \(u\) the creation parameter. Read its matrix entry from column \((2,2)\) to row \((1,1)\). After division of the RTT relation by \(\hbar^2\), it is the \(\hbar^2\) coefficient that must vanish. This is the quartic coefficient before division.

To measure it, take the part with three insertion points. Average the six orders of the slots, project to the vacuum at \(x\) and to the translation towers of the current \(e_{12}\) at \(y,z\). Transfer derivatives of either current to its multiplier by the translation relation. Finally take the residue at \(x=y\), keeping \(z\) separate. An \(x\)-derivative has zero residue; a detached normalized vacuum with multiplier \(x^{-1}\) has no pole there. The residue therefore detects a class in the normalized mode algebra itself. The mixed entry gives \(K/[3yz(y-z)]\), which at \(y=1,\ z=2,\ K=-2\) is \(1/3\).

In every rank \(N\ge2\), the same calculation with \(e_{1N}\) detects a defect in each of the three relations. For the creation, annihilation and centered mixed entries, respectively, the residues are
\[
 \frac{K}{3y^2z^2(y-z)},\qquad \frac{K}{3(y-z)},\qquad
 \frac{K}{3yz(y-z)} .
\]
The first two use the coefficients \(u^0v^2\) and \(p^0q^{-2}\) after clearing the same-half spectral denominator. Thus at every nonzero level the prescribed lifts already fail modulo \(\hbar^3\), including at \(K=-N\). An all-order homomorphism with these generator images would reduce to one at this precision.

Both divided quantum determinant defects vanish at this precision in every rank and at every level. In rank two both auxiliary partial traces of each divided RTT defect also vanish. What happens to the remaining tensor product of traceless auxiliary matrices? Under simultaneous \(\mathrm{SL}_2\) conjugation it is \(V_4\oplus V_2\oplus V_0\), where \(V_j\) has highest weight \(j\). At \(K=0\) all three projections of each defect vanish. Thus the original Cauchy assignment gives
\[
 D_0/\hbar^3D_0\ \hookrightarrow\ \bar M_3
 \qquad (N=2,\ K=0)
\]
with proper image. The two algebras are free over \(\mathbb C[\hbar]/(\hbar^3)\). A first nonzero \(\hbar\)-coefficient of a kernel element would contradict classical injectivity. Surjectivity would express the two-point pole above as a polynomial in classical current modes.

Can one change the lifts at \(K\ne0\) while preserving their actions on states? In rank two write \(W_f^{ij}\) for the divided Cauchy lift with Laurent multiplier \(f\), with the original centred spectral shift. The minus sign in the annihilation series multiplies the entire corrected lift. Set \(J^{ij}=\tfrac12\sum_\ell(e_{i\ell}\otimes e_{\ell j}-e_{\ell j}\otimes e_{i\ell})\) and \(S^{ij}=\mu((T\otimes1)J^{ij})\), with \(\mu(a\otimes b)=a_{(-1)}b\), the regular coefficient of \(Y(a,z)b\). Add \(\hbar^2(U_f^{ij}+D_f^{ij})\) to \(W_f^{ij}\), where
\[
 \begin{aligned}
 U_f^{ij}&=2K\left[\frac{f(z)}{(x-y)(y-z)^2};J^{ij}(y,z),\mathbf1(x)\right],\\
 D_f^{ij}&=-K\left[\frac{f(y)}{x-y};S^{ij}(y),\mathbf1(x)\right].
 \end{aligned}
\]
The vacuum occupies the last slot. For example \(1/(x-y)\), expanded in \(x\) about the puncture with \(y\ne0\), has no \(x^{-1}\) coefficient. Expanded about the occupied position \(x=y\), its residue is one. The first expansion makes the terminal correction invisible on normalized smooth multipoint modules. The second explains how the correction can change an intrinsic relation. Both corrections vanish at \(K=0\).

Through divided precision three these modified lifts preserve the determinants and partial traces. They satisfy the \(V_4\) and \(V_0\) projections of all three RTT relations at every level. The \(V_2\) equation still fails in each relation at every \(K\ne0\). For a mixed entry take the ordered colours \(b=e_{12}\), \(H=(e_{11}-e_{22})/2\) and the coefficient \(p^{-2}u^0\). In the convention for current modes, \([b,H]=b\). Project the averaged symbol to two vacua at \(x,y\) and the translation tower of \(b\) at \(z\). Move each derivative of \(b\) to its Laurent multiplier before taking the residues first at \(x=z\), then at \(y=z\). The coefficient along \(b\) is \(2K^2/(3z^2)\), hence \(8/3\) at \(K=-2,\ z=1\). The unnormalized covector \(b\otimes H-H\otimes b\) gives twice this coefficient. The earlier \(1/3\) measured a single residue of the original lifts at a different Laurent coefficient.

The scalar projection needs care at the critical level. In the classical universal affine \(\mathfrak{sl}_2\) vacuum module at \(K=-2\), the quadratic Segal–Sugawara state has a nonzero intrinsic one-point class with constant multiplier whose action on all states vanishes. After the two-point and three-point terms of the scalar equation are reduced, its remaining one-point coefficient is polynomial in \(K\). The vacuum module detects every finite Laurent one-point class at noncritical level. Vanishing there forces this polynomial to vanish also at \(K=-2\).

There is a rank-two lift that cancels the remaining adjoint residue. For \(a\) an entry of the traceless current matrix \(e-\tfrac12\operatorname{tr}(e)I\) and \(l\) a Laurent polynomial, write
\[
 \mathcal J_r(l;a)=\left[\frac{l(z)}{\prod_{i=1}^r(x_i-z)};a(z),\mathbf1(x_1),\ldots,\mathbf1(x_r)\right]\qquad(r=1,2).
\]
Let \(P_-\) retain the strictly negative Laurent powers. To \(W_f^a+\hbar^2(U_f^a+D_f^a)\) add
\[
 \hbar^2K^2\left(\mathcal J_2(f'';a)+\mathcal J_1\bigl(\tfrac12 f''-(P_-f)'';a\bigr)\right).
\]
The innermost vacuum in each word has zero puncture residue on normalized smooth modules. At the same ordered mixed coefficient for \(b,H\), the two-vacuum word contributes \(-2K^2/(3z^2)\), cancelling the \(8/3\) at \(K=-2,\ z=1\). On \(H\otimes b-b\otimes H\) the remaining one-vacuum residue is \(2K^2/z^2\), and the one-vacuum word contributes \(-2K^2/z^2\). With these images both half relations, the centered mixed relation and both divided determinants hold. At every numerical level \(K\) the resulting injection \(D_K/\hbar^3D_K\hookrightarrow\bar M_3\) has proper image.

The original normalized embedding modulo \(\hbar^2\) holds in every rank at every level. At \(K=0\) every slot in a Cauchy word lies in the state augmentation ideal. The counit ensures that exchange and occupied collisions preserve the span of all words with slots in this ideal. This span and the scalar unit act faithfully on the universal vacuum module at every precision. Thus the RTT and determinant identities on states hold in the mode algebra. For every \(N\ge2\) the original maps from \(D_0/\hbar^dD_0\) to \(M_d\) and to \(\bar M_d\) are compatible injections with proper image for every \(d\ge1\). Both \(\hbar\)-adic inverse-limit maps are continuous injections with proper image.

At rank two and \(K=-2\), a further change with zero state action makes the mixed adjoint coefficient \([p^{-2}u^0]\), the adjoint half rows \([u^0v^j]\) and \([p^{-1}q^{-j}]\), and both divided determinant defects vanish together modulo \(\hbar^4\). A full rank-two lift at fourth precision and a higher-rank lift at third precision remain open at nonzero level. The field identities act on vacuum states. The level-composing coproduct of modes lands in the joint algebra, which retains both state inputs at each position. To land in a completion of two separately integrated factors one must also realize poles between their positions, such as \(1/(x-y)\). [The joint level coproduct](18-open-problems.md#problem-chiral-quantum-groups)

In rank two at \(K=-2\), fix the puncture \(s=0\) and the representative \(W_1\) of the horizontal Lie action in \(\bar M_4\). Write \(B_f(a)=[f;a]\) for a classical singleton current and \(S=\sum_i(u_i)_{-1}(u^i)_{-1}\mathbf1\) for the quadratic Sugawara state in trace-dual bases. The only possible singular current product with \(S\) is \(a_{(1)}S=2(K+2)a\). Hence \(C=[t;S]\) commutes with the currents and kills the universal vacuum module since \(S_{(1)}\mathbf1=0\). On the standard two-dimensional top of a smooth critical induced module it acts by the Casimir \(3/2\).

For each \(q\ge1\) add \(\hbar^3 C^qB_{L(f)}(a)\) to the divided lift, with \(L(f)=-s^{-2}\partial_s(P_-f)\) and \(P_-\) the strictly negative Laurent projection. On either half \(L\) is a derivation and \(f'L(g)-g'L(f)=0\), so every same-half defect has zero variation. Tracelessness preserves both divided determinants. For \(f=s^m,\ g=s^{-r}\), \(m\ge0,\ r\ge1\), the Leibniz difference \(fL(g)+gL(f)-L(fg)\) is \(\min(m,r)s^{m-r-3}\). With the annihilation sign, the change in the \(\hbar^3\) coefficient of the mixed adjoint row \([p^{-m-1}u^{r-1}]\) is
\[
2C^q B_{\min(m,r)s^{m-r-3}}(a).
\]
For \(a=b=e_{12}\) the contraction is \(H\otimes b-b\otimes H\). The marked row \([p^{-2}u^0]\) therefore changes by \(2C^qB_{s^{-3}}(b)\). Its symbol with \(q\) Sugawara slots and one current has multiplier \(2t_1\cdots t_qz^{-3}/(q+1)\). All slots are occupied, so normalization preserves these independent classes of different arities. For equal colours \(d,d\) with \(\operatorname{tr}(d^2)=1\), the \([p^{-5}u^0]\) change is \(-KC^q\operatorname{Res}_{s=0}4s^3s^{-4}\,ds=8C^q\). More generally, preservation of the two halves by a correction of the form \(C^qB_{L(f)}(a)\) forces separate derivations \(\alpha\partial_s,\beta\partial_s\). The equal-colour rows then test every residue \(\operatorname{Res}_{s=0}(\alpha-\beta)s^{m-r-2}\,ds\). Fixing them all forces \(\alpha=\beta\) and removes the mixed variation in this family.

A change invisible on every normalized smooth module is \(\hbar^3[t^{-1};S]\mathcal J_j(-\partial_sP_-f;a)\), where \(\mathcal J_j(l;a)\) places the current at \(z\) and \(j\) terminal vacua at \(x_i\) with multiplier \(l(z)/\prod_i(x_i-z)\), for \(j=1,2\). The innermost puncture residue vanishes and the pure-vacuum Ward term is zero after normalization. This preserves both half defect matrices, both determinants and every equal-colour mixed row. The change at \([p^{-2}u^0]\) is \(2[t^{-1};S]\mathcal J_j(s^{-1};a)\). In the symmetric symbol, taking the residues at all \(x_i=z\) with the two occupied slots labelled gives \(t^{-1}z^{-1}/3\) and \(t^{-1}z^{-1}/6\), respectively. A full lift still requires one choice satisfying the remaining mixed and same-half equations together.

The Cauchy relations involve two halves of the double. Dualizing just the annihilation half gives a differential without the mixed curvature. In the regular half-dual the generating series of odd matrix coefficients satisfies
\[
c(y)=\sum_{s\ge1}c_sy^{s-1},\qquad
dc(y)=-c(y)^2,
\]
with exchange relations
\[
c_{ij}(y)c_{kl}(y')+c_{kl}(y')c_{ij}(y)
=\frac{\hbar}{y-y'}
\bigl(c_{kj}(y)-c_{kj}(y')\bigr)
\bigl(c_{il}(y)-c_{il}(y')\bigr).
\]
Its ordered exterior monomials form a topological basis, but its algebra is deformed. With \(Tc_s=sc_{s+1}\), its fields are regular:
\[
Y(a,z)b=(e^{zT}a)b.
\]
These fields have a nontrivial quantum exchange and satisfy the differential graded quantum vertex identities in their specified \(\hbar\)-adic domain. [CQ5](#ref-ch12-cq5)

The **full curved dual** also retains the mixed creation–annihilation relation. Its curvature contains
\[
\Theta_K(x)=\hbar^{-2}
\left(1-\mathsf R(x+K\hbar/2)^{-1}
             \mathsf R(x-K\hbar/2)\right),
\qquad
[x^{-2}]\Theta_K=K\Omega.
\]
Inserting \(\mathsf R(x)=I-\hbar\Omega/x+O(\hbar^2)\), the positive shift contributes \(+K\hbar^2\Omega/(2x^2)\) and the negative shift contributes its negative. The unshifted second-order term cancels in the ratio. Subtracting that ratio from \(1\) gives the displayed positive sign. At \(K=0\) the two shifted matrices coincide and this mixed curvature term vanishes identically. The closed two-sided ideal generated by the creation ghosts is stable under the differential and contains this curvature. The quotient contains the regular half-dual. Thus passage to half-ghosts can remove precisely the mixed datum that remembers the level. [CQ5](#ref-ch12-cq5)

### Smooth modules of the Yang double at a point {#ch12-yang-double-at-a-point}

Keep both sets of ghosts and take the normalized \(\mathfrak{gl}_N\) point double, \(N\ge2\), at \(K\in\mathbb C\), without a determinant relation. At precision \(d\ge1\) the scalars are \(R_d=\mathbb C[\hbar]/(\hbar^d)\). A left module is smooth if every vector is killed by all sufficiently high annihilation modes. In the restricted dual, each functional has a lower bound on its total-weight support at every fixed upper bound on creation weight. A contramodule can sum terms whose coefficients eventually vanish on each such creation window. Twisting takes a termwise \(R_d\)-free complex of smooth modules to a free graded contramodule with a connection. The raw convolution dual acts on the right. If its curvature is \(\theta\), the connection satisfies \(D^2f=-f\theta\). The graded opposite acts on the left with curvature \(-\theta\). Smooth coinduction is the right adjoint. On a free generator its counit evaluates the coinduced function at the unit of the double.

The adjunction becomes an equivalence in two specified quotients. On the smooth side, reduce modulo \(\hbar\) and restrict to \(\mathfrak p=\mathfrak{gl}_N[[t]]\). A complex is null if this restriction belongs to the triangulated subcategory generated by totalizations of short exact sequences of complexes and closed under coproducts and retracts. On the curved side, the underlying graded contramodule must be a retract of a free one on a graded \(R_d\)-free module. Reduce modulo \(\hbar\), then divide out the allowed contramodule sums whose coefficients restrict to zero on \(\mathfrak p\). This gives a complex over the continuous cochain algebra \(C^\bullet_{\rm cont}(\mathfrak p)\). The null objects are those for which the complex of maps from this positive reduction into every dg module with graded-injective underlying module is acyclic. Both functors, their unit and their counit commute with every reduction \(R_d\to R_e\), \(1\le e\le d\). The cones of the unit and counit are null by the classical equivalence.

Passing to all precisions changes what a morphism can detect. Put \(R=\mathbb C[[\hbar]]\) and \(E=(\bigoplus_{j\ge1}\mathbb C v_j)[[\hbar]]\). Take the scalar complex \(T=(E\xrightarrow{\delta}E)\) in degrees zero and one, with \(\delta v_j=\hbar^j v_j\). The vector \(y=\sum_{j\ge1}\hbar^j v_j\) has primitive \(z_d=\sum_{1\le j<d}v_j\) modulo \(\hbar^d\). A formal primitive would have every coefficient equal to one, whereas the coefficients of a vector in \(E\) must tend to zero \(\hbar\)-adically.

To see \(y\) in a point module, write \(D_d^{\rm pt}\) for the point double at precision \(d\). Let \(I_{\ell,d}\) be its left ideal generated by the annihilation modes of index greater than \(\ell\). Take \(M=\varprojlim_d\bigoplus_{\ell\ge1}D_d^{\rm pt}/I_{\ell,d}\) in degree zero. The scalar functional \(p:M\to R\) takes the coefficient of the empty ordered word in the first cyclic summand. It sends the class \(e_1\) of the unit there to one.

Untwisted smooth coinduction \(J\) is right adjoint to forgetting the point action. Evaluation at the unit identifies the complex of maps from \(M\) to \(J(T)\) with that of continuous scalar maps from \(M\) to \(T\). It also computes maps in the localization because a null smooth complex becomes contractible after forgetting the action. Under this identification \(m\mapsto p(m)y\) gives the degree-one point map \(f(m)(a)=p(am)y\), where \(a\) belongs to the formal point double. At precision \(d\), replacing \(y\) by \(z_d\) gives a primitive for the reduced map. A formal primitive evaluated on \(e_1\) and at \(a=1\) would supply a primitive for \(y\). Thus \([f]\) gives a nonzero element of \(\lim^1_d H^0\) of the finite mapping complexes.

On the smooth side take complete topologically free \(\mathbb C[[\hbar]]\)-terms, allowing the annihilation cutoff of a vector to depend on the precision. On the curved side take degreewise complete objects whose entire underlying graded contramodule is a retract of a free one with joint creation-weight and precision bounds on its sums. With the same two null tests, the formal point localizations are the homotopy limits of their finite localizations. Every coherent system has a formal representative, even in unbounded cochain degrees. Extending the point comparison to quantum vertex modules, their collisions and their tensor products requires compatible field actions. [CQ5](#ref-ch12-cq5)

### Consecutive collisions of RTT Yangian states {#ch12-ordered-yangian}

Read the three positions from left to right and start a new block each time the position changes. At \((x,y,x)\), with \(x\ne y\), the blocks are \(x|y|x\). At \((x,x,y)\) they are \(xx|y\). Only in the second configuration are the first two states multiplied. This distinction gives an associative chiral algebra in which two adjacent Yangian states collide by their ordered product. Its coproduct acts on two copies at the same positions.

Take \(X=\mathbb A^1_{\mathbb C}\). A **run** of a configuration is a maximal consecutive string of equal positions. Let \(P_n\) be the subsets of \(\{1,\ldots,n-1\}\), ordered by inclusion. The map \(p_n:X^n\to P_n\) records the gaps \(z_i\ne z_{i+1}\). For a unital algebra \(H\) over \(\mathbb C\), put
\[
 M_H(S)=H^{\otimes(|S|+1)} .
\]
For \(S'\supseteq S\), multiply, in order, the runs of \(S'\) that join into a single run of \(S\). Associativity makes this a diagram on \(P_n^{\mathrm{op}}\). On the analytic space of \(X^n\) it has a constructible realization \(C_n(H)\) with these extraordinary fibres. For finite-dimensional coefficients, take the ordinary sheaf on \(P_n\) with stalks \(M_H(S)^*\) and the transposed maps, pull it back by \(p_n\), and Verdier-dualize. Here upward-closed subsets of \(P_n\) are open. These sheaves are constructible with constant local systems on the algebraic strata. Riemann–Hilbert realizes them by regular holonomic complexes of right differential modules. The dual of the constant sheaf corresponds to \(J_n=\omega_{X^n}[n]\). For filtered coefficients, apply the construction on finite pieces of the entire diagram and take the filtered colimit. Set \(C_0(H)=\mathbb C\).

**Theorem.** For the RTT Yangian \(H=Y(\mathfrak{gl}_N)\), the word coalgebra \(C(H)\) factorizes across consecutive cuts. The associative chiral algebra \(A(H)=\Omega_{\rm cut}C(H)\) has a vacuum marking, a coassociative coproduct to two copies at the same positions, and a counit. For \(N\ge2\) its adjacent collision distinguishes the order of the states. Its bar admits no factorization across all subsets of the labels.

*Proof.* Repeating a label inserts zero gaps and leaves the diagram of runs unchanged. Ordinary pullback of its dual sheaf therefore gives the smaller diagram, and Verdier duality gives \(d_\alpha^!C_n(H)=C_m(H)\) for every monotone collision. On the open \(U_{p,q}\) all points in the first block are distinct from all points in the second. The gap between the blocks is open there. Splitting the list of runs at this gap identifies \(C_{p+q}(H)\) with \(C_p(H)\boxtimes C_q(H)\) on \(U_{p,q}\). Its adjoint is the map to the open direct image in the cut coproduct. Splitting into three or more blocks gives the same list for every sequence of cuts. Empty cuts act by the identity. Connected bar–cobar duality now identifies \(BA(H)\) with \(C(H)\). The unit of \(H\) gives the coalgebra map \(J=C(\mathbb C)\to C(H)\). The unit of \(A(H)\) lies at the empty configuration.

Tensoring two diagrams at the same run interleaves their factors in pairs. It gives
\[
 C(H)\otimes^! C(H')\simeq C(H\otimes H'),\qquad
 A\diamond A'=\Omega_{\rm cut}\bigl(BA\otimes^!BA'\bigr).
\]
On a cut open, interleaving before splitting and splitting before interleaving give the same pairs. Adjunction extends this identity to the cut maps. The Yangian matrix coproduct and counit are algebra maps. Applying \(C\) and then cobar gives \(A(H)\to A(H)\diamond A(H)\) and \(A(H)\to A(\mathbb C)\). Every iterated output uses the ordinary iterated Yangian coproduct within each run. This proves coassociativity, interchange and the counit laws. The singleton coefficient of \(A(H)\) is \(\omega_X\otimes H\).

On two points with complement \(j:U\hookrightarrow X^2\), multiplication \(m:H\otimes H\to H\) has the section \(a\mapsto1\otimes a\). The extension splits as
\[
 C_2(H)\simeq (J_2\otimes H)\ \oplus\
              (Rj_*J_U\otimes\ker m).
\]
The second term is singular at coincidence. Its coefficient contains \(1\otimes a-a\otimes1\) for every nonscalar \(a\). On \(z_1\ne z_2,\ z_3\ne z_2\), the three-run coefficient \(C_3(H)\) is smooth even when \(z_1=z_3\). Factorization for \(\{1,3\}|\{2\}\) would give the singular binary extension there. This rules out that extension of the bar. The cut support formula gives an actual surviving coefficient at the outer collision, with extraordinary point fibre \(H^{\otimes3}[-1]\) for \(A(H)\) at \((x,y,x)\). For adjacent Yangian generators the evaluation representation sends \(t^{(1)}_{12}t^{(1)}_{21}\) and \(t^{(1)}_{21}t^{(1)}_{12}\) to \(E_{11}\) and \(E_{22}\). ∎

**Two deformation parameters.** Write \(t^{(r)}_{ij}\), \(r\ge1\), for the ordinary RTT generators, normalized by \(T(u)=I+\sum_{r\ge1}t^{(r)}u^{-r}\). Over \(R=\mathbb C[h,t]\) form the subalgebra of \(Y(\mathfrak{gl}_N)[h,t]\) generated over \(R\) by
\[
 X^{(r)}_{ij}=h^rt^{r-1}t^{(r)}_{ij}.
\]
Its ordered monomials form a free \(R\)-basis. Indeed the RTT straightening commutator has output of total mode weight \(r+s-1\) on inputs of weight \(r+s\). After the rescaling each linear term has coefficient \(h\), and each quadratic term has coefficient \(ht\). Induction on the weight straightens products, and Yangian PBW gives independence. The matrix coproduct becomes
\[
 \Delta X^{(r)}_{ij}
 =X^{(r)}_{ij}\otimes1+1\otimes X^{(r)}_{ij}
  +t\!\sum_{\substack{p+q=r\\p,q>0}}\sum_k
                  X^{(p)}_{ik}\otimes X^{(q)}_{kj}.
\]
Put \(X(u)=\sum_{r\ge1}X^{(r)}u^{-r}\). The matrix \(I+tX(u)\) is group-like. The antipode on \(X(u)\) is \(((I+tX(u))^{-1}-I)/t\), polynomial in the generators and \(t\) at each mode. The counit kills each \(X^{(r)}_{ij}\). Each bounded total mode weight of the run diagram is finite free. Its finite relative dual construction commutes with change of coefficients, and taking the filtered colimit gives the family over \(R\) and its fibres. The fibre \(t=0\) has the enveloping relations of \(\mathfrak{gl}_N[v]\) with bracket scaled by \(h\) and primitive coproduct. At \(h=0\) the algebra is polynomial, and its coproduct pulls back the ordered matrix series law \(X+Y+tXY\). At \(h=t=1\) one recovers the full Yangian. [Molev, Nazarov and Olshanskii, §§1.20–1.28](https://arxiv.org/abs/hep-th/9409025)

The two first variations meet on a single current. At the origin let \(x^{(r)}_{ij}\) denote the primitive linear generators. Denote the \(h\)-coefficient of the commutator by \([\ ,\ ]_1\), and the \(t\)-coefficient of \(\Delta-\Delta^{\rm op}\) by \(\delta\). In rank two,
\[
 [x_{11}^{(1)},x_{12}^{(2)}]_1=x_{12}^{(2)},\qquad
 \delta(x_{12}^{(2)})
  =(x_{11}^{(1)}-x_{22}^{(1)})\wedge x_{12}^{(1)}\ne0 .
\]
Both operations on the primitive space are invariant under an isomorphism of the parameterized Hopf families. In a tensor product of a multiplication deformation with fixed cocommutative coproduct and a coproduct deformation with fixed commutative multiplication, the first bracket takes values in the first primitive summand and the first cobracket vanishes there. The displayed composite excludes such a decomposition.

The mixed coefficient can also be read before taking either variation. In rank two,
\[
 [X^{(2)}_{11},X^{(2)}_{22}]
 =ht\bigl(X^{(1)}_{21}X^{(2)}_{12}-X^{(2)}_{21}X^{(1)}_{12}\bigr).
\]
The two monomials in parentheses have distinct images in the polynomial fibre. The commutator therefore survives modulo \((h,t)^3\).

Substitution \(X(u)\mapsto X(u-s)\) is a Hopf automorphism \(\sigma_s\), polynomial on each coefficient. For output parameters \(s_1,\ldots,s_\ell\) the map \((\bigotimes_i\sigma_{s_i})\Delta^{(\ell)}\) gives a coproduct of the same configuration objects. Subdividing output \(i\) adds \(s_i\) to each of its new parameters. These parameters translate the Yangian current. The collision extension itself uses the positions of points on \(X\). Identification with vertex fields would require their collision residues and exchanges, including the nonconsecutive collision excluded above.

**A Yangian field on all ordered collision charts**

One can change the extension at a collision of nonconsecutive labels. The new datum is a rule for crossing a spectator before multiplying the states brought together. It gives a second configuration algebra on the same RTT Yangian.

Let \(H\) be the Yangian above, or its two-parameter form. Write \(\sigma_sX(u)=X(u-s)\), and let \(T\) be the infinitesimal generator of \(\sigma_s\). Thus \(TX^{(r)}=(r-1)X^{(r-1)}\) for \(r>1\), and \(TX^{(1)}=0\). This derivation is locally nilpotent on every state, so \(\sigma_s=e^{sT}\) is polynomial there. For a unital associative algebra the Dăscălescu–Nichita braid operator has the specialization
\[
 c(a\otimes b)=ab\otimes1+1\otimes ab-a\otimes b .
\]
Write \(\tau\) for the flip, \(S_0=c\tau\), and define the fields and exchange by
\[
\begin{aligned}
 Y(a,z)b&=(\sigma_z a)b,\\
 S(z)(a\otimes b)
 &= (\sigma_{-z}b)a\otimes1
       +1\otimes b(\sigma_z a)-\sigma_{-z}b\otimes\sigma_z a .
\end{aligned}
\]
The fields have regular products. They retain derivatives in collisions. With \(s\) the separation of the two points, for instance,
\[
 \operatorname{Res}_{s=0}s^{-2}Y(X^{(2)}_{12},s)X^{(1)}_{21}\,ds
       =X^{(1)}_{12}X^{(1)}_{21}.
\]
In the fundamental evaluation representation at \(h=t=1\), this is \(E_{11}\). The term linear in \(s\) in \(S(s)(X^{(2)}_{12}\otimes X^{(1)}_{21})\) is \(1\otimes X^{(1)}_{21}X^{(1)}_{12}-X^{(1)}_{21}\otimes X^{(1)}_{12}\). It remains nonzero in the same representation on the two slots.

**Theorem.** These formulas give a quantum vertex algebra with polynomial exchange. Its residue coalgebra factorizes for all ordered decompositions, including \(\{1,3\}|\{2\}\). Over \(\mathbb C\) its cobar is an associative chiral algebra on the full ordered collision atlas. The Yangian coproduct is a morphism of the fields and their residue coalgebras into the joint same-position tensor specified below.

*Proof.* Denote multiplication by \(m\). The operator \(c\) exchanges a unit with its neighbour, \(c^2=1\) and \(mc=m\). Its two multiplication hexagons are
\[
 c(m\otimes1)=(1\otimes m)c_{12}c_{23},\qquad
 c(1\otimes m)=(m\otimes1)c_{23}c_{12}.
\]
For instance both sides of the first equation on \(a,b,d\) give \(abd\otimes1+1\otimes abd-ab\otimes d\). Expanding the second gives \(abd\otimes1+1\otimes abd-a\otimes bd\). The braid relation \(c_{12}c_{23}c_{12}=c_{23}c_{12}c_{23}\) follows by expanding the same formula. With vertical bars separating slots, each side is
\[
 abd|1|1+1|1|abd+1|ab|d+a|bd|1
     -ab|d|1-1|a|bd-a|b|d .
\]
Thus \(S_0\) is unitary, satisfies the Yang–Baxter equation and fixes both vacuum slots. Locality for the constant product is \(mS_0=m\tau\). The displayed exchange with translation is characterized by
\[
 (\sigma_v\otimes\sigma_w)S(v-w)
       =S_0(\sigma_v\otimes\sigma_w).
\]
Indeed \(S_0\) commutes with simultaneous algebra automorphisms. Conjugating in each insertion position carries the constant braid and hexagon identities to their spectral identities. The two ways of substituting three fields both give \((\sigma_{z+w}a)(\sigma_w b)d\). The vacuum is \(1\), translation is \(T\), and all clearing powers for the field products can be taken to be zero. [S. Dăscălescu and F. F. Nichita, *Yang–Baxter operators arising from (co)algebra structures*](https://doi.org/10.1080/00927879908826793)

At a partition of the labels, assign one \(H\) to each block at its own coordinate. Localize where distinct blocks have distinct coordinates and push this coefficient forward along the partition diagonal. To merge two blocks bring them together by the displayed exchange and take the entire principal part of the multiplier times \(Y(a,s)b\), including the Taylor expansion of every spectator. The full residue differential, ordered-chart transitions and factorization then follow from the rational-exchange construction in Chapter 5. To examine the \(\{1,3\}\) collision, keep label 2 distinct from both. On this open \(W\) the new ternary coefficient factors as the binary coefficient at \(1,3\) times the singleton at 2. In a separated binary frame the change \(a\otimes b\mapsto\sigma_s(a)\otimes b\) reduces the contact to the principal part after ordinary multiplication \(m\). Thus a polar coefficient with value in \(\ker m\) survives throughout the binary lattice, producing the singular extension along \(\Delta_{13}\) required on \(W\). The earlier three-run bar was smooth there. The field coalgebra over the cut chart and its cobar are defined for the flat two-parameter state module as well. Over the ground field the full ordered-atlas bar–cobar theorem applies. The same pole-free input works after every specialization of \(h,t\). The exchange can already be nontrivial in the joint commutative special fibre.

For a pair \(H,K\) of such differential algebras, put the state \(H\otimes K\) at each occupied position. Its field multiplies the translated \(H\)-states and the translated \(K\)-states componentwise. Give each pair of blocks the exchange \(S_{H\otimes K}\) from the displayed formula, using the product of \(H\otimes K\) and translation \(\sigma_s^H\otimes\sigma_s^K\). Use these merged coefficients, principal parts and exchanges on each chart. This defines a same-position tensor on this class of field systems. Its morphisms are the unital differential algebra maps, since \(Y(a,0)b\) recovers their multiplication. Its unit is the scalar field. On three systems either grouping uses the same multiplication and exchange on \(H\otimes K\otimes L\).

On a separating open \(U_{A,B}\), a surviving partition splits as \(\pi_A\sqcup\pi_B\). Regrouping its paired states by \(S_{H\otimes K}\) identifies the joint coefficient with the external product of the two joint block coefficients there. These are the interchange identifications for cuts and the joint tensor. Since \(\Delta_H\) is a unital algebra map commuting with \(\sigma_s\), it preserves \(Y\) and intertwines \(S_H\) with \(S_{H\otimes H}\). Applying \(\Delta_H\) at each occupied block therefore commutes with regrouping on \(U_{A,B}\), taking principal parts and changing charts. It yields a coproduct of the associative cobars into the joint tensor just defined. Coassociativity and counitality hold on every occupied block. ∎

The two independent exchanges of the separate systems give a different target. At \(z=0\) take a nonzero mode-one primitive \(x\), and put \(p=x\otimes1,\ q=1\otimes x\) in the output algebra \(H\otimes H\). On \(\Delta x\otimes\Delta x\), the joint exchange minus the independent exchanges has value
\[
 2\left(pq\otimes1+1\otimes pq-p\otimes q-q\otimes p\right).
\]
Applying the counit to the second occupied position gives \(2x\otimes x\ne0\). Thus the prescribed coproduct fails the exchange test for that independent tensor. The exchange constructed here is polynomial in separation and is determined by the ordered product and the current translation. A collision pole with Yang’s rational matrix would require a different field datum.

**Rational exchange on fundamental field modules**

The regular Yangian fields have an ordinary representation-theoretic test. Let \(M\) be a module over the coefficient ring, with lower-truncated unital fields \(Y_M(a,z)\) satisfying weak associativity and \(Y_M(Ta,z)=\partial_zY_M(a,z)\). Every such field module of the preceding algebra comes from a unital representation \(\pi\) of the chosen coefficient algebra \(H\), by
\[
 Y_M(a,z)=\pi(\sigma_z a).
\]
{#ch12-fundamental-field-modules}
Indeed \(T^da=0\) for some \(d\), so \(\partial_z^dY_M(a,z)=0\). Over a \(\mathbb C\)-algebra of coefficients each such Laurent series is a polynomial of degree less than \(d\). Evaluation at zero defines \(\pi(a)\), and translation gives the formula. Weak associativity of these polynomial fields, with both variables set to zero after clearing and cancelling the weak-associativity factor, gives \(\pi(ab)=\pi(a)\pi(b)\). Conversely the formula for any unital representation satisfies the field axioms and the prescribed exchange locality by applying \(\pi\) to the algebra identities. The joint coproduct gives the usual tensor product of representations. A map intertwines all their translated fields precisely when it intertwines the actions at zero.

For a concrete exchange let \(\pi_a\) be the fundamental evaluation at parameter \(a\) on the free rank-\(N\) module, so \(\pi_a(X^{(r)}_{ij})=h a^{r-1}E_{ij}\). It is the ordinary evaluation at zero composed with \(\sigma_a\), after scaling the zero mode by \(h\). Set \(\lambda=ht\), and let \(P\) exchange the two modules. For generic \(a,b\) the matrix
\[
 R(a-b)=\frac{(a-b)I+\lambda P}{a-b+\lambda}
\]
intertwines the ordered and opposite actions, before flipping the two modules. It therefore intertwines the full fields on their tensor product. To see this on every mode, write \(A=E_{ij}\otimes I\), \(B=I\otimes E_{ij}\), and \(d_r=(a^{r-1}-b^{r-1})/(a-b)\). The ordered action of \(X^{(r)}_{ij}\) is
\[
 h\bigl(a^{r-1}A+b^{r-1}B+\lambda d_r AP\bigr).
\]
The opposite action replaces \(AP\) by \(PA\). Since \(BP=PA\) and \(PB=AP\), multiplication on the left and right by the numerator of \(R(a-b)\) gives equal matrices. This is an identity of polynomials before scalar division. The normalization gives \(R(u)R(-u)=I\) as rational matrices. The rational Yang–Baxter equation follows from \(P_{ij}^2=I\), the permutation relations on three tensor factors and \(1/(uv)=1/(u(u+v))+1/(v(u+v))\). Products of fundamental exchanges hence intertwine blocks of evaluation modules wherever their denominators and inverses are defined.

On the symmetric subspace \(R(u)\) acts by \(1\), and on the alternating subspace by \((u-\lambda)/(u+\lambda)\). For \(\lambda\ne0\) and \(N\ge2\) the latter has a pole at \(u=-\lambda\). This is a pole in the difference of the two module evaluation parameters. The state field \(Y(a,z)b\) and its spectator exchange remain polynomial in the separation of insertion points.

### Two parameters in the rational Yangian fields {#ch12-two-parameter-yangian}

A level fixes the central term in an affine current collision. A second kind of parameter changes what happens when two charged currents change order. In rank three these effects can be measured separately. Write \(h\) for the rational Yangian parameter and work over \(\mathbb C[[h,\eta]]\), taking fields and tensor products modulo \((h,\eta)^d\) at each precision \(d\). The two Cartan charges are the eigenvalues of
\[
 H_1=E_{11}-E_{22},\qquad H_2=E_{22}-E_{33}.
\]
For charge vectors \(\alpha,\beta\), set \(B(\alpha,\beta)=\alpha_1\beta_2\). Let \(F\) multiply an ordered pair of states by \(\exp(\eta B(\alpha,\beta))\).

**Theorem (Cartan twist of the rational quantum affine fields).** Let \(V_K^h\) be the divided determinant-one quantum affine vacuum algebra at level \(K\). Its two-parameter fields, on the same topologically free state module after base change, are
\[
 Y^{h,\eta}(a,z)b=e^{-\eta B(|a|,|b|)}Y^h(a,z)b,\qquad
 \mathcal S^{h,\eta}(z)=F_{12}\mathcal S^h(z)F_{21}^{-1}.
\]
Here \(|a|\) denotes the Cartan charge of a homogeneous state. The second formula uses the locality convention in which \(\mathcal S\) acts on the inputs of the product in the order \(a,b\). On a word of \(n\) states the field acquires the factor \(\exp(-\eta\sum_{i<j}B(|a_i|,|a_j|))\). For three charges \(a,b,c\), multiplying the first pair first gives the exponent \(-\eta(B(a,b)+B(a+b,c))\). Multiplying the last pair first gives \(-\eta(B(b,c)+B(a,b+c))\), the same sum of three pairings. This proves the assertion for any consecutive block by iteration. In an exchange the ratio of the two factors for the two orders gives the displayed conjugations. The original substitutions, exchange hexagon and Yang–Baxter identity therefore hold after twisting. The factors are constant in the positions, so all residues including their normal derivatives have the original pole bounds at each precision. [Rational affine field comparison](#ch12-theorem-rational-affine-field-comparison)

The simple-root currents \(a=J_{12}\), \(b=J_{23}\) have charges \((2,-1)\), \((-1,2)\). At \(h=0\) the two ordered simple-pole coefficients are \(e^{-4\eta}J_{13}\) and \(-e^{-\eta}J_{13}\). Their signed ratio \(e^{-3\eta}\) survives separate rescalings of the three root currents. A coefficient of the exchange measures the interaction with \(h\). Before twisting, its first-order \(z^{-1}\) term on \(a\otimes b\) is
\[
 -\sum_{i,j}[E_{ij},a]\otimes[E_{ji},b]
 =H_1\otimes J_{13}-J_{13}\otimes H_2+a\otimes b .
\]
The component along \(H_1\otimes J_{13}\) in the residue of the twisted exchange is \(h e^{-\eta}+O(h^2)\), at every \(K\). Setting \(\eta=0\) recovers the rational quantum affine fields. Setting \(h=0\) retains the change of order of the affine fields. [Etingof–Kazhdan, §§1–3](https://arxiv.org/abs/math/9808121)

There is also a coproduct on the fields. Write \(D_{K,L}\) for the divided field coproduct from level \(K+L\) to the cross-contracted tensor of levels \(K,L\), and \(Y_{12}\) for the field on that tensor. The new coproduct is \(F D_{K,L}\). Its tensor target has field
\[
 (p,q)\longmapsto
 e^{-\eta B(|p|,|q|)}F\,Y_{12}(F^{-1}p,z)F^{-1}q .
\]
Substituting \(p=FDa\), \(q=FDb\) gives \(FD(Y^{h,\eta}(a,z)b)\). The two triple cuts both multiply \(D^{(3)}\) by the same three-pair factor, and the level-zero counit removes a neutral factor. The outgoing \(F\) is visible even at \(h=0\). The image of the normal product of \(J_{12}\) and \(J_{23}\) under the level coproduct has split component \(J_{12}\otimes J_{23}\) with coefficient \(e^{-4\eta}e^{4\eta}=1\). Leaving out the outgoing factor gives \(e^{-4\eta}\). On covariant coefficients with rational, finite-pole passes commuting with collision pullbacks, each pass is conjugated by its incoming and outgoing factors. This transports the braided diagonal tensor and its interchange on the consecutive-cut cobars.

The positive Yangian exhibits the same two parameters on a tensor product of evaluation modules. Use \(T_{ij}(p)=\delta_{ij}+h\sum_{r\ge1}t^{(r)}_{ij}p^{-r}\), \(\Delta T_{ij}=\sum_kT_{ik}\otimes T_{kj}\), and \(t^{(r)}_{ij}v=a^{r-1}E_{ij}v\) on \(V_a\). Its coproduct on \(V_a\otimes V_b\) becomes \(F\Delta F^{-1}\). In the action of \(t_{12}^{(2)}\), the coefficient from \(v_3\otimes v_2\) to \(v_1\otimes v_3\) is exactly \(h e^{-\eta}\). Only the term \(h E_{13}\otimes E_{32}\) contributes. The input pair has \(B=0\) and the output pair has \(B=-1\). The \(h\)-linear skew coproduct vanishes on all constant currents and contains \(E_{13}\wedge E_{32}\) on \(t_{12}^{(2)}\). The \(\eta\)-linear skew coproduct already sends \(E_{12}\) to \(E_{12}\wedge(H_1+2H_2)\). Their independence distinguishes the two marked deformations. The tensor identification \(F\) gives a monoidal equivalence of the positive Yangian module categories. Identifying these rational fields and their braided tensor with Zeng's chiral cotangent Yangian requires an isomorphism preserving the fields and the spectral cuts.

### A two-parameter coproduct for the cotangent currents {#ch12-coloured-cotangent}

In the level-zero cotangent vertex algebra for \(GL_N\), two currents can collide to give a third. A diagonal torus assigns a charge to each current and each loop coordinate. We can vary the strength of the current collision and, independently, the scalar acquired when two charges pass each other. Both variations affect the current coproduct.

Write \(T(u)=1+\sum_{r\ge1}t^{(r)}u^{-r}\) for the negative loop and \(L_\xi\) for the invariant current with polynomial label \(\xi\in\mathfrak{gl}_N[u]\). Give functions and their vertex derivatives order zero. Let \(P_d V\) consist of the PBW words in Zeng's vertex envelope \(V\) with at most \(d\) invariant current letters, counting a derivative of a current as one letter. In the Rees algebra \(V_h=\sum_{d\ge0}h^dP_d V\) write \(J_\xi=hL_\xi\). A PBW word with \(d\) current letters gives a basis element after multiplication by \(h^d\). In particular \(J_\xi\) has a nonzero symbol at \(h=0\) for \(\xi\ne0\). The current-current and current-function residues are \(hJ_{[\xi,\nu]}\) and \(h\rho_\xi f\), respectively, with \(\rho\) the dressing action above. The coproduct \(\Delta_h\) on a function is pullback by loop multiplication. Its formula on \(J_\xi\) has one current in each summand, so it preserves total PBW order. [Zeng, Theorems 2.6 and 5.5](https://arxiv.org/html/2610.10202v2)

Let \(\Lambda\) be the \(A_{N-1}\) root lattice and \(\epsilon_i\) the diagonal characters. Pullback of functions by \(g\mapsto t^{-1}gt\), together with \(J_\xi\mapsto J_{t\xi t^{-1}}\), makes all field products and the coproduct homogeneous. For example conjugating the negative loop by \(t^{-1}(-)t\) multiplies its \(ij\) coordinate by \(t_j/t_i\), while conjugating the current label \(E_{ij}\) by \(t(-)t^{-1}\) multiplies it by \(t_i/t_j\). Hence the two matrix frames have opposite index conventions,
\[
 |t^{(r)}_{ij}|=\epsilon_j-\epsilon_i,\qquad
 |J_{E_{ij}u^m}|=\epsilon_i-\epsilon_j .
\]
For an integral bilinear form \(B\) on \(\Lambda\) put \(F(a,b)=q^{B(a,b)}\) and \(\chi(a,b)=F(a,b)/F(b,a)\). The scalars are \(k[h,q^{\pm1}]\) over a characteristic-zero field. Writing \(q=e^\eta\) gives the formal expansion at \(q=1\). For homogeneous states and for every output bidegree put
\[
 Y^F(x,z)y=F(|x|,|y|)Y_h(x,z)y,\qquad
 (\Delta^F v)_{a,b}=F(a,b)^{-1}(\Delta_hv)_{a,b}.
\]
The vacuum has charge zero, and vertex translation preserves every charge. The counit evaluates functions at the identity loop and kills currents.

For \(N\ge3\) set \(\alpha=\epsilon_1-\epsilon_2\) and \(\beta=\epsilon_2-\epsilon_3\). Take \(B(a,b)=a_1b_2\) in simple-root coordinates. With \(J_{ij}=J_{E_{ij}}\), the two orders of the collision are
\[
 J_{12}(z)J_{23}(w)\sim\frac{h e^\eta J_{13}(w)}{z-w},
 \qquad
 J_{23}(z)J_{12}(w)\sim-\frac{h J_{13}(w)}{z-w}.
\]
The first residue has mixed coefficient \(J_{13}\) at order \(h\eta\) in the PBW basis. At \(\eta=0\) the Rees current residue survives. At \(h=0\) all fields are regular, while the normal products of independent coordinate functions of charges \(\alpha,\beta\) still differ by \(e^\eta\) in the two orders. The original vertex algebra is the specialization \(h=1,\ q=1\). The current-count parameter has a commutative PBW fibre at \(h=0,\ q=1\) whose coordinate coproduct still multiplies negative loops. Abedin and Niu's parameter deforms the enveloping Hopf algebra of a current Lie algebra. Zeng's dense Zhu comparison for a complex simple Lie algebra uses its graded evaluation at one. [Zeng, §5.5](https://arxiv.org/html/2610.10202v2#S5.SS5) · [Abedin and Niu, §3](https://arxiv.org/html/2405.19906v2#S3)

**Proposition.** The coloured fields \(W=V_h^F\) have a factorizing ordered bar \(C(W)\). Its cut cobar \(A(W)\) has a coassociative, counital coproduct for the same-position tensor with middle passage \(y_b\otimes v_c\mapsto\chi(b,c)v_c\otimes y_b\). For the stated rank-three charges, the ordinary diagonal tensor admits no coproduct on this word object inducing \(\Delta^F\) at a singleton.

*Proof.* On independent rows at the same position the field of \(x_a\otimes y_b\) on \(v_c\otimes w_d\) is
\[
 \chi(b,c)Y^F(x_a,z)v_c\otimes Y^F(y_b,z)w_d .
\]
The two Laurent series share \(z\). Preservation of all field products by \(\Delta^F\) follows from
\[
 \frac{F(a+b,c+d)}{F(a+c,b+d)}
   =\frac{\chi(b,c)F(a,c)F(b,d)}{F(a,b)F(c,d)}.
\]
Bilinearity proves the identity. The multiplier on an iterated coproduct is \(\prod_{i<j}F(a_i,a_j)^{-1}\) in any parenthesization. The weight-zero counit gives the two counit identities.

To see the map at a collision, take the partition coefficients of Chapter 5. Each block has one state and a position at its largest label. Its coefficient allows poles between distinct block positions and retains the normal derivatives on its partition diagonal. For a merger of the \(i\)th and \(j\)th blocks in root order, the multiplier of the full uncoloured principal part is
\[
 F(a_i,a_j)\prod_{i<k<j}\chi(a_i,a_k).
\]
Indeed \(a_i\) passes the intervening blocks before colliding with \(a_j\). If \(F_r=\prod_{i<j}F(a_i,a_j)\) on \(r\) blocks, this multiplier is \(F_r/F_{r-1}\) on the corresponding input and merged output. Thus \(F_r\) conjugates the signed residue differential to the local one. On a consecutive cut open all partitions joining the two sides disappear and the surviving complex is the external product of the two block complexes. With scalar empty coefficient this gives a strong cut coalgebra \(C(W)\). Connected cut duality identifies it with the bar of \(A(W)=\Omega_{\rm cut}C(W)\). [Ordered cuts and connected duality](05-bar-and-coherence.md#ch05-ordered-cuts-give-a-finite-geometric-bar-construction)

For two rows, sorting the interleaved block states of charges \((a_i,b_i)\) into row order contributes \(\Theta=\prod_{i<j}\chi(b_i,a_j)\). At a merger this scalar intertwines the full principal parts. Across a cut \(I|J\) it differs from the two within-block shuffles by \(\chi(\sum_{i\in I}b_i,\sum_{j\in J}a_j)\). Passing back from rows to cut blocks uses its inverse. The regular-lattice tensor comparison identifies the resulting coalgebra with the coefficientwise extraordinary tensor of the two bars carrying this corrected cut. Its hypotheses hold with the external group algebra \(k[h,q^{\pm1}][\Lambda]\), zero translation on that algebra, and constant unitary form \(\rho(e^a,e^b)=\chi(b,a)\). The grading gives a state of charge \(a\) the group-like tail \(e^a\). The external form gives the exchange of the fields \(Y^F\), with \(\chi(a,b)\chi(b,a)=1\). All passages preserve the complete pole coefficients and commute with collision pullback because charges add. The comparison multiplies scalar functions on regular sections after the shuffle. It is the identity on singleton states. Three rows give the same pairwise passes in either grouping, and passages across the scalar row are identities. Applying \(\Delta^F\) to each block and taking cut cobar therefore gives the asserted coproduct with target \(\Omega_{\rm cut}(C(W)\otimes^!_\chi C(W))\). Its counit takes values in the cobar of the dualizing family with occupied scalar vacuum. At \(q=1\) the partition complex is the Beilinson–Drinfeld chiral Chevalley complex of the local fields. Its \(r\)-fold symmetric chiral power has one summand for each partition into \(r\) blocks, with the root order fixing the suspension sign. Hence the regular-lattice comparison supplies the ordinary same-position tensor for the original cotangent word algebra as well. At general \(q\) the passage factors enter the residue complex itself. [The regular-section comparison for the braided tensor](#ref-ch12-cq2)

For the ordinary tensor take the primitive coordinate functions \(x=t^{(1)}_{21}\), \(y=t^{(1)}_{32}\) of charges \(\alpha,\beta\). Write \(x*y\) for their coloured normal product. The independent input
\[
 \frac{x\otimes y-\mathbf1\otimes(x*y)}{z_1-z_2}
\]
has regular field expansion, since the two evaluated terms have the same constant coefficient. On separated points a map of cut coalgebras must act by the tensor of its singleton maps. Under \(\Delta^F\) the ordinary target gives mixed placements \(x\otimes y+y\otimes x\) for the first term and \(x\otimes y+q\,y\otimes x\) for the second. The resulting principal part is \((1-q)y\otimes x/(z_1-z_2)\). This prevents the forced separated map from extending over the binary lattice, which embeds in its localization and represents the binary complex in a single degree. The middle passage above cancels this pole. □

The one-form in the coordinate current detects the same two parameters with the opposite colour exponent. In the original linear frame set \(K^{h,(r)}_{ij}=hK_{E_{ji}u^{r-1}}\), of charge \(\epsilon_j-\epsilon_i\). Apply \(F(a,b)^{-1}\) to each output bidegree in the uncoloured cut of \(K^h\), including its one-form term. In the \((1,3)\) entry of (12.5), the term \(NX_{12}\otimes DY_{23}\) has charges \(-\alpha,-\beta\), so its coefficient becomes \(Nh e^{-\eta}\). On the spectral translates \(S_sT(u)=T(u+s)\) and \(S_sK^h(u)=K^h(u+s)\), while \(S_sJ_\xi=J_{\xi(u-s)}\). These substitutions preserve the charges and commute with the vertex derivative \(D\).

For a symmetric integral addition \(S\) to \(B\), a change of frame over \(k[h,q^{\pm1}]\) acts on charge \(a=\sum_i m_i\alpha_i\) by \(q^{Q(a)}\), where
\[
 Q(a)=\sum_i S(\alpha_i,\alpha_i)\frac{m_i(m_i-1)}2
       +\sum_{i<j} S(\alpha_i,\alpha_j)m_i m_j .
\]
Indeed \(Q(a+b)-Q(a)-Q(b)=S(a,b)\). Writing \(T|_a=q^{Q(a)}\), this gives \(T Y^B(x,z)y=Y^{B+S}(Tx,z)Ty\) and \(\Delta^{B+S}T=(T\otimes T)\Delta^B\). On output bidegree \((a,b)\) the change in the coproduct multiplier is \(q^{-S(a,b)}\). In the formal coordinate \(q=e^\eta\) one can also use \(\exp(\eta S(a,a)/2)\). On a simple root of odd self-pairing the latter expression requires a square root of \(q\) over the Laurent polynomial ring. The exchange ratio \(\chi\) survives this rescaling. If the tensor identification itself may vary, the identity functor with tensorator \(F\) carries the original graded fields, coproduct and cut coherences to the coloured family. The crossing is constant in the separation. Intertwining the two oppositely ordered loop products by Abedin and Niu's meromorphic spectral operator remains a separate condition.

## Nonlinear fields: the \(W_3\) example {#ch12-nonlinear-fields-the-w3-example}

The field hexagon compares two ways of moving a third field past a product. To use it we must already know what the product returns. Integrate \(J(z)J(w)\) against \((z-w)\,dz/(2\pi i)\) about \(w\) for a Heisenberg current. The double pole gives the scalar \(\kappa\mathbf1\). The same contour applied to two spin-three fields can return two stress tensors at the same point. Where do those fields come from, and how can one tell a two-field state from a derivative of a single field?

Start with a trace-zero complex matrix \(M\). The trace pairing identifies \(\mathfrak{sl}_3^*\) with \(\mathfrak{sl}_3\). Under this identification the coadjoint action is conjugation: \(\operatorname{tr}(M g^{-1}Ag)=\operatorname{tr}(gMg^{-1}A)\). For the observable \(\ell_A(M)=\operatorname{tr}(MA)\), the Lie–Poisson bracket is \(\{\ell_A,\ell_B\}=\ell_{[A,B]}\). In particular the bracket of \(M_{21}\) and \(M_{32}\) is \(M_{31}\), since their labels are \(E_{12}\) and \(E_{23}\). Here \(E_{ij}\) sends basis vector \(j\) to basis vector \(i\). Fix the three values \(M_{21}=M_{32}=1,\ M_{31}=0\). These are the restrictions of the linear observables to \(f=E_{21}+E_{32}\), a single nilpotent Jordan block. The constraints generate upper unitriangular changes of basis and are compatible because their bracket vanishes on the constraint surface.

**Example (a principal nilpotent slice).** Let \(n\) be an upper unitriangular matrix and put \(r=n_{12}\), \(s=n_{23}\). If the constrained matrix \(M\) has diagonal \((d_1,d_2,d_3)\), its conjugate \(M'=nMn^{-1}\) has diagonal \((d_1+r,d_2-r+s,d_3-s)\). Taking \(r=-d_1\) and \(s=d_3\) makes the first and last entries zero. The middle entry then vanishes because \(M\) has trace zero. Write \(x=M'_{12}\) and \(y=M'_{23}\). Conjugating \(M'\) by \(1+hE_{13}\) preserves the zero diagonal and changes these two entries to \(x+h\) and \(y-h\). They agree precisely for \(h=(y-x)/2\). Apply these two conjugations to the following matrix \(M\).
\[
 M=\begin{pmatrix}1&2&3\\1&0&4\\0&1&-1\end{pmatrix},\qquad
 n=\begin{pmatrix}1&-1&3/2\\0&1&-1\\0&0&1\end{pmatrix}
\]
First take \(n_0=I-E_{12}-E_{23}\). The matrix \(n_0Mn_0^{-1}\) has \(x=2\), \(y=5\) and upper-right entry \(1\). This gives \(h=3/2\) and the displayed \(n=(1+hE_{13})n_0\). Thus \(nMn^{-1}=S(7/2,1)\), where
\[
 S(u,v)=\begin{pmatrix}0&u&v\\1&0&u\\0&1&0\end{pmatrix},
 \qquad \det(\xi I-S)=\xi^3-2u\xi-v .
\]
The characteristic polynomial recovers the quotient coordinates on the original matrix as \(u=\operatorname{tr}(M^2)/4,\ v=\operatorname{tr}(M^3)/3\). Both are conjugation invariants, so their finite Poisson brackets with every linear observable vanish. When \(32u^3-27v^2\ne0\), the three eigenvalues are distinct. On the discriminant at least two eigenvalues coincide. The representative is still regular because \(e_1,S e_1,S^2 e_1\) are a basis even there. At \(u=v=0\) the representative is the principal nilpotent \(f\). The other nilpotent orbits in the ambient zero fibre do not meet this slice.

This plane is the principal Slodowy slice \(f+\ker(\operatorname{ad}e)\), where \(e=2(E_{12}+E_{23})\) and \([e,f]=\operatorname{diag}(2,0,-2)\). The traceless matrices commuting with \(e\) are spanned by \(e,e^2\), the two directions of the plane. Tangents to the coadjoint orbit at \(f\) are the commutators \([A,f]\). The differentials \(du_f(V)=\operatorname{tr}(fV)/2\) and \(dv_f(V)=\operatorname{tr}(f^2V)\) vanish on them. On \(E_{12}+E_{23},E_{13}\) their two columns are \((1,0),(0,1)\). Since the centralizer of the single Jordan block \(f\) in \(\mathfrak{sl}_3\) has dimension two, the orbit has dimension six. These two directions therefore give a transverse plane in dimension eight. Conjugating by \(\operatorname{diag}(t,1,t^{-1})\) and multiplying by \(t\) fixes \(f\) and sends \((u,v)\) to \((t^2u,t^3v)\). The finite calculation accounts for the degrees two and three. The singular products require fields on a disk. [Arakawa, §§2.2–2.8](https://arxiv.org/pdf/1605.00138#page=5)

At affine level \(k\) take the universal currents with brackets \([J^A_\lambda J^B]=J^{[A,B]}+k\lambda\operatorname{tr}(AB)\mathbf1\). Here \([a_\lambda b]=\sum_{j\ge0}\lambda^j a_{(j)}b/j!\) packages the singular part of a product, with \(a_{(j)}b\) the coefficient of \((z-w)^{-j-1}\). A varying change of basis acts through both poles of the affine bracket.

For two fields \(a,b\), the normal product \(:ab:=a_{(-1)}b\) is the constant coefficient of \(Y(a,z)b\). At coincidence it is what remains after subtracting all poles and taking the regular value. A product of a ghost with a constraint below is taken in precisely this sense.

To impose the constraints as field equations, label the three currents for \(E_{12},E_{23},E_{13}\) by \(J_1,J_2,J_3\). Introduce odd fields \(b_i,\gamma^i\) of cohomological degrees \(-1,1\) with \(b_i(z)\gamma^j(w)\sim\delta_i^j/(z-w)\). Like fields have regular products. The principal Drinfeld–Sokolov differential \(Q\) is the residue of
\[
 :\gamma^1(J_1-\mathbf1):+:\gamma^2(J_2-\mathbf1):
 +:\gamma^3J_3:-:\gamma^1\gamma^2 b_3: .
\]
The antighost \(b_3\) has \(Qb_3=J_3\). On \(\gamma^3\) the last term gives \(-:\gamma^1\gamma^2:\), canceling the commutator of the first two constraint currents in \(Q^2\). For example \(Qb_1=J_1-\mathbf1-:\gamma^2b_3:\) and \(QJ_1=-:\gamma^2J_3:\). The odd Leibniz rule gives the opposite term from \(Q(-:\gamma^2b_3:)\), so \(Q^2b_1=0\). The central pairing vanishes on the strictly upper triangular Lie algebra. This gives the Becchi–Rouet–Stora–Tyutin (BRST) complex. Its degree-zero cohomology, the closed degree-zero fields modulo the images of fields of degree minus one, is the universal principal \(W^k(\mathfrak{sl}_3)\).

In the associated graded complex for the Li filtration, which counts derivatives, one first imposes the three constraints and all their derivatives. The undifferentiated constraints and their jets are independent coordinate equations, so their Koszul complex has cohomology only in degree zero. The remaining ghost differential takes invariants under the jets of the upper unitriangular group. The gauge calculation above works coefficient by coefficient in a formal power series, splitting the constraint space of jets into a group factor and a slice factor. The group cochain calculation removes the first factor and has no higher cohomology here. This computes \(H^0(\operatorname{gr}C)=\mathbb C[J_\infty S]\), the differential polynomial algebra of the jets of \(u,v\), with cohomology zero in every other degree. Here \(C\) is the BRST complex and \(J_\infty S\) denotes formal arcs in the slice.

To identify \(\operatorname{gr}H^0(C)\), use the smaller BRST complex obtained by removing its acyclic factor. Its modified conformal-weight spaces are finite dimensional, so the filtered calculation converges on each of them. It gives \(\mathbb C[J_\infty S]\) for the filtration induced on cohomology. The comparison from the Li filtration surjects onto the undifferentiated slice coordinates and hence onto all their derivatives. Equality of the graded characters makes it an isomorphism. The two coordinates therefore lift to fields whose derivatives and ordered products span the universal vacuum. Their singular contractions still have to be computed. [Arakawa, Theorem 5.7](https://arxiv.org/pdf/1605.00138#page=31) · [Theorem 5.8](https://arxiv.org/pdf/1605.00138#page=32) · [Filtered comparison, §5.6](https://arxiv.org/pdf/1605.00138#page=35)

For \(k\ne-3\) the quantum Miura map gives explicit representatives. Choose a square root of \(k+3\), put \(\alpha=(k+2)/\sqrt{k+3}\), and take traceless Heisenberg currents \(H_1+H_2+H_3=0\) with contraction \((\delta_{ij}-1/3)/(z-w)^2\). Write \(T\) for the derivative in the insertion coordinate. In the ordered normally ordered product below, move the formal symbol \(D\) to the right with \(DH_i=H_iD+\alpha TH_i\). Keeping \(D\) as a symbol defines the coefficients even at \(\alpha=0\). They satisfy
\[
 :(D+H_1)(D+H_2)(D+H_3):=D^3+B_2D+B_3 .
\]
The quadratic coefficient is \(\sum_{i<j}:H_iH_j:+\alpha T(H_2+2H_3)\). The cubic coefficient is
\[
 B_3=:H_1H_2H_3:
 +\alpha\bigl(:(H_1+H_2)TH_3:+:(TH_2)H_3:\bigr)
 +\alpha^2T^2H_3 .
\]
The two coefficients generate the image of the injective Miura map. The stress tensor is \(L=-B_2\). Improving the cubic by a derivative gives \(X=B_3+\alpha TL/2\), primary of weight three, meaning that the only poles of \(L(z)X(w)\) have coefficients \(3X\) and \(TX\) at orders two and one. The fourth pole of \(L(z)L(w)\) gives \(c/2\), with \(c=2-24\alpha^2\). [Arakawa, Theorem 5.17](https://arxiv.org/pdf/1605.00138#page=38) · [Corollary 5.20](https://arxiv.org/pdf/1605.00138#page=39)

At \(k=-2\) the improvements vanish and \(X=:H_1H_2H_3:\). To find the sixth pole of \(X(z)X(w)\), contract all three currents across the two insertion points. A diagonal contraction gives \(2/3\), an off-diagonal contraction \(-1/3\). In units of \(1/27\) the identity permutation gives \(8\), each transposition \(2\), and each three-cycle \(-1\). There are three transpositions and two three-cycles, so the coefficient is
\[
 \frac{8+3\cdot 2-2}{27}=\frac49 .
\]
Here \(c=2\), so \(W=\sqrt{3/2}\,X\) gives sixth pole \(c/3=2/3\). In general the sixth and fourth poles of \(X(z)X(w)\) have coefficients \(c(22+5c)\mathbf1/144\) and \((22+5c)L/24\). For \(22+5c\ne0\) the conventional field \(W=\sqrt{48/(22+5c)}\,X\) therefore has fourth pole \(2L\). This condition fixes its squared scale even at \(c=0\), where the sixth pole vanishes. The stress field survives there in the universal vacuum. At the critical affine level \(k=-3\) the normalized Heisenberg currents and this conformal-vector formula are unavailable.

With the conventional field \(W\) and \(22+5c\ne0\), set
\[
\beta=\frac{16}{22+5c},\qquad
\Lambda=:LL:-\frac3{10}T^2L.
\]
The stress field \(L\) and spin-three field \(W\) obey
\[
\begin{aligned}
{}[L_\lambda L]&=(T+2\lambda)L+\frac c{12}\lambda^3\mathbf1,\\
[L_\lambda W]&=(T+3\lambda)W,\\
[W_\lambda W]&=\frac c{360}\lambda^5\mathbf1
 +\frac13\lambda^3L+\frac12\lambda^2TL\\
&\quad+\lambda\left(2\beta\Lambda+\frac3{10}T^2L\right)
 +\beta T\Lambda+\frac1{15}T^3L.
\end{aligned}
\]
The contour weighted by \(z-w\) returns \(2\beta\Lambda+3T^2L/10\). At \(k=-2\) one has \(\beta=1/2\), so the two derivative terms cancel and the whole double pole is \(:LL:\). A hexagon for an exchange on these fields would have to transport this two-stress-tensor output. Existence of such an exchange for \(W_3\) does not follow from the spectral Hopf construction. [De Sole and Kac, Example 3.13](https://arxiv.org/pdf/math-ph/0312042#page=10)

Transpose the relations on the two even fields, including their singular terms. The dual fields \(\tau,\varpi\), paired with \(L,W\) respectively, are odd. Their singular product includes
\[
[\tau_\lambda\tau]=2\beta\varpi T\varpi,
\]
and \(\varpi\) has zero singular products with every field. Although square-free ordered jet monomials give a basis, the normal product is not exterior multiplication. For example, quasi-commutativity gives
\[
\frac{\tau T\tau-(T\tau)\tau}{2}
=\tau T\tau-\frac\beta2T^2(\varpi T\varpi).
\]
This derivative correction is part of transposing the quadratic source relation. It disappears if one replaces the dual fields by regular exterior ghosts. [CQ6](#ref-ch12-cq6)

More generally, for a universal vertex algebra over a characteristic-zero field, freely generated by finitely many even fields of half-integer weights at least one, homogeneous quadratic–linear–scalar brackets admit a derivative-corrected transpose. Its odd envelope has an ordered jet basis, a degree-one derivation \(d\), and curvature \(w\) of degree two satisfying
\[
d^2=w_{(0)},\qquad dw\in TB.
\]
The construction supplies a finite translation primitive for \(dw\). To test a proposed map of fields into an ordinary vertex algebra \(V\), choose an image \(y_i\in V\) for each source generator \(x_i\). Pair these images with the corresponding odd generators \(c_i\) of \(B\), giving the degree-one state \(q=\sum_i y_i\otimes c_i\). The images extend to a vertex-algebra map precisely when
\[
 (1\otimes d)q+\tfrac12 q_{(0)}q+\mathbf1\otimes w
 \ \in\ T(V\otimes B).
\]
Here \(T\) translates both factors. The zero mode of a total derivative vanishes, so the condition makes \(1\otimes d+q_{(0)}\) square to zero. The correspondence uses couplings linear in the specified \(c_i\) and tests the singular products, normal products, translation and vacuum of the source. [CQ6](#ref-ch12-cq6)

The same nonlinear term can be tested at the exceptional charge. Put \(a=(22+5c)/16\) and choose the regular field \(U=\sqrt3\,X\). Away from \(a=0\), \(U=\sqrt a\,W\) with compatible signs. Multiplying the \(WW\) bracket by \(a\) gives polynomial coefficients because \(a\beta=1\). Specializing these coefficients at \(c=-22/5\), corresponding to \(k=-4/3\) or \(-12/5\), leaves double and simple poles \(2\Lambda\) and \(T\Lambda\). The regular universal vacuum has the independent generator \(U\) also in this fibre. Relations in a simple quotient require a separate calculation. [Al-Ali and Linshaw, equations (3.3)–(3.5)](https://arxiv.org/pdf/1608.06255#page=4)

Write \(U(z)=\sum_m U_m z^{-m-3}\) and \(L(z)=\sum_m L_m z^{-m-2}\). Since \(U_{-1}\mathbf1=0\), the commutator with \(U_{-3}\) on the vacuum takes the double pole of \(U\) acting on its own state. The states of \(:LL:\) and \(T^2L\) are \(L_{-2}^2\mathbf1\) and \(2L_{-4}\mathbf1\), respectively. Hence

\[
[U_{-1},U_{-3}]\mathbf1
=2L_{-2}^2\mathbf1+\tfrac35(a-2)L_{-4}\mathbf1 .
\]

For \(c=2\) the derivative state disappears and the commutator is \(2L_{-2}^2\mathbf1\). At \(c=-22/5\) its coefficients on \(L_{-2}^2\mathbf1,L_{-4}\mathbf1\) are \(2,-6/5\). Ordered creation words are independent in the universal vacuum at either charge. At weight four a single original mode can create \(L_{-4}\mathbf1\) or \(U_{-4}\mathbf1\). Their span misses the two-mode word. A linear coupling to freely exterior scalar ghosts on the original modes would require just such a linear closure. To retain the quadratic operation on modules we use the regular algebra and its curved bar construction. [CQ7](#ref-ch12-cq7)

A module is smooth when sufficiently high modes kill each vector, with a bound allowed to depend on that vector. In the complete mode algebra \(A_c\), a basic neighborhood of zero consists of the operators killing a specified finite tuple of such vectors. This is the vector-annihilator topology. For a mode operator \(a\), let \(e(a)\) be the coefficient of the vacuum vector in \(a\mathbf1\). This continuous linear functional retracts the scalar unit of \(A_c\). Multiplication can produce a vacuum coefficient from two operators in its kernel. Put \(E=\ker e\) and define the bilinear maps
\[
\begin{aligned}
\mu:E\otimes E&\longrightarrow E,&\mu(a,b)&=ab-e(ab)1,\\
h:E\otimes E&\longrightarrow\mathbb C,&h(a,b)&=e(ab).
\end{aligned}
\]
For \(x,y,z\in E\), associativity of \(A_c\) yields
\[
\mu(\mu(x,y),z)-\mu(x,\mu(y,z))
=e(yz)x-e(xy)z.
\]
Thus the failure of the projected product to be associative is exactly the scalar term that becomes curvature.

The completed bar dual has
\[
B_c^n=\operatorname{Hom}_{\mathbb C}(E^{\otimes n},\mathbb C),
\]
with algebraic input tensors and graded-opposite concatenation. On a linear form \(\xi\in B_c^1\), the bar differential is \((d\xi)(x,y)=-\xi(\mu(x,y))\). Applying \(d\) again gives the associator just displayed, evaluated by \(\xi\). With graded-opposite concatenation, the full identity is \(d^2=[h,-]\) and \(dh=0\). To specify its infinite summations, set \(\widehat B_c=\prod_{n\ge0}B_c^n\). For finite-dimensional \(H\subset E\) and \(N\ge0\), let \(J_{H,N}\) be the ideal of forms vanishing on \(\bigoplus_{n=0}^N H^{\otimes n}\). These ideals define the finite-dual topology. For example, take one multilinear form of each arity. On words of length at most \(N\) from \(H\), only the first \(N+1\) forms, including the scalar, can contribute to their sum. The inverse limit over \(H,N\) retains all such finite evaluations. For coefficients in a graded vector space \(M\), total degree \(r\) pairs arity \(n\) with degree \(r-n\) in \(M\). This gives the free contramodule monad
\[
\begin{aligned}
\mathbb T_{B_c}(M)^r=B_c[[M]]^r
&=\varprojlim_{H,N}
\bigl((\widehat B_c/J_{H,N})\otimes M\bigr)^r\\
&=\prod_{n\ge0}\operatorname{Hom}_{\mathbb C}
\bigl(E^{\otimes n},M^{r-n}\bigr).
\end{aligned}
\]
At each finite quotient, the total degree uses ordinary direct sums. Equivalently, a coefficient family \((b_i)\) is summable when only finitely many \(b_i\) are nonzero modulo each \(J_{H,N}\). The monad unit \(\eta\) inserts coefficient \(1\); its multiplication \(m\) opens a summable sum of summable sums, using the product of \(\widehat B_c\).

**Definition (graded contramodule).** A graded contramodule is a graded vector space \(Q\) with a degree-zero contraaction \(\gamma:\mathbb T_{B_c}(Q)\to Q\) satisfying
\[
\gamma\eta_Q=1_Q,\qquad
\gamma\mathbb T_{B_c}(\gamma)=\gamma m_Q.
\]
Thus \(\gamma\) evaluates the permitted infinite sums. A **curved differential graded contramodule** additionally has a degree-one connection \(D_Q\) satisfying the Leibniz rule for all these sums and
\[
D_Q(bq)=d(b)q+(-1)^{|b|}bD_Q(q),\qquad D_Q^2(q)=hq.
\]
These objects and their graded contramodule maps form the differential graded category \(\operatorname{CDGContra}(B_c)\), with differential \(f\mapsto D_{Q'}f-(-1)^{|f|}fD_Q\) on maps \(Q\to Q'\). An arbitrary \(Q\) is not assigned a topology: its summations are the contraaction, whereas the specified free objects have the displayed inverse-limit topology.

At fixed central charge \(c\), let \(\mathcal S_c\) denote the category of smooth modules. Given a complex \(M\) of such modules, \(K_cM\) is the free graded contramodule \(B_c[[M]]\) with its twisting connection. In the other direction the smooth coinduction \(F_cQ\) consists of the continuous linear maps from \(A_c\) to the graded pieces of \(Q\) taken as discrete spaces, with the opposite twisting term in the differential. The resulting functors are adjoint as differential graded functors
\[
K_c:\operatorname{Ch}(\mathcal S_c)
\rightleftarrows
\operatorname{CDGContra}(B_c):F_c .
\]
The free-on-degree-zero objects with smooth recovered action characterize \(\mathcal S_c\) exactly. For smooth \(M,N\), the bar complex with the specified continuity in successive inputs computes \(\mathbf R\!\operatorname{Hom}_{\mathcal S_c}(M,N)\). Its composition induces the Yoneda product
\[
\operatorname{Ext}_{\mathcal S_c}^{r}(N,P)\otimes
 \operatorname{Ext}_{\mathcal S_c}^{s}(M,N)
\longrightarrow \operatorname{Ext}_{\mathcal S_c}^{r+s}(M,P)
\]
for smooth \(P\). [CQ7](#ref-ch12-cq7)

For a curved object \(Q\), the counit \(K_cF_cQ\to Q\) evaluates a free generator \(1\otimes\phi\) at \(1\in A_c\). This tests what smooth coinduction recovers from one such object. At every finite central charge there exists a nonzero graded-free curved object \(Q\) with contractible smooth coinduction \(F_cQ\). The cone of its counit \(K_cF_cQ\to Q\) is isomorphic to \(Q\) in the homotopy category. It survives the quotient by the smallest product-closed thick subcategory containing the totalizations of componentwise exact short triples. This rules out an equivalence on that full unpolarized quotient. A polarization or a different null class must give an invertible unit and counit and preserve the mixed curvature. [The counit obstruction in §18.2](#problem-chiral-quantum-groups)

## Exceptional \(W_4\) fibres and the algebra of extensions {#ch12-exceptional-w4-fibres-and-the-algebra-of-extensions}

In the principal reduction of \(\mathfrak{sl}_3\) the regular field \(U\) survived at \(22+5c=0\). A different specialization question arises if we first resolve a vacuum as a module over its fields. For the principal reduction of \(\mathfrak{sl}_4\), the Miura algebra \(W_4\) has three generating fields of weights two, three and four. Their sixteen quadratic–linear–scalar relations, with the vacuum included, admit the inverse-transpose curved construction. A polynomial form over \(\mathbb C[a]\) preserves the fields, modes and translation under every scalar extension, including nonflat extensions. This makes specialization a legitimate operation on that field construction. [CQ6](#ref-ch12-cq6)

To see what changes in a fibre, take the universal principal algebra \(W^k(\mathfrak g)\) and regard its vacuum as a module over itself. Compute self-extensions in all weak, equivalently smooth, modules. Composition here is the Yoneda product, given by splicing extensions. The differential of a resolution can lose rank at a special level even when the fields themselves specialize. At every noncritical level, a nonlinear resolution reduces vacuum self-Ext to a finite weight-zero complex with polynomial parameter differential. Generically its algebra is
\[
\operatorname{Ext}^\bullet(W^k,W^k)
\cong\Lambda(\eta_{2m_1+1},\ldots,\eta_{2m_r+1}),
\]
where \(m_i\) are the exponents of \(\mathfrak g\); it is associative \(A_\infty\)-formal. For \(\mathfrak{sl}_2,\mathfrak{sl}_3,\mathfrak{so}_5\), this exterior algebra and formality hold at every noncritical level. The canonical Drinfeld–Sokolov reduction map has its own exceptional kernels and need not be an isomorphism just because the target ring is exterior. [CQ8](#ref-ch12-cq8)

For \(\mathfrak g=\mathfrak{sl}_4\), write \(\tau=k+4\). At
\[
\tau=\frac32,-\frac32,\frac23,-\frac23,
\]
the dimensions in degrees zero through fifteen are
\[
(1,0,0,1,0,1,0,1,2,1,1,1,2,0,0,1),
\]
and all higher groups vanish. The total dimension is twelve, whereas the generic exterior algebra on degrees \(3,5,7\) has dimension eight. The primitive products satisfy
\[
\eta_3\eta_5\ne0,\qquad
\eta_3\eta_7\ne0,\qquad
\eta_5\eta_7=0.
\]
Exactly two local torsion pairs, in degrees \((8,9)\) and \((11,12)\), account for the excess. To see what specialization detects, consider a two-term summand \(R\xrightarrow{\,t^\ell\,}R\) over a local parameter ring, with \(\ell\ge1\). Its differential is invertible after \(t\) is inverted and zero after \(t=0\). All positive \(\ell\) give the same two special-fibre dimensions. Lifting the lower generator, applying the differential, dividing by \(t\) and reducing again gives a nonzero map precisely for \(\ell=1\). This is the first Bockstein on that summand. In the local parameter \(t=\tau-\tau_0\), write the finite zero-weight differential as \(A+tB+O(t^2)\). On a class killed by \(A\), reduction of \(B\) modulo the image of \(A\) is the first Bockstein. In each of the two degrees its rank is one at both \(\tau_0=3/2\) and \(-3/2\). Indeed null vectors on opposite sides of the constant matrix have nonzero pairing through \(B\), detected modulo \(1000003\) on maximal-rank minors. A single nonunit elementary divisor occurs in each degree, so it has valuation one. The reciprocal parameter change takes a uniformizer to a unit times a uniformizer. Thus both torsion summands are \(R/(t)\) at each of the four points, for \(R=\mathbb C[\tau]_{(\tau-\tau_0)}\). [CQ8](#ref-ch12-cq8), [CQ12](#ref-ch12-cq12)

How many other levels could have extra extensions? A noncritical jump in type \(A_3\) requires \(k\lambda\) to lie in the root lattice for some nonzero dominant coroot-lattice element \(\lambda\le2\rho^\vee\), with roots and coroots identified. Here \(2\rho^\vee\) is the sum of the positive coroots. Its two end coefficients in the simple-coroot basis are three, so the corresponding coefficients of \(\lambda\) are positive integers at most three. The reduced denominator of \(\tau=k+4\) is therefore at most three. Reciprocal duality gives the same bound for the absolute numerator. This leaves fourteen signed reduced fractions. At \(\tau=\pm1\) the dimensions through degree five are \(1,0,0,1,0,1\). Both the generic algebra and the twelve-dimensional fibres above have this initial sequence, although they differ in degree eight. At \(\tau=\pm2,\pm1/2\) the dimensions agree with the generic ones through degree four. At \(\tau=\pm3,\pm1/3\) the generic dimensions supply lower bounds. Whether any of these ten fibres has a dimension jump, and whether its derived endomorphisms have the formal exterior model, remain open. [CQ8](#ref-ch12-cq8)

To compute composition at \(\tau_0\in\{\pm3/2,\pm2/3\}\), let \(K_R^\bullet\) be the weight-zero complex of the universal principal vacuum coupled to the three ghosts of spins \(2,3,4\). Specialize its differential before taking cohomology, and write \(K^\bullet_{\tau_0}=K_R^\bullet\otimes_R R/(t)\). For \(V=W^{\tau_0-4}(\mathfrak{sl}_4)\) and its category \(\mathcal S_{\tau_0}\) of smooth weak modules, the vacuum resolution gives
\[
H^\bullet_{\tau_0}
=H^\bullet(K^\bullet_{\tau_0})
\simeq \operatorname{Ext}^\bullet_{\mathcal S_{\tau_0}}(V,V).
\]
Write \(a_3=\eta_3\). Multiplication by \(a_3\) pairs six generators in degrees \(0,5,7,8,9,12\) with six classes three degrees higher. The Yoneda algebra is free on these generators as a graded module over \(\Lambda(a_3)\). Let \(Q\) be the specialized coupled differential. For a closed field \(a\), the supercommutator \([Q,a_{(-1)}]=(Qa)_{(-1)}=0\) makes \(a_{(-1)}\) an operation on every coefficient module. It commutes with connecting maps up to the graded sign, so evaluation on the vacuum and dimension shifting identify it with Yoneda multiplication. Only the \((-1)\)-mode survives in weight-zero cohomology, where the product is graded commutative.

Write \(u\) for the degree-eight generator independent of \(a_3\eta_5\). The product \(\eta_7u\) would land in degree fifteen, a one-dimensional space, so dimensions alone allow a nonzero product. At \(\tau_0=3/2\) it vanishes. To compute it, assign a ghost word its total spin, the sum of the spins of its letters. There are rational cocycles \(C\in K^7_{\tau_0}\) and \(U\in K^8_{\tau_0}\) with all terms of spin at least \(23\) and \(27\), respectively. Pairing with a functional that annihilates boundaries shows that \([C]\) spans \(H^7_{\tau_0}\). The first Bockstein of \([U]\) is nonzero, whereas the degree-eight kernel of this Bockstein is \(\mathbb C\,\eta_3\eta_5\). Thus \([U]\) has a nonzero component along \(u\).

The ordinary ghost product preserves total spin, and every singular reordering term raises it. Consequently every term of \(C_{(-1)}U\) would have spin at least \(50\). The largest ghost spin in the entire weight-zero, degree-fifteen complex is \(49\), so \(C_{(-1)}U=0\) as a rational cochain. Since \(\eta_7(\eta_3\eta_5)=0\), this gives \(\eta_7u=0\) in the chosen generators. For other cochain representatives their product can be a nonzero boundary. The reciprocal isomorphism \(\tau\mapsto1/\tau\) and the complementary duality \(\tau\mapsto-\tau\), which reverses composition, carry this product calculation from \(3/2\) to \(-3/2,\,2/3,\,-2/3\). At \(\tau_0=\pm3/2\) the three primitive generators can be chosen as images of the affine classes under Drinfeld–Sokolov reduction. At \(\tau_0=\pm2/3\) their names refer to the transported classes. At each of these four levels the graded Yoneda algebra is
\[
H^\bullet_{\tau_0}\cong\Lambda(a_3)\otimes(\mathbb C\oplus I),
\qquad I=\operatorname{span}_{\mathbb C}\{\eta_5,\eta_7,u,v,z\},
\qquad I^2=0,
\]
where \(|u|=8,\ |v|=9,\ |z|=12\) and \(a_3z\) spans degree fifteen. [CQ12](#ref-ch12-cq12)

The Yoneda algebra describes binary composition. Associative formality also requires eliminating the higher multiplications on cohomology by a quasi-isomorphism. The transferred ternary operation \(m_3(a_3,a_3,a_3)\) vanishes when the same primitive of \(a_3^2\) is used for both adjacent pairs. Allowing two independent choices gives the ordinary triple Massey indeterminacy \(\mathbb C\,a_3\eta_5\). At the shifted level \(\tau_0=-3/2\), the pinned \(A_3\) diagram involution acts on the actual smooth vacuum and its enhanced affine reduction. It preserves the Whittaker character and the coweight \(2\theta^\vee\). Pullback commutes with the convolution defining the orbit coefficient, and the support morphism is equivariant by naturality. The two surviving orbit rows carry the same negative character after integration. In eigenvector coordinates the signs on \((a_3,\eta_5,\eta_7,u,v,z)\) are consequently \((+,-,+,-,-,-)\). The deformation parameter is fixed.

In characteristic zero one can average a contraction over this involution. In the resulting minimal \(A_\infty\) algebra all candidate ternary operations have negative character and hence vanish. Compatibility with the marked affine map reduces the quartic operation, up to a change of coordinates with identity linear part, to one possible entry in suspended notation,
\[
b_4(sa_3,sa_3,sa_3,su)=\gamma\,s(a_3z),
\]
where \(s\) lowers degree by one. Before this choice of coordinates, \(\gamma\) is the sum of the four \(s(a_3z)\)-coefficients obtained by placing \(su\) in each position among three copies of \(sa_3\). The first Bocksteins alone allow every value of \(\gamma\). An auxiliary flat, strictly unital \(A_\infty\) family over \(\mathbb C[[t]]\) has \(bc=t z,\ du=t v,\ d(au)=-t av\), where \(a=\eta_3,\ b=\eta_5,\ c=\eta_7\). Those equations give the same special binary algebra and both simple Bocksteins for arbitrary \(\gamma\).

**Theorem (formality of the exceptional \(W_4\) vacuum).** For the universal principal \(\mathfrak{sl}_4\) vacuum in all smooth weak modules at \(\tau_0=-3/2\), the quartic coefficient \(\gamma\) vanishes. Its derived endomorphism algebra is formal as an associative dg algebra. The reciprocal equivalence and complementary duality give the same formality at \(\tau_0=3/2,\,2/3,\,-2/3\).

The remaining coefficient has a Lie-theoretic test. Antisymmetrization puts it in a four-input bracket, while the commutators of the weight-zero state modes are themselves modes of translated states. To compare these two calculations, write \(D=\mathbf R\operatorname{End}_{\mathcal S_{\tau_0}}(V)\). For every smooth weak coefficient module \(N\), let \(K(N)=N\otimes B_{\rm gh}\) be its coupled complex with the three ghost families and differential \(Q\). A weight-zero state \(x\in L:=K(V)_0\) acts on every \(K(N)\) by \(O_x^N=x_{(-1)}\). The module identities give \([Q,O_x]=O_{Qx}\) and
\[
 [O_x,O_y]=O_{\{x,y\}},\qquad
 \{x,y\}=\sum_{j\ge0}\frac{(-1)^j}{(j+1)!}\,T^{j+1}(x_{(j)}y).
\]
Here the left side is the graded commutator of actual operators. To see what it computes, take the dg algebra of graded natural endomorphisms of \(K(-)\) on all smooth weak modules. The coupled pro-resolution of \(V\) represents the coefficient functors degree by degree. By Yoneda, composing the natural operations corresponds to graded-opposite composition on that resolution. Its natural endomorphism algebra thus models \(D^{\mathrm{op}}\). Evaluation at the vacuum is a quasi-isomorphism of complexes by the resolution and its augmentation. Its composite with \(x\mapsto O_x\) is the inclusion \(L\hookrightarrow K(V)\), since \(x_{(-1)}\mathbf1=x\). All nonzero internal weights are acyclic on this noncritical fibre. Consequently the modes give a strict dg Lie quasi-isomorphism from \(L\) to the commutator of the endomorphism model.

The bracket \(\{x,y\}\) of two weight-zero states lands in \(I_T=T K(V)_{-1}\). Indeed \(x_{(j)}y\) has internal weight \(-j-1\), so \(T^j(x_{(j)}y)\) has weight \(-1\) in each summand. Translation commutes with \(Q\) and is injective in weight \(-1\). In the associated graded Poincaré–Birkhoff–Witt basis of matter and ghost jets, differentiating the highest jet appearing in a nonconstant finite polynomial introduces an independent jet of the next order, also for exterior generators. Only constants can have zero derivative, and they have weight zero. Thus \(I_T\) is isomorphic as a complex to the acyclic weight-\(-1\) complex. The projection onto the abelian dg Lie algebra \(L/I_T\) is a quasi-isomorphism. This proves that the commutator dg Lie algebra of \(D\) is homotopy abelian, since the commutator for the graded opposite is identified by \(x\mapsto-x\).

Now antisymmetrize the four labelled inputs of the associative minimal model. On suspended inputs this is the graded symmetric permutation sum. The three copies of \(sa_3\) have even degree \(2\), and \(su\) has degree \(7\), so all \(3!\) permutations within each placement of \(su\) have positive sign. In the normalized model only its last placement contributes. The arity-four commutator bracket is therefore
\[
 \ell_4(sa_3,sa_3,sa_3,su)=6\gamma\,s(a_3z).
\]
The lower commutator brackets vanish. In a minimal \(L_\infty\) algebra the first nonzero bracket is carried by the invertible linear part of any equivalence of minimal models. Homotopy abelianness therefore forces this bracket to vanish. Since \(a_3z\) spans the nonzero degree-fifteen line and the field has characteristic zero, \(\gamma=0\). The quartic was the only possible higher operation, so \(D\) is formal as an associative dg algebra at \(\tau_0=-3/2\).

The reciprocal vertex-algebra equivalence and the complementary duality of the compact shifted vacuum, taking the opposite dg algebra where composition reverses, transport ordinary associative formality to \(3/2,\,2/3,\,-2/3\). At the original marked fibre formality makes the Hochschild characteristic map \(HH^\bullet(D,D)\to H^\bullet(D)\) surjective, so every cohomology class has a two-sided derived lift. For two generators one can construct these lifts directly on the coefficient complexes. The component with no inputs gives the action of the generator. The component with one input gives a homotopy for its graded commutator with a closed operator. The higher components express compatibility of these homotopies with composition. Let \(A=\operatorname{Nat}^{\bullet}(K(-),K(-))\), with differential \([Q,-]\) and product composition. For \(y=v_-\), the degree-nine Bockstein at \(\tau=-3/2\), or \(y=z_+\), the marked degree-twelve generator at \(\tau=3/2\), let \(O_y=y_{(-1)}\) act on each smooth weak coefficient complex. A normalized Hochschild cocycle has constant term \(F_0=sO_y\), where \(s\) lowers degree by one. For the bar differential \(b_1+b_2\), use the contraction \(K_n\) of the internal Hom differential in arity \(n\) onto its cohomology representatives. Put \(R_n=[b_2,F_{n-1}]\) and take \(F_n=-K_nR_n\), with the unary normalization on translation described below. The bracket includes composition at both ends of a word and multiplication of adjacent inputs. The unary obstruction vanishes by graded commutativity. For inputs of positive cohomological degrees \(q_i\), a higher obstruction could only take values in degree \(\sum_iq_i+|y|+1-n\). For \(z_+\) this is at least \(17\) in arity two and higher. For \(v_-\) it is \(14\) or at least \(16\). The cohomology vanishes in these degrees. This proves all the equations \([b_1,F_n]+[b_2,F_{n-1}]=0\) directly for the two generators.

The unary component can be evaluated on two specified coefficient operators, the Becchi–Rouet–Stora–Tyutin (BRST) differential \(Q\) and the simultaneous translation \(T=[Q,H_c]\), where \(H_c\) is the spin-two ghost contraction normalized by \(H_c\gamma_2=-1\). The normalizations give
\[
 F_1(sQ)=-|y|\,sO_y,\qquad F_1(sT)=(-1)^{|y|}sO_{H_cy}.
\]
In the negative-fibre PBW basis the ghost is \(\delta_2=-\gamma_2/\tau\). Its deletion in the signed degree-nine primitive therefore has coefficient \(-1/\tau=2/3\). In the ordered ghost basis, a mask encodes the occupied exterior generators. Reducing the coefficients modulo \(1000003\), the resulting vacuum vector has \(15657\) nonzero coefficients. Its first coefficient is \(122031\) at vacuum matter and ghost mask \(4398061191214\). At the positive fibre the indicated translation primitives have exact coefficients \(+1\) for the marked affine state \(a_+=h_{3,0}\) at vacuum matter and mask \(6\), and \(-1\) for \(z_+\) at vacuum matter and mask \(840026912980994\).

The positive degree-three state \(a_+\) has an all-arity determinant formula. Here fixed-fibre associative formality proves consistency of the \(31\) linear equations in \(41\) small-cochain coefficients. Their matrix has rank \(9\). In the marked basis \(a=a_+,\,b=\eta_5,\,c=\eta_7\), the first three required values are the arity-two obstruction coefficients on \((a,b)\to ac,\ (a,c)\to av,\ (a,c)\to z\). After their correction, the other six come from \((a,a,b)\) and \((a,b,a)\), each with outputs \(av,z\), and from \((a,a,u)\) and \((a,u,a)\), each with output \(az\). The two diagonal minors have determinant \(+1\), so these prescribed readings suffice to correct every row, including the arity-four rows. The nine scalar values in the original coefficient complex remain unevaluated. Whether a different choice of measurements could use fewer values is open. An explicit lift of the additional degree-eight class \(u\) also remains to be constructed.

Further questions are whether the separately defined reciprocal Drinfeld–Sokolov reductions intertwine their pinned affine maps and whether the integrated degree-seven orbit operation has a local nullhomotopy before integration. Formality of the entire level family, and simultaneous formality of the affine morphism with its source and target, are separate comparisons. [CQ12](#ref-ch12-cq12)

A coproduct answers the opening question only with its target specified. The spectral coproduct acts on two covariant modules with their cross contraction. For the divided rational double the original current lifts give a proper embedding in normalized multipoint modes through precision two at every rank and level. At level zero the original embedding persists at every precision and in the inverse limit. At nonzero level the rank-two embedding through precision three uses the corrected generators. The ungenerated two-point pole explains why even an injective action of currents leaves other collision operations to determine.

The exceptional \(W_4\) vacuum supplies a different invariant, its graded Yoneda algebra, which as an associative dg algebra with zero differential models the derived endomorphisms at the four specified fibres. To identify a category of physical lines one needs a functor carrying collisions, units and exchange. For example, the ordinary current residue \(J^x_{(0)}J^y=J^{[x,y]}\) returns a state, and a third current can act on it. Recovering the algebra requires knowing which state that residue returns. Two lattice theories can have the same ribbon category and even the same vacuum character while their weight-one residues give different Lie algebras. [The two lattice residues](13-geometric-reconstruction.md#ch13-counterexample-two-unimodular-lattices) · [The geometric vacuum at a collision](13-geometric-reconstruction.md#ch13-the-realized-vacuum-on-every-configuration)

## References {#ch12-references}

### CQ1. Associative chiral algebras {#ref-ch12-cq1}

*Associative chiral algebras*, sections “Factorization and the support of the cobar,” “Recovering the symmetric theory,” and “Coproducts, the second tensor and centres.”

### CQ2. Coproducts from a spectral form {#ref-ch12-cq2}

*Coproducts from a spectral form*, sections “A form with a spectral parameter,” “The fields at a level,” and the tensor-product, coproduct and module-tensor theorems; *The tensor category of a spectral form*, “The identity level of a cocommutative Hopf algebra” and “The symmetry of comodules”; *Chiral quantum groups: the constructed sector*, Definition “Spectral chiral quantum group” and Theorem “Consequences of the datum”; *Quantum vertex algebras as associative chiral algebras*, definition of a quantum vertex algebra with rational exchange. In *Regular sections of a tensor product, and duals*, the theorem “Regular sections of a tensor product” identifies the product lattice at every arity. The theorem “The tensor at every number of positions” gives the corresponding identification after the braided shuffle and shows that it commutes with collisions and cuts.

### CQ3. Chiral Koszul duality {#ref-ch12-cq3}

J. Francis and D. Gaitsgory, [*Chiral Koszul duality*](https://arxiv.org/abs/1103.5803), Theorems 5.1.1 and 5.2.1. A. Beilinson and V. Drinfeld, *Chiral Algebras*, §§3.1 and 3.4–3.5.

### CQ4. The rational affine comparison and its double {#ref-ch12-cq4}

*The rational affine comparison and its double*, creation–annihilation factorization and rational affine comparison theorems. *Integral fields of the rational RTT algebra*, “The coordinate algebra and the divided algebra” and “The coaction and the pairing.” P. Etingof and D. Kazhdan, [*Quantization of Lie bialgebras, V*](https://arxiv.org/abs/math/9808121), §§1–3. N. Jing, S. Kožić, A. Molev and F. Yang, [*Center of the quantum affine vertex algebra in type A*](https://arxiv.org/abs/1603.00237v2), Theorem 2.2 (PBW for the \(\mathfrak{gl}_N\) double), §4.1 (its \(\hbar\)-adic presentation) and Theorem 4.1 in §4.2 (vacuum fields (4.17) and exchange (4.19)).

### CQ5. The Yang double as a chiral quantum group {#ref-ch12-cq5}

*The Yang double of gl_n as a chiral quantum group*, §§3–4 on the regular dual vacuum, exchange and full curvature, and §15.3, Theorem 15.4 and Corollary 15.5, on the point adjunction and the finite quotients. R. Lorgat, *Koszul cochains of the Yang double*, §8, equations (57)–(58) and the construction following (58), pp. 32–34, gives the formal mapping complexes and the realization of coherent systems.

### CQ6. Curved duals of nonlinear fields {#ref-ch12-cq6}

*The dual of the W3 algebra*; *The curved dual of the W4 algebra*; *The ramified Miura parameter*, polynomial-form theorem; *Polynomial transposes and derivative corrections*, Theorem “General derivative-corrected transpose.”

### CQ7. Curved duality for the regular universal \(W_3\) algebra {#ref-ch12-cq7}

*Curved duality for the regular universal W3 algebra*, Theorems 0.1–0.2 and §§3–6.

### CQ8. The bulk of a principal \(W\)-algebra {#ref-ch12-cq8}

*The bulk of a principal W-algebra*, finite weight-zero comparison, generic formality and §§12.3–12.6 on the orbit differential, the top-degree minor and the primitive products. R. Lorgat, *Vacuum self-extensions of principal W-algebras*, Theorem 1.1 and §8, Proposition 8.1 and the calculations that follow it, pp. 22–24.

### CQ9. The quantum group of the Virasoro algebra {#ref-ch12-cq9}

*The quantum group of the Virasoro algebra, as an object*, Theorems 14.1 and 15.2, equations (14.18)–(14.22) and (15.13)–(15.19), and §§16.3, 17–19 for the endpoint and finite-length categories. The trivalent Ising gauge is given by P. Bonderson, M. Freedman and C. Nayak, *Measurement-Only Topological Quantum Computation via Anyonic Interferometry*, Appendix A.1.

### CQ10. Charged endpoints and chiral fusion {#ref-ch12-cq10}

*Chern–Simons observables, charged endpoints and chiral fusion*, Theorem 4.1. *The fusion of abelian lines at a Heisenberg boundary*, “The comparison,” with dual half-loop transport on states.

### CQ11. The rational double in the algebra of modes {#ref-ch12-cq11}

*The algebra of modes of a quantum vertex algebra*, “Modes on several points,” “The algebra of modes” and “The filtration by the number of points.” *Flatness and the rational deformation*, “The first-order current calculation” and “Recovering creation and annihilation operators.” *The rational double in the algebra of modes*, the divided determinants and the rank-two mixed and same-half relations.

### CQ12. The exceptional \(W_4\) vacuum {#ref-ch12-cq12}

*The first Bocksteins and degree-three products of the exceptional universal W₄ vacuum*, §§2–6, and *The exceptional W₄ vacuum product in degrees seven and eight*, §§1–4. For the equivariant minimal model see *One quartic value decides formality with the marked diagram involution*. The polynomial vacuum complex and its special dimensions are those of [CQ8](#ref-ch12-cq8). The geometric input at \(\tau=-3/2\) is the diagram action on the filtered Whittaker orbit coefficient and its two integrated rows. The four-insertion and two-sided-lift tests use the same marked vacuum endomorphism algebra. *The native exceptional W₄ quartic vanishes*, §§1–3, gives the coefficient-operator comparison, the translation ideal and the four-input calculation. *Two-sided characteristic cocycles in the exceptional \(W_4\) coefficient resolution*, §§1–4, and *The affine three-class in the positive native PBW coordinates* give the original cocycles and the spin-two normalization. *Nine BRST readings determine the original affine characteristic cocycle* gives the rank and the two prescribed minors.

### CQ13. Crossings and coproducts of Wilson lines {#ref-ch12-cq13}

K. Costello, E. Witten and M. Yamazaki obtain the rational dependence on the two holomorphic positions and compute the one-gauge-boson exchange in perturbation theory. The fundamental matrix is determined here up to a scalar. [*Gauge Theory and Integrability, I*, §§3.4–3.6, equations (3.23)–(3.24)](https://arxiv.org/pdf/1709.09993#page=25) · [§4, equations (4.11)–(4.13)](https://arxiv.org/pdf/1709.09993#page=33)

For \(\mathfrak{gl}_N\) the two ways of crossing two fundamental test lines with a third line give the matrix relation \(RT_1T_2=T_2T_1R\). Crossing a test line with a pair of parallel lines gives the coproduct by summing its intermediate colour. [*Gauge Theory and Integrability, II*, §§2.2–2.3, equations (2.11)–(2.12) and (2.19)–(2.22)](https://arxiv.org/pdf/1802.01579#page=9)
