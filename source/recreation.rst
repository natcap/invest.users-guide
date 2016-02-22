.. primer
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

**********************************
Visitation: Recreation and Tourism
**********************************

Summary
=======

Recreation and tourism are important components of many national and local economies and they contribute in innumerable ways to quality of life, sense of place, social connection, physical wellbeing, learning, and other intangibles.  To quantify the value of natural environments, the InVEST recreation model predicts the spread of person-days of recreation, based on the locations of natural habitats and other features that factor into people's decisions about where to recreate.  The tool estimates the contribution of each attribute to visitation rate in a simple linear regression.  In the absence of empirical data on visitation, we parameterize the model using a proxy for visitation: geotagged photographs posted to the website flickr.  Using photo-user-day estimates, the model predicts how future changes to natural features will alter visitation rates.  The tool outputs maps showing current patterns of recreational use and maps of future patterns of use under alternate scenarios.

Introduction
============

Recreation and tourism are important components of many national and local economies and they contribute in innumerable ways to quality of life, sense of place, social connection, physical wellbeing, learning, and other intangibles.  A key reason for studying patterns of recreation or tourism is the economic significance of this industry.  The total contribution of travel and tourism to the world's gross domestic product (GDP) in 2011 was approximately $6 B USD (9% of GDP), with expected growth to $10 B USD by 2022 (World Travel and Tourism Council 2012).  Of course, economic impacts are only one way of measuring the importance of recreation and tourism.  These activities are critical contributors to diverse aspects of human wellbeing (Russell et al. 2013).  For example, outdoor recreation is a spiritual experience for many people (eg Trainor and Norgaard 1999), and social interactions in nature contribute to building a sense of place (e.g. Willox et al. 2012).

A major and growing portion of recreation is "nature-based", involving interactions with or appreciation of the natural environment (Balmford et al. 2009).  For these types of activities, characteristics of the environment influence people's decisions about where, when, and how to recreate.  SCUBA divers, for example, select destinations based on the water clarity, water temperature, and diversity of marine life (Williams and Polunin 2000, Uyarra et al. 2009).  Bird-watchers are drawn to the best places to see target species (Naidoo and Adamowicz 2005), which inevitably are places where natural systems support populations of desirable birds (Puhakka et al. 2011).  Some recreation depends on environmental attributes such as species richness (Loureiro et al. 2012), the diversity of habitats (Neuvonen et al. 2010, Loureiro et al. 2012), precipitation (Loomis and Richardson 2006), and temperature (Richardson and Loomis 2005), as well as to other attributes such as infrastructure and cultural attractions (Mills and Westover 1987, Hill and Courtney 2006).

.. primerend
.. _rec-the-model:

The Model
=========

The purpose of the InVEST recreation model is to predict the spread of person-days of recreation and tourism, based on the locations of natural habitats, accessibility, and built features such as roads that factor into people's decisions about where to recreate (Adamowicz et al. 2011).  The tool outputs maps showing current patterns of recreational use and, optionally, maps of future use under alternative scenarios.

.. _rec-how-it-works:

How it Works
------------

The model displays rate of visitation across landscapes (grid cells) or in discrete areas (polygons) and optionally builds a regression model to estimate the contribution of attributes of the landscape to the visitation rate, using a simple linear regression:

.. math:: y_i = \beta_{0} + \beta_1 x_{i1} + ... + \beta_{p} x_{ip} \text{ for } i = 1 ... n,

where :math:`x_{ip}` is the coverage of each attribute in each cell or polygon (hereafter called 'cell'), :math:`i`, within an Area of Interest (AOI) containing :math:`n` cells.  In the absence of empirical data on visitation for :math:`y_i`, we parameterize the model using a crowdsourced measure of visitation: geotagged photographs posted to the website flickr (see :ref:`rec-photos` section for more information).  Stated again, the InVEST recreation model predicts the spread of person-days of recreation in space.  It does this using attributes of places, such as natural features (eg parks), built features (eg roads), and human uses (eg industrial activities), among others.  

