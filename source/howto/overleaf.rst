.. index:: Overleaf

======================================
Import from Overleaf
======================================

This little guide explains how to export LaTeX files from `Overleaf`_
and import them into a CoCalc project.

.. _Overleaf: https://www.overleaf.com

Step 1: Export
======================

In the project overview, select one or more LaTeX projects you want to export. Then, click on the **Download** button:

.. image:: img/overleaf-export.png
    :width: 75%
    :align: center
    :alt: export from overleaf


Step 2: Import
=======================

In your CoCalc project, open the File Explorer where you would like to upload the LaTeX files.
Select `Upload` at the upper right of the file listing
and use the file picker to upload the zip file you downloaded in the previous step.

.. image:: img/latex-upload.png
    :width: 100%
    :align: center
    :alt: upload to CoCalc

To extract the files from the Zip archive, click on it and then the  **Extract Files** button.
A folder will be created with the name of the zipfile without the .zip extension.
Your files will be extracted into that folder.
In case you've exported several projects, they'll extract as individual zip files.
Just click on them again to extract the actual files.

.. image:: img/latex-unzip.png
    :width: 50%
    :align: center
    :alt: extracting files from zip archive

**Congratulations!**
Now you are ready to edit your LaTeX files in CoCalc!
Click on the ``*.tex`` file and the integrated :doc:`LaTeX Editor <../latex>` opens up for you.

If you have any problem compiling your files (maybe CoCalc is missing something that is installed in Overleaf), please don't hesitate to click the Help button with your LaTeX file open, and create a support request.


