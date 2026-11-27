# From boundary operations to bulk reconstruction

The boundary reconstruction problem can now be stated without asking one invariant to carry several meanings. A local field algebra specifies position-dependent products. A category of representations specifies systems on which those products act. An interface specifies how to pass between two such categories. A state evaluates observables, while a geometric filling prepares a particular state with its amplitude and gluing law. Each construction has appeared in a concrete form in the preceding chapters.

The central question is whether these constructions agree with ones defined independently in the bulk. There is no single comparison whose existence follows from the word *holography*. There are maps of observables, functors on representations, compatibility with products and collisions, and comparisons of states and amplitudes. Their hypotheses may overlap without coinciding. The strongest available reconstruction is obtained by composing the maps on their common domains and retaining the distinctions outside those domains.

## Interfaces give an explicit reconstruction map {#interfaces-and-reconstruction}

The ordinary algebraic model is useful because all its arrows can be written. Let \(A,B\) be differential graded algebras and let \(P\) be an \(A\)-\(B\) bimodule. The two actions commute with the differential. A vector in \(P\) can therefore be acted on by \(A\) from the left and by \(B\) from the right, as an interface can be acted on from its two sides.

The derived functors
\[
F=P\otimes_B^{\mathbf L}-:D(B)\longrightarrow D(A),
\qquad
G=R\operatorname{Hom}_A(P,-):D(A)\longrightarrow D(B)
\tag{17.1}
\]
form an adjunction. Derived categories are used with their mapping complexes, as in Chapter 6. The right \(B\)-action on \(P\) produces the left \(B\)-action on the Hom complex by precomposition. The actual unit and counit are
\[
\eta_L:L\longrightarrow GF(L),
\qquad
\varepsilon_M:FG(M)\longrightarrow M.
\tag{17.2}
\]
They compare the original object with the result of passing through the interface and back. If all units are equivalences, \(F\) is fully faithful. The counit then identifies which objects of \(D(A)\) it reconstructs. Full faithfulness is already a reconstruction theorem on the image; equivalence with the whole target category requires that image to be the whole category.

For a complete finite example, take \(A=M_n(k)\), \(B=k\), \(P=k^n\), and let \(E_{ij}\) be the matrix units. Put \(e=E_{11}\). Then \(G(M)=eM\), and the counit is
\[
\varepsilon_M:k^n\otimes eM\longrightarrow M,
\qquad v_i\otimes m\longmapsto E_{i1}m.
\tag{17.3}
\]
Its inverse is
\[
M\longrightarrow k^n\otimes eM,
\qquad m\longmapsto\sum_i v_i\otimes E_{1i}m.
\]
The two composites are identities because \(E_{1j}E_{i1}=\delta_{ij}e\) and \(\sum_iE_{i1}E_{1i}=1_A\). The unit sends a vector \(v\) to \(v_1\otimes v\) in \(e(k^n\otimes V)\), so it is also an isomorphism. This proves the equivalence of module categories directly, including its maps.

The same example shows why a centre alone is insufficient. The algebra of upper triangular two-by-two matrices over \(k\) has centre \(k\), just as \(M_2(k)\) does. It has two nonisomorphic simple modules, obtained by evaluating the two diagonal entries; \(M_2(k)\) has one simple module up to isomorphism. Their module categories are not equivalent. A centre comparison and an interface equivalence answer different questions.

In a field theory, \(P\) is not an arbitrary bimodule selected to make (17.2) invertible. It must come from the prescribed line, junction or boundary condition. Its action, support and differential are part of the comparison. The finite matrix example gives the criterion to test; it does not identify any physical interface with \(k^n\).

## What the affine theorem reconstructs {#affine-reconstruction-scope}

Chapter 6 constructs this kind of comparison for the line algebra \(B=Y_{-s}(\mathfrak{sl}_3)\), with \(s\in\mathbb C\setminus\mathbb Q\), and affine raw level \(s-3\), with invariant form \(\kappa(x,y)=\operatorname{Tr}(xy)\). The induced object
\[
W=A_{s-3}\otimes_{U(t\mathfrak{sl}_3[t])}\mathbb C
\]
has a horizontal regular representation at energy zero. The generator action on its Chevalley resolution, including the correction to right multiplication, specifies the line action used in the adjunction.

Under the smooth realization hypotheses stated in that chapter—its prescribed right action, homogeneous endomorphism comparison, Taylor-resolution coherences and enhanced tensor–Hom adjunction—the original unit is invertible on every ordinary unbounded \(B\)-complex. Internal energy can be forgotten or retained with arbitrary algebraic support. The resulting equivalence is
\[
D(B)\simeq\mathscr C,
\qquad
\mathscr C=\operatorname{Loc}(W)
\tag{17.4}
\]
in the ungraded case; in the graded case all energy shifts of \(W\) generate \(\mathscr C\). Here \(\operatorname{Loc}\) means closure under shifts, cones, arbitrary coproducts and retracts inside the given smooth derived category. The actual counit \(\Phi\Psi M\to M\) is the coreflection into this subcategory.

