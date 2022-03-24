.. index::
    Billing
    Upgrades
    Pricing
    Quotas
    FAQ; Billing
    FAQ; Subscription


.. _upgrades-faq:

===========================
Billing/Upgrades FAQ
===========================

This page answers questions related to upgrading projects and billing.

To learn more about licenses, see :doc:`licenses`.

Questions about projects are covered in :doc:`project-faq`.

.. contents::
   :local:
   :depth: 2


General
===========================


What is the difference between **free and paid service**?
----------------------------------------------------------

Learn more about :doc:`Trial Projects <trial>`.

With licensed projects and other paid plans, the main differences are:

* increased resource quotas
* better quality of hosting
* prioritized support.

We encourage you to make an account and explore our product for free.
Other than lack of internet access for free projects, there is no difference in functionality between the free and for-pay versions of
CoCalc. Everything is private by default for free users. You can
make as many projects as you want. You can start teaching a course
in CoCalc for free, then add a license later so that your students
have a **much** better quality experience (for a small fraction of the cost of
their textbook).

.. _invoice:
.. index::
    Billing; Invoice
    Invoice

How do I get an **invoice** with specific information?
------------------------------------------------------------

After purchasing, please email us at help@cocalc.com, reference what you bought,
and tell us the payer's name, contact information and any other specific instructions.
We will then respond with a custom invoice for your purchase
that satisfies your unique requirements.


.. index::
    PayPal
    Wire transfer

Can I pay via wire transfer or PayPal?
----------------------------------------

For purchases **above $100** we support PayPal or wire transfers.
Please contact help@cocalc.com with all relevant details about your intended purchase.



.. index:: Member Hosting;subscriptions

**The free servers really are massively overloaded, so it is well worth it to upgrade to member hosting, enable internet access, etc.**

**In case you're teaching a course and bought a license to manage that course**: please read :ref:`install-course-license`.


Quota upgrades
===========================

.. index::
    Quotas; Member hosting

.. _member-hosting:

What is **"member hosting"**?
---------------------------------------------


There are two types of projects: "trial (free) projects" and "member projects".
:doc:`Trial projects <trial>` run on heavily loaded computers
sharing the same node with many other projects and system tasks.
These nodes might also shutdown at any time,
causing your currently running project to interrupt your work and restart.

Member-hosted projects are moved to less loaded machines,
which are reserved only for paying customers and aren't restarted on a daily basis.
The cluster scales up dynamically to accommodate for a varying number of member-projects.

Working in member-hosted projects feels much smoother because commands execute
more quickly with lower latency,
and CPU, memory and I/O heavy operations run more quickly.


.. index::
    Quotas; Network access

.. _network-access:

What exactly is the **"network access"** quota?
------------------------------------------------

(This was formerly called the **Internet access** quota.)

Despite the fact that you are accessing CoCalc through the internet,
you are actually working in a highly restricted environment.
Processes running *inside* a free project are not allowed to directly
access the internet.  (We do not allow such access for free users, since when we did,
malicious users launched attacks on other computers from CoCalc.)
Enable internet access by adding the "internet access" quota.


.. _idle-timeout-quota:
.. index::
    Quotas; Idle timeout
    Idle Timeout; quota

What exactly is the **"idle timeout"** quota?
-------------------------------------------------


By default, free projects stop running after about 30 minutes of idle time.
This makes doing an overnight research computation –
e.g., searching for special prime numbers – impossible.

There is an advanced license option to prevent idle timeouts completely: see :ref:`licenses-always-running`.
Processes might still stop if they use too much memory, crash due to an exception, or if the server they are running on is rebooted.

.. note::

    Projects do not stop if you are continuously using them,
    and there are no daily or monthly caps on how much you may use a CoCalc project, even a free one.

See also: :ref:`Software development/idle timeout <idle-timeout>`.

.. _cpu-shares:
.. index::
    Quotas; CPU

What are **"CPU shares"** and **"CPU cores"**?
-----------------------------------------------------


All projects on a single server share the underlying resources.
These quotas determine how CPU resources are shared between projects.
Increasing them increases the priority of a project compared to others on the same host computer.
In particular, "shares" determines the amount of relative CPU time you get.

