# Quantum groups and nonlinear chiral algebras

For two representations \(M,N\) of a Lie algebra \(\mathfrak g\), the diagonal action on \(M\otimes N\) comes from the coproduct of the universal enveloping algebra \(U(\mathfrak g)\),
\[
\Delta(x)=x\otimes1+1\otimes x.
\]
For affine currents the central terms add. Suppose the operator product expansions (OPEs) of two independent Heisenberg currents are
\[
h_i(z)h_i(w)\sim\frac{\kappa_i}{(z-w)^2},\qquad i=1,2,
\]
with regular mixed OPE \(h_1(z)h_2(w)\). Then \(h=h_1+h_2\) has level \(\kappa_1+\kappa_2\). Thus the natural map is
\[
H_{\kappa_1+\kappa_2}\longrightarrow
H_{\kappa_1}\otimes H_{\kappa_2},\qquad
h\longmapsto h_1\otimes1+1\otimes h_2.
\]
It belongs to a family of algebras indexed by level. Moreover, a nonzero level prevents a scalar counit that preserves fields: such a map would imply
\[
\kappa=\varepsilon(h_{(1)}h)
=\varepsilon(h)_{(1)}\varepsilon(h)=0.
\]
The universal algebra, in which the central state is retained as a generator, has a coproduct and counit; fixing its nonzero value changes that conclusion. [CQ1]

For a chiral coproduct \(D\) the corresponding bialgebra condition is an identity of fields,
\[
D\bigl(Y(a,z)b\bigr)=Y_{\mathrm{tensor}}(Da,z)\,Db.
\]
Here \(Y_{\mathrm{tensor}}\) is the field on the specified tensor product of the two targets. Its cross contractions and the levels of both factors enter the equation. In the spectral Hopf-algebra construction below this identity holds on all states, together with coassociativity and the field hexagon. For rational matrix currents the construction uses an \(R\)-matrix exchange relation, usually called the RTT relation. Generation of the algebra of multipoint modes is a separate question.

## Associative products on configurations {#ch12-associative-products-on-configurations}

Recall the distinction between fields and collision residues. A vertex algebra has weakly associative fields \(Y(a,z)\), but the corresponding Beilinson–Drinfeld chiral operation is a Lie operation. For right differential modules on a smooth curve \(X\), its binary map has the form
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
For the first flag, \(\alpha=ds\wedge dt/[s(s+t)]\); for the second, the coordinate change contributes a minus sign and \(\alpha=-ds\wedge dt/[t(t-s)]\), which has no \(s^{-1}\) term. The third expansion begins with \(-s^{-1}t^{-1}ds\wedge dt\). The first two flags join consecutive positions. The third first joins positions 1 and 3 while position 2 remains separate. Their relation is the residue form of Jacobi. Associative composition requires a complex that keeps this third stratum. [CQ1]

For word configurations, the coefficient category is \(\mathcal W_X\) from Chapter 5: complexes on \(X^n\) with coherent extraordinary-pullback identifications along monotone collisions, together with an isolated empty coefficient. Its convolution \(\star_{\mathrm{cut}}\) sums over consecutive cuts and extends external products from the corresponding separating opens. This convolution is nonsymmetric.

The full ordered collision category uses the schemes \(\mathscr R_I\), obtained by gluing one \(X^I\)-chart for every total order, and collision maps for surjections with ordered fibres. Its convolution \(\star\) sums over all ordered decompositions into subsets and is symmetric monoidal. Restriction to the increasing chart followed by projection to consecutive summands transports a coalgebra to the word category. That projection need not be an equivalence. Both convolutions have a unit \(K\) supported at the empty configuration; a coefficient system is **positive** when its empty coefficient is zero. [CQ1]

For either convolution, an **associative chiral algebra** is an augmented \(E_1\)-algebra \(A\) with positive augmentation ideal whose bar coalgebra \(BA\) factorizes. If \(I=S\sqcup T\) is an admissible decomposition and \(U_{S,T}\) is the open where its two blocks are disjoint, factorization requires the coproduct component to induce an equivalence
\[
(BA)_I|_{U_{S,T}}\xrightarrow{\sim}
     \bigl((BA)_S\boxtimes(BA)_T\bigr)|_{U_{S,T}} .
\]
For \(\star_{\mathrm{cut}}\) the admissible decompositions are the consecutive cuts. For \(\star\) they are all ordered decompositions into subsets. [CQ1]

In a differential graded presentation, the associative structure can be described by an \(A_\infty\) structure: a differential, multiplication, homotopies relating triple products, and higher homotopies satisfying the Stasheff identities. This is the meaning of \(E_1\) here. With the cohomological convention \(V[1]^n=V^{n+1}\), its suspended operations on \(A[1]\) have degree one. The residue coalgebra \(C(V)\) of appropriate fields gives
\[
A_V=\Omega_{\mathrm{cut}}C(V).
\]
The cobar construction assembles the ordered collision terms and their differential into the associative object. Its algebra unit is supported at the empty configuration. A vacuum marking specifies a left differential module \(G\), a horizontal map \(\mathcal O_X\to G\), and an identification \(A_{\{1\}}\cong\omega_X\otimes_{\mathcal O_X}G\). A vacuum framing also compares the configuration operations with the original simultaneous fields, preserving substitutions, translation and that vacuum.

