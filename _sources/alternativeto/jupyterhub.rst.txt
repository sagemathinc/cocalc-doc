Alternative to JupyterHub
=========================

If your primary goal is to have a centralized solution for working with Jupyter Notebooks, CoCalc may be a great alternative to hosting your own instance of JupyterHub!

Let's take a closer look at how these services compare to each other and what will you gain (and lose) by going with CoCalc.


Key Features of JupyterHub
--------------------------
These are copied from https://jupyter.org/hub

- **Customizable** - JupyterHub can be used to serve a variety of environments. It supports dozens of kernels with the Jupyter server, and can be used to serve a variety of user interfaces including the Jupyter Notebook, JupyterLab, RStudio, nteract, and more.

- **Flexible** - JupyterHub can be configured with authentication in order to provide access to a subset of users. Authentication is pluggable, supporting a number of authentication protocols (such as OAuth and GitHub).

- **Scalable** - JupyterHub is container-friendly, and can be deployed with modern-day container technology. It also runs on Kubernetes, and can run with up to tens of thousands of users.

- **Portable** - JupyterHub is entirely open-source and designed to be run on a variety of infrastructure. This includes commercial cloud providers, virtual machines, or even your own laptop hardware.


Portability
-----------

Note that JupyterHub is "just a software project", i.e. in order to make use of it and benefit from the above features, you do need to own appropriate hardware or setup a suitable environment with some cloud provider. You also need to have sufficient technical expertise and time to do this or hire someone else to do it for you. Exact time and money requirements depend a lot on the situation, but tend to be quite noticeable. There are companies that are happy to sell you their JupyterHub support services.

CoCalc also can be deployed in a variety of ways as a standalone instance just for you or your organization. The main difference with JupyterHub is that CoCalc is NOT a fully open-source project, we use `Microsoft Reference Source License <https://github.com/sagemathinc/cocalc/blob/master/LICENSE.md>`_. You can look at the `source code <https://github.com/sagemathinc/cocalc>`_, but you cannot run an instance yourself without getting permission from us. Third party companies also cannot provide support without having a suitable arrangement with us. We are happy to discuss your needs if an :doc:`OnPrem </on-premises>` installation suits your case. We already have a number of customers using this setup!

In many cases, however, it makes sense to directly use our hosted service - a fully configured and actively managed cluster which you can use, easily increasing or decreasing the computational power available to you, including :doc:`vast CPU and GPU resources </compute_server>`.

Flexibility
-----------

Similar to JupyterHub, CoCalc can work with multiple :doc:`Jupyter kernels </howto/jupyter-kernel-selection>`. Many of them are preconfigured and you can add more, both in the hosted and OnPrem installations. CoCalc allows you to easily run :doc:`JupyterLab </servers>`, :doc:`/vscode`, or R IDE on any of the servers in your project, so you can use the same familiar interfaces, if you choose so. However, CoCalc also gives you its own interface to work with Jupyter notebooks, and it does have a number of advantages:

- **Server-side notebook state** - When you close your browser (or it crashes, or your laptop goes to sleep) new output is accumulated and saved, waiting for you to resume your work.
- **IPyWidgets support** - Our support is the best and most complete one that we are aware off. Collaborators see the same state of all widgets, since it is synchronized with the server.
- **Full real-time collaboration** - Edit the same file simultaneously with your collaborators, see their cursors, use the side chat, and video chat.
- **AI Assistant**  - Choose your favourite LLM to help you generate, fix, and improve code, translate between programming languages, and :doc:`more </ai>`.
- **TimeTravel** - Our unique :doc:`automatic version control </time-travel>` and backup system complements ``git``.

Of course, apart from :doc:`/jupyter`, CoCalc supports many other document types, including :doc:`LaTeX documents </latex>`, :doc:`Linux terminals </terminal>`, :doc:`/markdown`, :doc:`/chat`, :doc:`Courses </teaching-instructors>`, etc.

CoCalc does not have plugins that extend its functionality, instead everything is included right away. In this sense you may consider JupyterHub to be more flexible/tunable, but it conveniently brings us to the next point.


Reliability
-----------

CoCalc functionality is continuously tested as a single unit in our production environment. Occasionally, there are bugs and regressions which we try to address as soon as possible. You may not even become aware of the problem because of our `continuous monitoring <https://status.cocalc.com/>`_ of the service and other users reporting problems as well.

With JupyterHub, on the other hand, our experience has shown that a user may attempt to install an innocuously looking plugin (``jupyterlab-git`` to be specific) to discover that not only it does not work, but the whole environment becomes unusable and requires admin intervention to be fixed.
