# Real-root embeddings used at rational and critical affine levels

Source-integrity supplement to UR-11 and UR-14, 18 November 2026. The underlying dossier is bound by SHA-256 28301884246d5b8458766dede3a74d5c13315a467a2297d5ea3bbff1aa70c3f7. This supplement gives a proof for each real-root step in its specified ordinary Verma modules. It also presents a direct check of the existential conclusion at the critical level.

## 1. Citation and required assertion

Kübel, §4, Theorem 4.1, records the ordinary Verma composition-multiplicity criterion. The subsequent Remark 4.2 states an embedding equivalence and attributes it to Rocha-Caridi and Wallach, Theorem 15. The independent source check flagged the dominant-integral hypothesis in that cited Theorem 15. A composition factor alone does not construct the maps used in the native tensor words. For UR-11 and UR-14 the required assertion is the existence of an injection after **one** downward reflection in a positive real root. We give the direct proof below. It covers the literal sequence of highest weights in the frozen dossier, including intersections of integral hyperplanes and the critical level.

## 2. The singular-vector condition is closed on a real-root hyperplane

Work with the extended untwisted affine algebra of a finite-dimensional simple complex \(\mathfrak g\), its full Cartan \(\widehat{\mathfrak h}\), and its standard positive Borel. Write \(\widehat\rho\) for a Weyl vector, with value \(h^\vee\) on the canonical central \(K\). Normalize long finite roots to square two. Let \(\beta=\alpha+n\delta\) be any positive real affine root and \(q\) a positive integer.

**Lemma.** Every complex highest weight \(\xi\) satisfying \(\langle\xi+\widehat\rho,\beta^\vee\rangle=q\) has an injective homomorphism of ordinary affine Verma modules
\[
 M(s_\beta\mathbin{\cdot}\xi)=M(\xi-q\beta)\longrightarrow M(\xi).
\]
The homomorphism preserves the full Cartan action, including the degree derivation and central scalar. The lemma asserts existence only.

**Proof.** Set \(\mu=(\xi+\widehat\rho)|_{\mathfrak h}\) and \(s=\langle\xi+\widehat\rho,K\rangle\). In the basic normalization,
\[
 \beta^\vee=\alpha^\vee+\frac{2n}{(\alpha,\alpha)}K,\qquad
 \langle\xi+\widehat\rho,\beta^\vee\rangle
       =\frac{2((\mu,\alpha)+ns)}{(\alpha,\alpha)} .
 \tag{1}
\]
In particular the hyperplane
\[
 {\cal H}_{\beta,q}=\{\xi:\langle\xi+\widehat\rho,\beta^\vee\rangle=q\}
\]
is a complex affine space. We allow the central scalar to vary **within this hyperplane** during the proof. The \(d\)-coordinate may be fixed throughout since (1) is independent of it. Equation (1) includes short roots, for which the coefficient of \(K\) has the root-length denominator shown.

For a nonnegative element \(\nu\) of the positive affine root lattice let \(P_\nu=U(\widehat{\mathfrak n}_-)_{-\nu}\). Take \(P_\nu=0\) when \(\nu\) is outside that nonnegative cone. The PBW isomorphism identifies \(P_\nu\) with \(M(\xi)_{\xi-\nu}\), for each \(\xi\), by multiplication on its highest vector. These are vector spaces independent of \(\xi\). At fixed affine height there are only finitely many positive affine roots of smaller or equal height; their multiplicities are finite, and the exponents in a PBW word of the given weight are bounded by its height. Thus all these spaces are finite dimensional. The space \(P_{q\beta}\) has positive dimension, since the \(q\)-th power of a nonzero negative \(\beta\)-root vector has a nonzero PBW symbol.

