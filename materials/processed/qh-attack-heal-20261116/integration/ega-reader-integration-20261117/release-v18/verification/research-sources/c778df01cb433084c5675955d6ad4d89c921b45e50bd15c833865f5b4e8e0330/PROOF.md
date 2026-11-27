# F2-N03: the parameter-family obstruction

## 0. Statements and status

Current correction: §8 replaces the same-left-action assertion by the side-preserving/signed-right-action proof, preserving a=b at every fibre, and uses R-length for the arbitrary-DVR formula. Section 9 proves reciprocal equality of local elementary divisors. Thus two positive integers remain: m_+ at 3/2,2/3 and m_- at −3/2,−2/3. Neither value is determined. The retained matrices reach D5; the new degree-seven continuation is recorded separately and gives no deciding D8/D11 rank unless its saved status explicitly says so.

For the actual W4 family in PRIOR.md, **a=b at each of the four exceptional levels is proved in §§2,8,10**, using the adopted orbit/Ext calculation and the relative family Yoneda model. The two reciprocal-pair common lengths m_+,m_- remain undetermined; §9 proves equality within each pair. Exactly one torsion factor in each of degrees 9 and 12 is **ADOPTED**. The DVR/first-jet criterion (§1), dg-algebra countermodels with arbitrary common length (§3), and a parameter Cartan contraction on the raw spectral-flow CE family (§4) are proved here. No general-theory novelty is claimed.

The initial recursive Miura/PBW run (§5) completed D0–D4; subsequent retained work completed D5. Later resolution lifts remain partial. Sections 11–12 now prove that the direct polynomial three-ghost coupled complex computes the same full smooth vacuum Ext and local parameter torsion. It permits a direct D11 computation without lower resolution lifts. Its separate exact matrices and checks are in scripts/coupled/. No deciding rank or exponent is inferred from partial rows. The geometric route still needs descent of the parameter homotopy to the actual cone.

All computations use exact rational, polynomial or finite-field arithmetic, with explicit distinctions between a lower-bound modular rank and a rational equality. A rank obtained by reconstructing from an adopted cohomology table is not a direct rank computation of the parameter differential.

## 1. What the actual first-jet matrix must decide

**Lemma.** A bounded finite free complex K over a DVR R, with uniformizer t, splits up to chain isomorphism as a sum of one-term free complexes and two-term complexes [R --t^s--> R], s>=0. If r_q is its generic cohomology rank and e_q is the number of nonunit two-term summands ending in degree q, then

dim_(R/t) H^q(K/t)=r_q+e_q+e_{q+1}.

A two-term summand ending in q of length s>=1 has its first nonzero Bockstein on page s, from degree q-1 to q, of rank one. More generally

length_R H^q(K/t^m)=m r_q+sum_{s in T_q}min(m,s)+sum_{s in T_{q+1}}min(m,s),

where T_q is the multiset of torsion lengths of H^q(K).

**Proof.** Apply Smith reduction to a nonzero differential. A diagonal entry t^s joins one basis vector in its source to one in its target. The preceding differential has zero component on that source, and the following differential kills that target, because t^s is a nonzero divisor and adjacent products are zero. Hence the two-term complex splits off. Iterate; the remaining zero differentials give the one-term free summands. Reduction modulo t proves the residue-field dimension formula. Modulo t^m the kernel and cokernel of multiplication by t^s each have R-length min(m,s); a free summand contributes m. For the actual C-DVR these lengths equal C-dimensions. Finally the Bockstein representative t^-j d(1)=t^{s-j} first reduces to a nonzero class exactly when j=s. This also gives a second proof of the fibre dimension formula via the universal-coefficient short exact sequence. QED.

For the adopted W4 dimensions, solve this recurrence from degree zero upward. It gives e9=e12=1, all other e_q=0. It gives no exponent. For the actual polynomial differential D_q(t)=D_q,0+t D_q,1+O(t²), the induced linear map over R/t² is represented over C by

J_q = [[D_q,0,0],[D_q,1,D_q,0]].

If r=rank D_q,0, then rank J_q=2r+rank(bar D_q,1:ker D_q,0→coker D_q,0). A proof is to perform invertible constant row/column operations putting D_q,0 into identity and zero blocks, then eliminate its derivative rows and columns. The remaining block is precisely the induced derivative. Independently Smith reduction over R/t² shows that each unit contributes rank two, each t-entry rank one, and every t^s entry with s>=2 rank zero.

Consequently a=1 precisely when the actual D8 first-jet matrix has rank 25487 instead of 25486, and b=1 precisely when the actual D11 first-jet matrix has rank 5315 instead of 5314. These numbers use the adopted special ranks 12743 and 2657. The matrix orientation in the copied PBW engine is transposed; transpose leaves all these ranks unchanged. A good-prime rank attaining the larger value is a rational certificate once all rational denominators and the known upper bound are checked. A lower rank modulo a prime alone would not prove a>1.

The elementary formulas and rank increments were verified by explicit t,t²,t⁴ blocks in `scripts/torsion_structure.py`. That check is not a W4 rank computation.

## 2. The degree-three action couples the two torsion lengths

**Theorem.** For the actual local W4 complex at each of the four levels in PRIOR.md, with the family Yoneda product furnished by the polynomial pro-resolution (w-bulk Lemma 9.5), the two torsion lengths are equal: **a=b**. Their common positive value is not determined by this theorem.

**Inputs and their scope.** Use the adopted four-fibre dimensions, the canonical cone triangle at tau=-3/2, and its module structure under H*(sl4) acting by precomposition (w-bulk Proposition 10.1, §§12.1–12.3). The coefficient is the fixed-level spectral-flow complex H*(sl2+C²)[-17]; the two geometric rows have degrees three and five and transgression i_{Zx+Zz}. The primitive theta3 restricts to a nonzero multiple of the sl2 primitive omega. These are fixed-level geometric inputs, not a claim of an R-linear orbit comparison. The ONLY family operation used is multiplication by a degree-three class in the derived endomorphism algebra of the polynomial vacuum. It is defined by composition of the R-linear pro-resolution. In the torsion-free endomorphism model of Lemma 9.5, reduction and composition commute on every retained coefficient block; its augmentation comparison identifies the product with Yoneda and the same complex computes the Bocksteins. The argument uses this standard family model, not an assumed equivariant descent of the spectral-flow homotopy of §4 below.

**First step: two nonzero products at the special fibre.** The adopted orbit model, after its common suspension, has the two-row form

T_gr = h tensor Lambda(x,z,omega) ⊕ g tensor Lambda(x,z,omega),
|h|=8, |g|=10, |x|=|z|=1, |omega|=3,
d(h alpha)=g i_{Zx+Zz}alpha, d(g alpha)=0.

In the h row, contraction has kernel spanned by 1,x-z,omega,(x-z)omega. In the g row its cokernel has representatives x,xz,x omega,xz omega. Thus multiplication by omega is nonzero from T8 to T11 and from T9 to T12 (indeed all four relevant consecutive degree-three maps have rank one). These nonzero associated-graded maps remain nonzero through the two-row filtration: their source classes and detected target components survive. The explicit 16-dimensional exterior model in `scripts/torsion_structure.py` verifies d²=0, anticommutation with omega and the induced ranks, independently of the large vacuum matrices.

Write E for the special W4 Ext and A=H*(sl4). In the cone exact sequence A→E→T→A[1], A9=A11=A13=0. The adopted table and product eta5 eta7=0 imply: E8→T8 is onto; E9→T9 is an isomorphism (delta9=0); E11→T11 is injective; E12→T12 is an isomorphism (the map A12→E12 is zero). Module linearity now proves

