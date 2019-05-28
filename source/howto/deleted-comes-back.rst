.. index:: Deleted files come back
.. _deleted-comes-back.rst:

================================================
Deleted File or Folder Comes Back
================================================

This page explains why you may sometimes see a deleted file or folder reappear in the :doc:`Files list <../project-files>` of a project, and what to do about it.

.. index:: Deleted files come back; reasons for

Reasons Why a Deleted File Might Reappear
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* First, if it seems that a deleted file has resurfaced, try :ref:`refreshing the Files list <refresh-files>` to make sure the list is current.

* If someone clicks on the name of the deleted file in the :ref:`Project Activity Log <ft-history>`, CoCalc will open a 0-length file with that name.

* If a file is deleted in one browser session but open in another session, any activity in the second session that tries to write the file can make the file reappear.

* If a second session had the file open and then its browser was closed before the file was deleted, the file can come back when the second user reopens the browser.

* The above can also happen if a file is moved, i.e. a "ghost" of the moved file appears in the original location.

See also: `CoCalc issue #2880 <https://github.com/sagemathinc/cocalc/issues/2880>`_.

.. index:: Deleted files come back; Jupyter notebook

Jupyter Notebook Comes Back After Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some specific remarks when the deleted file in question is a Jupyter notebook:

* If a notebook is deleted while there is a tab open on it, then any action that triggers saving the notebook will bring it back.

* If a notebook is closed without halting, its python process will continue to run. That process could trigger a save of the file, bringing it back after deletion.

* If a notebook is closed and halted, reopening it by clicking in the project log will bring the file back.

To prevent deleted notebooks from reappearing: before deleting a notebook, make sure there are no tabs open running it. In fact, it's generally a good idea, when you are finished working with a notebook, to click `Close and halt`. This has the added benefit of freeing up memory, as well as preventing unwanted ghost files.