The tool begins by log-transforming all :math:`y_i` values, by taking the natural log of average photo-user-days per cell + 1.  Then, a simple linear regression is performed to estimate the effect of each attribute on log-transformed visitation rates across all grid cells within the study region.  These estimates (the :math:`\beta_{p}` values) can be used for an additional scenario, to predict how future changes to the landscape will alter visitation rate.  The model uses ordinary least squares regression, performed by the lm function for R (R Core Team 2013).

.. _rec-photos:

Photo User Days
--------------------

Since fine-scale data on numbers of visitors is often only collected at a few specific locations in any study region, we assume that current visitation can be approximated by the total number of annual person-days of photographs uploaded to the photo-sharing website `flickr <http://www.flickr.com>`_.  Many of the photographs in flickr have been assigned to a specific latitude/longitude.  Using this location, along with the photographer's user name and date that the image was taken, the InVEST tool computes the total annual days that a user took at least one photograph within each cell, then returns to users the average annual number of photo-user-days (PUD_AVG) from 2005-2014 (or a user-defined range within those years).  PUD_AVG is :math:`y_i` in the equation above. We have observed that the number of recreators who visit a location annually is related to the number of photographs taken in the same area and uploaded to the flickr database at 836 visitor attractions worldwide (Wood et al. 2013).  The density of photographs varies spatially, and this has ramifications for the cell-size that can be chosen for analysis (see :ref:`rec-initial-tool`: Cell size). PUD calculations are computed on a remote server on an extensive global dataset curated and maintained by The Natural Capital Project.


Predictor Variables
-------------------

In the regression equation above, photo-user-days are the :math:`y_i` variable and all the :math:`x` variables on the right side are predictor variables. These are features in the area of interest that are likely to influence the visitation patterns across space.

We find that it often helps to consider at least one predictor variable from several main categories: natural capital (eg habitats, lakes), built capital (eg roads, hotels), industrial activities, and access or cost (eg distance to major airport).  Often, single variables representing each of these categories can explain the majority of variation in photo-user-days.  This tool allows users to provide predictor variables in GIS formats and to process those layers in a variety of ways (described in the :ref:`rec-data-needs` section). 

Limitations and Simplifications
-------------------------------

The model does not presuppose that any predictor variable has an effect on visitation.  Instead, the tool estimates the magnitude of each predictor's effect based on its spatial correspondence with current visitation in the area of interest.  The values of photo-person-days per cells are taken as a proxy-measure of visitation and are regressed against the values of the predictor variables across all cells.  In subsequent model-runs, the tool employs the beta values computed in the initial model-run to predict visitation, given a spatial configuration of the predictors, under future scenarios.  This step requires the assumption that people's responses to attributes that serve as predictors in the model will not change over time.  In other words, in the future, people will continue to be drawn to or repelled by the attributes as they are currently.


.. _rec-data-needs: 

Data Needs
==========

The following outlines the options presented to the user via the two interfaces, and the content and format of the required and optional input data used by the model. More information on how to format and obtain data is provided in :ref:`rec-appendix-a`.

.. _rec-initial-tool:

Initial Tool
------------

#. **Workspace (required).** Users must specify a path to the workspace folder where the tool will create a file of results::

     Name: Path to a workspace folder.  Avoid spaces.
     Sample path: \InVEST\Recreation\

#. **Area of Interest (required).** This input provides the model with a geographic shape of the area of interest (AOI).  The AOI must be projected (see :ref:`rec-supported-projections`) and have an associated linear unit.  The extent of the AOI is used to create the grid (if checked, see below) and only cells that fall within the AOI are included.  The total area of the AOI must be smaller than 800,000 square km::

     Name: File can be named anything, but no spaces in the name
     File type: polygon shapefile (.shp)

#. **Grid type (required).** This input specifies the shape of the grid cells.  Rectangular grids contain squares oriented parallel to the coordinate system of the AOI.  Hexagonal grids contain hexagons oriented with a long diagonal parallel to the horizontal component of the coordinate system.

