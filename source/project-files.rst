.. index:: Projects; files
.. _project_files:

**********************************
Project Files
**********************************

The project **Files** listing gives you an overview of your files in that project. Click on a line to open a file,
or select one or more files via the checkbox on the left to manipulate them (deleting, moving, ...)

.. figure:: img/project-files/files-list.png
     :width: 80%
     :align: center

     *files list*


.. index:: Hidden Files; in Files list
.. _hidden-files:

=====================
Show Hidden Files
=====================

By convention, a file whose name begins with a dot is a hidden file. It will not show up in various file listings by default. Click the eye icon with a slash (|eye-slash|) to include hidden files in the list; the icon changes to an eye (|eye|)  without a slash. Click the |eye| icon to exclude hidden files.

.. figure:: img/project-files/files-with-hidden.png
     :width: 80%
     :align: center

     *files list showing hidden files*

.. index:: Masked Files; in Files list
.. index:: Temporary Files; in Files list
.. _masked-files:

=====================
Hide Temporary Files
=====================

Processing some programs, notably LaTeX source (e.g. ``.tex`` files) causes temporary files to be generated. These can clutter your file listing. Click the mask icon (|mask|) to toggle display of hidden files on or off.

.. figure:: img/project-files/files-filtered-mask.png
     :width: 80%
     :align: center

     *files list filtered for "latex-sample", temporary files masked*

.. figure:: img/project-files/files-filtered-nomask.png
     :width: 80%
     :align: center

     *files list filtered for "latex-sample", showing temporary files*

.. index:: Backups; in Files list
.. index:: Snapshots; in Files list
.. _project-snapshot:

=====================
Snapshots
=====================

Click on the "|life-ring| Backup" button to switch to a directory containing consistent point-in-time backups of all your files.
Use this in case you have deleted a whole set of files, or just want to restore them from a while ago.

*Note:* Snapshots are in a read-only file system. If you want to modify a file that resides in a snapshot, you will need to copy it into a writable part of your project first.

.. |life-ring|
    image:: https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/128/life-ring.png
    :width: 16px

.. |eye|
    image:: https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/128/eye.png
    :width: 16px

.. |eye-slash|
    image:: https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/128/eye-slash.png
    :width: 16px

.. |mask|
     image:: img/icons/mask-icon.png
     :width: 16px