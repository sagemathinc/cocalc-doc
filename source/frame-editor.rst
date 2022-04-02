.. index:: Frame Editor

.. _frame-editor:

============
Frame Editor
============

.. contents::
     :local:
     :depth: 2

This guide explains how to work with the **frame editor** for editing source code, :doc:`LaTeX documents <latex>`, :doc:`Command-line terminal <terminal>` etc. The screenshot below shows a Python file and a Terminal. In order to get that view, the frame editor is split vertically first, and then the right frame is splitted horizontally. After that, the bottom right frame is changed to a :doc:`Terminal <terminal>`.

Therefore, you can not only view the same Python source code file in two places, but you can also work with e.g. IPython_ on the command-line in the same directory.

.. _IPython: https://www.ipython.org

.. image:: img/frame-editor-python.png
    :width: 100%
    :alt: split screen with two views of source file plus terminal running ipython

#####################
Supported file types
#####################


.. index:: Markdown; frame editor
.. index:: Frame Editor; markdown

.. _frame-editor-markdown:

********
Markdown
********

If you open/create a file ending with ``*.md``, you're presented by default with a split view of `Markdown <https://www.markdowntutorial.com/>`_ code on the left and HTML rendered output on the right hand side.

There's an entire page in this guide dedicated to :doc:`markdown`.



.. index:: Source Code files
.. index:: Frame Editor; source code

***************************
Text and Other File Types
***************************

The frame editor lets you edit text files, i.e. files whose name ends in ``*.txt``.

You can also use it to edit source code in many programming languages, including file types ``*.c``, ``*.c++``, ``*.sage``, ``*.java``, ``*.py``, and ``*.adb``.

And you can use the frame editor to edit common data formats, including ``*.csv``, ``*.yaml``, and ``.json``.

.. index:: HTML; frame editor
.. index:: Frame Editor; HTML
.. _edit-html:

******
HTML
******

Open/create a ``*.html`` file and you'll see the rendered output on the right hand side. You can switch the rendered view between "Preview" (which is faster) or "iframe" (which renderes the page as it is) depending on your needs. You can even close the editor pane, to just see the rendered HTML.

.. index:: RMarkdown; frame editor
.. index:: Frame Editor; RMarkdown
.. _edit-rmd:

***********
R Markdown
***********

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

********
LaTeX
********

See :doc:`latex`.

.. index:: Frame Editor; multiple cursors
.. index:: Text; frame editor
.. index:: Frame Editor; text files

################
Multiple Cursors
################

You can get multiple cursors while editing any file in the frame editor using the mouse and ctrl+click (cmd+click on Mac).

If you switch to Sublime keybindings in "Account" > "Preferences" > "Editor settings", you can select text and then use ctrl-D (cmd-D on Mac) to multi-select the next occurrence of the same text.

The frame editor also supports simultaneous editing by more than one user. In this case, separate cursors are displayed for each user.


################
Spell Checker
################

Here are two ways to spell-check your documents in CoCalc.

**Use your browser's native spell checker.**

The CoCalc frame editor supports the browser's native spell checker for varying file types, including ``.md``, ``.rmd``, and ``.html``. See the documentation for your specific browser for information on how to enable and configure spell checking. You may have to save your file before the spell checker is activated.


.. _use-aspell:

**Use the ``aspell`` Linux command.**

The ``aspell`` utility will find possible misspellings and offer corrections. Here's how to use it:

    1. Open a :doc:`./terminal`
    2. ``aspell -t -c <filename.tex>``

You can add words for ``aspell`` to ignore using `personal dictionaries <http://aspell.net/man-html/Format-of-the-Personal-and-Replacement-Dictionaries.html#Format-of-the-Personal-and-Replacement-Dictionaries>`_. These words won't be underlined red. To do this create the file ``~/.aspell.lang.pws``, where ``lang`` is the choice of langauge. The first line of this file should be ``personal_ws-1.1 lang 0``, where ``lang`` is the choice of language. Then add one word per line for ``aspell`` to ignore. For example, to ignore the words 'bijection' and 'surjection' in an English document, create the file ``~/.aspell.en.pws`` with the content::

   personal_ws-1.1 en 0
   bijection
   surjection

The changes will take place the next time ``aspell`` is run on the document. 

################
Side Chat
################

You can share comments on a CoCalc file using a side chat panel. For more information, see :ref:`side-chat`.
