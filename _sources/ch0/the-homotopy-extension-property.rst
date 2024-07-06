The Homotopy Extension Property
===============================

In this final section of the chapter we will actually prove a few things, including 
the two criteria for homotopy equivalence described above. The proofs depend upon 
a technical property that arises in many other contexts as well. Consider the following 
problem. Suppose one is given a map :math:`f_0:X \rightarrow Y`, and on a subspace :math:`A \subset X` one is also 
given a homotopy :math:`f_t:A \rightarrow Y` of :math:`f_0 \mid A` that one would like to extend to a homotopy 
:math:`f_t:X \rightarrow Y` of the given :math:`f_0`. If the pair :math:`(X,A)` has the **homotopy extension property**. Thus 
:math:`(X,A)` has the homotopy extension property if every pair of maps :math:`X \times \{0\} \rightarrow Y` and 
:math:`A \times I \rightarrow Y` that agree on :math:`A \times \{0\}` can be extended to a map :math:`X \times I \rightarrow Y`.

    *A pair* :math:`(X,A)` *has the homotopy extension property if and only if* :math:`X \times \{0\} \cup A \times I` *is a
    retract of* :math:`X \times I`.

.. container:: no-indent
        
    For one implication, the homotopy extension property for :math:`(X,A)` implies that the 
    identity map :math:`X \times \{0\} \cup A \times I \rightarrow X \times \{0\} \cup A \times I` extends to a map :math:` X \times I \rightarrow X \times \{0\} \cup A \times I`,
    so :math:`X \times \{0\} \cup A \times I` is a retract of :math:`X \times I`. The converse is equally easy when :math:`A` is closed 
    in :math:`X`. Then any two maps :math:`X \times \{0\} \rightarrow Y` and :math:`A \times I \rightarrow Y` that agree on :math:`A \times \{0\}` combine 
    to give a map :math:`X \times \{0\} \cup A\times I \rightarrow Y` which is continuous since it is continuous on the 
    closed sets :math:`X \times \{0\}` and :math:`A \times I`. By composing this map :math:`X \times \{0\} \cup A \times I \rightarrow Y` with a 
    retraction :math:`X \times I \rightarrow X \times \{0\} \cup A \rightarrow I` we get an extension :math:`X \times I \rightarrow Y`, so :math:`(X,A)` has the 
    homotopy extension property. The hypothesis that :math:`A` is closed can be avoided by a 
    mor complicated argument given in the Appendix. If :math:`X \times \{0\} \cup A \times I` is a retract of 
    :math:`X \times I` and :math:`X` is Hausdorff, then :math:`A` must in fact be closed in :math:`X`. For if :math:`r:X \times I \rightarrow X \times I`
    is a retraction onto :math:`X\times \{0\} \cup A \times I`, then the iamge of :math:`r` is the set of points :math:`z \in X \times I` 
    with :math:`r(z)=z`, a closed set if :math:`X` is Hausdorff, so :math:`X \times \{0\} \cup A\times I` is closed in :math:`X \times I` and 
    hence :math:`A` is closed in :math:`X`.

A simple example of a pair :math:`(X,A)` with :math:`A` closed for which the homotopy 
extension property fails is the pair :math:`(I,A)` where :math:`A = \{0, 1, \dfrac{1}{2}, \dfrac{1}{3}, \dfrac{1}{4},\cdots \}`. It is not hard to 
show that there is no continuous retraction :math:`I\times I \rightarrow I \times \{0\} \cup A \times I`. The breakdown of 
homotopy extension here can be attributed to the bad structure of :math:`(X,A)` near :math:`0`.
With nicer local structure the homotopy extension property does hold, as the next example shows.

.. _Example 0.15:

