.. _Chatper 2:

Chapter 2. Homology
===================

Homology

|indent| The fundamental group :math:`\pi_1(X)` is especially useful when studying spaces of low
dimension, as one would expect from its definition which involves only maps from
low-dimensional spaces into :math:`X`, namely loops :math:`I \rightarrow X` and homotopies of loops, maps
:math:`I\times I \rightarrow X`. The definition in terms of objects that are most :math:`2`-dimensional manifests
itself for example in the fact that when :math:`X` is a CW complex, :math:`\pi_1(X)` depends only on
the :math:`2`-skeleton of :math:`X`. In view of the low-dimensional nature of the fundamental group,
we should not expect it to be a very refined toll for dealing with high-dimensional
spaces. Thus it cannt distinguish between sphere :math:`S^n` with :math:`n \geq 2`. This limitation
to low dimensions can be removed by considering the natural higher-dimensional
analogs of :math:`\pi_1(X)`, the homotopy groups :math:`\pi_n(X)`, which are defined in terms of maps
of the :math:`n`-dimensional cube :math:`I^n` into :math:`X` and homotopies :math:`I^n\times I \rightarrow X` of such maps. Not
surprisingly, when :math:`X` is a CW complex, :math:`\pi_n(X)` depends only on the :math:`(n+1)-skeleton` 
of :math:`X`. And as one might hope, homotopy groups do indeed distinguish spheres of all
dimensions since :math:`\pi_i(S^n)` is :math:`0` for :math:`i<n` and :math:`\mathbb{Z}` for :math:`i=n`.

|indent| However, the higher-dimensional homotopy groups have the serious drawback
that they are extremely difficult to compute in general. Even for simple spaces like
spheres, the calculation of :Math:`\pi_i(S^n)` for :math:`i>n` turns out to be a huge problem. Fortunately
there is a more computable alternative to homotopy groups: the homology
groups :math:`H_n(X)`. Like :math:`\pi_n(X)`, the homology group :math:`H_n(X)` for a CW complex :math:`X`
depends only on the :math:`(n+1)`-skeleton. For spheres, the homology groups :math:`H_i(S^n)` are
isomorphic to the homotopy groups :math:`\pi_i(S^n)` in the range :math:`1\leq i \leq n`, but homology
groups have the advantage that :math:`H_i(S^n)=0` for :math:`i \geq n`.

|indent| The computability of homology groups does not come for free, unfortunately.
The definition of homology groups is decidedly less transparent than the definition
of homotopy groups, and once on gets beyond the definition there is a certain amount
of technical machinery to be set up before any real calculations and applications can
be given. In the exposition below we approach the definition of :math:`H_n(X)` by two preliminary
stages, first giving a few motivating examples nonrigorously, then constructing
a restricted model of of homology theory called simplicial homology, before plunging
into the general theory, known as singular homology. After the definition of singular
homology has been assimilated, the real work of establishing its basic properties begins.
This take close to 20 pages, and there is no getting around the fact that it is a
substantial effort. This takes up most of the first section of the cahpter, with small
digressions only for two applications to classical theorems of Brouwer: the fixed point
theorem and 'invariance of dimension'.

|indent| The second section of the chapter gives more applications, including the
homology definition of Euler characteristic and Brouwer's notion of degree for maps
:math:`S^n\rightarrow S^n`. However, the main thrust of this section is toward developing techniques
for calculating homology groups efficiently. The maximally efficient method is known
as cellular homology, whose power comes perhaps from the fact that it is 'homology
squared' -- homology defined in terms of homology. Another quite useful tool is
Mayer-Vietoris sequences, the analog for homology of :ref:`van Kampen's theorem <Theorem 1.20>` for the
fundamental group.

|indent| An interesting feature of homology that begins to emerge after one has worked
with it for a while is that it is the basic properties of homology that are used most
often, and not the actual definition itself. This suggests that an axiomatic approach
to homology might be possible. This is indeed the case, and in the third section of
the capter we list axioms which completely characterize homology groups for CW
complexes. One could take the viewpoint that these rather algebraic axiomx are all that
really matters about homology groups, that the geometry involved in the definition of 
homology is secondary, needed only to show that the axiomatic theory is not vacuous.
The extent to which one adopts this viewpoint is a matter of taste, and the route taken
here of postponing the axioms until the theory is well-established is just one of several
possible approaches.

