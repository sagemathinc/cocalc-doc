=============================
user-query
=============================

Use the ``user-query`` endpoint to get the email address and account_id for the owner of the API key. A request header is set because the query is a JSON string. The example sends output to the linux command "jq" to format the output nicely.

.. code:: bash

    x='sk_xxxxx' # your API key
    q='{"query":{"accounts":{"account_id":null,"email_address":null}}}'

    curl -sk \
      -u $x: \
      -d $q \
      -H 'Content-Type: application/json' \
      https://cocalc.com/api/v2/user-query | jq

    echo

    ### sample output (not from a real account):

    {
      "query": {
        "accounts": {
          "account_id": "e32a26f8-262c-11ed-8a33-8358017cec89",
          "email_address": "jane.doe@example.com"
        }
      }
    }

You can learn more about the ``user-query`` endpoint by viewing the source code at `https://github.com/sagemathinc/.../api/v2/user-query.ts <https://github.com/sagemathinc/cocalc/blob/master/src/packages/next/pages/api/v2/user-query.ts>`__.
