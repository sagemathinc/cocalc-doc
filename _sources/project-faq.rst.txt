.. index::
    Projects; FAQ
    FAQ; Projects

.. _projects-faq:

===============
Projects FAQ
===============

This FAQ guide answers questions about :doc:`Projects <project>`.

Upgrades/quotas, billing, and pricing related questions covered in :doc:`billing`.

.. index::
    Git; with projects
    GitHub; with projects
    GitLab
    Bitbucket

Can I work with Git – including GitHub, Bitbucket, GitLab, etc.?
============================================================================

Git and various other source control tools are installed and ready to use via the :doc:`terminal`.
But, in order to also interoperate with sites hosting Git repositories,
you have to :doc:`purchase a plan <upgrade-guide>` giving you "internet upgrades"
and then applying this upgrade to your project.

**More information**: :doc:`CoCalc Git Howto <howto/git>`


.. index::
    Projects; Download all files

How can I download my files?
==================================================

- You can download each file individually via the "Files" interface.
  Select the file and click the "Download" button.

- It is also possible to create an archive for a directory or all files.
  For that, create a "Terminal"-file and issue one of these commands:

  - ZIP archive (Windows): ``zip -r9 "[filename].zip" [directory-name...]``
  - Tarball (Unix-like): ``tar cjvf "[filename].tar.bz2" [directory-name...]``

  (Replace ``[filename]`` with the actual filename and ``[directory-name]``
  by one or more filenames or directory names.)
  Afterwards, download the archive as explained above.


.. _backup:

Are my files backed up?
=============================

All files in every project are snapshotted every couple of minutes.
You can browse your snapshots by clicking the **"Backups"** link to the right of the file listing.
Also, CoCalc records the :doc:`history of all edits <time-travel>` you or your collaborators make to most files,
and you can browse that history with a slider by clicking on the "Time Travel" button (next to save) in files.
We care about your data, and also make offsite backups periodically to encrypted USB
drives that are not physically connected to the internet.


Can I close my web-browser at any time?
===========================================

**Yes!**

When you close your web-browser, all your processes and running sessions continue running.
You can start a computation, shut down your computer, go somewhere else,
sign in on another computer, and continue working where you left off.

The only reasons why a project or process stops are that it hits its :ref:`idle timeout <idle-timeout>`,
was killed after :doc:`using too much memory <howto/low-memory>`,
crashed due to an exception, or the server had to reboot.

.. index::
    SSH host key
    SSH fingerprint
.. _ssh-host-key:

What's the fingerprint of the SSH gateway's host key? 
=========================================================

How can I make sure to connect to CoCalc?
As of September 2019, the SSH host key's fingerprint is::

    2048 MD5:b1:92:cc:67:ee:b8:ff:65:48:93:e6:f1:72:93:59:b0 cocalc@kucalc-k3-ctl (RSA)

You can see it when you try to connect via::

    ssh -v -o FingerprintHash=md5 ssh.cocalc.com

Somewhere in the output it says::

    debug1: Server host key: ssh-rsa MD5:b1:92:cc:67:ee:b8:ff:65:48:93:e6:f1:72:93:59:b0

**Note:** this key could have changed due to technical reasons. Please contact us at help@cocalc.com if you suspect a discrepancy. 
