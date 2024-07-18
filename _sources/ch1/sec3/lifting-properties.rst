Lifting Properties
================================================

|indent| Covering spaces are defined in fairly geometric terms, as maps :math:`p:\tilde{X} \rightarrow X` that are
local homeomorphisms in a rather strong sense. But from the viewpoint of algebraic
topology, the distinctive feature of covering spaces is their behavior with respect to 
lifting of maps. Recall the terminology from the proof of :ref:`Theorem <Theorem 1.7>`: A **lift** of a map
:math:`f:Y \rightarrow X` is a map :math:`\tilde{f} : Y \rightarrow \tilde{X}` such that :math:`p\tilde{f}=f`. We will describe three special lifting
properties of covering spaces and derive a few applications of these.

|indent| First we have **homotopy lifting property**, also known as the **covering homotopy property**:

.. _Proposition 1.30:

.. container::

    ..

        **Proposition 1.30.** *Given a covering space* :math:`p:\tilde{X} \rightarrow X`, *a homotopy* :math:`f_t:Y \rightarrow X`, *and a
        map* :math:`\tilde{f}_0: Y \rightarrow \tilde{X}` *lifting* :math:`f_0`, *then there exists a unique homotopy* :math:`\tilde{f}_t: Y\rightarrow \tilde{X}` *of* :math:`\tilde{f}_0` *that
        lifts* :math:`f_t`.

    **Proof:** This was proved as property (c) in the proof of :ref:`Theorem 1.7 <Theorem 1.7>`. |qed|

|indent| Taking :math:`Y` to be apoint gives the **path lifting property** for a covering space
:math:`p:\tilde{X} \rightarrow X`, which says that for each path :math:`f:I \rightarrow X` and each lift :math:`\tilde{x}_0` of the starting
point :Math:`f(0)=x_0` there is a unique path :math:`\tilde{f}:I \rightarrow \tilde{X}` lifting :math:`f` starting at :math:`\tilde{x}_0`. In particular,
the uniqueness of lifts implies that every lift of a constant path is constant, but this
could be deduced more simply from the fact that :math:`p^{-1}(x_0)` has the discrete topology,
by the definition of a covering space.

|indent| Taking :math:`Y` to be :math:`I`, we see that every homotopy :math:`f_t` of a path :math:`f_0` in :math:`X` lifts to a
homotopy :math:`\tilde{f}_t` of each lift :math:`\tilde{f}_0` of :math:`f_0`. The lifted homotopy :math:`\tilde{f}_t` is a homotopy of paths,
fixing the endpoints, since as :math:`t` varies each endpoint of :Math:`\tilde{f}_t` traces out a path lifting a 
constant path, which must therefore be constant.

|

|indent| Here is a simple application.

|


.. _Proposition 1.31:

.. container::

    ..

        **Proposition 1.31.** *The map* :math:`p_*: \pi_1(\tilde{X},\tilde{x}_0)\rightarrow \pi_1(X,x_0)` *induced by a covering space*
        :math:`p:(\tilde{X}, \tilde{x}_0) \rightarrow (X, x_0)` *is injective. The image subgroup* :math:`p_*(\pi_1(\tilde{X}, \tilde{x}_0))` *in* :math:`\pi_1(X, x_0)`
        *consists of the homotopy classes of loops in* :math:`X` *based at* :math:`x_0` whose lifts to :math:`\tilde{X}` *starting
        at* :math:`\tilde{x}_0` *are loops*.
    
    **Proof:** An element of the kernel of :math:`p_*` is represented by a loop :math:`\tilde{f}_0:I \rightarrow \tilde{X}` with a 
    homotopy :math:`f_t:I \rightarrow X` of :math:`f_0=p\tilde{f}_0` to the trivial loop :math:`f_1`. By the remarks preceding the 
    proposition, there is a lifted homotopy of loops :math:`\tilde{f}_t` starting with :math:`\tilde{f}_0` and ending with
    a constant loop. Hence :math:`[\tilde{f}_0]=0` in :math:`\pi_1(\tilde{X}, \tilde{x}_0)` and :math:`p_*` is injective.

    |indent| For the second statement of the proposition, loops at :math:`x_0` lifting to loops at :math:`\tilde{x}_0`
    certainly represent elements of the image of :math:`p_*: \pi_1(\tilde{X}, \tilde{x}_0) \rightarrow \pi_w(X,x_0)` Conversely,
    a loop representing an element of the image of :math:`p_*` is homotopic to a loop having such
    a lift, so by homotopy lifting, the loop itself must have such a lift. |qed|

