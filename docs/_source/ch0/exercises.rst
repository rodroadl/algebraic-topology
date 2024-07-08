Exercises
================

.. _ex-0-0-01: 

.. container:: no-indent

    **1.** Construct an explicit deformation retraction of the torus with one point deleted 
    onto a graph consisting of two circles intersecting in a point, namely, longitude and 
    meridian circles of the torus.

.. _ex-0-0-02:

.. container:: no-indent
    
    **2.** Construct an explicit deformation retraction of :math:`\mathbb{R}^n-\{0\}` onto :math:`S^{n-1}`.

.. _ex-0-0-03:

.. container:: no-indent

    **3.** (a) Show that the composition of homotopy equivalences :math:`X \rightarrow Y` and :math:`Y\rightarrow Z` is a 
    homotopy equivalence :math:`X\rightarrow Z`. Deduce that homotopy equivalence is an equivalence relation.

    \(b\) Show that the relation of homotopy among maps :math:`X \rightarrow Y` is an equivalence relation.

    \(c\) Show that a map homotopic to a homotopy equivalence is a homotopy equivalence.

.. _ex-0-0-04:

.. container:: no-indent

    **4.** A **deformation retraction in the weak sense** of a space :math:`X` to a subspace :math:`A` is a 
    homotopy :math:`f_t : X\rightarrow X` such that :math:`f_0 = \mathbb{1}, \, f_1(X) \subset A`, and :math:`f_t(A) \subset A` for all :math:`t`. Show 
    that if :math:`X` deformation retracts to :math:`A` in this weak sense, then the inclusion :math:`A \hookrightarrow X` is 
    a homotopy equivalence.

.. _ex-0-0-05:

.. container:: no-indent

    **5.** Show that if a space :math:`X` deformation retracts to a point :math:`x \in X`, then for each 
    neighborhood :math:`U` of :math:`x` in :math:`X` there exists a neighborhood :math:`V \subset U` of :math:`x` such that the 
    inclusion map :math:`V \hookrightarrow U` is nullhomotopic.

.. _ex-0-0-06:

.. container:: no-indent

    .. image:: fig/ex-06-a.png
        :width: 20%
        :align: right

    **6.** (a) Let :math:`X` be the subspace of :math:`\mathbb{R}^2` consisting of the horizontal segment 
    :math:`[0,1] \times \{0\}` together with all the vertical segments :math:`\{r\} \times [0,1-r]` for 
    :math:`r` a rational number in :math:`[0,1]`. Show that :math:`X` deformation retracts to 
    any point in the segment :math:`[0,1] \times \{0\}`, but not to any other point. [See 
    the preceding problem.]

    \(b\) Let :math:`Y` be the subspace of :math:`\mathbb{R}^2` that is the union of an infinite number of copies of :math:`X`
    arranged as in the figure below. Show that :math:`Y` is contractible but does not deformation 
    retract onto any point.

    .. image:: fig/ex-06-b.png
        :width: 100%
        :align: center

    \(c\) Let :math:`Z` be the zigzag subspace of :math:`Y` homeomorphic to :math:`\mathbb{R}` indicated by the heavier 
    line. Show there is a deformation retraction in the weak sense (see :ref:`Exercise 4 <ex-0-0-04>`) of :math:`Y` 
    onto :math:`Z`, but no true deformation retraction.

.. _ex-0-0-07:

.. container:: no-indent

    .. image:: fig/ex-07.png
        :width: 40%
        :align: right

    **7.** Fill in the details in the following construction from 
    [Edwards 1999] of a compact space :math:`Y \subset \mathbb{R}^3` with the 
    same properties as the space :math:`Y` in :ref:`Exercise 6 <ex-0-0-06>`, that is, :math:`Y`
    is contractible but does not deformation retract to any 
    point. To begin, let :math:`X` be the union of an infinite sequence
    of cones on the Cantor set arranged end-to-end, 
    as in the figure. Next, form the one-point compactification
    of :math:`X \times \mathbb{R}`. This embeds in :math:`\mathbb{R}^3` as a closed disk with curved 'fins' attached along
    circular arcs, and with the one-point compactification of :math:`X` as a cross-sectional slice. 
    The desired space :math:`Y` is then obtained from this subspace of :math:`\mathbb{R}^3` by wrapping one more 
    cone on the Cantor set around the boundary of the disk.

