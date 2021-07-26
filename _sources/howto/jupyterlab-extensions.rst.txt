.. index:: Jupyter Server; JupyterLab extensions

=============================
JupyterLab Extensions
=============================

JupyterLab allows the use of `extensions <https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#extensions>`_, such as notebook `table of contents <https://github.com/jupyterlab/jupyterlab-toc>`_ and `rendering of custom data formats <https://github.com/jupyterlab/jupyter-renderers>`_ such as `FASTA <https://en.wikipedia.org/wiki/FASTA_format>`_.

Here's how to get started with JupyterLab extensions:


Prepare your project
=====================


* Make sure you have enough memory. You'll need at least 2 GB of RAM in your project to build JupyterLab extensions, possibly more depending on the extension. See :ref:`Adjust Quotas <apply_project-upgrades>` for more information on how to add upgrades.

* Configure a directory to store the installed extensions. In this example, we use ``.lab`` in the project home directory. In :ref:`Custom environment variables <project-env-vars>` in project settings, set environment variable ``JUPYTERLAB_DIR`` to the value ``/home/user/.lab``.

.. figure:: img/jlab-env.png
     :width: 70%
     :align: center

     ..


Click Save to store the variable setting, and **restart your project.**


Build the extensions
====================

After restarting your project, open a :doc:`Linux Terminal <../terminal>` and run the following:

.. code-block:: bash

    # check that JUPYTERLAB_DIR variable is set to `/home/user/.lab`
    echo $JUPYTERLAB_DIR
    
    # install extension(s) - this step takes a couple minutes
    jupyter labextension install @jupyterlab/toc @jupyterlab/fasta-extension


Start JupyterLab
================

In the "Project settings", scroll down to find :ref:`jupyterlab-server`. A moment after you click that link, JupyterLab starts up.

At this point, your extensions are installed and enabled.

.. figure:: img/jlab-ext-example.png
     :width: 90%
     :align: center

     ..


