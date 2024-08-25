
Purpose
-------

The purpose of the CoCalc API (application programming interface) is to make
essential operations within the CoCalc platform available to automated
clients. This allows embedding of CoCalc services within other products
and customizing the external look and feel of the application.

Protocol and Data Format
------------------------

Each API command is invoked using an HTTPS POST request.
All commands support request parameters in JSON format, with request header
``Content-Type: application/json``. Many commands (those that do not
require lists or objects as parameters)
also accept request parameters as key-value pairs, i.e.
``Content-Type: application/x-www-form-urlencoded``.

Responses are formatted as JSON strings.
Note that it is possible for a request to fail and return
a response code of 200. In that case, the response
string may contain helpful information on the nature of
the failure. In other cases, if the request cannot
be completed, a response code other than 200 may be
returned, and the response body may be a
generic HTML message rather than a JSON string.

Authentication
--------------

A valid API key is required on all API requests. To learn how to create an API key, see :doc:`../apikeys`.

Additional References
---------------------


* The `CoCalc API tutorial <https://share.cocalc.com/share/6eec7a75ce704502e2d557f44c316bf75c5c6ce7/Public/?viewer=share>`_ illustrates API calls in Python.
* The CoCalc PostgreSQL schema definition `src/packages/util/db-schema <https://github.com/sagemathinc/cocalc/blob/master/src/packages/util/db-schema>`_ has information on tables and fields used with the API ``query`` request.
* The API test suite `src/smc-hub/test/api/ <https://github.com/sagemathinc/cocalc/tree/master/src/smc-hub/test/api>`_ contains mocha unit tests for the API messages.
* The CoCalc message definition file `src/packages/util/message.js <https://github.com/sagemathinc/cocalc/blob/master/src/packages/util/message.js>`_ contains the source for this guide.

API Message Reference
---------------------

The remainder of this guide explains the individual API endpoints.
Each API request definition begins with the path of the
URL used to invoke the request,
for example ``/api/v1/change_email_address``.
The path name ends with the name of the request,
for example, ``change_email_address``.
Following the path is the list of options.
After options are one or more sample invocations
illustrating format of the request as made with the ``curl``
command, and the format of the response.

The following two options appear on all API messages
(request parameters are often referred to
as 'options' in the guide):


* **event**\ : the command to be executed, for example "ping"
* **id**\ : uuid for the API call, returned in response in most cases.
  If id is not provided in the API message, a random id will be
  generated and returned in the response.
