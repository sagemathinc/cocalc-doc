
.. _course-upgrading-students:

Upgrading Student Projects
=============================


The **Configuration** tab of a ``.course`` file allows you to upgrade students' course projects in two ways:

.. figure:: img/teaching/upgrading_students.png
     :width: 75%
     :align: center
     :alt: Choices for Upgrading Student Projects
     
     Choices for Upgrading Student Projects


.. contents::
   :local:
   :depth: 2

.. index:: Upgrading students; students pay
.. _course-students-pay:

----------------------------------------------------
Students Pay For Upgrades
----------------------------------------------------

You can request that the students pay for CoCalc resources needed for the course. You set exactly which resources are needed, as well as the start and end dates.

.. note::

  As of August, 2023, students in a course must buy the license specified for that course. Upgrading the student project in some other way is not sufficient.


1. Instructor configures the payment option
-----------------------------------------------

In the course **Configuration** tab, choose **Students pay directly** and adjust parameters as needed:

.. figure:: img/students_pay_directly.png
     :width: 75%
     :align: center
     :alt: Students Pay Directly
     
     Students Pay Directly

.. hint::

  If you are running multiple sections of the same course, you probably want to configure these licenses to be exactly the same including the dates, so that students in different sections pay exactly the same fee.


2. Students see a payment banner
-------------------------------------------------

When the students open their course projects, they will see a banner at the top:

.. figure:: img/student-pay-2b.png
     :width: 75%
     :align: center
     :alt: Payment Banner

     Payment Banner

3. Students make payments
-------------------------------------------------

After clicking the banner, they will see a button allowing them to pay for the course:

.. figure:: img/student-pay-3b.png
     :width: 75%
     :align: center
     :alt: Student Payment

     Student Payment


.. index:: Upgrading students; institution pays
.. _inst-pays:

--------------------------------------------
Teacher or Institute Pays for Upgrades
--------------------------------------------

You can buy a license that will upgrade all student projects. The same license can be used to upgrade the main course project as well.

1. Configure the payment option
-----------------------------------------------

In the course **Configuration** tab, choose **You or your institute will pay for this course**:

.. figure:: img/institute_pays.png
     :width: 75%
     :align: center
     :alt: Institute Pays
     
     Institute Pays


.. _install-course-license:

2. Apply a license to the course
-----------------------------------------------

If you already have a license for this course, click **Upgrade using a license key...**. Otherwise use **Buy a license...** button below, get a license, and come back to the course.

Once you successfully apply your license key, you will see its details including the maximum number of simultaneously running projects:

.. figure:: img/institute_license_applied.png
     :width: 90%
     :align: center
     :alt: Applying a License
     
     Applying a License

.. warning::

    You must use a license with at least the same limit of running projects as the number of enrolled students. (Plus 2 if you use the same license for the instructor project as well as the shared project.) Otherwise some students may not be able to get the upgrades, preventing them from completing their work.
    
.. hint::

    You can easily adjust the number of projects your license can upgrade at any time if your enrollment number changes - click on the license description and then **Edit license...** button!
    

3. Apply the course license to the instructor project (optional)
----------------------------------------------------------------

You can use the same license that you're using for the students to upgrade the instructor project. This will count against the maximum number of running projects for the license. With this option, if you have 20 students and plan to run your instructor project at the same time as all 20 students, your course license should allow for at least 21 projects.

If using this option, click **Upgrade instructor project** and then **Save**:

.. figure:: img/upgrade_instructor_project.png
     :width: 90%
     :align: center
     :alt: Upgrade Instructor Project
     
     Upgrade Instructor Project

Then you have to manually restart the project to apply the license: click **Settings** and then **Restart Project...**

.. hint::

    While it is convenient to use the course license for the instructor project, you should consider if having more RAM or a longer timeout would be beneficial to you. In that case you can buy a more powerful (and more expensive) license just for one project and apply it in project settings.
    

4. What do students see
-----------------------

Here is what a student will see upon opening the student project for the course.

First, this is what is seen if the instructor has not yet applied a license for the course. Note the red banner warning that the project is not upgraded.

.. image:: img/teaching/inst-pay-03-student-before.png
     :width: 50%
     :align: center
     :alt: Student project quotas before applying course license.

Second, this is what is seen if the instructor has added a license in the course Configuration tab. The exact resource amounts will vary depending on the license.

.. image:: img/teaching/student-license-view.jpg
     :width: 50%
     :align: center
     :alt: Student project quotas after applying course license.


.. index:: Site licenses; course strategy
.. _license-strategy:

5. License strategy (multiple licenses only)
---------------------------------------------

.. warning::

    Using multiple licenses for a course was necessary before it was possible to edit an existing license. Now using multiple licenses is discouraged.

If you have applied two or more licenses to a course, a dialog appears
for choosing how those licenses are combined. The two options are:

- **Maximize number of covered students:** apply one license to each project associated to this course (e.g., you bought a license to handle a few more students who added your course). This is the default.
- **Maximize upgrades to each project:** apply all licenses to all projects associated to this course (e.g., you bought a license to increase the RAM or CPU for all students).


----------------------------
Problems with Licenses
----------------------------

If a license does not seem to be correctly applied to a student project, first check that the student project has been restarted since adding the license. If there is still a problem, see :ref:`license-errors`.



.. index:: Site licenses; adding capacity to course

-------------------
Adding Capacity
-------------------

After you have courses up and running, you may discover that you need to provide for more students,
or increase computing resources on student projects. You can do this by editing your license at any time!


---------------------------------------
Teaching with Compute Servers
---------------------------------------

If CoCalc projects are not sufficient for your needs, e.g. because you need GPUs or more CPU cores, you can consider :ref:`teaching_with_compute_servers`!


--------------------------------------------
Charges for Paid LLMs
--------------------------------------------

Just as other users, students are free to use CoCalc :doc:`ai`. If they want to use paid LLMs, they will have to put some money on their accounts. If *you* want your students to work with advanced LLMs and *you* want to pay for that, you can use :ref:`credit-vouchers` to distribute funds, similar to :ref:`teaching_with_compute_servers`. If, on the other hand, you want to discourage students from using AI, you can turn it off for their projects, see :doc:`restrict-student-projects`.

