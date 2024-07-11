.. index:: Turtle graphics

===========================
Turtle Graphics with CoCalc
===========================

There are several ways to use turtle graphics with CoCalc.

.. contents::
   :local:
   :depth: 1

.. index:: Turtle graphics; Sage worksheet

Sage worksheet with Turtle module
=================================

Here is a `Sage worksheet on the CoCalc share server <https://cocalc.com/share/public_paths/75c54b5a2f56cdfeba825a4411325137f5c1502d>`_ using Turtle.
In the Sage worksheet, code and turtle graphics output are visible in the same tab.

.. figure:: img/turtle-spirals.png
     :width: 40%
     :align: center
     :alt: Sage worksheet source code for Turtle spirals

     Turtle spirals in the example Sage worksheet

To copy the example into a project of your own, do the following:

#. Sign into CoCalc.
#. While signed in, open another browser tab in the same browser session and navigate to the share link above. After a moment, you will see the published read-only copy of the worksheet.
#. Click ``Open in CoCalc`` at the upper right. A third browser tab will open.
#. Click ``Files`` at upper left in this latest tab. You will see a Files listing with a line for the Turtle example.
#. Click the ``Copy`` button at the left of the Turtle entry. You can now copy the worksheet to a destination project and folder of your own.

.. figure:: img/only-public.png
     :width: 80%
     :align: center
     :alt: screenshot of copy steps

     copying worksheet from share server to personal project

.. note::

   The remaining methods use the `Python turtle library`_. This library relies on `tkinter <https://docs.python.org/3/library/tkinter.html>`_. You can use tkinter in CoCalc only from the the :doc:`X11 Desktop<../x11>`. Code for the examples below is taken from the **Turtle star** on the doc page for the `Python turtle library`_.

X11 terminal with Jupyter notebook
==================================

.. figure:: img/jupyter-turtle.png
     :width: 80%
     :align: center
     :alt: screenshot of X11 session with Turtle graphics

     python turtle display created by jupyter notebook in a second tab


1. In the x11 terminal, echo the DISPLAY environment variable to get the display number:

.. code-block:: bash

    ~$ echo $DISPLAY
    :581076966

2. In your Jupyter notebook set DISPLAY to the same number:

.. code-block:: python

    import os
    os.environ['DISPLAY'] = ":581076966"

3. Turtle graphics work in the Jupyter notebook, but appear in the X11 desktop. You may have to run the graphics cell twice to see the turtle graphics.


X11 Desktop on a Compute Server
===============================

This is similar to the above, but you run :ref:`X11 Desktop <compute_server_applications>` on a :doc:`Compute Server </compute_server>`, where you have to install ``python3-tk``, for example by putting ``!sudo apt install -y python3-tk`` into a cell in your Jupyter notebook (which has to run on the same compute server, of course):

.. figure:: img/compute_server_turtle.png
     :width: 90%
     :align: center
     :alt: Turtle Graphics on a Compute Server

     Turtle Graphics on a Compute Server


X11 terminal with nteract
==================================

.. figure:: img/nteract-turtle.png
     :width: 100%
     :align: center
     :alt: screenshot of X11 session with nteract and Turtle graphics

     nteract python turtle display


This approach uses the `enteract <https://github.com/nteract/nteract>`_ desktop application with X11.

1. Open an X11 Desktop.

2. Click the ``nteract`` button at the bottom, or type "nteract" at the shell prompt. Wait for nteract to start. This can take up to a minute the first time you run it in CoCalc X11.

3. Paste this code and hit shift enter:

.. code-block:: python

    from turtle import *
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

4. A new tab with title "Python Turtle Graphics" will appear in the X11 display when you run the code. It may not look right the first time. If that happens, return to the compute cell in the nteract tab and run the code again. You can click the vertical split button (upper right) and see the Jupyter notebook and graphics side-by-side, as shown in the screenshot.

.. _Python turtle library: https://docs.python.org/3/library/turtle.html
