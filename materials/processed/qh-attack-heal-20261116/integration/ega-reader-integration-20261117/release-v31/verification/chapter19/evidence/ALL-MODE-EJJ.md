# The cubic \(EJJ\) identity for polynomial transverse currents

The target is a normalized, colour- and transverse-equivariant local primitive for the order-\(s^3\) \(EJJ\) Jacobiator on every polynomial input. The incoming current and closed-generator bases, the simplex endpoints and the checked \(s^2\) four-tower brackets are fixed. Its non-axis and axis restrictions must agree with their separate signed results.

## Operation

Let \(A=\mathbb C[x,y]\), \(B=A\otimes A=\mathbb C[U,V]\), and \(\tau b(U,V)=b(V,U)\). The endpoint \(A\)-bimodule structure is \(f\cdot b\cdot g=f(U)b\,g(V)\). Put \(\mathcal E=x\partial_x+y\partial_y\). On \(A/\mathbb C\) define \(\mathcal E^{-1}\) by dividing a homogeneous component of positive degree by its degree. For a closed input \(p\in A/\mathbb C\), set \(X=X_p=\{\mathcal E^{-1}p,-\}\), with \(\{f,g\}=f_xg_y-f_yg_x\). Thus \(X=(X^1,X^2)=(-P_y,P_x)\) for \(P=\mathcal E^{-1}p\), and \(\partial_x X^1+\partial_y X^2=0\).

Let the normalized degree-two Hochschild cochain be
\[
 \Phi(f,g)(U,V)=-\int_{0\le b\le a\le1}
    [\nabla f(z_a),\nabla g(z_b)]\,da\,db,\qquad
 z_a=aU+(1-a)V ,
\]
where brackets inside the integral denote the determinant, and write
\[
 H_p(f,g)=(X_U+X_V)\Phi(f,g)-\Phi(Xf,g)-\Phi(f,Xg).
 \tag{1}
\]
Define \(h_p:A\to B\) by \(h_p(1)=h_p(x)=h_p(y)=0\). For a monomial \(q\) and a coordinate \(s_0=x,y\), set
\[
       h_p(qs_0)=h_p(q)s_0(V)-H_p(q,s_0).
 \tag{2}
\]
Extend linearly in both inputs. The recursion is independent of which coordinate is removed. For \(c\in\mathfrak{sl}_2\), let
\[
 \Xi_c=(1\otimes\operatorname{ad}_{-c})\Omega
       =\sum_i u_i\otimes[u^i,c],\qquad
 \Omega=\tfrac12 h\otimes h+e\otimes f+f\otimes e .
\]
If \(Q\) sends a pair of coloured endpoint polynomials to its normally ordered \(LL\) product, the physical correction is
\[
 [E[p]_\lambda J_c[t]]_{s^3}
    =\ell\nu\,\psi_c(p,t),\qquad
 \boxed{\displaystyle\psi_c(p,t)=-\tfrac12\,Q(\Xi_c h_p(t)).}
 \tag{3}
\]
Here \(\ell=s,\ \nu=-3s^2/8\), and \(\gamma=8\) for \(K=\operatorname{Tr}_2\). Equations (1)–(3) solve the complete \(EJJ\) identity at order \(s^3\) in the pure axion-coupled extended-SDYM source. They give the unique normalized local coefficient with the native colour, field content, degree and transverse equivariance. The local coefficient is a simple pole with two negative currents, no longitudinal derivative, no negative output degrees, and \(\sum k=p+t-2(1,1)\) on monomials. Vertex translation supplies every longitudinal descendant.

## Why the endpoint primitive exists

The lower simplex obeys \(b\Phi=0\) and \(\Phi(f,g)=-\tau\Phi(g,f)\). This can be seen by expanding its coboundary in the ordered three-simplex, where the integrand is the contraction of an alternating three-covector on a plane. The signed order-two source and independent simplex review use these precise endpoints. The derivations \(X\) on \(A\) and \(X_U+X_V\) on \(B\) obey the two bimodule Leibniz rules. Consequently \(bH_p=0\). It is normalized, and \(H_p(f,g)=-\tau H_p(g,f)\).

