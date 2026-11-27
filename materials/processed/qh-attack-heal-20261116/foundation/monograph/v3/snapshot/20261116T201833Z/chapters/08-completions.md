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
