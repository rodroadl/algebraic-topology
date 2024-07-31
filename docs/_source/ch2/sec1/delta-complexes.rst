:math:`\Delta`-Complexes
===============================================

|indent| The torus, the projective plane, and the Klein bottle can each be obtained from a 
square by identifying opposite edges in the way indicated by the arrows in the following
figures:

.. image:: fig/squares.png
    :width: 100%
    :align: center

.. image:: fig/polygon.png
    :width: 25%
    :align: right

Cutting a square along a diagonal produces two triangles, so each of these surfaces
can also be built from two triangles by identifying their edges in pairs. In similar
fashion a polygon with any number of sides can be cut along
diagonals into triangles, so in fact all closed surfaces can be
constructed from triangles by identifying edges. Thus we have
a single building block, the triangle, from which all surfaces can
be constructed. Using only triangles we could also construct a 
large class of :math:`2`-dimensional spaces that are not surfaces in the
strict sense, by allowing more than two edges to be identified
together at a time.

.. image:: fig/n-simplex.png
    :align: right
    :width: 50%

.. image:: fig/standard-n-simplex.png
    :align: right
    :width: 20%

|indent| The idea of a :math:`\Delta`-complex is to generalize constructions like these to any number
of dimensions. The :math:`n`-dimensional analog of the triangle is the :math:`n`-**simplex**. This is the
smallest convex set in a Euclidean space
:math:`\mathbb{R}^m` containing :math:`n+1` points :math:`v_0,\cdots,v_n`
that do not lie in a hyperplane of dimension
less than :math:`n`, where by a hyperplane
we mean the set of solutions of a system
of linear equations. An equivalent
condition would be that the difference vectors
:math:`v_1-v_0,\cdots,v_n-v_0` are linearly independent. The points :math:`v_i` are the **vertices** of the
simplex, and the simplex itself is denoted :math:`[v_0,\cdots,v_n]`. For 
example, there is the standard :math:`n`-simplex

.. math::

    \Delta^n=\{(t_0,\cdots,t_n)\in \mathbb{R}^{n+1} \mid \sum_i t_i = 1 \text{ and } t_i \geq 0 \text{ for all }i\}

whose vertices are the unit vectors along the coordinate axes.

|indent| For purposes of homology it will be important to keep track of the order of the
vertices of a simplex, so ':math:`n`-simplex' will really menal ':math:`n`-simplex with an ordering
of its vertices'. A by-product of ordering the vertices of a simplex :math:`[v_0,\cdots, v_n]` is 
that this determines orientations of the edges :math:`[v_i,v_j]` according to increasing 
subscripts, as shown in the two preceding figures. Specifying the ordering of the vertices
also determines a canonical linear homeomorphism from the standard :math:`n`-simplex
:math:`\Delta^n` onto any other :math:`n`-simplex :math:`[v_0,\cdots , v_n]`, preserving the order of vertices, namely,
:math:`(t_0,\cdots,t_n)\mapsto\sum_it_iv_i`. The coefficients :math:`t_i` are the **barycentric coordinates** of the point
:math:`\sum_it_iv_i` in :math:`[v_0,\cdots,v_n]`.

|indent| If we delete one of the :math:`n+1` vertices of an :Math:`n`-simplex :math:`[v_0,\cdots,v_n]`, then the
remaining :math:`n` vertices span an :math:`(n-1)`-simplex, called a **face** of :math:`[v_0,\cdots,v_n]`. We
adopt the following convention:

    *The vertices of a face, or of any subsimplex spanned by a subset of the vertices,
    will always be ordered according to their order in the larger simplex.*

The union of all the faces of :math:`\Delta^n` is the **boundary** of :Math:`\Delta^n`, written :math:`\partial \Delta^n`. The **open
simplex** :math:`\mathring{\Delta}^n` is :math:`\Delta^n-\partial \Delta^n`, the interior of :math:`\Delta^n`.

|indent| A :math:`\mathbf{\Delta}`-**complex** structure on a space :math:`X` is a collection of maps :math:`\sigam_\alpha:\Delta^n \rightarrow X`, with :math:`n`
depending on the index :math:`\alpha`, such that:


.. _delta-complex-condition-i:
(i) The restriction :math:`\sigma_\alpha\mid\mathring{\Delta}^n` is injective, and each point of :maht:`X` is in the image of exactly
    one such restriction :math:`\sigma_\alpha\mid\mathring{\Delta}^n`.
