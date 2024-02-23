.. index:: Sharing files
.. index:: Publishing files

.. _sharing-files:

Collaborate. Share! Publish!!!
##############################

.. contents::
     :local:
     :depth: 2

When you create a new project in CoCalc, all of its files and folders are accessible only by you. You can add collaborators to work with you on the whole project - they will have read and write access. You can also grant read-only access (with the option to edit a copy) to individual files and folders for people who possess a secret link, or even publish these links in a way that makes them discoverable by search engines.


Collaborating
=============

Projects are CoCalc's way to organize collaboration. The owner of the project and added collaborators have equal access to all files, folders, and settings of the project, including ability to add new collaborators or remove existing ones. (The only exception to this rule is that it is impossible to remove the owner of the project.)

Not only your collaborators have access to the same files as you do, you can edit the same file at the same time with edits merged thanks to real time collaboration and merging of simultaneous edits. You can also chat with other users of the project.

To manage collaborators on the current project, go to :doc:`Users tab <users>`.


.. _publishing-files:

Sharing Files and Folders
=========================

You can share individual files and folders with other people by sending them a link. To create it, use menu **File > Publish File** for an open file or in the file explorer select *one* file or folder using the checkbox on the left and click **Publish** button:

.. figure:: img/publish_using_explorer.png
     :width: 80%
     :align: center
     :alt: Publish a file using explorer
     
     Publish a file using explorer

Next pick **Public (unlisted)**. Yu can then copy the link to your clipboard using the button on the right of the link:

.. figure:: img/publish_unlisted.png
     :width: 80%
     :align: center
     :alt: Publish a file without listing
     
     Publish a file without listing

You may optionally enter a description for the file being shared, a copyright license, and even a custom name (see :ref:`vanity-urls` to learn more). You can even tie your CoCalc license to the shared file - this way people who make their own copy of your content will be able to benefit from upgrades that it provides.

Shared files are marked with an icon in file explorer:

.. figure:: img/published_file_in_explorer.png
     :width: 80%
     :align: center
     :alt: Published file in a file explorer
     
     Published file in a file explorer
     
     
Publishing Files and Folders
============================

In addition to creating links to access your files and folders, you can publish them on `CoCalc share server <https://cocalc.com/share>`_ where people can discover them directly or using search engines. Follow the same steps as for sharing above, but choose the **Public (listed)** option:

.. figure:: img/publish_listed.png
     :width: 80%
     :align: center
     :alt: Publish a file with listing
     
     Publish a file with listing


.. index:: Sharing files; share server
.. _share-server:

CoCalc Share Server
===================

To view CoCalc files published by others, navigate to https://cocalc.com/share. You can search for text in the title and contents of published files using the search box at upper right. You can sort the list of files by any of the columns listed, in increasing or decreasing order, by clicking in the column headings.

.. figure:: img/share-home-page.png
     :width: 90%
     :align: center
     :alt: Share server home page

     Share server home page

There is also a preview at the CoCalc home page, allowing people who are just learning about CoCalc to view a sample of published files.

When you open a sharing link, you get a view of the contents. Click **Edit your own copy** to copy a shared file or folder to a project that you own or collaborate on:

.. figure:: img/open_sharing_link.png
     :width: 90%
     :align: center
     :alt: Opened sharing link

     Opened sharing link



.. index:: Sharing files; vanity URLs
.. _vanity-urls:

Vanity URLs
-----------

You can set up your profile so that all the documents you've published are listed under your unique URL, ``https://cocalc.com/name-of-your-choice``  (e.g., https://cocalc.com/wstein).

CoCalc lets you assign a username, project names, and file names, so that you can create links to shared files that are easy to type and remember.

* Set your username in :ref:`Account Preferences <username>`.

* Set the project name in :ref:`Project Settings <set-project-title>`.

* Set the name while :ref:`Sharing Files and Folders <publishing-files>`.

If you set all these you get a nice url, e.g.
https://cocalc.com/wstein/support/examples


.. _star-shared-file:

Starring Published Files
------------------------

You can star published files on the share server and see everything you starred here: https://cocalc.com/stars.

.. figure:: img/add-star.png
     :width: 80%
     :align: center
     :alt: Star a file on the share server

     Star a shared file so you can find it easily later

You can undo the operation by clicking **Starred**:

.. figure:: img/remove-star.png
     :width: 80%
     :align: center
     :alt: remove previously-added star from a file on the share server

     Click **Starred** to remove a previously-added star


.. _url-proxy:
.. _share-rendered-notebook:

Publishing Rendered GitHub Files
--------------------------------

CoCalc share server offers a simple way to publish fully-rendered Jupyter notebooks and certain other file types in gists and GitHub repositories. All you need is a URL to the gist or repository you want to publish. Rendered document publishing is done by means of URL proxying (see :ref:`url-proxy-notes`).

The URL schema is exactly the same as what https://nbviewer.org uses, i.e., ``github/<github url>`` and ``gist/[github user]/[gist id]``. Here are a couple of examples:

- GitHub Repo https://cocalc.com/github/sagemanifolds/IntroToManifolds
- GitHub Gist https://cocalc.com/gist/darribas/4121857

.. _url-proxy-cocalc-diff:

The main differences relative to nbviewer are:

* You can put a URL to any file CoCalc can render or edit in a GitHub repository, and you'll see it, not just ``.ipynb`` files. For example:

  * Markdown: https://cocalc.com/github/sagemathinc/cocalc/blob/master/README.md
  * Whiteboard: https://cocalc.com/github/williamstein/scratch/blob/main/2022-06-27-ws.board
  * Sage worksheet: https://cocalc.com/github/williamstein/scratch/blob/main/2022-06-30-061806.sagews

* When you click **Edit my own copy** (analogue of mybinder for some nbviewer content), the content is copied to a project in CoCalc and you can use it. E.g., Sage notebooks actually work, since Sage is installed. The mybinder flakiness is avoided. Also, all content is editable, not just content that has been setup to work with mybinder.

.. _url-proxy-notes:

Notes on URL proxying
---------------------

* Editing whole git repositories isn't implemented yet. In CoCalc, any time anybody views one of these URL proxies in the share server, a new entry is created in the list of published documents starting at https://cocalc.com/share/public_paths/page/1

* Anybody can star a document published in this way, to make it easy to come back to it later (via https://cocalc.com/stars), and also to signify that it is interesting.

* See also the  `initial implementation comment <https://github.com/sagemathinc/cocalc/issues/6015#issuecomment-1172967091>`_ in the CoCalc sources.


.. index:: Sharing files; direct from project

Publishing Tips and Considerations
==================================

Test Your Publication
---------------------

To make sure that what you have published works as expected, open the link while you are signed out of your CoCalc account or in a new incognito window (to avoid using your account).

Auxiliary Files
---------------

If your document depends on auxiliary files, e.g. images embedded in a markdown file, make sure these auxiliary files are accessible. To do this, put your document and all auxiliary files in a common folder and *publish that folder*.

Collections of Documents
------------------------

If you want to publish multiple related files, e.g. notebooks accompanying your book, the best approach is likely to organize everything in a single folder, perhaps with subfolders for each chapter, and *publish the top level folder*. You still will be able to use links to individual chapters and/or notebooks!

Data Sets
---------

Whenever feasible, you should host your data sets on CoCalc, either alongside your notebooks (if the data sets are small enough), or by making a request for global installation. This will ensure that your code will not break due to data sets becoming unavailable for one reason or another.

Interactive Elements
--------------------

Interactive elements that use server processes, such as notebooks with Jupyter widgets and worksheets with Sage ``@interact``, will not operate in files viewed from the share server. That is because documents on the share server are truly static. There is no kernel or Sage server running in the background to facilitate any sort of interactive computing. Controls that run completely in the browser work when served from the share server, for example 3d plots like `this cardioid <https://cocalc.com/share/public_paths/7eee8ccdeb4acf37e6c258df1cd973871373df05>`_.

Duration of Software Support
----------------------------

If you are concerned that your code may stop working when software installed on CoCalc gets upgraded to its next version (which is very likely to happen sooner or later), you can pin a software environment in CoCalc with a reasonable expectation that it will be available for 5 years. Beyond that your notebooks and code still will be available, but may fail to work correctly without adjustments with newer versions of dependencies. To pin the environment, click **Settings** in the side panel and then pick a date-stamped **Software Environment** in the drop down:

.. figure:: img/pin_software_environment.png
     :width: 80%
     :align: center
     :alt: Pin a software environment

     Pinning a date-stamped software environment

Also, if you are concerned about your code working long term, consider adding software tests in addition to the main notebooks that focus on the content of your material!