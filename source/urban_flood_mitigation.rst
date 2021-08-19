.. _ufrm:

*********************************
Urban Flood Risk Mitigation model
*********************************

Introduction
============

Flood hazard comes from different sources, including: riverine (or fluvial) flooding, coastal flooding, and stormwater (or urban) flooding - the focus of this InVEST model. Natural infrastructure can play a role for each of these flood hazards. Related to stormwater flooding, natural infrastructure operates mainly by reducing runoff production, slowing surface flows, and creating space for water (in floodplains or basins).

The InVEST model calculates the runoff reduction, i.e. the amount of runoff retained per pixel compared to the storm volume. For each watershed, it also calculates the potential economic damage by overlaying information on flood extent potential and built infrastructure.

The model
=========

How it works
^^^^^^^^^^^^

Runoff production and runoff attenuation index
----------------------------------------------

For each pixel :math:`i`, defined by a land use type and soil characteristics, we estimate runoff :math:`Q` (mm) with the Curve Number method:

.. math:: Q_{p,i} = \begin{Bmatrix}
        \frac{(P - \lambda S_{max_i})^2}{P + (1-\lambda) S_{max,i}} & if & P > \lambda \cdot S_{max,i} \\
        0 & & otherwise
        \end{Bmatrix}
    :label: runoff

Where :math:`P` is the design storm depth in mm, :math:`S_{max,i}` is the potential retention in mm, and :math:`\lambda \cdot S_{max}` is the rainfall depth needed to initiate runoff, also called the initial abstraction (:math:`\lambda=0.2` for simplification).

:math:`S_{max}` (calculated in mm) is a function of the curve number, :math:`CN`, an empirical parameter that depends on land use and soil characteristics (NRCS 2004):

.. math:: S_{max,i}=\frac{25400}{CN_i}-254
    :label:

The model then calculates runoff retention per pixel :math:`R_i` as:

.. math:: R_i=1-\frac{Q_{p,i}}{P}
    :label: runoff_retention

And runoff retention volume per pixel :math:`R\_m3_i` as:

.. math:: R\_m3_i=R_i\cdot P\cdot pixel.area\cdot 10^{-3}
    :label: runoff_retention_volume

With :math:`pixel.area` in :math:`m^2`.

Runoff volume (also referred to as "flood volume") per pixel :math:`Q\_m3_i` is also calculated as:

.. math:: Q\_m3_i=Q_{p,i}\cdot pixel.area\cdot 10^{-3}
   :label: flood_volume

Calculate potential service (optional)
--------------------------------------
The service is the monetary valuation of avoided damage to built infrastructure and number of people at risk. As of this version of InVEST, the population metrics described here are not yet implemented.

For each watershed (or sewershed) with flood-prone areas, compute:

 * **Affected.Pop** : total potential number of people affected by flooding (could focus on vulnerable groups only, e.g. related to age, language, etc. See Arkema et al., 2017, for a review of social vulnerability metrics). This metric is calculated by summing the population in the intersection of the two shapefiles (watershed and flood-prone area).
 * :math:`Affected.Build` : sum of potential damage to built infrastructure in $, This metric is calculated by multiplying building footprint area within the watershed and potential damage values in :math:`m^2`.

Aggregation of runoff retention and potential service values at the watershed scale
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

For each watershed, compute the following indicator of the runoff retention service:

.. math:: Service.built=Affected.Build\sum_{watershed}R\_m3_i
   :label: service.built

where :math:`pixel.area` is the pixel area (:math:`m^2`), :math:`Service.built` is expressed in :math:`m^3`.

Limitations and simplifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 **Runoff production:** the model uses a simple approach (SCS-Curve Number), which introduces high uncertainties. However, the ranking between different land uses is generally well captured by such an approach, i.e. that the effect of natural infrastructure will be qualitatively represented in the model outputs. Future work will aim to include a routing over the landscape: ideas include TOPMODEL (there is an R package), UFORE (used in iTree), CADDIES, etc

 **Valuation approaches:** Currently, a simple approach to value flood risk retention is implemented, valuing flood risk as the avoided damage for built infrastructure. Alternative approaches (e.g. related to mortality, morbidity, or economic disruption) could be implemented.

Data needs
==========

