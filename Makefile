# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
SPHINXOPTS    = 

.PHONY: help clean html changes linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean     to remove the build directory"
	@echo "  html      to make standalone HTML files"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"

clean:
	-rm -rf $(BUILDDIR)/*

html: $(SOURCEDIR)
	$(SPHINXBUILD) -W -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html

changes: $(SOURCEDIR)
	$(SPHINXBUILD) -b changes $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/changes

linkcheck: $(SOURCEDIR)
	$(SPHINXBUILD) -b linkcheck $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."
