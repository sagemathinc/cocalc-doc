
API Examples & Howto
====================

.. index:: pair: API; Copy files


Copy a file between projects
----------------------------

First, save your API key in a file ``api.key``.
Then, we use the `requests <https://requests.readthedocs.io/en/master/>`_ library to issue calls:

.. code-block:: python

   key = open('api.key').read().strip()
   import requests as r

Copy request:

.. code-block:: python

   data = {
       'src_project_id': '...',
       'src_path': 'cocalc-api/api-demo.ipynb',
       'target_project_id': '...',
       'wait_until_done': False
   }

   req = r.post('https://cocalc.com/api/v1/copy_path_between_projects',
                auth=(key, ''),
                data=data)
   res = req.json()
   res

response ``res``\ :

.. code-block:: python

   {'event': 'copy_path_between_projects_response',
    'id': '52818dfe-b580-404e-89e6-9845fac7076c',
    'copy_path_id': '65cd2079-098d-4147-bb54-12d44cebb8cb',
    'note': 'Query copy_path_status with the copy_path_id to learn if the copy operation was successful.'
   }

Now, we wait a few seconds. Then, we check the status using ``copy_path_id``\ :

.. code-block:: python

   data = {
       'copy_path_id': res['copy_path_id']
   }

   req = r.post('https://cocalc.com/api/v1/copy_path_status',
                auth=(key, ''),
                data=data)
   res = req.json()
   res

which gives

.. code-block:: python

   {'event': 'copy_path_status_response',
    'id': 'abc3ca91-1388-4208-bdeb-540054e5bcaf',
    'data': {'copy_path_id': 'da3a8eaf-14df-4bf8-9131-13bcb9c7e9e5',
     'time': '2020-11-03T16:20:54.222Z',
     'source_project_id': '...',
     'source_path': 'cocalc-api/api-demo.ipynb',
     'target_project_id': '...',
     'target_path': 'cocalc-api/api-demo.ipynb',
     'overwrite_newer': False,
     'delete_missing': False,
     'backup': False,
     'started': '2020-11-03T16:20:54.234Z',
     'finished': '2020-11-03T16:20:55.177Z'}
   }

Note: ``started`` and ``finished`` being part of the response, signals it did work.

.. index:: pair: API; IFrame


Embedding in an IFrame
----------------------

Here are notes on integrating CoCalc in an IFrame in a web application using the CoCalc API.
You should be able to create a proof of concept using the API introduction above and these notes.


#. You need an account with an API key. You can get an API key via the UI or here using the :doc:`../api/create_account` API call.
#. You can create several accounts. If you are running the CoCalc Docker image, you probably want one account `to be an admin <https://github.com/sagemathinc/cocalc-docker#make-a-user-an-admin>`_ and then have additional accounts for each actual user of your platform.
#. You have to create at least one project.
   Note: *The production website runs each project in their own container.*
   *This means you might want to create several projects to get proper isolation.*
#. With the API, you can :doc:`copy files between projects <../api/copy_path_between_projects>` or :doc:`write to a file <../api/write_text_file_to_project>`. It's also possible to :doc:`run arbitrary commands <../api/project_exec>`.
#. To show a notebook to a user (and just the notebook) you need to do this:

   * :doc:`get a fresh auth token <../api/user_auth>`
   * make an IFrame in your website, which points to a project and file, and ends with ``?auth_token=...&fullscreen=kiosk``.
     The parameter ``fullscreen=kiosk`` removes the UI.
     A full example might look like this
     ``https://cocalc.com/projects/.../files/calculate.ipynb?auth_token=...&fullscreen=kiosk&session=``

IFrame communication
--------------------

This is a communication channel to improve working with an embedded CoCalc instance.
It gives the parent page the ability to send command-messages to CoCalc (e.g. opening a specific page, etc.) and receiving responses.

.. warning::

     The IFrame communication might be currently broken.
     Please check `issue #6059 <https://github.com/sagemathinc/cocalc/issues/6059>`_ for the current status.


The underlying technology is `window.postMessage <https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage>`_.

The parent page must be served using ``https``\ !

.. note::

    This is *beta* and only available for specific domains.
    Please contact us if you want to use this.


To get started, you just have to embed the main ``/app`` endpoint in an IFrame's ``src`` like that:

   https://cocalc.com/app?auth_token=......&fullscreen=kiosk&session=

Once CoCalc is ready, the loading screen shows a green banner of confirmation.

**Sending messages** Use `postMessage <https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage>`_ on the ``contentWindow`` of CoCalc's IFrame to send messages.
E.g. if your IFrame has the ``id="cocalc"``\ , run ``cocalc = document.getElementById("cocalc").contentWindow;`` and then ``cocalc.postMessage(payload, "https://cocalc.com")``. ``payload`` is the message, which is explained below.

**Receiving message**


#. write a callback function like ``function replies(mesg) { console.log(mesg.data); }``.
#. Possibly check if ``mesg.origin`` is really CoCalc's domain.
#. Hook up this callback via ``window.addEventListener("message", replies, false);``.

**Messages sent to CoCalc** have the following structure. The ``action`` field is mandatory.

.. code-block:: python

   {
     action: "[command]",
     field1: ...,
     field2: ...
   }


Each message has a **response**\ , usually containing ``{status: "ack|done|error", ...}``.

In particular, **error responses** have the structure ``{status: "error", mesg: "[error message]", ...}``.

Available commands and their responses:


* ``open`` – open a specific file in a project.

  * fields:

    * ``project_id`` – the UUID of the project
    * ``path`` – the location relative to the home directory. e.g. ``notebook.ipynb`` or ``subdir1/file.md``.

  * responses:

    #. acknowledgement of command (project will start, file will open): ``{ status: "ack", ... }``
    #. file editor is opened and loading of content starts: ``{ status: "done", ... }``

* ``closeall`` – this closes all open files

  * response: ``{status: "done", mesg: "all files are closed"}``

* ``status`` – returns a snapshot of CoCalc's overall status. In particular during starting CoCalc, querying this for a response is useful to know when CoCalc is available and connected to the front-end servers.

  * response:

    * ``connection`` – more detailed information about the connection quality, ping time, etc.
    * ``open_files`` – mapping of ``project_id`` to a list of paths.
