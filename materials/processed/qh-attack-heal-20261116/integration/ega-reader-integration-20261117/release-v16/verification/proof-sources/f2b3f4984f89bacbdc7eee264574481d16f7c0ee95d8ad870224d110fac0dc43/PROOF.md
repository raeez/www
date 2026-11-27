> **A ruling on this record names changes it needs: frontier/attack-heal/shape-wave-4/F7/RULINGS.md section 1.1** (Fable session w4-F7, 14 Nov 2026; accepted as the mathematical coordinator's ruling, frontier/attack-heal/shape-wave-4/CONSOLIDATED.md section F7). Notice added 14 Nov 2026 14:04 WIB by a lane of the Opus coordinator. The text below this notice is unchanged.
>
> - RULINGS.md 1.1: "The lemma is true and sections 6 to 9 with section 11 prove it. I found no false sentence in sections 6 to 12."
> - Changes asked of the owner (RULINGS.md 1.1, "Minimal changes to the record (for its owner; none made by me)"): (1) "In section 0 and in Lemma 8.1, say which half of Rozenblyum's Theorem 3.5.1 is used where, and that it is an arXiv preprint; or replace its use in section 9 by S-1 and S-2." (2) "After (8.2), add that the isomorphism is an isomorphism of actions and give the reason (S-2 or the family structure); the present sentence "agrees with the module-family diagonal comparison" asserts it." (3) "In section 9, replace the paragraph on normal forms of finite maps by the uniqueness statement of S-3, or keep it and add the relabelling case (3), which it does not treat." (4) "OPEN.md may then say: Theorem 9.1 read independently (Fable family) with three supplements; cross-family check owed; the physical line-category application open."
> - The supplements S-1, S-2, S-3 of RULINGS.md 1.1 are unchecked: "A cross-family check is still owed; this reading is by the family of the coordinator."

# G10-03: what a realized categorical vacuum reconstructs

## 0. Statements and scope

The base field is C and X is a smooth separated algebraic curve. All coefficient sheaves and state spaces are algebraic. The classical BD coefficient convention is used: B_I is an ordinary quasi-coherent O_(X^I)-module, and the chiral algebra is the right D-module omega_X tensor B_1. No derived Chevalley shift, Hilbert completion or completed state carrier is suppressed.

Throughout, the ordinary coefficient-family category means the classical BD/Rozenblyum category: coefficients have the relative differential-module structure in unmarked variables, coherent normal collision and factorization maps, and no nonzero local sections supported on diagonals involving an unmarked variable. No corresponding torsion exclusion or flatness hypothesis is imposed on the minimal coefficient in the original marked parameters. In particular arbitrary quasi-coherent minimal coefficients are allowed. Right coefficients in the added variables are converted to left coefficients by tensoring with the inverse relative canonical line, without a cohomological shift. Arbitrary parameter base change means ordinary base change between classical complex schemes; its categorical meaning on affine charts is the relative tensor product proved in §7.

**Theorem R (proved by the owner; new unconditional step in §§6–9).** An admissible vacuum-marked categorical system with a geometric realization, precisely as in §1 with its normalized empty algebra unit, canonically determines a unital chiral algebra Rec(C,F). This construction is invariant under equivalences preserving the geometric carrier and its coherent unit/collision comparisons. Only the disjoint comparison on the vacuum is required to be invertible; no assertion that fusion of the whole module categories is an equivalence is needed.

For every classical unital BD chiral algebra A, its complete ordinary coefficient-family system is admissible and Rec canonically returns A, including its collision extensions. Here a category over X^I has the chart/sheaf meaning made explicit in §8: an ordinary QCoh-linear sheaf of presentable categories, with genuine categorical scalar extension on affine parameter charts and arbitrary parameter schemes handled by descent. Theorem 9.1 proves the full-category pullbacks, collision equivalences, insertions, fusion and evaluation compatibilities; its vacuum is the regular family Fact(A). No additional global-sections tensor or 1-affineness assertion is used.

On A1, translation equivariance gives the corresponding vertex algebra. If the input also retains a conformal vector and the compatible conformal grading, the reconstructed isomorphism preserves that VOA structure. A bare category does not canonically choose a conformal marking.

**Theorem N (proved below, with the standard lattice/VOA classifications cited in root PRIOR.md).** The braided shadow alone does not reconstruct a VOA and its fibres are not its fixed-central-charge genera. V_E8 and C have the same ribbon category and different charge; tensoring with V_E8 yields infinitely many charges with the same shadow. Even retaining c=16 and the torus character does not separate V_(E8+E8) and V_(D16+). The state-valued current collision does separate them. A pointwise marked carrier or scalar two-point pairing cannot be substituted for the collision extensions consumed by Theorem R.

**Status and provenance.** The realized-vacuum mechanism is already Raskin §§6.2–6.3, the coefficient-to-chiral equivalence is BD Theorem 3.4.9, and the classical many-marked action/family equivalence is Rozenblyum Theorem 3.5.1. Sections 6–9 supply the ordinary kernel base-change proof, the internal-module and relative-tensor universal property, descent and full categorical compatibilities that the earlier proof lacked. CHECK-1113-1102 and CHECK-1113-1305 correctly rejected the earlier unconditional proof and adopted its stated conditional components; they predate and do not certify §§6–10. The current unconditional result is an owner proof, not a new independent adoption or a priority claim. Finite controls verify only their stated finite identities. No full-faithfulness claim for arbitrary functors between module categories, and no physical Einstein comparison, follows.

For any proposed physical line category, the full categorical input of §1 must be supplied, and its actual vacuum carrier must extend across every collision with the base-change, unit and disjoint comparison maps specified there. The theorem does not infer these from its ribbon fibre.

## 1. The exact category-valued input and the extracted coefficient sheaves

We use the classical finite-configuration chart description, avoiding any implicit derived-to-abelian passage. For every finite set I, including the empty set, give a QCoh-linear category C_I with specified coherent pullbacks over X^I and arbitrary parameter base changes T->X^I. For a finite-set map pi:I->J, let Delta_pi:X^J->X^I repeat the coordinates according to pi. Supply coherent functors

    beta_pi: Delta_pi^* C_I -> C_J.

For surjective pi these are equivalences. Injections are the unit-insertion functors. Require C_empty=Vect. For a partition pi:J->I, on U_pi where points in different fibres of pi are distinct, give coherent external fusion functors from the external product of the C_(J_i) to C_J. They obey the symmetric, iterated-partition and base-change/unit compatibilities of a unital weak factorization system. No global invertibility of these external fusion functors is required.

The vacuum v_I is beta_(empty->I)(C), not an arbitrarily chosen simple object at each point. Composition supplies canonical identifications beta_pi(v_I)=v_J. The unit and external-fusion coherence supplies its coherent disjoint multiplication. This is the chart form of the unit construction in Raskin §§4.24 and 6.3; in the weak case we explicitly impose the comparisons on these particular objects below.

The geometric realization consists of O-linear functors

    F_I: C_I -> QCoh(X^I),

and coherent comparison maps for the beta_pi and external fusion functors. On the vacuum these give isomorphisms for surjective pi and disjoint external fusion. For injections they give maps, not required to be isomorphisms. Their compositions, relabellings and mixed base-change diagrams commute. The empty-fusion and unit comparisons give B_empty:=F_empty(v_empty) a unital commutative algebra structure. Require B_empty=C as a unital commutative algebra, including its algebra unit; this is the normalized empty comparison, not merely an identification of underlying vector spaces. Require B_I:=F_I(v_I) to have no nonzero local sections supported on the diagonal divisor in X^I. These are explicit admissibility conditions on a specified functor and object, not a reconstruction conclusion. O-flatness is one sufficient condition for the last requirement but is not imposed unnecessarily.

Apply F to the actual vacuum objects and their maps. The resulting maps are

    nu_pi: Delta_pi^* B_I -> B_J,
    c_pi: (external_product_i B_(J_i))|_(U_pi) -> B_J|_(U_pi).

The first is invertible for surjections and the second is invertible on U_pi. The distinguished section 1 is the image under nu_(empty->1) of the algebra unit of B_empty; under the normalized algebra identification this unit is the scalar 1. For all finite maps, nu_(sigma pi)=nu_sigma Delta_sigma^*(nu_pi), because this is the image of the categorical composition comparison. For iterated partitions, the two composites of the c maps agree by the external-fusion associativity diagram. The mixed nu/c diagram is the image of the categorical mixed comparison. Symmetry is likewise inherited. Together with the absence of diagonal-supported sections and the normalized empty algebra B_empty=C, these verify each of BD §3.4.5(a)--(f), and hence produce a factorization algebra B. This proves all-arity compatibility; it is not extrapolated from a two-point calculation.

The normalization is necessary. For nonzero lambda, transport the trivial coefficient system B_I=O_(X^I) by e_I=lambda^(|I|-1). For a finite-set map q:S->T and a partition pi:J->I, the transported maps are

    nu_q = lambda^(|T|-|S|),    c_pi = lambda^(|I|-1).

All finite-map, partition and mixed diagrams remain coherent, and there is no diagonal torsion. Empty multiplication has scale lambda, its algebra unit is lambda^(-1), and nu_(empty->1) sends the unnormalized scalar 1 to lambda. Its image on the algebra unit is instead 1. The binary residue scales by lambda times lambda^(-1)=1, so at lambda=2 the unnormalized section 2 fails the chiral unit axiom while the normalized section 1 satisfies it. This is a countermodel only to the unnormalized wording. The [repair script](scripts/check_repair_1113_1102.py) records 10,148 exact empty-unit assertions, including 1,678 composable finite-map pairs on sets of sizes 0 through 3; its [JSON results](scripts/check_repair_1113_1102.json) and [stdout](scripts/check_repair_1113_1102.stdout.txt) reproduce these scales.

There is no requirement F_1(v_1)=O_X. The map O_X->F_1(v_1) is only the realized vacuum vector. This distinction is exactly Raskin Remark 6.3.1 and is essential for any nontrivial VOA, whose vacuum module has many states. Nor do we require F to be faithful on every morphism of every C_I: the coefficient data needed for the reconstruction sit on the realized vacuum diagram.

The construction is functorial. An equivalence of the categorical input with a compatible natural isomorphism of realizations carries v_I to v'_I and induces an isomorphism B_I->B'_I commuting with every nu and c. It therefore induces a factorization-algebra isomorphism, independently of chart presentations. Conversely no assertion that every coefficient morphism lifts to a categorical functor is being made.

## 2. Connection, collision operation and the all-arity identities

BD Proposition 3.4.7 gives B its unique canonical connection with horizontal unit. This connection can also be read directly from the input: in a local coordinate t, the two insertions of the vacuum identify B_1 along the formal neighbourhood of the diagonal, and

    1 external_tensor b - b external_tensor 1
       = (t_2-t_1)(partial_t b external_tensor 1)
                                          modulo (t_2-t_1)^2 B_2.

The all-arity composition identities of §1 make these infinitesimal identifications transitive, hence give a flat connection. Thus translation is not recovered by choosing an unrelated linear operator. Set A=omega_X tensor B_1 with its resulting right D-module structure.

Write j:X^2 minus Delta -> X^2. Let mu_omega be the canonical residue operation

    j_*j^*(omega_X external_tensor omega_X) -> Delta_*omega_X.

The binary chiral operation on A is the following explicitly determined composite:

    j_*j^*(A external_tensor A)
       -> [j_*j^*(omega_X external_tensor omega_X)] tensor_(O_X^2) B_2
       -> (Delta_*omega_X) tensor_(O_X^2) B_2
       -> Delta_*(omega_X tensor B_1).                          (2.1)

The first arrow uses the disjoint coefficient comparison c_pi from §1. The middle arrow is mu_omega tensor id. The last arrow uses the diagonal map nu and the D-module projection formula in BD (3.4.8.1). In particular the extension B_2 across Delta, and not merely its restriction to j, enters the middle and last arrows. Formula (2.1) is BD (3.4.8.3); it uses no supplied OPE on the desired output.

Here is an explicit check of the all-arity point that a two-point test cannot settle. For any finite J and geometric chiral operation phi on omega_X, replace B_2 by B_J in (2.1), obtaining Phi_B(phi). For a substitution of operations indexed by a partition of J, factorization first identifies the separated tensor with B_J. Performing the inner operations tensors their residues with the same B_J; applying the outer operation then composes the geometric residue maps. The alternative, composing geometric operations first and then tensoring with B_J, gives the same map. The two coefficient identifications coincide by the mixed nu/c and iterated-partition identities proved in §1. Hence

    Phi_B(phi composed with {psi_i})
       = Phi_B(phi) composed with {Phi_B(psi_i)}.

It is therefore a morphism of operads. The canonical Lie operad inside the chiral operations on omega_X transfers to A. Antisymmetry follows from relabelling two points, and the ternary Jacobi sum is the image of the zero Jacobi sum on omega_X. The same argument handles every substitution, not just arity three. The injection maps involving the empty set supply the chiral unit identity. This proves that (2.1) is a unital chiral algebra, with all required identities.

A second verification is BD Theorem 3.4.9: §1 constructed an actual object of FA(X), and (2.1) is its prescribed image in CA(X). That equivalence also gives uniqueness of its factorization lift. The more general ordered systems of S `hpc:thm:full-faithfulness` are not automatically objects of this symmetric BD category with its finite-set descent; this theorem makes no such substitution.

On A1 with translations, evaluate at a point and use the formal coordinate difference z. The chiral operation determines the maps a_(n)b by its pairing with all Laurent test powers z^n, giving Y(a,z)b=sum_n (a_(n)b)z^(-n-1). The chiral axioms imply the vertex axioms by the standard chiral/vertex correspondence. A conformal state omega and its grading, if retained by the input, are transported by this construction. Equality of central charge is then a consequence of preserving its collision, not a property of the abstract unit alone.

## 3. Historical conditional round trip and the former admissibility gap

**Status correction after §§6–9.** The following section preserves the check-stage argument and the exact open lemma identified by both independent checks. Theorem 9.1 now proves that lemma at the ordinary chart/sheaf scope specified in §§1 and 8. Its statements that the unconditional clause “remains open” are historical and are superseded by this owner proof; the conditional calculation and the ordinary/derived δ-module distinction remain valid. The old checks remain accurate records of their checked inputs.

**Precise coefficient-family definition used in the continuation.** Fix a finite marked set I and a classical parameter scheme T→X^I. For a finite set R of additional, unmarked labels, a coefficient-family object has a quasi-coherent left coefficient M_R on X^R×T, with differential operators in the X^R directions and ordinary O_T-linearity. Its minimal coefficient M_empty is an arbitrary object of QCoh(T). The family has coherent ordinary normal collision identifications for finite-set surjections fixing the original marked labels, permutation maps, normalized unit-insertion maps, and the factorization identifications

    Fact(A)_R external_tensor M_S → M_(R union S)

on the specified separated loci, where these are isomorphisms. These satisfy the classical module compatibility diagrams. Each coefficient has no nonzero local section supported on the union of diagonals involving an unmarked label. This condition does not exclude sections supported on a collision locus among the original marked parameters.

This is the ordinary left-coefficient presentation of the classical factorization-module category. In the right-coefficient convention its R-component is ω_(X^R) tensor M_R. Rozenblyum's Definition 3.3.1 and Theorem 3.5.1 identify this category with the marked chiral-action category; §2 specifies the differential operators in unmarked variables and ordinary linearity in marked variables. The category-valued system retains these entire families, and coefficient evaluation is F_T(M)=M_empty. [Rozenblyum, *Modules Over a Chiral Algebra*, §§2, 3.3–3.5](https://arxiv.org/html/1010.1998v1).

**Historical check-stage description and argument.**

Let A be a classical unital BD chiral algebra, and let B=Fact(A) be the factorization algebra constructed by the inverse in BD §§3.4.10--3.4.12. We describe the proposed ordinary coefficient-family categories of its unital factorization module system. Their full categorical admissibility is the open step; the regular-vacuum calculation below is conditional on the stipulated categorical structure.

For a finite set of marked points I, a factorization module family has coefficient sheaves on configurations S containing those marked points. It has compatible pullbacks, collision maps, unit-insertion maps, and a factorization identification

    B_R external_tensor M_S -> M_(R union S)

when R is disjoint from S and from the marked points. These maps satisfy the module associativity, symmetry for the unmarked points, and unit conditions. The proposed construction asks for this description after every base change T->X^I. Its intended C_I is the category of these unital algebraic families and their compatible morphisms. Its coefficient-evaluation functor F_I restricts a family to the minimal configuration consisting just of the marked points, allowing their repetitions through the finite-set diagonal maps. The intended realization retains this entire family functor, not merely its fibre at a fixed point, and uses ordinary classical coefficients. This description does not yet construct or verify the coherent categorical pullback and fusion functors on all these categories.

**Open lemma (classical categorical admissibility).** For every classical unital BD chiral algebra A, the ordinary coefficient-family categories just specified form a QCoh-linear unital weak factorization system over all charts X^I and arbitrary parameter base changes T->X^I, with coherent equivalences

    Delta_pi^* C_I ≃ C_J

for every surjective finite-set map pi:I->J, coherent unit insertions and external fusion, and coefficient-evaluation functors compatible with those pullbacks, units and fusion maps. These equivalences and compatibilities are required on the full categories, not only on the regular object.

Assume this lemma, or more generally an admissible system of §1 with the following regular-family realization. For I empty the module condition gives, for every configuration R,

    M_R = B_R external_tensor M_empty.

Indeed take S empty in the disjoint module identification; the unit axiom makes all these identifications compatible. Conversely the displayed free family is a unital factorization module for every vector space M_empty. Evaluation at the empty configuration is therefore an equivalence C_empty=Vect, with inverse W -> B external_tensor W. This proves that the categorical empty unit is the regular factorization module B, without choosing its components afterward.

The unit-insertion functor empty->I restricts this no-defect module to configurations containing the marked points. Its coefficient at S is still B_S. Consequently its realized vacuum is

    F_I(v_I)=B_I                                                       (3.1)

canonically, including the diagonal extensions and the normalized empty algebra unit. Under the assumed categorical comparisons, when marked points collide, reindexing these very same families gives precisely nu_pi of B. When they split into disjoint groups, the regular-module comparison is c_pi of B, hence is invertible. This last assertion follows directly from B's factorization property on its regular module; it does not use an equivalence between external products of arbitrary module categories. This computation identifies the comparisons on the regular object; it does not establish the categorical equivalences in the open lemma.

Under the stated categorical assumption, all vacuum-level hypotheses of §1 hold, and extraction returns B with its original finite-set maps. By BD Theorem 3.4.9, the residue construction returns A. More concretely, BD §3.5.11 identifies the original OPE as the gluing datum for B_2: restrict a separated section a external_tensor b to the punctured formal neighbourhood of the diagonal. That is exactly the operation recovered from (2.1). This verifies the conditional round trip, retaining the entire extension B_2 across the diagonal and every Laurent coefficient.

This argument does not define Rec(C,F) to be A. Rec was defined in §§1--2 on independent admissible categorical data, by evaluation on its unit and a geometric residue. Equation (3.1) computes its vacuum realization provided the proposed classical module system has the stipulated categorical structure. As for ordinary reconstruction of a ring from its regular module and forgetful functor, the forward construction naturally uses the original algebra; the inverse is a separate formula using only the retained category data.

Raskin Proposition 8.14.1 constructs the DG/de Rham factorization-module system. It does not establish passage to these ordinary coefficient-family categories and their ordinary parameter pullbacks. BD Proposition 3.4.19 and its O-linear variant on p.190 give the classical single-defect module comparison, and the following multi-input formulas describe chiral operations. They do not by themselves supply the full multi-marked categorical base-change and fusion lemma above. The missing point is that entire classical categorical construction, not merely the fact that Raskin's formulation is derived.

The distinction between ordinary and derived pullbacks occurs on an allowed input. Take the square-zero chiral extension A=omega_X direct_sum delta_0 on X=A1; its left coefficient is O_X direct_sum delta_0^l. Write

    delta_0^l=C[s],    t=-d/ds,    partial_t=s.

These actions satisfy [partial_t,t]=1. The map t is surjective, since t(-s^(n+1)/(n+1))=s^n for every n>=0, and its kernel consists of constants. The ordinary and derived parameter pullbacks therefore have

    C tensor_(C[t]) delta_0^l = coker(t)=0,
    Tor_1^(C[t])(C,delta_0^l) = ker(t)=C.

They cannot be silently identified. This is not a counterexample to BD equivalence or to the open admissibility lemma. The [repair script](scripts/check_repair_1113_1102.py) checks the Weyl relation and polynomial preimages with unrestricted intermediate degree, on monomials of degrees 0 through 64 and 3,125 rational-coefficient polynomials. Its 12,762 nonflat-pullback assertions, together with the 10,148 empty-unit assertions in §1, give 22,910 passing exact controls in the [recorded results](scripts/check_repair_1113_1102.json). The general surjectivity and kernel arguments are the polynomial identities above; these finite controls do not certify categorical admissibility.

Thus the original full Theorem R remains open. The recorded unconditional proof of R3 is rejected, while its conditional regular-vacuum calculation is retained; the missing lemma has not been disproved. For a different proposed meaning of physical lines, or a restriction to grading-restricted modules at one point, the full §1 input, (3.1) and its collision comparisons must also be checked afresh. Neither a braided fibre nor the word 'vacuum' supplies those data.

## 4. What pointwise, braided and monadic data fail to establish

For every strongly rational V, tensoring with the holomorphic lattice VOA V_E8 preserves its ribbon representation category and increases its actual central charge by eight. Hence the fibre of V->Rep(V) contains objects with different charges. The fibre of V->(Rep(V),c(V)) is its bulk genus by definition, but this definition provides no reconstruction. The rank-16 lattice VOAs V_(E8+E8) and V_(D16+) lie in the same such fibre. Their weight-one Lie algebras are e8 direct_sum e8 and d16. One has two simple ideals and the other one, so they are not isomorphic, even after scalar extension. Their common character and equal weight-one dimension 496 are reproduced in the root healer checks. Over C their nondegenerate symmetric weight-one pairings are isometric; the state-valued simple-pole bracket retains information that those scalar pairings discard.

The pointed carrier alone also does not specify collision multiplication, even among elementary vertex algebras. On the two-dimensional space with basis 1,x and translation zero, the commutative associative algebras with x^2=0 and x^2=1 define constant vertex algebras Y(a,z)b=ab. They have the same vector space, unit and translation. In the first, x is a nonzero nilpotent; in the second, the algebra is C direct_sum C and has no nonzero nilpotents. Thus their collision products differ. This example concerns the insufficiency of pointwise coefficient data; their complete module categories with forgetful functors need not be equivalent, and it is not a strongly rational counterexample.

The monadic route gives a useful precise comparison. For a unital associative algebra R, the pair (R-Mod,U) with its underlying-vector-space functor determines R: its free/forgetful monad has T(C)=R and monad multiplication is the original multiplication. Equivalently, every natural endomorphism of U is action by a unique r in R. To prove the latter, apply naturality to the maps R->M, a->a m; a natural transformation is determined by its value on 1 in the regular module. Composition agrees with multiplication of the acting elements. This argument explains what an actual carrier functor can retain. It does not identify the singular-coordinate action or the diagonal extensions of a chiral system from a monad on a single fibre.

There is also a specific invalid shortcut: take the quotient of an operator algebra by the annihilator of a vacuum and use representative multiplication as the vertex product. In the Weyl representation on C[x], partial_x kills 1, while partial_x*x sends 1 to 1. The annihilator of 1 is a left ideal but not a right ideal, so the quotient has no well-defined multiplication by representatives. This is why S `itg:thm:states` is a statement about a left module over a mode algebra already constructed from fields. The geometric unit/residue construction in §§1--3 avoids that false inference.

These are distinct tests of the weaker routes: the holomorphic and rank-16 examples obstruct the braided route; the constant vertex algebras obstruct reconstruction from a pointed carrier alone; and the Weyl example obstructs the vacuum-quotient multiplication. None contradicts reconstruction from the fully specified geometric data of Theorem R.

## 5. Stress, currents, and the marked lattice check

For r free bosons choose Heisenberg fields a_i with a_i(z)a_j(w) having singular part delta_ij/(z-w)^2, and T=(1/2)sum_i :a_i a_i:. The double contractions in T(z)T(w) give two matchings for each i, hence coefficient r*2/4=r/2 in the fourth pole. The single contractions give the normal product of a_i(z)a_i(w), whose expansion gives 2T/(z-w)^2 and partial T/(z-w). Thus c=r. Independently, on the polynomial Fock space, L_-2 applied to the vacuum is (1/2)sum_i x_i^2 and the relevant part of L_2 is (1/2)sum_i partial_(x_i)^2; their pairing is r/2. This is the same coefficient obtained from [L_2,L_-2] on the vacuum.

For V_E8 the fourth pole is 4 and for C it is 0. Therefore an equivalence preserving the realized stress insertion and its collision is impossible. For the rank-16 pair the fourth poles agree at 8, but the current OPE

    J^a(z)J^b(w) ~ (a,b)/(z-w)^2 + J^[a,b](w)/(z-w)

recovers the distinct weight-one Lie algebras of §4. The full state-valued two-input operation separates them; merely contracting it with the vacuum to retain a scalar two-point function does not. These tests check exactly which part of (2.1) is being retained.

There is an independent reconstruction proof in the marked lattice class of positive-definite even integral lattices. Retain the free charge lattice L, its Heisenberg space, the algebraic carrier direct_sum_(alpha in L) F_alpha, nonzero charge products, translations and the standard conformal vector. Here F_alpha are the actual standard Heisenberg Fock modules, including h(0)e^alpha=B(h,alpha)e^alpha and h(n)e^alpha=0 for n>0, not merely named vector-space summands. For chosen charge vectors e^alpha, the leading collision is

    Y(e^alpha,z)e^beta
       = epsilon(alpha,beta) z^B(alpha,beta)
         exp(sum_(n>0) alpha(-n) z^n/n) e^(alpha+beta).            (5.1)

The leading integral orders recover B, not merely its parity or its value modulo Z. The nonzero leading coefficients satisfy the normalized group cocycle identity by three-input associativity and epsilon(alpha,beta)/epsilon(beta,alpha)=(-1)^B(alpha,beta) by exchange. Any two choices with these properties have a symmetric cocycle ratio. Its central extension of L by C* is abelian; lifting a basis of the free group L gives a splitting, hence the ratio is a coboundary. Rescaling the charge vectors removes it. The Heisenberg commutation relations determine the rest of (5.1) and the corresponding annihilation exponentials on general Fock vectors. This proves uniqueness of the marked lattice VOA up to a marked isomorphism. The isomorphism itself need not be unique: character rescalings remain.

All-arity coherence has a separate direct check here. Repeatedly commute the creation and annihilation exponentials using their central Heisenberg commutator. For n charges the resulting scalar factor is the product over pairs of (z_i-z_j)^B(alpha_i,alpha_j), multiplied by the iterated cocycle coefficient. The cocycle identity makes that coefficient independent of parenthesization; the displayed commutator rule gives the exchange signs. Induction on n therefore checks every iterated collision in this lattice class. This is the standard lattice construction already recorded as G10-N03, not a theorem that arbitrary ordered systems follow from two-point data.

The independently run [script](scripts/check_reconstruction.py) tests the double-contraction/Fock coefficient by two exact calculations, the Weyl left-ideal witness, the constant-vertex-algebra distinction, and a nontrivial A2 cocycle on a bounded charge cube. Its rerun passes 48,776 exact assertions, as recorded in the [JSON results](scripts/check_reconstruction.json) and [stdout](scripts/check_reconstruction.stdout.txt). The infinite splitting and coherence arguments are proofs above. Half-loop phases alone would miss, for example, the change of a rank-one Gram matrix from (2) to (4); both have the same parity but different collision orders.

## 6. The ordinary kernel calculation over an arbitrary parameter ring

Fix a classical unital chiral algebra A on a smooth separated complex algebraic curve X. Mark finitely many sections x_i of X_T for T=Spec B; repetitions and nilpotents in B are allowed. Let D=sum_i Γ_(x_i), let j:X_T\D→X_T, and write ω for the relative canonical line. Only the X direction carries differential operators. For a B-module M put

    E_D(M)=j_*j^*(A boxtimes M),
    G_D(M)=(ω(*D)/ω) tensor_B M.

These are quasi-coherent sheaves on X_T. For an affine open V containing the marked sections, write E_D^V(M)=Γ(V_T,E_D(M)) and G_D^V(M)=Γ(V_T,G_D(M)). Every splitting used below is a splitting of these B-modules of sections. No splitting as sheaves on X_T is asserted. For D empty take G_D=0. A chiral action is the usual D_(X_T/T)-linear map μ_M:E_D(M)→G_D(M), satisfying the chiral Lie-action identity and the normalized unit identity

    μ_M (u boxtimes id_M)=q_M,                         (6.1)

where u:ω→A is the algebra unit and q_M:ω(*D) boxtimes M→G_D(M) is the principal-parts quotient. This is the ordinary marked-action convention, with O-linear marked parameters, of [Rozenblyum, arXiv:1010.1998](https://arxiv.org/html/1010.1998v1), §2 and Definition 3.4.1. No de Rham quotient of principal parts is taken.

**Lemma 6.1.** Locally on T choose such an affine V. The quotient q_M^V:Γ(V_T,ω(*D) boxtimes M)→G_D^V(M) has a B-linear section natural in M. Consequently μ_M^V:E_D^V(M)→G_D^V(M) has a B-linear section. For every B-algebra B′, the canonical quasi-coherent sheaf map

    B′ tensor_B ker(μ_M) → ker(B′ tensor_B μ_M)         (6.2)

is an isomorphism. It is compatible with the relative differential-module structures and successive base changes. No flatness of M, B′ or the underlying O_X-module of A is required.

**Proof.** First take X=A1, with coordinate z, and x_i=t_i in B. If d=|I|>0 and P(z)=product_i(z-t_i), monic division gives

    B[z,P^(-1)]/B[z]
       = direct_sum_(n≥1,0≤a<d) B·[z^a/P^n].          (6.3)

Indeed, at denominator P^N every numerator has a unique remainder of degree less than dN; repeated division of that remainder by P gives the displayed coefficients. Multiplication by the monic P is injective over every B, so this computation also proves independence in the localization. Sending each displayed basis element to its proper rational representative gives a B-linear section on global sections, natural under every B→B′. Tensoring these B-modules with dz and M gives s_M^V. This is not a sheaf-theoretic splitting on A1_T. This argument does not separate the roots or invert any difference t_i-t_j.

Here is the coordinate-free local argument, which also gives a second verification of the needed splitting. After shrinking T around any of its points, all the finitely many marked sections land in a common affine open V of X. Such an open exists because a finite set of points of a smooth separated curve is contained in an affine open. On V_T the divisor D is a relative effective Cartier divisor, finite and flat of degree d over T. One can verify this directly by successively adding its graphs: the quotient arising when one graph is added is an invertible module on that copy of T. Thus the modules

    Q_n=Γ(V_T,ω(nD)/ω)

are finite projective B-modules of rank nd, and Q_(n+1)/Q_n is finite projective of rank d. Each inclusion Q_n→Q_(n+1) therefore splits over B. It follows that Q=colim_n Q_n is a direct sum of finite projective B-modules, hence projective. The surjection Γ(V_T,ω(*D))→Q consequently has a B-linear section. The same successive-graph filtration proves that Q_n and Q commute with every base change, including nonflat ones. This argument uses the actual graph divisor; it introduces no extra inverse-image points by choosing an étale coordinate.

Compose s_M^V with the map on global sections induced by the localized unit. This gives r_M^V:G_D^V(M)→E_D^V(M), with μ_M^V r_M^V=id by (6.1). Thus, as B-modules,

    E_D^V(M)=ker(μ_M^V) direct_sum r_M^V(G_D^V(M)).    (6.4)

Tensoring this split sequence with B′ proves the kernel comparison on the affine scheme V_(T′). Independently, the B-linear idempotent id-r_M^V μ_M^V has image ker(μ_M^V), and its scalar extension has image ker(μ_M^V tensor_B B′). These are two direct verifications of the same ordinary comparison.

Global sections on V_T identify quasi-coherent sheaves with modules over Γ(V,O_V) tensor_C B, and tensoring those modules with B′ is precisely parameter pullback. Hence the just-proved comparison is the restriction of the canonical sheaf map (6.2), which is linear for O_(V_(T′)) and for all surviving relative differential operators: it was induced by the differential-linear kernel inclusion. The auxiliary B-linear section is not O_V-linear or differential-linear and is not used to define that map. Different affine charts and choices of sections therefore prove invertibility of the same canonical map; the maps agree on overlaps and glue. Away from the marked divisor the target G_D is zero, so the comparison is immediate there. This proves the global assertion and compatibility with successive base changes. For D empty there is no principal-parts term. ∎

The same proof applies with any already introduced unmarked coordinates retained as additional parameters. Therefore every successive coefficient kernel in the marked-module construction commutes with arbitrary changes of the original parameter base. The natural comparison retains all differential operators in coordinates that remain unmarked; temporarily viewing a coordinate as a parameter does not alter the canonical kernel map.

**Boundary checks.** For A=ω_X the unit forces μ_M=q_M, so its kernel is ω_X boxtimes M. The marked-action category is exactly QCoh(T), and promotion merely pulls M to one additional coordinate. Conversely an arbitrary unsplit kernel need not commute with scalar extension: multiplication by u on C[u] has zero kernel, but after u=0 its kernel is C. The positive statement above uses the chiral unit identity, not a general claim that ordinary kernels commute with nonflat pullback. The δ-module calculation in §3 remains unchanged: it concerns a different pullback and is not contradicted by (6.2).

## 7. Scalar extension of the whole ordinary action category

Let C_B be the category of B-modules M equipped with the action of §6; morphisms commute with that action. Initially work on an affine parameter chart on which the marked graphs lie in a common affine V⊂X. The action and its identities are determined on V because their targets are supported on the marked graphs. Let U_B:C_B→B-Mod be the underlying-module functor. Tensor products in this section are ordinary algebraic tensors. For presentable B-linear categories, the relative category tensor product is characterized by cocontinuous functors out of it, equivalently by separately cocontinuous B-balanced functors out of its two factors.

**Lemma 7.1.** C_B is an ordinary locally presentable B-linear abelian category. U_B is faithful, exact, and creates all small colimits. For every B-module N, the B-linear action N tensor_B M on C_B has the usual underlying B-module tensor product. Every coefficient of the associated marked factorization family preserves colimits and commutes with arbitrary parameter scalar extension.

**Proof.** On the affine ambient chart, both E_D^V(-) and G_D^V(-) are exact and preserve colimits as functors on B-modules. For E this follows by tensoring the complex vector space Γ(V,A) with M and then localizing on V_T. For G it follows from G_D^V(M)=Q tensor_B M and the projectivity of Q established in §6. The two-input principal-parts targets occurring in the action identity have the same exactness: their modules are successive tensors of these flat principal-parts modules with M. Localization and diagonal direct image used in the identity are exact on these affine module expressions.

For a morphism of actions, the action on the underlying kernel factors uniquely through the principal-parts module of that kernel; the action on its cokernel descends uniquely to its principal-parts quotient. The unit and Lie-action equations are inherited, using the injectivity of the target comparison for kernels and its surjectivity for cokernels. Thus kernels, cokernels, images and coimages are created by U_B, and C_B is abelian. For any small diagram of actions, form its colimit in B-Mod and use the colimit comparisons for E and G to define the action. The same finite equations still hold. This constructs the colimit and proves its universal property.

For completeness, presentability does not require an assumed free unrestricted vertex module. Choose an infinite cardinal λ bounding the sets of coefficients of B, Γ(V,O_V), Γ(V,A), the differential operators and a free module having Q as a direct summand, including the coefficients of the chosen splitting projector B^(S)→Q→B^(S). Choose an uncountable regular cardinal κ>λ. Starting with fewer than κ elements of an action M, close under B-linear combinations and then under all coordinates of the images of E_D^V applied to the current submodule under μ. The chosen embedding Q→B^(S) makes those coordinates ordinary elements of M. At each step fewer than κ elements are required; a countable iteration remains of size less than κ and produces a subaction. As the submodule is B-stable, the projector preserves its finite-coordinate sums, so Q tensor M_small is exactly (Q tensor M) intersect M_small^(S); this justifies closure and the restricted action. Its defining equations are inherited from M. The poset of all such small subactions is κ-filtered and has union M.

There is a set of isomorphism classes of actions whose underlying sets have size less than κ. Each is κ-presentable: an underlying module map into a κ-filtered colimit lifts after imposing fewer than κ module relations, and action compatibility adds fewer than κ equations, since E_D^V of the source also has size less than κ. Equality of two lifts is checked on fewer than κ elements. The same argument handles morphisms. Hence C_B is generated under κ-filtered colimits by a set of κ-presentable objects; together with the colimits already constructed, this proves local presentability.

The action on N tensor_B M is induced by N tensor_B μ, using the canonical tensor comparisons for E and G; the unit and Lie-action equations tensor with N. The associativity and unit comparisons are those of ordinary module tensor products. No flatness of N is needed.

Finally, the first added coefficient is the kernel in §6, followed by tensoring with the inverse canonical line to change that newly marked coordinate to the left-coefficient convention. The splitting on affine sections is natural in morphisms of actions. Consequently this kernel functor preserves all colimits: the natural direct-sum decomposition (6.4) remains a direct-sum decomposition after taking any colimit. Lemma 6.1 proves its arbitrary-base-change comparison. Repeat the same argument for each additional coordinate. This proves the assertion for every coefficient, including the natural relative differential-module structures. ∎

**Lemma 7.2.** For every homomorphism of commutative C-algebras B→B′, there is a canonical equivalence

    B′-Mod tensor_(B-Mod) C_B ≃ C_(B′),                (7.1)

and its underlying-coefficient functor is ordinary scalar extension. In particular this is an equivalence of the full categories, not only their regular objects.

**Proof.** First identify C_(B′) with the category Mod_(B′)(C_B) of internal B′-module objects in C_B. Such an object is an action M over B together with a B′-action on M by endomorphisms of that action. Equivalently M is a B′-module and μ is B′-linear. Localization and the principal-parts quotient identify its source and target with E_(D′)(M) and G_(D′)(M) over B′. The unit and Lie-action equations are the same equations after these identifications. This gives mutually inverse functors on objects and morphisms. It works for arbitrary B′, not only for quotients or flat extensions.

We verify rather than assume the relative-tensor universal property. Put C=C_B and D=Mod_(B′)(C). The functor

    b:(B′-Mod)×C→D,    (N,M)↦N tensor_B M,

is separately cocontinuous and B-balanced. Let E be any presentable complex-linear category and let H:(B′-Mod)×C→E be a separately cocontinuous B-balanced functor. For an internal module (M,ρ), define

    H_bar(M,ρ)=coeq[ H(B′,B′ tensor_B M) ⇉ H(B′,M) ].  (7.2)

One arrow is H(B′,ρ). For the other, use balancing to identify the source with H(B′ tensor_B B′,M), then apply multiplication B′ tensor_B B′→B′. Since colimits of internal modules are created in C, this construction is cocontinuous.

For b(N,M), balancing turns (7.2) into H applied to the usual free B′-module coequalizer

    B′ tensor_B B′ tensor_B N ⇉ B′ tensor_B N → N

in its first argument. Thus H_bar b≃H. Conversely every internal module has the canonical free coequalizer

    Free(B′ tensor_B U(M)) ⇉ Free(U(M)) → M,

where Free(P)=B′ tensor_B P and the two maps are multiplication and the module action. A cocontinuous functor out of D is therefore recovered uniquely, including its natural transformations, from its composite with b by (7.2). This proves the required equivalence of functor categories and hence the universal property of D as the left side of (7.1). Composing with the preceding explicit identification gives (7.1).

The two descriptions give independent checks of the comparison: internal scalar actions identify objects and morphisms directly, while the free coequalizer proves that this same category has the required categorical universal property. Under the universal functor, M goes to B′ tensor_B M with its induced chiral action. Lemma 6.1, iterated as in Lemma 7.1, identifies every coefficient of its factorization family with the ordinary scalar extension of the original coefficient. These canonical comparisons compose by ordinary tensor associativity. ∎

This proof does not tensor a completed topological enveloping algebra with B′, and does not assert that tensor product commutes with its inverse limit. BD §3.6.13’s pro-algebra statement is compatible background; it is not a substitute for (7.1).

## 8. Ordinary coefficient families, descent and marked collisions

A category over a scheme is used here in the chart sense of §1: an ordinary QCoh-linear sheaf of presentable categories, whose pullback on affine parameter schemes is categorical scalar extension. Section 7 proves that scalar-extension assertion by its universal property. An additional formula identifying global sections after every nonaffine base change with an unqualified tensor product of global-section categories is not assumed or proved.

**Lemma 8.1.** The action categories of §7 are canonically equivalent to the ordinary coefficient-family categories of §3, on every parameter scheme T→X^I. The equivalence preserves the minimal coefficient, all added coefficients and their ordinary base-change comparisons. These categories, objects, morphisms and comparison functors satisfy Zariski descent in T.

**Proof.** On the universal marked chart X^I, use [Rozenblyum, arXiv:1010.1998](https://arxiv.org/html/1010.1998v1), Definition 3.3.1 and Theorem 3.5.1. Its marked variables are O-linear; differential operators act only in the unmarked variables. The inverse construction successively takes the kernel of the unit-surjective chiral action. We use its theorem for that classical action/family equivalence; we do not infer arbitrary categorical scalar extension from the citation.

Restrict first to an affine parameter chart U=Spec R⊂X^I. The construction and its comparisons restrict to U because localization, principal parts, the action and its kernel are local in the parameter. For any affine parameter T=Spec B→U, an action over B is, by Lemma 7.2, an internal B-module in the action category over R. The equivalence on U carries this to an internal B-module in its coefficient-family category. On each configuration chart, a B-module object in quasi-coherent sheaves is precisely a quasi-coherent sheaf on its affine base change to Spec B. All structure maps become B-linear. Their unit, permutation and factorization equations are unchanged; the diagonal operations in unmarked variables are the same module operations after restriction of scalars. This identifies the internal family category with the actual family category over T, and gives the required equivalence there. Conversely restriction of scalars recovers the internal module structure, so this argument proves essential surjectivity and full faithfulness, rather than only producing some families.

The conversion of a coefficient in unmarked variables R from right differential modules to ordinary left coefficients is tensoring with ω_(X^R)^(-1), without a cohomological shift. The normal diagonal restrictions are ordinary: the following local calculation verifies the requisite regularity and fixes their unit normalization.

Suppose one new variable z is promoted after some earlier marked or promoted variables, and choose an earlier variable t_i. Put f=z-t_i. In the affine coordinate model, E=E_D^V(M) has f invertible. For Γ=G_D^V(M) there is an exact sequence of B-modules

    0→M --m↦[dz/f] tensor m--> Γ --f--> Γ→0.           (8.1)

For M=B, surjectivity follows by division by f in the localization. If f h is regular, h is a regular numerator divided by f, and polynomial division reduces its class to a unique b/f; this proves the kernel assertion. The sequence splits as B-modules because Γ for M=B is projective by §6. Tensoring therefore proves (8.1) for arbitrary M. This is also verified directly at each finite monic denominator: in B[z]/P^N the kernel of multiplication by f is generated by P^N/f, since f is a non-zero-divisor in B[z]. No reducedness of B is used.

Apply the kernel/cokernel exact sequence for multiplication by f to

    0→K→E --μ--> Γ→0.

Multiplication by f on E is invertible. Consequently f is injective on K and the boundary map gives

    M ≃ K/fK.                                          (8.2)

To compute that boundary, lift [dz/f] tensor m using the chiral unit and multiply the lift by f. The result is u(dz) tensor m. After changing the new variable to the left-coefficient convention, (8.2) is exactly the map inserting the normalized vector 1. Thus the ordinary fibre comparison agrees with the module-family diagonal comparison, including its unit. On a general curve the same calculation uses a local parameter for the graph; its residue description makes it independent of that parameter.

Every collision involving unmarked variables factors into such one-variable mergers, after permuting those variables. After each merger the coefficient is again a coefficient of the same family. Applying the injectivity assertion successively proves regularity for the resulting sequence of normal parameters and identifies the ordinary collision pullback with the prescribed coefficient. This also checks that the source's shifted extraordinary-pullback notation is not being identified indiscriminately with an ordinary parameter pullback. The δ-module example in §3 is a pullback in an original marked parameter and remains a genuine ordinary/derived distinction.

Lemma 6.1 at each kernel step shows that the family associated to B′ tensor_B M has coefficients B′ tensor_B M_R, canonically and with all surviving relative differential operators. All permutations, diagonal and factorization comparisons are the ones of the classical equivalence; its functoriality transports them to internal modules and hence to every affine parameter base.

Finally, let {T_a} be any affine open cover of T. Compatible underlying quasi-coherent modules M_a glue to M by quasi-coherent descent. The source and target of the action commute with restriction; therefore the maps μ_a glue uniquely to a sheaf map μ on X×T. Differential-linearity and the unit and Lie-action identities are identities of maps and can be checked on this cover. Morphisms glue by the same argument. For coefficient families, perform the identical gluing at each finite configuration; all comparison maps and their equations glue, and their invertibility and the exclusion of unmarked-diagonal-supported sections are local properties. This proves descent on both sides and glues the equivalences. It also proves descent of the canonical base-change comparisons, rather than postulating a category stack. ∎

**Lemma 8.2.** For every surjection π:I→J, categorical scalar extension along Δ_π identifies the entire action/family category over X^I with the category over X^J. The equivalences preserve the minimal coefficient and are coherent under composition, relabelling and arbitrary parameter base change.

**Proof.** For I=J=empty the asserted equivalence is the identity; assume J nonempty in the divisor argument below. On a parameter chart over X^J, write the marked sections as y_j. The pulled-back divisor from I is D_I=sum_j |π^(-1)(j)|Γ_(y_j), while D_J=sum_j Γ_(y_j). Their positive multiples are cofinal: if m=max_j|π^(-1)(j)|, then D_J≤D_I≤mD_J. Therefore

    O(*D_I)=O(*D_J),    ω(*D_I)/ω=ω(*D_J)/ω.          (8.3)

Equivalently, in a polynomial chart the localization in product_j(z-y_j)^(|π^(-1)(j)|) is exactly the localization in product_j(z-y_j). The argument permits collisions among the y_j and nilpotents in the parameter ring.

The localized action source, the principal-parts target, the unit map and the two-input Lie-action diagrams are therefore identical. They define identical categories with the same underlying modules and morphisms. Lemma 7.2 identifies the category on the pulled-back side with the genuine categorical scalar extension, so (8.3) gives the required categorical equivalence. In coefficient-family terms Lemma 8.1 and its canonical kernel comparisons give that same equivalence at every coefficient. Since all identifications are induced by equality of the localization and principal-parts functors, any composite of surjections gives the same identification. These maps commute with arbitrary base change and glue by the descent just proved. ∎

## 9. Unit insertion, fusion, evaluation and the unconditional chart round trip

Retain the ordinary categories and the chart/sheaf convention of §§6–8. In particular every affine parameter pullback below is the relative tensor product proved in Lemma 7.2; it is not a newly defined substitute for that tensor product.

**Theorem 9.1 (classical categorical admissibility).** For every classical unital BD chiral algebra A on a smooth separated complex algebraic curve X, the ordinary coefficient-family categories of §3 form the QCoh-linear unital weak factorization system required in §1. They have arbitrary parameter base change, coherent categorical collision equivalences for every surjection, coherent unit insertions and separated external fusion, and compatible ordinary coefficient-evaluation functors. The empty category is Vect. Its inserted vacuum realizes Fact(A), with its normalized empty algebra unit and all original collision extensions. Consequently the reconstruction of §§1–2 canonically returns A.

**Proof: insertion.** Let a:I↪J be an injection. For a family M marked by I, regard its coefficient at the extra coordinates J\I as its new minimal coefficient. The full family at further coordinates is the original family with these extra coordinates now marked. This is promotion of marked points; its action is the one supplied by the action/family equivalence. On the universal charts this is also Rozenblyum Remark 3.3.2(i).

The promotion functor preserves colimits by Lemma 7.1 and is QCoh(X^I)-linear. Hence it induces a functor

    β_a: Δ_a^* C_I → C_J

on the genuine category scalar extension. This assertion has a concrete description over any affine parameter T carrying both the old and the added marked sections. Start with the factorization family of an arbitrary action M on T, introduce free variables for the added labels, and pull its corresponding coefficient back ordinarily along the graphs of those added sections. The resulting action is β_a(M). This description agrees with the universal scalar-extension functor: both are cocontinuous and agree on free scalar-extended objects, and the free internal-module coequalizer in Lemma 7.2 presents every object. It therefore also applies when M depends on the added positions and when the graph pullback is nonflat.

The map of underlying coefficients for insertion is the family's unit map, followed by this ordinary graph pullback. It need not be invertible. Iterated promotion gives the same original family with a larger marked subset, so the comparison for two injections is canonical. Permuting added coordinates gives its symmetry comparison. These comparisons commute with arbitrary parameter base change by §§6–8.

**Proof: mixed insertion and collision.** The categorical equivalences for collisions of existing marks are Lemma 8.2. They commute with promotion because the latter's successive kernels commute with parameter base change. If an added coordinate merges with an earlier marked or added coordinate, the comparison is (8.2); its map is exactly insertion of the normalized vacuum. Thus inserting a point and then merging it with an existing point acts as the identity, with the specified unit map. Mergers of several added points give the ordinary diagonal comparisons of the same coefficient family. Their normal parameters are regular in the order verified in §8, so no higher Tor term has been discarded.

These checks give the finite-map composition coherence, not merely its binary instances. To see this explicitly, factor a finite-set map as its surjection to its image followed by inclusion. Decompose the surjection into mergers and the inclusion into singleton insertions. Two such decompositions are related by relabellings, commuting disjoint mergers or insertions, reassociating three mergers, and moving an insertion past a merger, with the insertion-then-merger relation just checked. One can obtain this normal form by moving inserted labels to the end and deleting each that later merges with an earlier label; the remaining mergers record exactly the fibres of the original map. The merger relations hold by the identical-support description of Lemma 8.2 and the all-arity coefficient-family comparisons; the insertion relations hold by restriction of one and the same family; the mixed relations hold by the kernel base-change map and (8.2). Hence the resulting functor and all comparison maps depend coherently on the finite-set map, independently of its decomposition.

**Proof: separated fusion.** On the open where two groups of marked sections are disjoint, write their divisors as D_1 and D_2. Principal parts have the canonical support decomposition

    G_(D_1+D_2)(P)=G_(D_1)(P) direct_sum G_(D_2)(P).  (9.1)

This follows by restricting to neighbourhoods of the two disjoint closed supports; equivalently it is the usual Chinese-remainder decomposition of principal parts. It is unaffected by repetitions within a group. For actions M,N at the two groups, give M tensor N the action whose components in (9.1) are μ_M tensor id_N and id_M tensor μ_N. Each component extends to localization away from the other group, since that divisor is disjoint from its support.

The unit equation holds because the canonical principal-parts quotient decomposes into those same two components. To check the Lie-action equation, decompose its two-variable supported target according to which of the two disjoint groups receives each variable. When both variables meet one group, the equation is the module equation for that factor tensored with the other factor. When they meet different groups, the two actions commute because they act on different tensor factors, and the bracket term, supported on equality of those variables, restricts to zero on the two disjoint groups. These are all components of the target, so the full equation holds. The construction is functorial and separately cocontinuous and therefore gives the external fusion functor on the tensor product of the categories.

For three or more mutually separated groups, the same action is the sum of the actions of the individual tensor factors in the canonical direct-sum decomposition by support. This proves associativity and all iterated-partition comparisons; permutations permute the summands and give symmetry. The empty group gives ordinary scalar tensoring. These formulas also prove compatibility with arbitrary parameter base change and with collisions within a group, since (9.1) and its action maps commute with that base change. No equivalence of the complete fusion functor is asserted.

There is one remaining mixed comparison to verify on full categories. Promote a new point into the first group and restrict to the open where it stays separated from the second group. In the new variable the second summand of (9.1) is absent. The coefficient kernel for the fused object is therefore the kernel of μ_M tensor id_N. The split exact sequence of §6 identifies it canonically with ker(μ_M) tensor N, even when N is not flat over the parameter ring. This is precisely fusion after promotion. Iteration handles any set of newly inserted points and every refinement of a partition. Together with the finite-map coherences above, this proves all unit/fusion/collision mixed diagrams required by the weak factorization system. These are equalities on the minimal coefficients of every action, not only on the vacuum. The forgetful functor U is faithful (Lemma 7.1), and the action/family equivalence is fully faithful; hence the equalities of the specified coefficient maps prove the corresponding natural-transformation diagrams and their higher composition coherences.

**Proof: evaluation and descent.** Define F_T by the minimal underlying coefficient M of an action, equivalently the minimal coefficient of its family. Lemma 7.2 identifies its pullback comparison with ordinary tensoring, and Lemma 8.2 gives the collision comparison. The insertion comparison is the unit map just constructed. On separated external fusion, the minimal coefficient is the ordinary external tensor of the minimal coefficients, so its evaluation comparison is invertible. Every comparison was constructed from the same action, its canonical kernels, the unit map or the canonical support decomposition. The preceding calculations verify that their diagrams commute. Section 8 glues these functors and diagrams on arbitrary parameter schemes: objects and morphisms descend as quasi-coherent modules with action maps, and every displayed identity can be checked on an affine cover.

**Proof: empty category and vacuum.** With no marked points the principal-parts target is zero, so a vector space has a unique action and C_empty=Vect. Its associated no-defect family is

    M_R=Fact(A)_R external_tensor M_empty.

This is a factorization module with that minimal coefficient; uniqueness follows from the action/family equivalence, or directly by taking the empty marked configuration in its module factorization map. In particular the empty unit C gives the regular family Fact(A). Promotion to I therefore gives

    F_I(v_I)=Fact(A)_I,                               (9.2)

with the original insertion, collision and disjoint factorization comparisons. The empty algebra is C with its usual multiplication and unit, since the empty category and evaluation are the usual vector-space category and its identity functor. The coefficients in (9.2) have no diagonal-supported sections by the classical BD factorization theorem. Thus all of §1's admissibility hypotheses hold. Applying the already proved reconstruction and BD Theorem 3.4.9 returns A, including every diagonal extension. This proves the unconditional chart round trip. ∎

The proof has three distinct checks on the former gap. The unit algebra A=ω_X gives the full category QCoh(T) directly. For general A, ordinary kernel preservation is proved from the unit splitting on affine sections, with nonflat extensions allowed. The independent categorical issue is settled by internal scalar actions together with the explicit relative-tensor universal property. Marked collision equivalences then come from equality of the actual localization and principal-parts functors, while (8.1)–(8.2) verify the mixed normal restriction. None of these steps equates an arbitrary derived pullback with an ordinary one.

The result concerns the complete ordinary coefficient-family system specified in §3. It neither extracts the needed geometry from a bare ribbon fibre nor identifies an unspecified physical line category. Those distinctions, Theorem N, the delta pullback control, and the absence of a claim of strong fusion remain unchanged. The extra global-sections tensor/1-affineness assertion excluded at the start of §8 is not used in any chart-level pullback or reconstruction.

## 10. An actual module with the ordinary collision quotient

The kernel mechanism can be checked in a nontrivial classical chiral module without a finite pole cutoff. Let A=C[x]/(x²) be the constant vertex algebra, with translation zero. For any commutative C-algebra B, any B-module M and any B-linear N:M→M with N²=0, the action x↦N defines a constant vertex module. Its field identities reduce to the associative module identity for A, so this is an actual chiral-module example.

Write A tensor_C M=M direct_sum M, let

    ρ(m_0,m_1)=m_0+N m_1,    u(m)=(m,0),

and let h be the coordinate difference from its single marked point. The action on finite Laurent polynomials is the principal-parts quotient after applying ρ. Its coefficient kernel is therefore

    K={v=sum_(n in Z) v_n h^n, finite support:
                         ρ(v_n)=0 for every n<0}.                 (10.1)

Define e:K→M by e(v)=ρ(v_0). Then e is onto with the normalized unit lift u(m), and e(hv)=ρ(v_(-1))=0. Conversely, if e(v)=0, the actual Laurent polynomial v/h belongs to K: its only new negative coefficient is v_0, which is killed by ρ. Thus

    0→K --h--> K --e--> M→0,    K/hK≃M.                         (10.2)

Multiplication by h is injective because h is invertible on the ambient Laurent module. The division in this proof is not projected back into an input window.

A second derivation gives the complete kernel decomposition. Since ρu=id,

    A tensor_C M=u(M) direct_sum ker ρ,
    ker ρ={(-Nm,m):m in M}.

Condition (10.1) becomes

    K=u(M[h]) direct_sum (ker ρ)[h,h^(-1)].                      (10.3)

The second summand has invertible h, while the first has quotient M. This proves (10.2) again and shows directly that its kernel, quotient and normalized unit commute with every B→B′. Neither M nor B′ needs to be flat.

The owner's [exact script](scripts/check_collision_module.py), with [JSON results](scripts/check_collision_module.json) and [stdout](scripts/check_collision_module.stdout.txt), uses B=Q[ε]/ε², M=B² and N_a=[[0,a],[0,0]] for a=0,1,ε. It passed 3,160 assertions on 243 Laurent inputs across these three module actions in 0.654 seconds, using 17,252,352 bytes of peak RSS. Inputs have exponents from -2 through 1; the division is retained down to -3. It tests the quotient map, unit lift, multiplication and division, and nonflat reduction ε→0. These are finite checks of the displayed actual-module identities; the proof above establishes the unbounded assertion.

The separate [principal-parts script](scripts/check_principal_parts.py) passed 23,394 assertions, including 256 split-kernel matrices, over the same dual-number coefficient ring. It checks monic denominator stages with repeated and nilpotent roots, specialization ε→0, and the negative unsplit-kernel control. It took 48.535 seconds with 18,202,624 bytes of peak RSS. These finite calculations corroborate the local algebra. The relative-category tensor product, descent and all-arity categorical coherence are proved in §§7–9, not inferred from these scripts.


## 11. Invariant normal restriction and the canonical line

Equations (8.1)–(8.2) use a local coordinate and a corresponding trivialization of the canonical line. The following invariant statement records their meaning on an arbitrary smooth curve.

**Lemma 11.1.** Let T be a classical complex scheme, p:X_T→T, and ω=ω_(X_T/T). Let D be the sum of finitely many marked graphs, and choose one of those graphs i:S→X_T, identified with T, corresponding to a map s:T→X. Let M∈QCoh(T) carry a unital marked chiral action, and put

    W=ω tensor p* M,
    E=j_*j*(A external_tensor M),
    G=(ω(*D)/ω) tensor p* M,
    K=ker(E --μ--> G).

The unit induces a canonical map W→K. Its restriction gives an isomorphism

    i*W=s*ω_X tensor M → i*K.                              (11.1)

Moreover,

    Tor_q^(O_(X_T))(K,O_S)=0   (q>0),
    i*(ω^(-1) tensor K) ≅ M.                               (11.2)

These are canonical ordinary comparisons, compatible with arbitrary parameter base change and with the surviving relative differential operators. No flatness of M, of the parameter change, or of the underlying O_X-module of A is assumed.

**Proof by the unit diagram.** The unit identity gives a commutative diagram with exact rows:

    0 → W → W(*D) → G → 0
        ↓      ↓     ║
    0 → K →   E   → G → 0.                                (11.3)

Here W(*D)=ω(*D) tensor p*M. Exactness of the top row for arbitrary M follows from the principal-parts calculation of §6; exactness on the right of the bottom row follows from the unit identity. No row is asserted to split as a sequence of sheaves.

Locally, let f generate the ideal of S. Since S is contained in D, multiplication by f is invertible on both W(*D) and E. Their derived restrictions to S therefore vanish: the two-term normal Koszul complexes are acyclic. Applying derived restriction to (11.3) consequently identifies

    L i* W → L i* K

through the displayed unit map, as an isomorphism.

The graph is a relative effective Cartier divisor. Its structure sheaf is flat over T, so the sequence defining the graph remains exact after tensoring with the pullback of any M. Thus W has no higher normal Tor and

    L i* W=i*W=s*ω_X tensor M

in degree zero. The same holds for K, proving (11.1) and the first assertion of (11.2). Tensoring with the inverse canonical line proves the last assertion.

This use of derived restriction computes the normal Tor groups of these particular coefficients. It makes no identification between ordinary and derived pullback in an arbitrary original marked parameter.

**Independent ordinary normal-Koszul verification.** Work where the graph ideal is generated by f and ω is trivialized by a relative one-form η. Multiplication by f is invertible on E, hence injective on K. From the top row of (11.3), division by f gives

    G[f] ≅ W/fW,
    [η/f] tensor m ↦ η tensor m.                           (11.4)

Multiplication by f on G is surjective. These assertions also follow directly by taking the kernel and cokernel of multiplication by f in that row; they do not require tensoring an unsplit sequence with M.

Applying the same calculation to the bottom row gives

    G[f] ≅ K/fK.                                           (11.5)

The boundary sends [η/f] tensor m to the class of u(η) tensor m: lift the principal part by the localized unit and multiply the lift by f. Combining (11.4) and (11.5) therefore gives precisely the map induced by W→K, rather than an isomorphism chosen from a splitting. Since the normal Koszul resolution has length one and f is injective on K, all higher normal Tor groups vanish.

Both proofs identify the same canonical unit map. They consequently agree on overlaps. The kernel comparison of §6 and ordinary pullback of the canonical line prove compatibility with every parameter base change. The maps retain the surviving differential operators because the unit diagram and its canonical kernel maps do so. ∎

**Iterated normal collisions.** Apply Lemma 11.1 after each promotion, treating previously introduced coordinates as parameters for that step. Every merger eliminating an unmarked label has the normalized unit comparison (11.2). After that merger its quotient is again a coefficient of the same family. Induction therefore proves regularity of the resulting sequence of normal equations and identifies its ordinary collision pullback with the prescribed coefficient. This covers normal collision maps fixing the original marked labels. Collisions among original marks remain the categorical equivalences of Lemma 8.2; they do not acquire a general ordinary-versus-derived pullback identification.

**A general-curve negative control.** Take X=P1, A=ω_X, T=X, the diagonal marked graph, and M=O_X. The action is the principal-parts quotient, so K=W. Consequently

    i*K=ω_X ≅ O_(P1)(−2),

which is not O_X. Thus an unqualified global identification of the raw right coefficient with M would be false. The asserted left-coefficient comparison is nevertheless

    i*(ω^(-1) tensor K)=O_X.

The transitions can be checked directly. On the overlap z,t≠0, set w=z^(-1), v=t^(-1). Then

    w−v=−(z−t)/(zt),     dw=−z^(−2)dz,

and

    dw/(w−v) − dz/(z−t)=−dz/z.                            (11.6)

The last expression is regular near the graph on this overlap, so the principal-part residue is unchanged. The raw unit coefficient transforms by the canonical-line transition; its inverse canonical line cancels that transition. This verifies the normalization by a second coordinate calculation.

There is also no hidden sheaf splitting. Already on A1, every O-linear map from ω(*0)/ω to ω(*0) is zero: each source element is killed by a power of z, whereas z is invertible on the target. The affine section-module splitting used in §6 is therefore essential to the proof's stated formulation.


## 12. Verification of the invariant normal comparison

The owner opened the classical source definitions and checked the invariant unit diagram of §11 independently. The source conversion by the inverse canonical line is also explicit in /Users/raeez/cbc/chapters/theory/bar_cobar_construction.tex:414–420. The unrelated nonsplit hull of S support-saturated-partners.tex:480–536 does not have the unit-surjective principal-parts diagram used here.

The independently implemented [check_normal_line.py](scripts/check_normal_line.py), with its [saved result](scripts/check_normal_line.json), passed 727 exact assertions in 0.563 seconds using 17,661,952 bytes. It tests 30 P1 overlap charts over Q[epsilon]/epsilon², their inverse-coordinate residue identity, the canonical-line transition and its cancellation, and ordinary reduction epsilon→0. It also tests 162 polynomial normal-module inputs, including the epsilon-annihilated module. Multiplication and division retain their actual output degree; no projection to a finite input window creates a false kernel.

These checks corroborate the coordinate identities. The sheaf-level comparison, normal Tor vanishing and coherence follow from the unit diagram and the independent normal-Koszul proof in §11; no categorical theorem follows from the finite run. The clarified classical family definition retains arbitrary minimal quasi-coherent modules and nonflat parameter changes. The earlier independent checks keep their historical scope; this continuation has not received independent adoption. The physical line-category comparison remains a separate open application.
