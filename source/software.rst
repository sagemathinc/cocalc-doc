.. index:: Software Stack

======================================
Software
======================================

The following software is used by CoCalc under the hood.
It's either installed directly or slightly modified to fit into the infrastructure.
Besides that, there is a `more detailed and fairly up-to-date list <https://cocalc.com/doc/software.html>`_ available.

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



.. _software-updates:

Software Updates
======================================

Recent updates to CoCalc's software stack available in the :ref:`"Default" environment <software-environment>`.

.. toctree::
   :maxdepth: 1
   :caption: Archive

   software/software-updates-2018


.. _update-2019-02-16:

2019-02-16
------------------

- New `SPARQL kernel <https://github.com/paulovn/sparql-kernel>`_: see `issue #3573 <https://github.com/sagemathinc/cocalc/issues/3573>`_. You can query remote endpoints. Make sure your project has :doc:`internet access <upgrade-guide>` enabled! (`SPARQL demo notebook <https://cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/sparql-vanGogh.ipynb?viewer=share>`_)

- `LEAN 3.4.2 <https://github.com/leanprover/lean/releases/tag/v3.4.2>`_, with a precompiled mathlib in ``/ext/lean/lean/mathlib``.

- Python 3 changes:
    - `JAX <https://github.com/google/jax>`_ (`jax demo worksheet <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/jax.ipynb?viewer=share>`_)
    - tornado 5.1.1, distributed 1.25.3
    - `mypy 0.6.7.0 <https://mypy-lang.blogspot.com/2019/02/mypy-0670-released.html>`_
    - `cython-0.29.5 <https://github.com/cython/cython/blob/master/CHANGES.rst#0295-2019-02-09>`_
    - pylint-2.2.2
    - requests-2.21.0
    - scipy-1.2.1 (see `1.2.0 <https://scipy.github.io/devdocs/release.1.2.0.html>`_ and `1.2.1 <https://scipy.github.io/devdocs/release.1.2.1.html>`_ notes)
    - `mesa-0.8.5 <https://github.com/projectmesa/mesa>`_
    - Sphinx-1.8.4 (update) and commonmark 0.8.1 and recommonmark-0.5.0 for developing `sphinx-rtd-theme-0.4.3 <https://sphinx-rtd-theme.readthedocs.io/en/latest/>`_ out of the box!
    - cookiecutter-1.6.0
    - `wordcloud-1.5.0 <https://amueller.github.io/word_cloud/>`_

- Python 2 changes: scipy-1.2.1, decorator-4.3.2, networkx-2.2, keras-applications-1.0.7, keras-preprocessing-1.0.9, tensorflow-1.12.0

- Sage's Python2: pip-19.0.2, PySingular-0.9.7, soupsieve-1.7.3, and a couple of dependencies

- R: `ggmap 3.0.0 <https://cran.r-project.org/web/packages/ggmap/>`_

- Linux: `PyPy 7.0.0 <https://pypy.org/>`_ and a set of minor linux package updates

- Node: `npm 6.8.0 <https://github.com/npm/cli/releases/tag/v6.8.0>`_


.. _update-2019-02-09:

2019-02-09
------------------------

- (Linux)
   - new: `Cantera <https://cantera.org/>`_ 2.4.0 for Python 2 and Python 3
   - updates: `macaulay2 <http://www2.macaulay2.com/Macaulay2/>`_ 1.13, bazel 0.22, chrome and firefox, and various other packages

- (Python3)
   - new: pyfftw 0.11.1, pymp-pypi 0.4.2
   - updates: dask-1.1.1

- (Node): npm 6.7.0

- (Julia): making **Julia 1.1.0 the default** (`v1.1.0 release notes <https://github.com/JuliaLang/julia/blob/v1.1.0/NEWS.md#julia-v11-release-notes>`_) and removing older, no longer maintained versions. Maybe cleanup the build cache, by running ``rm -rf ~/.julia`` in the Terminal/Miniterm.

- (Anaconda 5): various updates to packages

- (Sage) Development version 8.7 beta 3 (Python 3)


.. _update-2019-01-26:

2019-01-26
-------------------------

- (sage): **Sage 8.6** is the default! (use ``sage_select 8.4`` to switch back). Enjoy the shorter startup time, which also speeds up compiling :ref:`latex-sagetex` documents!
    - A Python3 version of Sage 8.6 is also available: ``sage-8.6-py3`` or in a Jupyter Notebook: `sagemath-8.6-python3.ipynb <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/smc-build/sagemath-8.6-python3.ipynb?viewer=share>`_. (this is experimental)

- (py3):
   - new:
      - `ipyvolume <https://github.com/maartenbreddels/ipyvolume#ipyvolume>`_ 0.5.1 (`demo notebook <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/ipyvolume-demo.ipynb?viewer=share>`_, requires the plain jupyter server!)
      - `qiskit-chemistry <https://github.com/Qiskit/qiskit-chemistry>`_ 0.4.2 – a set of tools, algorithms and software to use for quantum chemistry research
      - `PySCF <https://sunqm.github.io/pyscf/>`_ – a simple, light-weight, and efficient platform for quantum chemistry calculations

   - updated:
      - ``pip3`` 19.0.1
      - `qiskit`_ 0.7.2, qiskit-aqua 0.4.1
      - `scikit-bio <http://scikit-bio.org/>`_ 0.5.5
      - `dask`_ 1.1.0
      - nbgrader 0.5.5
      - ipython 6.5.0
      - Cython 0.29.2
      - setuptools 40.6.3
      - tensorboard 1.12.2
      - tmuxp 1.4.2
      - `axelrod <https://axelrod.readthedocs.io/en/stable/>`_ 4.4.0

