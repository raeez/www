# Arithmetic traces and positivity

A trace formula compares two descriptions of the same functional. One description sums spectral contributions; the other is assembled from geometric or arithmetic operations. In statistical mechanics, a trace such as \(\operatorname{Tr}(e^{-tH})\) counts energy levels with multiplicity. In arithmetic, the explicit formula for the Riemann zeta function relates its zero divisor to prime powers and the real place. The analogy becomes a mathematical construction only when the spaces, operators and trace domains are defined independently of the spectral answer.

Several such arithmetic objects can be constructed. They retain integer summation, Fourier transform, full multiplicity jets and even a geometric realization of the complete explicit-formula trace. The stronger questions concern positivity and local operations: can the full functional arise from an ordinary positive star representation, and can its arithmetic operations be compared with local fields while preserving collisions, units and integral normal directions? A scalar trace identity answers neither question by itself.

## The complete arithmetic functional {#ch16-the-complete-arithmetic-functional}

Use logarithmic scale \(u=\log x\), so multiplication of positive scales becomes addition. For a test \(f\in C_c^\infty(\mathbb R)\), set
\[
\widehat f(z)=\int_{\mathbb R}f(u)e^{izu}\,du,
\qquad
H_f(s)=\int_{\mathbb R}f(u)e^{(s-1/2)u}\,du
=\widehat f(-i(s-1/2)).
\]
Convolution and involution are
\[
(f*g)(u)=\int f(t)g(u-t)\,dt,
\qquad f^*(u)=\overline{f(-u)}.
\]
The complete Weil functional, in this normalization, is
\[
\begin{aligned}
W(f)={}&H_f(0)+H_f(1)-f(0)\log\pi\\
&+\frac1{2\pi}\int_{\mathbb R}\widehat f(r)
\operatorname{Re}\psi(1/4+ir/2)\,dr\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(f(\log n)+f(-\log n)\bigr),
\end{aligned}
\tag{16.1}
\]
where \(\psi=\Gamma'/\Gamma\), \(\Lambda(p^k)=\log p\), and \(\Lambda(n)=0\) otherwise. The first two terms are the polar contributions, the integral is the real-place contribution, and the last sum contains both orientations of every prime power. For instance, the term at \(n=4\) has coefficient \(\log2/2\); it is not a second copy of the prime-\(2\) term. [The test algebra and its scalar functional][trace-foundations]

The completed zeta function
\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
is entire. Let \(\rho\) run through its zeros, with multiplicity \(m_\rho\), and write \(w_\rho=-i(\rho-1/2)\). The explicit formula identifies (16.1) with
\[
W(f)=\sum_\rho m_\rho\widehat f(w_\rho).
\tag{16.2}
\]
The decay of the transform and the zero-counting bound give convergence on the stated test class. Formula (16.1), however, can be defined without knowing any zero individually. This distinction is the starting point for a geometric trace construction.

Positivity concerns the quadratic form
\[
Q(g)=W(g*g^*).
\tag{16.3}
\]
Since \(\widehat{g*g^*}(z)=\widehat g(z)\overline{\widehat g(\bar z)}\), a real \(w_\rho\) contributes \(m_\rho|\widehat g(w_\rho)|^2\). A nonreal point does not contribute an absolute square. The Weil positivity criterion equates \(Q(g)\ge0\) for every compact smooth complex test with the Riemann hypothesis. Thus the all-test quantifier is part of the mathematical problem, not a harmless extension of a finite calculation.

## Multiplicity, nilpotence and two different pairings {#ch16-multiplicity-nilpotence-and-two-different-pairings}

Before constructing an infinite-dimensional arithmetic space, consider the finite algebra
\[
A_m=\mathbb C[z]/(z^m).
\]
For \(a=a_0+a_1z+\cdots+a_{m-1}z^{m-1}\), multiplication \(M_a\) is triangular in the monomial basis, with diagonal \(a_0\). Hence
\[
\operatorname{Tr}M_a=ma_0,
\qquad
B_{\mathrm{tr}}(a,b)=\operatorname{Tr}M_{ab}=ma_0b_0.
\]
The trace counts the length \(m\), but its associated pairing has radical \((z)\). All nilpotent directions disappear from that pairing.

The residue functional gives a different answer:
\[
\operatorname{res}(a)=[z^{m-1}]a,
\qquad
B_{\mathrm{res}}(a,b)=[z^{m-1}](ab).
\]
For \(m=3\), the two pairing matrices in \(1,z,z^2\) are
\[
B_{\mathrm{tr}}=
\begin{pmatrix}3&0&0\\0&0&0\\0&0&0\end{pmatrix},
\qquad
B_{\mathrm{res}}=
\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}.
\tag{16.4}
\]
The residue matrix has determinant \(-1\), so it is perfect. It is a complex-bilinear duality, not a positive Hermitian inner product. Already over the real subalgebra,
\(B_{\mathrm{res}}(1-z^2,1-z^2)=-2\).

