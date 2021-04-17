.. index:: Pluto notebooks
.. index:: Julia; pluto notebooks

=========================
Pluto Notebooks for Julia
=========================

Here are instructions for running a Pluto notebook on CoCalc.

*************
Install Pluto
*************

Note that in CoCalc it's necessary right now to install Pluto. To do that, run the following in a CoCalc Linux Terminal::

    export JULIA_DEPOT_PATH=$HOME/julia_depot
    $ julia
    julia> ]
    pkg> add Pluto
    # wait a few seconds
    # then exit package manager with ^C

This only needs to be done once.

*****************
Launch a Notebook
*****************

Run the following in a CoCalc Linux Terminal to get the ID of the current project (or you can copy the project ID from within the URL of any file in the current project)::

    $ echo $COCALC_PROJECT_ID
    12345678-1234-1234-1234-123456789012

Then start Julia::

    $ julia
    julia> Pluto.run(launch_browser = false, require_secret_for_access = false, host="0.0.0.0")
    
Open a browser tab to the following, substituting your project ID where indicated::

    https://cocalc.com/PROJECT_ID/server/1234/

If you get a gateway timeout the first time, hit refresh to give the notebook more time to launch.

Enjoy.

**********
References
**********

* Read more about Pluto at the `Pluto github repo <https://github.com/fonsp/Pluto.jl>`_.

* Github issue discussing `Pluto on CoCalc <https://github.com/fonsp/Pluto.jl/discussions/1084#discussioncomment-620582>`_.

* Discussion of ongoing support for Pluto in CoCalc `Support Pluto notebooks #5270 <https://github.com/sagemathinc/cocalc/issues/5270>`_.


