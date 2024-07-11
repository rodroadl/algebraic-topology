Induced Homomorphisms
=====================

|indent| Suppose :math:`\varphi:X \rightarrow Y` is a map taking the basepoint :math:`x_0 \in X` to the basepoint :math:`y_0 \in Y`.
For brevity we write :math:`\varphi:(X,x_0)\rightarrow (Y,y_0)` in this situation. Then :math:`\varphi` induces a homomorphism
:math:`\varphi_*: \pi_1(X,x_0) \rightarrow \pi_1(Y, y_0)`, defined by composing loops :math:`f:I \rightarrow X` based at 
:math:`x_0` with :math:`\varphi`, that is :math:`\varphi_*[f_0]=[\varphi f_0]=[\varphi f_1]=\varphi_* [f_1]`. Furthermore, :math:`\varphi_*` is a homomorphism
since :math:`\varphi (f\cdot g)=(\varphi f) \cdot (\varphi g)`, both functions having the value :math:`\varphi f(2s)` for :math:`0 \leq s \leq \frac{1}{2}`
and the value :math:`\varphi g(2s-1)` for :math:`\frac{1}{2} \leq s \leq 1`.

|indent| Two basic properties of induced homomorphisms are:

-   :math:`(\varphi \psi)_* = \varphi_* \psi_*` for a composition :math:`(X,x_0)\xrightarrow{\psi}(Y,y_0)\xrightarrow{\varphi}(Z,z_0)`.
-   :math:`\mathbb{1}_* = \mathbb{1}`, which is a concise way of saying that the identity map :math:`\mathbb{1}:X\rightarrow X` induces
    the identity map :math:`\mathbb{1}:\pi_1(X,x_0) \rightarrow \pi_1(X,x_0)`.

The first of these follows from the fact that composition of maps is associative, so 
:math:`(\varphi \psi)f = \varphi(\psi f)`, and the second is obvious. These two properties of induced 
homomorphisms are what makes the fundamental group a functor. The formal definition 
of a functor requires the introduction of certain other preliminary concepts, however,
so we postpone this until it is needed in :ref:`§2.3 <sec 2.3>`.

|indent| As an application we can deduce easily that if :math:`\varphi` is a homeomorphism with inverse
:math:`\psi` then :math:`\varphi_*` is an isomorphism with inverse :math:`\varphi_* \psi_* = (\varphi \psi)_* = \mathbb{1}_* = \mathbb{1}`
and similarly :math:`\psi _* \varphi_* = \mathbb{1}`. We will use this fact in the following calculation of the 
fundamental groups of higher-dimensional spheres:

.. _proposition 1.14:

    **Proposition 1.14.** :math:`\pi_1(S^n)=0` *if* :math:`n \geq 2`.

|indent| The main step in the proof will be a general fact that will also play a key role in the next section:

.. _lemma 1.15:

.. container::

        **Lemma 1.15.** *If a space** :math:`X` *is the union of a collection of path-connected open sets* 
        :math:`A_\alpha` *each containing the basepoint* :math:`x_0 \in X` *and if each intersection* :math:`A_\alpha \cap A_\beta` *is 
        path-connected, then every loop in* :math:`X` *at* :math:`x_0` *is homotopic to a product of loops each of
        which is contained in a single* :math:`A_\alpha`

    **Proof:** Given a loop :math:`f:I \rightarrow X` at the basepoint :math:`x_0`, we claim there is a partition 
    :math:`0=s_0<s_1< \cdots < s_m = 1` of :math:`I` such that each subinterval :math:`[s_{i-1},s_i]` is mapped by :math:`f` to
    a single :math:`A_\alpha`. Namely, since  :math:`f` is continuous, each :math:`s \in I` has an open neighborhood
    :math:`V_s` in :math:`I` mapped by :math:`f` to some :math:`A_\alpha`. We may in fact take :math:`V_s` to be an interval whose
    closure is mapped to a single :math:`A_\alpha`. Compactness of :math:`I` implies that a finite number of 
    these intervals cover :math:`I`. The endpoints of this finite set of intervals then define the
    desired partition of :math:`I`

    |indent| Denote the :math:`A_\alpha` containing :math:`f([s_{i-1},s_i])` by :math:`A_i`, and let :math:`f_i` be the path obtained by
    restricting :math:`f` to :math:`[s_{i-1},s_i]`. Then :math:`f` is the composition :math:`f_1 \cdot \cdots \cdot f_m` with :math:`f_i` a path in
    :math:`A_i`. 
    
    .. image:: fig/lem-1-15.png
        :align: right
        :width: 40%
    
    Since we assume :math:`A_i \cap A_{i+1}` is path-connected,
    we may choose a path :math:`g_i` in :math:`A_i \cap A_{i+1}` from :math:`x_0` to
    the point :math:`f(s_i) \in A_i \cap A_{i+1}`. Consider the loop
    :math:`(f_1 \cdot \bar{g}_1) \cdot (g_1 \cdot f_2 \cdot \bar{g}_2) \cdot (g_2 \cdot f_3 \cdot \bar{g}_3) \cdot \cdots \cdot (g_{m-1} \cdot f_m)`
    which is homotopic to :math:`f`. This loop is a composition
    of loops each lying in a single :math:`A_i`, the loops indicated
    by the parentheses. |qed|

