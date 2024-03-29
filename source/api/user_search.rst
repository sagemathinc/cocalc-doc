user_search
===========

-  ``id``: A unique UUID for the query
-  ``query``: comma separated list of email addresses or strings such as
   ‘foo bar’ (required)
-  ``admin``: if true and user is an admin, includes email addresses in
   result, and does more permissive search (default: false)
-  ``active``: only include users active for this interval of time
   (default: ““)
-  ``limit``: maximum number of results returned (default: 20)

There are two possible item types in the query list: email addresses and
strings that are not email addresses. An email query item will return
account id, first name, last name, and email address for the unique
account with that email address, if there is one. A string query item
will return account id, first name, and last name for all matching
accounts.

We do not reveal email addresses of users queried by name to non admins.

String query matches first and last names that start with the given
string. If a string query item consists of two strings separated by
space, the search will return accounts in which the first name begins
with one of the two strings and the last name begins with the other.
String and email queries may be mixed in the list for a single
user_search call. Searches are case-insensitive.

Note: there is a hard limit of 50 returned items in the results.

Examples:

Search for account by email.

::

     curl -u : \
       -d query=jd@m.local \
       https://cocalc.com/api/v1/user_search
     ==> {"event":"user_search_results",
          "id":"3818fa50-b892-4167-b9d9-d22d521b36af",
          "results":[{"account_id":"96c523b8-321e-41a3-9523-39fde95dc71d",
                      "first_name":"John",
                      "last_name":"Doe",
                      "email_address":"jd@m.local"}

Search for at most 3 accounts where first and last name begin with ‘foo’
or ‘bar’.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d 'query=foo bar'\
       -d limit=3 \
       https://cocalc.com/api/v1/user_search
     ==> {"event":"user_search_results",
          "id":"fd9b025b-25d0-4e27-97f4-2c080bb07155",
          "results":[{"account_id":"1a842a67-eed3-405d-a222-2f23a33f675e",
                      "first_name":"foo",
                      "last_name":"bar"},
                     {"account_id":"0e9418a7-af6a-4004-970a-32fafe733f29",
                      "first_name":"bar123",
                      "last_name":"fooxyz"},
                     {"account_id":"93f8131c-6c21-401a-897d-d4abd9c6c225",
                      "first_name":"Foo",
                      "last_name":"Bar"}]}

The same result as the last example above would be returned with a
search string of ‘bar foo’. A name of “Xfoo YBar” would not match.

Note that email addresses are not returned for string search items.

Email and string search types may be mixed in a single query:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d 'query=foo bar,jd@m.local' \
       -d limit=4 \
       https://cocalc.com/api/v1/user_search