If \(N=M_z\) and \(A=\rho I+N\), then
\[
e^{tA}=e^{t\rho}\sum_{j=0}^{m-1}\frac{t^jN^j}{j!},
\qquad \operatorname{Tr}(e^{tA})=me^{t\rho}.
\]
The trace retains multiplicity but does not determine the Jordan chain. Nor does putting weight \(m\) on one point of a measure space create \(m\) independent operator-trace coordinates. These elementary distinctions recur in the arithmetic complex: a full zero divisor, a perfect residue dual and a positive Hilbert representation encode different information.

There is also a sharp conditional constraint. If a Hilbert-space generator satisfies \(A^*=1-A\) on its full equal adjoint domain, then \(A-\tfrac12\) is skew-adjoint. Its spectral values lie on the imaginary axis, and no nontrivial finite Jordan chain can lie in that domain. Such an adjoint identity would therefore impose both a critical-line condition and a restriction on nilpotent jets. A continuous duality alone does not supply it. [Integer-summation middle complex, duality and primary blocks][integer-complex]

## Integer summation defines the complex before its spectrum {#ch16-integer-summation-defines-the-complex-before-its-spectrum}

Let \(S=\mathscr S(\mathbb R)^{\mathrm{even}}\), and impose the two Poisson boundary conditions
\[
S_{00}=\{\phi\in S:\phi(0)=0,\ \int_{\mathbb R}\phi=0\}.
\]
For \(n\ge2\), define
\[
E_n=\{f:e^{n\langle x\rangle}f\in H^n(\mathbb R)\},
\qquad E=\bigcap_{n\ge2}E_n,
\qquad \langle x\rangle=(1+x^2)^{1/2},
\]
with its projective-limit Fréchet topology. Equivalently, the derivatives of an element of \(E\) decrease faster than every exponential at both ends. The arithmetic complex is
\[
C_{\mathbb Z}=[S_{00}\xrightarrow{Z}E],
\qquad (Z\phi)(x)=2\sum_{m\ge1}\phi(me^x),
\tag{16.5}
\]
in cohomological degrees zero and one.

Why do these two boundary conditions occur? For the Fourier transform
\(\mathcal F\phi(v)=\int\phi(u)e^{-2\pi iuv}\,du\), Poisson summation gives
\[
Z\phi(x)=e^{-x}Z\mathcal F\phi(-x)
+e^{-x}\int\phi-\phi(0).
\tag{16.6}
\]
Schwartz decay controls \(+\infty\); (16.6) controls \(-\infty\) once the two displayed boundary terms vanish. The two excluded functionals themselves form the polar lines, with dilation characters zero and one. They have not been inserted from a list of zeros.

To define the adelic averaging, let \(\mathbb A_{\mathbb Q}\) be the adele ring and \(C_{\mathbb Q}=\mathbb A_{\mathbb Q}^{\times}/\mathbb Q^{\times}\) its idele class group. The modulus \(|c|\) is the product of the normalized local absolute values. Its kernel \(C^1\) is compact; over \(\mathbb Q\), it identifies with \(\widehat{\mathbb Z}^{\times}\), where \(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\). Give \(C^1\) Haar measure of mass one and put
\[
(PF)(c)=\int_{C^1}F(kc)\,dk,
\qquad
(\Sigma\Phi)(c)=\sum_{q\in\mathbb Q^{\times}}\Phi(qc).
\]
Here \(\Phi\) is an adelic Schwartz–Bruhat test: Schwartz at the real place and locally constant with compact support at the finite places. Impose \(\Phi(0)=\int_{\mathbb A_{\mathbb Q}}\Phi=0\), with finite additive volume \(\operatorname{vol}(\widehat{\mathbb Z})=1\). For \(\Phi=\phi\otimes1_{\widehat{\mathbb Z}}\), finite-place integrality selects exactly the nonzero integers, and \((P\Sigma\Phi)(e^x)=Z\phi(x)\). This is the averaging map in the following theorem.

