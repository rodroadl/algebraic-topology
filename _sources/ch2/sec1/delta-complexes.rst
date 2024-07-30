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

    **The vertices of a face, or of any subsimplex spanned by a subset of the vertices,
    will always be ordered according to their order in the larger simplex.

The union of all the faces of :math:`\Delta^n` is the **boundary** of :Math:`\Delta^n`, written :math:`\partial \Delta^n`. The **open
simplex**

.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>