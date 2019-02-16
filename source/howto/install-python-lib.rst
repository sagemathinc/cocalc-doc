.. index:: Python Packages

============================
Install Python Packages
============================

This page decribes how to install a Python package in a CoCalc project.

CoCalc already includes `hundreds of packages for several Python development environments <https://cocalc.com/doc/software-python.html>`_.


.. contents::
   :local:
   :depth: 3

Install requests
===================

If a package may have general use but is not already installed in CoCalc, you can open a support request to install it.
Uncomplicated install requests are typically handled within 1 business day for paying customers.
Install will happen faster if you include as much as possible of the following information:

* Which Python environment?
* Which language version: 2 or 3?
* A link to the package website
* Special requirements and dependencies to build & install
* A short but complete example, such that we can verify that we properly installed the software. This example might be included in internal tests, to make sure future updates do not break that library.

User installs
==================

You can install additional packages yourself, but only at user-permission level.
CoCalc accounts do not have superuser (root) privileges.
Software must be installed into user-writeable parts of the filesystem, which are in ``/home/user`` (check the value of ``$HOME``).

.. note::

    **In a nutshell:** a CoCalc project is a Linux user account under the username ``user``.
    Therefore, installing software and libraries should usually be done in ``~/.local`` (i.e. ``/home/user/.local``),
    which is the canonical location for user installs.
    Furthermore, in case the documentation mentions to specify a custom "prefix" path,
    set this to ``~/.local``.
    Executables will install into ``~/.local/bin`` and will work right away,
    because projects already include that path in their ``$PATH`` variable.


.. _python-pkg-install-user:

Install Python packages as a user
------------------------------------

.. note::

    In the case of Python 2, ``$HOME/.local/lib/python2.7/site-packages/`` will contain the package you've installed.
    Similarly, this path will contain ``python3.5`` for a Python 3.5 executable.

    In case your Python environment can't find the package,
    you might have to add your ``~/.local/...`` directory dynamically during runtime like that::

        import sys, os
        sys.path.insert(0, os.path.expanduser('~/.local/lib/python2.7/site-packages'))

    Make sure, the path is correct.
    I.e. for Python 3 this could be one of ``python3.4``, ``python3.5``, ``python3.6``...

pip
^^^^^^^^^^^^

Pip is the "Python package manager". It installs packages hosted at `PyPI.org <https://pypi.org/>`_.

If your package can be installed via ``pip``, then run in a  `CoCalc Terminal file <../terminal>`_:

* Python2: ``pip2 install --user [package-name]``
* Python3: ``pip3 install --user [package-name]``

.. note::

    **Regarding Python 2 vs. Python 3:**

    * Python 2: use ``pip2`` and ``python2``/``ipython2`` -- ``pip`` and ``python`` should default to these variants.
    * Python 3: use ``pip3`` and ``python3``/``ipython3``.

.. warning::

    Your project **must** have the :ref:`"Internet access" upgrade <project-upgrades>` in order to download software from the pip repository to your project.  The Python pip command will not work unless you :ref:`upgrade your project <project-upgrades>` to have internet access.

setup.py
^^^^^^^^^^^^^

If your package is in a folder inside your project (e.g., you uploaded it) with a ``setup.py`` folder, you can do either ``python setup.py install --user`` or ``pip install --user --upgrade ./``

(Some setup instructions alternatively mention ``python setup.py install --home``)

If pip requires that any external dependencies be downloaded, then your project must have internet access.

Virtualenv
^^^^^^^^^^^^^^^

You can avoid the need for ``--user`` flags if you work inside a Python virtual environment.
See  `Virtualenv`_ for more information.

Sage
^^^^^^^^^^^^^^^^^^

A special case is [SageMath]_, which is a fully integrated environment built on top of Python.
To install a Python package in Sage, it needs to also install into your local home directory.
To accomplish that, first start the Sage-environment in a Terminal, and then issue the pip-install command with ``--user``. For example:

1. ``sage -sh`` for the sage environemnt
2. ``pip install --user git+https://github.com/videlec/sage-flatsurf``

If it happens that Sage doesn't recognize packages in your local path, prepend them to your path via running

::

    import site, sys
    sys.path.insert(0, site.USER_SITE)


Other
^^^^^^^^^^^^^^^^^

There are also other managers, which might fit your needs:

* `pyenv <https://github.com/pyenv/pyenv>`_


