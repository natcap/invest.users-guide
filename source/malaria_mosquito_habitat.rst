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

.. math:: q_i = p_i \cdot e ^{-s_i} \cdot \log f_i

where

 * :math:`q_i` is the suitability rating of cell :math:`i`
 * :math:`p_i` is the land type breeding suitability rating of the land cover in cell :math:`i`, this is a function of the land cover type in cell `i`
 * :math:`s_i` the slope of cell `i`
 * :math:`f_i` the flow accumulation at cell :math:`i`

Breeding Site Influence
-----------------------

Limitations and simplifications
===============================


Data Needs
==========

The following are the data needs for the Marine Water Quality Model.  The model is distributed with default arguments which are defaulted in the following parameters on the tool's first run.

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory. To run multiple scenarios, create a new workspace for each scenario.

 * **DEM**: 

 * **Land cover map**:

 * **Land cover type suitability table**

 * **Population Density map**:

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
