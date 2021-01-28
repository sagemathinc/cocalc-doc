.. index:: Projects

========================
Projects
========================

The concept of a "Project" is the fundamental building block for running any calculations on CoCalc.
It is an isolated, private working space, where you work with files organized in directories.

Under the hood, this is a remote Linux environment, which runs inside a Docker container.
All files reside in the ``$HOME`` directory of a fictitious user or a subdirectory.


To start being productive, you have to create a
:doc:`Sage Worksheet <sagews>`,
:doc:`Jupyter Notebook <jupyter>`,
:doc:`terminal`,
:doc:`LaTeX document <latex>`, or other files.



.. toctree::
   :maxdepth: 2

   project-list
   project-files
   plus-new
   project-log
   project-settings
   upgrade-guide
   project-library
   project-init
   project-faq