
.. index:: APIv2

=========================
API v2
=========================


With API Version 2, the CoCalc API is being improved and expanded.

Source code for the API v2 implemention is in the `CoCalc public GitHub repository under src/packages/next/pages/api/v2 <https://github.com/sagemathinc/cocalc/tree/master/src/packages/next/pages/api/v2>`_. Each ".ts" file under the ``v2`` directory corresponds to an endpoint in the new API. For example, the "stop" endpoint, which allows you to stop a project, has source code at `https://github.com/sagemathinc/.../api/v2/projects/stop.ts <https://github.com/sagemathinc/cocalc/blob/master/src/packages/next/pages/api/v2/projects/stop.ts>`__ and is called with the URL https://cocalc.com/api/v2/projects/stop.

.. note::

    For security reasons, **API v2 calls must be made with the POST method**. This policy supersedes any comments about the availability of GET that may appear in the source code.

.. _get_api_key:

################################
Get an API Key
################################

To get started with API v2, you will need a CoCalc account and an API key for that account. To learn how to create an API key, see :doc:`../apikeys`.

################################
API v2 Endpoints
################################

The remainder of this guide describes individual API v2 endpoints.

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