.. _delta-complex-condition-ii:
(ii)    Each restriction of :math:`\sigma_\alpha` to a face of :math:`\Delta^n` is one of the maps :math:`\sigma_\beta:\Delta^{n-1}\rightarrow X`. Here we
        are identifying of :Math:`\sigma_\alpha` to a face of :math:`\Delta^n` is one of the maps :math:`\sigma_\beta:\Delta^{n-1}\rightarrow X`. Here we
        are identifying the face of :math:`\Delta^n` with :math:`\Delta^{n-1}` by the canonical linear homeomorphism
        between them that preserves the ordering of the vertices.
.. _delta-complex-condition-iii:
(iii)   A set :math:`A\subset X` is open iff :math:`\sigma^{-1}_\alpha (A)` is open in :math:`\Delta^n` for each :math:`\sigma_\alpha`.

Among other things, this last condition rules out trivialities like regarding all the 
points of :math:`X` as individual vertices. The earlier decompositions of the torus, projective
plane, and Klein bottle into two triangles, three edges, and one or two vertices define
:math:`\Delta`-complex structures with a total of six :math:`\sigma_\alpha`'s for the torus and Klein bottle and seven
for the projective plane. The orientations on the edges in the pictures are compatible
with a unique ordering of the vertices of each simplex, and these orderings determine
the maps :math:`\sigma_\alpha`.

|indent|A consequence of :ref:`(iii) <delta-complex-condition-iii>` is that :math:`X` can be built as a quotient space of a collection
of disjoint simplices :math:`\Delta^n_\alpha`, one for each :math:`\sigma_\alpha:\Delta^n \rightarrow X`, the quotient space obtained by
identifying each face of a :math:`\Delta^n_\alpha` with the :math:`\Delta^{n-1}_\beta` corresponding to the restriction :math:`\sigma_\beta` of
:math:`\sigma_\alpha` to the face in question, as in condition :ref:`(ii) <delta-complex-condition-ii>`. One can think of building the quotient
space inductively, starting with a discrete set of vertices, then attaching edges to
tehse to produce a graph, then attaching :math:`2`-simplices to the graph, and so on. From
this viewpoint we see that the data specifying a :math:`\Delta`-complex can be described purely
combinatorially as collections of :math:`n`-simplices :math:`\Delta^n_\alpha` for each :math:`n` together wit hfunctions
associating to each face of each :math:`n`-ximples :math:`\Delta^n_\alpha` an (:math:`n-1`)-simplex :math:`\Delta^{n-1}_\beta`.

|indent| More generally, :math:`\Delta`-complexes can be built from collections of disjoint simplices by
identifying various subsimplices spanned by subsets of the vertices, where the identifications
are performed using the canonical linear homeomorphisms that preserve
the orderings of the vertices. The earlier :Math:`\Delta`-complex structures on a torus, projective
plane, or Klein bottle can be obtained in this way, by identifying pairs of edges of
two :math:`2`-simplices. If one starts with a single :math:`2`-simplex and identifies all three edges
to a single edge, preserving the orientations given by the ordering of the vertices,
this produces a :math:`\Delta`-complex known as the 'dunce hat'. By contrast, if the three edges
of a :math:`2`-simplex are identified preserving a cyclic orientation of the three edges, as in
the first figure at the right, this does not produce a 
:math:`\Delta`-compelx structure, although if the :math:`2`-simplex is
subdivided into three smaller :Math:`2`-simplices about a
central vertex, then one does obtain a :math:`\Delta`-complex
structure on the quotient space.

|indent| Thinking of a :Math:`\Delta`-complex :math:`X` as a quotient space of a collection of disjoint simplices,
it is not hard to see that :math:`X` must be a Hausdorff space. :ref:`Condition (iii) <delta-complex-condition-iii>` then
implies that each restriction :math:`\sigma_\alpha \mid \mathring{\Delta}^n` is a homeomorphism onto its image, which is
thus an open simplex in :math:`X`. It follows from :ref:`Proposition A.2 <Proposition A.2>` in the Appendix that
these open simplicies :math:`\sigma_\alpha(\mathring{\Delta}^n)` are the cells :math:`e^n_\alpha` of a CW complex structure on :math:`X` with
the :math:`\sigma_\alpha`'s as characteristic maps. We will not need this fact at present, however.

.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>