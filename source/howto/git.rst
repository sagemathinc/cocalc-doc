.. index:: Git
.. index:: GitHub
.. index:: GitLab
.. index:: Bitbucket

=========================
Git Version Control
=========================


.. note::

    First, despite the fact that you are accessing CoCalc through the internet,
    you are actually working in a highly restricted environment.
    Processes running inside a *free* project are not allowed to directly access the internet.
    (We do not allow such access for free users, since when we did,
    malicious users launched attacks on other computers from CoCalc.)
    Enable internet access by adding the "internet access" quota.  See :doc:`../upgrade-guide`.


.. index:: Git; in command-line terminal

Git command-line
========================

CoCalc gives you full control over `Git`_ via a :doc:`../terminal` in the command-line.

Once you have *enabled internet access for your project*, you can to connect to online Git services like
`GitHub <https://www.github.com>`_, `GitLab <https://about.gitlab.com/>`_ or `Bitbucket <https://bitbucket.org/>`_.
You can immediately pull from a public repository.

To access private repositories or to push your new commits,
you need to create an SSH key and explicitly allow that account/key access to access the remove repository.

1. Create an SSH key public/private key pair by typing the command `ssh-keygen`. (consult :ref:`ssh-keys` for more information)

2. Copy the content of ``.ssh/id_rsa.pub`` (could be named similarly, but has the ending ``.pub``) to GitHub's setting for setting up an additional key. To open that file quickly, you can run this in the Terminal: ``open ~/.ssh/id_*.pub``.

3. If necessary, `navigate to a different directory <https://ryanstutorials.net/linuxtutorial/navigation.php>`_.

4. Use `Git`_ as usual.

.. index:: Git; in X11 desktop

Git graphical desktop emulator
===================================

You can use Git apps in an :doc:`X11 Desktop <../x11>`.
Open an ``.x11`` file in CoCalc. There are launch buttons in the panel at lower left for `gitg`_ and `gitk`_.

.. index:: Git; repo hosted in CoCalc project

Host a Git repository in CoCalc
=====================================

You can create a Git repository hosted inside a CoCalc project, and then access that repository remotely from any client computer that has :ref:`SSH Access <ssh-keys>` to the project enabled. See "Hosting a git repository on CoCalc" in the blog article, `Using SSH with CoCalc <http://blog.sagemath.com/cocalc/2017/09/08/using-ssh-with-cocalc.html>`_.



.. _gitg: https://wiki.gnome.org/Apps/Gitg/
.. _gitk: https://git-scm.com/docs/gitk
.. _Git: https://www.git-scm.org