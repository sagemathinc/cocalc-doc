.. index:: Software Stack

======================================
Software
======================================

Each :doc:`Project <../project>` on CoCalc runs on top of a software environment.
Such an environment holds all the software and libraries, which are necessary to run
code, notebooks and worksheets in your project. There are two types of environments available:

* The :ref:`default environment <default-software-environment>` is very large,
  well tested, regularly maintained and matured over many years.
  This is what a project runs by default.

* A :ref:`custom environment <custom-software-environment>` is based on an exact definition of
  the underlying software stack,
  to fulfill specific purposes and to also convey accompanying material.


.. index:: Software; Default environment
.. _default-software-environment:

Default environment
=================================

.. note::
    This is a very large collection of libraries, which offers a lot of open-source software
    and receives regular updates.
    There is a  `more detailed and fairly up-to-date list <https://cocalc.com/doc/software.html>`_ available.


Software update summaries
-----------------------------------

.. toctree::
   :maxdepth: 1

   software/updates-2022
   software/updates-2021
   software/updates-2020
   software/updates-2019
   software/updates-2018


Main supported software environments
-----------------------------------------------

* `SageMath`_ – Sage is an open-source mathematics software system. It is the patron for CoCalc's former name "SageMathCloud".
   * Inside Sage, there are `a lot of components <http://sagemath.org/links-components.html>`_ bundled. Note, they maybe replace existing system-wide software like Python libraries and R. (i.e. there is a difference between ``sage -R`` vs. ``R``, ``sage -ipython`` vs. ``ipython``/``ipython3`` and of course, ``sage -python`` vs. ``python``/``python3``.)

* `Python <https://www.python.org>`_ – Python is a general purpose programming language. For a list of Python packages which are already installed in CoCalc, see `Python Environments <https://cocalc.com/doc/software-python.html>`_. For instruction on installing your own Python packages in a CoCalc project, see :doc:`howto/install-python-lib`.

* `R Statistical Software <http://r-project.org/>`_ – the R-project provides a statistical programming language and a vast plethora of packages on top of it to extend its core functionalities.  `For a list of R packages which are already installed in CoCalc, see `R Statistical Software Environments <https://cocalc.com/doc/software-r.html>`_. For instruction on installing your own R packages in a CoCalc project, see :doc:`howto/install-r-package`.

* `Julia <https://julialang.org/>`_ – programming language for scientific computing.  For a list of Julia packages which are already installed in CoCalc, see `Julia Environment <https://cocalc.com/doc/software-julia.html>`_. For instruction on installing your own Julia packages in a CoCalc project, see :doc:`howto/install-julia-package`.

* `LaTeX <http://www.latex-project.org/>`_ – CoCalc provides the capability to :doc:`author LaTeX documents online <latex>`. This is a typesetting system with a focus for high-quality layout and formulas. Besides ``pdflatex``, also other variants like ``XeTeX`` and `LuaTeX <http://www.luatex.org/>`_ are installed and available.

* `Linux <https://www.linux.org>`_ – The famous open-source operating system, which holds together everything. The used variant is `Ubuntu <https://www.ubuntu.com>`_.

.. note::

    Via the :ref:`software-environment` selector,
    you have a little bit control over the software you're running in your project.

.. _SageMath: https://sagemath.org


.. index:: Software; Custom environment
.. _custom-software-environment:

Custom environments
==============================


.. warning::
    This is an experimental new feature!


*Custom software environments* provide a narrow stack of software and libraries for specific purposes.

Motivation
-------------

Not all software/library install requests can be fulfilled.
Especially conflicting requirements, requests for an exact version of a library,
or cutting-edge development versions require a more specific and flexible way.

Besides the software, they also bundle accompanying material like the source code,
Jupyter Notebooks containing examples and tutorials, exercises, etc.
This combination makes sure that the material uses exactly the version of the software it was written for.

Under the hood, they're usually pre-built `Binder`_ repositories,
converted via `repo2docker`_,
and then integrated into CoCalc's backend infrastructure.
Simplified, you can think this as an alternative to `MyBinder`_ with a couple of differences.


.. toctree::
   :maxdepth: 1
   :caption: Available Custom Environments

   software/custom_software

Getting started
----------------------

In order to run such an environment,

* Create a new project,
* Click on "Advanced ...",
* Select "Custom" as the type of software environment, and then
* Select the one you want to have and confirm to create the project.

.. note::

    Please do not hesitate to `contact us`_,
    if you want to have a specific environment for your project on CoCalc available.

The screenshot below show how to instantiate a project
to use the alpha version of `"Tensorflow 2" <https://www.tensorflow.org/alpha>`_ (as of May 2019).

.. figure:: img/cocalc-custom-tensorflow2.png
    :width: 100%
    :align: center

    *Selecting "Tensorflow 2" Custom Software Environment*


Key benefits
------------------------------

* A *custom software environment* **bundles software & libraries** –
  which are defined in a well-specified way (compatible with `Binder`_) –
  **with accompanying content to run** (usually :doc:`../jupyter`).
  This is useful for distributing interactive teaching material (tutorials, courses, ...)
  or publications (reproducible science, ...).
  This mitigates slightly inconsistent versions, etc.

* Compared to the `MyBinder`_ service:
    * Your **files are persistently stored across sessions**!
    * Your project is **completely private**.
      You can explicitly :ref:`share it with collaborators <project-collaborators>` or
      :doc:`make specific files public <./share>`.
    * **Projects always start in about 15s**, because the software image was built ahead of time.
      This means you do not have to wait 5 minutes or more to open it
      and you'll never witness that building the image fails.


Current limitations
-----------------------------

Pre-built environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you start a project with a custom software environment,
there will never be an attempt to build the underlying image.
Instead, *the project will always start without an additional delay*!

This implies that updates are not automatically taken into account.
If one of these environments is outdated, please `contact us`_ and we'll update them.
Once they did build successfully and are distributed in CoCalc's cluster,
your project will receive the update after the next project restart.

You'll keep your files as they are, because only the underlying software stack is updated.
Optionally, you can ask to ``Reset...`` your files (in the "Files" bar).
Read the revealed information text to learn more about that.


Jupyter Classic/Lab vs. CoCalc's Jupyter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

    Do not open the same Jupyter Notebook file in a classical Jupyter server
    and CoCalc's Jupyter editor.

Please read about various pros/cons and warnings regarding :ref:`jupyter-classical-vs-cocalc` notebooks.


Port forwarding
^^^^^^^^^^^^^^^^^^^^^^^^^^

Some services need specific proxy forwarding to make them work on CoCalc.
In particular, that's Shiny, the web-based RStudio client, and Jupyter servers without specific command line parameters.
This also means it is most likely not possible to run certain web-service extensions on top of Jupyter.


Start file
^^^^^^^^^^^^^^^^^^

There is currently no support for so called ``start`` files.
A possible workaround is to execute them in a terminal.

.. _contact us: mailto:help@cocalc.com
.. _Binder: https://mybinder.readthedocs.io/en/latest/
.. _MyBinder: https://mybinder.org/
.. _repo2docker: https://repo2docker.readthedocs.io/

