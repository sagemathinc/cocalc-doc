.. index:: Projects; recover deleted
.. _missing-project:

==================================================
Recovering a Project That Was Accidentally Deleted
==================================================

###############################################
I think I deleted my project! What do I do?
###############################################

First, relax -- there is currently (as of Feb 2019) no way for you to **permanently** delete a project in CoCalc (we do `plan to implement this <https://github.com/sagemathinc/cocalc/issues/262>`_). It is also almost impossible to delete data from a project, too.

##################################################################
I clicked the x next to my project at the top, and now it is gone.
##################################################################

If you close a project, just click on the "Projects' tab in the upper right, then find your project in the list and open it.  Done.

###########################################################################
I (or a collaborator) clicked on "Delete Project" in Project Settings.
###########################################################################

In this case, click "Deleted" at the top of the Projects page to show all deleted projects, then find your project, click on it, go the project settings page, and **undelete** your project.  Your project will then be listed as normal.

.. index:: Projects; missing

==================================
What To Do If a Project Is Missing
==================================

##################################################################
I logged in and my projects are gone or empty!
##################################################################

If your projects are all gone, then really you have somehow signed in using a **different account**.   You can sign into CoCalc in many ways:
  - using an email address and password that you setup specifically for CoCalc
  - by clicking on one of the Google, Twitter, Github or Facebook buttons.

If you sign in, and your projects are all gone, then what really happened is that you've created a new account using a different sign in method.   Try signing in other ways.  If you really, really can't figure out what is going on, email help@cocalc.com, tell us as much as you can about yourself and how you first made an account, and we'll sort things out.  *For example, every few days somebody emails help@cocalc.com because they make a typo in their email address when creating their account, and we hunt it down for them.*

If your project is empty, then again you may have signed in using the wrong account and probably are looking at a different project. Maybe you made another one with the same name.  See above.


##################################################################
My files are really gone. Help!
##################################################################

Don't worry -- CoCalc makes extensive backups of all your work, and they are fully accessible to you.

1. Backups: Click the "Backups" button in the upper right of the Files listing.  You'll find many complete backups of ALL files in your project at various points in time.  These backups are made periodically (at most every 20 minutes), and old backups are deleted.

.. index:: TimeTravel

2. The Project Log and TimeTravel: Try checking the log by clicking on the "Log" button in your project.  The Log lists every file opened in your project, and if you click on a link, then click TimeTravel, you can go back and view any version of that file, even if it was deleted.  You can then restore this past version.  These backups are made *every few seconds*, and these old backups are never deleted (unless you explicitly write to us and ask us to delete them).

Unfortunately, there's some very small chance that somehow your files really did get deleted, that they are not backed up as above, and it really is entirely the fault of CoCalc. (As far as we know, it's been a long time since this has happened to anybody.) In this case, create a support ticket or email help@cocalc.com, and we'll figure out what is wrong, and (if possible) restore everything from a recent backup.  Make sure to tell us as much as you remember about your files (e.g., their names, when you last worked with them, etc.).