|

.. _Proposition 1.32:

.. container::

    ..

        **Proposition 1.32.** *The number of sheets of a covering space* :math:`p:(\tilde{X}, \tilde{x}_0) \rightarrow (X, x_0)`
        *with* :math:`X` *and* :math:`\tilde{X}` *path-connected equals the index of* :math:`p_*(\pi_1(\tilde{X},\tilde{x}_0))` *in* :math:`\pi_1(X, x_0)`.
    
    **Proof:** For a loop :math:`g` in :math:`X` based at :math:`x_0`, let :math:`\tilde{g}` be its lift to :math:`\tilde{X}` starting at :math:`\tilde{x}_0`. A product
    :math:`h \cdot g` with :math:`[h] \in H=p_*(\pi_1(\tilde{X}, \tilde{x}_0))` has the lift :math:`\tilde{h} \cdot \tilde{g}` ending at the same points as :math:`\tilde{g}`
    since :math:`\tilde{h}` is a loop. Thus we may define a function :math:`\phi` from cosets :math:`H[g]` to :math:`\p^{-1}(x_0)`
    by sending :math:`H[g]` to :math:`\tilde{g}(1)`. The path-connectedness of :math:`\tilde{X}` implies that :Math:`\phi` is surjective
    since :math:`\tilde{x}_0` can be joined to any point in :math:`p^{-1}(x_0)` by a path :math:`\tilde{g}` projecting to a loop :math:`g` at
    :math:`x_0`. To see that :math:`\phi` is injective, observe that :math:`\phi(H[g_1])=\phi(H[g_2])` implies that :math:`g_1 \cdot \bar{g}_2`
    lifts to a loop in :math:`\tilde{X}` based at :math:`\tilde{x}_0`, so :math:`[g_1][g_2]^{-1} \in H` and hence :math:`H[g_1]=H[g_2]`. |qed|

|

|indent| It is importnat also to know about the existence and uniqueness of lifts of general
maps, not just lifts of homotopies. For the existence question an answer is provided
by the following **lifting criterion:**

.. Proposition 1.33:

