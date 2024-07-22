Deck Transformations and Group Actions
================================================

|indent| For a covering space :math:`p:\tilde{X} \rightarrow X` the isomorphisms :math:`\tilde{X} \rightarrow \tilde{X}` are called **deck transfor
mations** or **covering transformations**. These form a group :math:`G(\tilde{X})` under composition.
For example, for the covering space :math:`p: \mathbb{R} \rightarrow S^1` projecting a vertical helix onto a circle,
the deck transformations are the vertical translations taking the helix onto itself, so
:math:`G(\tilde{X}) \approx \mathbb{Z}` in this case. For the :math:`n`-sheeted covering space :math:`S^1 \rightarrow S^1,\, z \mapsto z^n`, the deck
transformations are the rotations of :math:`S^1` through angles that are multiples of :math:`2\pi / n`,
so :math:`G(\tilde{X})=\mathbb{Z}_n`.

|indent| By the :ref:`unique lifting property <Proposition 1.34>`, a deck transformation is completely determined
by where it sends a single point, assuming :math:`\tilde{X}` is path-connected. In particular, only
theidentity deck transformation can fix a point of :math:`\tilde{X}`.

|indent| A covering space :math:`p:\tidle{X} \rightarrow X` is called **normal** if for each :math:`x \in X` and each pair of lifts
:math:`\tilde{x},\tilde{x}'` of :math:`x` there is a deck transformation taking :math:`\tilde{x}`to :math:`\tilde{x}'`. For example, the covering
space :math:`\mathbb{R} \rightarrow X^1` and the :math:`n`-sheeted covering spaces :math:`S^1 \rightarrow S^1` are normal. Intuitively, a 
normal covering space is one with maximal symmetry. This can be seen in the covering
spaces of :math:`S^1 \vee S^1` shown in the talbe earlier in this section, where the normal covering
spaces are (1),(2),(5)-(8), and (11). Note that in (7) the group of deck transformations
is :math:`\mathbb{Z}_4` while in (8) it is :math:`\mathbb{Z}_2 \times \mathbb{Z}_2`.

|indent| Sometimes normal covering spaces are called regular covering spaces. The term
'normal' is motivated by the following result.

.. _Proposition 1.39:

.. container::

        **Proposition 1.39.** *Let* :math:`p:(\tilde{X}, \tilde{x}_0) \rightarrow (X, x_0)` *be a path-connected covering space of 
        the path-connected, locally path-connected space* :math:`X`, *and let* :math:`H` be the subgroup
        :math:`p_*(\pi_1(\tilde{X},\tilde{x}_0)) \subset \pi_1(X,x_0)`. *Then*:

        (a) *This covering space is normal iff* :math:`H` *is a normal subgroup of* :math:`\pi_1(X,x_0)`.
        (b) :math:`G(\tilde{X})` *is isomorphic to the quotient* :math:`N(H)/H` *where* :math:`N(H)` *is the normalizer of*
            :math:`H` *in* :math:`\pi_1(X,x_0)`.
        *In particular,* :math:`G(\tilde{X})` *is isomorphic to* :math:`\pi_1(X,x_0)/H` *if* :math:`\tilde{X}` *is a normal covering. Hence
        for the universal cover* :math:`\tidle{X} \rightarrow X` *we have* :math:`G(\tilde{X}) \approx \pi_1(X)`.
    
    **Proof:** We observed earlier in the proof of the :ref:`classification theorem <Theorem 1.38>` that changing
    the basepoint :Math:`\tilde{x}_0 \in p^{-1}(x_0)` to :math:`\tilde{x}_1 \in p^{-1}(x_0)` corresponds precisely to conjugating 
    :math:`H` by an element :math:`[\gamma] \in \pi_1(X,x_0)` where :math:`\gamma` lifts to a path :math:`\tilde{\gamma` from :math:`\tilde{x}_0` to :Math:`\tilde{x}_1`. Thus :math:`[\gamma]`
    is in the normalizer :math:`N(H)` iff :math:`p_*(\pi_1(\tilde{X},\tilde{x}_0))=p_*(\pi_1(\tilde{X},\tilde{x}_1))`, which by the :ref:`lifting
    criterion <Proposition 1.33>` is equivalent to the existence of a deck transformation taking :math:`\tilde{x}_0` to :math:`\tilde{x}_1`.
    Hence the covering space is normal iff :math:`N(H) = \pi_1(X,x_0)`, that is, iff :math:`H` is a normal 
    subgroup of :Math:`\pi_1(X,x_0)`.

    |indent| Define :math:`\varphi : N(H) \rightarrow G(\tilde{X})` sending :Math:`[\gamma]` to the deck transformation :math:`\tau` taking :math:`\tilde{x}_0` to
    :math:`\tilde{x}_1`, in the notation above. Then :math:`\varphi` is a homomorphism, for if :Math:`\gamma'` is another loop corresponding
    to the deck transformation :math:`\tau '` taking :math:`\tilde{x}_0` to :math:`{x}_1'` then :math:`\gamma \cdot \gamma'` lifts to :math:`\tilde{\gamma} \cdot (\tau(\tilde{\gamma}'))`,
    a path from :math:`\tilde{x}_0` to :math:`\tau(\tilde{x}_1')=\tau \tau'(\tilde{x}_0)`, so :math:`\tau \tau'` is the deck transformation corresponding 
    to :math:`[\gamma][\gamma']`. By the preceding paragraph :math:`\varphi` is surjective. Its kernel consists of classes
    :math:[\gamma] lifting to loops in :math:`\tilde{X}`. These are exactly the elements of :math:`p_*(\pi_1(\tilde{X},\tilde{x}_0))= H`. |qed|

