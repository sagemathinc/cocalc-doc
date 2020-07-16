.. index:: Connectivity Issues
.. _connectivity-issues:

==================================
Debugging connectivity issues
==================================

There are numerous reasons why you could experience a problematic connection when accessing `CoCalc <https://cocalc.com>`_.

This FAQ/Help page consists of

.. contents::
   :local:
   :depth: 1


**Remember:** if you don't find what you need, or if you'd like to ask a question, then email `help@cocalc.com <mailto:help@cocalc.com>`_ at any time. We'd love to hear from you! Please include a link (the URL address in your browser) to any relevant project or document, as part of your email.

.. note::

    **Quick Solution**

    * Hold down the ``Shift``-key and click your browser's **reload** button to refresh the CoCalc tab.
      Sometimes this simple action resolves the problem.
    * **Restart your browser.** Maybe even restart your computer!
    * You might be using an old, unsupported browser.
      Check for updates available to the browser you are using, or switch to the latest version of a different browser.

    If this doesn't help, try additional diagnostic steps mentioned below.


Process for Debugging Connectivity
==================================================

The following multi-step process will help you identify the problem. If you still have a problem and are contacting CoCalc support, it saves time if you let us know what you found out from following these steps:

Step 1: Try connecting with the latest version of Google Chrome.
------------------------------------------------------------------

If you are not using Google Chrome, or are using an outdated version of it, install the latest Chrome and test your connection again.

Step 2: Make sure you are running a very recent version of Google Chrome, Safari, Firefox, or Edge.
-------------------------------------------------------------------------------------------------------

**We do NOT support old versions of web browsers!!**
For example, there's zero chance CoCalc will work at all with a web browser from e.g. 2016.

When CoCalc starts, it checks your browser version and will report this to you.

Overall, CoCalc works best with the most recent version of Google Chrome.

Step 3: Double check if are you connected at all.
-------------------------------------------------------------------------------------------------------

Look in the upper-right hand corner of any CoCalc web page. You will see there the "wifi symbol" and to the right of it, a number of milliseconds (e.g. 43 ms). This means that you are connected to CoCalc, with a latency of 43 ms. (For those unfamiliar with the idea of latency, after your computer sends some data packet, it will take 43 ms to arrive at the CoCalc server.)

Many times, it can happen that your internet connection is cut off. For example, in a cafe or coffee shop, the internet access may be shutdown during peak hours. Alternatively, in a residence, a roommate might have inadvertently unplugged the wireless router. When this happens, the WiFi symbol and the latency indicator will be replaced by a red rectangle with the word "disconnected." If you restore your wireless connection, then you'll see a yellow rectangle with the word "connecting..."

Once a broken connection is reestablished, your files will be saved and everything returns to normal. During the period of disconnection, the green "Save" button will be replaced by a red warning that says "NOT saved!" As you can see, you will always know whether or not your changes have reached the server.

.. note::

    Sometimes, it might be necessary to entirely close and restart your browser.
    If that doesn't help, restart your computer.


Step 4: Network congestion?
-------------------------------------------------------------------------------------------------------

The internet connects billions of machines worldwide via a sophisticated network.
All the data sent around is chopped into small pieces (packages)
and labeled with source and destination addresses.
While you are working on CoCalc, a constant stream of such packages is sent back and forth
between your computer and the servers in the cloud.

There are situations where your computer or your router cannot handle all the ongoing traffic.
For example, you are simultaneously watching a video or participate in a video chat.
Or, in the case of a router sharing internet access, another device like a smart TV
is streaming a new episode of your favourite series.

Then, these packages sent back and forth with CoCalc
are slowed down or even dropped entirely.
Besides a poor experience of using CoCalc,
you could also see erratically high ping times or sporadic "disconnect" warnings.

Step 5: Do you have tons of tabs open?
---------------------------------------------

