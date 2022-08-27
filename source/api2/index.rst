
.. index:: API

=========================
API v2
=========================

.. contents::
   :local:
   :depth: 2

################################
Introduction
################################

*New in April 2022*

With API v2, the CoCalc API is being improved and expanded.

Source code for the API v2 implemention is in the `CoCalc public GitHub repository under src/packages/next/pages/api/v2 <https://github.com/sagemathinc/cocalc/tree/master/src/packages/next/pages/api/v2>`_. Each ".ts" file under the ``v2`` directory corresponds to an endpoint in the new API. For example, the "stop" endpoint, which allows you to stop a project, is at https://cocalc.com/api/v2/projects/stop.

.. note::

    For security reasons, **API v2 calls must be made with the POST method**. This policy supersedes any comments about the availability of GET that may appear in the source code.

################################
Get an API Key
################################

To get started with API v2, you will need a CoCalc account and an API key for that account. Visit the link `Account - API Key <https://cocalc.com/config/account/api>`_ under your account settings to create and view your API key. A CoCalc API key will be a text string beginning with the symbols "sk\_"


################################
API v2 Examples
################################

*****************************
stop
*****************************

Use the ``stop`` endpoint to stop a CoCalc project, given its project_id. Note that this endpoint is in the ``v2/projects/`` subdirectory.

.. code:: bash

    x='sk_xxxxx' # your API key

    # project_id of the project you want to stop
    p='304506b4-262e-11ed-a279-2f22f36cbe91'

    curl -sk \
      -u $x: \
      -d project_id=$p \
      https://cocalc.com/api/v2/projects/stop

    ### output
    {}

*****************************
user-query
*****************************

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


*****************************
latex
*****************************

Use the ``latex`` endpoint to compile a latex document.

.. code:: bash

    x='sk_xxxxx' # your API key

    # c is the latex document as a text string
    c='\documentclass{article}\begin{document}\section{Main Section}Hello.\end{document}'

    curl -sk \
      -u $x: \
      -d path=/tmp/d.tex \
      -d content=$c \
      https://cocalc.com/api/v2/latex | jq '.url'
      
    echo
    
    ### sample output is a url
    ### browse to this link to see the compiled pdf document
    "https://cocalc.com/blobs/tmp/d.pdf?uuid=36862b42-2634-11ed-889d-3b8b6aedd65b"