**Theorem (continuous integer-summation duality).** The map \(Z\) is a closed topological embedding. Its quotient \(M=E/Z(S_{00})\) is complete and nuclear. Norm-one adelic averaging identifies the actual averaged pole-free lattice-summation image with \(Z(S_{00})\). Under the Mellin transform, that image is exactly the ideal of functions vanishing at every zero of \(\xi\) to its full multiplicity. At each weighted Sobolev stage, the annihilator is the norm closure of the full dualizing-jet functionals at the same stage. Their inductive limit gives the strong continuous dual. Evaluation yields a nondegenerate hypocontinuous pairing: continuity is uniform when either argument ranges over a bounded set. It extends through the specified tensor completion formed using bounded sets. [An integer-summation middle complex and its continuous dual][integer-complex]

The first step of the proof is arithmetic inversion, after removing the factor of two in \(Z\). On logarithmic weighted spaces with exponent \(\sigma>1\), the operators
\[
\sum_{m\ge1}\lambda_{-\log m},
\qquad
\sum_{m\ge1}\mu(m)\lambda_{-\log m}
\]
converge in operator norm and are inverse; \(\mu(m)\) is the Möbius function and \(\lambda_t\phi(u)=\phi(e^{-t}u)\). Fourier reflection then controls both ends and gives inverse continuity in Schwartz seminorms. This proves closed range before spectral synthesis is used.

For \(\operatorname{Re}s>1\), Mellin transformation gives \(\mathcal M(Z\phi)(s)=2\zeta(s)\int_0^\infty\phi(u)u^s\,du/u\). An explicitly differentiated Gaussian supplies an arithmetic convolution generator with Mellin transform \(\xi(s)\). Quantitative division on vertical strips, followed by Gaussian regularization, proves equality with the full vanishing ideal. The dual jet functionals are therefore genuine continuous functionals on the arithmetic quotient; no simplicity assumption removes their higher derivatives.

The dual is complex-linear. To compare dilation characters, its contragredient action is tensored with the character \(e^t\): an exponent \(\rho\) becomes \(1-\rho\). This weight-one twist explains the reflection symmetry without turning the pairing into a positive inner product. The finite example (16.4) warns precisely against that inference.

## A geometric construction of the full trace {#ch16-a-geometric-construction-of-the-full-trace}

For trace-class operators one needs explicit Hilbert domains. Fix \(a>1/2\), and use the convolution algebra
\[
\mathcal A_a=
\left\{f\in C^\infty(\mathbb R):
p_{a,N}(f)=\sum_{j=0}^N\int e^{a|u|}|f^{(j)}(u)|\,du<\infty
\text{ for every }N\right\}.
\]
It is a complete nonunital Fréchet star algebra. Its Fourier transforms are holomorphic in \(|\operatorname{Im}z|<a\); on smaller strips they decrease faster than every power in the real direction. Compact smooth tests are dense. The identity for convolution would be the Dirac distribution, which is outside this function algebra.

The arithmetic relation ideal in this test algebra is defined by normalized theta summation:
\[
\theta_v(u)=e^{u/2}\sum_{n\ge1}v(ne^u)
=\tfrac12e^{u/2}(Zv)(u),\qquad v\in S_{00},
\qquad
\mathcal J_a=
\overline{\{\theta_v:v\in S_{00}\}}^{\,\mathcal A_a}.
\]
Poisson summation and the decay conditions place every \(\theta_v\) in \(\mathcal A_a\); its closed image span is a convolution star ideal. Thus \(\mathcal A_a/\mathcal J_a\) is the quotient by specified arithmetic relations, with its Hausdorff quotient topology.