eta3: E8/(C eta3 eta5) → E11 is nonzero,
eta3: E9 → E12 is nonzero.

Both source spaces on the left have dimension one; E11 also has dimension one. The first product is independent of the choice of representative modulo eta3 eta5 because eta3²=0. Complementary and reciprocal fibre algebra equivalences carry the unique nonzero degree-three line and hence the same two nonzero products to the other three fibres. No relative parameter equivalence is needed for that transport.

**Second step: Bockstein derivation.** H3(K_R) is free of rank one and H4(K_R)=0, so base change makes any chosen eta3 in E3 the reduction of an R-cohomology class. Therefore eta3 is permanent in the Bockstein sequence and multiplication by it commutes with every Bockstein, with the degree-three sign. Let u in E8 represent the additional line, v span E9, x=eta3 u span E11 and y=eta3 v be the nonzero corresponding line in E12. By §1 the only nonzero Bocksteins are the pair u→v on page a and the pair x→(a nonzero line in E12) on page b.

If a<b, page a gives beta_a(x)=beta_a(eta3 u)=-eta3 beta_a(u), a nonzero multiple of y, contradicting the asserted later first differential for x. If b<a, then at page b both eta3 and u have zero Bockstein, forcing beta_b(x)=0, again a contradiction. All four classes survive to the smaller page because no other torsion pair can remove them. Thus a=b.

**Independent DVR-module proof.** Multiplication by the lift of eta3 maps the torsion module H9(K_R)=R/t^a to the torsion summand R/t^b of H12(K_R); a torsion element has no nonzero image in the free summand. The nonzero E9 product says its map modulo t is nonzero. Such a map must have unit coefficient at the target generator, hence b<=a. Naturality of the universal-coefficient sequence identifies the nonzero E8→E11 quotient product with the induced map on t-torsion kernels. A unit-coefficient map R/t^a→R/t^b has nonzero map on those kernels only when a<=b: for a>b it sends t^{a-1} to zero. Therefore a=b. This proves the same claim without spectral-sequence signs. QED.

The potentially delicate dependency is the family multiplication and its specialization, not the numerical table. It is explicit above for independent checking. No assertion a=b=1 follows from equality of the lengths.

## 3. Even the additional products do not force a simple root

**Theorem (countermodels to inference from fibre algebras).** For every integer m>=1 there is a bounded finite free graded-commutative dg algebra K^(m) over R=C[t]_(t), whose generic cohomology is Lambda(a3,b5,c7), whose special cohomology has the entire adopted W4 dimension table, with ab and ac nonzero, bc=0, and with both additional degree-three multiplication maps of §2 nonzero. The natural map from Lambda(a3,b5,c7) has special kernel (b5 c7). Nevertheless H9(K^(m))=R/t^m and H12(K^(m))=R⊕R/t^m. Thus even these algebra and canonical-map data cannot decide whether the common W4 length is one.

**Construction and proof.** In Lambda_F(a,b,c), F=C(t), degrees (3,5,7), take the R-lattice A with basis

1,a,b,c,ab,ac,f=bc/t,g=abc/t.

It is a subalgebra: the only extra nonzero products needed for closure are bc=t f, a f=g, (ab)c=t g and b(ac)=-t g, with their graded commutations. Give A zero differential. Over F it is the ordinary exterior algebra. Its special algebra has ab,ac nonzero but bc=0, and the image of the original exterior algebra has kernel exactly the ideal (bc), whose basis is bc,abc.

There is an augmentation-preserving algebra map A→Lambda_R(a) killing b,c,ab,ac,f,g. Let M=Lambda_R(a) tensor [R u --t^m--> R v], with |u|=8, |v|=9, and the tensor differential. Thus with x=a u, y=a v, one has |x|=11, |y|=12, du=t^m v, dx=-t^m y. Form the square-zero extension K^(m)=A⊕M, using that A-module structure, and M²=0. The tensor differential is an A-derivation, so this is a unital dg algebra. Generic M is acyclic; over R its cohomology is R/t^m in degrees 9 and 12. Modulo t its differential vanishes and it contributes one class each in degrees 8,9,11,12. Together with A's degrees 0,3,5,7,8,10,12,15 this gives exactly

(1,0,0,1,0,1,0,1,2,1,1,1,2,0,0,1).

The additional products are a u=x and a v=y, both nonzero. All special algebras (including these products) and generic algebras are independent of m, while the first nonzero Bockstein page is m. This proves the assertion. QED.

The exterior-lattice construction proves associativity without a structure-constant guess. An independent exact check in `scripts/torsion_structure.py` verifies associativity, graded commutativity, the derivation identity, the special products and first-jet ranks for m=1,2,3. A separate square-zero extension with trivial positive A action permits arbitrary unequal a,b while retaining only the original three primitive products; it fails the extra module-action requirement used in §2, as it should. These countermodels are NOT proposed W4 realizations. They show exactly why a derivative of the actual family, or a new family-specific homotopy, is necessary after the fibre calculations.

## 4. A parameter Cartan contraction exists before geometric descent

**Theorem (raw spectral-flow family).** Let g be a complex semisimple Lie algebra, lambda a nonzero integral coweight, k0 a fixed complex number, R=C[k]_(k-k0) and t=k-k0. Let V_R be the universal affine vacuum with its PBW R-lattice, and V_R,(lambda) its spectral flow, with h0 acting by the ordinary Cartan action plus k(lambda,h). Use finite-support continuous CE cochains of g[[z]] with values in this module, algebraic state sums and the usual direct sum by total Cartan weight. Multiplication by t is null-homotopic on that CE complex. Its R-cohomology is therefore annihilated by t; no higher-order torsion occurs in this RAW spectral-flow family.

**Proof.** Decompose the cochains by the unshifted total root weight beta. The differential preserves beta, and the total action of a Cartan h on this summand is the scalar

ell_beta(h)=beta(h)+k(lambda,h).

The CE Cartan formula is d i_h+i_h d=ell_beta(h) id. This formula includes the coefficient-module action and the adjoint action on the CE arguments; omitting the second term would give the wrong beta. If beta+k0 iota(lambda) is nonzero, choose h_beta on which it is nonzero. Then ell_beta(h_beta) is a unit in R, so this summand is contractible. Define a homotopy for t id on it by t ell_beta(h_beta)^-1 i_{h_beta}. If beta=-k0 iota(lambda), choose h with (lambda,h) nonzero and take i_h/(lambda,h), since ell_beta(h)=t(lambda,h). Both maps are R-linear. Finite-support cochains and algebraic states lie in a finite sum of weight summands; no uniform denominator or convergence of infinitely many operators is needed. Contraction by a constant Cartan element preserves the continuous finite-support condition. Assembling these maps proves dH+Hd=t id. QED.

For the actual orbit lambda=(2,0,0,-2) at k0=-11/2, take h=diag(1,0,0,-1)=Zx-Zz on the resonant block. Then (lambda,h)=4, so H=i_h/4. The fixed-level coefficient cohomology is the adopted H*(sl2+C²)[-17]. The exact sequence for multiplication by t, whose chain terms are R-free, and the t-annihilation just proved give

H^q(N_R)=C for q=18,19,21,22, and zero in every other degree,

