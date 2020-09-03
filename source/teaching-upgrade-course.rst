
.. _course-upgrading-students:

=============================
Upgrading Student Projects
=============================


The **Configuration** tab of a **.course** file allows you to upgrade students' course projects in two ways, indicated by the checkboxes in the image below:

.. image:: img/teaching/upgrading_students.png
     :width: 75%
     :align: center


.. contents::
   :local:
   :depth: 2

.. index:: Upgrading students; students pay
.. _course-students-pay:

----------------------------------------------------
Students pay for upgrades
----------------------------------------------------

You can request that the students pay a one-time fee of $14 for four months.
This will move their projects to members-only hosts and enable full internet access.

If you click "Students will pay for this course", another checkbox appears, "Require that students upgrade...":

.. image:: img/teaching/students-pay-2.png
     :width: 50%
     :align: center


When you check that checkbox, a calendar form opens. The default is to require students to pay within one week, but you can change the deadline. Select a different date if you want, or leave it at the default, and click "Close".

.. image:: img/teaching/students-pay-3.png
     :width: 50%
     :align: center

To continue from the perspective of your students,
read the :ref:`instructions for students to pay for a course <student-pay-for-course>`.

**Can we mix free and upgraded student projects?**

Yes.
Just set the due date by which the students have to pay to be at the end of the course.
Give them the opportunity to pay for an upgrade for the first few weeks (say),
then just unclick the student pay checkbox and thus no longer requiring them to pay at all.
In short, whether they have to pay or not is something you can change at any time,
they have a grace period before being required to pay,
and you can change any of these settings at any time.


.. index:: Upgrading students; institution pays
.. _inst-pays:

--------------------------------------------
Teacher or institution pays for upgrades
--------------------------------------------

.. note::

    CoCalc now supports site licenses in addition to the upgrade system described in this section.
    Licenses greatly simplify managing student upgrades, especially when dealing with multiple courses or sections.
    See :ref:`Setting up a Course with a Site License <site-license-course-setup>` for more information.
    Contact us at `help@cocalc.com <mailto:help@cocalc.com">`_ if you are interested in a site license.

Assuming you are an instructor and want to setup everything for a course,
here are the rough steps to **pay for upgrading your students' projects**.

**Background:** The course purchase option provides you with upgrades for *your account*,
but you then distribute these upgrades to all student projects in your course
(these projects are automatically created for the course).
The students then fully benefit from using these upgraded projects.

In your account settings there are two methods to upgrade your course:

1.  The tab "Licenses" lets you order "license keys". They allow you to specify exactly the number of student projects and upgrades. This is the newer and preferred method. Read more in :ref:`here <site-license-course-setup>`.

2.  Next to the "upgrades" page, there is a tab :ref:`Purchases <account-subscriptions>`. In that tab, enter your payment information and purchase one or more course packages. `We can help you <mailto:help@cocalc.com>`_ if you are not sure which one to buy (it depends on the size of the class, your needs, etc) or if you need us to process a format purchase order (PO), etc.

Once you purchase the course upgrades,
go to the project where you created the course and **open the .course file**.
In that interface, where you can add the students, etc.
there is also **a tab called "Configurations"** (next to "Students", "Assignments", etc.).

Current pricing is available at https://cocalc.com/policies/pricing.html
which at the time of writing ranged from a **total** of about $7 to $14 per student for a 4 month course.
The price per student varies according to the size of the student cohort.
You get significant per-student discounts when you buy in bulk.

... and after selecting that "you/your institution pays",
you can proceed to distribute the upgrades of the course package here:

.. image:: img/teaching/upgrading_students2.png
     :width: 75%
     :align: center

Clicking "Adjust upgrades..." lets you allocate any available upgrades in your account.

Entering initial student upgrades
=================================

The following screenshots assume the instructor has purchased a One Week Standard Extra Small subscription, with upgrades for 10 projects, and applied upgrades to the TEACHING project, leaving upgrades for 9 student projects.
Two students have been added to the "MATH 101" .course file.

After clicking `Adjust upgrades...` as shown above, this is what the instructor sees:

.. image:: img/teaching/inst-pay-01-no-upgr.png
     :width: 50%
     :align: center

.. index:: Member Hosting;student upgrades

The instructor enters the usual upgrades *per student* for Standard subscriptions:

* Member Hosting: ✓
* Internet Access: ✓
* Idle Timeout: 2.4 hours
* Shared RAM: 1000 MB
* Shared CPU: 1 core

.. image:: img/teaching/inst-pay-02-add-upgr.png
     :width: 50%
     :align: center

After checking that everything looks right, the instructor clicks `Apply changes`.

.. _adding-student-upgrades:

Adding more student upgrades
============================

Now suppose a third student arrives after the previous upgrades have been applied. The instructor again opens the .course file, selects Configuration, and clicks `Adjust upgrades...`. Note the message at the bottom of the dialog that only one of the student projects will be upgraded.

*Without making any changes to the numbers entered,* the instructor again clicks `Apply changes`. The third student project is now upgraded.

.. image:: img/teaching/inst-pay-06-before3rd.png
     :width: 50%
     :align: center

What the student sees
============================

Here is what a student will see upon opening his/her student project for the course.

First, this is what is seen if the instructor has not yet applied upgrades for the student project. Note the red banner warning that the project is not upgraded.

.. image:: img/teaching/inst-pay-03-student-before.png
     :width: 50%
     :align: center

Second, this is what is seen if the instructor has added typical upgrades for a Standard course. The exact amounts added will vary for different plans. For example, Basic courses include upgrades for Member Hosting and Internet Access, but not for other resources. Note in the Projects toolbar at very top, that the project is restarting. That is because upgrades were applied by the instructor moments ago.

.. image:: img/teaching/inst-pay-04-student-after.png
     :width: 50%
     :align: center
