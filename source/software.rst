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

.. _update-2018-12-30:

2018-12-30
-------------------------------

* Sage Development 8.6 beta0
* Sage 8.5 (not the default yet)
* (py3/new)
  - `PyFlux <https://pyflux.readthedocs.io>`_
  - `algopy <https://pythonhosted.org/algopy/>`_
  - `numdifftool <https://github.com/pbrod/numdifftools>`_
  - `xgboost <https://xgboost.readthedocs.io>`_ 0.8.1
  - `joblib <https://joblib.readthedocs.io>`_
  - `qiskit`_ (`demo qiskit.ipynb <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/quiskit.ipynb?viewer=share>`_)

.. _update-2018-12-22:

2018-12-22
-------------------------------

* (py3)
  - **new**: `nbval <https://github.com/computationalmodelling/nbval>`_ for unit-testing Jupyter Notebooks
* (x11)
  - **new**: `sqlitebrowser <https://sqlitebrowser.org/>`_
  - **updated**: OpenModelica 1.14
* (software)
  - SageMath development version 8.5.rc1
  - we have ``sqlite`` (version 2) and ``sqlite3`` (version 3) command line interface on board
  - Updated `Rust <https://www.rust-lang.org/>`_ to 1.30
  - broad Linux package update
* (node/upd): npm 6.50, TypeScript 3.2.2, `prettier <https://prettier.io/blog/2018/11/07/1.15.0.html>`_ from 1.11 to 1.15.3, ...
* (julia): removing deprecated 0.6 Jupyter kernel


.. _update-2018-12-16:

2018-12-16
-------------------------------

* (Py3)
   - **new:**
      - `Google API <https://developers.google.com/api-client-library/python/start/get_started>`_: see our `quickstart notes <https://doc.cocalc.com/examples/google-api.html>`_
      - utility libs: `locket <https://github.com/mwilliamson/locket.py>`_ 0.2.0, `partd <https://github.com/dask/partd/>`_ 0.3.9

   - **updated:** `numpy <http://www.numpy.org/>`_ 1.15.4, `pipenv <https://pipenv.readthedocs.io/en/latest/>`_ 2018.11.26, `MyPy <http://mypy-lang.org/>`_ 0.650 (`release notes <http://mypy-lang.blogspot.com/2018/12/mypy-0650-released.html>`_), `keras <https://keras.io/>`_ 2.2.4

* (x11)
    - **new**: `QGIS <https://qgis.org>`_, ``gnome-system-monitor``, `SAOImage DS9 <http://ds9.si.edu/site/Home.html>`_
    - **updated**: PyCharm
* (software/new): `ROOT <https://root.cern.ch/>`_ version 6.14/06, released 2018-11-05. To work with graphical interface: first, open up an X11 environment, then start ROOT by calling ``start-root`` in the terminal.
* (Sage/upd) Sage Development updated to 8.5.rc0

Note about future updates:

* We will remove Julia 0.6.x (0.7 and 1.0 remains for now)
* Make the ``python2`` jupyter kernel choice more explicit (System's global version vs. SageMath's)

.. _update-2018-12-08:

2018-12-08
-------------------------------

* (Julia/upd) Julia 1.0.2 (``julia-1``) and packages CSV, DataFrames, Gadfly, Statistics, LinearAlgebra and GLM in default `julia` 0.7
* (Software/new) `sqlline <https://github.com/julianhyde/sqlline>`_, JDBC for PostgreSQL and MySQL -- `issue #3400 <https://github.com/sagemathinc/cocalc/issues/3400>`_
* (Linux/upd) various updates, only minor version number changes
* (X11/new) ``kgraphviewer`` and additional launcher buttons
* (Py3/upd) graphviz 0.10.1, mxnet 1.3.1, tellurium 2.1.3, jinja2 2.9.6, pymc3 3.5, scikit-image 0.14.1
* (Py2&3/new) `hmmlearn 0.2.1 <https://hmmlearn.readthedocs.io/en/latest/>`_
* (Library) new entry `Scikit Image Tutorial <https://github.com/scikit-image/skimage-tutorials>`_ and updates of several entries


.. _update-2018-12-03:

2018-12-03
-------------------------------

* (Sage/upd) Sage Development updated to 8.5.beta6

.. _update-2018-12-01:

2018-12-01
-------------------------------

