.. _software-updates-2020:

Software Updates 2020
======================================


.. .. contents::
..      :local:
..      :depth: 1

.. highlight:: python


.. _update-2020-09-28:

2020-09-28: aTSA, BERT and pyGIMLi
-----------------------------------------------

- Node.js:
    - (upd) `typescript`_ ``4.0.2``, ``prettier@2.1.1``, ``webpack@4.44.1``, ``coffeescript@2.5.1``, ``data-cli@0.10.1``, ``ijavascript@5.2.0``, ...

- R (system-wide):
    - (new) `aTSA <https://cran.r-project.org/package=aTSA>`_ – *Contains some tools for testing, analyzing time series data and fitting popular time series models such as ARIMA, Moving Average and Holt Winters, etc.*
    - (upd) various packages

- Python 3 (system-wide):
    - (upd) `nbconvert`_ ``6.0.6``, `matplotlib`_ ``3.3.2`` and various other packages

- Python 3 (Anaconda 2020):
    - (new) `pyGIMLi <https://www.pygimli.org/>`_– *an open-source multi-method library for modelling and inversion in geophysics*
    - (new) `BERT <http://resistivity.net/bert/>`_ – *a software package for modelling and inversion of Electrical Resistivity Tomography data*
    - (upd) various packages

- Utilities:
    - (upd) `heroku`_ ``7.43.0``

.. _update-2020-09-12:

2020-09-12: Regular update
-----------------------------------------------

- Anaconda 2020:
    - `statsmodels`_ ``0.12.0``, `pandas`_ ``1.1.1``, `matplotlib`_ ``3.3.1``, `dask`_/`distributed`_ ``2.25.0``, `biopython`_ ``1.78``,  etc.

- Python 3 (system-wide):
    - `pandas`_ ``1.1.2``, `seaborn`_ ``0.11.0`` (to fix `plotting issue #2194 <https://github.com/mwaskom/seaborn/issues/2194>`_), ...

- Ubuntu 18.04:
    - a couple of small updates, mostly system packages

.. _update-2020-09-01:

2020-09-01: Julia 1.5.1
----------------------------------------------

- Julia:
    - updated to 1.5.1
    - various package updates

- Python (system-wide):
    - various package updates, including `dask`_/`distributed`_ ``2.25.0``, `hypothesis`_ ``5.29.1``

- R (system-wide)
    - various package updates

- Software
    - (new) `Asciidoctor`_ ``2.0.10``
    - `CMake`_ ``3.18.2``
    - `Haskell`_ ``ghc 8.10.2``


.. _update-2020-08-15:

2020-08-18: Ubuntu 20.04
----------------------------------------------

The default environment for new projects changed: :ref:`learn more ... <ubuntu-2004-upgrade>`

.. _update-2020-08-14:

2020-08-14/18.04: Regular update of Ubuntu 18.04
--------------------------------------------------

Cumulative updates to various software package environments.


.. _update-2020-07-31:

2020-07-31: Cumulative Updates
----------------------------------------------

Yet another round of cumulative updates to Linux, Python and R and a
new tool `grepcidr`_.


.. _update-2020-07-16:

2020-07-16: Minor/Bugfixes
----------------------------------------------

This is a cumulative update with several small changes and bugfixes.
For example a dependency problem for `PyTorch`_.
A noteworthy new library is `Epidemics-on-Networks`_ for Python 3 (system-wide), e.g. `EoN example test <https://share.cocalc.com/share/3ae747a3539ade9e76f5de6364d71d7dfb9157b2/TESTS/eon-test.ipynb?viewer=share&session=>`_.

.. _update-2020-06-20:

2020-06-20: Updating `SnapPy`_ in SageMath
----------------------------------------------

- Python 3 (system-wide)
    - (upd) `tensorflow`_ ``2.2.0``, `Cython`_ ``0.29.20``, `dask`_ ``2.18.1``, `dask`_ ``2.19.0``, `distributed`_ ``2.19.0``, `pandas`_ ``1.0.5``
    - (upd) `qiskit`_ related packages and `pyscf`_ ``1.7.3``

- Sage 9.1
    - (upd) `snappy`_ ``2.8``, `spherogram`_ ``1.8.3``, `plink`_ ``2.3.1``

- Sage 8.9
    - (upd) `plink`_ ``2.3.1``, `snappy`_ ``2.8``, `spherogram`_ ``1.8.3``

- Software
    - various system-wide updates, including R packages


.. _update-2020-06-06:

2020-06-06: Prophet and pmdarima
----------------------------------------------

- Python 3 (system-wide)
    - (new) `pmdarima`_ ``1.6.1`` – *ARIMA estimators for Python*
    - (new) `fbprophet`_ – *Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.*
    - (upd) `numba`_ ``0.49.1``, `numpy`_ ``1.18.5``


.. _update-2020-05-27:

2020-05-27: Sage 9.1 and Node.js 12
----------------------------------------------

- `SageMath`_ 9.1 available now
    - `Sage 9.1 example notebook <https://share.cocalc.com/share/5ecad91c75ac8591603714693871c056ad3658ad/sage-9.1.ipynb?viewer=share>`_

- Julia
    - (upd) `Julia`_ ``1.4.2``