**Proof of Proposition 1.14:** We can express :math:`S^n` as the union of two open sets :math:`A_1`
and :math:`A_2` each homeomorphic to :math:`\mathbb{R}^n` such that :math:`A_1 \cap A_2` is homeomorphic to :math:`S^{n-1} \times \mathbb{R}`,
for example by taking :math:`A_1` and :math:`A_2` to be the complements of two antipodal points in
:math:`S^n`. Choose a basepoint :math:`x_0` in :math:`A_1 \cap A_2`. If :math:`n \geq 2` then :math:`A_1 \cap A_2` is path-connected.
The lemma then applies to say that every loop in :math:`S^n` based at :math:`x_0` is homotopic to a 
product of loops in :math:`A_1` or :math:`A_2`. Both :math:`\pi_1(A_1)` and :math:`\pi_1(A_2)` are zero since :math:`A_1` and :math:`A_2` are
homeomorphic to :math:`\mathbb{R}^n`. Hence every loop in :math:`S^n` is nullhomotopic. |qed|

.. _corollary 1.16:

.. container:: 

        **Corollary 1.16.** :math:`\mathbb{R}^2` *is not homeomorphic to** :math:`\mathbb{R}^n` *for* :math:`n \neq 2`.
    
    **Proof:** Suppose :math:`f:\mathbb{R}^2 \rightarrow \mathbb{R}^n` is a homeomorphism. The case :math:`n=1` is easily 
    disposed of since :math:`\mathbb{R}^2-\{0\}` is path-connected but the homeomorphic space :math:`\mathbb{R}^n-\{f(0)\}`
    is not path-connected when :math:`n=1`. When :math:`n>2` we cannot distinguish :math:`\mathbb{R}^2-\{0\}`
    from :math:`\mathbb{R}^n-\{f(0)\}` by the number of path-components, but we can distinguish them
    by their fundamental groupos. Namely, for a point :math:`x` in :math:`\mathbb{R}^n`, the complement :math:`\mathbb{R}^n-\{x\}`
    is homeomorphic to :math:`S^{n-1} \times \mathbb{R}`, so :ref:`Proposition 1.12 <proposition 1.12>` implies that :math:`\pi_1(\mathbb{R}^n-\{x\})` is
    isomorphic to :math:`\pi_1(S^{n-1}) \times \pi_1(\mathbb{R}) \approx \pi_1(S^{n-1})`. Hence :math:`\pi_1(\mathbb{R}^n -\{x\})` is :math:`\mathbb{Z}` for :math:`n=2` and
    trivial for :math:`n>2`, using :ref:`Proposition 1.14 <proposition 1.14>` in the latter case. |qed|

|indent| The more general statement that :math:`\mathbb{R}^m` is not homeomorphic to :math:`\mathbb{R}^n` if :math:`m \neq n` can
be proved in the same way using either the higher homotopy groups or homology 
groups. In fact, nonempty open sets in :math:`\mathbb{R}^m` and :math:`\mathbb{R}^n` can be homeomorphic only if
:math:`m=n`, as we will show in :ref:`Theorem 2.26 <theorem 2.26>` using homology.

