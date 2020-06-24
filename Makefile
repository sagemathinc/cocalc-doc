# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = CoCalcManual
SOURCEDIR     = source
BUILDDIR      = build
APIIDX        = source/api/index.md

.PHONY: help Makefile watch api
.SUFFIXES: json py rst md

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

watch: api html
	while inotifywait -re close_write,moved_to,create source; do make html; done

api: Makefile $(APIIDX)

$(APIIDX): api.json api.py
	#python3 api.py

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile api
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