- (R):
   - new:
      - `styler <http://styler.r-lib.org>`_ 1.1.0 – will be used soon to format R code; `tidyverse styleguide <https://style.tidyverse.org>`_
      - `usethis <https://usethis.r-lib.org>`_ 1.4.0
      - `tidytransit <https://cran.r-project.org/web/packages/tidytransit/index.html>`_

   - updated: knitr 1.21, ggplot 3.1.0, data.table 1.20.0, dplyr 0.7.8, Rcpp 1.0, rlang 0.3.1, forecast 8.5, psych 1.8.12, plotly 4.8, yaml 2.2

- (Julia): new: `D4M package <https://github.com/Accla/D4M.jl.git>`_ – *Dynamic Distributed Dimensional Data Model*
- (node/upd): **npm 6.6.0**, TypeScript 3.2.4, tslint 5.12.1, forever 0.15.3, CoffeeScript 2.3.2, reveal-md 2.4.1, prettier 1.16.0, tldr 3.2.6, docsify-cli 4.3.0, chromedriver 2.45.0
- (Linux) various system packages, noteworthy: xpra 2.4.3


.. _update-2019-01-20:

2019-01-20
-------------------------------

* (new) `SageMath`_ version 8.6 (`sage-8.6`) + Jupyter Kernel available (not the default yet!)
* (new) `Cadabra2`_ _"a field-theory motivated approach to computer algebra"_ available via ``cadabra2`` or in an `X11 desktop <https://doc.cocalc.com/x11.html>`_ as ``cadabra2-gtk`` (`screenshot <https://storage.googleapis.com/cocalc-extra/2019-01-19-cadabra2.png>`_)
* (chg) As announced previously, **Julia version 1** is the **default** now. Symlink ``~/bin/julia`` to ``julia-0.7`` if you need to switch back.
* (new): Julia 1 packages: SymPy, Combinatorics, UnicodePlots, Bokeh and Nemo
* (py3):

   - **new**:

      - `surprise <http://surpriselib.com/>`_ 1.0.6
      - `python-twitter <https://github.com/bear/python-twitter>`_ 3.5
      - `mlrose 1.0 <https://mlrose.readthedocs.io>`_: Machine Learning, Randomized Optimization and SEarch. `example <https://cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/py3-mlrose.ipynb?viewer=share>`_

   - **updates**:

      - `sphinx <http://www.sphinx-doc.org/en/master/>`_ 1.8.3
      - `statsmodels <https://www.statsmodels.org/stable/index.html>`_ 0.9.0 + `patsy <https://patsy.readthedocs.io/en/latest/>`_ 0.5.1 fixing some problems with formulas
      - `pymc3 <https://docs.pymc.io/>`_ 3.6
      - distributed 1.25.2
      - `Cython <https://cython.org>`_ 0.29.2
      - llvmlite 0.27.0 & `numba <http://numba.pydata.org/>`_ 0.42.0
      - `xarray <http://xarray.pydata.org/en/stable/>`_ 0.11.2
      - `quandl <https://www.quandl.com/tools/python>`_ 3.4.5
      - `plotly <https://plot.ly/python/>`_ 3.5.0
      - `apache-libcloud <https://libcloud.apache.org/>`_ 2.4.0
      - `black <https://github.com/ambv/black>`_ 18.9b0

.. _update-2019-01-12:

2019-01-12
-------------------------------

* (r): `Rstan <https://mc-stan.org/users/interfaces/rstan>`_ 2.18.2 → `demo worksheet <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/rstan.ipynb?viewer=share>`_, with some setup instructions specific to CoCalc
* (py2/py3): `PyStan <https://pystan.readthedocs.io/en/latest/index.html>`_ 2.18.1 (`demo  pystan.ipynb <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/smc-build/pystan.ipynb?viewer=share>`_)
* Julia 1:
  * JuMP & Ipopt (`demo julia-1-jump.ipynb <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/julia-1-jump.ipynb?viewer=share>`_)
  * We'll also switch the default version of Julia to be 1.0.x soon!
* Linux updates, notably bazel 0.21
* Fonts: ocr-a, ocr-b, `opendyslexic <https://gumroad.com/l/OpenDyslexic>`__, mononoki, comic-neue, linex, roboto, vollkorn, tuffy. `Testing some fonts in LuaTeX <https://share.cocalc.com/share/8baad8828430618da0446ee80d6ebcacb83bba14/fonts-luatex/fonts-in-luatex.pdf?viewer=share>`_ (`tex source <https://share.cocalc.com/share/8baad8828430618da0446ee80d6ebcacb83bba14/fonts-luatex/fonts-in-luatex.tex?viewer=share>`_)


.. _update-2019-01-06:

2019-01-06
-------------------------------

* Julia 1.0.3: comes with packages PyPlot, Plots, DifferentialEquations, Compat, LinearAlgebra, GLM, etc. now!
* Sage development version 8.6.rc0

.. _SageMath: https://sagemath.org
.. _Cadabra2: https://cadabra.science
.. _qiskit:  https://qiskit.org
.. _dask: https://dask.org