Choose \(1/2<s<\min(a,1)\). The theta construction uses the Hilbert completion of even Schwartz functions in the norm
\[
\|v\|_{\mathscr V_s}^2
=\int_0^\infty x^{2s}
\bigl(|v(x)|^2+|\mathcal Fv(x)|^2\bigr)\,dx.
\tag{16.7}
\]
Both boundary values \(v(0)\) and \(\mathcal Fv(0)\) are continuous because \(s>1/2\). In logarithmic coordinates, combine the weighted spaces \(L^2(e^{2su}du)\) and \(L^2(e^{-2su}du)\). The diagonal image and the paired theta/Fourier image are closed; their difference, by Poisson summation, spans exactly the two polar characters. This produces a two-term Hilbert complex
\(\mathscr C_s=[V\xrightarrow d U]\) in degrees \(-1,0\), with \(d\) bounded below, and theta quotient \(K_s=U/dV\).

Convolution acts strictly on the complex by \(\rho_f\). Choose a nonnegative even smooth bump \(b\), supported in \([-1,1]\), with integral one, and put \(\phi(u)=\int_{-\infty}^u b(v)\,dv\). A bounded smoothing homotopy \(H_f\), constructed using this cutoff, gives
\[
\Lambda_f=\rho_f-\delta H_f,
\qquad \delta T=dT-(-1)^{|T|}Td.
\]
Each diagonal component of \(\Lambda_f\) is trace class.

**Theorem (geometric theta trace).** For every \(f\in\mathcal A_a\), the induced quotient operator \(\Pi_{s,a}(f)\) satisfies
\[
\operatorname{Tr}_{K_s}\Pi_{s,a}(f)
=\operatorname{Str}_{\mathscr C_s}\Lambda_f=W(f),
\qquad
\|\Pi_{s,a}(f)\|_1\le C_{a,s,\phi}p_{a,4}(f).
\tag{16.8}
\]
Here \(\phi\) is the fixed smoothing cutoff, and the supertrace is the degree-zero trace minus the degree-minus-one trace. [A common Hilbert theta complex, geometric full trace][theta-complex]

The prime-power operators and the real-place Fourier defect are constructed before their traces are evaluated. The two-dimensional polar quotient contributes both polar terms. Trace-class cyclicity and the closed-image decompositions then give (16.8). No spectral expansion is used to define this complex or prove its complete trace formula.

Thus the complete arithmetic trace already has a geometric operator construction. The inherited quotient norm does not make its convolution action an ordinary star representation. Establishing that additional adjoint relation on a suitable domain is a further mathematical problem.

## The trace domain and its coherent multiplication {#ch16-the-trace-domain-and-its-coherent-multiplication}

The identity on an infinite-dimensional Hilbert space is not trace class. One should therefore expect a proper trace ideal, rather than a finite trace on every bounded operator. For \(\mathscr C_s=[V\to U]\), put
\[
\begin{aligned}
\mathfrak I^0&=\{(T^{-1},T^0)\in\mathfrak S_1(V)\oplus\mathfrak S_1(U):
dT^{-1}=T^0d\},\\
\mathfrak I^{-1}&=\mathfrak S_1(U,V).
\end{aligned}
\]
Here \(\mathfrak S_1\) denotes trace-class operators. Composition and \(\delta\) make \(\mathfrak I\) a complete proper nonunital differential ideal of the bounded chain endomorphisms. Its closed graded trace is
\[
\tau(T)=\operatorname{Tr}_UT^0-\operatorname{Tr}_VT^{-1},
\qquad \tau(\delta K)=0.
\]
The last identity follows from \(\operatorname{Tr}(dK)=\operatorname{Tr}(Kd)\). Orthogonal splitting of the closed range of \(d\) contracts this ideal onto \(\mathfrak S_1(K_s)\) by a split differential-algebra quasi-isomorphism. The chain-map equation involves \(d\), whereas taking ordinary Hilbert adjoints involves \(d^*\); a positive differential-star structure does not follow. [Trace-class coefficient homotopies][trace-operations]

