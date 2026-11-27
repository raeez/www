# The affine three-class in the positive native PBW coordinates

Use \(\tau=3/2\) and the published marked generator
\[
 a=h_{3,0}=e_0-A_3[0,J]\,A_3[I,J]^{-1}E_I.
\]
Its coordinate at zero is one. The input tuple and pivot minor are the actual positive degree-three adapted data. The full two-sided representative below is specified by finite linear algebra on 41 scalars followed by the same original BRST recursion as for \(v_-\) and \(z_+\). In this lower degree the proof of consistency uses the previously proved associative formality of this fibre. The separately defined normalization of an affine Lie algebra three-form need not be chosen to specify the displayed PBW class. [Source marking](</tmp/astra62-programme-rebuild-20261118/constructions/w-bockstein/DOSSIER.md:68>) · [Fixed-fibre formality and its transport](../w4-native-quartic/PROOF.md)

Use the explicit contractions, normalization and notation of [the coefficient calculation](PROOF.md). Write \(H=H^*(A)\), \(\bar H=H/\mathbb C1\), and let the *small* arity-\(n\) cochains have source \((s\bar H)^{\otimes n}\) and target \(sH\). For such a cochain \(g\) use
\[
 \iota_n g=(sIs^{-1})g\,(s\bar\pi s^{-1})^{\otimes n},\qquad
 \rho_n f=(s\pi s^{-1})f\,(s\bar I s^{-1})^{\otimes n}.
\]
Thus \(\iota_n\rho_n=\Pi_n\) of the coefficient calculation. The normalized lift has degree two after suspension. Put \(F_0=sO_a\). Compute \(\widehat F_1\) from (9), (14) of the coefficient calculation. Give the small cochains \(g_1,g_2,g_3\) unspecified scalar entries; below these entries are fixed by one determinant prescription. Use
\[
 F_1=\widehat F_1+\iota_1g_1,\qquad
 R_n=[b_2,F_{n-1}],\qquad F_n=-K_nR_n+\iota_n g_n \quad(n\ge2),           \tag{1}
\]
where \(g_n=0\) for \(n\ge4\). Define \(e_n=\rho_n R_n\). Each \(e_n\) is affine linear in the unknown entries.

The suspended degree of \(g_n\) is two, so on ordinary homogeneous inputs \(q_i\) its output has degree \(\sum q_i+3-n\). For an \(e_n\)-entry the degree is \(\sum q_i+4-n\). The coefficient counts from the eleven positive inputs, with multiplicities, are

| Arity \(n\) | \(g_n\)-cells | \(e_n\)-cells |
|---|---:|---:|
| 1 | 8 | 9 |
| 2 | 19 | 16 |
| 3 | 14 | 13 |
| 4 | 11 | 2 |
| 5 | 5 | 0 |
| 6 | 1 | 0 |

For arity above six both counts vanish by degree. The arity-one obstruction is zero by graded commutativity, and \(g_4,g_5,g_6\) first affect obstructions of arity at least five. Therefore it suffices to solve the single \(31\)-row, \(41\)-column linear system \(e_2=e_3=e_4=0\). The dimensions count *actual individual input words and output labels*, including the two basis vectors in degrees 8 and 12. [Finite dimension replay and marked coordinates](CHECKS.json)

Here is an unambiguous formula for the solution. Order the basis by \(1,a,b,ab,c,ac,u,au,v,av,z,az\), order words and outputs lexicographically within each increasing arity, and flatten \(e=(e_2,e_3,e_4)\) in that order. Let \(u=e(0)\); the \(i\)th column of \(M\) is \(e(\mathbf e_i)-u\). These expressions use only the PBW operators, the finite pivots specified in the coefficient calculation, and signed compositions. Scan the columns of \(M\), retaining the first independent ones, with index tuple \(C\). Scan the rows of \(M[:,C]\) in the same way to obtain a nonsingular row tuple \(R\). Set all unknowns outside \(C\) to zero and set
\[
                g[C]=-M[R,C]^{-1}u[R].                                  \tag{2}
\]
For the empty minor use the empty assignment. Equations (1)–(2) determine the component on every finite bar word in the original coefficient model. They are a determinant formula, with no arbitrary primitive left to choose. The numerical entries of this particular \(31\times41\) native matrix have not been expanded in the accompanying replay.

To prove that (2) works on all rows, take any Hochschild lift given by native formality. First change it by a Hochschild coboundary in arity zero so that its constant is exactly \(sO_a\). In a fixed arity \(n\) with previous choices settled, the existing component and \(-K_nR_n\) differ by a \(\partial_H\)-cycle, by (8) of the coefficient calculation. Every such cycle is homologous to \(\iota_n\) of its \(\rho_n\)-projection. Correcting by the full Hochschild coboundary of an arity-\(n\) primitive achieves the displayed shape while preserving all smaller arities. The extra Cartan prescription at arity one changes \(-K_1R_1\) by a cycle supported on the contractible input disk. This cycle is \(\partial_H\)-exact, by precomposition with the disk contraction, so the same argument applies after the prescription. Through arity four this proves consistency of the 31 equations. Thus \(-u\) lies in the column span of \(M\); (2) solves every row. In all higher arities \(e_n=0\) by the table and the degree bound. Induction in (1), using \(\partial_H\delta=-\delta\partial_H\), proves the complete two-sided cocycle equations.

Three actual values do not require any entries of (2). One has \(\pi Q=\pi N=\pi H_c=\pi T=0\), so adding \(\iota_1g_1\) leaves both disk restrictions in the original calculation unchanged. In particular
\[
 F_1(sQ)=-3sO_a,\qquad F_1(sT)=-sO_{H_c a},\qquad
 F_1(sN)=F_1(sH_c)=0.
\]
The first has PBW coordinate \(-3\) on the vacuum at native index zero. For the second, delete the first spin-two \(-1\) ghost wherever it occurs in the cochain \(h_{3,0}\); with the two signs displayed above, the remaining coefficient is exactly the original coefficient. The accompanying file gives all these terms at the good prime. On the closed input \(T\) the first commutator is \(sO_{Ta}\), and \(QH_ca=Ta\) gives its actual native primitive. Thus the affine case has both a finite all-arity formula and separately evaluated nonzero cochain values in the original resolution. [All signed Cartan PBW coordinates](CARTAN-PBW.json)
