.. index::
    Billing
    Upgrades
    Pricing
    Quotas
    FAQ; Billing
    FAQ; License Key
    FAQ; Subscription


.. _upgrades-faq:

===========================
Billing/Upgrades FAQ
===========================

This page answers questions related to `purchasing upgrades <https://cocalc.com/policies/pricing.html>`_,
:doc:`upgrading projects or courses <upgrade-guide>`, subscriptions, license keys, and billing.

Questions about projects are covered in :doc:`project-faq`.


.. contents::
   :local:
   :depth: 2


General
===========================

Subscriptions & Upgrades 101
-------------------------------

Purchasing a personal subscription or course package awards to with certain quota upgrades
for the indicated period of time.

Use these upgrades to improve hosting quality,
enable internet access from within a project
or increase quotas for CPU and RAM in order to work on larger problems
and do more computations simultaneously.
On top of that, your `support questions <mailto:help@cocalc.com>`_ are prioritized.

You can upgrade the quotas up to the total amount given by your subscription(s)
and the upper limits per project.

Project collaborators can collectively contribute to the same project,
in order to increase the quotas of their common project –
these contributions add together to benefit all project collaborators equally.

You can *remove* your contributions to any project *at any time*.

You may also purchase any plans *more than once*,
in order to increase the total amount of upgrades available to you.

Right after the purchase the subscription becomes active.
It *automatically renews* after the indicated period.

You can *cancel* a subscription at any time and
it will continue to run until the end of the current period and *not renew*.


What is the difference between **free and paid plans**?
----------------------------------------------------------

Learn more about :doc:`Trial Projects <trial>`.

The main differences are increased quotas and the quality of hosting; we also
prioritize supporting paying users.
We very strongly encourage you to make an account and explore our product for free!
There is no difference in functionality between the free and for-pay versions of
CoCalc; everything is still private by default for free users, and you can
make as many projects as you want.  You can even fully start teaching a course
in CoCalc completely for free, then upgrade at any point later so that your students
have a **much** better quality experience (for a small fraction of the cost of
their textbook).

.. _invoice:
.. index::
    Billing; Invoice
    Invoice

How do I get an **invoice** with a specific information?
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

For purchases **above $50** we support PayPal or wire transfers.
In particular that might be a year-long personal subscription or a larger course plan.
Please contact help@cocalc.com with all relevant details about your intended purchase.



.. index:: Subscription Does Not Work
.. _sub_not_work:

Subscription does not work
---------------------------------------

After you buy a subscription, the first thing you need to do is go to settings in your project and :ref:`apply upgrades <project-upgrades>` from your subscription quotas to your project(s). Do this for each project that you would like to be upgraded. Exception: if you are managing a course with CoCalc, you :ref:`upgrade student projects <inst-pays>` within the .course file, and not in project settings.

At any time, you can visit https://cocalc.com/settings/upgrades to see exactly how all of your upgrades are allocated across your projects.

.. index:: Member Hosting;subscriptions

**The free servers really are massively overloaded, so it is well worth it to upgrade to member hosting, enable internet access, etc.**

If you used up your upgrades, e.g., you are often using 3 or 4 projects, then you can always buy multiple subscription and you'll get more upgrades as a result.

**In case you're teaching a course and bought a course package**: please read :ref:`inst-pays`.

If this doesn't completely answer your question, please don't hesitate to create a support request or email help@cocalc.com.




Quota upgrades
===========================

.. _member_hosting:
.. index::
    Quotas; Member hosting

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



.. _network-access:
.. index::
    Quotas; Network access


What exactly is the **"internet access"** quota?
------------------------------------------------

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

With an increased idle timeout, projects are allowed to run longer unattended.
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
Increasing them increases the priority of a project compared to others on the same host computer.<br/>
In particular, "shares" determines the amount of relative CPU time you get.


.. index::
    Course packages

Course packages
===========================

.. include:: teaching-vfaq.inc



Am I **required to pay** for conducting a course?
-----------------------------------------------------------------

**No.** You can evaluate all course related functionalities under a free plan.

Please `contact us <help@cocalc.com>`_ for a limited trial to test the upgrade functionality.


What happens with the **files of my students** after the course finishes?
------------------------------------------------------------------------------

Students will **continue to have access** to their files after the course,
regardless of running the course under a paid plan or for free.
Their projects remain accessible,
they can (optionally) upgrade their projects with their own subscriptions,
and they can also download all files to their local computer.


Do you offer **academic discounts**?
---------------------------------------

Our course subscriptions are for academic use
and are already significantly discounted from the standard plans.
Please compare our monthly plans running for 4 months with a 4 month course plan.


**Which upgrade scheme** do I need for student courses?
-------------------------------------------------------

Any upgrades you purchase and distribute to student projects are added on top of the "free quotas".

For the **smallest course plan**, this means your student projects get better hosting and internet access.
This should be sufficient for running one or two Notebooks with moderate resource requirements.

If you work with more involved notebooks or worksheets, process data, or run CPU-intensive tasks,
we advice to order a plan which includes upgrades for CPU and memory.

.. note::

    We do strongly suggest all classes upgrade the projects to "members-only" hosting,
    since this provides a better experience and higher availability.





.. index:: Personal Plans
.. _personal-plans:

Personal Plans
===========================

CoCalc personal plans are a good fit for individuals and small teams.
Unlike the course subscriptions, they are automatically renewing.
They can be canceled at any time through the Account / Subscriptions and Course Packages tab.

There are three resource levels available. Upgrades provided with each plan are listed below. For the latest information and further detail, see the CoCalc `pricing page <https://cocalc.com/policies/pricing.html>`_.

For additional resources, you can purchase multiple plans and have them run concurrently, thus "stacking" available upgrades to reach the desired level.

.. index:: Personal Plans; standard
.. _personal-standard:

1. Standard Plan
-----------------

* 4 projects Member Hosting
* 8 projects Internet Access
* 1 day Idle Timeout
* 8 GB Disk Space
* 4 GB Shared RAM

.. index:: Personal Plans; premium
.. _personal-premium:

2. Premium Plan
----------------

* 16 projects Member Hosting
* 32 projects Internet Access
* 8 days Idle Timeout
* 40 GB Disk Space
* 24 GB Shared RAM
* 2 GB Dedicated RAM
* 2 cores Shared CPU
* 1 core Dedicated CPU

.. index:: Personal Plans; professional
.. _personal-professional:

3. Professional Plan
--------------------

* 40 projects Member Hosting
* 80 projects Internet Access
* 20 days Idle Timeout
* 100 GB Disk Space
* 60 GB Shared RAM
* 4 GB Dedicated RAM
* 4 cores Shared CPU
* 2 cores Dedicated CPU

Which plan offers "private" file storage?
----------------------------------------------

All our plans (free and paid) host your files privately by default.
You can :ref:`share a file with collaborators <add-collaborators>`
or :doc:`publish it online <share>`, though.

For more information about storing data about you and your files on CoCalc,
please read our `Privacy Policy <https://cocalc.com/policies/privacy.html>`_ and
`Copyright Notice <https://cocalc.com/policies/copyright.html>`_.

