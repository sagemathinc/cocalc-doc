.. index::
    Billing
    Upgrades
    Pricing
    Quotas
    FAQ; Billing

===========================
Billing/Upgrades FAQ
===========================

This page answers questions related to `purchasing upgrades <https://cocalc.com/policies/pricing.html>`_,
:doc:`upgrading projects or courses <upgrade-guide>`, and billing.

Questions about projects are covered in :doc:`project-faq`.


.. contents::
   :local:
   :depth: 2


General
===========================

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
.. index:
    Billing; Invoice
    Invoice

How do I get an **invoice** with a specific information?
------------------------------------------------------------

After purchasing, please email us at help@cocalc.com, reference what you bought,
and tell us the payer's name, contact information and any other specific instructions.
We will then respond with a custom invoice for your purchase
that satisfies your unique requirements.


Can I pay via wire transfer or PayPal?
----------------------------------------

For purchases **above $50** we support PayPal or wire transfers.
In particular that might be a year-long personal subscription or a larger course plan.
Please contact help@cocalc.com with all relevant details about your intended purchase.


Quota upgrades
===========================

.. _member_hosting:
.. index:
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
.. index:
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
.. index:
    Idle timeout

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
.. index:
    Quotas; CPU Shares

What are **"CPU shares"** and **"CPU cores"**?
-----------------------------------------------------


All projects on a single server share the underlying resources.
These quotas determine how CPU resources are shared between projects.
Increasing them increases the priority of a project compared to others on the same host computer.<br/>
In particular, "shares" determines the amount of relative CPU time you get.


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


Personal plans
===========================

Which plan offers "private" file storage?
-----------------------------------------------

All our plans (free and paid) host your files privately by default.
You can :ref:`share a file with collaborators <add-collaborators>`
or :doc:`publish it online <share>`, though.

For more information about storing data about you and your files on CoCalc,
please read our `Privacy Policy <https://cocalc.com/policies/privacy.html>`_ and
`Copyright Notice <https://cocalc.com/policies/copyright.html>`_.

