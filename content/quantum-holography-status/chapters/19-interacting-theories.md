# Recovering interactions from boundary operations

How far can an odd boundary operator deform a boundary condition while the bulk interaction stays fixed? Consider the B-twisted Landau–Ginzburg model with one formal coordinate \(x\), potential \(W=x^3\) and ground field \(k\) of characteristic zero. The protected bulk operators at the origin form the Jacobi ring, the quotient of \(k[[x]]\) by the critical equation \(W'(x)=3x^2=0\). The class of \(x\) is nonzero. Take a boundary with one even and one odd basis vector over \(k[[x]]\), in that order, and the odd operator
\[
 Q=\begin{pmatrix}0&x\\x^2&0\end{pmatrix}.
\]
Its square is \(W\) times the identity \(1\). A homogeneous boundary endomorphism \(B\) of parity \(|B|\) has differential \(dB=QB-(-1)^{|B|}BQ\), with \(d^2B=[W\,1,B]=0\). The protected boundary operators are the closed endomorphisms modulo the exact ones. Bringing \(x\) to this boundary gives \(x\,1\). Write \(E_{ij}\) for the matrix sending basis vector \(j\) to basis vector \(i\) and killing the other vector. Then \(dE_{21}=QE_{21}+E_{21}Q=x\,1\). A single insertion of the bulk coordinate acts by zero on boundary cohomology.

To couple an odd operator to this boundary, perturb \(Q\) by an odd matrix \(\alpha(t)\) with zero constant term in an even parameter \(t\). Keeping \(W\) fixed asks for
\[
 (Q+\alpha)^2-W\,1=d\alpha+\alpha^2=0.
\]
The linear term \(t\psi\), with \(\psi=E_{12}-xE_{21}\), satisfies \(d\psi=0\). Its square is \(-t^2x\,1\), so \(t^2E_{21}\) corrects the coupling through order two. Put \(Q_t=Q+t\psi+t^2E_{21}\). Since \(E_{21}^2=0\), the remaining terms give
\[
 \begin{aligned}
 Q_t^2-W\,1&=t^3(\psi E_{21}+E_{21}\psi)\\
            &=t^3\,1 .
 \end{aligned}
\]
Every entry of a boundary \(dB\) vanishes at \(x=0\), so no third-order correction has differential \(-1\). The binary product \([\psi]^2\) vanished in cohomology. The failed lift has returned the unit on three insertions. For a quartic bulk the same lift reaches one order further.

The homotopy \(E_{21}\) also explains how the invisible bulk field \(x\) can survive. It makes \(x\,1\) exact on this boundary, yet its graded commutator with \(\psi\) is the unit just computed. An action on all boundary conditions must respect their operators and maps up to coherent homotopy. Its home is the derived centre, the endomorphisms of the defect that transmits every boundary unchanged. A disk amplitude asks for one more datum, a trace on boundary operators. [Bulk actions and centres](#bulk-action-and-centre) · [States and amplitudes](#states-lines-and-caps)

## Reading a potential from a boundary {#ch19-boundary-potential}

**Definition (matrix factorization).** Over \(R=k[[x]]\), a matrix factorization of \(W\in R\) is a \(\mathbb Z/2\)-graded finite free module \(P\) with an odd operator \(Q\) satisfying \(Q^2=W\,1_P\). Its boundary operators form the algebra \(\operatorname{End}_R(P)\) with differential \(d=[Q,-]\).

At a marked critical point with \(W(0)=W'(0)=0\), keep the two basis vectors and replace the lower left entry of \(Q\) by \(W(x)/x\). This factorisation is the stabilised residue field at the origin. At an isolated critical point its shifts, cones and direct summands generate the compact boundary conditions supported there. Even for such a generator, \(x\) acts by zero on its endomorphism cohomology. Its identity and the odd matrix
\[
 \psi=\begin{pmatrix}0&1\\-W(x)/x^2&0\end{pmatrix}
\]
represent a basis of its cohomology over \(k\). Indeed an even cocycle must be a scalar matrix. The odd cocycles are the multiples of \(\psi\). In either parity the boundaries are exactly the multiples of \(x\) times the displayed generator. For \(W=x^d\), \(d\ge3\), one has \(\psi^2=-x^{d-2}1\). Thus the ordinary cohomology algebra in every one of these cases is the exterior algebra on one odd class, with its usual unit and \([\psi]^2=0\). Write \(\psi\) also for this class when it is an input of a higher product. [Dyckerhoff, Theorem 4.1](https://arxiv.org/pdf/0904.4713#page=13) · [Products with chosen primitives](#ch05-relations-can-leave-a-higher-operation)

For the quartic \(W=x^4\) the odd representative is \(\psi=E_{12}-x^2E_{21}\). Its square is now \(-x^2\,1\), so the second-order correction to \(Q+t\psi\) is \(t^2xE_{21}\). The coefficient of \(t^3\) in the square is \(x\,1=dE_{21}\). Adding \(-t^3E_{21}\) cancels the cubic term and leaves \(Q(t)^2=(x^4-t^4)1\). Thus three insertions give the unit for the cubic and zero in cohomology for the quartic. In the latter case it takes a fourth insertion to produce the first nonzero obstruction.

Which coefficient of a general potential is detected by \(n\) insertions? Keep \(x+t\) as the upper right entry of \(Q(t)\) and require \(Q(t)^2=(W(x)-c(t))1\), so that the change is a scalar series in \(t\). Evaluating at \(x=-t\) forces \(c(t)=W(-t)\). The required lower left entry is
\[
                  \frac{W(x)-W(-t)}{x+t}.
\]
Division by \(x+t\) is exact in \(k[[x,t]]\) because the numerator vanishes at \(x=-t\). The linear term of \(Q(t)-Q\) is \(t\psi\). Hence the scalar on the left of the fixed-bulk equation is \(-W(-t)\). For the cubic it is \(t^3\), for the quartic it is \(-t^4\). When this scalar vanishes the coupling solves the equation. Which deformations does the coordinate \(t\) describe?

::: {.proposition #ch19-flat-boundary-couplings title="deformations of the two-state boundary"}
Let \(S\) be a commutative local Artin \(k\)-algebra in degree zero, with maximal ideal \(\mathfrak m\) and residue field \(k\). Fix \(x\), \(W\) and the identification of the boundary modulo \(\mathfrak m\) with \(Q\). The odd matrices on the free \(S[[x]]\)-module of rank one in each parity which lift \(Q\) and square to \(W\,1\), up to even changes of basis equal to the identity modulo \(\mathfrak m\), are in natural bijection with
\[
                 \{\,t\in\mathfrak m\mid W(-t)=0\,\}.
\]
The matrix corresponding to \(t\) is \(Q(t)\).
:::

::: {.proof #ch19-flat-boundary-couplings-proof}
Write \(p,q\) for the upper right and lower left entries of a lift. Since \(p(x)\equiv x\bmod\mathfrak m\), it has a unique root \(-t\) in \(\mathfrak m\). Indeed a root modulo \(\mathfrak m^j\) lifts uniquely modulo \(\mathfrak m^{j+1}\) by dividing its error by the unit \(p'(-t)\), and \(\mathfrak m\) is nilpotent. Division gives \(p(x)=(x+t)u(x)\) with \(u\equiv1\bmod\mathfrak m\). Conjugation by \(\operatorname{diag}(u^{-1},1)\) makes the two entries \(x+t,uq\). Evaluation of \(pq=W\) at \(-t\) gives \(W(-t)=0\). Conversely this equality makes the divided difference in \(Q(t)\) a solution. Its lower entry is unique because \(x+t\) is a nonzero divisor, as one sees by translating \(x\) by \(-t\). Every even change of basis multiplies \(p\) by a unit and therefore preserves its root. The root and the matrix both commute with change of \(S\).
:::

For \(S_j=k[\epsilon]/(\epsilon^j)\), the choice \(t=\epsilon\) solves both the cubic and the quartic equation over \(S_3\). Every lift to \(S_4\) has \(t=\epsilon+c\epsilon^3\) for \(c\in k\), hence \(t^3=\epsilon^3\ne0\) and \(t^4=0\). This distinguishes the two interactions without choosing a primitive. Continuous local \(k\)-algebra maps from \(k[[t]]/(W(-t))\) to \(S\) describe these isomorphism classes. For any nonzero potential of order \(d\), the ideal \((W(-t))\) equals \((t^d)\). Thus the ordinary deformation functor retains the multiplicity alone. For \(W=x^3\) and \(W=2x^3\) its values agree, while the scalar errors are \(t^3\) and \(2t^3\). To distinguish their coefficients one must retain the value of the obstruction before setting it to zero.

**Proposition (higher products of the stabilized residue field).** The boundary endomorphism algebra has a minimal strictly unital \(A_\infty\) model on \(H=k1\oplus k\psi\). It has \(m_0=0\), and minimality means \(m_1=0\). The unit acts by the usual binary product, and operations of arity greater than two vanish on inputs containing the unit. Use the deformation convention \(d\alpha+\alpha^2\), the coordinate \(t\) of \(Q(t)\), and let \([x^n]W\) denote the coefficient of \(x^n\). For \(n\ge2\) the \(n\)-ary product is
\[
 m_n(\psi^{\otimes n})
       =(-1)^{n+1}[x^n]W\;1 .
\]
**Proof.** Write \(\alpha=Q(t)-Q=\sum_{n\ge1}t^n q_n\), so \(q_1=\psi\), and set \(\lambda_n=[t^n](-W(-t))\). Equating coefficients in the square gives
\[
             d q_n+\sum_{i+j=n,\ i,j\ge1}q_i q_j=\lambda_n\,1 .
\]
Define the comparison from \(H\) to the boundary endomorphisms by sending \(\psi^{\otimes n}\) to \(q_n\), the unit to the identity in arity one, and any higher word containing a unit to zero. The displayed equations are its \(A_\infty\) morphism equations on all nonunit words. Indeed, substituting an inner operation of \(H\) produces a scalar unit, so only the linear component can carry that output to the target. The identities for \(H\) itself follow by strict unitality. On a word of odd letters, the only nonzero nested terms multiply an inner scalar on the left or right by the remaining letter, and their two suspended signs are opposite. The linear comparison takes \(1,\psi\) to the cohomology basis above, proving the quasi-isomorphism. Dyckerhoff's one-variable minimal model gives the Taylor coefficients up to signs. Here the entry \(x+t\) and the square \(d\alpha+\alpha^2\) fix them. At a quadratic critical point the same formula gives the Clifford square \(m_2(\psi,\psi)=-[x^2]W\,1\). [The signed bar differential](#ch05-one-differential-encodes-all-associativity-homotopies) · [Dyckerhoff, §5.6, Theorem 5.8](https://arxiv.org/pdf/0904.4713#page=31)

The undeformed boundary has an ordinary differential graded endomorphism algebra. Its zero-input operation \(m_0\) is zero. After insertion of \(t\psi\), the new zero-input term is the sum of the positive-arity products \(\sum_{n\ge2}t^n m_n(\psi^{\otimes n})=-W(-t)1\). This explains why reduction by the unit needs care. Let \(e:H\to k\) take the scalar coefficient. On the reduced word of length \(n\) the composite \(e\circ m_n\) records a coefficient of \(W\). Projecting every output to \(H/k1\) would erase those values. The curved bar construction keeps these scalar components, with their suspension signs, as a functional on the reduced words called the curvature. Its length-three component records the scalar part of \(m_3\), even at a boundary with \(m_0=0\). [Splitting off the unit in the curved bar](#ch05-scalar-bar-curvature)

How much of \(W\) survives a change of boundary coordinate? Let \(V\) be a second potential with the same marked origin. For a based, strictly unital \(A_\infty\) map the zero-input component vanishes. Its \(n\)-input component has degree \(1-n\), so on \(n\) copies of \(\psi\) it is \(F_n\) times the target's odd generator. With \(F(t)=\sum_{n\ge1}F_nt^n\), the morphism equations read \(W(-t)=V(-F(t))\), coefficient by coefficient. The map is a quasi-isomorphism exactly when \(F_1\ne0\). In the marked Taylor coordinates the products recover the series \(W\) with \(W(0)=0\). Invertible changes of those coordinates give precisely the substitutions \(x\mapsto-F(-x)\).

For \(W=x^3+c x^4\) and \(V=y^3\), the source obstruction is \(t^3-ct^4\). Put \(F(t)=t(1-ct)^{1/3}\), taking the root with constant term one. Then \(F(t)^3=t^3-ct^4\) and \(F_1=1\). Thus a change with identity tangent map removes the fourth product \(-c\,1\). The order of the first nonzero product is preserved, and its coefficient transforms by the corresponding power of \(F_1\). Over \(k=\mathbb Q\) the potentials \(2x^3\) and \(y^3\) give identical sets of flat couplings in the displayed coordinate. A based unital quasi-isomorphism of their minimal models would require \(F_1^3=2\), impossible over \(\mathbb Q\). After adjoining a cube root of two, rescaling the odd generator gives the isomorphism. These statements concern the protected formal germ. The boundary \(Q\) was constructed from the given \(W\). A comparison with independently supplied boundary operations must identify their generator, coordinate and scalar unit before comparing coefficients.

## When two insertions can be distinguished {#ch19-ordered-insertions}

With one odd letter the coefficient of \(t^3\) could only come from one word. Take now \(W=x^3+xy^2\). A deformation in the two coordinate directions with commuting parameters \(s,t\) has scalar obstruction \(-W(-s,-t)=s^3+st^2\). The coefficient of \(st^2\) is a sum over three positions for the \(x\)-insertion. To recover the individual products, we must specify the representatives of the two boundary operators and the primitives used when two of them meet.

Work over \(k[[x,y]]\). On the exterior algebra of a two-dimensional space let \(e_i\) denote exterior multiplication and \(c_i\) contraction, with \(e_i c_j+c_j e_i=\delta_{ij}\). For \(W=f(x)+xg(y)\) put
\[
 Q=xe_1+ye_2+(f(x)/x+g(y))c_1 .
\]
Assume \(f\) starts in degree at least three and \(g\) in degree at least two. The square is \(W\). In the endomorphism algebra choose closed representatives
\[
 A=e_1-(f/x^2)c_1-(g/y)c_2
\]
and \(B=e_2\). The differential sends \(c_1,c_2\) to \(x,y\). Denote the classes of \(A,B\) by \(a,b\). Order both closed letters before the contractions, with \(A\) before \(B\). On each closed prefix the remaining differential is, up to the sign of the prefix, the Koszul differential \(dc_1=x,\ dc_2=y\). Thus \(1,A,B,AB\) represent the four cohomology classes and the binary product is the exterior product.

To fix the higher products, include these four representatives and project back by discarding contractions and evaluating their coefficients at the origin. The primitive of \(h(x)-h(0)\) is \((h(x)-h(0))c_1/x\), and likewise for \(y,c_2\). On a series in both variables first remove the terms divisible by \(x\), then apply the \(y\) contraction at \(x=0\). This gives a homotopy \(H\) with \(dH+Hd=1-ip\), where \(i,p\) are the inclusion and projection. The transferred product on an ordered word sums binary trees with \(i\) at the leaves, \(-H\) on each internal edge for these odd letters, and \(p\) at the root.

Now \(A^2=-f/x^2\) and \(BA=-AB-g/y\). The latter identity starts a homotopy on the ordered pair \(b,a\), while the pair \(a,b\) is already in the chosen order. Starting at \(b,a\) leaves \((g/y^2)c_2\) on the internal edge of the product tree. Multiplication on the right by \(B\) produces a scalar part, since \(c_2B=1-Bc_2\). In the cubic example \(g=y^2\), the edge is \(c_2\) and projection gives the unit on the word \(b,a,b\). For general \(g\), the constant part of \(g/y^2\) gives this three-input operation. Its remaining terms can continue along the edge by removing one further power of \(y\), with a minus sign. A factor multiplying this edge on the left produces no scalar. If two such internal edges meet, they give either zero or a multiple of \(c_1c_2\), killed by both projection and homotopy. The same reasoning on \(A^2\) uses \(c_1A=1-Ac_1\). Consequently the whole table on words of the two individual odd letters in arity \(n\ge3\) consists of
\[
\begin{aligned}
 m_n(a,\ldots,a)&=(-1)^{n-1}[x^n]f\;1,\\
 m_n(b,a,b,\ldots,b)&=(-1)^{n-1}[y^{n-1}]g\;1 .
\end{aligned}
\]
All other words of length \(n\ge3\) in \(a,b\) give zero for this contraction. The even class \(ab\) is also an allowed input of the full algebra. Its insertions use the full tree transfer. Dyckerhoff's multivariable theorem determines selected products of generators for a choice of homotopy. The ordered values here use the specified lifts of \(a,b,ab\). [Dyckerhoff, §5.6, Theorem 5.9](https://arxiv.org/pdf/0904.4713#page=31)

**Example (ordered mixed insertions).** For \(f=x^3,\ g=y^2\) (type \(D_4\)), the three coefficients contributing to \(st^2\) are \(m_3(b,a,b)=1\) and \(m_3(a,b,b)=m_3(b,b,a)=0\). On an auxiliary two-dimensional space attach \(S=E_{12}\) to \(a\) and \(T=E_{21}\) to \(b\). Give both insertions a common even parameter \(u\). The scalar part of their cubic product is \(u^3TST=u^3E_{21}\), since \(S^3=ST^2=T^2S=0\). Their binary product is \(u^2ab\otimes(ST-TS)=u^2ab\otimes(E_{11}-E_{22})\). The \((2,1)\) entry thus distinguishes the ordered cubic word in this representative even though the quadratic obstruction already prevents a flat coupling.

With \(g=y^3\) (type \(E_7\)) the mixed coefficient first occurs at \(m_4(b,a,b,b)=-1\). Which word carries the coefficient depends on the chosen representatives. Ordering \(B\) before \(A\) changes the lift of \(ab\) from \(AB\) to \(-BA\) and moves the \(D_4\) value to \(m_3(a,b,b)\). Both choices give \(st^2\) on commuting parameters. To compare matrix insertions between the two minimal models one must also transport the input by the higher components of the change of representatives.

## Which bulk operators reach the boundary {#ch19-diagonal-and-trace}

Changing the boundary representatives moved the mixed coefficient to a different word. Which operation of the boundary category can represent a bulk field independently of these choices? In the cubic example every \(h(x)\) acts on the cohomology of the two-state boundary by \(h(0)\,1\). On the bulk side, in \(r\) formal coordinates the gradient equations define a Koszul complex on odd generators \(\xi_i\) with \(d\xi_i=\partial_i W\). At an isolated critical point the gradient is a regular sequence, so its cohomology is the Jacobi ring \(\operatorname{Jac}(W)=k[[x_1,\ldots,x_r]]/(\partial_1W,\ldots,\partial_rW)\). To account for the surviving cubic class of \(x\), the boundary action must also act coherently on the maps between boundaries. [The bulk action on modules](#bulk-action-and-centre)

In the cubic, every odd nullhomotopy of \(x\,1\) on the generating boundary has the form \(h_g=E_{21}+g(x)\psi\), since two such primitives differ by an odd cocycle. To extend \(h_g\) over the boundary operator \(\psi\), its graded commutator with \(\psi\) would itself have to be exact. Direct multiplication gives
\[
             \psi h_g+h_g\psi=(1-2xg)\,1 .
\]
This represents \([1]\) for every \(g\). Thus the nullhomotopy on the object already fails the first condition of naturality up to homotopy. The identity defect computes the class with all its naturality conditions.

The identity defect transmits a boundary condition unchanged. As a kernel between two copies of the one-variable theory it is a factorization over \(k[[x,y]]\), with off-diagonal entries \(x-y\) and
\[
                  v(x,y)=\frac{W(x)-W(y)}{x-y}.
\]
Its square is \((W(x)-W(y))1\). Even endomorphisms commuting with this matrix are scalar. Exact scalars form the ideal \((x-y,v)\). Modulo \(x-y\) the second equation is \(v(x,x)=W'(x)\), a nonzero divisor for an isolated critical point. The pair is therefore a regular sequence, and its Koszul complex has no odd cohomology. Multiplication by \(h(x)\) on the defect represents the residue class of \(h\) in \(k[[x]]/(W')\). For \(W=x^3\), this sends the bulk class of \(x\) to the nonzero class of \(x\) in the derived centre.

**Proposition (endomorphisms of the identity defect).** Let \(W\in k[[x_1,\ldots,x_r]]\) have an isolated critical point at the origin with \(W(0)=0\). Consider the two-periodic category of matrix factorizations supported at the origin. Its derived centre has cohomology only in even parity, where the cohomology algebra is \(\operatorname{Jac}(W)\). Indeed, telescope \(W(x)-W(y)=\sum_i(x_i-y_i)v_i\). The endomorphism differential of the resulting Koszul factorization sends the contractions to \(x_i-y_i\) and the exterior generators to \(v_i\). On the diagonal the latter are \(\partial_iW\), so the combined sequence is regular. Scalar endomorphisms give the stated algebra. The identity-kernel theorem identifies its cohomology with Hochschild cohomology, and the stabilized residue field is a compact generator at that support. For an isolated point \(p\) of value \(W(p)\), the same statement uses the completed germ of \(W-W(p)\). An identification of the centre including its \(E_2\) operations requires a comparison of cochains. [Dyckerhoff, Proposition 6.3 and Corollaries 6.4–6.5](https://arxiv.org/pdf/0904.4713)

**Definition (residue trace).** Fix the coordinate volume \(dx\) at an isolated one-variable critical point. The sphere functional on \(\operatorname{Jac}(W)\) is \(\tau_W(h)=\operatorname{Res}_0 h(x)\,dx/W'(x)\), the coefficient of \(x^{-1}\) in \(h/W'\). It gives the bulk pairing \((h,g)\mapsto\tau_W(hg)\). For \(W=ax^3\) with \(a\ne0\), this gives \(\tau_W(x)=1/(3a)\). The marked boundary product is \(m_3(\psi,\psi,\psi)=a\,1\). Thus \(x^3\) and \(2x^3\) have the same Jacobi ideal and the same flat-coupling equation, but the sphere insertion of the same \(x\) gives \(1/3\) and \(1/6\), respectively.

On the disk take the two-state factorisation and one odd boundary insertion \(\psi\). Moving this insertion into the bulk gives the class of \(\operatorname{str}((\partial_x Q)\psi)\,dx\), with supertrace equal to the even trace minus the odd trace. The two diagonal entries are \(-W/x^2\) and \((W/x)'\), so the supertrace is \(-W'/x\). Pairing with a bulk field \(h\) gives \(\operatorname{Res}_0(-h/x)\,dx=-h(0)\). From the boundary side \(h\) acts by \(h(0)\) and the disk trace of \(\psi\) is \(-1\), giving the same answer. In particular the mixed disk amplitude for \(h=x\) vanishes even though \(x\) survived at the identity defect. The boundary-to-bulk class belongs to Hochschild **homology**, which has parity \(r\bmod 2\) in \(r\) variables. The volume and the order of the factors in the supertrace fix this sign. [Dyckerhoff and Murfet, Theorems 3.4 and 4.9](https://arxiv.org/pdf/1004.0687) · [Polishchuk and Vaintrob, Theorem 3.2.3](https://arxiv.org/pdf/1002.2116#page=33)

::: {.example #ch19-quartic-sphere-moments title="two higher products and three sphere insertions"}
Fix \(dx\) and a potential \(W=x^4+a x^5+b x^6+O(x^7)\). In the marked boundary coordinate the first three scalar products are \(m_4=-1,\ m_5=a,\ m_6=-b\) on copies of \(\psi\), in units of the identity. Suppose instead that the sphere functional at the origin is given on the marked fields \(1,x,x^2\). The critical equation is \(W'=x^3(4+5ax+6bx^2+O(x^3))\), so expansion of the reciprocal gives
\[
 \begin{aligned}
 \tau_W(x^2)&=\tfrac14,\\
 \tau_W(x)&=-\tfrac{5a}{16},\\
 \tau_W(1)&=\tfrac{25a^2}{64}-\tfrac{3b}{8}.
 \end{aligned}
\]
The \(x\) insertion fixes \(a\). The vacuum value then fixes \(b\), including the contribution quadratic in \(a\). For \(a=b=1\) these three values are \(1/4,-5/16,1/64\). In this model both calculations start from the same potential. With a sphere functional and higher boundary products supplied separately, the displayed equations test their compatibility in the specified coordinate and volume. Terms of order seven or higher in \(W\) affect none of these three residues.
:::

Suppose the two marked-origin potentials are related by an invertible formal coordinate \(y=\phi(x)\), \(W(x)=V(\phi(x))\). Does this coordinate also preserve the numerical amplitudes defined with \(dx\) and \(dy\)? Substitution in the residue gives
\[
 \tau_V(h)=\tau_W\big((h\circ\phi)(\phi')^2\big).
\]
One factor of \(\phi'\) comes from the volume and the other from the derivative of the potential. Because the residue pairing is perfect, the pullback \(h\mapsto h\circ\phi\) preserves the sphere trace exactly when \((\phi')^2=1\) modulo \(W'\). The odd disk fixes an additional sign. Put \(S=\operatorname{diag}(\phi(x)/x,1)\). Then \(Q_V(\phi(x))=S Q_W(x)S^{-1}\). Pullback followed by conjugation by \(S^{-1}\) takes the odd class to \(\psi_W/\phi'(0)\) in cohomology, so preservation of the normalized disk trace requires \(\phi'(0)=1\).

If \(W,V\) have order \(d\ge2\), then \((W')=(x^{d-1})\). Since \(\phi'+1\) is a unit when \(\phi'(0)=1\), the two trace conditions say \(\phi=x+O(x^d)\). Such a change exists exactly when \(W-V\in(x^{2d-1})\). Necessity follows by substituting \(x+O(x^d)\) in an order-\(d\) series. Conversely, the congruence gives a common leading coefficient \(a\). Write \(W=a w^d,\ V=a v^d\) by taking the \(d\)-th roots with \(w=x+O(x^2),\ v=x+O(x^2)\). Then \(w-v\in(x^d)\), so \(\phi=v^{-1}\circ w\) has the required order. For \(d\ge3\), \(x^d\) and \(x^d+c x^{2d-2}\) with \(c\ne0\) are equivalent under a coordinate change tangent to the identity and have identical Jacobi ideals. Yet their standard sphere traces of \(1\) are \(0\) and \(-(2d-2)c/d^2\).

**Example (two colliding vacua).** For \(W_t=x^3/3-tx\), the monic critical polynomial is \(P=x^2-t\). In \(k[t,x]/(P)\), the residue of an insertion is the coefficient of \(x\) after reduction. Away from \(t=0\) the two roots, in a splitting field, have sphere weights \(1/(2\sqrt t)\) and \(-1/(2\sqrt t)\). Inserting \(x\) multiplies each weight by its own root, so their sum is \(1\). The remainder calculation gives the same value at \(t=0\) and gives \(\tau_t(x^3)=t\), an insertion that reads the splitting parameter.

To sew two boundaries one needs the inverse bulk pairing. Here it is the two-variable element \(x+y\). Multiplication by \(x-y\) kills it and tracing its first leg returns \(1\), so tracing \(h(x)(x+y)\) returns \(h(y)\). Closing the two legs sets \(y=x\) and inserts a handle \(2x\). The genus-one vacuum value is \(\tau_t(2x)=2\), and the genus-three value is \(\tau_t((2x)^3)=8t\). For any monic \(P=W'\) of degree \(d\), replace the trace by the coefficient of \(x^{d-1}\) in the remainder modulo \(P\). The same argument gives the inverse pairing \((P(x)-P(y))/(x-y)\) and handle \(P'(x)\), including on the discriminant. [Critical points and sphere insertions](critical-points-and-sphere-insertions.pdf)

Which critical point is being observed when the interaction varies? In the family
\[
                 W_s=x^3+xy^2(y+s)
\]
the marked boundary products are \(m_3(b,a,b)=s\) and \(m_4(b,a,b,b)=-1\). The closed equations are \(3x^2+y^2(y+s)=0\) and \(xy(3y+2s)=0\). Over \(k[[s]]\) the first eliminates \(x^2\). In the resulting module on \(1,x\) over the \(y\)-series, the second kills \(y(3y+2s)\) times \(x\), and multiplying it by \(x\) kills \(y^3(y+s)(3y+2s)\) in the scalar part. The two quotient polynomials have degrees two and five with invertible leading coefficients. Thus the relative Jacobi algebra is free of rank seven, also the dimension of the \(E_7\) fibre at \(s=0\).

After passing to \(k((s))\), the origin has length four, and \((0,-s)\) is a simple critical point with value zero. Two more simple critical points, over a splitting field, have \(y=-2s/3,\ x^2=-4s^3/81\), and \(W_s=-2x^3\ne0\). All seven dimensions survive scalar extension. Completion at the single generic origin selects four of them. Fixing the value of the potential also matters. Near either nonzero critical value \(W_s\) is a unit and \(Q/(2W_s)\) contracts the identity of a factorization of \(W_s\). The whole critical scheme, its value-zero part and the chosen origin thus select lengths seven, five and four, respectively.

## A coordinate mode detects a Jordan block in the chiral Koszul complex {#ch19-chiral-screening}

The Jacobi ring tells us how coordinates multiply at a critical point. What does repeated insertion of a coordinate do to a state that also contains a derivative of a field? The same gradient equations define the differential of a chiral Koszul complex in which the field and its derivatives are separate operators. In the polynomial free-field vacuum take even fields \(\beta_i,\gamma_i\) and odd fields \(b_i,c^i\), with \([\beta_i{}_\lambda\gamma_j]=[b_i{}_\lambda c^j]=\delta_i^j\) and all other independent brackets zero. These constant brackets specify the simple-pole contractions. Give \(\gamma_i,b_i\) weight zero and \(\beta_i,c^i\) weight one. Their cohomological degrees are zero for the even fields and \(-1,+1\) for \(b_i,c^i\), respectively. [Fields and their modes](#fields-and-modes)

**Definition (gradient screening).** For \(f_i=\partial_i W\), the screening differential \(D\) is the residue of the normally ordered current \(\sum_i:f_i(\gamma)c^i:\). Its self-product is regular, since none of its constituents contract with one another. Thus \(D^2=0\). As a zero mode it commutes with translation \(T\) and differentiates every vertex product. At weight zero \(Db_i=f_i,\ D\gamma_i=0\), precisely the bulk Koszul complex. A regular gradient sequence gives the Jacobi ring in degree zero. At positive weight two contractions can contribute to a single residue. [Malikov and Schechtman, chiral Koszul complexes](https://arxiv.org/pdf/1406.0284) · [Dedushenko, Landau–Ginzburg chiral algebras](https://arxiv.org/pdf/1511.04372)

For the one-variable screening \(f=x^3\) the potential is \(W=x^4/4\). In weight-indexed oscillator notation \(x=\gamma_0\) is the coefficient of \(z^0\) in \(\gamma(z)\). It creates a coordinate on the vacuum and acts on any state by this single mode. Write \(y=T\gamma,\ p=\beta_{-1},\ \theta=b_0,\ \eta=c_{-1}\) for the other creators needed here. In the ordered basis of creation operators the differential is
\[
 D(p\theta)=x^3p+3x^2\theta\eta-6xy .
\]
The first two terms follow from a single contraction. The last uses contractions against both \(p\) and \(\theta\), giving a double pole. The linear Taylor coefficient of the remaining \(\gamma\) then supplies \(y\), leaving a simple pole with coefficient \(-6xy\). To see where it goes in cohomology, note that \(Dp=-3x^2\eta,\ D(\theta\eta)=x^3\eta,\ Dy=0\). Thus the weight-one, degree-zero cycles are generated over \(k[x]\) by \(J=xp+3\theta\eta\) and \(y\). The incoming states \(T\theta,\ p\theta,\ y\theta\) give \(3x^2y,\ x^2J-6xy,\ x^3y\). The last relation follows from the first.

The relations \(x^2J=6xy\) and \(x^2y=0\) reduce every class to a combination of \(J,xJ,y,xy\). These four are independent. In a relation among them the coefficient of \(J\) must be divisible by \(x^2\), so it vanishes. The remaining coefficient of \(y\) must then also be divisible by \(x^2\). In particular \(xy\) survives. Repeated coordinate insertions give \(J,xJ,x^2J=6xy\ne0,x^3J=0\), a Jordan chain of length three. The vector \(y-xJ/6\) supplies a chain of length one. Omitting the double contraction gives \(x^2J=x^2y=0\) and two chains of length two. Counting the states gives four in either case. Applying \(x\) twice to the prepared class \([J]\) distinguishes the two differentials.

For \(f=x^m\), \(m\ge2\), the same relations are \(x^{m-1}y=0\) and \(x^{m-1}J=m(m-1)x^{m-2}y\), with \(J=xp+m\theta\eta\). The common divisor of the entries in this relation matrix is \(x^{m-2}\) and its determinant is \(x^{2m-2}\) up to sign. The Smith factors therefore give lengths \(m-2,m\), omitting the zero length when \(m=2\). The differential with only single contractions gives lengths \(m-1,m-1\).

Can this length-three chain come from ordinary multiplication by \(x\) on a boundary of the quartic \(W=x^4/4\)? Work over \(k[[x]]\) in characteristic zero. In any finite free matrix factorisation, Smith normal form for one parity map splits the factorisation into blocks with off-diagonal entries \(x^a,x^{4-a}/4\), \(0\le a\le4\), since their product is \(W\). On each block multiplication by \(x^2\) is nullhomotopic. With \(x^a\) in the upper-right slot, take the odd matrix \(x^{2-a}E_{21}\) for \(a\le2\), or \(4x^{a-2}E_{12}\) for \(a\ge2\). In both cases \(QH+HQ=x^2I\). Composition with this homotopy kills \(x^2\) on the cohomology of every morphism complex with this target. For \(a=2\) the class of \(xI\) survives because exact scalar matrices are divisible by \(x^2\). The longest coordinate chain in these boundary cohomologies has length two. In the chiral vacuum above, applying the coordinate mode twice to \([J]\) gives the nonzero class \(6[xy]\).

The coupled potential \(W=X^3+XY^3\) lets us perform two distinct insertions on the same state. Its screening polynomials are \(3X^2+Y^3,\ 3XY^2\). Here \(X,Y\) also denote the two single coordinate creators. Put \(Y_1=T\gamma_Y\), insert a parameter \(h\) in every elementary contraction, and divide the screening residue by \(h\). Every residue uses at least one contraction, so the divided differential is defined at \(h=0\). At weight one the cohomology dimensions are \(8,16,8\) in degrees \(-1,0,1\) on both the zero and the nonzero fibres. The Jordan lengths of \(Y\) on degree zero are \((4,4,3,3,1,1)\) at \(h=0\) and \((5,4,3,2,2)\) at \(h\ne0\).

Prepare the closed Euler current \(J=3Xp_X+2Yp_Y+6\theta_X\eta_X+7\theta_Y\eta_Y\), using the creator order above in each species. Closure follows from the weights \(3,2\) of the coordinates and \(6,7\) of the two gradient equations. To read the fourth iterate, put
\[
\begin{aligned}
 U={}&4Y\theta_X\theta_Y\eta_Y+2Y^2\theta_Xp_Y+Y^2\theta_Yp_X\\
    &-2X\theta_Yp_Y-4h\theta_XY_1-2hY\,T b_X .
\end{aligned}
\]
Taking the screening residue gives \(DU=Y^4J-28hY^3Y_1\). To see that \(Y^3Y_1\) survives, give \(X,Y\) charges \(3,2\), \(\theta_X,\theta_Y\) charges \(6,7\), and the conjugate creators \(p_i,\eta_i\) the opposite charges of their partners. The differential preserves charge. Look for a charge-eight boundary involving only coordinate derivatives. Its momentum components must vanish, as must its \(\theta_i\eta_j\) components. Imposing those conditions in that order leaves two possible sources, \(Y\,Tb_X\) and \(\theta_XY_1\). Their images are
\[
 6XY\,T\gamma_X+3Y^3Y_1,\qquad (3X^2+Y^3)Y_1 .
\]
The first carries \(XY\,T\gamma_X\) and the second \(X^2Y_1\). No linear combination gives \(Y^3Y_1\) alone. It represents the nonzero class in this one-dimensional weight-one, degree-zero, charge-eight group.

Four applications of \(Y\) to \([J]\) give \(28h[Y^3Y_1]\). Taking the coefficient of \(z^0\) in the single field \(:\gamma_Y(z)^4:\) also permits a contraction with \(p_Y\). On weight one its extra term is \(-12hY^2Y_1\partial_{p_Y}\). Since \(\partial_{p_Y}J=2Y\), this insertion gives \(4h[Y^3Y_1]\). The difference is visible on the nonzero fibres in the very same output class.

## A gauge algebra and an independent sphere measurement {#ch19-gauge-and-sphere}

In the preceding example four successive coordinate insertions gave a different operator from one insertion of the fourth power. For two different operators we can also reverse their order. Can the two products be different while a specified state assigns them the same expectation? A protected Higgs-branch algebra in three-dimensional \(\mathcal N=4\) gauge theory lets us calculate both the products and a sphere expectation. Take \(n\ge2\) hypermultiplets and a gauge torus of rank \(n-1\). Its \(a\)-th generator has charge \(+1\) on species \(a\), \(-1\) on species \(n\), and zero on the others. Quantize the coordinates and momenta as Weyl pairs with \([p_i,x_j]=\hbar\delta_{ij}\). Take the torus-invariant algebra and impose the moment equations \(x_ap_a-x_np_n=\zeta_a\). A neutral monomial has the same excess of coordinate powers over momentum powers in every species. Its unpaired factors are therefore powers of \(X=\prod_i x_i\) or \(Y=\prod_i p_i\). All remaining factors are polynomials in \(z=x_np_n\) after the moment equations.

**Proposition (quantum Hamiltonian reduction).** In this ordering, with \(P(z)=z\prod_{a<n}(z+\zeta_a)\), the protected algebra has relations
\[
\begin{aligned}
 [z,X]&=\hbar X,&[z,Y]&=-\hbar Y,\\
 XY&=P(z),&YX&=P(z+\hbar),
\end{aligned}
\]
**Proof.** In \(XY\) each species contributes \(x_ip_i\). In \(YX\) each contributes \(p_ix_i=x_ip_i+\hbar\). The commutators with \(z=x_np_n\) follow from the \(n\)th Weyl pair, since \(z\) commutes with every other species. The neutral monomials above span the reduction in the forms \(z^b,\ z^bX^a,\ z^bY^a\), with \(b\ge0,\ a\ge1\). To test their independence, invert all \(x_i\) in the ambient Weyl algebra and put \(z_i=x_ip_i\). Its torus invariants are generated by the \(z_i\) and the Laurent powers of \(t=\prod_i x_i\), with \(t z_i=(z_i-\hbar)t\). Indeed a neutral Laurent monomial has the same exponent of every \(x_i\) once its \(z_i\)'s are moved to the left. The differences \(z_a-z_n\) commute with these generators, so imposing \(z_a-z_n=\zeta_a\) gives a map from the original reduction to the skew Laurent algebra in \(z,t^{\pm1}\). There \(X=t,\ Y=P(z+\hbar)t^{-1}\). Different powers of \(X,Y\) have distinct Laurent degrees. In degree \(-a\) the coefficient of \(Y^a\) is the product of the monic factors \(P(z+j\hbar)\) for \(1\le j\le a\). Multiplication by that product is injective, proving independence of the images of \(z^bY^a\), and hence of these elements in the original reduction. The nonnegative degrees give the same conclusion directly. At zero moment parameter and \(n=3\), the order difference \([Y,X]=P(z+\hbar)-P(z)\) is \(3\hbar z^2+3\hbar^2z+\hbar^3\). [Gaiotto and collaborators, quantized Higgs-branch operator algebras](https://arxiv.org/pdf/2308.15198)

The chiral gauge reduction has a further condition. Put \(t_i=:\gamma_i\beta_i:\) and \(J_a=t_a-t_n\). Their double pole is \(-\hbar^2 M_{ab}\), where \(M_{ab}=\delta_{ab}+1\). Introduce independent Heisenberg fields \(H_a\) with double pole \(+\hbar^2 M_{ab}\) and odd ghost pairs \(b_a,c^a\) with simple pole \(\hbar\delta_a^b\). The gauge differential is the residue of \(\sum_a:c^a(J_a-H_a):\) divided by \(\hbar\). The two levels cancel, so the gauge current in this residue has regular self-product. Without the compensating fields its square on \(b_a\) would give \(-\hbar\sum_b M_{ab}T c^b\).

For \(n=3\) bring \(\mathsf X=:\prod_i\gamma_i:\) at \(z_1\) towards \(\mathsf Y=:\prod_i\beta_i:\) at \(z_2\). In this order the basic \(\gamma_i,\beta_i\) contraction is \(-\hbar/(z_1-z_2)\). The cubic pole has coefficient \(-\hbar^3\), the double pole \(\hbar^2\sum_i t_i\), and the simple pole
\[
 -\hbar\sum_{i<j}:t_i t_j:
       +\hbar^2\sum_i:(T\gamma_i)\beta_i: .
\]
The derivative comes from expanding the uncontracted \(\gamma_i(z_1)\) after two contractions. Its gauge variation cancels that of the two-species products. A comparison with the associative reduction must carry this differential to the zero-mode complex and specify the specialization of the Heisenberg zero modes. [Kuwabara, hypertoric vertex algebras](https://arxiv.org/pdf/1706.02203)

A multiplication table still needs a state before it predicts a number. Set \(\hbar=1,\ P(z)=z(z-2)(z-5)\). On two states \(v_0,v_1\) put \(zv_j=jv_j,\ Xv_0=v_1,\ Yv_1=4v_0\), with \(Xv_1=Yv_0=0\). Since \(P(1)=4\), the diagonal entries of \(XY\) are \(0,4\), and those of \(YX\) are \(4,0\). The metric \(\operatorname{diag}(1,4)\) makes \(Y\) the adjoint of \(X\). The state \(\tfrac12\operatorname{Tr}\) gives \(2\) on both orders. A one-dimensional character would have \(X=Y=0\) by the commutators with \(z\). It would require \(P(z)=P(z+1)=0\), and this polynomial has no roots a unit apart.

::: example {#ch19-positive-weight-string title="The positive weight string"}
Which finite-dimensional Hilbert space representations of this fibre can realise \(z^*=z\) and \(X^*=Y\)? For \(zv=sv\), the commutators give \(Xv\) weight \(s+1\) and \(Yv\) weight \(s-1\) whenever these vectors are nonzero. The product relations give
\[
 \|Xv\|^2=P(s+1)\|v\|^2,\qquad
 \|Yv\|^2=P(s)\|v\|^2 .
\]
In an irreducible representation, start with a lowest-weight eigenvector and apply \(X\) until it vanishes. The span of the string is invariant under \(Y\), since \(YXv=P(s+1)v\), so it is the whole representation. Its weights run from a root \(a\) of \(P\) to \(b-1\), where \(b\) is another root. Each intermediate value \(P(a+1),\ldots,P(b-1)\) must be positive. Here \(P(1)=4\), \(P(2)=0\), \(P(3)=-6\) and \(P(4)=-8\). Only the weights \(0,1\) qualify, and normalising the two vectors fixes the raising coefficient at \(2\). This proves uniqueness up to unitary equivalence.

The representation still allows several preparations. If the two weight populations are \(p_0,p_1\), the readings of \(XY\) and \(YX\) are \(4p_1\) and \(4p_0\). The pure lowest-weight state gives \(0,4\), while the normalised trace gives \(2,2\).
:::

A round three-sphere prepares a functional independently of these matrices. Place the protected insertions on an oriented great circle. With no insertion the functional gives the partition function. Fix sphere radius one, dimensionless real masses \(m_i\) in these radius units, and zero Fayet–Iliopoulos parameters. Localization assigns Lebesgue measure \(d\sigma_a\) to each real gauge variable and a factor \(F(t)=(2\cosh\pi t)^{-1}\) to each hypermultiplet. The first \(n-1\) arguments are \(\sigma_a+m_a\), the last is \(-\sum_{a<n}\sigma_a+m_n\). Shift \(\sigma_a+m_a\) to new integration variables and Fourier-expand the last factor. Each of the other integrations returns \(F(t)\), since \(F\) is its own transform for the kernel \(e^{2\pi iMt}\). Thus for \(M=\sum_i m_i\),
\[
\begin{aligned}
 Z_n(M)&=\int_{\mathbb R}e^{2\pi iMt}F(t)^n\,dt\\
       &=\frac{\Gamma(n/2+iM)\Gamma(n/2-iM)}
                    {2\pi\Gamma(n)} .
\end{aligned}
\]
The substitution \(q=e^{2\pi t}\) gives the second equality by the beta integral. At \(n=3,\ M=0\), \(\Gamma(3/2)=\sqrt\pi/2\) gives \(Z_3(0)=1/16\). This is an exact unnormalized partition function in the localization measure. The two-state trace fixes its own value on the identity by \(\tfrac12\operatorname{Tr}1=1\). [Dedushenko, Pufu and Yacoby, localization of the protected sector](https://arxiv.org/pdf/1610.00740)

To compare ordered insertions, fix \(\hbar=1\), place all the mass \(M\) on species \(n\), and turn on real Fayet–Iliopoulos parameters \(\nu_a\) by inserting \(e^{2\pi i\sum_{a<n}\nu_a\sigma_a}\). Set \(\nu_n=0\). For one oscillator, differentiating its hypermultiplet factor with respect to its mass and dividing by \(2\pi\) inserts the symmetrically ordered \(x_jp_j+1/2\). After Fourier transformation this acts as \(i(t-\nu_j)\). The difference of the \(a\)-th and last insertions fixes \(\zeta_a=-i\nu_a\), and \(z\) acts as \(it-1/2\) in this functional.

**Definition (sphere trace on the protected algebra).** For a neutral polynomial \(q(z)\) the unnormalized insertion is
\[
 I_\nu(q;M)=\int_{\mathbb R} e^{2\pi iMt}
        \prod_{j=1}^n F(t-\nu_j)\,q(it-\tfrac12)\,dt .
\]
Charged one-point functions vanish by the residual circle symmetry. The unit insertion is \(I_\nu(1;M)\). Division by this number, when nonzero, gives the normalized expectation.

The orientation of the circle can now be tested on \(XY\) and \(YX\). Put \(\lambda=(-1)^n e^{2\pi M}\). In the integral for \(P(z)q(z)\), move the contour down by \(i\). At each crossed pole \(t=\nu_j-i/2\), \(P(it-1/2)\) has a compensating zero, including its multiplicity for equal shifts. The shift sends \(z\) to \(z+1\) and multiplies the density by \(\lambda\). Hence \(I_\nu(P(z)q(z);M)\) equals \(\lambda I_\nu(P(z+1)q(z+1);M)\). Taking \(q=1\) gives \(I_\nu(XY;M)=\lambda I_\nu(YX;M)\). Allowing arbitrary \(q\) tests the exchange in the presence of any additional neutral insertion. Together with charge vanishing and the normal basis, this gives \(I_\nu(ab;M)=I_\nu(\sigma(b)a;M)\) on every word, with \(\sigma(z)=z,\ \sigma(Y)=\lambda Y,\ \sigma(X)=\lambda^{-1}X\).

For three massless species and zero shifts one has \(P=z^3\). As the total mass varies from zero, the gamma integral gives \(Z_3(M)/Z_3(0)\) as \((1+4M^2)/\cosh(\pi M)\). Its second derivative gives \(\langle t^2\rangle=(\pi^2-8)/(4\pi^2)\) in the even density \(F(t)^3/Z_3(0)\). Inserting \((it-1/2)^3\) therefore gives \(\langle XY\rangle=1/4-3/\pi^2\), and the twist gives \(\langle YX\rangle=-\langle XY\rangle\).

The finite-matrix trace is reached by a different preparation. Continue the *unnormalized* functional meromorphically, take the residue at \(\nu_1=-2i\) first, and then at \(\nu_2=-5i\). The first pole selects the weights \(z=0,1\). On a neutral \(q\) the double residue is \(e^{\pi M}(q(0)+\lambda q(1))/(4\pi^2)\). At \(M=i/2\) the twist is one. Dividing by the double residue of the unit gives \((q(0)+q(1))/2\), precisely the two-state trace on the fibre \(P=z(z-2)(z-5)\).

In the reverse order the first residue selects the five weights \(j=0,\ldots,4\) at the poles \(t_j=-i(j+\tfrac12)\), where \(it_j-\tfrac12=j\). At successive weights both residues of the pinching pair change sign. The remaining hypermultiplet residue changes sign as well, and the mass exponential contributes \(e^{2\pi M}\). Hence successive weights have ratio \(\lambda\). At \(M=i/2\) the normalised reverse residue on \(q\) is \(\tfrac15\sum_{j=0}^{4}q(j)\). For the fibre involution \(z^*=z,\ X^*=Y\), take \(q(z)=P(z)=Y^*Y\). The forward residue gives \(2\) on this square. The reverse residue gives \((0+4+0-6-8)/5=-2\), which excludes a positive state for this involution. This test concerns the continued fibre at the specified complex parameters. The round sphere with real parameters has its own reality condition. [Protected circle traces and their parameter conventions](https://arxiv.org/pdf/2308.15198)

## Four celestial currents at the first quantum order {#ch19-four-currents}

The sphere trace assigned numbers to the two orders of insertion on an oriented great circle. On a celestial line we can ask for the product before taking a trace. In flat self-dual Yang–Mills theory coupled to its anomaly-cancelling axion, place the fields at \(z\) and \(0\), take a Laurent coefficient in \(z\), and resolve the colour and transverse Taylor degrees of its output. The two gauge helicities give even currents \(J_a[r]\) and \(L_a[r]=\widetilde J_a[r]\), with colour \(a\) and transverse index \(r=(r_1,r_2)\in\mathbb N^2\). In the coupling to the bulk gauge field, \(J_a[r]\) multiplies the Taylor coefficient \(\partial_1^{r_1}\partial_2^{r_2}A^a_{\bar z}/(r_1!r_2!)\) evaluated at the line. The axion, whose kinetic operator is fourth order, gives the two towers \(E[r]\) and \(F[r]\), with \(E[0,0]\) absent. The holomorphic Chern–Simons example of the four-dimensional Wess–Zumino–Witten theory has a single untilded open tower. In self-dual gravity the transverse Hamiltonians have a Poisson bracket. The following coefficients use the gauge-plus-axion couplings. [The celestial current product](#ch14-celestial-yangian-like) · [Fernández and Paquette, §2 and Table 1](https://arxiv.org/pdf/2412.17168v2)

Let \(\mathfrak g\) be the complex simple gauge Lie algebra, \(h^\vee\) its dual Coxeter number, and \(K\) the basic form fixed by \(\operatorname{Tr}_{\rm ad}(\operatorname{ad}_a\operatorname{ad}_b)=2h^\vee K(a,b)\). Assume \(\operatorname{Tr}_{\rm ad}((\operatorname{ad}_a)^4)=\gamma K(a,a)^2\) for all \(a\), with \(\gamma\ne0\). Set the axion coupling to \(s\) and the open-loop coefficient to \(\nu=\hbar/(16\pi^2)=-3s^2/\gamma\). Work first over \(R=\mathbb C[s]/(s^3)\). Two axion vertices and one open loop then contribute at the same order. We write the longitudinal poles as \([A_\lambda B]=\sum_{j\ge0}\lambda^j A_{(j)}B/j!\), where \(A_{(j)}B\) is the coefficient of \(z^{-j-1}\) in \(A(z)B(0)\). The operator \(T\) differentiates the output along the line.

At tree level the transverse monomials of two gauge currents multiply. At one loop a derivative can land on either of two output currents. To retain this information, assign the outputs independent transverse variables \(U,V\). For transverse polynomials \(f,g\), put \(z_a=V+a(U-V)\), \(f_a=\nabla f(z_a)\), \(g_b=\nabla g(z_b)\). The ordered scalar coefficient is an integral over \(\Delta=\{0<b<a<1\}\),
\[
 \Phi(f,g)=-\int_\Delta \det(f_a,g_b)\,db\,da .
\]
For input coordinates \(x,y\) this gives \(\Phi(x,y)=-1/2\). Replacing \(x\) by \(x^2\) gives \(-2\int_0^1a(V_1+a(U_1-V_1))\,da=-(2U_1+V_1)/3\). The weights \(-2/3,-1/3\) distinguish the two slots before any colours are contracted.

For incident monomials of indices \(r,t\), put \(d=r_1t_2-r_2t_1,\ w=r+t-(1,1),\ N_r=r_1+r_2\), and define \(N_t\) likewise. A negative output index gives zero. Write \(\Phi_{kl}\) for the coefficient of \(U^kV^l\) on those inputs. In a colour basis with structure constants \(f_{ab}{}^c\), put \(C_{ab}^{ij}=K^{pq}f_{ap}{}^i f_{bq}{}^j\), using the inverse form and summing repeated colour indices. The quadratic fields in the two channels are
\[
\begin{aligned}
 Q_{ab}&=\sum_{k+l=w}(\Phi_{kl}C_{ab}^{ij}+\Phi_{lk}C_{ab}^{ji})
                           :J_i[k]L_j[l]:,\\
 P_{ab}&=\sum_{k+l=w}\Phi_{kl}C_{ab}^{ij}:L_i[k]L_j[l]: .
\end{aligned}
\]
The colons denote the regular, normally ordered product. In \(Q_{ab}\) the positive current comes first.

Write \(J_{[a,b]}\) and \(L_{[a,b]}\) for currents coloured by the Lie bracket of \(a,b\), and \(K_{ab}=K(a,b)\). To display the intermediate axion in the positive-positive channel, set
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
For example, \(E[1,0]\) against \(J_a[0,1]\) gives the simple pole \(sL_a[0,0]\). The other axion field \(F[0,0]\) against \(J_a[0,0]\) gives \(-s(T+\lambda)L_a[0,0]\), with both a simple and a double pole. All pairs among \(L,E,F\) have regular products to this order. Reversing an even bracket gives the negative of the opposite orientation evaluated at \(-\lambda-T\), with \(T\) acting on the whole output. Thus the four formulas determine every pair and all translated inputs. The denominator \(N_r\) occurs only for the allowed, nonconstant \(E[r]\).

**Theorem (four-current algebra through second order).** Under the fourth-trace hypothesis and coupling relation above, the displayed brackets satisfy Jacobi for every triple of generators and their translates over \(R\). Their vertex algebra has a free \(R\)-basis of ordered monomials in the translated generators.

**Proof.** In the quadratic output, multiplication by a third transverse polynomial acts on the left at \(U\) and on the right at \(V\). Let \(f,g,h\) be the three transverse labels. After the product rule, one endpoint difference is \(f(U)-f(z_a)\), the integral of \(df(z_c)(U-V)\) from \(a\) to \(1\). Expand the other two endpoint differences along the same segment. After renaming the integration variables, all three terms have \(0<b<a<c<1\). Their sum contracts the alternating product of \(df(z_c),dg(z_a),dh(z_b)\) with \(U-V\) and the area bivector. Three covectors alternate to zero on a plane, so the Hochschild differential vanishes. Antisymmetrizing with the adjoint matrices gives the quadratic Jacobi terms for two positive currents and one negative current as well as for three positive currents.

For three positive currents the *linear* output tests a different cancellation. The open residual is the polarized adjoint fourth trace. Two successive axion brackets give the three products of pairings. Both multiply the same expression in \(T\) and the longitudinal bracket variables. Polarization gives the open prefactor \(\nu\gamma/3\) and the closed prefactor \(s^2\), whose sum vanishes. Jacobi with an external axion reduces to its displayed tree action at the retained order. Regularity among \(L,E,F\) removes the other nestings. For the basic form \(K(a,a)=\operatorname{tr}_4(a^2)\) on \(\mathfrak{sl}_4\), the diagonal matrices with entries \((1,-1,0,0)\) and \((1,1,-1,-1)\) require \(\gamma=10\) and \(8\), respectively. A single axion in the pure theory cannot cancel that quartic invariant. [The open and closed Ward terms](#ch14-celestial-closed-ward) · [Costello and Paquette, the gauge anomaly](https://doi.org/10.1103/PhysRevLett.129.231604)

For the basis assertion, give a generator of transverse index \(r\) filtration degree \(N_r+2\) and give \(T,\lambda\) degree zero. Every bracket lowers the sum of the input degrees, including the two-field output. Interchanging two adjacent generators gives the ordered pair plus lower-degree terms. On triples the difference of the two reorderings vanishes by the Jacobi identity just computed, using quasi-commutativity to order the normal products. The nonlinear Poincaré–Birkhoff–Witt construction consequently gives both spanning and independence. Each interchange is monic, so this works on the nilpotent layers of \(R\) without division by \(s\). [De Sole and Kac, Theorem 3.9, part 1, on the ordered basis over the complex numbers](https://arxiv.org/pdf/math-ph/0312042v3#page=9) ∎

The full vertex operators now define the translation-equivariant chiral algebra on the affine line over \(R\). To get the associative chiral operation, take its chiral Chevalley chains, retain the coproducts separating consecutive blocks, and apply cobar. On a separating open, a partition contributing to the chains splits into partitions of the two blocks. This gives the factorization maps used in that construction. Its unit at the empty configuration and its vacuum on the occupied line are supplied by their respective operations. [Associative products on configurations](#ch12-associative-products-on-configurations) · [Francis and Gaitsgory, §5.2](https://arxiv.org/pdf/1103.5803)

One projection admits an all-order scalar calculation independently of the four-current theorem over \(R\). In the mixed simple pole put a negative field first and a positive field second, labelled by monomials \(f,g\) of total degrees \(A,B\). At loop \(m\ge1\) require \(A,B\ge m\). Select \(m+1\) negative outputs and take the first \(m\) transverse indices to be zero. For incoming indices \(r,t\), the last index must be \(r+t-(m,m)\), with a negative component again giving zero. Put \(\mathcal D=\partial_{x_1}\partial_{y_2}-\partial_{x_2}\partial_{y_1}\), acting on \(f(x)g(y)\), and write \((a)_m=a(a-1)\cdots(a-m+1)\). Factor out \(\nu^m\) from the coefficient of the ordered colour word. The remaining scalar is the coefficient of the last output monomial \(x^{r+t-(m,m)}\) in
\[
 -\frac{(\mathcal D^m(f\otimes g))|_{y=x}}
        {m!(A)_m(A+B-m+1)_m}.
\]
The determinant contraction is forced up to a scalar by transverse \(SL_2\) covariance on the two homogeneous input spaces. Testing \(x_1^A,y_2^B\) evaluates the scalar by the angular beta integral. At two loops, for \(f=x_2^3,\ g=x_1^2\), move the sole degree-one output through the three slots. The ordered values are \(-1/4,-1/6,-1/12\), with the displayed terminal formula giving the last value. Summing the slots would hide their different matrix words. This all-order statement selects a specific output in the mixed gauge channel. [Ordered angular and mixed-helicity products](#ch14-celestial-reconstruction)

### The scalar bracket of transverse Hamiltonians {#ch19-scalar-hamiltonian-bracket}

Let \(k\) be a field of characteristic zero. On the transverse plane take coordinates \(x,y\) with \(\{x,y\}=1\). The pairs \((x^3,y^3)\) and \((x^2y,xy^2)\) have Poisson brackets \(9x^2y^2\) and \(3x^2y^2\). Subtracting three copies of the second bracket from the first gives zero. What happens to the same two pairs when their Hamiltonian vector fields act on the ordered one-loop coefficient \(\Phi\)?

Write \(U,W\) for the two endpoints of \(\Phi\), and \(X_P=\{P,-\}\) for the vector field of a polynomial \(P\). Its Lie derivative \(\mathcal L_P\) acts on a cochain by differentiating at both output points and subtracting the action on each input. A change of the ordered coefficient by \(\mathcal L_P\Phi\) has a unique primitive \(h_P\) vanishing on \(1,x,y\). Here the subscript is the Hamiltonian itself. A homogeneous \(P\) of positive degree \(d\) corresponds to the closed-current label \(dP\). The equation for the primitive is
\[
 (\mathcal L_P\Phi)(f,g)=f(U)h_P(g)-h_P(fg)+h_P(f)g(W).
\]
Taking \(g=x\) or \(y\) determines \(h_P\) successively on monomials. The two possible orders on \(xy\) agree because \(X_P\) preserves area. [The endpoint primitive in the cubic Ward identity](#ch19-cubic-ward-identity)

Apply first one Hamiltonian variation and then the other, antisymmetrize, and subtract the variation for their Poisson bracket. This gives the one-cochain \(Z=\mathcal L_P h_Q-\mathcal L_Q h_P-h_{\{P,Q\}}\). Its Hochschild differential vanishes because \([\mathcal L_P,\mathcal L_Q]=\mathcal L_{\{P,Q\}}\). Thus \(Z(fg)=f(U)Z(g)+Z(f)g(W)\). Computing \(Z(xy)=Z(yx)\) shows that \((U_x-W_x)Z(y)=(U_y-W_y)Z(x)\). The two coordinate differences are relatively prime, so there is a common polynomial factor \(\omega(P,Q)\) with
\[
 Z(f)=(f(U)-f(W))\,\omega(P,Q)(U,W).
\]
Setting \(U=W\) in \(Z(f)\) gives zero. To read the diagonal coefficient, divide \(Z(x)\) by \(U_x-W_x\) and then set \(U=W\).

For the first cubic pair the primitive equation on \(y,y\) gives \(h_{x^3}(y^2)=-(U_x-W_x)\). Since \(X_{y^3}x=-3y^2\) and every primitive vanishes on \(x\), one gets \(Z(x)=-3h_{x^3}(y^2)=3(U_x-W_x)\). The diagonal reading is \(3\). To compute it for all inputs, translate the common point to the origin. On homogeneous inputs of degrees \(r,s\) the factor \(\omega\) has degree \(r+s-6\), by counting derivatives in the primitive equation and removing the endpoint difference. A Hamiltonian \(P\) of degree at most two generates an infinitesimal affine symplectic transformation. It preserves \(\Phi\), so the normalized primitive \(h_P\) is zero. Covariance of the other primitive gives \(\mathcal L_P h_Q=h_{\{P,Q\}}\). These two identities make \(Z\), and hence \(\omega\), vanish whenever either Hamiltonian has degree at most two. Only the two cubic Taylor terms can therefore contribute at that point. The invariant pairing of two binary cubics is unique up to scale. It contracts three derivatives across the inputs.

::: {.definition #ch19-poisson-transvectant title="Poisson transvectant"}
Let \(V\) be a nonzero finite-dimensional symplectic vector space over \(k\), \(A=k[V]\) its polynomial functions, and \(\pi\) the Poisson bivector, with \(\pi(dx,dy)=1\) on a Darboux plane. In linear coordinates with components \(\pi^{ij}\), put \(\Pi=\sum_{i,j}\pi^{ij}\partial_i\otimes\partial_j\), and let \(\mu\) multiply the two polynomial factors. The \(m\)-th Poisson transvectant is \(B_m(f,g)=\mu\Pi^m(f\otimes g)\) for \(m\ge1\). In particular \(B_1=\{-,-\}\). On a single plane,
\[
 B_m(f,g)=\sum_{i=0}^m(-1)^i\binom mi
 (\partial_x^{m-i}\partial_y^i f)(\partial_x^i\partial_y^{m-i}g).
\]
:::

For \(x^3,y^3\) the third transvectant is \(36\), fixing the diagonal coefficient at \(B_3/12\). On \(x^2y,xy^2\) only \(i=1\) contributes, giving \(B_3=-12\) and diagonal coefficient \(-1\). The combination with zero Poisson bracket now gives \(3-3(-1)=6\). Retain this first correction from the flat transverse plane. If a formal parameter \(t\) gives it the coefficient \(tB_3/12\), which scalar brackets obey Jacobi at the higher orders of \(t\)?

::: {.definition #ch19-formal-local-scalar-bracket title="formal local scalar bracket"}
A formal local scalar bracket takes two elements of \(A[[t]]\) to an element of \(A[[t]]\). It is alternating and \(k[[t]]\)-bilinear. On polynomial inputs, the coefficient of each power of \(t\) must be a bidifferential operator of finite order with polynomial coefficients. Impose covariance under translations and the full linear symplectic group of \(V\). Fix the classical bracket at \(t=0\) to be \(B_1\), and require \([p,q]_t=\pi(p,q)\) exactly on all linear Hamiltonians \(p,q\in V^*\).
:::

::: {.proposition #ch19-scalar-bracket-classification title="invariant scalar brackets of polynomial Hamiltonians"}
With these covariance and normalization conditions, the brackets satisfying Jacobi are exactly
\[
 [f,g]_t=\sum_{j\ge0}\frac{\kappa(t)^j}{(2j+1)!}B_{2j+1}(f,g),
 \qquad \kappa(t)\in t\,k[[t]] .
\]
The first correction \(tB_3/12\) fixes \(\kappa'(0)=1/2\). If the coefficient of \(t^j\) lowers total input degree by \(4j+2\), this fixes \(\kappa(t)=t/2\). Every family with the same first correction takes this homogeneous form in the unique parameter \(t'=2\kappa(t)=t+O(t^2)\).
:::

::: {.proof #ch19-scalar-bracket-classification-proof}
Translation invariance makes the coefficients of every differential operator in the bracket constant. For a formal covector \(p\) put \(e_p(v)=\exp(p(v))\). Its coefficients in the components of \(p\) recover every coordinate monomial divided by its factorial. Thus the bracket of \(e_p,e_q\), divided by \(e_{p+q}\), determines the operation on all polynomials. This quotient is its symbol. It is polynomial in \(p,q\) at each order of \(t\) by finite differential order. Any two pairs with the same nonzero pairing \(z=\pi(p,q)\) are carried to each other by extending them to symplectic bases. On one plane evaluate the symbol at \((e_1,z e_2)\), where \(\pi(e_1,e_2)=1\). This gives a polynomial in \(z\) at each order. Equality on the dense locus \(z\ne0\) gives the whole symbol \(F(z)\). Alternation makes \(F\) odd. The exact bracket of linear Hamiltonians fixes \(F'(0)=1\) in \(k[[t]]\).

Write \(a=\pi(p,q),\ b=\pi(q,r),\ c=\pi(r,p)\) for three formal momenta. The term \([[e_p,e_q]_t,e_r]_t\) has symbol \(F(a)F(b-c)\), since \(\pi(p+q,r)=b-c\). Jacobi is therefore the polynomial identity, coefficient by coefficient in \(t\),
\[
 F(a)F(b-c)+F(b)F(c-a)+F(c)F(a-b)=0 .
\]
Already on one plane every triple with \(a\ne0\) occurs by taking \(p=e_1,\ q=a e_2,\ r=-(b/a)e_1-c e_2\). Hence the three variables can be varied independently. Differentiate in \(c\) at zero. Oddness of \(F\) and \(F'(0)=1\) give \(F(a-b)=F(a)F'(b)-F(b)F'(a)\). Changing the sign of \(b\) gives the addition formula
\[
 F(a+b)=F(a)F'(b)+F(b)F'(a).
\]
Two derivatives in \(b\) at zero now give \(F''(a)=\kappa F(a)\), where \(\kappa=F'''(0)\), since \(F''(0)=0\). With \(F(0)=0,\ F'(0)=1\), the recursion on coefficients gives \(F(z)=\sum_{j\ge0}\kappa^j z^{2j+1}/(2j+1)!\). The classical fibre gives \(\kappa(0)=0\). Conversely, the binomial formula for this series gives the subtraction identity above. Substituting it in the cyclic sum cancels the terms in pairs. The symbol of \(B_m\) is \(z^m\), which gives the stated bracket. At each order of \(t\) only finitely many terms occur. For fixed polynomial inputs every contraction beyond the smaller input degree vanishes.

Finally \(B_3\) has coefficient \(\kappa/6\) and lowers total degree by six. In the homogeneous grading it can occur only at order \(t\), so the prescribed \(1/12\) forces \(\kappa=t/2\). Without the grading, the same coefficient fixes \(t'=2\kappa(t)\) uniquely, and its unit linear term gives a formal inverse.
:::

The quintic contraction is already necessary on one plane. At \((a,b,c)=(1,2,3)\), retaining only \(F(z)=z+tz^3/12\) leaves a Jacobi coefficient at \(t^2\) of \(\sum_{\rm cyc}a^3(b-c)^3/144=36/144=1/4\). In the homogeneous parameter the linear and quintic terms contribute \(\sum_{\rm cyc}(a^5(b-c)+a(b-c)^5)/480=-120/480\), which cancels it. On the polynomial triple \((x^5,y^5,x^2y)\) the same omission leaves \(600t^2x\) in the left-nested Jacobiator. This failure survives passage modulo constants.

There is an independent construction of the bracket. With formal parameter \(u\) the Moyal product is \(f\star_u g=\mu\exp(u\Pi/2)(f\otimes g)\). Multiplying three exponential generators in either order of association adds the same three pairings in the exponent. The divided commutator \((f\star_u g-g\star_u f)/u\) has symbol
\[
 \frac{\exp(uz/2)-\exp(-uz/2)}{u}
   =z+\frac{u^2z^3}{24}+\frac{u^4z^5}{1920}+\cdots .
\]
Thus \(\kappa=u^2/4\). In the homogeneous parameter set \(t=u^2/2\). For a general marked bracket first pass to \(t'=2\kappa(t)\), then set \(t'=u^2/2\). The distinction is visible on \(x^4,y^3\), for which \(B_3=144x\) and \(B_5=0\). If \(\kappa=t/2+t^2/7\), direct substitution of \(t=u^2/2\) adds \(6u^4x/7\) to the Moyal answer. Substitution in \(t'\) gives the divided commutator exactly. [Moyal, *Quantum mechanics as a statistical theory*](https://doi.org/10.1017/S0305004100000487) · [Fairlie, Fletcher and Zachos, *Trigonometric structure constants for new infinite-dimensional algebras*](https://doi.org/10.1016/0370-2693%2889%2991418-4)

Constants have zero bracket, so the scalar bracket descends to \(\mathfrak h=A/k\), identified at \(t=0\) with the polynomial Hamiltonian vector fields by \(P\mapsto X_P\). The induced local operations still detect the full symbol. Indeed, if their difference has constant output on every polynomial pair, differentiating its exponential output in the spatial coordinate \(v_i\) gives \((p_i+q_i)\) times its symbol, times \(e_{p+q}\). This forces the symbol to vanish. For the Jacobiator the factor is \(p_i+q_i+r_i\), with the same consequence.

::: {.corollary #ch19-scalar-quotient-class title="the diagonal class modulo constants"}
The first correction \(B_3/12\) gives a nonzero class in the adjoint Chevalley–Eilenberg cohomology \(H^2(\mathfrak h,\mathfrak h)\). A \(k[[t]]\)-linear change of Hamiltonians equal to the identity modulo \(t\) cannot carry the marked bracket to the undeformed Poisson bracket.
:::

::: {.proof #ch19-scalar-quotient-class-proof}
Jacobi to first order says \(B_3/12\) is a cocycle. The opening cubic pairs give constants and lose their distinguishing values in \(\mathfrak h\). Use \((x^4,y^3)\) and \((x^3y,xy^2)\) instead. Their Poisson brackets are \(12x^3y^2\) and \(5x^3y^2\), so taking five times the first minus twelve times the second gives zero. For any \(k\)-linear map \(\alpha:\mathfrak h\to\mathfrak h\), its coboundary on \(f,g\) is
\[
 \{f,\alpha(g)\}-\{g,\alpha(f)\}-\alpha(\{f,g\}).
\]
The last terms cancel in this combination. The vector fields of all four inputs vanish to order at least two at the origin. Thus the two action terms have zero first derivative there for every polynomial representative of the values of \(\alpha\), even in additional symplectic coordinates. The two third transvectants are \(144x\) and \(-36x\). The same combination for \(B_3/12\) gives \(96x\), whose \(x\)-derivative survives modulo constants. This excludes every linear primitive. The first coefficient of a linear change trivializing the bracket would be such a primitive.
:::

::: {.open-problem #ch19-scalar-field-comparison title="comparison with the celestial fields"}
Can the scalar bracket be realized by operations on the full celestial fields? Its first correction reads a diagonal coefficient of two Hamiltonian variations of the flat one-loop simplex. The ordered mixed pole retains separate output jets, helicities and colours. A comparison would have to reproduce these field operations and their longitudinal descendants. Covariance of the full fields under changes of transverse coordinates, descent to a curved transverse surface and a coproduct for two independently prepared lines each require a compatible field map. An ordered product must retain the unit, so return from Hamiltonians modulo constants to polynomial functions themselves. Even there the normalized Lie bracket leaves the symmetric part of multiplication and the scale of the commutator to be determined. [Ordered angular coefficients](#ch14-celestial-reconstruction) · [The closed-current simple pole](#ch19-closed-current) · [Tensor products of line modules](#ch14-celestial-ordered-transport)
:::

### The coefficient ring of the ordered Hamiltonian product {#ch19-scalar-associative-lift}

Write \(L_\kappa\) for the [classified scalar bracket](#ch19-scalar-hamiltonian-bracket). On the polynomial functions \(A=k[V]\) it gives \(L_\kappa(x,y)=1\) for a Darboux pair. The Moyal orders are \(xy+u/2\) and \(xy-u/2\), with common symmetric part \(xy\) and difference \(u\). Could an associative product with the same locality and symmetries give the divided bracket over \(R=k[[t]]\) itself? Write its commutator as \(dL_\kappa\). The pair \(x,y\) would read \(d\). On \(x^4,y^3\) the same \(d\) must multiply \(12x^3y^2+24\kappa(t)x\).

::: {.proposition #ch19-scalar-associative-square title="associative realization of the scalar bracket"}
Let \(A=k[V]\) for a nonzero finite-dimensional symplectic \(V\) over a characteristic-zero field \(k\), and let \(0\ne\kappa\in tR\). Consider an associative \(R\)-bilinear product on \(A[[t]]\). Require that it have unit \(1\) and reduce to ordinary multiplication modulo \(t\). Translations and all linear symplectic transformations must preserve it. At each order of \(t\) its coefficient on polynomial inputs must be a bidifferential operator of finite order with polynomial coefficients. Within this class, the products whose commutator is \(dL_\kappa\) for some nonzero \(d\in R\) are precisely the following. Choose \(w\in tR\) with \(w^2=\kappa\) and put \(B_0(f,g)=fg\). Then
\[
 f\star_w g=\sum_{n\ge0}\frac{w^n}{n!}B_n(f,g),\qquad d=2w .
\]
Changing \(w\) to \(-w\) reverses the order of multiplication.
:::

::: {.proof #ch19-scalar-associative-square-proof}
Use the same exponential generators \(e_p\) as for the Lie bracket. The symplectic group acts transitively on each fibre of a fixed nonzero pairing. Their union is dense and open. Polynomial continuation at each formal order therefore gives \(e_p\star e_q=G(\pi(p,q))e_{p+q}\). The unit fixes \(G(0)=1\). For the three pairings \(a=\pi(p,q), b=\pi(q,r), c=\pi(r,p)\), the two associations give
\[
 G(a)G(b-c)=G(b)G(a-c).
\]
These variables vary independently, so setting \(b=0\) gives \(G(a+v)=G(a)G(v)\) with \(v=-c\). Differentiating at \(v=0\) gives \(G'=wG\), where \(w=G'(0)\), hence \(G(z)=\exp(wz)\). Reduction to the ordinary product puts \(w\) in \(tR\). Conversely the exponential satisfies the associativity identity. The coefficient of \(z\) in \(G(z)-G(-z)\) gives \(d=2w\). Comparing the cubic terms gives \(2w^3=d\kappa\). The nonzero scalar \(d\) cancels in the domain \(R\), leaving \(w^2=\kappa\). All higher odd coefficients then agree. [Moyal, *Quantum mechanics as a statistical theory*](https://doi.org/10.1017/S0305004100000487)
:::

For the marked bracket \(\kappa=t/2+O(t^2)\), the first nonzero term has odd degree in \(t\), whereas every nonzero square in \(R\) has even order. Adjoin the missing square root. The ring \(R'=R[w]/(w^2-\kappa(t))\) is free over \(R\) on \(1,w\). Inverting the series \(\kappa(t)\) under composition identifies \(R'\) with \(k[[w]]\). The canonical parameter and the Moyal parameter are \(t'=2\kappa\) and \(u=2w\). Any root of \(\kappa\) in a complete local domain extending \(R\) determines a coefficient map from \(R'\). In a discrete valuation extension with ramification index \(e\) one has \(2v(w)=v(\kappa)=e\), so this extension attains the least possible index, two.

There are two different specializations. Modulo \(w\), multiplication on \(A\) is ordinary. Modulo \(t\), the coefficients are \(k[w]/(w^2)\) and the product of plain polynomial inputs is \(fg+w\{f,g\}\). The raw commutator of \(x,y\) is \(2w\) and survives on this latter fibre. This also rules out associative descent through an arbitrary algebra isomorphism. Suppose an \(R\)-algebra \(C\) gave the marked product after extension to \(R'\). Reduction modulo \(w\) would identify \(C/tC\) with the commutative algebra \(A\). Thus every commutator in \(C\) belongs to \(tC\), and every extended commutator would belong to \((t)=(w^2)\). The value \(2w\) contradicts this. Finite freeness gives the same argument for the completed tensor product of a separated \(t\)-adically complete \(C\).

Two operations on functions do descend. The even part of the ordered product is its symmetrization
\[
 J_\kappa(f,g)=\sum_{j\ge0}\frac{\kappa^j}{(2j)!}B_{2j}(f,g).
\]
This is a unital Jordan product. The raw commutator divided by \(2w\) gives \(L_\kappa\). In the associative algebra, four times the left-minus-right associator of the symmetrized product is the double commutator \([g,[f,h]_{\star}]_{\star}\), where the subscript denotes the raw commutator. Since \(R\to R'\) is injective, this gives on \(A[[t]]\)
\[
 J_\kappa(J_\kappa(f,g),h)-J_\kappa(f,J_\kappa(g,h))
      =\kappa L_\kappa(g,L_\kappa(f,h)).
\]
For \(f=x^2,g=y,h=y^2\) the inner bracket is \(4xy\) and the outer bracket is \(-4y\). The two symmetric products therefore differ by \(-4\kappa y\). Constants can be divided out for the Lie operation. The Jordan operation uses actual functions since \(J_\kappa(1,f)=f\).

Restriction of scalars keeps both components of a function \(a+wb\), with \(a,b\in A[[t]]\). Multiplying \(a+wb\) by \(c+wd\) with the product \(J_\kappa+wL_\kappa\) gives a pair with components
\[
\begin{aligned}
 (\,\cdot\,)_0={}&J_\kappa(a,c)+\kappa J_\kappa(b,d)\\
                 &+\kappa\big(L_\kappa(a,d)+L_\kappa(b,c)\big),\\
 (\,\cdot\,)_1={}&J_\kappa(a,d)+J_\kappa(b,c)\\
                 &+L_\kappa(a,c)+\kappa L_\kappa(b,d).
\end{aligned}
\]
For \((x,0),(y,0)\) the two orders give \((xy,1)\) and \((xy,-1)\). Their commutator \((0,2)\) exhibits what the second copy remembers. This associative algebra over \(R\) has carrier \(A[[t]]\oplus A[[t]]\). A realization on the celestial fields would also have to identify their separately labelled pole coefficients. [The closed-current simple pole](#ch19-closed-current)

## A closed current at the next order {#ch19-closed-current}

The ordered Hamiltonian product determines a bracket on scalar functions. A pole of two celestial fields must also specify each output field, its transverse Taylor label and, for a gauge current, its colour. Does the proposed cubic correction to the [four celestial currents](#ch19-four-currents) satisfy Jacobi when an axion acts on two ordered gauge insertions?

For this test pass to \(\mathbb C[s]/(s^4)\), take \([h,e]=2e,\ [h,f]=-2f,\ [e,f]=h\) in \(\mathfrak{sl}_2\), and normalize \(K(h,h)=2,\ K(e,f)=1\). Then \(\gamma=8\) and \(\nu=-3s^2/8\). Insert the axion current \(A=E[3,0]\) and the ordered positive-helicity gauge currents \(B=J_h[0,1]\), \(C=J_e[0,1]\). In each nesting take the simple-pole coefficient of the inner pair first, then its simple pole with the remaining field. In these zeroth products the Jacobiator is \([A,[B,C]]-[[A,B],C]-[B,[A,C]]\).

**Counterexample (shifted-index formula for the axion current).** The inner \(E,J\) bracket produces a negative current. Its bracket with the other positive current carries the two simplex weights \(-1/3,-2/3\). The putative higher \(E,J\) term in Fernández–Paquette (B.12) uses the first transverse argument \((3,0)-(1,1)=(2,-1)\), so that prescription gives zero. It leaves the Jacobiator
\[
 \frac{2s\nu}{3}
 \bigl(:L_h[0,0]L_e[1,0]:-:L_e[0,0]L_h[1,0]:\bigr).
\]
The first coefficient is \(-s^3/4\), and the two colour assignments give independent classical ordered monomials. Thus this prescription fails at precisely the first order discarded in the four-current theorem. The unequal jets locate a missing closed-current simple pole. [Fernández and Paquette, (B.12)](https://arxiv.org/pdf/2412.17168v2#page=52)

The inner tree bracket of the two gauge currents is \(2J_e[0,2]\), since \([h,e]=2e\) and their transverse labels multiply. The axion acting on this composite is the only place where a new cubic term can enter. The coefficient \(-s^3/4\) above is the residual of the three-current identity on \(:L_h[0,0]L_e[1,0]:\). To cancel it, the cubic simple pole of \(E[3,0]\) with \(J_e[0,2]\) must contribute \(+s^3/8\) on that word before multiplication by two. [The cubic identity for all transverse polynomials](#ch19-cubic-ward-identity)

Does the coefficient just forced on this ordered word belong to a family of axion simple poles at every loop order? To test this on one transverse axis, restrict the positive inputs to \(J_a[0,n]\) and quotient the algebra of negative fields by those with strictly positive second transverse index and their translates. This ideal is stable. If the incident negative field has second index \(t_2\), the second indices of its outputs sum to \(t_2+n-m\) at loop \(m\le n\). For \(t_2>0\) some output belongs to the ideal. For \(t_2=0\) only \(m=n\) can survive. Killing every nonzero jet would lose stability, since the action on a first jet can already give a quadratic zero-jet output.

Let \(\mathfrak g\) now be a finite-dimensional Lie algebra over a characteristic-zero field \(k\) with nondegenerate invariant symmetric form \(K\). Put \(\kappa=-2K\) and \(X_p=\kappa^{-1}L[p,0]\), so the metric turns the negative current into a vector of commuting coordinate functions. Write \(A=k[X_p^i:p\ge0][[\epsilon]]\) for their polynomial algebra completed in the loop parameter \(\epsilon=\hbar/(16\pi^2)\). The formal variables \(u,v\) record the first index of the negative current and the second index of the positive current, respectively. Put \(X(u)=\sum_{p\ge0}X_pu^p,\ C(u)=\partial_u(uX(u))\). The ordered integrals of the simple poles give the parallel transport
\[
 \partial_u U_v=2\epsilon v\,\operatorname{ad}_{C(u)}U_v,
 \qquad U_v(0)=1.
\]
Later times multiply on the left. For colour \(a\), let \(D_{a,n}\) be the simple-pole action of \(J_a[0,n]\) on \(A\). Its generating series \(D_a(v)=\sum_{n\ge0}v^n D_{a,n}\) satisfies
\[
 D_a(v)X(u)=\frac{(U_v(u)-1)a}{2\epsilon uv}.
\]
The numerator is divisible by \(\epsilon uv\). Its first term gives \(D_{a,0}X_p=[X_p,a]\). Vary the transport equation at a second parameter \(w\) under \(D_a(v)\). The solution involves the divided difference of the bracket of the two transported colours and the transport of their bracket. At equal parameters these agree, since parallel transport preserves the Lie bracket. Antisymmetrizing the two variations then gives \([D_{a,m},D_{b,n}]=D_{[a,b],m+n}\). This constructs a representation of the polynomial current Lie algebra on \(A\) at every order in \(\epsilon\).

The axion simple pole needs a vector to pair with its incident colour. Rescale the transport interval to \(0\le t\le1\), put \(C_t=\partial_t(tX(ut))\), and use the parameter \(q=\epsilon uv\). To extract coefficients, regard \(q,u\) as independent and solve \(\partial_tU_q(t)=2q\operatorname{ad}_{C_t}U_q(t),\ U_q(0)=1\). Define
\[
                  \Psi(q,u)=\int_0^1U_q(t)^{-1}C_t\,dt .
\]
Its adjoint action is \(\tfrac12 U_q(1)^{-1}\partial_qU_q(1)\). The vector integral also retains any central component. For \(m,N\ge0\), pair \([q^m u^N]\Psi\) with the colour \(a\) using \(\kappa\), then multiply by \(s\epsilon^m\). This gives the closed simple-pole contribution in the axis quotient for \(E[m+N+1,0]\) against \(J_a[0,m+1]\). In particular the term linear in \(u\) is
\[
 [q^m u]\Psi=\frac{2(-2)^m}{(m+2)!}
                         (\operatorname{ad}_{X_0})^m X_1 .
\]
To obtain it, linearize the transport around \(X_0\). The remaining integral is \(2\int_0^1(1-t)\exp(-2qt\,\operatorname{ad}_{X_0})X_1\,dt\). Thus the first correction is \(-2[X_0,X_1]/3\). In the compact three-colour basis with \(\varepsilon_{012}=1,\ K=-I/2\), one has \(\kappa=I\). In the \(E[3,0],J_b[0,2]\) orientation, the full tree term is \(2sL_b[2,1]\), which projects to zero on the axis. The quadratic term survives there with coefficient \(-2s\epsilon/3\) on \(\varepsilon_{bde}:X_0^d X_1^e:\). This is the missing term detected by the unequal-jet calculation. For fixed \(E\)-index the resulting linear assignment \(\beta\) to each positive current is a Chevalley–Eilenberg cocycle on the quotient. Its equation is \(D_j\beta(k)-D_k\beta(j)=\beta([j,k])\) for currents \(j,k\).

At \(u=0\) the integrand is \(X_0\), so \(\Psi(q,0)=X_0\). In the balanced Ward test the two incident positive currents have jets \((m,0)\) and \((0,m)\). Test their pole with a third current of constant transverse label and retain only negative currents with zero output jet. The positive-loop closed correction vanishes on that output. Thus the ordered colour-chain double pole and its one-derivative companion retain their values in this test. A spectator of positive transverse degree detects an additional term in the [quartic double pole of the marked currents](#ch19-marked-sl2-cubic-closure). With general incident and outgoing jets one must also satisfy the longitudinal double-pole and derivative equations. The axis action gives a specific family of simple poles at every order. A lift of the whole algebra modulo \(s^4\) requires the other brackets and Jacobi identities at order \(s^3\). [The balanced Ward calculation and its normalization](#ch14-celestial-closed-ward)

Two modules for this current action can share the negative-coordinate algebra \(A\). If \(M,N\) carry compatible current derivations, then \(j(m\otimes n)=(jm)\otimes n+m\otimes(jn)\) descends to \(M\otimes_A N\). Moving \(f\in A\) across the tensor sign gives the same extra term \(D_j(f)\) on either side. The counit on the action algebra sends an operator \(P\) to \(P(1)\in A\).

For independent backgrounds \(X_0^L,X_0^R\), test the rule that adds them and acts on the two factors separately. The first nonlinear term is \(D_{a,1}X_1=\epsilon[X_0,[X_0,a]]\). Substitution of \(X_0^L+X_0^R\) produces the two cross commutators. In the split basis above, \(X_0^L=e,\ X_0^R=f,\ a=h\) gives \(4\epsilon h\) beyond the sum of the separate actions. A fusion of independently prepared physical lines must supply a map accounting for this value and the closed cocycle. [Ordered transport and tensor products](#ch14-celestial-ordered-transport)

### The cubic Ward identity on the transverse plane {#ch19-cubic-ward-identity}

Consider the formal vacuum algebra of pure self-dual Yang–Mills theory coupled to its anomaly-cancelling axion. In type \(A_2\) take gauge algebra \(\mathfrak{sl}_3\) with \(K(a,b)=\operatorname{tr}_3(ab)\). The polynomials in \(x,y\) label Taylor modes transverse to the celestial line. Insert a closed axion current \(E[x^2y]\) and two positive-helicity gauge currents, \(J_{12}[x]\) followed by \(J_{23}[y]\). The subscripts on the gauge currents denote the matrix units \(E_{ij}\). Their colours bracket to \(E_{13}\), so their tree bracket contains \(J_{13}[xy]\). When the axion at \(z\) approaches this highest-root current at \(w\), what is the coefficient of the normal product \(:L_{12}[1,0]L_{23}[0,0]:\) in the simple pole at cubic order in the axion coupling \(s\)? The two \(L\)'s have negative helicity. The first carries the transverse label \(x\), the second the constant label.

Write \(E[p]_{(0)}J_c[t]\) for the coefficient of \(1/(z-w)\) in the product \(E[p](z)J_c[t](w)\), with its output fields at \(w\). This is the positively oriented residue in \(z\), or the contour integral divided by \(2\pi i\). Keep the four-current brackets through order \(s^2\), with \(s\) the axion coupling and \(\nu\) the open one-loop coefficient. The cubic term has order \(s\nu\). For arbitrary positive currents \(J_a[f],J_b[g]\) in that order, the Jacobi identity equates the axion acting on their bracket to the sum of its actions on the two inputs. Their difference, with only the lower brackets inserted, is the residual. At tree level the axion differentiates the transverse label of a positive current and produces a negative one. Each quadratic term of the one-loop gauge product has one positive current, on which the axion acts, and one negative current, with which its product is regular. The two orderings of the simplex coefficient place the positive label at opposite endpoints, so both endpoint derivatives occur. In the other two nestings of Jacobi the axion differentiates \(f\) or \(g\) before the ordered product is taken. Subtracting the two input variations from the output variation gives the term the cubic pole must cancel.

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

For reductive colour \(\mathfrak g=\mathfrak s\oplus\mathfrak z\), this freedom lies entirely on the centre. For each axion label \(p\), a homogeneous correction maps \(\mathfrak z\otimes A_{\ge2}\) linearly into \(\operatorname{Sym}^2(\mathfrak z\otimes A)\) and vanishes on the other modes. Every such family of maps gives a correction if it has the stated degrees and covariance in both polynomial inputs. These families exhaust the choices. In fact invariance under \(a\otimes1\) and \(a\otimes x\) implies that the adjoint action in the first slot is killed by \(U_x-V_x\). This difference acts injectively on polynomial coefficients, so each slot must be separately central. If sign reversal of the central summand is also a required symmetry, the central input changes sign and the quadratic output keeps its sign, eliminating this freedom. Coefficients supported on the collision \(U=V\) require a separate argument.

The \(EJJ\) identity now holds at order \(s^3\) for all transverse polynomial inputs with the stated lower brackets. To construct a cubic vertex algebra one must also check \(FJJ\) and the identity for three positive currents. In the pure \(\mathfrak{sl}_2\) theory these equations enter the proof of an ordered basis over \(\mathbb C[s]/(s^4)\). Flatness of the derived chiral cuts requires a further comparison on the coefficient complexes.

### Three positive currents in the marked cubic algebra {#ch19-marked-sl2-cubic-closure}

The cubic identity with one \(E\) insertion leaves a test on three positive currents. Work now in the pure \(\mathfrak{sl}_2\) gauge theory with its anomaly-cancelling axion, \(K(a,b)=\operatorname{tr}_2(ab)\), axion coupling \(s\), and \(\nu=-3s^2/8\). Let the transverse \(\mathrm{SL}_2\) act linearly on the four polynomial towers. Insert \(J_e[x^2]\) at \(z\) and \(J_f[y^2]\) at \(0\), with \([e,f]=h\). In the vacuum simple pole, select the ordered word \(:F[1]L_h[1]:\), where \([1]\) means the **constant transverse polynomial** on each field. In units of \(s\nu\) the coefficient \(i\) in Fernández–Paquette gives \(-2\). On the same two colours with transverse inputs \(xy,xy\) it gives zero. These values satisfy the three-current Ward equation. Yet the transverse raising operator \(x\partial_y\) applied to the inputs \(y^2,xy\) gives \(2xy,xy\) and \(y^2,x^2\). The constant output has zero raising action. A covariant coefficient must therefore obey \(2i(xy,xy)+i(y^2,x^2)=0\), whereas the displayed values give \(-2\). Which simple pole does the linear action select? [Fernández and Paquette, §§2.5, 3.2 and Appendix B.4](https://arxiv.org/pdf/2412.17168v2) · [Costello and Paquette, §§4.3 and 7.2](https://arxiv.org/pdf/2201.02595v3)

Write \(U,V\) for the transverse variables on the closed and negative output, respectively. For polynomial labels \(p,q\), put \(z_\rho=V+\rho(U-V)\). For incoming colours \(a,b\), select the output \(:FL_{[a,b]}:\) in the simple pole. In units of \(s\nu\), its covariant coefficient is
\[
\begin{aligned}
 D_F(p,q)&=-\int_0^1\!\int_0^1\min(v,w)\,H_2(v,w)\,dv\,dw,\\
 H_2(v,w)&=p_{xx}(z_v)q_{yy}(z_w)-2p_{xy}(z_v)q_{xy}(z_w)\\
         &\qquad+p_{yy}(z_v)q_{xx}(z_w).
\end{aligned}
\]
The two Hessians are evaluated at separately labelled points. One way to obtain the weight is to compute on \(p=x^m,q=y^n\) by stripping a final \(y\) from the ordered simplex. The endpoint term and the integral along the remaining segment give \(vw+vw(1/\max(v,w)-1)=\min(v,w)\) in the interior. Powers of independent linear forms follow by linear symplectic change of coordinates and scaling. Polynomiality extends to dependent forms, and pure powers span each homogeneous degree. At \(U=V\) the integral is \(-B_2(p,q)/3\), since the minimum integrates to \(1/3\). For the two opening pairs \(H_2\) is the constant \(4\) or \(-2\). Their coefficients are thus \(-4/3,+2/3\), satisfying the raising identity. The ordered cubic simple pole on the first pair has coefficient \((-4/3)s\nu=s^3/2\).

To describe the longitudinal terms, let \(d_E,d_L\) translate individual factors of an \(:EL:\) word and put \(\mathcal E_U=U_x\partial_{U_x}+U_y\partial_{U_y}\). For homogeneous transverse inputs \(p,q\), let \(\alpha,\beta\) be the incoming momenta. In a binary bracket \(\alpha=\lambda,\ \beta=-\lambda-d_E-d_L\). In the same units and colour, the three \(:EL:\) coefficients are specified by
\[
\begin{aligned}
 D_E(p,q)={}&(|p|d_E+\alpha\mathcal E_U)\Phi(p,q)\\
            &+(|q|d_E+\beta\mathcal E_U)\Phi(q,p).
\end{aligned}
\]
Here \(|p|,|q|\) are polynomial degrees and \(E\) has no field with constant transverse Taylor label. Substitution for \(\beta\) gives the double pole, the derivative on \(E\), and the derivative on \(L\) separately. These agree with the three corresponding primary coefficients. The two closed–positive brackets also enter the algebra at this order. The \(EJ\) operation is the primitive in the [cubic Ward identity](#ch19-cubic-ward-identity). For \(F[p]{}_\lambda J_c[q]\) and homogeneous \(p\), including \(1\), the cubic part is
\[
 s\nu\,Q\!\left(\Xi_c
       \left[d_1+\lambda\,\frac{2+\mathcal E_U}{|p|+2}\right]\Phi(p,q)\right).
\]
In this formula both outputs are negative, \(\Xi_c=\sum_i u_i\otimes[u^i,c]\) in trace-dual bases, \(Q\) forms the normal product, and \(d_1\) translates its first factor. Interchange of factors interchanges their colours, labels and derivatives together. The \(FJJ\) Ward equation follows by applying the endpoint cocycle identity of \(\Phi\) in its three orders. The product rule for \(\mathcal E_U\) supplies the input degree in the coefficient of \(\lambda\). The \(EJJ\) and \(FJJ\) operations extend by linearity in the labels. [Four-current brackets and the endpoint actions](#ch19-four-currents) · [Fernández and Paquette, §§3.2, 3.4](https://arxiv.org/pdf/2412.17168v2)

::: {.theorem #ch19-marked-sl2-cubic-pbw title="the marked cubic four-current algebra"}
The gauge currents \(J,L\) and the axion currents \(E,F\) are all even. In the pure \(\mathfrak{sl}_2\) gauge theory coupled to its axion, fix their brackets through order \(s^2\). Here \(s\) is the axion coupling, \(K(a,b)=\operatorname{tr}_2(ab)\), and \(\nu=-3s^2/8\). Add the cubic \(EJ\) and \(FJ\) brackets and the \(JJ\) correction given above. The resulting brackets satisfy Jacobi through order \(s^3\) for every triple of generators and all their longitudinal derivatives.

Keep the lower brackets and the cubic \(EJ,FJ\) brackets fixed. Consider cubic \(JJ\) corrections with local polynomial coefficients in the field and degree classes allowed by these couplings. A local change of \(J\) starting at order \(s^3\) relates any two solutions of Jacobi in this class. Exactly one correction in this class is equivariant for the prescribed linear transverse \(\mathrm{SL}_2\) action.

Use \(J,L,F\) at all transverse Taylor labels and \(E\) at positive transverse degree. This omits \(E[0,0]\) and all its longitudinal derivatives. Ordered normal monomials in the resulting strong generators and their longitudinal derivatives form a basis of the universal enveloping vertex algebra over \(\mathbb C[s]/(s^4)\). Its vertex products define a translation-equivariant relative chiral algebra on the affine line.
:::

::: {.proof #ch19-marked-sl2-cubic-pbw-proof}
At cubic order the graph degree and curve spin allow \(JJ\) to produce one closed and one negative field. The \(FL\) word has a simple pole. The \(EL\) word has one longitudinal momentum. A closed–positive pair can produce two negatives, with one longitudinal momentum for \(FJ\) and none for \(EJ\). The mixed \(LJ\) channel has only even orders through this range, and \(\{L,E,F\}\) are mutually regular. The graph inequalities for the number of axion vertices and legs exclude two closed factors. [Fernández and Paquette, (2.19)–(2.21)](https://arxiv.org/pdf/2412.17168v2#page=19)

In the \(JJJ\) equation a tree axion exchange can hit the \(J\) in the one-loop \(:JL:\) word. The \(L\) is left in the output throughout this contraction. The other contributions are the tree action on the \(L\) of a cubic word and the cubic bracket on an inner tree current. The Wick integral ends in a regular closed–negative bracket. Use independent contour variables \(\lambda,\mu\), so the third momentum is \(-\lambda-\mu-d_E-d_L\) in the \(EL\) channel. Acting on a differentiated spectator shifts its translation by the acting momentum. The colour of each contribution is a cyclic permutation of \([[a,b],c]\). Lie Jacobi cancels the cyclic colour terms when their scalar coefficients agree. Testing the triples \(h,e,f\) and \(h,h,e\) forces those coefficients to agree, so the condition is also necessary.

Here is the cancellation on polynomial labels \(p,q,r\). For a monomial \(p=x^{p_x}y^{p_y}\) with incoming momentum \(\alpha\), write \(D_p=|p|d_E+\alpha\mathcal E_U\) in the \(E\) component. In the \(F\) component take \(D_p(U^kV^l)=(p_x k_y-p_y k_x)U^{k-(1,1)}V^l\), retaining nonnegative outputs after the indicated polynomial operations. Use the respective incoming momentum for \(D_q,D_r\). The representative \(\Theta^0(p,q)=D_p\Phi(p,q)+D_q\Phi(q,p)\) gives the three \(E\) coefficients and the uncorrected \(F\) coefficient. Expanding the three contributions just described, the coefficient of \([[a,b],c]\) is
\[
\begin{aligned}
 &D_p\big(p(U)\Phi(q,r)\big)+D_q\big(q(U)\Phi(p,r)\big)\\
 &\qquad-\Theta^0(pq,r)-r(V)\Theta^0(p,q).
\end{aligned}
\]
In \(\Theta^0(pq,r)\) the momentum of \(pq\) is the sum of those of \(p,q\). The endpoint identity \(p(U)\Phi(q,r)-\Phi(pq,r)+\Phi(p,qr)-\Phi(p,q)r(V)=0\) changes the displayed expression to
\[
 -D_p\Phi(p,qr)-D_q\Phi(q,pr)-D_r\Phi(r,pq).
\]
This is symmetric in all three labelled inputs, coefficient by coefficient in the momenta and output translations. It proves the Ward identity for this representative, including the two derivative placements.

Fix the lower brackets and the cubic \(EJ,FJ\) brackets, and compare two solutions for the cubic \(JJ\) bracket. Their \(F\) coefficients differ by a symmetric Hochschild cocycle. Both module actions multiply by the input polynomial evaluated at the negative endpoint \(V\). The cocycle has the form \(\eta(pq)-p(V)\eta(q)-q(V)\eta(p)\). Indeed, assigning \(\eta\) on a monomial times \(x\) or \(y\) by this equation gives the same value under an adjacent interchange by symmetry and the cocycle identity. The coefficient of \(d_E\) obeys the same argument. For the remaining spectral terms write the difference as \(\alpha B(p,q)+\beta B(q,p)\). Its cocycle identity at \(\alpha\) gives \(B(p,q)=B(1,pq)-q(V)B(1,p)\), also a change of the unary current. These are precisely the local positive-current changes in the allowed class.

Averaging a solution on each finite homogeneous input space over the transverse compact group \(\mathrm{SU}_2\) preserves the Ward equation and gives a covariant solution. An equivariant unary change on degree \(n\) would have output of total degree \(n-4\) for \(FL\) or \(n-2\) for the \(EL\) changes. All output highest weights are strictly below \(n\), so such a change vanishes. For the \(F\) term the covariant solution vanishes on \((z^{n-1},z)\) for a linear form \(z\), by the same highest-weight bound. Subtract the coboundary above from \(\Theta^0_F\). Its unary coefficient is fixed by \(\eta(z^n)=\Theta^0_F(z^{n-1},z)+z(V)\eta(z^{n-1})\), zero in degrees below four. Polarization gives every monomial. In degree four it gives \(\eta(x^2y^2)=-2/3\), shifting both opening entries by \(+2/3\). The integral computes this covariant solution. The change relates the printed \(F\) representative to the marked one with the corrected companion brackets. The shifted-index \(EJ\) pole still fails the [unequal-jet test](#ch19-closed-current).

Of the twenty unordered generator triples, \(JJJ\) is now settled. The \(EJJ\) and \(FJJ\) equations use their respective two-negative-current operations. In \(LJJ\) the even orders of \(LJ\) and regularity of \(L\) with the new mixed outputs leave zero at cubic degree. In each of the other sixteen types there is at most one \(J\), and each possible singular inner output is regular with the outer generator. Conformal skew gives every ordering. Translating the three inputs \(i,j,k\) times multiplies the Jacobi polynomial by \((-\lambda)^i(-\mu)^j(T+\lambda+\mu)^k\).

Give a generator of transverse degree \(n\) filtration degree \(n+2\), and longitudinal derivatives degree zero. A cubic \(JJ\to EL\) or \(FJ\to LL\) lowers the sum of input degrees by two, and \(JJ\to FL\) or \(EJ\to LL\) lowers it by four. The exchanges of the new closed–negative and negative–negative words have zero contraction. Reordering an old order-two \(JL\) word first sees the next correction to its own bracket at order four. Thus the Jacobi identities hold in the lower-degree relations used to order words. The monic swaps of the nonlinear Poincaré–Birkhoff–Witt construction then give an ordered basis over each nilpotent layer. The associated graded is the symmetric differential algebra. The full vertex products give the relative chiral operations in the affine coordinate. [De Sole and Kac, §5, proof of Theorem 3.9 over the complex numbers](https://arxiv.org/pdf/math-ph/0312042v3#page=23)
:::

At order \(s^4\), compose the brackets with all intermediate jets present. Then retain the words in which every output field carries the constant transverse polynomial \(1\). Write \(L_a=L_a[1]\) on these outputs. Insert \(J_h[1],J_e[x^2],J_f[y^2]\) in that order and read the coefficient of \(\lambda^1\mu^0:L_h[1]^2:\) in the Jacobiator. The tree action \([J_h[1]{}_\lambda F[1]]=-s\lambda L_h[1]\) multiplies the corrected \(FL\) coefficient \(-4s\nu/3\). The open one-loop contraction on the one-loop \(JL\) word gives four ordered terms \(-1/3,5/3,5/3,-1/3\) in units of \(\nu^2\lambda\). Thus the fixed lower brackets give
\[
 \left(\frac43s^2\nu+\frac83\nu^2\right)\lambda=-\frac18s^4\lambda .
\]
Holding the other brackets fixed, the printed \(i\) gives \(-3s^4\lambda/8\) in the same calculation. The shift to the marked cubic value is \(+s^4\lambda/4\). The change of positive current that restores the printed value of the cubic \(FL\) coefficient \(i\) also transports the companion brackets. It adds \(2s\nu:F[1]L_h:/3\) to \(J_h[x^2y^2]\). The tree action of \(J_h[1]\) therefore adds \(-2s^2\nu\lambda:L_h^2:/3=+s^4\lambda:L_h^2:/4\) to their quartic bracket.

For \(J_e[x^2](z)J_f[y^2](0)\), let \(B_{hh},B_{ef}\) be the total double-pole coefficients on \(:L_h^2:\) and \(:L_eL_f:\), in units of \(\nu^2=9s^4/64\). On these two quadratics the ordered two-loop scalar is \(-1/6\). Let \(A\) be the three-field simple pole in units of \(\nu^2\), summed over the three placements of the positive current in right-associated \(J_i(L_jL_k)\) order. Its Wick contraction with \(J_h[1]\) contributes \(W(A)=8/3\) to the Cartan row in units of \(\nu^2\lambda\). The other contours give \(-2B_{hh}\), so \(W(A)-2B_{hh}=8/9\) fixes \(B_{hh}=8/9\). Now insert \(J_h[x],J_e[x],J_f[y^2]\). The first tree bracket gives \(2J_e[x^2]\). On \(\lambda:L_eL_f:\) the lower open and closed brackets contribute \(40/9\) and \(16/3\) in the same units, so \(2B_{ef}=40/9+16/3\) gives \(B_{ef}=44/9\). The two-field simple pole has coefficients \(8/9\) on \(:(TL_h)L_h:\), \(44/9\) on \(:(TL_e)L_f:\), and zero on \(:L_e(TL_f):\), in units of \(\nu^2\).

The open colour chain with the corrected cubic \(i\) gives \(B_{ef}=16/9\) by itself, leaving \(28/9\) to reach the total in this marking. A graph with \(m\) loops and \(v_\eta\) axion vertices has order \(s^{2m+v_\eta}\). Two open loops and one loop with two axion vertices can therefore both contribute to the quartic two-field poles. In the latter class the \(d,e\) terms carry \(\widehat\lambda_g^2\hbar^2=s^2\hbar\), since \(s=\widehat\lambda_g\sqrt{\hbar}\). The derivative terms admit different assignments between the two classes with the same total. Identifying the individual graph contributions and matching the marked currents to microscopic defect fields remain open. [Fernández and Paquette, graph grading (2.19)–(2.21)](https://arxiv.org/pdf/2412.17168v2#page=19) · [Two-field coefficients, Appendix B.6.2](https://arxiv.org/pdf/2412.17168v2#page=62)

For arbitrary polynomial labels \(p,q\) the projected quartic binary brackets have transverse factor \(B_2(p,q)(0)/4\), the second transvectant at the origin. In a Jacobi identity only total input bidegree \((2,2)\) can reach this output. Distributing the two powers of each variable among the three inputs gives \(36\) monomial triples, including the positive spectators. The \(JJJ\) and \(LJJ\) terms cancel on each, with both contour variables and the translations of each output retained. The other generator triples vanish at this order by the parity of the closed–positive brackets and regularity among \(L,E,F\). Sesquilinearity gives all longitudinal descendants. The [degree-one calculation](#ch19-quartic-current-outputs) keeps the two transverse labels distinct.

The type \(A_2\) pole \(+s^3/27\) in the preceding calculation retains its own trace and coupling, and its \(EJJ\) identity alone leaves the other cubic equations in that colour algebra to be solved.

### Two transverse outputs of the quartic current product {#ch19-quartic-current-outputs}

Place \(J_e[x^3]\) at \(z\) and \(J_f[y^2]\) at the origin of the celestial line. In the coefficient of \(s^4\), select two outgoing negative-helicity currents with colours \(e,f\). Their total transverse Taylor degree is one. The \(x\) label may sit on the \(e\) field or the \(f\) field. Keep the pair \(L_e[x]L_f[1]\). What is the simple-pole coefficient when the curve derivative acts on \(L_e[x]\), and what is it when the derivative acts on \(L_f[1]\)? Here \(T\) differentiates along the celestial line. It acts even on a field whose transverse polynomial is the constant \(1\). Lowering \(x\) to \(1\) will compare this product with the one on \(J_e[x^2],J_f[y^2]\), where the derivative on \(L_f\) had coefficient zero.

The [four-current algebra](#ch19-marked-sl2-cubic-pbw) of pure axion-coupled self-dual Yang–Mills theory fixes the input to this calculation. In its formal vacuum the gauge currents \(J,L=\widetilde J\) and the axion currents \(E,F\) have specified brackets through order \(s^3\). We seek their next coefficient after projecting to the indicated output fields. Use \(K(a,b)=\operatorname{tr}_2(ab)\), \([h,e]=2e,\ [h,f]=-2f,\ [e,f]=h\), and \(\ell=s,\ \nu=-3s^2/8\). We give the numerical coefficients of order \(s^4\) in units of \(\nu^2=9s^4/64\). A term \(\mu B+C\) in the bracket gives \(B/z^2+C/z\) in this order of the fields. Products are normally ordered. Use the linear transverse \(\mathrm{SL}_2\) action, the prescribed cubic brackets and the ordered three-field residues \(J(LL)\) and \(LLL\), with the positive-helicity letter first in the right-associated product.

First consider the output of transverse degree zero. Write \(L_a=L_a[1]\) and \(S=\tfrac12L_h^2+2L_eL_f\). On the quadratic inputs \(x^2,y^2\) the two-field coefficients for any colours \(a,b\) have the form
\[
\begin{aligned}
 B(a,b)&=uK(a,b)S+vL_aL_b,\\
 C(a,b)&=\tfrac12 TB(a,b)\\
       &\quad+w\big((TL_a)L_b-(TL_b)L_a\big).
\end{aligned}
\]
Indeed the symmetric square of the adjoint representation has a scalar and a five-dimensional summand. They give the two maps in \(B\). Reversing the incoming contours fixes the symmetric part of \(C\), and the alternating square supplies one adjoint. The [Cartan and root contractions](#ch19-marked-sl2-cubic-closure) give \(u=16/9\) and \(4u+2v=88/9\). In the first equation the ordered \(J(LL)\) simple pole contributes \(8/3\) when the outer \(J_h[1]\) contracts with it. On the constant Cartan spectator the \(\lambda L_eL_f\) contributions from the open one-loop products and the three-field residue cancel. The remaining equation is \(4w=4u+2v\). Thus \(v=4/3,\ w=22/9\). The double pole on \(e,f\) is \((8L_h^2+44L_eL_f)/9\), and the simple pole differentiates the \(e\) leg of the root pair with coefficient \(44/9\). Keeping just the open colour chain with its corrected cubic input would give \(16/9\) on \(L_eL_f\). The positive spectator \(J_h[x]\) forces the missing term, \(28/9\) times \(\mu L_aL_b+(TL_a)L_b\) on these transverse inputs. The total is the constant-output formula of Raeez Lorgat, *Calabi–Yau Quantum Groups*, §14.10, p. 299, equation 14.63.

For general polynomial inputs \(p,q\), take their second transvectant
\[
\begin{aligned}
 H(p,q)={}&p_{xx}q_{yy}-2p_{xy}q_{xy}\\
           &+p_{yy}q_{xx}.
\end{aligned}
\] The constant output multiplies these maps by \(H(p,q)(0)/4\). Indeed a transverse singlet in input degree four occurs only in \(S^2\otimes S^2\), with multiplicity one, where \(S^j\) denotes the degree-\(j\) binary forms. Only the value of the completed bracket is projected. For example the intermediate bracket of \(J_e[x]\) and \(J_f[y]\) contains the constant axion field \(-sF[1]\). Removing the positive jets at the outset would lose this term.

Now let \(p,q\) be homogeneous of degrees three and two and put \(\xi=H(p,q)/12\). Thus \(\xi=x\) on the opening pair. Let \(Q_\xi(i\otimes j)=L_i[\xi]L_j[1]\) for two colours \(i,j\). Write \(d_+\) and \(d_0\) for \(T\) on its first and second fields, respectively. In the colour tensor product take the ordered basis of equivariant maps
\[
\begin{gathered}
 O=K(a,b)\Omega,\\
 P=a\otimes b,\qquad R=b\otimes a ,
\end{gathered}
\]
where \(\Omega=\tfrac12h\otimes h+e\otimes f+f\otimes e\). A triple of numbers denotes its linear combination of \(O,P,R\). The tensor square of the adjoint splits with multiplicity one into summands of dimensions \(1,3,5\).

::: {.theorem #ch19-quartic-labelled-poles title="quartic poles at transverse degree one"}
Keep the marking above and take the degree-three and degree-two inputs \(p,q\) in that order. Project the quartic \(JJ\) bracket onto two negative fields of total transverse degree one. The result is
\[
\begin{aligned}
 &\mu Q_\xi(B)+d_+Q_\xi(C_+)\\
 &\qquad+d_0Q_\xi(C_0),
\end{aligned}
\]
in units of \(\nu^2\), with
\[
\begin{aligned}
 B&=(16/3,\,4,\,0),\\
 C_+&=(8/3,\,6,\,-2),\\
 C_0&=(8/3,\,-10/3,\,10/3).
\end{aligned}
\]
Reversing the two incoming fields uses the identity \([A_\mu B]=-[B_{-\mu-T}A]\). The double pole has the same tensor with the arguments exchanged. Since \(T\) differentiates both output fields, this reversal contributes one copy of the double-pole tensor to each derivative coefficient. The two simple-pole tensors in the reversed order are therefore \(B-C_+\) and \(B-C_0\), with the arguments exchanged. The projected Jacobi identities hold for all polynomial inputs and all their longitudinal descendants.
:::

::: {.proof #ch19-quartic-labelled-poles-proof}
Insert \(J_h[y],J_f[y],J_e[x^3]\), with frequencies \(\lambda,\mu\) for the first two currents. Their first tree bracket is \(-2J_f[y^2]\). In the allowed quartic \(JJ\) channels, input degree \(n<4\) would give negative output degree. For \(n\ge4\), a linear input gives smallest transverse highest weight \(n-2\) in \(S^1\otimes S^{n-1}\). Every output has highest weight at most \(n-4\). Such a pair therefore has zero quartic bracket. Only the middle term of Jacobi contains the unknown two-field coefficient. Its minus sign and \([h,f]=-2f\) give \(+2\) times the reversed bracket. Moving that contour past the third insertion replaces the frequency by \(-\lambda-\mu-T\), with \(T=d_++d_0\) on the two fields. The unknown term on any fixed output word is therefore
\[
\begin{aligned}
 &2(\lambda+\mu)B+2d_+(B-C_+)\\
 &\qquad+2d_0(B-C_0),
\end{aligned}
\]
where each tensor now denotes its coefficient on that word.

For \(L_e[x]L_f[1]\), the known terms have coefficients \(-56/3,-56/3,-4/3,-20\) on \(\lambda,\mu,d_+,d_0\), in that order. They include both orders of axion exchange through the cubic \(EJ,FJ\) and \(JJ\) operations. For example the gauge and axion contributions to the last two entries are \(20/3-8=-4/3\) and \(-100/3+40/3=-20\). The [ordered mixed-current recurrence](#ch14-celestial-yangian-like) fixes the three-field term. Let \(b_i\) be one plus the transverse degree in slot \(i\). On these axes its [ordered integral](#ch14-celestial-ordered-transport) has weight
\[
 -\frac{b_1}{b_1+b_2+b_3}\frac{b_2}{b_2+b_3}.
\]
Putting \(x\) in slot one, two or three therefore gives \(-1/4,-1/6,-1/12\). For \(J(LL)\) each of the three letters in turn carries positive helicity. For \(LLL\) all three letters retain negative helicity. [Fernández and Paquette, §§3.4–3.5](https://arxiv.org/pdf/2412.17168v2#page=42)

On this root word the frequency gives \(2B=56/3\). The derivative equations give \(2(B-C_+)=4/3\) and \(2(B-C_0)=20\). The coefficient of \((TL_e[x])L_f[1]\) in the simple pole is \(26\nu^2/3\). On \(L_e[x](TL_f[1])\) it is \(-2\nu^2/3\). The same contractions on the Cartan and the reversed root word give the three rows below. In each word the left field carries \(x\).
\[
\begin{array}{c|rrr}
 (i,j)&B&C_+&C_0\\ \hline
 (h,h)&8/3&4/3&4/3\\
 (e,f)&28/3&26/3&-2/3\\
 (f,e)&16/3&2/3&6
\end{array}
\]
The first row reads half the coefficient of \(O\). Subtracting the full coefficient of \(O\) from each root row reads the coefficients of \(P\) and \(R\). This gives the three tensors of the theorem.

For the all-polynomial assertion, a linear output in total input degree five occurs only in \(S^3\otimes S^2\) and its reverse, once in each. The full three-input identity has total transverse exponent \((3,2)\) or \((2,3)\). Distributing these exponents over three ordered fields gives \(120\) monomial triples. To evaluate each contour, apply the outer bracket to the two letters of an inner normal product and add its Wick integral \(\int_0^\lambda [[A_\lambda B]_\eta C]\,d\eta\) for inner word \(:BC:\). Reassociating \((J_iL_j)L_k\) to \(J_i(L_jL_k)\) also contributes \((TL_j)L_{[i,k]}\) at tree level, with the incident labels multiplied on the bracketed letters. On the \(27\) colour triples this gives \(3{,}240\) three-current identities. Their two-field system has rank nine and the coefficients above satisfy every row. The three-field terms cancel. Computing in the original nested order or cyclically with the third frequency \(-\lambda-\mu-T\) gives the same polynomials in \(\lambda,\mu,d_+,d_0\).

Both closed brackets are essential here. On \(J_e[x],J_f[x^2],J_h[y^2]\), the inner \(E[x^3]\) meets the last current. Omitting its cubic \(EJ\) action leaves \(16(2\lambda-\mu)\nu^2/9\) on \(L_e[x]L_f[1]\). The factor \(2\lambda-\mu\) comes from moving \(T+3\lambda\) across the contour of frequency \(\lambda+\mu\). With one \(L\) the three possible placements give \(9{,}720\) identities with the prescribed \(LLL\) term. With a closed spectator the parities of the mixed brackets eliminate the quartic term. Pairs among \(L,E,F\) are regular. Multilinearity and sesquilinearity then give the assertion for arbitrary jets and their curve translates.
:::

The lowering operation \(\partial_x\) on the answer agrees with replacing \(x^3\) by \(3x^2\). It identifies the two Cartan words \((TL_h[x])L_h[1]\) and \(L_h[x](TL_h[1])\). The open-chain derivative formula with the corrected cubic inputs leaves opposite Ward residuals \(+8\nu^2/3,-8\nu^2/3\) on those words. They cancel after lowering. Even adding the colour tensors \(a\otimes b,b\otimes a\) from the two-axion class cannot remove this discrepancy on \(a=e,b=f\), since neither has a Cartan component. Thus the labelled Ward identity determines a part of the simple pole invisible in the constant-output comparison. Both two open loops and one loop with two axion vertices can contribute at order \(s^4\). Identifying the individual diagrams or their microscopic currents requires further input. [Fernández and Paquette, Appendix B.6](https://arxiv.org/pdf/2412.17168v2#page=62)

The same linear spectator gives a recursion in every transverse degree. Let \(\Theta_{ab}(p,q;\eta)\) denote any solution for the two-field quartic bracket in this marking. In Jacobi insert a linear polynomial \(t=x\) or \(y\) on the spectator of colour \(a\) and set its frequency to zero. Write \(G\) for the two-field Jacobi contribution formed from the fixed lower brackets and three-field residue on \(a[t],b[p],c[q]\). Let \(\rho_{a[t]}\) act by the tree bracket on each negative letter, multiplying its label by \(t\). Then
\[
\begin{aligned}
 &\Theta_{[a,b],c}(tp,q;\eta)\\
 &\quad=G+\rho_{a[t]}\Theta_{bc}(p,q;\eta)\\
 &\qquad-\Theta_{b,[a,c]}(p,tq;\eta).
\end{aligned}
\]
In the two occurrences of \(\Theta\) on the right, the first polynomial is \(p\). On the left it is \(tp\). A constant or linear first input gives zero by the transverse weight bound. Every nonconstant monomial splits off a coordinate and every colour is a sum of brackets in \(\mathfrak{sl}_2\), so induction determines at most one solution. Existence requires independence of the chosen decompositions and the full Ward equations in both contour variables. At transverse output degree two the resulting candidate satisfies all \(7{,}560\) three-positive-current identities in the original contour order.

To put the second transverse endpoint at the origin, translate both endpoints \(U,V\) by the same vector \(-V\). The new pair is \((U-V,0)\), with its separation unchanged. This translation acts on the fields in the Ward recursion. A constant vector \(D=v_x\partial_x+v_y\partial_y\) differentiates the polynomial labels on \(J\) and \(L\). The axion modes are closed two-forms. For a homogeneous polynomial \(p\) of degree \(n\), put \(\beta_p=p(x\,dy-y\,dx)/(n+2)\) and write \(d_\perp\) for the transverse differential. The \(k\)th mode of \(F[p]\) is represented by \(d(z^k\beta_p)\), and that of \(E[p]\) by \(z^k dz\wedge d_\perp(p/n)\) for \(n>0\). [Costello and Paquette, §4.3, equation 4.3.1](https://arxiv.org/pdf/2201.02595v3#page=29)

Put \(\theta=v_x y-v_y x\). The difference \(D\beta_p-\beta_{Dp}\) has transverse primitive \(p\theta/((n+1)(n+2))\). Differentiating \(z^k\) gives \(kz^{k-1}dz\). With the mode convention \((TE)_{(k)}=-kE_{(k-1)}\), the two currents therefore transform as
\[
\begin{aligned}
 D F[p]&=F[Dp]-\frac{T E[p\theta]}{n+2},\\
 D E[p]&=\frac{n-1}{n}\,E[Dp]\quad(n>1).
\end{aligned}
\]
For linear \(p\), \(Dp\) is constant and \(d_\perp(Dp)=0\), so \(D E[p]=0\). Here \(1\) is the constant transverse polynomial, so \(E[1]=0\). The first formula gives \(\partial_x F[1]=-\tfrac12 T E[y]\).

In the [tree bracket](#ch19-four-currents) of \(J_e[x^2]\) with \(J_f[y^2]\), the axion part is \(-s\) times \(F[4xy]+(2T+4\lambda)E[x^2y^2]\). Under \(\partial_x\) the first term becomes \(F[4y]-TE[xy^2]\), and the second gives \((3T+6\lambda)E[xy^2]\). Their sum is \(F[4y]+(2T+6\lambda)E[xy^2]\), exactly the axion coefficient for the differentiated input \(J_e[2x]\) against \(J_f[y^2]\).

For the fixed cubic brackets the variation under \(D\) satisfies the homogeneous Ward equations. The transverse weight bounds eliminate its possible unary terms in \(JJ,FJ\) and its constant and linear seeds in \(EJ\). The ordered three-field residues commute with the same translation.

If \(U\ne V\), a determinant-one linear change of transverse coordinates now sends \(U-V\) to \((1,0)\) and fixes the origin. What remains to compare in this frame? Keep two components, the ordered double pole and the simple pole with the derivative on the first output. The opposite-root recursion gives a coefficient \(W(p,q)\) of the invariant colour tensor \(K(a,b)\Omega\) on transverse inputs \(p,q\). It is twice the coefficient on \(L_hL_h\) for colours \(e,f\), since the \(h\otimes h\) entry of \(\Omega\) is \(1/2\). There is a second way to read it. Take the \(L_eL_f\) output of the spectator equation on \(J_h[x],J_h[p],J_h[q]\). Let \(G_x^{ef}(p,q)\) be the contribution from the fixed lower brackets and the ordered three-field residue. The equation gives \(4W_{\rm C}(p,q)=-G_x^{ef}(p,q)\), since \(x(U)-x(V)=1\). The two determinations must agree.

Put \(Z=W-W_{\rm C}\). Its transverse degree shift is \((-2,-2)\). Both endpoints now have \(y=0\), so only inputs with a total of two \(y\)'s can contribute. Write \(H_{ij}=Z(x^i,x^j y^2)\) and \(S_{ij}=Z(x^iy,x^jy)\). The shear \((x,y)\mapsto(x+u y,y)\) fixes both endpoints. Apply it to \((x^{i+1},x^j y)\) and take the coefficient of \(u\). This gives \((i+1)S_{ij}=-jH_{i+1,j-1}\), with zero on the right for \(j=0\).

In moving the two Cartan spectators one uses their tree actions on the quartic coefficient \((s^4)/(s^5)\). On a charged negative current the two quantum zero modes already have a nonzero commutator. In the stated order, the mixed brackets give
\[
 [J_h[x]_{(0)},J_h[y]_{(0)}]\,L_e[1]
      =-4\nu:L_h[1]L_e[1]:\pmod {s^3}.
\]
The sign reverses on the opposite root, with \(L_f[1]\) in place of \(L_e[1]\). Here \(\nu=-3s^2/8\), so this correction vanishes when applied to the quartic coefficient.

Moving a linear spectator label \(y\) between the two inputs gives the remaining Ward equation \(4(S_{ij}-H_{ij})=0\). If it holds, the shear identity first gives \(H_{i0}=0\), then \(H_{ij}=0\) by induction on \(j\). It also gives \(S_{ij}=0\). Reversing the input contours supplies the case with both \(y\)'s on the first input. This reduces the calculation to one spectator equation on \(x^i,x^j y\) in both curve components. At \(i=j=1\) the open contraction gives \((16/3,32/9)\) in these two components. The two orders of axion exchange give \((0,-16/9)\) and \((-16/3,-16/9)\), so both sums vanish.

For arbitrary \(i,j\ge0\), put \(N=i+j+1\). Denote the mixed coefficient \(\Phi_{k,i+j-1-k}(x^i,x^jy)\) by \(\Phi_k\). For \(0\le k\le i+j-1\), integration on the ordered triangle gives
\[
 \Phi_k=-\frac{k+1}{N}+\frac{\max(k-i+1,0)}{j+1} .
\]
The two intervals on either side of \(k=i-1\) give sums of affine functions of \(k\). The common endpoint contributes once. In the crossed contour replace the frequency by \(-\eta-T\), where \(\eta\) is the frequency on the second input, before selecting the first derivative. In each of the following triples the entries come respectively from two open contractions, tree axion exchange followed by the cubic return, and cubic exchange followed by the tree return. Use the units
\[
 \begin{aligned}
 D&=\frac{16}{3(i+1)(j+1)},\\
 C&=\frac{32}{3(j+1)(j+2)N}
 \end{aligned}
\]
for the double pole and the first derivative. For \(i\ge2,\ j\ge1\) the three double-pole entries are \(i^2+ij+3i+1,\ j-i,\ -(i+1)N\). Their sum vanishes. For the derivative the first two entries are
\[
\begin{aligned}
 A={}&i^2j+2i^2+ij^2+4ij\\
    &+6i-2j^2-4j-2,\\
 B={}&ij-2j-2 .
\end{aligned}
\]
The last entry is \(-(j+2)(i^2+ij+3i-2j-2)\), which cancels \(A+B\). For \(i=1,\ j\ge1\) the double-pole triple in units of \(D\) is \((j+3,j-1,-2(j+1))\). The derivative triple in units of \((j+2)C\) is \((3-j,-1,j-2)\). For \(i\ge2,\ j=0\) the double-pole triple in units of \(D\) is \((i^2+2i-1,1-i,-i(i+1))\). The derivative entries in units of \(C\) are \(2(i-1)(i+3),0,-2(i-1)(i+3)\). At \(i=0\) the first input in either term of the comparison is constant or linear. At \((i,j)=(1,0)\) all three contributions vanish. Thus the two components cancel on the full range, including the boundary exponents. Polynomiality extends the identity from distinct transverse points to their diagonal. The full colour recursion and the three-field contractions appear in Raeez Lorgat's *Chiral Quantum Groups and Holography: Associative chiral algebras, derived centres and gravity*, Theorem 31.18.39, “The quartic vertex algebra”.

Thus the recursion gives the unique quartic two-field operation with these lower brackets and ordered three-field residues. The full brackets satisfy Jacobi on all polynomial jets and their curve derivatives. In the [PBW filtration](#ch19-marked-sl2-cubic-pbw) the three-field and two-field quartic terms lower degree by two and four, respectively. The ordered normal monomials in the four towers and their translates, omitting \(E[1]\), give a free basis of the enveloping vertex algebra over \(\mathbb C[s]/(s^5)\).

## Coefficients at a collision {#ch19-cut-coefficients}

The transverse Taylor labels distinguished the two outgoing fields in the current product. Their insertion points \(z_i\) *along* the celestial line determine when two consecutive groups of fields can be separated. For instance, place three labelled insertions at \((z_1,z_2,z_1)\) with \(z_2\ne z_1\). Both possible cuts put the first and third labels on opposite sides, although their positions coincide. Neither cut separates the fields into independent groups, even though the middle field has met neither neighbour. It is this locus of failed cuts that enters the ordered cobar construction.

**Definition (separating cut).** On \(X^n=\mathbb A^n\) allow coincidences among the labelled positions \(z_1,\ldots,z_n\) in their word order. The cut \(p\), \(1\le p<n\), separates the initial \(p\) fields from the rest on the principal open \(D(F_p)\), where
\[
                F_p=\prod_{i\le p<j}(z_i-z_j)
\]
is invertible. The union of the separating opens is \(U_n\), and \(Z_n=X^n\setminus U_n\). For the chiral Chevalley chains of the four-current algebra over \(R=\mathbb C[s]/(s^3)\), write \(C_n\) for the complex on \(X^n\) over that base. Its factorization map on \(D(F_p)\) identifies the restriction of \(C_n\) with the restricted external tensor product of \(C_p\) and \(C_{n-p}\).

Which part of a coefficient complex is supported on \(Z_n\)? Let \(M\) be a complex of quasi-coherent right differential modules on \(X^n\). Localize \(M\) on intersections of the separating opens. The term in Čech degree \(j\) is
\[
 K_n^j(M)=\bigoplus_{|S|=j}
                  M\left[(\prod_{p\in S}F_p)^{-1}\right] .
\]
Here \(S\) ranges over subsets of the \(n-1\) cuts. The empty subset contributes \(M\). Adding a cut \(a\) localizes the coefficient with sign \((-1)^{|\{s\in S:s<a\}|}\). The two orders of adding two cuts cancel. On degree \(j\), the internal differential of \(M\) has sign \((-1)^j\). The nonempty intersections of principal opens are affine, so their Čech complex computes derived restriction to \(U_n\) followed by pushforward. Augmenting by \(M\) gives the fibre of that restriction map, \(K_n(M)\simeq R\Gamma_{Z_n}(M)\).

A choice of \(j\) cuts gives a cobar word of \(j+1\) blocks. Desuspending each block and using the factorization identifications on the intersection gives the positive-arity reduced cobar coefficient \(K_n(C_n)[-1]\). Its multiplication uses the inverse factorization map on the open separating the two words. [Associative products on configurations](#ch12-associative-products-on-configurations) · [Where successive collisions meet](#ch14-celestial-cut-support)

**Example (three labelled fields).** Put \(u=z_1-z_3,\ v=z_2-z_3\). The cut equations are \(F_1=u(u-v)\) and \(F_2=uv\). They generate \((u^2,uv)\) with radical \((u)\), so \(U_3=D(u)\). The supported complex reduces to \(M\longrightarrow M[u^{-1}]\) in degrees zero and one for a module \(M\) in degree zero. Let \(S=\mathbb C[z_3,u,v]\). For the volume module \(S\,\mathrm{vol}\), the only cohomology is \((S[u^{-1}]/S)\,\mathrm{vol}\) in degree one, containing the simple pole \(\mathrm{vol}/u\). A module supported on \(u=0\) instead has zero localization and survives in degree zero. The Koszul cochain complex of the two equations on \(S\) would give \(S/(u^2,uv)\) in degree two. The locus of failed cuts and the coefficient placed on it both enter the calculation.

There is also a scalar topological question about the complex points of \(U_n\). Intersect the diagonal components of \(Z_n\) in all possible ways, ordering these intersections by reverse inclusion with ambient space first. An intersection is specified by the equality partition \(\pi\) of the coordinates and has complex codimension \(c=n-\#\pi\). The proper interval consists of the intersections strictly between the ambient space and that diagonal. Make its strict chains into simplices, with alternating deletion as the boundary and the empty chain in degree \(-1\). If \(\beta_j(\pi)\) is the dimension of its reduced rational homology in degree \(j\), the contribution of this diagonal to \(H^k(U_n;\mathbb Q)\), \(k>0\), has dimension
\[
                   \beta_{2c-k-2}(\pi)
\]
and Hodge weight \(2c\). One way to see the degree is to resolve the closed union by its intersections. Each affine intersection has compactly supported cohomology in a single degree. Grouping chains by their final intersection leaves precisely the reduced chain complex just described. Distinct pure weights prevent higher differentials between those rows. Localization and duality then give the cohomology of the complement. This calculation gives the dimensions of the weight-graded spaces. Cup products need further maps.

At six labels the interval below full collision has augmented chain dimensions \(1,33,97,66\) in degrees \(-1,0,1,2\). The boundaries out of degrees \(0,1,2\) have ranks \(1,32,63\). Its first and second reduced homology groups have dimensions \(97-32-63=2\) and \(66-63=3\). Since \(c=5\), these give two classes in \(H^7\) and three in \(H^6\), all of weight ten. A point count sees the signed difference \(3-2=1\).

Call a label active when its equality block has at least two members. Deleting singleton blocks preserves the interval because no equality pair below \(\pi\) touches a deleted label and the cuts on either side of it impose the same condition. Both endpoints must be active since the first and last gaps have to be crossed. A core with \(r\) active labels therefore occurs \(\binom{n-2}{r-2}\) times at arity \(n\). Each block of size \(\ell\ge2\) uses \(\ell\le2(\ell-1)\) labels, giving \(r\le2c\). The only codimension-one component equates the endpoints. A different minimal collection of equality pairs crossing every gap uses at least two pairs and puts the endpoints in different blocks. Its intersection with the endpoint diagonal therefore has codimension at least three. A chain of proper intersections therefore omits at least one of codimensions one and two. For \(c\ge2\) its simplex dimension is at most \(c-3\). The index \(2c-k-2\) can then contribute for \(k\ge3\) only if \(c\le k-1\).

**Proposition (seventh Betti number of the separating opens).** For \(n\ge2\) put \(B_i=\binom{n-2}{i}\), taken as zero for \(i>n-2\). Then
\[
\begin{aligned}
 b_7(U_n)&=2B_4+28B_5+57B_6\\
          &\quad+28B_7+6B_8 .
\end{aligned}
\]
The weight-eight part has dimension \(B_6\) and the weight-twelve part dimension \(4B_5+5B_6\). The remaining classes have weight ten.

**Proof.** In degree seven the interval index is \(2c-9\), at least \(-1\) and at most \(c-3\). This leaves \(c=4,5,6\) and at most twelve active labels. Of the 1,633 intersection intervals in this window, 102 have nonzero rational homology in the required degree. The ranks, summed over cores with the indicated number of active labels, are

| Codimension \(c\) | Interval degree | 6 labels | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- |
| \(4\) | \(-1\) | 0 | 0 | 1 | 0 | 0 |
| \(5\) | \(1\) | 2 | 24 | 51 | 28 | 6 |
| \(6\) | \(3\) | 0 | 4 | 5 | 0 | 0 |

The other core sizes contribute zero. Each entry is obtained from the kernel of alternating deletion modulo the boundary from the next chain group, as in the six-label calculation. Multiplying the column for \(r\) labels by \(B_{r-2}\) and summing gives the displayed polynomial. Reading each row in its weight \(2c\) gives the weight decomposition. ∎

These are rational cohomology groups of the open set of positions. To multiply quantum fields one still needs \(C_n\) and its factorization maps on those opens.

A second use of localization occurs on the *transverse* punctured plane, where the line has been removed. Put \(S=k[x,y]\). The ordered two-chart Čech algebra of \(D(x),D(y)\) is \(S_x\oplus S_y\longrightarrow S_{xy}\), with \(d(A,B)=B-A\). Degree zero multiplies componentwise. On an overlap element \(v\) the left action is \((A,B)v=Av\), the right action \(v(A,B)=vB\). For \(\eta=[1/(xy)]\) in degree one, \(x\eta\) and \(\eta y\) are exact, with primitives \(P=(0,1/y)\) and \(Q=(-1/x,0)\). Thus \(Py-xQ=(1,1)\), a triple Massey value of \(1\) modulo the indeterminacy \((x,y)\). A unital character evaluating \(x,y\) at zero would have to send this unit to zero. This obstructs evaluation on an occupied line at the missing point. The empty configuration still has its own augmentation. [Products with chosen primitives](#ch05-relations-can-leave-a-higher-operation)

The same charts give higher products at arbitrarily large arity in a specified minimal model. In degree zero project a chart pair to the polynomial part of its second component. In degree one keep the Laurent monomials with both exponents negative. For a monomial with nonnegative \(y\) exponent take its primitive in the first chart with a minus sign. When the \(y\) exponent is negative and the \(x\) exponent nonnegative, place the primitive in the second chart. Let \(\sigma\) lower degree by one and write \(b_n\) for the suspended products, with \(b_2(\sigma a,\sigma b)=(-1)^{|a|}\sigma(ab)\).

For \(q\ge1\), take the word with endpoints \(x^qy^{q-1},y\) and \(q\) copies of \(\eta\) between them. On the suspended word \(b_{q+2}\) gives \((-1)^{q-1}\sigma1\). On the surviving branch the first \(q-1\) Laurent factors stay in the first chart. The last moves into the second, and multiplication by \(y\) gives the constant. In this transfer, retaining the products only through arity \(N\ge3\) leaves an uncancelled unit in the length-\(N+2\) identity. For instance the deciding word has letters \(x,(xy)^{N-2}\), followed by \(N-1\) copies of \(\eta\) and the final \(y\). The two-chart differential algebra itself encodes all these homotopies with its differential and binary product. The arities of the transferred formulas refer to the chosen contraction.

## Reconstructing an interacting comparison {#ch19-interacting-comparison}

The two-chart example needs higher products of unbounded arity on cohomology. Arity counts insertions. In deforming a bulk-to-boundary map we must also count powers of the bulk coupling in each operation. For instance, in the family \(W_s=x^3+s x^4\) the marked boundary with parameter \(t\) has scalar obstruction \(t^3-st^4\). Its \(t^4\) coefficient uses four boundary inputs and is first order in \(s\). The change \(t\mapsto t(1-st)^{1/3}\) removes it as an unmarked operation. A specified interface must also preserve the markings and products it compares. Let \(s\) be a formal coupling over a field \(k\) of characteristic zero. Encode the associative operations by a degree-one coderivation \(b(s)\) on the tensor coalgebra of the suspended operator space, including the unit among possible outputs. Write \(b(s)=b^{(0)}+s b^{(1)}+s^2 b^{(2)}+\cdots\), with the superscripts indexing powers of \(s\). The coefficient of \(s^2\) in \(b(s)^2=0\) reads
\[
 [b^{(0)},b^{(2)}]=-(b^{(1)})^2 .
\]
Thus the square of the first variation has to be a boundary for the differential \([b^{(0)},-]\). If the unit is split off before forming reduced words, its scalar outputs must be retained as curvature. [Associativity as a coderivation equation](#ch05-one-differential-encodes-all-associativity-homotopies)

For an obstruction in the multiplication itself, let \(1,x,y,z\) span an algebra with square-zero ideal \((x,y,z)\). Change the products to first order by \(x*x=s y,\ y*x=s z\), setting the other radical products to zero. Every first-order associativity equation on three radical inputs vanishes since the first variation lands in the radical. But \((x*x)*x-x*(x*x)=s^2z\). Any second-order correction \(\nu\) contributes its Hochschild differential, whose value at \((x,x,x)\) is \(x\nu(x,x)-\nu(x,x)x=0\). The coefficient of \(z\) obstructs a lift of this first-order multiplication.

**Example (obstruction to lifting a marked map).** Even if two products \(\mu_{B,s},\mu_{A,s}\) are separately associative, a map \(f_s:B_s\to A_s\) must satisfy \(f_s\mu_{B,s}=\mu_{A,s}(f_s\otimes f_s)\). Fix the flat endpoints \(B_s=k[[s]][u]/(u^2)\), \(A_s=k[[s]][v]/(v^2-s^2)\), with \(u\) identified with \(v\) at \(s=0\). They agree modulo \(s^2\). To lift the marked identity, write \(f_s(u)=v+s(a+bv)+s^2w\) modulo \(s^3\). At order \(s\) its square has coefficient \(2av\), so \(a=0\). At order \(s^2\), \(v^2=s^2\) supplies the unit, whereas \(vw+wv\) in the special fibre belongs to \((v)\). Thus \(f_s(u)^2\) cannot vanish modulo \(s^3\). The two algebras exist to all orders and the marked map lifts through first order only.

For a physical interface the comparison must also carry units, restrictions to regions and operations at collisions. Once such a comparison has been constructed at compatible finite orders, there is a criterion for its formal limit. [Lifting through a square-zero ideal](#ch05-relative-lifting) · [Products through an interface](#products-through-an-interface)

**Lemma (derived-complete comparison).** Let \(C\) be the cone of a marked comparison over \(R=k[[s]]\). Assume that \(C\) is derived \(s\)-complete. At each order \(N\), require that the cone of the compatible comparison at that order is the derived reduction \(C_N=C\otimes_R^{\mathbf L}R/(s^N)\). If the comparison on the special fibre is a quasi-isomorphism, the formal comparison is a quasi-isomorphism as well.

**Proof.** The hypothesis on the special fibre says \(C_1\simeq0\). The kernel of \(R/(s^N)\to R/(s^{N-1})\) is a copy of \(k\) generated by \(s^{N-1}\). Tensoring the resulting exact triangle with \(C\) shows inductively that \(C_N\simeq0\) for every \(N\). Derived completeness identifies \(C\) with their derived inverse limit. ∎

When the target is a centre, one must identify what its derived reduction computes. For an ordinary unital differential graded algebra \(A\) over \(R\), put \(A^e_R=A\otimes_R^{\mathbf L}A^{\mathrm{op}}\). The relative derived centre is the complex of endomorphisms of the diagonal bimodule, \(Z_R(A)=\mathbf R\operatorname{Hom}_{A^e_R}(A,A)\). Let \(S\) be a commutative \(R\)-algebra perfect as an \(R\)-module. For these coefficients there is an equivalence
\[
 Z_R(A)\otimes_R^{\mathbf L}S
       \simeq Z_S(A\otimes_R^{\mathbf L}S).
\]
Indeed tensoring the cochains by \(S\) and tensoring their target by \(S\) agree for \(S=R\). Both constructions preserve finite cones and retracts in the coefficient complex, and these generate the perfect complexes from \(R\). Extension of scalars then identifies the extended diagonal and its enveloping algebra. In particular \(R/(s^N)\) has a two-term free resolution, so the comparison applies to every finite order.

The ordinary centre can still jump. On the free \(R\)-module with basis \(1,x,y,z\) define \(xy=sz\) as its only nonzero product of two radical generators. Commuting with \(x\) and \(y\) forces their two coefficients in a central element to vanish. The centre is \(R1\oplus Rz\), while all four basis elements become central at \(s=0\). To see why the class of \(x\) fails to lift centrally, compute \([x,y]=sz\). Dividing \([x,-]\) by \(s\) and reducing on the special fibre gives a derivation sending \(y\) to \(z\). Changing the lift to \(x+sa\) adds the inner derivation \([a,-]\) on the special fibre. That fibre is commutative, so the nonzero value on \(y\) survives every such change. For continuous chiral cochains one must identify the coefficient functors, the completed diagonal and the collision supports under scalar change. The \(E_7\) family already illustrates the need to specify that support. Inverting \(s\) retains seven dimensions in the critical algebra, while completing at one generic point selects four. [The changing critical scheme](#ch19-diagonal-and-trace)

On the boundary constructed from \(W=ax^3\) with \(a\ne0\), the scalar \(a\) occurs in the marked triple product. The identity defect recovers the bulk field \(x\). With volume \(dx\), this field has sphere value \(1/(3a)\) and zero mixed disk amplitude with \(\psi\), since the disk with insertions \(h,\psi\) gives \(-h(0)\). The radius-one gauge sphere fixes its own vacuum value \(1/16\) by localisation. On the celestial line the four-current calculation gives collision operators through \(s^2\), and the axis quotient has an all-order current action on a common background. With the specified cubic operations, the marked pure \(\mathfrak{sl}_2\) algebra has an ordered basis through \(s^3\). At order \(s^4\) its [Ward identities at constant transverse output](#ch19-marked-sl2-cubic-closure) and [at transverse degree one](#ch19-quartic-labelled-poles) hold for all polynomial inputs and longitudinal descendants. In this marking the quartic identities hold at every transverse degree and the ordered basis extends through \(s^4\). The microscopic identification of these currents and the individual graph amplitudes remain open. Does the marked current algebra extend to higher orders in \(s\)? What coproduct, if any, governs two independently prepared physical lines? A physical reconstruction of an interacting bulk must specify which independently prepared boundary state measures each bulk insertion. Its interface must transport their ordered products on the same supports, and gluing the resulting states must reproduce the bulk amplitude with its normalisation. The calculation on independent celestial lines gives a nonzero cross commutator when the two backgrounds are added. Any proposed fusion must account for it. [Independent realisations of reconstruction](#independent-realizations)
