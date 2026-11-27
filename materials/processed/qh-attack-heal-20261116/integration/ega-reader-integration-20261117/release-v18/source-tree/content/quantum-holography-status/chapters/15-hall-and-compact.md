# Hall geometry and compact states

A short exact sequence
\[
0\longrightarrow B\longrightarrow M\longrightarrow A\longrightarrow0
\]
defines a point of the stack of extensions of \(A\) by \(B\). In a category of branes such an extension models a bound state. Its Hall product counts subobjects \(B\subset M\) with quotient \(A\). Over \(\mathbb C\) one integrates the corresponding constructible functions by compactly supported Euler characteristic.

Can Hall multiplication be realized by a local field product, or by the relative Donaldson–Thomas operation on the compact state space \(H_d=H^*(S^{[d]},\mathbb Q)\) of a K3 surface \(S\)? The comparison already has content before taking cohomology. If \(p\) records the quotient and subobject and \(q\) the middle term, the critical coefficient complexes require a morphism \(p^*(\mathscr P_\alpha\boxtimes\mathscr P_\beta)\to q^!\mathscr P_{\alpha+\beta}\) on the extension stack. On \(H_d\) the three-boundary operation gives a cyclic product. In degree \(d=1\) a nonzero Hochschild class changes that product while preserving the specified traces.

## Extensions and the reason for associativity {#ch15-extensions-and-the-reason-for-associativity}

Let \(\mathcal M_\alpha\) be a moduli stack of objects of charge \(\alpha\). Here a charge is an additive class, such as a class in a Grothendieck group. Let \(\mathcal E_{\alpha,\beta}\) classify exact sequences with quotient of charge \(\alpha\) and subobject of charge \(\beta\). The two maps are
\[
\mathcal M_\alpha\times\mathcal M_\beta
\xleftarrow{\ p\ }\mathcal E_{\alpha,\beta}
\xrightarrow{\ q\ }\mathcal M_{\alpha+\beta},
\qquad
p(M,B)=(M/B,B),\quad q(M,B)=M.
\]
Pullback along \(p\) places the two inputs on the extension space; pushforward along \(q\) combines all extensions with the same middle object. For constructible functions over \(\mathbb C\), the resulting ordinary Hall product is
\[
(f*g)(M)=\int_{B\subset M}f(M/B)g(B)\,d\chi_c.
\tag{15.1}
\]
The integral is the compactly supported Euler characteristic of the actual subobject varieties, weighted by the constructible function. We use finite charge support and domains on which this integral is defined. The indicator of the zero object is the unit. The order in (15.1) is quotient first, subobject second.

A small counting example explains why subobject geometry matters. In the category of vector spaces over \(\mathbb F_q\), use finite counting in place of Euler integration, and let \(e_1\) be the indicator of a one-dimensional space. Every extension of two one-dimensional vector spaces splits, but
\[
(e_1*e_1)(\mathbb F_q^2)
=\#\mathbb P^1(\mathbb F_q)
=\frac{q^2-1}{q-1}=q+1.
\]
The product counts the lines inside the middle object. It does not count just the isomorphism classes of possible middle objects. Over \(\mathbb C\), the constructible-function version gives \(\chi(\mathbb P^1)=2\).

Associativity has the same explanation one dimension higher. Either bracketing of three one-dimensional factors counts flags
\[
0\subset V_1\subset V_2\subset\mathbb F_q^3,
\qquad \dim V_i=i.
\]
There are \(q^2+q+1\) choices of a line and \(q+1\) planes through it, hence
\[
(e_1*e_1)*e_1=e_1*(e_1*e_1),
\qquad
\text{value on }\mathbb F_q^3=(q^2+q+1)(q+1).
\]
In a sheaf category, the two iterated extension spaces are likewise descriptions of the same three-step flag space. Base change and composition of the appropriate pushforwards prove associativity. For derived coefficient complexes, the same comparison must preserve their maps and homotopies on flags. Equality of the numerical integrals alone would not establish that statement.

::: figure fig-hall-correspondence

## One loop on finite root jets {#ch15-one-loop-on-finite-root-jets}

A Hall product can also be studied by asking what its Taylor coefficients do to one another. In the one-loop shuffle algebra the resulting comparison can be made over the polynomial ring \(R=\mathbb Q[\hbar]\). In charge \(m\) take \(A_m=R[x_1,\ldots,x_m]^{S_m}\), with \(A_0=R\). For this formula put the subobject in the first input. To multiply \(f\in A_p\) and \(g\in A_q\), sum over decompositions \(I\sqcup J=\{1,\ldots,p+q\}\), \(|I|=p\), the expressions
\[
 f(x_I)g(x_J)\prod_{i\in I,\,j\in J}
 \left(1+\frac{\hbar}{x_i-x_j}\right).
\]
The sum is a symmetric polynomial. For two singletons, write \(s(x,y)=(y,x)\) and \(u=x-y\). On an ordered two-variable input \(f\) the merge is \(f+sf+\hbar(f-sf)/u\). The last numerator is divisible by \(u\). In particular \(1*1=2\), \(x*1=x+y+\hbar\), and \(1*x=x+y-\hbar\). Thus exchange has a measurable effect even though the output is symmetric.

A finite root jet in \(W_m\) is an \(R\)-linear functional on \(A_m\) vanishing above some total root degree. For example \(J_i(f)=\partial_x^i f(0)\) in charge one. Form words on the positive-charge jets, each letter \(x(w)\) in cochain degree one. Transposing the Hall merge splits a letter into two and gives the differential of this cobar algebra \(\Omega(W)\). Let \(S_R\) be the zero-differential associative algebra on \(a_i\), \(i\ge0\), in degree and charge one. Its relations are the coefficients of
\[
 (z-w+\hbar)a(z)a(w)=(w-z+\hbar)a(w)a(z),
 \qquad a(z)=\sum_{i\ge0}a_i z^i.
\]
The augmented algebra map
\[
 F_R:\Omega(W)\longrightarrow S_R,\qquad
 x(J_i)\longmapsto i!\,a_i,\qquad
 x(w)\longmapsto0\quad\text{if \(w\) has charge greater than one}
\]
is a quasi-isomorphism in every charge. The derivative at the origin is \(i!\) times the coefficient of \(x^i\). For example the charge-two boundary of \(x(J_0^2)\) maps to \(2a_0^2+\hbar(a_1a_0-a_0a_1)\), the coefficient of \(z^1w^0\) in the exchange relation. The scalar unit maps to the scalar unit.

