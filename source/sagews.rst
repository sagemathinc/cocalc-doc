.. index:: Sage Worksheet
.. _sage-worksheet:


===============
Sage Worksheets
===============

Sage Worksheets were developed for collaborative, notebook-style computing with `SageMath <https://www.sagemath.org>`_ on the `CoCalc <https://cocalc.com>`_ platform. Like Jupyter Notebooks, Sage Worksheets support many programming environments, including Python 3, R, and the Bash shell. More than one language environment can be used in the same Sage Worksheet.

.. warning::

    This page is work in progress

.. contents::
   :local:
   :depth: 2

What's a Sage Worksheet?
==============================

A Sage Worksheet is a file ending in ``.sagews`` and is subdivided into cells. Each cell has an input region and an output region, which might be 0, 1, 2, or many lines long. The input can be mathematical, in the Sage syntax, or it could be in many other formats, including `Markdown <https://daringfireball.net/projects/markdown/syntax>`_, HTML, Python 2 or 3, R, and so forth.

When you *run* a cell, by clicking ``Run`` or typing ``Shift-Enter``, the input is executed (or formatted, for text processing). The result appears in the output after the calculation is done.

To begin work on a Sage Worksheet, create a file ending with ``*.sagews``.

.. figure:: img/sagews/sagews-example.png
     :width: 90%
     :align: center

     *Example of a Sage Worksheet*


Wiki resources
==================

Sage Worksheets
-------------------

* `Sage Worksheet UI and Help <https://github.com/sagemathinc/cocalc/wiki/sagews>`_
* `Custom "Mode Commands" in Sage Worksheets <https://github.com/sagemathinc/cocalc/wiki/sagews-custom-modes>`_


Conversion utilities
----------------------

* There are buttons in the UI to convert to PDF, a print-button or a Jupyter Notebook
* `SageWS to HTML <https://github.com/sagemathinc/cocalc/wiki/sagews2html>`_ (including a utility to extract the sagews file from a generated HTML file)
* Run ``smc-sagews2pdf --help`` in a :doc:`./terminal` for more information about converting to PDF
* Similarly, ``smc-sagews2ipynb`` is a command-line utility to convert to ``*.ipynb``.

SageMath specific
====================

Items relating strictly to SageMath, whether or not you are using CoCalc.

* **Quickstart:** read the `documentation <https://doc.sagemath.org/html/en/>`_, in particular the `Tutorial <https://doc.sagemath.org/html/en/tutorial/index.html>`_.
* `The Top Mathematical Syntax Errors in Sage <https://github.com/sagemathinc/cocalc/wiki/MathematicalSyntaxErrors>`_
* :ref:`Questions about Sage <sage-question>` -- how to get help working with Sage.
* `Sage Bugreport <https://github.com/sagemathinc/cocalc/wiki/SageBug>`_ -- I am using Sage and think I have found a bug

Howto
==================


.. index:: Attach Sage files
.. _attach-sage-files:

Attach Sage files to Sage Worksheets
---------------------------------------------------------------

**Is there a way to write functions in one worksheet, and then important them to another and use them there?**

Not exactly, but you can write code in a ``.sage`` file and then load it into another Sage Worksheet as illustrated at
https://cocalc.com/share/4a5f0542-5873-4eed-a85c-a18c706e8bcd/support/2018-06-12-sage-code/?viewer=share

#. Put code in a new file with extension ``.sage``, e.g. ``code.sage``
#. In a Sage worksheet or the terminal, run this: ``%attach code.sage`` or ``attach("code.sage")``
#. Now all code in ``code.sage`` is available in your worksheet, and whenever it changes, it will get reloaded automatically.
#. If you're using Jupyter, this is all broken (see https://github.com/sagemathinc/cocalc/issues/2916), but at least you can use ``load("code.sage")`` instead.



How can I connect an HTML form with my Python code?
---------------------------------------------------------------

.. note::

    The following explanation might be outdated!

To create a connection between your HTML form in a .sagews file created using HTML, CSS and JS, you need to use the ``worksheet.execute_code()`` function in your JS code.

Because ``worksheet.execute_code` isn't a standard JS function, but special CoCalc function, you need to load your JS code with ``worksheet.execute_code()``.  In particular do NOT use

::

    load('path/to/js/code.js')

but instead use

::

    salvus.javascript(open('path/to/js/code.js').read())

For example in a ``.sagews`` file suppose you created a div with ``id='myApp'`` as follows::

    %html
    <div id='myApp'>
    ....
        <div id="msgLog"></div>
        <div id="msgErr"></div>
    </div>

Let's say your Python function will double ``x``::

    def myfunc(x):
        print(x*2)

In your JS code type::

    worksheet.execute_code({
        code: 'myfunc(n)',
        data: {n: 2},
        preparse: true,
        cb: function(msg){
                if(msg.stdout){$('#myApp #msgLog').html(msg.stdout);}
                if(msg.stderr){$('#myApp #msgErr').html(msg.stderr);}
        }
    });

Please note that ``myfunc()`` doesn't ``return`` anything.
On the contrary, it uses ``print()`` to send output. This is because JS and python are different languages, and you can't just use ``return`` in your Python function to return some answer. ``stdout`` in JS code means standard output stream.
That is, the ``print`` function in your Python code places the result of ``myfunc()`` in the output stream.
That's why you need to use ``print()`` but not ``return()`` in your Python code.

Also, if your Python code will raise some exception,
then it will result in output to ``stderr`` the standard error stream.
If you JS code (as in the example above) catches stderr,
you can get any error message from your Python code.
