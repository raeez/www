# Bar constructions and coherent operations

When three local fields are combined, there are two successive operations: combine the first two and then the third, or combine the last two and then the first. To compare them, fix a common configuration domain and a coefficient complex \(Q\) in which both operations take values. They then give maps \(f,g:P\to Q\), where \(P\) is the complex of the three inputs. Constructing these maps into the same \(Q\) is part of the problem. Their appropriate comparison can be a homotopy in the mapping complex \(\operatorname{Hom}(P,Q)\), rather than equality of formulas. With four fields, the comparisons must themselves satisfy a further homotopy relation.

To describe this without hiding the compatibility conditions, we first work with ordinary vector spaces and algebras. The bar construction will organize multiplication, its relations and the relations between those relations. Only after that construction is explicit will we return to points moving on a curve.

The reconstruction question is precise: can the operations on all ordered configurations be recovered from a coalgebra whose coproducts cut a configuration into consecutive blocks, including every higher homotopy? For coefficients equal to \(k\) on the empty configuration, positive word length is bounded by the number of points. That finite bound permits a bar–cobar equivalence even for cohomologically unbounded coefficients. Its support theorem also explains why, for three ordered points, the collision of the first and third can matter without a collision with the second. Readers already familiar with dg algebras can begin with the word construction below; the first two sections fix conventions and give the elementary examples used to interpret it.

## Complexes retain the equations and their solutions {#cohomology-and-parameters}

A cochain complex is a sequence of vector spaces and linear maps
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
The distinction between a boundary and a chosen primitive matters. Knowing that \(v=dw\) is solvable does not specify \(w\), and different choices can enter later operations.

Our shift convention is
\[
V[1]^n=V^{n+1},\qquad d_{V[1]}=-d_V.
\]
Thus a vector of degree \(r\) in \(V\) has degree \(r-1\) in \(V[1]\). Write \(sv\) for that shifted vector; \(s\) has degree \(-1\). Tensor products use the Koszul sign rule:
\[
d(v\otimes w)=dv\otimes w+(-1)^{|v|}v\otimes dw,
\]
where \(|v|\) denotes the degree of a homogeneous vector.

A chain map \(f:V\to W\) commutes with the differentials. A homotopy from \(g\) to \(f\) is a degree-minus-one map \(h\) satisfying
\[
f-g=d_Wh+hd_V.
\]
Homotopic maps induce the same cohomology map, but the homotopy contains information that this induced map forgets. More generally, maps of all degrees form a complex
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
in degrees zero and one. For \(t\ne0\), the \(u_1,v_1\) summand is contractible: set \(h(v_1)=t^{-1}u_1\) and let \(h\) vanish on the other basis vectors. If \(p\) projects to the remaining \(u_2,v_2\) summand and \(i\) includes it, then
\[
dh+hd=1-ip.
\]
Both cohomology groups have dimension one. At \(t=0\), both have dimension two. The Euler characteristic is zero throughout, but the contracting homotopy has a pole at the point where the cohomology changes. A fibrewise calculation and a comparison valid over the whole parameter line are therefore different assertions.

::: figure fig-cohomology-jump

## Relations can leave a higher operation {#ch05-relations-can-leave-a-higher-operation}

A differential graded algebra is a graded associative algebra \(A\), equipped with a differential satisfying
\[
d(ab)=(da)b+(-1)^{|a|}a\,db.
\]
Its cohomology is an associative graded algebra. Passing to cohomology nevertheless loses information about how products become boundaries.

Here is an explicit example. Let
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
This cycle is not a boundary: the degree-two boundaries are spanned by \(ab\) and \(bc\), whereas \(ay+xc\) is a different linear combination of words in the free algebra.

Changing \(x\) or \(y\) by a degree-one cycle changes \([z]\) by an element of
\([a]H^1(A)+H^1(A)[c]\). In this example \(H^1(A)\) is spanned by \([a],[b],[c]\), and that indeterminacy cannot remove the words \(ay\) and \(xc\). The resulting nonzero coset is a **triple Massey product**: a higher operation defined from two vanishing products and choices of their primitives. The multiplication table on cohomology records the two zero products but does not determine this further class.

The same issue arises when an associative multiplication is transferred to a smaller complex. Suppose maps \(i:H\to A\), \(p:A\to H\) and a homotopy \(h\) satisfy \(pi=1\) and \(dh+hd=1-ip\). Projecting the product gives \(p\mu(i\otimes i)\) on \(H\). Composing products introduces the intermediate projection \(ip\); replacing it by the identity produces terms containing \(h\). Those terms are the first higher operations. A comparison that retains only the projected binary product can discard the very primitives needed to compose it.

