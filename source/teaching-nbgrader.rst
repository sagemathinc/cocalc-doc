.. index:: Courses; nbgrader
.. index:: nbgrader
.. _nbgrader-doc:

=====================
nbgrader in CoCalc
=====================

.. note::

    This section of the User Manual describes features that are under active development and expected to be available soon.

`nbgrader`_ is a tool for creating and grading assignments in Jupyter notebooks. CoCalc Jupyter notebooks include support for ``nbgrader`` core features without the need for added modules and extensions.

.. contents::
   :local:
   :depth: 2

.. index:: nbgrader; purpose
.. _nbgrader-purpose:

Purpose of nbgrader
===============================

`nbgrader`_  provides the following teaching-related functionality in a Jupyter notebook environment:

#. Maintain separate instructor & student versions of Jupyter notebooks
#. Automatically grade coding exercises written using Python, R, Julia, and more.
#. Manually grade free-form exercises and other tasks
#. Leave comments for students
#. Track student grades

CoCalc nbgrader
===============

The official nbgrader project is implemented as Python scripts
and `extensions to Jupyter classic and JupyterLab <https://nbgrader.readthedocs.io/en/stable/user_guide/installation.html>`_.
CoCalc has its own completely new implementation of nbgrader
from scratch in order to fully support realtime collaboration,
course management, and other functionality of CoCalc.

The Jupyter metadata format of Cocalc's nbgrader is the same as that of the
official nbgrader extension, and the user experience is similar,
though with some changes.


* There is no need to install special modules, extensions or configure anything.
* Students see an annotation next to answer cells, so they know that evaluating these cells without errors gives a certain number of points.
* Instructors have a toolbar that inserts a template with example input or automated tests.
* There is a Table of Contents overview that shows a link to each question, and whether or not each question passes tests (coming soon).
* Integration with CoCalc's course management tools for distributing and collecting assignments.
* Automated grading safely runs code in the student's project, not in the instructor's project.

Getting started
================

In any Jupyter notebook, use the top menu to select

View --> Cell Toolbar... --> Create assignment (nbgrader)

You will then see dropdown menus in the upper right of each cell, which you can use to create problems, answer tests, etc.   What you see
depends on whether the cell is a code cell or a markdown cell.

When you select a menu option from the dropdown for the cell, e.g., "Autograded answer", a sample working snippet of code will be inserted in the notebook (assuming you are using a Python, R, or Julia kernel). You can then modify this template for your purposes. There's also a button with a link to the official nbgrader documentation for
this type of nbgrader cell.

When the nbgrader toolbar is visible, you can click the "Student version..." button at the top of the Jupyter notebook and CoCalc will generate the student version of the notebook, with solutions removed, and only the student-visible tests. You will see this new version of the notebook in another tab, where you can ensure it looks right. When the student uses that notebook, they can "self evaluate" their code by running the test cells and seeing whether or not there are errors, or
they can click the "Validate..." button at the top of the notebook
to run all code.

If you click the "Contents" button at the top of your Jupyter notebook, you'll see a table of contents appear to the left that has links to all the nbgrader problems, in addition to section headings for markdown cell titles.

1. Create an assignment in a CoCalc course, and put one or more ipynb files in
the assignment
2. Use the "Make an assignment" toolbar in the Jupyter notebook to
create questions in the notebook
3. Click "Generate student version" at the top of the notebook to
generate a version for students in the student subdirectory.
4. Push out the assignment to the students -- (NOTE: they will ONLY get a copy of the student/ subdirectory -- this is a new feature.)
5. Have them edit it; they can click Validate to see if all tests pass.
6. Collect the assignment as usual
7. There's a new "Run nbgrader" button -- click it and nbgrader is run
on all the collected notebooks **in memory in the student projects
(for security)**, and the results are saved in the course.  This actually runs
my own re-implementation of the nbgrader validation steps, and it is *not*
really running the nbgrader python scripts behind the scenes.
8. You will see a summary of scores, and can click to see a nice little
table with scores for each problem.
9. You can enter manual scores as needed; when all manual scores are
entered the overall scores are automatically updated.
10. You can then return the assignment to the student.
11. I greatly improved GRADE.md (which appears in the returned assignment)
to actually use markdown and also show a table of scores of problems from nbgrader.  

If you have any questions, comments, or are likely to
use nbgrader in CoCalc in the future,
`let us know! <mailto:help@cocalc.com>`_



.. _nbgrader: https://nbgrader.readthedocs.io/
