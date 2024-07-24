.. _Section 1.B:
1.B. K(G,1) Spaces and Graphs of Groups
================================================

|indent| In this section we introduce a class of spaces whose homotopy type depends only
on their fundamental group. These spaces arise many places in topology, especially
in its interactions with group theory.

|indent| A path-connected space whose fundamental group is isomorphic to a given group
:math:`G` and which has a contractible universal covering space is called a :math:`\mathbf{K(G,1)` **space**. The
':math:`1`' here refers to :math:`\pi_1`. More general :math:`K(G,n)` spaces are studied in :ref:`§4.2 <Section 4.2>`. All these spaces
are called Eilenberg-MacLane spaces, though in the case :math:`n=1` they were studied by 
Hurewicz before Eilenberg and MacLane took up the general case. Here are some examples:

.. _Example 1B.1:
**Example 1B.1.** :math:`S^1` is a :math:`K(\mathbb{Z}, 1)`. More generally, a connected graph is a :math:`K(G,1)` with
:math:`G` a free group, since by the results of :ref:`§1.A <Section 1.A>` its universal cover is a tree, hence contractible.

.. _Example 1B.2:
**Example 1B.2.** Closed surfaces with infinite :math:`\pi_1`, in other words, closed surfaces other
than :math:`S^2` and :Math:`\mathbb{R}P^2`, are :math:`K(G,1)`'s. This will be shown in :ref:`Example 1B.14 <Example 1B.14>` below. It also
follows from the theorem in surface theory that the only simply-connected surfaces 
without boundary are :Math:`S^2` and :math:`\mathbb{R}^2`, so the universal cover of a closed surface with
infinite fundamental group must be :math:`\mathbb{R}^2` since it is noncompact. Nonclosed surfaces
deformation retract onto graphs, so such surfaces are :math:`K(G,1)`'s with :math:`G` free.

.. _Example 1B.3:
**Example 1B.3.** The infinite-dimensional projective space :math:`\mathbb{R}P^\infty` is a :math:`K(\mathbb{Z}_2, 1)` since its
universal cover is :math:`S^\infty`, which is contractible. To show the latter fact, a homotopy from
the identity map of :math:`S^\infty` to a constant map be constructed in two stages as follows.
First, define :math:`f_t: \mathbb{R}^\infty \rightarrow \mathbb{R}^\infty` by :math:`f_t(x_1,x_2,\cdots) = (1-t)(x_1,x_2,\cdots)+t(0,x_1,x_2,\cdots)`.
This takes nonzero vectors to nonzero vectors for all :math:`t \in [0,1], so f_t / |f_t|` gives a
homotopy from the identity map of :math:`S^\infty` to the map :math:`(x_1,x_2,\cdots) \mapsto (0,x_1,x_2,\cdots)`. Then a 
homotopy from this map to a constant map is given by :math:`g_t / |g_t|` where :math:`g_t(x_1,x_2,\cdots)=(1-t)(0,x_1,x_2,\cdots) +t(1,0,0,\cdots)`.

.. _Example 1B.4:
**Example 1B.4.** Generalizing the preceding example, we can construct a :math:`K(\mathbb{Z}_m,1)` as 
an infinite-dimensional lens space :math:`S^\infty / \mathbb{Z}_m`, where :math:`\mathbb{Z}_m` acts on :math:`S^\infty`, regarded as the 
unit sphere in :math:`\mathbb{C}^\infty`, by scalar multiplication by :math:`m^{th}` roots of unity, a generator of this
action being the map :math:`(z_1,z_2,\cdots) \mapsto e^{2\pi i/m}(z_1,z_2,\cdots)`. It is not hard to check that
this is a covering space action.

.. _Example 1B.5:
**Example 1B.5.** A product :math:`K(G,1) \times K(H,1)` is a :math:`K(G \times H,1)` since its universal cover
is the product of the universal covers of :math:`K(G,1)` and :math:`K(H,1)`. By taking products of
circles and infinite-dimensional lens spaces we therefore get :math:`K(G,1)`'s for arbitrary
finitely generated abelian groups :math:`G`. For example the :math:`n`-dimensional torus :Math:`T^n`, the 
product of :math:`n` circles, is a :math:`K(\mathbb{Z}^n, 1)`.

