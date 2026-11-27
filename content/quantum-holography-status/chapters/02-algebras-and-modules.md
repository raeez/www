# Algebras, modules and combining systems

Put a system of electric charge \(\lambda\) beside a system of charge \(\mu\), using the same unit for both readings. On a product of charge eigenstates \(u\in M,\ v\in N\), a total-charge measurement gives \(\lambda+\mu\). If \(Q_Mu=\lambda u\) and \(Q_Nv=\mu v\), the operator giving this result is
\[
 Q_{M\otimes N}=Q_M\otimes\mathrm{id}_N+\mathrm{id}_M\otimes Q_N .
\]
The first term reads the charge of \(u\) and leaves \(v\) alone. The second interchanges those roles. The addition law follows, for real charges, from the action of a simultaneous phase rotation. On \(u\otimes v\) the phase is \(e^{it\lambda}e^{it\mu}=e^{it(\lambda+\mu)}\). Differentiating at \(t=0\) and dividing by \(i\) recovers the total charge. Thus the symmetry transformations multiply and their infinitesimal generators add. What determines the combination rule for other observables?

Which systems can couple to a given symmetry in the first place? Its generators can act on a single system only if their operators obey the symmetry relations. To combine such systems we seek one rule that works in all representations of a given symmetry. Our state spaces are vector spaces over a field \(k\). Their algebraic tensor product \(M\otimes_k N\) consists of finite sums of tensors \(m\otimes n\), subject to bilinearity.

## Multiplication and representations {#ch02-multiplication-and-representations}

