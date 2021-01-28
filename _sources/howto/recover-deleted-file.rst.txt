.. index:: Files; recover deleted
.. index:: Recover deleted file
.. index:: Backups; recover deleted file
.. index:: TimeTravel; recover deleted file

.. _recover-deleted-file:

==================================================
Recovering a Deleted File
==================================================

Don't worry -- CoCalc makes extensive backups of all your work, and they are fully accessible to you.


1. **The Project Log and TimeTravel.**
Click on "Log" in your project. You can type "delete" in the Log search box to filter for deletions. Then click on the filename in the log. You'll get a dialog asking if you want to recover the file -- click OK.
Use :doc:`TimeTravel <../time-travel>` to go back to the version you want and click "Revert".
TimeTravel backups are made *every few seconds* and are never deleted (unless you explicitly write to us and ask us to delete them).


2. **Backups.** Click the "Backups" button in the upper right of the Files listing.
You'll find backups of ALL files in your project at various points in time.
These backups are made periodically (at most every 20 minutes), and old backups are deleted.


Unfortunately, there's a small chance that somehow your files really did get deleted, that they are not backed up as above, and it really is entirely the fault of CoCalc. (As far as we know, it's been a long time since this has happened to anybody.) In this case, create a support ticket or email help@cocalc.com, and we'll figure out what is wrong, and (if possible) restore everything from a recent backup.  Make sure to tell us as much as you remember about your files (e.g., their names, when you last worked with them, etc.).
