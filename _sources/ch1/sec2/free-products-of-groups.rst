Free Products of Groups
================================================

|indent| Suppose one is given a collection of groups :math:`G_\alpha` and one wishes to construct a 
single group containing all these groups as subgroups. One way to do this would be 
to take the product group :math:`\prod_\alpha G_\alpha`, whose elements can be regarded as the functions
:math:`\alpha \mapsto g_\alpha \in G_\alpha`. Or one could restrict to functions taking on nonidentity values at 
most finitely often, forming the direct sum :math:`\bigoplus_\alpha G_\alpha`. Both these constructions produce
groups containing all the :math:`G_\alpha`'s as subgroups, but with the property that elements of 
different subgroups :math:`G_\alpha` commute with each other. In the realm of nonabelian groups
this commutativity is unnatural, and so one would like a 'nonabelian' version of :math:`\prod_\alpha G_\alpha`
or :math:`\bigoplus_\alpha G_\alpha`. Since the sum :math:`\bigoplus_\alpha G_\alpha` is smaller and presumably simpler than :math:`\prod_\alpha G_\alpha`, it 
should be easier to construct a nonabelian version of :math:`\bigoplus_\alpha G_\alpha`, and this is what the free
product :math:`{\Large *}_\alpha G_\alpha` achieves.

|indent| Here is the precise definition. As a set, the free product :math:`{\Large *}_\alpha G_\alpha` consists of all
words :math:`g_1g_2 \cdots g_m` of arbitrary finite length :math:`m \geq 0`, where each letters :math:`g_i` belongs to 
a group :math:`G_{\alpha_i}` and is not the identity element of :math:`G_{\alpha_i}`, and the adjacent letters :math:`g_i` and :math:`g_{i+1}`
belong to different groups :math:`G_\alpha`, that is, :math:`\alpha_i \neq \alpha_{i+1}`. Words satisfying these conditions 
are called *reduced*, the idea being that unreduced words can always be simplified to
reduced words by writing adjacent letters that lie in the same :math:`G_{\alpha_i}` as a single letter and 
by canceling trivial letters. The empty word is allowed, and will be identity element
of :math:`{\Large *}_\alpha G_\alpha`. The group operation in :math:`{\Large *}_\alpha G_\alpha` is juxtaposition, :math:`(g_1 \cdots g_m)(h_1 \cdots h_n) =` 
:math:` g_1 \cdots g_m h_1 \cdots h_n`. This product may not be reduced, however: If :math:`g_m` and :math:`h_1` belong
to the same :math:`G_\alpha`, they should be combined into a single letter :math:`(g_mh_1)` according to the 
multiplication in :math:`G_\alpha`, and if this new letter :math:`g_mh_1` happens to be the identity of :math:`G_\alpha`, it
should be canceled from the product. This may allow :math:`g_{m-1}` and :math:`g_2` to be combined,
and possibly canceled too. Repetition of this process eventually produces a reduced
word. For example, in the product :math:`(g_1 \cdots g_m)(g^{-1}_m \cdots g^{-1}_1)` everything cancels and 
we get the identity element of :math:`{\Large *}_\alpha G_\alpha`, the empty word.

|indent| Verifying directly that this multiplication is associative would be rather tedious,
but there is an indirect approach that avoids most of the word. Let :math:`W` be the set of 
reduced words :math:`g_1 \cdots g_m` as above, including the empty word. To each :math:`g \in G_\alpha` we 
associate the function :math:`L_g : W\rightarrow W` given by multiplication on the left, :math:`L_g(g_1 \cdots g_m)=`
:math:`gg_1 \cdots g_m` where we combine :math:`g` with :math:`g_1` if :math:`g_1 \in G_\alpha` to make :math:`gg_1 \cdots g_m` a reduced
word. A key property of the association :math:`g \mapsto L_g` is the formula :math:`L_{gg'}=L_gL_{g'}` for 
:math:`g,g' \in G_\alpha`, that is, :math:`g(g'(g_1 \cdots g_m)) = (gg')(g_1 \cdots g_m)`. This special case of
associativity follows rather trivially from associativity in :math:`G_\alpha`. The formula :math:`L_{gg'} = L_gL_{g'}`
implies that :math:`L_g` is invertible with inverse :math:`L_{g^{-1}}`. Therefore the association :math:`g \mapsto L_g`
defines a homomorphism from :math:`G_\alpha` to the group :math:`P(W)` of all permutations of :math:`W`. More
generally, we can define :math:`L:W \rightarrowP(W)` by :math:`L(g_1 \cdots g_m) = L_{g_1} \cdots L_{g_m}` for each reduced 
word :math:`g_1 \cdots g_m`. This function :math:`L` is injective since the permutation :math:`L(g_1 \cdots g_m)` sends
the empty word to :math:`g_1 \cdots g_m`. The product operation in :math:`W` corresponds under :math:`L` to 
composition in :math:`P(W)`, because of the relation :math:`L_{gg'}=L_gL_{g'}`. Since composition in
:math:`P(W)` is associative, we conclude that the product in :math:`W` is associative.

