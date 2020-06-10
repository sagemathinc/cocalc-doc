=====================
Course Management
=====================

No matter what you've added in the instructor's view of the course, the students will not see any files until you explicitly assign them.

.. contents::
   :local:
   :depth: 2

.. index:: Courses; create handout
.. _create-handout:

Create a new Handout
===============================

A handout consists of a folder that contains one or more files to be distributed to your students.

Create a folder called **Handouts** in the root directory of your course project. Within this folder create a subfolder called, say, **Handout1** and populate it with one or more files for the handout. These files can be anything - text, Markdown, code, pdf, and may contain subfolders.

Open the **.course** file and click on the **Handouts** tab

.. image:: img/teaching/handout-course.png
     :width: 100%

Type **handout** in the search box on the right hand of the screen and press enter. Note that search is case-insensitive.

The system will look for any folders with **Handout1** in their path name and  return a set of options. Highlight the one you want and click on **Add selected handout**.

.. image:: img/teaching/find-handout.png
     :width: 100%

The new handout will be added to the list of handouts available for the course.

.. index:: Courses; create assignment
.. _create-assignment:

Create a new assignment
===============================


An assignment is a folder that contains one or more files that can be distributed to your students and collected at some future time for grading.

Create a folder called **Assignments** in the root directory of your course project.
Within this folder create a subfolder called, say, **Assignment1** and populate it with files that contains questions or problems for your students to answer. For example, an assignment can contain a Jupyter notebook and data files, with instructions for a programming exercise.

Open the **.course** file and click on the **Assignments** tab.
Enter **assignment1** in the search box on the right hand of the screen and press enter.

The system will return a list of folders with **assignment1** in their path name. Highlight the one you want and click on **Add assignment**.

.. image:: img/teaching/find_assignment.png
     :width: 100%

The new assignment will be added to the list of assignments available for this course.

.. image:: img/teaching/assignment_list.png
     :width: 75%

Assigning an assignment to students
======================================

Click on the assignment in the assignment list.
When the assignment opens, set the **Due** date. You can do this in the text area, or using the calendar and clock widgets to the right. Click on the **Assign** button to assign to all students in the course.

.. image:: img/teaching/send_assignment.png
     :width: 100%

Alternatively, you can assign just to individual students.

When an assignment is made to a student, a **copy** of the assignment folder will appear in their course project.

Advise the students that all work on the assignment should take place in this folder. Any work performed outside of this folder will not be collected.

Peer Grading
======================================

A very useful function for formative assessment is **peer grading**.
Use peer grading to randomly (and anonymously) redistribute collected homework to your students, so that they can grade it for you.

Within the assignment, click on the **Peer Grading** icon and follow the instructions to activate this feature.

.. image:: img/teaching/peer_grading_activation.png
     :width: 100%

Collecting assignments from students
======================================

After an assignment has been made, a **Collect** icon appears next to each student.
Clicking on one of these will make a copy of the student's assignment folder to your account.
The entire folder will be copied including any extra files the student may have created.

Alternatively, click on the **Collect** icon in the top row to collect from all students simultaneously.

.. image:: img/teaching/collect_assignment.png
     :width: 100%

You should make sure that your project has enough disk space to accommodate this.
It may be necessary to purchase an upgrade if you need more than the free allowance (currently 3GB per project).

Once the assignment has been collected, anything the student subsequently does in **their** copy will not be reflected in **your** copy.

If you click on the **Files** icon and go to the root directory of the course project, you'll see that a new folder will have been created with the name **[your_course_name]-collect**

.. image:: img/teaching/filelist_with_collect.png
     :width: 100%

Navigating within this folder, you'll find that it has a similar file structure to the original assignment.
For example, for this demonstration we had the structure `/assignments/Assignment1` which appears in the collected folder as `[your_course_name]-collect/assignments/Assignment1`.
Entering this folder will give a view of all students' versions of this assignment

.. image:: img/teaching/collected_assignments.png
     :width: 100%

