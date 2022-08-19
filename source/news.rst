.. _platform-news:

==========================
News
==========================

.. toctree::
    :hidden:

    news/ubuntu-2004


.. _news-2022-08-18-quarto:

2022-08-18 Quarto
=====================================

Adding basic support for `Quarto <https://quarto.org/>`_ – *an open-source scientific and technical publishing system built on Pandoc*.

.. figure:: img/quarto.jpeg
    :width: 100%
    :align: center

    Quarto side-by-side editor


.. _news-2020-10-09-project-info:

2020-10-09: Project Information
=====================================

Projects got a new panel called "Info".
It shows the current status regarding the overall container the project is running in
and also a detailed list of processes.

In the example below, three Jupyter Notebooks are running.
You can e.g. see how one of them spawned Octave.
The indications in red highlight elevated resource usage, which might harm the overall experience.

.. figure:: img/project-info/project-info-table.png
    :width: 100%
    :align: center

    Project Info: showing project's resource usage and processes


.. _news-2020-08-18:

:ref:`ubuntu-2004-upgrade`
====================================


.. _new-2020-03-15:

2020-03-15: Convert Batch of Jupyter Notebooks and Sage Worksheets to PDF
=========================================================================

Added a convenience feature that can be used for offline grading and archiving of student work. See :ref:`Convert student notebooks to pdf for export <export-collected>`.

.. _new-2020-01-16:

.. index:: Account Settings; dark mode
.. index:: Dark mode
.. _overall-dark-mode:

2020-01-16: dark mode
=====================================================

Added: an option to enable overall dark mode in "Account" /  "Preferences".
Checking this gives you a uniformly dark background across the whole page:

.. figure:: img/dark-mode-setting.png
     :width: 65%
     :align: center

     Check the box to enable dark mode.

.. figure:: img/dark-mode-example.png
     :width: 100%
     :align: center

     Screen capture of CoCalc with dark mode enabled.


.. index:: nbgrader; autograder
.. index:: Jupyter Notebooks; nbgrader

2020-01-16: nbgrader autograder for Jupyter notebooks
=====================================================

CoCalc now has integrated nbgrader/autograder for Jupyter notebooks. You can create an assignment with problems that are automatically graded, providing immediate feedback to students. Manual grades and instructor comments can be added after the assignment is collected.

It's all tightly integrated with the course management system. You don't have to configure anything -- you can just use it...

There's an extensive getting-started guide here: :doc:`nbgrader in CoCalc <teaching-nbgrader>`.


.. _new-2020-01-14:

2020-01-14: Export student file use
=====================================

This feature lets you export data about what students do in an assignment or handout. See :ref:`Export student file use <export-file-use>`.

.. _new-2020-01-13:
.. index:: Site licenses (news)
.. _site-license-news:

2020-01-13: Site licenses
===============================

.. index:: Site licenses; for courses (news)

Site license for courses
-------------------------

Site licenses can be used to upgrade student projects in a CoCalc-managed course.
After the license key is entered in course configuration,
all student projects associated to that course are automatically upgraded the next time they start. Here are :ref:`detailed site license course setup instructions <inst-pays>`.


.. index:: Site licenses; for projects (news)

Site license for individual projects
------------------------------------

A site license can be used for a project that is not part of a CoCalc course.
Add the key in Project settings under "Project usage and quotas".
See the section on :ref:`project Licenses <project-add-license>` for details.

.. _new-2019-12-16:
.. index:: Anonymous accounts

2019-12-16: Anonymous accounts
===============================

New users do not have to sign up on CoCalc any more.
An "anonymous" account is created and you can start exploring CoCalc immediately.
It is possible to convert this account into a regular CoCalc account any time.

Beyond that, :ref:`publicly shared files <sharing-files>` can be the seed for a new project.
This makes it easy to experiment with published content.
