# Boundary observables and reconstruction

Two abelian Wilson rays end at \(r\) and \(0\) on the boundary of a Gaussian half-space theory, with charges \(a,-a\), \(a\in\mathbb R\), \(0<r<1\). At current level one their fusion prepares the neutral Heisenberg state
\[
 \Psi_{a,r}=r^{-a^2}\exp\!\left(a\sum_{n>0}\frac{r^n}{n}J_{-n}\right)|0\rangle .
\]
Here \(J_{-n}\) creates a current oscillator of energy \(n\). There is an independent two-dimensional preparation. On the unit disk write the real harmonic field with zero constant mode as \(h+\bar h\), with \(h(z)=\sum_{n>0}Z_nz^n/n\). The disk action makes the \(Z_n\) independent centred complex Gaussian variables of variance \(n\). The Fock isometry sends \(J_{-n_1}\cdots J_{-n_m}|0\rangle\) to \(Z_{n_1}\cdots Z_{n_m}\). Under this identification, the probability density of the ray state is the normalized exponential tilt by \(2a\operatorname{Re} h(r)\). Thus the normalized laws agree on every disk mode. For a cylinder of length \(-\log q\), \(0<q\le1\), the ground-energy-subtracted transfer is \(q^{L_0}\) on holomorphic states, and both preparations give
\[
 \frac{\langle\Psi_{a,r},q^{L_0}\Psi_{a,r}\rangle}{\|\Psi_{a,r}\|^2}
 =\left(\frac{1-r^2}{1-qr^2}\right)^{a^2}.
\]
The collar pairing loses the absolute scalar \(r^{-a^2}\). An absolute amplitude needs the normalization of the three-dimensional filling. The ray regularization, disk source and common Hilbert space are specified in [Chapter 11](11-states-and-lines.md).

Four charge-one rays at level two pose a different reconstruction problem. Their outgoing charge-four primary coefficient is \(\prod_{i<j}(z_i-z_j)^{1/2}\) on a chosen branch. Its local system \(L\) has monodromy \(-1\) about each pair diagonal. A full twist of all four labels has monodromy \((-1)^6=1\). On a three-dimensional slice transverse to the full diagonal, let \(j\) include the distinct configurations and \(i\) the full collision point. The normal link \(K=i^*Rj_*L\) has \(\dim H^2K=\dim H^3K=2\), whereas the links at proper collisions are acyclic. Lines \(W\subset H^2K\) give pairwise nonisomorphic perverse quotients \(j_!L[3]/i_*W\) with identical stalk and costalk ranks. Requiring \(S_4\)-equivariance with positive half-braid \(+i\) leaves the trivial and sign lines. Requiring ordinary inverse image from the coarse quotient leaves the trivial line. Determining which extension a physical collision produces requires its attaching map. [Chapter 4](04-factorization.md)

Let \(X\) be a smooth complex algebraic curve, \(j:X^2\setminus\Delta(X)\hookrightarrow X^2\) the open immersion, and \(\Delta:X\hookrightarrow X^2\) the diagonal. A **Beilinson–Drinfeld chiral algebra** is a right \(\mathcal D_X\)-module \(L\) with a skew-symmetric chiral bracket
\[
 \mu_{\mathrm{ch}}:j_*j^*(L\boxtimes L)\longrightarrow\Delta_*L
 \qquad\text{in right }\mathcal D_{X^2}\text{-modules},
\]
satisfying the Jacobi identity in the ternary chiral operation space. The source allows poles on the diagonal. The target is the direct image as a differential module, including all finite normal derivatives. A chiral unit \(\omega_X\to L\), when specified, acts by the principal-part map.