- Python 3 (system-wide)
    - (upd) `scikit-learn`_, `sympy`_ ``1.6.0``, `mxnet`_ ``1.6.0``

- Software
    - (upd) `Node.js`_ version 12
    - (upd) `cmake`_ ``3.17.2``


.. _update-2020-05-20:

2020-05-20
----------------------------------------------

- Software
    - (new) `mathlibtools`_ ``0.0.6`` for `LEAN`_

- Python 3 (system-wide)
    - (upd) `scikit-learn`_ ``0.23.0``, `imageio`_ ``2.8.0``, `PyLaTeX`_ ``1.3.2``, `obspy`_ ``1.2.1``

- Julia 1.4
    - (new) `FFTW`_



.. _update-2020-05-12:

2020-05-12: Octave 5.2.0
----------------------------------------------

- Expanded the list of `pre-installed Octave packages <https://cocalc.com/doc/software-octave.html>`_
- Updated the Octave Jupyter kernel
- Made it a `first class citizen <https://cocalc.com/doc/octave>`_


.. _update-2020-05-10:

2020-05-10: QuSpin and RmdFormats
----------------------------------------------

- Python 3 (Anaconda 2019):
    - (new) `QuSpin`_ ``0.3.4`` – *Python package for exact diagonalization and quantum dynamics of arbitrary boson, fermion and spin many-body systems. QuSpin supports the use of various (user-defined) symmetries for one and higher-dimensional lattice systems, (imaginary) time evolution following arbitrary user-specified driving protocols, and constrained Hilbert spaces.*

- Python 3 (system-wide)
    - (fix) the ``/ext/bin/tensorboard`` wrapper script works again
    - (upd) `dask`_/`distributed`_ ``2.16.0``

- R (system-wide)
     - (new) `rmdformats`_ – *provides several HTML output formats of unique and attractive styles for RMarkdown*
     - various package updates …


.. _update-2020-05-08:

2020-05-08: Fixing `Keras`_
----------------------------------------------

- Python 3 (system-wide)
    - (fix) `keras`_ in `tensorflow`_ by downgrading `tensorflow-estimator`_ (`issue tf #37525 <https://github.com/tensorflow/tensorflow/issues/37525>`_)

- Software
    - (upd) `npm`_ ``6.14.5``, `typescript`_ ``3.8.3``


.. _update-2020-05-04:

2020-05-04: Stellargraph
----------------------------------------------

- Python 3 (system-wide)
    - (new) `stellargraph`_ ``0.11.1`` – *software for network graph analytics*
    - (upd) `tensorflow-estimator`_ ``2.2.0``, `tensorflow-probability`_ ``0.9.0``, `dask`_ ``2.15.0``, `distributed`_ ``2.15.1``, `statsmodels`_ ``0.11.1``

- R (system-wide)
    - (new) `genlasso`_ ``1.4`` – *Provides fast algorithms for computing the solution path for generalized lasso problems*
    - (new) `coronavirus` ``0.1`` – *Provides a daily summary of the Coronavirus (COVID-19) cases by state/province*
    - many additional packages and updates

- Jupyter Notebooks:
    - (rem) disabling deprecated and little useful kernels:
        - Julia 1.3: use Julia 1.4
        - Sage's Python 2: use Sage's Python mode. also, starting with 9.0 it's Python 3
        - Sage's R: use R (system-wide), there is no reason left to use this one


.. _update-2020-04-25:

2020-04-25: R ``3.6.3`` and Julia ``1.4.1``
----------------------------------------------

- R (system-wide)
    - (upd) Upgrading R to ``3.6.3 -- "Holding the Windsock"`` and many R packages
    - (rem) Removing ``r-cran-bvs``, ``r-cran-haplo.ccs``, and ``r-cran-haplo.stats``, because they were holding back updating R

- Julia
    - (upd) to 1.4.1
    - (new) adding several packages: see `Julia Packages on CoCalc`_

- Python 3 (system-wide)
    - (new) `ruptures`_ ``1.0.3`` – *a Python library for off-line change point detection*
    - (upd) `pwlf`_ ``2.0.0``, `pyDOE`_ ``0.3.8``, `numba`_ ``0.49.0``, `numpy`_ ``1.18.3``

- Python 3 (Anaconda 2019):
    - (new) `pyDOE`_ ``0.3.8``, `ruptures`_ ``1.0.3``
    - (upd) `tensorflow`_ ``2.1.0``, `sympy`_ ``1.5.1``, `networkx`_ ``2.4.0``, `obspy`_ ``1.2.1``


.. _update-2020-04-16:

2020-04-16 COBOL (GnuCOBOL)
-----------------------------------------------

- Software:
    - (new) `COBOL` via `GnuCOBOL`_ – *an acronym for "common business-oriented language"). Created in the 1960's, it is a compiled English-like computer programming language designed for business use. It is imperative, procedural and, since 2002, object-oriented.* – `cobol example file <https://share.cocalc.com/share/55f06a489bf8944f65f10a8aa8c1a2af30dd3690/cobol/?viewer=share>`_
    - (upd) `Rust`_ 
        - ``rustc +stable: 1.42.0``
        - ``rustc +beta: 1.43.0-beta.5``
        - ``rustc +nightly: 1.44.0-nightly``
    - (new) `Intel MKL`_ ``intel-mkl-64bit-2020.1-102`` – *The Fastest and Most-Used Math Library for Intel®-Based Systems*
        - use via ``export LD_LIBRARY_PATH=/opt/intel/mkl/lib/intel64``