|indent| The chapter then concludes with three optional sections of Additional Topics. The
first is rather brief, relating :math:`H_1(X)` to :math:`\pi_1(X)`, while the other two contain a selection
of classical applications of homology. These include the :math:`n`-dimensional version of the
Jordan curve theorem and the 'invariance of domain' theorem, both due to Brouwer,
along with the Lefxchetz fixed point theorem.

-----------------------
The Idea of Homology
-----------------------

|indent| The difficulty with the higher homotopy groups :math:`\pi_n` is that they are not directly
computable from a cell structure as :math:`\pi_1` is. For example, the :math:`2`-sphere has no cells in
dimensions greater than :math:`2`, yet its :math:`n`-dimensional homotopy group :math:`\pi_n(S^2)` is nonzero
for infinitely many values of :math:`n`. Homology groups, by contrast, are quite directly
related to cell structures, and may indeed be regarded as simply an algebraization of
the first layer of geometry in cell structures: how cells of dimension :math:`n` attach to cells
of dimension :Math:`n-1`.

.. image:: fig/X1.png
    :width: 25%
    :align: right

|indent| Let us look at some examples to see what the idea is. Consider the graph :math:`X_1` shown
in the figure, consisting of two vertices joined by four edges.
When studying the fundamental group of :Math:`X_1` we consider
loops formed by sequences of edges, starting and ending
at a fixed basepoint. For example, at the basepoint :math:`x`, the
loop :math:`ab^{-1}` travels forward along the edge :math:`a`, then backward
along :math:`b`, as indicated by the exponent :math:`-1`. A more complicated
loop would be :math:`ac^{-1}bd^{-1}ca^{-1}`. A salient feature of the
fundamental group is that it is generally nonabelian, which both enriches and complicates
the theory. Suppose we simplify matters by abelianizing. Thus for example the 
two loops :math:`ab^{-1}` and :math:`b^{-1}a` are to be regarded as equal if we make :math:`a` commute with
:math:`b^{-1}`. These two loops :Math:`ab^{-1}` and :math:`b^{-1}a` are really the same circle, jsut with a different
choice of starting and ending point: :math:`x` for :math:`ab^{-1}` and :math:`y` for :math:`b^{-1}a`. The same thing
happens for all loops: Rechoosing the basepoint in a loop just permutes its letters
cyclically, so a byproduct of abelianizing is that we no logner have to pin all our loops
down to a fixed basepoint. Thus loops become *cycles*, without a chosen basepoint.

|indent| Having abelianized, let us switch to additive notation, so cycles become linear
combinations of edges with integer coefficients, such as :math:`a-b+c-d`. Let us call
these linear combinations *chains* of edges. Some chains can be decomposed into
cycles in several different ways, for example :math:`(a-c)+(b-d)=(a-d)+(b-c)`,
and if we adopt an algebraic viewpoint then we do not want to distinguish between
these different decompositions. Thus we broaden the meaning of the term 'cycle' to
be simply any linear combination of edges for which at least one decomposition into 
cycles in the previous more geometric sense exists.

|indent| What is the condition for a chain to be a cycle in this more algebraic sense? A
geometric cycle, thought of as a path traversed in time, is distinguished by the property
that it enters each vertex the same number of times that it leaves the vertex. For
an arbitrary chain :math:`ka+lb_mc_nd`, the net number of times this chain enters :math:`y`
is :math:`k+l+m+n` since each of :Math:`a,b,c`, and :math:`d` enters :math:`y` once. Similarly, each of the
four edges leaves :math:`x` once, so the net number of times the chain :math:`ka+lb+mc+nd` 
enters :math:`x` is :math:`-k-l-m-n`. Thus the condition for :Math:`ka+lb+mc+nd` to be a cycle
is simply :math:`k+l+m+n=0`.

