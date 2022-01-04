.. _getting-started:

***************
Getting Started
***************

.. _installing-on-win:

Installing InVEST and sample data on your Windows computer
==========================================================

Download the InVEST installer from https://naturalcapitalproject.stanford.edu/software/invest. The executable will be called "InVEST_<version>_Setup.exe". Double-click on this .exe to run the installer.

After clicking through the first screen and agreeing to the Licence Agreement, the Choose Components screen will appear. The installer will always install the InVEST Tools and HTML and PDF versions of the InVEST User's Guide. Optionally, sample datasets may also be installed, and by default they are all selected. Note that these datasets are downloaded over the internet, and some are very large (particularly the Marine Datasets), so they make take a long time to install. If you do not wish to install all or some of the sample datasets, uncheck the corresponding box(es).

Next, choose the folder where the InVEST toolsets and sample data will be installed. The installer shows how much space is available on the selected drive. Click Install to begin the installation.

Once installed, the InVEST install folder will contain the following:

+ A **documentation** folder, containing the InVEST User Guide in HTML format.
+ An **invest-3-x64** folder, containing the compiled Python code that makes up the InVEST toolset.
+ **InVEST_<version>_Documentation.pdf**, the InVEST User Guide in PDF format.
+ **Uninstall_<version>.exe**, which will uninstall InVEST.
+ **HISTORY.rst**, lists of all of the updates included in each new version.
+ If you chose to also install sample data, they will be located in the folder **sample_data**, with a sub-folder for each model's data.

Additionally, shortcuts for all InVEST standalone applications will be added to your Windows start menu under *All Programs -> InVEST |version|*

Advanced Installation
---------------------

The InVEST windows installer has a number of installation options for several use cases, including silent installation and the use of local sample data.  To view the available options, download the installer, open a CMD prompt to the directory that contains the downloaded installer and type:


.. code-block:: text

    .\InVEST_<version>_x64_Setup.exe /?


.. _installing-on-mac:

Installing InVEST on your Mac
=============================================

.. note::
    In Mac OS 10.13 "High Sierra", InVEST 3.4.0 or later is required.

    In Mac OS 11 "Big Sur", InVEST 3.9.0 or later is required.

    Numerical results of the Mac binaries may differ slightly (usually within 1e-4) from the results of the Windows binaries.  For this reason, we consider InVEST binaries "unstable", but they should still provide reasonable results.  As always, if something does not seem to be working, please let us know on the forums: https://community.naturalcapitalproject.org/

Download the InVEST disk image file from https://naturalcapitalproject.stanford.edu/software/invest.  The file will be called "InVEST-<version>.dmg".  This contains a copy of the InVEST executable. Note that, as of the 3.9.0 release, the user's guide
and HISTORY.rst file are no longer included in the Mac distribution; please access these resources online.

To install:

  1. Right-click on your downloaded ``InVEST-<version>.dmg``, and in the context menu, select *Open*.
  2. In the dialog that pops up, click *Open* once again.
  3. The disk image will open and instruct you to drag the InVEST app to your Applications folder. This step is essential for InVEST to work correctly.
  4. Go to your Applications folder and open the InVEST app from there.
  5. The first time you open the InVEST app, you'll need to do the following:
       1. Right-click on ``InVEST``, and in the context menu, select *Open*.
       2. In the dialog that pops up, click *Open* once again.
  6. In the launcher dialog, select the model you'd like to run and click *Launch*.

Unlike the Windows installer, the Mac distribution does not include sample data or the user's guide.  These can be found online at https://naturalcapitalproject.stanford.edu/software/invest.


Quick Start InVEST Tutorial
===========================

This high-level tutorial gives you an idea of the main activities involved with doing an ecosystem service analysis using InVEST. It is not an exhaustive step-by-step technical resource, but does provide steps, tips, and a general idea of the time requirement needed for running one InVEST model. While time requirements vary widely project to project, a general estimate is provided for each step: *Low* = generally requires less than one day; *Medium* = less than one week; *High* = a week or more.

1. **Install InVEST**
	- Download InVEST, and install as detailed in the :ref:`installing-on-win` or :ref:`installing-on-mac` sections of this chapter.
	- It is recommended to also install the sample data that is offered by the InVEST installer.
	- Time required to install InVEST: Low
