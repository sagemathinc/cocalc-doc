.. index:: ChatGPT

=====================
ChatGPT
=====================

ChatGPT can transform how you use CoCalc for learning, writing programs, and writing scientific documents.

Here are some areas where CoCalc's context-sensitive ChatGPT help can save you time and effort:

.. contents::
   :local:
   :depth: 2

You can read all CoCalc ChatGPT announcements to date and join the discussion at the links shown:

#. `ChatGPT integration via any chatroom in cocalc <https://github.com/sagemathinc/cocalc/discussions/6543>`_.

#. `Cocalc chatrooms now support reply message threads, and chatgpt now has "long memory" of the entire thread it was involved in <https://github.com/sagemathinc/cocalc/discussions/6567>`_.

#. `CoCalc Jupyter notebooks now have a new "Explain" button in Jupyter notebooks <https://github.com/sagemathinc/cocalc/discussions/6583>`_.

#. `New button to help you fix errors in Jupyter notebooks <https://github.com/sagemathinc/cocalc/discussions/6584>`_.

#. `ChatGPT integration with the Linux Terminal <https://github.com/sagemathinc/cocalc/discussions/6594>`_.

#. `Easily use the OpenAI ChatGPT API from your Jupyter notebooks in CoCalc <https://github.com/sagemathinc/cocalc/discussions/6600>`_.

####################################
Jupyter Notebooks
####################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Suggesting Code
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Here is an example of a code suggestion using ChatGPT with a python Jupyter notebook.

Sample request: *plot time series data using a pandas dataframe*

#. Ask the question in the ChatGPT box above the :doc:`Jupyter notebook <jupyter>`.

   .. figure:: img/ch-ask-pandas-question.png
      :width: 90%
      :align: center
      :alt: copy chat response

      asking for a code suggestion


#. Copy the code from the response in side chat.

   .. figure:: img/ch-copy-python-code.png
      :width: 90%
      :align: center
      :alt: copy chat response

      copying suggested code

#. Paste the code into a notebook code cell.
#. Inspect the code for correctness.
#. Run the code.


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Fixing Errors
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

ChatGPT can help you understand and fix execution errors in a :doc:`Jupyter notebook <jupyter>` code cell.

   .. figure:: img/ch-fix-jup-err.png
      :width: 90%
      :align: center
      :alt: ask how to fix an error

      asking how to fix an error


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Explaining Code
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

ChatGPT can explain what is going on in a :doc:`Jupyter notebook <jupyter>` code cell.

   .. figure:: img/ch-explain-code-jup.png
      :width: 90%
      :align: center
      :alt: explain a code cell

      asking to explain contents of a code cell

####################################
Editing Python, R, and Other Files
####################################

For programming language file types such as .py, .R, pl, and .c, the CoCalc :doc:`frame-editor` includes ChatGPT buttons in the top menu.

#. Open a .py file in CoCalc.
#. Notice there's a ChatGPT button in the top menu bar.

   .. figure:: img/ch-top-of-frame-ed.png
      :width: 60%
      :align: center
      :alt: chat help editing a python file

      ChatGPT button displayed above .py file



####################################
Linux Terminal
####################################

:doc:`terminal` windows include a ChatGPT button at the top.

   .. figure:: img/ch-linux-term.png
      :width: 60%
      :align: center
      :alt: chat button in a terminal window

      ChatGPT button displayed above terminal window


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Suggest Code for Shell Scripts
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can get help with basic shell scripting as well as with advanced CoCalc commands. Sample requests:

* *replace 'x' by 'y' in all files*
* *how can I use pari/gp to compute the number of primes up to 2023*


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Help Writing SQL Queries
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Sample request:

*I am using psql to query a table with a column called "time". I would like to make a table showing the number of entries in my table for each of the last 7 days.*

####################################
Scientific Documents
####################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Typeset Scientific Content with LaTeX
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can describe a formula in English and have ChatGPT turn it into a latex formula. Sample requests:

* *Use latex to typeset the following formula: the integral from 0 to infinity of sin(x^2)*

* *Use latex to typeset the following formula: (a + b + c) / alpha*

.. figure:: img/ch-4.png
   :width: 50%
   :align: center
   :alt: custom help latex formulas

   ChatGPT help with latex formulas


####################################
ChatGPT on Sign-in and Feature Pages
####################################

You can ask a question at the start of your CoCalc session. ChatGPT help boxes are at the top of the sign-in page and all feature headings (landing pages).

.. figure:: img/ch-2.png
   :width: 90%
   :align: center
   :alt: custom help at sign-in page

   ChatGPT help near top of sign-in page

ChatGPT is available near the top of the CoCalc features main page and each of the individual feature pages.

.. figure:: img/ch-cocalc-features.png
   :width: 90%
   :align: center
   :alt: help at features page

   ChatGPT help near top of features page


####################################
ChatGPT in Chat Rooms and Side Chat
####################################

In a :doc:`chat room <chat>` or in the :ref:`side chat <side-chat>` next to an open file, you can do an :ref:`@-mention <chat-at-mentions>` of ChatGPT and enter your question there.

.. figure:: img/ch-5.png
   :width: 70%
   :align: center
   :alt: @-mention help with latex

   @-mention help with latex

########################################
CoCalc Admins: add ChatGPT to your site
########################################

CoCalc-Docker:
`ChatGPT integration in latest image <https://github.com/sagemathinc/cocalc-docker/discussions/183>`_.


