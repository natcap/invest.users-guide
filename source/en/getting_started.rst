.. _getting-started:

***************
Getting Started
***************

Quick Start InVEST Tutorial
===========================

This high-level tutorial gives you an idea of the main activities involved with doing an ecosystem service analysis using InVEST. It is not an exhaustive step-by-step technical resource, but does provide steps, tips, and a general idea of the time requirement needed for running one InVEST model. While time requirements vary widely project to project, a general estimate is provided for each step: *Low* = generally requires less than one day; *Medium* = less than one week; *High* = a week or more.

1. **Install InVEST Workbench**
	- Download InVEST Workbench, and install as detailed in the :ref:`installing-on-win` or :ref:`installing-on-mac` sections of this chapter.
	- It is recommended to also install the sample data. In the InVEST Workbench, sample data can be downloaded through the Settings window, by clicking on the gear icon in the upper right corner of the user interface. Links to sample data are also available through `the InVEST web page <https://naturalcapitalproject.stanford.edu/software/invest>`_. See the :ref:`using-sample-data` section of this chapter for more information.
	- Time required to install InVEST: Low
2. **Read the User Guide chapter for each model of interest**
	- For each model, the User Guide contains background, equations, data requirements, descriptions of results and recommendations for global data sources and methods.
	- This is the first place to go with questions about models and data requirements.
	- Time required to read a model chapter: Low
3. **Examine the model’s sample data**
	- Sample data is provided for all models, available for installation through the Workbench Settings, or downloadable through `the InVEST web page <https://naturalcapitalproject.stanford.edu/software/invest>`_.
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
	- Scenarios are often based on altering land use/land cover, habitat, or land management practices to reflect the impacts of a proposed intervention, or climate change.
	- Creating scenarios may be very time-consuming if, for example, a stakeholder process is used, or climate modeling is required.
	- Time required to create scenarios: Medium to High.
6. **Run the model**
	- Use the InVEST Workbench user interface or command-line scripting to run the model using your data.
	- Allocate sufficicient time for this step, in case you need to troubleshoot errors.
	- See the :ref:`running-models` section of this chapter for more information.
	- Time required: Low to Medium, depending on size and complexity of the input data, and which model is being run. More time is required for high-resolution data and/or large areas of interest.
7. **Examine model results**
	- Critically examine the results using GIS software - do the patterns and values make sense? Why?
	- Unexplained patterns or abnormally high or low values might indicate problems with the input data.
	- Allocate sufficient time for this step, in case the results do not look correct and you need to troubleshoot. 
	- Time requirement: Low to Medium.
8. **Calibrate the model**
	- Optional, not necessarily required for a high-level screening analysis and/or if field data is not available for validation.
	- However, it is important to do calibration if valuation is being done using the model results.
	- Collect and process observed data corresponding to the InVEST model output of interest. For example, sediment load from a monitoring station in a reservoir intake.
	- Adjust model inputs to produce an agreement between modeled results and observed data.
	- Calibration may be accompanied by a sensitivity analysis, to determine which parameters have the greatest effect on results. The most sensitive parameters are good choices for calibration adjustment.
	- See the :ref:`calibration_freshwater` section of this Guide for more information.
	- Time required: Medium to High.
9. **Incorporate beneficiaries**
	- Link model results to people, or other type of beneficiary. This is where it becomes an ecosystem *service*.
	- Collect and pre-process data on the location of people, infrastructure or other beneficiary of interest.
	- Combine InVEST model results with beneficiary data, generally done using GIS software.
	- Time requirement: Medium.
10. **Valuation**
	- Valuation of ecosystem services, whether monetary or non-monetary, is generally complex and context-specific. It is also optional.
	- Gather economic data related to the service and beneficiary you're analyzing.
	- Calibrate your model results before using them for valuation.
	- Time required: Medium to High.
