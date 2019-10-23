.. index:: Pair: Courses; nbgrader

=====================
nbgrader in CoCalc
=====================

.. note::

    This section of the User Manual describes features that are under active development and expected to be available soon.

`nbgrader <https://nbgrader.readthedocs.io/en/stable/>`_ is a tool for creating and grading assignments in Jupyter notebooks. CoCalc Jupyter notebooks include support for ``nbgrader`` core features without the need for added modules and extensions.

.. contents::
   :local:
   :depth: 2

.. index:: nbgrader; purpose
.. _nbgrader-purpose:

Purpose of nbgrader
===============================

`nbgrader <https://nbgrader.readthedocs.io/en/stable/>`_  provides the following
teaching-related functionality in a Jupyter notebook environment: [#]_

#. Maintain separate instructor & student versions of Jupyter notebooks
#. Automatically grade coding exercises written using Python, R, Julia, and more.
#. Manually grade free-form exercises and other tasks
#. Leave comments for students
#. Track student grades

CoCalc nbgrader (currently under active development!)
======================================================

The official nbgrader project is implemented as Python scripts
and `extensions to Jupyter classic and JupyterLab <https://nbgrader.readthedocs.io/en/stable/user_guide/installation.html>`_.
CoCalc has it's own completely new implementation of nbgrader
from scratch in order to fully support realtime collaboration,
course management, and other functionality of CoCalc.

The Jupyter metadata format of Cocalc's nbgrader is the same as that of the
official nbgrader extension, and the user experience is similar,
though with some changes.


* There is no need to install special modules, extensions or configure anything.
* Students see an annotation next to answer cells, so they know that evaluating these cells without errors gives a certain number of points.
* Instructors have a toolbar that inserts a template with example input or automated tests.
* There is a Table of Contents overview that shows a link to each question, and whether or not each question passes tests (coming soon).
* (coming soon) Integration with CoCalc's course management tools for distributing and collecting assignments.
* (coming soon) Automated grading safely runs code in the student's project, not in the instructor's project.

Getting started
================

In any Jupyter notebook, use the top menu to select

Cell --> Cell Toolbar... --> Create assignment (nbgrader)

You will then see dropdown menus in the upper right of each cell, which you can use to create problems, answer tests, etc.   What you see
depends on whether the cell is a code cell or a markdown cell.

When you select a menu option from the dropdown for the cell, e.g., "Autograded answer", a sample working snippet of code will be inserted in the notebook (assuming you are using a Python, R, or Julia kernel). You can then modify this template for your purposes. There's also a button with a link to the official nbgrader documentation for
this type of nbgrader cell.

When the nbgrader toolbar is visible, you can click the "Student version..." button at the top of the Jupyter notebook and CoCalc will generate the student version of the notebook, with solutions removed, and only the student-visible tests. You will see this new version of the notebook in another tab, where you can ensure it looks right. When the student uses that notebook, they can "self evaluate" their code by running the test cells and seeing whether or not there are errors, or
they can click the "Validate..." button at the top of the notebook
to run all code.

If you click the "Contents" button at the top of your Jupyter notebook,
you'll see a table of contents appear to the left that has links to all the nbgrader problems, in addition to section headings for markdown cell
titles.

**As of October 23, 2019, CoCalc is currently missing** integration of nbgrader with our course management system. When implemented, this will include support
for both manual (and automatic) grading of student work. CoCalc hasn't yet automated running the teacher tests on student code.  Right now, the only thing you can do is click "Student version..." to generate the
student version of the notebook, which will be placed in a subdirectory
called "student".  You could then make this student ipynb file available
to the students by placing it in an assignment.  The student would then
answer all the questions, and verify their correctness by running
the tests you provide.  You would then collect their work, but you would
have to  manually grade it (at least you could click Validate...), and there is no way to easily
run your secret tests on the student code.

If you have any questions, comments, or are likely to
use nbgrader in CoCalc in the future,
`let us know! <mailto:help@cocalc.com>`_


