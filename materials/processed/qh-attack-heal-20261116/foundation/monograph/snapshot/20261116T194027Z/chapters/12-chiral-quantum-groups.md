# Quantum groups and nonlinear chiral algebras

A current acting on two systems should act on their tensor product. For a Lie algebra this is expressed by
\[
\Delta(x)=x\otimes1+1\otimes x.
\]
For local currents, the same formula changes the central term. Suppose that two independent Heisenberg fields satisfy
\[
h_i(z)h_i(w)\sim\frac{\kappa_i}{(z-w)^2},\qquad i=1,2,
\]
and have no mixed singular products. Then \(h=h_1+h_2\) has level \(\kappa_1+\kappa_2\). Thus the natural map is
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

This calculation identifies the first requirements on a chiral quantum group. Its product must retain local singularities. Its coproduct must specify the tensor product of fields and the levels of its source and target. Their compatibility must survive iterated collisions. These requirements also explain why a dual algebra of ghosts, even when explicitly constructed, is only part of the question.

## Associative products on configurations

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

One such construction uses ordered configurations. Its coefficients are complexes on the configuration spaces and their collision strata. A convolution product, denoted \(\star\), concatenates ordered blocks and applies the specified geometric extensions from loci separating those blocks. Its unit \(K\) is supported on the empty configuration. A coefficient system is **positive** if its empty coefficient vanishes.

An **associative chiral algebra** in this setting is an augmented associative algebra \(A\) for \(\star\), with positive augmentation ideal, whose bar coalgebra \(BA\) factorizes. Factorization means that its cut coproduct is an equivalence to the external product on each designated separating open set. For word configurations these are consecutive cuts; the ordered collision category also permits ordered decompositions into subsets. The chosen category and cuts are part of the definition. [CQ1]

In a differential graded presentation, the associative structure can be described by an \(A_\infty\) structure: a differential, multiplication, homotopies relating triple products, and higher homotopies satisfying the Stasheff identities. This is the meaning of \(E_1\) here. With the cohomological convention \(V[1]^n=V^{n+1}\), its suspended operations on \(A[1]\) have degree one. The residue coalgebra \(C(V)\) of appropriate fields gives
\[
A_V=\Omega_{\mathrm{cut}}C(V).
\]
The cobar construction assembles the ordered collision terms and their differential into the associative object. Its empty algebra unit and the local field vacuum are different: the latter is a horizontal section of the one-point coefficient module, with a comparison to the original fields.

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

These associative structures should also be distinguished from Francis–Gaitsgory chiral Koszul duality. Their Chevalley chains relate Lie objects and cocommutative coalgebras for the chiral tensor on Ran space. Factorization corresponds to a Lie object supported on the one-point copy of \(X\). Restricting the coalgebra to ordered cuts and then taking associative cobar gives an associative chiral algebra. This uses Lie–commutative Koszul duality as an input; it does not identify it with associative bar–cobar duality, nor construct the additional chiral coproduct. [CQ1, CQ3]

## A spectral construction of products and coproducts

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

## Rational matrix fields and the full curved dual

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
describe creation and annihilation halves. Each obeys the relation \(\mathsf R X_1X_2=X_2X_1\mathsf R\), conventionally called an RTT relation. Their mixed relation at numerical level \(K\in\mathbb C\) is
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
At each precision and on fixed inputs the pole order is finite; one common bound for all precisions is not assumed. This all-order field comparison does not by itself give an equivalence of completed module categories. An intrinsic relation in a mode algebra also requires a proof before applying its representation on states. In particular, the normalized vacuum condition and the complete all-arity relation ideal matter in that question.

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

## Nonlinear fields: the \(W_3\) example

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

The normalized \(W_3\) chart inverts \(22+5c\). The regular universal presentation instead retains a spin-three generator \(U\) at every finite charge, including \(c=-22/5\). Its creation words remain linearly independent there. This distinction permits a separate curved bar construction at every charge.

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
\operatorname{CDGContra}(B_c):F_c,
\]
The free-on-degree-zero objects with smooth recovered action characterize \(\mathcal S_c\) exactly. For every pair of smooth modules, the iterated-continuous bar complex computes derived Hom and Yoneda composition. The localization making \(K_c,F_c\) inverse on the proposed larger derived categories remains a further problem. [CQ7]

## Exceptional \(W_4\) fibres and the algebra of extensions

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
Exactly two local torsion pairs, in degrees \((8,9)\) and \((11,12)\), account for the excess; their positive torsion exponents are undetermined. Products involving the extra classes and associative formality at these fibres remain open. The finite comparison and the protected top differential determine the displayed table, rather than a generic specialization argument. [CQ8]

The examples now supply several concrete pieces of the chiral quantum-group question: field products, an exchange-compatible level coproduct in the spectral class, nonlinear curved duals, and derived algebras of module extensions. None identifies an arbitrary category of physical lines with these objects. Such an identification must retain enough geometric information to recover the original collision operations. The next chapter asks precisely what that information is.

## References

[CQ1] *Associative chiral algebras*, sections “Factorization and the support of the cobar,” “Recovering the symmetric theory,” and “Coproducts, the second tensor and centres.”

[CQ2] *Coproducts from a spectral form*, sections “A form with a spectral parameter,” “The fields at a level,” and the tensor-product, coproduct and module-tensor theorems; *Chiral quantum groups: the constructed sector*, Definition “Spectral chiral quantum group” and Theorem “Consequences of the datum”; *Quantum vertex algebras as associative chiral algebras*, definition of a quantum vertex algebra with rational exchange.

[CQ3] J. Francis and D. Gaitsgory, [*Chiral Koszul duality*](https://arxiv.org/abs/1103.5803), Theorems 5.1.1 and 5.2.1. A. Beilinson and V. Drinfeld, *Chiral Algebras*, §§3.1 and 3.4–3.5.

[CQ4] *The rational affine comparison and its double*, creation–annihilation factorization and rational affine comparison theorems. P. Etingof and D. Kazhdan, [*Quantization of Lie bialgebras, V*](https://arxiv.org/abs/math/9808121), §§1–3. N. Jing, S. Kožić, A. Molev and F. Yang, [*Center of the quantum affine vertex algebra in type A*](https://arxiv.org/abs/1603.00237), Theorem 2.2 and §4.1.

[CQ5] *The Yang double of gl_n as a chiral quantum group*, regular dual-vacuum, exchange and full-curvature constructions, §§3–4 and the restricted cochain constructions.

[CQ6] *The dual of the W3 algebra*; *The curved dual of the W4 algebra*; *The ramified Miura parameter*, polynomial-form theorem; *Polynomial transposes and derivative corrections*, Theorem “General derivative-corrected transpose.”

[CQ7] *Curved duality for the regular universal W3 algebra*, Theorems 0.1–0.2 and §§3–6.

[CQ8] *The bulk of a principal W-algebra*, finite weight-zero comparison, generic formality, and §12, especially Theorems 12.3–12.6.
