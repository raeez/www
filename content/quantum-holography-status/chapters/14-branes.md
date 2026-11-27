# Branes and open–closed operations

Place a topological line at \(z=w=0\) and apply the gauge-field source \(A_t=a(t)z^2w\) in one colour direction. Its value on the line vanishes. Yet \(\partial_z^2\partial_w A_t/(2!1!)=a(t)\) there. The time integral couples this source to the \((2,1)\) line generator. The zero source and \(a(t)z^2w\) have the same value on the line. Their divided \((2,1)\) derivatives differ by \(a(t)\), so this line coupling distinguishes them. A constant transverse profile instead tests the charge.

This preparation takes place in the protected Omega-deformed M-theory on \(\mathbb R_t\times\mathbb C_z\times\mathbb C_w\), whose perturbative bulk action is noncommutative Chern–Simons theory. An M2 brane has two spatial worldvolume dimensions and an M5 has five, each with one time dimension. After the deformation the M2 supplies the line along \(t\). An M5 supplies a chiral surface along \(z\) at fixed \(t,w\). The general line coupling pairs the divided transverse Taylor coefficient \(\partial_z^m\partial_w^n A_t/(m!n!)\) with the generator labelled by \(m,n\). [Gaiotto–Oh, *Aspects of Omega-deformed M-theory*, §§2.7–3.1](https://arxiv.org/html/1907.06495v2)

What relation must two such couplings obey when they act in succession on the same line? Costello's protected M2 theory permits two independent calculations of the answer. Place \(K\) M2 branes at the tip of an \(A_{n-1}\) singularity. The five-dimensional gauge field then takes values in \(\mathfrak{gl}_n\). Write \(c\) for the transverse noncommutativity, so \(z*w-w*z=c\) in the Moyal product, and \(h_{\mathrm b}\) for the bulk loop parameter. Fix \(c\ne0\) and choose units with \(c=1\). Perturbation theory is formal in \(h_{\mathrm b}\).

::: example {#ch14-m2-first-jet-commutator title="Two first jets on an M2 line"}
For \(n\ge2\) let \(E=E_{12}\) send the second basis vector to the first. Write \(J(H)\) for the universal line generator labelled by the matrix-valued polynomial \(H\). Apply the two first-jet operations \(J(Ez)\) and \(J(Ew)\) in opposite time orders and subtract. At tree level their bracket is the matrix commutator with Moyal multiplication of the entries. Both orders contain the matrix factor \(E^2=0\). At one loop the bulk operator product has a second colour contraction. For labels \(E_{ij}z,E_{kl}w\) it leaves the product of the two constant generators \(J(E_{il})J(E_{kj})\). Every other term in the one-loop formula is multiplied by \(\delta_{jk}\) or \(\delta_{il}\). On the chosen pair both deltas vanish, so in the order and normalisation of Costello's (9.3.11) the bulk dual gives
\[
 [J(Ez),J(Ew)]
   =\frac{h_{\mathrm b}}{32\pi^2}\,J(E)^2+O(h_{\mathrm b}^2).
\]
The constant algebra embeds in the classical enveloping algebra by the Poincaré–Birkhoff–Witt theorem. In this subalgebra \(U(\mathfrak{gl}_n)\), \(E\) acts on two copies of the defining representation by \(E\otimes1+1\otimes E\). Its square sends \(e_2\otimes e_2\) to \(2e_1\otimes e_1\). Replacing this product by multiplication of the colour matrices would discard a nonzero output. [Costello, §9.3, equation (9.3.11)](https://arxiv.org/pdf/1705.02500#page=42)

The brane description begins with two matrices \(B_1,B_2\) acting on \(\mathbb C^K\) and maps \(I:\mathbb C^n\to\mathbb C^K\), \(P:\mathbb C^K\to\mathbb C^n\). The classical equation is \([B_1,B_2]+IP=c\,1_K\), modulo changes of basis in \(\mathbb C^K\). Quantum Hamiltonian reduction gives its protected operator algebra. The generators labelled by transverse monomials come from the framed words \(PB_1^rB_2^sI\) with their colour indices contracted against a matrix. In the presentation valid uniformly in \(K\), interchanging the two first-jet words can join their colour indices or contract their transverse letters. The two colour joins again require \(2=1\). The transverse contraction leaves two constant words, giving \(h_{\mathrm l}J(E)^2\) to first order in the brane parameter \(h_{\mathrm l}\).

At \(K=1\) this contraction is visible in the reduction itself. Write \(D,X\) for the conjugate centre-of-mass operators in the order \([D,X]=h_{\mathrm l}\). They commute with the constant off-diagonal flavour operator \(T\). The corresponding one-letter insertions give
\[
 [TD,TX]=T^2[D,X]=h_{\mathrm l}T^2 .
\]
For a finite numerical example take \(n=2\) and \(c/h_{\mathrm l}=4\). In the ordered reduction the moment equation on the framing variables \(r_1,r_2\) reads \(r_1\partial_{r_1}+r_2\partial_{r_2}+2=c/h_{\mathrm l}\). Thus homogeneous quadratics furnish a flavour module. With \(T=r_1\partial_{r_2}\), the commutator sends \(r_2^2\) to \(2h_{\mathrm l}r_1^2\).

On the uniform algebra, comparing the two first-order coefficients fixes \(h_{\mathrm l}=h_{\mathrm b}/(32\pi^2)\) to first order in these conventions. The reading is an operator coefficient, before choosing a state on the line. [Costello, §§1.5–1.7, Lemma 11.0.1 and §§13.1–13.3](https://arxiv.org/pdf/1705.02500#page=56)
:::

Which algebra contains this commutator to every order? On the bulk side, take the Koszul dual at the vacuum augmentation on a time interval times a formal transverse disc, retain the sum of rotation weight spaces at each finite perturbative order and take the inverse limit over those orders. On the brane side, use the algebra of operators uniform in \(K\). Its maps to the finite-\(K\) reductions at nonzero brane parameter are surjective and send the central rank parameter \(\kappa\) to \(K\). Costello's deformation theorem identifies the two completed associative algebras after a formal change of the loop parameter whose higher coefficients may depend polynomially on \(\kappa\). Constructing the bulk dual uses only the bulk fields and their augmentation. The independent M2 comparison comes from the framed matrix reduction and the agreement of its deformation class with the bulk one. The theorem concerns products of protected line operators. Joining two endpoints asks for the actions at the ends of the interval as well. [Costello, §§8 and 13.4, Theorem 16.0.1](https://arxiv.org/pdf/1705.02500#page=84)

Let the line end on an M5 surface. Operators incident on an endpoint act on its space of states, making that space a module. At a crossing a state \(m\) carries an action from each side. If an insertion \(a\) on the left can pass an insertion \(b\) on the right without changing the state, then \((am)b=a(mb)\). These commuting actions make the crossing states a bimodule. Shrink an interval with an operator at each end. An insertion on the common line can first be moved to the right end of the left piece or to the left end of the right piece. The two answers must agree after joining. In the [fusion channels of the preceding chapter](#ch13-finite-rational-categories-and-a-non-scalar-base) the shared datum was a sector label. At this junction it is the whole action of the operators on the line.

The fields on a brane form the open sector; a field that can be inserted away from the brane belongs to the closed sector. A square-zero supercharge gives differentials on these fields, and the Becchi–Rouet–Stora–Tyutin (BRST) differential implements gauge symmetry with ghost fields. On these complexes, composition can retain a relation among junction operators even if ordinary multiplication forgets it. In the particle model a degree-two class detects the flux of the line. Its proposed realization by integrating the fields on a physical interval requires an independently constructed interval action with both endpoints.

## What a joined interface remembers {#ch14-what-a-joined-interface-remembers}

Let \(R\to A\) describe how operators on the common line act at an endpoint. In degree zero the relation to impose is \(ar\otimes b=a\otimes rb\), with the action of \(r\in R\) taken through this map. Relations among these identifications can carry operators of their own.

**Definition (derived composition of interfaces).** For the two regular endpoints of \(R\to A\), the complex of the joined interface and its multiplication are
\[
X=A\otimes_R^{\mathbf L}A,
\qquad
\mu:X\longrightarrow A.
\]
Here \(\otimes_R^{\mathbf L}\) means that one first resolves an \(R\)-module factor by projectives and then tensors the resolution with the other factor. The resulting differential remembers relations imposed at the common interface. The map \(\mu\) multiplies the two outer factors, which retain commuting left and right \(A\)-actions. With cohomological grading, \(H^{-i}(X)=\operatorname{Tor}_i^R(A,A)\). If \(R\to A\) is surjective, the ordinary tensor product is already \(A\). Even in this case a relation between paths at an endpoint may persist in degree \(-2\). The smallest example below has only one surviving vertex.

**Example (a relation between paths).** Take the quiver
\[
1\mathrel{\mathop{\longrightarrow}^{a}}2
\mathrel{\mathop{\longrightarrow}^{b}}1
\]
over \(\mathbb C\), impose \(ab=0\), and multiply paths in the order they are traversed. Its path algebra \(R\) has basis
\[
e_1,e_2,a,b,ba.
\]
Let \(A=R/(Re_2R)\cong\mathbb C\), supported at vertex 1. The right projective modules have bases
\[
e_1R=\langle e_1,a\rangle,
\qquad e_2R=\langle e_2,b,ba\rangle.
\]
A projective resolution of \(A\) is
\[
0\longrightarrow e_1R
\xrightarrow{\,b\cdot\,}e_2R
\xrightarrow{\,a\cdot\,}e_1R
\longrightarrow A\longrightarrow0.
\]
Indeed, the first map sends \(e_1,a\) to \(b,ba\), so it is injective. The second sends \(e_2\) to \(a\) and kills \(b,ba\). Its image is precisely the kernel of \(e_1R\to A\). The composite is zero because \(ab=0\).

Tensoring with the left module \(A\) replaces \(e_1R\) by \(\mathbb C\) and \(e_2R\) by zero. Thus the derived tensor is represented by
\[
\mathbb C\longrightarrow0\longrightarrow\mathbb C
\quad\text{in degrees }-2,-1,0,
\]
and
\[
\operatorname{Tor}_0^R(A,A)=\mathbb C,
\qquad \operatorname{Tor}_1^R(A,A)=0,
\qquad \operatorname{Tor}_2^R(A,A)=\mathbb C.
\]
The leftmost copy of \(\mathbb C\) survives because the resolution had a relation \(ab=0\) before the vertex \(2\) was removed. Multiplication maps this degree-minus-two class to zero. Could one have predicted it just by examining the ideal \(I=Re_2R\) of the quotient? For any quotient \(A=R/I\), tensoring \(0\to I\to R\to A\to0\) with \(A\) gives \(\operatorname{Tor}_1^R(A,A)=I/I^2\), the conormal module. Here \(e_2^2=e_2\), so \(I^2=I\). The conormal module vanishes even though the relation has already given a nonzero \(\operatorname{Tor}_2\).

For the quiver the ordinary junction is one-dimensional and the degree-two class is represented by the discarded path relation. Now fix the number \(N\) of indistinguishable Weyl particles. The brane comparison above was uniform in the stack size and formal in the bulk loop parameter. Here the particle algebra is given at a fixed numerical Weyl parameter. The commutator of the collective position and momentum fixes the flux normalization for a degree-two test on the derived junction. Fix a numerical \(\hbar\in\mathbb C^\times\), and set
\[
W_\hbar=\mathbb C\langle x,y\rangle/([x,y]-\hbar),
\qquad \mathfrak g=W_\hbar^{\mathrm{Lie}},
\qquad U_N=U(\mathfrak g)/(1_{\mathfrak g}-N).
\]
In the quotient relation \(1_{\mathfrak g}=N\,1_U\), the left side is the Lie generator represented by the Weyl unit and \(1_U\) is the unit of the enveloping algebra. At zero Cherednik deformation parameter, the \(N\)-particle algebra and coupling are
\[
A_N=(W_\hbar^{\otimes N})^{S_N},
\qquad
\phi_N:U_N\longrightarrow A_N,
\qquad J(f)\longmapsto\sum_{i=1}^N f(x_i,y_i).
\]
Use symmetric Weyl ordering for \(f\). The image of \(J(x)\) is the sum of the \(N\) position operators and that of \(J(y)\) is the sum of their conjugates. Distinct particles commute, so the commutator of the two sums is \(N\hbar\,1\). This reads the flux \(J(1)=N\,1\) in units fixed by the single-particle commutator. The derived composition uses this same \(\phi_N\) at both ends.

**Theorem: the flux class in derived particle composition.** For every integer \(N\ge1\) and every numerical \(\hbar\ne0\), \(\phi_N\) is surjective. Its kernel \(I_N\) is generated by the Newton relation \(e_{N+1}\), the elementary symmetric polynomial expressed in the power sums \(J(x^k)\), and \(I_N^2=I_N\). Consequently
\[
\operatorname{Tor}^{U_N}_1(A_N,A_N)=0.
\]
To identify a degree-two contribution, quotient the Weyl Lie algebra by its scalar centre. Two lifts of elements of this quotient can have a scalar commutator even when their classes commute; for instance \([x,y]=\hbar 1\). This scalar defect defines the class of the central extension
\[
0\longrightarrow\mathbb C1\longrightarrow\mathfrak g
\longrightarrow\mathfrak g/\mathbb C1\longrightarrow0
\]
and will be denoted by \(\omega\). Capping a degree-two sewing class with \(\omega\) evaluates it on that extension and gives a split surjection of \(A_N\)-bimodules
\[
\omega\mathbin{\frown}-:
\operatorname{Tor}^{U_N}_2(A_N,A_N)\twoheadrightarrow A_N.
\]
Every sewing Tor group is a possibly infinite direct sum of the bimodules
\[
D(\tau)=(\tau\otimes W_\hbar^{\otimes N})^{S_N},
\]
where \(\tau\) runs through irreducible representations of \(S_N\). These modules are projective separately on the left and on the right. The cap kernel is canonically \(\operatorname{Tor}^{U(\mathfrak g)}_2(A_N,A_N)\), while its splitting requires a choice. At \(N=1\), the cap is an isomorphism; for \(N\ge2\), the kernel's multiplicities remain to be determined. See [*The junction with its flux class*, Theorems 4–6](#ref-ch14-01).

Since \(A_N\ne0\), the derived multiplication \(A_N\otimes^{\mathbf L}_{U_N}A_N\to A_N\) fails to be a quasi-isomorphism at every rank. Ordinary Hom and Ext-one comparisons nevertheless hold for all \(A_N\)-modules. The flux class measures a failure that those lower-degree comparisons cannot see.

The proof uses Weyl commutators to generate polarized trace relations from \(e_{N+1}\). Rigidity of particle-module extensions, together with the classification of Harish–Chandra bimodules, then kills \(I_N/I_N^2\). Here the Harish–Chandra condition controls iterated commutators with polynomial symmetric observables. An explicit homotopy on the bar complex transfers this condition to the two outer actions on Tor. The central-extension sequence supplies the degree-two cap; the bimodule decomposition supplies its splitting. The published classification used here is [Berest–Etingof–Ginzburg, Theorem 8.5](https://arxiv.org/abs/math/0111005).

A splitting at the junction must commute with the two endpoint actions simultaneously, which makes it a map of modules over \(A^e=A\otimes A^{\mathrm{op}}\). Separate projectivity is a weaker property. For example, the diagonal bimodule of \(A=\mathbb C[t]\) is free on either side, but over \(A^e=\mathbb C[t_L,t_R]\) it has resolution
\[
0\longrightarrow A^e\xrightarrow{t_L-t_R}A^e
\longrightarrow A\longrightarrow0.
\]
Applying \(\operatorname{Hom}_{A^e}(-,A)\) makes the differential zero, so \(\operatorname{Ext}_{A^e}^1(A,A)=A\). Separate one-sided splittings therefore do not establish a bimodule contraction. The M2 flux-cap splitting is genuinely bimodule-linear.

What happens if one inserts the flux twice? Write \(\mathfrak l=\mathfrak g/\mathbb C1\), and lift each polynomial Weyl symbol to its representative with zero constant term. The constant part of the commutator of two lifts is a scalar two-cocycle \(\omega\) on \(\mathfrak l\). Its class acts on the two-sided interval by cap product. Its square vanishes in algebraic cohomology at every numerical \(\hbar\ne0\), even though its four-input representative is nonzero. For example,
\[
 (\omega\wedge\omega)(x,y,x^3,y^3)=3\hbar^4 .
\]
In the Moyal formula the constant coefficient of \([x^d,y^d]\) for odd \(d\) is \(c_d=2d!(\hbar/2)^d\); mixed degrees contribute no constant. The displayed value is \(2c_1c_3\).

Vanishing of the square means finding a three-cochain \(H\) whose differential is the displayed four-cochain on every input. Such a primitive comes from cyclic homology of the polynomial Weyl algebra. The normalized Hochschild chain \(u=\hbar^{-1}x[y]\) has \(bu=1\). Its Connes boundary \(Bu=\hbar^{-1}(1[x|y]-1[y|x])\) generates top Hochschild homology and survives in cyclic degree two. Thus the unit gives a nonzero ordinary cyclic degree-two class. Choose an algebraic cyclic two-cocycle \(\Phi\) on unnormalized chains with \(\Phi(1,1,1)=1\). Antisymmetrizing \(\Phi\) gives a closed Lie three-cochain on \(\mathfrak g\). For the chosen lift \(s:\mathfrak l\to\mathfrak g\), let \(P\) be its restriction to the three lifted inputs and put \(\beta(a)=\Phi(1,1,sa)\). The cyclic cocycle identity gives \(dP=\omega\wedge(\omega-d\beta)\). Hence \(H=P+\omega\wedge\beta\) satisfies \(dH=\omega\wedge\omega\). Contraction by \(H\) gives a bimodule homotopy for the two successive cap operations. At rank one, where the cap in degree two is an isomorphism, the component of the *outgoing cut* from degree four to two degree-two factors is zero. The higher Tor groups themselves are not determined by this identity.

What transverse data would a field theory need to produce this homotopy? The Taylor jet of order \(L\) at the origin keeps the coefficients of monomials of total degree at most \(L\). Choose distinct odd \(d,e>L\). All four inputs \(x^d,y^d,x^e,y^e\) have zero \(L\)-jet. In each term of the differential of a three-cochain, two of those inputs remain untouched after bracketing the other two. A three-cochain depending only on \(L\)-jets therefore has zero differential on this tuple. Yet \(\omega\wedge\omega\) takes the value \(2c_dc_e\ne0\). This works for every finite \(L\). The algebraic primitive admits arbitrarily high jets of polynomial inputs. To realize it on a physical interval one must specify the endpoint actions and a contact homotopy in the allowed space of distributions, and recover both the cap and the outgoing cut with the chosen regularization.

At a fixed numerical \(\hbar\ne0\) even compact transverse support is impossible for a scalar distribution primitive with trivial coefficient action on all polynomial symbols. Suppose its kernel on the three arguments is supported inside a box of radius \(R\ge1\), with a distributional bound by derivatives through order \(L\) on that box. Test \(dH\) on \(x^{e-2},y^{e-2},x^e,y^e\) for odd \(e\ge3\). In a bracket \([x^i,y^j]\) with \(i,j\le e\), the coefficient for odd \(k\) is \(2(\hbar/2)^k\binom{i}{k}j!/(j-k)!\). Its absolute sum is at most \(2e!(2b)^e\), with \(b=\max(1,|\hbar|/2)\). Removing the scalar leaves this bound intact. At most four bracket terms in \(dH\) survive in the quotient by scalars. For \(e=3\), the bracket \([x,y]=\hbar 1\) already vanishes there. Each surviving term pairs the kernel with monomials of combined degree at most \(4e\) and coordinate exponents at most \(e\). Consequently \(|dH|\le C e^L e!(2bR^4)^e\), with \(C\) independent of \(e\). The required absolute value is \(8(e-2)!e!(|\hbar|/2)^{2e-2}\). Its extra factorial contradicts this estimate.

With formal \(\hbar\) the scalar equation has a compatible point-supported solution order by order. Choose the algebraic primitive at \(\hbar=1\) and average it under \((x,y)\mapsto(-x,-y)\). It vanishes on homogeneous triples of odd total degree. On a homogeneous triple of even total degree \(D\) multiply its value by \(\hbar^{D/2}\) and extend by trilinearity. In fact, putting \(\hbar=s^2\), substitution \((x,y)\mapsto(sx,sy)\) intertwines the bracket at \(s^2\) with the bracket at \(1\) and fixes constants. Pulling back the primitive therefore gives \(dH_\hbar=\omega_\hbar\wedge\omega_\hbar\). Its coefficient of order \(m\) reads only total input degree \(2m\), so it is a finite sum of derivatives of point masses. The physical interval also requires its two endpoint actions and outgoing cut.

## The matrix complex before taking cohomology {#ch14-the-matrix-complex-before-taking-cohomology}

At rank one the classical matrix equation \([X,Y]_{\mathrm{cl}}=0\) imposes no relation: two scalar matrices commute identically. If we nevertheless introduce an odd generator for this equation, its differential is zero and the generator survives. In higher rank the entries of the moment equation can have relations with one another. To see them, return to the matrix variables before imposing the equation. For each component of their moment map introduce an odd variable whose differential is that component. A relation between the components can then give a cycle containing odd variables. Work over \(R=\mathbb C[\hbar]\) with \(\hbar\) an indeterminate, so the same complex has a fibre at \(\hbar=0\). For \(\mathfrak g_N=\mathfrak{gl}_N\), define
\[
K_N^{\mathrm{full}}=
\left(W_\hbar(\mathfrak g_N\oplus\mathfrak g_N^*)
\otimes\Lambda(\Psi_1,\ldots,\Psi_{N^2})\right)^{GL_N}.
\]
Its even matrix variables satisfy
\([X_{ij},Y_{kl}]=\hbar\delta_{il}\delta_{jk}\); the exterior variables \(\Psi_a\) have cohomological degree \(-1\). In symmetric Weyl symbols, write \(\mu_a\) for the components of the classical matrix commutator. The differential is
\[
\delta F=\frac12\sum_a
\bigl(\mu_a\star\partial_{\Psi_a}F+
\partial_{\Psi_a}F\star\mu_a\bigr).
\]
For a single odd generator the formula reads \(\delta\Psi_a=\mu_a\), and it annihilates functions of \(X,Y\) alone. The classical matrix commutator is traceless at every rank, so \(\operatorname{Tr}\Psi\) is closed. On the displayed invariant algebra \(\delta\) is a square-zero derivation. The effective complex \(K_N^{\mathrm{eff}}\) further quotients by \(\operatorname{Tr}\Psi\). The absolute BRST complex also includes positive-degree gauge ghosts. These operations produce different complexes.

Curvature is already forced by one Weyl pair. An augmentation \(W_\hbar\to\mathbb C\) at numerical \(\hbar\ne0\) would send \([x,y]=\hbar\) to \(0=\hbar\). The constant term in this relation must instead survive in the dual construction. For the matrix model it becomes a degree-two curvature element.

To retain the particle permutations during duality, take the group algebra \(S=R[S_N]\) as the base of the tensor products. The unit in the symmetric particle sector will be its averaging idempotent. Let \(D_N\) be generated over this group algebra by exterior generators \(\xi_i,\eta_i\) of degree one and commuting generators \(u_i\) of degree two, which commute with the exterior algebra. Permutations act on the exterior indices, and the adjacent transposition \(s_i\) obeys
\[
s_i u_i-u_{i+1}s_i
=-(\xi_i-\xi_{i+1})(\eta_i-\eta_{i+1}),
\qquad
s_i u_j=u_js_i\quad(j\ne i,i+1).
\]
The differential is zero and the central curvature is
\[
w=\hbar\sum_i\xi_i\eta_i.
\]
Dualize each graded component as a left \(S\)-module and put \(C=\bigoplus_{r\ge0}\operatorname{Hom}_{S-}((D_N)_r,S)\). The coproduct is dual to multiplication with the tensor factors reversed. Identify the opposite group base by \(\sigma\mapsto\sigma^{-1}\). Form the curved cobar algebra \(\Omega_S(C,w)\), where the curvature is the functional dual to \(w\). This is the tensor algebra on the shifted coalgebra generators, with differential incorporating both coproduct and curvature. Let \(e=\frac1{N!}\sum_{\sigma\in S_N}\sigma\).

**Theorem: integral curved comparison.** For \(1\le N\le3\), there is a strictly unital \(R\)-linear \(A_\infty\) quasi-isomorphism
\[
K_N^{\mathrm{full}}\simeq_{A_\infty}e\Omega_S(C,w)e,
\]
without inverting or completing in \(\hbar\). Its derived zero fibre is formal, with algebra
\[
\left(\mathbb C[x_1,\ldots,x_N,y_1,\ldots,y_N]
\otimes\Lambda(\theta_1,\ldots,\theta_N)\right)^{S_N},
\qquad |\theta_i|=-1.
\]
The comparison uses ordered symbols and homotopy transfer over the polynomial parameter ring; the group-relative relations retain the permutation terms that ordinary symmetrization would lose. See [*The integral relative curved model*, main theorem](#ref-ch14-02).

Over \(\mathbb C(\hbar)\), the full comparison extends to every rank. It retains a nonzero fourth multiplication from \(N=3\) onward. Choose a transpose-equivariant minimal \(A_\infty\) model, where the differential vanishes, odd arities vanish, and \(m_n\) has degree \(2-n\). Writing \(H_N=H^*(K_N^{\mathrm{full}})\), the fourth operation defines a nonzero Hochschild class
\[
[m_4]\in HH^{4,-2}(H_N,H_N).
\]
The second superscript is the cohomological degree of this four-input operation. Its image under the comparison is the negative cup square of the binary comparison class in the odd particle coefficients. A three-cycle permutes three different labels, so this test first detects the square at rank three. For \(N\ge3\) the integral obstruction is divisible by \(\hbar^2\) and remains nonzero modulo \(\hbar^3\), even after adding coboundaries. At these ranks the polynomial complex and every nonzero numerical fibre are nonformal. For \(N=3,4\) the transpose-equivariant minimal model over \(\mathbb C(\hbar)\) has only \(m_2,m_4\). An \(m_6\) is first possible at \(N=5\). At rank one \(\mu=[X,Y]_{\rm cl}=0\), so the differential vanishes and the odd trace survives in the full complex. [Full matrix nonformality and curved duality, §§3–6](#ref-ch14-03)

There is also a category theorem for the separate cohomology algebra
\(B_N=(W_\hbar^{\otimes N}\otimes\Lambda(\theta_1,\ldots,\theta_N))^{S_N}\)
at zero Cherednik parameter and fixed numerical \(\hbar\ne0\). The symmetric idempotent is full in the Weyl–exterior crossed product, so it gives a Morita equivalence on ordinary unbounded derived module categories. Its curved dual uses equivariant coderived comodules or contraderived contramodules, the localizations appropriate to that curved coalgebra; the comodule presentation imposes local nilpotence of the even dual variables. This theorem concerns \(B_N\). The fourth operation explains why applying it to \(K_N^{\mathrm{full}}\) requires the full curved comparison. [*Curved duality for symmetric Weyl particles*, main theorem](#ref-ch14-04).

For a polynomial Hamiltonian \(f(x,y)\), the unary action is the symmetrized trace \(J(f)=\operatorname{Tr}\operatorname{Sym}f(X,Y)\). On \(x,y\) the ordinary commutator of the traces gives \([J(x),J(y)]=hN\), while \(J(1)=N\). To recover the Hamiltonian bracket one must divide the commutator by the Weyl parameter \(h\). On \(L_h=\mathbb Q[x,y,h]\), put \(P=\partial_x\otimes\partial_y-\partial_y\otimes\partial_x\) and define
\[
 f\star g=m\exp\left(\frac h2P\right)(f\otimes g),
 \qquad b_h(f,g)=\frac{f\star g-g\star f}{h},
\]
where \(m\) is ordinary multiplication. The exponential terminates on polynomial inputs, the numerator is divisible by \(h\), and \(b_h(x,y)=1\). To vary the rank, use the effective cyclic-trace complex \(K\) over \(\mathbb Q[\nu,h]\), with \(\operatorname{Tr}1=\nu\), \(\operatorname{Tr}\Psi=0\), and divided graded commutator \([\, ,\,]_h\). Evaluation at \(\nu=N\) gives a chain map to \(K_N^{\mathrm{eff}}\) over \(\mathbb Q[h]\).

An arity-\(n\) component \(\Phi_n\) takes \(n\) Hamiltonians to a cochain of degree \(1-n\) in \(K\). The higher components give the homotopies by which \(J\) preserves brackets. For example, \(dF_2(f,g)=[J(f),J(g)]_h-J(b_h(f,g))\). On \(x,y\) the two terms agree because \([J(x),J(y)]_h=\nu=J(1)\). More generally, adding a closed two-input cochain to \(F_2\) leaves \(dF_2(f,g)\) unchanged for every \(f,g\). The next identity involves \(F_2\) itself, so the choice of this cochain matters on three inputs. Write \(\delta_J\) for the Chevalley–Eilenberg formula using the divided adjoint action of \(J\) on cochains. Fix the lower maps
\[
 \Phi_1=J,\qquad \Phi_2=F_2+\widehat s_h,\qquad
 \Phi_3=F_3+G_3+Z_3.
\]
Transposition acts on the antighost by \(\Psi\mapsto-\Psi^{\mathsf T}\). Here \(F_2,F_3\) are the transpose-even choices with \(dF_3=\delta_JF_2\). The closed transpose-odd lift \(\widehat s_h\) comes from the two-point Moyal cocycle given below, and \(dG_3=\delta_J\widehat s_h\) with \(G_3\) transpose-odd. The closed correction \(Z_3\) is the one adapted to the particle tree solution in Lemma 12.1. At each rank, normal-order the matrix variables with lower triangular entries first, restrict to the diagonal matrices, then average over particle permutations. Applied to \(\Phi_3\), this gives the permutation average of the ternary particle tree map. [The binary cocycle and the tree normalization](#ref-ch14-05)

**Theorem (Hamiltonian transport through total degree 24).** Use the universal homology basis of ordered monomials in \(J(m)\) and \(z(m)=\operatorname{Tr}((\operatorname{Sym}m)\Psi)\), with \(m\) nonconstant and each odd generator \(z(m)\) used at most once. For the lower maps above, start with the homogeneous, alternating, \(\mathfrak{sl}_2\)-equivariant extension through arity five of Theorem 12.6. Its higher components vanish if an input is constant or quadratic. Keeping \(\Phi_1,\ldots,\Phi_4\) fixed, one can change \(\Phi_5\) by a closed cochain supported on five-tuples of total polynomial degrees \(22\) and \(23\). The resulting homotopy Lie map extends in every arity on tuples of total degree \(D\le24\), including tuples with linear inputs. Here \(D\) is the sum of the degrees in \(x,y\) on homogeneous inputs. With weights \(\deg(x,y,h,\nu)=(1,1,2,0)\), the physical weight shift of \(\Phi_n\) is \(2-2n\). The construction is polynomial over \(\mathbb Q[\nu,h]\) and specializes to every positive rank over \(\mathbb Q[h]\). [*Polynomial Hamiltonian transport*, Theorem 14.2](#ref-ch14-05)

**Proof.** Each antighost has physical weight two. The sixth defect has cohomological degree \(-4\) and output weight \(D-10\). In the ordered homology basis, four odd trace factors have four distinct nonconstant monomial labels. Their degrees sum to at least \(1+1+2+2=6\). The four antighosts add eight, so the first possible output has weight \(14\), at \(D=24\). Its coefficient space over \(\mathbb Q[\nu]\) is the three-dimensional \(\mathfrak{sl}_2\)-module \(V_2\) of highest weight two.

Let \(\mathfrak q=(x,y)^3\subset\mathbb Q[x,y]\) be the span of the monomials of degree at least three, with the Poisson bracket. Give each homogeneous polynomial of degree \(a\) weight \(a-2\). Six such inputs of total degree 24 have weight 12. The obstruction identity makes the sixth defect on them a cocycle with trivial coefficient action. In torus weight two the Chevalley–Eilenberg chain groups \(C_5,C_6,C_7\) at weight 12 have dimensions \(720,335,52\). Modulo the prime \(1{,}000{,}003\) the boundary ranks are \(284\) for \(d_6\) and \(51\) for \(d_7\). Over \(\mathbb Q\) these are lower bounds, and \(d_6d_7=0\) bounds their sum by 335. Since \(284+51=335\), the sixth homology has no vector of torus weight two, hence no copy of \(V_2\). The cocycle kills \(\operatorname{im}d_7\). Its restriction to \(\ker d_6\) therefore induces an equivariant map from sixth homology to the \(V_2\) coefficient. That map is zero because the homology has no copy of \(V_2\). The cocycle thus factors through \(\operatorname{im}d_6\subset C_5\). A rational equivariant splitting extends this factor to a five-cochain on \(C_5\), still at weight \(12\). Five inputs of weight \(12\) have total polynomial degree \(12+2\cdot5=22\). The two translations generated by \(x,y\) extend it to tuples with one or two linear inputs, using a second five-cochain in degree 23. Three linear inputs vanish by alternation. Subtracting a closed lift of the two pieces from \(\Phi_5\) makes the sixth defect exact. Obstructions of arity at least seven have minimum total degree at least 30, so their primitives can be chosen successively throughout the stated range. [*Polynomial Hamiltonian transport*, Lemma 14.1 and Theorem 14.2](#ref-ch14-05) ∎

There is a different way to extend the *input degrees* while keeping the arity at five. Let \(E\) be the normalized fifth-obstruction cocycle with coefficients in \(H^{-3}(K)\), and let \(\delta_h\) be the Chevalley–Eilenberg differential with the induced Hamiltonian action on this cohomology. Theorem 13.5 gives \(\nu E=\delta_h\widehat\zeta\) on all polynomial inputs. Thus \(\widehat\zeta/\nu\) is a primitive over \(\mathbb Q[\nu,\nu^{-1},h]\). At a positive integer rank \(N\) one divides only by \(N\), giving arity five in every degree over \(\mathbb Q[h]\). At \(1\le N\le4\) the rank bound on negative cohomology gives all arities over \(\mathbb Q[h]\). At \(\nu=0\) the identity reduces to \(\delta_h(\widehat\zeta|_{\nu=0})=0\). It says that the specialized cochain is closed and gives no equation with \(E|_{\nu=0}\) on the left.

**Conditional theorem (universal arity five with a fixed ternary map).** Assume the universal Poincaré–Birkhoff–Witt homology model with cycle lifts, injectivity after specialization at sufficiently large positive ranks in each fixed weight, and the ordered-symbol comparison for the effective trace complex. Assume also the all-weight calculation of \(H_3(\mathfrak q)\), in which no summand of highest weight \(m\le w-6\) occurs in weight \(w\). Then the specified \(\Phi_1,\Phi_2,\Phi_3\), including the same \(Z_3\), extend through arity five on every polynomial input over \(\mathbb Q[\nu,h]\). A closed adjustment of \(\Phi_4\) is allowed. [*Universal arity-five obstruction*, §§5–8](#ref-ch14-05)

In the ordered symbols modulo the total odd trace, the third-homology condition supplies a primitive for the difference between the ternary brane and tree maps. Write \(\bar\lambda\) for this primitive, \(\bar\Psi_2\) for the binary tree map in the same quotient and \(a\) for averaging the ordered symbols. The four-cochain is \(\Xi=-a([\bar\Psi_2,\bar\lambda]_{\mathrm{cup}})\), with the signed shuffle in the cup bracket. At every sufficiently large rank \(\delta_h\Xi\) evaluates to \(E\). For each tuple both sides are polynomial in \(\nu,h\), and stable injectivity gives \(\delta_h\Xi=E\) before specialization. Thus \(\widehat\zeta-\nu\Xi\) is a closed lift of \(\widehat\zeta\bmod\nu\). The all-degree arity-six obstruction over \(\mathbb Q[\nu,h]\) remains open.

The coupling equation uses full Hom in each arity and a product over arities. Each individual Taylor value is polynomial. To use the ordinary associative Maurer–Cartan equation, replace the source bracket by \(hb_h\) and \(\Phi_n\) by \(h^{n-1}\Phi_n\). This recovers the ordinary commutator \(hN\) on \(x,y\). Comparing these algebraic operations with an independently quantized bulk and line defect requires a physical coupling with that normalization. [Paquette–Williams, §§5–6](https://arxiv.org/abs/2110.10257).

## D3 branes: chiral operators and Hilbert-scheme sections {#ch14-d3-branes-chiral-operators-and-hilbert-scheme-sections}

A stack of D3 branes has a four-dimensional worldvolume. Its \(\mathcal N=4\) gauge theory has a protected operator sector on a complex plane with insertion coordinate \(z\). A second plane parametrizes the algebraic geometry of the reduction. A point of \(M_N=\operatorname{Hilb}^N(\mathbb C^2)\) is an ideal \(I\subset\mathbb C[x,y]\) for which \(\dim_{\mathbb C}\mathbb C[x,y]/I=N\). On this quotient, multiplication by \(x,y\) gives two commuting matrices, and the class of \(1\) is a cyclic vector. For instance \(I=(x^2,y)\) gives the basis \(1,x\), with \(x\) acting nilpotently. This is a length-two subscheme supported at one point. The sheaf of chiral fields lives over \(M_N\), while its operator products use separation in \(z\). Which of its global sections come from polynomial gauge operators? [Arakawa–Kuwabara–Möller, §§2.3, 4.1 and 5.1](https://arxiv.org/abs/2309.17308)

The framed relative BRST complex contains adjoint symplectic bosons \(X,Y\), a fundamental bosonic pair \(\gamma,\beta\), a fundamental fermionic pair \(\psi,\phi\), and gauge ghosts \(b,c\). Matter fields have weight \(1/2\), and \(b,c\) have weights \(1,0\). With the following ordering, the nonzero contractions are
\[
\begin{gathered}
Y_{ij}(z)X_{kl}(w)\sim\frac{\delta_{il}\delta_{jk}}{z-w},
\qquad \beta_i(z)\gamma_j(w)\sim\frac{\delta_{ij}}{z-w},\\
\psi_i(z)\phi_j(w)\sim\frac{\delta_{ij}}{z-w},
\qquad b_{ij}(z)c_{kl}(w)\sim\frac{\delta_{il}\delta_{jk}}{z-w}.
\end{gathered}
\]
Reverse products follow from vertex skew-symmetry. With normal ordering understood, set
\[
J_{ij}=(XY-YX)_{ij}+\gamma_i\beta_j+\psi_i\phi_j,
\qquad j=\sum_{ij}c_{ji}J_{ij}+\operatorname{tr}(bcc),
\qquad Q=j_{(0)}.
\]
**Definition (framed relative BRST complex).** On the polynomial creation states of these fields, impose \((b_{ij})_{(0)}v=(Qb_{ij})_{(0)}v=0\) for every \(i,j\) and keep the differential \(Q\). The first set of equations removes the undifferentiated \(c\) ghosts and the second imposes gauge invariance. Write \(K_N=H^0(C_{\mathrm{fr}},Q)\). The stable bosonic moment reduction \(([X,Y]+\gamma\beta=0)^{\mathrm{st}}/GL_N\) is \(M_N\), where stability means that \(\gamma\) generates \(\mathbb C^N\) under \(X,Y\). Localizing the formal free fields there gives the BRST sheaf \(\mathcal D\). Put
\[
V_N=\Gamma(M_N,\mathcal D)_{\mathrm{fin}}/(\hbar-1).
\]
The subscript means the torus-finite part, taken before specialization. Homogenizing a polynomial operator, restricting to the stable locus and passing to the sheaf defines \(\alpha_N:K_N\to V_N\). To test the image in this target, integrate the weight-one field \(\chi^-=\sum_i:\phi_i\gamma_i:\) on a small positively oriented contour about the insertion, with measure \(dz/(2\pi i)\). Its zero mode is the simple-pole coefficient and preserves conformal weight.

**Theorem: the exact chiral image.** For every \(N\ge1\), the framed relative complex has cohomology only in degree zero, in every conformal weight. Its algebra \(K_N\) is simple, with central charge \(-3N^2\) and a nondegenerate invariant form normalized on the vacuum. The natural map is injective and
\[
\alpha_N(K_N)=\ker(\chi^-_{(0)}:V_N\to V_N),
\qquad \chi^-=\phi\gamma.
\]
There is an odd global section \(\tau\) of conformal weight zero satisfying
\[
\chi^-_{(0)}\tau=N,
\qquad
V_N=\alpha_N(K_N)\oplus\tau_{(-1)}\alpha_N(K_N)
\]
as graded vector spaces. Thus the map is not surjective at any rank. The complementary factors are
\[
K_N=W_N\otimes\mathrm{Sb}\otimes\mathrm{SF},
\qquad
V_N=W_N\otimes\mathrm{Sb}\otimes bc.
\]
Here \(\mathrm{Sb}\) consists of the trace symplectic bosons and \(W_N\) is the common commuting factor. The two fermionic factors can be read in the same normalization: the \(bc\) pair has \(b=\chi^-/N\) of weight one and \(c=\tau\) of weight zero, with \(b_{(0)}c=1\). The symplectic-fermion algebra \(\mathrm{SF}\) is generated by \(b,\partial c\). The total unframed relative cohomology is \(K_N\) for \(\mathfrak{gl}_N\) and \(W_N\) for \(\mathfrak{sl}_N\), with ghost number matching framing fermion number. For \(N\ge2\), the traceless quadratic currents generate affine \(\mathfrak{sl}_2\) at level \(-(N^2-1)/2\); their zero modes give the Lie action used below. See [*Global sections on the Hilbert scheme*, Theorems A–B](#ref-ch14-06).

Where \(\gamma\) is cyclic for \(X\), write \(B_\gamma=(\gamma,X\gamma,\ldots,X^{N-1}\gamma)\) and \(B_\psi=(\psi,X\psi,\ldots,X^{N-1}\psi)\). The odd section is \(\tau=\operatorname{tr}(B_\psi B_\gamma^{-1})\) on this chart and extends globally. The zero mode of \(\chi^-\) replaces the fermionic column generator \(\psi\) by \(\gamma\). Its value on the trace is therefore \(\operatorname{tr}(B_\gamma B_\gamma^{-1})=N\), while it vanishes on the polynomial image. This separates \(\tau\) from the polynomial image. At rank one the test reduces to \(b_{(0)}c=1\) and \(b_{(0)}\partial c=\partial\mathbf1=0\).

To prove that the image exhausts \(V'=\ker\chi^-_{(0)}\), one needs to find a polynomial field in every nonzero submodule of \(V'\). On the cyclic chart the trace fields \(\operatorname{tr}(X^{j+1})/(j+1)\) and the framed fields \(\phi X^m\gamma\), for \(0\leq j,m<N\), already lie in the polynomial image. Their nonnegative modes act on the chart's creation variables. The trace modes differentiate the conjugate even variables with a minus sign. Once those variables have been removed, the framed modes differentiate the odd coordinates of \(B_\gamma^{-1}\psi\). In any nonzero submodule, apply a longest string of these modes with nonzero result. The string terminates because the number of conjugate and odd coordinates decreases. What remains is a nonzero polynomial in the creation modes of the trace and framed fields. Simplicity of \(K_N\) then puts the vacuum in that submodule.

The invariant pairing of \(K_N\) with \(V'\) restricts on the polynomial image to its nondegenerate vacuum-normalized form. Weight by weight, \(V'\) splits as the image and its orthogonal complement. Invariance makes that complement a \(K_N\)-submodule. A nonzero complement would contain the vacuum by the chart argument, although the vacuum pairs to \(1\) with itself. Thus the complement vanishes. [The cyclic-chart proof of the image theorem](#ref-ch14-06)

The missing global section \(\tau\) was detected after torus-finite specialization at \(\hbar=1\). For \(N\ge2\) specialization also kills a nonzero class in sheaf degree one. To exhibit it, start with \(\sum_i\phi_i\psi_i\), a global invariant of the classical sheaf \(\mathcal D/\hbar\mathcal D\). Choose lifts on the cyclic charts. On an overlap their difference, in the order second lift minus first, is \(\hbar\) times the logarithmic derivative of the determinant transition function. Dividing the difference by \(\hbar\) gives a degree-one Čech cocycle. Its class \(e_0\) is the image of the invariant under the connecting homomorphism for multiplication by \(\hbar\), the Bockstein. Write \(e_r\) for its \(r\)-th translate along the insertion coordinate.

Over \(R=\mathbb C[[\hbar]]\), the subalgebra generated by these classes and the vacuum under the normally ordered cup product is
\[
\frac{R\otimes\Lambda(e_0,e_1,\ldots)}
{(\hbar e_r,\Lambda^{\ge N})}.
\]
Each \(e_r\) has sheaf degree one, intrinsic even parity and conformal weight \(r+1\). Its exterior sign comes from sheaf degree. Products with increasing indices and fewer than \(N\) factors are nonzero and survive reduction modulo every \(\hbar^m\), \(m\ge1\). Only finite sums and products enter this subalgebra. Its positive-degree classes are killed by \(\hbar\), so they disappear when \(\hbar\) is set to one in the torus-finite part. A map from jets to differential forms detects the products by powers of the first Chern class of the tautological determinant. A Hartogs–Leray argument extends this test from the cyclic charts. For every \(m\ge1\), the sheaves \(\mathcal D\) and \(\mathcal D/\hbar^m\mathcal D\) have nonzero cohomology in precisely the degrees \(0,\ldots,N-1\). [*Global sections on the Hilbert scheme*, §§21–22](#ref-ch14-07)

The determinant subalgebra does not exhaust the higher cohomology. In rank two, remove the free spectator factors and decompose the full reduced torsion into \(\mathfrak{sl}_2\)-representations. Fix the positive reduced fermion number \(r\). Its least possible oscillator energy is \(e_{\min}=0+1+\cdots+(r-1)=r(r-1)/2\). Write \(q=e-e_{\min}\) for the integer energy index above this minimum. The conformal grading subtracts \(r/2\) from \(e\). For example \(r=1,q=3\) gives \(e=3\) and \(H=5/2\). Put
\[
a=\left\lfloor\frac{r-1}{2}\right\rfloor,
\quad H=\frac{r(r-2)}2+q,
\quad d=2q-r,
\quad \mu=a-\frac r2.
\]
Torsion begins at \(q=a+1\). For every subsequent \(q\), its highest-weight-\(d\) component is
\[
R/(\hbar^{q-a})[\mu]\otimes\operatorname{Sym}^{d}\mathbb C^2,
\]
where \([\mu]\) denotes the torus-weight shift. The next-largest spin is also determined, giving the complete first two occurrence representations. For \(r=1\), these are
\[
\begin{aligned}
H=\tfrac12:&\quad R/(\hbar)[-\tfrac12]\otimes\mathbb C^2,\\
H=\tfrac32:&\quad
R/(\hbar^2)[-\tfrac12]\otimes\operatorname{Sym}^3\mathbb C^2
\;\oplus\;
R/(\hbar)[-\tfrac12]\otimes\mathbb C^2.
\end{aligned}
\]
The divided Lie action is defined on the torsion-free sheaf before taking cohomology. A lower-spin block can also be calculated. Remove the free symplectic-boson and ghost spectators. At rank two, \(r=1,\ q=3\) and conformal weight \(5/2\), the full highest-weight-one torsion in the individual completed block is
\[
 \bigl(R/(\hbar)[-\tfrac12]\oplus R/(\hbar^2)[-\tfrac12]
              \oplus R/(\hbar)[+\tfrac12]\bigr)\otimes\mathbb C^2,
 \qquad R=\mathbb C[[\hbar]].
\]
The brackets give the torus degrees at which the generators are born. In the two-chart description the torsion intervals at flavour weight \(-1\) are \([0,3),\,2[0,2),\,[0,1),\,[1,2)\), before subtracting \(r/2\) from each birth. An irreducible \(\mathfrak{sl}_2\)-module of odd highest weight at least three contributes one copy of the same multiplicity space at each of the flavour weights \(-3,-1\). A doublet contributes only at \(-1\) among these two weights. The weight \(-3\) calculation gives the intervals \([0,3),[0,2)\) from the larger irreducibles. Removing one copy of each from the weight \(-1\) list leaves \([0,1),[0,2),[1,2)\) for the doublets. These are polynomial \(\mathbb C[\hbar]\)-blocks of lengths \(1,2,1\). Completing the individual block gives the three displayed doublets. Each length is also the page of its first nonzero \(\hbar\)-filtration Bockstein, since its two-term differential is multiplication by that power of \(\hbar\). The last doublet starts one torus degree later than the first. [*Global sections on the Hilbert scheme*, §§23–25](#ref-ch14-06).

::: figure fig-d3-three-torsion-intervals

In the first row of the figure the relation \(\hbar v_1=0\) has torus weight \(1/2\). In the last row \(\hbar v_3=0\) has weight \(3/2\), although both intervals have length one. Allow any reduced fermion number \(f\in\mathbb Z\). A finite chart interval \([i,j)\) has a generator \(v\) of torus weight \(\mu=i-f/2\). Since \(\hbar\) has weight one, its relation \(\hbar^{j-i}v=0\) has weight \(\delta=j-f/2\).

::: theorem {#ch14-rank-two-relation-weights title="Relation weights in rank-two chiral cohomology"}
At fixed conformal weight \(H\), reduced fermion number \(f\) and flavour weight \(F\), every finite torsion interval \([i,j)\) in the reduced two-chart complex on \(\operatorname{Hilb}^2(\mathbb C^2)\) satisfies
\[
                 2j-|f|\ \ge\ |F|.
\]
In an irreducible multiplet of highest weight \(m\), the relation has torus weight \(j-f/2\ge m/2+\max(0,-f)\).
:::

::: proof {#ch14-proof-rank-two-relation-weights}
Work over \(\mathbb C[\hbar]\). In an ordered chart monomial, omit the power of the base coordinate. Let \(P,B,X,C\) count the momenta, odd \(b\)-factors, positive-order \(x\)-jets and odd \(c\)-factors, respectively. The filtration degree is \(k=P+B\), the charge is \(f=C-B\), and the flavour before inserting the base power is \(w=2P-2X-f\). Thus \(w=2k-f-2(X+B)\le 2k-|f|\), since \(B\ge\max(0,-f)\).

The first base coordinate \(x\) has flavour \(-2\), and its reciprocal \(y=x^{-1}\) has flavour \(2\). Both have filtration degree zero. Before the base power is inserted, a monomial type of flavour \(w\) on the first chart has flavour \(-w\) on the second. To reach total flavour \(F\), its base factor must be \(x^{(w-F)/2}\) on the first chart and \(y^{(w+F)/2}\) on the second. Since \(w=2P-2X-f\), both exponents are integers exactly when \(F\equiv f\pmod{2}\). Only integral Laurent powers occur on the overlap, so the block is empty in the other parity. In the admissible parity, quotienting by sections regular on the first chart keeps the negative \(x\)-powers as rows, giving \(w<F\). The second-chart columns are the regular monomials with nonnegative \(y\)-power, giving \(w\ge-F\). For the vacuum monomial \(1\) at \(H=f=0\), flavour \(1\) would require exponents \(-1/2\) and \(1/2\). At flavour \(2\) the column \(y\) maps to the row \(x^{-1}\) with coefficient one.

If \(2j-|f|<-F\), there are no columns through degree \(j\) to impose a relation. If \(2j-|f|<F\), every overlap row through that degree survives. On the full overlap the chart change and its inverse are polynomial in \(\hbar\), with entries from degree \(\ell\) to \(k\) proportional to \(\hbar^{\ell-k}\). Evaluating the two matrices at \(\hbar=1\) gives inverse filtered maps, hence inverse maps on each associated graded piece. The newly admitted degree-\(j\) columns have independent leading terms. No combination of them can kill a class from an earlier degree. These two cases exclude a finite interval ending at \(j\) whenever \(2j-|f|<|F|\). Completion of the finite block preserves its differential \(\hbar^{j-i}\). The divided currents preserve torus degree and commute with \(\hbar\), so an interval in the multiplicity space of highest weight \(m\) occurs at flavour \(m\) itself. Applying the inequality there gives the bound on \(\delta\).
:::

At \(f=r>0\) the top component has relation weight \((a-r/2)+(q-a)=q-r/2=d/2\) for \(q\ge a+1\). For \(q\ge a+2\) every nonzero summand of the next component has birth plus length \(q-1-r/2=(d-2)/2\). Both families attain the bound. At \(H=7/2\) and \(f=-1\) the doublet has interval \([1,2)\) in both flavours \(-1,1\). Its relation has weight \(5/2\), strictly above the bound \(3/2\).

At charge \(f=2\) the first torsion sector has excess energy \(q=1\), oscillator energy \(e=2\) and conformal weight \(H=1\). Write \(v_n=T^nv/n!\) for the jets of a reduced chart field, with \(T\) translation along the insertion coordinate. After omitting the Laurent power of \(x\), the three monomials of this energy and charge are \(c_0c_2,\ x_1c_0c_1,\ p_0c_0c_1\), where \(p\) is the momentum conjugate to \(x\) and \(c\) is the odd field of charge one. Their pairs \((k,w)\) of filtration degree and flavour are \((0,-2),(0,-4),(1,0)\). At flavour \(0\) the two degree-zero rows are \(x^{-1}c_0c_2\) and \(x^{-2}x_1c_0c_1\). In this order the single degree-one column of the chart transition is \((\hbar,-\hbar/2)^{\mathsf T}\). Its image is \(\hbar\) times a primitive row vector, giving one interval \([0,1)\) and one free generator at flavour \(0\). At flavour \(-2\) there is one degree-zero row and no column. The difference \(2-1=1\) of the degree-zero dimensions counts one singlet. Subtracting the interval lists puts \([0,1)\) in its multiplicity space.

For every positive even charge \(f=2s\), the first torsion energy is \(q=s\). The top-component formula gives highest weight zero and the interval \([s-1,s)\). Thus its torus birth stays at \(-1\) and its relation at \(0\) as the charge increases. To bound the birth for any specified horizontal representation, compare two successive flavours of the same parity at the degree of its generator. [The first positive-charge intervals, Theorems 23.3 and 24.2](#ref-ch14-06)

::: theorem {#ch14-generator-weights-at-fixed-horizontal-spin title="Generator weights at fixed horizontal spin"}
Fix conformal weight \(H\) and reduced fermion number \(f\in\mathbb Z\) in the polynomial two-chart complex on \(\operatorname{Hilb}^2(\mathbb C^2)\). If its degree-one cohomology in torus weight \(\ell-f/2\) contains \(\operatorname{Sym}^m\mathbb C^2\) under the divided horizontal \(\mathfrak{sl}_2\) action, then \(2\ell-|f|\ge -m-2\). Every finite interval \([i,j)\) in the multiplicity space of this representation satisfies
\[
 |f|-2i-2\ \le\ m\ \le\ 2j-|f|,\qquad i+j\ \ge\ |f|-1 .
\]
The degree and interval bounds hold after completion of each fixed sector. The first positive even-charge singlets attain equality in both interval bounds and in the degree bound at birth.
:::

::: proof {#ch14-proof-generator-weights-at-fixed-horizontal-spin}
Use shifted degree \(\ell\), obtained by adding \(f/2\) to torus weight. A chart type of degree \(k\le\ell\) contributes in this degree with the single power \(\hbar^{\ell-k}\). Its flavour before the Laurent power is inserted satisfies \(w\le 2k-|f|\) by the [two-chart calculation](#ch14-proof-rank-two-relation-weights). Occurrence of highest weight \(m\) requires \(m\equiv f\pmod 2\), so both \(-m\) and \(-m-2\) are admissible flavours. Suppose \(2\ell-|f|<-m-2\). Then every eligible type has \(w<-m-2\). It contributes one row at each flavour, since the row condition is \(w<F\). There are no columns at either flavour, since these require \(w\ge m\) and \(w\ge m+2\), respectively. The two cokernels in degree \(\ell\) have equal dimension.

At fixed \(H,f\) the oscillator energy \(e=H+f/2\) bounds the positive-energy factors, and the only zero-energy non-base jet is the odd \(c_0\), which occurs at most once. Thus there are finitely many types. At sufficiently negative flavour there is no row. At sufficiently positive flavour every type gives a regular second-chart column, so the invertible overlap transition spans the first-chart quotient. Only finitely many flavours therefore contribute in degree \(\ell\). The divided zero modes preserve \(H,f,\ell\) and give a finite-dimensional \(\mathfrak{sl}_2\)-module on this cohomology. Each irreducible containing flavour \(-m-2\) contributes once at \(-m\) as well. By complete reducibility the difference of the two dimensions counts the copies of \(\operatorname{Sym}^m\mathbb C^2\). Equal dimensions exclude this representation, which proves the degree bound for the whole cohomology.

Multiplication by \(\hbar\) commutes with the horizontal action. An interval in the multiplicity space supplies the representation at its birth \(\ell=i\), and supplies the same interval at flavour \(m\). The degree bound gives the first inequality and the [relation bound at flavour \(m\)](#ch14-rank-two-relation-weights) gives the second. Combining them gives \(i+j\ge |f|-1\). In each finite sector homogeneous diagonalization over \(\mathbb C[\hbar]\) gives the same graded generators and interval differentials after completion. For the singlet \([s-1,s)\) at \(f=2s\), both bounds on \(m\) give zero and \(i+j=2s-1\).
:::

Each individual polynomial torsion interval specializes to zero at \(\hbar=1\). When all the chart complexes are completed together, the primitives for a family of intervals must belong to a single completed direct sum. We take the finite sums of torus weight vectors in its cohomology before specializing.

::: corollary {#ch14-torsion-at-torus-finite-specialization title="Torsion intervals at torus-finite specialization"}
Complete the direct sum of the reduced rank-two chart complexes \(\hbar\)-adically, take the torus-finite part of \(H^1\), then specialize at \(\hbar=1\). The torsion intervals contribute zero exactly when their torus birth weights have a uniform lower bound. Otherwise their contribution has complex dimension \(2^{\aleph_0}\).
:::

::: proof {#ch14-proof-torsion-at-torus-finite-specialization}
For weights \(s_\ell\) indexed by the finite intervals, let \(V(s)\) consist of scalar families \((c_\ell)\) with only finitely many nonzero entries at weights \(s_\ell\ge B\) for each real \(B\). In torus weight \(u\), a generator of weight \(\mu_\ell\) carries the power \(\hbar^{u-\mu_\ell}\) whenever that exponent is a nonnegative integer. Completion allows only finitely many terms below any fixed power of \(\hbar\). After specialization the generators thus give \(V(\mu)\) and the relations give \(V(\delta)\). The torsion-interval contribution is \(V(\mu)/V(\delta)\). [The two-chart specialization formula](#ref-ch14-06)

Every \(\delta_\ell\ge0\), so \(V(\delta)\) consists of the finite-support families. A uniform lower bound on \(\mu_\ell\) gives the same space for \(V(\mu)\). Otherwise choose distinct intervals with \(\mu_{\ell_n}\le-n\). On these indices the sequences \((z^n)_{n\ge1}\), \(z\in\mathbb C^\times\), are linearly independent modulo finite support by the Vandermonde determinant on consecutive indices. This gives the asserted dimension, since the set of intervals is countable. Restoring the spectator monomials shifts both endpoints by the same nonnegative weight, with shift zero for the vacuum, so the criterion still applies.
:::

::: corollary {#ch14-specialization-at-bounded-horizontal-spin title="Specialization at bounded horizontal spin"}
The finite torsion intervals of bounded horizontal highest weight contribute zero to torus-finite specialization. On the infinite support of any representative of a nonzero class in the torsion-interval contribution, the reduced births \(\mu\) tend to \(-\infty\), while the reduced charges \(f\), highest weights \(m\), relation weights \(\delta\) and lengths \(j-i\) tend to \(+\infty\). The same assertions hold with the global spectator factors adjoined before completion.
:::

::: proof {#ch14-proof-specialization-at-bounded-horizontal-spin}
At fixed \(H,f\), the ranks of multiplication by powers of \(\hbar\) add over the horizontal irreducibles. A finite interval \([i,j)\) contributes one to the rank from shifted degree \(a\) to \(b\ge a\) exactly when \(i\le a\le b<j\). Taking differences of successive ranks recovers the multiplicity of each interval. Thus the intervals in the specialization formula can be counted with their horizontal highest weights. Equivalently, the number of intervals with given endpoints in the highest-weight-\(m\) multiplicity space is their count at flavour \(-m\) less their count at \(-m-2\). This is the subtraction used for the three doublets.

For each such interval the [bounds on the endpoints](#ch14-generator-weights-at-fixed-horizontal-spin) give
\[
 \mu\ge \max(0,-f)-\frac{m+2}{2},\qquad
 \mu+\delta\ge 2\max(0,-f)-1 .
\]
For \(m\le M\) every birth is at least \(-(M+2)/2\). A scalar family in \(V(\mu)\) supported there has finite support and represents zero in the quotient. On an infinite support of a nonzero class, only finitely many births lie at or above any prescribed threshold. Hence \(\mu\to-\infty\). Since \(i\ge0\), the identity \(\mu=i-f/2\) forces \(f\to+\infty\). The first inequality forces \(m\to+\infty\), and the second gives \(\delta\ge-1-\mu\), so both \(\delta\) and \(j-i=\delta-\mu\) tend to \(+\infty\). A spectator monomial leaves the reduced horizontal representation and length unchanged and adds a nonnegative weight to both endpoints. If the shifted births tend to \(-\infty\), so do the reduced births.
:::

What can the finite quotients of the formal cohomology detect before specialization? Put \(t=\hbar\), \(R=\mathbb C[[t]]\), and let \(E\) be sheaf cohomology in degree one of the reduced rank-two model. The completion of a direct sum with basis indexed by \(I\) consists of the restricted families
\[
 S(I)=\left\{(a_\alpha)\in\prod_{\alpha\in I}R\ \middle|
  \#\{\alpha:a_\alpha\notin t^rR\}<\infty\ \text{for every }r\ge1\right\}.
\]
For example, at charge one take the lowest flavour \(F=1-2n\) of the top component at each excess energy \(q=n\ge1\). The resulting intervals \([0,n)\) have birth weight \(-1/2\) and differential \(t^n\). In these target coordinates the family \((t^n)_{n\ge1}\) is restricted. Its only coordinatewise primitive is \((1)_{n\ge1}\), which fails the restriction already at \(r=1\). The family therefore defines a nonzero class of \(E\). For each \(r\) its first \(r\) entries are a finite boundary, and the remaining tail is \(t^r\) times a restricted family. Thus the class belongs to \(\bigcap_{r\ge1}t^rE\). Tensoring with the spectator vacuum gives the same nonzero class in the full sheaf. Its entries have weights \(n-1/2\). [The charge-one family and its completed complex, Theorem 18.1](#ref-ch14-06)

Could the same kernel contain a class of a single torus weight? In an abstract diagonal complex with the same differentials \(t^n\), assign the births \(1/2-n\). Then every entry of \((t^n)_n\) has weight \(1/2\), and its primitive still fails the restriction. These intervals have \(\mu_n+\delta_n=1-n\), which violates the geometric bound \(\mu+\delta\ge-1\) for \(n>2\).

::: theorem {#ch14-torus-finite-classes-and-separated-completion title="Torus-finite classes and separated completion in rank two"}
Let \(E\) be \(H^1\) of the formal chiral sheaf on \(\operatorname{Hilb}^2(\mathbb C^2)\) with its geometric two-chart transition, either reduced or with the global symplectic-boson and \(bc\) factors adjoined before completion. Write \(\widehat E_{\rm sep}=\varprojlim_{r\ge1}E/t^rE\), with \(t=\hbar\) of torus weight one. For a module \(M\) with this torus action, let \(M_{\rm fin}\) be its finite sums of weight vectors. The natural projection induces an isomorphism of graded \(\mathbb C[t]\)-modules
\[
 E_{\rm fin}\ \xrightarrow{\ \sim\ }\ (\widehat E_{\rm sep})_{\rm fin}
\]
and an isomorphism of their specializations at \(t=1\).
:::

::: proof {#ch14-proof-torus-finite-classes-and-separated-completion}
Use homogeneous diagonal coordinates in each finite polynomial chart complex. The changes of basis and their inverses take each basis vector to a finite sum with nonnegative \(t\)-orders, so they extend to the completion of the direct sum. If \(I_{\rm free}\) indexes the free generators, their coordinates give the same \(S(I_{\rm free})\) on each side of the projection. Let \(I\) index the finite intervals, with lengths \(n_\alpha>0\), births \(\mu_\alpha\), and relation weights \(\delta_\alpha=\mu_\alpha+n_\alpha\). Their term in \(E\) is \(S(I)/D S(I)\), where \((Db)_\alpha=t^{n_\alpha}b_\alpha\). Modulo \(t^r\) this term gives the direct sum of the \(R/(t^{\min(r,n_\alpha)})\). Its inverse limit consists of families of residues in \(R/(t^{n_\alpha})\) with all but finitely many residues divisible by \(t^r\) for each \(r\). The projection reduces each coordinate modulo \(t^{n_\alpha}\).

A weight-\(u\) class in the cokernel has a representative of weight \(u\). To see this, project each cochain onto its weight-\(u\) monomials. Take a positive real torus element acting by \(g^v\) in weight \(v\), where \(g>1\). On the complementary monomials the difference of this action and \(g^u\) is invertible by division by \(g^v-g^u\). Both projection and division preserve the restricted condition, since they act separately on scalar coefficients of each \(t\)-power. They commute with \(D\), whose source and target generators have weights \(\delta_\alpha\) and \(\mu_\alpha\). The difference of the torus action and \(g^u\) applied to a representative of the eigenclass is a boundary. Inverting on the complement shows that its entire complementary part is a boundary.

Each nonzero entry of the homogeneous representative is now \(c_\alpha t^{u-\mu_\alpha}\) with a nonnegative integral exponent. In the kernel of coordinate reduction this exponent is at least \(n_\alpha\), so \(\delta_\alpha\le u\). The geometric bound \(\mu_\alpha+\delta_\alpha\ge-1\) then gives
\[
 0\le u-\mu_\alpha\le 2u+1 .
\]
Choose a positive integer \(r>2u+1\). Only finitely many entries of a restricted family can have order below \(r\), so the representative has finite support. Dividing those entries by \(t^{n_\alpha}\) gives a restricted primitive. This proves injectivity in each weight, including after the nonnegative spectator shifts.

Conversely, a nonzero coordinate of a weight-\(u\) family in the separated target lifts uniquely to a monomial \(c_\alpha t^{u-\mu_\alpha}\) of exponent less than \(n_\alpha\). Lift the zero residues to zero. A nonzero lift has order below \(r\) precisely when its residue is outside \(t^r(R/(t^{n_\alpha}))\). The residue condition thus makes the lifts a single restricted cochain of weight \(u\). Together with the free coordinates this proves surjectivity. The projection commutes with \(t\). Taking finite sums gives the graded isomorphism. The element \(1-t\) is a unit in the formal ring \(R\). Specialization at \(t=1\) takes place on the two graded \(\mathbb C[t]\)-modules, where the isomorphism descends modulo \(t-1\).
:::

Whether the actual interval births are bounded below across all reduced charges, conformal weights and highest weights remains open. If the interval contribution to specialization is nonzero, it can already be read on the separated completion. The free summands contribute separately. A closed formula for the lower-spin multiplicities also remains open. A continuous boundary duality for the full completed complex must retain the nonzero kernel \(\bigcap_{r\ge1}t^rE\) in its cohomology. Comparing the derived endomorphisms of that complex with an independently defined Kodaira–Spencer bulk further requires a defect coupling and a map preserving the specified operations.

## Surface fusion and the Miura product {#ch14-surface-fusion-and-the-miura-product}

For the particle junction the common algebra labels the end over which one tensors. For two parallel M5 surfaces the order of the two insertions can already be tested at rank one on each surface. In an ordered product of two first-order differential operators, the left derivative acts on the coefficient to its right. Reversing the surfaces changes which current is differentiated. A field on the fused surface should act on two independently prepared surface sectors; the algebra map would therefore run from the sum of their ranks to the tensor product of their field algebras. Normalize the independent currents by \(J_i(z)J_j(w)\sim k\,\delta_{ij}/(z-w)^2\); \(k\) is their common level. The parameter \(a\) multiplies the derivative along the surface. In this normalization the Miura operator is
\[
L_N=(a\partial+J_1)\cdots(a\partial+J_N).
\]
Let \(p\) denote the symbol of \(a\partial_z\). Move derivatives to the right in the product of two factors. The derivative in the first factor then acts on \(J_2\), contributing \(a\partial_z J_2\) to the constant coefficient. Passing from this normal symbol to the Weyl symbol applies \(\exp(-a\partial_z\partial_p/2)\). On the linear term \((J_1+J_2)p\) it subtracts half the derivative of each current, multiplied by \(a\). Thus composition becomes the Moyal product with \([p,z]_* =a\), and the two factors give
\[
(p+J_1)*(p+J_2)
=p^2+(J_1+J_2)p+J_1J_2
+\frac a2(\partial J_2-\partial J_1).
\]
The derivative term records the order of composition. Write \(\mathcal W_N^{\mathrm{Miura}}(a,k)\) for the vertex subalgebra generated by the coefficients of \(L_N\). Splitting its ordered factors after the first \(N_1\) specifies the image of every coefficient by the displayed symbol product. The resulting vacuum-preserving map is
\[
\mathcal W_{N_1+N_2}^{\mathrm{Miura}}(a,k)\longrightarrow
\mathcal W_{N_1}^{\mathrm{Miura}}(a,k)\otimes\mathcal W_{N_2}^{\mathrm{Miura}}(a,k).
\]
Associativity of symbol composition identifies its two iterates on three ordered groups. Write \(\widehat U_r\) for the coefficient of \(p^{N-r}\) in the Weyl symbol. In the fixed Poincaré–Birkhoff–Witt basis of normally ordered differential monomials in the \(\widehat U_r\), the scalar structure constants of their operator products are even in \(a\), and after inverting \(k\) the central charge is \(N-N(N^2-1)a^2/k\). [*Miura composition and surface fusion*, §§3,8](#ref-ch14-08).

The five-dimensional fields give a signed test with the line and surface still separated. Orient time by increasing \(t\) and both complex planes by their complex orientations. Take positive Taylor couplings on the line and surface, use \(dz/(2\pi i)\) on the surface, and take the perturbative weight \(e^{+S/\hbar_{\mathrm b}}\), where \(\hbar_{\mathrm b}\) is the bulk loop parameter. Let \(y=w_{\rm line}-w_{\rm surface}\ne0\), let \(x\) denote the tangential position, \(e\) the line charge and \(j=W_0\) the surface current. A line at fixed \((z,w)\) probes a surface jet at transverse separation \(y\). Keep \(y\) fixed as the lower and upper heat times \(0<u<v\) vary. In the flat heat-kernel metric \(u,v\) have the units of \(|y|^2\). Integration along \(t\) and Gaussian averaging of the tangential polynomial give the ordered inverse-Hessian pairing
\[
 B_{u,v}=-\frac{e\,j(x)}{4\pi^2 y}
           \left(e^{-|y|^2/v}-e^{-|y|^2/u}\right).
\]
Completing the square gives the connected contraction \(-\hbar_{\mathrm b} B_{u,v}\). At fixed \(y\ne0\), the lower-cutoff exponential tends to zero as \(u/|y|^2\to0\), and the upper-cutoff exponential tends to one as \(|y|^2/v\to0\). The elementary pole is therefore \(+\hbar_{\mathrm b} e\,j(x)/(4\pi^2y)\). The \(n\)th surface jet applies \((-\partial_y)^n/n!\), producing \(y^{-n-1}\) from \(y^{-1}\). This is a calculation on separated supports.

**Example (the order of two surface collars).** Prepare one level-one current excitation on the second surface and the vacuum on the first. The part of the response odd under exchanging the two collars tests the derivative term of the Miura product. Put \(\tau=\hbar_{\mathrm b}/(4\pi^2)\). With the elementary right action \(Y=a\partial_X\), level-one unit surfaces, and incoming magnetic strength \(q_i=\tau/c_{\mathrm M}\) for Moyal parameter \([z,w]_* =c_{\mathrm M}\ne0\), the order-odd response to the test \(f(z)=z^2/2\) is \(\tau(j_2[f']-j_1[f'])/2\). Here \(j_i[f']=\operatorname{Res}f'(z)j^{(i)}(z)dz\). On \(|0\rangle_1\otimes j^{(2)}_{-1}|0\rangle_2\), the current in the second factor returns the vacuum and the first contributes zero. The reading is \(+\tau/2\) times the vacuum. Write \(S=J_1+J_2\) and \(Q=J_1J_2+\tfrac a2(\partial J_2-\partial J_1)\) for the first two elementary Weyl coefficients. The Miura stress tensor \(T=({:}S^2{:}-2Q)/(2k)\) gives the order-odd reading \(+a/2\) on the same marked vector at \(k=1\), fixing \(a=\tau\) at this order and in these markings. Integration by parts gives \(-a/2\) for the order-odd reading of \(Q\). At \(a=0,\ k=1\), the fourth pole of \(T(z)T(w)\) has vacuum coefficient one. An independently prepared magnetic flux must be compared with the stated incoming strength.

A physical surface-fusion theorem would extend these separated calculations to coincident supports and identify the renormalized line, surface and mixed operations on their full domains. Reflection constrains a first-order deformation only under compatible defect quantization, Ward identities and uniqueness hypotheses. The algebraic Miura coproduct, the single connected tree, and the two-collar response specify coefficients and normalizations that an all-orders comparison must preserve.

## Higher currents and open–closed coupling {#ch14-higher-currents-and-openclosed-coupling}

The separated line and surface above probe Taylor coefficients of regular fields. Removing a point from a complex manifold also admits polar modes. On a Calabi–Yau threefold with holomorphic volume form \(\Omega\), holomorphic Chern–Simons theory has a \(\mathfrak g\)-valued \((0,1)\)-connection \(A\). An invariant nondegenerate pairing gives the classical action
\[
S(A)=\int\Omega\wedge
\left(\frac12\langle A,\bar\partial A\rangle
+\frac16\langle A,[A,A]\rangle\right).
\]
The extended field complex is \(\Omega^{0,*}\otimes\mathfrak g[1]\), with linear differential \(\bar\partial\). Removing a point exposes higher-dimensional current modes, including principal parts that have no counterpart among regular functions. Their algebraic model is derived global sections of punctured affine space, as in [Faonte–Hennion–Kapranov, §§1.2–1.4](https://arxiv.org/abs/1701.01368).

For \(n=2,3\), an explicit commutative differential graded algebra is
\[
\mathscr A_n=
\frac{\mathbb C[z_i,u_i]\otimes\Lambda(du_i)}
{(\sum_i z_i u_i-1,\sum_i z_i du_i)},
\qquad d u_i=du_i.
\]
Give \(z_i\) internal weight one and \(u_i,du_i\) internal weight minus one. The algebra computes \(R\Gamma(\mathbb A^n\setminus\{0\},\mathcal O)\). Its cohomology consists of polynomials in degree zero and
\[
(z_1\cdots z_n)^{-1}\mathbb C[z_1^{-1},\ldots,z_n^{-1}]
\]
in degree \(n-1\). Let \(E_n\subset\mathscr A_n\) be the span of \(u^\alpha\omega_n\), where
\(\omega_n=\sum_i(-1)^{i-1}u_i\,du_1\wedge\cdots\widehat{du_i}\cdots\wedge du_n\).
Then \(E_n\) represents the principal parts. Define
\[
L_n=\mathfrak g\otimes\mathscr A_n,
\quad P_n=\mathfrak g\otimes\mathbb C[z_1,\ldots,z_n],
\quad N_n=\mathfrak g\otimes E_n.
\]
The regular and polar currents each close under their own Lie bracket. Together their representatives give \(P_n\oplus N_n\to L_n\), a quasi-isomorphism of complexes. For example, on the punctured plane the class of \(z_1^{-1}z_2^{-1}\) lives on the overlap \(z_1z_2\ne0\). Multiplication by \(z_1\) gives \(z_2^{-1}\), already a section of the second chart, so the resulting top cohomology class is zero. A regular current multiplied into a principal part may thus cancel one of its poles. Its mixed bracket then need not be the chosen representative of its cohomology class. This is the correction that will enter the endomorphisms of the induced module.

**Definition (co-vacuum for the punctured current algebra).** Give \(\mathbb C\) the trivial action of the polar subalgebra \(N_n\). Inducing to all modes, at zero central extension, gives the left \(U(L_n)\)-module \(W_n=U(L_n)\otimes^{\mathbf L}_{U(N_n)}\mathbb C\). Its generating vector is annihilated by the polar currents.

Which operators on this induced module commute, in the derived sense, with every current? Take the derived endomorphisms in left \(U(L_n)\)-modules, with the direct sum over homogeneous internal weights.

**Theorem (endomorphisms of the co-vacuum).** Assume \(\mathfrak g\) is finite-dimensional and two-step nilpotent,
\([\mathfrak g,[\mathfrak g,\mathfrak g]]=0\).
Then its internally graded derived endomorphism algebra has a strict multiplicative model
\[
\operatorname{REnd}(W_n)\simeq
U(P_n)\ltimes\operatorname{Sym}(N_n^\vee[-1]),
\qquad d=0.
\]
The dual is restricted by internal weight; the symmetric algebra is graded-commutative. Its ghost generators have degree \(2-n\), so they are polynomial for \(n=2\) and exterior for \(n=3\). For \(p\in P_n\) and \(v\in N_n\), define \(\rho(p)v\) by taking the mixed bracket \([p,v]\), passing to its top cohomology class and choosing the unique representative in \(N_n\). Thus \(\rho\) is the projected principal-part action: multiply a Laurent principal part by the regular polynomial, discard terms in which a pole disappears, and include the bracket of the Lie-algebra coefficients. The mixed relation is
\[
[X_p,c_\lambda]=-c_{\lambda\circ\rho(p)}.
\]
The cancelled-pole example above therefore has zero projected coefficient. Starting with \([z_1^{-2}z_2^{-1}]\) instead gives the surviving class \([z_1^{-1}z_2^{-1}]\) with the Lie bracket of the two colours. This is the projection that enters the ghost commutator. All modes are retained, with algebraic sums and products. [*Higher current algebras and their induced modules*, Theorem 13.2](#ref-ch14-09).

The proof constructs polynomial primitives
\(db(p,v)=[p,v]-\rho(p)v\).
Use the Chevalley resolution \(Q_W=U(L_n)\otimes\operatorname{Sym}(N_n[1])\). Let \(R_v\) be signed right multiplication on its first factor, \(S_v\) multiplication by the suspended variable on the second, and \(\partial_i\) contraction against a basis element \(v_i\) of \(N_n\). Define
\[
A_p=R_p-\sum_i R_{b(p,v_i)}\partial_i
-\sum_i S_{\rho(p)v_i}\partial_i.
\]
Every sum acts finitely on each polynomial input. The comparison sends \(X_p\mapsto-A_p\) and \(c_\lambda\mapsto\partial_\lambda\); the minus sign accounts for the order reversal of right multiplication. Two-step nilpotence makes the primitives' Lie-algebra coefficients central, so these operators are closed and satisfy the regular, ghost and mixed relations strictly. A filtration by ghost length proves the map is a quasi-isomorphism; at each internal weight that filtration is finite.

This works for the nonabelian quadratic algebra with basis \(a_i,b^i\), brackets \([a_i,a_j]=\epsilon_{ijk}b^k\), central \(b^k\), and pairing \(\langle a_i,b^j\rangle=\delta_i^j\), zero on the two individual spans; here \(\epsilon_{123}=1\).

For the full algebraic Hom extension, let \(B\) be either \(\mathbb C[z_1,\ldots,z_n]\) or \(\mathbb C[[z_1,\ldots,z_n]]\), replace \(\mathscr A_n\) by the algebraic tensor product \(B\otimes_{\mathbb C[z_1,\ldots,z_n]}\mathscr A_n\), and put \(P_{n,B}=\mathfrak g\otimes B\). Give the ghost dual to \(e_a u^\alpha\omega_n\) weight \(|\alpha|+n\), for a basis \(e_a\) of \(\mathfrak g\). The endomorphism model is completed in this positive ghost weight, separately in each cohomological degree. Equivalently, it contains arbitrary coefficient families
\[
\sum_I a_Ic^I,
\qquad a_I\in U(P_{n,B}),
\]
indexed by the ghost monomials \(c^I\) of that degree. Every coefficient \(a_I\) is an algebraic enveloping-algebra element, a finite sum of finite words in regular currents; their word lengths need not have a uniform bound as \(I\) varies. Formal power series are allowed inside each regular current when \(B\) is formal, but only the ghost series are completed in this endomorphism model. [*Higher current algebras and their induced modules*, Theorem 14.3](#ref-ch14-10). Arbitrary nonabelian \(\mathfrak g\) in dimension three and nonzero central extension require further comparisons.

These associative endomorphism theorems do not yet identify an interacting open–closed field theory. Paired free fields on \(\mathbb C^2\), over \(\mathbb C[\hbar,\kappa]\) with algebraic field-number sums and compact smooth joint kernels, have an [all-arity factorization comparison preserving both field species, translations and vacuum](#ref-ch14-11). Unshifted surface currents instead carry a [ternary central operation with the vacuum-compatible central shift](#ref-ch14-12). A bulk action must reproduce that operation and its level. Quantum anomaly cancellation may require closed fields, as in [Costello–Li's coupled holomorphic Chern–Simons and Kodaira–Spencer theory](https://arxiv.org/abs/1905.09269).

A finite quantum example comes from the anomaly-cancelled self-dual gauge theory. On a twistor line, the two transverse Taylor indices \(t=(t_1,t_2)\) label modes of a field along the line. The two helicities give open currents \(J[t],\widetilde J[t]\) with colours in a finite-dimensional simple complex Lie algebra \(\mathfrak g\). The axion supplies colour-singlet modes \(E[t],F[t]\). The twistor bidegree is \(t\) for \(J[t],E[t]\) and \(t+(1,1)\) for \(\widetilde J[t],F[t]\). Translation has bidegree zero. Thus \(J[1,0]\) and \(\widetilde J[0,0]\) have bidegrees \((1,0)\) and \((1,1)\). Their normally ordered product has bidegree \((2,1)\). Both generators can survive a cutoff that kills this product. In each of the boundary and ghost algebras every state of total bidegree outside \(D=\{0,1\}^2\) vanishes, even when it is a normally ordered product of retained generators. Over \(\mathbb C[s]/(s^3)\), take the quadratic current coefficient \(c_1=s^2a\), the linear coefficients \(c_2=-h^\vee c_1/3\) and \(c_3=2c_2\), and the axion coupling \(\ell=s\ell_0\). Here \(h^\vee\) is the dual Coxeter number and the invariant form \(K\) gives long roots squared length two. The boundary algebra \(A_D\) has its free ordered presentation and the ghost differential \(Q\) squares to zero when
\[
2a\,\operatorname{Tr}_{\mathfrak g}\bigl((\operatorname{ad}X)^4\bigr)=3\ell_0^2K(X,X)^2
\qquad(X\in\mathfrak g).
\]
Let \(I\) pair the ghosts with their corresponding boundary currents, and let \(D_{\rm tot}\) translate both factors along the line. There is a state \(H\) in the tensor product for which \(QI+\tfrac12 I_{(0)}I=D_{\rm tot}H\). At nonzero axion coupling the translated state \(D_{\rm tot}H\) is nonzero. Its zeroth mode vanishes because the residue of a total derivative is zero. On the ghost algebra tensored with any ordinary untwisted \(A_D\)-module, the square of the odd operator \(Q+I_{(0)}\) is precisely this zeroth mode. Thus it gives a differential on each such module. Extending this simultaneous boundary-and-ghost construction to all bidegrees in \(\{0,1,2\}^2\), and then to a smooth quantum module theory, remains an open problem. [*Celestial current algebras*, §§4.6–4.8](#ref-ch14-13).

### The celestial current product {#ch14-celestial-yangian-like}

Take the two transverse first derivatives of an open field along a twistor line, one in direction \(w_1\) and one in direction \(w_2\). Give them commuting gauge generators. At tree level a contour around the collision reads their Lie bracket and gives zero. A quantum contraction can still leave *two* colour currents at the surviving point. Which two currents does it produce?

Here the theory is the flat four-dimensional Wess–Zumino–Witten model. Its open field has one tower of scalar currents. The twistor description couples \(\mathrm{SO}(8)\) holomorphic Chern–Simons theory to the type I Kodaira–Spencer sector, which gives Mabuchi gravity in four dimensions. Put the line at \(w_1=w_2=0\) and use \(z\) as its longitudinal coordinate.

**Definition (scalar jet current).** The field \(J_a[r,s](z)\) couples on this line to the \(T_a\) component of the transverse Taylor coefficient \(\partial_{w_1}^{\,r}\partial_{w_2}^{\,s}A/(r!s!)\), for \(r,s\ge0\) and a basis \(T_a\) of \(\mathfrak{so}_8\). Equivalently its source monomial is \(w_1^rw_2^sT_a\). A current of degree \((1,0)\) tests the first transverse derivative of a field at the line. In a celestial amplitude these currents insert the corresponding conformally soft scalar states.

At tree level the transverse monomials multiply and the colour generators take their Lie bracket. With \([T_a,T_b]=f_{ab}{}^{c}T_c\), the pole in the convention in which the first insertion is at \(0\) is
\[
\begin{gathered}
 J_a[r,s](0)J_b[t,u](z)\\
 \sim\frac{f_{ab}{}^{c}}{z}J_c[r+t,s+u](0).
\end{gathered}
\]
Here \(\sim\) records the singular part at the collision. Taking its \(z^{-1}\) coefficient with the residue normalized by \(\operatorname{Res}_0 dz/z=1\) returns a field at the surviving insertion. If \([T_a,T_b]=0\), this tree residue vanishes for all transverse degrees. The regular coefficients also belong to the field product.

At the first quantum order in the gauge sector there is another way to join the two insertions. Contract one colour from each cubic vertex across the twistor propagator. The inverse invariant form \(K^{ef}\) performs that contraction. The remaining two lines at the defect carry zero transverse degree. Put
\[
 C_{ab}{}^{cd}=K^{ef}f_{ae}{}^{c}f_{bf}{}^{d}.
\]
For \(J_a[1,0](0)J_b[0,1](z)\), the tree term is \(f_{ab}{}^cJ_c[1,1]/z\). In the ordered convention of Costello and Paquette, the gauge correction to the simple pole is
\[
 \frac{\hbar}{z}\,C_{ab}{}^{cd}:J_c[0,0]J_d[0,0]: .
\]
The colons prescribe the regular product at the remaining point, obtained after subtracting the singular contraction of the two output currents. This term cancels the gauge variation of the diagram coupling the defect to the two transverse derivatives. Its colour tensor can survive even when the tree bracket vanishes. Costello credited this subleading calculation to Raeez Lorgat, Faroogh Moosavian and Yehao Zhou. [Costello, Strings 2021, slide 18](https://www.ictp-saifr.org/wp-content/uploads/2021/06/Kevin-Costello.pdf#page=18) · [Costello and Paquette, JHEP (7.23)](https://inspirehep.net/files/65769bae9f165431f3ebb5863f596224#page=45) · [Preprint, gauge correction (7.3.2) and its variation (7.3.4)](https://arxiv.org/pdf/2201.02595v3#page=53)

**Example (four distinct colours).** Let \(E_{ij}\) be the matrix taking the \(j\)-th coordinate vector to the \(i\)-th and killing the others. Use the basis \(T_{ij}=E_{ij}-E_{ji}\), \(i<j\), orthonormal for \(K(X,Y)=-\tfrac12\operatorname{tr}_{8}(XY)\). The matrices \(T_{12},T_{34}\) commute. Only a generator sharing an index with each of them can contribute to the contracted tensor. Summing over \(T_{13},T_{14},T_{23},T_{24}\) gives, with \(J_{ij}=J_{T_{ij}}[0,0]\),
\[
\begin{gathered}
 C_{12,34}{}^{cd}:J_cJ_d:\\
 =-2\bigl(:J_{13}J_{24}:-:J_{14}J_{23}:\bigr).
\end{gathered}
\]
Denote the two products on the right by \(B,C\) in the order shown, and the direct product \(:J_{12}J_{34}:\) by \(A\). The Killing form used in the published formula is \(6\operatorname{tr}_8=-12K\). If all other propagator conventions are fixed, the parameter multiplying the inverse of our form is consequently \(\hbar_K=-\hbar_{\mathrm{CP}}/12\). Each pair on the right has disjoint indices. Its two currents have zero bracket, so exchanging their order introduces no derivative commutator. Thus the simple pole of the two commuting first jets has a component along \(B-C\). It takes values in the weight-two fields. A scalar vacuum expectation by itself would discard those output colours.

For these two output monomials there is an all-orders statement. Work in a flat volume coordinate patch away from the poles of the meromorphic twistor volume form \(\Omega\). Write the open action as \(\lambda^{-1}\int\Omega\,\mathrm{CS}(A)\), and calibrate \(\lambda=\hbar_K\) by the gauge correction just computed. The type-I open–closed bulk theory admits an equivariant perturbative quantization in this chart. Under the transverse change \((w_1,w_2)\mapsto(aw_1,bw_2)\) the volume form acquires the determinant \(ab\). The string parameter has this same character. Choose an equivariant restriction and augmentation on the line and homogeneous current symbols in its completed bar construction. The two transverse characters then survive passage to those symbols. Consequently a contribution of order \(\lambda^L\) to a homogeneous symbol with only open output currents of transverse degrees \((m_i,n_i)\) obeys
\[
 (r+t,s+u)=\sum_i(m_i,n_i)+(L,L).
\]
Longitudinal derivatives preserve this bidegree. For the incident jets \((1,0),(0,1)\) and outgoing zero jets the equation forces \(L=1\). Thus the open gauge diagram contributes exactly \(-2\lambda\) and \(+2\lambda\) to the two crossed symbols to all orders. The complete projected coefficients are \(\lambda\) times their complete first-order constants. A single closed exchange has one of the colour tensors \(K_{ab}K_{cd}\), \(K_{ac}K_{bd}\), \(K_{ad}K_{bc}\). Each vanishes on both crossed assignments. A direct output \(:J_{12}J_{34}:\) has a nonzero pairing. A first-order contact term intrinsic to the defect would obey the same bidegree rule. Its coefficient is constrained by current Ward identities, which test the candidate field with a third insertion. [Costello, quantum scaling and twistor quantization](https://arxiv.org/abs/2111.08879) · [Costello, Paquette and Sharma, §4.2](https://arxiv.org/pdf/2306.00940v2)

Colour contraction gives the two crossed terms on the preceding pair. To test whether an additional defect contact can change either coefficient, bring a third zero-jet current to their output. Work with the marked universal gauge currents at level zero. Compare two defect products with the same source marking and the same lower and mixed Ward operations after composition and projection to one zero-jet current. A third contour measures the first positive mode of \(j_v=J_v[0,0]\): integrating \(u\,j_v(u)\,du/(2\pi i)\) about the output at \(0\) selects its double-pole coefficient. This mode sends the symmetric quadratic symbol \(a\odot b\) to the current of colour \(([[v,a],b]+[[v,b],a])/2\). As \(v\) varies, this defines an operator \(M\) on symmetric two-tensors, using \(K\) to identify them with self-adjoint maps. Its eigenvalues on \(\operatorname{Sym}^2\mathfrak{so}_8\) are \(-12,-4,2\). Subtract the two Ward identities. A possible difference \(F(a,b)\) in the quadratic term then satisfies \(M(F(a,b))=\sigma M(a\odot b)\), where \(\sigma\) is the change in the companion double-pole coefficient. Injectivity leaves only \(\sigma a\odot b\). On \(12,34\) this is the direct product \(A\). The full crossed coefficients are therefore \((-2,+2)\lambda\) to all orders for this fixed gauging, whenever the two crossed symbols survive independently. Changing the affine level or the mixed translation action changes the Ward equation.

One can fix the coupling by a pair of open–closed operations instead. Take the oriented separation \(t=z_1-z_2\), a bulk loop parameter \(\ell\), and the volume form \(dz\,dw_1\,dw_2\). Normalize the closed two-form made by open gauge parameters \(af,bg\) as \(uK(a,b)\,df\wedge dg\), and the reciprocal action of a closed two-form as \(v\ell\) times its corresponding volume-preserving vector field on an open parameter. With both actions and the unmixed linear closed representative fixed, the all-colour Ward identity gives \(uv\ell(B-C)/(2t)\) in the crossed projection. Since \(t=-z\) in the \(0,z\) formula, these two calibrations agree for \(uv\ell=4\lambda\). Shifting the closed representative by a quadratic current would change the comparison on other colours.

One can locate the entire pole for these colours under an additional assumption on the vacuum states. Suppose they are spanned by products and longitudinal derivatives of open currents of spin \(1+(r+s)/2\) and colour-singlet closed fields of strictly positive spin, with the scalar zero mode fixed and no background parameter carrying transverse weight. Each incoming field has spin \(3/2\). A singlet output would pair the two colours by \(K\), and a single adjoint output would take their bracket. Both vanish. Indeed the invariant trilinear form on three skew matrices in dimension eight is proportional to the alternating trace. A pole of order \(p\) has an output of spin \(3-p\). Two open currents already have spin at least two. It follows that the only possible pole is simple, with precisely two zero-jet open currents and with no derivative. This proves the first-order support of the entire singular part in that polynomial sector. The numerical coefficient of each allowed contact is a separate question.

There is also an explicit family of higher coefficients in the flat open theory. Surround the line by a transverse unit three-sphere. Decomposing the bulk fields into angular harmonics and eliminating the exact harmonics gives higher interaction vertices. Choose the sphere trace of total mass one and the invariant tangential \((0,1)\) form \(\epsilon\) with \(\bar\partial_b\bar w_2=w_1\epsilon\), \(\bar\partial_b\bar w_1=-w_2\epsilon\). For \(k=(i,j)\) the form dual to \(w_1^iw_2^j\) is
\[
 U_k=\frac{(i+j+1)!}{i!j!}\bar w_1^i\bar w_2^j\epsilon .
\]
Let \(h\) invert \(\bar\partial_b\) on its noncohomological harmonics and vanish on cohomology. For incident monomials \(w^t,w^r\) and an ordered list of \(m+1\) open outputs, start with \(P_0=w^r\). For \(1\le j\le m\), put \(P_j=h(P_{j-1}U_{k_j})\). The trace after these successive contractions gives
\[
\begin{gathered}
 T_m(t,r;k_1,\ldots,k_{m+1})\\
 =\operatorname{Tr}(w^tP_mU_{k_{m+1}}).
\end{gathered}
\]
This computes the angular coefficient in the transferred open vertex with two incoming gauge fields and the maximal number of open output fields. In the action it multiplies the ordered nested colour brackets, summed over the orderings with the cyclic action's symmetry factor. For \(t=(m,0)\), \(r=(0,m)\) and every \(k_j=0\), each contraction replaces one \(w_2\) by \(-\bar w_1\) and divides by the number of \(\bar w_1\)'s after the replacement. Hence \(P_m=(-1)^m\bar w_1^m/m!\). Since the spherical mean of \(|w_1|^{2m}\) is \(1/(m+1)\), the coefficient in this order is
\[
 T_m\bigl((m,0),(0,m);0,\ldots,0\bigr)
     =\frac{(-1)^m}{(m+1)!}.
\]
It is \(-1/2,1/6,-1/24\) in the first three lengths. A count of bulk graphs explains why classical transfer gives the term with the largest possible number of open fields. For a connected graph, let \(k\) be the number of open ends attached to linear defect sources, \(b_1\) its number of independent cycles, and \(v_m,v_c\) its numbers of mixed and closed cubic vertices. There are no external closed ends. With any number of amputated open test fields, counting half-edges with the propagator weights gives
\[
 L=k-1+b_1+\tfrac12(v_m+v_c).
\]
Thus \(k=L+1\) forces a pure open tree. Lower numbers of open fields allow loops or closed vertices. A primitive contact intrinsic to a differently specified defect would require its own calculation. [Zeng, (4.49), (4.63), (9.47) and (9.54)](https://arxiv.org/abs/2302.06693) · [Costello, twistor-space quantization, Appendix C](https://arxiv.org/abs/2111.08879)

There is a direct way to see these coefficients as gauge transport. Cover the punctured transverse plane by \(x\ne0\) and \(y\ne0\). Use the residue with \(\operatorname{Res}((xy)^{-1})=1\). A constant polar colour \(b/(xy)\) glues the two charts by \(\exp(-\operatorname{ad}_b/(xy))\). Apply it to \(x^mX\), subtract the transported section from the untransported one, and pair the jump against \(y^mY\) using \(K\). The terms before the \((m+1)\)-st power extend across one of the two charts. The first term with both powers negative gives the residue. In this orientation its coefficient is \((-1)^m K(Y,\operatorname{ad}_b^{m+1}X)/(m+1)!\). Rescale the polar field by a parameter \(\tau\) and the bracket by \(\tau^{-1}\). If \(u,v\) mark the two external jet orders, \(q=\tau uv\) records the order along this family. Summation gives the single function
\[
 \frac{1}{q}K\bigl(Y,(1-e^{-q\operatorname{ad}_b})X\bigr).
\]
For \(b=T_{12},X=T_{13},Y=T_{23}\) the answer is \(-\sin(q)/q\). In particular the cubic open term in the second-jet product is \(+1/6\) in these residue units. The quadratic term on a general polar field is \(\tau K([b,X],[b,Y])/2\). Matching it to the first gauge pole with the same trace form, labelled currents and pole orientation sets \(\tau=2\lambda\). This comparison fixes the first symbol. The formula sums different pairs of input jets on the marked polar field, and uses precisely the fields defined by this gluing.

To see what these residues mean for the charges, expand a field in modes, \(Y(A,t)=\sum_n A_nt^{-n-1}\), now taking \(t\) to be the position of the first field minus that of the second. A simple pole contributes \([A_0,B_n]=(A_{(0)}B)_n\). Here \(t=-z\) for the order used in the first formula. The commutator of the first transverse modes therefore contains modes of a normal product of zero-jet currents. This is one sense in which the charges are *Yangian-like*. The two polynomial variables of the classical current algebra survive, while the deformed bracket of their first powers contains a quadratic Casimir contraction. A related contraction occurs in the deformed double current algebra. The celestial mode algebra has in addition the Laurent modes along the line. [Guay and Yang, Definition 2.2 and Proposition 4.1](https://arxiv.org/abs/1608.02900)

Can the charges act on a tensor product at the same point? Try \(D J=J\otimes1+1\otimes J\) on all the currents, with independent commuting factors. The singular product of two such sums places its quadratic term wholly in one factor. Applying \(D\) to the quadratic output also produces the mixed tensor \(J_{13}\otimes J_{24}\), with coefficient \(-2\lambda\) in the original \(0,z\) gauge convention. Testing this coefficient where the classical currents are independent disproves this primitive rule. In the polynomial gauge mode algebra there is a stronger first-order test. Write \(x^\square=x\otimes1+1\otimes x\). If \([x,y]=\lambda C\bmod\lambda^2\) for the two commuting classical first jets, first-order corrections \(D_x,D_y\) to their primitive images must satisfy
\[
\begin{aligned}
 D_0 C-C^\square
   &=[x^\square,D_y]+[D_x,y^\square].
\end{aligned}
\]
Here \(D_0\) is the classical primitive coproduct. Evaluate the transverse variables at zero in both classical factors. Each of \(x,y\) carries a positive transverse degree, so \(x^\square\) and \(y^\square\) evaluate to zero. Both commutators on the right therefore vanish. On the left, \(C^\square\) puts both output currents in a single factor. Applying \(D_0\) to their product also puts one current in each factor. The coefficient of \(J_{13}\otimes J_{24}\) survives this evaluation because both of those currents have jet zero. For Laurent modes one may take mode \(0\) of the first field and mode \(1\) of the second, so that the two surviving currents can both have mode \(0\). This obstruction uses an ordinary tensor square with a defined coefficient on the two classical currents and the indicated nonzero first-order symbol. Evaluating the two factors at different transverse parameters changes the equation. A quantum group action would require a coproduct preserving the field products, a counit and coherent coassociativity. A braided field action would also require an exchange satisfying the field hexagon. The nonlinear current product supplies the relation any such action has to respect. [The spectral coproduct and field hexagon](#ch12-a-spectral-construction-of-products-and-coproducts)

One can test the same colour calculation in another realization. A stack of \(N\) D1 branes changes the four-dimensional geometry to the Burns background. Here the finite-rank free-field representatives allow the residue itself to be paired with a chosen output current product. In the corresponding chiral algebra, obtained by symplectic BRST reduction, there are flavour fields \(I_i\) and two matrix-valued fields \(X^{\dot1},X^{\dot2}\). The current \(J_{ij}[0,0]\) is an \(I_iI_j\) bilinear. The first jets put a single \(X^{\dot1}\) or \(X^{\dot2}\) between these two fields. Take four distinct flavours, so there can be no \(I\)-\(I\) contraction across the insertions. Only the pair of \(X\)'s can contract. Write \(d=2N\) for the dimension of the symplectic vector space. Let \(h_0=1\) for the traceless antisymmetric matrix representation and \(h_0=0\) when the free centre-of-mass field is restored. Choose \(\epsilon^{\dot1\dot2}=1\) and take \(A,B,C\) to be the same three normal products, now in the brane algebra. In the brane convention the *entire singular product* is
\[
\begin{gathered}
 J_{12}[1,0](z)J_{34}[0,1](w)\\
 \sim\frac{(B-C)/2-h_0A/d}{z-w}.
\end{gathered}
\]
Antisymmetrizing the two possible symplectic contractions gives \((B-C)/2\). Removing the symplectic trace gives the direct-colour term \(-h_0 A/d\). There is no second cross-contraction, so there is no higher pole. Contract the numerator once more, now against \(B\). The coefficient of the fourth-order pole is \(d(d-1)/2-h_0\), nonzero for \(d\ge4\). Thus the residue survives as a measurable field in this realization. The rank and the centre-of-mass convention are part of the answer. Identifying this Burns-brane current with a chosen flat bulk current requires a comparison of backgrounds and marked fields. [Costello, Paquette and Sharma, the symplectic trace and its subtraction, (4.2)–(4.6)](https://arxiv.org/pdf/2306.00940v2#page=38)

With the same colour at the two insertions all three elementary fields can contract. The coefficient of the third-order pole for colours \(a,b\) is \((d(d-1)/2-h_0)K(a,b)\). The factor is the dimension of the chosen antisymmetric representation. More generally the currents are symmetrized words in the two \(X\)'s between two \(I\) endpoints. To compute their product, pair elementary letters across the two words, multiplying the numerators of their propagators. An \(\ell\)-fold pairing contributes \((z-w)^{-\ell}\). Taylor-expanding the surviving left letters through degree \(\ell-1\) gives every singular coefficient. Two endpoints and only oppositely polarized \(X\)'s can pair. Thus for jet indices \((r,s),(t,u)\) the pole order is at most \(2+\min(r,u)+\min(s,t)\). This finite prescription computes the product of the marked polynomial representatives at every jet order and rank. Expressing its coefficients in a chosen set of reduced cohomology generators can require further relations. [Costello, Paquette and Sharma, elementary contractions (4.4)–(4.6)](https://arxiv.org/pdf/2306.00940v2#page=38) · [Symmetrized current words (4.17)](https://arxiv.org/pdf/2306.00940v2#page=40)

There is a genuine tensor action on one transverse axis. Complexify the flavour space and choose isotropic vectors \(e_i,f_i\), \(1\le i\le4\), with \((e_i,f_j)=\delta_{ij}\). In the symplectic space of the branes let \(M\) be \(X^{\dot1}\) with one index raised. For \(i<j\) form the currents
\[
 A_i{}^j[r]=:\!\omega(I_{e_i},M^r I_{f_j})\!: .
\]
Two copies of \(X^{\dot1}\) have zero contraction. Only an \(e\) endpoint can contract with an \(f\) endpoint. For \(i<j,\ k<l\), the two equalities \(j=k,\ l=i\) cannot both hold. A single contraction joins the two powers of \(M\). In the matrix-unit convention the entire singular residue is
\[
 \delta_{jk}A_i{}^l[r+s]-\delta_{li}A_k{}^j[r+s].
\]
These residues identify the source Lie algebra. The elementary matrix \(E_{ij}u^r\) acts by the field \(A_i{}^j[r]\), with \(u\) recording the power of the single transverse matrix. A mode \(E_{ij}u^rz^n\) acts on a brane module by the contour \(\operatorname{Res}_{z=0}z^n A_i{}^j[r](z)\,dz\). The absence of a double pole is what permits all Laurent modes to act without a central term. They give an action of \(U(\mathfrak n_+(\mathfrak{sl}_4)[u,z,z^{-1}])\). Its primitive coproduct acts on the tensor product of two such modules. Finite-rank relations may give a kernel. Both the upper triangular restriction and the common transverse polarization enter the calculation. With the two different transverse directions, the \(X\)-\(X\) contraction that produced the four-colour quadratic residue returns.

A second all-orders calculation concerns self-dual Yang–Mills theory. Here the twistor theory is holomorphic BF theory. Its propagator pairs an \(A\) leg with a \(B\) leg, and the opposite helicity supplies a second tower \(\widetilde J\). Even for the same commuting colours the gauge correction to \(JJ\) now contains \(:J\widetilde J:\) and \(:\widetilde JJ:\). Declaring the two towers identical would change the propagator and its contractions. A bare one-loop deformation can fail associativity. For the extended theory with a real matter representation \(R\), the quartic anomaly must factor as
\[
 \operatorname{Tr}_{\mathrm{ad}}(X^4)-\operatorname{Tr}_{R}(X^4)
   =\lambda_{\mathfrak g,R}^2\bigl(\operatorname{Tr}_{\mathrm{fun}}X^2\bigr)^2
\]
with the indicated axion coupling when its coefficient is nonzero. In that theory the associativity equations determine, in particular, the entire ordered mixed-helicity family below from its one-loop seed. Other coefficients in the full OPE have their own equations. The coefficient denoted by \(c\) is given explicitly at the first two loop orders. The longitudinal position, the helicity, and the order of the output factors are all retained. [Costello and Paquette, §7.3, equation (7.3.5)](https://arxiv.org/pdf/2201.02595v3#page=53) · [Costello and Paquette, *Associativity of One-Loop Corrections to the Celestial Operator Product Expansion*](https://arxiv.org/abs/2204.05301) · [Fernández and Paquette, §§1–3](https://arxiv.org/abs/2412.17168)

For example consider a negative-helicity current at \(z\) and a positive-helicity current at \(0\), in the order \(\widetilde J_a[r](z)J_b[t](0)\). At tree level their residue is \(f_{ab}{}^c\widetilde J_c[r+t]\). At loop order \(m\ge1\) it contains ordered products of \(m+1\) negative-helicity currents. The tensor in their colour indices is the chain of \(m+1\) structure constants contracted by \(m\) inverse invariant forms in [equation (3.14) of Fernández and Paquette](https://arxiv.org/pdf/2412.17168v2#page=31). The scalar coefficient multiplying that chain is \((\hbar/(16\pi^2))^m F_m(r,t;k_1,\ldots,k_{m+1})\). All \(k_i\) are nonnegative pairs satisfying \(\sum_i k_i=r+t-m(1,1)\). This is a finite sum at every input.

Here is a polynomial form of their recurrence. Write \(A_0=\mathbb Q[x,y]\), \(X^r=x^{r_1}y^{r_2}\). Define \(B_m(X^r,X^t)\) as the polynomial in \(m+1\) separate pairs of variables \(X_i\) whose coefficient of \(\prod_iX_i^{k_i}\) is \(F_m(r,t;k_1,\ldots,k_{m+1})\). For a linear polynomial \(s=cx+dy\) put \(D_s=c\partial_y-d\partial_x\). The one-loop operation on a linear second input is
\[
\begin{gathered}
 U_s(p)(Z,W)\\
 =\int_0^1 v\,(D_s p)\bigl(vZ+(1-v)W\bigr)\,dv .
\end{gathered}
\]
Introduce \(B_0(p,q)=-pq\) as an auxiliary initial value, and put \(B_m(p,1)=0\) for \(m>0\). Stripping the last linear factor \(s\) from the second input gives
\[
\begin{aligned}
 B_m(p,qs)={}&s(X_{m+1})B_m(p,q)\\
 &-(1^{\otimes(m-1)}\otimes U_s)B_{m-1}(p,q)\\
 &+(B_{m-1}(p,-)\otimes1)U_s(q).
\end{aligned}
\]
The middle term splits the last output into two. The last term instead feeds the first output of \(U_s(q)\) into \(B_{m-1}\). Induction on \(m\) and on the degree of the second input terminates. Expanding the integral on monomials gives the factorial seed. This recovers the ordered coefficients of equations (3.42) and (3.44). Equations (3.46)–(3.47) give their closed expression. [Fernández and Paquette, §§3.4–3.5](https://arxiv.org/pdf/2412.17168v2)

Take \(r=(m,0)\), \(t=(0,m)\) and retain the output with all zero jets. Its ordered coefficient is
\[
 F_m((m,0),(0,m);0,\ldots,0)=-\frac1{(m+1)!}.
\]
One way to evaluate it is to strip one \(y\) at a time. At the first step \(U_y(x^m)=-m\int_0^1 v(vZ_x+(1-v)W_x)^{m-1}dv\) has coefficient \(-1/(m+1)\) on \(W_x^{m-1}\). The successive last-output splittings give the remaining factorial. At two loops this ordered residue has scalar coefficient \(-\hbar^2/[6(16\pi^2)^2]\) in front of the three-current colour chain. Exchanging the two incident monomials multiplies the extremal scalar by \((-1)^m\). The signs differ from the flat angular coefficient because the field order and colour-chain convention differ. The recurrence fixes individual ordered output coefficients before the variables \(X_i\) are set equal.

The divided Taylor convention can matter even at one loop. For \(r=(0,3)\), \(t=(1,0)\), \(k=(0,0)\), \(l=(0,2)\), the coefficient of \(W_y^2\) in \(U_x(y^3)\) is \(3\int_0^1v(1-v)^2\,dv=1/4\). [Fernández and Paquette, Appendix C, (C.6)–(C.12)](https://arxiv.org/pdf/2412.17168v2) give \(1/2\) on these labels. The ratio is the outgoing \(2!\), which unit labels cannot detect. The values above use the main-text normalization. This finite check concerns the ordered mixed-helicity coefficient and does not import it into the single scalar tower.

[Download *The celestial current product* (PDF)](celestial-current-product.pdf)

There are two ways to ask for more information from a celestial residue. Raise the orders of the two incident jets and its output can contain three currents. Keep the incident jets fixed and apply a third current to the quadratic output, and its first positive mode tests which part of that field survives. These operations have different targets, even when they use the same colours. [What the celestial residue determines](#ch14-celestial-reconstruction)

### What the celestial residue determines {#ch14-celestial-reconstruction}

In the flat four-dimensional Wess–Zumino–Witten model, a current on the line \(w_1=w_2=0\) can distinguish different Taylor coefficients of the open field. Write \(J_c[r,s](z)\) for the current coupled to its coefficient of \(w_1^r w_2^s\) in colour \(c\), at position \(z\) along the line. What can a contour around two such currents tell us when one tests \(w_1^2\) and the other \(w_2^2\)?

Fix \(T_{ij}=E_{ij}-E_{ji}\) in \(\mathfrak{so}_8\), with \(E_{ij}\) the matrix units. Set \(H=T_{12}\), \(b=T_{13}\), \(R_Hc=[c,H]\) and \(a=R_H^3 b\). Take the coefficient of \(1/(z-w)\) in the product of \(J_a[2,0](z)\) and \(J_b[0,2](w)\). At second order retain its part with three open currents, modulo terms with fewer currents. The three factors are then symmetric. In the chosen basis one can read off the coefficient of \(:J_H[0]^3:\), where \([0]\) means \([0,0]\). Write \(\ell_{\rm bulk}\) for the loop parameter, \(u\) for the open-to-closed coupling and \(v\ell_{\rm bulk}\) for the reciprocal action. In the units \(\hbar_{\rm sc}=uv\ell_{\rm bulk}\), this coefficient is \(\hbar_{\rm sc}^2/24\). Which part of the same contour reading survives when both transverse orders increase together?

At order \(m\) a connected graph joining \(m+1\) linear open sources has to be a tree of open vertices. Retain the part of its output with \(m+1\) currents in the associated graded for the number of open fields. Normal products there are symmetric. Each ordered angular coefficient is accompanied by an ordered sequence of colour operations. For outgoing colours \(c_1,\ldots,c_{m+1}\) this gives
\[
 K\bigl(a,R_{T^{c_{m+1}}}\cdots R_{T^{c_1}}b\bigr),
\]
where \(T^c\) is the dual basis for \(K=-\operatorname{tr}_8/2\). Choosing every outgoing colour to be \(H\) and setting \(a=R_H^{m+1}b\) makes the displayed pairing one. Indeed \(R_H\) interchanges \(T_{13}\) and \(T_{23}\) with opposite signs and preserves their norm. For the transverse monomials \(w_1^m,w_2^m\), the only outgoing degrees at this order are zero. The normalized angular coefficient is \((-1)^m/(m+1)!\). Matching the first quadratic pole fixes the angular propagator parameter to \(-\hbar_{\rm sc}/2\). The resulting term is
\[
 \frac{\hbar_{\rm sc}^{\,m}}{2^m(m+1)!}\,
 \frac{\operatorname{symb}:J_H[0]^{m+1}:}{z-w}.
\]
The first three numerical coefficients in these reciprocal units are \(1/4,1/24,1/192\). Both incident jet orders change with \(m\). For the [four distinct colours and two fixed first jets](#ch14-example-four-distinct-colours), the product still terminates at first order. Here the flat chart, linear Taylor sources and cyclic open tree give the marked symbol. Products with fewer outgoing fields also receive contributions from other graphs. [The angular transfer and first open product](https://arxiv.org/abs/2302.06693)

The angular calculation has an unexpected second use. The twisted self-dual Yang–Mills product of a negative-helicity current at \(z\) and a positive-helicity current at \(0\) has its own ordered output modes. Why does its coefficient satisfy the same recursion? Write \(b_i=\bar w_i\) on the transverse sphere, with \(w\cdot b=1\), and let \(\epsilon\) be the one-form used for angular integration. The generating kernel \(U_Y=\epsilon/(1-b\cdot Y)^2\) reproduces holomorphic polynomials under the normalized trace. For the linear polynomial \(s=s_1w_1+s_2w_2\) form
\[
 V_s(Y)=\frac{b_2s_1-b_1s_2}{1-b\cdot Y}.
\]
The tangential Dolbeault operator sends \(b_2\) to \(w_1\epsilon\) and \(b_1\) to \(-w_2\epsilon\). Differentiating the fraction gives \(\bar\partial_b V_s(Y)=(s(w)-s(Y))U_Y\). Thus multiplying the last incident polynomial by \(s\), and subtracting multiplication by its value at the last output, inserts an exact form. Integration by parts moves the derivative onto the last angular propagator \(h\). On one-forms \(\bar\partial_b h=1-\pi_1\), where \(\pi_1\) projects onto harmonic forms. The identity term splits the last outgoing factor. The harmonic projection, transposed across the trace, feeds one of the two new outputs back into the preceding operation. These are the two terms of the mixed-helicity recurrence besides multiplication by \(s(Y)\). The initial one-propagator integral is the same beta integral as in the gauge theory. Decreasing the order or the degree of the last incident polynomial determines every coefficient from this seed. Write \(f_m=(16\pi^2)^{-m}F_m\), so that the physical ordered coefficient has the remaining loop factor \(\hbar^m\). In the stated pole orientation one obtains, for every \(m\ge1\) and every ordered list \(K\) of outgoing jet degrees,
\[
\begin{gathered}
 f_m(r,t;K)\\
 =-(16\pi^2)^{-m}T_m(t,r;K).
\end{gathered}
\]
The inputs are transposed, and the outgoing list stays in its original order. On the gauge theory side the output fields have negative helicity. On the scalar side the formula computes the angular part of the maximally open tree. The equality gives a calculation of the ordered scalar before any specialization of the outgoing variables. [Fernández and Paquette, the ordered mixed-helicity recurrence](https://arxiv.org/pdf/2412.17168v2)

The angular tensor keeps a symbol before finite-rank relations are imposed. In the Burns-brane algebra the coefficient of the fourth pole against a specified field gives a scalar test on BRST cohomology. For four different flavours write \(A=:J_{12}J_{34}:\), \(B=:J_{13}J_{24}:\), \(C=:J_{14}J_{23}:\). The first transverse jets on the Burns branes have residue \((B-C)/2-\eta A/d\), where \(d=2N\) and \(\eta=1\) removes the symplectic trace. Set \(\eta=0\) to restore the centre-of-mass field. Pair the residue with \(B\) in the vacuum. The three fourth-pole coefficients of \(A,B,C\) against \(B\) are \(d,d^2,d\): a closed symplectic index loop contributes \(d\). The normalized vacuum coefficient of the fourth pole is therefore \((d^2-d)/2-\eta\). For \(d=4\) it is \(5\) after removing the trace and \(6\) when the trace is retained. For every \(d\ge4\) it detects a nonzero class. At \(d=2\), the two-dimensional Pfaffian relation reads \(A-B+C=0\). Removing the symplectic trace then kills the residue, in agreement with the fact that a two-dimensional symplectic space has no traceless antisymmetric tensors. Here the calculation takes place in the BRST reduction, and the vacuum pairing annihilates exact states. Continuing the coefficients in \(d\) would not produce a nonzero current on a zero-dimensional stack. To compare with the flat physical theory one needs a map on the two defect complexes that carries the marked jets, their Ward operations and the closed fields through the collision. [Costello, Paquette and Sharma, the brane currents and symplectic reduction](https://arxiv.org/pdf/2306.00940v2#page=37)

### Quadratic currents and their Ward identity {#ch14-celestial-colour-reconstruction}

At \(d=2\), removing the symplectic trace sets \(\eta=1\). The Pfaffian relation then makes the measured residue zero. Keeping the trace instead sets \(\eta=0\), and the same fourth-pole pairing is \(1\). We can ask which quadratic states are already distinguished *before* taking any finite-rank quotient. Suppose the elementary currents of a simple Lie algebra \(\mathfrak g\) are independent in their universal affine vacuum. If one knows the quadratic residue for *every* pair of colours, which states of conformal weight two can one recover? This question concerns the coefficient itself. If the only available operation is multiplication by \(\hbar\) times that coefficient, extracting its value over a ring of power series is an additional operation.

In the universal affine vacuum, a weight-two state is a sum of a symmetrized product of two currents and a derivative \(TJ_a\) of a single current. These two subspaces are independent by the Poincaré–Birkhoff–Witt basis. The order of the currents matters before symmetrization.

**Definition (ordered quadratic residue).** Write \(h=h^\vee\), put \(\kappa=-B_{\rm Kill}/(2h)\), and choose \(\kappa\)-dual bases \(e_i,e^i\). Let \(V^k(\mathfrak g)_2\) be the weight-two space of the universal vacuum at affine level \(k\). With the loop coefficient removed, the ordered residue \(q:\mathfrak g\otimes\mathfrak g\to V^k(\mathfrak g)_2\) is given by
\[
 q(a,b)=\sum_i :J_{[a,e_i]}J_{[b,e^i]}: .
\]
Use \(a\odot b=(a\otimes b+b\otimes a)/2\), and let \(Q(a\otimes b)=\sum_i[a,e_i]\otimes[b,e^i]\). The two outgoing currents need not commute at the same point. Quasi-commutativity gives \(:J_uJ_v:-:J_vJ_u:=TJ_{[u,v]}\), with \(T\) the longitudinal derivative. The adjoint Casimir in this sign convention is \(-2h\). Applying it to the bracket \([a,b]\) and expanding its two derivations gives \(\sum_i [[a,e_i],[b,e^i]]=h[a,b]\). Consequently the skew part of \(q(a,b)\) is \((h/2)TJ_{[a,b]}\). Reversing the metric reverses this coefficient.

The symmetric part of \(q\) is just \(Q\) followed by the symmetrized normal product. In \(\mathfrak{so}_8\) the symmetric square splits into its scalar, three summands of dimension \(35\), and a final summand of dimension \(300\). On these spaces \(Q\) takes the values \(12,4,-2\), respectively. One can therefore reverse the colour contraction on a symmetric state by applying
\[
 Q^{-1}=\frac{-Q^2+14Q-16}{96}.
\]
For example on a traceless symmetric tensor in a \(35\)-dimensional summand the right side gives \(1/4\). The skew part supplies all \(28\) translated generators, since every element of \(\mathfrak{so}_8\) is a sum of brackets. Thus the ordered first correction spans all \(406+28\) weight-two states of the universal vacuum. On \(\Lambda^2\mathfrak{so}_8\) its kernel is the kernel of the bracket map. In particular, a single wedge \(a\wedge b\) is killed exactly when \([a,b]=0\). A finite-rank representation, as the two-dimensional symplectic example shows, can kill some of these states.

There is a reason the reconstruction works for every simple complex Lie algebra. On an irreducible summand of highest weight \(\nu\), the split operator is \(2h-c_\nu/2\), where \(c_\nu=(\nu,\nu+2\rho)\) uses long roots of squared length two. These numbers are nonzero on the symmetric square. For example in type \(A_1\) they are \(4,-2\); in \(G_2\) they are \(8,10/3,-2\). The same argument gives the symmetric weight-two states and all translations. A direct sum of two simple Lie algebras already behaves differently. A colour in each of two different ideals has no common contracted generator. Their symmetric two-current state can exist although every such mixed quadratic residue vanishes. [Isaev and Krivonos, the split Casimir and its spectral projectors](https://arxiv.org/abs/2102.08258)

Measuring a quadratic state by another current is a different experiment. Write its affine bracket as \([J_x{}_\lambda J_y]=J_{[x,y]}+k\kappa(x,y)\lambda\mathbf1\). Identify \(a\odot b\) with the linear map \(x\mapsto(\kappa(x,a)b+\kappa(x,b)a)/2\). The first positive mode of \(J_x\) on a symmetrized quadratic state \(S\) gives the current of colour \(((2k-Q)S)(x)\). The central terms supply \(2kS(x)\). The remaining term is the integral in the Wick rule, with colour \(([[x,a],b]+[[x,b],a])/2\). At compact-normalized level \(k=2\) in \(\mathfrak{so}_8\) every state in the three \(35\)-dimensional sectors becomes invisible to this test. The inversion of the original quadratic coefficient still makes sense in the universal vacuum at that very level. The first positive mode on the coefficient can vanish while the coefficient survives.

At level zero the local Ward test on \(q\) also identifies the obstruction to using the open pole in isolation. Let \(\mathcal S(a,b,x,y)\) be the fully symmetrized trace of the four adjoint matrices; use \(\kappa\) to raise the last two indices. The trace of four skew-adjoint matrices has only three distinct cyclic and reversal classes. The average of two of these classes gives \(Q^2\); subtracting the remaining class amounts to tracing a product of two commutators. Since the trace pairing of two adjoints is \(-2h\kappa\), one obtains
\[
 \mathcal S=Q^2-\tfrac h3 Q
 \quad\text{on }\operatorname{Sym}^2\mathfrak g .
\]
Add \((h/6)(T+2\mu)J_{[a,b]}\) to the symmetrized residue, with \(\mu\) the spectral variable of the two incident fields. The current Jacobi identity on \(J_x\) and those fields then has residual \(-\lambda J_{\mathcal S(a\odot b)(x)}\) if their other brackets retain only the tree adjoint actions. The term with \(T\) supplies precisely the commutator correction to \(Q^2\). The residual is still nonzero. In the long-root-positive \(\mathfrak{sl}_2\) convention, testing the Cartan generator \(\mathrm{diag}(1,-1)\) in all three slots gives \(-16\lambda J_{\mathrm{diag}(1,-1)}\). Every bracket of two incident colours in this last test vanishes.

Can a single invariant scalar account for that fourth-order tensor? In the eight-dimensional vector representation of \(\mathfrak{so}_8\), choose the Cartan with all four positive vector weights equal to one. Six roots have value \(+2\), six have value \(-2\), and the remaining adjoint weights are zero. The fourth adjoint trace is \(192\), while the square of the second vector trace is \(64\). The identity is \(\mathrm{Tr}_{\rm ad}X^4=3(\operatorname{tr}_8 X^2)^2\), or \(12\kappa(X,X)^2\). For \(\mathfrak{sl}_4\), the Cartan diagonals \((1,-1,0,0)\) and \((1,1,-1,-1)\) give ratios \(10\) and \(8\) to the squared second defining trace. A single scalar coefficient cannot fit both values. Precisely \(A_1,A_2,G_2,D_4,F_4,E_6,E_7,E_8\) have a factorizing adjoint fourth trace. For them its coefficient in \(\kappa(X,X)^2\) is \(h+6\). This identifies the colour tensor that a closed exchange would have to cancel. The coupled theory must still supply the closed field, its propagator and the two reciprocal actions. Adding charged matter changes the trace in the obstruction to \(\mathrm{Tr}_{\rm ad}-\mathrm{Tr}_R\); it changes the physical theory as well. [Costello and Li, the type I anomaly](https://arxiv.org/abs/1905.09269) · [Costello and Paquette, the gauge-theory associativity test](https://doi.org/10.1103/PhysRevLett.129.231604)

### What cancels the local obstruction {#ch14-celestial-closed-ward}

In flat Wess–Zumino–Witten theory the closed field on twistor space is a constrained Beltrami differential, or equivalently a \(\partial\)-closed two-form with an antiholomorphic leg after contraction with the holomorphic volume. Its coupling to two open fields has the form \(\int\eta\,\operatorname{tr}(A\partial A)\). In four dimensions it describes fluctuations of the Kähler potential in Mabuchi gravity. The holomorphic data at the two poles of the twistor line are part of the bulk quantization. There are two reciprocal operations to normalize. Two open parameters \(af,bg\) produce the closed form \(uK(a,b)\,df\wedge dg\); a closed two-form acts back on an open parameter through its volume-preserving vector field with coefficient \(v\ell_{\rm bulk}\). A return from open fields to open fields can therefore measure the product \(uv\ell_{\rm bulk}\). [Calibration on the crossed current colours](#ch14-celestial-yangian-like) For instance, rescaling the open-to-closed operation by a nonzero scalar and the reciprocal operation by its inverse gives the same returned open coefficient. A separate closed-field measurement must fix the scale of the individual operations. Transporting the calculation to another geometry also requires its distance normalization, closed propagator and boundary vacuum. [Costello, the twistor-space quantization](https://arxiv.org/abs/2111.08879) · [Costello, Paquette and Sharma, the four-dimensional fields](https://arxiv.org/pdf/2306.00940v2)

One can make the test of the closed sector directly in the marked flat model. Let \(E[2,0]\) generate the transverse Hamiltonian \(w_1^2/2\), and set \(s=uv\ell_{\rm bulk}\) for the two reciprocal closed-operation normalizations of the preceding example. On the second open jet, the principal Hamiltonian action is \(2v\ell_{\rm bulk}J_b[1,1]\). The contour with two disjoint colours also detects a lower-field double pole. Keep \(u\ne0\) in this calibration. With \([A_\nu B]=\sum_{j\ge0}\nu^j A_{(j)}B/j!\), the constant and linear terms in \(\nu\) read the simple and double poles, respectively. In this convention the two terms are
\[
\begin{aligned}
 [E[2,0]{}_\nu J_b[0,2]]
    &={}2v\ell_{\rm bulk}J_b[1,1]\\
    &\phantom{{}={}}-\frac{s^2}{2u}\nu J_b[0,0].
\end{aligned}
\]
The second coefficient comes from applying the positive affine mode to the crossed quadratic colour residue; the four nonzero colour contractions sum to \(-4T_{34}\) for \(b=T_{34}\). Rotations give the other root-plane colours. There is an independent contraction in the balanced D1 model, with the centre-of-mass field retained and Chan–Paton superdimension zero. Normalize the elementary matrix propagator by \(h\) and give the two transverse jets scale factors \(x_1,x_2\), with \(x_1x_2h=s\). The closed input acts by \(x_1^2\operatorname{Str}(X_1^2)/(2u)\), and the marked open input has two \(X_2\)'s between its flavour endpoints, with scale \(x_2^2\). A single Wick contraction replaces either \(X_2\) by \(X_1\), giving the first coefficient above. In a double contraction the two pairings cancel the \(1/2\) in the closed input. The sum over supertrace-dual self-adjoint matrices on the remaining open word is \(-\tfrac12\) times the identity at superdimension zero. The two propagators and jet scales therefore give \(-s^2/(2u)\) on the zero jet. This equality compares the displayed matrix elements in the marked flat and balanced models. This decides a lower-field question left open by the maximal tree symbol, for these marked operations and lifts. A complete comparison would also intertwine the remaining closed fields, their descendants and their collisions on both geometries.

The axion in anomaly-cancelled self-dual Yang–Mills provides a calculation on a different pair of fields. Take \(H_x=J_x[0,0]\), \(P_a=J_a[1,0]\), \(Q_b=J_b[0,1]\) and \(L_a=\widetilde J_a[0,0]\). In the present paragraph use the gauge theory's invariant form \(K=B_{\rm Kill}/(2h)\) and its pole at \(z-w\). With these divided jets let \(a_0=-\hbar/(32\pi^2)\), and let \(\lambda,\mu\) be the formal variables of the two longitudinal brackets. The one-loop open residue contains \(:J\,\widetilde J:\), its symmetrization and the linear companion fixed by the affine Wick formula. For colours \(x,y,z\), let \(G(x,y,z)\) be the sum of \(K(y,z)x\), \(K(x,y)z\) and \(K(x,z)y\). In the three-current Jacobi identity the open terms contribute
\[
 -\tfrac{2a_0\gamma}{3}\,\lambda L_{G(x,y,z)} .
\]
Here \(y,z\) are the two incident colours. The quartic factor in these units is \(\mathrm{Tr}_{\rm ad}X^4=\gamma K(X,X)^2\). Follow the other intermediate states in the three possible nestings. The closed \(F[0,0]\) produced by \(P_y,Q_z\) returns \(L_x\). The brackets of \(H_x\) with \(P_y\) or with \(Q_z\) produce \(E[1,0]\) or \(E[0,1]\), whose reciprocal action gives \(L_z\) or \(L_y\). Each closed vertex has coefficient of order \(\sqrt{\hbar}\). The three return paths add \(\ell^2\lambda L_{G(x,y,z)}\). With \(\ell^2=-\gamma\hbar/(48\pi^2)=2a_0\gamma/3\), the Jacobi residual cancels. Dropping \(F[0,0]\) would lose the coefficient of \(K(y,z)x\) even if the other two contractions were retained. [Costello and Paquette, the self-dual gauge Ward calculation](https://doi.org/10.1103/PhysRevLett.129.231604) · [Fernández and Paquette, the tree couplings](https://arxiv.org/pdf/2412.17168v2)

The cancellation has a jet-dependent test. Give the three incident positive-helicity currents degrees \(p,t,r\in\mathbb N^2\) and let \(p\wedge r=p_1r_2-p_2r_1\). The three determinants are constrained by
\((t\wedge r)p-(p\wedge r)t+(p\wedge t)r=0\). In the component with one negative-helicity current, the open term and the three closed returns therefore come with the same longitudinal operator
\[
\begin{aligned}
 \Omega={}&(t\wedge r)\lambda-(p\wedge r)\mu\\
          &-(p\wedge t)(\lambda+\mu+T).
\end{aligned}
\]
Its output jet is \(p+t+r-(1,1)\); a negative index gives zero. The open and closed prefactors are again \(-2a_0\gamma/3\) and \(\ell^2\). The quadratic fields retain a second test at each ordered pair of output jets. Give the \(J\) and \(\widetilde J\) outputs separate transverse variables \(Z,W\). Their one-loop coefficient integrates the alternating product of two gradients at two ordered points of the segment from \(W\) to \(Z\). Apply the product rule to a third polynomial. The terms left after subtracting the two endpoint actions form an alternating expression in three transverse covectors. It vanishes in two dimensions. This is the associative cocycle identity for the ordered coefficient. Its antisymmetrization gives the six quadratic terms in the current Jacobi identity, with the adjoint matrices in their original order. Together the one-current and two-current calculations exhaust the order-\(\hbar\) identity for three positive-helicity currents of arbitrary jets in the pure gauge theory coupled to its axion.

A double pole from two *positive*-helicity inputs tests the order of an intermediate mixed bracket. Reversing just its jet labels changes the resulting Ward identity. Work in the anomaly-cancelled \(\mathfrak{su}_2\) theory with \(f_{ab}{}^c=\varepsilon_{abc}\), inverse form \(-2\delta^{ab}\), and the fixed lower gauge and axion products. Take *two positive-helicity* inputs of degrees \((m,0),(0,m)\), and select \(m\) negative-helicity output currents all of degree zero. Denote by \(b_m\) the double-pole multiplier after removing the ordered colour chain and the common gauge factors, including \((\hbar/(16\pi^2))^m\). When a nested pair reverses, both its colour chain and its ordered transverse labels must reverse together. The printed expression for this double pole gives \(b_3=1/3\). In the basis \(0,1,2\), choose the two input colours \(0,0\) and the testing colour \(2\). On the output \(\widetilde J_2[0]^3\) the right side minus the left side is \(-4\) after removing only \((\hbar/(16\pi^2))^3\). The adjoint factor \(4\) and the colour chain remain in this residual. Every unknown derivative coefficient drops out of this component. It cannot be repaired by adjusting those coefficients. Keeping the inner pair in its correct order gives \(b_3=1/12\). At four loops the same test replaces \(7/45\) by \(1/18\). These discrepancies concern the positive–positive double pole. The mixed-helicity scalar in the first section enters its calculation with a definite order of its arguments. [Fernández and Paquette, the double pole and the nested mixed product](https://arxiv.org/pdf/2412.17168v2#page=70)

One can do this Ward calculation at every \(m\ge2\). Take the coefficient linear in \(\lambda\) and constant in \(\mu\) with a testing current of jet zero. Polarize the \(m\) outgoing colours from a single colour vector and first take the testing colour parallel to it. Take the two incident colours in the perpendicular plane. Derivatives of individual outgoing fields drop out. An inner mixed bracket can contribute only when its two transverse labels supply its order. Its colour matrices then kill the terms in which the two selected slots are separated. The sum over the surviving Wick contractions is \(-m(m+2)/(6m!)\). The axion returns \(m^2/(3m!)\). Thus in the normalization above the *total* double-pole coefficient on this family is
\[
 b_m=\frac{m-2}{6(m-1)!}.
\]
Any further term allowed in that same double-pole component must be counted in its total. The first three values are \(0,1/12,1/18\).

There is also a simple pole with one longitudinal derivative. In the ordered colour-chain ansatz, with these fixed lower products and no separately prescribed additional derivative term, write \(c_j\) for the multiplier when the derivative lands in slot \(j\). A testing colour perpendicular to the repeated colour distinguishes the two endpoints. It gives \(c_1=b_m\) and \(c_m=0\). In the three-dimensional adjoint representation the interior insertions all induce the same operator. Exchanging the inputs fixes their sum to \((m-2)b_m/2\). Polarization gives every choice of output colours at zero transverse jet. These equations determine the derivative operator there. Other transverse output jets and the remaining powers of the two longitudinal variables have their own Ward equations.

To see which part of this distinction is already algebraic, give each colour a coefficient in the dual numbers \(A=\mathbb C[\epsilon]/\epsilon^2\). The tree bracket on \(\mathfrak g\otimes A\) has \([x\otimes1,y\otimes\epsilon]=[x,y]\otimes\epsilon\) and \([x\otimes\epsilon,y\otimes\epsilon]=0\). These are the two gauge towers before adding the axion. Give \(A\) the trace \(\tau(1)=0,\ \tau(\epsilon)=1\). Contracting two coefficient indices now inserts the copairing \(c=1\otimes\epsilon+\epsilon\otimes1\). Multiplying its two legs gives \(2\epsilon\). Thus on symmetric coefficients the operation \(D=\Delta_A\circ\mu_A\), with \(\Delta_A(v)=(v\otimes1)c\), gives the chain
\[
 1\otimes1\longmapsto c
 \longmapsto 2\epsilon\otimes\epsilon\longmapsto0 .
\]
The colour operator is \(Q_{\mathfrak g}\otimes D\) on symmetric colour and coefficient pairs, and vanishes on pairs alternating in both. Its cube is zero. Yet for the \(\mathfrak{sl}_2\) Cartan generator \(h_0=\mathrm{diag}(1,-1)\), the ordinary adjoint fourth trace at \(h_0\otimes1\) is \(64\), twice its value on \(\mathfrak{sl}_2\). The Frobenius norm of that element is zero. Nilpotence of the colour operation has therefore left a nonzero Ward obstruction. The physical cancellation required the two closed vertices.

The same argument works over any finite-dimensional commutative Frobenius algebra. Its regular trace is \(\mathrm{Tr}(m_v)=\tau(e v)\), with \(e=\sum_i u_i u^i\) for dual bases. On a local block that is larger than its residue field, \(e\) spans the socle, \(e^2=0\), and \(\tau(e)=\dim A\). Consequently \(D\) on that block always has \(\operatorname{rank} D=\dim A\), \(\operatorname{rank}D^2=1\), \(D^3=0\). A nonzero uniform affine level makes the measurement \(2k-Q_{\mathfrak g\otimes A}\) invertible there, although the ordered quadratic field still has a kernel. The coefficient coalgebra has a counit, but its coproduct sends \(1\) to a tensor whose square is \(2\epsilon\otimes\epsilon\) in the dual-number case. It does not preserve the field product required for fusion of two lines.

The gravitational calculation begins at a different tree algebra. In self-dual gravity the gauge bracket is replaced at tree level by the Hamiltonian bracket \(\{x^p y^q,x^r y^s\}=(ps-qr)x^{p+r-1}y^{q+s-1}\). On \(x^3,y^3\) this gives \(9x^2y^2\). The gravitational axion also couples through the covariant kinetic term; its two fields have their own descendant coefficients. For these jets the transverse contractions \(R_j\) are the \(j\)-fold contractions of transverse derivatives by the alternating bivector. They give \(R_1=9,\ R_2=R_3=36\). In the gravitational axion normalization the new order-\(\sqrt{\hbar}\) output is proportional to \(-36 f[0,0]+18(T+2\lambda)e[1,1]\). Already the first axion exchange uses information absent from the Poisson structure constant. This places a concrete limit on transporting the gauge recurrence to gravitational amplitudes. [Bittleston, celestial OPEs in self-dual gravity](https://arxiv.org/pdf/2211.06417v3) · [Fernández and Paquette, gravitational axion products](https://arxiv.org/pdf/2412.17168v2)

### From a collision to its homotopies {#ch14-celestial-coherent-collisions}

After a contour has produced \({:}J_cJ_d{:}\), the pair inside the colons is one state for the next collision. Translating an incident current tests more than this surviving state alone. To pass from a pole of currents to an associative chiral algebra one must also say how that state is attached to the collision stratum and how two successive attachments compose. Even a translation of the inputs measures this attachment. Suppose \(Y(a,u)b=C/u\) in the polar part and let \(f\) be regular at zero. Translating the first input gives \(-C/u^2\), whose residue against \(f\) is \(-f'(0)C\). Translating the second gives \(TC/u+C/u^2\), with residue \(f(0)TC+f'(0)C\). Their sum is the translation of the original output. Erasing the second-order pole before testing against \(f\) destroys this identity.

**Example (an ordered product on the punctured plane).** Take a normal slice to the line and remove its origin. For \(R=\mathbb C[x,y]\), the open charts \(D(x)=\{x\ne0\}\) and \(D(y)=\{y\ne0\}\) have rings \(R_x,R_y\). On the overlap both coordinates are invertible. The ordered Čech complex is \(R_x\oplus R_y\to R_{xy}\) in degrees zero and one, with differential \((a,b)\mapsto b-a\). On an overlap cochain \(w\), left multiplication by \((a,b)\) uses \(aw\) and right multiplication uses \(wb\). Its degree-zero classes are polynomials. Its degree-one classes are represented by linear combinations of \(x^{-i}y^{-j}\), \(i,j\ge1\). The cohomology products \(x[x^{-1}y^{-1}]\) and \([x^{-1}y^{-1}]y\) vanish, but they have different primitives. \(1/y\) extends over \(D(y)\), and \(1/x\) extends over \(D(x)\). Take the two primitives \((0,1/y)\) and \((-1/x,0)\). Multiply the first on the right by \(y\), and subtract the product of \(x\) with the second. The result is \((1,1)\). Changing either primitive changes this answer by an element of \((x,y)\). Thus the triple Massey product is \(1+(x,y)\), and contains no zero. The ordered differential algebra on the punctured plane retains a homotopy that cannot be read from its two cohomology products.

More generally for \(\xi=[q/(x^my^n)]\) one can calculate the entire indeterminacy. If \(f\xi=\xi g=0\), write \(fq=A x^m+B y^n,\ gq=C x^m+D y^n\). Then, for the same order of the two choices of primitive, the answer is \(w+(f,g)\), where
\[
 w=\frac{fD-Bg}{x^m}=\frac{Ag-fC}{y^n}.
\]
The two fractions agree and lie in the intersection \(R_x\cap R_y=R\). In particular taking \(q=1,\ f=x^m,\ g=y^n\) gives a unit modulo \((x^m,y^n)\) for every positive \(m,n\). The splitting of Laurent monomials used here is linear over \(\mathbb C\). Multiplying a negative-negative monomial by \(x\) can move it into the other chart, so this choice of homotopy is not \(R\)-linear. Descent of a local propagator under a change of normal coordinates requires an actual comparison.

Transposing a single quadratic residue into ghosts encounters a related problem. Use \([h,e]=2e,[h,f]=-2f,[e,f]=h\). Let \(\eta,p,q\) be odd fields dual to the zero jet and its two first transverse jets. The symmetric quadratic output tensor \(S_{ab}^{cd}\) transposes to the component \([\eta^c{}_\lambda\eta^d]=-2a S_{ab}^{cd}:p^a q^b:\). Suppose one keeps just this singular component, makes \(p,q\) singularly central, and retains the tree Chevalley–Eilenberg differential with \(d_0 p^h=-\eta^ep^f+\eta^fp^e\). The bracket \([\eta^h{}_\lambda p^h]\) is zero, while \([\eta^h{}_\lambda d_0p^h]\) contains \(-4a p^ep^fq^h\). The other terms have different exterior monomials. Hence \(d_0\) fails to preserve a defining bracket. This coefficient survives after discarding every translated jet, so a total derivative cannot remove it. The selected transpose remains a correct coefficient. Extending it to a differential on this larger collection of fields needs more first-order brackets.

There are two places where an actual construction can start. In a central model take even \(L_c,R_t\) with zero singular brackets against every generator and give the active \(P_a,Q_b\) the sole bracket \(f^t_{ab}R_t+aS_{ab}^{cd}:L_cL_d:\). On the dual side use closed central odd \(p,q\), set \(d r^t=-f^t_{ab}:p^a q^b:\), and take the displayed bracket on the \(\eta\)'s. All outputs in the defining brackets are now central. The canonical pairing cancels the linear term by \(dr\) and the quadratic term by the ghost bracket. This soluble chiral model omits the adjoint action that gave the preceding cubic obstruction.

For a general unital mode algebra one can instead keep *every* word. Choose a linear retraction to scalars and write \(xy=\mu(x,y)+c(x,y)1\) on its kernel. On functions of words insert \(\mu\) in adjacent slots with the alternating bar signs. Associativity implies \(dc=0\) and \(d^2\phi=\phi\smile c-c\smile\phi\). Already for \(M_2(\mathbb C)\) with half the trace as retraction, \(c(E_{12},E_{21})=1/2\). If \(\phi(\mathrm{diag}(1,-1))=1\) and \(\phi(E_{12})=\phi(E_{21})=0\), the square on \(E_{12},E_{21},\mathrm{diag}(1,-1)\) is \(-1/2\). The curvature records the scalar vacuum term that the retraction removed. The word construction needs the complete product as input, as well as continuity on the chosen completed tensor powers when the modes are topological.

### Where successive collisions meet {#ch14-celestial-cut-support}

Label the insertions \(1,\ldots,n\) by their positions in a word. Their geometric positions \(z_1,\ldots,z_n\) vary on a smooth separated finite-type curve \(X\). Shrinking a gap in a word is allowed only while the two groups on opposite sides of that gap have disjoint supports. At two points there is one gap. At three points the word \(1,2,3\) can be cut either after 1 or after 2. A collision between 1 and 3 crosses both cuts, even if 2 is elsewhere.

**Definition (support of the consecutive cuts).** In \(X^n\) let \(U_p\) consist of the tuples with \(z_i\ne z_j\) for every \(i\le p<j\), and let \(Z_n=X^n\setminus\bigcup_{p=1}^{n-1}U_p\). A tuple lies in \(Z_n\) exactly when every cut is crossed by an equal-coordinate pair. For an arity-connected cut coalgebra \(C\) of right algebraic \(\mathcal D\)-modules that factorizes on every \(U_p\), the reduced cobar in arity \(n\) is \(R\Gamma_{Z_n}(C_n)[-1]\). The local cohomology takes the part of the coefficient supported on this closed locus, with its derived attachment. The shift is cohomological. [The cut construction and its mapping spaces](#ch12-associative-products-on-configurations)

For \(n=3\) the first cut fails on \(\Delta_{12}\cup\Delta_{13}\), the second on \(\Delta_{13}\cup\Delta_{23}\). The reduced support is therefore \(\Delta_{13}\). Even this example distinguishes the underlying set from a scheme intersection. On the affine line put \(a=z_1-z_2,\ b=z_2-z_3\). The intersection of the two discriminant divisors has ideal \((a+b)(a,b)\). The class of \(a+b\) has square zero and is nonzero there. It disappears on the reduced support. One can know the support exactly and still have to decide which sheaf, thickening or local cohomology complex describes the observable.

At \(n=4\), either \(z_1=z_4\), or the two simultaneous equalities \(z_1=z_3,\ z_2=z_4\) cross the three cuts. Their intersection is the small diagonal. Over a finite field let \(s\) be the number of rational points on \(X\). The first component has \(s^3\) rational points, the second \(s^2\), and the intersection \(s\). Inclusion–exclusion gives \(s^3+s^2-s\). There is a uniform count in every arity. Partition the labels by their exact equal coordinates. Such a partition is supported precisely when no proper initial segment is a union of blocks. Every partition factors uniquely by cutting at all the boundaries no block crosses. If \(a_{n,k}\) counts the resulting indecomposable partitions with \(k\) blocks, each such partition contributes one copy of \(\operatorname{Conf}_k(X)\), the space of ordered \(k\)-tuples of distinct points of \(X\). Order the blocks by their least label. Repeating the coordinate of each block gives the corresponding stratum of \(Z_n\). Thus in the Grothendieck ring the class of \(Z_n\) is
\[
 \sum_k a_{n,k}\,[\operatorname{Conf}_k(X)] .
\]
For a positive-dimensional geometrically integral curve its irreducible components are given by minimal systems of equality pairs whose intervals cover the cuts. There are \(2^{n-3}\) components for \(n\ge3\). The equality strata keep track of their overlaps. They do not specify the restriction maps of a complex on those overlaps.

There is a corresponding derived distinction on the affine line. At five labels take the conditions \(z_1=z_3,\ z_2=z_5\) for one component and \(z_1=z_4,\ z_3=z_5\) for a second. The four equality edges form a spanning tree, so their four linear equations are independent and cut out the small diagonal. Add the component \(z_1=z_5\). The ordinary intersection is still the same small diagonal, but its derived intersection now has a degree-minus-one generator. The fifth equation closes an edge cycle and is a linear combination of the other four. In the Koszul complex one may subtract that combination and leave one generator with zero differential. More generally the excess generators for a multigraph of equality edges form its cycle space; parallel copies of a shared edge count separately. Knowing the reduced join alone would give the same answer for the tree and for the tree with an extra edge.

At finite perturbative order, work modulo \(s^N\), with \(s^2=\hbar\) when a vertex has an order-\(\sqrt{\hbar}\) coupling. The cut construction can then be applied before taking a limit.

**Conditional theorem (completed cut cobar).** Suppose for every \(N\) the fully specified current source gives a connected coaugmented collision coalgebra \(C_N\), factorizing over each \(U_p\), compatible with derived change of coefficients. Then \(A_N=\Omega_{\rm cut}C_N\) is an associative chiral algebra for the consecutive-cut convolution. The connected bar–cobar mapping-space equivalence applies at each \(N\); taking the derived inverse limit gives the corresponding complete object. At each fixed arity only finitely many positive cut words occur, so the conclusion allows an infinite tower of transverse currents.

A scalar pole makes the order of these operations visible. \(\sum_{j\ge0}s^j/u^j\) has bounded pole order at every finite \(N\), but no common finite pole order over \(\mathbb C[[s]]\). An all-loop list of singular coefficients supplies neither the regular collision products nor their coordinate changes. Those are inputs to this passage from a field theory to the chiral algebra.

### Ordered transport and tensor products {#ch14-celestial-ordered-transport}

An ordered list of output jets can be tested without identifying their positions in the list. At the first mixed-helicity step let two successive integrations have densities \(2s_1\) and \(1\) on \(0<s_2<s_1<1\). Interchanging the jet orders puts the factor \(2s_2\) under the same integral. This elementary distinction persists in the angular recurrence at every length. On one transverse axis, put \(d_i\) for the outgoing degrees and \(b_i=d_i+1\). In the order \(\widetilde J[r](z)J[t](0)\) take \(r=(m+\sum_i d_i,0)\), \(t=(0,m)\), with outputs \(k_i=(d_i,0)\). The second input has total degree \(m\). There are \(m+1\) outputs and the last-slot recurrence reduces to an iterated integral. After the individual monomial factors are removed its weight is
\[
 \prod_{i=1}^{m}\frac{b_i}{b_i+\cdots+b_{m+1}} .
\]
For two outputs of degrees \(1,0\), integrate \(2s_1\) on the triangle \(0<s_2<s_1<1\). The integral is \(2/3\). Reversing the degrees puts the density \(2s_2\) on the same triangle and gives \(1/3\). In general the weight is the integral over \(1>s_1>\cdots>s_{m+1}>0\) with density \(\prod_i(d_i+1)s_i^{d_i}\). In the signed mixed-helicity scalar on this axis the weight occurs with a minus sign. For general two-coordinate jets with one incident polynomial of total degree \(m\), polarizing a pure power of a linear form gives the same suffix product multiplied by the appropriate binomial coefficients. If both incident degrees exceed \(m\), evaluating both differentiated inputs at the same barycentric point fails. At \(m=1\), with incident \(x^2,y^2\), the two crossed output monomials have coefficients \(-5/6,-1/6\) in the normalized recurrence. A common evaluation would give \(-1/3,-1/3\).

Write \((B_j)_{ab}=f_{ab}{}^d\widetilde J_d[j,0]\), and let \(Y_j=GB_j\), where \(G=K^{-1}\) raises the first colour index. The ordered colour chain contributes its own minus sign, so the signed scalar gives a positive matrix word with these conventions. The parameter \(u\) marks the outgoing jet order. The generator at the integration variable \(s\in[0,1]\) is \(A(s,u)=\sum_{j\ge0}(j+1)s^ju^jY_j\). With an independent formal parameter \(q\), the ordered integrals solve \(U'=qAU,\ U(0)=1\). The largest time multiplies on the left. At order \(q^2u\) this gives \(2Y_1Y_0/3+Y_0Y_1/3\). Taking \(Y_1=\operatorname{ad}_e,\ Y_0=\operatorname{ad}_f\) in \(\mathfrak{sl}_2\), this coefficient sends \(e\) to \(4e/3\). Reversing the order gives \(2e/3\), and exponentiating the time integral without ordering gives \(e\). The difference can therefore be measured in a two-generator colour sector.

Concatenating two ordered intervals multiplies their endpoint matrices. This gives a group law when the coefficients are formal jet coordinates. With primitive adjoint letters, the ordered exponential \(U(1)\) is group-like in the completed enveloping algebra. Its logarithm divided by \(q\) is a Lie series \(\Psi(Y)\), with leading term \(Y(u)\). It can be inverted recursively. Multiplying two endpoint matrices transports the Baker–Campbell–Hausdorff law back through \(\Psi\) and gives an associative product on formal jet coordinates. At output degree \(a+b\), the first mixed correction has coefficient \((b+1)/(a+b+2)\) on \(q[Y_{L,a},Y_{R,b}]\). For \(a=b=0\) one recovers the ordinary half-commutator. The successive intervals, their order and their formal parameter are part of the construction.

Now specialize \(q=\hbar uv/(16\pi^2)\), where \(v\) marks the other incident jet. Can this jet law act by a single coproduct on physical current generators, independent of \(u,v\)? If the same matrix numerator were to intertwine this coproduct with multiplication of endpoint matrices for all \(u,v\), its coefficient of \(v^0\) would force the detected gauge currents to remain exactly primitive. The mixed commutator at the next order contradicts that value for noncommuting colours. This excludes that particular spectral-independent intertwining equation. A separating parameter or a different tensor product of line operators changes the question.

The first mixed residue has thus led to two explicit tensor constructions with different domains. The triangular brane currents act diagonally on a genuine pair of modules. The ordered mixed-helicity coefficients compose by a group law on formal endpoint data. To identify an operation on two physical defects one needs the tensor product of their states and a map carrying their marked collision operators to that tensor product, compatible with translation, exchange and a third defect. Its restrictions would have to recover the crossed first-jet residue and closed Ward identity on the flat chart, the fourth-pole pairing on the finite-rank brane, and the ordered \(4/3\) reading in the indicated mixed-helicity colour representation.

[Download *What the celestial residue determines* (PDF)](celestial-residue.pdf)

### A meromorphic surface defect on mini-twistor space {#ch14-cotangent-yangian-defect}

An oriented line in Euclidean three-space is determined by its direction and its point closest to the origin. The space of these lines is the mini-twistor surface \(M=\operatorname{Tot}_{\mathbb P^1}\mathcal O(2)\). A marked point on the line gives a real coordinate \(t\), its signed distance from the closest point. Thus the correspondence space is smoothly \(\mathbb R_t\times M\). The sphere of lines marked at the origin is the surface \(S=\{t=0,u=0\}\), where \(u\) denotes the tautological fibre coordinate. A framed gauge defect on \(S\) gives a classical realization of spectral loop coordinates and their dressing action.

The variable \(u\) measures transverse displacement at fixed direction. A pole at \(u=0\) can therefore be probed by transporting a gauge frame along \(t\) on a nearby line with \(u\ne0\). Fix the frames at both ends. The scattering matrix transports an outgoing frame back to the incoming frame. For two successive elementary sheets, take \(T_1=I+E_{12}/u\) and \(T_2=I+E_{21}/u\), where \(E_{ij}\) are matrix units. Both orders give \(E_{12}+E_{21}\) at \(u^{-1}\). At \(u^{-2}\) the product \(T_1T_2\) gives \(E_{11}\) and \(T_2T_1\) gives \(E_{22}\). A measurement of the upper-left entry at fixed direction distinguishes the orders. We now construct a connection giving a single such simple-pole scattering matrix.

**The field and its scattering matrix.**

Write \(d'=d_t+\bar\partial_M\) for the differential on forms modulo the holomorphic one-forms pulled back from \(M\). Take the classical holomorphic-topological \(GL_n\) BF action
\[
 S_{\rm BF}=\int_{\mathbb R\times M}
 \left\langle B,d'A+\tfrac12[A,A]\right\rangle .
\]
Here \(A\) is a \(\mathfrak{gl}_n\)-valued partial one-form and \(B\) is a \(K_M\otimes\mathfrak{gl}_n^*\)-valued partial one-form. The holomorphic top degree carried by \(B\) supplies the integration density on \(M\), whose canonical line is \(p^*\mathcal O(-4)\) for \(p:M\to\mathbb P^1\). The equations are \(F'_A=0\) and \(D'_AB=0\). This is the undeformed, one-topological-direction BF theory. [Elliott–Safronov–Williams, Theorem 9.3](https://arxiv.org/abs/2002.10517) · [Zeng, §6.5](https://arxiv.org/html/2607.09486v1#S6.SS5)

Fix holomorphic frames at the two real ends. Permit a meromorphic change of frame across the sheet, regular and invertible for \(u\ne0\), and normalized to the identity at fibre infinity. Compactifying each spectral fibre to \(\mathbb P^1_u\) specifies this last condition. Locally at \(u=0\) we allow a Hecke modification, so its type is the list of exponents of \(u\) after regular invertible changes of frame on the two sides. Gauge redundancies fix the end frames. A prescribed singular germ can be regulated by fixing the tangential connection on the excision boundary. This kills the boundary variation proportional to \(\langle B,\delta A\rangle\).

For rank two, use homogeneous coordinates \([x:y]\) on the base and put
\[
 Q=\binom{x}{y}(-y,\ x)
   =\begin{pmatrix}-xy&x^2\\-y^2&xy\end{pmatrix}.
\]
This is a section of \(\mathcal O(2)\otimes\mathfrak{sl}_2\) of rank one everywhere, with \(Q^2=0\). Consequently \(Q/u\) is a globally defined meromorphic matrix. Choose a Hermitian norm on \(\mathcal O(2)\) and a smooth cutoff \(\chi=H(t/\ell(\|u\|))\), where \(H=0\) below \(-1\), \(H=1\) above \(1\), and \(\ell(r)>0\) equals \(r\) near zero and is constant for large \(r\). The fields
\[
 A=(Q/u)d'\chi,\qquad B=0
\]
solve the equations on the complement of \(S\). Indeed \(Q/u\) is holomorphic there wherever \(u\ne0\), and \(d'\chi\wedge d'\chi=0\). At \(u=0,\ t\ne0\) the connection extends by zero.

Use inverse parallel transport \(T_{ab}\), mapping the frame at \(b\) to the frame at \(a\), with \(\partial_b T_{ab}=T_{ab}A_t(b)\) and \(T_{aa}=I\). Transport across the sheet gives \(T=\exp(Q/u)=I+Q/u\). In a local basis for the rank-one nilpotent \(Q\), the matrix \(uT\) has a unit entry and determinant \(u^2\). Its elementary divisors are \(1,u^2\), so the sheet has Hecke type \((1,-1)\) over the entire base. In the displayed framing the same coefficient is a transverse flux,
\[
 \frac1{2\pi i}\int_{S^2_{\rm link}}du\wedge A=Q .
\]
Indeed, on the outward-oriented sphere \((t,u)=(r\cos\theta,r\sin\theta\,e^{i\phi})\), the integrand is \(Q(du/u)\wedge d\chi\). Integration gives \(Q(\chi(0)-\chi(\pi))=Q\) after division by \(2\pi i\). The framed scattering matrix is independent of the choice of cutoff.

**Fusion and the regular frame at the next endpoint.**

Two successive sheets have scattering matrix \(T_1T_2\). Translated cutoffs of sufficiently small bounded widths give connections with disjoint transition regions, so this composition holds for noncommuting charges. After bringing the sheets together one can place the transitions in disjoint ordered intervals of \(t/\ell(\|u\|)\), giving the same product on the complement of a single sheet.

::: figure fig-hecke-two-sheet-order

Let \(\xi(u)\in\mathfrak{gl}_n[u]\) be an infinitesimal change of the incoming holomorphic frame and let \(\eta(u)\) be the change at the outgoing end. Then \(\delta T=-\xi T+T\eta\). The normalization \(T=I+O(u^{-1})\) requires \(T^{-1}\delta T\) to have only strictly negative powers. Since \(\eta\) is polynomial, this determines
\[
 M_T\xi=(T^{-1}\xi T)_+,\qquad
 \rho_\xi(T)=-\xi T+T M_T\xi .
\]
The subscript keeps the polynomial part at infinity. To transport a polynomial label \(\xi\) through two sheets, first split \(T_1^{-1}\xi T_1\) into its polynomial part \(M_{T_1}\xi\) and its strictly negative part. Conjugation by \(T_2=I+O(u^{-1})\) preserves strictly negative powers. The negative part left by the first sheet can therefore contribute nothing to the final polynomial part. This proves \(M_{T_1T_2}\xi=M_{T_2}(M_{T_1}\xi)\). The outgoing label of the first sheet is exactly the incoming label of the second. This gives the classical dressing rule for fusion directly from the two framings. [Zeng, §§3.2 and 5.6](https://arxiv.org/html/2610.10202v2)

**Which loop coordinates occur?** On a base disc, ordered products of simple-pole sheets of the form \(I+f(z)N/u\), with \(N\) a constant rank-one square-zero complex matrix, realize every finite jet of an \(SL_n\) loop based at fibre infinity, for \(n\ge2\). Here \(f\) is holomorphic, with the regular stratum allowed at a zero of \(f\). To see this, put \(s=u^{-1}\). Rank-one square-zero matrices span \(\mathfrak{sl}_n\). The off-diagonal matrix units are examples, and \(E_{ii}-E_{jj}+E_{ij}-E_{ji}\) is another. Products of sheets therefore yield any first coefficient. The commutator of loops beginning with \(I+Xs^a\) and \(I+Ys^b\) begins with \(I+[X,Y]s^{a+b}\), up to terms of degree \(a+b+1\). The inverse of an elementary sheet has charge \(-fN\). Since \([\mathfrak{sl}_n,\mathfrak{sl}_n]=\mathfrak{sl}_n\), induction produces loops whose first nonzero coefficient is any prescribed traceless holomorphic matrix at each order. Correct a target determinant-one jet one order at a time. At order \(r\) the quotient between the target and the approximation is \(I+Xs^r\bmod s^{r+1}\) with \(\operatorname{tr}X=0\), so the correction applies.

Conversely, on a complex spectral fibre every meromorphic \(GL_n\) scattering matrix of this single-support type satisfies \(\det T=1\). Its determinant has neither zeros nor poles outside \(u=0\), and its value at infinity is \(1\). A principal divisor on the sphere has degree zero. Over an Artin base a nilpotent deformation can have nonconstant determinant. In the local free abelian theory the two polar fluxes realize the logarithmic determinant coordinates and the central currents. [The two central fluxes](#ch14-cotangent-central-flux)

**The chiral comparison.**

Which field product could detect this classical profile? For a polynomial frame label \(\xi(u)\), let \(L_\xi\) denote the current generating its dressing action, and \(K_\xi\) the coordinate current in the corresponding loop-matrix presentation. The latter uses the scattering matrix to express the source in the incoming frame. Its [ordered field realization](#ch14-cotangent-quantum-currents) requires additional surface matter. The classical profile itself is already known. On the chart \(x=1,\ y=z\), its first coefficient in \(u^{-1}\) is
\[
 T^{(1)}=Q(z)=\begin{pmatrix}-z&1\\-z^2&z\end{pmatrix}.
\]
Its diagonal difference \(h=Q_{22}-Q_{11}\) is \(2z\), and \(\partial_z h=2\). The frame change \(E_{12}\) gives \(\rho_{E_{12}}Q=[Q,E_{12}]\), hence \(\rho_{E_{12}}h=2Q_{21}=-2z^2\). For the ordered pair of coordinate currents \(K_{E_{12}u},K_{E_{21}}\), the vertex algebra predicts \(h\) in the double pole and \(\partial_z h\) beyond the algebroid bracket in the simple pole. Acting on the outer double-pole coefficient with a middle \(L_{E_{12}}\) predicts \(-2z^2\). These predictions can be distinguished within this single Hecke stratum. For two copies of the same sheet, \(T^2=I+2Q/u\). In Zeng's matrix vertex algebra the predicted derivative correction \(-\mathcal E(u)\) in the fused \(K\) current has coefficient \(+2Q\) at \(u^{-3}\) on this chart. Indeed only the constant currents enter at this order. The translation \(D=\partial_z\) differentiates the sheet profile along the base curve, with the spectral coordinate \(u\) fixed. For these identical traceless jets, \(Q\,DQ=Q\) and \((DQ)Q=-Q\), so \(-\mathcal E_3=2Q\,DQ-\operatorname{tr}((DQ)Q)I=2Q\). [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6)

The distinction between these scattering observables and quantum currents already appears in perturbation theory. Consider perturbation theory at a fixed defect background with a cotangent propagator pairing \(A\) only with \(B\), and with no boundary or defect interaction vertices. The cubic interaction has one \(B\) leg. With \(v\) bulk vertices, a diagram joining two insertions that depend only on \(A\) can have at most \(v\) internal edges, whereas connectedness needs at least \(v+1\). Hence these observables have no connected mutual contraction in the undeformed theory with fixed boundary data and no additional defect vertices. Adding tangent Fermi fields and specifying an ordered current source gives a different surface theory. Its double pole is \(h\), its simple-pole correction is \(\partial_z h\), and on this profile its outer three-current residue is \(-2z^2\). The same subtraction on two equal sheets gives the fused coefficient \(2Q\). Whether the five-dimensional theory itself selects this surface matter, current and fusion law remains open. [Electric modes on the orbit](#ch14-cotangent-normal-modes) · [The coupled current and its fusion](#ch14-cotangent-quantum-currents)

### An electric mode of the mini-twistor defect {#ch14-cotangent-normal-modes}

On a base disc of the mini-twistor surface, let \(u\) be the spectral coordinate and \(t\) the real correspondence coordinate. Fix frames at both real ends and normalize the scattering matrix to the identity at spectral infinity. A determinant-one Hecke modification of type \((1,-1)\), with scattering matrix and inverse having a single simple pole, has \(T=I+Q/u\), where \(Q\) is a nonzero nilpotent \(2\times2\) matrix. These matrices form a smooth complex surface \(X\).

The scattering coefficient \(Q\) varies along this orbit. To measure an infinitesimal variation \(\delta Q\), couple a normal mode of the dual BF field \(B\) with coefficient \(P\); its pairing with the variation will be \(\operatorname{tr}(P\,\delta Q)\). This is the electric mode conjugate to the magnetic scattering datum. Let \(d'_\perp=d_t+\bar\partial_u\). Choose a cutoff \(\chi\) changing from zero to one across \(t=0\), with transition width of order \(|u|\) near the defect. Choose a radial function \(k\) on the spectral plane, zero near the origin and one near infinity. On the support of \(\bar\partial k\) put \(g=I+\chi Q/u\). For a matrix \(P\), take the fields
\[
 A=(Q/u)d'_\perp\chi,\qquad
 B=-\frac{1}{2\pi i}\,dz\wedge du\wedge\bar\partial k\ g^{-1}Pg .
\]
The electric field vanishes off its spectral annulus and reaches the framed real ends. Both normal field equations hold. With bulk action \((2\pi i\hbar)^{-1}\int\operatorname{tr}(B\wedge F'_A)\), the induced action is
\[
 \frac{1}{2\pi i\hbar}\int dz\wedge\operatorname{tr}(P\bar\partial Q).
\]
Indeed the time integral averages conjugation by \(I+\chi Q/u\) over \(0\leq\chi\leq1\). The spectral integral \(\int u^{-r}du\wedge\bar\partial k=-2\pi i\,\delta_{r,1}\) removes every correction to \(\bar\partial Q/u\). In coordinates \(x^i\) on \(X\), the momenta \(p_i=\operatorname{tr}(P\,\partial_iQ)\) thus have the Gaussian contraction \(p_i(z)x^j(w)\sim\hbar\delta_i^j/(z-w)\).

The electric mode tests the proposed level-zero currents. A polynomial change \(\xi\) of the incoming frame induces
\[
 v_\xi T=-\xi T+T(T^{-1}\xi T)_+ .
\]
Varying the end connections in the BF action couples to \(\operatorname{tr}(P v_\xi Q)\). For \(E=E_{12}\), the dressed incoming source \(Eu+QE\) and outgoing source \(Eu+EQ\) satisfy \((Eu+QE)T=T(Eu+EQ)\). Dressing before quantizing therefore gives zero in the reduced action, even when \(Q_{22}-Q_{11}\) varies.

There is a separate obstruction for every geometric current of the bosonic cotangent surface. Write \(F=E_{21}\), \(H=\operatorname{diag}(1,-1)\) and take \(\xi=H+2uF\). On the double cover \(Q=(a,b)^{\mathsf t}(-b,a)\) its action is \((-a+a^3,b+a^2b)\). At \(Q=E\) it vanishes, with derivative \(2I_2\). The double contraction of \({:}p_iv_\xi^i{:}\) with itself gives \(-\hbar^2\operatorname{tr}((2I_2)^2)=-8\hbar^2\). A one-form improvement \(\alpha_i(x)\partial_zx^i\) changes this coefficient by a term proportional to \(\alpha(v_\xi)\), which vanishes at the fixed point. Zeng's zero-level current has zero self double pole for the same label. A full five-dimensional construction needs an additional contribution to the flavor current algebra and a physical prescription for the dressed composite. The contribution of the remaining bulk and surface fields to these quantum products is open. [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6)

### Cotangent matter on a framed Hecke sheet {#ch14-cotangent-quantum-currents}

A simple pole of a rank-two scattering matrix can have two dynamical coordinates. On the smooth nilpotent orbit \(\mathcal O\) write
\[
 T=1+X/u,\qquad
 X=r\begin{pmatrix}-q&1\\-q^2&q\end{pmatrix},\qquad r\ne0 .
\]
Here \(q\) gives the image line of \(X\), spanned by \((1,q)^{\mathsf T}\), and \(r=X_{12}\) gives its scale on this chart. Since \(X^2=0\), the inverse transition is \(T^{-1}=1-X/u\). The modification is invertible on the punctured spectral fibre, is based at infinity, and has elementary divisors \(u^{-1},u\) at zero. The bosonic cotangent current on this orbit had a double pole even at the fixed point of its frame action. At \(Q=E_{12}\) its self-contraction gave \(-8\hbar^2\) for a generator that vanishes at the point. To realize a level-zero current, add odd partners to the two tangent directions \(q,r\). Their contraction has the fermionic sign. The coupling to the incoming gauge field will determine how the two enter the current.

**The coupling.** Work on a base disc with coordinate \(z\), a spectral disc with coordinate \(u\), and an oriented real interval. The bulk theory is holomorphic-topological BF with partial differential \(d_t+\bar\partial_z+\bar\partial_u\), connection \(A\), and canonically density-valued dual field \(B\). In the incoming regular trivialization let \(a(u)=A_{\bar z}|_{t=0}\) denote its holomorphic jet at \(u=0\). On the punctured overlap flat transport satisfies \(\bar\partial T=-aT+T a_+\), where \(a_+\) is regular. Projection to the regular Laurent part gives
\[
 M_T a=(T^{-1}aT)_+=a_+,\qquad v_a(T)=T M_Ta-aT .
\]
Indeed \(T^{-1}\bar\partial T\) has strictly negative powers. For constant \(C,S\) this gives
\[
 v_C(X)=[X,C],\qquad v_{Su}(X)=XSX=\operatorname{tr}(SX)X,\qquad v_{Su^m}(X)=0\quad(m\ge2).
\]
Consequently the surface coupling depends just on the value and first \(u\)-derivative of the incoming \(A_{\bar z}\). On a flat solution with \(\bar\partial X=v_a(X)\) the outgoing matrix \(M_T a\) gives the regular holomorphic structure of the Hecke transform. This construction permits a fluctuating sheet and specifies matter on it.

Give \(x=(q,r)\) a pair of odd tangent fields \(\psi=(\psi^q,\psi^r)\). A frame variation \(v\) acts by \(\widehat v=(v,\partial v\,\psi)\) on \(Z=(x,\psi)\). Introduce right conjugate momenta \(P=(\beta,b)\), and use the graded cotangent pairing. The surface action in a regular frame is
\[
 S_\Sigma=\frac{1}{2\pi i}\int_\Sigma dz\,
          \langle\bar\partial Z-\widehat v_a(Z),P\rangle.
 \tag{1}
\]
In Ward units the propagators are \(\beta_i(z)x^j(w)\sim\delta_i^j/(z-w)\) and \(b_i(z)\psi^j(w)\sim\delta_i^j/(z-w)\). Adding (1) to the BF action makes \(a\) dynamical. Varying \(A_{\bar z}\) sources \(D'_AB\) by the transpose of the holomorphic jet restriction applied to the surface moment current. Varying \(\beta\) gives precisely the scattering equation above. At zero background the current which sources the constant-frame variation \(v\) is the cotangent Noether current
\[
 L_v=Q\iota_v,\qquad \iota_v=:v^i b_i:,\qquad
 Q=\operatorname{Res}\sum_i:\beta_i\psi^i: .
\]
This expression uses the tangent lift with chiral normal ordering. The elementary propagators give \([L_v{}_\lambda\iota_w]=\iota_{[v,w]}\) and \([L_v{}_\lambda f]=v(f)\). Applying \(Q\) gives the current bracket \(L_{[v,w]}\) with zero level. The odd derivation \(Q\) organizes the fields. The BF gauge BRST differential acts through frame transformations and their ghosts.

For a local framed calculation take tangential \(A\) fixed at the incoming end of the regular slab and tangential \(B\) zero at the outgoing end. Gauge transformations are based at the incoming end and \(B\)-shift transformations at the outgoing end. In perturbation theory on the interval, \(\partial_t\) with the corresponding initial or final condition is invertible. Axial gauges \(A_t=B_t=0\) have triangular gauge variation with field-independent diagonal \(\partial_t\). The surviving BF action is the pairing of \(B_{\mathrm{tan}}\) with \(\partial_t A_{\mathrm{tan}}\). Integrating the dual variables fixes \(A_{\mathrm{tan}}\) to its incoming value. The surface current produces an allowed dual flux at the incoming end. At zero incoming connection the framed surface fields therefore have the Gaussian operator products of (1). Equivalently, a bulk cubic vertex has two \(A\) legs and one \(B\) leg, while a surface gauge coupling brings an \(A\) and no \(B\). With only surface insertions and an \(A\)-\(B\) propagator, no diagram containing either kind of interaction can saturate the bulk legs. This protection applies to the specified local polarization and to observables with no external \(B\).

**The current measured by an ordered source.** The scattering observation at \(z+s\) determines the incoming polynomial frame label \((T(z+s)\xi)_+=\sum_e a_e(z+s)e\) for a current source at \(z\). This conversion follows by expressing \(d\operatorname{Res}_u\operatorname{tr}(\xi T)\) in the right Maurer–Cartan frame. Use the fixed incoming frame at both points and take the constant Laurent coefficient as \(s\) tends to zero. The resulting field is \(K_\xi=\sum_e:a_eL_e:\). The choice of this ordered, separated source fixes the contact subtraction.

There is a short intrinsic calculation for \(S\in\mathfrak{sl}_2\). Put \(f_S=\operatorname{tr}(SX)\), \(j=:\psi^q b_q:+:\psi^r b_r:\) and \(D=\partial_z\). On the orbit \(v_{Su}+\sum_e (XS)_e v_e=0\). Apply \(Q\) to \(\iota_{av}=:a\iota_v:\). The finite part of the ordered source is
\[
 K_{Su}=-\sum_e:(Q(XS)_e)\iota_{v_e}:
        = f_S j+D f_S .                                      \tag{2}
\]
For the second equality put \(a_e=(XS)_e\). The fermion matrix is \(-\sum_e v_e\otimes d a_e\), and contraction of \(\psi^i(z+s)b_j(z)\) leaves the one-form \(-\sum_{e,i}v_e^i D(\partial_i a_e)\) in its finite part. For \(E=E_{12}\) the only nonzero \(a_e\) are \(-rq\) and \(-rq^2\), paired with \(v_E=q^2\partial_q-2rq\partial_r\) and \(v_{E_{22}}=-q\partial_q+r\partial_r\). They give \(-rq^2 I\) and \(D(-rq^2)\). For \(F=E_{21}\) the two outputs are \(r I,Dr\), and for \(H=[E,F]\) they are \(-2rq I,-D(2rq)\). This proves (2) by linearity.

Write \(p=X_{21}=-rq^2\) and \(h=X_{22}-X_{11}=2rq\). For the constant label \(F=E_{21}\), the polynomial part of \(T(z+s)F\) is \(F\), so the ordered prescription gives \(K_F=L_F=-\beta_q\). Equation (2) gives \(K_{Eu}=p j+Dp\) and \(K_{Hu}=-h j-Dh\). The free propagator for this ordered pair now gives
\[
 K_{Eu}(z)L_F(w)\sim \frac{h(w)}{(z-w)^2}
                 -\frac{h(w)j(w)}{z-w}
       =\frac{h(w)}{(z-w)^2}+\frac{(K_{Hu}+Dh)(w)}{z-w}.       \tag{3}
\]
In particular the double pole comes from the \(Dp\) term on this two-dimensional chart. For the middle insertion \(L_E\) fix positive normal coordinates \(x=z_1-z_3,\ y=z_2-z_3\). Taking the \(x\,dx\) residue at \(x=0\) first and then the \(dy\) residue at \(y=0\) gives \(v_Eh=2p\). Taking \(y\) first yields \(L_H\) and then the double pole of \(K_{Eu}L_H\), also \(2p\). The \(12\)-first residue vanishes because \(K_{Eu}L_E\) is regular. The test \(x=(z_1-z_2)+y\) adds no pole in this channel. On the flux profile \(q=z,\ r=1\) the three nontrivial readings are \(2z,2,-2z^2\).

**Two sheets.** For the ordered transition \(T_1T_2\), cancellation of the intermediate frame gives \(M_{T_1T_2}=M_{T_2}M_{T_1}\). Couple a single incoming BF field to the two surfaces. The action on their two independent tangent multiplets is
\[
 V_\xi=\widehat v_\xi^{(1)}+\sum_j (M_{T_1}\xi)_j\,\widehat v_j^{(2)} .
\]
Here the second multiplet differentiates in its own orbit coordinates. The BF frame at the shared end depends on the first bosonic scattering observation. The identity
\[
 v_\xi(M\eta)-v_\eta(M\xi)+[M\xi,M\eta]=M[\xi,\eta]
\]
follows by differentiating \(M_T\xi=(T^{-1}\xi T)_+\). It gives \([V_\xi,V_\eta]=V_{[\xi,\eta]}\): the matter gauge BRST differential closes off shell with the cotangent action on both momenta, including the \(X\)-derivatives of the second action on the first momentum. The joint action is (1) with \(V_a\) in place of \(\widehat v_a\). Its Noether current is \(L_e^{(1)}+\sum_j(M_{T_1}e)_jL_j^{(2)}\), because the coefficients and currents of the second summand have regular mutual products. The ordinary outgoing connection equals \(M_Xa\) on shell. Off shell its gauge variation differs from that of a connection by \(-d_X(M_X\xi)(\bar\partial X-v_aX)\).

Apply the same ordered source to the measured product \(T_1(z+s)T_2(z+s)\). For a coefficient \(a\otimes b\) the finite part against \(L_e\otimes1\) has the extra term \(-v_e(a)\otimes Db\), from the pole of \(a(z+s)L_e(z)\) times \(b(z+s)=b+sDb+\cdots\). Against \(1\otimes L_e\) it has \(-Da\otimes v_e(b)\). Put \(X=T_1^{(1)},Y=T_2^{(1)}\), and \(K_{ij}(u)=\sum_{r\ge1}K_{E_{ji}u^{r-1}}u^{-r}\). The first mixed coefficient of the scattering observation is \(XY/u^2\). It multiplies a constant current in the \(u^{-3}\) coefficient of \(K\). After subtracting \(K_1T_2+T_1K_2\), the two finite parts give
\[
\begin{aligned}
 &-\sum_{k,l}E_{lk}\big([X,E_{kl}]DY+DX[Y,E_{kl}]\big)\\
 &\qquad=2X\,DY-\operatorname{tr}((DX)Y)I .
\end{aligned} \tag{4}
\]
Here \(\operatorname{tr}X=\operatorname{tr}DX=0\). For the two identical profiles \(X=Y=Q(z)=\left(\begin{smallmatrix}-z&1\\-z^2&z\end{smallmatrix}\right)\), the two matrix products are \(Q(DQ)=Q\) and \((DQ)Q=-Q\), where \(D=\partial_z\) at fixed \(u\). Thus \(\operatorname{tr}((DQ)Q)=-\operatorname{tr}Q=0\), and (4) gives \(+2Q\). On a disc about \(z=1\), the distinct Hecke profiles \(X=E_{12},Y=zE_{21}\), with the second profile in the \(Y_{21}\ne0\) chart, give \(2E_{11}\). In reverse order they give \(-I\). In this example \(D(XY)=E_{11}\), which also detects improvements invisible on the identical pair.

The choice of Fermi matter at the seam affects the result. Taking the tangent lift of the entire two-sheet space adds \(\sum_j (Q(M_{T_1}e)_j)\iota_j^{(2)}\) to the incoming current. For \(e=Su\), its action on the outgoing tangent coordinate in direction \(Z\) at \(X\) is \([Y,[S,Z]]\). At \(X=E_{12},Y=E_{21},S=E_{12},Z=H\) this is \(2H\). The two separate matter multiplets in (1) implement the actions on the vertical tangent and its quotient. The source at \(z+s\) and the current at \(z\) also have to use the same incoming frame when the constant Laurent coefficient in \(s\) is taken. This prescription fixes a derivative term which the classical action on \(X\) alone cannot measure. For instance \(K(u)\mapsto K(u)+\alpha u^{-1}DT(u)\) preserves the ordinary anchor and the one-form (4) by the Leibniz rule, but changes (3) to double coefficient \((1+\alpha)h\) and derivative correction \((1+\alpha)Dh\) relative to the shifted bracket current.

**Ordered stacks.** For \(n\) sheets put \(P_i=T_1\cdots T_i\), \(P_0=1\). The source coupled to sheet \(i\) is the incoming source transported by the actual prefix \(P_{i-1}\). The joint cotangent action (1) has invariant current
\[
 J_\xi^{[n]}=\sum_{i=1}^n\sum_e (M_{P_{i-1}}\xi)_e L_e^{(i)} .
 \tag{5}
\]
The incoming jet through order \(2n-1\) suffices, since each simple transition and its inverse have pole order one. The bracket of two currents in (5) has only a simple pole. For different slots only the earlier current can contract with the later coefficient. The resulting derivatives give the matched-pair identity above, and the actions on \(P_n\) telescope to \(P_nM_{P_n}\xi-\xi P_n\). These facts give off-shell gauge BRST closure and the same Gaussian quantization for every finite stack.

For any grouping into consecutive blocks \(P,R\), the two constant-mode contractions in (4) give the complete correction
\[
 -\sum_{m\ge0}\sum_{k,l=1}^2 u^{-m-1}E_{lk}
 \left((v_{E_{kl}u^m}P)\,DR+DP\,(v_{M_P(E_{kl}u^m)}R)\right).
 \tag{6}
\]
All coefficients are finite. Indeed \(M_{PR}=M_RM_P\) identifies the invariant current from either grouping with (5). The coordinate source in both orders is the constant coefficient of the same separated observable, with multiplier \((P_n(w+s)\xi)_+\) and current \(J^{[n]}(w)\). Thus the complete response, including normal derivatives, agrees in both parenthesizations. This identifies measured current operations on finite words of the prescribed defects. Compression to a single equivalent defect requires a map on its remaining matter observables.

This gives a perturbative realization of the marked measurements in a surface theory with specified matter, gauge polarization and sewing. The construction of these multiplets and this source from the unadorned five-dimensional defect remains open. The single-support meromorphic condition forces determinant one in the spectral fibre. The extra central loop coordinates of the full \(GL_2\) vertex algebra require further data. [Zeng, §5.6](https://arxiv.org/html/2610.10202v2#S5.SS6) · [Chiral de Rham complex](https://arxiv.org/abs/math/9803041)

**A Hecke surface for every simple gauge algebra**

Let \(G\) be a connected complex simple group and let \(X\) vary on the adjoint orbit of a highest long-root vector. One can insert the meromorphic transition \(T_X=\exp(X/u)\) in holomorphic-topological \(G\)-BF theory. In the root \(SL_2\), an upper unipotent matrix with entry \(1/u\) has elementary divisors \(u^{-1},u\). Its image in \(G\) is a Hecke modification of coweight \(\theta^\vee\), where \(\theta\) is the highest long root. In a local regular collar \(A=(X/u)d'\chi,\ B=0\) has this inverse transport for a holomorphic profile \(X(z)\) and a smooth step \(\chi\) supported in its transition region through \(d'\chi\).

The grading by \(\theta^\vee\), the coroot of the highest long root \(\theta\), is supported in degrees \(-2,\ldots,2\), with \(\mathfrak g_2=\mathbb C X\) in a root frame. Thus \(\operatorname{ad}_X^3=0\) and \([X,[X,\mathfrak g]]\subset\mathbb C X\). The regular part of \(\operatorname{Ad}_{T_X^{-1}}\xi\) is the frame reaching the next sheet. Its complementary strictly negative part gives the three possible incoming variations
\[
 v_C X=[X,C],\qquad v_{Su}X=-\tfrac12[X,[X,S]],\qquad
 v_{Su^k}X=0\quad(k\ge2).
\]
The middle vector is tangent because the coroot scales \(X\). On any smooth orbit chart put an even coordinate, an odd tangent field and their two conjugate momenta. Couple the cotangent action to the value and first holomorphic \(u\)-derivative of the incoming regular BF connection through the tangent lift of \(v\). In a word of \(n\) sheets each tangent multiplet transforms in its own orbit, with the ordinary frame parameter transported by the preceding scattering product. The adjoint exponential lowers the power of a frame label by at most two per sheet, so the incoming jet through order \(2n-1\) suffices. The graded cotangent Noether operators obey the zero-level current algebra on every orbit chart. The chiral de Rham coordinate changes identify them on overlaps.

In the regular-slab polarization with incoming tangential \(A\) fixed and outgoing tangential \(B\) zero, the bulk equations in axial gauge fix the tangential connection to its incoming value. At zero input, the framed, external-\(B\)-free observables have the Gaussian matter contractions. Their invariant current for \(\xi\) acts on the loop product by its dressing vector field. Separating a word into two consecutive blocks therefore gives Zeng's coproduct on all functions and invariant currents, hence on their vertex algebra. These are physical realizations in the specified theory with added tangent matter and framed sources. The numerical diagonal difference and the explicit two-matrix derivative are the separate \(GL_2\) measurements above.

The physical transitions reach every finite jet at spectral infinity locally in \(z\). With \(v=u^{-1}\), the vectors in the long-root orbit span \(\mathfrak g\), so products of \(\exp(vX)\) prescribe the coefficient of \(v\). A group commutator of words beginning in degrees \(i,j\) has leading coefficient the Lie bracket in degree \(i+j\). Since \([\mathfrak g,\mathfrak g]=\mathfrak g\), successive products correct every coefficient through a prescribed order. A holomorphic scalar multiple of an orbit vector which vanishes at the observation point can be split into two nonvanishing scalar multiples on a smaller disc. Thus one can use smooth sheets throughout. Combined with the independence of the cotangent moment symbols on sufficiently long words, these framed invariant-field measurements separate the algebraic states of the simple level-zero envelope. [Joint separation by Hecke sheets](#ch14-cotangent-faithful-sheets)

### How many sheets detect a cotangent current? {#ch14-cotangent-faithful-sheets}

On one rank-two Hecke sheet the scattering matrix is \(I+X/u\), with \(X^2=0\) and \(\operatorname{rank}X=1\). Its current for \(Su^2\) has zero dressing vector field. That same label can act on a second sheet. Conjugation by the first frame \(I+X/u\) sends \(Su^2\) to a polynomial whose lower coefficients include \(u[S,X]\) and \(-XSX\). Either can act where the initial quadratic label had zero vector field. More generally a word of sheets changes the polynomial label before it reaches each subsequent sheet. The resulting family detects every algebraic state of the level-zero chiral cotangent Yangian for \(\mathfrak{sl}_2\), using the momenta of the sheets themselves.

The algebraic construction works for every complex simple \(\mathfrak g\). Put \(v=u^{-1}\). Take \(X\) in the orbit of a highest long-root vector and use the loop \(\exp(vX)\). The grading by the coroot of the highest long root gives \(\operatorname{ad}_X^3=0\) and \([X,[X,\mathfrak g]]\subset\mathbb C X\). Thus constant labels act by conjugation, \(Su\) acts radially by \(-[X,[X,S]]/2\), and higher powers act by zero on a single orbit. On each smooth chart take the chiral de Rham coordinate, tangent Fermi field and their momenta. For an ordered word with partial products \(P_i\), pass \(M_{P_{i-1}}\xi=(\operatorname{Ad}_{P_{i-1}^{-1}}\xi)_+\) to its \(i\)-th sheet. The Fermi multiplets at adjacent sheets are independent. [Zeng, §§3.2 and 5.3](https://arxiv.org/html/2610.10202v2#S5.SS3) · [Chiral de Rham complex](https://arxiv.org/abs/math/9803041)

A finite collection of currents uses only polynomial frame labels of some degree at most \(d\). To separate their actions, put \(p=d+1\). Choose a regular element \(H\) of a Cartan subalgebra and let \(B\) be the sum of simple positive root vectors. An element commuting with \(H\) lies in the Cartan. If it also commutes with \(B\), every simple root vanishes on it, so it is zero. The two tests can be made on a single loop. At
\[
                 T_*=\exp(v^pH)\exp(v^{2p}B)
\]
the first \(p\) negative coefficients of \(\operatorname{Ad}_{T_*^{-1}}\sum_{j=0}^d\xi_jv^{-j}\) are \(-[H,\xi_j]\) in reverse order. If they vanish, the next \(p\) coefficients are \(-[B,\xi_j]\) in reverse order. Consequently the dressing vectors of all these labels are independent on a nonempty open set of loop jets.

That open set can be reached by products of smooth sheets. Take \(R\ge 2p+d\) so that the minor is defined modulo \(v^{R+1}\). In this jet group the sheet curves \(\exp(tvX)\) span \(v\mathfrak g\) in the Lie algebra they generate. Successive brackets give every \(v^j\mathfrak g\) up to \(j=R\). The closures of the word images are nested and irreducible, and successive multiplication by one sheet preserves any stabilized closure. Hence some finite word length dominates the whole jet group. On a dense open the product map is submersive, so finite \(z\)-jets of the coordinates lift as well.

For each incoming label \(\xi\) let \(V_\xi\) be the tuple of dressing vectors on the sheets. Its image under the derivative of multiplication is the dressing vector at the product. The above independence therefore holds already for the tuples. In the leading momentum symbol of the current, set the odd symbols to zero. The result is \(\langle\beta,V_\xi\rangle\), where \(\beta\) ranges over the entire cotangent space of the word. In the \(j\)-th vertex derivative its highest momentum jet contributes \(\langle D^j\beta,V_\xi\rangle\). After the lower jets are fixed, these pairings can take any values on the independent labels. Every nonzero finite current PBW polynomial, including its coordinate-jet coefficients, consequently survives on some word.

Cut a word after its first block. Loop multiplication gives the coproduct on functions and dressing gives it on currents. These generators determine every vertex product. An element of the algebraic tensor square involves only finite-dimensional subspaces in its two factors. On each such subspace the matrix coefficients of the separating sheet maps span its dual. Taking pairs of these coefficients detects the tensor, so the two-block measurements determine the full local vertex coproduct.

The required length can grow with the state. On a word of length \(m\) the adjoint scattering matrix is polynomial in \(v\) of degree at most \(2m\). Its coefficient of \(v^{2m+1}\) vanishes there, although it is nonzero on a loop \(\exp(v^{2m+1}X)\) for a highest-root vector \(X\). For \(GL_N\) the determinant-one sheets kill exactly the ideal generated by the scalar logarithmic loop coordinates and the scalar invariant-frame currents, including their translates.

For every simple group the root \(SL_2\) gives the Hecke modification whose coweight is the coroot of the highest long root. Its tangent matter couples to the value and first spectral derivative of the incoming gauge connection. With zero incoming tangential connection, zero outgoing tangential dual field, the marked ordered source and no external dual insertions, the framed BF slab yields the Gaussian surface fields used above. The jointly faithful realization holds in this engineered sector. For two highest-long-root sheets with residues \(X,Y\) at distinct supports \(a,b\), the two orders have isomorphic framed fields on \((a-b)^2\ne k_\theta(X,Y)\), where \(k_\theta(E_\theta,F_\theta)=1\). The isomorphism carries the separate tangent fields and intertwines the normally ordered currents. The gauge-invariant observables of the full unframed five-dimensional theory remain a separate comparison. [Exchange of separated Hecke sheets](#ch12-theorem-exchange-of-separated-hecke-sheets)

**Restoring the scalar currents by two fluxes**

The determinant-one Hecke sheets have no scalar loop coordinate. A different boundary condition supplies this coordinate and its independent current from the centre of the same \(GL_N\) BF field. Work at vertex level zero, on a coordinate disc, with the formal normal variable \(u\), and use the matrix trace pairing. For the \(\mathfrak{sl}_N\) summand use the framed regular slab with separate tangent Fermi matter, zero incoming tangential connection, zero outgoing tangential dual field and no external traceless dual insertions. Keep the incoming point-split current source fixed. In the scalar summand allow the polar modes of both BF fields on the normal tube, with regular exact modes divided out. Orient the linking sphere outward in \((t,\operatorname{Re}u,\operatorname{Im}u)\).

Set \(a=\operatorname{tr}A/N\), \(\widetilde b=\operatorname{tr}b\), where \(B=dz\,du\,b\) is the dual field in this chart. With traceless parts \(A_0,b_0\) the local BF density splits as
\[
 \operatorname{tr}\bigl(b F'(A)\bigr)
   =\operatorname{tr}\bigl(b_0 F'(A_0)\bigr)+\widetilde b\,d'a .
\]
Scalar frame changes act trivially on the Hecke orbit. The specified product polarization and the added surface action split between these summands. For every \(N\ge2\) the traceless sector has the framed highest-root-sheet action and independent tangent multiplets on each block. In the scalar polarization the two fluxes are
\[
 x_r=\frac{1}{2\pi i}\int_{S^2}u^{r-1}du\wedge a_\perp,\qquad
 j_m\,dz=\frac{dz}{2\pi i}\int_{S^2}u^mdu\wedge\widetilde b_\perp ,
 \quad r\ge1,\quad m\ge0 .
\]
The free abelian field gives them regular mutual products. Both fluxes add when the linking sphere is separated into its two oriented components, and every finite set of their tangential jets varies independently.

**Corollary.** For \(N\ge2\), the product boundary condition gives a jointly faithful realization of the full algebraic level-zero chiral cotangent Yangian of \(\mathfrak{gl}_N\) and its ordered local vertex coproduct in the marked field sector of this engineered theory. The scalar observation on a word can be taken on one enclosing tube. To cut the word, use a tube around each block.

*Proof.* Put \(X(u)=\sum_{r\ge1} x_r u^{-r}\). The scalar matrix factor is \(\exp X(u)\,I\), so for the complete coordinate loop the coefficient series is \(\log\det T=N X(u)\); the current labelled by \(Iu^m\) pairs with \(j_m\). Every coefficient of the exponential and its formal inverse is a polynomial in finitely many fluxes. At level zero the formal splitting
\[
 T=(\det T)^{1/N}\,T_{\mathrm{ss}},\qquad \det T_{\mathrm{ss}}=1
\]
splits the vertex envelope as the tensor product of its \(\mathfrak{sl}_N\) envelope and the commutative differential polynomial algebra of \(x_r,j_m\). The scalar logarithm has zero dressing derivative, and every scalar current is fixed by all preceding loops and has zero bracket with the traceless currents. The universal relations and the vertex PBW basis give both the tensor product and the corresponding product of coproducts.

The traceless word fields distinguish every finite algebraic state. The two flux towers distinguish every differential polynomial of the scalar factor. Tensor separation then proves joint faithfulness, including for mixed normal products and their derivatives. On a two-block cut the traceless observations compose by dressing, the \(j_m\) add, and the exponential of \(X\) multiplies. These are the defining coproducts on all generating fields, so the two-block measurement determines the full coproduct. The argument also applies coefficientwise to formal deformation coefficients when the field maps have been extended coefficientwise. ∎

The complete \(T\) in this statement is an observable formed from two boundary sectors. On a reduced compactified spectral fibre a single-support meromorphic scattering matrix regular and invertible elsewhere and normalized at infinity has determinant one. A general exponential of polar flux gives a formal loop at infinity; the proof does not give it a reduced single-support meromorphic representative. The marked observable subalgebra, including the independent flux of the dual BF field, is the scope of the realization. Identifying the entire unframed quantum BRST algebra, or deriving these boundary data from the proposed bare defect, remains open. [Zeng, §§3 and 5](https://arxiv.org/html/2610.10202v2) · [Elliott–Safronov–Williams, Theorem 9.3](https://arxiv.org/abs/2002.10517)

### Two fluxes on a meromorphic surface {#ch14-cotangent-central-flux}

The determinant part of the chiral cotangent Yangian has a local five-dimensional realization. Place a surface at \(t=u=0\) in \(\mathbb R_t\times\mathbb C_z\times\mathbb C_u\). For abelian holomorphic-topological BF theory the action in this chart is \(\int dz\,du\,b\wedge d'A\), with \(d'=d_t+\bar\partial_z+\bar\partial_u\). Both \(A\) and \(b\) are partial one-forms, defined modulo independent \(d'\)-exact shifts. The intrinsic cotangent field is \(B=dz\,du\,b\).

Allow finite meromorphic principal parts in the transverse variable. Viewed from opposite ends of the \(t\)-axis, the punctured normal tube gives two formal \(u\)-disks with a common punctured disk. Write \(O=\mathbb C[[u]]\), \(K=\mathbb C((u))\). The normal fields are resolved by \(O\oplus O\to K\), with differential \((f_-,f_+)\mapsto f_+-f_-\). The regular modes lie in degree zero and the principal parts \(K/O\) in degree one. On an outward sphere the BF pairing between a degree-zero cochain and \(h\in K\) is \(\operatorname{Res}_{u=0}(f_-+f_+)h\,du/2\). Indeed a cutoff interpolating between the two pole values has mean \(1/2\) against its own differential. The antidiagonal maps isomorphically onto the regular exact one-cochains. After removing this contractible pair, the regular modes of each field pair with the polar modes of the other. Choose the boundary condition retaining the polar modes of both fields. Its inverse image in the normal complex includes the antidiagonal gauge transformations.

For example a pure \(u^{-1}\) pole of \(A\) with coefficient \(f(z)\) contributes \(f(z)\) to the unweighted linking integral and zero to every positive moment. A pole of the dual field \(b\) can be varied while holding this reading fixed. The two sets of normalized measurements use the same small outward sphere,
\[
 a_r=\frac{1}{2\pi i}\int_{S^2}u^{r-1}du\wedge A,\qquad
 j_m\,dz=\frac{1}{2\pi i}\int_{S^2}u^m B,
 \qquad r\ge1,\quad m\ge0,
\]
Here \(dz\) is kept outside the second integral. Exact shifts integrate to zero. Let \(\chi\) rise from zero on the negative real half-axis to one on the positive half-axis and put \(d'_\perp=d_t+\bar\partial_u\). Test the first flux on \(A=f(z)u^{-k}d'_\perp\chi\), \(k\ge1\). The sphere integral reduces to the residue of \(f(z)u^{r-1-k}\,du\), so \(a_r\) reads \(f(z)\) exactly when \(r=k\) and reads zero otherwise. The second flux selects the coefficient of \(u^{-m-1}\) in the corresponding polar mode of \(b\). Either input can be varied with the other fixed.

These fluxes have regular quantum products. Equal species have no Gaussian contraction because the BF propagator pairs \(A\) with \(b\). A mixed contraction would be scalar. Rotating \(u\) gives it weight \(r+m>0\), whereas a scalar distribution in the \(z\) coordinates has weight zero. The normal reduction leaves the two polar towers in field degree zero with differential \(\bar\partial_z\). Their holomorphic jets are independent, and their Wick products give the polynomial differential algebra on those jets.

An outward sphere enclosing two successive sheets is homologous to the sum of their separate linking spheres. The equations \(d'A=d'b=0\) therefore give primitive coproducts on \(a_r\) and \(j_m\). The empty sphere has zero flux. Thus \(T(u)=\exp(\sum_{r\ge1}a_ru^{-r})\) multiplies across sheets, while \(L_{u^m}=j_m\) adds. This is the full zero-level \(GL_1\) vertex bialgebra. For \(GL_n\), traces give the primitive coefficients of \(\log\det T\) and the central currents \(L_{Iu^m}\). The determinant splits off using its formal \(n\)th root with constant term one. [Zeng, §§3.1 and 5.6](https://arxiv.org/html/2610.10202v2)

The same measurements glue near the zero section of mini-twistor space \(T\mathbb P^1\). Under \(z'=f(z)\), write \(u'=h(z)u\) for the fibre transition. The sphere has \(dz=0\), so \(a'_r=h^ra_r\) and \(j'_m\,dz'=h^mj_m\,dz\). In derivative tangent frames \(h=f'\), giving the two mini-twistor primary weights \(-r\) and \(1-m\). [Zeng, §4.3](https://arxiv.org/html/2610.10202v2#S4.SS3)

The traceless currents pose an additional problem even for a gauge supergroup with odd tangent fields. Write \(Y\) for the odd variation of the even holonomy \(T\). Ordinary parallel transport gives \(Y_{12}=Y_1T_2+T_1Y_2\). Let \(M_T\xi=(T^{-1}\xi T)_+\) denote the regular outgoing frame for the dressing current \(L_\xi\), where \(+\) retains nonnegative powers of \(u\). Varying that frame across the first sheet contributes \(v_{(dM_{T_1})(Y_1)\xi}(T_2)\) to the second odd holonomy, with \(v_\eta(T)=TM_T\eta-\eta T\). Two independently acting invariant currents in the vertex coproduct lack this term.

For \(E=E_{12}\), \(F=E_{21}\), take \(\xi=Eu\), \(T_1=I\), \(T_2=I+F/u\), \(Y_1=\varepsilon F/u\) and \(Y_2=0\), with \(\varepsilon\) odd. The variation of the seam frame is \(\varepsilon[E,F]\). Its action on the outgoing holonomy is \(\varepsilon[T_2,[E,F]]=2\varepsilon F/u\). The separate invariant currents instead give zero on the fused odd field, since \(F^2=0\). With ordinary tangent transport, endpoint-fixed gauge transformations and this gluing law, a current acting on the full superholonomy would need the additional seam term.

The right unit already obstructs a regular change to the odd gluing law on the full formal tangent group. Put \(s=u^{-1}\), take a square-zero even parameter \(\delta\) and an independent odd parameter \(\varepsilon\), and set
\[
 T_1=I,\quad Y_1=\varepsilon Fs,\qquad T_2=I+\delta Fs,\quad Y_2=0,
 \qquad E=E_{12},\quad F=E_{21}.
\]
The separate invariant currents for \(\xi=E/s\) fix both inputs. Indeed \(v_{E/s}(I+xFs)=x^2Fs\), whose derivative at \(x=0\) and whose value at \(x=\delta\) vanish. Keep the even product \(T=T_1T_2\). The right vacuum at \(\delta=0\) forces any regular odd output to have the form \(Y=\varepsilon Fs+\delta\varepsilon Z(s)\). For \(T=I+\sum X_rs^r\), the first coefficient of \(v_{E/s}(T)\) is \([X_2,E]+X_1[E,X_1]\). Differentiation along \(Y\) gives \(\delta\varepsilon([Z_2,E]+2F)\). Its \((2,1)\) entry is \(2\delta\varepsilon\) for every \(Z_2\). Thus no regular right-unital merger of the two odd holonomies intertwines the separate input currents with the tangent dressing current on the output. This obstruction assumes that the comparison acts on the odd observables as well as the even ones.

**The affine current in a transported end frame**

Place a Wess–Zumino–Witten field \(U\) at the end of a word of framed \(SL_2\) Hecke sheets. Its level \(b\) is the coefficient of \(\operatorname{tr}(XY)/(z-w)^2\) in the product of the currents labelled \(X,Y\). The sheets transport \(U\) to \(Y(u)=P(u)U\) in the incoming frame, where \(P\) is their ordered scattering product. Couple a fixed incoming source to the constant spectral coefficient \([u^0]\) of the ordinary left Wess–Zumino–Witten action with source. At zero source both \(P\) and \(P^{-1}\) have only nonpositive powers and constant term one. The kinetic and Wess–Zumino terms then have the ordinary action of \(U\) as their constant coefficient. The end field and the original surface multiplets have independent operator products at this preparation.

Write \(D=\partial_z\), \(j(U)=-b(DU)U^{-1}\), and \(j_X=\operatorname{tr}(Xj(U))\). A polynomial frame label \(\xi(u)\) measures
\[
 [u^0]\operatorname{tr}\bigl(\xi j(PU)\bigr)
 =j_{(P^{-1}\xi P)_0}
       -b[u^0]\operatorname{tr}\bigl(\xi(DP)P^{-1}\bigr).
\]
This follows by differentiating \(PU\). The coefficient \(b\) in the derivative term is also fixed by the affine Ward identity under a local change of frame. Functions of \(P\) have regular mutual products and contract trivially with the independent end current. For \(P=(1+xE_{12}/u)(1+yE_{21}/u)\) put \(H=[E_{12},E_{21}]\). The end current for \(Hu^2\) is \(2xyj_H-2b x\,Dy\). Reversing the sheets gives \(2xyj_H+2b y\,Dx\). On \(x=z,\ y=z^2\) the two derivative terms are \(-4bz^2\) and \(2bz^2\).

For end levels \(b_i\), add each such insertion to the original zero-level matter current using the actual prefix before that end. The right logarithmic derivative of \(PR\) is \(DP\,P^{-1}+\operatorname{Ad}_P(DR\,R^{-1})\). Since the constant coefficient of a product of two strictly negative series vanishes, a cut after \(P\) therefore acquires \(-b_{\mathrm{right}}[u^0]\operatorname{tr}(\xi DP\,P^{-1})\), with \(b_{\mathrm{right}}\) the sum of the levels to its right. This realizes the level-additive current on the marked fields of the dressed regular five-dimensional slab. The source is fixed at its measurement cap. Gauging that frame encounters the affine central term at evaluation level \(\sum_i b_i\). An off-shell nonabelian gauge coupling at an interior seam would also have to implement the field-dependent change of outgoing frame. [Witten, *Non-Abelian Bosonization in Two Dimensions*](https://doi.org/10.1007/BF01215276) · [Zeng, Theorem 5.9](https://arxiv.org/html/2610.10202v2#S5.SS4)

For \(GL_1\) the same polynomial level \(b f(0)g(0)\) admits two different wall preparations. In the abelian BF surface with polar boundary fields let \(a_m=(2\pi i)^{-1}\int_{S^2}u^{m-1}du\wedge A\) be the flux through the outward linking sphere, \(m\ge1\). Both walls have a constant chiral Chern–Simons mode at level \(b\). The double form \(b f_+(0)g_+(0)\) has only this block after quotienting its radical, and gives zero wall contribution for a source labelled \(u^m\). For \(b[u^0](fg)\) the modes \(u^m,u^{-m}\) form an additional abelian pair. Its three-dimensional action on an oriented interval times the \(z\)-disc is \(b(2\pi i)^{-1}\int C^-\wedge dC^+\). Fix \(C^+|_L=\mu\,d\bar z\) on the left and \(C^-|_R=0\) on the right. Identify the relative Wilson integral \(\int_L^R C^-_t\,dt\) with the preceding sheets' flux \(a_m\), keeping the minus gauge transformations based at both faces. For \(b\ne0\), variation of the plus field imposes \(dC^-=0\), so \(C^-_z(L)=-D a_m\). Varying \(\mu\) measures \(b C^-_z(L)=-bD a_m\). At zero source translation by the flat representative \(d((t-1)a_m)\) removes the flux from the wall integral. In addition to the common five-dimensional flux current, the two walls give \(0\) and \(-bDx\) on the same \(u^{-1}\) flux profile \(x(z)\) and the same \(u\)-current marking. At \(b=0\) the wall action vanishes, imposes no equation \(dC^-=0\), and contributes zero in both preparations. The undifferentiated Wilson-line matching and the choice of double form specify the additional three-dimensional junction.

### The two celestial jets and the cotangent Yangian {#ch14-celestial-cotangent-comparison}

The flat WZW\(_4\) current has two transverse jet indices. At a twistor line take the commuting colours \(T_{12},T_{34}\), where \(T_{ij}=E_{ij}-E_{ji}\) and \(K=-\mathrm{tr}_8/2\). Write \(J_{ij}=J_{T_{ij}}[0,0]\). The mixed first jets at \(0,z\) have the following open gauge contribution to their simple pole:

\[
 \frac{2\lambda}{z}
 \bigl(:J_{14}J_{23}:-:J_{13}J_{24}:\bigr).
\]

Here \(\lambda\) is the coupling for \(K\). These coefficients persist in the level-zero marked regular polynomial sector when the lower and mixed Ward operations are fixed and the crossed symbols survive independently. [The mixed-jet Ward identity](#ch14-celestial-yangian-like) · [Costello–Paquette, §7.3](https://arxiv.org/pdf/2201.02595v3#page=52)

In Zeng's chiral cotangent Yangian the dressing currents for \(p(u)T_{12}\) and \(q(u)T_{34}\) have zero simple pole for all polynomials \(p,q\). Could nonlinear fields represent the two jets? First evaluate functions of the negative loop at the identity, where the dressing action vanishes. The target is the universal affine vertex algebra \(V\) of \(\mathfrak{so}_8[u]\) at the same level. Next take \(V/C_2(V)\), where \(C_2(V)\) is the span of the states \(a_{(-2)}b\). In this quotient the normal product induces commutative multiplication, and the simple pole induces the Poisson bracket. Finally evaluate the polynomial variable \(u\) at \(s\). One obtains \(S(\mathfrak{so}_8)\) with its Lie–Poisson bracket, and each constant current \(J_{ij}\) goes to \(T_{ij}\). Any proposed assignment carrying the marked pole must still do so after these maps. [Zeng, (16), (21) and Corollary 2.8](https://arxiv.org/pdf/2610.10202v2)

Choose the Cartan of rotations in the four coordinate two-planes. Both incident colours \(T_{12}\) and \(T_{34}\) are fixed by this torus. In its invariant polynomials every linear term is a Cartan element and Poisson-commutes with every invariant. Constants have zero bracket, and the linear Cartan parts have zero bracket with every torus invariant. The remaining terms in both polynomials have degree at least two. Their Lie–Poisson bracket has degree at least \(2+2-1=3\), so it has no quadratic part. Whenever the complete source residue retains the displayed crossed projection after evaluation, no assignment of the two fields respecting this torus and zero-jet marking can preserve the simple pole, at any invariant target level.

The holomorphic BF model instead has two helicity towers and a mixed \(:J\widetilde J:\) pole. Zeng's proposed physical realization concerns a five-dimensional theory on \(\mathbb R\times\mathbb C_z\times\mathbb C_u\), where fusion along the real direction would induce the coproduct. The specified surface coupling realizes marked nonabelian current products on a framed Hecke orbit. Deriving its fields and seam conditions from the bulk path integral would give an intrinsic realization. [Costello–Paquette, §§7.3–7.4](https://arxiv.org/pdf/2201.02595v3#page=53) · [Zeng, introduction](https://arxiv.org/pdf/2610.10202v2#page=4)

[Ordered cuts of the chiral cotangent Yangian](#ch12-cotangent-yangian-cuts)

## A symplectic boundary and the next geometric comparison {#ch14-a-symplectic-boundary-and-the-next-geometric-comparison}

A zero-jet marking tested which currents could survive a proposed comparison of the twistor theories. Another necessary marking is the vacuum: a tensor equivalence must carry the tensor unit and hence its algebra of self-extensions. On a three-dimensional supersymmetric boundary we can compute this algebra and compare it with an explicit surface. Consider \(T[SU(2)]\), the three-dimensional \(\mathcal N=4\) theory with a \(U(1)\) gauge field and two hypermultiplets. Its holomorphic boundary contains two symplectic-boson pairs and two fermion pairs. In the Neveu–Schwarz vacuum their gauge currents \(J_b,J_f\) have levels \(-2,+2\), read from the double poles. Impose charge zero and the relative ghost condition \(b_0=0\), omitting \(c_0\). The residue \(Q=\operatorname{Res}c(J_b+J_f)\) squares to zero because the levels add to zero. Keeping only the bosonic current would give \(Q_b^2 b=-2\partial c\), which survives in the relative space. For each positive mode number the total current, its conjugate and the ghosts form a contractible quartet away from their common vacuum. The contraction is finite on each conformal weight. The cohomology is concentrated at ghost number zero. The identification of its vertex algebra with the simple \(L_1(\mathfrak{psl}(2|2))\) is the boundary-algebra result of Costello–Creutzig–Gaiotto. [Costello–Gaiotto](https://arxiv.org/abs/1804.06460) · [Costello–Creutzig–Gaiotto, §9.9.1](https://arxiv.org/abs/1811.03958)

Write \(\mathcal C_\rho^A,\mathcal C_{\rho^\vee}^B\) for the line categories of the two mirror presentations, with charge vectors \(\rho=(1,1)\), \(\rho^\vee=(1,-1)\). The first uses local lifts of finite-length symplectic-boson modules. The second uses local lifts of finite-length grading-restricted affine superalgebra modules and includes the simple-current extension by boundary monopoles. In either category \(\mathcal C\), take the vacuum to be its tensor unit \(\mathbf1\). Its Yoneda ring has degree-\(j\) space \(\operatorname{Hom}_{D^b(\mathcal C)}(\mathbf1,\mathbf1[j])\), with product given by splicing extensions. The two computations give the same graded algebra
\[
Z=\mathbb C[u,v,w]/(uv-w^2),
\qquad |u|=|v|=|w|=2.
\]
The braided equivalence identifies the two units. [Ballin–Creutzig–Dimofte–Niu, Definitions 8.10 and 8.21 and Theorem 8.32](https://arxiv.org/abs/2304.11001)

This ring has a geometric interpretation. Let \(g\in\mathbb C^\times\) act on \(T^*\mathbb C^2\) by \((x,y)\mapsto(gx,g^{-1}y)\), and set \(y(x)=0\). The products \(m_{ij}=x_i y_j\) form a trace-zero matrix of rank at most one. Its entries \(u=m_{12},\ v=-m_{21},\ w=m_{11}\) satisfy \(uv=w^2\) and generate the affine quotient ring. Positive stability requires \(x\ne0\). Write \(L=\mathbb Cx\). Since \(y(x)=0\), the map \(v\mapsto y(v)x\) kills \(L\) and has image in \(L\). It therefore defines an element of \(\operatorname{Hom}(\mathbb C^2/L,L)\). This space is dual, by the trace pairing, to the tangent space \(\operatorname{Hom}(L,\mathbb C^2/L)\) at \(L\in\mathbb P^1\). Rescaling \(x\) by \(g\) and \(y\) by \(g^{-1}\) preserves the line and its cotangent vector. The stable quotient is \(T^*\mathbb P^1\). Its zero section is contracted to the vertex of the affine cone.

At that vertex evaluation gives the augmentation \(Z\to\mathbb C\). Its ordinary derived endomorphisms \(\operatorname{RHom}_Z(\mathbb C,\mathbb C)\) are formal with model \(U(\mathfrak l)\), where \(\alpha,\beta,\gamma\) are odd of degree \(-1\), \(\tau\) is central of degree \(-2\), and
\[
[\alpha,\beta]=-\tau,
\qquad [\gamma,\gamma]=2\tau.
\]
It is free of rank eight over \(\mathbb C[\tau]\), and dualizing again recovers \(Z\) multiplicatively. Explicit operators on a hypersurface resolution establish the product, not merely the dimensions. This ordinary dual has no spectral parameter. [*The symplectic boundary model*, §9](#ref-ch14-14).

A proposed tensor functor must also preserve the vacuum. Put \(\mathfrak n_-=t^{-1}\mathfrak{psl}(2|2)[t^{-1}]\). Ordinary negative-current coinvariants \(\mathbb C\otimes^{\mathbf L}_{U(\mathfrak n_-)}M\) fail this test: on the boundary vacuum their first homology in conformal weight two is \(\mathbb C^{24|24}\), containing the cycle \(e_{-1}\otimes e_{-1}\mathbf1\) produced by the null square of an even current. Thus they cannot be a strong unital tensor functor to complexes. [The negative-current unit obstruction](#ref-ch14-14)

The vacuum extension ring gives the affine cone. Its resolution retains the projective line over the vertex, on which the framing torus has two fixed points. Under a generic one-parameter subgroup a generic line flows to one of them. Reversing the subgroup makes it flow to the other.

**Example (the two framing chambers).** On \(T^*\mathbb P^1\) the fixed points \(p_1,p_2\) are the coordinate lines. Give the two coordinates weights \(a_1,a_2\) and their cotangent partners weights \(\hbar-a_1,\hbar-a_2\). In this calculation \(u=a_1-a_2\) is the framing difference. The function called \(u\) on the affine cone was the matrix entry \(m_{12}\). A stable envelope extends a fixed-point class to equivariant cohomology with support in its attracting closure and diagonal value given by a signed Euler class. In the polarization with base tangent weights \((-u,u)\), these conditions and the off-diagonal degree bound determine the two chamber maps \(S_\pm\). Over \(\mathbb C(a_1,a_2,\hbar)\) both are invertible. Their change of basis, in fixed-point order \(p_1,p_2\), is
\[
 S_-^{-1}S_+=\frac{1}{u+\hbar}
 \begin{pmatrix}u&\hbar\\ \hbar&u\end{pmatrix}.
\]
For the one-vertex quiver with no arrows, the full carrier uses \(T^*\operatorname{Gr}(v,2)\) for \(v=0,1,2\). The extreme varieties are points. For a doublet with basis \(e_+,e_-\), put \(e_{ij}=e_i\otimes e_j\). Splitting the framing gives the ordered basis \(e_{++},e_{+-},e_{-+},e_{--}\) of the localized tensor square. The displayed block acts on the middle two vectors and the two extremes are fixed. Hence \(R(u)=(uI+\hbar P)/(u+\hbar)\), where \(P\) interchanges the doublets. The formula is regular for \(u+\hbar\ne0\). For \(\hbar\ne0\) the antisymmetric-to-symmetric eigenvalue ratio is \((u-\hbar)/(u+\hbar)\).

On the same doublet tensor space the two-point Knizhnik–Zamolodchikov equation is \(dG/dz=\lambda(P-\tfrac12 I)G/z\), where \(z\) is insertion separation and \(\lambda=(k+2)^{-1}\) at fixed affine level \(k\ne-2\). A counterclockwise half-turn without flipping the tensor labels gives ratio \(e^{-2\pi i\lambda}\), independent of \(z\). A scalar rescaling and a similarity of the same fibre preserve the eigenvalue ratio. They therefore cannot give the varying framing-weight ratio at generic \(u\). [*The symplectic boundary model*, §§5–6](#ref-ch14-14)

For a geometric Hall product or coproduct one must specify the correspondence among moduli spaces \(\mathcal M(r,n)\) of framed instantons at fixed positive stability. The framing rank \(r\) and the instanton number \(n\) are independent. In particular \(\mathcal M(1,1)=\mathbb C^2\) and \(\mathcal M(2,1)=\mathbb C^2\times T^*\mathbb P^1\). In these instanton spaces \(\mathbb C^2\) records the position of the charge-one instanton. The \(T^*\mathbb P^1\) factor belongs to the rank-two framing at that same charge. A length-two ideal on the D3 Hilbert scheme instead has framing rank one and charge two. For a Hall product there is still a choice even when both factors and the middle object have been specified. Fix two one-dimensional factors and take a two-dimensional vector space as the middle object. A subobject is a line in that plane. As it varies, the quotient stays one-dimensional. The correspondence in the next chapter sums over precisely these choices of subobject. Comparing it to boundary fusion requires identifying the components and the space of choices on both sides. [Hall multiplication by pullback and pushforward](#ch15-extensions-and-the-reason-for-associativity)

## Source manuscripts {#ch14-source-manuscripts}

### 1. The junction with its flux class {#ref-ch14-01}

Theorems 4–6 identify the fixed-flux cap \(\operatorname{Tor}^{U_N}_2(A_N,A_N)\to A_N\), its kernel \(\operatorname{Tor}^{U(\mathfrak g)}_2(A_N,A_N)\), and its bimodule splitting at every positive rank. For the action and the classification used in the proof, see Gaiotto–Oh, §§2.7–3.1, and Berest–Etingof–Ginzburg, Theorem 8.5. [Flux and derived composition](#ch14-theorem-the-flux-class-in-derived-particle-composition)

### 2. The integral relative curved model {#ref-ch14-02}

The integral comparison uses the full \(GL_N\)-invariant matrix complex over \(\mathbb C[\hbar]\) and the spherical corner of the group-relative curved cobar for \(1\le N\le3\). [Integral curved comparison](#ch14-theorem-integral-curved-comparison)

### 3. Non-formality of the brane algebra at rank four and at every rank, exactly {#ref-ch14-03}

Sections 3–6 compute the generic obstruction \([m_4]\) in the three-cycle sectors and its integral divisibility. The rank-three detector applies for \(N\ge3\). [The fourth multiplication in the full matrix complex](#ch14-the-matrix-complex-before-taking-cohomology)

### 4. Curved duality for symmetric Weyl particles {#ref-ch14-04}

The category theorem uses the cohomology algebra of Weyl particles with exterior partners at zero Cherednik parameter and numerical \(\hbar\ne0\). Equivariant coderived comodules and contraderived contramodules occur on its dual side. [The algebras in the comparison](#ch14-the-matrix-complex-before-taking-cohomology)

### 5. Polynomial Hamiltonian transport {#ref-ch14-05}

*Polynomial Hamiltonian transport*, §§1.5–1.7 and Lemma 12.1, specify the lower maps. Write \(z(f)=\operatorname{Tr}((\operatorname{Sym}f)\Psi)\). For \(u,v\) in the polynomial plane let \(p(t)=(1-t)u+tv\). The symmetric kernel \(B_h(f,g;u,v)\) is the sum of \(K_h(f,g;u,v)\) and \(K_h(f,g;v,u)\). To compute \(K_h\), write \(\Delta=\{0<s<t<1\}\) and \(P_{st}^{j}=P^j(f,g)(p(s);p(t))\), differentiating \(f\) in the first slot and \(g\) in the second. For positive odd integers \(r,k\), form the moments
\[
 I_{rk}=\int_\Delta s^k(1-t)^r P_{st}^{r+k+1}\,ds\,dt .
\]
Then the kernel in this order is
\[
 K_h(f,g;u,v)=
 \sum_{\substack{r,k\ge1\\ r,k\ {\rm odd}}}
 \frac{(h/2)^{r+k-2}}{r!\,k!}\, I_{rk}.
\]
The map \(\rho\) sends \(a(u)c(v)\) to the symmetrized product of \(J(a)\) with \(z(c)\). The binary correction lifts the class \(s_h=\tfrac h2\bigl(\nu z(\partial_{h^2}b_h)-\rho B_h\bigr)\). Theorem 12.6 supplies the finite-degree fifth map. Lemma 14.1 and Theorem 14.2 extend all arities through degree 24 with the first four components fixed. [The degree-24 theorem and its proof](#ch14-theorem-hamiltonian-transport-through-total-degree-24)

Theorem 13.5 gives the fifth-obstruction identity after multiplication by \(\nu\). *Universal arity-five obstruction*, §§5–8, constructs the polynomial primitive before specialization under the homology and ordered-symbol hypotheses. Its fourth component may change while the ternary map stays fixed. [The conditional arity-five theorem](#ch14-conditional-theorem-universal-arity-five-with-a-fixed-ternary-ma)

### 6. Global sections on the Hilbert scheme {#ref-ch14-06}

Theorems A–B identify the image of the polynomial operators. In §7, Lemma 7.2 detects the vacuum by chart modes, Lemma 7.6 supplies the invariant pairing, and Theorem 7.7 proves equality with the zero-mode kernel. Sections 23–25 concern the reduced rank-two torsion with its conformal and torus gradings. In §19, equation 19.3 gives the graded chart matrix and formula 19.16 gives the torus-finite specialization. The proof of [Relation weights in rank-two chiral cohomology](#ch14-rank-two-relation-weights) uses the filtration of that matrix. The first even-charge singlet in Theorems 23.3 and 24.2 attains the [bound on generator weights](#ch14-generator-weights-at-fixed-horizontal-spin). Theorem 19.3 describes the nonseparated kernel and the coordinatewise residue map. These coordinates and the weight projection of §19.4 enter the [proof of the torus-finite isomorphism](#ch14-proof-torus-finite-classes-and-separated-completion). The stable cyclic chart is that of Arakawa–Kuwabara–Möller, §2.3, and their §5.1 defines the finite-part specialization. [The image and its missing weight-zero section](#ch14-theorem-the-exact-chiral-image)

### 7. Global sections on the Hilbert scheme {#ref-ch14-07}

Sections 21–22 detect the cup products of determinant Bocksteins before specializing \(\hbar\). Their exterior degrees are sheaf-cohomological degrees. [The completed Hilbert-scheme sheaf](#ch14-d3-branes-chiral-operators-and-hilbert-scheme-sections)

### 8. Miura composition and surface fusion {#ref-ch14-08}

For the ordered Miura operator and rank splitting in normal generators, see equations 3.4 and 3.16 of Gaiotto, Rapčák and Zhou. Proposition 4.2.2 gives the ordered monomial basis. Weyl ordering is a triangular change of generators. Formal transposition identifies the Weyl fields for the given ordering at \(a\) with those for the reverse ordering at \(-a\). Reversal permutes independent currents of equal level and preserves their operator products. Uniqueness of expansion in the ordered monomial basis then gives parity of each scalar coefficient. [Gaiotto, Rapčák and Zhou, *Deformed double current algebras, matrix extended W-infinity algebras, coproducts, and intertwiners from the M2–M5 intersection*](https://arxiv.org/abs/2309.16929v3).

### 9. Higher current algebras and their induced modules {#ref-ch14-09}

Theorem 13.2 identifies the internally graded endomorphisms of the co-vacuum at zero central extension for finite-dimensional two-step nilpotent \(\mathfrak g\) and \(n=2,3\). [The polar action and the Chevalley resolution](#ch14-higher-currents-and-openclosed-coupling)

### 10. Higher current algebras and their induced modules {#ref-ch14-10}

Theorem 14.3 treats full algebraic Hom. Completion in positive ghost weight permits arbitrary ghost coefficients in each cohomological degree, with an ordinary enveloping-algebra element on each ghost monomial. [Full Hom on the punctured space](#ch14-higher-currents-and-openclosed-coupling)

### 11. Marked realization of the paired higher Heisenberg coalgebra {#ref-ch14-11}

The marked realization theorem compares the realization on compact smooth joint kernels with the paired free fields on \(\mathbb C^2\). Its quasi-isomorphism preserves the two linear field species, the level, translations, disjoint products and the vacuum. [Free fields and higher currents](#ch14-higher-currents-and-openclosed-coupling)

### 12. Currents on a surface and their cubic level {#ref-ch14-12}

For unshifted currents on an affine complex surface, the central target \(\Delta_{n*}\omega_X[1]\) and operation degree \(2-n\) allow a central component only at \(n=3\). Its value is a cocycle. [The cubic level and open–closed coupling](#ch14-higher-currents-and-openclosed-coupling)

### 13. Celestial current algebras {#ref-ch14-13}

Sections 4.6–4.8 construct the simultaneous gauge-current and ghost algebras in the four retained bidegrees, under the quartic trace identity, and the coupling modulo total translation. The self-dual gauge calculation uses both helicities. [The finite bidegree quotient](#ch14-higher-currents-and-openclosed-coupling) · [The axion Ward identity](#ch14-celestial-closed-ward)

### 14. The symplectic boundary model {#ref-ch14-14}

Theorems 3.1, 5.1, 8.1 and 9.2 concern the line-category vacuum extensions, the chamber matrix, the weight-two negative-current obstruction and the ordinary augmentation dual, respectively. For stable envelopes and the two-point matrix see Maulik–Okounkov, Theorem 3.3.4 and §4.1.2. [The affine cone and its resolution](#ch14-a-symplectic-boundary-and-the-next-geometric-comparison) · [Maulik–Okounkov](https://arxiv.org/abs/1211.1287)