The trace-class representatives multiply up to an actual trace-class homotopy:
\[
\Lambda_f\Lambda_g-\Lambda_{f*g}=\delta K(f,g).
\tag{16.9}
\]
The homotopy is obtained by applying the bounded inverse of \(d\) on its closed range to the degree-zero defect. It also satisfies
\[
\Lambda_fK(g,h)-K(f,g)\Lambda_h
+K(f,g*h)-K(f*g,h)=0.
\tag{16.10}
\]
Products of two degree-minus-one homotopies vanish. Equations (16.9)–(16.10), with their mixed-degree versions, assemble into a coalgebra chain map on the bar construction. On a word, it sums over partitions into consecutive blocks of size one or two, applying \(\Lambda\) to a singleton and \(K\) to a pair. The triple identity is exactly the equality needed when a bar differential joins adjacent entries.

This also has an analytic completion theorem. Using the arithmetic ideal \(\mathcal J_a\) defined above, form the coefficient complex \(\mathcal E=[\mathcal J_a\to\mathcal A_a]\) in degrees \(-1,0\). Its degree-zero multiplication and action on \(\mathcal J_a\) are convolution; products of two degree-minus-one terms are zero. On tensor words use the completed projective seminorms
\[
P_{R,N}(x)=\sum_{n\ge0}R^nq_{N,\pi}(x_n),\qquad R>0,
\]
where \(q_N\) is the sum of the two coefficient seminorms. In this nonfactorial entire completion, the bar map is continuous with radius bound
\[
P_R^{\mathfrak I}(Gx)\le P_{C_1R+\sqrt{C_2R},4}(x).
\]
The estimate counts the same singleton/pair partitions. It extends the actual identities, not just a scalar trace, through the specified completion.

Locality asks for different structure. A supported coefficient can carry derivatives normal to a collision locus; a derived diagonal product also retains the classes measuring nontransverse intersection. Supported mapping complexes, such normal-jet sheaves, Gaussian preparation and completed finite-word comparisons are available. Their linking construction supplies a cyclic vector and nonlocal creation fields. It does not turn the linking algebra into a local field algebra.

A finite matrix calculation makes two boundaries visible. On \(K\oplus\mathbb C\Omega\), extend an original operator by \(T\oplus0\). Then
\[
\operatorname{Tr}(T\oplus0)=\operatorname{Tr}T,
\qquad \langle\Omega,(T\oplus0)\Omega\rangle=0.
\]
Rank-one maps \(c(v)=|v\rangle\langle\Omega|\) and \(a(w)=|\Omega\rangle\langle w|\) can make \(\Omega\) cyclic, but
\[
[a(w),c(v)]=\langle w,v\rangle P_\Omega-|v\rangle\langle w|
\]
is generally nonzero. For constant fields, multiplying this commutator by any power of \(z-w\) does not make it vanish. Cyclicity is not locality, and a cyclic vector state is not the counting trace. In the arithmetic linking construction, the original trace remains on the corner that annihilates the added invariant vector. [Invariant vacuum and linking fields][linking-fields]

## A positive representation and its exact missing remainder {#ch16-a-positive-representation-and-its-exact-missing-remainder}

There is nevertheless an ordinary positive representation on the critical part of the divisor. Differences of polynomially weighted quotient traces define positive functionals
\[
\sigma_n(f)=\sum_{\substack{\gamma\in\mathbb R\\m_\gamma\ge n}}
\widehat f(\gamma),\qquad n\ge1.
\]
Here \(\gamma\) ranges over the real centered zeros and \(m_\gamma\) is their multiplicity. Complete the test algebra modulo the null space of
\(\sigma_n(f^**g)\), and call the resulting Hilbert space \(G_n\). The direct sum \(G_{\mathrm{crit}}=\bigoplus_nG_n\) carries a continuous ordinary star representation
\[
\pi_{\mathrm{crit}}:\mathcal A_a/\mathcal J_a\longrightarrow\mathfrak S_1(G_{\mathrm{crit}}),
\]
with
\[
\operatorname{Tr}\pi_{\mathrm{crit}}(f)
=\sum_{\gamma\in\mathbb R}m_\gamma\widehat f(\gamma).
\tag{16.11}
\]
A zero of multiplicity \(m\) occurs in exactly \(m\) layers. This is how multiplicity becomes ordinary trace multiplicity, rather than merely a scalar measure weight. The generator is self-adjoint on its declared weighted square-summability domain, and inverse moments of order at least two converge. [Polynomial quotients, positive multiplicity layers][positive-layers]

