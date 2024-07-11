.. _paths-and-homotopy:

Paths and Homotopy
==================

The fundamental group will be defined in terms of loops and deformations of 
loops. Sometimes it will be useful to consider more generally paths and their
deformations, so we begin with this slight extra generality.

By a **path** in a space :math:`X` we mean a continuous map :math:`f:I \rightarrow X` where :math:`I` is the unit
interval [0,1]. The idea of continuously deforming a path, keeping its endpoints
fixed, is made precise by the following defintion. A **homotopy** of paths in :math:`X` is a 
family :math:`f_t: I \rightarrow X, \, 0 \leq t \leq 1`, such that

.. image::fig/homotopic.png
    :align: right
    :width: 40%

When two paths :math:`f_0` and :math:`f_1` are connected in this way by a homotopy :math:`f_t`, they are said
to be **homotopic**. The notation for this :math:`f_0 \simeq f_1`.

.. _example 1.1:

.. container:: no-indent

    **Example 1.1: Linear Homotopies.** Any tow paths :math:`f_0` and :math:`f_1` in :math:`\mathbb{R}^n` having the same
    endpoints :math:`x_0` and :math:`x_1` are homotopic via the homotopy :math:`f_t(s)=(1-t)f_0(s)+tf_1(s)`.
    During this homotopy each point :math:`f_0(s)` travels along the line segment to :math:`f_1(s)` at constant
    speed. This is because the line through :math:`f_0(s)` and :math:`f_1(s)` is linearly parametrized
    as :math:`f_0(s)+t[f_1(s)-f_0(s)]=(1-t)f_0(s)+tf_1(s)`, with the segment from :math:`f_0(s)` 
    then this segment degenerates to a point and :math:`f_t(s)=f_0(s)` for all :math:`t`. This occurs in
    particular for :math:`s=0` and :math:`s=1`, so each :math:`f_t` is a path from :math:`x_0` to :math:`x_1`. Continuity of 
    the homotopy :math:`f_t` as a map :math:`I \times I \rightarrow \mathbb{R}^n` follows from continuity of :math:`f_0` and :math:`f_1` since the 
    algebraic operations of vector addition and scalar multiplication in the formula for :math:`f_t`
    are continuous.

This construction shows more generally that for a convex subspace :math:`X \subset \mathbb{R}^n`, all
paths in :math:`X` with given endpoints :math:`x_0` and :math:`x_1` are homotopic, since if :math:`f_0` and `f_1` lie in
:math:`X` then so does the homotopy :math:`f_t`.

Before proceeding further we need to verify a technical property:

.. _proposition 1.2:

.. container:: no-indent

        **Proposition 1.2.** *The relation of homotopy on paths with fixed endpoints in any space 
        is an equivalence relation*

    .. container:: indent

        The equivalence class of a path :math:`f` under the equivalence relation of homotopy
        will be denoted :math:`[f]` and called the **homotopy class** of :math:`f`.
    
    **Proof:** Reflexivity is evident since :math:`f \simeq f` by the constant homotopy :math:`f_t = f`. Symmetry
    is also easy since if :math:`f_0 \simeq f_1` via :math:`f_t`, then :math:`f_1 \simeq f_0` via the inverse homotopy :math:`f_{1-t}`. 
    
    
    .. image:: fig/proposition-1.2.png
        :align: right
        :width: 25%
    
    For transitivity, if :math:`f_0 \simeq f_1` via :math:`f_t` and if :math:`f_1 = g_0` with :math:`g_0 \simeq g_1`
    via :math:`g_t`, then :math:`f_0 \simeq g_1` via the homotopy :math:`h_t` that equals :math:`f_{2t}` for 
    :math:`0 \leq t \leq \frac{1}{2}` and :math:`g_{2t-1}` for :math:`\frac{1}{2} \leq t \leq 1`. These two definitions
    agree for :math:`t=\frac{1}{2}` since we assume :math:`f_1 = g_0`. Continuity of the 
    associated map :math:`H(s,t)=h_t(s)` comes from the elemetary
    fact, which will be used frequently without explicit mention, that a function defined
    on the union of two closed sets is continuous if it is continuous when restricted to 
    each of the closed sets separately. In the case at hand we have :math:`H(s,t)=F(s,2t)` for 
    :math:`0 \leq t \leq \frac{1}{2}` and :math:`H(s,t) = G(s, 2t-1)` for :math:`\frac{1}{2} \leq t \leq 1` where :math:`F` and :math:`G` are the maps
    :math:`I \times I \rightarrow X` associated to the homotopies :math:`f_t` and :math:`g_t`. Since :math:`H` is continuous on :math:`I \times [0, \frac{1}{2}]`
    and on :math:`I \times [\frac{1}{2}, I]`, it is continuous on :math:`I \times I`. |qed|


