.. index:: File too large
.. _file-too-large:

================================================
File Too Large
================================================

.. contents::
   :local:
   :depth: 1

Here are suggestions for what to do if you get a file-too-large error when :ref:`opening a file <ft-open-files>` in CoCalc.

.. index:: File too large; Jupyter notebook
.. _howto-ipynb-too-large:

Jupyter Notebook Too Large
==========================

If you receive the error message ``Fatal Error loading ipynb file`` with text saying your file is too large, your notebook has probably created too much output. The :ref:`Notebook too large? <jupyter-ipynb-too-large>` section of this manual has suggestions what to do.

.. index:: File too large; HTML file
.. _howto-html-too-large:

HTML or Text File
=================

An HTML or text file larger than 5 MB can't be edited with the CoCalc :doc:`../frame-editor`.

Here is a workaround to view a large .html or .txt file in a CoCalc project in your browser.

#. In the file listing, click the checkbox to the left of the file.
#. Click the "Download" button at the top.
#. Click on the link that you see.

If you want to edit the file, you can open a :doc:`../terminal` and use one of the Linux editing utilities, such as "vi" or "emacs".

.. index:: File too large; CSV file
.. _howto-csv-too-large:

CSV File
==========

Attempting to open a CSV file over 5 MB in size results in the following error:

.. figure:: img/big-file.png
     :width: 60%
     :align: center

     CSV *file too large* error

In this case you can view the file with command-line tools like ``less``, or the `vim` editor, or view the file using `libreoffice`_ or the ``localc`` application in an  :ref:`x11 <x11_installed_applications>` terminal.


.. _libreoffice: https://www.libreoffice.org