as R-modules with t acting by zero. Indeed the fibre dimensions in degrees 17,...,22 are (1,2,1,1,2,1), and dim H^q(fibre)=dim H^q(N_R)+dim H^{q+1}(N_R); starting below degree zero fixes the four nonzero answers. This is an actual parameter-family CE conclusion, with the fixed-level cohomology cited. It is NOT yet a W4 torsion-length conclusion.

**Why descent is still required.** The W4 comparison cone T is a geometric construction using a stabilizer torsor and the opposite-twist coefficient line, not the raw CE fibre N_R. The opened proof of w-bulk Lemma 12.1 explicitly cancels the scalar character k(lambda,Z) against that line when identifying its fixed-level stabilizer operations. Consequently the Cartan scalar used above cannot simply be declared unchanged after descent. One needs an R-linear geometric coefficient model and a homotopy compatible with its transition maps, its opposite-twist line and its attachment to the basepoint. Fixed-level insertion and transgression matrices do not provide this parameter comparison.

The elementary danger is visible without geometry. The two-term filtered complex with differential [[t,1],[0,t]] has each associated-graded piece [R --t--> R], where multiplication by t is null-homotopic. But the total differential has a unit entry and determinant t², so its cokernel is R/t². The two graded homotopies do not combine to a total homotopy. Thus “all local pieces have simple torsion” does not prove that their glued object does. This example is not asserted to be the W4 cone; it identifies the exact invalid inference the geometric route must avoid.

**Potential completion, with the missing step retained.** If an actual R-linear triangle A_R→K_R→T_R were constructed with free H*(A_R) of the generic affine ranks, the generic map an isomorphism, and multiplication by t null-homotopic on T_R, then every torsion element of H*(K_R) would be killed by t. To prove this, a torsion x maps to a t-annihilated class of T_R, so tx belongs to the image of H*(A_R). The latter map is injective because it is generically an isomorphism and its source is free. Its image contains no torsion, forcing tx=0. This would prove the common length is one. The new obligation is precisely the R-linear, homotopy-compatible geometric cone, not the already proved raw Cartan formula. No such cone comparison is established here.

## 5. Actual first-jet calculation and remaining obstruction

`scripts/first_jet.py` uses a local byte copy of the request-7 polynomial Miura/PBW engine and OPE file. It replaces scalar arithmetic by F_p[e]/e² at tau=3/2+e, p=1000003, and retains the tensor Koszul contraction and every derivative term in its recursive lifts. This differentiates the actual polynomial resolution; it does not input the desired Bockstein or guess a two-pair differential. All 68 rational OPE coefficient jets were independently checked by symbolic differentiation before lifting. The constant parts of the smallest matrices were independently compared with a scalar engine.

Completed first-jet matrices have source/target dimensions (1,7), (7,77), (77,485), (485,1972), (1972,5690), for D0 through D4. Their total stored nonzero entries are respectively 0,213,5742,67548,429123; entries with nonzero parameter derivative are 0,212,5735,67481,428850. The next degree-six resolution lift is checkpointed but incomplete. D8 and D11 were not reached. The 900-second arithmetic timer ended the run; saving the partial checkpoint and report brought measured elapsed time to 969.574 seconds. Peak RSS was 2,415,820,800 bytes; one numerical process was used, with thread variables at two. This is within the requested 30-minute and 8-GB computation limits.

`scripts/check_first_jet.py` independently verifies all five saved hashes and multiplies adjacent matrices over the dual-number ring: every source vector for q=0,1,2 and 32 deterministic source vectors for q=3 has zero constant AND derivative square. It passed in 10.204 seconds, peak 169,017,344 bytes. These checks certify the recorded blocks and method, not a missing middle rank. Status, resources, complete blocks and partial lift are retained beside the scripts; an incomplete report is not a numerical refutation or a positive test of a=1.

The algebra route proves equality of the two lengths and shows, by explicit families, why fibre information cannot determine the common exponent. The raw Cartan route proves simple torsion before descent but does not provide the needed equivariant family homotopy. The actual differential route has not reached the detecting blocks: its recursively expanded resolution grows before those blocks. What is missing is a family-specific reduction of that middle differential (or a compatible geometric descent) retaining the derivative, not a further scalar determinant test or repetition of the known dimension table. The common-exponent question remains open and is not counted as a completed push.

## 6. The actual saturated affine coefficient has a nonzero first derivative

**Proposition.** Put k0=-11/2, R=C[k]_(k-k0), t=k-k0 and lambda=(2,0,0,-2). In the continuous affine CE family N_R of §4, the finite saturated summand at this level, retaining the complete middle sl2 complex, has 17 forced ghosts and residual complex

    CE(sl2) tensor Lambda_R(x,z),    d=d_sl2+t(2x-2z) wedge,

up to the common suspension by 17 and its common differential sign. Here x and z are dual to the central elements Zx and Zz of w-bulk Lemma 12.1. In particular its actual first Bockstein takes the lowest fibre class to a nonzero multiple of x-z. Its ranks from degrees 17,...,22 to the following degrees are (1,1,0,1,1,0). The operator (i_Zx-i_Zz)/4 is a null-homotopy for t. This proposition concerns the affine coefficient, not yet the W4 comparison cone.

**Construction from the affine modes.** Use the matrix units E_ij, i!=j, and the Cartan basis H_i=E_ii-E_44, 1<=i<=3. A ghost for E_ij z^n, n>=0, has shifted energy n+lambda_i-lambda_j. A Cartan ghost has energy n. At total centre weight fixed to its resonant value k0 lambda, the energy-zero cochains have vacuum matter coefficient. All 12 negative-energy root ghosts must occur: four for E_41, at n=0,1,2,3, and two each for E_21,E_31,E_42,E_43, at n=0,1. Their energies sum to -22=k0(lambda,lambda)/2, and their combined root weight is (-8,0,0,8). The required centre weight is (-11,0,0,11). Consequently all five remaining zero-energy non-Levi root ghosts must occur, at n=4 for E_41 and n=2 for the four others. These are the 17 forced factors. The unforced zero-energy ghosts are the three constant Cartans and E_23,E_32. Retaining all of them, rather than projecting to the middle Cartan-weight-zero part, gives the full five-dimensional Levi CE complex with dimensions (1,5,10,10,5,1).

There are no creation-state corrections in this block. A positive matter energy would exceed the saturated bound. A coefficient action by a negative shifted root mode inserts a ghost already among the forced factors and is zero. Zero shifted root modes annihilate the matter vacuum; the only scalar coefficient action is the Cartan character k(lambda,H). The bracket part of the differential is independent of k. On the forced determinant line its constant character cancels k0(lambda,H), as can be checked by the displayed root sum. Thus changing k to k0+t adds exactly t times the exterior Cartan character lambda. That character vanishes on the middle sl2 and takes values 2,-2 on Zx,Zz. After the common suspension the differential is the formula above. The sign of that suspension has no bearing on the nonzero Bockstein or its page.

This also identifies a genuine subcomplex of the raw family: the unshifted central weights and the energy with k fixed at k0 are preserved by the parameter-dependent CE differential. The inclusion induces the fixed-fibre classes used here; no assertion of equivariant descent along the whole orbit stabilizer is being made from this inclusion. Its lowest class is the unique H17(N_0) class of the adopted saturated calculation.

**Two derivations of the derivative and homotopy.** Differentiating the coefficient character directly gives d1=(2x-2z) wedge. Alternatively the CE Cartan formula, including both the coefficient and argument actions, gives

    [d0,i_Zx]_s=[d0,i_Zz]_s=0,
    [d1,i_Zx]_s=2 id,       [d1,i_Zz]_s=-2 id.

