.. _ubuntu-2004-upgrade:

========================================
2020-08-18: Ubuntu 20.04 Upgrade
========================================

CoCalc's default software environment for new projects changed: It is based on `Ubuntu 20.04 <https://ubuntu.com/>`_ now!

.. warning::

    This update changes the system-wide Python to 3.8, Sage to 9.1 (`Python 3 syntax! <https://wiki.sagemath.org/Python3-user>`_), Julia to 1.5, and many more.
    It is possible to :ref:`continue using Ubuntu 18.04 <switch-to-ubnutu1804>`.

Just like before, updates are performed on a regular basis.
If something is missing, out of date, broken, or not quite ok, please :ref:`let us know <software-install-problems>`!


- Python:
    - Ubuntu is based on Python3. This means ``python`` and ``pip`` is for version 3 now! In doubt, be explicit with ``python2/pip2`` and ``python3/pip3``.
    - Python 2: is installed, but not maintained and only a small selection of still available packages installed. Maybe stay with Ubuntu 18.04 if you still need it!
    - Python 3: this updated to version 3.8, and contains a lot of pre-installed packages. In particular, almost all that were present in the previous environment are also installed here.
    - `Anaconda 2020 <https://www.anaconda.com/products/individual>`_: a new setup, based on Python 3.7. It contains almost all of the installed packages of the previous Anaconda 2019 environment. Start it via ``anaconda2020``.

- `SageMath <https://sagemath.org>`_:
    - Version 9.1 is the default now. This implies that Sage Worksheets will use the Python 3 syntax now. More information from the Sage project: https://wiki.sagemath.org/Python3-user
    - For older versions of Sage and the previous behavior of Sage Worksheets (8.9), :ref:`switch to use Ubuntu 18.04 <switch-to-ubnutu1804>`.
    - Discontinued a "development version", because it is too hard to maintain and if you really work with it, you need to have write access to all files and hence it must reside in your own project.

- `R Software Environment <https://www.r-project.org/about.html>`_:
    - This runs the official build of R at version 4. Many packages are already installed.
    - There is also a smaller R environment inside of Sage (``R-sage``)
    - Known issues: ``rstan`` fails to compile due to a conflict with the global Node.js 12 setup.

- `Julia <https://julialang.org/>`_:
    - Version 1.5 is installed, along with a selection of additional packages.

- LaTeX:
    - The default Ubuntu 20.04 `textlive  2019 <https://packages.ubuntu.com/focal/texlive-full>`_  distribution.

- `LEAN <https://leanprover.github.io/>`_:
    - The general future direction of CoCalc serving LEAN/mathlib will be to pin the version and not make frequent changes.
    - Initially, CoCalc is using the same setup as the newer one of codewars.com, i.e. ``3.11.0`` + `mathlib 51e2b4c <https://github.com/leanprover-community/mathlib/tree/51e2b4ccef20e49bc24ef86a6afe6e48196abbcf>`_
    - In the future, we will work on supporting a local project setup (see e.g. `issue #3589 <https://github.com/sagemathinc/cocalc/issues/3589>`_) via ``leanproject`` and ``elan``.

- `Octave <https://www.gnu.org/software/octave/>`_:
    - This setup is on-par with Ubuntu 18.04. In both cases built from 5.2.0 sources and a couple of packages are added.

- `ROOT <https://root.cern/>`_:
    - Updated to version 6. As usual, start it in the terminal via `start-root` and then call `root` or use the Jupyter Kernel.

- C/C++:
    - The jupyter kernels for C++ and ROOT are updated.

- Haskell:
    - **Discontinued**. We tried to install an updated version of IHaskell + some packages, but we failed.
    - Call for help: if someone in the Haskell community is motivated to help us set up a fresh setup, please `contact us <help@cocalc.com>`_.
    - Until then, :ref:`switch to Ubuntu 18.04 <switch-to-ubnutu1804>` to use the older setup.


.. _switch-to-ubnutu1804:

Continue using Ubuntu 18.04
=======================================

It is possible to switch back to the previous Ubuntu 18.04 software environment.
Select the environment you want to run in
Project Settings → Project Control → :ref:`Software Environment <software-environment>`.

You can also define the software environment for all student projects in a course.
That's in the course configuration, at the bottom, in the "Software environment" panel.


.. _future-of-ubuntu-1804:

Future of Ubuntu 18.04
=======================================

The previous "Default" Ubuntu 18.04 based environment will stay around at CoCalc for the foreseeable future.
There won't be frequent upgrades any more, though.
The focus of maintenance shifts towards supporting 20.04!


.. _software-install-problems:

Problems/Missing?
===========================

If you experience any problems or if you discover that some packages are missing,
please report to us at `<help@cocalc.com>`_.

Alternatively, you can install packages for Python, R and Julia in a project as well.
e.g. see :ref:`install-python-packages` and :ref:`install-r-packages`.

