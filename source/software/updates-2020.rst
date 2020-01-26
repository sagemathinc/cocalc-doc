.. _software-updates-2020:

Software Updates 2020
======================================


.. .. contents::
..      :local:
..      :depth: 1



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
.. _numpy: https://numpy.org/
.. _matplotlib: https://matplotlib.org/
.. _pytest: https://docs.pytest.org/en/latest/
.. _spyder: https://www.spyder-ide.org/
.. _pandas-bokeh: https://github.com/PatrikHlobil/Pandas-Bokeh
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
.. _admcycles: https://gitlab.com/jo314schmitt/admcycles
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
.. _SentimentAnalysis: https://cran.r-project.org/web/packages/SentimentAnalysis/vignettes/SentimentAnalysis.html
.. _pgmpy: https://pgmpy.org/
.. _bitarray: https://github.com/ilanschnell/bitarray
.. _pyreadstat: https://github.com/Roche/pyreadstat
.. _okpy: https://okpy.org/
.. _drive-cli: https://github.com/nurdtechie98/drive-cli
.. _ifsFractals: https://github.com/francisp336/ifsFractals
.. _seaborn: https://seaborn.pydata.org/
.. _numba: https://numba.pydata.org/