|indent| The group of deck transformations is a special case of the general notion of
'groups acting on spaces'. Given a group :math:`G` and a space :math:`Y`, then an **action** of :Math:`G` 
on :Math:`Y` is a homomorphism :math:`\rho` from :math:`G` to the group Homoe(:math:`Y`) of all homeomorphisms
from :math:`Y` to itself. Thus to each :math:`g \in G` is associated a homeomorphisms :math:`\rho(g): Y \rightarrow Y`,
which for notational simplicity we write simply as :math:`g:Y \rightarrow Y`. For :math:`\rho` to be a homomorphism
amounts to requiring that :Math:`g_1(g_2(y)) = (g_1g_2)(y)` for all :math:`g_1,g_2 \in G` and
:math:`y \in Y`. If :math:`\rho` is injective then it identifies :math:`G` with a subgroup of Homeo(:math:`Y`), and in
practice not much is lost in assuming :math:`\rho` is an inclusion :math:`G \hookrightarrow`Homeo(:math:`Y`) since in any
case the subgroup :math:`\rho(G) \subset \text{Homeo}(Y)` contains all the topological information about 
the action.

|indent| We shall be interested in actions satisfying the following condition:

(:math:`{\Large *}`) Each :math:`y \in Y` has a neighborhood :math:`U` such that all the images :math:`g(U)` for varying
    :math:`g \in G` are disjoint. In other words, :math:`g_1(U) \cap g_2(U) \neq \emptyset` implies :math:`g_1 = g_2`.

The action of the deck transformation group :math:`G(\tilde{x})` on :math:`\tilde{X}` satisfies (:math:`{\Large *}`). To see this.
let :math:`\tilde{U} \subset \tilde{X}` project homeomorphically to :math:`U \subset X`. If :math:`g_1(\tilde{U}) \cap g_2(\tilde{U}) \neq \emptyset` for some
:math:`g_1,g_2 \in G(\tilde{X})`, then :math:`g_1(\tilde{x}_1)=g_2(\tilde{x}_2)` for some :Math:`\tilde{x}_1,\tilde{x}_2\in \tilde{U}`. Since :math:`\tilde{x}_1` and :math:`\tilde{x}_2` must lie
in the same set :math:`p^{-1}(x)`, which interesects :math:`\tilde{U}` in only one point, we must have :math:`\tilde{x}_1=\tilde{x}_2`.
THen :math:`g_1^{-1}g_2` fixes this point, so :math:`g_1^{-1}g_2 = \mathbb{1}` and :math:`g_1 = g_2`.