2. **Read the User Guide chapter for each model of interest**
	- For each model, the User Guide contains background, equations, data requirements, descriptions of results and recommendations for global data sources and methods.
	- This is the first place to go with questions about models and data requirements.
	- Time required to read a model chapter: Low
3. **Examine the model’s sample data**
	- Sample data is provided for all models, available for installation during the InVEST install, or downloadable separately.
	- Look at the spatial data using GIS software, and tabular data using a spreadsheet or text editor.
	- Use these data for getting a feel for the inputs and outputs and running the model.
	- Use them as an example of how to format your own data.
	- See the :ref:`using-sample-data` section of this chapter for more information.
	- Time required to try out a model with sample data: Low
4. **Create your own data for the baseline case**
	- Gather the spatial and non-spatial model inputs required by the model. 
	- Process the collected data for your area of interest, so that each input meets InVEST requirements. 
	- Most of this processing will be done using GIS software.
	- Many models also require an extensive literature search for certain parameters.
	- Consult the model's User Guide chapter and sample data for requirements and examples of what the datasets should look like.
	- Also consult the :ref:`formatting-data` section of this chapter for general tips.
	- The amount of processing will vary greatly, depending on the particular model input and format of the original source.  
	- It’s best to look for more local sources of data, but if these aren’t available, coarser, global layers and values are generally available. The User Guide Appendix for each model provides pointers to some global data sources.
	- Time required to create data for one model: High.
5. **Create future scenarios**
	- Analyzing scenarios is optional, but commonly done.
	- Scenarios are often based on altering land use/land cover, habitat, or land management maps to reflect the impacts of a proposed intervention, or climate change. 
	- Creating scenarios may be very time-consuming if, for example, a stakeholder process is used, or climate modeling is required.
	- Time required to create scenarios: Medium to High.
6. **Run the model**
	- Use the InVEST user interface or command-line scripting to run the model using your data.
	- See the :ref:`running-models` section of this chapter for more information.
	- Time required: Low to Medium, depending on size and complexity of the input data, and which model is being run. More time is required for high-resolution data and/or large areas of interest.
7. **Examine model results**
	- Critically examine the results using GIS software - do the patterns and values make sense? 
	- Unexplained patterns or abnormally high or low values might indicate problems with the input data.
	- Time requirement: Low to Medium.
8. **Calibrate the model**
	- Optional, not necessarily required for a high-level screening analysis and/or if field data is not available for validation. 
	- However, it is important to do calibration if valuation is being done using the model results.
	- Collect and process observed data corresponding to the InVEST model output of interest. For example, sediment load from a monitoring station in a reservoir intake.
	- Adjust model inputs to produce an agreement between modeled results and observed data.
	- Calibration may be accompanied by a sensitivity analysis, to determine which parameters have the greatest effect on results. The most sensitive parameters are good choices for calibration adjustment.
	- Time required: Medium to High.
9. **Incorporate beneficiaries**
	- Link model results to people, or other type of beneficiary. This is where it becomes an ecosystem *service*.
	- Collect and pre-process data on the location of people, infrastructure or other beneficiary of interest.
	- Combine InVEST model results with beneficiary data, generally done using GIS software.
	- Time requirement: Medium.
10. **Valuation**
	- Valuation of ecosystem services, whether monetary or non-monetary, is generally complex and context-specific.
	- Gather economic data related to the service and beneficiary you're analyzing.
	- Calibrate your model results before using them for valuation.
	- Time required: Medium to High.
11. **Communicate results**
	- Once you have InVEST results, you'll be creating maps, tables, graphs, etc, depending on what is needed to communicate your results to your audience.
	- Post-processing may also be done with the results. For example, you may show a map of protected areas overlaid on an InVEST result map. Or combine multiple ecosystem service maps into a "hotspot" map of greatest combined service provision. Or aggregate results within an area of interest.
	- Remember to choose your colors and symbols to be easy to read by a wide audience, intuitive to interpret, and such that they accurately represent the results.
	- Time required: Low to Medium, depending on the complexity of project needs.
	

GIS Skills
==========

**Intermediate geographic information system (GIS) skills are required for many InVEST analysis steps, especially when creating model inputs, and working with model outputs.**