The folder corresponding to each collected assignment will have been given a unique random name.
Navigating inside this folder, you will see all collected files along with a text file whose filename identifies the student.

.. image:: img/teaching/Identify_student.png
     :width: 100%

At this point, you can open and mark the student's returned assignment.

An easier interface for opening a student's collected assignment is via the **.course** file.
Simply click on the **Open** icon corresponding to the student you are interested in and you'll be taken to the folder described above.

.. image:: img/teaching/open_assignment.png
     :width: 100%

Grading
======================================

You are free to annotate the student's assignment in any way you like.
The student will get a copy of everything you do once you return it to them.

When working with Jupyter notebooks, I usually do my annotations in Markdown cells and surround my comments in HTML tags that colour the text red.
This allows the students to quickly identify my comments.

::

    <font color="red">Great work!</font>

.. image:: img/teaching/feedback.png
     :width: 50%

Once you've finished marking and commenting on the student's notebook, you can enter a grade via the **.course** file.
Click on the **Enter Grade** button to open up the grade entry text box and enter the grade.
This can be a number or any other string that makes sense for your course.

.. image:: img/teaching/Enter_grade.png
     :width: 100%

Exporting grades
======================================

It is possible to export grades for all assignments as either a .csv file or as executable Python code.
The **Export grades** function is available in the **Configuration** tab of the **.course** file.

.. image:: img/teaching/Export_grades.png
     :width: 66%

The .csv file format looks like this::

    # Course 'Autumn_2016_PHY001'
    # exported 2016-06-13T13:24:40.141Z
    Name,Email,"assignments/Assignment1","Notes"
    "Mike Croucher","some.email@sheffield.ac.uk","80",""
    "Mike_test ","some_other_email@sheffield.ac.uk","100",""
    "bar@sheffield.ac.uk","bar@sheffield.ac.uk","90",""
    "foo@sheffield.ac.uk","foo@sheffield.ac.uk","70",""

The corresponding Python code looks like this::

    course = 'Autumn_2016_PHY001'
    exported = '2016-06-13T13:26:19.407Z'
    assignments = ['assignments/Assignment1','Notes']
    students = [
        {'name':'Mike Croucher', 'email':'some.email@sheffield.ac.uk', 'grades':['80','']},
        {'name':'Mike_test ', 'email':'some_other_email@sheffield.ac.uk', 'grades':['100','']},
        {'name':'bar@sheffield.ac.uk', 'email':'bar@sheffield.ac.uk', 'grades':['90','']},
        {'name':'foo@sheffield.ac.uk', 'email':'foo@sheffield.ac.uk', 'grades':['70','']},
    ]

Returning an assignment to students
======================================

Once an assignment has been graded, the *Return* to student button appears.

.. image:: img/teaching/return_button.png
     :width: 100%

Clicking on this sends a copy of the graded assignment back to the student.
It appears in their assignments folder like this:

.. image:: img/teaching/returned_assignment.png
     :width: 100%

Note that the student now has both their original assignment **and** a copy of the returned, graded assignment.

Suggested course folder structure
==========================================

I tend to place course content in one of two categories:

* Content that you only push out to students (e.g. lecture notes, data)
* Content that requires pushing out and pulling back (e.g. assignments and homeworks)

The reason for splitting content in this way is to save on disk space.

When you push content out to the students, a copy is placed in their individual projects. When you pull it back for marking, a fresh copy of each student's assignment is made in **your** project. If the assignment contains large files, the lecturer's project can quickly run out of space for large classes.

Each project has 3GB of disk space provided for free, with more being provided by purchasing upgrades.

There are many ways one could organise a course in CoCalc but the following schema has proven to be useful for many people.


* notes/date1
* notes/date2
* ...
* assignments/date1
* assignments/date2
* ...
* data/xyz
* data/abc

This way, the students just see the following three folders in their course project.

* notes/
* assignments/
* data/

The **notes** and **data** folders contain content that you push to the students and **assignments** contains material that you also collect back from them.