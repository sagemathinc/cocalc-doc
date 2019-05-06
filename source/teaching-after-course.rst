.. index:: Courses; ending

=====================
After the Course Ends
=====================

Here are some suggestions on wrapping up after a course you managed with CoCalc comes to an end.

.. contents::
   :local:
   :depth: 2

.. index:: Courses; hide/delete projects
.. _hide-delete-student-projects:

Hide or Delete Student Projects
===============================

To keep the project list from becoming cluttered, an instructor may choose to hide or delete all student projects when a course ends. Student projects may be hidden using the :ref:`"Hide" batch operation <project_batch>` in the project list. Student projects may be deleted - which marks them as deleted for all students as well as the instructor - in the course file **Configuration** tab with the "Delete all Student Projects..." button, or with the :ref:`"Delete" batch operation <project_batch>` in the project list.

*NOTE: Upgrades to student projects may only be removed by the account that added them. If a course administrator initially upgraded student projects, then a
teaching assistant with a different account deletes student projects, the upgrades will remain on the deleted projects. See the next section to recover upgrades in this case.*

.. index:: Courses; recover upgrades
.. _recover-upgrades:

Recover Upgrades from Student Projects
=======================================

Upgrades applied to student projects may be re-used on other projects after the course ends. Upgrades remain valid until their expiration date.

To recover upgrades from student projects, i.e. to remove them from student projects and return them to the pool of available upgrades, the owner of the account that originally applied the upgrades can do a :ref:`"Remove Upgrades..." batch operation <project_batch>`, after selecting the desired projects with either search text or hashtag. Or, if student projects are to be deleted, the owner of the upgrades can open the course file **Configuration** tab and click "Delete all Student Projects...".

.. index:: Courses; access after end
.. _access-after-end:

Student Access After Course Ends
======================================

**Question:** My students have been asking whether they can keep using their CoCalc account after this course ends. I assume that their account **and projects** will remain active, but revert to the settings associated with a free account and projects. Is that correct? If not, is there anything they need to do to use their accounts in the future?

**Answer:** Yes, they will have full access, though they may need to take an extra step to ensure they can easily login.

The detail is how they are authenticated with CoCalc. For example, in case they exclusively use a Google account associated with your-college.edu, and the university revokes their account, they would be unable to access CoCalc without adding another access method.

For cases like that, instruct your students to **make sure they have a password set in their account settings**. Then, they can always access their course projects by accessing their account via an email address and password. Later, they can change their email address, while keeping access to their projects. In account settings, students can also associate their account with Facebook (or Github or Twitter), and login using one of those providers.

If the instructor has marked the student project Deleted, the student may still see the project in the project list by selecting the checkbox for Deleted projects.



