.. index:: Display options
.. _display-options:

====================================
Display Options
====================================

The following options allow you to change how CoCalc appears in your browser, and what information it restores when you return to the site after leaving it.

.. toctree::
   :maxdepth: 2

#######################
Fullscreen Options
#######################


***************
kiosk
***************

Visiting a CoCalc file URL with a query string of `?fullscreen=kiosk` offers a limited user interface suitable for embedding in an iframe. The user won't be able to use the UI to open files. The Project toolbar and Files toolbar are not displayed. The button for side chat while editing a file is not displayed.

***************
project
***************

Visiting a CoCalc file URL with a query string of `?fullscreen=project` hides the functionality for switching between projects, viewing
account settings, etc., and focused on *one single project*.
However, unlike fullscreen=kiosk, users can
still use the Files page to download/upload and navigate files,
and other useful tabs like Find and Log.

You might use "fullscreen=project" in combination with the "session" query parameter (see below) as follows: https://cocalc.com/projects/project-id/files/main.ipynb?fullscreen=project&session=

***************
default
***************

Visiting a CoCalc file URL with a query string of `?fullscreen=default`  presents the full user interface. It is the same as using a query string of `?fullscreen=` and the same as not providing any "fullscreen" query parameter at all.


#######################
Sessions
#######################

***************
default
***************

By default, CoCalc remembers your session with a specific browser, that is, if you have certain projects open, and certain file tabs displayed within those projects when you close your browser, they will normally be restored when you visit CoCalc again with that browser.

Limitations:

* CoCalc sessions are totally client-side They are not remembered across different browsers.
* Browser refresh does not open a file until you click the tab. The session feature just remembers the tabs and their order, not which files were open.

***************
no session
***************

If you visit CoCalc with a query string of `session=`, then the link is loaded and the "session=" parameter is removed from the displayed URL. In this case, there is no session at all. No project or files tabs will be remembered the next time you visit CoCalc with that browser.

###########################
Desktop Application
###########################

The CoCalc desktop application provides a lightweight wrapper around the latest version of the website. (So it's always up to date from the point of view of CoCalc.) The main advantages of the desktop application are:

* You can use emacs/vim keyboard shortcuts without accidentally triggering browser actions.

* No extensions: by omitting browser extensions and other browser configuration, CoCalc performance in the desktop app may be improved, and some connectivity issues seen in the full browser (such as problems arising from ad blockers) can be eliminated.

You can download macOS and Windows binaries for the CoCalc desktop application at https://github.com/sagemathinc/cocalc-desktop/releases. 

See the `CoCalc desktop github repository <https://github.com/sagemathinc/cocalc-desktop>`_ for more information.