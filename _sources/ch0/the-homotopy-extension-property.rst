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