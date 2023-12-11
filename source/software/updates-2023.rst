 .. _software-updates-2023:

Software Updates 2023
======================================


.. .. contents::
..      :local:
..      :depth: 1

.. highlight:: python

.. _update-2023-12-11:

2023-12-11: Sage 10.2 and Python 3 (Colab)
---------------------------------------------

- (new) `Sagemath 10.2 <https://github.com/sagemath/sage/wiki/Sage-10.2-Release-Tour>`_ is now available as a Jupyter Notebook kernel or the ``sage-10.2`` executable. Note: `3D graphics are broken <https://github.com/sagemathinc/cocalc/issues/7103>`_.
- (new) **Python 3 (Colab)**: this Python environment is very similar to what is offered in `Google Colab`_. This makes moving your worksheets over to CoCalc easy. Note, for GPU support start a :ref:`Compute Server <compute-servers>` and select the "Colab" environment.
- (upd) system-wide/R/Python 3: as usual, many updated packages and libraries

.. _update-2023-10-23:

2023-10-23: Miniforge 2023
---------------------------------------

- (new) Python3 `Miniforge`_ 2023 environment:
    - Based on Python 3.10, various data science related packages with a newer version than in the existing Anaconda 2022 environment

- Python3 (system-wide):
    - (new) `capytaine`_: *Python BEM solver for linear potential flow, based on Nemoh*


- System-wide: update various packages


.. _update-2023-09-11:

2023-09-11: Sage 10.1
--------------------------------------------------

After an intermediate update, this one makes Sage 10.1 available.
More info, see `CoCalc News item #23 <https://cocalc.com/news/sage-10-1-23>`_.

.. _update-2023-07-12:

2023-07-12: Sage 10.0 on Ubuntu 20.04
------------------------------------------------

The deprecated Ubuntu 20.04 recieved an update. Besides many package updates across all areas, the default `SageMath`_ version is now ``10.0``. Run ``sage_select`` in a :ref:`terminal` to learn how to switch back to an earlier version.

This line of software environments only receives occasional updates.


.. _update-2023-06-28:

2023-06-28: Macaulay2, new Python pkgs, etc.
-------------------------------------------------

Updates to the Ubuntu 22.04 image:

- (new) `Macaulay2`_ – Jupyter Kernel: `m2 example notebook <https://cocalc.com/hsy/ubuntu-22.04-testing/macaulay2>`_
- Python3 (system-wide):
    - (new) `GerryChain`_ – *a library for using Markov Chain Monte Carlo methods to study the problem of political redistricting.*
    - (new) `cirq`_ – *creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits*
    - (new) `tequila`_ – *A High-Level Abstraction Framework for Quantum Algorithms*

Besides that, various updates to system packages and Anaconda 2021.

.. _update-2023-06-07:

2023-06-07: Ubuntu 22.04 and Sage 10.0
-------------------------------------------------

The "Ubuntu 22.04" based line of images became `the default for new projects <https://cocalc.com/news/ubuntu-22-04-default-software-environment-9>`_.
We'll continue to update the 20.04 line of images, but long-term it will become stale.


- Sage:
    - (upd) the system-wide `SageMath`_ version to ``10.0``. Run ``sage_select`` in a :ref:`terminal` to learn how to switch back to an earlier version.

- System-wide:
    - cont. update various packages
    - (rem) IJavascript on Ubuntu 20.04: Updating Node.js to 16 (from the deprecated 14) made it impossible to compile ``ijavascript``. Please switch to the Ubuntu 22.04 image!


.. _update-2023-03-30:

2023-03-30: DUNE, OpenAI, etc.
-------------------------------------------------

- Python 3:
    - (new) `DUNE`_ – *the Distributed and Unified Numerics Environment is a modular toolbox for solving partial differential equations (PDEs) with grid-based methods. It supports the easy implementation of methods like Finite Elements (FE), Finite Volumes (FV), and also Finite Differences (FD)*
    - (upd) many packages, among them the `OpenAI`_ python library

- Executables:
    - Various updates to software packages, python libs, R, etc.

.. _update-2023-02-27:

2023-02-27: Sage 9.8
------------------------------------------------

- Sage:
    - (upd) the system-wide `SageMath`_ version to ``9.8``. Run ``sage_select`` in a :ref:`terminal` to learn how to switch back to an earlier version. In the near future, this will become the default version of Sage.


.. _update-2023-01-08:

2023-01-08: First release of Ubuntu 22.04
------------------------------------------------

The main focus of releasing the ``22.04`` variant is to provide as many software applications as for the older ``20.04`` line.
However, it won't be possible to provide 100% and there will also be new software, only available in the newer variant.
Additionally, many newer versions will be available – starting with a more recent version of `Python`_.




.. _GNU C Compiler: https://gcc.gnu.org/
.. _Sage: https://www.sagemath.org/
.. _numpyro: https://num.pyro.ai/
.. _admcycles: https://www.math.uni-bonn.de/people/schmitt/admcycles
.. _pypy: https://www.pypy.org/
.. _valgrind: https://valgrind.org/
.. _bioconductor: https://bioconductor.org/
.. _requests-cache: https://requests-cache.readthedocs.io/en/stable/
.. _xlrd: https://xlrd.readthedocs.io/en/latest/
.. _pandas: https://pandas.pydata.org/
.. _R 4.2: https://www.r-bloggers.com/2022/04/new-features-in-r-4-2-0/
.. _prophet: https://facebook.github.io/prophet/
.. _pyspice: https://pyspice.fabrice-salvaire.fr/pages/documentation.html
.. _timml: https://github.com/mbakker7/timml
.. _octave 7.1.0: https://www.gnu.org/software/octave/NEWS-7.html
.. _SageMath: https://www.sagemath.org/
.. _rust: https://www.rust-lang.org/
.. _node.js: https://nodejs.org/
.. _checkit: https://checkit.clontz.org/
.. _code-server: https://github.com/coder/code-server
.. _black: https://black.readthedocs.io/en/stable/
.. _papermill: https://papermill.readthedocs.io/en/latest/
.. _pyarrow: https://arrow.apache.org/docs/python/index.html
.. _gprofiler2: https://cran.r-project.org/package=gprofiler2
.. _holoviews: https://holoviews.org/
.. _ipywidgets: https://ipywidgets.readthedocs.io/en/stable/
.. _mapclassify: https://pysal.org/mapclassify/
.. _lsqfit: https://lsqfit.readthedocs.io/en/latest/overview.html
.. _gvar: https://gvar.readthedocs.io/en/latest/overview.html
.. _Pluto: https://github.com/fonsp/Pluto.jl
.. _msImpute: https://www.bioconductor.org/packages/release/bioc/html/msImpute.html
.. _ComplexUpset: https://cran.r-project.org/package=ComplexUpset
.. _Python: https://www.python.org
.. _DUNE: https://www.dune-project.org/
.. _OpenAI: https://openai.com/
.. _GerryChain:  https://gerrychain.readthedocs.io
.. _cirq: https://github.com/quantumlib/Cirq
.. _tequila: https://github.com/tequilahub/tequila
.. _Macaulay2: http://www2.macaulay2.com/Macaulay2/
.. _capytaine: https://github.com/capytaine/capytaine
.. _miniforge: https://github.com/conda-forge/miniforge
.. _Google Colab: https://colab.research.google.com/
