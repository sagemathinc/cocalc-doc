.. index:: Jupyter Notebooks; R step by step
.. index:: R; jupytext

.. _run-r-step-by-step:


=======================================
R Step-by-Step with Jupyter
=======================================

Suppose you have an R script that you would like to debug, or step through line by line collaboratively with others.

You can do this using a Jupyter notebook and CoCalc's built-in collaboration.
Start by using the `jupytext <https://jupytext.readthedocs.io/en/latest/index.html>`_ command to convert a script to blocks of code in cells in a notebook.

If your R script is ``rscript.R``, then do the following:

#. Upload ``rscript.R`` to a CoCalc project.

#. Open a :doc:`terminal <../terminal>` and run the commands::

    jupytext rscript.r --to ipynb
    open rscript.ipynb

#. In the Jupyter notebook, select the "R (system-wide)" kernel. You will see the script separated into multiple cells in the notebook.

You can then step through the script by running one cell in the notebook at a time.
