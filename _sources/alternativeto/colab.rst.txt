Alternative to Colab
====================

If you need to work with Python in Jupyter notebooks, CoCalc may be a great alternative to Colab!

Let's take a closer look at how these services compare to each other and what will you gain (and lose) by going with CoCalc.

According to https://research.google.com/colaboratory/faq.html 

.. epigraph ::

    Colab is a hosted Jupyter Notebook service that requires no setup to use and provides free of charge access to computing resources, including GPUs and TPUs. Colab is especially well suited to machine learning, data science, and education.

.. important::

    For the discussion below, we **focus on hosted Python Jupyter Notebooks** only. CoCalc's scope is much bigger, but if you need to work with LaTeX documents, or R, or use VS Code, then Colab cannot be considered as a viable alternative at all.

Free Tier
---------

For occasional light usage Colab is completely free, including GPU access.

While CoCalc's :doc:`/trial` are free, their purpose is to give you a sense of how CoCalc works, not to allow subsidized free usage. Since our size is *much* smaller than Google, we can't afford it.

UI Simplicity
-------------

Colab has a noticeably simpler user interface. This is a consequence of CoCalc being much more flexible and feature-rich, supporting way more than just Python notebooks. If you don't need any of that, Colab may feel better.


Environment Flexibility
-----------------------

Both platforms have many popular libraries preinstalled and allow you to install your own ones as well.

On top of that, CoCalc offers a choice between multiple :doc:`Software Environments </software>` and Jupyter kernels, including previous versions to address compatibility problems. Packages that you install yourself persist between sessions and you can ask us to extend our default environment to include packages needed for your application.

CoCalc gives you a choice to work with the same notebook using our implementation of :doc:`/jupyter`, or :ref:`JupyterLab <jupyterlab-server>` itself, or :doc:`/vscode`.

Real File System
----------------

Integration of Colab with Google Drive is convenient, but it comes with limitations that you may hit when processing large amounts of data in terms of total size or number of files. CoCalc provides you with a dedicated persistent file system for every project and allows mounting external storage resources as well.

Compute Scalability
-------------------

Both platforms allow you to pay for more powerful compute resources if the default is not sufficient for your needs. However, Colab is offering a rather limiting choice. In contrast, CoCalc lets you start :doc:`any machine </compute_server>` supported by Google Cloud Platform or Hyperstack, with hundreds of CPUs, terabytes of RAM, and multiple GPUs. We also support using your own hardware and plan to expand our choice of cloud providers. To get comparable flexibility with Colab you have to be on an enterprise contract.

Price Transparency
------------------

The entry price for the paid tier is similar and is based on a monthly license fee with possibility to pay more for extra resources. There is a difference in transparency, however. CoCalc allows you to view a detailed list of your charges at any time and your pay-as-you-go balance does not expire from month to month. You can even use it to pay for the base license in the future. In contrast, Colab operates with "compute units" without a clear conversion into VM pricing and these units expire after 3 months.

Collaboration
-------------

Despite its name, the current version of Colab has no real time collaboration, although you can share your notebook with other people in the same way as any other file in your Google Drive. CoCalc does support full real time collaboration:

- multiple users may edit the same file at the same time (and see each other's cursors, similar to Google Docs)
- these users see the same state of the notebook including its output and all interactive widgets
- they also share the same current RAM (and disk) state
- it is also possible to :ref:`chat on a side <side-chat>` of the notebook in real time or asynchronously, with notifications


AI Assistant
------------

Both platforms allow you to use AI to generate and troubleshoot code. CoCalc supports multiple AI providers including Google.

Regardless of the model you pick in CoCalc, your data are processed by :doc:`/ai` only at your explicit request and are *NOT* used for any other purposes by either CoCalc or AI service providers. Colab, on the other hand, informs you that your prompts and generated outputs will be stored and used for AI training purposes.

CoCalc also gives you an option to disable AI integration either for your own account or for your students.

Course Management
-----------------

Instructors using Colab for courses typically rely on some external LMS to distribute files to students. They have to upload these to Colab and then download and submit either the notebook itself or its PDF rendering.

CoCalc has :doc:`extensive support </teaching-instructors>` for creating projects for students, distributing assignments, then collecting, grading, and returning them. You can optionally use :doc:`peer grading </teaching-peer-grading>` and automatic grading with :doc:`nbgrader </teaching-nbgrader>`.
But most importantly, you and your students (or workshop participants) can benefit from CoCalc collaboration. At any point in time you can check the current version of your student's work, either to assess the progress or to help resolve a problem.


Billing Flexibility
-------------------

Colab may be easy to use for a personal account, but we heard complaints about not accommodating teams and courses.

CoCalc supports quotes, purchase orders, and invoices for orders over $100. Payments can be done via credit cards, bank transfers, or checks. When using course management functionality, you can let your students pay for themselves or use your own funds. The latter case is applicable even to pay-as-you-go functionality: you can set and adjust spend limits for your students.


Support
-------

At CoCalc we are proud of the support that we provide to our users. It is easy to create a support ticket at any moment and most of them are answered within a few hours. If you need a video call to configure a course or set up compute servers, we are happy to do it as well.

On the other hand, we heard complaints about difficulties getting in touch with Colab support or having them actually solve users problems.


Much More
---------

We said we'll focus on Python Notebooks, but if you read up to here - we do offer much more! Probably you don't need all of it, but likely some pieces are useful and can enhance your work: :doc:`LaTeX documents </latex>`, :doc:`Linux terminals </terminal>`, :doc:`/markdown`, :doc:`/chat`, :doc:`/slides`, :doc:`/whiteboard`, etc.

If you handle sensitive data and want to keep complete control over it, or if you have existing hardware resources and want to take full advantage of it, we offer `CoCalc OnPrem <https://onprem.cocalc.com/>`_ with mostly the same functionality as our hosted platform. ("Removed" features are relevant only for large scale cloud deployments with millions of projects.)