Given two paths :math:`f,g:I \rightarrow X` such that :math:`f(1) = g(0)`, there is a **composition** or
**product path** :math:`f\cdot g` that traverses first :math:`f` and then :math:`g`, defined by the formula

.. math::
    
    f\cdot g =
    \begin{cases}
    f(2s) & 0 s \leq \frac{1}{2} \\
    g(2s-1) & \frac{1}{2} \leq s \leq 1
    \end{cases}

.. image:: fig/composition.png
    :align: right
    :width: 30%

Thus :math:`f` and :math:`g` are traversed twice as fast in order for :math:`f\cdot g` to be traversed in unit
time. This product operation respects homotopy classes 
since if :math:`f_0 \simeq f_1` and :math:`g_0 \simeq g_1` via homotopies :math:`f_1` and :math:`g_t`,
and if :math:`f_0(1) = g_0(0)` so that :math:`f_0\cdot g_0` is defined, then :math:`f_t \cdot g_t`
is defined and provides a homotopy :math:`f_0 \cdot g_0 \simeq f_1 \cdot g_1`.

In particular, suppose we retrict attention to paths :math:`f: I \rightarrow X` with the same starting
and ending point :math:`f(0) = f(1) =x_0 \in X`. Such pats are called **loops**, and the 
common starting and ending point :math:`x_0` is referred to as the **basepoint**. The set of all
homotopy classes :math:`[f]` of loops :math:`f:I \rightarrow X` at the basepoint :math:`x_0` is denoted :math:`\pi_1(X,x_0)`.

.. _proposition 1.3.:

.. container:: no-indent

        **Proposition 1.3.** :math:`\pi_1(X,x_0)` *is a group with respect to the product* :math:`[f][g]=[f\cdot g]`.

    .. container:: indent

        This group is called the **fundamental group** of :math:`X` at the basepoint :math:`x_0`. We 
        will see in :ref:`Chapter 4<chapter 4>` that :math:`\pi_1(X, x_0)` is the first in a sequence of groups :math:`\pi_n(X,x_0)`,
        called homotopy groups, which are defined in an entirely analogous fashion using the 
        :math:`n`-dimensional cube :math:`I^n` in place of :math:`I`.
    
    .. container:: no-indent-no-margin

        **Proof:** By restricting attention to loops with a fixed basepoint :math:`x_0 \in X` we guarantee 
        that the product :math:`f\cdot g` of any two such loops is defined. We have already observed
        that the homotopy class of :math:`f \cdot g` depends only on the homotopy classes of :math:`f` and :math:`g`,
        so the product :math:`[f][g]=[f\cdot g]` is well-defined. It remains to verify the three axioms 
        for a group.

    .. container:: indent-no-margin

        As a preliminary step, define a **reparametrization** of a path :math:`f` to be a 
        composition :math:`f\varphi` where :math:`\varphi:I \rightarrow I` is any continuous map such that :math:`\varphi(0)=0` and :math:`\varphi(1)=1`.
        Reparametrizing a path preserves its homotopy class since :math:`f\varphi \simeq f` via the homotopy
        :math:`f\varphi_t` where :math:`\varphi_t(s) = (1-t)\varphi(s) + ts` so that :math:`\varphi_0 = \varphi` and :math:`\varphi_1(s) = s`. Note that 
        :math:`(1-t)\varphi(s)+ts` lies between :math:`\varphi(s)` and :math:`s`, hence is in :math:`I`, so the composition :math:`f\varphi_t` is 
        defined.

        .. image:: fig/reparametrization.png
            :align: right
            :width: 25%

        If we are given paths :math:`f,\, g,\, h` with :math:`f(1)=g(0)` and :math:`g(1)=h(0)`, then both products
        :math:`(f\cdot g)\cdot h` and :math:`f\cdot (g\cdot h)` are defined, and :math:`f\cdot(g\cdot h)` is a reparametrization
        of :math:`(f\cdot g)\cdot h` by the piecewise linear function :math:`\varphi` whose graph is shown
        in the figure at the right. Hece :math:`(f \cdot g)\cdot h \simeq f \cdot(g\cdot h)`. Restricting attention
        to loops at the basepoint :math:`x_0`, this says the product in :math:`\pi_1(X, x_0)` is 
        associative.

        .. image:: fig/two-graphs.png
            :align: right
            :width: 40%

        Given a path :math:`f:I\rightarrow X`, let :math:`c` be the constant path at :math:`f(1)`, defined by :math:`c(s)=f(1)`
        for all :math:`s\in I`. Then :math:`f\cdot c` is a reparametrization of :math:`f` via the function :math:`\varphi` whose graph is
        shown in the first figure at the right, so :math:`f \cdot c \simeq f`. Similarly,
        :math:`c \cdot f \simeq f` where :math:`c` is now the constant path at :math:`f(0)`, using 
        the reparametrization function in the second figure. Taking 
        :math:`f` to be a loop, we deduce that the homotopy class of the 
        constant path at :math:`x_0` is a two-sided identity in :math:`\pi_1(X,x_0)`.

        For a path :math:`f` from :math:`x_0` to :math:`x_1`, the **inverse path** :math:`\mathbf{\bar{f}}` from :math:`x_1` back to :math:`x_0` is defined
        by :math:`\bar{f}(s)=f(1-s)`. To see that :math:`f \cdot \bar{f}` is homotopic to a constant path we use the
        homotopy :math:`h_t = f_t \cdot g_t` where :math:`f_t` is the path that equals :math:`f` on the interval :math:`[0,1-t]`
        and that is stationary at :math:`f(1-t)` on the interval :math:`[1-t,1]`, and :math`g_t` is the inverse path of 
        :math:`f_t`.

        .. image:: fig/inverse.png
            :align: right
            :width: 25%
        
    .. container:: indent
        
        We could also describe :math:`h_t` in terms of the associated function
        :math:`H:I \times I \rightarrow X` using the decomposition of :math:`I\times I` shown in the figure. On
        the bottom edge of the square :math:`H` is given by :math:`f \cdot \bar{f}` and below the 'V' we 
        let :math:`H(s,t)` be independent of :math:`t`, while above the 'V' we let :math:`H(s,t)` be 
        independent of :math:`s`. Going back to the first description of :math:`h_t`, we see that since :math:`f_0 = f`
        and :math:`f_1` is the constant path :math:`c` at :math:`x_0,\, h_t` is homotopy from :math:`f\cdot \bar{f}` to :math:`c\cdot \bar{c}`. Replacing
        :math:`f` by :math:`\bar{f}` gives :math:`\bar{f}\cdot f \simeq c` for :math:`c` the constant path at :math:`x`. Taking :math:`f` to be a loop at the 
        basepoint :math:`x_0`, we deduce that :math:`[\bar{f}]` is a two-sided inverse for :math:`[f]` in :math:`\pi_1(X,x_0)`. |qed|

.. _example 1.4:

.. container:: no-indent

    **Example 1.4.** For a convex set :math:`X` in :math:`\mathbb{R}^n` with basepoint :math:`x_0 \in X` we have :math:`\pi_1(X,x_0)=0`,
    the trivial group, since any two loops :math:`f_0` and :math:`f_1` based at :math:`x_0` are homotopic via the
    linear homotopy :math:`f_t(s)=(1-t)f_0(s)+tf_1(s)`, as described in :ref:`Example 1.1 <example 1.1>`.

It is not so easy to show that a space has a nontrivial fundamental group since one
must somehow demonstarte the nonexistence of homotopies between certain loops.
We will tackle the simplest example shortly, computing the fundamental group of the circle.

