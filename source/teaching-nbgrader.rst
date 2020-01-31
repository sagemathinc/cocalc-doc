.. index:: Courses; nbgrader
.. index:: nbgrader
.. _nbgrader-doc:

=====================
nbgrader in CoCalc
=====================

`nbgrader`_ is a tool for creating and grading assignments in Jupyter notebooks. CoCalc Jupyter notebooks include support for nbgrader core features without the need for added modules and extensions.

.. contents::
   :local:
   :depth: 2

.. index:: nbgrader; purpose
.. _nbgrader-purpose:

Purpose of nbgrader
===============================

**nbgrader**  allows an instructor to do the following when teaching in a Jupyter notebook environment:

#. Maintain separate instructor & student versions of Jupyter notebooks.
#. Automatically grade coding exercises written using Python, R, Julia, and more.
#. Manually grade free-form exercises and other tasks.
#. Leave comments for students.
#. Track student grades.

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

These steps illustrate CoCalc course integration with nbgrader. So we start with a .course file and assume that at least one student has been :ref:`added to the course <adding-students>`.

1. Create an assignment folder.
-------------------------------

Open the .course file and select the ``Assignments`` tab. There is field at upper right with the prompt "Add assignment by folder name ..."

.. figure:: img/nbgrader/nbg-create-assg-0.png
     :width: 95%
     :align: center

     About to create an assignment

You can enter the path of a new folder you want to create:

.. figure:: img/nbgrader/nbg-create-assg.png
     :width: 95%
     :align: center

     Creating a folder for ``Assignments/Assignment3``


Or the enter name of an existing folder that hasn't been assigned yet:

.. figure:: img/nbgrader/nbg-create-assg-1.png
     :width: 95%
     :align: center

     Selecting the existing folder ``Assignment4``

2. Start a Jupyter notebook for the assignment.
------------------------------------------------

With the assignment folder created, open the folder for the assignment:

.. figure:: img/nbgrader/nbg-open-assg-folder.png
     :width: 95%
     :align: center

     Opening the folder for ``Assignments/Assignment3``

Start a new Jupyter notebook:

.. figure:: img/nbgrader/nbg-new-notebook.png
     :width: 95%
     :align: center

     Starting notebook ``hw3.ipynb`` in folder ``Assignments/Assignment3``


In the Jupyter notebook, use the top menu to select:

   View --> Cell Toolbar... --> Create assignment (nbgrader)

.. figure:: img/nbgrader/nbg-view-ca.png
     :width: 95%
     :align: center

     Starting nbgrader assignment in a Jupyter notebook

You will a dropdown cell-type menu in the upper right of each cell, which you can use to create problems, answer tests, etc. What you see depends on whether the cell is a code cell or a markdown cell. Here is an example of the cell-type menu for a code cell:

.. figure:: img/nbgrader/nbg-cq-code.png
     :width: 95%
     :align: center

     Cell-type menu for a code cell


3. Create questions.
---------------------

When you select a menu option from the dropdown for the cell, e.g., "Autograded answer", a sample working snippet of code will be inserted in the notebook (assuming you are using a Python, R, or Julia kernel). You can then modify this template for your purposes.

.. figure:: img/nbgrader/nbg-code-snippet.png
     :width: 95%
     :align: center

     Sample working snippet inserted in Python code cell

The `official nbgrader documentation`_ explains the use of each nbgrader cell type. For your convenience, CoCalc has a button at right with a link to the  documentation for whichever type of nbgrader cell has been selected.

At this point, go ahead and create all the cells for the assignment.

4. Generate student version of the notebook.
--------------------------------------------

After creating cells for the assignment, click ``Generate student version.`` button at the top of the notebook.


.. figure:: img/nbgrader/nbg-gen-sv.png
     :width: 95%
     :align: center

     About to generate student version of the notebook