|indent| induced homomorphisms allow relations between spaces to be transformed into
relations between their fundamental groups. Here is an illustration of this principle:

.. _proposition 1.17:

.. container::

        **Proposition 1.17.** *If a space* :math:`X` *retracts onto a subspace* :math:`A`, *then the homomorphism*
        :math:`i_*:\pi_1 (A,x_0) \rightarrow \pi_1(X,x_0)` *induced by the inclusion* :math:`i:A \hookrightarrow X` *is injective. If* :math:`A` *is a
        deformation retract of* :math:`X`, then :math:`i_*` is an isomorphism.
    
    **Proof:** If :math:`r:X\rightarrow A` is a retraction, then :math:`ri=\mathbb{1}`, which implies that :math:`i_*`
    is injective. If :math:`r_t:X \rightarrow X` is a deformation retraction of :math:`X` onto :math:`A`, so :math:`r_0=\mathbb{1},\, r_t|A =\mathbb{1}`,
    and :math:`r_1(X) \subset A`, then for any loo :math:`f:I\rightarrow X` based at :math:`x_0 \in A` the composition :math:`r_t f` gives
    a homotopy of :math:`f` to a loop in :math:`A`, so :math:`i_*` is also surjective. |qed|

|indent| This gives another way of seeing that :math:`S^1` is not a retract of :math:`D^2`, a fact we showed
earlier in the proof of the :ref:`Brouwer fixed point theorem <theorem 1.9>`, since the inclusion-induced
map :math:`\pi_1(S^1)\rightarrow \pi_1(D^2)` is a homomorphism :math:`\mathbb{Z}\rightarrow 0` that cannot be injective.

|indent| The exact group-theoretic analog of a retraction is a homomorphism :math:`\rho` of a group
:math:`G` onto a subgroup :math:`H` such that :math:`\rho` restricts to the identity on :math:`H`. In the notation
above, if we identify :math:`\pi_1(A)` with its image under :math:`i_*`, then :math:`r_*` is such a homomorphism
from :math:`\pi_1(X)` onto the subgroup :math:`\pi_1(A)`. The existence of a retracting homomorphism
:math:`\rho : G \rightarrow H` is quite a strong condition on :math:`H`. If :math:`H` is a normal subgroup, it implies that
:math:`G` is the direct product of :math:`H` and the kernel of :math:`\rho`. If :math:`H` is not normal, then :math:`G` is what
is called in group theory the semi-direct product of :math:`H` and the kernel of :math:`\rho`.

|indent| Recall from Chapter 0 the general definition of a homotopy as a family :math:`\varphi_t : X \rightarrow Y,\, t\in I`,
such that the associated map :math:`\Phi : X \times I \rightarrow Y ,\, \Phi(x,t) = \varphi_t(x)`, is continuous. If :math:`\varphi_t`
takes a subspace :math:`A \subset X` to a subspace :math:`B \subset Y` for all :math:`t`, then we speak of a homotopy of
maps of pairs, :math:`\varphi_t : (X,A) \rightarrow (Y,B)`. In particular, a **basepoint-preserving homotopy**
:math:`\varphi_t:(X,x_0) \rightarrow (Y, y_0)` is the case that :math:`\varphi_t(x_0)=y_0` for all :math:`t`. Another basic property
of induced homomorphisms is their invariance under such homotopies:

- If :math:`\varphi_t:(X,x_0)\rightarrow (Y,y_0)` is a basepoint-preserving homotopy, then :math:`\varphi_{0*} = \varphi_{1*}`.

This holds since :math:`\varphi{0*}[f]=[\varphi_0 f]=[\varphi_1f]=\varphi_{1*}[f]`, the middle equality coming 
from the homotopy :math:`\varphi_t f`.