* (Py3/new+fix) dask 1.0, distributed 1.25, dask-glm 0.2, dask-ml 0.11 -- `CoCalc example <https://share.cocalc.com/share/20e4a191-73ea-4921-80e9-0a5d792fc511/dask.ipynb?viewer=share>`_ -- `Wiki page <https://github.com/sagemathinc/cocalc/wiki/Dask>`_
* (Py3/new) `Scikit-Optimize <https://scikit-optimize.github.io/>`_ -- `see CoCalc example <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/skopt.ipynb?viewer=share>`_


.. _update-2018-11-28:

2018-11-28
-------------------------------

* (Sage/upd) Sage Development updated to 8.5.beta5
* (Linux/upd) noteworthy minor updates: vs code: 1.29.1, bazel: 0.19.2, idle: 3.6.7, python3: 3.6.7, postgresql: 11.1
* (Py3/new) `NOAA SDK <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/noaa-sdk.ipynb?viewer=share>`_
* (Py3/upd) yapf 0.25, tensorflow 1.12, tensorboard 1.12, tensorflow-probability 0.5, scikit-learn 0.20.1, numba 0.40.1, arctic 1.73 (also Py2)

.. _update-2018-11-13:

2018-11-13
-------------------------------

* (Sage/upd) Sage Development updated to 8.5.beta3
* (C/new) `MLV-2 library <http://www-igm.univ-mlv.fr/~boussica/mlv/api/French/html/index.html>`_ and `test on CoCalc <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/mlv-2/?viewer=share/>`_
* (Gap/upd) `GAP 4.10.0 <https://mail.gap-system.org/pipermail/forum/2018/005826.html>`_


.. _update-2018-11-10:

2018-11-10
-------------------------------

* (Linux/upd) `git-lfs <https://git-lfs.github.com/>`_ 2.6.0
* (X11/new)
  * `krita <https://krita.org/en/>`_
  * `darktable <https://www.darktable.org/>`_
  * `blender <https://www.blender.org/>`_
  * `pcb-gtk <http://pcb.geda-project.org/>`_
  * `gschem <http://www.geda-project.org/>`_
* (Py/upd) `dask`_ 0.20.1, `distributed <http://distributed.dask.org/en/latest/>`_ 1.24.1
* (Py+Sage/new) `Automatic Differentiation "ad" <https://pythonhosted.org/ad/>`_ 1.3.2 → `Demo pythonhosted <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/ad.ipynb?viewer=share>`_
* (R/new) `hablar <https://cran.r-project.org/web/packages/hablar/index.html>`_

.. _update-2018-11-03:

2018-11-03
-------------------------------

* (py2/py3 updates): Bokeh 1.0, Sphinx 1.8.1, Plotly 3.3.0, tensorflow 1.11 (py3 only), Pip 18.1
* (Sage/upd) Sage Development version updated to `8.5.beta2`
* (py3/new)
    - `Tensorflow Probability <https://www.tensorflow.org/probability/>`_ Lib, especially for `edward2 <https://github.com/tensorflow/probability/tree/master/tensorflow_probability/python/edward2#edward2>`_ (formerly `edward <http://edwardlib.org/>`_)
    - `sklearn-porter <https://github.com/nok/sklearn-porter#sklearn-porter>`_: Transpile trained scikit-learn estimators to C, Java, JavaScript and others.

* (x11) xdotool, xclip, xvfb update
* (linux/upd) broad Linux update, in particular rustc 1.28, cargo 0.29, bazel 0.19, ...
* (node.js/upd) noteworthy are typescript 3.1.4, coffeescript 2.3.2, prettier 1.14.3, reveal-md 2.3.0 and tldr 3.2.5
* (R/upd) updating some packages like dplyr, knitr, data.table, plotly, etc.
* (R/new) `export <https://cran.r-project.org/web/packages/export/index.html>`_ package
* (R/new) installing "swirl" courses globally for R. Create an "X11 Desktop" file, run `R`, and then start it::

    > require(swirl)
    > swirl_options(swirl_data_dir = "/home/user/swirl")
    > swirl()

.. _update-2018-10-27:

2018-10-27
-------------------------------

* (upd) SageMath 8.4 as the new default Sage version.
   * Run ``sage_select`` in a terminal to change the default in a project.
   * known issue: ``libhomfly`` not available, because it doesn't compile