A confirmation screen appears. Click ``Create or update student version``. CoCalc will generate the student version of the notebook, with solutions removed, and only the student-visible tests, and place it in the ``student`` subdirectory of the assignment folder. For example, if you have been creating questions in ``Assignments/Assignment3/hw3.ipynb``, the filesystem will look like this::

    Assignments/
    ...
    ├── Assignment3
    │   ├── hw3.ipynb      ← instructor version
    │   └── student
    │       └── hw3.ipynb  ← student version

The student version of the notebook automatically opens in another tab, where you can review the contents. When the student uses that notebook, they can "self evaluate" their code by running the test cells and seeing whether or not there are errors, or they can click the "Validate..." button at the top of the notebook to run all code.

5. Notebook table of contents.
--------------------------------------------

If you click the "Contents" button at the top of your Jupyter notebook, you'll see a table of contents appear to the left that has links to all the nbgrader problems. You can create section headings using markdown titles. The table of contents view is available in instructor and student versions of the notebook.

.. figure:: img/nbgrader/nbg-contents.png
     :width: 95%
     :align: center

     Notebook table of contents


6. Distribute the assignment to students.
--------------------------------------------

Back in the .course file under "Assignments", click ``Assign...`` to distribute the homework to students. This step copies contents of the "student/" folder into student projects. Here's a view of the files in the *student project*::

    Assignments/
    ...
    ├── Assignment3
    │   └── hw3.ipynb  ← student version

.. note::

   When there is a "student/" subdirectory in the assignment folder, as is the case with all nbgrader notebooks, the ``Assign...`` button will ONLY distribute contents of the "student/" subdirectory. This is a new feature.

7. Students complete the assignment.
--------------------------------------------

Have your students complete the assignment. All student work takes place in the student's project. Students can click ``Validate`` to see if all tests pass.

7. Collect the assignment.
--------------------------------------------

In the .course file under "Assignments", click ``Collect...`` to distribute the homework to students.

8. Run nbgrader.
--------------------------------------------

When you click the "Run nbgrader" button, nbgrader is run on the collected notebooks **in memory in the student projects (for security)** and the results are saved in the course.
This step runs CoCalc's re-implementation of the nbgrader validation steps. It is *not* running nbgrader's python scripts behind the scenes.

.. figure:: img/nbgrader/nbg-about-to-autograde.png
     :width: 95%
     :align: center

     About to run nbgrader for all collected copies of Assignment3.

After running nbgrader, a summary of scores is displayed for each graded assignment. Click ``More...`` to see a small table with scores for each problem.

At this point, all cells of type "Manually graded answer" will show a blank score.

.. figure:: img/nbgrader/nbg-autograded.png
     :width: 95%
     :align: center

     After autograding, before reviewing manually graded questions

9. Do manual grading and add instructor comments.
-------------------------------------------------

You can enter manual scores as needed. When all manual scores are
entered the overall scores are automatically updated.

If you want to make additional comments, click ``Edit grade``. You can use Markdown in the comments, including LaTeX expressions.

.. figure:: img/nbgrader/nbg-manual-grade.png
     :width: 95%
     :align: center

     Entering a manual grade and an instructor comment


10. Return the assignment.
--------------------------------------------

Click ``Return...`` to return the assignment to the student. Here's a view of the files in the *student project* after graded work is returned::

    Assignments/
    ...
    ├── Assignment3
    │   ├── hw3.ipynb
    └── graded-Assignment3
        ├── GRADE.md
        ├── STUDENT - Janice Doe.txt
        └── hw3.ipynb

The file GRADE.md appears in the returned assignment. It uses markdown and shows a table of scores of problems from nbgrader. Here's an example of the GRADE.md file that the student receives (rendered view only):

.. figure:: img/nbgrader/nbg-student-grade.png
     :width: 65%
     :align: center

     Sample grade report returned to the student


Feedback
================

If you have questions or comments, or are likely to use nbgrader in CoCalc in the future, `let us know! <mailto:help@cocalc.com>`_



.. _nbgrader: https://nbgrader.readthedocs.io/
.. _official nbgrader documentation: https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html#developing-assignments-with-the-assignment-toolbar