|indent| In particular, we have the free product :math:`\mathbb{Z} * \mathbb{Z}` as described earlier. This is an
example of a *free group*, the free product of any numbers of copies of :math:`\mathbb{Z}`, finite or 
infinite. The elements of a free group are uniquely representable as reduced words in
powers of generators for the various copies of :math:`\mathbb{Z}`, with one generator for each :math:`\mathbb{Z}`, just
as in the case of :math:`\mathbb{Z} * \mathbb{Z}`. These generators are called a *basis* for the free group, and the 
number of basis elements is the *rank* of the free group. The abelianization of a free 
group is a free abelian group with basis the same set of generators, so since the rank
of a free abelian group is well-defined, independent of the choice of basis, the same
is true for the rank of a free group.

|indent| An interesting example of a free product that is not a free group is :math:`\mathbb{Z}_2 * \mathbb{Z}_2`. This
is like :math:`\mathbb{Z} * \mathbb{Z}` but simpler since :math:`a^2 = e = b^2`, so powers of :math:`a` and :math:`b` are not needed, and 
:math:`\mathbb{Z}_2 * \mathbb{Z}_2` consists of just the alternating words in :math:`a` and :math:`b`: :math:`a`, :math:`b`, :math:`ab`, :math:`ba`, :math:`aba`, :math:`bab`,
:math:`abab`, :math:`baba`, :math:`ababa`, :math:`\cdots`, together with the empty word. The structure of :math:`\mathbb{Z}_2 * \mathbb{Z}_2`
can be elucidated by looking at the homomorphism :math:`\varphi : \mathbb{Z}_2 * \mathbb{Z}_2 \rightarrow \mathbb{Z}_2` associating to 
each word its length mod :math:`2`. Obviously :math:`\varphi` is surjective, and its kernel consists of the 
words of even length. These form a infinite cyclic subgroup generated by :math:`ab` since
:math:`ba=(ab)^{-1}` in :math:`\mathbb{Z}_2 * \mathbb{Z}_2`. in fact, :math:`\mathbb{Z}_2 * \mathbb{Z}_2` is the semi-direct product of the subgroups
:math:`\mathbb{Z}` and :math:`\mathbb{Z}_2` generated by :math:`ab` and :math:`a`, with the conjugation relation :math:`a(ab)a^{-1}=(ab)^{-1}`.
This group is sometimes called the infinite dihedral group.

|indent| For a general free product :math:`{\Large *}_\alpha G_\alpha`, each group :math:`G_\alpha` is naturally identified with a 
subgroup of :math:`{\Large *}_\alpha G_\alpha`, the subgroup consisting of the empty word and the nonidentity
one-letter words :math:`g \in G_\alpha`. From this viewpoint the empty word is the common identity
element of all the subgroups :math:`G_\alpha`, which are otherwise disjoint. A consequence
of associativity is that anay product :math:`g_1 \codts g_m` of elements :math:`g_i` in the groups :math:`G_\alpha` has a 
unique reduced form, the element of :math:`{\Large *}_\alpha G_\alpha` obtained by performing the multiplications
in any order. Any sequence of reduction operations on an unreduced product
:math:`g_1 \cdots g_m`, ombining adjacent letters :math:`g_i` and :math:`g_{i+1}` that lie in the same :math:`G_\alpha` or canceling
a :math:`g_i` that is the identity, can be viewed as a way of inserting parentheses into :math:`g_1 \cdots g_m`
and performing the resulting sequence of multiplications. Thus associativity implies
that any two sequences of reduction operations performed on the same unreduced
word always yield the same reduced word.

|indent| A basic property of the free product :math:`{\Large *}_\alpha G_\alpha` is that any collection of 
homomorphisms :math:`\varphi_\alpha : G_\alpha \rightarrow H` extends uniquely to a homomorphism :math:`\varphi : {\Large *}_\alpha G_\alpha \rightarrow H`. Namely,
the value of :math:`\varphi` on a word :math:`g_1 \cdots g_n` with :math:`g_i \in G_{\alpha_i}` must be :math:`\varphi_{\alpha_1}(g_1) \cdots \varphi_{\alpha_n}(g_n)`, and
using this formula to define :math:`\varphi` gives a well-defined homomorphism since the process 
of reducing an unreduced product in :math:`{\Large *}_\alpha G_\alpha` does not affect its image under :math:`\varphi`. For
example, for a free product :math:`G {\Large *} H` the inclusions :math:`G \hookrightarrow G \times H` and :math:`H \hookrightarrow G \times H` induce
a surjective homomorphism :math:`G {\Large *} H \rightarrow G \times H`.


.. |indent| raw:: html
    
    <span style="margin-left: 2em">