# Four frontier comparisons

17 November 2026

## Bulk fields with current corrections

Let \(R_3=\mathbb C[\hbar]/(\hbar^3)\) and let \(M_3=V^{KB}(\mathfrak{gl}_2)\otimes_{R_3}F_0\) be the native state complex, where \(F_0\) is the polarized ghost state module, the current factor is extended to \(R_3\), and the trace current and trace ghosts are retained. Its inputs here are finite algebraic PBW and exterior combinations. The ghost polarization is a left-module quotient. The two fields \(\mathbb Y_\pm\) take values in the pointwise complex
\[
\operatorname{Hom}_{R_3}(M_3\otimes M_3,M_3((u))).
\]
Their construction corrects the tensor product of the reversed current field and the ghost field by
\[
\mathbb Y_-=(\mu_-\otimes Y_{\rm gh})\circ
 e^{-\hbar s^{\ell J}(u+\hbar)},
\qquad \mathbb Y_+=\mathbb Y_-^{\rm op}.
\]
The kernel \(s^{\ell J}\) pairs the nonnegative coadjoint ghost modes on the inserted state with the nonnegative current modes on the rooted state. The shift by \(\hbar\) records their opposite multiplication order; the opposite field includes the sign \((-1)^{|X||Y|}\). Every coefficient is finite; on homogeneous inputs the order-\(\hbar^j\) Laurent floor is \(-\mathrm{wt}(X)-\mathrm{wt}(Y)-j\). Both vacuum laws and both translation laws hold at every numerical level \(K\).

Through \(R_3\),
\[
(M_3,d_M,\mathbb Y_-,T,\mathbf1,S_M)
\]
is a differential graded quantum vertex superalgebra with rational exchange at every numerical \(K\), including \(0\) and \(-2\). The two twist hexagons H1 and H2 reduce at second order, with their prescribed operator orders and shifted arguments, to the positive-jet classical Yang–Baxter equation. A common localized germ proves weak associativity on all algebraic triples; a separate locality argument gives one exponent \(N(X,Y)\) for every final state \(Z\). Pure-pair identities and filtered propagation of the order-\(\hbar^2\) differential defect prove the chain identity on all algebraic pairs. The proof retains the actual \(D_2+E_2\), corrected currents and full classical trace tensor factor with its Koszul sign. The direct all-mode current-column argument proves that column independently of bulk weak associativity.

The 285 current-column and 252 twist-hexagon coefficient controls corroborate these analytic arguments. The coefficient windows of the mixed-field calculations are not dg subcomplexes, and sampled three-input coefficients do not prove formal weak associativity. First-order classification concerns the four-parameter constant-coefficient current/ghost-kernel ansatz; finite second-order fits and failed exponential substitutions classify no unrestricted correction space.

With \(\delta\) the field differential, an explicit tensor operator \(\Lambda\) and cochain \(\mathbb H=\mathbb Y_-\Lambda\) satisfy
\[
[d_M^{\otimes},\Lambda]=S_M-1,
\qquad \mathbb Y_+=\mathbb Y_-S_M,
\qquad \delta\mathbb H=\mathbb Y_+-\mathbb Y_-.
\]
Thus \(S_M\) is a chain automorphism homotopic to the identity, and \(\mathbb H\) is a homotopy between the two chain fields on all algebraic pairs. The graded tensor calculation retains the minus term in \([d^\otimes,\iota^F\otimes L^F]\). The opposite \(\mathbb Y_+\) is weakly associative; the full quantum vertex axioms for its candidate exchange \(S_M^{-1}\) are not part of this theorem.

The scalar projection gives \(W_\pm\) at every level. Identification with \(E_3(e),\overline E_3(e)\) retains \(K\ne-2\), including \(K=0\), and
\(-\pi_{\rm cor}\mathbb H\equiv H_3(e)\pmod{\hbar^2}\) only. Two further exclusions have narrow domains. Ordinary current postcomposition is not a dg endpoint action: \([d_0,J_H(0)]\ne0\). The fixed curved ghost-output arrow is obstructed for \(K\ne0\); at \(K=0\), affine augmentation supplies a ghost-output chain map that discards the nonvacuum currents. Neither exclusion rules out a coherent physical comparison. Even unital chain fields on the full trace complex need not be homotopic: a trace-bilinear \(\hbar^2\)-correction can change the closed pair \(I_1\otimes I_1\) by \(\hbar^2\mathbf1\). This example changes the prescribed trace corner.