- Python 3 (system-wide):
    - (upd) `numpy`_ ``1.18.2``

- SageMath:
    - (upd) development version ``9.1.rc0``


.. _update-2020-04-08:

2020-04-08: healpy 1.13
-----------------------------------------------

- Python 3 and Anaconda 2019:
    - (new) `healpy`_ 1.13.0`` – *a Python package to handle pixelated data on the sphere*

- System.
    - (upd) `bazel`_ ``3.0.0``
    - (upd) various system package updates, including R packages


.. _update-2020-03-30:

2020-03-30: Julia 1.4
-----------------------------------------------


- Julia:
    - (new) `Julia 1.4 release notes <https://docs.julialang.org/en/v1.4/NEWS/#>`_ – please update from 1.3 to 1.4 soon, since 1.3 is deprecated.

- Python 3 (system-wide)
    - (upd) `geopandas`_ ``0.7.0``, `rasterio`_ ``1.1.3``, `isochrones`_ ``2.1``, `cython`_ ``0.29.16``, `matplotlib`_ ``3.2.1``, `pandas`_ ``1.0.3``, `ipykernel`_ ``5.2.0``, `nipype`_ ``1.4.2``

- Python 3 (Anaconda 2019)
    - (upd) `matplotlib`_ ``3.2.1``, `numba`_ ``0.48.0``, `numpy`_ ``1.18.1``, `statsmodels`_ ``0.11.1``,  `geopandas`_ ``0.7.0``, `pandas`_ ``1.0.3``

- Node.js
    - (upd) `coffeescript`_ ``2.5.1``, `typescript`_ ``3.8.3``, `npm`_ ``6.14.4``, `data-cli`_ ``0.9.6``, `ijavascript`_ ``5.2.0`` (for the JavaScript kernel), `chromedriver`_ ``80.0.1``, `prettier`_ ``2.0.2``, `lerna`_ ``3.20.2``, `webpack`_ ``4.42.1``

- Software
    - (upd) various Linux package updates, including ``qgis`` related ones to ``3.12.1``



.. _update-2020-03-20:

2020-03-20:
-----------------------------------------------

- Python 3 Anaconda 2019
    - (upd) `scikit-learn`_ ``0.22.2.post1``, `matplotlib`_ ``3.2.0``

- Python 3 system-wide
    - (new) `ccdproc`_ ``2.1.0``  – *an Astropy affiliated package for basic data reductions of CCD images*
    - (upd) `matplotlib`_ ``3.2.0``, `dask`_/`distributed`_ ``2.12``, `scikit-learn`_ ``0.22.2.post1``

- Software
    - (new) ``libnetcdff6 (4.4.4+ds-3)`` and ``libnetcdff-dev (4.4.4+ds-3)``

- R (system-wide)
    - (new) ``markovchain 0.8.4``
    - (upd) various packages …


.. _update-2020-02-29:

2020-02-29: Async I/O in Jupyter Notebooks
-----------------------------------------------

- Python 3
    - (upd) various Jupyter libs:  `jupyter-client`_ ``6.0.0``, `jupyter-console`_ ``6.1.0``, `jupyterhub`_ ``1.1.0``, `jupyterlab`_ ``1.2.6``, `ipykernel`_ ``5.1.4``,  `ipython`_ ``7.12.0``, ...

      This means you work seamlessly with Python 3's `async/await coroutines <https://docs.python.org/3.7/library/asyncio-task.html>`_ in the system-wide Python3 kernel::

          import asyncio

          async def main():
              print('hello')
              await asyncio.sleep(1)
              print('world')

          await main()

    - (new) `folium`_ ``0.10.1`` – maps of the world. try ``import folium; folium.Map(location=[45.523, -122.675], width=750, height=500)``
    - (upd) `requests`_ ``2.23.0``, `cython`_ ``0.29.15``,  `numba`_ ``0.48.0``, `numpy`_ ``1.17.5``, `curio`_ ``1.0``, `nest-asyncio`_ ``1.2.3``, `biopython`_ ``1.76``
    - (upd) `PyTest`_ related: ``pytest-5.3.5``, ``pytest-doctestplus-0.5.0``, ``pytest-forked-1.1.3``, ``pytest-html-2.0.1``, ``pytest-mock-2.0.0``, ``pytest-pylint-0.15.0``, ``hypothesis-5.5.4``, ``pytest-astropy-0.8.0``

- Software
    - (upd) `qgis`_ ``3.12``
    - (upd) `typescript`_ ``3.8.2``