Some power users will have several browser tabs open simultaneously, which is fine.
However, having too many open causes high memory usage by your web browser,
which might make your browser stall. After closing a few tabs, reloading the tab that
you are currently working on (just like you might reload any other web page)
will clean that process and possibly free up some memory.

If you are using Google Chrome, you can see cpu and memory usage for each
and every tab in the `Chrome Task Manager`_. This way, you can see which tabs are memory hogs (whether they are CoCalc
or something else) and decide for yourself if you wish to close them.

.. _Chrome Task Manager: https://www.google.com/search?q=chrome+task+manager

Step 6: Is your browser (or an intermediate server) attempting to cache too much?
-------------------------------------------------------------------------------------------------------

The symptom for this malady is if you can load the page but it keeps timing out, or if it doesn't load up properly. If you are experiencing those symptoms, then either old copies of the page that you are working on are cached on some server, between yourself and the CoCalc server, or perhaps your browser is caching them locally.

In this situation, the fix is easy. Just **reload the website with the Shift-key held down** (that tells the browser to ignore your local cache), or clean your browser's cache directly via its interface.

Browser caches are an important way of speeding up your internet connection. However, the methods and strategies that work for static web content and relatively straightforward websites do not always work well for sophisticated and complex systems like CoCalc. For example, hotels often have aggressive cache servers, because a large portion of their guests will access the same handful of websites (e.g. to check the weather, get navigation, or print boarding passes.)

Step 7: Does the problem relate to stale cookies?
-------------------------------------------------------------------------------------------------------

This situation can happen to users who are attempting to use two different CoCalc accounts, even if they are not attempting to do so simultaneously. We have an entire page devoted to strategies to make it easy to :ref:`painlessly operate with multiple CoCalc accounts <multiple-accounts>`.

For a quick fix, try to connect to CoCalc by opening up a "new private browsing window" or "new incognito window." While inside those special windows, your old cookies will not be active and any new cookies you are given will not affect the main browser.

Step 8: Have you installed browser extensions ("add-on"s) or enabled blocking software on your computer?
----------------------------------------------------------------------------------------------------------------------

Another source of problems is **installed browser extensions**. Extensions might inject JavaScript code into the website. In such a situation, it is likely that the injected code does not play along well with the JavaScript code of CoCalc.

Some extensions, for example ad blockers, block certain external websites. It may be necessary to whitelist cocalc.com if you are running one of these. In addition, some libraries used by CoCalc are loaded via CDN (content delivery network) instead of Cocalc's own servers. Blocking their access (or more general, blocking any 3rd party scripts from a website) could cause problems. The same can happen with other firewall or anti-virus software on your computer.

The site-blocking extension `ScriptSafe <https://github.com/andryou/scriptsafe>`_ used with Chrome-based browsers, including `Iridium <https://iridiumbrowser.de/>`_, has been reported to cause connection problems with CoCalc.

With Google Chrome, you can go to the Settings and disable some. Alternatively, you can run Google Chrome with the command-line switch `--disable-extensions`. Incidentally, extensions are disabled in "incognito mode", so "Step 3" above should have taken care of this.

In Firefox, it is very easy to `disable add-ons <https://support.mozilla.org/en-US/kb/disable-or-remove-add-ons>`_ by clicking on that link.

Step 9: Are the CoCalc servers down?
-------------------------------------------------------------------------------------------------------

This is extremely unlikely. One of the advantages of cloud computing is that if a server goes down, then you can automatically be reconnected to some other server. You can also explicitly request to be connected to a different front-end server:

1. Click on the connection information in the top right corner, a dialog should pop up.
2. In it, click the "Reconnect" button.

The following webpage will show you a bit of technical information about the running servers:

https://cocalc.com/stats

However, if that link were to time out, or if there is nothing to see, then there is a problem with either your internet connectivity or the CoCalc website. If your browser tells you about any issues while loading that link, then the problem is likely to be on your end.

Maybe also check **other** websites:

- If a page like https://google.com are also down, it is an indicator that your internet connection is broken.
- You can also check CoCalc's status indirectly via services like https://down.com/

Step 10: Is your computer infected with malware?
-------------------------------------------------------------------------------------------------------

If you experience issues like frequent reloads, see strange advertising banners across the page, or additional odd banners around the page, then you might be a victim of some tool or virus injecting additional HTML code into webpages in your browser. Such malicious software can serve several purposes (e.g. tracking you, showing you ads, just disrupting your connectivity), and is almost always considered highly undesirable.

For Google Chrome there is the `Chrome Cleanup Tool <https://www.google.com/chrome/cleanup-tool/>`_ which might help you fix this.

For Firefox, you might want to check
the `disable add-ons <https://support.mozilla.org/en-US/kb/disable-or-remove-add-ons>`_ screen, which might display for you an undesired add-on that might have been installed on your browser without your knowledge.

Step 11: Is the problem with your DNS (Domain Name Service) settings?
-------------------------------------------------------------------------------------------------------

It is possible that you might be a victim of some malicious software changing your DNS server and re-routing you through a bad proxy server. This is not always the result of hacking. It can be a bad configuration on your computer, the result of an over-zealous employer, or hotel.

Check your DNS settings and try setting `8.8.8.8 <https://developers.google.com/speed/public-dns/docs/using>`_ as your only DNS server to see if this helps. That's a free DNS service provided by Google. Alternatively (or additionally) you can setup `1.1.1.1 <https://1.1.1.1/>`_ by Cloudflare.

Step 12: Is your browser out of date or otherwise incompatible with CoCalc?
-------------------------------------------------------------------------------------------------------

The problem may be solved by using another browser, in particular Google Chrome, or by updating your browser to a recent version if it is outdated.

Step 13: Do WebSocket connections work?
-------------------------------------------------------------------------------------------------------

The following test page checks if WebSockets do work for you.
They're necessary to "Connect" with CoCalc.

1. Open this page: https://www.websocket.org/echo.html
2. Enable "secure websocket TLS"
3. Then click "Connect" and finally,
4. Send yourself a test message.

On the right hand side in the output box, the same message should come back and hence confirm that encrypted websocket connections work for you.

A broken router configuration (e.g. in a larger organization like a university) or some firewall software trying to inspect your traffic might cause troubles.


FAQ
============

Question: I don't see any icons, but everything else works.
-------------------------------------------------------------------------------------------------------

You are most likely using a customized font or an extension to customize fonts via CSS (Cascading Style Sheets), in your web browser.
This interferes with the font displaying the images for the icons.

The best solution is to disable the extension, in your browser.

Question: I can access some of my files/projects in my CoCalc account but not others in that same account. What's wrong?
---------------------------------------------------------------------------------------------------------------------------

Sometimes this can happen if you are using multiple CoCalc accounts in the same browser.
This can happen even if you are not using two different accounts simultaneously.

We have a short help page, :ref:`multiple-accounts` which discusses this.
The suggestions there will make it work very smoothly for you.

.. index:: Timeout; loading CoCalc
.. index:: Connectivity Issues; Timeout
.. _timeout-loading-cocalc:

Question: I see the error message "Timeout while loading CoCalc" instead of the CoCalc landing page.
-------------------------------------------------------------------------------------------------------

If you see the error message **"Timeout while loading CoCalc."** when you try to connect to CoCalc, there are several things to try:

* Hold down the ``Shift``-key and click your browser's reload button to refresh the CoCalc tab.
  Sometimes this simple action resolves the problem.
* Close your browser and open it again. Maybe even restart your computer!
* You might be using an old, unsupported browser.
  Check for updates available to the browser you are using, or switch to the latest version of a different browser.
* If you are on a very slow network, loading may succeed, but take more than 60 seconds.
  Try waiting. Loading may succeed after the timeout warning is displayed.

If this doesn't help, try additional diagnostic steps mentioned above.
