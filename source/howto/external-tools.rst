=======================
External Tools
=======================

Notes about external (or 3rd party) tools on CoCalc.

.. contents::
   :local:
   :depth: 2


Sync with Dropbox or Google Drive?
-------------------------------------------------

We do not support Google Drive at present, but we plan to.

Following the instructions at https://www.dropbox.com/install-linux you can install it in a :doc:`../terminal`.
However, Dropbox recently made a very sad decision to not support Linux (except ext4 unencrypted, which is a nonstarter), so Dropbox is no longer possible with CoCalc.


.. index:: GitHub

Pull from GitHub using SSH
-----------------------------------

.. note::

    First, despite the fact that you are accessing CoCalc through the internet,
    you are actually working in a highly restricted environment.
    Processes running inside a *free* project are not allowed to directly access the internet.
    (We do not allow such access for free users, since when we did,
    malicious users launched attacks on other computers from CoCalc.)
    Enable internet access by adding the "internet access" quota.  See :doc:`../upgrade-guide`.

Once you have enabled network access for your project,
to use ssh from CoCalc to connect to `GitHub <https://www.github.com>`_
you need to create an SSH key and explicitly allow that account/key access to GitHub.

1. Make a new :doc:`../terminal` in  +New → Terminal or use an existing one

2. Create an SSH key public/private key pair by typing the command `ssh-keygen`. (consult :ref:`ssh-keys` for more information)

3. Copy the ``.ssh/id_rsa.pub`` (could be named similarly, but has the ending ``.pub``) to GitHub's setting for setting up an additional key



.. index:: SSHFS

Mount remote files via SSHFS
-----------------------------------

**Unfortunately, SSHFS is no longer supported in CoCalc due to security issues.**

If you really, really need sshfs support,
feel free to write to us (help@sagemath.com),
and we may consider implementing a workaround if their is sufficient interest.

.. warning::

    Again, the following instructions will not work no matter what

.. note::
    The following will only work if your project has outgoing network access, i.e.,
    it says "Network access: true" under project settings.
    See :doc:`../upgrade-guide`.

Suppose you have an account on some computer that you can ssh to, e.g, so this works for you::

    ssh user@my.uni.edu

To temporarily make the files at user@my.uni.edu available in a cloud project, open a Terminal and type


::

    mkdir foo   # make any directory you want
    sshfs user@my.uni.edu:path/to/files/ foo/

and type your password to login to user@my.uni.edu.
You'll find that you can now use the files at path/to/files in user@my.uni.edu as if they were in the directory foo in your project.
You can edit files (with sync), open and output data files, etc.
When you're done, type

::

    fusermount -u foo

to unmount foo.
Whenever the project server is restarted, ``foo/`` will also be unmounted.
So you'll have to type ``sshfs user@my.uni.edu: foo/`` to mount foo every once in a while.

**NOTE:** The files in ``foo/`` will *not* be included in :ref:`Snapshots <project-snapshot>`,
because they are part of another filesystem,
and the snapshot system is configured to not cross filesystem boundaries.



.. index:: Emacs

Use Emacs in a Terminal (Chrome)
--------------------------------------------

Chrome absolutely doesn't allow normal web applications to intercept certain keystrokes,
which makes Emacs-in-a-terminal painful on some operating systems (esp. Linux/Windows).
E.g., Ctrl-N brings up a new window, instead of going to the next line!

However, you can `install the CoCalc chrome app <https://chrome.google.com/webstore/detail/the-sagemath-cloud/eocdndagganmilahaiclppjigemcinmb>`_ from the app store or on Linux,
type

::

    google-chrome --app=https://cocalc.com/app

to start the website as an "app".
(If you use chromium instead, type ``chromium-browser --app=https://cocalc.com/app``).

This is not a completely solution since in some cases,
control-shift-minus and control-shift-plus still zoom in and out
(on ChromeOS they zoom the entire desktop – every window, all icons, the time, etc., in and out!).

This is a major problem, because control-shift-minus is "undo" in emacs.
The workaround I currently use is to put this in my ``.emacs`` file,
and instead type "alt-u" for undo::

    (define-key esc-map "u" 'undo)

Note that undo is also available by default through other key bindings,
like C-x u and C-/. (Execute "M-x where-is undo".)
So there are other options available.



.. index:: FriCAS

Customized version of FriCAS
-------------------------------------

The following Sage/Python command modifies the ``PATH`` variable to include ``$HOME/bin``.
Sage looks for the ``fricas`` executable in this ``PATH``::

    os.environ['PATH'] = '%s/bin:%s'%(os.environ['HOME'],os.environ['PATH'])

Restart the Sage worksheet to make sure the new version of FriCAS is started.




.. index:: Pentadactyl plugin

Pentadactyl plugin isn't working
----------------------------------------

The `Pentadactyl plugin <https://addons.mozilla.org/en-us/firefox/addon/pentadactyl/>`_ is not compatible with the `Codemirror <http://codemirror.net/>`_ editor in CoCalc.
You can disable Pentadactyl for a particular page, perhaps by pressing Control+Z.
CoCalc has it's own Vim bindings for worksheets and editing files;
to enable it, go to :doc:`../project-settings` (click the gear by your name in the upper right), then select Vim next to Editor → Bindings.

