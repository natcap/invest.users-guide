These source files, in restructured text format, are designed to be compiled into stand-alone HTML documents
(and sometimes PDF) using the Sphinx documentation generator (http://sphinx.pocoo.org/).

See requirements.txt for the python dependencies required to build the documentation.

Some source files reference tables from the [invest-sample-data](https://bitbucket.org/natcap/invest-sample-data/src/master/) repo.
A clone of `invest-sample-data` must exist in the top level of this repo before you build the documentation.
Execute the following command to clone `invest-sample-data` and check out the correct revision:

`make get_sampledata`

Execute the following command to build HTML documentation from the reStructuredText source:

`make html`

Then find the html documents in `build/html` and view them in a web browser to evaulate for correctness.

## Style Guidelines

Our [style guide google doc](https://docs.google.com/document/d/1BHwHDu_I-x0s_2GsbUb4rfVmXMkl7kl97sx2suBTLh8/edit?usp=sharing) is actively being developed.
For anything not listed in our style guide, follow the [Google developer documentation style guidelines](https://developers.google.com/style).

## Requirements

`requirements.txt` is the complete list of requirements needed to build the user's guide.
However, `pip install -r requirements.txt` will fail in a fresh environment because `natcap.invest` depends on `gdal`, which cannot be `pip install`ed unless the GDAL library and headers already exist on the system.

Since the GDAL library and headers can be installed with `conda`, an `environment.yml` is included that will install GDAL with `conda`, and then the rest of the requirements with `pip`.