This User Guide assumes that you have the required GIS skills, it does not generally provide instruction related to viewing or processing data using GIS software. You may use any geospatial software that you are comfortable with, QGIS and ArcGIS being the most common. There are many classes and tutorials available for learning GIS skills and software, and we recommend getting comfortable with these concepts and tools before beginning to work with InVEST.

Here are some examples of the types of GIS tasks that are typically part of an InVEST analysis. This is not a comprehensive list:

+ View and navigate raster, vector and tabular data 
 
+ Symbolize raster and vector data
 
+ Reproject data layers to a common coordinate system
 
+ Clip data layers to an area of interest
 
+ Convert vector to raster and raster to vector
 
+ Create new point, line or polygon layers
 
+ Edit vector attribute tables
 
+ Perform a variety of raster math
 
+ Reclassify raster values
 
+ Resample rasters

Also see the :ref:`working-with-the-DEM` section of this chapter, which does provide some detail regarding GIS processing of digital elevation model (DEM) data for use in the SDR, NDR, Seasonal Water Yield, Scenic Quality and Coastal Vulnerability models. 


Standalone InVEST Tools
=======================

All of the InVEST models run on an entirely open-source platform, where historically the toolset was a collection of ArcGIS scripts. The new interface does not require ArcGIS and the results can be explored with any GIS tool including `ArcGIS <https://www.esri.com/en-us/home>`_, `QGIS <https://qgis.org/en/site/>`_, and others. As of InVEST 2.3.0, the toolset has had standalone versions of the models available from the Windows start menu after installation, under *All Programs -> InVEST |version|*.  Standalone versions are currently available for all models. The ArcGIS versions of InVEST models are no longer supported.


Older InVEST Versions
=====================
Older versions of InVEST can be found at http://data.naturalcapitalproject.org/invest-releases/deprecated_models.html. Note that many models were deprecated due to critical unsolved science issues, and we strongly encourage you to use the latest version of InVEST.

.. _using-sample-data:

Using sample data
=================

InVEST comes with sample data as a guide for formatting your data, and starting to understand how the models work. For instance, in preparation for analysis of your data, you may wish to test the models by changing input values in the sample data to see how the output responds. For most models it is important that their sample data is only used for testing and example, do not use the spatial data or table values for your own analysis, because their source and accuracy is not documented. Some of the marine models come with global datasets that may be used for your own application - please see the individual User Guide chapters for these models for more information.

Sample data are found in separate sub-folders within the InVEST install folder. For example, the sample datasets for the Pollination model are found in \\{InVEST install folder}\\sample_data\\pollination\\, and those for the Carbon model in \\{InVEST install folder}\\sample_data\\carbon\\. For testing the models, you may make a Workspace folder called "output" within the sample data folders for saving model results. Once you are working with your own data, you will need to create a workspace and input data folders to hold your own input and results.  You will also need to redirect the tool to access your data and workspace.

If running on Windows, sample data may be installed at the same time that InVEST is being installed, or datasets may be downloaded individually from `the InVEST website <https://naturalcapitalproject.stanford.edu/software/invest>`_.

.. _formatting-data:

Formatting your data
====================

Before running InVEST, it is necessary to format your data. Although subsequent chapters of this guide describe how to prepare input data for each model, there are several formatting guidelines common to all models:

+ Data file names should not have spaces (e.g., a raster file should be named 'landuse.tif' rather than 'land use.tif').

+ For raster data, TIFFs are preferred for ease of use, but you may also use IMG or ESRI GRID.

+ If using ESRI GRID format rasters, their dataset names cannot be longer than 13 characters and the first character cannot be a number. TIFF and IMG rasters do not have the file name length limitation. When using ESRI GRID as input to the model interface, use the file "hdr.adf".

