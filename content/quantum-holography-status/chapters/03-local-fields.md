# Local fields on a curve

To measure the charge of a line ending on a surface, place its endpoint at \(z=0\) and integrate the current one-form \(J(z)\,dz\) on a small positively oriented circle. Divide the integral by \(2\pi i\). Only a term \(Q\,dz/z\) contributes, so an endpoint state \(v\) of charge \(a\) gives \(Qv=av\). We can use the same circle to ask another question. Multiply the current by \(z^n\) before integrating. Now it is the coefficient of \(z^{-n-1}\) that acts on \(v\). The field thus supplies a whole family of operations on a state.

Two contour operations can be composed by nesting their circles. The inner operation prepares the input for the outer one. Interchanging which circle lies inside compares two orders of acting, and their difference can be calculated from the pole where the insertions meet. A simple pole returns the value of a test function there. A double pole returns its derivative. To express both tests on algebraic states, we begin with the coefficient selected by a single circle.

## Fields and their modes {#fields-and-modes}

On the vacuum all the positive modes vanish. The same statement fails already on a one-quantum state \(p_r\). For the neutral current at level one, \(J_n=n\partial_{p_n}\) and \(J_{-n}\) multiplies by \(p_n\) for \(n>0\). Thus \(J_rp_r=r\mathbf1\), where \(\mathbf1=1\) is the vacuum, and the other positive modes kill \(p_r\). Its current has a pole of order \(r+1\). Increasing \(r\) makes this pole arbitrarily high, although the pole order on any one polynomial is finite. This is the distinction built into the definition of a field.

**Definition (field and modes).** Let \(V\) be a complex vector space of states. A field on \(V\) is a series
\[
\begin{gathered}
A(z)=\sum_{n\in\mathbb Z}A_nz^{-n-1},\\
A_n\in\operatorname{End}_{\mathbb C}(V),
\end{gathered}
\tag{3.1}
\]
such that for each \(v\in V\) there exists a bound beyond which every \(A_n v\) is zero. The operators \(A_n\) are its *modes*. The bound is allowed to change with the input, as it does for \(p_r\). Consequently \(A(z)v\) belongs to \(V((z))\), the space of Laurent series with finitely many negative powers and arbitrary nonnegative powers, all with coefficients in \(V\).

A mode is an operation on an input vector. For example, multiplying \(J(z)p_r\) by \(z^r\) makes its singular term \(r\mathbf1 z^{-1}\), so its residue is the vacuum vector multiplied by \(r\). In general
\[
A_n v=\operatorname{Res}_{z=0}z^n A(z)v\,dz.
\]
The formal residue in this formula takes the coefficient multiplying \(z^{-1}dz\). It returns the vector \(A_n v\) for every input \(v\) in the stated domain. To obtain a scalar, choose a linear functional \(\ell\) on \(V\). If \(\ell(A(z)v)\) converges to a meromorphic function near the origin, the integral of \(z^n\ell(A(z)v)\,dz\) on a small positively oriented circle, divided by \(2\pi i\), gives \(\ell(A_n v)\).

What can one subtract when the two circles change order? Apply \(B(w)\) to \(v\) first. Its series has a lower bound in \(w\). Each coefficient is a new state to which \(A(z)\) can be applied, with its own lower bound in \(z\). The result lies in \(V((z))((w))\). Reversing the operations gives \(V((w))((z))\). Nevertheless at \(z^{-m-1}w^{-n-1}\) the two coefficients are simply \(A_mB_nv\) and \(B_nA_mv\). Subtract them there for every \(m,n\). The resulting doubly indexed array is a *formal distribution*. Multiplication by a polynomial such as \((z-w)^N\) takes finite linear combinations of these coefficients.

**Definition (locality).** Two even fields \(A,B\) are local if there is an integer \(N\geq0\) such that
\[
(z-w)^N[A(z),B(w)]=0.
\tag{3.2}
\]
Here the bracket is the commutator \(A(z)B(w)-B(w)A(z)\). For fields of definite parity one uses the graded commutator, inserting the sign \((-1)^{|A||B|}\) on interchanging them. The integer \(N\) may depend on the field pair and must work on *every* input. Locality is an identity of distributions. To give a value to the product at the collision itself, its singular terms must still be treated.

