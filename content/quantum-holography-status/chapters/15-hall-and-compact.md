# Hall geometry and compact states

Fix the middle object in an extension. What is left to sum over? Take a plane \(M=\mathbb F_3^2\) and ask for a subspace \(B\) such that both \(B\) and \(M/B\) are lines. The eight nonzero vectors of \(M\) come in pairs \(v,-v\) spanning the same line. There are four choices for \(B\). Each gives a split exact sequence
\[
 0\longrightarrow B\longrightarrow M\longrightarrow M/B\longrightarrow0 .
\]
Thus even when the two incident objects and the isomorphism class of their extension are fixed, the middle object contains four possible subobjects. Giving each weight one gives the Hall coefficient \(4\).

Keep one of these lines for a moment. From \((M,B)\) we can read the ordered pair \((M/B,B)\), on which the two input weights are evaluated. We can also forget the line and remember just \(M\), the argument of the product. Summing the input weights over all four lines answers the [question about intermediate objects at a junction](#ch14-a-symplectic-boundary-and-the-next-geometric-comparison) in this elementary category. The same two maps make sense for sheaves, whose subobjects can vary in a positive-dimensional variety. For two distinct simple sheaves on a K3 surface, reversing the prescribed factors can leave an empty fibre above the same middle sheaf. [The order of two simple factors](#ch15-order-of-two-k3-factors)

## Extensions and the reason for associativity {#ch15-extensions-and-the-reason-for-associativity}

**Definition (Hall correspondence).** Let \(\mathcal M_\alpha\) be the moduli stack of objects of charge \(\alpha\) in an abelian category. A charge is an additive class, such as a class in a Grothendieck group. Let \(\mathcal E_{\alpha,\beta}\) classify pairs \(B\subset M\) with quotient of charge \(\alpha\) and subobject of charge \(\beta\). Keeping the two factors, or keeping the middle object, gives the two maps
\[
\mathcal M_\alpha\times\mathcal M_\beta
\xleftarrow{\ p\ }\mathcal E_{\alpha,\beta}
\xrightarrow{\ q\ }\mathcal M_{\alpha+\beta},
\qquad
p(M,B)=(M/B,B),\quad q(M,B)=M.
\]
For rational, isomorphism-invariant constructible functions \(f,g\) of finite charge support over \(\mathbb C\), pull their product back along \(p\) and integrate over the fibre of \(q\). The ordinary Hall product at \(M\) is
\[
(f*g)(M)=\int_{B\subset M}f(M/B)g(B)\,d\chi_c.
\tag{15.1}
\]
On a domain with constructible subobject varieties, stratify the fibre into finitely many pieces on which \(f(M/B)g(B)\) has constant value. Multiply each value by the compactly supported Euler characteristic of its piece and add. The indicator of the zero object is the unit. The order in (15.1) is quotient first, subobject second.

Over \(\mathbb F_q\) the weights are summed by finite counting. Write \(e_1\) for the indicator of a one-dimensional vector space. In a plane the fibre over \(M\) is the projective line, and the common weight of its points is one. Dividing the number of nonzero vectors by the number of generators of a given line gives
\[
(e_1*e_1)(\mathbb F_q^2)
=\#\mathbb P^1(\mathbb F_q)
=\frac{q^2-1}{q-1}=q+1 .
\]
For the complex product (15.1), decompose the same projective line into an affine line and a point. Both pieces have compactly supported Euler characteristic one. The coefficient is now \(2\). In either calculation the middle object is a single plane.

Associativity has the same explanation one dimension higher. Either bracketing of three one-dimensional factors counts flags
\[
0\subset V_1\subset V_2\subset\mathbb F_q^3,
\qquad \dim V_i=i.
\]
There are \(q^2+q+1\) choices of a line and \(q+1\) planes through it, hence
\[
(e_1*e_1)*e_1=e_1*(e_1*e_1),
\qquad
\text{value on }\mathbb F_q^3=(q^2+q+1)(q+1).
\]
On a flag \(U\subset V\subset M\), put \(f\) on \(M/V\), \(g\) on \(V/U\) and \(h\) on \(U\). In \(f*(g*h)\) first choose \(V\subset M\), then choose \(U\subset V\). In \((f*g)*h\) first choose \(U\subset M\), then lift a subobject of \(M/U\) to \(V\). In both integrals the flag carries the weight \(f(M/V)g(V/U)h(U)\). This identification of the two iterated correspondences also works for sheaves. Base change and composition of pushforwards give associativity on the stated constructible domain. With complexes as coefficients, the two maps on this common flag must agree up to the prescribed homotopy. [Critical coefficients on an extension](#ch15-critical-coefficients-and-orientation)

::: figure fig-hall-correspondence

## One loop on finite root jets {#ch15-one-loop-on-finite-root-jets}

Interchanging the identical factors \(e_1,e_1\) could never tell us which input was the subobject. Give one factor a variable instead. For a quiver with one vertex and one loop, the Hall algebra has a polynomial presentation over \(R=\mathbb Q[\hbar]\). A charge-\(m\) class is a symmetric polynomial in \(m\) variables, called roots, so \(A_m=R[x_1,\ldots,x_m]^{S_m}\) and \(A_0=R\). Here the shuffle convention puts the **subobject first**. For \(f\in A_p,\ g\in A_q\), choose the roots of the subobject, indexed by \(I\), and give the remaining roots, indexed by \(J\), to the quotient. Sum over \(I\sqcup J=\{1,\ldots,p+q\}\), \(|I|=p\), the expressions
\[
 f(x_I)g(x_J)\prod_{i\in I,\,j\in J}
 \left(1+\frac{\hbar}{x_i-x_j}\right).
\]
The sum is a symmetric polynomial. In charge two let \(s\) interchange \(x,y\) and put \(u=x-y\). The two choices of the first root send an ordered polynomial \(f\) to \(f+sf+\hbar(f-sf)/u\). The numerators for \(f=x\) and \(f=y\) are respectively \(u\) and \(-u\). Thus \(x*1_1=x+y+\hbar\) and \(1_1*x=x+y-\hbar\), where \(1_1\) is the constant polynomial in charge one. At \(x=y=0\) the two answers differ by \(2\hbar\). For \(f=1\) the two shuffle terms are \(1+\hbar/u\) and \(1-\hbar/u\). Their sum is the constant polynomial \(2\), so \(1_1*1_1\) has value \(2\) even at the origin. The scalar unit of the algebra lies in charge zero.

Evaluation at the origin reads the constant term. To read the coefficient of \(x^i\) instead, apply the \(i\)th derivative at the origin and divide by \(i!\). Both readings ignore every term above a fixed degree. This finiteness will matter when a functional on the output of a product is pulled back to its two inputs.

**Definition (finite root jet).** An element of \(W_m\) is an \(R\)-linear functional on \(A_m\) which kills every homogeneous root degree above some finite bound. In charge one \(J_i(f)=\partial_x^i f(0)\). In charge two write \(J_0^2(h)=h(0,0)\). Its transpose under the merge acts on \(f\otimes g\) by \(J_0^2(f*g)\). On \(x*1_1,\ 1_1*x,\ 1_1*1_1\) it gives \(\hbar,-\hbar,2\), respectively.

The jets have cochain degree zero. In the [cobar algebra](#ch05-cobar-reverses-the-construction) \(\Omega(W)\), write \(uw\) for the shifted generator attached to a positive-charge jet \(w\). Transposing the merges of two positive charges gives the reduced coproduct \(\bar\Delta w=\sum w'\otimes w''\). The cobar differential is \(d(uw)=-\sum(uw')(uw'')\) in these generators. Use the degree-one letters \(x(w)=-uw\) for the Hall calculation. Their differential is then \(d x(w)=\sum x(w')x(w'')\). Let \(S_R\) be the zero-differential associative algebra on \(a_i\), \(i\ge0\), in degree and charge one. Its relations are the coefficients of
\[
 (z-w+\hbar)a(z)a(w)=(w-z+\hbar)a(w)a(z),
 \qquad a(z)=\sum_{i\ge0}a_i z^i.
\]
**Theorem (the one-loop cobar on finite root jets).** The augmented algebra map
\[
 F_R:\Omega(W)\longrightarrow S_R,\qquad
 x(J_i)\longmapsto i!\,a_i,\qquad
 x(w)\longmapsto0\quad\text{if \(w\) has charge greater than one}
\]
is a quasi-isomorphism in every charge over \(R\). The derivative at the origin is \(i!\) times the coefficient of \(x^i\). For an input monomial of total root degree \(d\ge2\), the two terms \(f+sf\) and \(\hbar(f-sf)/u\) both vanish at the origin because their degrees are \(d\) and \(d-1\) whenever they are nonzero. Thus only the constant and the two linear inputs contribute to \(\bar\Delta J_0^2\). Their evaluations give \(2J_0\otimes J_0+\hbar(J_1\otimes J_0-J_0\otimes J_1)\). Substituting \(x(J_0)\mapsto a_0\) and \(x(J_1)\mapsto a_1\) in the cobar differential gives \(2a_0^2+\hbar(a_1a_0-a_0a_1)\) before imposing the target relations. This is the coefficient of \(z^1w^0\) in the difference of the two sides of the exchange relation, so it vanishes in \(S_R\). The scalar unit maps to the scalar unit.

Why is finite support preserved by a contracting homotopy? In charge \(m\) use the adjacent operators
\[
 T_i f=s_i f+\hbar\,\frac{f-s_i f}{x_i-x_{i+1}}
\]
on ordered polynomials. They satisfy the symmetric-group relations. In the three-variable braid identity the common denominator reduces the comparison to \(ab=c(a+b)\) for \(a=\hbar/(x-y)\), \(b=\hbar/(y-z)\), \(c=\hbar/(x-z)\). Symmetrizing with these operators gives precisely the shuffle merge, with each shuffle counted once. Concretely, if two neighboring blocks merge and their permutation subgroup grows from \(H\) to \(J\), the operator on \(H\)-invariants is \(|H|^{-1}\sum_{w\in J}T_w\).

The resulting bar complex is the signed complex of ordered set partitions tensored over \(\mathbb Q[S_m]\) with these polynomial coefficients. A partition with \(k\) blocks gives a flag of its \(k-1\) proper prefix unions. Deleting the \(i\)th prefix merges blocks \(i\) and \(i+1\). For \(m\ge2\) these flags are the augmented simplices in the subdivided boundary of an \((m-1)\)-simplex. Its sole homology is the orientation line at word length \(m\). Averaging a rational contraction onto this line makes it equivariant. Each coefficient of the resulting contraction is a rational combination of \(T_w\). A reduced expression for \(w\) uses at most \(\binom m2\) divided differences, each lowering root degree by at most one. The transposed contraction therefore sends a jet of order at most \(D\) to a jet of order at most \(D+\binom m2\), over \(R\) itself. At top length the boundaries insert a charge-two split into neighboring letters. Their span is exactly the exchange ideal, so \(H^m(\Omega(W)_m)=(S_R)_m\) and all other degrees vanish. In charges zero and one the map is already an isomorphism of complexes.

The map preserves the root power sums, the charge and the translation \(Ta_i=(i+1)a_{i+1}\). Hence it preserves \(Y(a,z)b=(e^{zT}a)b\), which is regular in \(z\). In the calculation \(u=x-y\) was a difference of internal roots. A pole at the difference of *support positions* would have to be carried by a coefficient on the collision locus. To compare it with boundary fusion we need a map from the oriented extension correspondence to that coefficient.

## A faithful ordinary comparison on a K3 surface {#ch15-a-faithful-ordinary-comparison-on-a-k3-surface}

A representation can satisfy all the Hall relations and still kill a nonzero Hall word. To test faithfulness, compare the flags themselves. We need a category of sheaves in which every flag with the prescribed simple quotients can also be read as a flag of quiver modules. Start by putting the simple sheaves in one abelian category of semistable sheaves. This requires a common reduced Hilbert polynomial, the Hilbert polynomial divided by its leading coefficient. Choose a smooth projective complex K3 surface \(S\) with an ample polarization \(H\), \(H^2=8\), and divisor classes \(D_1,D_2,D_3,V\) whose Néron–Severi lattice has matrix
\[
\begin{pmatrix}
-8&-4&-4&1\\
-4&-8&-4&1\\
-4&-4&-8&2\\
1&1&2&0
\end{pmatrix},\qquad H=D_3+4V.
\]
The lattice has signature \((1,3)\), and \(H^\perp\) contains no class of square \(-2\). The period construction supplies a surface with this ample class. Put \(L_i=\mathcal O_S(D_i)\). Since \(H\cdot D_i=0\) and \(D_i^2=-8\), Riemann–Roch gives \(\chi(L_i(mH))=2+(D_i+mH)^2/2=4m^2-2\) for each \(i\). All three line bundles are \(H\)-Gieseker stable.

For \(i\ne j\), a nonzero section of \(L_i^\vee\otimes L_j\) would make \(D_j-D_i\) effective. This nonzero class has zero intersection with the ample class \(H\), so there is no such section in either order. Serre duality identifies \(\operatorname{Ext}^2(L_i,L_j)\) with \(\operatorname{Hom}(L_j,L_i)^\vee\), which also vanishes. The matrix gives \((D_j-D_i)^2=-8\). Riemann–Roch now gives \(-\dim\operatorname{Ext}^1(L_i,L_j)=2-4=-2\). Including the diagonal groups gives
\[
\dim\operatorname{Ext}^\bullet(L_i,L_i)=(1,0,1),
\qquad
\dim\operatorname{Ext}^\bullet(L_i,L_j)=(0,2,0)\quad(i\ne j).
\]
Let \(\mathcal A_L\) consist of the zero object and the sheaves admitting a finite filtration with factors among the \(L_i\). Work in the abelian category of semistable sheaves of this fixed reduced Hilbert polynomial. Subquotients there of objects of \(\mathcal A_L\) again have filtrations by the \(L_i\), so they too are vector bundles.

The surface and polarization are part of this construction; arbitrary triples of spherical bundles need not have the same reduced Hilbert polynomial. [A common-polynomial spherical triple][k3-triple]

::: example {#ch15-order-of-two-k3-factors title="The order of two simple factors on K3"}
Take \(i\ne j\) and a nonzero class \(\xi\in\operatorname{Ext}^1(L_i,L_j)\). Its extension has the form
\[
 0\longrightarrow L_j\longrightarrow M_\xi
   \longrightarrow L_i\longrightarrow0 .
\]
Can the same middle object be formed in the opposite order? Applying \(\operatorname{Hom}(L_i,-)\) shows what a reversed flag would require. The connecting map sends the identity of \(L_i\) to \(\xi\), so no nonzero scalar multiple of the identity lifts. Since \(\operatorname{Hom}(L_i,L_j)=0\), this gives \(\operatorname{Hom}(L_i,M_\xi)=0\). Applying \(\operatorname{Hom}(L_j,-)\) instead gives \(\operatorname{Hom}(L_j,M_\xi)=\mathbb C\), spanned by the inclusion. Every nonzero multiple has the same image. With \(e_i=1_{[L_i]}\) and the quotient-first convention (15.1), the two fibres are a point and the empty set. Hence
\[
 (e_i*e_j)(M_\xi)=1,\qquad (e_j*e_i)(M_\xi)=0 .
\]
On \(L_i\oplus L_j\) both products take the value one. There is a further distinction even among the nonsplit objects. Changing bases at the two simple ends multiplies \(\xi\) by a nonzero scalar. Any isomorphism between two such middle objects must preserve their unique subobject of type \(L_j\), so their isomorphism classes are parametrised by \(\mathbb P\operatorname{Ext}^1(L_i,L_j)\simeq\mathbb P^1\). A flag in \(M_\xi\) with simple successive quotients has length two and these two factors. All the other words in simple indicators vanish on this family. Thus every function in the ordinary algebra generated by the three simple indicators is constant on this projective line of nonisomorphic sheaves.
:::

The two-dimensional space of extensions from \(L_i\) to \(L_j\) suggests two arrows between each pair of vertices. Choose two arrows \(a:i\to j\) for \(i<j\) and add their reverse arrows. A representation assigns spaces \(V_i\) to the vertices and maps \(X_a:V_i\to V_j\), \(Y_a:V_j\to V_i\) to each such pair of arrows. At vertex \(i\) impose the preprojective relation
\[
 \sum_{a\ {\rm ending\ at}\ i} X_aY_a
 -\sum_{a\ {\rm starting\ at}\ i} Y_aX_a=0
 \quad\text{in }\operatorname{End}(V_i).
\]
Complete the resulting path algebra at its arrow ideal \(J\) to obtain \(\widehat\Pi\). The objects to compare with sheaves are finite-dimensional left modules \(M\) with \(J^NM=0\) for some \(N\). Only paths of length less than \(N\) can act on such a module.

**Definition (composition subalgebra).** In each ordinary Hall algebra take the unital algebra generated by the indicators of the three simple objects. These are \(\mathcal C_\Pi\) and \(\mathcal C_L\), graded by the three multiplicities in a composition series. A word in the indicators evaluates on a middle object by integrating over its flags with the prescribed sequence of simple quotients. This is the family of functions compared by the theorem.

**Theorem (ordinary K3 Hall comparison).** Choose the simultaneous cyclic minimal \(A_\infty\) model of the collection and a comparison with its Dolbeault category strictly unital over the quiver vertex-idempotent algebra \(\mathbb C^3\). There is a unique unital, charge-graded isomorphism
\[
\Theta:\mathcal C_\Pi\xrightarrow{\sim}\mathcal C_L
\]
sending the simple indicator at vertex \(i\) to \(1_{[L_i]}\). At every finite nilpotence bound it comes from an algebraic tensor family. Over reduced bases this family identifies reduced relative flag varieties, their subquotients, and all forgetting and regrouping maps. [Primitive recognition, Proposition “Regular families and the ordinary composition algebra”][ordinary-hall]

To pass from sheaves to these quiver equations we must rule out relations involving three or more arrows. The minimal model has zero differential, and \(m_k\) has degree \(2-k\). For an operation \(m_k\) with \(k\ge3\), a degree-zero input is a vertex unit, so strict unitality kills the operation. A degree-two input with the remaining inputs positive would force the output above degree two. If every input has degree one, the output has degree two. Pair it with any degree-zero vertex unit. Cyclicity moves that unit into an input of \(m_k\), where strict unitality kills the term. The perfect cyclic pairing then forces the output itself to vanish. The remaining quadratic equation is precisely the preprojective moment relation.

At nilpotence bound \(N\), the comparison applied to a module involves only paths shorter than \(N\). Applied to the regular module of \(\widehat\Pi/J^N\), it gives an algebraic bundle with a right action of that finite-dimensional algebra. Tensoring this bundle with a module family preserves exact sequences and base change. The resulting flag comparison makes every Hall word have the same value on corresponding objects. The two word-evaluation maps therefore have the same kernel, which proves faithfulness as well as surjectivity.

An independent action on completed Enriques cycle states satisfies the six real Serre relations \((\operatorname{ad}e_i)^3e_j=0\) for \(i\ne j\), where \(\operatorname{ad}e_i\) is commutation with the \(i\)th generator. These relations allow the representation on states to have a kernel. Faithfulness of \(\Theta\) follows instead from the comparison of all flag integrals.

## Critical coefficients and orientation {#ch15-critical-coefficients-and-orientation}

On the K3 surface a flag contributed an Euler characteristic to (15.1). On a Calabi–Yau threefold the self-extension complex gives a local deformation problem that can be presented as the critical locus of a function \(f\) on a smooth space. As a nearby fibre approaches the critical value, some of its cohomology disappears. The vanishing-cycle complex retains these classes and their degrees. An Euler characteristic would keep only their alternating sum. One now has to transport a *complex* along an extension, and even the sign of its gluing map matters.

**Definition (orientation root).** To glue these coefficient complexes, fix a line \(J_F\) on the moduli problem with an isomorphism from its tensor square to the self-extension determinant at \(F\). Write
\[
K_F=\det R\operatorname{Hom}(F,F),\qquad
D(F,G)=\det R\operatorname{Hom}(F,G),\qquad
J_F^{\otimes2}\simeq K_F.
\]
Already for a split extension the root map takes \(J_F\otimes J_G\otimes D(F,G)\) to \(J_{F\oplus G}\). Its square is the determinant identification for the direct sum. For a flag the corresponding maps must be compatible on exact triangles. Taking only an Euler-characteristic sign loses the cross determinant line \(D(F,G)\) that occurs in these maps.

Write \(\mathscr P_\alpha\) for the resulting oriented vanishing-cycle complex in charge \(\alpha\). On an extension \(B\subset M\), the inputs are the complexes belonging to \(M/B\) and \(B\), in the order of (15.1). To integrate their contribution at \(M\) one first needs a map of coefficients on this very extension. In the notation of the two Hall projections it has the form
\[
p^*(\mathscr P_\alpha\boxtimes\mathscr P_\beta)
\longrightarrow q^!\mathscr P_{\alpha+\beta}.
\tag{15.2}
\]
Here \(q^!\) is exceptional inverse image, the duality-compatible pullback. The source of (15.2) is the single complex \(p^*(\mathscr P_\alpha\boxtimes\mathscr P_\beta)\) on the extension stack. By the adjunction \(q_!\dashv q^!\), (15.2) gives a map from \(q_!p^*(\mathscr P_\alpha\boxtimes\mathscr P_\beta)\) to \(\mathscr P_{\alpha+\beta}\). Thus \(q_!\) integrates the endpoint coefficients together, with proper supports, over extensions of each middle object. When \(q\) is proper, \(q_!=q_*\). The chosen cohomology theory, support convention and degree shifts must make this push-pull operation well defined. Associativity asks that its two composites agree on the actual three-step flag, with the orientation identifications included.

The first framed charge-two example shows what the geometric comparison must retain. A flag for framed instanton data includes an invariant line. In a chart let \(u\) be the difference of the two support positions and \(D\) the slope of that line. Restriction of the matrix moment equation to the curve, after eliminating two regular pairs, gives the coefficient
\[
 K_f=R'[D]\otimes\Lambda(\eta,\chi),\qquad
 |\eta|=|\chi|=-1,\qquad d\eta=uD,\quad d\chi=0 .
\]
Here one can take \(R'=\mathbb C[t_1,t_2,\beta^{\pm1},\kappa,z,w,q]/(q^4)\), \(u=z-w\). The parameters \(t_1,t_2\) are the two equivariant weights, \(\beta\) sets the scale, and \(q\) records the order of the deformation. The closed odd variable comes from a fourth moment equation whose value on the flag is identically zero. Replacing \(K_f\) by the equation \(uD=0\) would discard it.

The equation \(uD=0\) permits either a line of slope zero at arbitrary separation or any slope at a collision. A constant section on the union is a pair of sections on these branches whose restrictions to \(u=D=0\) agree. Both branches have multiplicity \(+1\) in the oriented transverse graph. The component \(u=0\) contributes integration with compact support over the slope \(D\), followed by the Thom map for that divisor. To compare this with a field, keep the auxiliary insertion at \(t\) between \(z\) and \(w\). The supported Cauchy coefficient on the field side, after removing its invertible exchange factor, has first cubic representative
\[
 2t_1t_2(t_1+t_2)q^3\beta^{-3}(z-t)^{-3}(t-w)^{-1}.
\]
Keep \(z\ne w\) and extract the coefficient of \((t-w)^{-1}\) in this first-current term. The remaining factor \((z-t)^{-3}\) is regular at \(t=w\), with value \(u^{-3}\). The result is \(2t_1t_2(t_1+t_2)q^3\beta^{-3}u^{-3}\). Multiplication by \(u^2\) now leaves a simple pole in \(u\), whose residue reads its coefficient.

How many powers of the normal coordinate \(u\) does this cubic pole require? For an integer \(p\ge1\), impose \(u^p=D=0\) and write \(M_p=R'[D]/(u^p,D)\). The Cauchy module \(T\) consists of finite sums of \(u^{-j}(t-w)^{-a}\), with \(j,a\ge1\) and coefficients in \(R'/(u)\). Multiplication by \(u\) lowers \(j\) and kills the \(j=1\) row. On the moment complex \(C=T[D]\otimes\Lambda(\eta,\chi)\), with \(d\eta=uD\), the degree-zero cohomology is \(T\) because \(uT=T\).

**Lemma (lifting a principal part).** A map \(M_p\to H^0(C)=T\) with \(1\mapsto m\in\ker u^p\) lifts to a derived \(R'[D]\)-linear map \(M_p\to C\) exactly when \(u^{p-1}m=0\).

*Proof.* Put \(R=R'[D]\), in cochain degree zero. The ordered equations \(u^p,D\) form a regular sequence in \(R\). Indeed, \(u=z-w\) is a polynomial coordinate over \(R'/(u)\), and \(D\) is still a polynomial coordinate after imposing \(u^p=0\). Resolve \(M_p\) by the Koszul complex \(R\otimes\Lambda(s,h)\), with \(|s|=|h|=-1\), \(ds=u^p\), \(dh=D\). A chain map inducing \(1\mapsto m\) can be chosen to send \(1\) to the constant polynomial \(m\in T[D]\), since any other representative differs by a boundary. Project its values to the summand without \(\chi\). The images of \(s,h\) have the form \(\eta A,\eta B\), with \(A,B\in T[D]\). Their differentials give \(uDA=0\) and \(uDB=Dm\). Cancelling \(D\) gives \(uA=0\) and \(uB=m\). This summand has no degree \(-2\), so \(d(sh)=u^ph-Ds\) forces \(u^pB-DA=0\). At \(D=0\) this says \(u^{p-1}m=0\). Conversely, raise each \(u\)-pole of \(m\) by one to obtain \(b\) with \(ub=m\). When \(u^{p-1}m=0\), the assignments \(1\mapsto m,\ s\mapsto0,\ h\mapsto\eta b,\ sh\mapsto0\) commute with the differential. ∎

Write \(v=t-w\) and \(\lambda=2t_1t_2(t_1+t_2)q^3\beta^{-3}\). The first current gives \(m=\lambda u^{-3}v^{-1}\) in \(T\), with the external one-form \(du\) understood. For \(\lambda\ne0\), \(u^3m=0\) while \(u^2m=\lambda u^{-1}v^{-1}\ne0\). On the third cut the class defines a map to \(H^0(C)\), but the last Koszul face leaves \(\lambda\eta u^{-1}v^{-1}\) at \(D=0\). On the fourth cut this obstruction vanishes. This is the least cut for the nonzero cubic. At a specialization with \(\lambda=0\) the cubic gives no obstruction.

What becomes of this lift before taking principal parts? Let \(P_z,P_w,P_{zw}\) be the \(R'\)-modules of rational functions in \(t\), proper at infinity, with poles allowed at \(z\), at \(w\), or at both, respectively. Equivalently, localize \(R'[t]\) at the indicated pole factors and take the module quotient by \(R'[t]\). In the untwisted Cauchy complex
\[
 \mathcal K_1=[P_z\oplus P_w\xrightarrow{\ \delta\ }P_{zw}],
 \qquad \delta(a,b)=a-b ,
\]
the pair \((a,b)\) has degree \(-1\) and a two-point representative has degree zero. Taking first the \(v\)-principal part at \(v=0\) with \(u\ne0\), then the \(u\)-principal part, identifies \(P_{zw}/(P_z+P_w)\) with \(T\). Thus \(u^3\) kills the supported class of \(F_3=(u-v)^{-3}v^{-1}\). On \(P_{zw}\) itself multiplication by \(u\) is injective. In fact, division by the monic quadratic \(Q=(t-z)(t-w)\) writes each proper representative uniquely as a finite sum of \((a_i+b_i t)/Q^i\), \(i\ge1\), with \(a_i,b_i\in R'\). Multiplication by the polynomial coordinate \(u\) is injective on each coefficient even modulo \(q^4\). Consequently a strict \(R\)-linear map from the underived fourth cut must send \(1\) to zero in \(P_{zw}[D]\).

To send \(1\) to the rational cubic, resolve the auxiliary \(K_f\)-module \(M_4\otimes\Lambda(\chi)\), on which \(\eta\) acts by zero and \(\chi\) acts by exterior multiplication. Adjoin the two Koszul generators and one even generator \(\theta\) to \(K_f\).
\[
 P=K_f\otimes\Lambda(s,h)\otimes\mathbb C[\theta],\qquad
 ds=u^4,\quad dh=D,\quad |\theta|=-2,\quad d\theta=\eta-uh .
\]
Here \(s,h,\eta,\chi\) all have degree \(-1\). The difference \(\eta-uh\) is closed since \(d\eta=uD\). In the coordinate \(\eta'=\eta-uh\), the pair \(\theta,\eta'\) contracts to the scalars by \(\eta'\theta^n\mapsto\theta^{n+1}/(n+1)\). The remaining complex resolves \(M_4\) and carries the free exterior factor \(\Lambda(\chi)\). This gives the augmentation from the semifree \(K_f\)-module \(P\) to the specified cut.

The nullhomotopies can be written as single-site poles. Put \(F_i=(u-v)^{-i}v^{-1}\) for \(i\ge0\), \(Z_i=((u-v)^{-i},0)\) for \(i\ge1\), and \(W=(0,-v^{-1})\). For \(k=3,4\) put
\[
 U_k=u^{4-k}\left(W+\sum_{i=1}^k u^{i-1}Z_i\right).
\]
The \(F_i\) have degree zero and \(Z_i,W,U_k\) have degree \(-1\) in \(\mathcal K_1\). In \(K_f\otimes_{R'}\mathcal K_1\) write exterior factors on the left. The following values specify a degree-zero \(K_f\)-linear chain map \(\Phi\) from \(P\).
\[
\begin{aligned}
 \Phi(1)&=\lambda F_3,                 &\Phi(s)&=\lambda U_3,\\
 \Phi(h)&=\lambda(\eta F_4-D Z_4),     &\Phi(sh)&=-\lambda\eta U_4,\\
 \Phi(\theta)&=\lambda\eta Z_4 .
\end{aligned}
\]
Every other \(K_f\)-basis monomial containing \(\theta\) maps to zero. In particular \(K_f\)-linearity gives \(\Phi(\eta)=\lambda\eta F_3\), \(\Phi(\chi)=\lambda\chi F_3\) and \(\Phi(\eta\chi)=\lambda\eta\chi F_3\).

To check the signs, \(u=(u-v)+v\) gives \(uF_i=F_{i-1}+\delta Z_i\). Summing this identity gives \(\delta U_k=u^4F_k\), and \(uU_4=U_3+u^4Z_4\). The identity for \(F_4\) gives \(d\Phi(h)=D\Phi(1)\). Using the tensor differential \(d(\eta Z_4)=uD Z_4-\eta\,\delta Z_4\) gives \(d\Phi(\theta)=\eta\Phi(1)-u\Phi(h)\). The other two identities give \(d\Phi(s)=u^4\Phi(1)\) and \(d\Phi(sh)=u^4\Phi(h)-D\Phi(s)\). For \(s\theta\) the required value is \(\lambda\eta(u^4Z_4+U_3-uU_4)=0\). For \(h\theta\) the two \(D\eta Z_4\) terms cancel. The remaining equations follow from \(\eta^2=h^2=0\) and these zero images.

In the field graph the exchange factor is \(G=1+\lambda(u-v)^{-3}\) modulo \(q^4\), and the differential is \(\delta_G(a,b)=a-Gb\). Multiplication by \(G\) on \(P_{zw}\) and \((a,b)\mapsto(Ga,b)\) on the relation pair identify \(\mathcal K_1\) with \(\mathcal K_G\). The quotient there is \(P_{zw}/(P_z+G P_w)\), and the residue first removes \(G\). Composing \(\Phi\) with this isomorphism gives the strict lift with both exterior actions. Since \(G\lambda=\lambda\) at this precision, its value on \(1\) is the original rational function \(\lambda F_3\).

At \(u=0\) the three pole modules all become the single-site module spanned by \(v^{-j}\), \(j\ge1\). The graph differential sends \((a,b)\) to \(a-G_0b\), with \(G_0=1-\lambda v^{-3}\). The scalar value on \(1\) becomes \(-\lambda v^{-4}\), the boundary of \((-\lambda v^{-4},0)\). Every degree-zero pole is a boundary here. The kernel consists of the pairs \((G_0b,b)\), so taking the second entry identifies the degree-\(-1\) cohomology of the graph with the single-site poles.

What does the fourth-cut map detect when the slope also vanishes? The monic-denominator bases above make the pole terms free over \(R'\). Both complexes are bounded above and termwise free over \(R'[D]\), so substitution computes the joint derived fibre. At \(u=0\) one has \(d(sh)=-Ds\). On setting \(D=0\) as well, both \(s\) and \(h\) are closed, and the pair \(d\theta=\eta\) contracts in the source. Now \(U_4=W+Z_1=(-v^{-1},-v^{-1})\). The twist preserves the second entry, so \(\Phi(sh)=-\lambda\eta U_4\) gives
\[
 [sh]\longmapsto +\lambda\eta v^{-1}\qquad\text{in degree }-2 .
\]
Here \(\eta\) belongs to the target moment complex, whose differential vanishes on the joint fibre. The poles form a free module, so this class is nonzero whenever \(\lambda\ne0\). For \(t_1=t_2=\beta=1\) the coefficient is \(4q^3\ne0\) modulo \(q^4\).

What remains open is a map of the same variance on the *whole flag* which carries the proper oriented operation to the field operation. It must act on both odd directions, the framing line, the two branches and their common restriction, agree with both vacuum maps and compose on refined flags. In particular one must construct the image of the geometric Cartan–creation operation in this auxiliary jet, or realize its cubic coefficient directly on the flag.

For a compact orientation example take \(X=S_{\mathrm{Kum}}\times E\), where \(S_{\mathrm{Kum}}\) is a smooth projective Kummer K3 surface and \(E\) an elliptic curve. Fix a Calabi–Yau volume form, a smooth elliptic fibre \(C\subset S_{\mathrm{Kum}}\) meeting a divisor in degree one, points \(p\in C\), \(x\in E\), and \(L\in\operatorname{Pic}^0(E)\). The actual semi-topological components of
\[
A=\mathcal O_C\boxtimes\mathcal O_x,
\qquad B=\mathcal O_p\boxtimes L
\]
generate a subgroup \(\Gamma\cong\mathbb Z^2\). Here a semi-topological component is a connected-component class in the moduli of perfect complexes, with addition induced by direct sum. The two degree-four Chern characters lie in distinct Künneth summands, so the two component classes are independent. On the union of components indexed by \(\Gamma\), the Joyce–Upmeier compact orientation root with its prescribed square admits unital associative root maps for every finite ordered flag with graded terms in this union. The two isomorphism classes of enhancements form an \(H^2(\Gamma,\mathbb F_2)\)-torsor. [Strong orientation on compact two-charge components][strong-orientation]

On three graded factors the two composites of binary root maps have the same square. Their ratio is therefore a sign. Comparing the bracketings of four factors around the pentagon makes these signs a three-cocycle on \(\Gamma\). A two-torus is a classifying space for \(\mathbb Z^2\), so \(H^3(\Gamma,\mathbb F_2)=0\). Rescaling the binary maps by a two-cochain cancels the defect. The remaining choices up to isomorphism differ by \(H^2(\Gamma,\mathbb F_2)\), which has two elements. The use of actual components is essential. Numerical charge alone need not place an object in the specified union. Equivariant descent and comparison with a separately chosen geometric root require their own maps.

The same loss of degree occurs in a signed dimension. At the root considered [in the genus-two denominator](#ch15-the-igusa-series-and-the-stronger-realization-question) the even and odd dimensions are \(29\) and \(93\). Their difference is \(-64\), which is also the superdimension of a space of \(64\) odd vectors. Recovering the root space and its bracket therefore requires more than the integer in the denominator.

## Compact reduction keeps relative moment values {#ch15-compact-reduction-keeps-relative-moment-values}

On an elliptic curve with origin \(0\), take two skyscraper sheaves supported at \(y\) and \(-y\), with \(y\ne0\). The sum of the two support positions is zero. Choosing the first summand as a subobject gives an extension whose middle term is centered but whose two factors have nonzero support sums. If reduction required each factor to be centered, it would remove this flag even before we integrated over it.

To follow the flag in the compact threefold, let \(S\) be a smooth projective K3 surface and \(E\) the elliptic curve. Fix a holomorphic volume form on \(S\) and an invariant one-form on \(E\), giving a volume form on the product. Pull a finite-length sheaf \(T\) on \(E\) back to \(S\times E\) by putting
\[
J(T)=\mathcal O_S\boxtimes T
\]
For \(T=\mathcal O_y\), this is the structure sheaf of the K3 fibre over \(y\). Write \(C_n=\operatorname{Coh}_0^n(E)\) for the stack of length-\(n\) sheaves on \(E\). The extension complex of two such pullbacks is
\[
R\operatorname{Hom}_{S\times E}(J(T),J(T'))
\simeq R\operatorname{Hom}_E(T,T')
\otimes(\mathbb C\oplus\mathbb C\eta),
\qquad |\eta|=2,\quad\eta^2=0.
\tag{15.3}
\]
The adjective spherical refers here to the two scalar self-extension groups of \(\mathcal O_S\), in degrees zero and two. The second summand carries the paired obstruction directions. The classical \(C_n\) is smooth, but (15.3) is not just its ordinary tangent complex. The flag domain requires every associated graded factor to lie in this spherical sector; constraining only the middle object admits extra subobjects.

For \(n>0\) there are two symmetries already visible on a length-\(n\) sheaf \(T\). Scalars act on its space of sections, and elliptic translation moves its support. Removing these symmetries in the derived moduli problem also requires removing their Serre-dual directions.

For every \(n>0\), let \(\mathfrak U_n\) be the derived sheaf open with classical objects \(J(T)\), and fix a point \(x_*\in S\). Write \(r_*=Li_{x_*}^*\) for restriction to \(\{x_*\}\times E\), and let \(p_S,p_E\) be the projections of \(S\times E\). The four reduction maps have types
\[
\begin{aligned}
\det V &: \mathfrak U_n\longrightarrow B\mathbb G_m,
&V(F)&=R\Gamma(E,r_*F),\\
m_nr_* &: \mathfrak U_n\longrightarrow E,\\
\mu_E &: \mathfrak U_n\longrightarrow\mathbb A[-1],
&\mu_{\mathrm{sc}}&:\mathfrak U_n\longrightarrow\mathbb A[-2].
\end{aligned}
\]
Here \(B\mathbb G_m\) classifies line bundles, \(m_n(T)\) is the support sum with multiplicities, and \(\mathbb A[-j]=\mathbb V(\mathbb C[-j])\) is a derived additive group, rather than an ordinary affine line. The map \(\mu_E\) is minus the logarithm of \(\det Rp_{S*}F\), normalized by its value at \(x_*\). Its line is classically trivial and rigidified at that point; the K3 volume form identifies its derived logarithm with \(\mathbb A[-1]\). The second moment uses the similarly rigidified relative determinant
\(\det_XF\otimes p_E^*(\det_Er_*F)^{-1}\); elliptic Serre integration gives its logarithm in \(\mathbb A[-2]\). These are algebraic determinant maps, including their exact-triangle addition homotopies.

Their common derived fibre is
\[
\mathfrak V_n=
\mathfrak U_n\times^R_{B\mathbb G_m\times E\times\mathbb A[-1]\times\mathbb A[-2]}
(\mathcal O,0,0,0).
\]
The first fibre includes a trivialization of \(\det V\), with \(V=H^0(E,T)\) at a classical point. A scalar \(\lambda\) on \(T\) multiplies this line by \(\lambda^n\), and pullback by translation \(a\) changes the support sum by \(-na\). Thus the scalar automorphisms preserving the framing are \(\mu_n=\{\lambda:\lambda^n=1\}\), and the translations preserving the centre are \(E[n]=\{a:na=0\}\). They contribute the residual scalar gerbe and the finite translation action.

Rigidifying the residual central \(\mu_n\) and dividing by the translation subgroup \(E[n]\) defines
\[
\mathfrak R_n^{\mathrm{amb}}
=\bigl[(\mathfrak V_n\mathbin{/\mkern-6mu/}\mu_n)/E[n]\bigr].
\]
The derived stack \(\mathfrak R_n^{\mathrm{amb}}\) has a closed nondegenerate \((-1)\)-shifted symplectic form and smooth classical truncation
\[
\mathcal B_n=[(C_n\mathbin{/\mkern-6mu/}\mathbb G_m)/E].
\]
The double slash denotes rigidification: locally the objects are retained while their central scalar automorphism subgroup is quotiented out. The corresponding lifting gerbe is the stack of local choices of a lift, with their scalar automorphisms; it is not just a set of choices. The cyclic formal neighbourhoods of \(\mathfrak R_n^{\mathrm{amb}}\) agree with those of \(T^*[-1]\mathcal B_n\). A global algebraic equivalence is known at length one; formal agreement at general length does not assert a global equivalence. Nevertheless, the canonical roots \(K_{\mathcal B_n}\) identify the critical coefficients with \(\mathscr P_n=\mathbb Q_{\mathcal B_n}[0]\). On the common-lifting classical flag stack the resulting map \(p^*(\mathscr P_a\boxtimes_{BE}\mathscr P_b)\to q^!\mathscr P_{a+b}\) is an isomorphism with zero source shift; \(BE\) is the classifying stack of elliptic-curve torsors. These give actual classical Hall arrows at every positive length, compatible with the full ordered flags. [Elliptic Weyl transport, ambient paired reduction and critical coefficients][spherical-reduction]

The proof removes symmetries together with their paired directions. At a point, the scalar identity, elliptic translation, and their two Serre-dual partners form a nondegenerate two-pair subcomplex. The four actual derived fibres have its symplectic orthogonal complement as tangent complex. Pullback preserves closedness; the finite quotients preserve nondegeneracy. This constructs the reduced stack, rather than merely naming an orthogonal complement of one tangent space.

Return to the flag in \(T=\mathcal O_y\oplus\mathcal O_{-y}\). The factors have support sums \(y,-y\), while their middle term belongs to the fibre over zero. This tells us which fibre to take also for the additive derived moments. On a flag the total condition
\[
\mu_M=\mu_A+\mu_B=0
\]
allows opposite relative values \(\mu_A=t,\ \mu_B=-t\). A three-step flag uses the same total normalization and its intermediate scalar lifting gerbes. A global comparison with the shifted conormal must carry these relative values, the closed form and the homotopies for refining the flag.

Elliptic translation has the same relative character. If \(Q_\alpha\to BE\) records the translation torsor, two endpoints lie in
\[
Q_\alpha\times_{BE}Q_\beta.
\]
A point of this fibre product includes an identification of the two translation torsors. Thus a change of origin translates both ends together. At charge zero the relative unit is \(BE\) with its coefficient. Quotienting the two ends independently would introduce a second copy of the torsor cohomology.

There is also a mixed operation in a volume-preserving Kummer neighbourhood \(Y\times\Delta\), where \(Y=C\times E\) is an abelian surface and \(\Delta\) is a disc away from a branch value. On \(Y\) take \(A=P\boxtimes\mathcal O_x\) and \(B=\mathcal O_p\boxtimes L\), with \(P\in\operatorname{Pic}^0(C)\), \(L\in\operatorname{Pic}^0(E)\), \(p\in C\) and \(x\in E\). Write \(\alpha=[A]\), \(\beta=[B]\) for their full surface characters. Put the endpoints at \(z_A,z_B\in\Delta\) and set \(\delta=z_B-z_A\). For the ordered extension \(0\to B\to M\to A\to0\), its coordinate \(a\) satisfies \(\delta a=0\) on the branch \(b=0\). The reverse order has \(a=0,\ \delta b=0\). The common critical function is \(f=\delta ab\).

For \(\alpha+n\beta\), \(0\le n\le2\), the determinant slice gives the reduced shifted-cotangent description. Take one reduced input of class \(\alpha+i\beta\) and one ordinary input of class \(j\beta\), with \(i=0,1\), \(j=1,2\) and \(i+j\le2\). Both extension orders have maps of the form (15.2) with binary index shift zero. Together with the ordinary \((\beta,\beta)\) map, their two composites agree on the one-\(A\)/two-\(B\) flag. Properness of the middle maps uses fixed Hilbert polynomials and slope-zero semistability. Extending the operation beyond these product neighbourhoods and comparing a prescribed compact orientation require further maps. [Reduced mixed coefficients, theorem “Mixed coefficients and one-\(A\)/two-\(B\) flags”][mixed-coefficients]

Compare two such charts around a branch value in the base of the elliptically fibred Kummer surface. On the overlap of opposite sheets let \(g\) be the change of frame on the forward extension line. The transition is
\[
 (\delta,a,b)\longmapsto(-\delta,ga,-g^{-1}b).
\]
Inversion on \(C\) negates the two-form on \(Y=C\times E\). The normal differential \(dz\) changes sign as well, preserving the threefold volume. The sign on the reverse line compensates the first change in the surface Serre pairing, and reversing \(\delta\) preserves the cubic. Each ordered extension and its intrinsic orientation map is transported to the corresponding order in the second chart, with both endpoints translated on the same elliptic torsor. For an independently prescribed compact root, assume its square comparison exists over the whole elliptic family of split endpoints and their two extension germs. Its ratio to the intrinsic root is a \(\{\pm1\}\)-local system there. Pullback along the multiplication-by-two cover of this elliptic parameter kills its character, since \(\epsilon(2\lambda)=1\) for every period \(\lambda\). Descent back to the elliptic curve still sees the two independent values of \(\epsilon\). The local cubic and its two ordered operations do not select those values for a prescribed compact root.

## Relative Donaldson–Thomas theory produces an operator first {#ch15-relative-donaldsonthomas-theory-produces-an-operator-first}

Closing a flag calculation to a number can hide the subobject that produced it. There is a compact theory in which one can perform the gluing and still inspect its two inputs beforehand. Degenerate the elliptic factor of \(S\times E\) to a rational curve with one node. On its normalization \(\mathbb P^1\), the two preimages of the node give the marked fibres \(0,\infty\) of the tube \(S\times\mathbb P^1\).

Let \(S\) be a smooth projective complex K3 surface, \(0\ne\beta\in\operatorname{Pic}(S)\) an effective class and \(d\ge0\) the degree over the base curve. A relative ideal sheaf on the tube restricts at either end to the ideal of a length-\(d\) subscheme of \(S\). The Hilbert scheme \(S^{[d]}\) parametrizes precisely these subschemes. A boundary insertion is a cohomology class on that Hilbert scheme. It is evaluated by pulling it back along the restriction map at the chosen end. The pair of ends therefore has a common state space and pairing
\[
H_d=H^*(S^{[d]},\mathbb Q),\qquad
\eta_d(a,b)=\int_{S^{[d]}}a\cup b.
\]
The Hilbert scheme \(S^{[d]}\) has complex dimension \(2d\). Thus the pairing selects total cohomological degree \(4d\). All states have even degree, including the unit and its dual point class. For the empty boundary \(H_0=\mathbb Q\).

Write \(M_{\beta,d,m}\) for the stable expanded relative ideal-sheaf moduli, with \(m=\int\operatorname{ch}_3(\mathcal O_Z)\) for the curve subscheme \(Z\). On the tube \(\chi(\mathcal O_Z)=m+d\). Gluing subtracts the Euler characteristic of the common restriction. For example, when \(d=1\) the tube curve has Euler characteristic \(m+1\) and the common point contributes one. In general that restriction has length \(d\), so the closed Euler index is \(m+d-d=m\). Removing the K3 obstruction direction gives a reduced virtual class of complex dimension \(2d+1\).

**Definition (marked tube operator).** Choose \(D\in H^2(S,\mathbb Q)\) and the class \(\omega\) of an interior point of the base. The descendant \(\tau_0(\omega D)\) is obtained by integrating \(\operatorname{ch}_2(\mathcal O_{\mathcal Z})\) times the pullback of \(\omega D\) over the universal target, where \(\mathcal Z\) is the universal subscheme. Using the structure sheaf of the universal subscheme fixes the sign. The three factors \(\operatorname{ch}_2(\mathcal O_{\mathcal Z})\), \(\omega\) and \(D\) have complex codimensions \(2,1,1\). Integration along the threefold gives a class of codimension one on the moduli space. Capping the reduced virtual class with this descendant leaves complex dimension \(2d\). For boundary insertions \(a,b\in H_d\), define
\[
\begin{aligned}
 &\eta_d(\widehat B^D_{\beta,d,m}a,b)\\
 &\quad=\int_{[M_{\beta,d,m}]^{\mathrm{red}}}
 \tau_0(\omega D)\operatorname{ev}_0^*a\operatorname{ev}_\infty^*b .
\end{aligned}
\tag{15.4}
\]
Here \(\operatorname{ev}_0,\operatorname{ev}_\infty\) are the proper restriction maps to \(S^{[d]}\). Varying \(b\) over all states determines \(\widehat B^D_{\beta,d,m}a\) by nondegeneracy. For homogeneous insertions the integral in (15.4) can be nonzero only if \(\deg a+\deg b=4d\). This is also the degree condition for the Poincaré pairing on \(S^{[d]}\), so the operator preserves degree.

The series \(\widehat B^D_{\beta,d}(r)=\sum_m(-r)^m\widehat B^D_{\beta,d,m}\) is Laurent with a finite lower bound. If \(\beta\cdot D\ne0\), geometric closure gives
\[
\begin{aligned}
 &\frac{1}{\beta\cdot D}\operatorname{Tr}_{H_d}\widehat B^D_{\beta,d}(r)\\
 &\quad=\sum_n(-r)^n\mathrm{DT}_{n,(\beta,d)}^{S\times E}.
\end{aligned}
\tag{15.5}
\]
To prove (15.5), degenerate \(E\) to a rational curve with one node. Its two labeled branches give the ends of the tube. In a homogeneous basis \(e_i\) of \(H_d\) with Poincaré-dual basis \(e^i\), gluing inserts the full diagonal and contracts (15.4) to
\[
 \sum_i\eta_d(\widehat B^D_{\beta,d,m} e_i,e^i)
 =\operatorname{Tr}_{H_d}\widehat B^D_{\beta,d,m}.
\]
All the cohomology is even, so this diagonal contraction is the ordinary trace on the full state space. One marked insertion remains in the interior. As the curve translates along \(E\), the marked divisor counts \(\beta\cdot D\) intersections before taking its finite stabilizer into account. For a stabilizer \(G\) the insertion has degree \((\beta\cdot D)/|G|\) on \(E/G\). Dividing by the intersection number therefore leaves exactly the quotient-stack weight \(1/|G|\) in (15.5). [Relative Donaldson–Thomas operators, geometric closure][relative-dt]

Multiple covers also admit an untraced formula. For each \(k\mid\beta\), choose a K3 surface \(S_k\) and the stated real isometry \(\phi_k:H^2(S,\mathbb R)\to H^2(S_k,\mathbb R)\) sending \(\beta/k\) to a primitive integral effective class \(\beta_k\). Its extension \(\Phi_k:H_d(S,\mathbb R)\to H_d(S_k,\mathbb R)\) is a graded isometric ring isomorphism. Then
\[
\widehat B^D_{\beta,d}(r)
=\sum_{k\mid\beta}\Phi_k^{-1}
\widehat B^{D_k}_{\beta_k,d}(r^k)\Phi_k,
\qquad D_k=\phi_kD.
\tag{15.6}
\]
Each summand in (15.6) has coefficient one. After closing the tube we divide by \(\beta\cdot D\), whereas the primitive trace for the \(k\)th summand is divided by \(\beta_k\cdot D_k=(\beta\cdot D)/k\). Expressing the former in units of the latter gives \(1/k\). The transport \(\Phi_k\) is defined here on real cohomology. Lifts to rational or integral cohomology, Hodge structures, Chow correspondences or sheaf functors need additional constructions.

## A cyclic product that all these traces can miss {#ch15-a-cyclic-product-that-all-these-traces-can-miss}

The trace in (15.5) has identified the two ends. To find out how states multiply, keep a third fibre of \(S\times\mathbb P^1\) at \(1\), in addition to \(0,\infty\). Insert \(a,b,c\in H_d\) independently at the three fibres. Their reduced relative invariant, summed with weights \((-r)^m\), is trilinear in these classes. Fix \(a,b\) and vary \(c\). By nondegeneracy there is a unique output \(\mu_{\beta,d}(r)(a,b)\) whose pairing with \(c\) is that invariant.

The marked tube also uses this operation. Move its interior divisor insertion onto a third cap. An ordinary cap inserts the divisor state \(D^{[d]}\) on \(S^{[d]}\), induced by the universal length-\(d\) subscheme. A reduced cap contributes a scalar \(c^D_{\beta,d}(r)\) times the cup unit. Exactly one side of the cut is reduced, so
\[
 \widehat B^D_{\beta,d}(r)a
 =\mu_{\beta,d}(r)(D^{[d]},a)+c^D_{\beta,d}(r)a .
\]
Thus a fixed cap scalar and a marked tube determine one input row of the multiplication. Varying all three boundary states asks for the full product.

The ordinary three-boundary operation is cup product. Each coefficient \(\mu\) of the reduced operation has degree \(-2\), vanishes when one input is the ordinary unit, and satisfies the Hochschild cocycle equation
\[
a\mu(b,c)-\mu(ab,c)+\mu(a,bc)-\mu(a,b)c=0.
\tag{15.7}
\]
To compare the two ways of sewing four boundaries, write the product as \(ab+\epsilon\mu(a,b)\), with \(\epsilon^2=0\) and \(|\epsilon|=2\). In either channel the coefficient of \(\epsilon\) has one ordinary and one reduced factor. Equality of the two channels gives exactly the four terms of (15.7). Thus the product is unital and associative to first order. Rotating the three insertions gives cyclicity of \(\mu\), meaning that the scalar \(\eta_d(\mu(a,b),c)\) is invariant under cyclic permutation.

For \(d=1\), let \(C\) be a rational section and \(F\) a fibre of an elliptic K3, so
\[
C^2=-2,\quad F^2=0,\quad C\cdot F=1.
\]
**Proposition (the section cubic).** For \((\beta,d,m)=(C,1,0)\), identify \(S^{[1]}=S\). The complete coefficient is
\[
\mu(a,b)=\eta_1(a,C)\eta_1(b,C)C
\quad\text{on all }H^*(S,\mathbb Q).
\tag{15.8}
\]
The primary relative correspondence identifies this coefficient with the reduced genus-zero invariant of \(S\) in class \(C\). Each divisor insertion contributes its intersection with \(C\). The section meets \(F\) once, and the section invariant gives \(\eta_1(\mu(F,F),F)=1\), fixing the scalar multiplying the cubic. The other possible degree pattern \((0,2,4)\) vanishes by cyclicity and the unit identity. In particular
\[
\mu(C,C)=4C,\qquad \mu(C,F)=-2C,\qquad \mu(F,F)=C.
\]
This determines the product on all twenty-four states. Here \(F^{[1]}=F\) and the fibre-marked cap scalar is zero, so the fibre-marked tube reads precisely \(\mu(F,-)\). [Relative Donaldson–Thomas operators, the section cubic][section-cubic]

::: example {#ch15-section-cubic-two-sewings title="Two sewings with one reduced section"}
Let \(p\in H^4(S,\mathbb Q)\) be the point class with \(\int_Sp=1\), and write \(a*b=a\cup b+\epsilon\mu(a,b)\) with \(\epsilon^2=0\). Use the three incoming states \(F,F,C\) and leave the outgoing state free. The ordinary products \(F\cup F=0\), \(F\cup C=p\) and \(C\cup C=-2p\), together with (15.8), give
\[
\begin{aligned}
 (F*F)*C&=(\epsilon C)*C=-2\epsilon p,\\
 F*(F*C)&=F*(p-2\epsilon C)=-2\epsilon p .
\end{aligned}
\]
In the first sewing the reduced factor lies on the component carrying the two fibres. In the second, \(F\cup p=0\) by degree and \(\mu(F,p)=0\) by (15.8), so only the reduced product of \(F\) with \(C\) contributes. Opposite cuts give the same outgoing class. Pairing it with the ordinary unit gives the number \(-2\epsilon\). This checks the one-reduced-factor sewing rule on a specified compact curve class and specified boundary states. [The relative section coefficient and its geometric origin][section-cubic]
:::

The fibre-marked tube fixes every value \(\mu(F,a)\). Could another cyclic product keep this entire row and all the multiplication traces, yet give a different value on three classes perpendicular to \(F\)? The cup algebra makes it possible to construct one. Write it as
\[
A=\mathbb Q1\oplus V\oplus\mathbb Qp,
\qquad V=H^2(S,\mathbb Q),\quad
ab=q(a,b)p\ (a,b\in V),\quad pV=p^2=0.
\]
Here \(p\) is the point class and \(q\) the intersection pairing. Choose \(u,v\perp C,F\) with \(q(u,u)=q(v,v)=0\) and \(q(u,v)=1\). These form a hyperbolic pair in the rational K3 lattice. A change of product along \(u\) will go unseen by the marked row because \(u\perp F\). Its trace will involve the self-pairing of \(u\), while a third insertion \(v\) can pair with its output. Put
\[
\ell_u(a)=\eta_1(a,u),\qquad
\nu_u(a,b)=\ell_u(a)\ell_u(b)u,
\qquad \widetilde\mu=\mu+\nu_u.
\]
For degree-two inputs, the first and last terms of the Hochschild differential of \(\nu_u\) are the same scalar multiple of \(p\); the middle terms vanish. The unit and point-class cases give the same identity, so \(\nu_u\) is a normalized cocycle. Its paired cubic is \(\ell_u(a)\ell_u(b)\ell_u(c)\), hence cyclic.

Because \(\ell_u(F)=0\), the fibre-marked operation is unchanged. For every \(D\in A\), the change in multiplication has rank at most one, since
\[
\nu_u(D,-)=\ell_u(D)u\otimes\ell_u.
\]
The trace of \(x\otimes\ell\) is \(\ell(x)\). Consequently
\[
\operatorname{Tr}\nu_u(D,-)
=\ell_u(D)q(u,u)=0.
\]
This holds on all twenty-four states, not only on the section–fibre plane. Yet
\[
\mu(v,v)=0,\qquad \widetilde\mu(v,v)=u,
\qquad \eta_1(v,\widetilde\mu(v,v))=1.
\tag{15.9}
\]
Even a change of first-order splitting cannot remove the difference while fixing the ordinary algebra. For a one-cochain \(f\),
\[
\eta_1(v,(\delta f)(v,v))
=2\int_Sv^2f(v)=0,
\]
since \(v^2=0\), whereas the same functional on \(\nu_u\) equals one. The two Hochschild classes are distinct. The geometric relative invariant selects (15.8). The other product exhibits an ambiguity in recovering it from the marked tube and the traces.

Fix the rational cup algebra with its grading, unit and pairing. Keep all cap scalars, the full operator \(\mu(F,-)\), and every trace \(\operatorname{Tr}\mu(D,-)\). To measure the ambiguity of these data, subtract two commutative cyclic first-order corrections. Their difference \(\nu\) has degree \(-2\). A paired coefficient involving the unit vanishes, and the only remaining degree pattern consists of three degree-two states. The difference is therefore determined by the symmetric cubic \(T(a,b,c)=q(\nu(a,b),c)\) on \(V\).

Conversely, raise the third index of a symmetric cubic with \(q^{-1}\). Its first-order associator on middle classes is \((T(a,b,c)-T(b,c,a))p=0\). What does each of the two measurements impose? The marked row sets \(T(F,-,-)=0\). The trace of \(b\mapsto\nu(a,b)\) is \((\tau_qT)(a)=\sum_{ij}q^{ij}T(a,e_i,e_j)\) in any basis, so it sets \(\tau_qT=0\). The remaining cubics form
\[
 \ker\!\left(\operatorname{Sym}^3 L\xrightarrow{\ \tau_q\ }L\right),
 \qquad L=\operatorname{Ann}(F)\subset V^* .
\]
Here \(L\) has dimension \(21\), and \(q^{-1}|_L\) has rank \(20\). Contraction is onto. For example, choose \(\ell\in L\) with nonzero square. Contracting \(\ell^3\) yields a nonzero multiple of \(\ell\), and contracting \(\operatorname{sym}(\ell^2m)\) for \(m\perp\ell\) yields a nonzero multiple of \(m\). The dimension is \(\binom{23}{3}-21=1750\). These directions remain distinct even allowing a change of first-order splitting. A degree-minus-two Hochschild coboundary with the stated normalization has paired cubic \(\lambda(a)q(b,c)+\lambda(b)q(a,c)+\lambda(c)q(a,b)\). Its contraction is \(24\lambda\), so a trace-free coboundary of this form vanishes.

There is an explicit set of \(1750\) scalar insertions that recovers the missing coefficients. Subtract the known section reading from each measured cubic value to obtain \(T\). Put \(G=C+F\), so \(G^2=F^2=0\), \(q(F,G)=1\). Set \(W=\langle F,G\rangle^\perp\). For \(z\in W\) the state \(v(z)=G+z-q(z,z)F/2\) has square zero. Since \(T(F,-,-)=0\), its diagonal reading equals \(H(z)=T(G+z,G+z,G+z)\), a polynomial of degree at most three. The two terms of the inverse metric pairing \(F\) with \(G\) also drop out of the contraction. Thus trace-freeness becomes \(\Delta_WH=0\), with \(\Delta_W=\sum q_W^{ij}\partial_i\partial_j\). Choose \(s\in W\) of square \(a=2\), and write \(z=y+xs\) with \(y\in s^\perp\cap W\), a space of dimension \(19\). If \(\Delta'\) denotes its inverse-metric operator, the harmonic equation gives
\[
 H(y+xs)=A(y)+xB(y)-\tfrac a2x^2\Delta'A(y)
                         -\tfrac a6x^3\Delta'B(y)
\]
Here \(A,B\) are polynomials of degrees at most three and two. The formula determines all higher powers of \(x\) from \(A,B\) by the harmonic equation. To recover \(A\), set \(x=0\) and use the \(1540\) nonnegative integer tuples \(y\) of coordinate sum at most three in rational coordinates. The products \(\prod_i\binom{y_i}{j_i}\) with \(\sum_i j_i\le3\) have a triangular evaluation matrix on these tuples with diagonal one. This is the interpolation being used.

At \(x=1\), subtract the known contribution of \(A\). The \(210\) tuples of sum at most two determine \(B-a\Delta'B/6\). Applying \(1+a\Delta'/6\) recovers \(B\), since \((\Delta')^2B=0\). Homogenization and polarization then recover \(T\). Fewer than \(1750\) fixed scalar linear readings cannot separate a vector space of dimension \(1750\). These insertions solve the first-order algebraic inverse problem. A compact physical theory must still provide their preparation.

The \(1750\) parameters describe first-order *differences*. To extend a product beyond first order, apply associativity to its *total* cubic. Write \(E=\langle C,F\rangle^\perp\), \(g=q|_E\), \(f=q(F,-)\) and \(T_0=q(C,-)^{\otimes3}\). With the same marked data and fixed rational coordinates, a cubic admitting an associative lift must have the form \(T_0+B+kf^3\), where \(k\) is a scalar and \(B\) a symmetric trace-free cubic on \(E\), extended by zero on \(\langle C,F\rangle\). For \(a,b,c\in E\) raise the last index by \(g(m_B(a,b),c)=B(a,b,c)\). The remaining condition on every \(a,b,c,d\in E\) is
\[
 g(m_B(a,b),m_B(c,d))-g(m_B(b,c),m_B(a,d))
   =k\bigl(g(a,b)g(c,d)-g(b,c)g(a,d)\bigr).
\]
It characterizes the cubics admitting a second-order associative lift. Each such cubic has a unique graded Frobenius extension in these coordinates, polynomial of degree at most four in the degree-two deformation parameter. At \(T_0\) one has \(B=k=0\). The left side of the equation is quadratic in \(B\), so its linearization forces only the variation of \(k\) to vanish. The tangent space is the space of trace-free cubics on \(E\), of dimension \(\binom{22}{3}-20=1520\). The number \(1520\) counts tangent directions at the section cubic. To count actual products with \(k\ne0\), fix \(k\) first. The associated rank-\(21\) étale algebra then splits over an algebraic closure. Its twenty-dimensional trace-zero summand has an orthogonal marking, determined up to permutation of the \(21\) primitive idempotents. The geometric fibre is \(O_{20}/S_{21}\), of dimension \(190\). Varying \(k\) adds one parameter, giving a smooth open stratum of dimension \(191\).

At \(k=0\), \(m_B\) makes \(E\) a commutative associative algebra with invariant form \(g\) and traceless multiplication operators \(L_a\). Suppose more generally that \(g\) is nondegenerate in dimension \(d>0\) over a field \(K\) of characteristic zero. Its Witt index \(w\) is the largest dimension of a totally isotropic subspace. Put \(m=\min(d,2w+1)\), and let \(E^r\) be the span of the \(r\)-fold products. Since \(\operatorname{Tr}L_a^j=\operatorname{Tr}L_{a^j}=0\) for every \(j>0\), Newton's identities make \(L_a\) nilpotent. Take a Jordan chain \(v,L_av,\ldots,L_a^{l-1}v\) of length \(l\). Self-adjointness gives \(g(L_a^iv,L_a^jv)=g(v,L_a^{i+j}v)=0\) whenever \(i+j\ge l\). The last \(\lfloor l/2\rfloor\) chain vectors are therefore independent and span a totally isotropic space. Hence \(l\le 2w+1\) and \(l\le d\), so \(L_a^m=0\) for every \(a\). Polarizing this identity gives \(m!L_{a_1}\cdots L_{a_m}=0\), since the multiplication operators commute. Apply it to one further element and divide by \(m!\) in characteristic zero to obtain \(E^{m+1}=0\).

The bound is attained. Use the basis \(z,\ldots,z^m\) of the ideal \((z)\subset K[z]/(z^{m+1})\). The product \(z^i z^j\) is \(z^{i+j}\) if \(i+j\le m\) and zero otherwise. Put \(g(z^i,z^j)=c\) for \(i+j=m+1\), and zero otherwise. On a triple \(z^i,z^j,z^k\), either bracketing of the paired product gives \(c\) exactly when \(i+j+k=m+1\) and gives zero otherwise. This proves invariance. Its anti-diagonal pairs give \(\lfloor m/2\rfloor\) hyperbolic planes. In odd dimension choose \(c\ne0\) to give the remaining line the square of a nonisotropic vector in their orthogonal complement in \(E\). In even dimension any \(c\ne0\) gives the required split summand. Put zero multiplication on the complementary space and across the two summands. Multiplication by any element of the ideal raises the exponent of every surviving monomial, so its diagonal entries vanish. The product of \(m\) copies of \(z\) is still \(z^m\ne0\).

On the original rational or real K3 marking \((d,w)=(20,2)\). Every sixfold product of middle elements vanishes, and a fivefold product can survive. Over the complexified marking the sharp vanishing length is \(21\). To see a genuinely complex specialization, take \(\mathbb C[s,z]/(z^{21}-s)\) with \(e_i=z^i\) for \(1\le i\le20\) spanning its trace-zero summand. A complex marking identifies \(g(e_i,e_j)=\delta_{i+j,21}\). Removing the unit component of multiplication gives
\[
 B_s(e_i,e_j,e_l)=\delta_{i+j+l,21}+s\,\delta_{i+j+l,42},\qquad k=-s .
\]
For \(s\ne0\) the algebra is étale. At \(s=0\) its middle algebra is \(z\mathbb C[z]/(z^{21})\), with \(e_1^{20}=e_{20}\ne0\). Any particular real or rational law on the original marking retains its sixfold identity after extension of scalars. The complex marked family supplies new laws. Its isometric stabilizer is \(\mu_{21}\subset SO(g)\), so the \(O(g)\)-orbit of the cyclic point splits into two \(SO(g)\)-orbits. Their closures are distinct \(190\)-dimensional irreducible components of the reduced zero fibre inside the closure of the complex étale stratum. Other components and scheme multiplicities remain open. The degree-two deformation parameter integrates a fixed cubic on all \(24\) states, while \(s\) here varies the middle multiplication itself.

There is a trace that can distinguish the lifted products when \(k\ne0\). In the algebraic Frobenius theory of a fixed lift over \(\mathbb Q[t]\), write \(L_a(b)=a*b\), with \(|t|=2\). Closing a cylinder with successive insertions \(a_1,\ldots,a_j\) gives \(\operatorname{Tr}(L_{a_1}\cdots L_{a_j})\) on all twenty-four states. At a torus with point insertion \(p\), and with middle insertions \(x,y,z\in E\), the readings are
\[
 \operatorname{Tr}L_p=-9kt^2,\qquad
 \operatorname{Tr}(L_xL_y)=-21kt^2g(x,y),\qquad
 \operatorname{Tr}(L_xL_yL_z)=-21kt^3B(x,y,z).
\]
At \(k\ne0\) the first trace determines \(k\) as \(-[t^2]\operatorname{Tr}L_p/9\). Now the third trace determines every \(B(x,y,z)\) by division of its cubic coefficient by \(-21k\). The second trace is a check on the normalization of the pairing. These operations determine the integrated product on this stratum. At \(k=0\) all three displayed traces vanish for every \(B\). The three-boundary sphere will still read \(B\).

To see the two integers, put \(P=\langle C,F\rangle\), \(h=kt^2/2\) and \(b_\pm=p\pm h1\). Raise an index of the plane cubic \(T_0+kf^3\) with \(q|_P\) to obtain \(m_P\). The integrated multiplication on the two summands is
\[
 a*b=q(a,b)b_++t m_P(a,b)\quad(a,b\in P),\qquad
 x*y=g(x,y)b_-+t m_B(x,y)\quad(x,y\in E).
\]
The mixed product vanishes, \(p\) multiplies by \(h\) on \(P\) and by \(-h\) on \(E\), and \(p*p=h^2 1\). Their associativity is precisely the four-state equation on \(E\). On the plane its curvature is \(-k\), as evaluation on \((F,F,C,C)\) shows. The mixed associators vanish since \(b_+*E=b_-*P=0\). This gives the unique integrated product. The point trace is \((2-20)h\) and \(\operatorname{Tr}L_{b_-}=(2-20-24)h\). For \(x\in E\), \(\operatorname{Tr}L_x=t\operatorname{tr}m_B(x,-)=0\). Using \(L_xL_y=L_{x*y}\) gives the two-state reading. Multiplication by \(z\), with \(b_-*z=-2hz\), gives the three-state reading.

At \(k=0\), every regular trace word and every connected positive-genus scalar, with arbitrary insertions, agrees with the section product. Indeed, on \(E\) each nonempty word in the middle multiplication operators is multiplication by a single middle element and has trace zero. The handle, obtained by multiplying and summing dual pairs of states, is \(24p-2tC\). It annihilates \(E\oplus\mathbb Q[t]p\), the ideal containing every change of an inserted product. Multiplication by the handle is common to both laws. A sphere with three middle insertions measures the difference \(tB(x,y,z)\). In any finite-dimensional Frobenius space with a perfect pairing \(\eta\), the complete three-input scalar \(C_3\) gives the product by \(a*b=\eta^{-1}(C_3(a,b,-))\).

A product in this zero stratum can have nonisotropic image. Choose a hyperbolic pair \(e,f\in E\), \(g(e,f)=1\), and \(s\perp e,f\) with \(g(s,s)=a\ne0\). Set \(m_B(e,e)=s\), \(m_B(e,s)=af\), and take all other basis products to be zero, up to symmetry. The only nonzero triple middle product of basis vectors is \(e^3=af\). The resulting sphere changes by \(ta\) on \((e,e,s)\), by zero on \((e,e,e)\), and by \(t^2a\) on four copies of \(e\). With only \(e\) prepared, four inputs are needed.

For the ordinary cup algebra \(K1\oplus V\oplus Kp\), the criterion works over any field \(K\) with finite-dimensional \(V\) and perfect symmetric \(q\). Keep \(pV=p^2=0\) and put \(x*y=q(x,y)p+t\,m(x,y)\). This gives a commutative Frobenius product exactly when \(m\) is associative and \(q(m(x,y),z)\) is symmetric. Its regular trace words and all inserted positive-genus scalars agree with the cup product exactly when every \(m(x,-)\) has trace zero. Indeed, the handle paired against \(x\in V\) reads \(t\operatorname{tr}m(x,-)\). When these traces vanish the handle is \((\dim V+2)p\), and two handles multiply to zero.

The relative section coefficient itself is fixed by (15.8). A physical comparison must supply its marked states and oriented three-boundary operation.

### Which preparations detect a cubic on K3 cohomology? {#ch15-k3-prepared-cubic-probes}

A scalar pair of pants can test the cubic only on states one can prepare. Work over a characteristic-zero field \(K\) with formal parameter \(t\), and set \(V=H^2(S,K)\), \(E=\langle C,F\rangle^\perp\). The intersection form \(q\) is perfect on the 20-dimensional space \(E\). The original rational marking has signature \((2,18)\) after extension to \(\mathbb R\). Compare the fixed section product (15.8), added with coefficient \(t\) to the cup product, with its deformation by \(t\lambda\nu_u\). Here \(0\ne\lambda\in K\), \(0\ne u\in E\) and \(q(u,u)=0\). Three copies of a marked middle state \(x\) change the genus-zero scalar by \(t\lambda q(u,x_E)^3\), where \(x_E\) is its orthogonal projection.

Suppose every element of a prescribed linear subspace \(S_0\subset E\) is available as a projection. A rival indexed by \(u\) gives the reference reading on a probe \(x\) exactly when \(q(u,x_E)=0\). Thus a set of probes spanning \(W\subset S_0\) misses some rival exactly when \(W^\perp\) contains a nonzero vector of square zero. A space containing no such vector is called anisotropic over \(K\). All rivals can be detected precisely when \(S_0^\perp\) is anisotropic. If feasible, the minimum number of fixed diagonal readings is
\[
 \dim E-\max\{\dim D:S_0^\perp\subseteq D\subseteq E,\ D\text{ anisotropic over }K\}.
\]
The zero space counts as anisotropic. For unrestricted projections over \(\mathbb Q\) or \(\mathbb R\), choose two perpendicular positive directions, one in each of two rational hyperbolic planes. Their common perpendicular is negative definite. One probe always misses a nonzero vector of the totally isotropic plane spanned by the two first null basis vectors. The minimum is therefore two. Over \(\mathbb C\), an anisotropic subspace has dimension at most one, and the perpendicular to a nonsingular line has dimension nineteen. The minimum there is nineteen.

If every probe itself must lie in \(E\) and have ordinary cup square zero, the respective counts become \(3,3,19\). Indeed \(E\) contains two rational hyperbolic pairs \(e_i,f_i\), with \(q(e_i,f_i)=1\) and the pairs mutually orthogonal. The three null states
\[
 e_1,\qquad f_1,\qquad e_1-f_1+e_2+f_2
\]
have a negative definite common perpendicular over the reals. Two orthogonal null probes miss their own span, and the perpendicular to a nonorthogonal pair still contains a rational hyperbolic plane. Over \(\mathbb C\) a subspace of dimension at least two contains a nonzero null vector, while the perpendicular to an anisotropic line has a null basis of size nineteen. The nullness condition changes if the actual preparation may lie anywhere in \(V\). The rational states \(C+e_i+f_i\) have cup square zero and project to positive vectors in \(E\). Those two lifts suffice over both \(\mathbb Q\) and \(\mathbb R\).

The three displayed probes detect a change from the section product but leave an ambiguity about its direction. For weight one, \(u=e_2\) and \(u=f_2\) both change the three readings by \((0,0,t)\). A further probe \(f_2\) gives \(t\) for the first rival and zero for the second. Thus a family of tests can separate every alternative from the fixed section product while assigning the same values to two alternatives. To identify an unknown weighted cubic, the tests must separate each pair.

Over \(\mathbb Q\) or \(\mathbb R\), exactly **twenty** fixed diagonal readings distinguish every pair of weighted rank-one tensors, even using null preparations in \(E\). With fewer readings choose \(0\ne z\) perpendicular to all probes. A null \(z\) already gives invisible rivals. If \(q(z,z)\ne0\), choose a null \(e\) with \(q(e,z)\ne0\). Then \(u=q(z,z)e/(2q(e,z))\) and \(u-z\) are distinct null directions with the same pairings at all probes. For sufficiency, take a basis of null probes. For each probe take the coefficient of \(t\) in the change from the section product. At least one of these scalars is nonzero for a nonzero rival, since the pairing is perfect. Divide all the coefficients by that nonzero scalar. The weight cancels, leaving the cubes of the ratios of the pairings. Cubing is injective over \(\mathbb Q\) and \(\mathbb R\), so equal readings determine the same ratios on the basis. The one nonzero reading then fixes the weighted cubic itself.

A nonzero complex number has three cube roots. Let \(\omega\ne1\) satisfy \(\omega^3=1\), and extend \(e_1,f_1,e_2,f_2\) to a hyperbolic basis of \(E\). The two null vectors \(e_1+e_2\) and \(e_1+\omega e_2\) have the same cubed pairings with every basis vector. The additional null probe \(f_1+f_2\) gives \(8\) and \((1+\omega)^3=-1\). This probe distinguishes these two tensors. How many probes chosen in advance distinguish every pair?

The preparation space matters even if the number of probes is unrestricted. On a single projective K3 take \(u=[\Omega_S]\), the class of its holomorphic two-form. Its square and its pairing with every divisor class vanish by Hodge type, so \(u\in E\) is null. The section product and its deformation by \(t\nu_u\) agree on every triple prepared from divisors. For \(v=[\bar\Omega_S]/q([\Omega_S],[\bar\Omega_S])\), one has \(q(u,v)=1\) and \(q(v,v)=0\). Three copies of this transcendental state change the reading by \(t\).

::: theorem {#ch15-complex-cubic-probe-count title="Pairwise recovery of a complex isotropic cubic"}
Let \(E=\langle C,F\rangle^\perp\) over \(\mathbb C\), with its nondegenerate symmetric intersection form \(q\) and \(\dim E=20\). For each prepared \(p\in E\), read the coefficient \(\lambda q(p,u)^3\) of \(t\) in the change from the section product on three copies of \(p\). To identify every nonzero tensor \(\lambda u^{\otimes3}\) with \(q(u,u)=0\), the minimum number of fixed probes is \(38\). Every list of at most \(37\) linear probes misses a pair of distinct tensors. A Zariski-open dense set of lists of \(38\) isotropic probe directions suffices.
:::

::: proof {#ch15-proof-complex-cubic-probe-count}
Absorb a cube root of \(\lambda\) into \(u\). The three representatives \(u,\omega u,\omega^2u\) give the same tensor. Replacing the probe \(p\) by \(bp\), with \(b\ne0\), multiplies both cubic readings by \(b^3\). Thus whether \(p\) separates two tensors depends only on its direction. For two independent null vectors \(u,v\), a probe gives equal readings exactly when one of the three linear pairings \(q(p,u-\omega^jv)\) vanishes. On the projective quadric \(\mathcal Q\) of null directions in \(E\), the agreeing probes therefore form
\[
 \bigcup_{j=0}^{2}\bigl(\mathcal Q\cap\mathbb P((u-\omega^j v)^\perp)\bigr).
 \tag{15.9a}
\]
Each section in (15.9a) has dimension \(17\), since the \(18\)-dimensional quadric spans \(\mathbb P(E)\). Independent pairs of nonzero null vectors, up to simultaneous scaling, have dimension \(19+19-1=37\). Simultaneous scaling leaves their relative weight free. The space of such pairs with \(38\) agreeing probe directions has dimension at most \(37+38\cdot17=683\). Its projection has closure of dimension less than \(684=\dim\mathcal Q^{38}\). A generic list also spans \(E\). It thus detects every independent pair, and if \(v=cu\), a nonzero reading forces \(c^3=1\) whenever the readings agree. This proves sufficiency.

For necessity take any \(37\) covectors \(\ell_i=q(p_i,-)\). Shorter lists can be extended to this size. If their common kernel contains \(z\ne0\), the null and nonnull cases in the preceding argument over \(\mathbb Q\) or \(\mathbb R\) still give indistinguishable tensors. Suppose the covectors span \(E^*\). First consider a partition into two groups of ranks at most \(18\). Their kernels \(U,V\) have dimensions \(s,r\ge2\) and \(U\cap V=0\). Write \(Q(x)=q(x,x)\). We seek \(a\in U,\ b\in V\), both nonzero, with
\[
 Q(a-b)=Q(\omega a-b)=0 .
\]
Indeed, the independent null vectors \(a-b,\omega a-b\) then give equal linear readings on the first group and readings differing by a factor of \(\omega\) on the second. If \(Q|_U=0\), take a nonzero null \(b\in V\) and a nonzero \(a\in U\cap b^\perp\). The same choice with the roles exchanged works if \(Q|_V=0\). Otherwise the two quadrics in \(\mathbb P(U\oplus V)\) meet in dimension at least \(s+r-3\). The solutions on the two coordinate subspaces have dimensions \(s-2\) and \(r-2\). Neither subspace, nor their union, contains all the solutions.

A covector whose deletion lowers the rank is called a coloop. For such an index \(i\), let \(z_i\) be the vector killed by the other covectors with \(\ell_i(z_i)=1\). Take \(a=z_i\) and \(b\in\ker\ell_i\). The two null equations now prescribe
\[
 2q(z_i,b)=(1+\omega)Q(z_i),\qquad Q(b)=\omega Q(z_i).
\]
If \(z_i\) is null, its perpendicular in \(\ker\ell_i\) has dimension at least \(18\) and contains a nonzero null \(b\). If \(Q(z_i)\ne0\) and \(q(z_i,-)\) is nonzero on \(\ker\ell_i\), the first equation cuts out an affine space of dimension \(18\). Its direction contains a vector of nonzero square, since a totally isotropic space has dimension at most ten. On a line in this direction the second equation is quadratic and has a complex root. The first equation ensures \(b\ne0\). In both cases \(a,b\) are independent and the two groups of probes again give equal cubes.

It remains to treat lists for which every coloop has \(Q(z_i)\ne0\) and \(\ker\ell_i=z_i^\perp\). These lines are mutually orthogonal. If there are at least three, choose components on three of them with squares \(1,\omega^2,\omega\). Their sum is a null vector. Multiplying the components respectively by \(1,\omega,\omega^2\) gives another null vector. The two directions differ, and each probe sees at most one component, so all cubic readings agree.

If there are \(c\le2\) such lines, take their orthogonal complement \(E'\), of dimension \(n'=20-c\). The remaining \(m'=37-c\) covectors vanish on the removed lines and span \((E')^*\). Deleting any one of them preserves that span. Write \(A:E'\to\mathbb C^{m'}\) for their joint evaluation and \(W=A(E')\). We want to divide the remaining indices into three groups such that the complement of each group still spans \((E')^*\). Then a vector in \(W\) supported in a single group must vanish.

To see when this division is possible, take the coordinate functionals on the space of linear relations among the remaining covectors. For a subset \(S\) of size \(h\), put \(k=n'-\operatorname{rank}(\ell_i|_{E'}:i\notin S)\). The vectors in \(W\) supported in \(S\) form a space of dimension \(k\). These are exactly the relations among the \(h\) coordinate functionals on the relation space, since its annihilator is \(W\). Their rank is \(h-k\). Independence of a group is thus equivalent to its complement spanning. Edmonds's matroid partition theorem gives a partition into three independent groups, allowing empty groups, precisely when \(h\le3(h-k)\) for every \(S\). [Edmonds, §1.3, Theorem 1](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p67_A1b.pdf#page=3)

If the inequality fails, \(k\le h<3k/2\). The case \(k=1\) would give a single remaining coloop, so \(k\ge2\). Put the original coloops, the remaining indices outside \(S\), and \(k-2\) indices from \(S\) in one group. Its rank is at most \(20-k+(k-2)=18\). The other has \(h-k+2<k/2+2\le12\) members. The two-group argument gives a collision.

Otherwise assign the phases \(1,\omega,\omega^2\) to the three groups and let \(D\) multiply coordinates by these phases. The space \(L=W\cap D^{-1}W\) has dimension at least \(2n'-m'=3-c\). A nonzero \(y\in L\) cannot be an eigenvector of \(D\), since its support would lie in a single group. Thus \(x=A^{-1}y\) and \(x'=A^{-1}Dy\), taking the inverse on \(W\), are independent and give equal cubes on all remaining probes.

When \(c=0\), the two homogeneous equations \(Q(x)=Q(x')=0\) have a common point in \(\mathbb P(L)\), of dimension at least two. When \(c=1\), impose \(Q(x)=Q(x')\) on \(L\), of dimension at least two. For a nonzero solution add the same component on the removed line to both vectors, of square \(-Q(x)\). When \(c=2\), take any nonzero solution of the linear conditions \(y\in L\). Add two orthogonal components of squares \(s_1,s_2\) to \(x\), and the same components to \(x'\) with the second multiplied by \(\omega\). The equations \(s_1+s_2=-Q(x)\) and \(s_1+\omega^2s_2=-Q(x')\) have a unique solution. Every prescribed square is attained on a nonnull complex line. In each case the lifted vectors are null, their projections are independent and their readings at the removed probes also have equal cubes. This proves the lower bound. ∎
:::

One can also ask for every cubic on a *known* totally isotropic subspace \(U\subset E\) of dimension \(r\). For \(B\in\operatorname{Sym}^3U\), let \(\ell(x)=q(x,-)|_U\). The change of the three-middle-state scalar is \(tB(\ell(x),\ell(y),\ell(z))\). The corrected product is associative and cyclic. Its change takes values in \(U\) on two middle states, and the common handle annihilates \(U\oplus Kp\), so every connected positive-genus scalar sewing agrees. Exactly \(\binom{r+2}{3}\) predetermined diagonal readings recover an arbitrary weighted cubic on this known space. Evaluations span its dual and a dual isotropic subspace supplies null lifts. If projections are restricted to \(S_0\), with every vector in it available, recovery requires \(S_0\to U^*\) onto. When \(U=\langle e_1,e_2\rangle\), the four null states \(f_1,f_2,f_1+f_2,f_1-f_2\) suffice. The polynomial \(XY(X-Y)\) vanishes on the first three and gives \(-2\) on the fourth. Physical or Hall realizations of these experiments must supply the prepared states and the oriented pair of pants. [K3 preparations and cubic measurements](#atlas-c-k3-prepared-cubic-probes)

## The Igusa series and the stronger realization question {#ch15-the-igusa-series-and-the-stronger-realization-question}

The sphere can distinguish two products with equal closed traces. We can nevertheless ask for the closed traces themselves, for all primitive classes at once. A second description of the counted curves uses a stable pair on \(X=S\times E\). This is a morphism \(\mathcal O_X\to F\) with \(F\) pure of dimension one and zero-dimensional cokernel. Purity means that \(F\) has no nonzero zero-dimensional subsheaf. For a primitive effective K3 class \(\beta_h\) of square \(2h-2\), the reduced Donaldson–Thomas and stable-pair theories have a common rational function \(R_{h,d}(v)\). Its Laurent expansion at \(v=0\) gives their series.

Closing the tube in (15.5) fixed the K3 class and the length at the boundary. To collect all the primitive counts, keep one variable for the square of the K3 class and another for the boundary length, in addition to the variable for the Euler index. These three variables are the exponential coordinates of the genus-two Siegel upper half-space,
\[
Z=\begin{pmatrix}z_1&z_2\\z_2&z_3\end{pmatrix},\quad
\operatorname{Im}Z>0,\qquad
(q,r,s)=(e^{2\pi iz_1},e^{2\pi iz_2},e^{2\pi iz_3}).
\]
Let \(\chi_{10}\) be the genus-two Igusa cusp form of weight ten, normalized by \([qrs]\chi_{10}=1\). Let \(\Delta_5\) be the weight-five product of the ten even genus-two theta constants, with sign fixed by leading coefficient \(+64(qrs)^{1/2}\), and put \(D_5=\Delta_5/64\). Then \(\chi_{10}=D_5^2\). [Primitive reduced counting and normalization][igusa-normalization]

Sum the normalized traces (15.5) with weights \(q^{h-1}s^{d-1}\). In their rational representatives, the inverse Igusa theorem gives
\[
\sum_{h,d\ge0}R_{h,d}(-r)q^{h-1}s^{d-1}
=-\frac1{\chi_{10}(Z)}
=-D_5^{-2}=-4096\Delta_5^{-2},
\qquad D_5=\Delta_5/64.
\tag{15.10}
\]
Here \(r\) records the closed Euler index, \(q\) the square of the primitive K3 class through \(h-1=\beta_h^2/2\), and \(s\) the boundary length through \(d-1\). The DT series is the expansion of \(R_{h,d}(-r)\) at \(r=0\). Expanding at \(r=\infty\) or substituting \(r=e^{iu}\) uses the same rational representative in a different expansion. The empty boundary \(d=0\), with state space \(H_0=\mathbb Q\), supplies its entire \(s^{-1}\) coefficient. [Relative Donaldson–Thomas operators, primitive inverse Igusa series][igusa-series]

Equation (15.10) is a numerical theorem with a geometric trace construction behind it. The imprimitive numerical formula follows from the multiple-cover theorem. A realization of the compact state theory asks for more: an independently defined critical Hall or field state space, a map to the full \(H_d\), and compatibility with the actual extension correspondences, ordinary cup unit, full pairing and reduced three-boundary operation. The comparison must recover the zero in (15.9), as well as the scalar in (15.10).

There is a finite-dimensional geometric operator that produces the Igusa form itself. For a smooth complex genus-two curve \(C_2\), let \(W_6\) be its six Weierstrass points and \(H=H^0(C_2,\omega)\). Evaluate the fifth powers of holomorphic differentials:
\[
 e_5:\operatorname{Sym}^5 H\longrightarrow
            \bigoplus_{P\in W_6}\omega_P^{\,5}.
\]
Both sides have dimension six. In the coordinates \(y^2=a_6\prod_{i=1}^6(x-x_i)\), with \(\alpha=dx/y\) and \(\beta=x\,dx/y\), the evaluation matrix in the monomial basis has rows proportional to \((1,x_i,\ldots,x_i^5)\). The Wronskian fixes the proportionality in the determinant line. With \(\lambda=\det H\) the result is
\[
 d_e=a_6^5\!\prod_{i<j}(x_j-x_i)(\alpha\wedge\beta)^5
               \otimes\operatorname{or}(W_6)
       \ \in\lambda^5\otimes\operatorname{Or}(W_6).
\]
The final factor changes sign on an odd permutation of the six points. Write \(j\) for the Jacobian map from smooth genus-two curves to principally polarized abelian surfaces. In the period normalization of (15.10),
\[
 j^*\chi_{10}=\frac{d_e^2}{2^{32}\pi^{20}},\qquad
 j^*D_5=-\frac{d_e}{2^{16}\pi^{10}} .
\]
The unsquared sign uses the orientation fixed on the bielliptic family. To extend that calibration to all smooth curves, first compare the squares as algebraic sections. The determinant \(d_e\) is nowhere zero when the six roots are distinct. A smooth genus-two Jacobian has an irreducible theta divisor, the Abel image of the curve. It therefore avoids the decomposable locus on which \(\chi_{10}\) vanishes. The weight-ten modular form is an algebraic section of the tenth Hodge power, and its pullback by the Jacobian map is algebraic. Hence \(d_e^2/j^*\chi_{10}\) is an invertible regular function on the smooth locus. The period normalization can change this comparison by a nonzero constant.

Pull the ratio back to binary sextics with nonzero discriminant. The units in the polynomial ring of coefficients localized at the irreducible discriminant are \(c\,\operatorname{Disc}^k\). Multiplying the sextic by a nonzero complex scalar gives an isomorphic curve and multiplies its discriminant by the tenth power of that scalar. The ratio is intrinsic to the curve, so \(k=0\). The calibrated equality of squares now holds throughout the smooth locus. With the orientation lines identified, the ratio of the unsquared sections has fixed square on the connected smooth moduli space. Its value on the bielliptic family fixes the sign everywhere in that frame.

For the ordered roots \(0,1,2,4,7,11\) in a monic sextic the fifteen factors multiply to \(838252800\). Thus the coefficient of \((\alpha\wedge\beta)^{10}\) in \(j^*\chi_{10}\) is \(10721859080625/(65536\pi^{20})\). This constructs a section on smooth curves. Preparing the evaluation by a compact \(S\times E\) operation and extending that operation to stable degenerations remain separate problems.

The determinant on smooth curves gives a modular section. A second question concerns the states counted by an automorphic denominator. In a Lie superalgebra a signed root multiplicity is the even dimension minus the odd dimension. For the Gritsenko–Nikulin algebra one can compute the two dimensions separately. Use its parity-minimal presentation, with a single parity for each signed simple multiplicity. Its signed denominator in the doubled coordinate is \(D_5(2Z)\). At the sum of the three real simple roots the signed multiplicity is \(-64\), while the presentation gives \(29\) even and \(93\) odd states. Two even three-generator brackets survive Jacobi and \(27\) more come from bracketing a real and a null generator. The chamber correction supplies \(93\) odd simple generators. An auxiliary space with \(64\) odd states gives the same signed multiplicity. A compact Hall realization must recover both parity dimensions, the primitive bracket, its relations and a compatible action on the state space.

For a Hall-to-field map, the test before taking traces is (15.2). Fix charge, coefficients and allowed supports. An extension determines the input pair and the coefficient at its middle object. Their map must go to the position-dependent field operation, including its shifted singular divisors and normal directions. On three inputs the two orders of composition must agree, or be related by the specified homotopy, on the full flag and configuration correspondence. Preparing a state also requires a distinguished vector or functional with its gluing laws. A scalar character supplies none of those evaluations on separate inputs.

Period and isogeny constructions supply additional genuine comparisons. Rational marked isogeny transport preserves the Hilbert-state ring and pairing, and the primitive marked relative tensors in the stated effectiveness chambers with one reduced sewing factor. An integral Brauer-twisted Fourier–Mukai endpoint changes rank and degree, so its relative operation problem belongs to the corresponding twisted higher-rank moduli. These maps constrain a realization, but do not identify its full coefficient, orientation and prepared-state systems automatically. [Period and isogeny state comparison][isogeny-states]

For the class \((C,1,0)\), a proposed Hall realization can be tested before taking a trace. On \(F,F,F\) the geometric scalar is \(1\). On \(v,v,v\) it is \(0\), while the rival in (15.9) gives \(1\) with all the same marked traces. The comparison must identify the boundary states and transport the oriented three-input operation that gives both values. [The compact Hall comparison problem](#problem-branes-and-compact-states)

In this compact example the operator on two open ends came first, and gluing gave its trace. For the [arithmetic trace](#ch16-the-complete-arithmetic-functional) the order of discovery is reversed. A formula gives the scalar on each test function. The question is which space carries operators with those traces, and which of their actions the scalar can distinguish.

[ordinary-hall]: #ref-ch15-01
[strong-orientation]: #ref-ch15-02
[spherical-reduction]: #ref-ch15-03
[mixed-coefficients]: #ref-ch15-04
[relative-dt]: #ref-ch15-05
[section-cubic]: #ref-ch15-05
[igusa-series]: #ref-ch15-05
[isogeny-states]: #ref-ch15-06
[k3-triple]: #ref-ch15-07
[igusa-normalization]: #ref-ch15-08

## Source manuscripts {#ch15-source-manuscripts}

### 1. Primitive recognition {#ref-ch15-01}

The proposition “Regular families and the ordinary composition algebra” identifies the unital algebras generated by the three simple indicators by comparing flags at each finite nilpotence bound. The simultaneous cyclic model uses Ben Davison, *Purity and 2-Calabi–Yau categories*, Lemmas 4.4–4.5, Proposition 4.8 and Corollary 4.9. [The comparison on reduced flag varieties](#ch15-a-faithful-ordinary-comparison-on-a-k3-surface) · [Davison](https://arxiv.org/abs/2106.07692)

### 2. Strong orientation on compact two-charge components {#ref-ch15-02}

Joyce and Upmeier, Theorems 3.10 and 4.4 and Proposition 4.3, give the compact orientation and its obstruction theory. For the specified subgroup of actual components, the vanishing of \(H^3(\mathbb Z^2,\mathbb F_2)\) gives associativity on the fixed root. [The two-charge restriction](#ch15-critical-coefficients-and-orientation) · [Joyce and Upmeier](https://arxiv.org/abs/2001.00113)

### 3. Elliptic actions and critical Hall transport {#ref-ch15-03}

“An actual ambient paired reduction” constructs the four derived fibres at positive length. “Refinement with a common total normalization” keeps the intermediate scalar lifting gerbe when a flag is refined. [The reduced spherical sector](#ch15-compact-reduction-keeps-relative-moment-values)

### 4. Reduced mixed critical coefficients {#ref-ch15-04}

“Mixed coefficients and one-\(A\)/two-\(B\) flags” treats the two orders of extension in the local Kummer chart \(f=\delta ab\), with a shared elliptic torsor. Proper pushforward uses fixed Hilbert polynomials and slope-zero semistability. [The local mixed operation](#ch15-compact-reduction-keeps-relative-moment-values)

### 5. Relative Donaldson–Thomas operators {#ref-ch15-05}

Georg Oberdieck, *Multiple cover formulas for K3 geometries, wall-crossing, and Quot schemes*, Theorem 5.1 and §6.2, supplies the relative insertion formula and translation descent in (15.5)–(15.6). Denis Nesterov, *Quasimaps to moduli spaces of sheaves on a K3 surface*, Definition 3.3 and Corollary 4.1, supplies the primary comparison used for (15.8). The three results use different boundary data. [Geometric closure](#ch15-relative-donaldsonthomas-theory-produces-an-operator-first) · [The section cubic](#ch15-a-cyclic-product-that-all-these-traces-can-miss) · [The primitive inverse Igusa series](#ch15-the-igusa-series-and-the-stronger-realization-question) · [Oberdieck](https://arxiv.org/abs/2111.11239v3) · [Nesterov](https://arxiv.org/abs/2111.11425v3)

### 6. Isogenies and K3 state comparisons {#ref-ch15-06}

“Primitive marked-state transport” compares the Hilbert-scheme ring, its pairing, and the primitive relative tensors in chambers where the transported class is effective on both fibres. The sewing uses exactly one reduced factor. [Rational transport and the twisted endpoint](#ch15-the-igusa-series-and-the-stronger-realization-question)

### 7. K3 lattices and spherical objects {#ref-ch15-07}

“A common-polynomial spherical triple” constructs the polarized surface of degree eight and its three stable line bundles. The intersection matrix determines their Hilbert polynomials and off-diagonal extension groups. [The lattice and its three bundles](#ch15-a-faithful-ordinary-comparison-on-a-k3-surface)

### 8. Curves, states and a square root {#ref-ch15-08}

Oberdieck and Pixton, *Holomorphic anomaly equations and the Igusa cusp form conjecture*, give the primitive inverse Igusa count. For the comparison with the rational stable-pair series see Oberdieck, *On reduced stable pair invariants*, Theorem 3. Equation (15.10) fixes the expansion variable and the normalization \(D_5=\Delta_5/64\). For the unsquared section on smooth genus-two curves the sign comes from the ordering of the Weierstrass branches and the bielliptic calibration in the stated frame. [Oriented determinant on smooth curves](#atlas-c-si-15) · [Oberdieck and Pixton](https://arxiv.org/abs/1706.10100) · [Oberdieck](https://arxiv.org/abs/1605.04631)
