log_client_error
================

-  ``id``: A unique UUID for the query
-  ``error``: error string (required)

Log an error so that CoCalc support can look at it.

In the following example, an explicit message id is provided for future
reference.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d id=34a424dc-1731-4b31-ba3d-fc8a484980d9 \
       -d "error=cannot load library xyz" \
       https://cocalc.com/api/v1/log_client_error
     ==> {"event":"success",
          "id":"34a424dc-1731-4b31-ba3d-fc8a484980d9"}

Note: the above API call will create the following record in the
``client_error_log`` database table. This table is not readable via the
API and is intended for use by CoCalc support only:

::

   [{"id":"34a424dc-1731-4b31-ba3d-fc8a484980d9",
     "event":"error",
     "error":"cannot load library xyz",
     "account_id":"1c87a139-9e13-4cdd-b02c-e7d41dcfe921",
     "time":"2017-07-06T02:32:41.176Z"}]

