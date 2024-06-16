Why CoCalc?
===========

What a great question! You are probably the only one who can answer it correctly for your use case, but if you are new to CoCalc and considering adopting it for your own workflow or for your organization, we would like to help you.

To compare individual features with some of our competitors, take a look at https://cocalc.com/features/compare

If you are wondering about some specific requirements, reach out to us at help@sagemath.com and perhaps schedule a video chat.

We assume that you are aware of advantages (and some disadvantages) of working in the cloud rather than your own laptop, but there are quite a few cloud options out there. So, what makes CoCalc different from them?


Open World Approach
-------------------

CoCalc strives to give you as much flexibility as possible. Instead of deciding what you are allowed to do, we only put in place necessary security limits and, of course, have to deal with technical ones. Moreover, we try to push even those limits! You can't be root in :doc:`regular CoCalc projects <project>`, but you can :ref:`request installation <install-request>` of any necessary packages and you can :ref:`install anything as a regular user <python-pkg-install-user>`. On :doc:`compute servers <compute_server>` you are able to do anything on the underlying virtual machines, including creation of nested virtual machines! There are UI libraries that are not supported by our Jupyter notebook implementation, but we do try to improve it and you can run a standard :doc:`JupyterLab or VS Code <servers>` instance with a click of a button!

We want to facilitate access to open source software. This should not come as a surprise, given that our founder and CEO William Stein is also the founder of `SageMath <https://www.sagemath.org/>`_ whose mission is to be a viable open source alternative to proprietary math software. Some other people in the company were early developers of SageMath as well. While Python and Jupyter may be particularly famous, we have extensive support for R, Julia, LaTeX, C++, VS Code, and many other projects, languages, packages, and environments. We try to reduce "the setup time" as much as possible for our users, ideally - to zero! Most of our competitors have a narrower focus and even if they do include a large software collection, such as Colab (which you :ref:`can run <colab_example>` on CoCalc's compute servers), it may be tricky to expand it with packages that you need.

CoCalc's flexibility sometimes may create a feeling of a more complicated/overloaded interface. If your goal is to have a single feature, say Linux terminals, and nothing else, then perhaps there are easier to learn alternatives for your use case. However, if your needs may grow over time, you may find more and more ways to make use of CoCalc. We are also trying to separate "essential" elements and configuration options from "advanced" ones, to keep it simple yet powerful.


No Vendor Lock-In
-----------------

While most of our `source code <https://github.com/sagemathinc/cocalc>`_ and configuration files are public, we put restrictions on running your own instance without :doc:`purchasing a license <cocalc-cloud>`. We do have our own implementation of the Jupyter notebook interface and :doc:`Sage Worksheet format <sagews>` is specific to our platform. Yet you remain in full control of your data and code, CoCalc acts more like an operating system that allows you to run your code to process your data. Sage Worksheets can be converted to Jupyter notebooks. "Our" Jupyter notebooks are standard ``.ipynb`` files that you can download and use on your own machine or on another cloud provider, should you decide down the road that CoCalc no longer serves your needs.


Full Control of the Software Stack
----------------------------------

Core functionality of CoCalc, including our implementation of the Jupyter notebook interface, real-time collaboration, :doc:`AI integration <ai>`, :doc:`TimeTravel <time-travel>`, and :doc:`course management <teaching-instructors>`, is developed by `CoCalc team <https://cocalc.com/about/team>`_. As a consequence, we support the product that we know very well and we can quickly fix reported bugs as well as develop requested features for it (especially if you have funds available to facilitate such development). CoCalc does not have an extensive library of plugins and extensions of varied quality and support; instead all the features are included and maintained from the start.


On Premises Option
------------------

Using our fully hosted version greatly reduced administration burden for your organization, but there are situations where you may prefer to run your own cluster - maybe because of privacy requirements, maybe because you already have hardware resources and dedicated IT professionals. :doc:`CoCalc Cloud <cocalc-cloud>` can be deployed on your own resources or on cloud providers such as GCP, AWS, or Aliyun. CoCalc's AI integration can be easily tuned to use your own AI servers as well.


Responsive Support Team
-----------------------

In most cases we do not provide support SLAs (contact us if you are interested in such an option), but historically our response time was within a few hours - our team is geographically distributed, so urgent issues are dealt with regardless of your time zone. Due to service monitoring, many problems on the instances that we host are likely to be fixed even before you notice and report them. As your needs grow, we are with you along the way to provide extended enterprise support and custom feature implementation.


Next Steps
----------

`Create an account <https://cocalc.com/auth/sign-up>`_, give CoCalc a spin, and get in touch with your questions and comments - we would love to connect!
