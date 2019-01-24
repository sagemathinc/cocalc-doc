.. index:: Software (available)

======================================
Software
======================================

The following software is used by CoCalc under the hood.
It's either installed directly or slightly modified to fit into the infrastructure.
Besides that, there is a `more detailed and fairly up-to-date list <https://cocalc.com/doc/software.html>`_ available.

* `SageMath <https://www.sagemath.org>`_ - Sage is an open-source mathematics software system. It is the patron for CoCalc's former name "SageMathCloud".
   * Inside Sage, there are `a lot of components <http://sagemath.org/links-components.html>`_ bundled. Note, they maybe replace existing system-wide software like Python libraries and R. (i.e. there is a difference between ``sage -R`` vs. ``R``, ``sage -ipython`` vs. ``ipython``/``ipython3`` and of course, ``sage -python`` vs. ``python``/``python3``.)

* `IPython <http://www.ipython.org>`_ - This is a shell, a notebook and a distributed computing environment built on top of Python.

* `R Statistical Software <http://r-project.org/>`_ - the R-project provides a statistical programming language and a vast plethora of packages on top of it to extend its core functionalities.  `Installed R packages <https://cocalc.com/doc/software-julia.html>`_

* `LaTeX <http://www.latex-project.org/>`_ - CoCalc provides the capability to :doc:`author LaTeX documents online <latex>`. This is a typesetting system with a focus for high-quality layout and formulas. Besides ``pdflatex``, also other variants like ``XeTeX`` and `LuaTeX <http://www.luatex.org/>`_ are installed and available.

* `Linux <https://www.linux.org>`_ – The famous open-source operating system, which holds together everything. The used variant is `Ubuntu <https://www.ubuntu.com>`_.

* `Python <https://www.python.org>`_ – Python is a general purpose programming language. `Installed Python packages <https://cocalc.com/doc/software-python.html>`_

* `Julia <https://julialang.org/>`_ – programming language for scientific computing.  `Installed Julia packages <https://cocalc.com/doc/software-julia.html>`_

Updates
======================================

`Recent updates to CoCalc's software stack <https://github.com/sagemathinc/cocalc/wiki/SoftwareUpgrades/>`_.

