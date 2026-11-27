# Actions and derived centres

Place a linear bulk field above a boundary and leave the boundary empty. In the free abelian half-space model there are fields whose projection to the boundary is zero. Keep one of these fields in place and insert a boundary current below it. The two fields can now contract. Take a nonzero current level \(\kappa\). With the test scaled by \(\kappa\) and the mixed pairing normalized as below, the output is \(\hbar\kappa\) times the vacuum, where \(\hbar\) counts one contraction. The two inputs to the same operation have given different information, already on the field complexes.

For an ordinary algebra \(A\), multiplication by a central element \(z\) can be recovered from its value on the unit. Evaluating at \(1\) gives \(z\) itself, and multiplication then specifies its action on every module. On a boundary complex, an insertion can be homotopic to zero. Does the homotopy still work when another boundary operator is composed with it? The cubic potential gives an example where even the choice of homotopy cannot make the two compositions agree. For fields at several positions the same question also involves restriction when positions separate or collide.

## Central operations on modules {#ch07-central-operations-on-modules}

**Definition (centre).** For a unital associative algebra \(A\) over a characteristic-zero field \(k\), its centre is
\[
Z(A)=\{z\in A:za=az\text{ for every }a\in A\}.
\]
For every left \(A\)-module \(M\), a central element gives an \(A\)-linear operator \(m\mapsto zm\), naturally in \(M\). Conversely, every natural endomorphism of the identity functor on \(A\)-modules arises this way. Let \(\eta\) be such an endomorphism and set \(z=\eta_A(1)\) on the regular left module. By left \(A\)-linearity, \(\eta_A(a)=az\). Right multiplication by \(a\) is also a map of left modules. Naturality for this map gives \(\eta_A(a)=za\), so \(z\) is central. For any \(m\in M\), the module map \(A\to M,\ b\mapsto bm\), sends \(1\) to \(m\). Naturality now gives \(\eta_M(m)=zm\).

In particular \(Z(A)\cong\operatorname{End}(\mathrm{id}_{A\text{-}\mathrm{Mod}})\), with composition on the right. Here a proposed operator is tested on every module and every module map. For boundary fields a restriction to a smaller open set and a collision of two insertions give further maps on which to test it.

The left action on the regular module determines the value at \(a\) from the value at \(1\). Right multiplication supplied the other condition in the proof. To impose both actions in a derived calculation, regard \(A\) as a module over its enveloping algebra \(A^e=A\otimes_k A^{\mathrm{op}}\), with \((a\otimes b^{\mathrm{op}})x=axb\). An \(A\)-bimodule map \(A\to A\) is determined by a central element, so
\[
Z(A)=\operatorname{Hom}_{A^e}(A,A).
\]
Replacing Hom by its derived functor gives the Hochschild cochain complex
\[
C^\bullet(A,A)\simeq R\operatorname{Hom}_{A^e}(A,A).
\]
For an ordinary algebra over \(k\), the bar resolution represents this complex by \(C^n(A,A)=\operatorname{Hom}_k(A^{\otimes n},A)\). Its first differentials are
\[
(bz)(a)=az-za,\qquad
(bf)(a_1,a_2)=a_1f(a_2)-f(a_1a_2)+f(a_1)a_2.
\]
Consequently \(HH^0(A)=Z(A)\), while \(HH^1(A)\) consists of derivations modulo inner derivations. Higher degrees retain further compatibility data.

