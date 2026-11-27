# Arithmetic traces and positivity

At the two ends of the [K3 tube](#ch15-relative-donaldsonthomas-theory-produces-an-operator-first) we could choose cohomology classes, measure a matrix entry and then glue to take the trace. Suppose we are given just one number for every test function. What could the operators be?

Take a smooth complex function \(f\) supported in a small interval around \(\log 4\). The variable is the logarithm of a positive scale. In Weil's formula the finite-prime contribution there is \(-(\log 2)f(\log4)/2\). The prime is \(2\), the scale is its square, and the coefficient uses \(\sqrt4=2\). Two polar terms and a term from the real place also enter the number \(W(f)\). There is a second expression for it, summed over the zeros of the Riemann zeta function with their multiplicities. We seek a space constructed from the integers on which \(f\) acts with ordinary trace \(W(f)\).

Two successive changes of scale add their logarithms. Averaging them with weights \(f,g\) therefore calls for an action in which composition represents convolution. Reversing scale and conjugating the weight sends \(g\) to \(g^*(u)=\overline{g(-u)}\). If this operation also gives the Hilbert adjoint, the trace of \(g*g^*\) must be nonnegative. These two demands lead to different arithmetic tests.

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
**Definition (complete Weil functional).** With Lebesgue measure \(du\) on logarithmic scale and the Fourier sign above, put
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
Here \(\psi=\Gamma'/\Gamma\). The von Mangoldt function is \(\Lambda(p^k)=\log p\) for a prime \(p\) and \(k\ge1\), and vanishes on other integers. The evaluations \(H_f(0),H_f(1)\) are the polar terms. The term at zero and the integral containing \(\psi\) come from the real place. A test concentrated near \(\log4\) selects the positive orientation of the \(2^2\) term calculated above. Reflecting the test selects the other orientation with the same weight. Both tests still have their polar and real-place contributions. [The test algebra and its scalar functional][trace-foundations]

::: example {#ch16-composing-two-scale-tests title="Composing two scale tests"}
Choose a nonnegative even smooth function \(b\) supported in \((-\eta,\eta)\), with \(\int b^2\,du=1\) and \(0<\eta<\tfrac14\log(7/6)\). Let \(R_t b(u)=b(u-t)\). A pulse \(f_j=R_{\log j}b\) tests a scale close to \(j\). Substituting \(t=v+\log i\) in the convolution integral gives
\[
 f_i*f_j=R_{\log(ij)}(b*b),\qquad (b*b)(0)=1 .
\]
Take \(i=2\) and first \(j=2\), then \(j=3\). The two supports lie within \(2\eta\) of \(\log4\) and \(\log6\), respectively. In each support the indicated integer is the only one whose logarithm occurs. Denote the finite-prime term of (16.1) by \(P\). It follows that
\[
 P(f_2*f_2)=-\frac{\log2}{2},\qquad P(f_2*f_3)=0 .
\]
The second convolution still has value one at its centre. Its prime contribution vanishes because \(6\) is not a prime power. Both composed tests enter the polar and real-place terms of \(W\). An operator realisation must compose the actions of the two tests before taking their trace.
:::

The completed zeta function
\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
is entire. Let \(\rho\) run through its distinct zeros, let \(m_\rho\) be the multiplicity, and write \(w_\rho=-i(\rho-1/2)\). The explicit formula identifies (16.1) with
\[
W(f)=\sum_\rho m_\rho\widehat f(w_\rho).
\tag{16.2}
\]
The decay of the transform and the zero-counting bound give absolute convergence on the stated test class. The shift by \(1/2\) puts a zero \(\rho=\tfrac12+i\gamma\) at the real frequency \(w_\rho=\gamma\). Formula (16.1) therefore gives a way to construct the same functional before assigning any spectral coordinates to an operator.

**Conjecture (Riemann hypothesis).** Every zero \(\rho\) of \(\xi\) satisfies \(\operatorname{Re}\rho=1/2\). Equivalently, every centered frequency \(w_\rho\) in (16.2) is real.

**Definition (Weil form).** The Hermitian pairing of two complex tests \(f,g\) is \(W(f^**g)\), conjugate-linear in \(f\). Its diagonal is
\[
Q(g)=W(g*g^*).
\tag{16.3}
\]
**Conditional corollary (Weil positivity).** Assuming the Riemann hypothesis, \(Q(g)\ge0\) for every \(g\in C_c^\infty(\mathbb R;\mathbb C)\). Indeed \(\widehat{g*g^*}(z)=\widehat g(z)\overline{\widehat g(\bar z)}\), so (16.2) then sums the nonnegative numbers \(m_\rho|\widehat g(w_\rho)|^2\).

Weil's positivity criterion gives the converse. A nonreal \(w_\rho\) pairs two distinct evaluations, at \(w_\rho\) and \(\bar w_\rho\). In the exponentially decaying test algebra below one can prescribe the two transform values \(1,-1\) and zero at the other frequencies. The two terms in (16.2) then contribute \(-m_\rho\) each. Compact smooth approximation preserves the strict inequality \(Q<0\). Nonnegativity on *all* compact smooth tests therefore forces the conjecture. An ordinary Hilbert-space representation with \(W(f)=\operatorname{Tr}\pi(f)\) and \(\pi(g^*)=\pi(g)^*\) would give precisely this sign since \(Q(g)=\operatorname{Tr}(\pi(g)\pi(g)^*)=\|\pi(g)\|_{\mathrm{HS}}^2\), the squared Hilbert–Schmidt norm. The [fixed-window inequality](#ch16-whole-window-positivity-and-the-off-block-term) proves positivity directly for a restricted class of supports.

## Multiplicity, nilpotence and two different pairings {#ch16-multiplicity-nilpotence-and-two-different-pairings}

At a zero of multiplicity two, (16.2) gives twice the same Fourier value. Two independent eigenvectors would account for it. So would a two-dimensional Jordan block with the same eigenvalue. To see precisely what the trace has lost, let \(z\) act by multiplication in the algebra with basis \(1,z,\ldots,z^{m-1}\) and relation \(z^m=0\), for any \(m\ge1\). This is
\[
A_m=\mathbb C[z]/(z^m).
\]
For \(a=a_0+a_1z+\cdots+a_{m-1}z^{m-1}\), multiplication \(M_a\) is triangular in the monomial basis, with diagonal \(a_0\). Hence
\[
\operatorname{Tr}M_a=ma_0,
\qquad
B_{\mathrm{tr}}(a,b)=\operatorname{Tr}M_{ab}=ma_0b_0.
\]
Here the regular trace is the ordinary operator trace on the \(m\)-dimensional vector space \(A_m\). It counts the length \(m\). Its pairing has radical \((z)\) because multiplying by any \(z b\) leaves a zero diagonal.

To detect the coefficient \(a_j\), with \(0\le j<m\), multiply \(a\) by \(z^{m-1-j}\) and take the coefficient of \(z^{m-1}\). The result is \(a_j\). This gives the residue functional and its bilinear pairing
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
Every positive power of \(N\) has zero diagonal. Consequently the same trace \(me^{t\rho}\) would result from \(A=\rho I\) on \(m\) independent lines. For \(m\ge2\), apply \(A-\rho I\) to distinguish them. It vanishes on the independent lines. In the truncated algebra it is multiplication by \(z\), with Jordan chain \(1,z,\ldots,z^{m-1}\). It kills the last vector. At \(m=1\) the two operators coincide. A measure with mass \(m\) at one point gives a third possibility. It changes the norm of one coordinate, whose contribution to an ordinary operator trace still occurs only once.

::: example {#ch16-convolution-on-a-double-jet title="A convolution that detects a double jet"}
Fix any complex frequency \(w\) and let \(N\) act on \(\mathbb C[\varepsilon]/(\varepsilon^2)\) by multiplication by \(\varepsilon\). The Fourier value and its derivative give a two-dimensional action of compact smooth tests,
\[
 \pi(f)=\widehat f(w)I+\widehat f'(w)N .
\]
Indeed \(\widehat{f*g}=\widehat f\,\widehat g\), and the product rule together with \(N^2=0\) gives \(\pi(f*g)=\pi(f)\pi(g)\). On the same two-dimensional space put \(\sigma(f)=\widehat f(w)I\). Both representations have trace twice the product of the Fourier values at \(w\) on every convolution word.

To distinguish the actions, take \(b\in C_c^\infty(\mathbb R)\) with \(\int b=1\) and put \(h(u)=e^{-iwu}b(u)\). Then \(\widehat h(w)=1\). For \(f=ih'-wh\), integration by parts with the positive Fourier sign gives \(\widehat f(z)=(z-w)\widehat h(z)\). Thus \(\sigma(f)=0\), while \(\pi(f)\) sends \(1\) to \(\varepsilon\). Reading the coefficient of \(\varepsilon\) on this input gives one. Closing the same action to a trace gives zero. This calculation applies at any frequency. If a zero of \(\xi\) has multiplicity two, its term in (16.2) supplies the common trace of these two local actions.
:::

Hilbert adjunction is a further condition on the generator. Suppose \(A^*=1-A\) and \(\operatorname{Dom}A^*=\operatorname{Dom}A\) for a densely defined Hilbert-space generator. Then \(A-\tfrac12 I\) is skew-adjoint and \(\sigma(A)\subset\tfrac12+i\mathbb R\). For an eigenvalue \(\rho\) on that line the range of \(A-\rho I\) is orthogonal to its kernel. A nonzero eigenvector in that range, as required for a chain of length two, is therefore impossible. The bilinear pairing in (16.4) allowed just such chains. Integer summation gives a space on which the full multiplicity can be read even before a Hilbert norm is chosen. [Integer-summation middle complex, duality and primary blocks][integer-complex]

## Integer summation defines the complex before its spectrum {#ch16-integer-summation-defines-the-complex-before-its-spectrum}

How can a quotient constructed from the integers retain the derivative at a double zero? Start with an even Schwartz function \(\phi\) on the line. At each logarithmic scale \(x\), evaluate it at the nonzero points of the dilated lattice \(e^x\mathbb Z\) and add. Evenness pairs \(m\) with \(-m\), giving \(2\sum_{m\ge1}\phi(me^x)\). At large \(x\) the sum decays. At small scales the lattice becomes dense, so decay at the other end requires two conditions. Put \(S=\mathscr S(\mathbb R)^{\mathrm{even}}\) and
\[
S_{00}=\{\phi\in S:\phi(0)=0,\ \int_{\mathbb R}\phi=0\}.
\]
To keep all derivatives of the sum small at both ends of the scale axis, use the Sobolev space \(H^n(\mathbb R)\) of functions with square-integrable weak derivatives through order \(n\). For integers \(n\ge2\), define
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
As \(x\) tends to \(+\infty\), the lattice points \(me^x\) leave every bounded interval and Schwartz decay controls the sum. As \(x\) tends to \(-\infty\), the reflected sum in (16.6) has the same decay. The other terms are \(e^{-x}\int\phi\) and \(-\phi(0)\). Since their dependence on \(x\) differs, decay at this end requires both coefficients to vanish. These two boundary functionals give the polar lines with dilation characters zero and one.

Does allowing rational lattice points and all finite primes change this image? Let \(\mathbb A_{\mathbb Q}\) be the adele ring and \(C_{\mathbb Q}=\mathbb A_{\mathbb Q}^{\times}/\mathbb Q^{\times}\) its idele class group. The modulus \(|c|\), the product of the normalized local absolute values, measures the scale. Its kernel \(C^1\) is compact and over \(\mathbb Q\) identifies with \(\widehat{\mathbb Z}^{\times}\), where \(\widehat{\mathbb Z}=\prod_p\mathbb Z_p\). Average over \(C^1\) with Haar mass one to retain the dependence on scale. For this average \(P\) and the rational summation operator \(\Sigma\) put
\[
(PF)(c)=\int_{C^1}F(kc)\,dk,
\qquad
(\Sigma\Phi)(c)=\sum_{q\in\mathbb Q^{\times}}\Phi(qc).
\]
Here \(\Phi\) is an adelic Schwartz–Bruhat test: Schwartz at the real place and locally constant with compact support at the finite places. Impose \(\Phi(0)=\int_{\mathbb A_{\mathbb Q}}\Phi=0\), with finite additive volume \(\operatorname{vol}(\widehat{\mathbb Z})=1\). For \(\Phi=\phi\otimes1_{\widehat{\mathbb Z}}\), finite-place integrality selects exactly the nonzero integers, and \((P\Sigma\Phi)(e^x)=Z\phi(x)\). This is the averaging map in the following theorem.

For \(h\in E\) use the uncentered Mellin transform \(\mathcal Mh(s)=\int_{\mathbb R}h(x)e^{sx}\,dx\). To test whether \(h\) lies in the image of integer summation, evaluate \(\mathcal Mh\) and its derivatives at a zero \(\rho\) of multiplicity \(m_\rho\). The image condition is \((\mathcal Mh)^{(j)}(\rho)=0\) for every \(\rho\) and \(0\le j<m_\rho\). At a double zero both the value and the first derivative must vanish. The derivative evaluations are continuous already on \(E_n\) because \(|\operatorname{Re}\rho|<n\).

**Theorem (continuous integer-summation duality).** The map \(Z\) is a closed topological embedding. Its quotient \(M=E/Z(S_{00})\) is complete and nuclear. Norm-one adelic averaging identifies the actual averaged pole-free lattice-summation image with \(Z(S_{00})\). In \(\mathcal M E\) this image corresponds exactly to the ideal cut out by the preceding vanishing conditions. At each weighted Sobolev stage \(E_n\), the annihilator of the image is the norm closure in \(E_n'\) of the span of these derivative evaluations. The inductive limit of these closed spaces gives the strong continuous dual of \(M\). Evaluation yields a nondegenerate hypocontinuous pairing, continuous uniformly when either argument ranges over a bounded set. It extends to the completed projective bornological tensor product for the bounded sets of these locally convex spaces. [An integer-summation middle complex and its continuous dual][integer-complex]

The first step of the proof is arithmetic inversion, after removing the factor of two in \(Z\). On logarithmic weighted spaces with exponent \(\sigma>1\), the operators
\[
\sum_{m\ge1}\lambda_{-\log m},
\qquad
\sum_{m\ge1}\mu(m)\lambda_{-\log m}
\]
converge in operator norm and are inverse. Here \(\lambda_t\phi(u)=\phi(e^{-t}u)\) and \(\mu(m)\) is the Möbius function. In the product of the two series, the coefficient of dilation by \(n\) is \(\sum_{m\mid n}\mu(m)\), which is one for \(n=1\) and zero for \(n>1\). The bound \(\sum_{m\ge1}m^{-\sigma}<\infty\) justifies collecting these coefficients. Fourier reflection then controls both ends and gives inverse continuity in Schwartz seminorms. This proves closed range before spectral synthesis is used.

For \(\operatorname{Re}s>1\), change variables \(u=me^x\) in the term with index \(m\). Its Mellin integral acquires a factor \(m^{-s}\). Summing first on this half-plane gives \(\mathcal M(Z\phi)(s)=2\zeta(s)\int_0^\infty\phi(u)u^s\,du/u\). To use this identity at a nontrivial zero, continue it from the half-plane of summation. Evenness and \(\phi(0)=0\) give \(\phi(u)=O(u^2)\) near zero, so the integral on the right is holomorphic for \(\operatorname{Re}s>-2\). At \(s=1\) it equals \(\tfrac12\int_{\mathbb R}\phi=0\), cancelling the pole of \(\zeta\). The left side is entire because \(Z\phi\in E\). Hence the identity holds throughout the critical strip, where the factor \(\zeta(s)\) forces \(\mathcal M(Z\phi)\) to vanish to order at least \(m_\rho\) at \(\rho\). The converse requires division. An explicitly differentiated Gaussian supplies an arithmetic convolution generator with Mellin transform \(\xi(s)\). Quantitative division on vertical strips, followed by Gaussian regularization, gives the full vanishing ideal. Derivative evaluations at the zeros consequently descend to continuous functionals on the quotient, with every multiplicity retained.

On a jet of order \(j\) at \(\rho\), the normalized dual functional takes \([h]\in M\) to \((\mathcal Mh)^{(j)}(\rho)/j!\). This descends to the quotient by the vanishing ideal. The dual is complex-linear. Under contragredient dilation an exponent \(\rho\) becomes \(-\rho\). Tensoring with the line of character \(e^t\) changes it to \(1-\rho\), so the equivariant evaluation takes values in this weight-one line. As in (16.4), evaluation retains the higher jets without furnishing a positive norm.

## A geometric construction of the full trace {#ch16-a-geometric-construction-of-the-full-trace}

The quotient \(M\) and its dual retain the zero jets. The Hilbert-space trace in (16.8) requires a Hilbert completion on which the test operators have summable singular values. To obtain them from the same integer sum, fix \(a>1/2\) and use the convolution algebra
\[
\mathcal A_a=
\left\{f\in C^\infty(\mathbb R):
p_{a,N}(f)=\sum_{j=0}^N\int e^{a|u|}|f^{(j)}(u)|\,du<\infty
\text{ for every }N\right\}.
\]
It is a complete nonunital Fréchet star algebra. Its Fourier transforms are holomorphic in \(|\operatorname{Im}z|<a\); on smaller strips they decrease faster than every power in the real direction. Compact smooth tests are dense. The identity for convolution would be the Dirac distribution, which is outside this function algebra.

To use the integer sum as a relation for convolution, its Mellin variable must have the same origin as the Fourier variable in (16.2). Multiplication by \(e^{u/2}\) shifts the Mellin exponent to \(1/2+iz\). Counting only positive integers removes the factor of two in (16.5). With these normalizations put
\[
\theta_v(u)=e^{u/2}\sum_{n\ge1}v(ne^u)
=\tfrac12e^{u/2}(Zv)(u),\qquad v\in S_{00},
\qquad
\mathcal J_a=
\overline{\{\theta_v:v\in S_{00}\}}^{\,\mathcal A_a}.
\]
Poisson summation puts each \(\theta_v\) in \(\mathcal A_a\). In the sum defining it, translation of \(u\) dilates the argument of \(v\), and integration against \(f\in\mathcal A_a\) gives convolution. The closed span is a convolution star ideal. In the Hausdorff quotient \(\mathcal A_a/\mathcal J_a\) it is these specified integer-summation functions that act as zero.

Choose \(1/2<s<\min(a,1)\). To retain the two boundary terms in a Hilbert space, both \(v(0)\) and \(\mathcal Fv(0)\) must extend from Schwartz functions. The Fourier transform interchanges them. This leads to a norm that weights \(v\) and \(\mathcal Fv\) equally. Complete the even Schwartz functions in the norm
\[
\|v\|_{\mathscr V_s}^2
=\int_0^\infty x^{2s}
\bigl(|v(x)|^2+|\mathcal Fv(x)|^2\bigr)\,dx.
\tag{16.7}
\]
Both weights in (16.7) vanish at the origin. To control \(v(0)\) by this norm, first bound the ordinary \(L^2(\mathbb R)\) norm of \(v\). Choose \(0<r<1/4\) and let \(P_x,P_\xi\) restrict to \([-r,r]\) in position and frequency. The kernel of \(P_x\mathcal F^{-1}P_\xi\) has modulus one on a square of area \(4r^2\), so its Hilbert–Schmidt norm is \(2r\). Write \(v=(1-P_x)v+P_xv\). In the second term insert \(P_\xi+(1-P_\xi)\) between \(\mathcal F^{-1}\) and \(\mathcal Fv\). Outside either interval the corresponding weight is at least \(r^s\). The twice restricted term has norm at most \(2r\|v\|_2\). Consequently
\[
 (1-2r)\|v\|_2
 \le r^{-s}\bigl(\||x|^s v\|_2+\||\xi|^s\mathcal Fv\|_2\bigr).
\]
For even functions both weighted norms on the right are controlled by (16.7), since their squared integrals on the line are twice those on its positive half.

Fourier inversion and Cauchy–Schwarz now give
\[
 |v(0)|\le
 \left(\int_{\mathbb R}\frac{d\xi}{1+|\xi|^{2s}}\right)^{1/2}
 \left(\|v\|_2^2+\||\xi|^s\mathcal Fv\|_2^2\right)^{1/2}.
\]
The first factor is finite exactly when \(s>1/2\), and the preceding bound controls the second. Fourier transformation exchanges the two terms of (16.7), so \(\mathcal Fv(0)\) is continuous as well. Both boundary evaluations therefore extend to the completion used in the theta complex.

**Construction (the Hilbert theta complex).** Write \(X_{\pm s}=L^2(\mathbb R,e^{\pm2su}du)\). In \(X_s\oplus X_{-s}\), take the diagonal \((h,h)\) for \(h\in X_s\cap X_{-s}\). The other closed subspace is the image of \(V=\mathscr V_s\) under the bounded, bounded-below extension of the map on even Schwartz functions
\[
 \begin{aligned}
 (dv)(u)&=\bigl(\theta_v(u),\theta_{\mathcal Fv}(-u)\bigr),\\
 \theta_v(u)&=e^{u/2}\sum_{m\ge1}v(me^u).
 \end{aligned}
\]
The formula for \(\theta_v\) now allows arbitrary boundary values in this pair. By (16.6) its first component minus its second is \(\tfrac12(\mathcal Fv(0)e^{-u/2}-v(0)e^{u/2})\). The two exponentials are linearly independent, so \(dv\) is diagonal exactly when both boundary evaluations vanish. Modulo the diagonal the two exponential characters survive. Let \(U\) be the closed sum of the diagonal and \(dV\). The complex \(\mathscr C_s=[V\xrightarrow d U]\) has degrees \(-1,0\). Every class in \(K_s=U/dV\) has a diagonal representative. Two such representatives give the same class exactly when their difference belongs to the intersection of the diagonal with \(dV\), the closed pole-free theta image just identified.

On a diagonal class \([h]\) of \(K_s\), the integrated operator acts by \(\Pi_{s,a}(f)[h]=[f*h]\). It factors through \(\mathcal A_a/\mathcal J_a\). On the complex the corresponding strict action \(\rho_f\) integrates dilations on \(V\) and convolves on \(U\). To take a trace there, choose a nonnegative even smooth bump \(b\), supported in \([-1,1]\), with integral one, and put \(\phi(u)=\int_{-\infty}^u b(v)\,dv\). A bounded degree-minus-one smoothing homotopy \(\mathsf H_f:U\to V\), constructed using this cutoff, gives
\[
\Lambda_f=\rho_f-\delta\mathsf H_f,
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

To see the cancellation in (16.8), split \(U=dV\oplus(dV)^\perp\). On \(dV\) the chain-map identity gives \(\Lambda_f^0 d=d\Lambda_f^{-1}\), where the superscript denotes cochain degree. Since \(d:V\to dV\) is a bounded isomorphism, this diagonal block has exactly the trace of the degree-minus-one operator. It cancels in the supertrace. The other diagonal block acts on \(U/dV\) and gives its ordinary trace.

The evaluation of the supertrace still uses both ends of the scale axis. The two Poisson boundary characters give \(H_f(0)+H_f(1)\). The prime-power operators give the two translates at \(\pm\log n\), and the Fourier defect gives the real-place term in (16.1). This computes the trace without using the zero ordinates to construct the quotient.

For the two pulses about scales \(2,3\), (16.8) evaluates the trace of \(\Pi_{s,a}(f_2)\Pi_{s,a}(f_3)\). In the Mellin transform, translation by \(\log6\) multiplies \(H_f(s')\) by \(6^{s'-1/2}\), where \(s'\) denotes the Mellin variable. Since the profile \(b\) is even, \(H_b(0)=H_b(1)\). The polar contribution of the composite is consequently
\[
 H_{f_2*f_3}(0)+H_{f_2*f_3}(1)
   =(6^{-1/2}+6^{1/2})H_b(1)^2 .
\]
The real-place integral also enters, while the finite-prime sum is zero. Thus the integer-summation representation realises composition even at a scale with no prime-power atom. [The two scale tests](#ch16-composing-two-scale-tests)

One can decide whether an equivalent Hilbert norm on this quotient would turn the convolution action into a star representation. Let \(U_t^{(s)}\) be translation by \(t\) on \(K_s\). At every \(1/2<s<\min(a,1)\) and every real \(t\ne0\) its spectrum and its Fredholm essential spectrum both equal
\[
 \{\lambda\in\mathbb C:e^{-s|t|}\le|\lambda|\le e^{s|t|}\}.
\]
In the Fourier representation on the strip \(|\operatorname{Im}z|<s\), translation is the compression of multiplication by \(e^{itz}\) to the Hardy quotient by the inner factor of the theta divisor. Applying the multiplier bound to \(t\) and \(-t\) gives the two radii. For the reverse inclusion, there are unit horizontal intervals containing arbitrarily many zeros counted with multiplicity. Translating those intervals moves their zeros into a fixed box strictly inside the strip, since \(|\operatorname{Im}w_\rho|<1/2<s\). The translated inner factors tend to zero on compact sets, and the translated quotient projections tend strongly to the identity. Projecting a point-evaluation vector and translating it back gives unit vectors tending weakly to zero, on which the adjoint acts arbitrarily close to the conjugate of the corresponding multiplier value, up to a unit phase. These values fill the open annulus, and essential spectrum is closed.

The outer radius exceeds one. Spectrum is preserved by an equivalent norm, whereas a unitary has spectrum on the unit circle. If the integrated tests gave a star representation in that norm, translating a real even approximate identity would make \(U_t^{(s)}\) unitary. Thus changing the norm within its equivalence class cannot produce the desired positive realization. The integrated smooth operators in (16.8) still have their full trace. The strip-width assumption is needed to put the entire translated zero box strictly inside the Hardy strip.

## The trace domain and its coherent multiplication {#ch16-the-trace-domain-and-its-coherent-multiplication}

The smoothed representative \(\Lambda_f\) has two diagonal components with finite trace. Its construction also used a homotopy mapping \(U\) back to \(V\). To multiply such representatives and compare their traces we need a domain for both kinds of maps.

**Definition (trace-class endomorphisms of the theta complex).** For Hilbert spaces \(H,K\), write \(\mathfrak S_1(H,K)\) for the operators \(H\to K\) whose singular values have finite sum, and \(\mathfrak S_1(H)=\mathfrak S_1(H,H)\). The identity on an infinite-dimensional space has singular value one in every direction. For \(\mathscr C_s=[V\to U]\) the proper trace domain has two degrees,
\[
\begin{aligned}
\mathfrak I^0&=\{(T^{-1},T^0)\in\mathfrak S_1(V)\oplus\mathfrak S_1(U):
dT^{-1}=T^0d\},\\
\mathfrak I^{-1}&=\mathfrak S_1(U,V).
\end{aligned}
\]
Composition and \(\delta\) make \(\mathfrak I\) a complete proper nonunital differential ideal of the bounded degree-zero chain maps and degree-minus-one homotopies. Its closed graded trace is zero in degree minus one and satisfies
\[
\tau(T)=\operatorname{Tr}_UT^0-\operatorname{Tr}_VT^{-1},
\qquad \tau(\delta K)=0.
\]
The last identity follows from \(\operatorname{Tr}(dK)=\operatorname{Tr}(Kd)\). Orthogonal splitting of the closed range of \(d\) contracts this ideal onto \(\mathfrak S_1(K_s)\) by a split differential-algebra quasi-isomorphism. The chain-map equation involves \(d\), whereas taking ordinary Hilbert adjoints involves \(d^*\); a positive differential-star structure does not follow. [Trace-class coefficient homotopies][trace-operations]

On \(K_s\), composing the operators for \(f\) and \(g\) gives the operator for \(f*g\). On the complex, the product of the representatives need only agree with the representative of \(f*g\) after passing to \(U/dV\). Their difference therefore sends \(U\) into \(dV\). This is exactly the subspace on which \(d\) has a bounded inverse. There is a trace-class homotopy \(K(f,g):U\to V\) with
\[
\Lambda_f\Lambda_g-\Lambda_{f*g}=\delta K(f,g).
\tag{16.9}
\]
Write \(\Delta^0\) for the component of this difference on \(U\). Then \(K(f,g)=d^{-1}\Delta^0\), with \(d^{-1}\) restricted to \(dV\). In degree zero this gives \(dK=\Delta^0\). In degree minus one the chain-map equation gives the other component \(Kd\). On three tests the two ways of applying this correction satisfy
\[
\Lambda_fK(g,h)-K(f,g)\Lambda_h
+K(f,g*h)-K(f*g,h)=0.
\tag{16.10}
\]
The associativity of convolution makes the differential of the left side of (16.10) zero. Its value is a map \(U\to V\). Since \(d:V\to U\) is injective, a closed endomorphism of this degree is zero. Products of two degree-minus-one homotopies also vanish, because each has source \(U\) and target \(V\). Consequently the bar map on a word sums over partitions into consecutive blocks of size one or two. A singleton contributes \(\Lambda\), a pair contributes \(K\), and (16.10) compares the two possible first mergers of three entries. Together with the mixed-degree identities this gives a coalgebra chain map.

This also has an analytic completion theorem. Using the arithmetic ideal \(\mathcal J_a\) defined above, form the coefficient complex \(\mathcal E=[\mathcal J_a\to\mathcal A_a]\) in degrees \(-1,0\). Its degree-zero multiplication and action on \(\mathcal J_a\) are convolution; products of two degree-minus-one terms are zero. On tensor words use the completed projective seminorms
\[
P_{R,N}(x)=\sum_{n\ge0}R^nq_{N,\pi}(x_n),\qquad R>0,
\]
where \(q_N\) is the sum of the two coefficient seminorms. In this nonfactorial entire completion, the bar map is continuous with radius bound
\[
P_R^{\mathfrak I}(Gx)\le P_{C_1R+\sqrt{C_2R},4}(x).
\]
The estimate counts the same singleton/pair partitions. It extends the actual identities, not just a scalar trace, through the specified completion.

The radius estimate controls the sum over lengths of words in the convolution tests. Locality concerns a different variable, the separation of two field insertions. For example, impose the equation \(u=z_1-z_2=0\) twice. The two degree-\(-1\) Koszul generators then satisfy \(de_1=de_2=u\). In the basis \(e_1,e_2-e_1\), the first generator resolves the diagonal and the second gives a degree-\(-1\) class on it. On a fixed finite graph of affine collision equations with nonempty common zero set, the normal-jet sheaf records densities on that set and their finite normal derivatives. To give these jets operator coefficients, use the action of \(\mathcal E\) on \(K_s\). It sends a degree-zero test \(f\) to \(\Pi_{s,a}(f)\) and the degree-\(-1\) copy of \(\mathcal J_a\) to zero.

Resolve the coefficients of the graph module by the bar construction. Take for \(P\) the resulting free resolution of that module, or its extension by differential operators and tangent generators that resolves the normal jets with their exterior classes. The supported mapping complex consists of continuous module maps from \(P\) to a given target, compatible with restriction to smaller open sets. One may also form finite words of maps through modules whose sections admit local scalar contractions. In a word beginning \(P\to C\), a continuous contraction on the sections of \(C\) induces a bounded contraction on the space of maps \(P\to C\). It therefore extends through the completed tensor product of the map spaces. Filtering by word length shows that adjoining these words preserves the cohomology sheaves of the original mapping complex after ordinary sheafification.

Oriented residues give products on fixed finite affine supports. A [local arithmetic field realization](#problem-arithmetic) must still supply a local vacuum and match these operations with field products, including their contact terms and their compatibility under successive collisions. Even for [two charged rays](03-local-fields.md#ch03-charged-current-contour), the normalized oscillator-free coefficient \((z_1-z_2)^{\alpha\beta/k}\) in the outgoing sector of charge \(\alpha+\beta\) has trivial full-turn monodromy exactly when \(\alpha\beta/k\in\mathbb Z\), with the frames fixed and \(k\ne0\).

There is a preparation on the [theta quotient](#ch16-a-geometric-construction-of-the-full-trace) itself. For \(1/2<s<\min(a,1)\), let \(e_s\) be the normalized class of \(u\mapsto e^{-u^2}\) in \(K_s\). Its translates span a dense subspace, and a test \(f\) prepares the vector \(\Pi_{s,a}(f)e_s\). Orthonormalizing the rational translates of \(e_s\) and omitting dependent vectors gives a basis \((b_n)\) of \(K_s\). Since \(\Pi_{s,a}(f)\) is trace class, (16.8) reads \(W(f)=\sum_n\langle b_n,\Pi_{s,a}(f)b_n\rangle\) with absolute convergence. The linking construction adjoins a line fixed by translations. For a prepared vector \(v\), the creator \(|v\rangle\langle\Omega|\) sends the unit vector \(\Omega\) on that line to \(v\).

To test whether a cyclic vector gives the counting trace, start with a finite-dimensional Hilbert space \(K\) and adjoin a unit vector \(\Omega\) orthogonal to it. Extend an operator \(T\) on \(K\) by zero on this new line. Then
\[
\operatorname{Tr}(T\oplus0)=\operatorname{Tr}T,
\qquad \langle\Omega,(T\oplus0)\Omega\rangle=0.
\]
Rank-one maps \(c(v)=|v\rangle\langle\Omega|\) and \(a(w)=|\Omega\rangle\langle w|\) can make \(\Omega\) cyclic, but
\[
[a(w),c(v)]=\langle w,v\rangle P_\Omega-|v\rangle\langle w|
\]
is generally nonzero. For example take \(w=v\) of norm one. The commutator acts by \(+1\) on \(\Omega\) and by \(-1\) on \(v\). If the fields are constant, no power of their separation annihilates this operator. The new vector can generate the space even as its expectation on \(T\oplus0\) remains zero. In the arithmetic linking construction the counting trace stays on the corner that annihilates the added invariant vector. [Invariant vacuum and linking fields][linking-fields]

## A positive representation and its exact missing remainder {#ch16-a-positive-representation-and-its-exact-missing-remainder}

At a real centered zero \(\gamma\) the term in (16.3) is a positive square. To obtain it from a Hilbert-space trace, count how often its Fourier value must appear on the diagonal. A double zero needs two coordinates. Putting weight two in the norm of a single coordinate still gives only one diagonal entry. Differences of polynomially weighted quotient traces separate the zeros into layers. The \(n\)th difference includes each real centered zero whose multiplicity reaches \(n\), giving the positive functional
\[
\sigma_n(f)=\sum_{\substack{\gamma\in\mathbb R\\m_\gamma\ge n}}
\widehat f(\gamma),\qquad n\ge1.
\]
Here \(\gamma\) ranges over the real centered zeros and \(m_\gamma\) is their multiplicity. In the form \(\sigma_n(f^**g)\) each term is \(\overline{\widehat f(\gamma)}\widehat g(\gamma)\). Quotient the test algebra by its zero-norm vectors and complete to obtain \(G_n\). On the \(n\)th layer, \(f\) acts by multiplying the \(\gamma\) coordinate by \(\widehat f(\gamma)\). Thus conjugate reflection of the test acts by the Hilbert adjoint. The direct sum \(G_{\mathrm{crit}}=\bigoplus_nG_n\) carries the continuous ordinary star representation
\[
\pi_{\mathrm{crit}}:\mathcal A_a/\mathcal J_a\longrightarrow\mathfrak S_1(G_{\mathrm{crit}}),
\]
with
\[
\operatorname{Tr}\pi_{\mathrm{crit}}(f)
=\sum_{\gamma\in\mathbb R}m_\gamma\widehat f(\gamma).
\tag{16.11}
\]
For instance, a real centered zero of multiplicity two contributes once to \(G_1\) and once to \(G_2\). On the corresponding two one-dimensional summands \(\pi_{\mathrm{crit}}(f)\) has eigenvalue \(\widehat f(\gamma)\) twice, giving trace \(2\widehat f(\gamma)\). Placing measure weight two on one point would rescale its Hilbert norm but leave a single eigenvector. More generally a zero of multiplicity \(m\) occurs in precisely \(m\) layers. The generator acts there by the real scalar \(\gamma\). Its self-adjoint domain is \(\sum_{n,\gamma}\gamma^2|x_{n,\gamma}|^2<\infty\), and its inverse moments of order at least two converge. [Polynomial quotients, positive multiplicity layers][positive-layers]

Comparing (16.11) with the [geometric theta trace](#ch16-a-geometric-construction-of-the-full-trace) gives
\[
W(f)-\operatorname{Tr}\pi_{\mathrm{crit}}(f)
=\sum_{w_\rho\notin\mathbb R}m_\rho\widehat f(w_\rho).
\tag{16.12}
\]
A smooth test need not isolate a single zero by itself. In the decaying test algebra one can isolate a nonreal spectral evaluation as in the [positivity criterion](#ch16-the-complete-arithmetic-functional). Thus vanishing of (16.12) on every test is equivalent to all centered zeros being real. The layer construction proves positivity of its own representation. Equality of its trace with \(W\) on all tests remains the Riemann hypothesis. A comparison of local collision operations has its own coefficient maps to construct.

::: figure fig-programme-context-arithmetic

::: figure fig-weil-trace-remainder

## What integral arithmetic points forget {#ch16-what-integral-arithmetic-points-forget}

A jet at a complex zero records derivatives as well as its scalar value. At a finite prime \(p\) one can ask the corresponding question with integral coefficients, including \(p=2\). Work with \(p\)-torsionfree, \(p\)-complete delta test rings. A Frobenius lift \(\varphi\) is a ring endomorphism reducing to \(x\mapsto x^p\) modulo \(p\). It determines \(\delta(x)=(\varphi(x)-x^p)/p\). On \(\mathbb Z_p\), take \(\varphi=\mathrm{id}\). A point \(a\in\mathbb Z_p\) then gives the height-\(h\) list \(a,\delta a,\ldots,\delta^{h-1}a\). To retain the neighbourhood of such a list, put
\[
A_h=\mathbb Z_p[x_0,\ldots,x_{h-1}],\quad
R_h=\varprojlim_nA_h/p^n,\quad
I_h=(p,x_i^p-x_i:i<h),\quad
B_h=\varprojlim_nA_h/I_h^n.
\]
Here \(R_h\) completes polynomial coefficients \(p\)-adically. The equations \(x_i^p-x_i=0\bmod p\) define all of \(\mathbb F_p^h\), and \(B_h\) completes along this whole locus. For each \(c\in\mathbb F_p^h\), choose the integer representatives \(0\le c_i<p\) in \(\mathbb Z_p\). With these lifts, Chinese remainders give
\[
B_h\simeq\prod_{c\in\mathbb F_p^h}\mathbb Z_p[[z_0,\ldots,z_{h-1}]],
\qquad x_i=c_i+z_i.
\tag{16.13}
\]
For \(h=1,\ p=2\), (16.13) has two factors. In the factor labelled \(0\) the coordinate is \(z=x_0\), and in the one labelled \(1\) it is \(z=x_0-1\). Specifying a function in each factor retains its entire formal dependence on \(z\). Evaluation at the mark instead takes a scalar. The map \(j_h:R_h\to B_h\) is injective, also modulo each \(p^n\). Indeed translation by any chosen \(c\) is a polynomial automorphism, and a polynomial over \(\mathbb Z/p^n\) injects into the corresponding formal power-series ring.

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
At height two and \(p=2\) this says \(h_0=x_0^2+2x_1-x_0\) vanishes at every pair \((a,\delta a)\), whereas \(D_0h_0=-2\equiv2\bmod 4\). Thus the ideal of functions vanishing at the arithmetic points is not stable under the first normal derivation. The formal factors in (16.13) retain the missing direction.

At height two the [first normal derivative at the origin](#atlas-c-ar-08) sends \(f\) to \((D_0f)(0,0)=p\,\partial_{x_0}f(0,0)\), since \(D_0x_1\) vanishes there. It kills \((x_0,x_1)^2\) and takes \(h_0\) to \(-p\bmod p^2\). Thus a functional supported on the first infinitesimal neighbourhood of the origin detects a class whose value at every scalar arithmetic point is zero.

The same translation gives normal operators of higher order. Assign \(t_i\) weight \(p^i\). For a coefficient functional \(\lambda\) supported in bounded weight, apply \(\lambda\) to the displacement variables in \(\alpha(f)\). This defines \(D_\lambda f=(1\otimes\lambda)\alpha(f)\), a finite combination of coefficient extractions. For displacements \(t,v\), the \(i\)th parameter of the composite is the integral polynomial \(S_i(pt,pv)/p\). At \(p=2\) its second coordinate is \(t_1+v_1-2t_0v_0\). This addition law defines the product of the coefficient functionals. Their convolution gives the normal operators. An enriched congruence arrow retains both its arithmetic labels and its normal displacements. Its nerve is the diagram of finite strings of composable arrows, with composition deleting the common middle object. The comparison preserves these maps, congruence depth and coefficient reduction. Frobenius takes a height-\(h\) coordinate to height \(h+1\). In the comparison with displacements whose Frobenius images satisfy the congruence conditions, the coefficients on the source are also pulled back by Frobenius. Fourier–Tate operations on locally constant labels use a compatible character and a coefficient field in which \(p\) is invertible. [Integral arithmetic tubes with their normal operations][integral-tubes]

For a locally constant label the normalized average is already a finite sum. To average a varying function, compare one residue class with its \(p\) children. Let \(f:\mathbb Z_p\to E\), where \(E\) is a Banach space over \(\mathbb C_p\) with \(|p|_p=p^{-1}\), and suppose \(\|f(x)-f(y)\|\le H|x-y|_p^\alpha\). At depth \(N\) choose representatives \(x_a\) and put \(I_N=p^{-N}\sum_{a\bmod p^N} f(x_a)\). The child values differ from their parent by at most \(Hp^{-\alpha N}\). In the nonarchimedean norm the sum of these differences is bounded by their maximum, while \(|p^{-(N+1)}|_p=p^{N+1}\). Thus \(\|I_{N+1}-I_N\|\le pH\,p^{-(\alpha-1)N}\). For \(\alpha>1\) this gives convergence independently of the representatives.

For a character of exact conductor \(p^m>1\), its values on the children sum to zero in each parent. Subtracting the parent value of \(f\) gives \(\|\widehat f(\xi)\|\le p^\alpha H p^{-(\alpha-1)m}\). The Fourier partial sum is the normalized average on \(x+p^m\mathbb Z_p\), giving uniform inversion. At \(0<\alpha\le1\) the scalar example \(f(x)=x\) belongs to the class. Since \(f(x+1)=f(x)+1\), a translation-invariant linear integral on the full class would satisfy \(I(1)=0\). The normalization \(I(1)=1\) is therefore impossible on this larger domain.

The polynomial comparison extends to ordered collision diagrams. At finite \(p\)-adic precision, a collision equation \(f=0\) gives a two-term complex \([A\to A[1/f]]\). The second term restricts to the open set where \(f\) is invertible. Tensor these complexes for the prescribed equations in their given order. For the comparison replace the polynomial coefficients by the completed coefficients \(B\) before localization, and take the \(p\)-adic inverse limit last. The comparison is termwise injective and preserves independent normal operations, permitted substitutions and both empty tensor factors. For a partial diagonal, join the points that must coincide by a tree in each block. The resulting forest has a root coordinate in each block and independent difference coordinates on its edges. Following the edges from the root recovers every point by arithmetic addition. For these supports with no extra denominator, the induced map on supported cohomology is injective and preserves the ordered partial residues. Arbitrary extra denominators are outside that cohomology theorem. Frobenius carries the diagram to the higher-height diagram with its transformed support list. [Integral normal operations at an arithmetic marked point][integral-collisions]

The normal derivation also restricts which operators can share a cyclic trace. Let \(M_{x_0}\) denote multiplication by \(x_0\). For every \(f\) the Leibniz rule gives \(D_0(x_0f)-x_0D_0f=(D_0x_0)f=pf\). Thus
\[
[D_0,M_{x_0}]=pI.
\tag{16.15}
\]
Let \(e\) be a residue-class idempotent. Applying the derivation to \(e^2=e\) gives \((1-2e)D_0e=0\). Since \((1-2e)^2=1\), this forces \(D_0e=0\) even at \(p=2\). The Leibniz rule now gives \(D_0(x_0e)=pe\), hence \([D_0,M_{x_0e}]=pM_e\). To see what cyclicity requires on operators of higher order, fix \(h\ge1\) and write \(M_f\) for multiplication by \(f\in B_h\). For \(\alpha\in\mathbb N^h\), let \(D_\alpha g\) be the coefficient of \(t^{[\alpha]}=\prod_{i<h}t_i^{[\alpha_i]}\) in the congruence translate of \(g\). Then \(D_{\mathbf 0}=I\), while \(D_{e_0}\), for \(e_0=(1,0,\ldots,0)\), is the derivation called \(D_0\) in (16.15). Let \(\mathscr D_h\subseteq\operatorname{End}_{\mathbb Z_p}(B_h)\) be the unital algebra generated by the multiplications and these finite-weight normal operators. Its coefficients belong to the completed position ring \(B_h\). Its elements are finite sums of finite products.

**Corollary (cyclic traces on the position–normal algebra).** Let \(L\) be a \(p\)-torsionfree \(\mathbb Z_p\)-module. Every \(\mathbb Z_p\)-linear trace \(\tau:\mathscr D_h\to L\) satisfying \(\tau(AB)=\tau(BA)\) for all \(A,B\in\mathscr D_h\) vanishes identically.

*Proof.* In the translate of \(x_0g\), the first factor is \(x_0+pt_0\). Multiplying \(t^{[\alpha]}\) by \(t_0\) gives \((\alpha_0+1)t^{[\alpha+e_0]}\). Extract the coefficient indexed by \(\alpha+e_0\) and multiply by \(f\). The \(x_0\) term cancels in the commutator, leaving
\[
 [M_fD_{\alpha+e_0},M_{x_0}]
   =p(\alpha_0+1)M_fD_\alpha .
\]
Cyclicity kills the left side. The integer \(p(\alpha_0+1)\) is a power of \(p\) times a unit of \(\mathbb Z_p\), so it acts injectively on \(L\). Hence \(\tau(M_fD_\alpha)=0\) for every \(f,\alpha\).

These operators span \(\mathscr D_h\). Indeed, taking a coefficient in the product of two translates gives
\[
 D_\alpha M_g
 =\sum_{\beta+\gamma=\alpha}
   \binom{\alpha}{\beta}M_{D_\beta g}D_\gamma,
 \qquad \binom{\alpha}{\beta}=\prod_{i<h}\binom{\alpha_i}{\beta_i}.
\]
This finite sum moves a multiplication to the left. Composition of two extractors is their convolution. The arithmetic addition polynomials preserve the weights \(\mathrm{wt}(t_i)=p^i\), so the convolution uses only indices of the combined weight, of which there are finitely many. Repeating the two operations expresses every word as a finite sum of \(M_fD_\alpha\). Linearity proves the claim. ∎

The annihilator identity \(p(\alpha_0+1)\tau(M_fD_\alpha)=0\) also holds for targets with \(p\)-torsion. Which nonzero values can a trace take? Choose one of the two formal disks in (16.13) at \(p=2\), \(h=1\). Write \(z\) for multiplication by its coordinate and \(d=2\partial_z\) for the first extractor. With derivatives on the right, an operator has the form \(\sum_{j=0}^N f_j(z)d^j\). Read the coefficient of \(z\) in \(f_1\). It takes the value \(1\) on \(zd\). If \(g(z)=\sum_{k\ge0}b_kz^k\), the two generator commutators that can contribute to this reading are
\[
 [d,g d]=2g' d,\qquad [z,g d^2]=-4g d .
\]
Their \(zd\) coefficients are \(4b_2\) and \(-4b_1\). Polynomial commutators reduce to brackets with \(z\) or \(d\). A fixed coefficient of a product of finite-order operators uses only finitely many Taylor coefficients, so the same divisibility holds for formal inputs. Reduction of this coefficient modulo four therefore gives a cyclic trace. Modulo eight, the same reading takes the value \(4\) on \([d,z^2d]=4zd\).

**Definition (commutator quotient).** For an algebra \(A\) over \(R=\mathbb Z_p\), let \([A,A]_R\) be the \(R\)-linear span of the elements \(UV-VU\), for \(U,V\in A\). The quotient module \(HH_0(A/R)=A/[A,A]_R\) is the relative zeroth Hochschild homology. Every cyclic \(R\)-linear map from \(A\) factors uniquely through this module. The distinction from a two-sided ideal matters already on the disk above. Since \([d,z]=2\), the ideal generated by the commutators contains \(2zd\), on which the trace modulo four takes the value \(2\).

**Theorem (finite-order traces on formal arithmetic disks).** Fix a prime \(p\) and a finite height \(h\ge1\). On the disk \(c\in\mathbb F_p^h\) in (16.13) put \(d_i=p\partial_{z_i}\) and \(d^\beta=\prod_{i<h}d_i^{\beta_i}\). An operator in \(\mathscr D_h\) has a unique expression on this disk as a finite sum \(\sum_\beta f_{c,\beta}(z)d^\beta\), with \(f_{c,\beta}\in R[[z_0,\ldots,z_{h-1}]]\). Every such choice on the finitely many disks gives an operator in \(\mathscr D_h\). Write \(a_{c,\alpha,\beta}\) for the coefficient of \(z^\alpha\) in \(f_{c,\beta}\). For \(\alpha,\beta\in\mathbb N^h\) set
\[
 s(\alpha,\beta)=1+\min_{0\le i<h}
             \{v_p(\alpha_i+1),\,v_p(\beta_i+1)\},
 \qquad v_p(p)=1 .
\]
Reducing each \(a_{c,\alpha,\beta}\) modulo \(p^{s(\alpha,\beta)}\) induces an isomorphism of \(R\)-modules
\[
 HH_0(\mathscr D_h/R)\simeq
 \prod_{c\in\mathbb F_p^h}
 \bigoplus_{\beta\in\mathbb N^h}
 \prod_{\alpha\in\mathbb N^h}R/p^{s(\alpha,\beta)}R .
\]
The direct sum permits finitely many derivative indices \(\beta\) for each operator. At each such index the product permits an arbitrary sequence of Taylor coefficients.

*Proof.* First recover the scaled derivatives from the congruence translation. It preserves each disk since \(S_i(x,pt)\equiv x_i\bmod p\). Indeed, the idempotent of a disk and its translate have the same reduction at the residue locus. If \(e,e'\) are these idempotents, \(e(1-e')\) and \(e'(1-e)\) are idempotents in the defining ideal of the completed target. Each lies in every power of that ideal, hence is zero. Thus \(e=e'\). Multiplication by the disk idempotents lets us specify an operator on each component separately.

The addition law has the form \(S_i=x_i+y_i+P_i(x_{<i},y_{<i})\). To see this, start with \(S_0=x_0+y_0\) and apply \(\delta\). In \((\varphi S_i-S_i^p)/p\) the two new highest coordinates occur as \(x_{i+1}+y_{i+1}\), and all remaining terms use only coordinates through \(i\). Consequently \(J_{ij}=\partial_{y_j}S_i(x,0)\) is triangular with diagonal entries one. Write \(e_j\) for the multi-index with a single one in position \(j\). The first extractors are \(D_{e_j}=\sum_i M_{J_{ij}}d_i\). Inverting this triangular matrix over the position ring expresses each \(d_i\) in \(\mathscr D_h\).

Conversely, extracting \(t^{[\gamma]}\) from \(f(S(x,pt))\) means taking its ordinary \(\gamma\)-derivative in \(t\) at zero. On a polynomial \(f\), substituting \(pt\) supplies \(p^{|\gamma|}\). The chain rule uses integral polynomial coefficients and derivatives \(\partial_z^\eta f\) with \(|\eta|\le|\gamma|\). Each term can therefore be written as a position coefficient times \(p^{|\gamma|-|\eta|}d^\eta f\). Taylor polynomials are dense on each disk. Both the coaction extractor and the scaled derivatives are continuous for the \((p,z_0,\ldots,z_{h-1})\)-adic topology. In particular \(p\partial_{z_i}\) preserves each power of this ideal. The calculation thus holds for every formal \(f\).

The rule \([d_i,M_g]=M_{p\partial_{z_i}g}\) moves derivatives to the right in every finite word. For uniqueness, suppose a normal sum is zero and choose a term of largest total derivative order, with index \(\beta\). Take successive commutators on the right with \(M_{z_i}\), using each \(i\) exactly \(\beta_i\) times. All other terms disappear. The result is multiplication by \(p^{|\beta|}\beta! f_{c,\beta}\), where \(\beta!=\prod_i\beta_i!\). Applying it to \(1\) and using torsion-freeness gives \(f_{c,\beta}=0\). Descending in the order proves uniqueness.

Which coefficients can a commutator change? On one disk the two brackets at output order \(\beta\) are
\[
 [d_i,M_gd^\beta]=M_{p\partial_{z_i}g}d^\beta,\qquad
 [M_{z_i},M_gd^{\beta+e_i}]=-p(\beta_i+1)M_gd^\beta .
\]
At \(z^\alpha d^\beta\) the first reads the coefficient of \(z^{\alpha+e_i}\) in \(g\), multiplied by \(p(\alpha_i+1)\). The second reads its \(z^\alpha\) coefficient, multiplied by \(-p(\beta_i+1)\). Together these integers generate the ideal \(p^{s(\alpha,\beta)}R\).

For polynomial position coefficients the identity \([UV,W]=[U,VW]+[V,WU]\) reduces each commutator to brackets with a single \(z_i\) or \(d_i\) in the first slot. The same divisibility holds at each Taylor coefficient for formal inputs. Indeed, if the two operators have derivative orders at most \(N_1,N_2\), truncating their position coefficients through total degree \(|\alpha|+N_1+N_2\) preserves the \(z^\alpha d^\beta\) coefficient of both products by the Leibniz rule.

Conversely, take a finite-order operator whose coefficients all satisfy these divisibilities. For each \(c,\alpha,\beta\), choose one of the \(2h\) displayed integer factors of least \(p\)-adic valuation and divide its coefficient \(a_{c,\alpha,\beta}\) by that signed factor in \(R\). For a bracket with \(d_i\), put the quotient in Taylor slot \(\alpha+e_i\) of its multiplier at order \(\beta\). For a bracket with \(M_{z_i}\), put it in slot \(\alpha\) at order \(\beta+e_i\). For each chosen generator the assigned slots are distinct. They define formal multipliers even when infinitely many Taylor coefficients are present. Collecting the finitely many orders and disks gives operators \(U_i,V_i\) in \(\mathscr D_h\). With \(Z_i=(z_i)_c\in B_h\), the original operator is
\[
 \sum_{i<h}\bigl([d_i,U_i]+[M_{Z_i},V_i]\bigr).
\]
Thus at most \(2h\) commutators suffice for the whole kernel. Finally, lift the specified residues one Taylor coefficient at a time at each of the finitely many derivative orders. The resulting formal multipliers give a preimage of every element of the displayed module. ∎

For any \(R\)-module \(L\), the cyclic traces into \(L\) are precisely the algebraic \(R\)-linear maps from this quotient to \(L\), composed with coefficient reduction. Such a map acts on the whole Taylor product at each derivative order. For example, on one disk multiplication by \((1-z_0)^{-1}=\sum_{n\ge0}z_0^n\) has derivative order zero. Its class has entry \(1\bmod p\) at every Taylor index \(n e_0\). The classification includes algebraic linear maps without any continuity assumption. The summand of order \(\beta\) is killed by \(p^{1+\min_i v_p(\beta_i+1)}\), so each finite-order class is killed by a power of \(p\). This recovers the torsionfree corollary. Every \(p^r\), \(r\ge1\), occurs as the exact order of a class. Take \(\alpha_i=\beta_i=p^{r-1}-1\) on one disk and use \(z^\alpha d^\beta\). For instance, at \(p=2\) and height two, \(z_0z_1d_0d_1\) has order four in the quotient. At height one this gives the trace modulo four on \(zd\) with which we began.

An algebra allowing infinite derivative order requires a topology. If the finite-order algebra is dense in such a completion, a continuous trace into a Hausdorff \(p\)-torsionfree target vanishes by restriction and density. On the supported coefficient modules one may take a residue and then evaluate. For one normal coordinate \(u\), the residue of \(du/u\) is \(1\), so evaluation at a single mark of weight one gives \(1\). [Integral normal operations at an arithmetic marked point][integral-collisions]

A comparison with a local field algebra must give the ordered coefficient complex on each side and a common domain for the evaluations. On it one must match the class killed by scalar evaluation in (16.14), its nonzero normal derivative, the height change under Frobenius, the allowed nonconsecutive collisions, both empty cuts and the local vacuum. The integral construction provides the source of these tests. On the real logarithmic line a different trace problem remains even for ordinary scalar test functions. There the question is the sign of (16.3) as we enlarge their support.

## Whole-window positivity and the off-block term {#ch16-whole-window-positivity-and-the-off-block-term}

Return to the complex Weil form (16.3). For a prime-power term in \(W(g*g^*)\) to contribute, the support of \(g\) must overlap its translate by the logarithm of that prime power in positive measure. This gives a way to restrict the primes while leaving the shape of the test arbitrary. Suppose \(g\) has essential support in an interval of full width \(2T\). Translating the interval to \((-T,T)\) and extending \(g\) by zero gives the autocorrelation
\[
 h(u)=(g*g^*)(u)=\int_{\mathbb R} g(v)\overline{g(v-u)}\,dv .
\]
In particular \(h(0)=\|g\|_2^2\), and \(h(\log n)=0\) when \(\log n\ge 2T\), since the two copies of the interval overlap in a set of measure zero. At \(T=31/20\), \(e^{2T}\) lies between \(22\) and \(23\). This gives a finite list of prime powers, while the inequality still has to hold for every shape of \(g\). Writing \(\gamma_E\) for the Euler–Mascheroni constant, the real-space form of (16.1) is
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
Near \(u=0\), replacing \(2e^{-u/2}h(0)\) by \(2h(0)\) in the last integral changes its integrand by a bounded function, since \((1-e^{-u/2})/\sinh u\to1/2\). The minus sign in front of the integral makes its only possibly divergent part nonnegative, because
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

The half-width \(31/20\) fixes which prime powers can occur, but a test in that interval still has infinitely many modes. Split it into even and odd parts and retain \(1,152\) Legendre modes of each parity. The discarded tail contributes both its own quadratic form and a cross term with the retained part. A lower bound for the retained matrix alone places no constraint on the mixed term.

The estimate controls the full Gram matrix of the coupling, including its mixed entries. Both polar contributions, the real-place term and the prime powers \(2,3,4,5,7,8,9,11,13,16,17,19\) enter. Weighted Schur estimates and rigorous interval inequalities give \(7.0942\cdot10^{-109}\) in even parity and \(3.6094\cdot10^{-104}\) in odd parity. The two parities are orthogonal, so their smaller bound holds for every test. An even polynomial of degree at most \(2302\) gives the upper bound in (16.17) by its Rayleigh quotient.

There is room to enlarge that interval strictly. For one explicit bound set \(c=7.0942\cdot10^{-109}\), \(T_0=31/20\), \(R_0=2\exp(10^7/c)\) and \(d=c/(10^5R_0)\). Every test supported in width \(2T_0(1+d)\) satisfies \(Q(g)\ge(c/2)\|g\|_2^2\). To see how a tiny increase can control all vectors, dilate a norm-one test by \(g_b(x)=b^{-1/2}g(x/b)\) for \(1\le b\le1+d\). The prime multipliers on the fixed window become \(\cos(\xi\log n/b)\). Below frequency \(R_0\) their changes are at most \(4dR_0\). On the only relevant sublevel \(Q(g_b)\le1\), logarithmic growth of the real-place multiplier bounds the Fourier mass above \(R_0\) by \(750/\log(R_0/2)\). Together with the changes of the polar terms and real-place multiplier this gives
\[
 |Q(g_b)-Q(g)|\le224d+2000dR_0+750000/\log(R_0/2)<c/2 .
\]
The estimate propagates one known positive margin. A proof on all windows would have to control how the margin changes over arbitrarily large dilations.

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
At \(c=1/2\) minimizing in \(y\) leaves \(3x^2/4\). At \(c=2\) the vector \((1,-2)\) gives \(-3\) although the two diagonal entries are still \(1\). In the Weil problem the finite block and the tail play the roles of \(x\) and \(y\). Their coupling is determined by the entire arithmetic form. There are two versions of the same test, depending on what is defined on the finite block.

First work on the finite-energy domain \(\mathcal Q_T\) of (16.16). It consists of the \(g\in L^2(-T,T)\) whose zero extensions satisfy \(\int_{\mathbb R}\log(2+|\xi|)|\widehat g(\xi)|^2\,d\xi<\infty\). Write \(q_T\) for the Hermitian polarization there. Let \(P\) be the orthogonal projection onto a finite-dimensional \(X\subset\mathcal Q_T\), and put \(Y=X^\perp,\ P^\perp=I-P\). Suppose the tail form on \(\mathcal Q_T\cap Y\) is nonnegative. For \(u\in X\) and \(v\) in this tail, vary a complex scalar in \(Q_T(u+t v)\). Its phase can make the mixed term negative. Minimization in its magnitude gives the discriminant inequality below. If \(Q_T(v)=0\), varying the magnitude forces the mixed term to vanish. Thus \(Q_T\ge0\) precisely when
\[
Q_T(u)\ge0,\qquad |q_T(v,u)|^2\le Q_T(v)Q_T(u)
\qquad(u\in X,\ v\in\mathcal Q_T\cap Y).
\]

The associated self-adjoint operator \(W_T\) is defined on those \(u\in\mathcal Q_T\) for which \(v\mapsto q_T(v,u)\) is bounded in the \(L^2\) norm. This extra domain condition matters even when the tail is strictly positive. At \(T=31/20\), compact resolvent allows a *subsequence* of orthonormal eigenvectors \(e_j\) with eigenvalues \(\mu_j\ge2^j\). The vector \(u=\sum_{j\ge1}e_j/\mu_j\) has finite energy \(\sum_{j\ge1}1/\mu_j\). An \(L^2\) representative of \(q_T(\cdot,u)\) would have coefficient one along every \(e_j\), which is impossible by square summability. Taking \(X=\mathbb C u\) thus permits the preceding form test, and its tail inherits (16.17), but the operator \(W_TP\) is undefined on \(u\).

Now suppose \(X\subset\operatorname{Dom}W_T\). Let \(A=PW_T|_X\) and let \(D\) be the self-adjoint operator on \(Y\) associated with the tail form. The coupling from \(X\) to \(Y\) is bounded since \(X\) is finite-dimensional. On \(X\oplus\operatorname{Dom}D\) the blocks are
\[
W_T=\begin{pmatrix}A&K^*\\K&D\end{pmatrix},
\qquad K=P^\perp W_TP.
\]
**Proposition (Schur complement).** Under the operator-domain hypothesis \(X\subset\operatorname{Dom}W_T\), suppose \(D\ge dI\) for some \(d>0\). Then \(D^{-1}\) is bounded on \(Y\) and has range \(\operatorname{Dom}D\). For each \(u\in X\), completing the square as in (16.18) gives the minimum of \(Q_T(u+v)\) over \(v\in\mathcal Q_T\cap Y\) at \(v=-D^{-1}Ku\). Hence positivity is equivalent to
\[
A-K^*D^{-1}K\ge0.
\tag{16.19}
\]
The correction has quadratic form \(\langle Ku,D^{-1}Ku\rangle\ge0\). In the two-dimensional example (16.18) it was \(c^2x^2\). Positivity of \(A\) bounds the minimum from above. To bound it from below one needs the size of the coupling as well as the positive lower bound on the tail.

The retained Legendre polynomials and interval Fourier modes belong to \(\operatorname{Dom}W_T\). After zero extension their Fourier transforms are \(O((1+|\xi|)^{-1})\) by integration by parts. Multiplication by the logarithmically growing real-place symbol in (16.1) gives an \(L^2\) function, and the prime and polar terms are bounded on the window. At fixed \(T\), the tail lower bounds tend to infinity as the cutoffs exhaust either basis. Otherwise there would be unit vectors of bounded energy in successive tails. They converge weakly to zero, and compactness of the form-domain inclusion would give a subsequence converging in norm to zero.

For the projection onto the first eigenvectors of the real-place operator \(A_T\), the archimedean cross term vanishes. If the first omitted eigenvalue is \(a>\|W_T-A_T\|\), the tail has lower bound \(a-\|W_T-A_T\|\). In a Fourier cutoff, the archimedean part \(P^\perp A_TP\) is generally nonzero and belongs to \(K\). Dropping it changes (16.19). [Whole-window operators and Schur reductions][whole-windows]

There is a second way to restrict the overlap of \(g\) with a translate. Put two intervals at \(0,\log n\), \(n\ge2\), and give each the same full width \(0<w\le\min(2^{-19},1/(2n))\). A shift \(\log m\) couples the intervals only when \(|\log(m/n)|<w\). This width isolates the integer \(n\), whose prime coefficient vanishes unless it is a prime power. For arbitrary complex shapes \(f,g\) of finite form energy in the first interval, let \(R_tg(x)=g(x-t)\). Then
\[
 Q(f+R_{\log n}g)\ \ge\ \tfrac14(\|f\|_2^2+\|g\|_2^2).
\]
Each diagonal term dominates its squared norm on these narrow supports. Only the prime coefficient \(-\Lambda(n)/\sqrt n\) can occur between the two intervals, and its magnitude is at most \(2/e\). The smooth cross term has norm at most \(w e^{w/2}\sqrt n\le2^{-9}\). Subtracting the two bounds from one leaves more than \(1/4\). Return to the prime square \(n=4\). Place the same nonnegative norm-one profile in each interval. At displacement \(\log4\) one copy meets the other exactly, giving autocorrelation one. The reflected displacement gives one as well. Each carries weight \(-\Lambda(4)/\sqrt4=-(\log 2)/2\), so their combined contribution is \(-\log 2\). The estimate uses the entire form, including this negative contribution.

## One fixed shape and its logarithmic translates {#ch16-fixed-shape-translates}

The isolation estimate used \(w\le1/(2n)\), so it permits narrower and narrower intervals as \(n\) grows. Suppose instead that the two copies of a test have one fixed shape. Eventually adjacent integer logarithms are closer together than its width, so this spacing can no longer isolate one prime-power atom. In the zero expansion (16.2) there is another requirement. A zero at which the profile's transform vanishes could be absent from every translate, since translation only multiplies the transform by an exponential. We therefore need a compact profile whose transform has no zero in the entire closed strip \(|\operatorname{Im}z|\le1/2\).

**Definition (translated Weil test).** Put \(a_j=2^{-20-j}\), \(j\ge1\), and let \(b\) be the density of the infinite convolution of the uniform probability measures on \([-a_j,a_j]\). Normalize \(\phi(x)=e^xb(x)/\|e^{(\cdot)}b\|_2\). For \(n\ge2\) use the two translates \(g_n=\phi+R_{\log n}\phi\) and denote their Weil reading by \(E_n=Q(g_n)\).

The profile is real and supported in \([-2^{-20},2^{-20}]\) since \(\sum_j a_j=2^{-20}\). Its untilted transform is \(P(z)=\prod_j\operatorname{sinc}(a_jz)\), where \(\operatorname{sinc} v=\sin(v)/v\) and \(\operatorname{sinc}0=1\). The first \(k\) factors give decay of order \(k\) on the real axis, proving smoothness for every \(k\). Since \(\sum_j a_j^2<\infty\), the product converges locally uniformly and vanishes only at the real zeros of its factors. The positive Fourier sign gives \(\widehat\phi(z)=P(z-i)/\|e^{(\cdot)}b\|_2\), which is nonzero throughout \(|\operatorname{Im}z|\le1/2\).

**Theorem (a fixed translate test for Weil positivity).** With \(\log^+ x=\max(0,\log x)\) for \(x>0\) and \(\log^+0=0\),
\[
 \limsup_{n\to\infty}
 \frac{\log^+\max(0,-E_n)}{\log n}
       =\sup_\rho|\operatorname{Re}\rho-\tfrac12| .
\]
To prove the formula, write \(F(t)=W(\phi^**R_t\phi)\). The autocorrelation of the real profile is even, and \(W\) is invariant under reflection. Thus \(F\) is real and even, and the two off-diagonal terms in \(E_n=2F(0)+2F(\log n)\) are equal. In the zero expansion (16.2), the coefficient of \(e^{(\rho-1/2)t}\) in \(F(t)\) is \(m_\rho\overline{\widehat\phi(\bar w_\rho)}\widehat\phi(w_\rho)\ne0\). Its Laplace transform therefore has an actual pole at each \(\rho-\tfrac12\).

Smoothness gives \(|F'(t)|\le Ce^{t/2}\) for \(t\ge0\). Between \(\log n\) and \(\log(n+1)\) the interval has length at most \(1/n\), while the derivative is \(O(\sqrt{n+1})\). A lower bound at the samples thus extends to the intervening times with error \(O(n^{-1/2})\). If the sampled negative parts have exponent below \(\eta>0\), then \(F(t)+C_\eta e^{\eta t}\) is nonnegative on \(t\ge0\) for sufficiently large \(C_\eta\).

The Laplace transform of this nonnegative function has no real pole to the right of \(\eta\), since \(\zeta\) has no real zero in \(0<s<1\). A finite abscissa of convergence of a Laplace transform of a nonnegative function is singular on the real axis. The transform therefore converges throughout \(\operatorname{Re}s>\eta\). An off-line zero giving a pole there would contradict this convergence. Reflection yields one inequality in the formula, and absolute convergence of the zero expansion yields the other.

If all zeros have real part \(1/2\), (16.2) gives \(E_n\ge0\) for every \(n\). Conversely, eventual nonnegativity makes the exponent on the left zero and forces every zero onto that line. The width of \(\phi\) is \(2^{-19}\). It satisfies \(2^{-19}\le1/(2n)\) exactly through \(n=2^{18}\), where the two-interval bound gives \(E_n\ge1/2\) since each copy has norm one. At larger \(n\) further prime powers can enter the cross term. Eventual nonnegativity for this fixed shape remains open.

For squares the gap between successive sample times is \(2\log(1+1/j)\le 2/j\). To tell whether a negative reading can fall between the squares, we need to bound how fast the reading changes across that gap.

::: corollary {#ch16-corollary-perfect-power-weil title="The fixed Weil test on perfect powers"}
Let \(E_n=Q(\phi+R_{\log n}\phi)\) for the [fixed translated Weil test](#ch16-fixed-shape-translates), and put \(x_-=\max(0,-x)\). For each fixed positive integer \(q\),
\[
 \limsup_{j\to\infty}
 \frac{\log^+\big((E_{j^q})_-\big)}{\log(j^q)}
 =\sup_\rho\big|\operatorname{Re}\rho-\tfrac12\big|.
\]
The Riemann hypothesis holds if and only if \(E_{j^q}\ge0\) for all sufficiently large \(j\).
:::

::: proof {#ch16-proof-perfect-power-weil}
Write \(\delta=\sup_\rho|\operatorname{Re}\rho-\tfrac12|\) and \(\lambda_\rho=\rho-\tfrac12\). The coefficient of \(e^{\lambda_\rho t}\) in \(F(t)\) is \(a_\rho=m_\rho\widehat\phi(w_\rho)\overline{\widehat\phi(\bar w_\rho)}\). Integration by parts gives rapid decay of \(\widehat\phi\) uniformly on \(|\operatorname{Im}w|\le1/2\). The zero count up to height \(R\), with multiplicities, is \(O(R\log(2+R))\). Hence \(\sum_\rho |a_\rho|(1+|\lambda_\rho|)<\infty\). We can differentiate the series on compact intervals and retain the actual width of the strip in the estimate
\[
 |F'(t)|\le e^{\delta t}\sum_\rho |a_\rho\lambda_\rho|,\qquad t\ge0 .
\]

Take \(j=\lfloor n^{1/q}\rfloor\). The distance from \(\log n\) to the preceding sample \(q\log j\) is at most \(q\log(1+1/j)=O_q(n^{-1/q})\). Since \(E_n=2F(0)+2F(\log n)\), integrating the derivative across this gap gives
\[
 |E_n-E_{j^q}|\le C_{\phi,q}\,n^{\delta-1/q}.
\]
The same bound holds for the difference of the negative parts, since \(x\mapsto x_-\) is 1-Lipschitz. The full-integer theorem bounds the exponent on the subsequence from above by \(\delta\), giving equality at once if \(\delta=0\). For \(\delta>0\) take \(0<\eta<\min(\delta,1/q)\). The theorem gives arbitrarily large \(n\) with \((E_n)_->n^{\delta-\eta}\). At the preceding power the negative part is then at least \(\tfrac12 n^{\delta-\eta}\). Since \(\log(j^q)/\log n\to1\), the sampled exponent is at least \(\delta-\eta\). Let \(\eta\) decrease to zero. Eventual nonnegativity on the powers now forces \(\delta=0\). Conversely, on the Riemann hypothesis (16.2) expresses each \(E_{j^q}\) as a sum of nonnegative squares.
:::

::: example {#ch16-geometric-sampling-quartet title="A four-frequency test on a geometric progression"}
At the integers \(4^j\) the gaps on the logarithmic scale stay equal to \(\log4\). Keep \(\phi\) and form a model reading \(E^*_n\) by using just the four frequencies \(\pm\gamma\pm i\beta\), each once, in (16.2). Take \(\gamma=2\pi/\log4\) and \(\beta=1/3\). For \(a=\widehat\phi(\gamma-i\beta)\overline{\widehat\phi(\gamma+i\beta)}\), the real part is the integral of
\[
 \phi(u)\phi(v)e^{\beta(u-v)}\cos\big(\gamma(u-v)\big)
\]
over \(u,v\). Since \(\phi\) is nonnegative and its support has diameter \(2^{-19}\), the cosine is positive throughout that support and \(\operatorname{Re}a>0\). At \(n=4^j\) the phase \(e^{i\gamma\log n}\) equals \(1\), and multiplication of \(n\) by two changes its sign. Adding the four terms and both diagonal readings gives
\[
 \frac{E^*_n}{8\operatorname{Re}a}=
 \begin{cases}
   1+\cosh(\beta\log n),& n=4^j,\\
   1-\cosh(\beta\log n),& n=2\cdot4^j .
 \end{cases}
\]
For example, the ratio is \(25/8\) at \(n=64\) and \(-1/4\) at \(n=8\). All the geometric samples are positive, although the intervening negative readings grow in magnitude like \(n^{1/3}\). The sufficiency of these geometric samples for the zeta spectrum remains open here.
:::

On whole windows the allowed negative part of the spectral infimum is \(\varepsilon(T)=\max(0,-\lambda(T))\). Support inclusion makes it nondecreasing. For \(n\ge2\), the two copies of \(\phi\) in \(g_n\) have disjoint supports, so \(\|g_n\|_2^2=2\). An interval of full width \(2T_n=\log n+2^{-19}\) contains both supports. The infimum on that window satisfies \(\lambda(T_n)\le E_n/2\), hence \(\max(0,-E_n)\le2\varepsilon(T_n)\). Since \(2T_n/\log n\to1\), the fixed-translate theorem gives \(\sup_\rho|\operatorname{Re}\rho-\tfrac12|\le\limsup_{T\to\infty}\log^+\varepsilon(T)/(2T)\). Subexponential growth on all windows would therefore imply the Riemann hypothesis. In particular, a single constant \(C\) with \(\varepsilon(T_j)\le C\) along a sequence \(T_j\to\infty\) would suffice. Given \(T\), choose \(j\) with \(T_j\ge T\). Then \(\varepsilon(T)\le\varepsilon(T_j)\le C\), so the growth exponent is zero.

Monotonicity alone leaves an uncontrolled factor \(T_{j+1}/T_j\) between sparse samples. An off-line zero supplies a test on every sufficiently large window.

::: proposition {#ch16-proposition-sparse-weil-windows title="The Weil form on an unbounded sequence of windows"}
Let \(T_j\) be any sequence of half-widths tending to infinity. If \(\log^+\varepsilon(T_j)=o(T_j)\), every nontrivial zero of \(\zeta\) has real part \(1/2\).
:::

::: proof {#ch16-proof-sparse-weil-windows}
Suppose \(v=r-i\sigma\), \(\sigma>0\), is a centred zero of multiplicity \(m\). Put \(X(z)=\xi(1/2+iz)\). The entire transform
\[
 \widehat f_v(z)=\frac{m!\,X(z)}{X^{(m)}(v)(z-v)^m}
\]
has value one at \(v\) and zero at every other centred zero. Make the same choice for \(\bar v\). On every bounded horizontal strip, Stirling's formula for the gamma factor and the polynomial strip bounds for zeta give exponential decay of these transforms as \(|\operatorname{Re}z|\to\infty\). Shifting the inverse Fourier contour gives \(|f_v^{(k)}(u)|\le C_{B,k}e^{-B|u|}\) for every \(B>0\) and \(k\ge0\).

For \(0<L<T\) put \(h=T-L\) and take \(G=R_h f_v-e^{2irh}R_{-h}f_{\bar v}\). Its two surviving transform values are \(e^{irh+\sigma h}\) and \(-e^{irh+\sigma h}\). Thus (16.2) gives \(Q(G)=-2m e^{2\sigma h}\). Multiply each packet before translation by a smooth cutoff equal to one on \([-L+1,L-1]\) and supported in \([-L,L]\), with uniformly bounded first derivative for \(L>1\). The resulting test lies in \([-T,T]\) and has uniformly bounded \(L^2\) norm. For \(a>1/2\), integration by parts bounds each transform on the zero strip by \(C p_{a,1}(f)/(1+|z|)\). The zero count makes \(\sum_\rho m_\rho(1+|w_\rho|)^{-2}\) finite, so the Weil pairing is bounded by \(C p_{a,1}(f)p_{a,1}(g)\). Cutting off a packet costs \(O_b(e^{-bL})\) in this seminorm for any \(b>0\), and translating by either \(h\) or \(-h\) costs at most \(e^{ah}\). The error in \(Q\) is consequently \(O_b(e^{2ah-bL})\).

Take \(L=\delta T\), \(0<\delta<1\), and choose \(b\delta>2(a-\sigma)(1-\delta)\). The Rayleigh quotient gives \(\varepsilon(T)\ge c_{v,\delta}e^{2\sigma(1-\delta)T}\) for every sufficiently large \(T\). Letting \(\delta\) tend to zero proves
\[
 \sup_\rho|\operatorname{Re}\rho-\tfrac12|
 \le \liminf_{T\to\infty}\frac{\log^+\varepsilon(T)}{2T}.
\]
A positive value of \(\sigma\) contradicts the assumed estimate along \(T_j\). For a zero on the other side of the line, the functional equation gives a zero at the same distance on this side.
:::

Under the Riemann hypothesis \(\varepsilon(T)=0\) on every window. Proving the subexponential estimate, even along one unbounded sequence, still requires a bound for the complete form. [The Weil form on compact windows][whole-windows]

The theta quotient realizes \(W(f)\) for \(\tfrac12<s<\min(a,1)\). Its positive counterpart has the remainder (16.12), and its vanishing for every test is equivalent to the same global sign question. Even equality of those scalar traces would leave a question about operators. At height \(h\ge2\) a local field map must carry \(h_0\) and its nonzero derivative \(D_0h_0=-p\bmod p^2\), although all scalar arithmetic points kill \(h_0\). [Arithmetic positivity and local operations](#problem-arithmetic)

At a double zero specialize the [jet multiplication \(N=M_z\)](#ch16-multiplicity-nilpotence-and-two-different-pairings) to \(\mathbb C[z]/(z^2)\). On two independent eigenvectors the nilpotent part is zero. On the two-step jet it sends \(1\) to \(z\). The scalar trace agrees, but acting on a specified input distinguishes the operators. A [bulk field acting on a boundary insertion](#ch17) admits the same kind of test.

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

The normalization uses additive \(du\) after \(u=\log x\), both polar evaluations, and both orientations of each prime power. The zero expansion (16.2) pairs reflected frequencies on a convolution square. [Weil functional and form](#ch16-the-complete-arithmetic-functional)

### 2. An integer-summation middle complex and its continuous dual {#ref-ch16-02}

Ralf Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, Definition 3.1, Proposition 3.2 and Theorems 3.3 and 4.1, gives the summation and Mellin quotient. The continuous duality used here specifies in addition the norm closure of the jets at each weighted Sobolev stage. [The summation complex and its continuous dual](#ch16-integer-summation-defines-the-complex-before-its-spectrum) · [Meyer](https://arxiv.org/abs/math/0412277)

### 3. A common Hilbert theta complex {#ref-ch16-03}

“Closed theta and polar quotients” identifies the intersection and sum of the two Hilbert subspaces. “The geometric full trace” subtracts the restriction to the closed image of the differential and obtains the ordinary quotient trace (16.8). [Hilbert domains and trace](#ch16-a-geometric-construction-of-the-full-trace)

### 4. Trace-class coefficient homotopies {#ref-ch16-04}

“A proper differential trace ideal” specifies the supertrace and “The quotient contraction” constructs the inverse of the differential on its image. The binary and triple identities (16.9)–(16.10) hold in this ideal. [The coherent multiplication](#ch16-the-trace-domain-and-its-coherent-multiplication)

### 5. Linking operators and vacuum creation {#ref-ch16-05}

On the plane spanned by the added vacuum and a unit vector in the old summand, the commutator of the rank-one annihilation and creation maps has eigenvalues \(+1,-1\). The counting trace is taken on the old summand. [The linking-operator calculation](#ch16-the-trace-domain-and-its-coherent-multiplication)

### 6. Polynomial completions and the critical trace {#ref-ch16-06}

The multiplicity layers count a real centered zero of order \(m\) in \(m\) separate summands. The ordinary Hilbert trace is (16.11), and the omitted contribution is (16.12). [The positive representation](#ch16-a-positive-representation-and-its-exact-missing-remainder)

### 7. Integral arithmetic tubes with their normal operations {#ref-ch16-07}

The congruence arrows carry both the arithmetic point and its normal displacement. The higher-height Frobenius map and the divided-power addition law specify the coefficient operations before scalar evaluation. [Integral arithmetic tubes](#ch16-what-integral-arithmetic-points-forget)

### 8. Integral normal operations at an arithmetic marked point {#ref-ch16-08}

The ordered polynomial collision complexes retain partial residues on forest-supported diagonals. In *Marked arithmetic jet completions, normal operations, and polynomial collision residues*, Raeez Lorgat constructs the coaction and computes \(D_0h_0=-p\) (Theorem 2 and Proposition 3, pp. 4–5). Corollary 9 gives the finite marked residue sums, and Theorem 10 gives the commutators for the identity and residue-class idempotents (pp. 9–10). The coefficient calculation following (16.15) extends the vanishing to the whole generated algebra for \(p\)-torsionfree targets. The [finite-order trace theorem](#ch16-theorem-finite-order-traces-on-formal-arithmetic-disks) uses the coaction on the disks of (16.13) to compute the commutator quotient for arbitrary \(R=\mathbb Z_p\)-linear targets. [Point evaluation and the normal derivation](#ch16-what-integral-arithmetic-points-forget) · [The commutator and its consequence](#eq-16-15)

### 9. Local Weil positivity through half-width 31/20 {#ref-ch16-09}

In *Local Weil positivity through half-width \(31/20\)*, §5, equations (25)–(31), take the first \(K\) Legendre modes of the approximating operator \(A^{\rm ap}\). Its compression to those modes is \(M\). Project their images under \(A^{\rm ap}\) onto the orthogonal complement. The Gram matrix of these projected vectors is \(G\), and \(B\) records their coefficients in modes \(K\le n<L\). Write \(Q^{\rm ap}\) for the approximating form. For every vector \(v\) in the tail form domain, its Legendre coefficients \(v_n\) must satisfy
\[
 Q^{\rm ap}(v)-\lambda'\|v\|^2
 \ge \sum_{K\le n<L}d_n|v_n|^2+d_L\sum_{n\ge L}|v_n|^2,
 \qquad d_n,d_L>0 .
\]
Completing the square in the intermediate modes and then on their orthogonal complement gives the sufficient inequality
\[
 M-\lambda' I-B^*\operatorname{diag}(d_n^{-1})B-(G-B^*B)/d_L\succeq0.
\]
It gives \(Q^{\rm ap}(g)\ge\lambda'\|g\|^2\) on the full form domain. If the operator approximation error is at most \(\epsilon\), the continuum lower bound is \(\lambda'-\epsilon\). Section 8 bounds this error and verifies the weighted inequality separately in the two parity sectors. The resulting lower bounds are \(7.0942\cdot10^{-109}\) and \(3.6094\cdot10^{-104}\). The even polynomial trial gives the opposite inequality in (16.17). [The whole-window inequality](#ch16-whole-window-positivity-and-the-off-block-term)

### 10. The Weil form on compact windows {#ref-ch16-10}

The closed log-energy form gives the operator on a finite window, and completing the square gives the Schur complement (16.19) on operator-domain cutoffs with positive tail. The proposition “Growth detected by translated tests” bounds the zero strip by the growth of the whole-window allowance. The fixed-profile theorem in §16.9 instead samples two translates at every integer logarithm. [Form and operator domains](#ch16-whole-window-positivity-and-the-off-block-term) · [The fixed profile and the whole-window bound](#ch16-fixed-shape-translates) · [The fixed Weil test on perfect powers](#ch16-corollary-perfect-power-weil)
