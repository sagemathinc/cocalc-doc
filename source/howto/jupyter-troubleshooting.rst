Jupyter Notebooks
=================

.. index:: Jupyter Notebooks; notebook too large
.. _jupyter-ipynb-too-large:

Notebook Too Large - Remove Output
----------------------------------

If the size of your notebook exceeds 50 MB, you will not be able to open it in the usual way. Instead, you will see an error message. Usually, the problem occurs when the notebook has created large amounts of output. In that case, there is a command you can run from the :doc:`Linux Terminal </terminal>` to remove output. If removing output results in a small enough notebook, you will be able to open the ``-no-output`` version of the notebook normally.

.. code-block:: bash

    # run this from a CoCalc Linux terminal (.term file)
    # use the actual name of your notebook for "myfile.ipynb"
    cc-jupyter-no-output myfile.ipynb
    # the above command creates myfile-no-output.ipynb

If your Jupyter notebook is creating an image file from a plot that exceeds the size limit, here are some things you can do:

1. If you are using a CoCalc Jupyter notebook (which we generally recommend), it may be possible to open the notebook with :ref:`jupyterlab-server`. Once you have the file open, you can modify the code to produce a smaller plot. Then you can go back to using the CoCalc notebook.

2. Revert the notebook to an earlier version, before the large plot was created. Click the :ref:`Backups button <project-snapshot>` in the file listing and copy over an earlier version, then modify your code to produce a smaller plot.

3. The default image file format for plots with the "R (R Project)" Jupyter kernel is SVG. For large plots, smaller files may be produced if the format is set to PNG, because SVG plots (the default) grow in size proportionally to the data they are supposed to show, wherease PNG plots are rasterized, so file size does not have the same proportionality relationship to amount of data. To set image output format in an R Jupyter notebook to PNG, run the following in a compute cell before creating the plot::

    options(jupyter.plot_mimetypes = c('text/plain', 'image/png'))


.. index:: Jupyter Notebooks; remove local files

Remove Local Files
------------------

If you have a Jupyter Notebook that suddenly stops working, especially with extensions or widgets, you can try removing local files in a :doc:`Linux Terminal </terminal>`, then restarting and running the notebook::

    cd
    rm -rf .sage .ipython/ .config/ .local/ .jupyter .cache/

You will need to reinstall packages you added locally after doing the above.


.. index:: pair: Jupyter Notebooks; shutdown kernel
.. _jupyter-halt:

Shutdown Kernel
---------------

Each running Jupyter Notebook uses up memory, which could cause troubles if you run multiple notebooks during one session.
If you have finished working on a particular notebook, you may click ``Kernel > Shutdown kernel...`` in the menu to stop the kernel, free up memory, and close the notebook.