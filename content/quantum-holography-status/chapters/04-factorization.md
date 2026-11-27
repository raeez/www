# Factorization and collision geometry

How can the product of two fields at nearby points serve as an input to a third field? Place two Heisenberg currents at \(z,w\) on the complex plane. Prepare the vacuum and project the product back onto the vacuum. At level \(\kappa\) its coefficient is \(\kappa/(z-w)^2\). Hold \(w\) fixed. Integrating the first insertion with weight \(f\), holomorphic on and inside a small counterclockwise circle about \(w\), gives
\[
 \frac{1}{2\pi i}\oint_{w} f(z)\frac{\kappa}{(z-w)^2}\,dz
 =\kappa f'(w).
\]
The weights \(1\) and \(1+(z-w)\) agree at the collision. They give \(0\) and \(\kappa\), respectively. At nonzero level the residue distinguishes the first derivatives of the two weights in the direction normal to the collision diagonal. [The free-current vacuum coefficient](03-local-fields.md#heisenberg-current)

Now take three fields. Bring the first two together and keep the third, the spectator, at \(y\). Write their positions as \((w+t,w,y)\). We can shrink the contour about \(w\) without enclosing \(y\) provided \(w\ne y\) and \(t\) is sufficiently small. Extract a coefficient of the first pair by taking a weighted residue in \(t\). For the two currents the weight \(t\), for instance, gives \(\kappa\) times the vacuum field at \(w\). The coefficient selected in this way and the spectator still occupy two positions, \(w\) and \(y\). In the original three coordinates this is the partial collision \((w,w,y)\).

Which separations may vanish during that first operation? The product \((z_1-z_3)(z_2-z_3)\) must stay nonzero. On \((w,w,y)\) it becomes \((w-y)^2\). Thus one open set contains both the approaching triple and the partially collided pair, and it excludes the final collision with the spectator. Bringing the last two fields together first requires the open set where the *first* field stays apart.

The spectator can detect a coefficient of the pair product that its vacuum projection misses. Take three abelian Gaussian Wilson rays at level \(1\), with charges \(q_1=1,\ q_2=-1,\ q_3=1\). Prepare oscillator-free incoming states and project onto the oscillator-free state of total charge \(1\). Use the Cauchy propagator, outgoing mutual subtraction and parallel-copy framing, and normalise the outgoing state to have coefficient one. In the separated chamber each pair contributes \((z_i-z_j)^{q_iq_j}\). Put \(t=z_1-z_2\) and \(v=z_2-z_3\). The vacuum coefficient of the neutral first pair alone is \(1/t\). With the third ray present the three pair factors give
\[
 F(t,v)=\frac1t\,\frac{v+t}{v}
       =\frac1t+\frac1v .
\]
{#eq-ch04-neutral-pair-with-spectator}
The unweighted residue in \(t\) is \(1\) in both preparations. Now weight by \(1/t\) to extract the constant term of the pair expansion. The vacuum reading of the isolated pair gives zero. In the three-ray coefficient the residue is \(1/v\), whose residue at \(v=0\) is \(1\).

Which field survived the first fusion? The current contour weighted by \((z-z_2)^n\), \(n>0\), reads \(t^n\) on the charge at \(z_1\) and zero on the charge at \(z_2\). In the Fock coordinates \(p_n=J_{-n}\), the positive mode \(J_n\) acts by \(n\partial_{p_n}\) at level one. Thus the neutral pair state \(\Psi\) satisfies \(n\partial_{p_n}\Psi=t^n\Psi\) for all \(n>0\), with vacuum coefficient \(1/t\). Solving in each oscillator weight gives
\[
 \Psi(t)=\frac1t\exp\!\left(\sum_{n>0}\frac{t^n p_n}{n}\right)|0\rangle
       =\frac1t|0\rangle+J_{-1}|0\rangle+O(t).
\]
The constant term is the current. Its simple pole with the remaining unit charge gives precisely \(1/v\). Factorisation specifies the independent inputs while their blocks stay apart and how to restrict a product when points inside a block coincide. [Charge read by a current contour](03-local-fields.md#ch03-charged-current-contour) · [The Gaussian ray coefficient](#ch04-gaussian-collision)

## Configurations and partial diagonals {#configuration-spaces}

**Definition (configuration space).** Let \(X\) be a smooth algebraic curve over a characteristic-zero field \(k\). For a finite nonempty set \(I\), the product \(X^I\) records an \(I\)-labelled family of points. Its open configuration space is
\[
U_I=\{(x_i)\in X^I:x_i\ne x_j\text{ whenever }i\ne j\}.
\tag{4.1}
\]
Write \(j_I:U_I\hookrightarrow X^I\) for its inclusion. The **small diagonal** is the map
\[
\Delta_I:X\longrightarrow X^I,
\qquad x\longmapsto(x)_{i\in I}.
\]
Its image is the locus where all the labelled points coincide. For two labels \(i,j\), the partial diagonal \(\Delta_{ij}\) imposes only \(x_i=x_j\).

In the three-field calculation \(U_{\{1,2,3\}}\) is too small for the first residue. It contains the contour but omits the locus \(z_1=z_2\) that supports its residue. For the order \(12|3\) we need only \(z_1\ne z_3\) and \(z_2\ne z_3\). For any chosen groups of fields, call \(J\) the set of labels and \(I\) the set of groups. Assigning each label to its group gives a surjection \(\pi:J\twoheadrightarrow I\) with nonempty fibres \(J_i=\pi^{-1}(i)\). The required open is
\[
U_\pi=\{(x_j)\in X^J:
x_j\ne x_{j'}\text{ if }\pi(j)\ne\pi(j')\}.
\tag{4.2}
\]
No inequality is imposed within any one block. To put all the labels of a block at a single position, use the diagonal map
\[
\Delta_\pi:X^I\longrightarrow X^J,
\qquad(x_i)\longmapsto(x_{\pi(j)})
\]
It repeats the position of each block at all its labels. Its image is the locus where the points in every block coincide.

For \(12|3\) the diagonal sends \((x,y)\) to \((x,x,y)\). The three configurations \((0,1,2)\), \((0,0,2)\) and \((0,0,0)\) distinguish the conditions on a coordinate line. The first belongs only to the block-separation open, the second belongs both to the open and to the image of this diagonal, and the third belongs only to the image. Pulling the open back to the two block positions therefore gives precisely \(x\ne y\). The same test on a pair of distinct blocks proves \(\Delta_\pi^{-1}(U_\pi)=U_I\) for every \(\pi\).

## A chiral operation is a map with a collision target {#chiral-operation}

Before colliding two fields, one can multiply them by \(1/(z-w)\). At separated positions this is an ordinary function. At coincidence the test by a residue still makes sense, even though the multiplier has a pole. To allow such inputs, take right \(\mathcal D_X\)-modules \(L_i\) for the fields and \(M\) for their output. In the external tensor product \(\boxtimes_{i\in I}L_i\), the \(i\)-th factor depends on the \(i\)-th position. Restrict this module to \(U_I\) and take its direct image back to \(X^I\). The resulting input module is
\[
j_{I*}j_I^*\Bigl(\boxtimes_{i\in I}L_i\Bigr).
\]
On a coordinate chart for two points this adjoins \((z-w)^{-1}\). A section has a finite pole order, which may vary from one section to the next. The density convention identifies the module in which its residue takes values. [Right differential modules for fields](03-local-fields.md#differential-modules)

**Definition (chiral operation).** The direct image \(\Delta_{I*}M\) is a differential module on \(X^I\) supported on the small diagonal. It includes derivatives in directions normal to that diagonal. A **chiral \(I\)-operation** is a differential-module map
\[
\mu:
j_{I*}j_I^*\Bigl(\boxtimes_{i\in I}L_i\Bigr)
\longrightarrow\Delta_{I*}M.
\tag{4.3}
\]
Thus its space is
\[
P_I^{\mathrm{ch}}((L_i);M)
=\operatorname{Hom}_{\mathcal D_{X^I}}
\left(j_{I*}j_I^*\boxtimes_iL_i,\Delta_{I*}M\right).
\tag{4.4}
\]
Both sides of the Hom are modules on \(X^I\). Restrict (4.3) to the distinct open for \(|I|>1\) and its target becomes zero. A nonzero operation can therefore only be seen by extending the inputs to the localization and retaining the supported output. This is the operation space of Beilinson–Drinfeld, *Chiral Algebras*, §3.1.1.

The simplest model is a residue. With a local normal coordinate \(t=z-w\), the functional associated to a pole of order \(r\) acts on a test series \(f(t)\) by
\[
\operatorname{Res}_{t=0}\frac{f(t)}{t^r}\,dt
=\frac{f^{(r-1)}(0)}{(r-1)!}.
\tag{4.5}
\]
In a density frame, the unit operation on two one-forms takes a meromorphic two-form to its principal part modulo forms regular along \(t=0\). The class of \(t^{-1}dz\,dw\) gives the diagonal generator \(dw\). The class of \(t^{-2}dz\,dw\) pairs with \(f(z)\) to give \(f'(w)\,dw\), as in the current calculation. For example, the principal part \(A(w)t^{-2}+B(w)t^{-1}\), in this frame, returns \(\bigl(A(w)f'(w)+B(w)f(w)\bigr)\,dw\). Taking \(f=1\) reads \(B(w)\), and taking \(f=z-w\) reads \(A(w)\). The supported output retains the two coefficients separately.

Keep the spectator at \(y\) and take the first residue at \(z_1=z_2=x\). In the residue pairing for densities, write \(s=z_1-z_2\) and \(v=z_2-z_3\). The simple pole \(1/(sv)\) has residue \(1/v\) in \(s\). The spectator multiplier survives at \((x,x,y)\) as \(1/(x-y)\). The result therefore lives on the partial diagonal, still localized in the *remaining* separation. Write \(\delta_{12}(x,y)=(x,x,y)\), let \(j:U_2\hookrightarrow X^2\) omit \(x=y\), and call the output module of the inner operation \(N\). For fields in \(L_1,L_2,L_3\), the composite on \(X^3\) is
\[
\begin{aligned}
 &j_{3*}j_3^*(L_1\boxtimes L_2\boxtimes L_3)\\
 &\quad\longrightarrow\delta_{12*}j_*j^*(N\boxtimes L_3)
 \longrightarrow\Delta_{3*}M .
\end{aligned}
\]
Here \(j_3=j_{\{1,2,3\}}\) and \(\Delta_3=\Delta_{\{1,2,3\}}\). On \(U_{12|3}\) the first arrow can apply the inner operation while the spectator stays apart. Its output is supported on \(\delta_{12}\), with coefficients in \(j_*j^*(N\boxtimes L_3)\). The second arrow applies the outer binary operation to those coefficients and pushes its result forward along \(\delta_{12}\). For \(1|23\) the middle module lies on a different partial diagonal. Both composites are elements of the ternary space (4.4). Substitution of specified operations along successive partitions is associative. Asking whether a *particular* binary operation gives equal elements of (4.4) in the two channels imposes another condition. [Beilinson–Drinfeld, *Chiral Algebras*, §3.1.2](https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf#page=2)

## The Lie convention and the full operator product {#lie-and-operator-product}

**Definition (chiral algebra).** In the classical Beilinson–Drinfeld terminology, a nonunital **chiral algebra** is a right differential module \(A\) with a binary operation
\[
\mu\in P_2^{\mathrm{ch}}(A,A;A)
\]
satisfying skew-symmetry and the Jacobi identity in these operation spaces. It is a Lie algebra object for the chiral operations. A unit is a differential-module map \(\omega_X\to A\) whose operation with \(A\) is the canonical residue operation; see *Chiral Algebras*, §§3.3.1–3.3.3.

The ordinary Lie bracket of modes can be read from just the singular terms of a product. The geometric chiral bracket has a larger domain. Multiply a regular coefficient \(c_q(w)t^q\), \(q\ge0\), by \(t^{-q-1}\) and take a residue in \(t=z-w\). This recovers \(c_q(w)\), since no other power contributes. The chiral operation accepts precisely such Laurent multipliers. After converting from right to left differential modules and taking the punctured formal neighbourhood of the diagonal, it determines an operator-product expansion with its regular as well as singular coefficients. In local coordinates this is a map of the form
\[
a\boxtimes b\longmapsto
\sum_{n\in\mathbb Z}c_n(w)(z-w)^n,
\tag{4.6}
\]
with a finite negative tail for fixed inputs. For vertex fields in a translation coordinate, \(c_q\) is the field coefficient \(a_{(-q-1)}b\). In particular \(c_0=a_{(-1)}b\). Its iterated normal products on three copies of the free current have difference \(\kappa T^2j\), where \(j\) is the current state and \(T\) is translation. Selecting this single coefficient can lose associativity. [The current associator](03-local-fields.md#heisenberg-current)

What happens to the current associator when we put all the coefficients of (4.6) back together? For the order \(1,2,3\), the two familiar bracketings bring \(1,2\) or \(2,3\) together first. On the labelled curve \(1,3\) may also collide while \(2\) stays apart. Each choice of pair gives a region in which the product can be expanded in two stages. A common three-field product must restrict to the prescribed iterated expansion in all three regions.

Beilinson–Drinfeld's Theorem 3.5.10 identifies chiral Lie brackets with commutative and associative *full operator products*. Commutativity exchanges the point-labelled inputs. For associativity, the three iterated expansions form a tuple. In the exact sequence of the proof, the next map takes the signed sum of its collision residues. Exactness says that the tuple comes from a common expansion precisely when this sum vanishes. That vanishing is Jacobi. The individual residues can have different values, as the following rational function shows. [Beilinson–Drinfeld, *Chiral Algebras*, §3.5.10](https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch3.pdf#page=43)

### Three residues and the obstruction to a diagonal multiplication {#ch04-three-residues}

Translate the third point to the origin by writing \(u=z_1-z_3,\ v=z_2-z_3\). The rational function \(F=1/[u(u-v)]\) has a pole at \(z_1=z_2\) and at \(z_1=z_3\); it has no pole at a generic point of \(z_2=z_3\). For a collision in two stages, first extract the coefficient of the inverse separation of the colliding pair. Then extract the residue in the remaining separation. To collide 1 with 2 first, set \(s=u-v\) and expand near \(s=0\) with \(v\ne0\):
\[
 F=\frac{1}{s(v+s)}
   =\frac{1}{sv}-\frac{1}{v^2}+\frac{s}{v^3}-\cdots .
\]

The coefficient of \(s^{-1}\) is \(v^{-1}\), so the second residue is \(1\). Collide 2 with 3 first and the expansion \(F=u^{-2}(1-v/u)^{-1}\) is regular in \(v\), giving \(0\). Collide 1 with 3 first and \(F=-u^{-1}v^{-1}(1-u/v)^{-1}\) gives \(-1\). With these choices of normal coordinates the three oriented contributions add to \(1+0-1=0\). The collision of the outer pair \(1,3\) supplies the third term in the residue form of Jacobi. Could a different choice of binary chiral operation give the same ternary map in the first two orders? For such an equality to hold, it must hold on every localized input. The separation \(z_1-z_3\) is invertible at the first step in *both* orders. This gives a test for equality of the maps themselves.

**Proposition (ternary diagonal operations).** For ordinary right differential modules with the fully localized source and unshifted target of (4.3), the linear spans of composites through \(12|3\) and \(1|23\) have zero intersection. Consequently a strictly associative binary operation in these spaces has zero triple products.

*Proof.* Near the small diagonal choose a local étale coordinate and put \(s=z_1-z_2\), \(v=z_2-z_3\), \(h=z_1-z_3=s+v\). Fix a section \(e\) of the fully localized input. Let \(\alpha_{12}\) and \(\alpha_{23}\) be the first arrows in the two channels. The section \(\alpha_{12}(e)\) involves finitely many derivatives normal to \(\Delta_{12}\), so \(s^a\alpha_{12}(e)=0\) for some \(a\ge1\). Likewise \(v^b\alpha_{23}(e)=0\) for some \(b\ge1\). Why can we divide these intermediate sections by \(h\)? In the first channel \(v\) is invertible. If \(s^2y=0\), multiplying \(v^{-1}y-v^{-2}sy\) by \(h=v+s\) gives \(y\). For a section killed by \(s^a\), the same geometric sum ends after \(a\) terms. In the second channel \(s\) is invertible and \(v\) acts nilpotently on each section. The first arrows are linear over the functions with \(h\) inverted. Hence \(s^a\alpha_{12}(h^{-N}e)=h^{-N}s^a\alpha_{12}(e)=0\) for every \(N\ge0\), and likewise \(v^b\alpha_{23}(h^{-N}e)=0\).

Suppose that the two composites give the same map \(F\). Take \(N=a+b-1\) and expand \(e=(s+v)^Nh^{-N}e\). A summand with \(i\) factors of \(s\) contains \(N-i\) factors of \(v\). If \(i\ge a\), its image under \(\alpha_{12}\) vanishes. If \(i<a\), then \(N-i\ge b\) and its image under \(\alpha_{23}\) vanishes. Since either composite computes \(F\) on each summand, \(F(e)=0\). All divisions by \(h\) took place before the outer arrows, whose target is supported on \(h=0\). A finite sum of composites factors through the direct sum of their intermediate modules, where the same argument applies. The two bracketings of a strictly associative operation give an element of the intersection and therefore vanish. ∎

For a vacuum with left action equal to the normalized principal-part map, two successive simple-pole vacuum insertions return any given state. The proposition would make this operation zero. Thus a nonzero ordinary object on this carrier cannot have both that vacuum and a strictly associative binary operation. In a cochain complex the differential raises degree by one, and \(H^q\) is the space of degree-\(q\) cycles modulo boundaries. For complexes of right algebraic differential modules with quasi-coherent underlying modules, the conclusion is \(A\simeq0\) when the multiplication is homotopy associative on the fully localized source with unshifted small-diagonal target and the left action of a closed degree-zero vacuum is homotopic to principal parts. Indeed, external tensor over the field, localization and diagonal direct image pass the two identities to cohomology, where the ordinary obstruction applies. A homotopy of ternary operations has degree \(-1\). The three scalar residues just computed supply the terms of Jacobi. To obtain an associative algebra of configuration complexes one must specify its coefficient at each configuration and its multiplication there. [Associativity in the bar complex](05-bar-and-coherence.md#ch05-one-differential-encodes-all-associativity-homotopies)

## Factorization includes the collision extension {#factorization-algebra}

At two positions the residue uses a meromorphic input. To *restrict* a section to the diagonal, we first have to know which sections extend there. With regular functions on \(X^2\), \(f(z)g(w)\) extends and has value \(f(w)g(w)\) on the diagonal. On a coordinate chart \(1/(z-w)\) is also regular on the distinct open and has no such value. Both are legitimate separated inputs. The distinction is the sheaf \(\mathcal O_{X^2}\) of sections admitted across the collision. For general fields we must supply its analogue \(B_{\{1,2\}}\) and the identifications before and after the collision.

**Definition (factorization algebra).** In the classical algebraic formulation, a factorization algebra consists of quasi-coherent sheaves \(B_I\) on \(X^I\), together with two kinds of identifications. A surjection \(\pi:J\twoheadrightarrow I\) gives the diagonal identification
\[
\nu_\pi:\Delta_\pi^*B_J\xrightarrow{\sim}B_I
\tag{4.7}
\]
and the factorization identification on the block-separation open
\[
c_\pi:
\left.\boxtimes_{i\in I}B_{J_i}\right|_{U_\pi}
\xrightarrow{\sim}
\left.B_J\right|_{U_\pi}.
\tag{4.8}
\]
The diagonal identifications compose under successive collapses, the open identifications compose under refinements, and restricting a separated product along a diagonal within its blocks agrees with first restricting each block. The \(B_I\) have no nonzero local sections supported on the union of collision diagonals. A unit is a global section \(1\in B_{\{1\}}\) such that the separated product of \(1\) with each local section \(b\) extends to \(B_{\{1,2\}}\) and restricts to \(b\) on the diagonal. These are the ordinary sheaf conditions of *Chiral Algebras*, §§3.4.2–3.4.4.

Test the compatibility at the partial collision \((x,x,y)\), with \(x\ne y\). For functions the separated section is \(f(z_1,z_2)g(z_3)\). Form it on \(U_{12|3}\) and then set \(z_1=z_2=x\). Alternatively evaluate \(f\) at \((x,x)\) first and multiply by \(g(y)\). Both operations give \(f(x,x)g(y)\). The constant function \(1\) satisfies the unit condition.

For general sections the first route uses \(c_{12|3}\) and then \(\nu_{12|3}\). The second uses the diagonal map on the first block and the separated product of the two resulting blocks. Compatibility says these two restrictions agree. Which separated products can be restricted to the diagonal? If a local section of \(B_{\{1,2\}}\) vanishes on the distinct open, it is supported on the collision diagonal. The axiom excludes such a section unless it is zero. Thus restriction embeds \(B_{\{1,2\}}\) in its localization. On the open, (4.8) identifies the two-point sheaf with the external product of the two singleton sheaves. A separated section has a diagonal value by (4.7) precisely when it lies in the image of this embedding. For complexes, these restrictions and identifications must be made with derived pullbacks and coherent equivalences.

The tuples \((x,y)\), \((x,x,y)\) and \((y,x)\) correspond to the same finite subset when \(x\ne y\). The diagonal and relabelling identifications explain why one often describes the compatible family as a sheaf on the **Ran space** of \(X\). At the level of points, this is the set of finite nonempty subsets of \(X\); repeated labels specify the same subset. The maps \(\Delta_\pi\) express exactly those repetitions. One may use the compatible family \((B_I,\nu_\pi)\) without treating the Ran space as an ordinary finite-dimensional variety.

**Theorem: classical factorization and chiral algebras.** The above category of unital factorization algebras is equivalent to the category of unital Beilinson–Drinfeld chiral algebras on \(X\). The factorization sheaves acquire a canonical differential-module structure, and the corresponding right differential module is \(\omega_X\otimes B_{\{1\}}\).

Start with a factorization algebra. Use (4.8) to write a separated pair of densities in terms of the two-point sheaf \(B_{\{1,2\}}\). Apply the principal-part operation on the densities, carrying that sheaf as coefficient. On the supported output (4.7) identifies the diagonal coefficient with \(B_{\{1\}}\). This gives (4.3) on \(A=\omega_X\otimes B_{\{1\}}\).

Conversely, start with the chiral bracket. On two labels the Chevalley–Cousin complex has a term for the partition \(1|2\) in degree \(-2\) and a term for \(12\) in degree \(-1\). The differential between them is the bracket, with the shifts for these two degrees. On any finite label set a partition into \(r\) blocks contributes a term on its diagonal in degree \(-r\). The differential brackets a pair of blocks and leaves the others in place. Two successive mergers of three blocks give precisely the three signed terms of Jacobi. Mergers on disjoint pairs cancel in opposite orders. Thus the differential squares to zero. For a unital chiral algebra its cohomology on \(X^I\) is concentrated in degree \(-|I|\). In the left-module convention this surviving sheaf is \(B_I\). These are Proposition 3.4.7, Theorem 3.4.9 and the construction of §§3.4.8–3.4.12 of *Chiral Algebras*. [The two-point reconstruction from a realized vacuum](13-geometric-reconstruction.md#ch13-the-realized-vacuum-on-every-configuration)

## Ordered points lead to a different support {#ordered-cut-geometry}

Write three points in order as \((x,y,x)\) with \(x\ne y\). The partition \(13|2\) separates its two positions, but neither \(1|23\) nor \(12|3\) does. Keeping a word order therefore changes which open sets can impose factorization.

In a word the positions on the curve can vary while the labels retain their order \(1,\ldots,n\). Repeating the first letter gives the closed diagonal \(d:X^2\hookrightarrow X^3\), \(d(x,y)=(x,x,y)\), for the monotone surjection \(12|3\). What does a coefficient on \(X^3\) give on this repeated word? For complexes of right differential modules, the functor \(d^!\), called *extraordinary pullback*, is right adjoint to direct image \(d_*\). If a coefficient is obtained by placing \(N\) on the diagonal, Kashiwara's equivalence gives \(d^!d_*N\simeq N\). For a general word coefficient \(M_3\) we supply an identification \(d^!M_3\simeq M_2\). Repeating a letter twice, in either order, must give compatible identifications on the word coefficients.

The tuple \((x,y,x)\) with \(x\ne y\) has equal first and last positions, but another letter lies between them. No monotone surjection collapses those two labels while leaving the middle one in place.

**Definition (consecutive cut).** For \(0<p<n\), the cut after the \(p\)-th input separates the blocks \(\{1,\ldots,p\}\) and \(\{p+1,\ldots,n\}\). Every point in the first block must be distinct from every point in the second. Thus its open set is
\[
U_{p,n-p}=X^n\setminus\bigcup_{i\le p<j}\Delta_{ij}.
\tag{4.9}
\]
Collisions within either block are allowed. These are the opens used by the consecutive-cut tensor product in Chapter 5.

For instance, at \((x,x,y,y)\) with \(x\ne y\) the middle cut separates the two \(x\)-inputs from the two \(y\)-inputs. We can form the two pair products independently. Interchange the middle labels to obtain \((x,y,x,y)\). The first cut puts \(x\) on both sides, the last puts \(y\) on both sides, and the middle cut puts both values on both sides. The same grouping by position is now \(13|24\). To transport the original composition to this order requires an exchange of the middle inputs. A rule for products along a word supplies only its consecutive cuts. [An exchange tested on three fields](05-bar-and-coherence.md#ch05-from-support-to-fields)

In arity three, the two consecutive cuts give
\[
U_{1,2}=X^3\setminus(\Delta_{12}\cup\Delta_{13}),
\qquad
U_{2,1}=X^3\setminus(\Delta_{13}\cup\Delta_{23}).
\]
Their common failure locus is
\[
\begin{aligned}
Z_3
&=X^3\setminus(U_{1,2}\cup U_{2,1})\\
&=(\Delta_{12}\cup\Delta_{13})
\cap(\Delta_{13}\cup\Delta_{23})
=\Delta_{13}.
\end{aligned}
\tag{4.10}
\]
If \(x_1=x_3\), this pair lies across both cuts. Conversely, suppose both cuts fail and \(x_1\ne x_3\). The first cut can then fail only at \(x_1=x_2\), and the second only at \(x_2=x_3\). Together these equalities contradict \(x_1\ne x_3\). Thus the middle letter is free on the whole failure locus. This explains why a coefficient forced to vanish on both opens can still be nonzero at \((x,y,x)\) for \(x\ne y\). Whether a given coefficient does survive there is a further question. [The support theorem and two different supports](05-bar-and-coherence.md#ch05-the-support-remembers-which-cuts-were-allowed)

At two distinct labelled points both orders of the two singleton blocks, \(1|2\) and \(2|1\), are possible. A fixed increasing word counts only the first cut. To retain both orders, take one chart \(X^I\) for each total order on the labels, and glue two charts where their orders agree within every cluster of coincident labels. This gives the full ordered collision atlas. Its coefficient systems have extraordinary pullback along surjections with ordered fibres. Its convolution sums over all ordered decompositions \(I=A\sqcup B\), with the blocks separated. Swapping the two blocks makes this convolution symmetric monoidal. An algebra for it may still multiply noncommutatively.

Restrict a coalgebra on this atlas to the increasing chart. Project its coproduct onto the components in which the first block is an initial interval and the second is the remaining final interval. The resulting coproduct is the one for consecutive cuts. Already at two separated points that projection discards \(2|1\). This gives a reason why the passage to one word need not be invertible.

In formulas, let \(F_n,G_n\) denote the coefficients of words of length \(n\). The consecutive-cut convolution is
\[
 (F\star G)_n=\bigoplus_{p+q=n}Rj_{p,q*}j_{p,q}^*
      (F_p\boxtimes^{\mathbf L}G_q).
\]
Here \(j_{p,q}\) is the inclusion (4.9). The external derived tensor puts the two independent coefficients on their respective blocks, restriction imposes separation, and the derived direct image retains the cohomology of the nearby separated configurations. The unit \(k_\varnothing\) is supported on the empty word. An augmented associative algebra \(A\) for this convolution has a coherent multiplication \(A\star A\to A\) and a map \(A\to k_\varnothing\). Require this augmentation to be an equivalence on the empty word.

To express factorization of \(A\), form its bar coalgebra \(BA\). Its differential records multiplication of adjacent factors and, more generally, their associativity homotopies. Its coproduct splits a word. The required factorization map for each \(p,q>0\) is the restriction of this coproduct,
\[
 (BA)_{p+q}|_{U_{p,q}}\longrightarrow
 \bigl((BA)_p\boxtimes^{\mathbf L}(BA)_q\bigr)|_{U_{p,q}},
\]
and it must be an equivalence. On the separating open this coproduct identifies the whole bar coefficient, up to equivalence, with the external product of the two block coefficients. Conversely the cobar construction assembles a coalgebra into an algebra using its coproduct in the differential. For coefficients reduced at the empty word, a convolution of more than \(n\) positive factors vanishes on \(n\) labels. Thus the bar–cobar filtration is finite in each arity for both coefficient categories, with their respective convolutions. [Connected bar–cobar duality](05-bar-and-coherence.md#ch05-ordered-cuts-give-a-finite-geometric-bar-construction)

Starting with a chiral Lie algebra on the curve, regard it as supported on the singleton configurations of the Ran space. Its chiral Chevalley chains form a cocommutative coalgebra with factorization on separated blocks. Its differential uses the chiral bracket. Restrict to order-preserving surjections and project the coproduct onto the consecutive cuts. Applying associative cobar gives an associative chiral algebra of configuration complexes. A comparison with the original fields and their vacuum requires further data. To reverse the passage, the entire bar coalgebra would have to extend to every finite-set surjection with a compatible cocommutative coproduct and factorization on disjoint opens. The missing summand at two distinct labels and the additional collision open at \((x,y,x)\) explain why mere symmetry away from collisions does not give this extension. [Chapter 12](12-chiral-quantum-groups.md#ch12-associative-products-on-configurations)

These two sources of information appear separately even on three letters. The allowed cuts determine where the separated coefficients are known. Multiplying letters in either order also produces two maps on coefficients. Take closed degree-zero letters \(a,b,c\). In the bar word \([a|b|c]\), erasing the left separator first contributes \(+[(ab)c]\). Erasing the right one first contributes \(-[a(bc)]\). Their sum is the associator on these inputs, written as a one-letter word. Its primitive in a coherent associative algebra is specified by the [length-three bar equation](05-bar-and-coherence.md#eq-ch05-associator-homotopy). The geometry leaves its own question. Where both cuts fail, what can be recovered from the nearby separated fields?

::: figure fig-ordered-cut-support

## The open locus cannot determine every extension {#collision-supported-data}

The consecutive cuts tell us where a coefficient may be supported. What can one learn there from its values at separated points? Consider a sheaf \(F\) on a complex disk about \(0\). Adding a copy of \(\mathbb C\) supported at \(0\) leaves every stalk on the punctured disk unchanged. The inclusion \(F\to F\oplus\mathbb C_{\{0\}}\) is an isomorphism there and has cokernel \(\mathbb C_{\{0\}}\) at the centre. More generally restriction \(j^*\) to an open set kills every sheaf or differential module supported on its complement. A kernel or cokernel at a collision can thus disappear on restriction. The diagonal and unit axioms impose further conditions on a factorization algebra. [Sections supported on a collision](05-bar-and-coherence.md#ch05-the-support-remembers-which-cuts-were-allowed)

Suppose now that the stalk at the collision has also been specified. A section near the collision restricts to the punctured neighbourhood. Which classes there can occur as restrictions? To describe the target of this map, take complexes of sheaves in the usual topology on complex configurations and begin with two points. Their separation can wind around zero before the points meet.

### The normal link of a collision {#ch04-normal-link}

For two points on the complex line, hold their common position fixed and move their difference around zero. A small punctured disk of differences retracts onto a circle. Suppose a locally constant family of vector spaces has fibre \(E\) there and a trip around the circle returns vectors by a linear map \(C:E\to E\). The circle has one vertex and one oriented edge. A vector \(v\) assigned to that vertex returns as \(Cv\), so the cellular cochains are
\[
 E\xrightarrow{\,C-1\,}E
\]
in degrees \(0,1\). The cohomology in degree zero is \(\ker(C-1)\), the vectors unchanged by the loop. In degree one it is \(E/(C-1)E\). For a one-dimensional coefficient both groups have dimension one when \(C=1\) and both vanish when \(C=-1\).

The circle cochains occur in comparing two extensions. Extension by zero has zero stalk at the collision. The derived direct image takes the cochains of the punctured disk there. For a map \(f:P\to Q\) of cochain complexes the **cone** has degree-\(n\) term \(Q^n\oplus P^{n+1}\) and differential \((q,p)\mapsto(d_Qq+f(p),-d_Pp)\). Its cohomology vanishes exactly when \(f\) induces an isomorphism in each degree. At our boundary point the map has source zero. Its cone there is just the target, the circle complex we have computed. With more labels the punctured disk has to be replaced by the separated configurations near the chosen collision.

**Definition (normal link complex).** For \(n\) distinct labelled points write \(j:\operatorname{Conf}_n(\mathbb C)\hookrightarrow\mathbb C^n\). Let \(L\) be a finite-rank complex local system in degree zero, that is, a family of vector spaces with invertible parallel transport along paths. At a boundary point \(x\), a transverse slice fixes the locations of the clusters and varies the differences inside them. The **normal link complex** \(K_x\) is the cochain complex, considered up to maps inducing cohomology isomorphisms, of the separated part of a sufficiently small transverse neighbourhood with coefficients in \(L\). Its cohomology comprises closed cochains modulo exact ones. In sheaf notation,
\[
 K_x=(Rj_*L)_x
     \simeq\bigl(\operatorname{Cone}(j_!L\longrightarrow Rj_*L)\bigr)_x .
\]
Here \(Rj_*L\) takes sections and their higher cohomology on the part of each neighbourhood lying in the open. Its stalk is obtained by shrinking the neighbourhood to \(x\). Extension by zero \(j_!L\) has zero stalk there. The cone measures the difference of these two extensions, so its stalk at \(x\) is \(K_x\). Complexes use cohomological degrees. A shift \([r]\) moves degree \(a\) to \(a-r\). [Complexes, shifts and homotopies](05-bar-and-coherence.md#cohomology-and-parameters)

Can the link survive when each of two colliding pairs has a fixed vector? Give their common fibre the basis \(e_1,e_2\). Let the first twist act by \(\operatorname{diag}(1,2)\) and the second by \(\operatorname{diag}(2,1)\). On the first line the second circle differential is the identity. On the second line the first circle differential is the identity. Each line contributes an acyclic factor, although each twist has an invariant of its own. In larger fibres the correct test uses the vectors on which *every* \(C_i-1\) acts nilpotently.

**Theorem (simultaneous cluster twists).** Suppose the coincident points at \(x\) form nontrivial blocks \(S_1,\ldots,S_b\). A positive full twist of a block rotates all its points once around their common centre while leaving the other blocks apart. Let \(C_i\) be its action on a common fibre \(E\), using local base paths. Then
\[
 K_x\not\simeq0\quad\Longleftrightarrow\quad
 \bigcap_{i=1}^b\ker(C_i-1)^{\dim E}\ne0 .
\]
Conjugating the local representation does not change the criterion. The twists commute with each other and with the angular monodromies in this local product, even when the angular monodromies fail to commute among themselves.

*Proof.* In a cluster of size \(r\) translate its first point to zero, choose the difference of the first two as scale, and divide all the other differences by that scale. Up to homotopy the separated normal directions are \(S^1\times Y_r\), where \(Y_r\) parametrizes \(r-2\) ordered points of \(\mathbb C\setminus\{0,1\}\). Write \(Y_2=\mathrm{pt}\). The scale circle acts by the full twist. Disjoint discs give a product of these spaces for the different blocks. Decompose \(E\) into simultaneous generalized eigenspaces of the central twists. Any summand on which some \(C_i-1\) is invertible has a contractible circle complex. On the common generalized unit summand \(E_1\), the angular cochains have Euler characteristic
\[
 \dim(E_1)\prod_i(-1)^{|S_i|-2}(|S_i|-2)! .
\]
Forgetting the moving points one at a time gives punctured-line fibres with Euler characteristics \(-1,-2,\ldots,-(r-2)\), which proves the formula. It is nonzero when \(E_1\ne0\), so some angular cohomology survives. Appending a scale circle forms the two-term complex of \(C_i-1\) acting on these angular cochains. If this new complex were acyclic, \(C_i-1\) would act invertibly on their cohomology. It is nilpotent there, and a nilpotent map cannot be invertible on a nonzero space. Each remaining twist commutes with the ones already used and is still unipotent on the common summand. The same argument adds all the scale circles. ∎

In the two-line example take the colliding pairs to be \(12\) and \(34\), with all the other pair monodromies trivial. The common generalized unit space is zero, so the link at the double collision vanishes. Testing each divisor separately would retain one line on each and give the wrong answer at their intersection.

At one full collision of size \(n\ge3\), the scale circle and the shapes \(Y_n\) also determine the ranks. Put \(C\) for the scale monodromy, \(V_0=\ker(C-1)\) and \(V_1=\operatorname{coker}(C-1)\), with their induced angular actions. The shape space identifies with \(M_{0,n+1}\) by fixing \(0,1,\infty\). Its stable compactification \(\overline M_{0,n+1}\) includes boundary divisors at infinity. Suppose the monodromy around *every* boundary divisor has no eigenvalue \(1\) on either \(V_0\) or \(V_1\). With \(m=n-2\), the link then has cohomology only in degrees \(m,m+1\), of dimension \(m!\dim\ker(C-1)\) in each.

The two cohomology groups along the radial circle are \(V_0,V_1\). Take either as the angular coefficient \(V\). At an angular boundary point the normal circles have commuting monodromies. The hypothesis makes a circle differential invertible, so the boundary complex contracts and \(H_c^*(Y_n;V)\to H^*(Y_n;V)\) is an isomorphism. Forgetting the \(m\) moving points one at a time bounds ordinary cohomology above degree \(m\), also for the dual coefficient \(V^\vee\). Since \(Y_n\) has real dimension \(2m\), Poincaré duality then makes \(H_c^q(Y_n;V)\) vanish for \(q<m\). Only angular degree \(m\) remains, with dimension \(m!\dim V\) by the Euler characteristic. The two radial degrees therefore contribute to total degrees \(m\) and \(m+1\). Their ranks are equal because the kernel and cokernel of \(C-1:E\to E\) have the same dimension.

For \(n=3\) take a single unipotent Jordan block \(C\) of size \(d\ge2\) and angular generators \(2I,3I\) around the two finite punctures. The angular multiplier at infinity is \(I/6\). Both link groups have dimension one for every \(d\). The generalized unit eigenspace detects survival. Under the angular hypothesis the ordinary kernel determines its multiplicity.

### Two ordered points on the sphere {#ch04-sphere-binary-collision}

For a colliding pair in the plane, translating the common point transports its circle of normal directions without a choice of frame. On a sphere the normal plane at a collision moves with that point. Put \(C=\mathbb P^1(\mathbb C)\simeq S^2\), let \(i:C\hookrightarrow C^2\) be the diagonal and \(j:U=C^2\setminus i(C)\hookrightarrow C^2\) its complement. The first projection \(p:U\to C\) is a locally trivial bundle with contractible fibre \(S^2\setminus\{x\}\), hence a homotopy equivalence. At \((x,x)\), the difference \((v_1,v_2)\mapsto v_2-v_1\) identifies the normal plane with \(T_xC\). Its unit circles form the oriented bundle \(q:E=S(TC)\to C\).

Take first a locally constant coefficient \(L\) on \(C\), locally equivalent to a bounded complex of finite-dimensional vector spaces. Such a coefficient is called perfect. It can record the homotopies between transports as well as their action on cohomology. The open coefficient is \(p^*L\). On a small punctured normal neighbourhood the radial coordinate contracts, leaving just the unit circle with coefficient \(q^*L\). Thus the complex of nearby sections along the diagonal is
\[
 \mathcal B(L)=i^*Rj_*p^*L\simeq Rq_*q^*L.
\]
In particular, \(p^*L=j^*(L\boxtimes\mathbb C)\) is a separated two-point input. On the normal circle bundle the first projection is \(q\), and the second is homotopic to \(q\) along the short normal geodesic. Thus two perfect inputs \(A,B\) give \(\mathcal B(A\otimes B)\).

**Definition (attaching map).** For a constructible complex \(P\) on this two-stratum space, set \(W=i^*P\) and \(p^*L=j^*P\). Restricting sections from a neighbourhood to its punctured part induces
\[
 W=i^*P\longrightarrow i^*Rj_*j^*P=\mathcal B(L).
\]
The homotopy fibre of this arrow, its cone shifted by \([-1]\), is the costalk along the diagonal \(i^!P\). It records classes with support on the diagonal. The ordinary restriction \(i^*P\) supplies the source of the arrow. Even when both its source and target are prescribed, the arrow can vary.

Both strata are simply connected. A loop in the base detects no ordinary monodromy. Nevertheless the oriented tangent frames on the two hemispheres differ along the equator by a rotation of winding number two. Thus the Euler number of \(TC\) is \(2\). To keep track of its sign on cochains, take the round sphere. In colatitude \(s\), longitude \(\varphi\) and positive tangent angle \(\psi\), choose the normalized area form and angular connection
\[
 \omega=\frac{\sin s}{4\pi}\,ds\wedge d\varphi,\qquad
 \vartheta=\frac{d\psi+\cos s\,d\varphi}{2\pi}.
\]
The area integral and the positive fibre integral are both one. Differentiation gives \(d\vartheta=-2q^*\omega\) as an equality of forms. The total space is \(E\simeq\mathbb RP^3\), and \(\gamma=\vartheta\wedge q^*\omega\) has integral one on \(E\).

Take the southern horizontal frame minus the northern frame on the equator oriented as the boundary of the northern hemisphere. In that convention the positive generator of \(\pi_2(C)\) gives a degree-minus-one map on the fibre cohomology of \(Rq_*\mathbb C\). It takes the positive circle class \(\theta\) to \(T\theta=-2\) and the constant class to \(T1=0\). The same factor of \(-2\) will give a primitive for the pullback of the area class.

What does pulling back to the circle bundle do to a coefficient \(L\) with cohomology only in degrees \(a<b\)? Its two cohomology sheaves are constant on the sphere. The truncation triangle gives a connecting map
\[
 H^b(L)[-b]\longrightarrow H^a(L)[1-a].
\]
This map, the Postnikov extension class, records how the two sheaves are joined in \(L\). The shift difference is \(b-a+1\), so its matrix entries belong to the cohomology of the base in that degree. On the sphere it can survive only if \(b=a+1\), in which case each matrix entry is a multiple of \([\omega]\). Since \(q^*\omega=-\tfrac12 d\vartheta\), the pulled-back extension admits a splitting. Splitting amounts to choosing a primitive for the pulled-back class.

Three degrees give a different answer. Give \(e_0,e_1,e_2\) degrees \(0,1,2\) and zero internal differential. For \(c=0,1\), let \(N_ce_2=e_1\), \(N_ce_1=ce_0\), \(N_ce_0=0\). On differential forms with values in these three graded fibres, \(\omega N_c\) raises form degree by two and lowers fibre degree by one. Thus \(D=d+\omega N_c\) has total degree one. Its square is zero since \(d\omega=0\) and a four-form on the sphere vanishes. This flat superconnection defines a perfect local system \(L_c\). Its ordinary cohomology sheaves in the three fibre degrees are the same for both choices of \(c\). On \(\mathcal B(L_c)\), tensoring the actions of \(N_c\) and \(T\) with the graded sign gives the following matrix from degree two to degree one:
\[
 (e_1\otimes\theta,e_2\otimes1)
 \longrightarrow (e_0\otimes\theta,e_1\otimes1),
 \qquad
 M_c=\begin{pmatrix}c&0\\2&1\end{pmatrix}.
\]
For \(c=0\) the two columns of \(M_c\) span the same line. For \(c=1\) its determinant is one. Thus transport on the normal circles distinguishes coefficients whose three ordinary cohomology sheaves agree. The same distinction has a representative on \(E\). The section \(e_2\) has differential \(q^*\omega\,e_1\). The term \(\tfrac12\vartheta e_1\) cancels this contribution because \(d\vartheta=-2q^*\omega\). The differential acting on \(e_1\) leaves one more term, with a minus sign from passing the one-form \(\vartheta\),
\[
 D\bigl(e_2+\tfrac12\vartheta e_1\bigr)=-\tfrac c2\,\gamma e_0 .
\]
Thus the dimensions of the global cohomology of \(\mathcal B(L_c)\), in degrees zero through five, are \((1,1,1,1,1,1)\) for \(c=0\) and \((1,1,0,0,1,1)\) for \(c=1\). The second step survives precisely when \(c\ne0\), because \(\int_E\gamma=1\).

Even identical open and diagonal restrictions can have different attachments. Fix the constant open coefficient and \(W=\mathbb C[-3]\). A map \(W\to Rq_*\mathbb C\) is specified up to homotopy by a class in \(H^3(E;\mathbb C)\). The zero class and \([\gamma]\) agree on each individual direction circle. Taking global sections of their homotopy fibres gives dimensions \((1,1,1,1)\) and \((1,0,0,1)\) respectively in degrees \(1,3,4,5\). An all-arity unital factorization algebra on this geometry still requires compatible multiplications and a vacuum insertion. [Higher transport at the sphere collision](#atlas-c-sphere-binary-higher-transport)

### Four charged rays and their possible attachments {#ch04-gaussian-collision}

The attaching map on the sphere could vary with the open coefficient fixed. There is a physical example in which even the open coefficient can be calculated. Take a Heisenberg boundary of abelian Chern–Simons theory at nonzero complex level \(k\). A Gaussian Wilson ray carries a fixed charge to a boundary insertion. Choose the Cauchy propagator, radial transverse regularization, outgoing mutual subtraction and parallel-copy framing. Fix a branch in a separated chamber and work on finite oscillator polynomials. Send in oscillator-free states of charges \(\alpha_a\), and project onto the oscillator-free outgoing state of charge \(\sum_a\alpha_a\), with that state assigned coefficient one. For this preparation the model gives the separated amplitude
\[
 F_{\boldsymbol\alpha}(z)=\prod_{a<b}(z_a-z_b)^{\alpha_a\alpha_b/k}.
\]
Each pair contributes its Gaussian contraction to the logarithm. Equivalently, commuting the annihilation part of one current intertwiner through the creation part of the next produces its factor. Continue from the chosen chamber along a common path with the individual coordinate frames fixed. The branches span a rank-one local system. A full twist of \(S\) winds each internal difference once, hence has multiplier
\[
 \exp\!\left(\frac{2\pi i}{k}\sum_{\{a,b\}\subset S}\alpha_a\alpha_b\right).
\]
For this rank-one system the link criterion is \(\sum_{\{a,b\}\subset S}\alpha_a\alpha_b/k\in\mathbb Z\) for each nontrivial block \(S\) of the collision. For a pair this recovers the full-turn phase of the normalized two-ray amplitude. The frames are held fixed during continuation. A rotation of an individual frame has its own conformal phase. The outgoing projection makes sense also at nonzero total charge. [Two charged rays](03-local-fields.md#ch03-charged-current-contour)

Take four charges \(1,1,1,1\) at level \(2\), so the outgoing charge is \(4\). For a block of \(r\) rays the exponent in units of \(2\pi i\) is \(\binom r2/2\). At \(r=2,3,4\) this gives \(1/2,3/2,3\) and phases \(-1,-1,+1\). Every proper collision contains a block of size two or three, including each block in a two-pair collision. Its \(-1\) phase kills the corresponding link. For the full four-point collision the scale phase is \(+1\), so both degrees of the radial circle survive.

It remains to count the shapes. Fix three marks at \(0,1,\infty\) on the projective line. The remaining two distinct marks parametrize \(Y_4=M_{0,5}\). Every boundary divisor of the stable compactification corresponds to a proper block and has monodromy \(-1\). Its circle cochains contract. Compactly supported and ordinary angular cohomology therefore agree. Forgetting one moving point at a time bounds its degree above by two, and duality bounds it below by two. The two punctured-line fibres used in the count have Euler characteristics \(-1,-2\), giving two classes in degree two. Combining them with the two radial degrees gives the full link \(K\),
\[
 \dim H^2K=\dim H^3K=2,\qquad H^aK=0\quad(a\ne2,3).
\]
More generally, at integral level \(\ell\ge2\) with every charge one, the first collision with nonzero link is the full collision at the least \(n\ge2\) for which \(\ell\) divides \(\binom n2\). The same argument on \(M_{0,n+1}\) gives ranks \((n-2)!\) in degrees \(n-2,n-1\).

The two-dimensional space \(H^2K\) is large enough to contain many different image lines of an attaching map. Which lines can actually occur? Work on the labelled transverse slice \(\mathbb C^3\), with \(i\) the inclusion of its origin. Use middle-perversity support and cosupport conditions. The resulting category of perverse sheaves is abelian, so one can form a quotient by a subobject supported at the origin. A degree-zero local system on the smooth open threefold is placed in ordinary degree \(-3\), by the shift \([3]\).

Write \(V=H^2K\) and \(V'=H^3K\). In this example extension by zero \(P_!=j_!L[3]\) is perverse. Its intermediate extension \(j_{!*}L[3]\) has no nonzero subobject or quotient supported on the boundary. The part lost in passing from the former to the latter is the point-supported \(i_*V\), giving the exact sequence
\[
 0\longrightarrow i_*V\longrightarrow P_!
 \longrightarrow j_{!*}L[3]\longrightarrow0 .
\]
For each line \(W\subset V\), form the quotient \(P_W=P_!/(i_*W)\) in the perverse category. Its ordinary stalk is \(i^*P_W\simeq W[1]\). The costalk \(i^!P_W\) measures local cohomology supported at the origin. Since \(i^!P_!\simeq K[2]\), the costalk sequence gives \(H^0 i^!P_W=V/W\) and \(H^1 i^!P_W=V'\), with all other groups zero.

Thus the stalk has one class in degree \(-1\), and the costalk has ranks one and two in degrees zero and one, for every line. The quotients also agree off the origin. The attaching map \(i^*P_W\to K[3]\) on \(H^{-1}\) has image the particular line \(W\subset V\). Indeed its image is the kernel of the boundary map \(V\to H^0i^!P_W=V/W\). An isomorphism of two such sheaves acts on the separated rank-one local system by a scalar and, by naturality of \(j_!\), must carry one embedded kernel in \(P_!\) to the other. A scalar fixes each line. Hence distinct \(W\)'s give distinct isomorphism classes parametrized by \(\mathbb P(V)\cong\mathbb P^1\). This calculation concerns extensions on the fixed labelled slice. A comparison with an oriented Hall coefficient must identify the attaching morphisms and respect the other collision maps.

The four rays have identical charges. What changes if their labels may be permuted? Fix the positive elementary half-braid to act by \(+i\), keeping every individual coordinate frame fixed. One description is the connection \(d-\tfrac12d\log\Delta\), with \(\Delta=\prod_{a<b}(z_a-z_b)\), on the trivial line with permutations acting trivially on its coordinate fibre. A positive half exchange changes the argument of \(\Delta\) by \(\pi\). On the centred normal slice with origin fixed by \(S_4\), this determines an \(S_4\)-action on \(V=H^2K\).

Its character can be computed on the shapes \(M_{0,5}\). Under simultaneous dilation by \(a\), a horizontal section scales by \(a^3\). Compactly supported angular cohomology is concentrated in degree two and identifies equivariantly with \(V\). The trace of a finite permutation is consequently its compactly supported Lefschetz number on the shape space. A transposition has no fixed shape, since an affine map fixing the two unswapped points fixes every point. A three-cycle has two fixed shapes, the two orderings of an equilateral triple about the fourth mark. Their dilation factors are primitive cube roots, with cube \(1\), so the trace is \(2\). An operator of order dividing three is diagonalizable over \(\mathbb C\). Two cube roots of unity have sum \(2\) only if both are \(1\), so every three-cycle acts as the identity on \(V\). The three-cycles generate \(A_4\), and the transposition trace \(0\) distinguishes the two summands:
\[
 V\simeq{\bf1}\oplus\operatorname{sgn}.
\]
Naturality of \(P_!\to P_W\) says that the permutation action descends to the quotient exactly when it preserves the kernel \(i_*W\). A transposition has eigenvalues \(+1\) and \(-1\) on the two summands of \(V\). A line spanned by a vector with nonzero components in both summands changes under that transposition. Thus only the trivial line and the sign line in \(V\) survive from the labelled \(\mathbb P^1\). On the open set the half-braid acts by \(i\). At the collision the stabilizer acts on \(H^{-1}i^*P_W=W\) by \(+1\) or \(-1\).

There is a further choice between retaining that stabilizer and requiring ordinary inverse image from the coarse variety. Write \(\pi:X\to X/S_4\) for the finite quotient of the centred slice and \(\bar L\) for the specified line on the unordered open \(\bar j\). For an equivariant complex \(P\), the counit \(\pi^*(R\pi_*P)^{S_4}\to P\) on the stalk at \(x\) is the inclusion of its stabilizer invariants. Indeed the finite fibre is an orbit, and over \(\mathbb C\) taking invariants is exact. Stabilizers are trivial on the distinct open, and the proper collision stalks vanish. At the origin the test reduces to \(W^{S_4}\to W\), so precisely the trivial line meets this extra requirement. In fact \(P_{\bf1}\simeq\pi^*\bar j_{!*}\bar L[3]\). Taking invariant finite pushforward in the canonical sequence retains exactly \(V^{S_4}={\bf1}\), and preserves the perverse image of extension by zero in right direct image. This identifies the intermediate extension downstairs. The selection is unique within the displayed quotient family under the coarse inverse-image hypothesis. The Gaussian coefficient alone imposes no such hypothesis on a physical collision. The two tests ask different questions of \(W\). Equivariance asks whether every permutation preserves \(W\) as a subspace. Coarse pullback asks whether every permutation fixes each vector of \(W\).

Which attachment does the outgoing charge-four Wick functional give? Work at finite field number with compact smooth spacetime tests, keeping the rays vertical over their supports. Resolve the collision diagonals by real oriented blowup. In a cluster chart let \(r_S\) be the radius of cluster \(S\), measured relative to its parent for a proper cluster. Divide the Wick evaluation on the interior by \(\prod_S r_S^{\binom{|S|}{2}/2}\). Its value \(\Phi\) on the unit extends smoothly to the face and retains the nonzero angular branch. On a test \(x\) the result is \(\Phi\lambda(x)\), where the translated Gaussian functional satisfies \(\lambda(1)=1\). Cauchy translation fixes the unit and transports \(\lambda\). Thus \(G\mapsto G(1)\lambda\) projects the complex of test functionals onto a line and commutes with the differential twisted by the measured phase.

Allow smooth position forms to take unrestricted boundary values on the blowup. Each small corner meets the distinct-position locus in a contractible set, so the line there extends by derived direct image from the interior. Proper pushforward to the centred slice gives the split summand \(P=Rj_*L[3]\), where \(j\) includes the distinct positions. At the origin \(i\), write \(K=i^*Rj_*L\) as above. The attaching map is
\[
 i^*P=K[3]\xrightarrow{\;1_{K[3]}\;}K[3]=i^*Rj_*j^*P .
\]
{#eq-ch04-absolute-wick-attachment}
Its homotopy fibre is zero, so \(i^!P=0\). Its image in degree \(-1\) is all of \(V\), whereas each line quotient \(P_W\) has attaching image \(W\).

Compact support of the tests in spacetime allows these unrestricted position forms. Requiring the forms to vanish on the position boundary would give \(j_!L[3]\) for the same line. The full charge-four state space also contains the nonzero descendant \(J_{-1}|4\rangle\), whose projection onto the oscillator-free outgoing state vanishes. For the full compact Batalin–Vilkovisky complex one still needs a comparison on cochains with prescribed normal and point supports, including coincident distributional inputs, compatible with iterated collisions and both vacua. [The absolute Wick line at a four-ray collision](#s-four-ray-absolute-wick-line)

### An irregular collision can detect a hidden extension {#ch04-irregular-collision}

The circle calculation measured what happens after continuation around a closed loop. For a connection with an irregular singularity, horizontal solutions can also grow or decay exponentially on approaching the collision. Two connections with identical loop transport can then give different cohomology at the collision. Consider three points. Take difference coordinates \(x=z_1-z_3\) and \(y=z_2-z_3\). Off the three collision lines \(xy(x-y)=0\), the slope \(u=x/y\) is defined. Pull back the two-dimensional connection whose horizontal columns satisfy
\[
dy_1=a y_2\,du,\qquad dy_2=-2u^{-3}y_2\,du .
\]
Its diagonal exponential factors are \(1\) and \(e^{1/u^2}\). The second component of a horizontal column is a multiple of \(e^{1/u^2}\), and the first is obtained by integrating \(a e^{1/u^2}du\). The Laurent series of this one-form has no \(u^{-1}du\) coefficient. Its integral around the puncture vanishes, so the ordinary analytic monodromy is trivial for every \(a\in\mathbb C\). At \(a=0\) the connection splits. To test splitting algebraically, let \(j\) include the complement of the collision lines, let \(i\) include their common origin, and put \(C_a=\operatorname{Cone}(j_!M_a\to j_*M_a)\) for the pulled-back connection \(M_a\). Use algebraic holonomic direct images and the de Rham normalization in which the constant connection on the plane gives \(\mathbb C[2]\).

Separate the common scale \(x\) from the shape \(r=y/x=1/u\). The open then has the form \(\mathbb G_m\times(\mathbb A^1\setminus\{0,1\})\). On the shape curve, write a section of the dual connection in coordinates \((p,q)\). Its de Rham differential is
\[
 (p,q)\longmapsto \bigl(p',\,q'+2rq-a p/r^2\bigr)\,dr .
\]
The second coordinate alone has differential \(q\mapsto (Tq)\,dr\) with \(Tq=q'+2rq\). The quotient, with coordinate \(p\), has the ordinary derivative. Does its constant section \(1\) admit a horizontal lift? The trial lift \((1,0)\) has differential \((0,-a/r^2)\,dr\). Changing the lift by a section of the second coordinate changes this by \((Tq)\,dr\). Its class in the cokernel is therefore \(-a[r^{-2}dr]=-2a[dr]\), since \(T(-1/r)=r^{-2}-2\). To see that \([dr]\ne0\), try to solve \(Tq=1\). A finite pole of \(q\) would give a higher pole in \(q'\), and a nonzero polynomial \(q\) gives a polynomial of positive degree in \(Tq\). Thus the class obstructs a horizontal algebraic lift exactly when \(a\ne0\).

In the exponential summand, subtracting \(Tq\,dr\) reduces every higher pole and every positive polynomial power. The remaining cohomology classes have basis \(dr,dr/r,dr/(r-1)\) in degree one, and the kernel of \(T\) is zero. The trivial quotient contributes one constant in degree zero and two logarithms in degree one. The constant maps to \(-2a[dr]\). At \(a=0\) it survives and all three exponential classes remain. At \(a\ne0\) it dies and removes one of those three classes. The angular dimensions are therefore \((1,5)\) and \((0,4)\).

The scale factor contributes \(1,dx/x\), so the ordinary de Rham dimensions in degrees \(0,1,2\) become \((1,6,5)\) and \((0,4,4)\). Dilation contracts the transverse plane to the origin without changing its angular coefficient. In the indicated de Rham normalization, duality for the supported complex sends ordinary degree \(m\) to costalk degree \(1-m\). Reading the ordinary dimensions in reverse order gives, in degrees \(k=-1,0,1\), the dimensions of \(H^k(i^!C_a)\),
\[
 (5,6,1)\quad(a=0),\qquad (4,4,0)\quad(a\ne0).
\]
The ranks decide whether the algebraic connection splits. To recover its marked Stokes multiplier, use the horizontal column \(s_1=(1,0)^{\mathsf t}\). Give the second solution the lower component \(e^{1/u^2}\), and normalize its upper component to tend to zero in the chosen decay direction. Denote the two columns by \(s_{2,+},s_{2,-}\) for \(r=1/u\to+i\infty,-i\infty\), respectively. In these frames
\[
 s_{2,+}-s_{2,-}=2i\sqrt{\pi}\,a\,s_1 .
\]
Take the upward contour \(\gamma:r=\delta+it\) with \(0<\delta<1\) and \(t\) increasing from \(-\infty\) to \(+\infty\). The rapid-decay period of the dual extension class is \(-2a\int_\gamma e^{r^2}\,dr=-2i\sqrt{\pi}\,a\). Subtracting the lower normalized column from the upper gives minus that period. Changing a graded frame rescales the multiplier, while the costalk dimensions stay fixed.

### Three flags at a four-point collision {#ch04-three-flags-four-points}

For three points the dimension of the total costalk distinguished the two connections. With four points we can also compare maps *into* the costalk. Two different sequences of collisions can approach the same stratum. Translate \(z_1\) to zero and write \(s=z_2-z_1,\ x=z_3-z_1,\ y=z_4-z_1\) on the transverse space \(X=\mathbb A^3\). On the distinct-point open \(j:U\hookrightarrow X\) use \(r=x/s,\ t=y/s\). Write \(N_a(r)\) for the preceding angular connection and tensor it with a two-dimensional \(W\) carrying \(d-J\,d\log(t-r)\), where \(J^2=0\ne J\). Winding \(t-r\) once counterclockwise gives \(\exp(2\pi iJ)=1+2\pi iJ\). Let \(M\) be the resulting coefficient and \(C=\operatorname{Cone}(j_!M\to j_*M)\).

On the line \(L=\{x=y=s\}\) labels \(2,3,4\) coincide. Its origin \(i\) is the total collision. To reach \(L\) we can first collide \(2,3\), at \(u=r-1=0\), or \(3,4\), at \(w=t-r=0\). These nested collisions are the two flags to be compared.

These two orders differ on a single logarithmic one-form. First let \(u\) become small compared with \(w\). The form \(\beta=d\log(1+u/w)\) is regular at \(u/w=0\), so its logarithmic residue there is zero. In the opposite order \(w/u\) tends to zero. The identity
\[
 d\log(1+u/w)=d\log(u/w)+d\log(1+w/u)
\]
then leaves \(d\log(u/w)\), since the second term has zero residue in that chart. The term \(1+u/w\) appears because the third normal divisor meeting the two flag divisors is \(u+w=0\).

To compare the two maps, keep the horizontal frame of \(N_a^\vee\) at \(r=1\) and transport \(W^\vee\), the dual of \(W\), in the same positive real chamber. In the simultaneous normal germ, \(w\) is a scale and \(u/w\) is a coordinate on the line with punctures at \(0,-1,\infty\). Write \(q=d\log w\), \(\alpha=d\log(u/w)\), \(\beta=d\log(1+u/w)\). Its complex \(P\) has angular classes \(1,\alpha,\beta\). On each iterated germ the two logarithms \(p=d\log u\), \(q=d\log w\) identify the target complex \(T\), and \(\rho=p-q\). The ordinary restrictions \(F_u,F_w:P\to T\) are
\[
\begin{array}{c|ccc}
 &q&\alpha&\beta\\ \hline
 F_u&q&\rho&0\\
 F_w&q&\rho&\rho
\end{array}
\]
on logarithmic generators. Both keep the same differential \(d+J^{\mathsf t}q\wedge-\) on the dual of the two-dimensional coefficient \(W\). The comparison therefore asks whether the difference on \(\beta\) survives passage to cohomology and then to the total collision.

A punctured disk in \(L=\{x=y=s\}\) still separates this triple from the first label. Its cohomology is the exterior algebra \(\Lambda(\lambda)\) on \(\lambda=d\log s\) in degree one. Indeed \(s\) is a complex coordinate, and on \(s=\varepsilon e^{i\theta}\) its logarithmic derivative integrates to \(2\pi i\) for one positive turn. Both flags have this same outer link.

Now let \(A\) be the unshifted algebraic de Rham complex of the dual coefficient on the shape surface \(r,t\notin\{0,1\},\ t\ne r\). Restriction \(S:A\to P\) to the simultaneous normal germ followed by \(F_j:P\to T\) computes the ordinary restriction for flag \(j\). Tensor with the outer link, then dualize. Naturality of the localization triangle uses the same boundary for extension by zero in the two cases and gives
\[
 D_j=(1\otimes F_jS)^\vee[-1]:
 (\Lambda(\lambda)\otimes T)^\vee[-1]\longrightarrow
 (\Lambda(\lambda)\otimes A)^\vee[-1]\simeq i^!C[1],
 \qquad j=u,w .
\]
With \(\mathrm{DR}(\mathcal O_X)=\mathbb C[3]\), an ordinary class of degree \(m\) is dual to degree \(1-m\) in this target. Choose \(v\notin J^{\mathsf t}W^\vee\) with \(J^{\mathsf t}v\ne0\). For \(g=e=(1,-a/r)\) or \(g=f=(0,1)\) in the dual angular frame, consider the closed form \(g(r)v\,q\wedge d\log(t-1)\). Since \(t-1=u+w=w(1+u/w)\), its logarithmic factor is \(q\wedge(q+\beta)=q\wedge\beta\). The first row of the table sends this to zero. The second sends it to \(q\wedge\rho\) with coefficient \(g(1)v\). This class survives because the image of \(v\) in \(W^\vee/J^{\mathsf t}W^\vee\) is nonzero. Multiplication by \(\lambda\) raises the ordinary degree by one and detects the difference one degree lower after duality.

The explicit form distinguishes the two maps. To see how much of the total collision they account for, take the ranks of each map, the sum of their images, and their difference. The four entries in each tuple below are in degrees \(1,0,-1,-2\). The middle columns give image ranks on cohomology.

| Parameter | \(H^\bullet(i^!C[1])\) dimensions | Each flag | Sum of the images | \(D_w-D_u\) |
| --- | --- | --- | --- | --- |
| \(a=0\) | \((1,9,31,23)\) | \((1,4,5,2)\) | \((1,5,8,4)\) | \((0,1,3,2)\) |
| \(a\ne0\) | \((0,4,24,20)\) | \((0,2,4,2)\) | \((0,2,6,4)\) | \((0,0,2,2)\) |

For example, at \(a\ne0\) in degree \(-1\), each image has dimension four and their sum has dimension six. The two images therefore meet in a plane inside a vertex cohomology group of dimension \(24\). Which subspace do they generate together?

On angular one-forms the pair of restrictions sends \(x\alpha+y\beta\) to \((x\rho,(x+y)\rho)\). The first entry recovers \(x\) and subtracting it from the second recovers \(y\). Both maps retain the same radial complex and take \(1\) to \(1\). This splits the pair on the normal complex. After duality the two images together span the image of the localization boundary from \(L\), a proper subspace of the vertex cohomology in both rows.

What happens when labels 2 and 4 meet first? Their collision is \(t=1\), or \(u+w=0\). Keep \(w\) as the scale and use \(\xi=(u+w)/w\) at this third puncture. Then \(u=w(\xi-1)\). On its punctured normal disc, \(\alpha=d\log(1-\xi)\) has a holomorphic primitive, while \(\beta=d\log\xi\) represents the positive class \(\eta\). Thus restriction \(F_c\) on cohomology takes \([p]=[d\log u]\) and \([q]=[d\log w]\) to the same class \([q]\). Two test forms separate the outcomes:
\[
 F_c[q\wedge p]=0,\qquad F_c\bigl[q\wedge d\log(t-1)\bigr]=[q\wedge\eta] .
\]
The last class pairs to \((2\pi i)^2\) with the product of the positive \(w\)- and \(\xi\)-circles, in that order. With the coefficient \(v\) above it survives modulo \(J^{\mathsf t}W^\vee\).

On the exceptional line with coordinate \(u/w\), take positive meridians at \(0,\infty,-1\) in that order. Their scalar residues on \((\alpha,\beta)\) are \((1,0),(-1,-1),(0,1)\). At infinity the positive parameter is \(w/u\), so its logarithm has differential \(-\rho\) in the earlier table. The three rows sum to zero on the angular one-forms. Each restriction also carries the constant \(1\) to \(1\). Any two rows recover both angular coefficients, and every pair retains the radial complex. Hence any two boundary images span the same image from \(L\).

For the third boundary alone the global angular images have dimensions \((1,2,2)\) when \(a=0\) and \((0,0,2)\) when \(a\ne0\). In the latter case the degree-one classes reaching the simultaneous normal complex are multiples of \(\alpha\), which vanishes at the third puncture. In degree two the two coefficient values \(e(1)\) and \(f(1)\), expressed in the horizontal frame at the regular point \(r=1\), multiply \(\bar v\,q\wedge\eta\), where \(\bar v\) is the class of \(v\) modulo \(J^{\mathsf t}W^\vee\). The global sections \(e(r),f(r)\) occurred as coefficients of closed two-forms. Their values at \(1\) specify the two local horizontal germs.

An angular image in successive dimensions \((x,y,z)\) occurs once with \(1\) and again one degree higher with \(\lambda\). Its four dimensions are therefore \((x,x+y,y+z,z)\). After the shifted duality the third image, in degrees \(1,0,-1,-2\), has ranks \((1,3,4,2)\) at \(a=0\) and \((0,0,2,2)\) otherwise. Comparing these algebraic maps with independently defined sectorial specialization still requires the Stokes filtrations, sectors and their identification with the chosen markings.

The two marked flag maps induce different maps on cohomology, so a chain homotopy between them cannot exist with these identifications. For two bracketings whose difference *is* a boundary, one can ask for the map exhibiting that boundary. On three inputs it must lower degree by one. Its differential has to account both for the differential of the output and for those of the individual inputs. [The three-letter bar equation](05-bar-and-coherence.md#eq-ch05-associator-homotopy)