Spatial layers for Urban Flood Mitigation may have different coordinate systems, but they must all be projected coordinate systems, not geographic. Raster inputs may have different cell sizes, and they will be resampled to match the cell size of the land use/land cover raster. Therefore, raster model results will have the same cell size as the land use/land cover raster.

 * **Workspace** (required): Folder where model outputs will be written. Make sure that there is ample disk space, and write permissions are correct.

 * **Suffix** (optional). Text string that will be appended to the end of output file names, as "_Suffix". Use a Suffix to differentiate model runs, for example by providing a short name for each scenario. If a Suffix is not provided, or changed between model runs, the tool will overwrite previous results.

 * **Watershed Vector** (required). shapefile delineating areas of interest, which should be hydrologic units: watersheds or sewersheds.

 * **Depth of rainfail in mm** (required). This is :math:`P` in equation :eq:`runoff`.

 * **Land Cover Map** (required). Raster of land use/land cover (LULC) for each pixel, where each unique integer represents a different land use/land cover class. All values in this raster MUST have corresponding entries in the Land Cover Biophysical Table. The model will use the resolution of this layer to resample all outputs. The resolution should be small enough to capture the effect of green areas in the landscape, although LULC categories can comprise a mix of vegetated and non-vegetated covers (e.g. "residential", which may have 30% canopy cover, and have biophysical table parameters that change accordingly)

 * **Soils Hydrological Group Raster** (required). Raster of categorical hydrological groups. Pixel values must be limited to 1, 2, 3, or 4, which correspond to soil hydrologic group A, B, C, or D, respectively (used to derive the CN number)

 * **Biophysical Table** (required). A .csv (Comma Separated Value) table containing model information corresponding to each of the land use classes in the Land Cover Map. All LULC classes in the Land Cover raster MUST have corresponding values in this table. Each row is a land use/land cover class and columns must be named and defined as follows:

    * **lucode**: Land use/land cover class code. LULC codes must match the **value** column in the Land Cover Map raster and must be integers and unique.

    * Curve number (CN) values for each LULC type and each hydrologic soil group. Column names should be: **CN_A**, **CN_B**, **CN_C**, **CN_D**, which the letter suffix corresponding to the hydrologic soil group

 * **Built Infrastructure Vector** (optional): shapefile with built infrastructure footprints. The attribute table must contain a column 'Type', with integers referencing the building type (e.g. 1=residential, 2=office, etc.)

 * **Damage Loss Table** (optional): Table with columns **"Type"** and **"Damage"** with values of built infrastructure type (see above) and potential damage loss (in $/:math:`m^2`)

Interpreting outputs
====================

 * **Parameter log**: Each time the model is run, a text (.txt) file will be created in the Workspace. The file will list the parameter values and output messages for that run and will be named according to the service, the date and time. When contacting NatCap about errors in a model run, please include the parameter log.

 * **Runoff_retention.tif**: raster with runoff retention values (no unit, relative to precipitation volume).  Calculated from equation :eq:`runoff_retention`.

 * **Runoff_retention_m3.tif**: raster with runoff retention values (in :math:`m^3`).  Calculated from equation :eq:`runoff_retention_volume`.

 * **Q_mm.tif**: raster with runoff values (mm).  Calculated from equation :eq:`runoff`.

 * **flood_risk_service.shp**: Shapefile with results in the attribute table:

    * **rnf_rt_idx**: average of runoff retention values (:math:`R_i`) per watershed

    * **rnf_rt_m3**: sum of runoff retention volumes (:math:`R\_m3_i`), in :math:`m^3`, per watershed.

    * **flood_vol**: The flood volume (``Q_m3``, equation :eq:`flood_volume`) per watershed.

    * **aff_bld**: potential damage to built infrastructure in $, per watershed.  Only calculated when the Built Infrastructure Vector input is provided.

    * **serv_blt**: :math:`Service.built` values for this watershed (see equation :eq:`service.built`).  An indicator of the runoff retention service for the watershed.  Only calculated when the Built Infrastructure Vector input is provided.

Appendix: Data sources and guidance for parameter selection
===========================================================

:ref:`LULC <lulc>`
^^^^^^^^^^^^^^^^^^

:ref:`Watersheds <watersheds>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Design Storm Precipitation <design_storm>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Soil Groups <soil_groups>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Curve Number <cn>`
^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Built Infrastructure <buildings>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Potential damage loss for each building type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the US, HAZUS provides damage data. Globally, a recent report from the European Commission provides useful data: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC105688/global_flood_depth-damage_functions__10042017.pdf


References
==========

NRCS-USDA Part 630 Hydrology National Engineering Handbook, Chapter 7 Hydrologic Soil Groups. 2007. 

NRCS-USDA Part 630 Hydrology National Engineering Handbook, Chapter 9 Hydrologic Soil-Cover Complexes. 2004.

NRCS-USDA Part 630 Hydrology National Engineering Handbook, Chapter 10 Estimation of Direct Runoff from Storm Rainfall. 2004.