.. container:: no-indent

    .. image:: fig/example-0-15.png
        :align: right
        :width: 25%

    **Example 0.15**. A pair :math:`(X,A)` has the homotopy extension property if :math:`A` has a mapping
    cylinder neighborhood in :math:`X`, by which we mean a closed 
    neighborhood :math:`N` containing a subspace :math:`B`, thought of as the 
    boundary of :math:`N`, with :math:`N-B` an open neighborhood of :math:`A`, 
    such that there exists a map :math:`f:B \rightarrow A` and a homeomorphism 
    :math:`h:M-f \rightarrow N` with :math:`h \mid A \cup B = \mathbb{1}`. Mapping cylinder neighborhoods 
    like this occur fairly often. For example, the thick letters 
    discussed at the beginning of the chapter provide such 
    neighborhoods of the thin letters, regarded as subspaces of the plane. To verify the 
    homotopy extension property, notice first that :math:`I \times I` retracts onto :math:`I \times \{0\} \cup \partial I \times I`, hence 
    :math:`B \times I \times I` retracts onto :math:`B \times I \times \{0\} \cup B \times \partial I \times I`, and this retraction induces a retraction 
    of :math:`M_f \times I` onto :math:`M_f \times \{0\} \cup (A \cup B) \times I`. Thus :math:`(M_f, A \cup B)` has the homotopy extension 
    property. Hence so does the homeomorphic pair :math:`(N, A \cup B)`. Now given a map 
    :math:`X \rightarrow Y` and a homotopy of its restriction to :math:`A`, we can take the constant homotopy on 
    :math:`X - (N-B)` and then extend over :math:`N` by applying the homotopy extension property 
    for :math:`(N, A\cup B)` to the given homotopy on :math:`A` and the constant homotopy on :math:`B`.

.. _Proposition 0.16:

.. container:: no-indent

        **Proposition 0.16.** *If* :math:`(X,A)` *is a CW pair, then* :math:`X \times \{0\}\cup A \times I` *is a deformation retract 
        of* :math:`X \times I`, *hence* :math:`(X,A)` *has the homotopy extension property.*
        
    .. image:: fig/proposition-0-16.png
        :align: right
        :width: 20%
    
    **Proof:** There is a retraction :math:`r:D^n \times I \rightarrow D^n \times \{0\} \cup \partial D^n \times I`, for example
    the radial projection from the point point :math:`(0,2) \in D^n \times \mathbb{R}`. Then setting 
    setting :math:`r_t = tr + (1-t)\mathbb{1}` gives a deformation retraction of :math:`D^n \times I` 
    onto :math:`D^n \times \{0\} \cup \partial D^n \times I`. This deformation retraction gives rise to 
    a deformation retraction of :math:`X^n \times I` onto :math:`X^n \times \{0\} \cup (X^{n-1} \cup A^n) \times I` 
    since :math:`X^n \times I` is obtained from :math:`X^n \times \{0\} \cup (X^{n-1} \cup A^n) \times I` during the :math:`t`-interval :math:`[1/2^{n+1},1/2^n]`,
    this infinite concatenation of homotopies is a deformation retraction of :math:`X \times I` onto 
    :math:`X \times \{0\} \cup A \times I`. There is no problem with continuity of this deformation retraction 
    at :math:`t=0` since it is  continuous on :math:`X^n \times I`, being stationary there during the :math:`t`-interval
    :math:`[0,1/2^{n+1}]`, and CW complexes have the weak topology with respect to their skeleta
    so a map is continuous iff its restriction to each skeleton is continuous. |qed|

Now we can prove a generalizatoin of the earlier assertion that collapsing a 
contractible subcomplex is a homotopy equivalence.


.. _Proposition 0.17:

.. container:: no-indent

        **Proposition 0.17.** *If the pair* :math:`(X,A)` *satisfies the homotopy extension property and* 
        :math:`A` *is contractible, then the quotient map* :math:`q:X \rightarrow X/A` *is a homotopy equivalence.*
    
    .. image:: fig/proposition-0-17.png
        :align: right
        :width: 40%

    **Proof:** Let :math:`f_t:X \rightarrow X` be a homotopy extending a contraction of :math:`A`, with :math:`f_0 = \mathbb{1}`. Since 
    :math:`f_t(A) \subset A` for all :math:`t` , the composition :math:`qf_t:X \rightarrow X/A` sends :math:`A` to a point and hence factors 
    as a composition :math:`X \overset{q}{\rightarrow} X/A \rightarrow X/A`. Denoting the latter map by :math:`\bar{f}_t:X/A \rightarrow X/A`, 
    we have :math:`qf_t = \bar{f}_tq` in the first of the two 
    diagrams at the right. When :math:`t=1` we have 
    :math:`f_1(A)` equal to a point, the point to which :math:`A` 
    contracts, so :math:`f_1` induces a map :math:`g:X/A \rightarrow X`
    with :math:`gq=f_1`, as in the second diagram. It 
    follows that :math:`qg = \bar{f}_1` since :math:`qg(\bar{x}) = qgq(x) = qf_1(x) = \bar{f}_1q(x) = \bar{f}_1(\bar{x})`. The 
    maps :math:`g` and :math:`q` are inverse homotopy equivalences since :math:`gq = f_1 \simeq f_0 = \mathbb{1}` via :math:`f_t` and 
    :math:`qg = \bar{f}_1 \simeq \bar{f}_0 = \mathbb{1}` via :math:`\bar{f}_t`.

