:orphan:

Alternative to JupyterHub
=========================

If your primary goal is to have a centralized solution for working with Jupyter Notebooks, CoCalc may be a great alternative to hosting your own instance of JupyterHub!

Let's take a closer look at how these services compare to each other and what will you gain (and lose) by going with CoCalc.


Key Features of JupyterHub
--------------------------
These are copied from https://jupyter.org/hub

- **Customizable** - JupyterHub can be used to serve a variety of environments. It supports dozens of kernels with the Jupyter server, and can be used to serve a variety of user interfaces including the Jupyter Notebook, Jupyter Lab, RStudio, nteract, and more.

- **Flexible** - JupyterHub can be configured with authentication in order to provide access to a subset of users. Authentication is pluggable, supporting a number of authentication protocols (such as OAuth and GitHub).

- **Scalable** - JupyterHub is container-friendly, and can be deployed with modern-day container technology. It also runs on Kubernetes, and can run with up to tens of thousands of users.

- **Portable** - JupyterHub is entirely open-source and designed to be run on a variety of infrastructure. This includes commercial cloud providers, virtual machines, or even your own laptop hardware.


Portability
-----------

Note that JupyterHub is "just a software project", i.e. in order to make use of it and benefit from the above features, you do need to own appropriate hardware or setup a suitable environment with some cloud provider. You also need to have sufficient technical expertise and time to do this or hire someone else to do it for you. Exact time and money requirements depend a lot on the situation, but tend to be quite noticeable. There are companies that are happy to sell you their JupyterHub support services.

CoCalc also can be deployed in a variety of ways as a standalone instance just for you or your organization. The main difference with JupyterHub is that CoCalc is NOT a fully open-source project, we use Microsoft Reference Source License. You can look at the source code, but you cannot run an instance yourself without getting a permission from us. Third party companies also cannot provide support without having a suitable arrangement with us. We are, however, happy to discuss your needs if an OnPrem installation works well your case, we do have a number of such customers!

In many cases, however, it makes sense to directly use our hosted option - we already have a configured and actively managed cluster which you can use, easily increasing or decreasing the computational power available to you, including vast CPU and GPU resources.

Flexibility
-----------

Just as JupyterHub, CoCalc supports dozens of Jupyter kernels. Many of them are preconfigured and you can add more, both in the hosted and OnPrem installations. CoCalc allows you to easily run JupyterLab, VS Code, or R IDE on any of the servers in your project, so you can use the same familiar interfaces, if you choose so. However, CoCalc also gives you its own interface to work with Jupyter notebooks, and it does have a number of advantages:

- server-side notebook state - the output is preserved if you close your browser or switch to a different machine
- full real-time collaboration - simultaneous editing of the same file and chat
- the best and most complete support of IPyWidgets that we are aware off, including sharing widget state between collaborators
- AI Assistant to generate and fix code, transalate between programming languages, and more
- TimeTravel automatic version control and backup system to complement ``git``

Of course, apart from Jupyter notebooks CoCalc supports many other document types, including LaTeX documents, Linux terminals, Markdown, chats, courses, etc.

CoCalc does not have plugins that extend its functionality, rather everything available is included right away. In this sense you may consider JupyterHub to be more flexible/tunable, but it conveniently brings us to the next point.


Reliability
-----------

CoCalc functionality is continuously tested as a single unit in our production environment. Occasionally, there are bugs and regressions which we try to address as soon as possible. You may not even become aware of the problem because of our continuous monitoring of the service and other users reporting problems as well.

With JupyterHub, on the other hand, our experience has shown that a user may attempt to install an innocuously looking plugin to discover that not only it does not work, but the whole environment becomes unusable and requires admin intervention to be fixed. 