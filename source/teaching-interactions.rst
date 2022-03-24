.. index:: Collaboration
.. _collaboration:

=========================================================
Collaboration
=========================================================

There are multiple ways in which you can interact with your students or collaborators, in this section we will present some features that you might find useful when managing a course.


.. contents::
   :local:
   :depth: 2

.. index:: Collaboration; chat rooms
.. _teaching-chatrooms:

Real-time chatrooms
=========================================================

You can create general real-time chatrooms for your CoCalc projects.
You can create a project chat room by clicking on the **New** button, this will create a file with `.sage-chat` extension.

In addition, every file in CoCalc has a separate chat that can be found on the upper left corner of your screen.

.. image:: img/teaching/chat_button.png
     :width: 30%

Every time one of your students writes something into a chat on any one of their files,
you will get a notification displayed on the top bar.

.. image:: img/teaching/instructor_notification.png
     :width: 66%

Clicking on the notification button (bell icon on the top of the screen) displays a notification menu with the latest chats and modifications in the project or specific files.

.. image:: img/teaching/notification_highlighted.png
     :width: 100%

The chat notifications are always presented at the top of the menu, followed by any updates you or your collaborators have done to the project. Clicking on a chat notification will take you to **the student's copy** of the file inside **his/her project**.
From there, you can both reply to their questions and look at their work simultaneously.

.. image:: img/teaching/student_question.png
     :width: 66%

Once you have replied to the student's question (s)he will receive a notification.


.. index:: Collaboration; multi-user editing
.. _multi-user-edit:

Live collaborative editing
===================================

Multiple users can collaborate on a project.
As soon as a collaborator is added to a a project (see :doc:`teaching-create-course`) they share both the project and the associated files.

Live collaborative editing is possible in CoCalc.
If one of your collaborators updates a notebook, the rest can see the changes as they are being made (similar to Google Docs).

.. index:: @Mentions in chat
.. index:: Mentions in chat
.. index:: Chat; @mentions
.. _at-mention-chat:


@Mention collaborators in chat
=================================

CoCalc chats support an ``@mentions`` feature, where you type ``@`` and a list appears of collaborators, which you can select from. Anybody mentioned there will get emailed (unless they are mentioned again in the next few hours, since we don't want to spam people). This helps ensure people know about chats. Any chat will cause the notification count to go up in the bell in the upper right, whether or not you are mentioned.

.. figure:: img/teaching/tex-mentions.png
     :width: 90%
     :align: center

     *@mentioning names in course shared project chat*


.. index:: Shared project; in course
.. index:: Collaboration; shared project


Creating a shared project
===============================

You can create a common shared project for your course. Think of a shared project as your private course website for the students with automatic forum and code support. By default everybody (collaborators and students) will have **write** access to the project and its associated files.

To create a shared project you need to go to your **.course** file and click on the **Shared Project** button.

.. image:: img/teaching/shared1.png
     :width: 100%

If you create a **.sage-chat** file here, all students will receive automatic notifications when questions are posted on the chat.

If you want to make a file or an assignment **read-only** so that students cannot modify it, you need to modify the file permissions. Launch a terminal and type::

    chmod a-w filename

If you want to check the access permissions of all the files contained in a given directory, use the following::

    ls -l

In case you want to change a read only file into a read and write, type::

    chmod a+w filename

Group Projects
========================

There are various ways in which you can facilitate students' group projects in CoCalc.
A couple of options are:

One project per team
-------------------------------

Have someone in each group make a project with all the group members as collaborators.
They will all then be able to collaborate on the same project and modify files simultaneously.

You should note, however, that by using this approach you cannot automatically collect assignments from the team. A workaround could be creating an assignment in your main project and having the students copy that file to their group project.

Using Git
-----------------------------

Students can collaborate from within their individual course projects using [Git] via the terminal in CoCalc.
See :ref:`Using Git <teaching-using-git>` in
:doc:`Tips and tricks <teaching-tips_and_tricks>`.



