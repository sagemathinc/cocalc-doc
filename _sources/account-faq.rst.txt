===============================
Account FAQ, Tips & Tricks
===============================




.. index:: Multiple Accounts
.. _multiple-accounts:

Multiple Accounts
=============================

**If you have more than one CoCalc account, sometimes you might have problems when logged into both accounts simultaneously.**

The key fact is that you *should not* attempt to use two different accounts on CoCalc simultaneously, from the same browser.
The cookies will interfere with each other.
However, both Firefox and Chrome allow for two or more **identities** / **profiles** at once,
where each identity has a distinct set (cookie jar?) of cookies.
That approach works very well with CoCalc.


What Can go Wrong?
--------------------------

One phenomenon is that you might be able to access some files from one account,
but not other files from that account, even from the same browser tab!

For example, you might see the error message like "Opening ``'filename'`` publicly not yet supported" if you are signed into two user accounts simultaneously.



An Easy Fix when Things Get Weird
---------------------------------------------------------------

Make sure you close all cocalc.com windows in a given browser,
log out of cocalc.com entirely (Account Settings → Sign out…),
and then log in again with the account that you want to use.



For Beginners, who wish to use more than one CoCalc account
---------------------------------------------------------------

There are some easy ways to do this. For example, you might use one account in one browser, like FireFox, and the other account in a different browser, perhaps Google Chrome.

Or within Firefox alone, you can have one account in a normal window.
Then open a "New Private Window" under the "File" menu and use the other account in that window.
The browser will keep those separate.

Similarly, within Google Chrome alone, you can have one account in a normal window.
Then open a "New Incognito Window" under the "File" menu
and use the other account in that window.
Again, the browser will keep those separate.

If you have both Firefox and Google Chrome on the same machine,
you can use four accounts simultaneously this way!



For Advanced Users, who wish to use more than one CoCalc account
------------------------------------------------------------------

**Google Chrome** refers to adding multiple identities as "Add a person or profile".
Here is a link to some `Google Chrome Support Pages <https://support.google.com/chrome/answer/2364824?hl=en>`_ that discuss this.

**Firefox** users can manage multiple identities via Contextual Identity Containers.
Here is a `the Mozilla Wiki page about Containers <https://wiki.mozilla.org/Security/Contextual_Identity_Project/Containers>`_.





.. _merging-accounts:

Merging Accounts
=======================

Right now, we do not have a way to merge accounts and associated projects. However, adding your primary account as a collaborator for each project of the deprecated account is sufficient to have access to all projects by the primary account. Use the exact email address in the search box for collaborators to be sure to select the correct one. Then, you can access everything from your primary account, also distribute quota upgrades, etc.

* `Ticket for merging accounts <https://github.com/sagemathinc/cocalc/issues/2880>`_