## Words and the reduced bar construction {#ch05-words-and-the-reduced-bar-construction}

An augmentation of a unital dg algebra is a dg algebra map \(\epsilon:A\to k\), where \(k\) is the ground field. It splits the underlying complex as
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
The empty word is \(1\). This deconcatenation is coassociative because splitting at two positions gives the same three consecutive subwords in either order.

The bar differential has two kinds of terms. It applies the differential of \(A\) to one letter, or multiplies two adjacent letters. With our cohomological suspension convention, its defining components are
\[
b_1(sa)=-s(da),\qquad
b_2(sa\otimes sb)=(-1)^{|a|}s(ab).
\]
They extend to words by applying the operation in each possible position. Passing a degree-one operation across a prefix contributes the degree of that prefix. Explicitly,
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
Applying \(b\) again gives \([(ab)c]-[a(bc)]=0\). The length-three word makes the relation between the two multiplications into an explicit boundary equation. Longer words organize the compatible ways of repeating this operation. These are the usual algebraic bar formulas, expressed in cohomological degrees; see Loday–Vallette, [*Algebraic Operads*, §§2.2–2.3](https://www.math.univ-paris13.fr/~vallette/Operads.html).

Two small algebras show what this complex measures. For \(A=k[x]\), augmented by \(x\mapsto0\), the two-term free resolution
\[
0\longrightarrow A\xrightarrow{\,x\,}A\longrightarrow k\longrightarrow0
\]
computes the same groups as the bar resolution. Tensoring over \(A\) with \(k\) kills its differential, so
\[
H^*(BA)=k\oplus k\cdot[x],\qquad |[x]|=-1.
\]
In the bar complex itself, \([x^2]=b[x|x]\), and similarly higher powers in a single letter do not give new degree-minus-one classes.

For \(A=k[\epsilon]/(\epsilon^2)\), the augmentation ideal is one-dimensional and its product is zero. Every bar differential is therefore zero:
\[
BA=\bigoplus_{n\ge0}k[\epsilon|\cdots|\epsilon],
\qquad H^{-n}(BA)=k\quad(n\ge0).
\]
The corresponding free resolution has multiplication by \(\epsilon\) at every step. It is exact before tensoring with \(k\), and every differential becomes zero afterwards. Thus the single relation \(\epsilon^2=0\) produces homological information in arbitrarily long words. These groups are traditionally denoted \(\operatorname{Tor}_n^A(k,k)\), with \(n=-\text{cohomological degree}\).

## One differential encodes all associativity homotopies {#ch05-one-differential-encodes-all-associativity-homotopies}

The word complex also accommodates multiplication that is associative only through specified homotopies. A degree-one map \(b\) on \(T^c(V[1])\) is a **coderivation** if
\[
\Delta b=(b\otimes1+1\otimes b)\Delta,
\]
with the graded tensor convention. Such a map is determined by its components
\[
b_n:(V[1])^{\otimes n}\longrightarrow V[1].
\]
On a finite word only finitely many components can act. An uncurved \(A_\infty\)-algebra structure is a coderivation with no constant component and with \(b^2=0\). Undoing the shifts gives operations \(m_n:V^{\otimes n}\to V\) of degree \(2-n\). The suspended formulation fixes the signs without a separate convention for every arity.

The length-one equation is \(m_1^2=0\); length two says that \(m_2\) is a chain map. At length three, the associator of \(m_2\) is the boundary of a degree-minus-one operation. At length four, the homotopies along the five parenthesizations of a fourfold product form a closed compatibility expression, and the next operation supplies its primitive. Continuing gives all the equations at once. Equivalently, their suspended form is
\[
\sum_{r+s+t=n}
b_{r+1+t}(1^{\otimes r}\otimes b_s\otimes1^{\otimes t})=0,
\]
where composition of graded tensor maps supplies the signs.

This is the meaning of **coherence** here: the actual operations and these compatibility equations are included in the structure. An associative product on cohomology does not provide them. Nor do a binary operation and one ternary homotopy determine all higher operations. The bar complex provides a place to write the entire family, while finite words ensure that its differential is an actual algebraic operation.

## Cobar reverses the construction {#ch05-cobar-reverses-the-construction}

Let \(C=k\oplus\bar C\) be a coaugmented dg coalgebra. Its reduced coproduct is \(\bar\Delta:\bar C\to\bar C\otimes\bar C\), obtained by removing the two terms involving \(1\). The coalgebra is **conilpotent** if sufficiently many iterated reduced coproducts kill each element. The tensor coalgebra above has this property because a word cannot be split into more nonempty pieces than its length.

The cobar construction is the tensor algebra
\[
\Omega C=T(\bar C[-1]).
\]
Write \(uc\) for a generator in \(\bar C[-1]\), so \(|uc|=|c|+1\). If \(\bar\Delta c=\sum c'\otimes c''\), its differential is the derivation determined by
\[
d_\Omega(uc)=-u(d_Cc)
+\sum(-1)^{|c'|+1}(uc')(uc'').
\]
Thus bar shortens words by multiplication, while cobar lengthens them by coproduct. The signs are compatible: when \(a,b\) have degree zero, the generator \(u[a|b]\) in \(\Omega BA\) satisfies
\[
d_\Omega u[a|b]=-u[ab]+(u[a])(u[b]).
\]
The map \(\Omega BA\to A\) sending \(u[a]\) to \(a\) and the longer single generators to zero respects this equation. Its extra generators explicitly encode the multiplication relations in \(A\).

More generally, a degree-one map \(\tau:C\to A\), vanishing on the coaugmentation and landing in \(\bar A\), is a **twisting cochain** when
\[
d_A\tau+\tau d_C+\mu_A(\tau\otimes\tau)\bar\Delta=0.
\]
Here \((\tau\otimes\tau)(c'\otimes c'')=(-1)^{|c'|}\tau(c')\otimes\tau(c'')\). This one equation says exactly that \(uc\mapsto\tau(c)\) extends to a dg algebra map \(\Omega C\to A\). For conilpotent \(C\), iterating its reduced coproduct gives the corresponding dg coalgebra map \(C\to BA\). We obtain the strict bar–cobar adjunction
\[
\operatorname{Hom}_{\rm dgAlg}(\Omega C,A)
\cong\operatorname{Tw}(C,A)
\cong\operatorname{Hom}_{\rm dgCoalg}(C,BA).
\]
An adjunction provides comparison maps. Whether those maps are equivalences requires a theorem about the objects and weak equivalences under consideration. The geometry of ordered configurations supplies an especially useful finiteness condition for such a theorem.

## Ordered cuts give a finite geometric bar construction {#ch05-ordered-cuts-give-a-finite-geometric-bar-construction}

Let \(X\) be a smooth separated finite-type curve over a characteristic-zero field \(k\). Write \(\mathcal D(X^n)\) for the unbounded derived category of right algebraic differential modules with quasi-coherent underlying modules, retaining its higher mapping spaces. A **word coefficient system** consists of complexes \(M_n\in\mathcal D(X^n)\) for \(n\ge1\), together with coherent equivalences
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
The symbol \(\boxtimes^{\mathbf L}\) means derived external tensor product. Open direct image allows the prescribed singular behaviour along the removed diagonals; it is not a choice of a finite pole bound. Empty blocks contribute their complexes over \(k\). Iterated products use consecutive blocks in their written order. Localizing at their interblock diagonals gives the common domain for every parenthesization.

The unit is \(\mathbf1=(k,0,0,\ldots)\). An augmented algebra is **connected in arity** if its augmentation identifies \(A_0\) with \(k\); a counital coaugmented coalgebra has the analogous condition \(C_0\simeq k\). This says nothing about cohomological degrees. The positive-arity summands \(\bar A,\bar C\) have the decisive property
\[
(M^1\star\cdots\star M^r)_n=0
\quad\text{if all }M^i_0=0\text{ and }r>n.
\]
Indeed, every nonzero term assigns at least one point to each of the \(r\) factors.

**Theorem: connected consecutive-cut duality.** In \(\mathcal W_X\), bar and cobar for consecutive-cut convolution are inverse equivalences between connected augmented coherent associative algebras and connected counital coaugmented coherent coassociative coalgebras. The equivalence includes their full mapping spaces. It requires no cohomological boundedness or finite-dimensionality of coefficients.

“Coherent” means that all higher associativity or coassociativity comparisons are retained, not just the equations visible on cohomology. One can compute the equivalence with strict dg representatives. Its proof uses the arity filtration: the normalized bar and cobar layers are
\[
\bar A^{\star r}[r],\qquad \bar C^{\star r}[-r].
\]
In arity \(n\), they vanish for \(r>n\). Consequently the relevant constructions stabilize after finitely many normalized stages in each coefficient. No interchange of an arbitrary infinite tensor product with an inverse limit is needed. The underlying filtered associative duality is developed by Matsuoka, [*Koszul duality between \(E_n\)-algebras and coalgebras in a filtered category*, Lemmas 4.13 and 4.17](https://arxiv.org/html/1409.6943v4); intrinsic bar and cobar are treated in Lurie, [*Higher Algebra*, §5.2.2](https://www.math.ias.edu/~lurie/papers/HA.pdf).

There are two adjunction conventions to distinguish. The strict twisting-cochain construction above has \(\Omega_{\rm dg}\dashv B_{\rm dg}\). The intrinsic connected equivalence also has the adjunction \(B\dashv\Omega\), with maps \(A\to\Omega BA\) and \(B\Omega C\to C\). The comparison of the two presentations identifies their equivalences, not their oppositely directed canonical chain maps.

::: figure fig-connected-bar-cobar

## The support remembers which cuts were allowed {#ch05-the-support-remembers-which-cuts-were-allowed}

A coalgebra \(C\) is **factorizing across consecutive cuts** if, on every \(U_{p,n-p}\), its cut coproduct
\[
C_n|_{U_{p,n-p}}\longrightarrow
(C_p\boxtimes^{\mathbf L}C_{n-p})|_{U_{p,n-p}}
\]
is an equivalence. An **associative chiral algebra** in the word category is an augmented \(E_1\)-algebra \(A\) for consecutive-cut convolution, with \(A_0\simeq k\), whose bar coalgebra \(BA\) factorizes in this sense. Here \(E_1\) means that the multiplication and all its associativity homotopies are retained. Its augmentation ideal has zero empty coefficient. The support theorem below identifies these algebras by the support of their positive-arity coefficients. Put
\[
Z_n=X^n\setminus\bigcup_{p=1}^{n-1}U_{p,n-p},
\qquad Z_1=X.
\]
For a complex \(F\), derived sections supported on \(Z\), denoted \(R\Gamma_ZF\), form the fibre of the restriction map \(F\to Rj_*j^*F\) to the complementary open set.

**Support theorem.** Consecutive-cut duality restricts to an equivalence between factorizing coalgebras and connected algebras whose positive-arity coefficients vanish on every cut open. For a factorizing coalgebra,
\[
\overline{\Omega C}_n\simeq R\Gamma_{Z_n}(C_n)[-1].
\]
The shift is part of the formula. To see its origin, index a cube by subsets of the \(n-1\) possible cuts. A subset of size \(r-1\) gives \(r\) blocks, hence a cobar term shifted by \([-r]\). The corresponding localization cube has shift \([-(r-1)]\); the two totalizations differ by \([-1]\). Factorization identifies the entire cut cube with the localization cube, including its maps.

For three points,
\[
Z_3=(\Delta_{12}\cup\Delta_{13})
\cap(\Delta_{13}\cup\Delta_{23})=\Delta_{13}.
\]
Here \(\Delta_{ij}\) is the diagonal \(x_i=x_j\). A configuration with \(x_1=x_3\) and \(x_2\) elsewhere defeats both consecutive cuts. The support is therefore larger than the small diagonal where all three points coincide.

The supported complex alone does not specify the associative algebra. The multiplication on the cut cobar also uses the inverse factorization maps on the separating opens. Its unit lies at the empty configuration. A vacuum marking is separate singleton data: an identification \(A_{\{1\}}\cong\omega_X\otimes_{\mathcal O_X}G\) with a left differential module \(G\) and a horizontal map \(\mathcal O_X\to G\). A vacuum framing further compares the configuration operations with the simultaneous field products, preserving substitutions, translation and the vacuum.

The same definition of an associative chiral algebra can be used with the symmetric convolution on the full ordered collision atlas. There, factorization requires each specified coproduct component to be an equivalence. Its support consequence differs from the cut theorem. If \(C=BA\) and \(U\) is the two-point distinct locus, put \(V=(C_{\{1\}}\boxtimes C_{\{1\}})|_U\). Componentwise factorization gives
\[
\overline A_{\{1,2\}}|_U\simeq V[-2].
\]
Thus nonzero \(V\) gives a nonzero coefficient away from the diagonal. Small-diagonal support on the atlas is instead characterized by a joint word-factorization condition, which compares the full direct sum of ordered word terms. It cannot be substituted for the componentwise condition defining the factorizing bar.

We have obtained an equivalence of specified algebraic structures, with their homotopies and geometric supports. To turn it into a duality of representations, one must determine the functors on modules and inspect their unit and counit. Those maps, rather than a resemblance between two algebras, are the subject of the [next chapter](06-duality-and-induction.md).
