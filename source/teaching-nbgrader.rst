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

``nbgrader`` is intended to provide the following teaching-related functions in a Jupyter notebook environment: [#]_

#. Maintain separate instructor & student notebooks.
#. Autograde coding exercises.
#. Manually grade free-form responses.
#. Leave comments for students.


CoCalc nbgrader differences from classic nbgrader
=================================================

* no need to install special modules or extensions
* integrates with CoCalc course management tools for distributing and collecting assignments
* run student in student project, not in instructor project
* error reports in a separate frame
* annotating cells
* summary at the top
    * how many questions there are
    * how many you are successfully completed
    * how many remain
    * able jump directly to each question
* validate button does "run all not stopping for errors"
* annotation next to answer cells, so you know that evaluating them without errors gives you a certain number of points
* button to insert a template with the appropriate text when making an assignment
* more context/support for students using nbgrader enhanced notebooks

.. rubric:: Footnotes

.. [#] The list of nbgrader functions is taken from the introductory video in the `nbgrader documentation <https://nbgrader.readthedocs.io/en/stable/>`_.
