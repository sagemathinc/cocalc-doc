
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
the failure. In other cases, if the request cannnot
be completed, a response code other than 200 may be
returned, and the response body may be a
generic HTML message rather than a JSON string.

Authentication
--------------

A valid API key is required on all API requests.

To obtain a key manually, log into
CoCalc and click on Settings (gear icon next to user name at upper
right), and look under ``Account Settings``.
With the ``API key`` dialogue, you can create a key,
view a previously assigned key, generate a replacement key,
and delete your key entirely.

.. index:: API; get_api_key


It is also possible to obtain an API key using a javascript-enabled automated web client.
This option is useful for applications that embed CoCalc
in a custom environment, for example `juno.sh <https://juno.sh>`_\ ,
the iOS application for Jupyter notebooks.
Visiting the link :samp:`https://cocalc.com/app?get_api_key=myapp`,
where "myapp" is an identifier for your application,
returns a modified sign-in page with the banner
"CoCalc API Key Access for Myapp".
The web client must
sign in with credentials for the account in question.
Response headers from a successful sign-in will include a url of the form
:samp:`https://authenticated/?api_key=sk_abcdefQWERTY090900000000`.
The client should intercept this response and capture the string
after the equals sign as the API key.

Your API key carries access privileges, just like your login and password.
**Keep it secret.**
Do not share your API key with others or post it in publicly accessible forums.

Additional References
---------------------


* The `CoCalc API tutorial <https://share.cocalc.com/share/6eec7a75ce704502e2d557f44c316bf75c5c6ce7/Public/?viewer=share>`_ illustrates API calls in Python.
* The CoCalc PostgreSQL schema definition `src/smc-util/db-schema <https://github.com/sagemathinc/cocalc/blob/master/src/smc-util/db-schema>`_ has information on tables and fields used with the API ``query`` request.
* The API test suite `src/smc-hub/test/api/ <https://github.com/sagemathinc/cocalc/tree/master/src/smc-hub/test/api>`_ contains mocha unit tests for the API messages.
* The CoCalc message definition file `src/smc-util/message.js <https://github.com/sagemathinc/cocalc/blob/master/src/smc-util/message.js>`_ contains the source for this guide.

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