* (upd) SageMath development version 8.5.beta0
* (new) `Tellurium <http://tellurium.analogmachine.org/>`_ in Python 2 and 3. `example worksheet <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/tellurium.ipynb?viewer=share>`_
* (new) X11 releated: `nteract.io <https://nteract.io/>`_, `atom editor <https://atom.io/>`_ (to e.g. be able to install `juno for julia <http://junolab.org/>`_ in your project), `Avogadro <https://avogadro.cc/>`_, etc.
* (py2/py3) `monty library <http://guide.materialsvirtuallab.org/monty/>`_ and `pivottablejs <https://pypi.org/project/pivottablejs/>`_


.. _update-2018-10-18:

2018-10-18
-------------------------------

* (new) Sage 8.4 (default still 8.3). Use ``sage_select`` to switch it, test it, and maybe give us feedback.
* (new) PostgreSQL 11 (default still 10). It's in ``/usr/lib/postgresql/11/bin/``. To use it, fix your path, e.g. via ``path-remove "/usr/lib/postgresql/10/bin"; path-append "/usr/lib/postgresql/11/bin"`` in your ``~/.bashrc``.
* (upd) overall Linux software update. notable:
  * git (1:2.17.1-1ubuntu0.3`_
  * texlive-binaries (2017.20170613.44572-8ubuntu0.1)
* (new) xpra/websockify
* (new) couple of `X11 related software <x11-help>`_, like PSPP, Gimp, LibreOffice, ...
* (fix) relaxing policies for ImageMagick to be able to run `convert` on PDF files.

.. _update-2018-10-06:

2018-10-06
-------------------------------

* (upd/enh) Julia 1.0.1 and associated `Julia Jupyter kernel <https://share.cocalc.com/share/b9bacd7b-6cee-402c-88ed-9d74b07f29a1/julia-1.ipynb?viewer=share>`_
    * in a terminal, run ``julia-1`` to get the 1.0.1 release.

* (new) `Ada programming language <https://gcc.gnu.org/wiki/GNAT>`_ (`Ada wikibook <https://en.wikibooks.org/wiki/Ada_Programming>`_), including syntax highlighting of ``*.adb`` files
* (upd) overall Linux software update, in particular OpenCV libraries and ``python-opencv``
* (new/lib) ``libopenblas-dev`` for building C/Fortran code on top of it
* (new/bin) screen, `powerline <https://powerline.readthedocs.io/en/latest/usage/shell-prompts.html), `glances <https://nicolargo.github.io/glances/>`_, `docsify <https://docsify.js.org/#/?id=docsify>`_, gnat (GNU Ada compiler)
* (env) changing `TERM=xterm-256color` default environment variable
* (env) global config file for `htop`
* (new/py2,py3): ``prettytable``
* (chg) switching videochat from https://appear.in to https://meet.jit.si
* (new/py3) `jupytext <https://github.com/mwouts/jupytext/), [notedown <https://github.com/aaren/notedown>`_, `control <https://sourceforge.net/projects/python-control/>`_, and `slycot <https://github.com/python-control/Slycot>`_
* (upd/py3) jupyter nbconvert (just 5.3.1 to 5.4.0, but there could be `noticeable changes <https://nbconvert.readthedocs.io/en/latest/changelog.html#id1>`_)
* (bug/py) there are known issues with ``mpl_toolkits/Basemap`` -- please use Ubuntu's Python 3 environment.

.. _update-2018-09-29:

2018-09-29
-------------------------------

* (upd) broad Linux software packages update, including minor updates to bazel, chrome, curl and python3.6
* (upd/py3) "pip3" 18.0, seaborn 0.9.0, geopandas 0.4.0, and scikit-learn 0.20.0
* (upd/py2) "pip2" 18.0, seaborn 0.9.0, tensorflow 1.10.1
* (rem/ac5) removing broken `pandas-datareader` from anaconda5 (no update available yet, use Ubuntu's Python 3)
* (new/npm) `tldr pages <https://tldr.sh/>`_

.. _update-2018-09-23:

2018-09-23
-------------------------------

* (upd) broad round of updating Anaconda 5 packages
* (rem) Removal of PostgreSQL 9.6. We provide the 10.x series by default.
  - for the purpose of `upgrading <https://www.postgresql.org/docs/10/static/pgupgrade.html>`_, the old install is kept in ``/usr/lib/postgresql/9.6/`` for a little while.
* (fix) pandas-datareader incompatibility resolved
* (upd/py3) dask/distributed, SymPy 1.3, Numba 0.38.1/llvmlite, and pandas-datareader 0.7.0
* (upd/py2) pandas 0.23.4 and pandas-datareader 0.7.0
* (upd) `LEAN <https://leanprover.github.io/>`_ mathlib to rev `d0f1b21a9df64f`, located in `/ext/lean/lean-3.4.1-linux/mathlib/`.
* (new/py2+py3) `pyLADvis <https://pyldavis.readthedocs.io/en/latest/readme.html>`_
* (new) C++ 17 Jupyter kernel via `xeus-cling <https://github.com/QuantStack/xeus-cling/>`_
* (upd) `SageMath`_  `release 8.4.beta6 2018-09-22 <https://groups.google.com/d/topic/sage-release/lKuxjPFGWVw/discussion>`_

.. _update-2018-09-15:

2018-09-15
-------------------------------

* (new) R packages: `roperators <https://happylittlescripts.blogspot.com/2018/09/make-your-r-code-nicer-with-roperators.html>`_ and a couple from `R Views 2018-07 <https://rviews.rstudio.com/2018/08/27/july-2018-top-40-new-packages/>`_
* (upd) bazel 0.17.1
* (upd) nodejs 8.12 (+ npm package updates)
* (upd) relaxing browser compatibility check specifically for newest Firefox 60.2 ESR
* (upd) major changes in handling `RMarkdown <https://rmarkdown.rstudio.com/>`_ files
* (new) support for automatically processing `PythonTeX <https://ctan.org/pkg/pythontex>`_ code in LaTeX documents
* (new) additional Library entries for RMarkdown and LaTeX/PythonTeX examples
* (new) first iteration to support `LEAN <https://leanprover.github.io/>`_
* (upd) SageMath 8.4.beta5 (released on 2018-07-16)

.. _update-2018-09-11:

2018-09-11
-------------------------------

* (upd) `GAP 4.9.3 <https://www.gap-system.org/>`_
* (new/py3) Python 3 `RTree Spatial indexing <http://toblerity.org/rtree/>`_ used in `geopandas <http://geopandas.org/>`_

.. _update-2018-09-08:

2018-09-08
-------------------------------

* (fix) irregularities with man-pages introduces in previous update
* (compat) Firefox 62 was released, which works well again with CoCalc's websocket over Cloudflare
* (upd/py3) tensorflow 1.10.1
* (upd/node) npm 5.6.0 → 6.4.1, typescript 3.0.3, CoffeeScript 2.3.1 and a couple other global node packages
* (upd/linux) headless chrome 69, and a couple of linux system libs
* (upd/sage) SageMath development 8.4beta4 available
* (upd/anaconda) broad package upgrade of Anaconda5 environment
* (chg) Jupyter plots done via R in Sage output SVG by default


.. _update-2018-09-01:

2018-09-01
-------------------------------

* (new) stapler python tool, a successor of pdftk (which is discontinued) -- https://github.com/hellerbarde/stapler
* (new) julia 0.7 upgrade: either keep the existing 0.6 line, or select 0.7
   * (old) you can still select a 0.6 kernel or run julia-0.6
   * for 0.7, only a few global libraries installed, i.e. those where precompiling works without errors
   * upon opening a jupyter file, you have to explicitly select the version

*  (upd) isochrones library: upgraded, and primarily updated a lot of datasets into $ISOCHRONES for dartmouth, but also some for "mist" -- https://isochrones.readthedocs.io/en/latest/
* (fix) no man/doc pages were installed. this is fixed now.
* (new) giac wrapper script to expose sage's binary globally in $EXT/bin/giac. Therefore cocalc  provides giac again. https://www-fourier.ujf-grenoble.fr/~parisse/giac.html
* (enh) web client: tightening browser requirements to inform affected users about https://bugzilla.mozilla.org/show_bug.cgi?id=1453204 
* (exp) experimental support for LEAN -- https://leanprover.github.io/





.. _SageMath: https://sagemath.org
.. _Cadabra2: https://cadabra.science
.. _qiskit:  https://qiskit.org
.. _dask: https://dask.org


