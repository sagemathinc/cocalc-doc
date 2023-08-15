=========================================
get-purchases (Python example)
=========================================

Use the ``get-purchases`` endpoint to get purchases made by the owner of the :ref:`API key <get_api_key>`.

Note that the API v2 path has an additional node "purchases", so that the full URL for the endpoint is `https://cocalc.com/api/v2/purchases/get-purchases`

See :doc:`../account/purchases` for the user interface corresponding to this API call.

.. code:: python

    import requests
    from requests.auth import HTTPBasicAuth
    import json
    import pprint
    pp = pprint.PrettyPrinter()

    api_key='YOUR_API_KEY'

    query_str = '{"offset":2, "limit":1}'
    s = requests.Session()
    a = requests.adapters.HTTPAdapter(max_retries=3)
    s.mount('https://', a)
    url = 'https://cocalc.com/api/v2/purchases/get-purchases'
    auth = HTTPBasicAuth(api_key,'')
    headers = {'content-type': 'application/json'}
    r = s.post(url,auth=auth,data=query_str,headers=headers)
    assert r.status_code == requests.codes.ok, \
      f'bad status code {r.status_code}'
    pp.pprint(r.json())

Sample output (not for a real project ID):

.. code-block:: python

    [{'cost': 0.017470052,
      'cost_per_hour': 0.05464481,
      'description': {'project_id': 'd0381938-38be-11ee-9202-2ae9a0a47fef',
                      'quota': {'cost': 0.0546448087431694,
                                'disk_quota': 3000,
                                'enabled': 1691447836428,
                                'member_host': 1,
                                'memory': 2000,
                                'network': 1,
                                'start': 1691447837010},
                      'start': 1691447837010,
                      'stop': 1691448987937,
                      'type': 'project-upgrade'},
      'id': 427,
      'invoice_id': None,
      'notes': None,
      'pending': None,
      'period_end': '2023-08-07T22:56:27.937Z',
      'period_start': '2023-08-07T22:37:17.010Z',
      'project_id': 'd0381938-38be-11ee-9202-2ae9a0a47fef',
      'service': 'project-upgrade',
      'time': '2023-08-07T22:37:17.011Z'}]


You can learn more about this endpoint by viewing the `source code <https://github.com/sagemathinc/cocalc/blob/master/src/packages/next/pages/api/v2/purchases/get-purchases.ts>`_.
