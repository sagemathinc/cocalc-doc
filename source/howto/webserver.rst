.. index: Webserver

.. _webserver:

==================================
Run A Webserver
==================================

For testing and development, it is possible to run a small webserver inside a CoCalc project.
Access to it is restricted to only the owner and all collaborators on the project, and nobody else.

If you want to run an exposed webserver, you can do it with :doc:`../compute_server`!


Webserver proxy
==================

If your project's ID is ``PROJECT_ID`` like ``60f9ea81-5bd0-45ae-9965-76de986e101f``
and the service is serving on ``PORT``
to **all** ip addresses (**not** just localhost!), you can use::

    https://cocalc.com/PROJECT_ID/server/PORT/

to access your HTTP web server.
For example, you might have to start the service using ``--ip=0.0.0.0`` to serve all IPs
(the exact flag depends on the service).

.. warning::

    If the webserver directs the client to make additional requests to the backend for absolute URL's, e.g., the service serves a file index.html like this

    ::

        <a href='/index.html'>HOME!</a>

    then when you click on the link, your browser will try to grab

    ::

        https://cocalc.com/index.html

    instead of

    ::

        https://cocalc.com/PROJECT_ID/server/PORT/index.html

    Obviously, this can't possibly work.

    Many webservers, e.g., tensorboard, work fine and do not do this.
    Others won't work without modification.


Using the port proxy
===========================

This is similar to above (``port`` instead of ``server``)

::

    https://cocalc.com/PROJECT_ID/port/PORT/

When you visit that URL with your web browser, your web server will get a request for ``/PROJECT_ID/port/PORT/`` rather than for ``/`` as it does with server.
Otherwise, everything is the same, including the warning above.


What about security?
==========================

Only the owner and collaborators on the given project can access the webserver via an SSL encrypted connection.
Our proxy server will reject all other requests.
This means you don't have to worry about setting up logins/passwords on whatever webserver you run in your project.
If you want to run a webserver that is visible to anybody in the world, use :doc:`../compute_server`!


What about dynamically generated subdomains?
====================================================

Use :doc:`../compute_server`!


Raw Files Server
==================

If you just want an HTTPS view of your files, use the raw server, which is already available by default at ``https://cocalc.com/PROJECT_ID/raw/``.
