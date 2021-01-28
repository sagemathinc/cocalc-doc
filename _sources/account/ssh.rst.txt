.. index:: Account Tab; SSH keys
.. _account-ssh:

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
=========

``SSH keys``

Add an SSH key
================

``copy/paste`` your ssh key