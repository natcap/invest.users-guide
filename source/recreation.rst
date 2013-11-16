.. _recreation:

.. |openfold| image:: ./shared_images/openfolder.png
              :alt: open
	      :align: middle 
         
.. |addbutt| image:: ./shared_images/addbutt.png
             :alt: add
	     :align: middle 
	     :height: 15px

.. |okbutt| image:: ./shared_images/okbutt.png
            :alt: OK
	    :align: middle 

.. |adddata| image:: ./shared_images/adddata.png
             :alt: add
	     :align: middle 

***********************
Recreation Model (Beta)
***********************

This model is a beta release and has minimal documentation at the moment.

Summary
=======


.. note:: IP addresses are recorded with each run for usage statistics.

Introduction
============


The model
=========



Limitations and Simplifications
===============================

The model does not presuppose that any predictor variable has an effect on visitation.  Instead, the tool estimates the magnitude of each predictor's effect based on its spatial correspondence with current visitation in the area of interest.  The values of photo-person-days per cells are taken as a proxy-measure of visitation and are regressed against the values of the predictor variables across all cells.  In subsequent model-runs, the tool employs the beta values computed in the initial model-run to predict visitation, given a spatial configuration of the predictors, under future scenarios.  This step requires the assumption that people's responses to attributes that serve as predictors in the model will not change over time.  In other words, in the future, people will continue to be drawn to or repelled by the attributes as they are currently.


.. _rec-data-needs: 

Data Needs
==========

The model uses an interface to input all required and optional data, as outlined in this section. It outputs a vector grid and optionally processed predictors. The grid is always produced. To compute the initial grid the user has the option of selecting any or all of the predictors in :ref:`table-99` and supplying any of their own predictors.

To run the model, two steps are required:

#.	Run the Initial tool
#.	Run the Scenario tool

The Initial tool usually takes the longest amount of time to run (this varies greatly depending on spatial resolution and extent). The most informative attribute of the output grid is usdmav_pr, the estimated user days percentage. Users should review it before running the second model to ensure that there has not been an unexpected value. The Scenario tool usually takes the shortest amount of time to run (this has similar dependence as the Initial tool, but is largely dependent on the scenario data). The outputs of the Scenario tool are more useful in most analyses; outputs of the Initial tool serve mostly as inputs to the Scenario tool.

The following outlines the options presented to the user via the two interfaces, and the content and format of the required and optional input data used by the model. More information on how to fill the input interface or on how to obtain data is provided in :ref:`rec-appendix-a`.

.. note:: The data size is limited to 20MB zipped.

.. note:: Predictor file names are limited to US-ASCII and cannot contain accent marks.

.. _rec-Initial:

Initial Tool
------------

#. **Workspace (required).** The user is required to specify a workspace folder path.  The model will create a file named results-YYYY-MM-DD--HH_MM_SS.zip in the workspace, where YYYY-MM-DD--HH_MM_SS represents the year, month, day, hour, minute, and seconds respectively. Please note that users DO NOT have to run this model every time they run the Scenario model::

     Name: Path to a workspace folder.  Avoid spaces. 
     Sample path: \InVEST\Recreation\

#. **Area of Interest (projected , required).** This input provides the model with a geographic shape of the area of interest in which the grid will be located. It must be projected (see supported projections) and have an associated linear unit. The extent of the area of interest is used to create the grid and only cells that fall within the area of interest are included::

     Name: File can be named anything, but no spaces in the name
     File type: polygon shapefile (.shp)

#. **Grid type (required).** This input provides the model with the shape of the grid cells. Rectangular grids contain squares oriented parallel to the coordinate system of the area of interest. Hexagonal grids contain hexagons oriented with a long diagonal parallel to the horizontal component of the coordinate system.

#. **Cell size (projection units, required).** This input provides the model with the size of grid cells in the same linear unit as the projection.

#. **Comments (optional).** This input provides the model with text comments to include in the output.

#. **Data Directory (optional).** The user can optionally specify a data folder that contains additional geographic data to use as predictors. The data can be in a geographic or projecteed coordinate system, but it must be known and specified in the projection file (*.prj). Additionally, the geographic data can be classified if an optional classification table (*.csv) is specified. See predictor folders for more information::

     Name: Path to a data directory.  Avoid spaces. 
     Sample path: \InVEST\Recreation\data\BC\pred

#. **Download Data (optional).** The user can optionally have the processed predictors, including the user supplied predictors, returned with the model results.

