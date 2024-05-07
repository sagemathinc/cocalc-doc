.. index:: Julia Package
.. _install-julia-packages:

============================
Install Julia Packages
============================

.. warning::

    This page describes how to install a Julia package as a user in a CoCalc project. If you are using :doc:`../compute_server`, there is no need to do anything special since you have full ``root`` access and can follow standard instructions.
    
.. hint::

    You *should* consider using :doc:`../compute_server` for research or production work with Julia, since it quickly becomes resource-intensive. Here CoCalc's CEO and Founder William Stein explains how to use Julia on compute servers:

.. raw:: html

    <center><iframe width="640" height="360" src="https://www.youtube.com/embed/OM7R3im9Vgg?si=HyLUtGhG3ORM_HYc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>
    <br/>


Install Requests
===================

CoCalc already includes `hundreds of Julia packages <https://cocalc.com/doc/software-julia.html>`_.
If a package may have general use but is not already installed in CoCalc,
please open a support request to tell us to install it globally for everyone.
Please include information about special dependencies or a specific example to test it.
Please be aware, due to upgrade issues or general conflicts, not all packages can be installed.


Install/Update a Package Yourself
=================================

.. note::

    Your project **must** have the :ref:`"Internet access" upgrade <project-upgrades>` in order to download software from a remote repository (i.e. the `General Julia package registry <https://github.com/JuliaRegistries/General>`_ to your project.
    The install command will not work unless you :ref:`upgrade your project <project-upgrades>` to have internet access.


Command Line / Custom Depot Path
----------------------------------------------

To install custom Julia packages as a normal user, you have to type this in a terminal before starting Julia::

    export JULIA_DEPOT_PATH=$HOME/julia_depot

When you do this, you will have to reinstall any needed Julia packages that were installed system-wide, since that's the way Julia works.

To have this setting picked up by any terminal in a given project, you can set the ``JULIA_DEPOT_PATH`` environment variable as explained in :ref:`Custom environment variables <project-env-vars>` and restart the project.

After setting ``JULIA_DEPOT_PATH``, follow the usual Julia `pkg documentation <https://docs.julialang.org/en/v1/stdlib/Pkg/>`_:

#. Create or open an existing :doc:`../terminal` file.
#. Type ``]`` (right bracket). You don't have to hit Return.
#. Type type ``add <package_name>`` to add a package; you can provide the names of several packages separated by spaces.
#. Allow some time for the package to be compiled.
#. Hit backspace or Control-C to exit the package manager and Control-D to exit Julia.


Command Line / Custom Environment
----------------------------------------------

Julia comes with a packaging mechanism to create
`custom environments <https://pkgdocs.julialang.org/v1/environments/>`_.
This might be what you really need in order to make your code work
in many places.

Note: details about how to set this up and how it works is beyond CoCalc's expertise.

To use such an environment in a Jupyter Notebook,
you will have to setup your own kernel in a CoCalc project.
Follow :ref:`jupyter-custom-kernel` for how to do this – you basically copy one of the global Julia kernels and tweak it's ``kernel.json`` definition.


In a Jupyter Notebook
----------------------------------------------

No special environment setting is needed. Simply do the following in a code cell in a Jupyter notebook that has the default Julia kernel selected::

    import Pkg; Pkg.add("package_name")

and let the install run to completion.

This will cause Julia to install that package locally on top of the globally installed packages.
That might not always work, though.
You might also want to try installing from the command-line,
to get a better view into the console output and to better understand any error messages.

