Simplicial Homology
===============================================

|indent| Our goal now is to define the simplicial homology groups of a :math:`\Delta`-complex :math:`X`. Let
:math:`\Delta_n(X)` be the free abelian group with basis the open :math:`n`-simplices :math:`e^n_\alpha` of :math:`X`. Elements
of :math:`\Delta_n(X)`, called :math:`\mathbf{n}`-**chains**, can be written as finite formal sums :math:`\sum_\alpha n_\alpha e^n_\alpha` with
coefficients :math:`n_\alpha \in \mathbb{Z}`. Equivalently, we could write :math:`\sum_\alpha n_\alpha \sigma_\alpha` where :math:`\sigma_\alpha: \Delta^n \rightarrow X` is the
characteristic map of :math:`e^n_\alpha`, with image the closure of :math:`e^n_\alpha` as described above. Such a
sum :math:`\sum_\alpha n_\alpha \sigma_\alpha` can be thought of as finite collection, or 'chain', of :math:`n`-simplices in :math:`X`
with integer multiplicities, the coefficients :math:`n_\alpha`.

|indent| As one can see in the next figure, the boundary of the :math:`n`-simplex :math:`[v_0,\cdots ,v_n]` 
consists of the various :math:`(n-1)`-dimensional simplices :math:`[v_0,\cdots,\hat{v}_i,\cdots,v_n]`, where the 'hat'
symbol :math:`\hat` over :math:`v-i` indicates that this vertex is deleted from the sequence :math:`v_0,\cdots,v_n`.
In terms of chains, we might then wish to say that the boundary of :math:`[v_0,\cdots,v_n]` is the
:math:`(n-1)`-chain formed by the sum of the faces :math:`[v_0,\cdots,\hat{v}_i,\cdots,v_n]`. However, it turns
out to be better to insert certain signs and instead let the boundary of :math:`[v_0,\cdots,v_n]` be
:math:`\sum_i (-1)^i[v_0,\cdots,\hat{v}_i,\cdots,v_n]`. Heuristically, the signs are inserted to take orientations
into account, so that all the faces of a simplex are coherently oriented, as indicated in
the following figure:

.. image:: fig/orientation.png
    :align: center
    :width: 100%

In the last case, the orientations of the two hidden faces are also counterclockwise
when viewed from outside the :math:`3`-simplex.

|indent| With this geometry in mind we define for a general :math:`\Delta`-complex :math:`X` a **boundary 
homomorphism** :math:`\partial_n : \Delta_n(X) \rightarrow \Delta_{n-1}(X)` by specifying its values on basis elements:

.. math::

    \partial_n(\sigma_\alpha)=\sum_i(-1)^i\sigma_\alpha\mid[v_0,\cdots,\hat{v}_i,\cdots,v_n]

Note that the right side of this equation does indeed lie in :math:`\Delta_{n-1}(X)` since each restriction
:math:`\sigma_\alpha \mid [v_0,\cdots,\hat{v}_i,\cdots,v_n]` is the characteristic map of an :math:`(n-1)`-simplex of :Math:`X`.

.. _Lemma 2.1:

.. container::

        **Lemma 2.1.** *The composition* :math:`\Delta_n(X) \xrightarrow{\partial_n}\Delta_{n-1}\xrightarrow{\partial_{n-1}}\Delta_{n-2}(X)` *is zero.*
    
    **Proof:** We have :math:`\partial_n(\sigma)=\sum_i(-1)^i\sigma\mid[v_0,\cdots,\hat{v}_i,\cdots,v_n]`, and hence

    .. math::

        \begin{aligned}
        \partial_{n-1}\partial_n(\sigma)&=\sum_{j<i}(-1)^i(-1)^j\sigma\mid[v_0,\cdots,\hat{v}_j,\cdots,\hat{v}_i,\cdots,v_n]\\
        \sum_{j>i}(-1)^i(-1)^{j-1}\sigma\mid[v_0,\cdots,\hat{v}_i,\cdots,\hat{v}_j,\cdots,v_n]\\
    
    The latter two summations cancel since after switching :math:`i` and :math:`j` in the second sum, it
    becomes the negative of the first. |qed|

|indent| The algebraic situation we have now is a sequence of homomorphisms of abelian
groups

.. math::

    \cdots \rightarrow C_{n+1} \xrightarrow{\partial_{n+1}} C_{n} \xrightarrow{\partial_{n+1}} C_{n-1} \rightarrow \cdots \rightarrow C_{1} \xrightarrow{\partial_{1}} C_{0} \xrightarrow{\partial_{0}} 0

with :math:`\partial_n \partial_{n+1}=0` for each :math:`n`. Such a sequelnce is called a **chain complex**. Note that
we have extended the sequence by a :math:`0` at the right end, with :math:`\partial_0=0`. The equation
:math:`\partial_n\partial_{n+1}=0` is equivalent to the inclusion :math:`\text{Im}\partial_{n+1} \subset \text{Ker}\partial_n`, where Im and Ker denote
image and kernel. So we can define the :math:`n^{th}` **homology group** of the chain complex to
be the quotient group :math:`H_n=\text{Ker}\partial_n/\text{Im}\partial_{n+1}`. Elements of :math:`\text{Ker}\partial_n` are called **cycles** and
elements of :Math:`\text{Im}\partial_{n+1}` are called **boundaries**. Elements of :Math:`H_n` are cosets of :math:`\text{Im}\partial_{n+1}`,
called **homology classes**. Two cycles representing the same homology class are said
to be **homologous**. This means their difference is a boundary.

|indent| Returning to the case that :math:`C_n=\Delta_n(X)`, the homology group :math:`\text{Ker}\partial_n /\text{Im}\partial_{n+1}` will
be denoted :math:`H^\Delta_n(X)` and called the :math:`n^{th}` **simplicial homology group** of :math:`X`.

.. _Example 2.2:

.. container::









.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>