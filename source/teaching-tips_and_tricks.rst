.. index:: Courses; FAQ

=======================
FAQ, Tips and Tricks
=======================

In this section we will present some CoCalc features and useful tricks that will make the management of your project easier and answer some common questions.

.. contents::
   :local:
   :depth: 2

.. index:: Text fields; Markdown and LaTeX

Text fields generally support Markdown and LaTeX
==========================================================

CoCalc not only facilitates the creation of LaTeX documents, but most input areas in CoCalc support and render LaTeX and markdown  (specifically  `GitHub Flavored Markdown`_).

For example, you can use LaTeX math formulas in the chat rooms:

.. image:: img/teaching/before_latex_render.png
     :width: 66%

which renders as

.. image:: img/teaching/after_latex_render.png
     :width: 100%


.. _GitHub Flavored Markdown: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

.. index:: Courses; multiple assignment folders

Making multiple assignment folders quickly
==========================================================

So far we have shown how to create folders and files by using the **New** button every time. → |NEW_BUTTON|

.. |NEW_BUTTON| image:: img/teaching/new.png
                  :height: 20pt

However, such a method could be quite time consuming when you need to create multiple folders, subfolders, and documents. If you are a terminal fan you could create a shell script in your preferred programming language and run it from the terminal.


Alternatively, in the files menu of your project, you can enter paths such as `assignments/assignment1/directions.md` then hit **enter** or **ctrl+enter** to create `directions.md` inside the folder `assignment1` within `assignments`. Hitting **enter** will open up the new file while **ctrl+enter** will silently create the necessary files and folders in the path.

.. image:: img/teaching/file.png
     :width: 100%

You can also create folders here just by ending with a `/`

.. image:: img/teaching/folder.png
     :width: 100%

.. index:: Courses; start all student projects

Starting up everyone's project before class
==========================================================

By default, projects have an idle time of 24 hours before they spin down and need to be restarted. However, it may be handy to start everyone's project before a class or presentation so that they are all "hot loaded".

You can easily do this from your course manager:
first, open the course configuration tab:

.. image:: img/teaching/settings.png
     :width: 100%

Then scroll down to find and click on the `Start all...` button

.. image:: img/teaching/start_all_clicked.png
     :width: 100%

.. index:: Courses; restarting a project

Restarting a project
==========================================================