The stronger identity needed for (2) is \(H_p(x,y)=H_p(y,x)\) *before* diagonal restriction. For any polynomial \(F\), direct integration gives
\[
\begin{aligned}
 \Phi(F,y)&=-\int aF_x(z_a)\,da,&
 \Phi(y,F)&=\int(1-a)F_x(z_a)\,da,\\
 \Phi(F,x)&=\int aF_y(z_a)\,da,&
 \Phi(x,F)&=-\int(1-a)F_y(z_a)\,da .
\end{aligned}
\]
All four integrals run from zero to one. Since \(\Phi(x,y)=-1/2,\ \Phi(y,x)=1/2\), equation (1) gives
\[
 H_p(x,y)-H_p(y,x)
 =\int_0^1 ((X^1)_x+(X^2)_y)(z_a)\,da=0.
\]
For two final coordinate letters \(s_0,t_0\), the difference between the two evaluations of (2) on \(q s_0 t_0=q t_0 s_0\) is \(-q(U)(H_p(s_0,t_0)-H_p(t_0,s_0))\), by \(bH_p(q,s_0,t_0)=0\). It vanishes. Appending any suffix preserves the equality, so adjacent swaps prove independence of the word chosen to represent an arbitrary commutative monomial.

By construction \((bh_p)(q,s_0)=H_p(q,s_0)\). The difference \(b h_p-H_p\) is a normalized two-cocycle vanishing whenever its second input is linear. Its cocycle equation extends the vanishing one letter at a time to every second input. This proves \(bh_p=H_p\). Any two scalar primitives with the displayed coordinate normalization differ by an endpoint derivation vanishing on \(x,y\), hence coincide. Applying this uniqueness to \(-\tau h_p\) and using reversal gives \(\tau h_p=-h_p\). Since \(\Phi\), \(\mathcal E^{-1}\) and the Hamiltonian bracket are \(SL_2^+\)-covariant and \(h_p\) vanishes on the entire space of linear polynomials, the unique normalized \(h_p\) is equivariant. No choice of order for \(x,y\) enters the result.

Each application of a determinant lowers the total transverse bidegree by \((1,1)\). Thus \(H_p(f,g)\) has bidegree \(p+f+g-(2,2)\) on monomial labels, and (2) gives the asserted support. No negative powers occur. One integration and finitely many polynomial operations suffice at each recursion step. Euler inversion acts on the closed polynomial alone and is defined on every allowed mode. There is no inverse longitudinal derivative or nonlocality on the chiral curve. The empty transverse mode of \(p\) is absent, and current degree zero or one gives \(\psi=0\). Closed degree one or two also gives zero because \(X\) then acts by a translation or by an infinitesimal determinant-one linear transformation, both symmetries of the kernel.

## Colour and Ward signs

Write \(C_{ab}=(\operatorname{ad}_a\otimes\operatorname{ad}_b)\Omega\), so \(C_{ba}=\tau_{\rm col}C_{ab}\), with \(\tau_{\rm col}\) interchanging solely the colour tensors. The \(JJ\to JL\) term contains the two ordered placements. When the external \(E[p]\) hits the positive current in them, its tree coefficient is \(X_p\). Recombining both placements by commutativity of the two final \(L\)'s gives \(Q(C_{ab}(X_U+X_V)\Phi(f,g))\). The next nesting, with \(E\) acting first on \(J_a[f]\), yields \(-Q(C_{ab}\Phi(Xf,g))\). The final nesting, first on \(J_b[g]\), yields \(+Q(C_{ba}\Phi(Xg,f))=-Q(C_{ab}\Phi(f,Xg))\). Hence the complete bare residue in units of \(\ell\nu\) is \(Q(C_{ab}H_p(f,g))\). The two formal bracket variables remain independent in this argument. Both the outer \(E\) on the lower \(T\)-, \(\lambda\)- or \(\mu\)-dependent \(LL,E,F\) recipient and the Wick integral between two \(L\)'s vanish, so only a spectral-constant \(LL\) polynomial remains. This repeats the finite proof without a transverse degree bound.

