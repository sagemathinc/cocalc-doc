.. index:: Jupyter Notebooks; Classical vs CoCalc
.. _jupyter-classical-vs-cocalc:

==========================================
Classical Versus CoCalc Jupyter Notebooks
==========================================

These enhanced features are available in CoCalc Jupyter notebooks:

.. contents::
     :local:
     :depth: 1

#######################
Classical versus CoCalc
#######################

If you are having trouble with the `CoCalc Jupyter Notebook`_, you can switch to the Classical Jupyter Notebook.
You can always switch back to CoCalc Jupyter easily later (and please let us know what is missing so we can add it!).

*NOTE: The Classical Jupyter notebook is not supported in the Firefox browser. See Jupyter Server options below if you need to use Firefox and do not want to use the CoCalc Jupyter notebook.*

You can change the default for opening a Jupyter notebook - CoCalc or Classical - by clicking the checkbox labeled "Jupyter classic ..." in your :ref:`Editor settings in Account Preferences <ed-settings-jupyter>`.

To switch your notebook to Classical from within a CoCalc Jupyter notebook: select "File" → "Switch to Classical Notebook" in the menu.

.. figure:: img/jupyter/switch-to-classical.png
     :width: 100%
     :align: center
     :alt: switch from CoCalc to Classical notebook

     switching to Classical from CoCalc Jupyter notebook

To switch your notebook to CoCalc from within a Classical Jupyter notebook: select "File" → "Switch to Classical Notebook" in the menu.

.. figure:: img/jupyter/switch-to-cocalc.png
     :width: 100%
     :align: center
     :alt: switch from Classical to CoCalc notebook

     switching to CoCalc from Classical Jupyter notebook

.. role:: strike

The main reasons to use the classical notebook are:
  - need for certain extensions (:ref:`Howto setup Jupyter Extensions <jupyter-extensions>`).
  - :strike:`interactive widget support` *Note: as of April, 2019, CoCalc Jupyter notebooks support ipywidgets.*

See our `list of Jupyter related issues <https://github.com/sagemathinc/cocalc/issues?q=is%3Aissue+is%3Aopen+label%3AA-jupyter>`_ for more details.

*************************************
Collaboration with Classical Jupyter
*************************************

Here's a pro tip if you need a classical Jupyter notebook for one of the reasons above and want real-time collaboration as well.
If you and another user both select "Jupyter classic" in :ref:`Account / Preferences / Editor <ed-settings-jupyter>`,
then open the ipynb file in cocalc as you normally would, multiple users are supported.

Multiple users are NOT supported with the :ref:`Plain Jupyter Classic Server <plain-jupyter-server>` and :ref:`JupyterLab Server <jupyterlab-server>` activated under Project settings.
Multiple users ARE supported with classical Jupyter embedded as a normal editor within CoCalc, which is what you get when you enable "Jupyter classic" as in the preceding paragraph.

Basically, we fully implemented two very different approaches to realtime collaboration for Jupyter.

.. _dont-mix-warning:

*******************************
Don't mix CoCalc and Classical!
*******************************

.. warning::

    Multiple people simultaneously editing the same notebook,
    with some using classical and some using the new mode, will NOT work!
    Switching back and forth **will** cause problems (you may need to use TimeTravel to recover).
    *Please avoid using classical notebook mode if you possibly can!*

.. index:: Jupyter Server; alternatives
.. _jupyter-server-alternatives:

********************************************************
Alternatives: Plain Jupyter Server and JupyterLab Server
********************************************************

You can also run the full classical Jupyter notebook server, using either **Plain Jupyter Server** or **JupyterHub Server**. These options are available under
:ref:`Project settings <alt-jupyter-server>` and :ref:`(+) New <plusnew>`.

Using either of these options for the classical notebook has an advantage: it does not affect your "Jupyter classic" Editor setting, allowing you to keep CoCalc Jupyter notebook as the default for opening .ipynb files in the CoCalc main interface.

Note that the same :ref:`warning <dont-mix-warning>` applies as above: you shouldn't open the same ipynb file in cocalc and in classical/lab servers.

.. _Cocalc Jupyter Notebook: http://blog.sagemath.com/jupyter/2017/05/05/jupyter-rewrite-for-smc.html