A compatible **\(E_1\) chiral coproduct** requires further data. Specify a tensor product \(\diamond\) combining systems at the same positions, together with the geometric interchange that makes \(A\diamond A'\) an algebra for \(\star\). A coproduct is then an algebra map
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
This construction does not automatically identify \(\diamond\) with a tensor of fields carrying a nontrivial exchange. The latter needs its own comparison. [CQ1, CQ2]

The construction from a Beilinson–Drinfeld chiral Lie algebra \(L\) is
\[
L\longmapsto C_{\mathrm{ch}}(L)
\longmapsto\operatorname{res}_{\mathrm{cut}}C_{\mathrm{ch}}(L)
\longmapsto\Omega_{\mathrm{cut}}\operatorname{res}_{\mathrm{cut}}C_{\mathrm{ch}}(L).
\]
Here \(C_{\mathrm{ch}}\) is the Francis–Gaitsgory chiral Chevalley-chain construction. Its coalgebra is cocommutative for the chiral tensor on Ran space and factorizes when the Lie object is supported on the singleton copy of \(X\). The operation \(\operatorname{res}_{\mathrm{cut}}\) retains only monotone collision maps and projects the all-subset coproduct onto consecutive cuts. Coassociativity survives because both iterated projections retain the same consecutive blocks; factorization survives on the cut opens. Taking associative cobar then gives the word object defined above.

This comparison is performed on the coalgebra before taking cobar. It does not identify associative bar–cobar duality with Lie–commutative duality. To recover a chiral Lie algebra in the reverse direction, the entire associative bar must extend along every finite-set surjection with a compatible cocommutative coproduct and factorization. A field comparison and a chiral coproduct require their additional vacuum and tensor data. [CQ1, CQ3]

## A spectral construction of products and coproducts {#ch12-a-spectral-construction-of-products-and-coproducts}

There is a class in which the fields, their exchange, and the tensor product can all be written explicitly. Let \(R\) be a commutative algebra over a characteristic-zero field. Take a flat Hopf algebra \(H\) over \(R\), with bijective antipode \(\mathsf s\), and a derivation and coderivation \(T\) satisfying \(\varepsilon T=0\). Write
\[
\Delta a=a_1\otimes a_2,\qquad a(z)=e^{zT}a,
\]
with summation understood. A **unitary spectral coquasitriangular form** is an \(R\)-bilinear map
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
The fourth identity specifies exchange, and the last makes exchange reversible. A **level** is a Hopf automorphism \(\eta\) commuting with \(T\) and preserving \(\rho_z\). Choose a group \(\Lambda\) of levels; it need not be commutative. These data define the spectral class of chiral quantum groups considered here. [CQ2]

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
One coproduct component creates the translated state; the other contracts with the state already present. Finite coproducts and finite Laurent values of \(\rho\) make this an element of \(H((z))\) for fixed inputs. Denote the resulting field algebra by \(V_\eta\).

**Theorem (spectral field and coproduct construction).** Under the hypotheses above, \(V_\eta\) is a quantum vertex algebra with vacuum \(1\), translation \(T\), and rational exchange
\[
\mathcal S_\eta(z)(a\otimes b)
=a_{(0)}\otimes b_{(0)}\rho_z(a_{(1)},b_{(1)}).
\]
Every finite ordered product on a fixed state has a common finite denominator. For \(V_1=V_{\eta_1}\) and \(V_2=V_{\eta_2}\), their tensor product \(\boxtimes_\rho\) has underlying module \(V_1\otimes_RV_2\) and fields
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
preserve fields, vacuum, translation and coaction. They are coassociative, with counit \(\varepsilon:V_{\mathrm{id}}\to R\) at the identity level. They induce maps of residue coalgebras and their augmented associative chiral cobars. Over a field, the same constructions descend to the ordered collision schemes. [CQ2]

The cross contraction in \(Y_{12}\) is the extra factor required by interchange. Omitting it changes the product against which \(D\) is tested. The compatibility equation is the actual field identity
\[
D\bigl(Y_{\eta_1\eta_2}(a,z)b\bigr)
=Y_{12}(Da,z)Db.
\]
In its proof, the coaction intertwines annihilation operators and the antipode cancels adjacent Hopf factors. Coassociativity can be seen without commuting the levels: both triple maps send \(a\) to
\[
\eta_2\eta_3a_1\otimes\eta_3a_2\otimes a_3.
\]
The two counit identities are
\[
(1\boxtimes_\rho\varepsilon)D_{\eta,\mathrm{id}}=1,
\qquad
(\varepsilon\boxtimes_\rho1)D_{\mathrm{id},\eta}=1.
\]
This coalgebra counit is unrelated to the counit of a module adjunction.

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
These are called **covariant modules of fields**. The same cross-contraction formula defines their tensor action. Pulling it back along \(D_{\eta_1,\eta_2}\) gives a module at level \(\eta_1\eta_2\). The categories together are monoidal, graded by \(\Lambda\), with scalar unit at the identity level. [CQ2]

### What a half-turn measures in the Ising model {#ch12-ising-half-turn}

One can also begin with a category of fields whose fusion and exchange have been specified and reconstruct a quantum group acting on its channel spaces. In the simple Ising Virasoro theory at \(c=1/2\), the three simple fields \(\mathbf1,\psi,\sigma\) have conformal weights \(0,1/2,1/16\). Here \(\mathbf1\) is the vacuum, \(\psi\) is the fermion and \(\sigma\) is the spin field. Fusion obeys

\[
\psi\boxtimes\psi=\mathbf1,\qquad
\psi\boxtimes\sigma=\sigma,\qquad
\sigma\boxtimes\sigma=\mathbf1\oplus\psi .
\]

An ordinary multiplicative vector-space dimension would give \(d_\psi=1\) and \(d_\sigma^2=2\). The integer dimension of a nonzero finite vector space cannot satisfy the second equation. Keep instead the two labels at the ends of each fusion channel. With \(A=\bigoplus_i\mathbb C e_i\) and \(L_i\) the three simples, set

\[
e_i\,\mathcal F(M)\,e_j=\operatorname{Hom}(L_i,M\boxtimes L_j).
\]

Gluing two channels sums over a **common** intermediate label \(j\). Composition of these maps with the fusion associator therefore identifies \(\mathcal F(M)\otimes_A\mathcal F(N)\) with \(\mathcal F(M\boxtimes N)\). Their complex vector-space dimensions on \(\mathbf1,\psi,\sigma\) are \(3,3,4\). The reconstructed algebra is a ribbon weak Hopf algebra \(H\) of dimension \(3^2+3^2+4^2=34\). Its coproduct on the unit, \(\Delta(1)\), projects the ordinary tensor product onto the pairs with matching intermediate labels. This is the space on which exchange acts. [CQ9]

There are two paths for fusing three spins to one spin, according as the first pair gives the vacuum or the fermion. In the real trivalent basis, with \(\zeta=e^{\pi i/8}\), the positive half-turn of the first pair and the change of fusion channel have matrices

\[
B_1=\begin{pmatrix}\zeta^{-1}&0\\0&\zeta^3\end{pmatrix},
\qquad
F=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

Removing the scalar \(\zeta^{-2}\) from \(B_1^2\) gives \(Z=\operatorname{diag}(1,-1)\). For the second pair it gives \(FZF=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). The two involutions anticommute and their products span the full two-by-two matrix algebra. More generally the complex algebra generated by adjacent double exchanges on \(\sigma^{\boxtimes n}\) is its entire intertwiner algebra. For instance four spins have two vacuum paths and two fermion paths, giving \(M_2(\mathbb C)\oplus M_2(\mathbb C)\). This assertion takes linear combinations of braids. In each simple output of multiplicity \(d\), individual pure braids have only \(d^2\) projective images.

Reflection inverts both half-turn phases. Their **labelled ratio** in the fermion and vacuum channels changes from \(i\) to \(-i\), while both squared phases acquire the same factor \(i\). Thus projective double exchanges lose the orientation. The twist of a framed spin, \(\zeta\) in the given orientation and \(\zeta^{-1}\) in the mirror, also distinguishes them. For the Gaussian rays of Chapter 11 the variance of the comparison matters even in a one-dimensional channel. At level \(k\ne0\) the operation on charges \(a,b\) has coefficient \(z^{ab/k}\), with upper half-turn \(e^{\pi iab/k}\). Parallel transport on the dual state line has the inverse phase. Evaluation pairs the two transports to one. [CQ9, CQ10]

The finite-length Virasoro Ward construction also treats logarithmic modules. It uses the universal vacuum, lower-bounded generalized modules of finite length and finite-dimensional generalized weight spaces, finite support in integral weight cosets, and the \(C_1\)-cofiniteness condition. This last condition means the quotient by the span of \(v_{-1}w\) for positive-weight vertex-algebra states \(v\) is finite dimensional. On this domain the Ward operation represents logarithmic fusion at every charge. At \(c=1,25\) the resulting rigid ribbon categories admit reconstruction by complete quasi-Hopf algebras, including nonsplit objects. On their finite-sum semisimple parts the normalized descriptions have common simple labels \(V_j\) of parity \(j-1\bmod 2\). A half-turn of two odd strands is the flip times \(+i\) at \(c=1\) and times \(-i\) at \(c=25\). Their common associator makes the ratio for a braid the sign of the induced permutation of the odd strands. Every unframed pure braid therefore agrees exactly in these two presentations, while a framed turn of \(V_2\) distinguishes them. Extending that parity formula to nonsplit objects would require their logarithmic transport. [CQ9]

::: figure fig-programme-context-quantum

::: figure fig-spectral-coproduct

## Rational matrix fields and the full curved dual {#ch12-rational-matrix-fields-and-the-full-curved-dual}

For rational matrix currents, the exchange is expressed by an \(R\)-matrix. To avoid confusing it with the coefficient ring, write
\[
\mathsf R(u)=f(u)\left(I-\frac{\hbar P}{u}\right),\qquad
f(u+N\hbar)=f(u)(1-\hbar^2/u^2),
\]
where \(P\) exchanges the two factors of \(\mathbb C^N\otimes\mathbb C^N\), \(N\ge2\), and \(f(u)=1+O(\hbar/u)\). Its first correction is
\[
\mathsf R(u)=I-\frac{\hbar\Omega}{u}+O(\hbar^2),
\qquad\Omega=P-N^{-1}I.
\]
The two matrices
\[
L(v)=I+\hbar\sum_{r\ge1}\ell^{[r-1]}v^{r-1},\qquad
C(p)=I+\hbar\sum_{r\ge1}m^{(r)}p^{-r}
\]
describe the creation and annihilation halves. In each half the RTT relation is
\[
\mathsf R(u-v)X_1(u)X_2(v)=X_2(v)X_1(u)\mathsf R(u-v).
\]
Here \(X=L\) or \(C\). Subscripts \(1,2\) indicate the two auxiliary copies of \(\mathbb C^N\). The mixed relation at numerical level \(K\in\mathbb C\) is
\[
\mathsf R(p-v+K\hbar/2)C_1(p)L_2(v)
=L_2(v)C_1(p)\mathsf R(p-v-K\hbar/2).
\]
The denominators are expanded at \(p=\infty\). The relations are imposed in their divided integral form: the RTT defects are divided by \(\hbar^2\), and the determinant-one relations by \(\hbar\), before taking coefficients. This retains the classical relations at \(\hbar=0\). [CQ4]

**Theorem (rational affine field comparison).** For every \(N\ge2\) and every \(K\in\mathbb C\), the divided determinant-one double is topologically free over \(\mathbb C[[\hbar]]\). Multiplication identifies it, as a module, with the \(\hbar\)-adically completed tensor product of its creation and annihilation halves. The integral divided-state fields agree with the Etingof–Kazhdan quantum affine fields on every state and on their exchange. Their classical determinant-one fibre is \(V_K(\mathfrak{sl}_N)\), with the trace-form normalization. [CQ4]

The proof first establishes the Poincaré–Birkhoff–Witt basis and the creation–annihilation factorization. It then identifies the annihilation matrix with the inverse of the operator matrix obtained from the coordinate coaction. The scalar pairing used in that identification has one divided input. Coordinate functions and divided states therefore play different roles even though both are described by matrices.

The field target is
\[
M((z))^\wedge=\varprojlim_d(M/\hbar^dM)((z)).
\]
At each precision and on fixed inputs the pole order is finite. A bound uniform in the precision would be stronger. The comparison above identifies the fields on states. To recover the algebra of modes one must also account for all functions against which several fields can be integrated.

### What the rational currents generate {#ch12-intrinsic-rtt-modes}

At precision \(d\), put \(R_d=\mathbb C[\hbar]/(\hbar^d)\) and \(V_d=U/\hbar^dU\), with \(U\) the divided creation algebra. An \(n\)-point mode \([f;a_1,\ldots,a_n]\) has a multiplier \(f\) regular on configurations of distinct nonzero positions and a state \(a_i\in V_d\) at each position. Integration by parts imposes \(\partial_{z_i}+T_i=0\), where \(T_i\) translates the \(i\)-th state. Concatenation multiplies the multipliers. Exchanging adjacent fields changes an ordered mode by the collision residue. At a pair \(x=y+u,y\) this residue takes the \(u^{-1}\) coefficient of \(f(y+u,y,\ldots)Y(a,u)b\). The other positions and their poles survive inside \(f\). Impose this relation at every arity. Write \(\bar M_d\) for the resulting algebra with the local vacuum \(\mathsf v=[z^{-1};\mathbf1]\) identified with the empty product \(1\).

This last identification can be tested. In the creation-first convention the classical affine commutator supplies \(K\mathsf v\,\Omega/(u-v)^2\), while the centered shifts in the mixed relation supply \(-K\Omega/(u-v)^2\). Without normalization the difference \(K(\mathsf v-1)\Omega/(u-v)^2\) is nonzero at \(K\ne0\). Thus an equality after acting on the vacuum would miss a relation inside the intrinsic algebra.

Let \(e_{ij}=\ell_{ij}^{[0]}\) be the matrix-current states. The Cauchy lift of a current mode begins with the one-position mode of \(e_{ij}\). At first order its creation correction for Laurent multiplier \(f\) is

\[
-\hbar\sum_a [f(x)/(x-y);e_{ia},e_{aj}] .
\]

The negative-current lift also includes the shift of its argument by \(-K\hbar/2\). With these prescribed lifts, at rank two and **every** numerical level \(K\) there is an injective algebra homomorphism with proper image

\[
D_K/\hbar^2D_K\ \longrightarrow\ \bar M_2 .
\]

The precision is taken **after division** of the two same-half RTT relations and the centered mixed relation by \(\hbar^2\), and of each determinant defect by \(\hbar\). Thus the identities retain the constant and linear coefficients of each divided relation. Both divided determinants hold to this precision in every rank \(N\ge2\), even before identifying the local vacuum. For the determinant, the descending-column shifts give a translation of the diagonal states, which cancels their first integral trace correction. The remaining coefficient is an exchange difference whose collision residue is the ordered state product. In the mixed rank-two relation, sliding a current across both slots of its Cauchy correction keeps the spectator pole. The derivative from undoing the spectral shift cancels the central first-order correction. These computations take place inside the mode algebra. [CQ11]

The missing modes have a geometric witness. Reduce at \(\hbar=0\) and filter by number of positions. In the two-current component, the symmetrized leading multiplier of

\[
[(x-y)^{-1};e_{12},e_{21}]
\]

has \(e_{12}\otimes e_{21}\) coefficient \(1/(2(x-y))\). Products of classical single-current modes have Laurent-polynomial coefficients in \(x,y\), regular along \(x=y\) away from the punctures. The ordered Poincaré–Birkhoff–Witt symbols of higher-degree words are independent, so cancellation among such words cannot produce this two-point pole. The same independence gives injectivity of the classical current map. Freeness over \(R_2\) then lifts injectivity to the displayed precision. For the rank-two intrinsic homomorphism the next coefficients are quartic in the undivided RTT equations and cubic in the undivided determinants. Their vanishing, the all-order homomorphism and its level-composing coproduct remain open. The pole already excludes generation of the whole normalized multipoint algebra by these lifts. [CQ11]

The dual ghost algebra illustrates another distinction. The regular half-dual has odd matrix coefficients
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
These fields have a nontrivial quantum exchange and satisfy the differential graded quantum vertex identities in their specified \(\hbar\)-adic domain. [CQ5]

The **full curved dual** also retains the mixed creation–annihilation relation. Its curvature contains
\[
\Theta_K(x)=\hbar^{-2}
\left(1-\mathsf R(x+K\hbar/2)^{-1}
             \mathsf R(x-K\hbar/2)\right),
\qquad
[x^{-2}]\Theta_K=K\Omega.
\]
The leading term follows by inserting \(\mathsf R(x)=I-\hbar\Omega/x+O(\hbar^2)\) into the two opposite shifts. Their difference first contributes at order \(\hbar^2\). A differential-stable ideal generated by the creation ghosts contains this curvature; the corresponding quotient contains the regular half-dual. Thus passage to half-ghosts can remove precisely the mixed datum that remembers the level. A module duality for the full double must handle that curvature and the actual summation domains. The algebraic curved duality and the regular half-field construction do not settle the smooth completed comparison. [CQ5]

## Nonlinear fields: the \(W_3\) example {#ch12-nonlinear-fields-the-w3-example}

Matrix exchange deforms commutation among currents. A different complication occurs when a singular product is itself quadratic in fields. On the normalized universal \(W_3\) chart, set
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
Here \([a_\lambda b]=\sum_{n\ge0}\lambda^na_{(n)}b/n!\), and \(:ab:=a_{(-1)}b\). The coefficient \(\Lambda\) prevents the modes from forming a Lie algebra on the original generators alone.

The curved field dual has odd generators \(\tau,\varpi\) with
\[
[\tau_\lambda\tau]=2\beta\varpi T\varpi,
\]
and \(\varpi\) has zero singular products with every field. Although square-free ordered jet monomials give a basis, the normal product is not exterior multiplication. For example, quasi-commutativity gives
\[
\frac{\tau T\tau-(T\tau)\tau}{2}
=\tau T\tau-\frac\beta2T^2(\varpi T\varpi).
\]
This derivative correction is part of transposing the quadratic source relation. It disappears if one replaces the dual fields by regular exterior ghosts. [CQ6]

More generally, for a universal vertex algebra over a characteristic-zero field, freely generated by finitely many even fields of half-integer weights at least one, homogeneous quadratic–linear–scalar brackets admit a derivative-corrected transpose. Its odd envelope has an ordered jet basis, a degree-one derivation \(d\), and curvature \(w\) of degree two satisfying
\[
d^2=w_{(0)},\qquad dw\in TB.
\]
The construction supplies a finite translation primitive for \(dw\). If \(q=\sum_i x_i\otimes c_i\) is the generator-linear coupling, its Maurer–Cartan identity is taken modulo total translation. Such couplings into an ordinary vertex algebra characterize the maps from the original universal algebra. This is a field theorem with algebraic states; it is not yet a theorem about topological module categories. [CQ6]

The normalized \(W_3\) chart inverts \(22+5c\). The regular universal presentation retains a spin-three generator \(U\) at every finite charge, including \(c=-22/5\). Write \(a=(22+5c)/16\) in its regular mode convention. Applying one commutator to the vacuum gives

\[
[U_{-1},U_{-3}]\mathbf1
=2L_{-2}^2\mathbf1+\tfrac35(a-2)L_{-4}\mathbf1 .
\]

The two creation words are independent by the Poincaré–Birkhoff–Witt basis. A linear coupling to freely exterior scalar ghosts on the original modes would express the commutator by single modes and scalars. It cannot produce the coefficient two of \(L_{-2}^2\mathbf1\), even at the exceptional charge. The regular algebra instead permits a curved bar construction at every charge. [CQ7]

Let \(A_c\) be its complete mode algebra, with the vector-annihilator topology: neighborhoods are left ideals annihilating finite tuples of vectors in smooth modules. A module is **smooth** if each vector is killed by all sufficiently high modes; the bound may depend on the vector. The continuous vacuum coefficient \(e:A_c\to\mathbb C\) is a linear unit retraction, generally not an algebra homomorphism. Put \(E=\ker e\) and define the bilinear maps
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
with algebraic input tensors and graded-opposite concatenation. Its bar differential satisfies \(d^2=[h,-]\) and \(dh=0\). To specify its infinite summations, set \(\widehat B_c=\prod_{n\ge0}B_c^n\). For finite-dimensional \(H\subset E\) and \(N\ge0\), let \(J_{H,N}\) be the ideal of forms vanishing on \(\bigoplus_{n=0}^N H^{\otimes n}\). These ideals define the finite-dual topology. The free contramodule monad on graded vector spaces is
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

A **graded contramodule** is a graded vector space \(Q\) with a degree-zero contraaction \(\gamma:\mathbb T_{B_c}(Q)\to Q\) satisfying
\[
\gamma\eta_Q=1_Q,\qquad
\gamma\mathbb T_{B_c}(\gamma)=\gamma m_Q.
\]
Thus \(\gamma\) evaluates the permitted infinite sums. A **curved differential graded contramodule** additionally has a degree-one connection \(D_Q\) satisfying the Leibniz rule for all these sums and
\[
D_Q(bq)=d(b)q+(-1)^{|b|}bD_Q(q),\qquad D_Q^2(q)=hq.
\]
These objects and their graded contramodule maps form the differential graded category \(\operatorname{CDGContra}(B_c)\), with differential \(f\mapsto D_{Q'}f-(-1)^{|f|}fD_Q\) on maps \(Q\to Q'\). An arbitrary \(Q\) is not assigned a topology: its summations are the contraaction, whereas the specified free objects have the displayed inverse-limit topology.

Writing \(\operatorname{Ch}(\mathcal S_c)\) for complexes in the category of smooth modules, there are actual differential graded adjoint functors
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
for smooth \(P\). A localization on which \(K_c,F_c\) become inverse equivalences of the proposed larger derived categories remains open. [CQ7]

## Exceptional \(W_4\) fibres and the algebra of extensions {#ch12-exceptional-w4-fibres-and-the-algebra-of-extensions}

Miura \(W_4\) supplies another nonlinear field example. Its three generating fields have weights two, three and four. Their sixteen quadratic–linear–scalar relations, with the vacuum included, admit the inverse-transpose curved construction. A polynomial form over \(\mathbb C[a]\) preserves the fields, modes and translation under every scalar extension, including nonflat extensions. This makes specialization a legitimate operation on that field construction. [CQ6]

Specializing a derived invariant can nevertheless change its answer. Let \(W^k(\mathfrak g)\) be the universal principal algebra, and take absolute Ext in the category of all weak, equivalently smooth, modules. At every noncritical level, a nonlinear resolution reduces vacuum self-Ext to a finite weight-zero complex with polynomial parameter differential. Generically its algebra is
\[
\operatorname{Ext}^\bullet(W^k,W^k)
\cong\Lambda(\eta_{2m_1+1},\ldots,\eta_{2m_r+1}),
\]
where \(m_i\) are the exponents of \(\mathfrak g\); it is associative \(A_\infty\)-formal. For \(\mathfrak{sl}_2,\mathfrak{sl}_3,\mathfrak{so}_5\), this exterior algebra and formality hold at every noncritical level. The canonical Drinfeld–Sokolov reduction map has its own exceptional kernels and need not be an isomorphism just because the target ring is exterior. [CQ8]

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
Exactly two local torsion pairs, in degrees \((8,9)\) and \((11,12)\), account for the excess. Their lengths can be read from the first derivative of the differential. In the local parameter \(t=\tau-\tau_0\), write the finite zero-weight differential as \(A+tB+O(t^2)\). On a class killed by \(A\), reduction of \(B\) modulo the image of \(A\) is the first Bockstein. In each of the two degrees its rank is one at both \(\tau_0=3/2\) and \(-3/2\). Indeed null vectors on opposite sides of the constant matrix have nonzero pairing through \(B\), detected modulo \(1000003\) on maximal-rank minors. A single nonunit elementary divisor occurs in each degree, so it has valuation one. The reciprocal parameter change takes a uniformizer to a unit times a uniformizer. Thus both torsion summands are \(R/(t)\) at each of the four points, for \(R=\mathbb C[\tau]_{(\tau-\tau_0)}\). [CQ8, CQ12]

Let \(K_R^\bullet\) be the weight-zero complex of the universal principal vacuum coupled to the three ghosts of spins \(2,3,4\). At each of the four shifted levels \(\tau_0\), specialize its differential before taking cohomology, and write \(K^\bullet_{\tau_0}=K_R^\bullet\otimes_R R/(t)\). For \(V=W^{\tau_0-4}(\mathfrak{sl}_4)\) and its category \(\mathcal S_{\tau_0}\) of smooth weak modules, the vacuum resolution gives
\[
H^\bullet_{\tau_0}
=H^\bullet(K^\bullet_{\tau_0})
\simeq \operatorname{Ext}^\bullet_{\mathcal S_{\tau_0}}(V,V).
\]
Write \(a_3=\eta_3\). Multiplication by \(a_3\) pairs six generators in degrees \(0,5,7,8,9,12\) with six classes three degrees higher. The Yoneda algebra is free on these generators as a graded module over \(\Lambda(a_3)\). Let \(Q\) be the specialized coupled differential. For a closed field \(a\), the supercommutator \([Q,a_{(-1)}]=(Qa)_{(-1)}=0\) makes \(a_{(-1)}\) an operation on every coefficient module. It commutes with connecting maps up to the graded sign, so evaluation on the vacuum and dimension shifting identify it with Yoneda multiplication. Only the \((-1)\)-mode survives in weight-zero cohomology, where the product is graded commutative.

At \(\tau_0=3/2\) the product of \(\eta_7\) with the additional degree-eight generator \(u\) vanishes. To compute it, assign a ghost word its total spin, the sum of the spins of its letters. There are rational cocycles \(C\in K^7_{\tau_0}\) and \(U\in K^8_{\tau_0}\) with all terms of spin at least \(23\) and \(27\), respectively. Pairing with a functional that annihilates boundaries shows that \([C]\) spans \(H^7_{\tau_0}\). The first Bockstein of \([U]\) is nonzero, whereas the degree-eight kernel of this Bockstein is \(\mathbb C\,\eta_3\eta_5\). Thus \([U]\) has a nonzero component along \(u\).

The ordinary ghost product preserves total spin, and every singular reordering term raises it. Consequently every term of \(C_{(-1)}U\) would have spin at least \(50\). The largest ghost spin in the entire weight-zero, degree-fifteen complex is \(49\), so \(C_{(-1)}U=0\) as a rational cochain. Since \(\eta_7(\eta_3\eta_5)=0\), this gives \(\eta_7u=0\) in the chosen generators. For other cochain representatives their product can be a nonzero boundary. The reciprocal isomorphism \(\tau\mapsto1/\tau\) and the complementary duality \(\tau\mapsto-\tau\), which reverses composition, carry the result to all four exceptional fibres. Their graded Yoneda algebra is
\[
H^\bullet_{\tau_0}\cong\Lambda(a_3)\otimes(\mathbb C\oplus I),
\qquad I=\operatorname{span}_{\mathbb C}\{\eta_5,\eta_7,u,v,z\},
\qquad I^2=0,
\]
where \(|u|=8,\ |v|=9,\ |z|=12\) and \(a_3z\) spans degree fifteen. [CQ12]

The transferred ternary operation \(m_3(a_3,a_3,a_3)\) vanishes when the same primitive of \(a_3^2\) is used for both adjacent pairs. Allowing two independent choices gives the ordinary triple Massey indeterminacy \(\mathbb C\,a_3\eta_5\). At the shifted level \(\tau_0=-3/2\), the pinned \(A_3\) diagram involution acts on the actual smooth vacuum and its enhanced affine reduction. It preserves the Whittaker character and the coweight \(2\theta^\vee\). Pullback commutes with the convolution defining the orbit coefficient, and the support morphism is equivariant by naturality. The two surviving orbit rows carry the same negative character after integration. In eigenvector coordinates the signs on \((a_3,\eta_5,\eta_7,u,v,z)\) are consequently \((+,-,+,-,-,-)\). The deformation parameter is fixed.

In characteristic zero one can average a contraction over this involution. In the resulting minimal \(A_\infty\) algebra all candidate ternary operations have negative character and hence vanish. Compatibility with the marked affine map reduces the quartic operation, up to a change of coordinates with identity linear part, to one possible entry in suspended notation,
\[
b_4(sa_3,sa_3,sa_3,su)=\gamma\,s(a_3z),
\]
where \(s\) lowers degree by one. Before this choice of coordinates, \(\gamma\) is the sum of the four \(s(a_3z)\)-coefficients obtained by placing \(su\) in each position among three copies of \(sa_3\). The first Bocksteins alone allow every value of \(\gamma\). An auxiliary flat, strictly unital \(A_\infty\) family over \(\mathbb C[[t]]\) has \(bc=t z,\ du=t v,\ d(au)=-t av\), where \(a=\eta_3,\ b=\eta_5,\ c=\eta_7\). Those equations give the same special binary algebra and both simple Bocksteins for arbitrary \(\gamma\). For the actual vacuum endomorphism algebra at \(\tau_0=-3/2\), the coefficient is **zero**.

To compute it, write \(D=\mathbf R\operatorname{End}_{\mathcal S_{\tau_0}}(V)\). For every smooth weak coefficient module \(N\), let \(K(N)=N\otimes B_{\rm gh}\) be its coupled complex with the three ghost families and differential \(Q\). A weight-zero state \(x\in L:=K(V)_0\) acts on every \(K(N)\) by \(O_x^N=x_{(-1)}\). The module identities give \([Q,O_x]=O_{Qx}\) and
\[
 [O_x,O_y]=O_{\{x,y\}},\qquad
 \{x,y\}=\sum_{j\ge0}\frac{(-1)^j}{(j+1)!}\,T^{j+1}(x_{(j)}y).
\]
Here the left side is the graded commutator of actual operators. To see what it computes, take the dg algebra of graded natural endomorphisms of \(K(-)\) on all smooth weak modules. The coupled pro-resolution of \(V\) represents the coefficient functors degree by degree. By Yoneda, composing the natural operations corresponds to graded-opposite composition on that resolution. Its natural endomorphism algebra thus models \(D^{\mathrm{op}}\). Evaluation at the vacuum is a quasi-isomorphism of complexes by the resolution and its augmentation. Its composite with \(x\mapsto O_x\) is the inclusion \(L\hookrightarrow K(V)\), since \(x_{(-1)}\mathbf1=x\). All nonzero internal weights are acyclic on this noncritical fibre. Consequently the modes give a strict dg Lie quasi-isomorphism from \(L\) to the commutator of the endomorphism model.

The commutator takes values in \(I_T=T K(V)_{-1}\). Indeed \(x_{(j)}y\) has internal weight \(-j-1\), so \(T^j(x_{(j)}y)\) has weight \(-1\) in each summand. Translation commutes with \(Q\) and is injective in weight \(-1\). In the associated graded Poincaré–Birkhoff–Witt basis of matter and ghost jets, differentiating the highest jet appearing in a nonconstant finite polynomial introduces an independent jet of the next order, also for exterior generators. Only constants can have zero derivative, and they have weight zero. Thus \(I_T\) is isomorphic as a complex to the acyclic weight-\(-1\) complex. The projection onto the abelian dg Lie algebra \(L/I_T\) is a quasi-isomorphism. This proves that the commutator dg Lie algebra of \(D\) is homotopy abelian, since the commutator for the graded opposite is identified by \(x\mapsto-x\).

Now antisymmetrize the four labelled inputs of the associative minimal model. On suspended inputs this is the graded symmetric permutation sum. The three copies of \(sa_3\) have even degree \(2\), and \(su\) has degree \(7\), so all \(3!\) permutations within each placement of \(su\) have positive sign. In the normalized model only its last placement contributes. The arity-four commutator bracket is therefore
\[
 \ell_4(sa_3,sa_3,sa_3,su)=6\gamma\,s(a_3z).
\]
The lower commutator brackets vanish. In a minimal \(L_\infty\) algebra the first nonzero bracket is carried by the invertible linear part of any equivalence of minimal models. Homotopy abelianness therefore forces this bracket to vanish. Since \(a_3z\) spans the nonzero degree-fifteen line and the field has characteristic zero, \(\gamma=0\). The quartic was the only possible higher operation, so \(D\) is formal as an associative dg algebra at \(\tau_0=-3/2\).

The reciprocal vertex-algebra equivalence and the complementary duality of the compact shifted vacuum, taking the opposite dg algebra where composition reverses, transport ordinary associative formality to \(3/2,\,2/3,\,-2/3\). At the original marked fibre formality makes the Hochschild characteristic map \(HH^\bullet(D,D)\to H^\bullet(D)\) surjective, so every cohomology class has a two-sided derived lift. Explicit lifts in the original Poincaré–Birkhoff–Witt complex remain to be constructed. Further questions are whether the separately defined reciprocal Drinfeld–Sokolov reductions intertwine their pinned affine maps and whether the integrated degree-seven orbit operation has a local nullhomotopy before integration. Formality of the entire level family, and simultaneous formality of the affine morphism with its source and target, are separate comparisons. [CQ12]

The level coproduct \(D_{\eta_1,\eta_2}\) gives a tensor product on covariant field modules. The rational double gives an embedding \(D_K/\hbar^2D_K\hookrightarrow\bar M_2\) with proper image at rank two. The exceptional \(W_4\) calculation identifies the associative vacuum endomorphism algebra with its graded Yoneda algebra up to quasi-isomorphism. Identifying any of these constructions with a category of physical lines requires a functor carrying line collisions, units and exchange to their algebraic counterparts. The next chapter describes the collision data needed to reconstruct a chiral algebra.

## References {#ch12-references}

[CQ1] *Associative chiral algebras*, sections “Factorization and the support of the cobar,” “Recovering the symmetric theory,” and “Coproducts, the second tensor and centres.”

[CQ2] *Coproducts from a spectral form*, sections “A form with a spectral parameter,” “The fields at a level,” and the tensor-product, coproduct and module-tensor theorems; *Chiral quantum groups: the constructed sector*, Definition “Spectral chiral quantum group” and Theorem “Consequences of the datum”; *Quantum vertex algebras as associative chiral algebras*, definition of a quantum vertex algebra with rational exchange.

[CQ3] J. Francis and D. Gaitsgory, [*Chiral Koszul duality*](https://arxiv.org/abs/1103.5803), Theorems 5.1.1 and 5.2.1. A. Beilinson and V. Drinfeld, *Chiral Algebras*, §§3.1 and 3.4–3.5.

[CQ4] *The rational affine comparison and its double*, creation–annihilation factorization and rational affine comparison theorems. P. Etingof and D. Kazhdan, [*Quantization of Lie bialgebras, V*](https://arxiv.org/abs/math/9808121), §§1–3. N. Jing, S. Kožić, A. Molev and F. Yang, [*Center of the quantum affine vertex algebra in type A*](https://arxiv.org/abs/1603.00237), Theorem 2.2 and §4.1.

[CQ5] *The Yang double of gl_n as a chiral quantum group*, regular dual-vacuum, exchange and full-curvature constructions, §§3–4 and the restricted cochain constructions.

[CQ6] *The dual of the W3 algebra*; *The curved dual of the W4 algebra*; *The ramified Miura parameter*, polynomial-form theorem; *Polynomial transposes and derivative corrections*, Theorem “General derivative-corrected transpose.”

[CQ7] *Curved duality for the regular universal W3 algebra*, Theorems 0.1–0.2 and §§3–6.

[CQ8] *The bulk of a principal W-algebra*, finite weight-zero comparison, generic formality, and §12, especially Theorems 12.3–12.6.

[CQ9] *The quantum group of the Virasoro algebra, as an object*, Theorems 14.1 and 15.2, equations (14.18)–(14.22) and (15.13)–(15.19), and §§16.3, 17–19 for the endpoint and finite-length categories. The trivalent Ising gauge is given by P. Bonderson, M. Freedman and C. Nayak, *Measurement-Only Topological Quantum Computation via Anyonic Interferometry*, Appendix A.1.

[CQ10] *Chern–Simons observables, charged endpoints and chiral fusion*, Theorem 4.1. *The fusion of abelian lines at a Heisenberg boundary*, “The comparison,” with dual half-loop transport on states.

[CQ11] *The algebra of modes of a quantum vertex algebra*, “Modes on several points” and “The filtration by the number of points.” *Flatness and the rational deformation*, “Recovering creation and annihilation operators.” *The rational double in the algebra of modes*, the divided determinants and the rank-two mixed and same-half relations.

[CQ12] *The first Bocksteins and degree-three products of the exceptional universal W₄ vacuum*, §§2–6, and *The exceptional W₄ vacuum product in degrees seven and eight*, §§1–4. For the equivariant minimal model see *One quartic value decides formality with the marked diagram involution*. The polynomial vacuum complex and its special dimensions are those of [CQ8]. The geometric input at \(\tau=-3/2\) is the diagram action on the filtered Whittaker orbit coefficient and its two integrated rows. The four-insertion and two-sided-lift tests use the same marked vacuum endomorphism algebra. *The native exceptional W₄ quartic vanishes*, §§1–3, gives the coefficient-operator comparison, the translation ideal and the four-input calculation. The quartic calculation is dated 18 November 2026, 08:00:18.782514 WIB.
