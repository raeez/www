# Local fields on a curve

On a formal coordinate disc a vertex algebra \((V,\mathbf1,T,Y)\) assigns a field \(Y(a,z)\) to each state \(a\). Its Laurent coefficients \(a_{(n)}\) act on \(V\). One current already illustrates the passage from an operator product expansion to an algebra of modes. If
\[
 J(z)J(w)\sim\frac{\kappa\,\mathrm{id}}{(z-w)^2},
 \qquad J(z)=\sum_{m\in\mathbb Z}J_mz^{-m-1},
\]
then taking residues gives \([J_m,J_n]=\kappa m\delta_{m+n,0}\,\mathrm{id}\). Here \(\sim\) records the singular part at \(z=w\). The same double pole determines the commutator in every charge sector, while the zero mode \(J_0\) measures the charge. Laurent expansions are formal throughout. Analytic continuation and convergence of matrix coefficients require additional hypotheses. [Chapter 10](10-analytic-sewing.md)

## Fields and their modes {#fields-and-modes}

Let \(V\) be a complex vector space of states. A **field** on \(V\) is a series
\[
A(z)=\sum_{n\in\mathbb Z}A_nz^{-n-1},
\qquad A_n\in\operatorname{End}_{\mathbb C}(V),
\tag{3.1}
\]
such that, for each \(v\in V\), the vector \(A_nv\) vanishes for all sufficiently large \(n\). The bound may depend on \(v\). Consequently \(A(z)v\) belongs to \(V((z))\): it has only finitely many negative powers of \(z\), although it may have infinitely many positive powers. The operators \(A_n\) are the **modes** of the field.

The residue formula for the modes is
\[
A_n v=\operatorname{Res}_{z=0}z^n A(z)v\,dz.
\]
Here the formal residue extracts the coefficient of \(z^{-1}\). No analytic integral is required for this definition. If a particular matrix coefficient is represented by a convergent meromorphic function, the same coefficient is its usual contour residue.

The products \(A(z)B(w)\) and \(B(w)A(z)\) initially have different expansion conventions. Their difference is interpreted as a two-variable formal distribution. Two fields are **local** if there is an integer \(N\geq0\) such that
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
Their difference is \(\partial_w\delta(z,w)\), where \(\delta(z,w)=\sum_{m\in\mathbb Z}z^{-m-1}w^m\) is the formal delta distribution. Since \((z-w)\delta(z,w)=0\), one has \((z-w)^2\partial_w\delta(z,w)=0\). This is locality of order two for the Heisenberg current.

## A vertex algebra retains states and local products {#vertex-algebra}

A vertex algebra packages a compatible family of fields on one state space. In the even convention used here, its data are a vector space \(V\), a vacuum vector \(\mathbf1\), a translation operator \(T:V\to V\), and a linear assignment
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
and locality for every pair \(Y(a,z),Y(b,w)\). These conditions express the state–field correspondence, the infinitesimal motion of an insertion, and the compatibility of products at distinct positions. They imply
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
The symbol \(\sim\) means equality of singular parts in the indicated expansion convention. The sum is finite for each pair of states. The regular coefficients also belong to the vertex-algebra structure: in particular, \(a_{(-1)}b\) defines the normally ordered product. Retaining only (3.6) therefore retains less information than the full state–field map.

One can collect the singular coefficients into a polynomial in a formal variable \(\lambda\):
\[
[a_\lambda b]=\sum_{n\geq0}\frac{\lambda^n}{n!}a_{(n)}b.
\tag{3.7}
\]
This **\(\lambda\)-bracket** is convenient for differential identities. It records the singular products; it is not, by itself, a definition of the full vertex algebra. Beilinson and Drinfeld relate vertex algebras to translation-equivariant chiral algebras on the affine line in *Chiral Algebras*, §0.15, and express the state–field operation geometrically in §3.5.

## The free current as a complete calculation {#heisenberg-current}

Let \(\kappa\in\mathbb C\). Consider operators \(J_n\), for \(n\in\mathbb Z\), satisfying
\[
[J_m,J_n]=\kappa m\,\delta_{m+n,0}\operatorname{id}.
\tag{3.8}
\]
Here \(\delta_{r,0}\) is \(1\) for \(r=0\) and \(0\) otherwise. A vacuum representation with zero charge is
\[
V=\mathbb C[x_1,x_2,x_3,\ldots],
\qquad \mathbf1=1,
\]
where
\[
J_{-n}=x_n\cdot(-),\qquad
J_n=\kappa n\frac{\partial}{\partial x_n}
\quad(n>0),
\qquad J_0=0.
\tag{3.9}
\]
Every polynomial involves only finitely many variables, so \(J_n\) annihilates it for all sufficiently large positive \(n\). Hence
\[
J(z)=\sum_{n\in\mathbb Z}J_nz^{-n-1}
\]
is a field. The commutator in (3.8) follows directly from differentiation and multiplication. The negative modes create polynomial factors; the positive modes remove them.

