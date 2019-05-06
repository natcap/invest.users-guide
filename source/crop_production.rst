.. primer

.. _crop_production:

***************
Crop Production
***************

Summary
=======

The Crop Production Percentile and Crop Production Regression models estimate crop yield and nutrient value for a fixed set of crops, derived from user-supplied landcover information. Crop yield is primarily driven by climate, and if fertilizer rates are available, they may also be taken into account with the Regression model.


Introduction
============

Expanding agricultural production and closing yield gaps is a key strategy for many governments and development agencies focused on poverty alleviation and achieving food security. However, conversion of natural habitats to agricultural production impacts other ecosystem services that are key to sustaining the economic benefits that agriculture provides to local communities. Intensive agricultural practices can add to pollution loads in water sources, often necessitating future costly water purification methods. Overuse of water also threatens the supply available for hydropower or other services. Still, crop production is essential to human well-being and livelihoods. The InVEST crop production model allows detailed examination of the costs and benefits of this vital human enterprise, including exploration of questions such as:

+ How would a different arrangement or selection of cropping systems compare to current systems in terms of total production? Could switching crops yield higher economic returns or nutritional value?

+ What are the impacts of crop intensification on ecosystem services? If less land is used to produce equal amounts of food by increasing intensification, is the net result on ecosystem services production positive or negative?

+ How can we evaluate different strategies for meeting increasing food demand while minimizing the impact on ecosystem services?

.. primerend

The Model
=========

The InVEST crop production model is divided into a percentile based yield model, covering 175 crops worldwide, and a regression based model that accounts for fertilization rates on 12 crops.  These models are deployed to the end user as the "percentile" and "regression" models.

All results are paried with observed results from the same region for quality control checks as well as nutrition information for 33 macro and micronutrients.

Percentile Model
----------------

The InVEST Crop Production Percentile model produces estimates of 175 crops' yield from existing data, percentile summaries, and observed yields.  These observations are based on FAO and sub-national datasets for 175 crops, as tons/ha (Monfreda et al. 2008) and nutrition information.  The percentile yields are useful for exploring a range of intenstification levels, listing the yield for the 25th, 50th, 75th, and 95th percentiles, amongst observed yield data in each of the crop's climate bins.

Regression Model
----------------

For 12 staple crops for which yields have been modeled globally by Mueller et al. (2011), the Crop Production Regression model can provide estimates of yields given fertilizer inputs. These crops include barley, maize, oil palm, potato, rapeseed, rice, rye, soybean, sugar beet, sugar cane, sunflower, and wheat. To run this model, the user must provide an additional table that corresponds crops with nitrogen, phosphate, and potash application rates (kg/ha) per crop.  The model produces modeled and observed crop yields, as well as nutritional value.


How it Works
------------

Percentile Model
^^^^^^^^^^^^^^^^

The Percentile model's algorithm is as follows:

 1. Reclass landcover to climate bin per crop type
 2. Look up percentile yield per crop type in percentile table associated with climate bin and crop
 3. Calculate nutrient valuation per crop
 4. Fetch observed yield per crop.
 5. (optional) Aggregating total production and nutrient covering the query polygon. Including percentiles/observed.
 6. Output yield maps, percentile production table - observed, and nutrient information.

Regression Model
^^^^^^^^^^^^^^^^

The Regression model's algorithm is as follows:

 1. Reclass landcover to climate bin per crop type
 2. Reclass landcover to all the various regression parameters which are a function of crop type and climate bin
 3. Calculate yield per crop type on map using the supplied fertilization rates (kg/ha for K, N, and Pot)
 4. Calculate nutrient valuation per crop
 5. Fetch observed per crop
 6. Output yield maps, production table - observed, and nutrient information.

 The crop regression itself comes from Mueler et. al 2012 and has the form

 .. math:: Y_{mod_{GC}}=\min(Y_{max}(1-b_{NP}\exp(-c_N N_{GC})), Y_{max}(1-b_{NP} \exp(-c_P P_{GC})), Y_{max}(1-b_K \exp(-c_K K_{GC})))

Where :math:`N_{GC}, P_{GC}, K_{GC}` are the user supplied fertilization rates (N = nitrogen, P = phosphorus, K = potassium), and the other regression parameters are provided as global data to the model.



Limitations and Simplifications
-------------------------------

The current version of the model is a coarse global model driven mostly by climate and optionally by management. This model is therefore not able to capture the variation in productivity that occurs across heterogeneous landscapes. A rocky hill slope and a fertile river valley, if they share the same climate, would be assigned the same yield in the current model. This is a problem if the question of interest is where to prioritize future habitat conversion, or where farming is most productive and least destructive.

Data Needs
==========

There are two InVEST crop production models available, a Percentile based observation model that operates on 175 crops, and a Regression model for exploring fertilziation rates that operates on 12 crops.  The arguments below are for both models unless otherwise specified.

**Important**: You need to download the InVEST dataset for Crop Production, to get the Monfreda Dataset required as input to the models. If you choose to install the sample data when you install InVEST, there will be a folder called CropProduction in the installation folder for InVEST, where this data may be found. Or, you can download it from  http://data.naturalcapitalproject.org/invest-data/. Click on the latest version of InVEST and the dataset is called CropProduction.zip.

Please also consult the Crop Production dataset for examples of all of these data inputs. This will help with file type, folder structure and table formatting. Note that all GIS inputs must be in the same projected coordinate system and in linear meter units.