11. **Communicate results**
	- Once you have InVEST results, you'll be creating maps, tables, graphs, etc, depending on what is needed to communicate your results to your audience.
	- Post-processing may also be done with the results. For example, you may show a map of protected areas overlaid on an InVEST result map. Or combine multiple ecosystem service maps into a "hotspot" map of greatest combined service provision. Or aggregate results within an area of interest.
	- Remember to choose your colors and symbols to be easy to read by a wide audience, intuitive to interpret, and such that they accurately represent the results.
	- Time required: Low to Medium, depending on the complexity of project needs.

.. _installing-on-win:

Installing InVEST Workbench on your Windows computer
=====================================================

Download the InVEST Workbench installer from https://naturalcapitalproject.stanford.edu/software/invest. The executable will be called "InVEST_<version>_workbench_win32_x64.exe". Double-click on this .exe to run the installer.

The first screen asks you to confirm the Licence Agreement, click **I Agree** to continue.

The Installation Options screen will appear. You may choose to install InVEST only for yourself, or for all users. Click **Next**.

Next, choose the folder where Workbench will be installed. Click **Install**.

There are a few things that may be of particular interest in the Workbench installation folder:

+ A **resources/documentation** folder, containing the InVEST User Guide in HTML format in English, Spanish and Chinese.
+ A **resources/invest** folder, containing the compiled Python code that makes up the InVEST toolset.
+ **InVEST <version> Workbench.exe**, which is the main executable used to launch Workbench
+ **Uninstall InVEST <version> Workbench.exe**, which will uninstall Workbench.

Additionally, a shortcut will be added to your Windows start menu under *All Programs -> InVEST <version> Workbench*

Sample data is also available for all models. To install these, launch Workbench, and go to **Settings** (the gear icon in the upper right corner) **-> Download Sample Data**.


Advanced Installation
---------------------

The InVEST windows installer has a number of installation options for several use cases, including silent installation. Options include:

* ``/S``: Silent installation
* ``/D=<directory>``: Installation directory
* ``/allusers``: Install for all users
* ``/currentuser``: Install for the current user only
* ``/NCRC``: Disable the CRC check


.. code-block:: text

    .\InVEST_<version>_x64_Setup.exe /?


.. _installing-on-mac:

Installing InVEST Workbench on your Mac
========================================

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

Sample data is also available for all models. To install these, launch Workbench, and go to **Settings -> Download Sample Data**.

Unlike the Windows installer, the Mac distribution does not include the user's guide.  This can be found online at https://naturalcapitalproject.stanford.edu/software/invest.


Workbench interface
===================

.. figure:: ./getting_started/Workbench_main_screen_316.png

When you launch Workbench, the first screen that appears lists all of the InVEST models. Click on one of the models to open the input interface for that model. If you have previously run any models, each model run will appear in a list on the right hand side of the screen. Click on one of the runs to open a window that contains the inputs and logging messages from that model run.

On any Workbench screen, clicking on the "Home screen" InVEST link will take you to the first/main Workbench screen. Also on every screen, in the upper right corner is an icon with three bars, providing the following functionality:

+ **Manage Plugins**: Add or remove third-party plugins for Workbench.
+ **Download Sample Data**: Select the model(s) that you would like to download data for, then click the "**Download**" Button. See the :ref:`using-sample-data` section of this chapter for more information.
+ **Conigure Metadata**: Add your (optional) contact and licensing information to the metadata YML files that are created with each InVEST model output.
+ **View Changelog**: See what's new in this version of Workbench.
+ **Settings**: Choose the user interface language (English, Spanish, Chinese); change parameters related to logging and Taskgraph.

When you click on a particular model, a tab opens and shows the inputs specific to that model.

.. figure:: ./getting_started/Workbench_Carbon_input_screen_316.png

See the :ref:`running-models` section of this chapter for more information about adding data to the interface.

This screen also provides the ability to save parameters (and optionally data) to a file, through the "**Save as...**" link. Three options are available:

+ **Parameters only**: Saves a JSON file that includes the paths to your input data, but it does not save the data itself. You can use the "**Load parameters from file**" option to bring this file into InVEST, or drag and drop the JSON file into the model interface, to restore your parameters. 

