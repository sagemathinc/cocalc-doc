.. index:: Python Packages
.. _install-python-packages:

============================
Install Python Packages
============================

This page describes how to install a Python package in a CoCalc project.

CoCalc already includes hundreds of packages for several Python environments.
**Check first** if the lib you're looking for `is already installed <https://cocalc.com/doc/software-python.html>`_!

Related: :doc:`custom-jupyter-kernel`, :doc:`jupyter-extension` and :doc:`install-r-package`.


.. contents::
   :local:
   :depth: 3

.. _install-request:

Install requests
===================

If a package may have general use but is not already installed in CoCalc,
please open a support request to tell us to install it globally for everyone.
Uncomplicated install requests are typically handled within 1 business day for paying customers.
Install will happen faster if you include as much as possible of the following information:

* Which Python environment?
* A link to the package website
* Special requirements and dependencies to build & install
* A short but complete example, such that we can verify that we properly installed the software. This example might be included in internal tests, to make sure future updates do not break that library.


.. _python-pkg-install-user:

Python "user" installs
===================================

You can install additional packages yourself, but only at user-permission level.
CoCalc accounts do not have superuser (root) privileges.
Software must be installed into user-writeable parts of the filesystem, which are in ``/home/user`` (check the value of ``$HOME``).

.. note::

    After installing a package, you may need to restart your kernel **twice** before you can use it. It takes time to check if a module is available, so for performance reasons Python caches such checks and they could be performed by some libraries, not your code. This makes it necessary to restart the kernel once. In addition, CoCalc often keeps a fresh kernel ready for you to use, so that you don't have to wait for it to start. But this spare kernel may "remember" that your package is not installed, hence it has to be discarded as well.


.. warning::

    Your project **must** have the :ref:`"Internet access" upgrade <project-upgrades>` in order to download software from a remote repository (e.g. PyPI or Anaconda) to your project.
    Installing a Python package will require you to :ref:`add a license <project-add-license>` or :ref:`add upgrades <project-upgrades>` so that your project has internet access.


**In a nutshell:** a CoCalc project is a Linux user account under the username ``user``.
Therefore, installing software and libraries should usually be done in ``~/.local`` (i.e. ``/home/user/.local``),
which is the canonical location for user installs.
Furthermore, in case the documentation mentions to specify a custom "prefix" path,
set this to ``~/.local``.
Executables will install into ``~/.local/bin`` and will work right away,
because projects already include that path in their ``$PATH`` variable.


Install location and ``sys.path``
------------------------------------

The path that looks like ``~/.local/lib/python3.10/site-packages`` will contain the package you've installed.
In some cases (like when you are using Sage) your Python environment may not be able to find the package and you might have to add that path dynamically during runtime like that::

    import sys, os
    sys.path.insert(0, os.path.expanduser('~/.local/lib/python3.10/site-packages'))

Make sure that the path is correct, since it includes the version number.


pip
------------------------------------

Pip is the "Python package manager".
It installs packages hosted at `PyPI.org <https://pypi.org/>`_.

If your package can be installed via ``pip``,
then run in a :doc:`CoCalc Terminal file <../terminal>`:

* Python2: ``pip2 install --user [package-name]``
* Python3: ``pip3 install --user [package-name]``

.. note::

    **Regarding Python 2 vs. Python 3:**

    * Python 2: use ``pip2`` and ``python2``/``ipython2``.
    * Python 3: use ``pip3`` and ``python3``/``ipython3`` -- ``pip`` and ``python`` should default to these variants.

If you've :doc:`uploaded a zip/wheel file <./upload>`,
change the ``[package-name]`` to the actual filename.

pip install directly from git repository
---------------------------------------------

Suppose there is a GitHub repository for a python 3 package at :samp:`https://github.com/{organization}/{repo}`. (There should be a ``setup.py`` file at the top-level directory of the repo.)
The simplest way to install directly from GitHub via pip is this::

    pip3 install --user git+https://github.com/organization/repo.git

This approach works with any remote git repository for which you have the necessary access.


setup.py
------------------------------------

If your package is in a folder inside your project
(e.g., :doc:`you uploaded it <./upload>`) which includes a ``setup.py`` file,
you can do either ``python setup.py install --user`` or ``pip install --user --upgrade ./``

(Some setup instructions alternatively mention ``python setup.py install --home``)

If pip requires that any external dependencies be downloaded, then your project must have internet access.



Virtualenv
------------------------------------

You can avoid the need for ``--user`` flags if you work inside a Python virtual environment.
See  `Virtualenv`_ for more information.




.. _sage-install-python-pkg:

Sage
------------------------------------

A special case is `SageMath`_, which is a fully integrated environment built on top of Python.

To install a python package to be used from Sage, first open a CoCalc :doc:`../terminal`. Then run the command::

    sage --pip install <package_name>

After this, you will be able to use the python package from within Sage in any of these settings:

