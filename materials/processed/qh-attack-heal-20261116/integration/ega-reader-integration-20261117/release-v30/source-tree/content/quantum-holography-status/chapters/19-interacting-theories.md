# Recovering interactions from boundary operations

A boundary can fail to see a bulk field even when that boundary generates all the other boundary conditions. Consider a two-state boundary with one even state and one odd state. Let \(x\) be a bulk scalar, and let the odd operator which exchanges the two states be
\[
 Q=\begin{pmatrix}0&x\\x^2&0\end{pmatrix}.
\]
Its square is \(x^3\) times the identity. The differential on boundary operators is the supercommutator with \(Q\), and its square vanishes because \(x^3\) is scalar. Multiplication by \(x\) is a boundary, since \(Q E_{21}+E_{21}Q=x\,1\), where \(E_{21}\) is the elementary matrix. Yet \(x\) is a nonzero protected bulk operator. In the B-twisted Landau–Ginzburg theory with potential \(W=x^3\), the bulk equations for this sector impose \(3x^2=0\). How can a boundary on which \(x\) acts by zero distinguish this theory from one with potential \(x^4\)?

A product with three boundary inputs does it. The same calculation will distinguish three things one might hope to reconstruct. A higher product can determine an interaction coefficient. An action on all boundary conditions can recover a bulk algebra. An amplitude requires in addition a trace, or an independently prepared state. These distinctions persist when the boundary operators are fields and the positions of several insertions can collide. [Bulk actions and centres](#bulk-action-and-centre) · [States and amplitudes](#states-lines-and-caps)

## Reading a potential from a boundary {#ch19-boundary-potential}

Work locally over \(k[[x]]\), where the field \(k\) has characteristic zero. For any \(W\) with \(W(0)=W'(0)=0\), use \(W(x)/x\) as the lower left entry of \(Q\). This is a matrix factorization of \(W\). In its algebra of endomorphisms the identity and the odd matrix
\[
 \psi=\begin{pmatrix}0&1\\-W(x)/x^2&0\end{pmatrix}
\]
represent all cohomology. Indeed an even cocycle must be a scalar matrix. Odd cocycles are multiples of \(\psi\). The exact multiples of either generator have coefficient divisible by \(x\). For \(W=x^d\) with \(d\ge3\) the ordinary product is always \(\psi^2=0\) in cohomology. One can nevertheless insert \(\psi\) repeatedly, retaining the choices of primitive involved when an intermediate product is exact.

There is an efficient way to perform all these insertions. Introduce a formal parameter \(t\), replace the upper right entry by \(x+t\), and choose the lower left entry to be
\[
                  \frac{W(x)-W(-t)}{x+t}.
\]
This quotient is a formal power series. The linear term of the resulting matrix \(Q(t)-Q\) is \(t\psi\). Its square equation reads \(Q(t)^2=W(x)-W(-t)\). Thus the failure to deform the boundary within the *fixed* bulk is the scalar \(-W(-t)\). For \(W=x^3\) the second-order change of the lower left entry cancels the square of the first variation. At the next order the scalar \(t^3\) is left over. For \(W=x^4\) it is \(-t^4\).

In the convention \(d\alpha+\alpha^2\) for an odd boundary deformation, this gives a strictly unital minimal algebra with the following products for \(n\ge2\).
\[
 m_n(\psi^{\otimes n})
       =(-1)^{n+1}[x^n]W\;1 .
\]
There is only one nonunit input letter. Comparing the coefficient of \(t^n\) tests its unique ordered word of length \(n\). If an inner higher product yields the unit, every higher Taylor map with that unit as an input vanishes. These observations account for the full morphism equations between the minimal algebra and the matrix algebra. In particular the unit on the right of the display must be retained. An operation which discards scalar outputs loses every coefficient of the potential it was meant to reconstruct. At a quadratic critical point the same computation gives the Clifford square already at arity two. [Dyckerhoff, higher products of the stabilized residue field](https://arxiv.org/pdf/0904.4713)

A change of boundary coordinate has a precise meaning here. Let a second minimal algebra correspond to a potential \(V\). On a word of \(n\) odd letters a unital \(A_\infty\) map has odd output. Write \(F_n\) for its coefficient on the odd generator of the target, and \(F(t)=\sum_{n\ge1}F_nt^n\). Its morphism equations read \(W(-t)=V(-F(t))\), again coefficient by coefficient. If \(F_1\ne0\), this is an invertible formal change of coordinate. Thus retaining the actual input \(\psi\) and its higher Taylor coordinates determines all of \(W\). Forgetting that choice permits a formal change of variable. Both statements fix the value \(W(0)=0\).

## When two insertions can be distinguished {#ch19-ordered-insertions}

With two different odd insertions, a scalar deformation need no longer identify an ordered operation. Take \(W=x^3+xy^2\). A deformation with two commuting parameters \(s,t\) has scalar obstruction \(s^3+st^2\). The second monomial could have come from any of the three words with one \(x\)-letter and two \(y\)-letters. We can tell them apart by returning to the endomorphism differential before passing to its cohomology.

On the exterior algebra of a two-dimensional space let \(e_i\) denote exterior multiplication and \(c_i\) contraction, with \(e_i c_j+c_j e_i=\delta_{ij}\). For \(W=f(x)+xg(y)\) put
\[
 Q=xe_1+ye_2+(f(x)/x+g(y))c_1 .
\]
Assume \(f\) starts in degree at least three and \(g\) in degree at least two. The square is \(W\). In the endomorphism algebra choose closed representatives
\[
 A=e_1-(f/x^2)c_1-(g/y)c_2
\]
and \(B=e_2\). The differential sends \(c_1,c_2\) to \(x,y\). Order both closed letters before the contractions, with \(A\) before \(B\). Project to constant coefficients of \(1,A,B,AB\), and take the primitive of a scalar \(h(x)-h(0)\) to be \((h(x)-h(0))c_1/x\). Use \(c_2/y\) for a function of \(y\) in the same way. On the full two-variable Koszul complex first remove multiples of \(x\), then apply the \(y\) contraction at \(x=0\). These choices give an actual contracting homotopy. The two odd cohomology classes will be denoted by \(a,b\).

Now \(A^2=-f/x^2\) and \(BA=-AB-g/y\). The latter identity starts a homotopy on the ordered pair \(b,a\), while the pair \(a,b\) is already in the chosen order. Starting at \(b,a\) leaves \((g/y^2)c_2\) on the internal edge of the product tree. Multiplication on the right by \(B\) gives a scalar because \(c_2B=1-Bc_2\). Its constant part supplies the next operation. Any nonconstant part can continue on this edge by removing one further power of \(y\), with a minus sign. A factor multiplying this edge on the left produces no scalar. If two such internal edges meet, they give either zero or a multiple of \(c_1c_2\), killed by both projection and homotopy. The same reasoning on \(A^2\) uses \(c_1A=1-Ac_1\). Consequently the whole table on words of the two individual odd letters in arity \(n\ge3\) consists of
\[
\begin{aligned}
 m_n(a,\ldots,a)&=(-1)^{n-1}[x^n]f\;1,\\
 m_n(b,a,b,\ldots,b)&=(-1)^{n-1}[y^{n-1}]g\;1 .
\end{aligned}
\]
All other such words give zero. The algebra has also the even class \(ab\), whose insertions use the full tree transfer.

Thus in type \(D_4\), with \(f=x^3,\ g=y^2\), it is \(m_3(b,a,b)=1\). Both \(m_3(a,b,b)\) and \(m_3(b,b,a)\) vanish. With \(g=y^3\) the type \(E_7\) mixed word instead gives \(m_4(b,a,b,b)=-1\). One can measure the distinction by attaching matrices to the two inputs. For \(S=E_{12},\ T=E_{21}\) one has \(TST=E_{21}\) and \(ST^2=T^2S=0\). There is also the binary contribution \(ab(ST-TS)\). A noncommuting test of a Taylor coefficient need not be a deformation with zero curvature. Ordering the chosen closed representatives the other way moves the \(D_4\) mixed value to \(m_3(a,b,b)\). This change gives an equivalent minimal model of the same boundary differential algebra with the same commuting obstruction.

## Which bulk operators reach the boundary {#ch19-diagonal-and-trace}

The odd multiplication just calculated was an operation on a particular boundary. To recover \(x\) itself, let the boundary vary. The identity defect between two copies of the theory represents the operation of doing nothing to such a boundary. In one variable its matrix factorization has entries \(x-y\) and
\[
                  v(x,y)=\frac{W(x)-W(y)}{x-y}.
\]
Its square is \(W(x)-W(y)\). An even endomorphism commuting with this matrix is a scalar. Exact scalars form the ideal \((x-y,v)\). At an isolated critical point these two equations are a regular sequence, so each odd cycle is a boundary. On setting \(x=y\) one obtains \(v(x,x)=W'(x)\). Hence the endomorphisms of the identity in cohomology are exactly \(k[[x]]/(W')\), including the class of \(x\) lost by its unary action in the opening example. In several coordinates telescope the difference of the two potentials as \(\sum_i(x_i-y_i)v_i\). The corresponding Koszul factorization restricts to the full gradient equations. Compact generation identifies this calculation with the Hochschild cohomology of the boundary category. It computes the cohomology algebra of its derived centre. An identification of all its \(E_2\) operations requires a cochain comparison. [Dyckerhoff, the stabilized diagonal and its Hochschild invariants](https://arxiv.org/pdf/0904.4713)

A disk measures something else. Choose the coordinate volume \(dx\) and give the bulk the residue trace \(\tau_W(h)=\operatorname{Res}_0 h(x)\,dx/W'(x)\). On the one-variable factorization the supertrace of \((\partial_xQ)\psi\) is \(-W'(x)/x\). The disk with boundary insertion \(\psi\) has value \(-1\). Inserting a bulk field \(h\) as well gives \(-h(0)\), whether one brings \(h\) to that boundary or first takes the bulk residue against \(-W'/x\). The map in this direction uses Hochschild **homology**. In \(r\) variables its parity is \(r\bmod2\), while the identity endomorphisms above lie in even Hochschild cohomology. The choice of volume and the order of the supertrace fix the stated sign. [Dyckerhoff and Murfet, the Kapustin–Li pairing](https://arxiv.org/pdf/1004.0687) · [Polishchuk and Vaintrob, the boundary-to-bulk map](https://arxiv.org/pdf/1002.2116)

Even a change of coordinate that preserves the complete boundary algebra can change a numerical amplitude. Suppose \(W(x)=V(\phi(x))\). Substitution in the one-variable residue gives
\[
 \tau_V(h)=\tau_W\big((h\circ\phi)(\phi')^2\big).
\]
One factor of \(\phi'\) comes from the volume and the other from the derivative of the potential. For the traces in the two standard coordinates to agree on every bulk insertion, perfectness of the residue pairing requires \((\phi')^2=1\) modulo \(W'\). Agreement also on the normalized odd disk insertion requires \(\phi'(0)=1\). At a critical point of multiplicity \(d-1\), these conditions say \(\phi=x+O(x^d)\). In characteristic zero this occurs for a pair of order-\(d\) potentials precisely when they agree through degree \(2d-2\). Indeed dividing each potential by its leading multiple of \(x^d\) and taking the \(d\)-th root gives a unique tangent-to-identity normal coordinate. Their difference has order at least \(d\) precisely under this congruence. For \(d\ge3\), the potentials \(x^d\) and \(x^d+c x^{2d-2}\) with \(c\ne0\) give isomorphic marked-origin theories after a tangent coordinate change and identical Jacobi ideals. Their standard sphere traces of the unit are nevertheless \(0\) and \(-(2d-2)c/d^2\).

Sewing can fix a scalar even where the contributions of individual vacua diverge. Take the normalized family \(W_t=x^3/3-tx\), with monic derivative \(P=x^2-t\). In \(k[t,x]/(P)\) the residue extracts the coefficient of \(x\) from a reduced polynomial. The inverse pairing is the two-variable element \((P(x)-P(y))/(x-y)=x+y\). Indeed it is killed by \(x-y\), and integrating its first leg against \(1\) leaves \(1\). Closing the two legs gives the handle element \(2x\). At \(t\ne0\) the two simple vacua have sphere weights \(1/(2\sqrt t)\) and \(-1/(2\sqrt t)\), in a splitting field. At collision the sum with an \(x\) insertion still equals one. The genus-one vacuum value is \(2\). The genus-three value is the coefficient of \(x\) in \((2x)^3\), namely \(8t\). For general monic \(P=W'\), division by \(P\) makes the same difference quotient the inverse pairing and \(P'\) the handle, even on the discriminant. Thus a sphere measurement and its sewing can stay defined when separate simple-vacuum amplitudes cease to exist.

Which critical point is being observed when the interaction varies? In the family
\[
                 W_s=x^3+xy^2(y+s)
\]
the ordered cubic mixed operation above equals \(s\), and the quartic mixed operation equals \(-1\). At \(s=0\) the Jacobi ring has dimension seven. At a generic \(s\) the equations become \(3x^2+y^2(y+s)=0\) and \(xy(3y+2s)=0\). The origin now has length four. One simple critical point lies at \((0,-s)\), and two more, over a splitting field, lie at \(y=-2s/3\). At the last pair \(x^2=-4s^3/81\) and \(W_s=-2x^3\ne0\). One can account for all seven dimensions in the relative algebra. After eliminating \(x^2\), its scalar part is defined by \(y^3(y+s)(3y+2s)\) and its \(x\)-part by \(y(3y+2s)\). Completing at the single boundary origin retains only four of these seven dimensions. Fixing the value of the potential also matters. Where \(W_s\) is invertible, \(Q/(2W_s)\) contracts the identity of a factorization of \(W_s\). A varying critical scheme, its zero critical fibre and a chosen boundary condition can therefore give different answers to the same dimension count.

## A boundary field measures a Jordan block {#ch19-chiral-screening}

The weight-zero chiral fields give another route to the Jacobi ring. It starts from even free fields \(\beta_i,\gamma_i\) and odd fields \(b_i,c^i\), with brackets \([\beta_i{}_\lambda\gamma_j]=[b_i{}_\lambda c^j]=\delta_i^j\). Give \(\gamma_i,b_i\) weight zero and \(\beta_i,c^i\) weight one. For the gradient \(f_i=\partial_iW\) take the zero mode of the screening current \(\sum_i:f_i(\gamma)c^i:\) as differential \(D\). The current has regular product with itself, since none of its constituents contract. Its zero mode squares to zero, commutes with translation \(T\), and differentiates every vertex product. On the zero-weight generators \(Db_i=f_i\) and \(D\gamma_i=0\), giving exactly the bulk Koszul complex. At positive weight an insertion can contract twice before its residue is taken. [Malikov and Schechtman, chiral Koszul complexes](https://arxiv.org/pdf/1406.0284) · [Dedushenko, Landau–Ginzburg chiral algebras](https://arxiv.org/pdf/1511.04372)

To see the extra operation, take one screening polynomial \(f=x^3\), so the potential in this normalization is \(x^4/4\). Write \(x=\gamma_0\) for the single creation mode, \(y=T\gamma\), \(p=\beta_{-1}\), \(\theta=b_0\), and \(\eta=c_{-1}\) acting on the vacuum. Then
\[
 D(p\theta)=x^3p+3x^2\theta\eta-6xy .
\]
The first two terms follow from the action on generators. The last uses both contractions, against \(p\) and against \(\theta\), while the remaining \(\gamma\) supplies its linear Taylor term \(y\). At weight one and cohomological degree zero the cycles are generated as a \(k[x]\)-module by \(J=xp+3\theta\eta\) and \(y\). Applying \(D\) to \(T\theta\) gives \(3x^2y\), and the displayed formula gives the other relation \(x^2J=6xy\). The sole remaining incoming basis state, \(y\theta\), gives \(x^3y\), a multiple of the first relation.

It follows that \(J,xJ,x^2J\) form a chain of length three for multiplication by \(x\), with \(x^2J=6xy\ne0\). The vector \(y-xJ/6\) forms a second chain of length one. Removing the double contraction gives instead \(x^2J=x^2y=0\), two chains of length two. Both answers have four degree-zero states. The process of inserting the same coordinate a second time distinguishes them. For \(f=x^m\), \(m\ge2\), the two relations become \(x^{m-1}y=0\) and \(x^{m-1}J=m(m-1)x^{m-2}y\), with \(J=xp+m\theta\eta\). Their Smith factors have degrees \(m-2,m\), rather than the repeated degree \(m-1\) of the commutative symbol. Here the measured action is a creation mode. Taking a mode of an arbitrary normally ordered polynomial in \(\gamma\) is a different operation.

The coupled \(E_7\) potential supplies the same distinction without splitting into two one-variable theories. Write \(X,Y\) for the zero-coordinate modes and \(Y_1=T\gamma_Y\). Restore a parameter \(h\) in each elementary contraction and divide the screening zero mode by \(h\). The normalized zero mode is integral, since every residue term uses at least one contraction. At weight one, both \(h=0\) and \(h\ne0\) have dimensions \(8,16,8\) in degrees \(-1,0,1\). The degree-zero Jordan lengths of \(Y\) change from \((4,4,3,3,1,1)\) to \((5,4,3,2,2)\). Take the Euler current \(J\) whose terms \(X\beta_X,Y\beta_Y,b_Xc^X,b_Yc^Y\), in the stated creation order, have coefficients \(3,2,6,7\). Applying the coordinate mode \(Y\) four times to \(J\) gives \(28h[Y^3Y_1]\). Taking the single creation mode of the composite field \(:\gamma_Y^4:\) gives \(4h[Y^3Y_1]\). The output class is nonzero. Both operations have the same classical polynomial name. The distinction comes from which contractions can occur before the residue is taken.

## A gauge algebra and an independent sphere measurement {#ch19-gauge-and-sphere}

A dynamical gauge field changes even the binary products. Take \(n\) Weyl pairs with \([p_i,x_j]=\hbar\delta_{ij}\), gauged by a rank-\((n-1)\) torus. Its \(a\)-th generator has charges \(1\) on the \(a\)-th hypermultiplet and \(-1\) on the last. Fix the moment map \(x_ap_a-x_np_n=\zeta_a\). In the invariant algebra put \(z=x_np_n\), \(X=\prod_i x_i,\ Y=\prod_i p_i\). Since an invariant Weyl monomial has the same difference of exponents in every species, these generators, with their powers in normal order, span the reduction. Their products are
\[
\begin{aligned}
 [z,X]&=\hbar X,&[z,Y]&=-\hbar Y,\\
 XY&=P(z),&YX&=P(z+\hbar),
\end{aligned}
\]
where \(P(z)=z\prod_{a<n}(z+\zeta_a)\). Independence follows by realizing \(X\) as a shift \(t\) with \(tq(z)=q(z-\hbar)t\), and \(Y=P(z+\hbar)t^{-1}\). At zero moment parameter and \(n=3\), the commutator \([Y,X]\) is \(3\hbar z^2+3\hbar^2z+\hbar^3\). All three terms are measured in one ordering of the product. [Gaiotto and collaborators, quantized Higgs-branch operator algebras](https://arxiv.org/pdf/2308.15198)

The corresponding chiral reduction needs a cancellation before it defines a differential. The charged currents \(t_i=:\gamma_i\beta_i:\) give gauge currents \(J_a=t_a-t_n\). Their double pole is \(-\hbar^2M_{ab}\) in pole units, where \(M_{ab}=\delta_{ab}+1\). An independent Heisenberg field with the opposite double pole cancels it. Otherwise squaring the gauge differential on the antighost produces a nonzero derivative of the ghost. For \(n=3\) the invariant chiral fields \(\mathsf X=:\prod_i\gamma_i:\) and \(\mathsf Y=:\prod_i\beta_i:\) have a cubic pole \(-\hbar^3\) and a double pole \(\hbar^2\sum_i t_i\). Their simple pole has both the uncontracted two-species products and \(\hbar^2\sum_i:(T\gamma_i)\beta_i:\). The latter comes from Taylor expanding the third species after two contractions. It cancels the gauge variation of the former. Passing to an associative algebra of zero modes must respect this differential and its cohomology. [Kuwabara, hypertoric vertex algebras](https://arxiv.org/pdf/1706.02203)

Which expectation functional should be applied to the associative products? A finite-dimensional module can live where a one-dimensional vacuum character is impossible. For example set \(\hbar=1,\ P(z)=z(z-2)(z-5)\). On two states let \(z\) have eigenvalues \(0,1\), \(X\) raise the first state to the second, and \(Y\) return the second to four times the first. Both \(XY=P(z)\) and \(YX=P(z+1)\) hold. The positive metric \(\operatorname{diag}(1,4)\) makes \(Y\) the adjoint of \(X\), and the normalized matrix trace gives \(2\) on both products. A character would force \(X=Y=0\) and require a pair of roots a unit apart. This polynomial has no such pair.

There is another experiment, performed directly in the three-dimensional \(\mathcal N=4\) gauge theory. On a sphere of radius one, at zero Fayet–Iliopoulos parameter, use a real integration variable \(d\sigma_a\) for each gauge factor and one factor \(F(t)=(2\cosh\pi t)^{-1}\) per hypermultiplet. The first \(n-1\) arguments are \(\sigma_a+m_a\), and the last is \(-\sum_{a<n}\sigma_a+m_n\). With the Fourier kernel \(\exp(2\pi iMt)\), \(F\) is its own Fourier transform. Integrating over the \(\sigma_a\)'s makes all dual variables equal. Hence, for \(M=\sum_i m_i\),
\[
\begin{aligned}
 Z_n(M)&=\int_{\mathbb R}e^{2\pi iMt}F(t)^n\,dt\\
       &=\frac{\Gamma(n/2+iM)\Gamma(n/2-iM)}
                    {2\pi\Gamma(n)} .
\end{aligned}
\]
The substitution \(q=e^{2\pi t}\) gives the second equality by the beta integral. With three massless hypermultiplets this fixes the unnormalized value \(Z_3(0)=1/16\), including the measure. The commutator of line operators alone has no such unit. In particular the two-state trace, whose value on the identity is one by definition, does not fix this spherical amplitude. [Dedushenko, Pufu and Yacoby, localization of the protected sector](https://arxiv.org/pdf/1610.00740)

There is an insertion test in the same sphere experiment. Set \(\hbar=1\), keep the radius and Fourier conventions just used, and let the real Fayet–Iliopoulos shifts be \(\nu_j\), with \(\nu_n=0\) and all the mass on the last species. The oscillator insertion \(x_jp_j+1/2\) is represented by \(i(t-\nu_j)\). Indeed differentiating one hypermultiplet factor before Fourier transformation inserts this symmetrically ordered oscillator operator. Thus \(x_ap_a-x_np_n=-i\nu_a\), so the algebraic parameters are \(\zeta_a=-i\nu_a\), and \(z\) on the last species goes to \(it-1/2\). The measure for a neutral insertion is \(e^{2\pi iMt}\prod_j F(t-\nu_j)\,dt\). The charged one-point functions vanish by the residual circle action. Moving \(t\) down by \(i\) shifts the inserted \(z\) to \(z+1\). The zeros of \(P(z)\) cancel the poles crossed by the contour, giving the precise relation \(I(XY)=(-1)^n e^{2\pi M}I(YX)\) for the unnormalized sphere functional \(I\). This proves the rule on the generators and therefore on every word.

For three massless species and zero shifts this gives the normalized expectation \(\langle XY\rangle=1/4-3/\pi^2\), and \(\langle YX\rangle=-\langle XY\rangle\). To recover the positive two-state trace above requires changing the experiment. Continue the two shifts to \(-2i,-5i\), taking the two residues in that order, and then normalize at the complex mass \(M=i/2\). The twist has become one and the residues select precisely the two weights \(z=0,1\) with equal coefficients. Reversing the residues retains three additional weights. The real massless measurement belongs to the fibre with \(P=z^3\). The ordered residues reach the different fibre \(P=z(z-2)(z-5)\) of the two-state example. There the order of the contours specifies the measured state. [Protected circle traces and their parameter conventions](https://arxiv.org/pdf/2308.15198)

## Four celestial currents at the first quantum order {#ch19-four-currents}

The gauge screening was defined by an actual field with a regular self-product. In a nonlinear celestial algebra the proposed products must first pass the Jacobi identity, including the terms from successive contractions. Consider pure self-dual Yang–Mills theory coupled to its anomaly-cancelling axion. Its two gauge helicities give even fields \(J_a[r]\) and \(L_a[r]=\widetilde J_a[r]\). The axion gives \(E[r]\) and \(F[r]\). The transverse Taylor index is \(r=(r_1,r_2)\in\mathbb N^2\). The \(E\) tower starts at nonzero \(r\). This field content is different from the single untilded open tower of holomorphic Chern–Simons theory in the four-dimensional Wess–Zumino–Witten example. Self-dual gravity also has different vertices, with a Poisson bracket of transverse Hamiltonians. [The celestial current product](#ch14-celestial-yangian-like) · [Fernández and Paquette, the four towers](https://arxiv.org/pdf/2412.17168v2)

Let \(K\) be the basic form on the gauge Lie algebra, normalized by \(\operatorname{Tr}_{\rm ad}(\operatorname{ad}_a\operatorname{ad}_b)=2h^\vee K(a,b)\). We assume the adjoint fourth trace is \(\gamma K(a,a)^2\) on the diagonal. Set the axion coupling to \(s\) and the open-loop coefficient to \(\nu=\hbar/(16\pi^2)=-3s^2/\gamma\). We first work over \(\mathbb C[s]/(s^3)\). Thus two axion vertices and one open loop appear at the same order. Longitudinal poles are written in the bracket variable \(\lambda\), and \(T\) translates the output along the celestial line.

For incident indices \(r,t\) put \(d=r_1t_2-r_2t_1\), \(w=r+t-(1,1)\), and \(N_r=r_1+r_2\). An output with a negative index vanishes. The two genuinely nonlinear terms use one ordered scalar. For polynomials \(f,g\) on the transverse plane take two independent endpoints \(U,V\), write \(z_a=V+a(U-V)\). On the triangle \(\Delta=\{0<b<a<1\}\) put \(f_a=\nabla f(z_a)\) and \(g_b=\nabla g(z_b)\). Set
\[
 \Phi(f,g)=-\int_\Delta \det(f_a,g_b)\,db\,da .
\]
The integral evaluates a polynomial over a simplex. In particular \(\Phi(x,y)=-1/2\), whereas \(\Phi(x^2,y)=-(2U_1+V_1)/3\). The latter coefficients remember which of the two output currents receives the transverse derivative. Write \(\Phi_{kl}\) for the coefficient of \(U^kV^l\) when the input monomials are \(x^r,x^t\), using multi-index notation. With \(f_{ab}{}^c\) the structure constants, let \(C_{ab}^{ij}=K^{pq}f_{ap}{}^i f_{bq}{}^j\). Define \(Q_{ab}\) by summing the monomial \(:J_i[k]L_j[l]:\) with coefficient \(\Phi_{kl}C_{ab}^{ij}+\Phi_{lk}C_{ab}^{ji}\), and \(P_{ab}\) by summing \(:L_i[k]L_j[l]:\) with coefficient \(\Phi_{kl}C_{ab}^{ij}\). Both sums have \(k+l=w\). The order \(J,L\) is part of the first definition.

The bracket of two positive currents has a classical gauge term, an axion term and two open one-loop terms. In this paragraph write \(J_{[a,b]}\) and \(L_{[a,b]}\) for a current with the bracket colour. Set
\[
\begin{aligned}
 H_{rt}&=dF[w]+N_r T E[r+t]\\
       &\quad+(N_r+N_t)\lambda E[r+t] .
\end{aligned}
\]
Dropping the term of an absent field, the bracket is
\[
\begin{aligned}
 &[J_a[r]{}_\lambda J_b[t]]\\
 &=J_{[a,b]}[r+t]\\
   &\quad-s K_{ab}H_{rt}+\nu Q_{ab}\\
   &\quad+\nu\,\frac{h^\vee d}{6}
               (T+2\lambda)L_{[a,b]}[w] .
\end{aligned}
\]
The remaining nonzero orientations are
\[
\begin{aligned}
 [L_a[r]{}_\lambda J_b[t]]
       &=L_{[a,b]}[r+t]+\nu P_{ab},\\
 [E[r]{}_\lambda J_a[t]]
       &=s\,\frac{d}{N_r}\,L_a[w].
\end{aligned}
\]
For the fourth tower put \(c_{rt}=1+N_t/(N_r+2)\). Then
\[
 [F[r]{}_\lambda J_a[t]]
       =-s(T+c_{rt}\lambda)L_a[r+t].
\]
All pairs among \(L,E,F\) have regular products to this order. Reversing a bracket substitutes \(-\lambda-T\) in the opposite orientation, with \(T\) acting on the whole output. The four formulas therefore determine all pairs and all translated inputs. The factor \(1/N_r\) occurs only for the allowed, nonconstant \(E[r]\).

There are two independent cancellations. In the quadratic output, the two endpoints of \(\Phi\) act on different factors. Applying the product rule to its Hochschild differential leaves an integrand alternating three covectors of the two-dimensional transverse plane, hence zero. Antisymmetrizing with the adjoint matrices gives the quadratic Jacobi terms, for two positive fields and one negative field as well as for three positive fields. In the linear three-positive output, the open residual is the polarized adjoint fourth trace. The two axion vertices give the three products of pairings. Both multiply the same expression in translations and longitudinal brackets. Polarization gives the open prefactor \(\nu\gamma/3\) against the closed prefactor \(s^2\), and their sum vanishes. Jacobi identities with an external axion reduce to its displayed tree action at the retained order, and the regular \(L,E,F\) pairs remove the other possible nestings. The fourth-trace condition is essential for this pure theory with a single axion. For the defining trace on \(\mathfrak{sl}_4\), the Cartan elements with entries \((1,-1,0,0)\) and \((1,1,-1,-1)\) would require coefficients \(10\) and \(8\), respectively. [Costello and Paquette, the gauge anomaly in the celestial algebra](https://doi.org/10.1103/PhysRevLett.129.231604)

This calculation supplies more than a consistency test on two selected fields. Assign each generator of transverse degree \(r\) the filtration degree \(N_r+2\). Every bracket in the table lowers the sum of the input degrees, including the quadratic terms. Ordering a pair of generators therefore adds only smaller terms. On triples the two possible reorderings differ by the Jacobi identity just computed. The nonlinear Poincaré–Birkhoff–Witt construction gives a vertex algebra free over \(\mathbb C[s]/(s^3)\) on the ordered monomials in translated generators. The leading rewrites are monic, so the construction requires no division by \(s\). The resulting vertex operators define a translation-equivariant chiral algebra on the affine line with this coefficient ring. Its chiral Chevalley chains give a factorizing coalgebra, and restricting to consecutive cuts before taking cobar makes it an augmented associative chiral algebra. The empty-configuration unit and the vacuum on the occupied line are supplied by their respective operations. [De Sole and Kac, nonlinear conformal algebras and PBW](https://arxiv.org/pdf/math-ph/0312042) · [Francis and Gaitsgory, chiral Koszul duality](https://arxiv.org/pdf/1103.5803)

One projection admits an all-order scalar calculation independently of this finite-order construction of the four fields. Take a negative field first and a positive one second, labelled by monomials \(f,g\) of total degrees \(A,B\ge m\). Select \(m+1\) negative output fields, with the first \(m\) transverse degrees zero. At loop \(m\) the last output then carries all the remaining degree. Let \(\mathcal D=\partial_{x_1}\partial_{y_2}-\partial_{x_2}\partial_{y_1}\), acting on \(f(x)g(y)\), and let \((a)_m\) denote the falling factorial. In the units in which \(\nu^m\) multiplies the colour word, the terminal output is the coefficient of its monomial in
\[
 -\frac{(\mathcal D^m(f\otimes g))|_{y=x}}
        {m!(A)_m(A+B-m+1)_m}.
\]
The determinant contraction is forced up to a scalar by transverse \(SL_2\) covariance on the two homogeneous input spaces. Testing \(x_1^A,y_2^B\) evaluates the scalar by the angular beta integral. At two loops, for \(f=x_2^3,\ g=x_1^2\), move the sole degree-one output through the three slots. The ordered values are \(-1/4,-1/6,-1/12\), with the displayed terminal formula giving the last value. Summing the slots would hide their different matrix words. This all-order statement selects a specific output in the mixed gauge channel. [Ordered angular and mixed-helicity products](#ch14-celestial-reconstruction)

## A closed current at the next order {#ch19-closed-current}

The first order outside this construction can be tested on a single pair of transverse directions. Work in \(\mathfrak{sl}_2\) with \(K(h,h)=2\), \(K(e,f)=1\). Insert \(E[3,0]\), \(J_h[0,1]\), \(J_e[0,1]\). The inner axion bracket produces a negative current. Its bracket with the other positive current carries the unequal one-loop weights \(-1/3\) and \(-2/3\) from the simplex. In the formula obtained by giving the first \(E\) index a shift by \(-(1,1)\), this input acquires a negative second component, so its proposed contribution is zero. But the coefficient of \(:L_h[0,0]L_e[1,0]:\) in the Jacobiator, with the left nested bracket minus the two right-hand terms of the Jacobi identity, is \(2s\nu/3=-s^3/4\). The opposite order of the two assigned jets gives the other colour monomial with the opposite sign. Both are independent in the classical PBW algebra. The discrepancy first obstructs this prescription on passing from the quotient modulo \(s^3\) to the quotient modulo \(s^4\). [Fernández and Paquette, the higher axion-current term](https://arxiv.org/pdf/2412.17168v2#page=52)

The negative-current action explains how this particular coefficient is repaired. Restrict positive inputs to \(J_a[0,n]\), and retain negative fields only along the first transverse axis. The quotient is well defined because a negative input with positive second index has output second indices summing to that index plus \(n-m\) at loop \(m\le n\). Some output must still have positive second index. On an axis input the only power remaining in the quotient is \(m=n\). Setting all nonzero jets to zero would fail, since the action on a first jet can already give a quadratic zero-jet output.

Use a finite-dimensional quadratic Lie algebra and the metric \(\kappa=-2K\). Write \(X_p\) for the raised negative-current coordinate at first-axis degree \(p\). Let \(X(u)=\sum_{p\ge0}X_pu^p\) and \(C(u)=\partial_u(uX(u))\). With \(\epsilon=\hbar/(16\pi^2)\) define parallel transport by
\[
 \partial_u U_v=2\epsilon v\,\operatorname{ad}_{C(u)}U_v,
 \qquad U_v(0)=1.
\]
In these coordinates the positive current derivations \(D_{a,n}\) have series \(D_a(v)=\sum_n v^n D_{a,n}\) with
\[
 D_a(v)X(u)=\frac{(U_v(u)-1)a}{2\epsilon uv}.
\]
The numerator is divisible by \(\epsilon uv\). Vary the equation for \(U_w b\) by this action. The result is a divided difference of transports with parameters \(v,w\). Its apparent pole cancels since each transport preserves brackets. Its two variations in opposite orders give \([D_{a,m},D_{b,n}]=D_{[a,b],m+n}\). This constructs the current action at every order on the specified quotient.

The same transport gives a vector without losing central colours. Rescale the interval to \(0\le t\le1\), put \(C_t=\partial_t(tX(ut))\), and let \(U_q(t)\) solve the corresponding equation with \(2q\operatorname{ad}_{C_t}\) in place of the original coefficient. Define
\[
                  \Psi(q,u)=\int_0^1U_q(t)^{-1}C_t\,dt .
\]
Its adjoint is half the logarithmic \(q\)-derivative of \(U_q(1)\), but the vector integral also retains any central component. Pair its coefficient of \(q^m u^N\) with the current colour using \(\kappa\). This yields the closed extension term for \(E[m+N+1,0]\) with \(J_a[0,m+1]\), after restoring the simple-pole factor \(s\epsilon^m\). In particular the coefficient linear in the outgoing jet \(u\) is
\[
 [q^m u]\Psi=\frac{2(-2)^m}{(m+2)!}
                         (\operatorname{ad}_{X_0})^m X_1 .
\]
To obtain it, linearize the transport around \(X_0\). The remaining integral is \(2\int_0^1(1-t)\exp(-2qt\,\operatorname{ad}_{X_0})X_1\,dt\). Thus the first correction is \(-2[X_0,X_1]/3\). In the orthonormal compact three-colour coordinates \(\epsilon_{012}=1,\ K=-I/2\), it supplies the term missing in \(E[3,0]\) against \(J_b[0,2]\). The tree contribution there is \(2s L_b[2,1]\). The repaired quadratic contribution has coefficient \(-2s\epsilon/3\) on \(\epsilon_{bde}:X_d[0,0]X_e[1,0]:\) in that orientation. In the quotient the return term is a Chevalley–Eilenberg cocycle for the current action. At \(u=0\) the integrand fixes \(X_0\), so \(\Psi(q,0)=X_0\). The positive-loop correction therefore vanishes on the all-zero output in the balanced double-pole Ward calculation. In its ordered colour-chain class the earlier total double pole and derivative operator keep their values. On arbitrary incident and outgoing transverse jets the double-pole and derivative equations still have to be solved. The all-order construction controls this axis. A general order-\(s^3\) lift still has other brackets and Jacobi equations.

One can now take a tensor product, provided one specifies what the two modules share. Write \(A\) for the commutative polynomial algebra of negative-axis coordinates with its formal coefficient parameter. Modules with this same \(A\)-action have a diagonal current action on \(M\otimes_A N\), given by the Leibniz rule. The counit on the action algebra evaluates an operator at the constant \(1\). For independent backgrounds \(X_0^L,X_0^R\), however, evaluating the first nonlinear current action on their sum produces two cross commutators. For example on \(X_1\) the one-mode term is \(\epsilon[X_0,[X_0,a]]\). Taking \(X_0^L=e,\ X_0^R=f,\ a=h\) yields the extra \(4\epsilon h\). It disappears from the sum of the separate actions. Combining two independent physical lines would need a map dealing with this measured term as well as the closed cocycle. [Ordered transport and tensor products](#ch14-celestial-ordered-transport)

## Coefficients at a collision {#ch19-cut-coefficients}

The current calculations kept the transverse output positions distinct until the last step. The same precaution on the celestial line itself takes a geometric form. Above a separating configuration two groups of fields may be prepared independently. When several groups collide, the quantum chiral algebra supplies a complex of coefficients \(C_n\) on the configuration space, together with the maps that compare it to the two smaller groups on every separating open. A calculation of the space of positions alone would discard the fields carried by these maps.

On the affine line write \(z_1,\ldots,z_n\) for the coordinates in their word order. A cut between labels \(p\) and \(p+1\) separates the groups wherever
\[
                F_p=\prod_{i\le p<j}(z_i-z_j)
\]
is invertible. Let \(U_n\) be the union of these opens and \(Z_n\) its closed complement. For a quasi-coherent differential-module complex \(M\) on the affine configuration space, form the finite complex with term in degree \(j\)
\[
 K_n^j(M)=\bigoplus_{|S|=j}
                  M\left[(\prod_{p\in S}F_p)^{-1}\right] .
\]
Here \(S\) ranges over subsets of the \(n-1\) cuts. The empty subset contributes \(M\). Adding a cut \(a\) localizes the coefficient with sign \((-1)^{|\{s\in S:s<a\}|}\). The two orders of adding two new cuts cancel. On the summand of degree \(j\), the internal differential of \(M\) has sign \((-1)^j\). This augmented Čech complex is the fibre of restriction from all configurations to \(U_n\). For the actual factorizing chiral-chain coalgebra above, the reduced cobar coefficient is consequently \(K_n(C_n)[-1]\). Its multiplication uses the factorization maps on \(C_n\). [Associative products on configurations](#ch12-associative-products-on-configurations) · [Where successive collisions meet](#ch14-celestial-cut-support)

At three labels put \(u=z_1-z_3\), \(v=z_2-z_3\). The two equations generate \((u^2,uv)\). Its radical is \((u)\), so the complex simplifies, up to quasi-isomorphism, to \(M\longrightarrow M[u^{-1}]\). The Koszul complex on the two original equations would retain a redundant equation and different homology. Once the open set is known, it is the restriction of the chosen \(M\), with its internal differential, that determines the supported coefficient.

There is a scalar topological measurement one can make without choosing \(M\). Over \(\mathbb C\), intersect the diagonal components of \(Z_n\) in all possible ways. The intersection labelled by an equality partition \(\pi\) has complex codimension \(c=n-\#\pi\). The strictly intermediate intersections between the ambient space and this one form a finite poset. Its chains have a differential which deletes one entry at a time with alternating signs. If \(\beta_j(\pi)\) is the dimension of its reduced rational homology, the contribution of this intersection to \(H^k(U_n;\mathbb Q)\) has dimension
\[
                   \beta_{2c-k-2}(\pi)
\]
and Hodge weight \(2c\). One way to see the degree is to resolve the closed union by its intersections. Each affine intersection has compactly supported cohomology in a single degree. Grouping chains by their final intersection leaves precisely the reduced chain complex just described. Distinct pure weights prevent higher differentials between those rows. Localization and duality then give the cohomology of the complement. This calculation gives the dimensions of the weight-graded spaces. Cup products need further maps.

At six labels the interval below full collision has augmented chain dimensions \(1,33,97,66\) in degrees \(-1,0,1,2\), and its boundary ranks are \(1,32,63\). Thus it contributes two classes to \(H^7\) and three to \(H^6\), all in weight ten. A point count retains their signed difference, one. Removing singleton blocks from an intersection leaves the proper interval unchanged. Both ends of a nontrivial indecomposable configuration must be active. It follows that an \(r\)-label core occurs \(\binom{n-2}{r-2}\) times on \(n\) labels. Codimension \(c\) requires at most \(2c\) active labels. In degree \(k\ge3\) the interval dimensions give \(c\le k-1\), so an arity-independent finite calculation suffices. This explains how an assertion at every arity can follow from a finite list of complexes, while keeping the quantum coefficients out of a purely topological count.

In degree seven only codimensions four, five and six can contribute. For \(B_i=\binom{n-2}{i}\), with \(B_i=0\) if \(i>n-2\), the rational Betti number at every \(n\ge2\) is
\[
\begin{aligned}
 b_7(U_n)&=2B_4+28B_5+57B_6\\
          &\quad+28B_7+6B_8 .
\end{aligned}
\]
The weight-eight part has dimension \(B_6\) and the weight-twelve part dimension \(4B_5+5B_6\). The remaining classes have weight ten. To obtain the coefficients one takes the actual rational boundary ranks of the proper intersection intervals on at most twelve active labels. Exactly 102 of the 1,633 intervals in the degree-seven window contribute. At six labels the formula gives the same two classes found on the full-collision interval. Neither this Betti number nor its weight decomposition supplies the factorization map on a quantum \(C_n\).

A related homotopy appears in the two transverse coordinates around the line. On the punctured plane \(\mathbb A^2\setminus\{0\}\), take the ordered Čech algebra of \(D(x),D(y)\). Put \(\eta=[1/(xy)]\) in degree one. Then \(x\eta\) and \(\eta y\) vanish in cohomology. Their primitives can be taken as \((0,1/y)\) and \((-1/x,0)\) on the two charts. Taking their difference after multiplication at the two ends gives the unit \((1,1)\) modulo \((x,y)\). An occupied character evaluating both coordinates at zero cannot preserve that ternary operation. The excluded character would evaluate those functions and homotopies at the precise point removed from their domain. This is a separate issue from the augmentation at the empty configuration.

The same choice of charts gives actual higher operations at arbitrarily large arity. Project a degree-zero chart pair to the polynomial part of its second component. In degree one keep the Laurent monomials with both exponents negative. A primitive with nonnegative \(y\) exponent is placed in the first chart with a minus sign, and one with negative \(y\) and nonnegative \(x\) exponent in the second chart. Write \(b_n\) for the operations on the shifted space in which \(b_2(\sigma a,\sigma b)=(-1)^{|a|}\sigma(ab)\). For \(q\ge1\), feed the word with endpoints \(x^qy^{q-1},y\) and \(q\) copies of \(\eta\) between them. Its \(b_{q+2}\) is \((-1)^{q-1}\sigma1\). On the surviving branch the first \(q-1\) Laurent factors stay in the first chart. The last moves into the second, and multiplication by \(y\) gives the constant. Keeping the operations only up to any fixed \(N\ge3\) leaves a nonzero unit in the length-\(N+2\) identity for a suitable word. This concerns the specific transferred presentation. The original two-chart differential algebra, with its differential and ordinary product, already encodes all of these homotopies.

## Reconstructing an interacting comparison {#ch19-interacting-comparison}

The opening cubic example gave an explicit nullhomotopy for the action of \(x\) on one boundary. In general perturbation theory one must construct a map comparing the two theories, and prove the identities which relate its values on products. Suppose a formal coupling is \(s\). Associative structure on the full tensor coalgebra of the suspension of a space of operators is described by a degree-one coderivation \(b_s=b_0+s b_1+s^2 b_2+\cdots\) whose square is zero. The scalar outputs belong to this equation. At order \(s^2\), \(b_1^2\) must be a \(b_0\)-boundary. On a nonunital reduction a separate curvature term records the scalar outputs.

This obstruction can be seen in four dimensions of ordinary algebra. Let \(1,x,y,z\) span an algebra with square-zero ideal \((x,y,z)\). Add the first-order products \(x*x=s y,\ y*x=s z\), with the other radical products zero. The order-\(s\) associativity equations hold. But \((x*x)*x-x*(x*x)=s^2z\). An arbitrary second-order correction \(\nu\) contributes its Hochschild differential. At the triple \((x,x,x)\) this is \(x\nu(x,x)-\nu(x,x)x=0\). No correction to the product at that order removes \(z\). Even when the two endpoint algebras do deform, the map between them has separate equations involving both actions.

There can also be an obstruction entirely in the map. The two flat algebras \(k[[s]][u]/(u^2)\) and \(k[[s]][v]/(v^2-s^2)\) agree modulo \(s^2\). An algebra map reducing to the identity would send \(u\) to \(v+s(a+bv)+O(s^2)\). Squaring modulo \(s^2\) forces \(a=0\). At the next order its square has unit coefficient \(s^2\), and any second-order correction from a term \(s^2w\) contributes \(s^2(vw+wv)\), whose coefficient modulo \((v)\) vanishes. The marked identity between these two formal algebras already fails to lift at this finite order.

For a marked bulk, boundary and interface the corresponding equations must retain the units, region restrictions and collision operations. Suppose the cone of the comparison is derived \(s\)-complete and the coherent maps over \(k[s]/(s^N)\) are its compatible derived scalar reductions. If its special fibre is acyclic, the successive scalar quotients show by induction that every reduced cone is acyclic. Taking their derived inverse limit proves that the formal comparison is a quasi-isomorphism. When the target is a derived centre, reduction of its continuous cochain model to the centre of the special fibre is an additional hypothesis. For ordinary relative Hochschild cochains of a dg algebra \(A\) over \(R\), use the derived enveloping algebra \(A\otimes_R^{\mathbf L}A^{\mathrm{op}}\). There is a positive scalar-change test. A perfect coefficient quotient is built from the base by finite cones and retracts. Derived Hom from the diagonal commutes with tensoring by these perfect coefficients. Extension of scalars then identifies the new diagonal and enveloping algebra. Thus the derived centre in this setting does commute with reduction from \(k[[s]]\) modulo \(s^N\), even when the ordinary algebraic centre jumps. For an algebra with \(xy=sz\) as its only nonzero product of two radical generators \(x,y,z\), the ordinary centre is spanned by \(1,z\) over \(k[[s]]\), while all four elements become central at \(s=0\). This test uses the actual relative bimodule diagonal. In a continuous chiral model one must still identify the coefficient and support functors which play its role. This is where the changing support in the \(E_7\) family matters. Completing at a single generic critical point had already changed the space of bulk observables before any comparison of operators could be made.

On the original two-state boundary, the class of \(x\) was invisible as a single endomorphism. The ternary product located the cubic interaction, the identity defect recovered \(x\) as a bulk field, and the disk put a number on its pairing with a boundary insertion. In the gauge theory an actual sphere experiment fixed \(1/16\). On the celestial line the four-current algebra supplied collision operators through \(s^2\), and a separately retained axis supplied an all-order action on a shared background. A complete physical reconstruction would still have to carry independent bulk insertions, states and gluings to those boundary measurements in the same theory. Those requirements give different experiments even when the algebra of protected bulk fields is already known. [Independent realizations of reconstruction](#independent-realizations)
