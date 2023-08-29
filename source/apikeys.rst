========
API Keys
========


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