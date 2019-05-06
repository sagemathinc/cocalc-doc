.. index:: File too large
.. _file-too-large:

================================================
File Too Large
================================================

Here are notes on a two situations in which opening a file leads
to a the "file too large" error.

These errors can arise if you use CoCalc to open the file, i.e. if you do one of the following:

* Select the name of the file in :doc:`../project-files` list. 

* Select the filename in an entry in the :ref:`Project Activity Log <ft-history>`.

* Use the `open` command to open the file :ref:`from a terminal <terminal-file-open>`.

.. index:: File too large; Jupyter notebook

Jupyter Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may see the following warning when opening a Jupyter notebook:

.. figure:: img/ipynb-too-large.png
     :width: 60%
     :align: center

     Jupyter notebook *file too large* error

A possible cause for this is creating an image file from a plot that exceeds the size limit. The default image file format for plots with the "R (R Project)" Jupyter kernel is SVG. For large plots, smaller files may be produced if the format is set to PNG. To set image output format in an R Jupyter notebook to PNG, run the following in a compute cell before creating the plot::

    options(jupyter.plot_mimetypes = c('text/plain', 'image/png'))

.. index:: File too large; CSV file

CSV File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempting to open a CSV file over 5 MB in size results in the following error:

.. figure:: img/big-file.png
     :width: 60%
     :align: center

     CSV *file too large* error

In this case you can view the file with command-line tools like ``less``, or the `vim` editor, or view the file using `libreoffice`_ or the ``localc`` application in an  :ref:`x11 <x11_installed_applications>` terminal.


.. _libreoffice: https://www.libreoffice.org
