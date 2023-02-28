=================================
Information for Firewall Admins
=================================

URLs and Port Numbers
=================================


Q: What URLs and ports should I whitelist on my organization's firewall to enable access to Cocalc.com services?

A: Enable URLs to domain `cocalc.com` and its subdomains. Enable connections to TCP port 443 for HTTPS, and to port 22 to allow access via the SSH protocol. In the design of CoCalc.com, we have worked to ensure that all services are provided exclusively via port 443, plus SSH access when the user has properly configured encryption keys. Connections to CoCalc.com on port 80 are redirected to port 443, so you might want to enable that, too

WebSockets
==========

Most of CoCalc's services use websocket connections, so it's necessary to allow this protocol over port 443.

It may be helpful to test your configuration for websocket connections on a 3rd party website. See :ref:`Do WebSocket connections work? <websocket-test>` in the CoCalc troubleshooting guide for more info.

Browser tools can help to analyze websocket traffic. See for example
`WebSocket binary message viewer <https://developer.chrome.com/blog/new-in-devtools-74/#binary>`_ for Google Chrome
and
`Inspecting web sockets <https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor/Inspecting_web_sockets>`_ for Firefox.