The **associative chiral algebra** in the ordered word construction is an augmented \(E_1\)-algebra \(A\) for a convolution \(\star\) on configuration complexes. Write \(F_n\) for a word coefficient on \(X^n\). Its collision maps identify extraordinary pullbacks along diagonals that repeat consecutive labels. For \(p+q=n\), let \(j_{p,q}:U_{p,q}\hookrightarrow X^n\) require the first \(p\) points to be distinct from the last \(q\) across the cut. Then
\[
 (F\star G)_n=\bigoplus_{p+q=n}Rj_{p,q*}j_{p,q}^*
            (F_p\boxtimes^{\mathbf L}G_q).
\]
The convolution unit \(k_\varnothing\), with \(k=\mathbb C\), is supported at the empty word. The augmentation \(A\to k_\varnothing\) is an equivalence at arity zero. The factorization condition says that the coproduct of its bar coalgebra \(BA\) induces
\[
 (BA)_{p+q}|_{U_{p,q}}\ \xrightarrow{\ \sim\ }\
 \bigl((BA)_p\boxtimes^{\mathbf L}(BA)_q\bigr)|_{U_{p,q}}
 \qquad(p,q>0).
\]
Multiplication \(A\star A\to A\) is associative with all its coherences. From a Beilinson–Drinfeld bracket one obtains such an object by taking chiral Chevalley chains, restricting to monotone surjections, projecting to consecutive coproducts and applying cobar. A chiral quantum group also requires a coproduct compatible with the tensor at coincident positions and with this convolution. [Chapters 4–5](05-bar-and-coherence.md) and [Chapter 12](12-chiral-quantum-groups.md)

## Reduction must retain the measurements {#reduction-must-retain-the-measurements}

In a Wilsonian effective theory the integration over high-energy modes changes both the action and the observables of the remaining modes. For a finite-dimensional calculation let \(x,y\) be real displacements and take the quadratic action
\[
 S(x,y)=\frac12 ax^2+cxy+\frac12 by^2,
 \qquad b>0,\qquad ab>c^2 .
\]
The real symmetric Hessian has Schur complement \(a-c^2/b>0\), so the form is positive definite. Let \(\hbar>0\) control the scale of fluctuations, and use ordinary Lebesgue measure. At fixed \(x\), the weight remaining after \(y\) is integrated out is
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

The result retains two pieces of information: the effective stiffness \(a-c^2/b\) and the factor \(\sqrt{2\pi\hbar/b}\). The stiffness agrees with \(a\) when \(c=0\), and the factor can equal one at particular parameter values. Setting \(y=0\) would leave \(e^{-ax^2/(2\hbar)}\) and omit these two outputs of the integration. Substituting the conditional mean \(y=-cx/b\) gives the effective quadratic form but does not perform the fluctuation integral.

