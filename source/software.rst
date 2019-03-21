.. index:: Software Stack

======================================
Software
======================================

The following software environments in projects are available on CoCalc:

Legacy software environment
=================================

.. note::
    This is a very large collection of libraries, which offers a lot of open-source software
    and recieves :doc:`regular updates <software/updates>`.
    There is a  `more detailed and fairly up-to-date list <https://cocalc.com/doc/software.html>`_ available.


.. toctree::
   :maxdepth: 1

   software/updates


.. index::
   single: SageMath
   see: Sage; SageMath

* `SageMath`_ – Sage is an open-source mathematics software system. It is the patron for CoCalc's former name "SageMathCloud".
   * Inside Sage, there are `a lot of components <http://sagemath.org/links-components.html>`_ bundled. Note, they maybe replace existing system-wide software like Python libraries and R. (i.e. there is a difference between ``sage -R`` vs. ``R``, ``sage -ipython`` vs. ``ipython``/``ipython3`` and of course, ``sage -python`` vs. ``python``/``python3``.)

* `IPython <http://www.ipython.org>`_ – This is a shell, a notebook and a distributed computing environment built on top of Python.

* `R Statistical Software <http://r-project.org/>`_ – the R-project provides a statistical programming language and a vast plethora of packages on top of it to extend its core functionalities.  `Installed R packages <https://cocalc.com/doc/software-julia.html>`_

* `LaTeX <http://www.latex-project.org/>`_ – CoCalc provides the capability to :doc:`author LaTeX documents online <latex>`. This is a typesetting system with a focus for high-quality layout and formulas. Besides ``pdflatex``, also other variants like ``XeTeX`` and `LuaTeX <http://www.luatex.org/>`_ are installed and available.

* `Linux <https://www.linux.org>`_ – The famous open-source operating system, which holds together everything. The used variant is `Ubuntu <https://www.ubuntu.com>`_.

* `Python <https://www.python.org>`_ – Python is a general purpose programming language. `Installed Python packages <https://cocalc.com/doc/software-python.html>`_

* `Julia <https://julialang.org/>`_ – programming language for scientific computing.  `Installed Julia packages <https://cocalc.com/doc/software-julia.html>`_

.. note::

    Via the :ref:`software-environment` selector,
    you have a little bit control over the software you're running in your project.

.. _SageMath: https://sagemath.org

Custom environments
==============================

These are more specialized and for specific purposes.
They are pre-built based on `Binder <https://mybinder.readthedocs.io/en/latest/>`_ or similar techniques.
They usually come with a set of accompanying documents. :doc:`More information... <software/custom>`.


.. toctree::
   :maxdepth: 1

   software/custom

