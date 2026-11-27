# Tensor products, support and completion

Bring a third line to a pair whose product is already expanded in the inverse separation \(p\). Over the field \(F\), write \(T_{12}=M_1\otimes_F M_2\) for the state space of the pair and \(M_3\) for the third module. Choose a nonzero pair state \(v\) and independent third states \(w_0,w_1,\ldots\), taking all states in degree zero for this example. At any finite order \(m\) we can adjoin the third line *after* expanding the pair. The sum
\[
 s_m=\sum_{j=0}^{m}(p^j v)\otimes w_j
 \quad\longmapsto\quad
 \sum_{j=0}^{m}p^j(v\otimes w_j)
\]
belongs on either side of the coefficient map from \(T_{12}((p))\otimes_F M_3\) to \((T_{12}\otimes_F M_3)((p))\). Here \(T((p))\) denotes the space of Laurent series with coefficients in \(T\) and exponents bounded below.

Which side contains the limit? At order \(j\) the coefficient on the right stabilises at \(v\otimes w_j\). On the left every tensor is a finite sum \(\sum_{a=1}^r f_a(p)\otimes u_a\). Its coefficients all belong to \(T_{12}\otimes_F\operatorname{span}\{u_1,\ldots,u_r\}\). Apply a linear functional on \(T_{12}\) taking \(v\) to \(1\). If the limit came from the left, this one finite span would contain every \(w_j\). Their independence rules that out.