The second pair, together with the fact that the level enters only the scalar Cartan action in this block, determines the same central one-form. Subtraction gives [d,(i_Zx-i_Zz)/4]_s=t id. Since H*(sl2)=Lambda(omega3), the Bockstein is exterior multiplication by 2x-2z on Lambda(x,z,omega3). Its four nonzero ranks are the stated ones. In particular it cannot be zero on the lowest class. This is a computation of an actual parameter derivative, unlike the dimension recurrence of §1.

**Exact check and scope.** `scripts/saturated_parameter.py` independently starts from 4-by-4 matrix commutators, enumerates the centre-weight block, and constructs all 32 basis vectors, D0, D1 and the Cartan insertion matrices over Q. It verifies D0²=0, D0 D1+D1 D0=0, D1²=0 and the two displayed scalar Cartan identities in every degree. It also computes the induced Bockstein ranks by quotienting cycles by boundaries. Output: `scripts/saturated_parameter.json`; runtime 1.133 seconds and peak RSS 61,571,072 bytes. The complete matrices are retained, not only their ranks.

The same script checks the *candidate* two-row family on h Lambda(x,z,omega) and g Lambda(x,z,omega), |h|=8, |g|=10, with d0(h alpha)=g i_(Zx+Zz)alpha, d0(g alpha)=0, and d1=(2x-2z) wedge on both rows. It has special dimensions (1,1,0,2,2,0,1,1) in degrees 8,...,15, first Bockstein ranks 1,2,1 in degrees 8,11,14 and t-null-homotopy (i_Zx-i_Zz)/4. These identities follow independently from (x-z)(Zx+Zz)=0 and anticommutation of contractions. This is not, by itself, an identification of that candidate with the actual W4 orbit family. In particular the script explicitly records `actual_W4_identification: false`.

## 7. The infinitesimal comparison: construction, and the remaining coherence test

This section records the next attempted construction explicitly. **It is not yet a proved relative orbit theorem.** The distinction matters because §6 computes the fibre derivative, whereas the needed Bockstein is on the descended coefficient complex. The finite calculation alone cannot supply a relative equivariance structure.

Work over Rhat=C[[t]], k=k0+t, with k0=-11/2; only its quotient Rhat/(t²) is needed to decide the first Bockstein. This is an explicitly introduced parameter completion for the proof attempt. The polynomial weight-zero K_R is finite free, so completion is faithfully flat and would preserve its elementary-divisor exponents. No completion of the state or ghost carrier in weight is introduced.

There is a natural proposed parameter comparison. Form the universal affine vacuum V_Rhat from its PBW lattice, its quantum DS functor q_Rhat with the ordinary ghost differential, and X_Rhat=Av_!^(I1,psi)(V_Rhat). The unipotent averaging groups and their character do not depend on the level. If the continuous averaging and Whittaker constructions are made over this base, their unit gives

    A_Rhat=RHom(V_Rhat,V_Rhat) -> RHom(V_Rhat,X_Rhat).