+ Spatial data must be in a projected coordinate system (such at UTM), not a geographic coordinate system (such as WGS84), and all input data for a given model run must be in the same projected coordinate system. If your data is not projected, InVEST will give errors or incorrect results. (There are exceptions to this, such as Coastal Vulnerability - see the model's User Guide chapter for specific requirements.)

+ While the InVEST 3.0 models are now very memory-efficient, the amount of time that it takes to run the models is still affected by the size of the input datasets. If the area of interest is large and/or uses rasters with small cell size, this will increase both the memory usage and time that it takes to run the model. If they are too large, a memory error will occur. If this happens, try reducing the size of your area of interest, or using coarser-resolution input data.

+ Similarly, the amount of disk space that is used by the model is in proportion to the resolution of the input data. If the area of interest is large and/or uses rasters with small cell size, this will increase the amount of disk space required to store intermediate and final model results. If not enough disk space is available, the model will return an error.

+ Running the models with the input data files open in another program can cause errors. Ensure that the data files are not in use by another program to prevent data access issues.

+ Regional and Language options: Some language settings cause errors while running the models.  For example settings which use comma (,) for decimals instead of period (.) cause errors in the models.  To solve this change the computer's regional settings to English.

+ As the models are run, it may be necessary to change values in the input tables. This is usually done with a spreadsheet program like Excel or text editor like Notepad++. Input tables are required to be in CSV (comma-separated value) format, where the values are separated by commas, not semicolons or any other character. If working in Excel, you cannot see the separator, so double-check in Notepad or another text editor.  When saving the CSV file, be sure to save the file using one of the following encodings: ASCII, UTF-8 or Signed UTF-8.  Using any other encoding (such as Latin-1) will result in incorrect text rendering in output files and could cause models to fail with an error.

+ Some models require specific naming guidelines for data files (e.g., Habitat Quality model) and field (column) names, which are defined in the User Guide chapter for each model. Follow these carefully to ensure your dataset is valid, or the model will give an error.

+ Remember to use the sample datasets as a guide to format your data.

.. _running-models:

Running the models
==================

You are ready to run an InVEST model when you have prepared your data according to the instructions in the relevant model chapter and have installed the latest version of InVEST.

To begin:

+ Review your input data. View spatial data in a GIS, make sure that the values look correct, there are no areas of missing data where it should be filled in, that all layers are in the same projected coordinate system, etc. View table data in a spreadsheet or text editor, make sure that the values look correct, the column names are correct, and that it is saved in CSV format.

+ Launch the model you wish to run (e.g., Carbon), and add your input data to each field in the user interface. You may either drag and drop layers into the field, or click the File icon to the right of each field to navigate to your data.

+ Inputs for which the entered path leads to a non-existent file or a file that is incorrectly formatted will be marked with a red "X" to the left of the name of the input. If you click the red X, it will give an idea of what is wrong with the data. The model will not run if there are any red Xs.

+ Note that each tool has a place to enter a Suffix, which is a string that will be added to the output filenames as *<filename>_Suffix*. Adding a unique suffix prevents overwriting files produced in previous iterations. This is particularly useful if you are running multiple scenarios, so each file name can indicate the name of the scenario.

+ When all required fields are filled in, and there are no red Xs, click the **Run** button on the interface.

+ Processing time will vary depending on the script and the resolution and extent of your input datasets.  Every model will open a window showing the progress of the script. Be sure to scan the output window for useful messages and errors. This progress information will also be written to a file in the Workspace called *<model name>-log-<timestamp>.txt*. If you need to contact NatCap for assistance with errors, always send this log file, it will help with debugging. Also see the :ref:`support-and-error-reporting` section of this chapter for more information.

+ Results from the model can be found in the **Workspace** folder. Main outputs are generally in the top level of the Workspace. There is also an 'intermediate' folder which contains some of the additional files generated while doing the calculations. While it's not usually necessary to look at the intermediate results, it is sometimes useful when you are debugging a problem, or trying to better understand how the model works. Reading the model chapter and looking at the corresponding intermediate files can be a good way to understand and critique your results. Each model chapter in this User Guide provides a description of these output files.

After your script completes successfully, you can view the spatial results by adding them from the Workspace to your GIS. It is important to look closely and critically at the results. Do the values make sense? Do the patterns make sense? Do you understand why some places have higher values and others lower? How are your input layers and parameters driving the results?

.. _support-and-error-reporting:

Support and Error Reporting
===========================

If you encounter any issues when running the models, or have questions about their theory, data, or application that the User Guide does not cover, please visit the user support forum at https://community.naturalcapitalproject.org/. First, please use the **Search** feature to see if a similar question has already been asked. Many times, your question or problem has already been answered. If you don't find existing posts related to your question or issue, or they don't solve your issue, you can log in and create a new post.

If you are reporting an error when running a model, please include the following information in the forum post:

+ InVEST model you're asking about

+ InVEST version you're using

+ What you have already tried to solve the issue, and hasn't worked

+ The entire log file produced by the model, located in the output Workspace folder - *<model name>-log-<timestamp>.txt*

Training
--------

Several training workshops on InVEST may be offered annually, subject to funding and demand.  Information on these trainings will be announced on the support page and can be found at the `Natural Capital Project website <https://naturalcapitalproject.stanford.edu/>`_. This site is also a good source of general information on InVEST, related publications and use cases and other activities of the Natural Capital Project.

A free Massive Open Online Course (MOOC) is available `In English <https://www.edx.org/course/introduction-to-the-natural-capital-project-approach/>`_ and `in Spanish <https://www.edx.org/course/una-introduccion-al-enfoque-de-capital-natural-ver-2/>`_, which provides:

- An introduction to the Natural Capital Project's methods

- Introduction to InVEST

- SDR, Coastal Vulnerability and Urban Cooling models presented in some detail

- Overviews of other ecosystem service analysis topics including scenarios, beneficiaries and data sources

- Several case studies.



There is also a `YouTube playlist <https://www.youtube.com/playlist?list=PLSFk2iLV3UfNqRZGwfcgyoZZZqZDnj2V7/>`_ with video training tutorials, including:

- Summer Series: Introduction to InVEST (Brief introduction to InVEST, SDR, Coastal Vulnerability and communicating results)

- Summer Series: Freshwater quality (NDR and SDR are presented in more detail)

- Summer Series: Urban InVEST (Urban Cooling is presented in more detail)

- Introduction to: Rangeland Production

- Introduction to: Habitat Quality

- Introduction to: Carbon Storage

- Introduction to: Seasonal Water Yield

- Introduction to: Urban Flood Risk Mitigation

.. _working-with-the-DEM:

Working with the DEM
====================

For the freshwater models SDR, NDR and Seasonal Water Yield, having a well-prepared digital elevation model (DEM) is critical. It must have no missing data (holes of NoData values), and should correctly represent the surface water flow patterns over the area of interest in order to get accurate results.

Use the highest quality, finest resolution DEM that is appropriate for your application. This will reduce the chances of there being sinks and missing data, and will more accurately represent the terrain's surface water flow, providing the amount of detail that is required for making informed decisions at your scale of interest. 

While each DEM source is different, as is the extent of each study area and requirements of each project, there are several general steps that we usually need to do to prepare a DEM to run in an InVEST hydrology model. Each of these steps is outlined below. Included is information on using built-in functions from ArcGIS and QGIS. There are other options for DEM processing as well, including ArcHydro, ArcSWAT, AGWA, and BASINS, which are not covered here.  This is only intended to be a brief overview of the issues and methods involved in DEM preparation, not a GIS tutorial.

+ **Mosaic raw, tiled DEM data**

  If you have downloaded DEM data for your area that is in multiple, adjacent tiles, they will need to first be mosaicked together to create a single DEM file.  In ArcToolbox, use Data Management -> Raster -> Mosaic to New Raster.  Look closely at the output raster to make sure that the values are correct along the edges where the tiles were joined.  If they are not, try different values for the Mosaic Method parameter to the Mosaic to New Raster tool.

  In QGIS, you can use the Raster -> Miscellaneous -> Merge function to combine the tiles.


+ **Reprojecting DEMs**

  When reprojecting a DEM in either ArcGIS (Project Raster tool) or QGIS (Warp tool), it is important to select BILINEAR or CUBIC for the "Resampling Technique" in ArcGIS or "Resampling method" in QGIS. Selecting NEAREST (or Near in QGIS) will produce a DEM with an incorrect grid pattern across the area of interest, which might only be obvious when zoomed-in or after Flow Direction has been run. This will create a bad stream network and flow pattern and lead to bad model results.

+ **Check for missing data**

  After getting (and possibly mosaicking) the DEM, make sure that there is no missing data, represented by NoData cells within the area of interest.  If there are NoData cells, they must be assigned values.

  For small holes, one way to do this is to use the  ArcGIS Focal Mean function within Raster Calculator (or Conditional -> CON).  For example, in ArcGIS 10.x::

	Con(IsNull("theDEM"),FocalStatistics("theDEM",NbrRectangle(3,3),"MEAN"),"theDEM")

  Interpolation can also be used, and can work better for larger holes. Convert the DEM to points using Conversion Tools -> From Raster -> Raster to Point, interpolate using Spatial Analyst's Interpolation tools, then use CON to assign interpolated values to the original DEM::

    Con(isnull([theDEM]), [interpolated_grid], [theDEM])

  In QGIS, try the Fill Nodata tool, or the GRASS r.neighbors tool. r.neighbors provides different statistics types, including Mean.

+ **Identify sinks in the DEM and fill them**

  From the ESRI help on "How Sink works": "A sink is a cell or set of spatially connected cells whose flow direction cannot be assigned one of the eight valid values in a flow direction raster. This can occur when all neighboring cells are higher than the processing cell or when two cells flow into each other, creating a two-cell loop."

  Sinks are usually caused by errors in the DEM, and they can produce an incorrect flow direction raster.  This can lead to several problems with hydrology processing, including creating a discontinuous stream network. Filling the sinks assigns new values to the anomalous processing cells, such that they are better aligned with their neighbors. But this process may create new sinks, so an iterative process may be required.

  We have found that the QGIS Wang and Liu Fill tool does a good job of filling sinks, and is recommended. You can also use ArcGIS by using the Hydrology -> Fill tool. Multiple runs of Fill may be needed.


+ **Verify the stream network**

  The stream network generated by the model from the DEM should closely match the streams on a known correct stream map. Several of the InVEST hydrology models and the supporting InVEST tool RouteDEM output a stream network (usually called *stream.tif*.) These tools create streams by first generating a Flow Accumulation raster, then applying the user input 'threshold flow accumulation' (TFA) value to select pixels that should be part of the stream network. For example, if a TFA value of 1000 is given, this says that 1000 pixels must drain into a particular pixel before it's considered part of a stream. This is the equivalent of saying that streams are defined by having a flow accumulation value >= 1000.

  Use these *stream.tif* outputs to evaluate how well the modelled streams match reality, and adjust the threshold flow accumulation accordingly. Larger values of TFA will produce coarser stream networks with fewer tributaries, smaller values of TFA will produce more tributaries. There is no one "correct" value for TFA, it will be different for each area of interest and DEM. A good value to start with for testing is 1000. When comparing *stream.tif* with a real-world stream map, check that you have the appropriate granularity of tributaries, and make sure that the *stream.tif* streams are continuous, not chopped in disconnected segments or individual pixels. If the modeled streams are discontinuous, try doing another Fill on the DEM, and make sure that you used BILINEAR or CUBIC resampling method for reprojecting. If a DEM does not make continuous streams, then we advise trying another source of elevation data, there are several globally-available sources, and they each perform differently in different places in the world. 

  To create flow accumulation and stream maps without needing to run a whole hydrology model, you can use the InVEST tool `RouteDEM <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-userguide/latest/routedem.html/>`_, which is specifically for processing the DEM. See the `RouteDEM chapter of the User Guide <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-userguide/latest/routedem.html/>`_ for more information.


+ **Create watersheds**

  It is recommended to create watersheds from the DEM that you will be using in the analysis. If a watershed map is obtained from elsewhere, the boundaries of the watershed(s) might not line up correctly with the hydrology created from the DEM, leading to incorrect aggregated results.

  There are a variety of tools that can create watersheds, including the ArcGIS Watershed tool and QGIS Watershed basins or r.basins.fill. InVEST also provides a tool called `DelineateIt <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-userguide/latest/delineateit.html/>`_, which works well, is simple to use, and is recommended. It has the advantage of being able to create watersheds that overlap, such as when there are several dams along the same river. See the `DelineateIt section of the User Guide <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-userguide/latest/delineateit.html/>`_ for more information.

  After watersheds are generated, verify that they represent the catchments correctly and that each watershed is assigned a unique integer ID in the field "ws_id" (or "subws_id", depending on the model - see the Data Needs section of the hydrology model you're using to find out what's required.)
  
  + **Clip the DEM to your study area**

  We generally recommend that the DEM be clipped to an area that is slightly larger than your area of interest. This is to ensure that the hydrology around the edge of the watershed is captured. This is particularly important if the DEM is of coarse resolution, as clipping to the area of interest will lead to large areas of missing data around the edge. To do this, create a buffer around your area of interest (or watershed) polygon, and clip the DEM to that buffered polygon. Make sure that the buffer is at least the width of one DEM pixel.
