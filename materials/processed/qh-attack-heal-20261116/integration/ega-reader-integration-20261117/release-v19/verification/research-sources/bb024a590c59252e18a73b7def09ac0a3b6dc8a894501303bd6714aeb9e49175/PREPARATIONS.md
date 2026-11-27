# Which prepared K3 states distinguish weighted cubic changes?

These are three further results from the independent review of BP-K3-SEW and BP-K3-PROBES. The parameter \(t\) remains formal in a characteristic-zero field \(K\). The rank-one experiment compares one fixed reference product to \(\star_0+\lambda t\nu_u\), with \(\lambda\ne0\) and \(u\ne0\) null in the nondegenerate space \(E=\langle C,F\rangle^\perp\). A preparation here means a marked algebraic state. Physical accessibility of its lift, the ambient cap and the oriented trinion require independent constructions. [Reviewed handle law and scope](CHECK.md)

## K3P-S. Restricted preparation spaces

Suppose the permitted projections of the preparations form a linear subspace \(S\subset E\), and every element of \(S\) is accessible. A set of fixed diagonal scalar trinions can detect every rank-one change if and only if \(S^\perp\) contains no nonzero \(K\)-null vector. When this holds, the minimum number is
\[
 d-\max\{\dim D:\ S^\perp\subset D\subset E,\quad D\text{ is anisotropic over }K\},
 \qquad d=\dim E.
\]
Here the zero space is anisotropic. Indeed a set of probes spanning \(W\subset S\) detects precisely when \(D=W^\perp\) is anisotropic. The perfect ambient form makes the assignments \(W\leftrightarrow D\) inverse to one another and \(\dim W=d-\dim D\). This proof allows a degenerate restriction to \(S\). If \(S\) has nonzero radical, its radical lies in \(S^\perp\) and supplies a missed rival.

Over \(\mathbb R\) with indefinite signature \((p,q)\) and \(S=E\), this gives \(\min(p,q)\). If \(S^\perp\) is nonzero positive definite, the answer is \(q\). If it is nonzero negative definite, the answer is \(p\). A definite subspace extends to one of its sign's maximal dimension by orthogonal splitting and Sylvester inertia. Any other nonzero type of \(S^\perp\) contains a missed real null direction.

## K3P-N. Ordinary square-zero preparations

Now require each individual preparation to be a pure middle state \(x\in E\) whose ordinary cup square is zero, equivalently \(q(x,x)=0\). Arbitrary complex or rational states can satisfy this condition. For the actual K3 the sharp counts over \(\mathbb Q,\mathbb R,\mathbb C\) are respectively **three, three and nineteen**. These are counts of fixed diagonal scalar readings against a single, unknown, nonzero weighted rank-one change.

Over \(\mathbb Q\) or \(\mathbb R\), one null preparation misses its own direction. A pair of null preparations with zero mutual pairing likewise misses any nonzero member of their span. A pair with nonzero mutual pairing spans a hyperbolic plane. Its complement retains Witt index one over each of the two fields on this K3, so also contains a missed null vector. For an explicit three-state design use hyperbolic pairs \(e_1,f_1,e_2,f_2\), each with pairing one, and take
\[
 e_1,\qquad f_1,\qquad e_1-f_1+e_2+f_2 .
\]
All three have square zero. They span \(H_1\oplus\langle e_2+f_2\rangle\) of signature \((2,1)\); its real orthogonal complement is negative definite. Thus every real or rational rival is detected. For a concrete missed rival of the two-state design \(e_1,f_1\), take \(u=e_2\). The third state pairs with it to one.

More generally, on any real indefinite space with signature \((p,q)\), the square-zero-only minimum is \(\min(p,q)+1\). Let \(W\) be the span of the tested null vectors. If it detects every rival, \(W^\perp\) is anisotropic or zero, hence nondegenerate, so \(W\) is nondegenerate too. As it is nonzero and spanned by nulls it must be indefinite. Its complement being definite or zero forces \(\dim W\ge \min(p,q)+1\). For sufficiency one can choose \(W\) of signature \((p,1)\) if \(p\le q\), or \((1,q)\) if \(q<p\). Such a space is spanned by its null vectors. Indeed over any characteristic-zero field a space containing a hyperbolic pair \(e,f\) has null spanning vectors \(e,f\) and \(x+e-q(x,x)f/2\) for basis vectors \(x\) of its orthogonal complement. This gives a null basis of the required size.