Identify tensors of the two colours with endomorphisms via \(u\otimes v:z\mapsto uK(v,z)\). Then \(\Xi_a=\operatorname{ad}_a\) is skew and \(C_{ab}=-\operatorname{ad}_a\operatorname{ad}_b\). The first-slot action of \(b\) on \(\Xi_a\) equals \(-C_{ba}\), the second-slot action equals \(C_{ab}\), and \(\Xi_{[a,b]}=C_{ba}-C_{ab}\). The linearized Ward differential on any correction is
\[
 (\delta\psi)(p;a,f;b,g)=\psi_{[a,b]}(p,fg)
       +\mathcal R_{b,g}\psi_a(p,f)-\mathcal R_{a,f}\psi_b(p,g)
\]
with \(\mathcal R_{a,f}L_b[t]=L_{[a,b]}[ft]\). Using the preceding three colour identities, the expression on \(Q(\Xi_c h(t))\) for \(h=-\tau h\) is
\[
 Q\big(C_{ab}(bh)(f,g)-C_{ba}(bh)(g,f)\big)
      =2Q\big(C_{ab}(bh)(f,g)\big).
\]
This fixes both the minus sign and the factor \(1/2\) in (3). Together with \(bh_p=H_p\), it gives \(\rho+\delta\psi=0\) for every colour and both ordered currents. The Jacobiator on \(T^i E,T^jJ,T^kJ\) is this identity multiplied by \((-\lambda)^i(-\mu)^j(T+\lambda+\mu)^k\).

## Local ambiguities and uniqueness

For \(\mathfrak{sl}_2\) the equivariant colour map from the adjoint to two adjoints is unique up to scalar and is antisymmetric. Thus a general \(EJ\to LL\) correction uses \(\Xi_c\) paired with an exterior transverse two-tensor. At fixed positive \(E\)-degree \(R\), current degree \(S\) and output degrees \(A\le B,\ A+B=R+S-4\), its complete local \(SL_2^+\)-equivariant space has one line for every \(0\le n\le A\) with \(n+2\le\min(R,S)\), restricted to odd \(n\) when \(A=B\). Indeed the Clebsch–Gordan weights match when one first takes the \(n+2\) input transvectant and then polarizes the result into \((A-n,B-n)\) and multiplies by \(\det(U,V)^n\). These are precisely the columns used in the signed finite calculation. The FP scaling, colour and field-content assumptions are essential to the list. In the associated chiral coordinate problem the positive-pole field \(LL\) has no available longitudinal derivative and it has no ordering ambiguity since \(LL\) is regular. The finite first-quantum source fixes the inhomogeneous term, independent of higher changes to the other brackets.

For \(S=0,1\) the displayed space is empty. Equivalently the least input highest weight exceeds the total available output degree whenever \(\min(R,S)<2\). Suppose \(\psi'\) is any other admissible solution, without assuming an endpoint-cocycle ansatz for it. For fixed \(p\), \(d(a f)=(\psi'-\psi)_a(p,f)\) is a Lie one-cocycle of \(\mathfrak{sl}_2\otimes A\) with values in the commutative \(LL\) recipient under the tree action. The degree cutoff gives \(d=0\) on \(\mathfrak g\otimes\langle 1,x,y\rangle\). The Lie algebra generated by these elements is the entire current algebra. In detail, write any degree-\(S\) monomial as \(q s_0\) with \(s_0=x\) or \(y\). Perfection expresses its colour as a sum of brackets, and \([a q,b s_0]=[a,b]q s_0\). Induction and the Lie cocycle identity imply \(d=0\) in every degree. This proves actual uniqueness of the physical coefficient, without requiring the scalar endpoint model to exhaust Lie-complex primitives a priori.

