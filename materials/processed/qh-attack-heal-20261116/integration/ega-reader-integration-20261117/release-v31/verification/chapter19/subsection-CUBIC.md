### The cubic Ward identity on the transverse plane {#ch19-cubic-ward-identity}

Consider the formal vacuum algebra of pure self-dual Yang–Mills theory coupled to its anomaly-cancelling axion. In type \(A_2\) take gauge algebra \(\mathfrak{sl}_3\) with \(K(a,b)=\operatorname{tr}_3(ab)\). The polynomials in \(x,y\) label Taylor modes transverse to the celestial line. Insert a closed axion current \(E[x^2y]\) and two positive-helicity gauge currents, \(J_{12}[x]\) followed by \(J_{23}[y]\). The subscripts on the gauge currents denote the matrix units \(E_{ij}\). Their colours bracket to \(E_{13}\), so their tree bracket contains \(J_{13}[xy]\). When the axion at \(z\) approaches this highest-root current at \(w\), what is the coefficient of the normal product \(:L_{12}[1,0]L_{23}[0,0]:\) in the simple pole at cubic order in the axion coupling \(s\)? The two \(L\)'s have negative helicity. The first carries the transverse label \(x\), the second the constant label.

Write \(E[p]_{(0)}J_c[t]\) for the coefficient of \(1/(z-w)\) in the product \(E[p](z)J_c[t](w)\), with its output fields at \(w\). This is the positively oriented residue in \(z\), or the contour integral divided by \(2\pi i\). Keep the four-current brackets through order \(s^2\), with \(s\) the axion coupling and \(\nu\) the open one-loop coefficient. The cubic term has order \(s\nu\). For arbitrary positive currents \(J_a[f],J_b[g]\) in that order, the Jacobi identity equates the axion acting on their bracket to the sum of its actions on the two inputs. Their difference, with only the lower brackets inserted, is the residual. At tree level it turns a positive current into a negative current by differentiating its transverse label. At one loop it can differentiate each endpoint of the product. The difference of these operations determines the required pole.