On the complex 20-space, the original lower bound nineteen still applies. For an anisotropic line \(Kz\), the nondegenerate space \(z^\perp\) of dimension nineteen contains a hyperbolic pair and therefore has a null basis by the same construction. One can even choose a rational anisotropic \(z\) in the negative part of the actual K3 marking, preserving both rational hyperbolic planes inside \(z^\perp\). This gives nineteen rational square-zero preparations that detect every complex rival. For a complex nondegenerate space of dimension \(d\ge3\), the same argument gives \(d-1\). In dimension two a null line equals its own orthogonal and two null preparations are required. Definite real forms and a complex line have no nonzero null rivals.

## K3P-U. Weighted rivals on a fixed null plane

Fix a known totally isotropic \(K\)-subspace \(U\subset E\) of dimension \(r\ge1\). Allow finite sums of null rank-one corrections with arbitrary field weights and directions in \(U\). Writing \(l(x)=q(-,x)|_U\in U^*\), their paired cubic changes form the entire space \(\operatorname{Sym}^3 U\), evaluated on \(l(x)\). Indeed the cubes of linear forms span homogeneous cubic polynomials by polarization in characteristic zero. For \(B\in\operatorname{Sym}^3 U\), define \(m_B(x,y)\) by pairing its third slot with \(q\) and extend by zero on \(e,p\). Then \(m_B\) takes values in \(U\) and vanishes if either middle input lies in \(U\) or is \(C\). The product \(\star_B=\star_0+t m_B\) is an associative cyclic polynomial product. The linearized associator cancels on middle states by symmetry of \(B\) and the point-class multiplication. All mixed and double iterations containing a correction with output in \(U\) vanish. The trace and handle corrections from \(B\) vanish because \(U\) is totally isotropic. The common handle annihilates the common discrepancy ideal \(U\oplus Kp\). Thus every connected positive-genus scalar sewing still agrees with the reference.

In genus zero the exact change in an \(n\)-point scalar function, for \(a_i=\lambda_i e+x_i+\mu_i p\), is
\[
 t\sum_{1\le i<j<k\le n}
   \left(\prod_{h\notin\{i,j,k\}}\lambda_h\right)
   B\big(l(x_i),l(x_j),l(x_k)\big).
\]
To see this, expand out the unit parts. On two pure middle inputs the change is \(t m_B\in U\), with zero counit. On three such inputs it is \(tB\,p\). A fourth middle input kills \(p\). In the product grouped from the left the reference product of three middle inputs lies in \(\langle C,p\rangle\), which annihilates \(m_B\) in any subsequent correction. Induction gives zero scalar change on four or more middle inputs. Any pure \(p\)-input in a term also prevents a change. This establishes the formula for all arities and arbitrary field weights.

Consequently exactly \(\binom{r+2}{3}\) predetermined scalar diagonal readings are necessary and sufficient to detect every nonzero \(B\) relative to the fixed reference. Each such reading is a linear functional on this space of cubics. Fewer readings have a common kernel. Since \(K\) is infinite, evaluations on \(U^*\) span the whole dual of \(\operatorname{Sym}^3 U\). Choose a basis of those evaluations. A dual isotropic partner to \(U\) supplies square-zero lifts of all required arguments in \(U^*\), by extending a basis of \(U\) to hyperbolic pairs using the perfect form. With a restricted linear preparation space \(S\) and unrestricted states in it, the same count is attainable exactly when \(S\to U^*\) is onto. Otherwise a nonzero element of \(U\) annihilates \(S\), so its rank-one cube escapes every reading. These counts concern scalar observations. The formula above also makes each fixed higher-arity scalar genus-zero reading linear in \(B\).

For the rational K3 plane \(U=\langle e_1,e_2\rangle\), four explicit square-zero states suffice:
\[
 f_1,\qquad f_2,\qquad f_1+f_2,\qquad f_1-f_2 .
\]
In coordinates \((X,Y)\) on \(U^*\), these evaluate a binary cubic at \((1,0),(0,1),(1,1),(1,-1)\). The first two determine its pure coefficients; the last two independently determine the two remaining mixed coefficients. The weighted cubic \(XY(X-Y)\) vanishes on the first three readings and gives \(-2\) on the last, an explicit failure of a three-reading design. The dimension argument rules out every other three-reading design as well. The unknown-direction single-rival experiment and the arbitrary signed superposition on a known plane have different parameter spaces.
