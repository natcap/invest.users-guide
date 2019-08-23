.. primer
.. _ufrm:

************************************************
Urban Flood risk mitigation model - User's guide
************************************************

Introduction
============

Flood hazard comes from different sources, including: riverine (or fluvial) flooding, stormwater (or urban) flooding, and coastal flooding. Natural infrastructure can play a role for each of these. Related to stormwater flooding - the focus of the InVEST flood risk mitigation model, natural infrastructure operates mainly by: reducing runoff production, slowing surface flows, creating space for water (in floodplains or basins). The InVEST model calculates the runoff reduction, i.e. the amount of runoff retained per pixel compared to the storm volume. It also calculates, for each watershed, the potential economic damage, by overlaying information on flood extent potential and built infrastructure.

The model
=========

How it works
^^^^^^^^^^^^

*Runoff production and runoff attenuation index*

For each pixel i, defined by a land use type and soil characteristics, we estimate runoff Q (mm) with the Curve Number method:

.. math:: Q_{p,i}=\frac{(P-\lambda S_{max,i})^2}{P+(1-\lambda)S_{max,i}} if >\lambda S_{max,i}; Q=0\ otherwise.
    :label: Eq. 1

Where P is the design storm depth in mm, :math:`S_{max,i}` is the potential retention in mm, and :math:`\lambda S_{max}` is the rainfall depth needed to initiate runoff, also called the initial abstraction (=0.2 for simplification).

:math:`S_{max}` is a function of the curve number, CN, an empirical parameter that depends on land use and soil characteristics (NRCS 2004):

.. math:: S_{max,i}=\frac{25400}{CN_i}-254\ (S_{max}\ in\ mm)
    :label: Eq. 2

The model then calculates runoff retention as:

.. math:: R_i=1-\frac{Q_{p,i}}{P}
    :label: Eq. 3

And runoff retention volume as:

.. math:: R\_m3_i=R_i\cdot P\cdot pixel.area\cdot 10^{-3}

With pixel.area in m2.

Runoff volumes are also calculated as:

.. math:: Q\_m3_i=Q_i\cdot P\cdot pixel.area\cdot 10^{-3}

*Calculate potential service (optional): monetary valuation of avoided damage to built infrastructure and number of people at risk*

For each watershed (or sewershed) with flood-prone areas, compute:

 * Affected.Pop : total potential number of people affected by flooding (could focus on vulnerable groups only, e.g. related to age, language, etc. see Arkema et al., 2017, for a review of social vulnerability metrics). This metric is calculated by summing the population in the intersection of the two shapefiles (watershed and flood-prone area)
 * Affected.Build : sum of potential damage to built infrastructure in $, This metric is calculated by multiplying building footprint area and potential damage values in $/m2).

*Aggregation of runoff retention and potential service values at the watershed scale*

For each watershed, compute the following indicators of the runoff retention service:

.. math:: Service.pop=Affected.Pop\sum_{watershed}0.001(P-Q_{p,i})\cdot pixel.area

.. math:: Service.built=Affected.Build\sum_{watershed}0.001(P-Q_{p,i})\cdot pixel.area

where pixel.area is the pixel area (:math:`m^2`), Service.pop is expressed in ppl.m3 and Service.built in $/m3

Limitations and simplifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 * Runoff production: the model uses a simple approach (SCS-Curve Number), which introduces high uncertainties. However, the ranking between different land uses is generally well captured by such an approach, i.e. that the effect of natural infrastructure will be qualitatively represented in the model outputs. Future work will aim to include a routing over the landscape: ideas include TOPMODEL (there is an R package), UFORE (used in iTree), CADDIES, etc

 * Valuation approaches: Currently, a simple approach to value flood risk retention is implemented, valuing flood risk as the avoided damage for built infrastructure. Alternative approaches (e.g. related to mortality, morbidity, or economic disruption) could be implemented.

Data needs
==========

 * Workspace (required): Folder where model outputs will be written. Make sure that there is ample disk space, and write permissions are correct.

 * Suffix (optional). Text string that will be appended to the end of output file names, as "_Suffix". Use a Suffix to differentiate model runs, for example by providing a short name for each scenario. If a Suffix is not provided, or changed between model runs, the tool will overwrite previous results.

 * Land Cover Map (required). Raster of land use/land cover (LULC) for each pixel, where each unique integer represents a different land use/land cover class. All values in this raster MUST have corresponding entries in the Land Cover Biophysical Table. The model will use the resolution of this layer to resample all outputs. The resolution should be small enough to capture the effect of green areas in the landscape, although LULC categories can comprise a mix of vegetated and non-vegetated covers (e.g. "residential", which may have 30% canopy cover, and have biophysical table parameters that change accordingly)

 * Biophysical Table (required). A .csv (Comma Separated Value) table containing model information corresponding to each of the land use classes in the Land Cover Map. All LULC classes in the Land Cover raster MUST have corresponding values in this table. Each row is a land use/land cover class and columns must be named and defined as follows:

    * lucode: and use/land cover class code. LULC codes must match the 'value' column in the Land Cover Map raster and must be integer or floating point values, in consecutive order, and unique.

    * Curve number (CN) values for each LULC type and each hydrologic soil group. Column names should be: CN_A, CN_B, CN_C, CN_D, which the letter suffix corresponding to the hydrologic soil group

 * Areas of interest: shapefile delineating areas of interest, which should be hydrologic units: watersheds or sewersheds.

 * Flood-prone areas (optional): raster of known (or predicted) occurrence of flooding, i.e. where the runoff retention service upstream will be critical

 * Population (optional): raster of number of population (in number of people, or number of people in specific subgroups)

 * Built infrastructure (optional): shapefile with built infrastructure footprints. The attribute table must contain a column 'Type', with integers referencing the building type (e.g. 1=residential, 2=office, etc.)

 * Potential damage loss table (optional): Table with columns "Type" and "Damage" with values of built infrastructure type (see above) and potential damage loss (in $/m2)

Interpreting outputs
====================

The following is a short description of each of the outputs from the urban flood risk mitigation model. Final results are found within the user defined Workspace specified for this model run. "Suffix" in the following file names refers to the optional user-defined Suffix input to the model.

 * Parameter log: Each time the model is run, a text (.txt) file will be created in the Workspace. The file will list the parameter values and output messages for that run and will be named according to the service, the date and time. When contacting NatCap about errors in a model run, please include the parameter log.

 * R.tif: raster with runoff retention values (no unit, relative to precipitation volume)

 * R_m3.tif: raster with runoff retention values (in m3)

 * cn_raster.tif: raster with CN values

 * q_p.tif: raster with runoff values (mm)

 * s_max.tif: raster with S_max values

 * flood_risk_service.shp: shapefile with results in the attribute table:

    * rnf_rt_idx: average of runoff retention values per watershed

    * rnf_rt_m3: sum of runoff retention volumes, in m3, per watershed

    * aff_bld: potential damage to built infrastructure in $, per watershed

    * serv_bld: spatial indicator of the importance of the runoff retention service (product of potential damage to built infrastructure by runoff retention)

Appendix: Data sources and guidance for parameter selection
===========================================================

The following table summarizes possible data sources for inputs specific to the urban flood risk mitigation model. Additional information on common InVEST inputs (e.g. LULC, evapotranspiration) can be found in the annual water yield model documentation.

Table 1
^^^^^^^
.. csv-table::
  :file: urban_flood_mitigation_appendix.csv
  :header-rows: 1
  :name: Table 1

Table 2
^^^^^^^
.. csv-table::
  :file: urban_flood_mitigation_soil_types.csv
  :header-rows: 1
  :name: Table 2
