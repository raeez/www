# The cubic closed-current identity for metric Lie algebras

Let \(A=k[x,y]\), where \(k\) has characteristic zero. A transverse mode is a monomial of \(A\). The two negative-current outputs of a simple pole carry two independent points \(U,V\) of the transverse plane. Set \(B=A\otimes_k A\), with \(f\) acting on the left by \(f(U)\) and on the right by \(f(V)\). Let \((\mathfrak g,K)\) be a finite-dimensional Lie algebra with a nondegenerate invariant symmetric form, and put \(L=\mathfrak g\otimes A\), \(M=\operatorname{Sym}^2_k L\). A current \(a f\) acts on \(M\) by the adjoint action on each factor, multiplying that factor by \(f\). The distinct endpoint labels are essential, even though the two output fields have regular mutual OPE.

## Existence for every metric colour

Write \(\Omega=\sum_i u_i\otimes u^i\) for the inverse form, \(C_{ab}=(\operatorname{ad}_a\otimes\operatorname{ad}_b)\Omega\), and \(\Xi_c=\sum_i u_i\otimes[u^i,c]\). Let \(Q:(\mathfrak g\otimes\mathfrak g)\otimes B\to M\) give the two factors their respective colours and transverse modes and then take their symmetric product.

For an occupied closed generator \(E[p]\), \(p\in A/k\), divide each positive homogeneous part by its degree to form \(P=\mathcal E^{-1}p\), where \(\mathcal E=x\partial_x+y\partial_y\). Its tree action has Hamiltonian vector field \(X=\{P,-\}\), with \(\{x,y\}=1\). Let
\[
 \Phi(f,g)=-\int_{0\le b\le a\le1}
 \det\!\big(\nabla f(z_a),\nabla g(z_b)\big)\,db\,da,\qquad z_a=V+a(U-V).
\]
The integrals integrate polynomials over \(k\). Define \(H=(X_U+X_V)\Phi-\Phi(X-,-)-\Phi(-,X-)\). There exists a unique endpoint one-cochain \(h\) with \(bh=H\) and \(h(1)=h(x)=h(y)=0\). It is antisymmetric in \(U,V\).

Indeed \(b\Phi=0\) and the three derivations are compatible with endpoint multiplication, so \(bH=0\). Direct integration at the two linear inputs gives
\[
 H(x,y)-H(y,x)=\int_0^1 \operatorname{div}(X)(z_a)\,da=0.
\]
Define \(h(qs)=h(q)s(V)-H(q,s)\) for \(s=x,y\). The two ways of evaluating \(h(qxy)\) differ by \(-q(U)(H(x,y)-H(y,x))\), by \(bH=0\). Interchanging adjacent letters proves independence of the monomial presentation. The same cocycle equation, by induction on the second argument, gives \(bh=H\). An endpoint derivation vanishing on both coordinates is zero. The reversal \(\Phi(f,g)(U,V)=-\Phi(g,f)(V,U)\), followed by uniqueness, makes \(h\) antisymmetric. The construction commutes with the transverse \(\mathrm{SL}_2\) action. [Polynomial endpoint construction](../all-mode-ejj/THEOREM.md) · [One-loop source](../../first-quantum-source/REVIEW.md)

**Proposition.** Suppose the lower current brackets give the order-\(\ell\nu\) bare \(EJJ\) residual \(Q(C_{ab}H(f,g))\). Then the single-pole coefficient of \([E[p]_\lambda J_c[t]]\) given by
\[
                         \psi_c(p,t)=-\tfrac12 Q(\Xi_c h(t))
\]
cancels it for all \(a,b,c,p,f,g,t\) over every metric Lie algebra. For each generator triple use its two independent spectral variables. All longitudinal descendants follow by sesquilinearity.

To prove the proposition, identify \(u\otimes v\) with \(z\mapsto uK(v,z)\). Invariance of the metric gives \(\Xi_a=\operatorname{ad}_a\) and \(C_{ab}=-\operatorname{ad}_a\operatorname{ad}_b\). The first and second slot actions of \(b\) on \(\Xi_a\) correspond to \(-C_{ba}\) and \(C_{ab}\), and \(\Xi_{[a,b]}=C_{ba}-C_{ab}\). Substituting these identities into
\[
 (\delta\psi)(a f,b g)=\psi_{[a,b]}(p,fg)+
       (b g)\cdot\psi_a(p,f)-(a f)\cdot\psi_b(p,g)
\]
gives \(\delta Q(\Xi h)=Q(C_{ab}bh(f,g)-C_{ba}bh(g,f))=2Q(C_{ab}H(f,g))\). In the last equality simultaneous exchange of endpoints and colour slots preserves \(Q\). This proof uses invariance of the form and Lie Jacobi alone.

