.. _software-updates-2021:

Software Updates 2021
======================================


.. .. contents::
..      :local:
..      :depth: 1

.. highlight:: python

.. _update-2021-12-13:

2021-12-13: Routine updates...
-------------------------------------------------

- Python:
    - (upd) various packages

- Executables:
    - (upd) routine Linux package updates, including R packages
    - (upd) Jupyter Lab ``3.2.5``

- Known issues:
    - Selenium in Python, you can use the "Preivous" software environment instead

.. _update-2021-11-01:

2021-11-01: taichi, tikzplotlib, Scikit Optimize
-------------------------------------------------

- Python 3 (system-wide):
    - (new) `tikzplotlib`_ – export matplotlib to PGF/TikZ plots – `TikZ plot example <https://cocalc.com/share/public_paths/be93350eccca7cf72b62aa8eab2de1509be32a63>`_
    - (new) `taichi`_ ``0.8.4`` – *a parallel programming language for high-performance numerical computations* –  `taichi example <https://cocalc.com/share/public_paths/ae23d804c707870993372c86c66623bb933dc8c7>`_
    - (upd) `scikit-optimize`_ ``0.9`` to fix compatibility bugs
    - (upd) various package updates

- Executables:
    - (upd) Jupyter Lab ``3.2.1``
    - (upd) routine Linux package updates, including R packages


.. _update-2021-10-10:

2021-10-10: Routine updates
------------------------------------------------

- (upd) routine updates for system packages, Python and R


.. _update-2021-09-27:

2021-09-27: Mathics 4, Scikit-Learn 1.0, Julia 1.6.3
-----------------------------------------------------

- Executables:
    - (upd) `Mathics`_ ``4.0.0``
    - (upd) `Rust`_ ``1.55``
    - (upd) `Julia`_ ``1.6.3``

- Python (system-wide):
    - (upd) `scikit-learn`_ ``1.0``

- various package and system lib updates

.. _update-2021-09-07:

2021-09-07: PyPy (Python 3)
---------------------------------------------

- Python 3:
    - (new) for the audacious: `PyPy`_ jupyter kernel.

- Misc:
    - (upd) as usual, updated Python and Linux/R packages.


.. _update-2021-09-02:

2021-09-02:  Sage 9.4, NASM, ...
---------------------------------------------

- Executables:
    - (new): `SageMath`_ ``9.4`` – `Release Tour Sage 9.4 <https://wiki.sagemath.org/ReleaseTours/sage-9.4>`_, accessible via the "SageMath 9.4" Jupyter kernel, ``sage-9.4`` on the command-line, or run ``sage_select 9.4`` and restart the Sage Worksheet server. In the future, this will become the default Sage version.
    - (new): `NASM`_ ``2.15.05`` – *Netwide Assembler (NASM), an asssembler for the x86 CPU architecture portable to nearly every modern platform*

- Misc:
    - (upd) various updates to the "system-wide" and "Anaconda 2020" Python environments
    - (upd) some Julia packages
    - (upd) Linux packages

.. _update-2021-08-13:

2021-08-13: R 4.1.1
----------------------------------------------

- Executables:
    - (upd) `R`_ ``4.1.1``
    - (new) `zig`_ ``0.8.0`` – *a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software*

- Python 3 (system-wide):
    - (upd) `yfinance`_ ``0.1.63``

.. _update-2021-08-02:

2021-08-02: Octave 6.3.0
----------------------------------------------

- Executables:
    - (upd) `Octave version 6.3.0 <https://www.gnu.org/software/octave/news/release/2021/07/11/octave-6.3.0-released.html>`_

- Python 3 (system-wide):
    - (upd) `nbconvert`_ version 6 – it was erroneously reverted to 5.x

.. _update-2021-08-03:

2021-08-03: VSCode
--------------------------------------------

- Python 3 (system-wide)
    - (upd) `pymatgen`_ ``2022.0.11``

- Executables:
    - (new) `VSCode`_ **Server** – available in "+New" or "Settings"
    - (upd) `Jupyter Lab`_ ``3.1.1``


.. _update-2021-07-26:

2021-07-26  Julia 1.6.2
-------------------------------------------

