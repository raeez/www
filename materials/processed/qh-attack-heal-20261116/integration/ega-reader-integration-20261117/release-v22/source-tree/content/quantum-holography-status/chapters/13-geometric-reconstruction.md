# Geometric reconstruction and rational examples

The coproduct in Chapter 12 tells us how to combine representations. How much of the field algebra could an observer recover by fusing and exchanging its sectors? An ordinary module of a conformal vertex algebra \(V\) has a diagonal energy operator \(L_0\), finite-dimensional energy spaces and a lower bound on the energy in each grading progression. Suppose the ordinary modules carry a ribbon tensor structure. Does this category \(\operatorname{Rep}^{\mathrm{ord}}(V)\) determine \(V\)? A **ribbon category** has dual objects, a braiding \(c_{M,N}:M\otimes N\to N\otimes M\), and a natural twist \(\theta_M:M\to M\). The twist satisfies
\[
\theta_{M\otimes N}
=c_{N,M}c_{M,N}(\theta_M\otimes\theta_N),\qquad
\theta_{M^\vee}=(\theta_M)^\vee,
\]
with \(\theta_{\mathbf1}=1\). The braiding satisfies the hexagons, and the evaluation and coevaluation maps satisfy the duality triangles.

Consider a positive-definite even integral lattice \(L\): a finite-rank free abelian group with integral symmetric pairing and \((\alpha,\alpha)\in2\mathbb Z\). Its lattice vertex algebra \(V_L\) is the direct sum of Heisenberg Fock spaces with charges \(\alpha\in L\). The irreducible ordinary modules are indexed by \(L^*/L\), where
\[
L^*=\{x\in L\otimes\mathbb R:(x,L)\subset\mathbb Z\}.
\]
When \(L\) is unimodular, \(L^*=L\), the vacuum is the only simple ordinary module. Its finite semisimple representation category is therefore the ribbon category of finite-dimensional vector spaces, with ordinary exchange and identity twist. The two even unimodular rank-sixteen lattices \(E_8\oplus E_8\) and \(D_{16}^{+}\) give this same category. Their vertex algebras have central charge sixteen and the same torus character, but their weight-one current Lie algebras are different:
\[
\mathfrak e_8\oplus\mathfrak e_8
\qquad\text{and}\qquad
\mathfrak{so}_{32}.
\]
Both have dimension \(496\), and their nondegenerate scalar pairings are isometric over \(\mathbb C\). The state-valued simple pole
\[
J^a(z)J^b(w)\sim
\frac{(a,b)}{(z-w)^2}+\frac{J^{[a,b]}(w)}{z-w}
\]
distinguishes them. Its residue is the bracket on the weight-one space \((V_L)_1\). Recovering that bracket requires the chiral product on the diagonal, even when the ribbon categories, characters and double-pole pairings agree. [GR1]

There is a way to observe this missing bracket. Keep the two insertion points as variables on a curve \(X\), let them approach one another, and record the vacuum coefficient through the collision. The ordinary geometric realization gives the full two-point coefficient \(B_{\{1,2\}}\) on \(X^2\), together with two identifications. Off the diagonal it is the external product of the one-point coefficients; on the diagonal it restricts to the one-point coefficient. Given sections in both incoming factors, the first identification places their polar product in this two-point extension, and the geometric residue followed by the diagonal identification gives a one-point field. This recovers the product on all such sections. In a finite rational category one can instead recover an algebra acting on the fusion channels. These reconstructions use different measurements of the vacuum.

## The realized vacuum on every configuration {#ch13-the-realized-vacuum-on-every-configuration}

Let \(X\) be a smooth separated complex algebraic curve. For every finite set \(I\), including the empty set, consider a category \(\mathcal C_I\) over \(X^I\). “Over” means that it has categories on parameter schemes \(T\to X^I\), linear over quasi-coherent \(\mathcal O_T\)-modules, with specified pullback functors and descent. If \(\pi:I\to J\) is a finite-set map, write
\[
\Delta_\pi:X^J\longrightarrow X^I,
\qquad (x_j)\longmapsto(x_{\pi(i)}).
\]
The system supplies functors
\[
\beta_\pi:\Delta_\pi^*\mathcal C_I\longrightarrow\mathcal C_J.
\]
For surjections these are collision equivalences. For injections they insert vacuum positions. On the open subset where different groups of points are separated, external fusion combines the corresponding categories. These functors come with comparison isomorphisms satisfying composition, permutation, partition, unit and base-change diagrams. External fusion of arbitrary module categories is not required to be an equivalence.