The difference from (16.8) is explicit:
\[
W(f)-\operatorname{Tr}\pi_{\mathrm{crit}}(f)
=\sum_{w_\rho\notin\mathbb R}m_\rho\widehat f(w_\rho).
\tag{16.12}
\]
Isolation of a nonreal spectral point shows that this remainder vanishes on every test exactly when all centered zeros are real. The positive construction does not prove that vanishing. Its estimates on products of test operators likewise do not create local collision maps.

::: figure fig-programme-context-arithmetic

::: figure fig-weil-trace-remainder

## What integral arithmetic points forget {#ch16-what-integral-arithmetic-points-forget}

Integral arithmetic has an analogous loss of information under scalar evaluation. Fix a prime \(p\), including two. A delta structure is encoded by a Frobenius lift \(\varphi\) through
\(\delta(x)=(\varphi(x)-x^p)/p\). On \(\mathbb Z_p\), take \(\varphi=\mathrm{id}\). At positive finite height \(h\ge1\), put
\[
A_h=\mathbb Z_p[x_0,\ldots,x_{h-1}],\quad
R_h=\varprojlim_nA_h/p^n,\quad
I_h=(p,x_i^p-x_i:i<h),\quad
B_h=\varprojlim_nA_h/I_h^n.
\]
The last ring is the formal completion along the finite-field rational locus, defined independently of any comparison image. For each \(c\in\mathbb F_p^h\), choose the integer representatives \(0\le c_i<p\) in \(\mathbb Z_p\). With these lifts, Chinese remainders give
\[
B_h\simeq\prod_{c\in\mathbb F_p^h}\mathbb Z_p[[z_0,\ldots,z_{h-1}]],
\qquad x_i=c_i+z_i.
\tag{16.13}
\]
The natural \(j_h:R_h\to B_h\) is injective, also modulo every \(p^n\): translation by \(c\) is a polynomial automorphism, and polynomials inject into formal power series over the finite coefficient ring.

Frobenius has the variance
\[
\varphi_h:R_h\longrightarrow R_{h+1},
\qquad x_i\longmapsto x_i^p+px_{i+1}.
\]
It raises height. Its extension to \(B_h\to B_{h+1}\) commutes with \(j\). At the arithmetic point \(a\), evaluate \(x_i\) at \(\delta^i(a)\). This evaluation commutes with Frobenius because \((\delta^i a)^p+p\delta^{i+1}a=\delta^ia\); it does not preserve all normal operations.

To define the normal operation, let \(S_i(x,y)\) be the integral arithmetic addition polynomials, characterized by the free-jet identity \(S_i(x,y)=\delta^i(x_0+y_0)\). The first two are
\[
S_0=x_0+y_0,\qquad
S_1=x_1+y_1-
\frac{(x_0+y_0)^p-x_0^p-y_0^p}{p}.
\]
The quotient polynomial is integral. Use independent divided-power parameters \(t_i\); their symbols \(t_i^{[n]}\) satisfy \(t_i^{[r]}t_i^{[s]}=\binom{r+s}{r}t_i^{[r+s]}\), so the construction does not invert factorials in \(\mathbb Z_p\). Congruence translation is the coaction
\[
\alpha(x_i)=S_i(x,pt).
\]
It extends continuously to the rational-locus completion because it preserves its defining ideal. Extracting the coefficient of \(t_0^{[1]}\) defines the first normal derivation \(D_0\). For \(h\ge2\), in the first two coordinates,
\[
D_0x_0=p,\qquad D_0x_1=-px_0^{p-1}.
\]
The point relation \(h_0=x_0^p+px_1-x_0\) therefore obeys
\[
\operatorname{ev}_a(h_0)=0,
\qquad D_0h_0=p^2x_0^{p-1}-p^2x_0^{p-1}-p=-p.
\tag{16.14}
\]
Modulo \(p^2\), the last coefficient is nonzero. Any comparison factoring through scalar point values would erase an operation that (16.13) retains.

