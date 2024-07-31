.. index:: Jupyter Notebooks; getting started

=======================================
Getting Started with Jupyter Notebooks
=======================================

.. contents::
     :local:
     :depth: 2

.. raw:: html

    <center><iframe
        width="640" height="360"
        src="https://www.youtube.com/embed/Fhu-RWYvUh4?si=oKj9sLhGY7cS29wm"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe></center>


##########################
What's a Jupyter Notebook?
##########################

A Jupyter notebook is a specific filetype with the ending ``.ipynb``, which records an interactive session with a **Kernel**.
It is made up of *cells*, which can either store one or more lines of code or formatted text.
When you *run* a cell – which evaluates the piece of code in the cell via the active kernel session – you can see its output after the calculation is done.
This combination of communicating back and forth with a kernel and adding descriptive text makes this form of document very attractive.

.. _jupyter-kernels:

##########################
Jupyter Kernels
##########################

You can choose the programming language and environment by selecting a Jupyter kernel for the notebook.
Popular choices are `Python3`_, `SageMath`_, and `R`_. There many others. Our page on :doc:`howto/jupyter-kernel-selection` shows how to set the kernel.

.. note::

    Make sure and double-check that you're working with :doc:`a suitable kernel <howto/jupyter-kernel-selection>` for your calculations!

.. _cocalc-jupyter-features:

##########################################
Basic Features
##########################################

By default, a Jupyter notebook on CoCalc has all CoCalc's core features, including real-time collaboration, side chat, and TimeTravel.
Read more in our `blogpost <http://blog.sagemath.com/jupyter/2017/05/05/jupyter-rewrite-for-smc.html>`_. The basic user interface looks like the following:

.. image:: img/jupyter/jupyter-notebook-cocalc-1.png
    :width: 100%
    :alt: example of a jupyter notebook with Python kernel selected


*****************************
menu bar
*****************************

.. image:: img/jupyter/jupyter-notebook-cocalc-2.png
    :width: 100%
    :alt: menu bar, button row, and active cell pointed out


Above the scrollable area for the notebook, there is a menu bar beginning with buttons for "File  Edit  View  ...". The menu bar is contains the button for selecting the kernel, which determines the programming language and version for this notebook.

*****************************
button row
*****************************

Under the menu bar is the button row. The button row gives you a one-click access to *Run* the current cell (otherwise press your Shift+Return keys), a way to restart the kernel (which clears the current session) and a Save button to make sure CoCalc has stored the file. The :doc:`time-travel` button allows you to see previous versions of that notebook, such that you can go back in time to recover from a bad change.

*****************************
active cell
*****************************

In the screenshot above, the blue bar on the left and a blue border indicate that this is the currently active cell. Actions like *Run*, *Delete Cell*, etc. operate on the currently selected cell. It is possible to select more than one cell.

*****************************
execution counter
*****************************

On the left of each code cell, there is an execution counter ``In [ x ]``. The number ``x`` increases each time a cell is being run. After the kernel stopped and restarted, that counter starts again at *1*.

*****************************
code cell output
*****************************

The output of code cells is below the code. For example, ``Out [7]:`` is the output of cell ``In [7]:``. In the right hand corner of the input cell is some information about how long it took to calculate the result.

*****************************
select multiple cells
*****************************

Selecting multiple cells in a notebook enables you to copy, move, or delete them in a single operation. It works as you might expect. To select a range of cells, click to select the first, then shift-click to select the last (or vice versa). To select cells that are not in a contiguous range, command- or control-click each one.

Suppose you wanted to delete several cells. To do that, select multiple cells as above, then delete them the same way you would delete a single cell (edit menu or "dd").


*****************************
text cells
*****************************

Text cells are for explanatory text. Select "Text" in the ``[ Code ]`` dropdown menu in the button bar to change a code cell to text. You can use `Markdown`_ to format the text. Similar to code cells, either *Run* these text cells to see the processed Markdown code or press Shift+Return. To edit a text cell, either double click it or press your Return key.

*****************************
saving
*****************************

One advantage of Jupyter Notebooks is that they save all your input and output in a single file. This means you can download or publish the notebook as it is, and everyone else sees it in exactly the same way.

.. _Python3: https://docs.python.org/3/
.. _SageMath: https://www.sagemath.org/
.. _R: https://www.r-project.org/about.html
.. _Markdown: https://www.markdownguide.org/basic-syntax