Split the field into
\[
J_-(z)=\sum_{n<0}J_nz^{-n-1},
\qquad J_+(z)=\sum_{n\geq0}J_nz^{-n-1}.
\]
Normal ordering places the creation operators to the left:
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
The double pole is the sum of the mode commutators. In state notation, if \(j=x_1\), then \(j_{(1)}j=\kappa\mathbf1\) and the other singular products vanish. Thus \([j_\lambda j]=\kappa\lambda\mathbf1\).

Define \(T\) on the polynomial algebra as the derivation
\[
Tx_n=n x_{n+1}.
\]
It satisfies \([T,J_n]=-nJ_{n-1}\), hence \([T,J(z)]=\partial_zJ(z)\). The fields of polynomial states are generated by normal products and derivatives; for example,
\[
Y(x_2,z)=\partial_zJ(z),
\qquad Y(x_1^2,z)=:J(z)^2:.
\]
This is the rank-one Heisenberg vertex algebra. The central coefficient \(\kappa\) is part of its structure. Choosing a positive real value may support further analytic constructions, but the algebraic construction above assumes no positivity.

The functional \(\langle\mathbf1^*,-\rangle\) that takes the constant term of a polynomial gives
\[
\langle\mathbf1^*,J(z)J(w)\mathbf1\rangle
=\kappa\,\iota_{z,w}(z-w)^{-2}.
\tag{3.11}
\]
This particular two-point coefficient is the expansion of a meromorphic function. Its existence follows here from the explicit vacuum representation and functional. A different representation, charge or functional is additional data, even when the local mode relations remain the same.

### A charge measured by a contour {#ch03-charged-current-contour}

The contour operator \((2\pi i)^{-1}\oint J(z)\,dz=J_0\) measures the charge of a line ending at the encircled point. In abelian Chern–Simons theory on the half-space take a proper oriented Wilson ray of charge \(a\), fix the boundary complex coordinate and let \(k\ne0\) be the numerical boundary current level. The source couples the ray to the integral of the gauge one-form. For the local Fock calculation take the ray straight in the endpoint half-ball, with a moving graph ray vertical near the current tests. On that half-ball the change of source shifts the contour mode by \(a\). On the part of the cohomology spanned by finite angular weights the result is
\[
\mathcal F_a=\mathbb C[x_1,x_2,\ldots]|a\rangle,\qquad
J_{-n}=x_n,\quad J_n=kn\partial_{x_n}\ (n>0),\quad J_0=a .
\]
Thus the very same double-pole relation holds for every charge. The contour distinguishes two charges which any measurement using only that pole would identify.

The mutual normalization of two rays supplies information beyond their separate charges. Choose the Cauchy propagator, radial regularization, self-contraction prescription, outgoing subtraction and a fixed framing. Pair the result with the functional that sends the outgoing highest-weight state to one. In the prescribed common chamber the normalized primary coefficient is \((z-w)^{ab/k}\) for charges \(a,b\). Counterclockwise continuation of \(z-w\) through a full turn multiplies it by \(e^{2\pi iab/k}\). At level two a pair of unit charges therefore has full-turn multiplier \(-1\). The calculation on four lines in [Chapter 4](04-factorization.md#ch04-gaussian-collision) begins with these measured pair factors, then asks what else is required when the positions coincide.

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
The simple pole records the Lie bracket, while the double pole records the central extension. Neither can be recovered from the dimension of the state space.

For a direct check, take the \(z\)-residue after multiplying the simple pole by \(z^m\). It yields \(w^mJ^{[x,y]}(w)\). The double pole yields the derivative \(m w^{m-1}\). Taking the \(w\)-residue with \(w^n\) then gives precisely the two terms of (3.12). The residue calculation explains why a first derivative occurs in the central term.

A module for the current algebra must specify the action of every mode. The local-field condition asks that sufficiently high positive modes kill each vector. This is a vectorwise condition, often called **smoothness** in this setting; it does not impose a single bound on the whole module. The induced vacuum modules and the derived functors studied in later chapters preserve this distinction. Their algebraic completions cannot be selected by the shape of an operator-product formula alone.

## Differentiation and a change of coordinates {#differential-modules}

The coordinate \(z\) made the mode calculation transparent. To move from a disc to a curve, one needs a way to differentiate sections and to compare their descriptions in different coordinates. The sheaf \(\mathcal D_X\) on a smooth curve \(X\) is the sheaf of algebraic differential operators. On an affine coordinate chart its generators satisfy
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
This conversion accounts for the signs and one-form factors in a geometric residue. It is an equivalence between left and right differential modules; it is not a duality of the state spaces.

Locally, \(a_{(n)}b=\operatorname{Res}_{t=0}t^n Y(a,t)b\,dt\), with \(t=z-w\). Allowing Laurent multipliers in the source therefore recovers regular as well as singular field products. For a vertex algebra with the required coordinate-change action, the corresponding right differential module \(\mathcal V^{\mathrm r}\) on \(X\) has its two-point chiral operation valued in \(\Delta_*\mathcal V^{\mathrm r}\), where \(\Delta:X\hookrightarrow X^2\) is the diagonal. This is the local form of the chiral operation in [Chapter 4](04-factorization.md).
