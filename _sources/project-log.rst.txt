.. index::
    Projects; activity log
    Project Activity Log
    Log; project activity

.. _project-log:

===============
Project Log
===============

The **Project activity log** gives you quick access to a timeline of past project actions. Once you have a project open, you can view the log by clicking the |history| ("history") icon at upper left in the project toolbar.

.. contents::
   :local:
   :depth: 1

.. figure:: img/project-log.png
     :width: 95%
     :align: center

     ..

.. index:: Project Activity Log; opened files

Recently opened files
---------------------

Opening a recently-updated file by clicking on its name in the project log is often the quickest way to get back to a file you were just working on.

Each time a file is opened with the CoCalc editor, a log entry is created with the timestamp and the name of the user who opened the file. The name of the file is a link that lets you open the file in your session.

.. index:: Project Activity Log; collaborator actions

Collaborator actions
---------------------

Note that each event in the log has the name of the project owner or collaborator who caused that event. You can enter the name of a user in the log filter ("Search log..." - see below) to view the activities of a specific collaborator.

.. index:: Project Activity Log; what is logged

What is logged
---------------------

Here is a list of project activities that cause log entries to be created:

    * changing :ref:`project upgrades <project-upgrades>`
    * :ref:`inviting <add-collaborators>` a CoCalc user to become a collaborator
    * :ref:`inviting <add-collaborators>` a person without a CoCalc account to become a collaborator
    * loading a code :doc:`snippet <snippets>`.
    * loading documentation and sample code from the :doc:`project library <project-library>`
    * :ref:`opening a file <ft-open-files>`
    * :ref:`acting on file(s) <file-actions>` selected in the Files list: Download, Delete, Rename, Duplicate, Move, Copy, Share
    * :ref:`removing <remove-collaborators>` a collaborator
    * requesting :ref:`project restart <project-control>`
    * requesting :ref:`project stop <project-control>`
    * running a command in the Files list :ref:`mini-terminal <mini-terminal>`
    * setting the :ref:`project title and description <set-project-title>`
    * :ref:`starting <project-control>` the project

.. index:: Project Activity Log; filter log entries

Filter log entries displayed
-----------------------------

By typing any string into the "Search log..." box, you can limit the log entries displayed to those that contain your search text. This way, you can search for events relating to a specific file, user, action, etc.

.. figure:: img/project-log-filter.png
     :width: 95%
     :align: center

     filtering log entries for the string "data"

.. index:: Project Activity Log; load older entries

Load older entries
---------------------

The initial project log shows at most 300 entries from the last 2 months. When you click "Load older..." it gets up 7500 log entries going back as long as you want. The display returns to the shorter list if you refresh your browser.

.. |history|
     image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/128/history.png
     :width: 16px