The averaging adjunction identifies the latter with End(X_Rhat). Applying q gives a natural map End(X_Rhat)->End(qX_Rhat). The canonical comparison Av_!->Av_*[2 Delta], Delta=10, is an isomorphism on the spherical vacuum at t=0. Its proposed formal lift, together with q Av_*=q on the indicated H-equivariant inputs, would identify qX_Rhat with qV_Rhat[20], and then with W_Rhat[20] by the universal vacuum DS quasi-isomorphism. Endomorphisms ignore this common shift. Notice that q applied to the *unit* V->X is not the required vacuum equivalence; replacing the canonical !/* comparison by that unit is incorrect because of the shift.

The precise fixed-level inputs are w-bulk/PROOF.md:638–719, using Raskin, *W-algebras and Whittaker categories*, Theorem 5.1.1, Theorem 2.7.1 and Remark 2.7.3; and the vacuum DS quasi-isomorphism cited there to Arakawa, Theorems 4.8.5 and 4.11.1. These are adopted at their stated fixed-level scope. The proposed maps are specified here to make the extension question testable rather than to promote those inputs automatically to a family theorem.

There is a useful exact lifting principle. If an Rhat-linear exact functor and a natural comparison map have already been constructed on derived t-complete objects, and their formation commutes with derived reduction, a comparison which is an equivalence modulo t is an equivalence. Indeed its cone is derived complete; its reduction is zero, hence all successive reductions are zero by the triangles for the powers of t, and the derived inverse limit is zero. On finite free complexes this is also elementary elimination over the local ring. This principle does **not** construct the functor, the comparison, or its base-change coherence. It cannot justify an unconstructed parameter-dependent adjoint by itself.

Assuming those constructions, the relative version of the fixed-level coefficient object would be the object C_S,Rhat representing

    F |-> RHom(V_Rhat, F * V_Rhat)

on a finite Schubert variety S containing the orbit closure in the fixed-level proof. The opposite level twist is essential. Categorical Verdier duality, locally implemented by Spencer resolutions, suggests its construction in the category of relative (-k)-twisted differential modules. The !-fibre at t^lambda must be the actual N_Rhat of §6, compatibly with reduction modulo t². The canonical trivialization of the determinant line on N1^- then removes the twist on that open atlas, so its parameter Bockstein is a morphism of ordinary differential-module complexes there. The clean averaging pairing would give the comparison cone T_Rhat as the de Rham pairing of e^psi with the restriction away from the basepoint.

The missing check in this attempt is **not** a scalar rank or the ordinary derived Nakayama principle. It is construction of this coefficient object and averaging comparison over the varying TDO, with the same equivariance and base-change maps on the kernel and its !-fibres. The fixed-level proof in w-bulk Proposition 10.1 uses categorical duality and compactness. It does not write these relative data. A family of pointwise equivalences is insufficient, and an arbitrary lift of the finite two-row complex would beg the question about its derivative. This section therefore keeps the parameter comparison outside the stable core.

### A conditional discriminating calculation, including its exact hypothesis

Suppose the following concrete infinitesimal comparison has been constructed: an Rhat/(t²)-linear coefficient object with its actual orbit filtration and canonical map from the affine vacuum, whose underlying comparison with K_Rhat/(t²) is an equivalence; whose !-fibres are the spectral-flow CE families; and whose Bockstein, after the canonical determinant trivialization on N1^-, induces on the fixed-level hypercohomology spectral sequence the coefficient map of §6. This last compatibility includes the opposite-twist line. Under these hypotheses the common W4 exponent at tau=-3/2 is one.

To prove the implication, use the actual fixed-level geometric rows m=3,5 and fibre degrees q=17,...,22. The class of T8 occupies (m,q)=(3,17). The coefficient Bockstein maps it to 2 h3(x-z) in (3,18). The only possible geometric differential on that row is contraction by Zx+Zz. It annihilates x-z, and there is no incoming row of geometric degree one. Hence this target survives and is the nonzero T9 class. There are no further geometric rows that could kill it. The leading term of the Bockstein therefore gives a nonzero T8->T9 map. This conclusion uses functoriality of the specified filtered comparison, not merely the vanishing of a fixed-level characteristic class.

At the special fibre the adopted cone triangle A->K->T has K8->T8 surjective and K9->T9 an isomorphism: A9=0 and the connecting map T9->A10 is zero, as in §2. Naturality now makes the first Bockstein K8->K9 nonzero. Section 1 gives a=1, and §2 then gives b=1. This proves the conditional implication completely; it does not assert that its relative-comparison hypothesis has been proved.

The calculation is useful because it isolates the first place at which a parameter comparison can fail: it must either carry this nonzero coefficient derivative to the cone, or exhibit the precise varying-twist/descent correction which changes its image. A fixed-level cancellation of the scalar stabilizer character is not such a calculation. Until that choice is decided in the actual coefficient model, the W4 exponent remains open.

## 8. Corrections after the independent check

Throughout the general DVR lemma in §1, write κ=R/(t), replace dim H^q(K/t) by dim_κ H^q(K/tK), and replace the displayed dim_C H^q(K/t^m) by length_R H^q(K/t^mK). Then

length_R H^q(K/t^mK)=m r_q+Σ_(s∈T_q)min(m,s)+Σ_(s∈T_(q+1))min(m,s).

Smith splitting proves this because the kernel and cokernel of t^s on R/t^m both have length min(m,s). Independently the universal-coefficient exact sequence gives the same two summands. For the actual W4 DVR, residue field C, these lengths equal the stated C-dimensions; its numerical conclusions are unchanged.

The last transport sentence in §2 requires a multiplication-side correction. Reciprocal Feigin–Frenkel duality preserves multiplication, so the two nonzero left actions established at τ=−3/2 transport to τ=−2/3. Complementary duality τ↦−τ is a graded anti-isomorphism (w-bulk Proposition 4.4), so it transports them to nonzero right actions at the positive levels. Centrality of the additional classes u,v has not been proved. At each fibre choose the side supplied by these maps, and define M(z)=αz for a left action, or M(z)=(-1)^(3|z|)zα for a right action, where α is a closed family lift of η3. In both cases dM=−Md and β_s M=−Mβ_s. The two nonzero products become M(u)=x and M(v)=y. The smaller-page argument in §2 applies unchanged and proves a=b separately at every level. The independent cyclic-module proof also applies to M: nonzero reduction of R/t^a→R/t^b forces b≤a, while nonzero action on the t-torsion kernels forces a≤b. Thus equality survives; the stronger same-left-action assertion at all four levels is withdrawn.

This repair uses the family endomorphism dg algebra of w-bulk Lemma 9.5(a),(b), restricted to internal weight zero. Its torsion-free augmentation cone is acyclic and stays acyclic modulo t by the multiplication-by-t short exact sequence. Hence specialization-compatible composition supplies the same Bockstein exact couple as the actual K_R. Lemma 9.5(c)’s classical hbar-page identifications are not exceptional-level inputs.

The current retained computation status before the new-prefix continuation is: the original run completed D0–D4; its later continuation completed the degree-six resolution lift and D5; the degree-seven lift remains partial. Neither D8 nor D11 has been computed. D5 has source×target dimensions 5690×12184, 1,705,769 stored entries, and 1,704,834 entries with nonzero parameter derivative. The historical D5 continuation took 1504.5405 seconds and 2,348,040,192 bytes peak RSS; the audit’s 181.1352-second rebuild is a separate run. The original D0–D4 run remains the historical 969.574-second, 2,415,820,800-byte run. The constant-term comparison used scalar runs of the same PBW engine, while the oscillator/Miura/Virasoro checks are separately implemented controls. All-source adjacent-product checks strengthen the earlier samples but are finite-field composition checks, not missing detecting ranks.

For §7, the algebraic vacuum DS step is available over an integral parameter domain. ACL, W-algebras as coset vertex algebras, §5, equations (22),(23) and the following base-change paragraph, gives H_DS^i(V_T)=0 for i≠0, a free W_T, and base change. Take T=C[[t]], K↦−11/2+t. The free BRST complex C_T has the exact sequence 0→C_T --t²→ C_T→C_T/t²→0; freeness of H^0 and vanishing in other degrees give H^i(C_T/t²)=0 for i≠0 and H^0(C_T/t²)=W_T/t²W_T. Equivalently tensor the free degree-zero cohomology with the two-term free resolution of T/(t²). This does not apply the integral-domain hypothesis directly to the dual numbers. The remaining geometric requirements are relative averaging, its adjunction and clean comparison, full faithfulness on X, and the opposite-TDO coefficient object with its attachment and reduction maps. Identifying qX with W[20] alone does not prove End(X)→End(qX) is an equivalence. No unconditional a=b=1 assertion follows.

## 9. Reciprocal levels have the same local elementary divisors

**Theorem.** For the actual universal principal sl4 vacuum family at nonzero shifted level τ0, the multisets of torsion exponents in every cohomological degree agree at τ0 and τ0^−1. In particular, after the side repair of §8, there are two positive integers m_+,m_- such that a=b=m_+ at τ=3/2,2/3 and a=b=m_- at τ=−3/2,−2/3. No equality m_+=m_- is asserted.

**Proof.** Put R0=C[τ]_(τ−τ0), F=C(τ), and regard the dual family as the R0-family with shifted level τ^L=τ^−1. Both τ and τ^−1 are units in R0. For sl4 the Feigin–Frenkel Heisenberg isomorphism is

Φ: π_τ→π_(τ^−1),     b_i↦−τ b_i^L.

It is defined and invertible over R0: its λ-bracket is τ²·τ^−1(α_i,α_j)λ=τ(α_i,α_j)λ; its inverse sends b_i^L to −τ^−1b_i. Over F it identifies the two generic Miura W subalgebras by Feigin–Frenkel duality.

Each Miura image is saturated in its Heisenberg R0-lattice. Precisely, ACL Lemma 5.1 and its proof from equation (25) give

Υ(W_R0)=Υ(W_F)∩π_R0,

for either structure map C[K]→R0. The associated graded image is C[J∞(h*/W)]⊗R0, so the intersection statement applies to this actual local ring. Therefore

Φ(Υ(W_R0))=Φ(Υ(W_F)∩π_R0)=Υ(W_F^L)∩π_R0^L=Υ(W_R0^L).

This is an R0-linear vertex-algebra isomorphism of the two actual families, including their vacua and translation. It is stronger than a collection of fibre isomorphisms. The alternative lattice proof is to take an element of the generic image lying in π_R0, lift its leading symbol through the parameter-independent graded Miura image, subtract, and repeat in the finite PBW filtration; this reconstructs its coefficients in W_R0 without any parameter pole.

A vertex-algebra isomorphism gives an exact R0-linear equivalence of all weak/smooth module categories by transport of action, and sends the universal vacuum to the universal vacuum. It therefore identifies their R0-derived vacuum endomorphism complexes. The polynomial pro-resolution of w-bulk Proposition 3.4 and Lemma 9.5 computes these complexes, with the internal-weight-zero restriction of Proposition 3.2; hence the two finite complexes K have isomorphic R0-cohomology. This argument does not require compatibility of the canonical affine DS maps at reciprocal levels.

Finally write s=τ^L−τ0^−1 and t=τ−τ0. Under the local-ring isomorphism induced by reciprocity,

s=−t/(τ0 τ).

The factor −1/(τ0τ) is a unit, so R/(s^n) becomes R0/(t^n), with the exponent unchanged. Alternatively, reciprocity has derivative −τ0^−2≠0 and is an isomorphism of the DVRs preserving normalized valuation. Thus all elementary-divisor exponents agree, in particular those in degrees 9 and 12. QED.

