Exercises
==============

**1.** Show that composition of paths satisfies the following cancellation property: If
:math:`f_0 \cdot g_0 \simeq f_1 \cdot g_1` and :math:`g_0 \simeq g_1` then :math:`f_0 \simeq f_1`.

**2.** Show that the change-of-basepoint homomorphism :math:`\beta_h` depends only on the homotopy
class of :math:`h`.

**3.** For a path-connected space :math:`X`, show that :math:`\pi_1 (X)` is abelian iff all basepoint-change
homomorphisms :math:`\beta_h` depend only on the endpoints of the path :math:`h`.

**4.** A subspace :math:`X \subset \mathbb{R}^n` is said to be *star-shaped* if there is a point :math:`x_0 \in X` such that,
for each :math:`x \in X`, the line segment from :math:`x_0` to :math:`x` lies in :math:`X`. Show that if a subspace
:math:`X \subset \mathbb{R}^n` is locally star-shaped, in the sense that every point of :math:`X` has a star-shaped
neighborhood in :math:`X`, then every path in :math:`X` is homotopic in :math:`X` to a piecewise linear
path, that is, a path consisting of a finite number of straight line segments traversed
at constant speed. Show this applies in particular when :math:`X` is open or when :math:`X` is a 
union of finitely many closed convex sets.

**5.** Show that for a space :math:`X`, the following three conditions are equivalent:

.. container:: no-margin
    
    |indent| \(a\) Every map :math:`S^1 \rightarrow X` is homotopic to a constant map, with image a point.

    |indent| \(b\) Every map :math:`S^1 \rightarrow X` extends to a map :math:`D^2 \rightarrow X`.

    |indent| \(c\) :math:`\pi_1(X,x_0)=0` for all :math:`x_0 \in X`. 

Deduce that a space :math:`X` is simply-connected iff all maps :math:`S^1 \rightarrow X` are homotopic. [In
this problem, 'homotopic' means 'homotopic without regard to basepoinbts'.]

**6.** We can regard :math:`\pi_1(X,x_0)` as the set of basepoint-preserving homotopy classes of 
maps :math:`(S^1,s_0)\rightarrow(X,x_0)`. Let :math:`[S^1, X]` be the set of homotopy classes of maps :math:`S^1 \rightarrow X`,
with no conditions on basepoints. Thus there is a natural map :math:`\Phi : \pi_1(X, x_0)\rightarrow [S^1,X]`
obatined by ignoring basepoints. Show that :math:`\Phi` is onto if :math:`X` is path-connected, and that
:math:`\Phi([f])=\Phi([g])` iff :math:`[f]` and :math:`[g]` are conjugate in :math:`\pi_1(X,x_0)`. Hence :math:`\Phi` induces a 
one-to-one correspondence between :math:`[S^1, X]` and the set of conjugacy classes in :math:`\pi_1(X)`, 
when :math:`X` is path-connected.

**7.** Define :math:`f:S^1 \times I \rightarrow S^1 \times I` by :math:`f(\theta , s) = (\theta + 2\pi s, s)`, so :math:`f` restricts to the identity
on the two boundary circles of :math:`S^1 \times I`. Show that :math:`f` is homotopic to the identity by
a homotopy :math:`f_t` that is stationary on one of the boundary circles, but not by any 
homotopy :math:`f_t` that is stationary on both boundary circles. [Consider what :math:`f` does to the 
path :math:`s \mapsto (\theta_0 ,s)` for fixed :math:`\theta_0 \in S^1`.]

**8.** Does :ref:`the Borsuk-Ulam theorem <theorem 1.9>` hold for torus? In other words, for every map
:math:`f:S^1 \times S^1 \rightarrow \mathbb{R}^2` must there exist :math:`(x,y) \in S^1 \times S^1` such that :math:`f(x,y) = f(-x,-y)`?

**9.** Let :math:`A_1,\, A_2,\, A_3` be compact sets in :math:`\mathbb{R}^3`. Use :ref:`the Borsuk-Ulam theorme <theorem 1.9>` to show
that there is one plane :math:`P \subset \mathbb{R^3}` that simultaneously divides each :math:`A_t` into two pieces of
equal measure.

**10.** From the isomorphism :math:`\pi_1(X \times Y, (x_0,y_0)) \approx \pi_1(X,x_0) \times \pi_1(Y,y_0)` it follows that 
loops in :math:`X \times \{y_0\}` and :math:`\{x_0\}\times Y` represent commuting elements of :math:`\pi_1(X \times Y, (x _0, y_0))`.
Construct an explicit homotopy demonstrating this.

