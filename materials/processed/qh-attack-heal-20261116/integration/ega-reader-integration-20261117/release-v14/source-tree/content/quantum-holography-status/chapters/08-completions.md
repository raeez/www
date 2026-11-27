# Tensor products, support and completion

An operation on every finite collection of states need not act on an infinite state. The difficulty can occur before any integral diverges: the proposed output may simply lie outside the vector space on which the next operation is defined. For boundary reconstruction this matters twice. Several incoming representations must first be combined, and the resulting object must then be compared with a space of current operations. These constructions involve different infinite sums. Their order determines the comparison map.

## Tensor completion and matrix rank {#tensor-completion-and-rank}

Consider the vector space \(V=\mathbb C^{\mathbb N}\) of all complex sequences. The natural map

\[
V\otimes_{\mathbb C}V\longrightarrow
\mathbb C^{\mathbb N\times\mathbb N},
\qquad f\otimes g\longmapsto(f_i g_j)_{i,j\geq0},
\]
{#eq-sequence-tensor-map}

has image the matrices of finite rank. A sum of \(r\) elementary tensors has column space contained in the span of \(r\) sequences; conversely, a finite-rank matrix can be expressed using a basis of its column space. The infinite identity matrix \((\delta_{ij})\) therefore does not belong to this image.

Give the image the coordinatewise topology inherited from the full matrix space. Its completion is the full matrix space: finite-support matrices are dense, and the finite diagonal matrices converge coordinatewise to \((\delta_{ij})\). The identity matrix becomes available after this specified completion. Nothing in this calculation identifies the completion with a tensor product defined using a different topology.

::: figure fig-infinite-rank

The same issue appears in the current constructions below, where matrix indices are replaced by cohomological degrees, bar lengths, current modes and Laurent exponents. We will keep these indices separate long enough to see which infinite expressions the operations can act on.

## Algebraic tensors and mapping complexes {#ch08-algebraic-tensors-and-mapping-complexes}

For cochain complexes \(M,N\), with differential of degree \(+1\), the algebraic tensor complex has

\[
(M\otimes N)^n=\bigoplus_{i+j=n}M^i\otimes N^j,
\qquad
d(m\otimes n)=dm\otimes n+(-1)^{|m|}m\otimes dn.
\]

Every element has finite support along the cohomological diagonal. The mapping complex instead has

\[
\operatorname{Hom}^{r}(M,N)
=\prod_i\operatorname{Hom}(M^i,N^{i+r}),
\qquad
d(f)=d_Nf-(-1)^rf d_M.
\]

A homogeneous map must specify a map on every input degree; the product records that requirement. If \(M^i=N^i=\mathbb C\) for all integers \(i\), with zero differentials, then degree zero of the tensor complex contains a direct sum indexed by \(\mathbb Z\), whereas degree zero of the mapping complex is a product indexed by \(\mathbb Z\). Replacing either by the other changes the complex even in this elementary example.

A topology makes a further distinction. Put the discrete topology on each copy of \(\mathbb C\). Every continuous linear functional

\[
\prod_{i\geq0}\mathbb C\longrightarrow\mathbb C
\]

depends on finitely many coordinates. Continuity makes its kernel contain a basic neighbourhood on which only finitely many coordinates are constrained. By contrast, an algebraic functional on \(\bigoplus_i\mathbb C\) can assign an arbitrary coefficient to every basis vector. Thus passing from a direct sum to a product and then taking a continuous dual can recover a direct sum. This conclusion depends on the displayed topology and on the discrete target.

These examples explain why “take the dual” does not completely specify an operation for a field-theoretic construction. One must name the topology, the scalar ring and the degree totalization. The convention for shifts throughout this chapter is \(V[1]^n=V^{n+1}\).

## Laurent series with algebraic coefficients {#ch08-laurent-series-with-algebraic-coefficients}

For a vector space \(V\) over a field \(F\), define

\[
V((q))=\bigcup_{N\in\mathbb Z}q^N V[[q]].
\]

An element has one lower Laurent bound and an arbitrary sequence of coefficients in \(V\). If \(V=\bigoplus_{j\geq0}Fe_j\), then

\[
v(q)=\sum_{j\geq0}q^j e_j
\]

is allowed: each coefficient has finite support. There is no requirement that all coefficients lie in one finite-dimensional subspace of \(V\). Consequently

\[
V\otimes_F F((q))\subsetneq V((q))
\]

for this \(V\). A vector in the left side is a finite sum of Laurent series multiplied by fixed vectors of \(V\), so all its coefficients lie in one finite-dimensional subspace. The series \(v(q)\) does not.

For a cochain complex, Laurent completion here means \((V((q)))^n=V^n((q))\), degree by degree. Its lower bound may depend on \(n\). If another product index is present, its lower bounds require a separate decision. For example, the family \((q^{-r})_{r\geq0}\) belongs to

\[
\prod_{r\geq0}F((q)),
\]

but not to \((\prod_{r\geq0}F)((q))\): the latter requires a lower bound common to all coordinates. In the current complex below, the product index includes exterior arity. Requiring one lower bound across every arity would discard valid cochains.

There is also an order of scalar extension. Let

\[
A_0=\mathbb C[\lambda,\lambda^{-1},(\lambda-1)^{-1}],
\qquad F=\mathbb C(\lambda).
\]

The series \(\sum_{n\geq2}q^n/(\lambda-n)\) belongs to \(F[[q]]\). It does not lie in \(A_0[[q]]\otimes_{A_0}F\). An element of this algebraic localization has a common denominator in \(A_0\), whereas no one denominator clears the distinct poles \(\lambda=n\). Scalar extension before completion therefore permits more series than algebraic localization afterwards.

These distinctions also govern continuity. Multiplication by a fixed Laurent polynomial has a finite loss of \(q\)-order. A family of operations is continuous on a completed direct sum only if the required bound applies before its support is allowed to grow. A bound depending on bar length, for instance, need not suffice when bar length grows with the Laurent exponent.

## The line algebra and its spectral tensor {#ch08-the-line-algebra-and-its-spectral-tensor}

We now apply these conventions to a concrete comparison. Let

\[
\mathfrak g=\mathfrak{sl}_2(\mathbb C),\qquad
\kappa(E,F)=1,\quad\kappa(H,H)=2,\qquad k\in\mathbb C\setminus\mathbb Q.
\]

The affine mode algebra \(A=A_{-k-2}\) has relations

\[
[xt^r,yt^s]=[x,y]t^{r+s}
 +r\delta_{r+s,0}(-k-2)\kappa(x,y)1.
\]

Put \(\mathfrak n=t\mathfrak g[t]\), \(U=U(\mathfrak g)\), and \(W=A\otimes_{U(\mathfrak n)}\mathbb C\). A smooth affine module is one in which every vector is annihilated by all sufficiently high positive modes; the bound can depend on the vector.

The differential graded line algebra \(Y=Y_k\) of Chapter 6 has even current generators \(B_n^a\) and odd generators \(c_{a,n}\), for \(n\geq0\). The latter have cohomological degree one. Their internal energies are \(n\) and \(n+1\), respectively; energy is a separate grading. To recall their concrete meaning, the induced Chevalley resolution

\[
P^{-p}=A\otimes\Lambda^p\mathfrak n
\]

carries right operators \(B_n^a\mapsto R_{t_at^{-n}}-a_{t_at^{-n}}\) and \(c_{a,n}\mapsto\iota_{a,n+1}\). Here \(R\) is right multiplication, \(a_x\) is the exterior derivation obtained by projecting \([x,-]\) to \(\mathfrak n\), and \(\iota_{a,n+1}\) contracts the indicated positive mode. The differential of \(Y\) is compatible with these operators. They represent line operations on the boundary resolution, including the odd operations that would be lost by keeping only ordinary endomorphisms. The full presentation and its energy-restricted endomorphism comparison are given in *Line operators and the boundary derived functor*, §“Lifts of the line generators.”

For ordinary, possibly unbounded, left \(Y\)-modules \(M,N\), form the algebraic tensor complex \(T=M\otimes N\). Let \(q=z^{-1}\). The spectral tensor has underlying complex \(T((q))\), but its differential includes the interaction

\[
S_z(T)=\bigl(T((q)),d_T+\rho_T(r(q))\bigr),
\]

\[
r(q)=\sum_{a,i,j\geq0}(-1)^i\binom{i+j}{i}q^{i+j+1}
 \bigl(c_{a,i}\otimes B_j^a-B_i^a\otimes c_{a,j}\bigr).
\]

The invariant form contracts the Lie indices. Every coefficient is a finite algebraic operator, and every term has positive \(q\)-order. Write \(d_Y\) for the differential of \(Y\). On the tensor-product algebra \((Y\otimes Y)((q))\), let \(Q\) be the induced differential

\[
Q(a\otimes b)=d_Ya\otimes b+(-1)^{|a|}a\otimes d_Yb,
\qquad Q(q)=0,
\]

extended coefficientwise. The identity

\[
Q r+r^2=0
\]

makes the corrected differential square to zero. It is the equation that permits the interaction, rather than a prescription to tensor two representations and ignore their coupling.

## The incoming bar, its completion, and the outgoing bar {#ch08-the-incoming-bar-its-completion-and-the-outgoing-bar}

The bar construction from Chapter 5 resolves the incoming module relations. Write \(\mathbf B=Y\otimes Y\). Its length-\(r\) term is

\[
\mathbf B\otimes\overline{\mathbf B}^{\otimes r}\otimes T,
\qquad\overline{\mathbf B}=\mathbf B/\mathbb C1,
\]

with total degree equal to internal cohomological degree minus \(r\). The relevant completed complex is

\[
\mathcal B_z(T)=
\left(\operatorname{Tot}_{\oplus}
 \operatorname{Bar}_{\mathbf B}(\mathbf B,T)\right)((q)),
\qquad d=d_{\rm bar}+L_{r(q)}.
\]

The tensor diagonals and bar lengths are summed before completion. At a fixed Laurent coefficient there are finitely many words and finitely many tensor-diagonal components. Those finite supports can grow with the exponent.

The original augmentation \(\mathcal B_z(T)\to S_z(T)\) is a quasi-isomorphism. Its mechanism is instructive. Before the correction, insertion of a unit gives a contracting homotopy \(h\) of Laurent order zero. Perturbing by \(\delta=L_{r(q)}\) gives a homotopy of the form

\[
H=h(1+\delta h)^{-1}
 =h\sum_{j\geq0}(-\delta h)^j.
\]

Each occurrence of \(\delta\) raises \(q\)-order. Only finitely many terms contribute to a fixed coefficient, and each such term is an algebraic bar vector. This proves convergence on the specified complex without interchanging an inverse limit with a bar realization. The projection remains the original augmentation. See *Rational evaluation on the completed incoming bar*, Proposition 1.

The smooth realization is a different operation. For the specified smooth affine–right-\(Y\) object \(\mathcal W\), put

\[
\Phi_K(V)=\mathcal W_K\otimes^{\mathbb L}_{Y_K}V,
\qquad K=\mathbb C((q)).
\]

To compute this derived tensor after forming \(\mathcal B_z(T)\), use a separate **algebraic outgoing bar** over \(Y_K\). It receives no further Laurent completion. The completed spectral module is not assumed to be \(K\)-flat over \(Y_K\).

The evaluation map is fixed on these bars. If \(p\) is an outgoing rational-current resolution word, it sends

\[
p\otimes b_0[b_1|\cdots|b_r]t
\longmapsto
\Delta_{\rm rat}(p)b_0[b_1|\cdots|b_r]t.
\]

The map \(\Delta_{\rm rat}\) expands rational currents at the incoming points and splits their exterior principal parts. Its Laurent loss depends on \(p\), uniformly in the incoming length, letters and terminal vector. A vector in the outgoing algebraic bar uses finitely many such \(p\), so their bounds have a common minimum. Its restriction along the affine resolution is the original affine evaluation, usually denoted \(b_{M,N}\); the rational evaluation is denoted \(\eta_{M,N}\). Their construction precedes the theorem that they induce an equivalence.

## A comparison for any finite number of radial inputs {#ch08-a-comparison-for-any-finite-number-of-radial-inputs}

Take \(d\geq2\) ordered points and fix their shape by

\[
t_{d-1}=1,\quad t_d=0,\qquad
A_0=\mathbb C[t_1,\ldots,t_{d-2},
 (\prod_{i<j}(t_i-t_j))^{-1}],
\]

\[
F=\operatorname{Frac}(A_0),\qquad K=F((q)),\qquad a_i=q^{-1}t_i.
\]

Thus \(q\) measures inverse overall separation, while the \(t_i\) describe the shape. Algebraic scalar extension to \(F\) takes place before Laurent completion. For \(d=2\), \(F=\mathbb C\).

For ordinary unbounded \(Y_F\)-modules \(M_i\), put \(T=\operatorname{Tot}_{\oplus}(M_1\otimes_F\cdots\otimes_FM_d)\). The corrected differential uses the pair sum

\[
R_{\mathbf a}=\sum_{i<j}r_{ij}(a_i-a_j),
\qquad S_{\mathbf a}(T)=(T((q)),d_T+\rho_T(R_{\mathbf a})).
\]

Every pair occurs, including nonconsecutive pairs. The outgoing action on either type of generator \(y_n=B_n^a,c_{a,n}\) is

\[
\Delta_{\mathbf a}(y_n)=
\sum_{i=1}^d\sum_{m=0}^n\binom nm
 q^{m-n}t_i^{n-m}y_m^{(i)}.
\]

To define the independent current complex, split rational currents into polynomial currents \(\mathfrak p=\mathfrak g[u]\) and proper currents \(x/(u-a_i)^s\), \(s\geq1\). “Proper” here means vanishing at infinity. Set

\[
C=\bigoplus_{e\geq0}U(\mathfrak n)_e^*.
\]

The energy pieces are finite-dimensional; this is their direct-sum dual. At proper exterior arity \(b\), use

\[
\mathscr R_{d,b}(V)=
\bigl(C_F^{\otimes d}\otimes_F
 \Lambda^b(\mathfrak n_F^{\oplus d})^{\circ}\otimes_F V\bigr)((q)),
\]

where \(\circ\) likewise means the direct-sum dual of finite total-pole-index pieces. For a smooth affine test complex \(X\), define

\[
\mathcal I_d^r(X;T)=
\prod_{a,b\geq0}\prod_{e\in\mathbb Z}
\operatorname{Hom}_K\!\left(
 \Lambda^a\mathfrak p_K\otimes_K X^e,
 \mathscr R_{d,b}(T^{r+e-a-b})\right).
\]

Its differential is the total Chevalley–Eilenberg and mapping-complex differential for the rational-current action. Each coefficient has finite cofree and proper-mode support. On a fixed exterior arity and finite polynomial/test stage it has a lower Laurent bound; the bound is a bound on the finite coordinate matrix and need not be uniform over other stages or arities. All displayed products are retained. This definition comes from current operations and their support conditions, independently of smooth realization.

Let \(D_{\mathcal N}(A_K)\) be the full subcategory of the original smooth derived category whose cohomology has jointly locally nilpotent positive currents: each cohomology vector is killed by all sufficiently long products of positive currents. Its maps are the ambient derived maps.

**Theorem — finite radial current comparison.** Assume the specified coherent smooth affine–right-\(Y\) realization, its tensor–Hom adjunction and full unit for ordinary unbounded \(Y\)-modules, its algebraic cofree model and common mode-cutoff actions. Assume also that every bounded-below smooth complex with jointly locally nilpotent positive-current cohomology belongs to the localizing category generated by \(W_K\), and that the derived ideal triangle expresses each \(Y_F\)-module by two complexes inflated from \(U_F\). Here inflation uses the augmentation \(Y_F\to U_F\), and the localizing category is closed under shifts, cones and arbitrary coproducts. Then, for every finite \(d\geq2\), every ordinary unbounded tuple \(M_1,\ldots,M_d\), and every \(X\in D_{\mathcal N}(A_K)\), the actual evaluation gives an equivalence

\[
\Xi_T(X):
R\operatorname{Hom}_{\operatorname{Sm}(A_K)}
 \bigl(X,\mathcal W_K\otimes^{\mathbb L}_{Y_K}S_{\mathbf a}(T)\bigr)
\xrightarrow{\sim}\mathcal I_d(X;T).
\]

The comparison retains the outgoing line action, all its specified higher compatibilities, and every additional commuting incoming right action. At the regular tuple it retains all \(d\) incoming regular right actions. Its coefficient evaluations are the rational maps \(\eta_{M_1,\ldots,M_d}\) and their original affine restrictions \(b_{M_1,\ldots,M_d}\). The theorem uses the bar and scalar-extension orders stated above. See *The radial finite-puncture current recipient*, equation (45).

The proof begins with inputs inflated from \(U_F\), so the ghosts act by zero. The proper-current complex then contracts at order zero by the energywise dual of the free Chevalley contraction. Cross-point terms have positive Laurent order and increase mode support by at most that order. Perturbation therefore preserves the required support. Composed with this contraction, the actual comparison is \(1+A\), with \(A\) of positive order, and has a coefficientwise geometric inverse.

For bounded-below inputs, representability and the positive-current torsion theorem extend this calculation to every ambient test in \(D_{\mathcal N}\). Explicit truncation towers then handle unbounded inflated inputs; their componentwise stabilization does not require a bound uniform over the product factors of \(\mathcal I_d\). Finally, the two inflated terms of the ideal triangle extend the equivalence to one arbitrary input at a time. There are finitely many such steps. No infinite incoming bar is moved through a continuous Hom, and no equality \(D_{\mathcal N}=\operatorname{Loc}(W_K)\) is required.

## Finite integral heads and separated values {#ch08-finite-integral-heads-and-separated-values}

There is a second useful route to the regular comparison. Before inverting the separation discriminant, one can work over \(R_d=\mathbb C[a_1,\ldots,a_{d-1}]\). The protected coefficient complex is generated by seeds \(\Delta^w\mathscr C_w^{\otimes d}\), where \(\Delta=\prod_{i<j}(a_i-a_j)\) and \(\mathscr C_w\) is the energy-\(w\) relative dual of the line algebra. The discriminant powers compensate the pole budgets. Closing these seeds under the specified currents and derivatives gives actual integral coefficient and current-chain complexes.

A finite *head* bounds top energy, proper pole budget and derivative order. Each such head is a bounded perfect relative complex, so its derived dual commutes with derived scalar base change. After separation, normalized head duals assemble into the explicit complex

\[
\widehat D^n=
\left(\bigoplus_N(D_N^0)^n\right)((q))
\oplus\left(\bigoplus_N(D_N^0)^{n-1}\right)((q)),
\]

\[
d(f,g)=\bigl(d_Df,(R_Nf_{N+1}-qf_N)_N-d_Dg\bigr).
\]

Here \(D_N^0\) is the normalized head dual and \(R_N\) its restriction matrix after removing the common \(q^{-1}\) factor. This formula specifies finite head support at every coefficient and one common lower Laurent bound. It does not use the unrestricted algebraic dual of the infinite head union.

Evaluation is the original tensor–Hom map

\[
\eta(p\otimes f)(l)=(-1)^{|p||f|}f(p\otimes l).
\]

For fixed \(p\), insertion changes the head \(N\) to \(N+c(p)\). Normalization gives a Laurent loss depending on \(p\), independent of \(N\). Evaluation and its homotopies therefore extend to the completed head complexes. For the full incoming bar, the stronger estimate is uniform in incoming length, including arbitrarily long words of energy zero. These estimates identify the separated head construction with the same evaluation used above. The two occupied-vacuum orders also have actual completed comparison roofs at the regular output test, retaining the surviving regular action. See *Integral kernels and the separated comparison diagrams*, §§1–3.

This separation of domains has a geometric consequence. A collision fibre sets a factor of \(\Delta\) to zero, whereas the separated Laurent chart has inverted \(\Delta\). Derived collision maps are obtained from the integral finite heads before that inversion. They cannot be obtained by substituting a collision into every vector of the separated Laurent complex.

## Common radial sewing and a failed substitution {#ch08-common-radial-sewing-and-a-failed-substitution}

The finite-point theorem permits a definite form of sewing: the original kernels can be composed along any finite binary tree on the same radial domain. The translation \(\tau_x\) of the source algebra \(Y\) is defined on either generator \(y_n=B_n^a\) or \(y_n=c_{a,n}\) by

\[
\tau_x(y_n)=\sum_{m=0}^n\binom nm x^{n-m}y_m,
\]

and extended multiplicatively. For fixed modes its kernel identities are rational identities,

\[
(\tau_x\otimes1)r(y)=r(y+x),\qquad
(1\otimes\tau_x)r(y)=r(y-x).
\]

Continue those coefficients rationally before expanding radially. Each pair of leaves first meets at one vertex, so the tree contributes each term of \(R_{\mathbf a}\) exactly once. Associative principal-part splitting gives the same rational and affine evaluations on the common completed incoming bar.

A separately completed nested tensor need not have that domain. In a three-point shape chart,

\[
f=\sum_{n\geq0}q^n\lambda^{-n^2}\in\mathbb C(\lambda)((q)).
\]

The substitution \(\lambda=zq\) would give

\[
\sum_{n\geq0}z^{-n^2}q^{n-n^2}.
\]

Its outer \(q\)-orders have no lower bound, so it is not in \(\mathbb C((z^{-1}))((q))\). The terms tend to zero before substitution and fail to do so afterwards. This is an obstruction to extending that substitution continuously to the entire radial field. It leaves the common radial sewing theorem intact and identifies the extra support estimate needed for a larger nested domain.

### Three rational poles and a finite-total spectator {#ch08-three-pole-comparison}

A separately completed pair-first operation has an actual comparison when its intermediate rational currents are retained. Fix the nonrational \(\mathfrak{sl}_2\) setting of this chapter and write
\[
a_1=z+w,\quad a_2=z,\quad a_3=0,
\qquad p=w^{-1},\quad q=z^{-1},
\qquad K_w=\mathbb C((p)),\quad K_N=K_w((q)).
\]
The inner rational current algebra has poles at \(u-z=w,0,\infty\). Let \(P_c^{(12)}\) be its induced Chevalley resolution, \(P_c^{(3)}\) the full three-pole resolution, and \(P\) the original affine resolution for the third slot. The outer tensorator has the precise target
\[
\Delta^{(12|3)}:P_c^{(3)}
\longrightarrow
\bigl(P_c^{(12)}\otimes_{\mathbb C}P\bigr)((q)).
\]
It is a chain map for the right-twisted differential, with the actual incoming rational action and outgoing line action, normalized by \(1\mapsto1\otimes1\), and satisfies
\[
(\Delta^{(12)}\otimes1)\Delta^{(12|3)}=\Delta^{(3)}
\]
on the entire three-pole resolution. The rational intermediate resolution retains the extra pole missed by the affine cluster resolution. [Full-source tensorator](atlas.html#atlas-c-horizontal-full-three-pole-tensorator).

The bar comparison gives a full-source derived evaluation into the original binary target. Its affine inclusion is a quasi-isomorphism in the original two-pole current category, and restriction recovers the original binary evaluation. This does not put a new strict three-pole action on the literal old complex. The further evaluation from the rational-cluster target to the triple target is not asserted to be a quasi-isomorphism.

For a constant input \(T=T_{12}\otimes_{\mathbb C}M_3\), distinguish the joint intermediate object from the factorized one:
\[
E=S_w^{12}(T),\qquad
E_1=S_w(T_{12})\otimes_{\mathbb C}M_3,
\qquad c:E_1\longrightarrow E.
\]
Here \(T_{12}\) may be correlated and unbounded, and the symbol \(M_3\) denotes the third line-module input. If \(H^\bullet(M_3)\) has finite **total** dimension, \(c\) is a quasi-isomorphism. Under the chapter's retained coherent native realization and full-unit hypotheses, the full three-pole evaluation then reaches the independently factorized endpoint, preserving affine restriction and the native outgoing unit. Strict commutativity holds in the displayed algebraic bar models; smooth replacement retains the enhanced comparison and its specified coherences. A fixed left comb admits stagewise comparisons when each newly attached spectator has finite-total cohomology. Finite dimension in each degree does not suffice. [Finite-total native comparison](atlas.html#atlas-c-horizontal-full-three-pole-native-finite-total).

There are two separate limits to this result. For trivial first inputs and third input given by the regular \(U=U(\mathfrak{sl}_2)\)-module, inflated along \(Y\to U\),
\[
E/E_1=U((p))/(U\otimes_{\mathbb C}K_w)\ne0
\]
with zero differential. The full-source evaluation still exists, but \(c\) is not a universal equivalence. Also, the common coefficient domain between radial and nested expansions has nonzero comparison cones even at trivial input; the finite-total theorem does not remove them. Its coefficientwise support bounds neither reverse the Laurent order nor identify the native outer-adic topology with the topology of that common domain.

### A common domain for the factorized intermediate object {#ch08-factorized-common-domain}

The regular spectator requires a comparison with the actual separately completed object. This comparison has an algebraic domain determined by the two carriers. Put \(s=q/p=w/z\), so that the substitution \(q=sp\) identifies \(K_w((q))\) with \(K_w((s))\), and set
\[
\mathcal O=\mathbb C[s]_{(s)},\qquad
D=\mathcal O((p))[s^{-1}],\qquad
K_R=\mathbb C(s)((p)),\qquad
K_N=\mathbb C((p))((s)).
\]
For the constant input \(T=T_{12}\otimes M_3\), define
\[
L_D(T)=(T\otimes\mathcal O)((p))[s^{-1}],\quad
L_R(T)=(T\otimes\mathbb C(s))((p)),\quad
L_N(T)=T((p))((s)).
\]
Each carrier has differential \(d_T+\rho_T(R)\), where
\(R=r_{12}(w)+r_{13}(z+w)+r_{23}(z)\), and the prescribed outgoing line action. An element of \(L_D\) has one lower \(s\)-bound across its whole \(p\)-series. The actual pair-first object has carrier
\[
N_1(T)=\bigl(T_{12}((p))\otimes M_3\bigr)((s))\subset L_N(T)
\]
with that same differential. Its intermediate module is the independently defined \(E_1=S_w(T_{12})\otimes M_3\).

The common domain is the coefficient-array intersection
\[
L_D^{\mathrm{fac}}(T)=L_D(T)\cap N_1(T)=L_R(T)\cap N_1(T).
\]
Degree by degree, for each outer exponent \(j\), its \(s^j\)-coefficient belongs to \(T_{12}((p))\otimes M^{(j)}\) for some finite-dimensional graded subspace \(M^{(j)}\subset M_3\). The subspace may grow with \(j\), but it works for the entire inner \(p\)-series at that outer coefficient. This condition makes the intersection a dg \(Y_D\)-module and gives actual maps
\[
L_R(T)\longleftarrow L_D^{\mathrm{fac}}(T)\longrightarrow N_1(T).
\]
The construction preserves quasi-isomorphisms in each input. The outgoing action and factorwise incoming actions preserve it; a general commuting endomorphism of the joint input need not preserve finite spectator support. [The factorized common domain](atlas.html#atlas-c-horizontal-factorized-common-domain).

If \(H^\bullet(M_3)\) has finite total dimension, the canonical inclusion \(L_D^{\mathrm{fac}}(T)\to L_D(T)\) is a quasi-isomorphism. A contraction of the underlying spectator complex to its finite cohomology suffices; no line-module structure on that auxiliary cohomology is required. The cross perturbation has positive order in both \(p\) and \(s\), so only finitely many spectator operators contribute at each fixed outer order. Both domains retract onto the same transferred complex. Their raw comparison cones consequently agree with the joint-domain cones. They need not vanish: at trivial input they are \(K_R/D\) and \(K_N/D\). [Finite-total comparison and its cones](atlas.html#atlas-c-horizontal-factorized-common-finite-total).

This domain reaches the actual independently completed endpoint. Evaluating the original full regular-current kernel on an incoming bar adapted to the intersection is a further construction. For the regular input \(T=Y^{\otimes3}\), the spectral vector \(\mathbf1\) and its differential \(R\mathbf1\) lie in the domain, but do not supply that evaluation. Its native outer topology and its comparison cones outside the finite-total hypothesis remain part of the problem.

### Tests over a coefficient ring {#ch08-common-ring-tests}

The common ring \(D\) is not a field, and an ordinary Hom formula can detect a choice of test representative. Let \(g=p+s\). Substitution \(p=-s\) maps \(D\) to \(\mathbb C((s))\) and kills \(g\), so \(g\) is a nonunit. The complex
\[
E=(D\xrightarrow{g}D\longrightarrow D/g),
\qquad E^0=D,\quad E^1=D,\quad E^2=D/g,
\]
is acyclic, but \(H^0\operatorname{Hom}_D(E,D)=D/g\ne0\). Let \(W_D\) be the scalar extension to \(D\) of the regular-top affine object in the tensor–Hom realization. For trivial incoming coefficient, the ordinary current formula on the acyclic smooth test \(W_D\otimes_D E\) retracts onto this nonacyclic Hom complex. Thus that formula cannot define the proposed functor on arbitrary derived \(D\)-tests. The field and constant ground-field test theorems retain their stated scope. [The ordinary-Hom counterexample](atlas.html#atlas-c-horizontal-common-ring-hom-counterexample).

A positive comparison holds on explicit finite \(W_D\)-cell models: bounded complexes formed from \(W_D\) by finitely many shifts, finite sums and cones, with their actual enhanced maps. Finite cone induction extends the comparison at \(W_D\), and proves invariance under quasi-isomorphisms between these models. This includes the finite induced Chevalley model of the parameter-Verma family. A value on an arbitrary representative, or on every object generated by unrestricted coproducts, requires a derived test construction and its support theorem. [Finite cell tests](atlas.html#atlas-c-horizontal-common-ring-finite-cell-tests).

### Two independently completed clusters {#ch08-incomparable-clusters}

For the configuration \((z+w_1,z,w_2,0)\), set \(p_i=w_i^{-1}\), \(q=z^{-1}\) and \(s_i=q/p_i\). The two inner completions have four distinct coefficient carriers. Their scalar rings are
\[
\Lambda_{\mathrm{fac}}=\mathbb C((p_1))\otimes_{\mathbb C}\mathbb C((p_2)),\qquad
\Lambda_{\mathrm{sym}}=\mathbb C[[p_1,p_2]][(p_1p_2)^{-1}],
\]
\[
F_{12}=\mathbb C((p_1))((p_2)),\qquad
F_{21}=\mathbb C((p_2))((p_1)).
\]
For \(T=T_{12}\otimes T_{34}\), the independently completed inner object is \(E_{\mathrm{fac}}=S_{w_1}(T_{12})\otimes S_{w_2}(T_{34})\). Its next spectral operation is \(N_{\mathrm{fac}}=S_z^{\Lambda_{\mathrm{fac}}}(E_{\mathrm{fac}})\), whose carrier is \(E_{\mathrm{fac}}((q))\). The ordered objects \(N^{12},N^{21}\) have carriers \(T((p_1))((p_2))((q))\) and \(T((p_2))((p_1))((q))\), with the common four-point spectral differential. Their array intersection is
\[
N_{\mathrm{sym}}=
\bigl(T[[p_1,p_2]][(p_1p_2)^{-1}]\bigr)((q)).
\]
Both images of \(N_{\mathrm{fac}}\) have identical coefficients there. The two ordered fields remain distinct. [The four coefficient objects](atlas.html#atlas-c-horizontal-two-cluster-coefficient-objects).

If both pair inputs have finite total cohomology, then for either \(F=F_{12}\) or \(F_{21}\), the canonical maps
\[
N_{\mathrm{fac}}\otimes_{\Lambda_{\mathrm{fac}}((q))}F((q))
\longrightarrow S_z^F(E_{\mathrm{fac}}\otimes_{\Lambda_{\mathrm{fac}}}F)
\longrightarrow N^F
\]
are quasi-isomorphisms. Under the retained native realization hypotheses, they preserve the independent binary recipients, evaluations and tensor–Hom units on the full ambient field tests. The unextended scalar legs are different maps and need not be equivalences. [Finite-total pair comparison](atlas.html#atlas-c-horizontal-two-cluster-finite-total).

To compare with the radial four-point carrier, define
\[
\mathcal O_2=\mathbb C[s_1,s_2]_{(s_1,s_2)},\qquad
\mathfrak q=s_1^{-1}\mathcal O_2+s_2^{-1}\mathcal O_2,
\]
\[
D_{\mathrm{con}}=\bigcup_{c\ge0}
\left\{\sum_{n\ge-c}q^n\theta_n:
\theta_n\in\mathfrak q^{n+c}\right\}.
\]
The fractional-ideal condition bounds the sum of the two pole orders and ensures local finiteness after \(s_i=q/p_i\). It embeds \(D_{\mathrm{con}}\) into \(\Lambda_{\mathrm{sym}}((q))\). Let \(L_{D_{\mathrm{con}}}(T)\) be the same series construction with coefficients \(\theta_n\in T\otimes\mathfrak q^{n+c}\), carrying the four-point spectral differential. The factorized intersection needs the smaller scalar ring
\[
D_*=D_{\mathrm{con}}\cap\Lambda_{\mathrm{fac}}((q)),\qquad
L_*^{\mathrm{fac}}(T)=L_{D_{\mathrm{con}}}(T)\cap N_{\mathrm{fac}}(T),
\]
where both intersections use the symmetric expansion. At each outer coefficient, membership in \(N_{\mathrm{fac}}\) means a finite algebraic sum of tensors of the two completed cluster factors. The intersection is a dg \(Y_{D_*}\)-module with maps to the radial and factorized endpoints. In general it is not a \(D_{\mathrm{con}}\)-module: the scalar series \(\sum_{n\ge0}p_1^np_2^n\) lies in the conic expansion but has infinite separated rank at outer order zero. [The scalar ring of the factorized intersection](atlas.html#atlas-c-horizontal-four-point-factorized-intersection).

The full four-pole rational tensorator and its algebraic bar identities also exist, with the two rational cluster resolutions retained. They do not provide an ambient current-recipient theorem over these nonfield rings, or an adapted full-current evaluation on \(L_*^{\mathrm{fac}}\). Strict agreement of coefficients in the two inner orders is one ingredient of the required native interchange; compatibility with the full bars, native topology, associativity in larger trees and all parameter facets remains to be constructed. [Four-pole evaluation and its scope](atlas.html#atlas-c-horizontal-four-pole-rational-tensorator).

### Occupied deletion and parameter variation {#ch08-deletion-and-spectral-connection}

There are positive operation results on these specified domains. A normalized trivial input can be deleted in any of the three slots: restrict proper-current functionals to wedges with no factor in that slot, then apply its normalized cofree energy-zero covector. The resulting current map is a quasi-isomorphism on all ambient tests over \(K_R,K_N\), and on constant ground-field ambient tests for \(D\). It preserves the original evaluation at the surviving positions. Deleting slot three leaves the nonanchored pair \((z+w,z)\), with outgoing action \(\Delta_w\circ\tau_z\). Comparing its tests with the anchored inner recipient, integral collision deletion, nonzero jets and opposite insertion maps remain separate. The normalized trivial input is distinct from the regular line input. [Occupied deletion](atlas.html#atlas-c-horizontal-occupied-deletion-all-slots).

For constant inputs at any finite number of positions \(a_i\), write \(R_{\mathbf a}=\sum_{i<j}r_{ij}(a_i-a_j)\). Let \(L\) be the odd line-algebra derivation determined by \(Lc_{a,n}=k^{-1}\kappa^{ab}B^b_n\), \(LB^a_n=0\), and \([Q,L]=T_Y\), with \(Q\) the line differential. Acting in slot \(i\), it defines
\[
X_i=L^{(i)}R_{\mathbf a},\qquad
\nabla_i=\partial_{a_i}+\rho_T(X_i).
\]
This connection is flat and commutes strictly with the spectral differential. The outgoing action is horizontal up to the explicit homotopies \(\lambda_i=L^{(i)}\Delta_{\mathbf a}\). These identities do not construct a connection on arbitrary shape-dependent inputs or the current-recipient comparisons over polynomial forms. The normalized full-complex gauge, its inverse and action homotopies, and the native parameter and tree coherences remain further requirements. [The flat spectral connection](atlas.html#atlas-c-horizontal-flat-spectral-connection).

The next problem is spatial as well as algebraic. Boundary kernels are distributions whose derivatives acquire terms on collision loci. To compose them, one must specify their support and retain the terms created when an ordered region acquires a boundary. Chapter 9 develops those operations on the actual current complexes.

## References {#ch08-references}

- [*Line operators and the boundary derived functor*](#ref-ch08-01), affine resolution and line-generator comparison.
- [*Rational evaluation on the completed incoming bar*](#ref-ch08-02), Proposition 1 and the rational evaluation construction.
- [*The radial finite-puncture current recipient*](#ref-ch08-03), equations (20)–(23), (30)–(45), and the common radial sewing construction.
- [*Integral kernels and the separated comparison diagrams*](#ref-ch08-04), finite-head evaluation, incoming bars, occupied insertions and derived collision maps.

## Source manuscripts {#ch08-source-manuscripts}

### 1. Line operators and the boundary derived functor {#ref-ch08-01}

### 2. Rational evaluation on the completed incoming bar {#ref-ch08-02}

### 3. The radial finite-puncture current recipient {#ref-ch08-03}

### 4. Integral kernels and the separated comparison diagrams {#ref-ch08-04}