**Source precision.** Primary local text: engine/prep/opus-prep/literature-sources/1801.03822.txt:971–1027 (integral DS, base change, graded Miura image and Lemma 5.1),1137–1157 (generic Heisenberg map and saturation proof of Theorem 5.6). The specific ring named R in ACL Definition 2.4, lines441–443, allows poles at nonpositive rational shifted levels and cannot be specialized at τ=−3/2. The proof above applies Lemma 5.1 directly to the actual noncritical local DVR instead. Its input is the generic duality and local saturation, not an impermissible specialization of ACL’s globally named R. Internal source pins: w-bulk/PROOF.md:554–601,740–759,1541–1579.

**Independent checks.** The bracket rescaling and the displayed uniformizer identity derive the two normalizations directly; the saturated-intersection argument and leading-symbol induction independently verify preservation of the local lattice. This does not transport exponents under complementary duality, for which only a fixed-level category anti-equivalence has been supplied. This is a new consequence assembled from published Miura saturation and the adopted polynomial vacuum model, not a new Feigin–Frenkel duality theorem.

## 10. Relative vacuum comparison, including torsion coefficient modules

**Theorem (relative vacuum comparison and family product).** Let R=C[τ]_(τ−τ0), τ0≠0, and let V_R be the universal principal W vacuum with the polynomial PBW pro-resolution of w-bulk Proposition 3.4. Let S_R(V_R) be the abelian category of all smooth weak V_R-modules on arbitrary R-modules, with R-linear morphisms. Then H^q(C_R(M))=Ext^q_(S_R(V_R))(V_R,M), naturally for every M. For M=V_R, the bounded finite free complex K_R=C_R(V_R)_0 computes these groups. The composition model E_R of w-bulk Lemma 9.5 represents their Yoneda product, and its augmentation comparison to C_R(V_R), including its internal-weight-zero part, remains a quasi-isomorphism modulo every t^n. Consequently the products used in §§2,8 and the integral Ext comparison used in §9 are justified in this full module category.

**Proof.** The PBW modules W_N^β and the complexes P^β are R-free. The straightening, representability and finite-support arguments of w-bulk §§2.1–2.4 use only the module relations and the displayed PBW bases; they therefore apply to an arbitrary coefficient module M, even when M has R-torsion. For instance, the proof of Lemma 2.3(c) uses the cyclic submodule generated by (m,1_γ) in M⊕π_γ: projection sends its spanning ordered monomials to an R-basis of W_γ, so the projection is an isomorphism without requiring M to be free. The polynomial construction of Proposition 3.4 is an exact augmented resolution over R: its associated graded is the truncated Koszul complex, whose Euler homotopies divide only by nonzero integers, and exhaustive bounded-below PBW filtration lifts exactness.

For any injective R-module J define I_R(J)=colim_(β,N) Hom_R(W_N^β,J), with xφ=φρ_x. The same finite-support relations as in Lemma 2.5 make this a smooth weak module. Evaluation at 1 gives

    Hom_(S_R)(M,I_R(J)) ≅ Hom_R(U M,J).

The inverse sends f to m↦[a1_γ↦f(am)], using any cutoff containing m. The forgetful functor U is exact, so I_R(J) is injective. An embedding U M→J adjoints to an embedding M→I_R(J), since evaluation at 1 recovers it. Thus S_R has enough injectives. By adjunction C_β(I_R(J))=Hom_R(P^β,J), acyclic in positive degrees by exactness of P^β and injectivity of J. Exact filtered colimits give H^{>0}(C_R(I_R(J)))=0. Each C_R^q(M) is a direct sum of copies of M, so C_R is exact; H^0(C_R(M))=Hom(V_R,M). Effaceability proves the asserted universal delta-functor comparison.

Every internal-weight complex of C_R(V_R) is bounded finite free by the counting proof of Lemma 3.1. Since τ0≠0, the regular factor s(k) is a unit in R and L_0=s(k)^−1 W^1_0 exists. The endomorphism L_0−DD of the pro-resolution induces zero on V_R. Its induced natural transformation of the universal delta functor is therefore zero in all degrees, while on internal weight w it is multiplication by w. Every nonzero integer is invertible in R; all nonzero weights are acyclic. Algebraic state sums and finite-support cochains make C_R(V_R) the direct sum of these weight complexes, so its cohomology is H^*(K_R).

Finally E_R=End_Pro(P_.) is the torsion-free dg algebra of Lemma 9.5. Its proof uses exact direct sums, products, a degreewise surjective inverse tower, and the just-established injective comparison; these operations apply over R. Thus E_R→C_R(V_R) is a quasi-isomorphism and composition induces Yoneda multiplication. Its cone Q is degreewise torsion-free and acyclic. For n≥1, the sequence

    0 → Q --t^n→ Q → Q/t^nQ → 0

is exact, so Q/t^nQ is acyclic. Reduction of E_R commutes with its sums and products and with the inverse tower: apply the inverse-limit exact sequence to 0→X_β --t^n→X_β→X_β/t^n→0, using surjectivity of the X tower. Hence E_R/t^nE_R is the same composition model formed from the reduced resolution. Weight-preserving construction gives the same statement on weight zero. These are chain-level specialization statements; no claim that H^*(K_R) itself commutes with specialization is made. QED.

**Source and verification scope.** This supplies the explicit base-ring argument requested in CHECK-1113-1824, S05/S27. It extends a stated internal PID theorem, rather than constructing a relative Whittaker or geometric averaging theorem. The owner opened w-bulk/PROOF.md:300–340 (arbitrary-module representability),351–407 (truncated modules/coinduction),421–479,590–597 (integral exactness),483–494 (effaceability),515–550 (weight reduction),554–583 (regular conformal factor),1541–1579 (composition/reduction). The independent check’s `reciprocal/internal_model.md` gives the same repair by relative injectives. As a second route for weight reduction, each nonzero-weight finite free complex has acyclic residue fibre; its universal-coefficient sequence and Nakayama imply zero integral cohomology. Neither route computes m_+ or m_-.

## 11. The polynomial three-ghost complex computes smooth W4 vacuum Ext

**Theorem.** Let A=C[α]. Let V_A be the universal Miura W4 family with generators U_2,U_3,U_4, and let B_A⊂B_A^circ be the polynomial curved ghost family of S, `ramified-parameter-descent.tex`, Lemma `rpd:lem:polynomial`. Its three generators γ_s are odd of cohomological degree 1 and weight 1−s, s=2,3,4; B_A^circ additionally contains S. Put d_B=S_(0)|B and e=1⊗S+Σ_s U_s⊗γ_s. For every ordinary smooth weak V_A-module M on an arbitrary A-module, set

    C_Q^q(M)=M⊗_A B_A^q,
    Q(m⊗b)=m⊗d_B b+Σ_(s=2)^4 Σ_(j∈Z) (U_s)_(j)m⊗(γ_s)_(-1-j)b.

All states and sums are algebraic. Then Q is defined, Q²=0, and H^q(C_Q(M))≅Ext^q_(S_A(V_A))(V_A,M), naturally as universal delta functors. The assertion persists under localization of A and reduction modulo a power of α−α0. For M=V_A, internal weight zero is a bounded finite free complex computing the full self-Ext. Its cochain ranks are the same as the polynomial vacuum complex already used in this item. This theorem identifies the groups and parameter torsion; it does not identify its vertex (−1)-product with Yoneda multiplication or assert a geometric bar comparison. S is an operator on B_A, not a fourth creation species in C_Q.