Why is finite support preserved by a contracting homotopy? In charge \(m\) use the adjacent operators
\[
 T_i f=s_i f+\hbar\,\frac{f-s_i f}{x_i-x_{i+1}}
\]
on ordered polynomials. They satisfy the symmetric-group relations. In the three-variable braid identity the common denominator reduces the comparison to \(ab=c(a+b)\) for \(a=\hbar/(x-y)\), \(b=\hbar/(y-z)\), \(c=\hbar/(x-z)\). Symmetrizing with these operators gives precisely the shuffle merge, with each shuffle counted once. Concretely, if two neighboring blocks merge and their permutation subgroup grows from \(H\) to \(J\), the operator on \(H\)-invariants is \(|H|^{-1}\sum_{w\in J}T_w\).

The resulting bar complex is the signed complex of ordered set partitions tensored over \(\mathbb Q[S_m]\) with these polynomial coefficients. A partition with \(k\) blocks gives a flag of its \(k-1\) proper prefix unions. Deleting the \(i\)th prefix merges blocks \(i\) and \(i+1\). For \(m\ge2\) these flags are the augmented simplices in the subdivided boundary of an \((m-1)\)-simplex. Its sole homology is the orientation line at word length \(m\). Averaging a rational contraction onto this line makes it equivariant. Each coefficient of the resulting contraction is a rational combination of \(T_w\). A reduced expression for \(w\) uses at most \(\binom m2\) divided differences, each lowering root degree by at most one. The transposed contraction therefore sends a jet of order at most \(D\) to a jet of order at most \(D+\binom m2\), over \(R\) itself. At top length the boundaries insert a charge-two split into neighboring letters. Their span is exactly the exchange ideal, so \(H^m(\Omega(W)_m)=(S_R)_m\) and all other degrees vanish. In charges zero and one the map is already an isomorphism of complexes.

The map preserves the root power sums, charge and translation \(Ta_i=(i+1)a_{i+1}\). It therefore also preserves the regular operation \(Y(a,z)b=(e^{zT}a)b\). Here the \(x_i\) are internal roots. To recover a pole as two physical support positions meet, one still needs a coefficient on their collision locus and a map from the oriented extension correspondence into it.

## A faithful ordinary comparison on a K3 surface {#ch15-a-faithful-ordinary-comparison-on-a-k3-surface}

There is a compact example in which the flags themselves can be compared. Choose a smooth projective complex K3 surface \(S\) with an ample polarization \(H\), \(H^2=8\), and divisor classes \(D_1,D_2,D_3,V\) whose Néron–Severi lattice has matrix
\[
\begin{pmatrix}
-8&-4&-4&1\\
-4&-8&-4&1\\
-4&-4&-8&2\\
1&1&2&0
\end{pmatrix},\qquad H=D_3+4V.
\]
The period construction supplies such a polarized surface: the lattice has signature \((1,3)\), and \(H^\perp\) contains no class of square \(-2\). Set \(L_i=\mathcal O_S(D_i)\). They are \(H\)-Gieseker stable with the common Hilbert polynomial \(\chi(L_i(mH))=4m^2-2\), and satisfy
\[
\dim\operatorname{Ext}^\bullet(L_i,L_i)=(1,0,1),
\qquad
\dim\operatorname{Ext}^\bullet(L_i,L_j)=(0,2,0)\quad(i\ne j).
\]
Let \(\mathcal A_L\) be their finite-extension category in the abelian category of semistable sheaves of the fixed reduced Hilbert polynomial. All its objects and subquotients are vector bundles.

The surface and polarization are part of this construction; arbitrary triples of spherical bundles need not have the same reduced Hilbert polynomial. [A common-polynomial spherical triple][k3-triple]

The independent algebraic category is that of finite-dimensional nilpotent left modules over a completed preprojective algebra \(\widehat\Pi\). Start with three vertices and two arrows on each chosen oriented pair; double the arrows and impose the preprojective moment relation at each vertex. If \(J\) is the arrow ideal, a module is nilpotent when \(J^NM=0\) for some finite \(N\). Completion of the path algebra does not turn such a module into an infinite-dimensional object.

Take the ordinary Hall algebras of rational constructible functions, and within them the unital composition subalgebras \(\mathcal C_\Pi\) and \(\mathcal C_L\) generated by the three simple indicators. The distinction is useful: the theorem identifies these entire generated algebras, rather than merely checking a few relations, but does not assert an isomorphism of every constructible function on the two moduli problems.

**Theorem (ordinary K3 Hall comparison).** Choose the simultaneous cyclic minimal \(A_\infty\) model of the collection and a comparison with its Dolbeault category strictly unital over the quiver vertex-idempotent algebra \(\mathbb C^3\). There is a unique unital, charge-graded isomorphism
\[
\Theta:\mathcal C_\Pi\xrightarrow{\sim}\mathcal C_L
\]
sending the simple indicator at vertex \(i\) to \(1_{[L_i]}\). At every finite nilpotence bound it comes from an algebraic tensor family. Over reduced bases this family identifies reduced relative flag varieties, their subquotients, and all forgetting and regrouping maps. [Primitive recognition, Proposition “Regular families and the ordinary composition algebra”][ordinary-hall]

The proof explains why the result reaches flags. In the minimal model, the differential is zero. For an operation \(m_k\) with \(k\ge3\), a degree-zero input is a vertex unit, so strict unitality kills the operation. A degree-two input with the remaining inputs positive would force the output above degree two. With all inputs in degree one, cyclicity pairs the output against a unit; strict unitality again makes it zero. The perfect cyclic pairing then forces the output itself to vanish. The remaining quadratic equation is precisely the preprojective moment relation.

At nilpotence bound \(N\), the comparison applied to a module involves only paths shorter than \(N\). Applied to the regular module of \(\widehat\Pi/J^N\), it gives an algebraic bundle with a right action of that finite-dimensional algebra. Tensoring this bundle with a module family preserves exact sequences and base change. The resulting flag comparison makes every Hall word have the same value on corresponding objects. The two word-evaluation maps therefore have the same kernel, which proves faithfulness as well as surjectivity.

