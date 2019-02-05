.. :index: Custom Jupyter Kernel

==========================
Custom Jupyter Kernel
==========================

This short howto explains how you can create and access your own custom Jupyter Kernel inside a CoCalc.

To accomplish this, we're working in a :doc:`../terminal`.
If you do not already have one, you can create a terminal in Files, as a "Terminal" file with the extension ``*.term``.

1. Get a list of the currently installed kernels as follows::

    /usr/local/share$ jupyter kernelspec list
    Available kernels:
      anaconda3         /ext/jupyter/kernels/anaconda3
      bash              /ext/jupyter/kernels/bash
      calysto_prolog    /ext/jupyter/kernels/calysto_prolog
      gap               /ext/jupyter/kernels/gap
      ir                /ext/jupyter/kernels/ir
      ir-sage           /ext/jupyter/kernels/ir-sage
      julia             /ext/jupyter/kernels/julia
      octave            /ext/jupyter/kernels/octave
      pari_jupyter      /ext/jupyter/kernels/pari_jupyter
      postgres          /ext/jupyter/kernels/postgres
      python2           /ext/jupyter/kernels/python2
      python2-ubuntu    /ext/jupyter/kernels/python2-ubuntu
      python3           /ext/jupyter/kernels/python3
      sage-8.0          /ext/jupyter/kernels/sage-8.0
      sage-8.1          /ext/jupyter/kernels/sage-8.1
      sage-develop      /ext/jupyter/kernels/sage-develop
      sagemath          /ext/jupyter/kernels/sagemath
      scala211          /ext/jupyter/kernels/scala211
      singular          /ext/jupyter/kernels/singular
      vpython           /ext/jupyter/kernels/vpython

2. Copy one of the above over that is closest to the kernel you want to create into your project's ``~/.local/share/jupyter/kernels/<kernel_name>`` directory, e.g.,

::

    mkdir -p $HOME/.local/share/jupyter/kernels
    cp -arv /ext/jupyter/kernels/sage-8.1 $HOME/.local/share/jupyter/kernels/sage_custom

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
