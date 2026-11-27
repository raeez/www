# States, determinant lines and quantum fields

For \(\lambda,\hbar>0\) and a polynomial \(P\), put \(Z_\lambda(P)=\int_{\mathbb R}P(x)e^{-\lambda x^2/(2\hbar)}\,dx\). Its mass and its normalized second moment are

\[
Z_\lambda(1)=\sqrt{\frac{2\pi\hbar}{\lambda}},
\qquad
\frac{Z_\lambda(x^2)}{Z_\lambda(1)}=\frac{\hbar}{\lambda}.
\]

The covariance \(\hbar/\lambda\) determines all moments of the centered normalized Gaussian \(\omega_\lambda(P)=Z_\lambda(P)/Z_\lambda(1)\). The factor \(Z_\lambda(1)\) transforms with the integration density. In a family of complex Gaussian field theories the vacuum amplitude also carries the orientation and phase of the continued cycle.

For the level-one Heisenberg current, the Fock representation and the harmonic scalar on the disk give independent realizations of the same oscillator modes. A mixed moment distinguishes two states with identical one-mode marginals. A neutral pair of Wilson rays gives a coherent state whose collar amplitude can also be evaluated using the disk heat kernel. In quadratic gravity the corresponding observable is a line-valued functional. On a common small family of Ward backgrounds \(u\), it takes the form \(\mathcal Z_u(P)=s_{\mathrm{fp}}(u)\,\omega_u(P)\), where \(\omega_u\) is the normalized Gaussian state and \(s_{\mathrm{fp}}\) is a based section of the vacuum line obtained from the coefficient heat trace. Identifying this functional with the amplitude of a geometric cap requires a cutting map.

## Finite Gaussian integration and the determinant line {#ch11-finite-gaussian-integration-and-the-determinant-line}

Let \(C\) be a finite acyclic cochain complex, with differential of degree \(+1\). Its cotangent complex \(C\oplus C^*[-1]\) carries a nondegenerate pairing \(\mathcal B\) of degree \(-1\). A cyclic differential \(Q\) obeys the graded integration-by-parts identity for this pairing. If \(Q^2=0\), the quadratic action is

\[
S(\phi)=\frac12\mathcal B(\phi,Q\phi).
\]

A cyclic contraction \(R\) satisfies \(QR+RQ=1\) and \(R^2=0\), with the corresponding graded pairing compatibility. Its image is the complex gauge subspace used below; the restricted action has the inverse induced by \(R\). To integrate, one must still specify a real cycle for the even variables and an order of extraction for the odd variables. This is the finite-dimensional geometry behind Batalin–Vilkovisky integration. [Schwarz, *Geometry of Batalin–Vilkovisky quantization*](https://arxiv.org/abs/hep-th/9205088).

For the diagonal cotangent differential induced by \(d:C^j\to C^{j+1}\), choose Hermitian metrics and singular pairs \(u_{j,\ell},v_{j,\ell}\) with

\[
du_{j,\ell}=\sigma_{j,\ell}v_{j,\ell},
\qquad \sigma_{j,\ell}>0,
\]

where \(u_{j,\ell}\) has degree \(j\). The gauge coordinates \(x_{j,\ell},y_{j,\ell}\) have parity \(j\bmod2\), and the action is the sum of \(\sigma_{j,\ell}y_{j,\ell}x_{j,\ell}\).

For one even pair, take

\[
x=\sigma^{-1/2}w,\qquad
y=\sigma^{-1/2}\overline w,\qquad w\in\mathbb C,
\]

with the original oriented density. Its integral is

\[
\int_{\mathbb C}e^{-|w|^2/\hbar}
                 \frac{d^2w}{\pi\hbar\,\sigma}
=\sigma^{-1}.
\]

For an odd pair, let \([xy]\) mean extraction of the coefficient of the ordered monomial \(xy\). Since \(yx=-xy\),

\[
\hbar[xy]e^{-\sigma yx/\hbar}
=\hbar[xy]\left(1+\frac{\sigma}{\hbar}xy\right)=\sigma.
\]

Both normalized pair contractions are \(\hbar/\sigma\), with the sign reversed when an odd pair is reversed. Their vacuum factors are different. Multiplication in the fixed interleaved order gives

\[
G_C=\prod_{j,\ell}\sigma_{j,\ell}^{\,(-1)^{j+1}}.
\]

This calculation retains the even orientation, the odd order and the density. An inverse Hessian determines the normalized Wick contractions; it does not determine these choices.

Their coordinate dependence is organized by the determinant line

\[
\operatorname{Det}C
=\bigotimes_j(\det C^j)^{(-1)^j}.
\]

An exponent \(-1\) means the dual line. The cotangent semidensity line in this construction is \((\operatorname{Det}C)^{-1}\). A semidensity transforms by the square root of the Berezinian, the graded analogue of a Jacobian. For a coefficient change \(A\), the cotangent lift has Berezinian \((\operatorname{Ber}A)^2\), and the transported semidensity acquires \((\operatorname{Ber}A)^{-1}\). The determinant-line description fixes this factor without an independent square-root choice. The continued orientation of the even cycle is retained in a separate flat line. Determinant lines also provide the setting for regularized determinants of elliptic operators; Quillen's construction is a basic example. [Quillen, *Determinants of Cauchy–Riemann operators over a Riemann surface*](https://link.springer.com/article/10.1007/BF01086022).

If \(C_{\mathrm{Wick}}\) denotes the graded symmetric inverse-action contraction without its factor \(\hbar\), normalized integration is

\[
\omega(F)=
\left[\exp\left(\frac{\hbar}{2}\partial_{C_{\mathrm{Wick}}}\right)F\right](0).
\]

Here \(\partial_C\) contracts two observable slots with \(C\); the exponential terminates on a polynomial. The unnormalized functional is \(Z(F)=G_C\omega(F)\). Consequently a state is the normalized linear functional \(\omega\), while an amplitude retains the factor and line in which \(G_C\) lives. Positivity is asserted for the actual even probability law when available; odd integration is algebraic Berezin extraction.

### The scalar disk and its collar {#ch11-harmonic-disk-and-collar}

Mark the centre and angular coordinate of a Euclidean unit disk \(D\). A real harmonic field with constant mode zero has the expansion

\[
\phi=h+\bar h,\qquad h(z)=\sum_{n\ge1}Z_nz^n/n .
\]

At finite Fourier cutoff the disk assigns the amplitude \(e^{-S_D}\), where \(S_D=(8\pi)^{-1}\int_D|\nabla\phi|^2\,d^2z\). Angular integration gives \(S_D=\frac12\sum_n |Z_n|^2/n\). Squaring the amplitude and normalizing against \(d^2Z_n\) gives independent circular complex Gaussians,

\[
d\mu=\bigotimes_{n\ge1}\frac{e^{-|Z_n|^2/n}}{\pi n}\,d^2Z_n .
\]

The factors have mass one, so removing a cutoff preserves every finite marginal. Almost every sample is harmonic in the open disk and has a distributional boundary value. The action defines this law by its finite-dimensional marginals even though a typical sample has infinite total Dirichlet energy.

The disk Hilbert space is the closure of holomorphic polynomials in \(L^2(\mu)\). In the level-one current Fock space a creator acts by multiplication by \(p_n\), and its adjoint acts by \(n\partial_{p_n}\). The substitution \(V:p_n\mapsto Z_n\) is unitary because on both sides the distinct occupation monomials are orthogonal and \(\|Z^{\boldsymbol m}\|^2=\prod_n n^{m_n}m_n!\). A norm-one amplitude \(F\) therefore gives a probability law \(|F|^2d\mu\) on the harmonic fillings.

The same scalar action on a cylinder of real length \(t\) gives a two-dimensional oscillator of frequency \(n\) and mass \(n^{-2}\) in each complex coordinate. Subtract its ground energy \(n\) before removing the cutoff. The ground-state transform of its heat kernel has mean \(q^n Z_n\) and variance \(n(1-q^{2n})\), where \(q=e^{-t}\). Thus for independent unit-variance circular Gaussians \(\xi_n\),

\[
(P_qG)(Z)=\mathbb E_\xi G\!\left(
  (q^n Z_n+\sqrt{n(1-q^{2n})}\,\xi_n)_{n\ge1}\right),
 \qquad 0<q\le1 .
\]

This is the Mehler semigroup for the independent complex oscillators. It satisfies \(P_1=1\) and \(P_qP_s=P_{qs}\) by addition of the independent Gaussian noises. On the holomorphic subspace it is \(q^{L_0}\), with \(L_0=\sum_{n\ge1} nZ_n\partial_{Z_n}\) on polynomials. Indeed a monomial \(Z^{\boldsymbol m}\) has eigenvalue \(q^{\sum_n n m_n}\). The amplitude with one cylinder inserted is \(\langle F,P_qG\rangle\).

### Measuring a relative phase from the half-space {#ch11-relative-phase}

Put a free current on the boundary of \(M=\mathbb R_{\ge0}\times D\), with \(t\) increasing into the interior and orientation \(dt\wedge dx\wedge dy\). Its three-dimensional input is the bracket with Hamiltonian operator \(\kappa\partial_z\). The corresponding quadratic action is

\[
S_\kappa=\tau_M\!\left(\eta D_M\Phi+\tfrac{\kappa}{2}\eta\partial_z\eta\right),
\qquad D_M=dt\,\partial_t+d\bar z\,\partial_{\bar z},
\qquad i^*\eta=0 .
\]

Here \(\tau_M\) integrates after wedging with \(dz/(2\pi i)\), and \(i^*\) is tangential restriction to the physical boundary. Choose numerical parameters with \(\hbar\kappa=1\). Regular observables have compact smooth joint kernels in each finite field number, with projective completion at fixed support and an algebraic sum over field numbers. The quantum collar inclusion \(i_\hbar\) and projection \(p_\hbar\) obey \(p_\hbar i_\hbar=1\). With the boundary trace \(\tau(\alpha)=(2\pi i)^{-1}\int_D dz\wedge\alpha\), integration by parts identifies the boundary binary differential on \(sf\,s\alpha\) with \(-\hbar\kappa\,\tau(f\partial_z\alpha)=\tau((\partial_z f)\alpha)\). The suspension \(s\) lowers degree by one. This identifies the regular current complexes together with their disjoint-support products.

Choose a compact radial cutoff \(\chi\) equal to one near the origin. The smooth forms \(\alpha_m=z^{-m}\bar\partial\chi\) share an annulus and have moments \(\tau(z^{j-1}\alpha_m)=\delta_{jm}\). Write \(I_B(p_m)=s\alpha_m\) and extend to polynomials by multiplication. These are closed boundary representatives. Their internal contractions vanish by angular weight, and the annular current \(b_{-n}\) acts on them as multiplication by \(p_n\).

To probe one mode from the interior, choose \(\chi_o=1\) on that annulus with compact support in \(D\), and a smooth normal profile \(\rho_j(t)dt\) of integral one strictly above the collar. In the collar convention \(\zeta^2=-1\) the test on the \(\Phi\) component is \(u_j=\zeta^{-1}\kappa\,s(\rho_jdt\,\chi_o z^{j-1}e_\Phi)\). Extend it by zero and multiply by the collar inclusion of a boundary observable. Projection gives

\[
\beta(u_j)v=p_\hbar\bigl(\operatorname{ext}(u_j)i_\hbar(v)\bigr),
\qquad \beta(u_j)I_B f=I_B\,\partial_{p_j}f .
\]

Indeed the linear projection of \(u_j\) vanishes. The mixed Wick contraction against the \(m\)-th annular factor is \(\hbar\kappa\,\tau(\chi_o z^{j-1}\alpha_m)=\delta_{jm}\). Summing over the slots of a monomial differentiates it. Mere restriction of the interior test to \(t=0\) would give zero even on \(p_j\). This computation uses cochains. The bulk tests may have nonzero differential.

Take two copies \(u'_1,u''_1\) on disjoint ordered normal slabs. The successive operation \(2b_{-1}^2\beta(u_2)+b_{-2}\beta(u''_1)\beta(u'_1)\) acts on the chosen representatives by

