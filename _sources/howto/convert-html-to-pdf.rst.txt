.. index:: Convert HTML to PDF
.. _html2pdf:

=========================
Convert HTML to PDF
=========================

There are various ways to convert an HTML file you have to a PDF. One that is supported on CoCalc uses the Chrome browser directly::

    chromium-browser --headless --disable-gpu --no-sandbox --run-all-compositor-stages-before-draw --print-to-pdf="output.pdf" "input.html"


Open a :doc:`../terminal` to run it.
You have to replace ``input.html`` by the HTML file and ``output.pdf`` by the name of the PDF file how you want to call it.
Note, that you need to be in the same directory as the files – otherwise use ``cd`` to switch there or prefix the filenames with the corresponding paths.

PS: for Jupyter Notebooks, there are two export to PDF functionalities. They're in the "File" menu and either use this command under the hood or first convert to LaTeX and then render it.