.. container::

        **Proposition 1.33.** *Suppose given a covering space* :math:`p:(\tilde{X} , \tilde{x}_0) \rightarrow (X,x_0)` *and a map*
        :math:`f:(Y, y_0) \rightarrow (X,x_0)` *with* :math:`Y` *path-connected and locally path-connecetd. Then a lift*
        :math:`\tilde{f}:(Y,y_0) \rightarrow (\tilde{X}, \tilde{x}_0)` *of* :math:`f` *exists iff* :math:`f_*(\pi_1(Y, y_0)) \subset p_*(\pi_1(\tilde{X}, \tilde{x}_0))`.
    
    |indent| When we say a space has a certain property locally, such as being locally 
    path-connected, we usually mean that each point has arbitrarily small open neighborhoods
    with this property. Thus for :math:`Y` to be locally path-connected means that for each point
    :math:`y \in Y` and each neighborhood :math:`U` of :math:`y` there is an open neighborhood :math:`V \subset U` of :math:`y`
    that is path-conneceted.

    **Proof:** The 'only if' statement is obvious since :Math:`f_*= p_*\tilde{f}_*`. For the converse, let 
    :math:`y \in Y` and let :math:`\gamma` be a path in :math:`Y` from :math:`y_0` to :math:`y`. The path :math:`f\gamma` in :math:`X` starting at :math:`x_0`
    has a unique lift :math:`\tilde{f\gamma}` starting at :math:`\tilde{x}_0`. Define :math:`\tilde{f}(y) = \tilde{f\gamma}(1)`. To show this is well-defined,
    independent of the choice of :math:`\gamma`, let :math:`\gamma '` be another path from :math:`y_0` to :math:`y`. Then
    :math:`(f\gamma '`)\cdot (\bar{f\gamma})` is a loop :math:`h_0` at :math:`x_0` with :math:`[h_0] \in f_*(\pi_1(Y, y_0)) \subset p_*(\pi_1(\tilde{X},\tilde{x}_0))`.

    .. image:: fig/prop-1-33.png
        :align: right
        :width: 60%
    
    This
    means there is a homotpy :math:`h_t` of :math:`h_0` to a loop :math:`h_1` that lifts to a 
    loop :math:`\tilde{h}_1` in :math:`\tilde{X}` based at :math:`\tilde{x}_0`. Apply the covering homotopy
    property to :math:`h_t` to get a lifting :math:`\tilde{h}_t`. Since :math:`\tilde{h}_1` is a loop at
    :math:`\tilde{x}_0`, so is :math:`\tilde{h}_0`. By the uniqueness of lifted paths,
    the first half of :math:`\tilde{h}_0` is :math:`\tilde{f\gamma '}` and the second
    half is :math:`\tilde{f\gamma}` traversed backwards, with
    the common midpoint :Math:`\tilde{f\gamma}(1)=\tilde{f\gamma '}(1)`.
    This shows that :math:`\tilde{f}` is
    well-defined.

    |indent| To see that :math:`\tilde{f}` is continuous, let :math:`U \subset X` be an open neighborhood of :math:`f(y)` having
    a lift :math:`\tilde{U} \subset \tilde{X}` containing :math:`\tilde{f}(y)` such that :math:`p:\tilde{U} \rightarrow U` is a homeomorphism. Choose a 
    path-connected open neighborhood :math:`V` of :math:`y` with :math:`f(V) \subset U`. For paths from :math:`y_0` to
    points :Math:`y' \in V` we can take a fixed path :math:`(f\gamma) \cdot (f\eta)` in :math:`X` have lifts :math:`(\tilde{f\gamma}) \cdot (\tilde{f\eta})`
    where :math:`\tilde{f\eta}=p^{-1}f\eta` and :math:`p^{-1}:U \rightarrow \tilde{U}` is the inverse of :math:`o:\tilde{U} \rightarrow U`. Thus :math:`\tilde{f}(V) \subset \tilde{U}` and
    :math:`\tilde{f} | V = p^{-1}f`, hence :math:`\tilde{f}` is continuous at :math:`y`. |qed|

|

|indent| Without the local path-connectedness assumption on :math:`Y` the lifting criterion in the 
preceding proposition can fail, as shown by an example in :ref:`Exercise 7 <Exercise 1-3-7>` at the end of this 
section.

|indent| Next we have the **unique lifting property:**

.. _Proposition 1.34:

.. container::

        **Proposition 1.34.** *Given a covering space* :math:`p:\tilde{X} \rightarrow X` *and a map* :math:`f: Y \rightarrow X`, *if two lifts*
        :math:`\tilde{f}_1,\tilde{f}_2: Y \rightarrow \tilde{X}` *of* :math:`f` *agree at one point of* :math:`Y` *and* :math:`Y` *is connected, then* :math:`\tilde{f}_1` *and* :math:`\tilde{f}_2` *agree
        on all of* :math:`Y`.
    
    **Proof:** For a point :math:`y \in Y`, let :math:`U` be an evenly covered open neighborhood of :Math:`f(y)`
    in :math:`X`, so :math:`p^{-1}(U)` is decomposed into disjoint sheets each mapped homeomorphically 
    onto :math:`U` by :math:`p`. Let :math:`\tilde{U}_1` and :math:`\tilde{U}_2` be the sheets containing :math:`\tilde{f}_1(y)` and :math:`\tilde{f}_2(y)`, respectively.
    By continuity of :math:`\tilde{f}_1` and :math:`\tilde{f}_2` there is a neighborhood :math:`N` of :math:`y` mapped into :math:`\tilde{U}_1` by :math:`\tilde{f}_1`
    and into :math:`\tilde{U}_2` by :math:`\tilde{f}_2`. If :math:`\tilde{f}_1(y) \neq \tilde{f}_2(y)` then :math:`\tilde{U}_1 \neq \tilde{U}_2`, hence :math:`\tilde{U}_1` and :math:`\tilde{U}_2` are disjoint and 
    :math:`\tilde{f}_1 \neq \tilde{f}_2` throughout the neighborhood :math:`N`. On the other hand, if :math:`\tilde{f}_1(y) = \tilde{f}_2(y)` then
    :math:`\tilde{U}_1 = \tilde{U}_2` so :math:`\tilde{f}_1 = \tilde{f}_2` on :math:`N` since :math:`p\tilde{f}_1 = p\tilde{f}_2` and :math:`p` is injective on :math:`\tilde{U}_1 = \tilde{U}_2`. Thus
    the set of points where :Math:`\tilde{f}_1` and :math:`\tilde{f}_2` agree is both open and closed in :math:`Y`. |qed|



.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>