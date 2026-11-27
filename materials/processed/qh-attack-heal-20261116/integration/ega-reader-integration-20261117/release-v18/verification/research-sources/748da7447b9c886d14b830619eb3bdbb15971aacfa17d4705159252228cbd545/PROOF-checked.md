# The bulk of a principal W-algebra

Notation. g is a simple complex Lie algebra of rank r, with exponents m_1 <= ... <= m_r, Coxeter data
d_i = m_i + 1 (the degrees of the basic invariants), dual Coxeter number h^v. For k in C, V = W^k(g) is the
universal principal W-algebra at level k (quantum Drinfeld-Sokolov reduction of the universal affine vertex
algebra V^k(g)); tau = k + h^v; the level is critical when tau = 0. S_k is the abelian category of all (weak)
V-modules: vector spaces M with fields Y_M(a, z), a in V, satisfying the Borcherds identities, with no
grading or finiteness condition ("smooth modules": Y_M(a, z)m is a Laurent series for every m). Ext is taken
in S_k. H^*(g) is the cohomology of g with trivial coefficients, the exterior algebra on primitive classes
theta_i of degrees 2 m_i + 1.

## 0. The theorem as it stands

THEOREM. Let g be simple and k in C.

(A) (comparison, every k, Section 2). There is an exact functor C from S_k to non-negatively graded
complexes, with C^q(M) = M (x) Lambda^q_cont(a_+^*) (finitely supported cochains on the set a_+ of modes of
the generators that kill the vacuum), with differential of the form D m = sum_x x m (x) c^x + ..., and a
unique isomorphism of cohomological delta-functors

    Ext^n_{S_k}(V, M) = H^n(C(M)),      M in S_k,

