import sys, os
import subprocess
import setuptools_scm  # Just fail the process if this can't be found.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------
if not os.path.exists('../invest-sample-data'):
    subprocess.run(['make', '-C', '..', 'get_sampledata'])
if not os.path.exists('invest-sample-data/pollination/landcover_biophysical_table_modified.csv'):
    subprocess.run(['make', '-C', '..', 'prep_sampledata'])

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_reredirects'
]

# Enable figure number referencing with the :numref: syntax
numfig = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

gettext_compact = False

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'InVEST'
copyright = '2021, The Natural Capital Project'

# configure user-agent to avoid 403 errors on linkcheck
# https://github.com/sphinx-doc/sphinx/issues/7369
# This user agent string is coming from James' mac.
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0'

# this link has been unreliable but still seems to exist as of 3/2021. revisit in the future
linkcheck_ignore = ['http://trapdoor.bren.ucsb.edu/research/2014Group_Projects/documents/BermudaWind_Final_Report_2014-05-07.pdf']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# If we're building the docs and have knowledge of the natcap.invest package,
# use the version string. If the version of natcap.invest cannot be found,
# raise an exception.
try:
    # If we're within an InVEST build context, use the InVEST version string.
    import subprocess
    version = subprocess.check_output(
        ['python', 'setup.py', '--version'], cwd='../../..').decode("ASCII")
    version = version.rstrip()  # remove the trailing newline

    # If in a development build, note that we're in an InVEST repo-managed version
    if 'post' in version:
        version = version.replace('+', '+invest.')
except subprocess.CalledProcessError:
    # If we're in a standalone build (like with the on-demand, always-updated
    # UG build), use the version string for the UG.
    version = setuptools_scm.get_version(
        version_scheme='post-release', local_scheme='node-and-date',
        root='..')

    # If not at a tag, note that we're in a UG repo-managed version
    if 'post' in version:
        version = version.replace('+', '+ug.')

# The full version, including alpha/beta/rc tags.
print (f'Version: {version}')

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# When a page is moved, redirect to the new page.
# Provided by the sphinx-reredirects extension.
redirects = {
    'reservoirhydropowerproduction': 'annual_water_yield.html',
}


# -- Options for HTML output ---------------------------------------------------

html_theme = 'natcapUG'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../themes']

# Don't generate an index
html_use_index = False

# Don't generate a domain-specific index
html_domain_indices = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