.. _ex-0-0-08:

.. container:: no-indent

    **8.** For :math:`n > 2`, construct an :math:`n`-room analog of the house with two rooms.

.. _ex-0-0-09:

.. container:: no-indent

    **9.** Show that a retract of a contractible space is contractible.

.. _ex-0-0-10:

.. container:: no-indent

    **10.** Show that a space :math:`X` is contractible iff every map :math:`f:X \rightarrow Y`, for arbitrary :math:`Y`, is 
    nullhomotopic. Similarly, show :math:`X` is contractible iff every map :math:`f: Y \rightarrow X` is nullhomotopic.

.. _ex-0-0-11:

.. container:: no-indent

    **11.** Show that :math:`f:X \rightarrow Y` is a homotopy equivalence if there exist maps :math:`g,h:Y \rightarrow X`
    such that :math:`fg \simeq \mathcal{1}` and :math:`hf \simeq \mathbb{1}`. More generally, show that :math:`f` is a homotopy equivalence 
    if :math:`fg` and :math:`hf` are homotopy equivalences.

.. _ex-0-0-12:

.. container:: no-indent

    **12.** Show that a homotopy equivalence :math:`f:X\rightarrow Y` induces a bijection between the set 
    of path-components of :math:`X` and the set of path-components of :math:`Y`, and that :math:`f` restricts to 
    a homotopy equivalence from each path-component of :math:`X` to the corresponding path 
    component of :math:`Y`. Prove also the corresponding statements with components instead 
    of path-components. Deduce that if the components of a space :math:`X` coincide with its 
    path-components, then the same holds for any space :math:`Y` homotopy equivalent to :math:`X`.

.. _ex-0-0-13:

.. container:: no-indent

    **13.** Show that any two deformation retractions :math:`r^0_t` and :math:`r^1_t` of a space :math:`X` onto a 
    subspace :math:`A` can be joined by a continuous family of deformation retractions :math:`r^s_t`,
    :math:`0 \leq s \leq 1`, of :math:`X` onto :math:`A`, where continuity means that the map :math:`X \times I \times I \rightarrow X` sending
    :math:`(x,s,t)` to :math:`r^s_t(x)` is continuous.

.. _ex-0-0-14:

.. container:: no-indent

    **14.** Given positive integers :math:`v, \, e`, and :math:`f` satisfying :math:`v-e+f = 2`, constructy a cell 
    structure on :math:`S^2`  having :math:`v` :math:`0`-cells, :math:`e` :math:`1`-cells, and :math:`f` :math:`2`-cells.

.. _ex-0-0-15:

.. container:: no-indent

    **15.** Enumerate all the subcomplexes of :math:`S^{\infty}`, with the cell structure on :math:`S^\infty` that has :math:`S^n`
    as its :math:`n`-skeleton.

.. _ex-0-0-16:

.. container:: no-indent

    **16.** Show that :math:`S^\infty` is contractible.

.. _ex-0-0-17:

.. container:: no-indent

    **17.** (a) Show that the mapping cylinder of every map :math:`f:S^1 \rightarrow S^1` is a CW complex.

    \(b\) Construct a :math:`2`-dimensional CW complex that contains both an  annulus :math:`S^1 \times I` and 
    
    a Möbius band as deformation retracts.

.. _ex-0-0-18:

.. container:: no-indent

    **18.** Show that :math:`S^1 * S^1 = S^3`, and more generally :math:`S^m * S^n = S^{m+n+1}`.

.. _ex-0-0-19:

.. container:: no-indent

    **19.** Show that the space obtained from :math:`S^2` by attaching :math:`n` :math:`2`-cells along any collection
    of :math:`n` circles in :math:`S^2` is homotopy equivalent to the wedge sum of :math:`n+1` :math:`2`-spheres.

.. _ex-0-0-20:

.. container:: no-indent

    .. image:: fig/ex-20.png
        :align: right
        :width: 20%

    **20.** Show that the subspace :math:`X \subset \mathbb{R}^3` formed by a Klein bottle
    intersecting itself in a circle, as shown in the figure, is homotopy 
    equivalent to :math:`S^1 \vee S^1 \vee S^2`.

.. _ex-0-0-21:

.. container:: no-indent

    **21.** If :math:`X` is a connected Hausdorff space that is a union of a finite number of :math:`2`-spheres,
    any two of which intersect in at most one point, show that :math:`X` is homotopy equivalent 
    to a wedge sum of :math:`S^1`'s and :math:`S^2`'s.

.. _ex-0-0-22:

.. container:: no-indent

    **22.** Let :math:`X` be a finite graph lying in a half-plane :math:`P \subset \mathbb{R}^3` and intersecting the edge 
    of :math:`P` in a subset of the vertices of :math:`X`. Describe the homotopy type of the 'surface of 
    revolution' obtained by rotating :math:`X` about the edge line of :math:`P`.

.. _ex-0-0-23:

.. container:: no-indent

    **23.** Show that a CW complex is contractible if it is the union of two contractible 
    subcomplexes whose intersection is also contractible.

.. _ex-0-0-24:

.. container:: no-indent

    **24.** Let :math:`X` and :math:`Y` be CW complexes with :math:`0`-cells :math:`x_0` and :math:`y_0`. Show that the quotient
    spaces :math:`X * Y / (X *\{y_0\} \cup \{x_0\} *Y)` and :math:`S(X\wedge Y)/S(\{x_0\} \wedge \{y_0\})` are homeomorphic,
    and deduce that :math:`X * Y \simeq S (X \wedge Y)`.

.. _ex-0-0-25:

.. container:: no-indent

    **25.** If :math:`X` is a CW complex with components :math:`X_\alpha`, show that the suspension :math:`SX` is 
    homotopy equivalent to :math:`\bigvee_\alpha SX_\alpha` for some graph :math:`Y`. In the case that :math:`X` is a finite
    gprah, show that :math:`SX` is homotopy equivalent to a wedge sum of circles and :math:`2`-spheres.

.. _ex-0-0-26:

.. container:: no-indent

    **26.** Use :ref:`Corollary 0.20 <Corollary 0.20>` to show that if :math:`(X,A)` has the homotopy extension property,
    then :math:`X \times I` deformation retracts to :math:`X \times \{0\} \cup A \times I`. Deduce from this that 
    :ref:`Proposition 0.18 <Proposition 0.18>` holds more generally for any pair :math:`(X_1, A)` satisfying the homotopy extension
    property.

.. _ex-0-0-27:

.. container:: no-indent

    **27.** Given a pair :math:`(X,A)` and a homotopy equivalence :math:`f:A\rightarrow B`, show that the natural
    map :math:`X \rightarrow \sqcup_f X` is a homotopy equivalence if :math:`(X,A)` satisfies the homotopy extension 
    property. [Hint: Conisder :math:`X\cup M_f` and use the preceding problem.] An interesting 
    case is when :math:`f` is a quotient map, hence the map :math:`X \rightarrow B \sqcup_f X` is the quotient map
    identifying each set :math:`f^{-1}(b)` to a point. When :math:`B` is a point this gives another proof of 
    :ref:`Proposition 0.17 <Proposition 0.17>`.

.. _ex-0-0-28:

.. container:: no-indent

    **28.** Show that if :math:`(X_1, A)` satisfies the homotopy extension property, then so does every 
    pair :math:`(X_0 \sqcup_f X_1, X_0)` obtained by attaching :math:`X_1` to a space :math:`X_0` via a map :math:`f:A \rightarrow X_0`.

.. _ex-0-0-29:

.. container:: no-indent

    **29.** In case the CW complex :math:`X` is obtained from a subcomplex :math:`A` by attaching a single 
    cell :math:`e^n`, describe exactly what the extension of a homotopy :math:`f_t: A \rightarrow Y` to :math:`X` given by
    the proof of :ref:`Proposition 0.16 <proposition 0.16>` looks like. That is, for a point :math:`x \in e^n`, describe the path
    :math:`f_t(x)` for the extended :math:`f_t`.


