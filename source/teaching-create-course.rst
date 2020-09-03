.. _create-a-new-course:

=====================
Creating a New Course
=====================

In this section we will learn how to create a course project,
how to populate it with a course management file and how to invite all of your students to join the course.

.. contents::
   :local:
   :depth: 1


###########################
Creating the Course Project
###########################

The first step is to create an instructor's project to contain the course.

.. note::

    :ref:`upgrade-teacher-project-first`
    Then check our :ref:`very frequently asked questions <teaching-vfaq>`.

Log into CoCalc and click on the **Projects** icon in the top left hand corner of the screen.

.. image:: img/teaching/projects-cc.png
    :width: 100px
    :align: center

Click on **Create New Project**, fill out the **Title** and **Description** and click on **Create Project**

.. image:: img/teaching/create_new_course_project.png
     :width: 100%
     :align: center

The new project will appear at the top of the project list. Click on its  title to open it.

.. image:: img/teaching/course_list.png
     :width: 100%
     :align: center

.. index:: Courses; adding teaching assistants
.. _teaching-add-ta:

########################################
Adding Teaching Assistants to the Course
########################################

To add teaching assistants or other teachers to the course, open the course project, click on the settings tab and look down to see "Add new collaborators" in the project settings.

Under **Add new collaborators**, you can find or add collaborators by name or email address.
These collaborators will also have access to all associated student projects orchestrated by that project.
Do **not** add any students of yours as project collaborators!

.. image:: img/teaching/collaborators.png
     :width: 50%
     :align: center

If the email address you add as a collaborator is not associated with a CoCalc account,
an email will be sent to that address with instructions how to join.
Once the account with exactly that email address is created, that new user will be added automatically to all projects with pending invitations.

.. index:: Courses; course file

########################
Creating the Course File
########################

Almost all aspects of a course, such as which students are enrolled and assignment management, are controlled by a **.course** file. We'll now create this file.

Open the course project, click on **New** and give the course a title.
Here, I've used `Autumn_2016_PHY001`.
Click on **Manage a Course** to create the course file.

.. image:: img/teaching/new_managecourse.png
     :width: 100%
     :align: center

If you go to the root of the course project directory, you will see that a new file has been created with the extension **.course**. This is the course management file and most aspects of your course are controlled by it.

.. image:: img/teaching/course_file.png
     :width: 100%
     :align: center

.. index:: Courses; multiple courses in same project
.. note::

    You may have more than one course file in a single project, as is explained in the next section. Be aware that that any account you add as a TA to the project will have access to course files and student work for **all** courses in that project.

.. index:: Courses; split into sections

Split course into multiple groups
-------------------------------------

**Note:** If your course is large, it is possible to partition your class into several groups or sections.
To accomplish that, simply create more than one course file.
For example, ``PHY001_A.course``, ``PHY001_B.course``, ``PHY001_C.course``, ...
for groups ``A``, ``B``, ``C`` and so on.

These course files are independent of each other,
which allows not only different groups of students, but also different due dates, etc.

.. index:: Courses; adding students
.. _adding-students:

#############################
Adding Students to the Course
#############################

Open your course by clicking on the **.course** file.

In the **Students** tab, add a comma separated list of students' emails addresses in the search box and click on the search icon.

.. image:: img/teaching/student_list.png
     :width: 100%
     :align: center

If you have a particular large class, the above method may take a very long time. If you have your students' email addresses in an Excel spreadsheet (or Google Sheet) you can copy and paste them directly in the **Add student** box.

After parsing the list, you can either explicitly the students to add (press shift or ctrl key for multiple selections),
or just click the "Add all students" button.

Next, the student projects will be created. Please be patient until all students are processed and do not close CoCalc.

.. image:: img/teaching/student_list2.png
     :width: 100%
     :align: center

If your project (the one with the .course file) has the :ref:`Internet Access upgrade <internet-access>`, any student who does not have an account on CoCalc will be sent an email invitation to create an account and join your course. 
For security reasons, CoCalc does not automatically send email invitations to students added if they already have a CoCalc account.

Your course page will now look like this

.. image:: img/teaching/student_list3.png
     :width: 100%
     :align: center

* Email addresses that are followed by **(invited)** do not have a CoCalc account yet.
  **(invited)** will disappear as soon as they sign up.
* You can see when each student last used the course project. In this case -- never!
* The **! Free** warning next to each student shows that they are running this course on free servers.
  It is **strongly** recommended that you upgrade this to members-only servers for your students. 
  You can also require in the configuration page that your students pay a small one-time fee to upgrade their projects (see below).

.. note::
    Some email services, notably Hotmail and Yahoo Mail, may silently block emails sent from our service. In that case, an invitation to sign up will not appear in the inbox or spam folder of the intended recipient and another method must be used to communicate sign-up information to the student.


.. index:: Courses; reconfigure student projects
.. index:: Reconfigure student projects
.. index:: Courses; re-send email invitations
.. index:: Re-send student email invitations

**Reconfiguring student projects and re-issuing email invitations.**
To ensure student projects have correct students and TA's, titles and descriptions, click `Reconfigure all projects`.
Doing so will also resend email invitations to students who have not already signed up for CoCalc.

.. figure:: img/teaching/course-reconfigure.png
     :width: 60%
     :align: center

     "Reconfigure all projects" at lower right in Configuration

#########################
What do the Students Get?
#########################

On being invited to a course, each student will have a project created for them in their CoCalc account that corresponds to that course. Each project will have you and the course Teaching assistants set as collaborators.

The student's course project will have its own individual quotas set for disk storage, internet access and so on (e.g. students get 1GB of RAM). These quotas will be the standard set of quotas that everybody gets with free CoCalc projects.

You can learn more about upgrades and quotas in the :ref:`next chapter <course-upgrading-students>` or the :doc:`upgrade-guide`.