Another application of the homotopy extension property, giving a slightly more 
refined version of one of our earlier criteria for homotopy equivalence, is the following:

.. _Proposition 0.18:

.. container:: no-indent

        **Proposition 0.18.** *If* :math:`(X_1, A)` *is a CW pair and we have attaching maps* :math:`f,g:A \rightarrow X_0`
        *that are homotopic, then* :math:`X_0 \sqcup_f X_1 \simeq X_0 \sqcup_g X_1` rel :math:`X_0`.
    
    .. container:: indent

        Here the definition of :math:`W \simeq Z \text{ rel } Y` for pairs :math:`(W,Y)` and :math:`(Z,Y)` is that there are 
        maps :math:`\varphi : W \rightarrow Z` and :math:`\psi : Z \rightarrow W` restricting to the identity on :math:`Y`, such that :math:`\psi \varphi \simeq \mathbb{1}`
        and :math:`\varphi \psi \simeq \mathbb{1}` via homotopies that restrict to the identity on :math:`Y` at all times.

    **Proof:** If :math:`F:A\times I \rightarrow X_0` is a homotopy from :math:`f` to :math:`g`, consider the space :math:`X_0 \sqcup_F (X_1 \times I)`.
    This contains both :math:`X_0 \sqcup_f X_1` and :math:`X_0 \sqcup_g X_1` as subspaces. A deformation retraction 
    of :math:`X_1 \times I` onto :math:`X_1 \times \{0\} \cup A \times I` as in :ref:`Proposition 0.16 <Proposition 0.16>` induces a deformation retraction 
    of :math:`X_0 \sqcup_F (X_1 \times I)` onto :math:`X_0 \sqcup_f X_1`. Similarly :math:`X_0 \sqcup_F (X_1 \times I)` deformation retracts onto 
    :math:`X_0 \sqcup_g X_1`. Both these deformation retractions restrict to the identity on :math:`X_0`, so together 
    they give a homotopy equivalence :math:`X_0 \sqcup_f X_1 \simeq X_0 \sqcup_g X_1` rel :math:`X_0`. |qed|

We finish this chapter with a technical result whose proof will involve several 
applications of the homotopy extension property:

.. _Proposition 0.19:

.. container:: no-indent

    ..

        **Proposition 0.19.** *Suppose* :math:`(X,A)` *and* :math:`(Y,A)` *satisfy the homotopy extension property,* 
        *and* :math:`f:X \rightarrow Y` *is a homotopy equivalence with* :math:`f|A=\mathbb{1}`. *Then* :math:`f` *is a homotopy*
        *equivalence* rel :math:`A`.
    
    ..

.. _Corollary 0.20:

.. container:: no-indent

        **Corollary 0.20.** *If* :math:`(X,A)` *satisfies the homotopy extension property and the inclusion*
        :math:`A \hookrightarrow X` *is a homotopy equivalence, then* :math:`A` *is a deformation retract of* :math:`X`.
    
    **Proof:** Apply the :ref:`proposition <Proposition 0.19>` to the inclusion :math:`A \hookrightarrow X`.

.. _Corollary 0.21:

.. container:: no-indent

        **Corollary 0.21.** *A map* :math:`f:X \rightarrow Y` *is a homotopy equivalence iff* :math:`X` *is a deformation
        retract of the mapping cylinder* :math:`M_f`. *Hence, two spaces* :math:`X` *and* :math:`Y` *are homotopy
        equivalent iff there is a third space containing both* :math:`X` and :math:`Y` *as deformation retracts.*

    .. image:: fig/corollary-0-21.png
        :width: 25%
        :align: right

    **Proof:** In the diagram at the right the maps :math:`i` and :math:`j` are the inclusions 
    and :math:`r` is the canonical retraction, so :math:`f=ri` and :math:`i \simeq jf`. Since 
    :math:`j` and :math:`r` are homotopy equivalences, it follows that :math:`f` is a homotopy 
    equivalence iff :math:`i` is a homotopy equivalence, since the composition 
    of two homotopy equivalences is a homotopy equivalence and a map homotopic to a 
    homotopy equivalence is a homotopy equivalence. Now apply the preceding corollary 
    to the pair :math:`(M_f, X)`, which satisfies the homotopy extension property by :ref:`Example 0.15 <Example 0.15>`
    using the neighborhood :math:`X \times [0, \frac{1}{2}]` of :math:`X` in :math:`M_f`. |qed|

