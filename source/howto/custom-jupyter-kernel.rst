.. index:: Jupyter Notebooks; custom kernels
.. _jupyter-custom-kernel:

==========================
Custom Jupyter Kernel
==========================

This short howto explains how you can create and access your own custom Jupyter Kernel inside a CoCalc.
In case you require a specific software package, there are related guides: :doc:`install-python-lib` and  :doc:`install-r-package`.

Adding a Kernel to CoCalc Jupyter
=================================

Suppose you have a kernel from another source and you would like to add it to the list of Jupyter kernels that can be selected from CoCalc Jupyter. You will need to know the command line arguments needed to start the kernel. Then follow the steps here.

For your convenience, there is a link to these instructions at the bottom of both the :ref:`kernel selection menu <jupyter-kernel-menu>` and the :ref:`kernel selection dialog <jupyter-change-kernel-lg>`.

To accomplish this, we're working in a :doc:`../terminal`.
If you do not already have one, you can create a terminal in Files, as a "Terminal" file with the extension ``*.term``.

1. Get a list of the currently installed kernels as follows::

    /usr/local/share$ jupyter kernelspec list
    Available kernels:
      bash              /ext/jupyter/kernels/bash
      ir                /ext/jupyter/kernels/ir
      julia             /ext/jupyter/kernels/julia
      octave            /ext/jupyter/kernels/octave
      python2           /ext/jupyter/kernels/python2
      python3           /ext/jupyter/kernels/python3
      sagemath          /ext/jupyter/kernels/sagemath
      [...]

2. Copy one of the above over that is closest to the kernel you want to create into your project's ``~/.local/share/jupyter/kernels/<kernel_name>`` directory, e.g.,

::

    mkdir -p $HOME/.local/share/jupyter/kernels
    cp -arv /ext/jupyter/kernels/sagemath $HOME/.local/share/jupyter/kernels/sage_custom

3. Edit the ``kernel.json`` file copy of the kernel you made::

    cd $HOME/.local/share/jupyter/kernels/sage_custom
    open kernel.json


Make sure to change the name of the kernel, etc.  E.g., you might change ``kernel.json`` to::

    {
     "display_name": "sage_custom",
     "argv": [
         "/home/user/sage/sage",
         "--python",
         "-m",
         "sage.repl.ipython_kernel",
         "--matplotlib=inline",
         "-f",
         "{connection_file}"
     ]
    }


where ``/home/user/sage/sage`` points to your own Sage installation.
Note, ``$HOME`` should expand to ``/home/user``, which you can check by running ``echo $HOME``.

4. Now, run ``jupyter kernelspec list`` again to check that your kernel shows up in the list of all kernels.

5. Test your kernel in the terminal first to more easily see what is wrong (if anything)::

      jupyter console --kernel=sage_custom


An interactive IPython console should start up and you should be able to run Sage commands.

6. Once you have your kernel working in a terminal, test your kernel from a :doc:`Jupyter Notebook <../jupyter>`. To load an updated list of kernels, scroll down in the "Kernel" menu and select "Refresh kernel list". Your kernel should show up with the given ``display_name``!

Creating a new kernel for a Custom Python Version
=================================================

These instructions are for the special case in which you want to create a Jupyter kernel for a version of Python that is not already in CoCalc.

.. note::

    The following approach may not succeed with a pre-release version of Python.

The example below uses Python version 3.10.0. This version may already be available in CoCalc when you are reading these instructions. Substitute the actual version of Python you want added to the list of available CoCalc Jupyter kernels.

1. Get pyenv running `More details <https://github.com/pyenv/pyenv/blob/master/README.md#basic-github-checkout>`_::

    curl https://pyenv.run | bash

Add this to the bottom of your ``~/.bashrc`` or ``~/.bash_aliases``::

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"
    eval "$(pyenv init -)"


Restart the terminal via Ctrl-d. "pyenv versions" should then show you what you can install.

2. Install the desired version of Python::

    pyenv install 3.10.0
    pyenv virtualenv 3.10.0 py3.10
    pyenv virtualenvs # should include py3.10

3. Start the new virtual environment::

    pyenv activate py3.10
    python -V # displays 3.10.0

.. note::

    You won't have access to CoCalc's more than 1,000 pre-installed Python packages from the virtual environment. You'll need to ``pip install`` such packages as pandas and matplotlib. The ``--user`` flag is not needed with ``pip`` in the virtual environment.

4. Install ipykernel for Jupyter::

    pip install ipykernel
    python -m ipykernel install --user --name=py3.10 --display-name "Python 3.10"

After the above steps, when you open a Jupyter notebook, you may have to do "Refresh kernel list" at the bottom of the Kernel menu, or refresh the CoCalc tab. You will then see "Python 3.10" listed among the available kernels.

.. note::

    For a Python kernel, we suggest to add these parameters to the ``argv`` array:

    * ``"--HistoryManager.enabled=False"``: there is no need to record the history in a local database
    * ``"--matplotlib=inline"``: to automatically load matplotlib