At \(K\ne-2\), the full marked evaluations \(E_3,\overline E_3\) and their endpoint-ordered homotopy are given. Their operation-preserving comparison with the native field remains open. It must respect the resolved source, both ordered endpoint actions, the inserted restriction, and the proper output-unit cone and corrected section. Defining the relative deformation problem requires compatible endpoint actions, the prescribed proper unit homotopy, translations and allowed corrections; the relative class and its exactness have not been established. Extending the scalar cell to the original coefficient source must preserve its nested cutoffs, outer word-length direct sum and pointwise Hom placement. At each right quotient, a whole Laurent series must have one middle ghost cutoff, one Laurent floor and finite right PBW support. The independent physical module categories, adjunction, units and counits, and product tensorator remain open; neither a transported algebraic field nor an unconstrained chain homotopy supplies them. The intrinsic theorem supplies no critical physical evaluation or extension beyond \(R_3\).

## Coefficient heat and the quartet map

On a smooth reflected Ward filling, with \(\partial=\partial_z\), the triangular change of currents
\[
u'=h-\frac\kappa2\partial e,
\qquad w=f+\frac\kappa2\partial h+\kappa Te
              -\frac{\kappa^2}{2}\partial^2e
\]
splits the absolute current complex into a constant quartet and the stress complex. It and its inverse are bounded on each reflected Sobolev scale with offsets \((2,1,0,2,0)\); uniform estimates require the corresponding higher seminorms of the filling. The coefficient heat operator is block triangular, so its weighted trace is independent of the filling \(T\) at fixed source \(\mu\). This independence concerns the trace, not finite action maps or their nonscalar moments.

For the original gapped square-zero heat family at numerical \(\kappa\ne0\), on its common reflected domain, let \(A=da_0+a_0d\), let \(P_F\) project to the \(F\)-current component, and put \(x=|\kappa|^2\). Duhamel differentiation and graded cyclicity give
\[
x\partial_xW^{\rm aff}_\epsilon
 =\operatorname{Str}_X(P_Fe^{-\epsilon A}),
\qquad
c_F:=\operatorname{FP}_{\epsilon\downarrow0}
\operatorname{Str}_X(P_Fe^{-\epsilon A})
 =\frac12R_2[JP_F],
\]
where \(J\) is the parity operator and \(R_2\) the reflected constant heat coefficient. Its normal-reflection factor \(1/2\) is already included in \(R_2\); the displayed factor comes from the positive reflection sector. Level conjugation scales \((\kappa,T)\) together. The variation formula uses decay at the upper time endpoint, and \(P_F\) need not commute with \(d\).

Integrating from \(x=0\) remains conditional. A common domain, uniform sectorial bounds and gap, twice differentiable inserted traces and large-time majorants are needed along \((\kappa_r,T_r)=r(\kappa_*,T_*)\). For \(G_\epsilon(r)=\operatorname{Str}_X(P_Fe^{-\epsilon A_r})\), evenness and the endpoint decomposition would then give \(G_\epsilon(r)=O(r^2)\), making \(G_\epsilon(\sqrt y)/y\) integrable. Passing a finite part through that integral additionally needs uniform short-time and source-derivative bounds. The zero quartet torsions use the vanishing Euler characteristics of the weight-zero and weight-one complexes, not acyclicity alone. This auxiliary zero-level endpoint constructs no physical affine Gaussian. Universal vanishing of \(c_F\) is also open: the special symbol calculations cover only their specified jets and coefficients, and charged densities can integrate to zero while remaining nonzero pointwise.

