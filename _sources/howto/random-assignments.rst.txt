.. index:: Git
.. index:: GitHub
.. index:: GitLab
.. index:: Bitbucket

=========================
Randomized Assignments
=========================

This guide outlines how you can distribute randomized assignments to students.
To learn more about course management, please read the :ref:`instructor-guide`.

.. warning::

    The procedure described below is a "hack". Please be careful and try it in a test course first!


The plan is to create 6 slightly different notebooks as assignments to all your students.

First, you need to serve those 6 quizzes somewhere online. You could put them into a directory on CoCalc and :doc:`../share` that directory. Set its visibility to "unlisted" (the option in the middle). For the next step, copy the resulting "raw" URL to the actual file – not the URL of the share page. In any case, the goal is to serve files numbered 1 to 6 like this (the URL is exactly the same except for the number, hence you have to share the directory, not each file!):

- ``https://share.cocalc.com/...subdir/file-1.ipynb?viewer=raw``
- ``https://share.cocalc.com/...subdir/file-2.ipynb?viewer=raw``
- ``[...]``
- ``https://share.cocalc.com/...subdir/file-6.ipynb?viewer=raw``

Next, create an assignment directory for the quizzes. You could assign an empty directory to all students. Let's assume it's called assignment/quiz-1 for now.

Finally, in the course configuration is a text box under "Run Terminal command in all student projects". What we'll do is to run a small script in each student project, which randomly downloads one of these 6 files right into the assignment directory!

Here is a command that should work::

    curl "https://share.cocalc.com/...subdir/file-$((1 + RANDOM % 6)).ipynb" > "assignment/quiz-1/quiz.ipynb"

- The ``$(( ... ))`` generates a random digit character from 1 to (including) 6 – make sure to use `" ... "` quotes!
- ``curl`` downloads the file and the ``>`` operator saves this in the assignment's path with that filename.

Once it's done, everyone will work in a file called ``quiz.ipynb``. You can collect the assignment to get all answers.

If you want to keep the filename, this should also work via ``wget``, probably something like::

    cd assignment/quiz-1/ && wget -q "https://some.domain/subdir/file-$((1 + RANDOM % 6)).ipynb"

PS: if something goes wrong on first try, you can clean up the directory in all student projects via: ``rm -rf assignment/quiz-1/; mkdir assignment/quiz-1/``