It is natural to ask about the dependence of :math:`\pi_1(X,x_0)` on the choice of the basepoint
:math:`x_0`. Since :math:`\pi_1(X,x_0)` involves only path-component of :math:`X` containing :math:`x_0`, it 
is clear that we can hope to find relation between :math:`\pi_1(X,x_0)` and :math:`\pi_1(X,x_0)` for two
basepoints :math:`x_0` and :math:`x_1` only if :math:`x_0` and :math:`x_1` lie in the same path-component of :math:`X`.

.. image:: fig/change-of-basepoint.png
    :align: right
    :width: 30%

So let :math:`h : I \rightarrow X` be a pathfrom :math:`x_0` to :math:`x_1`, with the inverse path
:math:`\bar{h}(s)=h(1-s)` from :math:`x_1` the loop :math:`h \cdot f \cdot \bar{h}` based at :math:`x_0`.
Strictly speaking, we should choose an order of forming the product :math:`h \cdot f \cdot \bar{h}`, either
:math:`(h \cdot f)` or :math:`h \cdot (f \cdot \bar{h})`, but the two choices are homotopic and we are only interested in
homotopy classes here. Alternatively, to avoid any ambiguity we could define a general
:math:`n`-fold product :math:`f_1 \cdot \cdots f_n` in which the path :math:`f_i` is traversed in the time interval
:math:`[\frac{i-1}{n}, \frac{i}{n}]`. Either way, we defie a **change-of-basepoint** map :math:`\beta_h : \pi_1(X,x_1) \rightarrow \pi_1(X,x_0)`
by :math:`\beta_h [f] = [h \cdot f \cdot \bar{h}]`. This is well-defined since if :math:`f_t` is a homotopy of loops based at 
:math:`x_1` then :math:`h \cdot f_t \cdot \bar{h}` is a homotopy of loops based at :math:`x_0`.

.. _proposition 1.5.:

.. container:: no-indent

            **Proposition 1.5.** *The map* :math:`\beta_h : \pi_1(X,x_1) \rightarrow \pi_1 (X,x_0)` *is an isomorphism*.

        **Proof:** We see first that :math:`\beta_h` is a homomorphism since :math:`\beta_h[f \cdot g] = [h \cdot f \cdot g \cdot \bar{h}] = [h \cdot f \cdot \bar{h} \cdot h \cdot g\cdot \bar{h}] = \beta_h[f]\beta_h[g]`.
        Further, :math:`\beta_h` is an isomorphism with inverse :math:`\beta_{\bar{h}}` since
        :math:`\beta_h \beta_{\bar{h}}=\beta_h[\bar{h} \cdot f \cdot h]=[h \cdot \bar{h} \cdot f \cdot h \cdot \bar{h}] = [f]`, and similarly :math:`\beta_{\bar{h}}\beta_h[f]=[f]`. |qed|
    
Thus if :math:`X` is path-connected, the group :math:`\pi_1(X,x_0)` is, up to isomorphism, independent
of the choice of basepoint :math:`x_0`. In this case the notation :math:`\pi_1(X,x_0)` is often
abbreviated to :math:`\pi_1(X)`, or one could go further and write just :math:`\pi_1 X`.

In general, a space is called **simply-connected** if it is path-connected and has 
trivial fundamental group. The following result explains the name.

.. _proposition 1.6.:

.. container:: no-indent

        **Proposition 1.6.** *A space* :math:`X` *is simply-connected iff there is a unique homotopy class
        of paths connecting any two points in* :math:`X`.

    **Proof:** Path-connectedness is the existence of paths connecting every pair of points,
    so we need to be concerned only with the uniqueness of connecting paths. Suppose 
    :math:`\pi_1(X)=0`. If :math:`f` and :math:`g` are two paths from :math:`x_0` to :math:`x_1`, then :math:`f \simeq f \cdot \bar{g}\cdot g\simeq g` since
    the loops :math:`\bar{g} \cdot g` and :math:`f \cdot \bar{g}` are each homotopic to constant loops, using the assumption
    :math:`\pi_1(X,x_0)=0` in the latter case. Conversely, if there is only one homotopy class of 
    paths connecting a basepoint :math:`x_0` to itself, then all loops at :math:`x_0` are homotopic to the 
    constnat loop and :math:`\pi_1(X,x_0)=0`.

    




.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>