.. _Example 1B.6:
**Example 1B.6.** For a closed connected subspace :math:`K` of :math:`S^3` that is nonempty, the 
complement :math:`S^3 - K` is a :Math:`K(G,1)`. This is a theorem in :math:`3`-manifold theory, but in the special 
case that :math:`K` is a torus knot the result follows from our study of torus knot complements
in :ref:`Examples 1.24 <Examples 1.24>` and :ref:`1.35 <Examples 1.35>`. Namely, we showed that for :math:`K` the torus knot :math:`K_{m,n}`
there is a deformation retraction of :Math:`S^3-K` onto a certain :Math:`2`-dimensional complex
:math:`X_{m,n}` having contractible universal cover. The homotopy lifting property then implies
that the universal cover of :math:`S^3-K` is homotopy equivalent to the universal cover of
:math:`X_{m,n}`, hence is also contractible.

.. _Example 1B.7:
.. container::

    **Example 1B.7.** It is not hard to construct a :math:`K(G,1)` for an arbitrary group :math:`G`, using
    the notion of a :math:`\Delta -complex` defined in :ref:`§2.1 <Section 2.1>`. Let :Math:`EG` be the :math:`\Delta`-complex whose
    :math:`n`-simplices are the ordered :math:`(n+1)`-tuples :math:`[g_0,\cdots,g_n]` of elements of :math:`G`. Such an
    :math:`n`-simplex attaches to the :Math:`(n-1)`-simplices :math:`[g_0,\cdots, \hat{g}_i,\cdots,g_n]` in the obvious way,
    just as a standard simplex attaches to its faces. (The notation :math:`\hat{g}_i` means that this 
    vertex is deleted.) The complex :math:`EG` is contractible by the homotopy :math:`h_t` that slides
    each point :Math:`x \in [g_0, \cdots, g_n]` along the line segment in :math:`[e,g_0,\cdots,g_n]` from :math:`x` to the 
    vertex :math:`[e]`, where :math:`e` is the identity element of :math:`G`. This is well-defined in :math:`EG` since
    when we restrict to a face :math:`[g_0, \cdots, \hat{g}_i, \cdots, g_n]` we have the linear deformation to :math:`[e]`
    in :math:`[e,g_0,\cdots,\hat{g}_i, \cdots, g_n]`. Note that :math:`h_t` carries :Math:`[e]` around the loop :math:`[e,e]`, so :math:`h_t` is not
    actually a deformation retraction of :math:`EG` onto :math:`[e]`.

    |indent| The group :math:`G` acts on :math:`EG` by left multiplication, an element :math:`g \in G` taking the 
    simplex :math:`[g_0,\cdots, g_n]` linearly onto the simplex :math:`[gg_0, \cdots, gg_n]`. Only the identity :math:`e`
    takes any simplex to itself, so by an exercise at the end of this section, the action
    of :math:`G` on :math:`EG` is covering space action. Hence the quotient map :math:`EG \rightarrow EG/G` is the 
    universal cover of the orbit space :math:`BG=EG/G`, and :Math:`BG` is a :math:`K(G,1)`.

    |indent| Since :math:`G` acts on :math:`EG` by freely permuting simplices, :math:`BG` inherits a :math:`\Delta`-complex
    structure from :math:`EG`. The action of :math:`G` on :math:`EG` identifies all the vertices of :Math:`EG`, so :math:`BG`
    has just one vertex. To describe the :math:`\Delta`-complex structure on :math:`BG` explicitly, note first
    that every :math:`n`-simplex of :Math:`EG` can be written uniquely in the form

    .. math::

        [g_0,g_0g_1,g_0g_1g_2,\cdots,g_0g_1 \cdots g_n] = g_0[e,g_1,g_1g_2, \cdots, g_1 \cdots g_n]

    .. image::fig/BG.png
        :width: 60%
        :align: right

    The image of this simplex in :math:`BG` may be denoted unambiguously by the symbol
    :math:`[g_1|g_2|\cdots |g_n]`. In this 'bar' notation the :math:`g_i`'s and their ordered products can be
    used to label edges, viewing an 
    edge label as the ratio between
    the two labels on the vertices
    at the endpoints of the edge,
    as indicated in the figure. With
    this notation, the boundary of 
    a simplex :math:`[g_1|\cdots | g_n]` of :Math:`BG`
    consists of the simplices :math:`[g_2|\cdots| g_n],\,[g_1|\cdots|g_{n-1}]`, and :math:`[g_1|\cdots |g_ig_{i+1}|\cdots|g_n]`
    for :math:`i=1,\cdots ,n-1`.