The physical cotangent map still contains the formal bilinear transpose and response shear,
\[
\mathcal M_\mu(a,\gamma)
 =(R_Ta,R_T^{-t}(\gamma-K_\mu a)).
\]
Bounded current transport does not prove its ordinary relative-domain, cycle or semidensity properties. On a meridian disk, \(\partial_zr=\bar z/(2r)\) is generally nonzero, so the Green flux retains a first normal jet. The required finite-cut pushforward from the cyclic map \(J_R\) and quartet integration \(I_{\mathcal Q}\),
\(\Pi_\epsilon=(\mathrm{id}\otimes I_{\mathcal Q,\epsilon})J_{R,\epsilon}\), its source/cut/scale square and its independently normalized cap remain unconstructed. A coefficient-heat response difference is not yet the transported physical quartet connection: its covariant response term has sign \(-d_UW\), opposite to the logarithmic response. Density, phase, finite subtractions and admissible corrections remain part of the comparison. Interaction moments and spatial sewing require additional maps; numerical nonzero \(\hbar\) cannot be substituted for the truncated formal \(\chi\) coefficient.

## The genuine Heisenberg action space

Work in the localization of ordinary algebraic dg vertex superalgebras at state quasi-isomorphisms. Let \(H=V_\kappa\), \(\kappa\ne0\), \(B=\Lambda(\epsilon)\) with \(|\epsilon|=1\) and \(d\epsilon=T\epsilon=0\), and \(X=B\otimes H\). The comparison \(q_B:N\operatorname{Act}_{\mathrm{roof},H}(B)\to\mathscr F_H(B)\) uses the full original actor-roof category, both legs and every admissible boundary arrow. Its target is
\[
\mathscr F_H(B)=\operatorname{hofib}_{\mathrm{id}_H}
 [\operatorname{Map}(X,H)\longrightarrow\operatorname{Map}(H,H)].
\]
The arrow is restriction along the canonical inclusion \(H\to X\). A connectivity theorem gives
\(\operatorname{Map}(A,C)\simeq\operatorname{Hom}_{\rm VA}(H^0A,Z^0C)_{\rm disc}\)
when \(H^{>0}(A)=0\) and \(C^{<0}=0\). Consequently the unit path in this target has contractible choices. The separate pointing path \(\eta\) of a sphere representative must still be retained through strictification and refinement.

The actual universal-tuple augmentation supplies
\[
\Pi:\mathscr F_H(B)\longrightarrow\mathbb C^2_{\rm disc}\times K(\mathbb C,1),
\qquad \Pi q_B\text{ is a weak equivalence}.
\]
Its component condition is \(F_{(0)}J=0\), equivalently \(F\in\mathbb CJ+\mathbb C1+TH\), rather than an arbitrary closed-pair coordinate. Convolution on full roof diagrams and an explicit scalar simplicial family identify the actual maps and their fibres. Writing \(\Theta=(\operatorname{ch}/\kappa,\operatorname{ct})\), \(\mathscr F^0=\Theta^{-1}(0)\), and \(\alpha_0\) for the trivial action, one obtains
\[
\mathscr F_H(B)\simeq\mathbb C^2_{\rm disc}\times\mathscr F^0,
\]
and the exact criterion
\[
q_B\text{ is an equivalence}\quad\Longleftrightarrow\quad
\pi_0\mathscr F^0=*,\quad
\ker\chi_{\alpha_0}=0,\quad
\pi_n(\mathscr F_H(B),\alpha_0)=0\ (n\ge2).
\]
Here \(\chi\) is the scalar loop detector. Translations preserve this particular detector and its scalar section. Abelian fundamental groups and trivial actions on higher groups are proved on the \(q_B\)-image components only. Over an image component, the actual \(q_B\)-fibre has component set \(\ker\chi\) and higher groups shifted by one; it is distinct from the connected scalar-detector fibre on one genuine component.

For the universal tuple stages \(S_{H,a}\), half-interpolation asks, cofinally, for actual maps \(Y\to X\) and \(Y\to S_{H,a}\) over \(X\), with the first a state quasi-isomorphism. It implies the full equivalence. Target-\(H\) tuple surjectivity supplies neither this condition nor the additional map \(S_{H,b}\to Y\) required by full exact interpolation. General tame incoming roofs need not be nonnegative, and their tame ideal need not be the ideal of all negative states.

