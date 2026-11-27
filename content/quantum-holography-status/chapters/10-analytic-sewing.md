# Analytic sewing and conformal blocks

On the sphere with punctures \(0,z,1,\infty\), draw a circle enclosing \(0,z\). On each side the amplitude is a three-point functional. To glue the two sides one must convert a functional on the intermediate states into a state that the other functional can accept. Even in a one-dimensional space there is a normalization to remember. If a basis state \(e\) has bilinear pairing \((e,e)=g\ne0\) and the functionals take values \(u,v\) on \(e\), the contraction is \(uv/g\). Rescaling \(e\) by \(\lambda\ne0\) multiplies both values by \(\lambda\) and the pairing by \(\lambda^2\), leaving the contraction unchanged.

The positive principal Virasoro representations at real central charge \(c>1\) are labelled by their momentum. Each representation has its own grading by level. At a fixed momentum \(k>0\), sum over the discrete levels of the representation, using at each level the inverse matrix of its invariant bilinear form. The answer still depends on \(k\). A spectral norm or a pairing with a momentum packet integrates this function. Drawing the circle around \(z,1\) instead gives a second function, expanded near \(z=1\) rather than near \(z=0\). Relating the two functions requires the normalized four-point hypothesis below. Even for the first circle alone, a further insertion asks how much energy decay is left in its output. The first nontrivial Virasoro level lets us calculate the contraction before we estimate its tail.

## Virasoro representations and domains of fields {#ch10-virasoro-representations-and-domains-of-fields}

Fix a real central charge \(c>1\). The Virasoro relations are

\[
[L_m,L_n]=(m-n)L_{m+n}
 +\frac{c}{12}(m^3-m)\delta_{m+n,0}\,\mathrm{id}.
\]

For a positive principal label \(p\), let \(H_p\) be the Hilbert completion of the irreducible highest-weight module with highest vector \(\Omega_p\) and weight

\[
h_p=\frac{c-1}{24}+p^2,
\qquad L_0\Omega_p=h_p\Omega_p,
\qquad L_n\Omega_p=0\quad(n>0).
\]

Its level-\(N\) subspace has energy \(h_p+N\). A descendant is a vector obtained by applying negative modes to \(\Omega_p\). Positive Hilbert forms control convergence; the contractions used in sewing are the complex-bilinear invariant forms, with their inverse Gram matrices. For example, normalize the invariant bilinear form by \((\Omega_p,\Omega_p)=1\). At level one there is just the state \(L_{-1}\Omega_p\). Its Gram matrix has the single entry
\[
 (L_{-1}\Omega_p,L_{-1}\Omega_p)
 =(\Omega_p,L_1L_{-1}\Omega_p)=2h_p,
\]
since \([L_1,L_{-1}]=2L_0\) and \(L_1\Omega_p=0\). The scalar \(g\) of the opening calculation is therefore \(2h_p\). For values \(u_1,v_1\) on this state the level contributes \(u_1v_1/(2h_p)\) in the fixed local coordinates. The denominator is nonzero for every positive principal label. At a higher level choose a basis \(e_i\) and write \(G_{ij}=(e_i,e_j)\). If the two amplitudes take values \(u_i,v_j\) on these basis vectors, their contribution is \(\sum_{i,j}u_i(G^{-1})_{ij}v_j\). This is still a finite sum. The analytic question first enters when all levels contribute. A Hilbert norm weighted by energy will tell us whether the tail is small enough for the next vertex.

**Definition (energy spaces).** Write \(E_p=L_0^{(p)}\), and let \(v_N\) denote the level-\(N\) component of \(v\). For real \(t\), let \(H_p[t]\) be the completion of the finite descendants in the norm

\[
\|v\|_{H_p[t]}^2
=\sum_{N\ge0}e^{2t(h_p+N)}\|v_N\|_{H_p}^2.
\]

The resulting space \(H_p[t]\) is the domain of \(e^{tE_p}\) for \(t>0\). Negative \(t\) gives a weaker completion. To see what an exponent measures, choose one unit descendant at every level and give it coefficient \(e^{-\alpha N}\), with \(\alpha>0\). The squared norm is a geometric series, finite exactly for \(t<\alpha\). A state that must supply every positive energy margin belongs to the entire-energy space

\[
\mathscr E_p=\bigcap_{n\ge1}H_p[n],
\]

with the topology defined by these norms. Every finite descendant belongs to it. The intersection permits arbitrary positive exponential energy weights, which is stronger than requiring smoothness under finitely many powers of \(L_0\).

Two external fields may be prepared in a correlated state. A sum over the levels of one leg can then involve ever higher levels on the other. For finitely many labels take the completed projective tensor product

\[
E_{\mathbf p}
=\mathscr E_{p_1}\widehat\otimes_\pi\cdots
 \widehat\otimes_\pi\mathscr E_{p_d}.
\]

In the joint level decomposition this space consists exactly of the coefficient arrays \(u_{N_1,\ldots,N_d}\) for which

\[
\sum_{\mathbf N}e^{2a\sum_i(h_{p_i}+N_i)}
                 \|u_{\mathbf N}\|^2<\infty
\quad\text{for every }a\ge1.
\]