|indent| This construction of a :math:`K(G,1)` produces a rather large space, since :math:`BG` is
always infinite-dimensional, and if :math:`G` is infinite, :math:`BG` has an infinite number of cells in
each positive dimension. For example, :math:`B\mathbb{Z}` is much bigger than :math:`S^1`, the most efficient
:math:`K(\mathbb{Z},1)`. On the other hand, :math:`BG` has the virtue of being functorial: A homomorphism
:math:`f:G \rightarrow H` induces a map :matH:`Bf:BG \rightarrow BH` sending a simplex :math:`[g_1 | \cdots g_n]` to the simplex
:math:`[f(g_1)|\cdots |f(g_n)]`. A different construction of a :math:`K(G,1)` is given in :ref:`§4.2 <Section 4.2>`. Here one
starts with any :math:`2`-dimensional complex having fundamental group :math:`G`, for example
the complex :math:`X_G` associated to a presentation of :Math:`G`, and then one attaches cells of
dimension :math:`3` and higher to make the universal cover contractible without affecting :Math:`\pi_1`.
In general, it is hard to get any control on the number of higher-dimensional cells
needed in this construction, so it too can be rather inefficient. Indeed, finding an
efficient :Math:`K(G,1)` for a given group :math:`G` is often a difficult problem.

|indent| It is a curious and almost paradoxical fact that if :math:`G` contains any elements of finite
order, then every :math:`K(G,1)` CW complex must be infinite-dimensional. This is shown
in :ref:`Proposition 2.45 <Proposition 2.45>`. In particular the infinite-dimensional lens space :math:`K(\mathbb{Z}_m, 1)`'s in
:ref:`Example 1B.4 <Example 1B.4>` cannot be replaced by any finite-dimensional complex.

|indent| In spite of the great latitude possible in the construction of :Math:`K(G,1)`'s, there is a 
very nice homotopical uniqueness property that accounts for much of the interest in
:math:`K(G,1)`'s:

.. _Theorem 1B.8:
    **Theorem 1B.8.** *The homotopy type of a CW complex* :math:`K(G,1)` *is uniquely determined
    by* :math:`G`.

|indent| Having a unique homotopy type of :math:`K(G,1)`'s  associated to each group :math:`G` means
that algebraic invariants of spaces that depend only on homotopy type, such as 
homology and cohomology groups, become invariants of groups. This has proved to be a
quite fruitful idea, and has been much studied both from the algebraic and topological
viewpoints. The discussion following :ref:`Proposition 2.45 <Proposition 2.45>` gives a few references.

|indent| The preceding theorem will follow easily from:

.. _Proposition 1B.9:

.. container::

        **Proposition 1B.9.** *Let* :math:`X` *be a connected CW complex and let* :math:`Y` *be a* :math:`K(G,1)`. *Then
        every homomorphism* :Math:`\pi_1(X,x_0)\rightarrow \pi_1(Y,y_0)` *is induced by a map* :math:`(X,x_0) \rightarrow (Y,y_0)`
        *that is unique up to homotopy fixing* :math:`x_0`.
    
    |indent| To deduce the theorem from this, let :math:`X` and :math:`Y` be CW complex :math:`K(G,1)`'s with
    isomorphic fundamental groups. The proposition gives maps :math:`f:(X,x_0) \rightarrow (Y,y_0)` and
    :math:`g:(Y,y_0) \rightarrow (X,x_0)` inducing inverse isomorphisms :math:`\pi_1(X,x_0) \approx \pi_1(Y,y_0)`. Then :math:`fg`
    and :math:`gf` induce the identity on :math:`\pi_1` and hence are homotopic to the identity maps.

    .. image:: fig/prop-1B-9.png
        :align: right
        :width: 30%

    **Proof of 1B.9:** Let us first consider the case that :math:`X` has a single :math:`0`-cell, the basepoint
    :math:`x_0`. Given a homomorphism :math:`\varphi: \pi_1(X,x_0) \rightarrow \pi_1(Y,y_0)`, we begin the construction
    of a map :math:`f:(X,x_0) \rightarrow (Y,y_0)` with :math:`f_* = \varphi` by setting :Math:`f(x_0)=y_0`. Each :math:`1`-cell
    :math:`e^1_\alpha` of :Math:`X` has closure a circle determining an element
    :math:`[e^1_\alpha]\in \pi_1(X,x_0)`, and we let :math:`f` on the closure of :math:`e^1_\alpha`
    be a map representing :math:`\varphi([e^1_\alpha])`. If :math:`i:X^1 \hookrightarrow X` denotes
    the inclusion, then :math:`\varphi i_* = f_*` since :math:`\pi_1(X^1,x_0)` is 
    generated by the elements :math:`[e^1_\alpha]`.

    |indent| To extend :math:`f` over a cell :math:`e^2_\beta` with attaching map :math:`\psi_\beta : S^1 \rightarrow X^1`, all we need is for the
    composition :Math:`f \psi_\beta` to be nullhomotopic. Choosing a basepoint :Math:`s_0 \in S^1` and a path in :Math:`X^1`
    from :math:`\psi_\beta (s_0)` to :Math:`x_0,\, \psi_\beta` determines an element :math:`[\psi_\beta] \in \pi_1(X^1, x_0)`, and the existence
    of a nullhomotopy of :math:`f\psi_\beta` is equivalent to :math:`f_*([\psi_\beta])` being zero in :math:`\pi_1(Y,y_0)`. We
    have :math:`i_*([\psi_\beta])=0` since the cell :math:`e^2_\beta` provides a nullhomotopy of :math:`\psi_\beta` in :math:`X`. Hence
    :math:`f_*([\psi_\beta])=\varphi i_*([\psi_\beta])=0`, and so :math:`f` can be extended over :math:`e^2_\beta`.

    |indent| Extending :math:`f` inductively over cells :math:`e^n_\gamma` with :math:`n>2` is possible since the attaching
    maps :math:`\psi_\gamma : S^{n-1} \rightarrow X^{n-1}` have nullhomotopic compositions :math:`f\psi_\gamma : S^{n-1} \rightarrow Y`. This is
    because :math:`f\varphi_\gamma` lifts to the universal cover of :Math:`Y` if :math:`n>2`, and this cover is contractible
    by hypothesis, so the lift of :math:`f \varphi_\gamma` is nullhomotopic, hence also :Math:`f\varphi_\gamma` itself.

    |indent| Turning to the uniqueness statement, if two maps :math:`f_0,f_1:(X,x_0) \rightarrow (Y,y_0)` induce
    the same homomorphism on :Math:`\pi_1`, then we see immediately that their restrictions
    to :Math:`X^1` are homotopic, fixing :Math:`x_0`. To extend the resulting map :math:`X^1 \times I \cup X \times \partial I \rightarrow Y`
    over the remaining cells :math:`e^n \times (0,1)` of :Math:`X \times I` we can proceed just as in the preceding
    paragraph since these cells have dimension :math:`n+1 >2`. Thus we obtain a homotopy
    :math:`f_t:(X,x_0)\rightarrow (Y,y_0)`, finishing the proof in the case that :math:`X` has a single :math:`0`-cell.

    |indent| The case that :math:`X` has more than one :math:`0`-cell can be treated by a small elaboration
    on this argument. Choose a maximal tree :math:`T \subset X`. To construct a map :math:`f` realizing a 
    given :Math:`\varphi`, begin by setting :math:`f(t)=y_0`. Then each edge :math:`e^1_\alpha` in :math:`X-T` determines an
    element :math:`[e^1_\alpha] \in \pi_1(X,x_0)`, and we let :math:`f` on the closure of :math:`e^1_\alpha` be a map representing
    :math:`\varphi([e^1_\alpha])`. Extending :math:`f` over higher-dimensional cells then proceeds just as before.
    Constructing a homotopy :math:`f_t` joining two given maps :math:`f_0` and :math:`f_1` with :math:`f_{0*}=f_{1*}` also
    has an extra step. Let :Math:`h_t:X^1 \rightarrow X^1` be a homotopy starting with :math:`h_0=\mathbb{1}` and restricting
    to a deformation retraction of :Math:`T` onto :Math:`x_0`. (It is easy to extend such a deformation
    retraction to a homotopy defined on all of :Math:`X^1`.) We can construct a homotopy from
    :math:`f_0 | X^1` to :math:`f_1|X^1` by first deforming :math:`f_0|X^1` and :math:`f_1|X^1` to take :math:`T` to :math:`y_0` by composing with
    :math:`h_t`, then applying the earlier argument to obtain a homotopy between the modified
    :math:`f_0|X^1` and :math:`f_1|X^1`. Having a homotopy :math:`f_0|X^1 \simeq f_1|X^1` we extend this over all of :math:`X` in
    the same way as before. |qed|

