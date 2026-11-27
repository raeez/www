# Bar constructions and coherent operations

For three ordered fields, forming the two products \((ab)c\) and \(a(bc)\) may require two different collision maps. Once their inputs and outputs have been identified, what could relate the maps themselves? The [scalar collision residues](04-factorization.md#ch04-three-residues) give \(1\) and \(0\) in two orders. Regard them as the values at \(1\) of maps \(k\to k\), with the field \(k\) concentrated in degree zero. No vector has a differential equal to their difference.

Change the target. Give it a vector \(u\) in degree \(-1\), a vector \(v\) in degree zero and differential \(du=v\). Now the maps \(1\mapsto v\) and \(1\mapsto0\) differ by the differential of \(1\mapsto u\). The map sending \(1\) to \(u\) is a homotopy between these two maps. For the associator of fields we need a primitive that depends trilinearly on the inputs and also accounts for their differentials.

Write \([a|b|c]\) for the inputs before multiplication. In an ordinary associative algebra concentrated in degree zero the signed ways to erase one separator give \([ab|c]-[a|bc]\). Erasing the remaining separator gives \([(ab)c]-[a(bc)]=0\). When this last difference is a boundary, a three-input operation can supply its primitive. Four inputs require the primitives themselves to agree up to a further homotopy. On a curve the [consecutive cuts](04-factorization.md#ordered-cut-geometry) also bound the length of these words, because each nonempty block uses a label.

Suppose the second system in a coupling is a complex of probe states. Assign an operator \(T\) to a degree-zero letter \(\epsilon\) satisfying \(\epsilon^2=0\). Acting twice on the probe gives \(T^2\). To respect the relation up to homotopy, we need a primitive for \(T^2\) in the complex of probe operators. That primitive is the value assigned to \([\epsilon|\epsilon]\). Splitting the word recovers the two successive actions it compares. [A probe with a nonzero square and a chosen primitive](#ch05-twisting-cochain-probe)

## Complexes retain the equations and their solutions {#cohomology-and-parameters}

**Definition (cochain complex).** A cochain complex is a sequence of vector spaces and linear maps
\[
\cdots\longrightarrow V^{n-1}\xrightarrow{d}V^n
\xrightarrow{d}V^{n+1}\longrightarrow\cdots,
\qquad d^2=0.
\]
The superscript is the **cohomological degree**, and the differential has degree \(+1\). A vector killed by \(d\) is a cycle; a vector of the form \(dw\) is a boundary. Their quotient is
\[
H^n(V)=\ker(d:V^n\to V^{n+1})/
\operatorname{im}(d:V^{n-1}\to V^n).
\]
In the two-term target above, \(v\) represents zero in cohomology and \(u\) witnesses that fact. More generally, once \(dw=v\) has a solution, so does \(w+z\) for any cycle \(z\) in the same degree. The set of solutions can therefore matter even after the class of \(v\) has disappeared.

Our shift convention is
\[
V[1]^n=V^{n+1},\qquad d_{V[1]}=-d_V.
\]
Thus a vector of degree \(r\) in \(V\) has degree \(r-1\) in \(V[1]\). Write \(sv\) for that shifted vector, so \(s\) has degree \(-1\). Moving a map \(G\) of degree \(|G|\) past a homogeneous vector \(v\) of degree \(|v|\) contributes the Koszul sign \((-1)^{|G||v|}\). In particular the tensor differential is
\[
d(v\otimes w)=dv\otimes w+(-1)^{|v|}v\otimes dw .
\]

**Definition (cochain homotopy).** A degree-zero chain map \(f:V\to W\) commutes with the differentials. A homotopy from \(g\) to \(f\) is a degree-minus-one map \(h\) satisfying
\[
f-g=d_Wh+hd_V.
\]
If \(x\) is closed, then \((f-g)x=d_W(hx)\). This proves that homotopic maps induce the same map on cohomology. To keep the choice of \(h\), put maps of all degrees into a single complex
\[
\operatorname{Hom}^r(V,W)=\prod_n\operatorname{Hom}(V^n,W^{n+r}),
\qquad
\partial f=d_Wf-(-1)^rfd_V.
\]
Chain maps are its degree-zero cycles, and homotopies identify maps whose difference is a boundary. The product over \(n\) is intentional: a degree-\(r\) map has a component on every degree of \(V\).

A chain map is a **quasi-isomorphism** if it induces an isomorphism on every cohomology group. The ordinary **derived category** formally makes these maps invertible. We will also retain the derived mapping complexes, obtained by resolving the inputs as necessary, rather than keeping only their degree-zero cohomology. This enhanced form of the derived category remembers homotopies and homotopies between them; it is the meaning intended when the geometric theorem below refers to higher mapping spaces.

Consider the complex
\[
\mathbb C u_1\oplus\mathbb C u_2
\xrightarrow{\ d_t\ }
\mathbb C v_1\oplus\mathbb C v_2,
\qquad d_tu_1=tv_1,\quad d_tu_2=0,
\]
{#eq-cohomology-jump}
in degrees zero and one. For \(t\ne0\) the differential identifies the line spanned by \(u_1\) with the line spanned by \(v_1\). Its inverse on that line is the homotopy \(h(v_1)=t^{-1}u_1\). Extend \(h\) by zero on the other basis vectors. If \(p\) projects to the remaining \(u_2,v_2\) summand and \(i\) includes it, then
\[
dh+hd=1-ip.
\]
Indeed \(hd\) fixes \(u_1\), \(dh\) fixes \(v_1\), and both vanish on the retained pair. What happens at \(t=0\)? The equation \(dw=v_1\) then has no solution. The extra pair now contributes one class in each degree, so the cohomology dimensions jump from \((1,1)\) to \((2,2)\). The Euler characteristic stays zero. The pole in \(t^{-1}u_1\) explains why the contraction on the nonzero fibres cannot extend across zero.

::: figure fig-cohomology-jump

## Relations can leave a higher operation {#ch05-relations-can-leave-a-higher-operation}

In the two-term family, solving \(dw=v_1\) required the choice \(w=t^{-1}u_1\). What if the vector to be made exact is itself a product? We need a multiplication compatible with the differential.

**Definition (differential graded algebra).** A differential graded (dg) algebra is a graded associative algebra \(A\) with a differential of degree \(+1\) satisfying
\[
d(ab)=(da)b+(-1)^{|a|}a\,db.
\]
Its cohomology is an associative graded algebra. Passing to cohomology nevertheless loses information about how products become boundaries.

Can two zero products in \(H^*(A)\) leave a detectable ternary operation? Let
\[
A=T(a,b,c,x,y),\qquad
|a|=|b|=|c|=|x|=|y|=1,
\]
be the free associative graded algebra on five generators, with
\[
da=db=dc=0,\qquad dx=ab,\qquad dy=bc.
\]
Extend \(d\) by the graded Leibniz rule. Since \(a,b,c\) are closed, \(d^2=0\). The cohomology products \([a][b]\) and \([b][c]\) vanish. The chosen primitives \(x,y\) then give
\[
z=ay+xc,
\qquad
dz=-abc+abc=0.
\]
In the free algebra, different words of length two are independent. The only boundaries in degree two are linear combinations of \(dx=ab\) and \(dy=bc\). Neither contains \(ay\) or \(xc\). This proves that \(z\) represents a nonzero class for these particular primitives. We still have to test the other choices of primitives.

Changing \(x\) or \(y\) by a degree-one cycle changes \([z]\) by an element of
\([a]H^1(A)+H^1(A)[c]\). In this example \(H^1(A)\) is spanned by \([a],[b],[c]\), and that indeterminacy cannot remove the words \(ay\) and \(xc\). The resulting nonzero coset is a **triple Massey product**. Its degree is \(1+1+1-1=2\), since each primitive lowers the product degree by one. To see what the multiplication table misses, give the algebra \(H^*(A)\) itself zero differential. Its two adjacent products are already zero as elements. Choosing both primitives zero gives the zero coset there.

The same choice of primitive enters the transfer of a product to a smaller complex. Let \(i:H\to A\) and \(p:A\to H\) be chain maps with \(pi=1\). Put \(P=ip\) and choose \(h:A\to A\) of degree \(-1\) with \(dh+hd=1-P\). For homogeneous \(a,b,c\in H\), write \(a'=ia\), \(b'=ib\), \(c'=ic\). The product on \(H\) is \(m_2(a,b)=p(a'b')\). To multiply this result by \(c\), one first sends it back to \(A\) by \(i\), which gives \(P(a'b')\). Thus the two bracketings in \(H\) are \(p(P(a'b')c')\) and \(p(a'P(b'c'))\). To subtract the second from the first, write \(P=1-(1-P)\). The terms \(p((a'b')c')\) and \(p(a'(b'c'))\) cancel by associativity in \(A\), leaving
\[
 p\bigl(a'(1-P)(b'c')-(1-P)(a'b')c'\bigr).
\]
In the Hom complex \(\partial h=dh+hd=1-P\). Thus each occurrence of \(1-P\) has a specified primitive. In the first term apply \(1\otimes h\) to \(a'\otimes(b'c')\). Moving \(h\) across \(a'\) contributes \((-1)^{|a|}\). In the second term \(h\) acts on \(a'b'\) before the multiplication by \(c'\). The resulting trilinear map is
\[
 m_3(a,b,c)=p\bigl((-1)^{|a|}a'h(b'c')-h(a'b')c'\bigr).
\]
Taking its Hom differential replaces \(h\) by \(dh+hd=1-P\) in both terms, since the product of \(A\) and the maps \(i,p\) commute with the differentials. Thus \(\partial m_3\) is the left bracketing minus the right. The [arity-three identity](#eq-ch05-associator-homotopy) expands this equality on all homogeneous inputs.

## Words and the reduced bar construction {#ch05-words-and-the-reduced-bar-construction}

The two terms in the transferred \(m_3\) remember which pair was multiplied first. To record all such choices, keep the inputs in a word and let multiplying neighbours erase one separator. A word \([a|b]\) should have degree \(|a|+|b|-2\) if the one-letter answer \([ab]\) has degree \(|a|+|b|-1\). Lowering the degree of each letter by one gives exactly this convention. The empty word will carry a copy of the ground field. An augmentation singles out the part of the algebra from which to take the letters of a nonempty word.

**Definition (reduced bar construction).** An augmentation of a unital dg algebra is a dg algebra map \(\epsilon:A\to k\), where \(k\) is the ground field. It splits the underlying complex as
\(A=k\cdot1\oplus\bar A\), with \(\bar A=\ker\epsilon\). The **reduced bar construction**, including its empty word, is
\[
BA=T^c(\bar A[1])
=k\oplus\bigoplus_{n\ge1}(\bar A[1])^{\otimes n}.
\]
We write
\[
[a_1|\cdots|a_n]=sa_1\otimes\cdots\otimes sa_n,
\qquad
|[a_1|\cdots|a_n]|=\sum_i|a_i|-n.
\]
The superscript \(c\) indicates the tensor **coalgebra**. Its coproduct splits a word at every position:
\[
\Delta[a_1|\cdots|a_n]
=\sum_{i=0}^n[a_1|\cdots|a_i]
\otimes[a_{i+1}|\cdots|a_n].
\]
The empty word is \(1\). This deconcatenation is coassociative because splitting at two positions gives the same three consecutive subwords in either order. For instance the reduced coproduct of \([a|b|c]\) has the two terms \([a]\otimes[b|c]\) and \([a|b]\otimes[c]\). It retains both places where the triple can be cut.

On the two-letter word \([a|b]\), the internal differential can act on either letter and the product can merge them into \([ab]\). Each contribution must raise the shifted degree by one. For a single letter the shift changes the sign of its differential. For a merger we use the signed product on the shifted factors. The two components are
\[
b_1(sa)=-s(da),\qquad
b_2(sa\otimes sb)=(-1)^{|a|}s(ab).
\]
Both maps have degree \(+1\) on the shifted letters. Inserting either map after \(sa_1,\ldots,sa_{i-1}\) therefore contributes the sign \((-1)^{\sum_{j<i}(|a_j|-1)}\). Including the signs of \(b_1,b_2\) themselves gives
\[
\begin{aligned}
b[a_1|\cdots|a_n]
={}&\sum_{i=1}^n
(-1)^{1+\sum_{j<i}(|a_j|-1)}
[a_1|\cdots|da_i|\cdots|a_n]\\
&+\sum_{i=1}^{n-1}
(-1)^{|a_i|+\sum_{j<i}(|a_j|-1)}
[a_1|\cdots|a_ia_{i+1}|\cdots|a_n].
\end{aligned}
\]
The equation \(b^2=0\) expresses three familiar facts: \(d^2=0\), the Leibniz rule, and associativity. For an ordinary algebra concentrated in degree zero, the internal-differential terms vanish, and
\[
b[a|b]=[ab],\qquad
b[a|b|c]=[ab|c]-[a|bc].
\]
Applying \(b\) again to the three-letter word gives \([(ab)c]-[a(bc)]=0\). The signs on homogeneous inputs can be read from the two routes separately. On the left the signs multiply to \((-1)^{|a|+|ab|}=(-1)^{|b|}\). On the right the first merger, on the last two letters, crosses \(sa\), giving total sign \((-1)^{|a|-1+|b|+|a|}=-(-1)^{|b|}\). Thus the two mergers contribute \((-1)^{|b|}s((ab)c-a(bc))\). Mergers at disjoint pairs occur in opposite orders with opposite signs. Two internal differentials cancel or square to zero, and the mixed terms on a multiplying pair cancel by the Leibniz rule. These exhaust the terms in \(b^2\). [Loday–Vallette, *Algebraic Operads*, §§2.2–2.3](https://www.math.univ-paris13.fr/~vallette/Operads.pdf#page=51)

Two augmented algebras generated by one element in degree zero distinguish a nonzero square from a square-zero relation. For \(A=k[x]\), augmented by \(x\mapsto0\), the two-term free resolution
\[
0\longrightarrow A\xrightarrow{\,x\,}A\longrightarrow k\longrightarrow0
\]
computes the same groups as the bar resolution. Tensoring over \(A\) with \(k\) kills its differential, so
\[
H^*(BA)=k\oplus k\cdot[x],\qquad |[x]|=-1.
\]
This calculation has a visible trace on words. For instance \(b[x|x]=[x^2]\), so the one-letter class represented by \(x^2\) is zero. For \(m\ge2\), \(b[x|x^{m-1}]=[x^m]\) does the same for every higher power. If we impose \(x^2=0\) in the algebra, then \([x|x]\) becomes a cycle. Can a longer word have it as its boundary?

For \(A=k[\epsilon]/(\epsilon^2)\), the augmentation ideal is one-dimensional and its product is zero. Every bar differential is therefore zero:
\[
BA=\bigoplus_{n\ge0}k[\epsilon|\cdots|\epsilon],
\qquad H^{-n}(BA)=k\quad(n\ge0).
\]
The corresponding free resolution has multiplication by \(\epsilon\) at every step. It is exact before tensoring with \(k\), and every differential becomes zero afterwards. Thus the single relation \(\epsilon^2=0\) produces homological information in arbitrarily long words. These groups are traditionally denoted \(\operatorname{Tor}_n^A(k,k)\), with \(n=-\text{cohomological degree}\).

## One differential encodes all associativity homotopies {#ch05-one-differential-encodes-all-associativity-homotopies}

In the strictly associative case the two binary mergers sufficed on three letters. Allow a third component to replace \([a|b|c]\) by a single letter. On \([x|a|b|c]\), cutting after \(x\) before this replacement must leave the same right-hand operation on \([a|b|c]\), with the sign for passing \(sx\). Every cut outside a substituted string imposes such a condition. Deconcatenation expresses this requirement.

**Definition (coderivation).** Let \(V\) be a graded vector space. A degree-one map \(b\) on \(T^c(V[1])\) is a coderivation if
\[
\Delta b=(b\otimes1+1\otimes b)\Delta,
\]
with the graded tensor convention. For a coderivation vanishing on the empty word, project its value on words of length \(n\) to the one-letter summand. The resulting maps are
\[
b_n:(V[1])^{\otimes n}\longrightarrow V[1],
\]
with \(n\ge1\). They determine \(b\) by inserting \(b_n\) at every consecutive string of \(n\) letters, with the sign for passing its prefix. Only finitely many insertions occur on a finite word.

**Definition (uncurved \(A_\infty\)-algebra).** Such a structure on \(V\) is a degree-one coderivation \(b\) vanishing on the empty word and satisfying \(b^2=0\). Use \(b_n=-s\,m_n(s^{-1})^{\otimes n}\), with graded tensor products. Thus \(m_n:V^{\otimes n}\to V\) has degree \(2-n\). For \(m_1=d\) and \(ab=m_2(a,b)\) this gives the preceding \(b_1,b_2\), and
\[
 b_3(sa\otimes sb\otimes sc)=(-1)^{|b|}s\,m_3(a,b,c).
\]

In length one, \(b^2=0\) gives \(d^2=0\). In length two it says that \(m_2\) is a chain map. In length three, project \(b^2[a|b|c]\) onto one letter. The two binary mergers contribute \((-1)^{|b|}s((ab)c-a(bc))\). The terms inserting \(b_1\) before or after \(b_3\) contribute \(-(-1)^{|b|}s(\partial m_3)(a,b,c)\), where \(\partial\) is the [Hom differential](#cohomology-and-parameters). Cancelling the common factor gives the associator on homogeneous inputs,
\[
\begin{aligned}
 &(ab)c-a(bc)\\
 &\quad=d\,m_3(a,b,c)+m_3(da,b,c)\\
 &\qquad+(-1)^{|a|}m_3(a,db,c)\\
 &\qquad+(-1)^{|a|+|b|}m_3(a,b,dc).
\end{aligned}
\]
{#eq-ch05-associator-homotopy}
The difference of bracketings has degree zero, so its primitive \(m_3\) has degree \(-1\). If \(a,b,c\) are closed, only \(d\,m_3(a,b,c)\) remains on the right. Consequently the induced product on cohomology is associative. A higher operation can nevertheless carry information there. In the [free dg algebra](#ch05-relations-can-leave-a-higher-operation) the original multiplication is already strictly associative. The nonzero Massey coset measures the effect of choosing primitives for the vanishing products \(ab\) and \(bc\) when the multiplication is transferred.

In length \(n\), the one-letter component of \(b^2\) is the sum
\[
 \sum_{\substack{r+s+t=n\\s\ge1}}
 b_{r+1+t}(1^{\otimes r}\otimes b_s\otimes1^{\otimes t})=0 .
\]
For any summand the inner map crosses \(r\) shifted letters. In length four, the terms with inner and outer arities \(2,3\) or \(3,2\) are the five edges of the pentagon. For closed degree-zero \(a,b,c,e\), the equation takes the form
\[
\begin{aligned}
 &d\,m_4(a,b,c,e)\\
 &\quad=a\,m_3(b,c,e)-m_3(ab,c,e)\\
 &\qquad+m_3(a,bc,e)-m_3(a,b,ce)\\
 &\qquad+m_3(a,b,c)\,e .
\end{aligned}
\]
To read the five signs, start at \(((ab)c)e\) and end at \(a(b(ce))\). One path passes first through \((a(bc))e\) and then through \(a((bc)e)\). Its three homotopies are \(m_3(a,b,c)e\), \(m_3(a,bc,e)\) and \(a\,m_3(b,c,e)\). The other path passes through \((ab)(ce)\) and uses \(m_3(ab,c,e)\) and \(m_3(a,b,ce)\). Each path has the same differential, the difference of the endpoint products. Their difference is a cycle of degree \(-1\), and the displayed equation specifies its primitive \(m_4\) of degree \(-2\). In higher arities the same equation \(b^2=0\) gives the successive comparisons. **Coherence** consists of these operations and identities on the complex.

### Where a scalar output goes in the reduced bar {#ch05-scalar-bar-curvature}

The letters of the reduced bar of an augmented algebra belong to its augmentation ideal. Their product stays in that ideal. What changes if we can project onto the unit line only as a vector space? In \(A=M_2(k)\) over a characteristic-zero field let \(p(a)=\operatorname{tr}(a)/2\). For traceless matrices write \(a*b=ab-p(ab)1\) for the traceless part of their product. Put \(e=E_{12}\), \(f=E_{21}\) and \(h=E_{11}-E_{22}\), where \(E_{ij}\) are the matrix units. Then \(ef=(1+h)/2\), \(fh=f\) and \(h^2=1\). If we use only the traceless products in the bar differential \(\bar b\), its square on three letters is
\[
 \bar b^2[e|f|h]
 =[(e*f)*h]-[e*(f*h)]
 =0-\tfrac12[h].
\]
The missing contribution came from the scalar \(p(ef)=1/2\), which multiplies \(h\) at the next step. Indeed, on any three traceless matrices the projected associator is \(p(bc)a-p(ab)c\).

For a strictly unital uncurved \(A_\infty\)-algebra choose a graded linear map \(p:A\to k\) with \(p(1)=1\), and write \(\bar A=\ker p\). Strict unitality means that \(1\) acts by the binary unit law and higher products vanish on inputs containing \(1\). On \(T^c(\bar A[1])\), project each \(b_n\) to the shifted complement to obtain the coderivation \(\bar b\). Record its discarded scalar as the degree-two functional
\[
 \theta([a_1|\cdots|a_n])
   =-p\bigl(s^{-1}b_n(sa_1\otimes\cdots\otimes sa_n)\bigr),
 \qquad \theta(\text{empty word})=0 .
\]
In the one-letter component of \(b^2=0\), an intermediate scalar can return to the complement only by multiplying the remaining letter on the left or on the right. The two unit products have opposite shifted signs. Projecting the same identity onto the scalar line gives the second equation below. With deconcatenation \(\Delta\), the curved bar identities are
\[
 \bar b^2=(\theta\otimes1-1\otimes\theta)\Delta,
 \qquad \theta\bar b=0 .
\]
{#eq-ch05-reduced-bar-curvature}
Here \(k\otimes T^c(\bar A[1])\) and \(T^c(\bar A[1])\otimes k\) are identified with the word space. In the matrix example \(\theta([e|f])=-1/2\) and \(\theta([f|h])=0\), which gives the computed square. The functional \(\theta\) is the **curvature of the reduced bar coalgebra**. [Burke, Corollary 4.11 and Definition 4.12](https://arxiv.org/pdf/1801.06943#page=17)

For a boundary interaction, the scalar can be the quantity we want to recover. In the two-periodic one-variable matrix factorisation with potential \(W=x^3\) or \(W=x^4\), the marked minimal boundary algebra has unit \(1\) and an odd class \(\psi\). In both cases \(m_0=0\), \(m_1=0\) and \(m_2(\psi,\psi)=0\). With the boundary coordinate of Chapter 19, the cubic gives \(m_3(\psi,\psi,\psi)=1\) and the quartic gives \(m_4(\psi,\psi,\psi,\psi)=-1\). The remaining products on nonempty words of \(\psi\)'s vanish. Take \(p(\psi)=0\). Since \(s\psi\) has even parity, the sign in \(b_n=-s\,m_n(s^{-1})^{\otimes n}\) gives \(\theta([\psi|\cdots|\psi])\) equal to the scalar value of \(m_n\). Thus \(\bar b=0\) in both examples, while the curvature on words has generating series \(t^3\) and \(-t^4\), respectively.

On the generator \(t\) of \(k[t]/(t^4)\), the cubic has nonzero obstruction \(t^3\,1\), while the quartic gives zero. On the generator of \(k[t]/(t^5)\) the quartic gives \(-t^4\,1\ne0\). For an even \(r\) in the maximal ideal of a local Artin base, the two obstructions have values \(r^3\,1\) and \(-r^4\,1\). This records an operation with three or four inputs in the undeformed algebra, whose zero-input operation vanishes. [The boundary deformation with square \(W(x)-W(-t)\)](19-interacting-theories.md#ch19-boundary-potential)

::: example {#ch05-two-marked-artin-parameters title="Two parameters with the same tangent class"}
Take \(S=\mathbb Q[u,v]/(u^3,v^3)\) with maximal ideal \(\mathfrak m=(u,v)\). The parameters \(r=u\) and \(r'=u+v^2\) have the same nonzero class in \(\mathfrak m/\mathfrak m^2\). Both fourth powers vanish, but their cubes are
\[
 r^3=0,\qquad (r')^3=3u^2v^2\ne0 .
\]
Indeed the monomials \(u^a v^b\) with \(0\le a,b<3\) form a basis of \(S\). The cubic boundary is flat at \(r\) and has scalar obstruction \(3u^2v^2\,1\) at \(r'\). The quartic boundary is flat at both marked parameters.
:::

## Cobar reverses the construction {#ch05-cobar-reverses-the-construction}

Return to an augmented algebra. For closed degree-zero \(a,b\) in the augmentation ideal, the bar differential gives \(b[a|b]=[ab]\). To recover multiplication from this coalgebra, we need a differential whose boundary identifies the formal product of the two one-letter generators with the generator for \(ab\). The old word \([a|b]\) supplies both terms of that boundary. Its bar differential supplies \([ab]\), and cutting it supplies \([a]\otimes[b]\).

Deconcatenation on \([a|b|c]\) produces at most three nonempty factors. For a counital coaugmented dg coalgebra \(C=k\oplus\bar C\), write \(1\) for the image of the coaugmentation and \(\bar C\) for the kernel of the counit. On \(c\in\bar C\), remove \(1\otimes c+c\otimes1\) from \(\Delta c\) to obtain the reduced coproduct \(\bar\Delta c\). The coalgebra is **conilpotent** if sufficiently many iterated reduced coproducts kill each element. The three-letter bound illustrates this for the tensor coalgebra.

**Definition (cobar construction).** The cobar construction is the tensor algebra
\[
\Omega C=T(\bar C[-1]).
\]
Write \(uc\) for a generator in \(\bar C[-1]\), so \(|uc|=|c|+1\). If \(\bar\Delta c=\sum c'\otimes c''\), its differential is the derivation determined by
\[
d_\Omega(uc)=-u(d_Cc)
+\sum(-1)^{|c'|+1}(uc')(uc'').
\]
To check the two signs, take closed degree-zero elements \(a,b\) of the augmentation ideal. The shifted element \([a]\) has degree \(-1\), so its cut contributes \((-1)^{-1+1}=1\). Closedness kills both internal differential terms in \(b[a|b]\). The cobar differential on the generator \(u[a|b]\) is therefore
\[
d_\Omega u[a|b]=-u[ab]+(u[a])(u[b]).
\]
Sending \(u[a]\) to \(a\) and longer single generators to zero takes the displayed boundary to \(-ab+ab=0\). This is the strict counit \(\Omega BA\to A\) on the first multiplication relation. For a coalgebra \(C\), the same check on every generator \(uc\) determines when an assignment of elements of \(A\) extends to a chain map.

**Definition (twisting cochain).** A degree-one map \(\tau:C\to A\), vanishing on the coaugmentation and landing in \(\bar A\), is a twisting cochain when
\[
d_A\tau+\tau d_C+\mu_A(\tau\otimes\tau)\bar\Delta=0.
\]
Here \((\tau\otimes\tau)(c'\otimes c'')=(-1)^{|c'|}\tau(c')\otimes\tau(c'')\). This one equation says exactly that \(uc\mapsto\tau(c)\) extends to a dg algebra map \(\Omega C\to A\). For conilpotent \(C\), iterating its reduced coproduct gives the corresponding dg coalgebra map \(C\to BA\). Taking algebra maps that preserve the augmentation and counital coalgebra maps that preserve the coaugmentation gives the strict bar–cobar adjunction
\[
\operatorname{Hom}_{\rm dgAlg}(\Omega C,A)
\cong\operatorname{Tw}(C,A)
\cong\operatorname{Hom}_{\rm dgCoalg}(C,BA).
\]
The identities correspond to the strict counit \(\Omega BA\to A\) just tested on \(u[a|b]\), and the strict unit \(C\to B\Omega C\). In the latter map a one-letter component records \(c\) and the longer components record its successive reduced coproducts. Conilpotence makes the word sum finite on each element. An adjunction alone gives no inverse to either comparison.

::: example {#ch05-primitive-and-augmentation title="A primitive generator tests the augmentation"}
Let \(C=k1\oplus kc\) with zero differential and \(c\) primitive of degree \(-1\). Then \(X=uc\) has degree zero and \(d_\Omega X=0\). Thus \(\Omega C=k[X]\), with augmentation \(X\mapsto0\). Take \(A=k\) with its identity augmentation. Evaluation at \(X=1\) gives a unital dg algebra map. A reduced twisting cochain takes \(c\) into \(\ker(k\to k)=0\), so its map must send \(X\) to zero. This is the unique augmentation-preserving evaluation. On the coalgebra side \(Bk=k\), and the corresponding map is the counit of \(C\).
:::

### Coupling a square-zero letter to a probe {#ch05-twisting-cochain-probe}

For the square-zero letter \(\epsilon\), take the subcoalgebra \(C\subset B(k[\epsilon]/(\epsilon^2))\) spanned by the empty word, \(e=[\epsilon]\) and \(f=[\epsilon|\epsilon]\). Their degrees are \(0,-1,-2\). The differential is zero and the only nonzero reduced coproduct is \(\bar\Delta f=e\otimes e\). Fix a probe complex \(V\) and let \(D=\operatorname{End}_k(V)\), with composition and the Hom differential \(\partial\). Here we use unital maps to \(D\) with unrestricted generator images. Equivalently use augmented maps to \(k\oplus D\) with \(D\) as augmentation ideal.

A twisting cochain assigns \(T=\tau(e)\in D^0\) and \(H=\tau(f)\in D^{-1}\). The tensor sign for applying the second \(\tau\) past \(e\) is \((-1)^{-1}=-1\). Its two equations are therefore
\[
 \partial T=0,\qquad \partial H=T^2 .
\]
The cobar algebra has free generators \(X=ue\) and \(Y=uf\), with \(dX=0,\ dY=X^2\). A choice of \(T,H\) extends to a dg algebra map precisely when these two equations hold. Changing the probe operator algebra by a dg algebra map carries both assignments to their images. This is the sense in which \(\Omega C\) represents the coupling problem for this coalgebra. [Loday–Vallette, Theorem 2.2.9](https://www.math.univ-paris13.fr/~vallette/Operads.pdf#page=54) · [Paquette and Williams, §5.2](https://arxiv.org/pdf/2110.10257v4#page=23)

If \(V\) is concentrated in degree zero, the second equation requires \(T^2=0\). On two states the matrix \(E_{12}\) meets this condition and the identity does not. Take instead the complex \(kv\xrightarrow{\,d\,}kw\) in degrees \(-1,0\), with \(dv=w\). Choose \(T=1_V,\ H(w)=v,\ H(v)=0\). Then \((dH+Hd)v=v\) and \((dH+Hd)w=w\). The identity now gives a coupling through length two, with the nonzero composite accounted for by \(H\). A larger coalgebra can impose equations on longer words. For ordered configurations the number of labels bounds every word in each arity.

## Ordered cuts give a finite geometric bar construction {#ch05-ordered-cuts-give-a-finite-geometric-bar-construction}

For three letters, repeating the first position sends \((x,y)\) to \((x,x,y)\). The coefficient on that repeated word must recover the two-letter coefficient under the specified collision pullback. Repetitions of arbitrary adjacent positions give the following system.

**Definition (word coefficient system).** Let \(X\) be a smooth separated finite-type curve over a characteristic-zero field \(k\). Write \(\mathcal D(X^n)\) for the unbounded derived category of right algebraic differential modules with quasi-coherent underlying modules, retaining its higher mapping spaces. A word coefficient system consists of complexes \(M_n\in\mathcal D(X^n)\) for \(n\ge1\), together with coherent equivalences
\[
d_\alpha^!M_n\simeq M_m
\qquad
\bigl(\alpha:[n]\twoheadrightarrow[m]\text{ monotone}\bigr),
\]
where \(d_\alpha(x)_i=x_{\alpha(i)}\). Here \(d_\alpha^!\) is extraordinary derived pullback. The equivalences include their compatibilities under composition and all higher homotopies. Add an isolated empty coefficient \(M_0\in D(k)\), with no collision arrow from a nonempty configuration to it. Denote this category by \(\mathcal W_X\); the integer \(n\) is the arity.

For \(p+q=n\), let \(U_{p,q}\subset X^n\) be the open set on which every point in the first block is distinct from every point in the second. There is no separation condition within either block. With \(j_{p,q}:U_{p,q}\hookrightarrow X^n\), define consecutive-cut convolution by
\[
(M\star N)_n=
\bigoplus_{p+q=n}Rj_{p,q*}j_{p,q}^*
(M_p\boxtimes^{\mathbf L}N_q).
\]
The symbol \(\boxtimes^{\mathbf L}\) means derived external tensor product. Restriction keeps the two blocks apart, and \(Rj_{p,q*}\) extends that coefficient to \(X^n\). For three nonempty blocks both ways of iterating \(\star\) invert the differences between every pair of blocks. This common localization is what allows comparison of the two bracketings. Empty blocks contribute their complexes over \(k\). [The two cut opens for three labels](04-factorization.md#ordered-cut-geometry)

The unit is \(\mathbf1=(k,0,0,\ldots)\). An augmented algebra is **connected in arity** if its augmentation identifies \(A_0\) with \(k\). A counital coaugmented coalgebra has the analogous condition \(C_0\simeq k\). This condition allows arbitrary cohomological degrees. The augmentation ideal \(\bar A\) and the coaugmentation coideal \(\bar C\) (the kernel of the counit) both vanish on the empty word. The convolution of such objects has the bound
\[
(M^1\star\cdots\star M^r)_n=0
\quad\text{if all }M^i_0=0\text{ and }r>n.
\]
Every nonzero term assigns at least one point to each factor. At \(n=3\) the possibilities with two positive factors have arities \((1,2)\) and \((2,1)\). With three they have arities \((1,1,1)\), and with four the sum is empty.

**Theorem: connected consecutive-cut duality.** In \(\mathcal W_X\), bar and cobar for consecutive-cut convolution are inverse equivalences between connected augmented coherent associative algebras and connected counital coaugmented coherent coassociative coalgebras. The equivalence includes their full mapping spaces. It requires no cohomological boundedness or finite-dimensionality of coefficients.

The bar and cobar functors compare maps and their higher homotopies as well as objects. For strict dg inputs their normalized models have the differentials just described. To see why the constructions converge, split the augmentation and coaugmentation in each degree. In the simplicial bar the normalized quotient discards words containing a unit. In the cosimplicial cobar the common fibre of the counit maps retains words in the coaugmentation coideal. The normalized layers left in length \(r\) are
\[
\bar A^{\star r}[r],\qquad \bar C^{\star r}[-r].
\]
In arity \(n\), they vanish for \(r>n\). Consequently the relevant constructions stabilize after finitely many normalized stages in each coefficient. No interchange of an arbitrary infinite tensor product with an inverse limit is needed. The underlying filtered associative duality is developed by Matsuoka, [*Koszul duality between \(E_n\)-algebras and coalgebras in a filtered category*, Lemmas 4.13 and 4.17](https://arxiv.org/html/1409.6943v4); intrinsic bar and cobar are treated in Lurie, [*Higher Algebra*, §5.2.2](https://www.math.ias.edu/~lurie/papers/HA.pdf#page=821).

Consider a word of words in the composite bar and cobar. On the associated graded, fix the flattened list of \(r\) positive letters. With two letters there are two copies of their coefficient. The one gap can separate the two words or lie inside one word. Changing that assignment gives the identity up to sign, so the two copies form a contractible complex. With three letters record the two gap assignments by \(00,10,01,11\). Here \(0\) marks a gap inside a word and \(1\) a separator between words. The four copies form a square. Changing the first gap pairs \(00\) with \(10\) and \(01\) with \(11\). The opposite incidence signs around the square make this contraction compatible with changing the second gap.

For \(r>1\) there are \(r-1\) gaps. Pair each assignment with the one that differs only at the first gap. Every other change belongs to a square of the same kind, so the contraction works on the whole cube. Only the empty and one-letter terms remain. In arity \(n\) the filtration has only finitely many nonzero layers. The equivalence on its associated graded therefore gives an equivalence on the original coefficient.

For strict dg representatives the twisting-cochain adjunction is \(\Omega_{\rm dg}\dashv B_{\rm dg}\). The intrinsic connected equivalence also has the adjunction \(B\dashv\Omega\), with maps \(A\to\Omega BA\) and \(B\Omega C\to C\). The comparison of the two presentations identifies their equivalences, not their oppositely directed canonical chain maps.

::: figure fig-connected-bar-cobar

### Lifting through a square-zero ideal {#ch05-relative-lifting}

Suppose a multiplication is known modulo an ideal \(J\) with \(J^2=0\). Choose lifts of \(a,b\) and of their product. The difference between multiplying the lifts and lifting the product lies in \(J\). Can we remove this difference while keeping a given action on states? The first obstruction can already be calculated for ordinary algebras.

Fix unital algebra maps \(f:A\to B\) and \(\alpha:A\to C\) over a field \(k\) of arbitrary characteristic. Let \(q:B'\twoheadrightarrow B\) be a unital algebra surjection with square-zero kernel \(J\), and let the unital algebra map \(\rho:B'\to C\) record the prescribed action. Suppose a unital linear \(s:A\to B'\) satisfies \(qs=f\) and \(\rho s=\alpha\). Its defect \(D(a,b)=s(a)s(b)-s(ab)\) maps to zero under both \(q\) and \(\rho\), hence lies in \(I=J\cap\ker\rho\). For \(u\in I\), set \(a\cdot u=s(a)u\) and \(u\cdot a=us(a)\). Both products lie in \(I\). Why do these formulas give an \(A\)-bimodule when \(s\) need only be linear? The defect \(D(a,b)\) and \(u\) both belong to \(J\), so \(D(a,b)u=uD(a,b)=0\). Thus the left and right actions each respect multiplication in \(A\), and associativity in \(B^{\prime}\) makes the two actions commute. Changing \(s(a)\) by an element of \(J\) gives the same actions on \(I\).

Expand \((s(a)s(b))s(c)\) and \(s(a)(s(b)s(c))\), using \(s(a)s(b)=s(ab)+D(a,b)\). The first gives \(s(abc)+D(ab,c)+D(a,b)c\), and the second gives \(s(abc)+D(a,bc)+aD(b,c)\). Their equality is the Hochschild cocycle equation
\[
 aD(b,c)-D(ab,c)+D(a,bc)-D(a,b)c=0.
\]
With only the two prescribed maps held fixed, adding any linear \(t:A\to I\) with \(t(1)=0\) preserves both constraints, and every other unital linear lift of both maps arises this way. Its defect changes by \(at(b)-t(ab)+t(a)b\). Thus an action-preserving algebra lift exists precisely when \([D]\) vanishes in the second Hochschild cohomology \(HH^2(A,I)\), the group of normalized cocycles modulo these changes. A linear residue functional on the cocycles descends to this cohomology group exactly when it vanishes on every coboundary.

One can test all changes of generator at once for a truncated polynomial algebra. Let \(R=k[h]/(h^n)\), \(n\ge1\), and let \(G(T)\) be monic of degree \(m\ge2\) with \(G(T)\equiv T^m\bmod h\). A unital \(R\)-algebra map
\[
 R[X]/(X^m)\longrightarrow R[x]/(G(x))
\]
reducing to \(X\mapsto x\) exists exactly when \(G(T)=(T-c)^m\) for some \(c\in hR\). To see necessity, use \(1,X,\ldots,X^{m-1}\) and \(1,x,\ldots,x^{m-1}\) as bases over \(R\). The matrix of such a map reduces to the identity modulo \(h\), hence is invertible. Multiplication by \(x\) on the target has characteristic polynomial \(G\). Transport \(x\) to the source and call its constant coefficient \(c\), necessarily in \(hR\). On each successive quotient \((X^i)/(X^{i+1})\) it acts by \(c\), giving characteristic polynomial \((T-c)^m\). Conversely, when \(G=(T-c)^m\), the choice \(X\mapsto x-c\) gives a lift.

For instance, take \(m=2\) and \(G(T)=T^2-hT\) over \(\mathbb Q\). The linear coefficient forces \(c=h/2\). The constant term of \((T-c)^2\) is \(h^2/4\), so the lift works modulo \(h^2\) and fails modulo \(h^3\) for *every* possible change of generator. More generally let \(G(T)=T^m-h^sT^{m-1}\), with \(s\ge1\). Comparing the coefficient of \(T^{m-1}\) gives \(mc=h^s\). If the characteristic divides \(m\), this first fails modulo \(h^{s+1}\). If \(m\) is invertible, let \(e\) be the first \(j\ge2\) with \(\binom mj\ne0\) in \(k\). All the remaining coefficients agree precisely when \(h^{se}=0\). In characteristic zero \(e=2\). In characteristic two with \(m=5,s=1\), the identity \((1+T)^5=1+T+T^4+T^5\) gives a lift modulo \(h^4\) and excludes one modulo \(h^5\).

For a deformation of the ordered bar differential, the coefficient of \(h^i\) is an entire coderivation, which can act in several word lengths. Write \(b(h)=b^{(0)}+\sum_{i\ge1}h^i b^{(i)}\), with \(|h|=0\) and \(|b^{(i)}|=1\). In the graded commutator \([P,Q]=PQ-(-1)^{|P||Q|}QP\), the equation \(b(h)^2=0\) at order \(N\ge1\) reads
\[
 [b^{(0)},b^{(N)}]=-\sum_{i=1}^{N-1} b^{(i)} b^{(N-i)}.
\]
The obstruction on the right has degree two. If the lower equations hold, it is closed for \([b^{(0)},-]\), since the truncated differential commutes with its square. A lift needs a degree-one primitive satisfying the translation, vacuum, cut, collision and support conditions on the ordered configurations.

For a comparison with a prescribed module action, the source algebra, target algebra and state module are the three types of inputs and outputs. The comparison map and the action on the state module are operations of this coloured diagram. Fixing the observation up to a specified homotopy calls for the homotopy fibre of the restriction map. A surjective map of deformation dg Lie algebras with the corresponding fibration on the filtered layers computes this fibre by its kernel. In a characteristic-zero model with higher brackets, the ternary bracket of the first variation \(\gamma_1\) contributes \(\ell_3(\gamma_1,\gamma_1,\gamma_1)/6\) to the third-order curvature. Compatible primitives yield a formal comparison when the relative complex controls the stated diagram, its insertions converge and its filtration is complete, separated and pronilpotent.

## The support remembers which cuts were allowed {#ch05-the-support-remembers-which-cuts-were-allowed}

At \((x,y,x)\), with \(x\ne y\), the two consecutive cuts of a three-letter word both fail. Away from the common failure locus, however, a coalgebra may give exactly the information in the two separated blocks. The map to test is its coproduct on that cut.

**Definition (factorization across consecutive cuts).** A connected coaugmented coalgebra \(C\) factorizes across consecutive cuts if, for every \(0<p<n\), its cut coproduct on \(U_{p,n-p}\)
\[
C_n|_{U_{p,n-p}}\longrightarrow
(C_p\boxtimes^{\mathbf L}C_{n-p})|_{U_{p,n-p}}
\]
is an equivalence.

**Definition (associative chiral algebra on words).** This is an augmented \(E_1\)-algebra \(A\) for consecutive-cut convolution, with \(A_0\simeq k\), whose bar coalgebra \(BA\) factorizes across consecutive cuts. Here \(E_1\) retains the multiplication with all its associativity homotopies. Its augmentation ideal has zero empty coefficient.

Which positive-arity coefficients can this ideal have? On each cut open the coproduct must split the bar coalgebra into two independent coefficients. Let \(Z_n\) be the locus where *no* consecutive cut is available,
\[
Z_n=X^n\setminus\bigcup_{p=1}^{n-1}U_{p,n-p},
\qquad Z_1=X.
\]
For a complex \(F\), derived sections supported on \(Z\), denoted \(R\Gamma_ZF\), form the fibre of the restriction map \(F\to Rj_*j^*F\) to the complementary open set. In arity two there is just one cut. Its separating open is \(U_{1,1}=X^2\setminus\Delta_{12}\), and its closed support locus is \(Z_2=\Delta_{12}\). A factorizing coproduct identifies the two-letter term with the localization of \(C_2\) off that diagonal. Thus the comparison with the one-letter term is the familiar map \(C_2\to Rj_*j^*C_2\).

**Support theorem.** Consecutive-cut duality restricts to an equivalence between connected factorizing coalgebras and connected algebras whose positive-arity coefficients vanish on every cut open. For a connected factorizing coalgebra \(C\) and \(n\ge1\),
\[
\overline{\Omega C}_n\simeq R\Gamma_{Z_n}(C_n)[-1].
\]

*Proof.* Start with two letters. The one-block cobar term is shifted by \([-1]\) and the two-block term by \([-2]\). Factorization identifies their arrow before shifts with \(C_2\to Rj_*j^*C_2\). Its fibre shifted by \([-1]\) is the binary reduced cobar coefficient. With \(n\) letters choose a subset of the \(n-1\) gaps. If it has \(r-1\) members it cuts out \(r\) blocks. The cobar shift is \([-r]\), one lower than the shift \([-(r-1)]\) in the localization cube. On the intersection of these cut opens the iterated coproduct identifies the coefficient with the external product of the \(r\) block coefficients. Coassociativity makes these identifications commute with adding a cut. The total fibre of the localization cube computes sections supported off the union of the opens. Comparing the shifts at each vertex gives the cobar coefficient an additional shift \([-1]\).

Conversely, assume the positive algebra coefficients vanish on the cut opens. Fix one cut and restrict the bar to its open. A bar factor straddling the cut has zero coefficient, since that factor itself admits the cut. Every surviving term therefore has a separator at the chosen gap. A multiplication face that removes this separator has zero target. Each remaining face, including a higher multiplication face, acts wholly to its left or wholly to its right. Splitting at the separator identifies the two complexes in the definition above. ∎

The same argument applies to word coefficients in unbounded right differential modules with quasi-coherent underlying modules on a smooth separated finite-type scheme of positive pure dimension over the characteristic-zero field \(k\). Extraordinary pullback of an open direct image localizes on the inverse-image open, which gives compatibility with monotone collisions.

For three labels, the cut \(1|23\) fails when \(x_1=x_2\) or \(x_1=x_3\). The cut \(12|3\) fails when \(x_3=x_1\) or \(x_3=x_2\). If both cuts fail, either the first and third points agree or all three do. Thus, writing \(\Delta_{ij}=\{x_i=x_j\}\),
\[
Z_3=(\Delta_{12}\cup\Delta_{13})
\cap(\Delta_{13}\cup\Delta_{23})=\Delta_{13}.
\]
At \((x,y,x)\) with \(x\ne y\), both cuts fail. The following two coalgebras show why this determines a support bound and why the actual support can be smaller. On an equality stratum \(i:S\hookrightarrow X^n\) inside \(Z_n\), localization gives \(i^!\overline{\Omega C}_n\simeq i^!C_n[-1]\). The dualizing coalgebra \(J_n=\omega_{X^n}[n]\) on the curve, with \(J_0=k\), attains the whole bound. Its cut coproducts come from external products on the cut opens, and its extraordinary fibres are nonzero throughout \(Z_n\).

On \(X=\mathbb A^1\), take the square-zero algebra with \(A_0=k\) and \(\bar A_n=\Delta_{n,*}\omega_X\), where \(\Delta_n(x)=(x,\ldots,x)\). For a repetition \(d:X^m\hookrightarrow X^n\) we have \(\Delta_n=d\circ\Delta_m\). Its coefficient is already carried by the image of \(d\), so \(d^!\Delta_{n,*}\omega_X\simeq\Delta_{m,*}\omega_X\) by the [diagonal pullback calculation](04-factorization.md#ordered-cut-geometry). This gives the monotone collision identifications. On a cut open every surviving bar word has a separator at that cut, so \(BA\) factorizes. Its reduced ternary cobar coefficient is \(\bar A_3\), supported on the small diagonal.

At four labels, the single equality \(x_1=x_4\) crosses every cut. The two equalities \(x_1=x_3,\ x_2=x_4\) also cross all three cuts, and removing either one loses an end cut. These are the two components of \(Z_4\). On a curve \(\Delta_{14}\) has codimension one and \(\Delta_{13}\cap\Delta_{24}\) has codimension two. Thus a common failure locus of cuts can already have components of different dimensions.

To count components in general, let \(X\) be a separated geometrically integral variety of dimension \(d>0\). A partition diagonal \(D_\pi\) imposes equality within each block. It is isomorphic to \(X^{|\pi|}\) and distinct block values form a dense open in it. The components are therefore indexed by the partitions that cross every cut and lose this property under every proper refinement. If a block contained an interior label as well as its two extreme labels, we could split off that interior label without losing a single cut. Minimality therefore forces each nonsingleton block to be a pair. The intervals of gaps covered by the pairs \((a_i,b_i)\), listed by left endpoint, must cover every gap, with a private gap for each interval. This forces \(a_1=1,\ b_r=n\), with internal endpoints in the order \(a_2,b_1,a_3,b_2,\ldots,a_r,b_{r-1}\). Conversely each such choice covers every gap and gives every pair a gap covered by that pair alone. Choosing the \(2r-2\) internal endpoints among \(2,\ldots,n-1\) now determines all \(r\) pairs. Thus \(Z_1=X\), and for \(n\ge2\) there are \(\binom{n-2}{2r-2}\) components of codimension \(dr\) for \(1\le r\le\lfloor n/2\rfloor\). The total is one at \(n=2\) and \(2^{n-3}\) at \(n\ge3\).

For any finite family of cuts, a partition crossing them all is minimal precisely when every bipartition of each block is induced by a cut that leaves all its other blocks intact. Indeed that cut is lost on splitting the block. For a tree whose vertices are the labels, deleting an edge gives a cut into the two connected components. For any two edges, the sides facing away from each other are disjoint. A block of four or more labels would require cuts inducing both \(12|34\) and \(13|24\) on four of its labels. Each side of the first meets each side of the second. No two tree edges can do this, so every nonsingleton block is a pair or a triple. A pair crosses precisely the edges on its path, and a triple crosses the edges of its spanning subtree. Together these paths and subtrees must cover the tree. A pair needs a private edge on its path, and a triple needs one on each arm from the common meeting point of its three paths. The tree with edges \(12,13,14,25\) has one triple \(345\) and five two-pair components, all of codimension \(2d\). On a star with \(m\) leaves there are \(a\) leaf pairs, \(b\) leaf triples and \(e\in\{0,1\}\) centre–leaf pairs. Each type with \(2a+3b+e=m\) gives \(m!/(2^a6^b a!b!)\) components of codimension \(d(a+2b+e)\). For any cut family, start with the discrete partition. For each cut in turn adjoin one equality across it in every possible way and retain the refinement-minimal results. This recursion distributes intersection with the next failure locus over the preceding component diagonals.

The two components at four labels meet at the small diagonal. To take sections with support in their union, map the sections supported on their intersection to the direct sum of the two component complexes. The two inclusions have opposite signs. Mayer–Vietoris identifies the cofiber of this map with \(R\Gamma_{Z_4}F\). For \(F=C_4\), the extra shift \([-1]\) in the support theorem makes the *fibre* of the same map the reduced cobar coefficient.

For any \(n\), assume a stable coefficient theory with coherent support inclusions and Mayer–Vietoris. Intersecting component diagonals imposes all the equalities of their partitions, hence gives the diagonal of their join. Let \(J\) be the set of distinct joins of nonempty sets of component partitions, ordered from coarser to finer. Then
\[
R\Gamma_{Z_n}F\simeq\operatorname*{hocolim}_{\rho\in J}R\Gamma_{D_\rho}F.
\]
Indeed iterated Mayer–Vietoris uses all nonempty subsets of components, ordered by reverse inclusion. For a given join \(\rho\), the subsets whose joins receive an arrow from \(\rho\) are exactly the nonempty subsets of component partitions refining \(\rho\). The set of all such components is initial among them. This proves cofinality and permits each distinct intersection to be indexed by its partition.

### From support to fields {#ch05-from-support-to-fields}

Knowing the supported complex does not yet say how two sections multiply. For cobar words one must also use the inverse factorization maps to join coefficients over a separating open. The unit for that multiplication lies at the empty configuration. To put the vacuum at a point on the curve takes another datum. A **vacuum marking** identifies the singleton coefficient \(A_{\{1\}}\) with \(\omega_X\otimes_{\mathcal O_X}G\) for a left differential module \(G\) and specifies a horizontal map \(\mathcal O_X\to G\). A **vacuum framing** also compares the configuration operations with simultaneous field products, preserving substitutions, translation and the vacuum.

The same definition of an associative chiral algebra can be used with the symmetric convolution on the full ordered collision atlas. There, factorization requires each specified coproduct component to be an equivalence. Its support consequence differs from the cut theorem. If \(C=BA\) and \(U\) is the two-point distinct locus, put \(V=(C_{\{1\}}\boxtimes C_{\{1\}})|_U\). Componentwise factorization gives
\[
\overline A_{\{1,2\}}|_U\simeq V[-2].
\]
Indeed the binary cobar differential uses a map \(C_{\{1,2\}}|_U\to V\oplus V\), one component for each order. Both components are equivalences, so after either identification this is the graph of an isomorphism. Its cofiber is a copy of \(V\), in the two-block term shifted by \([-2]\). Thus a nonzero separated coefficient survives on the atlas. Small-diagonal support there is characterized by a different, joint word-factorization condition comparing the full direct sum of ordered word terms.

Two different units occur already on these coefficients. For convolution the coaugmentation is a map from \(k\) at the empty configuration. For the coefficientwise extraordinary tensor the unit has \(n\)-point coefficient \(\omega_{X^n}[n]\) on a curve. A map from this second system to a coalgebra, with its compatible insertions, specifies what happens when a vacuum occupies a position. For the current \(J\) at scalar level \(k_0\ne0\), the first product satisfies \(J_{(1)}J=k_0\mathbf1\). A unital map of field algebras to the scalar field algebra would send its left side to zero and its right side to \(k_0\). Projection to the vacuum coefficient is a linear functional. Preservation of field products is a stronger condition that fails on this pair.

The occupied vacuum is needed to recover fields from configuration coefficients. Over a characteristic-zero field \(k\), field recognition on \(X=\mathbb A^1_k\) uses an \(E_1\)-coalgebra for the chiral tensor on the full Ran space, with one \(X^I\) for each nonempty finite label set \(I\). Its coefficients \(C_I=L_I[|I|]\) are shifts of ordinary right differential modules. All surjections carry coherent extraordinary collision isomorphisms, and every ordered bipartition gives a coproduct equivalence on the open where its blocks are disjoint. A nonzero occupied vacuum has insertion maps for every subset. They compose, respect relabelling and factorization, and retract to the identity under any collision that retains one label in each fibre. The translation data include an operator \(D\) on the global one-point sections \(\Gamma(L_1)\). It obeys \(D(fa)=f'a+fD(a)\) for scalar polynomials \(f\), commutes with the constant vector-field action, is locally nilpotent and kills the vacuum. Simultaneous translation must preserve the image of every \(L_n\) in the separated standard-order trivialization.

These objects are equivalent to quantum vertex algebras with nonzero vacuum whose exchange \(\mathcal S(u)\) and its inverse have finite Laurent expressions on each state tensor. To recover the states, take a global one-point section \(v\) and set
\[
 P(v)=\sum_{j\ge0}\frac{(-z)^j}{j!}\,D^jv .
\]
For a horizontal section \(a\), so \(Da=0\), the formula gives \(P(za)=za-zD(za)=0\) and \(P(a)=a\). Thus it selects the constant coefficient of a linear polynomial in \(z\). For a general section the sum is finite by local nilpotence. When \(D\) differentiates the \(j\)-th power of \(-z\), the resulting term cancels the term in which \(D\) hits \(D^{j-1}v\). Hence \(P(v)\) belongs to \(V=\ker D\).

To reconstruct \(v\), form \(\sum_{j\ge0} z^jP(D^jv)/j!\). After inserting the definition of \(P\), the coefficient of \(z^mD^mv\) is \(\sum_{j=0}^m(-1)^{m-j}/(j!(m-j)!)\). This is one at \(m=0\) and zero for \(m>0\), by the binomial theorem. Conversely, differentiating a polynomial relation among horizontal sections sufficiently many times gives its top coefficient times a nonzero factorial. These two calculations identify \(\Gamma(L_1)=k[z]\otimes V\). The right action of the constant vector field gives the state translation \(Ta=-a\partial_z\) on \(V\).

Once the state space is known, the binary lattice specifies which sections in the separated two-point localization extend. For \(u=z_1-z_2\), this submodule \(L_2\) is the kernel of the full principal-part map \(\alpha:j_*j^*(L_1\boxtimes L_1)\to\Delta_*L_1\), where \(j\) omits the diagonal. In the density frame, \(a_{(m)}b=[u^{-1}]\alpha(u^m;a,b)\) recovers every mode. For \(m=-1\), multiplying the field by \(u^{-1}\) makes its regular constant coefficient a simple pole. The same extraction after multiplication by \(u^m\) gives the coefficient of \(u^{-m-1}\) in the field. Comparing the two ordered binary coproducts gives \(\mathcal S_{21}(-u)=\mathcal S(u)^{-1}\). Agreement of successive adjacent collisions gives weak associativity. The three collision channels give locality with a clearing power independent of the spectator, and passing a field across a collision gives the exchange hexagon. Between existing such objects, unary isomorphisms preserving translation, vacuum, binary lattice, boundary and exchange extend uniquely.

The equivalence also holds over a commutative local Artinian \(k\)-algebra with residue field \(k\), with flat \(L_I\) on the geometric side, a flat state module and a vacuum spanning a free direct summand on the field side. For compatible systems over \(k[\hbar]/(\hbar^N)\), the Laurent bounds may depend on \(N\) and on the input. A separate recognition theorem starts with the contact and finite-Laurent exchange on a fixed free even state frame at each precision. It requires a translation-invariant differential-module contact with the two vacuum principal parts, exchange fixing the vacuum slots and congruent to the identity modulo \(\hbar\), the shift, unitarity and Yang–Baxter identities, the contact hexagon on independent outputs and the signed three-channel identity with all normal derivatives. With compatible reductions the same moments recover an exact Etingof–Kazhdan quantum vertex algebra.

Can the two-point field alone supply the missing exchange? Return to the word \((x,y,x)\), with \(y\ne x\). Neither consecutive cut is available there. Take the family of cut coalgebras indexed by \(c\in k^\times\) with common state algebra \(B=k[\epsilon]/(\epsilon^2)\), zero translation and constant binary field \(Y(a,u)b=ab\). In the given three-point coefficient, consider simple poles along \(z_1=z_3\) while the middle point stays away. Their allowed numerators form the kernel of a map \(q^c_{13}:B^{\otimes3}\to B^{\otimes2}\) identifying the two outside positions. The consecutive-cut coproducts place no separation condition at this configuration. Put the vacuum \(1\) in one outside slot and then in the other. The two evaluations are
\[
\begin{aligned}
 q^c_{13}(\epsilon\otimes\epsilon\otimes1)&=\epsilon\otimes\epsilon,\\
 q^c_{13}(1\otimes\epsilon\otimes\epsilon)&=c\,\epsilon\otimes\epsilon .
\end{aligned}
\]
In the binary coefficient \(1\otimes\epsilon-\epsilon\otimes1\) is an allowed pole numerator because its product is zero. Move the middle \(\epsilon\) past the first input of this binary relation. The crossing fixes the vacuum slot. Write \(v\in B^{\otimes2}\) for its value on \(\epsilon\otimes\epsilon\). The crossed numerator is \(1\otimes\epsilon\otimes\epsilon-v\otimes1\). The second evaluation above gives \(c\,\epsilon\otimes\epsilon\) on the first term, while \(q^c_{13}(v\otimes1)=v\). Thus the numerator lies in \(\ker q^c_{13}\) exactly when \(v=c\,\epsilon\otimes\epsilon\). The opposite convention gives \(c^{-1}\). Unitarity of a full exchange would force \(c=c^{-1}\). Thus \(c=2\) gives a cut coalgebra with the same binary field as \(c=1\) and no such full exchange. Both \(c=1\) and \(c=-1\) extend in every arity in this family. More general cut lattices can agree with the constant-exchange field object through any prescribed arity and first fail at a later collision.

One can also transpose the geometric bar. For bounded holonomic coefficients, Verdier duality sends the cut coproduct with \(j_*\)-extension to multiplication with \(j_!\)-extension, and sends extraordinary collision pullbacks to ordinary ones. It therefore produces an algebra in the category with the dual transition maps. A pointwise cochain dual paired with the occupied vacuum instead has multiplication formed with \(j_*\). The comparison between those open extensions has the normal links calculated in [Chapter 4](04-factorization.md#ch04-normal-link) when its own open and coefficients agree with that fully distinct Betti problem. The input of a word cut can allow collisions inside each block. Its comparison requires the link for that open.

## Rational exchange on all finite collision diagrams {#ch05-rational-exchange-diagram}

To identify labels \(1,3\) while \(2\) remains separate, one must bring the outside fields past the middle one. The cut example shows why this exchange has to be supplied. Work over a commutative \(k\)-algebra \(R\), with \(k\) a characteristic-zero field, and on the affine line \(U\) with finitely many \(k\)-rational points removed. Take an ordinary flat \(R\)-module of states \(V\), a vacuum spanning a free direct summand and a translation \(T\). Write \(Y(a,u)b\) for the lower-truncated field obtained by inserting \(a\) at displacement \(u\) from \(b\). Assume the vacuum, translation and weak associativity identities.

Suppose the exchange \(\mathcal S(z)\) and its inverse have finite Laurent expressions on each state tensor. They fix the vacuum slots and obey translation, unitarity, Yang–Baxter, field locality and the exchange hexagon. The hexagon identifies the two ways of moving a spectator past a product. These hypotheses hold over \(R\) itself in the theorem, so identities must also hold on coefficients killed by reduction to its residue fields.

Assign a coordinate \(z_B\) to every block \(B\) of a partition of a finite label set \(I\). On the locus of distinct block positions take their external field coefficients, invert all differences \(z_B-z_{B'}\) between blocks, and push forward along the partition diagonal. This retains every finite derivative of the delta section in the normal directions. These are the **Cousin coefficients**. For instance the summand indexed by \(13|2\) has two distinct block positions, the first representing both labels 1 and 3. A spectator can cross one of those labels before they coincide.

In the associative cobar a word groups the blocks into successive nonempty factors. Its differential splits one factor or merges two blocks inside it. Put \(X_{ab}=\mathcal S_{ba}(z_b-z_a)\) on fixed labelled slots. For an unsplit two-block factor with coefficient \(x\), its boundary in the two orders and on the merged support is
\[
 x[a][b]-(X_{ab}x)[b][a]-(r^\circ_{ab}x)[m] .
\]
The label \(m\) records the position kept when \(a\) and \(b\) merge. At that position \(r^\circ_{ab}\) takes the whole polar part of the multiplier times the field product \(Y(a,z_a-z_b)b\). The multiplier may depend on a spectator, so it must first be expanded about the surviving position. For instance a multiplier \(1/(d+u)\), with \(d\) a nonzero spectator difference and \(u\) the collision coordinate, turns a double pole into
\[
 \frac{1}{u^2(d+u)}=\frac{1}{d\,u^2}-\frac{1}{d^2u}+O(1).
\]
The leading coefficient \(1/d\) multiplies the double pole. The first derivative of the spectator multiplier contributes \(-1/d^2\) to the simple pole. Dropping the spectator before forming the principal part would miss this term. Moving the surviving position transfers the entire normal distribution with its orientation.

The **Spencer complex** adjoins an exterior tangent vector \(e_i\) of degree \(-1\) at each label. Its differential contracts tangent factors with the covariant derivatives, which on the block coefficient are \(\nabla_B=\partial_{z_B}+T_B\). Denote by \(K(I)\) the total complex including the word differential. A surjection \(\alpha:I\twoheadrightarrow J\) gives a map \(K(J)\to K(I)\). It inserts the supported coefficient on the repeated labels and sends
\[
 e_j\longmapsto\sum_{\alpha(i)=j}e_i .
\]
For example repeating a block \(13\) sends its tangent to \(e_1+e_3\), the derivative for moving both labels together. Ordering the quotient labels by their largest preimages determines which adjacent exchanges to apply **inside each word factor**. Taking a maximum in two stages agrees with taking it once. Unitarity and Yang–Baxter identify different presentations of the same order change. The exchange hexagon and the re-rooting identity for the full principal part make these transitions chain maps. Concatenation of two words, followed by localization at all differences between their blocks, gives an associative external multiplication compatible with the support maps. The empty set carries its own scalar \(R\).

For the interlaced partition \(13|24\), first multiply at the two block positions and then repeat each position. On the exterior tangent \(e_a\wedge e_b\) this gives
\[
 (e_1+e_3)\wedge(e_2+e_4).
\]
Doing the two repetitions first and then multiplying gives the same wedge. In either order the term \(e_3\wedge e_2\) has a minus sign when written with increasing indices. There is also a mixed term on ordinary coefficients. Put \(u=z_1-z_3,\ h=z_2-z_4,\ d=z_3-z_4\). The multiplier \(1/(z_1-z_2)\) becomes \(1/(d+u-h)\). The two block positions are separate, so \(d\) is invertible. Both \(u^2\) and \(h^2\) annihilate \([u^{-2}][h^{-2}]\). Thus the quadratic Taylor term \((u-h)^2/d^3\) contributes only \(-2uh/d^3\), and all higher terms vanish on this input. We can also expand first in \(u\). Its linear coefficient is \(-1/(d-h)^2\), whose term linear in \(h\) is \(-2h/d^3\). Both orders therefore give \(-2d^{-3}[u^{-1}][h^{-1}]\) as the mixed contribution. At any fixed normal order only finitely many Taylor terms survive.

Exchange itself can be detected over the original ring. Take the polynomial current \(J\) with Wick contraction \(P(d)=\kappa d^{-2}+\lambda d^{-1}\) over \(k[\kappa,\lambda]\). On the primary oscillator polynomials the order change is the finite exponential of \((2\lambda/d)\partial_J\otimes\partial_J\), with \(d=z_a-z_b\). In particular
\[
 X_{ab}(J^2\otimes J^2)=J^2\otimes J^2+
 \frac{8\lambda}{d}J\otimes J+
 \frac{8\lambda^2}{d^2}\mathbf1\otimes\mathbf1 .
\]
Identifying labels 1 and 3 while 2 stays separate changes the root order on the two-block factor. Crossing before the identification or using the induced order afterwards gives this same operator, together with the orientation sign on the factor. At \(\kappa=0,\lambda=\epsilon\), \(\epsilon^2=0\), its first correction survives. Passing to the residue field sets this coefficient of \(J\otimes J\) to zero. Thus exchange has to be checked over \(R\) itself.

After one identifies configurations along all surjections, which degree-zero operations on an open curve remain? Denote by \(\mathsf M_U(V)\) the intrinsic all-arity mode algebra. Its generators are rational multipoint field coefficients. Take the quotient by translation derivatives and the relations \(x-\sigma_i x-\rho_i x\) in every arity with arbitrary spectators. Here \(\sigma_i\) exchanges and relabels two neighbouring inputs, and \(\rho_i\) takes the supported simple residue after the full Taylor transfer to the surviving root.

Use chains of nonidentity surjections of nonempty finite label sets, with \(R\) on the empty set adjoined separately. For the single arrow \(J\xleftarrow{\alpha} I\), a coefficient \(y\in K(J)\) appears one degree lower. Its two faces give \(K(\alpha)y\) at \(I\) minus \(y\) at \(J\), and the internal differential on this shifted summand is \(-d_K\). In length \(p\), an interior face composes two successive surjections and the internal differential is \((-1)^p d_K\).

**Theorem (the algebraic collision integral).** Form \(G_U(V)\) by taking an algebraic direct sum over chains of surjections, placing a chain of length \(p\) in simplicial degree \(-p\), with the usual alternating face maps on the \(K(I)\). Shuffling two chains and concatenating their coefficient words makes \(G_U(V)\) a unital dg algebra over \(R\). Its degree-zero cohomology is the intrinsic all-arity mode algebra \(\mathsf M_U(V)\).

To see how a field relation becomes a boundary, insert a configuration cochain as a word of singleton factors by \(\phi\), and let \(\widehat\sigma_i,\widehat\rho_i\) act also on its exterior tangents. For each adjacent pair there is a degree-minus-one homotopy
\[
 dh_i+h_id=\phi(1-\widehat\sigma_i-\widehat\rho_i).
\]
The boundary of the unsplit double factor gives an ordered product, its exchanged product, and the full principal part on the common support. A normal contraction replaces that last term by the pushed-forward simple residue. The transposition and collision edges in the surjection diagram supply the changes of representative, giving the displayed homotopy on the whole Spencer complex. This argument uses the Taylor expansion of every spectator multiplier, including the \(-d^{-2}\) term just computed.

Conversely a boundary reaching degree zero starts in degree minus one. It can come from one tangent, one double factor or one diagram edge. These impose, respectively, a translation relation, an exchange with residue, or identification of a coefficient with its image under a surjection. Passing to the quotient by the Spencer derivatives first removes the higher normal derivatives. Each remaining singleton word is the support image of the standard word with its blocks listed in that order. This listing gives the inverse to the map from the stated mode quotient.

The filtration by the number of labels also determines the additive complex. Write
\[
 \mathcal D_r=\mathcal O(\operatorname{Conf}_r U)\otimes_k
 V^{\otimes_R r}\otimes_R\Lambda^\bullet R^r
\]
with its Spencer differential and the exchange action of \(\Sigma_r\), including its permutation of tangents. In cardinality \(r\), all proper collision partitions already enter from a smaller set. On the discrete partition the complex of orders and their consecutive groupings is the cellular complex of a permutohedron, a contractible polytope whose vertices are the orders. The resulting layer is \((\mathcal D_r)_{\Sigma_r}\), the coinvariants for the indicated exchange action.

The separate cardinality layers do not yet give a splitting of the complex. Consider two singleton blocks on \(U=\mathbb G_m\). Over \(k=\mathbb Q\) take the constant field algebra \(k\mathbf1\oplus ka\) with \(a^2=0\), \(T=0\), and \(a\) in cohomological degree zero. The exchange fixes vacuum slots and sends \(a\otimes a\) to \(-a\otimes a\). For \(x=(z_1z_2)^{-1}a\otimes a\) the merged field vanishes. The unsplit double factor therefore has boundary \(x[1][2]+x[2][1]\) in the original word coordinates. Express the second coefficient in the order \(1,2\). The exchange sends it to \(-x\), so a single field coefficient \(x\) now multiplies the scalar commutator \([1][2]-[2][1]\).

Return to the given \(U,R,V\). For any partition \(\pi\), order its blocks by their largest labels and call this order \(\omega\). A word \(w=(J_1,\ldots,J_q)\) groups those blocks into successive factors. Read each \(J_l\) internally in the order \(\omega\) and concatenate the lists to obtain \(\gamma_w\). Write \(\tau_{\nu,\gamma}\) for transport from order \(\gamma\) to order \(\nu\) by adjacent exchanges. On the coefficient of \(w\) apply \(P_w=\tau_{\omega,\gamma_w}\), leaving its determinant lines fixed. In this common order the summand at \(\pi\) has the form \(C_\pi\otimes_k E_\pi\). Here \(C_\pi\) is the entire supported Cousin coefficient with its Spencer tangents. It includes poles between distinct blocks in different word factors and all finite normal derivatives. The scalar complex \(E_\pi\) has one word line for each ordered grouping. A group \(J\) contributes the letter \(t\det J\), its top exterior line \(\bigwedge^{|J|}k^J\) placed in degree \(1-|J|\). Each block occurs once in the word.

Give the scalar tensor algebra on these letters the unshuffle coproduct. It sends a letter \(\ell\) to \(1\otimes\ell+\ell\otimes1\) and extends multiplicatively with the graded tensor sign. An element with this two-term coproduct is called primitive. In particular the mixed terms cancel on the graded commutator of two primitive letters. After transport, splitting a group leaves \(C_\pi\) fixed. The two orders of each split combine to give precisely such a commutator in \(E_\pi\).

A merger also acts on the field coefficient. For example, put the three singleton blocks in the word \((\{1,3\},\{2\})\). In order \(1,2,3\), bringing \(1\) to \(3\) crosses the spectator \(2\) before taking the full principal part. In order \(1,3,2\) the merging pair is adjacent, but the merged field must then cross \(2\) to reach the output order \(2,3\). The exchange hexagon identifies the two calculations, including the Taylor transfer of the spectator multiplier. In general, merging \(i<j\) within a factor keeps \(j\) and deletes \(i\) from both orders. If \(w'\) is the resulting word, its coefficient map satisfies
\[
 P_{w'}\,r^{\mathrm{raw}}_{ij,w}\,P_w^{-1}=r^\omega_{ij}.
\]
The right side depends on the ordered blocks and the pair, so every word that allows this merger has the same coefficient map. Its scalar partner acts on a letter containing both blocks by minus contraction of its determinant with the covector dual to \(i\). It kills every other letter and extends to words by the graded Leibniz rule.

For a surjection \(\alpha:I\twoheadrightarrow J\), relabel the incoming blocks by their inverse images and include their supported coefficient. In the common orders, the two grouped orders cancel from the state transport. What remains is \(\tau_{\omega_{\rm out},\alpha^*\omega_{\rm in}}\) for every word, with the induced relabelling on determinant lines. For example, if \(1,3\) map to \(A\) and \(2\) to \(B\), the fibre maxima order the output blocks as \(B,A\). An input ordered \(A,B\) requires one exchange, and its tangent \(e_A\) goes to \(e_1+e_3\). For an adjacent transposition the action on \(\mathcal D_r\) is the state exchange \(X_{i,i+1}\) followed by relabelling the positions and their tangents.

Since \(k\) has characteristic zero, the Eulerian idempotent \(e^{(n)}\) on the scalar tensor algebra projects to symmetric degree \(n\) in its primitives. For endomorphisms \(f,g\), their convolution \(f\star g\) applies the unshuffle, applies \(f\) and \(g\) to the two subwords and concatenates the results. Then \(e^{(1)}=\log^\star(\mathrm{id})\), with the projection to the empty word as convolution unit, and \(e^{(n)}=(e^{(1)})^{\star n}/n!\) for \(n\ge1\). The logarithm is finite on each word. The scalar split and each signed merger are derivations taking primitive letters to primitives. They are therefore also coderivations of the unshuffle, so they commute with the Eulerian projectors. Relabelling the letters commutes with them as well. Thus \(1_{C_\pi}\otimes e^{(n)}\) respects the differential and the support maps in the common order. In the original word coordinates its action is \(P^{-1}(1_{C_\pi}\otimes e^{(n)})P\), where \(P\) applies \(P_w\) separately on each word.

On the discrete partition the permutohedral augmentation sends every singleton word to \(1\). To see its Eulerian degree, send the \(r\) singleton letters to distinct commuting variables and all larger letters to zero. Every singleton word maps to the same monomial, the product of the \(r\) variables, of symmetric degree \(r\). The permutohedron is contractible, so only \(e^{(r)}\) contributes to this layer. Averaging over \(\Sigma_r\) gives ordinary coinvariants for the exchange and tangent action above. Each projector has only one possibly nonzero layer. Taking the exact filtered union gives the additive splitting
\[
 G_U(V)\simeq R\oplus\bigoplus_{r\ge1}(\mathcal D_r)_{\Sigma_r}
 \qquad\text{as complexes}.
\]
The cardinality spectral sequence consequently degenerates on its first page. Multiplication in \(G_U(V)\) still contains the lower-cardinality residue term \(\rho_i x\) from the unsplit double factor.

Return to the constant square-zero field. In the surviving cardinality-one layer, the residue of \(dz/z\) detects the unary mode \(A=[z^{-1};a]\). Thus \(A\ne0\) in degree zero. In the mode algebra the two relabelled terms of the double-factor boundary both represent \(A^2\), giving \(2A^2=0\). An ordinary multiplicative coproduct declaring the even mode \(A\) primitive would send this zero square to \(2A\otimes A\ne0\). The scalar unshuffle used above acts on the determinant letters of \(E_\pi\). Its transported projectors give endomorphisms of the additive complex.

The chain map from multipoint coefficients and their relation homotopies to \(G_U(V)\) induces the identity on \(\mathsf M_U(V)\) in degree zero by the boundary and listing argument above. A comparison in negative degrees with an independent derived algebra of modes or a global geometric pushforward requires a map to that object. [Integration and field reconstruction](13-geometric-reconstruction.md#ch13-integrating-the-collision-diagram)

A mode algebra can act on many representations. Fix an affine current representation \(W\) used for induction. Given a second representation \(M\), maps out of \(W\) detect those states that can occur as images of its generators. On derived maps from \(W\) into \(M\), precomposition is a right action of the derived endomorphism algebra of \(W\). Write \(B\) for its graded opposite, so this is a left \(B\)-module. Tensoring back with \(W\) over \(B\) gives an evaluation map to \(M\). In the tensor–Hom adjunction this is the counit. In the other order the unit starts from a \(B\)-module, tensors with \(W\), and maps the module into the derived maps from \(W\) to the result.

Even for a single symmetry, the choice of \(W\) affects what evaluation can reach. If an involution acts trivially on \(W\), every equivariant map \(W\to M\) has image in the fixed subspace of \(M\). Which part of a current representation can be recovered when \(W\) is induced from its positive modes? [The two comparison maps](06-duality-and-induction.md#adjunction-comparison-maps)