|indent| Note that in (:math:`{\Large *}`) it suffices to take :math:`g_1` to be the identity since :math:`g_1(U) \cap g_2(U) \neq \emptyset` 
is equivalent to :math:`U \cap g_1^{-1}g_2(U) \neq \emptyset`. Thus we have the equivalent condition that
:math:`U \cap g(U) \neq \emptyset` only when :math:`g` is the identity.

|indent| Given an action of a group :math:`G` on a space :math:`Y`, we can form a space :Math:`Y/G`, the quotient
space of :math:`Y` in which each point :math:`y` is identified with all its images :math:`g(y)` as :math:`g` ranges
over :Math:`G`. The points of :math:`Y/G` are thus **orbits** :math:`Gy = \{g(y) \mid g \in G\}` in :math:`Y`, and 
:math:`Y/G` is called the **orbit space** of the action. For example, for a normal covering space
:math:`\tilde{X} \rightarrow X`, the orbit space :math:`\tilde{X}/G(\tilde{X})` is just :math:`X`.

.. _Proposition 1.40:

.. container::

        **Proposition 1.40.** *If an action of a group* :math:`G` *on a space* :math:`Y` *satisfies* (:math:`{\Large *}`), *then*:

        (a) *The quotient map* :math:`p:Y \rightarrow Y/G,\, p(y)=Gy`, *is a normal covering space.*
        (b) :math:`G` *is the group of deck transformations of this covering space* :math:`Y \rightarrow Y/G` *if* :math:`Y` *is
            path-connected.*
        (c) :math:`G` *is isomorphic to* :math:`\pi_1(Y/G)p_*(\pi_1(Y))` *if* :math:`Y` *is path-connected and locally path-
            connected.*
    
    **Proof:** Given an open set :math:`U\subset Y` as in condition (:math:`{\Large *}`), the quotient map :math:`p` simply
    identifies all the disjoint homeomorphic sets :math:`\{g(U) \mid g \in G\}` to a single open set
    :math:`p(U)` in :math:`Y/G`. By the definition of the quotient topology on :math:`Y/G,\, p` restricts to 
    a homeomorphism from :math:`g(U)` onto :math:`p(U)` for each :math:`g \in G` so we have a covering 
    space. Each element of :math:`G` acts as a deck transformation, and the covering space is 
    normal since :math:`g_2g_1^{-1}` takes :math:`g_1(U)` to :math:`g_2(U)`. The deck transformation group contains
    :math:`G` as a subgroup, and equals this subgroup if :math:`Y` is path-connected, since if :math:`f` is any
    deck transformation, then for an arbitrarily chosen point :math:`y \in Y` and :math:`f(y)` are 
    in the same orbit and there is a :math:`g \in G` with :math:`g(y) = f(y)`, hence :math:`f=g` since deck
    transformations of a path-connected covering space are uniquely determined by where 
    they send a point. The final statement of the proposition is immediate from part (b)
    of :ref:`Proposition 1.39 <Proposition 1.39>`. |qed|

