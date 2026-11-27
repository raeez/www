# Radial comb sewings of arbitrary finite length

Fix a compact charge interval \(J\Subset(1,\infty)\). For \(c\in J\),
put
\[
 h_p=(c-1)/24+p^2,\qquad E_p=L_0^{(p)},\qquad
 \|u\|_{H_p[t]}=\|e^{tE_p}u\|,\qquad
 d\nu(p)=m_b(p)\,dp .
\tag{FC.1}
\]
The measure has at most exponential growth in \(p\). Retain the
all-\(c>1\) hypotheses of the normalized positive Ward vertex and
the every-fibre two-radius tensor estimate, including the boundary
hypothesis \(H\). The binary normalization is
\[
 \mu_{p,q}(z)(u,v)(e)
   =2^{1/4}\sqrt{C_0(p,q,e)}\,I_e^{q,p}(v,z)u.
\tag{FC.2}
\]
The stationary input is written first. Coordinate logarithms are fixed.
All inner products used for estimates are the positive Hilbert forms;
the actual internal contractions are the inverse-Shapovalov
contractions of the corresponding complex-bilinear Ward forms.

## The uniform two-input kernel

For independently arbitrary \(\alpha,\beta>0\), the two-radius
estimate supplies a finite \(\theta\) and constants \(C,\epsilon,\gamma>0\)
such that
\[
 \begin{split}
 V_{p,q;e}^{\alpha,\beta}
 &=e^{-\beta E_e}\mu_{p,q}(1)(e^{-\alpha E_p}\otimes1),\\
 \|V_{p,q;e}^{\alpha,\beta}\|_{
    \mathrm{HS}(H_p\widehat\otimes_2H_q[\theta],H_e)}^2
 &\le C e^{-\gamma(p^2+e^2)-\epsilon q^2}.
 \end{split}
\tag{FC.3}
\]
The constants can be chosen uniformly on compact sets of
\(c,\alpha,\beta\) within their admitted ranges. The full
middle-input basis sum is included. Finite-level cutoffs converge
normally in this Hilbert--Schmidt norm. Taking slightly weaker
endpoint damping and a slightly weaker middle-input exponent
gives strict energy margins for all three level tails. The
same estimates are holomorphic in the endpoint dilation
parameters and give Gaussian spectral tails.

This is precisely the every-fibre statement with the binary
factor \(2^{1/4}\). It is an estimate of the canonical family
at every positive label, not point evaluation on an arbitrary
spectral \(L^2\) space.

**Lemma FC.1.** Write \(\ell_z=-\log|z|\). Given
\[
 r>\ell_z,\qquad s<\ell_z,
\tag{FC.4}
\]
there is a finite \(t\) such that the energy-conjugated kernel
\[
 K_z(p,q;e)
   =e^{sE_e}\mu_{p,q}(z)(e^{-rE_p}\otimes e^{-tE_q})
\tag{FC.5}
\]
is Hilbert--Schmidt, with
\[
 \|K_z(p,q;e)\|_{\mathrm{HS}}^2
       \le C e^{-\gamma_0(p^2+q^2+e^2)}
\tag{FC.6}
\]
for some \(\gamma_0>0\). On every compact logarithmic
coordinate set where (FC.4) has strict uniform margins,
one may choose \(t,C,\gamma_0\) uniformly. All level
cutoffs converge normally, as do spectral cutoffs against
any subset of the three canonical measures. The kernel
is holomorphic in Hilbert--Schmidt norm.

**Proof.** Choose
\[
 0<\alpha<r-\ell_z,\qquad 0<\beta<\ell_z-s,
 \qquad t>\ell_z+\theta .
\tag{FC.7}
\]
Use homogeneity in its actual finite coefficients:
\[
 \mu_{p,q}(z)(u,v)
       =z^{E_e}\mu_{p,q}(1)(z^{-E_p}u,z^{-E_q}v).
\tag{FC.8}
\]
After the Hilbert identifications, (FC.5) is (FC.3)
composed with
\[
 e^{(s+\beta+\log z)E_e},\qquad
 e^{(\alpha-\log z-r)E_p},\qquad
 e^{(-\log z+\theta-t)E_q}.
\tag{FC.9}
\]
Each has strictly negative real exponent. Its norm is
at most one. The ideal property of the Hilbert--Schmidt
norm gives (FC.6) from (FC.3), with the smallest of its
positive Gaussian constants. The strict residual
exponents in (FC.9), together with the normal estimates
in (FC.3), give geometric level tails. The Gaussian
bound gives integrable spectral tails, since
\(\int e^{-a p^2}\,d\nu(p)<\infty\) for every \(a>0\).

