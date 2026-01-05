Overview
========

The goal of this page is to give you a good idea of what will happen when you teach a course or run a workshop using CoCalc. Our :doc:`teaching-instructors` has details on individual aspects of the process, but may take a while to go through.

Setting up a Course
-------------------

We recommend creating a separate project for each course, although in some cases different sections of the same course can share the same project. You upgrade it using the instructor license and add other instructors and TAs as collaborators for this project.

Then you need to create a course file and configure it as necessary:

- set title and description
- determine license model for students
- disable some of the functionality for students, if desired
- enroll your students by copy-pasting a list of emails - a separate project will be automatically created for each one

If you need us to install some package/library that is not available on CoCalc yet, or to provide access to a particular dataset, create a support ticket in advance.

Assignments and Handouts
------------------------

An "assignment" is just a folder in your project that contains arbitrary files. Typical steps include:

- **Create** - upload or copy existing files or create new ones in CoCalc, such as Jupyter notebooks, potentially with nbgrader cells.
- **Assign** - put a copy of your files into each student project.
- **Collect** - copy files (hopefully, with work) from each student back into your course project.
- **Grade** - manually or automatically using nbgrader, optionally incorporating peer grading.
- **Return** - make a copy of a graded assignment in the corresponding student project (under a different path than the original one).

A "handout" is the same as an assignment, but without grading process. Perfect for distributing syllabus, class notes, etc.

CoCalc also allows you to "distribute" a terminal command to all student projects, e.g. to install a particular package needed for your course.

Working on Assignments
----------------------

While working on assignments, each student can:

- **stay in a separate dedicated project** without interfering with the work of others
- **create new files and terminals** in addition to editing files copied from you
- **invite other students** for collaboration or group work, *if you allow it*
- **use AI tools** to fix error or generate code, *if you allow it*
- **run nbgrader tests** to check the work, if you have provided them
- **ask you for help** using @-mentions in a side chat
- **recover "lost" work** through TimeTravel and automatic snapshots
- **use JupyterLab, VS Code, or R IDE** if desired

While your students are working on assignments, you can:

- **access student work at any time** without collecting it, to assess how students are doing or to help them
- **use the same state of Jupyter notebooks** that your students have, including widgets
- **see fine-grained writing history** to detect cheating and understand how students approach the problem

Extra Compute Resources
-----------------------

Resources provided by each student project are sufficient for most classes, but if you want your students to go beyond basics, we got you covered! Compute servers allow you to:

- work with basic or advanced GPUs
- experiment with parallel computations on multiple (and numerous) CPU cores
- accommodate large data sets

You can easily create a compute server for each student with the same configuration or give them full flexibility.

CoCalc Roadmap
--------------

These are some of the course-related features that we are planning to add in the future:

- Streamlined support for group assignments: define groups, create a project for each group, add all of its members as collaborators. At the moment you can do these steps manually.
- Exam mode: create a dedicated project for the exam for each student, restrict access to other projects, automatically collect work at a set time. (At the moment we support ephemeral exam mode, where students get an empty project as a scratchpad for their work. Some instructors want exactly that. If you are interested in this or other approaches - contact us to discuss details!)
- Analyze student engagement: see how much time students are actively editing files, determine outliers, see who needs help and who may be cheating. This may involve AI analysis based on your explicit request.
- LMS integration: automatically add and remove students, sync grades. At the moment you can copy students' emails from a CSV file for enrollment and you can export their grades into a CSV file.

Budgeting and Billing
---------------------

CoCalc is not subsidized as some of the alternatives, so teaching a course does require purchasing a suitable license. If you are considering a pilot project using CoCalc, we are happy to learn more about your plans and provide you with a suitable free credit. `Get in touch! <https://cocalc.com/support/new?hideExtra=true&type=question&subject=Considering%20CoCalc&body=I%20want%20to%20teach%20a%20course%20using%20CoCalc%20...&title=Pilot%20Project>`_

For the instructor project we recommend an ongoing monthly or yearly subscription. That way instructors can work on the course material and prepare for teaching throughout the year. Your department or the whole institute may also consider a single subscription to cover all courses to make the process even smoother. Our recommended configuration for instructors is in the range of $20-$30 per month per course depending on the choice of billing term (the number of instructors and TAs for each course does not matter).

For students it is usually more convenient to get a license with specific start and end dates. The standard configuration costs about $10 per month per student.

If you are going to use compute servers, you need to pick a suitable configuration and estimate the number of hours each of them will be used. If you need to preserve the disks of compute servers over several weeks or months, you need to factor it in as well.

*It is possible to let each student individually pay for resources that are configured by the instructor.*

Depending on your bureaucratic constraints, you can use a credit card directly in our store or go with a formal quote, purchase order, invoice process. These invoices can be paid using credit cards, bank transfers, wire transfers, or checks.
