import datetime
import os
import re
import subprocess
import sys

import requests
import setuptools_scm  # Just fail the process if this can't be found.
import yaml

# add to the path so that sphinx can find our custom extension
sys.path.append(os.path.abspath('../extensions/investspec'))

# this is for the ReadTheDocs build, where conf.py is the only place we can
# run arbitrary commands such as checking out the sample data
subprocess.run(['make', '-C', '..', 'prep_sampledata'])

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_reredirects',
    'investspec'
]

# config value for the investspec custom extension
# this is prefixed onto the :investspec: role's `module` argument before importing
# this way, we don't have to write 'natcap.invest' every time
investspec_module_prefix = 'natcap.invest'

# Enable figure number referencing with the :numref: syntax
numfig = True
#math_numfig = False  # Number equations by chapter, not cumulatively

gettext_compact = False

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'InVEST®'

# configure user-agent to avoid 403 errors on linkcheck
# https://github.com/sphinx-doc/sphinx/issues/7369
# This user agent string is coming from James' mac.
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0'

# this link has been unreliable but still seems to exist as of 3/2021. revisit in the future
linkcheck_ignore = [
    'http://trapdoor.bren.ucsb.edu/research/2014Group_Projects/documents/BermudaWind_Final_Report_2014-05-07.pdf']

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
    git_version = subprocess.check_output(
        ['python', 'setup.py', '--version'], cwd='../../..').decode("ASCII")
    git_version = git_version.rstrip()  # remove the trailing newline

    # If in a development build, note that we're in an InVEST repo-managed version
    if 'post' in git_version:
        git_version = git_version.replace('+', '+invest.')
except subprocess.CalledProcessError:
    # If we're in a standalone build (like with the on-demand, always-updated
    # UG build), use the version string for the UG.
    git_version = setuptools_scm.get_version(
        version_scheme='post-release', local_scheme='node-and-date',
        root='..')

    # If not at a tag, note that we're in a UG repo-managed version
    if 'post' in git_version:
        git_version = git_version.replace('+', '+ug.')

# We decided on slack 2023-06-19 that the UG version in the citation should
# only be the version in the latest
version = git_version.split('.post')[0]

# The full version, including alpha/beta/rc tags.
print(f'Version: {version}')

# Guard against malformed version strings (like when setuptools_scm can't get
# the full version string)
if not re.match('^[1-9]\\.[0-9]+\\.[0-9]+', version):
    raise AssertionError(
        f"Invalid version string, did you clone the full git tree? {version}")

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# When a page is moved, redirect to the new page.
# Provided by the sphinx-reredirects extension.
redirects = {
    'reservoirhydropowerproduction': 'annual_water_yield.html',
}

# -- Options for HTML output --------------------------------------------------

# Alabaster is the default theme
html_theme = 'alabaster'

html_logo = 'en/index/InVEST_logo_300x300.png'
html_theme_options = {
    'analytics_id': 'UA-787904-8',
    'fixed_sidebar': True,
    'github_user': 'natcap',
    'github_repo': 'invest.users-guide',
    # Custom fonts are installed in the template file layout.html
    'font_family': "'Source Serif 4', serif",
}

html_sidebars = {
    '**': [
        'about.html',
        'localtoc.html',
        'searchbox.html'
    ]
}

# Don't generate an index
html_use_index = False

# Don't generate a domain-specific index
html_domain_indices = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

html_static_path = ['custom.css']

templates_path = ["_templates"]

# -- Internationalization options ---------------------------------------------
locale_dirs = ['locales/']
gettext_compact = False

# -- Substitutions ------------------------------------------------------------

# Get the YYYY year from the current commit in the user's guide.
try:
    commit_year = subprocess.run(
        ['git', 'show', '-s', '--format=%cs', 'HEAD'],
        capture_output=True).stdout.decode('ASCII').strip().split('-')[0]
except subprocess.CalledProcessError:
    # If there's an error, default to the current year.
    commit_year = datetime.datetime.now().year

citation_text = None  # In case we can't access the citation
try:
    citation_filepath = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'CITATION.cff')
    with open(citation_filepath) as citation_file:
        citation_text = citation_file.read()
    print('Loaded citation from local CITATION.cff')
except FileNotFoundError:
    try:
        citation_file_resp = requests.get(
            'https://raw.githubusercontent.com/'
            'natcap/invest/{git_version}/CITATION.cff')
        citation_file_resp.raise_for_status()  # fail if 404
        citation_text = citation_file_resp.text
        print(f'Loaded citation from remote CITATION.cff, using {git_version}')
    except requests.HTTPError:
        pass

invest_doi = 'https://doi.org/10.60793/natcap-invest-3.16.0'
if not citation_text:
    print("Falling back to default citation")
else:
    for doi_data in yaml.load(citation_text,
                              Loader=yaml.Loader)['identifiers']:
        if doi_data['type'] != 'doi':
            continue

        if doi_data['description'] == (
                'Persistent identifier for this version of InVEST'):
            invest_doi = f"https://doi.org/{doi_data['value']}"
            break
print(invest_doi)

# Here we expose variables for use in our RST pages.
rst_prolog = f"""
.. |commit_year| replace:: {commit_year}
.. |git_version| replace:: {git_version}
.. |invest_doi| replace:: {invest_doi}
"""


# Shoehorning the git commit information into the copyright.
# This feels like a hacky shortcut, but it's easier to do than the custom theme
# modification needed to do it 'right' and it does what it needs to.
copyright = f'The Natural Capital Project. | Build {git_version}'