\[
O=2p_1^2\partial_{p_2}+p_2\partial_{p_1}^2 .
\]

On the half-space take the closed cycles \(i_\hbar I_B((p_1^2\pm p_2)/2)\). On the disk take the two amplitudes \(F_\pm=(Z_1^2\pm Z_2)/2\) and measure the real, rotation-invariant function of the central field derivatives

\[
C=2\operatorname{Re}\bigl(h'(0)^2\overline{h''(0)}\bigr)
  =Z_1^2\bar Z_2+\bar Z_1^2Z_2 .
\]

Its operator on holomorphic states is the Toeplitz operator \(T_C\), multiplication by \(C\) followed by orthogonal projection. Gaussian integration by parts turns \(\bar Z_n\) under this projection into \(n\partial_{Z_n}\). The two indices in each term are distinct, so \(T_C=VOV^{-1}\) on polynomials. The vectors \(p_1^2,p_2\) are orthogonal, each has squared norm two, and \(O\) exchanges them with coefficient two. Thus \(F_\pm\) have norm one and \(\int C|F_\pm|^2d\mu=\pm2\). Integrating out either active coordinate removes the cross term. Every single-mode marginal agrees between the two laws.

Both amplitudes have energy two. The **one-sided** collar pairing and its normalization are consequently

\[
\langle F_\pm,P_qT_CF_\pm\rangle=\pm2q^2,\qquad
\langle F_\pm,P_qF_\pm\rangle=q^2 .
\]

Their ratio retains the measured value \(\pm2\) at every finite real collar. Propagating the real function \(C\) itself would give \(P_qC=q^4C\). The distinction already appears in two oscillator modes.

### A neutral ray pair and a sourced disk {#ch11-neutral-ray-pair}

There is a second way for the half-space to prepare a state. A Wilson ray of charge \(a\) couples the one-form \(A\) to an oriented curve by \(\int_L A\). In the Gaussian Chern–Simons presentation use orientation \(dx\wedge dy\wedge dt\), level one and the boundary condition \(i^*A\in(dz)\) on compact form tests. The line changes the quantum differential by \(-iaI_L\), where \(I_L\) integrates a one-form test along the ray. Stokes' formula gives \(I_Ld=0\) on admissible zero-forms because they vanish at the boundary endpoint and have compact support. A free interior endpoint would contribute a nonzero evaluation.

Place charges \((a,-a)\) at \((r,0)\), with \(a\in\mathbb R\) and \(0<r<1\). Use the real logarithm. Continue the two proper rays upwards as disjoint smooth graphs, vertical near the endpoints and eventually constant, with the prescribed smooth convergence and first-derivative bounds on the merging family. Use the planar Cauchy propagator, disjoint radial transverse mollifiers, caps above the bending region and the compact tests, and constant framing. Remove self-contractions. If the outgoing separation is \(\epsilon d\) with \(d>0\) fixed, the mutual Gaussian contraction in the exponent is \(-a^2(\log r-\log(\epsilon d))\). Multiplication by the prescribed outgoing factor \((\epsilon d)^{-a^2}\) leaves \(r^{-a^2}\).

The outer contour current sees \(a/(w-r)-a/w\). Its \(n\)-th positive mode therefore has eigenvalue \(ar^n\), and the zero mode sees total charge zero. Since \(J_n=n\partial_{p_n}\) for \(n>0\), these equations together with the computed constant term give the outgoing vector

\[
\Psi_{a,r}=r^{-a^2}\exp\!\left(a\sum_{n\ge1}p_n r^n/n\right)|0\rangle .
\]

The three-dimensional formula first specifies one coefficient at each oscillator weight. Hilbert convergence follows from the independent disk preparation. Add the real source \(2a\operatorname{Re}h(r)\) to the logarithm of the disk's *probability* weight. At cutoff \(N\) set \(h_N(r)=\sum_{n=1}^NZ_nr^n/n\) and \(L_N=\sum_{n=1}^Nr^{2n}/n\). Completing the square in each complex coordinate gives

\[
d\nu_N=e^{2a\operatorname{Re}h_N(r)-a^2L_N}\,d\mu,\qquad
L_N\longrightarrow L=-\log(1-r^2).
\]

Each of the first \(N\) means shifts to \(ar^n\) and its variance remains \(n\). For \(M\le N\), the disk inner product of \(e^{ah_M(r)}\) and \(e^{ah_N(r)}\) is \(e^{a^2L_M}\), by independence of the tail. The squared distance is therefore \(e^{a^2L_N}-e^{a^2L_M}\). The exponentials converge in the holomorphic Hilbert space, and their normalized squared moduli converge in \(L^1(\mu)\). The ray state has squared norm \(r^{-2a^2}(1-r^2)^{-a^2}\). Its normalized harmonic filling law is exactly \(e^{2a\operatorname{Re}h(r)-a^2L}\,d\mu\).

On the second holomorphic amplitude the real collar replaces \(r\) by \(qr\). Pairing with the first inserts \(qr^2\) into the covariance sum. With \(V\) the Fock-to-disk isometry, this gives

\[
\frac{\langle V\Psi_{a,r},P_q V\Psi_{a,r}\rangle}
     {\|V\Psi_{a,r}\|^2}
=\exp\!\left(a^2\sum_{n\ge1}\frac{(q^n-1)r^{2n}}{n}\right)
=\left(\frac{1-r^2}{1-qr^2}\right)^{a^2}.
\]

This pairing equals one when the collar length is zero or the charge vanishes. For nonzero real \(a\) the unnormalized norm diverges as \(r\uparrow1\). Neutrality places the output in the disk theory with its constant mode fixed to zero. A nonneutral output requires a charged zero-mode sector. Absolute cap normalization would also have to retain the three-dimensional mutual scalar, which cancels from the probability law.

## The quadratic theory on a solid torus {#ch11-the-quadratic-theory-on-a-solid-torus}

Fix \(0<|q|<1\), \(\kappa\in\mathbb C^\times\) and \(\hbar>0\). The underlying three-manifold is

\[
N_q=
\bigl(([0,\infty)\times\mathbb C)\setminus\{0\}\bigr)
\big/\langle(t,z)\mapsto(|q|t,qz)\rangle.
\]

Its boundary is the elliptic curve \(\mathbb C^\times/q^{\mathbb Z}\). The differential in the topological and antiholomorphic directions is

\[
D=dt\,\partial_t+d\bar z\,\partial_{\bar z}.
\]

Use the fixed coefficient metric and density

\[
\rho^2=t^2+|z|^2,\qquad
d\mathrm{vol}=\rho^{-3}dt\,dx\,dy,\qquad
|dz^w|^2=\rho^{2w},\quad |dt|^2=\rho^2,\quad
|d\bar z|^2=4\rho^2.
\]

The absolute coefficient complex has components \((e,h,f,b,c)\), weights \((0,1,2,0,1)\), and internal degrees \((0,0,0,1,-1)\). Weight \(w\) means the coefficient takes values in \((dz)^w\), with descent under the displayed quotient. The last two components are the odd constraint fields. Total degree is internal degree plus partial form degree. On partial form degree \(p\), its source-zero differential is

\[
d_C=D+(-1)^p\delta_A,\qquad
\delta_A(e,h,f,b,c)=(0,-2c,\kappa\partial_zc,-e,0).
\]

Let \(B\) be its paired relative complex. Absolute smooth cochains are unrestricted up to the boundary; relative cochains have zero tangential pullback. The paired field space is

\[
\mathcal E=C^\infty(C)\oplus C^\infty(B)_{\mathrm{rel}}[1],
\qquad V[1]^n=V^{n+1}.
\]

The degree-\(-1\) form is fixed by

\[
\mathcal B(a,b[1])
=\frac{(-1)^{|a|+1}}{2\pi i}
                  \int_{N_q}dz\wedge\langle a,b\rangle,
\qquad
\mathcal B(y,x)=-(-1)^{|x||y|}\mathcal B(x,y).
\]

The differential on the relative summand is the signed bilinear transpose of the absolute differential. It is not its Hermitian adjoint.

A background consists of a smooth weight-minus-one partial one-form \(\mu\), with zero normal trace, and an actual smooth weight-two function \(T_\mu\) satisfying

\[
D\mu+\mu\wedge\partial_z\mu=0,
\qquad
(D+L_\mu^{(2)})T_\mu=\frac{\kappa}{2}\partial_z^3\mu,
\qquad
L_\mu^{(2)}=\mu\wedge\partial_z+2(\partial_z\mu)\wedge.
\]

The first equation is the Maurer–Cartan equation for the vector-field-valued form \(\mu\,\partial_z\). The second is the Virasoro Ward identity for the stress tensor \(T_\mu\), with the third derivative of \(\mu\) as its central term. The numerical Gaussian requires a smooth solution of both equations on \(N_q\).

Let \(\Delta_C=d_Cd_C^\dagger+d_C^\dagger d_C\) be the original absolute Hodge realization, which has a positive spectral gap, and let \(r_C=d_C^\dagger\Delta_C^{-1}\) be its Green contraction. It satisfies

\[
d_Cr_C+r_Cd_C=1,\qquad r_C^2=0.
\]

Let \(r_B\) be the actual signed paired transpose of \(r_C\), and put \(R_{\mathrm{diag},0}=\operatorname{diag}(r_C,r_B)\), with the relative shift included. The original adjoint is fixed. A single sufficiently small ordinary \(C^1\) neighbourhood of \(\mu=0\) gives a numerical inverse of

\[
1+L_\mu^{(2)}\widehat r,
\qquad
\widehat r=(r_C)_{ff}
       +\frac{\kappa}{2}\partial_z(r_C)_{hf},
\]

on every ordinary Sobolev level. Bounds at higher levels depend on finitely many higher smooth seminorms, which must be bounded but need not be small. No iterated reflected boundary conditions are imposed on these ordinary smooth inputs.

The deformation \(a_\mu=d_{C,\mu}-d_C\) takes values in the \(f\)-component. Its row on \((e,h,f)\), with source forms multiplying on the left, is

\[
\mathcal A_\mu=
\left(
\frac{\kappa^2}{2}(\partial_z^3\mu)
+\kappa\mu T_\mu\partial_z
-\frac{\kappa^2}{2}L_\mu^{(2)}\partial_z^2,\quad
\frac{\kappa}{2}L_\mu^{(2)}\partial_z,\quad
L_\mu^{(2)}
\right).
\]

The explicit coefficient map \(D_\mu=1+a_\mu r_C\) intertwines the original and deformed differentials. Its inverse is \(1-\iota_f(1+L_\mu^{(2)}\widehat r)^{-1}\mathcal A_\mu r_C\), where \(\iota_f\) inserts the \(f\)-component. Its cotangent lift is
\(\mathsf S_\mu=\operatorname{diag}(D_\mu,D_\mu^{-t})\), where \(t\) is the signed bilinear transpose. The full quadratic differential also contains the response block \(P_\mu\), including both odd fields:

\[
\widetilde Q_\mu=
\begin{pmatrix}d_{C,\mu}&P_\mu\\0&-d_{B,\mu}\end{pmatrix},
\qquad
P_\mu=
\begin{pmatrix}
0&2&\kappa\partial_z&0&0\\
-2&2\kappa\partial_z&2\kappa T_\mu&0&0\\
\kappa\partial_z&-2\kappa T_\mu&0&0&0\\
0&0&0&0&1\\
0&0&0&1&0
\end{pmatrix}.
\]

A triangular cyclic response shear
\(V_\mu=1-\tfrac12(R_{\mathrm{diag},\mu}P_\mu-P_\mu R_{\mathrm{diag},\mu})\),
with \(P_\mu\) understood as the upper off-diagonal operator, gives

\[
M_\mu=V_\mu\mathsf S_\mu,\qquad
\widetilde Q_\mu M_\mu=M_\mu d_{\mathrm{diag},0},
\qquad
S_\mu(M_\mu\phi)=S_{\mathrm{diag},0}(\phi).
\]

Here \(d_{\mathrm{diag},0}=\operatorname{diag}(d_C,-d_B)\),
\(R_{\mathrm{diag},\mu}=\mathsf S_\mu R_{\mathrm{diag},0}\mathsf S_\mu^{-1}\)
is its transported paired contraction, and
\(S_\mu(\phi)=\tfrac12\mathcal B(\phi,\widetilde Q_\mu\phi)\).
The full inverse-action contraction is
\(\mathcal R_\mu=M_\mu R_{\mathrm{diag},0}M_\mu^{-1}\).
The map at zero source is the original response shear \(M_0=V_0\); discarding it would change the original cycle. [*A numerical Gaussian on the native source graph*, §§1–3](#ref-ch11-01).

## A numerical state from the original cycles {#ch11-a-numerical-state-from-the-original-cycles}

Take the original finite singular windows \(C_\Lambda\) of \(\Delta_C\), with their singular pairs, ordered odd coordinates and cotangent lines. Apply \(M_\mu\) to their actual finite integration cycles. The cyclic chain identity above proves the action equality before any covariance is assigned. Each even action becomes \(\sum|w_{j,\ell}|^2\), and its unnormalized factor in the transported coefficient frame is

\[
G_\Lambda=\prod_{(j,\ell)\in\Lambda}
                    \sigma_{j,\ell}^{\,(-1)^{j+1}}.
\]

This finite line statement does not assert convergence of the product as \(\Lambda\to\infty\).

Let \(\mathscr H_s\) be the ordinary Sobolev space of the full coefficient bundle, with no boundary condition, and let \(\mathscr D_{-s}=\mathscr H_s'\) using the fixed coefficient pairing. Let \(\mathsf W\) be the square-summable complex even-pair coordinates, regarded as a real Hilbert space. The original cylindrical cycle map is

\[
A_{\mathrm{ev}}w
=\sum_{j\ {\rm even},\ell}\sigma_{j,\ell}^{-1/2}
       (u_{j,\ell}w_{j,\ell}
           +v_{j,\ell}^{\vee}\overline{w_{j,\ell}}).
\]

The dual vectors have the fixed pairing signs. Its continued real-linear map \(\mathfrak A_\mu:\mathsf W\to\mathscr D_{-6}\) is defined weakly by

\[
\langle x,\mathfrak A_\mu w\rangle
=\mathcal B(M_\mu^{-1}x,A_{\mathrm{ev}}w),
\qquad x\in\mathscr H_6.
\]

It is Hilbert–Schmidt: its transpose factors through the bounded map
\(\mathscr H_6\to\mathscr H_2\) induced by \(M_\mu^{-1}\), followed by the Hilbert–Schmidt inclusion \(\mathscr H_2\hookrightarrow L^2\) in dimension three.

**Theorem 11.1 (normalized numerical Gaussian).** Fix the original metric and density, \(0<|q|<1\), \(\kappa\ne0\), \(\hbar>0\), and a smooth integrable \(\mu\) with zero normal trace in the single small \(C^1\) inverse neighbourhood. Supply a smooth solution \(T_\mu\) of the Ward equation above, based by \(T_0=0\) for families through zero. Couple the normalized even finite-cycle integrals using the same singular-pair Gaussian coordinates at every window. The resulting fields \(\Phi_{\Lambda,\mu}\) converge in mean square and almost surely in \(\mathscr D_{-6}\) to a centered Radon Gaussian \(\Phi_\mu\). Its law has support equal to the closure of \(\mathfrak A_\mu\mathsf W\). For a real orthonormal basis \(e_n\) of \(\mathsf W\),

\[
\mathbb E\|\Phi_\mu-\Phi_{\Lambda,\mu}\|_{-6}^2
=\frac{\hbar}{2}
 \sum_{e_n\notin\Lambda}\|\mathfrak A_\mu e_n\|_{-6}^2
\longrightarrow0.
\]

The real covariance is
\(\frac{\hbar}{2}\mathfrak A_\mu\mathfrak A_\mu^*\), with the real Hilbert adjoint. Odd and mixed moments converge by the graded Wick rule for the full inverse action. They do not define an odd-variable probability measure. Parameter-uniform statements require bounds on the finitely many higher source and background seminorms used in the estimates. [*A numerical Gaussian on the native source graph*, Theorems 4–6](#ref-ch11-01).

The action domain is smaller than this distributional support. In the original unwhitened coordinates \(x_{j,\ell}\), its transported form domain requires

\[
\sum_{j,\ell}\sigma_{j,\ell}|x_{j,\ell}|^2<\infty,
\]

while the operator domain requires the same sum with \(\sigma_{j,\ell}^2\). The Cameron–Martin space is the transported form domain with its covariance norm. In infinite rank a typical Gaussian sample has nonsquare-summable white coordinates and lies outside this domain. The construction does not evaluate the quadratic action on a typical distribution.

There is an exact space of observables on which the state and its Ward identity are numerical. Represent a linear observable by \(\ell_x(\phi)=\mathcal B(x,\phi)\), of degree \(|x|-1\), and put \(\mathcal T=\mathcal E[1]\). For ordinary graded Taylor tensors, complete with all seminorms

\[
\|F\|_{p,r}^2
=\sum_{n\ge0}(n!)^{2p}
             \|F_n\|_{T_r^{\widehat\odot n}}^2,
\qquad p\ge0,\quad r\ge1,
\]

where \(T_r\) is the ordinary Sobolev completion of the labels, retaining the relative tangential condition. Let \(C_\mu\) be the graded bilinear tensor of \(\mathcal R_\mu\), without its factor \(\hbar\). The intersection is nuclear Fréchet. On it,

\[
\omega_\mu(F)
=\left[e^{\hbar\partial_{C_\mu}/2}F\right](0),
\qquad
\omega_\mu(q_\mu F+\hbar\Delta_{\mathrm{BV}}F)=0.
\]

The observable differential is \(q_\mu\ell_x=\ell_{\widetilde Q_\mu x}\), extended by the graded derivation rule; no additional shifted-complex minus sign is inserted. The degree-\(+1\) Batalin–Vilkovisky operator \(\Delta_{\mathrm{BV}}\) contracts with the canonical paired tensor. The identity follows from
\([q_\mu,\tfrac12\partial_{C_\mu}]=\Delta_{\mathrm{BV}}\).
Trace-norm covariance convergence and the factorial weights extend the polynomial calculation continuously. For entire even tests, the functional is actual integration against the Gaussian law. Boundary conditions belong to the test labels; they are not imposed by assigning an undefined boundary trace to a negative-regularity sample. [*A numerical Gaussian on the native source graph*, Theorem 7](#ref-ch11-01).

## Original coefficient heat and a based local vacuum line {#ch11-original-coefficient-heat-and-a-based-local-vacuum-line}

Recovering normalization requires separate input. Reflect the solid torus across its boundary to the closed double \(M_q\), and use smooth reflection-invariant backgrounds on that double. The coefficient operator is

\[
A_{\mu,T}=d_{\mu,T}d_0^\dagger+d_0^\dagger d_{\mu,T},
\]

with the source-zero adjoint \(d_0^\dagger\) fixed. For the five components take Sobolev offsets \(\alpha=(2,1,0,2,0)\) and weights \(w=(0,1,2,0,1)\), and set

\[
X^s=\left(\bigoplus_iH^{s+\alpha_i}(M_q;w_i)\right)_+,
\]

where \(+\) is the subspace invariant under reflection. The realization \(A_+\) on this reflection-even sector has common domain \(X^2\), a uniform right-half-plane spectral gap and trace-class holomorphic heat. Its source neighbourhood is small in \(\|\mu\|_{C^4}+\|T\|_{C^1}\), with bounded higher seminorms for uniform source derivatives. This reflected weighted realization is distinct from the ordinary cochain domain of Theorem 11.1.

On the integrable locus, with its smooth Ward filling, choose a positively oriented contour \(\Gamma\) in the resolvent set enclosing a finite spectral cluster. The Riesz projection
\[
P_\Gamma(u)=\frac{1}{2\pi i}\oint_\Gamma
           (\zeta-A_+(u))^{-1}\,d\zeta
\]
selects the finite absolute complex, paired with its smooth relative transpose. Let \(A_\Gamma(u)\) be the restricted coefficient operator and \(D_j(u)\) its action blocks. In the original continued density and cycle,

\[
G_\Gamma(u)=\prod_j\det D_j(u)^{(-1)^{j+1}},
\qquad
k_\Gamma(u)=\operatorname{Str}\bigl(N\log A_\Gamma(u)\bigr),
\]

\[
\log\frac{G_\Gamma(u)}{G_\Gamma(0)}
=k_\Gamma(u)-k_\Gamma(0).
\]

The supertrace \(\operatorname{Str}\) inserts cohomological parity, and \(N\) multiplies degree \(j\) by \(j\). Logarithms use the branch continued from the positive source-zero spectrum. This coefficient-level formula has no extra factor \(1/2\). Same-operator finite spectral shells satisfy Fubini with their complete determinant factors, signs and phase. Their line maps are actual integration over the eliminated shell. A fixed finite collection of contours has a common sufficiently small neighbourhood; no uniform neighbourhood is asserted for an unbounded contour family. [*Finite action integrals from the original coefficient Riesz spaces*, Theorem 3 and §6](#ref-ch11-02).

The difference between relative and absolute normalization also has an infinite-dimensional example. Use exactly the same metric for the original reduced contraction \(\widehat r\) and the weight-two stress contraction \(h_2=D_2^\dagger\Delta_2^{-1}\). For a smooth reflection-invariant integrable source, set

\[
\mathsf T=L_\mu^{(2)}(\widehat r-h_2)
                      (1+L_\mu^{(2)}h_2)^{-1}.
\]

On its small-source branch, \(\|\mathsf T\|<1\), the fourth modified Berezinian is defined by the trace-class series

\[
\operatorname{Ber}_4(1+\mathsf T)
=\exp\left(\sum_{n\ge4}
       \frac{(-1)^{n+1}}{n}\operatorname{Str}_+(\mathsf T^n)\right).
\]

It equals one, and the common scalar-principal heat finite parts of every power vanish. With the specified zero-source stress heat, the actual logarithmic trace tends to zero as well. The proof combines a sourced chain homotopy with bulk and reflection-symbol cancellations. This determines the common relative factor; the original separate heat placements and the absolute base vacuum remain different data. [*The common relative determinant of the native contraction*](#ref-ch11-03).

**Theorem 11.2 (original heat finite part).** Use the original fixed-adjoint weighted realization above, with smooth reflected \(\mu,T\) sufficiently small in \(\|\mu\|_{C^4}+\|T\|_{C^1}\) and the stated bounds on higher seminorms. Put \(\ell_q=-\log|q|\). The coefficient supertrace on the reflection-even sector has, for every \(0<\delta<1/2\),

\[
\tau_+(t,u)=\operatorname{Str}_{X}(Ne^{-tA_+(u)})
=-\frac{\ell_q}{4t}+\frac{B(u)}{\sqrt t}+C(u)+O(t^\delta),
\]

where \(B(u),C(u)\) are scalar local heat coefficients. The estimate holds after each specified finite number of source derivatives under the higher-seminorm bounds. The coefficient of \(t^0\log t\) is zero. Consequently, with

\[
W_\epsilon(u)=-\int_\epsilon^\infty\tau_+(t,u)\frac{dt}{t},
\qquad
D_\epsilon(u)=\frac{\ell_q}{4\epsilon}
 -\frac{2B(u)}{\sqrt\epsilon}+C(u)\log\epsilon,
\]

the finite part \(W_{\mathrm{fp}}=\lim_{\epsilon\downarrow0}(W_\epsilon-D_\epsilon)\) exists with error \(O_{C^k}(\epsilon^\delta)\). It is holomorphic on the admitted holomorphic source families. [*The original coefficient heat finite part and its based vacuum line*, Theorems 3–4](#ref-ch11-04).

The coefficients come from the full matrix heat symbol and the fixed-surface reflection contribution. Parity cancels the intervening powers; both reflection factors of one half enter the leading coefficient. The right-half-plane gap on the reflection-even sector controls the integral at infinite time. Integrability of \(O(t^\delta)/t\) gives the finite-part limit. For action and line statements, the background must in addition satisfy the integrability and Ward-filling equations. The trace is independent of \(T\) at fixed \(\mu\) because \(T\) occurs in an off-diagonal triangular block; non-scalar action moments still depend on it.

Take a source family based by \(\mu(0)=T(0)=0\). Choose a nonempty finite original spectral window there, with its original density, odd ordering and oriented cycle. Its directly evaluated amplitude is

\[
A_*=\prod_{(j,\ell)\in\Gamma_*}
               \sigma_{j,\ell}^{\,(-1)^{j+1}}>0.
\]

The finite shell maps glue the density-cycle lines locally. Combining these maps with the complementary heat finite part gives a nonzero based section \(s_{\mathrm{fp}}\). In action-evaluation coordinates,

\[
\mathcal I(s_{\mathrm{fp}}(u))
=A_*e^{W_{\mathrm{fp}}(u)-W_{\mathrm{fp}}(0)},
\qquad
\nabla_{\mathrm{fp}}=d-dW_{\mathrm{fp}}.
\]

The section is horizontal for this local flat line connection. Its base value comes from the finite action integral; it has not been set equal to one. In a finite spectral frame the connection is
\(\nabla^K+dk_\Gamma-dW_{\mathrm{fp}}\), where \(\nabla^K\) is the determinant connection induced by spectral projection transport. The Mellin conversion also retains Euler's constant \(\gamma_E\):

\[
W_{\mathrm{fp}}(u)
=-\partial_s\operatorname{Str}_{X}(NA_+(u)^{-s})\big|_{s=0}
 +\gamma_E C(u).
\]

This is a local renormalized line section, not a limit of an unnormalized infinite product. Its construction does not fix global holonomy or an infinite bare phase. [*The original coefficient heat finite part and its based vacuum line*, Theorems 5–6](#ref-ch11-04).

The connection sign can be checked without a determinant calculation. Set
\(\mathcal D_\epsilon=D_\epsilon(u)-D_\epsilon(0)\) and
\(f_\epsilon=e^{-\mathcal D_\epsilon}\).
If \(\nabla_\epsilon s_\epsilon=0\), the product rule gives

\[
\bigl(\nabla_\epsilon+d\mathcal D_\epsilon\bigr)
                  (f_\epsilon s_\epsilon)=0.
\]

Thus the counterterm is **added** to the covariant connection. It is subtracted from the response one-form \(dW_\epsilon\), whose sign in the connection is negative. The resulting source connection tends to \(\nabla_{\mathrm{fp}}\) in \(C^{k-1}\) when the finite-part estimate holds in \(C^k\). No zero-scale limit of a heat-time component is implied. [*The source counterterm in the covariant connection*](#ref-ch11-05).

### Varying a positive level in the original heat construction {#ch11-positive-level-variation}

The original coefficient heat finite part also has a relative level formula on a specified family. Use the square-zero reflected Ward family, put \(x=|\kappa|^2\), and scale \(\kappa\) and the supplied filling together. On a compact interval \([a,b]\subset(0,\infty)\), assume a common gapped realization, the positive-cutoff variation identity and continuous differentiability in \(x\). The inserted trace must have a uniform expansion in one fixed finite power/logarithm scale, with the stated source derivatives and a decaying remainder. Compactness of the interval does not supply these analytic hypotheses.

Under them, the projection \(P_F\) to the \(F\)-current component has inserted finite part
\[
c_F(v,x)=\operatorname{FP}_{\epsilon\downarrow0}
\operatorname{Str}_X(P_Fe^{-\epsilon A_x})
=\frac12R_2[JP_F](v,x),
\]
where \(v\) is the admitted source parameter, \(J\) is parity and \(R_2\) is the second reflected heat coefficient. This coefficient already includes the normal-reflection factor; the displayed \(1/2\) comes from the positive reflection sector. The original endpoint finite parts obey
\[
W_{\mathrm{fp}}(v,x_1)-W_{\mathrm{fp}}(v,x_0)
=\int_{x_0}^{x_1}c_F(v,x)\,\frac{dx}{x}.
\]
If the inserted coefficients are continuous in \(x\), this yields \(x\partial_xW_{\mathrm{fp}}=c_F\), including the covered source derivatives. [Positive-level variation](#atlas-c-gravity-positive-level-variation).

The Mellin comparison fixes which absolute constant is retained. Absence of an \(\epsilon^0\log\epsilon\) term in the inserted trace makes the original constant heat coefficient \(C(v,x)\) independent of \(x\) on the interval. For the original Mellin branch,
\[
Z(0,v,x)=C(v,x),\qquad
W_{\mathrm{fp}}(v,x)=-Z'(0,v,x)+\gamma_EC(v,x).
\]
Thus positive-level differences equal the corresponding differences of \(-Z'(0)\). Neither \(C\) nor \(c_F\) has been proved zero, and the absolute Euler term remains. The estimate contains \(\log(b/a)\); it gives no control at \(x=0\). Passage through zero requires an integrable endpoint estimate and compatible heat control there. [The zero-level endpoint](#atlas-c-gravity-positive-level-zero-endpoint).

An explicit source distinguishes the local density from its integral. Take \(q=e^{-2\pi}\), \(\kappa=2\), \(u=\log\sqrt{t^2+|z|^2}\), and set \(F=z(1-\lambda_+e^{iu}-\lambda_-e^{-iu})\) for two small complex parameters. The fields \(\mu=-DF/\partial_zF\) and \(T=-(\kappa/2)\{F,z\}\) solve the two Ward equations, where \(\{F,z\}\) is the Schwarzian derivative. In the fixed coefficient frame, the two first derivatives of the density for \(c_F\) are

\[
\frac{1-2\log 2\mp i}{16\pi}\,e^{\pm iu}\,du\wedge d\varphi ,
\]

with \(\varphi=\arg z\) on the fixed torus. Each is a nonzero tangential derivative with integral zero. For the neutral mixed derivative, the two heat-symbol contributions proportional to \(-\log 2\) and \(+\log 2\) cancel. Thus the integrated first and second source derivatives vanish on these directions. Constancy for arbitrary sources or through zero level would require additional estimates.

On a based reflected Ward family small enough for both the numerical Gaussian and the local line construction, the product
\[
\mathcal Z_u(F)=s_{\mathrm{fp}}(u)\,\omega_u(F)
\]
is an actual continuous line-valued functional with the fixed-source Ward identity. This conditional composition retains the finite action anchor of the line and the independently constructed covariance of the normalized state. It does not identify their product with a state prepared by a geometric cap. That comparison still needs the map from uncut coefficient fields to cut fields, the identification of amplitude lines and the transport of observables through the same cutting-and-gluing diagram. [Line and state on a common family](#atlas-c-gravity-common-family-line-state).

## Moving boundary conditions and comparison of Gaussian constructions {#ch11-moving-boundary-conditions-and-comparison-of-gaussian-constructions}

The physical source changes the boundary graph of the fields. With \(\partial=\partial_z\), the tangential Hessian on the three even current components is

\[
K_\mu^{\mathrm{gr}}=
\begin{pmatrix}
\frac{\kappa}{2}[-\mu\partial^2-(\partial\mu)\partial+\partial^2\mu]
 &\frac12(\mu\partial+\partial\mu)&\mu/\kappa\\
-\mu\partial/2&\mu/(2\kappa)&0\\
\mu/\kappa&0&0
\end{pmatrix}.
\]

Its ghost block is zero; its graded extension raises partial form degree by one, compensating for the relative shift. For the boundary inclusion \(j:\partial N_q\hookrightarrow N_q\), the graph map and its domain are

\[
\mathsf G_\mu(a,b)=(a,b+K_\mu^{\mathrm{gr}}a),
\qquad
\mathcal E_\mu=
\{(a,\gamma):j^*(\gamma-K_\mu^{\mathrm{gr}}a)=0\}.
\]

The map is cyclic and intertwines \(\widetilde Q_\mu\) with the physical Hessian differential \(Q_{\mathrm{aff},\mu}\) on \(\mathcal E_\mu\). Static transport sends the finite cycles to this graph and the normalized law to \(\mathscr D_{-8}\). The observable topology is transported with the graph map; it cannot be replaced by an ordinary Sobolev graph norm without accounting for its derivative loss.

Differentiation requires more care. Let \(i\) be a finite cyclic embedding, \(p=i^\sharp\) its paired projection, and \(d\) the finite differential. For a source direction \(v\), put
\(A_v=\mathsf G_\mu^{-1}\partial_v\mathsf G_\mu\).
The vector \(A_vi x\) need not satisfy the fixed relative boundary condition. Its projection defect is

\[
\mathcal C_v=(p\widetilde Q_\mu-dp)A_vi,
\]

and the actual Green formula gives

\[
\mathcal B_{\mathrm{fin}}(u,\mathcal C_vx)
=-\frac1{2\pi i}\int_{\partial N_q}dz\wedge
 \left\langle\gamma_t a(iu),
       \gamma_t K_v^{\mathrm{gr}}a(ix)\right\rangle.
\]

Here \(\gamma_t\) is tangential pullback and \(a(-)\) selects the absolute current components. With
\(\Theta_v=p\partial_vi\) and \(\Gamma_v=pA_vi\), the differentiated chain equation is

\[
\partial_vd+[\Theta_v+\Gamma_v,d]
=p\mathsf G_\mu^{-1}(\partial_vQ_{\mathrm{aff},\mu})
             \mathsf G_\mu i+\mathcal C_v.
\]

The Green term is the boundary Hessian contribution. Applying a chain identity outside its relative domain would incorrectly erase it. Mixed source derivatives differentiate both embedded current factors and the Hessian, as well as the supplied filling \(T_\mu\). [*A numerical Gaussian on the native source graph*, Theorem 8 and equations (74)–(78)](#ref-ch11-01).

There is a precise formal comparison with the original homological-perturbation cutoff. A cyclic polar correction, followed by a gauge correction, compares it with a finite Riesz action. If \(\rho\) is the genuine based semidensity ratio and \(B_R,B_H\) are the two covariances after their actual maps to the same stress observables, then

\[
\mathcal Z_R^{\mathrm{st}}(F)
=\rho^{-1}\mathcal Z_H^{\mathrm{st}}
       \left(e^{\hbar\partial_{B_R-B_H}/2}F\right).
\]

This equality is over the formal source ring; each contraction exponential terminates on a polynomial. The line ratio and the ambient covariance correction are both required, even when the intrinsic finite actions are cyclically isomorphic. Numerical convergence of the original sharp-tail perturbation series and its identification with the continued-cycle limit remain separate questions. [*Finite action integrals from the original coefficient Riesz spaces*, Theorem 4 and equation (68)](#ref-ch11-02).

## Boundary insertions and the physical cap {#ch11-boundary-insertions-and-the-physical-cap}

A state on bulk observables becomes relevant to boundary fields through an insertion map. In the boundary coordinate \(e=1+u\), the classical symbol algebra is the graded polynomial algebra on \(u,h,f,b,c\) and their holomorphic derivatives. The actual differential includes

\[
q_{\mathrm{cl}}b=u,\qquad q_{\mathrm{cl}}u=q_{\mathrm{cl}}c=0,
\qquad
q_{\mathrm{cl}}h=-2(1+u)c,\qquad
q_{\mathrm{cl}}f=hc+\kappa\partial_zc.
\]

It also includes the partial-form differential on descendants. At the quantum level the source is the prescribed affine–ghost vacuum module with its actual Poincaré–Birkhoff–Witt products.

For ordinary boundary insertions there is a full-source result at each fixed finite polynomial and holomorphic-jet stage, retaining the enlarged source and output stages needed by the differentials and homotopies. “Ordinary” means that a root is at height zero before any incoming normal derivative is taken. The relative tangential endpoint quotient is part of the domain.

Let \(J_L^0\) be the classical insertion at positive heat scale \(L\), \(q_{\mathrm{cl}}\) the actual boundary differential, and \(Q_L^0\) the bulk differential. Then

\[
Q_L^0J_L^0-J_L^0q_{\mathrm{cl}}=0
\]

on the complete stated finite stage, including all physical components. The proof groups the lower heat-edge collapses before taking their limit: root terms reproduce the actual boundary differential, internal terms cancel by the classical master equation, and the remainders have a positive power of the lower cutoff.

There is also a first quantum heat comparison for the fixed supported unary map \(\widehat J_L\). This is formal perturbation theory for the constrained interacting action, with parameter \(\chi=-\hbar\) and independent \(\kappa\). Retain the complete forward transport \(W=W^0+\chi W^1\). With the Hom differential
\(\delta F=Q_{\mathrm{out}}F-(-1)^{|F|}Fq_{\mathrm{source}}\), a specified degree-\(-1\) chain homotopy satisfies

\[
\delta C_{L',L}
=\widehat J_{L'}-W_{L',L}\widehat J_L
\pmod{\chi^2}.
\]

It preserves the fixed normal collars, vanishes on the unit, commutes with holomorphic translation and retains the mixed antiholomorphic component. Further homotopies compare every fixed finite chain of heat scales. These statements concern the ordinary zero-height finite-stage domain. Incoming normal derivatives, positive-height roots, singular binary or higher collisions and higher quantum orders require additional equations. In particular, \(W^1\) cannot be discarded in the displayed difference. [*Ordinary boundary Ward identity and full-source heat cells*, Theorems 2 and 5](#ref-ch11-06).

### Transfer across a sourced affine collar {#ch11-sourced-affine-collar}

How much does a source between two meridians change a measured propagation amplitude? Fix \(q=1/2\), \(\kappa\ne0\), \(\hbar>0\) in the affine quadratic theory. On the cover put \(r^2=t^2+|z|^2\), \(u=\log r\) and \(D=dt\,\partial_t+d\bar z\,\partial_{\bar z}\). Cut at \(u_0<u_1<u_0+\log2\) and fix an angular frame separately on each end. Choose a smooth \(\log2\)-periodic real function \(f\) with constant values \(f_j\) on the end collars. For small real \(\lambda\) the change of angular coordinate \(F=zA(u)\), \(A=e^{i\lambda f}\), gives the genuine Ward background
\[
 J=\partial_zF,\qquad \mu=-zA'(u)Du/J,\qquad T=-\tfrac\kappa2\{F;z\},
\]
where \(\{F;z\}\) is the Schwarzian derivative. The sources \(\mu,T\) vanish on both end collars. For every \(M\ge2\), the positive-frequency weight-two scalar \(a=F^{M-2}J^2\) is closed. Its lift to the original affine fields has current \(a_F=\kappa a\) and conjugate component \(\gamma_E=\mu a\). Its traces are nonzero, and their coefficients in the marked unit frames are proportional to \(e^{Mu_j}A(u_j)^M\). Thus the outer-to-inner transfer is
\[
 R_M=e^{-ML}\left(\frac{A(u_0)}{A(u_1)}\right)^M
     =e^{-ML-iM\lambda(f_1-f_0)},\qquad L=u_1-u_0 .
\]
The source descends to the solid torus. The weighted mode has deck multiplier \(q^M\) and is a state of the cut shell. Its phase compares the two fixed frames.

The weighted pullback intertwines the source differential on scalars. On smooth finite sums of angular Fourier modes, extending this pullback to transverse fields requires a homotopy correction for the stress response. The absolute and relative harmonic projections have disjoint frequency support, so the response defect induces zero between them. An angular Green operator supplies a skew-adjoint homotopy for the complex-bilinear cut pairing. The resulting cyclic chain isomorphism preserves radial support and agrees with geometric rotation on the rigid ends. On a complete finite window through energy \(M_0\) with \(n+1\) complete radial singular pairs, transport the zero-source gauge, contour and density by that isomorphism. For the window with just the stated physical cohomology, its radial scalar remains \(\prod_{M=2}^{M_0}\prod_{j=0}^n\sigma_{M,j}^{-1}\), where \(\sigma_{M,j}\) are the original radial singular values. With the zero-frequency sector paired separately, the normalized transfer on positive-frequency harmonic states is \(\eta^{N}\), with \(\eta=e^{-L-i\lambda(f_1-f_0)}\) and \(N\) the total energy.

For example, supply both ends with the same positive Virasoro vacuum representation at \(c>25\), using the specified energy-preserving identification on each complete window through weight six. For the vacuum \(v\), the two orders of the bra against \(L_{-5}v\) give \(4c\eta^5\) for \(L_2L_3\) and \(14c\eta^5\) for \(L_3L_2\). At weight six, projecting \(L_{-4}L_{-2}v\) and \(L_{-3}^2v\) perpendicular to \(L_{-6}v\) gives a pairing of \(62c\eta^6/7\). On this marked Hilbert space the transfer has positive modulus \(e^{-LN}\) and unitary phase \(e^{-i\lambda(f_1-f_0)N}\). These closed-state measurements can distinguish global sources even when all germs of \(\mu,T\) agree at the two ends and at a nonflat middle meridian. A relative end rotation by \(\lambda\) changes the ratio of the weight-six and weight-five readings by \(e^{-i\lambda}\), independently of a common scalar normalization. [Sourced affine meridian transfer](#atlas-c-sourced-affine-meridian-transfer)

### Two-sided classical flux and the on-shell action {#ch11-classical-meridian-flux}

One can prepare the positive solution on the outer half of the shell and a relative negative harmonic of frequency \(-M\) on the inner half. Normalize each at its own end. Write \(a\) for the positive scalar and \(b\) for the relative component of the closed negative affine solution. Their mixed current is
\[
 \mathcal J=\frac{1}{2\pi i}(dz-\mu)\wedge a b .
\]
The Ward equations make \(\mathcal J\) closed and the relative condition makes its pullback to the physical annulus zero. Consequently its integral can be measured on any intermediate meridian \(Y\), including one where the source varies. With increasing-radius orientation and the negative input first, the raw relative harmonic on the reference hemisphere gives
\[
 \int_Y\mathcal J=c_M R_M,\qquad
 c_M=-\int_0^{\pi/2}\sin^{2M-3}\theta\,d\theta
     =-\frac{(2M-4)!!}{(2M-3)!!}.
\]
Taking the action-dual normalization of the negative harmonic makes \(c_M=1\). This uses two independently solved classical linear boundary problems on the cut.

The classical action also detects the shape of the source between the marks. More generally take \(A\) smooth, periodic and sufficiently close to one, constant of unit modulus near each end. Assume \(J\ne0\) and \(u\mapsto u+\log|A(u)|\) has positive derivative, so the real change \((t,z)\mapsto(|A|t,Az)\) preserves the radial foliation. Write \(s=A'/A\) and \(h=1+s/2\). On the small branch the original on-shell action is
\[
 S_{\mathrm{crit}}(A)-S_{\mathrm{crit}}(1)
 =\frac{\kappa}{32}\int_{u_0}^{u_1}
 \left(\frac{4s^2}{h}+\frac{(s')^2}{h^3}\right)du .
\]
For the twist \(A=e^{i\lambda f}\) the quadratic term is \(-\kappa\lambda^2\int((f'')^2+4(f')^2)\,du/32\). A twist which returns to its starting angle can therefore change the action even when its marked transfer equals the zero-source transfer. The factor \(e^{-S_{\mathrm{crit}}/\hbar}\) belongs to the classical saddle. This flux fixes the relative normalization of two classical modes. A quantum pairing also needs a contour and a half-density on each side. By 08:15:59 WIB on 18 November 2026, the sourced transfer, the classical flux and this action had been computed. [Classical affine flux and action](#atlas-c-classical-affine-meridian-flux)

### A fixed quantum measure on a nonflat meridian {#ch11-independent-meridian-measure}

Two Ward fillings can agree near every boundary face, corner and cut and still have different unnormalized quantum amplitudes. On the \(q=1/2\) solid torus take \(F_j=F_*e^{i\epsilon g_j}\), where \(F_*=zA_*(\log r)\) has a small nonzero source near the middle meridian and is the identity coordinate on both exterior collars. The two angular bumps \(g_1,g_2\) have disjoint supports inside the left half, related by a dilation of factor \(16/15\). All source and field germs agree on the collars. The dilation preserves the integrated critical density on the two patches, so the classical actions agree separately on each half.

Fix a compact current and its conjugate on the first patch before choosing the filling. The current coefficient \(p\) and conjugate one-form \(\beta\) have angular charges \(+8,-8\). The original affine action restricted to their two coefficients \(x,y\) is \(B_jxy\), up to its critical value. In the convention \(\tau(\omega)=(2\pi i)^{-1}\int dz\wedge\omega\), the kinetic term and the affine Poisson term give \(B_j=\tau(\beta\wedge(Dp+p\,\partial_z\mu_j))\). On the support of \(\beta\) the first bump has \(g_1=t\), so \(\partial_z\mu_1=-i\epsilon\,dt\). The second source vanishes there. Unit-integral test functions with mean \(t=1\) give \(B_1=1-i\epsilon,\ B_2=1\). On the common contour \(x=w,\ y=\bar w\) the oriented integral is
\[
 \int_{\mathbb C}e^{-B_j|w|^2/\hbar}\frac{d^2w}{\pi\hbar}=\frac{1}{B_j}.
\]
An independently prepared pair in the right half has \(B_R=1\).

At frequency five the negative-first Green pairing of the raw meridian modes is \(-16/35\). Rescale the negative mode by \(-35/16\) and write \(a,b\) for the resulting positive and negative coordinates. In each coordinate \(v\) prescribe the half-density \((\pi\hbar)^{-1/2}e^{-|v|^2/(2\hbar)}|d^2v|^{1/2}\). On the ordered seam \(b=-\bar a\) their product is the Gaussian density and \(a^k b^\ell\) has a signed Fischer moment. With the opposite exterior polarizations set to zero and \(S_{\mathrm{cl}}\) the sum of the two critical actions, the unnormalized result is
\[
 Z_{j;k,\ell}=\frac{e^{-S_{\mathrm{cl}}/\hbar}}{B_jB_R}
                   \delta_{k\ell}(-\hbar)^k k!,\qquad
 \frac{Z_{1;k,k}}{Z_{2;k,k}}=\frac1{1-i\epsilon}.
\]
At \(\epsilon=1/8\) the ratio is \((64+8i)/65\), with phase \(\arctan(1/8)\simeq0.124355\) radians. Vacuum division removes the entire difference. Holding the filling fixed and moving only the compact test changes the answer as well. If the same regulator includes both dilation-related tests, the couplings on the two fillings are \((1-i\epsilon,1)\) and \((1,1-i\epsilon)\). Their product integrals have ratio one.

For five meridian pairs of frequencies \(2,\ldots,6\), use compact charges \(\pm17\) and the product of the prescribed half-densities. Each half has harmonic frequencies of one sign, so the original cubic action has no neutral term there. With the specified positive Virasoro marks at \(c>25\) and unrotated end frames, the two bra orders \(L_2L_3,L_3L_2\) against \(L_{-5}v\) give \(Z_{j;0,0}\,4c e^{-5L}\) and \(Z_{j;0,0}\,14c e^{-5L}\). The projected weight-six pairing gives \(Z_{j;0,0}(62c/7)e^{-6L}\). The interacting identification of the exterior marks is an input. A continuum cap would require a controlled removal of the regulator on the full boundary complex, with its residual modes and absolute phase. The derivation is given in *A fixed finite quantum measure on a non-flat native meridian*, §§1–5. The independent evaluation of these finite integrals is dated 18 November 2026, 08:35:18 WIB. [Independent quantum measure on a meridian](#atlas-c-independent-affine-meridian-measure)

A gravitational cap would assign a vector or functional to a specified compact filling, on its boundary state space, with its absolute normalization and cutting law. In the scalar disk the action supplied the ground amplitude, the cylinder supplied a transfer, and the interior contractions or charged rays supplied probes with which to test both. For the solid torus one still needs the map from uncut coefficient fields to the fields on the geometric cut, an identification of the two amplitude lines with their phases, and a comparison of the disk-cut Green kernels on the same insertions. These data would let the numerical bulk state, the local vacuum line and the ordinary unary Ward equation enter the same gluing formula.

The unary Ward identity compares a single insertion with the differential. To combine boundary states one also needs the singular coefficients \(a_{(n)}b\) of their field product and a coproduct that intertwines the fields on two modules. The level of a Heisenberg current under tensor product gives the first example in Chapter 12.

## Source manuscripts {#ch11-source-manuscripts}

### 1. A numerical Gaussian on the native source graph {#ref-ch11-01}

### 2. Finite action integrals from the original coefficient Riesz spaces {#ref-ch11-02}

### 3. The common relative determinant of the native contraction {#ref-ch11-03}

### 4. The original coefficient heat finite part and its based vacuum line {#ref-ch11-04}

### 5. The source counterterm in the covariant connection {#ref-ch11-05}

### 6. Ordinary boundary Ward identity and full-source heat cells {#ref-ch11-06}

The disk action and its transfer appear in *Harmonic fillings and mixed state correlations*, “The scalar filling and its state space” and “Scalar-cylinder sewing.” The two half-space constructions appear in *From holomorphic brackets to bulk fields*, “The supported bulk action,” in *Native cochains, supported fields, and harmonic fillings*, “Native annuli and all neutral fields,” and in *Chern–Simons observables, charged endpoints and chiral fusion*, Lemmas 3.2–3.4 and Theorem 4.1.
