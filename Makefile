# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
SPHINXOPTS    =

# use this commit hash when the user's guide is built independently
# when built within invest, the sample data commit hash from invest is used
GIT_SAMPLE_DATA_REPO        := https://bitbucket.org/natcap/invest-sample-data.git
GIT_SAMPLE_DATA_REPO_PATH   := invest-sample-data
GIT_SAMPLE_DATA_REPO_REV    := c8df675a2c446bf8d00ffd8f0cbab933f7d5c25a

.PHONY: help clean html changes linkcheck get_sampledata

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean           to remove the build directory"
	@echo "  html            to make standalone HTML files"
	@echo "  changes         to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck       to check all external links for integrity"
	@echo "  get_sampledata  to check out the invest-sample-data repo"
	@echo "  prep_sampledata to create modified tables in invest-sample-data that display nicely"

clean:
	-rm -rf $(BUILDDIR)/*

# files in source/ reference tables from the invest-sample-data repo to avoid duplication
# it is assumed that a clone of invest-sample-data exists in the top level of
# invest.users-guide, and that certain modified files created by `prep_sampledata` exist,
# before `make html` is called.
html: $(SOURCEDIR) prep_sampledata
	$(SPHINXBUILD) -W -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html

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

get_sampledata:
	-git clone $(GIT_SAMPLE_DATA_REPO) $(GIT_SAMPLE_DATA_REPO_PATH)
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) fetch
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) lfs install
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) lfs fetch
	git -C $(GIT_SAMPLE_DATA_REPO_PATH) checkout $(GIT_SAMPLE_DATA_REPO_REV)

prep_sampledata:
	# take selections of tables that are too long to display in full
	head -n1 invest-sample-data/pollination/landcover_biophysical_table.csv > invest-sample-data/pollination/landcover_biophysical_table_modified.csv
	tail -n3 invest-sample-data/pollination/landcover_biophysical_table.csv >> invest-sample-data/pollination/landcover_biophysical_table_modified.csv

	head -n2 invest-sample-data/Carbon/carbon_pools_willamette.csv > invest-sample-data/Carbon/carbon_pools_willamette_modified.csv
	tail -n4 invest-sample-data/Carbon/carbon_pools_willamette.csv >> invest-sample-data/Carbon/carbon_pools_willamette_modified.csv

	head -n7 invest-sample-data/WaveEnergy/input/Machine_Pelamis_Performance.csv > invest-sample-data/WaveEnergy/input/Machine_Pelamis_Performance_modified.csv

	head -n4 invest-sample-data/WindEnergy/input/NE_sub_pts.csv > invest-sample-data/WindEnergy/input/NE_sub_pts_modified.csv
