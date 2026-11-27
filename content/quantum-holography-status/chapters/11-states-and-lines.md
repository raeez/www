# States, determinant lines and quantum fields

Suppose that a measurement on the boundary records a real coordinate \(x\). In a quadratic filling with stiffness \(\lambda>0\), the amplitude for a polynomial insertion \(P\) is
\[
 Z_\lambda(P)=\int_{\mathbb R}P(x)e^{-\lambda x^2/(2\hbar)}\,dx,
 \qquad Z_\lambda(1)=\sqrt{2\pi\hbar/\lambda},\qquad \hbar>0.
\]
Its normalized expectation is \(Z_\lambda(P)/Z_\lambda(1)\). Differentiating the density with respect to \(\lambda\) inserts \(-x^2/(2\hbar)\), giving
\[
 \frac{Z_\lambda(x^2)}{Z_\lambda(1)}
 =-2\hbar\,\partial_\lambda\log Z_\lambda(1)=\frac{\hbar}{\lambda}.
\]
Now put an independent quadratic coordinate \(y\) inside the filling. Give it stiffness \(\mu>0\) and integrate it with measure \(dy\). Its integral multiplies \(Z_\lambda(P)\) by \(\sqrt{2\pi\hbar/\mu}\) for *every* observable of \(x\). Quadrupling \(\mu\) halves the vacuum amplitude. Even knowledge of the entire probability law of \(x\) cannot detect the change. If we glue along \(x\), that factor multiplies the amplitude paired with the other filling. This is the normalization that the homogeneous Ward identity at the [end of the sewing calculation](10-analytic-sewing.md#ch10-two-completed-clusters) leaves free.

::: example {#ch11-two-coupled-gaussian-fillings title="Two fillings with the same boundary amplitude"}

Now couple the interior coordinate to the boundary. Keep the oriented coordinates \(x,y\) and their Lebesgue densities fixed. For a real coupling \(b\), prepare the action \(S_b(x,y)=\tfrac12\lambda x^2+\tfrac12\mu(y-bx)^2\). Integrating at fixed \(x\) produces the boundary amplitude
\[
 A_b(x)=\int_{\mathbb R}e^{-S_b(x,y)/\hbar}\,dy
        =\sqrt{2\pi\hbar/\mu}\,e^{-\lambda x^2/(2\hbar)} .
\]
The substitution \(y'=y-bx\) has unit Jacobian. Thus even the absolute amplitude \(A_b(x)\) is independent of \(b\). For example, a second filling with amplitude \(e^{-\lambda' x^2/(2\hbar)}\), \(\lambda'>0\), gives the same sewn vacuum \(2\pi\hbar/\sqrt{\mu(\lambda+\lambda')}\) for every \(b\) when we integrate the product against \(dx\). In the original filling the specified interior coordinate \(y\) has conditional mean \(bx\) at fixed \(x\). Therefore \(\langle xy\rangle_b=b\langle x^2\rangle_b=b\hbar/\lambda\). The two fillings with couplings \(b\) and \(-b\), \(b\ne0\), agree on every insertion at the cut and give opposite expectations for this mixed insertion. The coordinate reflection that exchanges their actions also reverses the specified interior probe. To compare the fillings on bulk observables one must say how the probe is identified.

:::

For several fields we must also say which density is carried from one filling to the next. Changing a basis rescales the even integration volume, and reversing two odd integration variables changes a sign. The determinant line records this change of coordinates. On the scalar disk, the action determines a probability law for boundary modes against which we can test the operations of a current. On a solid torus, finite integrals before division by the vacuum value also retain changes of absolute amplitude.

## Finite Gaussian integration and the determinant line {#ch11-finite-gaussian-integration-and-the-determinant-line}

Let \(C\) be a finite acyclic cochain complex, with differential of degree \(+1\). Its cotangent complex \(C\oplus C^*[-1]\) carries a nondegenerate pairing \(\mathcal B\) of degree \(-1\). A cyclic differential \(Q\) obeys the graded integration-by-parts identity for this pairing. If \(Q^2=0\), the quadratic action is

\[
S(\phi)=\frac12\mathcal B(\phi,Q\phi).
\]

