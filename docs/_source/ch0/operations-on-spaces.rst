Operations on Spaces
====================

Cell complexes have a very nice mixture of rigidity and flexibility, with enough 
rigidity to allow many arguments to proceed in a combinatorial cell-by-cell fashion 
and enough flexibility to allow many natural constructions to be performed on them. 
Here are some of those constructions. 

.. container:: no-indent

    **Products**. If :math:`X` and :math:`Y` are cell complexes, then :math:`Y \times Y` has the structure of a cell 
    complex with cells the products :math:`e^m_\alpha \times e^n_\beta` where :math:`e^m_\alpha` ranges over the cells of :math:`X` and 
    :math:`e^n_\beta` ranges over the cells of :math:`Y`. For example, the cell structure on the torus :math:`S^1 \times S^1` 
    described at the beginning of this section is obtained in this way from the standard 
    cell structure on :math:`S^1`. For completely general CW complexes :math:`X` and :math:`Y` there is one 
    small complication: The topology on :math:`X \times Y` as a cell complex is sometimes finer than
    the prouct topology, with more open sets than the product topology has, though the 
    two topologies coincide if either :math:`X` or :math:`Y` has only finitely many cells, or if both :math:`X` 
    and :math:`Y` have countably many cells. This is explained in the Appendix. In practice this 
    subtle issue of point-set topology rarely causes problems, however.

.. container:: no-indent-no-margin

    **Quotients**. If :math:`(X,A)` is a CW pair consisting of a cell complex :math:`X` and a subcomples :math:`A`, 
    then the quotient space :math:`X / A` inherits a natural cell complex structure from :math:`X`. The 
    cells of :math:`X/A` are the cells of :math:`X-A` plus one new :math:`0`-cell, the image of :math:`A` in :math:`X/A`. For a 
    cell :math:`e^n_\alpha` of :math:`X-A` attached by :math:`\varphi_\alpha : S^{n-1} \rightarrow X^{n-1}`, the attaching map for the corresponding 
    cell in :math:`X/A` is the composition :math:`S^{n-1} \rightarrow X^{n-1}\rightarrow X^{n-1}/A^{n-1}`.

For example, if we give :math:`S^{n-1}` any cell structure and build :math:`D^n` from :math:`S^{n-1}` by attaching 
an :math:`n`-cell, then the quotient :math:`D^n / S^{n-1}` is :math:`S^n` with its usual cell structure. As another 
example, take :math:`X` to be a closed orientable surface with the cell structure described at 
the beginning of this section, with a single :math:`2`-cell, and let :math:`A` be the complement of this 
:math:`2`-cell, the :math:`1`-skeleton of :math:`X`. Then :math:`X/A` has a cell structure consisting of a :math:`0`-cell with 
a :math:`2`-cell attached, and there is only one way to attach a cell to a :math:`0`-cell, by the constant 
map, so :math:`X/A` is :math:`S^2`.

.. image:: fig/suspension.png
    :scale: 20% 
    :align: right

.. container:: no-indent-no-margin

    **Suspension**. For a space :math:`X`, the **suspension** SX is the quotient of 
    :math:`X \times I` obtained by collapsing :math:`X\times\{0\}` to one point and :math:`X\times\{1\}` to another 
    point. The motivating example is :math:`X=S^n`, when :math:`SX=S^{n+1}` 
    with the two 'suspension points' at the north and south poles of 
    :math:`S^{n+1}`, the points :math:`(0, \cdots, 0, \pm 1)`. One can regard :math:`SX` as a double cone
    on :math:`X`, the union of two copies ofthe **cone** :math:`CX=(X\times I) / (X\times \{0\})`. If :math:`X` is a CW complex,
    so are :math:`SX` and :math:`CX` as aquotients of :math:`X \times I` with its product cell structure, :math:`I` being 
    given the standard cell structure of two :math:`0`-cells joined by a :math:`1`-cell.

Suspension becomes increasingly important the farther one goes into algebraic 
topology, though why this should be so is certainly not evident in advance. One 
especially useful property of suspension is that not only spaces but also maps can be 
suspended. Namely, a mpa :math:`f:X\rightarrow Y` suspends to :math:`Sf:SX \rightarrow SY`, the quotient map of 
:math:`f\times \mathbb{1}: X \times I \rightarrow Y \times I`.

.. container:: no-indent-no-margin

    **Join**. The cone :math:`CX` is the union of all line segments joining points of :math:`X` to an external 
    vertex, and similarly the suspension :math:`SX` is the union of all line segments joining 
    points of :math:`x` to two external vertices. More generally, given :math:`X` and a second space :math:`Y`, 
    one can define the space of all line segments joining points in :math:`X` to points in :math:`Y`. This 
    is the **join** :math:`X * Y`, the quotient space of :math:`X \times Y \times I` under the identifications :math:`(x, y_1, 0) \sim (x, y_2, 0)` 
    and :math:`(x_1,y,1) \sim (x_2, y, 1)`. Thus we are collapsing the subspace :math:`X \times Y \times \{0\}`
    to :math:`X` and :math:`X \times Y \times \{1\}` to :math:`Y`.

    .. image:: fig/join.png
        :align: right
        :width: 40%
    
    For example, if :math:`X` and :math:`Y` are both closed intervals, then we 
    are collapsing two opposite faces of a cube 
    onto line segments so that the cube becomes 
    a tetrahedron. In the general case, :math:`X * Y` 
    contains copies of :math:`X` and :math:`Y` at its two ends,
    and every other point :math:`(x,y,t)` in :math:`X * Y` is on a unique line segment joining the point 
    :math:`x \in X \subset X*Y` to the point :math:`y \in Y \subset X*Y`, the segment obtained by fixing :math:`x` and :math:`y`
    and letting the coordinate :math:`t` in :math:`(x,y,t)` vary.

