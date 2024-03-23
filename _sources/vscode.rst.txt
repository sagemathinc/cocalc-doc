.. index:: vscode

Visual Studio Code Server
==========================

Visual Studio Code is a source-code editor made by Microsoft. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. For more information about the server, see the home page: `Visual Studio Code Server <https://code.visualstudio.com/docs/remote/vscode-server>`_.

To start VS Code Server in a CoCalc project, select Servers in the :doc:`activity-bar` and click the "VS Code" button:

.. figure:: img/vscode-server.png
    :width: 90%
    :align: center
    :alt: Starting VS Code Server from the Activity Bar

    Starting VS Code Server from the Activity Bar

When you click the link to start Visual Studio Code Server, a new browser tab opens with VS Code running as a browser application. All files are in the project, and therefore accessible from any browser.

There's no transparent support for multiple collaborative editing yet.

Plotting from Python Scripts
----------------------------

You can use VSC to work with Jupyter notebooks with inline plots. It is also possible to make use of CoCalc support for X11 to display plots from python scripts.

#. In the CoCalc browser tab open :ref:`X11 desktop <X11>`.
#. In the terminal frame enter ``echo $DISPLAY`` which will show something like ``:1295981061``
#. Set ``$DISPLAY`` environment variable to this value (including the column) in your VSC script/terminal.
#. Run your code - plots should show up on the X11 desktop!

.. figure:: img/vsc_x11_plotting_cocalc.png
    :width: 90%
    :align: center
    :alt: CoCalc Tab with the Plot

    CoCalc Tab with the Plot

.. figure:: img/vsc_x11_plotting_vsc.png
    :width: 90%
    :align: center
    :alt: VSC Tab with ``$DISPLAY`` Set
    
    VSC Tab with ``$DISPLAY`` Set
