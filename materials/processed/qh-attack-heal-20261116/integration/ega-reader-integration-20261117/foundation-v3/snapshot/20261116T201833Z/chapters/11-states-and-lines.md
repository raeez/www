# States, determinant lines and quantum fields

For \(\lambda,\hbar>0\), the Gaussian integral and its normalized second moment are

\[
Z_\lambda(1)=\int_{\mathbb R}e^{-\lambda x^2/(2\hbar)}\,dx
             =\sqrt{\frac{2\pi\hbar}{\lambda}},
\qquad
\frac{Z_\lambda(x^2)}{Z_\lambda(1)}=\frac{\hbar}{\lambda}.
\]

Multiplying the measure by any nonzero constant changes the first expression and leaves the second unchanged. A normalized state therefore cannot recover the normalization of the integral that produced it. In a family of complex field theories, it also cannot recover the choice of integration cycle or its phase.

This distinction persists after all the analytic difficulties of the Gaussian have been solved. A convergent normalized state, a renormalized determinant line, and a state prepared by a geometric filling are different mathematical objects. The quadratic gravity construction supplies the first and a local form of the second on specified domains. Its relation to a physical cap requires additional maps, boundary conditions and gluing laws. We shall develop the finite action first, because it fixes the signs and normalizations that survive every later limit.

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

The first equation makes the deformed partial complex integrable. The second is the sourced stress-tensor Ward equation. A formal series for \(T_\mu\) is insufficient for a numerical theorem: the smooth solution is part of the data.

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

On the integrable locus, with the smooth Ward filling supplied, a finite Riesz projection gives a finite absolute complex and its genuine smooth relative transpose. A Riesz projection is the contour integral of the resolvent around a finite spectral cluster. Let \(u\) be a source parameter, \(A_\Gamma(u)\) the finite coefficient operator and \(D_j(u)\) the resulting action blocks. In the original continued density and cycle,

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

A physical cap would assign a vector or functional to a specified compact filling, on its boundary state space, with the original normalization and compatibility with cutting and gluing. Such a construction must compare the boundary insertion map, the numerical bulk state and the vacuum line on a common domain. It must also supply the map from uncut coefficient fields to the fields on the geometric cut. The normalized Gaussian, the based local line and the ordinary unary Ward equation provide concrete parts of this problem; they do not determine that cap.

The boundary algebra itself must therefore remain visible. Its products, quantum corrections and nonlinear relations decide which insertions are being compared, while its representations specify the possible boundary states. The next chapter returns to these algebras and to the quantum-group structures that their local operations can support.

## Source manuscripts {#ch11-source-manuscripts}

### 1. A numerical Gaussian on the native source graph {#ref-ch11-01}

### 2. Finite action integrals from the original coefficient Riesz spaces {#ref-ch11-02}

### 3. The common relative determinant of the native contraction {#ref-ch11-03}

### 4. The original coefficient heat finite part and its based vacuum line {#ref-ch11-04}

### 5. The source counterterm in the covariant connection {#ref-ch11-05}

### 6. Ordinary boundary Ward identity and full-source heat cells {#ref-ch11-06}
