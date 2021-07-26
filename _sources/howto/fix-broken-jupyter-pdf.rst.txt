
=====================================
Fix broken Jupyter PDF export
=====================================

:doc:`Jupyter Notebooks <../jupyter>` allow to export the given file as a static PDF (in the "File" menu).
There is just one problem, though: **Sometimes it fails to generate the desired PDF document!**

The overall process at play is that in the first step, the notebook is translated to [LaTeX]_, a typesetting language. It is famous for supporting mathematical formulas and producing high-quality output, but it is also a *programming language* and therefore inherits all its "problems" like `syntax errors`_ and so on.

.. _syntax errors: https://en.wikipedia.org/wiki/Syntax_error

If there are problematic commands in LaTeX, processing the document stops and you end up with a partial result or no PDF at all. This could even break silently and leaves you puzzled about what's going on.

**To fix this, convert the document to LaTeX instead**, which is essentially a text file ending with ``*.tex``. To accomplish this, select the LaTeX export in the Jupyter Notebook's file menu, right above the PDF export. Then either click the button to open end edit it, or click on the generated ``*.tex`` file to open it up in :doc:`CoCalc's LaTeX editor <../latex>`.


That editor will attempt to compile it and will quickly point out one or more errors. It lists them in order to direct you to the line where the problems are. For example, let's assume there is a line like this::

    \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}

This will be reported as a missing dollar sign (``$``) error, because in the Jupyter Notebook's Markdown cells such formulas do not need to be wrapped inside of them – proper LaTeX requires that, though. To continue that example, changing the line to

::

    $$\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$

makes LaTeX happy and the document compiles fine to the PDF file.