* Command-line Sage.
* :doc:`../sagews`. After installing the package, you will have to restart the Sage worksheet server under project Settings, or restart the project.
* Jupyter notebook running the Sage kernel. The version of Sage in the Jupyter kernel selected must match the version of Sage used on the command line to install the package. Restart the Jupyter kernel to pick up the newly installed package.


Pipenv with a Jupyter Kernel
======================================

Here, we explain how to setup your own encapsulated Python environment using `pipenv`_.
You can either choose to use the global packages,
or – as we do here – tell it to only have explicitly installed ones on board.

We start with an empty directory in our ``$HOME``::

    ~$ cd
    ~$ mkdir my-special-env
    ~$ cd my-special-env

Then we run ``pipenv install`` without site packages and specifying the python interpreter to use (Note: by default it might pick up ``pypy3``, which is not a good idea in general). Install pandas below version ``1.2`` and the juypter kernel::

    ~/my-special-env$ pipenv install --python /usr/bin/python3 --no-site-packages ipykernel 'pandas<1.2'
    [output is abbreviated ...]
    Creating a virtualenv for this project...
    ✔ Successfully created virtual environment! 
    Installing ipykernel...
    ✔ Installation Succeeded 
    Installing pandas<1.2...
    ✔ Installation Succeeded 
    ✔ Success! 
    Updated Pipfile.lock (4eda65)!
    Installing dependencies from Pipfile.lock (4eda65)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
    To activate this project's virtualenv, run pipenv shell.

Now, we can launch it and give it a try. Let's check if Pandas is below version ``1.5`` and other libs like ``scipy`` are not available::

    ~/my-special-env$ pipenv shell
    Launching subshell in virtual environment...
     . /home/user/.local/share/virtualenvs/my-special-env-gNmS0l6R/bin/activate
    ~/my-special-env$  . /home/user/.local/share/virtualenvs/my-special-env-gNmS0l6R/bin/activate
    (my-special-env) ~/my-special-env$ python
    Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import scipy
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'scipy'
    >>> import pandas
    >>> pandas.__version__
    '1.1.5'

Finally, we install the Juypter Kernel. We run ``ipykernel install`` and give the kernel a unique name.
After opening the file in CoCalc's editor via ``open <filename.ipynb>`` ,
make sure to run "Kernel" → "Refresh kernel list", to get the new kernel.
Then select it and you're good to code!

::

    (my-special-env) ~/my-special-env$ python3 -m ipykernel install --user --name=my-special-env
    Installed kernelspec my-special-env in /home/user/.local/share/jupyter/kernels/my-special-env
    (my-special-env) ~/my-special-env$ open my-special-env.ipynb
    creating file 'my-special-env.ipynb'

All in all this gives you a precisely defined environment, outfitted with checksums for all dependencies for reproducibility.

.. _anaconda-install:

Anaconda Environment
=======================

`Conda <https://conda.io/en/latest/>`_ is an alternative packaging system by `Anaconda <https://anaconda.org/>`_.
It is mostly used for Python packages, but it can manage and deliver almost any kind of software.

CoCalc provides a global environment, which you can start by running ``anaconda2020`` in a :doc:`../terminal` or a related kernel in a :doc:`../jupyter`.
To get going with your own setup for your own CoCalc project,
you have to :ref:`create your own environment <anaconda-install-own-env>`
and your :ref:`own kernel <anaconda-jupyter>`.

.. _anaconda-install-own-env:

Install my own Anaconda environment
------------------------------------------------------------

This will create a custom Anaconda overlay environment called ``myenv`` in your project.

To get it installed in Anaconda as a user, do this:

1. Open a terminal.

2. Type ``anaconda`` to launch.

3. Type ``mamba env create --prefix ~/myenv --file=environment.yml`` This creates a new isolated local (hence ``--prefix ...``) environment in the directory ``~/myenv``. Use an :download:`environment.yml <../_files/environment.yml>` to reconstruct from a full definition. For more details, see http://conda.pydata.org/docs/using/envs.html#create-an-environment.

4. When installing, it will resolve the package dependencies, download packages, unpack and install them. Afterwards, run ``mamba clean --all --yes`` to save disk space.

5. Now that we have it installed, we can get out of this "root" environment via ``source deactivate`` or restart the session. In any case, you are back in the the normal Linux terminal environment.

6. To activate it again, run ``source ~/myenv/bin/activate``. You can also add this line to your Terminal's :ref:`terminal-startup-files`.

7. In the very same spirit, you can also run pip installations::

    (myenv)~$ pip install plotly
    Downloading/unpacking plotly
    [...]
    Successfully installed plotly requests six pytz


.. _anaconda-jupyter:

Configure a Jupyter kernel for my custom Anaconda environment
--------------------------------------------------------------------

Make sure to install ``ipykernel`` in your custom environment. Then see :ref:`install-custom-python-env-kernel`.


.. _Virtualenv: https://virtualenv.pypa.io/en/latest/user_guide.html

.. _pipenv: https://pipenv.pypa.io/en/latest/

.. _SageMath: https://sagemath.org
