.. index:: Software Stack

======================================
Software
======================================

Each :doc:`Project <../project>` on CoCalc runs on top of a software environment.
Such an environment holds all the software and libraries, which are necessary to run
code, notebooks and worksheets in your project. There are two types of environments available:

The :ref:`legacy environment <legacy-software-environment>` is very large,
well tested, regularly maintained and matured over many years.
This is what a project runs by default.

A :ref:`custom environment <custom-software-environment>` is based on an exact definition of
the underlying software stack,
to fulfill specific purposes and to also convey accompanying material.



.. _legacy-software-environment:

Legacy environment
=================================

.. note::
    This is a very large collection of libraries, which offers a lot of open-source software
    and receives regular updates.
    There is a  `more detailed and fairly up-to-date list <https://cocalc.com/doc/software.html>`_ available.

Software update summaries
-----------------------------------

.. toctree::
   :maxdepth: 1

   software/updates-2019
   software/updates-2018


Main supported software environments
-----------------------------------------------

* `SageMath`_ – Sage is an open-source mathematics software system. It is the patron for CoCalc's former name "SageMathCloud".
   * Inside Sage, there are `a lot of components <http://sagemath.org/links-components.html>`_ bundled. Note, they maybe replace existing system-wide software like Python libraries and R. (i.e. there is a difference between ``sage -R`` vs. ``R``, ``sage -ipython`` vs. ``ipython``/``ipython3`` and of course, ``sage -python`` vs. ``python``/``python3``.)

* `Python <https://www.python.org>`_ – Python is a general purpose programming language. `Installed Python packages <https://cocalc.com/doc/software-python.html>`_

* `R Statistical Software <http://r-project.org/>`_ – the R-project provides a statistical programming language and a vast plethora of packages on top of it to extend its core functionalities.  `Installed R packages <https://cocalc.com/doc/software-julia.html>`_

* `LaTeX <http://www.latex-project.org/>`_ – CoCalc provides the capability to :doc:`author LaTeX documents online <latex>`. This is a typesetting system with a focus for high-quality layout and formulas. Besides ``pdflatex``, also other variants like ``XeTeX`` and `LuaTeX <http://www.luatex.org/>`_ are installed and available.

* `Linux <https://www.linux.org>`_ – The famous open-source operating system, which holds together everything. The used variant is `Ubuntu <https://www.ubuntu.com>`_.

* `Julia <https://julialang.org/>`_ – programming language for scientific computing.  `Installed Julia packages <https://cocalc.com/doc/software-julia.html>`_

.. note::

    Via the :ref:`software-environment` selector,
    you have a little bit control over the software you're running in your project.

.. _SageMath: https://sagemath.org



.. _custom-software-environment:

Custom environments
==============================


.. warning::
    This is an experimental new feature!


*Custom software environments* provide a narrow stack of software and libraries for specific purposes.

Not all software/library install requests can be fulfilled.
Especially conflicting requirements, requests for an exact version of a library,
or cutting-edge development versions require a more specific and flexible way.

Besides the software, they also bundle accompanying material like the source code,
Jupyter Notebooks containing examples and tutorials, exercises, etc.
This combination makes sure that the material uses exactly the version of the software it was written for.

Under the hood, they're usually pre-built `Binder <https://mybinder.readthedocs.io/en/latest/>`_ repositories,
converted via `repo2docker <https://repo2docker.readthedocs.io/>`_,
and then integrated into CoCalc's backend infrastructure.

Getting Started
----------------------

In order to run such an environment,

* Create a new project,
* Click on "Advanced ...",
* Select "Custom" as the type of software environment, and then
* Select the one you want to have and confirm to create the project.



.. note::

    Please do not hesitate to `contact us <mailto:help@cocalc.com>`_,
    if you want to have a specific  environment for your project on CoCalc available.