In pure axion-coupled self-dual Yang–Mills, the verified four-tower lower brackets have this bare residual. The tree \(EJ\) term differentiates the one-loop \(JJ\to JL\) kernel at both endpoints. The two other nestings differentiate its two inputs. All terms ending in \(E,F,L\) are regular with the outer \(E\), and the two negative outputs have regular mutual bracket. This leaves precisely \(H\), independent of the spectral variables. For each anomalously factorizing simple colour with \(\operatorname{Tr}_{\rm ad}((\operatorname{ad}a)^4)=\gamma K(a,a)^2\), take \(\ell=s,\ \nu=-3s^2/\gamma\). The proposition supplies its cubic \(EJJ\) sector. The full four-tower vertex algebra has been established through order \(s^2\). Extending it through \(s^3\) also requires the \(FJJ\), \(JJJ\), and other coupled identities. For matter-dependent anomaly cancellation, the additional physical brackets must be included when deriving the bare residual. [First-quantum source and hypotheses](../../first-quantum-source/REVIEW.md) · [Fernández–Paquette](https://arxiv.org/abs/2412.17168)

## When the coefficient is forced

Assume full transverse \(\mathrm{SL}_2\) equivariance for every admissible map, including every difference of two solutions. Allow all adjoint-colour-equivariant maps in the two-negative-field simple-pole ansatz, with transverse total output degree \(R+S-4\) on inputs of degrees \(R=\deg p,\ S=\deg t\). If \(S=0,1\), each input summand has transverse highest weight at least \(|R-S|\), while the maximal output weight is \(R+S-4\). The former exceeds the latter for each \(R\) when \(S<2\). Thus a difference \(d\) of two solutions vanishes on \(\mathfrak g\otimes\langle1,x,y\rangle\), independently of the number of allowed invariant colour tensors. For fixed \(p\), \(d\) is a Lie one-cocycle \(L\to M\).

If \(\mathfrak g\) is perfect, those currents generate \(L\). To see this, factor a monomial of degree \(n\ge2\) as \(qs\), \(s=x,y\), and write its colour as \(\sum_i[a_i,b_i]\). Then \(\sum_i[a_iq,b_is]\) is the required current, and induction finishes the proof. Each summand in its cocycle equation has zero right-hand side. Hence the cubic coefficient is unique for every perfect metric colour. In particular a symmetric cubic invariant, when present, gives no additional solution with these physical weights.

One can instead prescribe the coefficient on constants and both linear transverse currents and omit transverse equivariance in the perfect-colour uniqueness argument. If neither prescription is imposed, a coboundary can survive already for \(\mathfrak{sl}_2\). With \(Q\) as above take \(m_p=\tfrac14 Q(\Omega(\partial_x^2\partial_y^2p)(U))\) and \(d_p(a f)=(a f)\cdot m_p\). The metric singlet makes \(d_p\) colour-equivariant. It has the required Cartan bidegree and total degree, and is a Lie coboundary. At \(p=x^2y^2,\ a=h,\ f=x\), it is \(4(:L_e[x]L_f[1]:-:L_e[1]L_f[x]:)\) for \(K(h,h)=2,\ K(e,f)=1\). The two polynomial endpoints detect this difference. The operator \(\partial_x^2\partial_y^2\) selects a weight component and violates the full transverse covariance.


For instance, this uniqueness applies to the nonsemisimple metric algebra \(\mathfrak{sl}_2\ltimes\mathfrak{sl}_2^*\) with its evaluation form. The adjoint and coadjoint summands are both spanned by brackets. The algebraic statement can therefore hold well beyond the simple pure-gauge examples.

The criterion is sharp if colour covariance means equivariance for the adjoint Lie algebra. For any nonperfect metric \(\mathfrak g\), choose \(0\ne z\in [\mathfrak g,\mathfrak g]^\perp=Z(\mathfrak g)\). The functional \(a\mapsto K(z,a)\) vanishes on brackets and takes a nonzero value somewhere, even when \(z\) is isotropic. For the second transvectant below the assignment
\[
      d_p(a t)=K(z,a)(z\otimes1)\odot(z\otimes(p,t)_2)
\]
is nonzero, has the required bidegree, and vanishes on constants and linear currents. Its image consists of invariant polynomials and it factors through the abelianization on colours, so \(d_p\) solves the homogeneous equation. Therefore perfection is necessary and sufficient for uniqueness of the polynomial family in this adjoint-equivariant class. For example the solvable four-dimensional algebra with \([h,u]=u,\ [h,v]=-v,\ [u,v]=z\) and \(K(h,z)=K(u,v)=1\), all other pairings zero, has precisely such an isotropic central witness. This sharpness concerns the freedom permitted by the projected equation and its markings. A physical Lagrangian may pick particular invariant tensors.

There is also an exact answer for a reductive colour \(\mathfrak g=\mathfrak s\oplus\mathfrak z\). The normalized difference vanishes on \(\mathfrak s\otimes A\) by the same induction. On \(\mathfrak z\otimes A_{\ge2}\) it can be any linear map with values in \(\operatorname{Sym}^2(\mathfrak z\otimes A)\) satisfying the stated transverse weights and covariance, extended by zero on the other modes. If further colour symmetries are imposed one keeps their equivariant maps.

For the last assertion it suffices to compute the invariants \(M^L\). Embed \(M\) into \((\mathfrak g\otimes\mathfrak g)\otimes B\) by symmetrization in characteristic zero. An invariant is killed by \(\operatorname{ad}_a^{(1)}+\operatorname{ad}_a^{(2)}\) and \(U_x\operatorname{ad}_a^{(1)}+V_x\operatorname{ad}_a^{(2)}\). Subtract \(V_x\) times the first identity from the second. Multiplication by \(U_x-V_x\) is injective on this free \(B\)-module. Thus each slot is individually central and \(M^L=\operatorname{Sym}^2(\mathfrak z\otimes A)\). Every central input acts trivially, so its cocycle equation against any input is exactly invariance of its value. Conversely, the announced maps into invariants factor through the abelianization on the inputs and are cocycles. The polynomial coefficient domain enters essentially in this proof. Collision-supported distribution coefficients can be annihilated by \(U_x-V_x\).

For a marked one-dimensional abelian summand with basis \(z\), let
\[
 (p,t)_2=p_{xx}t_{yy}-2p_{xy}t_{xy}+p_{yy}t_{xx}.
\]
The assignment \(z t\mapsto (z\otimes1)\odot(z\otimes(p,t)_2)\) is a local transverse-equivariant homogeneous ambiguity. It vanishes on linear currents and takes \(p=x^2,t=y^2\) to \(4(z\otimes1)^{\odot2}\). If equivariance under the full isometry group of the central summand is required, the central sign reversal acts as \(-1\) on its input and \(+1\) on this target, eliminating all such linear ambiguities. These are statements about the projected Ward problem with its specified marking.

## A mixed-root current in type \(A_2\)

Take \(K(a,b)=\operatorname{tr}_3(ab)\) and the two simple root matrices \(a=E_{12}, b=E_{23}\). Their bracket is the highest root vector \(c=E_{13}\). With \(p=x^2y,\ f=x,\ g=y\), we have \(P=x^2y/3\), \(Xx=-x^2/3,\ Xy=2xy/3\). For two linear inputs the two gradients are on opposite sides of the integration simplex. Their contraction gives
\[
 H(x,y)=-\frac{2}{3}\int_0^1(2a-1) (V_x+a(U_x-V_x))\,da
         =-\frac{U_x-V_x}{9},\qquad h(xy)=\frac{U_x-V_x}{9}.
\]
In \(\Xi_{E_{13}}\) the coefficient of \(E_{12}\otimes E_{23}\) is \(+1\), from \([E_{21},E_{13}]=E_{23}\). Its transpose is \(-1\), from \([E_{32},E_{13}]=-E_{12}\). Thus the coefficient of \(:L_{12}[1,0]L_{23}[0,0]:\) in the bare Ward residual is \(+\ell\nu/9\), and in \([E[x^2y]_\lambda J_{13}[xy]]\) it is \(-\ell\nu/9\). The opposite endpoint assignment has the opposite coefficient. Since \(\gamma=9\), the correcting coefficient in the \(s\)-normalization is \(+s^3/27\). To check \(\gamma\), the traceless \(3\times3\) Cayley–Hamilton identity gives \(p_4=p_2^2/2\), and summation over the adjoint weights gives \(6p_4+6p_2^2=9p_2^2\). The root pair is present only once the calculation sees beyond a single root \(\mathfrak{sl}_2\). [Reproducible matrix and endpoint calculations](check_colour.py) · [Exact coefficients](CHECKS.json)
