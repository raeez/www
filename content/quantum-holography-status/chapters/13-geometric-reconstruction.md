# Geometric reconstruction and rational examples

The [rational crossing of two probes](12-chiral-quantum-groups.md#ch12-combined-probe-exchange) is a map between two ordered tensor products at separated spectral marks. Now let two fields approach one another on a smooth complex curve \(X\). Which field is left when the two insertions become one? In a local coordinate on \(X\), put the weight-one currents \(J^a,J^b\) of a level-one lattice theory at \(w+u,w\). Their labels belong to its weight-one Lie algebra, with invariant pairing \((\, ,\,)\). The singular part of their product is
\[
J^a(w+u)J^b(w)\sim
\frac{(a,b)\mathbf1}{u^2}+\frac{J^{[a,b]}(w)}{u}.
\]
To find out what the collision returns, multiply by a regular test function \(f(u)\) and take the coefficient of \(du/u\). Only the first two Taylor coefficients of \(f\) contribute to the residue.
\[
\operatorname{Res}_{u=0}f(u)J^a(w+u)J^b(w)\,du
=f(0)J^{[a,b]}(w)+f'(0)(a,b)\mathbf1.
\]
For a lattice with a root of squared length two, take opposite root vectors \(E,F\) with \((E,F)=1\), \([E,F]=H\) and \([H,E]=2E\). For this pair the test \(f=u\) returns the vacuum. The test \(f=1\) returns \(J^H\). Taking the simple pole of each output against a third current \(J^E\) gives zero for the vacuum and \(2J^E\) for \(J^H\). Thus the collision returns a state on which a further operation can act. How much of that operation can the fusion and exchange of the sectors determine? [Residues with a test function](#chiral-operation) · [The coproduct on field modules](#ch12-a-spectral-construction-of-products-and-coproducts)

For a conformal vertex algebra \(V\), take the sectors to be its ordinary modules. The energy operator \(L_0\) acts diagonally, with finite-dimensional energy spaces and a lower bound in each grading progression. Suppose these modules admit fusion, exchange, duals and a full twist making \(\operatorname{Rep}^{\mathrm{ord}}(V)\) a ribbon category.

**Definition (ribbon category).** A ribbon category is a rigid braided monoidal category with a twist compatible with duality. For objects \(M,N\), write \(c_{M,N}:M\otimes N\to N\otimes M\) for the exchange and \(\theta_M:M\to M\) for the natural twist. Write \(\mathbf1\) for the tensor unit and \(M^\vee\) for the dual of \(M\). The twist satisfies
\[
\theta_{M\otimes N}
=c_{N,M}c_{M,N}(\theta_M\otimes\theta_N),\qquad
\theta_{M^\vee}=(\theta_M)^\vee,
\]
with \(\theta_{\mathbf1}=1\). The braiding satisfies the hexagons, and the evaluation and coevaluation maps satisfy the duality triangles.

**Counterexample (two unimodular lattices).** Let \(L\) be a positive-definite even integral lattice. Its underlying abelian group is free of finite rank, its symmetric pairing is integral, and every squared length \((\alpha,\alpha)\) is even. The lattice vertex algebra \(V_L\) has a Heisenberg Fock space for each charge \(\alpha\in L\). Its irreducible ordinary modules are indexed by \(L^*/L\), where
\[
L^*=\{x\in L\otimes\mathbb R:(x,L)\subset\mathbb Z\}.
\]
For a unimodular lattice \(L^*=L\), so the vacuum is the only simple ordinary module. Every object in the finite semisimple category is a sum of copies of that unit. Fusion, exchange and twist then give the ribbon category of finite-dimensional complex vector spaces with its ordinary flip and identity twist.

Take \(L=E_8\oplus E_8\) and \(L=D_{16}^{+}\). Both give this category, central charge sixteen and the same torus character. In both theories weight one has dimension \(496\). The two nondegenerate complex pairings are isometric, so even the double-pole test can agree under an identification of the state spaces. Now take the simple-pole test on *all* pairs of weight-one states. It gives respectively
\[
\mathfrak e_8\oplus\mathfrak e_8
\qquad\text{and}\qquad
\mathfrak{so}_{32}.
\]
In the first algebra two nonzero commuting simple ideals exhaust the space. The second algebra is simple. An isomorphism preserving all the residues would transport the first decomposition to such a decomposition of the second. Thus the ribbon category, central charge, torus character and isometry class of the pairing together admit no reconstruction inverse on these two algebras. [Dong–Mason, Theorem 2, Lemma 2.1 and the proof at \(c=16\)](https://arxiv.org/pdf/math/0203005#page=2) · [GR1](#ref-ch13-gr1)

The missing datum lives where the positions coincide. On the complement of the diagonal in \(X^2\) the two fields belong to an external product. To take their residue as they meet, we need a sheaf on \(X^2\) extending that product and an identification of its coefficient on the diagonal with the one-point fields.

One differential on the affine line shows what such an extension retains. Put marks at \(0,t\) in a coordinate \(s\). The form \(\nu_t=ds/[s(s-t)]\) is defined for the whole family as a form with these allowed poles. At \(t\ne0\) and for a polynomial \(f\), the sum of the two residues is
\[
 \begin{aligned}
 &\operatorname{Res}_{s=0}f(s)\nu_t+\operatorname{Res}_{s=t}f(s)\nu_t\\
 &\qquad=\frac{f(t)-f(0)}{t}.
 \end{aligned}
\]
{#ch13-colliding-residues}
The right side is a polynomial in \(t\). At \(t=0\) it gives \(f'(0)\), exactly the residue of \(f(s)\,ds/s^2\) at the single remaining mark. Thus the tests \(1,s\) have values \(0,1\) throughout the family. The test \(s^2\) gives \(t\), so it also sees a first-order displacement over \(\mathbb C[t]/(t^2)\). In a chiral algebra this residue of differentials must still be applied with its *field* coefficient. Geometric realisation supplies that coefficient on every configuration. The [fusion channels of a finite rational category](#ch13-finite-rational-categories-and-a-non-scalar-base) give a second construction in which the algebra acts on the channels themselves.

## The realized vacuum on every configuration {#ch13-the-realized-vacuum-on-every-configuration}

Let \(X\) be a smooth separated complex algebraic curve. A point of \(X^I\) assigns a position to each label in the finite set \(I\). Coordinates may coincide. A map \(T\to X^I\) gives a family of these positions over a parameter scheme \(T\). For instance the family \(z_1=v+u,\ z_2=v\) on the affine line meets the diagonal at \(u=0\). Along such a family we need both the sectors at distinct points and the rule for bringing them together. [Configurations and partial diagonals](#configuration-spaces)

A unital weak factorization system supplies a category \(\mathcal C_I\) over each \(X^I\), including \(I=\varnothing\). Its categories on \(T\to X^I\) are linear over quasi-coherent \(\mathcal O_T\)-modules and come with pullback functors and descent. If \(\pi:I\to J\) is a finite-set map, write
\[
\Delta_\pi:X^J\longrightarrow X^I,
\qquad (x_j)\longmapsto(x_{\pi(i)}).
\]
For example take \(I=\{1,2,3\}\) and send \(1,3\) to \(a\) and \(2\) to \(b\). The map on spaces takes \((v,w)\) to \((v,w,v)\). A family on the three-position space can be pulled back along this map even when \(v=w\). To identify the resulting family with one on the two remaining labels, the system supplies functors
\[
\beta_\pi:\Delta_\pi^*\mathcal C_I\longrightarrow\mathcal C_J.
\]
A surjection identifies labels in each fibre \(I_j=\pi^{-1}(j)\). Its functor is a collision equivalence. An injection adds the missing labels as vacuum positions. For a partition \(I=\coprod_j I_j\), let \(U\subset X^I\) be the open set where points in different blocks are distinct. On \(U\) external fusion combines the categories belonging to the blocks. Thus for \(I_1=\{1,3\}, I_2=\{2\}\), positions 1 and 3 may coincide while position 2 stays separate. These functors come with comparison isomorphisms satisfying composition, permutation, partition, unit and base-change diagrams. External fusion of arbitrary module categories is not required to be an equivalence.

Set \(\mathcal C_\varnothing=\operatorname{Vect}_{\mathbb C}\). The vacuum at \(I\) is the object actually inserted from the empty set,
\[
v_I=\beta_{\varnothing\to I}(\mathbb C).
\]
**Definition (geometric realization).** A geometric realization of the vacuum-marked system consists of \(\mathcal O\)-linear functors
\[
F_I:\mathcal C_I\longrightarrow\operatorname{QCoh}(X^I)
\]
and comparisons with the finite-map functors and separated fusion. Here \(\operatorname{QCoh}\) denotes quasi-coherent sheaves. Define the realized vacuum coefficients
\[
B_I=F_I(v_I).
\]
Require their collision and separated-fusion comparisons to be isomorphisms, and require that \(B_I\) have no nonzero local sections supported on the diagonal divisor. Finally, the empty comparison must identify \(B_\varnothing\) with \(\mathbb C\) **as a unital algebra**. To see the scale this fixes, take the trivial coefficients \(B_I=\mathcal O_{X^I}\) and give a section \(a\) the new coordinate \(2^{|I|-1}a\). At the empty set, coordinates \(x,y\) thus represent the old scalars \(2x,2y\). Their product has new coordinate \(\tfrac12(2x)(2y)=2xy\), so its unit has coordinate \(1/2\). At one point the coordinate is unchanged. Insertion therefore sends \(x\) to \(2x\) and carries the empty algebra unit to the vacuum \(1\). Inserting the vector with coordinate \(1\) would instead give \(2\). [GR1](#ref-ch13-gr1)

These conditions give a factorization algebra \(B\). Its maps
\[
\Delta_\pi^*B_I\longrightarrow B_J,
\qquad
\left.\boxtimes_j B_{I_j}\right|_U
\longrightarrow B_I|_U
\]
are the images of actual categorical maps. The composition diagrams imply all their finite-set identities. At one position the vacuum gives a section, that is, a map \(\mathcal O_X\to B_{\{1\}}\). The other sections of \(B_{\{1\}}\) can still carry currents. At two positions the separated and collision identifications concern the entire sheaf \(B_{\{1,2\}}\). They act on sections carrying arbitrary incoming fields, including the two weight-one currents in the lattice example.

A current also has a derivative along the curve. To recover it, insert the vacuum beside a section of \(B_{\{1\}}\), first on its left and then on its right. Near the diagonal this compares the pullbacks of the section from the two positions. The first-order difference gives its covariant derivative. The comparisons agree under composition at three infinitesimally close positions, so they give the canonical integrable connection of Beilinson and Drinfeld. The vacuum section is horizontal. Put
\[
A:=\operatorname{Rec}(\mathcal C,F)
=\omega_X\otimes_{\mathcal O_X}B_{\{1\}},
\]
where \(\omega_X\) is the line of one-forms on \(X\). Tensoring by this line turns the coefficient with its connection into a right \(\mathcal D_X\)-module. Let \(\Delta:X\hookrightarrow X^2\) be the diagonal embedding and \(j:X^2\setminus\Delta(X)\hookrightarrow X^2\) the complementary open immersion. The chiral product is the following map of right \(\mathcal D_{X^2}\)-modules
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
The first arrow places the two incoming fields in the separated coefficient. The residue is a distribution on the diagonal, where the last arrow identifies the surviving coefficient with \(B_{\{1\}}\). With normal coordinate \(u=z-w\), its value on a double pole tested against \(f(u)\) is \(f'(0)\). The scalar and current terms of the lattice product therefore land in the same one-point module with their distinct normal orders intact. For an iterated collision, both orders tensor geometric residues with the same coefficient \(B_I\). The finite-map and partition identities identify the two coefficient maps, so residue substitution gives every chiral operadic identity. On the affine line, translation equivariance gives the corresponding vertex algebra. A specified conformal vector and compatible grading are carried through this construction. [GR1](#ref-ch13-gr1) · [GR2](#ref-ch13-gr2)

## The ordinary categorical round trip {#ch13-the-ordinary-categorical-round-trip}

Start instead with a unital chiral algebra \(A\) and a module at one marked point. Away from the mark a second insertion gives an independent field of \(A\). At the mark its pole acts on the module. A family of modules must supply a coefficient on which both operations make sense as the added point moves. For several original marks \(x_i:T\to X\), the same requirement applies even over parameters where two of the marks coincide.

**Definition (ordinary coefficient family).** Write \(\operatorname{Fact}(A)\) for the ordinary factorization algebra corresponding to \(A\) under the Beilinson–Drinfeld equivalence. Over \(T\to X^I\) a complete family has a quasi-coherent left \(\mathcal D_{X^R\times T/T}\)-module \(M_R\) for each finite set \(R\) of added positions. Thus only the added curve variables carry differential operators. The minimal coefficient \(M_\varnothing\) is a quasi-coherent \(\mathcal O_T\)-module. The realization functor \(F\) evaluates the family on this coefficient.

Where the \(S\)-positions are disjoint from the \(R\)-positions and all original marks, the family has an isomorphism \(\operatorname{Fact}(A)_S\boxtimes M_R\simeq M_{S\sqcup R}\). It has ordinary restriction isomorphisms for collisions fixing the original labels, permutation maps and normalized unit insertions. These maps commute with one another and with refining a partition or composing collisions. No \(M_R\) has a nonzero local section supported on the union of diagonals involving an added label. The minimal coefficient may be supported where the original marks coincide.

**Theorem (ordinary classical reconstruction).** Fix an ordinary unital Beilinson–Drinfeld chiral algebra \(A\) on a smooth separated complex algebraic curve \(X\). For arbitrary classical parameter schemes \(T\to X^I\), its complete ordinary coefficient-family categories form a quasi-coherent-linear unital weak factorization system. They have categorical base change, coherent collision equivalences for every surjection, unit insertions, separated external fusion, and compatible evaluation on the minimal coefficient. The empty category is \(\operatorname{Vect}_{\mathbb C}\), and its inserted vacuum realizes \(\operatorname{Fact}(A)\), including the normalized empty algebra and all collision extensions. Consequently
\[
\operatorname{Rec}\bigl(\mathcal C(A),F\bigr)\cong A.
\]
All tensors are ordinary. Category tensors are taken among locally presentable complex-linear categories and cocontinuous functors; descent is Zariski. No flatness or finite-generation condition is imposed on action coefficient modules, and parameter schemes may be nonreduced or have coincident marked sections. [GR1, Theorem 9.1](#ref-ch13-gr1)

Return to the [two colliding marks](#ch13-colliding-residues), now \(0,\epsilon\) over \(B=\mathbb C[\epsilon]/(\epsilon^2)\). Their pole divisor is cut out by the monic polynomial \(P(z)=z(z-\epsilon)\). Partial fractions at the individual points would require division by \(\epsilon\). In the localisation at \(P\) one can instead write \(1/P=z^{-2}+\epsilon z^{-3}\). The extra term has residue \(\epsilon\) against \(z^2\,dz\). The two principal parts \(1/P,z/P\) specialise directly to \(z^{-2},z^{-1}\) when \(\epsilon=0\). To recover the coefficient of an added point we also need the *kernel* of its action to specialise correctly. Tensoring with its new coefficient ring need not preserve a kernel. The unit makes the kernel needed for the action an exception. On \(T=\operatorname{Spec}B\), let \(D=\sum_i\Gamma_{x_i}\) be the sum of the marked graphs and \(j\) its complement. A marked chiral action on a \(B\)-module \(M\) is a relative \(\mathcal D_{X\times T/T}\)-linear map
\[
\mu_M:E_D(M)=j_*j^*(A\boxtimes M)
\longrightarrow
G_D(M)=\bigl(\omega(*D)/\omega\bigr)\otimes_BM
\]
satisfying the following two identities. Along the chiral unit \(\omega\to A\), the action is the quotient taking a polar one-form to its principal part. Here \(\omega=\omega_{X\times T/T}\), so the quotient forgets precisely the regular forms. For the Lie-action identity, label the two fields \(1,2\) and the marked coefficient \(3\). Write \(\mu_{1,\{2,3\}}\) for acting first with field \(2\) and then with field \(1\), and \(\mu_{2,\{1,3\}}\) for the map obtained by transposing the fields. In Rozenblyum’s right differential-module convention, acting by their bracket gives \(\mu_{\{1,2\},3}=\mu_{2,\{1,3\}}-\mu_{1,\{2,3\}}\). [Rozenblyum’s unit and Lie-action diagrams](#ref-ch13-gr3)

The unit condition already gives the splitting. Locally on \(T\) choose an affine \(V\subset X\) containing the marked sections. Put \(V_T=V\times T\). Adding a single graph increases the allowed pole divisor. The quotient of the two successive sheaves of forms is a line on that graph, hence has projective \(B\)-module of sections. Iterating over the graphs and pole orders gives a split filtration over \(B\), so its union \(Q=\Gamma(V_T,\omega(*D)/\omega)\) is projective. Lifting its sections to polar forms and applying the chiral unit splits the action on affine \(B\)-module sections
\[
\Gamma(V_T,E_D(M))
\cong\Gamma(V_T,\ker\mu_M)\oplus(Q\otimes_BM).
\]
**Lemma (base change for the action kernel).** For every homomorphism \(B\to B'\), the canonical comparison
\[
B'\otimes_B\ker\mu_M
\xrightarrow{\sim}
\ker(B'\otimes_B\mu_M)
\]
is an isomorphism.

**Proof.** On affine sections the preceding \(B\)-linear splitting exhibits the kernel as a direct summand. Tensoring preserves this split sequence for every \(B'\). The resulting canonical map commutes with the relative differential operators and glues, even though the chosen splitting need only be \(B\)-linear. ∎

On adding a point, the right-module kernel \(K=\ker\mu_M\) gives the left coefficient \(\omega^{-1}\otimes K\). What happens when the new point meets a marked section \(s:T\to X\)? Write \(i:T\hookrightarrow X\times T\) for its graph and \(p:X\times T\to T\) for the projection. Put \(W=\omega\otimes p^*M\). Applying the chiral unit to polar forms gives a map from the first exact sequence to the second,
\[
\begin{aligned}
0&\longrightarrow W\longrightarrow W(*D)\longrightarrow G_D(M)\longrightarrow0,\\
0&\longrightarrow K\longrightarrow E_D(M)\xrightarrow{\mu_M}G_D(M)\longrightarrow0.
\end{aligned}
\]
The unit condition says that the map on the common target \(G_D(M)\) is the identity. Let \(f\) be a local equation for the marked graph. Both middle terms allow poles along that graph, so multiplication by \(f\) is invertible on them. If \(f g=0\) in \(G_D(M)\), lift \(g\) to the middle term of either row and multiply the lift by \(f\). Its class in the first term modulo \(f\) is independent of the lift. Division by \(f\) in the middle term gives the inverse construction. Thus the two rows identify the same submodule of \(G_D(M)\), the elements killed by \(f\), with \(W/fW\) and \(K/fK\), respectively. The unit carries the first identification to the second. Multiplication by \(f\) is injective on both kernels, so their restrictions to the graph have no higher normal Tor.

It follows that \(i^*K\simeq i^*W=s^*\omega_X\otimes M\). The inverse canonical line in the left coefficient cancels \(s^*\omega_X\), recovering precisely \(M\). For \(T=X=\mathbb P^1\), \(A=\omega_X\), the diagonal graph and \(M=\mathcal O_X\), the raw kernel restricts to \(\mathcal O(-2)\). Tensoring by its inverse gives \(\mathcal O_X\). [GR1, Lemma 11.1](#ref-ch13-gr1)

The module Jacobi identity makes the induced action preserve each successive kernel. Thus adding a point commutes with extension of scalars at every stage. Write \(\mathcal C_B\) for the category of marked actions over \(B\). To give such an action a \(B'\)-module structure is to let each new scalar commute with the action map \(\mu_M\). Its source and its principal-parts target then have their defining descriptions over \(B'\). Morphisms obey the same commutation rule. In the category of locally presentable linear categories this gives
\[
B'\text{-}\operatorname{Mod}
\otimes_{B\text{-}\operatorname{Mod}}\mathcal C_B
\simeq\mathcal C_{B'}.
\]
With no marked points the principal-parts target of the action is zero. A vector space then has a unique action. Under Rozenblyum's equivalence its coefficient at extra positions \(R\) is \(\operatorname{Fact}(A)_R\) tensored with that vector space. Taking the empty unit \(\mathbb C\) gives the regular family itself. When the positions \(I\) become marks, its minimal coefficient is therefore \(F_I(v_I)=\operatorname{Fact}(A)_I\), with the original separated and collision maps. Their Beilinson–Drinfeld residue recovers the chiral product of \(A\). [GR1](#ref-ch13-gr1) · [GR2](#ref-ch13-gr2) · [GR3](#ref-ch13-gr3)

The two specializations above are the first terms of a basis. On the affine line, take a nonempty set \(I\) of marks \(t_i\in B\). For the monic polynomial \(P(z)=\prod_i(z-t_i)\),
\[
B[z,P^{-1}]/B[z]
=\bigoplus_{n\ge1,\,0\le a<|I|}B\,[z^a/P^n].
\]
Monic division proves the formula without dividing by \(t_i-t_j\). Coincident points and nilpotents in \(B\) cause no failure of this argument.

**Example (derived restriction at a point).** For the closed point \(t=0\) on the affine line, a free resolution of its residue field is multiplication by \(t\) between two copies of \(\mathbb C[t]\). Tensor it with the left differential module
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

The principal parts in the preceding affine example also occur in a comparison of symmetric and exterior states. Two polar factors may sit at a single marked point. Exchanging the factors then has a sign on the exterior states, even though their position has stayed fixed. For the Heisenberg field \(J\) with \([J_\lambda J]=\kappa\lambda\mathbf1\), keep the level as a parameter and take \(X=\mathbb A^1_R\) over \(R=\mathbb C[\kappa]\). Denote the marked positions by \(z_i\) and the variable of a principal part by \(t\). For a nonempty label set \(I\), put
\[
\begin{aligned}
 A_I&=R[z_i:i\in I],\\
 q_I(t)&=\prod_{i\in I}(t-z_i),\\
 P_I&=A_I[t,q_I(t)^{-1}]/A_I[t].
\end{aligned}
\]
In \(P_I\) two rational functions with poles at the marked roots give the same principal part if they differ by a polynomial in \(t\). The position count \(|I|\) and the number \(n\) of polar factors are independent. Form the symmetric and exterior coefficients over \(A_I\)
\[
F^+_{I,n}=\omega_{X^I}\otimes\operatorname{Sym}^nP_I,
\qquad
F^-_{I,n}=\omega_{X^I}\otimes\Lambda^nP_I.
\]
Their Cousin complexes \(\mathcal C^\pm_{I,n}\) place these coefficients on the collision strata. The differential retains the residue maps between strata with zero central contractions. At the empty set take \(R\) for \(n=0\) and zero for \(n>0\). The exterior states here have degree zero. To restore ghost degrees, shift the primal complex by \([-n]\) and its dual by \([n]\).

At one position \(z\) write \(p_j=[(t-z)^{-j-1}]\) for \(j\ge0\). Multiplication by \(t-z\) sends \(p_1\) to \(p_0\) and \(p_0\) to zero. Thus \(t_1-t_2\) sends the averaged alternating tensor \((p_1\otimes p_0-p_0\otimes p_1)/2\) to \(p_0\otimes p_0\). In \(n\) auxiliary variables the alternating multiplier is \(\prod_{\alpha<\beta}(t_\alpha-t_\beta)\).

On this affine line, for the principal parts of one Heisenberg current, multiplication by the Vandermonde in the auxiliary variables gives an integral coefficient isomorphism
\[
V_n:F^-_{I,n}\xrightarrow{\sim}F^+_{I,n}.
\]
For the differential with zero central contractions, it extends to the full Cousin complexes, their subcomplexes with positive state count at every block, and the corresponding vacuum quotients. Dualizing requires a specified topology. For a perfect right differential-module complex \(P\), use
\[
P^\sharp=\operatorname{RHom}_{D_{X^I/R}}
(P,D_{X^I/R})^t[|I|],
\qquad t(\partial_{z_i})=-\partial_{z_i}.
\]
For an increasing perfect presentation, retain the inverse system of these duals: a **pro-object**. Finite state, pole and normal-derivative data determine a finite stage; no common finite stage for all states is imposed.

**Theorem (supported Vandermonde pro-duality).** For one Heisenberg current on the affine line with a chosen coordinate, use the Cousin differential with zero central contractions. For every finite position set \(I\) and every number \(n\) of polar factors,
\[
\Phi_{I,n}=V_n^\sharp:
(\mathcal C^+_{I,n})^\sharp
\xrightarrow{\sim}(\mathcal C^-_{I,n})^\sharp
\]
is an isomorphism of the full supported pro-diagrams and their dual vacuum triangles. It retains all finite normal derivatives and the spectator extension at three positions, and commutes with finite-stage numerical specialization of \(\kappa\). Its cut products are intertwined by the cross Vandermonde factors. [GR4](#ref-ch13-gr4)

The last qualification determines the product. Cut the positions into \(I=J\sqcup K\) and separate the two groups on \(U_{J,K}\). Partial fractions give \(P_I=P_J\oplus P_K\) there, with each summand pulled back to the open set. The component \(\Delta^\pm\) of the cut selects \(r\) polar factors over \(J\) and \(s\) over \(K\), where \(r+s=n\). Its target is the external coefficient on this open set pushed forward to \(X^I\). The source of the transposed product is the pro-dual of that entire localized coefficient, including the pole orders at the omitted diagonals. In the order \(J,K\), put
\[
C_{J|K}=\prod_{\alpha=1}^{r}\prod_{\beta=1}^{s}
(t_\alpha-t_{r+\beta}).
\]
The primal equation is
\[
\Delta^+V_{r+s}=(V_r\boxtimes V_s)C_{J|K}\Delta^-.
\]
For a cut with one polar factor on each side, the two internal Vandermondes are both \(1\). The entire multiplier \(t_1-t_2\) is therefore a cross factor. For three singleton groups, take auxiliary values \(1,3,6\). Splitting off the last group gives \((1-3)(1-6)(3-6)=-30\). Splitting off the first gives \((3-6)(1-3)(1-6)=-30\). For a general cut, transpose the primal equation from right to left. On the symmetric side the transposed cut starts at the dual of the localized external coefficient and lands in the dual of the uncut coefficient. On the exterior side the same composite first applies \((V_r\boxtimes V_s)^\sharp\), then \(C_{J|K}^\sharp\), then the transposed exterior cut. For three groups,
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
A comparison in the opposite direction would have to send exterior states to the original current operation. In particular it must carry an insertion of the vacuum and its subsequent collision to their prescribed one-point maps. It must also carry the curvature, translations of composite states, and the collision of positions 1 and 3 in the presence of a separate position 2.

::: figure fig-supported-vandermonde-directions

Insert an empty position beside one carrying a state. For the ordinary vacuum coefficient, extraordinary restriction \(i^!\) to the diagonal has its sole normal cohomology in degree one. The occupied branch of the proposed pro-dual coefficient already has cohomology in degree one before restriction. Its surviving group on the diagonal lies in degree two, so recovering the original one-point state from this branch takes \(i^![2]\).

To see both degrees, suppress the tangential state and write \(u=z_1-z_2\), \(p=\partial_u\). On the ordinary density the normal differential is multiplication by \(u\) on polynomials in \(u\). It is injective and leaves the constant coefficient in degree one. On the occupied branch the intrinsic differential first multiplies by \(\pm p\) on the left. In the normal order \(p^b u^a\) its cokernel consists of polynomials in \(u\) in degree one. The remaining normal differential multiplies by \(u\) up to sign, so the surviving constant now has degree two.

For the mixed binary coefficient that gives the Taylor and curvature terms, the normal complex has an injective differential and its cokernel is in degree one. That comparison takes \(i^![1]\). No single shift gives both prescribed maps. With the one-point evaluation and collision functor fixed, allowing further cohomology in the target does not change the obstruction. At \(\kappa\ne0\) the specified global regular product also gives the wrong marked curvature. At \(\kappa=0\) this curvature obstruction disappears. A different collision degree or product requires a new comparison with the original one-point maps. [GR5](#ref-ch13-gr5)

**Open problem (the forward exterior contact).** At two positions write \(U\to V\to W\xrightarrow{\epsilon}U[1]\) for the reversed exterior pro-dual triangle above. Can one construct a triangle \(G'\to G\to G''\xrightarrow{g}G'[1]\) for the original regular exterior contact, together with continuous endpoint maps \(f:U\to G'\) and \(h:W\to G''\) such that \(f[1]\epsilon\simeq gh\)? The homotopy must respect the transitions on composite states, both vacuum maps, the original scalar contact and the cuts. At three positions it must retain the collision of positions 1 and 3 with position 2 separate. [The reversed comparison](#ch13-theorem-supported-vandermonde-pro-duality) · [The forward comparison and its hypotheses](#ref-ch13-gr5)

## Integrating the collision diagram {#ch13-integrating-the-collision-diagram}

On the punctured affine line put three Heisenberg currents \(J\) at \(v+u,v,w\). Multiply their product by \((v+u)^2/[vw(v-w)]\). As the first pair collides, its double pole \(\kappa/u^2\) differentiates the multiplier at \(u=0\). Expanding \(v^2+2vu+u^2\) gives the surviving two-point coefficient
\[
 \frac{2\kappa}{w(v-w)}\,\mathbf1\otimes J.
\]
For \(|v|>|w|\), expand \(1/(v-w)=\sum_{j\ge0}w^jv^{-j-1}\). The \(v^{-1}\) term leaves \(2\kappa J(w)/w\). Acting on the vacuum and taking the \(w\)-residue returns \(2\kappa J\). Substituting \(u=0\) before taking the first residue would lose the \(2vu\) term altogether. An integral of several fields must keep the surviving positions, the whole principal part at each collision and, for fields with nontrivial exchange, the order in which the inputs reach it. [GR6](#ref-ch13-gr6)

Let \(R\) be a commutative algebra over a characteristic-zero field \(k\), and let \(U\subset\mathbb A^1_k\) be the complement of finitely many \(k\)-rational points. Take an ordinary \(R\)-flat state module \(V\) with vacuum spanning a free direct summand, translation, weakly associative fields and exact rational exchange on each finite tensor of states. The exchange satisfies unitarity, the shift identity, Yang–Baxter, field locality and the hexagon for crossing a product. Identity exchange recovers the ordinary vertex-algebra case. Use algebraic tensor products, finite normal derivatives on each element, and direct-sum totalizations. The Cousin coalgebra has a summand for every partition of a finite set \(I\). Its differential merges two blocks by the full principal part of their field product, expanding the multiplier in the normal coordinate as well. Determinant lines supply the signs.

Form the associative cobar, whose factors are words in the blocks, then take its de Rham, or Spencer, complex \(K(I)\). The Spencer differential contracts a tangent vector and applies the corresponding connection. For a surjection \(\alpha:I\twoheadrightarrow J\), the map \(K(J)\to K(I)\) places a coefficient on the diagonal where coordinates with the same image coincide. The partitions of \(I\) that occur are precisely those whose blocks are unions of fibres of \(\alpha\). On Spencer tangents the map sends \(e_j\) to \(\sum_{\alpha(i)=j}e_i\). For example the direction moving the first and third marks together maps to \(e_1+e_3\), while the spectator direction maps to \(e_2\). Changing the order inside one word factor applies the corresponding exchanges on its labelled states. If the order of a colliding pair reverses, the full principal part must also be transferred to the new surviving coordinate. These maps commute with the cobar differential and with products for arbitrary pairs of surjections. The construction works over the original \(R\), including nilpotent parameters. [The rational exchange diagram](05-bar-and-coherence.md#ch05-rational-exchange-diagram)

The normalized simplicial replacement has one summand for each chain of surjections. A chain of length \(p\) lowers degree by \(p\). Adjoin the empty scalar summand separately and call the resulting differential graded algebra \(G_U(V)\). Its product is the signed shuffle of simplicial chains combined with concatenation of their coefficient words. [GR6](#ref-ch13-gr6)

Form the mode algebra \(\mathsf M_U(V)\) from rational multipoint field coefficients modulo translation derivatives and the relations
\[
y-\sigma_i y-\rho_i y,
\]
in every arity. The map \(\sigma_i\) exchanges adjacent insertions with their state transport. The map \(\rho_i\) takes their collision residue, including Taylor transfer, and lowers arity.

**Theorem (degree-zero mode algebra).** For the stated rational exchange and direct-sum totalization, placing the labelled inputs in their standard order induces
\[
 \mathsf M_U(V)\xrightarrow{\ \sim\ }H^0(G_U(V)).
\]

The collision term \(\rho_i y\) can thus still have a pole involving a spectator, as \(2\kappa/[w(v-w)]\) did above. Even for scalar vacuum fields, the ideal generated using only two inputs can be strictly smaller than the all-arity ideal. To prove the theorem one must realize a defining relation as a boundary with the other inputs present. [GR6](#ref-ch13-gr6)

Before passing to cohomology, exchanging two neighbours and taking their collision give chain maps \(\widehat\sigma_i,\widehat\rho_i\). The exchange transports the labelled states and their tangent vectors. The collision takes the residue of the full Taylor-expanded input and retains the tangent along the surviving point. Write \(\mathcal D_n\) for the de Rham complex of the \(n\)-point inputs and \(\mathcal D=\bigoplus_n\mathcal D_n\) for their algebra. Let \(\phi:\mathcal D\to G_U(V)\) place the inputs in the standard word of singletons. The difference that defines the mode relation is the boundary of a degree-minus-one homotopy \(h_{n,i}\) on \(\mathcal D_n\),
\[
dh_{n,i}+h_{n,i}d
=\phi(1-\widehat\sigma_i-\widehat\rho_i).
\]
The homotopy combines a word with one double factor, a contraction of nonsimple normal principal parts, a transposition edge, and a collision edge. Their boundary terms cancel. Adjoining these relation homotopies defines a differential graded algebra \(\mathcal P_U(V)\) and a map
\[
\Theta:\mathcal P_U(V)\longrightarrow G_U(V)
\]
which induces the identity on \(\mathsf M_U(V)\) in degree zero. To see the inverse, list the blocks of a singleton word in the order in which they occur. A boundary reaching degree zero comes from one Spencer tangent, one double letter, or one simplicial edge. Listing gives, respectively, a translation derivative, the relation \(y-\sigma_i y-\rho_i y\) with all its spectators, or the same coefficient at the two ends of the edge. After quotienting by the derivatives, every singleton word on a partition is the support image of the standard word under the surjection whose fibres are its blocks, numbered in word order. Thus listing induces \(H^0(G_U(V))\to\mathsf M_U(V)\), inverse to the map from the mode quotient.

The target has an additive decomposition over the same coefficient ring,
\[
 G_U(V)\simeq R\oplus\bigoplus_{r\ge1}
                     (\mathcal D_r)_{\widehat\Sigma_r}.
\]
The subscript means coinvariants for the actual state exchange and the permutation of tangent vectors. Recall the pole \(1/(v-w)\) which survived the three-current collision. It depends jointly on the surviving point and the spectator. At a partition \(\pi\) of the labels there is one such field coefficient for the entire word, localized at all differences of distinct block coordinates and carrying the normal derivatives and Spencer tangents. What varies with the word is the order in which we read its blocks.

Order the blocks of \(\pi\) by their largest label and call this order \(\omega\). A word \(w=(J_1,\ldots,J_q)\) groups the blocks into nonempty sets \(J_i\). Reading each group in its inherited order gives the concatenated order \(\gamma_w\). Let \(P_w=\tau_{\omega,\gamma_w}\) carry the coefficient from \(\gamma_w\) to \(\omega\) by adjacent state exchanges. It leaves the abstract determinant lines fixed. In this common order the summand for \(\pi\) is \(C_\pi\otimes_k E_\pi\). Here \(C_\pi\) is the Spencer complex of the whole localized coefficient. The scalar complex \(E_\pi\) is spanned by words of letters \(t\det J\) in which every block occurs once. The letter is the determinant line on the basis \(J\), placed in degree \(1-|J|\).

Splitting a group now acts as the identity on \(C_\pi\). Suppose instead that two blocks \(a<b\) in the same group merge at \(b\). Both orders then delete \(a\). Transporting the full principal part after the merger gives the same result as first transporting the input and then merging in order \(\omega\), including every spectator. Thus the component of the collision differential is \(r^\omega_{ab}\otimes d_{ab}\). The first map takes that common principal part. The second replaces the letter containing \(a,b\) by minus its determinant contraction with the basis covector \(e_a^*\), with the graded derivation sign, and vanishes if the pair lies in different letters. For a bijection or a support surjection \(\alpha\), the transports through the intermediate grouped orders likewise cancel. After relabelling and induction to the support, the remaining state transport takes \(\alpha^*\omega_{\rm in}\) to \(\omega_{\rm out}\) independently of the word. The determinant bases retain their relabelling signs.

On the scalar tensor algebra declare each determinant letter primitive. Its unshuffle coproduct distributes letters between two subwords in all ways, preserving order within each and giving each permutation its graded sign. The two orders of a split combine to a graded commutator of primitive letters. A merger sends a letter to another primitive letter or to zero. Hence these scalar derivations are also coderivations. They commute with the rational Eulerian projectors \(e^{(n)}\) onto symmetric degree \(n\) in the primitives. Relabelling does too. Writing \(P=\bigoplus_w P_w\), the projector in the original word coordinates is
\[
 P^{-1}(1_{C_\pi}\otimes e^{(n)})P .
\]

In the cardinality-\(r\) layer each nondiscrete partition already occurs on its proper quotient. The quotient by that partition is initial among the contributing proper quotients, and their support maps are quasi-isomorphisms on the Spencer coefficients. The remaining discrete partition contributes \(\mathcal D_r\otimes_k E_r\). The scalar complex is the cellular complex of the permutohedron. Its augmentation sends each singleton word to \(1\). Equivalently, send the \(r\) singleton letters to distinct commuting variables and all larger letters to zero. Their product has symmetric degree \(r\), so only \(e^{(r)}\) survives the augmentation. Averaging over \(\Sigma_r\) gives the stated coinvariants. Each Eulerian summand thus has a single potentially nonzero layer. Exactness of the filtered union in the algebraic direct sum gives the additive splitting and degeneration at \(E_1\).

For a test on the state coefficient take \(R=k\), \(U=\mathbb G_m\), and the constant field algebra \(k\mathbf1\oplus ka\) with \(a\) in degree zero, \(a^2=0\) and translation zero. Let exchange act by \(-1\) on \(a\otimes a\) and trivially against the vacuum. The one-point mode \(A=[z^{-1};a]\) survives in the first summand since its residue is \(a\) and a derivative has zero residue. The two identical inputs have zero collision and exchange with sign \(-1\), so \(2A^2=0\). An ordinary unshuffle making \(A\) primitive would send this zero square to \(2A\otimes A\ne0\). The scalar word projectors leave the common state coefficient intact in the transported order. Multiplication in \(G_U(V)\) still has terms of smaller cardinality. Whether \(\Theta\) is a quasi-isomorphism in negative degrees is a question about its source as well. [The rational exchange diagram](05-bar-and-coherence.md#ch05-rational-exchange-diagram)

Compact support gives two different questions even for a single collision. On \(U=\mathbb C^\times\), take the finite constant field algebra \(\mathbb C[x,y]/(x,y)^4\) with translation zero and multiplication twisted by \(F=(1+E_2)^{H_1}\), where \(E=x\partial_y\) and \(H=x\partial_x\) act in the indicated tensor slots. Thus \(m_*=m_{\rm pol}F^{-1}\), and \(m=m_*(x,y)=xy-x^2\). In the \(13|2\) collision let \(a=\{1,3\}\) and \(b=\{2\}\). For the multiplier \(1/[z_b(z_a-z_b)]\), both quotient orders give the same density \(m\,dz/z\) in the surviving coordinate \(z\). Does it come from compactly supported integration? On compactifying \(U\) to the projective line, integrate about \(0\) and \(\infty\) with the positive orientation in each local coordinate and divide by \(2\pi i\). The periods are \((m,-m)\), since \(dz/z=-d(1/z)/(1/z)\) at infinity. This is a nonzero class in the cone of \(R\Gamma_c(U,V)[1]\to R\Gamma(U,V)[1]\), with \(V\) the constant coefficient just defined. It lies in the first Eulerian summand of the realized comparison, so passing through all finite sets does not kill it.

There is nevertheless a compactly supported construction on the ordered charts themselves. Let \(U\) be a smooth complex curve of finite type. Use analytic constructible coefficients, or the corresponding regular holonomic sector, with a supplied global word system whose coefficients are finite at each arity. Its changes of order, its identifications under extraordinary restriction to every collision diagonal, and its external product must be given coherently. Over a labelled collection of points, a lift chooses an order. Draw a Čech edge between two lifts and send a coefficient along that edge by the given change of order. Its boundary is the transported coefficient at the second lift minus the coefficient at the first. A chosen order contracts the augmented chain complex by prepending that lift. The exceptional image of an open chart is extension by zero. On intersections its counits give the alternating face maps. Common refinements of the orders before and after each collision then give the proper diagonal maps, compatibly under composition and external products.

Taking compact sections of these chains and then the homotopy colimit over finite sets with the proper diagonal maps for surjections computes \(p_{\mathrm{Ran},!}\), the left adjoint to extraordinary pullback from a point. Here the Ran space records a finite nonempty subset of the curve, with repeated coordinates giving the same subset. At a collision the extraordinary restriction identifies the coefficients on the repeated and unrepeated labels. This is the datum needed for compact pushforward along the proper diagonal. Both operations still agree on the derived coefficient ring \(B=T\otimes_A^{\mathbf L}T\), where \(A=\mathbb C[\kappa,\lambda]\) and \(T=A/(\kappa)\). The two-term resolution of \(T\) by multiplication by \(\kappa\) has zero differential after tensoring with \(T\). Its odd coefficient \(\eta\) in degree \(-1\) gives a second puncture class \(\eta(m,-m)\) in the comparison with ordinary integration. Thus the compact order construction recovers compact Ran integration, while the ordinary closed-incidence integral retains a logarithmic class and its odd partner outside the compact image. Further de Rham realizations require the actual maps on attachments, products and the marked vacuum.

Two other choices would already change the answer. On the ordered atlas, taking the free colimit of *all* expansion branches identifies one class \(x\) with a composite having two copies of \(x\). The relation \(x=2x\) kills the occupied vacuum along with every other positive-cardinality class. On \(\mathbb G_m\) the mode \([z^{-1};\mathbf1]\) survives. A different construction weights the configuration complex by its scalar dual. On \(\mathbb A^1\) its scalar singleton contributes the constant polynomial paired with constant-coefficient evaluation. This pair evaluates to one and gives a nonempty degree-zero class independent of the empty unit, whereas \(\mathsf M_{\mathbb A^1}(k)=k\). A geometric integral must preserve both the collision residue above and these unit distinctions.

## Finite rational categories and a non-scalar base {#ch13-finite-rational-categories-and-a-non-scalar-base}

Suppose one is given only the sectors and their fusion. The Ising spin sector \(\sigma\) fuses with itself to give the vacuum and an invertible sector \(\psi\) with \(\psi^2=1\). If tensor products of ordinary vector spaces realized these rules and the vacuum had dimension one, then \(\dim\psi=1\) and \((\dim\sigma)^2=2\). The required vector space cannot have integral dimension. There are, however, perfectly good finite spaces of *channels*: for an insertion of \(\sigma\), specify the sector entering at one end and the sector leaving at the other. Two successive insertions can be composed when these middle labels agree.

For coprime integers \(2\le p<q\), put
\[
c_{p,q}=1-\frac{6(p-q)^2}{pq},\qquad
h_{r,s}=\frac{(qr-ps)^2-(p-q)^2}{4pq},
\]
with \(1\le r<p\), \(1\le s<q\), and \((r,s)\sim(p-r,q-s)\). Let \(\mathcal C_{p,q}\) be the category of finite direct sums of the simple modules \(L_i\) of the **simple** Virasoro minimal-model algebra. Here \(c_{p,q}\) is the central charge and \(h_{r,s}\) the lowest conformal weight of the sector \((r,s)\). Its tensor product \(\boxtimes\) represents the full rational Ward problem: a map from the product to a module \(L_i\) specifies a three-point intertwiner, tested against the contragredient \(L_i^\vee\) at infinity. The category has the usual ribbon structure. This category is smaller than the category of all modules of the universal Virasoro algebra. [GR7](#ref-ch13-gr7)

To glue two successive fusion channels, the output sector of one must equal the input sector of the next. Let \(I\) index the simple objects and put \(B=\mathbb C^I\), the algebra of functions on \(I\). Its idempotent \(e_j\) is the function supported on sector \(j\). If \(v=ve_j\) and \(w=e_k w\) have mismatched labels, their relative tensor satisfies \(v\otimes_Bw=v\otimes_B e_je_kw=0\). This explains why the following fibre functor keeps both end labels. Define
\[
F(M)=\bigoplus_{i,j\in I}
\operatorname{Hom}(L_i,M\boxtimes L_j).
\]
A vector in the \((i,j)\)-summand is an intertwiner from \(L_i\) to \(M\boxtimes L_j\). Left multiplication by \(e_i\) and right multiplication by \(e_j\) select this space. Thus \(F\) takes values in finite-dimensional \(B\)-bimodules even though the individual Virasoro modules have infinitely many energy levels. Tensoring over \(B\) matches the intermediate label. For
\[
f:L_i\to M\boxtimes L_j,
\qquad g:L_j\to N\boxtimes L_k,
\]
the tensor comparison is composition with the associator:
\[
f\otimes g\longmapsto
a^{-1}_{M,N,L_k}(1_M\boxtimes g)f.
\]
To invert this map, decompose \(N\boxtimes L_k\) into simple summands. The multiplicity space of \(L_j\) in it is \(\operatorname{Hom}(L_j,N\boxtimes L_k)\). Thus a map from \(L_i\) to \(M\boxtimes(N\boxtimes L_k)\) is specified by one element of
\[
\bigoplus_j\operatorname{Hom}(L_i,M\boxtimes L_j)
       \otimes_{\mathbb C}\operatorname{Hom}(L_j,N\boxtimes L_k).
\]
These are exactly the \((i,k)\)-components of \(F(M)\otimes_B F(N)\). This proves that the tensor comparison is invertible. The associator pentagon makes the two ways of composing three channels agree. Thus \(F\) is exact, faithful and strong monoidal, with \(F(\mathbf1)=B\). For \(M=\mathbf1\) only \(i=j\) survives, with basis \(\mathrm{id}_{L_i}\) after the unit identification. These basis elements give the idempotents of \(B\).

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
Here \(m s=1\) on the fused coefficient, whereas \(s m\) projects onto matching labels in the ordinary tensor product. Thus \((s h m)(s h' m)=s h h' m\). The associator pentagon gives coassociativity by identifying the two triple splittings. The unit and counit satisfy the weak Hopf identities: the coproduct is coassociative and multiplicative, but \(\Delta(1)\) need not be \(1\otimes1\), and the scalar counit need not be multiplicative. The tensor of representations is
\[
\Delta(1)(V\otimes W),
\qquad
\Delta(1)=\sum_{i\in I}\rho_i\otimes\ell_i,
\]
where \(\rho_i,\ell_i\) are right and left actions of the idempotent \(e_i\in B\). This projection is exactly intermediate-label matching. The reconstruction preserves the ribbon structure and the finite pairing tensor. [GR7](#ref-ch13-gr7)

For the Ising model \((p,q)=(3,4)\), the simples \(1,\psi,\sigma\) satisfy
\[
\psi^2=1,\qquad\psi\sigma=\sigma,\qquad
\sigma^2=1+\psi.
\]
A faithful additive tensor functor to finite vector spaces with scalar unit would give positive integer dimensions with
\[
d_\psi^2=1,\qquad d_\sigma^2=1+d_\psi=2,
\]
which is impossible. The finite-base functor has no such problem. Its \(\sigma\)-bimodule has the following dimensions, in row and column order \(1,\psi,\sigma\)
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
In \(V_\sigma\otimes V_\sigma\) there are sixteen pairs of basis vectors. Fix the intermediate sector. If it is \(1\) there is one matching pair, and if it is \(\psi\) there is one. At \(\sigma\) there are two choices at each outer end, hence four pairs. Thus \(\Delta(1)\) has rank \(1+1+4=6\), the dimension of \(F(1)\oplus F(\psi)\) required by \(\sigma^2=1+\psi\).

::: figure fig-ising-matching-pairs

The finite-base construction works for every minimal model above. Except for \((2,3)\), a faithful finite vector-space fibre with scalar unit and multiplicative tensor isomorphisms is impossible even before coherence is imposed. At \((2,3)\), the reconstructed weak Hopf algebra is \(\mathbb C\). The simple-vacuum unit remains distinct from the ambient augmentation unit in the derived universal construction, including at this one-simple-object example. [GR7](#ref-ch13-gr7)

## Positive-integral affine fusion retains higher classes {#ch13-positive-integral-affine-fusion-retains-higher-classes}

Within a semisimple category every short exact sequence splits. Resolving its objects there would leave the fusion product concentrated in degree zero. The integrable affine sectors also lie in a larger module category, where the same objects have resolutions by induced modules. What survives if one fuses these resolutions before passing to the simple quotient? Let \(\mathfrak g\) be simple, \(k\in\mathbb Z_{>0}\), and \(L(\lambda)\) its integrable affine modules indexed by
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
with central generator \(K\) and cocycle \((x,y)\sum_{s=p,q}\operatorname{Res}_{w=s}(g\,df)\) on \(x\otimes f,y\otimes g\). On \(W_1(p)\otimes W_2(q)\), a current acts by the sum of its Laurent expansions in \(w-p\) on the first factor and \(w-q\) on the second. Since both factors have level \(k\), the central term of the commutator of \(x\otimes f\) and \(y\otimes g\) is \(k(x,y)\sum_{s=p,q}\operatorname{Res}_{w=s}(g\,df)\). The single generator \(K\) acts by \(k\).

**Example (two affine vacua).** Put a copy of \(L(0)\) at each of \(0,1\), with vacuum tensor \(v=|0\rangle\otimes|0\rangle\). Take a Cartan element \(H\) with \((H,H)\ne0\) and the functions \(f(w)=w\) and \(g(w)=1/w+2/(w-1)\). Write \(H_n^{(s)}\) for the mode \(H\otimes(w-s)^n\) on the factor at \(s\). All \(H_n^{(s)}\) with \(n\ge0\) kill \(v\), so
\[
(H\otimes f)v=0,\qquad
(H\otimes g)v=(H_{-1}^{(0)}+2H_{-1}^{(1)})v.
\]
The linear coefficient of \(f\) at each point is \(1\). Since \([H_1,H_{-1}]=(H,H)K\) at either point, the commutator of these two currents sends \(v\) to \(3k(H,H)v\). The residues of \(g\,df\) at \(0\) and \(1\) are \(1\) and \(2\). In the geometric local coordinate \(u=1/w\) at infinity, \(g=3u+O(u^2)\) and \(g\,df=(-3u^{-1}+O(1))\,du\). Reading powers of \(u\) as output mode indices would pair \(H_{-1}\) with \(3H_1\), giving the opposite central scalar. Equivariance would then force even the vacuum intertwiner, which sends \(v\) to \(|0\rangle\), to vanish.

For an output module \(X\in\mathcal G_\kappa\) at zero, write \(x_n=x\otimes t^n\) for its affine modes. To express a rational current in these modes, expand at infinity in descending powers of the pole variable \(t=w\). If \(f(t)=\sum_{n\le N} f_n t^n\), the expansion map is
\[
\begin{aligned}
\iota\colon\mathfrak g_{\{p,q\}}&\longrightarrow
       \mathfrak g((t^{-1}))\oplus\mathbb C K,\\
\iota(x\otimes f)&=\sum_{n\le N}f_n\,x\otimes t^n,\qquad \iota(K)=K.
\end{aligned}
\]
{#ch13-outgoing-current-expansion}
The target cocycle multiplies \((x,y)\) by the coefficient of \(t^{-1}\) in \(g(t)f'(t)\). The residue theorem gives
\[
[t^{-1}]\bigl(g(t)f'(t)\bigr)
  =-\operatorname{Res}_{w=\infty}(g\,df)
  =\sum_{s=p,q}\operatorname{Res}_{w=s}(g\,df),
\]
so \(\iota\) preserves the Lie bracket. For the two vacua, \(g(t)=3t^{-1}+2t^{-2}+2t^{-3}+\cdots\). Only \(3H_{-1}\) contributes to the commutator with \(H_1\), giving \(3k(H,H)\) on the output.

The infinitely many negative modes can raise the energy without bound. They act on the product \(\overline X=\prod_hX_{[h]}\) of generalized energy spaces. Since \(x_n\) lowers energy by \(n\), the component at energy \(h\) of the action on \(\xi=(\xi_h)_h\) is
\[
\bigl(\iota(x\otimes f)\xi\bigr)_h
   =\sum_{n\le N}f_n\,x_n\xi_{h+n}.
\]
For fixed \(h\), the spectrum of \(X\) is bounded below in \(h+\mathbb Z\), so \(\xi_{h+n}=0\) for all sufficiently negative \(n\). The upper bound \(N\) from the Laurent expansion makes this a finite sum in every component.

**Definition (rational-current intertwining map).** An intertwining map is a linear map \(I:W_1(p)\otimes W_2(q)\to\overline X\) satisfying \(I(av)=\iota(a)I(v)\) for every rational current \(a\in\mathfrak g_{\{p,q\}}\) and every input \(v\).

Pairing \(I(v)\) with the restricted dual \(D(X)=\bigoplus_h X_{[h]}^*\) uses only finitely many energy components. In the pairing of \(\overline X=D(X)^*\) with \(D(X)\), the modes satisfy \(\langle x_n z,\ell\rangle=-\langle z,x_{-n}\ell\rangle\) for \(z\in\overline X\) and \(\ell\in D(X)\). Since \(t^n=u^{-n}\), the insertion at infinity in this description is \(D(X)\), with local level \(k\). Equivariance of \(I\) makes \((v,\ell)\mapsto\langle I(v),\ell\rangle\) invariant under the sum of the three local current actions.

For the two simple vacua take their vertex-algebra multiplication with \(X=L(0)\), normalised by \(I(v)=|0\rangle\). The current \(H\otimes(w-1)^{-1}\) acts on \(v\) as \(H_{-1}^{(1)}v\). Its expansion in \(t=w\) gives
\[
 I(H_{-1}^{(1)}v)=\sum_{m\ge1}H_{-m}|0\rangle .
\]
Every term has a different energy and \(H_mH_{-m}|0\rangle=mk(H,H)|0\rangle\ne0\). Thus the image of this single incoming state requires the energy product.

More generally, choose the pole variable \(t=w-a\). Translation sends \(I\) to \(I_a=e^{-aL_{-1}}I\), since \([L_{-1},x_n]=-nx_{n-1}\) implements the substitution \(w=t+a\) and \(L_{-1}|0\rangle=0\). For an allowed rational coefficient \(b(w)\), write
\[
 b(t+a)=P(t)+\sum_{m\ge1}b_m t^{-m}.
\]
The polynomial part kills the vacuum. The energy-\(m\) component of \(I_a((H\otimes b)v)\) is \(b_m H_{-m}|0\rangle\) for \(m>0\). The full vector \(I_a((H\otimes b)v)\) lies in the algebraic vacuum module precisely when every finite pole of \(b\) lies at \(a\), since this is equivalent to a finite negative Laurent tail. Applying \(H_m\) to that vector returns \(mk(H,H)b_m|0\rangle\). For \(b=g\) and \(m=1\) this gives \(3k(H,H)|0\rangle\), independently of the higher coefficients. [Vacuum insertion and simple multiplication](#ref-ch13-gr8)

Write \(U=W_1\odot_{p,q}W_2\). Its universal map is \(I_{\rm univ}:W_1(p)\otimes W_2(q)\to\overline U\). An affine homomorphism \(\phi:U\to X\) extends energy by energy, giving the intertwiner \(\overline\phi\,I_{\rm univ}\) and the natural bijection
\[
\operatorname{Hom}_{\widehat{\mathfrak g}}
(W_1\odot_{p,q}W_2,X)
\cong
\operatorname{Hom}_{\mathfrak g_{\{p,q\}}}
\bigl(W_1(p)\otimes W_2(q),\iota^*\overline X\bigr).
\]
For two simple vacuum inputs the ordinary fusion object is \(L(0)\), and the vacuum multiplication above gives its unit comparison. A nonzero affine homomorphism \(\phi:L(0)\to X\) is injective and preserves energy. At least one input mark \(s\) differs from \(a\). For \(b=(w-s)^{-1}\), the coefficients \(b_m=(s-a)^{m-1}\) are then all nonzero. The image of this one state under \(\overline\phi I_a\) has a nonzero component at every positive integer energy. Consequently a genuine intertwiner of these two vacua whose values on all inputs lie in the algebraic \(X\) must be zero. [Simple affine fusion, Proposition 5.2](#ref-ch13-gr8)

The ambient fusion functor \(\odot_{p,q}\) is right exact in each input. For the finite integrable inputs considered here, choose resolutions \(P_\bullet(W_i)\) by affine Weyl modules with finitely many finite-dimensional tops in each degree. These Weyl modules are induced from finite-dimensional \(\mathfrak g\)-modules, with positive currents acting by zero and the central element by \(k\). Define
\[
L_b\odot(W_1,W_2)
=H_b\!\left(\operatorname{Tot}
\bigl(P_\bullet(W_1)\odot_{p,q}P_\bullet(W_2)\bigr)\right).
\]
These are the left-derived functors of the ambient universal-affine fusion, with their level-\(k\) affine-module action. The derivation is taken before restricting to the semisimple simple-quotient category. The spectral product of differential graded modules is a separate construction related to this one by a comparison map. [GR8](#ref-ch13-gr8)

Let \(G\) be the simply connected compact group with complexified Lie algebra \(\mathfrak g\), and \(\Omega G\) its space of loops beginning and ending at the identity.

**Theorem (derived fusion of integrable modules).** At the stated positive integral level and distinct points \(p,q\), the higher fusion functors on simple integrable inputs satisfy
\[
L_b\odot\bigl(L(\lambda),L(\mu)\bigr)
\cong
\bigoplus_{\nu\in P_k^+}
N_{\lambda\mu}^{\nu}L(\nu)
\otimes H_b(\Omega G;\mathbb C).
\]
The formula extends additively to finite sums of these inputs. The integers \(N_{\lambda\mu}^{\nu}\) are the Verlinde fusion multiplicities. The index \(b\) is homological; in the cohomological convention it contributes in degree \(-b\). [GR8](#ref-ch13-gr8)

Why do only integrable summands occur? Inside the algebra of currents regular at infinity, let \(\mathfrak r^{(M)}\) be the ideal vanishing there to order at least \(M\). A pole at infinity can lower the order. For \(p=0,q=1\) and an \(\mathfrak{sl}_2\) pair with \([H,E]=2E\), the bracket of \(E\otimes w\) with \(H\otimes w^{-M}\) is \(-2E\otimes w^{1-M}\). The regular algebra preserves a fixed depth. A pole of order \(d\) sends chains at depth \(M>d\) to depth \(M-d\), where its central residue against a vanishing current is zero. Dualising reverses these transition maps. Put \(W=L(\lambda)(p)\otimes L(\mu)(q)\). Currents vanishing at infinity act nilpotently on each finite-dimensional \(H_b(\mathfrak r^{(M)};W)\). The complementary root operator has a pole there. Reflection in the corresponding affine real root exchanges the two root operators up to sign and changes the truncation depth by at most two for \(M\ge5\). The direct limit of the dual homology groups identifies equivariantly with the restricted dual \(D(L_b\odot(L(\lambda),L(\mu)))\). The reflection acts on this limit by an automorphism and conjugates the missing operator to one already locally nilpotent. Together with local finiteness for \(\mathfrak g\), this proves integrability on the restricted dual and hence on the derived fusion module. Write \(m_b^\nu\) for the multiplicity of \(L(\nu)\) in \(L_b\odot\). Taking negative-current homology of the fused Weyl resolutions gives a spectral sequence. In homological column \(a\), the finite \(\mathfrak g\)-types have highest weights \(w\circ\nu\), where \(w\) runs over the minimal representatives of length \(a\) in the left cosets of the finite Weyl group in the affine Weyl group. Here \(w\circ\nu\) is the finite part of the shifted affine Weyl action. These weights distinguish the pairs \((w,\nu)\). Every higher differential changes column and preserves \(\mathfrak g\)-type, so it vanishes. For \(w=1\) the column is zero and the weight is \(\nu\). Thus the finite \(\mathfrak g\)-type \(V_\nu\) of highest weight \(\nu\) has multiplicity \(m_b^\nu\) in total degree \(b\).

Which current cohomology reads this multiplicity? To test the finite-dimensional type \(V_\nu\) at infinity, let \(\mathfrak l=\mathfrak g\otimes\mathcal O(\mathbb P^1\setminus\{p,q\})\) act on \(V_\nu\) by evaluation there. The evaluation map to \(\mathfrak g\) has kernel \(\mathfrak r\) and is split by the constant currents. Pairing the principal-parts chains with \(V_\nu\) uses the full algebraic dual \(W^*=\operatorname{Hom}_{\mathbb C}(W,\mathbb C)\) of the incoming tensor product, with contragredient action \((a\phi)(v)=-\phi(av)\). In this action each incoming local central element acts by \(-k\). The cochains relative to the constants are
\[
 C^j(\mathfrak l,\mathfrak g;W^*\otimes V_\nu)
 \cong \operatorname{Hom}_{\mathfrak g}(\Lambda^j\mathfrak r\otimes W,V_\nu).
\]
The right-hand side is the dual of the \(V_\nu\)-multiplicity space in the principal-parts chains. Its differential transposes their boundary.

In the absolute calculation the constant directions contribute \(H^\bullet(\mathfrak g;\mathbb C)\cong H^\bullet(G;\mathbb C)\). Evaluation splits off the constants, and the cochains on \(\mathfrak r\) are products of duals of finite-dimensional \(\mathfrak g\)-modules. Passing to the relative complex takes the invariant cochains on \(\mathfrak r\) and removes the constant-group factor. For two punctures the remaining topological factor in Teleman’s formula is \(H^\bullet(\Omega G;\mathbb C)\). At \(w=1\) the Verlinde multiplicity is \(N_{\lambda\mu}^{\nu}\) in degree zero. Dualizing in each degree gives \(m_b^\nu=N_{\lambda\mu}^{\nu}\dim H_b(\Omega G;\mathbb C)\). [Teleman, Theorem 0 and its remark, PDF p. 3](https://arxiv.org/pdf/alg-geom/9707014#page=3) · [GR8, Corollary 5.6](#ref-ch13-gr8)

The comparison to simple fusion acts by the augmentation \(H_\bullet(\Omega G;\mathbb C)\to\mathbb C\) after identifying the multiplicity spaces in loop degree zero by the comparison itself. It kills positive *loop* degree. A surviving multiplicity map need not be the identity in bases chosen in advance. Even with a simple-vacuum input, this map is not a quasi-isomorphism. For \(G=SU(2)\),
\[
H_\bullet(\Omega SU(2);\mathbb C)=\mathbb C[x],
\qquad |x|=2.
\]
The additional classes \(x,x^2,\ldots\) explain the failure directly. They belong to the derived ambient construction although the underived fusion category has its own tensor unit. With two level-one vacuum inputs and the trivial representation tested at infinity, the relative multiplicity in degree three is zero. The absolute cohomology also contains the degree-three class pulled back from \(SU(2)\).

Recording the homological degree by a formal variable \(t\), the exponents \(m_i\) of \(\mathfrak g\) give the product in the completed graded Grothendieck group
\[
a\star b=P(t)ab,
\qquad P(t)=\prod_i(1-t^{2m_i})^{-1}.
\]
Multiplying the simple-vacuum class by \(P(t)^{-1}\) gives a formal unit in that completed group. It does not construct a differential graded unit or multiplication on the entire loop-homology-enhanced object. Those require maps and associativity homotopies on the complexes themselves. Similarly, extending tensor comparisons across rational parameter walls requires integral lattices, specialization retaining higher Tor terms, and coherent reassociation on those lattices. Naive evaluation of a generic associator can fail at resonance. [GR8](#ref-ch13-gr8)

Return to the two rank-sixteen lattices. In the normal coordinate \(\delta=z_1-z_2\) of their collision, the test \(\delta\) recovers the pairing on each marked pair of weight-one currents. The test \(1\) on the *extended* two-point coefficient recovers their bracket. The residue between the separated factorization and diagonal collision isomorphisms reconstructs the chiral product of \(A\) as a morphism of right \(\mathcal D_{X^2}\)-modules. The finite-base fibre functor reconstructs the ribbon category \(\mathcal C_{p,q}\simeq\operatorname{Rep}(H)\) of a weak Hopf algebra. In the ambient universal affine category, the derived fusion \(L_b\odot\) also contains \(H_b(\Omega G;\mathbb C)\). A line probe also tests more than the value on its support. A bulk source can vanish along the line and still couple through a transverse derivative to a line operator. When the line joins two endpoints, its operators act from the right on one endpoint space and from the left on the other. Shrinking the interval tensors the two spaces over that common algebra. The derived tensor can detect a class even when ordinary multiplication identifies the joined interface with a single copy of its endpoint algebra. [A transverse Taylor source on a line](#ch14) · [Composition at a junction](#ch14-what-a-joined-interface-remembers)

## References {#ch13-references}

### GR1. What a realized categorical vacuum reconstructs {#ref-ch13-gr1}

*What a realized categorical vacuum reconstructs*, §§1–2 and 6–11. For a fixed unital chiral algebra, the unit splits the principal-parts quotient on affine sections. The action kernel therefore survives arbitrary classical base change. Theorem 9.1 uses that kernel to add a marked point, and Lemma 11.1 identifies its ordinary restriction at an existing mark after tensoring by the inverse canonical line. Applying these operations to the empty unit recovers the factorization coefficients of the algebra. [Base change for the action kernel](#ch13-lemma-base-change-for-the-action-kernel) · [Ordinary classical reconstruction](#ch13-theorem-ordinary-classical-reconstruction)

The unit-insertion functors carry the empty object \(\mathbb C\) to the vacua \(v_I\). On disjoint groups of positions, compatibility of insertion with external fusion gives their factorization maps. Raskin, [*Chiral Categories*, §§6.2–6.3](https://www.samraskin.net/chiralcats.pdf#page=41). The passage from factorization coefficients to a chiral product is A. Beilinson and V. Drinfeld, [*Chiral Algebras*, chapter 3, §3.4.8 and Theorem 3.4.9](https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf#page=24). [Realizing the vacuum and taking its residue](#ch13-the-realized-vacuum-on-every-configuration)

### GR2. Factorization and chiral algebras {#ref-ch13-gr2}

A. Beilinson and V. Drinfeld, *Chiral Algebras*, Proposition 3.4.7 (canonical connection), Theorem 3.4.9 (the equivalence), and §§3.4.10–3.4.12 (the inverse construction). [The chiral operation on the diagonal](#chiral-operation)

### GR3. Modules over a chiral algebra {#ref-ch13-gr3}

N. Rozenblyum, *Modules Over a Chiral Algebra*, arXiv:1010.1998v1. Definition 3.3.1 gives a factorization module with fixed labels \(I_0\). Definition 3.4.1 gives its action description. Equation 3.8 on PDF p. 8 makes the action of a polar one-form its principal part. Equation 3.9 on PDF p. 9 compares the two orders of action. On that page Theorem 3.5.1 identifies the two categories over quasi-coherent sheaves on \(X^{I_0}\). In its proof the boundary map of the one-added-point coefficient recovers the action, and the kernel recovers that coefficient. [PDF p. 8, https://arxiv.org/pdf/1010.1998v1#page=8](https://arxiv.org/pdf/1010.1998v1#page=8) · [PDF p. 9, https://arxiv.org/pdf/1010.1998v1#page=9](https://arxiv.org/pdf/1010.1998v1#page=9) · [The marked action and its kernel](#ch13-the-ordinary-categorical-round-trip)

### GR4. The transposed Vandermonde comparison {#ref-ch13-gr4}

*The transposed Vandermonde comparison*, theorem in “The cut and its completed recipient.” For the principal parts of one Heisenberg current on the affine line with its chosen coordinate, multiplication by the Vandermonde takes exterior coefficients to symmetric coefficients. The Cousin differentials here use zero central contractions. Transposition reverses the map and the vacuum triangle. The transposed product has as its source the dual of the whole localized external coefficient and includes the transposed cross factor. The final section, “The forward exterior contact,” asks for endpoint maps realizing the original contact. [The proved supported pro-duality](#ch13-theorem-supported-vandermonde-pro-duality) · [The open forward exterior contact](#ch13-open-problem-the-forward-exterior-contact)

### GR5. Occupied vacua and curvature {#ref-ch13-gr5}

*Derived occupied vacua and the first collision square* computes the occupied and mixed normal degrees. *A curvature obstruction for genuinely derived recipients* fixes the one-point readout, and *A curvature-tuned product and its next failures* treats a change of product. [The forward comparison and its hypotheses](#ch13-supported-duality-and-the-direction-of-comparison)

### GR6. Integration over the collision diagram {#ref-ch13-gr6}

*The symmetric Cousin coalgebra, its cobar words, and the all-surjection chain diagram*, Theorem D. *The integral over the Ran diagram*, Theorem E. *The arity filtration, its splitting, and the total cohomology*, Theorems F–G. *De Rham mode relations*, “A three-input boundary.” In *Ordered products, supported collisions and finite fusion*, §5 identifies the degree-zero boundary ideal by listing blocks in word order. Sections 6–7, equations (9)–(11), carry the full principal part through a change of order, including the spectators, and split the additive integral by the Eulerian projectors on determinant words. Reversing the colliding pair also requires transfer to the new surviving coordinate. *Compactly supported Ran integration on a derived self-intersection*, §§3–5, gives the two puncture residues. *Compactly supported Čech chains for order lifts*, §§1–3 and 7, identifies the compact pushforward under the stated descent hypotheses. [The word and Spencer maps](#ch05-rational-exchange-diagram) · [The three-current residue](#ch13-integrating-the-collision-diagram)

### GR7. The quantum group of the Virasoro algebra, as an object {#ref-ch13-gr7}

Sections 14–15, in particular Theorem 15.2, reconstruct the finite weak Hopf algebra from the marked rational Ward category and its finite-base fibre functor. [Label matching in the Ising model](#ch13-finite-rational-categories-and-a-non-scalar-base)

### GR8. Fusion for the affine family on the intended modules {#ref-ch13-gr8}

*Fusion for the affine family on the intended modules*, §§1.1 and 2.1. Expansion in descending powers of \(w\) gives the action on the completed output. Section 2.3 identifies this completion with the full dual of the restricted dual \(D(X)\). Proposition 2.6 gives the representing fusion product. Proposition 5.2 identifies ordinary fusion on the integrable inputs at distinct points. Theorem 5.3 compares the Weyl resolutions with two-point current homology. The real-root reflection in Theorem 5.5 proves integrability of the derived modules. Corollary 5.6 then identifies their affine summands and the augmentation on the loop factor. Section 8 treats noncritical tensor products and specialization. [The outgoing current expansion](#ch13-outgoing-current-expansion) · [The derived fusion theorem and its multiplicity calculation](#ch13-theorem-derived-fusion-of-integrable-modules)

The parabolic resolution used here is I. Heckenberger and S. Kolb, [*On the Bernstein–Gelfand–Gelfand resolution for Kac–Moody algebras and quantized enveloping algebras*, Theorem 3.6](https://arxiv.org/pdf/math/0605460#page=8). The current-algebra cohomology input is C. Teleman, [*Verlinde factorization and Lie algebra cohomology*](https://doi.org/10.1007/s002220050097), Theorem 2.5, *Inventiones Mathematicae* **126** (1996), 249–263. His [*Borel–Weil–Bott Theory for Loop Groups*, Theorem 0 and the ensuing remark, PDF p. 3](https://arxiv.org/pdf/alg-geom/9707014#page=3) displays the absolute topological factor. Relative cohomology for the constant currents gives the loop factor used in the multiplicity calculation. The affine-module conclusion also uses the integrability argument above.
