.. index: Webserver

.. _webserver:

==================================
Run A Webserver
==================================

For testing and development, it is possible to run a small webserver inside a CoCalc project.
Access to it is restricted to only the owner and all collaborators on the project, and nobody else.

Webserver proxy
==================

Given your project's ID is [project_id] like ``60f9ea81-5bd0-45ae-9965-76de986e101f``
and the service is serving on [port],
and it is serving to all ip addresses (**not** just localhost!), then use::

    https://cocalc.com/[project_id]/server/[port]/

to access your HTTP web server.
For example, you might have to start the service using ``--ip=0.0.0.0`` to serve all IPs
(the exact flag depends on the service).

.. warning:

    **CAVEAT:** If the webserver directs the client to make additional requests to the backend for absolute URL's, e.g., the service serves a file index.html like this

    ::

        <a href='/index.html'>HOME!</a>

    then when you click on the link, your browser will try to grab

    ::

        https://cocalc.com/index.html

    instead of

    ::

        https://cocalc.com/[project_id]/server/[port]/index.html

    Obviously, this can't possibly work.

    Many webservers, e.g., tensorboard, work fine and do not do this.
    Other's won't work with modification.


Using the port proxy
===========================

This is similar to above (``port`` instead of ``server``)

::

    https://cocalc.com/[project_id]/port/[port]/

When you visit that URL with your web browser, your web server will get a request for ``/[project_id]/port/[port]/`` rather than for ``/`` like it does with server.
Otherwise, everything is the same, including the big caveat above.

What about security?
==========================

Only the owner and collaborators on the given project can access the webserver via an SSL encrypted connection.
Our proxy server will reject all other requests.
This means you don't have to worry about setting up logins/passwords on whatever webserver you run in your project.
On the other hand, it means that CoCalc is not useful as a platform if you want to run a webserver that is visible to anybody in the world.
If you need that, use some other service.

What about dynamically generated subdomains?
====================================================

Obviously, it would be nice if we could map a project_id and port to a subdomain like

::

    https://[project id].project.cocalc.com

We have not implemented this.


Example Code
===================

Here's a simple example of an HTTP server written using the Python SimpleHTTPServer class.
Open a project and click "+New" then paste in this link, then click the "From Web" button (or use wget or copy/paste into a file)::

    https://gist.githubusercontent.com/williamstein/c69001187923c2a62f1b42126a4a77e8/raw/b50f9410a6d1a55144931ad419affa9466094386/server.py

Then in a terminal type

::

  chmod +x server.py
  ./server.py



Raw Files Server
==================

If you just want an http view of your files, use the raw servers, which is already available by default at ``https://cocalc.com/[project_id]/raw/``.  The point of the above is that you could modify it to provide all sorts of interesting functionality.