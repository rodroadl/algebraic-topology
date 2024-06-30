Cell complexes
==============

.. image:: fig/cell-complexes.png
    :align: right
    :width: 50%

A familiar way of constructing the torus :math:`S^1 \times S^1` is by identifying opposite isdes 
of a square. More generally, an orientable surface :math:`M_g` of  genus :math:`g` can be constructed 
from a polygon with :math:`4g` sides by identifying pairs of edges, as shown in the figure in the first three cases :math:`g=1,2,3`.
The :math:`4g` edges of the polygon become a union of :math:`2g` circles in the surface, all intersecting 
in a single point. The interior of the polygon ccan be thought of as an open disk, or a :math:`\mathbf{2}`-**cell**,
attached to the union of the :math:`2g` circles. One can also regard the union of the circles as being obtained 
from their common point of intersection, by attaching :math:`2g` open arcs, or :math:`\mathbf{1}`-**cells**. Thus 
the surface can be built up in stages: Start with a point, attach :math:`1`-cells to this point, 
then attach a :math:`2`-cell.

A natural generalization of this is to construct a space by the following procedure:

.. container:: no-indent
   
   1. Start with a discrete Set :math:`X^0`, whose points are regarded as :math:`0`-cells.
   2. Inductively, form the :math:`\mathbf{n}`-**skeleton** :math:`X^n` from :math:`X^{n-1}` by attaching :math:`n`-cells :math:`e^n_{\alpha}` via maps 
      :math:`\varphi_\alpha:S^{n-1} \rightarrow X^{n-1}`. This means that :math:`X^n` is the quotient space of the disjoint union 
      :math:`X^{n-1}\bigsqcup_\alpha D^n_\alpha` with a collection of :math:`n`-disks :math:`D^n_\alpha` under the identifications
      :math:`x~\varphi_\alpha(x)` for :math:`x \in \partial D^n_\alpha`. Thus as a set, :math:`X^n=X^{n-1}\bigsqcup_\alpha e^n_\alpha` where each :math:`e^n_\alpha` is an
      open :math:`n`-disk.
   3. One can either stop this inductive process at a finite stage, setting :math:`X=X^n` for 
      some :math:`n < \infty`, or one can continue indefinitely, setting :math:`X=\bigcup_nX^n`. In the latter 
      case :math:`X` is given the weak topology: A set :math:`A \subset X` is open (or closed) iff :math:`A\cap X^n` is 
      open (or closed) in :math:`X^n` for each :math:`n`.

.. container:: no-indent

   A space :math:`X` constructed in this way is called a **cell complex** or **CW complex**. The 
   explanation of the letters 'CW' is given in the Appendix, where a number of basic 
   topological properties of cell complexes are proved. The reader who wonders about 
   various point-set topological questions lurking in the background of the following 
   discussion should consult the Appendix for details.

If :math:`X=X^n` for some :math:`n`, then :math:`X` is said to be finite-dimensional, and the smallest
such :math:`n` is the **dimension** of :math:`X`, the maximum dimension of cells of :math:`X`.

.. container:: no-indent   

   **Example 0.1.** A :math:`1`-dimensional cell complex :math:`X=X^1` is what is called a **graph** in 
   algebraic topology. It consists of vertices (the :math:`0`-cells) to which edges (the :math:`1`-cells) are
   attached. The two ends of an edge can be attached to the same vertex.

.. container:: no-indent   

   **Example 0.2.** The house with two rooms, pictured earlier, has a visually obvious 
   :math:`2`-dimensional cell complex structure. The :math:`0`-cells are the vertices where three or more 
   of the depicted edges meet, and the :math:`1`-cells are the interiors of the edges connecting
   theses vertices. This gives the :math:`1`-skeleton :math:`X^1`, and the :math:`2`-cells are the components of 
   the remainder of the space, :math:`X-X^1`. If one counts up, one finds there are :math:`29` :math:`0`-cells,
   :math:`51` :math:`1`-cells, and :math:`23` :math:`2`-cells, with the alternating sum :math:`29-51+23` equal to :math:`1`. This is 
   the **Euler characteristic**, which for a cell complex with finitely many cells is defined 
   to be the number of even-dimensional cells minus the number of odd-dimensional 
   cells. As we shall show in Theorem 2.44, the Euler characteristic of a cell complex 
   depends only on its homotopy type, so the fact that the house with two rooms has the 
   homotopy type of a point implies that its Euler characteristic must be :math:`1`, no matter 
   how it is represented as a cell complex.

