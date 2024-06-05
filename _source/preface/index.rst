Preface
=======

This book was written to be a readable introduction to algebraic topology with
rather broad coverage of the subject. The viewpoint is quite classical in spirit, and
stays well within the confines of pure algebraic topology. In a sense, the book could
have been written thirty or forty years ago since virtually everything in it is at least
that old. However, the passage of the intervening years has helped clarify what are
the most important results and techniques. For example, CW complexes have proved
over time to be the most natural class of spaces for algebraic topology, so they are
emphasized here much more than in the books of an earlier generation. This emphasis
also illustrates the book's general slant towards geometric, rather than algebraic,
aspects of the subject. The geometry of algebraic topology is so pretty, it would seem
a pity to slight it and to miss all the intuition it provides.

At the elementary level, algebraic topology separates naturally into the two broad
channels of homology and homotopy. This material is here divided into four chapters,
roughly according to increasing sophistication, with homotopy split between
Chapters 1 and 4, and homology and its mirror variant cohomology in Chapters 2
and 3. These four chapters do not have to be read in this order, however. One could
begin with homology and perhaps continue with cohomology before turning to homotopy.
In the other direction, one could postpone homology and cohomology until
after parts of Chapter 4. If this latter strategy is pushed to its natural limit, homology
and cohomology can be developed just as branches of homotopy theory. Appealing
as this approach is from a strictly logical point of view, it places more demands on the
reader, and since readability is one of the first priorities of the book, this homotopic
interpretation of homology and cohomology is described only after the latter theories
have been developed independently of homotopy theory.

Preceding the four main chapters there is a preliminary Chapter 0 introducing
some of the basic geometric concepts and constructions that play a central role in
both the homological and homotopical sides of the subject. This can either be read
before the other chapters or skipped and referred back to later for specific topics as
they become needed in the subsequent chapters.

Each of the fourmain chapters concludes with a selection of additional topics that
the reader can sample at will, independent of the basic core of the book contained in
the earlier parts of the chapters. Many of these extra topics are in fact rather important
in the overall scheme of algebraic topology, though they might not fit into the time
constraints of a first course. Altogether, these additional topics amount to nearly half
the book, and they are included here both to make the book more comprehensive and
to give the reader who takes the time to delve into them a more substantial sample of
the true richness and beauty of the subject.

There is also an Appendix dealing mainly with a number of matters of a pointset
topological nature that arise in algebraic topology. Since this is a textbook on
algebraic topology, details involving point-set topology are often treated lightly or
skipped entirely in the body of the text.

Not included in this book is the important but somewhat more sophisticated
topic of spectral sequences. It was very tempting to include something about this
marvelous tool here, but spectral sequences are such a big topic that it seemed best
to start with themafresh in a new volume. This is tentatively titled 'Spectral Sequences
in Algebraic Topology' and is referred to herein as [SSAT]. There is also a third book in
progress, on vector bundles, characteristic classes, and K-theory, which will be largely
independent of [SSAT] and also of much of the present book. This is referred to as
[VBKT], its provisional title being 'Vector Bundles and K-Theory'.

In terms of prerequisites, the present book assumes the reader has some familiarity
with the content of the standard undergraduate courses in algebra and point-set
topology. In particular, the reader should know about quotient spaces, or identification
spaces as they are sometimes called, which are quite important for algebraic
topology. Good sources for this concept are the textbooks [Armstrong 1983] and
[J¨anich 1984] listed in the Bibliography.

A book such as this one, whose aim is to present classical material from a rather
classical viewpoint, is not the place to indulge in wild innovation. There is, however,
one small novelty in the exposition that may be worth commenting upon, even though
in the book as a whole it plays a relatively minor role. This is the use of what we call
Δ complexes, which are a mild generalization of the classical notion of a simplicial
complex. The idea is to decompose a space into simplices allowing different faces
of a simplex to coincide and dropping the requirement that simplices are uniquely
determined by their vertices. For example, if one takes the standard picture of the
torus as a square with opposite edges identified and divides the square into two triangles
by cutting along a diagonal, then the result is a Δ complex structure on the
torus having 2 triangles, 3 edges, and 1 vertex. By contrast, a simplicial complex
structure on the torus must have at least 14 triangles, 21 edges, and 7 vertices. So
Δ complexes provide a significant improvement in efficiency, which is nice froma pedagogical
viewpoint since it simplifies calculations in examples. A more fundamental
reason for considering Δ complexes is that they seem to be very natural objects from
the viewpoint of algebraic topology. They are the natural domain of definition for
simplicial homology, and a number of standard constructions produce Δ complexes
rather than simplicial complexes. Historically, Δ complexes were first introduced by
Eilenberg and Zilber in 1950 under the name of semisimplicial complexes. Soon after
this, additional structure in the form of certain 'degeneracy maps' was introduced,
leading to a very useful class of objects that came to be called simplicial sets. The
semisimplicial complexes of Eilenberg and Zilber then became 'semisimplicial sets',
but in this book we have chosen to use the shorter term 'Δ complex'.

This book will remain available online in electronic form after it has been printed
in the traditional fashion. The web address is

    http://www.math.cornell.edu/~hatcher

One can also find here the parts of the other two books in the sequence that are
currently available. Although the present book has gone through countless revisions,
including the correction of many small errors both typographical and mathematical
found by careful readers of earlier versions, it is inevitable that some errors remain, so
the web page includes a list of corrections to the printed version. With the electronic
version of the book it will be possible not only to incorporate corrections but also
to make more substantial revisions and additions. Readers are encouraged to send
comments and suggestions as well as corrections to the email address posted on the
web page.

**Note on the 2015 reprinting.** A large number of corrections are included in this
reprinting. In addition there are two places in the book where the material was rearranged
to an extent requiring renumbering of theorems, etc. In §3.2 starting on
page 210 the renumbering is the following:

.. table:: 
    :widths: auto

    === ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====
    old 3.11 3.12 3.13 3.14 3.15 3.16 3.17 3.18 3.19 3.20 3.21
    === ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====
    new 3.16 3.19 3.14 3.11 3.13 3.15 3.20 3.16 3.17 3.21 3.18
    === ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====

And in §4.1 the following renumbering occurs in pages 352-355:

.. table:: 
    :widths: auto

    === ==== ==== ==== ==== ====
    old 4.13 4.14 4.15 4.16 4.17
    === ==== ==== ==== ==== ====
    new 4.17 4.13 4.14 4.15 4.16
    === ==== ==== ==== ==== ====

.. toctree::
    
    standard-notations