#. **Cell size (required).** This input specifies the size of grid cells.  The cell size is **in the same linear units as the AOI**.  For example, if the AOI is in a UTM projection with units of meters, and cell size parameter will also be in meters.  The minimum allowable grid cell size is three square km and the AOI must contain at least five cells.  

   The appropriate size and number of cells depends on several factors, including the goals of the study and the density of photographs, which varies from region to region.  In order for the model to compute the effects of predictor variables (as described in the :ref:`rec-how-it-works` section), users must select a sufficiently large cell size, such that the majority of cells contain photographs.  We recommend that users begin by running the model with cells ranging between 100-1000 square km.  Then, iteratively assess the model outputs (grid.shp and regression_summary.pdf, described in :ref:`rec-interpreting-results`) and re-run the model to determine an appropriate cell size.  

#. **Comments (optional).** This input provides the model with text comments to include with the outputs.

#. **Data Directory (optional).** Users can optionally specify a data folder containing additional geographic data to use as predictors (for :math:`x_{ip}` values described in :ref:`rec-how-it-works`). The data can be in a geographic or projected coordinate system, but it must be known and specified in the projection file (.prj). Additionally, the geographic data can be classified if an optional classification table (.csv) is specified (see :ref:`rec-categorization-tables` for more information)::

     Name: Path to a data directory.  Avoid spaces. 
     Sample path: \InVEST\Recreation\data\BC\pred

#. **Download Data (optional).** User can choose have the processed predictors, including the user supplied predictors, returned with the model results.

#. **Global Default Data (optional).** The tool provides several global spatial datasets which users can optionally include as predictor variables for their AOI.  Further information on these datasets is available in the :ref:`rec-default-predictors` Section of Appendix A.

   + **2010 Population (optional).** Oak Ridge National Laboratory LandScan (2010) population data.  Please note that due to the license agreement, these data cannot be included in downloaded data.

   + **OSM Points (optional).** Open Street Map (2012) point features categorized into cultural, industrial, natural, structural, and miscellaneous features. See :ref:`rec-osm-categorization`.

   + **OSM Lines (optional).** Open Street Map (2012) line features categorized into cultural, industrial, natural, structural, and miscellaneous features. See :ref:`rec-osm-categorization`.

   + **OSM Polygons (optional).** Open Street Map (2012) polygon features categorized into cultural, industrial, natural, structural, and miscellaneous features. See :ref:`rec-osm-categorization`.

   + **Protected Areas (optional).** UNEP-WCMC World Data Base on Protected Areas (2012) polygon features.

   + **LULC (optional).** ESA GlobCover (2008) land use and land cover data. See LULC categorization.

   + **Mangroves (optional).** UNEP-WCMC Ocean Data Viewer Mangroves (1997).

   + **Coral Reefs (optional).** UNEP-WCMC Ocean Data Viewer Coral Reefs (2010).

   + **Seagrasses (optional).** UNEP-WCMC Ocean Data Viewer Seagrasses (2005).

.. _rec-scenario-tool:

Scenario Tool
-------------

#. **Workspace (required).** Users must specify a path to the workspace folder.  The model will create a file of results here::

     Name: Path to a workspace folder.  Avoid spaces. 
     Sample path: \InVEST\Recreation\

#. **init.json (required).** The configuration file created by the Initial Tool and saved in the results folder in the initial workspace.

#. **Data Directory (required).** Users must specify a data folder that contains the modified predictors for the scenario.  Uploaded shapefiles must have identical names as those uploaded for the first run using the Initial Tool.  It is only necessary to provide the changed shapefiles for scenario runs, unchanged data can be read from the initial model run.  The data can be in a geographic or projected coordinate system, but it must be known and specified in the projection file (.prj).  Additionally, the geographic data can be classified if an optional classification table (.csv) is specified (see the :ref:`rec-categorization-tables` Section for more information)::

     Name: Path to a data directory.  Avoid spaces. 
     Sample path: \InVEST\Recreation\data\BC\pred

#. **Comments (optional).** This input provides the model with text comments to include with the outputs.


.. _rec-running-model:

Running the Model
=================

.. warning:: The recreation model requires a connection to the internet.