The same distinction appears when the eliminated variable occurs in an observable. Its conditional moments are
\[
\langle y\rangle_x=-\frac cbx,
\qquad
\langle y^2\rangle_x=\frac{c^2}{b^2}x^2+\frac{\hbar}{b}.
\tag{1.2}
\]
{#eq-gaussian-moments}
The second term in \(\langle y^2\rangle_x\) is the variance. Replacing \(y\) by its mean loses it. Thus an exact reduction includes a rule for transporting observables, not only a new expression for the action.

For a polynomial \(f(x,y)\), write this rule as conditional expectation:
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
An effective theory therefore needs to explain how products are transported. In field theory the analogous correction is a contraction of fields. With many insertions, the corrections must also agree when the same reduction is performed in different orders.

The factor in (1.1) poses another question. It cancels from normalized expectations at a single fixed value of the parameters, but it matters when unnormalized amplitudes are compared, when parameters vary, or when two pieces of a theory are glued. In an infinite-dimensional field theory, the corresponding determinants and their phases need their own definition. A theorem about normalized correlations is consequently different from a theorem about the vacuum amplitude.

::: figure fig-gaussian-reduction

## From products to local operations {#from-products-to-local-operations}

Ordinary multiplication takes two elements of an algebra \(A\) to another element:
\[
m:A\otimes A\longrightarrow A.
\]
For local observables, positions are part of the input. On a complex curve with coordinate \(z\), a field associated with a state \(a\) is written \(Y(a,z)\). It is an operator-valued formal series; its coefficients act on the state space. If \(a\) and \(b\) are inserted at distinct points \(z\) and \(w\), their product can have a pole as \(z\) approaches \(w\).

The basic current example has singular part
\[
J(z)J(w)\sim \frac{\kappa}{(z-w)^2}.
\tag{1.4}
\]
{#eq-current-singularity}
The symbol \(\sim\) here records only the terms singular at the diagonal \(z=w\); it does not assert equality of the complete product with the displayed function. The number \(\kappa\) is the central coefficient of this current algebra.

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
They describe the same rational function on different domains. In formal algebra, the domain is replaced by a prescribed order of Laurent expansion. Changing that order is a mathematical operation; it cannot be suppressed by writing both series as the same completed tensor.

::: figure fig-local-expansions

For \(n\) insertions, the strata of \(X^n\) are indexed by coincidence partitions. The convolution must specify which partitions and which block decompositions it uses. On a fixed word of length three there are two nontrivial consecutive cuts, \(1|23\) and \(12|3\). At \((x,y,x)\), \(x\ne y\), neither cut separates its two blocks. In the full ordered collision atlas the decomposition \(\{1,3\}|\{2\}\) does separate them. Thus the two convolutions already have different separating opens at three labels. [Chapters 4–5](04-factorization.md#ordered-cut-geometry)

## Why representations and centres enter {#why-representations-and-centres-enter}

A local algebra is also tested by the objects on which it acts. An ordinary representation of an algebra \(A\) is a vector space \(M\) with an action \(A\otimes M\to M\). In the field-theoretic setting, boundary conditions and line operators lead to corresponding module constructions. Combining two such objects requires more than knowing the action on each separately.

For an ordinary bialgebra \(H\), a coproduct \(\Delta:H\to H\otimes H\) supplies the diagonal action on \(M\otimes N\):
\[
h\cdot(m\otimes n)
=\sum h_{(1)}m\otimes h_{(2)}n,
\qquad
\Delta(h)=\sum h_{(1)}\otimes h_{(2)}.
\tag{1.6}
\]
{#eq-tensor-action}
The compatibility between multiplication and coproduct makes this an action. Coassociativity controls its associativity on three modules. Maps interchanging the factors require additional structure: cocommutativity supplies the usual flip, while a more general exchange requires a braiding and its compatibility equations. A chiral quantum group must solve the corresponding problem with local position-dependent operations.

For an ordinary associative algebra \(A\), an element of \(Z(A)\) acts naturally on every left \(A\)-module. Its derived analogue is the Hochschild cochain complex \(C^\bullet(A,A)=\operatorname{RHom}_{A\otimes A^{\mathrm{op}}}(A,A)\). A bulk action on a chiral boundary has additional support and factorization requirements. The proposed bulk-to-centre map must identify the coherent operations on the specified boundary modules. A separate functor \(F:\mathcal C_{\mathrm{bulk}}\to\mathcal C_\partial\) between module categories is fully faithful if \(\operatorname{Map}(M,N)\to\operatorname{Map}(FM,FN)\) is an equivalence for every pair. To identify the categories one must in addition characterize its essential image.

## The mathematical problem in its present form {#the-mathematical-problem-in-its-present-form}

Fix a boundary condition with boundary algebra \(A_\partial\). In the Gaussian half-space, let \(V\) be a boundary open and \(U\) a bulk open above its collar. With quantum collar inclusion \(i_\hbar\) and projection \(p_\hbar\), an observable \(f\) supported in \(U\) acts by
\[
 \beta_{U;V}(f)(v)=p_\hbar\bigl(\operatorname{ext}_U(f)\,i_\hbar(v)\bigr),
 \qquad v\in A_\partial(V).
\]
The multiplication uses disjoint supports in the normal direction. A bulk-to-boundary reconstruction theorem would identify the bulk observables with the derived centre representing the specified coherent actions, compatibly with factorization. For two boundary conditions an interface gives candidate functors \(\Phi\dashv\Psi\) on their module categories. The unit \(\mathrm{id}\to\Psi\Phi\) tests full faithfulness of \(\Phi\), and the counit \(\Phi\Psi\to\mathrm{id}\) tests reconstruction on the other side. In either setting, identifying the state prepared by a filling requires the image of that state under the comparison, including its scalar or determinant line.

The disk computation tests a specified state and all its oscillator marginals. The four-point computation exhibits the attaching datum still required of an extension. Iterated fusion introduces a third issue, the choice of tensor product for series in several separations. For instance, an element of \(V((p))\otimes W\) has its \(W\)-coefficients in a finite-dimensional subspace of \(W\), whereas \((V\otimes W)((p))\) imposes no common finite-dimensional bound. These two spaces can therefore give different domains for the next insertion. [Chapter 8](08-completions.md)

::: figure fig-programme-overview