::: example {#ch08-current-on-spectator-states title="A current insertion after Laurent completion"}

What can a second field insertion do on the smaller space? Take \(F=\mathbb C\) and let the third states be one-quantum states of the neutral level-one current. Write \(\Omega\) for its vacuum, \(J(u)=\sum_n J_nu^{-n-1}\) for its field, and \(w_j=J_{-j-1}\Omega/(j+1)\) for \(j\ge0\). Insert the field at \(u\) and project onto the vacuum, with \(\langle\Omega,\Omega\rangle=1\). Only \(J_{j+1}\) can remove this quantum. Its commutator with \(J_{-j-1}\) is \(j+1\), so the amplitude is \(\langle\Omega,J(u)w_j\rangle=u^{-j-2}\). [The free-current contraction](03-local-fields.md#heisenberg-current).

Use the same formal parameter \(u=p\) for this insertion. On a finite sum of spectator states the amplitudes have a common bound on their pole orders. We may therefore multiply each by the corresponding Laurent series of pair states and add. On \(s_m\) this prescription gives
\[
 \sum_{j=0}^{m} p^j v\,\langle\Omega,J(p)w_j\rangle
       =(m+1)p^{-2}v .
\]
The inputs converge coefficient by coefficient in the joint completion. The coefficient of \(p^{-2}\) in the outputs never stabilises. Keeping the insertion at an independent coordinate gives the explanation in the free field itself. The infinite sum there is \(v/[u(u-p)]\), expanded in \(p/u\). It has a pole at the very value \(u=p\) at which the second insertion was requested. A finite spectator span was enough to define that insertion on the algebraic tensor. Enlarging its domain requires control of the poles of the states being admitted.

:::

## Tensor completion and matrix rank {#tensor-completion-and-rank}

**Example (finite-rank matrices).** Label the independent states in the example by rows and the powers of the separation by columns. The \(j\)th column has its only nonzero entry in row \(j\). Which matrices can a finite sum of products produce? In the space \(V=\mathbb C^{\mathbb N}\) of all complex sequences consider the map

\[
V\otimes_{\mathbb C}V\longrightarrow
\mathbb C^{\mathbb N\times\mathbb N},
\qquad f\otimes g\longmapsto(f_i g_j)_{i,j\geq0}.
\]
{#eq-sequence-tensor-map}

Its image consists of the matrices of finite rank. For \(\sum_{a=1}^r f^a\otimes g^a\), column \(j\) is \(\sum_a g^a_j f^a\). Conversely, choose a basis of the column space of a finite-rank matrix. The coefficients of the successive columns along each basis vector form the required second sequence. The diagonal matrix \((\delta_{ij})\) has infinitely many independent columns.

How can finite sums approximate this matrix? Give the image the coordinatewise topology inherited from the full matrix space. A test fixes finitely many entries. A diagonal projection onto the first \(m\) coordinates passes every such test against the identity once \(m\) exceeds the largest index tested. The same square truncation approximates any matrix, and the product of the coordinate spaces is complete. Thus the completion contains every matrix. The successive projection ranks show what the tests have ceased to bound.

::: figure fig-infinite-rank

In the matrix test the row and column indices had different jobs. A current state in a resolution carries four indices. Its cohomological degree determines a tensor diagonal, its bar length counts the inputs of a resolution word, its mode numbers specify the currents, and its Laurent exponent records the order in the separation. To multiply two such states one must decide, at each Laurent exponent, which of the other sums are finite. Start with the cohomological degree.

## Algebraic tensors and mapping complexes {#ch08-algebraic-tensors-and-mapping-complexes}

**Definition (algebraic tensor complex).** For cochain complexes \(M,N\), with differential of degree \(+1\), the algebraic tensor complex has

\[
(M\otimes N)^n=\bigoplus_{i+j=n}M^i\otimes N^j,
\qquad
d(m\otimes n)=dm\otimes n+(-1)^{|m|}m\otimes dn.
\]

Every element has finite support along the cohomological diagonal.

**Definition (mapping complex).** A map of degree \(r\) assigns a linear map to every input degree. The mapping complex has

\[
\operatorname{Hom}^{r}(M,N)
=\prod_i\operatorname{Hom}(M^i,N^{i+r}),
\qquad
d(f)=d_Nf-(-1)^rf d_M.
\]

Take one copy of \(\mathbb C\) in every integer degree of \(M=N\), with zero differential. An element of \((M\otimes N)^0\) has a component in \(M^i\otimes N^{-i}\) for only finitely many \(i\). Now try to write the identity map of \(M\). Its component \(M^i\to M^i\) is \(1\) in every degree. The product in the mapping complex contains that map. A direct sum in its place would lose even the identity.

Now regard a sequence as the input to a *continuous* scalar measurement. Put the discrete topology on each copy of \(\mathbb C\) and the product topology on the source. Every continuous linear functional

\[
\prod_{i\geq0}\mathbb C\longrightarrow\mathbb C
\]

depends on finitely many coordinates. The target is discrete, so the kernel is open. It contains all sequences that vanish on some fixed finite set of coordinates. Two sequences that agree on this set differ by an element of the kernel and therefore have the same value under the functional. An algebraic functional on \(\bigoplus_i\mathbb C\) can assign an arbitrary coefficient to every basis vector. Thus passing from a direct sum to a product and then taking a continuous dual can recover a direct sum. This conclusion depends on the displayed topology and on the discrete target.

In these topologies the two duals are \((\bigoplus_i\mathbb C)^*=\prod_i\mathbb C\) and \((\prod_i\mathbb C)'_{\mathrm{cont}}=\bigoplus_i\mathbb C\). Below we use algebraic tensor products on cohomological diagonals and continuous duals only for the stated mode and energy filtrations. Degree shifts follow \(V[1]^n=V^{n+1}\).

## Laurent series with algebraic coefficients {#ch08-laurent-series-with-algebraic-coefficients}

**Definition (degreewise Laurent completion).** Give the coefficient space \(V\) over \(F\) the discrete topology. The subspaces \(q^m V[[q]]\) are the neighbourhoods of zero in

\[
V((q))=\bigcup_{N\in\mathbb Z}q^N V[[q]].
\]

Here \(V[[q]]=\prod_{j\ge0}Vq^j\). Truncations converge because each prescribed coefficient eventually stabilizes and the omitted tail has order tending to infinity. An element of \(V((q))\) has one lower Laurent bound and an arbitrary sequence of coefficients in \(V\). If \(V=\bigoplus_{j\geq0}Fe_j\), then

\[
v(q)=\sum_{j\geq0}q^j e_j
\]

is allowed: each coefficient has finite support. There is no requirement that all coefficients lie in one finite-dimensional subspace of \(V\). Consequently

\[
V\otimes_F F((q))\subsetneq V((q))
\]

for this \(V\). The obstruction can be read from the coefficients alone.

**Lemma (finite coefficient span).** A vector-valued Laurent series with exponents bounded below comes from \(V\otimes_F F((q))\) exactly when its coefficients span a finite-dimensional subspace of \(V\).

*Proof.* A finite sum of elementary tensors uses only finitely many fixed vectors. Conversely, express every coefficient in a basis of their finite-dimensional span. Each basis coordinate gives a scalar Laurent series with the same lower bound, and their finite sum with those basis vectors recovers the given series. For \(v(q)\) the coefficient span contains every \(e_j\). ∎

For a cochain complex, Laurent completion here means \((V((q)))^n=V^n((q))\), degree by degree. Its lower bound may depend on \(n\). If another product index is present, its lower bounds require a separate decision. For example, the family \((q^{-r})_{r\geq0}\) belongs to

\[
\prod_{r\geq0}F((q)),
\]

but not to \((\prod_{r\geq0}F)((q))\): the latter requires a lower bound common to all coordinates. In the current complex below, the product index includes exterior arity. Requiring one lower bound across every arity would discard valid cochains.

A coefficient can also depend on the shape of the configuration. Clearing the denominator of one coefficient need not clear those of the whole series. Take

\[
A_0=\mathbb C[\lambda,\lambda^{-1},(\lambda-1)^{-1}],
\qquad F=\mathbb C(\lambda).
\]

The series \(\sum_{n\geq2}q^n/(\lambda-n)\) belongs to \(F[[q]]\). It does not lie in \(A_0[[q]]\otimes_{A_0}F\). An element of this algebraic localization has a common denominator in \(A_0\), whereas no one denominator clears the distinct poles \(\lambda=n\). Scalar extension before completion therefore permits more series than algebraic localization afterwards.

Which maps on Laurent polynomials still act after completion? Multiplication by a fixed Laurent polynomial costs at most its pole order at zero. Try instead the rule \(e_j\mapsto q^{-j}e_j\), extended \(F[q,q^{-1}]\)-linearly on polynomials with coefficients in \(\bigoplus_{j\ge0}Fe_j\). The inputs \(q^je_j\) tend to zero while every image has order zero. Applying the rule to \(\sum_{j=0}^n q^j e_j\) would require the constant coefficient \(e_0+\cdots+e_n\) to stabilize. The next application is to a bar word. Its length can grow with the Laurent exponent, so a loss estimate for each fixed length leaves precisely this difficulty.

## The line algebra and its spectral tensor {#ch08-the-line-algebra-and-its-spectral-tensor}

For two current lines there is an interaction to add to the ordinary tensor differential. Each coefficient acts on the two incoming states. Adding the interaction to the tensor differential must give a degree-one operator whose square is zero. We can identify its even and odd operators on a boundary resolution. For the rest of the current example use

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

The differential graded line algebra \(Y=Y_k\) has even current generators \(B_n^a\) and odd generators \(c_{a,n}\), for \(n\geq0\). The latter have cohomological degree one. Their internal energies are \(n\) and \(n+1\), respectively; energy is a separate grading. To recall their concrete meaning, the induced Chevalley resolution

\[
P^{-p}=A\otimes\Lambda^p\mathfrak n
\]

carries right operators \(B_n^a\mapsto R_{t_at^{-n}}-a_{t_at^{-n}}\) and \(c_{a,n}\mapsto\iota_{a,n+1}\). Here \(R\) is right multiplication, \(a_x\) is the exterior derivation obtained by projecting \([x,-]\) to \(\mathfrak n\), and \(\iota_{a,n+1}\) contracts the indicated positive mode. On the one-letter word \(t_b t^{n+1}\) the odd operator gives \(\delta_{ab}\). On the empty word it gives zero. Thus evaluation on exterior degree zero alone misses an operation that will occur in the first coefficient of the interaction. The operators on the whole resolution respect the differential of \(Y\). The algebraic endomorphism comparison allows a product over resolution degrees at each homogeneous energy shift, then a direct sum over shifts. To use these actions on smooth modules one also needs compatible truncations of the positive currents. For a finite diagram of operators one chooses a common \(N\) and keeps the modes below \(t^N\mathfrak g[t]\) in the Taylor resolution. The smooth endomorphism comparison and the tensor–Hom adjunction are additional hypotheses. [Affine currents and the algebra acting on their resolution](06-duality-and-induction.md#ch06-affine-currents-and-the-algebra-acting-on-their-resolution).

**Definition (spectral tensor).** Place two ordinary left \(Y\)-modules \(M,N\) at formal separation \(z\). They may be unbounded. Form \(T=M\otimes N\) with its algebraic tensor differential \(d_T\), and let \(\rho_T\) be the graded action of \(Y\otimes Y\) on \(T\). With \(q=z^{-1}\), the spectral tensor is

\[
S_z(T)=\bigl(T((q)),d_T+\rho_T(r(q))\bigr),
\]

\[
r(q)=\sum_{a,i,j\geq0}(-1)^i\binom{i+j}{i}q^{i+j+1}
 \bigl(c_{a,i}\otimes B_j^a-B_i^a\otimes c_{a,j}\bigr).
\]

Only \(i=j=0\) contributes at order \(q\). At order \(q^2\) the two possible pairs are \((0,1)\) and \((1,0)\), with opposite signs. More generally the coefficient of \(q^n\) uses just the \(n\) pairs \(i+j=n-1\), and the invariant form contracts the finite Lie index. The first possible order is \(q\), so every application of the interaction raises the Laurent order by at least one. Write \(d_Y\) for the differential of \(Y\). On the tensor-product algebra \((Y\otimes Y)((q))\), let \(Q\) be the induced differential

\[
Q(a\otimes b)=d_Ya\otimes b+(-1)^{|a|}a\otimes d_Yb,
\qquad Q(q)=0,
\]

extended coefficientwise. The identity

\[
Q r+r^2=0
\]

is the Maurer–Cartan equation in \((Y\otimes Y)((q))\). Write \(r=q r_1+q^2r_2+\cdots\). At first order \(Qr_1=0\). At the next order the two successive actions of \(r_1\) give \(r_1^2\), and \(Qr_2=-r_1^2\) cancels them. Applying the tensor-product representation \(\rho_T\) gives \((d_T+\rho_T(r))^2=\rho_T(Qr+r^2)=0\). Thus two lines at the prescribed separation carry a coupled differential on their completed state space. To attach a third line we must retain enough of its states for the next such differential to act. The finite spectator calculation tests that requirement on underlying vectors. For complexes the decisive question is which of the extra vectors survive in cohomology. [Three rational poles and a finite-total spectator](#ch08-three-pole-comparison).

## The incoming bar, its completion, and the outgoing bar {#ch08-the-incoming-bar-its-completion-and-the-outgoing-bar}

Put \(\mathbf B=Y\otimes Y\). Choose degree-zero cycles \(b_0,b_1\in\mathbf B\) and \(t\in T\). In the module \(T\), associativity gives \((b_0b_1)t=b_0(b_1t)\). In a free resolution the two length-zero tensors \((b_0b_1)\otimes t\) and \(b_0\otimes(b_1t)\) can be different. Their difference is the boundary of the one-letter word \(b_0[b_1]t\). Applying the augmentation sends that boundary to the difference of the two equal states. Longer words compare successive multiplications. In general the length-\(r\) term of the augmented bar of \(T\) is

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

On a length-one word \(b_0[b_1]t\) the two bar faces multiply \(b_0b_1\) and act by \(b_1t\), respectively. The operator \(L_{r(q)}\) multiplies the first coefficient \(b_0\). The tensor diagonals and bar lengths are summed before completion. At a fixed Laurent coefficient there are finitely many words and finitely many tensor-diagonal components. Those finite supports can grow with the exponent. [Words and the reduced bar construction](05-bar-and-coherence.md#ch05-words-and-the-reduced-bar-construction).

**Proposition (completed bar augmentation).** The augmentation \(\mathcal B_z(T)\to S_z(T)\) multiplies the length-zero coefficient into \(T\), kills positive lengths, and is a quasi-isomorphism. [Rational evaluation on the completed incoming bar, Proposition 1](#ref-ch08-02).

First set the interaction \(r(q)\) to zero. Inserting a unit contracts the augmented bar resolution onto \(T\), and the contracting homotopy \(h\) preserves Laurent order. Perturbing by \(\delta=L_{r(q)}\) gives a homotopy of the form

\[
H=h(1+\delta h)^{-1}
 =h\sum_{j\geq0}(-\delta h)^j.
\]

Each occurrence of \(\delta\) raises \(q\)-order. Only finitely many terms contribute to a fixed coefficient, and each such term is an algebraic bar vector. This proves convergence on the specified complex without interchanging an inverse limit with a bar realization. Write \(\varepsilon\) for the augmentation. On a word of length zero, multiplying the first coefficient by \(r(q)\) and then acting on \(t\) gives \(\varepsilon\delta=\rho_T(r(q))\varepsilon\). On words of positive length both sides vanish. Inserting the unit raises the bar length, so \(\varepsilon h=0\) and hence \(\varepsilon\delta h=0\). Every correction to the perturbed projection \(\varepsilon(1+\delta h)^{-1}\) therefore vanishes.

The augmentation has recovered the two-line state as a module. To compare it with currents on an affine test, one still has to turn that module into a smooth affine complex. The bimodule \(\mathcal W\) carries the affine action on the left and the line action on the right. Its realization functor is

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

The map \(\Delta_{\rm rat}\) expands a rational current at the incoming points and splits its exterior principal parts. For a fixed outgoing word \(p\), its expansion \(\Delta_{\rm rat}(p)\) multiplies the free coefficient \(b_0\) on the left. The evaluation leaves all the bar letters and the terminal state unchanged, even when the number of letters grows with the Laurent exponent. For a fixed \(p\) there is consequently one lower bound on the change of Laurent order for every incoming word. An element of the outgoing algebraic bar uses finitely many \(p\)'s, so one may take the least of their bounds. This is the uniform estimate that failed for \(e_j\mapsto q^{-j}e_j\). Write \(\eta_{M,N}\) for the resulting rational evaluation and \(b_{M,N}\) for its restriction along the affine resolution. Whether evaluation gives an equivalence can now be tested on the same maps.

## A comparison for any finite number of radial inputs {#ch08-a-comparison-for-any-finite-number-of-radial-inputs}

For three lines we would like to compare an expansion about all three punctures with the two-line evaluation. First move the punctures out together, keeping their ratios fixed. This gives a single Laurent variable and leaves all relative positions visible in its coefficients. For \(d\geq2\) ordered points normalize two of the shape coordinates by

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

In this formula \(r_{ij}(x)\) means the two-line kernel in slots \(i,j\) with inverse separation \(x^{-1}\). For the pair at \(a_i,a_j\), the coefficient of order \(q\) is the mode-zero interaction divided by \(t_i-t_j\). For three lines even the pair \(1,3\) contributes at this first order. The outgoing action on either type of generator \(y_n=B_n^a,c_{a,n}\) is

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

where \(\circ\) likewise means the direct-sum dual of finite total-pole-index pieces. A cochain takes exterior arguments from both summands of the rational currents. The polynomial arguments remain as inputs to the Hom below. The restricted dual records the proper pole arguments. For a smooth affine test complex \(X\), define

\[
\mathcal I_d^r(X;T)=
\prod_{a,b\geq0}\prod_{e\in\mathbb Z}
\operatorname{Hom}_K\!\left(
 \Lambda^a\mathfrak p_K\otimes_K X^e,
 \mathscr R_{d,b}(T^{r+e-a-b})\right).
\]

The indices \(a,b\) count polynomial and proper exterior arguments, and \(e\) is the degree of the test vector. The Hom in the polynomial and test variables is algebraic. Its differential is the total Chevalley–Eilenberg and mapping-complex differential for the rational-current action. Each coefficient has finite cofree and proper-mode support. Fix \(a,b\) and finitely many polynomial and test inputs. Choose a lower Laurent bound for each entry of their finite coordinate matrix. The minimum of these finitely many integers works for that stage. Enlarging the test or changing the arity may require a smaller bound. All displayed products are retained. This definition comes from current operations and their support conditions, independently of smooth realization.

Let \(D_{\mathcal N}(A_K)\) be the full subcategory of the original smooth derived category whose cohomology has jointly locally nilpotent positive currents: each cohomology vector is killed by all sufficiently long products of positive currents. Its maps are the ambient derived maps.

**Theorem — finite radial current comparison.** Assume the specified coherent smooth affine–right-\(Y\) realization, its tensor–Hom adjunction and full unit for ordinary unbounded \(Y\)-modules, its algebraic cofree model and common mode-cutoff actions. Assume also that every bounded-below smooth complex with jointly locally nilpotent positive-current cohomology belongs to the localizing category generated by \(W_K\), and that the derived ideal triangle expresses each \(Y_F\)-module by two complexes inflated from \(U_F\). Here inflation uses the augmentation \(Y_F\to U_F\), and the localizing category is closed under shifts, cones and arbitrary coproducts. Then, for every finite \(d\geq2\), every ordinary unbounded tuple \(M_1,\ldots,M_d\), and every \(X\in D_{\mathcal N}(A_K)\), the actual evaluation gives an equivalence

\[
\Xi_T(X):
R\operatorname{Hom}_{\operatorname{Sm}(A_K)}
 \bigl(X,\mathcal W_K\otimes^{\mathbb L}_{Y_K}S_{\mathbf a}(T)\bigr)
\xrightarrow{\sim}\mathcal I_d(X;T).
\]

The comparison retains the outgoing line action, all its specified higher compatibilities, and every additional commuting incoming right action. At the regular tuple it retains all \(d\) incoming regular right actions. Its coefficient evaluations are the rational maps \(\eta_{M_1,\ldots,M_d}\) and their original affine restrictions \(b_{M_1,\ldots,M_d}\). The theorem uses the bar and scalar-extension orders stated above. [The radial finite-puncture current recipient, equation (45)](#ref-ch08-03).

Take \(X=W_K\) first. The tensor–Hom unit identifies the spectral module with the right adjoint applied to its realization. Composing this unit with \(\Xi_T(W_K)\) gives the rational current evaluation on the spectral module. We can therefore test \(\Xi_T(W_K)\) by computing that evaluation. The ideal triangle reduces the calculation in each incoming slot to modules pulled back along \(Y_F\to U_F\), on which the ghost operators vanish. [The unit and counit](06-duality-and-induction.md#adjunction-comparison-maps).

For these inflated inputs the proper-current complex contracts at order zero by the energywise dual of the free Chevalley contraction. Cross-point terms have positive Laurent order and increase mode support by at most that order. Perturbation therefore preserves the required support. Composed with this contraction, the actual comparison is \(1+A\), with \(A\) of positive order, and has a coefficientwise geometric inverse.

For bounded-below inputs, representability and the positive-current torsion theorem extend this calculation to every ambient test in \(D_{\mathcal N}\). Explicit truncation towers then handle unbounded inflated inputs; their componentwise stabilization does not require a bound uniform over the product factors of \(\mathcal I_d\). Finally, the two inflated terms of the ideal triangle extend the equivalence to one arbitrary input at a time. There are finitely many such steps. No infinite incoming bar is moved through a continuous Hom, and no equality \(D_{\mathcal N}=\operatorname{Loc}(W_K)\) is required.

## Finite integral heads and separated values {#ch08-finite-integral-heads-and-separated-values}

The radial field admits \((a_i-a_j)^{-1}\), so evaluating at \(a_i=a_j\) there would require an inverse of zero. To take the collision first, fix \(a_d=0\) and work over the configuration ring \(R_d=\mathbb C[a_1,\ldots,a_{d-1}]\). Separation amounts to the localization \(R_d\to R_d[\Delta^{-1}]\), where \(\Delta=\prod_{i<j}(a_i-a_j)\). Let \(Y_w\) be the energy-\(w\) part of \(Y\). Its relative dual is \(\mathscr C_w=\operatorname{Hom}_{\mathrm{Mod}\text{-}U}(Y_w,U)\), the space of right \(U\)-linear maps to the regular module, with cohomological degrees reversed. In energy zero, \(Y_0=U\). A right \(U\)-linear map on \(U\) sends \(u\) to its value at \(1\) times \(u\), so \(\mathscr C_0=U\). The ground functional corresponding to \(1\) is the identity on \(U\). A current with a pole can lower the energy of a state. To compensate its denominator, weight a tensor of total energy \(w\) by \(\Delta^w\), counting the energy across all \(d\) factors. The resulting starting module is
\[
M_w=(\mathscr C^{\otimes d})_w
=\bigoplus_{w_1+\cdots+w_d=w}\mathscr C_{w_1}\otimes\cdots\otimes\mathscr C_{w_d},
\qquad E_{R_d}=\bigoplus_{w\ge0}\Delta^w(M_w\otimes R_d).
\]
Take all finite linear combinations obtained from this seed by finite words of currents and fixed-\(u\) derivatives. A fixed-\(u\) derivative moves a marked position while holding the rational current coordinate \(u\) fixed. A cross term with denominator \((a_j-a_i)^r\) lowers the total top energy by \(r\), so its coefficient on the weighted tops contains the integral factor \((\Delta/(a_j-a_i))^r\). For two marks the first positive seed contains both \(\Delta(\lambda\otimes1)\) and \(\Delta(1\otimes\lambda)\), where \(\lambda\in\mathscr C_1\) and \(1\in\mathscr C_0=U\) is the ground functional.

**Definition (finite head).** The coefficient head \(F_N\) retains top energy, total proper-pole budget and derivative order with sum at most \(N\). In the chosen monic basis of proper currents, the vector of order \(n\) at infinity contributes \(\lceil n/d\rceil\), its largest pole order at the separated marks. For two marks \(a,b\), put \(P=(u-a)(u-b)\). The basis vectors of orders \(2j+1\) and \(2j+2\) are \(1/[(u-b)P^j]\) and \(1/P^{j+1}\) for \(j\geq0\). Both have largest local pole order \(j+1\). Thus the order-three basis vector \(1/[(u-a)(u-b)^2]\) costs two. The current \(1/(u-b)^3\) has the same order at infinity and costs three at \(b\). In the current resolution the exterior entries also contribute their pole orders to the bound. This bounds the calculation over \(U^{\otimes d}\otimes R_d\), so the horizontal \(U\)-coefficients are retained. Each such head is a bounded perfect relative complex, so its derived dual commutes with derived scalar base change. On the separated chart \(a_i=q^{-1}t_i\), a homogeneous head generator \(g_h\) of scaling degree \(h\) is normalized at cutoff \(N\) to \(q^{N+h}g_h\). Raising the cutoff by one changes this factor by \(q\). In the dual tower the internal differential then has coefficients independent of \(q\), and restriction from \(N+1\) to \(N\) has a common factor \(q^{-1}\). Removing this factor gives the restriction matrix in the completed complex

\[
\widehat D^n=
\left(\bigoplus_N(D_N^0)^n\right)((q))
\oplus\left(\bigoplus_N(D_N^0)^{n-1}\right)((q)),
\]

\[
d(f,g)=\bigl(d_Df,(R_Nf_{N+1}-qf_N)_N-d_Dg\bigr).
\]

Here \(D_N^0\) is the dual of the normalized head. With \(R_N\) the restriction matrix after rescaling, compatibility reads \(q^{-1}R_N f_{N+1}=f_N\). Multiplication by \(q\) gives the difference \(R_N f_{N+1}-qf_N\) in the second component. Read the two direct sums before taking Laurent series. Each coefficient uses finitely many heads, and all heads share one lower Laurent bound. Taking the full algebraic dual of the union would remove the finite-support requirement.

Evaluation is the original tensor–Hom map

\[
\eta(p\otimes f)(l)=(-1)^{|p||f|}f(p\otimes l).
\]

For a fixed resolution word \(p\), insertion shifts the head bound from \(N\) to \(N+c(p)\). The ratio of the two normalizing powers of \(q\) sees this increment. It gives a bound on Laurent loss independent of the starting head. Evaluation and its homotopies therefore extend to the completed head complexes. For the full incoming bar, the stronger estimate is uniform in incoming length, including arbitrarily long words of energy zero. These estimates identify the separated head construction with the same evaluation used above. One can also insert the trivial line in either of the two prescribed orders and then evaluate at the regular output test. Each comparison is a roof of maps between completed complexes, with a quasi-isomorphism on the leg that is to be inverted. Both preserve the action on the surviving regular input. See *Integral kernels and the separated comparison diagrams*, §§1–3.

This separation of domains has a geometric consequence. A collision fibre sets a factor of \(\Delta\) to zero, whereas the separated Laurent chart has inverted \(\Delta\). Derived collision maps are obtained from the integral finite heads before that inversion. They cannot be obtained by substituting a collision into every vector of the separated Laurent complex.

## Common radial sewing and a failed substitution {#ch08-common-radial-sewing-and-a-failed-substitution}

On the radial field \(F((q))\) the iterated spectral differential is \(d_T+\rho_T(\sum_{i<j}r_{ij}(a_i-a_j))\) for every binary parenthesization. To see how the rational maps agree on the bar resolution, translate the generators \(y_n=B_n^a,c_{a,n}\) of \(Y\) by

\[
\tau_x(y_n)=\sum_{m=0}^n\binom nm x^{n-m}y_m,
\]

and extend \(\tau_x\) multiplicatively. With \(r(y)\) written as a function of separation, its identities at fixed output modes are rational identities,

\[
(\tau_x\otimes1)r(y)=r(y+x),\qquad
(1\otimes\tau_x)r(y)=r(y-x).
\]

For example, the coefficient with both modes zero in the first translated kernel sums to \(\sum_{m\ge0}(-x)^m y^{-m-1}=(y+x)^{-1}\). This identity continues the coefficient away from its expansion at \(x/y=0\). Continue each fixed-mode coefficient in this way before making the single radial expansion. Each pair of leaves first meets at one vertex, so the tree contributes each term of \(R_{\mathbf a}\) exactly once. Associative principal-part splitting gives the same rational and affine evaluations on the common completed incoming bar.

**Counterexample (substitution on the radial field).** A separately completed nested tensor need not have that domain. In a three-point shape chart,

\[
f=\sum_{n\geq0}q^n\lambda^{-n^2}\in\mathbb C(\lambda)((q)).
\]

The substitution \(\lambda=zq\) would give

\[
\sum_{n\geq0}z^{-n^2}q^{n-n^2}.
\]

Its outer \(q\)-orders have no lower bound, so it is not in \(\mathbb C((z^{-1}))((q))\). The terms tend to zero before substitution and fail to do so afterwards. This is an obstruction to extending that substitution continuously to the entire radial field. It leaves the common radial sewing theorem intact and identifies the extra support estimate needed for a larger nested domain.

### Three rational poles and a finite-total spectator {#ch08-three-pole-comparison}

Completing the first pair before adding the third line raises a question about the currents as well as their series. At the intermediate step, which punctures can a rational current still see? Fix the nonrational \(\mathfrak{sl}_2\) setting of this chapter and write
\[
a_1=z+w,\quad a_2=z,\quad a_3=0,
\qquad p=w^{-1},\quad q=z^{-1},
\qquad K_w=\mathbb C((p)),\quad K_N=K_w((q)).
\]
In the cluster coordinate \(v=u-z\), the proper current \(x/(v-w)\) still has a pole at the first line. An affine resolution at \(v=0\) omits that pole. The inner rational current algebra has poles at \(u-z=w,0,\infty\). Let \(P_c^{(12)}\) be its induced Chevalley resolution, \(P_c^{(3)}\) the full three-pole resolution, and \(P\) the original affine resolution for the third slot. The outer tensorator has the precise target
\[
\Delta^{(12|3)}:P_c^{(3)}
\longrightarrow
\bigl(P_c^{(12)}\otimes_{\mathbb C}P\bigr)((q)).
\]
It is a chain map for the right-twisted differential, with the actual incoming rational action and outgoing line action, normalized by \(1\mapsto1\otimes1\), and satisfies
\[
(\Delta^{(12)}\otimes1)\Delta^{(12|3)}=\Delta^{(3)}
\]
on the entire three-pole resolution. The rational intermediate resolution retains the extra pole missed by the affine cluster resolution. [Full-source tensorator](#atlas-c-horizontal-full-three-pole-tensorator).

Restrict the full-source derived evaluation along the affine inclusion into the binary rational resolution. That inclusion is a quasi-isomorphism in the original two-pole current category, and the restricted map is the original binary evaluation. This explains how the old target enters the bar comparison. A strict three-pole action on the literal old complex would require additional data. There is a further map from the rational-cluster target to the triple target. To see what can obstruct an equivalence there, follow the state of the third line through the inner completion.

::: {.conditional #ch08-finite-total-spectator title="The full three-pole comparison for a finite-total spectator"}

For a constant input \(T=T_{12}\otimes_{\mathbb C}M_3\), distinguish the joint intermediate object from the factorized one.
\[
\begin{aligned}
E_1&=S_w(T_{12})\otimes_{\mathbb C}M_3,\\
E&=S_w^{12}(T),\\
c&:E_1\hookrightarrow E.
\end{aligned}
\]
Both spaces carry the interaction of lines 1 and 2. In \(E\) the \(p\)-completion includes the third state. In \(E_1\) the third module is tensored on after that completion. The map \(c\) includes the resulting coefficient arrays. The pair \(T_{12}\) may be correlated and unbounded. If \(H^\bullet(M_3)\) has finite **total** dimension, \(c\) is a quasi-isomorphism. Assume in addition the coherent smooth realization and the full tensor–Hom unit used in the finite radial comparison. Then the three-pole evaluation reaches the endpoint obtained by completing the pair independently. It preserves the affine restriction and the unit of that adjunction on the outgoing module. The comparison diagram commutes strictly on the displayed algebraic bars and with the specified coherent homotopies after smooth replacement. A fixed left comb admits stagewise comparisons when each newly attached spectator has finite-total cohomology. Finite dimension in each degree does not suffice. [Finite-total native comparison](#atlas-c-horizontal-full-three-pole-native-finite-total).

:::

Return to the independent third states from the opening, this time with their differential. Over a field split the underlying complex of \(M_3\) into representatives of cohomology and a contractible summand. The pair interaction acts only in slots 1 and 2, so the spectator homotopy contracts the second summand coefficient by coefficient on either side of \(c\). A single homogeneous basis for the finite total cohomology then spans the surviving spectator coefficients in *all* degrees and orders. This proves sufficiency and uses only a splitting of complexes of vector spaces.

For trivial first inputs and third input given by the regular \(U=U(\mathfrak{sl}_2)\)-module, inflated along \(Y\to U\),
\[
E/E_1=U((p))/(U\otimes_{\mathbb C}K_w)\ne0
\]
with zero differential. For example \(\sum_{n\geq0}p^n H^n\), where \(H\) is the Cartan generator of \(U\), has one algebraic coefficient at every inner order. Its coefficients span an infinite-dimensional space, so it survives in the quotient. More generally, for fixed \(M_3\), the map \(c\) is a quasi-isomorphism for every constant first pair exactly when \(H^\bullet(M_3)\) has finite total dimension. For necessity, take \(T_{12}=\bigoplus_{j\in\mathbb Z}\mathbb C e_j\) with \(|e_j|=j\), zero differential and trivial line actions. Given independent homogeneous spectator classes \(v_n\), the joint object has the degree-zero class \(\sum_{n\ge0}p^n e_{-|v_n|}\otimes v_n\). Every class from the factorized object has its spectator coefficients in one finite-dimensional subspace. The displayed class therefore lies outside the image. A comparison of evaluations can still use maps *from* a common domain, as the following construction shows.

### A common domain for the factorized intermediate object {#ch08-factorized-common-domain}

For the regular spectator the comparison \(E_1\to E\) misses the series with coefficients \(H^n\). To compare the evaluations we can still ask which arrays both orders of fusion accept. Express the inner and outer separations in the same two variables. Put \(s=q/p=w/z\), so that the substitution \(q=sp\) identifies \(K_w((q))\) with \(K_w((s))\), and set
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

**Definition (factorized common domain).** Expand the rational shape coefficients at \(s=0\). A row of the resulting array has fixed \(p\)-exponent, and a column has fixed \(s\)-exponent. In this common space of arrays put
\[
L_D^{\mathrm{fac}}(T)=L_D(T)\cap N_1(T)=L_R(T)\cap N_1(T).
\]
Degree by degree, for each outer exponent \(j\), its \(s^j\)-coefficient belongs to \(T_{12}((p))\otimes M^{(j)}\) for some finite-dimensional graded subspace \(M^{(j)}\subset M_3\). The subspace may grow with \(j\), but it works for the entire inner \(p\)-series at that outer coefficient. This condition makes the intersection a dg \(Y_D\)-module and gives actual maps
\[
L_R(T)\longleftarrow L_D^{\mathrm{fac}}(T)\longrightarrow N_1(T).
\]
For example, the inverse separation of lines 1 and 3 is \(ps/(1+s)\), and that of lines 2 and 3 is \(ps\). A cross term of kernel order \(h\) first reaches column \(h\). Only finitely many such terms act on any prescribed column of a series bounded below in \(s\). The \(12\) kernel can run through all inner orders there because it fixes \(M_3\). The construction preserves quasi-isomorphisms in each input. The outgoing action and factorwise incoming actions preserve it; a general commuting endomorphism of the joint input need not preserve finite spectator support. [The factorized common domain](#atlas-c-horizontal-factorized-common-domain).

If \(H^\bullet(M_3)\) has finite total dimension, the canonical inclusion \(L_D^{\mathrm{fac}}(T)\to L_D(T)\) is a quasi-isomorphism. A contraction of the underlying spectator complex to its finite cohomology suffices; no line-module structure on that auxiliary cohomology is required. The cross perturbation has positive order in both \(p\) and \(s\), so only finitely many spectator operators contribute at each fixed outer order. Both domains retract onto the same transferred complex. The maps from the two domains to their endpoints therefore have equivalent cones. Even at the trivial input, these cones retain the quotients \(K_R/D\) and \(K_N/D\), one for each endpoint. [Finite-total comparison and its cones](#atlas-c-horizontal-factorized-common-finite-total).

**Theorem (three-pole evaluation).** The entire three-pole rational current resolution has an evaluation on a resolved model for \(L_D^{\mathrm{fac}}(T)\). The theorem holds for arbitrary constant ordinary dg inputs, in particular the regular triple \(Y^{\otimes3}\). Let \(M=T_{12}\), \(N=M_3\), \(A=Y^{\otimes2}\) and \(B=Y\). Resolve the two inputs separately by the augmented bars
\[
R_M=\operatorname{Bar}_A(A,M),\qquad R_N=\operatorname{Bar}_B(B,N).
\]
Write \(F_3(V,W)\) for the underlying array intersection just defined, with \(V\) in the completed pair and \(W\) in the spectator position. With the pair-sum twist on its free heads, \(F_3(R_M,R_N)\) augments by a quasi-isomorphism to \(L_D^{\mathrm{fac}}(T)\). For the evaluation target, replace the free right heads in the two bars by \(P^{\otimes2}\) and \(P\), respectively. Call the resulting bars \(T_M,T_N\). Their ordinary bar differentials give \(F_3(T_M,T_N)\) its differential.

Let \(P_c^D\) be the three-pole rational current resolution over \(D\). For \(\pi\in P_c^D\), expand \(\Delta^{(3)}(\pi)\) in the three affine heads. The direct expansion gives algebraic rational rows with common lower bounds. The factorization \(\Delta^{(3)}=(\Delta^{(12)}\otimes1)\Delta^{(12|3)}\) gives a second estimate. Each outer coefficient uses finitely many third heads, and applying the inner tensorator leaves them fixed. The two estimates put the same kernel in \(F_3(P^{\otimes2},P)\). The evaluation is the balanced chain map
\[
\begin{aligned}
\eta:P_c^D\otimes_{Y_D}F_3(R_M,R_N)&\longrightarrow F_3(T_M,T_N),\\
\pi\otimes(x\otimes y)&\longmapsto\Delta^{(3)}(\pi)\cdot(x\otimes y).
\end{aligned}
\]
The dot multiplies the heads and retains all letters and both terminal vectors, with the tensor signs. At each outer order a finite convolution of finite spectator spans suffices. The bound depends on the resolved word and the output order and permits arbitrarily long horizontal words in the incoming bars. In the chain identity the right twist of \(\Delta^{(3)}\) cancels the twist of the free heads. This explains the ordinary differential in the target.

There are two comparisons of this map. On the radial side, shuffle the two algebraic bars. The signed interleavings cancel the faces that multiply letters from different bars, and leave head multiplication intact. On the pair-first side, form the actual outer binary bar after \(S_w(R_M)\otimes R_N\) and use its augmentation and the separate augmentations of \(R_M,R_N\). On outer length zero apply the inner tensorator to the rational pair head. The two length-one faces cancel by its right-linearity. These maps give the radial and pair-first evaluations with their affine restrictions and specified endpoint units. They use no inverse of \(E_1\to E\). A further theorem would have to realize the common-domain adjunction unit as a universal class in an independently constructed smooth current complex on every admitted test.

Part of the recipient can also be built directly from currents. Divide the exterior proper modes between the first pair and the spectator, keeping the restricted dual of each exterior power. At each fixed outer exponent require the third-slot modes, their cofree coefficients and the spectator input to span a finite space through the inner series. The current differential preserves this requirement. An action internal to the pair leaves the third slot fixed, and a term crossing into it with kernel order \(h\) costs at least \(s^h\). Only finitely many such orders contribute to a fixed outer coefficient. This gives a subcomplex on constant smooth tests and the usual proper-current evaluation on every regular word, including arbitrary horizontal \(U\)-words. Identifying its full smooth action on general tests with the common-domain adjunction is the remaining representability question.

If only finitely many orders are observed, how accurately can the common domain approximate either endpoint? Give \(L_R(T)\) its radial \(p\)-adic topology and \(N_1(T)\) its outer \(s\)-adic topology. Each coefficient has discrete topology at its respective stage. Each fixed coefficient can be read continuously at both endpoints. In their product, equality of every \(p^is^j\) coefficient defines a closed subspace, the graph of \(L_D^{\mathrm{fac}}(T)\). It is complete, and its two projections have dense images. To approximate a radial input in its own topology, keep finitely many whole \(p\)-rows. Each row has algebraic rational coefficients in the shape variable and hence a finite spectator span. To approximate a pair-first input, keep finitely many whole \(s\)-columns. Each retained column already has finite spectator span through its inner \(p\)-series. For an array in the graph one can meet both cutoffs at once by adding the two truncations and subtracting their common rectangle. For \(v\ne0\), the sequence \(p^n v\) already distinguishes the two endpoints. It tends to zero radially and has constant outer order zero. Thus continuity on the common graph gives no continuous extension of the identity from the entire radial input to the native pair-first input.

### Tests over a coefficient ring {#ch08-common-ring-tests}

**Counterexample (an acyclic test over the common ring).** A functor on derived tests must take an acyclic test to zero. The ordinary Hom formula over \(D\) can fail even on an exact sequence of three modules. Let \(g=p+s\). Substitution \(p=-s\) maps \(D\) to \(\mathbb C((s))\) and kills \(g\), so \(g\) is a nonunit. The complex
\[
E=(D\xrightarrow{g}D\longrightarrow D/g),
\qquad E^0=D,\quad E^1=D,\quad E^2=D/g,
\]
is acyclic, but \(H^0\operatorname{Hom}_D(E,D)=D/g\ne0\). Indeed multiplication by \(g\) is injective in the domain \(D\), and \(\operatorname{Hom}_D(D/g,D)=0\). Dualizing leaves the cokernel of multiplication by \(g\) in degree zero. Let \(W_D\) be the scalar extension to \(D\) of the regular-top affine object in the tensor–Hom realization. For trivial incoming coefficient, the ordinary current formula on the acyclic smooth test \(W_D\otimes_D E\) retracts onto this nonacyclic Hom complex. Thus that formula cannot define the proposed functor on arbitrary derived \(D\)-tests. The field and constant ground-field test theorems retain their stated scope. [The ordinary-Hom counterexample](#atlas-c-horizontal-common-ring-hom-counterexample).

The obstruction came from applying ordinary Hom to an arbitrary acyclic test. Starting with \(W_D\) and attaching one cone at a time gives a class on which the comparison can be proved directly. It holds on explicit finite \(W_D\)-cell models: bounded complexes formed from \(W_D\) by finitely many shifts, finite sums and cones, with their actual enhanced maps. Finite cone induction extends the comparison at \(W_D\), and proves invariance under quasi-isomorphisms between these models. This includes the finite induced Chevalley model of the parameter-Verma family. A value on an arbitrary representative, or on every object generated by unrestricted coproducts, requires a derived test construction and its support theorem. [Finite cell tests](#atlas-c-horizontal-common-ring-finite-cell-tests).

### Two independently completed clusters {#ch08-incomparable-clusters}

Now fuse two pairs before bringing them together. A single spectator subspace no longer describes the restriction. At every order in the outer separation we need a *finite sum of tensors* of two independently completed pair states. To see what this requires already for scalars, place the lines at \((z+w_1,z,w_2,0)\), set \(p_i=w_i^{-1}\), \(q=z^{-1}\) and \(s_i=q/p_i\), and compare the four rings
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
Both images of \(N_{\mathrm{fac}}\) have identical coefficients there. To see why the order still matters for general inputs, take scalar coefficients and form \(\sum_{j\ge0}p_1^{-j}p_2^j\). It is a series in \(p_2\) whose individual coefficients belong to \(\mathbb C((p_1))\), so it belongs to \(F_{12}\). The powers of \(p_1\) have no common lower bound, so the same array lies outside \(F_{21}\) and outside the intersection. The same rational function \(p_1/(p_1-p_2)\) has the different expansion \(-\sum_{j\ge1}(p_1/p_2)^j\) in \(F_{21}\). [The four coefficient objects](#atlas-c-horizontal-two-cluster-coefficient-objects).

If both pair inputs have finite total cohomology, then for either \(F=F_{12}\) or \(F_{21}\), the canonical maps
\[
N_{\mathrm{fac}}\otimes_{\Lambda_{\mathrm{fac}}((q))}F((q))
\longrightarrow S_z^F(E_{\mathrm{fac}}\otimes_{\Lambda_{\mathrm{fac}}}F)
\longrightarrow N^F
\]
are quasi-isomorphisms. Under the same hypotheses on the smooth affine realization and its adjunction, they preserve the independent binary recipients, evaluations and tensor–Hom units on every test in \(D_{\mathcal N}(A_{F((q))})\), with mapping complexes taken in the ambient smooth category. The unextended scalar legs are different maps and need not be equivalences. [Finite-total pair comparison](#atlas-c-horizontal-two-cluster-finite-total) · [The two scalar extensions](#ref-ch08-05).

A radial coefficient may have poles in both shape variables \(s_1,s_2\). After substituting \(s_i=q/p_i\), either pole consumes powers of the same outer variable \(q\). The ring below bounds their sum. Let
\[
\mathcal O_2=\mathbb C[s_1,s_2]_{(s_1,s_2)},\qquad
\mathfrak q=s_1^{-1}\mathcal O_2+s_2^{-1}\mathcal O_2,
\]
\[
D_{\mathrm{con}}=\bigcup_{c\ge0}
\left\{\sum_{n\ge-c}q^n\theta_n:
\theta_n\in\mathfrak q^{n+c}\right\}.
\]
A monomial \(q^n s_1^{-i}s_2^{-j}\) with \(i,j\ge0\) and \(i+j\le n+c\) becomes \(q^{n-i-j}p_1^ip_2^j\). Thus the bound on the *sum* of pole orders keeps the new outer exponent at least \(-c\). Regular shape factors expand at \((s_1,s_2)=(0,0)\). The fractional-ideal condition gives the resulting locally finite coefficient array after \(s_i=q/p_i\). It embeds \(D_{\mathrm{con}}\) into \(\Lambda_{\mathrm{sym}}((q))\). Let \(L_{D_{\mathrm{con}}}(T)\) be the same series construction with coefficients \(\theta_n\in T\otimes\mathfrak q^{n+c}\), carrying the four-point spectral differential. The factorized intersection needs the smaller scalar ring
\[
D_*=D_{\mathrm{con}}\cap\Lambda_{\mathrm{fac}}((q)),\qquad
L_*^{\mathrm{fac}}(T)=L_{D_{\mathrm{con}}}(T)\cap N_{\mathrm{fac}}(T),
\]
where both intersections use the symmetric expansion. At each outer coefficient, membership in \(N_{\mathrm{fac}}\) means a finite algebraic sum of tensors of the two completed cluster factors. The intersection is a dg \(Y_{D_*}\)-module with maps to the radial and factorized endpoints. In general it is not a \(D_{\mathrm{con}}\)-module: the conic series \(\sum_{n\ge0}q^{2n}(s_1s_2)^{-n}\) becomes \(\sum_{n\ge0}p_1^np_2^n\) at outer order zero. Its coefficient matrix is the infinite identity from the [finite-rank example](#tensor-completion-and-rank). No finite sum of products of inner scalar series has that matrix. [The scalar ring of the factorized intersection](#atlas-c-horizontal-four-point-factorized-intersection).

**Theorem (four-pole evaluation).** Take constant ordinary pair inputs \(M,N\) over \(A=Y^{\otimes2}\), and write \(F_4(M,N)=L_*^{\mathrm{fac}}(M\otimes N)\). For each pair \(V=M,N\) take the bars \(R_V=\operatorname{Bar}_A(A,V)\) and \(T_V=\operatorname{Bar}_A(P^{\otimes2},V)\). Over \(D_*\), the four-pole resolution \(P_{c,*}^{(4)}\) has the evaluation
\[
P_{c,*}^{(4)}\otimes_{Y_{D_*}}F_4(R_M,R_N)\longrightarrow F_4(T_M,T_N),
\qquad \pi\otimes b\longmapsto\Delta^{(4)}(\pi)\cdot b .
\]
The source bars carry the four-point interaction and the target bars their ordinary bar differential. To see why the source resolves the stated intersection, contract an acyclic first input over \(\mathbb C\). Perturb its contraction first by the internal \(12\) kernel. A term of order \(e\) contributes \(q^e s_1^{-e}\) on the radial side and \(p_1^e\) in the first completed pair. It respects the conic bound and acts only in that pair. Next perturb by the four cross-pair kernels. All have positive outer order with finitely many factorwise operators in each coefficient. The resulting series converges on both sides and preserves finite tensor rank there. Interchanging the pairs proves invariance under a quasi-isomorphism in either input.

There are two estimates on one and the same resolution word. For \(\pi\) in the four-pole resolution extended from distinct positions to \(D_*\), the direct expansion of \(\Delta^{(4)}(\pi)\) satisfies the conic estimate. Its factorization
\[
\Delta^{(4)}=(\Delta^{(12)}\otimes\Delta^{(34)})\Delta^{(12|34)}
\]
has finitely many tensors of rational pair heads at each \(q\)-coefficient. Each inner tensorator acts only on its own head. Thus multiplying the independent free bar heads by this kernel lands in the same intersection with two affine heads in each target bar. The radial shuffle respects the multiplication. The comparison with the outer binary evaluation uses the two rational pair heads before applying their respective inner tensorators. Both sides carry the same right actions, affine restriction and unit normalization on the resolved words. The construction supplies a map on all the stated coefficients, including the regular inputs, without a finite-total cohomology hypothesis. [Four-pole rational tensorator](#atlas-c-horizontal-four-pole-rational-tensorator) · [Evaluations on the two factorized domains](#ref-ch08-06).

The finite-total result above identifies field-valued recipients after the specified scalar extensions. This four-pole evaluation is instead defined over the nonfield \(D_*\). A common-ring representation theorem on general smooth tests, a continuous associator for independently completed inputs in their original topologies, and compatibility of interchange with changes of tree on every parameter face remain open. Agreeing on all finite trees whose coefficients are expanded once in a common radial variable proves the common radial sewing theorem at its own domain.

### Occupied deletion and parameter variation {#ch08-deletion-and-spectral-connection}

Deletion starts with a point still occupied by the trivial line. Give that input its prescribed vacuum covector, which takes the cofree energy-zero unit to \(1\). Such an input can be deleted in any of the three slots. Restrict proper-current functionals to wedges with no factor in that slot, then apply its normalized cofree energy-zero covector. The resulting current map is a quasi-isomorphism on \(D_{\mathcal N}(A_{K_R})\) and \(D_{\mathcal N}(A_{K_N})\), and on constant tests from \(D_{\mathcal N}(A)\) over \(D\). Each uses the original smooth mapping complexes. It preserves the original evaluation at the surviving positions. Deleting slot three leaves the nonanchored pair \((z+w,z)\), with outgoing action \(\Delta_w\circ\tau_z\). The normalized trivial input and the regular line input give different tests. [Occupied deletion](#atlas-c-horizontal-occupied-deletion-all-slots).

The coordinates at infinity can be moved as well. Over \(L=\mathbb C((p))((s))\), set \(v=u-z\). A polynomial current \(f(v)\) at the anchored positions \((w,0)\) acts on the moving test as \(f(u-z)\). A proper current uses its Taylor expansion at infinity in the translated variable. Every positive-mode tail in that substitution truncates on each smooth test vector, and the inverse change uses \(-z\). This identifies the two survivor current complexes on the correspondingly transported tests and preserves the affine and rational evaluations. If \(F=\mathbb C((p))\) and \(E=S_w(T)\) is the binary spectral complex over \(F\), there is still a scalar comparison \(L\otimes_F E\to E((s))\) with the same outgoing translation on both sides. Its cone in degree \(i\) has cohomology
\[
H^i(E)((s))\big/\bigl(L\otimes_F H^i(E)\bigr).
\]
Indeed the map is injective and Laurent series preserve a splitting of an \(F\)-complex into its cohomology and contractible parts. In degree \(i\) the denominator consists of the series whose coefficients lie in one finite-dimensional \(F\)-subspace of \(H^i(E)\). If \(H^i(E)\) is infinite-dimensional, a series of independent classes in that degree survives in the quotient. Thus the quotient vanishes in every degree exactly when each \(H^i(E)\) is finite-dimensional over \(F\). This degreewise criterion concerns the scalar comparison after the coordinate change.

Does deletion commute with moving one of the surviving points towards the deleted point? The linear coefficient in their displacement already distinguishes the two orders of expansion. Put the three positions at \(z+t,z,0\), with \(z\) invertible, and delete the middle occupied point on the source regular there. The survivors have separation \(z+t\). Over the finite jet ring \(\mathbb C((q))[t]/(t^{\ell+1})\), the substitution \(q\mapsto q/(1+tq)\) carries their original binary rational and affine evaluations and their adjunction unit to the moved positions on scalar-pulled tests. In particular, for \(x\in\mathfrak{sl}_2\), the coefficient of \(u^h\) in the expansion of \(x/(u-z-t)\) at the third point has first jet
\[
-(z+t)^{-h-1}x=-q^{h+1}x+(h+1)tq^{h+2}x\pmod {t^2}.
\]
Suppose instead that the same unprojected current is first expanded at the occupied point, with local coordinate \(y=u-z\). It gives
\[
\frac{x}{y-t}=-\sum_{h\ge0}t^{-h-1}xy^h .
\]
Its zero mode has coefficient \(-t^{-1}\) and sends the regular horizontal vector \(1\in U\) to \(-t^{-1}x\). This coefficient cannot belong to the integral lattice \(\mathbb C((q))[[t]]\). The normalized vacuum covector kills the whole mode tail on its admissible source, which is why the projected binary jet exists. Recovering an integral three-input occupied insertion, its opposite deletion diagram and their coherent comparison still requires a construction on the unprojected inputs.

What can an unprojected calculation at this collision still measure? The integral ternary resolution retains all three positions. Its polynomial currents already make sense on the diagonal, so take its jet before comparing binary diagrams. For \(A=\mathbb C((q))[t]_{(t)}\), each bounded head of its coefficient module and of its Chevalley kernel is perfect over \(U^{\otimes3}\otimes A\). Dualizing such a head commutes with passage to \(J_\ell=A/(t^{\ell+1})\), with its actual head restrictions and transposed evaluations. The statement extends to the algebraic derived inverse limit of the dual heads. Indeed derived tensor with \(J_\ell\) is a finite cone of multiplication by \(t^{\ell+1}\), and homotopy limits commute with this cone. The original regular horizontal coefficients matter already on the smallest head. The polynomial current \(xu\) evaluates there on \(c\in U^{\otimes3}\) as \(c\bigl((z+t)x^{(1)}+zx^{(2)}\bigr)\). Taking \(c=1\) detects \(x^{(1)}\) in the first normal coefficient. This computes a jet of a single ternary diagram. Comparing the two integral diagrams obtained by independently composing binary operations remains open.

For constant inputs at any finite number of positions \(a_i\), write \(R_{\mathbf a}=\sum_{i<j}r_{ij}(a_i-a_j)\). Let \(L\) be the odd line-algebra derivation determined by \(Lc_{a,n}=k^{-1}\kappa^{ab}B^b_n\), \(LB^a_n=0\), and \([Q,L]=T_Y\), where \(Q\) is the line differential and \(T_Y\) generates translation of the line modes. Acting in slot \(i\), it defines
\[
X_i=L^{(i)}R_{\mathbf a},\qquad
\nabla_i=\partial_{a_i}+\rho_T(X_i).
\]
For these constant inputs the connection is flat and commutes with the spectral differential. The outgoing action is horizontal up to the homotopies \(\lambda_i=L^{(i)}\Delta_{\mathbf a}\). Varying the input modules with the positions would also require a connection on those modules. To compare the current complexes over polynomial differential forms one still needs a normalized gauge transformation on the full complex, its inverse, homotopies for the actions, and compatibility with parameter changes and changes of tree. [The flat spectral connection](#atlas-c-horizontal-flat-spectral-connection).

In the formal calculation a pole at \(u=z\) survives or disappears according to which state occupies the puncture. A boundary field on \(\mathbb R_t\times\mathbb C_z\) admits another test. Two insertions may agree in \(z\) while remaining strictly ordered in \(t\). A test function supported at positive real separation can detect the complex residue there. Moving the test to the endpoint \(t=0\) asks for the additional current carried by the ordering wall. [Ordered poles and their complete differential](09-mixed-boundaries.md#ch09-ordered-poles-and-their-complete-differential).

## References {#ch08-references}

- [*Line operators and the boundary derived functor*](#ref-ch08-01), affine resolution and line-generator comparison.
- [*Rational evaluation on the completed incoming bar*](#ref-ch08-02), Proposition 1 and the rational evaluation construction.
- [*The radial finite-puncture current recipient*](#ref-ch08-03), equations (20)–(23), (30)–(45), and the common radial sewing construction.
- [*Integral kernels and the separated comparison diagrams*](#ref-ch08-04), finite-head evaluation, incoming bars, occupied insertions and derived collision maps.

## Source manuscripts {#ch08-source-manuscripts}

### 1. Line operators and the boundary derived functor {#ref-ch08-01}

In “Lifts of the line generators” the contraction by a positive mode gives the odd generator on the induced Chevalley resolution. The corrected right multiplication gives the even generator. Both enter the first-order pair interaction. [The line algebra and its spectral tensor](#ch08-the-line-algebra-and-its-spectral-tensor).

### 2. Rational evaluation on the completed incoming bar {#ref-ch08-02}

Proposition 1 identifies the augmented bar after Laurent completion. The rational evaluation multiplies its first coefficient and has a loss of Laurent order bounded for each outgoing word. [The incoming and outgoing bars](#ch08-the-incoming-bar-its-completion-and-the-outgoing-bar).

### 3. The radial finite-puncture current recipient {#ref-ch08-03}

Equations (20)–(23) construct the independent current cochains. Equation (45) gives the comparison on smooth tests with jointly locally nilpotent positive-current cohomology. Equations (46)–(47) give the translation identities at fixed modes. [Finite radial comparison](#ch08-a-comparison-for-any-finite-number-of-radial-inputs) · [Common radial sewing](#ch08-common-radial-sewing-and-a-failed-substitution).

### 4. Integral kernels and the separated comparison diagrams {#ref-ch08-04}

Equations (I3)–(I10) bound the energy, pole orders and derivatives together. They give the restriction between successive duals and the loss of Laurent order under evaluation. For the binary total-energy seed and the two choices of occupied slot, see *Integral occupied insertions with one regular coefficient*, equation (50) and Theorem 7. Projecting the ground functional in the occupied slot sends the weighted regular top of energy \(w\) to \(\Delta^w\lambda\). With the regular position held fixed, \(w\) derivatives in the occupied coordinate give \((\partial_{\rm occ}\Delta)^w w!\lambda\). On the relative chart \((z,0)\) the moving slot can instead be regular. To lower \(\Delta^j\lambda\) by one power there, subtract the finite weight-\(w\) Sugawara action \(\mathcal S_{z,w}\) from \(\nabla_z\) and divide by \(j\,\partial_z\Delta\), as in equation (56). When the moving slot is occupied, \(\mathcal S_{z,w}=0\). [Finite integral heads and separated values](#ch08-finite-integral-heads-and-separated-values).

### 5. Support-controlled comparisons of nested current modules {#ref-ch08-05}

Theorem 1 contracts the spectator complex on the common factorized domain when its total cohomology is finite-dimensional. Theorem 2 compares the two ordered coefficient fields after the specified scalar extensions. [A common domain for a pair and spectator](#ch08-factorized-common-domain) · [Two independently completed clusters](#ch08-incomparable-clusters).

### 6. Horizontal fusion through independently completed pairs {#ref-ch08-06}

Sections 4–5 construct the rational evaluations on the separately resolved three- and four-pole intersections. Sections 6–7 compute the first jet after occupied deletion and the pole seen by the regular horizontal vector before projection. [Three-pole evaluation](#ch08-theorem-three-pole-evaluation) · [Four-pole evaluation](#ch08-theorem-four-pole-evaluation) · [Occupied deletion](#ch08-deletion-and-spectral-connection).
