.. index:: Jupyter Notebooks; extensions
.. _jupyter-extensions:

=============================
Setup Jupyter Extensions
=============================

Besides :doc:`CoCalc's own implementation <../jupyter>` of the `Jupyter Notebook <https://jupyter.org>`_, there is also the possibility of running the Classical Server or Jupyter Lab inside your project.

.. seealso::

    Please read about various pros/cons and warnings regarding :ref:`jupyter-classical-vs-cocalc` notebooks.

Setup
=============

To enable an extension for your project you have to

1. Install the extension library for Python 3 (using ``pip3``)
2. Install the extension for Jupyter
3. Enable it

The documentation of the extension you want to install might explain this in more detail.

.. note::

    In essence, you have to replace switches like ``--system`` (which are for global installations)
    with ``--user`` (which are for installing in your user account, which is equivalent to a project).

For example, here are the steps to install `contributed notebook extensions <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/>`_ and enable `equation numbering <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/equation-numbering/readme.html>`_.
To issue these commands, first open up a :doc:`../terminal`. Then run::

    pip3 install --user jupyter_contrib_nbextensions
    jupyter contrib nbextension install --user
    jupyter nbextensions_configurator enable --user
    jupyter nbextension enable equation-numbering/main

Related: :doc:`install-python-lib` and  :doc:`install-r-package`