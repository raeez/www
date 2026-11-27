# Local fields on a curve

To measure the charge of a line ending on a surface, draw a small circle around its endpoint and integrate the current along the circle. On a complex coordinate disk with coordinate \(z\) and endpoint \(0\), write \(J(z)\,dz\) for the current one-form. If \(J(z)\,dz\) has a term \(Q\,dz/z\) at the origin, the positively oriented contour integral divided by \(2\pi i\) returns the operator \(Q\). Weighting the same contour by \(z^n\) selects a different Laurent coefficient. In this way a local field can give a whole family of operators on states.

The product of two such operators depends on an ordering of the contours, one inside the other. When the inner contour is moved past the outer insertion, the singularity at their collision determines the change. For a charged insertion the simple-pole coefficient of its current gives the action of the charge operator. A double pole differentiates the function used to weight the contour. These residue operations make sense algebraically, even when no convergent contour integral has been given.

## Fields and their modes {#fields-and-modes}

Let \(V\) be a complex vector space of states. A **field** on \(V\) is a series
\[
A(z)=\sum_{n\in\mathbb Z}A_nz^{-n-1},
\qquad A_n\in\operatorname{End}_{\mathbb C}(V),
\tag{3.1}
\]
such that, for each \(v\in V\), the vector \(A_nv\) vanishes for all sufficiently large \(n\). The bound may depend on \(v\). Consequently \(A(z)v\) belongs to \(V((z))\): it has only finitely many negative powers of \(z\), although it may have infinitely many positive powers. The operators \(A_n\) are the **modes** of the field. Acting first on a fixed state is essential. A single common bound on the pole order for all states would exclude familiar oscillator fields.

The residue formula for the modes is
\[
A_n v=\operatorname{Res}_{z=0}z^n A(z)v\,dz.
\]
Here the formal residue extracts the coefficient of \(z^{-1}\). No analytic integral is required for this definition. If a particular matrix coefficient is represented by a convergent meromorphic function, the same coefficient is its usual contour residue.

Apply \(B(w)\) first, then \(A(z)\). The resulting expression \(A(z)B(w)v\) has its Laurent expansion ordered differently from \(B(w)A(z)v\). To subtract them one compares all coefficients of \(z^pw^q\), as operators on \(V\). An array of coefficients indexed by both powers, with no single choice of annulus imposed, is a *formal distribution* in two variables. The commutator of the two fields is such a distribution.

Two fields are **local** if there is an integer \(N\geq0\) such that
\[
(z-w)^N[A(z),B(w)]=0.
\tag{3.2}
\]
We are using even, or bosonic, fields; fields with odd parity require the corresponding graded commutator. Equation (3.2) says that multiplying by a sufficiently high power of the collision equation removes the difference between the two expansions. It does not assign a finite product at \(z=w\).