.. _Proof of 0.19:

.. container:: no-indent-no-margin

    **Proof of** :ref:`0.19 <Proposition 0.19>` **:** Let :math:`g:\rightarrow X` be a homotopy inverse for :math:`f`. There will be three steps
    to the proof:

    .. container:: indent-no-margin

        \(1\) Construct a homotopy from :math:`g` to a map :math:`g_1` with :math:`g_1 \mid A = \mathcal{1}`.

        \(2\) Show :math:`g_1f \simeq \mathbb{1} \text{ rel } A`.

        \(3\) show :math:`fg_1 \simeq \mathbb{1} \text{ rel } A`.

    .. container:: no-indent-no-margin
    
        \(1\) Let :math:`h_t: X \rightarrow X` be a homotopy from :math:`gf=h_0` to :math:`\mathbb{1}=h_1`. Since :math:`f \mid A=\mathbb{1}`, we 
        can view :math:`h_t \mid A` as a homotopy from :math:`g \mid A` to :math:`\mathbb{1}`. Then since we assume :math:`(Y,A)` has the 
        homotopy extension property, we can extend this homotopy to a homotopy :math:`g_t: Y \rightarrow X` 
        from :math:`g=g_0` to a map :math:`g_1` with :math:`g_1 \mid A = \mathbb{1}`.

        \(2\) A hotopy from :math:`g_1 f` to :math:`\mathbb{1}` is given by the formulas

        .. math::

            k_t = \begin{cases}
            g_{1-2t}f  & 0 \leq t \leq \frac{1}{2} \\
            h_{2t-1},  & \frac{1}{2} \leq t \leq 1 
            \end{cases}
        
        Note that the two definitions agree when :math:`t=\frac{1}{2}`. Since :math:`f \mid A=\mathbb{1}` and :math:`g_t =h_t` on :math:`A`, 
        the homotopy :math:`k_t \mid A` starts and ends with the identity, and its second half simply retraces 
        its first half, that is, :math:`k_t = k_{1-t}` on :math:`A`. We will define a 'homotopy of homotopies' 

        .. image:: fig/proposition-0-19.png
            :width: 30%
            :align: right

        :math:`k_{tu}: A \rightarrow X` by means of the figure at the right showing the parameter
        domain :math:`I \times I` for the pairs :math:`(t,u)`, with the :math:`t`-axis horizontal 
        and the :math:`u`-axis vertical. On the bottom edge of the square we define 
        :math:`k_{t0} = k_t \mid A`. Below the 'V' we define :math:`k_{tu}` to be independent of :math:`t`.
        This is unambiguous since :math:`k_t=k_{1-t}` on :math:`A`. Since :math:`k_0=\mathbb{1}` on :math:`A`,
        we have :math:`k_{tu}=\mathbb{1}` for :math:`(t,u)` in the left, right, and top edges of the square. Next we 
        extend :math:`k_{tu}` over :math:`X`, as follows. Since :math:`(X,A)` has the homotopy extension property, 
        so does :math:`(X \times I, A \times I)`, as one can see from the equivalent retraction property. Viewing
        :math:`k_{tu}` as a homotopy of :math:`k_t \mid A`, we can therefore extend :math:`k_{tu} A \rightarrow X` to :math:`k_{tu}: X \rightarrow X` with 
        :math:`k_{t0}=k_t`. If we restrict this :math:`k_{tu}` to the left, top, and right edges of the :math:`(t,u)`-square,
        we get a homotopy :math:`g_1 f \simeq \mathbb{1} \text{ rel } A`.

        \(3\) Since :math:`g_1 \simeq g`, we have :math:`fg_1 \simeq fg \simeq \mathbb{1}`, so :math:`fg_1 \simeq \mathbb{1}` and steps (1) and (2) can be 
        repeated with the pair :math:`f, \, g` replaced by :math:`g_1, \, f`. The result is a map :math:`f_1: X \rightarrow Y` with 
        :math:`f_1 \mid A = \mathbb{1}` and :math:`f_1g_1 \simeq \mathbb{1} \text{ rel } A`. Hence :math:`f_1 \simeq f_1(g_1 f) = (f_1 g_1)f \simeq f \text{ rel } A`. From this
        we deduce that :math:`fg_1 \simeq f_1g_1 \simeq \mathbb{1} \text{ rel } A`.




    
.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>