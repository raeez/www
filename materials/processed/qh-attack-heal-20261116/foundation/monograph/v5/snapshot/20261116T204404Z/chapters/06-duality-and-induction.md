# Derived adjunctions and induction

A representation can be studied through the maps into it from a chosen module \(W\). These maps carry an action of the endomorphisms of \(W\), and tensoring them back with \(W\) gives a candidate reconstruction. The question is whether
\[
W\otimes_B^{\mathbf L}\operatorname{RHom}(W,M)\longrightarrow M
\]
recovers the original representation, where \(B\) is the appropriate derived endomorphism algebra with its opposite multiplication. The arrow matters: an isomorphism between the two objects would not by itself identify this reconstruction map.

For affine current algebras, the useful \(W\) has an entire horizontal regular representation at its lowest energy. Its endomorphisms lead to a differential graded algebra with even current generators and odd generators recording relations. We will obtain a conditional reconstruction theorem for every ordinary unbounded module over this algebra in the nonrational \(\mathfrak{sl}_3\) case. The mechanism is finite: four successive derived augmentation factors vanish. At other levels, explicit infinite extensions show why the same conclusion can fail.

## What the unit and counit measure {#adjunction-comparison-maps}

For a differential graded (dg) algebra \(B\), the ordinary derived category \(D(B)\) is obtained from complexes of \(B\)-modules by inverting quasi-isomorphisms. We retain its enhancement, so derived mapping complexes and their composition remain available. There is no bound on cohomological degrees. As before, differentials raise degree by one and \(L[1]^n=L^{n+1}\).

Let \(A\) be another dg algebra and let \(W\) be an \(A\)-\(B\) bimodule. Derived tensor and derived Hom give an adjunction
\[
\Phi=W\otimes_B^{\mathbf L}-:D(B)
\rightleftarrows D(A):
\Psi=\operatorname{RHom}_A(W,-).
\]
Its defining property is the natural equivalence
\[
\operatorname{RHom}_A(\Phi L,M)
\simeq\operatorname{RHom}_B(L,\Psi M).
\]
The **unit** \(\eta_L:L\to\Psi\Phi L\) corresponds to the identity of \(\Phi L\); the **counit** \(\varepsilon_M:\Phi\Psi M\to M\) corresponds to the identity of \(\Psi M\). In degree zero the counit is evaluation. Derived resolutions supply its meaning on complexes. These are adjunction maps, distinct from an algebra unit or a coalgebra counit.

The two triangle identities are
\[
\varepsilon_{\Phi L}\circ\Phi(\eta_L)=1_{\Phi L},
\qquad
\Psi(\varepsilon_M)\circ\eta_{\Psi M}=1_{\Psi M}.
\]
They express compatibility of the two reconstructions. The functor \(\Phi\) is fully faithful precisely when every \(\eta_L\) is an equivalence. The functor \(\Psi\) is fully faithful precisely when every \(\varepsilon_M\) is an equivalence. An equivalence of the two whole categories requires both.

::: figure fig-adjunction-triangles

