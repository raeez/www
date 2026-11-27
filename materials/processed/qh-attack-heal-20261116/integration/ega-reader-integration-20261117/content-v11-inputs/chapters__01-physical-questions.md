# Boundary observables and reconstruction

A boundary of a quantum field theory supports measurements of its own. Fields can be inserted at different points of the boundary, multiplied when their positions are distinct, and brought together through singular limits. Line operators can end on the boundary or connect one boundary condition to another. The reconstruction problem asks how much of the bulk theory is determined by these boundary observables and their operations.

The word *operations* is essential. A list of states, a partition function or an algebra at one point records only part of the information. We also need to know how observables combine as their positions vary, how they act on line operators, how two boundaries are joined, and how a state assigns amplitudes to the resulting expressions. A proposed reconstruction must compare these structures with structures defined independently in the bulk.

The programme’s **associative chiral algebras are not Beilinson–Drinfeld chiral algebras**. They are augmented, coherently associative algebras of configuration complexes for a specified convolution. Their augmentation ideals vanish at the empty configuration, and their bar coalgebras factorize across the prescribed separating opens. Beilinson–Drinfeld chiral algebras have a chiral Lie operation on a differential module. To obtain an associative word object from one, take its Chevalley coalgebra, restrict its collision maps to monotone surjections and its coproduct to consecutive cuts, and take associative cobar. A quantum-group structure further needs a compatible coproduct for a tensor combining systems at the same positions; that tensor and its interchange with configuration multiplication are additional data.

There are several mathematical constructions to compare. A bar construction reorganizes an algebra in terms of its relations and higher relations. A derived centre records compatible operations on its modules. A boundary field theory supplies observables, products and line operators by geometric and physical means. These descriptions can agree in particular regimes, but their names do not define a comparison between them. The main questions concern the actual maps, the domains on which they exist, and the operations they preserve.

## Reduction must retain the measurements {#reduction-must-retain-the-measurements}

The need for this extra structure already appears before quantum field theory. In a gas, pressure and temperature describe large-scale measurements without specifying each molecular trajectory. Elasticity describes displacements at scales large compared with atomic separation. In a low-energy field theory, one may integrate out modes above a chosen scale while retaining their contribution to interactions among the remaining modes. Each description chooses observables and a regime of accuracy; none is justified merely by having fewer variables.