+ **Parameters and data**: Saves both parameters and data in a compressed archive (.tgz). This archive contains the same JSON file produced by the "**Parameters only**" option, plus the data. You can use the "**Load parameters from file**" option to bring this file into InVEST, or drag and drop the .tgz file into the model interface, to restore your parameters. This option is useful for copying all of the necessary data for a model run to a different location. For example, you can send the archive to a colleague to reproduce your model run. If you post to the Community Forum asking for help with a problem, you may be asked to provide your input data, and this is the preferred way to package up your input data and parameters.

+ **Python script**: Saves your parameters in a python script. This includes the paths to your input data, but not the data itself. Running the python script will run the model with your parameters. Use this as a starting point for batch scripts.

If you have a saved parameter datastack (.tgz file = parameters + data) to bring into Workbench, you can either drag and drop it into the interface, or use the "**Load parameters from file**" option and choose the .tgz. After dropping the .tgz into the interface, or selecting it in the "**Load parameters from file**" option, a window will appear called "**Choose location to extract archive**". Where it says "**File name**", type the name of a new *folder*, which is where the contents of the .tgz will be extracted to. Note that it does not currently work to select a folder that has already been created, you must create a new one only through the "**File name**" entry. 

The "**User's Guide**" link takes you to the User's Guide chapter for that model. The "**Frequently Asked Questions**" link takes you to the Natural Capital Project's Community Forum (https://community.naturalcapitalproject.org/), showing the posts that are related to that model.

Once you have filled in all of the required input data, click "**Run**" to run the model. A logging screen will appear.

.. figure:: ./getting_started/Workbench_log_screen_316.png

There will be a lot of logging messages, and usually you do not need to be concerned about them, unless the model fails to run. If the model does fail, look at the logging messages for an error that might help explain what went wrong. If the model runs successfully, you can click on "**Open Workspace**" to view the results of the model run. To return to the model input screen, click "**Setup**".

.. _using-sample-data:

Using sample data
=================

InVEST comes with sample data as a guide for formatting your data, and starting to understand how the models work. Before starting your own analysis, we highly recommend downloading the sample data for the model(s) that you're interested in, looking at the inputs in a GIS, running the model using the sample data, and examining the outputs in a GIS.

In the InVEST Workbench, sample data can be downloaded by clicking on the three-bar icon in the upper right corner of the user interface, and choosing **Download Sample Data**

.. figure:: ./getting_started/Workbench_settings_316.png

Links to sample data are also available through `the InVEST web page <https://naturalcapitalproject.stanford.edu/software/invest>`_.

Each model's sample data folder contains a .json file, which you can use to automatically fill in most of the model inputs. To use this, either drag and drop the .json file into the model's input screen in Workbench, or use the "Load parameters from file" interface to navigate to the .json file.

For most models it is important that their sample data is only used for testing and example, do not use the spatial data or table values for your own analysis, because their source and accuracy is not documented. Some of the marine models (like Coastal Vulnerability) come with global datasets that may be used for your own application - please see the individual User Guide chapters for these models for more information.

For testing the models, you may make a Workspace folder called "output" within the sample data folders for saving model results, or use whatever data organization structure works for you. Once you are working with your own data, you will need to create a workspace and input data folders to hold your own input and results.  You will also need to redirect the tool to access your data and workspace.


.. _formatting-data:

Formatting your data
====================

Before running InVEST, it is necessary to format your data. Although subsequent chapters of this guide describe how to prepare input data for each model, there are several formatting guidelines common to all models:

+ Data file names should not have spaces (e.g., a raster file should be named 'landuse.tif' rather than 'land use.tif').

+ For raster data, TIFFs are preferred for ease of use, but you may also use IMG or ESRI GRID.

+ If using ESRI GRID format rasters, their dataset names cannot be longer than 13 characters and the first character cannot be a number. TIFF and IMG rasters do not have the file name length limitation. When using ESRI GRID as input to the model interface, use the file "hdr.adf".

+ For most InVEST models, spatial data must be in a projected coordinate system (such at UTM, with distance units of meters), *not* a geographic coordinate system (such as WGS84, with distance units of degrees), and all input data for a given model run must be in the same projected coordinate system. If your data is not projected, InVEST will give errors or incorrect results. (There are exceptions to this, such as the Coastal Vulnerability model - see the model's User Guide chapter for specific requirements.)

+ Every raster that is used as input to InVEST models must have a numeric data value assigned to the raster's *NoData* value. This *NoData* value must not be considered valid model data. For example, the Land use/land cover raster might have valid land use codes of 1 through 30, so you could choose a *NoData* value of 9999. The value "nan" IS NOT a valid NoData value, and will produce an error when running models. You can check the *NoData* value by looking at the raster's Properties in a GIS.

+ While the InVEST 3.0 models are now very memory-efficient, the amount of time that it takes to run the models is still affected by the size of the input datasets. If the area of interest is large and/or uses rasters with small cell size, this will increase both the memory usage and time that it takes to run the model. If they are too large, a memory error will occur. If this happens, try reducing the size of your area of interest, or using coarser-resolution input data.

+ Similarly, the amount of disk space that is used by the model is in proportion to the resolution of the input data. If the area of interest is large and/or uses rasters with small cell size, this will increase the amount of disk space required to store intermediate and final model results. If not enough disk space is available, the model will return an error.

+ Running the models with the input data files open in another program can cause errors. Ensure that the data files are not in use by another program to prevent data access issues.

+ It is recommended to store model inputs and outputs on a local hard drive, not in cloud storage. Running the models with input data files accessed online (not on a local drive) can cause errors.

+ Regional and Language options: Some language settings cause errors while running the models.  For example settings which use comma (,) for decimals instead of period (.) cause errors in the models.  To solve this change the computer's regional settings to English.

+ As the models are run, it may be necessary to change values in the input tables. This is usually done with a spreadsheet program like Excel or text editor like Notepad++. Input tables are required to be in CSV format. If working in Excel, be sure to save as CSV.  When saving the CSV file, be sure to save the file using one of the following encodings: ASCII, UTF-8 or Signed UTF-8.  Using any other encoding (such as Latin-1) will result in incorrect text rendering in output files and could cause models to fail with an error.

+ Some models require specific naming guidelines for data files (e.g., Habitat Quality model) and field (column) names, which are defined in the User Guide chapter for each model. Follow these carefully to ensure your dataset is valid, or the model will give an error.

+ Remember to *use the sample datasets as a guide to format your data*.

.. _running-models:

Running the models
==================

You are ready to run an InVEST model when you have prepared your data according to the instructions in the relevant model chapter and have installed the latest version of InVEST.

To begin:

+ Review your input data. View spatial data in a GIS, make sure that the values look correct, there are no areas of missing data where it should be filled in, that all layers are in the same projected coordinate system, etc. View table data in a spreadsheet or text editor, make sure that the values look correct, the column names are correct, and that it is saved in CSV format.

+ Launch the model you wish to run (e.g., Carbon), and add your input data to each field in the user interface. You may either drag and drop layers into the field, or click the File icon to the right of each field to navigate to your data.

.. figure:: ./getting_started/Workbench_Carbon_input_screen.png

+ Inputs for which the entered path leads to a non-existent file or a file that is incorrectly formatted will be marked with a red "X" to the right of the name of the input and the input box will be outlined in red. Beneath the input will be a brief description of what's wrong with the input. For example, "Input is required but has no value" means that this input is required, but you have not yet filled it in with valid information. The model will not run if there are any red Xs.

+ Note that each tool has a place to enter a Suffix, which is a string that will be added to the output filenames as *<filename>_Suffix*. Adding a unique suffix prevents overwriting files produced in previous iterations. This is particularly useful if you are running multiple scenarios, so each file name can indicate the name of the scenario.

+ When all required fields are filled in, and there are no red Xs, click the **Run** button on the interface.

+ Processing time will vary depending on the script and the resolution and extent of your input datasets.  Every model will open a window showing the progress of the script. Be sure to scan the output window for useful messages and errors. This progress information will also be written to a file in the Workspace called *InVEST-natcap.invest.<model name>-log-<timestamp>.txt*. If you need to contact NatCap for assistance with errors, always send this log file, it will help with debugging. Also see the :ref:`support-and-error-reporting` section of this chapter for more information.

+ Results from the model can be found in the **Workspace** folder. Main outputs are generally in the top level of the Workspace. There is also an 'intermediate' folder which contains some of the additional files generated while doing the calculations. While it's not usually necessary to look at the intermediate results, it is sometimes useful when you are debugging a problem, or trying to better understand how the model works. Reading the model chapter and looking at the corresponding intermediate files can be a good way to understand and critique your results. Each model chapter in this User Guide provides a description of these output files.

After your script completes successfully, you can view the spatial results by adding them from the Workspace to your GIS. It is important to look closely and critically at the results. Do the values make sense? Do the patterns make sense? Do you understand why some places have higher values and others lower? How are your input layers and parameters driving the results? If you are concerned about your results, and want to ask about it on the user forum, please review these questions first. Very often, unexpectedly high or low values, or areas of missing data, can be easily explained by looking at units, values, or missing data in your input layers.

Metadata
========
Results of InVEST models also include **metadata** documents that describe each dataset in the output workspace. These are the *".yml"*, or YAML, sidecar files in the output workspace. Each metadata file has the same filename as the dataset it describes, plus the *".yml"* extension. Open a YAML file in a text editor to read the metadata, or even add to it. The metadata includes much of the same information as in the *Interpreting Results* section of the model's User Guide chapter. This includes descriptions of fields in tables, of the bands in a raster, and other useful information. If you plan on sharing your InVEST results with others, we strongly encourage you to share the metadata documents along with your results.

Some properties of the metadata are configureable from the *Settings* dialog of the Workbench. You may save information about the data author (you) and data license information. These details are included in all metadata documents created by InVEST and by GeoMetaMaker. This information is optional, it never leaves your computer unless you share your data and metadata, and you may modify it in the Workbench anytime.

GeoMetaMaker is a Python library that facilitates metadata creation for geospatial data pipelines.
https://github.com/natcap/geometamaker

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

.. _support-and-error-reporting:

Support and Error Reporting
===========================

If you encounter any issues when running the models, or have questions about their theory, data, or application that the User Guide does not cover, please visit the user support forum at https://community.naturalcapitalproject.org/. *First, please use the Search feature to see if a similar question has already been asked. Many times, your question or problem has already been answered.* This is especially true for error messages - you can Search for a few key words in the error message and will often find posts that help you fix the error.

If you don't find existing posts related to your question or issue, or they don't solve your issue, you can log in and create a new post.

If you are reporting an error when running a model, please include the following information in the forum post:

+ InVEST model you're asking about

+ InVEST version you're using

+ What you have already tried to solve the issue, and hasn't worked

+ The entire log file produced by the model, located in the output Workspace folder - *InVEST-natcap.invest.<model name>-log-<timestamp>.txt*

Training
--------

Several training workshops on InVEST may be offered annually, subject to funding and demand.  Information on these trainings will be announced on the support page and can be found at the `Natural Capital Project website <https://naturalcapitalproject.stanford.edu/>`_. This site is also a good source of general information on InVEST, related publications and use cases and other activities of the Natural Capital Project.

A free Massive Open Online Course (MOOC) is available `In English <https://www.edx.org/course/introduction-to-the-natural-capital-project-approach/>`_ and `in Spanish <https://www.edx.org/course/una-introduccion-al-enfoque-de-capital-natural-ver-2/>`_, which provides:

- An introduction to the Natural Capital Project's methods

- Introduction to InVEST

- SDR, Coastal Vulnerability and Urban Cooling models presented in some detail (although they're all out of date now, with recent updates to these models).

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

We also have a `GIS for InVEST video series <https://naturalcapitalproject.stanford.edu/software/virtual-training/gis-invest>`_  which provides hands-on instruction in some of the GIS tasks needed for working with InVEST models. These are provided for both QGIS and ArcGIS.

Older InVEST Versions
=====================
Older versions of InVEST can be found at http://data.naturalcapitalproject.org/invest-releases/deprecated_models.html. Note that many models were deprecated due to critical unsolved science issues, and we strongly encourage you to use the latest version of InVEST.

.. _working-with-the-DEM:

Working with the DEM
====================

For the freshwater models SDR, NDR and Seasonal Water Yield, having a well-prepared digital elevation model (DEM) is critical. It must have no missing data (holes of NoData values), and should correctly represent the surface water flow patterns over the area of interest in order to get accurate results.

Use the highest quality, finest resolution DEM that is appropriate for your application. This will reduce the chances of there being sinks and missing data, and will more accurately represent the terrain's surface water flow, providing the amount of detail that is required for making informed decisions at your scale of interest.

While each DEM source is different, as is the extent of each study area and requirements of each project, there are several general steps that we usually need to do to prepare a DEM to run in an InVEST model. Each of these steps is outlined below, including information on using built-in functions from ArcGIS and QGIS. There are other options for DEM processing as well, including ArcHydro, ArcSWAT, AGWA, and BASINS, which are not covered here.  This is only intended to be a brief overview of the issues and methods involved in DEM preparation, not a GIS tutorial.

1. **Mosaic raw, tiled DEM data**

   If you have downloaded DEM data for your area that is in multiple, adjacent tiles, they will need to first be mosaicked together to create a single DEM raster.  In ArcToolbox, use Data Management Tools -> Raster -> Raster Dataset -> Mosaic to New Raster.  Look closely at the output raster to make sure that the values are correct along the edges where the tiles were joined.  If they are not, try different values for the Mosaic Method parameter to the Mosaic to New Raster tool.

   In QGIS, you can use the Raster -> Miscellaneous -> Merge function to combine the tiles.

2. **Reproject to your project's coordinate system**

   When reprojecting a DEM in either ArcGIS (Project Raster tool) or QGIS (Warp tool), it is important to select BILINEAR or CUBIC for the "Resampling Technique" in ArcGIS or "Resampling method" in QGIS. Selecting NEAREST (or Near in QGIS) will produce a DEM with an incorrect grid pattern across the area of interest, which might only be obvious when zoomed-in or after Flow Direction has been run. This will create a bad stream network and flow pattern and lead to bad model results.

3. **Check for missing data**

   Look closely at the DEM raster to make sure that there is no missing data, represented by NoData cells within the area of interest.  If there are NoData cells, they must be assigned values.

   For small holes, one way to do this is to use the  ArcGIS Focal Mean function within Raster Calculator (or Conditional -> CON).  For example, in ArcGIS 10.x::

	Con(IsNull("theDEM"),FocalStatistics("theDEM",NbrRectangle(3,3),"MEAN"),"theDEM")

   Interpolation can also be used, and can work better for larger holes. Convert the DEM to points using Conversion Tools -> From Raster -> Raster to Point, interpolate using Spatial Analyst's Interpolation tools, then use CON to assign interpolated values to the original DEM::

        Con(isnull([theDEM]), [interpolated_grid], [theDEM])

   In QGIS, try the Fill Nodata tool, or the GRASS r.neighbors tool. r.neighbors provides different statistics types, including Mean.

4. **Identify sinks in the DEM and fill them**

   This step is almost always required.

   From the ESRI help on "How Sink works": "A sink is a cell or set of spatially connected cells whose flow direction cannot be assigned one of the eight valid values in a flow direction raster. This can occur when all neighboring cells are higher than the processing cell or when two cells flow into each other, creating a two-cell loop."

   Sinks are usually caused by errors in the DEM, and they can produce an incorrect flow direction raster.  This can lead to several problems with hydrology processing, including creating a discontinuous stream network. Filling the sinks assigns new values to the anomalous processing cells, such that they are better aligned with their neighbors. But this process may create new sinks, so an iterative process may be required.

   We have found that the QGIS Wang and Liu Fill tool does a good job of filling sinks, and is recommended (even for ArcGIS users). You can also use ArcGIS by using the Hydrology -> Fill tool. Multiple runs of Fill may be needed.

5. **Verify the stream network**

   At this point, the DEM should be ready to test. The main thing to look for is how well streams are generated, so you'll need a real-world stream map for comparision, which can be geospatial or not, just as long as you can visually compare it.

   The stream network generated by the model from the DEM should closely match the streams on a known correct stream map. Several of the InVEST hydrology models and the supporting InVEST tool RouteDEM output a stream network (usually called *stream.tif*.) These tools create streams by first generating Flow Direction and Flow Accumulation rasters (which you should check as part of this step), then applying the user input 'threshold flow accumulation' (TFA) value to select pixels that should be part of the stream network. For example, if a TFA value of 1000 is given, then 1000 pixels must drain into a particular pixel before it's considered part of a stream. This is the equivalent of saying that streams are defined by having a flow accumulation value >= 1000.

   Use these *stream.tif* outputs to evaluate how well the modelled streams match reality, and adjust the threshold flow accumulation accordingly. Larger values of TFA will produce coarser stream networks with fewer tributaries, smaller values of TFA will produce more tributaries. There is no one "correct" value for TFA, it will be different for each area of interest and DEM. A good value to start with for testing is 1000. When comparing *stream.tif* with a real-world stream map, check that you have the appropriate granularity of tributaries, and make sure that the *stream.tif* streams are continuous, not chopped in disconnected segments or individual pixels. Be aware that modeled streams are rarely, if ever, exactly the same as reality, so you're not aiming for perfection but for getting them reasonably close. If the modeled streams are discontinuous, try doing another Fill on the DEM, and make sure that you used BILINEAR or CUBIC resampling method for reprojecting. If a DEM does not make continuous streams no matter what you try, then we advise trying another source of elevation data. There are several globally-available sources, and they each perform differently in different places in the world.

   To create flow accumulation and stream maps without needing to run a whole hydrology model, you can use the InVEST tool RouteDEM, which is specifically for processing the DEM. See the :ref:`RouteDEM page <routedem>` for more information.

6. **Create watersheds**

   It is recommended to create watersheds from the DEM that you will be using in the analysis. If a watershed vector layer is obtained from elsewhere, the boundaries of the watershed(s) might not line up correctly with the hydrology created from the DEM you're using for modeling, leading to incorrect aggregated results.

  There are a variety of tools that can create watersheds, including the ArcGIS Watershed tool and QGIS Watershed basins or r.basins.fill. InVEST also provides a tool called DelineateIt, which works well, is simple to use, and is recommended. It has the advantage of being able to create watersheds that overlap, such as when there are several dams along the same river. See the :ref:`DelineateIt page <delineateit>` for more information.

   After watersheds are generated, verify that they represent the catchments correctly and that each watershed is assigned a unique integer ID in the field "ws_id" (or "subws_id", depending on the model - see the Data Needs section of the hydrology model you're using to find out what's required).

7. **Clip the DEM to your study area**

   We generally recommend that the DEM be clipped to an area that is slightly larger than your area of interest (which is usually a watershed). This is to ensure that the hydrology around the edge of the watershed is captured. This is particularly important if the DEM (and/or other model input data) is of coarse resolution, as clipping to the watershed polygon will lead to large areas of missing data around the edge. To do this, create a buffer around your watershed polygon, and clip the DEM to that buffered polygon. Make sure that the buffer is at least the width of the cell size of your coarsest model input. For example, if your precipitation data is the coarsest, with 1km resolution, create a buffer around the watershed polygon that is at least 1km in width, and use that buffered watershed to clip all of your model inputs, including the DEM. Then use the unbuffered watershed as input to the model.

