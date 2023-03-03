.. index:: CPU; Multiple
.. index:: Multiple CPUs

======================
Multiple CPUs
======================

Making use of more than 1 CPU specialized code. A typical program will not run twice as fast with two CPUs than with one, for example.

There are basically 3 ways to make use of more than 1 CPU in a project:

#. If you're processing data or a range of values, split them up into partitions and process them in parallel. E.g. for 3 CPUs, instead of 1 to 100, do 1 to 30, 31 to 65 and 66 to 100. Those 3 partitions can still only use one core (same code), but in total they can use all 3 when run at the same time.

#. Structure your code to run in parallel. This depends on what you are doing, the programming language, the type of problem, etc.

#. Use a library or code generator that supports parallel operations on a lower level.

A good way to start with the theory is this article: `Wikipedia: Parallel computing <https://en.wikipedia.org/wiki/Parallel_computing>`_.