Let \(A=\mathbb C[x,y]\), with \(f,g,t\in A\) and \(p\in A/\mathbb C\). Divide each nonconstant monomial \(x^m y^n\) of \(p\) by \(m+n\) to obtain the polynomial \(P\). The transverse derivative in the tree bracket is \(X=\{P,-\}\), with \(\{x,y\}=1\). In the ordered simplex coefficient \(\Phi(f,g)(U,V)\) of the [four-current product](#ch19-four-currents), \(U,V\) label the two output slots. Set
\[
\begin{aligned}
 H_p(f,g)={}&(X_U+X_V)\Phi(f,g)\\
            &-\Phi(Xf,g)-\Phi(f,Xg).
\end{aligned}
\]
These are the three nestings in the Jacobi identity with the closed input. The outer \(E\) has regular products with the negative and axion fields in the lower brackets. Two negative fields also have regular mutual product. Hence the surviving term has a simple pole and two negative-current outputs, independent of the two longitudinal bracket variables.

A polynomial at two endpoints carries a left action of \(f\) by \(f(U)\) and a right action by \(f(V)\). To compensate for \(H_p\), look for a linear map \(h_p:A\to A\otimes A\) with
\[
\begin{aligned}
 H_p(f,g)={}& f(U)h_p(g)-h_p(fg)\\
             &+h_p(f)g(V).
\end{aligned}
\]
The simplex coefficient is a Hochschild cocycle for precisely these endpoint actions. Differentiating the cocycle identity shows that \(H_p\) is one as well. Prescribe \(h_p(1)=h_p(x)=h_p(y)=0\). For a monomial \(q\) and a final letter \(v=x\) or \(y\), the equation now reads
\[
 h_p(qv)=h_p(q)v(V)-H_p(q,v).
\]
Does it matter which letter is taken last? Applying the cocycle identity, the difference on \(qxy=qyx\) reduces to \(-q(U)\bigl(H_p(x,y)-H_p(y,x)\bigr)\). In the two linear slots, direct integration of the simplex identifies the parenthesis with the integral of \(\operatorname{div}X\) on the segment from \(V\) to \(U\). A Hamiltonian vector field preserves area, so the difference is zero. Adjacent interchanges now give one value on every monomial. The cocycle identity extends the equation from a linear last input to an arbitrary polynomial. Two such primitives differ by an endpoint derivation zero on both coordinates, so they coincide. Reversing the simplex and applying this uniqueness gives \(h_p(t)(V,U)=-h_p(t)(U,V)\).

To put the colours back, use the inverse form \(\Omega=\sum_i u_i\otimes u^i\). For a colour \(c\) put \(\Xi_c=\sum_i u_i\otimes[u^i,c]\). Let \(Q\) assign each tensor factor its polynomial at the indicated endpoint and take the normally ordered product of the two negative currents \(L\). With this choice of Taylor currents, the oriented simple pole through cubic order is
\[
\begin{aligned}
 &E[p]_{(0)}J_c[t]\\
 &=sL_c[Xt]\\
 &\quad-\tfrac12s\nu\,Q(\Xi_c h_p(t))
        \pmod{s^4}.
\end{aligned}
\]
The first summand is linear in the negative current. The cubic summand lies in the symmetric square of the negative currents with polynomial transverse labels.
The half and the sign are fixed by the Ward equation. For positive colours \(a,b\) set \(C_{ab}=(\operatorname{ad}_a\otimes\operatorname{ad}_b)\Omega\). The bare residual, in units of \(s\nu\), is \(Q(C_{ab}H_p(f,g))\). If \(\chi_c(t)\) is a proposed correction in the same units for fixed \(p\), its contribution is
\[
\begin{aligned}
 &(\delta\chi)(af,bg)\\
 &=\chi_{[a,b]}(fg)\\
 &\quad+R_{b,g}\chi_a(f)-R_{a,f}\chi_b(g).
\end{aligned}
\]
The tree action is \(R_{a,f}L_d[t]=L_{[a,d]}[ft]\). It acts on a pair of negative currents by the Leibniz rule. Under the identification \(u\otimes v\mapsto uK(v,-)\), the tensors \(\Xi_c\) and \(C_{ab}\) become \(\operatorname{ad}_c\) and \(-\operatorname{ad}_a\operatorname{ad}_b\). In particular \(\Xi_{[a,b]}=C_{ba}-C_{ab}\). Substitution of \(\chi_c(t)=Q(\Xi_c h_p(t))\) in all three terms gives two copies of \(Q(C_{ab}H_p(f,g))\). The second copy comes from reversing both colours and both endpoints in the symmetric output. This gives the factor \(-1/2\) and cancels the residual for either ordering of the currents. Translation gives the identity on every longitudinal derivative.

For the three currents in type \(A_2\), take \(p=x^2y\) and \(f=x,\ g=y\). Now \(Xx=-x^2/3\) and \(Xy=2xy/3\). In the two linear slots the integral becomes
\[
\begin{aligned}
 H_p(x,y)&=-\tfrac23\int_0^1(2a-1)z_{a,x}\,da\\
          &=-\tfrac19(U_x-V_x),
\end{aligned}
\]
where \(z_a=V+a(U-V)\). The recursion gives \(h_p(xy)=(U_x-V_x)/9\). Setting \(U=V\) at the outset would have lost the entire coefficient.

The linear part of the axion–highest-root pole is \(sL_{13}[x^2y]/3\), since \(X(xy)=x^2y/3\). For its quadratic part, \([E_{21},E_{13}]=E_{23}\) gives coefficient \(1\) on \(E_{12}\otimes E_{23}\) in \(\Xi_{E_{13}}\). The transposed tensor has coefficient \(-1\). Multiplying by \(h_p(xy)\) and taking the normal product gives \(2/9\) on \(:L_{12}[1,0]L_{23}[0,0]:\). The factor \(-s\nu/2\) in the pole makes its coefficient \(-s\nu/9\).

The residual formed from the lower brackets is computed separately. Put \(H_i=E_{ii}-E_{i+1,i+1}\). The \(E_{12}\otimes E_{23}\) coefficient in \(C_{E_{12},E_{23}}\) is \(\operatorname{tr}_3(H_1H_2)=-1\), and the reversed tensor is absent. Multiplying by \(H_p(x,y)\) gives \(s\nu/9\) on the same normal product, exactly what the cubic pole cancels. To convert this to the axion coupling, put \(p_j=\operatorname{tr}_3(a^j)\). Cayley–Hamilton gives \(p_4=p_2^2/2\), and the adjoint fourth trace is \(6p_4+6p_2^2=9p_2^2\). Thus \(\gamma=9\) and \(\nu=-s^2/3\). The lower residual is \(-s^3/27\) and the requested simple-pole coefficient is \(+s^3/27\). Moving the \(x\)-jet onto the other root current reverses its sign.

Both incoming gauge currents can themselves carry derivatives in both transverse directions. For \(\mathfrak{sl}_2\) in the trace normalization above, take \(p=x^4y\) and positive currents \(J_h[xy]\), \(J_e[xy^3]\). On \(:L_e[0,0]L_h[4,3]:\) the bare residual in units of \(s\nu\) is \(-154/225\). Since \(\gamma=8\), this lower residual is \(77s^3/300\). The correction contributes \(-77s^3/300\) to the three-term identity. Taking \(p=x^k,\ t=y^2\) instead returns the cubic term of the axis transport for every \(k\ge2\). In the opening case \(k=3\), the pole with \(J_e[y^2]\) has coefficient \(-s\nu/3\) on \(:L_h[0,0]L_e[1,0]:\). The two original gauge currents have bracket colour \([h,e]=2e\). Their factor of two gives \(-2s\nu/3\) in the Jacobi identity, cancelling the earlier residual \(2s\nu/3=-s^3/4\).

How much of this coefficient does the Ward identity determine? The cancellation used only Lie Jacobi and an invariant nondegenerate symmetric form to deal with the colours. It therefore works for any finite-dimensional metric Lie algebra over characteristic zero whose lower brackets give the stated bare residual. In the pure gauge theory with one axion the lower four-current source uses the quartic factorization \(\operatorname{Tr}_{\mathfrak g}(\operatorname{ad}_a^4)=\gamma K(a,a)^2\) and \(\nu=-3s^2/\gamma\). A theory with extra matter has its own lower brackets.

Keep the two-negative-current simple pole, its polynomial coefficients at \(U,V\), adjoint colour equivariance and full transverse \(\mathrm{SL}_2\) equivariance. On homogeneous inputs of degrees \(r=\deg p,\ j=\deg t\), the total output degree is \(r+j-4\). For \(j=0,1\), the smallest highest weight in the input tensor product is \(|r-j|\), already greater than the maximum output weight. Any difference of two solutions vanishes on these modes. At fixed \(p\) this difference is a Lie one-cocycle of \(\mathfrak g\otimes A\). If \(\mathfrak g=[\mathfrak g,\mathfrak g]\), the currents with labels \(1,x,y\) generate that Lie algebra. Indeed \([a q,b v]=[a,b]qv\) for a coordinate \(v\). Induction on the monomial degree therefore forces the difference to vanish everywhere. Prescribing the constant and both linear current values gives the same uniqueness argument for perfect colour without a symmetry assumption on the transverse variables.

If the colour algebra is not perfect, choose a nonzero \(z\in[\mathfrak g,\mathfrak g]^\perp=Z(\mathfrak g)\). Denote the symmetric product by \(\odot\), and put
\[
\begin{aligned}
 (p,t)_2={}&p_{xx}t_{yy}-2p_{xy}t_{xy}\\
            &+p_{yy}t_{xx}.
\end{aligned}
\]
Then \(at\mapsto K(z,a)(z\otimes1)\odot(z\otimes(p,t)_2)\) can be added to the correction in units of \(s\nu\). Its colour functional annihilates brackets and its two outputs are central, so its Ward differential vanishes. It is transverse-equivariant and has all the prescribed degrees. At \(p=x^2,\ t=y^2\) its scalar is \(4K(z,a)\), nonzero for a suitable \(a\), even if \(K(z,z)=0\).

For reductive colour \(\mathfrak g=\mathfrak s\oplus\mathfrak z\), this freedom lies entirely on the centre. Every allowed linear map on \(\mathfrak z\otimes A_{\ge2}\) into \(\operatorname{Sym}^2(\mathfrak z\otimes A)\), with the stated degrees and covariance in both polynomial inputs, gives a homogeneous correction, and these exhaust the choices. In fact invariance under \(a\otimes1\) and \(a\otimes x\) implies that the adjoint action in the first slot is killed by \(U_x-V_x\). This difference acts injectively on polynomial coefficients, so each slot must be separately central. If sign reversal of the central summand is also a required symmetry, the central input changes sign and the quadratic output keeps its sign, eliminating this freedom. Coefficients supported on the collision \(U=V\) require a separate argument.

The result reconstructs the \(EJJ\) identity at order \(s^3\) on the whole polynomial plane. At this order the other closed current brings an \(FJJ\) identity, and the three positive currents bring their own coupled equations. A cubic vertex algebra, a PBW basis over \(\mathbb C[s]/(s^4)\), and flatness of its derived chiral cuts require those further comparisons.