extending Hom(V, M) = {m : a_+ m = 0}. At non-critical levels, for g = sl_2 the complex C(M) is the Chevalley-Eilenberg complex
of the Lie algebra of vector fields on the formal disc; for g = sl_3 at non-critical levels it is quasi-isomorphic, naturally in M,
to the paired complex M (x) W^{k'}(sl_3) (x) (ghosts of weights 2 and 3) with the BRST differential of
Bouwknegt-McCarthy-Pilch, k' = -k - 6, compatibly with products (adopted, inscribe/fab-T96).

(B) (finiteness, every non-critical k, Section 3). Ext^n(V, V) is finite-dimensional, vanishes for n
larger than a bound depending only on g, and has Euler characteristic 0. It is the cohomology of the
weight-zero part of C(V), a complex of finite-dimensional spaces whose terms do not depend on k and whose
differential is polynomial in k.
Consequently dim Ext^n(V, V) is upper semicontinuous in k and takes its generic value outside a finite set
of levels.

(C) (irrational levels, Section 4; uses the affine Skryabin theorem of Raskin). If k is not a rational
number, quantum Drinfeld-Sokolov reduction induces an isomorphism of graded algebras

    H^*(g) = Ext^*_{affine}(V^k(g), V^k(g))  ->  Ext^*_{S_k}(W^k(g), W^k(g)),

so the vacuum self-Ext algebra is the exterior algebra on classes of degrees 2 m_i + 1, and the derived
endomorphism algebra of the vacuum is formal. With (B): for every g the graded vector space
Ext^*(V, V) has the dimensions of H^*(g) at all but finitely many non-critical levels, and the exceptional levels are
rational. More precisely (Propositions 4.3, 4.4): at non-critical levels Ext^*(V, V) is an exterior algebra on classes of degrees
2 m_i + 1 outside a finite set F_g of rational levels. Its dimensions are invariant under tau -> -tau;
the reciprocal transformation tau -> 1/(r^v tau) also replaces g by its Langlands dual g^L.

(D) (g = sl_2, sl_3 and so_5 at every non-critical k; Sections 6 and 8.1). Ext^*(V, V) is the exterior
algebra on classes of degrees 3 (sl_2) and 3, 5 (sl_3). For sl_3 this includes the two levels
k + 3 = 3/5, 5/3 of central charge -22/5: the fibre there of the polynomial family used in the adopted
computation is W^k(sl_3) (Section 6.3). For so_5, at every non-critical level, Ext^*(V, V) is the exterior
algebra on classes of degrees 3 and 7 and the derived endomorphism algebra is formal (Theorems 8.1 and
8.6, computed over Q[tau, tau^{-1}] and at the four orbits of exceptional candidates; Proposition 9.6).

(E) (critical level, Section 6.4). For tau = 0 the algebra V is commutative, the differential of C(V)
vanishes, and Ext^*(V, V) = V (x) Lambda^*_cont(a_+^*), infinite-dimensional in every degree 0 <= n.

(F) (classical limit, Sections 5, 7, 9.3). The cohomology of the Lie algebroid of annihilation modes of the
classical W-algebra of g is H^*(g): restriction to the isotropy Lie algebra at the origin (the wedge
algebra, which is isomorphic to g) is a quasi-isomorphism. Over the local ring of the classical limit the
complex of (B) has a lattice with differential hbar D_cl + O(hbar^2), and every class of H^*(g) lifts to
the lattice: the Bockstein operations of the classical limit vanish for every g. For sl_4 this is the
vanishing of the map from degree 7 to degree 8; at every rank it says that the operations
beta(theta_i), which would define a Lie (and L-infinity) structure on the dual of the primitive classes, are
zero.

(G) (the reduction map at rational levels, Sections 7.4, 8.2). At every level
Ext^*(V, V) = Hom(V^k(g), K_2 * V^k(g)) for an explicit spherical kernel K_2, and DS_* is an isomorphism as
soon as the g[[t]]-cohomology of finitely many spectral flows of the affine vacuum vanishes, which holds
unless k (lambda, lambda)/2 is an integer and k (lambda, .) is in the root lattice for one of finitely many
coweights lambda. For sl_2: DS_*(theta_3) = -(1/2)(1 - tau^{-2}) omega_3 (computed), so DS_* fails to be an
isomorphism exactly at tau = +-1, where Ext is still Lambda(omega_3).

(H) (algebra structure, Section 9). At non-critical levels outside F_g, and for sl_2, sl_3 at every non-critical level, the
derived endomorphism algebra is formal (associative A-infinity). For sl_2 and sl_3 the
Batalin-Vilkovisky structure of the paired complex is trivial on the bulk. The natural Poisson bracket
of degree -2 on H^*(g) defined by an invariant form vanishes.

(I) (the exceptional sl_4 fibres; Sections 10-12). For g = sl_4 and tau = +-3/2, +-2/3
(central charges -7 and 253), the Ext dimensions in degrees 0,...,15 are
1,0,0,1,0,1,0,1,2,1,1,1,2,0,0,1, with no higher groups (Theorem 12.6).
The total dimension is twelve, rather than the exterior-algebra value eight.
For nonzero generators of degrees three, five and seven, eta_3 eta_5 and eta_3 eta_7
are nonzero, while eta_5 eta_7=0. At tau=+-3/2 the canonical reduction map has
kernel (theta_5 theta_7); at the reciprocal levels the generators are transported.
The proof computes the cone of
the reduction map from the affine algebra orbit by orbit on the affine Grassmannian (Proposition 10.1,
valid for every g and every level): at tau = -3/2 only the orbit of 2 theta^v contributes, through the
cohomology, twisted by the exponential of the Whittaker character and by a local system of square
roots, of an explicit variety of dimension 6 with three components.
The two-torus transgression of Section 12 determines the cone, and a nonzero
8 by 8 minor protected by the PBW filtration determines its final connecting rank.
Theorem 11.1 also identifies the first cyclic torsion summand of the local level-family complex.

(J) (higher primitives killed by reduction; Sections 11.3-11.5). For g=so_5 and k=-5,-1,
DS_*:Lambda(theta_3,theta_7)->Lambda(eta_3,eta_7) has kernel (theta_7) and is an
isomorphism in degree three. Thus reduction kills the higher primitive and the top
class although the universal W-vacuum self-Ext algebra remains exterior. For sl_3 at
tau=+-2,+-1/2, the canonical reduction kernel is (theta_5), and the degree-three map
is an isomorphism.

THE THEOREM ASKED OF THE CHAIN ("the vacuum self-Ext algebra of W^k(g) is the exterior algebra on classes
of degrees 2 m_i + 1 for every simple g at every non-critical level") IS FALSE AS STATED, by (I). What is
proved in its place: it holds for sl_2, sl_3 (proved) and so_5 (exact computation), with formality, at
every non-critical level; for every g it holds at non-critical levels, with formality, outside the finite set F_g of rational
levels (for sl_4: outside fourteen explicit levels, Corollary 8.5); it fails for sl_4 at four of these
fourteen levels. NOT PROVED: the full products involving the additional classes, formality,
and a Tor-to-Ext algebra comparison at tau=+-3/2,+-2/3; the bulk of W^k(sl_4) at the ten
levels tau = +-1, +-2, +-1/2, +-3, +-1/3 (predicted: the dimensions of
H^*(sl_4)); the description of the bulk at the levels of F_g for general g.

Relation to the published literature (STATE-OF-THE-ART.md gives the search and the exact locations).
Published results used as inputs: the structure of W^k(g) and the Miura map (Feigin-Frenkel; Arakawa,
arXiv:math/0506056, Theorems 4.8.5, 4.11.1, Proposition 4.12.1; arXiv:1605.00138, Theorems 5.17, 5.19,
Remark 5.24); reconstruction of modules (Li, hep-th/9406185, Theorem 3.2.10; De Sole-Kac,
arXiv:math-ph/0312042, Theorem 3.9); the affine Skryabin theorem and adolescent Whittaker averaging
(Raskin, arXiv:1611.04937, Theorems 2.7.1, 5.1.1); the duality of complementary levels (Dhillon,
arXiv:1905.06477, Theorems 5.12, 4.33); the Virasoro complex (Bakalov-Kac-Voronov, arXiv:math/9803022,
Theorems 6.1, 7.1); the paired W_3 differential (Bershadsky-Lerche-Nemeschansky-Warner, hep-th/9207067,
(2.2); Bouwknegt-McCarthy-Pilch, hep-th/9509119, Theorem 3.2); the classical wedge algebra and the oper
algebroid (Feher-O'Raifeartaigh-Tsutsui, hep-th/9307190, (2.12), (2.27); Frenkel-Gaitsgory,
arXiv:math/0508382, Proposition 4.4.3); the critical level (Arakawa, arXiv:1111.6329, Theorem 1.1;
Frenkel, arXiv:math/0210029, Theorem 9.8); the affine vacuum (Frenkel-Teleman, arXiv:math/0401428,
Propositions 4.2, 4.6); the regular presentation of W_3 at c = -22/5 (Hull-Palacios, hep-th/9206031;
Al-Ali-Linshaw, arXiv:1608.06255). Parts for which the search found no published statement, and which
are the theorem of this chain: (1) the comparison (A) in all smooth modules for every g and every level,
with the straightening lemmas and the resolution without a BRST current; (2) the finite weight-zero
model, its polynomial dependence on the level and the finiteness and rationality of the exceptional set
(B), (C); (3) the vacuum ring of W_3 at every non-critical level with its comparison, involution and
reduced classes (D); (4) the constant -(1/2)(1 - tau^{-2}) of the reduction map on Ext for sl_2 (G);
(5) the lattice of the classical limit, the first-order differential and the degeneration (F). The
exterior algebra itself is known for the Virasoro algebra at every central charge (it follows from
Bakalov-Kac-Voronov by Shapiro's lemma and the weight argument), and the isomorphism (C) for sl_2 at
irrational levels is sketched in Dhillon, Section 5.4.

Status of the ingredients. Proved here: (A), (B), (F), the reductions in (C) and (G), (E), (H), (I), (J),
Section 6.3. Cited: the inputs listed above. Adopted from this programme's checked records: the W_3 ring
computation (inscribe/ast-T96) and the W_3 comparison (inscribe/fab-T96), the affine and critical
statements of inscribe/fab-T53, the class of the reduced family (inscribe/fab-T125). Computed by the
other model family, with exact arithmetic and saved certificates: Theorem 8.1 (REQUESTS/3-calc),
Proposition 7.4 (REQUESTS/4-calc), the four products of Theorem 8.6 and the Tor table quoted in OPEN.md
(REQUESTS/5-calc). Computed here (scripts/): Section 6.3, the W_3 lifting controls, the parabolic
cohomology and Euler characteristics quoted in OPEN.md, and the spectral-flow cohomology of 8.2.
The final inscribe/chain-w-bulk/ADOPTION.md adopts the frozen Sections 0-9 after the restrictions
now incorporated in Sections 0, 2 and 3.3. The incremental
inscribe/chain-w-bulk-v2/ADOPTION.md adopts Sections 10-11 after the corrected
pole-order-to-coweight formula and the restriction of (F3) in 10.3 to its smooth
local-product applications, both now incorporated. Its frozen proof ends at 11.5.
Section 12 is later and is not covered by either adoption. The general formula (**)
and algebra comparison remain conjectural; Theorem 12.6 proves its dimension prediction
in the stated sl_4 case and is submitted for independent checking.

## 1. Setting and cited inputs

1.1 Generators. For every k in C the vertex algebra V = W^k(g) is Z_{>=0}-graded by a Hamiltonian H with
V_0 = C|0>, has a translation operator T, and is strongly and freely generated by homogeneous vectors
W^1, ..., W^r of weights d_1, ..., d_r: writing Y(W^i, z) = sum_n W^i_n z^{-n-d_i} (so [H, W^i_n] = -n W^i_n),
the monomials W^{i_1}_{-n_1} ... W^{i_s}_{-n_s}|0>, n_t >= d_{i_t}, taken in a fixed order, form a basis of V
(Feigin-Frenkel; Arakawa, Representation theory of W-algebras, arXiv:math/0506056, Theorem 4.11.1,
Proposition 4.12.1 and Remark 4.12.2). All d_i >= 2, and d_1 = 2 < d_i for i > 1, so V_2 = C W^1. For k
non-critical V has a conformal vector L with L_0 = H and L_{-1} = T, of central charge
c(k) = r - 12 |rho - (k + h^v) rho^v|^2 / (k + h^v) (loc. cit., formula (244)); thus W^1 = s L with a scalar
s = s(k) different from zero. Nothing in Section 2 depends on the normalisation of the generators. In the
family over C[k] of 3.3 the generator W^1 is regular at the critical level, where s vanishes; L itself has
a pole there.

1.2 Letters and words. A letter is a symbol x = W^i_n (1 <= i <= r, n in Z); deg x = n, d(x) = d_i. The
letters with n > -d_i are the annihilation letters; they form the set B_+ and span the space a_+; they are
exactly the letters killing |0>. For an integer beta >= 0 the beta-twisted degree of a letter is

    tw_beta(x) = deg x - beta d(x).

A word is a finite sequence of letters; deg, d (written Delta) and tw_beta are extended additively
(Delta(w) is the standard degree of w). For a word w, s_beta(w) >= 0 is the largest value of tw_beta on
a suffix of w (the empty suffix included). Fix for each beta a total order on letters refining tw_beta. A
word is beta-ordered if its letters increase weakly from left to right; an ordered word is called a
monomial; postw_beta(u) is the sum of the positive tw_beta of the letters of a monomial u. For a monomial,
s_beta(u) = postw_beta(u).

1.3 Relations. For all i, j there are vectors P^{ij}_s in V of weight d_i + d_j - s - 1 (s >= 0, finitely
many non-zero) with [W^i_lambda W^j] = sum_s lambda^s P^{ij}_s / s!. On every M in S_k

    (R)   [W^i_m, W^j_n] = sum_s binom(m + d_i - 1, s) (P^{ij}_s)_{m+n},

where for a PBW monomial p = W^{l_1}_{-n_1} ... W^{l_t}_{-n_t}|0> the operator p_N is the N-th mode (degree
N) of the iterated normally ordered product of the fields d^{n_1 - d_{l_1}} W^{l_1}, ..., d^{n_t - d_{l_t}} W^{l_t}
(up to factorials). Expanding the normally ordered products, p_N is a sum, with coefficients depending only
on (p, N) and the indices, of words in the letters W^{l_1}_{a_1}, ..., W^{l_t}_{a_t} (in some order) with
a_1 + ... + a_t = N; on a given vector of a module only finitely many of these words act non-trivially
(composite fields are fields). Since the weight of p is at least d_{l_1} + ... + d_{l_t}:

    (Delta)  every word u occurring in [x, y] has deg u = deg x + deg y and Delta(u) <= Delta(x) + Delta(y) - 1,
             hence tw_beta(u) >= tw_beta(x) + tw_beta(y) + beta for every beta >= 0

(for the empty word, which occurs only when deg x + deg y = 0, this reads 0 >= -beta(d(x) + d(y)) + beta).
A linear map between objects of S_k is a morphism if and only if it commutes with all letters (strong
generation).

1.4 Modules from fields. Let M be a vector space with operators W^i_n such that every W^i(z) =
sum_n W^i_n z^{-n-d_i} is a field on M and (R) holds on M. Then M carries a unique structure of object of
S_k with these generator fields. (The fields are mutually local by (R), hence generate a vertex algebra of
fields on M with M as a module: H. Li, Local systems of vertex operators, vertex superalgebras and modules,
arXiv:hep-th/9406185, Theorem 3.2.10, Corollary 3.2.11, Proposition 3.2.13. Their lambda-brackets are the
images of those of the generators, so the universal property of the freely generated vertex algebra gives a
homomorphism from V: De Sole-Kac, Freely generated vertex algebras and non-linear Lie conformal algebras,
arXiv:math-ph/0312042, Theorem 3.9 and Remark 3.10.)

1.5 The Miura map. Let pi be the Heisenberg vertex algebra of h at level tau (commutative for tau = 0),
with currents b^a(z) = sum_n b^a_n z^{-n-1}. There is a homomorphism of vertex algebras
Upsilon : W^k(g) -> pi, defined for every k, which is filtered for the standard filtration of W^k(g) and
the filtration of pi by the number of currents, and whose associated graded map is the pull-back
C[J(g//G)] -> C[J h] of functions on arc spaces along h -> g//G (Chevalley restriction). In terms of the
generators: the W^i can be chosen so that

    Upsilon(W^i) = P_i(b) + (normally ordered differential polynomials in the b^a with fewer than d_i currents),

P_1, ..., P_r homogeneous generators of C[h]^W of degrees d_i (Feigin-Frenkel; Arakawa, Introduction to
W-algebras and their representation theory, arXiv:1605.00138, Section 5.9, Theorem 5.17 with its proof,
Remark 5.18, and Section 2.6-2.7 for the classical map; Frenkel-Ben-Zvi, Vertex algebras and algebraic
curves, Chapter 15). Changing the generators W^i by elements of lower standard degree does not affect
anything below.

1.6 Conventions for the adopted W_3 records. For g = sl_3 the generators are T and a field U of weight 3
with [U_m, U_n] = (m - n)(Lambda_{m+n} + A a(m, n) L_{m+n}) + A (c/360) m(m^2-1)(m^2-4) delta_{m+n,0},
A = (22 + 5c)/16; with the usual normalisation W = U (16/(22+5c))^{1/2} the coefficient of Lambda in the
commutator [W_m, W_n] is 16/(22+5c) and the coefficient of Lambda at the double pole of the operator product
W(z)W(w) is 32/(22+5c) (the two numbers of frontier/register/conflicts/SYN/RESOLUTION.md, R112, are both
right, for these two different coefficients). Here

    Lambda = :TT: - (3/10) d^2 T,
    a(m,n) = (m+n+3)(m+n+2)/15 - (m+2)(n+2)/6,
    [L_m,U_n] = (2m-n) U_{m+n}.

The W_3 algebra is due to Zamolodchikov, Theor. Math. Phys. 65 (1985), 1205-1213,
doi:10.1007/BF01036128; the regular rescaling used here is as in the sources of Section 6.3.

## 2. The comparison theorem (every g, every level, all smooth modules)

For q >= 0 let Omega_q be the set of q-element subsets of B_+, and for M in S_k put
C^q(M) = {finitely supported functions Omega_q -> M}, written sum_omega m_omega c^omega.

THEOREM A. Let V = W^k(g), k in C arbitrary. There are natural linear maps D : C^q(M) -> C^{q+1}(M),
M in S_k, with D D = 0 and D m = sum_{x in B_+} x m c^x for m in M = C^0(M), such that
M -> H^n(C(M), D) is a universal cohomological delta-functor on S_k and

    H^n(C(M), D) = Ext^n_{S_k}(V, M)     for all n >= 0 and M in S_k,

by the unique isomorphism of delta-functors that is the identity on Hom(V, M) = {m : B_+ m = 0}. The maps D
preserve weights: if M is graded by weights so that a letter x lowers the weight by deg x, then D preserves
the total weight wt(m c^omega) = wt(m) + deg(omega). They are constructed in 2.7; any two constructions give
canonically isomorphic delta-functors.

The proof occupies 2.1-2.8. The inputs are 1.1-1.5 only.

### 2.1 Straightening on a vector

LEMMA 2.1. Let M be in S_k, m in M, beta >= 0, and w a word. Then w m is a finite linear combination of
vectors u m, u beta-ordered monomials with deg u = deg w and s_beta(u) >= s_beta(w); the monomial with the
same letters as w occurs with coefficient 1 and all other u have Delta(u) < Delta(w).

Proof. Induction on Delta(w), then on the number of inversions of w. If w is not ordered, write
w = w_1 y z w_2 with y > z adjacent. Then w m = w_1 z y w_2 m + w_1 [y, z] (w_2 m), and by (R) and 1.3,
[y, z](w_2 m) = sum_t c_t t (w_2 m), a finite sum over words t satisfying (Delta). The word w_1 z y w_2 has
the letters of w and fewer inversions; the words w_1 t w_2 have smaller standard degree. It remains to
compare suffixes. Suffixes of w_2 are suffixes of all the new words. The suffix z w_2 of w is dominated,
in w_1 z y w_2, by y w_2 (as tw(y) >= tw(z)); in w_1 t w_2, by t w_2 if tw(y) >= 0 (as
tw(t) >= tw(y) + tw(z)), and by w_2 if tw(y) < 0 (then tw(z) < 0). A suffix v y z w_2 of w, v a suffix
of w_1, has the same value as v z y w_2 and at most the value of v t w_2. So s_beta does not decrease. QED

### 2.2 Twisted depth

For M in S_k, beta >= 0 and N >= 0 put

    M^beta_{<=N} = {m in M : w m = 0 for every word w with tw_beta(w) > N},      M_beta = M^beta_{<=0},

and M^beta_{<=N} = 0 for N < 0.

LEMMA 2.2. (a) w M^beta_{<=N} is contained in M^beta_{<=N - tw_beta(w)} for every word w.
(b) M^beta_{<=N} = {m : u m = 0 for every beta-monomial u with postw_beta(u) > N}; in particular
M_beta = {m : x m = 0 for every letter x with tw_beta(x) > 0}.
(c) M^beta_{<=N} is contained in M^{beta'}_{<=N'} for beta' >= beta, N' >= N, and in M_{beta'} for
beta' >= beta + N/2. M is the union of the M_beta.

Proof. (a) If tw(w') > N - tw(w) then tw(w' w) > N. (b) A monomial u with postw(u) > N is u' u'' with u''
the product of its letters of positive twisted degree, a word of twisted degree > N; this gives one
inclusion. Conversely, if tw(w) > N then by Lemma 2.1 w m is a combination of u m with
postw(u) = s(u) >= s(w) >= tw(w) > N. For N = 0, a monomial with postw > 0 ends with a letter of positive
twisted degree. (c) tw_{beta'}(w) = tw_beta(w) - (beta' - beta) Delta(w) <= tw_beta(w). A letter with
tw_{beta'}(x) > 0 has tw_beta(x) > (beta' - beta) d(x) >= 2(beta' - beta) >= N. If W^i_n m = 0 for all i
and all n >= n_0, then m is in M_beta for beta >= n_0/2 by (b). QED

### 2.3 Twisted vacuum modules

Let gamma be a nonnegative integer. Let pi_gamma be the module over the Heisenberg Lie algebra (relations
[b^a_m, b^c_n] = tau m delta^{ac} delta_{m+n,0}) generated by a vector 1_gamma with b^a_n 1_gamma = 0 for
n > gamma; the monomials in the b^a_n, n <= gamma, form a basis of pi_gamma. The currents are fields on
pi_gamma, so pi_gamma is a module over the vertex algebra pi (1.4 applied to pi) and, through the Miura
map, an object of S_k. Let W_gamma be the V-submodule of pi_gamma generated by 1_gamma. Call a letter
gamma-good if tw_gamma(x) <= 0, and a word gamma-good if all its letters are.

LEMMA 2.3. (a) 1_gamma lies in (pi_gamma)_gamma.
(b) For integers 0 <= beta <= gamma the vectors u 1_gamma, u ranging over the gamma-good beta-monomials, form a basis
of W_gamma.
(c) (W_gamma, 1_gamma) represents the functor M -> M_gamma: for every M in S_k and m in M_gamma there is a
unique morphism W_gamma -> M with 1_gamma -> m.

Proof. Filter pi_gamma by the number of currents: F_p is spanned by the monomials with at most p letters b;
gr_F pi_gamma is the polynomial ring R_gamma = C[b^a_n : n <= gamma]. A letter b^a_n maps F_p to F_{p+1},
inducing multiplication by b^a_n on gr if n <= gamma, and maps F_p to F_{p-1} if n > gamma. By 1.5 the
operator W^i_n on pi_gamma is a sum of words in the b's with total index n, of length d_i (the modes of
P_i(b)) or less, finitely many of them non-zero on a given vector. Hence W^i_n maps F_p to F_{p+d_i} and
induces on gr the multiplication by

    w^i_n = coefficient of z^{-n-d_i} in P_i(b_gamma(z)),     b_gamma(z) = sum_{a <= gamma} b_a z^{-a-1},

a finite sum; w^i_n = 0 if n > gamma d_i, because then every term contains a letter of index > gamma.
(a) For n > gamma d_i every word of total index n and length <= d_i occurring in W^i_n contains a letter
b_a with a > gamma >= 0; such a letter stands in the annihilation part of the normally ordered word, the
annihilation letters commute with each other, so the word kills 1_gamma.
(b) The polynomials w^i_n, n <= gamma d_i, are algebraically independent in R_gamma. Indeed give
b^a_{gamma-j} the level j >= 0; then w^i_{gamma d_i - j} is homogeneous of level j, equals P_i(b_gamma) for
j = 0, and for j >= 1 equals sum_a (d_a P_i)(b_gamma) b^a_{gamma-j} plus a polynomial in the variables of
levels < j. So the Jacobian of the functions of levels <= j with respect to the variables of levels <= j is
block triangular with diagonal blocks the Jacobian J of (P_1, ..., P_r), and det J is a non-zero polynomial
(a non-zero multiple of the product of the positive roots). Hence the map they define is dominant and they
are algebraically independent.
Now let u be a word; u 1_gamma lies in F_{Delta(u)} with symbol the product of the w_x over the letters x
of u. For gamma-good words with distinct multisets of letters these symbols are distinct monomials in
algebraically independent polynomials. So the vectors u 1_gamma, u the gamma-good gamma-monomials, are
linearly independent (look at the terms of maximal standard degree of a relation). They span W_gamma:
by Lemma 2.1 every w 1_gamma is a combination of u 1_gamma, u gamma-monomials, and a gamma-monomial which
is not gamma-good ends with a letter of positive twisted degree and kills 1_gamma by (a) and Lemma 2.2(b).
This is (b) for beta = gamma. For beta < gamma: for a multiset A of gamma-good letters let u_A, u'_A be
the gamma- and the beta-monomial with letters A. Lemma 2.1 (for beta, then for gamma on the words of
lower standard degree) gives u'_A 1_gamma = u_A 1_gamma + a combination of u_{A'} 1_gamma with
deg A' = deg A and Delta(A') < Delta(A). For fixed degree and bounded standard degree there are finitely
many such multisets (indices are bounded above), so the passage is unitriangular.
(c) Let m be in M_gamma. In M (+) pi_gamma the vector (m, 1_gamma) lies in the gamma-part, so the submodule N
it generates is spanned by the u (m, 1_gamma), u gamma-good gamma-monomials (as in (b)). The projection
N -> W_gamma sends these to a basis, hence is an isomorphism, and its inverse followed by the projection
to M is the required morphism. QED

Remark (why the cut-off is twisted). The module generated by a vector killed by all W^i_n with n >= N (the
same N for all i) has no such basis in general: if the relations contain a product of three or more
letters (for g = sl_4 the commutator of two modes of the generator of weight 4 contains modes of TTT), the
relation [W^i_m, W^j_n] 1 = 0, m, n >= N, expresses products of letters of index < N through each other.
The twisted cut-off n > gamma d_i is the one compatible with (Delta); it corresponds to poles of order at
most (gamma + 1) d_i of W^i(z) on the generating vector (opers with singularity of order <= gamma + 1; these
are the generalized vacuum modules of Raskin, W-algebras and Whittaker categories, arXiv:1611.04937,
Section 4, Theorem 4.16.1). For sl_2 and sl_3 the relations are at most quadratic and both cut-offs work.

### 2.4 Truncated twisted vacuum modules

LEMMA 2.4. Let beta, N, gamma be nonnegative integers with gamma >= beta + N/2. Let K be the span of the vectors v w 1_gamma in
W_gamma, v, w words with tw_beta(w) > N, and W^beta_N = W_gamma / K, with generator 1 the image of 1_gamma.
(a) (W^beta_N, 1) represents M -> M^beta_{<=N}; in particular it does not depend on gamma.
(b) The vectors u 1, u ranging over the beta-monomials with postw_beta(u) <= N, form a basis of W^beta_N.
(c) Let G_p W^beta_N be the span of the w 1 with Delta(w) <= p. Then G_p is spanned by the basis vectors
of (b) with Delta(u) <= p, a letter x maps G_p to G_{p+d(x)}, and gr_G W^beta_N is the quotient S^beta_N of
the symmetric algebra S(a) on all letters by the span of the commutative monomials with postw_beta > N,
letters acting by multiplication.

Proof. (a) K is a submodule, and a morphism W_gamma -> M, 1_gamma -> m, kills K if and only if m lies in
M^beta_{<=N}; use Lemma 2.3(c) and Lemma 2.2(c).
(b) A beta-monomial with postw_beta <= N is gamma-good (its letters have tw_gamma <= tw_beta - 2(gamma - beta)
<= 0). By Lemma 2.3(b) it suffices to show that K is the span K' of the u 1_gamma, u gamma-good
beta-monomials with postw_beta(u) > N. Such a u is u' u'' with tw_beta(u'') > N, so K' is in K. Conversely
we show by induction on Delta(w) that w 1_gamma lies in K' for every word w with s_beta(w) > N (this
contains the generators of K). By Lemma 2.1, w 1_gamma is a combination of u 1_gamma, u beta-monomials
with s_beta(u) > N; those with Delta(u) < Delta(w) are covered by the induction, and there remains the
monomial u with the letters of w. If u is gamma-good, u 1_gamma is in K'. If not, write u = u_1 y z_1 ... z_l
with tw_gamma(y) > 0 and z_1, ..., z_l gamma-good. Since y 1_gamma = 0,

    u 1_gamma = sum_j u_1 z_1 ... z_{j-1} [y, z_j] z_{j+1} ... z_l 1_gamma,

a finite combination of words w'' = u_1 z_1 ... z_{j-1} t z_{j+1} ... z_l with t a word of [y, z_j], of smaller
standard degree. As tw_beta(t) >= tw_beta(y) + tw_beta(z_j) and tw_beta(y) >= tw_gamma(y) > 0, every suffix
of u is dominated by a suffix of w'' (compare the suffixes beginning at the same place, and the suffix of
u beginning at y with the suffix of w'' beginning at z_1). So s_beta(w'') > N and the induction applies.
(c) The first statement is Lemma 2.1. For a basis monomial u and a letter x, x u 1 is, modulo lower
standard degree, the monomial with letters u and x applied to 1, which vanishes if its postw_beta is > N
(it is then of the form u' u'' 1 with tw_beta(u'') > N). QED

### 2.5 Injective objects

For a word w and beta, N >= 0, the vector w 1 of W^beta_N lies in (W^beta_N)^beta_{<=N - tw_beta(w)}
(Lemma 2.2(a)); so there is a morphism

    rho_w : W^beta_{N - tw_beta(w)} -> W^beta_N,    a 1 -> a w 1     (zero if N - tw_beta(w) < 0).

For a vector space E let I(E) be the union over (beta, N) of the spaces Hom_C(W^beta_N, E) (the transition
maps are induced by the surjections W^{beta'}_{N'} -> W^beta_N, beta' >= beta, N' >= N, and by
W_gamma -> W^beta_N), with letters acting by x phi = phi rho_x. Then (w phi)(a 1) = phi(a w 1) for words w.

LEMMA 2.5. I(E) is an object of S_k; I(E)^beta_{<=N} = Hom_C(W^beta_N, E); and for M in S_k

    Hom_{S_k}(M, I(E)) = Hom_C(M, E),    F -> (m -> F(m)(1)),

naturally. Hence I(E) is injective, M embeds into I(M), and S_k has enough injectives.

Proof. If phi is in Hom_C(W^beta_N, E) then x phi = 0 for tw_beta(x) > N, so the W^i(z) are fields on I(E).
The relation (R) holds on I(E): for letters y, z, the words t of [y, z] with t 1 non-zero in W^beta_N are
finitely many, t phi = 0 for the others, and (([y, z] - sum_t c_t t) phi)(a 1) = phi(a ([y, z] - sum_t c_t t) 1)
= 0 because (R) holds in W^beta_N. By 1.4, I(E) is in S_k. If phi is in Hom_C(W^beta_N, E) and tw_beta(w) > N
then (w phi)(a 1) = phi(a w 1) = 0; conversely if phi in Hom_C(W_gamma, E), gamma >= beta + N/2, is killed by
all such w, then phi kills the submodule K of Lemma 2.4 and factors through W^beta_N. The inverse of the
displayed map sends f : M -> E to F_f, F_f(m)(a 1_gamma) = f(a m) for m in M_gamma, where a m is the image of
a 1_gamma under the morphism of Lemma 2.3(c); one checks F_f(x m) = x F_f(m) from the definitions. QED

### 2.6 Twisted truncated Koszul complexes

Fix a total order on B_+ (to define signs). For beta >= 0 let Omega^beta_q be the set of omega in Omega_q
with tw_beta(omega) <= 0. It is finite: each letter of B_+ has tw_beta > -(1 + beta) d_r, so the letters of
such an omega have bounded twisted degree. Put S^beta_N = 0 for N < 0 and

    K^beta_q = direct sum over omega in Omega^beta_q of S^beta_{-tw_beta(omega)} e_omega,
    kappa(f e_omega) = sum_{x in omega} eps(x, omega) f x e_{omega - x},

eps(x, omega) = (-1)^{number of elements of omega before x}. The map is well defined (if postw(f) > N then
postw(f x) > N + tw(x)) and kappa kappa = 0. Let a_- be the span of the letters outside B_+.

LEMMA 2.6. H_q(K^beta, kappa) = 0 for q > 0, and H_0 = S(a_-), the quotient of S^beta_0 by the letters of
B_+ of twisted degree <= 0.

Proof. Split the letters by the sign of tw_beta: a = a' (+) a'', a'' spanned by the letters of positive
twisted degree; these all lie in B_+, and the set B' of letters of B_+ in a' is finite. Then
S^beta_N = S(a') (x) S(a'')_{<=N}, where S(a'') is graded by tw_beta with finite-dimensional pieces. Writing
omega = omega' + omega'' accordingly, K^beta is the direct sum over omega' in B' of
S(a') e_{omega'} (x) L_{T(omega')}, T(omega') = -tw_beta(omega') >= 0, where L_T is the quotient of the
Koszul complex S(a'') (x) Lambda(a'') by its part of total twisted degree > T. The Koszul differential
preserves the total twisted degree, and the Koszul complex of a positively graded space is acyclic in every
positive total degree (Euler homotopy) and equal to C in total degree 0; so H(L_T) = C, in exterior degree 0,
for every T >= 0. The differential of K^beta is the sum of the Koszul differential of the factors L and of
the part removing a letter x of omega', which multiplies by x in S(a') and projects L_{T(omega')} onto
L_{T(omega') + tw(x)}. Filtering by the number of elements of omega' gives a spectral sequence with
E^1 = S(a') (x) Lambda(B') and d^1 the Koszul differential of the finitely many variables B' of the
polynomial ring S(a'), whose homology is S(a')/(B') = S(a_-) in degree 0. QED

### 2.7 The resolution

For beta >= 0 put P^beta_q = direct sum over omega in Omega^beta_q of W^beta_{-tw_beta(omega)} e_omega, an
object of S_k, graded by deg(a e_omega) = deg(a) + deg(omega) and filtered by
G_p P^beta_q = sum_omega (G_{p - Delta(omega)} W) e_omega. For beta <= beta' there is a surjection
P^{beta'}_q -> P^beta_q (identity on generators e_omega with omega in Omega^beta_q, zero on the others;
defined by Lemma 2.2(c), since -tw_{beta'}(omega) >= -tw_beta(omega)). Let eps : P^beta_0 = W_beta -> V be
the morphism 1 -> |0>.

PROPOSITION 2.7. There are morphisms d = d^beta_q : P^beta_q -> P^beta_{q-1}, q >= 1, beta >= 0,
compatible with the surjections P^{beta'} -> P^beta, preserving deg and the filtrations G, such that
(i) d d = 0 and eps d = 0;
(ii) d(e_omega) = sum_{x in omega} eps(x, omega) x e_{omega - x} modulo G_{Delta(omega) - 1} (terms with
omega - x outside Omega^beta_{q-1} omitted);
(iii) for every beta, ... -> P^beta_1 -> P^beta_0 -> V -> 0 is exact.

Proof. Two general facts. (1) If y in P^beta_{q-1} is homogeneous of degree deg(omega) and lies in
G_{Delta(omega)}, then y lies in (P^beta_{q-1})^beta_{<=-tw_beta(omega)}, so e_omega -> y defines a morphism
from the summand W^beta_{-tw_beta(omega)} e_omega: indeed y is a combination of u e_{omega'} with
deg u + deg omega' = deg omega and Delta(u) + Delta(omega') <= Delta(omega), hence
tw_beta(u) + tw_beta(omega') >= tw_beta(omega), and u 1 lies in the part of depth
<= -tw_beta(omega') - tw_beta(u) <= -tw_beta(omega) of W^beta_{-tw_beta(omega')} (Lemma 2.2(a)).
(2) Each homogeneous filtered piece (P^beta_q)_{deg = n, G_p} is finite-dimensional (finitely many omega;
for each, finitely many monomials of bounded standard degree, given degree and bounded indices), and the
surjections P^{beta'} -> P^beta are surjective on these pieces.
By Lemma 2.4(c) and (ii), the associated graded of the part of the complex already constructed is the
complex K^beta of 2.6, and gr of eps is the projection S^beta_0 -> S(a_-) (the basis of 1.1). Since G is
exhaustive with G_{-1} = 0, exactness of gr at a place implies exactness there and strictness: a cycle in
G_p is the boundary of an element of G_p.
Construction, by induction on q. For q = 1 put d(e_x) = x 1; then eps d = 0, and the cokernel of d
represents {m in M_beta : x m = 0 for x in B_+ with tw_beta(x) <= 0} = {m : B_+ m = 0}, so it is V. Let
q >= 2 and suppose d constructed in degrees < q with (i), (ii). For omega in Omega_q let
y_0 = sum_{x in omega} eps(x, omega) x e_{omega - x}, an element of every P^beta_{q-1} with
omega in Omega^beta_q, compatible with the surjections, homogeneous of degree deg(omega), in G_{Delta(omega)}.
By (ii) in degree q - 1, d(y_0) is, modulo G_{Delta(omega) - 1}, the sum over pairs x < y in omega of
+-[x, y] e_{omega - x - y}, which lies in G_{Delta(omega) - 1} by (Delta). So z = d(y_0) is a cycle (for
q = 2: eps z = 0) of degree deg(omega) in G_{Delta(omega) - 1}. By Lemma 2.6 and strictness, for each beta
the set Y^beta of the y_1 in (P^beta_{q-1})_{deg omega, G_{Delta(omega) - 1}} with d(y_1) = z is a non-empty
finite-dimensional affine space, and the surjections map Y^{beta'} into Y^beta. A countable inverse system
of non-empty finite-dimensional affine spaces has a non-empty limit; choose (y_1^beta) in it and put
d(e_omega) = y_0 - y_1 (a morphism by (1)). Then (i), (ii) hold in degree q, and (iii) follows from
Lemma 2.6 in all degrees. QED

### 2.8 Proof of Theorem A

Put C^q_beta(M) = Hom_{S_k}(P^beta_q, M), the space of cochains sum m_omega c^omega with omega in
Omega^beta_q and m_omega in M^beta_{<=-tw_beta(omega)}, with the differential D_beta dual to d. By the
compatibility in Proposition 2.7, C_beta(M) is a subcomplex of C_{beta'}(M) for beta <= beta'. Every
cochain m c^omega lies in C_beta(M) for beta large (m in M_beta by Lemma 2.2(c), and tw_beta(omega) <= 0).
So C(M) is the union of the C_beta(M) and carries a differential D, natural in M, preserving degrees, with
(D m)(e_x) = x m. The functor M -> C(M) is exact (C^q(M) is a direct sum of copies of M), so M -> H^n(C(M))
is a cohomological delta-functor; H^0(C(M)) = {m : B_+ m = 0} = Hom(V, M). For a vector space E, Lemma 2.5
gives C_beta(I(E)) = Hom_C(P^beta, E), which is exact in positive degrees by Proposition 2.7(iii); passing
to the union, H^n(C(I(E))) = 0 for n > 0. Every M embeds into I(M) and I(M) is injective, so the functors
H^n(C(-)), n > 0, are effaceable and vanish on enough injectives: M -> H^n(C(M)) is the universal
delta-functor extending Hom(V, -), i.e. the right derived functors of Hom(V, -) (Grothendieck, Sur quelques
points d'algebre homologique, II.2.2.1 and II.2.3). QED

2.9 Remarks. (1) For g = sl_2 at a non-critical level, normalising the generator to L makes (R) the Virasoro relations, and the
Chevalley-Eilenberg differential of the Lie algebra a_+ of vector fields on the disc satisfies
Proposition 2.7; so Ext^n(Vir^c, M) = H^n(a_+, M) (continuous cochains).
(2) For g = sl_3 at a non-critical level, Theorem A is the comparison theorem adopted in inscribe/fab-T96 (there the complex is
obtained from the paired complex by homological perturbation; both compute the same universal
delta-functor). The new points for general g are the construction of D without a BRST current (2.7) and
the twisted cut-offs (2.3, 2.4).
(3) All auxiliary cutoff indices beta, N, gamma in Section 2 are nonnegative integers. Such cutoffs
are cofinal: Lemma 2.2(c) puts every smooth vector in an integer M_beta, and every lower bound for gamma
can be replaced by its ceiling. At critical level Theorem A still holds, with the commutative Koszul
realisation of Section 6.4; neither the Witt nor the conformal paired realisation is asserted there.
(4) The same proof gives: for every word-homogeneous natural endomorphism of the system (P^beta) inducing
zero on V, the induced endomorphism of H^n(C(M)) is zero for all n (a morphism of universal delta-functors
is determined in degree 0). This is used in 3.2.

## 3. Finiteness, weight zero, dependence on the level

### 3.1 The weight grading

V is graded by the weights w >= 0, and C(V) is the direct sum of the subcomplexes
C(V)_w, C^q(V)_w = direct sum over omega in Omega_q of V_{w - deg omega} c^omega.

LEMMA 3.1. C^q(V)_w is finite-dimensional for all q, w, vanishes for q large (depending on g and w), and
sum_q (-1)^q dim C^q(V)_w = 0 for every w.

Proof. The letters of B_+ of negative degree are the W^i_n, -m_i <= n <= -1; their total degree is
-w_g, w_g = sum_i m_i(m_i + 1)/2. If V_{w - deg omega} is non-zero then deg omega <= w, so the letters of
omega of non-negative degree are distinct letters of total degree <= w + w_g: finitely many possibilities,
with a bounded number of letters. The generating function sum_w t^w sum_q (-1)^q dim C^q(V)_w is the product
of the character prod_i prod_{n >= d_i} (1 - t^n)^{-1} of V with prod_i prod_{n > -d_i} (1 - t^n), that is
prod_i prod_{-d_i < n < d_i} (1 - t^n) = 0 (the factor n = 0). QED

For g = sl_3 the dimensions of C^q(V)_0, q = 0, ..., 8, are 1, 3, 14, 37, 56, 54, 31, 10, 2. In general the
largest q with C^q(V)_0 non-zero can exceed dim g (for sl_10 it is 104 > 99).

### 3.2 Weight zero

PROPOSITION 3.2. Let k be non-critical and L_0 = s(k)^{-1} W^1_0 (1.1). For every M in S_k the operator
theta(m c^omega) = (L_0 m + deg(omega) m) c^omega commutes with D and induces zero on H^n(C(M)) for all n.
For M = V it is the multiplication by the total weight. Hence

    Ext^n_{S_k}(V, V) = H^n(C(V)_0, D),

a finite-dimensional space, zero for n large, and sum_n (-1)^n dim Ext^n(V, V) = 0.

Proof. On P^beta_q let DD be the linear operator multiplying a e_omega (a a word) by -(deg a + deg omega).
Since [L_0, x] = -deg(x) x for every letter x, the operator kappa = L_0 - DD (L_0 acting as a letter)
commutes with all letters, so it is an endomorphism of P^beta_q in S_k; it commutes with d (d is a
morphism and preserves degrees) and with the surjections P^{beta'} -> P^beta, and it induces zero on
V = coker(d_1), because L_0 a|0> = -deg(a) a|0>. The dual of kappa on C(M) is theta:
(theta phi)(e_omega) = phi((L_0 + deg omega) e_omega). So theta is a natural endomorphism of the complex
C(M), hence a morphism of the delta-functor H^n(C(-)) to itself; in degree 0 it is L_0 acting on
{m : B_+ m = 0}, which is zero since L_0 is in B_+. A morphism of universal delta-functors is determined
by its component of degree 0, so theta = 0 on all H^n(C(M)). On C(V), L_0 m = wt(m) m, so theta is the
total weight, and the cohomology of C(V)_w vanishes for w non-zero. The rest is Lemma 3.1. QED

### 3.3 Dependence on k

LEMMA 3.3 (the family). Let A = C[k]. There is a vertex algebra W_A over A, graded by weights, free as an
A-module in each weight, with elements W^1, ..., W^r of weights d_i such that for every k_0 in C the fibre
W_A (x)_A C_{k_0} is W^{k_0}(g) and the images of the W^i are strong free generators of it as in 1.1. The PBW
monomials in the W^i form an A-basis of W_A; in particular the coefficients of the PBW expansions of the
vectors P^{ij}_s of 1.3 are polynomials in k. The A-module of weight 2 is A W^1, and at a non-critical k_0
the conformal vector is L = s(k_0)^{-1} W^1, where s is a polynomial in k all of whose zeros are at the
critical level, and s(-h^v) = 0. (For g = sl_2: W^1 = S = tau L = (1/4) :hh: + ((tau - 1)/2) dh in the
Heisenberg algebra [h lambda h] = 2 tau lambda, with
[S lambda S] = tau (d + 2 lambda) S + ((-6 tau^3 + 13 tau^2 - 6 tau)/12) lambda^3, s = tau. The vector L is not a section of
W_A: its central charge has a pole at tau = 0.)

Proof. The affine vertex algebra, the ghosts and the Drinfeld-Sokolov complex are defined over A, with the
operator products and the differential polynomial in k (Arakawa, arXiv:math/0506056, Lemma 4.8.2, exhibits
the dependence of the differential on the level). Let C''_A be the subcomplex of loc. cit., Section 4.8;
it is concentrated in non-negative cohomological degrees, its weight spaces are free A-modules of finite
rank (loc. cit., (181)), and for every k_0 in C, H^0(C''_{k_0}) = ker(d : C''^0_{k_0} -> C''^1_{k_0}) = W^{k_0}(g)
(Remark 4.8.6, Theorems 4.8.5 and 4.11.1), of dimension in each weight independent of k_0 (1.1). Put
W_A = ker(d : C''^0_A -> C''^1_A). In each weight this is the kernel of a map of free A-modules of finite
rank, so it is free and saturated, and its fibre at k_0 is a subspace of ker(d_{k_0}) of the generic
dimension; as the dimension of ker(d_{k_0}) does not depend on k_0, the fibre is all of W^{k_0}(g). W_A is a
vertex subalgebra over A. The same argument applies to the pieces F_p W_A = W_A ∩ F_p C''_A of the filtration
of loc. cit., Section 4.11 (the graded dimensions of F_p W^{k_0}(g) do not depend on k_0, Theorem 4.11.1), so
the symbol maps F_p W_A -> gr_p are maps of free A-modules of finite rank in each weight which are surjective
on every fibre onto the corresponding piece of H^0(gr C''_{k_0}), hence surjective onto a saturated
submodule; lifting the symbols of the generators gives W^i in W_A whose fibres are generators as in 1.1.
The PBW monomials are a basis of every fibre, hence an A-basis of W_A in each weight. The weight-2 part of
W_A is free of rank one, spanned by W^1, whose fibres are all non-zero; so at a non-critical k_0,
W^1 = s(k_0) L with s(k_0) non-zero, and [W^1 lambda W^1] = s (d + 2 lambda) W^1 + (c s^2 / 12) lambda^3 has
coefficients polynomial in k: s is a polynomial. At the critical level the fibre is commutative (Theorem
6.4), so s(-h^v) = 0. QED

PROPOSITION 3.4. The constructions of Section 2 can be made over A: the differential D of C(V_k)_0 can be
chosen so that, in the bases of PBW monomials, its matrix entries are polynomials in k. Consequently
k -> dim Ext^n(W^k(g), W^k(g)) (k non-critical) is upper semicontinuous for the Zariski topology: it
takes its minimal value outside a finite set of levels and is at least that value everywhere.

Proof. Lemmas 2.1-2.6 hold verbatim over A for W_A-modules that are free over A with the bases described
(the Heisenberg algebra over A with tau = k + h^v, the modules pi_gamma, W_gamma, W^beta_N over A; the
independence argument of Lemma 2.3 uses only the symbols; the Koszul homotopies need Q inside A). In the
induction of Proposition 2.7 the element y_1 is chosen as follows instead: the kernel N of the surjection
P^{beta+1} -> P^beta has associated graded the kernel of K^{beta+1} -> K^beta, which is acyclic (both
resolve S(a_-)); hence, by strictness, a solution y_1^beta of d(y_1) = z in P^beta lifts to a solution in
P^{beta+1} (lift arbitrarily and correct by an element of N of the same filtration degree). Choosing the
solutions successively in beta gives a compatible family over A. The fibre at k_0 of the resulting system
satisfies Proposition 2.7 for W^{k_0}(g), so by Theorem A and Proposition 3.2 the complex of finitely
generated free A-modules C(W_A)_0 has fibres computing Ext^n(W^{k_0}(g), W^{k_0}(g)) at the non-critical
k_0. The ranks of the differentials of a complex of free A-modules of finite rank are lower
semicontinuous. QED

Remark. For g = sl_2, in the letters S_n = tau L_n, the matrix of D on
C(V)_0 = span{1, c^0, c^{-1}c^1, c^{-1}c^0c^1} is D c^0 = 2 tau c^{-1}c^1 and zero on the other three vectors:
its rank is constant on the non-critical levels and drops at tau = 0. For g = sl_3, in the noncritical
T,U coordinates of 1.6, the particular differential obtained by homological perturbation of the
paired complex has degree exactly two in the central charge. This bound concerns this choice of
differential, not every choice in Proposition 2.7 or the regular critical-level basis of Lemma 3.3.

To prove the bound, on the paired complex give a PBW state the Kazhdan degree
K = Delta(matter in both factors) + sum_b spin(b) - sum_c spin(c).
The Koszul differential and its contraction H preserve K and are independent of c. A linear-in-c
commutator branch lowers K by at least four: the Virasoro central term removes two weight-two letters;
the U,U-to-L term replaces total degree six by degree two; and the terms with coefficient
mu=(c-50)/32 have ghost degree change 2-3-3=-4. The quadratic central U,U branch lowers K by six.
All other branches have nonpositive K-shift. The same bounds hold in the complementary factor at
100-c. Consequently a coefficient of degree at least three in
D = pi delta sum_{j>=0}(-H delta)^j iota, delta=Q-d_K, would lower K by at least ten.
This expression terminates on every state by the contraction of Theorem 6.2.

At a one-sided weight-zero endpoint with q ghosts, of which n_3 have spin three,
K = Delta(matter)-2q-n_3 and -5 <= Delta(matter)-n_3 <= 2. Indeed the total negative ghost
weight is at most four, so the matter weight and Delta(matter) are at most four. For n_3=0
the negative budget is one and the matter is the vacuum; for n_3=1 the budget is at most three;
for n_3>=2 use Delta(matter)<=4. Six spin-three ghosts have minimum total weight three,
and spin-two ghosts supply at most one negative unit, so n_3<=5. A degree-one differential
therefore lowers endpoint K by at most nine. Cubic coefficients are impossible.
The bound is attained by the direct U_3 U_{-3}|0> entry c(22+5c)/48: choose source
U_{-3}|0> c^{U,-1}c^{U,-2} and target c^{U,3}c^{U,-1}c^{U,-2}, using physical mode labels.
The contraction H delta of this source is zero: the only possible second-factor matter term
comes from the mixed L_2 b^2 c^3 dc^3 term, whose matter and antighost creation weights
already exceed the available negative ghost weight. Thus no higher perturbation term
changes this entry. The five values in scripts/kazhdan_w3_pages.py check the formula;
the filtration argument, rather than interpolation, proves its degree bound.

## 4. Irrational levels: reduction from the affine algebra

### 4.1 The map induced by quantum reduction (every level)

Let A_k be the category of smooth modules over the affine Lie algebra of g at level k (the modules over
V^k(g)). For M in A_k let C_DS(M) = M (x) F be the Drinfeld-Sokolov complex (F the Fock space of the ghosts
of n((t)), with the differential of the character psi). It is a complex of objects of S_k (the vertex
algebra W^k(g) is a subalgebra of the complex C_DS(V^k(g)) consisting of cocycles, and acts on C_DS(M) by
chain maps), exact in M, and the inclusion W^k(g) -> C_DS(V^k(g)) is a quasi-isomorphism (Feigin-Frenkel;
de Boer-Tjin; Arakawa, arXiv:math/0506056, Theorems 4.8.5, 4.11.1). Totalisation of bounded complexes
gives an exact functor D^b(A_k) -> D(S_k) sending V^k(g) to an object isomorphic to W^k(g), hence a
homomorphism of graded algebras

    DS_* : Ext^*_{A_k}(V^k(g), V^k(g)) -> Ext^*_{S_k}(W^k(g), W^k(g)),

defined for every k. For k non-critical the source is H^*(g[[t]], V^k(g)) = H^*(g), an exterior algebra
on the primitive classes theta_i of degrees 2 m_i + 1, represented by cochains on the constant loops
(adopted: inscribe/fab-T53, items D1, D2 and Lemma E). So DS_* provides, at every non-critical level,
classes eta_i(k) = DS_*(theta_i) in Ext^{2 m_i + 1}(W^k(g), W^k(g)).

### 4.2 The theorem

THEOREM 4.1. Let k be an irrational complex number. Then DS_* is an isomorphism of graded algebras:

    Ext^*_{S_k}(W^k(g), W^k(g)) = Lambda(eta_1(k), ..., eta_r(k)),    deg eta_i = 2 m_i + 1,

and the derived endomorphism algebra of W^k(g) in S_k is formal.

Proof (from the theorems of Raskin, W-algebras and Whittaker categories, arXiv:1611.04937; references
R. below are to that paper; kappa is the level k).
Step 1 (the categories). R. Section 5.1 defines W_kappa-mod as the ind-completion of the full subcategory
of D^+(W_kappa-mod^heart) generated by the generalized vacuum modules W^n_kappa, n >= 0, where W^0_kappa is
the vacuum module and W_kappa-mod^heart is the category of discrete modules over the topological algebra
of the vertex algebra, that is S_k. Hence Hom_{W_kappa-mod}(W^0_kappa, W^0_kappa[n]) = Ext^n_{S_k}(V, V).
Likewise hat-g_kappa-mod has heart A_k, bounded below part D^+(A_k), and
Hom(V^k(g), M[n]) = H^n(g[[t]], M) for M in A_k.
Step 2 (affine Skryabin). R. Theorem 5.1.1 gives an equivalence Whit(hat-g_kappa-mod) = W_kappa-mod
compatible with the Drinfeld-Sokolov functor, and by R. 5.7 the vacuum module corresponds to iota_{0,!} V,
V = V^k(g) regarded in hat-g_kappa-mod^{G(O)} (the n = 0 term of the adolescent Whittaker system of
R. 2.2: I_0 = G(O); I_1 is the conjugate by rho^v(t)^{-1} of the pro-unipotent radical of the Iwahori
subgroup, with the character psi). By R. Theorem 2.7.1, iota_{0,1,!} exists, is left adjoint to
iota^!_{0,1}, and iota_{1,infinity,!} is fully faithful. Since I_1 and H = I_0 cap I_1 are pro-unipotent,
equivariant objects for them form full subcategories of hat-g_kappa-mod, and iota_{0,1,!} V = X is the
!-average of V from H-equivariance to (I_1, psi)-equivariance, with unit u : V -> X. Therefore

    Ext^*_{S_k}(V_W, V_W) = End(iota_{0,!} V) = End(X) = Hom(V, X[*]) = H^*(g[[t]], X),

V_W = W^k(g), and the homomorphism End(V) -> End(X) induced by the averaging functor L = Av_!^{I_1,psi} is
composition with u:

    L_* = u_* : H^*(g[[t]], V^k(g)) -> H^*(g[[t]], X).

L_* = DS_* on all derived endomorphisms of V, for the following reason. Let q be the functor of Whittaker
coinvariants (the Drinfeld-Sokolov functor of R. Section 5, with the conventions of R. Warning 5.5.1),
R = Av_*^{I_1,psi}, N_1 = N(K) cap I_1, and Delta = dim(I_1 / H). Since I_1 = N_1 H, the *-average of an
H-equivariant object to (I_1, psi) is its average along N_1, which is absorbed by the coinvariants along
N(K): q R = q on H-equivariant objects. On (I_1, psi)-equivariant objects q = iota_{1,infinity,!}[2 Delta].
The canonical morphism L -> R[2 Delta] is an isomorphism on V (R. Theorem 2.7.1 and Remark 2.7.3), hence on
the thick subcategory generated by V, which consists of H-equivariant objects. So on that subcategory
q = iota_{1,infinity,!} L naturally, and iota_{1,infinity,!} is fully faithful: the map induced by q on
End^*(V) is L_*. (Delta = 1, 4, 10, 7, 16 for A_1, A_2, A_3, B_2, G_2.) All this holds for every level.
Step 3 (irrational level). We show that u_* is an isomorphism. For Z in hat-g_kappa-mod^H,
Hom(V, Z) = Hom_{G(O)-equivariant}(V, Av_*(Z)), Av_* the right adjoint of the forgetful functor from
G(O)-equivariant objects. The functors Z -> Av_*(Z) applied to Z = V and Z = X are, functorially in the
G(O)-equivariant object V of a category acted on by G(K) at level kappa, the convolutions with two
objects K_1 = Av_*(delta_1) and K_2 = Av_*(Av_!^{I_1,psi} delta_1) of the category D_kappa(Gr)^{G(O)} of
G(O)-equivariant kappa-twisted D-modules on the affine Grassmannian, and u induces a morphism
a : K_1 -> K_2. It suffices that a is an isomorphism. (i) For kappa irrational every object of
D_kappa(Gr)^{G(O)} is supported at the base point 1: on the orbit of t^lambda, lambda a non-zero dominant
coweight, the torus T of the stabiliser acts on the fibre of the twisting through kappa(lambda, .), which
is not an integral character, so the orbit carries no non-zero equivariant twisted D-module. (ii) An
object supported at 1 is zero if its !-fibre at 1 vanishes. For Z in D_kappa(Gr)^H the !-fibre at 1 of
Av_*(Z) is C_dR(G(O)/H) (x) i_1^! Z = C_dR(G) (x) i_1^! Z, naturally in Z (de Rham cochains; i_1 the
inclusion of the base point). Finally Y = Av_!^{I_1,psi} delta_1 is the !-extension of the exponential
D-module from the orbit I_1 . 1 = I_1 / H, an affine space of dimension Delta containing 1, and by
adjunction and the full faithfulness of the !-extension from the orbit,

    i_1^! Y = RHom(delta_1, Y) = RHom(Y, Y) = C,

the unit u : delta_1 -> Y corresponding to the identity of Y. So u induces an isomorphism on !-fibres at 1,
the cone of a has zero !-fibre at 1, and it is zero.
Step 4. So DS_* is bijective, and it is multiplicative. Formality: DS_* is induced by a quasi-isomorphism
of the derived endomorphism dg algebras. Inflation from g-modules to smooth g[[t]]-modules (through the
evaluation t = 0) followed by induction to the affine algebra is an exact functor sending the trivial
module to V^k(g); it induces a homomorphism of dg algebras from the derived endomorphism algebra of the
trivial g-module to that of V^k(g), which on cohomology is the inclusion of the classes of constant loops,
an isomorphism (4.1). The derived endomorphism algebra of the trivial g-module is the algebra of cochains
of g, which is formal (it contains the algebra of invariant cochains, with zero differential, as a
quasi-isomorphic subalgebra). QED

Remarks. (1) Status: Steps 1-2 quote Raskin's theorems; Step 3 uses the standard formalism of categories
acted on by the loop group (the convolution description of averaging functors and base change). The
deduction is ours.
(2) The proof of Step 3 uses the irrationality of k only through (i), for the finitely many orbits meeting
the closure of G(O) I_1 . 1. So DS_* is an isomorphism for every non-critical k outside a set of
rational numbers with bounded denominators. E_g denotes the set of non-critical levels at which DS_* is not
an isomorphism; bounds for it are in 8.2.
(3) For g = sl_2 the source and the target are exterior algebras on one class of degree 3 at every
non-critical level (6.1), so DS_* is either an isomorphism or zero in positive degrees; by Proposition 7.4
it is zero exactly at tau = +-1.

COROLLARY 4.2. For every g: for all but finitely many k, dim Ext^n(W^k(g), W^k(g)) = dim H^n(g) for all n
(in particular the groups vanish for n > dim g); the exceptional levels are rational; and at every
non-critical level dim Ext^n >= dim H^n(g).

Proof. Theorem 4.1 and Proposition 3.4. QED

### 4.3 Two symmetries of the level, and the exceptional set

PROPOSITION 4.3 (Langlands dual level). For non-critical k let k^L be defined by
r^v (k + h^v)(k^L + h^v_L) = 1 (r^v the lacing number, g^L the Langlands dual Lie algebra). Then
W^k(g) = W^{k^L}(g^L) as vertex algebras (Feigin-Frenkel duality), so their vacuum self-Ext algebras
coincide. If k is outside E_g or k^L is outside E_{g^L} (Remark (2) of 4.2), then Ext^*(W^k(g), W^k(g))
is the exterior algebra on classes of degrees 2 m_i + 1. The levels k for which neither holds form a
finite set F_g of rational numbers.

Proof. Feigin-Frenkel duality holds at every non-critical level (Arakawa-Creutzig-Linshaw,
arXiv:1801.03822v4, Theorem 5.6). Its extension from generic levels can also be seen as follows:
both algebras are, through their Miura maps, saturated families of subalgebras of the same Heisenberg
algebra over C[tau, tau^{-1}] (1.5, Lemma 3.3); two saturated families that agree generically agree
fibre by fibre. The second statement is Theorem 4.1 with its Remark (2), applied to g or to g^L. E_g is
contained in (1/N)Z for some N: Step 3(i) involves finitely many orbits, and the orbit of t^lambda
carries an equivariant twisted D-module only if k (lambda, .) is integral on the coroot lattice. If
tau and 1/(r^v tau) both lie in lattices (1/N)Z + const, tau takes finitely many values. QED

PROPOSITION 4.4 (complementary level). For every k, with k' = -k - 2h^v (tau' = -tau), the algebras
Ext^*(W^k(g), W^k(g)) and Ext^*(W^{k'}(g), W^{k'}(g)) are anti-isomorphic as graded algebras; in
particular they have the same dimensions.

Proof. By Dhillon, Semi-infinite cohomology and the linkage principle for W-algebras, arXiv:1905.06477,
Theorem 5.12, the category W_{k'}-mod is canonically dual to W_k-mod, so the full subcategories of compact
objects are anti-equivalent, and End(c) is anti-isomorphic to End of the dual of c. By loc. cit.
Theorem 4.33, the dual of the image of a compact (I_1, psi)-equivariant object c_1 is the image of the
dual of c_1, shifted. The dual of the affine vacuum V^k(g) is the affine vacuum of the complementary
level (loc. cit. (5.8)); duality exchanges the !-average and the *-average to (I_1, +-psi)-equivariance
(loc. cit. Propositions 4.15, 4.22); and on the spherical vacuum the *-average and the !-average differ
by a shift (Raskin, Theorem 2.7.1(3)). So the dual of X = Av_! V^k(g) is the *-average of V^{k'}(g) to
(I_1, -psi)-equivariance, that is its !-average up to shift, whose image is the vacuum module of
W^{k'}(g) up to shift (the sign of psi is immaterial, Dhillon, Lemma 5.15). A shift does not change the
derived endomorphism algebra, and a contravariant equivalence reverses composition. QED

For g = sl_2, sl_3 Proposition 4.4 is visible on the paired complex, which is symmetric in its two
factors. Together the two propositions say that the set J_g of non-critical levels at which the
dimensions of Ext^*(W^k(g), W^k(g)) exceed those of H^*(g) is finite, contained in F_g, stable under
tau -> -tau, and that tau -> 1/(r^v tau) maps J_g onto J_{g^L}. The duality of Proposition 4.3 acts on the
type and the level together: for B_n and C_n, n >= 3, it relates two different Lie algebras; it maps
J_g to itself for the simply laced types and for B_2, G_2, F_4 (whose dual is isomorphic to g). The
identity W^k(g) = W^{k^L}(g^L) for all non-critical k is stated in Arakawa, arXiv:1605.00138, Remark 5.24.

## 5. The classical limit and the wedge algebra

### 5.1 A lemma on graded Lie algebroids

Let P = C[y_j] be a polynomial algebra on generators of positive integer weights, finitely many of each
weight, with augmentation ideal m. Let B_+ be a set of letters x with degrees deg x in Z, finitely many
of each degree, bounded below, and let C = P (x) Lambda[c^x : x in B_+] (finite polynomials), graded by
the number of c's and by the weight, wt(c^x) = deg x. Let D be a derivation of C of degree 1 preserving
weights with D D = 0, and write

    D f = sum_x rho_x(f) c^x  (f in P),      D c^z = -(1/2) sum_{x,y} f^z_{xy} c^x c^y,   f^z_{xy} in P.

(So (P, P (x) a_+) is a Lie-Rinehart algebra and C its cochain complex.) Assume:
(E) there is a letter x_0 of degree 0 with rho_{x_0} the weight derivation of P and
f^z_{x_0 y} = -deg(y) delta_{zy};
(T) for every weight w the pairing <x, y_j> = rho_x(y_j)(0) between the letters of degree w and the
generators of weight w has no kernel on the side of the generators.
Let g_0 be the space of the x in a_+ = span(B_+) with <x, .> = 0, with bracket
[x, y]_0 = sum_z f^z_{xy}(0) z.

LEMMA 5.1. g_0 is a Lie algebra (the isotropy algebra at the origin), the weight-zero part C_0 computes
H(C), and the restriction C -> Lambda(g_0^*) (y_j -> 0, cochains restricted to g_0) is a quasi-isomorphism
onto the Chevalley-Eilenberg complex of g_0. If C_0 is finite-dimensional, H^*(C) = H^*(g_0).

Proof. The identities expressing D D y_j = 0 and D D c^z = 0, evaluated at the origin on elements of g_0
(whose derivations rho_x vanish at the origin), give that g_0 is closed under [ , ]_0 and the Jacobi
identity. Let i be the derivation of C with i(c^x) = delta_{x, x_0}, i(P) = 0. By (E), D i + i D is the
derivation multiplying by the weight (check on generators), so C_w is acyclic for w non-zero; the same
holds for Lambda(g_0^*), as x_0 is in g_0. Choose a graded complement c of g_0 in a_+; by (T) it has a
basis (x_j) with <x_j, y_i> = delta_{ij}; let xi^j, gamma^a be the corresponding coordinates
(xi^j vanishing on g_0, gamma^a on c). Then eta_j = D y_j = xi^j + sum_x g_{j,x} c^x with g_{j,x} in m,
and since the g's have positive weight the substitution is triangular for the weights: the y_j, eta_j,
gamma^a are free generators of C. Let F^p be the span of the monomials with at least p factors among the
y's and eta's. D preserves F^p (D y = eta, D eta = 0, and F^0 = C), and on gr_F the differential is the
tensor product of the de Rham differential of C[y] (x) Lambda[eta], y -> eta, and of the derivation of
Lambda[gamma] with gamma^a -> -(1/2) sum f^a_{bc}(0) gamma^b gamma^c, the Chevalley-Eilenberg differential
of g_0. The polynomial de Rham complex is acyclic in positive weights and C in weight 0. On C_0 the
filtration is finite, so the spectral sequence converges; E_1 = H^*(g_0) is concentrated in filtration
degree 0, and the projection C -> C/F^1 = Lambda[gamma] is a quasi-isomorphism. It is the restriction
map. QED

### 5.2 The classical W-algebra

Let P be the classical W-algebra of g: the Poisson vertex algebra of functions on the space Op(D) of
g-opers on the formal disc, a polynomial algebra on the coefficients w^i_{-n}, n >= d_i, of the
generators w_i(z) = sum_n w^i_n z^{-n-d_i}; the letters are the w^i_n, B_+ the w^i_n with n > -d_i (the
functions on opers on the punctured disc that vanish on Op(D)); the Lie algebroid is the conormal Lie
algebroid of Op(D) in the Poisson ind-scheme of opers on the punctured disc:
rho_x(f) = {x, f} restricted to Op(D), and f^z_{xy} the coordinates of {x, y} modulo the square of the
ideal of Op(D) (Drinfeld-Sokolov, Lie algebras and equations of Korteweg-de Vries type; De Sole-Kac-Valeri,
Comm. Math. Phys. 323 (2013); Frenkel-Ben-Zvi, Chapter 15). The zero mode l_0 of the classical conformal
vector satisfies (E).

PROPOSITION 5.2. For the classical W-algebra, (T) holds, and the isotropy algebra g_0 at the origin of
Op(D) (the oper d + f) is isomorphic to g; it is the wedge algebra, spanned modulo terms vanishing at the
origin by the modes w^i_n, |n| <= m_i, and the degree n corresponds to the principal grading of g.

Proof. Opers on the disc are the connections d + f + v(t), v in b[[t]] (b the Borel subalgebra opposite
to f, n its nilradical), modulo the gauge action of N[[t]], and the Poisson structure is the Hamiltonian
reduction of the Kirillov-Kostant structure on connections on the punctured disc (Drinfeld-Sokolov).
Under the residue pairing the conormal space of Op(D) at the class of A = d + f + v is

    a_{+,A} = {xi in g[[t]] : xi' + [A, xi] in b[[t]]} / n[[t]],

with anchor xi -> xi' + [A, xi] modulo the tangent space of the N[[t]]-orbit, and the bracket of the gauge
algebroid: for sections xi, eta (functions of A),
[xi, eta]_A = [xi_A, eta_A] + (d eta)_A(rho xi) - (d xi)_A(rho eta), modulo n[[t]]. (The pointwise bracket alone
does not preserve the constraint: for sl_2 and A = d + f the elements f and t^2 f - t h satisfy it and
their pointwise bracket -2 t f does not.) At a point where the anchor of xi and of eta vanishes the
bracket is the pointwise one; this is the only case used. At A = d + f: the map xi -> xi' + [f, xi] of g[[t]] to itself is
surjective (solve the differential equation coefficient by coefficient), so the anchor is surjective
onto the tangent space b[[t]] / (n[[t]]-orbit) of Op(D); this is (T). Its kernel in a_{+,A} is the image
of the stabiliser {xi : xi' + [f, xi] = 0} = {exp(-t ad f) xi_0 : xi_0 in g}, a Lie subalgebra of g[[t]]
isomorphic to g meeting n[[t]] trivially (the action of N[[t]] is free). The grading by weights is
induced by t d/dt + ad rho^v, which acts on exp(-t ad f) xi_0 through the principal grading of xi_0; the
count of dimensions in each degree gives the description by modes. QED

(For g = sl_3 the statement, with the explicit classical W_3 algebra, is adopted with an exact machine
check in inscribe/fab-T96, item 4. The wedge algebra of a classical W-algebra was identified with g by
Feher, O'Raifeartaigh and Tsutsui, hep-th/9307190, (2.12) and (2.27). The conormal Lie algebroid of Op(D)
is identified with the Atiyah algebroid of the tautological G-bundle on Op(D) by Frenkel-Gaitsgory,
arXiv:math/0508382, Lemma 4.4.2 and Proposition 4.4.3; Proposition 5.2 and Theorem F below are
consequences of that identification, proved here directly.)

THEOREM F. For the classical W-algebra of g, H^*(C(P), D_cl) = H^*(g): the cohomology is concentrated in
weight zero and the restriction to the wedge algebra g is a quasi-isomorphism. The primitive classes are
the transgressions of the basic invariants (Casimirs) of the wedge algebra.

Proof. Lemma 5.1 and Proposition 5.2; C(P)_0 is finite-dimensional by Lemma 3.1. QED

### 5.3 The lattice of the classical limit

LEMMA 5.3 (Feigin-Frenkel). Let R = C[hbar]_(hbar), hbar = 1/(k + h^v). Inside the Heisenberg vertex
algebra over R with currents beta = hbar b, [beta lambda beta] = hbar ( | ) lambda, let V_R be the
intersection of the image of the Miura map of W^k(g) over C(k) with the R-lattice of normally ordered
differential polynomials in beta. Then V_R is a vertex algebra over R, free on the PBW monomials in
generators w_1, ..., w_r with w_i = P_i(beta) modulo fewer currents, all its operator products
[a lambda b] lie in hbar V_R[lambda], and V_R / hbar with the bracket hbar^{-1}[ , ] is the classical
W-algebra, embedded in C[J h] by the classical Miura map. For g = sl_N the w_i are the coefficients of
:prod_i ((1 - hbar) d + eps_i . beta):.

Proof. V_R is saturated, so it is free in each weight of the rank of W^k(g), and its special fibre embeds
in C[J h]. The fibre is killed by the classical limits of the screening operators, whose common kernel is
the classical W-algebra, of the same graded dimension (Feigin-Frenkel, Integrals of motion and quantum
groups, arXiv:hep-th/9310022; Frenkel-Ben-Zvi, Vertex algebras and algebraic curves, Chapter 15); so the
fibre is the classical W-algebra, a polynomial
algebra on the jets of generators w_i with symbols P_i, and lifts of the w_i give a PBW basis over R
(Nakayama). Operator products of the beta's are divisible by hbar. The formula for sl_N is 1.5 rescaled
(Arakawa, arXiv:1605.00138, Theorem 5.19). QED

### 5.4 The first-order term of the quantum differential

PROPOSITION 5.4. For the lattice V_R the differential of Proposition 2.7 (over R, as in Proposition 3.4)
can be chosen so that on C(V_R)

    D = hbar D_cl + O(hbar^2),

D_cl the differential of the Lie algebroid of 5.2. For every choice, D vanishes modulo hbar.

Proof. The fibre V_0 = P is commutative, so by Theorem A and the proof of Theorem 6.4 its self-Ext has in
each degree and weight the dimension of the whole space C^n(P)_w; hence the differential induced on
C(V_0) by any choice is zero. For letters x, y of B_+ write [x, y] = sum_z u^{xy}_z z, z in B_+, where
u^{xy}_z is hbar times a combination with coefficients in R of modes of normally ordered products (every
word of the expansion 1.3 of [x, y] ends with a letter of B_+: for x = W^i_m, y = W^j_n in B_+ the binomial
coefficient of (R) vanishes unless s <= m + d_i - 1, and then
m + n > s - d_i - d_j + 1 = -wt(P^{ij}_s), so the mode (P^{ij}_s)_{m+n} kills the vacuum; a word of creation
letters only has total degree at most minus the weight of the corresponding monomial of P^{ij}_s). Put

    d_1(e_omega) = sum_x eps(x, omega) x e_{omega - x} - sum_{x < y in omega} +- sum_z u^{xy}_z e_{omega - x - y + z}

(well defined in each P^beta, since z 1 = 0 in W^beta_N when tw_beta(z) > N). In d_1 d_1 the terms of
order hbar cancel: the square of the first sum is sum +-[x, y] e_{omega - x - y}, which is cancelled by
the cross terms in which z is removed; the remaining cross terms combine into commutators [x', u^{xy}_z],
of order hbar^2, and the square of the second sum is of order hbar^2. In the induction of Proposition 2.7
take y_1 = (second sum) + hbar^2 y_2, where y_2 solves d(y_2) = hbar^{-2} d(y_0 - (second sum)): the right
side is a cycle of the required degree and filtration, it is divisible by hbar^2 in the lattice (which is
saturated), and the solution y_2 over R exists by the strict exactness of the resolution over R
(Proposition 3.4). The resulting differential is congruent
to d_1 modulo hbar^2, and the dual of d_1 is hbar times the Chevalley-Eilenberg-Rinehart differential:
x m = hbar {x, m} modulo hbar^2 for m in P, and hbar^{-1} u^{xy}_z acts on P modulo hbar as the
multiplication by f^z_{xy}. QED

## 6. Rank one, rank two, and the critical level

### 6.1 g = sl_2

THEOREM 6.1. For every non-critical k, Ext^*_{S_k}(Vir^c, Vir^c) = Lambda(omega_3), deg omega_3 = 3,
c = 13 - 6 tau - 6/tau. The class omega_3 is represented by c^{-1} c^0 c^1 (the ghosts of L_{-1}, L_0, L_1),
the generator of the cohomology of the wedge algebra sl_2 = <L_{-1}, L_0, L_1>.

Proof. By Remark 2.9(1) and Proposition 3.2, Ext^n = H^n of the weight-zero part of the
Chevalley-Eilenberg complex of a_+ = <L_n, n >= -1> with coefficients in Vir^c. Ghosts c^n have weight
n >= -1 and Vir^c has no vector of weight 1, so C(V)_0 = span{1, c^0, c^{-1}c^1, c^{-1}c^0c^1}, with
D(c^0) = 2 c^{-1}c^1 and D = 0 on the other three vectors. QED (This is also adopted in inscribe/ast-T81
and inscribe/fab-T71. The complex is that of Bakalov-Kac-Voronov, Cohomology of conformal algebras,
arXiv:math/9803022, Theorem 6.1, for the annihilation algebra of the Virasoro conformal algebra; their
Theorem 7.1 is the computation with trivial coefficients, dimension one in degrees 0 and 3. The statement
for the vacuum module in all smooth modules, at every c, is the case g = sl_2 of Theorem A with
Proposition 3.2.)

### 6.2 g = sl_3

THEOREM 6.2. For every non-critical k (k + 3 non-zero), with c = 50 - 24(tau + 1/tau):
(a) Ext^*_{S_k}(W^k(sl_3), W^k(sl_3)) = Lambda(eta_3, eta_5), with deg eta_3 = 3, deg eta_5 = 5, as a graded
algebra; in particular eta_3 eta_5 is non-zero in degree 8.
(b) It is computed by the paired complex: for M in S_k let K(M) = M (x) W^{k'}(sl_3) (x) F_gh, k' = -k - 6
(central charge 100 - c), F_gh the Fock space of the ghost pairs of weights (2, -1) and (3, -2), with
Q = Res j, j the current of Bershadsky-Lerche-Nemeschansky-Warner (hep-th/9207067, (2.2)) and
Bouwknegt-McCarthy-Pilch (hep-th/9509119, Theorem 3.2 and (3.9)):
j = c^2(T_1 + T_2 + T_gh,2/2 + T_gh,3) + c^3(U_1 + U_2) + (T_1 - T_2) b^2 c^3 dc^3 - mu b^2 dc^3 d^2c^3
+ (2/3) mu b^2 c^3 d^3c^3, mu = (c - 50)/32. Here U_1 is the generator of 1.6 at central charge c and
U_2 is i times the generator of 1.6 at central charge 100 - c, so that
[U_{2,m}, U_{2,n}] = -(m - n)(Lambda_{2,m+n} + A' a(m, n) L_{2,m+n}) - A' ((100 - c)/360) m(m^2-1)(m^2-4) delta_{m+n,0},
A' = (522 - 5c)/16 (the convention eps = -1 of the adopted records for the second factor; all structure
constants remain polynomial in c). With the generator of 1.6 itself in the second factor the term is
c^3(U_1 +- i U_2); the sign of the self-commutator of U_2 is forced by the cancellation of the terms
c^3 dc^3 :T_2 T_2: in Q^2. Then H^n(K(M)) = Ext^n_{S_k}(W^k(sl_3), M) naturally, and
the product of vertex operators on H^*(K(V)) corresponds to the opposite of the Yoneda product (which is
the same algebra, being graded commutative).
(c) The diagram automorphism sigma (U -> -U) fixes eta_3 and negates eta_5. The derived endomorphism
algebra is formal as an associative A-infinity algebra (nothing is claimed about formality for other
structures). With G = b^2_{-1}, [Q, G] = T, the reduced cohomology
H^*(K(V)/T K(V)) has dimension one in degrees 0, 2, 3, 4, 5, 7, 8, spanned by the classes of
1, G eta_3, eta_3, G eta_5, eta_5, G(eta_3 eta_5), eta_3 eta_5.

Proof. For c different from -22/5: (b) is the comparison theorem adopted in inscribe/fab-T96 (it is
Theorem A for sl_3 together with the homological perturbation through the second factor); the ring of
the paired complex is adopted in inscribe/ast-T96, over Q[c] and at every specialisation, with polynomial
representatives a_3 and xi_5; (c) is adopted in inscribe/fab-T96, items 1 and 2. All these statements are
about the polynomial family of vertex algebras with the relations 1.6, whose fibre at c is W^k(sl_3) for
c different from -22/5. At c = -22/5 (k + 3 = 3/5 or 5/3): by 6.3 the fibre of the polynomial family is
still W^k(sl_3); Theorem A applies to it; the proofs of the adopted comparison use the relations 1.6
only through their polynomial form and the PBW basis, so they apply to this fibre; and the adopted ring
computation includes this specialisation. As a direct check, the one-sided complex C(V)_0 has cohomology
of dimensions (1, 0, 0, 1, 0, 1, 0, 0, 1) at c = -22/5 and at c = 522/5, 2, 98, 50, 0, -10, 110
(scripts/w3_onesided_cohomology.py, exact arithmetic). QED

Two corrections to the source record frontier/fable/T96 are incorporated (see SUPERSEDED.md): its
statement that monomials ordered by an arbitrary total order of the modes form a topological basis of the
completed mode algebra is false (reordering L_{-k} L_k produces coefficients (k^3 - k)/6 that do not tend
to zero); only the orders by twisted degree are needed, and in the present text no completed algebra and
no topological basis is used at all (Lemmas 2.3, 2.4 give bases of the modules W_gamma, W^beta_N for
every twisted order). And the coefficient of Lambda is 16/(22 + 5c) in the commutator of modes and
32/(22 + 5c) at the double pole of the operator product (1.6).

### 6.3 The fibre of central charge -22/5

PROPOSITION 6.3. Let X be the quasi-primary field of weight 3 in the image of the Miura map of sl_3:
with currents J^a, <J^a(z) J^b(0)> = delta^{ab}/z^2, and
:(a d + h_1.J)(a d + h_2.J)(a d + h_3.J): = (a d)^3 + U_2 (a d) + U_3 (h_i the weights of the fundamental
representation), T = -U_2 has central charge c = 2 - 24 a^2 and X = U_3 + (a/2) dT. Then

    <X(z) X(0)> = c (22 + 5c) / (144 z^6).

Consequently U = sqrt(3) X satisfies the relations 1.6 for every a, and the polynomial family of 1.6 is
the family W^k(sl_3), a^2 = tau + 1/tau - 2, at every non-critical level, including c = -22/5.

Proof. The two-point function is computed by Wick contraction (scripts/miura_sl3_norm.py: exact in a;
output N = (12a^2 - 1)(15a^2 - 4)/9 = c(22 + 5c)/144, and s = a/2). For c(22 + 5c) non-zero the vertex
algebra generated by T and a primary field of weight 3 with two-point function N/z^6 is the W_3 algebra
with W = X (c/(3N))^{1/2}, so [X_m, X_n] contains (16/(22 + 5c))(3N/c)(m - n) Lambda_{m+n} =
(1/3)(m - n) Lambda_{m+n} and U = sqrt(3) X satisfies 1.6. The coefficients of the PBW expansion of
[X_lambda X] in T, X are rational functions of a without poles (T and X generate a PBW basis of the image
of the Miura map for every a: 1.1, 1.5), hence polynomials, and they agree with those of 1.6 on a dense
set. The image of the Miura map is W^k(sl_3) for every k (Arakawa, arXiv:1605.00138, Theorems 5.17 and
5.19). QED

So the universal algebra is regular at c = -22/5: the two-point function of the generator of weight 3
vanishes there (the generator is null in the simple quotient), but the universal algebra, its PBW basis
and the complex C are those of the polynomial family. (The regular presentation at c = -22/5 is in
Hull-Palacios, hep-th/9206031, (4)-(6), and Al-Ali-Linshaw, arXiv:1608.06255, (3.3)-(3.5): for all c the
universal algebra is freely generated by L and a rescaled W.) That the vacuum self-Ext is still
Lambda(eta_3, eta_5) there is Theorem 6.2. The analogue for general g: the levels where the two-point form on the
generators of some weight degenerates; Theorem A, Proposition 3.4 and Corollary 4.2 do not see them, since
they never normalise generators by two-point functions.

### 6.4 The critical level

THEOREM 6.4. Let tau = 0. Then V = W^{-h^v}(g) is commutative (it is the centre of the affine vertex
algebra: Feigin-Frenkel; Arakawa, W-algebras at the critical level, arXiv:1111.6329, Theorem 1.1), all letters commute on every object of S_k, the differential of Proposition 2.7
can be taken to be the Koszul differential, and

    Ext^n_{S_k}(V, V) = C^n(V) = V (x) Lambda^n_cont(a_+^*)       for every n >= 0,

with D = 0. (Adopted as item D4 of inscribe/fab-T53.)

Proof. The vectors P^{ij}_s vanish, so (R) says that letters commute; the Koszul formula
d(e_omega) = sum eps(x, omega) x e_{omega - x} then satisfies Proposition 2.7(i), (ii). So
D(m c^omega) = sum_{x not in omega} +- x m c^{omega + x}, and for m = a|0> in V and x in B_+,
x m = a x |0> = 0. QED

At the critical level there is no operator L_0 (Proposition 3.2 fails), all weights contribute, and every
Ext^n is infinite-dimensional: the answer jumps from dimension 2^r to infinity. In the family of levels
with generators normalised as in Lemma 3.3 the differential of C(V_k) vanishes at tau = 0. The proof of
Proposition 5.4 uses only that the special fibre is commutative and that the operator products of the
lattice are divisible by the uniformiser; applied to W_A localised at tau = 0 it gives
D = tau D_1 + O(tau^2), D_1 the differential of the Lie algebroid of annihilation modes of the Poisson
vertex algebra (centre, tau^{-1}[ , ] at tau = 0). This Poisson vertex algebra is the classical
W-algebra of the Langlands dual Lie algebra, with its bracket multiplied by the lacing number r^v: by
Feigin-Frenkel duality (Proposition 4.3) the family W^k(g) near tau = 0 is the family W^{k^L}(g^L) near
hbar_L = (k^L + h^v_L)^{-1} = r^v tau = 0; both are, through their Miura maps, saturated lattices in the same
Heisenberg lattice over the local ring at tau = 0 (for the first by the injectivity of the Miura map on
every fibre, Arakawa, arXiv:1605.00138, Theorem 5.17 and Remark 5.18; for the second by Lemma 5.3), with
the same generic fibre, hence they coincide, and so do their first-order brackets up to the factor r^v.
(The centre with the Poisson structure obtained by varying the affine level is identified with the same
classical W-algebra in Frenkel, arXiv:math/0210029, Theorems 9.8 and 11.3.) So by Theorem F the second
page of the Bockstein spectral sequence at the critical level (all weights) is H^*(g^L), an exterior
algebra on classes of degrees 2 m_i + 1: it already has the size of the non-critical answer.

## 7. The first case beyond rank two: W_4, and the test differential

### 7.1 What the test is, and what it needs

For g = sl_4 the classical answer H^*(sl_4) = Lambda(theta_3, theta_5, theta_7) lives in degrees
0, 3, 5, 7, 8, 10, 12, 15. The only two adjacent degrees are 7 and 8 (theta_7 and theta_3 theta_5). A
quantum correction to the classical computation can therefore only be a map from degree 7 to degree 8.
For this map to be defined one needs the following, for g = sl_4 or any g; R = C[hbar]_(hbar) is the
local ring of the classical limit, hbar = 1/(k + h^v).

(1) A lattice: a vertex algebra V_R over R, free as an R-module on PBW monomials in generators
w_1, ..., w_r of weights d_i, with V_R (x) C(hbar) = W^k(g) over C(k), all operator products
[w_i lambda w_j] divisible by hbar, and special fibre the classical W-algebra P of g with the Poisson
vertex structure hbar^{-1}[ , ]. This is Lemma 5.3. For sl_N it is explicit: the coefficients of the
Miura operator :prod_i ((1 - hbar) d + eps_i . b): in currents b with [b lambda b] = hbar lambda.
(2) A complex: by Proposition 3.4 over R, a complex K = C(V_R)_0 of free R-modules of finite rank whose
generic fibre computes Ext^n(W^k(g), W^k(g)) over C(k). Its differential vanishes modulo hbar and can be
chosen congruent modulo hbar^2 to hbar D_cl, D_cl the differential of the Lie algebroid of annihilation
modes of P (Proposition 5.4).
(3) The classical computation: H^*(C(P)_0, D_cl) = H^*(g) (Theorem F).

Given (1)-(3), the test is a differential of the Bockstein spectral sequence of K, which is defined as
follows for any bounded complex K of free R-modules of finite rank. By the theory of elementary divisors
applied to the differentials one after the other, K is a direct sum of complexes of two kinds: R placed in
one degree n, and R -> R placed in degrees n, n+1 with differential hbar^a, a >= 0. Let Z_s^n be the set of
x in K^n / hbar with a lift x~ in K^n such that D x~ is divisible by hbar^s, and B_s^n the set of the
reductions of the elements hbar^{-(s-1)} D y, y in K^{n-1}, D y divisible by hbar^{s-1}; put
E_s^n = Z_s^n / B_s^n (s >= 1) and beta_s : E_s^n -> E_s^{n+1}, beta_s[x] = [hbar^{-s} D x~]. These are
well defined, beta_s beta_s = 0, E_{s+1} = H(E_s, beta_s), E_1 = H^*(K / hbar), and everything is functorial
for morphisms of complexes over R (this is the spectral sequence of the exact couple of
0 -> K -> K -> K / hbar -> 0; Weibel, An introduction to homological algebra, 5.9.9-5.9.12, for the
integers and a prime). On the decomposition: a summand R in degree n contributes one dimension to E_s^n
for all s; a summand with differential hbar^a contributes to E_s^n and E_s^{n+1} exactly for s <= a, and
beta_a maps the one onto the other. Hence beta_s = 0 for s large and

    dim E_infinity^n = rank_R H^n(K) = dim_{C(hbar)} H^n(K (x) C(hbar)),

and beta_s = 0 for all s >= s_0 if and only if the torsion of H^*(K) is killed by hbar^{s_0 - 1}.

For K = C(V_R)_0: the differential vanishes modulo hbar, so E_1 = C(P)_0 and beta_1 is the reduction of
hbar^{-1} D, that is D_cl (Proposition 5.4); E_2 = H^*(C(P)_0, D_cl) = H^*(g) (Theorem F); the
differentials are beta_s : E_s^n -> E_s^{n+1}, s >= 2; and dim E_infinity^n is the dimension of
Ext^n(W^k(g), W^k(g)) over C(k) at the generic level. The test differential for sl_4 is
beta_s : E_s^7 -> E_s^8, s >= 2. (The filtration of K by powers of hbar has a different spectral sequence,
which does not compute the generic fibre: for K = (R -> R) with differential 2 hbar its abutment is the
torsion module R / hbar.)

### 7.2 The result

THEOREM 7.1. For every simple g all the differentials beta_s, s >= 2, of the Bockstein spectral sequence
of 7.1 vanish; equivalently, hbar^{-1} D is a differential on C(V_R)_0 whose cohomology is a free R-module
with special fibre H^*(g). In particular for sl_4 the map from degree 7 to degree 8 is zero, and for all but finitely many k

    dim Ext^n(W^k(sl_4), W^k(sl_4)) = 1 for n = 0, 3, 5, 7, 8, 10, 12, 15, and 0 otherwise.

Proof. dim E_infinity^n is the generic dimension, which is dim H^n(g) = dim E_2^n by Corollary 4.2; so
E_infinity = E_2. For the equivalent form: D = hbar D' with D' D' = 0 (K is torsion free), the special fibre
of (K, D') is (C(P)_0, D_cl), and the summands of (K, D') are those of (K, D) with a lowered by one. QED

PROPOSITION 7.2 (independent of Section 4). For g = sl_4 the differential beta_s : E_s^7 -> E_s^8 vanishes
because of the diagram automorphism. Hence the dimension statement of Theorem 7.1 for sl_4 holds without
appeal to the theorems of Raskin.

Proof. The diagram automorphism of sl_4 induces an automorphism sigma of V_R acting on the generator of
weight d by (-1)^d (generators can be chosen as eigenvectors); the choices in Proposition 2.7 form affine
spaces stable under sigma, so the differential of K can be chosen sigma-equivariant, and then sigma acts
on the Bockstein spectral sequence (functoriality). On E_2 = H^*(sl_4), identified by restriction to the wedge algebra
(Theorem F), sigma acts through the diagram automorphism X -> -X^t (it acts on the summand of dimension
2d - 1 of the wedge algebra by (-1)^d, as the diagram automorphism fixing a principal sl_2 does), hence by
(-1)^d on the primitive class of degree 2d - 1. So sigma acts by +1 on theta_7 (d = 4) and by -1 on
theta_3 theta_5 (d = 2, 3), and an equivariant map E_s^7 -> E_s^8 is zero. As 7 and 8 are the only adjacent
degrees of E_2, all beta_s, s >= 2, vanish; the spectral sequence degenerates,
the generic dimensions are those of H^*(sl_4), and Proposition 3.4 applies. QED

Remarks. (1) For sl_2 and sl_3 there are no adjacent degrees and no test: this gives the dimension
statement at generic level without computation. (2) For general g the same parity argument, applied to all
pairs of adjacent degrees, decides some cases and not others; Theorem 7.1 covers all. (3) What Theorem 7.1
does not give is the list of the finitely many exceptional levels of sl_4 (rational by Corollary 4.2),
nor the algebra structure at rational levels.

### 7.3 What is not constructed for g beyond sl_3

A paired BRST complex. For sl_3 the complex C(M) is a contraction of K(M) = M (x) W^{k'} (x) F_gh
(Theorem 6.2(b)); the differential Q = Res j is a closed formula and the product of H^*(K(V)) is induced
by the vertex algebra structure of V (x) W^{k'} (x) F_gh. For g = sl_4 (and B_2) BRST currents are in the
physics literature (Hornfeck, hep-th/9306019; Zhu, hep-th/9306026); for general g no current is known
to us. Theorem A replaces it: the complex C(M) exists for every g, and Ext^*(V, V) carries the Yoneda
product. A complex K(M) with a vertex-algebra product for general g would be given by a nilpotent element
Q = sum_i c^i (W^i (x) 1 + 1 (x) W'^i) + (terms with antighosts) of W^k(g) (x) W^{k'}(g) (x) F_gh of
ghost number one, k' = -k - 2h^v; the vanishing of the total central charge is necessary; existence for
general g is open (OPEN.md, O3).

### 7.4 The constants of the reduction map

For every non-critical k the classes eta_i(k) = DS_*(theta_i) are defined (4.1), and for irrational k they
generate (Theorem 4.1).

PROPOSITION 7.4 (rank one; computed). For g = sl_2 and tau = k + 2 non-zero, with
theta_3 = c^{e,0} c^{h,0} c^{f,0} and omega_3 = c^{-1} c^0 c^1,

    DS_*(theta_3) = -(1/2)(1 - tau^{-2}) omega_3.

So DS_* is an isomorphism for tau different from +-1 and is zero in positive degrees at tau = +-1
(c = 1 and c = 25), where Ext^*(Vir^c, Vir^c) is nevertheless Lambda(omega_3) (Theorem 6.1).

Proof (a computation, made by the other model family: REQUESTS/4-calc.ANSWER.md, with the identities
displayed in REQUESTS/4-calc.d/DERIVATION.md). Let P_q = (U_k / U_k t sl_2[[t]]) (x) Lambda^q sl_2,
0 <= q <= 3, be the resolution of V^k(sl_2) induced from the Chevalley-Eilenberg resolution of the trivial
sl_2-module; the map f_3 : P_3 -> V^k, f_3(a (x) x ^ y ^ z) = tr(x[y, z]) a|0>, represents
-2 theta_3. The image of the class under the morphism of delta-functors DS_* is computed by lifting
the identity of the reduced vacuum through the Drinfeld-Sokolov complex against the Koszul resolution of
the Virasoro side: elements z_0 = 1 (x) |0>, z_1, z_2, z_3 with d z_{q+1} = D z_q are written explicitly
for all tau non-zero, and

    f_3(z_3) = (1 - tau^{-2}) omega + (1/(2 tau)) D(H u v),

H = h_{-1}, u = c^{-1}, v = c^0. The identities were verified symbolically in an independent realisation
with tau and the highest weight indeterminate, and numerically at eight levels. QED

This agrees with the class of the reduced family computed in inscribe/fab-T125
(-(1/2)(1 - tau^{-2}) [omega_3] = (dc/dk)/12 [omega_3], c = 13 - 6 tau - 6/tau, Dhillon,
arXiv:1905.06477, (9.15)). Consequences: the exceptional set of Remark (2) of 4.2 is
E_{sl_2} = {tau = 1, tau = -1}; the bound by integrality of the twisting (Proposition 4.3) only gives
tau in (1/2)Z, so that bound is not sharp; and at tau = +-1 the generator of Ext^3(Vir^c, Vir^c) is not the
reduction of a class of H^3(sl_2) at that level, from either side of the Feigin-Frenkel duality
(tau = +-1 is fixed by tau -> 1/tau up to sign).

### 7.5 A singular family (the routed lead R073)

All families used above (Lemma 3.3 over C[k], the lattice V_R of 7.1) are free modules with PBW bases,
and the complexes are complexes of free modules whose fibres are the complexes C of the fibre algebras;
no quotient by a vertex ideal is taken, so no derived correction of the kind found in the lead arises.
The lead's lattice is of the same type: inside W_3 over C((t)) with c = c_0 t^{-4}, c_0 non-zero, the
vectors l = t^3 L, u = t^2 W generate a free C[[t]]-lattice V_S with PBW basis and special fibre
V_0 = C[l, dl, ...] (x) H^{(5)}, l central, [u_nu u] = (c_0/360) nu^5.

PROPOSITION 7.3. Ext^*_{smooth}(V_0, V_0) = C[l_{-n}, n >= 2] (x) Lambda_cont(l_n^*, n >= -1)
(x) Lambda(u_n^*, |n| <= 2), infinite-dimensional in every degree, whereas the generic fibre of the same
lattice has Ext^* = Lambda(eta_3, eta_5).

Proof. V_0 is the vacuum module of a Lie conformal algebra with central extension, so its vacuum self-Ext
is the continuous cohomology of the Lie algebra a_+ spanned by l_n (n >= -1) and u_n (n >= -2) with
coefficients in V_0 (inscribe/fab-T53, Lemma E; or Theorem A). a_+ is abelian (the central term of
[u_m, u_n] is a multiple of binom(m + 2, 5) delta_{m+n,0}, zero for |m| <= 2); the l_n act by zero; u_n
acts by zero for |n| <= 2 and as a non-zero multiple of the derivative with respect to u_{-n} for
n >= 3. The cochain complex is the tensor product of the de Rham complex of the polynomial ring in the
u_{-n}, n >= 3, with the displayed exterior algebras with zero differential. QED

So the vacuum self-Ext of the fibres of this lattice jumps at t = 0, as upper semicontinuity allows, and
the statement at fixed level says nothing about the special fibre; the relation between the two is the
base-change sequence 0 -> H^n(K_S) (x) C -> H^n(K_0) -> Tor_1(H^{n+1}(K_S), C) -> 0 for the complex K_S of
free C[[t]]-modules. The lead's correction (the derived quotient of V_S by the vertex ideal of l has an
extra class in degree -1 which the Koszul complex of the special fibre misses) applies to constructions
that set the stress tensor to zero; quantum Drinfeld-Sokolov reduction, as used in 4.1, is the cohomology
of a complex of free modules and involves no such quotient.

## 8. Rational levels: what is proved and what is computed

### 8.1 g = so_5 at every non-critical level

THEOREM 8.1 (computed). For g = so_5 and every non-critical k (tau = k + 3 non-zero),

    dim Ext^n_{S_k}(W^k(so_5), W^k(so_5)) = 1 for n = 0, 3, 7, 10, and 0 otherwise,

the dimensions of H^*(so_5). More precisely, over A' = C[tau, tau^{-1}] the cohomology of the complex
C(W_{A'})_0 of Proposition 3.4 is a free A'-module of rank one in each of the degrees 0, 3, 7, 10 and zero in
the other degrees; so the set J_{so_5} of 4.3 is empty.

Proof (a computation, made by the other model family: REQUESTS/3-calc.ANSWER.md, data and scripts in
REQUESTS/3-calc.d). The algebra is realised by the Miura map in the Heisenberg algebra
[b^i_m, b^j_n] = tau m delta_{ij} delta_{m+n,0}, with generators of weights 2 and 4 whose coefficients are
polynomials in tau (the generator of weight 2 is tau L, as in Lemma 3.3; the generator of weight 4 has
symbol (b^1)^2 (b^2)^2 and is not normalised by its two-point function). The integral Miura image is
identified using the intersection statement of Arakawa-Creutzig-Linshaw, arXiv:1801.03822v4,
Lemma 5.1, with the screening description of Lemma 5.4 and Proposition 5.5; the integral
intersection, rather than generic screening equality alone, fixes the rational fibres. All operator products are computed
by Wick contraction and have coefficients in Q[tau], divisible by tau. The complex C(V)_0 has terms of
dimensions 1, 4, 27, 103, 231, 346, 363, 261, 118, 30, 4 (degrees 0 to 10; 1564 exterior generators). Its
differential is constructed over Q[tau] by the lifting of Proposition 2.7 with beta = 0, using the
contracting homotopy of the Koszul complexes (integer denominators only); D D = 0 is checked as an
identity of polynomial matrices. Each matrix D_q is reduced over Q[tau, tau^{-1}], by row and column
operations that are invertible over that ring, to an identity block of size 0, 4, 23, 79, 152, 194, 169,
91, 27, 3 (q = 0, ..., 9) and zeros; the sequence of operations is saved and was replayed by a second
implementation. So the images are direct summands and the cohomology over A' is free of the stated ranks.
Theorem A and Proposition 3.2 identify the cohomology of the fibre at tau_0 with Ext. Controls: the same
code gives 1, 0, 0, 1 for sl_2 and 1, 0, 0, 1, 0, 1, 0, 0, 1 for sl_3 at six central charges, and D = 0
at tau = 0. QED

COROLLARY 8.2. For g = so_5: Ext^*(W^k, W^k) is the exterior algebra Lambda(eta_3, eta_7) for every
non-critical k outside the finite set F_{so_5} of Proposition 4.3; at the levels of F_{so_5} it has the same
dimensions, and it is exterior if and only if the product Ext^3 x Ext^7 -> Ext^10 is non-zero there. Over
A' the product is p(tau) times a generator, with p a Laurent polynomial whose zeros lie in F_{so_5}; they
form a set stable under tau -> -tau and tau -> 1/(2 tau). By Theorem 8.6 below, p is a unit.

Proof. Theorem 4.1, Propositions 4.3 and 4.4 (so_5 is isomorphic to its Langlands dual sp_4, r^v = 2), and
Theorem 8.1; the Yoneda product is defined over A' and the three cohomology modules are free of rank
one. QED

### 8.2 The two kernels, and a bound for the exceptional set

Notation of the proof of Theorem 4.1: kappa the level, Gr the affine Grassmannian, delta_1 the delta
D-module at the base point, Y = Av_!^{I_1,psi} delta_1, K_1 = Av_* delta_1, K_2 = Av_* Y (Av_* the
*-average to G(O)-equivariance), a : K_1 -> K_2 induced by the unit u.

PROPOSITION 8.3 (every level). For every k and n,

    Ext^n_{S_k}(W^k(g), W^k(g)) = Hom(V^k(g), K_2 * V^k(g)[n]),      H^n(g[[t]], V^k(g)) = Hom(V^k(g), K_1 * V^k(g)[n]),

Hom in the category of G(O)-equivariant objects, and DS_* is induced by a. The cone K' of a is a bounded
holonomic G(O)-equivariant twisted D-module supported on the union of the orbits Gr^lambda, lambda in
Lambda_1, where Lambda_1 is the set of non-zero dominant lambda in the coroot lattice with lambda <= 2 rho^v
such that Gr^lambda meets the closure of G(O) I_1 . 1. Consequently there is a long exact sequence

    ... -> H^n(g) -> Ext^n(W^k(g), W^k(g)) -> Hom(V^k, K' * V^k[n]) -> H^{n+1}(g) -> ...    (k non-critical).

Proof. Steps 2 and 3 of the proof of Theorem 4.1, which hold at every level, give the two formulas and
the vanishing of the !-fibre of K' at the base point. The orbit I_1 . 1 consists of the points
t^{-rho^v} n t^{rho^v} G(O), n in N(O), which lie in the convolution of the closures of two orbits of
coweight rho^v (in the adjoint group); so only lambda <= 2 rho^v occur, and the points of N(K) . 1 lie in
the component of the base point. QED

For a coweight lambda let sigma_lambda be the automorphism of the affine algebra at level k

    x (x) t^n -> x (x) t^{n + <alpha, lambda>}  (x a root vector of weight alpha),
    h (x) t^n -> h (x) t^n + k (lambda, h) delta_{n,0}  (h in the Cartan subalgebra),

and V^k_{(lambda)} the pull-back of the vacuum module by sigma_lambda (spectral flow). It is generated by the
vector v_lambda = |0>, with (x (x) t^n) v_lambda = 0 for x of weight alpha and n >= -<alpha, lambda>,
(h (x) t^n) v_lambda = 0 for n > 0 and h v_lambda = k (lambda, h) v_lambda. For g = sl_2 and lambda = alpha^v:
e_n v = 0 for n >= -2, f_n v = 0 for n >= 2, h_0 v = 2k v, consistently with
[e_{-2}, f_2] = h_0 - 2k. Up to the action of G(O) and the replacement of lambda by a Weyl conjugate or by
its negative (which changes neither condition of Proposition 8.4(b)), V^k_{(lambda)} is the module of
sections of the delta D-module at the point t^lambda of the orbit Gr^lambda. Let iota(lambda) = (lambda, .) in
h^*, and Q the root lattice.

PROPOSITION 8.4. (a) If H^*(g[[t]], V^k_{(lambda)}) = 0 for every lambda in Lambda_1, then DS_* is an
isomorphism at the level k.
(b) For k non-critical, H^*(g[[t]], V^k_{(lambda)}) = 0 unless k (lambda, lambda)/2 is an integer and
k iota(lambda) lies in Q.
(c) Hence E_g is contained in the set of k for which some lambda in Lambda_1 satisfies the two conditions
of (b). For g = sl_2: Lambda_1 = {alpha^v}, the conditions say that k is an integer, so E_{sl_2} is
contained in Z and, by Proposition 4.3 (tau and 1/tau both integers), F_{sl_2} is contained in
{tau = 1, tau = -1}; by Proposition 7.4, E_{sl_2} = {tau = 1, tau = -1} exactly. For g = sl_3: Lambda_1 is contained in {theta^v, 3 omega_1^v, 3 omega_2^v, 2 theta^v},
E_{sl_3} is contained in (1/2)Z, and F_{sl_3} in {tau = +-1/2, +-1, +-2}.

Proof. (a) By Proposition 8.3 it suffices that Hom(V^k, F * V^k[n]) = 0 for every G(O)-equivariant F
supported on the orbits Gr^lambda, lambda in Lambda_1. Such an F is a finite extension of objects
j_{lambda,*} E, E an equivariant object on the orbit Gr^lambda = G(O)/S_lambda. The category of equivariant
objects on the orbit is generated under colimits and shifts by the *-average of the delta module at one
point: the stabiliser S_lambda is an extension of a connected reductive group L by a pro-unipotent group, the
equivariant category on the orbit is the category of modules over the algebra of chains of L (an exterior
algebra; Drinfeld-Gaitsgory, On some finiteness questions for algebraic stacks, 7.2.2-7.2.4), the pull-back
to the point is the forgetful functor, and its right adjoint sends C to the linear dual of the regular
module, which is a shift of the regular module (an exterior algebra is a Frobenius algebra). V^k is compact
in the renormalised category of Section 4 (Raskin, Remark 4.3.2), and convolution and the push-forward
from a stratum commute with colimits; and
Hom(V^k, Av_*(delta_{t^lambda}) * V^k[n]) = Hom(V^k, V^k_{(lambda)}[n]) in the category of all objects,
which is H^n(g[[t]], V^k_{(lambda)}) (Step 1 of the proof of Theorem 4.1).
(b) On V^k_{(lambda)} the Sugawara operator is L_0 + lambda_0 + k (lambda, lambda)/2 in terms of the operators of
V^k, with lambda_0 the zero mode of lambda in h; so it is diagonalisable with eigenvalues in
k (lambda, lambda)/2 + Z, and h acts diagonalisably with weights in k iota(lambda) + Q. For a smooth module M of
the affine algebra at a non-critical level, continuous cochains of g[[t]] with values in M compute the
derived functors of the invariants (a universal delta-functor: a finite cocycle with values in a
coinduced smooth module lies in the coinduced complex of a quotient of g[[t]] by a congruence subalgebra,
and induction from g[[t]] is exact, so restriction preserves injectives). The operator
Theta = (L_0 on M) + (degree of the cochain) is a natural endomorphism of this complex ([L_0, x_n] = -n x_n),
and it is zero on the invariants (a vector killed by g[[t]] has Sugawara energy zero); a morphism of
universal delta-functors is determined in degree zero, so Theta is zero on cohomology. The action of an
element h of the Cartan subalgebra on the complex is homotopic to zero (contraction with h). Degrees of
cochains are integers and their weights lie in Q. So for M = V^k_{(lambda)} the cohomology is computed by the
subcomplex of total energy zero and total weight zero, which is zero unless the two conditions hold.
(c) For sl_2, (alpha^v, alpha^v) = 2 and iota(alpha^v) = alpha. For sl_3 the non-zero dominant elements of the
coroot lattice below 2 rho^v = 2 theta^v are the four listed, with (lambda, lambda)/2 = 1, 3, 3, 4;
iota(lambda) is primitive in Q for the first three, and equal to 2 theta for the last. QED

COROLLARY 8.5 (the levels left open). (a) For g = sl_n: every lambda in Lambda_1 is m mu with mu primitive in
the coroot lattice and 1 <= m <= n - 1, so E_{sl_n} is contained in the union of the (1/m)Z, m <= n - 1, and

    F_{sl_n} is contained in { tau = +-a/b : 1 <= a, b <= n - 1, a and b coprime }.

(b) For g = sl_4: Ext^*(W^k(sl_4), W^k(sl_4)) is the exterior algebra on classes of degrees 3, 5, 7, and the
derived endomorphism algebra is formal, for every non-critical level except possibly the fourteen levels
tau = +-1, +-2, +-1/2, +-3, +-1/3, +-3/2, +-2/3 (central charges 3, 243; -27, 273; -77, 323; -7, 253), which
form four orbits under tau -> -tau, tau -> 1/tau.
(c) For g = so_5: Lambda_1 is contained in {(1,1), (2,0), (2,2), (3,1), (3,3), (4,0), (4,2)} (coordinates in
which the coroot lattice is {x in Z^2 : x_1 + x_2 even}), and E_{so_5} is contained in
(1/2)Z, (1/3)Z, (1/4)Z; F_{so_5} is contained in the set of tau with tau and 1/(2 tau) both in that union,
that is in {+-1/4, +-1/3, +-1/2, +-2/3, +-3/4, +-1, +-3/2, +-2} (four orbits of the group generated by
tau -> -tau and tau -> 1/(2 tau), with representatives 1, 2, 3/2, 2/3).

Proof. (a) For sl_n the coordinates of 2 rho^v in the simple coroots are i(n - i), with minimum n - 1, and
every non-zero dominant element of the coroot lattice has all coordinates >= 1; so m mu <= 2 rho^v forces
m <= n - 1. For lambda = m mu, mu primitive, iota(lambda) = m iota(mu) with iota(mu) primitive in Q (simply laced),
so k iota(lambda) in Q means k in (1/m)Z. If tau = +-a/b in lowest terms lies in the union and 1/tau = +-b/a
too, then a, b <= n - 1 (Proposition 4.3; sl_n is its own Langlands dual, r^v = 1). (b) is (a) for n = 4,
with Proposition 9.1(a) and c = 3 - 60 (tau + 1/tau - 2). (c) 2 rho^v = (4, 2); the dominant elements below
it are the seven listed; (lambda, lambda)/2 = 1, 2, 4, 5, 9, 8, 10 and the greatest common divisors of the
coordinates are 1, 2, 2, 1, 3, 4, 2; the two conditions of Proposition 8.4(b) say k in (1/d)Z with
d = 1, 2, 2, 1, 3, 4, 2. QED

Computed values (scripts/spectral_flow_sl2.py and scripts/spectral_flow.py, exact arithmetic over Q; the
complex of total energy zero and total weight zero is finite, because the energy of a cochain
m c^omega is N(m) + sum over the ghosts c^{x,n} of omega of (n + <wt x, lambda>) - k (lambda, lambda)/2 on the
subspace of weight zero, and only finitely many ghosts have n + <wt x, lambda> < 0):

    g = sl_2, lambda = alpha^v:  H^*(g[[t]], V^k_{(lambda)}) = C in degrees 3, 4 for tau = -1 and tau = 1;
                               zero for tau = -4, -3, -2 and tau = 2, 3, 4, 5, 6, 8.
    g = sl_3, lambda = theta^v:  dimensions 1, 2, 1 in degrees 7, 8, 9 for tau = -2 and tau = 2;
                               dimensions 1, 1, 1, 1 in degrees 5, 6, 8, 9 for tau = -1 and tau = 1;
                               zero for tau = -3, 3, 4.

(For sl_2 the values at tau = +-1, +-2 and the vanishing at half-integral tau were recomputed
independently in REQUESTS/6-attack.) For tau below the critical level the complex is very small: for
sl_2 and tau = -1 it is spanned by v_lambda c^{f,0} c^{f,1} c^{f,2} and v_lambda c^{f,0} c^{f,1} c^{f,2} c^{h,0}, and it is
zero for tau <= -2. So for sl_2 the criterion of Proposition 8.4(a) applies at every integral level
tau <= -2, and the integrality conditions of 8.4(b) are far from sharp: by Proposition 7.4 the reduction map
fails to be an isomorphism only at tau = +-1.

### 8.3 g = so_5: the product at the exceptional levels

THEOREM 8.6 (computed). For g = so_5 and every non-critical level k,

    Ext^*_{S_k}(W^k(so_5), W^k(so_5)) = Lambda(eta_3, eta_7)

as a graded algebra: the product Ext^3 x Ext^7 -> Ext^10 is non-zero at every non-critical level; the
Laurent polynomial p of Corollary 8.2 is a unit of C[tau, tau^{-1}].

Proof. By Theorem 8.1 the dimensions are those of Lambda(eta_3, eta_7), so the statement is that the product
of the classes of degrees 3 and 7 is non-zero. It is non-zero outside F_{so_5} (Proposition 4.3), the set
of levels where it vanishes is stable under tau -> -tau (Proposition 4.4: the algebras are
anti-isomorphic) and under tau -> 1/(2 tau) (Proposition 4.3: the vertex algebras coincide), and
F_{so_5} is contained in the sixteen levels of Corollary 8.5(c), which form four orbits with
representatives tau = 1, 2, 3/2, 2/3. At each of these four levels the Yoneda product was computed
exactly over Q (by the other model family: REQUESTS/5-calc.d/ANSWER.md and the certificates
product_c_so5_1.json, product_c_so5_2.json, product_c_so5_3_2.json, product_c_so5_2_3.json there): a
cocycle phi of degree 3 of C(V)_0, not a coboundary, is lifted to a chain map phi_n : P_{n+3} -> P_n,
0 <= n <= 7, of the resolution of Proposition 2.7 (in weight zero only the generators e_omega with
deg omega <= 0 occur, so the system beta = 0 suffices); the composite psi phi_7 with a cocycle psi of
degree 7, not a coboundary, is a cocycle of degree 10 which is not in the image of D_9 (the rank of the
space of coboundaries of degree 10 is 3 and becomes 4 when the product is adjoined), at each of the four
levels. Control: the same code gives a non-zero product Ext^3 x Ext^5 -> Ext^8 for sl_3 at
c = 2, -10, 50, as Theorem 6.2 requires. QED

So for so_5 the universal vacuum self-Ext dimensions and ring do not change at any non-critical level, including the
sixteen levels where at least one of the two reductions from an affine algebra may fail to be an
isomorphism. Formality at these levels is Proposition 9.6.

## 9. The algebra structure of the bulk

### 9.1 Product and higher products

PROPOSITION 9.1. (a) For every simple g and every non-critical k outside F_g, Ext^*(W^k(g), W^k(g)) is the
exterior algebra on classes of degrees 2 m_i + 1 and the derived endomorphism algebra of W^k(g) in S_k is
formal as an associative A-infinity algebra.
(b) The same holds for sl_2 and sl_3 at every non-critical level.
(c) For so_5 the derived endomorphism algebra is formal at every non-critical level (Proposition 9.6
below). The ring structure alone does not imply this: a strictly unital minimal A-infinity structure on
Lambda(eta_3, eta_7) can have one non-zero higher product, m_4(eta_3, eta_3, eta_3, eta_3) = c eta_3 eta_7, and for
c non-zero it is not formal (its Koszul dual is the algebra on x_3, x_7 with [x_3, x_7] = c x_3^4).

Proof. (a) For k outside E_g this is Theorem 4.1. If k is in E_g and the complementary level k' is not, the
anti-equivalence used in Proposition 4.4 is an anti-equivalence of differential graded categories, so
the derived endomorphism algebra at k is the opposite of the one at k', which is formal. If k^L is
outside E_{g^L}, the two vertex algebras are equal (Proposition 4.3). (b) Theorems 6.1 and 6.2. (c) A
strictly unital minimal structure has m_n of degree 2 - n; with inputs a classes of degree 3 and b
classes of degree 7 the output has degree 2a + 6b + 2, which is one of 0, 3, 7, 10 only for
(a, b) = (1, 1), the product, and (a, b) = (4, 0). QED

PROPOSITION 9.6 (so_5: formality at every level). For g = so_5 and every non-critical k the derived
endomorphism algebra of W^k(so_5) in S_k is formal.

Proof. Step 0 (an invariant). Let E be a differential graded algebra over C with H^5(E) = H^6(E) = H^8(E) = 0
and H^*(E) graded commutative in odd degrees (xy = -yx for classes of odd degree), and a in H^3(E). Choose
a cocycle alpha representing a, then u in E^5 with du = alpha^2, then t in E^7 with dt = alpha u + u alpha (a
cocycle: d(alpha u) = -alpha^3, d(u alpha) = alpha^3). Then

    o = alpha t + t alpha + u^2

is a cocycle of degree 10 (d(alpha t) = -alpha^2 u - alpha u alpha, d(t alpha) = alpha u alpha + u alpha^2,
d(u^2) = alpha^2 u - u alpha^2), and its class o(E, a) in H^10(E) does not depend on the choices. Indeed:
replacing t by t + z, z a cocycle, changes the class by a[z] + [z]a = 0; replacing u by u + dx (every
cocycle of degree 5 is of this form) and t by t - alpha x + x alpha changes o by d(-ux + xu + x dx); and for
two representatives alpha, alpha + dw, the cocycle alpha + d(sw) of the differential graded algebra E[s, ds]
(E tensor the polynomial forms on the line), together with choices of u, t in E[s, ds], gives a class of
H^10(E[s, ds]) whose images under the evaluations at s = 0 and s = 1, which induce the same isomorphism on
cohomology, are the classes computed from alpha and from alpha + dw. The class is natural:
o(E', f_* a) = f_* o(E, a) for a homomorphism f of differential graded algebras (when both sides are
defined); o(E, c a) = c^4 o(E, a); and o = 0 for an algebra with zero differential (take u = t = 0). Hence
o(E, a) = 0 if E is formal.

Step 1 (o is the only obstruction). Let E be as in Step 0 with H^*(E) = Lambda(a, b), |a| = 3, |b| = 7, and
o(E, a) = 0. Let F be the cobar construction of the symmetric coalgebra on two generators of degrees 2 and
6: the free algebra on generators x_{ij}, (i, j) non-zero, of degrees 2i + 6j + 1, with
d x_{ij} = - sum x_{i'j'} x_{i''j''} over the decompositions (i, j) = (i', j') + (i'', j'') into non-zero
terms. The homomorphism F -> Lambda(a, b), x_{10} -> a, x_{01} -> b, the other generators to zero, is a
quasi-isomorphism (the exterior algebra is Koszul). A homomorphism Phi : F -> E with Phi(x_{10}) = alpha and
Phi(x_{01}) = beta (cocycles representing a, b) is constructed by induction on i + j: Phi(d x_{ij}) is a
cocycle of the even degree 2i + 6j + 2 >= 6, and H^n(E) = 0 for even n different from 0 and 10; the degree
is 10 only for (i, j) = (1, 1), where the class is -(ab + ba) = 0, and for (i, j) = (4, 0), where, with
Phi(x_{20}) = -u and Phi(x_{30}) = t, the cocycle is -(alpha t + u^2 + t alpha) and its class is -o(E, a) = 0.
So Phi exists; it induces on cohomology a homomorphism Lambda(a, b) -> H^*(E) which is the identity on a
and b, hence an isomorphism. So E is formal.

Step 2 (the family). Let A' = C[tau, tau^{-1}] and E_{A'} the differential graded algebra of Lemma 9.5 over A'.
Its cohomology is that of C(W_{A'}) (Lemma 9.5(b)), the direct sum over the weights w of the cohomologies
of the bounded complexes of free modules of finite rank C(W_{A'})_w; for w non-zero all fibres are acyclic
(Proposition 3.2), so the complex is acyclic; for w = 0 the cohomology is free of rank one in degrees
0, 3, 7, 10 (Theorem 8.1). So H^*(E_{A'}) is free over A' with basis 1, a, b, w, and for every tau_0 non-zero
H^*(E_{tau_0}) = H^*(E_{A'}) (x) C_{tau_0} (Lemma 9.5(a) and the universal coefficient sequence). Choose a
cocycle alpha representing a, and u, t in E_{A'} as in Step 0 (possible because H^6(E_{A'}) = H^8(E_{A'}) = 0);
the class of alpha t + t alpha + u^2 is c(tau) w with c in A'. The reductions of alpha, u, t modulo tau - tau_0
are choices as in Step 0 for E_{tau_0}, so o(E_{tau_0}, a_0) = c(tau_0) w_0, with a_0, w_0 generators of H^3 and
H^10 of the fibre. For irrational tau_0 the algebra E_{tau_0} is formal (Theorem 4.1), so c(tau_0) = 0. A
Laurent polynomial with infinitely many zeros is zero. So o(E_{tau_0}, a_0) = 0 for every tau_0 non-zero, and
E_{tau_0} is formal by Theorem 8.6 and Step 1. QED

### 9.2 The bracket for sl_2 and sl_3

For g = sl_2 and g = sl_3 the algebra Ext^*(V, V) is the cohomology of the differential graded vertex
algebra K(V) of Theorem 6.2(b) (for sl_2: Vir^c (x) Vir^{26-c} (x) (ghosts of weight 2)), which contains
the field G = b^2 with [Q, G(z)] = T(z), the total stress tensor. By Lian-Zuckerman (New perspectives on
the BRST-algebraic structure of string theory, Comm. Math. Phys. 154 (1993), 613-646: the cohomology of a
topological chiral algebra) and, for W_3, Bouwknegt-McCarthy-Pilch (hep-th/9509119, Theorem 5.1), the
cohomology is a Batalin-Vilkovisky algebra:
the operator Delta = b^2_0 of degree -1 satisfies Delta Delta = 0 and

    {a, b} = (-1)^{|a|} ( Delta(ab) - Delta(a) b - (-1)^{|a|} a Delta(b) )

is a bracket of degree -1 making the cohomology a Gerstenhaber algebra.

PROPOSITION 9.2. For sl_2 and sl_3, at every non-critical level, Delta = 0 and the bracket is zero on
Ext^*(V, V).

Proof. The cohomology is non-zero only in degrees 0, 3 (sl_2) and 0, 3, 5, 8 (sl_3); no two of these
degrees differ by one, so Delta = 0, and the bracket is expressed through Delta and the product. QED

The operator G_{-1} = b^2_{-1} (degree -1, weight 1) gives the classes of the reduced complex (Theorem
6.2(c)): H^*(K(V)/T K(V)) is spanned by the classes x and G x, x in Ext^*(V, V), G 1 = 0; the connecting
map of 0 -> K/C -> K -> K/TK -> 0 (first map T) sends G x to x. The reduced cohomology has dimension one
in degree 2 for sl_2 and for sl_3, spanned by the class G eta_3, whose image under the connecting map is
eta_3. For sl_2 the adopted record inscribe/fab-T125 identifies omega_3/12 with the class of the family of
Virasoro algebras in the direction of the central charge c. The family of the level is the pull-back of
that family by c(k) = 13 - 6 tau - 6/tau, so its class is (dc/dk) omega_3/12 = -(1/2)(1 - tau^{-2}) omega_3
(the value of Proposition 7.4); it vanishes at tau = +-1, where the family of the level is trivial to
first order, while omega_3 and G omega_3 are non-zero there. So the non-zero class of degree 2 is the
direction of the central charge, not of the level. This agrees in dimension with the published
first-order deformations: for the Virasoro algebra the bounded vertex-algebra cohomology has dimension one
in degrees 0, 2, 3 (Bakalov-De Sole-Kac, arXiv:2002.03612, Theorem 7.2), and for W_3 the space of
first-order deformations has dimension one at every c, including -22/5 (Kovalchuk-Qi, arXiv:2408.16309,
Section 6.4, using their Theorem 5.13). A comparison map between the reduced complex and those
deformation complexes is not constructed here, so for W_3 the identification of G eta_3 with the
deformation in the direction of the central charge is conditional on such a map (for W_3,
c = 50 - 24 tau - 24/tau, and the family of the level is again trivial to first order at tau = +-1).
The class eta_5 is the image of G eta_5, of degree 4 in the reduced complex; since the space of first-order
deformations of W_3 has dimension one, G eta_5 is not the class of a first-order deformation of W_3 as a
vertex algebra if such a comparison holds. No deformation problem with tangent class G eta_5 is
constructed here.

### 9.3 The secondary operations of the two families, and the statement at every rank

A family of complexes of free modules over a discrete valuation ring with uniformiser t has the
Bockstein operations beta_s of 7.1 on the cohomology of its special fibre; they are the obstructions
to extending a class of the special fibre to a class of the family modulo higher powers of t. Two
families pass through the bulk.

(1) The classical limit (t = hbar, special fibre the classical W-algebra with first-order differential
D_cl; 7.1).

THEOREM 9.3 (every g). Every class of H^*(g) = H^*(C(P)_0, D_cl) is the reduction modulo hbar of a
class of the complex (C(V_R)_0, hbar^{-1} D) over R; equivalently beta_s = 0 for all s >= 2 on
E_2 = H^*(g) = Lambda(theta_1, ..., theta_r). In particular the primitive classes theta_i lift. The beta_s are
derivations of the algebras E_s (Lemma 9.5); so beta_s is determined by its values beta_s(theta_i), which lie
in the part of degree
2 m_i + 2 of the ideal of decomposable elements: sums of products of an even number 2n of primitive
classes theta_j with sum of the m_j equal to m_i + 1 - n. For n = 1 this is a product theta_j theta_l
with m_j + m_l = m_i: the binary part of beta_2 would be a Lie bracket on the graded space with basis
p_1, ..., p_r dual to the theta_i, p_i of weight m_i, [p_j, p_l] a multiple of the p_i with
m_i = m_j + m_l, and the higher parts an L-infinity structure extending it. The theorem says that this
structure is zero for every g. For sl_4 the only possible component is [p_1, p_2] = c p_3, that is
beta(theta_7) = c theta_3 theta_5, the map from degree 7 to degree 8; for sl_n the possible binary
components are the [p_j, p_l] = c_{jl} p_{j+l}, j + l <= n - 1.

Proof. Theorem 7.1 (the dimensions of the generic fibre are those of E_2, by Corollary 4.2). The
degrees: beta_s raises the degree by one, theta_i has degree 2 m_i + 1, and an
element of degree 2 m_i + 2 of the exterior algebra is a sum of products of an even number of the
theta_j. QED

LEMMA 9.5 (a differential graded model). Let B be C, or a principal ideal domain over which the
constructions of Section 2 are made (Proposition 3.4: a localisation of C[k], or the ring R of 7.1), V the
vertex algebra over B, (P^beta_q) the system of Proposition 2.7, regarded as a complex P_. of pro-objects of
S_k. Put

    E^n = prod_m Hom_{Pro}(P_m, P_{m-n}) = lim_beta prod_m C^m(P^beta_{m-n}),

where C^m(M) = colim_{beta'} Hom(P^{beta'}_m, M) is the space of finitely supported functions on Omega_m with values
in M. E is the complex of endomorphisms of P_., a differential graded B-algebra under composition.
(a) E is torsion free over B, and for every maximal ideal (t) of B, E / tE is the algebra E of the fibre
of V at t.
(b) The map E -> C(V) induced by the augmentations P^beta_0 -> V is a quasi-isomorphism, and the product
induced on H^*(C(V)) = Ext^*(V, V) is the Yoneda product.
(c) For B = R: the Bockstein operations of C(V_R)_0 are those of the weight-zero part of E; they are
derivations of the algebras E_s; the product of E_1 = C(P)_0 is the exterior product of cochains, and
E_2 = H^*(g) as an algebra.

Proof. (a) The modules P^beta_q are free over B (bases of Lemma 2.4), C^m(M) is a direct sum of copies of M,
and products and limits of torsion-free modules are torsion free. Reduction modulo t commutes with
direct sums, with products (t prod M_i = prod t M_i), and with the limit over beta: the transition maps
are surjective (P^{beta+1}_q -> P^beta_q is surjective and C^m is exact), so for the tower X_beta of the
torsion-free modules prod_m C^m(P^beta_{m-n}) the sequence 0 -> lim X -> lim X -> lim X/t -> lim^1 X = 0 is
exact. The fibre at t of the system (P^beta) is a system as in Proposition 2.7 for the fibre of V.
(b) For fixed m and beta the functor C^m is exact, so C^m(P^beta_.) -> C^m(V) is a quasi-isomorphism; the
double complex has coordinates p=-m<=0, q=m-n>=0 and exact augmented columns. Its product
total complex maps quasi-isomorphically to C(V) by the exact-columns/product-total case of the
acyclic assembly lemma (Weibel, Lemma 2.7.3). No filtered colimit is moved through an infinite product. The
cones of these quasi-isomorphisms form a tower of acyclic complexes with degreewise surjective
transition maps; the exact sequence 0 -> lim -> prod -> prod -> 0 (second map 1 - shift) shows that its
limit is acyclic. Let V -> I be an injective resolution in S_k. The maps
End(P_.) -> Hom_{Pro}(P_., I) <- End(I) (composition with P_. -> V -> I) are quasi-isomorphisms: the first
because C^m is exact, as above; the second because Hom_{Pro}(P_m, I^j) = C^m(I^j) and
H^m(C(I^j)) = Ext^m(V, I^j) vanishes for m > 0 (Theorem A). So the differential graded algebra of triples
(an endomorphism of P_., an endomorphism of I, a homotopy between the two composites in Hom_{Pro}(P_., I))
maps quasi-isomorphically to End(P_.) and to End(I): E is a model of the derived endomorphism algebra of
V, and its product induces the Yoneda product.
(c) The Bockstein spectral sequence of a torsion-free complex depends only on its quasi-isomorphism
class, and in a torsion-free differential graded algebra the rule
t^{-s} D(xy) = (t^{-s} D x) y + (-1)^{|x|} x (t^{-s} D y) shows that every beta_s is a derivation. At hbar = 0
the letters commute, P_. is the Koszul resolution of the commutative algebra of modes, and the product
transported to C(P) is the exterior product of cochains with the product of P; the first Bockstein is
D_cl, a derivation, and by Theorem F the restriction to the wedge algebra is a quasi-isomorphism of
differential graded algebras onto the cochains of g. QED

For sl_4 the vanishing has the independent proof of Proposition 7.2 (the diagram automorphism). For
general g the proof is the comparison with the affine algebra at irrational levels (Section 4): the bulk
of the affine vertex algebra is H^*(g) at every non-critical level, with no dependence on the level.

LEMMA 9.4 (the bracket of the classical bulk). Let ( , ) be a non-degenerate invariant symmetric bilinear
form on a semisimple Lie algebra g, e_i a basis and e^i the dual basis. The operation

    {a, b} = (-1)^{|a| - 1} sum_i iota(e_i) a ^ iota(e^i) b

on the exterior algebra of g^* is the Poisson bracket of degree -2 extending the form on g^* (half of the
first-order term of the graded commutator of the Clifford algebra of g^*, uv + vu = 2 (u, v)). It vanishes
on the invariants (Lambda g^*)^g = H^*(g).

Proof. Let a, b be invariant cochains. They are closed, and by Cartan's formula d iota(x) a = 0 for x in g.
The map x -> [iota(x) a] from g to H^*(g) is g-equivariant and the target is a trivial module, so it is
zero (g = [g, g]). Hence iota(x) a is a coboundary for every x; the surjection of finite-dimensional
g-modules from cochains onto coboundaries has an equivariant linear section, which gives cochains h_x
with d h_x = iota(x) a depending linearly and equivariantly on x. The cochain
sum_i h_{e_i} ^ iota(e^i) b is invariant, and its differential is sum_i iota(e_i) a ^ iota(e^i) b, because
d iota(e^i) b = 0. The differential vanishes on invariant cochains (Chevalley-Eilenberg, Cohomology theory
of Lie groups and Lie algebras, Trans. Amer. Math. Soc. 63 (1948), (19.2) and Theorem 19.1). So
{a, b} = 0. QED

So the natural candidate for a bracket of degree -2 on the bulk, and the Lie structure on the dual of the
primitive classes of Theorem 9.3, are both zero at every rank, in the classical limit and at the levels
outside F_g. At the levels of F_g nothing of this kind is proved (OPEN.md, O1, O6).

(2) The family of the level (t = tau - tau_0, special fibre the bulk at the level tau_0). Its operations
beta_s^{tau_0} : E_s^n -> E_s^{n+1}, E_1 = Ext^*(W^{k_0}(g), W^{k_0}(g)), vanish for all s if and only if tau_0 is
not in J_g; this holds at every non-critical level for sl_2, sl_3 (Theorems 6.1, 6.2) and so_5 (Theorem
8.1), and for every g outside the finite set F_g. Since the ranks of the differentials can only drop at a
special level, the classes of the bulk at tau_0 in excess of H^*(g) come in pairs of adjacent degrees
(n, n+1), one pair for each elementary divisor of the torsion of the cohomology of the family at tau_0,
joined by a non-zero operation beta_s^{tau_0}. For sl_4 at tau_0 = +-3/2, +-2/3,
Theorem 12.6 gives exactly two such pairs, in degrees (8,9) and (11,12). Their
orders as torsion summands, equivalently their nonzero Bockstein page numbers,
are not determined by the fibre dimensions.

## 10. The first exhibited failure of the exterior algebra: sl_4 at tau = +-3/2 and +-2/3

### 10.1 The contribution of an orbit (every g, every level)

Notation of 8.2. Let n_1^- be the span of the elements x_alpha t^{-s}, alpha a positive root, 1 <= s <= ht(alpha)
(a nilpotent Lie subalgebra of g((t)), of dimension Delta = sum of the heights), N_1^- = exp(n_1^-); then
I_1 = N_1^- H, H = I_1 cap G(O), and I_1 . 1 = N_1^- . 1 is a locally closed subvariety of the affine Grassmannian Gr
isomorphic to the affine space N_1^- of dimension Delta, on which the twisting of level k is trivialised by
the canonical lift of N(K) to the central extension. psi is the function sum over the simple roots of
the coefficient of x_{alpha_i} t^{-1} on N_1^-. For a dominant coweight lambda in the coroot lattice put

    Y_lambda = (N_1^- . 1) cap Gr^lambda,

a locally closed subvariety of N_1^- (empty unless lambda = 0 or lambda is in Lambda_1); Y_0 is the point 1.
For a variety Y of pure dimension d, closed in a smooth variety U of dimension D, and a rank-one D-module
L on a neighbourhood of Y (or the restriction to Y of such), put

    H_!^m(Y; L) = H^{m + 2(D - d)}_Y(U; L)

(de Rham cohomology with supports; it does not depend on U, being the cohomology of the dualising complex
of Y with coefficients in L, and H_!^m(Y; L) = H^m(Y; L) if Y is smooth). For closed subvarieties
Z_1, Z_2 of Y the groups H_Y(U; L) satisfy the Mayer-Vietoris sequence for supports.

For this subsection define N_lambda geometrically as RHom(V^k, delta_{t^lambda} * V^k) in the
renormalised affine category. Its normalised !-fibre convention fixes any sign in the spectral-flow
label of 8.2: twisting by Ad(t^{-lambda}) uses the opposite spectral flow. For the self-opposite
coweights theta^v and 2 theta^v in the examples below, a Weyl conjugation identifies the two choices,
and N_lambda^q is exactly H^q(g[[t]], V^k_{(lambda)}) of 8.2.
The line bundle of level one on Gr restricted to Gr^lambda is the
G(O)-equivariant bundle G(O) x^{S_lambda} C_{chi_lambda}, chi_lambda the character of the stabiliser S_lambda of
t^lambda extending iota(lambda) = (lambda, .); on N_1^- . 1 it has the nowhere vanishing section sigma(y) = y sigma_0.
Let P_lambda -> Y_lambda be the pull-back of the S_lambda-torsor G(O) -> Gr^lambda, and f : P_lambda -> G_m the function
with sigma(y) = f(g) g sigma_lambda for y . 1 = g t^lambda . 1 (sigma_lambda a fixed non-zero vector of the fibre at
t^lambda); f(g s) = chi_lambda(s)^{-1} f(g). If k iota(lambda) is a weight of the maximal torus, the D-module f^k on
P_lambda descends to a rank-one local system L_lambda on Y_lambda (the restriction to Y_lambda of the irreducible
G(O)-equivariant twisted local system of Gr^lambda, in the trivialisation of the twisting on N_1^- . 1).

PROPOSITION 10.1. Let k be arbitrary.
(a) There is a long exact sequence

    ... -> H^n(g[[t]], V^k(g)) -> Ext^n_{S_k}(W^k(g), W^k(g)) -> T^n -> H^{n+1}(g[[t]], V^k(g)) -> ...

whose first map is DS_*, where T^n = Hom(V^k, K' * V^k[n]) (Proposition 8.3).
(b) T has a finite filtration with graded pieces T_lambda, lambda in Lambda_1, and T_lambda = 0 if N_lambda = 0.
(c) If N_lambda is non-zero and Y_lambda has pure dimension d_lambda, there is a spectral sequence

    E_2^{m,q} = H_!^m(Y_lambda; e^psi (x) L_lambda^vee) (x) N_lambda^q   ==>   T_lambda^{m + q - 2 d_lambda}.

Proof. Choose a finite G(O)-stable Schubert variety S containing the closure of N_1^- . 1.
Let A_k be the renormalised affine category of Section 4 and define the continuous functor

    Phi_S : D_k(S) -> Vect,     F -> RHom_{A_k}(V^k, F * V^k).

Convolution is continuous. The affine vacuum is compact in A_k: it is induced from the
one-dimensional module of the compact-open subalgebra g[[t]], one of the compact generators in
Dhillon, arXiv:1905.06477, Section 5.1.2, preceding Proposition 5.5. Thus RHom(V^k,-) is continuous.
Categorical Verdier duality supplies a coefficient object C_S in D_{-k}(S), uniquely representing
Phi_S by

    Phi_S(F) = R Gamma_dR(S, F tensor! C_S).

Here the level twists cancel in tensor!. The duality and its pairing are Drinfeld-Gaitsgory,
arXiv:1108.5351v3, Corollary 8.4.3 and Lemma 8.4.5; on a finite-type scheme de Rham direct image is
continuous, so the pairing holds for all objects. Twisted duality follows from the same local
pairing and descent, exchanging the twisting with its inverse. Evaluating on delta_y gives

    i_y^! C_S = RHom_{A_k}(V^k, delta_y * V^k).

This constructs the derived coefficient object and its fibres simultaneously. The spherical
structures on the two vacuum modules make Phi_S equivariant, so C_S is strongly G(O)-equivariant.
On an orbit, its connected stabiliser implies that the cohomology objects, in the normalisation
where !-fibre is exact, are sums of the unique rank-one twisted equivariant object, with
multiplicities N_lambda^q. In the trivialisation on N_1^- that local system is L_lambda^vee,
because C_S has level -k. This assertion concerns cohomology objects; it does not split C_S or
assert that the following spectral sequence degenerates.

Write j:N_1^- . 1 -> S. The averaging kernel is the clean extension
j_*(e^psi tensor! omega_{N_1^-}) in dualising normalisation. Cleanness is Raskin,
arXiv:1611.04937v1, Lemma 2.16.1, descended along right G(O)-equivariance; the averaging shift is
Theorem 2.7.1(3). The projection formula for the pairing therefore gives

    Phi_S(Y) = R Gamma_dR(N_1^-, e^psi tensor! j^! C_S).

The closed-point support map at 1 is Phi_S(delta_1 -> Y). By Theorem 4.1, Step 2, this is
DS_* under the comparison with the W-vacuum, proving (a). Removing that point and using
the closed/open support triangles for the finitely many remaining orbit intersections gives
a finite filtration of its cone T. All restrictions here are derived !-restrictions.
If N_lambda=0, equivariance implies that C_S restricts to zero on its entire orbit, giving (b).

For (c), restrict the cohomology objects on the smooth orbit by ! to Y_lambda. The result is
the dualising coefficient object on Y_lambda with coefficient L_lambda^vee and multiplicity
N_lambda^q. Its hypercohomology spectral sequence has the displayed E_2-term. For a stratum of
pure dimension d, a class in H_!^m is in degree m-2d of the dualising de Rham complex, directly
from the defining support shift. Adding the fibre degree q gives m+q-2d. The finite geometric
cohomological amplitude and finite number of strata give convergence. QED

At the half-integral levels used below L_lambda has order two, so L_lambda^vee is isomorphic to
L_lambda and the computed groups are unchanged. No fractional shift of the level is introduced
by this dualisation. The construction is a consequence of the cited categorical duality,
compactness and clean averaging theorems; those sources do not themselves compute these
orbit contributions to the smooth W-vacuum self-Ext.

Checks of the normalisation in (c) against known cases. (1) g = sl_2, tau = +-1, lambda = alpha^v: Y_lambda is the
punctured line {a non-zero} in N_1^- = {exp(a e t^{-1})}, f = a, L_lambda is trivial, H^*(G_m; e^a) is of dimension
one in degree 1, N_lambda has dimension one in degrees 3, 4, d_lambda = 1: T has dimension one in degrees 2 and
3, as Proposition 7.4 and Theorem 6.1 require (DS_* is zero in degree 3). (2) g = sl_3, tau = +-2,
lambda = theta^v: in the coordinates n_12 = a_1/t, n_23 = a_2/t, n_13 = b/t + c/t^2 of N_1^-, Y_lambda is
{c = 0, a_1 a_2 = 0, (a_1, a_2, b) non-zero}, the union of two punctured planes, and H_!^*(Y_lambda; e^{a_1 + a_2}) has
dimension one in degrees 1 and 3; N_lambda has dimensions 1, 2, 1 in degrees 7, 8, 9; so E_2 has total
dimension 8 and lowest degree 1 + 7 - 4 = 4. By Theorem 6.2 and (a), T^5 has dimension at most one and
T^6 = 0; this holds exactly when the differential d_2 has rank one on E_2^{1,8} and on E_2^{1,9}, and then T
has dimension one in degrees 4, 5, 7, 8 and DS_* kills theta_5 and theta_3 theta_5. (3) g = sl_3, tau = -1/2,
lambda = 2 theta^v: Y_lambda = {c non-zero, c different from a_1 a_2} is open in N_1^-, L_lambda is the square root
of c (c - a_1 a_2) (Lemma 10.3), H^*(Y_lambda; e^{a_1 + a_2} (x) L_lambda) has dimension one in degree 3, N_lambda has
dimension one in degrees 9, 10, 12, 13 (scripts/spectral_flow.py), d_lambda = 4: T has dimension one in
degrees 4, 5, 7, 8, compatible with Theorem 6.2 in the same way.

### 10.2 The orbit of 2 theta^v for sl_4

Let g = sl_4, G = SL_4. Coordinates on N_1^- (Delta = 10): the entries of the unipotent matrix n,

    n_12 = a_1/t,  n_23 = a_2/t,  n_34 = a_3/t,  n_13 = b_1/t + c_1/t^2,  n_24 = b_2/t + c_2/t^2,
    n_14 = e_1/t + e_2/t^2 + e_3/t^3;       psi = a_1 + a_2 + a_3.

The orbit of the lattice n O^4 is Gr^lambda with dominant lambda = (d_3, d_2-d_3, d_1-d_2, -d_1), d_i the largest order of
pole of the i x i minors of n. Let lambda = 2 theta^v = (2, 0, 0, -2), that is d_1 = d_2 = d_3 = 2.

LEMMA 10.2. Y_lambda is the disjoint union of the three locally closed subvarieties of dimension 6

    Y_A = {e_3 = c_1 = c_2 = a_2 = 0,  e_2 non-zero,  e_2 different from a_1 b_2 + b_1 a_3},
    Y_B = {e_3 = c_2 = a_3 = 0,  c_1 non-zero,  c_1 different from a_1 a_2,  b_2 c_1 = a_2 e_2},
    Y_C = {e_3 = c_1 = a_1 = 0,  c_2 non-zero,  c_2 different from a_2 a_3,  b_1 c_2 = a_2 e_2}.

Y_A is closed in Y_lambda, and the closures of Y_B, Y_C in Y_lambda are the smooth varieties
Y_B^- = Y_B u D_B, Y_C^- = Y_C u D_C, with D_B = Y_A cap {a_3 = 0}, D_C = Y_A cap {a_1 = 0}; and
Y_B^- cap Y_C^- = D_B cap D_C = D_BC = Y_A cap {a_1 = a_3 = 0}. Moreover

    Y_B^- = A^2_{(b_1, e_1)} x (A^2 - 0)_{(c_1, e_2)} x S,   S = {(a_1, mu) : a_1 mu different from 1},

with a_2 = mu c_1 and b_2 = mu e_2, and D_B is the divisor c_1 = 0.

Proof. d_1 = 2 means e_3 = 0 and (c_1, c_2, e_2) non-zero. The coefficients of t^{-4} and t^{-3} of the 2 x 2 minors
are, up to sign, c_1 c_2 and b_1 c_2 + c_1 b_2 - a_2 e_2 (rows 1, 2, columns 3, 4), a_1 c_2 (rows 1, 2, columns
2, 4), a_3 c_1 (rows 1, 3, columns 3, 4); the other minors have poles of order at most 2. The 3 x 3 minors
are the entries of n^{-1}; the coefficient of t^{-3} of (n^{-1})_14 is -e_3 + a_1 c_2 + c_1 a_3 - a_1 a_2 a_3, and its
entries have a pole of order 2 unless -c_1 + a_1 a_2, -c_2 + a_2 a_3 and -e_2 + a_1 b_2 + b_1 a_3 all vanish. So
Y_lambda is defined by e_3 = 0, c_1 c_2 = a_1 c_2 = a_3 c_1 = a_1 a_2 a_3 = 0, b_1 c_2 + c_1 b_2 = a_2 e_2, together with
(c_1, c_2, e_2) non-zero and (c_1 - a_1 a_2, c_2 - a_2 a_3, e_2 - a_1 b_2 - b_1 a_3) non-zero (when d_1 = 2 and d_2 <= 2
the coweight is (2, 0, 0, -2) or (1, 1, 0, -2), according as d_3 = 2 or 1). The three cases
c_1 = c_2 = 0; c_1 non-zero; c_2 non-zero give Y_A (then a_2 e_2 = 0 and e_2 is non-zero), Y_B (then
c_2 = a_3 = 0, and the last condition says c_1 different from a_1 a_2: if c_1 = a_1 a_2 then
e_2 - a_1 b_2 = e_2 (c_1 - a_1 a_2)/c_1 = 0) and Y_C. On Y_B the rows (c_1, e_2), (a_2, b_2) are proportional
with (c_1, e_2) non-zero, which gives mu; the condition is a_1 mu different from 1 both for c_1 non-zero and
for c_1 = 0 (where it reads e_2 different from a_1 b_2); the points with c_1 = 0 are those of D_B. The same
for Y_C. (Machine check: for the field with three elements, the enumeration of all 3^10 points of N_1^-
gives 1098 points on this stratum, 342 + 378 + 378 in Y_A, Y_B, Y_C, with no mismatch:
scripts/strata_sl4.py part1.) QED

LEMMA 10.3 (the local system). Let k be in 1/2 + Z.
(a) For g = sl_3 and lambda = 2 theta^v = (2, 0, -2): for the point n_12 = a/t, n_23 = b/t, n_13 = e/t^2 of N_1^-
(a, b, e and e - ab non-zero) the matrix g with columns
u_1 = (e, bt, t^2), u_2 = (0, ab - e, at), u_3 = (0, 0, 1/(e(ab - e))) lies in SL_3(O), n O^3 = g t^{-lambda} O^3, and
f(g) = e^3 (e - ab), using the reference vector sigma_{-lambda} at t^{-lambda}.
The points t^{-lambda} and t^lambda are Weyl conjugate. Changing the orbit representative in this
way changes neither the descended local system nor its square class. Thus L_lambda is the local
system of the square roots of e (e - ab).
(b) For g = sl_4 and lambda = 2 theta^v, L_lambda is the local system of the square roots of
e_2 (e_2 - a_1 b_2 - b_1 a_3) on Y_A, of c_1 (c_1 - a_1 a_2) on Y_B and of c_2 (c_2 - a_2 a_3) on Y_C; on Y_B^- it is the
local system of the square roots of 1 - a_1 mu.

Proof. (a) Let Lambda = n O^3, with basis w_i = n e_i, and Lambda_0 = O^3. The lattice spanned by t^{-2} u_1 = w_3,
u_2 = -e w_2 + a t w_3 and t^2 u_3 is contained in Lambda and has the same determinant, and det(u_1, u_2, u_3) = 1.
The fibre of the determinant line bundle at Lambda is det(Lambda_0 / Lambda cap Lambda_0) (x) det(Lambda / Lambda cap Lambda_0)^{-1}.
A vector p of Lambda_0 lies in Lambda if and only if p_3(0) = 0 and -a p_2(0) + (ab - e) p_3'(0) = 0, and a vector
x w_1 + z_2 w_2 + z_3 w_3 of Lambda lies in Lambda_0 if and only if z_3(0) = 0 and a z_2(0) + e z_3'(0) = 0; these
two pairs of linear forms are coordinates on the two quotients, of dimension 2. The section sigma is
(e_2 ^ e_3) (x) (w_2 ^ w_3)^{-1} (the flag of coordinate subspaces induces on both quotients filtrations with the
same graded pieces, identified by n). The vector g sigma_{-lambda} is (u_3 ^ t u_3) (x) (t^{-2} u_1 ^ t^{-1} u_1)^{-1}; in the
coordinates, u_3 = (1/(e(ab - e)), 0), t u_3 = (0, 1/e), e_2 = (0, -a), e_3 = (1, 0), and w_3 = (1, 0),
t w_3 = (0, e), w_2 = (0, a). So u_3 ^ t u_3 = (a e^2 (ab - e))^{-1} e_2 ^ e_3 and w_3 ^ t w_3 = -(e/a) w_2 ^ w_3, and
g sigma_{-lambda} = sigma / (e^3 (e - ab)). The other values of f on the torsor differ by the inverse
fibre character, which is the square of a character; so f^k, k in 1/2 + Z, descends to the square root of
e (e - ab). (Control: for s in the torus, s g = g' l with g' the matrix attached to s n s^{-1} and
l = diag(s_3, s_2 s_3/s_1, s_1^2/s_3), and e^3(e - ab) is multiplied by (s_1/s_3)^4, as the
invariance of f under left multiplication by the torus requires.)
(b) H_1 of Y_A is generated by small loops around the divisors e_2 = 0 and e_2 = a_1 b_2 + b_1 a_3. The
points of Y_A with a_3 = b_1 = e_1 = 0 are the points of (a) for the copy of SL_3 on the coordinates
1, 2, 4 (the lattice is the direct sum of the lattice of (a) and of O e_3, and the coweight restricts to
(2, 0, -2)), with (a, b, e) = (a_1, b_2, e_2); this slice meets both divisors transversally, so the
monodromy of L_lambda around each of them is -1. In the same way the points of Y_B with
b_1 = e_1 = e_2 = 0 (then b_2 = 0) are the points of (a) for the coordinates 1, 2, 3, with
(a, b, e) = (a_1, a_2, c_1), and H_1 of Y_B is generated by the loops around c_1 = 0 and c_1 = a_1 a_2. Similarly
for Y_C. On Y_B, c_1 (c_1 - a_1 a_2) = c_1^2 (1 - a_1 mu); a local system on the smooth variety Y_B^- is
determined by its restriction to the dense open subset Y_B. QED

### 10.3 The cohomology of the stratum

We use the following facts about de Rham cohomology with coefficients in rank-one D-modules (exponentials
of functions tensor square roots of invertible functions; all are holonomic).
(F1) H^*(A^1; e^{cx}) = 0 for c non-zero.
(F2) H^*(A^1 - {p}; (x - p)^{1/2}) = 0.
(F3) For the smooth projections between smooth varieties used below, which are locally products
in the displayed fibre coordinates with flat connection coefficients, fibrewise de Rham acyclicity
implies H^*(U;L)=0. On each such chart the relative de Rham complex contracts by (F1) or (F2),
so its derived direct image is zero; descent gives the stated vanishing. No assertion for an
arbitrary morphism is needed. These are also the smooth local-product instances of exceptional
base change and localization (Etingof, Introduction to algebraic D-modules, Propositions 3.1, 3.5).
(F4) If Z is a smooth closed subvariety of codimension c of a smooth variety Y and H^*(Y - Z; L) = 0, then
H^*(Y; L) = H^{* - 2c}(Z; L|_Z), the isomorphism being the push-forward from Z.
(F5) H^n(Y; L) = 0 for n > dim Y if Y is affine.

Let L be the local system of Lemma 10.3(b) and write h(Z) for the graded space H^*(Z; e^psi (x) L|_Z).

LEMMA 10.4. (a) h(D_BC) = C + C[-1] (dimension one in degrees 0 and 1).
(b) h(D_B) = h(D_BC)[-2] and h(Y_A) = h(D_BC)[-4], by push-forward from D_BC; likewise for D_C.
(c) h(Y_B) = C[-3], and h(Y_B^-) = C[-5]; the push-forward h(D_B)[-2] -> h(Y_B^-) is an isomorphism in degree 5
and zero in degree 4. Likewise for Y_C.

Proof. (a) D_BC = {(b_1, b_2, e_1, e_2) : e_2 non-zero}, psi = 0, and L is the local system of the square roots of
e_2^2, which is trivial.
(b) D_B - D_BC = {a_1 non-zero} in the coordinates (a_1, b_1, b_2, e_1, e_2) of D_B, with psi = a_1 and
L the square root of e_2 (e_2 - a_1 b_2). For fixed (a_1, b_1, e_1) the fibre is, in the coordinates e_2 and
q' = e_2 - a_1 b_2, the product of two punctured lines with the local system e_2^{1/2} (x) q'^{1/2}; its
cohomology vanishes by (F2). So h(D_B - D_BC) = 0 by (F3), and (F4) gives h(D_B) = h(D_BC)[-2]. In the same
way Y_A - D_BC = {(a_1, a_3) non-zero}; for fixed (a_1, a_3, e_1) the fibre is {(b_1, b_2, e_2)} with
e_2 and q' = e_2 - a_1 b_2 - a_3 b_1 non-zero, the product of a line and two punctured lines with the same local
system; so h(Y_A - D_BC) = 0 and h(Y_A) = h(D_BC)[-4].
(c) Y_B = A^3_{(b_1, e_1, e_2)} x Y'', Y'' = {(a_1, a_2, c_1) : c_1 non-zero, c_1 different from a_1 a_2}, with psi = a_1 + a_2 and L
the square root of c_1 (c_1 - a_1 a_2). Let Z = {a_1 a_2 = 0} in Y''. On Y'' - Z, in the coordinate
u = c_1/(a_1 a_2), L is the square root of u (u - 1) (the factor (a_1 a_2)^2 is a square), so
h(Y'' - Z) = H^*(G_m; e^a)^{(x) 2} (x) H^*(A^1 - {0, 1}; (u(u - 1))^{1/2}) = C[-3]. On Z the local system L is
trivial; Z is the union of Z_1 = {a_1 = 0} and Z_2 = {a_2 = 0}, with h(Z_i) = 0 by (F1) and
h(Z_1 cap Z_2) = H^*(G_m) = C + C[-1]; so H_Z^*(Y''; .) = C[-3] + C[-4] by the Mayer-Vietoris sequence, and the
sequence H_Z^n -> H^n(Y'') -> H^n(Y'' - Z) -> H_Z^{n+1} with H^4(Y'') = 0 (F5) gives h(Y'') = C[-3].
In the coordinates of Lemma 10.2, psi = a_1 + mu c_1 and L is the square root of 1 - a_1 mu on Y_B^-. First,
h(A^2_{(c_1, e_2)} x S) = 0: off the divisor mu = 0 the cohomology vanishes by (F1) (the variable c_1) and (F3),
so by (F4) it is the cohomology of the divisor mu = 0 with coefficients in e^{a_1}, which vanishes by (F1).
Hence h((A^2 - 0) x S) = H^{* + 1}_{0 x S}(A^2 x S; .) = H^{* - 3}(S; e^{a_1} (x) (1 - a_1 mu)^{1/2}). Off the line a_1 = 0
the cohomology of S vanishes by (F2) (the variable mu) and (F3), so by (F4) it is C[-2]. So
h(Y_B^-) = C[-5]. Finally the sequence H^n_{D_B}(Y_B^-) -> H^n(Y_B^-) -> H^n(Y_B), with
H^n_{D_B}(Y_B^-) = h(D_B)^{n-2} and h(Y_B) = C[-3], shows that the push-forward is surjective in degree 5,
hence an isomorphism there, and it is zero in degree 4 because H^4(Y_B^-) = 0. QED

PROPOSITION 10.5. H_!^m(Y_lambda; e^psi (x) L_lambda) has dimension one for m = 3 and m = 5, and vanishes for the other
m.

Proof. Y_lambda is the union of the closed subvarieties Y_A, Y_B^-, Y_C^-, smooth of dimension 6, with
Y_A cap Y_B^- = D_B, Y_A cap Y_C^- = D_C (dimension 5) and Y_B^- cap Y_C^- = D_BC, the triple intersection
(dimension 4). The Mayer-Vietoris spectral sequence for supports has
E_1^{-2,q} = H_!^{q-4}(D_BC), E_1^{-1,q} = H_!^{q-2}(D_B) + H_!^{q-2}(D_C) + H_!^{q-4}(D_BC),
E_1^{0,q} = H_!^q(Y_A) + H_!^q(Y_B^-) + H_!^q(Y_C^-), and converges to H_!^{p+q}(Y_lambda). By Lemma 10.4 only the rows
q = 4 and q = 5 are non-zero. In the row q = 4 the terms are C x, then C x_AB + C x_AC + C x_BC, then C x_A
(x a generator of H^0(D_BC), the other generators its images under the push-forwards, which are
isomorphisms by Lemma 10.4(b); Y_B^- and Y_C^- contribute nothing), with d x = x_AB - x_AC + x_BC,
d x_AB = d x_AC = x_A, d x_BC = 0: the cohomology is of dimension one, at the middle term, of total degree 3.
In the row q = 5 the terms are C y, then C y_AB + C y_AC + C y_BC, then C y_A + C y_B + C y_C (y a generator of
H^1(D_BC); by Lemma 10.4(b), (c) the push-forwards are isomorphisms), with d y = y_AB - y_AC + y_BC,
d y_AB = y_A - y_B, d y_AC = y_A - y_C, d y_BC = y_B - y_C: the cohomology is of dimension one, at the last term,
of total degree 5. There is no room for further differentials. QED

Control by exponential sums. For a finite field of odd cardinality q, psi a non-trivial additive character and
chi the quadratic character, the sums of psi(a_1 + a_2 + a_3) chi(F) over the points of D_BC, D_B, Y_A, Y_B, Y_B^-
and Y_lambda (F the function of Lemma 10.3(b) of which L is the square root) are

    q^4 - q^3,   q^4 - q^3,   q^4 - q^3,   -q^4,   -q^3,   -q^4 - q^3

(elementary: the sum of chi(x(x - p)) over x is -1 for p non-zero and q - 1 for p = 0; verified for
q = 3, 5, 7, 11, 13 by scripts/strata_sl4.py, and for q = 3 by enumeration of the whole stratum). These are
the traces of Frobenius on the compactly supported cohomologies dual to Lemma 10.4 and Proposition 10.5:
two classes for D_BC, D_B, Y_A (of weights 8 and 6, in degrees of opposite parity), one class for Y_B^-, and
for Y_lambda two classes in odd degrees with eigenvalues q^4 and q^3.

### 10.4 The theorem

THEOREM 10.6. Let g = sl_4 and tau = k + 4 in {3/2, -3/2, 2/3, -2/3} (central charges -7 and 253). Then

    Ext^n_{S_k}(W^k(sl_4), W^k(sl_4)) = H^n(sl_4) for n <= 7 (dimension one for n = 0, 3, 5, 7),
    dim Ext^8_{S_k}(W^k(sl_4), W^k(sl_4)) = 2,

whereas dim H^8(sl_4) = 1. So the vacuum self-Ext algebra of W^k(sl_4) at these four levels is not the
exterior algebra on classes of degrees 3, 5, 7: besides the nonzero product eta_3 eta_5 there is
a class of degree 8 which is not in the image of H^*(sl_4), and the family of the level has a non-zero
Bockstein operation at these levels (9.3).

Proof. Let tau = -3/2, k = -11/2. Step 1. By Proposition 8.4(b), N_lambda = 0 unless k (lambda, lambda)/2 is an integer
and k iota(lambda) is in the root lattice, that is unless (lambda, lambda)/2 is even and lambda is twice an element of
the coroot lattice. Among the fifteen elements of the coroot lattice which are dominant, non-zero and
at most 2 rho^v (in the basis of simple coroots: (1,1,1), (1,2,1), (1,2,2), (1,2,3), (2,2,1), (2,2,2), (2,3,2),
(2,3,3), (2,4,2), (2,4,3), (3,2,1), (3,3,2), (3,3,3), (3,4,2), (3,4,3), with (lambda, lambda)/2 = 1, 2, 3, 6, 3, 4, 5, 7,
8, 9, 6, 7, 9, 9, 10) this leaves (2,2,2) = 2 theta^v and (2,4,2) = (2, 2, -2, -2). For lambda = (2, 2, -2, -2):
k (lambda, lambda)/2 = -44, while the sum of the negative twisted indices n + <wt x, lambda> of the ghosts is -40; so
the complex of energy zero is zero and N_lambda = 0. For lambda = 2 theta^v: k (lambda, lambda)/2 = -22 and the sum of the
negative twisted indices is -22; so a cochain of energy zero is the vector v_lambda times the product of the
twelve ghosts of negative twisted index times ghosts of twisted index zero, which are the ghosts of the
parabolic subalgebra p of g with Levi factor l = s(gl_1 + gl_2 + gl_1) and nilradical u spanned by the root
vectors x_alpha t^{-<alpha, lambda>} with <alpha, lambda> < 0; the weight condition selects the five ghosts of u and an
element of the exterior algebra of l^* of weight zero, and the differential is that of l. So

    N_lambda = H^*(l)[-17]:   dimensions 1, 2, 1, 1, 2, 1 in degrees 17, ..., 22

(confirmed by scripts/spectral_flow.py 4 -11/2 2,0,0,-2 exact, which also gives the zero complex for
(2, 2, -2, -2)).
Step 2. By Proposition 10.1(b), T = T_lambda with lambda = 2 theta^v, and by 10.1(c), Lemma 10.2 (d_lambda = 6) and
Proposition 10.5 there is a spectral sequence with E_2^{m,q} = H_!^m(Y_lambda; e^psi (x) L_lambda) (x) N_lambda^q, non-zero only
for m in {3, 5} and 17 <= q <= 22, converging to T^{m + q - 12}. Hence T^n = 0 for n < 8, and T^8 = E_2^{3,17} is of
dimension one (no differential enters or leaves this corner).
Step 3. In the sequence of Proposition 10.1(a), T^{n-1} = T^n = 0 gives Ext^n = H^n(sl_4) for n <= 7, and

    0 = T^7 -> H^8(sl_4) -> Ext^8 -> T^8 -> H^9(sl_4) = 0

gives dim Ext^8 = 1 + 1 = 2.
Step 4. The dimensions at tau = 3/2 are the same by Proposition 4.4, and at tau = +-2/3 by Proposition 4.3
(Feigin-Frenkel duality; sl_4 is simply laced). QED

Remarks. (1) Status. The proof uses the theorems of Raskin through Propositions 8.3 and 10.1 (the
formalism of twisted D-modules on the affine Grassmannian acting on the category of modules), the
theorem of Dhillon (Proposition 4.4) for tau = 3/2, and the explicit computations 10.2-10.5. It does not
use the conjectural formula of OPEN.md, O1. An independent decision is the rank of the differential
D_8 of the complex C(V)_0 at tau = 3/2: the theorem says that rank D_7 + rank D_8 = 24449, one less than
generic (requested: REQUESTS/7-calc.md).
(2) The rest of the bulk at these levels. The E_2-term of Step 2 has total dimension 16. By
Proposition 10.1(a) and semicontinuity, dim Ext^n = dim H^n(sl_4) + (dim T^n - rank delta_n) - rank delta_{n-1},
delta_n : T^n -> H^{n+1}(sl_4). The formula of OPEN.md predicts that d_2 : E_2^{3,q} -> E_2^{5,q-1} is contraction
with one generator of degree 1 of H^*(l) (the Chern class of the torsor P_lambda acting on
H_!^*(Y_lambda)), so that T has dimensions 1, 1, 2, 2, 1, 1 in degrees 8, 9, 11, 12, 14, 15, and that
delta_11 and delta_14 have rank one (DS_* kills theta_5 theta_7 and theta_3 theta_5 theta_7), which gives the dimensions
1, 0, 0, 1, 0, 1, 0, 1, 2, 1, 1, 1, 2, 0, 0, 1. Section 12 proves the transgression,
both connecting ranks and these dimensions without using the Tor comparison.
(3) The same method decides the other levels. At a level tau = -p/q the coweights with N_lambda non-zero are
few, and the complexes computing N_lambda are small; Proposition 10.1 reduces the bulk to the twisted
exponential cohomology of the varieties Y_lambda. The three checks after Proposition 10.1 are instances.

## 11. Consequences for the exceptional fibres and reduction classes

### 11.1 The first additional torsion pair for W_4

THEOREM 11.1. Let g=sl_4 and tau_0 be one of +-3/2, +-2/3. Put
R=C[tau]_(tau-tau_0), t=tau-tau_0, and let K_R=C(W_R)_0 be the finite free complex of
Proposition 3.4. There is an integer a>=1 such that

    H^q(K_R) is torsion free for q<=8,
    H^9(K_R) = R/(t^a).

In particular the exceptional fibre has dim Ext^9>=1. At tau_0=-3/2 its degree-eight space
contains the nonzero product DS_*(theta_3) DS_*(theta_5); at the other three levels it
contains the product of the generators transported by Propositions 4.3-4.4. The quotient
by this product line is one-dimensional. In the Bockstein spectral sequence at tau_0, exactly one elementary
torsion pair starts in degree eight and ends in degree nine. Its first nonzero operation
occurs on page a. The integer a and possible further torsion starting in degree nine
are not determined by this statement.

Proof. Over the discrete valuation ring R, a bounded finite free complex is a direct sum
of one-term free complexes and two-term complexes R --t^b--> R, including contractible
summands with b=0. For each q let e_q be the number of summands with b>=1 whose target
has degree q; equivalently e_q is the number of cyclic torsion summands of H^q(K_R).
If h_q is the generic cohomology dimension and h_q^0 is the special-fibre dimension, then

    h_q^0 = h_q + e_q + e_{q+1}.

By Theorem 10.6, h_q^0=h_q for q<=7 and h_8^0=h_8+1. Nonnegativity gives e_q=0 for
q<=8 and e_9=1. The generic H^9(sl_4) is zero, so H^9(K_R) has no free summand and is
the single cyclic module R/(t^a). The same equation in degree nine gives
dim Ext^9=e_9+e_10=1+e_10>=1.

At tau=-3/2 the cone vanishes below degree eight, so Theorem 10.6 identifies DS_* with
an isomorphism through degree seven and an injection in degree eight. Since it is
multiplicative, DS_*(theta_3 theta_5) is the nonzero product of the two primitive images.
For the other three levels, transport this product line along the algebra isomorphism
or anti-isomorphism of Propositions 4.3-4.4; it is again a nonzero product of classes
of degrees three and five. This transport does not by itself identify the transported
classes with the canonical DS images at the other levels. Thus the assertion about
the canonical DS product is made at tau=-3/2; at the other levels use these transported
generators. Finally the two-term summand with differential t^a has its sole nonzero
Bockstein from degree eight to degree nine on page a, as in Section 7.1. QED

This is an application of the elementary-divisor and base-change description, rather than
a new general theorem about families of complexes. Its W_4 input is the orbit calculation
of Theorem 10.6, not the conjectural Tor comparison. It also determines, without constructing
their matrices, rank D_7=11706 and rank D_8=12743 at these four levels from the fixed term
dimensions and the cohomology through degree eight. Request 7's independent modular
calculation reaches D_6 only and is not a computation of these two ranks.

### 11.2 A single orbit for so_5 at tau=-2

LEMMA 11.2. Let g=so_5, k=-5 and tau=k+3=-2. In the conventions of Corollary 8.5(c),
only lambda=(1,1) can contribute to the cone T of Proposition 10.1. For that coweight

    N_lambda = H^*(sl_2 + C)[-7],
    H_!^m(Y_lambda;e^psi) = C for m=3, and zero otherwise,
    T^n = C for n=6,7,9,10, and zero otherwise.

Proof. The positive roots are e_1-e_2, e_1+e_2, e_1 and e_2, with (e_i,e_j)=delta_ij.
The energy bound on the underlying vacuum PBW vector in a weight-zero spectral-flow
cochain is

    B(lambda) = k |lambda|^2/2 + sum_{alpha>0} a_alpha(a_alpha+1)/2,
    a_alpha = <alpha,lambda> >= 0.

For the seven coweights of Corollary 8.5(c), in their printed order, these bounds are
0,-1,-4,-5,-12,-10,-13. A negative bound gives the zero complex. For lambda=(1,1),
energy zero forces the vacuum and the four ghosts of negative twisted index. Their
root-weight sum is (-3,-3). To obtain the required ghost weight k lambda=(-5,-5),
one must also take all three zero-twisted-index nilradical ghosts, of weights
-e_1,-e_2,-(e_1+e_2). What remains is the weight-zero CE complex of the Levi
l=sl_2+C, with trivial coefficient: the determinant characters of the forced ghosts
cancel the vacuum character. It is shifted by seven. Thus N_lambda=H^*(l)[-7],
with degrees 7,8,10,11, each once. Expanding brackets in the standard five-dimensional
orthogonal representation gives cochain dimensions (1,2,2,2,1) and differential ranks
(0,1,1,0,0) in degrees 7 through 11, an exact check of the cancellation.

In the vector representation, lambda has entries (1,1,0,-1,-1). Every lattice of
this orbit in N_1^- . 1 has its unique negative-loop representative n=1+t^{-1}X.
For the antidiagonal orthogonal form, the equations n^t J n=J imply X in so_5 and
X^2=0. Write

    X = ((0,a,c,d,0), (0,0,b,0,-d), (0,0,0,-b,-c),
         (0,0,0,0,-a), (0,0,0,0,0)).

Then X^2=0 is equivalent over C to b=0 and c^2+2ad=0. A nonzero such X has rank
two, and hence has the stated lattice elementary divisors. Consequently

    Y_lambda = {c^2+2ad=0} - {0},       psi=a,       dim Y_lambda=2.

The coefficient local system is trivial, since k is integral. The finite etale double
cover (u,v)->(a,c,d)=(u^2,uv,-v^2/2) identifies this smooth punctured quadric with
(A^2-{0})/{+-1}; its exponential coefficient pulls back to e^{u^2}.
The polynomial operator d/du+2u is injective with one-dimensional cokernel, represented
by du. Thus H^*(A^2;e^{u^2})=C[-1], on which (u,v)->(-u,-v) acts by -1.
The support group at the origin is C in degree four and has trivial involution.
The localization sequence gives one odd class in H^1(A^2-{0};e^{u^2}) and one even
class in H^3. Taking invariants under the free order-two action gives H^*(Y_lambda;e^a)=C[-3].
Because Y_lambda is smooth, this is also H_! in the stated normalisation.

There is just one geometric cohomology row in Proposition 10.1, so its spectral
sequence has no nonzero differentials. The total degree is 3+q-2(2)=q-1, which
gives the four displayed degrees of T. QED

The exact root and cochain computations use actual matrices and the form tr(AB)/2
in REQUESTS/8-attack.d/b2_spectral_check.py; the geometry and character sums are checked
by b2_control.py there. Fresh outputs are in scripts/round1-verification. The exponential
sum of the punctured quadric is -1 over every odd finite field: the a!=0 part contributes
-q and the a=0 part contributes q-1. This checks the twist and shift; the de Rham proof
above, rather than the trace alone, determines the cohomology groups.

### 11.3 A vanishing primitive reduction class without a dimension jump

THEOREM 11.3. For g=so_5 and k=-5 (tau=-2), the canonical reduction homomorphism is

    DS_* : Lambda(theta_3,theta_7) -> Ext^*(W^{-5}(so_5),W^{-5}(so_5))
                                      = Lambda(eta_3,eta_7),

with DS_*(theta_3) nonzero and DS_*(theta_7)=DS_*(theta_3 theta_7)=0. Equivalently
its kernel is the ideal (theta_7) and its image is the exterior algebra generated by
DS_*(theta_3). The target still has its nonzero degree-seven generator and nonzero
degree-ten product. This statement does not specify a normalised scalar in degree three
or transport the canonical reduction map to a reciprocal level.

Proof. Use the exact sequence of Proposition 10.1 and Lemma 11.2. Since T^2=T^3=0,
DS_* is an isomorphism in degree three. In degree six, H^6(so_5)=0 and
Ext^6(W^{-5},W^{-5})=0 by Theorem 8.1. Thus the connecting map T^6 -> H^7(so_5)
is injective, and it is an isomorphism because both spaces have dimension one.
Exactness forces DS_* to vanish in degree seven; the surviving target class maps
isomorphically to T^7. The same argument at degree nine, where both affine and
W-vacuum self-Ext vanish, makes T^9 -> H^10(so_5) an isomorphism and DS_* zero
in degree ten. The target ring and its nonzero product are Theorem 8.6. There are
no other nonzero source degrees, and the degree-zero map is the identity. QED

The published antecedents used here are the affine absolute self-Ext computation of
Frenkel-Teleman (arXiv:math/0401428, Proposition 4.2 for the relative group, together
with the semidirect-product factorization in the proof of Proposition 4.6 for the absolute factor)
and the Whittaker
comparison of Raskin (arXiv:1611.04937v1, Theorems 2.7.1 and 5.1.1). They determine
the source and averaging formalism; they do not calculate this rational-level kernel.
The W(B_2) BRST currents of Zhu (hep-th/9306026, Section 4) concern a specified string
critical charge and do not identify this smooth-vacuum reduction map. The additional
conclusion follows here from the single orbit calculation and the all-level target ring.

### 11.4 Compatibility of reduction with complementary duality

PROPOSITION 11.4. Let k'=-k-2h^v. The complementary dualities of the affine and
W categories induce graded anti-isomorphisms a and b on the two vacuum endomorphism
algebras such that

    b DS_{k,*} = DS_{k',*} a.

Consequently the ranks of the canonical reduction maps in each degree agree at
tau and -tau. In particular Theorem 11.3 also holds for so_5 at k=-1 (tau=2).

Proof. Use the notation of Theorem 4.1, Step 2. Put H=G(O) cap I_1 and let
L_k=Av_!^{I_1,psi}, R_k=Av_*^{I_1,psi} on H-equivariant objects. The subgroup H is
pro-unipotent, so its equivariant category is a full stable subcategory of the affine
category and contains the thick subcategory generated by V^k. On that subcategory
the natural clean-averaging morphism L_k -> R_k[2 Delta] is an isomorphism: it is
one on the spherical vacuum by Raskin, Theorem 2.7.1(3), and hence on its shifts,
cones and summands. Step 2 identifies DS there with the insertion of L_k into the
Whittaker category, naturally on all morphisms of that thick subcategory.

Let D_aff and D_1 denote the contravariant equivalences on compact affine and
I_1-equivariant objects. Dualising the adjunction between L_k and the forgetful
functor gives, on these compact objects,

    D_1 L_k = R_{k'} D_aff,

with Whittaker character -psi on the right. This is the functorial compatibility
of Dhillon, arXiv:1905.06477v1, Propositions 4.15 and 4.22. The same clean-averaging
isomorphism replaces R_{k'} by L_{k'}[-2 Delta] on the dual thick subcategory.
Dhillon's Theorem 4.33 identifies duality after insertion with stage-one duality
followed by a fixed shift. Thus the composite is naturally isomorphic, on the
thick vacuum subcategory, to DS_{k'} D_aff followed by a fixed shift. Changing
-psi to psi is the inner conjugation of loc. cit., Lemma 5.15.

Formula (5.8) of that paper, with the compact-open subalgebra equal to g[[t]]
and its one-dimensional trivial module, identifies D_aff V^k with V^{k'}.
The corresponding W-vacuum identification is Proposition 4.4. A common shift
does not change an endomorphism algebra, and the preceding isomorphisms are
natural on morphisms, so they give the stated square of graded anti-isomorphisms.
In degrees three, seven and ten for so_5, each source space is one-dimensional.
The anti-isomorphism a therefore preserves its nonzero line, and the vanishing
and nonvanishing in Theorem 11.3 transfer from tau=-2 to tau=2. QED

This is the compatibility on morphisms implicit in the same averaging and duality
inputs used for Proposition 4.4; no comparable compatibility with the reciprocal
Feigin-Frenkel isomorphism and the two different affine reduction functors is asserted.

### 11.5 The degree-five reduction class for W_3

THEOREM 11.5. For g=sl_3 and tau in {2,-2,1/2,-1/2}, the canonical reduction map

    DS_* : Lambda(theta_3,theta_5) -> Lambda(eta_3,eta_5)

is an isomorphism in degree three and has kernel (theta_5). In particular
DS_*(theta_5)=0 at tau=2, whereas it is nonzero at every irrational level by
Theorem 4.1. At tau=-2 the two possibly nonzero differentials of the orbit spectral
sequence, E_2^{1,8}->E_2^{3,7} and E_2^{1,9}->E_2^{3,8}, each have rank one.

Proof. First take tau=-2, k=-5. The four possible nonzero coweights in 8.4(c)
have PBW energy bounds 0,-3,-3,-4, respectively. Only lambda=theta^v contributes.
Its saturated-energy complex is the exterior algebra of the two-dimensional Cartan,
shifted by seven, so N_lambda has multiplicities 1,2,1 in degrees 7,8,9.
The stratum in the coordinates of the first check after Proposition 10.1 is

    Y = {c=0, a_1 a_2=0, (a_1,a_2,b)!=0},       psi=a_1+a_2.

It is the union of two punctured planes, meeting along the punctured b-line; its
dimension is two and its coefficient local system is trivial. Each plane has
exponential cohomology C[-3], by localization at the removed point of an affine
plane with vanishing exponential cohomology. The intersection has C in degrees
zero and one. The degree-one intersection class maps isomorphically, by Gysin,
to the degree-three class of each plane: this follows from the divisor sequence,
whose complementary open set is G_m x A^1 with coefficient e^a and cohomology C[-1].
The support Mayer-Vietoris sequence therefore gives H_!^*(Y;e^psi)=C[-1]+C[-3].

The total E_2 dimensions are (1,2,2,2,1) in degrees four through eight. Let u,v
be the ranks of the two d_2 maps in the statement; each is zero or one, and there
are no other possible differentials. Then

    (dim T^4,...,dim T^8) = (1, 2-u, 2-u-v, 2-v, 1).

Theorem 6.2 gives Ext^4=Ext^6=0 and dim Ext^5=1. In the cone exact sequence,
T^4 -> H^5(sl_3) is an isomorphism, so DS_* is zero in degree five and
Ext^5 -> T^5 is an isomorphism. Thus u=1. The vanishing in degree six forces
T^6=0, giving v=1. Now T^7 -> H^8(sl_3) is an isomorphism and DS_* vanishes
in degree eight. Since T is zero below degree four, DS_* is an isomorphism in
degree three. This proves the kernel assertion at tau=-2 without computing d_2
by a chosen connection: its ranks are forced by the established target theorem.

Next take tau=-1/2, k=-7/2. The integrality conditions exclude the first three
coweights and leave only 2 theta^v. Its stratum is
{c!=0, c!=a_1 a_2} in A^4_{a_1,a_2,b,c}, of dimension four, with the quadratic
local system sqrt(c(c-a_1 a_2)). Lemmas 10.3(a) and 10.4(c), with the extra
affine b-coordinate, give geometric cohomology C[-3]. The exact spectral-flow
calculation has the following finite dimensions and ranks:

    q                     8   9   10   11   12  13  14
    dim C^q               9  58  143  176  113  34   3
    rank d_q              9  48   94   82   30   3   0
    dim N_lambda^q        0   1    1    0    1   1   0.

These are the weight-zero, energy-zero CE cochains of the spectral-flow convention
in 8.2, computed over Q by REQUESTS/8-attack.d/spectral_check.py; the enumeration
is closed under the differential and every consecutive composite is zero. The
independent Cartan basis E_ii-E_33 and the complete enumeration are in that script,
with a fresh run in scripts/round1-verification/spectral_results.json.
The single geometric row gives T in degrees 4,5,7,8, each once. The same exact
sequence proves the asserted kernel. Finally Proposition 11.4 transfers the ranks
to tau=2 and tau=1/2. Since the primitive source spaces have dimension one and
there are no decomposables in their degrees, the kernel is precisely (theta_5). QED

The published paired W_3 current of Bouwknegt-McCarthy-Pilch, hep-th/9509119,
Theorem 3.2, does not calculate this affine-to-W map in absolute smooth Ext.
The additional rational-level vanishing follows from that target calculation's
smooth comparison, the orbit formula and the explicit spectral-flow complexes.

## 12. The remaining maps at the exceptional W_4 fibre

Throughout this section tau=-3/2, k=-11/2, lambda=(2,0,0,-2), and the notation of
Sections 10.1-10.5 is retained. Thus the only nonzero orbit coefficient has
N=H^*(l)[-17], l=sl_2+C^2, and its geometric coefficient has degrees three and five.
The coefficient local system has order two, so its dual is isomorphic to itself.

### 12.1 The central stabilizer operations

LEMMA 12.1. Write H^*(l)=Lambda(x,z,omega), with |x|=|z|=1 and |omega|=3.
The two central stabilizer homotopies of the derived coefficient object of 10.1,
for

    Z_x=diag(1,-1/2,-1/2,0),    Z_z=diag(0,-1/2,-1/2,1),

induce contraction in x and z, respectively, and annihilate omega. Their sum has
ranks 1,1,0,1,1 from fibre degrees 18,19,20,21,22 to the preceding degree.

Proof. Compute the derived Hom defining the !-fibre by the continuous induced CE
resolution of the affine vacuum. For a stabilizer element Z, its infinitesimal
equivariance homotopy is the usual insertion i_Z, with

    d i_Z + i_Z d = Lie_Z.

The right side includes the action on the coefficient module and on the CE
arguments. The difference between the stabilizer lift and the spectral-flow lift
is the scalar character k(lambda,Z); the opposite-twist line in 10.1 cancels that
character. It does not discard the insertion. Thus the degree-minus-one
stabilizer operations used in descent are these Cartan insertions, even though
the induced degree-zero action on fibre cohomology is trivial.

For Z_x and Z_z insertion preserves the energy-zero and weight-zero subspaces.
The projections to those subspaces therefore commute with insertion. The saturated
complex of Theorem 10.6 is the product of its seventeen forced ghosts with the
Cartan-weight-zero CE complex of l; insertion by these central Cartan elements
does not remove a forced root ghost. The cancellation of determinant and vacuum
characters leaves precisely the two ordinary central insertions on CE(l).
The inclusion of the weight-zero subcomplex of CE(l) is a quasi-isomorphism,
since nonzero Cartan weights contract. The assertion follows from
H^*(l)=Lambda(x,z,omega), with omega the sl_2 primitive. A suspension changes at
most the common sign of the two insertions.

An exact calculation in the saturated affine complex gives cochain dimensions
(1,3,4,4,3,1), differential ranks (0,1,2,1,0,0), and the stated insertion ranks.
Every insertion anticommutes with d. The independent full five-dimensional Levi
complex has cochain dimensions (1,5,10,10,5,1) and differential ranks
(0,3,6,3,0,0), giving the same cohomology. These rational matrices, bases and
insertion maps are in REQUESTS/9-calc.d/stabilizer.py and stabilizer_results.json,
with a fresh replay in scripts/round1-verification/request9. QED

### 12.2 The two characteristic classes of the stabilizer torsor

LEMMA 12.2. Let h_3 and h_5 generate the two geometric groups of Proposition 10.5.
The two central characteristic classes of the stabilizer torsor act by

    x -> -h_5,       z -> -h_5

on h_3 tensor H^1(l), for compatible orientations. Thus the transgression has
rank one on H^1(l), with kernel the line x-z.

Proof. Put A=Y_A, B=Y_B^-, C=Y_C^-. The leading t^{-2} term of the lattice and
its dual determine the extreme line ell and the extreme one-dimensional quotient Q
of the associated flag. To distinguish vectors from the coordinate e_2, write E_i
for the standard basis vectors of C^4. Frames of ell on A,B,C are, respectively,

    E_1,        E_1,        e_2 E_1 + c_2 E_2.

Frames of Q on A and C are E_4. On B the nonzero covector
c_1 E_3^*+e_2 E_4^* trivialises Q; on D_B its associated frame is E_4/e_2.
These formulas follow by reading the t^{-2} matrix entries: on B the leading
map is E_1 tensor (c_1 E_3^*+e_2 E_4^*), while on C it is
(e_2 E_1+c_2 E_2) tensor E_4^*. The nonvanishing conditions in Lemma 10.2
make all the frames valid on their stated components.

The bundle of frames of ell and Q is the two-torus quotient of the actual
stabilizer torsor, with its SL_2 and pro-unipotent factors removed. Write its
fibre coordinates as u_A,v_A over A. On overlaps,

    u_B=u_A,        v_B=e_2 v_A,
    u_C=u_A/e_2,    v_C=v_A.

Put e=dlog(e_2), x=dlog(u_A), z=dlog(v_A). In B coordinates the two fibre forms
are dlog(u_B), dlog(v_B)-e; in C coordinates they are dlog(u_C)+e, dlog(v_C).

The two support rows of Proposition 10.5 have maps

    X: C --(1,-1,1)^t--> C^3 --(1,1,0)--> C,
    Y: C --(1,-1,1)^t--> C^3 --((1,1,0),(-1,0,1),(0,-1,-1))--> C^3.

Use pair labels AB,AC,BC. The class h_3 is represented by X_BC, and h_5 by
Y_A=Y_B=Y_C modulo the second row's boundaries. Multiplication by e on an
intersection takes its X class to its Y class. The Gysin maps to B and C kill
X and carry Y to their respective component generators, by Lemma 10.4(c).
Apply the displayed frame changes before each Gysin map. The projection formula
then gives

    d(X_BC x)=-Y_C,        d(X_BC z)=-Y_B.

For the first equation, the term with dlog(u_C) pushes forward to zero and the
term with e pushes to Y_C, with the negative endpoint sign. For the second,
the correction -e in the B expression has the negative sign, while that endpoint
has positive incidence. This proves the stated matrix (-1,-1) on h_3.

One can retain all the torus forms in this calculation. Tensor the terms of
each support row with Lambda(x,z) and use the same substitutions in its maps.
The resulting rational complex has one-dimensional cohomology in degrees
3,4,6,7, and no other cohomology. The triple-to-pair map is injective, including
these fibre forms, so its Cech E_2 column -2 vanishes. There are only three
Cech columns, and consequently no further Cech differential. Thus replacing
the local terms by their cohomology loses no subsequent differential relevant
to this calculation. Matrices and a fresh exact replay are in
REQUESTS/9-calc.d/torsor.py and scripts/round1-verification/request9.
Suppressing the frame changes instead gives eight classes and fails this check.
The determinant character is twice x-z; its zero transgression is consistent
with the determinant line's trivialisation on N_1^-. QED

### 12.3 The cone and the two possible dimension tables

THEOREM 12.3. At tau=-3/2 the orbit differential in Proposition 10.1 is, up to a
common suspension sign, contraction by Z_x+Z_z from the geometric row of degree
three to that of degree five. Its total rank is four. Consequently

    dim T^n = 1,1,2,2,1,1 for n=8,9,11,12,14,15,

and T vanishes in all other degrees. Moreover eta_3 eta_7 is nonzero, where
eta_j=DS_*(theta_j). The remaining connecting maps have a common rank

    epsilon = rank(delta_11) = rank(delta_14) in {0,1},

where delta_n:T^n->H^{n+1}(sl_4). All other connecting maps vanish. The two possible
Ext dimension lists, in degrees zero through fifteen, are

    epsilon=1: 1,0,0,1,0,1,0,1,2,1,1,1,2,0,0,1,
    epsilon=0: 1,0,0,1,0,1,0,1,2,1,1,2,3,0,1,2.

In particular eta_5 eta_7=0 if and only if epsilon=1. The dimensions and the
vanishing or nonvanishing of products of the one-dimensional primitive spaces
transport to the other three levels +-3/2,+-2/3 by Propositions 4.3-4.4.

Proof. Descent of the CE coefficient complex along the stabilizer torsor gives
the Cartan transgression: each degree-two central characteristic class acts by
its associated insertion on the fibre. Lemmas 12.1 and 12.2 identify these two
operations explicitly, so d_2 is contraction in x+z, with ranks 1,1,0,1,1 from
source fibre degrees 18,19,20,21,22. The semisimple primitive omega has degree
three and contributes no degree-two characteristic class. No later differential
can occur between the only geometric degrees three and five. This gives the
displayed cone dimensions, using the total degree m+q-12.

The affine class theta_3 acts on the finite fibre by its restriction to the
middle sl_2, namely a nonzero multiple of multiplication by omega. In CE
representatives, terms involving non-Levi root ghosts repeat a forced ghost
and vanish; the invariant trace form restricts nontrivially to that sl_2.
The operation commutes with the central insertions. Hence the associated graded
of T is a free Lambda(theta_3)-module with generators of degrees 8,9,11,12.
In particular theta_3:T^8->T^11 is injective and theta_3:T^11->T^14 is onto,
with kernel that same image. These ranks survive extensions between the two
geometric rows: the first rank is already one on the associated graded, the
second already one with one-dimensional target, and the square is zero.

The cone triangle is linear for the affine self-Ext algebra acting by
precomposition. Since T^10=0, the exact sequence would give Ext^10=0 if
delta_9:T^9->H^10(sl_4) were nonzero. Semicontinuity gives dim Ext^10>=1,
so delta_9=0. Thus DS_* is an isomorphism in degree ten, and its multiplicativity
gives eta_3 eta_7!=0. The only remaining possible connecting maps are delta_11
and delta_14. Module linearity makes delta_11 zero on theta_3 T^8, since its
preceding map delta_8 has zero target. On the complementary one-dimensional
quotient it has rank epsilon. The surjection theta_3:T^11->T^14 and the
isomorphism theta_3:H^12(sl_4)->H^15(sl_4) give rank(delta_14)=epsilon.

Finally exactness gives
dim Ext^n=dim H^n(sl_4)+dim T^n-rank(delta_n)-rank(delta_{n-1}), yielding the two
lists. In degree twelve the source is the line theta_5 theta_7; its image is zero
exactly when delta_11 is onto. This is the asserted product criterion. QED

The finite calculations determining d_2 are REQUESTS/9-calc, not the Tor model.
They do not determine the coefficient object's attachment to the base point,
which is what epsilon measures. The two-torus method also gives the two rank-one
transgressions for the separate SL_3 minimal stratum, agreeing with Theorem 11.5
without using its target dimensions to impose their ranks.

### 12.4 The first correction to the filtered Koszul differential

LEMMA 12.4. Suppose that homogeneous free generators of V satisfy the hypotheses
of Section 2 and that every word in a commutator [x,y] has standard degree at
most Delta(x)+Delta(y)-2. The pro-resolution of Proposition 2.7 can be chosen so
that its differential, on a generator e_omega, is

    d(e_omega) = d_K(e_omega) - b(e_omega)
                modulo G_{Delta(omega)-4} P_{q-1}.

Here write [x,y]=sum_z u_z^{xy} z with z an annihilation letter, as in 5.4,
and b is the signed exterior sum replacing x,y in omega by z with coefficient
u_z^{xy}, using the ordinary Chevalley-Eilenberg signs. Each b term has total
standard degree at most Delta(omega)-2. On pure-ghost cochains with vacuum
coefficient, a scalar matrix entry of D can be nonzero only if the target ghost
degree exceeds the source ghost degree by at least two. If the difference is
exactly two, that entry is the usual CE contribution from the scalar linear
part of the commutators; all choices below the displayed filtration bound leave
it unchanged.

Proof. The factorisation by a rightmost annihilation letter is the one used in
Proposition 5.4: the binomial support of a commutator of annihilation letters
excludes a creation-only normally ordered word. The factorisation respects the
standard-degree bound. Its formulas are finite in each truncated module of
Section 2 and define compatible maps in the inverse system. The degree and
filtration estimate in Proposition 2.7(1) ensures they define module morphisms.

Put d_app=d_K-b on exterior generators and extend by module linearity. The
terms d_K^2 are the commutators [x,y] and cancel the terms of d_K b+b d_K in
which the inserted z is removed. The remaining cross terms contain commutators
[x',u_z^{xy}], and the terms of b^2 contain two bracket coefficients. The first
kind lowers total standard degree by at least four: u_z^{xy} has already lost
two degrees, and commuting a letter past any word loses two more. The second
kind loses two degrees twice. Therefore

    d_app^2(e_omega) lies in G_{Delta(omega)-4} P_{q-2}.

Construct the actual differential by induction on q, retaining d_app modulo
this bound. If the lower differentials have been constructed, the defect of
d_app(e_omega) under d_{q-1} is a cycle in that same filtered piece. Strict
filtered exactness in Proposition 2.7 gives its preimage in
G_{Delta(omega)-4} P_{q-1}. Subtract it. The affine-space inverse-limit argument
of that proposition makes the corrections compatible with every cutoff. The
new differential has square zero and the prescribed first correction. Thus no
equivariant contraction or invariant creation/annihilation splitting is used.

Now evaluate on pure-ghost cochains. The Koszul term acts on the vacuum by an
annihilation letter and is zero. A b term with source ghost degree p and target
ghost degree t has coefficient of standard degree at most t-p-2. Hence it is
zero for t-p<2, and for t-p=2 its coefficient is a scalar, exactly the linear
commutator coefficient. A correction in G_{t-4} has no component on a source
of ghost degree p>t-4. Evaluation of nonempty coefficient words on the vacuum
cannot change these inequalities. This proves the scalar assertions. QED

For the present W_4 fibre the hypothesis holds. Choose L and primary generators
P_3,P_4 of weights three and four; such generators exist at c=253 (and at c=-7),
as verified over Q from the Miura presentation in REQUESTS/9-calc.d/primary_check.py.
They may be chosen with diagram parities +,-,+, by averaging the primary generators
under the involution; their independent leading invariant symbols are preserved.
Every PBW word then has parity (-1)^Delta. The degree drop of (Delta) in 1.3 is
at least one, and parity makes it even, hence at least two. The global Virasoro
commutators are exactly [L_a,P_{d,n}]=((d-1)a-n)P_{d,n+a}, a=-1,0,1.
Lemma 12.4 is the filtered version of the first-order construction in 5.4;
its use here concerns the fixed-level PBW filtration, not the classical limit
in the level parameter.

### 12.5 The protected top-degree minor

THEOREM 12.5. For W^k(sl_4) at tau=-3/2,

    rank D_14=8,       dim Ext^15=1,       epsilon=1.

Proof. The fifteen smallest annihilation indices have sum -1, and sixteen have
sum two. Since V_1=0, all nine basis elements of C^15(V)_0 have vacuum coefficient,
and C^16(V)_0=0. Put s=<L_-1,L_0,L_1> and use the exterior tensor ordering with
the three s-ghosts first. Thirteen annihilation letters outside s have minimum
index sum two; at most two s-letters can contribute a sum no smaller than -1.
Thus every weight-zero fifteen-ghost word contains all three s-letters.

The relative twelve-letter words of index sum -1,0,1 number 1,9,24. This count
is finite and independent of the level. For example the nine middle words have
the common nine letters

    P4_-3, P3_-2, P4_-2, P3_-1, P4_-1, P3_0, P4_0, P3_1, P4_1,

followed by two letters from {L_2,P3_2,P4_2} and one from {L_3,P3_3,P4_3}.
Let v_s be the product of the three s-ghosts. Use as source cochains
i_{L_a}(v_s) times each relative word of index a, for a=-1,1. They give 25
distinct vacuum-coefficient elements of C^14(V)_0. The nine target cochains
are v_s times the relative words of index zero.

Choose the differential of Lemma 12.4. Its scalar entries increasing ghost
standard degree by exactly two are the linear CE terms. In this submatrix only
brackets involving a global s-letter can contribute: brackets of two relative
letters either leave all three s-ghosts in the source, or insert an already
present s-letter and give zero. Brackets internal to s contribute zero by
unimodularity of sl_2. Hence the degree-two part is precisely the cochain action
of L_-1 and L_1 on the relative exterior words, using

    [L_a,P_{d,n}]=((d-1)a-n) P_{d,n+a}.

With the lexicographic word order of REQUESTS/9-calc.d/top_sl2.py, an eight-row,
eight-column minor of this leading matrix is

    ( 0  2  0  0  0  0  0  0 )
    ( 0  0  1  0  0  0  0  0 )
    ( 6  0  0  0  0  0  0  0 )
    ( 0  0  0  2  0  0  0  0 )
    (-5  0  0  0  1  0  0  0 )
    ( 0  0  0  0  0  0  0 -1 )
    ( 4  0  0  0  0  2  0  0 )
    ( 0  0  0  0  0  0  1  0 ).

Its determinant is -48, also verified by independent integer Bareiss elimination.
The target standard degrees are (45,46,47,46,47,48,47,48), and the source degrees
are (45,43,44,44,45,45,46,46). Their total difference is sixteen. Every nonzero
entry of the actual differential has degree difference at least two, by Lemma
12.4. A determinant term has eight entries and fixed total difference sixteen;
therefore every entry in a nonzero term must have difference exactly two. No
higher filtered correction can change the determinant. Thus this is a nonzero
minor of the actual D_14, not merely of a proposed relative complex.

It follows that rank D_14>=8. Semicontinuity gives dim Ext^15>=dim H^15(sl_4)=1,
while dim C^15=9 and C^16=0, so rank D_14<=8. Hence rank D_14=8 and dim Ext^15=1.
The alternatives of Theorem 12.3 give dim Ext^15=2-epsilon, forcing epsilon=1. QED

The row indices are 0,...,7 and the column indices are 0,1,2,4,5,10,11,17 in
the saved 9 by 25 matrix. The degree check is recorded in
scripts/round1-verification/request9/degree_protection.json. A deliberately
incorrect primary-action coefficient gives rank nine, so the rank check detects
that convention error. The comparison used here is Lemma 12.4; no equivariance
of the PBW creation/annihilation splitting is assumed.

### 12.6 The exceptional W_4 dimensions and primitive products

THEOREM 12.6. Let g=sl_4 and tau in {3/2,-3/2,2/3,-2/3}. In the category of all
smooth modules of the universal principal W-algebra, the vacuum self-Ext dimensions
in degrees zero through fifteen are

    1,0,0,1,0,1,0,1,2,1,1,1,2,0,0,1,

and all higher groups vanish. Their total dimension is twelve. Nonzero generators
eta_3,eta_5,eta_7 of the three primitive-degree spaces satisfy

    eta_3 eta_5 != 0,       eta_3 eta_7 != 0,       eta_5 eta_7 = 0.

At tau=+-3/2 these generators can be taken to be the canonical reduction images,
and the kernel of DS_*:H^*(sl_4)->Ext^*(W^k,W^k) is the ideal (theta_5 theta_7).
At the reciprocal levels the assertions about dimensions and products use the
transported generators; no comparison of the two affine reduction maps is needed.

Proof. At tau=-3/2, Theorem 12.5 selects epsilon=1 in Theorem 12.3, giving the
complete dimension list and the last two product assertions. The first product
assertion is Theorem 10.6 and multiplicativity of DS_* (also Theorem 11.1).
The source exterior algebra has one class in degrees 0,3,5,7,8,10,12,15. The map
is injective in the first six of these degrees, and vanishes on theta_5 theta_7
and its product with theta_3 in the last two. Thus its kernel is precisely the
stated ideal. Proposition 11.4 gives the same canonical kernel at tau=3/2.
Propositions 4.3 and 4.4 transport the algebra and the one-dimensional primitive
spaces to all four levels. Reversing products does not change their zero or
nonzero status, since the three primitive classes at the starting level lie in
the graded-commutative image of the source. There are no cochain terms beyond
degree fifteen by the finite character enumeration of Section 3. QED

This proves the dimension formula (**) for its first discriminating pair
sl_4, {p,q}={2,3}, and the displayed primitive products agree with its prediction.
It does not prove the general Tor-to-Ext comparison, identify the full algebra
of the additional classes, or establish formality at these fibres. The exact
Tor table is a separately computed comparison target (REQUESTS/5-calc and
6-attack); it is not an input to the Ext calculation.

For the fixed finite terms in OPEN.md, the corresponding differential ranks are

    0,7,70,414,1558,4131,8053,11706,12743,10365,6220,2657,749,121,8.

These ranks follow from the orbit calculation, the protected top minor and the
dimension identity for a finite complex. The actual newly evaluated matrices
are the small stabilizer, torsor and 9 by 25 corner matrices. The nearest
published inputs, Raskin's Whittaker equivalence, Dhillon's duality and the
categorical Verdier pairing cited in 10.1, do not state this exceptional fibre
calculation. The published W_4 string currents at matter charge 246 likewise
do not compute these universal smooth-vacuum Ext groups at charges -7 and 253.
