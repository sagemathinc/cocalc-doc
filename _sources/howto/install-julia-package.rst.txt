.. index:: Julia Package
.. _install-julia-packages:

============================
Install Julia Packages
============================


This page describes how to install an Julia package in a CoCalc project.

CoCalc already includes `hundreds of Julia packages <https://cocalc.com/doc/software-julia.html>`_, but you can install even more or update them inside your project.


.. warning::

    Your project **must** have the :ref:`"Internet access" upgrade <project-upgrades>` in order to download software from a remote repository (i.e. the `General Julia package registry <https://github.com/JuliaRegistries/General>`_ to your project.
    The install command will not work unless you :ref:`upgrade your project <project-upgrades>` to have internet access.


Install requests
===================

If a package may have general use but is not already installed in CoCalc,
please open a support request to tell us to install it globally for everyone.
Please include information about special dependencies or a specific example to test it.


Install a package
===================

Install a Julia Package from the Command Line
----------------------------------------------

To install custom Julia packages as a normal user, you have to type this in a terminal before starting Julia::

    export JULIA_DEPOT_PATH=$HOME/julia_depot

When you do this, you will have to reinstall any needed Julia packages that were installed systemwide, since that's the way Julia works.

To have this setting picked up by any terminal in a given project, you can set the ``JULIA_DEPOT_PATH`` environment variable as explained in :ref:`Custom environment variables <project-env-vars>` and restart the project.

After setting ``JULIA_DEPOT_PATH``, follow the usual Julia `pkg documentation <https://docs.julialang.org/en/v1/stdlib/Pkg/>`_:

#. Create or open an existing :doc:`../terminal` file.
#. Type ``]`` (right bracket). You don't have to hit Return.
#. Type type ``add <package_name>`` to add a package; you can provide the names of several packages separated by spaces.
#. Allow some time for the package to be compiled.
#. Hit backspace or Control-C to exit the package manager and Control-D to exit Julia.


Install a Julia Package in a Jupyter Notebook
----------------------------------------------

No special environment setting is needed. Simply do the following in a code cell in a Jupyter notebook that has the default Julia kernel selected::

    import Pkg; Pkg.add("package_name")

and let the install run to completion.