On the energy-two space, let \(P\) project orthogonally onto the state \(a\) with two first-harmonic quanta, and let \(S\) exchange \(a\) with \(b\), the state with one second-harmonic quantum. Select \(a\) and then exchange it, giving \(SPa=b\). Exchange it first and the projection gives \(PSa=0\). An operator product therefore remembers which map acts first, here the factor on the right. Grouping three operations is a different matter. Both \((SP)P\) and \(S(PP)\) act by applying \(P,P,S\) in that order. [The energy-two states](01-physical-questions.md#ch01-two-preparations)

**Definition (unital associative algebra).** An algebra \(A\) over \(k\) consists here of a vector space, a bilinear multiplication \(m:A\otimes A\to A,\ a\otimes b\mapsto ab\), and an element \(1_A\) with
\[
 (ab)c=a(bc),\qquad 1_Aa=a=a1_A.
\]
For operators, the identity transformation supplies \(1_A\) and composition supplies the associative product. The scalar multiple \(c\,1_A\) defines the unit map \(u_A:k\to A\). An abstract product acquires this operational meaning once we choose its action on a space of states.

**Definition (left module).** A representation of \(A\), or left \(A\)-module, is a vector space \(M\) with a linear action \(A\otimes M\to M,\ a\otimes v\mapsto av\), satisfying
\[
(ab)v=a(bv),\qquad 1_Av=v.
\]
Thus assigning the operator \(\rho_M(a):v\mapsto av\) to \(a\) gives a unital algebra map \(\rho_M:A\to\operatorname{End}_k(M)\), the algebra of linear operators on \(M\). A map of modules, or *intertwiner*, is a \(k\)-linear map \(f:M\to N\) that transports states compatibly with every action. Its defining equation \(f(av)=af(v)\) compares acting on the input \(v\in M\) and on its image in \(N\).

For example, specifying a \(k[x]\)-module on \(M\) amounts to choosing one operator \(X\). The polynomial \(c_0+c_1x+c_2x^2\) acts on \(v\) by \(c_0v+c_1Xv+c_2X(Xv)\). On the one-dimensional module \(k_\lambda\), \(x\) acts as multiplication by \(\lambda\), so each polynomial acts by its value at \(\lambda\). A module map \(f:k_\lambda\to k_\mu\) must satisfy
\[
\lambda f(1)=\mu f(1).
\]
If \(\lambda\ne\mu\), this equation forces \(f(1)=0\), hence \(f=0\). The lines \(k_\lambda,k_\mu\) have the same dimension but represent different characters of the polynomial algebra. The linear map that identifies their two basis vectors fails the intertwining equation.

### Which operators can couple to a symmetry? {#ch02-consistent-lie-couplings}

One operator always defines an action of \(k[x]\). For a first example with a relation, return to the energy-two space with ordered basis \(a,b\). Let \(P\) be the projection onto \(a\) and \(E\) the operation taking \(b\) to \(a\) and taking \(a\) to zero. Then \(PE=E\) and \(EP=0\). Their commutator is \(E\), so they can represent two infinitesimal symmetries \(h,e\) with bracket \([h,e]=e\). Replacing \(E\) by \(E+sI\), where \(I\) is the identity and \(s\ne0\), leaves the commutator equal to \(E\). The shifted pair fails the defining relation. How can one equation impose all such relations for an arbitrary system?

Let \(\mathfrak g\) be a finite-dimensional Lie algebra in degree zero over a field \(k\) of characteristic zero. Its alternating bilinear bracket satisfies the Jacobi identity. Choose a basis \(x_a\) with \([x_a,x_b]=\sum_r f_{ab}{}^r x_r\). A linear map from \(\mathfrak g\) to a unital associative algebra \(B\) assigns an operator \(T_a\) to each \(x_a\). Take \(B\) in degree zero with zero differential. The difference between the required bracket and the commutator is alternating in the two inputs. To encode it, give the dual basis \(c^a\) degree one and form the exterior algebra \(C=\bigwedge\mathfrak g^*\), with \(c^ac^b=-c^bc^a\). The Chevalley–Eilenberg differential on \(C\) evaluates a one-form on the negative of the bracket. Thus
\[
 \begin{gathered}
 dc^r=-\frac12\sum_{a,b}f_{ab}{}^r c^ac^b,\\
 d(uv)=(du)v+(-1)^{|u|}u\,dv
 \end{gathered}
\]
for \(u\) of degree \(|u|\). On three inputs \(x,y,z\), \(d^2c^r\) evaluates \(c^r\) on \([[x,y],z]+[[y,z],x]+[[z,x],y]\), which is zero by Jacobi. The derivation rule then gives \(d^2=0\) on \(C\).

Pair each input with its proposed operator in \(\alpha=\sum_a c^a\otimes T_a\). Every element of total degree one in \(C\otimes B\) has this form. The differential there acts on \(C\), and left multiplication by \(\alpha\) also raises degree by one. For any \(u\in C\otimes B\), applying \(D_\alpha u=du+\alpha u\) twice gives \(D_\alpha^2u=(d\alpha+\alpha^2)u\), since the two terms involving \(\alpha\,du\) cancel. Thus the coupled operator squares to zero exactly when \(\alpha\) obeys the *Maurer–Cartan equation* \(d\alpha+\alpha^2=0\).

::: proposition {#ch02-universal-lie-coupling title="The algebra of strict Lie couplings"}
Define the universal enveloping algebra \(U(\mathfrak g)\) by taking words in \(\mathfrak g\), with concatenation as product and the empty word as unit, and imposing linearity in each letter and \(xy-yx=[x,y]\). Unital algebra maps \(U(\mathfrak g)\to B\) are in natural bijection with the degree-one solutions of the Maurer–Cartan equation in \(C\otimes B\).
:::

::: proof {#ch02-universal-lie-coupling-proof}
In \(\alpha^2\) the terms with input labels \(a,b\) and \(b,a\) have opposite exterior signs. Pairing them gives the commutator \([T_a,T_b]=T_aT_b-T_bT_a\). The other term differentiates the one-form. The coefficient \(F_{ab}\) of the resulting curvature on the inputs \(x_a,x_b\) is therefore
\[
 \begin{gathered}
 F_{ab}=[T_a,T_b]-\sum_r f_{ab}{}^r T_r,\\
 d\alpha+\alpha^2=\frac12\sum_{a,b}c^ac^b\otimes F_{ab}.
 \end{gathered}
\]
The \(c^ac^b\) with \(a<b\) are linearly independent. The right side vanishes precisely when the map \(x_a\mapsto T_a\) respects the Lie bracket. Sending a word to the product of its operators then respects the defining relations of \(U(\mathfrak g)\), and this gives the unique extension to a unital algebra map. Conversely any such map gives those operators by restriction to the generators. If \(\iota:\mathfrak g\to U(\mathfrak g)\) denotes the generator map, the identity of \(U(\mathfrak g)\) gives the universal solution \(\sum_a c^a\otimes\iota(x_a)\). Applying a map to \(B\) in its second factor produces the specified coupling. Composition with any unital map \(B\to B'\) transports the coupling by the same rule. ∎
:::

For the two-generator example, let \(u,v\) be the forms dual to \(h,e\). Then \(du=0\) and \(dv=-uv\). For \(\alpha_s=u\otimes P+v\otimes(E+sI)\) the two contributions to the square are \(-uv\otimes(E+sI)\) and \(uv\otimes E\). Their sum is \(-s\,uv\otimes I\). Even a scalar change of the second operator obstructs the coupling here.

This strict classification is the Lie algebra example of the universal line defect in Paquette and Williams's account of Koszul duality. The augmentation \(C\to k\), given by setting the \(c^a\) to zero, fixes the vacuum. The bijection classifies assignments of operators before taking a quotient by changes of basis. [Paquette and Williams, §5.2](https://arxiv.org/pdf/2110.10257#page=23)

How far can the two charges and the raising operator vary together? Start at \((P,0)\) on the energy-two space. Let \(h\) act by \(A=\operatorname{diag}(1+x,y)\) and \(e\) by \(B=\beta E\). The charge gap is \(1+x-y\), so \([A,B]=B\) reads \((x-y)\beta=0\). Taking \(x=\beta=t\) and \(y=0\) gives a coupling over \(k[t]/(t^2)\). Over \(k[t]/(t^3)\) the bracket error \([A,B]-B\) is \(t^2E\). A second-order change in \(A\) first contributes at order three because \(B=tE\). Changing \(B\) by \(t^2C\) adds \(t^2([P,C]-C)\). Since \([P,C]_{12}=C_{12}\) for every \(C\), this first-order coupling has no lift.

Passing to a cochain algebra with the same cohomology can already lose such assignments. In the example, setting \(v=0\) defines a map \(C\to\bigwedge(u)\). Its kernel has basis \(v,uv\), and \(dv=-uv\) maps the first line isomorphically onto the second. The map therefore induces an isomorphism on cohomology. Yet the two distinct solutions \(u\otimes P\) and \(u\otimes P+v\otimes E\) have the same image. To formulate a derived coupling problem one must specify which deformations and equivalences are admitted. For a differential graded target, its internal differential also enters the equation. The cobar construction represents twisting cochains when the input is a coaugmented differential graded coalgebra and the target carries the specified augmentation. [Twisting cochains and their representing algebra](05-bar-and-coherence.md#ch05-cobar-reverses-the-construction)

## A coproduct gives the action on a tensor product {#ch02-a-coproduct-gives-the-action-on-a-tensor-product}

Suppose two probes separately carry consistent couplings. Which coupling acts on their tensor product? For a single abelian generator the enveloping algebra is \(k[x]\). Take its modules \(M=k_\lambda\) and \(N=k_\mu\). With \(\lambda=2,\mu=3\) over \(\mathbb C\), the sum of the separate operators reads \(5\) and their tensor product reads \(6\). Both define actions of \(k[x]\) on the same line, since assigning any one operator to the generator fixes the action of every polynomial. What distinguishes addition from multiplication here is the prescription for \(x\) on the pair.

There is a way to specify such a prescription independently of the representations. If \(H\) acts on \(M\) and \(N\), an element \(a\otimes b\) of \(H\otimes H\) already acts on \(m\otimes n\) by \(am\otimes bn\). For the additive rule assign \(x\otimes1+1\otimes x\) to \(x\), and for the multiplicative rule assign \(x\otimes x\). More generally assign a tensor to each \(h\in H\) and let it act in this way.

Write such a map as
\[
\Delta:H\longrightarrow H\otimes H,
\]
and set
\[
h\cdot(m\otimes n)
=\sum h_{(1)}m\otimes h_{(2)}n,
\qquad
\Delta(h)=\sum h_{(1)}\otimes h_{(2)}.
\tag{2.1}
\]
In this **Sweedler notation** the subscripts distinguish the left and right components of each summand. Acting component by component is bilinear, so the result depends only on the tensor \(\Delta(h)\). There remains the question whether composing two of these operators represents the product in \(H\).

**Proposition (diagonal action).** Let \(H\) be a unital associative algebra and let \(\Delta:H\to H\otimes H\) be linear. Formula (2.1) defines a unital action on the tensor product of every pair of left \(H\)-modules precisely when
\[
\Delta(hh')=\Delta(h)\Delta(h'),\qquad
\Delta(1_H)=1_H\otimes1_H.
\tag{2.2}
\]

*Proof.* The product in \(H\otimes H\) is \((a\otimes b)(c\otimes d)=ac\otimes bd\). Acting first by \(h'\) and then by \(h\) applies the tensor \(\Delta(h)\Delta(h')\), so (2.2) gives both action laws. Conversely choose \(M=N=H\) with the left regular action, multiplication in \(H\). Every tensor \(u\in H\otimes H\) is recovered by applying it to \(1_H\otimes1_H\). Evaluating the two action laws on this one vector gives \(\Delta(hh')=\Delta(h)\Delta(h')\) and \(\Delta(1_H)=1_H\otimes1_H\). ∎

Apply \(h\) to \((L\otimes M)\otimes N\). Splitting its action between the first pair and \(N\), and then between \(L\) and \(M\), applies the tensor \((\Delta\otimes\mathrm{id})\Delta(h)\). The grouping \(L\otimes(M\otimes N)\) applies \((\mathrm{id}\otimes\Delta)\Delta(h)\). If the tensors agree, the usual reassociation of vector spaces intertwines the two actions. Conversely, take all three modules to be \(H\) with its left regular action. As in the proof for two modules, evaluation on \(1_H\otimes1_H\otimes1_H\) recovers each tensor. Reassociation therefore intertwines the actions for every triple precisely when
\[
(\Delta\otimes\mathrm{id})\Delta
=(\mathrm{id}\otimes\Delta)\Delta.
\tag{2.3}
\]
This condition is **coassociativity**. For the additive charge, both sides give \(Q\otimes1\otimes1+1\otimes Q\otimes1+1\otimes1\otimes Q\). They correspond to grouping the first two systems or the last two.

Which system can be adjoined without changing any of these actions? For charges it is the line of charge zero. In general a one-dimensional action is given by a unital algebra map \(\epsilon:H\to k\). Acting on \(k\otimes M\) applies \(\epsilon\) to the first component of \(\Delta(h)\), while acting on \(M\otimes k\) applies it to the second. After identifying both spaces with \(M\), either procedure must give the original action, so
\[
(\epsilon\otimes\mathrm{id})\Delta
=\mathrm{id}
=(\mathrm{id}\otimes\epsilon)\Delta.
\tag{2.4}
\]
**Definition (bialgebra).** A bialgebra \(H\) is a unital associative algebra with unital algebra maps \(\Delta:H\to H\otimes H\) and \(\epsilon:H\to k\) satisfying coassociativity (2.3) and the two counit identities (2.4). The map \(\Delta\) is its coproduct and \(\epsilon\) its coalgebra counit. In the two polynomial examples above the neutral one-dimensional system has \(x=0\) for the additive rule and \(x=1\) for the multiplicative rule. These are the respective values of \(\epsilon(x)\).

Multiplicativity has one interchange hidden in it. Write \(\Delta(h)=\sum a\otimes b\) and \(\Delta(h')=\sum c\otimes d\). The first system must receive \(ac\) and the second \(bd\). On the four factors \(a,b,c,d\), the required map is
\[
\Delta m
=(m\otimes m)
(\mathrm{id}\otimes\tau\otimes\mathrm{id})
(\Delta\otimes\Delta),
\tag{2.5}
\]
where \(\tau(a\otimes b)=b\otimes a\). The middle interchange places the first components together and the second components together. This equation is the ordinary model for one of the compatibility problems in a chiral quantum group. The chiral problem must specify the position-dependent operation spaces and their interchange before it can assert the corresponding equation.

## Group multiplication reverses direction on functions {#ch02-group-multiplication-reverses-direction-on-functions}

Suppose the state of a system is specified by a group element \(g\), and an observable \(f\) reads \(f(g)\). Combine two such systems by group multiplication. The apparatus must now read \(f(g_1g_2)\), which is a function of the *pair*. For an affine algebraic group \(G\), let \(\mathcal O(G)\) denote its algebra of regular functions. Multiplication on states is the map
\[
\mu:G\times G\longrightarrow G.
\]
Composing a function with \(\mu\) gives the pullback
\[
\mu^*:\mathcal O(G)\longrightarrow
\mathcal O(G\times G)
=\mathcal O(G)\otimes\mathcal O(G).
\]
This pullback is the coproduct. On a pair it reads \((\mu^* f)(g_1,g_2)=f(g_1g_2)\). On a triple, \((\Delta\otimes\mathrm{id})\Delta f\) reads \(f((g_1g_2)g_3)\), and \((\mathrm{id}\otimes\Delta)\Delta f\) reads \(f(g_1(g_2g_3))\). Both are pullbacks along the same multiplication map from \(G^3\) to \(G\). Group associativity therefore gives coassociativity. Fix either argument to be the identity and one recovers the original function on the other. Evaluation at the identity is the counit.

For the additive group, \(\mathcal O(G)=k[x]\), and
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad \epsilon(x)=0.
\tag{2.6}
\]
It follows that
\[
\Delta(x^2)=x^2\otimes1+2x\otimes x+1\otimes x^2.
\]
On charges \(2\) and \(3\) the squared total charge reads \(25\), whereas adding the two squared charges gives only \(13\). The missing \(12\) is the value of \(2x\otimes x\). In general this term contributes \(2\lambda\mu\), which vanishes in characteristic two. The algebraic statement behind the measurement is \(k_\lambda\otimes k_\mu=k_{\lambda+\mu}\) under the usual identification of the product line in (2.1).

Group inversion also acts by pullback. Its map \(S\) on functions, called the *antipode*, takes \(f\) to \(g\mapsto f(g^{-1})\). Addition gives \(S(x)=-x\), so adding a label and its inverse gives the counit value zero. Multiplication makes a further demand on the polynomial example. The inverse coordinate must exist. On the multiplicative group the function algebra is \(k[x,x^{-1}]\), and \(S(x)=x^{-1}\) gives \(x S(x)=1=\epsilon(x)\). On all of \(k[x]\) the multiplication rule still defines a bialgebra, but \(x\) has no polynomial inverse.

**Definition (Hopf algebra).** A Hopf algebra is a bialgebra \(H\) with a linear map \(S:H\to H\) satisfying \(m(S\otimes\mathrm{id})\Delta=m(\mathrm{id}\otimes S)\Delta=u_H\epsilon\), where \(u_H(c)=c1_H\). On group functions the two composites evaluate \(f\) at \(g^{-1}g\) and \(gg^{-1}\). Both are the constant function with value \(f(1_G)\).

The identity \(\mathcal O(G\times G)=\mathcal O(G)\otimes_k\mathcal O(G)\) uses affineness. For smooth or analytic observables, identifying functions on a product with a completed tensor product requires the function spaces and their topologies. Drinfeld derives the Hopf operations by pullback in *Quantum groups*, §1, pp. 798–800.

## Lie algebra actions and dual representations {#ch02-lie-algebra-actions-and-dual-representations}

Return to simultaneous transformations, now allowing them to act by matrices. Let \(g_M(t),g_N(t)\) be differentiable one-parameter symmetries on finite-dimensional real or complex spaces with value the identity at zero. Differentiating \(g_M(t)\otimes g_N(t)\) at zero gives \(\dot g_M(0)\otimes1+1\otimes\dot g_N(0)\). The phase calculation is its one-dimensional case. For several generators the question is whether their brackets act by the same rule.

Over any field \(k\), a Lie algebra \(\mathfrak g\) has an alternating bilinear bracket with \([x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0\), the Jacobi identity. Alternation requires \([x,x]=0\), including in characteristic two where a symmetric bracket alone need not vanish on \((x,x)\). To make products of its operators, form the universal enveloping algebra \(U(\mathfrak g)\), generated linearly by \(\mathfrak g\) with unit and relations
\[
xy-yx=[x,y].
\]
The primitive formula
\[
\Delta(x)=x\otimes1+1\otimes x
\qquad(x\in\mathfrak g)
\tag{2.7}
\]
extends to a coproduct on \(U(\mathfrak g)\). To see why the relations survive, calculate
\[
[\Delta(x),\Delta(y)]
=[x,y]\otimes1+1\otimes[x,y]
=\Delta([x,y]).
\]
The cross commutators vanish because the two tensor factors commute. Formula (2.1) becomes the familiar diagonal Lie algebra action
\[
x(m\otimes n)=(xm)\otimes n+m\otimes(xn).
\]

What is the charge of a measurement functional \(\phi:M\to k\)? Evaluating it on a state should give an invariant scalar. In the diagonal action on \(\phi\otimes m\), one term differentiates the functional and the other differentiates the state. Their scalar values must add to zero. This determines the action on the algebraic dual \(M^\vee=\operatorname{Hom}_k(M,k)\),
\[
(x\phi)(m)=-\phi(xm).
\tag{2.8}
\]
The two contributions to the action on the evaluation pairing cancel,
\[
(x\phi)(m)+\phi(xm)=0.
\]
For the enveloping algebra, this is expressed using the antipode \(S\), defined by \(S(x)=-x\) and \(S(ab)=S(b)S(a)\). The order reversal is necessary because transposing a product reverses the order of the operators.

For additive charge \(\lambda\) on a line, (2.8) gives charge \(-\lambda\) on the dual, so evaluation sends the pair to charge zero. Can a scalar also *prepare* a vector paired with a functional? In finite dimension coevaluation sends \(1\) to \(\sum_i m_i\otimes m_i^\vee\) in any basis and its dual. Under \(u\otimes\phi\mapsto(v\mapsto\phi(v)u)\), this sum acts as the identity. That characterization makes it basis independent. In infinite dimension every algebraic tensor gives a finite-rank operator because its image lies in the span of finitely many \(u\)'s. The identity has infinite rank, so evaluation survives but its corresponding coevaluation has no value in \(M\otimes M^\vee\). Likewise the evaluation map \(M\to M^{\vee\vee}\) is an isomorphism in finite dimension and can fail to be onto in infinite dimension. [Tensor products and finite rank](08-completions.md#tensor-completion-and-rank)

## Associators, exchange and coherence {#ch02-associators-exchange-and-coherence}

The tensor product also acts on intertwiners. For example \(f\otimes g\) sends \(m\otimes n\) to \(f(m)\otimes g(n)\). In the category of vector spaces, the assignment \((\ell\otimes m)\otimes n\mapsto\ell\otimes(m\otimes n)\) commutes with applying a linear map to any of the three inputs. This is what *natural* means here. In a general category equipped with a tensor product and tensor unit, the corresponding comparison is specified by an **associator**, a natural isomorphism
\[
\alpha_{L,M,N}:(L\otimes M)\otimes N
\longrightarrow L\otimes(M\otimes N).
\]
On three \(H\)-modules the vector-space reassociation is an intertwiner by (2.3). With four modules we can reassociate successive triples in two ways. Both paths go from
\[
((L\otimes M)\otimes N)\otimes P
\quad\text{to}\quad
L\otimes(M\otimes(N\otimes P))
\]
by applying the associator. The shorter route passes through \((L\otimes M)\otimes(N\otimes P)\). The longer first reassociates the innermost \(L,M,N\), then makes two further moves. The pentagon identity equates the two composite maps. A category with this tensor product, natural associator and compatible left and right identifications with its unit is called **monoidal**.

Reassociating \(L,M,N\) leaves \(L\) first. To move it to the end, one can pass it across \(M\otimes N\) in one step or pass it across \(M\) and then \(N\). A rule for exchanging pairs of factors must compare these two maps.

**Definition (braiding).** A braiding on a monoidal category is a natural family of isomorphisms
\[
\beta_{M,N}:M\otimes N\longrightarrow N\otimes M,
\]
compatible with tensoring in either variable. With parentheses identified by the associator, these two requirements are the hexagon equations
\[
\beta_{L,M\otimes N}
=(\mathrm{id}_M\otimes\beta_{L,N})
(\beta_{L,M}\otimes\mathrm{id}_N),
\tag{2.9}
\]
\[
\beta_{L\otimes M,N}
=(\beta_{L,N}\otimes\mathrm{id}_M)
(\mathrm{id}_L\otimes\beta_{M,N}).
\tag{2.10}
\]
Equation (2.9) takes \(L,M,N\) to \(M,N,L\), either in one move or through \(M,L,N\). Equation (2.10) takes the same initial order to \(N,L,M\), either moving the pair \(L,M\) at once or through \(L,N,M\). Two successive exchanges of the same pair need not return the identity. This distinction matters for lines whose continuation around each other contributes a phase.

Which exchange intertwines the actions? For \(H\)-modules the ordinary flip changes \(\Delta(h)\) to \((\tau\Delta)(h)\). It works when \(\Delta=\tau\Delta\). In a quasitriangular Hopf algebra an invertible tensor \(\mathcal R\in H\otimes H\), the universal \(R\)-matrix, corrects the flip. Its identity \(\mathcal R\Delta(h)=(\tau\Delta)(h)\mathcal R\) makes \(\beta_{M,N}=\tau\circ(\rho_M\otimes\rho_N)(\mathcal R)\) an intertwiner. To test a crossing of three factors, put \(\mathcal R\) in slots \(i,j\) and the unit in the unused slot, writing \(\mathcal R_{ij}\). The identities \((\Delta\otimes\mathrm{id})\mathcal R=\mathcal R_{13}\mathcal R_{23}\) and \((\mathrm{id}\otimes\Delta)\mathcal R=\mathcal R_{13}\mathcal R_{12}\) give the two hexagons. For local fields the exchange may also depend on separation or analytic continuation along a braid.

Here *coherence* means these specified compatibility equations. For complexes, some equalities are replaced by homotopies, which must satisfy further equations of their own. Retaining an associator without its pentagon, or a binary homotopy without the next compatibility, retains only part of the structure.

### A tensor product that remembers where two lines meet {#ch02-ising-matching-ends}

The preceding constructions take the state space of a pair to be its ordinary tensor product. For physical lines one can test this assumption just by counting dimensions. If fusion corresponds to ordinary tensoring and the vacuum corresponds to a one-dimensional space, what dimension can the spin line of the Ising model have?

::: example {#ch02-ising-fibre title="Ising fusion over the algebra of sectors"}
In the Ising conformal field theory at central charge \(1/2\), the three simple sectors are the vacuum \(1\), a fermion \(\psi\), and the spin sector \(\sigma\). A simple sector has no proper nonzero subobject. Fusion, denoted \(\boxtimes\), combines two sectors and can split into a direct sum of possible channels. The fusion rules include
\[
\begin{aligned}
\psi\boxtimes\psi&=1,\\
\psi\boxtimes\sigma&=\sigma,\\
\sigma\boxtimes\sigma&=1\oplus\psi .
\end{aligned}
\]
Suppose a faithful additive assignment to finite-dimensional complex vector spaces were to send the vacuum to \(\mathbb C\) and fusion to ordinary tensor product. The first rule would make the fermion space one-dimensional. The last would then require the spin space to have integer dimension \(d\) with \(d^2=2\).

A fibre functor to ordinary vector spaces would preserve the unit and fusion up to coherent isomorphisms and so would face this obstruction. At a junction there is more to record than the line \(X\) itself. A sector \(j\) can enter the line and a sector \(i\) can leave it. Use separate commuting actions to select these two labels, a left action for \(i\) and a right action for \(j\). A space with the two actions is called a *bimodule*. For fixed labels the junction space is
\[
V_X(i,j)=\operatorname{Hom}(i,X\boxtimes j)
\]
where a vector is a map from the outgoing simple \(i\) into \(X\boxtimes j\). Let \(A=\mathbb C^3\), with \(e_s\) the coordinate idempotent for sector \(s\). For \(v\in V_X(i,j)\) we have \(e_i v=v\) and \(v e_j=v\). Every other coordinate idempotent on the respective side kills \(v\). These two actions make \(V_X=\bigoplus_{i,j}V_X(i,j)\) an \(A\)-bimodule. For a pair \(v\otimes w\) in the ordinary tensor product \(V_X\otimes V_Y\), select the same intermediate sector on the right of \(v\) and the left of \(w\). The resulting projector is
\[
v\otimes w\longmapsto\sum_i ve_i\otimes e_iw .
\]
In \(V_X\otimes_A V_Y\) the balancing relation is \(ve_s\otimes w=v\otimes e_s w\). If \(v\) has right label \(s\) and \(w\) has a different left label, this relation sets \(v\otimes w\) to zero. On a pair with matching labels the projector is the identity. Such a pair consists of maps \(v:i\to X\boxtimes s\) and \(w:s\to Y\boxtimes j\). Their composite \((\mathrm{id}_X\boxtimes w)\circ v\) maps \(i\) into \(X\boxtimes(Y\boxtimes j)\). In the semisimple Ising category, the space of maps \(s\to Y\boxtimes j\) is the multiplicity space of the simple summand \(s\) in \(Y\boxtimes j\). Decomposing into these summands identifies the direct sum over \(s\) of the matching tensor products with the whole space of maps \(i\to X\boxtimes(Y\boxtimes j)\) by composition. Postcompose with the inverse associator \(\alpha_{X,Y,j}^{-1}\) to obtain a map into \((X\boxtimes Y)\boxtimes j\). Summing over the two external labels \(i,j\) now gives \(V_X\otimes_A V_Y\simeq V_{X\boxtimes Y}\).

For \(X=1,\psi,\sigma\) the junction spaces have dimensions \(3,3,4\), respectively. A spin line accepts one junction for input \(1\), one for \(\psi\) and two for \(\sigma\). Two spin lines have sixteen unrestricted pairs. The matching tensor product keeps six, since the two possible fused lines are \(1,\psi\), each with three junctions. Thus a change in what one tensors accounts for the failure of the scalar dimension test.

In the weak Hopf algebra reconstructed from these three endomorphism blocks, \(\Delta(1)\) acts by the matching projector. The algebra has dimension \(3^2+3^2+4^2=34\), and its tensor unit carries all three sector labels. Fusion determines these dimensions. Specifying which continuation represents an oriented half-exchange also requires the marked braiding. [The Ising half-turn](12-chiral-quantum-groups.md#ch12-ising-half-turn)
:::

## Universal maps and the other meaning of counit {#ch02-universal-maps-and-the-other-meaning-of-counit}

The junction construction imposed relations on an ordinary tensor product. Now ask the reverse question for an ordinary unital algebra \(A\). Given a space \(V\) of generators with no prescribed \(A\)-action, which module admits *every* linear assignment of those generators to an \(A\)-module \(M\)? It must contain both \(v\) and each formal product \(av\), subject only to linearity and the action laws. Set \(F(V)=A\otimes V\), include \(v\) as \(1_A\otimes v\), and let \(b(a\otimes v)=ba\otimes v\). Write \(U(M)\) for the underlying vector space of \(M\). Each linear map \(g:V\to U(M)\) now extends by the action to
\[
\widetilde g:A\otimes V\longrightarrow M,
\qquad
\widetilde g(a\otimes v)=ag(v).
\]
Conversely, an \(A\)-linear map \(\widetilde g\) is determined by its values on \(1_A\otimes V\). Thus
\[
\operatorname{Hom}_A(FV,M)
\cong\operatorname{Hom}_k(V,UM).
\tag{2.11}
\]
**Definition (adjunction).** A functor \(F\) is left adjoint to \(U\), written \(F\dashv U\), if maps \(FV\to M\) correspond bijectively to maps \(V\to UM\), naturally in both inputs. In (2.11) the correspondence restricts a module map to the generators \(1_A\otimes v\), and its inverse applies the action. This property gives \(F(V)\) its name, the free left \(A\)-module on \(V\).

The same bijection applied to identities produces the two comparison maps. First set \(M=FV\) in (2.11). The identity of \(FV\) restricts to the generators \(1_A\otimes v\), giving the unit
\[
\eta_V:V\longrightarrow UFV,\qquad v\longmapsto1_A\otimes v.
\]
For the counit, fix a module \(M\) and set \(V=UM\) in (2.11). Now extend the identity of \(UM\) by the action of \(A\). The resulting module map evaluates each formal product in \(M\),
\[
\varepsilon_M:FUM\longrightarrow M,\qquad a\otimes m\longmapsto am.
\tag{2.12}
\]
The first triangle identity applies \(F\eta_V\) and then \(\varepsilon_{FV}\). It sends \(a\otimes v\) to \(a\otimes1_A\otimes v\), then multiplies \(a\) by \(1_A\) and returns \(a\otimes v\). The second applies \(\eta_{UM}\) and then \(U\varepsilon_M\), sending \(m\) to \(1_A\otimes m\) and then to \(m\). Thus each composite is the identity on the object where it starts.

Take \(A=k[x]\) with its additive coproduct and \(M=k_\lambda\). The adjunction counit sends \(x\otimes1\in A\otimes U(M)\) to \(\lambda\in M\), the action of \(x\) on that state. The coalgebra counit sends \(x\in A\) to \(0\in k\), its action on the tensor unit. The inputs and outputs of these two operations explain their different values. In a derived adjunction it is again the first kind of counit that compares a reconstructed module with its target. [The derived comparison maps](06-duality-and-induction.md#adjunction-comparison-maps)

The charge example gave a rule for a single generator acting on two states. If a charged line ends at a point, there is a physical way to apply that generator to the state there. Integrate the current once around the endpoint and divide by \(2\pi i\). The Laurent coefficient selected by that contour acts on the endpoint state. Varying the weight will give further operators on the same state. [Fields and their modes](03-local-fields.md#fields-and-modes)
