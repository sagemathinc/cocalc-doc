=============================
latex
=============================

Use the ``latex`` endpoint to compile a latex document. This endpoint converts a tex file to pdf, and stores the pdf
temporarily as a blob in CoCalc's PostgreSQL database. The tmp files used
for compilation are cleaned up. You can specify a ``project_id`` in the
API call, or leave that off and your most recent project gets used
automatically (or a new one created). By default the compilation uses "latexmk" with certain options, but you can specify a custom ``command`` parameter to convert the tex to pdf.

.. code:: bash

    x='sk_xxxxx' # your API key

    # c is the latex document as a text string
    c='\documentclass{article}\begin{document}\section{Main Section}Hello.\end{document}'

    curl -sk \
      -u $x: \
      -d path=/tmp/d.tex \
      -d content="$c" \
      https://cocalc.com/api/v2/latex | jq '.url'
      
    echo
    
    ### sample output is a url
    ### browse to this link to see the compiled pdf document
    "https://cocalc.com/blobs/tmp/d.pdf?uuid=36862b42-2634-11ed-889d-3b8b6aedd65b"

You can learn more about the ``latex`` endpoint by viewing the source code at `https://github.com/sagemathinc/.../api/v2/latex.ts <https://github.com/sagemathinc/cocalc/blob/master/src/packages/next/pages/api/v2/latex.ts>`__.