The reach to unbounded complexes has an algebraic explanation. With \(R=U(\mathfrak{sl}_3)\) and positive-weight ideal \(I\),
\[
I^{\otimes_R^{\mathbf L}4}=0,
\qquad I^{\otimes_R^{\mathbf L}3}\ne0.
\tag{17.5}
\]
The finite descent tower reduces every source to four unrestricted inflated \(R\)-complexes. The cofree calculation already identifies the actual unit on those complexes. Finite triangles then extend that same natural transformation to every source. An unproved interchange of an infinite coproduct with the right adjoint is unnecessary.

This result retains several useful boundaries. It does not identify \(\mathscr C\) with every smooth affine object. It also does not identify the coreflection with the derived joint-torsion functor. Chapter 6 gives an unbounded positive-current example where the torsion adjunction has an additional product-modulo-sum class and fails to be fully faithful. At other affine levels, actual realization kernels coexist with the valid finite-stage unit. At raw \(\mathfrak{sl}_2\) level \(-3\), a different telescope survives realization but is killed by the weight-zero quotient; it obstructs that descent route, not realization itself.

The reconstruction theorem therefore identifies a precise category through a precise interface. To identify a separately defined physical boundary functor with this one, its action and right adjoint must be compared on the original complexes. Agreement of ordinary endomorphism algebras or of cohomology dimensions does not supply that comparison. The inflated-coefficient theorem for every simple type and every level remains available on its stated inputs, independently of whether a full-unit theorem holds there.

## Products must survive passage through the interface {#products-through-an-interface}

An equivalence of linear categories can forget the way systems combine. If \(\mathcal C\) and \(\mathcal D\) have specified tensor products, a monoidal comparison includes maps
\[
\gamma_{L,M}:F(L)\otimes_{\mathcal D}F(M)
\longrightarrow F(L\otimes_{\mathcal C}M)
\tag{17.6}
\]
and a unit comparison. Their associativity square compares the two maps obtained from three inputs, and the unit diagrams compare insertion of the tensor unit. A strong monoidal functor requires these maps to be equivalences. A braided comparison also includes the exchange square and its compatibility with the associator.

For local fields, the two tensor products in (17.6) may depend on positions and expansions. Chapter 12 supplies a complete positive example in the spectral class: the form \(\rho_z\) defines fields, their exchange, the cross-contracted tensor product, and a level-indexed coproduct preserving the fields. The field hexagon is an identity on a stated Laurent expansion space. This is substantially more information than an abstract coproduct on state vectors.

Chapter 8 supplies another positive result. For nonrational \(\mathfrak{sl}_2\), under its realization and finite-descent hypotheses, every finite tuple of ordinary unbounded line modules has a comparison with the independently defined radial current complex. Scalar extension to the shape field \(F\) occurs before completion to \(F((q))\). Rational evaluation and its affine restriction preserve the outgoing action and all stated incoming actions. Composition of the original kernels along a finite tree agrees on this common radial domain.

That conclusion does not define substitution on every separately completed intermediate tensor. The series
\[
\sum_{n\geq0}q^n\lambda^{-n^2}
\]
is a valid element of \(\mathbb C(\lambda)((q))\), whereas substituting \(\lambda=zq\) produces outer orders \(n-n^2\) with no lower bound. The proposed substituted series is outside the iterated Laurent space. A larger tensor comparison must impose and prove the support estimates that exclude this failure, or choose a different independently justified domain.

Likewise, an integral collision fibre cannot be obtained by setting the discriminant to zero in a space where it has been inverted. The finite integral heads in Chapter 8 carry actual derived collision maps before localization. Comparing those maps with the radial theorem requires the finite-head and completion comparisons together. A common formal expression is not a common domain.

## A bulk action and a universal centre {#bulk-action-and-centre}

In the ordinary associative case, Hochschild cochains
\[
C^\bullet(B,B)=R\operatorname{Hom}_{B\otimes B^{\mathrm{op}}}(B,B)
\]
act coherently on derived \(B\)-modules. This suggests a place for bulk observables that act compatibly on all boundary systems. In chiral geometry, however, the appropriate action problem includes the configuration opens, the tensor products, the pointing and the collision homotopies. Its representing object need not be the Hochschild complex of a two-dimensional test algebra.

Chapter 7 defines one such geometric problem exactly. A pointed factorizing coalgebra \((F,u)\) is tested against the Chevalley coalgebra \(C\) of the two-idempotent algebra. The complete character and action spaces are \(\mathcal X(F,u)\) and \(\mathcal A_C(F,u)\). Multiplication and vacuum evaluation give
\[
\Theta:\mathcal X(F,u)\longrightarrow\mathcal A_C(F,u),
\qquad
\Psi:\mathcal A_C(F,u)\longrightarrow\mathcal X(F,u),
\qquad \Psi\Theta\simeq1.
\tag{17.7}
\]
Recognition asks whether the other composite is homotopic to the identity with all the required compatibilities. This is proved for the full families stated in Chapter 7: arbitrary pointings on genuinely unital Chevalley coalgebras, their specified module extensions, and the nonunital families covered by the horizontal-representative or commutative-connection theorems. The three-block filling for arbitrary coassociative actors requires no cocommutativity. The separate old-base closed-corner comparison has its own coherent cocommutativity hypothesis and remains on the separated locus.

