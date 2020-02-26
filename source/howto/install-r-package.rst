.. index:: R Packages
.. _install-r-packages:

============================
Install R Packages
============================


This page describes how to install an R package in a CoCalc project.

CoCalc already includes `hundreds of R packages <https://cocalc.com/doc/software-r.html>`_, but you can install even more or update them inside your project.


.. warning::

    Your project **must** have the :ref:`"Internet access" upgrade <project-upgrades>` in order to download software from a remote repository (i.e. CRAN) to your project.
    The install command will not work unless you :ref:`upgrade your project <project-upgrades>` to have internet access.

    Otherwise you have to download the tarball of the R package to your own machine,
    and :doc:`upload <./upload>` it to your project.
    Then, you can tell R to install the package directly from there as a local file.


In a nutshell, a :doc:`CoCalc project <../project>` is a Linux environment inside a Docker container.
This means, almost everything you can do as a "normal" Linux user also works.
In particular, you can install packages locally, such that R instances can pick them up.


Install requests
===================

If a package may have general use but is not already installed in CoCalc,
please open a support request to tell us to install it globally for everyone.
Please include information about special dependencies or a specific example to test it.


Install a package
===================

Command line (recommended)
--------------------------------

To actually install a package, create or open an existing :doc:`../terminal` file.

#. Wait for the command-line prompt and type in ``R`` and hit the `Return` key. R will start up.
#. Type in ``install.packages("<name of package>")`` and hit the `Return` key.
#. R will ask you to install it in a local directory, starting with "``~``" – the "home directory" of your project. In the example below it is ``~/R/x86_64-pc-linux-gnu-library/3.4``.
#. Confirm the questions with ``y`` and the installation process should run smoothly.
#. Exit R by pressing `Ctrl+d` or calling the ``q()`` function.

Here is a session for installing `conjoint <https://cran.r-project.org/web/packages/conjoint/index.html>`_ in a :doc:`../terminal`::

    ~$ R

    R version 3.4.4 (2018-03-15) -- "Someone to Lean On"
    Copyright (C) 2018 The R Foundation for Statistical Computing
    Platform: x86_64-pc-linux-gnu (64-bit)

    [...]

    > install.packages("conjoint")
    Installing package into ‘/usr/local/lib/R/site-library’
    (as ‘lib’ is unspecified)
    Warning in install.packages("conjoint") :
      'lib = "/usr/local/lib/R/site-library"' is not writable
    Would you like to use a personal library instead?  (y/n) y
    Would you like to create a personal library
    ~/R/x86_64-pc-linux-gnu-library/3.4
    to install packages into?  (y/n) y
    trying URL 'https://cloud.r-project.org/src/contrib/conjoint_1.41.tar.gz'
    Content type 'application/x-gzip' length 32601 bytes (31 KB)
    ==================================================
    downloaded 31 KB

    * installing *source* package ‘conjoint’ ...
    ** package ‘conjoint’ successfully unpacked and MD5 sums checked
    ** R
    ** data
    ** inst
    ** preparing package for lazy loading
    ** help
    *** installing help indices
    ** building package indices
    ** testing if installed package can be loaded
    * DONE (conjoint)

    The downloaded source packages are in
            ‘/tmp/RtmpHza9lC/downloaded_packages’
    > q()
    Save workspace image? [y/n/c]: n


Jupyter Notebook
---------------------

It is also possible to install packages directly via a Jupyter Notebook.
The drawback compared with the Terminal option above is the lack of interactivity.

To be able to install into your local package library in your home directory,
you have to make sure such a directory exists and tell the ``install.packages`` command –
it is defined by ``Sys.getenv("R_LIBS_USER")``.

Otherwise you end up with errors like::

    Installing package into ‘/usr/local/lib/R/site-library’
    (as ‘lib’ is unspecified)
    Warning message in install.packages("<package name>"):
    “'lib = "/usr/local/lib/R/site-library"' is not writable”


To install packages into your own collection of packages, run this in a notebook cell::

    dir.create(path = Sys.getenv("R_LIBS_USER"), showWarnings = FALSE, recursive = TRUE)
    install.packages("<name of package>", lib = Sys.getenv("R_LIBS_USER"), repos = "https://cran.rstudio.com/")

Credits: `stack overflow post <https://stackoverflow.com/a/43283085/54236>`_

**Note**: If your ``Sys.getenv("R_LIBS_USER")`` already exists, a freshly started kernel will already know about it. You can check this by running ``.libPaths()``. If the first listed path starts with ``/home/user/R/...`` you can run ``install.packages`` without any errors.

Aftermath
===========

The above will install R packages for use with CoCalc worksheets (``%r`` mode)
and Jupyter notebooks using default R.
The Sage binary may be built with a different release of R.
Use ``R-sage`` instead of ``R`` to install packages for it.