Set \(\mathcal C_\varnothing=\operatorname{Vect}_{\mathbb C}\). The vacuum at \(I\) is the object actually inserted from the empty set,
\[
v_I=\beta_{\varnothing\to I}(\mathbb C).
\]
A **geometric realization** consists of \(\mathcal O\)-linear functors
\[
F_I:\mathcal C_I\longrightarrow\operatorname{QCoh}(X^I)
\]
and comparisons with the finite-map functors and separated fusion. Here \(\operatorname{QCoh}\) denotes quasi-coherent sheaves. Define the realized vacuum coefficients
\[
B_I=F_I(v_I).
\]
Require their collision and separated-fusion comparisons to be isomorphisms, and require that \(B_I\) have no nonzero local sections supported on the diagonal divisor. Finally, the empty comparison must identify \(B_\varnothing\) with \(\mathbb C\) **as a unital algebra**. An identification of vector spaces alone does not fix the vacuum normalization.

These conditions give a factorization algebra \(B\). Its maps
\[
\Delta_\pi^*B_I\longrightarrow B_J,
\qquad
\left.\boxtimes_j B_{I_j}\right|_U
\longrightarrow B_I|_U
\]
are the images of actual categorical maps. The composition diagrams imply all their finite-set identities. At one position the vacuum gives a section, that is, a map \(\mathcal O_X\to B_{\{1\}}\). The other sections of \(B_{\{1\}}\) can still carry currents. At two positions the separated and collision identifications concern the entire sheaf \(B_{\{1,2\}}\). They act on sections carrying arbitrary incoming fields, including the two weight-one currents in the lattice example.

Beilinson–Drinfeld reconstruction supplies a canonical connection on \(B_{\{1\}}\) with horizontal vacuum. Put
\[
A:=\operatorname{Rec}(\mathcal C,F)
=\omega_X\otimes_{\mathcal O_X}B_{\{1\}},
\]
as a right differential module. Its chiral product is determined by the two-point extension \(B_{\{1,2\}}\). If \(j:X^2\setminus\Delta\hookrightarrow X^2\), the map is the composite
\[
\begin{aligned}
j_*j^*(A\boxtimes A)
&\longrightarrow
\bigl[j_*j^*(\omega_X\boxtimes\omega_X)\bigr]\otimes B_{\{1,2\}}\\
&\xrightarrow{\operatorname{Res}\otimes1}
(\Delta_*\omega_X)\otimes B_{\{1,2\}}
\longrightarrow\Delta_*A.
\end{aligned}
\]
The first arrow uses separated factorization; the last uses the collision comparison. Thus the extension across the diagonal enters the formula itself. For an iterated collision, both orders tensor geometric residues with the same coefficient \(B_I\). The finite-map and partition identities identify the two coefficient maps, so residue substitution gives every chiral operadic identity. On the affine line, translation equivariance gives the corresponding vertex algebra. A conformal vector is preserved when it is included in the input; it is not selected by an abstract tensor category. [GR1, GR2]

## The ordinary categorical round trip {#ch13-the-ordinary-categorical-round-trip}

The preceding reconstruction starts from a fully specified system. A separate theorem constructs that system from an ordinary chiral algebra, including its whole categories of modules.

**Theorem (ordinary classical reconstruction).** Fix an ordinary unital Beilinson–Drinfeld chiral algebra \(A\) on a smooth separated complex algebraic curve \(X\). For arbitrary classical parameter schemes \(T\to X^I\), its complete ordinary coefficient-family categories form a quasi-coherent-linear unital weak factorization system. They have categorical base change, coherent collision equivalences for every surjection, unit insertions, separated external fusion, and compatible evaluation on the minimal coefficient. The empty category is \(\operatorname{Vect}_{\mathbb C}\), and its inserted vacuum realizes \(\operatorname{Fact}(A)\), including the normalized empty algebra and all collision extensions. Consequently
\[
\operatorname{Rec}\bigl(\mathcal C(A),F\bigr)\cong A.
\]
All tensors are ordinary. Category tensors are taken among locally presentable complex-linear categories and cocontinuous functors; descent is Zariski. No flatness or finite-generation condition is imposed on action coefficient modules, and parameter schemes may be nonreduced or have coincident marked sections. [GR1, Theorem 9.1]