- Julia:
    - (upd) version 1.6.2
    - (upd) all globally installed packages

- Executables
    - (upd) `Jupyter Lab`_ ``3.0.16``
    - (upd) `pandoc`_ ``2.14.1``
    - (new) `Paraview`_ – as a test. Open an x11 desktop, then ``cd /ext/paraview/current/bin/`` and ``./paraview``.

.. _update-2021-07-13:

2021-07-13: flipper in Sage
---------------------------------------

- Sage 9.3:
    - (new) `flipper`_ – *a program for computing the action of mapping classes on laminations on punctured surfaces using ideal triangulation coordinates*

.. _update-2021-07-12:

2021-07-12: MODIS and PreTeXt
------------------------------------------------

- Executables:
    - ``pretext`` CLI tool for `PreTeXt <https://pretextbook.org/doc/guide/html/guide-toc.html>`_

- R (system-wide):
    - (new) `MODIS`_ – *automatizing the creation of time series of raster images derived from MODIS Land Products data*

- various system package updates

.. _update-2021-07-05:

2021-07-05: Package updates
---------------------------------------------

Various updates for Python, R and other languages and also Linux system packages.

.. _update-2021-06-07:

2021-06-07: Octave ``6.2.0`` & Bugfixes
----------------------------------------------

- Executables:
    - `Octave`_ ``6.2.0``
    - `SAOImageDS9 <ds9>`_ ``8.2.1``

- R (system-wide):
    - updating ``Cairo`` to fix a `ggplot2`_ problem
    - various package updates

- Python 3 (system-wide):
    - various updates


.. _update-2021-05-17:

2021-05-17: HAXE
---------------------------------------

- Executables:
    - (new) `HAXE`_ ``4.2.1`` – *an open source high-level strictly-typed programming language with a fast optimizing cross-compiler*
    - (new) `SageMath`_ ``9.3``: available as ``sage-9.3`` on the command-line and via Jupyter Notebooks. For Sage Worksheets, run ``sage_select 9.3`` first.


.. _update-2021-04-26:

2021-04-26: Julia ``1.6.1``
---------------------------------------

- Julia:
    - (upd) `Julia`_ version ``1.6.1``
    - (new) `Pluto Notebook`_ – see :ref:`instructions for CoCalc <howto-pluto>`
    - (upd) refreshing various globally installed packages

- Python 3 (system-wide):
    - (upd) various pkgs


.. _update-2021-04-03:

2021-04-03: R 4.0.5 ("Shake and Throw")
---------------------------------------

- R:
    - (upd) `R`_ to ``4.0.5``
    - (upd) rebuilding/updating all R packages

- Python 3 (system-wide):
    - (new) `Pyro`_ ``1.6.0`` – *Deep universal probabilistic programming with Python and PyTorch*
    - (upd) various pkgs

.. _update-2021-03-21:

2021-03-21: Julia 1.6
---------------------------------------

- Julia:
    - Version 1.6 & rebuilding all pre-installed libraries

- Python 3 (Anaconda 2020):
    - (new) `lmfit`_ – *provides a high-level interface to non-linear optimization and curve fitting problems for Python*
    - (new) `periodictable-py`_ – *provides an extensible periodic table of the elements pre-populated with data important to neutron and X-ray scattering experiments*

- Python 3 (system-wide):
    - (new) `sktime`_ – *specialized time series algorithms and scikit-learn compatible tools to build, tune and validate time series models for multiple learning problems*
    - (upd) various libs


.. _update-2021-03-08:

2021-03-08: Bioconductor
---------------------------------------

- R (system-wide):
    - (upd) refresh of all `bioconductor`_ packages, incl. `oligo`_
    - (new) `biomaRt`_  – *provides an interface to a growing collection of databases*

.. _update-2021-03-05:

2021-03-05: ASE, Papermill, etc.
---------------------------------------------------------------

- Software
    - (new) `papermill`_ – *Papermill is a tool for parameterizing and executing Jupyter Notebooks.*
    - (upd) system packages, some python packages, R, etc.

- Python 3 (Anaconda 2020)
    - (new) `ase`_ – The Atomic Simulation Environment (ASE) is a set of tools and Python modules for setting up, manipulating, running, visualizing and analyzing atomistic simulations.*