|indent| To describe this result in a way that would generalize to all graphs, let :math:`C_1` be the
free abelian group with basis the edges :math:`a,b,c,d` and let :math:`C_0` be the free abelian group
with basis the vertices :math:`x,y`. Elements of :math:`C_1` are chains of edges, or :Math:`1`-dimensional
chains, and elements of :Math:`C_0` are linear combinations of vertices, or :Math:`0`-dimensional
chains. Define a homomorphism :math:`\partial :C_1 \rightarrow C_0` by sending each basis element :math:`a,b,c,d`
to :math:`y-x`, the vertex at the head of the edge minus the vertex at the tail. Thus we have
:math:`\partila(ka+lb+mc+nd)=(k+l+m+n)y-(k+l+m+n)x`, and the cycles are
precisely the kernel of :math:`\partial`. It is a simple calculation to verify that :Math:`a-b,\, b-c,\,` and :math:`c-d`
form a basis for this kernel. Thus every cycle in :math:`X_1` is a unique linear combination of 
these three most obvious cycles. By means of these basic cycles we convey the
geometric information that the graph :math:`X_1` has three visible 'holes', the empty spaces
between the four edges.

.. image:: fig/X_2.png
    :align: right
    :width: 25%

|indent| Let us now enlarge the preceding graph :math:`X_1` by attaching a :math:`2`-cell :math:`A` along the
cycle :math:`a-b`, producing a :math:`2`-cell :math:`A` as being oriented clockwise, then
we can regard its boundary as the cycle :math:`a-b`. This cycle is
now homotopically trivial since we can contract it to a point
by sliding over :math:`A`. In other words, it no longer encloses a 
hole in :math:`X_2`. This suggests that we form a quotient of the
group of cycles in the preceding example by factoring out
the subgroup generated by :math:`a-b`. In this quotient the cycles :math:`a-c` and :math:`b-c`, for
example, become equivalent, consistent with the fact that tey are homotopic in :math:`X_2`.

|indent| Algebraically, we can define now a pair of homomorphisms :math:`C_2 \xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0`
where :math:`C_2` is the infinite cyclic group generated by :math:`A` and :math:`\partial_2(A)=a-b`. The map
:math:`\partial_1` is the boundary homomorphism in the previous example. The quotient group we
are interested in is :math:`\text{Ker} \partial_1 / \text{Im} \partial_2`, the kernel of :math:`\partial_1` modulo the images of :math:`\partial_2`, or in other
words, the :math:`1`-dimensional cycles modulo those that are boundaries, the multiples of 
:math:`a-b`. This quotient group is the *homology group* :math:`H_1(X_2)`. The previous example can
be fit into this scheme too by taking :math:`C_2` to be zero since ther are no :math:`2`-cells in :math:`X_1`,
so in this case :math:`H_1(X_1)=\text{Ker}\partial_1 / \text{Im}\partial_2 = \text{Ker}\partial_1`, which as we saw was free abelian on
three generators. In the present example, :math:`H_1(X_2)` is free abelian on two generators,
:math:`b-c` and :math:`c-d`, expressing the geometric fact that by filling in the :math:`2`-cell :math:`A` we have
reduced the number of 'holes' in our space from three to two.

.. image:: fig/X_3.png
    :align: right
    :width: 25%

|indent| Suppose we enlarge :math:`X_2` to a space :math:`X_3` by attaching a second :math:`2`-cell :math:`B` along the
same cycle :math:`a-b`. This gives a :math:`2`-dimensional chain group :math:`C_2`
consisting of linear combinations of :math:`A` and :math:`B`, and the boundary
homomorphism :math:`\partial_2:C_2\rightarrow C_1` sends both :math:`A` and :math:`B` to :math:`a-b`.
The homology gorup :math:`H_1(X_3)=\text{Ker}\partial_1/\text{Im}\partial_2` is the same as
for :math:`X_2`, but now :math:`\partial_2` has a nontrivial kernel, the infinite cyclic
group generated by :math:`A-B`. We view :math:`A-B` as a :math:`2`-dimensional
cycle, generating the homology group :math:`H_2(X_3)=\text{Ker}\partial_2\approx\mathbb{Z}`.
Topologically, the cycle :math:`A-B` is the sphere formed by the cells :math:`A` and :math:`B` together
with their common boundary circle. This spherical cycle detects the presence of a 
'hole' in :math:`X_3`, the missing interior of the sphere. However, since this hole is enclosed
by a sphere rather than a circle, it is of a different sort from the holes detected by
:math:`H_1(X_3)\approx \mathbb{Z}\times\mathbb{Z}`, which are detected by the cycles :math:`b-c` and :math:`c-d`.