A universal geometric centre would represent the action space for every admitted pointed actor. Even if such representability is established, a bulk reconstruction still needs a map from the independently defined bulk observables to that centre. It must identify the actual action, its product and its support. The ordinary exterior-source mapping-space theorem is another exact positive result; it does not define this geometric bulk map by changing the name of its target.

There is also an accomplished classical geometric reconstruction. Chapter 13 constructs the complete ordinary coefficient-family system of a fixed unital chiral algebra, with arbitrary classical parameter schemes, compatible vacuum insertions and collision equivalences. Realizing the vacuum and applying the geometric residue construction returns the original chiral algebra. This theorem explains what additional geometric information makes reconstruction possible. Its ordinary tensors and fixed algebra are part of its scope; its conclusion does not assert a derived reconstruction of an interacting bulk theory.

## States and amplitudes impose another comparison {#states-lines-and-caps}

Return to the Gaussian of Chapter 1. Normalization produces a linear functional \(\omega\) with \(\omega(1)=1\). The unnormalized functional has the form
\[
Z(O)=Z(1)\,\omega(O).
\tag{17.8}
\]
Knowing \(\omega\) leaves the factor \(Z(1)\) undetermined. If that factor varies in a line rather than as a scalar, one must also identify the line and its connection. This distinction survives when the finite integral becomes a field theory.

Chapter 11 constructs a numerical normalized Gaussian on the original continued source graph. Its domain includes the fixed metric and density, \(0<|q|<1\), \(\kappa\ne0\), \(\hbar>0\), a smooth integrable source in the stated small inverse neighbourhood, zero normal trace, and a supplied smooth Ward filling \(T_\mu\). The even finite-cycle fields converge to a Radon Gaussian; the complete odd and mixed moments are given by the graded Wick rule. Odd variables are not assigned an ordinary probability law.

The original weighted coefficient heat construction gives another object: a based local vacuum line with a nonzero finite-part section. It uses its own reflected realization, spectral gap, smooth source bounds and finite action integrals. In a finite spectral frame, the counterterm is added to the covariant connection because the response one-form enters that connection with a minus sign. This line result determines more than the normalized state. It does not claim a convergent bare infinite determinant product or a global holonomy theorem.

A **cap** is a chosen filling of a boundary together with fields, boundary conditions and normalization that prepare a vector or functional in the specified boundary state space. If an anomaly makes the amplitude line-valued, that line belongs to the data. For a bulk observable \(O\), an exact cap comparison would take the form
\[
Z_M^{\mathrm{bulk}}(O)
=Z_M^{\partial}\bigl(r_M(O)\bigr),
\tag{17.9}
\]
where \(r_M\) is the actual observable comparison and both sides take values in an identified amplitude line. This equation is a target, not a definition of \(Z_M^{\partial}\) by the left-hand side. The state prepared by the filling must be constructed independently, and the comparison must commute with cutting and gluing.

The ordinary zero-height finite-stage Ward and full-source heat identities are defined pieces of this problem. They include all physical components on that domain and retain the complete first quantum transport \(W^0+\chi W^1\), where \(\chi=-\hbar\). They do not supply the missing uncut-to-cut comparison, the higher collision operations or the cap. Nor can the numerical state and the local line be combined outside a proved common source domain merely because both use the symbol \(\mu\).

::: figure fig-state-line-cap

## Independent realizations test what reconstruction preserves {#independent-realizations}

The geometric and arithmetic families provide decisive tests of the same distinctions. In the M2 junction of Chapter 14, the group \(\operatorname{Tor}_1\), in cohomological degree \(-1\), vanishes, but a flux cap from \(\operatorname{Tor}_2\), in cohomological degree \(-2\), survives at every positive rank and nonzero numerical \(\hbar\). Ordinary tensor composition gives the expected quotient, while the derived interface retains an additional bimodule. A reconstruction preserving only ordinary products would miss the flux operation.

For compact states, Chapter 15 constructs relative Donaldson–Thomas operators before taking their traces. Their closure gives the inverse-Igusa series with its fixed normalization. The full three-boundary operation contains information that these traces omit: an explicit nonzero cyclic Hochschild class changes the state product while leaving the fibre-marked operation and every stated multiplication trace unchanged. Thus a numerical identity can be an exact theorem without characterizing the state algebra that produces it.

Arithmetic gives a related example with a different meaning. The integer-summation and theta constructions retain the full multiplicities and produce the complete Weil trace. A positive representation of the critical part is also constructed. Its missing trace is exactly the contribution of nonreal centred zeros. The full positivity problem remains stronger than continuous duality or the existence of a cyclic vector. Integral normal operations further distinguish arithmetic tubes from their scalar points.

These results explain what a common theory must preserve: actions as well as spaces, operations as well as counts, collision extensions as well as separated restrictions, and amplitude lines as well as normalized states. They also give actual constructions from which comparisons can start. The remaining questions are not requests to replace these theorems by a single slogan. They ask for the specific additional maps that let the constructions compose. The final chapter states those questions on their original domains.
