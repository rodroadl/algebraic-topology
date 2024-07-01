Two Criteria for Homotopy Equivalence
=====================================

Earlier in this chapter the main tool we used for constructing homotopy equivalences 
was the fact that a mapping cylinder deformation retracts onto its 'target' end. 
By repeated application of this fact one can often produce homotopy equivalences between 
rather different-looking spaces. However, this process can be a bit cumbersome
in practice, so it is useful to have other techniques available as well. We will describe 
two commonly used methods here. The first involves collapsing certain subspaces to 
points, and the second involves varying the way in whicn the parts of a space are put 
together.

Collapsing Subspaces
--------------------

The operation of collapsing a subspace to a point usually has a drastic effect 
on homotopy type, but one might hope that if the subspace being collapsed already 
has the homotopy type of a point, then collapsing it to a point might not change the 
homotopy type of the whole space. Here is a positive result in this direction:

    *If* :math:`(X,A)` *is a CW pair consisting of a CW complex* :math:`X` *and a contractible subcomplex* :math:`A`,
    *then the quotient map* :math:`X \rightarrow X/A` *is a homotopy equivalence.*

A proof will be given later in Proposition 0.17, but for now let us look at some examples 
showing how this result can be applied.

.. container:: no-indent-no-margin

    .. Example 0.7:

    **Example 0.7: Graphs**. The three graphs |three-graphs| are homotopy equivalent since 
    each is a deformation retract of a disk with two holes, but we can also deduce this 
    from the collapsing criterion above since collapsing the middle edge of the first and 
    third graphs produces the second graph.

.. container:: no-margin

    More generally, suppose :math:`X` is any graph with finitely many vertices and edges. If 
    the two endpoints of any edge of :math:`X` are distinct, we can collapse this edge to a point, 
    producing a homotopy equivalent graph with one fewer edge. This simplification can 
    be repeated until all edges of :math:`X` are loops, and then each component of :math:`X` is either 
    an isolated verte or a wedge sum of circles.

This raises the question of whether two such graphs, having only one vertex in 
each component, can be homotopy equivalent if they are not in fact just isomorphic 
graphs. Exercise 12 at the end of the chapter reduces the question to the case of 
connected graphs. Then the task is to prove that a wedge sum :math:`\bigvee_m S^1` of :math:`m` circles is not 
homotopy equivalent to :math:`\bigvee_n S^1` if :math:`m \neq n`. This sort of thing is hard to do directly. What 
one would like is some sort of algebraic object associated to spaces, depending only 
ontheir homotopy type, and taking different values for :math:`\bigvee_m S^1` has Euler characteristic :math:`1-m`. But it 
is a rather nontrivial theorem that the Euler characteristic of a space depends only on 
its homotopy type. A different algebraic invariant that works equally well for graphs, 
and whose rigorous development requires less effort than the Euler characteristic, is 
the fundamental group of a space, the subject of Chapter 1.

.. image:: fig/example0-8.png
    :align: right
    :width: 40%

.. _Example 0.8:

.. container:: no-indent

    **Example 0.8**. Consider the space :math:`X` obtained
    from :math:`S^2` by attaching the two ends of an arc 
    :math:`A` to two distinct points on the sphere, say the 
    north and south poles. Let :math:`B` be an arc in :math:`S^2`
    joining the two points where :math:`A` attaches. Then 
    :math:`X` can be given CW complex structure with 
    the two endpoints of :math:`A` and :math:`B` as :math:`0`-cells, the 
    interiors of :math:`A` and :math:`B` as :math:`1`-cells, and the rest of
    :math:`S^2` as a :math:`2`-cell. Since :math:`A` and :math:`B` are contractible, 
    :math:`X/A` and :math:`X/B` are homotopy equivalent to :math:`X`. The space :math:`X/A` is the quotient :math:`S^2/S^0`,
    the sphere with two potins identified, and :math:`X/B` is :math:`S^1 \vee S^2`. Hence :math:`S^2 / S^0` and :math:`S^1 \vee S^2`
    are homotopy equivalent, a fact which may not be entirely obvious at first glance.

.. _Example 0.9:

.. container:: no-indent

    **Example 0.9**. Let :math:`X` be the union of a torus with :math:`n` meridional disks. To obtain 
    a CW structure on :math:`X`, choose a longitudinal circle in the torus, intersecting each of 
    the meriodional disks in one point. These intersection points are then the :math:`0`-cells, the 
    :math:`1`-cells are the rest of the longitudinal circle and the boundary circles of the meridional 
    disks, and the :math:`2`-cells are the remaining regions of the torus and the interiors of 
    the meridional disks. Collapsing each meridional disk to a point yields a homotopy 
    equivalent space :math:`Y` consisting of :math:`n` :math:`2`-spheres, each tangent to its two neighbors, a 
    'necklace with :math:`n` beads'.

    .. image:: fig/example0-9.png
        :width: 100%
        :align: center

    The third space :math:`Z` in the figure, a strand of :math:`n` beads with a 
    string joining its two ends, collapses to :math:`Y` by collapsing the string to a point, so this 
    collapse is a homotopy equivalence. Finally, by collapsing the arc in :math:`Z` formed by the 
    front halves of the equators of the :math:`n` beads, we obtain the fourth spae :math:`W`, a wedge 
    sum of :math:`S^1` with :math:`n` :math:`2`-spheres. (One can see why a wedge sum is sometimes a called a 
    'bouquet' in the older literature.)