Sage Worksheets
=====================

.. note::

    In case you run a CoCalc worksheet, you need to restart the worksheet server (in the project's settings) and then the worksheet itself via the "restart" button.


.. _anaconda-install:

Anaconda
====================

Install some software into my own Anaconda environment
------------------------------------------------------------

The task below is to create a custom Anaconda overlay environment called ``myconda`` and, just for the sake of explanation,

1. install "Microsoft's Open R" (which is an enhanced version of R by Microsoft).
2. Install the plotly library from PyPI

To get it installed in Anaconda as a user, do this:

1. Open a terminal.

2. Type ``anaconda5``

3. Type ``conda create -n myconda -c mro r`` This creates a new local environment called "myconda" (name it as you wish) with the package "r" as its source coming from the channel "mro" (Microsoft's Open R). Instead of that, you can add any other anaconda package in that spot. The example from the documentation is biopython, see http://conda.pydata.org/docs/using/envs.html#create-an-environment.

4. When installing, it briefly shows you that it ends up in ``~/.conda/envs/myconda/....`` in your local files. Now that we have it installed, we can get out of this "root" environment via source deactivate or restart the session. In any case, you are back in the the normal Linux terminal environment.

5. Now run this: ``source ~/.conda/envs/myconda/bin/activate myconda`` Note that myconda is the name specified above, and the prompt switches to ``(myconda) $``. Typing ``which R`` shows: ``/projects/xxx-xxx-xxx/.conda/envs/myconda/bin/R`` and of course, just running ``R`` gives::

    R version 3.2.3 (2015-12-10) -- "Wooden Christmas-Tree"
    Copyright (C) 2015 The R Foundation for Statistical Computing
    Platform: x86_64-pc-linux-gnu (64-bit)
    [...]
    Microsoft R Open 3.2.3
    Default CRAN mirror snapshot taken on 2016-01-01
    The enhanced R distribution from Microsoft

6. In the very same spirit, you can also run pip installations::

    (myconda)~$ pip install plotly
    Downloading/unpacking plotly
    [...]
    Successfully installed plotly requests six pytz
    (myconda)~$ python -c 'import plotly; print(plotly)'
    <module 'plotly' from '/projects/20e4a191-73ea-4921-80e9-0a5d792fc511/.local/lib/python2.7/site-packages/plotly/__init__.pyc'>

Note that since I'm still in my own "myconda" overlay environment, the ``--user`` switch in ``pip install`` wasn't necessary. (Otherwise, it would be necessary.)



.. _anaconda-jupyter:

Configure a Jupyter kernel for my custom Anaconda environment
--------------------------------------------------------------------


With Anaconda's ``conda`` environment and software manager, you can `create custom environments <https://conda.io/docs/user-guide/tasks/manage-environments.html>`_ with specific versions of Python, R, and their packages. This is similar to capabilities provided by Python's environment manager, `Virtualenv`_.

Suppose you want to create a custom Anaconda environment with the ``mdtraj`` package and be able to use this environment in a Jupyter notebook. Here's how:

1. Follow these steps in `a .term file in CoCalc <../terminal>`_. In the last step, the display name of the new kernel is changed so that it does not duplicate the name of kernel installed by CoCalc::

        ~$ mkdir -p ~/.local/share/jupyter/kernels
        ~$ anaconda3
        (root) ~$ conda create --name mymdtraj mdtraj
        (root) ~$ source activate mymdtraj
        (mymdtraj) ~$ conda install ipykernel
        (mymdtraj) ~$ source deactivate
        ~$ mv ~/.conda/envs/mymdtraj/share/jupyter/kernels/python3 ~/.local/share/jupyter/kernels/mymdtraj
        ~$ open ~/.local/share/jupyter/kernels/mymdtraj/kernel.json
        ## change display_name from "Python 3" to "My mdtraj" and save the file

2. Open a new Jupyter notebook in CoCalc.
3. Click on the `Kernel` button and look for your new kernel, "My mdtraj", or whatever you used for ``display_name`` in ``kernel.json``. If you don't see your new kernel, scroll to the bottom of the Kernel menu and click `Refresh Kernel List`, and your new kernel should appear.
4. Select the new kernel. You will now be running the environment you created with the ``conda create`` command.


.. Virtualenv: https://virtualenv.pypa.io/en/stable/userguide/