Consider first two vectors with \(Qu=\sigma v\), \(Qv=0\) and \(\sigma\ne0\). Sending \(v\) to \(u/\sigma\) and \(u\) to zero gives a map \(R\) of degree \(-1\). On \(v\) the composite \(QR\) is the identity, and on \(u\) it is \(RQ\) that is the identity. On the paired complex we choose a cyclic contraction with \(QR+RQ=1\) and \(R^2=0\), compatible with the graded pairing \(\mathcal B\). Its image is the complex gauge subspace used below; the restricted action has the inverse induced by \(R\). To integrate, one must still specify a real cycle for the even variables and an order of extraction for the odd variables. This is the finite-dimensional geometry behind Batalin–Vilkovisky integration. [Schwarz, *Geometry of Batalin–Vilkovisky quantization*](https://arxiv.org/abs/hep-th/9205088).

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

Insert \(xy\) in either integral. In the odd integral the numerator is \(\hbar[xy](xy)=\hbar\), so division by the vacuum value \(\sigma\) gives \(\hbar/\sigma\). Reversing the insertion changes its sign. In the even integral \(xy=|w|^2/\sigma\) has the same mean \(\hbar/\sigma\), although its vacuum factor is \(1/\sigma\). Multiplication in the fixed interleaved order gives

\[
G_C=\prod_{j,\ell}\sigma_{j,\ell}^{\,(-1)^{j+1}}.
\]

This calculation retains the even orientation, the odd order and the density. An inverse Hessian determines the normalized Wick contractions; it does not determine these choices.

**Definition (determinant line).** For the complex \(C\), write \(\det C^j=\bigwedge^{\dim C^j}C^j\). The even-degree top exterior powers and the duals of the odd-degree ones form the line

\[
\operatorname{Det}C
=\bigotimes_j(\det C^j)^{(-1)^j}.
\]

For a single pair \(du=\sigma v\) in degrees zero and one, \(u\otimes v^\vee\) is a frame of \(\operatorname{Det}C\). Replacing \(u\) by \(a u\) and \(v\) by \(b v\) multiplies the frame by \(a/b\). The cotangent semidensity line in this construction is \((\operatorname{Det}C)^{-1}\). A semidensity transforms by the square root of the Berezinian, the graded analogue of a Jacobian. For a coefficient change \(A\), the cotangent lift has Berezinian \((\operatorname{Ber}A)^2\), and the transported semidensity acquires \((\operatorname{Ber}A)^{-1}\). The determinant-line description fixes this factor without an independent square-root choice. The continued orientation of the even cycle is retained in a separate flat line. Determinant lines also provide the setting for regularized determinants of elliptic operators; Quillen's construction is a basic example. [Quillen, *Determinants of Cauchy–Riemann operators over a Riemann surface*](https://link.springer.com/article/10.1007/BF01086022).

**Definition (normalized Gaussian state).** Divide the integral of a polynomial \(F\) by the vacuum integral on the same oriented cycle with the same odd order. If \(C_{\mathrm{Wick}}\) denotes the graded symmetric inverse-action contraction without its factor \(\hbar\), this ratio is

\[
\omega(F)=
\left[\exp\left(\frac{\hbar}{2}\partial_{C_{\mathrm{Wick}}}\right)F\right](0).
\]

Here \(\partial_C\) contracts two observable slots with \(C\); the exponential terminates on a polynomial. The unnormalized functional is \(Z(F)=G_C\omega(F)\). Consequently a state is the normalized linear functional \(\omega\), while an amplitude retains the factor and line in which \(G_C\) lives. Positivity is asserted for the actual even probability law when available; odd integration is algebraic Berezin extraction.

### The scalar disk and its collar {#ch11-harmonic-disk-and-collar}

Which Gaussian coordinates does a disk prepare? Mark the centre and angular coordinate of a Euclidean unit disk \(D\) and fix the constant mode of its real harmonic field at zero. For \(n\ge1\), the boundary mode \(e^{in\theta}\) extends harmonically as \(z^n\). Write its coefficient as \(Z_n/n\), so that the derivative of the holomorphic part has coefficient \(Z_n\) at \(z^{n-1}\). Reality supplies the conjugate modes. The field is therefore

\[
\phi=h+\bar h,\qquad h(z)=\sum_{n\ge1}Z_nz^n/n .
\]

At finite Fourier cutoff the disk assigns the amplitude \(e^{-S_D}\), where \(S_D=(8\pi)^{-1}\int_D|\nabla\phi|^2\,d^2z\). Since \(|\nabla\phi|^2=4|h'|^2\), the angular integral kills terms of unequal Fourier index. The integral of \(|z|^{2n-2}\) over the disk is \(\pi/n\), giving \(S_D=\frac12\sum_n |Z_n|^2/n\). Squaring the amplitude and normalizing against \(d^2Z_n\) gives independent circular complex Gaussians,

\[
d\mu=\bigotimes_{n\ge1}\frac{e^{-|Z_n|^2/n}}{\pi n}\,d^2Z_n .
\]

The factors have mass one, so removing a cutoff preserves every finite marginal. Almost every sample is harmonic in the open disk and has a distributional boundary value. The action defines this law by its finite-dimensional marginals even though a typical sample has infinite total Dirichlet energy.

To prepare an excited disk, multiply its ground amplitude by a holomorphic polynomial in finitely many \(Z_n\). Completing these polynomials in \(L^2(\mu)\) gives the disk Hilbert space. For the [level-one current](03-local-fields.md#heisenberg-current), the \(n\)th creation mode acts on Fock polynomials by multiplication by \(p_n\), and its adjoint acts by \(n\partial_{p_n}\). The substitution \(V:p_n\mapsto Z_n\) is unitary because on both sides the distinct occupation monomials are orthogonal and \(\|Z^{\boldsymbol m}\|^2=\prod_n n^{m_n}m_n!\). A norm-one amplitude \(F\) therefore gives a probability law \(|F|^2d\mu\) on the harmonic fillings.

The same scalar action on a cylinder of real length \(t\) gives a two-dimensional oscillator of frequency \(n\) and mass \(n^{-2}\) in each complex coordinate. Subtract its ground energy \(n\) before removing the cutoff. The ground-state transform of its heat kernel has mean \(q^n Z_n\) and variance \(n(1-q^{2n})\), where \(q=e^{-t}\). Thus for independent unit-variance circular Gaussians \(\xi_n\),

\[
(P_qG)(Z)=\mathbb E_\xi G\!\left(
  (q^n Z_n+\sqrt{n(1-q^{2n})}\,\xi_n)_{n\ge1}\right),
 \qquad 0<q\le1 .
\]

This is the Mehler semigroup for the independent complex oscillators. At zero length \(P_1\) is the identity. Every \(P_q\) fixes the constant function. In two successive collars the mean becomes \((qs)^n Z_n\) and the independent noises have total variance \(n(1-q^{2n})+q^{2n}n(1-s^{2n})=n(1-(qs)^{2n})\). Thus \(P_qP_s=P_{qs}\). On the holomorphic subspace it is \(q^{L_0}\), with \(L_0=\sum_{n\ge1} nZ_n\partial_{Z_n}\) on polynomials. On \(Z^{\boldsymbol m}\) the generator \(L_0\) has eigenvalue \(e=\sum_n n m_n\), the dimensionless oscillator grade. The collar \(P_q\) multiplies this monomial by \(q^e\). The amplitude with one cylinder inserted is \(\langle F,P_qG\rangle\).

### Measuring a relative phase from the half-space {#ch11-relative-phase}

Propagation by the collar multiplies both \(p_1^2\) and \(p_2\) by \(q^2\). To read the relative sign of their sum or difference we need an operation with a matrix entry between these occupations. Can an insertion in the interior supply the annihilation operator to go with boundary creation? Put a free current on the boundary of \(M=\mathbb R_{\ge0}\times D\), with \(t\) increasing into the interior and orientation \(dt\wedge dx\wedge dy\). The kinetic term pairs the field \(\Phi\) with its conjugate \(\eta\). The Hamiltonian operator \(\kappa\partial_z\) of the current bracket contributes the term quadratic in \(\eta\). With the tangential boundary condition, the action is

\[
S_\kappa=\tau_M\!\left(\eta D_M\Phi+\tfrac{\kappa}{2}\eta\partial_z\eta\right),
\qquad D_M=dt\,\partial_t+d\bar z\,\partial_{\bar z},
\qquad i^*\eta=0 .
\]

Here \(\tau_M\) integrates after wedging with \(dz/(2\pi i)\), and \(i^*\) is tangential restriction to the physical boundary. Choose numerical parameters with \(\hbar\kappa=1\). Regular observables have compact smooth joint kernels in each finite field number, with projective completion at fixed support and an algebraic sum over field numbers. The collar inclusion \(i_\hbar\) extends a boundary observable to the collar. The projection \(p_\hbar\) transfers regular collar observables back to the boundary, including their Wick contractions. They obey \(p_\hbar i_\hbar=1\). With the boundary trace \(\tau(\alpha)=(2\pi i)^{-1}\int_D dz\wedge\alpha\), integration by parts identifies the boundary binary differential on \(sf\,s\alpha\) with \(-\hbar\kappa\,\tau(f\partial_z\alpha)=\tau((\partial_z f)\alpha)\). The suspension \(s\) lowers degree by one. This identifies the regular current complexes together with their disjoint-support products.

Choose a compact radial cutoff \(\chi\) equal to one near the origin. The smooth forms \(\alpha_m=z^{-m}\bar\partial\chi\) share an annulus and have moments \(\tau(z^{j-1}\alpha_m)=\delta_{jm}\). Write \(I_B(p_m)=s\alpha_m\) and extend to polynomials by multiplication. These are closed boundary representatives. Their internal contractions vanish by angular weight, and the annular current \(b_{-n}\) acts on them as multiplication by \(p_n\).

To probe one mode from the interior, choose \(\chi_o=1\) on that annulus with compact support in \(D\), and a smooth normal profile \(\rho_j(t)dt\) of integral one strictly above the collar. In the collar convention \(\zeta^2=-1\) the test on the \(\Phi\) component is \(u_j=\zeta^{-1}\kappa\,s(\rho_jdt\,\chi_o z^{j-1}e_\Phi)\). Extend it by zero and multiply by the collar inclusion of a boundary observable. Projection gives

\[
\beta(u_j)v=p_\hbar\bigl(\operatorname{ext}(u_j)i_\hbar(v)\bigr),
\qquad \beta(u_j)I_B f=I_B\,\partial_{p_j}f .
\]

Indeed the linear projection of \(u_j\) vanishes. The mixed Wick contraction against the \(m\)-th annular factor is \(\hbar\kappa\,\tau(\chi_o z^{j-1}\alpha_m)=\delta_{jm}\). Summing over the slots of a monomial differentiates it. Thus the unit-strength bulk probe is \(\partial_{p_j}\), while the level-one current annihilation mode is \(J_j=j\partial_{p_j}\). Mere restriction of the interior test to \(t=0\) would give zero even on \(p_j\). The fixed compact probe distinguishes cochain representatives on the whole disk. Choose a radial cutoff \(\widetilde\chi\) equal to one on a disk containing the supports of \(\chi\) and \(\chi_o\), with its transition farther out. For \(m=j\) the two annular forms differ by \(\bar\partial[z^{-j}(\widetilde\chi-\chi)]\). The primitive is smooth and compactly supported. On a linear test the quantum differential has only its Dolbeault term, so the forms represent the same boundary class. The boundary Fock projection kills coboundaries and maps the unit to the nonzero vacuum. The original form pairs with \(\chi_o z^{j-1}\) to give one. The new form has support where \(\chi_o=0\) and gives zero. Thus this fixed slab does not act on whole-disk cohomology. On a subdisk where \(\chi_o=1\) the linear pairing is the holomorphic moment \(\tau(z^{j-1}\alpha)\). On linear whole-disk classes the boundary mode \(J_j\) reads \(j\tau(z^{j-1}\alpha)\) times the vacuum.

One interior test thus removes a quantum. To exchange two quanta of the first harmonic with one of the second, one needs both removal and creation. Take two copies \(u'_1,u''_1\) on disjoint ordered normal slabs. The successive operation \(2b_{-1}^2\beta(u_2)+b_{-2}\beta(u''_1)\beta(u'_1)\) acts on the chosen representatives by

\[
O=2p_1^2\partial_{p_2}+p_2\partial_{p_1}^2 .
\]

On the half-space take the closed cycles \(i_\hbar I_B((p_1^2\pm p_2)/2)\). On the disk take the two amplitudes \(F_\pm=(Z_1^2\pm Z_2)/2\) and measure the real, rotation-invariant function of the central field derivatives

\[
C=2\operatorname{Re}\bigl(h'(0)^2\overline{h''(0)}\bigr)
  =Z_1^2\bar Z_2+\bar Z_1^2Z_2 .
\]

Its operator on holomorphic states is the Toeplitz operator \(T_C\), multiplication by \(C\) followed by orthogonal projection. Gaussian integration by parts turns \(\bar Z_n\) under this projection into \(n\partial_{Z_n}\). The two indices in each term are distinct, so \(T_C=VOV^{-1}\) on polynomials. The vectors \(p_1^2,p_2\) are orthogonal and each has squared norm two. On their span write \(S\) for the operator exchanging the unit vectors \(p_1^2/\sqrt2\) and \(p_2/\sqrt2\). Then \(O=2S\), and the two prepared states are norm-one eigenvectors of \(S\) with eigenvalues \(\pm1\). Under the unitary \(V\) the Fock-space calculation gives \(\langle F_\pm,T_CF_\pm\rangle=\pm2\).

The disk probabilities give a direct check of what is measured. Put \(x=Z_1=h'(0)\) and \(y=Z_2=h''(0)\). Under the vacuum law \(\mu\) these are independent circular complex Gaussians with \(\mathbb E_\mu|x|^2=1\) and \(\mathbb E_\mu|y|^2=2\). The two preparations have densities relative to \(\mu\)
\[
 |F_\pm|^2=\tfrac14|x^2\pm y|^2
 =\tfrac14(|x|^4+|y|^2)\ \pm\ \tfrac12\operatorname{Re}(x^2\bar y).
\]
Their difference is \(R=\operatorname{Re}(x^2\bar y)\). It integrates to zero at fixed \(x\) by the circular symmetry of \(y\), and at fixed \(y\) by that of \(x\). Thus the two marginal distributions agree for each mode. To test the joint distribution, observe that \(x^2\bar y\) is circular and \(\mathbb E_\mu|x|^4=2\). Consequently
\[
 \mathbb E_\mu R^2=\tfrac12\mathbb E_\mu|x|^4\,\mathbb E_\mu|y|^2=2.
\]
The term \(R(|x|^4+|y|^2)\) has zero expectation by symmetry. The joint observable \(C=2R\) therefore has mean \(+2\) in \(|F_+|^2d\mu\) and \(-2\) in \(|F_-|^2d\mu\). A single measurement gives the value \(2\operatorname{Re}(x^2\bar y)\) for that filling, which varies with both boundary modes.

::: example {#ch11-squaring-the-disk-reading title="Squaring a reading on the disk"}

What does performing the boundary operation twice correspond to on the disk? Let \(\Pi\) project orthogonally onto holomorphic amplitudes. The operator \(T_C^2\) includes a projection between the two multiplications by \(C\), and \(T_C^2F_\pm=4F_\pm\). Squaring the number recorded on one filling uses the pointwise function \(C^2\). At fixed \(|x|,|y|\) its vacuum angular average is \(2|x|^4|y|^2\), and the term odd in \(R\) integrates to zero. Thus in each preparation
\[
 \int C^2 |F_\pm|^2\,d\mu
  =\tfrac12\left(\mathbb E_\mu|x|^8\,\mathbb E_\mu|y|^2+
                  \mathbb E_\mu|x|^4\,\mathbb E_\mu|y|^4\right)
  =\tfrac12(24\cdot2+2\cdot8)=32 .
\]
The variance of the dimensionless disk reading is \(32-4=28\). On these polynomials the difference between the two second moments is exactly \(\|(1-\Pi)CF_\pm\|^2\). This component leaves the holomorphic space after the first multiplication and is removed by the projection before the second boundary operation.

:::

Both amplitudes have oscillator grade two. Inserting a cylinder on one side of the field measurement propagates the holomorphic state after \(T_C\) has acted. The **one-sided** collar pairing and its normalization are consequently

\[
\langle F_\pm,P_qT_CF_\pm\rangle=\pm2q^2,\qquad
\langle F_\pm,P_qF_\pm\rangle=q^2 .
\]

Their ratio retains the measured value \(\pm2\) at every finite real collar. If instead we propagate the measured function \(C\), the two first-harmonic factors contribute \(q^2\) and the second-harmonic factor another \(q^2\). All terms containing the centered noise average to zero by independence and circular symmetry. Thus \(P_qC=q^4C\), whereas a single grade-two amplitude acquires \(q^2\).

Closing a collar by taking a trace makes a different preparation. Restrict both ends to the two-dimensional grade-two space \(\mathcal H_2\) and contract matching orthonormal states. On this space \(P_q=q^2I\), and \(O=2S\) has the two eigenvalues \(+2,-2\). Consequently
\[
 \operatorname{Tr}_{\mathcal H_2}(P_q O)=0,\qquad
 \operatorname{Tr}_{\mathcal H_2}(P_q O^2)=8q^2 .
\]
The trace of a single insertion loses its off-diagonal action on the two occupations. Keeping the seam open between two insertions lets the second undo the exchange, so both basis states contribute to the trace. Dividing by the empty trace \(2q^2\) gives the readings of the equal mixture. Inserting the projector onto \(F_+\) or \(F_-\) before closure gives the respective prepared-state reading above.

### Fermions on the boundary circle {#ch11-boundary-fermions}

The law \(\mu\) was obtained from the energy of a harmonic field in the disk. Particles on the boundary circle give finite-ring preparations \(F_\pm\) and a position measurement of \(C\). Their ground-state density waves reproduce a finite range of disk moments. The Gaussian law \(\mu\) arises in the limit of many particles.

Place \(N\) free fermions of mass \(m\) on a circle of circumference \(L\), without spin and with \(N\) odd. A particle at arc length \(y\) has the coordinate \(x=e^{2\pi iy/L}\) on the unit circle. For an integer \(j\), the function \(x^j\) is the state of momentum \(2\pi\hbar j/L\) and kinetic energy \((\hbar^2/2m)(2\pi/L)^2j^2\). A state of the \(N\) fermions is an antisymmetric function of \(x_1,\ldots,x_N\). In the ground state the momenta with \(|j|\le(N-1)/2\) are filled, and the wavefunction is the determinant of the corresponding functions \(x_a^j\). Writing \(d\theta_a/(2\pi)\) for normalized angular measure, the determinant has squared norm \(N!\). Up to phase its normalized wavefunction is
\[
\psi_0(x)=\frac{(x_1\cdots x_N)^{-(N-1)/2}}{\sqrt{N!}}\,\Delta_N(x),\qquad
\Delta_N(x)=\prod_{a<b}(x_a-x_b).
\]
{#eq-fermion-ground-state}
Distinct occupied momenta make the \(N!\) terms in the determinant orthogonal under product Haar probability. The resulting ground-state position law is
\[
 d\nu_N(x)=\frac{|\Delta_N(x)|^2}{N!}\prod_{a=1}^N\frac{d\theta_a}{2\pi},
 \qquad x_a=e^{i\theta_a}.
\]
It assigns mass one to all positions of the labelled coordinates together. Expectations of symmetric observables also describe the unlabelled configuration.

If \(f\) is a symmetric polynomial, then \(f\psi_0\) is again antisymmetric. It describes fermions which have been moved upward in momentum. The simplest symmetric polynomials are the power sums
\[
p_n(x)=x_1^n+\cdots+x_N^n=\sum_{a=1}^Ne^{2\pi iny_a/L},\qquad n\ge1 .
\]
Thus \(p_n(x)\) is a Fourier coefficient of the density of particles, and multiplying a wavefunction by it adds momentum \(2\pi\hbar n/L\). A polynomial \(F(p_1,p_2,\ldots)\) in the Fock space of the current now defines a state \(F(p(x))\,\psi_0(x)\) of the fermions. Multiplication by \(p_n\), which creates a quantum of the \(n\)th harmonic, becomes multiplication by a density wave. The weighted degree of \(p^\alpha\) is \(\sum_n n\alpha_n\), its added momentum in units of \(2\pi\hbar/L\). We call this the current energy when grading the Fock space. The physical kinetic energy of the particles will also depend on which momenta they occupy. Up to what weighted degree does substitution preserve inner products?

**Proposition (density waves of free fermions).** Let \(p^\alpha=\prod_np_n^{\alpha_n}\) and \(p^\beta=\prod_np_n^{\beta_n}\) be monomials of energies \(\sum_nn\alpha_n\le N\) and \(\sum_nn\beta_n\le N\). Then
\[
\int p^\alpha(x)\,\overline{p^\beta(x)}\,d\nu_N(x)
=\delta_{\alpha\beta}\prod_{n\ge1}n^{\alpha_n}\alpha_n!
=\mathbb E_\mu\bigl[Z^\alpha\,\overline{Z^\beta}\bigr].
\]
In particular the substitution \(F\mapsto F(p(x))\,\psi_0\) preserves the inner product on the span of the occupation monomials of weighted degree at most \(N\).

*Proof.* For a partition \(\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_N\ge0)\) the quotient
\[
s_\lambda(x)=\frac{\det\bigl(x_a^{\lambda_b+N-b}\bigr)_{a,b=1}^N}{\Delta_N(x)}
\]
is a symmetric polynomial, the Schur polynomial of \(\lambda\). The numerators for different partitions are determinants of different sets of momentum states. Hence \(\int s_\lambda\,\overline{s_{\lambda'}}\,d\nu_N=\delta_{\lambda\lambda'}\). Let \(p^\alpha\) have energy \(n\). The Frobenius formula is \(p^\alpha=\sum_\lambda\chi^\lambda(\alpha)\,s_\lambda\). The sum runs over the partitions of \(n\) with at most \(N\) rows, and \(\chi^\lambda(\alpha)\) is the value of the irreducible character \(\chi^\lambda\) of the symmetric group on \(n\) letters at a permutation with \(\alpha_k\) cycles of length \(k\). If \(n\le N\) every partition of \(n\) occurs. Monomials of different energies are then orthogonal. For equal energies the integral is \(\sum_\lambda\chi^\lambda(\alpha)\chi^\lambda(\beta)\). Orthogonality of the columns of the character table makes this \(\delta_{\alpha\beta}\prod_kk^{\alpha_k}\alpha_k!\), the number of permutations commuting with the given one. The Gaussian moments of \(\mu\) have the same value. ∎

Rotation of all \(x_a\) by a common phase makes monomials of unequal weights orthogonal at every \(N\). At common weight \(n\) the proof gives the exact finite-ring moment
\[
 \mathbb E_{\nu_N}\!\left[p^\alpha\overline{p^\beta}\right]
 =\sum_{\substack{\lambda\vdash n\\\ell(\lambda)\le N}}
       \chi^\lambda(\alpha)\chi^\lambda(\beta),
\]
where \(\ell(\lambda)\) is the number of rows. For the first density wave alone, \(\mathbb E_{\nu_N}|p_1|^{2n}\) is the sum of the squared dimensions of these representations. It equals \(n!\) through \(n=N\) and is strictly smaller thereafter. At \(n=N+1\) only the one-dimensional sign representation is missing, so the moment is \((N+1)!-1\). The bound \(|p_1|\le N\) also distinguishes its finite-ring law from the Gaussian.

The Schur polynomials, the Frobenius formula and the character relations are in I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I, Sections 3, 4 and 7.

As \(N\to\infty\) every joint moment of finitely many density waves is eventually given by the proposition. A Gaussian law is determined by its moments, so \(p_1(x),\ldots,p_k(x)\) converge in law to independent complex Gaussian variables with \(\mathbb E|Z_n|^2=n\). This is the theorem of Diaconis and Shahshahani on the traces of powers of a random unitary matrix, whose eigenvalues have the law \(\nu_N\) (*On the eigenvalues of random matrices*, J. Appl. Probab. 31A (1994), 49–62). The law \(\mu\) of the unexcited disk is therefore the limiting law of the density waves when the positions of the fermions are measured in their ground state. Fix a polynomial \(F\) of norm one in the disk law. Once \(N\) reaches its weighted degree, the state \(F(p(x))\,\psi_0\) has norm one, and the positions have law \(|F(p(x))|^2\,d\nu_N\). The joint laws of any fixed set of density waves converge to the corresponding marginals of \(|F(Z)|^2\,d\mu\). Indeed the fourth moments of \(F(p(x))\) eventually equal their disk value, so the squared amplitudes are uniformly integrable.

The harmonic field itself has a meaning for the particles. From a set of measured positions form, for \(|z|<1\),
\[
h(z)=\sum_{n\ge1}\frac{p_n(x)}{n}z^n=-\sum_{a=1}^N\log(1-zx_a),\qquad
\phi(z)=h(z)+\overline{h(z)}=-2\sum_{a=1}^N\log|z-\bar x_a| .
\]
{#eq-potential-of-the-fermions}
The field \(\phi\) is the logarithmic potential, at the interior point \(z\), of unit charges placed at the points \(\bar x_a\). The complex conjugate appears because adding momentum multiplies a wavefunction by \(x_a^n\), while the potential of a charge at \(x_a\) has the coefficients \(\bar x_a^{\,n}\). Conjugation only reverses the direction around the circle. One finite configuration gives this potential. On every smaller closed disk the random ground-state potential converges in law in the uniform norm to the harmonic disk field. Indeed the character of an \(n\)-cycle is \((-1)^j\) on a hook \((n-j,1^j)\) and zero on the other diagrams. The finite character sum therefore gives \(\mathbb E_{\nu_N}|p_n|^2=\min(n,N)\). On \(|z|\le r<1\) the expected supremum of the holomorphic tail after harmonic \(k\) is at most \(\sum_{n>k}r^n/\sqrt n\), uniformly in \(N\).

In the state \(u_\pm=(p_1^2\pm p_2)/2\) the wavefunction is \(\tfrac12\bigl(p_1(x)^2\pm p_2(x)\bigr)\psi_0(x)\). Measure all the positions and compute \(C=2\operatorname{Re}\bigl(p_1(x)^2\,\overline{p_2(x)}\bigr)\). In the integral of \(C\,|u_\pm|^2\), each monomial has weighted degree four in the holomorphic variables and four in their conjugates. Once \(N\ge4\) (hence \(N\ge5\) on the odd ring used here), the finite-ring mean is exactly \(\pm2\). The reading of the introduction is a function of the measured positions, the same function for both preparations. The first density wave alone also distinguishes these preparations at finite \(N\). For odd \(N\ge3\), both states have norm one. Their expectations of \(|p_1|^{2r}\), in the order \(u_+,u_-\), differ by \(\operatorname{Re}\mathbb E_{\nu_N}[p_1^{r+2}\overline{p_1^r p_2}]\). This difference is zero for \(r+2\le N\). At \(r=N-1\) the omitted sign character takes the values \(1,-1\) on the identity and a transposition, so the difference is \(1\).

How far do the positions determine a state when \(N\) is finite? On the unit circle \(\overline{p_1(x)}=x_1^{-1}+\cdots+x_N^{-1}\). The elementary symmetric polynomial \(e_{N-1}(x)=x_1\cdots x_N\,\overline{p_1(x)}\) therefore has the same absolute value as \(p_1(x)\). The states \(p_1\psi_0\) and \(e_{N-1}\psi_0\) give the same law of positions.

For odd \(N\ge3\), these two states even have different added momenta, \(1\) and \(N-1\) in units of \(2\pi\hbar/L\). Their position laws agree because the factor \(x_1\cdots x_N\) has absolute value one. The [disk reconstruction theorem](#ch11-recovering-a-state-from-the-disk) uses the joint law of arbitrarily many limiting harmonics.

For odd \(N\ge3\), take the density-wave states \(F\psi_0\) with \(F\) a homogeneous symmetric polynomial of degree \(n\). The added momentum is \(n\) in units of \(2\pi\hbar/L\). On this polynomial subspace the full position law determines every density matrix when \(0\le n<N\). Use the basis of products of elementary symmetric functions \(e_j\), with total degree \(n\), and write \(D=e_N\). The rank-one operators \(|F\rangle\langle G|\) for pairs of these basis monomials form a basis of all operators. Extending the position measurement linearly from positive operators, their densities relative to the ground law are \(F\overline G\). On the unit circle \(\overline{e_j}=e_{N-j}/D\). Distinct Laurent monomials in \(e_1,\ldots,e_{N-1},D\) are independent on the torus, since multiplication by a power of \(D\) reduces the assertion to independence of the elementary symmetric generators. Suppose two of these products give the same monomial. All indices are below \(N\), so the power of \(D\) fixes the length of the conjugated list. The total number of numerator factors then fixes the length of the first list. Cancel the common entries of the two first lists. If \(k\) entries of total degree \(m\) remain on either side, their complementary entries must occur in the conjugated lists in the other assignment to the same numerator. Thus \(m\le n\) and \(kN-m\le n\). The inequality \(kN\le2n<2N\) leaves at most one entry, and a single entry of the same degree on each side would already have cancelled. Hence the law recovers every coefficient of the density operator.

At grade \(N\), put \(A=e_1e_{N-1}-D=D(|p_1|^2-1)\). The Schur functions \(D=s_{(1^N)}\) and \(A=s_{(2,1^{N-2})}\) give orthonormal Slater states. The two orthogonal states \((D+iA)\psi_0/\sqrt2\) and \((D-iA)\psi_0/\sqrt2\) have equal position densities since \(\bar D A\) is real. Multiplying both polynomials by \(e_1^{n-N}\) and normalising gives distinct states with identical laws at every \(n>N\).

### The exchange at every energy {#ch11-cubic-observable}

The kinetic energy of the fermions is \(K=(\hbar^2/2m)(2\pi/L)^2\sum_aD_a^2\), where \(D_a=x_a\,\partial/\partial x_a\) reads the momentum of particle \(a\) in units of \(2\pi\hbar/L\). How does it act on the states \(F(p(x))\,\psi_0\)? On polynomials in \(p_1,p_2,\ldots\) let
\[
E=\sum_{n\ge1}np_n\frac{\partial}{\partial p_n},\qquad
W=\frac12\sum_{i,j\ge1}\Bigl((i+j)\,p_ip_j\frac{\partial}{\partial p_{i+j}}
 +ij\,p_{i+j}\frac{\partial^2}{\partial p_i\,\partial p_j}\Bigr).
\]
{#eq-cut-and-join}
The operator \(E\) counts added momentum in integer units. In \(W\), the first term splits a harmonic of index \(i+j\) into two of indices \(i,j\), and the second joins them. Both preserve the eigenvalue of \(E\). This is the [cubic observable of Chapter 1](01-physical-questions.md#eq-cubic-observable), written with \(J_{-n}=p_n\) and \(J_n=n\,\partial/\partial p_n\).

**Proposition (kinetic energy in the density waves).** For every polynomial \(F\),
\[
\sum_{a=1}^ND_a^2\,\bigl(F(p(x))\,\psi_0\bigr)
=\bigl((2W+NE+c_N)F\bigr)(p(x))\,\psi_0,
\qquad c_N=\frac{N(N^2-1)}{12}.
\]
Consequently \(K\) acts on these states as \(K_0+\varepsilon_1\bigl(E+\tfrac2NW\bigr)\). Here \(K_0\) is the energy of the ground state and \(\varepsilon_1=(\hbar^2/2m)(2\pi/L)^2N=2\pi\hbar v_F/L\), with \(v_F=\pi\hbar N/(mL)\) the slope of the kinetic energy halfway between the highest occupied momentum \(\pi\hbar(N-1)/L\) and the next allowed momentum \(\pi\hbar(N+1)/L\). Since the kinetic energy is quadratic, raising the last fermion by one step costs exactly \(\varepsilon_1\). At fixed density \(N/L\), the velocities at both momenta tend to \(v_F\) as \(L\) grows.

*Proof.* Since \(D_ap_n(x)=nx_a^n\), the chain rule gives \(\sum_aD_aF=EF\) and
\[
\sum_aD_a^2F=\sum_nn^2p_n\frac{\partial F}{\partial p_n}
 +\sum_{i,j}ij\,p_{i+j}\frac{\partial^2F}{\partial p_i\,\partial p_j}.
\]
Next \(D_a\Delta_N=\Delta_N\sum_{b\ne a}x_a/(x_a-x_b)\). Collecting the pairs \(a<b\),
\[
\sum_a\frac{D_a\Delta_N}{\Delta_N}\,D_aF
=\sum_nn\frac{\partial F}{\partial p_n}\sum_{a<b}\frac{x_a^{n+1}-x_b^{n+1}}{x_a-x_b},
\qquad
\sum_{a<b}\frac{x_a^{n+1}-x_b^{n+1}}{x_a-x_b}
=\Bigl(N-\frac{n+1}2\Bigr)p_n+\frac12\sum_{i+j=n}p_ip_j .
\]
Each term of \(\Delta_N\) is a monomial with the exponents \(0,1,\ldots,N-1\) in some order. Therefore \(\sum_aD_a\Delta_N=\tfrac12N(N-1)\Delta_N\) and \(\sum_aD_a^2\Delta_N=\tfrac16N(N-1)(2N-1)\Delta_N\). Adding the three contributions to \(\sum_aD_a^2(F\Delta_N)\),
\[
\frac1{\Delta_N}\sum_aD_a^2\,(F\Delta_N)
=\Bigl(2W+(2N-1)E+\tfrac16N(N-1)(2N-1)\Bigr)F .
\]
The factor \((x_1\cdots x_N)^{-(N-1)/2}\) in \(\psi_0\) replaces each \(D_a\) by \(D_a-\tfrac12(N-1)\). Expanding the square and using \(\Delta_N^{-1}\sum_aD_a(F\Delta_N)=\bigl(E+\tfrac12N(N-1)\bigr)F\) leaves the coefficient \(2N-1-(N-1)=N\) of \(E\) and the constant \(c_N\). ∎

Fix the added momentum \(E=n\). The linear term raises every energy on this subspace by \(\varepsilon_1 n\). Any splitting comes from \(W\), whose coefficient \(2\varepsilon_1/N\) is fixed by the curvature \(\hbar^2/m\) of the kinetic energy as a function of wave number. We already have states of definite kinetic energy. Multiplying the ground state by a Schur polynomial gives a determinant of occupied momenta. Reading their energies will diagonalize \(W\).

**Theorem (the spectrum of the cubic observable).** Let \(\lambda\) be a partition of \(n\), and let \(s_\lambda\) be the polynomial in \(p_1,\ldots,p_n\) which becomes the Schur polynomial \(s_\lambda(x)\) in any number \(N\ge n\) of variables. Then
\[
W\,s_\lambda=c(\lambda)\,s_\lambda,\qquad
c(\lambda)=\sum_{(i,j)\in\lambda}(j-i)=\frac12\sum_i\lambda_i(\lambda_i-2i+1),
\]
where \((i,j)\) runs over the boxes of the Young diagram of \(\lambda\), in row \(i\) and column \(j\). The \(s_\lambda\) with \(\lambda\) a partition of \(n\) form an orthonormal basis of the states of energy \(n\). On that space \(W\) is symmetric, with norm \(n(n-1)/2\).

*Proof.* Take \(N\ge n\) odd. The power sums \(p_1(x),\ldots,p_N(x)\) are algebraically independent, so the substitution is injective on polynomials of energy at most \(N\). By the proposition on density waves it preserves their inner products. It therefore suffices to work with the functions of \(x\). The Vandermonde denominator in the Schur polynomial cancels against the [ground state](#eq-fermion-ground-state), giving the normalized Slater determinant
\[
 s_\lambda(x)\psi_0(x)=\frac{1}{\sqrt{N!}}\det(x_a^{k_b})_{a,b=1}^N,
\]
where \(k_b=\lambda_b-b+\tfrac12(N+1)\). Each permutation term has the same sum of squared momenta, so \(\sum_aD_a^2\) multiplies the determinant by \(\sum_bk_b^2\). Subtracting the value for the empty partition and comparing with the preceding proposition gives
\[
2c(\lambda)+Nn=\sum_b\bigl(k_b^2-(k_b-\lambda_b)^2\bigr)=\sum_b\lambda_b(\lambda_b-2b+1)+Nn .
\]
Row \(i\) of the diagram contributes \(\sum_{j\le\lambda_i}(j-i)=\tfrac12\lambda_i(\lambda_i-2i+1)\) to the sum over boxes. Under product Haar probability the \(N!\) permutation monomials in each determinant are orthogonal and have norm one. Distinct partitions give different sets of occupied momenta, so the normalized determinants are orthonormal. The largest value of \(|c(\lambda)|\) is \(n(n-1)/2\), attained by a single row and by a single column. ∎

In combinatorics \(W\) is the cut-and-join operator of Goulden and Jackson (*Transitive factorisations into transpositions and holomorphic mappings on the sphere*, Proc. Amer. Math. Soc. 125 (1997), 51–60), and \(c(\lambda)\) is the content of the diagram. The description by fermions is that of A. Okounkov, *Toda equations for Hurwitz numbers*, Math. Res. Lett. 7 (2000), 447–453.

In the state \(s_\lambda\psi_0\) the fermions occupy the momenta \(k_b\). Measured from the middle of the gap above the filled momenta these are the half-integers \(\kappa_i=\lambda_i-i+\tfrac12\), and the ground state has \(\kappa_i=-i+\tfrac12\). The theorem says that
\[
n=\sum_i\Bigl(\kappa_i-\bigl(-i+\tfrac12\bigr)\Bigr),\qquad
2c(\lambda)=\sum_i\Bigl(\kappa_i^2-\bigl(-i+\tfrac12\bigr)^2\Bigr),
\]
{#eq-momentum-and-curvature}
and that the excitation energy is \(\varepsilon_1\bigl(n+2c(\lambda)/N\bigr)\). At \(n=2\) the row \((2)\) is \(u_+\). One fermion has been raised from \(\kappa=-\tfrac12\) to \(\kappa=\tfrac32\). The column \((1,1)\) is \(u_-\), in which one fermion has been raised from \(-\tfrac32\) to \(\tfrac12\). Both add two units of momentum. Their energies differ by \(4\varepsilon_1/N\) because the kinetic energy is curved.

For the density waves this is the splitting of a degenerate level by a cubic coupling. Neither two quanta of the first harmonic nor one quantum of the second is a stationary state. The stationary states are their sum and their difference, and an energy measurement which resolves the splitting measures the exchange \(S\) of the introduction.

The formula is exact for free fermions with kinetic energy \(\hbar^2k^2/2m\). A diagram with more than \(N\) rows gives \(s_\lambda(x)=0\), since there are only \(N\) fermions to raise. Thus the character of the polynomial density waves, graded by their added momentum \(n=|\lambda|\), is \(\sum_{\ell(\lambda)\le N}q^{|\lambda|}=\prod_{j=1}^N(1-q^j)^{-1}\) by transposition of diagrams. It agrees with the current character through degree \(N\). At degree \(N+1\) the column \((1^{N+1})\) is missing.

At fixed \(n\) a kinetic-energy measurement reads \(c(\lambda)\) from the known shift \(\varepsilon_1 n\). Across degrees a single kinetic energy can have different cubic readings. For odd \(N\ge3\), the row \((1)\) moves the highest occupied orbital up one step, and the column \((1^N)\) moves the entire filled sea up one step. Both cost the first gap \(\varepsilon_1\). Their added momenta are \(1,N\) in units of \(2\pi\hbar/L\), and their cubic readings are \(0,-N(N-1)/2\), respectively.

In interacting one-dimensional liquids the density-wave velocity and the cubic coupling can depend on the interaction. For the spinless fermions above, for example, the wavefunction vanishes when two positions coincide, so an ordinary two-body contact interaction has zero matrix element. Decay into several excitations requires a nonzero matrix element to a final state of the same energy and momentum. These conditions enter the theory of one-dimensional quantum liquids beyond the linear approximation (A. Imambekov, T. L. Schmidt and L. I. Glazman, *One-dimensional quantum liquids: beyond the Luttinger liquid paradigm*, Rev. Mod. Phys. 84 (2012), 1253). The Schur description also occurs at the edge of an integer quantum Hall droplet. There the electrons fill successive angular momenta, and the symmetric polynomials multiply the wavefunction of the filled droplet (M. Stone, *Schur functions, chiral bosons, and the quantum-Hall-effect edge states*, Phys. Rev. B 42 (1990), 8399).

Is this one observable enough to tell all the states \(s_\lambda\) apart? For each fixed \(n\le5\) the numbers \(c(\lambda)\) are distinct. At \(n=6\),
\[
c(4,1,1)=c(3,3)=3,\qquad c(3,1,1,1)=c(2,2,2)=-3 .
\]
The fermions show what to measure next. Every sum \(\sum_aD_a^r\) of powers of their momenta is diagonal on the determinants \(s_\lambda\psi_0\). After its value in the ground state is subtracted, its eigenvalue is a polynomial in \(N\) whose coefficients are multiples of the numbers
\[
M_r(\lambda)=\sum_i\Bigl(\kappa_i^{\,r}-\bigl(-i+\tfrac12\bigr)^r\Bigr),\qquad\kappa_i=\lambda_i-i+\tfrac12 .
\]
{#eq-momentum-moments}
By the two formulas above, \(M_1=n\) and \(M_2=2c(\lambda)\). The third of these numbers separates the diagrams which \(W\) confuses: \(M_3(4,1,1)=\tfrac{117}2\) and \(M_3(3,3)=\tfrac{45}2\).

::: figure fig-schur-readings

**Proposition (the momenta are a complete measurement).** The sequence \(M_1(\lambda),M_2(\lambda),M_3(\lambda),\ldots\) determines the partition \(\lambda\).

*Proof.* In the series \(\sum_rM_r(\lambda)t^r/r!=\sum_i\bigl(e^{t\kappa_i}-e^{t(-i+1/2)}\bigr)\) all but finitely many terms cancel. What remains is \(\sum_{\kappa\in A}e^{t\kappa}-\sum_{\kappa\in B}e^{t\kappa}\), where \(A\) is the set of occupied positive half-integers and \(B\) the set of unoccupied negative ones. Exponential functions with distinct exponents are linearly independent. The series therefore determines \(A\) and \(B\), and these determine \(\lambda\). ∎

Let \(M_r\) also denote the operator on the current Fock space with \(M_rs_\lambda=M_r(\lambda)s_\lambda\). In the boson–fermion correspondence these vacuum-subtracted momentum sums are angular zero modes of local polynomials in the cylinder current and its derivatives, of highest current degree \(r+1\) (V. Kac, *Vertex Algebras for Beginners*, second edition, Chapter 5). To take the grade-preserving mode of a homogeneous plane field \(A(z)\) of weight \(h\), take the constant Fourier coefficient of \(z^h A(z)\) on a circle. In the cylinder coordinate \(w=\log z\), the contour has differential \(dw=dz/z\). The corresponding plane residue is therefore \(\operatorname{Res}_{z=0}z^{h-1}A(z)\,dz\).

For the [neutral level-one current](03-local-fields.md#heisenberg-current) write \(J(z)=\sum_n J_nz^{-n-1}\), with \(J_0=0\). Normal ordering places all creation modes on the left. The two moments used here are
\[
\begin{aligned}
M_1=E  &=\tfrac12\operatorname{Res}_{z=0} z\,{:J(z)^2:}\,dz,\\
M_2=2W &=\tfrac13\operatorname{Res}_{z=0} z^2\,{:J(z)^3:}\,dz .
\end{aligned}
\]
{#eq-current-momentum-zero-modes}
The weights select mode indices with sum zero. In the square the indices \(n,-n\) occur in two orders. In the cube there are three positions for the index of opposite sign, leaving the ordered pair \(i,j>0\) in the [cut-and-join formula](#eq-cut-and-join). The plane translation \(T\) detects the weights too. An unweighted residue commutes with \(T\) because \([T,A(z)]=\partial_z A(z)\). Here \(Tp_1=p_2\), while \([E,T]p_1=p_2\) and \([2W,T]p_1=2p_1^2\).

Measuring all the \(M_r\) together amounts to measuring the momentum of every fermion. It distinguishes any two of the states \(s_\lambda\) with certainty. For a general preparation these measurements give the diagonal entries of its density operator in the basis \(s_\lambda\).

The mean of the cubic observable can also be obtained by sampling the harmonic field. On a circle of radius \(0<r<1\) put \(g_r(\theta)=re^{i\theta}h'(re^{i\theta})=\sum_nZ_nr^ne^{in\theta}\). Then \(r\,\partial_r\phi=2\operatorname{Re}g_r\) and \(\partial_\theta\phi=-2\operatorname{Im}g_r\), so that
\[
\Phi_r=\int_0^{2\pi}\operatorname{Re}\bigl(g_r^{\,2}\,\overline{g_r}\bigr)\frac{d\theta}{2\pi}
=\frac{r^3}{8}\int_0^{2\pi}|\nabla\phi|^2\,\partial_r\phi\;\frac{d\theta}{2\pi}.
\]
{#eq-cubic-disk-observable}
This is the average over the circle of the squared gradient of the field times its outward derivative. Integration over the angle keeps the terms of \(g_r^{\,2}\,\overline{g_r}\) whose frequencies cancel:
\[
\Phi_r=\frac12\sum_{i,j\ge1}r^{2(i+j)}\bigl(Z_iZ_j\overline{Z_{i+j}}+\overline{Z_iZ_j}\,Z_{i+j}\bigr).
\]
Almost every sample has \(|Z_n|\le n\) for all large \(n\), so the series converges. Let \(W_r\) be obtained from \(W\) by multiplying its terms with indices \(i,j\) by \(r^{2(i+j)}\).

**Theorem (the cubic observable on the disk).** For a unit vector \(F\) supported on finitely many oscillator grades,
\[
\int\Phi_r\,|F(Z)|^2\,d\mu=\langle F,W_rF\rangle\longrightarrow\langle F,WF\rangle\qquad(r\uparrow1).
\]
More generally let \(\rho\) be a positive trace-class operator of trace one on the completed Fock space. If \(\rho=\sum_j\lambda_j|F_j\rangle\langle F_j|\) in unit eigenvectors, its disk law is \(d\nu_\rho=\sum_j\lambda_j|F_j(Z)|^2d\mu\). A real collar acting on both sides, with \(0<q<1\), prepares \(\rho_q=q^E\rho\,q^E/\operatorname{Tr}(\rho\,q^{2E})\). Then \(\Phi_r\) is integrable for the law \(\nu_{\rho_q}\) of the state \(\rho_q\), and
\[
\lim_{r\uparrow1}\int\Phi_r\,d\nu_{\rho_q}=\operatorname{Tr}(\rho_qW).
\]
In particular \(\int\Phi_r\,|F_\pm|^2\,d\mu=\pm r^4\).

*Proof.* Under projection onto holomorphic polynomials, \(\overline{Z_n}\) becomes \(n\,\partial/\partial Z_n\), placed to the left of the multiplications. The index \(i+j\) differs from \(i\) and from \(j\). The compression of each term of \(\Phi_r\) is therefore the corresponding term of \(W_r\) under \(p_n\mapsto Z_n\). To sum the series, let \(F\) have energy \(e\) and put \(k=i+j\). Since \(|\overline{Z_k}|=|Z_k|\) and multiplication by \(Z_n\) has norm at most \(\sqrt{e'+n}\) on states of energy \(e'\),
\[
\bigl\|Z_iZ_j\overline{Z_k}\,F\bigr\|_{L^2(\mu)}=\bigl\|Z_iZ_jZ_kF\bigr\|\le(e+2k)^{3/2}\|F\|\le(2k)^{3/2}(e+1)^{3/2}\|F\| .
\]
The products with \(F\) of different energies are orthogonal. For every \(F\) in the domain of \((E+1)^{3/2}\) the series \(\Phi_rF\) then converges in \(L^2(\mu)\), with
\[
\|\Phi_rF\|_{L^2(\mu)}\le C_r\,\bigl\|(E+1)^{3/2}F\bigr\|,\qquad C_r=\sum_{k\ge2}(k-1)(2k)^{3/2}r^{2k}<\infty .
\]
This proves the first equality. On states of energy \(e\) only the terms with \(i+j\le e\) act, so \(W_r\) converges to \(W\) there.

For the second statement write \(\rho_q=\sum_j\lambda_j|F_j\rangle\langle F_j|\). The weight of \(\rho_q\) on energy \(e\) is at most \(q^{2e}/\operatorname{Tr}(\rho\,q^{2E})\), so \(\operatorname{Tr}\bigl(\rho_q(E+1)^3\bigr)<\infty\). The bound on \(\Phi_rF\) and the Cauchy–Schwarz inequality give \(\int|\Phi_r|\,d\nu_{\rho_q}\le C_r\operatorname{Tr}\bigl(\rho_q(E+1)^3\bigr)^{1/2}\) and \(\int\Phi_r\,d\nu_{\rho_q}=\operatorname{Tr}(\rho_qW_r)\). In the basis of monomials \(W\) has nonnegative entries, and those of \(W_r\) lie between zero and the entries of \(W\). For symmetric matrices this gives \(\|W_r\|\le\|W\|=e(e-1)/2\) on energy \(e\), uniformly in \(r\). Summation over \(e\) against the weights of \(\rho_q\) is therefore dominated, and the limit follows. On energy two, \(W_r=r^4W\) and \(WF_\pm=\pm F_\pm\). ∎

The means of the two preparations approach the exchange eigenvalues \(+1\) and \(-1\). What happens to a reading on a single filling as the circle approaches the boundary? The vacuum already exhibits fluctuations that grow without bound.

::: proposition {#ch11-proposition-boundary-fluctuations-of-the-cubic-disk-observable}

**Proposition (boundary fluctuations of the cubic disk observable).** Take \(\Phi_r,\Phi_s\) on the same filling, at radii \(0<r,s<1\). Under the vacuum law \(\mu\) they have mean zero and
\[
 \operatorname{Cov}_\mu(\Phi_r,\Phi_s)
 =\frac{2x^2(1+x)}{(1-x)^5},\qquad x=(rs)^2 .
\]
{#eq-cubic-disk-covariance}
For every fixed probability law \(\nu\) absolutely continuous with respect to \(\mu\), and every fixed \(H>0\),
\[
 \lim_{r\uparrow1}\ \sup_{a\in\mathbb R}
       \nu\bigl(|\Phi_r-a|\le H\bigr)=0 .
\]
{#eq-cubic-disk-escape}

:::

::: proof {#ch11-proof-cubic-disk-fluctuations}

Group the ordered pairs in the [circle reading](#eq-cubic-disk-observable) by their total index \(k\). Write \(U_k=\overline{Z_k}\sum_{i=1}^{k-1}Z_iZ_{k-i}\), so that \(\Phi_r=\sum_{k\ge2}r^{2k}\operatorname{Re} U_k\). Rotating every \(Z_n\) by the same phase shows that \(\mathbb E_\mu U_k=\mathbb E_\mu(U_kU_\ell)=0\). For \(k>\ell\), the mode \(Z_k\) occurs just once in \(U_k\overline{U_\ell}\), so that expectation vanishes too. At fixed \(k\), the two Gaussian pairings of the lower indices contribute equally, including when \(i=k-i\). Taking the real part gives
\[
 \mathbb E_\mu[(\operatorname{Re} U_k)^2]
 =\tfrac12\mathbb E_\mu|U_k|^2
 =k\sum_{i=1}^{k-1}i(k-i)=\frac{k^2(k^2-1)}{6}.
\]
Thus the first two contributions to the variance are \(2r^8\) and \(12r^{12}\). The orthogonal series converges in \(L^2(\mu)\) at every interior radius. Its covariance at \(r,s\) is the sum of \(k^2(k^2-1)x^k/6\) over \(k\ge2\). Summing by differentiation of the geometric series gives the stated formula. On taking \(s=r\), the variance diverges as \(r\uparrow1\), which precludes an \(L^2(\mu)\) limit.

To estimate the probability of an interval, leave the first harmonic unintegrated. The two placements of index \(1\) give
\[
\begin{aligned}
 \Phi_r&=D_r+\operatorname{Re}(Z_1 A_r)
           +r^4\operatorname{Re}(Z_1^2\overline{Z_2}),\\
 A_r&=2\sum_{j\ge2}r^{2j+2}Z_j\overline{Z_{j+1}},
\end{aligned}
\]
where \(D_r\) uses only modes of index at least two. The size of \(A_r\) can be tested with one high harmonic. Set \(m=\lfloor(1-r)^{-1}\rfloor\), taking \(r\) close enough to one that \(m\ge4\). Conditional on all modes except \(Z_m\), the real part of \(A_r\) is a fixed real number plus \(2\operatorname{Re}(\overline{Z_m}B_r)\), where
\[
 B_r=r^{2m}Z_{m-1}+r^{2m+2}Z_{m+1}.
\]
The conditional standard deviation is \(\sqrt{2m}|B_r|\). Under \(\mu\), \(B_r\) is a circular Gaussian with mean square \(v_r=(m-1)r^{4m}+(m+1)r^{4m+4}\). Since \(r^m\to e^{-1}\), \(v_r/m\) stays bounded above and away from zero. A real Gaussian density is bounded by the reciprocal of \(\sqrt{2\pi}\) times the reciprocal of its standard deviation. Integrating this bound over the other modes, using \(\mathbb E_\mu|B_r|^{-1}=\sqrt{\pi/v_r}\) by polar integration, gives \(\mu(|A_r|\le L)\le C L/m\) for \(L>0\), with \(C\) independent of \(r\) near one.

Now condition on the modes of index at least two. On \(|A_r|>L\), the real Gaussian \(\operatorname{Re}(Z_1A_r)\) has density at most \(1/(\sqrt{\pi}L)\). On \(|Z_1|,|Z_2|\le K\), the quadratic term in \(Z_1\) has absolute value at most \(K^3\). Thus a reading in \([a-H,a+H]\) forces the linear term into an interval of length at most \(2(H+K^3)\) after the fixed offset \(D_r\) is removed. For any centre \(a\) this gives
\[
\begin{aligned}
 \mu(|\Phi_r-a|\le H)
 &\le \mu\bigl(\max(|Z_1|,|Z_2|)>K\bigr)\\
 &\quad{}+CL/m+2(H+K^3)/(\sqrt{\pi}L).
\end{aligned}
\]
Take \(L=\sqrt m\) and let \(r\uparrow1\), then \(K\to\infty\). The bound tends to zero uniformly in \(a\). For a fixed \(\nu\ll\mu\), its density is integrable, so sets of sufficiently small \(\mu\)-probability also have arbitrarily small \(\nu\)-probability. This proves the assertion for the prepared laws as well.

:::

In particular \(|\Phi_r|\to\infty\) in probability under the vacuum and under either preparation. The laws of the raw readings are not tight, so the readings have no finite limit in distribution or in probability. Subtracting the prepared mean \(\pm r^4\) only moves the centre of the interval in the proposition. Dividing instead by the vacuum standard deviation gives a different normalization, with unit vacuum variance and prepared means tending to zero.

### Recovering a state from the disk {#ch11-recovering-a-state-from-the-disk}

The marked disk gives a complex amplitude \(Z_n\) for each harmonic mode. The joint distribution of the first two distinguishes \(F_+\) from \(F_-\). How much of a preparation can we recover from the joint law of all the \(Z_n\)? For a measurable event \(A\) in the space of fillings, compress multiplication by its indicator to the holomorphic space, obtaining \(T_{\mathbf1_A}\). The event has probability \(\operatorname{Tr}(\rho T_{\mathbf1_A})\). This is \(\sum_j\lambda_j\int_A|F_j|^2d\mu\) in any mixture realizing \(\rho\).

**Theorem (recovering a density operator from its filling law).** For the neutral free current at level one on the marked disk, the map \(\rho\mapsto\nu_\rho\) is injective on positive trace-class operators of trace one. Each finite set of harmonics determines a reduced density operator. Taking successively more harmonics recovers the matrix entries of \(\rho\).

First retain the measured values \(z=(z_1,\ldots,z_N)\) of the first \(N\) modes. Integrating out the remaining modes gives the law of the reduced operator \(\rho_N\), the partial trace of \(\rho\). An \(N\)-mode amplitude \(f\) has value \(f(z)=\langle K_z,f\rangle\), where \(K_z(w)=\exp(\sum_{n=1}^N\bar z_n w_n/n)\). Thus the marginal density relative to the first \(N\) vacuum Gaussians is \(D_N(z)=\langle K_z,\rho_N K_z\rangle\). Expanding the kernel in the normalized occupation basis \(e_\alpha(z)=z^\alpha/s_\alpha\) gives

\[
D_N(z)=\sum_{\alpha,\beta}
\frac{\langle e_\alpha,\rho_N e_\beta\rangle}{s_\alpha s_\beta}
  z^\alpha\bar z^\beta,\qquad
s_\alpha^2=\prod_{n=1}^N n^{\alpha_n}\alpha_n!.
\]

Cauchy–Schwarz bounds the absolute sum by the Hilbert–Schmidt norm of \(\rho_N\) times \(\|K_z\|^2=\exp(\sum_{n=1}^N|z_n|^2/n)\), uniformly on compact sets. The Gaussian gives positive measure to every nonempty open set, so the marginal law fixes this continuous density everywhere. For two modes the coefficient of \(z_1^2\bar z_2\) is \(\langle e_{(2,0)},\rho_2 e_{(0,1)}\rangle/2\), since both occupation monomials have squared norm two. In the preparations \(F_+\) and \(F_-\) it is \(+1/4\) and \(-1/4\), respectively. The same mixed Taylor expansion at zero gives every matrix entry of \(\rho_N\).

Now fix occupation basis states \(|\alpha\rangle,|\beta\rangle\) with finitely many occupied modes. Once \(N\) contains them all, form the local matrix unit \(L_N=|\beta_{\le N}\rangle\langle\alpha_{\le N}|\otimes I_{>N}\), including the zero occupations up to \(N\). Its expectation is the known entry \(\langle\alpha_{\le N}|\rho_N|\beta_{\le N}\rangle\). On each occupation basis state, \(L_N\) eventually agrees with \(|\beta\rangle\langle\alpha|\). Since \(\|L_N\|=1\), the convergence is strong on the whole Hilbert space. Approximating \(\rho\) in trace norm by finite-rank operators therefore gives \(\lim_{N\to\infty}\operatorname{Tr}(\rho L_N)=\langle\alpha|\rho|\beta\rangle\). These entries recover the full state, including any mixture.

For the fermions on the boundary circle the theorem concerns the limit of many particles. For a fixed density operator \(\rho\) of the current, project onto the Schur vectors with at most \(N\) rows and realize these vectors on the ring. The compression has positive trace for all sufficiently large \(N\). Normalize it by that trace. The projections increase strongly to the identity. On finite Schur combinations convergence of the joint density-wave laws follows from the polynomial calculation above. Trace-norm approximation then gives convergence against every bounded continuous test on finitely many waves for the fixed state \(\rho\). The family of limiting marginals determines \(\rho\).

### Reading the phase of the second harmonic {#ch11-second-harmonic-phase}

The joint law of the amplitudes \(Z_n\) is what a familiar instrument records. An ideal heterodyne receiver measures both quadratures of one oscillator mode. In each run it returns a complex number \(\alpha\), with probability density \(\langle\alpha|\rho|\alpha\rangle/\pi\), where \(|\alpha\rangle\) is the coherent state of amplitude \(\alpha\). For the \(n\)th harmonic put \(Z_n=\sqrt n\,\bar\alpha_n\). The vacuum then gives \(Z_n\) the Gaussian law of variance \(n\), and a state with amplitude \(F\) gives the law \(|F(Z)|^2\,d\mu\). The law of the disk is therefore the law of heterodyne readings of all the harmonics, and the preceding theorem says that these readings determine the state.

Two microwave receivers can test the opening experiment in this form. Let them record a field at the frequencies \(\omega\) and \(2\omega\). Two photons at \(\omega\) and one photon at \(2\omega\) have the same energy. These are the states \(a=|2,0\rangle\) and \(b=|0,1\rangle\) of Chapter 1, and photon counters cannot tell \((a+b)/\sqrt2\) from \((a-b)/\sqrt2\). On each run the receivers return \(Z_1\) and \(Z_2\). Form the angle
\[
\theta=2\arg Z_1-\arg Z_2 ,
\]
the angle which enters the reading \(C=2|Z_1|^2|Z_2|\cos\theta\). A time shift \(\Delta t\) rotates the two phases by angles in the ratio \(1:2\), with fundamental angle \(\omega\Delta t\) in the chosen convention, and leaves \(\theta\) fixed. The relative phase of the two receiver channels must still be calibrated. An unrecorded uniform rotation of either channel erases the dependence on \(\theta\).

Real receivers lose photons. Before detection let each mode pass through an independent loss channel with power transmission \(\eta_1\) or \(\eta_2\), whose unused port is in the vacuum. A coherent pulse of known amplitude calibrates the transmission and phase of each channel, and the vacuum fixes the scale of the readings. For the two preparations the angle then has the probability density
\[
\frac{1\pm G\cos\theta}{2\pi},\qquad G=\sqrt{\frac\pi8}\;\eta_1\sqrt{\eta_2}.
\]
{#eq-heterodyne-fringe}
A lost photon records which mode was occupied. The interference term therefore survives only when no photon is lost, and it carries the product \(\eta_1\sqrt{\eta_2}\) of the two amplitudes for that event. The factor \(\sqrt{\pi/8}=\tfrac12\,\mathbb E_\mu|Z_1|^2\;\mathbb E_\mu|Z_2|\) comes from averaging the term \(\pm\tfrac12|Z_1|^2|Z_2|\cos\theta\) of \(|F_\pm|^2\) over the two radii.

Suppose the two preparations are equally likely. The best decision from a single run reports the sum when \(\cos\theta>0\), and it is correct with probability \(\tfrac12+G/\pi\). With perfect transmission this is \((1+1/\sqrt{2\pi})/2\approx0.70\). Counting photons gave no information about the sign. One heterodyne reading decides it correctly seven times in ten, and a measurement of the exchange \(S\) decides it with certainty.

The same readings recover an arbitrary state on this energy shell, pure or mixed. The mean of \(e^{i\theta}\) is \(G\,\langle b,\rho\,a\rangle\). For the two populations, count the runs in which \(|Z_2|>\sqrt2\,|Z_1|^2\). With perfect transmission this event has probability \(0.0796\) in the state \(a\) and \(0.7049\) in the state \(b\). Since the event does not involve \(\theta\), its probability in a general state is their average with the weights \(\langle a,\rho\,a\rangle\) and \(\langle b,\rho\,b\rangle\). With losses the first probability stays below the value \(0.5456\) of the vacuum and the second stays above it, so they remain distinct when both transmissions are positive. Three bounded readings in each run thus determine the density matrix from their averages: the indicator of the event, and the real and imaginary parts of \(e^{i\theta}\).

Both readings depend on the two amplitudes only through the ratio \(Z_2/Z_1^2\). The heterodyne law has a density in the two complex coordinates, so \(Z_1=0\) has probability zero. The same is true on every energy shell of the two harmonics.

**Theorem (the ratio determines a known shell).** Let \(K\) be a nonnegative integer, and let \(\rho\) be a density operator on the states of oscillator grade \(K\) of the first two harmonics, which are spanned by \(p_1^{K-2j}p_2^{\,j}\) for \(0\le j\le K/2\). Suppose the two transmissions are known and positive. Then the probability law of the single complex number \(Z_2/Z_1^2\) determines \(\rho\).

*Proof.* Take first perfect transmission. Let \(e_j=p_1^{K-2j}p_2^{\,j}/c_j\) be the unit vectors, with \(c_j^2=(K-2j)!\,2^jj!\), and let \(\rho_{jk}=\langle e_j,\rho\,e_k\rangle\). The density of the readings relative to \(\mu\) is \(\sum_{j,k}\rho_{jk}\,e_j(Z)\overline{e_k(Z)}\). Rotation of the first oscillator by a phase and of the second by twice that phase multiplies each \(e_j\) by the same scalar. Thus the common phase cancels in \(e_j\overline{e_k}\). Its term \((j,k)\) has the phase \(e^{-i(j-k)\theta}\) and the modulus \(|Z_1|^{2K-2j-2k}|Z_2|^{j+k}/(c_jc_k)\). Fix \(d\ge0\). For real \(s\) near zero the moment
\[
T_d(s)=\mathbb E\Bigl[\,\bigl|Z_2/Z_1^2\bigr|^{2s}\,e^{id\theta}\Bigr]
\]
is determined by the law of the ratio, and only the terms with \(j-k=d\) contribute to it. Since \(\mathbb E_\mu|Z_n|^{2t}=n^t\,\Gamma(1+t)\),
\[
T_d(s)=\sum_k\rho_{k+d,k}\;\frac{2^{\,s+k+d/2}}{c_{k+d}\,c_k}\;
\Gamma(1+K-2k-d-2s)\;\Gamma\bigl(1+k+\tfrac d2+s\bigr).
\]
Divide by \(2^s\,\Gamma(1+d-2s)\,\Gamma(1+\tfrac d2+s)\). The coefficient of \(\rho_{k+d,k}\) becomes a polynomial in \(s\) of degree \((K-2k-2d)+k=K-2d-k\) with nonzero leading coefficient. These degrees are distinct for distinct \(k\). The polynomial is known on an interval, so its coefficients give first \(\rho_{d,0}\), then \(\rho_{d+1,1}\), and so on. The entries with \(j<k\) are their complex conjugates. With transmissions \(0<\eta_1,\eta_2\le1\) the lost photons move part of the state to lower shells. If the environment takes \(\ell_1,\ell_2\) photons from the two modes on both sides of a matrix entry, the phase difference \(d\) is unchanged. The two gamma factors then have their arguments lowered by \(\ell_1,\ell_2\), respectively. The same division gives degree \(K-2d-k-\ell_1-\ell_2\) since \(\ell_1\le K-2k-2d\) and \(\ell_2\le k\). Only the no-loss term reaches the original degree. Its coefficient is multiplied by \(\eta_1^{K-2k-d}\,\eta_2^{\,k+d/2}>0\), so the same descending-degree recovery works. ∎

The ratio is unchanged by a shift of the origin of time, so on a known shell no clock is needed. For a superposition across shells the ratio can lose relative phase. For example a rotation by \(\pi\) sends the norm-one amplitude \((1+Z_1)/\sqrt2\) to \((1-Z_1)/\sqrt2\) and leaves \(Z_2/Z_1^2\) fixed almost surely. The ratio has the same law in the two states. The full joint reading recovers both states by the [disk reconstruction theorem](#ch11-recovering-a-state-from-the-disk).

How sensitive is this recovery? Put \(2n\) photons in the fundamental, or \(n\) photons in the second harmonic, and prepare the sum or the difference of these two states. A suitable measurement distinguishes them with certainty. With perfect transmission the laws of their heterodyne readings differ in total variation by
\[
d_n=\frac2\pi\,\frac{\Gamma(n+1)\,\Gamma(\tfrac n2+1)}{\sqrt{(2n)!\,n!}},
\qquad d_1=0.399,\quad d_2=0.184,\quad d_4=0.031 ,
\]
{#eq-heterodyne-distance}
and losses multiply \(d_n\) by \(\eta_1^{\,n}\eta_2^{\,n/2}\). By Stirling's formula \(d_n\) decreases like \(\sqrt n\,2^{-3n/2}\). The relative sign of these two superpositions is therefore hard to resolve at high energy. The occupations themselves give a different signal on the same shell. At perfect transmission set \(X=|Z_1|^2\), in units of its vacuum mean. With \(2n\) photons in the first mode, \(X\) has density \(x^{2n}e^{-x}/(2n)!\) for \(x>0\). With all \(n\) photons in the second mode, its density is \(e^{-x}\). The event \(X>n\) consequently separates their probabilities by at least \(1-\tfrac12(e/4)^n-e^{-n}\). In the first state \(\Pr(X\le n)\le e^n\mathbb E(e^{-X})=e^n/2^{2n+1}\). This lower bound tends to one. Return to the superpositions and write \(P_+,P_-\) for their reading laws and \(d\) for their total-variation distance with the chosen transmissions. If the reported law has error at most \(\epsilon\), the two closed error balls overlap exactly when \(d\le2\epsilon\). The triangle inequality gives necessity. Their midpoint \((P_++P_-)/2\) has distance \(d/2\) from each law, so at this accuracy some reports are consistent with both signs. A report equal to \(P_+\) still excludes \(P_-\) whenever \(\epsilon<d\).

Experiments with superconducting circuits have realized separate parts of this measurement. H. Wang and coauthors prepared a superposition of two photons in one storage resonator and one photon in another, with both resonators near 6.3 GHz, and reconstructed the state by joint Wigner tomography with fidelity \(0.42\pm0.01\) (*Deterministic entanglement of photons in two superconducting microwave resonators*, Phys. Rev. Lett. 106 (2011), 060401, [supplementary Fig. S7](https://web.physics.ucsb.edu/~martinisgroup/papers/Wang2010supp.pdf#page=8)). S.-P. Wang and coauthors resolved an avoided crossing at which two photons of the first mode of a resonator match one photon of its second mode. Their model identifies the dressed states near the crossing as approximately the symmetric and antisymmetric combinations (Nature Communications (2025), doi 10.1038/s41467-025-63783-7, Fig. 2 and Eq. (9)). C. Lang and coauthors used heterodyne detection in two channels, with fourth-order correlations of the field, to distinguish an entangled state of two travelling microwave photons from its incoherent mixture (*Correlations, indistinguishability and entanglement in Hong–Ou–Mandel experiments at microwave frequencies*, Nature Physics 9 (2013), 345–348). None of these experiments reports the phase-calibrated joint heterodyne reading of both signs at the resonance of one to two. The density of \(\theta\) displayed above and its proportionality to \(\eta_1\sqrt{\eta_2}\) are predictions for that experiment. They test the two oscillator coordinates and their vacuum law. A realization of the boundary current would also require control of its other harmonics and of their operations.

### A neutral ray pair and a sourced disk {#ch11-neutral-ray-pair}

The differential probes removed individual oscillators from a prepared polynomial. A pair of charged rays instead prepares a state with a specified mean in every harmonic. A Wilson ray of charge \(a\) couples the one-form \(A\) to an oriented curve by \(\int_L A\). In the Gaussian Chern–Simons presentation use orientation \(dx\wedge dy\wedge dt\), level one and the boundary condition \(i^*A\in(dz)\) on compact form tests. The line changes the quantum differential by \(-iaI_L\), where \(I_L\) integrates a one-form test along the ray. Stokes' formula gives \(I_Ld=0\) on admissible zero-forms because they vanish at the boundary endpoint and have compact support. A free interior endpoint would contribute a nonzero evaluation.

Place a ray of charge \(a\) at the boundary point \(z=r\) and a ray of charge \(-a\) at \(z=0\), with \(a\in\mathbb R\) and \(0<r<1\). Take the positive real chamber and preserve the order of the two paths, so that their separation has the real logarithm. Continue the two proper rays upwards as disjoint smooth graphs \(z_i(t)\), vertical near the endpoints and constant in \(z\) above the bending region. As their outgoing separation shrinks, take a smoothly converging family on the compact normal intervals met by the tests, with uniformly bounded \(z_i\) and \(\dot z_i\) there. Use the planar Cauchy propagator, disjoint radial transverse mollifiers, caps above the bending region and the compact tests, and constant framing. Remove self-contractions. If the outgoing separation is \(\epsilon d\) with \(d>0\) fixed, the mutual Gaussian contraction in the exponent is \(-a^2(\log r-\log(\epsilon d))\). Multiplication by the prescribed outgoing factor \((\epsilon d)^{-a^2}\) leaves \(r^{-a^2}\).

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

The disk source fixes a probability law. Put \(L=-\log(1-r^2)\) and \(L_q=-\log(1-qr^2)\). Relative to \(\mu\), the positive square root of its density is \(e^{a\operatorname{Re}h(r)-a^2L/2}\). The normalised ray has holomorphic amplitude \(e^{a h(r)-a^2L/2}\). These amplitudes have identical squared moduli. Their matrix elements under a collar can differ. The two real parts of \(h(r)\) at the ends of the vacuum Mehler collar have variance \(L/2\) each and covariance \(L_q/2\). The normalised collar pairing of the positive square root is therefore \(\exp[a^2(L_q-L)/2]\). Requiring a holomorphic amplitude selects the ray state up to phase by the [disk reconstruction theorem](#ch11-recovering-a-state-from-the-disk).

The real collar sends each oscillator \(p_n\) in the second amplitude to \(q^n p_n\). Its exponential therefore contains \((qr)^n\), while the endpoint contraction still contributes \(r^{-a^2}\) to each amplitude. Pairing the two exponentials inserts \(qr^2\) into the covariance sum. With \(V\) the Fock-to-disk isometry, this gives

\[
\frac{\langle V\Psi_{a,r},P_q V\Psi_{a,r}\rangle}
     {\|V\Psi_{a,r}\|^2}
=\exp\!\left(a^2\sum_{n\ge1}\frac{(q^n-1)r^{2n}}{n}\right)
=\left(\frac{1-r^2}{1-qr^2}\right)^{a^2}.
\]

At zero collar length \(q=1\), the numerator is the squared norm \(r^{-2a^2}(1-r^2)^{-a^2}\). At zero charge the state is the vacuum for every collar. In both cases the ratio is one. At fixed \(r\), multiplying the ray vector by any scalar \(c(r)\ne0\) multiplies its squared norm, the disk weight \(|V\Psi_{a,r}|^2\) and the collar numerator by \(|c(r)|^2\). Thus the mutual ray factor \(r^{-a^2}\) enters both normalized readings through its squared modulus \(r^{-2a^2}\), which cancels. For nonzero real \(a\) the unnormalized norm diverges as \(r\uparrow1\). Neutrality places the output in the disk theory with its constant mode fixed to zero. A nonneutral output requires a charged zero-mode sector.

Keep the framing and outgoing subtraction fixed and move the endpoint of charge \(a\) from \(r\) to \(s\), with \(0<s<1\). The disk means change from \(ar^n\) to \(as^n\). The ray contraction multiplies the vacuum coefficient by \((s/r)^{-a^2}\). A filling with the same normalized disk law must also reproduce this factor to agree on the ray amplitude. For an [absolute cap comparison](17-holographic-reconstruction.md#states-lines-and-caps), the filling must supply its own amplitude \(Z(1)\) with no insertion. After the two vacuum lines are identified, their nonzero empty-insertion amplitudes must agree. One must also show that pairing the boundary states along the cut gives the amplitude of the glued filling.

## The quadratic theory on a solid torus {#ch11-the-quadratic-theory-on-a-solid-torus}

The disk heat kernel used the cylinder length to propagate a state between two boundary circles. To study a vacuum amplitude on a torus boundary, glue together the ends of a three-dimensional shell. Take \(0<|q|<1\), \(\kappa\in\mathbb C^\times\) and \(\hbar>0\). The identification contracts normal distance by \(|q|\) and multiplies the complex coordinate by \(q\), so the filling is

\[
N_q=
\bigl(([0,\infty)\times\mathbb C)\setminus\{0\}\bigr)
\big/\langle(t,z)\mapsto(|q|t,qz)\rangle.
\]

At \(t=0\) the orbit of a nonzero \(z\) is \(q^{\mathbb Z}z\), so the boundary is the elliptic curve \(\mathbb C^\times/q^{\mathbb Z}\). A radial shell \(|q|\le(t^2+|z|^2)^{1/2}\le1\) meets every orbit, and its two hemispherical faces are identified with a rotation by \(\arg q\). Thus \(q\) now specifies the complex gluing of a solid torus. The real Mehler parameter on the disk specified a propagation between two ends. The differential in the topological and antiholomorphic directions is

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

These choices descend to the quotient. Under the identification, \(dt\,dx\,dy\) picks up \(|q|^3\) and \(\rho^{-3}\) picks up its inverse. The absolute coefficient complex has three current components \(e,h,f\) and two constraint components \(b,c\). In the order \((e,h,f,b,c)\) they have weights \((0,1,2,0,1)\) and internal degrees \((0,0,0,1,-1)\). Weight \(w\) means the coefficient takes values in \((dz)^w\), with descent under the displayed quotient. The last two components are the odd constraint fields. Total degree is internal degree plus partial form degree. On partial form degree \(p\), its source-zero differential is

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

The absolute and relative fields are paired by integration. Integration by parts in \(\mathcal B\) defines the signed bilinear transpose on the shifted relative summand. The Hermitian metric instead defines the adjoint \(d_C^\dagger\) used to choose a gauge.

A background consists of a smooth weight-minus-one partial one-form \(\mu\), with zero normal trace, and an actual smooth weight-two function \(T_\mu\) satisfying

\[
D\mu+\mu\wedge\partial_z\mu=0,
\qquad
(D+L_\mu^{(2)})T_\mu=\frac{\kappa}{2}\partial_z^3\mu,
\qquad
L_\mu^{(2)}=\mu\wedge\partial_z+2(\partial_z\mu)\wedge.
\]

The first equation is the Maurer–Cartan equation for the vector-field-valued form \(\mu\,\partial_z\). The second is the Virasoro Ward identity for the stress tensor \(T_\mu\), with the third derivative of \(\mu\) as its central term. The numerical Gaussian requires a smooth solution of both equations on \(N_q\).

To put the torus action into Gaussian pairs, start at zero source. On a singular pair \(d_Cu=\sigma v\) the absolute Hodge Laplacian \(\Delta_C=d_Cd_C^\dagger+d_C^\dagger d_C\) has eigenvalue \(\sigma^2\). The harmonic space in the absolute complex is zero. In the coefficient differential the pairs \(e,b\) and \(c,h\) are contractible, and \(f+(\kappa/2)\partial_z h\) projects to the remaining weight-two complex. On the cover, contraction along \(t\) to the slice \(t=1\) and the Dolbeault resolution of the plane leave the entire functions \(G(z)(dz)^2\) in degree zero. A radial partition of unity makes one minus deck pullback surjective on smooth cover forms. The resulting exact sequence computes the quotient cohomology by the kernel and cokernel of \(1-U\), with \(UG(z)=q^2G(qz)\). The sum \(\sum_{j\ge0}q^{2j}G(q^jz)\) converges uniformly on compact sets and inverts \(1-U\). The absolute Hodge theorem identifies harmonic fields with this zero cohomology. Compact resolvent gives a positive spectral gap and a bounded \(\Delta_C^{-1}\). The Green contraction \(r_C=d_C^\dagger\Delta_C^{-1}\) sends \(v\) to \(u/\sigma\), just as in the finite complex. It satisfies

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

Conjugation by \(\mathsf S_\mu\) transports the two diagonal differentials and their contraction \(R_{\mathrm{diag},\mu}=\mathsf S_\mu R_{\mathrm{diag},0}\mathsf S_\mu^{-1}\). On \((0,b)\) the full differential still creates the absolute field \(P_\mu b\). Regard \(P_\mu\) as the upper off-diagonal operator and set
\(V_\mu=1-\tfrac12(R_{\mathrm{diag},\mu}P_\mu-P_\mu R_{\mathrm{diag},\mu})\).
The composite of this cyclic shear with \(\mathsf S_\mu\) then satisfies

\[
M_\mu=V_\mu\mathsf S_\mu,\qquad
\widetilde Q_\mu M_\mu=M_\mu d_{\mathrm{diag},0},
\qquad
S_\mu(M_\mu\phi)=S_{\mathrm{diag},0}(\phi).
\]

Here \(d_{\mathrm{diag},0}=\operatorname{diag}(d_C,-d_B)\)
and \(S_\mu(\phi)=\tfrac12\mathcal B(\phi,\widetilde Q_\mu\phi)\).
The full inverse-action contraction is
\(\mathcal R_\mu=M_\mu R_{\mathrm{diag},0}M_\mu^{-1}\).
The map at zero source is the original response shear \(M_0=V_0\); discarding it would change the original cycle. [*A numerical Gaussian on the native source graph*, §§1–3](#ref-ch11-01).

## A numerical state from the original cycles {#ch11-a-numerical-state-from-the-original-cycles}

Choose a finite spectral window of \(\Delta_C\) containing complete singular pairs \(d_Cu_{j,\ell}=\sigma_{j,\ell}v_{j,\ell}\). Denote the included pairs by \(\Lambda\) and their span by \(C_\Lambda\). Each retained even pair contributes one complex integration coordinate, and each odd pair retains its order in the Berezin integral. Apply \(M_\mu\) to their actual finite integration cycles. The cyclic chain identity above proves the action equality before any covariance is assigned. Each even action becomes \(\sum|w_{j,\ell}|^2\), and its unnormalized factor in the transported coefficient frame is

\[
G_\Lambda=\prod_{(j,\ell)\in\Lambda}
                    \sigma_{j,\ell}^{\,(-1)^{j+1}}.
\]

Enlarging the window by one even pair multiplies \(G_\Lambda\) by \(1/\sigma\). Its probability density, after division by that same integral, has mass one. This allows a limit of normalized fields to exist without a limit of the unnormalized products.

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

**Theorem 11.1 (normalized numerical Gaussian).** Fix the original metric and density, \(0<|q|<1\), \(\kappa\ne0\), \(\hbar>0\), and a smooth integrable \(\mu\) with zero normal trace in the single small \(C^1\) inverse neighbourhood. Supply a smooth solution \(T_\mu\) of the Ward equation above, based by \(T_0=0\) for families through zero. Exhaust the singular pairs by increasing finite windows. For each pair in even degree choose one circular complex Gaussian \(w_{j,\ell}\) with \(\mathbb E|w_{j,\ell}|^2=\hbar\), independently over pairs, and use that same variable in every window containing the pair. The resulting fields \(\Phi_{\Lambda,\mu}\) converge in mean square and almost surely in \(\mathscr D_{-6}\) to a centered Radon Gaussian \(\Phi_\mu\). Its law has support equal to the closure of \(\mathfrak A_\mu\mathsf W\). Let \(P_\Lambda\) project onto the retained real and imaginary singular-pair coordinates in \(\mathsf W\). In their orthonormal coordinate basis \(e_n\),

\[
\begin{gathered}
\mathbb E\|\Phi_\mu-\Phi_{\Lambda,\mu}\|_{-6}^2
=\frac{\hbar}{2}\|\mathfrak A_\mu(1-P_\Lambda)\|_{\rm HS}^2\\
=\frac{\hbar}{2}
 \sum_{P_\Lambda e_n=0}\|\mathfrak A_\mu e_n\|_{-6}^2
\longrightarrow0 .
\end{gathered}
\]

Each real coordinate of \(w_{j,\ell}\) has variance \(\hbar/2\). The sum in the display is the tail of the squared Hilbert–Schmidt norm. Orthogonality of the independent increments gives the mean-square limit, and the Hilbert-valued Gaussian series converges almost surely. The real covariance is
\(\frac{\hbar}{2}\mathfrak A_\mu\mathfrak A_\mu^*\), with the real Hilbert adjoint. Odd and mixed moments converge by the graded Wick rule for the full inverse action. They do not define an odd-variable probability measure. Parameter-uniform statements require bounds on the finitely many higher source and background seminorms used in the estimates. [*A numerical Gaussian on the native source graph*, Theorems 4–6](#ref-ch11-01).

The action domain is smaller than this distributional support. In the original unwhitened coordinates \(x_{j,\ell}\), its transported form domain requires

\[
\sum_{j,\ell}\sigma_{j,\ell}|x_{j,\ell}|^2<\infty,
\]

while the operator domain requires the same sum with \(\sigma_{j,\ell}^2\). The Cameron–Martin space is the transported form domain with its covariance norm. In infinite rank a typical Gaussian sample has nonsquare-summable white coordinates and lies outside this domain. The construction does not evaluate the quadratic action on a typical distribution.

Wick contraction terminates on a polynomial. For a sum of polynomials of increasing degree, we must also control the number of ways to contract their slots. Represent a linear observable by \(\ell_x(\phi)=\mathcal B(x,\phi)\), of degree \(|x|-1\), and put \(\mathcal T=\mathcal E[1]\). Write \(F_n\) for the graded symmetric tensor of labels in the term of field degree \(n\). Use ordinary Taylor coefficients, so for \(F=\ell_x^2\) with an even observable the quadratic coefficient is the symmetric square of its label. Complete the polynomials in all the seminorms

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

## Heat on the coefficient complex and the vacuum amplitude at a base point {#ch11-original-coefficient-heat-and-a-based-local-vacuum-line}

The normalized Gaussian of Theorem 11.1 takes the value one on the constant observable at every cutoff. It cannot detect the vacuum factor produced when modes are integrated out. For a single singular pair that factor was \(\sigma^{-1}\) in even degree and \(\sigma\) in odd degree. To compare all such factors as the background varies, reflect the solid torus across its boundary to the closed double \(M_q\), and use smooth reflection-invariant backgrounds on that double. The coefficient operator is

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
selects the finite absolute complex, paired with its smooth relative transpose. Here \(u\) labels a background in the source family. Write \(A_\Gamma(u)\) for the restricted coefficient operator. In the continued frame, let \(D_j(u)\) be the matrix pairing the \(x\)- and \(y\)-coordinates of the degree-\(j\) finite action, so that its contribution is \(y^{\mathsf t}D_j(u)x\). At zero source \(D_j(0)\) is diagonal with the original singular values. In the original continued density and cycle,

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

The difference between relative and absolute normalization also has an infinite-dimensional example. On the reflection-even weight-two coefficient complex let \(D_2\) be the restriction of \(D\) and \(\Delta_2=D_2D_2^\dagger+D_2^\dagger D_2\) its Hodge Laplacian. The reduced contraction \(\widehat r\) from the five fields and the stress contraction \(h_2=D_2^\dagger\Delta_2^{-1}\) both contract \(D_2\). Use the same metric for both. For a smooth reflection-invariant integrable source, set

\[
\mathsf T=L_\mu^{(2)}(\widehat r-h_2)
                      (1+L_\mu^{(2)}h_2)^{-1}.
\]

The logarithm of \(1+\mathsf T\) starts with \(\mathsf T-\mathsf T^2/2+\mathsf T^3/3\). Removing these three powers before taking the supertrace gives the fourth modified Berezinian. On the small-source branch \(\|\mathsf T\|<1\) its trace-class series gives

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

The coefficients come from the full matrix heat symbol and the fixed-surface reflection contribution. Parity cancels the intervening powers; both reflection factors of one half enter the leading coefficient. The right-half-plane gap on the reflection-even sector controls the integral at infinite time. For example, the trace term \(B(u)t^{-1/2}\) contributes \(-2B(u)/\sqrt\epsilon\) up to a finite constant in the cut-off integral. The constant trace term contributes \(C(u)\log\epsilon\). After these terms and the leading power are removed, the remaining integrand is \(O(t^{\delta-1})\), integrable at zero. For action and line statements, the background must in addition satisfy the integrability and Ward-filling equations. The trace is independent of \(T\) at fixed \(\mu\) because \(T\) occurs in an off-diagonal triangular block; non-scalar action moments still depend on it.

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

The relative amplitude between two positive levels can be computed by differentiating the heat integral at positive cutoff and integrating the derivative over the level. Use a reflected Ward family on which the coefficient differential squares to zero, put \(x=|\kappa|^2\), and scale \(\kappa\) and the supplied filling together. On a compact interval \([a,b]\subset(0,\infty)\), assume a common gapped realization, the positive-cutoff variation identity and continuous differentiability in \(x\). The inserted trace must have a uniform expansion in one fixed finite power/logarithm scale, with the stated source derivatives and a decaying remainder. Compactness of the interval does not supply these analytic hypotheses.

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
The integration measure is \(dx/x\) because the inserted coefficient differentiates with respect to \(\log x\). At a fixed source, a bound \(|c_F(v,x)|\le M\) gives a difference of at most \(M|\log(x_1/x_0)|\). If the inserted coefficients are continuous in \(x\), this yields \(x\partial_xW_{\mathrm{fp}}=c_F\), including the covered source derivatives. [Positive-level variation](#atlas-c-gravity-positive-level-variation).

The Mellin comparison fixes which absolute constant is retained. Absence of an \(\epsilon^0\log\epsilon\) term in the inserted trace makes the original constant heat coefficient \(C(v,x)\) independent of \(x\) on the interval. For the original Mellin branch,
\[
Z(0,v,x)=C(v,x),\qquad
W_{\mathrm{fp}}(v,x)=-Z'(0,v,x)+\gamma_EC(v,x).
\]
Thus positive-level differences equal the corresponding differences of \(-Z'(0)\). Neither \(C\) nor \(c_F\) has been proved zero, and the absolute Euler term remains. The estimate contains \(\log(b/a)\); it gives no control at \(x=0\). Passage through zero requires an integrable endpoint estimate and compatible heat control there. [The zero-level endpoint](#atlas-c-gravity-positive-level-zero-endpoint).

An explicit source distinguishes the local density from its integral. Take \(q=e^{-2\pi}\), \(\kappa=2\), \(u=\log\sqrt{t^2+|z|^2}\), and set \(F=z(1-\lambda_+e^{iu}-\lambda_-e^{-iu})\) for two small complex parameters. The fields \(\mu=-DF/\partial_zF\) and \(T=-(\kappa/2)\{F,z\}\) solve the two Ward equations, where \(\{F,z\}=(\partial_z^3F)/(\partial_zF)-\tfrac32((\partial_z^2F)/(\partial_zF))^2\) is the Schwarzian derivative. Here \(\partial_zF\) stays nonzero for small parameters. In the fixed coefficient frame, the two first derivatives of the density for \(c_F\) are

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

On the fixed absolute-relative complex the second field has zero tangential pullback. In the physical variables the boundary value of that field is prescribed by the first. A change of variables identifies these two domains at a fixed source. A derivative with respect to the source also differentiates the domain. With \(\partial=\partial_z\), the tangential Hessian on the three even current components is

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
For a fixed pair \((a,b)\), differentiating the graph adds \((\partial_v K_\mu^{\mathrm{gr}})a\) to the second field. Thus \(A_v(a,b)=(0,(\partial_v K_\mu^{\mathrm{gr}})a)\). Even when \(b\) has zero tangential trace, this new field can have a boundary value. Applying the finite projection to its differential gives the defect

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

Here \(K_v^{\mathrm{gr}}=\partial_vK_\mu^{\mathrm{gr}}\). For example its \((f,e)\) entry is \((\partial_v\mu)/\kappa\), so even an \(e\)-component at a fixed boundary can contribute to the varying \(f\)-component. The Green term is precisely the resulting boundary pairing. Applying a chain identity outside its relative domain would incorrectly erase it. Mixed source derivatives differentiate both embedded current factors and the Hessian, as well as the supplied filling \(T_\mu\). [*A numerical Gaussian on the native source graph*, Theorem 8 and equations (74)–(78)](#ref-ch11-01).

There is a precise formal comparison with the original homological-perturbation cutoff. A cyclic polar correction, followed by a gauge correction, compares it with a finite Riesz action. If \(\rho\) is the genuine based semidensity ratio and \(B_R,B_H\) are the two covariances after their actual maps to the same stress observables, then

\[
\mathcal Z_R^{\mathrm{st}}(F)
=\rho^{-1}\mathcal Z_H^{\mathrm{st}}
       \left(e^{\hbar\partial_{B_R-B_H}/2}F\right).
\]

For \(F=1\) the contraction exponential acts as the identity, so the comparison still reads the line ratio \(\rho^{-1}\). For the square of an even linear test the same exponential adds its scalar contraction with \(\hbar(B_R-B_H)\). These are two independent parts of the comparison. The equality holds over the formal source ring and each contraction series terminates on a polynomial. The line ratio and the ambient covariance correction are both required, even when the intrinsic finite actions are cyclically isomorphic. Numerical convergence of the original sharp-tail perturbation series and its identification with the continued-cycle limit remain separate questions. [*Finite action integrals from the original coefficient Riesz spaces*, Theorem 4 and equation (68)](#ref-ch11-02).

## Boundary insertions and the physical cap {#ch11-boundary-insertions-and-the-physical-cap}

A state on bulk observables becomes relevant to boundary fields through an insertion map. In the boundary coordinate \(e=1+u\), the classical symbol algebra is the graded polynomial algebra on \(u,h,f,b,c\) and their holomorphic derivatives. The actual differential includes

\[
q_{\mathrm{cl}}b=u,\qquad q_{\mathrm{cl}}u=q_{\mathrm{cl}}c=0,
\qquad
q_{\mathrm{cl}}h=-2(1+u)c,\qquad
q_{\mathrm{cl}}f=hc+\kappa\partial_zc.
\]

It also includes the partial-form differential on descendants. At the quantum level the source is the prescribed affine–ghost vacuum module with its actual Poincaré–Birkhoff–Witt products.

To test whether insertion preserves this differential, one can start with the boundary generator \(b\). Its bulk differential after insertion must equal the insertion of \(u\). For a polynomial in the generators and their holomorphic jets, take a fixed finite stage and retain the enlarged source and output stages required by the differentials and homotopies. “Ordinary” means that a root is at height zero before any incoming normal derivative is taken. The relative tangential endpoint quotient is part of the domain.

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

If \(f_0=f_1\), the marked scalar transfer is exactly \(e^{-ML}\), even for a source varying between the ends. To use this scalar calculation for affine states one must also transport the transverse fields. The weighted pullback intertwines the source differential on scalars. On smooth finite sums of angular Fourier modes, extending this pullback to transverse fields requires a homotopy correction for the stress response. The absolute and relative harmonic projections have disjoint frequency support, so the response defect induces zero between them. An angular Green operator supplies a skew-adjoint homotopy for the complex-bilinear cut pairing. The resulting cyclic chain isomorphism preserves radial support and agrees with geometric rotation on the rigid ends. On a complete finite window through energy \(M_0\) with \(n+1\) complete radial singular pairs, transport the zero-source gauge, contour and density by that isomorphism. For the window with just the stated physical cohomology, its radial scalar remains \(\prod_{M=2}^{M_0}\prod_{j=0}^n\sigma_{M,j}^{-1}\), where \(\sigma_{M,j}\) are the original radial singular values. With the zero-frequency sector paired separately, the normalized transfer on positive-frequency harmonic states is \(\eta^{N}\), with \(\eta=e^{-L-i\lambda(f_1-f_0)}\) and \(N\) the total energy.

For example, supply both ends with the same positive Virasoro vacuum representation at \(c>25\), using the specified energy-preserving identification on each complete window through weight six. For the vacuum \(v\), the two orders of the bra against \(L_{-5}v\) give \(4c\eta^5\) for \(L_2L_3\) and \(14c\eta^5\) for \(L_3L_2\). To obtain the two coefficients, commute \(L_3\) or \(L_2\) through \(L_{-5}\) on the vacuum. The first gives \(8L_{-2}v\), the second \(7L_{-3}v\). With \(\langle v,v\rangle=1\) the remaining contractions are \(c/2\) and \(2c\), respectively. At weight six, projecting \(L_{-4}L_{-2}v\) and \(L_{-3}^2v\) perpendicular to \(L_{-6}v\) gives a pairing of \(62c\eta^6/7\). On this marked Hilbert space the transfer has positive modulus \(e^{-LN}\) and unitary phase \(e^{-i\lambda(f_1-f_0)N}\). These closed-state measurements can distinguish global sources even when all germs of \(\mu,T\) agree at the two ends and at a nonflat middle meridian. A relative end rotation by \(\lambda\) changes the ratio of the weight-six and weight-five readings by \(e^{-i\lambda}\), independently of a common scalar normalization. [Sourced affine meridian transfer](#atlas-c-sourced-affine-meridian-transfer)

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
Rescaling the negative harmonic by \(1/c_M\) gives the action-dual normalization. Its measured flux is then \(R_M\), with the sign fixed by the order of the two inputs. This uses two independently solved classical linear boundary problems on the cut.

The classical action also detects the shape of the source between the marks. More generally take \(A\) smooth, periodic and sufficiently close to one, constant of unit modulus near each end. Assume \(J\ne0\) and \(u\mapsto u+\log|A(u)|\) has positive derivative, so the real change \((t,z)\mapsto(|A|t,Az)\) preserves the radial foliation. Write \(s=A'/A\) and \(h=1+s/2\). On the small branch the original on-shell action is
\[
 S_{\mathrm{crit}}(A)-S_{\mathrm{crit}}(1)
 =\frac{\kappa}{32}\int_{u_0}^{u_1}
 \left(\frac{4s^2}{h}+\frac{(s')^2}{h^3}\right)du .
\]
For the twist \(A=e^{i\lambda f}\) the quadratic term is \(-\kappa\lambda^2\int((f'')^2+4(f')^2)\,du/32\). A twist which returns to its starting angle can therefore change the action even when its marked transfer equals the zero-source transfer. The factor \(e^{-S_{\mathrm{crit}}/\hbar}\) belongs to the classical saddle. This flux fixes the relative normalization of two classical modes. A quantum pairing also needs a contour and a half-density on each side. [Classical affine flux and action](#atlas-c-classical-affine-meridian-flux)

### A fixed quantum measure on a nonflat meridian {#ch11-independent-meridian-measure}

Two Ward fillings can agree near every boundary face, corner and cut and still have different unnormalized quantum amplitudes. On the \(q=1/2\) solid torus take \(F_j=F_*e^{i\epsilon g_j}\), where \(F_*=zA_*(\log r)\) has a small nonzero source near the middle meridian and is the identity coordinate on both exterior collars. The two angular bumps \(g_1,g_2\) have disjoint supports inside the left half, related by a dilation of factor \(16/15\). All source and field germs agree on the collars. The dilation preserves the integrated critical density on the two patches, so the classical actions agree separately on each half.

Fix a compact current and its conjugate on the first patch before choosing the filling. The current coefficient \(p\) and conjugate one-form \(\beta\) have angular charges \(+8,-8\). The original affine action restricted to their two coefficients \(x,y\) is \(B_jxy\), up to its critical value. In the convention \(\tau(\omega)=(2\pi i)^{-1}\int dz\wedge\omega\), the kinetic term and the affine Poisson term give \(B_j=\tau(\beta\wedge(Dp+p\,\partial_z\mu_j))\). On the support of \(\beta\) the first bump has \(g_1=t\), so \(\partial_z\mu_1=-i\epsilon\,dt\). The second source vanishes there. Unit-integral test functions with mean \(t=1\) give \(B_1=1-i\epsilon,\ B_2=1\). On the common contour \(x=w,\ y=\bar w\) the oriented integral is
\[
 \int_{\mathbb C}e^{-B_j|w|^2/\hbar}\frac{d^2w}{\pi\hbar}=\frac{1}{B_j}.
\]
The real part of each \(B_j\) is one, so radial integration on this same contour converges for both fillings. The difference is the complex factor \(1/B_j\) left after integration. An independently prepared pair in the right half has \(B_R=1\).

At frequency five the negative-first Green pairing of the raw meridian modes is \(-16/35\). Rescale the negative mode by \(-35/16\) and write \(a,b\) for the resulting positive and negative coordinates. In each coordinate \(v\) prescribe the half-density \((\pi\hbar)^{-1/2}e^{-|v|^2/(2\hbar)}|d^2v|^{1/2}\). On the ordered seam \(b=-\bar a\) their product is the Gaussian density. Write the insertion there as \(a^k(-\bar a)^\ell\). Angular integration gives zero unless \(k=\ell\). For equal powers the radial moment is \(\hbar^k k!\) and the seam contributes the sign \((-1)^k\). With the opposite exterior polarizations set to zero and \(S_{\mathrm{cl}}\) the sum of the two critical actions, the unnormalized result is
\[
 Z_{j;k,\ell}=\frac{e^{-S_{\mathrm{cl}}/\hbar}}{B_jB_R}
                   \delta_{k\ell}(-\hbar)^k k!,\qquad
 \frac{Z_{1;k,k}}{Z_{2;k,k}}=\frac1{1-i\epsilon}.
\]
At \(\epsilon=1/8\) the ratio is \((64+8i)/65\), with phase \(\arctan(1/8)\simeq0.124355\) radians. For instance a single matched pair has normalized insertion \(Z_{j;1,1}/Z_{j;0,0}=-\hbar\) for both fillings. The phase distinguishes the two unnormalized vacuum amplitudes in the fixed measure. Holding the filling fixed and moving only the compact test changes the answer as well. If the same regulator includes both dilation-related tests, the couplings on the two fillings are \((1-i\epsilon,1)\) and \((1,1-i\epsilon)\). Their product integrals have ratio one.

For five meridian pairs of frequencies \(2,\ldots,6\), use compact charges \(\pm17\) and the product of the prescribed half-densities. Each half has harmonic frequencies of one sign, so the original cubic action has no neutral term there. With the specified positive Virasoro marks at \(c>25\) and unrotated end frames, the two bra orders \(L_2L_3,L_3L_2\) against \(L_{-5}v\) give \(Z_{j;0,0}\,4c e^{-5L}\) and \(Z_{j;0,0}\,14c e^{-5L}\). The projected weight-six pairing gives \(Z_{j;0,0}(62c/7)e^{-6L}\). The interacting identification of the exterior marks is an input. A continuum cap would require a controlled removal of the regulator on the full boundary complex, with its residual modes and absolute phase. The derivation is given in *A fixed finite quantum measure on a non-flat native meridian*, §§1–5. [Independent quantum measure on a meridian](#atlas-c-independent-affine-meridian-measure)

A gravitational cap would assign a vector or functional to a specified compact filling, on its boundary state space, with its absolute normalization and cutting law. In the scalar disk the action supplied the ground amplitude, the cylinder supplied a transfer, and the interior contractions or charged rays supplied probes with which to test both. For the solid torus one still needs the map from uncut coefficient fields to the fields on the geometric cut, an identification of the two amplitude lines with their phases, and a comparison of the disk-cut Green kernels on the same insertions. These data would let the numerical bulk state, the local vacuum line and the ordinary unary Ward equation enter the same gluing formula.

The unary Ward identity follows one boundary insertion into the filling. Now prepare two boundary systems independently and allow a current to act on both. Its action must preserve the coefficient of each pole when a second current approaches. For the level-one disk current the double-pole coefficient is one on each system. What level can act on the pair? [The level of the tensor product](12-chiral-quantum-groups.md#ch12)

## Source manuscripts {#ch11-source-manuscripts}

The disk action and its transfer appear in *Harmonic fillings and mixed state correlations*, “The scalar filling and its state space” and “Scalar-cylinder sewing.” The two half-space constructions appear in *From holomorphic brackets to bulk fields*, “The supported bulk action,” in *Native cochains, supported fields, and harmonic fillings*, “Native annuli and all neutral fields,” and in *Chern–Simons observables, charged endpoints and chiral fusion*, Lemmas 3.2–3.4 and Theorem 4.1.

### 1. A numerical Gaussian on the native source graph {#ref-ch11-01}

The finite action is computed on the transported cycles in §3, Theorem 4. The Hilbert–Schmidt estimate and the Gaussian limit are Lemma 5 and Theorem 6 in §4. Theorems 7–8 give the observable Ward identity and transport to the physical graph. [The normalized Gaussian](#ch11-a-numerical-state-from-the-original-cycles)

### 2. Finite action integrals from the original coefficient Riesz spaces {#ref-ch11-02}

Theorem 3 evaluates the determinant blocks in the continued finite density. Section 6 integrates a finite spectral shell. Theorem 4 compares the Riesz cutoff with the formal perturbation cutoff, including the change of covariance on stress observables. [The finite spectral integral](#ch11-original-coefficient-heat-and-a-based-local-vacuum-line)

### 3. The common relative determinant of the native contraction {#ref-ch11-03}

Theorem 3 gives the vanishing common relative heat finite parts. Corollary 4 treats the actual trace with the fixed source-zero stress heat in the common metric. [The common relative determinant](#atlas-c-gravity-common-relative-heat)

### 4. The original coefficient heat finite part and its based vacuum line {#ref-ch11-04}

Theorems 3–4 give the heat expansion and the Mellin conversion. Theorems 5–6 supply the complementary finite part and the finite action value at the base of the vacuum line. [The heat finite part and based section](#atlas-c-gravity-original-coefficient-heat-finite-part)

### 5. The source counterterm in the covariant connection {#ref-ch11-05}

The proposition gives the source connection after multiplication by the counterterm at fixed positive heat time, equations (A1)–(A6). [The connection of the based line](#ch11-original-coefficient-heat-and-a-based-local-vacuum-line)

### 6. Ordinary boundary Ward identity and full-source heat cells {#ref-ch11-06}

Theorem 2 establishes the ordinary classical insertion equation, and Theorem 5 gives the forward heat homotopy through first quantum order. [Boundary insertions](#ch11-boundary-insertions-and-the-physical-cap)