Choose the margins on a slightly larger compact coordinate
set. The finite coefficients are holomorphic powers of
\(z\), and their normally convergent Hilbert--Schmidt
sum proves the asserted holomorphy. The coefficient
identity (FC.8) identifies the resulting completed
kernel with the actual normalized vertex. \(\square\)

The same proof permits different finite source exponents
larger than the displayed ones. In particular the
constants are uniform in all positive values of \(p,q,e\)
after their full-energy conjugations.

## Packet composition with retained multiplicity

For a separable Hilbert space \(M\), set
\[
 \mathcal H_M[r]
 =L^2(d\nu(p);M\widehat\otimes_2H_p[r]).
\tag{FC.10}
\]
Its \(p\)-variable is the current output momentum. If it
is used in another positive vertex, it becomes a
retained multiplicity variable.

**Lemma FC.2.** Under the conditions of Lemma FC.1,
the actual outer operation with fixed positive moving
label \(q\) is bounded
\[
 \mathcal A_q(z):
 \mathcal H_M[r]\widehat\otimes_2H_q[t]
 \longrightarrow
 L^2(d\nu(p)d\nu(e);M\widehat\otimes_2H_e[s]).
\tag{FC.11}
\]
Its value on decomposable inputs is
\[
 [\mathcal A_q(z)(F,v)](p,e)
                     =\mu_{p,q}(z)(F(p),v)(e).
\tag{FC.12}
\]
It is also bounded if \(q\) is a second incoming
spectral variable with a separable Hilbert multiplicity:
\[
 \begin{split}
 \mathcal A(z):&
 \mathcal H_M[r]\widehat\otimes_2\mathcal H_N[t]\\
 &\longrightarrow
 L^2(d\nu(p)d\nu(q)d\nu(e);
                  M\widehat\otimes_2N\widehat\otimes_2H_e[s]).
 \end{split}
\tag{FC.13}
\]
Both incoming labels are retained in (FC.13).
A fixed-label incoming factor is obtained by omitting
its spectral integral. The estimates hold on the full
Hilbert tensor, with no decomposability assumption.

**Proof.** In the unweighted Hilbert identifications,
a source in (FC.13) is a measurable field
\(F(p,q)\in M\widehat\otimes_2N
                  \widehat\otimes_2H_p\widehat\otimes_2H_q\).
Apply \(1_{M\otimes N}\otimes K_z(p,q;e)\). By (FC.6),
\[
 \begin{split}
 &\int\!\!\int\!\!\int
  \|(1\otimes K_z(p,q;e))F(p,q)\|^2
                    \,d\nu(e)d\nu(p)d\nu(q)\\
 &\hspace{15mm}\le
 C\!\left(\int e^{-\gamma_0e^2}\,d\nu(e)\right)
                      \int\!\!\int\|F(p,q)\|^2\,d\nu(p)d\nu(q).
 \end{split}
\tag{FC.14}
\]
Only an operator norm bounded by the full
Hilbert--Schmidt norm of \(K_z\) has been used.
In particular no Hilbert--Schmidt norm of a
multiplicity identity occurs. The measurable
direct-integral operator is defined on equivalence
classes; no arbitrary spectral class is evaluated
at a point. Omitting the \(q\)-integral proves
(FC.11), uniformly in its fixed label.

Finite-level and compact-spectrum fields are dense.
The normal kernel cutoffs in Lemma FC.1 identify
(FC.12) and its two-packet version with the actual
inverse-Gram contractions there and then everywhere
by continuity. The compact-uniform estimates give
local operator holomorphy. \(\square\)

For normal convergence on Hilbert--Schmidt packet
inputs, a further useful fact is the following.
Suppose \(A:X\to\mathcal H_M[r]\) is
Hilbert--Schmidt, and its fibre kernels after energy
identification are \(A(\mathbf k,p)\). Then the pullback
of (FC.5) is a full Hilbert tensor on \(X\) and the
moving input. At almost every retained label,
\[
 \|K_z(p,q;e)(A(\mathbf k,p)\otimes1)\|_{\mathrm{HS}}
 \le \|K_z(p,q;e)\|_{\mathrm{HS}}\,
                         \|A(\mathbf k,p)\|_{\mathrm{op}}
 \le \|K_z(p,q;e)\|_{\mathrm{HS}}\,
                         \|A(\mathbf k,p)\|_{\mathrm{HS}}.
\tag{FC.15}
\]
Thus the fixed-moving-label version is
Hilbert--Schmidt on the full new source, without
assigning a Hilbert--Schmidt norm to the identity
on that moving source. For two Hilbert--Schmidt
packets the corresponding bound is the product
of their fibre operator norms and the kernel
Hilbert--Schmidt norm. Integrating their squares
uses Tonelli and the two packet norm identities.

