Exercises
====================

.. _Exercise 1-2-1:

**1.** Show that the free product :math:`G * H` of nontrivial groups :math:`G` and :math:`H` has trivial center,
and that the only elements of :math:`G *H` of finite order are the conjugates of finite-order
elements of :math:`G` and :math:`H`.

.. _Exercise 1-2-2:

**2.** Let :math:`X \subset \mathbb{R}^m` be the union of convex open sets :math:`X_1 \cdots X_n` such that :math:`X_i \cap X_j \cap X_k \neq \emptyset`
for all :math:`i,j,k`. Show that :math:`X` is simply-connected.

.. _Exercise 1-2-3:

**3.** Show that the complement of a finite set of points in :math:`\mathbb{R}^n` is simply-connected if 
:math:`n \geq 3`.

.. _Exercise 1-2-4:

**4.** Let :math:`X \subset \mathbb{R}^3` be the union of :math:`n` lines through the origin. Compute :math:`\pi_1(\mathbb{R}^3-X)`.

.. _Exercise 1-2-5:

**5.** Let :math:`X \subset \mathbb{R}^2` be a connected graph that is the union of a finite number of straight 
line segments. Show that :math:`\pi_1(X)` is free with a basis consisting of loops formed by 
suitably chosen paths in :math:`X`. [Assume the Jordan curve theorem for polygonal simple
closed curves, which is equivalent to the case that :math:`X` is homeomorphic to :math:`S^1`.]

.. _Exercise 1-2-6:

**6.** Use :ref:`Proposition 1.26 <Proposition 1.26>` to show that the complement of a closed discrete subspace
of :math:`\mathbb{R}^n` is simply-connected if :math:`n \geq 3`.

.. _Exercise 1-2-7:

**7.** Let :Math:`X` be the quotient space of :math:`S^2` obtained by identifying the north and south 
poles to a single point. Put a cell complex structure on :math:`X` and use this to compute
:math:`\pi_1(X)`.

.. _Exercise 1-2-8:

**8.** Compute the fundamental group of the space obtained from two tori :math:`S^1 \times S^1` by
identifying a circle :math:`S^1 \times \{x_0\}` in one torus with the corresponding circle :math:`S^1 \times \{x_0\}` in
the other torus.

.. _Exercise 1-2-9:

.. container::

    .. image:: fig/ex-1-2-9.png
        :align: right
        :width: 50%

    **9.** In the surface :math:`M_g` of genus :math:`g`, let
    :math:`C` be a circle that separates :math:`M_g` into
    two compact subsurfaces :math:`M_h'` and :math:`M_k'`
    obtained from the closed surfaces :math:`M_h` 
    and :math:`M_k` by deleting an open disk from
    each. Show that :math:`M_h'` does not retract onto its boundary circle :math:`C`, and hence :math:`M_g` does
    not retarct onto :math:`C`. [Hint: abelianize :math:`\pi_1`.] But show that :math:`M_g` does retract onto the
    nonseparating circle :math:`C'` in the figure.

.. _Exercise 1-2-10:

.. container::

    .. image:: fig/ex-1-2-10.png
        :align: right
        :width: 30%
    
    **10.** Consider two arcs :math:`\alpha` and :math:`\beta` embedded :math:`D^2 \times I` as
    shown in the figure. The loop :math:`\gamma` is obviously nullhomotopic
    in :math:`D^2 \times I`, but show that here there is no nullhomotopy of :math:`\gamma` in 
    the complement of :Math:`\alpha \cup \beta`.

.. _Exercise 1-2-11:

**11.** The **mapping torus** :math:`T_f` of a map :math:`f:X \rightarrow X` is the quotient of :Math:`X \times I` obtained
by identifying each point :math:`(x,0)` with :math:`(f(x),1)`. In the case :math:`X =S^1 \vee S^1` with :math:`f`
basepoint-preserving, compute a presentation for :math:`\pi_1(T_f)` in terms of the induced 
map :math:`f_*:\pi_1(X) \rightarrow \pi_1(X)`. Do the same when :math:`X=S^1 \times S^1`. [One way to do this is to
regard :math:`T_f` as built from :math:`X \vee S^1` by attaching cells.]

