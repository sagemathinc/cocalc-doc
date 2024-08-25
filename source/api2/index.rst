
.. index:: APIv2

=========================
API v2
=========================

Version 2 of the CoCalc API introduces a variety of improvements, including more structure, functionality, and better developer support. In particular, we validate our API v2 endpoints against an `OpenAPI <https://www.openapis.org/>`_ schema so that our documentation expands in lockstep with our API implementation. That documentation can be found at `https://cocalc.com/api/v2 <https://cocalc.com/api/v2>`_ - we're adding new endpoints every week, so be sure to check it out regularly if you're interested in developing against the CoCalc HTTP API!

Source code for the API v2 implementation is in the
`CoCalc public GitHub repository under src/packages/next/pages/api/v2 <https://github.com/sagemathinc/cocalc/tree/master/src/packages/next/pages/api/v2>`_. Each ".ts" file under the ``v2`` directory corresponds to an endpoint in the new API. For example, the "stop" endpoint, which allows you to stop a project, has source code at `https://github.com/sagemathinc/.../api/v2/projects/stop.ts <https://github.com/sagemathinc/cocalc/blob/master/src/packages/next/pages/api/v2/projects/stop.ts>`__ and is called with the URL https://cocalc.com/api/v2/projects/stop.

.. note::

    For security reasons, **API v2 calls must be made with the POST method**. This policy supersedes any comments about the availability of GET that may appear in the source code.

.. _get_api_key:

################################
Get an API Key
################################

To get started with API v2, you will need a CoCalc account and an API key for that account. To learn how to create an API key, see :doc:`../apikeys`.

################################
API v2 Examples
################################

To help get a feel for how one might work with the CoCalc HTTP API, we've added some guides and explanations for a handful of useful endpoints below. These are a great jumping-off point for getting started with writing your own integrations with the CoCalc API.

.. toctree::
   :caption: API v2 General-Purpose Endpoints
   :maxdepth: 1

   directory-listing
   get-purchases
   latex
   stop
   user-query

.. toctree::
   :caption: API v2 Partner Endpoints
   :maxdepth: 1

   email-address-from-account-id
   purchasing-licenses


