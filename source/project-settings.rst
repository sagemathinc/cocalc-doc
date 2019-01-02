================
Project Settings
================

All about the **Project Settings** tab.

.. contents::
   :local:
   :depth: 2


Title and description
---------------------

The text for **Title and description** for a project can be changed at any time.

.. image:: img/project-settings/title-and-desc-a.png
     :width: 50%

Title and Description fields are both used when searching for matching text under **Projects**.
If you have several projects, it can help to add hashtags to your project descriptions
for topics you want to return to quickly.

.. figure:: img/project-settings/project-match.png
     :width: 60%

     *searching for "astro" in project title & description*

.. _project-upgrades:

Project usage and quotas
------------------------

Why Add Upgrades?
"""""""""""""""""

There are many reasons that you might want to have an upgraded project.

* To give your project access to the internet. For example,
   * To download a software package from the internet.
   * To use Github/Bitbucket/Gitlab with your project.
   * To download datasets into your project.
   * To connect to your project with SSH.
* To get extra storage space (both RAM and disk space).
* To get more compute resources.
* To have a higher idle timeout threshold. (See `What is an idle timeout? <https://github.com/sagemathinc/cocalc/wiki/AllAboutProjects#idle-timeout>`_.)

You can share upgrades with any project that you are a collaborator on. You must be a collaborator (or owner) to update a project.

For details on paid subscriptions, see `Subscription and Pricing Information <https://cocalc.com/policies/pricing.html>`_.
Paid subscriptions start at \$14 per month.

View Current Resources
""""""""""""""""""""""

You can view allocated upgrades and current resource use under `Project usage and quotas`.
Here's an example for a project with no upgrades added (note the warning banner that
appears if the project does not have Member Hosting or Internet Access):

.. image:: img/project-settings/before-upgrade.png
     :width: 60%

Adjust Quotas
"""""""""""""

When you click `Adjust Quotas...`, a dialog like the following appears. The screenshot shows numbers
for a project that has not been upgraded.
Available upgrades show what the numbers would be if you just purchased a Standard Plan and
have not applied any upgrades yet:

.. image:: img/project-settings/add-upgrades-standard.png
     :width: 60%

You can enter any values that do not exceed available upgrades. This example continues
by adding as much in the way of resources as possible to the current project.
You can remove upgrades at any time and apply them to other projects.

Max All Upgrades
""""""""""""""""

Clicking `Max All Upgrades` will add as much as possible from available upgrades:

.. image:: img/project-settings/apply-max.png
     :width: 60%

Save Changes
""""""""""""
Then clicking `Save Changes` will apply the changes and restart the project if settings have changed:

.. image:: img/project-settings/max-added.png
     :width: 60%

Hide or delete project
----------------------

Next in the Project Settings window is the section for hidden and deleted projects,
which do not appear in the normal project list
(the list you get when you click `Projects` at upper left).

If the current project is neither hidden nor deleted, you will see this:

.. image:: img/project-settings/hide-or-delete.png
     :width: 60%

Hidden vs. Deleted projects
"""""""""""""""""""""""""""

If you delete a project, then you delete it for everyone---for all your collaborators. The good news is that this can be undone.

Alternatively, if you hide a project, then you will not see it in your projects listing, but your collaborators are unaffected.

Hiding a project
""""""""""""""""

If you click `Hide Project`, the button changes:

.. image:: img/project-settings/hidden.png
     :width: 60%

And now if you click the `Projects` button at upper left, you will have a checkbox
that lets you view hidden projects. The checkbox only appears if there are hidden projects.

.. image:: img/project-settings/show-hidden.png
     :width: 60%

Clicking `Unhide Project` instantly makes the project visible in the normal project list again.

Deleting a project
""""""""""""""""""

*Note: No files are actually deleted by this operation.
Only visibility of the project in the project list is changed.
If you need to permanently delete information that you
accidentally copied into a project, contact help@sagemath.com*

If you click `Delete Project`, the button changes:

.. image:: img/project-settings/delproj1.png
     :width: 60%

Click `Yes, please delete this project` to confirm, and the screen changes again:

.. image:: img/project-settings/delproj2.png
     :width: 60%

Note the warning banner that appears at the top.

The project will not appear in the normal project list for you and all collaborators on the project.

And now if you click the `Projects` button at upper left, you will have a checkbox
that lets you view deleted projects. The checkbox only appears if there are hidden projects.

.. image:: img/project-settings/show-deleted.png
     :width: 60%

Clicking `Undelete Project` instantly makes the project visible in the normal project list again
for you and all collaborators on the project.

Hidden and Deleted projects
"""""""""""""""""""""""""""

