.. index:: Frame Editor

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


.. index:: Markdown; frame editor
.. index:: Frame Editor; markdown

Markdown
-----------

If you open/create a file ending with ``*.md``, you're presented by default with a split view of `Markdown <https://www.markdowntutorial.com/>`_ code on the left and HTML rendered output on the right hand side.
You can also write `LaTeX formulas <https://en.wikibooks.org/wiki/LaTeX/Mathematics>`_ between ``$`` signs, e.g. ``$\frac{1}{1+x^2}$``.

.. index:: Frame Editor; markdown inverse search

The markdown editor supports **inverse search** when source and rendered views are both visible (this is the default display for markdown files). If you double-click on markdown in the rendered view, the source view will scroll to display the corresponding line.

.. index:: Source Code files
.. index:: Frame Editor; source code

Plaintext / Source Code
--------------------------

A file ending in ``*.txt`` is a plaintext file, which does not have any formatting.
Similarly, you can also edit plaintext files with a special purpose, e.g. ``*.csv`` for CSV data,
``*.yaml`` for structured data, and for source-code of software programs, there is
``*.c``, ``*.c++``, ``*.sage``, ``*.java``, ``*.py``, ``*.adb`` and many more!

.. index:: HTML; frame editor
.. index:: Frame Editor; HTML
.. _edit-html:

HTML
-----

Open/create a ``*.html`` file and you'll see the rendered output on the right hand side. You can switch the rendered view between "Preview" (which is faster) or "iframe" (which renderes the page as it is) depending on your needs. You can even close the editor pane, to just see the rendered HTML.

.. index:: RMarkdown; frame editor
.. index:: Frame Editor; RMarkdown
.. _edit-rmd:

RMarkdown
----------------

Open a ``*.rmd`` file to work with `RMarkdown`_.
Depending on the configuration in the preamble, you either produce an HTML or PDF output.
Do not forget to switch the panel for the rendered output accordingly.
(In case you produce PDF and HTML output, you can even see both after splitting the panel.)

.. _RMarkdown: https://rmarkdown.rstudio.com/

LaTeX
--------

See :doc:`latex`.

Text
-----------

.. index:: Frame Editor; multiple cursors
.. index:: Text; frame editor
.. index:: Frame Editor; text files

Multiple Cursors
=======================

You can get multiple cursors while editing any file in the frame editor using the mouse and ctrl+click (cmd+click on Mac).

If you switch to Sublime keybindings in "Account" > "Preferences" > "Editor settings", you can select text and then use ctrl-D (cmd-D on Mac) to multi-select the next occurrence of the same text.