The model uses an interface to input all required and optional data (see :ref:`rec-data-needs`), which are then sent to a server managed by the Natural Capital Project in California, where computations are performed.  Consequently, this model requires a connection to the internet.  The server outputs a vector polygon shapefile and .csv tables of results (described in :ref:`rec-interpreting-results`).  The InVEST recreation model consists of two individual tools, which must be run consecutively:

#. The Initial tool, which computes photo-user-days (:math:`y_i`), coverages of predictors (:math:`x_{ip}`), and effects of predictors (:math:`\beta_p`).
#. The Scenario tool, which uses effects per predictor (:math:`\beta_p`) to estimate future visitation rates.

The time required to run the Initial Tool varies depending on the extent of the AOI, the number grid cells, and the number and resolution of predictor layers.  The Scenario Tool takes less time to run.

Please note, the server performing the analysis also records the IP address of each user.

.. primer
.. _rec-interpreting-results:

Interpreting Results
====================

Model Outputs
-------------

The follwing is a short decription of each of the outputs from the Scenario model. Each of these output files is saved in the outputs saved into the workspace directory in a file named *results-YYYY-MM-DD--HH_MM_SS.zip* where *YYYY-MM-DD--HH_MM_SS* represents the year, month, day, hour, minute, and seconds, respectively.

+ aoi_params.csv

  + This text file contains the parameters estimated by the linear regression (see :ref:`rec-how-it-works`), including the :math:`\beta_p` and :math:`p` values.  Each predictor variable must be present in cells within the AOI in order to estimate their effects.  Any predictor variables that cannot be estimated remain blank in the aoi_params.csv table.

+ comments.txt

  + This text file contains the optional user comments.

+ grid.shp

  + This polygon feature layer contains the gridded AOI with the number of photo-user-days and coverage of each predictor variable per cell.

  + USDYAV is the average photo-user-days per year (using all photos from 2005-2012).  This corresponds to the average *PUD* described in Wood et al. (2013).

  + USDYAV_PR is simply the proportion of total USDYAV per cell.

  + USDYAV_EST is the average photo-user-days estimated by the linear regression equation. 

+ init.json

  + This configuration file contains the initial tool parameters.  It should not be edited.

+ download/ (optional)

  + This folder contains the feature layers for processed predictors.

.. primerend
.. _rec-appendix-a:

Appendix A
==========

.. _rec-supported-projections:

Supported Projections
---------------------

The supported projections are a subset of the European Petroleum Survey Group (EPSG) projections, which are commonly used and supported across a wide range of industries and platforms. Specifically we support the EPSG projections that use linear units (meters, feet, etc.) also known as projected coordinate systems, which include the following:

* Universal Transverse Mercator projections
* Albers projections
* Lambert projections

and many more.

For more information on EPSG projections see http://spatialreference.org/ref/epsg/.

Depending on the source of the data there can be minor variations in how a projection is stored, which may raise a projection error. If you have a projection that uses linear units and it is not working with the recreation model, please start a discussion on the user forum at http://ncp-yamato.stanford.edu/natcapforums/.

.. _rec-predictors:

Predictor Variables
-------------------

.. _rec-upload-directory:

Upload Directory
^^^^^^^^^^^^^^^^

Predictor folders should contain *predictors for the model run only*.  Files must be ESRI shapefiles format.  All files must be under 20MB zipped and file names are limited to US-ASCII and cannot contain accent marks.  Finally, the following file names are reserved for internal use and cannot be used: *borders*, *duplicates*, *photos*, *planet_osm*, *predictor*, *prj*, *searches*, *spatial*, *srid*, *tmp*, *users*, *wkt*.

.. _rec-categorization-tables:

Categorization Tables
^^^^^^^^^^^^^^^^^^^^^

Categorization Tables are tab delmited text files with three required columns: the field name, the field value, and the category name. The table should contain a row header and the category names cannot contain spaces or symbols.

.. _rec-osm-categorization:

OSM Categorization
^^^^^^^^^^^^^^^^^^

A supplementary table provides the `categorization scheme used for all OSM features <http://users-guide.invest-natcap.googlecode.com/hg/source/recreation_images/osm.csv>`_.  It is not exhaustive, but almost all other features fall into another cateogry.  For more information on how OSM features are tagged see the `OSM wiki <http://wiki.openstreetmap.org/wiki/Map_Features>`_.

