# Nine BRST readings determine the original affine characteristic cocycle

At \(\tau=3/2\) the \(31\times41\) affine system of [the determinant construction](MARKED-AFFINE.md) has rank exactly nine. One can fix nine input and output cells in advance. The two diagonal minors have determinant \(+1\). Thus the positive affine cocycle is determined by **nine evaluations of native commutator homotopies**, with no search for a nonzero native minor. The values of these nine remaining scalars are specified by the operator formulas; they have not been expanded numerically here.

Use the marked positive cohomology basis \(1,a,b,ab,c,ac,u,au,v,av,z,az\). These are coordinates on the actual cohomology \(H\) in the projection and inclusion of the previous construction. A different PBW complement used to choose cycle representatives simply computes \(I(x)\) of a given class \(x\) in that complement. A notation such as \(ab\mid z\) below is avoided to distinguish a single product class from a two-input word. Write \((x_1,\ldots,x_n)\to y\) for the coefficient of \(s y\) on the suspended input word. All unlisted entries of the small correction \(g\) are set to zero.

1. In \(g_1\) retain \((b)\to c,\ (c)\to v,\ (ac)\to z\), in this order. Let \(r\) be the three native components of \(e_2\) before adding \(g_1\), on \((a,b)\to ac,\ (a,c)\to av,\ (a,c)\to z\). Set the retained column vector to \(-D_1^{-1}r\).
2. With this \(g_1\) already in place and \(g_2=0\), let \(t\) be the native \(e_3\) entries \((a,a,b)\to av,\ (a,a,b)\to z,\ (a,a,u)\to az,\ (a,b,a)\to av,\ (a,b,a)\to z,\ (a,u,a)\to az\). The only retained \(g_2\) entries, in order, are \((a,b)\to v,\ (a,ab)\to z,\ (a,u)\to z,\ (b,a)\to v,\ (ab,a)\to z,\ (u,a)\to z\). Set them to \(-D_2^{-1}t\).
3. Use zero \(g_n\) in arity three and above. Continue the explicit \(F_n=-K_n[b_2,F_{n-1}]\) recurrence from arity four.

Here
\[
 D_1=\operatorname{diag}(-1,-1,1),\quad
 D_2=\begin{pmatrix}
 -1&0&0&0&0&0\\0&1&0&0&0&0\\0&0&-1&0&0&0\\
 1&0&0&-1&0&0\\0&-1&0&0&1&0\\0&0&1&0&0&-1
 \end{pmatrix}.
\]
The coordinates \(r,t\) use the original coefficient operations of (1) in the determinant construction, including the Cartan prescription in arity one. In particular the two nonzero unary values on \(Q,T\) are unchanged.

### Why all the other rows follow

Consider only cochains of arity at least one. Transfer the complete filtered original Hochschild complex from \(\partial_H\) to \(\partial_H+\delta\) using \(\rho,\iota,K\) from the coefficient proof. The tensor contractions have \(K^2=K\iota=\rho K=0\). The small differential is
\[
       D=\rho\,\delta(1+K\delta)^{-1}\iota.
\]
All geometric series are finite in fixed arity. The linear part of the \(31\times41\) system above is precisely the corresponding total-degree-two-to-three matrix of \(D\), omitting zero rows and columns. This follows by placing one small \(g_n\) in (1), setting the constant to zero, and expanding the subsequent \(-K\delta\) corrections. The Cartan normalization of the fixed constant changes only the inhomogeneous term. The part of \(D\) increasing arity by one is the actual suspended binary Hochschild differential on \(H\).

In fact \(D\) and the formal binary Hochschild differential are related by a filtration-preserving linear chain isomorphism on the small cochains. Here is a direct rank justification. Fixed-fibre formality provides a strictly unital, uncurved \(A_\infty\) quasi-isomorphism \(f:(H,b_2^H)\to A\). Consider the complex of coderivations along its bar map. Such a coderivation is specified by a Taylor map \((s\bar H)^{\otimes n}\to sA\) at each arity. Its differential on a degree-\(j\) map \(u\) is \(b_Au-(-1)^j u b_H\). Both maps
\[
 C^{\ge1}(A,A)\longrightarrow C_f^{\ge1}(H,A)
 \longleftarrow C^{\ge1}(H,H),\qquad
    X\longmapsto X f,\quad Y\longmapsto fY
\]
are filtered chain maps. Normalization and the arity lower bound are preserved by strict unitality and the absence of a constant term in \(f\). On the associated graded before taking internal cohomology, the two maps use input precomposition by \(f_1^{\otimes n}\) and output postcomposition by \(f_1\), respectively. The mixed complex contracts in its internal differential by applying the given output contraction of \(A\), since its input \(H\) has zero unary differential. Apply the filtered inclusion from the small source and the filtered projection to the small mixed target. The resulting small comparison maps both have invertible diagonal blocks, because \(f_1\) induces an isomorphism on cohomology. Their remaining terms increase arity. A triangular map of complete length products with invertible diagonal has an inverse by length induction. This proves a linear chain isomorphism and therefore equality of the total differential ranks in every degree. The argument requires only ordinary fixed-fibre formality and the original comparison; no relative or equivariant formality is invoked.

On the formal small side, the relevant direct-sum blocks have sizes \(16\times8,\ 13\times19,\ 2\times14\), with ranks \(3,6,0\). To reproduce the ranks, use \(b_2(sx,sy)=(-1)^{|x|}s(xy)\), with exterior \(a\) and square-zero \(b,c,u,v,z\). For an even suspended correction \(g_n\), add both outer insertions of \(g_n\); subtract each internal \(b_2\) insertion with prefix sign \((-1)^{\sum_{j<i}(|x_j|-1)}\). The resulting rational matrices give precisely the row and column tuples and minors displayed above. [Exact signed integer matrices and pivots](AFFINE-PIVOTS.json) · [Standalone pivot enumeration](affine_pivots.py)

Thus the *native* total matrix also has rank \(3+6=9\). Its indicated rows and columns form a lower block-triangular minor with diagonal \(D_1,D_2\). The upper off-diagonal block is zero by arity, so this minor is invertible and these nine columns span the entire image. The inhomogeneous system is consistent by the characteristic lift and coboundary argument of the determinant construction. Killing its indicated nine rows therefore kills every row, including both arity-four constraints. This proves the prescription above.