The objects here are complete families, not just modules at one fixed configuration. With original marks parameterized by \(T\), an object has coefficients on \(X^R\times T\) for every finite set \(R\) of additional positions. Differential operators act in those additional curve variables. The family includes normal collision identifications, permutations, units and separated factorization. The prohibition on diagonal-supported sections concerns diagonals involving an additional label; it does not exclude support on collisions among the original marked parameters. “Arbitrary coefficient modules” means modules carrying the required action, without a flatness restriction. It does not assert that every module admits such an action.

Changing the parameter scheme can merge two marks or introduce nilpotent directions. Tensoring with its new coefficient ring need not preserve a kernel. The unit makes the kernel needed for the action an exception. On \(T=\operatorname{Spec}B\), let \(D=\sum_i\Gamma_{x_i}\) be the sum of the marked graphs and \(j\) its complement. An action on \(M\) is a map
\[
\mu_M:E_D(M)=j_*j^*(A\boxtimes M)
\longrightarrow
G_D(M)=\bigl(\omega(*D)/\omega\bigr)\otimes_BM
\]
whose restriction along the chiral unit is the principal-parts quotient. Locally choose an affine open \(V\) containing the marked sections. Adding the graphs one at a time makes each successive principal-parts quotient a finite projective \(B\)-module. Their union \(Q=\Gamma(V_T,\omega(*D)/\omega)\) is projective. The unit therefore splits the action on these affine \(B\)-module sections:
\[
\Gamma(V_T,E_D(M))
\cong\Gamma(V_T,\ker\mu_M)\oplus(Q\otimes_BM).
\]
The splitting need not be linear over functions on the curve or over differential operators. It is used to prove that the **canonical** kernel comparison is invertible:
\[
B'\otimes_B\ker\mu_M
\xrightarrow{\sim}
\ker(B'\otimes_B\mu_M).
\]
That canonical map preserves the relative differential operators and glues. Successive kernels acquire the required actions, so the argument applies to every additional coefficient. Internal scalar actions then identify
\[
B'\text{-}\operatorname{Mod}
\otimes_{B\text{-}\operatorname{Mod}}\mathcal C_B
\simeq\mathcal C_{B'}.
\]
This is categorical scalar extension on objects and morphisms, rather than an equality checked only on the vacuum. The marked action/factorization-family equivalence of Rozenblyum and the coefficient reconstruction of Beilinson–Drinfeld complete the round trip. [GR1–GR3]

On the affine line, the principal-parts calculation can be seen directly. For the monic polynomial \(P(z)=\prod_i(z-t_i)\),
\[
B[z,P^{-1}]/B[z]
=\bigoplus_{n\ge1,\,0\le a<|I|}B\,[z^a/P^n].
\]
Monic division proves the formula without dividing by \(t_i-t_j\). Coincident points and nilpotents in \(B\) cause no failure of this argument.

The adjective “ordinary” remains essential. Consider the left differential module
\[
\delta_0=\mathbb C[s],\qquad
t=-\frac d{ds},\qquad\partial_t=s.
\]
Multiplication by \(t\) is surjective with one-dimensional kernel. Hence
\[
\mathbb C\otimes_{\mathbb C[t]}\delta_0=0,
\qquad
\operatorname{Tor}_1^{\mathbb C[t]}(\mathbb C,\delta_0)=\mathbb C.
\]
Ordinary and derived restriction differ even on this elementary coefficient. The theorem concerns a fixed \(A\) and classical parameters; it does not establish a derived or physical reconstruction, or a theorem for an arbitrary nonflat family in which \(A\) itself varies.

## Supported duality and the direction of comparison {#ch13-supported-duality-and-the-direction-of-comparison}

Another route begins with explicit coefficient systems for currents and exterior states. Let \(\kappa\) be the Heisenberg level, so that \([J_\lambda J]=\kappa\lambda\mathbf1\). Over \(R=\mathbb C[\kappa]\), let
\[
A_I=R[z_i:i\in I],\qquad
q_I(t)=\prod_{i\in I}(t-z_i),\qquad
P_I=A_I[t,q_I(t)^{-1}]/A_I[t].
\]
The module \(P_I\) retains principal parts at all marked roots. Form the independently defined symmetric and exterior coefficients
\[
F^+_{I,n}=\omega_{X^I}\otimes\operatorname{Sym}^nP_I,
\qquad
F^-_{I,n}=\omega_{X^I}\otimes\Lambda^nP_I.
\]
Their Cousin complexes \(\mathcal C^\pm_{I,n}\) place the coefficients on each collision stratum and retain the residue attachments between strata. In these complexes exterior states initially have degree zero; restoring their ghost degree uses the state-count shift \([-n]\). It is not a uniform shift of every configuration.

Multiplication by the Vandermonde in the auxiliary variables gives an integral coefficient isomorphism
\[
V_n:F^-_{I,n}\xrightarrow{\sim}F^+_{I,n}.
\]
It extends to the full Cousin complexes, their subcomplexes with positive state count at every block, and the corresponding vacuum quotients. Dualizing requires a specified topology. For a perfect right differential-module complex \(P\), use
\[
P^\sharp=\operatorname{RHom}_{D_{X^I/R}}
(P,D_{X^I/R})^t[|I|],
\qquad t(\partial_{z_i})=-\partial_{z_i}.
\]
For an increasing perfect presentation, retain the inverse system of these duals: a **pro-object**. Finite state, pole and normal-derivative data determine a finite stage; no common finite stage for all states is imposed.

**Theorem (supported Vandermonde pro-duality).** For every finite position set \(I\) and every state count \(n\),
\[
\Phi_{I,n}=V_n^\sharp:
(\mathcal C^+_{I,n})^\sharp
\xrightarrow{\sim}(\mathcal C^-_{I,n})^\sharp
\]
is an isomorphism of the full supported pro-diagrams and their dual vacuum triangles. It retains all finite normal derivatives and the spectator extension at three positions, and commutes with finite-stage numerical specialization of \(\kappa\). Its cut products are intertwined by the cross Vandermonde factors. [GR4]

The last qualification determines the product. On a cut with \(r\) auxiliary variables in the first group and \(s\) in the second, put
\[
C_{J|K}=\prod_{\alpha=1}^{r}\prod_{\beta=1}^{s}
(t_\alpha-t_{r+\beta}).
\]
The primal equation is
\[
\Delta^+V_{r+s}=(V_r\boxtimes V_s)C_{J|K}\Delta^-.
\]
Consequently the transposed product includes \(C_{J|K}^\sharp\). For three groups,
\[
C_{J|K}C_{J\cup K|L}
=C_{K|L}C_{J|K\cup L}:
\]
both sides contain precisely one oriented difference for every cross-group pair. This proves the cut associativity compatibility. Dropping the cross factors would preserve a vector-space comparison while changing its multiplication.

Duality also reverses the vacuum triangle. From a positive subcomplex \(\mathcal C^{>0}\), its ambient complex \(\mathcal C\), and quotient \(\mathcal Q\), it produces
\[
\mathcal Q^\sharp\longrightarrow
\mathcal C^\sharp\longrightarrow
(\mathcal C^{>0})^\sharp.
\]
A forward exterior field comparison with the original current operation needs additional endpoint maps. It must preserve both vacuum maps, the curvature marking, composite-state translations, and the collision joining positions 1 and 3 with position 2 separate.

There are precise obstructions to some such forward comparisons. With the original one-point evaluation and collision functor fixed, allowing arbitrary higher and negative target cohomology does not remove the degree obstruction. Occupied and mixed collisions require different suspensions. At \(\kappa\ne0\), the specified global regular product also gives the wrong marked curvature; this particular obstruction vanishes at \(\kappa=0\). Changed collision degrees or a changed product can support positive constructions, but require a comparison back to the original data. These statements leave the supported pro-duality intact and do not rule out every derived exterior realization. [GR5]

## Integrating the collision diagram {#ch13-integrating-the-collision-diagram}

Integration over an open curve asks what remains of a collision after taking its de Rham class. A rational multiplier can still depend on a third point, so taking the residue first and forgetting where the other inputs sit gives the wrong answer. An explicit algebra of configuration complexes retains this dependence, including when fields have nontrivial rational exchange.

Let \(R\) be a commutative algebra over a characteristic-zero field \(k\), and let \(U\subset\mathbb A^1_k\) be the complement of finitely many \(k\)-rational points. Take an ordinary \(R\)-flat state module \(V\) with vacuum spanning a free direct summand, translation, weakly associative fields and exact rational exchange on each finite tensor of states. The exchange satisfies unitarity, the shift identity, Yang–Baxter, field locality and the hexagon for crossing a product. Identity exchange recovers the ordinary vertex-algebra case. Use algebraic tensor products, finite normal derivatives on each element, and direct-sum totalizations. The Cousin coalgebra has a summand for every partition of a finite set \(I\). Its differential merges two blocks by the full principal part of their field product, expanding the multiplier in the normal coordinate as well. Determinant lines supply the signs.

Form the associative cobar, whose factors are words in the blocks, then take its de Rham, or Spencer, complex \(K(I)\). The Spencer differential contracts a tangent vector and applies the corresponding connection. For a surjection \(\alpha:I\twoheadrightarrow J\), exactly the partitions made of unions of its fibres survive the restriction to the collision diagonal. A tangent at \(j\) maps to \(\sum_{\alpha(i)=j}e_i\). Changing the order inside one word factor applies the corresponding exchanges on its labelled states. If the order of a colliding pair reverses, the full principal part must also be transferred to the new surviving coordinate. These maps commute with the cobar differential and with products for arbitrary pairs of surjections. The construction works over the original \(R\), including nilpotent parameters. [The rational exchange diagram](05-bar-and-coherence.md#ch05-rational-exchange-diagram)

The normalized simplicial replacement has one summand for each chain of surjections. A chain of length \(p\) lowers degree by \(p\). Adjoin the empty scalar summand separately and call the resulting differential graded algebra \(G_U(V)\). Its product is the signed shuffle of simplicial chains combined with concatenation of their coefficient words. [GR6]

The degree-zero answer is the intrinsic mode algebra
\[
H^0(G_U(V))\cong\mathsf M_U(V).
\]
Here \(\mathsf M_U(V)\) is formed from rational multipoint field coefficients modulo translation derivatives and the relations
\[
y-\sigma_i y-\rho_i y,
\]
in every arity. The map \(\sigma_i\) exchanges adjacent insertions with their state transport. The map \(\rho_i\) takes their collision residue, including Taylor transfer, and lowers arity. On \(U=\mathbb G_m\) one can see the spectator explicitly. Take three copies of the Heisenberg current \(J\), with \(J(v+u)J(v)\sim\kappa u^{-2}\mathbf1\), at \(v+u,v,w\). Multiply by \((v+u)^2/[vw(v-w)]\). The coefficient of \(u^{-1}\) is
\[
 \frac{2\kappa}{w(v-w)}\,\mathbf1\otimes J.
\]
Its iterated residue acting on the vacuum in \(|v|>|w|\) is \(2\kappa J\). Setting \(u=0\) in the multiplier before taking the residue would lose the whole term. Even with scalar vacuum fields the ideal generated using only two inputs can be strictly smaller than the all-arity ideal. [GR6]

There is a comparison on complexes, not only on their degree-zero quotients. Let \(\mathcal D=\bigoplus_n\mathcal D_n\) be the multipoint de Rham input algebra, and let \(\phi:\mathcal D\to G_U(V)\) place its inputs in the standard words of singletons. On \(\mathcal D_n\), the specified degree-minus-one maps satisfy
\[
dh_{n,i}+h_{n,i}d
=\phi(1-\widehat\sigma_i-\widehat\rho_i).
\]
The homotopy combines a word with one double factor, a contraction of nonsimple normal principal parts, a transposition edge, and a collision edge. Their boundary terms cancel. Adjoining these relation homotopies defines a differential graded algebra \(\mathcal P_U(V)\) and a map
\[
\Theta:\mathcal P_U(V)\longrightarrow G_U(V)
\]
which induces the identity on \(\mathsf M_U(V)\). To see that every degree-zero relation has been accounted for, list the blocks in the order of each singleton word. A degree-minus-one boundary comes from a Spencer tangent, one double letter, or a simplicial edge. Listing sends these to a translation derivative, the displayed exchange-minus-residue relation, or the same coefficient at both ends. Every singleton word arises from the standard one by a surjection. Listing thus defines an inverse on the quotient.

The target has an additive decomposition over the same coefficient ring,
\[
 G_U(V)\simeq R\oplus\bigoplus_{r\ge1}
                     (\mathcal D_r)_{\widehat\Sigma_r}.
\]
The subscript means coinvariants for the actual state exchange and the permutation of tangent vectors. To obtain the decomposition, transport every word to a common order of its roots. Word splitting then has the incidence signs of the permutohedron, and the coefficient of a merger depends only on its pair of blocks. Rational Eulerian projectors split this complex. In the cardinality-\(r\) quotient every nondiscrete partition has already arrived from a proper surjection. Only the discrete \(r\)-point coefficient survives in its Eulerian degree. Direct sums give the formula and degeneration of the cardinality spectral sequence at \(E_1\). Multiplication still has terms of smaller cardinality. Whether \(\Theta\) is a quasi-isomorphism in negative degrees is a question about its source as well.

An independent geometric comparison remains open. The Ran space parametrizes finite nonempty subsets of \(U\). To identify \(G_U(V)\) with a de Rham pushforward there, or with an integral using proper supports on an ordered configuration atlas, one needs a map carrying the actual attachments, support maps, product and marked vacuum across integration. Two failures help specify this requirement. On the ordered atlas, taking the free colimit of *all* expansion branches identifies one class \(x\) with a composite having two copies of \(x\). The relation \(x=2x\) kills the occupied vacuum along with every other positive-cardinality class. On \(\mathbb G_m\) the mode \([z^{-1};\mathbf1]\) survives. A different construction weights the configuration complex by its scalar dual. On \(\mathbb A^1\) its scalar singleton contributes the constant polynomial paired with constant-coefficient evaluation. This pair evaluates to one and gives a nonempty degree-zero class independent of the empty unit, whereas \(\mathsf M_{\mathbb A^1}(k)=k\). A geometric integral must preserve both the collision residue above and these unit distinctions.

## Finite rational categories and a non-scalar base {#ch13-finite-rational-categories-and-a-non-scalar-base}

Finite rational examples expose another reason why a reconstruction may require a different target category. For coprime integers \(2\le p<q\), put
\[
c_{p,q}=1-\frac{6(p-q)^2}{pq},\qquad
h_{r,s}=\frac{(qr-ps)^2-(p-q)^2}{4pq},
\]
with \(1\le r<p\), \(1\le s<q\), and \((r,s)\sim(p-r,q-s)\). Let \(\mathcal C_{p,q}\) be the category of finite direct sums of the simple modules \(L_i\) of the **simple** Virasoro minimal-model algebra. Its tensor product \(\boxtimes\) is represented by the full rational Ward problem, with the contragredient output at infinity, and has the usual ribbon structure. This category is smaller than the category of all modules of the universal Virasoro algebra. [GR7]

To glue two successive fusion channels, the output sector of one must equal the input sector of the next. Let \(I\) index the simple objects and put \(B=\mathbb C^I\), the algebra of functions on \(I\). Its idempotent \(e_j\) is the function supported on sector \(j\). If \(v=ve_j\) and \(w=e_k w\) have mismatched labels, their relative tensor satisfies \(v\otimes_Bw=v\otimes_B e_je_kw=0\). This explains why the following fibre functor keeps both end labels. Define
\[
F(M)=\bigoplus_{i,j\in I}
\operatorname{Hom}(L_i,M\boxtimes L_j).
\]
The \((i,j)\)-summand is the \((i,j)\)-component of a finite \(B\)-bimodule. Tensoring over \(B\) matches the intermediate label. For
\[
f:L_i\to M\boxtimes L_j,
\qquad g:L_j\to N\boxtimes L_k,
\]
the tensor comparison is composition with the associator:
\[
f\otimes g\longmapsto
a^{-1}_{M,N,L_k}(1_M\boxtimes g)f.
\]
Semisimplicity makes this comparison invertible, and the associator pentagon supplies its coherence. Thus \(F\) is exact, faithful and strong monoidal, with \(F(\mathbf1)=B\). The tensor unit is allowed to have several idempotents.

Writing \(V_a\) for the underlying vector space of \(F(L_a)\), reconstruction gives a finite weak Hopf algebra
\[
H=\bigoplus_{a\in I}\operatorname{End}_{\mathbb C}(V_a).
\]
The coproduct can be written using the tensor comparison \(J\). Let \(\pi\) project the ordinary tensor onto the relative tensor over \(B\), and let
\[
\iota(v\otimes_Bw)=\sum_i ve_i\otimes e_iw.
\]
Put \(m=J\pi\) and \(s=\iota J^{-1}\). If \(h_M\) denotes the natural action of \(h\) on \(F(M)\), then
\[
\Delta(h)_{M,N}=s_{M,N}h_{M\boxtimes N}m_{M,N},
\qquad
\varepsilon(h)=\lambda\!\left(h_{\mathbf1}\sum_i e_i\right),
\quad\lambda(e_i)=1.
\]
“Weak” refers to its unit and counit identities: the coproduct is coassociative and multiplicative, but \(\Delta(1)\) need not be \(1\otimes1\), and the scalar counit need not be multiplicative. The tensor of representations is
\[
\Delta(1)(V\otimes W),
\qquad
\Delta(1)=\sum_{i\in I}\rho_i\otimes\ell_i,
\]
where \(\rho_i,\ell_i\) are right and left actions of the idempotent \(e_i\in B\). This projection is exactly intermediate-label matching. The reconstruction preserves the ribbon structure and the finite pairing tensor. [GR7]

For the Ising model \((p,q)=(3,4)\), the simples \(1,\psi,\sigma\) satisfy
\[
\psi^2=1,\qquad\psi\sigma=\sigma,\qquad
\sigma^2=1+\psi.
\]
A faithful additive tensor functor to finite vector spaces with scalar unit would give positive integer dimensions with
\[
d_\psi^2=1,\qquad d_\sigma^2=1+d_\psi=2,
\]
which is impossible. The finite-base functor has no such problem. Its \(\sigma\)-bimodule has component dimensions
\[
\begin{pmatrix}
0&0&1\\
0&0&1\\
1&1&0
\end{pmatrix},
\]
so the ordinary vector dimensions of \(F(1),F(\psi),F(\sigma)\) are \(3,3,4\). Consequently
\[
H\cong\operatorname{Mat}_3(\mathbb C)
\oplus\operatorname{Mat}_3(\mathbb C)
\oplus\operatorname{Mat}_4(\mathbb C),
\qquad\dim H=34.
\]
The tensor projection on \(V_\sigma\otimes V_\sigma\) has rank six, matching the two three-dimensional summands of \(F(1\oplus\psi)\). A sixteen-dimensional ordinary tensor product would have forgotten the intermediate labels.

The finite-base construction works for every minimal model above. Except for \((2,3)\), a faithful finite vector-space fibre with scalar unit and multiplicative tensor isomorphisms is impossible even before coherence is imposed. At \((2,3)\), the reconstructed weak Hopf algebra is \(\mathbb C\). The simple-vacuum unit remains distinct from the ambient augmentation unit in the derived universal construction, including at this one-simple-object example. [GR7]

## Positive-integral affine fusion retains higher classes {#ch13-positive-integral-affine-fusion-retains-higher-classes}

An underived rational tensor product need not describe the derived operation from which it is obtained. Let \(\mathfrak g\) be simple, \(k\in\mathbb Z_{>0}\), and \(L(\lambda)\) its integrable affine modules indexed by
\[
P_k^+=\{\lambda\text{ dominant integral}:(\lambda,\theta)\le k\},
\]
where \(\theta\) is the highest root and long roots have squared length two. To define the derived operation, put \(\kappa=k+h^\vee\), with \(h^\vee\) the dual Coxeter number, and write \(\widehat{\mathfrak g}\) for the centrally extended loop algebra. Let \(\mathcal G_\kappa\) consist of smooth level-\(k\) affine modules with locally finite Sugawara operator \(L_0\), finite-dimensional generalized eigenspaces, and spectrum in finitely many sets \(h_i+\mathbb Z_{\ge0}\). Smoothness means that each vector is killed by \(t^N\mathfrak g[[t]]\) for some \(N\). Let \(\mathcal O_\kappa^+\) be its finitely generated objects on which \(\mathfrak g[[t]]\) acts locally finitely.

At distinct points \(p,q\), the ambient **fusion functor**
\[
\odot_{p,q}:\mathcal O_\kappa^+\times\mathcal O_\kappa^+
\longrightarrow\mathcal O_\kappa^+
\]
represents rational-current intertwining maps. More explicitly, \(\mathfrak g_{\{p,q\}}\) is the central extension of
\[
\mathfrak g\otimes\mathbb C[w,(w-p)^{-1},(w-q)^{-1}],
\]
with cocycle \((x,y)\sum_{s=p,q}\operatorname{Res}_{w=s}(g\,df)\) on \(x\otimes f,y\otimes g\). Write \(W(s)\) for the action obtained by Laurent expansion at \(s\), and \(\iota\) for expansion at the output point at infinity. For \(X\in\mathcal G_\kappa\), put \(\overline X=\prod_hX_{[h]}\), the product of its generalized energy spaces. The defining bijection is
\[
\operatorname{Hom}_{\widehat{\mathfrak g}}
(W_1\odot_{p,q}W_2,X)
\cong
\operatorname{Hom}_{\mathfrak g_{\{p,q\}}}
\bigl(W_1(p)\otimes W_2(q),\iota^*\overline X\bigr).
\]
This functor is right exact in each input. For the finite integrable inputs considered here, choose resolutions \(P_\bullet(W_i)\) by affine Weyl modules with finitely many finite-dimensional tops in each degree. These Weyl modules are induced from finite-dimensional \(\mathfrak g\)-modules, with positive currents acting by zero and the central element by \(k\). Define
\[
L_b\odot(W_1,W_2)
=H_b\!\left(\operatorname{Tot}
\bigl(P_\bullet(W_1)\odot_{p,q}P_\bullet(W_2)\bigr)\right).
\]
These are the left-derived functors of the ambient universal-affine fusion, with their level-\(k\) affine-module action. The derivation is taken before restricting to the semisimple simple-quotient category. The spectral product of differential graded modules is a separate construction related to this one by a comparison map. [GR8]

Let \(G\) be the simply connected compact group with complexified Lie algebra \(\mathfrak g\), and \(\Omega G\) its based loop space. For finite sums of the integrable inputs above, the higher fusion functors satisfy
\[
L_b\odot\bigl(L(\lambda),L(\mu)\bigr)
\cong
\bigoplus_{\nu\in P_k^+}
N_{\lambda\mu}^{\nu}L(\nu)
\otimes H_b(\Omega G;\mathbb C).
\]
The integers \(N_{\lambda\mu}^{\nu}\) are the Verlinde fusion multiplicities. The index \(b\) is homological; in the cohomological convention it contributes in degree \(-b\). [GR8]

The map to the simple vertex-algebra fusion product is the augmentation on the loop-homology factor. It is an isomorphism on loop degree zero and kills positive loop degree. Even with a simple-vacuum input, this map is not a quasi-isomorphism. For \(G=SU(2)\),
\[
H_\bullet(\Omega SU(2);\mathbb C)=\mathbb C[x],
\qquad |x|=2.
\]
The additional classes \(x,x^2,\ldots\) explain the failure directly. They belong to the derived ambient construction although the underived fusion category has its own tensor unit.

For exponents \(m_i\) of \(\mathfrak g\), the completed graded Grothendieck expression is
\[
a\star b=P(t)ab,
\qquad P(t)=\prod_i(1-t^{2m_i})^{-1}.
\]
Multiplying the simple-vacuum class by \(P(t)^{-1}\) gives a formal unit in that completed group. It does not construct a differential graded unit or multiplication on the entire loop-homology-enhanced object. Those require maps and associativity homotopies on the complexes themselves. Similarly, extending tensor comparisons across rational parameter walls requires integral lattices, specialization retaining higher Tor terms, and coherent reassociation on those lattices. Naive evaluation of a generic associator can fail at resonance. [GR8]

The residue between the separated factorization and diagonal collision isomorphisms reconstructs the chiral product of \(A\) as a morphism of right \(\mathcal D_{X^2}\)-modules. The finite-base fibre functor reconstructs the ribbon category \(\mathcal C_{p,q}\simeq\operatorname{Rep}(H)\) of a weak Hopf algebra. In the ambient universal affine category, the derived fusion \(L_b\odot\) also contains \(H_b(\Omega G;\mathbb C)\). A proposed open–closed correspondence must therefore specify which module category and which derived product carry the action of a bulk field.

## References {#ch13-references}

[GR1] *What a realized categorical vacuum reconstructs*, §§1–2 and Theorem 9.1, with the ordinary coefficient-family construction of §§6–11.

[GR2] A. Beilinson and V. Drinfeld, *Chiral Algebras*, Proposition 3.4.7, Theorem 3.4.9, and §§3.4.10–3.4.12.

[GR3] N. Rozenblyum, [*Modules Over a Chiral Algebra*](https://arxiv.org/abs/1010.1998), §§2–3 and Theorem 3.5.1.

[GR4] *The transposed Vandermonde comparison*, supported pro-duality theorem and the sections on cut products, operations and forward exterior contact.

[GR5] *Derived occupied vacua and the first collision square*; *A curvature obstruction for genuinely derived recipients*, fixed-evaluation curvature comparison; *A curvature-tuned product and its next failures*, separated product and collision conditions.

[GR6] *The symmetric Cousin coalgebra, its cobar words, and the all-surjection chain diagram*, Theorem D. *The integral over the Ran diagram*, Theorem E. *The arity filtration, its splitting, and the total cohomology*, Theorems F–G. *De Rham mode relations*, “A three-input boundary.” The rational-exchange construction uses full principal-part reversal together with the word and Spencer maps described above.

[GR7] *The quantum group of the Virasoro algebra, as an object*, rational Ward output and finite weak Hopf reconstruction, §§14–15.

[GR8] *Fusion for the affine family on the intended modules*, positive-integral higher fusion theorem, §5, and the noncritical tensor and specialization results of §8.
