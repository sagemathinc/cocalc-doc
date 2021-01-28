.. index:: Jupyter Notebooks; custom kernels
.. _jupyter-custom-kernel:

==========================
Custom Jupyter Kernel
==========================

This short howto explains how you can create and access your own custom Jupyter Kernel inside a CoCalc.
In case you require a specific software package, there are related guides: :doc:`install-python-lib` and  :doc:`install-r-package`.

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
     "argv": ["/home/user/sage/sage", "--python", "-m", "sage.repl.ipython_kernel", "--matplotlib=inline", "-f", "{connection_file}"]
    }


where ``/home/user/sage/sage`` points to your own Sage installation.
Note, ``$HOME`` should expand to ``/home/user``, which you can check by running ``echo $HOME``.

4. Now, run ``jupyter kernelspec list`` again to check that your kernel shows up in the list of all kernels.

5. Test your kernel in the terminal first to more easily see what is wrong (if anything)::

      jupyter console --kernel=sage_custom


An interactive IPython console should start up and you should be able to run Sage commands.

6. Once you have your kernel working in a terminal, test your kernel from a :doc:`Jupyter Notebook <../jupyter>`. To load an updated list of kernels, scroll down in the "Kernel" menu and select "Refresh kernel list". Your kernel should show up with the given ``display_name``!

