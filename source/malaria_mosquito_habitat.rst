.. _malaria_mosquito_habitat:

************************
Malaria Mosquito Habitat
************************

Summary
=======

Model the suitability of mosquito breeding areas, the impact on a human population, and the relative impacts of the landscape.


Introduction
============

The model
=========

How it works
------------

Mosquito breeding site suitability
----------------------------------

The suitability index of a mosquito breeding ground in a given pixel is defined as

.. math:: q_i = b_i e ^{-s_i} \log f_i

where

 * :math:`q_i` is the suitability rating of cell :math:`i`
 * :math:`b_i` is the land type breeding suitability rating of the land cover in cell :math:`i`, this is a function of the land cover type in cell :math:`i`
 * :math:`s_i` the slope of cell `i`
 * :math:`f_i` the flow accumulation at cell :math:`i`.

Breeding Site Influence
-----------------------

Once the suitability of a mosquito breeding grounds is calculated for a landscape, the influence of that ground over a population center in cell :math:`i` given as

.. math:: c_i = \sum_{j \in \mathrm{landscape}} q_j p_j e^{-d_{ij} \alpha}

where

 * :math:`d_ij` is the distance from the center of cell :math:`i` to cell :math:`j`
 * :math:`p_j` is the human population density of cell :math:`j`
 * :math:`\alpha` is the mean flight distance of the mosquito species

Influential Breeding Sites
--------------------------

Once the influence of the breeding grounds are projected on a landscape, the most influential breeding sites can be calculated as

.. math:: f_i = q_i \sum_{j \in \mathrm{landscape}} c_j e^{-d_{ij}}


Limitations and simplifications
===============================


Data Needs
==========

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory. To run multiple scenarios, create a new workspace for each scenario.

 * **DEM**: A height map raster of the area used to calculate slope and flow accumulation.

 * **Land cover map**: A raster indicating land types which is used to determine base breeding ground suitability.

 * **Land cover type suitability table**: a csv file with the fields `lucode` corresponding to the land use codes in the land cover map and `breeding_suitability_index` which is a number between 0 (not suitable) and 1 (most suitable) indicating the suitability of that land cover type for mosquito breeding grounds.

 * **Population Density map**: A raster indicating human population density.

 * **Mean mosquito flight distance**: The mean distance in meters that a mosquoto will travel to feed from its breeding site.

 * **Threshold Flow Accumulation**: The number of upstream pixels before a cell is classified as a running stream (not standing water).


 * **Amount of area available for conversion**: A value in hectares of how much land is under consideration for conversion.  The model will indicate the area on the land cover map most suitable for conversion to mitigate influence from mosquito breeding grounds.

Running the Model
=================

If you encounter any errors please email the output log to richsharp@stanford.edu.

Interpreting Results
====================

Model Outputs
-------------

Each of model output files is saved in the ``Output`` and ``Intermediate`` folders that are saved within the user-specified workspace.

**Output folder**

 * ``Output\\foo.tif``: 

**Intermediate folder**

 * ``Intermediate\bar.tif``:

References
==========

Foo, B. 1996. Mosquitoes 'n shit. Environ. Eng. Res. 1:1-13.

..  LocalWords:  InVEST advection nabla cdot mathbf eq advective mathrm AOI csv
..  LocalWords:  ESRI Shapefile WPS shapefile kh biogeochemical se floathomes
..  LocalWords:  eutrophication frac UC VC Eulerian MacCready Geyer Thomann eqx
..  LocalWords:  Wappinger Fishkill northerns Quayas advected Nicolson coli kx
..  LocalWords:  coliforms enterococci coliform Indictor Stormwater lookup exe
..  LocalWords:  resuspension tif discritize discritized quo Lemmens th px
..  LocalWords:  Clayoquot Maccready
