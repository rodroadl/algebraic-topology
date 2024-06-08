Homotopy and Homotopy Type
==========================

One of the main ideas of algebraic topology is to consider two spaces to be equivalent 
if they have 'the same shape' in a sense that is much broader than homeomorphism. 
To take an everyday example, the letters of the alphabet can be written either as unions of finitely many straight 
and curved line segments, or in thickened forms that are compact regions in the plane bounded by one or more simple closed curves. 
In each case the thin letter is a subspace of the thick letter, and we can continuously shrink the thick letter to the thin one. 
A nice way to do this is to decompse a thick letter, call it **X**, into line segments connecting each point on the outer boundary of **X** to a unique point of the think subletter X, 
as indicated in the figure. Then we can shrink **X** to X by sliding each point of **X**-X into X along the line segment that contains it. 
Points that are already X do not move.

.. image:: fig/ABC.png
    :width: 400
    :align: center

We can think of this shrinking process as taking place during a time interval :math:`0 \leq t \leq 1`, and then it defines a family of functions 
:math:`f_t`: **X** :math:`\rightarrow` **X** parametrized by :math:`t \in I=[0,1]`, where :math:`f_t(x)` is the point to which a given point 
:math:`x \in \textbf{X}` has moved at time :math:`t`. Naturally we would like :math:`f_t(x)` depend continuously on both :math:`t` and :math:`x`, 
and this will be true if we have each :math:`x \in` **X** - X move along its line segment at constant speed so as to reach its image point in X at time :math:`t=1`, 
while points :math:`x \in` X are stationary, as remarked earlier.

Examples of this sort lead to the following general definition. A **deformation retraction** of a space :math:`X` onto a subspace :math:`a` is a family of maps 
:math:`X\rightarrow X, \,  t \in I`, such that :math:`f_0=\mathbb{1}` (the identity map), :math:`f_1(X)=A`, and :math:`f_t \mid A = \mathbb{1}` for all :math:`t`. 
The family :math:`f_t` should be continuous in the sense that the associated map :math:`X\times I \rightarrow X, \, (x,t) \mapsto f_t(x)`, is continuous.

It is easy to produce many more examples similar to the letter examples, with the deformation retraction :math:`f_t` obtained by sliding along line segments. 
The figure on the left below shows such a deformation retraction of a Möbius band onto its core circle.

.. image:: fig/mobius-band.png

The three figures on the right show deformation retractions in which a disk with 
two smaller open subdisks removed shrinks to three different subspaces.

In all these examples the structure that gives rise to the deformation retraction can 
be described by means of the following definition. For a mp :math:`f:x \rightarrow Y`, the **mapping 
cylinder** :math:`M_f` is the quotient space of the disjoint union :math:`(X \times I) \sqcup Y` obtained by identifying 
each :math:`(x,1) \in X \times I` with :math: `f(x) \in Y`. In the letter examples, 
the space :math:`X` is the outer boundary of the thick letter, :math:`Y` is the thin letter, and :math:`f:X \rightarrow Y` sends 
the outer endpoint of each line segment to its inner endpoint. A similar description 
applies to the other examples. Then it is a general fact that a mapping cylinder :math:`M_f` 
deformation retracts to the subspace :math:`Y` by sliding each point :math:`(x,t)` along the segment 
:math:`\{x\} \times I \subset M_f` to the endpoint :math:`f(x) \in Y`. Continuity of this deformation retraction is 
evident in the specific examples above, and for a general :math:`f:X \rightarrow Y` it can be verified 
using Proposition A.17 in the Appendix concerning the interplay between quotient 
spaces and product spaces.

Not all deformation retractions arise in this simple way from mapping cylinders. 
For example, the thick **X** deformation retracts to the thin X, which in turn deformation 
retracts to the point of intersection of its two crossbars. The net result is a deformatio 
retraction of **X** onto a point, during which certain pairs of points follow paths 
that merge before reaching their final destination. Later in this section we will describe a 
considerably more complicated example. the so-called 'house with two rooms'.

