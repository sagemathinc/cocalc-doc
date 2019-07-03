.. index:: Jupyter Notebooks; kernel selection
.. index:: Kernel (Jupyter)
.. _jupyter-change-kernel:

================================
Jupyter Kernel Selection
================================

The `Jupyter Notebook <https://jupyter.org/>`_ (also in the :doc:`variant of CoCalc <../jupyter>`)
supports more than a single **programming language**.
The element which instantiates a session and runs the code of a cell is called **"Kernel"**.
(Note, CoCalc might some day rename that terminology to "Language", i.e. the "Programming Language")

The **currently active kernel's** "display name" is visible at the top right of the working area listing the cells.
In most cases, it also shows a logo, which helps you identifying it.

When you start a new notebook, the default kernel will generally be whatever kernel you last explicitly selected.
You can override this by creating your own :ref:`default notebook template <default-template>`.

.. note::

    Kernels of *existing* notebooks are only identified by their name.
    The actual meaning of it can change between environments,
    because kernels with the same name could be configured differently.
    There is no common scheme!

    Therefore, after uploading any of your notebooks to CoCalc,
    you have to double-check which kernel it starts to spin up.

CoCalc's Jupyter Notebook
=============================

To select the kernel in a CoCalc Jupyter notebook, click the "Kernel" button (usually in the middle toolbar, depending on your configuration).
In the menu that opens, scroll down past interrupt and restart commands to see the choices for available kernels.

.. figure:: img/jupyter-kernel.png
     :width: 100%
     :align: center

     selecting the kernel in a CoCalc Jupyter notebook


Jupyter Classic
=========================

Here is a sequence of steps depicted about how to change the Kernel in a notebook.
The current selection is "SageMath", and it is about to be change to "Python 3 (Ubuntu Linux)".

.. figure:: img/jupyter-classic-change-kernel.png
    :width: 100%

    selecting the kernel in a Classical Jupyter notebook

Jupyter Lab
======================

It works similar as above, but you have to use the main menu at the top.



