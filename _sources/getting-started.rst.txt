.. _essential_guide:

Essential Guide
===============

In this guide we highlight the most important concepts you should be aware of to work in CoCalc effectively. Some of them you may start using right away, others (like TimeTravel and Backups) may save the day later. Many have more detailed documentation pages should you wish to study them deeper.

Projects
--------

Once you create an account on CoCalc, you should have access to at least one project - either your personal one, or projects you were invited to collaborate on. You can think of "a project" as "a virtual computer": it has your files and can run various software to interact with them. In CoCalc it is also "a collaboration unit": you can look at and edit the same files as your collaborators. In particular, Jupyter Notebooks always have the same state for you and them, including variables in memory and widget settings.

How many projects do you need? As many as collaboration groups you are a part of. In particular, if you are working by yourself, then there is not much benefit to having more than one, although you may prefer to use projects as an organizational tool. If you are enrolled into CoCalc courses, a dedicated project will be created for you automatically and your collaborators on it will be your instructors and TAs.

Licenses
--------

You should have a license applied to every project you are working on. If you have collaborators, it is possible that they have already taken care of it. CoCalc licenses are applied to projects, not to users, they determine configuration of that "virtual computer", regardless of how many people are using it (of course, if there are many heavy users, you may prefer to have a more powerful license).

Without a license your project will work in trial mode with *very* limited resources. As soon as you confirm that CoCalc seems to be what you need, we strongly encourage you to get a subscription, i.e. an automatically renewing license. If you are not sure what variant to pick - pick the standard one!

Main UI
-------

If you open an empty project, you will see a screen similar to this one, where some of the useful features are marked:

.. figure:: img/annotated_empty_project.png
    :width: 100%
    :align: center
    :alt: Main UI Elements
    
    Main UI Elements
    
Hopefully, most elements are intuitive, but some may be easy to miss. In particular:

- The Full Screen Button at the top right allows you to hide most of the user interface to save space.
- Counters to the left of it show new changes in files that you have edited and different types of messages from other users or from the system.
- Help button allows you to contact CoCalc support **with context** - not only it is easy for you to access, but it also makes it easier for us to understand where are you working!
- Two buttons on the bottom left allow you to configure the side panel buttons: you may prefer full screen pages, small flyout panels, or quick access to both.
- Tours highlight essential UI elements interactively.


Supported Files
---------------

CoCalc allows you to create and upload arbitrary files. Some may have

- extensive dedicated support, e.g. ``*.ipynb`` or ``*.tex`` 
- CoCalc-specific usage, e.g. ``*.term`` or ``*.course``
- built-in viewers, e.g. ``*.pdf`` or ``*.png``
- nothing special at all, e.g. ``*.random_extension``

In the latter case you will be able to open the file with a code editor, but if it is a binary format, it may corrupt the content. You will get a warning, however, and there is a way to restore from a backup.

The most important file types have corresponding tiles when you are trying to make one, and many supported ones are in the dropdown menu:

.. figure:: img/annotated_new_file.png
    :width: 100%
    :align: center
    :alt: Creating a New File
    
    Creating a New File
    

Jupyter Notebooks
-----------------

Our most popular and widely used feature is our own implementation of Jupyter Notebook interface:

.. figure:: img/annotated_jupyter_notebook.png
    :width: 100%
    :align: center
    :alt: Jupyter Notebook
    
    Jupyter Notebook

While it strives to behave very close to familiar for many JupyterLab, it has a number of important advantages, such as full real-time collaboration and saving all output on the server side - nothing is lost if your connection is interrupted or you switch computers. When you do switch computers (or go for a coffee break), your projects and notebooks keep running, performing computations or keeping their state, until *idle timeout* is reached. For most users it is 30 minutes. If you need a longer timeout, more memory, or CPU, you may be able to upgrade to a more powerful license or spin up some compute servers, where the sky is the limit (and your budget).


Search and Pin Menu Items
-------------------------

Sometimes you may not remember where exactly some menu item is located or if it even exists. In such a case the menu search box may be useful. Or, perhaps you know exactly where something is, because you use it all the time, but you don't want to click through the menu so often. You can pin menu items to the shortcuts toolbar:

.. figure:: img/annotated_search_pin_menu.png
    :width: 100%
    :align: center
    :alt: Search Menu Items and Add Shortcuts
    
    Search Menu Items and Add Shortcuts


Frames and Terminals
--------------------

CoCalc does not support opening two arbitrary files side-by-side - you have to open CoCalc itself in multiple browser windows to achieve that. But you can have several views for the same file or related file, in particular, terminals. Sometimes you get it automatically, but it can always be done manually too. Split the frame and pick the required frame type in the first menu item:

.. figure:: img/annotated_frame_editor.png
    :width: 100%
    :align: center
    :alt: Multiple Frames
    
    Multiple Frames

TimeTravel and Backups
----------------------

You have nothing to lose when you are just starting out, but sooner or later you will be in a situation where you wish you didn't make a certain change or you manage to hit a bug. (Which we are trying to keep to a minimum!) In addition to you using ``git`` or doing manual backups, CoCalc offers automatic version history via TimeTravel and regular file system snapshots. These are the tools you can access on your own at any time. Should the unthinkable happen and you won't be able to recover your work using either - file a support ticket, we also maintain backups accessible only to admins. (These are used *extremely* rarely, but we had a few cases over the years.)

File system snapshots are accessible via **Backups** button in the File Explorer, while TimeTravel can be opened while editing many types of files:

.. figure:: img/annotated_timetravel.png
    :width: 100%
    :align: center
    :alt: TimeTravel for Jupyter Notebook
    
    TimeTravel for Jupyter Notebook


Collaboration and AI
--------------------

If you work in CoCalc with your colleagues, you can open the same files to view and edit them simultaneously. For not-quite-real-time collaboration you can use @-mentions in a side chat of any document. And if you don't have colleagues to ask for help, you can @-mention various LLMs:

.. figure:: img/annotated_side_chat_AI.png
    :width: 100%
    :align: center
    :alt: Side Chat with AI
    
    Side Chat with AI
