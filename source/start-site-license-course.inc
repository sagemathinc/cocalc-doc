.. index:: Site licenses; for courses (setup)


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


4. Install your license in the .course file.
--------------------------------------------

- Open the ``.course`` file and click "Configuration."
- Check the box for "You or your institute will pay for this course".
- Click "Upgrade using a license key...".
- Paste in your license key and click "Save". You will see additional text where you entered the license key, indicating which upgrades will be applied and the maximum number of simultaneous running projects that can use this license.

.. image:: img/teaching/site-lic-course-config.png
     :width: 85%
     :align: center


5. Restart the teaching project.
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