.. _Exercise 1-2-12:

.. container::

    .. image:: fig/ex-1-2-12.png
        :align: right
        :width: 40%

    **12.** The Klein bottle is usually pictured as a 
    subspace of :math:`\mathbb{R}^3` like the subspace :math:`X \subset \mathbb{R}^3` shown in
    the first figure at the right. If one wanted a model
    that could actually function as a bottle, one would 
    delete the open disk bounded by the circle of 
    self-intersection of :math:`X`, producing a subspace :math:`Y \subset X`. Show that :math:`\pi_1(X) \approx \mathbb{Z} * \mathbb{Z}` and that 
    :math:`\pi_1(Y)` has the presentation :math:`\langle a,b,c | aba^{-1}b^{-1}cb^\epsilon c^{-1} \rangle` for :math:`\epsilon = \pm 1`. (Changing the
    sign of :math:`\epsilon` gives an isomorphic group, as it happens.) Show also that :math:`\pi_1(y)` is isomorphic
    to :math:`\pi_1(\mathbb{R}^3 - Z)` for :math:`Z` the graph shown in the figure. The groups :math:`\pi_1(X)` and :math:`\pi_1(y)`
    are not isomorphic, but this is not easy to prove; see the discussion in :ref:`Example 1B.13 <Example 1B.13>`.

.. _Exercise 1-2-13:

**13.** The space :math:`Y` in the preceding exercise can be obtained from a disk with two holes
by identifying its three boundary circles. There are only two essentially different ways 
of identifying the three boundary circles. Show that the other way yields a space :math:`Z`
with :math:`\pi_1(Z)` not isomorphic to :math:`\pi_1(Y)`. [Abelianize the fundamental groups to show 
they are not isomorphic.]

.. _Exercise 1-2-14:

**14.** Consider the quotient space of a cube :math:`I^3` obtained by identifying each square
face with the opposite square face via the right-handed screw motion consisting of
a translation by one unit in the direction perpendicular to the face combined with a 
one-quarter twist of the face about its center point. Show this quotient space :math:`X` is a 
cell complex with two :math:`0`-cells, four :math:`1`-cells, three :math:`2`-cells, and one :math:`3`-cell. Using this
structure, show that :math:`\pi_1(X)` is the quaternion group :math:`\{ \pm1, \pm i, \pm j, \pm k\}`, of order eight.

.. _Exercise 1-2-15:

**15.** Given a space :math:`X` with basepoint :math:`x_0 \in X`, we may construct a CW complex :math:`L(X)`
having a single :math:`0`-cell, a :math:`1`-cell :math:`e^1_\gamma` for each loop :math:`\gamma` in :math:`X` based at :math:`x_0`, and a :math:`2`-cell :math:`e^2_\tau`
for each map :math:`\tau` of a standard triangle :Math:`PQR` into :math:`X` taking the three vertices :math:`P,\, Q`, 
and :math:`R` of the triangle to :math:`x_0`. The :math:`2`-cell :math:`e^2_\tau` is attached to the three :math:`1`-cells that are the
loops obtained by restricting :math:`\tau` to the three oriented edges :math:`PQ,\, PR`, and :Math:`QR`. Show
that the natural map :math:`L(X) \rightarrow X` induces an isomorphism :math:`\pi_1(L(X)) \approx \pi_1(X, x_0)`.

.. _Exercise 1-2-16:

.. container::

    **16.** Show that the fundamental group of the surface of infinite genus shown below is 
    free on an infinite number of generators.

    .. image:: fig/ex-1-2-16.png
        :align: center
        :width: 100%

.. _Exercise 1-2-17:

**17.** Show that :math:`\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)` is uncountable.

.. _Exercise 1-2-18:

.. container::

    **18.** In this problem we use the notions of suspension, reduced suspension, cone, and 
    mapping cone defined in :ref:`Chapter 0 <Chapter 0>`. Let :math:`X` be the subspace of :math:`\mathbb{R}` consisting of the 
    sequence :math:`1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\cdots` together with its limit point :Math:`0`.

    |indent| (a) 

.. |indent| raw:: html

    <span style="margin-left: 1em">