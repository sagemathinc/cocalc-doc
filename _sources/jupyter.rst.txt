.. index:: Jupyter Notebooks
.. _jupyter-notebook:

=================
Jupyter Notebooks
=================

.. contents::
     :local:
     :depth: 2

What Is It?
-----------

As the `official page of the Jupyter project <https://docs.jupyter.org/en/latest/>`_ states:

    A notebook is a shareable document that combines computer code, plain language descriptions, data, rich visualizations like 3D models, charts, graphs and figures, and interactive controls. A notebook, along with an editor (like JupyterLab), provides a fast interactive environment for prototyping and explaining code, exploring and visualizing data, and sharing ideas with others.

Nowadays a Jupyter Notebook is a de facto standard document format, typically stored in ``.ipynb`` files, which records interactive sessions with a *kernel*.
It is made up of *cells*, which can either store one or more lines of code or formatted text.
When you *run* a code cell, the active kernel session evaluates the piece of code in it and the resulting output is shown below.
The combination of communicating back and forth with a kernel and adding descriptive text makes this form of document very attractive.

CoCalc has its own implementation of the user interface to work with Jupyter Notebooks, which supports our unique features such as real-time collaboration, AI Assistant, and TimeTravel. However, the underlying format of ``.ipynb`` files is exactly the same. You can bring your existing notebooks to CoCalc and resume working, or you can download your work from CoCalc to a local computer or another cloud platform, there is no vendor-lock-in!

.. _jupyter-kernels:

Jupyter Kernels
---------------

Most of the time you don't have to think much about the Jupyter kernel which you are using, because your notebook already has the right kernel selected or your default kernel is picked automatically for new notebooks. But when you want or need to, you can choose the programming language and environment by selecting a kernel explicitly. See :doc:`howto/jupyter-kernel-selection`

.. _cocalc-jupyter-features:

Trusted Notebooks
-----------------

It is important to understand that Jupyter Notebooks are very flexible and can do pretty much anything in your account. Just as you should not click on links in random emails or install arbitrary apps on your phone, you should not open or run Jupyter Notebooks, unless you trust their source. When you do open a freshly uploaded notebook, you will see **Not Trusted** message which goes away if you start executing cells.

.. figure:: img/jn_TOC_and_trust.png
    :width: 100%
    :align: center
    :alt: A Not-Yet-Trusted Notebook
    
    A Not-Yet-Trusted Notebook

Running Code
------------

In order to execute code inside a cell (or multiple cells), you can use various menu items, toolbar buttons, buttons on the top of a cell itself, or press **Shift + Enter**.

Once the cell is executed, it will get a marker like **In [9]** on the left, meaning that it was the 9th execution of a cell during this kernel session. You can execute cells out of order and you can execute the same cell multiple times. Each time this counter increases and allows you to get a sense of the order in which cells were executed. Once again: *this order does not have to match the order in which the cells are written/shown*.

CoCalc does show a more stable cell number in the top right corner as well - it enumerates cells from top to bottom regardless of execution and includes text cells as well.

.. figure:: img/jn_running_code.png
    :width: 100%
    :align: center
    :alt: Running Code in Cells
    
    Running Code in Cells

Jupyter Notebooks can be in two modes: command one for operations on whole cells (and quickly navigating around using arrow keys) or editing mode. In CoCalc the current or selected cell in command mode has a blue border. You may select several cells at once to perform a group operation on them, e.g. delete. To select a range of cells, select the first one, then **Shift - Click** on the last one.

Editing Cells
-------------

To enter editing mode, click on a code cell, double click on a rendered text cell, or press Enter while the desired cell is selected in command mode. Press **Esc** to go back to command mode. To switch the type of a cell from code to text or back you can press **M** and **Y** respectively while in command mode or use **Edit > Cell Type** menu. To render a text cell, "run" it by pressing **Shift + Enter** or using menu.

.. figure:: img/jn_editing_cells.png
    :width: 100%
    :align: center
    :alt: Editing Notebook
    
    Editing Notebook

Help in Notebooks
-----------------

A lot can be done with Jupyter Notebooks and there are a lot of keyboard shortcuts if you like them. (If not, you still have to be careful in command mode, e.g. pressing **D** twice deletes the current cell!) Apart from browsing the menu items, two great sources when you are looking for some action are the search box in the **Help** menu and the list of all commands and their shortcuts accessible from the same menu or by pressing **H** while in command mode.

We also have a growing collection of videos, linked from the **Help** menu as well. For example, you can watch how to `📺 create <https://youtu.be/Fhu-RWYvUh4?feature=shared>`_ a new Jupyter Notebook in CoCalc or `📺 generate <https://youtu.be/2YWhSWGFQM8?feature=shared>`_ one using :doc:`ai`.

.. figure:: img/jn_help.png
    :width: 100%
    :align: center
    :alt: Help in Notebooks
    
    Help in Notebooks

