# Algebras, modules and combining systems

Let \(k\) be a field and \(H\) a unital associative \(k\)-algebra. A representation \(\rho_M:H\to\operatorname{End}_k(M)\) determines an action on \(M\). To define the diagonal action on \(M\otimes_k N\), one needs a coproduct \(\Delta:H\to H\otimes_k H\). If \(\Delta\) and its counit \(\epsilon:H\to k\) are unital algebra maps and \(\Delta\) is coassociative, then \(H\)-modules form a monoidal category with unit \(k_\epsilon\), the one-dimensional module defined by \(\epsilon\). A braiding on this category is further structure. Throughout this chapter tensor products are algebraic over \(k\) and vector spaces are ungraded.

## Multiplication and representations {#ch02-multiplication-and-representations}

A unital associative algebra consists of a vector space \(A\), a bilinear multiplication \(m:A\otimes A\to A\), and an element \(1_A\) such that
\[
(ab)c=a(bc),\qquad 1_Aa=a=a1_A.
\]
Equivalently, the unit is a linear map \(u_A:k\to A\), \(u_A(1)=1_A\). For an algebra of operators, associativity is the statement that three successive operations have a well-defined composite.

A left \(A\)-module is a vector space \(M\) together with an action \(\rho_M:A\otimes M\to M\) satisfying
\[
(ab)m=a(bm),\qquad 1_Am=m.
\]
A map of modules \(f:M\to N\) is a linear map with \(f(am)=af(m)\). Such a map compares the systems together with their observable actions, not merely their underlying vector spaces.

For example, let \(A=k[x]\). For every \(\lambda\in k\), there is a one-dimensional module \(k_\lambda\) on which \(x\) acts by multiplication by \(\lambda\). A module map \(f:k_\lambda\to k_\mu\) must satisfy
\[
\lambda f(1)=\mu f(1).
\]
In particular \(\operatorname{Hom}_{k[x]}(k_\lambda,k_\mu)=0\) if \(\lambda\ne\mu\), although both underlying vector spaces have dimension one. The category of representations retains the character \(x\mapsto\lambda\) and its intertwiners.

## A coproduct gives the action on a tensor product {#ch02-a-coproduct-gives-the-action-on-a-tensor-product}

Suppose \(M\) and \(N\) are representations of the same algebra \(H\). Their vector-space tensor product exists, but an \(H\)-action on it has not yet been specified. If we have a linear map
\[
\Delta:H\longrightarrow H\otimes H,
\]
we can try
\[
h\cdot(m\otimes n)
=\sum h_{(1)}m\otimes h_{(2)}n,
\qquad
\Delta(h)=\sum h_{(1)}\otimes h_{(2)}.
\tag{2.1}
\]
This is Sweedler notation for the algebraic tensor \(\Delta(h)\).

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
This is coassociativity. It compares two maps from \(H\) to \(H^{\otimes3}\).

There is also a distinguished one-dimensional representation if we have an algebra map \(\epsilon:H\to k\). It serves as the tensor unit when
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

The coproduct has a direct geometric origin. For an affine algebraic group \(G\), write \(\mathcal O(G)\) for its algebra of regular functions. Group multiplication is a map
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
The mixed term is forced by compatibility with multiplication. Under (2.1), the tensor product of \(k_\lambda\) and \(k_\mu\) is \(k_{\lambda+\mu}\). The action, tensor product and group law now express the same operation in three forms.

Thus \(\mathcal O(G)\) carries the Hopf algebra of functions on \(G\), with antipode \((Sf)(g)=f(g^{-1})\). The identity \(\mathcal O(G\times G)=\mathcal O(G)\otimes_k\mathcal O(G)\) uses affineness. For smooth or analytic observables, identifying functions on a product with a completed tensor product requires the chosen function spaces and topologies. Drinfeld treats the algebraic quantum-group formulation in *Quantum groups*, §1.

## Lie algebra actions and dual representations {#ch02-lie-algebra-actions-and-dual-representations}

