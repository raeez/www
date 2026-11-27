# Boundary observables and reconstruction

Suppose a quantum field occupies a half-space and its boundary is available for measurements. Which measurements in the interior can be reproduced at the boundary? Even for two oscillators there are states which agree on every measurement of either mode separately. The self-adjoint observable which converts two quanta of the first mode into one quantum of the second and includes the reverse process distinguishes their normalized sum from their normalized difference. Reconstructing a state therefore depends on which *joint* measurements the boundary theory supplies.

For the two oscillators this question can be answered completely, and the answer already shows how a joint measurement is made from local fields.

## Two preparations and one joint measurement {#ch01-two-preparations}

Take the first two harmonics of a free current on a circle. A state of one harmonic is specified by its number of quanta. The states with \(m_1\) quanta in the first harmonic and \(m_2\) in the second therefore form a basis of the joint state space. Write such a basis state as the monomial \(p_1^{m_1}p_2^{m_2}\) in two variables, so that the state with no quanta is the constant \(1\). Adding a quantum to harmonic \(n\) is multiplication by \(p_n\). At level one the modes of the current act by
\[
J_{-n}=p_n\cdot(-),\qquad J_n=n\frac{\partial}{\partial p_n}\qquad(n=1,2).
\]
{#eq-two-harmonic-modes}
Thus \(J_{-n}\) adds a quantum to harmonic \(n\) and \(J_n\) removes one. They satisfy \([J_n,J_{-n}]=n\), and modes of different harmonics commute. [Chapter 3](03-local-fields.md#heisenberg-current) obtains the same operators for all harmonics from the current \(J(z)\).

Two requirements fix the inner product. The state \(1\) has norm one, and \(J_n\) is the adjoint of \(J_{-n}\), as for the Fourier modes of a real current. Moving the removal operators to the right shows that distinct monomials are orthogonal and that
\[
\bigl\|p_1^{m_1}p_2^{m_2}\bigr\|^2=m_1!\,2^{m_2}\,m_2!.
\]
{#eq-two-harmonic-norms}
For instance \(\|p_1^2\|^2=\langle1,J_1^2\,p_1^2\rangle=2\) and \(\|p_2\|^2=\langle1,J_2\,p_2\rangle=2\). A quantum of harmonic \(n\) has energy \(n\), so \(p_1^{m_1}p_2^{m_2}\) has energy \(m_1+2m_2\). The states of energy two are spanned by the unit vectors
\[
a=\frac{p_1^2}{\sqrt2},\qquad b=\frac{p_2}{\sqrt2}.
\]
These are the states \(a\) and \(b\) of the introduction.

What can counting quanta reveal about a superposition? Prepare \(\psi=\alpha a+\beta b\) with \(|\alpha|^2+|\beta|^2=1\). A count finds two quanta in the first harmonic and none in the second with probability \(|\alpha|^2\). It finds none in the first and one in the second with probability \(|\beta|^2\). Now let \(A\) be any operator which acts on the first harmonic alone. It leaves the number of quanta in the second harmonic unchanged, so \(Aa\) is orthogonal to \(b\), and \(Ab\) is orthogonal to \(a\). Hence
\[
\langle\psi,A\psi\rangle=|\alpha|^2\langle a,Aa\rangle+|\beta|^2\langle b,Ab\rangle .
\]
The same argument applies to an operator on the second harmonic alone, because \(a\) and \(b\) contain different numbers of quanta of the first. No measurement on a single harmonic depends on the relative phase of \(\alpha\) and \(\beta\). In particular the sum and the difference
\[
u_\pm=\frac{a\pm b}{\sqrt2}=\frac{p_1^2\pm p_2}{2}
\]
{#eq-sum-and-difference}
give identical statistics in every such measurement.

The exchange \(S\), defined on the states of energy two by \(Sa=b\) and \(Sb=a\), does depend on that phase. Indeed \(Su_\pm=\pm u_\pm\), and in general \(\langle\psi,S\psi\rangle=2\operatorname{Re}(\bar\alpha\beta)\). Which operator made from the current has this effect? It must lower \(m_2\) by one while raising \(m_1\) by two, or do the reverse. The products of modes which do so are \(J_{-1}^2J_2\) and \(J_{-2}J_1^2\), and each is the adjoint of the other. Their sum is
\[
O=J_{-1}^2J_2+J_{-2}J_1^2
 =2p_1^2\frac{\partial}{\partial p_2}+p_2\frac{\partial^2}{\partial p_1^2},
\qquad
O\,p_2=2p_1^2,\quad O\,p_1^2=2p_2 .
\]
{#eq-energy-two-exchange}
Therefore \(Oa=2b\) and \(Ob=2a\). On the states of energy two the field operation \(O\) equals \(2S\), and its expectations in the two preparations are \(\langle u_\pm,Ou_\pm\rangle=\pm2\).

The introduction describes a second instrument, which uses no operators. Fill the unit disk with a real harmonic function \(\phi=h+\bar h\), where \(h(z)=\sum_{n\ge1}Z_nz^n/n\) is holomorphic and the constant term of \(\phi\) is zero. The first two coefficients are derivatives at the centre, \(Z_1=h'(0)\) and \(Z_2=h''(0)\). The Dirichlet energy
\[
S_D=\frac1{8\pi}\int_D|\nabla\phi|^2\,d^2z=\frac12\sum_{n\ge1}\frac{|Z_n|^2}{n}
\]
gives each field the amplitude \(e^{-S_D}\). The square of this amplitude is a probability law \(\mu\) in which the \(Z_n\) are independent complex Gaussian variables with \(\mathbb E_\mu|Z_n|^2=n\). This is the law of the unexcited disk. Its moments are
\[
\mathbb E_\mu\bigl[|Z_1|^{2m_1}|Z_2|^{2m_2}\bigr]=m_1!\,2^{m_2}\,m_2!,
\]
the squared norms found above. Substituting \(Z_n\) for \(p_n\) therefore sends a unit state to a polynomial \(F(Z)\) with \(\mathbb E_\mu|F|^2=1\). The disk prepared in that state has the law \(|F|^2\,d\mu\). The two preparations become \(F_\pm=(Z_1^2\pm Z_2)/2\).

For each sample of the field compute the real number
\[
C=2\operatorname{Re}\bigl(Z_1^2\,\overline{Z_2}\bigr)
 =2|Z_1|^2\,|Z_2|\cos(2\theta_1-\theta_2),
\]
{#eq-disk-reading}
where \(\theta_n\) is the phase of \(Z_n\). The reading compares the phase of the second harmonic with twice the phase of the first, weighted by the strengths of both waves. Since \(|Z_1^2\pm Z_2|^2=|Z_1|^4+|Z_2|^2\pm C\), its mean in the two prepared laws is
\[
\mathbb E_\pm C
=\tfrac14\,\mathbb E_\mu\bigl[(|Z_1|^4+|Z_2|^2)\,C\bigr]\pm\tfrac14\,\mathbb E_\mu\bigl[C^2\bigr]
=0\pm\tfrac12\,\mathbb E_\mu|Z_1|^4\;\mathbb E_\mu|Z_2|^2=\pm2 .
\]
The first expectation vanishes on averaging over the phase of \(Z_2\). In the second, \(C^2=4|Z_1|^4|Z_2|^2\cos^2(2\theta_1-\theta_2)\), and the squared cosine has average one half. The disk therefore reproduces the expectations \(\pm2\) of the field operation \(O\). Each harmonic taken alone has the same law in both preparations, because the term \(\pm C\) averages to zero over the phase of the other harmonic. [Chapter 11](11-states-and-lines.md#ch11-relative-phase) constructs \(O\) from probes in a half-space. It also shows that multiplying a holomorphic polynomial by \(C\) and projecting the product back onto holomorphic polynomials is the operator \(O\).

The operator \(O\) was assembled from three modes chosen for the purpose. It is the energy-two part of a single observable of the current. Allow all harmonics, with \(J_{-n}=p_n\) and \(J_n=n\,\partial/\partial p_n\) for every \(n\ge1\), and define on states of finite energy
\[
W=\frac12\sum_{i,j\ge1}\bigl(J_{-i}J_{-j}J_{i+j}+J_{-i-j}J_iJ_j\bigr).
\]
{#eq-cubic-observable}
Only finitely many terms are nonzero on a state of given energy, and each term preserves the energy. On a state of energy two only \(i=j=1\) contributes, so there \(W=\tfrac12O=S\). On states of zero total charge, where the mode \(J_0\) vanishes, the same operator is a residue of the current \(J(z)=\sum_nJ_nz^{-n-1}\):
\[
W=\frac16\operatorname{Res}_{z=0}\,z^2\,{:}J(z)^3{:}\;dz .
\]
{#eq-cubic-residue}
The colons place the removal operators \(J_n\), \(n>0\), to the right in each product of three modes. To check the formula, note that the residue selects the products \(J_iJ_jJ_k\) with \(i+j+k=0\). Each term of \(W\) arises from three such ordered triples, which gives the factor \(\tfrac16\cdot3=\tfrac12\). The exchange is therefore a contour integral of three currents multiplied *at one point*, after the singular terms of their product have been removed. An instrument which measures wave patterns around the whole circle can be built from local fields at coincident positions.

In which physical system does an instrument record \(W\)? Put \(N\) free fermions of mass \(m\) on a ring of circumference \(L\), without spin and with \(N\) odd, in their ground state. The fermions fill the momenta \(2\pi\hbar j/L\) with \(|j|\le(N-1)/2\). A wave of the particle density with \(n\) oscillations around the ring adds momentum \(2\pi\hbar n/L\). For \(n\) small compared with \(N\) these waves are the harmonics of a current at level one. Let \(E\) be the operator which multiplies a state of energy \(n\), in the units used above, by \(n\). If the energy of a fermion were proportional to its momentum, the excitation energy of the ring would be \(\varepsilon_1E\), with \(\varepsilon_1=2\pi\hbar v_F/L\). Here \(v_F=\pi\hbar N/(mL)\) is the velocity of a fermion at the upper end of the filled momenta. The kinetic energy \(\hbar^2k^2/2m\) is instead a curved function of the momentum \(\hbar k\), and the excitation energy is exactly
\[
\varepsilon_1\Bigl(E+\frac2N\,W\Bigr).
\]
{#eq-ring-energy}
The level with two quanta therefore splits into the two energies \(\varepsilon_1(2\pm2/N)\), and its stationary states are \(u_+\) and \(u_-\). An energy measurement which resolves the separation \(4\varepsilon_1/N\) is a measurement of the exchange \(S\). For \(N=101\) the separation is about four hundredths of the spacing \(\varepsilon_1\) between successive levels. The formula holds for fermions which do not interact, for excitations near one end of the filled momenta. [Fermions on the boundary circle](11-states-and-lines.md#ch11-boundary-fermions)

What does \(W\) measure at higher energy? At energy three the monomials \(p_1^3\), \(p_1p_2\) and \(p_3\) form a basis, and the definition gives
\[
W\,p_1^3=3p_1p_2,\qquad W\,(p_1p_2)=p_1^3+2p_3,\qquad W\,p_3=3p_1p_2 .
\]
Its eigenvalues are \(3,0,-3\), with unit eigenvectors
\[
\frac{p_1^3+3p_1p_2+2p_3}{6},\qquad\frac{p_1^3-p_3}{3},\qquad\frac{p_1^3-3p_1p_2+2p_3}{6}.
\]
These are three preparations which \(W\) distinguishes with certainty. On the ring they are the stationary states of the level with three quanta, at the energies \(\varepsilon_1(3+6/N)\), \(3\varepsilon_1\) and \(\varepsilon_1(3-6/N)\). In the first and the third, a count of quanta finds the three basis states with the same probabilities \(\tfrac16,\tfrac12,\tfrac13\).

At every energy \(n\) the eigenvectors of \(W\) are the Schur polynomials \(s_\lambda\), one for each partition \(\lambda\) of \(n\). They form an orthonormal basis of the states of energy \(n\). Draw \(\lambda\) as a Young diagram with \(\lambda_i\) boxes in row \(i\). The eigenvalue is the sum of \(j-i\) over the boxes, where \(i\) is the row and \(j\) the column of a box. At energy two the row of two boxes is \(u_+\), with eigenvalue \(0+1\), and the column of two boxes is \(u_-\), with eigenvalue \(0-1\). Through energy five the readings at each energy are all different. At energy six the diagrams with rows \((4,1,1)\) and \((3,3)\) both give \(3\). A single joint observable then no longer distinguishes every pair of these preparations, and one must ask which further measurements the boundary supplies. [The exchange at every energy](11-states-and-lines.md#ch11-cubic-observable)

In the disk experiment every harmonic fluctuates, although the reading used only two of them. This raises a prior question about the observables themselves. Once a degree of freedom has been eliminated, how does one measure something that used to depend on it? A pair of coupled coordinates lets us answer this question without making any assumptions about a quantum field theory.

## Reduction must retain the measurements {#reduction-must-retain-the-measurements}

Let \(x,y\) be the displacements of two coupled oscillators. A measurement retains \(x\) but averages over \(y\). Take the Euclidean quadratic action
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

The measured coordinate has effective stiffness \(a-c^2/b\), the Schur complement of \(b\) in the quadratic form. Indeed \(y\) can relax toward \(-cx/b\) when \(x\) is displaced. Fluctuations about that value supply the factor \(\sqrt{2\pi\hbar/b}\). Freezing \(y=0\) would assign stiffness \(a\) to the remaining oscillator.

The same distinction appears when the eliminated variable occurs in an observable. Its conditional moments are
\[
\langle y\rangle_x=-\frac cbx,
\qquad
\langle y^2\rangle_x=\frac{c^2}{b^2}x^2+\frac{\hbar}{b}.
\tag{1.2}
\]
{#eq-gaussian-moments}
The second term in \(\langle y^2\rangle_x\) is the conditional variance. At \(x=0\) the mean displacement of the hidden oscillator is zero, yet a detector sensitive to its squared displacement reads \(\hbar/b\) on average.

For a polynomial observable \(f(x,y)\), the corresponding function of \(x\) is its conditional expectation,
\[
\mathcal E(f)(x)
=Z_y(x)^{-1}
\int_{\mathbb R}
f(x,y)e^{-S(x,y)/\hbar}\,dy.
\]
It is linear and preserves the constant observable, but it is generally not multiplicative. Equations (1.2) give
\[
\mathcal E(y^2)-\mathcal E(y)^2=\frac{\hbar}{b}.
\tag{1.3}
\]
{#eq-conditional-product-defect}
The same covariance term occurs when integrating out Gaussian modes of a field. Physicists call the pairing of two field insertions by the covariance a *contraction*. More insertions bring more possible pairings. Their contribution must give the same expectation whichever pair of modes is integrated out first.

The factor in (1.1) poses another question. It cancels from normalized expectations at a single fixed value of the parameters, but it matters when unnormalized amplitudes are compared, when parameters vary, or when two pieces of a theory are glued. In an infinite-dimensional field theory, the corresponding determinants and their phases need their own definition. A theorem about normalized correlations is consequently different from a theorem about the vacuum amplitude.

::: figure fig-gaussian-reduction

One can now ask for a comparison involving two genuine field theories. In three-dimensional abelian Chern–Simons theory a Wilson line of charge \(a\) couples a gauge one-form to its integral along an oriented curve. Place two such rays of charges \(a,-a\) at \(r,0\) on the boundary, with \(a\) real and \(0<r<1\). The net charge is zero. At current level one let \(|0\rangle\) be the neutral vacuum and let \(J_{-n}\), \(n>0\), create a boundary oscillator of energy \(n\). With the prescribed parallel framing and subtraction of self-contractions, let the separation of the outgoing rays tend to zero. Dividing out the resulting factor of outgoing separation leaves the dependence on the incoming separation \(r\). The prepared state is
\[
 \Psi_{a,r}=r^{-a^2}\exp\!\left(a\sum_{n>0}\frac{r^n}{n}J_{-n}\right)|0\rangle .
\]
This exponential is a vector in the oscillator space. To compare it with a disk filling we must specify both a common space of wavefunctions and a common measurement.

On the unit disk take a real harmonic field with zero constant mode. Write it as \(h+\bar h\), where \(h(z)=\sum_{n>0}Z_nz^n/n\). The squared vacuum amplitude of the disk gives each complex coefficient \(Z_n\) the independent probability density \((\pi n)^{-1}e^{-|Z_n|^2/n}\,d^2Z_n\). Multiplication by \(Z_n\) represents \(J_{-n}\) on holomorphic polynomials. This identification preserves their inner products because the complex Gaussian moment \(\langle |Z_n|^{2m}\rangle=n^m m!\) is also the squared norm of \(J_{-n}^m|0\rangle\).

Couple the disk field to \(a\) at \(r\) and to \(-a\) at the origin. The squared amplitude then acquires the factor \(e^{2a\operatorname{Re}h(r)}\). Completing the square as in (1.1) shifts the mean of \(Z_n\) to \(ar^n\) and leaves its variance \(n\). The squared norm of \(e^{ah(r)}\) is \(\exp(a^2\sum_{n>0}r^{2n}/n)=(1-r^2)^{-a^2}\). Under the oscillator identification the ray wavefunction is precisely \(r^{-a^2}e^{ah(r)}\). The two preparations therefore give the same normalized probability law for the complex harmonic coordinates \(Z_n\), obtained by multiplying the vacuum Gaussian law by the squared wavefunction. Here the measured variables are the amplitudes \(Z_n\). The projectors onto occupation numbers define a different measurement on the same space.

A collar of Euclidean length \(-\log q\), with \(0<q\le1\), measures their propagation. After subtracting the vacuum energy, propagation multiplies an energy-\(m\) amplitude by \(q^m\). Write this operator \(q^{L_0}\), so that \(L_0\) measures total oscillator energy. The same Gaussian moment sum, now weighted by \(q^n\) in mode \(n\), gives
\[
 \frac{\langle\Psi_{a,r},q^{L_0}\Psi_{a,r}\rangle}{\|\Psi_{a,r}\|^2}
 =\left(\frac{1-r^2}{1-qr^2}\right)^{a^2}.
\]
This measurement is one at zero collar length. The scalar \(r^{-a^2}\) cancels from it at every length, just as the determinant cancels from a normalized finite Gaussian. Computing an absolute amplitude requires the normalization of the filling. The ray regularization and the independent disk and cylinder actions are given in [Chapter 11](11-states-and-lines.md#ch11-harmonic-disk-and-collar).

## From products to local operations {#from-products-to-local-operations}

The separation \(r\) mattered in the fusion of two rays. For two observables with no position labels their product is a bilinear map
\[
m:A\otimes A\longrightarrow A.
\]
For *local* observables the two positions belong to the input. On a complex curve with coordinate \(z\), write \(Y(a,z)\) for insertion of the field associated with a state \(a\). Its Laurent coefficients are operators on the state space. If \(a\) and \(b\) are inserted at distinct points \(z\) and \(w\), their product can have a pole as \(z\) approaches \(w\).

The basic current example has singular part
\[
J(z)J(w)\sim \frac{\kappa}{(z-w)^2}.
\tag{1.4}
\]
{#eq-current-singularity}
The symbol \(\sim\) specifies the terms singular at the diagonal \(z=w\). The omitted terms are regular there. The number \(\kappa\) is the central coefficient of this current algebra.

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
The first series corresponds to inserting the field at \(w\) inside a circle through \(z\). The second reverses those radial positions. They represent the same rational function in their respective domains. In a formal field theory the order of Laurent expansion keeps track of this distinction even in the absence of analytic convergence.

::: figure fig-local-expansions

How can a field at the coincident point remember the double pole? Test against a function \(f(t)\) of the separation \(t=z-w\). A contour integral divided by \(2\pi i\) extracts the coefficient of \(t^{-1}dt\), hence \(\operatorname{Res}_{t=0} f(t)t^{-2}dt=f'(0)\). The output must be able to act on a normal derivative. On a smooth complex algebraic curve \(X\), let \(j\) include the distinct pairs in \(X^2\), and let \(\Delta:X\to X^2\) send \(x\) to \((x,x)\). Beilinson and Drinfeld express fusion as a **chiral bracket**
\[
 \mu_{\mathrm{ch}}:j_*j^*(L\boxtimes L)\longrightarrow\Delta_*L .
\]
Here \(L\) is a right module for the differential operators on \(X\). Its external product has one copy of \(L\) at each input position. The source allows poles at the diagonal. The direct image \(\Delta_*L\) holds outputs on the diagonal and their finite normal derivatives. The bracket is skew-symmetric. Its Jacobi identity compares *three* ways of first fusing a pair of inputs. A unit, when specified, is a map from the one-forms \(\omega_X\) whose bracket acts by taking principal parts. [Chapters 3–4](04-factorization.md#chiral-operation)

Even when an amplitude is known at every configuration of distinct points, extending it to a collision can require a choice. At current level two the coefficient of the oscillator-free outgoing state of four charge-one rays is a branch of \(\prod_{i<j}(z_i-z_j)^{1/2}\). Winding a pair once multiplies this coefficient by \(-1\). Rotating the configuration through a full turn winds six pairs and gives \(+1\). One must therefore examine what survives when all four points coincide. Keep the common position fixed and vary their three independent differences. On this transverse slice the cohomology of the nearby separated configurations with the given branches has dimension two in degrees two and three. It vanishes at every proper collision. The perverse sheaves considered in Chapter 4 obey bounds on both the cohomology at each collision and the cohomology supported there. The quotient construction there gives a different extension for each line in the degree-two space, all with the same ranks at the collision point. Requiring permutation symmetry and assigning the phase \(+i\) to a positive exchange of neighbouring points leaves two lines. Requiring ordinary pullback from the unordered quotient selects the trivial one. Which line a physical collision supplies is a question about its attaching map. [Chapter 4](04-factorization.md#ch04-gaussian-collision)

A second construction retains the *order of the inputs* even as their positions vary. A cut \(1|23\) separates the first insertion from the next two provided its position differs from both of theirs. At \((x,y,x)\), \(x\ne y\), neither \(1|23\) nor \(12|3\) separates the two blocks. The decomposition \(\{1,3\}|\{2\}\) does separate them, but it cuts out a nonconsecutive block. This choice of allowed cuts changes where the factorization law applies.

For a fixed word, the operation which sums over all consecutive cuts is an *ordered convolution*. A multiplication for this convolution combines consecutive groups of inputs. Factorization requires that on an open where the two groups are disjoint their coefficients can be recovered independently. To say precisely which coefficients must factor in the associative construction, one first assembles the successive multiplications into a complex called the bar construction. Its coproduct cuts words. An associative chiral algebra puts the factorization condition on this coproduct. A chiral quantum group also needs a rule for the action on two systems at coincident positions. The convolution and the relation with the chiral bracket are developed in [Chapter 4](04-factorization.md#ordered-cut-geometry) and [Chapter 5](05-bar-and-coherence.md).

## Why representations and centres enter {#why-representations-and-centres-enter}

In the ray example the same current can act in sectors of different charge. Algebraically a sector is described by a representation, or module, \(M\) of an algebra \(A\). Its action \(A\otimes M\to M\) represents the product of observables by composition of operators. Bringing two charged lines together raises a new question. How does an observable act on the tensor product of their state spaces?

For an ordinary bialgebra \(H\), a coproduct \(\Delta:H\to H\otimes H\) supplies the diagonal action on \(M\otimes N\),
\[
h\cdot(m\otimes n)
=\sum h_{(1)}m\otimes h_{(2)}n,
\qquad
\Delta(h)=\sum h_{(1)}\otimes h_{(2)}.
\tag{1.6}
\]
{#eq-tensor-action}
The compatibility between multiplication and coproduct makes this an action. Coassociativity controls its associativity on three modules. For a conserved additive charge \(Q\), the formula \(\Delta Q=Q\otimes1+1\otimes Q\) gives total charge \(a+b\) on charge sectors \(a,b\). A coproduct invariant under the exchange of factors makes the usual flip a module map. A more general exchange requires a braiding with its own compatibility equations. A chiral quantum group must solve the corresponding problem with local position-dependent operations.

A bulk observable acting at a distance from the boundary should commute with moving a boundary operation past it. There is an algebraic model for this requirement. Suppose an operator \(T_M\) on every left \(A\)-module is \(A\)-linear and commutes with all module maps. Apply it to the regular module \(A\) and put \(z=T_A(1)\). Left linearity gives \(T_A(a)=az\). Naturality for right multiplication by \(a\) gives \(T_A(a)=za\). Thus \(z\) lies in the *centre* \(Z(A)\), and the module map \(a\mapsto am\) forces \(T_M(m)=zm\) for every \(m\). Conversely each central element gives such an operation. The ability to act consistently on *all* boundary sectors is what points to a centre.

For complexes, compatibility of operations includes homotopies. The ordinary derived centre of an associative algebra is modeled by the Hochschild cochain complex \(C^\bullet(A,A)=\operatorname{RHom}_{A\otimes A^{\mathrm{op}}}(A,A)\). Here \(A^{\mathrm{op}}\) is the algebra with multiplication reversed, so \(A\otimes A^{\mathrm{op}}\) acts on \(A\) by left and right multiplication. The derived Hom computes bimodule maps and their higher extension groups. The geometric centre sought for a chiral boundary must also respect positions, disjoint supports and collisions.

## The mathematical problem in its present form {#the-mathematical-problem-in-its-present-form}

Fix a boundary condition and write \(A_\partial(V)\) for the observables in a boundary open \(V\). In the Gaussian half-space choose a bulk open \(U\) above a thin collar of \(V\), at positive normal separation. Extend a bulk observable \(f\) to the joint region by \(\operatorname{ext}_U\). The quantum collar inclusion \(i_\hbar\) represents a boundary observable \(v\) there, and the projection \(p_\hbar\) returns a boundary observable after multiplication. The resulting action is
\[
 \beta_{U;V}(f)(v)=p_\hbar\bigl(\operatorname{ext}_U(f)\,i_\hbar(v)\bigr),
 \qquad v\in A_\partial(V).
\]
The separated supports make that product available. A reconstruction theorem would identify the bulk observables with the derived centre of the boundary for the specified coherent actions and would preserve factorization. The displayed action in this Gaussian theory supplies a map to study. A general identification with the geometric centre remains open.

There is a corresponding question for boundary conditions themselves. Suppose an interface gives functors \(\Phi,\Psi\) carrying modules across it in opposite directions and these functors are adjoint. Their unit compares a module with the result of crossing and returning, \(\mathrm{id}\to\Psi\Phi\). It is an equivalence on every module precisely when \(\Phi\) is fully faithful, that is, when it preserves all spaces of maps. The counit \(\Phi\Psi\to\mathrm{id}\) tests whether modules on the other side can be recovered this way. Even an equivalence of module categories must still match the state of a specified filling and its absolute scalar or determinant line.

Finally, repeated insertions involve series in more than one separation. For example let \(p\) be a formal separation, \(v\ne0\) a state in \(V\), and \(w_0,w_1,\ldots\) linearly independent states in \(W\). The series \(\sum_{j\ge0}(v\otimes w_j)p^j\) belongs to \((V\otimes W)((p))\). It cannot lie in \(V((p))\otimes W\), since a finite sum of simple tensors uses a common finite-dimensional subspace of \(W\) for all its coefficients. To compare two orders of insertion one must place both operations in a space that contains their actual series. The distinction already appears in the free current calculation. [Chapter 8](08-completions.md)

Even before positions and infinite series enter, one piece of the problem already arises for two ordinary quantum systems. A symmetry acts on each separately. What rule determines its action on their tensor product?

::: figure fig-programme-overview