**Proof.** The polynomial family theorem supplies the ordered odd-jet PBW basis of B_A and all identities over A, including e_(n)e=0 for n≥0. The tensor product M⊗B_A^circ is a module for V_A⊗B_A^circ. Its module commutator identity therefore gives 2e_(0)^2=(e_(0)e)_(0)=0 on this module. The submodule of states M⊗B_A is stable under e_(0), since S_(0)B_A⊂B_A and every γ_s mode preserves B_A. Thus Q²=0 on every smooth M, including A-torsion modules. In the displayed sum, j≫0 gives zero by smoothness of M, while j≪0 gives zero because the corresponding γ_s mode has sufficiently large nonnegative index on the fixed state b. The ghost-only term is finite by the polynomial PBW construction. Hence no state or ghost completion is used.

Identify the odd creation pair (s,p), p≥1, with the annihilation letter U^s_n, n=p−s, in the convention (U_s)_(j)=U^s_(j+1−s). Its weight is n. An ordered ghost word ω is thus exactly a finite subset of annihilation letters. Write degω=Σn and Δω=Σs. Consequently C_Q^q(M) is, as a module, the finite-support cochain functor C^q(M) of w-bulk Theorem A.

We verify the filtration property needed to identify its differential, rather than infer the Ext comparison from square-zero alone. Give γ_s the auxiliary filtration δ_s=9−2s and S filtration 9, with translation of filtration 0. The dual relation table has every nontrivial correction of gap m=k+l−i−j≥2, so each such correction lowers δ by 2m≥4. In degree q, δ(ω)=9q−2Δω. It follows, for every mode and every PBW input b, that each ghost word ω occurring in (γ_s)_(r)b satisfies Δω≥Δb+s. Equality is possible only for the ordinary exterior insertion from a negative creation mode; every singular-mode contraction or nontrivial normal-order correction has Δω≥Δb+s+2. Similarly, every word in S_(0)b has Δω≥Δb+2. These statements follow first for one generator from the displayed relation table and then for arbitrary words by the terminating commutator/iterate recursion: each correction lowers δ, while ordinary interchange only changes the odd sign.

Therefore every differential term sending input ghost ω′ to output ghost ω with matter-mode coefficient a satisfies

    deg a=degω−degω′,   Δ(a)+Δω′≤Δω,

where a is a single U-mode for the coupled terms and a=1 for the S_(0) term. Equality in the second relation occurs exactly in the Koszul terms. For tw_β=deg−βΔ this implies

    tw_β(a)≥tw_β(ω)−tw_β(ω′).

Use the represented cutoff cochains C_β^q(M)=Hom(P_q^β,M) from w-bulk §§2.4–2.8. A coefficient of ω′ has depth at most −tw_β(ω′). Applying a gives depth at most −tw_β(ω′)−tw_β(a)≤−tw_β(ω). If tw_β(ω)>0, this forces the coefficient to vanish. Hence Q preserves every C_β(M), including the vanished-generator boundary of the cutoff. Naturality and representability give compatible morphisms d_Q:P_(q+1)^β→P_q^β. Their squares vanish by Yoneda, since Q²=0 naturally for all M. On degree zero, S_(0)1=0 and creation gives Qm=Σ_(x∈B_+)xm c^x; thus d_Q augments to the vacuum in the usual way.

Filter P_q^β by standard matter PBW degree plus Δω. The verified inequality makes d_Q filtered. Its associated graded is precisely the ordinary truncated Koszul differential: the terms of equal filtration are the exterior insertions just identified, with the usual ordering signs. Lemma 2.6 of w-bulk proves this graded resolution exact in positive degrees and identifies its degree-zero quotient with the polynomial creation algebra. Its proof uses only the integer Euler homotopy, hence works over A. The filtration is exhaustive and bounded below. For a cycle, subtract a lift of a graded boundary with the same highest filtration degree; the residual has lower degree. Iteration terminates and proves the augmented P^β complex exact over A. This is a concrete pro-resolution supplied by Q, not a choice of recursive higher corrections.

Finally the relative coinduction argument of §10 applies to this exact pro-resolution. For an injective A-module J, C_β(I_A(J))=Hom_A(P^β,J) is acyclic in positive degrees. Filtered union is exact and exhausts C_Q(M), and every module embeds in such a coinduced injective. Since each C_Q^q is a direct sum of copies of M and H^0 is vacuum invariants, its cohomology is the universal delta functor Ext(V_A,−). The construction localizes. The augmented P^β complexes consist of free A-modules with free cycles (A is a PID), so their exact sequences split as A-modules and remain exact modulo every power of α−α0; alternatively the same associated-graded Euler proof works after that reduction. Relative coinduction over the quotient ring then gives the same result on all quotient-ring modules.

For M=V_A the weight-counting proof of w-bulk Lemma 3.1 applies verbatim to this identical PBW carrier, giving bounded finite free terms in each fixed internal weight. L=−U_2 exists over A and L_0 is the weight operator. On P^β, L_0 minus the degree operator is a natural module endomorphism commuting with d_Q and inducing zero on the vacuum. Universality of the preceding delta functor makes its action zero on all cohomology. On internal weight w it is scalar w; every nonzero integer is a unit in A. Hence all nonzero-weight complexes are acyclic and weight zero computes the full vacuum Ext. QED.

**Source scope.** Polynomial QLS family and all-state coupling are prior: S/manuscript/constructions/`w4-curved-dual.tex:238–303,305–425` and `ramified-parameter-descent.tex:73–114`. The owner opened the actual tables, PBW proof, scalar extension proof and complete coupling. The cutoff comparison mechanism is already proved for the paired W3 complex at E/inscribe/chain-w-bulk-v3/NOTE.tex:2252–2279. The assertion here is its application to the actual polynomial three-ghost W4 complex, with the S_(0) and singular ghost-mode inequalities checked above. No new general PBW or Koszul theorem is claimed. The numerical implementation in `scripts/coupled/` is a separate verification of these actual operations, not the recursively lifted differential in another name; equality of their matrices is not asserted.

## 12. Exact local parameter and generator comparison for the direct complex

**Lemma.** At any τ0 in {±3/2,±2/3}, the finite weight-zero complex of §11, in a local branch α²=(τ−1)²/τ, has the same local elementary-divisor exponents as the actual polynomial W4 vacuum complex. It can therefore replace the recursively lifted complex in the first-Bockstein test.

**Proof.** Adjoin a local square root u of τ, choosing u0²=τ0. Because τ0≠0, this is an étale extension and its completed local ring is C[[τ−τ0]]. Set a_i=b_i/u and α=(τ−1)/u. The raw Miura factor is (τ−1)T+b_i=u(αT+a_i). Comparing the four-factor operators, including their rightmost differential powers, gives raw U_s=u^s U_s(α). Hence the generators (g0,g1,g2) of the retained polynomial mode engine are

    g0=−τ U2,  g1=u³ U3,  g2=τ² U4.

These are invertible changes of the actual Miura lattices; no central-charge-only inference is used. Thus transport of module action identifies the two full smooth-module categories after this scalar extension. Section 10 and §11 identify the cohomology of both finite complexes with the same relative vacuum Ext.

Differentiating α²=τ+τ⁻¹−2 gives 2α dα/dτ=1−τ⁻². At the four levels, α² is respectively 1/6 or −25/6, and 1−τ⁻²≠0. Therefore α−α0 and τ−τ0 differ by a local unit. Equivalently, both parameter maps identify their completed local DVR with C[[t]], carrying uniformizers to unit multiples. Faithfully flat completion and these unit changes preserve every elementary-divisor exponent. At positive levels α0²=1/6; at negative levels α0²=−25/6. Consequently the same detecting first-jet thresholds apply to Q, with differentiation in either local parameter. QED.