The full normal action uses these arithmetic addition polynomials in every jet coordinate. Assign \(t_i\) weight \(p^i\); a finite-weight coefficient functional extracts only finitely many divided-power monomials. Their convolution gives the normal operators. An enriched congruence arrow retains both its arithmetic labels and its normal displacements. Its nerve is the diagram of finite strings of composable arrows; composition deletes the common middle object. The comparison preserves these maps, congruence depth and coefficient reduction. Frobenius uses the prolonged-height maps, and its antecedent-tube comparison includes the prescribed base change on the source coefficients. Fourier–Tate operations exist on its specified locally constant label sector after the character and \(p\)-inverting coefficient extension; they do not extend as normalized Haar integration on every continuous \(p\)-adic-valued label function. [Integral arithmetic tubes with their normal operations][integral-tubes]

The polynomial comparison extends to ordered collision diagrams. At each finite precision, form tensor products of two-term complexes \([A\to A[1/f]]\) for specified collision equations, replace coefficients by \(B\) before localization, and then take the \(p\)-adic inverse limit. The comparison is termwise injective and preserves independent normal operations, permitted substitutions and both empty tensor factors. For forest-supported partial diagonals with no extra denominator, the supported cohomology comparison is also injective and preserves ordered partial residues. Arbitrary extra denominators are outside that cohomology theorem. Frobenius carries the diagram to the higher-height diagram with its transformed support list. [Integral normal operations at an arithmetic marked point][integral-collisions]

A trace must have an equally explicit domain. If \(M_{x_0}\) is multiplication by \(x_0\), then
\[
[D_0,M_{x_0}]=pI.
\tag{16.15}
\]
A cyclic trace into a \(p\)-torsionfree module consequently satisfies \(p\tau(I)=0\), hence \(\tau(I)=0\). Since the normal derivation fixes each residue-class idempotent \(e\), the same argument with \(x_0e\) gives \(\tau(e)=0\). Finite residue evaluations remain legitimate functionals on their stated supported modules; they are not full cyclic traces on the position-normal operator algebra.

An arithmetic field comparison must therefore specify independently its ordered coefficient complex, its target collision system, and a common integrable trace domain. It must preserve (16.14), Frobenius variance, nonconsecutive collisions, both empty cuts and the local vacuum. The injective integral constructions supply substantial parts of that problem; scalar arithmetic evaluation cannot supply the remaining map.

## Whole-window positivity and the off-block term {#ch16-whole-window-positivity-and-the-off-block-term}

Return now to (16.3). For \(g\in L^2(-T,T)\), extended by zero, write \(h=g*g^*\). Writing \(\gamma_E\) for the Euler–Mascheroni constant, the real-space form of (16.1) is
\[
\begin{aligned}
Q_T(g)={}&\int h(u)(e^{u/2}+e^{-u/2})\,du
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\bigl(h(\log n)+h(-\log n)\bigr)\\
&-(\log(4\pi)+\gamma_E)h(0)
-\int_0^\infty\frac{e^{u/2}}{2\sinh u}
\bigl(h(u)+h(-u)-2e^{-u/2}h(0)\bigr)\,du.
\end{aligned}
\tag{16.16}
\]
The possibly divergent part is nonnegative, because
\[
h(u)+h(-u)-2h(0)=-\|g-g(\cdot-u)\|_2^2.
\]
Thus the form takes values in \(( -\infty,+\infty]\), with \(+\infty\) permitted outside its finite-energy domain. Translation of the support changes neither autocorrelation nor the form.

**Theorem (fixed whole-window positivity).** Every complex \(L^2\) test with essential support in an interval of width at most \(31/10\) satisfies
\[
Q(g)\ge7.0942\cdot10^{-109}\|g\|_2^2.
\]
For the infimum \(\lambda(T)=\inf_{g\ne0}Q_T(g)/\|g\|_2^2\),
\[
7.0942\cdot10^{-109}\le\lambda(31/20)
\le1.705263\cdot10^{-108}.
\tag{16.17}
\]
No assumption on zero locations or simplicity enters. [Local Weil positivity through half-width \(31/20\)][fixed-window]