Already extension of scalars requires the derived tensor. Put \(R=\mathbb C[x]\) and \(K=R/(x)\). The free resolution
\[
\bigl[R\xrightarrow{x}R\bigr]\longrightarrow K,
\]
with the two free terms in degrees \(-1,0\), gives
\[
K\otimes_R^{\mathbf L}K
\simeq\bigl[K\xrightarrow{0}K\bigr]
\simeq K\oplus K[1].
\]
Ordinary tensor retains only the degree-zero copy. The other copy records the relation \(x=0\). This is the simplest instance of the information carried by a bar resolution. Extension and restriction of scalars, with their derived adjunction, are described in the [Stacks Project, Example 22.33.6](https://stacks.math.columbia.edu/tag/0BYX).

A right dg module \(P\) is **K-flat** if \(P\otimes_B X\) is acyclic whenever the left dg module \(X\) is acyclic. Such a module computes derived tensor on arbitrary coefficients. Dually, a complex \(J\) is **K-injective** if its Hom complex from every acyclic complex is acyclic. This condition concerns the whole complex; injectivity of each term alone does not suffice in the unbounded case. See the [Stacks Project, §13.31](https://stacks.math.columbia.edu/tag/070G).

## Affine currents and the algebra acting on their resolution {#ch06-affine-currents-and-the-algebra-acting-on-their-resolution}

Let \(\mathfrak g\) be a nonzero finite-dimensional simple complex Lie algebra. Choose an invariant form \(\kappa\), normalized so that long roots have squared length two, and write
\[
\tfrac12\operatorname{tr}(\operatorname{ad}x\,\operatorname{ad}y)
=h^\vee\kappa(x,y).
\]
The integer \(h^\vee\) is the dual Coxeter number. For a scalar parameter \(k\), set \(\ell=(-k-h^\vee)\kappa\). The affine mode algebra \(A_\ell\) has relations
\[
[xt^r,yt^q]=[x,y]t^{r+q}
+r\delta_{r+q,0}\ell(x,y)1.
\]
The scalar \(-k-h^\vee\) is its **raw affine level**: it is the coefficient of the central cocycle in this normalization. The mode algebra here has no degree derivation. Its internal energy grading assigns energy \(-r\) to \(xt^r\).

Put
\[
\mathfrak n=t\mathfrak g[t],\qquad
\mathfrak l=\mathfrak g[t^{-1}],\qquad
R=U(\mathfrak g),\qquad H=U(\mathfrak l).
\]
A module is **smooth** if each vector is annihilated by \(t^N\mathfrak g[t]\) for some \(N\), which may depend on the vector. Consider the induced smooth module
\[
W=A_\ell\otimes_{U(\mathfrak n)}\mathbb C.
\]
The Poincaré–Birkhoff–Witt theorem identifies its underlying vector space with \(H\). Its energy-zero part is the regular \(R\)-module. This distinguishes \(W\) from the scalar-top vacuum
\[
V=A_\ell\otimes_{U(\mathfrak g[t])}\mathbb C,
\]
whose energy-zero part is \(\mathbb C\).

The polynomial dg algebra \(B=Y_k(\mathfrak g)\) has even generators \(b_m^a\) and odd generators \(c_{a,m}\), for \(m\ge0\). Fix a basis \(t_a\), write \([t_a,t_b]=f_{ab}{}^ct_c\), and sum repeated Lie-algebra indices. Its relations and differential are
\[
\begin{aligned}
[b_m^a,b_n^b]&=f_{ab}{}^cb_{m+n}^c,\\
[b_m^a,c_{b,n}]&=-f_{ac}{}^bc_{c,m+n},
&c_{a,m}c_{b,n}&=-c_{b,n}c_{a,m},\\
dc_{a,m}&=\tfrac12f_{bc}{}^a
 \sum_{r+p=m-1}c_{b,r}c_{c,p},\\
db_m^a&=mk\kappa_{ab}c_{b,m-1}
+\tfrac12f_{ab}{}^c
 \sum_{r+p=m-1}(c_{b,r}b_p^c+b_p^cc_{b,r}).
\end{aligned}
\]
Negative indices contribute nothing. The cohomological degrees of \(b,c\) are \(0,1\); their internal weights are \(m,m+1\). The differential preserves weight. The odd generators are often called ghosts; here that word means these specified degree-one algebra generators.

Write \(B_w\) for the entire weight-\(w\) complex. Then
\[
B=\bigoplus_{w\ge0}B_w,\qquad B_0=R,\qquad
I=\bigoplus_{w>0}B_w.
\]
There are two useful quotients:
\[
B\xrightarrow{q}H\xrightarrow{e_0}R,\qquad
q(c_{a,m})=0,\quad q(b_m^a)=t_at^{-m}.
\]
The map \(e_0\) kills the strictly negative modes. Thus \(p=e_0q\) is weight-zero projection and \(I=\ker p\). These quotients forget different information. An \(H\)-module inflated along \(q\) has zero ghost action but may have nonzero negative-current action. Inflation from \(R\) kills both.

The affine Chevalley resolution of \(W\) has
\[
P^{-p}=A_\ell\otimes\Lambda^p\mathfrak n.
\]
Its differential combines current multiplication with the Lie bracket. For \(x\in\mathfrak l\), let \(a_x\) be the exterior derivation induced by \(y\mapsto\operatorname{pr}_{\mathfrak n}[x,y]\). The generators act on this resolution through
\[
\rho(b_m^a)=R_{t_at^{-m}}-a_{t_at^{-m}},
\qquad
\rho(c_{a,m})=\iota_{a,m+1},
\]
where \(R_x\) is right multiplication on the affine factor and \(\iota_{a,m+1}\) is contraction with the indicated positive mode. This specified generator action is called the **native action**. The correction \(a_x\) is essential: its commutator supplies the half-Killing-form shift in \(\ell\). With the graded opposite composition, these operators give the algebraic derived endomorphism comparison. This construction is developed in *A derived endomorphism model for the line algebra*, the affine-resolution and generator-lift sections.

We must specify an additional smooth realization before using ordinary smooth derived Hom. Assume that the operators above are realized by a coherent right-\(B\) object \(\mathcal W\) in
\(\mathscr S_\ell=D(\operatorname{Sm}(A_\ell))\), with underlying object \(W\). Assume the prescribed homogeneous endomorphism comparison and the compatible smooth Taylor resolutions
\[
P_N=(A_\ell/A_\ell\mathfrak n_N)
\otimes\Lambda^\bullet(\mathfrak n/\mathfrak n_N),
\qquad \mathfrak n_N=t^N\mathfrak g[t],
\]
including their action comparisons on a common sufficiently large cutoff for each finite operator diagram. “Coherent” here includes all the higher compatibility homotopies for the right action. Finally assume the resulting enhanced adjunction
\[
\Phi=\mathcal W\otimes_B^{\mathbf L}-:
D(B)\rightleftarrows\mathscr S_\ell:
\Psi=\operatorname{RHom}_{\operatorname{Sm}(A_\ell)}(\mathcal W,-).
\tag{6.1}
\]
These are the smooth realization hypotheses used below. They identify a particular action and adjunction; they do not assert the desired unit theorem. They also keep smooth derived Hom distinct from derived Hom in all algebraic \(A_\ell\)-modules.

There is a parallel internally graded version. Modules are algebraic direct sums of their energy components, with arbitrary support. Set \(L\langle r\rangle_w=L_{w-r}\). Mapping complexes are formed at a specified homogeneous shift; their outer sum is algebraic. Neither convention introduces an energy completion.

## Cofree coefficients give the first unit theorem {#ch06-cofree-coefficients-give-the-first-unit-theorem}

The restricted positive-current dual
\[
C_{\mathfrak g}=\bigoplus_{E\ge0}U(\mathfrak n)_E^\vee
\]
uses the positive current degree \(\deg(xt^r)=r\). Each summand is finite dimensional, and every element of \(C_{\mathfrak g}\) has finite support in this degree. Put
\[
(L_x\phi)(u)=\phi(xu),\qquad
(D_x\phi)(u)=\phi(ux).
\]
Both actions lower the support bound of a functional. For a homogeneous positive-current basis \(x_i=t_at^r\), write \(c_i=c_{a,r-1}\). The complex
\[
\mathcal Q=C_{\mathfrak g}\otimes B,\qquad
d_{\mathcal Q}(\phi\otimes b)
=\phi\otimes db+\sum_iL_{x_i}\phi\otimes c_i b
\tag{6.2}
\]
has a pointwise finite differential. Its support filtration makes it semifree as a right \(B\)-module: the differential of a new free generator uses generators of smaller support degree.

The full affine action is restricted coinduction. Using the even \(H\)-action on the underlying graded algebra \(B\), identify \(\mathcal Q\) with
\[
\{f\in\operatorname{Hom}_H(A_\ell,B):
f|_{U(\mathfrak n)_{\ge d}}=0\text{ for some }d\},
\qquad (af)(b)=f(ba).
\]
The Poincaré–Birkhoff–Witt decomposition gives the preceding tensor description. The twist in (6.2) makes its differential affine-linear at precisely the level \(\ell=(-k-h^\vee)\kappa\).

Under the smooth realization hypotheses, \(\mathcal Q\) is equivalent to the whole coherent right-\(B\) object \(\mathcal W\), with its affine action retained. Consequently it computes \(\Phi L\) for every ordinary unbounded \(L\). This is the cofree-model theorem in *The cofree native model and inflated-base unit for every simple Lie algebra*. The comparison preserves the specified action on \(P\).

If \(T\) is an arbitrary unbounded \(H\)-complex inflated to \(B\), every ghost acts by zero. Formula (6.2) becomes
\[
\Phi T\simeq(C_{\mathfrak g}\otimes T,1\otimes d_T).
\]
Its positive-current action is \(D\) on the first factor. The restricted dual with arbitrary vector-space coefficients is injective in the smooth positive-current category. More is needed for an unbounded \(T\): split its underlying complex over \(\mathbb C\) into its cohomology and a contractible complex. Tensoring this splitting with \(C_{\mathfrak g}\) is positive-current-linear. It exhibits the restriction as homotopy equivalent to a product of injectives placed in single degrees, hence as K-injective. At each degree only one of those factors contributes; no completion of \(C_{\mathfrak g}\) is involved.

The positive-current invariants are exactly \(\delta_1\otimes T\), where \(\delta_1\) extracts the scalar coefficient of \(U(\mathfrak n)\). Evaluation on this vector identifies the original signed tensor–Hom unit with the identity of \(T\).

**Conditional unit theorem for inflated coefficients.** For every simple \(\mathfrak g\) and every \(k\in\mathbb C\), under the smooth realization hypotheses of (6.1), the actual unit
\[
T\xrightarrow{\eta_T}\Psi\Phi T
\]
is an equivalence for every ordinary unbounded \(H\)-complex inflated along \(q\), and therefore for every inflated \(R\)-complex. This holds with arbitrary algebraic internal support or without an internal grading.

The theorem includes critical affine level. It also includes raw \(\mathfrak{sl}_2\) level \(-3\). Its proof uses the zero ghost action on these coefficients; the cofree realization formula alone does not establish the unit for a general \(B\)-module.

## Finite descent from a quotient {#ch06-finite-descent-from-a-quotient}

To reach modules with nonzero ghost action, consider first a general split dg algebra extension
\[
R\longrightarrow B\xrightarrow{p}R,\qquad p|_R=1,
\qquad I=\ker p.
\]
Assume \(R\) is an ordinary algebra, \(B\) is K-flat on both \(R\)-sides, and for a finite integer \(N\),
\[
I^{\otimes_R^{\mathbf L}N}\simeq0
\quad\text{as a complex of \(R\)-bimodules}.
\tag{6.3}
\]
The two multiplication actions are part of this assertion; \(R\) need not be central.

Let \(F=R\otimes_B^{\mathbf L}-\), and let \(U\) be restriction of scalars along \(p\), also called inflation. A relative bar resolution converts (6.3) into vanishing of the \(N\)-fold derived tensor of \(I\) over \(B\). For every \(L\), put
\[
T_j(L)=I^{\otimes_B^{\mathbf L}j}
\otimes_B^{\mathbf L}L,\qquad T_0(L)=L.
\]
There is a functorial tower
\[
0\simeq T_N(L)\longrightarrow T_{N-1}(L)
\longrightarrow\cdots\longrightarrow T_0(L)=L
\tag{6.4}
\]
whose triangles are
\[
T_{j+1}(L)\longrightarrow T_j(L)
\xrightarrow{u_{T_j(L)}}UF(T_j(L))
\longrightarrow T_{j+1}(L)[1].
\tag{6.5}
\]
Here \(u\) is the scalar-extension unit, distinct from \(\eta\) in (6.1). Every cofiber is inflated from an unrestricted \(R\)-complex with its actual outer \(R\)-action.

The bar argument explains the change of base from \(R\) to \(B\). Resolve an \(I\)-factor by terms
\[
\bigl(I\otimes_R I^{\otimes_R q}\otimes_R B\bigr)[q],
\qquad q\ge0.
\]
In an \(N\)-fold derived tensor over \(B\), each resulting bar term contains at least \(N\) copies of \(I\) tensored over \(R\). Such a term is acyclic by (6.3) and the two-sided K-flatness. Finite bar-length filtrations and their exact algebraic union prove the asserted vanishing without a cohomological bound.

For an exact enhanced adjunction \(\Phi\dashv\Psi\), the class of objects on which its unit is invertible is closed under finite triangles and retracts. Thus (6.4) proves:

**Finite descent theorem.** Under the split-extension, K-flatness and tensor-vanishing hypotheses above, the actual unit is invertible on every \(L\in D(B)\) if it is invertible on every unrestricted inflated \(R\)-complex.

The proof propagates the same natural transformation through (6.5). It never assumes that \(\Psi\) preserves an infinite coproduct. The construction and its map identifications are given in *A finite filtration from derived tensor nilpotence*, Theorems A–B.

Ordinary ideal multiplication cannot replace (6.3). For
\(B=\mathbb C[\epsilon]/(\epsilon^2)\), \(R=\mathbb C\) and \(I=(\epsilon)\), one has \(I^2=0\), but
\[
I^{\otimes_{\mathbb C}N}\cong\mathbb C
\qquad(N\ge1).
\]
The multiplication of two ideal elements vanishes; the tensor of those elements remains nonzero.

There is a second, weaker sufficient criterion. For a dg algebra map \(B\to H\), form its fibre \(J\to B\to H\) in the derived category of genuine \(B\)-bimodules. It suffices that one tensor power of the **fibre-inclusion map**
\[
\mu_N:J^{\otimes_B^{\mathbf L}N}\longrightarrow B
\tag{6.6}
\]
be zero as a bimodule morphism, together with invertibility of the unit on all inflated unbounded \(H\)-complexes. The tensor object in (6.6) need not vanish. A fixed bimodule nullhomotopy makes \(B\) a retract of \(\operatorname{cofib}(\mu_N)\); the latter is a finite extension of bimodules whose left action factors through \(H\). Tensoring this one diagram with \(L\) gives a coefficient-functorial retract and proves the unit theorem. See *Finite bimodule descent for the actual adjunction unit*, Theorem 1.1.

## Four factors suffice for nonrational \(\mathfrak{sl}_3\) {#ch06-four-factors-suffice-for-nonrational-mathfraksl3}

Now take
\[
\mathfrak g=\mathfrak{sl}_3(\mathbb C),\qquad
\kappa(x,y)=\operatorname{Tr}(xy),\qquad
s\in\mathbb C\setminus\mathbb Q,\qquad B=Y_{-s}.
\]
The raw affine level is \(s-3\). The complement of \(\mathbb Q\) here includes nonreal complex parameters. With \(R=U(\mathfrak{sl}_3)\) and \(I=\bigoplus_{w>0}B_w\), the algebraic theorem is
\[
I^{\otimes_R^{\mathbf L}4}\simeq0,
\qquad I^{\otimes_R^{\mathbf L}3}\not\simeq0.
\tag{6.7}
\]
Four is the smallest vanishing exponent. Both statements use the original two \(R\)-actions and hold with the grading retained or forgotten.

The finite exponent comes from a bound on possible representation-theoretic transitions. Choose the diagonal Cartan subalgebra \(\mathfrak h\subset\mathfrak{sl}_3\) and the positive roots determined by upper-triangular matrices, and put \(\rho=\tfrac12\sum_{\alpha>0}\alpha\), the finite Weyl vector. For an affine highest weight \(\xi\), let \(\mu=\xi|_{\mathfrak h}+\rho\). A real affine root \(\alpha+n\delta\) is integral for this weight precisely when
\[
(\mu,\alpha)+ns\in\mathbb Z.
\]
For each finite root \(\alpha\), there is at most one such \(n\). Otherwise a nonzero integer multiple of \(s\) would be an integer. The integral reflection group therefore has type \(1\), \(A_1\), or \(A_2\), with longest Coxeter length at most three.

This observation becomes a tensor theorem through a specific comparison. A horizontal Verma module is the highest-weight \(U(\mathfrak g)\)-module induced from a one-dimensional representation of a Borel subalgebra. For a horizontal module \(N\) in the bounded category-O range, the actual complex
\[
B_m\otimes_R^{\mathbf L}N
\]
computes positive-current derived invariants in energy \(a+m\) of the affine module induced from \(N\) placed at energy \(a\). Category O here consists of weight modules with locally finite positive-root action and the stated highest-weight finiteness conditions.

For \(m>0\), every surviving component makes a strict transition in a finite Bruhat order, the order on reflection words determined by inclusion of reduced subwords. The relevant states are parabolic double cosets: the left parabolic records integral zero-mode roots, and the right parabolic records the stabilizer of the affine highest weight. The length of the largest element in a state lies between zero and three and strictly increases along a surviving transition. Four successive positive weights cannot survive.

Each fixed tensor word is a bounded complex of finitely generated bimodules with locally finite diagonal adjoint action \(xv-vx\). These are the Harish–Chandra bimodule conditions used here. A detection theorem for these complexes promotes vanishing on all horizontal Verma tests to vanishing of the actual bimodule tensor words. Summing those words algebraically proves the first assertion of (6.7). The nonzero third power has the weight word \(B_1\otimes_R^{\mathbf L}B_2\otimes_R^{\mathbf L}B_1\). These are the mechanisms in *The fourth derived tensor power of the native sl3 positive ideal*, §§1–6, together with the third-power theorem. The finite-block input uses Fiebig, [*The combinatorics of category O for symmetrizable Kac–Moody algebras*, Theorem 2.2 and §§2.3–2.4](https://arxiv.org/abs/math/0305378v2).

**Conditional full-unit theorem.** Let \(B=Y_{-s}(\mathfrak{sl}_3)\), \(s\in\mathbb C\setminus\mathbb Q\), and let the affine algebra have raw level \(s-3\) with form \(\operatorname{Tr}(xy)\). Assume the smooth realization data of (6.1), including the specified right action, homogeneous endomorphism comparison, Taylor-resolution coherences and actual enhanced tensor–Hom adjunction. Then
\[
\eta_L:L\xrightarrow{\sim}\Psi\Phi L
\]
for every ordinary cohomologically unbounded \(B\)-complex, either ungraded or algebraically internally graded with arbitrary support.

Its proof has four concrete steps. First, the weight-zero projection is a split dg augmentation. Each \(B_w\) is a bounded complex whose terms are free on each \(R\)-side, so the required K-flatness holds on both sides. Second, (6.7) supplies the fourth-power vanishing. Third, \(B\to H\to R\) and the inflated-coefficient theorem identify the actual unit on every inflated \(R\)-complex. Fourth, the tower (6.4) with \(N=4\) propagates that unit to every \(L\). No assertion about \(\Psi\) on infinite sums enters this argument.

The same tower gives an algebraic consequence independent of the smooth realization: every \(L\) has at most four inflated \(R\)-complex factors, and \(R\otimes_B^{\mathbf L}-\) is conservative. Indeed, if \(F(L)=0\), the first triangle makes \(I\otimes_B^{\mathbf L}L\to L\) an equivalence. Iterating four times identifies \(L\) with zero. The theorem and these consequences are established in *The full ordinary native unit for sl3 at nonrational parameter*, §§1–3. For \(Y_k(\mathfrak{sl}_2)\), \(k\in\mathbb C\setminus\mathbb Q\), the corresponding conditional full-unit theorem uses a square-zero derived ideal and a two-factor reduction.

::: figure fig-four-step-descent

## The image and its original counit {#ch06-the-image-and-its-original-counit}

Write \(\operatorname{Loc}(W)\) for the smallest full stable subcategory containing \(W\) and closed under arbitrary coproducts and retracts. In the internally graded case use all energy shifts:
\[
\mathscr C=
\begin{cases}
\operatorname{Loc}_{\mathscr S_\ell}(W),&\text{ungraded},\\
\operatorname{Loc}_{\mathscr S_\ell}
\{W\langle r\rangle:r\in\mathbb Z\},&\text{graded}.
\end{cases}
\]
Under the preceding full-unit theorem,
\[
D(B)\simeq\mathscr C.
\tag{6.8}
\]
The source is generated by \(B\), or by all its internal shifts, using semifree resolutions. The left adjoint preserves coproducts and sends these generators to \(W\) and its shifts. Full faithfulness also lifts cones and retracts between image objects. These facts identify the image exactly with \(\mathscr C\).

The original counit, not an independently chosen evaluation, is the **coreflection** into this image:
\[
\Phi\Psi M\xrightarrow{\varepsilon_M}M.
\]
This means that for every \(C\in\mathscr C\), it induces an equivalence on derived maps from \(C\). To prove it, the second triangle identity and the full-unit theorem give
\[
\Psi(\varepsilon_M)=\eta_{\Psi M}^{-1}.
\]
The cone of \(\varepsilon_M\) is therefore killed by \(\Psi\), hence is right-orthogonal to \(\mathscr C\). In particular, (6.8) identifies a specified part of the smooth category; it does not assert that every smooth object lies there.

An object is compact in a category if maps from it commute with arbitrary coproducts. The free module \(B\) is compact in \(D(B)\), so \(W\) is compact **inside \(\mathscr C\)**, with all shifts included when graded. This is a relative compactness assertion. It makes no claim about mapping from \(W\) into arbitrary families outside \(\mathscr C\). The image, compactness and original-counit statements are proved in the same manuscript, §§4–6.

::: figure fig-programme-context-duality

## Infinite extensions at other levels {#ch06-infinite-extensions-at-other-levels}

Finite descent explains why the nonrational theorem reaches unbounded coefficients. Without it, invertibility on every finite stage need not survive an infinite construction.

At critical raw level \(-h^\vee\), take \(B=Y_0\) and
\[
E=B\otimes_R^{\mathbf L}\mathbb C,\qquad \Phi E\simeq V.
\]
Assume the smooth realization and its actual lower-energy unit theorem. Critical vacuum cohomology supplies extension classes
\[
V\longrightarrow V[1]\langle-(n+2)\rangle,\qquad n\ge0,
\]
whose finite consecutive products are all nonzero. Their construction uses the quadratic central field and its successive derivatives. The level-deformation classes correspond to differentials of independent polynomial coordinates under the Frenkel–Teleman theorem: [*Self-extensions of Verma modules and differential forms on opers*, Theorem 4.4](https://arxiv.org/abs/math/0401428).

Lift these classes through the unit on the individually lower-weight-bounded objects and form
\[
L=\operatorname*{hocolim}_{r\ge0}
E[r]\left\langle-\frac{r(r+3)}2\right\rangle.
\tag{6.9}
\]
A sequential homotopy colimit is the cone of \(1-\mathrm{shift}\) on the direct sum of its terms. Compactness of \(E\) detects a nonzero map \(E\to L\): its successive representatives are precisely the nonzero extension products. Thus \(L\ne0\).

After realization, the terms are shifted copies of the module \(V\), concentrated in different cohomological degrees. Every transition induces zero on cohomology, so \(1-\mathrm{shift}\) induces the identity on the cohomology of the direct sum. Its cone is zero. Consequently
\[
L\ne0,\qquad \Phi L=0,\qquad \eta_L:L\longrightarrow0.
\]
The lower weight bounds in (6.9) tend to minus infinity. Each finite stage keeps its valid unit. This is the theorem of *A critical-level kernel of the ordinary first-kind realization*, §§1–4, conditional on its specified smooth realization and lower-energy comparison.

Related extension telescopes give kernels at raw \(\mathfrak{sl}_2\) levels \(-4,-5,\ldots\), and at raw level \(-2h^\vee\) for every simple type, under the corresponding realization and lower-energy hypotheses. They also show that \(W\) can fail to be compact even in its own generated category. The precise sources are *Actual-unit kernels at negative integral shifted sl2 levels* and *A noncritical ordinary-unit kernel for every simple Lie algebra*.

These ordinary-derived statements coexist with an all-type, all-level induction equivalence using different weak equivalences. For dg \(Y_k\)-modules that are termwise algebraically smooth for the even modes, twisted induction at raw level \(k-h^\vee\) has an explicit restricted twisted-coinduction inverse after inverting exactly the maps that induction sends to affine quasi-isomorphisms. That class is a proper subclass of the ordinary quasi-isomorphisms. This source localization therefore retains information that localization at all ordinary quasi-isomorphisms discards. This is the equivalence in *Corrected induction: the inverse, the adjunction and the equivalence*, Theorem 8.1. Its functor, level convention and source localization are part of the statement.

## Raw level minus three distinguishes the two quotients {#ch06-raw-level-minus-three-distinguishes-the-two-quotients}

For \(\mathfrak{sl}_2\) at raw level \(-3\), the line algebra is \(B=Y_1\). Let
\[
V_j=V(-2j-1),\qquad
F_j=(B\otimes_RV_j)\langle-j^2\rangle,
\]
where \(V(\lambda)\) is the horizontal Verma module of highest weight \(\lambda\). There are actual degree-zero maps \(\beta_j:F_{j-1}\to F_j\) represented by positive-weight cycles. Their affine realizations send highest vectors to
\[
v_{j-1}\longmapsto
f_0^{\,2j-2}e_{-1}^{\,2j-1}v_j.
\tag{6.10}
\]
Here \(f_0\) is the horizontal lowering current and \(e_{-1}\) the mode-\(-1\) raising current. These are injective maps of affine Verma modules.

For \(L=\operatorname{hocolim}_j(F_j,\beta_j)\), the two quotients have different effects:
\[
R\otimes_B^{\mathbf L}L=0,\qquad
H\otimes_B^{\mathbf L}L\ne0,\qquad
\Phi L\ne0.
\tag{6.11}
\]
Projection to \(R\) kills every positive-weight transition, and a telescope with zero transitions is zero. Projection to \(H\) retains the ghost-free word (6.10). The resulting system consists of injective Verma maps and has a nonzero filtered colimit; the affine realization has the same property.

Moreover, for \(I=\ker(B\to R)\), every finite map
\[
I^{\otimes_B^{\mathbf L}N}\longrightarrow B
\]
induced by the ideal inclusion is nonzero. Thus both the tensor-object and fibre-map descent routes through \(B\to R\) fail at this parameter. The proof is *A nonzero native telescope killed by the zero-weight augmentation*, §§2–4.

The ghost quotient \(B\to H\) has a different fibre, and (6.11) gives no obstruction to its finite fibre-map criterion. The unit is already invertible on every inflated \(H\)-complex. It is also invertible on every \(B\otimes_R^{\mathbf L}T\) for an arbitrary unbounded horizontal \(R\)-complex \(T\), by *A finite cofree resolution for arbitrary horizontal coefficients at raw level minus three*. Whether the unit is invertible on every \(B\)-complex at this level remains open. The object in (6.11) is not an affine-realization kernel.

## Cellularity and derived torsion {#ch06-cellularity-and-derived-torsion}

There is another plausible description of the image in (6.8), expressed directly in positive-current modules. To keep its ideal distinct from \(I\subset Y_k\), put
\[
U_+=U(t\mathfrak g[t]),\qquad
\mathfrak a=\ker(U_+\to\mathbb C).
\]
A smooth module is **jointly augmentation-torsion** if every vector \(v\) is killed by one whole power \(\mathfrak a^r\). The exponent may depend on \(v\), but it must work for every element of that ideal power. Let \(\mathcal T\subset\operatorname{Sm}(A_\ell)\) be this torsion category and set
\[
D_{\mathfrak a}=
\{M\in\mathscr S_\ell:H^q(M)\in\mathcal T
\text{ for every }q\}.
\]
The cellular category \(\mathscr C\) generated by \(W\) and its required shifts lies in \(D_{\mathfrak a}\).

Finite augmentation quotients explain a substantial converse. Since \(\mathfrak g\) is simple, \(U_+\) is generated in positive current degree one, and
\[
\mathfrak a^r=\bigoplus_{d\ge r}(U_+)_d.
\]
The quotient \(U_+/\mathfrak a^r\) is finite dimensional. The induced module
\[
E_r=A_\ell\otimes_{U_+}(U_+/\mathfrak a^r)
\]
has a finite filtration with factors
\[
W\langle-j\rangle\otimes_{\mathbb C}(U_+)_j,
\qquad 0\le j<r,
\]
where the last factor is a multiplicity space. Resolutions by such modules show that every complex whose terms are torsion is cellular. Every object with bounded-below torsion cohomology is also cellular. These statements, and the cellular coreflector on the whole unbounded smooth category, are proved in *Augmentation torsion and unbounded affine cellularization*.

The torsion inclusion has its own derived adjunction,
\[
i:D(\mathcal T)\rightleftarrows
D(\operatorname{Sm}(A_\ell)):R\Gamma_{\mathfrak a}.
\tag{6.12}
\]
It differs from both (6.1) and the inclusion of \(\mathscr C\). In particular, the exact inclusion of abelian categories need not induce a fully faithful functor on their unbounded derived categories.

This failure occurs already for positive-current \(\mathfrak{sl}_2\), before adjoining negative affine modes. Let \(\mathcal S_+=\operatorname{Sm}(t\mathfrak{sl}_2[t])\), let \(\mathcal T_+\) be its joint-torsion subcategory, and put
\[
e_n=\frac{n(n+1)}2,\qquad
X=\bigoplus_{n\ge1}\mathbb C[n]\langle-e_n\rangle.
\]
For the actual derived torsion adjunction one has
\[
H^0R\Gamma_{\mathfrak a}(iX)_0
\cong
\frac{\prod_{n\ge1}K_n}{\bigoplus_{n\ge1}K_n}\ne0,
\qquad \dim K_n=2n+1.
\tag{6.13}
\]
But \(H^0X=0\). Hence the unit of this torsion adjunction is not invertible. Its counit on the cellular object \(iX\) also fails to be an equivalence, so it cannot be the cellular coreflection there. Without an energy grading the corresponding quotient still injects into degree-zero cohomology. An explicit positive-current splitting transfers the failure to affine raw level zero; no transfer to arbitrary affine level is asserted. See *An unbounded joint-torsion unit failure for positive-current sl2*.

Finite quotients nevertheless admit a precise local-duality theorem. For an integer \(N\ge1\), put
\[
\mathfrak n=t\mathfrak{sl}_2[t],\quad
\mathfrak g_N=\mathfrak n/t^N\mathfrak{sl}_2[t],\quad
R_N=U(\mathfrak g_N),\quad d_N=3(N-1).
\]
Let \(J_N\) be the augmentation ideal of \(R_N\) and
\(E_N^{\mathrm{cof}}=\varinjlim_r(R_N/J_N^r)^\vee\), with action
\((b\phi)(a)=\phi(ab)\). In the actual positive-current smooth category,
\[
R\Gamma_{\mathfrak a}(R_N)
\simeq E_N^{\mathrm{cof}}\otimes
(\det\mathfrak g_N)^\vee[-d_N].
\tag{6.14}
\]
The comparison identifies the actual torsion counit. In the graded convention the determinant-dual line has energy \(3N(N-1)/2\). The proof first uses finite-dimensional Lie-algebra duality, then compares the inflated counit cone through finite Chevalley complexes with bounded coefficient terms. It proves (6.14) for these objects, not a formula on arbitrary unbounded coefficients. See *Actual torsion of the smooth regular quotients* and its finite-quotient local-duality argument.

The full unbounded equality \(\mathscr C=D_{\mathfrak a}\) remains a separate question. Non-full-faithfulness of (6.12) does not decide that equality of object classes. Nor does termwise vanishing of a torsion functor prove vanishing of its derived value: a concrete quotient complex in the graded positive-current category has zero torsion in every term but is cellular and has nonzero actual derived torsion. K-injective replacement changes the calculation. This example is computed in *The graded quotient does not give an outside or kernel object*.

We therefore have a representation-theoretic equivalence onto a specified generated category in the nonrational \(\mathfrak{sl}_2\) and \(\mathfrak{sl}_3\) cases, explicit kernels at other levels, and a distinct unbounded torsion problem. A comparison with a physical boundary theory must still identify its module category and the actual operations acting on it. The next question is how an operation can act compatibly on every module and every map between modules. That requirement leads to [actions and derived centres](07-actions-and-centres.md).
