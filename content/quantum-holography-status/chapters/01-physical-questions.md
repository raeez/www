# Boundary observables and reconstruction

Suppose a field is prepared in a half-space and only its boundary is accessible. Can boundary measurements distinguish two preparations with the same energy and occupation probabilities? Consider a wave on a circle. Its first harmonic oscillates once around the circle, its second twice. Two quanta of the first harmonic and one quantum of the second have the same energy. Prepare a superposition of these alternatives and reverse the sign of just the second amplitude. A count of the quanta has the same distribution in both preparations. To read the sign we must find an observable for which the two alternatives interfere.

## Two preparations and one joint measurement {#ch01-two-preparations}

Take the first two harmonics of a free current, with one independent oscillator for each positive harmonic, and leave all higher harmonics in the vacuum. Count energy above the vacuum in units of one quantum of the first harmonic. If the counts are \(m_1,m_2\), their energy is \(m_1+2m_2\). Energy two thus permits precisely the outcomes \((2,0)\) and \((0,1)\). We need operations that change one count into the other.

**Definition (two-harmonic Fock space).** Write \(1\) for the vacuum and \(p_1^{m_1}p_2^{m_2}\) for the state with \(m_n\) quanta of harmonic \(n\), where \(m_n\) is a nonnegative integer. Finite superpositions are the polynomials in \(\mathbb C[p_1,p_2]\). Multiplication by \(p_n\) adds a quantum. Differentiation with respect to \(p_n\) removes one and counts how many could have been removed. For a current of level one the creation and annihilation modes are respectively
\[
J_{-n}=p_n\cdot(-),\qquad J_n=n\frac{\partial}{\partial p_n}\qquad(n=1,2).
\]
{#eq-two-harmonic-modes}
For example, \(J_2p_2=2\), while \(J_2p_1^2=0\). On a polynomial \(f\), adding a quantum and then removing one gives \(n\partial_{p_n}(p_nf)=nf+p_n n\partial_{p_n}f\). The last term comes from removing a quantum already present in \(f\). Thus \([J_n,J_{-n}]=n\,\mathrm{id}\), with \([A,B]=AB-BA\). Modes on different harmonics commute. [The free current](03-local-fields.md#heisenberg-current)

Starting at the vacuum, the two paths to energy two give \(p_1^2\) and \(p_2\). To assign probabilities to their sum we need their lengths and their inner product. For the Fourier modes of a real current the amplitude for adding a quantum is the complex conjugate of the amplitude for the reverse transition. This is the adjoint relation in the following lemma.

**Lemma (occupation inner product).** With vacuum norm one and \(J_n\) adjoint to \(J_{-n}\), there is a unique positive Hermitian inner product on the polynomials. We take it conjugate-linear in the first entry. Different occupation monomials are orthogonal, and
\[
\bigl\|p_1^{m_1}p_2^{m_2}\bigr\|^2=m_1!\,2^{m_2}\,m_2!.
\]
{#eq-two-harmonic-norms}

*Proof.* Adjointness gives \(\langle p_n f,g\rangle=\langle f,n\partial_{p_n}g\rangle\). Transfer the factors of the first monomial, one at a time, to derivatives on the second. If the first exponent of a given harmonic is larger, these derivatives kill the second monomial. If the second exponent is larger, interchange the two monomials using Hermitian symmetry. For equal exponents \(m_n\) the repeated derivative gives \(n^{m_n}m_n!\). Multiplying the two factors leaves the vacuum norm, which is one. Conversely these positive diagonal entries satisfy the adjoint relation on monomials and hence on all polynomials. ∎

On our two paths the calculation gives \(\langle p_1^2,p_1^2\rangle=\langle1,J_1^2p_1^2\rangle=2\), \(\langle p_2,p_2\rangle=\langle1,J_2p_2\rangle=2\), and \(\langle p_1^2,p_2\rangle=\langle1,J_1^2p_2\rangle=0\). Completing the polynomials in this norm gives the two-harmonic Hilbert space. Its energy-two subspace has orthonormal basis
\[
a=\frac{p_1^2}{\sqrt2},\qquad b=\frac{p_2}{\sqrt2}.
\]
Thus \(a\) and \(b\) have the same energy and different occupation numbers in each harmonic. Write \(f\otimes g\) for the product \(f(p_1)g(p_2)\). By the occupation lemma the inner product of two such states is the product of the inner products in the two harmonics. In this notation \(a=(p_1^2/\sqrt2)\otimes1\) and \(b=1\otimes(p_2/\sqrt2)\).

Prepare \(\psi=\alpha a+\beta b\) with \(|\alpha|^2+|\beta|^2=1\). By the squared-amplitude rule the two counts have probabilities \(|\alpha|^2\) and \(|\beta|^2\). Let \(B\) be the operator for a measurement event on the first harmonic, so \(0\le B\le\mathrm{id}\). On the pair the event has operator \(A=B\otimes\mathrm{id}\), sending \(f\otimes g\) to \((Bf)\otimes g\). Its probability is \(\langle\psi,A\psi\rangle\). The cross term \(\langle a,Ab\rangle\) contains the inner product \(\langle1,p_2/\sqrt2\rangle=0\) from the second harmonic. Since \(A\) is self-adjoint, \(\langle b,Aa\rangle\) vanishes as well. Thus
\[
\langle\psi,A\psi\rangle=|\alpha|^2\langle a,Aa\rangle+|\beta|^2\langle b,Ab\rangle .
\]
An event on the second harmonic has operator \(\mathrm{id}\otimes C\). Its cross term contains the first-harmonic inner product \(\langle p_1^2/\sqrt2,1\rangle=0\). In particular the normalized sum and difference
\[
u_\pm=\frac{a\pm b}{\sqrt2}=\frac{p_1^2\pm p_2}{2}
\]
{#eq-sum-and-difference}
give the same probabilities in every such measurement. A joint observable can have a nonzero matrix element between \(a\) and \(b\). The simplest choice sends either unit vector to the other.

**Definition (exchange at energy two).** On the span of \(a,b\) let \(Sa=b\) and \(Sb=a\). The matrix of \(S\) in this orthonormal basis is real and symmetric. Its eigenvectors \(u_+,u_-\) have eigenvalues \(+1,-1\), respectively. Thus a measurement of this self-adjoint observable reads the sign with certainty on either preparation. On a general unit state \(\alpha a+\beta b\) its expectation is \(2\operatorname{Re}(\bar\alpha\beta)\).

Which operation of the current measures this exchange? To turn \(b\) into \(a\), remove a quantum of harmonic two and create two quanta of harmonic one. The reverse operation turns \(a\) into \(b\). Reading the modes from right to left gives \(J_{-1}^2J_2\) and \(J_{-2}J_1^2\). They are adjoints on polynomials. Their sum acts by
\[
\begin{gathered}
\begin{aligned}
O&=J_{-1}^2J_2+J_{-2}J_1^2\\
 &=2p_1^2\frac{\partial}{\partial p_2}
   +p_2\frac{\partial^2}{\partial p_1^2},
\end{aligned}\\[3pt]
O\,p_2=2p_1^2,\qquad O\,p_1^2=2p_2 .
\end{gathered}
\]
{#eq-energy-two-exchange}
Both transitions have coefficient two. On the energy-two subspace \(O=2S\), so \(O\) has the sharp readings \(+2\) on \(u_+\) and \(-2\) on \(u_-\). The symmetry of the matrix and the factor two have different origins. Adjointness pairs the two conversions, while the mode normalization fixes their common coefficient.

::: figure fig-energy-two-exchange

How could a second system read the sign? Give an ideal detector two orthonormal states \(|0\rangle,|1\rangle\), prepare \(|0\rangle\), and let the Hermitian operator \(Y\) send \(|0\rangle\) to \(i|1\rangle\) and \(|1\rangle\) to \(-i|0\rangle\). On the energy-two space couple the current to the detector by \(U_\theta=\exp(-i\theta O\otimes Y/2)\), with dimensionless interaction strength \(\theta\). Write \(u_\sigma\) for the state with \(Su_\sigma=\sigma u_\sigma\), where \(\sigma=\pm1\). Since \(O=2S\) there and \(Y^2=1\), the coupling gives
\[
 \begin{gathered}
 U_\theta(u_\sigma\otimes|0\rangle)=u_\sigma\otimes d_\sigma,\\
 d_\sigma=\cos\theta\,|0\rangle+\sigma\sin\theta\,|1\rangle .
 \end{gathered}
\]
At \(\theta=\pi/4\) the detector states \(d_+,d_-\) are orthogonal. Measuring in the basis \((|0\rangle\pm|1\rangle)/\sqrt2\) reads \(\sigma\) with certainty and leaves the prepared current state \(u_\sigma\) intact. Counting the detector in the basis \(|0\rangle,|1\rangle\) after the very same coupling gives equal probabilities for the two counts at either sign.

The two preparations can also be made on a disk. Here a measurement samples the shape of a real harmonic field \(\phi\) on the Euclidean unit disk \(D\). Mark its centre and choose an angular coordinate. With the constant mode fixed to zero, write \(\phi=h+\bar h\), where \(h(z)=\sum_{n\ge1}Z_nz^n/n\). The measured harmonic amplitudes are \(Z_n\). In particular \(Z_1=h'(0)\) and \(Z_2=h''(0)\), since the quadratic term is \(Z_2z^2/2\). To determine how often a shape occurs, first keep just \(N\ge2\) harmonics. For the truncated field \(\phi_N\) we have \(|\nabla\phi_N|^2=4|h_N'|^2\). Angular integration kills terms from different harmonics, so the Dirichlet action is
\[
S_{D,N}=\frac1{8\pi}\int_D|\nabla\phi_N|^2\,d^2z=\frac12\sum_{n=1}^N\frac{|Z_n|^2}{n}.
\]
At the vacuum, square the amplitude \(e^{-S_{D,N}}\) and normalize against \(\prod_{n=1}^N d^2Z_n\). The resulting density is a product. Each \(Z_n\) has circular complex Gaussian density \((\pi n)^{-1}e^{-|Z_n|^2/n}\). Integrating out one more coordinate multiplies the density of those already present by one. The consistent marginals define the product law \(\mu\) on all harmonics. This construction matters because one cannot insert a typical infinite sample back into the finite-action formula. The independent variables \(|Z_n|^2/n\) have exponential laws of mean one, so \(S_{D,N}/N\to1/2\) almost surely. The first two variables nevertheless have finite moments of every order, given by
\[
\mathbb E_\mu\bigl[|Z_1|^{2m_1}|Z_2|^{2m_2}\bigr]=m_1!\,2^{m_2}\,m_2!,
\]
which are precisely the squared occupation norms. A mismatch of exponents in either harmonic leaves an angular phase whose average is zero, so substitution \(p_n\mapsto Z_n\) preserves the full polynomial inner product. A unit state has a wavefunction \(F\) of squared integral one. Its disk preparation weights the vacuum law by \(|F|^2\). In particular \(u_\pm\) give the two densities \(|Z_1^2\pm Z_2|^2/4\) relative to \(\mu\), with wavefunctions \(F_\pm=(Z_1^2\pm Z_2)/2\).

Expanding the two squares reveals what to measure on a single sample. The pure terms \(|Z_1|^4\) and \(|Z_2|^2\) occur in both. The term that changes sign is
\[
C=2\operatorname{Re}\bigl(Z_1^2\,\overline{Z_2}\bigr)
 =2|Z_1|^2\,|Z_2|\cos(2\theta_1-\theta_2),
\]
{#eq-disk-reading}
where \(\theta_n\) is the phase of \(Z_n\). The reading compares the phase of the second harmonic with twice the phase of the first, weighted by the strengths of both waves. Since \(|Z_1^2\pm Z_2|^2=|Z_1|^4+|Z_2|^2\pm C\), its mean in the two prepared laws is
\[
\begin{aligned}
\mathbb E_\pm C
 &=\tfrac14\,\mathbb E_\mu\bigl[(|Z_1|^4+|Z_2|^2)C\bigr]\\
 &\quad{}\pm\tfrac14\,\mathbb E_\mu[C^2]\\
 &=0\pm\tfrac12\,\mathbb E_\mu|Z_1|^4\,\mathbb E_\mu|Z_2|^2\\
 &=\pm2 .
\end{aligned}
\]
The first expectation vanishes on averaging over the phase of \(Z_2\). The squared cosine in \(C^2\) has angular average \(1/2\), which gives the second expectation. Averaging over either harmonic phase also removes the interference term from the other harmonic's marginal. One disk reading varies from sample to sample. To find its second moment in either preparation, multiply \(C^2\) by the density \((|Z_1|^4+|Z_2|^2\pm C)/4\) and integrate against \(\mu\). Replacing \(Z_2\) by \(-Z_2\) preserves \(\mu\) and reverses \(C\), so the term in \(C^3\) integrates to zero. Averaging the squared cosine in the other two terms gives
\[
\begin{aligned}
\mathbb E_\pm C^2
 &=\tfrac12\,\mathbb E_\mu\!\left[|Z_1|^8|Z_2|^2+|Z_1|^4|Z_2|^4\right]\\
 &=\tfrac12(4!\cdot2+2!\cdot8)=32 .
\end{aligned}
\]
The disk statistic has mean \(+2\) or \(-2\) and variance \(32-4=28\) in the corresponding preparation. The current observable \(O\) gives its corresponding eigenvalue with certainty.

The equality of means has an operator explanation. Let \(P\) be orthogonal projection in \(L^2(\mu)\) onto the closed span of holomorphic polynomials. Multiply \(Z_n^m\) by \(\bar Z_n\). When \(m\ge1\) its angular dependence agrees with just one holomorphic monomial, \(Z_n^{m-1}\). Pairing with this monomial gives \(\langle Z_n^{m-1},\bar Z_n Z_n^m\rangle=\|Z_n^m\|^2\). Dividing by \(\|Z_n^{m-1}\|^2\) gives the projection coefficient \(nm\). When \(m=0\) every such pairing vanishes. Thus \(P(\bar Z_n F)=n\partial_{Z_n}F\) on holomorphic polynomials. Two conjugate factors in one variable give the twice-iterated derivative by the same moment calculation. Since the harmonics are independent, \(P(CF)=2Z_1^2\partial_{Z_2}F+Z_2\partial_{Z_1}^2F\). This is \(O\) under the substitution above. For every holomorphic polynomial \(F\), pairing with \(F\) gives \(\langle F,P(CF)\rangle=\int C|F|^2\,d\mu\).

Which bulk insertions have this boundary action? In the free half-space fix the fluctuation scale \(\hbar\) and bulk coefficient \(\kappa\) so that their product, the boundary level, is one. On the chosen boundary polynomials the unit-strength probe for harmonic \(n\) acts by \(\partial_{p_n}\), while a boundary insertion multiplies by \(p_n\). The first conversion therefore needs twice the second-harmonic probe. The reverse conversion needs two unit first-harmonic probes on disjoint successive slabs. This fixes both coefficients of \(O\) by the half-space calculation. [The half-space probes and the disk projection](11-states-and-lines.md#ch11-relative-phase)

### How far a boundary can move {#ch01-boundary-displacement}

The disk gave a reading for a specified coupling. Can the *allowed couplings themselves* distinguish two bulk interactions? In the B-twisted Landau–Ginzburg model take a formal coordinate \(x\) at the origin and a potential \(V_r(x)=x^r\), with \(r=3\) or \(4\). A boundary with one even and one odd basis vector over \(\mathbb C[[x]]\) is specified by a matrix \(Q\) interchanging the two parities and satisfying \(Q^2=V_r(x)I\), where \(I\) is the identity. Such a matrix is called a *matrix factorization* of the potential.

::: example {#ch01-fixed-potential-test title="A cubic and a quartic boundary"}
Start with upper right entry \(x\) and lower left entry \(x^{r-1}\). Displace the upper entry to \(x+t\). Can a change of the lower entry keep the same potential through order \(N\) in \(t\)? Set \(t^{N+1}=0\), so that terms through order \(N\) can be compared exactly. A lower entry \(b(x,t)\) would have to satisfy \((x+t)b(x,t)=x^r\). Substitution of \(x=-t\) in a formal \(x\)-series is legitimate since \(t\) is nilpotent. It forces \(t^r=0\). Conversely the finite geometric sum gives
\[
 \begin{gathered}
 b_r(x,t)=\sum_{j=0}^{r-1}(-t)^j x^{r-1-j},\\
 (x+t)b_r(x,t)=x^r-(-t)^r .
 \end{gathered}
\]
Thus the displacement is possible through order \(N\) precisely for \(N<r\). Retaining terms through \(t^3\) distinguishes the two boundaries. Before truncation the cubic square acquires \(+t^3 I\), while the quartic square first changes by \(-t^4 I\).

How can a third insertion detect the difference when two agree? Let \(E_{ij}\) denote the elementary matrices in the even, odd basis. The linear term of the displaced matrix is \(t\psi\) with \(\psi=E_{12}-x^{r-2}E_{21}\). The differential on boundary operators is \(dB=QB-(-1)^{|B|}BQ\), where \(|B|\) is the parity. Its square is \(Q^2B-BQ^2=0\). A closed operator satisfies \(dB=0\), and two closed operators give the same protected class if their difference is exact, that is, of the form \(dH\). For \(f,g,u,v\in\mathbb C[[x]]\), direct multiplication gives
\[
 \begin{aligned}
 d\,\operatorname{diag}(f,g)&=x(g-f)\psi,\\
 d(uE_{12}+vE_{21})&=(xv+x^{r-1}u)I .
 \end{aligned}
\]
The even cycles are multiples of \(I\), the odd cycles multiples of \(\psi\), and the exact multiples in either parity have coefficient in \((x)\). The classes \([I],[\psi]\) therefore form a basis over \(\mathbb C\). Since \(\psi^2=-x^{r-2}I\) is exact, the two potentials give the same ordinary multiplication.

For an odd change \(\alpha\) of \(Q\), the change in its square is \(d\alpha+\alpha^2\). Our choice of lower entry cancelled each coefficient up to the first scalar unit, which survives in cohomology. In the coordinates of this displacement, three copies of \([\psi]\) have higher product \(+[I]\) for the cubic. For the quartic it takes four copies to give \(-[I]\). [The higher products in the one-variable model](19-interacting-theories.md#ch19-boundary-potential)
:::

### Splitting and joining harmonics {#ch01-splitting-and-joining}

The free-current detector used a sum of two products of three modes. One converted the occupation \(1+1\) to \(2\), the other reversed the conversion at the same energy. At higher energies one can join harmonics \(i,j\) into \(i+j\) or split \(i+j\) into \(i,j\). Allow all harmonics, with \(J_{-n}\) multiplication by \(p_n\) and \(J_n=n\,\partial/\partial p_n\) for \(n\ge1\).

**Definition (cubic current observable).** The sum of the splitting and joining operations over ordered pairs of positive indices defines the operator
\[
W=\frac12\sum_{i,j\ge1}\bigl(J_{-i}J_{-j}J_{i+j}+J_{-i-j}J_iJ_j\bigr).
\]
{#eq-cubic-observable}
On a monomial of energy \(e\), a split requires an occupied harmonic \(i+j\) and a join requires the two quanta \(i,j\). Either can occur only when \(i+j\le e\), so the sum is finite on polynomials. Its adjoint pairs preserve each finite-dimensional energy space, where their sum \(W_e\) is self-adjoint. At energy two only \(i=j=1\) occurs, and \(W_2=O/2=S\). On the Hilbert completion the self-adjoint direct sum has domain \(\{F=\sum_e F_e:\sum_e\|W_eF_e\|^2<\infty\}\) and value \(WF=\sum_eW_eF_e\), where \(F_e\) is the orthogonal energy-\(e\) component.

There is a local expression for the same sum. In the neutral sector the total-charge mode \(J_0\) vanishes. Assemble the modes into \(J(z)=\sum_{n\in\mathbb Z}J_n z^{-n-1}\). In a product between colons put all creation modes to the left of the annihilation modes. Taking the residue means selecting the coefficient of \(z^{-1}dz\). With these conventions,
\[
W=\frac16\operatorname{Res}_{z=0}\,z^2\,{:}J(z)^3{:}\;dz .
\]
{#eq-cubic-residue}
The colons place the removal operators \(J_n\), \(n>0\), to the right. The residue selects triples whose three indices sum to zero. With \(J_0=0\), precisely one index has sign opposite to the other two. Its three possible positions give the factor \(3/6=1/2\), leaving the other two indices as the ordered pair in the sum. Thus the same exchange can be read from three currents multiplied *at one point*, with the singular terms removed by normal ordering. [Normal ordering of the free current](03-local-fields.md#heisenberg-current)

A free fermion on a ring has kinetic energy quadratic in its momentum. This curvature lets an energy measurement distinguish the states \(u_+\) and \(u_-\), which have the same oscillator energy. Put an odd number \(N\) of free spinless fermions of mass \(m\) on a ring of circumference \(L\). Their ground state fills momenta \(2\pi\hbar j/L\) for \(|j|\le(N-1)/2\). At positions \(y_a\) put \(x_a=e^{2\pi i y_a/L}\). Multiplying the ground-state wavefunction by the density wave \(p_n=\sum_{a=1}^N x_a^n\) adds momentum \(2\pi\hbar n/L\). At total oscillator energy \(n\), only the top \(n\) occupied orbitals can move. Thus \(n\ll N\) gives an upper-edge excitation. The current inner products already agree exactly with the density-wave inner products for \(n\le N\). [Density waves of free fermions](11-states-and-lines.md#ch11-boundary-fermions)

Let \(E\) multiply a current state of dimensionless energy \(n\) by \(n\). Raising the highest occupied fermion by one momentum step costs \(\varepsilon_1=2\pi\hbar v_F/L\), where \(v_F=\pi\hbar N/(mL)\) is the velocity halfway across that step. A dispersion relation linear with this slope would give excitation energy \(\varepsilon_1 E\). For a fermion of wave number \(k\), the kinetic energy is \(\hbar^2 k^2/(2m)\). With this quadratic dispersion the energy operator above the ground state acts on density-wave polynomials as
\[
\varepsilon_1\Bigl(E+\frac2N\,W\Bigr).
\]
{#eq-ring-energy}
For the preparations of energies two and three take odd \(N\ge3\). Since \(W u_\pm=\pm u_\pm\), the ring energies above the ground state are \(\varepsilon_1(2\pm2/N)\). An energy measurement on this shell that resolves the separation \(4\varepsilon_1/N\) determines the sign of \(S\). For \(N=101\) the predicted separation is about four hundredths of the spacing \(\varepsilon_1\) between successive levels of the linear spectrum. [Kinetic energy in the density waves](11-states-and-lines.md#ch11-cubic-observable)

Position measurement on the ring gives a separate test. Form \(C\) from the first two density waves of the measured positions. Its mean in \(u_\pm\) involves moments of weight four and hence equals \(\pm2\) for \(N\ge4\) in the stated odd-\(N\) regime. The full distribution still depends on \(N\). At any finite odd \(N\ge3\), the means of \(|p_1|^{2(N-1)}\) in the two preparations differ by one. Here both density waves are functions of the same particle positions, so a high moment of the first can distinguish their position laws. As \(N\) grows, the joint law of finitely many waves tends to its marginal under \(\mu\) in the ground state and under \(|F_\pm|^2d\mu\) in the two preparations. [Finite-ring moments and their disk limit](11-states-and-lines.md#ch11-boundary-fermions)

What does \(W\) measure at higher energy? At energy three the monomials \(p_1^3\), \(p_1p_2\) and \(p_3\) form a basis, and the definition gives
\[
W\,p_1^3=3p_1p_2,\qquad W\,(p_1p_2)=p_1^3+2p_3,\qquad W\,p_3=3p_1p_2 .
\]
Its eigenvalues are \(3,0,-3\), with unit eigenvectors
\[
\frac{p_1^3+3p_1p_2+2p_3}{6},\qquad\frac{p_1^3-p_3}{3},\qquad\frac{p_1^3-3p_1p_2+2p_3}{6}.
\]
These are three preparations which \(W\) distinguishes with certainty. On the ring they are stationary states from the shell \(E=3\), at the energies \(\varepsilon_1(3+6/N)\), \(3\varepsilon_1\) and \(\varepsilon_1(3-6/N)\). In the first and the third, a count of quanta finds the three basis occupations with the same probabilities \(\tfrac16,\tfrac12,\tfrac13\). At \(N=3\) the third polynomial equals \(x_1x_2x_3\). It takes the occupied momentum labels \(\{-1,0,1\}\) to \(\{0,1,2\}\), leaving a hole at the lower edge while adding a particle above the upper edge. The energy formula still applies exactly.

At every energy \(n\) the Schur polynomials \(s_\lambda\) give an orthonormal eigenbasis of \(W\). A partition \(\lambda\) of \(n\) lists positive integers in weakly decreasing order with sum \(n\). Give row \(i\) of its diagram \(\lambda_i\) boxes. For \(N\ge n\), the state \(s_\lambda\) times the ground state is the determinant obtained by moving the \(i\)-th fermion from the top up by \(\lambda_i\) momentum steps. Its initial momentum label is \((N+1)/2-i\). By the quadratic dispersion, its \(j\)-th step costs \(\varepsilon_1+(2\varepsilon_1/N)(j-i)\). Each box \((i,j)\) counts one step, so the first term sums to the linear energy \(\varepsilon_1 n\). After subtracting the ground energy and \(\varepsilon_1 E\), the residual operator is \((2\varepsilon_1/N)W\). Dividing by \(2\varepsilon_1/N\) therefore gives the dimensionless eigenvalue \(\sum_{(i,j)\in\lambda}(j-i)\). At energy two, the row is \(u_+\) and reads \(0+1\), while the column is \(u_-\) and reads \(0-1\). Through energy five this sum distinguishes the diagram within its energy space. At energy six the shapes \((4,1,1)\) and \((3,3)\) both give \(3\). [The exchange at every energy](11-states-and-lines.md#ch11-cubic-observable)

In the two disk preparations, both the squared wavefunction and the reading \(C\) depend only on \(Z_1,Z_2\). Integrating out every other harmonic leaves the mean unchanged because each of its Gaussian laws has mass one. What if the detector measures a variable we intend to integrate out? Two coupled oscillators give a first case in which the answer depends on the coordinate we keep.

## Reduction must retain the measurements {#reduction-must-retain-the-measurements}

Let \(x,y\) be the displacements of two coupled oscillators. We can keep a record of \(x\) alone even when an instrument also measures \(y^2\). To predict the mean of that second reading from the first record we need the distribution of \(y\) at each fixed \(x\). Take the Euclidean quadratic action
\[
 S(x,y)=\frac12 ax^2+cxy+\frac12 by^2,
 \qquad b>0,\qquad ab>c^2 .
\]
These inequalities make the quadratic form positive definite. Let \(\hbar>0\) control the scale of fluctuations, and use ordinary Lebesgue measure. At fixed \(x\), the weight remaining after \(y\) is integrated out is
\[
Z_y(x)=\int_{\mathbb R}\exp\!\left(-\frac{S(x,y)}{\hbar}\right)\,dy.
\]
Completing the square gives
\[
S(x,y)
=\frac b2\left(y+\frac cbx\right)^2
 +\frac12\left(a-\frac{c^2}{b}\right)x^2,
\]
and hence
\[
Z_y(x)
=\sqrt{\frac{2\pi\hbar}{b}}\,
\exp\!\left[
-\frac{1}{2\hbar}\left(a-\frac{c^2}{b}\right)x^2
\right].
\tag{1.1}
\]
{#eq-gaussian-integral}

The centre of the Gaussian in \(y\) moves with \(x\). Allowing \(y\) to relax to \(-cx/b\) gives the retained coordinate its effective stiffness \(a-c^2/b\), the Schur complement of \(b\). Holding \(y=0\) instead would give stiffness \(a\). Integration also supplies the prefactor \(\sqrt{2\pi\hbar/b}\), which measures fluctuations about the displaced centre.

For the instrument measuring \(y^2\), the displaced centre gives only part of the answer. What function of \(x\) gives the mean of its readings?

**Definition (conditional expectation).** For a polynomial observable \(f(x,y)\), average over \(y\) at fixed \(x\) in the normalized Gaussian law,
\[
\mathcal E(f)(x)=\frac{1}{Z_y(x)}\int_{\mathbb R} f(x,y)e^{-S(x,y)/\hbar}\,dy .
\]
Multiplying this function by \(Z_y(x)\) and integrating over \(x\) recovers the original integral with insertion \(f\). From the completed square, \(y\) at fixed \(x\) has mean \(-cx/b\) and variance \(\hbar/b\). Writing \(\langle f\rangle_x=\mathcal E(f)(x)\) gives
\[
\langle y\rangle_x=-\frac cbx,
\qquad
\langle y^2\rangle_x=\frac{c^2}{b^2}x^2+\frac{\hbar}{b}.
\tag{1.2}
\]
{#eq-gaussian-moments}
The second term in \(\langle y^2\rangle_x\) is the conditional variance. At \(x=0\) the mean displacement of the hidden oscillator is zero, yet a detector sensitive to its squared displacement reads \(\hbar/b\) on average.

The map \(\mathcal E\) is linear and sends \(1\) to \(1\). For two insertions of \(y\), the failure of multiplicativity is the variance
\[
\mathcal E(y^2)-\mathcal E(y)^2=\frac{\hbar}{b}.
\tag{1.3}
\]
{#eq-conditional-product-defect}
The covariance of two Gaussian field insertions is the mean of their product minus the product of their means. Pairing insertions by the covariance is a *contraction*. At fixed \(x\) first subtract the conditional mean of \(y\). Products of an even number of centred Gaussian insertions average to the sum over pairings of their covariances, and odd products have zero mean. Restoring the conditional means then recovers the moments of the original variables. Successive Gaussian integrations must give this same joint expectation.

There is a second loss of information if we keep only normalized expectations. Hold the effective stiffness \(a-c^2/b\) fixed and change \(b\), adjusting \(a\) accordingly. Equation (1.1) gives the same normalized distribution of \(x\) but a different absolute integral, through the factor \(\sqrt{2\pi\hbar/b}\). To glue Gaussian integrals one needs those factors as well. In a field theory their infinite-dimensional determinants and phases require a definition. The next example has a normalization that can be calculated as a function of the separation of its sources.

::: figure fig-gaussian-reduction

In three-dimensional abelian Chern–Simons theory a Wilson line of charge \(a\) couples to the integral of the gauge one-form along its oriented curve. Put two rays of charges \(a,-a\) at distinct boundary points \(r,0\), with \(a\) real and \(0<r<1\). Work at level one, with neutral vacuum \(|0\rangle=1\). An enclosing contour sees zero total charge. To determine which neutral state the pair actually prepares we can ask first for its vacuum coefficient and then for its response to every positive current mode.

For the vacuum coefficient use the planar Cauchy propagator and disjoint radial regularizations. Give the rays parallel framings and subtract each self-contraction. The rays are disjoint graphs, vertical near the boundary tests and above the bending region. In the real ordered chamber bring the outgoing ends to separation \(\epsilon d\) with fixed \(d>0\). As \(\epsilon\) tends to zero require uniform bounds on the graphs and their first derivatives on the compact intervals met by the tests, and smooth convergence there. The mutual contraction gives \(r^{-a^2}(\epsilon d)^{a^2}\). Dividing out the outgoing factor leaves the vacuum coefficient \(r^{-a^2}\).

For the mode responses, expand the current \(a/(w-r)-a/w\) on a contour enclosing both endpoints. The \(w^{-1}\) terms cancel, as total charge requires. For every \(n>0\) the coefficient of \(w^{-n-1}\) is \(ar^n\). On the polynomial variables this says \(n\partial_{p_n}\Psi=ar^n\Psi\). These equations fix the state up to its constant term. Inserting the vacuum coefficient just calculated gives
\[
 \Psi_{a,r}=r^{-a^2}\exp\!\left(a\sum_{n>0}\frac{r^n}{n}J_{-n}\right)|0\rangle .
\]
The exponential specifies a polynomial coefficient at each energy. The disk norm decides whether those coefficients form a vector in the completed state space.

Use the disk with the same centre, angular coordinate and zero constant mode as in the two-harmonic measurement. Under the vacuum law \(\mu\) the complex amplitudes \(Z_n\) in \(h(z)=\sum_{n>0}Z_nz^n/n\) are independent, with variance \(n\). The moment \(n^m m!\) is the squared norm of \(J_{-n}^m|0\rangle\). Thus multiplication by \(Z_n\) again represents \(J_{-n}\) on holomorphic polynomials, now in every harmonic.

We can prepare a disk field directly by coupling it to \(a\) at \(r\) and \(-a\) at zero. Its density relative to the vacuum is proportional to \(e^{2a\operatorname{Re}h(r)}\). Completing the square in each complex coordinate shifts its mean to \(ar^n\) and leaves its variance \(n\). The squared norm of \(e^{ah(r)}\) is \(\exp(a^2\sum_{n>0}r^{2n}/n)=(1-r^2)^{-a^2}\), finite in the chosen range. On substituting \(p_n=Z_n\), the ray state becomes \(r^{-a^2}e^{ah(r)}\). Squaring and normalizing therefore gives exactly the disk law, on every harmonic amplitude. Occupation-number projections ask a different question about the same state.

A collar of Euclidean length \(-\log q\), with \(0<q\le1\), measures their propagation. After subtracting the vacuum energy, propagation multiplies an energy-\(m\) amplitude by \(q^m\). Write this operator \(q^{L_0}\), so that \(L_0\) measures total oscillator energy. The same Gaussian moment sum, now weighted by \(q^n\) in mode \(n\), gives
\[
 \frac{\langle\Psi_{a,r},q^{L_0}\Psi_{a,r}\rangle}{\|\Psi_{a,r}\|^2}
 =\left(\frac{1-r^2}{1-qr^2}\right)^{a^2}.
\]
The collar acts on the second amplitude, replacing \(r\) there by \(qr\). Its pairing with the first therefore involves \(qr^2\). The ratio is one at zero collar length. The scalar \(r^{-a^2}\) cancels at every length, just as the determinant cancels from a normalized finite Gaussian. Computing an absolute amplitude requires the normalization of the filling. [The disk and cylinder actions](11-states-and-lines.md#ch11-harmonic-disk-and-collar) · [Ray regularization and the sourced disk](11-states-and-lines.md#ch11-neutral-ray-pair)

## From products to local operations {#from-products-to-local-operations}

Bringing the two rays closer changes their vacuum coefficient by a power of their separation. How can the product of two insertions record that dependence? Forgetting the positions gives only a bilinear map on a space \(A\) of observables,
\[
m:A\otimes A\longrightarrow A.
\]
For *local* observables, keep one point \(w\) fixed in a complex coordinate disk and move the other to \(z=w+t\). Acting with the field of a state \(a\) on a state \(b\) gives \(Y(a,t)b\), a Laurent series in the separation \(t\). Each coefficient is a state at \(w\). The negative powers record the singularity as \(z\) approaches \(w\). [Fields acting on states](03-local-fields.md#fields-and-modes)

For the free current write \(\kappa\) for the boundary level itself, equal to one in the oscillator experiment. The current product at distinct points has singular part
\[
J(z)J(w)\sim \frac{\kappa}{(z-w)^2}.
\tag{1.4}
\]
{#eq-current-singularity}
The symbol \(\sim\) gives the terms singular as \(z\) approaches \(w\). The scalar in the double pole multiplies the identity operator. All omitted terms are regular at \(z=w\).

Even this one pole has two different expansions. In the region \(|w|<|z|\),
\[
\frac1{(z-w)^2}
=\sum_{n\ge0}(n+1)\frac{w^n}{z^{n+2}},
\]
whereas in \(|z|<|w|\),
\[
\frac1{(z-w)^2}
=\sum_{n\ge0}(n+1)\frac{z^n}{w^{n+2}}.
\tag{1.5}
\]
{#eq-local-expansions}
These are Taylor expansions of the same rational function in two different ratios. In the first, the insertion at \(w\) is inside the contour through \(z\). Interchanging the radii gives the second. For a formal field the inner and outer variables specify an order of expansion even when no analytic convergence is assumed.

::: figure fig-local-expansions

What survives of the double pole at the point of collision? Integrate it against a regular test function \(f(t)\) around \(t=0\), with the positive contour divided by \(2\pi i\). The residue \(\operatorname{Res}_{t=0} f(t)t^{-2}dt=f'(0)\) distinguishes \(f(t)=t\) from zero although the two have the same value at the origin. A collision output must retain differentiation in the separation. On a smooth complex algebraic curve \(X\), let \(j\) include the distinct pairs in \(X^2\) and let \(\Delta(x)=(x,x)\) be the diagonal inclusion. The Beilinson–Drinfeld **chiral bracket** has precisely such an output,
\[
 \mu_{\mathrm{ch}}:j_*j^*(L\boxtimes L)\longrightarrow\Delta_*L .
\]
Here \(L\) is a right module for the differential operators on \(X\). Its external product \(L\boxtimes L\) has one copy at each input position. The source allows poles at the diagonal, and the map commutes with differential operators in both positions. The direct image \(\Delta_*L\) holds outputs on the diagonal and their finite normal derivatives. For the displayed current, testing with \(1\) gives zero, while testing with \(t\) gives \(\kappa\). The bracket is skew-symmetric. Its Jacobi identity compares *three* ways of first fusing a pair of inputs. A unit, when specified, is a map from the one-forms \(\omega_X\) whose bracket acts by taking principal parts. [Right differential modules](03-local-fields.md#differential-modules) · [The chiral operation on the diagonal](04-factorization.md#chiral-operation)

Even when an amplitude is known at every configuration of distinct points, extending it to a collision can require a choice. Prepare four oscillator-free charge-one inputs at level two. On the outgoing state apply the functional which extracts the oscillator-free coefficient and takes value one on the charge-four state with no excitations. With fixed coordinate frames and the Gaussian ray prescriptions, that coefficient on the separated points is a branch of \(\prod_{i<j}(z_i-z_j)^{1/2}\). Winding a pair once multiplies it by \(-1\). Rotating the whole configuration through a full turn winds six pairs and gives \(+1\).

Fix the common position and vary the three independent differences. On this labelled transverse slice the nearby separated configurations, with coefficients in the branches of the amplitude, have cohomology of dimension two in degrees two and three at the full collision and zero at every proper collision. To decide which nearby classes extend, take cochains of a proposed extension on a small neighbourhood of the collision and restrict them to its distinct-point part. Shrinking the neighbourhood gives the attaching map. Its image on cohomology is the space of extendible classes.

For the perverse sheaves in Chapter 4, one imposes bounds both on cohomology at a collision and on cohomology supported there. A family of quotient extensions has the same ranks at the collision for every member, yet a different attaching image for each line in the degree-two space. Within this family, permutation symmetry and the choice \(+i\) for a positive exchange leave the trivial and sign lines. Ordinary pullback from the unordered quotient selects the trivial line. To choose an extension for a physical preparation one needs its attaching map. [Four charged rays and their possible attachments](04-factorization.md#ch04-gaussian-collision)

There is another choice even before one extends across a collision. Are the inputs merely labelled, or are they arranged in a word? Consider the triple \((x,y,x)\) with \(x\ne y\). Its first and third inputs can form one cluster disjoint from the middle input. Neither consecutive cut \(1|23\) nor \(12|3\) separates the two blocks. In either cut \(x\) lies on both sides. The allowed cuts determine the open sets on which separate clusters can be multiplied.

For a fixed word, summing over consecutive cuts gives an *ordered convolution*. A multiplication for it combines consecutive groups of inputs. To impose factorization, assemble successive multiplications and their associativity homotopies into a complex, the bar construction. Its coproduct cuts a word. For an associative chiral algebra in this word construction, restriction to the open of a cut identifies the bar coefficient of the whole word with the tensor product of the two block coefficients. The example \((x,y,x)\) locates a point where neither consecutive cut gives that information. A chiral quantum group also needs a rule for the action on two systems at coincident positions. [The geometry of ordered cuts](04-factorization.md#ordered-cut-geometry) · [The bar construction on words](05-bar-and-coherence.md#ch05-ordered-cuts-give-a-finite-geometric-bar-construction)

## Why representations and centres enter {#why-representations-and-centres-enter}

A ray of charge \(a\) and one of charge \(b\) respond differently to an enclosing current even when the same operator relations hold in both sectors. Each sector is described by a representation, or module, \(M\) of the observable algebra \(A\). An element of \(A\) acts on \(M\), and a product acts by successive operations. Place the two rays side by side. The total charge is \(a+b\). How can a rule on the observables tell us this for every pair of modules?

For an ordinary bialgebra \(H\), a coproduct \(\Delta:H\to H\otimes H\) writes each single observable as a sum of pairs to be applied to the two modules. For \(m\in M,\ n\in N\), the resulting diagonal action is
\[
h\cdot(m\otimes n)
=\sum h_{(1)}m\otimes h_{(2)}n,
\qquad
\Delta(h)=\sum h_{(1)}\otimes h_{(2)}.
\tag{1.6}
\]
{#eq-tensor-action}
For a conserved additive charge \(Q\), take \(\Delta Q=Q\otimes1+1\otimes Q\). On a product of states with charges \(a,b\), the two terms act by \(a,b\), giving total charge \(a+b\). Requiring \(\Delta(hh')=\Delta(h)\Delta(h')\) makes acting by a product the same as acting in succession. Coassociativity says that the action on three modules is independent of how their tensor product is parenthesized. A coproduct invariant under the exchange of factors makes the usual flip a module map. A more general exchange requires a braiding with its own compatibility equations. A chiral quantum group must solve these problems for operations that depend on position. [Tensor actions](02-algebras-and-modules.md#ch02-a-coproduct-gives-the-action-on-a-tensor-product) · [Exchange and its two hexagons](02-algebras-and-modules.md#ch02-associators-exchange-and-coherence)

Now hold the bulk insertion fixed and change the boundary state on which it acts. If the insertion is separated from the boundary, its action should commute with boundary operators. It should also commute with transporting states along a map of boundary representations. For an ordinary algebra \(A\) this asks for an \(A\)-linear operator \(T_M\) on every module \(M\), compatible with every module map. How large is the space of such choices? It suffices to test the action on one vector in one module.

**Proposition (the centre acting on modules).** Let \(A\) be a unital associative algebra over a field. An \(A\)-linear operator \(T_M\) on every left \(A\)-module \(M\), satisfying \(fT_M=T_Nf\) for every module map \(f:M\to N\), is multiplication by a unique element of the centre \(Z(A)=\{z\in A:za=az\text{ for all }a\in A\}\).

*Proof.* Let \(A\) act on itself by left multiplication and put \(z=T_A(1)\). Left linearity gives \(T_A(a)=az\). Right multiplication by \(a\) is a left module map, so applying naturality to \(1\) gives \(T_A(a)=za\). For \(m\in M\), the map \(A\to M,\ a\mapsto am\), is also a module map. Evaluating its naturality equation at \(1\) gives \(T_M(m)=zm\). Conversely a central element defines such an \(A\)-linear family, and its value on \(1\in A\) recovers it. ∎

The proof used \(A\) as a module over itself, with multiplication on both sides. Equivalently, a map \(A\to A\) respecting left and right multiplication is determined by its value on \(1\), which can be any central element. One can therefore compute \(Z(A)\) as a space of bimodule maps. For complexes the corresponding derived space is modeled by the Hochschild cochain complex \(C^\bullet(A,A)=\operatorname{RHom}_{A\otimes A^{\mathrm{op}}}(A,A)\). The opposite algebra \(A^{\mathrm{op}}\) reverses multiplication, so a module for \(A\otimes A^{\mathrm{op}}\) carries the two actions of a bimodule. Derived Hom retains maps up to homotopy and their higher extension groups. For a chiral boundary one must in addition compare those operations when points separate or collide.

## The mathematical problem in its present form {#the-mathematical-problem-in-its-present-form}

In the Gaussian half-space one can construct the action of an interior observable directly. Let \(V\) be open in the boundary and \(A_\partial(V)\) its observables for the chosen boundary condition. Choose a bulk open \(U\) at positive normal separation above a thin collar of \(V\). In the joint region represent \(f\) from \(U\) by its extension \(\operatorname{ext}_U(f)\), and \(v\) from \(V\) by the quantum collar inclusion \(i_\hbar(v)\). Multiply there and project back to the boundary by \(p_\hbar\). This gives
\[
 \beta_{U;V}(f)(v)=p_\hbar\bigl(\operatorname{ext}_U(f)\,i_\hbar(v)\bigr),
 \qquad v\in A_\partial(V).
\]
A unit probe for harmonic \(j\) contracts with a single \(p_n\) to give \(\delta_{jn}\), one for \(j=n\) and zero otherwise. Summing over the factors of a monomial gives \(\partial_{p_j}\). This is the action on the chosen polynomial representatives that supplied the energy-two exchange. The probe can have nonzero differential. This calculation takes place on cochains. To pass from particular probes to a reconstruction theorem one would have to characterize *all* compatible actions and show that bulk observables realize them. [The supported probe calculation](11-states-and-lines.md#ch11-relative-phase)

**Open problem (bulk reconstruction).** Fix the class of coherent actions on boundary observables, including their restrictions to separated points and their behavior at collisions. Does a geometric centre represent those actions, and under what hypotheses do the supported bulk insertions induce an equivalence from bulk observables to this centre that preserves factorization? [Bulk actions and the universal centre](17-holographic-reconstruction.md#bulk-action-and-centre)

There is a corresponding question for boundary conditions themselves. Suppose an interface gives functors \(\Phi,\Psi\) carrying modules across it in opposite directions, with \(\Phi\) left adjoint to \(\Psi\). This means a map from \(\Phi M\) to \(N\) corresponds naturally to one from \(M\) to \(\Psi N\). The unit \(\eta_{M'}:M'\to\Psi\Phi M'\) compares a module with the result of crossing and returning. Under the adjunction, \(\Phi(g)\) for a map \(g:M\to M'\) corresponds to \(\eta_{M'}\circ g\). Thus comparing maps before and after the crossing tests the unit on maps from every \(M\). The unit is an equivalence on every module precisely when \(\Phi\) induces equivalences on all spaces of maps. The counit \(\Phi\Psi\to\mathrm{id}\) tests recovery on the other side. Matching the state of a specified filling and its absolute scalar or determinant line is a further condition even for equivalent module categories. [The unit and counit](06-duality-and-induction.md#adjunction-comparison-maps) · [The amplitude of a filling](17-holographic-reconstruction.md#states-lines-and-caps)

A third insertion already tests where such a comparison can be made. Fuse the first two fields in a Laurent series in their separation \(p\), leaving the third state in a complex vector space \(W\). If the coefficients of the fused pair lie in \(V\), tensoring after expansion gives \(V((p))\otimes W\). Expanding after tensoring gives \((V\otimes W)((p))\). In both expressions the series have finitely many negative powers. Choose \(v\ne0\) in \(V\) and independent \(w_0,w_1,\ldots\) in \(W\). The latter space contains \(\sum_{j\ge0}(v\otimes w_j)p^j\). An algebraic tensor in the former is a finite sum, so its coefficients use only a fixed finite-dimensional subspace of \(W\). Applying a functional taking \(v\) to \(1\) rules out such a bound for our series. A comparison of the two orders must specify the space in which its maps take values. [Laurent series with algebraic coefficients](08-completions.md#ch08-laurent-series-with-algebraic-coefficients)

For a symmetry acting on a boundary, which operators of a second system can couple to its generators? Even on the two-dimensional span of \(a,b\), two proposed operators can fail a single bracket relation. The algebra that represents the solutions answers the question for one system. Combining two solutions asks for an action on a tensor product. [The coupling equation](02-algebras-and-modules.md#ch02-consistent-lie-couplings) · [The action on a pair](02-algebras-and-modules.md#ch02-a-coproduct-gives-the-action-on-a-tensor-product)

::: figure fig-programme-overview
