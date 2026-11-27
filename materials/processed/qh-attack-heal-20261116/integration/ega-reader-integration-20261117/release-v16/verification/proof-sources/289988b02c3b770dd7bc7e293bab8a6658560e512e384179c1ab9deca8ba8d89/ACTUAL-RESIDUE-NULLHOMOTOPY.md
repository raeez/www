# Vanishing of the actual middle-block residue

Let \(\Bbbk\) be a field of characteristic zero and
\(X=\mathbb A^1_\Bbbk\). Let
\(\alpha:F\otimes^!C_{\Bbbk^2}\to C_{\Bbbk^2}\) be an actual pointed
coassociative coalgebra action, with \(F\) factorizing and with no bound
on its coefficient complexes. Fix three nonempty wrong-colour blocks
\(A|B|C\), a root \(a\in A\), and marks \(b\in B\), \(p\in C\).
Put
\[
Y=U_{A,B,C},\qquad M=(F_A\boxtimes F_B\boxtimes F_C)|_Y.
                                                               \tag{1}
\]
The source in (1) uses the original ordered word and its specified
coassociativity comparisons. All rooted primitives and their right-end
vacuum convention remain fixed.

Retain the original one-vacuum witness \(V_B\) for the cut \(A|BC\),
restricted to the carrier where its genuine correct-colour vacuum
\(z\) avoids \(C\) and may collide with \(B\). Let \(\ell_{B;p}\) be
the full residue/Spencer functional against
\[
\lambda_p(z)=d\log\frac{z-x_p}{x_p-x_a}.             \tag{2}
\]
It is regular along the \(B\)-divisor and kills the constant boundary
unit. Write \(\varepsilon_B\) for the unweighted normal residue,
including the same average of the two extreme ordered restrictions.
Its degree is \(-1\), and it also kills that unit.

**Theorem.** There are specified cochains, on the original sources,
\[
Q_\ell\in\mathcal E_Y^{-3},\qquad
Q_\varepsilon\in\mathcal E_Y^{-4},
\]
whose differentials are respectively the full pointed images
\(\ell_{B;p}V_B\) and \(\varepsilon_BV_B\) of the common pointed
recipient. Here
\[
\mathcal E_Y=\operatorname{Fib}\!\left[
R\operatorname{Hom}_{\mathcal D_Y}(M,J_Y)
\xrightarrow{u^*}R\operatorname{Hom}_{\mathcal D_Y}(J_Y,J_Y)
\right],\qquad
 d_{\mathcal E}(x,h)=(dx,xu-dh).                    \tag{3}
\]
The construction uses two genuine vacuum labels which remain distinct
singleton fibres under every quotient map. Their geometric coincidence
is allowed. It is natural in pointed actors, arbitrary action parameters,
and actual ordered collisions internal to \(A,B,C\), with \(a,b,p\)
transported.

For the originally fixed pointed three-block boundary
\[
\begin{split}
\Omega&=D_{A,B}^{b}f_C+D_{AB,C}^{p}-D_{A,BC}^{p}
                  -H_Ac_{B,C}-a_{A,B,C},\\
\Omega^{\mathrm{pt}}&=(\Omega,\omega),
\end{split}                                                     \tag{4}
\]
retain the specified cochain \(K\) from the same-word supported filling,
so that
\[
\Omega=dK-\ell_{B;p}\underline V_B.                  \tag{5}
\]
There is an explicit scalar comparison carrying the first nullhomotopy
above to a nullhomotopy of the original pointed residual
\[
R^{\mathrm{pt}}
 =\bigl(\ell_{B;p}\underline V_B,Ku-\omega\bigr).     \tag{6}
\]
Consequently (4) has a specified degree-minus-three primitive in (3),
with its original pointing and the stated parameter and collision faces.
No actor exchange or cocommutativity hypothesis is used.

The formulas below give both nullhomotopies and their scalar comparison.
They concern this action-generated class. They do not assert that
\(\ell_{B;p}\) or \(\varepsilon_B\) is null on an arbitrary kernel input.

## The restricted two-vacuum source