An independent action on completed Enriques cycle states satisfies all six real Serre relations. That action can have a kernel while \(\Theta\) remains faithful: a faithful identification of algebras and a faithful representation of that algebra are different assertions. This distinction will matter again when an algebra is represented on a space of compact states.

## Critical coefficients and orientation {#ch15-critical-coefficients-and-orientation}

On a Calabi–Yau threefold, the local deformation theory of an object is governed by its self-extension complex. A critical chart presents the moduli problem as the critical locus of a function \(f\) on a smooth space. Its vanishing-cycle complex records the topology of nearby fibres of \(f\); replacing it by its Euler characteristic discards cohomological degree and parity.

To glue these local coefficient complexes one needs an orientation: a square root of the appropriate determinant line, together with its squaring map. In the determinant convention used here, write
\[
K_F=\det R\operatorname{Hom}(F,F),\qquad
D(F,G)=\det R\operatorname{Hom}(F,G),\qquad
J_F^{\otimes2}\simeq K_F.
\]
An extension requires compatible root maps involving
\(J_F\otimes J_G\otimes D(F,G)\). The cross determinant \(D(F,G)\) is part of the map. Its Euler-characteristic sign is not a replacement for the line itself.

For critical coefficient complexes \(\mathscr P_\alpha\), the extension correspondence must carry an actual morphism
\[
p^*(\mathscr P_\alpha\boxtimes\mathscr P_\beta)
\longrightarrow q^!\mathscr P_{\alpha+\beta}.
\tag{15.2}
\]
Here \(q^!\) is exceptional inverse image, the duality-compatible pullback. By adjunction, (15.2) gives a map after \(q_!\); on a proper middle map this is the usual proper pushforward. The chosen cohomology theory, support convention and degree shifts must make this push-pull operation well defined. Associativity asks that its two composites agree on the actual three-step flag, with the orientation identifications included.

