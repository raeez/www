# Algebras, modules and combining systems

Take two systems in states of definite electric charge, with charges \(\lambda\) and \(\mu\). A charge measurement on the combined system reads \(\lambda+\mu\). If the individual charge operators are \(Q_M\) on a state space \(M\) and \(Q_N\) on \(N\), the operator with this property on product states is
\[
 Q_{M\otimes N}=Q_M\otimes\mathrm{id}_N+\mathrm{id}_M\otimes Q_N .
\]
Which part of the mathematics says that charge should add? The tensor product of state spaces alone cannot decide. Two phases multiply when symmetries act simultaneously, whereas their infinitesimal generators add. These are two different rules for acting on the very same product state.

The algebraic question is how to specify such a rule once for *all* representations of a given symmetry. Throughout, \(k\) is a field, the vector spaces are ungraded, and \(M\otimes_kN\) denotes the algebraic tensor product. Its elements are finite sums of \(m\otimes n\), with the relations expressing bilinearity in \(m,n\).

## Multiplication and representations {#ch02-multiplication-and-representations}

Successive linear transformations of a state are represented by composing their operators. Abstracting this operation gives a **unital associative algebra**. It consists of a vector space \(A\), a bilinear multiplication \(m:A\otimes A\to A\), and an element \(1_A\) with
\[
 (ab)c=a(bc),\qquad 1_Aa=a=a1_A.
\]
The order matters when the operators do not commute. Associativity permits either grouping of three successive operations. The map \(u_A:k\to A\) with \(u_A(1)=1_A\) is called the unit.

A left \(A\)-module is a vector space \(M\) together with an action \(\rho_M:A\otimes M\to M\) satisfying
\[
(ab)m=a(bm),\qquad 1_Am=m.
\]
Equivalently, the action specifies a unital algebra map from \(A\) to \(\operatorname{End}_k(M)\), the algebra of linear operators on \(M\). A map of modules, or *intertwiner*, is a linear map \(f:M\to N\) satisfying \(f(am)=af(m)\). One may transport a state before applying the operator \(a\), or apply \(a\) before transporting it. This equation says the two results agree.

For example, let \(A=k[x]\). For every \(\lambda\in k\), there is a one-dimensional module \(k_\lambda\) on which \(x\) acts by multiplication by \(\lambda\). A module map \(f:k_\lambda\to k_\mu\) must satisfy
\[
\lambda f(1)=\mu f(1).
\]
In particular \(\operatorname{Hom}_{k[x]}(k_\lambda,k_\mu)=0\) if \(\lambda\ne\mu\), although both underlying vector spaces have dimension one. The category of representations retains the character \(x\mapsto\lambda\) and its intertwiners.

## A coproduct gives the action on a tensor product {#ch02-a-coproduct-gives-the-action-on-a-tensor-product}

In the example \(A=k[x]\), giving its action on \(M\) and \(N\) means choosing one operator on each space. To make \(M\otimes N\) a representation one must say how \(x\) acts there. For instance, if the two eigenvalues over \(\mathbb C\) are \(2\) and \(3\), the addition rule yields \(5\). The product rule \(x\mapsto x\otimes x\) yields \(6\). Each prescription on the generator extends to the polynomial algebra. The extra datum is the rule on *one observable* which says how it acts on *two systems*.

For a general symmetry algebra \(H\), an element \(a\otimes b\in H\otimes H\) already acts on product states by \(am\otimes bn\). Hence a map from \(H\) to this tensor product will define the combined action.

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
The indices in this **Sweedler notation** label the two factors of one summand of \(\Delta(h)\). The sum does not require a preferred basis or a preferred decomposition.

For (2.1) to be a representation, multiplication must be respected:
\[
\Delta(hh')=\Delta(h)\Delta(h'),\qquad
\Delta(1_H)=1_H\otimes1_H.
\tag{2.2}
\]
For three modules, the two resulting actions agree under the usual vector-space associator if
\[
(\Delta\otimes\mathrm{id})\Delta
=(\mathrm{id}\otimes\Delta)\Delta.
\tag{2.3}
\]
This condition is **coassociativity**. For the additive charge, both sides give \(Q\otimes1\otimes1+1\otimes Q\otimes1+1\otimes1\otimes Q\). They correspond to grouping the first two systems or the last two.