Every time you open a Jupyter notebook or a Sage Worksheet, its state is stored in memory. This can become quite costly if you open multiple files one after the other (e.g. when you are marking your students' work).

To solve this, you can stop every instance using the stop button (for both Jupyter notebooks and Sage worksheets) once you are done with your marking.

.. image:: img/teaching/stop_notebook.png
     :width: 100%

Alternatively, you can restart the entire project, which will clean everything. You just need to go to your project settings and click on **Restart project**.

.. image:: img/teaching/restart_project.png
     :width: 60%

.. _teaching-using-git:

.. index:: Courses; teaching with Git

Using Git
==========================================================

CoCalc support for the terminal enables students (and instructors) to collaborate using Git within a course-affiliated project.

If you already have a project or some files allocated in GitHub you can add them to your project.
Click on the **New** button and add/paste the link to your repository in the appropriate text box. Click on the **Download from Internet** button.

Also you can use the terminal to commit and push changes to your repository in GitHub.
(see howto: :doc:`howto/git`)

.. image:: img/teaching/download.png
     :width: 100%

.. note::

    You need to have internet access enabled in your project.

.. index:: Courses; TimeTravel diffs

Time Travel Diffs
==========================================================

The editor based documents (e.g. Python code, LaTeX documents, markdown files, etc.) as well as Jupyter notebooks and Sage worksheets are Time Travel Diffs supported. The Time Travel Diffs feature allows you to see what happened with a file within a certain time interval.

Open up **Time travel** from any document:

.. image:: img/teaching/time_travel.png
     :width: 100%

then click on changes and drag the sliders to see the document in a given time interval.

.. image:: img/teaching/time_travel_sliders.png
     :width: 100%

If you need to revert the document to a previous state, drag the slider to the desired revision and click on **Revert live version to this**. Doing so reverts the document contents to that specific version. If you have checked the **Changes** box to compare two revisions and click on **Revert live version to this**, contents are reverted to the latter of the two revisions being compared. Note that reverting a file simply creates a new version of the file equal to the old file at that point in time; in particular, no work is lost!

.. index:: Courses; run a command in all student projects

Run Terminal command in all student projects
============================================

If you are managing a course, there may be a time when you want to
run a shell command in every student project. The following
feature allows you to do that, if you are using a .course file
for the course.

In the ``Configuration`` tab of the course there is a
panel called ``Run Terminal command in all student projects``.  You
can use it to run a command (e.g., to create a file or whatever) in
*all* projects in a course...  It's a single arbitrary bash command.

.. image:: img/teaching/term_command_course.png
     :width: 60%


.. index:: Courses; copying assignments to students
.. _course-copy-assignments:

How exactly are Assignments copied to students?
==================================================

When you assign an assignment to your students,
it is copied from your project to your students' projects.
Behind the scenes, this copy is done with the command

::

    rsync -zaxs --update --backup [...] source/  dest/

There are two important options here::

    --update: do not copy over a file if a NEWER file (by timestamp)
              exists in the destination

and

::

    --backup: if the source file `foo` (say) is NEWER than the destination file
              `foo` (e.g., you edit your homework assignment after students have worked
              on it),  then `dest/foo` is moved to `dest/foo~` and `foo` is copied
              to the destination.

In particular, if the source files have an old timestamp and you've already assigned the assignment (and students may have worked on it), then nothing at all will happen on copy (due to the ``--update`` option).
If one or more source files have a *newer* timestamp than a file in the target directory,
then the target file is copied to a backup and the source is copied over.

If you just want to add a new file to an assignment, you could ensure that all the other files are very old, e.g., by using the touch command in a :doc:`terminal`.  E.g.,


::

    touch -d 'Jan 1' *

would make it so that everything appears to be from January 1.

Alternatively, you could just remove the files from the assignment folder, then move them back later.

Assigning an assignment never deletes missing files in the target,
`unless` you explicitly clicked and confirmed the ``Replace student files!`` button.
This button adds an additional flag::

       --delete
              This  tells  rsync to delete extraneous files from the receiving side
              (ones that aren’t on the sending side), but only for the
              directories that are being synchronized.

Some tests below illustrate how rsync works::

    $ mkdir tmp2
    ~$ cd tmp2
    ~/tmp2$ mkdir a b
    ~/tmp2$ echo "0" > a/x
    ~/tmp2$ rsync -zaxs --update --backup a/ b/
    ~/tmp2$ ls a
    x
    ~/tmp2$ ls b
    x
    ~/tmp2$ rsync -zaxs --update --backup a/ b/
    ~/tmp2$ vi b/x
    ~/tmp2$ rsync -zaxs --update --backup a/ b/
    ~/tmp2$ ls -lht b
    total 1.5K
    -rw------- 1 user user 4 Oct 13 16:27 x
    ~/tmp2$ more b/x
    0
    1
    ~/tmp2$ touch a/x
    ~/tmp2$ rsync -zaxs --update --backup a/ b/
    ~/tmp2$ ls b
    x  x~
    ~/tmp2$



.. note::

    We would like to add a new 3-way merge option, which would be more clever and instead of making a backup file of students modified work, would merge your changes into their file.  This is not done yet.

.. index:: Courses; invite students without email

Invite Students Without Having Their Email Addresses
=====================================================

**Question:** The course management software at my university makes it hard to get a list of student emails. Is there a way I can send them a generic invitation link that they can click to join the course?

**Answer:** We don't support sending generic invitations yet (see `CoCalc issue #886 <https://github.com/sagemathinc/cocalc/issues/886)>`_). However, you can use the following workaround:

Assign fake email addresses to all students in your class, e.g.:: c

    student+<student_id>@your-university.edu

Then tell the students to sign up for CoCalc using that "fake" email address. This assumes you have some way to communicate with your students, perhaps in class.

Once students sign up, they will be added as collaborators to their project for the course. At that point, they can change their email address to anything they want, in order to ensure they get @mention notifications, can do password reset, etc.

If student_id's are secret/sensitive, you could use something derived from them, e.g., the last two digits.

.. index:: Courses; verifying student activity

Verifing Student Activity
=============================

In some situations it may be useful to confirm when work was done in a student project.

* If you open the activity log for a student project, you can see exactly when and who opened any file.

* With any file open in a student project, you can see exactly what was done with it and when by clicking the :doc:`TimeTravel <../time-travel>` button, including the total number of edits made to the file (as recorded by TimeTravel) and time and date of the last change. You can click the "Changes" checkbox and see what happened for any range of dates.

* It's impossible for users to delete or change something once it is recorded in TimeTravel (except by explicitly requesting deletion via a support request). However, it's conceivable maybe something got lost, since no software is perfect.

* Folders under :ref:`Backups <project-snapshot>` are snapshots of the exact state of the filesystem, which are independent of TimeTravel, but provide a good double check.
