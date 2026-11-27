# Analytic sewing and conformal blocks

Place four punctures at \(0,z,1,\infty\) on the sphere. One can draw a circle separating \(0,z\) from the other two punctures, or a circle separating \(z,1\) from the other two. Cutting along either circle gives two three-point amplitudes. To sew them back together one pairs their values on the states that can pass through the cut. The first cutting gives an expansion near \(z=0\), the second an expansion near \(z=1\). Even when both come from the same four-point amplitude, their series have different natural domains of convergence.

For the positive principal Virasoro representations at real central charge \(c>1\), the intermediate representations are labelled by a continuous momentum \(k>0\). Within each one the energy levels are discrete. A sewing therefore involves both a sum over these levels and a spectral measure for \(k\). The normalized four-point hypothesis assumes that the two sums converge in their channel discs and that continuing the punctures with their chosen local coordinates relates the two square-integrable channel vectors by the prescribed unitary operator. A second question arises even for a single channel. Can the state it produces be used as the input to another sewing? Its high-energy tail and, for a vacuum output, the concentration of its momentum distribution both matter.

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
since \([L_1,L_{-1}]=2L_0\) and \(L_1\Omega_p=0\). If the two three-point amplitudes take values \(u_1,v_1\) on this state, that level contributes \(u_1v_1/(2h_p)\) to their contraction in fixed local coordinates. The denominator is nonzero for every positive principal label. At higher levels the same prescription uses the inverse of the full Gram matrix. Hilbert norms control the convergence of this sum.

Write \(E_p=L_0^{(p)}\). For real \(t\), the energy space \(H_p[t]\) has norm

\[
\|v\|_{H_p[t]}^2
=\sum_{N\ge0}e^{2t(h_p+N)}\|v_N\|_{H_p}^2.
\]

For \(t>0\), this is the domain of \(e^{tE_p}\); negative \(t\) gives a weaker completion. The entire-energy input space is

\[
\mathscr E_p=\bigcap_{n\ge1}H_p[n],
\]

with the topology defined by these norms. Every finite descendant belongs to it. The intersection permits arbitrary positive exponential energy weights, which is stronger than requiring smoothness under finitely many powers of \(L_0\).

For finitely many labels, the completed projective tensor product

\[
E_{\mathbf p}
=\mathscr E_{p_1}\widehat\otimes_\pi\cdots
 \widehat\otimes_\pi\mathscr E_{p_d}
\]

is exactly the space of coefficient arrays \(u_{N_1,\ldots,N_d}\) for which

\[
\sum_{\mathbf N}e^{2a\sum_i(h_{p_i}+N_i)}
                 \|u_{\mathbf N}\|^2<\infty
\quad\text{for every }a\ge1.
\]