There is also a distinguished one-dimensional representation if we have an algebra map \(\epsilon:H\to k\). On a single vector \(1\in k\), \(h\) then acts by the scalar \(\epsilon(h)\). Adjoining this system to either side must leave every original action unchanged. Under \(k\otimes M\simeq M\simeq M\otimes k\), this requires
\[
(\epsilon\otimes\mathrm{id})\Delta
=\mathrm{id}
=(\mathrm{id}\otimes\epsilon)\Delta.
\tag{2.4}
\]
The map \(\epsilon\) is the **coalgebra counit**. An algebra \(H\) with \(\Delta\) and \(\epsilon\) satisfying (2.2)–(2.4) is a bialgebra.

The product–coproduct compatibility can be written as one equation between maps \(H\otimes H\to H\otimes H\):
\[
\Delta m
=(m\otimes m)
(\mathrm{id}\otimes\tau\otimes\mathrm{id})
(\Delta\otimes\Delta),
\tag{2.5}
\]
where \(\tau(a\otimes b)=b\otimes a\). The middle interchange places the first components together and the second components together. This equation is the ordinary model for one of the compatibility problems in a chiral quantum group. The chiral problem must specify the position-dependent operation spaces and their interchange before it can assert the corresponding equation.

## Group multiplication reverses direction on functions {#ch02-group-multiplication-reverses-direction-on-functions}

The combination rule can sometimes be read off from geometry. If the states are labelled by group elements \(g_1,g_2\), and \(f\) measures a function of a label, the combined reading is \(f(g_1g_2)\). It depends on *two* variables. For an affine algebraic group \(G\), write \(\mathcal O(G)\) for its algebra of regular functions. Group multiplication is a map
\[
\mu:G\times G\longrightarrow G.
\]
Pullback of functions reverses its direction:
\[
\mu^*:\mathcal O(G)\longrightarrow
\mathcal O(G\times G)
=\mathcal O(G)\otimes\mathcal O(G).
\]
This is the coproduct. Associativity of \(\mu\) becomes coassociativity of \(\mu^*\), and evaluation at the identity of \(G\) becomes the counit.

For the additive group, \(\mathcal O(G)=k[x]\), and
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad \epsilon(x)=0.
\tag{2.6}
\]
It follows that
\[
\Delta(x^2)=x^2\otimes1+2x\otimes x+1\otimes x^2.
\]
The middle term \(2x\otimes x\) is the contribution \(2\lambda\mu\) to the square of the *total* charge. Omitting it would give the sum of the separate squared charges. Under (2.1), the tensor product of \(k_\lambda\) and \(k_\mu\) is \(k_{\lambda+\mu}\). The action, tensor product and group law now express the same operation in three forms.

Group inversion also acts by pullback. The resulting map \(S\), called the **antipode**, sends \(f\) to \(g\mapsto f(g^{-1})\). For the additive coordinate \(S(x)=-x\), so combining a charge with its inverse gives the counit value zero. A bialgebra with such an inverse in the sense \(m(S\otimes\mathrm{id})\Delta=m(\mathrm{id}\otimes S)\Delta=u_H\epsilon\) is called a Hopf algebra. The identity \(\mathcal O(G\times G)=\mathcal O(G)\otimes_k\mathcal O(G)\) uses affineness. For smooth or analytic observables, identifying functions on a product with a completed tensor product requires the chosen function spaces and topologies. Drinfeld treats the algebraic quantum-group formulation in *Quantum groups*, §1.

## Lie algebra actions and dual representations {#ch02-lie-algebra-actions-and-dual-representations}

For a differentiable one-parameter symmetry with \(g(0)=1\), its action on \(M\otimes N\) is \(g_M(t)\otimes g_N(t)\). Differentiating at \(0\) gives \(\dot g_M(0)\otimes1+1\otimes \dot g_N(0)\). This explains why an infinitesimal generator obeys the additive rule even when the group acts by multiplication. A Lie algebra \(\mathfrak g\) describes these generators and their commutators through an alternating bilinear bracket satisfying the Jacobi identity. Alternation means \([x,x]=0\) for every \(x\), including in characteristic two, where antisymmetry alone gives \([x,y]=[y,x]\). Its universal enveloping algebra \(U(\mathfrak g)\) is generated by \(\mathfrak g\) with relations
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