A nice way to write points of :math:`X * Y` is as formal linear combinations :math:`t_1x+t_2y` 
with :math:`0 \leq t_i \leq 1` and :math:`t_1 + t_2 = 1`, subject to the rules :math:`0x+1y=y` and :math:`1x+0y=x` 
that correspond exactly to the identifications defining :math:`X*Y`. In much the same 
way, an iterated join :math:`X_1 * \cdots X_n` can be constructued as the space of formal linear 
combinations :math:`t_1x_1+\cdots t_nx_n` with :math:`0\leq t_i \leq 1` and :math:`t_1 + \cdots +t_n=1`, with the 
convenction that terms :math:`0x_i` can be omitted. A very special case that plays a central
role in algebraic topology is when each :math:`X_i` is just a point. For example, the join of 
two points is a line segment, the join of three points is a triangle, and the join of four 
points is a tetrahedron. In general, the join of :math:`n` points is a convex polyhedron of 
dimension :math:`n-1` is called a **simplex**. Concretely, if the :math:`n` points are the :math:`n` standard 
basis vectors for :math:`\mathbb{R}^n`, then their join is the :math:`(n-1)`-dimensional simplex

.. math::
    
    \Delta^{n-1}=\{(t_1, \cdots , t_n) \in \mathbb{R}^n | t_1 + \cdots + t_n = 1 \text{ and } t_i \geq 0\}

.. container:: no-indent-no-margin

    Another interesting examples is when each :math:`X_i` is :math:`S^0`, two points. If we take the two 
    points of :math:`X_i` to be the two unit vectors along the :math:`i^{th}` coordinate axis in :math:`\mathbb{R}^n`, then the 
    join :math:`X_1 * \cdots *X_n` is the union of :math:`2^n` copies of the simplex :math:`\Delta^{n-1}`, and radial projection 
    from the origin gives a homeomorphism between :math:`X_1 * \cdots X_n` and :math:`S^{n-1}`.

If :math:`X` and :math:`Y` are CW complexes, then there is a natural CW structure on :math:`X*Y` 
having the subspaces :math:`X` and :math:`Y` as subcomplexes, with the remaining cells being the 
product cells of :math:`X \times Y \times (0,1)`. As usual with products, the CW topology on :math:`X * Y` may 
be finer than the quotient of the product topology on :math:`X \times Y \times I`.

.. _Wedge Sum:

.. container:: no-indent-no-margin

    **Wedge Sum**. This is a rather trivial but still quite useful operation. Given spaces :math:`X` and 
    :math:`Y` with chosen points :math:`x_0 \in X` and :math:`y_0 \in Y`, then the **wedge sum** :math:`X \vee Y` is the quotient
    of the disjoint union :math:`X \sqcup Y` obtained by identifying :math:`x_0` and :math:`y_0` to a single point. For 
    example, :math:`S^1 \vee S^1` is homeomorphic to the figure ':math:`8`', two circles touching at a point. 
    More generally one could form the wedge sum :math:`\bigvee _\alpha X_\alpha` of an arbitrary collection of 
    spaces :math:`X_\alpha` by starting with the disjoint union :math:`\bigsqcup _\alpha X_\alpha` and identifying points :math:`x_\alpha \in X_\alpha`
    to a single point. In case the spaces :math:`X_\alpha` are cell complexes and the points :math:`x_\alpha` are 
    :math:`0`-cells, then :math:`\bigvee_\alpha X_\alpha` is a cell complex since it is obtained from the cell complex :math:`\bigsqcup_\alpha X_\alpha`
    by collapsing a subcomplex to a point.

For any cell complex :math:`X`, the quotient :math:`X^n / X^{n-1}` is a wedge sum of :math:`n`-spheres :math:`\bigvee_\alpha S^n_\alpha`, 
with one sphere for each :math:`n`-cell of :math:`X`.

.. container:: no-indent-no-margin

    **Smash Product**. Like suspension, this is another construction whose importance becomes 
    evident only later. Inside a product space :math:`X \times Y` there are copies of :math:`X` and :math:`Y`,
    namely :math:`X \times \{y_0\}` and :math:`\{x_0\} \times Y` for points :math:`x_0 \in X` and :math:`y_0 \in Y`. These two copies of :math:`X`
    and :math:`Y` in :math:`X \times Y` intersect only at the point :math:`(x_0, y_0)`, so their union can be identified 
    with the wedge sum :math:`X \vee Y`. The **smash product** :math:`X \wedge Y` is then defined to be the quotient 
    :math:`X \times Y / X \vee Y`. One can think of :math:`X \wedge Y` as a reduced version of :math:`X \times Y` obtained 
    by collapsing away the parts that are not genuinely a product, the separate factors :math:`X` and :math:`Y`.

The smash product :math:`X \wedge Y` is a cell complex if :math:`X` and :math:`Y` are cell complexes with :math:`x_0` 
and :math:`y_0` :math:`0`-cells, assuming that we give :math:`X \times Y` the cell-complex topology rather than the 
product topology in cases when these two topologies differ. For example, :math:`S^m \wedge S^n` has 
a cell structure with just two cells, of dimensions :math:`0` and :math:`m+n`, hence :math:`S^m \wedge S^n = S^{m+n}`.
In particular, when :math:`m=n=1` we see that collapsing longitude and meridian circles 
of a torus to a point produces a :math:`2`-sphere.