Thus the input includes entangled arrays, not just finite sums of separated vectors. The equality of topologies follows from the subexponential growth of descendant multiplicities: an arbitrarily small additional exponential weight makes the inclusions between Hilbert stages trace-class. Cauchy–Schwarz then bounds the projective tensor seminorm by a stronger Hilbert-array norm. This is the completion on which the subsequent operations act. [*Radial comb sewings of arbitrary finite length*, §“The entire finite-word source”](#ref-ch10-01).

A conformal block \(\mathcal B\) on the punctured sphere satisfies the Virasoro Ward identity
\[
\sum_i\mathcal B(v_1,\ldots,L_i(f)v_i,\ldots,v_d)=0
\]
for a rational vector field \(f(z)\partial_z\) with poles only at the punctures. The sum includes the outgoing puncture with its contragredient action. In a local coordinate \(w=z-a_i\) at a finite puncture the mode expansion is

\[
f(a_i+w)=\sum_{n=-M_i}^{\infty}f_{i,n}w^{n+1},
\qquad L_i(f)=\sum_{n=-M_i}^{\infty}f_{i,n}L_n^{(i)}.
\]

The finite principal part uses finitely many modes. The regular part is an infinite positive-mode series; its exponential coefficient growth is absorbed by a stronger entire-energy input norm. A formal Ward identity becomes an analytic identity only after this series and the sewing contractions have been defined continuously.

The normalized binary operation, with the stationary input first, is

\[
\mu_{a,b}(z)(u,v)(p)
=2^{1/4}\sqrt{C_0(a,b,p)}\,I_p^{b,a}(v,z)u.
\]

Here \(I_p^{b,a}\) is the normalized Virasoro intertwining field and \(z\ne0\) has a chosen logarithm. The three-point normalization and spectral measure are fixed input data of the normalized boundary hypothesis. To specify them, put

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

The primary component is

\[
g_z(p)=2^{1/4}\sqrt{C_0(a,b,p)}
                   z^{h_p-h_a-h_b}.
\]

The exponent is forced by \(L_0\)-covariance. The normalization and spectral measure carry further information: changing them changes the Hilbert comparison between channels.

Throughout the sewing results below, the **normalized boundary hypothesis** is retained: for algebraic external states, the two four-point inverse-Gram sewings converge in their respective channel discs, their marked channel vectors lie in the canonical spectral \(L^2\) spaces, and the two are related by the specified real unitary fusion transformation. We also retain the normalized positive-label pentagon when comparing trees. These are substantive hypotheses. The role of quantum-group harmonic analysis in constructing fusion transformations is developed by [Ponsot and Teschner, *Liouville bootstrap via harmonic analysis on a noncompact quantum group*](https://arxiv.org/abs/hep-th/9911110); analytic continuation of fusion coefficients alone does not supply every completed-source estimate used here.

## Finite uncut sewings {#ch10-finite-uncut-sewings}

The analytic estimate that permits iteration has two independent energy margins. If

\[
r>-\log|z|>s,
\]

there is a finite \(t\) such that the actual kernel

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

The constants are uniform on compact logarithmic coordinate sets with strict margins, uniformly in the positive labels and locally uniformly in \(c>1\). This estimate concerns the canonical kernel at every label. It never evaluates an arbitrary spectral \(L^2\) class at a point. All subsequent assertions retain this two-radius estimate and its normal descendant-tail bounds. [*Radial comb sewings*, Lemmas FC.1–FC.2](#ref-ch10-01).

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

No energy weight is imposed on a retained multiplicity label.

**Theorem 10.1 (finite analytic sewing).** Under the normalized boundary hypothesis and the two-radius estimates above, fix \(d\ge2\), \(s\in\mathbb R\), positive external labels, and

\[
K\Subset\{0<|a_2|<\cdots<|a_d|,\;
                              s<-\log|a_d|\}
\]

on a logarithmic coordinate cover. There is a finite input exponent \(t_K\) for which the actual left-associated sewing is a holomorphic Hilbert–Schmidt family

\[
C_d(\mathbf a):
\widehat\bigotimes_{i=1}^{d}{}_{\!2}H_{p_i}[t_K]
                         \longrightarrow\mathcal Z_d[s].
\]

It therefore acts continuously on \(E_{\mathbf p}\). Every internal and output spectrum and every descendant level is uncut. Finite cutoffs converge normally in this operator norm on smaller compact sets. The scalar factor is exactly

\[
2^{(d-1)/4}\sqrt{\prod_{v}C_0(k_{v,L},k_{v,R},k_v)},
\]

with one factor for each binary vertex. Bounds are uniform in the external positive labels and locally uniform in \(c\). They need not be uniform in \(d\), near collisions, or at the boundary of the strict output inequality. [*Radial comb sewings*, Theorem FC.3](#ref-ch10-01).

The mechanism is visible at the third insertion. The inequalities \(|a_2|<|a_3|\) permit an intermediate exponent

\[
-\log|a_3|<r<-\log|a_2|.
\]

The first collision produces an output in the stage \(r\); the second vertex receives that same stage. Its Gaussian spectral bound is integrable against the canonical measure. Strengthening the input stages slightly leaves geometric decay in the descendant tails. Repeating this argument finitely many times constructs the entire word. The intermediate output is used through its proved stage, rather than through an operation postulated on its whole distributional completion.

Every planar binary tree has an independently convergent hierarchical corner, obtained by taking each subcluster sufficiently small compared with its parent separation. Four-point fusion maps compare these corners. Disjoint rotations commute, and the normalized pentagon identifies the two reassociation paths among the five trees on four ordered leaves. If \(F_{T',T}\) denotes the comparison from the retained-label space of \(T\) to that of \(T'\), the two path products have the same source and target and agree. For trees \(T,T'\), write \(C_T\) for the resulting sewing. With the normalized four-point comparison, the positive-label pentagon, and the estimates at every triple of labels with normally convergent descendant tails on compact sets with strict energy margins, the equality of spectral sections on a common sewing domain is
\[
 C_{T'}=(F_{T',T}(e)\otimes\mathrm{id}_{H_e})C_T.
\]
Thus the comparison changes the intermediate momenta and leaves the output representation \(H_e\) fixed. A non-left-associated raw series still has its own convergence domain. [*Independent finite-tree sewings and their coherence*, FT.1–FT.4](#ref-ch10-03).

## The vacuum as an input and as an output {#ch10-the-vacuum-as-an-input-and-as-an-output}

The vacuum representation has highest weight zero and is a separate object from the positive principal family. Its highest vector \(\Omega\) obeys \(L_{-1}\Omega=0\). Write \(v_N\in V_N\) for its orthogonal level components. The fixed weighted vacuum Hilbert space is

\[
V_\sigma=\left\{v=\sum_{N\ge0}v_N:
              \|v\|_{V_\sigma}^2
              =\sum_{N\ge0}\sigma_N^2\|v_N\|_V^2<\infty\right\}.
\]

To control all field insertions, take its graph space

\[
G=\{v:\|Dv\|_{V_\sigma}<\infty
             \text{ for every finite Virasoro word }D\}.
\]

Its seminorms are \(q_D(v)=\|Dv\|_{V_\sigma}\), so the weight is applied at the output level after \(D\). The weights are the prescribed ones from the vacuum estimates:
\(\sigma_0=1\) and \(\sigma_N=2^{3N}e^{N^2}M_N\), with the fixed nondecreasing maximum \(M_N\ge1\) of the annular-action weights and finite three-vacuum Ward tensor norms specified in [*A common rapid completion for all vacuum sectors*, equation (A.3)](#ref-ch10-04). Replacing this graph topology by an arbitrary weak vacuum completion changes the theorem.

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

The second formula includes the translation of the remaining insertion. Its inverse is applied only on a stage on which that translation is defined. When the vacuum is first, the reflected construction gives the separate output range \(\mathcal Z[-b]\), \(b>\log2\), on the normalized real interior and local complex neighbourhoods. Mixed trees have their own convergent corners and inherit comparisons from the positive tree obtained by removing the vacuum leaf. [*One vacuum input in an arbitrary finite word*, equation FV.12 and Theorem FV.3](#ref-ch10-05).

Vacuum output requires another map. The strong dual \(G'_b\), equipped with uniform convergence on bounded subsets of \(G\), receives a nonzero three-positive-input conformal block. At positions \(0,z,1\), its primary coefficient is

\[
2^{1/4}\sqrt{C_0(A,B,C)}
 z^{h_C-h_A-h_B}(1-z)^{h_A-h_B-h_C}.
\]

The construction extends throughout \(|z|<1, |1-z|<1\), including \(0<z<1\). For every fixed finite positive word of length \(d\ge3\), a specified rooted vacuum channel similarly exists on the real ordered interior and complex neighbourhoods. It retains \(d-3\) uncut internal spectra as a Hilbert multiplicity \(M\), with target

\[
V(M)=(M^\vee\widehat\otimes_\pi G)'_b.
\]

The proof first constructs fixed-label canonical kernels, then uses annular composition and Möbius transport. [*A vacuum output for finite positive words*](#ref-ch10-06).

Four positive insertions already admit a comparison between two choices of vacuum channel. Number the positive punctures \(0,t,y,1\) in that order with \(0<t<y<1/2\), and place the vacuum at infinity. The Möbius charts \((1-t)z/(z-t)\) and \(k(1/z-1)\), \(0<k<1\), give two convergent radial contractions with internal partitions \(14|23\) and \(43|21\). Their cross-ratios are \(X=(y-t)/(y(1-t))\) and \(1-X\). After transport of the tangent coordinates, the ratio of the primary prefactors is \(X^{h_1+h_4-h_2-h_3}\). Reversal of the trivalent block supplies the inverse power, so the normalized four-point fusion unitary takes the second resolved output to the first. The unitary acts on the surviving momentum in \(M=L^2(d\nu)\).

This equality tests vacuum descendants as well as vacuum amplitudes. In the local coordinate \(1/z\) at infinity, inserting \(L_{-2}\Omega\) on positive primaries applies \(\sum_i(z_i^3\partial_{z_i}+3h_i z_i^2)\) to the ground-state block. The same Ward recursion moves any finite vacuum descendant onto the four positive legs. The two raw sewings obey common energy bounds on compact subsets of their shared complex neighbourhood, so density extends the comparison to the completed four-input stage and the vacuum tests in \(G\). The comparison for all root choices at general length remains open.

These outputs force the vacuum into any proposed common target. On the specified closed finite products of positive outputs, \(L_0\) is onto and invertible. A continuous Virasoro map from such a space to \(G'_b\) must have zero highest-vacuum coefficient, since that coefficient annihilates the image of \(L_0\). Vacuum cyclicity then kills every descendant coefficient. Thus the map is zero, whereas the displayed vacuum-output block is nonzero. The positive output alone cannot represent it.

## A common intrinsic input space {#ch10-a-common-intrinsic-input-space}

It is natural to ask whether the input topology can be recovered from the output representation itself. The relevant outputs have several different topologies. For continuous positive spectral sections, use the common oscillator realization \(\mathcal F=\widehat\bigoplus_{N\ge0}\mathcal F_N\), with energy \(E(p)=h_p+N\), and put

\[
\mathscr C_a
=\{f:e^{aE(p)}f(p)\in C_0([0,\infty);\mathcal F)\},
\qquad
\mathscr P_G=\varinjlim_{m\ge1}\mathscr C_{-m}.
\]

Here \(C_0\) denotes continuous functions vanishing at infinity, and each stage has its weighted supremum norm. It is unrelated to the three-point constant \(C_0(a,b,p)\). The input of \(\mathscr P_G\) is \(\bigcap_{n\ge1}\mathscr C_n\).

For a specified positive spectral object \(Y\), with its scalar measure \(\nu_Y\) and measurable Hilbert multiplicities \(M_p\), let

\[
\mathcal H_a(Y)
=L^2(d\nu_Y(p);M_p\widehat\otimes_2H_p[a]),
\qquad
\mathscr G(Y)=
\left(\bigcap_{n\ge1}\mathcal H_n(Y^\vee)\right)'_b.
\]

The superscript \(\vee\) means the complex-bilinear contragredient, including the multiplicity dual. The input consists of vectors in \(\bigcap_n\mathcal H_n(Y)\); it is not the contragredient test space. At a single positive label write \(R_p=(\mathscr E_p^\vee)'_b\). [*Functorial entire-energy sources for positive Virasoro recipients*, equations P.1–P.9](#ref-ch10-07).

The meromorphic output \(\mathscr M\) consists of germs \(F(\eta)=\eta^{-1}v+g(\eta)\), with residue in the vacuum submodule and regular part bounded and holomorphic on one of the prescribed small discs in a weak Hilbert level space. Its level weights are \(e^{-m\omega(N)}\), where \(\omega(N)=1+Np(N)\) and \(p(N)\) is the partition number; the disc and stage are allowed to shrink and weaken together. The topology is the original inductive-limit germ topology. Vacuum outputs are the spaces \(V(M)\) already defined.

Now take closed Virasoro-invariant subspaces \(R\) of finite products of these spaces, with their induced topologies. Morphisms are all ordinary continuous linear Virasoro intertwiners. Each factor keeps its original topology; “common” does not identify the different output spaces.

First impose rapid decay for all positive-mode words. If \(q\) is a continuous seminorm of \(R\), \(D\) a finite Virasoro word, \(a>0\), and \(k\ge0\), set

\[
p_{q,a,k,D}(x)=
\sum_{n_1,\ldots,n_k\ge1}
 e^{a(n_1+\cdots+n_k)}
 q(L_{n_1}\cdots L_{n_k}Dx),
\]

where \(k=0\) means \(q(Dx)\). Let \(\mathcal R_{\mathrm{reg}}(R)\) be the space on which all these seminorms are finite. Full mode words are needed to justify successive meromorphic actions and their brackets.

Let \(Z\) run through the elementary positive and vacuum outputs, with their original input spaces \(S_0(Z)\) and inclusions \(j_Z:S_0(Z)\hookrightarrow Z\). Define

\[
\mathscr S_{\mathrm{com}}(R)=
\left\{x\in\mathcal R_{\mathrm{reg}}(R):
 Tx\in j_ZS_0(Z)
 \text{ for every continuous Virasoro map }T:R\to Z\right\}.
\]

Give it the regular-domain seminorms and every pulled-back seminorm of \(j_Z^{-1}Tx\). Testing all maps removes dependence on a chosen finite-product presentation.

**Theorem 10.2 (intrinsic complete sources).** With these elementary spaces, their original topologies and the analytic hypotheses already stated, \(\mathscr S_{\mathrm{com}}(R)\) is complete and Hausdorff and injects continuously and densely into \(R\). Every continuous Virasoro map restricts continuously to these sources. Meromorphic vector-field germs with finite principal part act by absolutely convergent mode series. On the elementary positive and vacuum objects the construction recovers the original topology exactly; in particular,

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

impose the closed graph equations \(j_Zy_{Z,T}=Tx\). Injectivity of \(j_Z\) determines every auxiliary coordinate. Precomposition with a morphism proves functoriality. Density needs more: scalar Fourier filters in \(L_0\) converge to the identity in the output topology while mapping continuously into every required source. On the vacuum they fix \(\Omega\) and cut off sufficiently high levels. The filters commute with intertwiners by their Fourier-integral construction; they are not themselves Virasoro intertwiners. [*Natural regularization on common Ward recipients*, Theorems NR.3–NR.4](#ref-ch10-09).

## Collision and the two conditions for descent {#ch10-collision-and-the-two-conditions-for-descent}

Exact recovery of the positive input spaces permits a decisive test. The prescribed structure constant has a two-sided Gaussian estimate, so for fixed \(a,b,z\ne0\) there are \(C,D>0\) with

\[
C^{-1}e^{-Dh_p}\le |g_z(p)|\le Ce^{Dh_p}.
\]

Apply any fixed finite energy propagation \(e^{-\tau L_0}\), with \(\tau\in\mathbb C\). The primary component becomes \(e^{-\tau h_p}g_z(p)\). Choosing an integer \(n>D+\operatorname{Re}\tau\) gives

\[
e^{nh_p}|e^{-\tau h_p}g_z(p)|
 \ge C^{-1}e^{(n-D-\operatorname{Re}\tau)h_p}
 \longrightarrow\infty.
\]

It fails an entire-energy seminorm. The corresponding spectral norm also diverges for the canonical measure. Both primary inputs belong to their prescribed source spaces, and their collision is a well-defined continuous output, but that output is outside the positive entire-energy source. Its positive projection is one of the tests in the definition of \(\mathscr S_{\mathrm{com}}\), so the common construction cannot remove the failure. [*Entire positive sources and actual collision values*, Theorem C.1](#ref-ch10-10).

Multiplying by \(e^{-\varepsilon L_0^2}\) does put the result into the positive source, but changes its primary coefficient and its covariance:

\[
e^{-\varepsilon L_0^2}L_k
=L_k e^{-\varepsilon(L_0-k)^2}.
\]

That regularized operation is useful on its stated domain. It is a different operation.

For each finite sewing \(\mu:E\to R\) there is a factorization
\[
E\xrightarrow{\pi}T=E/\ker\mu
\xrightarrow{\,j\,}\overline{\mu(E)}^{\,R},
\qquad j([v])=\mu(v).
\]
The quotient \(T\) is complete Fréchet. The map \(j\) is continuous and injective with dense image, but the topology induced from \(R\) can be strictly coarser than the quotient topology. For a continuous linear map \(F:E\to W\) to factor through the completed image, two conditions enter.

1. It must annihilate the actual kernel, \(F(\ker\mu)=0\), so that its value depends only on the sewn vector.
2. The induced map on \(\mu(E)\) must be continuous for the topology inherited from \(R\), if it is to extend continuously to the completed image in \(R\).

For complete Hausdorff \(W\), these conditions give the unique continuous extension from the dense image. Continuity of \(F\) on \(E\) gives continuity on the quotient source; it does not by itself give the second condition. Ward identities likewise do not replace the first. [*Rational Ward identities and quotient sources for finite sewings*, Corollary FWd.3 and §“What the quotient property represents”](#ref-ch10-11).

On the completed binary sources with a vacuum factor, source separation proves injectivity of the actual continuous linear field maps on their stated received stages. The argument extracts a nonzero finite-bidegree component of a hypothetical kernel vector, then uses positive-mode words to reach the tensor of highest vectors, whose field value is nonzero. Even zero kernel does not make the image topology equal to the source topology or produce a continuous inverse. [*Injectivity with completed vacuum inputs*, Lemma KV.1 and Theorems KV.3–KV.5](#ref-ch10-12).

### Combining two completed clusters {#ch10-two-completed-clusters}

A binary output \(x\) retains its positive-momentum section \(f(p)\), a meromorphic germ and, where present, a vacuum component. Let \(R_{a,b}\) be the closure of the binary outputs of labels \(a,b\) in this product. At a fixed inner position \(\zeta\), choose \(r<-\log|\zeta|\). Require that the positive section of \(x\) belong to the Banach space

\[
X_r=\{f:e^{rE(p)}f(p)\in C_0([0,\infty);\mathcal F)\cap
                         L^2(d\nu;\mathcal F)\},\qquad
\|f\|_{X_r}=\|e^{rE}f\|_\infty+\|e^{rE}f\|_2 .
\]

The domain \(D_r(R_{a,b})\) is the graph of this condition in \(R_{a,b}\times X_r\). Thus convergence controls the marked output as well as both positive norms. The measure has full support and \(f\) is continuous, so its values at each momentum are specified. This graph is complete. At the fixed position \(\zeta\), finite preparations are dense in it. For example, let \(h_*=(c-1)/24\), choose a compact ground-energy band in \((h_*,h_*+1)\) avoiding integers, and take a nonzero continuous bump \(f(p)\) supported inside it. The pure ground packet \(f(p)\Omega_p\) with its other marks zero belongs to the graph. It cannot be the output of a single original binary preparation at a fixed position, since such a preparation has a locally holomorphic ground coefficient in positive momentum.

Put the outer separation equal to one. For \(s<0\), take \(r>\log 2\) and \(t>\log 2\) sufficiently large on the moving leg for the two-radius estimate. Take two independent inputs on the corresponding graphs with positive sections \(f(p),g(q)\). Under the normalized boundary hypothesis the two continuous outputs on their completed projective tensor product are

\[
\begin{aligned}
 (p,q,e)&\longmapsto\mu_{p,q}(1)(f(p),g(q))(e)
   &&\text{in }L^2(d\nu(p)d\nu(q)d\nu(e);H_e[s]),\\
 p&\longmapsto\beta_{p,p}(1)(f(p),g(p))
   &&\text{in }V(L^2(d\nu)).
\end{aligned}
\]

Here \(\beta_{p,p}\) is the bilinear three-point vacuum block with value one on its three highest vectors. The first map integrates the Gaussian bound of the positive kernel. The second keeps the common momentum as an output variable. Against \(d\nu(p)d\nu(q)\) its diagonal has density \(\delta(p-q)/m_{\mathfrak b}(q)\). The annular estimate bounds its resolved Hilbert norm by \(C\|e^{rE}f\|_\infty\|e^{tE}g\|_2\). For two ground packets this vacuum coefficient is the function \(f(p)g(p)\). Shrinking both packets to width \(\varepsilon\) and taking their height to be \(\varepsilon^{-1/2}\) keeps their separate Hilbert norms bounded, but the \(L^2\) norm of the product grows as \(\varepsilon^{-1/2}\). The supremum norm in \(X_r\) controls precisely this concentration. Integrating the common momentum away would lose the test.

On a common strict overlap of three completed clusters, the positive-channel change of parentheses follows fibre by fibre from the normalized fusion identity and its uniform energy estimate. The two maps displayed above use only the positive sections of their inputs. At equal binary labels the full marked closure also contains an element with zero positive section and vacuum ground one. Both displayed operations annihilate this element. A tensor product on all marked outputs would have to act on such an incoming vacuum, transport the vacuum channel between independently completed presentations, and respect the coefficient-one units. Even on original inputs, an outer primary can give a functional continuous for the quotient topology whose values on a sequence of negative modes grow linearly while the corresponding vectors tend to zero in the whole output space. This is where the continuity condition for descent has force.

A conformal block fixes a multilinear functional in a specified channel. Multiplying a filling amplitude by a nonzero scalar preserves its homogeneous Ward identities. To determine the corresponding state or absolute vacuum amplitude, one must also specify the filling, the pairing used for sewing and its normalization.

## Source manuscripts {#ch10-source-manuscripts}

### 1. Radial comb sewings of arbitrary finite length {#ref-ch10-01}

### 2. Virasoro fusion construction {#ref-ch10-02}

### 3. Independent finite-tree sewings and their coherence {#ref-ch10-03}

### 4. A common rapid completion for all vacuum sectors {#ref-ch10-04}

### 5. One vacuum input in an arbitrary finite word {#ref-ch10-05}

### 6. A vacuum output for finite positive words {#ref-ch10-06}

### 7. Functorial entire-energy sources for positive Virasoro recipients {#ref-ch10-07}

### 8. Complete functorial sources extending the original inputs {#ref-ch10-08}

### 9. Natural regularization on common Ward recipients {#ref-ch10-09}

### 10. Entire positive sources and actual collision values {#ref-ch10-10}

### 11. Rational Ward identities and quotient sources for finite sewings {#ref-ch10-11}

### 12. Injectivity with completed vacuum inputs {#ref-ch10-12}

For the two completed cluster inputs, see *Analytic Virasoro sewing and composite domains*, §§4–5, and *A necessary domain restriction for an outer sewing*, Theorem OS.3. The comparison of the two four-input vacuum channels is proved in *Four positive punctures and a reflected local coefficient*, §§1–2, using the normalized four-point fusion unitary of *Virasoro fusion construction*, Theorem 13.3.
