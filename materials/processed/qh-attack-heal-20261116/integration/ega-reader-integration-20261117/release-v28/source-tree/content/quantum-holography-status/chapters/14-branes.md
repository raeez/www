# Branes and open–closed operations

Suppose a line can end on a surface. Which operators can act where they meet, and what happens if a short interval between two such junctions is shrunk? The categories in the preceding chapter describe which sectors can propagate. To compose the junctions one also needs their spaces of operators, with the action from each side.

An M2 brane has a worldvolume with two spatial dimensions and one time dimension; an M5 brane has five spatial dimensions. Under the supersymmetric Omega deformation, directions along a brane can disappear from its support in the effective description. In the five-dimensional theory on \(\mathbb R\times\mathbb C^2\), the M2 degrees of freedom give a topological line and the M5 degrees of freedom a chiral surface. The bulk action is perturbative noncommutative Chern–Simons theory. Transverse derivatives of its gauge field couple to operators on the line. A line endpoint carries a module for the incident operators. At a crossing the two incident actions give a bimodule. [Gaiotto–Oh, *Aspects of Omega-deformed M-theory*, §§2.7–3.1](https://arxiv.org/html/1907.06495v2)

The fields on a brane form the open sector; a field that can be inserted away from the brane belongs to the closed sector. A square-zero supercharge gives differentials on these fields, and the Becchi–Rouet–Stora–Tyutin (BRST) differential implements gauge symmetry with ghost fields. On these complexes, composition can retain a relation among junction operators even if ordinary multiplication forgets it. In the particle model a degree-two class detects the flux of the line. Its proposed realization by integrating the fields on a physical interval requires an independently constructed interval action with both endpoints.

## What a joined interface remembers {#ch14-what-a-joined-interface-remembers}

Suppose an algebra map \(R\to A\) describes the action of bulk operators on a defect. Joining two copies along the \(R\)-side gives
\[
X=A\otimes_R^{\mathbf L}A,
\qquad
\mu:X\longrightarrow A.
\]
Here \(\otimes_R^{\mathbf L}\) means that one first resolves an \(R\)-module factor by projectives and then tensors the resolution with the other factor. The resulting differential remembers relations imposed at the common interface. The map \(\mu\) multiplies the two outer factors, which retain commuting left and right \(A\)-actions. With cohomological grading, \(H^{-i}(X)=\operatorname{Tor}_i^R(A,A)\). If \(R\to A\) is surjective, the ordinary tensor product is already \(A\). The question is whether the negative cohomology vanishes. Surjectivity alone says nothing about it.

Consider a five-dimensional algebra where the first discrepancy occurs in degree two. Take the quiver
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
The multiplication map forgets the degree-minus-two class. Even the first-order test misses it: the ideal \(I=Re_2R\) satisfies \(I^2=I\), and hence \(I/I^2=0\), as required by \(\operatorname{Tor}_1^R(A,A)\cong I/I^2\). A relation among the relations survives after the first conormal obstruction has vanished.

The algebraic particle model of the M2 coupling has exactly this separation between degrees one and two, although its algebras are infinite-dimensional. Fix a numerical \(\hbar\in\mathbb C^\times\), and set
\[
W_\hbar=\mathbb C\langle x,y\rangle/([x,y]-\hbar),
\qquad \mathfrak g=W_\hbar^{\mathrm{Lie}},
\qquad U_N=U(\mathfrak g)/(1_{\mathfrak g}-N).
\]
The symbol \(1_{\mathfrak g}\) is the central Lie-algebra element represented by the Weyl unit; it is distinct from the enveloping algebra's unit. At zero Cherednik deformation parameter, the \(N\)-particle algebra and coupling are
\[
A_N=(W_\hbar^{\otimes N})^{S_N},
\qquad
\phi_N:U_N\longrightarrow A_N,
\qquad J(f)\longmapsto\sum_{i=1}^N f(x_i,y_i).
\]
Symmetrized polynomials give Weyl symbols for \(f\). The equation \(J(1)=N\) records the flux seen by the line.

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

Both actions matter. A module can be projective on each side without being projective over \(A^e=A\otimes A^{\mathrm{op}}\). For example, the diagonal bimodule of \(A=\mathbb C[t]\) is free on either side, but over \(A^e=\mathbb C[t_L,t_R]\) it has resolution
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

The primitive comes from cyclic homology of the polynomial Weyl algebra. The normalized Hochschild chain \(u=\hbar^{-1}x[y]\) has \(bu=1\). Its Connes boundary \(Bu=\hbar^{-1}(1[x|y]-1[y|x])\) generates top Hochschild homology and survives in cyclic degree two. Thus the unit gives a nonzero ordinary cyclic degree-two class. Choose an algebraic cyclic two-cocycle \(\Phi\) on unnormalized chains with \(\Phi(1,1,1)=1\). Antisymmetrizing \(\Phi\) gives a closed Lie three-cochain on \(\mathfrak g\). For the chosen lift \(s:\mathfrak l\to\mathfrak g\), let \(P\) be its restriction to the three lifted inputs and put \(\beta(a)=\Phi(1,1,sa)\). The cyclic cocycle identity gives \(dP=\omega\wedge(\omega-d\beta)\). Hence \(H=P+\omega\wedge\beta\) satisfies \(dH=\omega\wedge\omega\). Contraction by \(H\) gives a bimodule homotopy for the two successive cap operations. At rank one, where the cap in degree two is an isomorphism, the component of the *outgoing cut* from degree four to two degree-two factors is zero. The higher Tor groups themselves are not determined by this identity.

This calculation places a real condition on a proposed physical junction. For *every* fixed spatial jet order \(L\), choose different odd \(d,e>L\). A trilinear primitive factoring through the order-\(L\) Taylor jet of each input would have zero differential on \(x^d,y^d,x^e,y^e\). Even after taking one bracket, two untouched inputs still have zero jets. Yet the marked square has value \(2c_dc_e\ne0\). The algebraic primitive can use arbitrarily high jets on polynomial inputs. An independent field theory would have to construct its two endpoint actions, preserve the cap and outgoing cut, and supply a contact homotopy in its own allowed space of distributions. Which jet orders and regularization it admits is a physical input.

## The matrix complex before taking cohomology {#ch14-the-matrix-complex-before-taking-cohomology}

The junction theorem concerns the even particle algebra. A BRST description also retains odd relation variables, and these affect the operations transferred to cohomology. Let \(R=\mathbb C[\hbar]\), now with \(\hbar\) formal but polynomial. For \(\mathfrak g_N=\mathfrak{gl}_N\), define
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
It is a square-zero derivation on the displayed invariant algebra. The effective complex \(K_N^{\mathrm{eff}}\) further quotients by \(\operatorname{Tr}\Psi\). The absolute BRST complex also includes positive-degree gauge ghosts. These operations produce different complexes.

Curvature is already forced by one Weyl pair. An augmentation \(W_\hbar\to\mathbb C\) at numerical \(\hbar\ne0\) would send \([x,y]=\hbar\) to \(0=\hbar\). The constant term in this relation must instead survive in the dual construction. For the matrix model it becomes a degree-two curvature element.

Here is the precise small relative dual. Put \(S=R[S_N]\). Let \(D_N\) be generated over this group algebra by exterior generators \(\xi_i,\eta_i\) of degree one and commuting generators \(u_i\) of degree two, which commute with the exterior algebra. Permutations act on the exterior indices, and the adjacent transposition \(s_i\) obeys
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
Put \(C=\bigoplus_{r\ge0}\operatorname{Hom}_{S-}((D_N)_r,S)\), with tensor-order-reversing coproduct and the opposite group base identified by \(\sigma\mapsto\sigma^{-1}\). Form the curved cobar algebra \(\Omega_S(C,w)\), where the curvature is the functional dual to \(w\). This is the tensor algebra on the shifted coalgebra generators, with differential incorporating both coproduct and curvature. Let \(e=\frac1{N!}\sum_{\sigma\in S_N}\sigma\).

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
The second superscript records its cohomological degree. The proof compares it with the negative cup square of the binary comparison class in the odd particle coefficients; three-cycle permutation sectors detect that square. The corresponding integral obstruction is divisible by \(\hbar^2\) but not by \(\hbar^3\). Thus neither the polynomial complex nor a nonzero numerical fibre can be replaced by its cohomology with only ordinary multiplication. For \(N=3,4\), this minimal model has only \(m_2,m_4\); an \(m_6\) is first possible at \(N=5\). These are [the full matrix nonformality and curved-dual theorems, §§3–6](#ref-ch14-03).

There is also a category theorem for the separate cohomology algebra
\(B_N=(W_\hbar^{\otimes N}\otimes\Lambda(\theta_1,\ldots,\theta_N))^{S_N}\)
at zero Cherednik parameter and fixed numerical \(\hbar\ne0\). The symmetric idempotent is full in the Weyl–exterior crossed product, so it gives a Morita equivalence on ordinary unbounded derived module categories. Its curved dual uses equivariant coderived comodules or contraderived contramodules, the localizations appropriate to that curved coalgebra; the comodule presentation imposes local nilpotence of the even dual variables. This theorem concerns \(B_N\). The fourth operation explains why applying it to \(K_N^{\mathrm{full}}\) requires the full curved comparison. [*Curved duality for symmetric Weyl particles*, main theorem](#ref-ch14-04).

The corresponding Hamiltonian action also has higher components. On \(L_h=\mathbb Q[x,y][h]\), put \(P=\partial_x\otimes\partial_y-\partial_y\otimes\partial_x\) and define
\[
f\star g=m\exp\left(\frac h2P\right)(f\otimes g),
\qquad b_h(f,g)=\frac{f\star g-g\star f}{h},
\]
where \(m\) is ordinary polynomial multiplication. The exponential terminates on polynomial inputs, and the commutator is divisible by \(h\). The map \(\Phi_1(f)=\operatorname{Tr}\operatorname{Sym}f\) extends into \(K_N^{\mathrm{eff}}\) through arity five at every positive rank, and through all arities when \(N\le4\), over \(\mathbb Q[h]\). Universally over \(\mathbb Q[\nu,h]\), all arities are established through total input degree 23; arity five also holds through degree 24. The all-degree fifth defect satisfies \(\nu E=\delta\zeta\), so specializing \(\nu=N>0\) divides only by a rational integer. Universal extension beyond this range remains a separate problem. [*Polynomial Hamiltonian transport*, §§12–13](#ref-ch14-05).

The coupling equation uses full Hom in each arity, an arity product, and the divided commutator. To use the ordinary associative Maurer–Cartan equation, replace the source bracket by \(hb_h\) and \(\Phi_n\) by \(h^{n-1}\Phi_n\). The necessity is visible on \(x,y\): the unscaled target commutator is \(hN\), whereas the image of \(b_h(x,y)=1\) is \(N\). This normalization matters when comparing with the line-defect coupling formalism of [Paquette–Williams, §§5–6](https://arxiv.org/abs/2110.10257).

## D3 branes: chiral operators and Hilbert-scheme sections {#ch14-d3-branes-chiral-operators-and-hilbert-scheme-sections}

A D3 stack has a four-dimensional worldvolume. Its \(\mathcal N=4\) gauge theory has a protected operator sector on a complex plane, whose products form a vertex algebra. The Hilbert scheme entering its description is a moduli space for an auxiliary Hamiltonian reduction, not the D3 worldvolume. The construction of [Arakawa–Kuwabara–Möller](https://arxiv.org/abs/2309.17308) connects this sector with a sheaf of vertex superalgebras on \(M_N=\operatorname{Hilb}^N(\mathbb C^2)\). The question is which global sections are represented by polynomial gauge-theory operators.

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
The relative complex is the intersection of the kernels of \((b_{ij})_{(0)}\) and \((Qb_{ij})_{(0)}\): equivalently, gauge-invariant polynomial creation states in which \(c\) occurs only through its derivatives. Write \(K_N=H^0(C_{\mathrm{fr}},Q)\). The stable bosonic moment reduction \(([X,Y]+\gamma\beta=0)^{\mathrm{st}}/GL_N\) is \(M_N\), where stability means that \(\gamma\) generates \(\mathbb C^N\) under \(X,Y\). Localizing the formal free fields there gives the BRST sheaf \(\mathcal D\). Put
\[
V_N=\Gamma(M_N,\mathcal D)_{\mathrm{fin}}/(\hbar-1).
\]
The subscript means the torus-finite part, taken before specialization. Homogenizing a polynomial operator, restricting to the stable locus and passing to the sheaf defines \(\alpha_N:K_N\to V_N\).

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
Here \(\mathrm{Sb}\) is the trace symplectic-boson pair, \(\mathrm{SF}\) the symplectic-fermion algebra, and \(bc\) the fermionic pair of weights \((1,0)\). The total unframed relative cohomology is \(K_N\) for \(\mathfrak{gl}_N\) and \(W_N\) for \(\mathfrak{sl}_N\), with ghost number matching framing fermion number. For \(N\ge2\), the traceless quadratic currents generate affine \(\mathfrak{sl}_2\) at level \(-(N^2-1)/2\); their zero modes give the Lie action used below. See [*Global sections on the Hilbert scheme*, Theorems A–B](#ref-ch14-06).

The missing section has a concrete construction. Where \(\gamma\) is cyclic for \(X\), form the matrix with columns \(\gamma,X\gamma,\ldots,X^{N-1}\gamma\). Replacing \(\gamma\) by \(\psi\) and multiplying by its inverse gives an odd matrix whose trace extends globally as \(\tau\). Its contraction with \(\chi^-\) proves that it cannot come from \(K_N\). A vacuum-detection argument on the cyclic chart identifies the entire kernel, rather than merely comparing characters. At rank one this becomes the familiar distinction between \(bc\) and the subalgebra generated by \(b,\partial c\): the undifferentiated weight-zero fermion is absent from the latter.

The formal geometry retains more information than \(V_N\). For every \(m\ge1\), both \(\mathcal D\) and \(\mathcal D/\hbar^m\mathcal D\) have nonzero sheaf cohomology exactly in degrees \(0,\ldots,N-1\). If \(R=\mathbb C[[\hbar]]\), the normal-cup subalgebra generated by the vacuum and translated determinant Bocksteins is
\[
\frac{R\otimes\Lambda(e_0,e_1,\ldots)}
{(\hbar e_r,\Lambda^{\ge N})}.
\]
Only finite sums and products occur. Each \(e_r\) has sheaf degree one, intrinsic even parity and conformal weight \(r+1\); the exterior sign comes from sheaf degree. Increasing products of fewer than \(N\) generators are nonzero and survive every finite quotient. They disappear after torus-finite specialization at \(\hbar=1\). A jet-to-differential-form map detects the products through powers of the tautological determinant's Chern class; a Hartogs–Leray argument makes the detector global. [*Global sections on the Hilbert scheme*, §§21–22](#ref-ch14-07).

The determinant subalgebra does not exhaust the higher cohomology. In rank two, remove the free spectator factors and decompose the full reduced torsion into \(\mathfrak{sl}_2\)-representations. Let \(r\) be the positive reduced fermion number, \(q\) the integer energy index and \(H\) the corresponding conformal weight. Put
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
The brackets give the torus degrees at which the generators are born. In the two-chart description the torsion intervals at flavour weight \(-1\) are \([0,3),\,2[0,2),\,[0,1),\,[1,2)\), before subtracting \(r/2\) from each birth. The weight \(-3\) part contributes \([0,3),[0,2)\) from the larger irreducibles. Their subtraction gives the three doublets displayed above, including the later doublet of length one. The uniform lower-spin families and the full specialization quotient remain open. The completed rank-two complex also has a nonzero infinitely \(\hbar\)-divisible class. A continuous boundary duality must retain this information. Comparing its derived endomorphisms with an independently defined Kodaira–Spencer bulk further requires a defect coupling and a map preserving the specified operations. [*Global sections on the Hilbert scheme*, §§23–25](#ref-ch14-06).

## Surface fusion and the Miura product {#ch14-surface-fusion-and-the-miura-product}

For the particle junction the common algebra labels the end over which one tensors. Combining two parallel M5 surfaces poses a different gluing question. A field on the fused surface should act on two independently prepared surface sectors; the algebra map would therefore run from the sum of their ranks to the tensor product of their field algebras. Algebraically, independent Heisenberg currents at common parameters \(a,k\) define the Miura operator
\[
L_N=(a\partial+J_1)\cdots(a\partial+J_N).
\]
Converting normal symbols to Weyl symbols by \(\exp(-a\partial_z\partial_p/2)\) turns operator composition into the Moyal product with \([p,z]_* =a\). Already two factors give
\[
(p+J_1)*(p+J_2)
=p^2+(J_1+J_2)p+J_1J_2
+\frac a2(\partial J_2-\partial J_1).
\]
The derivative term records the order of composition. Associativity gives a coassociative, vacuum-preserving rank-addition map from the universal Miura image at rank \(N_1+N_2\) to the tensor product at ranks \(N_1,N_2\). The coefficient algebra is even in \(a\), and after inverting \(k\) the central charge is \(N-N(N^2-1)a^2/k\). [*Miura composition and surface fusion*, §§3,8](#ref-ch14-08).

The five-dimensional fields give a signed test with the line and surface still separated. Orient time by increasing \(t\) and both complex planes by their complex orientations. Take positive Taylor couplings on the line and surface, use \(dz/(2\pi i)\) on the surface, and take the perturbative weight \(e^{+S/\hbar_{\mathrm b}}\), where \(\hbar_{\mathrm b}\) is the bulk loop parameter. Let \(y=w_{\rm line}-w_{\rm surface}\ne0\), let \(x\) denote the tangential position, \(e\) the line charge and \(j=W_0\) the surface current. For lower and upper heat times \(0<u<v\), integration along the time line and averaging the tangential polynomial against its Gaussian give the ordered inverse-Hessian pairing
\[
 B_{u,v}=-\frac{e\,j(x)}{4\pi^2 y}
           \left(e^{-|y|^2/v}-e^{-|y|^2/u}\right).
\]
Completing the square gives the connected contraction \(-\hbar_{\mathrm b} B_{u,v}\). As the heat cutoffs are removed the elementary pole is therefore \(+\hbar_{\mathrm b} e\,j(x)/(4\pi^2y)\). The \(n\)th surface jet applies \((-\partial_y)^n/n!\), producing \(y^{-n-1}\) from \(y^{-1}\). This is a calculation on separated supports.

The order of two surface collars can detect the same sign. Put \(\tau=\hbar_{\mathrm b}/(4\pi^2)\). With the elementary right action \(Y=a\partial_X\), level-one unit surfaces, and incoming magnetic strength \(q_i=\tau/c_{\mathrm M}\) for Moyal parameter \([z,w]_* =c_{\mathrm M}\ne0\), the order-odd response to the test \(f(z)=z^2/2\) is \(\tau(j_2[f']-j_1[f'])/2\). Here \(j_i[f']=\operatorname{Res}f'(z)j^{(i)}(z)dz\). On \(|0\rangle_1\otimes j^{(2)}_{-1}|0\rangle_2\), the current in the second factor returns the vacuum and the first contributes zero. The reading is \(+\tau/2\) times the vacuum. The spin-two Miura primary gives \(+a/2\) on the same marked vector, fixing \(a=\tau\) at this order and in these markings. The primary mixes the first two Weyl-symbol coefficients; its derivative term has the opposite sign to that of the second elementary Weyl coefficient. An independently prepared magnetic flux must be compared with the stated incoming strength.

A physical surface-fusion theorem would extend these separated calculations to coincident supports and identify the renormalized line, surface and mixed operations on their full domains. Reflection constrains a first-order deformation only under compatible defect quantization, Ward identities and uniqueness hypotheses. The algebraic Miura coproduct, the single connected tree, and the two-collar response specify coefficients and normalizations that an all-orders comparison must preserve.

## Higher currents and open–closed coupling {#ch14-higher-currents-and-openclosed-coupling}

On a Calabi–Yau threefold with holomorphic volume form \(\Omega\), holomorphic Chern–Simons theory has a \(\mathfrak g\)-valued \((0,1)\)-connection \(A\). An invariant nondegenerate pairing gives the classical action
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
Both \(P_n,N_n\) are actual Lie subalgebras, but their direct-sum comparison with \(L_n\) preserves complexes rather than mixed brackets.

At zero central extension, the co-vacuum is the induced module
\(W_n=U(L_n)\otimes^{\mathbf L}_{U(N_n)}\mathbb C\).
Assume \(\mathfrak g\) is finite-dimensional and two-step nilpotent:
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
All modes are retained, with algebraic sums and products. [*Higher current algebras and their induced modules*, Theorem 13.2](#ref-ch14-09).

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

The related celestial construction retains polynomial twistor-fibre degrees \(\{(0,0),(1,0),(0,1),(1,1)\}\), removing every state outside this set. Over \(\mathbb C[s]/(s^3)\), its quantum ghost differential and coupling modulo total translation exist under the stated cancellation of the quartic gauge-trace anomaly by the axion coupling. Extending this simultaneous boundary-and-ghost construction to all bidegrees in \(\{0,1,2\}^2\), and then to a smooth quantum module theory, remains an open problem. [*Celestial current algebras*, §§4.6–4.8](#ref-ch14-13).

## A symplectic boundary and the next geometric comparison {#ch14-a-symplectic-boundary-and-the-next-geometric-comparison}

For \(T[SU(2)]\), the three-dimensional \(\mathcal N=4\) theory with a \(U(1)\) gauge field and two hypermultiplets, a holomorphic boundary construction contains two symplectic-boson pairs and two fermion pairs. Their gauge currents \(J_b,J_f\) have levels \(-2,+2\). Thus \(Q=\operatorname{Res}c(J_b+J_f)\) squares to zero; omitting the fermionic current instead gives \(Q_b^2b=-2\partial c\), which survives in the relative complex. A quartet contraction computes the relative BRST cohomology in every conformal weight. The resulting vertex algebra is the simple \(L_1(\mathfrak{psl}(2|2))\), as in [Costello–Gaiotto](https://arxiv.org/abs/1804.06460) and [Costello–Creutzig–Gaiotto](https://arxiv.org/abs/1811.03958).

For vacuum self-Ext, use the line categories of [Ballin–Creutzig–Dimofte–Niu, Definitions 8.10 and 8.21](https://arxiv.org/abs/2304.11001), for charge vectors \(\rho=(1,1)\), \(\rho^\vee=(1,-1)\). These retain finite-length and grading restrictions, local simple-current lifts, and the boundary-monopole extension in the second category. In these categories the vacuum Yoneda ring is
\[
Z=\mathbb C[u,v,w]/(uv-w^2),
\qquad |u|=|v|=|w|=2.
\]

Its ordinary augmentation dual is a different algebra. It is formal with model \(U(\mathfrak l)\), where \(\alpha,\beta,\gamma\) are odd of degree \(-1\), \(\tau\) is central of degree \(-2\), and
\[
[\alpha,\beta]=-\tau,
\qquad [\gamma,\gamma]=2\tau.
\]
It is free of rank eight over \(\mathbb C[\tau]\), and dualizing again recovers \(Z\) multiplicatively. Explicit operators on a hypersurface resolution establish the product, not merely the dimensions. This ordinary dual has no spectral parameter. [*The symplectic boundary model*, §9](#ref-ch14-14).

A proposed tensor functor must also preserve the vacuum. Put \(\mathfrak n_-=t^{-1}\mathfrak{psl}(2|2)[t^{-1}]\). Ordinary negative-current coinvariants \(\mathbb C\otimes^{\mathbf L}_{U(\mathfrak n_-)}M\) fail this test: on the boundary vacuum their first homology in conformal weight two is \(\mathbb C^{24|24}\), containing the cycle \(e_{-1}\otimes e_{-1}\mathbf1\) produced by the null square of an even current. Thus they cannot be a strong unital tensor functor to complexes. On the geometric side, the specified stable-envelope comparison gives \(R(u)=(uI+\hbar P)/(u+\hbar)\), where \(u\) is the difference of framing weights, \(\hbar\) is the cotangent weight, \(P\) flips two factors, and \(u+\hbar\ne0\). For \(\hbar\ne0\), its channel ratio varies with \(u\); a fixed-level Knizhnik–Zamolodchikov half-turn ratio is constant. A scalar multiple and same-fibre similarity cannot identify those generic families. [*The symplectic boundary model*, §§4–8](#ref-ch14-14).

For a geometric Hall product or coproduct one must specify the correspondence among moduli spaces \(\mathcal M(r,n)\) of framed instantons at fixed positive stability. The framing rank \(r\) and the instanton number \(n\) are independent. In particular \(\mathcal M(1,1)=\mathbb C^2\) and \(\mathcal M(2,1)=\mathbb C^2\times T^*\mathbb P^1\). The \(T^*\mathbb P^1\) factor belongs to charge one with rank-two framing. Comparing a Hall correspondence with boundary fusion requires its pullback and pushforward on the prescribed rank and charge components.

## Source manuscripts {#ch14-source-manuscripts}

### 1. The junction with its flux class {#ref-ch14-01}

### 2. The integral relative curved model {#ref-ch14-02}

### 3. Non-formality of the brane algebra at rank four and at every rank, exactly {#ref-ch14-03}

### 4. Curved duality for symmetric Weyl particles {#ref-ch14-04}

### 5. Polynomial Hamiltonian transport {#ref-ch14-05}

### 6. Global sections on the Hilbert scheme {#ref-ch14-06}

### 7. Global sections on the Hilbert scheme {#ref-ch14-07}

### 8. Miura composition and surface fusion {#ref-ch14-08}

### 9. Higher current algebras and their induced modules {#ref-ch14-09}

### 10. Higher current algebras and their induced modules {#ref-ch14-10}

### 11. Marked realization of the paired higher Heisenberg coalgebra {#ref-ch14-11}

### 12. Currents on a surface and their cubic level {#ref-ch14-12}

### 13. Celestial current algebras {#ref-ch14-13}

### 14. The symplectic boundary model {#ref-ch14-14}