The proof keeps \(1,152\) Legendre modes in each parity and controls the entire uncaptured coupling Gram matrix, including all mixed terms. Both polar contributions, the real-place term and the prime powers \(2,3,4,5,7,8,9,11,13,16,17,19\) survive. Weighted Schur estimates and rigorous interval inequalities turn these finite matrices and their tail bounds into an inequality for every vector in the window. The resulting bounds are \(7.0942\cdot10^{-109}\) in even parity and \(3.6094\cdot10^{-104}\) in odd parity. Their orthogonal sum gives (16.17).

To see why the coupling is indispensable, first consider an elementary matrix. Let
\[
W_c=\begin{pmatrix}1&c\\c&1\end{pmatrix}.
\]
Both one-dimensional diagonal blocks are positive for every real \(c\). Completing the square gives
\[
(x,y)W_c\binom{x}{y}
=(y+cx)^2+(1-c^2)x^2.
\tag{16.18}
\]
At \(c=1/2\), the remaining coefficient is \(3/4\). At \(c=2\), it is \(-3\), attained for \(x=1,y=-2\). Positivity of either diagonal block misses the negative mixed vector. This is an illustrative finite calculation, not a numerical model of the arithmetic operator.

For a finite-rank projection \(P\) and complementary projection \(P^\perp\), the same identity has blocks
\[
W_T=\begin{pmatrix}A&K^*\\K&D\end{pmatrix},
\qquad K=P^\perp W_TP.
\]
When the tail satisfies \(D>0\) with bounded inverse on the stated form domain, positivity is equivalent to
\[
A-K^*D^{-1}K\ge0.
\tag{16.19}
\]
The subtraction is nonnegative as an operator, so positivity of \(A\) gives an upper comparison for the Schur complement, not its required lower bound. In a Fourier cutoff, the archimedean part \(P^\perp A_TP\), where \(A_T\) is the real-place operator, is generally nonzero and belongs to \(K\). Dropping it changes (16.19). [Whole-window operators and Schur reductions][whole-windows]

The full question asks for every vector on every cofinal sequence of whole windows. Selected positive sectors and diagonal Fourier estimates do not control mixed combinations. Separate positive separated-window constructions are also available, but their bounded coefficient-defined convolution operators have nonzero multiplication defects. They do not furnish a convolution-stable positive source exhausting all intervals.

There is no weak uniform allowance hidden between the fixed theorem and the global question. The allowance \(\varepsilon(T)=\max(0,-\lambda(T))\) is nondecreasing; global boundedness, boundedness along one cofinal sequence, or subexponential growth already has Riemann-hypothesis strength. The unresolved signed Schur estimates must retain all prime, polar, real-place and tail contributions.

The arithmetic problem consequently has several precise comparison maps. Continuous duality retains the full jets; the theta complex realizes the full trace; the positive critical construction leaves exactly (16.12); integral normal comparison retains (16.14); local fields require collision operations beyond the existing linking algebra. A reconstruction theorem must decide which of these structures it preserves and construct the corresponding map on its actual domain. That is the point at which arithmetic trace theory joins the general boundary-to-bulk questions of the next chapter.

[trace-foundations]: #ref-ch16-01
[integer-complex]: #ref-ch16-02
[theta-complex]: #ref-ch16-03
[trace-operations]: #ref-ch16-04
[linking-fields]: #ref-ch16-05
[positive-layers]: #ref-ch16-06
[integral-tubes]: #ref-ch16-07
[integral-collisions]: #ref-ch16-08
[fixed-window]: #ref-ch16-09
[whole-windows]: #ref-ch16-10

## Source manuscripts {#ch16-source-manuscripts}

### 1. The test algebra and its scalar functional {#ref-ch16-01}

### 2. An integer-summation middle complex and its continuous dual {#ref-ch16-02}

### 3. A common Hilbert theta complex {#ref-ch16-03}

### 4. Trace-class coefficient homotopies {#ref-ch16-04}

### 5. Linking operators and vacuum creation {#ref-ch16-05}

### 6. Polynomial completions and the critical trace {#ref-ch16-06}

### 7. Integral arithmetic tubes with their normal operations {#ref-ch16-07}

### 8. integral normal operations at an arithmetic marked point {#ref-ch16-08}

### 9. Local Weil positivity through half-width 31/20 {#ref-ch16-09}

### 10. The Weil form on compact windows {#ref-ch16-10}
