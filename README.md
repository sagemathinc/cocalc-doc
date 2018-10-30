# CoCalc User Manual

This is a documentation of CoCalc's features for users.
It covers topics like teaching, editing LaTeX documents,
calculating with Jupyter Notebooks and Sage Worksheets, etc.

- [CoCalc online service](https://cocalc.com/)
- [CoCalc source code](https://github.com/sagemathinc/cocalc)

## Development

[![Build Status](https://travis-ci.org/sagemathinc/cocalc-doc.svg?branch=master)](https://travis-ci.org/sagemathinc/cocalc-doc)

Note: the `Makefile` configures sphinx to throw warnings as errors.
Hence even small details like a broken URL link will cause a failed build.

### Prerequisites

- Sphinx 1.6+ (aiming for 1.8+)
- Knowledge about [ReST Doc](http://www.sphinx-doc.org/en/1.8/rest.html)

### Build

- In the root directory, run `make html`
- Before submitting a PR, make sure it works by cleaning up first: `make clean`
- With `inotifywait` installed, `make watch` should automatically build the html files upon changes.

## Legal

- License: [GNU Free Documentation License](LICENSE.md)

- "CoCalc" is a [registered trademark](http://tsdr.uspto.gov/#caseNumber=87155974&caseType=SERIAL_NO&searchType=statusSearch).

- Book graphic attribution: https://commons.wikimedia.org/wiki/File:Book_text.svg