Let \(\mathfrak g\) be a Lie algebra. Its universal enveloping algebra \(U(\mathfrak g)\) is generated by \(\mathfrak g\) with relations
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

In a monoidal category the associator is a natural isomorphism
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
agree. One path uses two associators; the other uses three. This is an equation of maps, not merely an assertion that the initial and final objects are isomorphic.

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

For \(H\)-modules the flip \(\tau\) intertwines the diagonal actions whenever \(\Delta=\tau\Delta\). More generally, for a quasitriangular Hopf algebra with universal \(R\)-matrix \(\mathcal R\), one has \(\mathcal R\Delta(h)=(\tau\Delta)(h)\mathcal R\). Its braiding is \(\beta_{M,N}=\tau\circ(\rho_M\otimes\rho_N)(\mathcal R)\). The two coproduct identities for \(\mathcal R\) give the two hexagons. For local fields the exchange operator can depend on the separation \(z-w\) or on analytic continuation along a braid.

Here *coherence* means these specified compatibility equations. For complexes, some equalities are replaced by homotopies, which must satisfy further equations of their own. Retaining an associator without its pentagon, or a binary homotopy without the next compatibility, retains only part of the structure.

### A tensor product that remembers where two lines meet {#ch02-ising-matching-ends}

A fibre functor to ordinary vector spaces must preserve fusion dimensions. In the semisimple Ising category at central charge \(1/2\), the simple line sectors are the vacuum \(1\), a fermion \(\psi\), and the spin field \(\sigma\). Write \(\boxtimes\) for their fusion. The relevant rules are
\[
\psi\boxtimes\psi=1,\qquad \psi\boxtimes\sigma=\sigma,\qquad
\sigma\boxtimes\sigma=1\oplus\psi .
\]
Suppose a faithful additive assignment to finite-dimensional complex vector spaces were to send the vacuum to \(\mathbb C\) and fusion to ordinary tensor product. The first rule would make the fermion space one-dimensional. The last would then require the spin space to have integer dimension \(d\) with \(d^2=2\).

A fibre functor to bimodules retains both endpoint labels. For a line \(X\) with incoming simple sector \(j\) and outgoing sector \(i\), the space
\[
V_X(i,j)=\operatorname{Hom}(i,X\boxtimes j)
\]
records all such junctions. To compose two junctions one must match the internal sector. If \(A=\mathbb C^3\) and \(e_i\) is the projector onto sector \(i\), then the direct sum \(V_X=\bigoplus_{i,j}V_X(i,j)\) is an \(A\)-bimodule. Tensoring it with \(V_Y\) over \(A\) performs exactly this matching. In the ordinary vector-space tensor product the projection to the matching pairs is
\[
v\otimes w\longmapsto\sum_i ve_i\otimes e_iw .
\]
The channel decomposition of \(Y\boxtimes j\) shows that the relative tensor gives \(V_{X\boxtimes Y}\). The three total dimensions are now \(3,3,4\). For instance, with \(X=\sigma\), the incoming sectors \(1,\psi,\sigma\) contribute one, one and two junctions respectively. The algebra of the three endomorphism blocks has dimension \(3^2+3^2+4^2=34\). Its tensor of modules uses the displayed projector and its unit carries all three sector labels. This gives a **weak Hopf algebra** in the finite reconstruction of [Chapter 12](12-chiral-quantum-groups.md). The fusion multiplicities determine the dimensions in this example. Specifying which continuation represents an oriented half-exchange also requires the marked braiding.

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

For \(F\dashv U\), evaluation \(\varepsilon_M:FUM\to M\) is a natural transformation of module functors. For a coalgebra, \(\epsilon:H\to k\) is a morphism of vector spaces satisfying (2.4). In the derived adjunction of Chapter 6 the relevant arrows are again a unit and a counit of functors. In the current algebra of Chapter 3 it is instead the position-dependent operator product (1.4) that must be defined.
