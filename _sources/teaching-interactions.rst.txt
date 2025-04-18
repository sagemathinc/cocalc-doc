.. index:: Collaboration
.. _collaboration:

Collaboration
=============

In principle, collaboration for the instructor project and all student projects is "the same" as for all other CoCalc projects. Here we will highlight some features and ways of using them that you might find useful specifically when managing a course.

.. contents::
   :local:
   :depth: 2
   
   
Look at Students Work
---------------------

As described in the handling of :ref:`assignments-and-handouts`, you can always open the files that each student is working on: before collecting them, during grading, or after. There can be several reasons for this:

- you may wonder how students are doing on a newly developed assignment that may need some tweaking to become more clear or more challenging
- you may wonder if particular students need some extra help
- unfortunately, sometimes you may wonder if some students are cheating...

Not only you can open each file at its current state, but you can also use :doc:`time-travel` to get a sense of its evolution and see what approaches have students tried to solve a problem or deal with code errors. If you see big chunks of text/code appearing in a single revision, they were likely copy-pasted from somewhere else.


Edit Students Files
-------------------

You do have write access to students projects and can make edits in their files and notebooks, even while students are actively editing these files as well. :doc:`time-travel` will keep track of who has done which change. If you are editing or looking at sections that are close to each other, you will see each other moving cursors with name tags:

.. figure:: img/teaching/instructor_cursor.png
    :width: 90%
    :align: center
    :alt: Instructor's Cursor in Student's View
    
    Instructor's Cursor in Student's View
    

Side Chats and Mentions
-----------------------

Of course, it may be difficult to notice if you edit a file of a student, and it may be unexpected. Instead of editing the file directly or in addition to it, you can leave comments in a :ref:`side-chat` of any file and attract student's attention using :ref:`chat-at-mentions`. The student will get a notification, can reply to you, and then you will get a notification as well:

.. figure:: img/teaching/mentioning_student.png
    :width: 90%
    :align: center
    :alt: Mentioning Student in a Side Chat
    
    Mentioning Student in a Side Chat
    
.. figure:: img/teaching/student_got_mentioned.png
    :width: 90%
    :align: center
    :alt: Student Sees a Mention Notification
    
    Student Sees a Mention Notification
    
.. figure:: img/teaching/student_replies.png
    :width: 90%
    :align: center
    :alt: Student Replies to the Instructor
    
    Student Replies to the Instructor
    
This may be even more useful in the other direction - any student can ask an instructor or a TA for help! They may also ask our :doc:`ai` for help, if you have not :ref:`disabled this functionality <restrict-student-projects>`.


.. index:: Shared project; in course
.. index:: Collaboration; shared project

Shared Project and Chat Rooms
-----------------------------

While regular student projects are isolated from each other, a shared project allows all students in a class to collaborate on a document or discuss some topics. For example, you can put an article into a shared project and all students can leave comments and ask/answer questions in a :ref:`side-chat`. Or you can create any number of standalone :ref:`chatroom`. To create or access your **Shared Project** use the corresponding tab in the course file.

Note that all students have equal access to the shared project. In particular, they are capable of deleting files or corrupting code in them, but if that happens it should be possible to restore the documents using :doc:`time-travel` and :ref:`snapshots`. Also, as a safeguard against accidents, you can change permission of some files to read-only in a :ref:`terminal`. For example, you can use ``chmod a-w filename`` to make a file read-only and ``chmod a+w filename`` to make it writable again.


Group Projects
--------------

When individual and shared projects are too extreme, you can also create projects for smaller groups.

At the moment we do not provide a completely hassle free way of creating projects for groups, but it is on our road map and a possible workaround meanwhile is to create another course file where only some of the students are "enrolled" - these are "group leaders" designated by you. Once their projects are created, you or these leaders may add other members of each group as collaborators.

.. hint::

    It is possible to edit student names in the course file. Such edits are local to that file, i.e. it does not affect student accounts. In the context of group projects you may change your leaders names to either group titles or names of all students in the group.