- LEAN
    - (upd) `mathlib`_ ``2020-02-27`` nightly build (LEAN 3.6.0 and mathlib aren't compatible yet, hence no update of LEAN itself)

- R
    - (new) `mltools`_ ``0.3.5`` – *A collection of machine learning helper functions, particularly assisting in the Exploratory Data Analysis phase.*


.. _update-2020-02-21:

2020-02-21: LEAN 3.5.1 and JavaScript Kernel
----------------------------------------------

- `LEAN`_, the open source theorem prover:
    - Update to 3.5.1, the most recent `LEAN community edition <https://github.com/leanprover-community>`_
    - Latest `mathlib`_ build
    - Try it:
        - `LEAN maths challenges <https://share.cocalc.com/share/f014cd1885a22e8665a728be825e563fc79b7e1f/Maths_Challenges/?viewer=share>`_ (open this link, click the green button at the top – that copies all files to your project and you can start playing around)
        - `Natural numbers example <https://share.cocalc.com/share/df81e09e5b8f16f28b3a2e818dcdd4560e7818ae/support/2020-02-19-lean-natural-numbers.lean?viewer=share>`_:

      .. figure:: https://share.cocalc.com/share/9ba989d8b4e822cb00df1471b2d46a249c90f364/img/2020-02-20-lean-mathlib-3.5.1-cocalc.png?viewer=raw
          :align: center
          :width: 75%

- Jupyter:
    - (new) You can run **JavaScript** in a Jupyter Notebook, powered by `Node.js`_ – `ijavascript example notebook <https://share.cocalc.com/share/2b6ef7cc0e2d7fe8c126e1901e44ecc57b1b98e2/javascript.ipynb?viewer=share>`_.

- Software:
    - (upd) `pandoc`_ ``2.9.2`` – `pandoc 2.9.2 release notes <https://github.com/jgm/pandoc/releases/tag/2.9.2>`_
    - (new) `fractint`_ – in an :doc:`X11 <../x11>` desktop, run ``xfractint``
    - (new) `surface evolver`_ ``2.70`` – *an interactive program for the modelling of liquid surfaces shaped by various forces and constraints* (run ``evolver`` in an :doc:`X11 <../x11>` desktop)

- Python
    - (upd) `protobuf`_ ``3.11.3``, `dask`_ ``2.11.0`` and `distributed`_ ``2.11.0``, `spacy`_ ``2.2.3``, `nilearn`_ ``0.6.1``


.. _update-2020-02-16:

2020-02-16: Pandas 1.0 and Octave 5.2.0
------------------------------------------

- Python 3:
    - (upd) `pandas`_ ``1.0`` – `Pandas 1.0 release notes <https://pandas.pydata.org/pandas-docs/version/1.0.0/whatsnew/v1.0.0.html>`_. This is a major release which might break some libs. Please `let us know`_ about any issues. You can always switch back to the previous release in ``Settings`` → ``Project Control`` → ``Software Environment`` and select ``Previous``.
    - (upd) updating Pandas reverse dependencies: `Mesa`_ ``0.8.6``, `Orange3`_ ``3.24.1``, `Quandl`_ ``3.5.0``, `TPOT`_ ``0.11.1``, `adtk`_ ``0.5.2``, `altair`_ ``4.0.1``, `arctic`_ ``1.79.3``, `arviz`_ ``0.6.1``, `bqplot`_ ``0.12.3``, `cobra`_ ``0.17.1``, `dask-ml`_ ``1.2.0``, `empyrical`_ ``0.5.3``, `isochrones`_ ``2.0.1``, `linearmodels`_ ``4.17``, `mlxtend`_ ``0.17.1``, `openTSNE`_ ``0.3.12``, `optlang`_ ``1.4.4``, `pandas-bokeh`_ ``0.4.2``, `pandas-profiling`_ ``2.4.0``, `pdpipe`_ ``0.0.41``, `pysal`_ ``2.1.0``, `qgrid`_ ``1.2.0``, `scikit-rf`_ ``0.15.1``, `tabulate`_ ``0.8.6``, `tellurium`_ ``2.1.5``, `teneto`_ ``0.5.0``, `xarray`_ ``0.15.0``

- Software:
    - (upd) `Octave`_ ``5.2.0`` (major upgrade!) with some extension packages
    - (upd) Jupyter related: `jupytext`_ ``1.3.3`` and `nbconvert`_ ``5.6.1``

- Anaconda Python:
    - (new) `ocaml`_ ``4.06.1`` – *an industrial strength programming language supporting functional, imperative and object-oriented styles*
    - (upd) various package updates, including numpy, scipy, scikit learn, statsmodels, etc.

.. _update-2020-02-03:

2020-02-03: AstroPy 4.0
---------------------------------

- Python 3:
    - (upd) `astropy`_ ``4.0``, `astroplan`_ ``0.6`` – `what's new in AstroPY 4.0 <http://docs.astropy.org/en/stable/whatsnew/4.0.html>`_
    - (upd) `mypy`_ ``0.761``, `pygments`_ ``2.5.2``, `yapf`_ ``0.29.0``, `dask`_ ``2.10.0``, `matplotlib`_ ``3.1.2``, `rpy2`_ ``3.2.5``, `statsmodels`_ ``0.11.0``, `pip`_ ``20.0.2``

- SageMath (8.9 and 9.0):
    - (upd) `admcycles`_ ``1.0``, a major release update!

- Software:
    - (new) `openscad`_  (available as ``openscad-nightly``) together with support packages ``meshlab``, ``geomview`` and ``librecad``
    - (upd) various Linux system packags, including R libs



.. _update-2020-01-29:

2020-01-29 Rust ``1.40``
------------------------------------------

- Software:
    - (upd) a round of updating `Rust`_:
        - stable: ``1.40.0``
        - beta:  ``1.41.0-beta.2``
        - nightly: ``1.42.0-nightly``

- Python 3 and Anaconda 2019:
    - (new) `pgmpy`_ ``0.1.9`` – *a python library for working with Probabilistic Graphical Models*

- Python 3:
    - (new) `okpy`_ ``1.14.19`` – *OK autogrades programming assignments, facilitates submission, composition feedback, and analytics for your class*. It's installed for the :doc:`../terminal` and run ``ok --help`` for more info.
    - (new) `pyreadstat`_ ``0.2.9`` – *read and write sas (sas7bdat, sas7bcat, xport), spps (sav, zsav, por) and stata (dta) data files into/from pandas dataframes*
    - (new) `bitarray`_ ``1.2.1`` – *efficient arrays of booleans*
    - (new) `ifsFractals`_ ``1.17.4`` – *fast IFS fractal generation* (`ifs fractals example <https://share.cocalc.com/share/10a1a74ea3be1a433ce127f46f2b5eb53dbd3907/ifs-fractals.ipynb?viewer=share>`_)
    - (upd) `PyTorch`_ ``1.3.1``, `joblib`_ ``0.14.1``, `drive-cli`_ ``2.1.0``, `seaborn`_ ``0.10.0``, `numba`_ ``0.47.0``



.. _update-2020-01-19:

2020-01-19: SentimentAnalysis R package
--------------------------------------------

- R Software:
    - (new) `SentimentAnalysis`_ – *package introduces a powerful toolchain facilitating the sentiment analysis of textual contents in R.*

- Python 3:
    - (upd) `sympy` ``1.5.1``, `tensorflow`_ ``2.1.0``,  `tensorflow-estimator`_ ``2.1.0``, `dask`_/`distributed`_ ``2.9.2/.3``



.. _update-2020-01-05:

2020-01-05: SageMath 9.0 based on Python 3
--------------------------------------------

- SageMath:
    - (new) ``sage-9.0`` and associated Jupyter Kernel available.
      This release marks a significant change, because the era of Python 2 ends and Python 3 starts – finally.

      .. note::

          Please read about the `changes in Sage 9.0 regarding Python 3 <https://wiki.sagemath.org/Python3-user>`_
          or more general, consult the `Python 3 porting guide <https://portingguide.readthedocs.io/en/latest/>`_!

- Julia:
    - new year cleanup: only supporting ``1.0 LTS`` and newer versions – currently ``1.3.1`` – which is the default Julia on CoCalc now.
    - (upd) re-installing all packages will lead to various updates
    - (new) `ApproxFun`_ and `SpecialMatrices`_ in ``1.3.1``

- Software:
    - (upd) `bazel`_ ``2.0.0``,  `pypy`_ ``7.3.0``, `xpra`_ ``3.0.4``
    - and various Linux package updates, including R packages

- Python 3:
    - (new) `kplr`_ ``0.2.2`` – *A Python interface to the Kepler data*
    - (upd) ``six 1.13``, `numpy`_ ``1.17.4``, `scipy`_ ``1.4.1``, ``ansi2html-1.5.2``, ``markdown2-2.3.8``, ``pylint-2.4.4``, `pillow`_ ``6.2.1``, `imageio`_ ``2.6.1``, `pywavelets`_ ``1.1.1``, `scikit-learn`_ ``0.22.1``, `tpot`_ ``0.11.0``

- Python 2:
    - Python 2 is still available, but w/o maintenance.
    - If you require specific setups for old libraries and python 2, we can setup a :ref:`custom software environment <custom-software-environment>`.

- R:
    - (new) `DeclareDesign`_ ``0.20.0`` and `DesignLibrary`_ ``0.1.4``




.. The duplication below with the 2019 file extremely silly, but I don't know how to share references properly

.. _Jupyter Lab: https://jupyterlab.readthedocs.io/en/stable/
.. _Scikit Image: https://scikit-image.org/
.. _scikit-image: https://scikit-image.org/
.. _Astroalign: https://astroalign.readthedocs.io/en/master/
.. _GAP: https://www.gap-system.org/
.. _SageMath: https://sagemath.org
.. _Cadabra2: https://cadabra.science
.. _Qiskit:  https://qiskit.org
.. _qiskit-terra: https://github.com/Qiskit/qiskit-terra
.. _qiskit-aqua: https://qiskit.org/aqua
.. _qiskit-aer: https://qiskit.org/aer
.. _dask: https://dask.org
.. _dask-ml: https://dask-ml.readthedocs.io/
.. _distributed: https://distributed.dask.org/
.. _QGIS: https://www.qgis.org
.. _arctic: https://arctic.readthedocs.io/en/latest/
.. _Gradle: https://gradle.org/
.. _PyGame: https://www.pygame.org/
.. _ipywidgets: https://ipywidgets.readthedocs.io/en/stable/user_guide.html
.. _VQE Playground: https://github.com/JavaFXpert/vqe-playground/
.. _RDKit: http://www.rdkit.org/docs/index.html
.. _BibTeX: http://www.bibtex.org/
.. _gspread: https://github.com/burnash/gspread
.. _pygsheets: https://pygsheets.readthedocs.io/en/stable/
.. _statsmodels: https://www.statsmodels.org/
.. _cvxpy: https://www.cvxpy.org/
.. _OpenCV: https://github.com/skvark/opencv-python
.. _pyppeteer: https://github.com/miyakogi/pyppeteer
.. _scikit-rf: https://scikit-rf.readthedocs.io/
.. _Binder: https://mybinder.readthedocs.io/en/latest/introduction.html
.. _pymc3: https://docs.pymc.io/
.. _theano: http://deeplearning.net/software/theano/
.. _IRkernel: https://irkernel.github.io/
.. _psycopg2: http://initd.org/psycopg/docs/
.. _PyTorch: https://pytorch.org/
.. _pandoc: https://pandoc.org/
.. _xpra: http://xpra.org/
.. _bazel: https://bazel.build/
.. _jieba: https://github.com/fxsjy/jieba
.. _julia_distributions: https://github.com/JuliaStats/Distributions.jl
.. _tensorly: http://tensorly.org/
.. _pip-upgrader: https://github.com/simion/pip-upgrader
.. _jax: https://github.com/google/jax
.. _R Statistical Software: https://www.r-project.org/
.. _NEURON: https://www.neuron.yale.edu/neuron/
.. _yapf: https://github.com/google/yapf
.. _GRASS GIS: https://grass.osgeo.org/
.. _Tensorflow: https://www.tensorflow.org/
.. _RISE: https://github.com/damianavila/RISE
.. _JuMP: http://www.juliaopt.org/JuMP.jl/stable/
.. _linearmodels: https://bashtage.github.io/linearmodels/
.. _typescript: https://www.typescriptlang.org/
.. _prettier: https://prettier.io/
.. _pandas: https://pandas.pydata.org/
.. _pandas-profiling: https://github.com/pandas-profiling/pandas-profiling
.. _pandas-bokeh: https://github.com/PatrikHlobil/Pandas-Bokeh
.. _numpy: https://numpy.org/
.. _matplotlib: https://matplotlib.org/
.. _pytest: https://docs.pytest.org/en/latest/
.. _spyder: https://www.spyder-ide.org/
.. _oligo: https://www.bioconductor.org/packages/release/bioc/html/oligo.html
.. _BioConductor: https://www.bioconductor.org
.. _music: https://github.com/ttm/music
.. _sckit-learn: https://scikit-learn.org/stable/
.. _SOAP: https://en.wikipedia.org/wiki/SOAP
.. _suds-jurko: https://bitbucket.org/jurko/suds/src/default/README.rst
.. _zeep: https://python-zeep.readthedocs.io/
.. _suds-community: https://github.com/suds-community/suds
.. _IPOPT: https://coin-or.github.io/Ipopt/
.. _ipopt examples: https://cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/ipopt.ipynb?viewer=share
.. _PyOMO: http://www.pyomo.org/
.. _cyipopt: https://github.com/matthias-k/cyipopt
.. _bokeh example notebook: https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/bokeh-plots.ipynb?viewer=share
.. _scipy: https://scipy.org/
.. _bokeh: https://bokeh.pydata.org/en/latest/
.. _Jupytext: https://jupytext.readthedocs.io/en/latest/introduction.html
.. _DEAP: https://deap.readthedocs.io/en/master/
.. _simanneal: https://github.com/perrygeo/simanneal
.. _admcycles: https://www.math.uni-bonn.de/people/schmitt/admcycles
.. _sherpa: https://parameter-sherpa.readthedocs.io/en/latest/
.. _GPyOpt: https://sheffieldml.github.io/GPyOpt/
.. _GPy: http://sheffieldml.github.io/GPy/
.. _CoCalc Docker: https://github.com/sagemathinc/cocalc-docker
.. _PyShp: https://github.com/GeospatialPython/pyshp
.. _go: https://golang.org/
.. _beautifulsoup4: https://www.crummy.com/software/BeautifulSoup/
.. _textract: https://textract.readthedocs.io/en/stable/
.. _tpot: https://epistasislab.github.io/tpot/
.. _scikit-mdr: https://github.com/EpistasisLab/scikit-mdr
.. _scikit-rebate: https://github.com/EpistasisLab/scikit-rebate
.. _pytables: http://www.pytables.org/
.. _xgboost: https://xgboost.readthedocs.io/en/latest/
.. _lerna.js: https://lerna.js.org/
.. _moreutils: https://joeyh.name/code/moreutils/
.. _coffescript: https://coffeescript.org/
.. _iverilog: http://iverilog.icarus.com/
.. _Verilog: https://en.wikipedia.org/wiki/Verilog
.. _GTKWave: http://gtkwave.sourceforge.net/
.. _keras: https://keras.io
.. _ortools: https://developers.google.com/optimization
.. _joblib: https://joblib.readthedocs.io/
.. _h5py: https://www.h5py.org/
.. _periodictable: http://www.reflectometry.org/danse/elements.html
.. _teneto: https://teneto.readthedocs.io/
.. _sklearn-porter: https://github.com/nok/sklearn-porter
.. _sklearn-pandas: https://github.com/scikit-learn-contrib/sklearn-pandas
.. _scikit-posthocs: https://scikit-posthocs.readthedocs.io/
.. _pandas-datareader: https://pandas-datareader.readthedocs.io/
.. _pandas-gbq: https://pandas-gbq.readthedocs.io/
.. _scikit-surprise: http://surpriselib.com/
.. _python-highcharts: https://github.com/kyper-data/python-highcharts
.. _Highcharts: https://www.highcharts.com/
.. _monty: https://github.com/materialsvirtuallab/monty
.. _rust: https://www.rust-lang.org/
.. _networkx: https://networkx.github.io/documentation/stable/
.. _sqlalchemy: https://www.sqlalchemy.org/
.. _datrie: https://github.com/pytries/datrie
.. _cherrypy: https://cherrypy.org/
.. _coverage: https://github.com/nedbat/coveragepy
.. _petsc: https://www.mcs.anl.gov/petsc/
.. _slepc: http://slepc.upv.es/
.. _fenics: https://fenicsproject.org/
.. _memory_profiler: https://pypi.org/project/memory-profiler/
.. _dill: https://github.com/uqfoundation/dill
.. _cytoolz: https://github.com/pytoolz/cytoolz
.. _emcee: https://emcee.readthedocs.io/
.. _qutip: http://qutip.org/
.. _geopandas: http://geopandas.org/
.. _pyproj: https://github.com/pyproj4/pyproj
.. _pystan: https://pystan.readthedocs.io/
.. _symengine: https://github.com/symengine/symengine
.. _llvmlite: http://llvmlite.pydata.org/en/latest/
.. _datashader: https://datashader.org/
.. _django: https://www.djangoproject.com/
.. _kwant: https://kwant-project.org/
.. _psycopg2: http://initd.org/psycopg/docs/
.. _folium: https://python-visualization.github.io/folium/
.. _ipyleaflet: https://ipyleaflet.readthedocs.io/en/latest/
.. _natsort: https://natsort.readthedocs.io/en/master/
.. _mpi4py: https://mpi4py.readthedocs.io/en/stable/
.. _drracket: https://racket-lang.org
.. _fsspec: https://filesystem-spec.readthedocs.io/
.. _gcsfs: https://gcsfs.readthedocs.io/
.. _pint: https://pint.readthedocs.io/
.. _pynormaliz: http://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/backend_normaliz.html
.. _git-lfs: https://git-lfs.github.com/
.. _python: https://www.python.org/
.. _adtk: https://arundo-adtk.readthedocs-hosted.com/
.. _pdpipe: https://github.com/shaypal5/pdpipe
.. _nltk: https://www.nltk.org/
.. _doepy: https://doepy.readthedocs.io/en/latest/
.. _diversipy: https://www.simonwessing.de/diversipy/doc/
.. _scikit-learn: https://scikit-learn.org/
.. _puma: https://www.bioconductor.org/packages/release/bioc/html/puma.html
.. _oligo: https://www.bioconductor.org/packages/release/bioc/html/oligo.html
.. _sympy: https://www.sympy.org/
.. _pypy: https://www.pypy.org/
.. _kplr: http://dfm.io/kplr/
.. _pillow: https://pillow.readthedocs.io/en/stable/
.. _pywavelets: https://pywavelets.readthedocs.io/en/latest/
.. _imageio: http://imageio.github.io/
.. _DeclareDesign: https://cran.r-project.org/package=DeclareDesign
.. _DesignLibrary: https://cran.r-project.org/package=DesignLibrary
.. _SpecialMatrices: https://github.com/JuliaMatrices/SpecialMatrices.jl
.. _ApproxFun: https://juliaapproximation.github.io/ApproxFun.jl/latest/
.. _tensorflow-estimator: https://www.tensorflow.org/guide/estimator
.. _tensorflow-probability: https://www.tensorflow.org/probability
.. _SentimentAnalysis: https://cran.r-project.org/web/packages/SentimentAnalysis/vignettes/SentimentAnalysis.html
.. _pgmpy: https://pgmpy.org/
.. _bitarray: https://github.com/ilanschnell/bitarray
.. _pyreadstat: https://github.com/Roche/pyreadstat
.. _okpy: https://okpy.org/
.. _drive-cli: https://github.com/nurdtechie98/drive-cli
.. _ifsFractals: https://github.com/francisp336/ifsFractals
.. _seaborn: https://seaborn.pydata.org/
.. _numba: https://numba.pydata.org/
.. _mypy: https://mypy.readthedocs.io/
.. _pygments: https://pygments.org/
.. _pip: https://pip.pypa.io/en/stable/user_guide/
.. _openscad: https://www.openscad.org/
.. _astroplan: https://astroplan.readthedocs.io/
.. _rpy2: https://rpy2.readthedocs.io/
.. _astropy: https://www.astropy.org/
.. _let us know: mailto:help@cocalc.com
.. _Mesa: https://mesa.readthedocs.io/
.. _Orange3: https://orange.biolab.si/
.. _Quandl: https://www.quandl.com/
.. _altair: https://altair-viz.github.io/
.. _empyrical: https://github.com/quantopian/empyrical
.. _xarray: http://xarray.pydata.org/en/stable/
.. _optlang: https://optlang.readthedocs.io/
.. _bqplot: https://github.com/bloomberg/bqplot
.. _arviz: https://arviz-devs.github.io/arviz/
.. _cobra: https://opencobra.github.io/cobrapy/
.. _pysal: https://pysal.readthedocs.io/
.. _scikit-rf: https://scikit-rf.readthedocs.io/
.. _qgrid: https://github.com/quantopian/qgrid
.. _tabulate: https://github.com/astanin/python-tabulate
.. _mlxtend: http://rasbt.github.io/mlxtend/
.. _isochrones: https://isochrones.readthedocs.io/
.. _openTSNE: https://opentsne.readthedocs.io/
.. _tellurium: http://tellurium.analogmachine.org/
.. _Coq: https://coq.inria.fr/
.. _ocaml: https://ocaml.org/
.. _nbconvert: https://nbconvert.readthedocs.io/
.. _octave: https://www.gnu.org/software/octave/
.. _fractint: https://www.fractint.org/
.. _surface evolver: http://facstaff.susqu.edu/brakke/evolver/evolver.html
.. _protobuf: https://developers.google.com/protocol-buffers
.. _nilearn: https://nilearn.github.io/
.. _LEAN: https://leanprover.github.io/about/
.. _mathlib: https://github.com/leanprover-community/mathlib
.. _Node.js: https://nodejs.org/en/
.. _spacy: https://spacy.io/
.. _nest-asyncio: https://github.com/erdewit/nest_asyncio
.. _cython: https://cython.org/
.. _jupyter-client: https://github.com/jupyter/jupyter_client
.. _jupyter-console: https://jupyter-console.readthedocs.io/en/latest/
.. _ipython: https://ipython.org/
.. _jupyterhub: https://jupyter.org/hub
.. _jupyterlab: https://jupyterlab.readthedocs.io/en/stable/
.. _ipykernel: https://ipython.readthedocs.io/en/stable/install/kernel_install.html
.. _requests: https://requests.readthedocs.io/en/master/
.. _curio: https://github.com/dabeaz/curio
.. _mltools: https://cran.r-project.org/package=mltools
.. _biopython: https://biopython.org/
.. _folium: https://python-visualization.github.io/folium/
.. _ccdproc: https://ccdproc.readthedocs.io/
.. _rasterio: https://rasterio.readthedocs.io
.. _coffeescript: https://coffeescript.org/
.. _npm: https://docs.npmjs.com/
.. _ijavascript: https://github.com/n-riesco/ijavascript
.. _chromedriver: https://github.com/giggio/node-chromedriver
.. _lerna: https://lerna.js.org/
.. _webpack: https://webpack.js.org/
.. _data-cli: https://datahub.io/docs
.. _nipype: https://nipype.readthedocs.io/
.. _healpy: https://healpy.readthedocs.io/
.. _GnuCOBOL: https://open-cobol.sourceforge.io/
.. _COBOL: https://en.wikipedia.org/wiki/COBOL
.. _Intel MKL: https://software.intel.com/en-us/mkl
.. _pwlf: https://github.com/cjekel/piecewise_linear_fit_py
.. _pyDOE: https://github.com/tisimst/pyDOE
.. _ruptures: https://github.com/deepcharles/ruptures
.. _Julia Packages on CoCalc: https://cocalc.com/doc/software-julia.html
.. _obspy: https://github.com/obspy/obspy/wiki
.. _stellargraph: https://www.stellargraph.io/
.. _genlasso: https://cran.r-project.org/package=genlasso
.. _coronavirus: https://cran.r-project.org/package=coronavirus
.. _rmdformats: https://bookdown.org/yihui/rmarkdown/rmdformats.html
.. _QuSpin: https://weinbe58.github.io/QuSpin/
.. _mathlibtools: https://github.com/leanprover-community/mathlib-tools
.. _PyLaTeX: https://jeltef.github.io/PyLaTeX/
.. _FFTW: https://juliamath.github.io/FFTW.jl/latest/
.. _Julia: https://julialang.org/
.. _mxnet: https://mxnet.apache.org/
.. _cmake: https://cmake.org/overview/
.. _pmdarima: https://alkaline-ml.com/pmdarima/
.. _fbprophet: https://facebook.github.io/prophet/
.. _pyscf: https://sunqm.github.io/pyscf/
.. _plink: https://www.math.uic.edu/t3m/plink/doc/
.. _snappy: https://snappy.math.uic.edu/
.. _spherogram: https://snappy.math.uic.edu/spherogram.html
.. _Epidemics-on-Networks: https://springer-math.github.io/Mathematics-of-Epidemics-on-Networks/
.. _grepcidr: http://www.pc-tools.net/unix/grepcidr/
.. _Haskell: https://www.haskell.org/
.. _Asciidoctor: https://asciidoctor.org
.. _hypothesis: https://hypothesis.readthedocs.io/en/latest/
.. _heroku: https://www.heroku.com/