.. _Example 0.10:

.. container:: no-indent-no-margin

    **Example 0.10: Reduced Suspension**. Let :math:`X` be a CW complex and :math:`x_0 \in X` a :math:`0`-cell.
    Inside the suspension :math:`SX` we have the line segment :math:`\{x_0\} \times I`, and collapsing this to a 
    point yields a space :math:`\sum X` homotopy equivalent to :math:`SX`, called the **reduced suspension** 
    of :math:`X`. For example, if we take :math:`X` to be :math:`S^1 \vee S^1` with :math:`x_0` the intersection point of the 
    two circles, then the ordinary suspension :math:`SX` is the union of two spheres intersecting 
    along the arc :math:`\{x_0\} \times I`, so the reduced suspension :math:`\sum X` is :math:`S^2 \vee S^2`, a slightly simpler 
    space. More generally we have :math:`\sum(X \vee Y) = \sum X \vee \sum Y` for arbitrary CW complexes :math:`X` 
    and :math:`Y`. Another way in which the reduced suspension :math:`\sum X` is slightly simpler than :math:`SX` 
    is in its CW structure. In :math:`SX` there are two :math:`0`-cells (the two suspension points) and an 
    :math:`(n+1)`-cell :math:`e^n \times (0,1)` for each :math:`n`-cell of :math:`X` other than the :math:`0`-cell :math:`x_0`.

The reduced suspension :math:`\sum X` is actually the same as the smash product :math:`X \wedge S^1` 
since both spaces are the quotinet of :math:`X \times I` with :math:`X \times \partial I \cup \{x_0\}\times I` collapsed to a point.

Attaching Spaces 
------------------

Another common way to change a space without changing its homotopy type involves 
the idea of continuously varying how its parts are attached together. A general 
definition of 'attaching one space to another' that includes the case of attaching cells 
is the following. We start with a space :math:`X_0` and another space :math:`X_1` that we wish to 
attach to :math:`X_0` by identifying the points in a subspace :math:`A \subset X_1` with points of :math:`X_0`. The 
data needed to do this is a map :math:`f: A \rightarrow X_0`, for then we can form a quotient space 
of :math:`X_0 \sqcup x_1` by identifying each point :math:`a \in A` with its image :math:`f(a) \in X_0`. Let us 
denote this quotient space by :math:`X_0 \cup_f X_1`, the space :math:`X_0` with :math:`X_1` **attached along** :math:`\mathbf{A}` via :math:`\mathbf{f}`.
When :math:`(X_1, A)=(D^n, S^{n-1})` we have the case of attaching an :math:`n`-cell to :math:`X_0` via a map 
:math:`f:S^{n-1} \rightarrow X_0`.

Maping cylinders are examples of this construction, since the mapping cylinder 
:math:`M_f` of a map :math:`f:X \rightarrow Y` is the space obtained from :math:`Y` by attaching :math:`X \times I` along :math:`X \times \{1\}`
via :math:`f`. 

.. image:: fig/attaching-spaces.png
    :width: 30%
    :align: right

Closely related to the mapping cylinder :math:`M_f` is the **mapping cone** :math:`C_f = y \sqcup_f CX` 
where :math:`CX` is the cone :math:`(X \times I) / (X \times \{0\})` and we attach this to :math:`Y` 
along :math:`X \times \{1\}` via the identifications :math:`(x,1) \sim f(x)`. For 
example, when :math:`X` is a sphere :math:`S^{n-1}` the mapping cone :math:`C_f` is the space 
obtained from :math:`Y` by attaching an :math:`n`-cell via :math:`f:S^{n-1} \rightarrow Y`. A 
mapping cone :math:`C_f` can also be viewed as the quotient :math:`M_f/X` of 
the mapping cylinder :math:`M_f` with the subspace :math:`X=X\times \{0\}` collapsed to a point.

If one varies an attaching map :math:`f` by a homotopy :math:`f_t`, one gets a family of spaces 
whose shape is undergoing a continuous change, it would seem, and one might expect 
these spaces all to have the same homotopy type. This is often the case:

    *If* :math:`(X_1, A)` *is a CW pair and the two attaching maps* :math:`f,g:A \rightarrow X_0` *are homotopic, then*
    :math:`X_0 \sqcup_f X_1 \simeq X_0 \sqcup_g X_1`.

Again let us defer the proof and look at some examples.

.. container:: no-indent

    .. _Example 0.11:

    **Example 0.11**. Let us rederive the result in :hoverxref:`Example 0.8 <mathjax:Example 0.8>` that a sphere with two points 
    identified is homotopy equivalent to :math:`S^1 \vee S^2`. The sphere 

.. |three-graphs| image:: fig/three-graphs.png
    :scale: 5%