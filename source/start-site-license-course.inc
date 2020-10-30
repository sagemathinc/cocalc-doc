.. index:: Site licenses; Courses; setup


For the best results, follow these steps when setting up a course with a site license:


1. Obtain a license key.
------------------------

In your account settings, open the tab "Licenses". There, you find a button named "Buy a license…".

A license key is a hexadecimal uuid string. It looks like this::

    78caa80a-4ddf-11ea-a5e5-53e10ace7b7b

2. Create a teaching project.
-----------------------------

Create a CoCalc project you will to use to manage the course.

.. image:: img/teaching/site-lic-course-create-proj.png
     :width: 85%
     :align: center


3. Create a .course file.
-------------------------

Use the ``(+)New`` button to create a ``.course`` file for managing your course.

.. image:: img/teaching/site-lic-course-create-crse.png
     :width: 85%
     :align: center


4. Install your license(s) in the .course file.
-----------------------------------------------

- Open the ``.course`` file and click "Configuration."
- Check the box for "You or your institute will pay for this course".
- Click "Upgrade using a license key...".
- Paste in your license key and click "Save". You will see additional text where you entered the license key, indicating which upgrades will be applied and the maximum number of simultaneous running projects that can use this license.
- You can apply more than one license. After you install the first license, a new button will appear, "Add another license key (more students or better upgrades)". Click this to add more licenses, one at a time.

.. image:: img/teaching/site-lic-course-config.png
     :width: 85%
     :align: center

.. index:: Site licenses; Courses; strategy

5. License strategy (multiple licenses only)
---------------------------------------------

If you have applied two or more licenses to a course, a dialog appears
for choosing how those licenses are combined. The two options are:

- **Maximize number of covered students:** apply one license to each project associated to this course (e.g., you bought a license to handle a few more students who added your course). This is the default.
- **Maximize upgrades to each project:** apply all licenses to all projects associated to this course (e.g., you bought a license to increase the RAM or CPU for all students).

.. image:: img/teaching/license-strategy.png
     :width: 85%
     :align: center


6. Restart the teaching project.
--------------------------------

In project Settings (wrench icon), restart your project so that the license will be applied. Click "Restart Project..." then click "Yes, restart project" in the confirmation dialog.

.. figure:: img/teaching/site-lic-course-restart-pre.png
     :width: 85%
     :align: center

     license entered in course Configuration; about to restart teaching project


In project Settings, within a few seconds you will see that the teaching project is being upgraded. The warnings about running on an unpaid server will be gone, and you will see your license upgrades applied to the teaching project, including Member Hosting and Internet Access.

.. figure:: img/teaching/site-lic-course-restart-post.png
     :width: 85%
     :align: center

     project settings after restarting teaching project



License setup done!
-------------------------------

You have just completed the steps to create a teaching project, upgrade the teaching project, and create a .course file. You are ready follow steps below to :ref:`add TAs <teaching-add-ta>`, if any, :ref:`add students <adding-students>`, and set up :ref:`handouts <create-handout>` and :ref:`assignments <create-assignment>`.

.. index:: Site licenses; Courses; adding capacity

Adding capacity
---------------

After you have courses up and running, you may discover that you need to provide for more students,
or increase computing resources on student projects. You can do either of those by obtaining
additional licenses and applying them as shown above.
If you need more flexibility than the available strategies offer,
contact CoCalc support at help@cocalc.com.