For a pointed kernel triple \((S,p,D)\) representing a detector-kernel loop or a higher homotopy class, linearization becomes null. Equality with that linearization follows if a frame square lies in an actual acyclic dg ideal
\(\mathcal I'^2\subseteq\mathcal J\subseteq\ker p\cap\ker D\).
This covers the specified split square-zero roofs, charge-graded roofs generated in charges zero and one, the stated acyclic-module extensions, and the canonical-frame case. It concerns kernel loops and higher classes, not classification of arbitrary components. A generated-square or generated-cube version gives another sufficient nullity theorem. A primitive functional can vanish while no suitable acyclic enlargement exists for the chosen frame, even when the genuine class is zero. Its identification with the global nullity functional requires a kernel triple; identifying its domain on an ideal \(\mathcal J_0\) with product cycles requires \(\mathcal J_0\subseteq\mathcal I_S^2\). These methods are not equivalent necessary descriptions of every obstruction.

The loop formulation makes the positive-degree residual concrete. For \(X_b=H\oplus\epsilon_bH\), \(|\epsilon_b|=b\), it is equivalent to looping inducing equivalences
\[
\operatorname{Map}_{H//H}(X_0,X_b)
 \longrightarrow\operatorname{Map}_{H//H}(X_1,X_{b+1}),
\qquad b\ge0;
\]
the \(b=0\) case suffices. These are genuine section-preserving mapping fibres, not full faithfulness on arbitrary shifted pairs. The relative interval construction keeps the base path fixed; imposing equal endpoints on an arbitrary base path would add an unwanted \(H\,ds\). Finally, scaling \(\epsilon\mapsto t\epsilon\) gives a polynomial family, not a differential-form homotopy, since \(d(t\epsilon)=dt\,\epsilon\), and no weight decomposition or graded representative theorem is available. Connectivity of \(\mathscr F^0\), the detector kernel and its higher groups remain unresolved; no missing component or noncontractible actual fibre is exhibited.

## Nested currents and their completion domains

For \(\mathfrak g=\mathfrak{sl}_2\) and \(k\notin\mathbb Q\), assume the specified smooth affine–right-\(Y_k\) realization, its full unbounded tensor–Hom unit, common-cutoff cofree actions, native ideal triangle and bounded-below positive-current torsion theorem. The input \(T\) is an arbitrary ordinary unbounded dg left \(Y_k^{\otimes3}\)-module, including correlated inputs. With inner separation \(w\), outer separation \(z\), \(p=w^{-1}\), \(q=z^{-1}=sp\), put
\[
\mathcal O=\mathbb C[s]_{(s)},\quad
D=\mathcal O((p))[s^{-1}],\quad
K_R=\mathbb C(s)((p)),\quad K_N=\mathbb C((p))((s)).
\]
The coefficient complexes have carriers \(L_D(T)=(T\otimes\mathcal O)((p))[s^{-1}]\), \(L_R(T)=(T\otimes\mathbb C(s))((p))\) and \(L_N(T)=T((p))((s))\). For prescribed double-coefficient expansions and every vector space \(V\),
\[
(V\otimes\mathbb C(s))((p))\cap V((p))((s))
 =(V\otimes\mathcal O)((p))[s^{-1}].
\]
For \(\sum q^nf_n(s)\), the exact condition is \(\inf_n(n+\nu_s(f_n))>-\infty\). This gives algebraic gluing and completion formulas. Maximality concerns these expansions; no field map fixing \(p,s\) exists between the two fields, but abstract common overfields do exist. Compatible common forms are required for general field-defined inputs; some nonconstant tests have them.

The twist preserves quasi-isomorphisms by finite quotients and surjective towers. Its jointly completed intermediate module \(E=S_w^{12}(T)=T((p))\), with the pair differential, has an independently defined binary current recipient and an actual next operation \(S_z(E)=L_N(T)\). The comparisons retain the original unit and evaluation on the full ambient \(D_{\mathcal N}\) of smooth tests with jointly locally nilpotent positive-current cohomology. The ground-field bounded-recipient argument also gives the three-point current theorem over \(D\); it is not a nonfield representability theorem. The realizations form an enhanced derived span through the \(D\)-object. Full units extend over every commutative complex coefficient algebra, and every left comb has its stagewise binary recipient over successive Laurent fields.

For \(T=T_{12}\otimes M_3\), the separately factorized recipient uses \(E_1=S_w(T_{12})\otimes M_3\). Its comparison with \(E\) is an equivalence when \(H^\bullet(M_3)\) is finite-dimensional in total. For an inflated regular third factor it has the nonzero defect \(U((p))/(U\otimes\mathbb C((p)))\), with zero differential. Moreover, \(p^nv\) tends to zero in the declared source topology but has constant outer \(s\)-order: the map to the native outer Laurent topology is not continuous. A coarser coefficient topology is a different construction. Raw cones \(D\to K_R,K_N\) remain nonzero even for the trivial input; the cones that vanish for finite Wilson cohomology are those of the scalar-extended maps. Algebraic base change is not completion.

The full three-point evaluation over \(D\) and its completions exist. Agreement with binary iteration is established on the affine and common two-pole sources through an explicit incoming-bar refinement. The extra \(a_1\)-pole resolving generators still need a map and homotopies. Outgoing actions preserve \(L_D,L_R,L_N\), not all positive lattices. For the occupied input \(T=M_1\otimes\mathbb C_\varepsilon\otimes M_3\), a jet series \(\sum_{n\ge n_0}q^n\tau_n(t)\), with \(\tau_n\in T[t]\), lies in the common domain exactly when its antidiagonals \(A_P(s)=\sum_ns^n[t^{n-P}]\tau_n(t)\) are rational in \(s\), equivalently lie in \(s^{n_0}(T\otimes\mathcal O)\), and have one common lower \(p\)-bound. Finite normal jets are obtained as quotients. The substitution \(t=p^{-1}\) embeds no nilpotent jet ring. For the regular triple, there is no degree-zero cycle \(\xi\in\mathbf1+pL_A\), with lattice \(L_A=(T\otimes\mathcal O)[[p]]\): the weight-one obstruction is nonzero. This normalization is essential; congruence modulo \(p\) after inverting \(p\) is vacuous. Normalized covector deletion holds in slots one and two, the latter at separation \(z+w\). The third slot and the full occupied-deletion functor remain separate.

For finite-dimensional Wilson modules, let \(\Omega_{ij}\) denote the pairwise Casimir operators. The rational cycle and iterated cycle differ by the unique matrix gauge
\[
sG'=A(s)G-GA(0),\quad
A(s)=k^{-1}\bigl(\Omega_{13}/(1+s)+\Omega_{23}\bigr),\quad G(0)=1.
\]
The cycle maps include the actual resolution augmentations; the chosen resolution of a trivial module is nontrivial before augmentation. Nonresonance proves the all-orders recursion, and \(\Omega_{13}\ne0\) gives nonrationality by monodromy at \(s=-1\). With \(\Omega_{(12),3}=\Omega_{13}+\Omega_{23}\) and residue \(R=-\Omega_{(12),3}/k\), the recurrence is \(n+\operatorname{ad}_R\). After the singular-power and scale normalizations in \(x=w/(w+z)\), continuation on \(0<x<1\) with positive-real logarithms gives the ratio \(F_1^{-1}F_0\) of normalized endpoint solutions, the KZ associator with arguments \(-\Omega_{12}/k,-\Omega_{23}/k\); the raw gauge ratio is not this constant comparison. This controls finite-dimensional cohomology and cycles, not a continuous gauge on the entire intermediate complex.

Finite energy heads must first be extended from \(\mathcal O_0=\mathbb C[s,(1+s)^{-1}]\) to \(\mathcal O\) before claiming the latter limit. Their homogeneous lattice has energy index \(e\ge\max(\omega,0)\) at weight \(\omega\); failure of degreewise surjectivity requires infinitely many energies in one cohomological degree. These heads do not yet give the original integral collision diagrams. A native comparison still needs the factorized recipient, its topology, the full rational-current source, collision and unit maps, and polynomial parameter families with literal facets and interchanges. The first incomparable clusters \((12)(34)\) require more than a common field. Neither the finite Wilson gauge nor failure of the specified PBW collision carrier settles those remaining maps.