|
|indent| In view of the preceding proposition, we shall call an action satisfying (:math:`{\Large *}`) a 
**covering space action**. This is not standard terminology, but there does not seem to 
be a universally accepted name for actions satisfying (:math:`{\Large *}`). Sometimes these are called
'properly discontinuous' actions, but more often this rather unattractive term means
something weaker: Every point :Math:`x \in X` has a neighborhood :math:`U` such that :math:`U \cap g(U)` 
is nonempty for only finitely many :math:`g \in G`. Many symmetry groups have this proper
discontinuity property without satisfying (:math:`{\Large *}`), for example the group of symmetries 
of the familiar tiling of :Math:`\mathbb{R}^2` by regular hexagons. The reason why the action of this
group on :math:`\mathbb{R}^2` fails to satisfy (:math:`{\Large *}`) is that there are **fixed points**: points :Math:`y` for which
there is a nontrivial element :math:`g \in G` with :math:`g(y)=g`. For example, the vertices of the 
ehxagons are fixed by the :math:`120` degree rotations abotu these points, and the midpoints 
of edges are fixed by :math:`180` degree rotations. An action without fixed points is called a 
**free** action. Thus for a free action of :math:`G` on :math:`Y`, only the identity element of :math:`G` fixes any 
point of :math:`Y`. This is equivalent to requiring that all the images :math:`g(y)` of each :math:`y \in Y` are 
distinct, or in other owrds :math:`g_1(y)=g_2(y)` only when :math:`g_1 = g_2`, since :math:`g_1(y)=g_2(y)`
is equivalent to :math:`g^{-1}_1g_2(y)=y`. Though condition (:math:`{\Large *}`) implies freeness, the converse
is not always true. An example is the action of :math:`\mathbb{Z}` on :math:`S^1` in which a generator of :math:`\mathbb{Z}` acts
by rotation through an angle :math:`\alpha` that is an irrtional multiple of :math:`2\pi`. In this case each
orbit :math:`\mathbb{Z}y` is dense in :math:`S^1`, so condition (:math:`{\Large *}`) cannot hold since it implies that orbits are 
discrete subspaces. An exercise at the end of the section is to show that for actions 
on Hausdorff spaces, freeness plus proper discontinuity implies condition (:math:`{\Large *}`). Note
that proper discontinuity is automatic for actions by a finite group.
|

.. _Example 1.41:

.. container::

    .. image:: fig/eg-1-41.png
        :align: right
        :width: 30%

    **Example 1.41.** Let :math:`Y` be the closed orientable surface of genus :math:`11`, an ':math:`11`-hole torus' as 
    shown in the figure. This has a :math:`5`-fold rotational symmetry,
    generated by a rotation of angle :math:`2\pi / 5`. Thus we have 
    the cyclic group :math:`\mathbb{Z}_5` acting on :math:`Y`, and the condition (:math:`{\Large *}`) is
    obviously satisfied. The quotient space :Math:`Y/\mathbb{Z}_5` is a surface
    of genus :math:`3`, obtained from one of the five subsrufaces of 
    :math:`Y` cut off by the circles :math:`C_1, \cdots, C_5` by identifying its two
    boundary circles :math:`C_i` and :math:`C_{i+1}` to form the circle :math:`C` as 
    shown. Thus we have a covering space :math:`M_{11} \rightarrow M_3` where
    :math:`M_g` denotes the closed orientable surface of genus :math:`g`.
    In particular, we see that :math:`\pi_1(M_3)` contains the 'larger'
    group :math:`\pi_1(M_{11})` as a normal subgroup of index :math:`5`, with
    quotient :math:`\mathbb{Z}_5`. This example obviously generalizes by 
    replacing the two holes in each 'arm' of :Math:`M_{11}` by :math:`m` holes and the :math:`5`-fold symmetry by
    :math:`n`-fold symmetry. This gives a covering space :math:`M_{mn+1} \rightarrow M_{m+1}`. An exercise in :ref:`§2.2 <Section 2.2>` is
    to show by an Euler characteristic argument that if there is a covering space :math:`M_g \rightarrow M_g`
    then :math:`g=mn+1` and :math:`h=m+1` for some :math:`m` and :math:`n`.

|
|indent| As a special case of the final statement of the preceding proposition we see that
for a covering space action of a group :math:`G` on a simply-connected locally path-connected
space :math:`Y`, the orbit spacer :math:`Y/G` has fundamental group isomorphic to :Math:`G`. Under this 
isomorphism an element :math:`g \in G` corresponds to a loop in :math:`Y/G` that is the projection of
a path in :math:`Y` from a chosen basepoint :Math:`y_0` to :math:`g(y_0)`. Any two such paths are homotopic
since :math:`Y` is simply-connected, so we get a well0defined element of :Math:`\pi_1(y/G)` associated
to :math:`g`.

