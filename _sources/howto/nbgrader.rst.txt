.. index:: nbgrader; R

===============
NBgrader
===============

.. warning::

    There are two "nbgrader" systems:

    - CoCalc's "nbgrader" built-in system, which supports its core functionality and can't be configured via that Python config file. Please check :doc:`../teaching-nbgrader` for more information about it.
    - The "official" NBgrader utility, which is available as well. For the nbgrader official website and documentation, see: `nbgrader <http://nbgrader.readthedocs.io>`_. This page explains roughly how to configure the official NBgrader utility.

How to setup ``nbgrader`` for CoCalc to work with ``R``
===========================================================

There are plenty of examples of creating assignments for ``Python``. For other languages, not so much.
I couldn't find any for ``R``. To get ``R`` to work, you need to add one line to the default ``nbgrader_config.py`` file. Here is my file that I placed in ``/etc/jupyter`` (on my own computer - have not gotten this to work yet on CoCalc)::

    from nbgrader.utils import get_username
    import os

    c = get_config()

    c.NbGrader.course_id = "demo"
    c.NbGrader.db_assignments = [dict(name="ps1")]
    c.NbGrader.db_students = [dict(id=get_username())]

    c = get_config()
    c.ClearSolutions.begin_solution_delimeter = "BEGIN MY SOLUTION"
    c.ClearSolutions.end_solution_delimeter = "END MY SOLUTION"
    c.ClearSolutions.code_stub = {
        "r": "# your code here\nfail() # No Answer - remove if you provide an answer",
        "python": "# your code here\nraise NotImplementedError",
        "javascript": "// your code here\nthrow new Error();"
    }

    # Exchange.root is by default in a global read-only /srv/... directory.
    # This defines it to be in your project's home directory (that's what ``~/`` is)
    c.Exchange.root = os.path.expanduser('~/nbgrader_exchange')

The line that starts with ``"R"`` enables using ``R`` in creating the student release version. ``nfail()`` is an ``R`` function from the ``testthat`` ``R`` package that raises an error if the student does not provide an answer. It's the equivalent to the ``raise NotImplementedError`` call in the line for ``Python``. This config file has to placed somewhere ``Jupyter`` can see it. On my own computer it is in ``/etc/jupyter``. We are still trying to figure out where it should go on CoCalc.

Note that you can see the paths for ``Jupyter`` by typing at the command line::

    jupyter --paths


How to prepare an assignment in CoCalc for ``R``
=====================================================

When you create an assignment for ``nbgrader``, you create the instructor version that includes the solution and a code cell that tests the solution.
When you create this version, you use the ``View/Cell Toolbar/Create Assignment`` pull down menu to add the metadata to the solution code cell and the test code cell.
The Create Assignment view is an extension added by ``nbgrader``.
(If you look at any Python example you will see similar cells.)
The test code cell assigns the number of points for the problem.

*Need to add a link to an example R notebook*

Until the link is added, here is an example of the ``R`` code in a solution code cell::


    cars <- 
    ### BEGIN SOLUTION
    read.table("mtcars.csv",header=TRUE,sep=",")
    ### END SOLUTION

Here is an example of the corresponding ``R`` code for the test code cell::

    # Do not modify this code
    require(testthat)
    cars2 <- data.frame(car=rownames(mtcars),mtcars)
    rownames(cars2) <- NULL
    expect_equal(cars,cars2)
    print("Success!")

When you generate the student release version, the solution cell code between the lines ``### BEGIN SOLUTION`` and ``### END SOLUTION`` will be replaced by the code specified in the ``nbgrader_config.py`` file for ``R``::


    # your code here
    nfail() # No Answer - remove if you provide an answer

(Note also that the comment delimiter is # for both ``R`` and ``Python`` - this simplifies things for ``R``. If we were using a language that uses a different comment delimiter, then we also have to specify that somewhere in the config file.)

Note that in this example I'm using functions from the ``testthat`` ``R`` package. When you go to autograde the student assignments, if the solution is considered incorrect by your test code, an error is raised and this is noted by ``nbgrader`` and handled accordingly. Other similar functions from similar packages of course could be used.