An exact finite calculation separates two operations that are often confused: removing a variable from the notation and integrating over its fluctuations. Let \(x\) be a measured displacement and \(y\) an additional displacement coupled to it. In units in which the action is dimensionless, take
\[
S(x,y)=\frac12 ax^2+cxy+\frac12 by^2,
\qquad b>0,\qquad ab>c^2.
\]
Here \(x,y,a,b,c\) are real. The inequalities make the quadratic form positive. Let \(\hbar>0\) control the scale of fluctuations, and use ordinary Lebesgue measure. At fixed \(x\), the weight remaining after \(y\) is integrated out is
\[
Z_y(x)=\int_{\mathbb R}\exp\!\left(-\frac{S(x,y)}{\hbar}\right)\,dy.
\]
Completing the square gives
\[
S(x,y)
=\frac b2\left(y+\frac cbx\right)^2
 +\frac12\left(a-\frac{c^2}{b}\right)x^2,
\]
and hence
\[
Z_y(x)
=\sqrt{\frac{2\pi\hbar}{b}}\,
\exp\!\left[
-\frac{1}{2\hbar}\left(a-\frac{c^2}{b}\right)x^2
\right].
\tag{1.1}
\]
{#eq-gaussian-integral}

The result retains two pieces of information: the effective stiffness \(a-c^2/b\) and the factor \(\sqrt{2\pi\hbar/b}\). The stiffness agrees with \(a\) when \(c=0\), and the factor can equal one at particular parameter values. Setting \(y=0\) would leave \(e^{-ax^2/(2\hbar)}\) and omit these two outputs of the integration. Substituting the conditional mean \(y=-cx/b\) gives the effective quadratic form but does not perform the fluctuation integral.

The same distinction appears when the eliminated variable occurs in an observable. Its conditional moments are
\[
\langle y\rangle_x=-\frac cbx,
\qquad
\langle y^2\rangle_x=\frac{c^2}{b^2}x^2+\frac{\hbar}{b}.
\tag{1.2}
\]
{#eq-gaussian-moments}
The second term in \(\langle y^2\rangle_x\) is the variance. Replacing \(y\) by its mean loses it. Thus an exact reduction includes a rule for transporting observables, not only a new expression for the action.

For a polynomial \(f(x,y)\), write this rule as conditional expectation:
\[
\mathcal E(f)(x)
=Z_y(x)^{-1}
\int_{\mathbb R}
f(x,y)e^{-S(x,y)/\hbar}\,dy.
\]
It is linear and preserves the constant observable, but it is generally not multiplicative. Equations (1.2) give
\[
\mathcal E(y^2)-\mathcal E(y)^2=\frac{\hbar}{b}.
\tag{1.3}
\]
{#eq-conditional-product-defect}
An effective theory therefore needs to explain how products are transported. In field theory the analogous correction is a contraction of fields. With many insertions, the corrections must also agree when the same reduction is performed in different orders.

The factor in (1.1) poses another question. It cancels from normalized expectations at a single fixed value of the parameters, but it matters when unnormalized amplitudes are compared, when parameters vary, or when two pieces of a theory are glued. In an infinite-dimensional field theory, the corresponding determinants and their phases need their own definition. A theorem about normalized correlations is consequently different from a theorem about the vacuum amplitude.

::: figure fig-gaussian-reduction

## From products to local operations {#from-products-to-local-operations}

Ordinary multiplication takes two elements of an algebra \(A\) to another element:
\[
m:A\otimes A\longrightarrow A.
\]
For local observables, positions are part of the input. On a complex curve with coordinate \(z\), a field associated with a state \(a\) is written \(Y(a,z)\). It is an operator-valued formal series; its coefficients act on the state space. If \(a\) and \(b\) are inserted at distinct points \(z\) and \(w\), their product can have a pole as \(z\) approaches \(w\).

The basic current example has singular part
\[
J(z)J(w)\sim \frac{\kappa}{(z-w)^2}.
\tag{1.4}
\]
{#eq-current-singularity}
The symbol \(\sim\) here records only the terms singular at the diagonal \(z=w\); it does not assert equality of the complete product with the displayed function. The number \(\kappa\) is the central coefficient of this current algebra.

Even this one pole has two different expansions. In the region \(|w|<|z|\),
\[
\frac1{(z-w)^2}
=\sum_{n\ge0}(n+1)\frac{w^n}{z^{n+2}},
\]
whereas in \(|z|<|w|\),
\[
\frac1{(z-w)^2}
=\sum_{n\ge0}(n+1)\frac{z^n}{w^{n+2}}.
\tag{1.5}
\]
{#eq-local-expansions}
They describe the same rational function on different domains. In formal algebra, the domain is replaced by a prescribed order of Laurent expansion. Changing that order is a mathematical operation; it cannot be suppressed by writing both series as the same completed tensor.

::: figure fig-local-expansions

This is one reason to formulate local products geometrically. The configuration of distinct points is an open subset of the Cartesian power of the curve. Its complement consists of collision diagonals. A local algebra must describe products on the open subset and their permitted behaviour near those diagonals. For three or more points, it must also compare different orders of combining the insertions.

**Factorization** expresses the first part of this structure: observables in disjoint regions can be combined in a larger region, compatibly with further inclusions and regroupings. In a holomorphic theory, the dependence on the regions and insertion points is accompanied by holomorphic or differential-module data. Associative chiral constructions add the ordered operations needed in the programme. Their precise definitions will distinguish multiplication from a Lie bracket and one notion of chiral duality from another.

## Why representations and centres enter {#why-representations-and-centres-enter}

A local algebra is also tested by the objects on which it acts. An ordinary representation of an algebra \(A\) is a vector space \(M\) with an action \(A\otimes M\to M\). In the field-theoretic setting, boundary conditions and line operators lead to corresponding module constructions. Combining two such objects requires more than knowing the action on each separately.

For an ordinary bialgebra \(H\), a coproduct \(\Delta:H\to H\otimes H\) supplies the diagonal action on \(M\otimes N\):
\[
h\cdot(m\otimes n)
=\sum h_{(1)}m\otimes h_{(2)}n,
\qquad
\Delta(h)=\sum h_{(1)}\otimes h_{(2)}.
\tag{1.6}
\]
{#eq-tensor-action}
The compatibility between multiplication and coproduct makes this an action. Coassociativity controls its associativity on three modules. Maps interchanging the factors require additional structure: cocommutativity supplies the usual flip, while a more general exchange requires a braiding and its compatibility equations. A chiral quantum group must solve the corresponding problem with local position-dependent operations.

Centres arise from a different aspect of representation theory. A central element of \(A\) acts on every \(A\)-module and commutes with the action. When modules and their relations are represented by complexes, the analogous compatible operations include homotopies. A derived centre retains that higher information. This gives a precise possible target for a bulk-to-boundary comparison: bulk observables may act compatibly on the boundary's modules and interfaces.

The existence of such an action does not by itself prove reconstruction. First one must construct the map from independently defined bulk observables and ask whether it recovers the observable algebra. A separate construction may give a functor \(F:\mathcal C_{\mathrm{bulk}}\to\mathcal C_{\partial}\) between categories of bulk and boundary modules. Full faithfulness is then a statement about that functor: it must identify the morphisms between every pair of modules, with the appropriate higher mapping data when these are present. An equivalence of the observable algebras and an equivalence of these module categories are distinct claims. Products, gluing and states impose further comparisons.

## The mathematical problem in its present form {#the-mathematical-problem-in-its-present-form}

The theory already contains substantial examples of the required structures. There are ordinary module duality theorems on explicitly stated parameter ranges; local operations for every finite number of inputs on a common formal domain; theorems characterizing specified factorizing objects through their actions; analytic conformal-block compositions; and numerical Gaussian states on controlled field domains. Geometric Hall constructions, branes and arithmetic trace theories provide further realizations with their own coefficients and operations.

Their limitations are informative because they distinguish the next comparisons. A theorem for every finite arity on one common Laurent-series space need not define an operation on separately completed intermediate spaces. A module duality at a generic parameter need not persist at a singular parameter. Agreement of traces need not identify a state algebra. A numerical state need not identify the state prepared by an independently specified geometric cap—a region with boundary, fields and boundary conditions whose path integral prepares that boundary state.

The central question is therefore concrete: **which algebraic and geometric operations can be transported between the independently defined constructions, on which objects, and with which normalizations?** The answers may include equivalences, exact restrictions to a class of modules, or obstructions to a specified comparison. Each answer must retain the positive structures it explains.

The Gaussian calculation gives the first criterion. A reduction must carry observables, their products and their normalization together. Locality adds positions and collision behaviour. Representation theory adds modules and the operation that combines them. The next chapter develops the ordinary algebraic maps that make these requirements precise; the subsequent chapters explain what changes when their inputs are local fields.

::: figure fig-programme-overview
