.. index:: Git

=========================
Git Version Control
=========================

.. index:: Git; in command-line terminal


CoCalc gives you full control over `Git`_ via a :doc:`../terminal` in the command-line.

.. _Git: https://www.git-scm.org

.. index:: Git; in X11 desktop

You can use Git apps in an :doc:`X11 Desktop <../x11>`. When you open a .x11 file in CoCalc, there are launch buttons in the panel at lower left for `gitg`_ and `gitk`_.

.. index:: Git; repo hosted in CoCalc project

You can create a git repository in a CoCalc project, and then access that repository remotely from any client computer that has :ref:`SSH Access <ssh-keys>` to the project enabled. See "Hosting a git repository on CoCalc" in the blog article, `Using SSH with CoCalc <http://blog.sagemath.com/cocalc/2017/09/08/using-ssh-with-cocalc.html>`_.

.. note::

    Accessing remote content from a CoCalc project requires the :doc:`internet access <../upgrade-guide>` upgrade.

.. _gitg: https://wiki.gnome.org/Apps/Gitg/
.. _gitk: https://git-scm.com/docs/gitk