.. container:: no-indent   

   **Example 0.3.** The sphere :math:`S^n` has the structure of a cell complex with just two cells, :math:`e^0` 
   and :math:`e^n`, the :math:`n`-cell being attached by the constant map :math:`S^{n-1}\rightarrow e^0`. This is equivalent 
   to regarding :math:`S^n` as the quotient space :math:`D^n/\partial D^n`.

.. container:: no-indent   

   **Example 0.4. Real projective** :math:`\mathbf{n}`-**space** :math:`\mathbb{R}P^n` is defined to be the space of all lines 
   through the origin in :math:`\mathbb{R}^{n+1}`. Each such line is determined by a nonzero vector in :math:`\mathbb{R}^{n+1}`, 
   unique up to scalar multiplication, and :math:`\mathbb{R}P^n` is topologized as the quotient space of 
   :math:`\mathbb{R}^{n+1}-\{0\}` under the equivalence relation :math:`v\sim \lambda v` for scalars :math:`\lambda \neq 0`. We can restrict 
   to vectors of length :math:`1`, so :math:`\mathbb{R}P^n` is also the quotient space :math:`s^n/(v \sim -v)`, the sphere 
   with antipodal points identified. This is equivalent to saying that :math:`\mathbb{R}P^n` is the quotient 
   space of hemisphere :math:`D^n` with antipodal points of :math:`\partial D^n` identified. Since :math:`\partial D^n` with 
   antipodal points identified is just :math:`\mathbb{R}P^{n-1}`, we see that :math:`\mathbb{R}P^n` is obtained from :math:`\mathbb{R}P^{n-1}` by 
   attaching an :math:`n`-cell, with the quotient projection :math:`s^{n-1} \rightarrow \mathbb{R}P^{n-1}` as the attaching map. 
   It follows by induction on :math:`n`; that :math:`\mathbb{R}P^n` has a cell complex structure :math:`e^0\cup e^1\cup \dots \cup e^n` 
   with one cell :math:`e^i` in each dimension :math:`i \leq n`.

.. container:: no-indent   

   **Example 0.5.** Since :math:`\mathbb{R}P^n` is obtained from :math:`\mathbb{R}P^{n-1}` by attaching an :math:`n`-cell, the infinite 
   union :math:`\mathbb{R}P^\infty=\bigcup_n \mathbb{R}P^n` becomes a cell complex with one cell in each dimension. We 
   can view :math:`\mathbb{R}P^\infty` as the space of lines through the origin in :math:`\mathbb{R}^\infty = \bigcup_n \mathbb{R}^n`.

.. container:: no-indent-no-margin

   **Example 0.6. Complex projective** :math:`n`-**space** :math:`\mathbb{C}P^n` is the space of complex lines through 
   the origin in :math:`\mathbb{C}^{n+1}`, that is :math:`1`-dimensional vector subspaces of :math:`\mathbb{C}^{n+1}`. As in the case 
   of :math:`\mathbb{R}P^n`, each line is determined by a nonzero vector in :math:`\mathbb{C}^{n+1}`, unique up to scalar 
   multiplication, and :math:`\mathbb{C}P^n` is topologized as the quotient space of :math:`\mathbb{C}^{n+1}-\{0\}` under the 
   equivalence relation :math:`v \sim \lambda v` for :math:`\lambda \neq 0`. Equivalently, this is the quotient of the unit 
   sphere :math:`S^{2n_1}\subset \mathbb{C}^{n+1}` with :math:`v \sim \;lambda v` for :math:`\mid \lambda \mid = 1`. It is also possible to obtain :math:`\mathbb{C}P^n` as a 
   quotient space of the disk :math:`D^{2n}` under the identifications :math:`v \sim \lambda v` for :math:`v \in \partial D^{2n}`, in the 
   following way. The vectors in :math:`S^{2n+1} \subset \mathbb{C}^{n+1}` with last coordinate real and nonnegative 
   are precisely the vectors of the form :math:`(w, \sqrt{1-|w|^2})\in \mathbb{C}^n \times \mathbb{C}` with :math:`|w| \leq 1`. Such 
   vectors form the graph of the function :math:`w \mapsto \sqrt{1-|w|^2}`. This is a disk :math:`D^{2n}_+` bounded 
   by the sphere :math:`S^{2n-1} \subset S^{2n+1}` consisting of vectors :math:`(w,0) \in \mathbb{C}^n \times \mathbb{C}` with :math:`|w|=1`. Each 
   vector in :math:`S^{2n+1}` is equivalent under the identifications :math:`v \sim \lambda v` to a vector in :math:`D^{2n}_+`, and 
   the latter vector is unique if its last coordinate is nonzero. If the last coordinate is 
   zero, we have just the identifications :math:`v \sim \lambda v` for :math:` v \in S^{2n-1}`.

