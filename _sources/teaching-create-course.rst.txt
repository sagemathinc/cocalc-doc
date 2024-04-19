.. _create-a-new-course:

Creating a New Course
=====================

In this section we will learn how to create a course project,
how to populate it with a course management file, and how to invite all of your students to join the course.

.. contents::
   :local:
   :depth: 1


Create the Course Project
#########################

The first step is to create a project to contain the course. (While it is technically possible to use the same project for multiple courses, in most cases a separate project for each course works better.)

Sign into CoCalc and click on **Projects** at upper left. Click on **Create New Project**, fill in the **Title**, and click **Create Project**.

.. figure:: img/teaching/create_new_course_project.png
     :width: 90%
     :align: center
     :alt: Creating the Course Project
     
     Creating the Course Project

The new project will be created. If the project does not automatically start, click the **Start Project** button to start it.

.. note::

  When a new project is first opened, you will see a "Free Trial" banner, warning that no license has been applied. You can add a license later (see the :ref:`next chapter <course-upgrading-students>`) in one of two ways:
    - there is an option in course configuration to use the same license for the course project that is used for all the students;
    - you can explicitly specify a different license in project Settings, for example you may want more resources or a longer timeout for the course project.


.. index:: Courses; adding teaching assistants
.. _teaching-add-ta:

Add Teaching Assistants to the Course Project
##############################################

As soon as the course project is created, you can add teaching assistants or other teachers to it as :doc:`collaborators/users <users>` . They will also have access to *all associated student projects*. Do **not** add students in the course as project collaborators!

If the email address you add as a collaborator is not associated with a CoCalc account, an email will be sent to that address with instructions how to join. Once the account with exactly that email address is created, that new user will be added automatically to all projects with pending invitations.


.. index:: Courses; course file

Create the Course File
########################

Almost all aspects of your course, such as which students are enrolled and assignment management, are controlled by a ``.course`` file.

Click **New**, enter the file name, then scroll to **Manage a Course** tile and click it to create the course management file:

.. figure:: img/teaching/create_course_file.png
     :width: 90%
     :align: center
     :alt: Creating the Course File
     
     Creating the Course File



.. index:: Courses; multiple courses in same project
.. index:: Courses; split into sections

You may have more than one course file in a single project, for example you can create different files for different sections. They will be completely independent of each other, allowing not only different groups of students, but also different due dates and different assignments.

.. warning::

  Be aware that any teaching assistant you add to the project will have access to **all** course files and **all** student work. It is often preferable to create a separate project for each section.

.. hint::

  Now is a great time to apply the license to the course file as explained in the :ref:`next chapter <course-upgrading-students>`!


.. index:: Courses; adding students
.. _adding-students:

Add Students to the Course
#############################

Open your new course by clicking on the course file. Select the **Students** tab if it is not already shown. You will see a box at upper right where you can add students and search for them in CoCalc. It's best to add students using their email addresses, because those are unique for CoCalc accounts. However, it is also possible to search for students by their first and last names.

.. hint::

  To add multiple students, you can paste in a comma-separated list of email addresses or names. You can also copy-paste your students' email addresses from a column of a spreadsheet.

.. figure:: img/teaching/add-students-3.png
     :width: 90%
     :align: center
     :alt: Put Students' Emails into Add Students Box
     
     Put Students' Emails into Add Students Box


After running the search by clicking **Search** or hitting Shift-Enter, you can select which students you want add from the search results (use Ctrl-click or Cmd-click for more than 1 student), or just click the **Add all students** button:

.. figure:: img/teaching/add-students-4.png
     :width: 90%
     :align: center
     :alt: Add All Students After Searching by Email Addresses
     
     Add All Students After Searching by Email Addresses


Next, the student projects will be created. Please be patient until all students are processed and do not close CoCalc. If the process appears stalled after creating some number of student projects, you can refresh your browser to check for updated results.

.. figure:: img/teaching/add-students-5.png
     :width: 90%
     :align: center
     :alt: List of Students in the Course
     
     List of Students in the Course


If your project (the one with the ``.course`` file) has network access (this is provided when any CoCalc license has been applied), any student who does not have an account on CoCalc will be sent an email invitation to create an account and join your course. For security reasons, CoCalc does not automatically send email invitations to students added if they already have a CoCalc account.

Some important points:

* Email addresses that are followed by **(invited)** do not have a CoCalc account yet.
  This note will disappear as soon as they sign up.
* You can see when each student last used the course project. In this case -- never!
* The **! Free Trial** warning next to each student shows that they are running this course on free servers.
  It is **strongly** recommended that you upgrade this to members-only servers for your students, see the :ref:`next chapter <course-upgrading-students>`. 

.. warning::

    Some email services, notably Hotmail and Yahoo Mail, may silently block emails sent from our service. In that case, an invitation to sign up will not appear in the inbox or spam folder of the intended recipient and another method must be used to communicate sign-up information to the student.


What do the Students Get?
#########################

On being invited to a course, each student will have a project created for them in their CoCalc account that corresponds to the course. Each project will have you and the course teaching assistants set as collaborators. This allows you to access student's work at any time and help them with their work.

Each student's course project will have its own resources according to the license configured in the course file. You can learn more about licenses in the :ref:`next chapter <course-upgrading-students>` or the :doc:`upgrade-guide`.


.. index:: Courses; reconfigure student projects
.. index:: Reconfigure student projects

Reconfigure Student Projects
###############################

In the course Configuration tab on the right, click `Reconfigure all projects` to ensure student projects have correct students and teaching assistants, titles and descriptions.
Doing so will also resend email invitations to students who have not already signed up for CoCalc.

.. figure:: img/teaching/course-reconfigure.png
     :width: 90%
     :align: center
     :alt: button to reconfigure all student projects in lower right of course Configuration tab

     "Reconfigure all projects" at lower right in course Configuration


.. index:: Courses; re-send email invitations
.. index:: Re-send student email invitations

Resend outstanding email invites
##################################

In the course Configuration tab on the right, click `Reinvite students` to send/resend an email invitation to all students who do not yet have an account on CoCalc. This will send at most one email per student per day.

.. figure:: img/teaching/reinvite-students.png
     :width: 90%
     :align: center
     :alt: button to resend email invitations to students in lower right of course Configuration tab

     "Reinvite students" at lower right in course Configuration