For example, write \(\iota_{z,w}\) for expansion in nonnegative powers of \(w/z\), and \(\iota_{w,z}\) for expansion in nonnegative powers of \(z/w\). Then
\[
\iota_{z,w}\frac1{(z-w)^2}
=\sum_{r\geq0}(r+1)w^rz^{-r-2},
\qquad
\iota_{w,z}\frac1{(z-w)^2}
=\sum_{r\geq0}(r+1)z^rw^{-r-2}.
\tag{3.3}
\]
To see what distinguishes the two expansions, start with the simple pole. Expanding \(1/(z-w)\) in \(w/z\) gives the monomials \(z^{-m-1}w^m\) for \(m\ge0\). Expanding it as \(-w^{-1}(1-z/w)^{-1}\) gives minus the same monomials for \(m<0\). In the first expansion minus the second, each integer label occurs once with a plus sign. The resulting formal delta distribution is
\[
 \delta(z,w)=\sum_{m\in\mathbb Z}z^{-m-1}w^m.
\]
Its name comes from the test \(f(z)=z^q\). Only \(m=q\) survives the \(z\)-residue, giving \(w^q\). By linearity \(\operatorname{Res}_z f(z)\delta(z,w)\,dz=f(w)\) for every Laurent polynomial. Shifting the index shows \((z-w)\delta=0\). Differentiate the two simple-pole expansions in \(w\). They give the two double-pole expansions (3.3), whose difference \(\partial_w\delta\) now returns \(f'(w)\). The tests \(1\) and \(z\) give zero and one. Differentiating \((z-w)\delta=0\) yields \((z-w)\partial_w\delta=\delta\), so a second factor of \(z-w\) kills the double-pole difference. This is locality of order two.

### Two contour tests at the diagonal {#ch03-diagonal-current-term}

Put \(t=z-w\). After \(t\) is inverted, the two expansions of \(t^{-2}\) agree, since multiplication by \(t^2\) sends each of them to \(1\). A contour that crosses the insertion at \(w\) can still distinguish them. Give its integrand the weight \(t\). Multiplying the difference by this weight gives \(\delta(z,w)\), so
\[
 \operatorname{Res}_z t\,\partial_w\delta(z,w)\,dz=1 .
\]
The weight itself vanishes at the collision. Its derivative in the incoming coordinate \(z\) is what the contour detects.

::: lemma {#ch03-order-two-distribution title="An order-two distribution on the diagonal"}
For a formal distribution \(D(z,w)\) killed by \(t^2\), put
\[
 \begin{gathered}
 A(w)=\operatorname{Res}_z D\,dz,\\
 B(w)=\operatorname{Res}_z tD\,dz .
 \end{gathered}
\]
Then \(D=A(w)\delta(z,w)+B(w)\partial_w\delta(z,w)\).
:::

::: proof {#ch03-order-two-distribution-proof}
For a Laurent polynomial \(f\), the difference \(f(z)-f(w)-t f'(w)\) is divisible by \(t^2\) in \(\mathbb C[z^{\pm1},w^{\pm1}]\). Hence testing \(D\) against \(f(z)\) gives \(f(w)A(w)+f'(w)B(w)\). The stated sum of delta distributions gives exactly those residues. Testing with \(f(z)=z^m\) for every integer \(m\) reads every coefficient, proving equality. ∎
:::

Restriction to \(t\ne0\) sends both delta terms to zero. For the free current at level \(\kappa\), the commutator has \(A=0\) and \(B=\kappa\,\mathrm{id}\). Levels one and two thus have the same zero commutator on separated points, while the weighted contour returns the identity in one case and twice the identity in the other. The ordered vacuum two-point functions distinguish these levels through the coefficient of \(t^{-2}\). Specifying the ordered field products fixes their difference. Restricting the commutator alone forgets it. [The free-current contraction](#heisenberg-current) · [Extensions from distinct points](04-factorization.md#collision-supported-data) · [Kac, Theorem 1.2](https://arxiv.org/pdf/1512.00821#page=7)

## A vertex algebra retains states and local products {#vertex-algebra}

So far a field has been an operator applied to a specified state. Acting on the vacuum also lets it *create* a state. For example, \(J(z)\mathbf1=p_1+p_2z+p_3z^2+\cdots\), whose value at the origin is the one-quantum state \(p_1\). A vertex algebra makes this relation part of the structure for every state. It specifies a field that prepares that state from the vacuum and tells us how its insertion varies with position.

**Definition (vertex algebra).** In the even convention used here, a vertex algebra consists of a vector space \(V\), a vacuum vector \(\mathbf1\), a translation operator \(T:V\to V\), and a linear assignment
\[
a\longmapsto Y(a,z)=\sum_{n\in\mathbb Z}a_{(n)}z^{-n-1}
\]
of a field to every state \(a\). They satisfy the vacuum and creation identities
\[
Y(\mathbf1,z)=\operatorname{id}_V,
\qquad
Y(a,z)\mathbf1\in a+zV[[z]],
\tag{3.4}
\]
the translation identities
\[
T\mathbf1=0,
\qquad
[T,Y(a,z)]=\partial_zY(a,z)=Y(Ta,z),
\tag{3.5}
\]
and locality for each pair \(Y(a,z),Y(b,w)\). Apply these identities to \(v(z)=Y(a,z)\mathbf1\). Creation gives the initial condition \(v(0)=a\). Translation gives the differential equation \(\partial_z v(z)=Tv(z)\), since \(T\mathbf1=0\). Starting from \(v_0=a\), the successive coefficients satisfy \((r+1)v_{r+1}=Tv_r\). Thus
\[
Y(a,z)\mathbf1=e^{zT}a,
\qquad a=a_{(-1)}\mathbf1.
\]
Taking the constant term recovers the state \(a\) from its field on the vacuum. To turn a vector after several insertions into a scalar amplitude one must also specify a functional or pairing.

Apply the field of \(a\) to a second state \(b\) at separation \(t=z-w\). The coefficient of \(t^{-n-1}\) is itself a state, \(a_{(n)}b\). At the point \(w\) its field \(Y(a_{(n)}b,w)\) acts on any further input. This is how the state products appear as coefficients of the operator product expansion. Its singular terms are
\[
Y(a,z)Y(b,w)
\sim\sum_{n\geq0}
\frac{Y(a_{(n)}b,w)}{(z-w)^{n+1}}.
\tag{3.6}
\]
The symbol \(\sim\) retains the operator-valued pole coefficients in the order \(z,w\). Their number is finite for fixed \(a,b\). In the state series \(Y(a,t)b\) subtract its own polar part \(\sum_{n\ge0}(a_{(n)}b)t^{-n-1}\). The constant term of the remainder is \(a_{(-1)}b\), the state of the *normally ordered product*. Even \(Y(\mathbf1,t)b=b\) illustrates the distinction. Its singular part vanishes and its constant term is \(b\).

To read several singular coefficients with one test, pair \(Y(a,t)b\) with \(e^{\lambda t}\,dt\) and take the residue in \(t\). A term \(a_{(n)}b\,t^{-n-1}\) contributes only when it meets the term \(\lambda^nt^n/n!\) of the exponential. Regular powers of \(t\) cannot contribute a residue to this test. The resulting polynomial in the formal variable \(\lambda\) is
\[
[a_\lambda b]=\sum_{n\geq0}\frac{\lambda^n}{n!}a_{(n)}b.
\tag{3.7}
\]
This *\(\lambda\)-bracket* collects the poles with the normalization just derived. For the vacuum field it is zero for every \(b\), although the regular product returns \(b\). The geometric chiral bracket permits Laurent multipliers, so it can also recover that regular coefficient. Beilinson and Drinfeld identify vertex algebras with translation-equivariant chiral algebras on the affine line in *Chiral Algebras*, §0.15. Their Theorem 3.5.10 relates the chiral bracket to the full operator product. [The geometric operation and Laurent multipliers](04-factorization.md#lie-and-operator-product)

## The free current as a complete calculation {#heisenberg-current}

The exchange in Chapter 1 used the number obtained by commuting the removal of a quantum with its creation. Does that number also determine the pole in the product of two fields? Fix a complex level \(\kappa\). For a single abelian current the algebraic mode test consists of computing the commutator in the Heisenberg relations
\[
[J_m,J_n]=\kappa m\,\delta_{m+n,0}\operatorname{id}.
\tag{3.8}
\]
Here \(\delta_{r,0}\) is \(1\) for \(r=0\) and \(0\) otherwise. A vacuum representation with zero charge is
\[
V=\mathbb C[p_1,p_2,p_3,\ldots],
\qquad \mathbf1=1,
\]
where
\[
J_{-n}=p_n\cdot(-),\qquad
J_n=\kappa n\frac{\partial}{\partial p_n}
\quad(n>0),
\qquad J_0=0.
\tag{3.9}
\]
The domain is the algebraic polynomial space. A polynomial \(v\) involves only finitely many variables, say \(p_1,\ldots,p_r\). Then \(J_n v=0\) for \(n>r\), giving exactly the state-dependent bound in (3.1). The generating series
\[
J(z)=\sum_{n\in\mathbb Z}J_nz^{-n-1}
\]
is therefore a field. On the vacuum, \(J_2J_{-2}\mathbf1=2\kappa\mathbf1\) and \(J_{-2}J_2\mathbf1=0\). On every polynomial the identity \(\partial_{p_m}(p_nv)-p_n\partial_{p_m}v=\delta_{mn}v\) proves (3.8). At \(\kappa=1\) adjointness for the occupation inner product supplies the [two-harmonic measurement](01-physical-questions.md#ch01-two-preparations). Arbitrary complex \(\kappa\) gives an algebraic action, with no positivity assumption.

To compute a product of two currents, separate the modes that create a quantum from those that can remove one. In the neutral representation the zero mode vanishes. We include it in the second sum and write
\[
J_-(z)=\sum_{n<0}J_nz^{-n-1},
\qquad J_+(z)=\sum_{n\geq0}J_nz^{-n-1}.
\]
To evaluate the product on the vacuum, put the modes which annihilate it on the right. Moving \(J_+(z)\) past \(J(w)\) leaves a commutator. The expression with that interchange already made is the **normally ordered product**,
\[
:J(z)J(w):=J_-(z)J(w)+J(w)J_+(z).
\]
**Proposition (free-current contraction).** In the neutral polynomial representation at level \(\kappa\), the product with \(J(w)\) acting first is
\[
\begin{aligned}
J(z)J(w)
&=:J(z)J(w):+[J_+(z),J(w)]\\
&=:J(z)J(w):+
\kappa\sum_{n\geq1}n z^{-n-1}w^{n-1}\\
&=:J(z)J(w):+
\kappa\,\iota_{z,w}\frac1{(z-w)^2}.
\end{aligned}
\tag{3.10}
\]

*Proof.* Moving \(J_+(z)\) to the right leaves its commutator with \(J(w)\). Only \(J_n\) and \(J_{-n}\) with \(n>0\) contribute. Their commutators give the scalar \(\kappa n\), so the remainder is \(\kappa z^{-2}\sum_{n\ge1}n(w/z)^{n-1}\). The differentiated geometric series gives the stated double pole. Reversing the order of the fields gives the same normally ordered term because the creation modes commute among themselves and so do the annihilation modes. The reversed contraction gives the other expansion of the pole, in powers of \(z/w\). Subtracting it from the first gives \(\kappa\partial_w\delta(z,w)\,\mathrm{id}\). ∎

Conversely, testing this difference first with \(z^m\) gives \(\kappa m w^{m-1}\,\mathrm{id}\). Testing next with \(w^n\) gives \(\kappa m\delta_{m+n,0}\,\mathrm{id}\), recovering the commutator including its sign. In state notation \(j=p_1\) has \(Y(j,z)=J(z)\), so \(j_{(1)}j=\kappa\mathbf1\) and the other singular products vanish. Thus \([j_\lambda j]=\kappa\lambda\mathbf1\).

Define \(T\) on the polynomial algebra as the derivation
\[
Tp_n=n p_{n+1}.
\]
This definition gives \([T,J_n]=-nJ_{n-1}\) and hence \([T,J(z)]=\partial_zJ(z)\). It identifies the two preparations of energy two as *different fields*. The state \(p_2=Tp_1\) is made by translating the first current, whereas \(p_1^2\) is made by its regular product with itself. Their fields are
\[
Y(p_2,z)=\partial_zJ(z),
\qquad Y(p_1^2,z)=:J(z)^2:.
\]
Normal products and derivatives of \(J\) similarly generate the fields of all polynomial states. This is the rank-one Heisenberg vertex algebra at level \(\kappa\). At nonzero level, taking the regular product of states can fail associativity even on this polynomial space. A third current tests this directly.

**Example (the normal-product associator).** The normally ordered square prepares \(p_1^2\). To compute \((j_{(-1)}j)_{(-1)}j\), take the constant term of \(:J(z)^2:\) on \(j=p_1\). The power from two modes \(J_m,J_n\) is \(z^{-m-n-2}\), so \(m+n=-2\). The two creation indices must both be \(-1\) when both are negative. If one index is positive, only \(J_1\) can remove the quantum in \(p_1\), and both orders \((-3,1),(1,-3)\) occur. The zero mode vanishes. Moving \(J_1\) to the right gives \(J_1j=\kappa\mathbf1\) in each mixed term. Reversing the *grouping* instead applies the constant mode of \(J(z)\), multiplication by \(p_1\), to \(p_1^2\). The two answers are
\[
(j_{(-1)}j)_{(-1)}j=p_1^3+2\kappa p_3,\qquad
j_{(-1)}(j_{(-1)}j)=p_1^3.
\]
The associator is \(2\kappa J_{-3}\mathbf1=\kappa T^2j\). At every nonzero level it distinguishes the field product from ordinary polynomial multiplication.

To read the pole as a scalar, specify how the experiment ends. Prepare the vacuum, apply the two currents and extract the constant term in the occupation variables \(p_n\). Denote this functional by \(\langle\mathbf1^*,-\rangle\), normalized to one on \(\mathbf1\). In the normally ordered term there is either an annihilator at the right, which kills the vacuum, or a product of creators, which has zero constant term. This leaves
\[
\langle\mathbf1^*,J(z)J(w)\mathbf1\rangle
=\kappa\,\iota_{z,w}(z-w)^{-2}.
\tag{3.11}
\]
This particular two-point coefficient is the expansion of a meromorphic function. Its existence follows here from the explicit vacuum representation and functional. A different representation, charge or functional is additional data, even when the local mode relations remain the same.

### A charge measured by a contour {#ch03-charged-current-contour}

The double pole of two currents measures \(k=\kappa\). To read a charge, keep this nonzero numerical level fixed and prepare the endpoint of a rank-one Wilson ray of charge \(a\) in Gaussian abelian Chern–Simons theory. The source couples to the integral of the gauge one-form along the ray oriented into the half-space. Take the endpoint at \(z=0\), use a ray vertical near the boundary current tests and surround it by a positively oriented contour. The contraction of the source with a current gives \(a\,dz/z\). Its residue after weighting by \(z^n\) is \(a\) for \(n=0\) and zero otherwise. Thus only the zero mode of the vacuum action shifts.

For the vertical ray the cohomology on finite sums of angular weights is the charged Fock module
\[
 \begin{gathered}
 \mathcal F_a=\mathbb C[p_1,p_2,\ldots]|a\rangle,\qquad J_0=a,\\
 J_{-n}=p_n,\qquad J_n=kn\partial_{p_n}\quad(n>0).
 \end{gathered}
\]
The vector \(|a\rangle\) has no oscillator excitations. Excite the second harmonic once to prepare \(p_2|a\rangle\). The unweighted contour acts by \(J_0\), so it sends this state to \(a\,p_2|a\rangle\). Its charge eigenvalue is the same \(a\) as on \(|a\rangle\). Weighting the contour by \(z^2\) applies \(J_2\) instead. It removes the excitation and gives \(2k|a\rangle\). The coefficient \(2k\) thus measures the oscillator response at the fixed level \(k\).

The double-pole relation is the same in every charge sector. The unweighted contour distinguishes their charges. The endpoint identification on the sector of finite angular weights is Theorem 2.2 of [Chern–Simons observables, charged endpoints and chiral fusion](12-chiral-quantum-groups.md#ref-ch12-cq10).

For endpoints of charges \(a,b\) at distinct \(z,w\), an enclosing contour adds the residues and reads \(a+b\) at every separation. To test the separation, prepare two oscillator-free inputs and project onto the oscillator-free outgoing state, taking value one on \(|a+b\rangle\). Use the planar Cauchy propagator, disjoint radial regularizations, the outgoing mutual subtraction and the parallel-copy prescription for self-contractions. The mutual contraction gives the coefficient \((z-w)^{ab/k}\) of the endpoint fusion operation, with the real logarithm for \(z>w\) and common-path continuation from that chamber. With the individual frames fixed, continuing the incoming separation once counterclockwise multiplies this coefficient by \(e^{2\pi iab/k}\). The projected operation is a functional on the state line, so the same winding along the upward rays multiplies the transported state by the inverse factor \(e^{-2\pi iab/k}\). For unit charges at level three the operation and state acquire \(e^{2\pi i/3}\) and \(e^{-2\pi i/3}\), respectively. At level two both factors are \(-1\). Multiplying the operation coefficients for all six pairs gives the separated coefficient for four rays. To take it through a collision still requires the attaching map. [Four charged rays and their possible attachments](04-factorization.md#ch04-gaussian-collision)

## Nonabelian currents and the information in a pole {#affine-currents}

In the abelian example an unweighted contour kills the double pole, because the derivative of its constant weight is zero. For a nonabelian symmetry, even unweighted contour operations can have a commutator. Let \(\mathfrak g\) be a finite-dimensional complex Lie algebra, \((x,y)\) an invariant symmetric bilinear form on it, and \(\ell\in\mathbb C\) a level. For a current with label \(x\) let \(J^x_m\) be its \(m\)-th mode, linear in \(x\). Its affine commutator has two terms,
\[
[J^x_m,J^y_n]
=J^{[x,y]}_{m+n}
+\ell m(x,y)\delta_{m+n,0}\operatorname{id}.
\tag{3.12}
\]
Invariance means \(([x,y],z)=(x,[y,z])\). It is the compatibility required for the central term to satisfy the Jacobi identity. The associated current expansion is
\[
J^x(z)J^y(w)
\sim\frac{J^{[x,y]}(w)}{z-w}
+\frac{\ell(x,y)}{(z-w)^2}.
\tag{3.13}
\]
Changing the current labels separates the two pole coefficients in this model. Take \(\mathfrak{sl}_2\) with \((x,y)=\operatorname{tr}(xy)\), \(H=\operatorname{diag}(1,-1)\), and \(E\) the matrix with a single nonzero entry \(E_{12}=1\). Then \([H,E]=2E\) and \(\operatorname{tr}(HE)=0\), leaving just \(2J^E(w)/(z-w)\). Take \(H\) twice instead. The Lie bracket vanishes, while \(\operatorname{tr}(H^2)=2\), leaving \(2\ell/(z-w)^2\). Thus the two ordered contour tests of (3.13) can recover separately the bracket and the level.

To read the mode commutator, take the difference of the two radial expansions. Its simple pole gives \(\delta(z,w)\) and its double pole gives \(\partial_w\delta(z,w)\). Testing with \(z^m\) returns \(w^mJ^{[x,y]}(w)\) in the first term and \(\ell(x,y)m w^{m-1}\) in the second. The residue against \(w^n\) is respectively \(J^{[x,y]}_{m+n}\) and \(\ell m(x,y)\delta_{m+n,0}\). This derives (3.12) with its sign and both mode indices.

What happens if we retain only the creation modes? For \(m,n<0\) the central term in (3.12) vanishes. Before imposing vacuum relations those modes have enveloping algebra \(N=U(t^{-1}\mathfrak g[t^{-1}])\), where \(xt^m\) denotes the mode with index \(m\) and label \(x\). At every level the augmentation \(N\to\mathbb C\) sends \(1\) to one and all generators to zero. Thus the self-extension groups \(\operatorname{Ext}_N^\bullet(\mathbb C,\mathbb C)\) are formed from the same algebra and the same scalar module at every level. Restoring a positive mode recovers the missing scalar. Indeed \(J^H_1 J^H_{-1}\mathbf1=2\ell\mathbf1\) in the vacuum representation, with the factor two fixed by the trace form.

There is a further loss if a relation between *states* is read as a relation between individual creation operators. At level one use the Frenkel–Kac lattice realization \(L_1(\mathfrak{sl}_2)=V_{\mathbb Z\alpha}\), with \((\alpha,\alpha)=2\). Its oscillator-free states \(|m\alpha\rangle\) have lattice momentum \(m\alpha\). Write \(h_m\) for the Cartan modes. With cocycle \(\epsilon(m\alpha,n\alpha)=(-1)^{mn}\), put \(e(z)=Y(|\alpha\rangle,z)\), \(f(z)=-Y(|-\alpha\rangle,z)\). Then \([e_m,f_n]=h_{m+n}+m\delta_{m+n,0}\,\mathrm{id}\). Acting on \(\mathbf1\), \(e_{-1}\) creates \(|\alpha\rangle\). On that state \(e(z)|\alpha\rangle\) begins at \(z^2\), so \(e_{-1}^2\mathbf1=0\). We can test whether \(e_{-1}^2\) is the zero operator by applying it to \(f_{-1}\mathbf1\). For this calculation we need the first coefficients of
\[
e(z)\mathbf1=\exp\!\left(\sum_{m>0}h_{-m}z^m/m\right)|\alpha\rangle .
\]
Its \(z^2\) coefficient is \(e_{-3}\mathbf1=(h_{-2}+h_{-1}^2)|\alpha\rangle/2\). Commute \(f_{-1}\) through \(e_{-1}^2\) using \([e_{-1},f_{-1}]=h_{-2}\) and \([h_{-2},e_{-1}]=2e_{-3}\). The term \(f_{-1}e_{-1}^2\mathbf1\) vanishes, leaving
\[
e_{-1}^2f_{-1}\mathbf1
=(2h_{-2}e_{-1}-2e_{-3})\mathbf1
=(h_{-2}-h_{-1}^2)|\alpha\rangle .
\]
Use the Hermitian form with \(\langle\alpha|\alpha\rangle=1\) and \(h_m^\dagger=h_{-m}\). Since \([h_m,h_n]=2m\delta_{m+n,0}\,\mathrm{id}\), the two oscillator states are orthogonal with squared norms \(4\) and \(2!\,2^2=8\). The resulting vector has squared norm \(12\). The two-sided associative relation \(e_{-1}^2=0\) would kill it.

The field of the zero state \(e_{-1}^2\mathbf1\) must vanish on *every* input. Its constant coefficient is the \((-1)\)-mode of \(:e(z)^2:\). As in the abelian square, the two indices sum to \(-2\). Besides \((-1,-1)\) there are the two orders of \((m,-m-2)\) for each \(m\ge0\). Normal ordering therefore gives \(e_{-1}^2+2\sum_{m\ge0}e_{-m-2}e_m\). Test the correction on \(f_{-1}\mathbf1\). Only \(e_0\) and \(e_1\) survive on the right, giving \(h_{-1}\mathbf1\) and \(\mathbf1\), respectively. The correction is \(2(e_{-2}h_{-1}+e_{-3})\mathbf1\). Commuting \(h_{-1}\) to the left and inserting the coefficients of \(z,z^2\) in the vacuum expansion gives \((h_{-1}^2-h_{-2})|\alpha\rangle\). It cancels the vector of squared norm \(12\) exactly. The full field relation thus holds on the input where the bare square failed.

The sum just used is finite on the input because sufficiently high positive modes annihilate it. The appropriate condition for a general input has a name.

**Definition (smooth current module).** An affine current module \(M\) is smooth if, for every \(v\in M\), there is an integer \(N(v)\) such that \(J^x_n v=0\) for all \(n\ge N(v)\) and all \(x\in\mathfrak g\). Suppose the field bound (3.1) holds on \(v\) for each current in a basis of the finite-dimensional Lie algebra \(\mathfrak g\). Take the largest of those finitely many bounds. Since \(J^x_n\) depends linearly on \(x\), this one bound works for every label on \(v\). This gives the finite negative Laurent tail required by (3.1).

The chosen domain matters even at level one. Complete the neutral polynomials in *all* the harmonics with the occupation inner product of Chapter 1. The partial sums \(v_R=\sum_{r=1}^R2^{-r}p_r\) converge in norm to a state \(v\), since the \(p_r\) are orthogonal and \(\sum_{r>0}r4^{-r}=4/9\). For each fixed \(n>0\), \(J_n v_R=n2^{-n}\mathbf1\) once \(R\ge n\). If we use these individual limits to define \(J_n v\), then \(J_n v\ne0\) for every positive \(n\). There is no cutoff \(N(v)\), even though each fixed mode has a limit on this sequence. The resulting series has infinitely many negative powers and so fails the field condition on \(v\). [Smooth affine modules](06-duality-and-induction.md#ch06-affine-currents-and-the-algebra-acting-on-their-resolution) · [Laurent bounds and completion](08-completions.md#ch08-laurent-series-with-algebraic-coefficients)

## Differentiation and a change of coordinates {#differential-modules}

Change from \(z\) to \(u=2z\). Then \(dz/z=du/u\), whereas \(dz/z^2=2\,du/u^2\). Why does the residue of a one-form survive an arbitrary change of local coordinate? At the marked point such a change has \(u(0)=0\) and nonzero linear coefficient. Write its inverse as \(z=u h(u)\), with \(h(0)\ne0\). Then \(dz/z=du/u+(h'(u)/h(u))\,du\), and the second term is regular. Every other Laurent monomial \(z^q\,dz\), \(q\ne-1\), is the differential of \(z^{q+1}/(q+1)\). A Laurent derivative has zero residue in either coordinate. Thus only the coefficient of \(dz/z\) contributes in the new coordinate. To move the fields themselves between coordinate disks we must also specify their transformation law and how differentiation acts on a field multiplied by a function. On a smooth complex algebraic curve \(X\) write \(\mathcal O_X\) for the regular functions and \(\mathcal D_X\) for their sheaf of algebraic differential operators. In a coordinate the basic relation is
\[
[\partial_z,z]=1.
\]
A left **differential module**, or left \(\mathcal D_X\)-module, is an \(\mathcal O_X\)-module \(M\) with differentiation obeying the Leibniz rule
\[
\nabla_{\partial_z}(fm)=f'm+f\nabla_{\partial_z}m.
\tag{3.14}
\]
For a vector bundle this is a connection. Differential modules may also be infinite-dimensional or supported on a subvariety, so they include more than vector bundles with connection.

On the coordinate line, a vector space with an operator \(T\) gives the example \(M=\mathcal O_X\otimes V\) with
\[
\nabla_{\partial_z}(f\otimes v)=f'\otimes v+f\otimes Tv.
\]
Indeed a constant section \(1\otimes v\) has derivative \(1\otimes Tv\), and the first term is forced on \(f\otimes v\) by the Leibniz rule. To glue a vertex algebra on arbitrary curves we need in addition the action of changes of formal coordinate. For example, suppose a conformal structure decomposes the state space as a direct sum of eigenspaces of \(L_0\) of nonnegative integral weights. A change of formal coordinate at the origin has a nonzero linear coefficient. First separate this scaling, which acts through the weights. The remaining change is tangent to the identity, with linear term \(z\). Its infinitesimal generators involve only Virasoro modes \(L_m\) with \(m\ge1\). Each lowers weight by at least one. On a state of greatest weight \(d\), every product of more than \(d\) such modes vanishes, so their exponential series terminates. Translation equivariance alone gives the construction on the affine line.

Chiral operations are conventionally written for right differential modules. If \(M\) is a left module, its corresponding right module is
\[
M^{\mathrm r}=\omega_X\otimes_{\mathcal O_X}M,
\]
where \(\omega_X\) is the line bundle of one-forms. In a coordinate,
\[
(dz\otimes m)\cdot\partial_z=-dz\otimes\nabla_{\partial_z}m.
\tag{3.15}
\]
For \(M=\mathcal O_X\) with its ordinary derivative, \((f\,dz)\cdot\partial_z=-f'\,dz\). The sign is forced by integration by parts. For Laurent polynomials \(f,g\), the residue of the exact form \(d(fg)\) vanishes, giving \(\operatorname{Res}f\,dg=-\operatorname{Res}g\,df\). Tensoring with \(\omega_X\) is the equivalence between left and right differential modules. It requires no choice of dual state space.

Now fix \(w\) and write \(t=z-w\). The multiplier in a local residue can be chosen just as it was for the first contour in this chapter. Thus \(a_{(n)}b=\operatorname{Res}_{t=0}t^nY(a,t)b\,dt\). For \(j=p_1\), multiplying by \(t\) selects the double-pole coefficient \(j_{(1)}j=\kappa\mathbf1\). Multiplying by \(t^{-1}\) selects its regular coefficient \(j_{(-1)}j=p_1^2\). A Laurent multiplier therefore recovers even a product invisible to all regular tests.

For a vertex algebra with the required coordinate-change action let \(\mathcal V^{\mathrm r}\) be its associated right differential module. The two-point chiral operation takes values in \(\Delta_*\mathcal V^{\mathrm r}\), with \(\Delta(w)=(w,w)\) in \(X^2\). Its support is the common point, but keeping \(w\) fixed and varying \(t\) probes a direction normal to the diagonal. On a regular test the double pole gives \(\kappa f'(0)\). Thus at nonzero level \(1\) and \(1+t\) give different outputs despite agreeing at \(t=0\). In coordinates this is the derivative term in the two contour tests. With several insertions one must also specify how such an output composes when a third point approaches it. [The collision target](04-factorization.md#chiral-operation) · [Three collision residues](04-factorization.md#ch04-three-residues)
