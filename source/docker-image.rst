.. index:: Docker image
.. index:: Cocalc; Docker image

=====================
CoCalc Docker Image
=====================


.. contents::
   :local:
   :depth: 1

##############################
About the CoCalc Docker Image
##############################

Not only does CoCalc let you use all open source math software in your browser, but `CoCalc itself is open source <https://github.com/sagemathinc/cocalc>`_. This means you can run CoCalc on your own laptop or server.

The CoCalc Docker image lets you:

* locally run:
   * Sage worksheets
   * Jupyter notebooks with R, Sage, and Python 2 & 3 kernels
   * Julia programs

* edit LaTeX documents and markdown locally

* learn about how CoCalc works

Note that files edited with the Docker image are fully compatible with online CoCalc. You can upload files from your Docker image to your cocalc.com account and work on them there. Files from cocalc.com will run in the Docker image as well, but you will need to ensure that any required packages and libraries are also installed locally.

##############################
Limitations
##############################

#. Unlike the `cocalc.com <https://cocalc.com>`_ service, the Docker image doesn't isolate projects from each other. There are no resource limitations between different projects.

#. The Docker image has no provisions to scale horizontally. The Docker image may be useful if you have a small number of *trusted*, non-malicious users. In contrast, the online service `cocalc.com <https://cocalc.com>`_ uses a proprietary resource management system based on kubernetes that provides scalability, fault isolation, and resilience. Contact us at help@cocalc.com if you are interested in running CoCalc with kubernetes infrastructure.

#. The software stack behind the `cocalc.com <https://cocalc.com>`_ service is several hundred gigabytes of well-tested code and data. In comparison, the Docker image provides a small subset of that stack, including SageMath and LaTeX. You can extend it on your own, though, by either installing more into the container or by amending the Dockerfile.

#. SageMath, Inc. doesn't prioritize supporting the Docker image, which means that if you ask a question about it, or make a support request, we likely won't have time to answer. Please set your expectations accordingly (but see below for alternatives). On the other hand, if you are willing to fully compensate us for our time, then we can likely be very helpful!

#. The license is `AGPLv3`_. If you want to run CoCalc internally and cannot use AGPLv3 licensed code at your organization, contact us and we can sell you a version of the Docker image under a different license.

##############################
Questions
##############################

**I'm working on a collaborative project on cocalc.com and the scripts we're using will very likely exceed the allotted server time for my cocalc.com account. Can I run the Docker image of CoCalc on my own machine, but still enable access by my collaborators remotely?**

Yes, you definitely can! The CoCalc team does exactly this in some special cases (e.g., for Sage Days workshops).
Follow the directions here:
`sagemathinc/cocalc-docker <https://github.com/sagemathinc/cocalc-docker>`_.
Be sure to make your account an admin and set an "account creation token" so that only you and your collab can make accounts on the server.

**What support is available for the CoCalc Docker image?**

If you want professional-level support for running the server from us, send email to `help@cocalc.com <mailto:help@cocalc.com">`_. There are also mailing lists for general community discussion :ref:`described below <cocalc-docker-mailing-lists>`.

**Is Anaconda available in the CoCalc Docker image?**

The Docker image does NOT currently include Anaconda at all. If you need it, you'll have to install it yourself.  This isn't difficult, since the Docker image is running Ubuntu 18.04, and it is easy to install Anaconda into Ubuntu.

**What about compatibility with the operating system on my local computer?**

The CoCalc Docker image is completely isolated from your main Linux system. It can't mess up anything installed there! It uses the exact same Linux kernel, but otherwise has minimal overhead (it is very much not a virtual machine).  Docker is designed to not touch or break anything related to your OS.

**How much disk space is needed for the CoCalc Docker image?**

About 12 GB. Remember, the Docker image includes a full LaTeX and Sage install, which is pretty big.

##############################
Getting Started
##############################

Detailed instructions to get the image up and running are at `the github repo for sagemathinc/cocalc-docker <https://github.com/sagemathinc/cocalc-docker>`_.

#############################################
Additional Licensing and Support Available
#############################################

CoCalc code is licensed under `AGPLv3`_. If you would instead like a business-friendly MIT license instead, please contact `help@cocalc.com <mailto:help@cocalc.com">`_, and we will sell you a 1-year license for $999.  This also includes some support, though with no guarantees (that costs more). We **do** have several happy paying customers as of Sept 2019.

.. _cocalc-docker-mailing-lists:


#############################################
Online Mailing Lists and Open Issues
#############################################

For additional news and support, we recommend joining the following lists:

* `CoCalc Docker mailing list <https://groups.google.com/a/sagemath.com/group/cocalc-docker/subscribe>`_ for news and updates.

* `CoCalc mailing list <https://groups.google.com/forum/?fromgroups#!forum/cocalc>`_ for general community support.

* Here is a list of `open docker-related CoCalc issues <https://github.com/sagemathinc/cocalc/issues?q=is%3Aopen+is%3Aissue+label%3AA-docker>`_.

##############################
Security Status
##############################

The CoCalc Docker image is **not blatantly insecure** from outside attack: the database has a long random password, user accounts are separate, encrypted SSL communication is used by default, etc. That said, please observe the following:

.. warning::

  A determined user with an account can easily access or change files of other users in the same container! Use this for personal use, behind a firewall, or with an account creation token, so that only other people you trust create accounts.  Don't make one of these publicly available with important data in it and no account creation token! See `issue 2031 <https://github.com/sagemathinc/cocalc/issues/2031>`_.  Basically, use the CoCalc Docker image only with people you trust.

##################################
Updates to the CoCalc Docker Image
##################################

The CoCalc Docker image is updated approximately weekly. Weekly updates incorporate all features and bug fixes that have been merged into the `CoCalc GitHub code repository <https://github.com/sagemathinc/cocalc>`_ master branch at the time of the build.

Other updates, such as new versions of Sagemath, Julia, and other additional software, happen less frequently but will be announced on the CoCalc Docker mailing list and listed below:

.. index:: Docker image; updates

.. toctree::
   :maxdepth: 1

   docker/image-updates-2019

.. _AGPLv3: https://opensource.org/licenses/AGPL-3.0