- **Workspace Folder** (required).  The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created. Make sure that there is ample disk space, and write permissions are correct.

- **Results Suffix** (optional).  Text string that will be appended to the end of output file names, as "\_Suffix". Use a Suffix to differentiate model runs, for example by providing a short name for each scenario. If a Suffix is not provided, or changed between model runs, the tool will overwrite previous results.

- **Directory to model data** (required). Both the percentile and regression models require the base Monfreda Dataset which will be installed if you choose to install sample data along with the InVEST tools, or download the dataset directly from http://data.naturalcapitalproject.org/invest-data/ as explained above. Once installed, the model folder is  ``CropProduction\model_data`` in the InVEST data installation directory.

- **Land-Use/Land-Cover Map** (required). Raster of land use/land cover (LULC) for each pixel, where each unique integer represents a different land use/land cover class. These integers are used in the **Landcover to Crop Table** to map landcover classes to specific crops. This raster must have a projected coordinate system with units of meters (e.g. UTM) because pixel areas are divided by 10000 in order to report some results in hectares.

- **Landcover to Crop Table** (required). A .csv (Comma Separated Value) table that maps a Land-Use/Land-Cover integer code (column *lucode*) to a crop name (column name *crop_name*).  The crop name must be one of the accepted 175 crops for the percentile model, or 12 for the regression model. Accepted crop names for the percentile model can be found in the dataset table ``CropProduction\model_data\crop_nutrient.csv`` while those for the regression model can be found in the dataset table ``CropProduction\model_data\crop_fertilization_rates.csv``. 

 The Landcover to Crop Table must have column names *crop_name* and *lucode*.  An example is given below:

    ========= ======
    crop_name lucode
    ========= ======
    barley    1
    wheat     20
    soybean   1000
    ========= ======


- **Aggregate Results Polygon** (optional). An optional polygon shapefile, where results will be aggregated within each polygon.
 

Additional Regression Data Needs
--------------------------------

- **Fertilization rate table path** (required). A .csv (Comma Separated Value) table that contains crop names, and application rates for nitrogen, phosphorus, and potassium in kilograms/hectare.  An example table is included below that is derived from the median values of observed CBI fertilization rates.  Users can explore the raw CBI data in ``CropProduction\model_data\cbi_mod_yield_use_as_check``. (See the **Important** note above for information on obtaining these data.)

 The following columns are required, and must be named as follows:
 
 - *crop_name*: One of the 12 crops supported for the regression model. Accepted names can be found in the dataset table ``CropProduction\model_data\crop_fertilization_rates.csv``.
 
 - *nitrogen_rate*: Rate of application of nitrogen for each crop, in kg/ha
 
 - *phosphorus_rate*: Rate of application of phosphorus for each crop, in kg/ha
 
 - *potassium_rate*: Rate of application of potassium for each crop, in kg/ha
 
**Example fertilizer table:**

.. csv-table::
  :file: crop_production/crop_fertilization_rates.csv
  :header-rows: 1
  :name: Crop Fertilization Rate Example.  Values come from the median of observed distribution of CBI fertilizer rates.

|

- **Aggregate polygon ID field** (required if providing an Aggregate Results Polygon). Field name in the Aggregate Results Polygon shapefile that is used to uniquely identify each polygon. String value.

Advanced Usage
^^^^^^^^^^^^^^
These models support avoided re-computation. This means the model will detect intermediate and final results from a previous run in the specified workspace and it will avoid re-calculating any outputs that are identical to the previous run. This can save significant processing time for successive runs when only some input parameters have changed.

.. primer

Running the model
=================

To launch the Crop Production model navigate to the Windows Start Menu -> All Programs -> InVEST [*version*] -> Crop Production (Percentile) or Crop Production (Regression). The interface does not require a GIS desktop, although the results will need to be explored with any GIS tool such as ArcGIS or QGIS.

Interpreting Results
====================

The following is a short description of each of the outputs from the Crop Production model. Final results are found within the user defined Workspace specified for this model run. "Suffix" in the following file names refers to the optional user-defined Suffix input to the model.

- **aggregate_results_[Suffix].csv**: If an Aggregate Results Polygon shapefile is provided, a table is produced that summarizes total observed/percentile/modeled production and nutrient information within each polygon.

- **Crop Production Rasters**: For each crop modeled, there will be a raster (.tif) corresponding to that crop name and the type of modeling - "observed", "regression", or "yield" plus percentile number (25th/50th/75th/95th), and the user-supplied Suffix.  These rasters represent the production rate of that crop per pixel.

- **result_table_[Suffix].csv**: Table listing all of the crops modeled in the run, the area covered, percentile or modeled production, observed production, and nutrient information for each crop.  It is the primary output of the model.

There is also an **intermediate_output** folder, containing many files that represent intermediate steps in the calculations of the final results. Usually, you don't need to work with these files, but they may be of interest if you are debugging a model run or want to understand the intermediate steps better. It also contains a subdirectory that stores metadata used internally to enable avoided re-computation.

References
==========

"Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000."" C. Monfreda N. Ramankutty, J. Foley. Biogeochemical Cycles, Vol.22, GB1022, doi:10.1029/2007GB002947. 2008

"Closing yield gaps through nutrient and water management" N Mueller, J. Gerber, M. Johnston, D. Ray, N. Ramankutty, J. Foley. Nature. 2012 Oct 11;490(7419):254-7. doi: 10.1038/nature11420. Epub 2012 Aug 29.