|indent| This method for computing fundamental groups vai group actions on simply-connected
spaces is essentially how we computed :Math:`\pi_1(S^1)` in :ref:`§1.1 <Section 1.1>`, via the covering
space :math:`\mathbbR{} \rightarrow S^1` arising from the action of :Math:`\mathbb{Z}` on :math:`\mathbb{R}` by translations. This is a useful general
technique for computing fundamental groups, in fact. Here are some examples 
illustrating this idea.

.. _Example 1.42:

.. container::

    **Example 1.42.** Consider the grid in :math:`\mathbb{R}^2` formed by the horizontal and vertical lines
    through points in :math:`\mathbb{Z}^2`. 

    .. image:: fig/eg-1-42.png
        :align: right
        :width: 30%

    Let us decorate this grid with arrows in either of the two ways 
    shown in the figure, the difference between the two
    cases being that in the second case the horizontal
    arrows in adjacent lines point in opposite directions.
    The group :math:`G` consisting of all symmetries
    of the first decorated grid is isomorphic to :Math:`\mathbb{Z} \times \mathbb{Z}`
    since it consists of all translations :math:`(x,y) \mapsto (x+m,y+n)` for :Math:`m,n \in \mathbb{Z}`. For the
    second grid the symmetry group :math:`G` contains a subgroup of translations of the form
    :math:`(x,y_ \mapsto (x+m, y+2n))` for :math:`m,n \in \mathbb{Z}`, but there are also glide-reflection symmetries
    consisting of vertical translation by an odd integer distance followed by reflection
    across a vertical line, either a vertical line of the grid or vertical line halfway between
    two adjacent grid lines. For both decorated grids there are elements of :math:`G` taking any
    square to nay other, butr only the identity element of :math:`G` takes a square to itself. The
    minimum distance any point is moved by a nontrivial element of :math:`G` is :math:`1`, which easily
    implies the covering space condition (:math:`{\Large *}`). The orbit space :math:`\mathbb{R}^2/G` is the quotient space
    of a square in the grid with opposite edges identified according to the arrows. Thus
    we see that the fundamental groups of the torus and the Klein bottle are the symmetry
    groups :math:`G` in the two cases. In the second case the subgroup of :math:`G` formed by the 
    translations ahs index two, and the orbit space for this subgroup is a torus forming a 
    two-sheeted covering spaces of the Klein bottle.

|
.. _Example 1.43:

**Example 1.43:** :math:`\mathbb{R}P^n`. The antipodal map of :Math:`S^n.\. x\mapsto -x`, generates an action of :math:`\mathbb{Z}_2`
on :math:`S^n` with orbit space :math:`\mathbb{R}P^n`, real projective :math:`n`-space, as defined in :ref:`Example 0.4 <Example 0.4>`. The
action is a covering space action since each open hemisphere in :math:`S^n` is disjoint from
its antipodal image. As we saw in :ref:`Proposition 1.14 <Proposition 1.14>`, :math:`S^n` is simply-connected if :math:`n \geq 2`,
so from the covering space :math:`S^n \rightarrow \mathbb{R}P^n`we deduce that :math:`\pi_1(\mathbb{R}P^n) \approx \mathbb{Z}_2` for :math:`n \geq 2`. A
generator for :Math:`\pi_1(\mathbb{R}P^n)` is any loop obtained by projecting a path in :math:`S^n` connecting two
antipodal points. One can see explicitly that such a loop :math:`\gamma` has order two in :math:`\pi_1(\mathbb{R}P^n)`
if :Math:`n \geq 2` since the composition :math:`\gamma \cdot \gamma` lifts to a loop in :math:`S^n`, and this can be homotoped to 
the trivial loop since :math:`\pi_1(S^n) = 0`, so the projection of this homotopy into :Math:`\mathbb{R}P^n` gives
a nullhomotopy of :math:`\gamma \cdot \gamma`.



.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>