For example, write \(\iota_{z,w}\) for expansion in nonnegative powers of \(w/z\), and \(\iota_{w,z}\) for expansion in nonnegative powers of \(z/w\). Then
\[
\iota_{z,w}\frac1{(z-w)^2}
=\sum_{r\geq0}(r+1)w^rz^{-r-2},
\qquad
\iota_{w,z}\frac1{(z-w)^2}
=\sum_{r\geq0}(r+1)z^rw^{-r-2}.
\tag{3.3}
\]
The difference of the simple-pole expansions has a useful name,
\[
 \delta(z,w)=\sum_{m\in\mathbb Z}z^{-m-1}w^m.
\]
For every Laurent polynomial \(f\), coefficient extraction gives \(\operatorname{Res}_z f(z)\delta(z,w)\,dz=f(w)\). Multiplication by \(z\) or by \(w\) gives the same series after shifting the summation index, hence \((z-w)\delta=0\). Differentiating the simple-pole expansions with respect to \(w\) gives (3.3). Their difference therefore tests \(f\) by \(f'(w)\), and is killed by \((z-w)^2\). This is how a double pole can contribute to a commutator concentrated at \(z=w\).

## A vertex algebra retains states and local products {#vertex-algebra}

A contour measures an existing state. Conversely, inserting a field into the vacuum can *prepare* a state. In a vertex algebra the two descriptions are tied together by assigning a field to every state, and translating a field agrees with moving its insertion. In the even convention used here, its data are a vector space \(V\), a vacuum vector \(\mathbf1\), a translation operator \(T:V\to V\), and a linear assignment
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
and locality for every pair \(Y(a,z),Y(b,w)\). For example set \(v(z)=Y(a,z)\mathbf1\). Creation gives \(v(0)=a\). Translation and \(T\mathbf1=0\) give \(\partial_zv(z)=Tv(z)\), so comparison of Taylor coefficients yields
\[
Y(a,z)\mathbf1=e^{zT}a,
\qquad a=a_{(-1)}\mathbf1.
\]
Thus the vacuum connects an operator-valued field with the state it creates. It has not yet supplied a scalar-valued vacuum expectation: that requires a linear functional or pairing in addition.

The singular part of the product is written
\[
Y(a,z)Y(b,w)
\sim\sum_{n\geq0}
\frac{Y(a_{(n)}b,w)}{(z-w)^{n+1}}.
\tag{3.6}
\]
The symbol \(\sim\) means equality of singular parts in the indicated expansion convention. The sum is finite for each pair of states. The constant term of \(Y(a,t)b\) at \(t=0\) is \(a_{(-1)}b\). It is the state corresponding to the normally ordered product, obtained by removing the singular part before evaluating the regular coefficient. Thus two fields can have a nonzero product even when all the singular products in (3.6) vanish.

To read several singular coefficients with one test, pair \(Y(a,t)b\) with \(e^{\lambda t}\,dt\) and take the residue in \(t\). The powers of \(t\) in the exponential select the pole coefficients with their factorials. The resulting polynomial in the formal variable \(\lambda\) is
\[
[a_\lambda b]=\sum_{n\geq0}\frac{\lambda^n}{n!}a_{(n)}b.
\tag{3.7}
\]
This **\(\lambda\)-bracket** is convenient for differential identities. It records the singular products; it is not, by itself, a definition of the full vertex algebra. Beilinson and Drinfeld relate vertex algebras to translation-equivariant chiral algebras on the affine line in *Chiral Algebras*, §0.15, and express the state–field operation geometrically in §3.5.

## The free current as a complete calculation {#heisenberg-current}

Consider a single conserved abelian current. Its modes with opposite indices can create and annihilate an excitation of the same energy. Write \(\kappa\in\mathbb C\) for the coefficient of the central term (the current level). The **Heisenberg commutation relations** prescribe operators \(J_n\), for \(n\in\mathbb Z\), satisfying
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
Every polynomial involves only finitely many variables, so \(J_n\) annihilates it for all sufficiently large positive \(n\). Hence
\[
J(z)=\sum_{n\in\mathbb Z}J_nz^{-n-1}
\]
is a field. For instance \(J_2J_{-2}\mathbf1=2\kappa\mathbf1\), whereas \(J_{-2}J_2\mathbf1=0\). When the indices differ, \(\partial_{p_m}\) commutes with multiplication by \(p_n\). This gives precisely (3.8). The negative modes create occupation factors and the positive modes lower their multiplicities. The variable \(p_n\) stands for one quantum of the \(n\)th harmonic. For \(\kappa=1\) and \(n=1,2\) these are the operators of the [two-harmonic measurement](01-physical-questions.md#ch01-two-preparations) in Chapter 1.

Split the field into
\[
J_-(z)=\sum_{n<0}J_nz^{-n-1},
\qquad J_+(z)=\sum_{n\geq0}J_nz^{-n-1}.
\]
In a vacuum matrix element an annihilation operator gives zero if it reaches the vacuum on the right. It is therefore useful to move the creation operators to the left. This prescription defines **normal ordering**,
\[
:J(z)J(w):=J_-(z)J(w)+J(w)J_+(z).
\]
Commuting the remaining positive modes through \(J(w)\) gives
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
The central coefficient survives each interchange of an annihilator and a creator of the same index. Summing these coefficients uses \(\sum_{n\ge1}n u^{n-1}=(1-u)^{-2}\) at \(u=w/z\). Conversely the difference of the two expansions in (3.3) is \(\partial_w\delta(z,w)\). Testing it first with \(z^m\) and then with \(w^n\) gives \(m\delta_{m+n,0}\), recovering the commutator from the pole. In state notation, if \(j=p_1\), then \(j_{(1)}j=\kappa\mathbf1\) and the other singular products vanish. Thus \([j_\lambda j]=\kappa\lambda\mathbf1\).

Define \(T\) on the polynomial algebra as the derivation
\[
Tp_n=n p_{n+1}.
\]
It satisfies \([T,J_n]=-nJ_{n-1}\), hence \([T,J(z)]=\partial_zJ(z)\). The fields of polynomial states are generated by normal products and derivatives; for example,
\[
Y(p_2,z)=\partial_zJ(z),
\qquad Y(p_1^2,z)=:J(z)^2:.
\]
This is the rank-one Heisenberg vertex algebra. The central coefficient \(\kappa\) is part of its structure. Choosing a positive real value may support further analytic constructions, but the algebraic construction above assumes no positivity.

To obtain a scalar amplitude, prepare the vacuum and extract the vacuum component after the two insertions. The linear functional \(\langle\mathbf1^*,-\rangle\) does this by taking the constant term of a polynomial. The normally ordered contribution to this particular matrix element is zero, so
\[
\langle\mathbf1^*,J(z)J(w)\mathbf1\rangle
=\kappa\,\iota_{z,w}(z-w)^{-2}.
\tag{3.11}
\]
This particular two-point coefficient is the expansion of a meromorphic function. Its existence follows here from the explicit vacuum representation and functional. A different representation, charge or functional is additional data, even when the local mode relations remain the same.

### A charge measured by a contour {#ch03-charged-current-contour}

Apply the unweighted contour to a state prepared by a charged source. A Wilson ray in abelian Chern–Simons theory couples the gauge one-form to its integral along an oriented half-line whose endpoint lies on the boundary. Fix the boundary coordinate, a numerical current level \(k\ne0\), and a ray of charge \(a\) which is straight near the endpoint. The test contour is positively oriented and surrounds that endpoint. In the half-space calculation with a moving graph ray one requires it to remain vertical near the current tests. The source contributes the residue \(a\), shifting the zero mode of the vacuum sector. On cohomology spanned by finite angular weights the resulting state space is
\[
 \mathcal F_a=\mathbb C[p_1,p_2,\ldots]|a\rangle,\qquad
 J_{-n}=p_n,\quad J_n=kn\partial_{p_n}\ (n>0),\quad J_0=a .
\]
Here \(|a\rangle\) has no oscillator excitations, \(k\) is the \(\kappa\) of (3.8), and \((2\pi i)^{-1}\oint J(z)\,dz=J_0\).

Thus the very same double-pole relation holds for every charge. The contour distinguishes two charges which any measurement using only that pole would identify.

With two rays the current can still measure the total charge by one enclosing contour. A different observable is the amplitude that remains after their oscillator-free outgoing component is extracted. Choose the Cauchy propagator, radial regularization, self-contraction prescription, outgoing subtraction and a fixed framing. Pair the result with the functional that sends the outgoing highest-weight state to one. In the prescribed common chamber the normalized primary coefficient is \((z-w)^{ab/k}\) for charges \(a,b\). Counterclockwise continuation of \(z-w\) through a full turn multiplies it by \(e^{2\pi iab/k}\). At level two a pair of unit charges therefore has full-turn multiplier \(-1\). The calculation on four lines in [Chapter 4](04-factorization.md#ch04-gaussian-collision) begins with these measured pair factors, then asks what else is required when the positions coincide.

## Nonabelian currents and the information in a pole {#affine-currents}

Let \(\mathfrak g\) be a finite-dimensional Lie algebra with an invariant symmetric bilinear form \((x,y)\), and let \(\ell\in\mathbb C\) be a level. The affine current relations are
\[
[J^x_m,J^y_n]
=J^{[x,y]}_{m+n}
+\ell m(x,y)\delta_{m+n,0}\operatorname{id}.
\tag{3.12}
\]
Invariance means \(([x,y],z)=(x,[y,z])\); it is the compatibility required for the central term to satisfy the Jacobi identity. The associated current expansion is
\[
J^x(z)J^y(w)
\sim\frac{J^{[x,y]}(w)}{z-w}
+\frac{\ell(x,y)}{(z-w)^2}.
\tag{3.13}
\]
For example, take \(\mathfrak{sl}_2\) with the trace form \((x,y)=\operatorname{tr}(xy)\). Let \(H=\operatorname{diag}(1,-1)\) and \(E\) be the matrix with entry \(1\) in position \((1,2)\) and zeros elsewhere. Then \([H,E]=2E\) and \(\operatorname{tr}(HE)=0\), so the \(H,E\) current product has only the simple pole \(2J^E(w)/(z-w)\). With two \(H\) currents the bracket is zero and \(\operatorname{tr}(H^2)=2\), so only the double pole \(2\ell/(z-w)^2\) remains.

To read the mode commutator, take the difference of the two radial expansions. Its simple pole gives \(\delta(z,w)\) and its double pole gives \(\partial_w\delta(z,w)\). Testing with \(z^m\) returns \(w^mJ^{[x,y]}(w)\) in the first term and \(\ell(x,y)m w^{m-1}\) in the second. The residue against \(w^n\) is respectively \(J^{[x,y]}_{m+n}\) and \(\ell m(x,y)\delta_{m+n,0}\). This derives (3.12) with its sign and both mode indices.

A module for the current algebra must specify the action of every mode. The local-field condition asks that sufficiently high positive modes kill each vector. This is a vectorwise condition, often called **smoothness** in this setting; it does not impose a single bound on the whole module. The induced vacuum modules and the derived functors studied in later chapters preserve this distinction. Their algebraic completions cannot be selected by the shape of an operator-product formula alone.

## Differentiation and a change of coordinates {#differential-modules}

The residue of a one-form at a point is unchanged by any regular change of local coordinate. Its Laurent coefficients away from degree \(-1\), taken separately, generally change. To place fields on an entire curve, one needs transition maps for the fields and a rule for differentiating a field multiplied by a function. The sheaf \(\mathcal D_X\) on a smooth curve \(X\) is the sheaf of algebraic differential operators. On an affine coordinate chart its generators satisfy
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
The equation records translation together with differentiation of scalar coefficients. It does not, on its own, give the response of a vertex algebra to every nonlinear coordinate change. To obtain a coordinate-independent construction on arbitrary curves, one supplies suitable coordinate-change actions; a conformal structure is a familiar way to obtain them. Translation-equivariant algebras on the affine line and coordinate-independent algebras on all curves are therefore different global assertions.

Chiral operations are conventionally written for right differential modules. If \(M\) is a left module, its corresponding right module is
\[
M^{\mathrm r}=\omega_X\otimes_{\mathcal O_X}M,
\]
where \(\omega_X\) is the line bundle of one-forms. In a coordinate,
\[
(dz\otimes m)\cdot\partial_z=-dz\otimes\nabla_{\partial_z}m.
\tag{3.15}
\]
The sign is the sign of integration by parts. For ordinary functions \(f,g\), the residue of the exact form \(d(fg)\) vanishes, giving \(\operatorname{Res}f\,dg=-\operatorname{Res}g\,df\). Tensoring with \(\omega_X\) is the equivalence between left and right differential modules. It requires no choice of dual state space.

Locally, \(a_{(n)}b=\operatorname{Res}_{t=0}t^n Y(a,t)b\,dt\), with \(t=z-w\). Allowing Laurent multipliers in the source therefore recovers regular as well as singular field products. For a vertex algebra with the required coordinate-change action, the corresponding right differential module \(\mathcal V^{\mathrm r}\) on \(X\) has its two-point chiral operation valued in \(\Delta_*\mathcal V^{\mathrm r}\), where \(\Delta:X\hookrightarrow X^2\) is the diagonal. This is the local form of the chiral operation in [Chapter 4](04-factorization.md).
