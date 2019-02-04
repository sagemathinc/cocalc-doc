================
Project Settings
================

All about the **Project Settings** tab.

.. contents::
   :local:
   :depth: 1


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


.. note::

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


.. index:: SSH Keys
.. _ssh-keys:

Setup SSH Keys
-----------------

Using SSH
"""""""""

For addtional detail, see the blog posting `Using SSH with CoCalc <http://blog.sagemath.com/cocalc/2017/09/08/using-ssh-with-cocalc.html>`_.

You can connect to a CoCalc project from your local desktop using `SSH`_ (Secure Shell) and you can upload/download files between your computer and CoCalc using the SSH protocol, with ``scp`` and ``rsync`` command line tools. You must have owner or collaborator status on a project for SSH access to be permitted.

When logging into a project with ``ssh``, make sure the project is running. If the project is stopped, or has been restarted within the last 20 seconds or so, you may get a message of 'Permission denied'.

SSH authentication uses a pair of keys, a private key and a public key. Each key is stored in a separate file. For example, a private key might be in the file ``id_ed25519`` and the matching public key in ``id_ed25519.pub``. In general, private keys are not distributed, while public keys are uploaded to remote systems.

On OS X, and Linux, key pairs are stored in ``~/.ssh``, where ``~`` indicates your user's home directory. Use the ``ssh-keygen`` command to generate a key pair. (You can do ``man ssh-keygen`` from a terminal for details on the command.)

*NOTE: CoCalc does not support manual editing of the authorized_keys file for SSH authentication.*

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

#. The user for the SSH connection is the project id *without the hyphens*. (Why? Because the project id is not a valid Linux username.) The hostname is ``ssh.cocalc.com``. Look for "Use the following username@host:" in the "SSH Keys" section of project status for a string you can copy and paste. For example, if the Project id is::

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

About collaborators
-------------------

Each CoCalc project has an owner and zero or more collaborators.
Owner and collaborators all appear in a project under the identity of "user" and home directory of ``/home/user``.
There is no difference in the Linux identity,
regardless of the CoCalc account that is signed in.
Owner and collaborators can read anything in the project, and write, delete, and modify anything except backups. They can add and remove other collaborators, but cannot remove the owner.

Although the owner and all collaborators appear in a project with the same
Linux user id, there are two ways to see *which CoCalc account* was used for certain actions in a project:

* The project activity log.
* Time travel for files edited using the CoCalc frame editor.

Current collaborators
---------------------

The "Current collaborators" section of the *Project Settings* page shows the names of the owner and all collaborators. Here you can remove collaborators, including yourself. It does not allow you to remove the owner.

Current collaborators are also shown in the *Projects* list. You can use the latter to remove yourself as collaborator from several projects at once.

.. image:: img/project-settings/current-collabs.png
     :width: 70%

.. _add-collaborators:

Add new collaborators
---------------------

At the **Add new collaborators** dialog, you can type in a person's name or email address. CoCalc will search its database of known users and show you possible matches.

#. After you select a name, don't forget to click "Invite User."
#. The user must accept the invitation to be added as a collaborator.

It is generally better to use an email address. The reason is that some CoCalc users have multiple accounts.

.. image:: img/project-settings/add-collabs.png
     :width: 70%

If there are no matches for an email address, then you can send an invitation for the user to start using CoCalc. You can modify the standard email. The default invitation has useful links to make it easier for the other person to start using CoCalc.

.. figure:: img/project-settings/email-invitation.png
     :width: 70%

     *customizing email invitation to new user*

Sometimes, you'd rather give someone read-only access. In CoCalc, this is called "sharing" with non-collaborators. See :ref:`share <ft-share>` for how to share a file.

Caution: if you are using CoCalc for course management with a .course file, add students under the **Students** tab of the .course file, and *NOT* as collaborators. That way, they get their own projects, separate from the instructor project. On the other hand, it is common practice to :ref:`add teaching assistants <teaching-add-ta>` as collaborators in the instructor project.

Project control
---------------

Here is a screen capture of the Project control section. Along with project statistics, it has two buttons and a menu, discussed below.

    .. image:: img/project-settings/project-control.png
         :width: 70%

Restart Project and Stop Project
""""""""""""""""""""""""""""""""

What happens when a project restarts?

* All computations will be stopped.
* **Good News:** You don't lose unsaved files.
* You do lose any information (state of variables/processes) in **RAM**.
* However, anything in files, as long as it's moved from the browser to the web servers (in most cases, at most a few seconds of information), is permanently saved to disk already in the database, and will not be lost.
* When the project starts back up, even if the files on disk are in an older state, the files you see yourself editing in your browser are new with nothing lost. Those files will then be updated on disc very shortly.
* On the other hand, project code, i.e. the CoCalc software environment, is updated.

To make all this happen, click "Restart Project...". Another button appears, to confirm the choice.

    .. image:: img/project-settings/project-restart-confirm.png
         :width: 70%

Click "Restart Project Server", and restart initiates.

    .. image:: img/project-settings/project-restarting.png
         :width: 70%

It normally takes about 30 seconds to restart a project. It may take another 10 seconds or so after the Files list is visible for terminal processes, etc. to be available.

You can also stop and restart a project in two separate steps. Why would you stop a project and then restart it, rather than simply restarting it in a single step?

* If you want CoCalc to move the project to another server, stopping it first and then restarting it allows CoCalc to select a different, possibly less-loaded server.
* If you don't want any of your project's processes to run until you explicitly restart the project, you have to stop the project.

Clicking "Stop Project..." causes the "Stop Project Server" button to appear, to confirm your choice:

    .. image:: img/project-settings/stop-project-confirm.png
         :width: 70%

.. index:: Software Environment
.. _software-environment:

Software Environment
""""""""""""""""""""""""

The CoCalc software environment is updated frequently. The collection of installed utilities, compilers, libraries, packages, etc. is called the *compute image*.

You can see a recent list of installed software at `Available Software  <https://cocalc.com/doc/software.html>`_ and in our `Help page <https://cocalc.com/help>`_ under "Software and Programming Libraries Details".

A running log of regular updates to the environment is the :ref:`software-updates` list.

You may want to revert to an older environment, or try a new environment that is about to be released. To change the software environment to a different compute image, use the "Selected Image" menu.
The exact list of available images will change from time to time.

Once you have selected an image, click "Save and Restart".

.. image:: img/project-settings/selected-image-experimental.png
     :width: 70%

*Note: Don't forget to reset your image to "Default" after you are finished working with an alternate image.*

Sage worksheet server
---------------------

Any time you run a Sage worksheet (.sagews file) there are two processes involved in your project:

* the Sage worksheet server process - one of these is enough to serve any number of running worksheets
* the Sage worksheet client process - there will be one of these for each worksheet that is running in the project

It can be helpful to restart the Sage worksheet server if you have changed the default version of Sage, for example with ``sage_select``.
Note that restarting the Sage worksheet server will not affect worksheets that are already running.

Occasionally, it may be useful to restart the Sage worksheet server if worksheets are not executing properly, followed by restarting individual Sage worksheet(s). You might do this as a less drastic step than restarting the entire project.


.. image:: img/project-settings/restart-sagews-a.png
     :width: 70%

Alternate Jupyter Servers in CoCalc
-----------------------------------

CoCalc by default provides an interface to Jupyter notebooks that has been rewritten to support multiple users, TimeTravel, and other enhancements. For more information, see the CoCalc blog `article on the Jupyter rewrite <http://blog.sagemath.com/jupyter/2017/05/05/jupyter-rewrite-for-smc.html>`_. There may be occasions when you may want to run the Classical Jupyter server. The most common reason is to use interactive widgets, which are not supported in the CoCalc Jupyter notebook.

The "Project Settings" page offers two ways to run the Classical Jupyter server code, shown below.
For more information and some important caveats, see :doc:`Classical versus CoCalc <jupyter>`.

Plain Jupyter server
""""""""""""""""""""

Starting the Plain Jupyter server opens a new browser tab with usual files listing. Opening a notebook from the Jupyter server tab opens another browser tab.

.. image:: img/project-settings/jupyter-server-a.png
     :width: 70%

JupyterLab server
"""""""""""""""""

Starting the `JupyterLab server <https://jupyterlab.readthedocs.io/en/stable/>`_ opens a new browser tab with the JupyterLab GUI.

.. image:: img/project-settings/jupyterlab-server-a.png
     :width: 70%


.. |header| image:: https://github.com/encharm/Font-Awesome-SVG-PNG/raw/master/black/png/16/header.png

.. _ssh: https://help.ubuntu.com/community/SSH
