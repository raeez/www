# A single two-sided lift of the affine three-class decides formality

Let \(D\) be the smooth exceptional \(W_4\) vacuum endomorphism dg algebra at \(\tau=-3/2\), with its original marked affine map. Write \(\chi:HH^*(D,D)\to H^*D\) for the Hochschild characteristic map. It evaluates a derived bimodule operation on the regular module. In a strictly unital minimal model it takes a normalized Hochschild cocycle to its zero-input value. For the marked basis \(1,a,b,ab,c,ac,u,au,v,av,z,az\), the image is
\[
\operatorname{im}\chi=
\begin{cases}
H^*D,& \gamma=0,\\
\langle 1,b,ab,c,ac,au,v,av,z,az\rangle,& \gamma\ne0 .
\end{cases}
\]
In particular the native affine degree-three class has a two-sided lift exactly when the ordinary associative dg algebra is formal. The same equivalence holds for any degree-eight class nonzero modulo \(ab\). This conclusion uses the independently checked native involution and quartic normal form. The existence of either lift in the original bimodule complex remains to be determined. [Geometric action and its verification](GEOMETRIC-REVIEW.md) · [Quartic normal form](QUARTIC.md)

In the suspended convention the normalized minimal structure is \(b=b_2+b_4\), where \(b_2(sx,sy)=(-1)^{|x|}s(xy)\) and \(b_4(sa,sa,sa,su)=\gamma s(az)\) is the sole higher coefficient. Write \(F_0=sx\) for the constant term of a proposed Hochschild cocycle \(F\), of suspended degree \(|x|-1\). Graded commutativity of the binary algebra gives \([b_2,F_0]=0\). The next two equations are \([b_2,F_1]=0\) and
\[
          [b_2,F_2]+[b_4,F_0]=0 .
\]
They apply to ordinary, possibly nonequivariant and nonrelative lifts. Higher choices cannot enter the arity-three equation. The characteristic map and these vanishing tests transport under the identity-linear uncurved \(A_\infty\) equivalence used to put the operations in normal form.

For \(x=a\), inserting \(sa\) into \(b_4\) produces \(3\gamma s(az)\) on \((sa,sa,su)\). Each insertion sign is positive since \(sa\) has degree two. The other two permutations with the same multiset have zero value. For every binary \(F_2\) the sum of the three \(s(az)\) coordinates of \([b_2,F_2]\) over these permutations is zero. Indeed \(b_2(sa,su)=-s(au)\) and \(b_2(su,sa)=s(au)\), so the internal \(au\) contributions cancel. On exterior factors the only contributing output of \(F_2(a,u)\) or \(F_2(u,a)\) is its degree-twelve \(z\) component. Its two \(a\)-actions cancel since \(b_2(sa,sz)=-s(az)\) and \(b_2(sz,sa)=s(az)\). The possible value of \(F_2(a,a)\) is a multiple of \(c\), and \(cu=uc=0\) by the native binary computation. Thus the three-position functional reads \(3\gamma\) on the obstruction. In ordinary internal degree \(+1\), the exact incoming differential has rank six, rising to seven when the obstruction for \(\gamma=1\) is adjoined. [Exact matrix and signs](CHARACTERISTIC-EXACT.json)

For \(x=u\), inserting \(su\) into \((sa,sa,sa)\) gives \(\gamma s(az)\), with positive sign because \(sa\) is even after suspension. On this word, the internal \(b_2(sa,sa)\) is zero. The two end terms of \([b_2,F_2]\) cancel for the \(z\) component of \(F_2(a,a)\) and separately vanish for its \(av\) component. This is the only normalized target cell in ordinary internal degree \(+6\), and the incoming Hochschild differential is zero. In particular no multiple of \(ab\) added to \(u\) can alter the obstruction because the normalized quartic has no \(ab\) input. [Native binary source](</tmp/paired-math-dispatch-20261118/astra/p11-exceptional-w4-algebra/extension/RESULT.md:50>) · [Finite computation](characteristic.py)

Every other basis vector \(y\) lifts using only \(F_0=sy\). The binary commutator vanishes, and inserting \(sy\) into \(b_4\) gives zero because it never occurs in the input word \(a,a,a,u\). The unit lifts by strict unitality. These cocycles and the two nonzero obstructions exhaust the possible homogeneous constants when \(\gamma\ne0\). If \(\gamma=0\), every constant lifts in the formal graded-commutative algebra. The argument identifies the image of \(\chi\) in this graded basis and remains invariant on replacing \(u\) by a nonzero multiple of \(u\) plus a multiple of \(ab\).

On the original geometric side either a two-sided derived endomorphism of the regular \(D\)-bimodule with characteristic value \(a\), or an actual Hochschild characteristic value nonzero on \(H^8/\langle ab\rangle\), suffices. The known operation on all coefficient modules obtained by precomposing with \(a\) gives the one-sided Yoneda action of every vacuum class. Two-sided coherence for that operation is the additional content of this test. [Original Yoneda calculation](</tmp/astra62-programme-rebuild-20261118/constructions/w-bockstein/DOSSIER.md:58>)
