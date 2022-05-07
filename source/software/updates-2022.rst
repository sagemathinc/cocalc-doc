.. _software-updates-2022:

Software Updates 2022
======================================


.. .. contents::
..      :local:
..      :depth: 1

.. highlight:: python

.. _update-2022-05-07:

2022-05-07: R 4.2
----------------------------------------------

- R (system-wide):
    - (upd) `R 4.2`_ + many packages
    - Not yet ready for 4.2? In Settings → Control → Software Environment, you can select ``Ubuntu 20.04``/``2022-04-19``.

- Python3 (system-wide):
    - (new) `prophet`_ – *a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects*
    - (new) `pyspice`_ – *Simulate Electronic Circuit using Python and the Ngspice / Xyce Simulators*
    - (new) `timml`_ – *an analytic element model for steady multi-layer flow*

- System:
    - as usual, various Linux, R and Python package updates


.. _update-2022-04-19:

2022-04-19: Various updates …
----------------------------------------------

- Python3 (system-wide) & System:
    - as usual, various Linux, R and Python package updates

- Python 3 (system-wide):
    - (fix) resolved an `xlrd`_ <-> `pandas`_ incompatibility for reading older Excel xls files.


.. _update-2022-03-24:

2022-03-24: New Anaconda Environment
----------------------------------------------

- (new) Anaconda 2021:
    - Despite we already have the year 2022, the installer is versioned as ``2021.11``, hence that name.
    - Most of the packages that were installed in Anaconda 2020 are also installed here.
    - The Python version is ``3.9``.
    - Anaconda 2020 will stay around, but updates or additional packages will go into the 2021 edition.

- Python 3 (system-wide):
    - (new) `requests-cache`_ ``0.9.2``

- System:
    - as usual, various Linux, R and Python package updates


.. _update-2022-03-19:

2022-03-19: Bioconductor Maintenance
----------------------------------------------

- R:
    - (upd) entire `Bioconductor`_ stack

- System:
    - various Linux, R and Python package updates


.. _update-2022-03-08:

2022-03-08: Regular update
-----------------------------------------------

- System:
    - various Linux, R and Python package updates

.. _update-2022-02-27:

2022-02-27: Removing PyPy Notebooks
------------------------------------------------

- Jupyter:
    - removing `pypy`_ kernel, since it is broken. ``pypy3`` still available on the command-line.

- Sage:
    - `admcycles`_: updated to be compatible with 9.5

- Executables:
    - (new) `valgrind`_
    - (upd) various Linux package updates, including R packages


.. _update-2022-02-12:

2022-02-12: Sage 9.5
------------------------------------------------

- Sage:
    - (new) `Sage`_ ``9.5`` available now: `Sage 9.5 Release Tour <https://wiki.sagemath.org/ReleaseTours/sage-9.5>`_

- Python:
    - (new) `numpyro`_ ``0.8.0`` – *Probabilistic programming with NumPy powered by JAX for autograd and JIT compilation*
    - (upd) various routine pkg updates

- Julia:
    - (upd) Version ``1.7.2``

- Executables:
    - (upd) various Linux package updates, including R packages


.. _update-2022-01-24:

2021-12-13: Julia 1.7 & various updates
-------------------------------------------------

- Julia:
    - (new) Version ``1.7`` now available

- Python 3:
    - (upd) routine upgrades

- Executables:
    - (new) `GNU C Compiler`_ version 10: ``gcc-10``, ``g++-10``, ...
    - (upd) various Linux package updates, including R packages



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