Let \(S=\{z,w\}\), with the order \(z<w\), where \(w\) is a further
genuine correct-colour vacuum. First take the actual vacuum diagram for
the old cut \(A|BC\), and then restrict every vacuum coordinate to avoid
\(C\). Over (1) its carrier is
\[
W'_S=U_{A,BC+S}\cap\{z_i\ne x_c:\ i\in S,\ c\in C\}.
                                                               \tag{7}
\]
For an old affine order chart with smooth Noetherian coefficient ring
\(R\), put
\[
h(t)=\prod_{v\in B}(t-x_v),\qquad
g(t)=\prod_{v\in A\sqcup C}(t-x_v),\qquad f_i=h(z_i).
\]
For \(D\subseteq S\), set \(H_D=\prod_{i\in D}f_i\), with
\(H_\varnothing=1\), and define
\[
O'_{S,D}=W'_S[H_D^{-1}],\qquad U'_S=W'_S[H_S^{-1}].  \tag{8}
\]
No difference between \(z\) and \(w\) is inverted.
The whole ordered \(B+S\) carrier, including every internal branch,
remains. The geometric identification
\[
W'_S\simeq
(\mathscr R_{A\sqcup C}\times\mathscr R_{B\sqcup S})_{\mathrm{disj}}
\big|_{U_{A,B,C}}                                   \tag{9}
\]
is used only for the normal source and its charts. The old coefficient
is still \(M\) in (1); it is not replaced using an actor factorization
for a different word.