The first framed charge-two example shows what the geometric comparison must retain. A flag for framed instanton data includes an invariant line. In a chart let \(u\) be the difference of the two support positions and \(D\) the slope of that line. Restriction of the matrix moment equation to the curve, after eliminating two regular pairs, gives the coefficient
\[
 K_f=R'[D]\otimes\Lambda(\eta,\chi),\qquad
 |\eta|=|\chi|=-1,\qquad d\eta=uD,\quad d\chi=0 .
\]
Here one can take \(R'=\mathbb C[t_1,t_2,\beta^{\pm1},\kappa,z,w,q]/(q^4)\), \(u=z-w\). The parameters \(t_1,t_2\) are the two equivariant weights, \(\beta\) sets the scale, and \(q\) records the order of the deformation. The closed odd variable comes from a fourth moment equation whose value on the flag is identically zero. Replacing \(K_f\) by the equation \(uD=0\) would discard it.

The classical equation has two branches, \(D=0\) and \(u=0\). Their constant coefficient glues along their common origin by the difference of the two restrictions. Both branches occur with multiplicity \(+1\) in the oriented transverse graph. The second branch contributes integration with compact support along \(D\) before the Thom map for \(u=0\). On the field side one can already construct the supported Cauchy coefficient. After removing its invertible exchange factor, its first cubic representative is
\[
 2t_1t_2(t_1+t_2)q^3\beta^{-3}(z-t)^{-3}(t-w)^{-1}.
\]
Taking the first-current coefficient at the auxiliary point \(t=w\) gives \(2t_1t_2(t_1+t_2)q^3\beta^{-3}u^{-3}\). Multiplication by \(u^2\) detects this simple residue.

There is a sharp way to test how much normal information a lift needs. Impose the two equations \(u^p=D=0\), and write \(M_p=R'[D]/(u^p,D)\). In the Cauchy coefficient \(T\) of finite principal parts, \(u\) lowers pole order and kills \(u^{-1}\). On the moment complex \(C=T[D]\otimes\Lambda(\eta,\chi)\), with \(d\eta=uD\), a map \(M_p\to H^0(C)=T\) may send \(1\) to any \(m\in\ker u^p\). It lifts to a derived linear map \(M_p\to C\) exactly when \(u^{p-1}m=0\). Indeed, resolve the two equations by Koszul generators and lift \(m\) through the \(D\) face by \(\eta t\), where \(ut=m\). The remaining face, evaluated at \(D=0\), requires \(u^pt=u^{p-1}m=0\). Conversely, raising the order of each pole in \(m\) by one gives such a \(t\) and a lift with zero last face. Thus the nonzero cubic pole has no lift on the third normal cut, and a lift on the fourth. On that fourth cut it also lifts to the original rational Cauchy representatives with both odd actions retained. This test has a prescribed auxiliary source \(M_4\otimes\Lambda\chi\).

What remains open is a map of the same variance on the *whole flag* which carries the proper oriented operation to the field operation. It must act on both odd directions, the framing line, the two branches and their common restriction, agree with both vacuum maps and compose on refined flags. In particular it must supply a geometric input for the cubic representative just calculated.

There is a strong orientation theorem on a specific compact domain. Let \(X=S_{\mathrm{Kum}}\times E\), with a Calabi–Yau volume form, and choose a smooth elliptic fibre \(C\subset S_{\mathrm{Kum}}\), points \(p\in C\), \(x\in E\), and \(L\in\operatorname{Pic}^0(E)\). The actual semi-topological components of
\[
A=\mathcal O_C\boxtimes\mathcal O_x,
\qquad B=\mathcal O_p\boxtimes L
\]
generate a subgroup \(\Gamma\cong\mathbb Z^2\). Here a semi-topological component is a connected-component class in the moduli of perfect complexes, with addition induced by direct sum. Deformation in a connected family preserves this class; equality of numerical Chern characters need not identify component classes. On the union of these components, the compact orientation root admits unital associative root maps for every finite ordered flag, without changing its square. The two isomorphism classes of enhancements form an \(H^2(\Gamma,\mathbb F_2)\)-torsor. [Strong orientation on compact two-charge components][strong-orientation]

The mechanism is concrete. The ratio between two triple root maps is a sign, and the pentagon makes these signs a group three-cocycle. Since a two-torus is a classifying space for \(\mathbb Z^2\), its third cohomology vanishes; correcting the binary maps by a two-cochain removes the defect. The use of actual components is essential. The theorem does not identify them with every object of the same numerical charge, nor does it provide equivariant descent or compare the root with a separately chosen geometric orientation.

Parity remains visible throughout. For example, \(29\) even and \(93\) odd directions have superdimension \(-64\), just as \(64\) purely odd directions do. The scalar \(-64\) determines neither the graded vector space nor its bracket. A proposed identification with an automorphic denominator algebra must compare these coefficients and operations, not only their alternating counts.

## Compact reduction keeps relative moment values {#ch15-compact-reduction-keeps-relative-moment-values}

A particularly explicit domain consists of sheaves
\[
J(T)=\mathcal O_S\boxtimes T
\]
on \(S\times E\), where \(T\) has finite length on \(E\). Put \(C_n=\operatorname{Coh}_0^n(E)\). Its self-extension theory on the threefold is
\[
R\operatorname{Hom}_{S\times E}(J(T),J(T'))
\simeq R\operatorname{Hom}_E(T,T')
\otimes(\mathbb C\oplus\mathbb C\eta),
\qquad |\eta|=2,\quad\eta^2=0.
\tag{15.3}
\]
The adjective spherical refers here to the two scalar self-extension groups of \(\mathcal O_S\), in degrees zero and two. The second summand carries the paired obstruction directions. The classical \(C_n\) is smooth, but (15.3) is not just its ordinary tangent complex. The flag domain requires every associated graded factor to lie in this spherical sector; constraining only the middle object admits extra subobjects.

For every \(n>0\), let \(\mathfrak U_n\) be the derived sheaf open with classical objects \(J(T)\), and fix a point \(x_*\in S\). Write \(r_*=Li_{x_*}^*\) for restriction to \(\{x_*\}\times E\), and let \(p_S,p_E\) be the projections of \(S\times E\). The four reduction maps have types
\[
\begin{aligned}
\det V &: \mathfrak U_n\longrightarrow B\mathbb G_m,
&V(F)&=R\Gamma(E,r_*F),\\
m_nr_* &: \mathfrak U_n\longrightarrow E,\\
\mu_E &: \mathfrak U_n\longrightarrow\mathbb A[-1],
&\mu_{\mathrm{sc}}&:\mathfrak U_n\longrightarrow\mathbb A[-2].
\end{aligned}
\]
Here \(B\mathbb G_m\) classifies line bundles, \(m_n(T)\) is the support sum with multiplicities, and \(\mathbb A[-j]=\mathbb V(\mathbb C[-j])\) is a derived additive group, rather than an ordinary affine line. The map \(\mu_E\) is minus the logarithm of \(\det Rp_{S*}F\), normalized by its value at \(x_*\). Its line is classically trivial and rigidified at that point; the K3 volume form identifies its derived logarithm with \(\mathbb A[-1]\). The second moment uses the similarly rigidified relative determinant
\(\det_XF\otimes p_E^*(\det_Er_*F)^{-1}\); elliptic Serre integration gives its logarithm in \(\mathbb A[-2]\). These are algebraic determinant maps, including their exact-triangle addition homotopies.

Their common derived fibre is
\[
\mathfrak V_n=
\mathfrak U_n\times^R_{B\mathbb G_m\times E\times\mathbb A[-1]\times\mathbb A[-2]}
(\mathcal O,0,0,0).
\]
The first fibre includes an actual trivialization of \(\det V\), with \(V=H^0(E,T)\) at a classical point. Pullback by translation \(a\) changes the support sum by \(-na\). The framing and centering therefore retain finite scalar and translation data \(B\mu_n\times E[n]\), which enter the quotient.

Rigidifying the residual central \(\mu_n\) and dividing by the translation subgroup \(E[n]\) defines
\[
\mathfrak R_n^{\mathrm{amb}}
=\bigl[(\mathfrak V_n\mathbin{/\mkern-6mu/}\mu_n)/E[n]\bigr].
\]
Here \(\mu_n\) is the group of \(n\)th roots of unity and \(E[n]\) the \(n\)-torsion subgroup of \(E\). The derived stack \(\mathfrak R_n^{\mathrm{amb}}\) has a closed nondegenerate \((-1)\)-shifted symplectic form and smooth classical truncation
\[
\mathcal B_n=[(C_n\mathbin{/\mkern-6mu/}\mathbb G_m)/E].
\]
The double slash denotes rigidification: locally the objects are retained while their central scalar automorphism subgroup is quotiented out. The corresponding lifting gerbe is the stack of local choices of a lift, with their scalar automorphisms; it is not just a set of choices. The cyclic formal neighbourhoods of \(\mathfrak R_n^{\mathrm{amb}}\) agree with those of \(T^*[-1]\mathcal B_n\). A global algebraic equivalence is known at length one; formal agreement at general length does not assert a global equivalence. Nevertheless, the canonical roots \(K_{\mathcal B_n}\) identify the critical coefficients with \(\mathscr P_n=\mathbb Q_{\mathcal B_n}[0]\). On the common-lifting classical flag stack the resulting map \(p^*(\mathscr P_a\boxtimes_{BE}\mathscr P_b)\to q^!\mathscr P_{a+b}\) is an isomorphism with zero source shift; \(BE\) is the classifying stack of elliptic-curve torsors. These give actual classical Hall arrows at every positive length, compatible with the full ordered flags. [Elliptic Weyl transport, ambient paired reduction and critical coefficients][spherical-reduction]

The proof removes symmetries together with their paired directions. At a point, the scalar identity, elliptic translation, and their two Serre-dual partners form a nondegenerate two-pair subcomplex. The four actual derived fibres have its symplectic orthogonal complement as tangent complex. Pullback preserves closedness; the finite quotients preserve nondegeneracy. This constructs the reduced stack, rather than merely naming an orthogonal complement of one tangent space.

Relative flags explain the remaining global problem. For a flag with one total moment condition,
\[
\mu_M=\mu_A+\mu_B=0
\]
allows \(\mu_A=t\), \(\mu_B=-t\). Requiring both terms to vanish imposes an extra equation. Accordingly, a three-step flag is formed using the same total normalization and its intermediate scalar lifting gerbes. Replacing its intermediate object by an independently reduced one deletes relative moment information. The global comparison with a shifted conormal construction must preserve these moment values, the closed form and every refinement homotopy.

Elliptic translation has the same relative character. If \(Q_\alpha\to BE\) records the translation torsor, two endpoints lie in
\[
Q_\alpha\times_{BE}Q_\beta,
\]
where \(BE\) is the classifying stack of elliptic-curve torsors. They share one torsor. The relative zero-object unit is \(BE\) with its coefficient; the product of two unrelated quotients would add independent torsor cohomology.

A separate mixed theorem treats actual endpoint families in a volume-preserving Kummer neighbourhood \(C\times E\times\Delta\). Its dual cross-extension lines give the cubic chart \(f=\delta ab\). For the classes \(\alpha+n\beta\), \(0\le n\le2\), the determinant slice yields the reduced shifted-cotangent description. Both reduced–ordinary extension orders have coefficient maps of the form (15.2), their composites agree on the one-\(A\)/two-\(B\) flag, and the binary index shift is zero. The proper middle maps use the stated fixed-Hilbert-polynomial, slope-zero domain. This establishes the local mixed operation; extending it beyond these product neighbourhoods and comparing the prescribed compact orientation require further maps. [Reduced mixed coefficients, theorem “Mixed coefficients and one-\(A\)/two-\(B\) flags”][mixed-coefficients]

Two such charts can be compared around a branch value in the elliptic base of the Kummer surface. On the overlap of opposite sheets let \(\delta\) be the spectral difference and \(a,b\) the two ordered cross-extension coordinates. If \(g\) is the change of frame on the forward extension line, the transition is
\[
 (\delta,a,b)\longmapsto(-\delta,ga,-g^{-1}b).
\]
Inversion on the elliptic surface factor reverses its two-form. The sign on the reverse line compensates this change in the Serre pairing, while the reversal of \(\delta\) preserves the whole cubic. Each ordered extension and its intrinsic orientation map is transported to the corresponding order in the second chart, with both endpoints translated on the same elliptic torsor. For an independently prescribed compact root, assume its square comparison exists over the whole elliptic family of split endpoints and their two extension germs. Its ratio to the intrinsic root is a \(\{\pm1\}\)-local system there. Pullback along the multiplication-by-two cover of this elliptic parameter kills its character, since \(\epsilon(2\lambda)=1\) for every period \(\lambda\). Descent back to the elliptic curve still sees the two independent values of \(\epsilon\). The local cubic and its two ordered operations do not select those values for a prescribed compact root.

## Relative Donaldson–Thomas theory produces an operator first {#ch15-relative-donaldsonthomas-theory-produces-an-operator-first}

Let \(S\) be a smooth projective complex K3 surface, \(E\) an elliptic curve, \(0\ne\beta\in\operatorname{Pic}(S)\) an effective class, and \(d\ge0\). Relative ideal sheaves on a tube \(S\times\mathbb P^1\), with ends at \(0,\infty\), restrict to length-\(d\) subschemes on each end. Their boundary state space is
\[
H_d=H^*(S^{[d]},\mathbb Q),\qquad
\eta_d(a,b)=\int_{S^{[d]}}a\cup b.
\]
It has its full cohomological grading and is concentrated in even degrees.

Write \(M_{\beta,d,m}\) for the stable expanded relative ideal-sheaf moduli, with third Chern-character index \(m\). On the tube its Euler characteristic is \(m+d\); after closing to \(S\times E\), the Euler index is \(m\). The reduced virtual class removes the K3 obstruction direction and has complex dimension \(2d+1\). An interior divisor descendant \(\tau_0(\omega D)\), for \(D\in H^2(S)\) and an interior point class \(\omega\), reduces the dimension by one. Proper evaluation at the ends gives a degree-zero correspondence
\[
\eta_d(\widehat B^D_{\beta,d,m}a,b)
=\int_{[M_{\beta,d,m}]^{\mathrm{red}}}
\tau_0(\omega D)\operatorname{ev}_0^*a\operatorname{ev}_\infty^*b.
\tag{15.4}
\]
Nondegeneracy of \(\eta_d\) determines the operator. The virtual correspondence, not a prescribed scalar trace, defines it.

The series \(\widehat B^D_{\beta,d}(r)=\sum_m(-r)^m\widehat B^D_{\beta,d,m}\) is Laurent with a finite lower bound. Geometric closure gives
\[
\frac{1}{\beta\cdot D}\operatorname{Tr}_{H_d}\widehat B^D_{\beta,d}(r)
=\sum_n(-r)^n\mathrm{DT}_{n,(\beta,d)}^{S\times E},
\qquad \beta\cdot D\ne0.
\tag{15.5}
\]
These are the reduced invariants of the translation quotient, including finite stabilizer weights. To prove (15.5), degenerate \(E\) to a nodal rational curve. The full Poincaré diagonal contracts the two relative insertions to the trace. Dividing the divisor insertion by \(\beta\cdot D\) implements translation descent, including the orbit weight \(1/|G|\) for a finite stabilizer \(G\). [Relative Donaldson–Thomas operators, geometric closure][relative-dt]

Multiple covers also admit an untraced formula. For each \(k\mid\beta\), choose a K3 surface \(S_k\) and the stated real isometry \(\phi_k:H^2(S,\mathbb R)\to H^2(S_k,\mathbb R)\) sending \(\beta/k\) to a primitive integral effective class \(\beta_k\). Its extension \(\Phi_k:H_d(S,\mathbb R)\to H_d(S_k,\mathbb R)\) is a graded isometric ring isomorphism. Then
\[
\widehat B^D_{\beta,d}(r)
=\sum_{k\mid\beta}\Phi_k^{-1}
\widehat B^{D_k}_{\beta_k,d}(r^k)\Phi_k,
\qquad D_k=\phi_kD.
\tag{15.6}
\]
Each operator summand has coefficient one. The scalar factor \(1/k\) appears only after (15.5), because \(\beta_k\cdot D_k=(\beta\cdot D)/k\). The real cohomological comparison does not automatically lift to rational or integral cohomology, Hodge structures, Chow correspondences or sheaf functors.

## A cyclic product that all these traces can miss {#ch15-a-cyclic-product-that-all-these-traces-can-miss}

Closing a tube is only one gluing operation. A three-boundary sphere defines a bilinear map \(\mu\), paired with the third state by \(\eta_d\). The ordinary operation is cup product. The reduced operation has degree \(-2\), vanishes when one input is the ordinary unit, and satisfies the Hochschild cocycle equation
\[
a\mu(b,c)-\mu(ab,c)+\mu(a,bc)-\mu(a,b)c=0.
\tag{15.7}
\]
Thus \(ab+\epsilon\mu(a,b)\), with \(\epsilon^2=0\) and \(|\epsilon|=2\), is a unital first-order associative deformation. Cyclicity means \(\eta_d(\mu(a,b),c)\) is invariant under cyclic permutation. Reduced degeneration proves (15.7): each channel of a four-boundary sphere contains one ordinary and one reduced factor.

For \(d=1\), let \(C\) be a rational section and \(F\) a fibre of an elliptic K3, so
\[
C^2=-2,\quad F^2=0,\quad C\cdot F=1.
\]
The complete section coefficient is
\[
\mu(a,b)=\eta_1(a,C)\eta_1(b,C)C
\quad\text{on all }H^*(S,\mathbb Q).
\tag{15.8}
\]
The divisor equation gives its three degree-two insertions; the unit identity eliminates the possible degree pattern \((0,2,4)\). The normalization is \(\eta_1(\mu(F,F),F)=1\). In particular
\[
\mu(C,C)=4C,\qquad \mu(C,F)=-2C,\qquad \mu(F,F)=C.
\]
These formulas determine a full twenty-four-dimensional state operation, including its vanishing on classes orthogonal to \(C\). [Relative Donaldson–Thomas operators, the section cubic][section-cubic]

The following algebraic calculation explains why this information cannot be recovered from the marked trace. Write the K3 cohomology algebra as
\[
A=\mathbb Q1\oplus V\oplus\mathbb Qp,
\qquad V=H^2(S,\mathbb Q),\quad
ab=q(a,b)p\ (a,b\in V),\quad pV=p^2=0.
\]
Here \(p\) is the point class and \(q\) the intersection pairing. Choose isotropic classes \(u,v\perp C,F\) with \(q(u,v)=1\). Set
\[
\ell_u(a)=\eta_1(a,u),\qquad
\nu_u(a,b)=\ell_u(a)\ell_u(b)u,
\qquad \widetilde\mu=\mu+\nu_u.
\]
For degree-two inputs, the first and last terms of the Hochschild differential of \(\nu_u\) are the same scalar multiple of \(p\); the middle terms vanish. The unit and point-class cases give the same identity, so \(\nu_u\) is a normalized cocycle. Its paired cubic is \(\ell_u(a)\ell_u(b)\ell_u(c)\), hence cyclic.

Because \(\ell_u(F)=0\), the fibre-marked operation is unchanged. For every \(D\in A\), the change in multiplication is the rank-one endomorphism
\[
\nu_u(D,-)=\ell_u(D)u\otimes\ell_u.
\]
The trace of \(x\otimes\ell\) is \(\ell(x)\). Consequently
\[
\operatorname{Tr}\nu_u(D,-)
=\ell_u(D)q(u,u)=0.
\]
This holds on all twenty-four states, not only on the section–fibre plane. Yet
\[
\mu(v,v)=0,\qquad \widetilde\mu(v,v)=u,
\qquad \eta_1(v,\widetilde\mu(v,v))=1.
\tag{15.9}
\]
Even a change of first-order splitting cannot remove the difference while fixing the ordinary algebra. For a one-cochain \(f\),
\[
\eta_1(v,(\delta f)(v,v))
=2\int_Sv^2f(v)=0,
\]
since \(v^2=0\), whereas the same functional on \(\nu_u\) equals one. The two Hochschild classes are distinct. The geometric relative invariant selects (15.8). The other product exhibits an ambiguity in recovering it from the marked tube and the traces.

How much information did those measurements lose? Fix the cup algebra, its grading, its unit, its pairing, all cap scalars, the whole operator \(\mu(F,-)\), and every trace \(\operatorname{Tr}\mu(D,-)\). Two commutative, cyclic first-order corrections differ by a symmetric cubic \(T\) on \(V\). Indeed, degrees and the unit force every other trilinear coefficient to vanish, and the first-order associator on three middle classes is \((T(a,b,c)-T(b,c,a))p=0\). The marked operator fixes \(T(F,-,-)=0\). The traces fix the contraction \(\tau_qT=0\), where \((\tau_qT)(a)=\sum_{ij}q^{ij}T(a,e_i,e_j)\) in any basis. Thus the space of differences is
\[
 \ker\!\left(\operatorname{Sym}^3 L\xrightarrow{\ \tau_q\ }L\right),
 \qquad L=\operatorname{Ann}(F)\subset V^* .
\]
Here \(L\) has dimension \(21\), and \(q^{-1}|_L\) has rank \(20\). Contraction is onto. For example, choose \(\ell\in L\) with nonzero square. Contracting \(\ell^3\) yields a nonzero multiple of \(\ell\), and contracting \(\operatorname{sym}(\ell^2m)\) for \(m\perp\ell\) yields a nonzero multiple of \(m\). The dimension is \(\binom{23}{3}-21=1750\). These directions remain distinct even allowing a change of first-order splitting. A degree-minus-two Hochschild coboundary with the stated normalization has paired cubic \(\lambda(a)q(b,c)+\lambda(b)q(a,c)+\lambda(c)q(a,b)\). Its contraction is \(24\lambda\), so a trace-free coboundary of this form vanishes.

There is an explicit set of \(1750\) scalar insertions that recovers the missing coefficients. Put \(G=C+F\), so \(G^2=F^2=0\), \(q(F,G)=1\). Set \(W=\langle F,G\rangle^\perp\). For \(z\in W\) the state \(v(z)=G+z-q(z,z)F/2\) has square zero. Its diagonal reading \(T(v(z),v(z),v(z))\) is a polynomial \(H(z)\) of degree at most three. The inverse metric on \(W\) gives the differential operator \(\Delta_W=\sum q_W^{ij}\partial_i\partial_j\). The trace condition is \(\Delta_WH=0\). Choose \(s\in W\) of square \(a=2\), and write \(z=y+xs\) with \(y\in s^\perp\cap W\), a space of dimension \(19\). If \(\Delta'\) denotes its inverse-metric operator, the harmonic equation gives
\[
 H(y+xs)=A(y)+xB(y)-\tfrac a2x^2\Delta'A(y)
                         -\tfrac a6x^3\Delta'B(y)
\]
for arbitrary polynomials \(A,B\) of degrees at most three and two. In rational coordinates use \(x=0\) and all nonnegative integer tuples \(y\) of sum at most three. Their \(1540\) values determine \(A\) by ordinary polynomial interpolation. At \(x=1\) the \(210\) tuples of sum at most two then determine \(B-a\Delta'B/6\). Applying \(1+a\Delta'/6\) recovers \(B\), since \((\Delta')^2 B=0\). Homogenization and polarization recover \(T\) from \(H\). Fewer than \(1750\) fixed scalar linear readings cannot separate this vector space. This inverse is for the stated first-order algebraic problem. Realizing a proposed set of insertions as operators of a compact brane theory requires a geometric or physical preparation.

Which of these cubics lift to associative products in the fixed rational coordinates? Write \(E=\langle C,F\rangle^\perp\), \(g=q|_E\), \(f=q(F,-)\) and \(T_0=q(C,-)^{\otimes3}\). With the cup unit, pairing, grading, cap scalars, fibre row and all first multiplication traces fixed, an integrable cubic has the form \(T_0+B+kf^3\). Here \(B\) is a symmetric trace-free cubic on \(E\). Define \(g(m_B(a,b),c)=B(a,b,c)\). The four-state associator equation is
\[
 g(m_B(a,b),m_B(c,d))-g(m_B(b,c),m_B(a,d))
   =k\bigl(g(a,b)g(c,d)-g(b,c)g(a,d)\bigr).
\]
It characterizes the cubics admitting a second-order associative lift. Each such cubic has a unique graded Frobenius extension in these coordinates, polynomial of degree at most four in the degree-two deformation parameter. The tangent space of this marked locus at \(T_0\) has dimension \(1520\), and its nonzero-\(k\) open stratum is smooth of dimension \(191\).

At \(k=0\), \(m_B\) makes \(E\) a commutative associative algebra with invariant form \(g\) and traceless multiplication operators \(L_a\). For a nondegenerate form of dimension \(d\) and Witt index \(w\) in characteristic zero, set \(m=\min(d,2w+1)\). Then \(E^{m+1}=0\), and some law on that fixed form has \(E^m\ne0\). Indeed \(\operatorname{Tr}L_a^j=\operatorname{Tr}L_{a^j}=0\), so the Newton identities make \(L_a\) nilpotent. The last \(\lfloor l/2\rfloor\) vectors of a Jordan chain of length \(l\) are mutually orthogonal isotropic vectors, since \(L_a\) is self-adjoint for \(g\). This bounds \(l\) by \(2w+1\). Polarizing \(L_a^m=0\) gives the product bound. A truncated polynomial ideal with its anti-diagonal invariant pairing attains it on an appropriate orthogonal summand.

On the original rational or real K3 marking \((d,w)=(20,2)\). Every sixfold product of middle elements vanishes, and a fivefold product can survive. Over the complexified marking the sharp vanishing length is \(21\). To see a genuinely complex specialization, take \(\mathbb C[s,z]/(z^{21}-s)\) with \(e_i=z^i\) for \(1\le i\le20\) spanning its trace-zero summand. A complex marking identifies \(g(e_i,e_j)=\delta_{i+j,21}\). Removing the unit component of multiplication gives
\[
 B_s(e_i,e_j,e_l)=\delta_{i+j+l,21}+s\,\delta_{i+j+l,42},\qquad k=-s .
\]
For \(s\ne0\) the algebra is étale. At \(s=0\) its middle algebra is \(z\mathbb C[z]/(z^{21})\), with \(e_1^{20}=e_{20}\ne0\). Any particular real or rational law on the original marking retains its sixfold identity after extension of scalars. The complex marked family supplies new laws. Its isometric stabilizer is \(\mu_{21}\subset SO(g)\), so the \(O(g)\)-orbit of the cyclic point splits into two \(SO(g)\)-orbits. Their closures are distinct \(190\)-dimensional irreducible components of the reduced zero fibre inside the closure of the complex étale stratum. Other components and scheme multiplicities remain open. The degree-two deformation parameter integrates a fixed cubic on all \(24\) states, while \(s\) here varies the middle multiplication itself.

## The Igusa series and the stronger realization question {#ch15-the-igusa-series-and-the-stronger-realization-question}

A stable pair on \(X=S\times E\) is a morphism \(\mathcal O_X\to F\) with \(F\) pure of dimension one and zero-dimensional cokernel. Purity means that \(F\) has no nonzero zero-dimensional subsheaf. Reduced Donaldson–Thomas/stable-pair comparison gives a common rational function \(R_{h,d}(v)\), whose Laurent expansion at \(v=0\) is their series for a primitive effective K3 class \(\beta_h\) with \(\beta_h^2=2h-2\).

The automorphic variables come from the genus-two Siegel upper half-space:
\[
Z=\begin{pmatrix}z_1&z_2\\z_2&z_3\end{pmatrix},\quad
\operatorname{Im}Z>0,\qquad
(q,r,s)=(e^{2\pi iz_1},e^{2\pi iz_2},e^{2\pi iz_3}).
\]
Let \(\chi_{10}\) be the genus-two Igusa cusp form of weight ten, normalized by \([qrs]\chi_{10}=1\). Let \(\Delta_5\) be the weight-five product of the ten even genus-two theta constants, with sign fixed by leading coefficient \(+64(qrs)^{1/2}\), and put \(D_5=\Delta_5/64\). Then \(\chi_{10}=D_5^2\). [Primitive reduced counting and normalization][igusa-normalization]

Sum the normalized traces (15.5) with weights \(q^{h-1}s^{d-1}\). In their rational representatives, the inverse Igusa theorem gives
\[
\sum_{h,d\ge0}R_{h,d}(-r)q^{h-1}s^{d-1}
=-\frac1{\chi_{10}(r,q,s)}
=-D_5^{-2}=-4096\Delta_5^{-2},
\qquad D_5=\Delta_5/64.
\tag{15.10}
\]
Expansion at \(r=0\), at \(r=\infty\), and after \(r=e^{iu}\) are distinct operations on that rational function. The empty boundary \(d=0\), with state space \(H_0=\mathbb Q\), supplies the indispensable \(s^{-1}\) coefficient. [Relative Donaldson–Thomas operators, primitive inverse Igusa series][igusa-series]

Equation (15.10) is a numerical theorem with a geometric trace construction behind it. The imprimitive numerical formula follows from the multiple-cover theorem. A realization of the compact state theory asks for more: an independently defined critical Hall or field state space, a map to the full \(H_d\), and compatibility with the actual extension correspondences, ordinary cup unit, full pairing and reduced three-boundary operation. The comparison must recover the zero in (15.9), as well as the scalar in (15.10).

There is a finite-dimensional geometric operator that produces the Igusa form itself. For a smooth complex genus-two curve \(C_2\), let \(W_6\) be its six Weierstrass points and \(H=H^0(C_2,\omega)\). Evaluate the fifth powers of holomorphic differentials:
\[
 e_5:\operatorname{Sym}^5 H\longrightarrow
            \bigoplus_{P\in W_6}\omega_P^{\,5}.
\]
Both sides have dimension six. In the coordinates \(y^2=a_6\prod_{i=1}^6(x-x_i)\), with \(\alpha=dx/y\) and \(\beta=x\,dx/y\), the evaluation matrix in the monomial basis has rows proportional to \((1,x_i,\ldots,x_i^5)\). The Wronskian fixes the proportionality in the determinant line. With \(\lambda=\det H\) the result is
\[
 d_e=a_6^5\!\prod_{i<j}(x_j-x_i)(\alpha\wedge\beta)^5
               \otimes\operatorname{or}(W_6)
       \ \in\lambda^5\otimes\operatorname{Or}(W_6).
\]
The final factor changes sign on an odd permutation of the six points. Write \(j\) for the Jacobian map from smooth genus-two curves to principally polarized abelian surfaces. In the period normalization of (15.10),
\[
 j^*\chi_{10}=\frac{d_e^2}{2^{32}\pi^{20}},\qquad
 j^*D_5=-\frac{d_e}{2^{16}\pi^{10}} .
\]
The second sign uses the orientation fixed on the bielliptic family; reversing that comparison reverses it. To see why one calibration suffices, the squared ratio is a regular unit on smooth binary sextics. The polynomial coefficient ring localized at the irreducible discriminant has units \(c\,\operatorname{Disc}^k\). Rescaling the sextic by any nonzero complex scalar gives an isomorphic curve, while its discriminant scales to the tenth power of that scalar times its original value. Hence \(k=0\). The calibrated equality of squares holds throughout the smooth locus, and the orientation identifies the unsquared sections there. For the ordered roots \(0,1,2,4,7,11\) in a monic sextic the fifteen factors multiply to \(838252800\), so the coefficient of \((\alpha\wedge\beta)^{10}\) in \(j^*\chi_{10}\) is \(10721859080625/(65536\pi^{20})\). This supplies the section on smooth curves. A compact \(S\times E\) operation preparing this evaluation, together with its behavior at stable degenerations, remains an additional construction.

The root-space question also has an independent mathematical answer on its own algebra. In the parity-minimal Gritsenko–Nikulin algebra the signed denominator in the doubled coordinate is \(D_5(2Z)\). At the sum of the three real simple roots the signed coefficient is \(-64\), while the presentation gives \(29\) even and \(93\) odd states. Two even three-generator brackets survive Jacobi and \(27\) more come from bracketing a real and a null generator. The chamber correction supplies \(93\) odd simple generators. An auxiliary space with \(64\) odd states gives the same signed coefficient. Lifting the denominator from such numbers to a compact Hall algebra requires both parity dimensions, the primitive bracket, its relations and a compatible action on the state space.

The same requirement applies to a Hall-to-field comparison. On a declared charge, coefficient and support domain, the map must carry the coefficient morphism (15.2) to the specified position-dependent field operation. Its three-input compatibility is an equality or a specified homotopy on the full flag/configuration correspondence. The target must contain the actual shifted singular divisors and normal directions; agreement of generator relations or scalar characters does not define this map. A prepared state is further data: a distinguished vector or functional with specified gluing laws, not an arbitrary normalization chosen to reproduce one trace.

Period and isogeny constructions supply additional genuine comparisons. Rational marked isogeny transport preserves the Hilbert-state ring and pairing, and the primitive marked relative tensors in the stated effectiveness chambers with one reduced sewing factor. An integral Brauer-twisted Fourier–Mukai endpoint changes rank and degree, so its relative operation problem belongs to the corresponding twisted higher-rank moduli. These maps constrain a realization, but do not identify its full coefficient, orientation and prepared-state systems automatically. [Period and isogeny state comparison][isogeny-states]

Closing the relative cylinder gives \((\beta\cdot D)^{-1}\operatorname{Tr}_{H_d}\widehat B^D_{\beta,d}(r)\) for \(\beta\cdot D\ne0\). At \(d=1\) the three-point invariant of a rational section \(C\) gives the cubic \((a,b,c)\mapsto q(a,C)q(b,C)q(c,C)\) on \(H^2(S,\mathbb Q)\), with \(q\) the intersection pairing. The trace and the fibre-marked cylinder admit the \(1750\)-dimensional space of trace-free first-order variations computed above. A Hall realization of the compact product must recover the section cubic itself.

[ordinary-hall]: #ref-ch15-01
[strong-orientation]: #ref-ch15-02
[spherical-reduction]: #ref-ch15-03
[mixed-coefficients]: #ref-ch15-04
[relative-dt]: #ref-ch15-05
[section-cubic]: #ref-ch15-05
[igusa-series]: #ref-ch15-05
[isogeny-states]: #ref-ch15-06
[k3-triple]: #ref-ch15-07
[igusa-normalization]: #ref-ch15-08

## Source manuscripts {#ch15-source-manuscripts}

### 1. Primitive recognition {#ref-ch15-01}

### 2. Strong orientation on compact two-charge components {#ref-ch15-02}

### 3. Elliptic actions and critical Hall transport {#ref-ch15-03}

### 4. Reduced mixed critical coefficients {#ref-ch15-04}

### 5. Relative Donaldson–Thomas operators {#ref-ch15-05}

### 6. Isogenies and K3 state comparisons {#ref-ch15-06}

### 7. K3 lattices and spherical objects {#ref-ch15-07}

### 8. Curves, states and a square root {#ref-ch15-08}