A class represented by a bimodule map \(A\to A[n]\) acts on a derived left module through
\[
M\simeq A\otimes_A^L M
\longrightarrow A[n]\otimes_A^L M\simeq M[n].
\]
Here differentials have degree \(+1\), and \(V[1]^j=V^{j+1}\). The derived centre retains these operations and their coherent compositions. Hochschild cochains carry an \(E_2\)-algebra structure: products are accompanied by homotopies encoding their interchange. On cohomology this includes the cup product and the degree-minus-one Gerstenhaber bracket. An equivalence of underlying complexes alone does not identify those operations. See [Higher Algebra, §5.3.1](https://www.math.ias.edu/~lurie/papers/HA.pdf) and [Gerstenhaber’s construction](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Ger63.pdf).

**Example (the dual numbers).** Take \(A=k[x]/(x^2)\). The ordinary centre is all of \(A\). A derivation is determined by \(f(x)=a+bx\), and
\[
0=f(x^2)=2x f(x)=2ax
\]
forces \(a=0\). Since \(A\) is commutative, inner derivations vanish. Hence
\[
HH^0(A)=k\oplus kx,\qquad HH^1(A)=k\delta,
\qquad \delta(x)=x.
\]
The class \(x\) in degree zero acts on an \(A\)-module by multiplication. The degree-one cochain \(\delta\) takes an algebra element as input. It gives \(\delta(1)=0\) and \(\delta(x)=x\), so the Gerstenhaber bracket with the degree-zero class is \([\delta,x]=x\). Its value on the unit alone would miss this bracket.

### A homotopy tested by an odd boundary operator {#ch07-cubic-naturality}

Consider the B-twisted Landau–Ginzburg model with \(W=x^3\) at the origin over \(k[[x]]\), in characteristic zero. Choose a boundary with one even and one odd basis vector. Its odd operator \(Q\) and its endomorphism differential \(d\) are
\[
 Q=\begin{pmatrix}0&x\\x^2&0\end{pmatrix},\qquad
 dB=QB-(-1)^{|B|}BQ .
\]
Thus \(Q^2=x^3 I\) and \(d^2=0\). Write \(E_{ij}\) for the matrix units in this order of the basis. Multiplication by the bulk coordinate gives \(xI=dh\) with \(h=E_{21}\). In particular it acts by zero on the cohomology of the boundary operators. Keep the closed odd operator \(\psi=E_{12}-xE_{21}\) at the boundary. Moving the odd homotopy past this insertion gives the graded commutator
\[
 h\psi+\psi h=E_{22}+E_{11}=I .
\]
{#eq-ch07-cubic-naturality}
For a homotopy natural up to higher homotopies, this commutator must itself have a primitive. Indeed the zero-input part of a Hochschild nullhomotopy is an odd endomorphism with differential \(xI\). The equation on one closed input says that the failure of this endomorphism to commute with that input is an internal boundary.

Could a different primitive of \(xI\) satisfy the equation? An odd matrix \(h'=aE_{12}+bE_{21}\) has \(dh'=x(b+xa)I\), so \(h'=h+a\psi\) is the general solution. Since \(\psi^2=-xI\),
\[
 h'\psi+\psi h'=(1-2ax)I .
\]
Every entry of an internal boundary is divisible by \(x\), since every entry of \(Q\) is. The commutator has constant term \(I\). Thus the proposed nullhomotopy of the bulk action already fails on one boundary morphism, for every possible initial choice.

The identity defect gives an independent calculation of this class across the category of matrix factorisations supported at the origin. Put \(u=x-y\) and \(v=x^2+xy+y^2\). The odd matrix with upper entry \(u\) and lower entry \(v\) squares to \((x^3-y^3)I\). Its closed even endomorphisms are scalar matrices. An odd endomorphism with entries \(a,b\) has differential \((ub+va)I\). Hence its even endomorphism cohomology is
\[
 k[[x,y]]/(u,v)\cong k[[x]]/(3x^2).
\]
The class of \(x\) survives. The identity-kernel theorem identifies this algebra with the even Hochschild cohomology of the two-periodic boundary category. On the single boundary \(h\) killed the coordinate. Its commutator with \(\psi\) explains why that calculation lost a class of the derived centre. [The diagonal factorisation and its proof](19-interacting-theories.md#ch19-diagonal-and-trace) · [Dyckerhoff, Proposition 6.3 and Corollaries 6.4–6.5](https://arxiv.org/pdf/0904.4713#page=34)

## A bulk insertion acting on a boundary current {#ch07-supported-bulk-action}

Take the free abelian half-space theory with response operator \(\kappa\partial_z\), normal coordinate \(t\geq0\) and complex boundary coordinate \(z\). Here \(\hbar\) is the formal parameter that counts contractions. Work with regular observables whose smooth test kernels have compact support at each finite field number. Over an open set \(V\) in the boundary, choose a smooth profile of integral one supported in \(0\leq t<\varepsilon\). It gives a cochain inclusion \(i^q\) of the boundary current complex \(\mathcal A_\kappa(V)\) into the collar observables. Integration in the normal direction gives the linear projection \(p\). Its quantum extension counts pair contractions involving the fields being integrated out,
\[
p^q=\operatorname{Sym}(p)\exp(\hbar\partial_{P_2}).
\]
Here \(P_2\) is the pairing obtained from the normal contracting homotopy. The operator \(\partial_{P_2}\) contracts one unordered pair, so its exponential is a finite sum on every polynomial observable.

Put the bulk support \(U\subset V\times(a,b)\) above the boundary profile, so that \(\varepsilon<a<b\). To act with a bulk observable \(f\) supported in \(U\), lift the boundary input \(v\) into the collar, multiply by the extension of \(f\), and project the product back to the boundary. This gives
\[
\beta_{U;V}(f)(v)=p^q\bigl(\operatorname{ext}_U(f)\, i^q(v)\bigr).
\]
The middle product is the factorization product after extension by zero. Its two factors have disjoint normal supports, which removes cross terms in the Batalin–Vilkovisky differential there. Both outside maps commute with the differentials. Thus \(\beta_{U;V}\) maps the bulk complex into the complex of continuous boundary endomorphisms, with differential \(D\mapsto dD-(-1)^{|D|}Dd\). This construction specifies a supported action on a particular boundary.

Take a normal one-form of integral one above the boundary profile, in the field component killed by \(p\). Choose its compact tangential function \(\phi\) and the compactly supported \((0,1)\)-form \(\alpha\) of the boundary current \(v\) with
\[
 \tau_{\mathbb C}(\phi\alpha)
 =\frac{1}{2\pi i}\int_V dz\wedge\phi\alpha=1 .
\]
Normalize the eliminated polarization by choosing its unit-strength test \(u_1\) with \(P_2(u_1,i(v))=1\), and insert \(u=\kappa u_1\). In the shifted field convention \(\zeta^2=-1\), the boundary inclusion on \(\alpha\) carries the factor \(-\zeta\), and \(u_1\) carries \(\zeta^{-1}\). The sign of the normal contraction then gives \(P_2(u,i(v))=\kappa\,\tau_{\mathbb C}(\phi\alpha)=\kappa\), while \(p(u)=0\). Only one pair can contract. Consequently
\[
\beta(u)(1)=0,\qquad \beta(u)(v)=\hbar\kappa .
\]
The term with no contraction contains \(p(u)=0\). The one contraction uses both inputs, leaving \(\hbar\kappa\) times the vacuum. On the square of the same even current there are two choices of factor, giving \(2\hbar\kappa v\). Here \(\kappa\) was fixed when the bulk test was scaled. The two readings compute the response of the free model to that test, before taking cohomology. A class of bulk observables would also require \(du=0\).

To compose two such operations one projects back to the boundary after the lower insertion. Write \(H^q\) for the degree-minus-one homotopy between the identity on collar observables and projection followed by boundary inclusion. If a second insertion \(g\) and its normal homotopy stay below \(f\), inserting \(1-i^qp^q=dH^q+H^qd\) between the two products gives a homotopy from joint insertion to successive action. Moving the supports through one another requires the [ordered contact terms](09-mixed-boundaries.md#ch09-ordered-poles-and-their-complete-differential).

## A factorizing actor and its pointing {#ch07-a-factorizing-actor-and-its-pointing}

Work on \(X=\mathbb A^1_k\). At the labelled configuration \((x,y,x)\) with \(x\ne y\), labels \(1,3\) can form one block and label \(2\) the other. The cut \(1|23\) would put \(x\) in both blocks. To encode which cuts exist as positions move, use a complex of differential modules at each finite labelled configuration, with its ordered collision charts. A differential module is a sheaf with an action of differential operators on the position variables.

A factorizing coalgebra \(F\) assigns such coefficients \(F_I\) to the label sets \(I\). We take the coalgebras coaugmented and counital, with empty coefficient \(k\). For an ordered division \(I=A\sqcup B\), let \(U_{A,B}\) be the locus where each point in \(A\) is disjoint from each point in \(B\). There the coproduct identifies the full coefficient with the external product of those of the two blocks,
\[
F_I\big|_{U_{A,B}}
\simeq (F_A\boxtimes F_B)\big|_{U_{A,B}}.
\]
Successive divisions carry coassociativity homotopies and their higher compatibilities. Maps of factorizing coalgebras respect these data and the collision restrictions. Exchanging \(A|B\) with \(B|A\) requires a suitable cocommutative structure.

In the three-label example the coproduct divides the labels between two coefficients. An operation on a boundary at \((x,y,x)\) instead needs an actor coefficient and a boundary coefficient, each at all three labels. The two constructions have different tensor products.

Call \(F\) an **actor** when it parametrizes operations on another object. To split an insertion into separated pieces one uses disjoint convolution \(\star\) on the full ordered collision atlas. It sums over all ordered bipartitions. At two distinct labelled points its positive part has the summands \(1|2\) and \(2|1\). Its unit \(K\) is concentrated at the empty configuration. To let \(F\) act on a boundary with the same labels, one uses \(\otimes^!\), the extraordinary pullback of the external tensor product along the diagonal. Its unit \(J\) has the local tensor unit at each configuration. [Convolution on the full ordered collision atlas](04-factorization.md#ordered-cut-geometry).

**Definition (pointing).** A pointing on \(F\) is a coherent coalgebra map
\[
u:J\longrightarrow F.
\]
It specifies a vacuum operation together with all its compatibility homotopies. It contains more information than a class in the singleton cohomology. These conventions are those of the [ordered-collision coalgebra construction](#ref-ch07-01), particularly its coalgebra category and diagonal tensor.

The smallest useful test algebra has two orthogonal idempotents:
\[
B=kp_1\oplus kp_2,\qquad p_ip_j=\delta_{ij}p_i.
\]
At a single position, multiplication by \(\lambda_1p_1+\lambda_2p_2\) sends \(p_i\) to \(\lambda_i p_i\), and its value on \(1=p_1+p_2\) recovers both coefficients. Write \(C=C_B\) for the Chevalley coalgebra. Its coefficients are built from finite partitions with a \(B\)-label on each block, and its differential merges blocks using the chiral operation of \(B\). It has multiplication \(m:C\otimes^!C\to C\) and total unit pointing \(u_B:J\to C\). The idempotents now distinguish colours on whole configurations. The test is whether multiplication recovers all pointed operations there.

**Definition (character and pointed action).** A character of \((F,u)\) is a coalgebra map \(g:F\to C\) together with a specified homotopy \(gu\simeq u_B\). An action is a coalgebra map \(\alpha:F\otimes^!C\to C\) together with a specified homotopy \(\alpha(u\otimes^!1_C)\simeq1_C\). Thus inserting the *actor* vacuum must act as the identity on every boundary input. The definition uses the coassociative coalgebra \(F\) and requires no multiplication on it. The spaces retaining these data are
\[
\begin{aligned}
\mathcal X(F,u)
&=\operatorname{hofib}_{u_B}\left[
\operatorname{Map}_{\mathrm{Coalg}}(F,C)
\xrightarrow{u^*}\operatorname{Map}_{\mathrm{Coalg}}(J,C)\right],\\
\mathcal A_C(F,u)
&=\operatorname{hofib}_{1_C}\left[
\operatorname{Map}_{\mathrm{Coalg}}(F\otimes^!C,C)
\xrightarrow{(u\otimes^!1_C)^*}\operatorname{Map}_{\mathrm{Coalg}}(C,C)\right].
\end{aligned}
\]
A homotopy fibre records a point upstairs and a path from its image to the specified base point; its higher simplices record the remaining compatibilities.

Given a character, multiply its value by the boundary input. Given an action, one can evaluate it on the total boundary unit \(p_1+p_2\) with the actor input still free. On whole configurations these operations are
\[
\begin{aligned}
\Theta(g)&=m(g\otimes^!1_C),\\
\Psi(\alpha)&=\alpha\circ(\mathrm{id}_F\otimes^!u_B):F\simeq F\otimes^!J\longrightarrow C.
\end{aligned}
\]
To define \(\Theta:\mathcal X(F,u)\to\mathcal A_C(F,u)\), use the path \(gu\simeq u_B\) supplied by the character. Multiplying along this path identifies the action of \(\Theta(g)\) at the actor pointing with \(m(u_B\otimes^!1_C)\simeq1_C\), by the left-unit law. For \(\Psi:\mathcal A_C(F,u)\to\mathcal X(F,u)\), start with the action path \(\alpha(u\otimes^!1_C)\simeq1_C\). Evaluating this path on the boundary vacuum gives \(\Psi(\alpha)u=\alpha(u\otimes^!u_B)\simeq u_B\), the path required of a character. Thus both constructions take values in the stated homotopy fibres. Starting with \(g\), evaluation of its multiplication action on the boundary vacuum gives \(\Psi\Theta(g)\simeq g\) by the right-unit law \(m(1_C\otimes^!u_B)\simeq1_C\).

**Definition (recognition).** For a fixed \((F,u)\) and this two-colour boundary \(C\), recognition means that \(\Theta\) is an equivalence of the complete spaces. The remaining composite would recover \(\alpha\) by first evaluating it on the boundary vacuum and then multiplying by the original boundary input. The required homotopy \(\Theta\Psi(\alpha)\simeq\alpha\) must itself respect the actor pointing, each collision restriction and families of actions. The half-space calculation tested a cochain map on two inputs. Recognition concerns the two coalgebra mapping fibres defined here.

A centre representing this geometric action problem would be a pointed actor \(Z_C\) with a universal action, such that
\[
\operatorname{Map}_{J/}\bigl((F,u),Z_C\bigr)
\simeq\mathcal A_C(F,u)
\]
naturally for every admitted actor. Existence is part of that assertion. The binary recognition question tests whether \(C\), with its multiplication action, has this property on a specified family of actors. It does not identify the action problem with the Hochschild complex of the two-dimensional algebra \(B\).

Derived maps can be represented using roofs
\[
P\xleftarrow{\simeq}Q\longrightarrow R,
\]
where the left arrow is a weak equivalence in the category being used. A common refinement replaces \(Q\) by another source and compares both legs. For pointed factorizing coalgebras, the pointing and the collision homotopies also belong to the diagram. For ordinary dg vertex algebras, the weak equivalences below are quasi-isomorphisms of state complexes. These two uses of roofs have different objects and weak equivalences. Comparing their mapping spaces requires a map that preserves both legs, their evaluation and their refinements.

::: figure fig-character-action-comparison

## Recognition on Chevalley coalgebras {#ch07-recognition-on-chevalley-coalgebras}

For a dg chiral algebra \(V\), form its main-diagonal Chevalley coalgebra \(C_V\) by attaching a \(V\)-coefficient to each block of a partition, at the common position of that block. Two labels give a term with two separate \(V\)-inputs and a term with one input at the merged position. The differential combines the internal differential with the merger induced by the chiral product. A closed horizontal unit in \(V\) satisfying the vacuum identities supplies a pointing of \(C_V\). It also supplies contractions in the mapping complexes. We can use those contractions even when the action we are testing specifies a different pointing \(u\).

**Recognition theorem.** Suppose \(V\) is any unbounded dg chiral algebra over a characteristic-zero field on \(\mathbb A^1\), with a genuine closed horizontal unit. For every coherent coassociative pointing \(u:J\to C_V\), the maps \(\Theta\) and \(\Psi\) are inverse equivalences between \(\mathcal X(C_V,u)\) and \(\mathcal A_C(C_V,u)\). No homotopy from \(u\) to the genuine unit pointing is required. The equivalence is natural under all pointed coalgebra maps between these objects, including those that preserve no chosen presentation. [Arbitrary-pointing recognition](#ref-ch07-02).

In the two-idempotent algebra, a nonzero product of idempotents has the same colour as each factor. A general action might carry a label of one colour to the other. In the resolved mapping diagram, count the source blocks containing at least one label whose input and output colours differ. The zero layer tests the colour-preserving maps. To recover the whole action it remains to contract the layers with positive count. The genuine unit supplies contractions \(h_P,h_Q\) of the two absolute complexes \(P,Q\) at a positive mismatch layer. The arbitrary pointing and the action path supply the actual restriction \(r:P\to Q\). In its fibre the differential and contraction are
\[
d(c,z)=(d_Pc,rc-d_Qz),\qquad
h(c,z)=(h_Pc,\,h_Qrh_Pc-h_Qz).
\]
Here \(c\in P^j,\ z\in Q^{j-1}\). The mixed term cancels the discrepancy between \(rh_P\) and \(h_Qr\), giving \(dh+hd=1\) for this \(r\). Thus every positive mismatch layer contracts with the prescribed pointing in place. There are only finitely many partition steps at each finite configuration. Passing through these layers in the full mapping diagrams proves the equivalence even for unbounded coefficient complexes.

One can attach coefficients to the Chevalley actor and project them away. For recognition to survive, pullback along this projection must preserve the character space and the action space, including the path at the chosen pointing. For an arbitrary unbounded complex \(M\) of right differential modules, form \(P(M)\) by assigning either a unit coefficient or an \(M\)-coefficient to each label. In a summand with several \(M\)-labels, those labels must occupy distinct positions, and an \(M\)-label is last in any equality block containing it. Restrict the external tensor of the assigned coefficients to that open, extend it by the direct-image functor, and sum over assignments. Projection to the summand with only unit coefficients gives \(P(M)\to J\).

For
\[
F=P(M)\otimes^!C_V,\qquad h:F\longrightarrow C_V,
\]
every pointing \(u\) gives the complete projected pointing \(hu\). Pullback along \(h\) identifies both character and action spaces with those of \((C_V,hu)\). Recognition therefore holds for every \(u\) in this family. No boundedness, finite generation, holonomicity or restriction on the connection of \(M\) is imposed. The proof contracts the positive \(M\)-sectors as two-sided coefficient modules, rather than requiring the pointing to preserve those sectors. [Radical reduction](#ref-ch07-03).

A nonunital chiral algebra \(W\) lacks the genuine vacuum used to contract the absolute layers. Its chiral unitization \(W^+=W\oplus\omega_X\) adjoins the vacuum line \(\omega_X\) of right differential forms on the curve. The inclusion gives \(i:C_W\to C_{W^+}\), pointed upstairs by the entire composite \(iu\). Restriction back to \(W\) now has to preserve both mapping fibres. Write \(u_1\) for the one-position component of the original pointing.

**Unitization theorem.** Let \(W\) be an arbitrary unbounded, possibly noncommutative and nonconstant nonunital dg chiral algebra on \(\mathbb A^1_k\). Suppose its coherent pointing \(u\) admits a strict closed horizontal degree-zero state \(a:\omega_X\to W\) such that
\[
H^0(a)=H^0(u_1):\omega_X\longrightarrow H^0(W).
\]
Then restriction along \(i\) induces equivalences on both complete character and action fibres. Consequently \(\Theta\) and \(\Psi\) are inverse for \((C_W,u)\), naturally on the full stated subcategory. The displayed equality is only in ordinary cohomology. Equality of \(a\) and \(u_1\) in full derived Hom is not a hypothesis. [Unitization from an ordinary horizontal representative](#ref-ch07-04).

The strict state supplies a central chain-level multiplier on \(W^+\). Binary naturality of the pointing makes its action idempotent on every cohomology module. Localizing that multiplier and its complement gives actual chiral quasi-isomorphisms
\[
W\longrightarrow E\times N,\qquad
W^+\longrightarrow E\times N^+,
\]
in a commuting square with the two unitization inclusions. Here \(E\) is genuinely unital. The transported coherent pointings have ordinary singleton classes equal to the unit on \(E\) and zero on \(N^+\); the derived zero/unit singleton theorem promotes these particular classes to the required derived equalities. It does not replace the higher pointing cells. The split comparison then reduces both full fibres to the genuinely unital theorem. If \(H^0(u_1)=0\), both required fibres are empty.

For quasicoherent commutative dg \(\mathcal O_X\)-algebras with a compatible connection, recognition holds for every coherent pointing without this representative hypothesis. This includes all unbounded nonunital constant commutative examples, and also nonconstant examples whose ordinary singleton class has no strict horizontal representative. Thus the two results have overlapping, different domains. [Commutative algebras with connection](#ref-ch07-05).

### A genuine pointing without a horizontal vacuum representative {#ch07-horizontal-vacuum-example}

The distinction persists in an algebra with a singular operator product. Put
\[
D=\mathbb C[x,s]\otimes\Lambda(\eta,b),\qquad
|\eta|=|b|=-1,\qquad d\eta=x^2-x,\quad db=s ,
\]
with \(x,s\) closed of degree zero. Define translation by \(Tx=sx,\ T\eta=x(2x-1)b,\ Ts=Tb=0\). Then \(dT\eta=x(2x-1)s=T(d\eta)\), so this is a commutative differential vertex algebra. Evaluating \(x\) at \(i\in\{0,1\}\) and the other generators at zero gives a map \(q_i:D\to\mathbb C\). The equations \(s=0,\ x^2-x=0\) form a regular sequence. Their Koszul complex \(D\) therefore has cohomology \(\mathbb C\times\mathbb C\) in degree zero. On the ideal \(A=\ker q_0\), the other evaluation \(q_1\) is a quasi-isomorphism to \(\mathbb C\).

Now tensor \(A\) with the Heisenberg vertex algebra \(H\), whose current satisfies \(J_{(1)}J=\kappa\mathbf1\) for \(\kappa\ne0\). The nonunital algebra \(W=A\otimes H\) has the double-pole coefficient
\[
(x\otimes J)_{(1)}(x\otimes J)=\kappa x^2\otimes\mathbf1.
\]
Does the vacuum of \(H\) give a pointing of this nonunital example? The map \(q_1\otimes1:W\to H\) induces an equivalence on Chevalley coalgebras over the affine line. At each finite configuration filter by partitions. On each piece the map is obtained by external products and direct images of the same quasi-isomorphism, and the filtration is finite. The inverse equivalence transports the entire vacuum pointing from \(C_H\) to \(C_W\). Characters and actions for this pointing therefore agree by unital recognition. We can test separately whether one horizontal state of \(W\) represents its singleton.

What would a strict representative look like? Take its component in the Heisenberg vacuum. It would be a polynomial \(\sum_{n\geq0}p_n(z,s)x^n\) in the ideal \((x,s)\), horizontal for \(\partial_z+T\), and equal to one at \(x=1,s=0\). Horizontality gives \((\partial_z+ns)p_n=0\). For \(n>0\), the highest power of \(z\) forces \(p_n=0\). The remaining \(p_0\) belongs to \(s\mathbb C[s]\), so its value at \(s=0\) is zero. The coherent vacuum thus exists and gives recognition even though this equation for a strict singleton representative has no solution.

## Ordinary exterior sources and the map they compute {#ch07-ordinary-exterior-sources-and-the-map-they-compute}

The transported vacuum above was defined on a coalgebra, although no horizontal polynomial could represent its singleton. Translation gives a simpler test in the category of vertex algebras. Start with one odd generator \(\epsilon\) whose translation is zero. A strict map must send it to a translation-invariant state. Resolving the source allows its translation upstairs to be a boundary. What must one record about that boundary to specify the derived map?

Let \(\mathcal V\) be the category of ordinary algebraic unital \(\mathbb Z\)-graded dg vertex superalgebras over \(\mathbb C\), with parity given by degree modulo two, localized at maps inducing isomorphisms on all cohomology groups of the state complex. “Ordinary algebraic” means that the state spaces and tensors are the algebraic ones; no completed state product is implicit. Write \(d\) for the internal differential and \(T\) for translation, with \(dT=Td\).

Fix a target \(B\in\mathcal V\). A strict map out of \(\Lambda(\epsilon)\), with \(\epsilon\) of odd degree \(a\) and \(d\epsilon=T\epsilon=0\), sends \(\epsilon\) to a closed, translation-invariant state. On a resolution a closed lift can instead have translation \(Tb=db'\). The complex of such pairs is the homotopy fibre \(B^{hT}\) of \(T:B\to B\). In the ordinary vertex category the full source comparison is
\[
\operatorname{Map}_{\mathcal V}(\Lambda(\epsilon),B)
\simeq Z^a(B^{hT}\otimes\Omega_\bullet),\qquad
(B^{hT})^j=B^j\oplus B^{j-1},
\]
where \(D(b,b')=(db,Tb-db')\). Here \(\Omega_n\) is the algebra of polynomial differential forms on the standard \(n\)-simplex. The notation \(Z^a\) means closed total-degree-\(a\) elements. The components are \(H^a(B^{hT})\), and \(\pi_n=H^{a-n}(B^{hT})\) for \(n\ge1\). Every odd integer \(a\), including negative \(a\), is allowed, and \(B\) can be noncommutative and unbounded. [Odd-degree exterior sources](#ref-ch07-06).

For example, take \(a=1\) and \(B=\mathbb C\) in degree zero. The image \(b\) of the generator has to vanish, but the primitive \(b'\) may be any scalar. Since \(d=T=0\) on this target, distinct scalars give distinct classes in \(H^1(B^{hT})\). With two generators we must compare the two chosen primitives as well as the two images.

Now take \(A=\Lambda(\epsilon_1,\epsilon_2)\) with both generators of degree one and \(d=T=0\). Let \(B\) again be an arbitrary target in \(\mathcal V\). Put \(B_n=B\otimes\Omega_n\), graded by total degree. Define \(N(B)_n\) to be the set of tuples
\[
(e_1,e_2,u_1,u_2,\beta,\zeta)
\in (B_n^1)^2\times(B_n^0)^3\times B_n^{-1}
\]
satisfying
\[
de_i=0,\qquad du_i=Te_i,\qquad
d\beta=u_{1(0)}e_2,\qquad
d\zeta=T\beta-u_{1(0)}u_2.
\]
The zeroth product \(u_{(0)}v\) is the coefficient of \(z^{-1}\) in the vertex field \(Y(u,z)v\), and \(d\) includes the simplex differential. The \(u_i\) record translation homotopies. Once the two pairs \((e_i,u_i)\) are fixed, the first mixed condition asks for a primitive \(\beta\) of \(u_{1(0)}e_2\). The next asks for a primitive of \(T\beta-u_{1(0)}u_2\). Forgetting one generator forgets both mixed entries.

**Binary exterior-source theorem.** The specified comparison
\[
\rho_B:\operatorname{Map}_{\mathcal V}(A,B)\longrightarrow N(B)
\]
is an equivalence for every ordinary algebraic dg vertex algebra \(B\), with arbitrary translation, no commutativity assumption and no boundedness assumption. [Logarithmic quotient construction](#ref-ch07-07).

A map on the six generators must respect the pole orders of their pairwise vertex products. For a given tuple these orders have finite bounds, which can vary with the tuple. Let \(F_m\) be the free stage on the six generators with the displayed differentials and with locality bounds increasing with \(m\). Each finite tuple defines a map from a sufficiently large stage. To evaluate a derived map from \(A\), one also needs stages mapping by state quasi-isomorphisms to \(A\). The decisive construction supplies ordinary quotients \(R_m\) with specified state quasi-isomorphisms \(R_m\to A\) and strict factorizations
\[
F_{m+2}\longrightarrow R_{m+2}\longrightarrow F_m
\]
of the actual free transition. The tuple gives a vertex map \(F_m\to B\). Composing it with \(R_{m+2}\to F_m\) gives the right leg \(R_{m+2}\to B\). The quotient's state quasi-isomorphism \(R_{m+2}\to A\) is the left leg. Together they give a roof \(A\xleftarrow{\sim}R_{m+2}\to B\). The factorization of the transition is strict, so this comparison also transports homotopies and finite diagrams after increasing \(m\). The free stages alone have no such quasi-isomorphism requirement. In the logarithmic quotient, the restricted dual differential combines de Rham differentiation with collision residues. Finite colour filtrations and a tensor resolution with \(dt=yx-xy\) leave ordered polynomial words in each charge. The subsequent Lie and symmetric-state constructions give the four exterior classes of \(A\).

For \(B=\mathbb C\), this theorem can be calculated directly. Translation and every zeroth product vanish. The three degree-zero coordinates \(u_1,u_2,\beta\) are closed polynomial functions on a simplex, hence constant. The coordinate \(\zeta\) vanishes because polynomial forms have no negative degree. Each \(e_i\) is a closed one-form, and its simplicial cocycle space is \(K(\mathbb C,1)\), a connected space with additive fundamental group \(\mathbb C\) and zero higher homotopy groups. Thus
\[
\operatorname{Map}_{\mathcal V}(A,\mathbb C)
\simeq\mathbb C^3_{\mathrm{disc}}\times K(\mathbb C^2,1).
\]
There is only one strict graded algebra map \(A\to\mathbb C\), yet the derived mapping space has these additional components and loops. They are the homotopy data carried by roofs, not further choices of the images of the degree-one generators in degree one of \(\mathbb C\).

### A finite number of exterior generators {#ch07-finite-exterior-sources}

With three generators one can solve the equations for each pair and still have a compatibility to impose on the triple. Write \(z_i=e_i,\ w_i=u_i\), and use \(b_{ij},v_{ij}\) for the entries \(\beta,\zeta\) of the ordered pair \(i<j\). Put \(L_i=(w_i)_{(0)}\) and \(V_{12}=(v_{12})_{(0)}\). The two expressions
\[
A=L_1b_{23}-L_2b_{13}+V_{12}z_3,\qquad
B'=L_1v_{23}-L_2v_{13}-V_{12}w_3
\]
satisfy \(dA=0\) and \(dB'=TA\). To see the first cancellation, differentiate the two terms with \(b\). Their difference contributes the commutator \([L_1,L_2]z_3\). The zero-mode Jacobi identity and \((Ta)_{(0)}=0\) give \([d,V_{12}]=-[L_1,L_2]\), which cancels it. Differentiating \(B'\) with the same identities leaves \(TA\). In the pair-only source, a closed logarithmic residue functional takes value one on \(A\), so the pair equations leave a nonzero class. The ternary top \(c\) and its translation companion \(s\) supply the missing primitives, with \(dc=A\) and \(ds=Tc-B'\).

**Theorem (finite exterior sources).** Let \(A_r=\Lambda(\epsilon_1,\ldots,\epsilon_r)\) with \(r\geq1\) finite, all generators of degree one, and differential and translation zero. In the ordinary algebraic localization above, \(\operatorname{Map}_{\mathcal V}(A_r,X)\) is represented by the following tuples in \(X\otimes\Omega_\bullet\), for every ordinary dg vertex target \(X\). Choose the order \(1,\ldots,r\). For each nonempty subset \(I\) take two entries \(a_I,s_I\) of degrees \(2-|I|,1-|I|\), respectively, and put \(L_I=(s_I)_{(0)}\). Sum over decompositions \(I=P\sqcup Q\) into nonempty blocks with \(\max I\in Q\). Let \(\varepsilon(P,Q)\) be the sign of listing \(P\), then \(Q\), in their increasing orders. The equations are
\[
\begin{aligned}
 d a_I&=\sum_{P,Q}\varepsilon(P,Q)L_Pa_Q,\\
 d s_I&=T a_I-\sum_{P,Q}\varepsilon(P,Q)(-1)^{1-|P|}L_Ps_Q .
\end{aligned}
\]
Singletons have empty sums. For \(I=\{1,2\}\) the only split allowed is \(\{1\}|\{2\}\), so the two equations give the terms \(u_{1(0)}e_2\) and \(T\beta-u_{1(0)}u_2\) of the binary calculation. For \(r=3\) they give exactly the fourteen entries above, including \(c,s\). For \(X=\mathbb C\) only the \(r\) singleton companions and \(\binom r2\) pair tops can be constants of degree zero. The singleton tops give closed one-forms on the simplex. This computes
\[
\operatorname{Map}_{\mathcal V}(A_r,\mathbb C)
\simeq \mathbb C_{\mathrm{disc}}^{\,r+\binom r2}\times K(\mathbb C^r,1).
\]

The general source comparison uses strict transition factorizations through logarithmic quotients as in the binary case. One can see why the quotient has the correct cohomology in every charge. In its tensor-word resolution write each subset letter as the decreasing sequence of its labels and filter by inversion number. For a fixed resulting word the leading differential cuts at one of its strict descents. The possible retained descents form a cube with unit coefficients on its edges and opposite signs around each square. Choosing one descent contracts that entire summand. Only the increasing words remain, one polynomial monomial in each multicharge. The Lie and symmetric-state constructions then give the exterior augmentation on the singleton states. Finiteness of the alphabet also lets one choose a single locality bound for a lifted simplex. A boundary actor with an independent spectator field has additional tensor-source refinement conditions, as the Heisenberg example illustrates.

### The genuine Heisenberg action of one exterior generator {#ch07-genuine-heisenberg-fibre}

Take the nonzero-level Heisenberg vertex algebra \(H=V_\kappa\), normalized by \(J_{(1)}J=\kappa\mathbf1\). To act on a current state, an exterior source \(B=\Lambda(\epsilon)\), with \(|\epsilon|=1\) and \(d\epsilon=T\epsilon=0\), now has a second input from \(H\). Put \(X=B\otimes H\). Restriction along the map \(j:H\to X\) given by \(j(h)=1\otimes h\) must recover the identity of \(H\), with its specified path. In the same ordinary dg vertex localization the comparison therefore has target the genuine unit fibre
\[
q_B:N\operatorname{Act}_{\mathrm{roof},H}(B)\longrightarrow F,
\qquad
F=\operatorname{hofib}_{\mathrm{id}_H}
\bigl[\operatorname{Map}(B\otimes H,H)
\longrightarrow\operatorname{Map}(H,H)\bigr].
\]
The source is the nerve \(N\) of the category of action roofs. Its points are described below, its edges are maps of the two resolutions respecting the action, and composable edges give its higher simplices. The maps of the two resolutions commute with their structure maps and with the action. All boundary arrows under \(H\), including energy-changing arrows, enter the comparison.

A roof consists of a degreewise surjective state quasi-isomorphism \(p:P\to B\), an admissible state quasi-isomorphism \(i:H\to W\), and a vertex map \(c:P\to\operatorname{Com}(W)\). The actor resolution \(P\) can be unbounded. Admissibility on the boundary requires a bounded-below direct-sum energy grading on \(W\) preserved by \(i,d\), with \(E(a_{(n)}b)=E(a)+E(b)-n-1\) on homogeneous products and locally nilpotent \(i(J)_{(0)}\). The commutant consists of states killed by all nonnegative modes of \(i(J)\). The two commuting images give \(a(x\otimes h)=c(x)_{(-1)}i(h)\). Inverting \(i\) and \(p\otimes1\) gives the value \(i^{-1}a(p\otimes1)^{-1}\) of \(q_B\) on this roof. On \(1\otimes h\) the map \(a\) restricts precisely to \(i\). This supplies the unit path and explains why a change of resolution must respect both legs.

First distinguish the components of the roofs. Represent the map by \(X\xleftarrow{p}S\xrightarrow f H\) with \(p\) a surjective state quasi-isomorphism. Lift \(\epsilon\otimes1\) to a closed \(e\). Since \(p(Te)=0\) and \(\ker p\) is acyclic, choose \(u\in\ker p\) with \(du=Te\). Another closed lift has the form \(e+dv\) with \(v\in\ker p\). Its translation has primitive \(u+Tv\), and any other primitive in \(\ker p\) differs from this one by a boundary. Boundaries vanish in the state complex of \(H\), which is concentrated in degree zero. Thus changing the lifts changes \(f(u)\) by \(Tf(v)\), and its class in \(H/TH\) is well defined. It has the form \((\mathrm{ch}/\kappa)[J]+\mathrm{ct}[\mathbf1]\), where \(\mathrm{ch}\) is the charge and \(\mathrm{ct}\) the constant. For a genuine action roof, the scalar first self-product of the translation primitive is \(\kappa(\mathrm{ch}/\kappa)^2\), twice the quadratic self-linking of the action.

A loop has a scalar of its own. Integrate the one-form coefficient of its state homotopy over the parameter interval, evaluate on \(\epsilon\otimes\mathbf1\), and take the energy-zero vacuum coefficient. The scalar loop with form \(\mu\,ds\) gives \(\mu\). Together these operations define \(\Pi:F\to\mathbb C^2_{\mathrm{disc}}\times K(\mathbb C,1)\), and \(\Pi q_B\) is a weak equivalence. This computes the space of roofs. There could still be further components or loops in the target fibre \(F\).

For a point of \(F\), choose a roof whose charge and constant are the negatives of its two labels. Translating by these roofs gives
\[
F\simeq\mathbb C^2_{\mathrm{disc}}\times F^0,
\]
where \(F^0\) is the whole fibre over the pair \((0,0)\). To compare its components, use the exterior coproduct \(\Delta\epsilon=\epsilon\otimes1+1\otimes\epsilon\). A pointed action \(\alpha:X\to H\) has a specified path \(\alpha j\simeq1_H\). Set \(C_\alpha=(1_B\otimes\alpha)(\Delta\otimes1_H):X\to X\). For a roof \(X\xleftarrow{p}S\xrightarrow{f}H\) with \(p\) a surjective quasi-isomorphism, \(C_\alpha\) is represented by the pullback of \(1_B\otimes p\) along \(\Delta\otimes1_H\), followed by \(1_B\otimes f\). Its left leg is a surjective quasi-isomorphism. On state cohomology \(\alpha\) fixes \(1\otimes H\) and kills \(\epsilon\otimes H\), since \(H\) is concentrated in degree zero. The primitive formula for \(\Delta\epsilon\) gives \(H^\bullet(C_\alpha)=1\) on both summands of \(H^\bullet(X)\), so the right leg is a quasi-isomorphism too.

The given path identifies \(C_\alpha j\simeq j\alpha j\) with \(j\). Thus \(C_\alpha\) is an equivalence under \(H\). For another pointed action \(\beta:X\to H\), right convolution by \(\alpha\) is \(\beta\mapsto\beta C_\alpha\). The coproduct first makes two actor inputs, \(\alpha\) acts with the second, and \(\beta\) acts with the first. The trivial action applies the exterior counit to its actor input, so its convolution with \(\alpha\) is \(\alpha\). Since \(C_\alpha\) is an equivalence under \(H\), this translation is an equivalence of \(F\). Every right translation on \(\pi_0F\) is bijective, so \(\pi_0F\) is a group. At the homotopy unit, interchange of loop concatenation and convolution makes \(\pi_1\) abelian, and its action on higher homotopy is trivial. Right translation carries these conclusions to every component.

Which automorphisms could escape the scalar-loop measurement? Form the square-zero extension
\[
X_1=H\oplus\epsilon_1H,
\qquad |\epsilon_1|=1,
\quad \epsilon_1^2=d\epsilon_1=T\epsilon_1=0,
\]
with its canonical section and projection. Work in the genuine pointed slice \(\mathcal V_{H//H}\), which retains both the under-\(H\) and over-\(H\) homotopies. Let \(U\) be the space of its automorphisms of \(X_1\) that induce the identity on state cohomology. At the trivial action \(\alpha_0\), define
\[
\Phi=\operatorname{hofib}_0
\bigl[F_{\alpha_0}\xrightarrow{\delta}K(\mathbb C,1)\bigr],
\]
where \(F_{\alpha_0}\) is the connected component of \(\alpha_0\). The scalar section makes \(\Phi\) connected, and the genuine loop comparison gives
\[
U\simeq\Omega\Phi,
\qquad
q_B\text{ is an equivalence}
\Longleftrightarrow
F^0\text{ is connected and }U\text{ is contractible}.
\]
The first condition tests whether a whole component escapes the two labels. The second tests for extra automorphisms within the trivial component. Loop concatenation adds scalars and has identity \(0\). Composition of endomorphisms multiplies their detected scalars and has identity \(1\). A splitting over the scalar set alone would give no splitting for composition.

**Theorem (components of the genuine Heisenberg action space).** Over \(\mathbb C\), for the single degree-one exterior generator and the rank-one boundary \(V_\kappa\) at \(\kappa\ne0\), the original roof comparison \(q_B\) is a weak equivalence. The charge and constant give all its components. Each component has additive fundamental group \(\mathbb C\) and vanishing higher homotopy groups. Thus \(F\simeq\mathbb C^2_{\mathrm{disc}}\times K(\mathbb C,1)\).

To see how the two conditions are proved, first represent a positive-dimensional sphere at the trivial action by its square-zero correction. Scale \(\epsilon\) by a polynomial variable. Use two exterior copies and \(\epsilon\mapsto\epsilon_1+\epsilon_2\). Scaling their generators independently extracts the coefficient of \(t^2\) in any polynomial \(p(t+v)\), with \(v\) still free. For \(p(z)=z^{j+2}\) this is \(\binom{j+2}{2}v^j\). The corresponding square-zero correction vanishes on an incoming resolution. The linear coefficient map \(v^j\mapsto z^{j+2}/\binom{j+2}{2}\) then kills the entire tail of the sphere there, even when there is no uniform polynomial-degree bound on its states. The constant term factors through the marked \(H\). The linear term gives exactly the scalar for a loop and vanishes in every higher sphere degree. The scalar detector is therefore an equivalence on the trivial component, and \(U\simeq\Omega\Phi\) is contractible.

For a component, remove the realized roof with the same charge and constant by convolution with its inverse. The resulting action has zero translation class. Scaling \(\epsilon\mapsto t\epsilon\) gives a polynomial family \(f_t\) from the projection at \(t=0\) to this action at \(t=1\). To turn the family into a path of dg vertex maps, it needs a \(dt\)-term. Substitute \(t+\delta\), with \(\delta^2=0\), and compare the resulting lift with the constant lift over the *same* \(f_t\). After convolution back to the projection its translation class is \((t+\delta)[f(u)]-t[f(u)]=0\), where \(u\) is the translation primitive. On the first-charge resolution a primitive value \(Th\) is contracted by sending the lifted generator to \(-ds\,\delta h\) and its translation primitive to \((1-s)\delta Th\). The identity \((Th)_{(0)}=0\) preserves the mixed zeroth products.

On one common incoming resolution the homotopy of lifts integrates to a degree-minus-one derivation \(E\) over \(f_t\) with \(Ed=\partial_t f_t\). Now \(f_t+dt\,E\) is a dg vertex map. The derivation law supplies its mixed products, and \(dt^2=0\). Its endpoints use the same left leg and recover the two right legs with their original unit comparison. Thus every zero-label action lies in the component of the projection. Translating back realizes each action in the unique component with its measured pair. [The positive spheres and the path of actions](#ref-ch07-14).

### Several exterior generators on the Heisenberg boundary {#ch07-finite-heisenberg-actions}

Keep the same boundary and take two exterior generators. Prescribe the trivial action on each of their lines, with the paths identifying the restrictions with those actions. A primitive involving both generators can still map to a scalar multiple of the vacuum. Every scalar occurs, and two different scalars give different components. With more generators, which of these pair values can be chosen independently?

**Theorem (finite-colour exterior actions).** Let \(H=V_\kappa\) be the rank-one vacuum Heisenberg algebra over \(\mathbb C\), with \(J_{(1)}J=\kappa\mathbf1\) and \(\kappa\ne0\). Let \(V\) be finite dimensional in cohomological degree one and put \(A_V=\Lambda(V)\) with zero differential and translation. In \(\mathcal V\), the ordinary algebraic dg vertex category localized at quasi-isomorphisms of whole state complexes, let \(F(V)\) be the homotopy fibre over \(1_H\) of restriction along \(h\mapsto1\otimes h\) from \(\operatorname{Map}_{\mathcal V}(A_V\otimes H,H)\) to \(\operatorname{Map}_{\mathcal V}(H,H)\). There is a weak equivalence, natural under all linear substitutions of the generators,
\[
 F(V)\simeq
 \bigl(V^*\oplus V^*\oplus(\Lambda^2V)^*\bigr)_{\mathrm{disc}}
 \times K(V^*,1).
\]
The first two functionals are the unary charge \(\lambda\) and constant \(\beta\). For a chosen basis of \(V\), the homotopy fibre over any specified tuple of genuine actions on the coordinate lines, with paths identifying the restrictions with those actions, is weakly equivalent to the discrete space \(\big((\Lambda^2V)^*\big)_{\mathrm{disc}}\).

*Proof (finite-colour exterior actions).* Represent a marked action by a roof \(A_V\otimes H\xleftarrow{q}Q\xrightarrow f H\) with \(q\) a surjective state quasi-isomorphism. Choose closed lifts \(z_v\) of \(v\otimes1\) and \(w_v\in\ker q\) with \(dw_v=Tz_v\), linearly in \(v\). The unary calculation gives \(f(w_v)=\lambda(v)J/\kappa+\beta(v)\mathbf1+Th_v\) for some \(h_v\in H\). For two colours \(u,v\), the acyclic kernel supplies bilinear choices of the mixed primitives \(b_{uv},c_{uv}\) with
\[
 d b_{uv}=(w_u)_{(0)}z_v,\qquad
 d c_{uv}=T b_{uv}-(w_u)_{(0)}w_v .
\]
The zero mode of \(f(w_u)\) vanishes on the vacuum Heisenberg module. The second equation therefore puts \(f(b_{uv})\) in \(\ker T=\mathbb C\mathbf1\). Write \(f(b_{uv})=m(u,v)\mathbf1\). Changing the lifts changes the first primitive by a kernel boundary and terms whose image contains either this zero mode or a state of negative degree in \(H\). Along a path the class of \(f(w_u)\) modulo \(TH\) stays fixed. Its zero mode still vanishes, so the first mixed equation makes \(m(u,v)\) constant along the path.

The value on two copies of a charged colour determines the symmetric part of \(m\). In the repeated-line roof one can take \(w\) with image \(\gamma J+\beta(v)\mathbf1\), where \(\gamma=\lambda(v)/\kappa\), and mixed primitive \(b\) with \([w_\xi w]=(T+2\xi)b\). The coefficient of the bracket variable \(\xi\) gives \(2f(b)=\kappa\gamma^2\mathbf1\). Hence \(m(v,v)=\lambda(v)^2/(2\kappa)\). Polarization gives the alternating component coordinate
\[
 \omega(u,v)=m(u,v)-\frac{\lambda(u)\lambda(v)}{2\kappa}.
\]
For example, if \(\kappa=2\) and \(\lambda(v)=3\), the repeated input gives \(m(v,v)=9/4\) and \(\omega(v,v)=0\).

To see why there is no further component coordinate, write \(V=\mathbb C e\oplus W\). In the induction on the number of generators, vary \(e\) while keeping the whole spectator \(\Lambda(W)\otimes H\). A square-zero correction that vanishes on the axes gives a correction of degree one higher on this spectator. In degree zero its degree-one value on each remaining line is precisely the mixed reading with \(e\). The degree-one corrections are detected by the linear functional on the colours, and the corrections in degrees at least two are null. The null homotopy on the whole spectator and the original action lift to one common source. Applying this calculation while scaling all generators by \(t\) detects a pair value by \(((t+\delta)^2-t^2)m=2t\delta m\), where \(\delta^2=0\). With all axis actions trivial and pair values zero, the resulting null homotopy supplies the \(dt\)-term of a path from the action to the augmentation.

Ordered convolution extends specified unary actions. Convolution on the right with a mixed action trivial on the axes adds any prescribed alternating form. A loop is evaluated on \(v\otimes\mathbf1\) followed by the vacuum coefficient, giving the degree-one functional on \(V\). All higher homotopy groups vanish. Restriction identifies \(V^*\) with the product of the loop groups on the coordinate lines, so the axis fibre has no remaining loops. ∎

At three generators the action therefore has nine component coordinates, six unary and three alternating, and fundamental group \(\mathbb C^3\) at each component. Specifying the three genuine axis actions leaves precisely the three pair scalars. Specifying those as well leaves a weakly contractible fibre. The coordinate-plane calculation retains the identifications on every shared axis. [The finite-colour action and its axis fibres](reference.html#s-heisenberg-finite-colour-actions).

## Residues with spectators {#ch07-residues-with-spectators}

The Heisenberg test kept a boundary current in place while the exterior input varied. To study more general tensor-source resolutions, keep additional field insertions at labelled positions \(z_1,\ldots,z_r\). These are the **spectators**. A residue can move an auxiliary mark \(w_a\) onto one of them. Whether a form has a primitive depends on the pole orders allowed before and after that collision. Write \(b_j\ge0\) for the basic bound at spectator \(j\), \(N_{ij}\ge0\) for a pair of spectators, and \(\mu\) for the positive odd bound on marked pairs.

First keep just one spectator at \(z\). There is one moving point \(w\), with relative coordinate \(y=w-z\). If functions may have a pole of order at most \(b\geq0\), the complex is
\[
 y^{-b}\mathbb C[z,y]\xrightarrow{d_y}
 y^{-b-1}\mathbb C[z,y]\,dy\xrightarrow{\operatorname{Res}_{y=0}}
 \mathbb C[z].
\]
A Laurent monomial \(y^jdy\) has the allowed primitive \(y^{j+1}/(j+1)\) except when \(j=-1\). The missing form \(dy/y\) has residue \(1\). Thus \(dy/y\) is no longer a cycle in the three-term complex. The residue is onto, and the only cohomology that remains consists of the functions of the spectator \(z\) in degree zero. The residue uses up the moving point and records a coefficient at the spectator. This is what a *selected* spectator records in the general complex.

With two spectators a restriction on *pairs* of residues is already visible. Take one mark \(w\), set \(b_1=b_2=N_{12}=0\), and take the allowed one-form
\[
\frac{dw}{(w-z_1)(w-z_2)}.
\]
Its residues at \(z_1\) and \(z_2\) are \(1/(z_1-z_2)\) and \(1/(z_2-z_1)\). Each has a pole when the spectators meet, but their sum is zero. In the complex with fixed pole bounds, the two possible choices of a spectator must therefore be related along their collision.

**Definition (residue complex with spectators).** Fix the charge \(q=m+s\). A component is indexed by the subset \(S\subseteq\{1,\ldots,r\}\) of spectators which have absorbed a mark, with \(s=|S|\le q\). It has \(m=q-s\) remaining marked variables. A degree-\(i\) form in these variables contributes to total degree \(n=2s+i\). Each form is anti-invariant under permutations of the marks acting on both coefficients and differentials. For an increasing set of indices \(I\), write \(dw_I\) for the wedge of their differentials in that order. Its coefficient obeys the bounds
\[
\begin{array}{c|c}
\text{divisor}&\text{maximum pole order}\\ \hline
w_a=w_b&\mu+\mathbf1_{\{a,b\}\cap I\ne\varnothing}\\
w_a=z_j&b_j+\mathbf1_{a\in I}\quad(j\notin S)\\
w_a=z_j&2b_j+\mu+1+\mathbf1_{a\in I}\quad(j\in S)\\
z_i=z_j&N_{ij}\quad(|\{i,j\}\cap S|=0)\\
z_i=z_j&N_{ij}+b_i+b_j+1\quad(|\{i,j\}\cap S|=1)\\
z_i=z_j&N_{ij}+2b_i+2b_j+\mu+2\quad(|\{i,j\}\cap S|=2).
\end{array}
\]
No other poles are allowed. A total-degree-\(n\) family is \(\Phi=(\phi_S)_S\), where \(\phi_S\) is a form of degree \(n-2|S|\) in \(q-|S|\) marked variables satisfying the displayed bounds. A component is zero unless \(0\le n-2|S|\le q-|S|\). For every \(i\ne j\), \(i\in S\), \(j\notin S\), put \(S'=(S\setminus\{i\})\cup\{j\}\). The additional relation is, coefficientwise,
\[
\phi_S+\varepsilon_{S;i,j}\phi_{S'}
\quad\text{has pole order at most }N_{ij}\text{ along }z_i=z_j.
\tag{R}
\]
To define the sign, let \(\theta_1,\ldots,\theta_r\) be anticommuting symbols and write \(\theta_S\) for their product in increasing order. Using a common anticommuting symbol \(\theta\), set \(\varepsilon_{S;i,j}\in\{1,-1\}\) by
\[
\left.\theta_S\right|_{\theta_i=\theta}
=\varepsilon_{S;i,j}
\left.\theta_{S'}\right|_{\theta_j=\theta}.
\]
For \(|S|=1\), relation (R) says that \(\phi_{\{i\}}+\phi_{\{j\}}\) has pole order at most \(N_{ij}\) along \(z_i=z_j\). The relation couples the components associated with the two possible selected spectator labels.

Denote the resulting complex by \(D_{r,q}(b,N;\mu)\). The \(S\)-component of the differential, with \(m=q-|S|\), is
\[
(d\Phi)_S=d_w\phi_S+
\sum_{j\in S}(-1)^{|\{i\in S:\,i<j\}|}
 \operatorname{Res}^{L}_{w_{m+1}=z_j}\phi_{S\setminus\{j\}} .
\]
The left residue extracts \(dw_{m+1}\) first. A residue lowers form degree by one and adds a selected spectator, so both terms raise \(2s+i\) by one. Left residue anticommutes with \(d_w\), and the exterior signs of the two possible selection orders cancel their double residues.

At charge one the calculation with \(dy/y\) leaves, for several spectators, the module
\[
M_N(r)=\left(\prod_{i<j}(z_i-z_j)^{-N_{ij}}\right)
\mathbb C[z_1,\ldots,z_r].
\]
It occurs in degree zero at \(q=1\), independently of \(\mu\). For \(q\ge2\) the first vanishing range is strictly below degree \(q\). At that boundary a fixed pole bound matters.

**Strict three-spectator theorem.** For \(r=3\), every \(b_j,N_{ij}\ge0\), every positive odd \(\mu\), and every charge \(q\ge2\),
\[
H^n(D_{3,q}(b,N;\mu))=0\qquad(n<q).
\]
This holds over the whole polynomial spectator base, including simultaneous collisions, and in every homogeneity. The conclusion \(H^n=0\) for \(q\ge2\) and \(n<q\), with positive odd \(\mu\), also holds for \(r=2\) and arbitrary nonnegative \(b,N\), and for arbitrary \(r\) when every \(b_j=0\) and \(N_{ij}\ge0\). [Three-spectator proof](#ref-ch07-08).

For three spectators, filter by the selected count \(s\). The associated graded differential is marked de Rham differentiation. After taking this de Rham cohomology, the columns at \(s=0,1,2,3\) can first contribute in total degrees \(q-1,q,q,q+2\), respectively, or later. At small \(q\) some columns are absent and form degree must still be nonnegative. Only the unselected column can contribute below \(q\). Its possible degree-\(q-1\) class maps injectively under the actual first residue into the constrained one-selected column, so it disappears. The filtration is finite, which gives convergence to the original total complex without a completion argument.

**Theorem (four spectators at charge five).** For \(b=(1,1,1,1)\), \(\mu=1\) and arbitrary \(N_{ij}\ge0\), one has \(H^n(D_{4,5})=0\) for \(n<5\). With one spectator selected, four marks remain and its marked de Rham cohomology vanishes in form degrees zero through two. With two selected, antisymmetry kills the only possible zero-form class below total degree five. With three or more selected the total degree is already at least six. In the unselected column the only possible class below five maps injectively under the first residue from form degree four to form degree three of the one-selected column. [The charge-five filtration](#ref-ch07-09).

The column estimates use the images of residues and the connections on them. The spectator–spectator allowance \(N_{ij}\) can be removed explicitly from the labelled calculation. Multiplication by \(g_N=\prod_{i<j}(z_i-z_j)^{N_{ij}}\) reduces every allowed pole at \(z_i=z_j\) by \(N_{ij}\), in both terms of (R). The factor is independent of the moving marks, so it commutes with their differentiation and left residues. Division by \(g_N\) recovers the original fractional module. If two spectator labels are exchanged, however, their difference changes sign.

For a permutation \(\sigma\) preserving \(b,N\), relabel \(z_i,\theta_i\) by \(\sigma(i)\). If \(\operatorname{inv}_S(\sigma)\) counts inversions among indices in \(S\), then \(\sigma(\theta_S)=(-1)^{\operatorname{inv}_S(\sigma)}\theta_{\sigma S}\). This exterior sign and the Koszul sign of the spectator word occur on both sides of multiplication. Reversing the spectator differences gives
\[
 \sigma(g_N\Phi)=\chi_N(\sigma)g_N\,\sigma\Phi,\qquad
 \chi_N(\sigma)=(-1)^{\sum_{i<j,\ \sigma(i)>\sigma(j)}N_{ij}}.
\]
For a word with colour-dependent bounds, group positions by colour. The factors between distinct colours are then separately symmetric, while the factors within each colour are powers of a Vandermonde. Hence on the word stabilizer \(G=\prod_c S_{m_c}\) one has \(\chi_N(\sigma)=\prod_c\operatorname{sgn}(\sigma_c)^{N(c,c)}\). Multiplication identifies \(D_{r,q}(b,N;\mu)^G\) with \((D_{r,q}(b,0;\mu)\otimes\chi_N)^G\), with the original signed action on the complex in each case. Exactness of finite-group invariants over \(\mathbb C\) carries the labelled vanishing above to these repeated-colour sectors.

Can pairwise principal parts be realized by a single form when several collision divisors meet? For the simple bounds \(b_j=1,\ \mu=1,\ N_{ij}=0\), encode the \(m\) moving positions by their monic polynomial \(P\). A mark has reached spectator \(i\) precisely when \(P(z_i)=0\). The cubic powers below record these simple bounds after the collision. For \(r\ge1,m\ge0\), work in \(S=\mathbb C[z_1,\ldots,z_r,c_1,\ldots,c_m]\) and put
\[
\begin{gathered}
P(X)=X^m+c_1X^{m-1}+\cdots+c_m,\qquad t_{ij}=z_j-z_i,\\
\Delta=\prod_{i<j}t_{ij}^3,\qquad G_i=P(z_i)^3,\\
F_i=\left(\prod_{a<b,\ i\notin\{a,b\}}t_{ab}^3\right)
       \prod_{j\ne i}G_j,\qquad \mathfrak a=(F_1,\ldots,F_r).
\end{gathered}
\]
For \(m=0\), take \(P=1\). The literal identity
\[
\bigcap_{i<j}(\mathfrak a,t_{ij}^3)=(\mathfrak a,\Delta)
\]
says that compatible pairwise principal parts in the specified image modules arise from a single joint source. Its proof uses the actual coefficient lattice, whose projective dimension is at most two for \(m\ge2\), and induction along collision partitions with the outside polynomial factors retained. [First compatibility defect](#ref-ch07-10).

At \(r=4,\ b_1=\cdots=b_4=\mu=1,\ N=0\), let \(B_S\) be the image of the coefficient ideal \(\mathfrak a\) acting on the module of iterated principal parts along the collision of the labels in \(S\). For each number \(m\) of marks the signed Cousin maps give
\[
\bigoplus_{|S|=2}B_S\xrightarrow{d_1}
\bigoplus_{|S|=3}B_S\xrightarrow{d_2}
B_{\{1,2,3,4\}}\longrightarrow0,\qquad
\ker d_2/\operatorname{im}d_1=0 .
\]
Thus any relation among the four triple images at the full diagonal comes from the six pair images. At two marks the projective dimensions of these coefficient modules rule out a defect supported only at the full collision. With more marks, the only possible associated prime of a defect has a double marked root there. Factoring out the other, coprime roots reduces the calculation at that prime to the two-mark case.

Let \(C_s(m)\) denote the column with \(s\) selected spectators and \(m\) marked points, using its de Rham differential. At charge six the one-selected column has five marks. Its group \(H^3(C_1(5))\) vanishes. In the calculation with the actual coefficient images, a nonzero horizontal class would have an associated prime of height at least seven, while the resolution bounds that height by five. Using the pure, pair and triple lower bounds and the injection of the first residue, the finite filtration gives \(H^n(D_{4,6})=0\) for \(n<6\) at the four simple bounds, \(\mu=1\), and every \(N_{ij}\ge0\). [The charge-six calculation](#atlas-c-rs-019).

For arbitrary \(m\), assume the logarithmic comparison for the pure column, the quartic finite-normal bound from its Spencer complex, and the degree bounds for the actual pair and triple images. These give \(H^i(C_1(m))=0\) for \(i<m-1\). Under these hypotheses and the four-label first-residue injection, the charge-seven total at the same bounds vanishes below degree six, and
\[
H^6(D_{4,7})\simeq H^2(C_2(5)).
\]
Indeed, after the first residue kills the possible pure-column class, only the column with two selected spectators and five marks can contribute in degree six. The incoming and outgoing differentials there have zero source or target. Computing this six-component group, as well as extending the vanishing statements to arbitrary positive spectator bounds, requires more information. [The conditional charge-seven comparison](#atlas-c-rs-022).

The strict inequality cannot be replaced by \(n\le q\) at fixed bounds. With \(r=2\), \(q=4\), \(b=(1,1)\), \(N_{12}=0\) and \(\mu=1\), write \(t=z_2-z_1\). There is a class \([\Phi]\in H^4\) with \(t[\Phi]\ne0\) and \(t^2[\Phi]=0\). After identifying the fractional lattices by their common denominator, raising the spectator-pair bound by one acts by \(t\). This class survives the first increase and dies at the second. [Fixed-bound construction](#ref-ch07-11) · [Exact spectator-bound increase for the charge-four class, Theorem 4.1](#atlas-c-centre-residue-minimal-bound-increase).

## Comparing the prescribed mixed actions {#ch07-the-remaining-comparison}

The residue complex tests a source resolution. In the recognition problem the map to reconstruct is the action \(\alpha\) itself. For the two-colour coalgebra one must compare \(\alpha:F\otimes^!C_{k^2}\to C_{k^2}\) with multiplication by \(\Psi(\alpha)\), through pointed coassociative actions. Fix such an \(\alpha\), with \(F\) factorizing and its coefficient complexes possibly unbounded. In the part of the mapping complex where input and output colours disagree, take three nonempty ordered blocks \(A|B|C\), a root \(a\in A\) and marks \(b\in B,\ p\in C\). On \(Y=U_{A,B,C}\) the blocks are mutually disjoint, but positions inside one block may collide. Put \(M=(F_A\boxtimes F_B\boxtimes F_C)|_Y\), and let \(J_Y\) be the diagonal tensor unit on \(Y\). The complex for these fixed data is the homotopy fibre of
\[
\mathbf R\!\operatorname{Hom}_{\mathcal D_Y}(M,J_Y)
\xrightarrow{\,u^*\,}\mathbf R\!\operatorname{Hom}_{\mathcal D_Y}(J_Y,J_Y),
\]
where \(u^*\) restricts along the three components of the pointing. A cochain in the fibre is a pair \((x,h)\) with differential \((dx,xu-dh)\). Thus a primitive must also recover the prescribed scalar homotopy at the pointing. Insert two genuine vacuum labels into the cut \(A|BC\), both away from \(A\) and \(C\). On the face that deletes one vacuum, the deleted vacuum must also avoid \(B\). The retained vacuum may meet \(B\). The vacuum positions may coincide wherever these conditions allow, and the labels remain distinct singleton fibres of every allowed quotient. Subtract the weighted residue evaluations on the two deletion faces. Their common two-vacuum term cancels, leaving a cochain whose differential is the residue of the retained one-vacuum vertex. The action supplies a comparison homotopy from that vertex to its prescribed one-vacuum cochain. Subtract the weighted residue of this homotopy to obtain a primitive of the prescribed residue. At the pointing there is still a closed scalar discrepancy of degree minus three. The scalar unit complex has no negative cohomology, so the scalar component of the primitive can be corrected. Subtract the corrected primitive from the cochain for the original cut. This degree-minus-three cochain has differential equal to the full three-block discrepancy, including its prescribed scalar homotopy. The root \(a\) and marks \(b,p\) stay fixed. This construction uses only coassociativity. [Three-block filling](#ref-ch07-12).

For the binary comparison take two singleton inputs of different colours, with output of the second colour. They lie over \(Y_2=\{z_0\ne z_1\}\). Let \(N=(F_{\{0\}}\boxtimes F_{\{1\}})^\ell|_{Y_2}\), where \(\ell\) denotes passage to left differential modules, and let \(J_{Y_2}\) be the corresponding unit. The primitive at the first input together with the binary cut gives one degree-\(-1\) cochain \(n\). The marked mixed insertion gives another, \(\Pi\). Both have the mixed binary operation \(N\to J_{Y_2}\) as differential, so \(n-\Pi\) is closed in degree \(-1\). To prove that this difference is a boundary, suppose that the underlying \(F\) has a supplied coherent cocommutative structure compatible with its coassociative structure. The action and pointing still need only be coassociative. For these two prescribed cochains there is a primitive
\[
 P_\nu\in\mathbf R\!\operatorname{Hom}_{\mathcal D_{Y_2}}(N,J_{Y_2})^{-2},
 \qquad dP_\nu=\nu=n-\Pi ,
\]
with the endpoint restrictions at both old inputs. Extension across \(z_0=z_1\) is a further condition. [Separated-base primitive comparison](#ref-ch07-13).

Recognition for arbitrary pointed factorizing actors still asks for \(\Theta\) to be an equivalence with all changes of roots, collision restrictions and arbitrarily long refined words. The three-block filling and the separated primitive comparison provide particular coherences. For each finite exterior algebra on degree-one generators the ordinary vertex mapping space is known. An action on an independent boundary must additionally preserve the original actor, both roof legs, evaluation and the unit comparison. For one exterior generator acting on \(V_\kappa\) at \(\kappa\ne0\), [the genuine roof theorem](#ch07-genuine-heisenberg-fibre) supplies this comparison. On the same rank-one Heisenberg boundary, the [action of a finite exterior algebra](#ch07-finite-heisenberg-actions) has a discrete alternating pair parameter over the specified unary actions. A cofinal family of resolutions with prescribed strict arrows into the Heisenberg tensor-source stages would give a different proof of the unary comparison. The existence of that family is a separate interpolation question. A higher-operadic enhancement must compare its additional operations, and a nonabelian boundary requires its own calculation of the marked action space.

The existence question changes when the *boundary* changes. Replace the two-idempotent boundary by the Chevalley coalgebra of the polynomial Heisenberg state space \(k[x_1,x_2,\ldots]\), over a characteristic-zero field at \(\kappa\ne0\). Here \(J_{-n}\) multiplies by \(x_n\) and \(J_n\) acts by \(\kappa n\partial_{x_n}\) for \(n>0\). In this full category of pointed factorizing actions, every degree-zero one-root operation of a receiving action must commute with the current modes. For \(D=\partial_{x_1}\) the creation mode already gives
\[
 (DJ_{-1}-J_{-1}D)\mathbf1=D(x_1)-x_1D(1)=\mathbf1 .
\]

Indeed, if a one-root module operation \(M\) commutes with every creation mode, then \(M(f)=fM(\mathbf1)\) for every polynomial state \(f\). Commutation with every annihilation mode forces \(M(\mathbf1)\) to be constant in all the \(x_n\), since \(\kappa\ne0\). In particular the derivation \(D\), which vanishes on the vacuum and sends \(x_1\) to \(1\), cannot be such a module operation.

Take the exterior Chevalley actors on two and one degree-one generators, with the trivial action on the first and the action associated to \(D\) on the second. There are two parallel pointed maps of actions between them. One factors through \(J\), and the other has an antisymmetric two-input component and a specified homotopy to the trivial pullback action. After any map out of their target, restrict to two separated labelled roots, with one fixed and the other moving. The two terms of the antisymmetric class then have different cohomological bidegrees. Its \((1,0)\) term survives by the one-root obstruction above and the unit at the fixed root. The map through \(J\) has zero binary class. Thus the composites lie in different components for every receiving action. A representing action would be terminal, and maps into it would give a path between these composites. This proves nonrepresentability of the full pointed factorizing-action functor for this boundary. The two arrows used here preserve the pointings and action paths. Requiring arrows to preserve a multiplication on the actors changes the test.

The two parallel arrows give an algebraic obstruction to a terminal pointed action on this Heisenberg boundary. To obtain a physical obstruction, one must realize both arrows, with their action paths, by supported bulk–boundary systems. Conversely, suppose one such system is universal in a specified physical class. If supported realization induces equivalences on its full mapping spaces and its image generates the algebraic action category by small colimits, the image of that system is terminal. Indeed, maps from a generating colimit into it form a limit of contractible mapping spaces. The realization must therefore account for supports and collisions as well as the underlying field maps.

### A marked action at finite quantum precision {#ch07-marked-retained-action}

There is another way for evaluation on a vacuum to lose an operation. In the four-current complex for \(\mathfrak{gl}_2\), take the current colours \(H,E,F,I\), where \(I\) is the trace, and work modulo \(\hbar^3\) over \(R_3=\mathbb C[\hbar]/(\hbar^3)\). Besides the current states, the complex has odd ghost states. Multiplying the output of a normalized closed field by a closed trace ghost produces a degree-one class. Its scalar vacuum coefficient vanishes, but the constant term of its full value on the two vacua recovers the trace ghost itself. Acting on that same output and pairing against a dual ghost coefficient are different operations. In the pairing, a trace creator on the field acts by contraction on the dual coefficient.

Keep the ghost output as well as the current state until the last pairing. Let \(u\) denote the separation between an inserted state \(x\) and a fixed, or rooted, current input \(w\). A retained kernel assigns to \(x,w\) a Laurent series in \(u\) valued in current states and in each finite-cutoff quotient of the ghost module. On one right slice a marked coefficient is represented, for the inserted input in question, by
\[
y=\sum_{i=1}^m\left(\sum_{j\geq\nu}u^jF_{ij}\right)\otimes b_i .
\]
The \(b_i\) are a finite list of right current coefficients. Every \(F_{ij}\) uses the same middle ghost cutoff and takes values in left current coefficients. First act on \(w\) by \(b_i\), then apply the kernel at \(x\), then contract the middle ghost and act on the output by \(F_{ij}\). There are only finitely many right translates \(b_iw\), so their kernel values at this cutoff have a common lower Laurent bound \(T_0\). To form the coefficient of \(u^t\) one needs only \(\nu\le j\le t-T_0\). If the right coefficients \(b_i\) were allowed to change without bound as \(j\) varies, a lower bound for each individual translate \(b_iw\) would give no common \(T_0\). That is why the finite right support and the middle ghost cutoff are chosen for the whole series before taking its coefficient.

At noncritical level \(K\ne-2\), let \(\Phi\) be the coefficient-defined rooted kernel and \(\mathcal Y^\sharp\) the reversed retained field. Write \(i,p,k\) for the state deformation retract, with \(d_Mk+kd_M=1-ip\), and \(h^\Lambda\) for the homotopy from the ordered field \(\mathcal Y_-\) to \(\mathcal Y^\sharp\). In the Hom complex of retained kernels the primitive is
\[
H=(\Phi-\mathcal Y^\sharp)k-h^\Lambda ip,\qquad
\delta H=\Phi-\mathcal Y^\sharp .
\]
Indeed, on the image of \(ip\) the kernel \(\Phi\) agrees with \(\mathcal Y_-\). With \(\delta h^\Lambda=\mathcal Y^\sharp-\mathcal Y_-\), the differentials of the two terms of \(H\) are \((\Phi-\mathcal Y^\sharp)(1-ip)\) and \((\Phi-\mathcal Y^\sharp)ip\). The homotopy has zero scalar pairing and satisfies both translation identities. Contracting each trace-ghost entry extends \(H\) to the trace summand of the marked source. On the positive traceless inserted summand the two evaluations use the same prescribed state operation \(\mathcal J\) and the correction \(\Xi\) obtained by differentiating a source homotopy. With these inputs the comparison holds on the Laurent domain just specified. [Retained kernels](17-holographic-reconstruction.md#ch17-retained-first-root) · [The comparison in all marked degrees](17-holographic-reconstruction.md#ch17-all-retained-marked).

An independent physical comparison would have to compute \(\mathcal J+\Xi\) from the two ordered junction products. For example, insert an \(E\)-ghost at one endpoint and an \(F\)-ghost at the other. Both orders must give the prescribed maps, after their separately defined identifications of tensor factors, including the contact where insertions \(1\) and \(3\) meet with \(2\) separated and the unit on each occupied slot. Identifying a physical adjunction further requires its unit, counit and triangle identities in specified module categories. At \(K=-2\) the retained field and its rooted exchange homotopy exist. The critical algebraic state complex admits a separate translation-compatible linear model with additional generators, including the critical quadratic current. Its marked operations still require comparison on these generators. The critical comparison, the independent physical products and the extension beyond \(R_3\) are distinct open questions.

The finite list of right coefficients \(b_i\) supplied a common lower Laurent bound at a fixed middle ghost cutoff. Now consider two successive fusions, with inverse separation \(q\) and intermediate states in a vector space \(V\) over \(k\). Truncating a Laurent series after \(q^m\) leaves finitely many coefficients because its exponents are bounded below. To use the series in a second operation with domain \(V\otimes_k k((q))\), its coefficients at all orders must lie in one finite-dimensional subspace of \(V\). Can their span grow with \(m\)? [Tensor products, support and completion](08-completions.md#ch08).

## Proofs of the action and residue comparisons {#ch07-source-manuscripts}

### 1. Ordered collisions and associative chiral bar–cobar duality {#ref-ch07-01}

On the full ordered collision atlas the arity filtration uses all ordered decompositions into positive blocks. Each block consumes a label, so there are at most \(n\) of them at \(n\) labels. At two separated points both orders contribute. Keeping one word order instead retains only its consecutive cut. [The two configuration products](04-factorization.md#ordered-cut-geometry).

### 2. Recognition for every pointing on a genuine-unit Chevalley actor {#ref-ch07-02}

In *Genuine vacua contract the full fibre of an arbitrary pointing*, §6, equations (32)–(34), the term \(h_Qrh_P\) in the contraction retains the restriction \(r\) supplied by the pointing. Passing from these relative layers to the complete action space gives recognition. [The relative contraction](#ch07-recognition-on-chevalley-coalgebras) · [Arbitrary-pointing recognition](#atlas-c-binary-native-arbitrary-pointing-recognition).

### 3. Radical reduction for every pointing {#ref-ch07-03}

The all-unit projection \(P(M)\otimes^!C_V\to C_V\) carries the entire pointing to \(hu\). Equations (4) and (5) identify the two pullbacks and their compatibility with vacuum evaluation. [Module-radical pointings](#atlas-c-binary-module-radical-all-pointings-recognition).

### 4. Unitization from an ordinary horizontal representative {#ref-ch07-04}

Equation (2) compares the chain-level state \(a\) with the singleton component of the pointing by the equality \(H^0(a)=H^0(u_1)\). [The unitization theorem](#ch07-unitization-theorem).

### 5. Unitization with an arbitrary commutative connection {#ref-ch07-05}

For a quasicoherent commutative dg algebra on the affine line the connection gives the two-column de Rham complex. Its positive form-degree part has square zero. This controls the idempotent in the derived singleton even without a strict horizontal representative. [The commutative and nonunital cases](#atlas-c-ac-06).

### 6. The one-generator mapping-space theorem in every odd degree {#ref-ch07-06}

The pair \((b,b')\) records the image of the generator and the primitive of its translation. Theorem \(A_d\), equations (0.1)–(0.3), gives the mapping space and its homotopy groups. Section 7 obtains the groups by integrating relative polynomial forms on simplices, including for unbounded targets. [The odd-degree comparison](#atlas-c-centre-odd-degree-source).

### 7. An exact logarithmic quotient of the binary cell tower {#ref-ch07-07}

Sections 6–8 compute the cohomology of the logarithmic quotient. In equation (34) the transition \(F_{m+2}\to F_m\) factors through \(R_{m+2}\). A tuple gives a map from the free stage \(F_m\), while \(R_{m+2}\to A\) gives the state quasi-isomorphism on the other side of the roof. These two arrows identify the mapping space with the space of six-tuples. [The transition factorization](#atlas-c-centre-binary-ordinary-interpolation) · [The scalar target](#atlas-c-centre-binary-scalar-exhaustion).

### 8. Strict positive-degree exactness with three spectators and arbitrary bounds {#ref-ch07-08}

Sections 3–4 give the degree threshold in each of the four columns. The first residue is injective on the only possible class below total degree \(q\) in the unselected column. The statement includes simultaneous spectator collisions. [The three-spectator theorem](#atlas-c-centre-three-colour-strict-total-vanishing).

### 9. Strict lower-place vanishing at four spectators and charge five {#ref-ch07-09}

With four simple bounds and \(\mu=1\), the one-selected column has four moving marks at charge five. On the first page the possible four-form in the unselected column maps to the three-forms in this one-selected column. Injectivity of that residue removes the last possible term below degree five. [The charge-five statement](#ch07-theorem-four-spectators-at-charge-five).

### 10. The first compatibility defect for simple spectator bounds {#ref-ch07-10}

The intersection of the ideals \((\mathfrak a,t_{ij}^3)\) gives the pairwise gluing test. At four spectators the next question concerns relations among the triple images at the full diagonal. [The coefficient ideals](#ch07-residues-with-spectators) · [Exactness among the triple images](#atlas-c-rs-021).

### 11. An explicit class in \(H^4(D(2;4))\) {#ref-ch07-11}

The fixed-bound construction gives the nonzero class \(\Phi=J\omega\), where \(J\) is alternating insertion. In *Exact spectator-bound increase for the charge-four class*, Propositions 1.1 and 2.1 give \(d\psi=t^2\omega\) and \(t[\omega]\ne0\). Insertion gives \(d(J\psi)=t^2\Phi\), and extraction at infinity sends \(\Phi\) back to \(\omega\), so \(t[\Phi]\ne0\). Corollary 3.2 and Theorem 4.1 give the exact annihilator \((t^2)\) and the first zero transition. [The bound transitions](#atlas-c-centre-residue-minimal-bound-increase).

### 12. Vanishing of the actual middle-block residue {#ref-ch07-12}

With the root and two marks fixed, apply the weighted residue with its base connection and the unweighted normal residue to the specified one-vacuum cochain of the action. Proposition 2, equations (35)–(36), gives primitives of these two images in the pointed fibre, of degrees minus three and minus four respectively. Equations (42)–(48) carry the weighted primitive to the original scalar pointing of the three-block boundary. Collisions inside each block are allowed. [The three-block mapping complex](#ch07-the-remaining-comparison).

### 13. Two closed ends of a middle insertion {#ref-ch07-13}

Equations (4), (7) and (8) follow the difference \(\nu\) of the two prescribed mixed primitives to its primitive \(P_\nu\) and its corner restriction. The exchange used in the construction requires coherent cocommutativity on the actor over the separated base. [The separated-base comparison](#ch07-the-remaining-comparison).

### 14. Components of the genuine Heisenberg action space {#ref-ch07-14}

*The cubic coefficient and the full pointed Heisenberg fibre*, equations (4)–(8), computes the positive spheres by scaling the generator with its marked spectator in place. *Components of the genuine Heisenberg action space*, equations (8)–(10), integrates the homotopy over the polynomial family to give the path on components. Both arguments use the maps of the original action roofs. [The action space and its unit fibre](#ch07-genuine-heisenberg-fibre).
