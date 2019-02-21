.. index:: Terminal

==============
Linux Terminal
==============

The CoCalc terminal allows you to run Linux programs on the command-line in your browser.

To get started, create a **"Terminal"** file in the "Files" listing or in "+ New".
Such files end in ``.term`` and open up in a :doc:`frame-editor`.
Inside of each panel a terminal session starts up and you can issue commands.

**New to Linux?** Find out more about the Linux command line at the
`Linux Tutorial <http://ryanstutorials.net/linuxtutorial/>`_, which
is one of several introductory topics at `Ryan's Tutorials <http://ryanstutorials.net/>`_.

Do you want to install certain **Python or Anaconda** packages,
please consult :ref:`python-pkg-install-user`.

Installing **R packages** locally in your project is covered here: :ref:`install-r-packages`.

.. contents::
   :local:
   :depth: 2

Features
=============


.. image:: img/terminals4.png
    :width: 100%



Extensive Command Set
-------------------------

In addition to the usual commands available at user level in `Ubuntu Linux <https://www.ubuntu.com/>`_, there are command line programming interfaces for ``sage``, ``python2`` / ``ipython2``, ``python3`` / ``ipython3``, ``R``, ``gap``, ``java``, ``julia``, ``octave`` and many more. There is an extensive list of added executables at the `CoCalc installed software list <https://cocalc.com/doc/software.html>`_.


Collaboration and Side Chat
------------------------------

Like any other application in CoCalc, the terminal environment allows
more than one user to enter commands and view results in the same session.
The terminal size will adjust according to the available number of rows and columns of each particiant.
It also allows users participating in the same session to share comments by opening a chat for the terminal session by clicking the Chat icon at upper right.

Additionally, you can use the "open door" button to remove all other collaborators interfering with your current terminal session.


Disconnect and Resume
-------------------------

If you disconnect your browser from CoCalc while you have a terminal session open, the session is preserved as long as the project is not restarted.
Next time you reconnect – even with a different browser or via another computer – a still running session will appear again and you can continue to work where you've left.


Multiple Terminals in a Single Browser Tab
---------------------------------------------

Terminals open up in a :doc:`frame-editor`. This means you can use buttons at upper right to split the terminal frame vertically or horizontally. The split defaults to the middle of the frame, but the dividing line can be dragged to give more space to one of the new frames and less to the other. You can continue splitting to get even more frames in a single browser tab. Click the `x` icon at upper left to close a frame.


.. index:: Terminal; startup files
.. _terminal-startup-files:

Startup files
--------------------

When you click on the "rocket" icon (|rocket|),
a hidden file – which is tied to that specific terminal – is created.
It contains further instructions about how to configure commands that are run when it starts.

.. |rocket|
    image:: https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/128/rocket.png
    :width: 16px

.. index:: Anaconda Environment

Anaconda Environment
------------------------

To use the `Anaconda data science platform <https://www.anaconda.com/>`_, enter the command ``anaconda5`` in a terminal session. The shell prompt will change to notify you that you're now working in the default ("base") anaconda environment. To exit the
anaconda platform and continue your terminal session, use the command ``exit-anaconda``.

Additionally, you can :ref:`setup your own Anaconda environment <anaconda-install>` inside your project, and even setup your own :ref:`customized Jupyter Kernel <anaconda-jupyter>` for it.

**Note:** an older version of anaconda is temporarily available with the command ``anaconda3``. We recommend all new applications use ``anaconda5``.


Tips and tricks
=================

.. _terminal-editor-panel:

Terminal Environment in Split Frame with File Editor
------------------------------------------------------

If you open a source code file in CoCalc for editing, for example an ``.sh``, ``.py``, ``.R``, or ``.rb`` file, you can :doc:`split the editor frame <frame-editor>` and add a command session. That way, you can easily move between editing and running the code.

.. image:: img/edit-terminal-split.png
    :width: 100%
    :align: center



Customize font
-----------------

To change the **size** of the font, click the plus and minus magnification glass icons at the top of a focused terminal frame.

In order to change the appearance of the **font family** of the terminal, adjust the font settings of your web browser.
For example, in *Google Chrome* this is done in **Settings** → **Appearace** → **Customize Fonts**:

.. image:: img/terminal/chrome-customize-fonts.png
    :width: 75%
    :align: center

Then select a different **fixed-width** font:

.. image:: img/terminal/chrome-fixed-width-font.png
    :width: 75%
    :align: center



Broken VIM key bindings
--------------------------------

If you have a browser extension that uses the vim keys it may intercept the 'Esc' character, preventing you from switching to command mode in CoCalc.
Either remap 'Esc' to a different key for the browser extension or disable the extension on the cocalc.com domain.


.. index:: Fish shell

Setup fish shell
-----------------------------------------------------

You can automatically span a process replacing of the default bash shell while it starts
via a :ref:`startup file <terminal-startup-files>`.
In order to avoid having broken Home/End keys in the fish shell,
you have to set the ``TERM`` environment variable correctly to use xterm! I.e.

1. Click on the rocket-icon in a terminal
2. Add this to the setup file::

       source ~/.bashrc
       export TERM=xterm-256color
       exec fish

Next time you launch this terminal, or restart it via typing in ``exit`` and pressing the return-key, this setup file will be evaluated and you'll end up in the fish shell with the correct TERM environment variable set.


.. index:: Terminal; remove history

Remove history from a terminal file
-----------------------------------

Suppose you want to use a .term file, but want to remove previous history, comments, etc. In addition to deleting the contents of the .term file, you need to delete one or more hidden files. Click the little "hidden eye" icon in the upper right of the file listing to show hidden files. Then delete the hidden files that end in .term. They have the (recent) history of use of that terminal. If you delete them, then they are gone.

.. image:: img/terminal/clean-terminal.png
    :width: 75%
    :align: center

One reason this situation might arise is if you are an instructor in  a course and want to distribute a .term file to your students using the Handouts or :ref:`Assignments <create-assignment>` feature in CoCalc courses, but do not want to distribute command history that may have accumulated with the original terminal in the instructor's project.