For the finitely many simple positive Chevalley generators \(e_i\), form
\[
 A(\xi):P_{q\beta}\longrightarrow
          \bigoplus_i P_{q\beta-\widehat\alpha_i},\qquad
 u\longmapsto (e_i u\,v_\xi)_i
 \tag{2}
\]
using the preceding fixed PBW identifications in the codomain. Its matrix has polynomial entries in affine Cartan coordinates. In fact in each finite word commute \(e_i\) past the factors, put the result in triangular PBW order, kill the positive factors on \(v_\xi\), and evaluate the resulting Cartan polynomials at \(\xi\). All commutators and basis changes have constant coefficients. There is no division by a parameter and there are no infinite series in this calculation. Since the \(e_i\) generate the positive nilpotent Lie subalgebra, the singular vectors of this weight are exactly \(\ker A(\xi)\).

Write \(m=\dim P_{q\beta}>0\). A nonzero kernel of (2) is equivalent to the vanishing of all \(m\)-by-\(m\) minors, with this condition automatic if the target has fewer than \(m\) rows. It gives a Zariski-closed subset \(Z\) of \({\cal H}_{\beta,q}\). Only the existence of a vector can pass to specialization by this argument. A normalized explicit vector or one-dimensionality of its span need not do so.

Remove from \({\cal H}_{\beta,q}\) the critical hyperplane \(s=0\) and all sets
\[
 \{\xi:\langle\xi+\widehat\rho,\zeta^\vee\rangle=j\},
 \qquad \zeta \text{ real},\quad \zeta\ne\pm\beta,\quad j\in\mathbb Z .
 \tag{3}
\]
Each intersection in (3) is empty or is a proper affine hyperplane inside \({\cal H}_{\beta,q}\). In the untwisted reduced root system, distinct coroot directions proportional to \(\beta^\vee\) can arise only from \(\pm\beta\). Explicitly, proportional finite coroot parts force the finite roots to be \(\pm\alpha\) and (1) then forces the corresponding modes to be \(\pm n\). The \(s=0\) intersection is proper as well, since \(\alpha^\vee\) has nonzero horizontal part. There are only countably many removals. Their complement is dense in the usual complex topology by the Baire theorem, hence Zariski dense in the hyperplane. This density is applied in the space where horizontal weight and central scalar vary, including when the desired terminal point has central shift zero.

At a point of this complement the integral real roots are exactly \(\pm\beta\). Imaginary roots supply no critical relation since \(s\ne0\). The ordinary noncritical block therefore has the two distinct labels \(\xi,\ s_\beta\cdot\xi=\xi-q\beta\). This follows from Fiebig §2.3, the noncritical integral Weyl orbit description. It also follows directly from the equivalence relation there: the shifted integral pairings change by integers under this integral reflection, so no other real hyperplane can appear at the reflected weight. As \(\beta\) is positive and \(q>0\), \(\xi\) is the largest of its two labels in the ordinary positive-root ordering. Fiebig Theorem 3.10, applied specifically to this noncritical two-label block over \(\mathbb C\), gives a nonzero map \(M(\xi-q\beta)\to M(\xi)\). Its highest vector is a nonzero element of the kernel in (2). Thus \(Z\) contains the dense subset, which gives \(Z={\cal H}_{\beta,q}\).

At any specified \(\xi\) on the hyperplane, take a nonzero vector from that kernel. The universal Verma property gives a module homomorphism. It is injective: under PBW both Vermas are free of rank one on the left over \(U(\widehat{\mathfrak n}_-)\), and the map is right multiplication by the nonzero enveloping-algebra element giving the vector. The associated graded of this enveloping algebra is a symmetric algebra over \(\mathbb C\), hence an integral domain even for this infinite-dimensional Lie algebra. Its PBW filtration gives the same non-zero-divisor property before passing to the associated graded. This completes the proof. ∎