|indent| The first part of the preceding proof also works for the :math:`2`-dimensional complexes
:math:`X_G` associated to presentations of groups. Thus every homomorphism :Math:`G \rightarrow H` is 
realized as the induced homomorphism of some map :math:`X_G \rightarrow X_H`. However, there is no
uniqueness statement for this map, and it can easily happen that different presentations
of a group :math:`G` give :Math:`X_G`'s that are not homotopy equivalent.

-------------------------
Graphs of Groups
-------------------------

|indent| As an illustration of how :math:`K(G,1)` spaces can be useful in group theory, we shall
describe a procedure for assembling a collection of :Math:`K(G,1)`'s together into a :Math:`K(G,1)`
for a larger group :math:`G`. Group-theoretically, this gives a method for assembling smaller
groups together to form a larger group, generalizing the notion of free products.

|indent| Let :math:`\Gamma` be a graph that is connected and oriented, that is, its edges are viewed as
arrows, each edge having a specified direction. Suppose that at each vertex :math:`v` of :math:`\Gamma` we
place a group :math:`G_v` and along each edge :math:`e` of :math:`\Gamma` we put a homomorphism :math:`\varphi_e` from the
group at the tail of the edge to the group at the head of the edge. We call this data a
**graph of groups**. Now build a space :math:`B\Gamm` by putting the space :maht:`BG_v` from :ref:`Example 1B.7 <Example 1B.7>`
at each vertex :math:`v` of :math:`\Gamma` and then filling in a mapping cylinder of the map :math:`B\varphi_e` along
each edge :math:`e` of :math:`\Gamma`, identifying the two ends of the mapping cylinder with the two :math:`BG_v`'s
at the ends of :Math:`e`. The resulting space :math:`B\Gamma` is then a CW complex since the maps :math:`B\varphi_e`
take :math:`n`-cells homeomorphically onto :math:`n`-cells. In fact, the cell structure on :Math:`B\Gamma` can be
canonically subdivided into a :math:`\Delta-complex` structure using the prism construction from
the proof of :ref:`Theorem 2.10 <Theorem 2.10>`, but we will not need to do this here.

