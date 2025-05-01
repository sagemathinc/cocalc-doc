R IDE
=====

.. admonition:: DISCLAIMER

    R IDE in CoCalc is the open source edition of RStudio. Posit Software, PBC is in no way associated with CoCalc.
    
There are a number of ways to use R in CoCalc.


Collaborative X11 Application
-----------------------------
You can create :doc:`x11`, then click **R IDE** in the application list at the bottom left and wait about 20 seconds. The advantage is real-time collaboration just as with any other X11 application, but the response time may be slow.


Notebook Server
---------------

Click on the **Servers / Notebook Servers** tab and launch **R IDE** :

.. figure:: img/R_IDE_server.png
    :width: 90%
    :align: center
    :alt: Launching R IDE Server

    Launching R IDE Server

.. raw:: html

    <center><iframe
        width="640" height="360"
        src="https://www.youtube.com/embed/Hl9MnHfuwCQ?si=JdM8eQb5T5pBKM1u"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe></center>
    
    
Compute Server
--------------

If you need more powerful compute resources, use :doc:`compute_server` with **R Statistics** image. Here CoCalc's CEO and Founder William Stein explains how to run it:

.. raw:: html

    <center><iframe width="640" height="360" src="https://www.youtube.com/embed/Owq90O0vLJo?si=Im_EpK-uJwSkJSSW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>
    <br/>


.. _edit-rmd:

R Markdown
----------

Open a ``*.Rmd`` or ``*.rmd`` file to work with `R Markdown`_.
Depending on the configuration in the preamble, you either produce an HTML or PDF output.
Do not forget to switch the panel for the rendered output accordingly. Here is an example of R markdown producing a pdf file:

.. image:: img/rmd-pdf-example.png
    :width: 100%
    :alt: example of R markdown producing a pdf file

If you produce PDF and HTML output, you can see both after splitting the panel.

There is a brief tutorial on R Markdown in the :doc:`project-library`. To view the sample files, do the following:

#. Open a project where you want the copied files to be placed.
#. Open the Files tab.
#. Click "Library" at upper right.
#. Select "RMarkdown in CoCalc".
#. Click "Get a copy".

.. image:: img/r-markdown-library.png
    :width: 100%
    :alt: fetching R Markdown intro from the project library

.. _R Markdown: https://rmarkdown.rstudio.com/

Other Ways
----------

You can also use R in CoCalc via:

- Jupyter notebooks with the R kernel. See :ref:`jupyter-kernels`.
- Creating a file ending in .r and running it. You can keep your source file in one pane with a Linux terminal beside it to run the program. See :ref:`terminal-editor-panel`.
- :ref:`latex-knitr` (rnw or Rtex file).
- Sage worksheet with R (sagews file and "%r" mode). See Custom “Mode Commands” in Sage Worksheets under :ref:`sagews-wiki`.