LULC Classification
^^^^^^^^^^^^^^^^^^^

The following is the reclassification table used for the global land use and land cover.

.. csv-table::
  :file: recreation_images/lulc.csv
  :header-rows: 1
  :name: LULC Classification

.. _rec-default-predictors:

Default Predictors
^^^^^^^^^^^^^^^^^^

The default global predictor data provided by the Initial and Scenario Tools are from the following sources.

.. csv-table::
  :file: recreation_images/recdata.csv
  :header-rows: 1


.. _rec-references:

References
==========

Adamowicz, WL, R Naidoo, E Nelson, S Polasky, J Zhang. 2011. Nature-based tourism and recreation. In: Kareiva P, G Daily, T Ricketts, H Tallis, S Polasky (eds) Natural Capital: Theory and Practice of Mapping Ecosystem Services. Oxford University Press, New York.

Balmford, A, J Beresford, J Green, R Naidoo, M Walpole, A Manica. 2009. A global perspective on trends in nature-based tourism. PLoS Biology 7: e1000144.

Hill, GW,  PR Courtney. 2006. Demand analysis projections for recreational visits to countryside woodlands in Great Britain. Forestry 79: 18-200.

Loomis, JB, RB Richardson. 2006. An external validity test of intended behavior: comparing revealed preference and intended visitation in response to climate change. Journal of Environmental Planning and Management 49: 621-630.

Loureiro, ML, F Macagno, PA Nunes, R Tol. 2012. Assessing the impact of biodiversity on tourism flows: an econometric model for tourist behaviour with implications for conservation policy. Journal of Environmental Economics and Policy 1: 174-194.

Mills, AS, TN Westover. 1987. Structural differentiation: a determinant of park popularity. Annals of Tourism Research 14: 486-498.

Naidoo, R, WL Adamowicz. 2005. Biodiversity and nature-based tourism at forest reserves in Uganda. Environment and Development Economics 10: 159-178.

Neuvonen, M, E Pouta, J Puustinen, T Sievänen. 2010. Visits to national parks: effects of park characteristics and spatial demand. Journal for Nature Conservation 18: 224-229.

Puhakka, L, M Salo, IE Sääksjärvi. 2011. Bird diversity, birdwatching tourism and conservation in Peru: a geographic analysis. PLoS One 6: e26786.

Richardson, R, JB Loomis. 2005. Climate change and recreation benefits in an alpine national park. Journal of Leisure Research 37: 307-320.

R Core Team. 2013. R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria.

Russell, R, AD Guerry, P Balvanera, RK Gould, X Basurto, KM Chan, S Klain, J Levine, J Tam. 2013. Humans and nature: how knowing and experiencing nature affect well-being. Annual Review of Environment and Resources 38: in press.

Trainor, SF, RB Norgaard. 1999. Recreation fees in the context of wilderness values. Journal of Park and Recreation Administration 17: 100-115.

Uyarra, MC, AR Watkinson, IM Côté. 2009. Managing dive tourism for the sustainable use of coral reefs: validating diver perceptions of attractive site features. Environmental Management 43: 1-16.

Williams, ID, NV Polunin. 2000. Differences between protected and unprotected reefs of the western Caribbean in attributes preferred by dive tourists. Environmental Conservation 27: 382-391.

Willox, AC, SL Harper, JD Ford, K Landman, K Houle, V Edge. 2012. "From this place and of this place:" climate change, sense of place, and health in Nunatsiavut, Canada. Social Science and Medicine 75: 538-547.

Wood, SA, AD Guerry, JM Silver, M Lacayo. 2013. `Using social media to quantify nature-based tourism and recreation <http://www.nature.com/srep/2013/131017/srep02976/full/srep02976.html>`_. Scientific Reports 3: 2976.

World Travel and Tourism Council. 2012. `Travel and Tourism: Economic Impact <http://www.wttc.org/site_media/uploads/downloads/world2012.pdf>`_.