The frozen source of the block statement and the generic embedding used here is Peter Fiebig, *The combinatorics of category O for symmetrizable Kac–Moody algebras*, revised 2004, §2.3 and Theorem 3.10, especially text lines 260–305, 657–666 and 759–781 in /tmp/induction-full-realization-20261116/global_unit/noncritical_unit/sl3_nilpotence_upper_bound/affine_transition/sources/Fiebig-math0305378v2.txt. The citation whose breadth prompted this supplement is Johannes Kübel, *A Jantzen sum formula for restricted Verma modules over affine Kac–Moody algebras at the critical level*, 2014, §4, printed pp. 376–377, text lines 347–372 in /tmp/induction-full-realization-20261116/global_unit/noncritical_unit/sl3_nilpotence_upper_bound/affine_transition/sources/Kuebel-PJM-2014-269-2.txt. The proof above invokes Fiebig only away from critical level and only in the two-label block.

## 3. Exact application to the two original staircases

At rational \(s=a/b\) in lowest terms, \(b>0\), take the long positive root \(\alpha\) of square two from §6 of the dossier. For \(\beta_j=(-1)^{j-1}\alpha+b\delta\), the value at the weight before the \(j\)-th reflection is \(u+(2j-1)a\). This follows by alternating the two transformations \(x\mapsto-x-2a\) and \(x\mapsto-x+2a\) on \(x=(\mu,\alpha)\). Both \(\beta_j\) are positive in the ambient affine root system because \(b>0\).

In UR-11 choose \(u\) so these values are positive for the prescribed number of steps. The lemma gives each injection in exactly the direction used in the dossier. In UR-14 choose \(a\le0,\ u+a<0\); all the old pairings are negative. Their negatives are the new positive pairings after reflection. Applying the lemma at that new weight gives each injection from the old Verma to the new one. These assertions include \(a=0,b=1\) and singular intersections with other integral hyperplanes. A countable chain can choose one injection at each step; since each is genuinely injective, all finite composites are nonzero. Nothing in the construction requires simultaneous polynomial choices of singular vectors at the different steps.

Restricting those maps to their horizontal tops gives the same actual invariant cycles under native cochain evaluation. Native degree-zero multiplication, with the left factors ordered as in dossier §6, still evaluates to the affine composite. Thus this proof supplies the disputed external premise for the **original witnesses** of UR-11 and UR-14. It does not introduce a conclusion about the unrestricted rational native unit.

## 4. Direct critical control

At \(s=0\) there is also an elementary witness, using the vacuum \(M=W\otimes_R\mathbb C\) rather than the regular top. PBW identifies \(M=U(t^{-1}\mathfrak g[t^{-1}])v\). For dual bases of \(\kappa\), set
\[
 z=\sum_i (x_i)_{-1}(x^i)_{-1}v.
\]
The zero-mode action on \(z\) vanishes by invariance of the inverse metric. The mode-one action is
\[
 y_1z=\left(\sum_i [[y,x_i],x^i]+2\ell y\right)_{-1}v
      =2(h^\vee+\ell)y_{-1}v=0 .
\]
The final equality uses the critical raw level \(\ell=-h^\vee\); the adjoint Casimir acts by \(2h^\vee\) in this normalization. The mode-two action reduces to \(\ell\sum_i\kappa([y,x_i],x^i)v=\ell\operatorname{tr}(\operatorname{ad}y)v=0\); all zero and positive modes remaining to the right kill the vacuum. Modes greater than two vanish by energy. The leading PBW symbol of \(z\) is the nonzero inverse quadratic form on the mode \(-1\) variables. Hence the affine map \(v\mapsto z\) is right multiplication by a nonzero element in the negative-mode enveloping domain and has nonzero powers of every order.

This supplies the degree-zero injection \(\mathbb C\to B_2\otimes_R\mathbb C\) into native cycles. Repeating it on the induced sources \((B\otimes_R\mathbb C)\langle-2j\rangle\) gives zero transitions after \(R\)-base change and injective transitions after \(H\)-base change. Its telescope has the same lower cochain bound \(-1\) as the dossier, so UR-13 puts it in the original unit locus under the stated native assumptions. This second witness tests the critical existential consequence without affine Verma-embedding results. Its normalization can also be checked against the critical quadratic-generator calculation in /tmp/induction-full-realization-20261116/global_unit/unit_counterexample/PROOF.md, §2, especially lines 96–134.