In the normalized generator problem, an admissible local change of lifts that leaves the lower brackets fixed in their identified PBW basis, respects the degrees and covariances, and preserves the FP field content takes one solution to another. Its variation in this recipient is therefore zero, by the preceding argument. The induced coboundary image and the homogeneous solution space in this projected channel are both zero. Lifts acting trivially here can still change other fields or other order-three identities. Without transverse equivariance there can already be endpoint-derivation primitives with freely chosen values on the two coordinate generators subject to the endpoint syzygy. Such unmarked choices are a different problem.

## Boundary tests

In the stable-axis quotient the only cubic component has \(J\)-degree two on the positive axis and \(E\)-degree \(k\ge2\). Put \(p=x^k,t=y^2\). Then \(X=x^{k-1}\partial_y\), \(\Phi(y,y)=0\). The two linear-slot kernels in (1) give
\[
 H_p(y,y)=(k-1)\int_0^1(2a-1)(aU_1+(1-a)V_1)^{k-2}\,da .
\]
This polynomial is antisymmetric in \(U,V\). From (2) \(h_p(y^2)=-H_p(y,y)\). Hence the coefficient of the stable-axis correction is
\[
 \psi_c(x^k,y^2)=\frac1k\sum_{i+j=k-2}(i+1)\,\Xi_c((i,0),(j,0)).
\]
Indeed the coefficient of the integral times \(1/2\) at \(U_1^i V_1^j\) is \((i+1)/k-1/2\), and the constant \(-1/2\) cancels against the antisymmetric colour tensor. This recovers the signed holonomy coefficient for every \(k\) and its rotated versions. The \(k=2\) colour contraction vanishes. At \(k=3\), \([E[3,0]_\lambda J_e[0,2]]_{\ell\nu}\) is \(\tfrac13:L_e[0]L_h[1,0]:-\tfrac13:L_e[1,0]L_h[0]:\). The literal published shifted kernel contains \((2,-1)\) and returns zero. Its bare Jacobi rows are \(-2/3,+2/3\) on the same two words. Powers of \(q\) beyond one in the signed holonomy are higher deformation orders, and the present calculation only uses the linear-in-\(q\) term.

On the independently signed homogeneous degrees \((4;2,3)\), (3) is a solution in the exact ten-column covariant space. Full rank of the signed finite system proves it equals the normalized ten-coefficient vector algebraically. A separate evaluation compared both operations at every input and all three colours, across current degrees \(2,3,5\). It recovers the basis vector
\[
\left(-\tfrac1{48},-\tfrac1{90},-\tfrac1{360},\tfrac1{288},-\tfrac1{210},
-\tfrac3{2800},\tfrac1{1800},-\tfrac1{5600},\tfrac{11}{21600},\tfrac1{17280}\right)
\]
in the ordering of the [independent finite certificate](../../first-quantum-source/mixed-cubic-independent/VERDICT.md). The deciding bare PBW coefficient remains \(-1/4\) in \(\ell\nu\) units, or \(+3s^3/32\), and (3) supplies the negative of it.

The [polynomial implementation](universal.py) compares both generator stripping orders, checks \(b h_p=H_p\) directly, and recomputes the equation in the complete PBW recipient. The additional degree block \((5;2,4)\) includes both orders on 1,620 triples, 1,464 with nonzero bare residues. For \(p=(4,1),f=(1,1),g=(1,3)\) and colours \(h,e\), \(\det(f,g)=2\). The bare coefficient on \(:L_e[0,0]L_h[4,3]:\) is \(-154/225\) in \(\ell\nu\) units, or \(+77s^3/300\). Equation (3) cancels that row. A separate low-degree block and the polynomial current unit give zero as predicted. [Exact tests](CHECKS.json)

The result is for the full \(EJJ\) identity at deformation order three. The \(FJJ,JJJ\) and other identities, the global four-tower extension at this order, and PBW or flatness of its derived chiral cuts require their own constructions.
