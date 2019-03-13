
*****************
Account Tab
*****************

The Account Tab is where you manage settings, subscriptions, and resources across your projects. There are 5 tabs under under Account Tab.

.. figure:: img/account-settings/account-subtabs.png
     :width: 80%
     :align: center

     ..

.. index:: Account Tab

.. contents::
   :local:
   :depth: 1


============
Preferences
============

.. index:: Account Settings
.. _account-settings:


Account settings
----------------

.. figure:: img/account-settings/account-settings.png
     :width: 80%
     :align: center

     ..

First and Last Name
^^^^^^^^^^^^^^^^^^^^

Email address
^^^^^^^^^^^^^^^

Newsletter
^^^^^^^^^^^^^

Password
^^^^^^^^^^

API key
^^^^^^^^

.. index:: Sign out of CoCalc, Log out of CoCalc

Sign out
^^^^^^^^^^

This is where you log out of your CoCalc session.

Linked accounts
^^^^^^^^^^^^^^^^^


Other settings
----------------

Profile
----------------

Editor settings
----------------

Terminal settings
-------------------

=============================
Subscriptions/Course Packages
=============================

.. figure:: img/account-settings/subscr-select.png
     :width: 80%
     :align: center

     *order form displays if no subscriptions are active*

.. figure:: img/account-settings/subscr-display.png
     :width: 80%
     :align: center

     *active subscriptions, if present, are displayed*

Payment methods
----------------

Subscriptions and course packages
----------------------------------

Invoices and receipts
----------------------

========
Upgrades
========

All upgrades
--------------

``Upgrades that you get from your subscriptions and course packages``

Applied upgrades
-----------------

``Upgrades you have applied to projects``


========
SSH keys
========

This section assumes you have created an SSH key pair as described in :ref:`SSH Keys <ssh-keys>`.

Click the gear icon next to your name at upper right to open Account Settings.
Choose the tab "SSH Keys" and note the form for adding a key at right.
Enter a title for the key in the Title field. Specify a title that is meaningful to you for the key pair you are using, for example John's CoCalc Key.
Copy the public key into the Key field. To do this, open the file for your public key on your local computer. For example, if you are using macOS or Ubuntu, you could open a terminal and type something like the following, depending on the name of your public key file.
cat ~/.ssh/id_ed25519.pub
Use your mouse to highlight the contents of the key file, then copy and paste it into the Key area. saving the entry.

Click Add SSH Key. Your key is now saved for that account and will work for all projects for which that account has owner or collaborator status.
As with the previous section, the user@hostname string needed for the ssh command consists of the project id with hyphens removed for the user, and 'ssh.cocalc.com' for the hostname, and can be found just below the caption Use the following username@host: in the 'SSH Keys' section of project status tab.

SSH keys
---------

``SSH keys``

Add an SSH key
----------------

========
Support
========

Support tickets
----------------