Source normalization is checked directly in E/chains/w-bulk/REQUESTS/3-calc.d/sl4_miura_core.py:41–56 and the W22 source copied to `scripts/coupled/source-freeboson.py:34–42`; normalized stress is S/manuscript/constructions/w4-curved-dual.tex:79–83. Computationally, when using existing g-mode actions, insert coefficients −τ⁻¹, u⁻³, τ⁻² in the s=2,3,4 coupling respectively. This is an actual family comparison; it adds no assertion that either local exponent equals one.

## 13. A detecting first derivative from one constant-rank factorization

**Lemma.** Let D(t) be the actual direct weight-zero degree-eleven differential of §§11–12, written with source images as rows, over the completed local DVR at τ0∈{±3/2,±2/3}. Write D=A+tB+O(t²). Its adopted special and generic ranks are r=2657 and r+1=2658. Choose row and column sets I,J of size r such that P=A[I,J] is invertible. For i∉I and j∉J, put

    x_iᵀ=e_iᵀ−A[i,J]P⁻¹E_Iᵀ,
    y_j=e_j−E_JP⁻¹A[I,j].

Then x_iᵀA=0, Ay_j=0, and the determinant of D on the augmented rows I,i and columns J,j satisfies

    (d/dt)det D[I∪{i},J∪{j}]|_(t=0)=±det(P)·x_iᵀBy_j.

Thus one nonzero scalar x_iᵀBy_j proves b=1, and hence a=b=1 by §§2,8,10, without constructing any other differential or the doubled jet matrix.

**Proof.** Since rank A=r, the rows indexed by I span its row space and the columns indexed by J span its column space. Restriction to J, respectively I, gives the displayed null vectors. Put the augmented minor in block form [P(t),u(t);v(t),a(t)]. Its determinant is det P(t) times its Schur complement a(t)−v(t)P(t)⁻¹u(t). This complement vanishes at t=0. Differentiating it and using (P⁻¹)'=−P⁻¹P'P⁻¹ gives exactly x_iᵀBy_j. Smith reduction of the actual complex has one nonunit factor t^b in D11, by §1 and the adopted cohomology table. Every 2658-minor is therefore divisible by t^b, while the displayed nonzero derivative gives valuation one. This forces b=1. The independent jet proof puts A into diag(I_r,0); its remaining derivative block has entries x_iᵀBy_j, so a nonzero entry gives rank J11=2r+1=5315. QED.

**Finite-field certificate.** Work in the number field containing the chosen u0 with u0²=τ0. Choose a localization Λ of its ring of integers containing all actual matrix coefficients and their first derivatives, and a residue map Λ→F_q at which every denominator is a unit. If reduction of A has rank 2657, a reduced P has nonzero determinant, and a reduced x_iᵀBy_j is nonzero, the same augmented determinant has nonzero derivative in characteristic zero. Its constant value is zero there by the adopted characteristic-zero rank. Therefore this is a sufficient exact certificate for the actual family. A modular kernel vector without the constant-rank check is insufficient, and a zero reduced pairing proves no higher torsion order.

**Efficient extraction.** For a free column j compute y_j as above, w=By_j, and ρ=w−A[:,J]P⁻¹w[I]. Then ρ_i=x_iᵀBy_j. This requires one factorization of P, two solves, and a sparse multiplication by B. One may first use a linear combination of free columns; a nonzero result guarantees that at least one constituent column detects. Retain the pivot indices, the chosen i,j, the constant determinant certificate and the derivative scalar, together with the source/basis hashes. The test uses only D11 because the Smith factor ending in H12 is already determined to be its unique nonunit factor; no separate choice of an H11 representative or a D12 cocycle is needed.

A subset of actual source rows suffices for a positive certificate: if it contains the indicated pivot minor and augmented detecting minor, these are minors of the full differential. Missing rows cannot erase their nonzero derivative. A partial matrix with a lower rank or a zero pairing supplies no negative conclusion.

Source scope: actual complex/cutoff identification is §§11–12, audited against S `rpd:lem:polynomial`, `w4d:tab:E`/mode-rule, and w-bulk §§2.3–2.8. Ranks and the one-factor location are CHECK-1113-1824 S02/S28. The Schur computation is elementary and independent of any geometric comparison. This is a certificate criterion; it does not itself compute either exponent.

## 14. A polynomial shifted-level model with no square root in its arithmetic

Put ε_0=ε_3=ε_4=1 and ε_2=−1. Write E_ij^{kl}(α)=Σ_r c_r α^r for a row of Table E, and m=k+l−i−j. Every occurring r satisfies 0≤r≤m and r≡m (mod 2), by direct inspection of that finite table. Define

    Ê_ij^{kl}(τ)=(ε_kε_l/(ε_iε_j)) Σ_r c_r (τ−1)^r τ^((m−r)/2).

These coefficients belong to Q[τ]. Use precisely the same mode rule and odd PBW ordering as in §11 with Ê in place of E, naming the generators δ_0=S,δ_2,δ_3,δ_4. Couple them to the retained raw matter generators g_0,g_1,g_2 by

    Q_τ=S_(0)+Σ_(s=2)^4 Σ_j (g_(s−2))_(j)⊗(δ_s)_(-1−j),

where j is the vertex-mode index. This is the actual vacuum Ext complex over C[τ,τ⁻¹] and its local noncritical coefficient rings, with no square root needed in its matrices. In particular the same finite-field prime can be used at either sign of τ0 whenever the ordinary rational denominators are units.

**Proof.** In the faithfully flat étale extension adjoining u with u²=τ, put a_s=ε_s u^s and a_0=1. Section 12 gives g_(s−2)=a_sU_s. Set δ_s=a_s⁻¹γ_s and δ_0=S. Rescaling the two sides of the dual mode rule multiplies E_ij^{kl} by a_ka_l/(a_ia_j). Since α=(τ−1)/u, its monomial c_rα^r becomes exactly the displayed polynomial Ê. Translation differentiates only the curve coordinate, so it commutes with this scalar change. The coupling is preserved term by term: g_(s−2)δ_s=U_sγ_s. Thus the rescaled relations, all-state Q²=0, and PBW basis are those of the actual coupled family after the étale extension. Faithful flatness descends these identities and basis statements. Alternatively, the finite mode recursion has the same strictly decreasing ghost filtration and polynomial coefficients, so its free PBW lattice inherits the generic identities directly. The cutoff/Koszul/coinduction proof of §11 then applies over the shifted-level ring itself; g_0/τ is the conformal vector. This gives full relative Ext and the finite weight-zero self-Ext model. QED.

For exact comparison with the retained α-normalized matrices, let Δ(g)=Σ_(s,p∈g)s and n_2(g)=#{(2,p)∈g}. Its raw ghost PBW word is F_g times the old word, with F_g=(−1)^(n_2(g))u^(−Δ(g)). In the row-image convention,

    D_τ[i,j]=F_(g_i) D_α[i,j] F_(g_j)^−1.

The identity holds over dual numbers, including the derivatives of F. It supplies an independent normalization check on retained rows; specializing only F at τ0 would omit genuine derivative terms.

Source pins: S `w4-curved-dual.tex:230–277` (complete Table E), :299–374 (mode rule/PBW), `rpd:lem:polynomial` and `rpd:lem:symmetry`; actual matter scaling sources in §12. The inverse-transpose transport for constant linear changes is already known; the explicit τ-polynomial coefficients are a normalization of that construction, not a new duality theorem.