#. **2010 Population (optional).** Oak Ridge National Laboratory LandScan (2010) population data.  Please note that due to the license agreement for this data it cannot be include in downloaded data.

#. **OSM Points (optional).** Open Street Map (2012) point features categorized into cultural, industrial, natural, structural, and miscellaneous features. See OSM categorization.

#. **OSM Lines (optional).** Open Street Map (2012) line features categorized into cultural, industrial, natural, structural, and miscellaneous features. See OSM categorization.

#. **OSM Polygons (optional).** Open Street Map (2012) polygon features categorized into cultural, industrial, natural, structural, and miscellaneous features. See OSM categorization.

#. **Protected Areas (optional).** UNEP-WCMC World Data Base on Protected Areas (2012) polygon features.

#. **LULC (optional).** ESA GlobCover (2008) land use and land cover data. See LULC categorization.

#. **Mangroves (optional).** UNEP-WCMC Ocean Data Viewer Mangroves (1997).

#. **Coral Reefs (optional).** UNEP-WCMC Ocean Data Viewer Coral Reefs (2010).

#. **Seagrasses (optional).** UNEP-WCMC Ocean Data Viewer Seagrasses (2005).

.. note:: The cell size is in the same units as the area of interest. For example, an area of interest in a UTM projection has units of meters, and therefore the units of the cell size will be meters.

.. note:: The download data option will provide the preprocessed data used in the model run and may be useful for the creation of scenarios.


.. _rec-Scenario:

Scenario Tool
-------------

#. **Workspace (required).** The user is required to specify a workspace folder path.  The model will create a file named results-YYYY-MM-DD--HH_MM_SS.zip in the workspace, where YYYY-MM-DD--HH_MM_SS represents the year, month, day, hour, minute, and second respectively. Please note that users DO NOT have to run this model every time they run the Scenario model::

     Name: Path to a workspace folder.  Avoid spaces. 
     Sample path: \InVEST\Recreation\

#. **init.json (required).** The initial tool configuration file.

#. **Data Directory (required).** The user must specify a data folder that contains the modified predictors for the scenario. The data can be in a geographic or projecteed coordinate system, but it must be known and specified in the projection file (*.prj). Additionally, the geographic data can be classified if an optional classification table (*.csv) is specified. See predictor folders for more information::

     Name: Path to a data directory.  Avoid spaces. 
     Sample path: \InVEST\Recreation\data\BC\pred

#. **Comments (optional).** This input provides the model with text comments to include in the output.

.. note:: It is only necessary to provide the changed shapefiles for scenario runs, unchanged data can be read from the initial model run.

Interpreting results
====================

Model outputs
-------------

The follwing is a short decription of each of the outputs from the Scenario model. Each of these output files is saved in the results.zip file located within the workspace directory that was specified:

results.zip
^^^^^^^^^^^
+ aoi_params.csv
    + This text file contains the regression model parameters.
+ comments.txt
    + This text file contains the optional user comments.
+ grid.shp
    + This polygon feature layer contains the grid with all distributable predictor values and regression parameters.
+ init.json
    + This text file contains the initial tool parameters.
+ download/
    + This folder contains the feature layers for processed predictors.

.. _rec-appendix-a:

Appendix A
==========

Predictor Folders
-----------------

Predictor folders should *only* contain predictors for the model run. *Only* shapefiles are supported. The following prefixes are reserved for internal use and cannnot be used:

 * borders
 * duplicates
 * photos
 * planet_osm
 * predictor
 * prj
 * searches
 * spatial
 * srid
 * tmp
 * users
 * wkt

Categorization Tables
---------------------

Categorization Tables are tab delmited text files with three required columns: the field name, the field value, and the category name. The table should contain a row header and the category names cannot contain spaces or symbols.

OSM Categorization
------------------

The following is the table used for OSM categorization. It is not exhaustive, but almost all other features fall into an other cateogry. For more information on how OSM features are tagged see http://wiki.openstreetmap.org/wiki/Map_Features


.. csv-table::
  :file: recreation_images/osm.csv
  :header-rows: 1
  :name: OSM Categorization

LULC Classification
-------------------

The following is the reclassification table used for the global land use and land cover.

.. csv-table::
  :file: recreation_images/lulc.csv
  :header-rows: 1
  :name: LULC Classification

.. _table-99:

Standard Predictors
-------------------

.. csv-table::
  :file: recreation_images/recdata.csv
  :header-rows: 1

References
==========
