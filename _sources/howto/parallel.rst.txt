.. index:: CPU; Multiple
.. index:: Multiple CPUs

======================
Utilize Multiple CPUs
======================

Making use of more than 1 CPU core requires specialized code. A typical program will not run twice as fast with two CPU cores than with one. You can, of course, run independent programs/notebooks in parallel and benefit automatically from having multiple cores, but if you want to speed up a single task, there are basically 3 approaches:

#. If you're processing data for a range of values, split them up into batches and process them in parallel. E.g. for 3 CPUs, instead of running a cycle from 1 to 100, run 3 cycles in parallel: one from 1 to 30, another one from 31 to 65, and the last one from 66 to 100. This will work, of course, only if later iterations do no depend on the result of prior iterations.

#. Structure your code to run in parallel. Details depend on what you are doing and your programming language, among other factors.

#. Use a library or code generator that supports parallel operations on a lower level.

A good way to start with the theory is this article: `Wikipedia: Parallel computing <https://en.wikipedia.org/wiki/Parallel_computing>`_.