**11.** If :math:`X_0` is the path-component of a space :math:`X` containing the basepoint :math:`x_0`, show that
the inclusion :math:`X_0 \hookrightarrow X` induces an isomorphism :math:`\pi_1(X_0, x_0) \rightarrow \pi_1(X,x_0)`.

**12.** Show that every homomorphism :math:`\pi_1(S^1) \rightarrow \pi_1(S^1)` can be realized as the induced
homomorphism :math:`\varphi_*` of a map :math:`\varphi:S^1\rightarrow S^1`.

**13.** Given a space :math:`X` and a path-connected subspace :math:`A` containing the basepoint :Math:`x_0`, 
show that the map :math:`\pi_1(A,x_0) \rightarrow \pi_1(X, x_0)` induced by the inclusion :math:`A \hookrightarrow X` is surjective
iff every path in :math:`X` with endpoints in :math:`A` is homotopic to a path in :math:`A`.

**14.** Show that the isomorphism :math:`\pi_1(X \times Y) \approx \pi_1(X) \times \pi_1(Y)` in :ref:`Proposition 1.12 <proposition 1.12>` is
given by :math:`[f] \mapsto (p_{1*}([f]), p_{2*}([f]))` where :math:`p_1` and :math:`p_2` are the projections of :math:`X \times Y`
onto its two factors.

.. container::

    .. image:: fig/ex-15.png
        :align: right
        :width: 40%

    **15.** Given a map :math:`f:X \rightarrow Y` and a path :math:`h:I \rightarrow X` 
    from :math:`x_0` to :math:`x_1`, show that :math:`f_* \beta_h = \beta_{fh} f_*` in the
    diagram at the right.


.. container:: no-margin

    **16.** Show that there are no retractions :math:`r: X \rightarrow A` in the following cases:

    .. image:: fig/ex-16.png
        :align: right
        :width: 30%

    |indent| \(a\) :math:`X=\mathbb{R}^3` with :math:`A` any subspace homeomorphic to :math:`S^1`.

    |indent| \(b\) :math:`X=S^1 \times D^2` with :math:`A` its boundary torus :math:`S^1 \times S^1`.

    |indent| \(c\) :math:`X=S^1 \times D^2` and :math:`A` the circle shown in the figure.

    |indent| \(d\) :math:`X=D^2 \vee D^2` with :math:`A` its boundary :math:`S^1 \vee S^1`.

    |indent| \(e\) :math:`X` a disk with two points on its boundary identified and :math:`A` its boundary :math:`S^1 \vee S^1`.

    |indent| \(f\) :math:`X` the Möbius band and :math:`A` its boundary circle.

..

**17.** Construct infinitely many homotopic retractions :math:`S^1 \vee S^1 \rightarrow S^1`.

.. container:: no-margin

    **18.** Using :ref:`Lemma 1.15 <lemma 1.15>`, show that if a space :math:`X` is obtinaed from a path-connected
    subspace :math:`A` by attaching a cell :math:`e^n` with :math:`n \geq 2`, then the inclusion :math:`A \hookrightarrow X` induces a 
    surjection on :math:`\pi_1`. Apply this to show:

    |indent| \(a\) The wedge sum :math:`S^1 \vee S^2` has fundamental group :math:`\mathbb{Z}`.
    |indent| \(b\) For a path-connected CW complex :math:`X` the inclusion map :math:`X^1 \hookrightarrow X` of its :math:`1`-skeleton
    induces a surjection :math:`\pi_1(X^1) \rightarrow \pi_1(X)`. [For the case that :math:`X` has infinitely many 
    cells, see :ref:`Proposition A.1 <Proposition A.1>` in the :ref:`Appendix <Appendix>`.]

..

**19.** Show that if :math:`X` is a path-connected :math:`1`-dimensional CW complex with basepoint :math:`x_0`
a :math:`0`-cell, then every loop in :math:`X` is homotopic to a loop consisting of a finite sequence of 
edges traversed monotonically. [See the proof of :ref:`Lemma 1.15 <lemma 1.15>`. This exercise gives an 
elementary proof that :math:`\pi_1(S^1)` is cyclic generated by the standard loop winding once
around the circle. The more difficult part of the calculation of :math:`\pi_1(S^1)` is therefore the
fact that no iterate of this loop is nullhomotopic.]

**20.** Suppose :math:`f_t: X \rightarrow X` is homotopy such that :math:`f_0` and :math:`f_1` are each the identity map.
Use :ref:`Lemma 1.19` to show that for any :math:`x_0 \in X`, the loop :math:`f_t(x_0)` represents an element of 
the center of :math:`\pi_1(X, x_0)`. [One can interpret the result as saying that a loop represents 
an element of the center of :math:`\pi_1(X)` if it extends to a loop of maps :math:`X \rightarrow X`.]












.. |indent| raw:: html

    <span style="margin-left: 1em">