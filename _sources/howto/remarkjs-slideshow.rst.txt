.. index:: RemarkJS Slideshow

===================================
RemarkJS Slideshow
===================================

This guide explains how to use RemarkJS to create a slideshow using Markdown in CoCalc.

A `RemarkJS Slideshow <https://github.com/gnab/remark/wiki>`_ lets you make nice browser-based slideshows using Markdown.


Step 1: HTML barebone
==========================

Create a file named ``remark.html`` with this content::

    <!DOCTYPE html>
    <html>
        <head>
            <title>Title</title>
            <meta charset="utf-8">
            <style>
                @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
                @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
                @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);
                body { font-family: 'Droid Serif'; }
                h1, h2, h3 {
                    font-family: 'Yanone Kaffeesatz';
                    font-weight: normal;
                }
                .remark-code, .remark-inline-code { font-family: 'Ubuntu Mono'; }
            </style>
        </head>
        <body>
            <script src="https://remarkjs.com/downloads/remark-latest.min.js">
            </script>
            <script>
                var slideshow = remark.create({
                    sourceUrl: 'remark.md'
                });
            </script>
        </body>
    </html>

Step 2: Markdown
===================

Create a file ``remark.md`` (in the same directory as ``remark.html``) with this content::

    class: center, middle

    # Title

    ---

    # Agenda for us!!!!

    1. Introduction
    2. Deep-dive
    3. blah
    4. Stuff!

    ---

    # Introduction

Step 3: Check
======================

Go back to the ``remark.html`` editor tab; you should show the slideshow on the right.
Close the "Source code" frame of remark.html, to show only the rendered iframe.

Step 4: Write Slideshow
=========================

Switch to the ``remark.md`` file and make some changes.
There are some `important features beyond just markdown <https://github.com/gnab/remark/wiki/Markdown#slide-properties>`_
for making slides.

Switch back to ``remark.html`` any time to see the updated version.

Step 5: Present
===================

For the actual presentation, click the checkbox to the left of ``remark.html`` in the main listing, then click "Download", and click on the download link to open it in a tab of your browser.
Press "P" to toggle presentation mode.


