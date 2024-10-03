.. index:: Projects

.. _projects-tour:

Projects
========

To get a short introduction to the `CoCalc Projects page <https://cocalc.com/projects>`_, click the blue **Tour** button in its top right corner. This is one of several :doc:`tours` of features in CoCalc.

You can think of a CoCalc's **Project** as a virtual computer. Its computational resources are determined by a :doc:`license <licenses>` applied to the project. You and your project collaborators have equal access to all the files in it, such as
:doc:`Jupyter Notebooks <jupyter>`,
:doc:`Linux Terminals <terminal>`,
:doc:`LaTeX documents <latex>`,
and many others. You can edit (or just observe) these files simultaneously and discuss your work in various ways using :doc:`chats <chat>`.

You can create multiple projects to work with different groups of collaborators or, well, to work on different projects. You can apply the same license to as many projects as you wish, but its run limit will determine how many of such virtual computers may be running *at the same time* with allocated resources. Depending on the nature of your work, you may find these resources insufficient. If this happens, you can consider :ref:`upgrading your license <manage-licenses>` or spinning up some arbitrarily powerful :doc:`compute_server`!

.. note::

    Under the hood, a project is a `Kubernetes pod <https://kubernetes.io/docs/concepts/workloads/pods/>`_ and all your files reside in the ``$HOME`` directory of a fictitious user or its subdirectory. All collaborators processes run as the same user, this is a consequence of real time collaboration. Different projects, however, are isolated from one another.

.. raw:: html

    <center><iframe
        width="640" height="360"
        src="https://www.youtube.com/embed/elru3WgRAVM?si=AIXIP_7AAcApxONc"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe></center>

.. toctree::
   :maxdepth: 2

   project-list
   project-files
   plus-new
   project-log
   project-settings
   upgrade-guide
   project-library
   project-init
   project-faq