For \(D=\varnothing,\{z\},\{w\}\), let
\(\mathsf G'_{S,D}=\mathsf N'_{S,D}[1]\) represent
\[
M_0\longmapsto
\operatorname{Fib}\!\left[
R\operatorname{Hom}_{O'_{S,D}}
 (j_*j^!q^!M_0,J)
\longrightarrow
R\operatorname{Hom}_{U'_S}(q^!M_0,J)
\right],\qquad j:U'_S\hookrightarrow O'_{S,D},       \tag{10}
\]
where \(q\) forgets the two vacuum coordinates. In the unshifted fibre
use \(d(m,k)=(dm,\operatorname{res}m-dk)\), and use
\(d_Gs=-s d_N\) for the shift.
The same notation with one vacuum denotes the corresponding restricted
one-vacuum kernel.

Open base change identifies the source in (10) with the restriction
of the original \(A|BC\) source. Before restriction it is localized at
all \((B\sqcup C)\)--vacuum walls. On (7), the \(C\)-walls are already
removed; the remaining source localization is exactly at all \(B\)-walls.
This identifies the relative open as well as the global source.

The chart kernel is therefore computed from
\[
Q_S=R[z,w,g(z)^{-1},g(w)^{-1}],\qquad
K_{S,D}=
\left(Q_S[H_D^{-1}]\right)^\wedge_{(H_{S\setminus D})}
                         [H_{S\setminus D}^{-1}],
\qquad
\mathsf G'_{S,D}|_{\mathrm{chart}}
 \simeq\operatorname{DR}_{z,w}K_{S,D}.               \tag{11}
\]
In particular, the \(C\)-avoidance factors are present before the
union-divisor completion. Formula (11) recomputes the actual restricted
source; it does not commute open localization with completion.

Write \(R_z,R_w\) for the two proper restriction maps out of
\(\mathsf G'_{S,\varnothing}\). Constant insertion gives
\[
P_w:\mathsf G'_z\to\mathsf G'_{S,\{w\}},\qquad
P_z:\mathsf G'_w\to\mathsf G'_{S,\{z\}}.             \tag{12}
\]
For example, inside \(O'_{S,\{w\}}\), the new coordinate \(w\) is
already disjoint from \(A,C\) by (7) and from \(B\) by (8).
Thus the inverse image of the old relative open is exactly \(U'_S\).
This verifies the localized-source map (12), including its open component.
Let \(j_z,j_w,j_{S,D}\) be the constant localization boundary units.

## Two mixed functionals before coefficient Hom

On the formal targets retain the two closed total forms
\[
\begin{split}
\lambda_z&=d\log\frac{z-x_p}{x_p-x_a}
           =\alpha_z\,dz+\mu_z,\\
\lambda_w&=d\log\frac{w-x_b}{x_b-x_a}
           =\alpha_w\,dw+\mu_w.
\end{split}                                                     \tag{13}
\]
Thus
\[
\begin{split}
\alpha_z&=(z-x_p)^{-1},&
\mu_z&=-\frac{d_Rx_p}{z-x_p}-d_R\log(x_p-x_a),\\
\alpha_w&=(w-x_b)^{-1},&
\mu_w&=-\frac{d_Rx_b}{w-x_b}-d_R\log(x_b-x_a).
\end{split}                                                     \tag{14}
\]
All old tangent directions, including those moving \(a,b,p\), are
retained in (14). The first form is regular at the entire \(B\)-divisor;
the second has its marked normalized residue there.

For \(T\subseteq S\), let
\[
J_T=R[z_i:i\in T]^\wedge_{(f_i:i\in T)}[H_T^{-1}].
\]
The proper kernels in (11) have the actual coefficient maps
\[
\begin{array}{lll}
K_{S,\varnothing}\longrightarrow J_{zw},&
K_{S,\{w\}}\longrightarrow J_{z|w},&
K_{S,\{z\}}\longrightarrow J_{w|z},
\end{array}                                                     \tag{15}
\]
where the first block of an iterated target is outermost. Deleted
coordinates are expanded first, and the active coordinates are then
completed. Every factor inverted in \(g\) has its unique inverse in
these targets. For \(u\in A\sqcup C\), this inverse is explicitly
\[
\frac1{t-x_u}
=-\frac{q_u(t)}{h(x_u)}
       \sum_{m\ge0}\left(\frac{h(t)}{h(x_u)}\right)^m,
\qquad
q_u(t)=\frac{h(t)-h(x_u)}{t-x_u}.                    \tag{16}
\]
The denominator \(h(x_u)\) is a unit on \(Y\). Formula (16) is used
in the formal targets, while all such factors remain in the source
\(Q_S\) of (11).

Let \(\mathcal L\) denote total unweighted \(B\)-residue in \(z,w\),
with fixed orientation \(dz\wedge dw\). On an iterated target it is
taken in the outer block first, with that same relative orientation.
Use the Spencer convention
\[
\operatorname{Sp}_R(C)^{q-r}
 =\mathcal D_R\otimes_R\bigwedge^rT_R\otimes_R C^q,
\qquad d=d_{\mathrm{Sp}}+(-1)^r d_C.                 \tag{17}
\]
There is a degree-zero functional \(E_D^\ell\) whose affine components
on (15) are
\[
\begin{split}
E_0^\ell(q)&=\mathcal L(q\alpha_z\alpha_w),\\
E_1^\ell(v;q\,dz)&=-\mathcal L(q\alpha_w\mu_z(v)),\\
E_1^\ell(v;q\,dw)&=-\mathcal L(q\alpha_z\mu_w(v)),\\
E_2^\ell(v_1\wedge v_2;q\,dz\wedge dw)
 &=-\mathcal L\bigl(q(\mu_z\wedge\mu_w)(v_1,v_2)\bigr).
\end{split}                                                     \tag{18}
\]
The differential operator in the leading Spencer factor acts on the
result in \(R\). Components not listed in (18) are zero.

There is also a degree-minus-one functional \(E_D^\varepsilon\).
Its only affine components are
\[
\begin{split}
E_0^\varepsilon(q\,dz)&=\mathcal L(q\alpha_w),&
E_0^\varepsilon(q\,dw)&=0,\\
E_1^\varepsilon(v;q\,dz\wedge dw)&=
                         +\mathcal L(q\mu_w(v)).
\end{split}                                                     \tag{19}
\]
In particular the last sign in (19) is positive.
Equations (18) and (19) are the full Spencer versions of
\[
\operatorname{Res}_{z,w}
 (\omega\wedge\lambda_z\wedge\lambda_w),\qquad
\operatorname{Res}_{z,w}(\omega\wedge\lambda_w),     \tag{20}
\]
respectively, after placing base forms first and using (17).

On the actual carrier, compose each affine map with restriction to a
pattern open having all relative labels before or after the entire
\(B\)-block. If the two ordered relative words are \((\ell,r)\), give
this restriction the weight
\[
q_S(\ell,r)=\frac1{2^{|S|}\,|\ell|!\,|r|!}.         \tag{21}
\]
For two variables there are four same-side patterns of weight \(1/8\)
and two mixed patterns of weight \(1/4\). All old \(A,C\) orders remain
in the base in (9). The selected pattern opens need not cover the
carrier; restriction from the entire actual kernel is part of each map.
This defines
\[
E_D^\ell:\mathsf G'_{S,D}\to J_Y,
\qquad E_D^\varepsilon:\mathsf G'_{S,D}\to J_Y[-1].  \tag{22}
\]
For the one-variable maps in the same convention put
\[
\phi_\ell=\ell_{B;p},\qquad
\phi_\varepsilon=\varepsilon_B,
\qquad e_\ell=0,\quad e_\varepsilon=-1.             \tag{23}
\]
A map of degree \(e\) is called closed when
\(df-(-1)^e fd=0\).

**Lemma 1.** The maps (22) are closed differential-module maps of their
stated degrees, formed before arbitrary coefficient Hom. For
\(\bullet=\ell,\varepsilon\), they satisfy
\[
\begin{split}
E_{\{w\}}^\bullet R_w
 &=E_\varnothing^\bullet
  =E_{\{z\}}^\bullet R_z,\\
E_{\{w\}}^\bullet P_w&=\phi_\bullet,
& E_{\{z\}}^\bullet P_z&=0,\\
\phi_\bullet j_z&=0.
\end{split}                                                     \tag{24}
\]
These identities have simultaneous representatives on the formal Spencer
diagrams and retain their actual ordered-chart and old-collision maps.

**Proof.** The localization telescope for the source in (10) gives
(11): its principal-part target is
\(Q_S[H_S^{-1}]/Q_S[H_D^{-1}]\), and multiplication by the active
support product is surjective on that target. The compatible inverse
system is multiplication by a formal Laurent element followed by
principal part. Relative de Rham and ordered descent give the displayed
kernel. This construction retains the source before any old Hom.

The maps (15) and their restriction squares are defined before puncturing
the active formal variables. For example, the two routes
\[
\begin{array}{ccc}
K_{S,\varnothing}&\longrightarrow&J_{zw}\\
\downarrow R_w&&\downarrow\\
K_{S,\{w\}}&\longrightarrow&J_{z|w}
\end{array}                                                     \tag{25}
\]
agree on \(Q_S\). Both are continuous for the original
\((h(z)h(w))\)-adic topology: in the target the \(w\)-factor is a
unit and the \(z\)-factor is topologically nilpotent. They therefore
agree on the union completion and its puncture. The identical argument
with \(z,w\) reversed proves the second proper square. Every extra
\(A\)- or \(C\)-factor maps to its same inverse (16). Differentiating
these formulas agrees with differentiating the rational inverses, so
the comparisons retain all old and normal connections.

The regular first logarithm needs a slightly different finite-coefficient
observation from a normalized marked logarithm. In a monic \(h\)-adic
expansion, \(\alpha_z\) and every coefficient of \(\mu_z\) have
nonnegative powers of \(h(z)\), by (16). A Laurent input has a finite
lower bound in each joint block. Consequently its residue after
multiplication by either regular coefficient reads only finitely many
of its negative-power coefficients. The number may depend on that lower
bound. It need not be only the indices \(0,-1\).

On an iterated target, the outer extraction still reads finitely many
coefficients. Each has its permitted finite inner lower bound, so the
next extraction is again finite. On the common joint source in (25),
regrouping followed by these extractions gives the same result as the
joint extraction. The normalized \(w\)-logarithm and unweighted residues
already read finitely many coefficients. Thus both functionals in
(20) are well defined on every target in (15), and the two restriction
identities in (24) follow on every Spencer component. No identification
of the two iterated rings, or interchange of ordinary localization with
completion, has been made.

Closedness of the total forms in (13), residue integration by parts,
and commutation of residue with old derivatives give, for (18),
\[
d_{\mathrm{CE}}E_r^\ell=(-1)^rE_{r+1}^\ell d_C
\quad(r=0,1),\qquad d_{\mathrm{CE}}E_2^\ell=0.        \tag{26}
\]
These are precisely the chain equations in convention (17). For (19),
\[
d_{\mathrm{CE}}E_0^\varepsilon
   =E_1^\varepsilon d_C,\qquad
 d_{\mathrm{CE}}E_1^\varepsilon=0,\qquad
 E_0^\varepsilon d_C|_{C^0}=0.                      \tag{27}
\]
For example, on \(q\,dz\), the first equality uses
\(v(\alpha_w)=\partial_w\mu_w(v)\), so both sides are
\(-\mathcal L((\partial_wq)\mu_w(v))\). On \(q\,dw\), both vanish
by \(z\)-integration by parts. This also fixes the positive sign in
(19). Extending \(\mathcal D_R\)-linearly on the Spencer resolution
gives the closed maps (22), including their degrees.

For constant insertion of \(w\), a source form contains no \(dw\)
and its coefficients are independent of \(w\). Its \(w\)-factor in
(18) or (19) is therefore only
\[
\operatorname{Res}_{h(w)}\frac{dw}{w-x_b}=1.
\]
The remaining component is exactly \(\ell_{B;p}\) or
\(\varepsilon_B\), with no extra sign. For insertion of \(z\),
formula (18) contributes
\(\operatorname{Res}_{h(z)}dz/(z-x_p)=0\); every other possible
component would require a missing \(dz\). Formula (19) always requires
\(dz\), so it is zero on this insertion as well. These are identities
of all the Spencer components, not only of horizontal sections.
The one-variable constant boundary has no positive normal-form degree;
its normalized regular-log residue and its unweighted residue are zero.
This proves the last two lines of (24) on affine charts.

Forgetting a relative label sends a pattern in (21) to its erased-word
pattern. The weights over either one-variable extreme pattern sum to
\(1/2\). Hence the affine insertion identities give exactly the original
one-variable averages, while a zero insertion remains zero. The actual
restriction maps use the same two-variable pattern opens throughout.
This proves (24) on the entire carrier, retaining all other branches in
the domain of its restriction maps.

An allowed old collision preserves \(A,B,C\) separately and transports
\(a,b,p\). In particular \(p-a\), every \(B\)--\(C\) difference and
every \(A\)--\(B\) difference remain units. Expanding ordered old fibres
commutes with every pattern and every forgetting map in (9), (21).
The specialized support polynomials have cofinal completion ideals.
The coefficient rings before completion are \(R\)-flat; their Noetherian
completions, punctures, finite relative de Rham terms and functorial
Spencer terms give the actual finite-quotient transfer comparison.
Formula (16), the total forms (13), and residue extraction specialize
under that comparison. This retains collisions within all three old
blocks, including mergers into the marked labels. It is a comparison
of these displayed kernels and maps, not a cartesian base-change claim
for arbitrary completed objects.

Old-chart restriction uses coefficientwise maps into the newly computed
completions. The finite coefficient operations just described commute
with those maps. All proper-restriction and insertion comparisons can
therefore be represented simultaneously by the common coefficient and
Spencer maps, with their higher comparison faces retained. Applying old
coefficient Hom, however unbounded, preserves these identities. This
proves the lemma. \(\square\)

## The two actual deletion edges

Use the genuine-vacuum deletion diagram for the original cut \(A|BC\),
with the original reference \(r=p\in C\subset BC\), and restrict it to
(7). This is a restriction of an action diagram, not a new cut of the
actor. Its one-vacuum vertices are \(\tau_z,\tau_w\) and its two-vacuum
vertex is \(\tau_{zw}\). They have degree \(-2\) in the shifted relative
kernel and are closed.

For a retained genuine label \(v\) and a deleted label \(d\), use the
prescribed edge
\[
L_d=s\Delta_{\{v\};d},\qquad
\Delta_{\{v\};d}=h_{\{v\};d}-\tau_v\vartheta_d.     \tag{28}
\]
Here the symbols on the right are first written in the unshifted fibre.
The original weighted edge is
\[
h_{\{v\};d}
 =\bigl(\Lambda_{I;v,d}
        -(\chi_{0;v,d}-H_A\chi_{BC;v,d}),
          D_r\eta_{v,d}+\epsilon_{v;d}\bigr),        \tag{29}
\]
where
\(\eta_{v,d}=\vartheta_{v+d}-\vartheta_vb_d-\vartheta_d\).
The last term is the actual cut/pointing comparison prism, with both
relative components retained. These are the original whole-vacuum
edges with their full rooted comparison.

Their partial-deletion cover consists of
\[
O'_d\cap U_{I\sqcup(\{v\}\setminus T),\ T\sqcup\{d\}},
\qquad T\subseteq\{v\},\quad I=A\sqcup B\sqcup C.   \tag{30}
\]
Restricting every vacuum to avoid \(C\) preserves this cover and all
its source identifications. The source on (30) still has one genuine
whole-vacuum block; there is no cut between coincident genuine vacua.
The deleted label is disjoint from \(I\) on its partial open. Equations
(7)--(12) identify precisely that partial open and its forgetting map.
The native edge equation consequently becomes
\[
\begin{split}
d_G L_w&=P_w\tau_z-R_w\tau_{zw},\\
d_G L_z&=P_z\tau_w-R_z\tau_{zw}.
\end{split}                                                     \tag{31}
\]
Only these two proper one-deletion edges are used. No fully deleted
vertex or quotient identifying \(z\) and \(w\) occurs.

The original one-vacuum recipient, on the same restricted carrier, has
its full pointed form
\[
V_B-j_zD_r=\tau_z-d_G A_z,\qquad
A_z=s(0,-D_r\vartheta_z).                            \tag{32}
\]
The underlying cochain of \(V_B\) is the prescribed
\(-s t_0+\partial_{\mathrm{loc}}Q\); \(A_z\) has degree \(-3\).
The fixed pointing comparison and the entire native cube transport are
part of (28)--(32). Their role is made explicit below.

Let \(\mathcal G^{u}_{S,D}\) be the fibre of the two mapping functors
\[
R\operatorname{Hom}_Y(M,\mathsf G'_{S,D})
\longrightarrow R\operatorname{Hom}_Y(J_Y,\mathsf G'_{S,D}).
                                                               \tag{33}
\]
The cochains in (31)--(32) are taken in these full source-pointing fibres.
A closed kernel map \(T\) of degree \(e\) acts on them by
\[
T(x,h)=(Tx,(-1)^eTh),\qquad d(Tx)=(-1)^eT(dx).       \tag{34}
\]
Thus both signs of the degree-minus-one functional in (22) are retained.

## The residue primitives

**Proposition 2.** In the full pointed complex (3), define
\[
\boxed{\quad
Q_\bullet=(-1)^{e_\bullet}
 \left(E_{\{w\}}^\bullet L_w
       -E_{\{z\}}^\bullet L_z-\phi_\bullet A_z\right),
\qquad \bullet=\ell,\varepsilon .\quad}             \tag{35}
\]
Then
\[
d_{\mathcal E}Q_\ell=\ell_{B;p}V_B,\qquad
 d_{\mathcal E}Q_\varepsilon=\varepsilon_BV_B.       \tag{36}
\]
In particular, the specified singleton-middle-block residue
\(\varepsilon_B\underline V_B\) has the actual degree-minus-four
primitive underlying \(Q_\varepsilon\). The same formula works for
arbitrary finite \(B\) with its total finite-divisor residue.

**Proof.** By (24) and (31),
\[
\begin{split}
d\bigl(E_{\{w\}}^\bullet L_w
       -E_{\{z\}}^\bullet L_z\bigr)
&=(-1)^{e_\bullet}
 \left(\phi_\bullet\tau_z-E_\varnothing^\bullet\tau_{zw}
                      +E_\varnothing^\bullet\tau_{zw}\right)\\
&=(-1)^{e_\bullet}\phi_\bullet\tau_z.
\end{split}                                                     \tag{37}
\]
The common two-vacuum term cancels because both proper-restriction
identities use the same map on the actual union-source kernel.
The other insertion vanishes as a complete kernel map. The two
one-vacuum vertices retain their different native labels: no equality
between them, and no relabelling or fusion identification, is used.
Since \(\phi_\bullet j_z=0\), equation (32) gives
\[
\phi_\bullet V_B
 =\phi_\bullet\tau_z-\phi_\bullet d_GA_z.
\]
Combine this with (34) and (37). The result is exactly (36), including
the minus signs for \(e_\varepsilon=-1\). Every term is evaluated on
the supplied action edge or its supplied recipient comparison. No
primitive is chosen merely from an equality of endpoint differentials.
\(\square\)

The calculation does not require an extension of the functional to the
empty-retained vertex. Nor does it fill every cycle in
\(\mathsf G'_z\). The particular vertices \(\tau_z,\tau_w,\tau_{zw}\)
and edges (31) come from the same action and genuine-vacuum pointing.
An arbitrary normal cochain need not occur in such a diagram.

## The original pointed edge and recipient transport

For completeness, retain the distinction between the common recipient
pointing and an independently fixed pointing of \(D_r\).
Let \(D_r^\circ\) denote the common detector image and let
\[
v_r=(0,-\eta_r),\qquad d_Ev_r=D_r-D_r^\circ,
\qquad |v_r|=-3.                                   \tag{38}
\]
This is the original scalar vertex comparison. The whole proper cube
has its affine transport
\[
C_{T,D}^{\mathrm{fixed}}-C_{T,D}^{\circ}
   =dU_{T,D}+(\partial U)_{T,D},\qquad
U_{T,D}=(-1)^{|D|}B_{T,D}v_r.                       \tag{39}
\]
Here \(|B_{T,D}|=-|D|\), and \(dB=\partial B\); every lower-face
term in (39) is retained. In particular, the pointing component of
\(U_{T,D}\) is \(-B_{T,D}\eta_r\), not a choice made independently
on each edge.

Write \(\beta_z=-\iota(b_z)\) and
\(a_z=-\iota(\vartheta_z)\), so that
\[
da_z=\beta_z+j_z,\qquad
\tau_z^{\mathrm{fixed}}-\tau_z^\circ=\beta_zd_Ev_r,
\qquad A_z^{\mathrm{fixed}}-A_z^\circ=a_zd_Ev_r.     \tag{40}
\]
These are the actual recipient comparison faces; they give (32) with
\(D_r\), while the common pointed recipient \(V_B\) remains fixed.

For either functional, evaluating the two edge faces of (39) and
using (24), (34)--(35) yields
\[
Q_\bullet^{\mathrm{fixed}}-Q_\bullet^\circ
 =d\left(E_{\{w\}}^\bullet U_{S,\{w\}}
         -E_{\{z\}}^\bullet U_{S,\{z\}}
         +\phi_\bullet a_zv_r\right).             \tag{41}
\]
Indeed the common \(U_{S,\varnothing}\) cancels, the other retained
vertex has zero insertion, and the remaining term is
\((-1)^{e_\bullet}\phi_\bullet(\beta_zv_r-a_zd_Ev_r)\).
It equals \(d(\phi_\bullet a_zv_r)\), by (34), (40), and
\(\phi_\bullet j_z=0\). This verifies the entire transport also
for the degree-minus-one functional.
Thus (35) consumes the originally prescribed pointed edges and their
whole-cube correction. Equality of different scalar pointing
representatives has not been assumed.

## Comparing with the fixed three-block pointing

Write the common pointed recipient as
\(V_B=(\underline V_B,h_V)\). By (36), write
\[
Q_\ell=(q,h_q),\qquad
 dq=\ell_{B;p}\underline V_B,
\qquad q u-dh_q=\ell_{B;p}h_V.                      \tag{42}
\]
The scalar difference between the pointing in (6) and this common
recipient image is
\[
\delta=Ku-\omega-\ell_{B;p}h_V.                     \tag{43}
\]
It has degree \(-3\) and is closed: the differential of each of its
first two terms combines, by (5), to
\(\ell_{B;p}\underline V_Bu\), which is also the differential of
its last term. More explicitly, the common recipient has
\(dh_V=\underline V_Bu-j_z\ell_\nu\), and
\(\ell_{B;p}j_z=0\) removes precisely that extra pointing term.
This statement includes all parameter and old-collision faces of these
originally fixed data.

The required scalar comparison can be constructed on the actual unit
complex. On each smooth old affine order chart, the Spencer resolution
computes
\[
R\operatorname{Hom}_{\mathcal D_R}(R,R)
 \simeq \Omega_R^\bullet,
\]
with nonnegative cohomological degrees. Finite ordered-chart descent
uses nonnegative Čech degrees. For an old collision or a pointed actor
arrow, the cross-arrow scalar coefficient is
\(R\operatorname{Hom}(f^!J_{\mathrm{source}},J_{\mathrm{target}})\).
Its actual coherent unit comparison identifies it with the same type
of scalar endomorphism complex. The full naturality bar construction
and action-parameter cochains again have nonnegative degrees.
Products and totalizations of these nonnegative models have no negative
terms. The fibre over a prescribed boundary diagram has the same
property, since it is a shifted cone of a map of nonnegative models.

Here the scalar complex is the homotopy end of the entire marked
parameter and naturality diagram, rather than a complex chosen
separately at each action. Consequently that full scalar complex, with
any already prescribed boundary, has a specified equivalence to a
nonnegative model \(S_{\ge0}\). Choose the inverse-comparison data in
that full diagram, and write them in cochain representatives as
\[
p_S:S\to S_{\ge0},\qquad i_S:S_{\ge0}\to S,\qquad
 dH+Hd=1-i_Sp_S.                                    \tag{44}
\]
These are the comparison maps of the scalar unit resolutions and their
homotopy inverse, not a contraction of an actor-valued mapping complex.
The homotopy inverse data of this equivalence are taken with their
coherent naturality and prescribed boundary.
Because \(p_S\delta=0\) in degree \(-3\), the explicit comparison
\[
\eta=H\delta\in S^{-4}\qquad\text{satisfies}\qquad d\eta=\delta.
                                                               \tag{45}
\]
Thus the scalar filling is obtained from the displayed unit model; no
negative-Ext condition on \(F\), \(M\), or an arbitrary recipient is
assumed.

Define
\[
\widetilde Q_\ell=Q_\ell+(0,-\eta)=(q,h_q-\eta).
                                                               \tag{46}
\]
The pointing-fibre sign in (3), (43), and (45) gives
\[
d_{\mathcal E}\widetilde Q_\ell
 =\bigl(\ell_{B;p}\underline V_B,Ku-\omega\bigr)
 =R^{\mathrm{pt}}.                                  \tag{47}
\]
Finally put
\[
\boxed{\qquad
\mathcal F_{A|B|C}=(K,0)-\widetilde Q_\ell
                =(K-q,-h_q+\eta).
\qquad}                                                       \tag{48}
\]
Its differential is the original \(\Omega^{\mathrm{pt}}\) in (4).
For example, its scalar differential is
\[
(K-q)u-d(-h_q+\eta)
 =Ku-\ell_{B;p}h_V-\delta=\omega,
\]
so no pointing path in the original boundary has been replaced.

All constructions were made on the actual restricted source, the
specified proper action edges, and the full scalar comparison diagram.
They retain all higher parameter and allowed old-collision faces.
The extra vacuum labels remain distinguished singleton fibres; no
vacuum-fusion comparison is asserted. The old root and marks remain
part of the data. Formula (48) fills this fixed three-block associativity
boundary. It does not by itself construct changes of root, a compatible
family for all longer ordered words, mixed arbitrary actor attachments,
or a full coalgebra recognition homotopy.