Here \(u_{\mathbf N}\) is the component in the Hilbert tensor product of the indicated finite level spaces. Finite sums of tensors of descendants are dense. Their limits include correlated arrays with arbitrarily many occupied levels in different legs. Write \(Q_a\) for the square root of the displayed sum and \(\pi_a\) for the projective seminorm at weight \(a\). On a finite array the triangle inequality gives \(Q_a\leq\pi_a\). Conversely, expand the array in tensor products of orthonormal level vectors and sum the weighted absolute values of its coefficients. Cauchy–Schwarz bounds this sum by \(C_\delta Q_{a+\delta}\) for each \(\delta>0\), because the remaining squared weights \(e^{-2\delta\sum_i(h_{p_i}+N_i)}\) are summable even with the level multiplicities, which grow subexponentially. Thus finite arrays have the same completion in the two families of norms. This is the completion on which the subsequent operations act. [*Radial comb sewings of arbitrary finite length*, §“The entire finite-word source”](#ref-ch10-01).

**Definition (Virasoro conformal block).** A change of coordinate generated by one rational vector field moves all the punctures together. A conformal block on the marked sphere assigns a multilinear functional \(\mathcal B\) to states in the specified puncture representations, subject to the infinitesimal invariance below. The Ward condition says that the sum of the actions of the *same* rational vector field, expanded at all punctures, vanishes in the functional. In formulas,
\[
\sum_i\mathcal B(v_1,\ldots,L_i(f)v_i,\ldots,v_d)=0
\]
for a rational vector field \(f(z)\partial_z\) with poles only at the punctures. The sum includes the outgoing puncture with its contragredient action. In a local coordinate \(w=z-a_i\) at a finite puncture the mode expansion is

\[
f(a_i+w)=\sum_{n=-M_i}^{\infty}f_{i,n}w^{n+1},
\qquad L_i(f)=\sum_{n=-M_i}^{\infty}f_{i,n}L_n^{(i)}.
\]

For the translation field \(f=1\), the coefficient \(f_{i,-1}=1\) selects \(L_{-1}\) at each finite puncture. The term at infinity uses its expansion in the reciprocal coordinate. For a general field the principal part uses finitely many modes. A regular germ of positive radius can have an infinite tail of positive modes. A stronger entire-energy input norm absorbs the exponential growth bound on its Taylor coefficients. A formal Ward identity becomes an analytic identity only after this series and the sewing contractions have been defined continuously.

The Ward identity relates the descendant coefficients of a three-point field. Its overall scalar remains to be fixed. Place finite descendants \(u\in H_a\) at the origin and \(v\in H_b\) at \(z\). For positive output momentum \(p\), use the normalized binary field

\[
\mu_{a,b}(z)(u,v)(p)
=2^{1/4}\sqrt{C_0(a,b,p)}\,I_p^{b,a}(v,z)u.
\]

Here \(I_p^{b,a}\) denotes the intertwining field whose three-highest-vector coefficient at \(z=1\) is one. Choose a logarithm of the nonzero separation \(z\). The three-point normalization and spectral measure are fixed input data of the normalized boundary hypothesis. To specify them, put

\[
Q=\sqrt{(c-1)/6},\qquad
\mathfrak b+\mathfrak b^{-1}=Q.
\]

Choose \(0<\mathfrak b\le1\) for \(c\ge25\), and
\(\mathfrak b=e^{i\theta}\), \(0<\theta<\pi/2\), for \(1<c<25\).
Let \(\Gamma_{\mathfrak b}\) be Barnes' double Gamma function with periods
\(\mathfrak b,\mathfrak b^{-1}\), normalized by
\(\Gamma_{\mathfrak b}(Q/2)=1\), with its continuation in
\(\operatorname{Re}\mathfrak b>0\). Then

\[
C_0(p_1,p_2,p_3)=
\frac{\Gamma_{\mathfrak b}(2Q)}
     {\sqrt2\,\Gamma_{\mathfrak b}(Q)^3}
\frac{\displaystyle\prod_{\epsilon_1,\epsilon_2,\epsilon_3=\pm1}
 \Gamma_{\mathfrak b}\!\left(Q/2+i\sum_{j=1}^3\epsilon_jp_j\right)}
 {\displaystyle\prod_{j=1}^3
 \Gamma_{\mathfrak b}(Q+2ip_j)\Gamma_{\mathfrak b}(Q-2ip_j)},
\]

\[
d\nu(p)=m_{\mathfrak b}(p)\,dp,\qquad
m_{\mathfrak b}(p)=
4\sinh(2\pi\mathfrak b p)\sinh(2\pi p/\mathfrak b).
\]

For real principal labels these quantities are positive, and the binary map uses the positive square root of \(C_0\). The measure is \(\rho_0(p)\,dp/\sqrt2\), where \(\rho_0=\sqrt2\,m_{\mathfrak b}\) is the vacuum-resolution density; the factor \(\sqrt2\) is therefore not absorbed into \(d\nu\). These conventions are invariant under \(\mathfrak b\leftrightarrow\mathfrak b^{-1}\). [Virasoro fusion construction, §11.0 and equation (13.2)](#ref-ch10-02).

On \(u=\Omega_a,v=\Omega_b\), pairing with the normalized highest covector at momentum \(p\) gives the primary component

\[
g_z(p)=2^{1/4}\sqrt{C_0(a,b,p)}
                   z^{h_p-h_a-h_b}.
\]

Since the two inputs have weights \(h_a,h_b\) and the output has weight \(h_p\), dilation covariance gives \(z\partial_z g_z=(h_p-h_a-h_b)g_z\). This determines the power of \(z\) on the chosen logarithmic branch. The value at \(z=1\) fixes the remaining factor.

::: example {#ch10-four-primary-level-one title="The first descendant in a four-point block"}

Return to the circle around \(0,z\). Place primary fields of weights \(h_1,h_2,h_3,h_4\) at \(0,z,1,\infty\), respectively, and keep a positive intermediate label of weight \(h\). Divide out the two trivalent constants so that each primary coefficient at unit separation is one. What is the first correction to propagation of the intermediate highest state? The inner primary amplitude is \(z^{h-h_1-h_2}\). To test the level-one state \(L_{-1}\Omega\) on the seam, move its transpose \(L_1\) onto the primary at \(z\). Its Ward action \(z^2\partial_z+2h_2 z\) gives
\[
 (z^2\partial_z+2h_2z)z^{h-h_1-h_2}
   =(h+h_2-h_1)z^{h-h_1-h_2+1}.
\]
On the outer disk the primary amplitude with the third field at \(y\) is \(y^{h_4-h-h_3}\). Translating the seam insertion while holding \(y\) fixed gives minus the \(y\)-derivative, hence \(h+h_3-h_4\) at \(y=1\). The two linear functionals compose through the inverse Gram entry \(1/(2h)\). The resulting block starts with
\[
 z^{h-h_1-h_2}\left(1+
  \frac{(h+h_2-h_1)(h+h_3-h_4)}{2h}\,z+O(z^2)\right).
\]
For four equal external weights the relative coefficient is \(h/2\). At \(c=25\) and intermediate momentum \(1/2\) it is \(5/8\). This number is a coefficient at one fixed momentum. A comparison between cuts also uses the higher levels and the dependence on momentum. [Al. B. Zamolodchikov, *An Explicit Recurrence Formula for the Conformal Partial Wave Amplitude*, equations (1)–(3)](https://strings.itp.ac.ru/Papers/zamolodchikov1984.pdf#page=1).

:::

**Definition (normalized boundary hypothesis).** Fix the displayed trivalent normalization, the measure \(d\nu\), and the local coordinates at the four punctures. Compare the two channel expansions on logarithms continued together from the positive real configurations. For algebraic external states the hypothesis requires that the two four-point inverse-Gram sewings converge in their respective channel discs, that their marked channel vectors lie in the canonical spectral \(L^2\) spaces, and that the specified real unitary fusion transformation relates these vectors. Comparing paths through several changes of channel also uses the normalized positive-label pentagon. The role of quantum-group harmonic analysis in constructing fusion transformations is developed by [Ponsot and Teschner, *Liouville bootstrap via harmonic analysis on a noncompact quantum group*](https://arxiv.org/abs/hep-th/9911110); analytic continuation of fusion coefficients alone does not supply every completed-source estimate used here.

On the opening sphere take highest states with momenta \(P_1,\ldots,P_4>0\) in order and \(0<z<1\). For the cut around \(0,z\), let \(F_P^s(z)\) be the block with leading coefficient one and put \(C_s(P)=C_0(P_1,P_2,P)C_0(P,P_3,P_4)\). Multiplication by \(\sqrt{m_{\mathfrak b}(P)}\) is unitary from \(L^2(d\nu)\) to \(L^2(dP)\). Each of the two normalised binary fields contributes \(2^{1/4}\sqrt{C_0}\). Their sewn highest-state coefficient is therefore \(2^{1/2}\sqrt{C_s(P)}F_P^s(z)\). The marked crossing vector is \(2^{-1/4}\) times this sewing in either channel. On that vector the unitary acts by
\[
 2^{1/4}\sqrt{C_s(P)}\,F_P^s(z)
 \quad\longmapsto\quad
 \sqrt{\rho_0(P)C_s(P)}\,F_P^s(z).
\]
For the cut around \(z,1\), the two vertices instead give \(C_t(P)=C_0(P_2,P_3,P)C_0(P,P_1,P_4)\). In \(L^2(d\nu)\) the fusion operator takes the marked \(t\)-channel vector to the marked \(s\)-channel vector. Conjugating by the change of measure gives its action on the two vectors in \(L^2(dP)\). [The marked four-point blocks](#ref-ch10-02).

To obtain a scalar, prepare a momentum packet \(\eta_t\in L^2(d\nu)\) on the cut around \(z,1\). Write \(\psi_t,\psi_s\) for the two marked vectors and \(U\) for this fusion operator. On a common continuation where \(\psi_s=U\psi_t\), the same test on the other circle is \(\eta_s=U\eta_t\). With the Hilbert pairing conjugate-linear in the test,
\[
 \int\overline{\eta_s(P)}\,\psi_s(P)\,d\nu(P)
 =\int\overline{\eta_t(P)}\,\psi_t(P)\,d\nu(P).
\]
Unitarity gives this equality after the two linear three-point amplitudes have been contracted with the bilinear form on descendants. Keeping the numerical packet \(\eta_t\) fixed on the new cut would instead test \(\psi_t\) against \(U^{-1}\eta_t\).

## Finite uncut sewings {#ch10-finite-uncut-sewings}

Suppose that a further field is inserted at \(z\). Its two inputs play different roles. One state was already at the origin and has only the decay delivered by the previous sewing. The other is a newly supplied state at \(z\) and may be taken in a stronger input norm. Write \(\ell_z=-\log|z|\). Fix the stationary input exponent \(r\) and the output exponent \(s\). If

\[
r>-\log|z|>s,
\]

there is a finite moving-input exponent \(t\) for which the actual kernel

\[
K_z(a,b;p)
=e^{sE_p}\mu_{a,b}(z)
       (e^{-rE_a}\otimes e^{-tE_b})
\]

is Hilbert–Schmidt and satisfies

\[
\|K_z(a,b;p)\|_{\mathrm{HS}}^2
 \le C e^{-\gamma(a^2+b^2+p^2)},\qquad \gamma>0.
\]

The square of the Hilbert–Schmidt norm sums the squared matrix entries in orthonormal bases of the two input spaces and the output space. Thus the estimate controls the sum over descendants before integration over momenta. It holds for the specified kernel uniformly over every triple of positive labels on compact logarithmic coordinate sets with strict margins, and locally uniformly in \(c>1\). We shall use this kernel at the momentum delivered by the first vertex. An arbitrary representative of a spectral \(L^2\) class could be changed at that point without changing its norm. Together with this two-radius estimate, one needs bounds on the terms beyond any finite cutoff in descendant level. They make the tails of the sums converge uniformly in norm on smaller compact sets. Both estimates enter each subsequent sewing. [*Radial comb sewings*, Lemmas FC.1–FC.2](#ref-ch10-01).

Place \(d\) inputs at \(0,a_2,\ldots,a_d\), with

\[
0<|a_2|<\cdots<|a_d|.
\]

The left-associated sewing successively contracts the clusters \((1,2)\), \(((1,2),3)\), and so on through the \(d\)-th input. Retain each intermediate momentum \(k_2,\ldots,k_{d-1}\) as a spectral multiplicity variable. The direct integral for the output is

\[
\mathcal Z_d[s]
=L^2\!\left(d\nu(k_2)\cdots d\nu(k_{d-1})d\nu(e);
                                                H_e[s]\right).
\]

Here \(e\) is the final momentum. The squared norm integrates the squared \(H_e[s]\)-norm over \(e\) and all the \(k_i\). For \(d=3\), the section at \((k_2,e)\) is obtained by using the first vertex at \(k_2\) as the stationary input to the second. The label \(k_2\) remains available for pairing with a spectral test. Only the final representation carries the output energy weight. On the input side, write \(\mathcal H_{\mathbf p}[t]\) for the completed Hilbert tensor product of the \(H_{p_i}[t]\). Its inner product on elementary tensors is the product of the inner products in the factors.

::: {.conditional-theorem #ch10-theorem-101-finite-analytic-sewing n="10.1" title="finite analytic sewing"}

Under the normalized boundary hypothesis and the two-radius estimates above, fix \(d\ge2\), \(s\in\mathbb R\), positive external labels, and

\[
K\Subset\{0<|a_2|<\cdots<|a_d|,\;
                              s<-\log|a_d|\}
\]

on a logarithmic coordinate cover. There is a finite input exponent \(t_K\) for which the actual left-associated sewing is a holomorphic Hilbert–Schmidt family

\[
C_d(\mathbf a):\mathcal H_{\mathbf p}[t_K]\longrightarrow\mathcal Z_d[s].
\]

It therefore acts continuously on \(E_{\mathbf p}\). Every internal and output spectrum and every descendant level is uncut. Cutoffs in input, intermediate and output levels, and in the momenta, converge in Hilbert–Schmidt norm uniformly on smaller compact sets. The scalar factor is exactly

\[
2^{(d-1)/4}\sqrt{\prod_{v}C_0(k_{v,L},k_{v,R},k_v)},
\]

with one factor for each binary vertex. Bounds are uniform in the external positive labels and locally uniform in \(c\). They need not be uniform in \(d\), near collisions, or at the boundary of the strict output inequality. [*Radial comb sewings*, Theorem FC.3](#ref-ch10-01) · [Finite radial combs under the boundary hypothesis](#atlas-c-analytic-all-finite-radial-combs).

:::

To see how much of the hypothesis is used, place just one more puncture outside the first pair. A level weight on the intermediate representation must be weak enough for the first vertex to produce it and strong enough for the next to receive it. In the left-associated channel \(|a_2|<|a_3|\) leaves the interval

\[
-\log|a_3|<r<-\log|a_2|.
\]

For example, in the chosen local coordinates take \(a_2=e^{-3}\), \(a_3=e^{-1}\) and final exponent \(s=0\). The inner vertex can deliver exponent \(2<3\), and the outer vertex accepts that same exponent \(2>1\). The moving leg has its own sufficiently large finite input exponent. The squared kernel is Gaussian in every momentum, whereas the density \(m_{\mathfrak b}\) grows at most exponentially in the momentum. This gives the required spectral integrability. Strengthening the input stages slightly leaves geometric decay in the descendant tails. At each subsequent vertex choose the intermediate exponent strictly between the negative logarithms of the two adjacent radii. All the original inputs can use the same exponent. Take the maximum of the first stationary exponent and the finitely many moving-input exponents, since increasing an input exponent strengthens its norm. Taking the maximum over a finite cover of \(K\) gives one \(t_K\) for the whole sewing. The construction therefore gives a composition on these outputs without requiring the next vertex to act on every distributional output.

For another planar binary tree, centre each vertex at the position of its first leaf. Apply its field at the displacement from the left child centre to the right child centre. Shrinking the child clusters relative to this displacement supplies both required input exponents at the parent. Each tree thus has a region in which its own series converges. Four-point fusion maps compare these corners. Disjoint rotations commute, and the normalized pentagon identifies the two reassociation paths among the five trees on four ordered leaves. If \(F_{T',T}\) denotes the comparison from the retained-label space of \(T\) to that of \(T'\), the two path products have the same source and target and agree. For trees \(T,T'\), write \(C_T\) for the resulting sewing. Choose the logarithms of the vertex separations real on positive ordered configurations and continue them together. For \(0<|a_i|<|a_j|\) this fixes \(\log(a_j-a_i)=\log a_j+\log(1-a_i/a_j)\), with the last logarithm zero at \(a_i/a_j=0\). Under the normalized four-point comparison, the positive-label pentagon and the every-fibre estimates with normally convergent descendant tails on compact sets with strict energy margins, the spectral sections on the common sewing domain satisfy
\[
 C_{T'}=(F_{T',T}(e)\otimes\mathrm{id}_{H_e})C_T.
\]
Thus the comparison changes the intermediate momenta and leaves the output representation \(H_e\) fixed. Winding only the first vertex of the left tree once multiplies its section at the intermediate momentum \(k\) by \(\exp(2\pi i(h_k-h_a-h_b))\), where \(a,b\) are the labels of its two leaves. Descendant levels shift the exponent by integers. For example, at \(c=25\), \(a=b=1\) and \(k=1/2\) the exponent is \(-11/4\) and the phase is \(i\). As \(k\) varies, the phase equals one only on a countable set of spectral measure zero. Thus the same fusion operator cannot identify this winding with the unwound right tree on a nonzero section. Each raw tree series still has its own convergence domain. [*Independent finite-tree sewings and their coherence*, FT.1–FT.4](#ref-ch10-03).

## The vacuum as an input and as an output {#ch10-the-vacuum-as-an-input-and-as-an-output}

At positive momentum the level-one contraction divided by \(2h_p\). The vacuum has weight zero and its level-one descendant \(L_{-1}\Omega\) vanishes in the vacuum module. Nor does the positive family approach this weight. As \(p\downarrow0\), its lowest weight tends to \(h_*=(c-1)/24>0\). To sew a vacuum leg one must supply its own space of states. For a vacuum state \(v\), write \(v_N\in V_N\) for its orthogonal projection to level \(N\). The fixed weighted vacuum Hilbert space is

\[
V_\sigma=\left\{v=\sum_{N\ge0}v_N:
              \|v\|_{V_\sigma}^2
              =\sum_{N\ge0}\sigma_N^2\|v_N\|_V^2<\infty\right\}.
\]

**Definition (vacuum graph space).** To test a sewn state against every vacuum descendant, use every finite word \(D\) in the modes, including the empty word. Their common domain is

\[
G=\{v:\|Dv\|_{V_\sigma}<\infty
             \text{ for every finite Virasoro word }D\}.
\]

Its seminorms are \(q_D(v)=\|Dv\|_{V_\sigma}\), so the weight is applied at the output level after \(D\). For instance, \(L_{-2}\Omega\) is tested with weight \(\sigma_2\), even though \(\Omega\) lies at level zero. In the prescribed vacuum estimates
\(\sigma_0=1\) and \(\sigma_N=2^{3N}e^{N^2}M_N\), for \(N\ge1\). Here \(M_N\) is the maximum of \(1\), the prescribed annular-action weights through level \(N\), and the Hilbert–Schmidt norms of the normalized three-vacuum Ward form on level triples \(i,j,k\le3N\). The form has value one on \(\Omega^{\otimes3}\). See [*A common rapid completion for all vacuum sectors*, equation (A.3)](#ref-ch10-04). Replacing this graph topology by an arbitrary weak vacuum completion changes the theorem.

One vacuum input may be inserted anywhere in a fixed finite positive word, on the full source

\[
G\widehat\otimes_\pi\mathscr E_{p_1}
 \widehat\otimes_\pi\cdots\widehat\otimes_\pi\mathscr E_{p_r}.
\]

The unit coefficients are one. With the stationary input written first, the binary unit formulas are

\[
\Gamma_{p,V}(z)(v,\Omega)=v,
\qquad
\Gamma_{V,p}(z)(\Omega,v)=e^{zL_{-1}}v.
\]

In the first formula the surviving state was at the origin before the vacuum was inserted. In the second it was at \(z\). Erasing the vacuum does not move that puncture back to zero, which accounts for the translation \(e^{zL_{-1}}\). Translating back requires an energy norm in which the inverse series converges. When the vacuum is first, the reflected construction gives the separate output range \(\mathcal Z[-b]\), \(b>\log2\), on the normalized real interior and local complex neighbourhoods. Mixed trees have their own convergent corners and inherit comparisons from the positive tree obtained by removing the vacuum leaf. [*One vacuum input in an arbitrary finite word*, equation FV.12 and Theorem FV.3](#ref-ch10-05).

When the vacuum is the outgoing representation, a sewing assigns a number to each vacuum test state. Continuity of this assignment must hold in the graph topology just defined. The strong dual \(G'_b\), equipped with uniform convergence on bounded subsets of \(G\), receives a nonzero three-positive-input conformal block. At positions \(0,z,1\), its primary coefficient is

\[
2^{1/4}\sqrt{C_0(A,B,C)}
 z^{h_C-h_A-h_B}(1-z)^{h_A-h_B-h_C}.
\]

In the lens \(|z|<1,\ |1-z|<1\), choose \(\log z\) and \(\log(1-z)\) real on \(0<z<1\). These branches give a single holomorphic vacuum-output map throughout the lens. For every fixed finite positive word of length \(d\ge3\), a specified rooted vacuum channel similarly exists on the real ordered interior and complex neighbourhoods. It retains \(d-3\) uncut internal spectra as the separable Hilbert multiplicity \(M=L^2(d\nu^{\otimes(d-3)})\), with \(M=\mathbb C\) at \(d=3\). The target is

\[
V(M)=(M^\vee\widehat\otimes_\pi G)'_b.
\]

Here \(M^\vee\) is the complex-bilinear dual of the Hilbert multiplicity. To read an output, pair it with a momentum packet in \(M^\vee\) and a vacuum test in \(G\). Uniform convergence on bounded sets of such tensor tests defines the strong-dual topology. The proof first constructs fixed-label kernels, then uses annular composition and Möbius transport. [*A vacuum output for finite positive words*](#ref-ch10-06).

With three positive inputs there was no free momentum at a vacuum output. Four leave one momentum variable. This is the first case in which we can ask whether two choices of vacuum channel give the same functional on packets. Number the positive punctures \(0,t,y,1\) in that order with \(0<t<y<1/2\), and place the vacuum at infinity. The Möbius charts \((1-t)z/(z-t)\) and \(k(1/z-1)\), \(0<k<1\), give two convergent radial contractions with internal partitions \(14|23\) and \(43|21\). Their cross-ratios are \(X=(y-t)/(y(1-t))\) and \(1-X\). After transport of the tangent coordinates, the ratio of the primary prefactors is \(X^{h_1+h_4-h_2-h_3}\). Reversal of the trivalent block supplies the inverse power, so the normalized four-point fusion unitary takes the second resolved output to the first. The unitary acts on the surviving momentum in \(M=L^2(d\nu)\).

This equality tests vacuum descendants as well as vacuum amplitudes. In the local coordinate \(1/z\) at infinity, inserting \(L_{-2}\Omega\) on positive primaries applies \(\sum_i(z_i^3\partial_{z_i}+3h_i z_i^2)\) to the ground-state block. The same Ward recursion moves any finite vacuum descendant onto the four positive legs. The two raw sewings obey common energy bounds on compact subsets of their shared complex neighbourhood, so density extends the comparison to the completed four-input stage and the vacuum tests in \(G\). The comparison for all root choices at general length remains open. [The two independent vacuum sewings](#ref-ch10-15).

These outputs force the vacuum into any proposed common target. On the specified closed finite products of positive outputs, \(L_0\) is onto and invertible. Suppose \(F\) is a continuous Virasoro map from such a space to \(G'_b\). For every \(x\), intertwining gives \(F(L_0x)(\Omega)=F(x)(L_0\Omega)=0\). Surjectivity of \(L_0\) therefore makes the vacuum coefficient vanish on every input. Moving a word of negative modes off the vacuum test by the contragredient action reduces each descendant coefficient to such a vacuum coefficient. The finite descendants are dense in \(G\). Thus the map is zero, whereas the displayed vacuum-output block is nonzero. The positive output alone cannot represent it.

## A common intrinsic input space {#ch10-a-common-intrinsic-input-space}

The vacuum test in the preceding calculation detected a component invisible in every positive output. To ask whether a state can enter another field, we must keep track of all the components we receive. They can include a positive spectral section or distribution, a germ near the vacuum momentum and a vacuum functional. A change of presentation by a continuous Virasoro isomorphism must preserve the input condition. This asks for tests that can be pulled back along such maps. For continuous positive spectral sections, use the common oscillator realization \(\mathcal F=\widehat\bigoplus_{N\ge0}\mathcal F_N\), with energy \(E(p)=h_p+N\), and put

\[
\mathscr C_a
=\{f:e^{aE(p)}f(p)\in C_0([0,\infty);\mathcal F)\},
\qquad
\mathscr P_G=\varinjlim_{m\ge1}\mathscr C_{-m}.
\]

Here \(C_0([0,\infty);\mathcal F)\) denotes the space of continuous functions vanishing at infinity, with the supremum norm. The same letter with three momentum arguments denotes the trivalent constant. The input of \(\mathscr P_G\) is \(\bigcap_{n\ge1}\mathscr C_n\).

For a positive spectral object \(Y\), use its specified separable spectral realization on \((0,\infty)\), with scalar measure \(\nu_Y\) and measurable Hilbert multiplicities \(M_p\). The Virasoro modes act on the representation factor and leave the multiplicities fixed. Put

\[
\mathcal H_a(Y)
=L^2(d\nu_Y(p);M_p\widehat\otimes_2H_p[a]),
\qquad
\mathscr G(Y)=
\left(\bigcap_{n\ge1}\mathcal H_n(Y^\vee)\right)'_b.
\]

The superscript \(\vee\) means the complex-bilinear contragredient, including the multiplicity dual. The input consists of vectors in \(\bigcap_n\mathcal H_n(Y)\); it is not the contragredient test space. At a single positive label write \(R_p=(\mathscr E_p^\vee)'_b\). [*Functorial entire-energy sources for positive Virasoro recipients*, equations P.1–P.9](#ref-ch10-07).

Near the vacuum root \(p_+=iQ/2\), take the coordinate \(p=p_+-i\eta^2\). The meromorphic output \(\mathscr M\) consists of germs \(F(\eta)=\eta^{-1}v+g(\eta)\), with residue in the vacuum submodule and regular part bounded and holomorphic on one of the prescribed small discs in a weak Hilbert level space. Its level weights are \(e^{-m\omega(N)}\), where \(\omega(N)=1+Np(N)\) and \(p(N)\) is the partition number; the disc and stage are allowed to shrink and weaken together. Two representatives give the same germ when they agree on a smaller disc. Use the locally convex inductive limit of these disc and energy stages. Vacuum outputs are the spaces \(V(M)\) already defined.

Now take closed Virasoro-invariant subspaces \(R\) of finite products of these spaces, with their induced topologies. Morphisms are all ordinary continuous linear Virasoro intertwiners. Each factor keeps its original topology; “common” does not identify the different output spaces.

Take first one field regular on a disc and a vector \(x\) in the proposed input space. The Taylor coefficients multiply \(L_n x\) for arbitrarily large \(n\). Applying two fields requires control of the double series in \(L_m L_n x\), even if a fixed descendant has already been applied to \(x\). To handle any finite number of fields allow exponential weights on their mode numbers. If \(q\) is a continuous seminorm of \(R\), \(D\) a finite Virasoro word, \(a>0\), and \(k\ge0\), set

\[
p_{q,a,k,D}(x)=
\sum_{n_1,\ldots,n_k\ge1}
 e^{a(n_1+\cdots+n_k)}
 q(L_{n_1}\cdots L_{n_k}Dx),
\]

where \(k=0\) means \(q(Dx)\). Let \(\mathcal R_{\mathrm{reg}}(R)\) be the space on which all these seminorms are finite. Full mode words are needed to justify successive meromorphic actions and their brackets.

**Definition (common intrinsic input space).** Let \(Z\) run through the elementary positive and vacuum outputs, with their original input spaces \(S_0(Z)\) and inclusions \(j_Z:S_0(Z)\hookrightarrow Z\). Define

\[
\mathscr S_{\mathrm{com}}(R)=
\left\{x\in\mathcal R_{\mathrm{reg}}(R):
 Tx\in j_ZS_0(Z)
 \text{ for every continuous Virasoro map }T:R\to Z\right\}.
\]

Give it the regular-domain seminorms and every pulled-back seminorm of \(j_Z^{-1}Tx\). For an elementary positive or vacuum output \(R=Z\), the identity is one of the tests, so \(x\) must belong to its prescribed input space. In a subspace of a product, each projection to such a factor tests the corresponding input condition. A meromorphic factor contributes seminorms through \(\mathcal R_{\mathrm{reg}}(R)\). The tests are independent of the chosen presentation. Indeed, for a continuous Virasoro map \(u:R\to R'\) and a test \(T:R'\to Z\) of \(ux\), the composite \(Tu:R\to Z\) tests \(x\).

**Theorem 10.2 (intrinsic complete sources).** With the elementary outputs and topologies above, retain the normalized four-point data, the energy estimates and the prescribed vacuum graph bounds. Then \(\mathscr S_{\mathrm{com}}(R)\) is complete and Hausdorff and injects continuously and densely into \(R\). Every continuous Virasoro map restricts continuously to these sources. Meromorphic vector-field germs with finite principal part act by absolutely convergent mode series. On the elementary positive and vacuum objects the construction recovers the original topology exactly; in particular,

\[
\mathscr S_{\mathrm{com}}(R_p)
 =\mathscr E_p,
\qquad
\mathscr S_{\mathrm{com}}(V(M))
 =M\widehat\otimes_\pi G.
\]

An arbitrary common source need not be metrizable or nuclear. [*Complete functorial sources extending the original inputs*, Theorems IS.1–IS.4](#ref-ch10-08).

Completeness has a short explanation. In the complete product

\[
\mathcal R_{\mathrm{reg}}(R)\times\prod_{(Z,T)}S_0(Z),
\]

impose \(j_Zy_{Z,T}=Tx\) for each test. Both sides depend continuously on the product coordinates and take values in the Hausdorff space \(Z\), so each equality defines a closed subspace. Their intersection is complete. Since \(j_Z\) is injective, \(x\) determines every \(y_{Z,T}\), and the induced product seminorms are exactly the defining seminorms of \(\mathscr S_{\mathrm{com}}(R)\). Precomposition with a morphism pulls each target test back to a source test. Density needs more: scalar Fourier filters in \(L_0\) converge to the identity in the output topology while mapping continuously into every required source. On the vacuum they fix \(\Omega\) and cut off sufficiently high levels. The filters commute with intertwiners by their Fourier-integral construction; they are not themselves Virasoro intertwiners. [*Natural regularization on common Ward recipients*, Theorems NR.3–NR.4](#ref-ch10-09).

## Collision and the two conditions for descent {#ch10-collision-and-the-two-conditions-for-descent}

Take the two highest states at positive labels \(a,b\), sew them at a fixed nonzero separation \(z\), and look again at their primary coefficient \(g_z(p)\). Each state belongs to the entire-energy input space. Does their output also belong to it, perhaps after a finite propagation that damps high energies? The prescribed structure constant gives constants \(C,D>0\) for these fixed data with

\[
C^{-1}e^{-Dh_p}\le |g_z(p)|\le Ce^{Dh_p}.
\]

Apply any fixed finite energy propagation \(e^{-\tau L_0}\), with \(\tau\in\mathbb C\). The primary component becomes \(e^{-\tau h_p}g_z(p)\). Choosing an integer \(n>D+\operatorname{Re}\tau\) gives

\[
e^{nh_p}|e^{-\tau h_p}g_z(p)|
 \ge C^{-1}e^{(n-D-\operatorname{Re}\tau)h_p}
 \longrightarrow\infty.
\]

Taking the supremum in \(p\) already gives an infinite entire-energy seminorm in the continuous positive section space. For a Hilbert test, integrate the square of the same lower bound against \(m_{\mathfrak b}(p)\,dp\). This density is bounded below by a positive constant times \(p^2\), so the integral diverges. Both primary inputs belong to their prescribed source spaces, and their collision is a well-defined continuous output, but that output is outside the positive entire-energy source. Its positive projection is one of the tests in the definition of \(\mathscr S_{\mathrm{com}}\), so the common construction cannot remove the failure. [*Entire positive sources and actual collision values*, Theorem C.1](#ref-ch10-10).

For \(\varepsilon>0\), multiplying by \(e^{-\varepsilon L_0^2}\) does put the result into the positive source, but changes its primary coefficient and its covariance:

\[
e^{-\varepsilon L_0^2}L_k
=L_k e^{-\varepsilon(L_0-k)^2}.
\]

The factor \(e^{-\varepsilon h_p^2}\) suppresses the primary tail for every energy exponent. Thus damping can put the vector back in the source at the price of changing the mode action. To use the unmodified sewing, ask a different question. If two initial preparations give the same sewn vector, must a further operation have the same value on them? If so, is the induced operation continuous when the sewn vectors carry the topology of the output space?

**Proposition (descent through a sewn image).** Fix a finite sewing \(\mu:E\to R\) on its complete Fréchet input at a fixed configuration, with \(R\) its specified complete Hausdorff recipient. The sewn vector determines the factorization
\[
E\xrightarrow{\pi}T=E/\ker\mu
\xrightarrow{\,j\,}\overline{\mu(E)}^{\,R},
\qquad j([v])=\mu(v).
\]
The kernel is closed because \(\mu\) is continuous and \(R\) is Hausdorff, so \(T\) is complete Fréchet. The quotient remembers which preparations are equivalent. Its map \(j\) identifies these classes as a set with the sewn vectors. The same image also has the topology inherited from \(R\). An outer operation defined on the closure must be continuous for this latter topology. In particular, whenever sewn vectors \(\mu(v_\alpha)\) tend to zero in \(R\), their assigned values must tend to zero in the next recipient, regardless of how the preparations \(v_\alpha\) behave in \(E\). For a continuous linear map \(F:E\to W\) to factor through the completed image, two conditions enter.

1. It must annihilate the actual kernel, \(F(\ker\mu)=0\), so that its value depends only on the sewn vector.
2. The induced map on \(\mu(E)\) must be continuous for the topology inherited from \(R\), if it is to extend continuously to the completed image in \(R\).

For complete Hausdorff \(W\), these conditions give the unique continuous extension from the dense image. Continuity of \(F\) on \(E\) gives continuity on the quotient source; it does not by itself give the second condition. Ward identities likewise do not replace the first. [*Rational Ward identities and quotient sources for finite sewings*, Corollary FWd.3 and §“What the quotient property represents”](#ref-ch10-11).

For the continuous binary field maps with a vacuum input, the first condition simplifies: their kernels vanish on the stated receiving stages. Ward covariance preserves the closed kernel under the regular polynomial source action. Separation of the two punctures gives invariance under the regular modes at each leg. The two level projections then preserve the kernel. A nonzero kernel would contain a nonzero finite-bidegree vector, and positive-mode words would give the tensor of highest vectors in the kernel. Its field value is nonzero. Even zero kernel does not make the image topology equal to the source topology or produce a continuous inverse. [*Injectivity with completed vacuum inputs*, Lemma KV.1 and Theorems KV.3–KV.5](#ref-ch10-12).

For the positive radial comb the first descent condition can be decided at each fixed configuration. To see what a kernel vector would mean, imagine placing a polynomial vector field near just one of the punctures. If its action can be isolated there, a relation between sewn states must survive the separate Virasoro modes on that input.

::: {.conditional #ch10-fixed-label-comb-injectivity title="Injectivity of the fixed-label positive radial comb"}

Fix \(c>1\), \(d\ge2\) and positive external momenta \(\mathbf p=(p_1,\ldots,p_d)\). Take \(a_1=0\), \(0<|a_2|<\cdots<|a_d|\) on the logarithmic cover, and \(s<-\log|a_d|\). Under the normalized four-point hypothesis, the every-fibre two-radius and cutoff estimates of Theorem 10.1, and the full rational Ward identity with its convergent regular input germs, the actual map \(C_d(\mathbf a):E_{\mathbf p}\to\mathcal Z_d[s]\) is injective. The same holds for its tree continuations on the compatible lifts.

:::

Write \(K=\ker C_d(\mathbf a)\). The Ward identity says that acting with one polynomial field at all punctures carries \(K\) into itself. Take disjoint closed discs about the punctures. On disc \(i\) prescribe the polynomial \((w-a_i)^{n+1}\), \(n\ge-1\), and on the others prescribe zero. Polynomials on the plane approximate these functions uniformly on the union of the discs, whose complement is connected. For any given output seminorm of the source action, the regular-germ estimate bounds its error by this uniform error times one stronger input seminorm. Since \(K\) is closed in \(E_{\mathbf p}\), each separate \(L_n^{(i)}\) preserves it. [Rational Ward covariance and regular input germs](#ref-ch10-11).

In particular \(K\) is invariant under \(L_0^{(i)}\) and its rotations. The exponential series for a rotation converges in every source seminorm by using a stronger energy weight. Fourier projection of these rotations in each slot puts every joint-level component of a vector of \(K\) back in \(K\). If one such component is nonzero, products of positive modes take it to a nonzero multiple of the tensor of highest vectors. Indeed the negative-mode descendants span each finite level and its invariant Gram form is nondegenerate. Their transposes therefore separate vectors on the tensor product of those levels.

Suppose the highest tensor belonged to \(K\). Applying \(L_{-1}\) separately at each moving input keeps it in \(K\). These states give all position derivatives of its sewn section at \(\mathbf a\). Holomorphy would then force that section to vanish throughout the connected logarithmic radial domain. Test this conclusion at positive ordered positions. Put \(k_1=p_1\), \(k_d=e\), and project to the highest output at each fixed positive tuple of intermediate and final momenta. After division by
\[
 \prod_{j=2}^{d}a_j^{\,h_{k_j}-h_{k_{j-1}}-h_{p_j}},
\]
the coefficient is a convergent series in the adjacent ratios \(a_j/a_{j+1}\). An internal level \(N_j\) supplies the power \((a_j/a_{j+1})^{N_j}\). Its constant term comes from level zero at every seam and is \(2^{(d-1)/4}\sqrt{\prod_v C_0(k_{v,L},k_{v,R},k_v)}>0\). For \(d=2\) this is the whole normalized coefficient. For \(d>2\), let all the ratios tend to zero along one sequence. Vanishing of the spectral section at every configuration in the sequence would make all these coefficients zero on a single set of full spectral measure. At each tuple in that set the fixed-fibre convergence gives the positive constant in the limit. This contradiction proves injectivity. The unitary between compatible tree continuations preserves the kernel. [Finite radial sewings](#ref-ch10-01) · [Continuation of tree germs](#ref-ch10-03).

Thus a fixed-label positive comb identifies the entire-energy source with its image as a vector space. The identification does not give a continuous inverse for the topology of the received image. At a fixed configuration choose a stage \(t_K\) from Theorem 10.1. Take a vector supported at total descendant level \(N\) and scale it to have norm one at exponent \(t_K+1\). Its norm at \(t_K\) is \(e^{-(\sum_i h_{p_i}+N)}\), so its sewn vector tends to zero in \(\mathcal Z_d[s]\) and in the positive strong-dual recipient. The original inputs retain norm one at the stronger stage. For an admitted forest of these positive subwords the quotient by each subword kernel likewise leaves the original source. An operation on the received image still has to pass the continuity test above.

### Combining two completed clusters {#ch10-two-completed-clusters}

Take the binary field with input labels \(a,b\) and retain its positive-momentum section, meromorphic germ and vacuum component together (zero when absent). Let \(R_{a,b}\) be the closure of these output tuples in \(\mathscr P_G\times\mathscr M\times G^{\prime}_b\), with the induced topology. At a second positive vertex, the two inner momenta \(p,q\) can vary independently. To form a vacuum coefficient one must multiply two sections at the *same* momentum \(p=q\). For ground packets the value on the diagonal is the pointwise product. Cauchy–Schwarz bounds its \(L^1\) norm by the two \(L^2\) norms. The vacuum functional must still pair against an \(L^2\) packet in the surviving momentum, so we need an \(L^2\) bound on the product itself. One uniform bound and one square-integral bound suffice. At a fixed inner position \(\zeta\), choose \(r<-\log|\zeta|\). Require that the positive section of \(x\) belong to the Banach space

\[
X_r=\{f:e^{rE(p)}f(p)\in C_0([0,\infty);\mathcal F)\cap
                         L^2(d\nu;\mathcal F)\},\qquad
\|f\|_{X_r}=\|e^{rE}f\|_\infty+\|e^{rE}f\|_2 .
\]

**Definition (received positive section).** The domain \(D_r(R_{a,b})\) consists of pairs \((x,f)\in R_{a,b}\times X_r\) for which \(f\) equals the positive section of \(x\). Give it the subspace topology of this product. Thus convergence controls the marked output as well as both positive norms. The measure has full support and \(f\) is continuous, so its values at each momentum are specified. This graph is complete. At the fixed position \(\zeta\), finite preparations are dense in it. For example, let \(h_*=(c-1)/24\), choose a compact ground-energy band in \((h_*,h_*+1)\) avoiding integers, and take a nonzero continuous bump \(f(p)\) supported inside it. The pure ground packet \(f(p)\Omega_p\) with its other marks zero belongs to the graph. For a single original binary preparation at a fixed position the ground coefficient is locally holomorphic along the connected positive momentum axis. The bump vanishes on an open interval outside its support. Analytic continuation would force the ground coefficient to vanish throughout the axis, including where the bump is nonzero.

::: {.conditional #ch10-continuous-composite-sewing title="Two independently completed conformal blocks"}

Put the outer separation equal to one. For \(s<0\), take \(r>\log 2\) and \(t>\log 2\) sufficiently large on the moving leg for the two-radius estimate. Take two independent inputs on the corresponding graphs with positive sections \(f(p),g(q)\). Under the normalized boundary hypothesis the two continuous outputs on their completed projective tensor product are

\[
\begin{aligned}
 (p,q,e)&\longmapsto\mu_{p,q}(1)(f(p),g(q))(e)
   &&\text{in }L^2(d\nu(p)d\nu(q)d\nu(e);H_e[s]),\\
 p&\longmapsto\beta_{p,p}(1)(f(p),g(p))
   &&\text{in }V(L^2(d\nu)).
\end{aligned}
\]

Here \(\beta_{p,p}\) is the bilinear three-point vacuum block with value one on its three highest vectors. The positive-channel norm integrates over the two independent momenta using the Gaussian bound. For the vacuum channel the output is still a function of \(p\). In the product measure \(d\nu(p)d\nu(q)\), the diagonal contraction has density \(\delta(p-q)/m_{\mathfrak b}(q)\). Integrating first over \(q\) cancels its density \(m_{\mathfrak b}(q)\) and evaluates the second section at \(p\). The annular estimate bounds its resolved Hilbert norm by \(C\|e^{rE}f\|_\infty\|e^{tE}g\|_2\).

:::

For ground packets \(f(p)\Omega_p,g(p)\Omega_p\), this vacuum coefficient is the function \(f(p)g(p)\). If only its integral is requested, Cauchy–Schwarz gives \(\left|\int f g\,d\nu\right|\le\|f\|_2\|g\|_2\). To leave the common momentum available to an arbitrary final packet one needs \(\|fg\|_2\). For example, \(f,g\in L^4(d\nu)\) suffice for these scalar ground coefficients by Hölder's inequality. If every \(L^2\) packet \(g\) must be admitted with \(\|fg\|_2\le K\|g\|_2\), then \(|f|\le K\) almost everywhere. Otherwise a set of finite positive measure on which \(|f|>K\) supplies a counterexample by taking \(g\) to be its indicator.

Choose the same nonzero continuous bump for both packets, centred at a fixed \(p_0>0\). Shrink its width to \(\varepsilon\) and multiply its height by \(\varepsilon^{-1/2}\). The spectral density is positive and continuous near \(p_0\), so the two separate Hilbert norms remain bounded while the \(L^2(d\nu)\) norm of their product grows as \(\varepsilon^{-1/2}\). The supremum norm in \(X_r\) controls precisely this concentration. The graph estimate also controls the descendant levels, for which the two inputs are vectors and the contraction uses the vacuum block. [The two graph inputs](#ref-ch10-13).

The compact bump tests the two Hilbert norms alone. On a fixed compact momentum interval the original marked tuple already controls the supremum of its ground coefficient. On the ground level the inverse weight \(e^{mh_p}\) is bounded on the interval, so this seminorm is continuous on every stage \(\mathscr C_{-m}\). To test the full tuple, keep its meromorphic and vacuum components and move the concentration to higher energies.

::: {.counterexample #ch10-marked-weighted-l2-diagonal title="A resolved vacuum output with weighted Hilbert inputs"}

Keep the labels, normalization, outer vertex and exponents \(r,t\) of the preceding two-cluster result. Choose fixed nonzero logarithmic inner coordinates with \(r<-\log|\zeta_1|\) and \(t<-\log|\zeta_2|\). Give each input the topology of its full marked tuple together with just the weighted \(L^2(d\nu)\) norm of its positive section. There are inputs tending to zero in these topologies whose vacuum ground outputs have unbounded \(L^2(d\nu)\) norm in the retained momentum. The resolved vacuum operation has no continuous bilinear extension to these weakened graphs agreeing on the original preparations.

:::

Start in each input with its actual marked output on two highest vectors. Write \(f_i\) for its positive section and \(g_i(p)\) for its ground coefficient, \(i=1,2\). Choose \(m,D\ge0\) and \(C>0\) so that both sections satisfy \(\|e^{-mE} f_i\|_\infty\le C\) and \(|g_i(p)|\ge C^{-1}e^{-Dh_p}\). The second inequality is the [primary lower bound](#ref-ch10-10). Write \(R_*=\max(0,r,t)\) and choose \(A>\max\{2(m+R_*),4D\}\). With \(h_*=(c-1)/24\), choose \(0<\theta<1\) so that \(h_*+\theta\) is not an integer. Around \(E_j=h_*+j+\theta\) take a continuous energy cutoff \(b_j\), supported on an interval of width \(\delta_j=e^{-3AE_j}\), bounded by \(e^{AE_j}\) and equal to this height on the middle half of the interval.

Apply the cutoff to **total** energy. On the positive section it multiplies level \(N\) by \(b_j(h_p+N)\). The resulting tuple \(x_{i,j}=(b_j(E)f_i,0,0)\) belongs to the original marked closure. Here the vanishing of the other two components matters. For each fixed large \(j\), express the cutoff as a continuous function of \(y=e^{-E}\). Its support stays away from \(0\) and every vacuum value \(e^{-N}\). Its Bernstein polynomials in \(e^{-L_0}\) act on the full marked carrier and converge uniformly to the cutoff on the positive spectrum. On a sufficiently small complex neighbourhood of the excluded vacuum values and their limit \(0\), the binomial tails make the same polynomials tend uniformly to zero. Write \(h(\eta)=h_{p_+-i\eta^2}\), so \(h(0)=0\). This controls the meromorphic values at \(e^{-N-h(\eta)}\) on a smaller germ disc as well as the vacuum levels. Closedness gives the asserted tuple. The disc may depend on \(j\). Each fixed cutoff has compact momentum support and uses finitely many oscillator levels, so the tuple also belongs to the original graph with its supremum norm. [Energy cutoffs on the marked graph](#ref-ch10-13).

For \(M>m+A\), the positive sections tend to zero in the single stage \(\mathscr C_{-M}\). Indeed the extra weight on the selected band is at most a constant times \(e^{(m+A-M)E_j}\). For either input exponent \(v=r,t\), change variables to \(h_p+N\) at each contributing level. There are at most \(j+1\) such levels for large \(j\). On the band, \(p^2=j+\theta-N+O(\delta_j)\) stays bounded away from zero, and \(m_{\mathfrak b}(p)/(2p)\le C_1 e^{C_2\sqrt{E_j}}\). Hence
\[
 \|e^{vE}b_j(E)f_i\|_2^2
 \le C_3(j+1)\exp\!\bigl((-A+2m+2R_*)E_j+C_2\sqrt{E_j}\bigr)
 \longrightarrow 0 .
\]
This proves convergence of the inputs with all three original marks and the added Hilbert norm.

Now restrict \(p\) to the plateau where \(h_p\) itself is in the middle half of the band. At these momenta the cutoff leaves only level zero. The coefficient-one vacuum pairing on the two ground states returns \(e^{2AE_j}g_1(p)g_2(p)\). The plateau has \(d\nu\)-measure at least a constant times \(\delta_j\), since \(m_{\mathfrak b}(p)\ge c_*p^2\) and \(dh_p=2p\,dp\). Its contribution to the norm of the vacuum ground output is therefore at least
\[
 c_1 e^{(2A-2D)E_j}\sqrt{\delta_j}
   =c_1 e^{(A/2-2D)E_j}\longrightarrow\infty .
\]
This norm is a continuous seminorm on the prescribed output \(V(L^2(d\nu))\). It is the supremum over the bounded set of unit momentum packets tensored with the fixed vacuum vector \(\Omega\). Original preparations are dense at each chosen coordinate in the stronger graphs. Consequently agreement there fixes the operation on each filtered pair as well. The supremum estimate in the preceding two-cluster result controls this very concentration. Integrating the product against a single bounded scalar function would instead use its \(L^1\) bound. The resolved output keeps the momentum available for every \(L^2\) packet.

The same construction gives individual inputs whose pointwise vacuum product has no square-integrable ground component. Choose the fractional centres \(\theta_j\) in a closed subinterval of \((0,1)\) away from \(\mathbb Z-h_*\), tending to an interior point with successive gaps of order \(2^{-j}\). Increase \(A\) if necessary so that the fractional supports of the bands are disjoint for all large \(j\). The two sequences of filtered inputs are summable in their fixed negative stages and in their respective weighted Hilbert norms by the estimates above. Their sums belong to the weakened graphs because the full tuples converge with the two other marks zero. At a momentum on the \(j\)th ground plateau, adding an integer level does not change the fractional part of the energy. Hence no other cutoff in either sum contributes there. The squared ground-output norm dominates the sum of the squared lower bounds over these disjoint plateaux and is infinite.

::: figure fig-two-sewing-momenta

On a common strict overlap of three completed clusters, the positive-channel change of parentheses follows fibre by fibre from the normalized fusion identity on compatible logarithms and its uniform energy estimate. The two maps displayed above use only the positive sections of their inputs. At equal binary labels the full marked closure also contains an element with zero positive section and vacuum ground one. Both displayed operations annihilate this element. A tensor product on all marked outputs would have to act on such an incoming vacuum, transport the vacuum channel between independently completed presentations, and respect the coefficient-one units.

The graph norms allowed the outer contraction. Would it already be continuous in the topology on the full binary output, with no extra norm? A single outer primary gives a test. Take real inner separation \(0<z<1\), outer separation one and fixed positive labels. Pair the output with a highest covector at a fixed final label and a nonzero nonnegative smooth compact packet in the intermediate momentum. Write \(F_z\) for this pairing and \(G_z\) for the same pairing with \(L_{-1}\) applied to the outer primary of weight \(h_C\). For a finite preparation \(x_0\) with \(F_z(x_0)\ne0\), put \(r_0=\boldsymbol\mu_z(x_0)\), the full binary output. The vectors \(L_{-n}r_0\) tend to zero in the output topology. Ward covariance would force a continuous extension of \(F_z\) to take on them the values \((n-1)h_CF_z(x_0)-G_z(x_0)\), which grow linearly. The outer pairing thus fails the image-topology condition for descent. [The outer-sewing obstruction](#ref-ch10-14).

Keep the centres of the two clusters at \(0\) and \(1\). Sew a pair of positive states of label \(a\) near \(0\) and, independently, a pair of label \(b\) near \(1\). Insert the stress tensor at \(w\) and take the coefficient of the highest vacuum at infinity. This coefficient admits two expansions, according to which cluster receives the stress modes. To compare them on completed inputs, fix \(c>1\) and the two positive labels. Use the normalized four-point data and the two-radius bounds above, with logarithms continued from positive real positions. [*Virasoro fusion construction*](#ref-ch10-02), [*Radial comb sewings of arbitrary finite length*](#ref-ch10-01).

The stress test must be able to reach the vacuum from the complex momentum variable after summing the levels. Recall that \(p_+=iQ/2\) is the upper root of \(h(p)=0\). In the local parameter \(p=p_+-i\eta^2\), a marked equal-label pair can have a simple pole in \(\eta\). Write \(N\) for the oscillator level. Besides its positive section in \(X_s\), a marked cluster \(X\in R_{a,a}\) has a vacuum component \(v_X\) and a meromorphic component \(P_{\mathrm{an}}X\). Require \(v_X\) to have finite physical vacuum norm \(\|e^{sN}v_X\|_V\). For its meromorphic component require an even holomorphic numerator on one disc on which
\[
 U_X(\eta)=\eta(P_{\mathrm{an}}X)(\eta),\qquad
 \sup_{|\eta|<\delta}\|e^{sN}U_X(\eta)\|_{\mathcal F}<\infty,\qquad
 U_X(0)=\gamma_a\,\iota v_X,\quad
 \gamma_a=(\pi m_{\mathfrak b}(a))^{-1/2}.
\]
Here \(\mathcal F\) is oscillator Fock space and \(\iota\) is the levelwise vacuum embedding at \(p_+\). The stress coefficient will specialize at \(\eta=0\) only after the oscillator levels have been summed. To pass that sum through analytic continuation we need a bound for the entire series on a single momentum disc. Estimates on separate Taylor coefficients leave its radius uncontrolled. For a unit oscillator vector \(u_M\) at level \(M\), the test profile \(e^{M^2}\eta^{2M}u_M\) has every fixed Taylor coefficient eventually zero. Its norm grows without bound on every fixed disc. The graph requires agreement with the given germ at every level as well as a common radius. Impose the same conditions on \(Y\in R_{b,b}\) on a common disc avoiding the other Kac poles. The resulting graph controls both the momentum dependence and the entire oscillator sum.

Every original preparation from \(E_{a,a}\) belongs to this graph on a strict collar \(s<-\log|\zeta|\), where \(\zeta\) is the inner separation. This includes correlated arrays with infinitely many input levels. To see how the collar enters, take the unmarked coordinate-one vertex from input levels \(j,k\) to output level \(N\). For each \(\nu>0\) its Hilbert–Schmidt norm on the disc is at most \(C_\nu e^{\nu N+A_\nu(j+k)}\). As in the level-one example above, multiplying a covector of three-point amplitudes by the inverse Virasoro Gram matrix produces its outgoing state. A Kac label records a singular vector where this Gram matrix degenerates. Viewed as a function of momentum, the outgoing state is regular at the upper vacuum root \(p_+\). Away from that root its denominators can be cleared with one factor for each Kac label and sign, keeping both factors when two labels give the same pole. A Chebyshev estimate on real intervals of radius \((N+2)^{1/4}\) transfers the real energy estimate to the disc at an arbitrarily small exponential cost in \(N\). Choose \(\nu\) so that \(|\zeta|e^{s+\nu}<1\). The coordinate power now gives summable decay over \(N\), and a stronger input norm absorbs the cost in \(j+k\).

The collar estimate controls the size of a state in the Fock norm. At real momentum the invariant bilinear metric in the oscillator basis has unitary level matrices. Its level-one entry \((p+p_+)/(p-p_+)\) has a pole on continuation. Transporting the insertions to the two centres gives the bilinear form \(\Phi_{1,p}\). For a unit primary \(v_h\) of real weight \(h>0\), the descendant \(e=L_{-1}v_h/\sqrt{2h}\) has norm one. Its pairing at the two centres follows by differentiating the primary two-point coefficient,
\[
 \Phi_{1,p}(e,e)
 =\left.\frac{1}{2h}\partial_x\partial_y(y-x)^{-2h}\right|_{x=0,\,y=1}
 =-(2h+1).
\]
At every level the residue of the continued form annihilates the embedded vacuum in either slot. For even profiles the expansions are holomorphic in \(p-p_+\), so each possible derivative term in the finite part pairs that residue with a vacuum value in the other slot. The value on the two vacuum components is the physical vacuum pairing. Its levelwise estimate in the physical Hilbert norm costs at most \(C_\nu e^{\nu N}\) in squared norm relative to the embedded Fock vector, which the strict collar also absorbs.

Set \(s=10\) and \(0<|\zeta_1|,|\zeta_2|<e^{-10}/2\). The two expansions of the marked numerator are
\[
 \sum_{j\in\mathbb Z} w^{-j-2}\Phi_{1,p}(L_jU_X,U_Y)
 =
 \sum_{j\in\mathbb Z} (w-1)^{-j-2}\Phi_{1,p}(U_X,L_jU_Y).
\]
Each series converges normally for \(|w-1/2|\le 1/32\) and \(|\eta|\le\delta/2\). On inputs of levels \(m,n\), the Ward identity turns the negative-mode tail at either centre into the Taylor expansion of the principal part at the other. Its binomial sum costs at most a polynomial times \((32/15)^{m+n+2}\). The pole-normalized bilinear form costs \(C_\epsilon(2e^\epsilon)^{m+n}\). The two factors \(e^{-10m}\) and \(e^{-10n}\) make the level sum absolute. The two independently defined series thus give one continuous bilinear map on the completed graph inputs. At \(\eta=0\), the residues in the bilinear metric annihilate the embedded vacuum, and the normally convergent sum specializes to \(\gamma_a\gamma_b\) times the stress coefficient sewn in the physical vacuum module. The two incoming simple poles account for the factor \(\eta^2\) in the numerator. [The complex-momentum collar and stress expansions](#ref-ch10-16).

**Example (the vacuum stress coefficient).** Take \(\mathfrak b=2^{-1/4}\), \(a=1\), \(b=2\), and two highest-state pairs at the same small positive inner separation \(\tau\). Multiply each pair's input by \(\tau^{2h_i}\), \(i=a,b\), to give its vacuum ground coefficient one. Its pairing with \(L_{-n}\Omega\) is \((n-1)h_i\tau^n\) for every \(n\ge2\). At \(w=1/2\) the physical vacuum coefficient in either expansion is
\[
 (96+12\sqrt2)\tau^2-192\tau^3+O(\tau^4).
\]
The level-two vector \((2h_i/c)\tau^2L_{-2}\Omega\) pairs with the stress two-point function \(c/(2w^4)\) at the first centre and \(c/(2(w-1)^4)\) at the second. Together these give \(16(h_a+h_b)\tau^2\). The level-three translations differentiate at the two opposite centres. Their opposite signs give \(64(h_a-h_b)\tau^3\).

The same preparation determines the endpoint of the vacuum energy estimate. Write \(v_i\) for the physical vacuum component of either pair. The Virasoro commutator gives \(\|L_{-n}\Omega\|_V^2=c\,n(n^2-1)/12\). Projecting onto this one direction in each of the mutually orthogonal grades gives
\[
 \|e^{sN}v_i\|_V^2\ \ge\ \frac{12h_i^2}{c}
 \sum_{n\ge2}\frac{n-1}{n(n+1)}(e^s\tau)^{2n}.
\]
At \(e^s\tau=1\) the series on the right diverges logarithmically. For \(e^s\tau>1\) the terms grow. Together with the strict collar estimate this proves that the prepared vacuum component has finite weighted norm exactly when \(s<-\log\tau\).

For this ground coefficient a moving vacuum unit acts as the identity. A stationary unit translates the other insertion by \(e^{dL_{-1}}\). Translation from exponent \(s_0\) to a weaker exponent \(s_1\) is bounded when \(e^{-s_1}>e^{-s_0}+|d|\). To sew after translation, keep the positions in a common strict overlap and the receiving exponent above \(\log 2+\log(32/15)\). For example, \(|d|\le e^{-6}/4\) allows a loss from \(10\) to \(5\), then to \(4\) for the inverse translation on a smaller position compact. The construction leaves open a full marked output with all its descendant coefficients, arbitrary changes of parenthesization for mixed clusters, and a unit on that entire space. A disc uniform as both external labels vary across their equality locus would also require a separate estimate.

Both expansions now give the same vacuum stress coefficient, down to the sign of the cubic term in \(\tau\). Its value used the normalization of each input pair and the bilinear form on the vacuum module. An absolute filling amplitude raises a further question. Multiplying every \(Z(P)\) for a given filling by the same nonzero scalar preserves its homogeneous Ward identities and all its ratios \(Z(P)/Z(1)\) when \(Z(1)\ne0\). The scalar survives in the amplitude used in gluing. The Gaussian in one variable lets us compute both quantities with the very same integration density. [The Gaussian filling amplitude](11-states-and-lines.md#ch11).

## Source manuscripts {#ch10-source-manuscripts}

### 1. Radial comb sewings of arbitrary finite length {#ref-ch10-01}

Lemmas FC.1–FC.2 give the two-radius bound and the packet composition estimate. Theorem FC.3 applies them on the logarithmic radial domain. A turn of a binary coordinate multiplies its highest output of label \(e\) by \(\exp(2\pi i(h_e-h_a-h_b))\). Descendant levels change this exponent by integers. [Finite uncut sewings](#ch10-finite-uncut-sewings).

### 2. Virasoro fusion construction {#ref-ch10-02}

Section 11.0 fixes the continuation of the three-point normalization, and equation (13.2) fixes the measure \(d\nu\). For \(c>25\), Theorem 6.1 identifies the fusion kernel on the blocks using the disc bootstrap at zero bulk cosmological constant. The boundary three-point formula for arc constants \((0,\mu,1)\), \(\mu>0\), and its two-zero limit supply the boundary factors. Cyclic covariance permutes the charges and the arc constants together. Uniform Gaussian bounds give the limit at \(c=25\) in Theorem 10.2. For \(1<c<25\), Theorem 11.1 first continues the channel identities locally in \(c\). For reflected external labels the continuous channel is a Laplace transform of a positive measure. The crossed vacuum block continues this transform across any proposed interior convergence threshold. Positivity then gives convergence on the full radial interval. Theorem 13.3 gives the unitary on \(L^2(d\nu)\) and the positive-label pentagon. On algebraic external descendants Theorem 18.3 applies the same finite Ward differential operator to both channels. [The normalized four-point hypothesis](#ch10-definition-normalized-boundary-hypothesis).

For a diagonal sewing with finite positive measurable densities on this principal spectrum, let \(\sigma_s\) be the ratio of its \(s\)-channel density to \(\rho_0 C_s\), and define \(\sigma_t\) in the other channel in the same way. Local boundedness on the lens \(|z|<1,\ |1-z|<1\) gives a Gaussian moment in each channel. Lemmas 12.1–12.2 then give density of the weighted block spans in \(L^2((1+\sigma_s)\,dP)\) and \(L^2((1+\sigma_t)\,dP)\). Equality of the two sewings on the lens identifies the closed multiplication forms. Because the flat fusion kernel is nonzero almost everywhere, their spectral projections force the two density ratios to agree with one scalar for almost every pair of internal momenta at each external quadruple satisfying these hypotheses. [Rigidity of positive sewing on the fixed principal spectrum, Theorem 12.3](#s-positive-sewing-is-rigid-from-a-local-crossing-domain).

### 3. Independent finite-tree sewings and their coherence {#ref-ch10-03}

Lemmas FT.1–FT.2 construct the individual tree germs and compare a rotation on a common sewing region. Theorem FT.4 continues these germs from the same real ordered configurations, with the logarithms real there, by the constant fusion operator. The raw tree series converges on its own normal sewing regions. [Finite uncut sewings](#ch10-finite-uncut-sewings).

### 4. A common rapid completion for all vacuum sectors {#ref-ch10-04}

Equation (A.3) uses the finite three-vacuum Ward tensors to choose a single weight at each level. The graph norm applies this weight after each mode word. [Vacuum input norms](#ch10-the-vacuum-as-an-input-and-as-an-output).

### 5. One vacuum input in an arbitrary finite word {#ref-ch10-05}

Equation (FV.12) distinguishes the stationary and moving vacuum. A stationary vacuum leaves a translation of the surviving field. Theorem FV.3 supplies its receiving stage. [The two positional units](#ch10-the-vacuum-as-an-input-and-as-an-output).

### 6. A vacuum output for finite positive words {#ref-ch10-06}

Theorem VF.2 constructs the chosen rooted channel with its internal momenta retained. Lemma VF.3 detects a nonzero vacuum output by a vacuum test and a momentum packet. [The vacuum as output](#ch10-the-vacuum-as-an-input-and-as-an-output).

### 7. Functorial entire-energy sources for positive Virasoro recipients {#ref-ch10-07}

Equations (P.1)–(P.9) distinguish the original entire-energy vector source from the contragredient test space used to define the output. [Positive spectral sources](#ch10-a-common-intrinsic-input-space).

### 8. Complete functorial sources extending the original inputs {#ref-ch10-08}

Theorem IS.1 gives the complete graph defined by all continuous intertwiner tests. Theorem IS.4 recovers the elementary topologies, including each vacuum multiplicity. [The common intrinsic input space](#ch10-a-common-intrinsic-input-space).

### 9. Natural regularization on common Ward recipients {#ref-ch10-09}

Theorems NR.3 and NR.4 supply the approximating scalar energy filters and absolute convergence of the mode series for local vector fields. [Completeness and density](#ch10-a-common-intrinsic-input-space).

### 10. Entire positive sources and actual collision values {#ref-ch10-10}

Theorem C.1 uses the highest-state coefficient after finite energy propagation to detect the failure of closure of the entire-energy source. [A primary outside the input space](#ch10-collision-and-the-two-conditions-for-descent).

### 11. Rational Ward identities and quotient sources for finite sewings {#ref-ch10-11}

Corollary FWd.3 constructs the complete quotient by the actual kernel. Equations (FWd.26)–(FWd.27) give the kernel and image-topology conditions for a further map. [The fixed-label positive case](#ch10-fixed-label-comb-injectivity) · [Descent through the image](#ch10-collision-and-the-two-conditions-for-descent).

### 12. Injectivity with completed vacuum inputs {#ref-ch10-12}

Lemma KV.1 separates the two source actions on the closed kernel. Theorems KV.3–KV.5 apply it to the right vacuum field, the left vacuum field and the field with two vacuum inputs. [Separation on completed sources](#ch10-collision-and-the-two-conditions-for-descent).

### 13. Analytic Virasoro sewing and composite domains {#ref-ch10-13}

Sections 4–5 construct the graph of the received positive section and the two operations with independent and with diagonal momenta. [The high-energy diagonal test](#ch10-marked-weighted-l2-diagonal) · [Two completed clusters](#ch10-two-completed-clusters).

### 14. A necessary domain restriction for an outer sewing {#ref-ch10-14}

Theorem OS.3 tests a proposed continuous outer functional on negative modes of a finite preparation. Its Ward values grow linearly although the vectors tend to zero in the binary output topology. [The outer primary pairing](#ch10-two-completed-clusters).

### 15. Four positive punctures and a reflected local coefficient {#ref-ch10-15}

Sections 1–2 compare the two specified vacuum roots at four positive punctures. The normalized four-point fusion unitary acts on the remaining momentum. The Ward identity (5) treats descendants at the vacuum puncture. [The four-positive-input comparison](#ch10-the-vacuum-as-an-input-and-as-an-output).

### 16. A joint complex-momentum and ordinary-energy collar for marked Virasoro sewing {#ref-ch10-16}

Sections 2–4 give the common disc and oscillator-energy bound, the pole cancellation on vacuum values, and normal convergence of the two stress expansions. Their value at zero momentum coordinate uses the physical vacuum pairing. [The vacuum stress coefficient](#ch10-example-the-vacuum-stress-coefficient).