|indent| There is a notion of homotopy equivalence for spaces with basepoints. One says
:math:`(X, x_0) \simeq (Y,y_0)` if there are maps :math:`\varphi : (X,x_0) \rightarrow (Y, y_0)` and :math:`\psi : (Y,y_0)\rightarrow (X, x_0)`
with homotopies :math:`\varphi \psi \simeq \mathbb{1}` and :math:`\psi \varphi \simeq \mathbb{1}` through maps fixing the basepoints. In
this case the induced maps on :math:`\pi_1` satisfy :math:`\varphi_* \psi_* = (\varphi \psi)_* = \mathbb{1}_*=\mathbb{1}` and likewise
:math:`\psi_* \varphi_* = \mathbb{1}`, so :math:`\varphi_*` and :math:`\psi_*` are inverse isomorphisms :math:`\pi_1(X,x_0)\approx \pi_1(Y,y_0)`. This
somewhat formal argument gives another proof that a deformation retration induces 
an isomorphism on fundamental groups, since if :math:`X` deformation retracts onto :math:`A` then
:math:`(X,x_0) \simeq (A,x_0)` for any choice of basepoint :math:`x_0 \in A`.

|indent| Having to pay so much attention to basepoints when dealing with the fundamental
groups is something of a nuisance. For homotopy equivalences one does not have to
be quite so careful, as the conditions on basepoints can actually be dropped:

.. _proposition 1.18:

    **Proposition 1.18.** *If* :math:`\varphi : X \rightarrow Y` *is a homotopy equivalence, then the induced homomorphism*
    :math:`\varphi_*:\pi_1(X,x_0) \rightarrow \pi_1(Y, \varphi(x_0))` *is an isomorphism for all* :math:`x_0 \in X`.

|indent| The proof will use a simple fact about homotopies that do not fix the basepoint:

.. _lemma 1.19:

.. container::



    ..

        .. image:: fig/lem-1-19.png
            :align: right
            :width: 40%

        **Lemma 1.19.** *If* :math:`\varphi_t:X \rightarrow Y` *is a homotopy and* :math:`h` *is the path* :math:`\varphi_t(x_0)` *formed by the images of
        a basepoint* :math:`x_0 \in X`, *then the three maps in the diagram at the right satisfy* :math:`\varphi_{0*}=\beta_h \varphi_{1*}`.

    ..

    .. image:: fig/lem-pf-1-19.png
        :align: right
        :width: 30%

    **Proof:** Let :math:`h_t` be the restriction of :math:`h` to the interval :math:`[0,t]`,
    with a reparametrization so that the domain of :math:`h_t` is still
    :math:`[0,1]`. Explicitly, we can take :math:`h_t(x)=h(ts)`. Then if :math:`f` is 
    a loop in :math:`X` at the basepoint :math:`x_0`, the product :math:`h_t \cdot (\varphi_t f) \cdot \bar{h}_t`
    gives a homotopy of loops at :math:`\varphi_0(x_0)`. Restricting this
    homotopy to :math:`t=0` and :math:`t=1`, we see that :math:`\varphi_{0*}([f])=\beta_h(\varphi_{1*}([f]))`. |qed|

**Proof of 1.18:** Let :math:`\psi : Y \rightarrow X` be a homotopy-inverse for :math:`\varphi`, so that :math:`\varphi \psi \simeq \mathbb{1}` and
:math:`\psi \varphi \simeq \mathbb{1}`. Consider the maps

.. math::

    \pi_1(X,x_0) \xrightarrow{\varphi_*} \pi_1(Y,\varphi (x_0)) \xrightarrow{\varphi_*} \pi_1(X,\psi \varphi (x_0)) \xrightarrow{\varphi_*} \pi_1(Y,\varphi \psi \varphi (x_0))

The composition of the first two maps is an isomorphism since :math:`\psi \varphi \simeq \mathbb{1}` implies that 
:math:`\psi_* \varphi_* = \beta_h` for some :math:`h`, by the :ref:`lemma <lemma 1.19>`. In particular, since :math:`\psi_* \varphi_*` is an isomorphism,
:math:`\varphi_*` is injective. The same reasoning with the second and third maps shows that :math:`\psi_*` 
is injective. Thus the first two of the three maps are injections and their composition
is an isomorphism, so the first map :math:`\varphi_*` must be surjective as well as injective. |qed|













.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>