A project can be both hidden and deleted. In that case, you will need to check both
`Deleted` and `Hidden` boxes in the `Projects` list to see the project.

.. image:: img/project-settings/deleted-and-hidden-a.png
     :width: 60%


SSH Keys
--------

For addtional detail, see the blog posting `Using SSH with CoCalc <http://blog.sagemath.com/cocalc/2017/09/08/using-ssh-with-cocalc.html>`_.

You can connect to a CoCalc project from your local desktop using `SSH`_ (Secure Shell) and you can upload/download files between your computer and CoCalc using the SSH protocol, with ``scp`` and ``rsync`` command line tools. You must have owner or collaborator status on a project for SSH access to be permitted.

When logging into a project with ssh, make sure the project is running. If the project is stopped, or has been restarted within the last 20 seconds or so, you may get a message of 'Permission denied'.

SSH authentication uses a pair of keys, a private key and a public key. Each key is stored in a separate file. For example, a private key might be in the file ``id_ed25519`` and the matching public key in ``id_ed25519.pub``. In general, private keys are not distributed, while public keys are uploaded to remote systems.

On OS X, and Linux, key pairs are stored in ``~/.ssh``, where ``~`` indicates your user's home directory. Use the ``ssh-keygen`` command to generate a key pair. (You can do ``man ssh-keygen`` from a terminal for details on the command.)

*NOTE: CoCalc does not support manual editing of the authorized_keys file server for SSH authentication.*

Configuring SSH Keys for a Single Project
"""""""""""""""""""""""""""""""""""""""""

.. highlight:: none

This section assumes you have created an SSH key pair as described above.

#. Open the project Settings tab (wrench icon) for the project you want to access.
#. Look for the section "SSH Keys" at lower left.

   .. image:: img/project-settings/usernameathost.png
        :width: 50%

#. Click "Add an SSH Key".
#. Enter a title for the key in the Title field. Specify a title that is meaningful to you for the key pair you are using, for example "Sample Key for TESTPROJ".
#. Copy the public key into the Key field. To do this, open the file for your public key on your local computer. For example, if you are using macOS or Ubuntu, you could open a terminal and type something like the following, depending on the name of your public key file::

      cat ~/.ssh/id_ed25519.pub

   Use your mouse to select the contents of the key file, then copy and paste it into the Key area.
#. Click "Add SSH Key". Your key is now saved for that project.

   .. image:: img/project-settings/addingprojkey.png
        :width: 50%

#. The user for the SSH connection is the project id *without the hyphens* (why? because the project id is not a valid Linux username). The hostname is ``ssh.cocalc.com``. Look for "Use the following username@host:" in the "SSH Keys" section of project status for a string you can copy and paste. For example, if the Project id is::

      2507078b-6e5b-43da-809a-0073f1196181

   then the SSH username@host will be::

      2507078b6e5b43da809a0073f1196181@ssh.cocalc.com

#. To login from your local computer, use a command equivalent to the following::

      ssh 2507078b6e5b43da809a0073f1196181@ssh.cocalc.com

#. On macOS or Linux, you can specify a host alias in ``~/.ssh/config`` to avoid having to explicitly pass the project id as above. For example, the following lines in ``~/.ssh/config``::

      Host CCPROJ
          Hostname ssh.cocalc.com
          User 2507078b6e5b43da809a0073f1196181
          IdentityFile ~/.ssh/id_ed25519

will allow you to log into the your project from your local computer with the command::

      ssh CCPROJ

You can also specify a single SSH key pair under :doc:`account-settings` to use with all your projects.

.. highlight:: default

Current collaborators
---------------------

Add new collaborators
---------------------

Project control
---------------

Sage worksheet server
---------------------

Plain Jupyter server
--------------------

JupyterLab server
-----------------


.. |header| image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/16/header.png

.. _ssh: https://help.ubuntu.com/community/SSH