.. _update-2021-02-17:

2021-02-17: Rust 1.5
---------------------------------------------------------------

- Software
    - (upd) `Rust`_ ``1.5``
    - (upd) various system packages


.. _update-2021-01-28:

2021-01-28: Julia 1.5.3, MACS2, ...
---------------------------------------------------------------

- Julia:
    - (upd) to version 1.5.3 and updating all packages we provide per default

- Software
    - (new) `macs2`_ – Model-based Analysis of ChIP-Seq
    - various system package updates


.. _update-2021-01-07:

2021-01-07: More Python libs!
---------------------------------------------------------------

- Python 3 (system-wide):
    - (new) `agate`_: *a Python data analysis library that is optimized for humans instead of machines. It is an alternative to numpy and pandas that solves real-world problems with readable code.*
    - (new) `scrapy`_: *An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.*
    - (new) `squarify`_: *Pure Python implementation of the squarify treemap layout algorithm*
    - (new) `SHERPA`_: *A Python Hyperparameter Optimization Library*

- various other package and software updates



.. The duplication below with the 2020 file extremely silly, but I don't know how to share references properly

.. _DS9: https://sites.google.com/cfa.harvard.edu/saoimageds9
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
.. _bokeh example notebook: https://cocalc.com/share/public_paths/224f8112a2798e52129e9ec55d71271ac400ba57
.. _scipy: https://scipy.org/
.. _bokeh: https://bokeh.pydata.org/en/latest/
.. _Jupytext: https://jupytext.readthedocs.io/en/latest/introduction.html
.. _DEAP: https://deap.readthedocs.io/en/master/
.. _simanneal: https://github.com/perrygeo/simanneal
.. _admcycles: https://www.math.uni-bonn.de/people/schmitt/admcycles
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
.. _rpcinfo: http://manpages.ubuntu.com/manpages/bionic/man7/rpcinfo.7.html
.. _pycaret: https://pycaret.org/
.. _r: https://www.r-project.org
.. _matplotlib_venn: https://github.com/konstantint/matplotlib-venn
.. _Mathics: https://mathics.org/
.. _gprMax: https://www.gprmax.com/
.. _pybedtools: https://daler.github.io/pybedtools/
.. _periodictable-py: https://periodictable.readthedocs.io/en/latest/
.. _lmfit: https://lmfit.github.io/lmfit-py/
.. _materialize: https://materialize.com/
.. _hardlink: https://linux.die.net/man/1/hardlink
.. _agate: https://agate.readthedocs.io/
.. _scrapy: https://scrapy.org/
.. _squarify: https://github.com/laserson/squarify
.. _SHERPA: https://parameter-sherpa.readthedocs.io/
.. _macs2: https://macs3-project.github.io/MACS/
.. _ase: https://wiki.fysik.dtu.dk/ase/
.. _papermill: https://papermill.readthedocs.io/en/latest/
.. _biomaRt: https://bioconductor.org/packages/release/bioc/vignettes/biomaRt/inst/doc/biomaRt.html
.. _oligo: https://www.bioconductor.org/packages/release/bioc/html/oligo.html
.. _sktime: https://www.sktime.org/en/latest/
.. _pyro: https://pyro.ai/
.. _Pluto Notebook: https://github.com/fonsp/Pluto.jl
.. _HAXE: https://haxe.org/
.. _ggplot2: https://ggplot2.tidyverse.org/
.. _MODIS: https://docs.ropensci.org/MODIStsp/
.. _flipper: https://github.com/MarkCbell/flipper
.. _Paraview: https://www.paraview.org/
.. _VSCode: https://code.visualstudio.com/
.. _pymatgen: https://pymatgen.org/
.. _yfinance: https://aroussi.com/post/python-yahoo-finance
.. _zig: https://ziglang.org/
.. _nasm: https://nasm.us/
.. _PyPy: https://www.pypy.org/
.. _scikit-optimize: https://scikit-optimize.github.io/stable/
.. _tikzplotlib: https://github.com/nschloe/tikzplotlib
.. _taichi: https://github.com/taichi-dev/taichi
