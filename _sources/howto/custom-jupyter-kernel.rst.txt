.. index:: Jupyter Notebooks; custom kernels
.. _jupyter-custom-kernel:

==========================
Custom Jupyter Kernel
==========================

This short howto explains how you can create and access your own custom Jupyter Kernel inside a CoCalc.
In case you require a specific software package, there are related guides: :doc:`install-python-lib` and  :doc:`install-r-package`.

.. _install-custom-python-env-kernel:

Adding a kernel for a Custom Python Environment
=================================================

These instructions are for the case in which you want to create a Jupyter kernel for Python environment inside your CoCalc project.

1. If you haven't already, create your own Python environment:

- Python via `venv`_ (for demo purposes, we install an old version of NumPy)::

    ~$ mkdir myenv
    ~$ cd myenv/
    ~/myenv$ python -m venv .
    ~/myenv$ . bin/activate
    (myenv) ~/myenv$ pip install ipykernel 'numpy<2'

    # quick check:

    (myenv) ~/myenv$ python
    Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy as np
    >>> np.__version__
    '1.26.4'

- Anaconda (make sure to also install ``ipykernel`` via the environment.yml configuration)::

    ~$ anaconda2023
    (base) ~$ mamba env create --prefix ~/myenv --file=environment.yml
    (base) ~$ conda activate ~/myenv
    (/home/user/myenv) ~$ python
    [...]

.. note::

  You can automatically activate your Python environment by configuring a :ref:`terminal-startup-files`
  in a :ref:`terminal`, and calling the ``source ~/myenv/bin/activate`` command.

  Then test it by restarting the shell via Ctrl-d.

  You can also make this permanent to all terminals by adding this to the bottom of your ``~/.bashrc``

2. Install the Jupyter Kernel:


- Python via pip::

    (myenv) ~/myenv$ pip install ipykernel
    (myenv) ~/myenv$ python -m ipykernel install --user --name=myenv --display-name "My Python Environment"

    # quick check:
    (myenv) ~/myenv$ jupyter kernelspec list | grep myenv
      myenv               /home/user/.local/share/jupyter/kernels/myenv

- Anaconda::

    (/home/user/myenv) ~$ python -m ipykernel install --user --name myenv --display-name "My Python Environment"

After the above steps, when you open a Jupyter notebook, you may have to do "Refresh kernel list" at the bottom of the Kernel menu, or refresh the CoCalc tab. You will then see "My Python Environment" listed among the available kernels.


Manually adding a Jupyter Kernel
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


.. note::

    For a Python kernel, we suggest to add these parameters to the ``argv`` array:

    * ``"--HistoryManager.enabled=False"``: there is no need to record the history in a local database
    * ``"--matplotlib=inline"``: to automatically load matplotlib


..  _venv: https://docs.python.org/3/library/venv.html