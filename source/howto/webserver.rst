.. index: Web server

.. _webserver:

==================================
Run a Web Server
==================================

For testing and development, it is possible to run a web server inside a CoCalc project.
Only project collaborators can access it.

If you want to run an exposed web server, you can do it with :doc:`../compute_server`!


Web Server Proxy
================

If your HTTP web server is listening on ``PORT``, you can access it at ::

    https://cocalc.com/PROJECT_ID/server/PORT/

where ``PROJECT_ID`` is your project ID like ``60f9ea81-5bd0-45ae-9965-76de986e101f``, visible in the URL of your project itself and accessible via ``COCALC_PROJECT_ID`` environment variable.

As a test, you can launch a simple server from your project as ::

    python -m http.server 8000

.. warning::

    Your web server must serve **all** IP addresses, **not** just ``localhost``!

For example, you might have to start the service using ``--ip=0.0.0.0`` (the exact flag depends on the service).


.. warning::
    
    Your web server should not rely on absolute URLs.
    

For example, if it serves a file ``index.html`` like this ::

        <a href='/index.html'>HOME!</a>

then when you click this link your browser will try to grab ::

        https://cocalc.com/index.html

instead of ::

        https://cocalc.com/PROJECT_ID/server/PORT/index.html

Obviously, this can't possibly work.

Many web servers, e.g., tensorboard, work fine and do not do this. Others won't work without modification.

.. note::

    This functionality is similar to VS Code proxy.


Port Proxy
==========

If you use ``port`` instead of ``server``, i.e. a URL like ::

    https://cocalc.com/PROJECT_ID/port/PORT/

your web server will get a request for ``/PROJECT_ID/port/PORT/`` rather than for ``/`` as it does with ``server``. Otherwise, everything is the same, including the warnings.


Python Example
==============

Let's put the following code into ``server.py``::

    from http.server import HTTPServer, SimpleHTTPRequestHandler
    import os

    BASE_URL = "/" + os.environ['COCALC_PROJECT_ID'] + '/port/8000'

    class BaseURLHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path.startswith(BASE_URL):
                # Rewrite to strip the prefix before serving files
                self.path = self.path[len(BASE_URL):] or "/"
                return super().do_GET()
            else:
                self.send_error(404, "Not Found")

    if __name__ == "__main__":
        server = HTTPServer(("0.0.0.0", 8000), BaseURLHandler)
        print(f"Serving on https://cocalc.com{BASE_URL}/")
        server.serve_forever()

Then you can start it in a terminal and get something like ::

    ~$ python -m server
    Serving on https://cocalc.com/35dd0d93-f702-4bd4-90dc-f5a3c2117ba2/port/8000/
    192.168.144.61 - - [05/Oct/2025 21:43:27] "GET /35dd0d93-f702-4bd4-90dc-f5a3c2117ba2/port/8000/HW2/ HTTP/1.1" 200 -
    ...


Security
========

Only project collaborators can access the web server via an SSL encrypted connection.
Our proxy server will reject all other requests.
This means you don't have to worry about setting up logins/passwords on whatever web server you run in your project.
If you want to run a web server that is visible to anybody in the world, use :doc:`../compute_server`!


Dynamically Generated Subdomains
================================

Use :doc:`../compute_server`!
