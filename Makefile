# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
SPHINXOPTS    =

# use this commit hash when the user's guide is built independently
# when built within invest, the sample data commit hash from invest is used
GIT_SAMPLE_DATA_REPO        := https://bitbucket.org/natc../../invest-sample-data.git
GIT_SAMPLE_DATA_REPO_PATH   := invest-sample-data
GIT_SAMPLE_DATA_REPO_REV    := 9adec6ee9000e192589b3538ff381e574c1812d6

.PHONY: help clean html gettext changes linkcheck prep_sampledata test_investspec

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean               to remove the build directory"
	@echo "  html                to make standalone HTML files"
	@echo "  changes             to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck           to check all external links for integrity"
	@echo "  $(GIT_SAMPLE_DATA_REPO_PATH)  to check out the invest-sample-data repo"
	@echo "  prep_sampledata     to create modified tables in invest-sample-data that display nicely"
	@echo "  test_investspec     to run unit tests for the custom Sphinx extension"

clean:
	-rm -rf $(BUILDDIR)/*

# files in source/ reference tables from the invest-sample-data repo to avoid duplication
# it is assumed that a clone of invest-sample-data exists in the top level of
# invest.users-guide, and that certain modified files created by `prep_sampledata` exist,
# before `make html` is called.
html: $(SOURCEDIR) prep_sampledata
	for language in en ; do \
		$(SPHINXBUILD) -W -b html $(SPHINXOPTS) \
		-c $(SOURCEDIR) \
		-D language=$$language \
		$(SOURCEDIR)/$$language $(BUILDDIR)/html/$$language ; \
	done

# extracts messages from source and creates POT files in build/gettext
gettext: $(SOURCEDIR)
	$(SPHINXBUILD) -M gettext $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)

changes: $(SOURCEDIR)
	$(SPHINXBUILD) -b changes $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/changes

linkcheck: $(SOURCEDIR)
	# Occasionally this will fail with a 403 error on links that work in your browser
	# So far it's been enough to replace them with an alternate link to the same paper
	# If it continues to be a problem, configuring the user-agent may help:
	# https://github.com/sphinx-doc/sphinx/issues/7369
	$(SPHINXBUILD) -b linkcheck $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

test_investspec:
	cd extensions/investspec && python -m unittest test.test_investspec

# initialize the sample data repo and check out the commit
$(GIT_SAMPLE_DATA_REPO_PATH):
	mkdir $(GIT_SAMPLE_DATA_REPO_PATH) && cd $(GIT_SAMPLE_DATA_REPO_PATH)
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) init
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) remote add origin $(GIT_SAMPLE_DATA_REPO)
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) fetch --depth 1 origin $(GIT_SAMPLE_DATA_REPO_REV)
	# GIT_LFS_SKIP_SMUDGE=1 prevents getting all the lfs files, we only need the CSVs
	GIT_LFS_SKIP_SMUDGE=1 git -C $(GIT_SAMPLE_DATA_REPO_PATH) checkout $(GIT_SAMPLE_DATA_REPO_REV)

prep_sampledata: $(GIT_SAMPLE_DATA_REPO_PATH)
	# take selections of tables that are too long to display in full
	head -n1 invest-sample-data/pollination/landcover_biophysical_table.csv > invest-sample-data/pollination/landcover_biophysical_table_modified.csv
	tail -n3 invest-sample-data/pollination/landcover_biophysical_table.csv >> invest-sample-data/pollination/landcover_biophysical_table_modified.csv

	head -n2 invest-sample-data/Carbon/carbon_pools_willamette.csv > invest-sample-data/Carbon/carbon_pools_willamette_modified.csv
	tail -n4 invest-sample-data/Carbon/carbon_pools_willamette.csv >> invest-sample-data/Carbon/carbon_pools_willamette_modified.csv

	head -n7 invest-sample-data/WaveEnergy/input/Machine_Pelamis_Performance.csv > invest-sample-data/WaveEnergy/input/Machine_Pelamis_Performance_modified.csv

	head -n4 invest-sample-data/WindEnergy/input/NE_sub_pts.csv > invest-sample-data/WindEnergy/input/NE_sub_pts_modified.csv