## The entire finite-word source

Fix \(d\ge2\) positive external labels
\(\mathbf p=(p_1,\ldots,p_d)\). Put
\[
 \begin{split}
 \mathscr E_{\mathbf p}
 &=\left\{u=(u_{n_1,\ldots,n_d}):
        Q_a(u)^2
        =\sum_{\mathbf n}
          e^{2a\sum_i(h_{p_i}+n_i)}
                         \|u_{\mathbf n}\|^2<\infty
                       \quad\hbox{for every }a\in\mathbb N\right\},\\
 E_{\mathbf p}
 &=\mathscr E_{p_1}\widehat\otimes_\pi\cdots
                                 \widehat\otimes_\pi\mathscr E_{p_d}.
 \end{split}
\tag{FC.16}
\]
These are canonically the same complete Fréchet space,
on all coefficient arrays. Indeed the projective
seminorm from the \(a\)-norms dominates the Hilbert
tensor norm \(Q_a\). Conversely, expand a finite array
in orthonormal level bases of its factors. Cauchy--Schwarz
gives, for every \(\delta>0\),
\[
 \pi_a(u)
 \le
 \left(\prod_{i=1}^d
        e^{-2\delta h_{p_i}}
          \sum_{n\ge0}\dim(H_{p_i})_n\,e^{-2\delta n}\right)^{1/2}
              Q_{a+\delta}(u).
\tag{FC.17}
\]
The factor is finite because the level dimensions
have subexponential growth. This also proves absolute
convergence of the elementary-basis expansion in
every projective seminorm for an arbitrary array in
the first line of (FC.16). Completeness and joint
finite-level approximation give the canonical
topological equality. Thus the source includes
every entangled entire-energy array.

## The arbitrary finite radial comb

Place the inputs at
\[
 a_1=0,\qquad a_j=z_{j-1}\quad(2\le j\le d),
 \qquad 0<|z_1|<\cdots<|z_{d-1}|.
\tag{FC.18}
\]
For \(2\le j\le d\), write \(k_j\) for the momentum
created after the first \(j\) inputs have been sewn;
\(k_d=e\) is the final momentum. The output space is
\[
 \mathcal Z_d[s]
 =L^2\bigl(d\nu(k_2)\cdots d\nu(k_{d-1})d\nu(e);
                                                   H_e[s]\bigr).
\tag{FC.19}
\]
When \(d=2\), the product of retained-label measures
is empty. All \(d-2\) nonfinal internal labels in
(FC.19) remain resolved multiplicities.

On finite coefficients define
\[
 \begin{split}
 C_2(z_1)&=\mu_{p_1,p_2}(z_1),\\
 C_j(z_1,\ldots,z_{j-1})
   &=\mu_{k_{j-1},p_j}(z_{j-1})
                         (C_{j-1}\otimes1),\qquad j\ge3.
 \end{split}
\tag{FC.20}
\]
The contractions are the actual inverse-Gram
contractions at the \(j-2\) internal seams.

**Theorem FC.3.** For every finite \(d\ge2\), every
real \(s\), and every compact logarithmic coordinate
set
\[
 K\Subset
 D_{d,s}=
 \{0<|z_1|<\cdots<|z_{d-1}|,\quad
                         s<-\log|z_{d-1}|\},
\tag{FC.21}
\]
there is a finite \(t_K\) such that the actual comb
extends as a holomorphic Hilbert--Schmidt family
\[
 C_d(z):
       \widehat\bigotimes_{i=1}^d{}_{\!2}H_{p_i}[t_K]
                                      \longrightarrow\mathcal Z_d[s],
\tag{FC.22}
\]
with a compact-uniform bound independent of all
positive external labels. The constants can also
be chosen locally uniformly in \(c>1\).
Consequently it is a continuous holomorphic family
on the complete source (FC.16).

All internal and final spectra and all descendant
levels are uncut. Input-level, internal-level,
output-level, and spectral cutoff contractions
converge normally on every smaller compact
coordinate set, in the Hilbert--Schmidt norm
from a common finite source stage. Their limit
is (FC.20). The mark is exactly
\[
 2^{(d-1)/4}
     \sqrt{\prod_{\text{the }d-1\text{ vertices}}C_0}.
\tag{FC.23}
\]
For algebraic external states, every fixed
positive tuple of retained and final momenta
has the same actual inverse-Gram coefficients;
the internal matrix expansions converge
absolutely in the indicated energy spaces.

**Proof.** The case \(d=2\) follows from Lemma FC.1:
integrate the squared full tensor norm in its
output label. The resulting map is Hilbert--Schmidt
on the full two-input Hilbert tensor. Its tail
and holomorphy assertions are those of that lemma.