|indent| Let us continue one more step and construct a complex :math:`X_4` from :math:`X_3` by attaching
a :math:`3`-cell :math:`C` along the :math:`2`-sphere formed by :math:`A` and :math:`B`. This creates a chain group :math:`C_3`
generated by this :math:`3`-cell :math:`C`, and we define a boundary homomorphism :math:`\partial_3:C_3\rightarrow C_2`
sending :math:`C` to :math:`A-B` since the cycle :math:`A-B` should be viewed as the boundary of :math:`C`
in the same way that the :math:`1`-dimensional cycle :math:`a-b` is the boundary of :math:`A`. Now we
have a sequence of three boundary homomorphisms :math:`C_3 \xrightarrow{\partial_3}C_2 \xrightarrow{\partial_2}C_1 \xrightarrow{\partial_1}C_0` and
the quotient :math:`H_2(X_4)=\text{Ker}\partial_2 / \text{Im}\partial_3` has become trivial. Also :math:`H_3(X_4)=\text{Ker}\partial_3=0`.
The group :math:`H_1(X_4)` is the same as :math:`H_1(X_3)`, namely :math:`\mathbb{Z}\times\mathbb{Z}`, so this is the only nontrivial
homology group of :math:`X_4`.

|indent| It is clear what the general pattern of the examples is. For a cell complex :math:`X` one
has chain groups :math:`C_n(X)` which are free abelian groups with basis the :math:`n`-cells of :math:`X`,
and there are boundary homomorphisms :math:`\partial_n:C_n(X) \rightarrow C_{n-1}(X)`, in terms of which
one defines the homology group :math:`H_n(X)=\text{Ker}\partial_n/\text{Im}\partial_{n+1}`. The major difficulty is
how to define :math:`\partial_n` in general. For :math:`n=1` this is easy: The boundary of an oriented
edge is the vertex at its head minus the vertex at its tail. The next case :math:`n=2` is also
not hard, at least for cells attached along cycles that are simply loops of edges, for 
then the boundary of the cell is this cycle of edges, with the appropriate signs taking
orientations into account. But for larget :math:`n`, matters become more complicated. Even
if one restricts attention to cell complexes formed from polyhedral cells with nice
attaching maps, there is still the matter of orientations to sort out.

|indent| The best solution to this problem seems to be to adopt an indirect approach.
Arbitrary polyhedra can always be subdivided into special polyhedra called simplices
(the triangle and the tetrahedron are the :math:`2`-dimensional and :math:`3`-dimensional instances)
so there is no loss of generality, though initially there is some loss of efficiency, in
restricting attention entirely to simplices. For simplices there is no difficulty in defining
boundary maps or in handling orientations. So one obtains a homology theory, called
simplicial homology, for cell complexes built from simplices. Still, this is a rather
restricted class of spaces, and the theory itself has a certain rigidity that makes it
awkward to work with.

|indent| The way around these obstacles is to step back from the geometry of spaces
decomposed into simplices and to consider instead something which at first glance
seems wildly more complicated, the collection of all possible continuous maps of
simplices into a given space :math:`X`. These maps generate tremendously large chain groups
:math:`C_n(X)`, but the quotients :math:`H_n(X)=\text{Ker}\partial_n / \text{Im}\partial_{n+1}`, called singular homology groups,
turn out to be much smaller, at least for reasonably nice spaces :math:`X`. In particular, for 
spaces like those in the four examples above, the singular homology groups coincide
with the homology groups we computed from the cellular chains. And as we shall
see later in this chapter, singular homology allows one to define these nice cellular
homology groups for all cell complexes, and in particular to solve the problem of
defining the boundary maps for cellular chains.



.. toctree::
    sec1/index
    sec2/index
    sec3/index
    additional-topics/index

.. |indent| raw:: html

    <span style="margin-left: 2em">

.. |qed| raw:: html
    
    <span style="float:right">&#9723</span>