From this description of :math:`\mathbb{C}^n` as the quotient of :math:`D^{2n}_+` under the identifications 
:math:`v \sim \lambda v` for :math:`v \in S^{2n-1}` it follows that :math:`\mathbb{C}P^n` is obtained from :math:`\mathbb{C}P^{n-1}` by attaching a 
cell :math:`e^{2n}` via the quotient map :math:`S^{2n-1} \rightarrow \mathbb{C}P^{n-1}` . So by induction on :math:`n` we obtain a cell 
structure :math:`\mathbb{C}P^n= e^0 \cup e^2 \cup \cdots e^{2n}` with cells only in even dimensions. Similarly, :math:`\mathbb{C}P^\infty` 
has a cell structure with one cell in each even dimension.

After these examples we return now to general theory. Each cell :math:`e^n_\alpha` in a cell 
complex :math:`X` has a **characteristic map** :math:`\Phi_\alpha : D^n_\alpha \rightarrow X` which extends the attaching map 
:math:`\varphi_\alpha` and is a homeomorphism from the interior of :math:`D^n_\alpha` onto :math:`e^n_\alpha`. Namely, we can take 
:math:`\Phi_\alpha` to be the composition :math:`D^n_\alpha \hookrightarrow X^{n-1} \bigsqcup _\alpha D^n_\alpha \rightarrow X^n \hookrightarrow X` where the middle map is 
the quotient map defining :math:`X^n`. For example, in the canonical cell structure on :math:`S^n` 
described in Example 0.3., a characteristic map for the :math:`n`-cell is the quotient map 
:math:`D^n \rightarrow S^n` collapsing :math:`\partial D^n` to a point. For :math:`\mathbb{R}P^n` a characteristic map for the cell :math:`e^i` is 
the quotient map :math:`D^i \rightarrow \mathbb{R}P^i \subset \mathbb{R}^n` identifying antipodal points of :math:`\partial D^i`, and similarly 
for :math:`\mathbb{C}P^n`.

A **subcomplex** of a cell complex :math:`X` is a closed subspace :math:`A \subset X` that is a union 
of cells of :math:`X`. Since :math:`A` is closed, the characteristic map of each cell in :math:`A` has image 
contained in :math:`A`, and in particular the image of the attaching map of each cell in :math:`A` is 
contained in :math:`A`, so :math:`A` is a cell complex in its own right. A pair :math:`(X,A)` consisting of a 
cell complex :math:`X` and a subcomplex :math:`A` will be called a **CW pair**.

For example, each skeleton :math:`X^n` of a cell complex :math:`X` is a subcomplex. Particular 
cases of this are the subcomplexes :math:`\mathbb{R}P^k \subset \mathbb{R}P^n` and :math:`\mathbb{C}P^k \subset \mathbb{C}P^n` for :math:`k \leq n`. These are 
in fact the only subcomplexes of :math:`\mathbb{R}P^n` and :math:`\mathbb{C}P^n`.

These are natural inclusions :math:`S^0 \subset S^1 \subset \cdots \subset S^n`, but these subspheres are not 
subcomplexes of :math:`s^n` in its usual cell structure with just two cells. However, we can give 
:math:`S^n` a different cell structure in which each of the subspheres :math:`S^k` is a subcomplex, by 
regarding each :math:`S^k` as being obtained inductively from the equatorial :math:`S^{k-1}` by attaching 
two :math:`k`-cells, the components of :math:`S^k-S^{k-1}`. The infinite-dimensional sphere :math:`S^\infty = \bigcup_n S^n` 
then becomes a cell complex as well. Note that the two-to-one quotient map :math:`S^\infty \rightarrow \mathbb{R}P^\infty` 
that identifies antipodal points of :math:`S^\infty` identifies the two :math:`n`-cells of :math:`S^\infty` to the single 
:math:`n`-cell of :math:`\mathbb{R}P^\infty`.

In the examples of cell complexes given so far, the closure of each cell is a subcomplex, 
and more generally the closure of any collection of cells is a subcomeplx. 
Most naturally arising cell structures have this property, but it need not hold in general. 
For example, if we start with :math:`S^1` with its minimal cellstructure nad attach to this 
a :math:`2`-cell by a map :math:`S^1 \rightarrow S^1` whose image is a nontrvial subacr of :math:`S^1`, then the closure 
of the :math:`2`-cell is not a subcomples since its contains only a part of the :math:`1`-cell.
