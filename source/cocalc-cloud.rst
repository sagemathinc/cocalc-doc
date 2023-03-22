.. index:: CoCalc Cloud
.. index:: On-Premises: CoCalc Cloud

=====================
CoCalc Cloud
=====================

.. contents::
   :local:
   :depth: 1

#################################
Introduction
#################################

**CoCalc Cloud** runs on a Kubernetes Cluster. The underlying services and their architecture are identical to those in online cocalc.com, with comparable performance, scalability, and reliability to the online site.

This page provides a summary of CoCalc Cloud features. For detailed information, see `CoCalc Cloud documentation <https://doc-cloud.cocalc.com/>`_.

Our blog article `CoCalc On-Premise <https://about.cocalc.com/2022/11/18/cocalc-on-premise/>`_ has introductory information about CoCalc Cloud.

Here's a link to CoCalc feature announcement and discussion of the updated project documentation: `CoCalc-Cloud on Kubernetes (e.g., cocalc.com) -- have you ever wondered how it works and what it is? <https://github.com/sagemathinc/cocalc/discussions/6558>`_.

*************
Features
*************

Jupyter Notebooks, a recent version of Sage, Python 3, R, Octave, and LaTeX. Editing code and text files, Linux terminal, compiling code, and virtual X11 desktop are also included.

Beyond the standard set of included software, it’s also possible to define and build customized software environments.

Support for single sign-on, in particular, includes SAML.

The networking is defined by standard NGINX ingress rules. Of course, it’s possible to run inside a VPN as well.

You can deploy this solution on your bare-metal cluster or managed Kubernetes clusters, including Amazon’s AWS EKS and Google’s GCE GKE.

*************
Prerequisites
*************

A Kubernetes cluster and some experience managing it. We will be happy to guide you through the setup and give you enough information to manage the service, react to issues, plan resource requirements, and know how to scale the various benefits to your expected usage.

Experience working with HELM charts.

A (sub)domain and TLS certificate (e.g., letsencrypt).

A standard PostgreSQL database.

Storage. A network file system such as NFS, supporting ReadWriteMany, is used to hold the data of all projects.

########################################
Purchasing CoCalc Cloud
########################################

See `CoCalc Cloud` at `CoCalc - On Premises Offerings <https://cocalc.com/pricing/onprem>`_ or email help@cocalc.com for licensing and support.