|indent| More generally, instead of :math:`BG_v` one could take any CW complex :math:`K(G_v,1)` at the
vertex :math:`v`, and then along edges put mapping cylinders of maps realizing the homomorphisms
:math:`\varphi_e`. We leave it for the reader to check that the resulting space :math:`K\Gamma` is
homotopy equivalent to the :math:`B\Gamma` constructed above.

.. _Example 1B.10:
**Example 1B.10.** Suppose :math:`\Gamma` consists of one central vertex with a number of edges
radiating out from it, and the group :math:`G_v` at this central vertex is trivial, hence also all
the edge homomorphisms. Then :ref:`van Kampen's theorem <Theorem 1.20>` implies that :math:`\pi_1(K\Gamma)` is the
free product of the groups at all the outer vertices.

|indent| In view of this example, we shall call :math:`\pi_1(K\Gamma)` for a general graph of groups :math:`\Gamma` the
**graph product** of the vertex groups :math:`G_v` with respect to the edge homomorphisms :math:`\varphi_e`.
The name for :math:`\pi_1(K\Gamma)` that is generally used in the literature is the rather awkward
phrase, 'the fundamental group of the graph of groups'.

|indent| Here is the main result we shall prove about graphs of groups:

.. _Theorem 1B.11:
    **Theorem 1B.11.** *If all the edge homorphisms* :math:`\varphi_e` *are injective, then* :math:`K\Gamma` *is a*
    :math:`K(G,1)` *and the inclusions* :math:`K(G_v,1) \hookrightarrow K\Gamma` *induce injective maps on* :math:`\pi_1`.

|indent| Before giving the proof, let us look at some interesting special cases:

.. _Example 1B.12:
.. container::

    **Example 1B.12: Free products with Amalgamation.** Suppose the graph of groups is
    :math:`A \leftarrow C \rightarrow B`, with the two maps monomorphisms. One can regard this data as a specifying
    embeddings of :math:`C` as subgroups of :math:`A` and :math:`B`. Applying :ref:`van Kampen's theorem <Theorem 1.20>`
    to the decomposition of :math:`K\Gamma` into its two mapping cylidners, we see that :math:`\pi_1(K\Gamma)` is
    the quotient of :math:`A{\Large *}B` obtained by identifying the subgroup :math:`C \subset A` with the subgroup
    :math:`C \subset B`. The standard notation for this group is :math:`A{\Large *}_C B`, the free product of :math:`A` and
    :math:`B` **amalgamated** along the subgroup :math:`C`. According to the theorem, :math:`A {\Large *}_C B` contains
    both :math:`A` and :math:`B` as subgroups.

    |indent| For example, a free product with amalgamation :math:`\mathbb{Z} {\Large *}_\mathbb{Z} \mathbb{Z}` can be realized by 
    mapping cylinders of the maps :math:`S^1 \leftarrow S^1 \rightarrow S^1` that are :math:`m`-sheeted and :Math:`n`-sheeted covering
    spaces, respectively. We studied this case in :ref:`Examples 1.24 <Examples 1.24>` and :ref:`1.35 <Examples 1.35>` where we showed
    that the complex :math:`K\Gamma` is a deformation retract of the complement of a torus knot in
    :math:`S^3` if :math:`m` and :math:`n` are relatively prime. It is a basic result in :math:`3`-manifold theory that the
    complement of every smooth knot in :math:`S^3` can be built up by iterated graph of groups
    constructions with injective edge homomorphisms, starting with free groups, so the
    theorem implies that these knot complements are :math:`K(G,1)`'s. Their universal covers
    are all :math:`\mathbb{R}^3`, in fact.

.. _Example 1B.13:
.. container::

    **Example 1B.13: HNN Extensions.** Consider a graph of groups :math:`C \mathrel{\substack {\varphi \\ \longrightarrow\\ \longrightarrow\\ \psi}} A` with :math:`\varphi`
    and :math:`\psi` both monomorphisms.





.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>