Dual representations require a reversal as well. On the algebraic dual \(M^\vee=\operatorname{Hom}_k(M,k)\), the Lie action is
\[
(x\phi)(m)=-\phi(xm).
\tag{2.8}
\]
The minus sign makes the evaluation pairing invariant:
\[
(x\phi)(m)+\phi(xm)=0.
\]
For the enveloping algebra, this is expressed using the antipode \(S\), defined by \(S(x)=-x\) and \(S(ab)=S(b)S(a)\). The order reversal is necessary because transposing a product reverses the order of the operators.

In finite dimension, duality also gives the usual coevaluation map \(k\to M\otimes M^\vee\). In infinite dimension the formal expression \(\sum_i m_i\otimes m_i^\vee\) need not be an algebraic tensor. Evaluation, coevaluation and biduality therefore have different domain requirements. This distinction will recur when line operators and completed state spaces are compared.

## Associators, exchange and coherence {#ch02-associators-exchange-and-coherence}

The tensor product also acts on intertwiners. For example \(f\otimes g\) sends \(m\otimes n\) to \(f(m)\otimes g(n)\). In the category of vector spaces, the assignment \((\ell\otimes m)\otimes n\mapsto\ell\otimes(m\otimes n)\) commutes with applying a linear map to any of the three inputs. This is what *natural* means here. In a general category equipped with a tensor product and tensor unit, the corresponding comparison is specified by an **associator**, a natural isomorphism
\[
\alpha_{L,M,N}:(L\otimes M)\otimes N
\longrightarrow L\otimes(M\otimes N).
\]
For four objects, the pentagon identity says that the two paths from
\[
((L\otimes M)\otimes N)\otimes P
\quad\text{to}\quad
L\otimes(M\otimes(N\otimes P))
\]
agree. One path first forms the middle grouping \((L\otimes M)\otimes(N\otimes P)\). The other first reassociates \(L,M,N\) inside the left factor and makes two more moves. The pentagon requires equality of the resulting maps. Together with the compatible identifications with the unit, these data define a **monoidal category**.

A braiding is a natural family of isomorphisms
\[
\beta_{M,N}:M\otimes N\longrightarrow N\otimes M,
\]
compatible with maps of both input objects. It has its own compatibility with composition. With parentheses identified by the associator, its two hexagon equations read
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
These equations say that moving one object past a pair agrees with moving it past the two factors successively.

For \(H\)-modules the flip \(\tau\) intertwines the diagonal actions whenever \(\Delta=\tau\Delta\). More generally, for a quasitriangular Hopf algebra with universal \(R\)-matrix \(\mathcal R\), one has \(\mathcal R\Delta(h)=(\tau\Delta)(h)\mathcal R\). Its braiding is \(\beta_{M,N}=\tau\circ(\rho_M\otimes\rho_N)(\mathcal R)\). Writing \(\mathcal R_{ij}\) for the invertible tensor \(\mathcal R\in H\otimes H\) placed in slots \(i,j\) of \(H^{\otimes3}\) with the unit in the remaining slot, the identities \((\Delta\otimes\mathrm{id})\mathcal R=\mathcal R_{13}\mathcal R_{23}\) and \((\mathrm{id}\otimes\Delta)\mathcal R=\mathcal R_{13}\mathcal R_{12}\) give the two hexagons. For local fields the exchange operator can depend on the separation \(z-w\) or on analytic continuation along a braid.

Here *coherence* means these specified compatibility equations. For complexes, some equalities are replaced by homotopies, which must satisfy further equations of their own. Retaining an associator without its pentagon, or a binary homotopy without the next compatibility, retains only part of the structure.

### A tensor product that remembers where two lines meet {#ch02-ising-matching-ends}