A deformation retraction :math:`F_t:X \rightarrow X` is a special case of the general notion of a 
**homotopy**, which is simply any family of maps :math:`f_t:X \rightarrow Y, \, t \in I`, such that the associated 
map :math:`F:X \times I \rightarrow Y` given by :math:`F(x,t) = f_t(x)` is continuous. One says that two 
maps :math:`f_0 , f_1 : X \rightarrow Y` are **homotopic** if there exists a homotopy :math:`f_t` connecting them, 
and one writes :math:`f_i \simeq f_1`.

In these terms, a deformation retraction of :math:`X` onto a subspace :math:`A` is a homotopy 
from the identity map of :math:`X` to a **retraction** of :math:`X` onto :math:`A`, a map :math:`r:X \rightarrow X` such that 
:math:`r(X) = A` and :math:`r \mid A = \mathbb{1}`. One could equally well regard a retraction as a map :math:`r:X \rightarrow X` 
restricting to the identity on the subspace :math:`A \subset X`. From a more formal viewpoint a 
retraction is a mpa :math:`r:X\rightarrow X` with :math:`r^2=r`, since this equation says exactly that :math:`r` is the 
identity on its image. Retractions are the topological analogs of projection operators in other parts of mathematics.

Not all retractions come from deformation retractions. For example, a space :math:`X` 
always retracts onto any point :math:`x_0 \in X` via the constant map sending all of :math:`X` to :math:`x_0`, 
but a space that deformation retracts onto a point must be path-connected since a 
deformation retraction of :math:`X` to :math:`x_0` gives a path joining each :math:`x \in X` to :math:`x_0`. It is less 
trivial to show that there are path-connected spaces that do not deformation retract 
onto a point. One would expect this to be the case for the letters 'with holes', **A**, **B**, 
**D**, **O**, **P**, **Q**, **R**. In Chapter 1 we will develop techniques to prove this.

A homotopy :math:`f_t : X \rightarrow X` that gives a deformation retraction of :math:`X` onto a subspace 
:math:`A` has the property that :math:`f_t \mid A = \mathbb{1}` for all :math:`t`. In general, a homotopy :math:`f_t : X \rightarrow Y` whose 
restriction to a subspace :math:`A \subset X` is independent of :math:`t` is called a **homotopy relative 
to** :math:`A`, or more concisely, a homotopy rel :math:`A`. Thus, a deformation retraction of :math:`X` onto 
:math:`A` is a homotopy rel :math:`A` from the identity map of :math:`X` to a retraction of :math:`X` onto :math:`A`.

If a space :math:`f_t : X \rightarrow X` that gives a deformation retraction of :math:`X` onto a subspace :math:`A` via :math:`f_t:X\rightarrow X`, then if 
:math:`r:X\rightarrow A` denotes the resulting retraction and :math:`i:A\rightarrow X` the inclusion, we have :math:`ri=\mathbb{1}` 
and :math:`ir \simeq \mathbb{1}`, the latter homotopy being given by :math:`f_t`. Generalizing this situation, a 
map :math:`f:X \rightarrow Y` is called a **homotopy equivalence** if there is a map :math:`g:Y \rightarrow X` such that
:math:`fg \simeq \mathbb{1}`  and :math:`gf \simeq \mathbb{1}`. The spaces :math:`X` and :math:`Y` are said to be **homotopy equivalent** or to 
have the same **homotopy type**. The notation is :math:`X \simeq Y`. It is an easy easy exercise to check 
that this is an equivalence relation, in contrast with the nonsymmetric notion of deformation 
retraction . For example, the three graphs |three-graphs| are all homotopy
equivalent since they are deformation retracts of the same space, as we saw earlier,
but none of the three is a deformation retract of any other.

It is true in general that two spaces :math:`X` and :math:`Y` are homotopy equivalent if and only
if there exists a third space :math:`Z` containing both :math:`X` and :math:`Y` as deformation retracts. For 
the less trivial implication one can in fact take :math:`Z` to be the mapping cylinder :math:`M_f` of
any homotopy equivalence :math:`f:X\rightarrow Y \`. We observed previously that :math:`M_f` deformation 
retracts to :math:`Y`, so what needs to be proved is that:math:`M_f` also deformation retracts to its 
other end :math:`X` if :math:`f` is a homotopy equivalence. This is shown in Corollary 0.21.

A space having the 


.. |three-graphs| image:: fig/three-graphs.png
    :scale: 5%