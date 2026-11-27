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

### Native fields on every algebraic input {#ch17-native-r3-fields}

The native four-colour construction has a dg quantum vertex structure on every algebraic input through the coefficient ring
\[
R_3=\mathbb C[\hbar]/(\hbar^3).
\]
Its state complex is \(M_3=V^{KB}(\mathfrak{gl}_2)\otimes_{R_3}F_0\), with the trace-current and trace-ghost factors retained. At every numerical level \(K\), including \(0\) and \(-2\), the field \(\mathbb Y_-\), translation, vacuum and exchange give a dg quantum vertex superalgebra on all algebraic states. The locality exponent depends on the first two states and works for every final state. The opposite field \(\mathbb Y_+\) is a weakly associative chain field, joined to \(\mathbb Y_-\) by the specified field homotopy. A separate full quantum vertex structure for the opposite exchange is not part of this conclusion. [All-input field theorem](atlas.html#atlas-c-native-r3-all-input-qva).

Passing to cohomology removes the exchange correction. The exchange has an algebraically finite Laurent homotopy
\[
[d_M^{\otimes},\Lambda(u)]=S_M(u)-1.
\]
For cycle representatives of the first two inputs, one power of the separation clears its poles. The difference of the two exchanged products then becomes a coefficientwise boundary for every final cycle. Consequently \(H^\bullet(M_3,d_M)\) carries an ordinary local vertex superalgebra, with \(R_3\)-bilinear fields and the original faithful central \(R_3\)-action. Both ordered fields induce that same operation. The argument needs no Künneth identification over \(R_3\), and ordinary locality does not make the singular products zero. [Cohomology fields](atlas.html#atlas-c-native-r3-ordinary-cohomology).

There is a separate computation of the states at each fixed \(K\ne-2\). An algebraic chain frame preserves the native minimal inclusion and identifies
\[
H^\bullet(M_3)\cong
(R_3\mathbf1\oplus R_3[\omega_\hbar])
\otimes_{\mathbb C}
\left(\mathbb C[I_1,I_2,\ldots]
\otimes\Lambda(\xi^I_0,\xi^I_1,\ldots)\right),
\qquad |\omega_\hbar|=3.
\]
The trace factor has zero differential. This is an identification of state cohomology; a presentation of all its vertex products requires the corresponding field calculation. The frame is chosen at the fixed numerical level and is not asserted to continue through \(K=-2\). At that critical level, algebraic current-invariant states tensored with the ghost vacuum give a free submodule of \(H^0\), including the classical Sugawara state. Exhaustion of critical cohomology and critical physical evaluation remain further questions.

### Retained kernels and the first rooted comparison {#ch17-retained-first-root}

A scalar field forgets its ghost output. A retained kernel keeps that output until it is paired with a coefficient functional. Let \(V=M_3^0\), let \(\mathcal G\) be the completed ghost algebra, and let \(\widehat I_L\) be its closed left ideal generated by ghost modes of index at least \(L\). Put \(F_L=\mathcal G/\widehat I_L\). A retained kernel of degree \(n\) assigns to each algebraic current state \(w\in V\) a compatible Laurent series
\[
T_L(w)\in(V\otimes F_L^n)((u)).
\]
These \(R_3\)-linear families form the retained kernel space \(\mathcal E^n_{\rm ret}\) for \(n\ge0\); put \(\mathcal E^n_{\rm ret}=0\) for \(n<0\). Their Laurent lower bound may depend on \(L\) and \(w\). The combined current–ghost differential \(\mathscr D\) on these kernels squares to zero. The ghost differential itself is evaluated at a larger cutoff before projection; the individual \(F_L\) are not thereby dg quotient algebras. A retained cochain has an additional state input: in degree \(j\) it belongs to
\[
\mathcal Q^{\mathrm{ret},j}
=\prod_{p\ge0}\operatorname{Hom}_{R_3}
\bigl(M_3^p,\mathcal E^{p+j}_{\rm ret}\bigr),
\qquad
\delta\Psi=\mathscr D\Psi-(-1)^j\Psi d_M.
\]
Thus \(\Psi(x)\) is a retained kernel on the current input \(w\), with output ghost degree \(p+j\) when \(x\in M_3^p\).

At every numerical \(K\), the dressed field gives a retained cocycle \(\mathcal Y_-\). The restricted exchange homotopy gives a second cocycle \(\mathcal Y^\sharp\), with the opposite scalar field; its polarization agrees with \(\mathbb Y_+\) up to a coboundary in the kernel of the corner projection. Write \(A_{\rm cur}\) for the full smooth native current algebra and \(A_{{\rm cur},R}\) for its specified right quotients. Coefficient pairing defines continuous dg \(A_{\rm cur}\)-bimodule evaluations on the ordered rooted carrier
\[
N_{\rm rt}^{1-n}
=\varprojlim_R\operatorname*{colim}_{L\ge1}
\left(\operatorname{Hom}_{R_3}(F_L^n,A_{\rm cur})
 \otimes_{R_3,\mathrm{alg}}A_{{\rm cur},R}\right).
\]
These source coefficients are independent of \(u\). At each right quotient they have one middle ghost cutoff and finite right PBW support; neither is required to be uniform over all right quotients. The recipient is the shifted scalar Hom complex
\[
Q_3=\operatorname{Hom}_{R_3}
\bigl(M_3,\operatorname{Hom}_{R_3}(V,V((u)))\bigr)[-1],
\]
with the pointwise Laurent topology in its two algebraic inputs. Its Laurent floor need not be uniform over all inputs. Homogeneity supplies the finite ghost box and Laurent floor needed for the pairing. The two evaluations \(E^\flat,E^\sharp:N_{\rm rt}\to Q_3\) retain both endpoint actions and both translation identities, and an actual bimodule homotopy joins them. At \(K=-2\) they are new rooted maps defined by the field, not an extension of the noncritical marked evaluation. [Retained kernels and rooted evaluations](atlas.html#atlas-c-native-r3-retained-rooted-evaluations).

At a fixed \(K\ne-2\), including \(K=0\), let \(E_3\) be the prescribed pure-root evaluation, with retained cochain \(\Phi\in\mathcal Q^{\mathrm{ret},0}\), and put \(\Delta=\Phi-\mathcal Y^\sharp\). Their scalar kernels agree. Use the translation-compatible state retract with its full trace factor: if \(i\) and \(p\) are its inclusion and projection, its degree-minus-one homotopy \(k\) satisfies \(d_Mk+kd_M=1-ip\). Write \(\Delta_1\) for the restriction to inserted ghost degree one. The degree-minus-one retained cochain
\[
\kappa^{(1)}|_{M_3^2}=\Delta_1k|_{M_3^2},
\qquad
\kappa^{(1)}|_{M_3^p}=0\quad(p\ne2)
\]
has zero scalar pairing and obeys both translation laws. With \(\delta\) the retained Hom differential,
\[
\mathcal Y^{\sharp,1}=\mathcal Y^\sharp+\delta\kappa^{(1)}
\]
agrees with \(\Phi\) on inserted ghost degrees zero and one. The induced evaluation therefore agrees with \(E_3\) on the subcomplex of middle degrees at most one, and is globally homotopic to the evaluation defined by \(\mathcal Y^\sharp\) on \(N_{\rm rt}\). [The first rooted comparison](atlas.html#atlas-c-native-r3-first-root-alignment).

The contraction explains why this correction exists. Its degree-one small image consists of trace-current polynomials times one trace ghost. The two kernels agree there, while the cocycle identity makes \(\Delta_1d=0\) on degree zero. The contraction identity then gives \(\Delta_1=\Delta_1kd\). The full trace factor is essential to this argument.

Zero scalar pairing fixes the scalar normalization. The correction is not asserted to start at order \(\hbar^2\) or to preserve the strict creation column. Higher retained degrees, positive inserted marked degree, the original coefficient-valued Laurent source and the three unit-cone comparisons remain separate. In the larger source, one ghost cutoff, one Laurent floor and finite right support must govern a whole series at each right quotient. The pointwise pairing above does not supply those whole-series estimates or a physical tensorator.

### The endpoint obstruction has a specified acting algebra {#ch17-native-endpoint-obstruction}

The intrinsic field theorem can coexist with an obstruction to a physical coefficient comparison because the latter must preserve an additional action. Write \(V=M_3^0\) for the ghost-degree-zero state module and \(A_3\) for its prescribed current algebra. Let
\[
A=\operatorname{End}^{\ge0}_{R_3}(M_3)
\times_{\operatorname{End}_{R_3}(V)}A_3,
\qquad q:A\longrightarrow A_3,
\]
be the actual dg fibre product, whose endomorphisms raise ghost degree by a nonnegative integer. Inflate the marked source \(\mathcal N_3[1]\) along \(q\). The exact corner sequence, with kernel \(\mathcal K\), is a sequence of dg \(A\)-bimodules, but it has no global chain section. The kernel of \(q\) contains a closed trace creator \(c\), with \(c^2=0\), which kills the source unit class. On every closed normalized bulk lift \(G\) of the prescribed scalar class,
\[
G(\mathbf1,\mathbf1)=\mathbf1,
\qquad [cG](\mathbf1,\mathbf1)=[\xi^I_0]\ne0.
\]
Thus the source unit and its required image cannot have the same \(c\)-action.

At every fixed \(K\ne-2\), the two ordered marked evaluations have the same nonzero derived obstruction:
\[
\beta_AE_3[1]=\beta_A\overline E_3[1]\ne0
\quad\text{in}\quad
\operatorname{Hom}_{D(A^e)}
\bigl(\mathcal N_3[1],\mathcal K[1]\bigr).
\]
Restriction to the exterior algebra generated by \(c\) detects a split free cyclic \(R_3\)-submodule. An equivalent resolution of the same source module cannot remove the obstruction, nor can standard uncurved \(A_\infty\)-bimodule coherence. This excludes the specified quotient-inflated lift. A replacement action, acting algebra or recipient must come with a comparison preserving the original operations. [The exact endpoint obstruction](atlas.html#atlas-c-native-quotient-inflated-endpoint-obstruction).

The trace detector has a stronger module-theoretic form in a specified corner complex. Put \(F^1M_3=M_3^{\ge1}\). Let \(\mathcal B\) be the subcomplex of two-input Laurent cochains
\[
\operatorname{Hom}_{R_3}(M_3\otimes M_3,M_3((u)))
\]
whose value lies in \((F^1M_3)((u))\) whenever the rooted, second input lies in \(F^1M_3\). Let \(\mathcal K\subset\mathcal B\) consist of cochains whose every output lies in \((F^1M_3)((u))\). The corner map
\[
\pi:\mathcal B\longrightarrow
\mathcal C=\operatorname{Hom}_{R_3}(M_3\otimes V,V((u)))
\]
restricts the rooted input to its ghost-free part \(V=M_3^0\) and projects the output to ghost degree zero; its kernel is \(\mathcal K\).

For a closed \(G\in\mathcal B^0\) with \([\pi G]=[W_\pm]\), multiplication of its output by exterior trace monomials gives a split copy of \(\Lambda_{R_3}(\xi^I_0,\xi^I_1,\ldots)\) in \(H^\bullet(\mathcal B)\); its positive-degree part splits into \(H^\bullet(\mathcal K)\). This is a splitting of graded \(R_3\)-modules, not a presentation of a product on Hom cohomology. Suppose a dg acting algebra preserves this corner exact sequence and contains a closed degree-one element acting by output multiplication by a trace ghost. If a dg module map from \(S\) to \(\mathcal C\) sends a closed degree-zero element to the normalized scalar class \([W_\pm]\) and \(H^1(S)=0\), it has no lift to \(\mathcal B\) in the derived module category or as a standard uncurved \(A_\infty\)-module map. The trace creator kills the source class and cannot kill its required image. The acting-algebra and diagram hypotheses are essential; this obstruction does not exclude the retained-kernel pairing or a relative cone with different cohomology. [Trace classes and the source-degree obstruction](atlas.html#atlas-c-native-r3-trace-classes-source-obstruction).

The noncritical marked evaluations themselves remain positive constructions. Their endpoint-bilinear homotopy restores the reversed scalar field, both Ward laws, the prescribed minimal pairings and the proper unit-cone diagrams. A separate scalar correction also aligns the two scalar homotopies while preserving translation. Scalar connecting classes can therefore vanish while the derived bimodule obstruction survives. Throughout, the coefficient source retains one Laurent floor, one ghost cutoff and finite right PBW support across each whole series at a fixed right quotient and algebraic inserted input. The independent physical right adjoint, its counit, both products and tensorator still require maps on that declared domain.

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

::: figure fig-programme-context-reconstruction
