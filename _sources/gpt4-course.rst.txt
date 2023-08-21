.. index:: GPT4 with Courses

======================
GPT4 with Courses
======================

.. contents::
   :local:
   :depth: 2

This article explains how payments work when GPT-4 capability is requested when using ChatGPT. This information is especially relevant, but not limited to, student projects in a CoCalc managed course. Learn about the differences in available GPT versions at :ref:`gpt-versions`.

Here's the CoCalc feature announcement and discussion: `Concerns about GPT-4 Fees for Students <https://github.com/sagemathinc/cocalc/discussions/6879>`_.

################################
First Notice of GPT-4 Use
################################

The first time you use GPT-4, a confirmation dialog requires you set a specific monthly spending limit. You can set any amount. The default is $0. The dialog also lets you add credit to your account, in case you don't have any.

The rates for GPT-4 are available in the dialog.  Also, on any day when you use GPT-4, you'll receive an email statement at the end of the day listing how much you spent (and this is easy to disable).

The confirmation dialog also serves as a reminder to users about the fee before the GPT-4 chat is sent.

After you explicitly set a limit and add credit, you don't get explicitly asked again every time you use GPT-4.

################################
Ongoing Use of GPT-4
################################

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Review Cost and Spending Limits
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can review costs for GPT-4 and GPT-3.5 by visiting https://cocalc.com/settings/purchases. To view and configure spending limits, select ``Self-Imposed Spending Limits`` at the above link.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Default ChatGPT version
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Q: If a student uses GPT-4 once, will CoCalc default to GPT-4 thereafter?

A: No. The default is always GPT-3.5.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Estimated Cost Per Semester
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Q: Can you offer an estimate of typical cost per semester for a student project?

A: Since all use is explicit and manual, e.g., via chat or clicking, in practice it's very difficult to use very much. A typical student might use $10 for an entire semester worth of use. A typical interaction is a few cents, so hundreds of interactions are about $10. You'll quickly get a sense of this because it's listed in the daily statements. The model in CoCalc where you pay for what you actually use is generally more affordable than what is charged by OpenAI or Microsoft.
 
Note that GPT-3.5 is significantly faster (and completely free to CoCalc users), and for some things it's pretty good, so people often use it just because the output appears so quickly.
 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Disabling ChatGPT in a Course
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Note to instructors: It's also possible to fully or partly disable ChatGPT for students in a class, e.g., during an exam. That's in course configuration. See :ref:`restrict-student-projects`.

