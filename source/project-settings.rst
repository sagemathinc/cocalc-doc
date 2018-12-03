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


SSH Keys
--------

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