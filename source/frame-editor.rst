============
Frame Editor
============

This guide explains how to work with the **frame editor** for editing source code, :doc:`LaTeX documents <latex>`, :doc:`Command-line terminal <terminal>` etc. The screenshot below shows a Python file and a Terminal. In order to get that view, the frame editor is split vertically first, and then the right frame is splitted horizontally. After that, the bottom right frame is changed to a :doc:`Terminal <terminal>`.

Therefore, you can not only view the same Python source code file in two places, but you can also work with e.g. IPython_ on the command-line in the same directory.

.. _IPython: https://www.ipython.org

.. image:: img/frame-editor-python.png
    :width: 100%

Supported file types
=======================

.. index:: HTML editor
.. _edit-html:

HTML
-----

Open a ``*.html`` file and you'll see the rendered output on the right hand side. You can switch the rendered view between "Preview" (which is faster) or "iframe" (which renderes the page as it is) depending on your needs. You can even close the editor pane, to just see the rendered HTML.

.. index:: RMarkdown
.. _edit-rmd:

RMarkdown
---------------

Open a ``*.rmd`` file to work with `RMarkdown`_.
Depending on the configuration in the preamble, you either produce an HTML or PDF output.
Do not forget to switch the panel for the rendered output accordingly.
(In case you produce PDF and HTML output, you can even see both after splitting the panel.)

.. _RMarkdown: https://rmarkdown.rstudio.com/

LaTeX
--------

See :doc:`latex`.