Assume the result through \(j-1\) inputs. Locally
on a small compact coordinate neighbourhood,
choose an intermediate exponent
\[
 -\log|z_{j-1}|<r<-\log|z_{j-2}|.
\tag{FC.24}
\]
The radial inequalities make this possible.
The induction hypothesis gives \(C_{j-1}\)
as a Hilbert--Schmidt packet with current
output exponent \(r\) and all its former
internal labels retained. Lemma FC.1, with
\(r\) as stationary-input exponent and \(s\)
as desired final exponent, supplies one
finite moving-input exponent \(t_j\).
Lemma FC.2 composes the packet with that
actual outer vertex. Formula (FC.15), its
Gaussian output integral, and the packet
fibre-norm identity show that this composition
is Hilbert--Schmidt on the full \(j\)-input
tensor. There is no restriction to sums of
decomposable original inputs.

All source exponents are finite. Increase
them to one common value. A finite cover of
the compact \(K\) gives finitely many choices
of (FC.24), of the vertex margins, and of
these source exponents. Taking their maximum
gives one \(t_K\). Their constants were uniform
in all external labels after full-energy
conjugation, so the resulting constant is
uniform as well. Compact charge uniformity
is inherited in the same finite construction.

We detail the limiting contraction. Choose
\(r_+\) slightly larger than \(r\), still below
the upper endpoint in (FC.24). The incoming
packet is constructed in exponent \(r_+\);
its internal seam cutoff therefore has a
geometric tail when read at exponent \(r\).
Choose a final exponent \(s_+>s\), still
below \(-\log|z_{j-1}|\). The same construction
with \(s_+\) gives a geometric output-level
tail in exponent \(s\). Increase the original
input exponents by a finite positive margin
to give geometric input tails.

For every older seam, the induction already
gives a normal tail; composing it with the
bounded outer operator preserves convergence.
For the new seam, the incoming packet tail
just described is composed with that same
bounded operator. For a new outer-vertex
level cutoff, use (FC.15) with the kernel
tail from Lemma FC.1; on compact label sets
it converges uniformly, while the Gaussian
bound and the integrable packet fibre-square
give dominated convergence. The spectral
tail in the new output is bounded by the
Gaussian in (FC.6). A tail in the new retained
label is controlled either by that Gaussian
or by the incoming packet tail. Older
retained-label tails are handled by induction.
All comparisons are uniform on a slightly
larger compact coordinate set. Since the
number of seams is finite, the telescoping
difference between two full cutoff contractions
is a finite sum of these errors. Thus arbitrary
joint rectangular cutoffs have the same
normal Hilbert--Schmidt limit.

The equality of the limit with (FC.20) is
an actual coefficient identification.
At fixed positive labels the damped fibre
operators in Lemma FC.1 are Hilbert tensors.
The incoming packet's finite-coefficient
expansion belongs to its stated energy
space. Cauchy--Schwarz therefore makes
each internal matrix contraction absolute.
For this assertion one may replace every
finite-level matrix by its entrywise absolute
value: its Hilbert--Schmidt norm is unchanged,
and its operator norm is at most that norm.
The same successive Cauchy--Schwarz estimates
therefore bound the series of absolute
values. Induction over the finite tree of
contractions gives absolute summation over
all its internal matrix indices.
The finite coefficient contraction has
exactly the inverse-Shapovalov entries of
the normalized Ward forms. The normal
cutoff convergence identifies those entries
with the limit just constructed.

One can also see fixed-label convergence
directly throughout this induction. The
initial pair kernel and every later
energy-conjugated fibre kernel obey
(FC.6) at every positive tuple.
Taking the Hilbert-tensor contraction
at each fixed tuple gives the same
finite product bound. Its strict energy
margins provide the level tails before
any spectral integration is taken.
No point evaluation of an arbitrary
completed spectral input is involved.

Finite-level, bounded-spectrum contractions
are holomorphic on the selected logarithmic
branches. Their local uniform convergence
in (FC.22) proves holomorphy of the limit.
Density identifies the same operator for
different intermediate exponents, cutoff
choices, or finite source stages.

Finally each of the \(j-1\) actual binary
vertices contributes exactly \(2^{1/4}\).
Their positive square-root factors multiply,
and no retained measure is changed. This
proves (FC.23) and completes the induction.
\(\square\)

At normalized last position \(z_{d-1}=1\),
every strictly negative final exponent
\(s<0\) is admitted for each fixed finite
word, with a compact-dependent finite
positive-input stage. The theorem does
not give a bound at the endpoint \(s=0\),
a source stage uniform in the word length,
or a finite source stage uniform up to
a collision boundary. It concerns the
actual radial comb series; convergence
of a different tree's raw expansion
requires its own sewing domain.