How much of the tensor product of physical lines can ordinary vector spaces reproduce? In the Ising conformal field theory at central charge \(1/2\), the three simple sectors are the vacuum \(1\), a fermion \(\psi\), and the spin sector \(\sigma\). A simple sector has no proper nonzero subobject. Fusion, denoted \(\boxtimes\), combines two sectors and can split into a direct sum of possible channels. The fusion rules include
\[
\psi\boxtimes\psi=1,\qquad \psi\boxtimes\sigma=\sigma,\qquad
\sigma\boxtimes\sigma=1\oplus\psi .
\]
Suppose a faithful additive assignment to finite-dimensional complex vector spaces were to send the vacuum to \(\mathbb C\) and fusion to ordinary tensor product. The first rule would make the fermion space one-dimensional. The last would then require the spin space to have integer dimension \(d\) with \(d^2=2\).

Assigning a space to each line in a way that preserves the tensor product and unit is the purpose of a *fibre functor*. In this example a different target works. Its objects carry commuting left and right actions of an algebra and so are called bimodules. The two actions will record the two endpoint labels. For a line \(X\) with incoming simple sector \(j\) and outgoing sector \(i\), the space
\[
V_X(i,j)=\operatorname{Hom}(i,X\boxtimes j)
\]
records all such junctions. To compose two junctions one must match the internal sector. If \(A=\mathbb C^3\) and \(e_i\) is the projector onto sector \(i\), then the direct sum \(V_X=\bigoplus_{i,j}V_X(i,j)\) is an \(A\)-bimodule. Tensoring it with \(V_Y\) over \(A\) performs exactly this matching. In the ordinary vector-space tensor product the projection to the matching pairs is
\[
v\otimes w\longmapsto\sum_i ve_i\otimes e_iw .
\]
For example, given a junction \(s\to Y\boxtimes j\) and one \(i\to X\boxtimes s\), tensor the first map with \(X\) and compose to obtain \(i\to X\boxtimes(Y\boxtimes j)\). Decomposing \(Y\boxtimes j\) over all intermediate simple sectors \(s\) yields exactly \(V_{X\boxtimes Y}\). The three total dimensions are now \(3,3,4\). For instance, with \(X=\sigma\), the incoming sectors \(1,\psi,\sigma\) contribute one, one and two junctions respectively. The algebra of the three endomorphism blocks has dimension \(3^2+3^2+4^2=34\). Its tensor of modules uses the displayed projector and its unit carries all three sector labels. This gives a **weak Hopf algebra** in the finite reconstruction of [Chapter 12](12-chiral-quantum-groups.md). The fusion multiplicities determine the dimensions in this example. Specifying which continuation represents an oriented half-exchange also requires the marked braiding.

## Universal maps and the other meaning of counit {#ch02-universal-maps-and-the-other-meaning-of-counit}

There is another common source of units and counits that does not require a coproduct. Let \(F(V)=A\otimes V\) be the free left \(A\)-module on a vector space \(V\), and let \(U(M)\) denote the underlying vector space of an \(A\)-module. A linear map \(g:V\to U(M)\) extends uniquely to
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
This natural bijection is an adjunction \(F\dashv U\).

Its unit is the natural map
\[
\eta_V:V\longrightarrow UFV,\qquad v\longmapsto1_A\otimes v,
\]
and its counit is
\[
\varepsilon_M:FUM\longrightarrow M,\qquad a\otimes m\longmapsto am.
\tag{2.12}
\]
The first triangle identity sends \(a\otimes v\) to \(a\otimes1_A\otimes v\) and then back to \(a\otimes v\). The second sends \(m\) to \(1_A\otimes m\) and then to \(m\). These identities express the compatibility of the free construction with evaluation.

For \(F\dashv U\), evaluation \(\varepsilon_M:FUM\to M\) is a natural transformation of module functors. For a coalgebra, \(\epsilon:H\to k\) is a morphism of vector spaces satisfying (2.4). In the derived adjunction of Chapter 6 the relevant arrows are again a unit and a counit of functors. For a charge carried by a line ending at a point, one can also ask for a *local* way to measure the charge. A contour of the current around the endpoint gives such a measurement. To see why a contour defines an operator and how two contours compose, we need the Laurent coefficients of a field. [Chapter 3](03-local-fields.md#fields-and-modes)
