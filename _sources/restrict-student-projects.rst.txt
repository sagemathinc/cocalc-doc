.. _restrict-student-projects:

###############################
Restrict Student Projects
###############################

.. figure:: img/teaching/restrict-student-projects.png
     :width: 90%
     :align: center
     :alt: several options for restricting student projects

     "Restrict student projects" at lower right in course Configuration


In the course Configuration tab, check any of the boxes under "Restrict student projects" to remove the corresponding functionality from student projects. See below for more information about each item. This information is also available if you hover over an option in the web dialog.

Because some CoCalc features may not be compatible with course content created by an instructor, restricting a project can reduce student confusion and prevent issues with running and grading assignments. It may also keep students more focused, e.g., during an exam. Do not gain a false sense of security and expect these to prevent all forms of cheating.

.. contents::
   :local:
   :depth: 2

*******************************
Disable file actions
*******************************

Make it so students can’t delete, download, copy, publish, etc., files in their project.

************************************
Disable whether cells are editable
************************************

Make it so that in Jupyter notebooks, students can't toggle whether cells are editable or deletable, and also disables the RAW Json Editor and the Jupyter command list dialog. If you set this, you should probably disable all of the JupyterLab and Jupyter classic options too.

****************************************
Disable Jupyter Classic notebook server
****************************************

Disable the user interface for running a Jupyter classic server in the student project. This is important, since Jupyter classic provides its own extensive download and edit functionality; moreover, you may want to disable Jupyter classic to reduce confusion if you don't plan to use it.

****************************************
Disable Jupyter Classic mode
****************************************

Do not allow opening Jupyter notebooks using classic mode. The Jupyter classic UI has some workarounds for the other restrictions here, and can also cause confusion if you don't want students to use it in your class.

****************************************
Disable JupyterLab notebook server
****************************************

Disable the user interface for running a JupyterLab server in the student project. This is important, since JupyterLab provides its own extensive download and edit functionality; moreover, you may want to disable JupyterLab to reduce confusion if you don't plan to use it.

****************************************
Disable VS Code IDE Server
****************************************

Disable the VS Code IDE Server, which lets you run VS Code in a project with one click.

****************************************
Disable Pluto Julia notebook server
****************************************

Disable the user interface for running a pluto server in student projects. Pluto lets you run Julia notebooks from a project.

****************************************
Disable command line terminal
****************************************

Disables opening or running command line terminals in the student project.

****************************************
Disable file uploads
****************************************

Blocks uploading files to the student project via drag-n-drop or the Upload button.

****************************************
Disable adding or removing collaborators
****************************************

Removes the user interface for adding or removing collaborators from the student project.

****************************************
Disable outgoing network access
****************************************

Blocks all outgoing network connections from the student project.

****************************************
Disable SSH access to project
****************************************

Makes any attempt to ssh to the student project fail.

****************************************
Disable all ChatGPT integration
****************************************

Remove *all* ChatGPT integrations from the student projects. This is a hint for honest students, since of course students can still use copy/paste to accomplish the same thing.

****************************************
Disable some ChatGPT integration
****************************************

Disable ChatGPT integration except that 'Help me fix' and 'Explain' buttons. Use this if you only want the students to use ChatGPT to get unstuck.

****************************************
Disable Public sharing
****************************************

Disable public sharing of files from the student projects. This is a hint for honest students, since of course students can still download files or even copy them to another project and share them. This does not change the share status of any files that are currently shared.

