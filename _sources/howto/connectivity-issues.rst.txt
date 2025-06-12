.. index:: Timeout; loading CoCalc
.. index:: Connectivity Issues; Timeout
.. _timeout-loading-cocalc:

.. index:: Connectivity Issues
.. _connectivity-issues:

==================================
Connectivity Issues
==================================


**Quick Tips**


* Hold down **Shift** and click your browser's **Reload** button to refresh the CoCalc tab.
  Sometimes this simple action resolves the problem.
* Restart your browser.
* Update your browser to the latest version or try a different browser.
* Restart your computer and/or Internet device, i.e. WiFi router or cable modem.
* Keep reading!

If you follow the steps below, still have a problem, and contact CoCalc support, please let us know what you have tried already.

.. contents::
     :local:


Step 1: Check Your Connection
-----------------------------

Check if the upper right corner of your CoCalc tab has a red "WiFi icon" or the message "Connecting..." or "Disconnected". If that is the case, can you use other websites? If not, perhaps your Internet connection is cut off.

Once a broken connection is reestablished, your files should be saved and everything should return to normal. During the period of disconnection, the green **Save** button will be replaced by a red "NOT saved!" warning.


Step 2: Check CoCalc Status
---------------------------

Visit https://status.cocalc.com/ to see if there is an outage for the entire system.

One of the advantages of cloud computing is that if a server you are connected to goes down, then you can automatically be reconnected to some other server. You can also explicitly request to be connected to a different front-end server. To do that click on the connection information in the top right corner and then on the **Reconnect** button.


Step 3: Clear Cache
-------------------

Your browser or an intermediate server may attempt to cache too much.
The symptom for this malady is if you can load the page but it keeps timing out, or if it doesn't load up properly.
Reload the website with the **Shift**-key held down - that tells the browser to ignore your local cache. Alternatively, clean your browser's cache directly via its interface.


.. index:: Connectivity Issues; no valid remember_me

Step 4: Clear Cookies
---------------------

Getting the message *Error: no valid remember_me token* when trying to sign into CoCalc is usually a sign of stale browser cookies.

This situation can happen to users who attempt to use multiple CoCalc accounts, even if they are not attempting to do so simultaneously. We have an entire page devoted to strategies to make it easy to :ref:`painlessly operate with multiple CoCalc accounts <multiple-accounts>`.

For a quick workaround, try to connect to CoCalc by opening up a new "private browsing window" or "incognito window." While inside those special windows, your old cookies will not be active and any new cookies you are given will not affect the main browser.

The definitive solution is to clear all browser cookies related to cocalc.com, or use a different browser.


Step 5: Update Your Browser
---------------------------

We do NOT support old versions of web browsers! As we add new features, fix bugs, and update dependencies, there is higher and higher chance that we require some functionality not supported by older versions.


Step 6: Disable Extensions
--------------------------

Another common source of problems is **installed browser extensions** which might inject JavaScript code into any website. It is quite likely that the injected code may not play along well with the JavaScript code of CoCalc.

Some extensions, for example ad blockers, block certain external websites. It may be necessary to whitelist cocalc.com if you are running one of these. In addition, some libraries used by CoCalc are loaded via CDN (content delivery network) instead of CoCalc's own servers. Blocking their access (or more generally, blocking any 3rd party scripts from a website) could cause problems. The same can happen with other firewall or anti-virus software on your computer.

The site-blocking extension `ScriptSafe <https://github.com/andryou/scriptsafe>`_ used with Chrome-based browsers, including `Iridium <https://iridiumbrowser.de/>`_, has been reported to cause connection problems with CoCalc.

With Google Chrome, extensions are disabled in "incognito mode". You can also go to the Settings and disable extensions, or run Google Chrome with the command-line switch `--disable-extensions`.

For Firefox, see `Firefox Disable or remove Add-ons <https://support.mozilla.org/en-US/kb/disable-or-remove-add-ons>`_.

If incognito mode works, then the problem is either:

* Cookies and other local data associated to cocalc.com are somehow bad (deleting them would fix it), or
* A browser extension is mangling/breaking cocalc.com -- disabling that extension would fix it.


Step 7: Try Google Chrome
-------------------------

Overall, CoCalc works best with the most recent version of Google Chrome. If you are not using it as your main browser, please install the latest version to check if CoCalc works with it.


Step 8: Reduce Traffic
----------------------

There are situations where your computer or your router cannot handle all the ongoing traffic.
For example, you are simultaneously watching a video or participate in a video chat.
Or, in the case of a router sharing internet access, another device is used to watch videos or play games.
Then messages sent to CoCalc and back may be slowed down or even dropped entirely.
Besides a poor experience of using CoCalc,
you could also see sporadic "disconnect" warnings.

If possible, turn off other traffic-heavy applications or connect to a different network.


Step 9: Free Memory and CPU
---------------------------

If you have multiple applications open on your computer or a lot of browser tabs, your browser may stall because of too high memory and/or CPU usage. Try closing some applications and tabs, then reload CoCalc tab.

If you are using Google Chrome, you can see CPU and memory usage for each
and every tab in the `Chrome Task Manager`_. This way, you can see which tabs are memory hogs (whether they are CoCalc
or something else) and decide for yourself if you wish to close them.

.. _Chrome Task Manager: https://www.google.com/search?q=chrome+task+manager


Step 10: Remove Malware
-----------------------

If you experience issues like frequent reloads, see strange advertising banners across the page, or additional odd banners around the page, then you might be a victim of some tool or virus injecting additional HTML code into webpages in your browser. Such malicious software can serve several purposes (e.g. tracking you, showing you ads, just disrupting your connectivity), and is almost always considered highly undesirable.

For Google Chrome there is the `Chrome Cleanup Tool <https://www.google.com/chrome/cleanup-tool/>`_ which might help you fix this.

For Firefox, you might want to check
the `disable add-ons <https://support.mozilla.org/en-US/kb/disable-or-remove-add-ons>`_ page, which might display for you an undesired add-on that might have been installed on your browser without your knowledge.


Step 11: Check DNS Settings
---------------------------

It is possible that you might be a victim of some malicious software changing your DNS  (Domain Name Service) server and re-routing you through a bad proxy. It may also be the result of a bad configuration on your computer, an over-zealous employer, or hotel.

Check your DNS settings and try setting `8.8.8.8 <https://developers.google.com/speed/public-dns/docs/using>`_ as your only DNS server to see if this helps. That is a free DNS service provided by Google. Alternatively (or additionally) you can setup `1.1.1.1 <https://1.1.1.1/>`_ by Cloudflare.


.. _websocket-test:

Step 12: Test WebSockets
------------------------

WebSockets are necessary to connect to CoCalc.
A broken router configuration (e.g. in a larger organization like a university) or some firewall software trying to inspect your traffic might cause troubles.
You can check that WebSockets are working for you by visiting https://echo.websocket.org/.ws and sending yourself a test message.
