.. index:: R Packages
.. _install-r-packages:

============================
Install R Packages
============================


This page describes how to install an R package in a CoCalc project.

CoCalc already includes `hundreds of R packages <https://cocalc.com/doc/software-r.html>`_, but you can install even more or update them inside your project.


.. warning::

    Your project **must** have the :ref:`"Internet access" upgrade <project-upgrades>` in order to download software from a remote repository (i.e. CRAN) to your project.
    Installing an R package will require you to :ref:`add a license <project-add-license>` or :ref:`add upgrades <project-upgrades>` so that your project has internet access.

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

To install a package, create or open an existing :doc:`../terminal` file.

It may first be necessary to create the path where your locally-installed R packages will be stored. The first steps make sure that the needed directory is created and available to R instances. It's necessary to exit R and restart it for the directory path to become available. This first part (steps 1-3) only needs to be done once per project.

#. Wait for the command-line prompt and type in ``R`` and hit the `Return` key. R will start up.
#. Type in ``dir.create(path = Sys.getenv("R_LIBS_USER"), showWarnings = FALSE, recursive = TRUE)`` and hit the `Return` key.
#. Exit R by pressing `Ctrl+d` or calling the ``q()`` function.
#. Again type in ``R`` and hit the `Return` key. This will start R with the new directory available.
#. Type in ``install.packages("<name of package>")`` and hit the `Return` key.
#. R may ask you to install it in a local directory, starting with "``~``" – the "home directory" of your project, for example ``~/R/x86_64-pc-linux-gnu-library/4.1``. If so, confirm the questions with ``y`` and the installation process should run smoothly.
#. Exit R by pressing `Ctrl+d` or calling the ``q()`` function.

Here is a session for installing `listcompr <https://cran.r-project.org/web/packages/listcompr/index.html>`_ in a :doc:`../terminal`::

    ~$ R

    R version 4.1.2 (2021-11-01) -- "Bird Hippie"
    Copyright (C) 2021 The R Foundation for Statistical Computing
    Platform: x86_64-pc-linux-gnu (64-bit)

    [...]

    > dir.create(path = Sys.getenv("R_LIBS_USER"), showWarnings = FALSE, recursive = TRUE)
    > q()
    Save workspace image? [y/n/c]: n

    ~$ R

    R version 4.1.2 (2021-11-01) -- "Bird Hippie"
    [...]

    > install.packages("listcompr") # this will take several seconds

    Installing package into ‘/home/user/R/x86_64-pc-linux-gnu-library/4.1’
    (as ‘lib’ is unspecified)
    [...]
    * DONE (listcompr)

    The downloaded source packages are in
            ‘/tmp/Rtmpu49yve/downloaded_packages’

    > library(listcompr) # make sure we can load the package
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


.. note::

    After installing a package, restart your Jupyter notbook kernel. Click "Kernel" then select "Restart kernel..." from the dropdown menu.

