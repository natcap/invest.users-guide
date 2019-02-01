.. primer

.. _crop_production:

***************
Crop Production
***************

Summary
=======

.. figure:: ./crop_production_images/field.png
   :align: center
   :scale: 60%


.. raw:: html

    <style> .red {color:#9F000F} </style>
    <br>

Introduction
============

Expanding agricultural production and closing yield gaps is a key strategy for many governments and development agencies focused on poverty alleviation and achieving food security. However, conversion of natural habitats to agricultural production sites impacts other ecosystem services that are key to sustaining the economic benefits that agriculture provides to local communities. Intensive agricultural practices can add to pollution loads in water sources, often necessitating future costly water purification methods. Overuse of water also threatens the supply available for hydropower or other services. Still, crop production is essential to human well-being and livelihoods. The InVEST crop production model allows detailed examination of the costs and benefits of this vital human enterprise, allowing exploration of questions such as:

+ How would different arrangement or selection of cropping systems compare to current systems in terms of total production? Could switching crops yield higher economic returns or nutritional value?

+ What are the impacts of crop intensification on ecosystem services? If less land is used to produce equal amounts of food by increasing intensification, is the net result on ecosystem services production positive or negative?

+ How can we evaluate different strategies for meeting increasing food demand while minimizing the impact on ecosystem services?

.. primerend

The Model
=========

The InVEST crop production model is divided into a percentile based yield model, covering 175 crops worldwide, and a regression based model that accounts for fertilization rates on 12 crops.  These models are deployed to the end user as the "percentile" and "regression" model.

All results are paried with observed results from the same region for quality control checks as well as nutrition information of 33 macro and micronutrients.

Percentile Model
----------------

The InVEST crop production percentile model will produce estimates of 175 crops' yield from existing data, percentile summaries, and observed yields.  These observations are based on FAO and sub-national datasets for 175 crops, as tons/ha (Monfreda et al. 2008) and nutrition information.  The percentile yields are useful for exploring a range of intenstification levels, listing the yield for the 25th, 50th, 75th, and 95th percentiles, amongst observed yield data in each of the crop's climate bins.

Regression Model
----------------

For 12 staple crops for which yields have been modeled globally by Mueller et al. (2011), the model can provide estimates of both yields given fertilizer inputs. These crops include barley, maize, oil palm, potato, rapeseed, rice, rye, soybean, sugar beet, sugar cane, sunflower, and wheat. To run this model, the user must provide an additional tabe that corresponds with nitrogen, phosphate, and potash application rates (kg/ha) per crop.  The model produces modeled and observed crop yields, as well as nutritional value.


How it Works
------------

Percentile Model
^^^^^^^^^^^^^^^^

The percentile model's algorithm is as follows

 1. Reclass landcover to climate bin per crop type
 2. Look up percentile yield per crop type in percentile table associated with climate bin and crop
 3. Calculate nutrient valuation per crop
 4. Fetch observed yield per crop.
 5. (optional) Aggregating total production and nutrient covering the query polygon. Including percentiles/observed.
 6. Output yield maps, percentile production table - observed, and nutrient information.

Regression Model
^^^^^^^^^^^^^^^^

In general, the algorithm for crop production regression is as follows

 1. Reclass landcover to climate bin per crop type
 2. Reclass landcover to all the various regression parameters which are a function of crop type and climate bin
 3. Calculate yield per crop type on map using the supplied fertilization rates (kg/ha for K, N, and Pot)
 4. Calculate nutrient valuation per crop
 5. Fetch observed per crop
 6. Output yield maps, production table - observed, and nutrient information.

 The crop regression itself comes from Mueler et. al 2012 and has the form

 .. math:: Y_{mod_{GC}}=\min(Y_{max}(1-b_{NP}\exp(-c_N N_{GC})), Y_{max}(1-b_{NP} \exp(-c_P P_{GC})), Y_{max}(1-b_K \exp(-c_K K_{GC})))

Where :math:`N_{GC}, P_{GC}, K_{GC}` are the user supplied fertilization rates, and the other regression parameters are provided as global data to the model.



Limitations and Simplifications
-------------------------------

The current version of the model is a coarse global model driven mostly by climate and optionally by management. This model is therefore not able to capture the variation in productivity that occurs across heterogeneous landscapes. A rocky hill slope and a fertile river valley, if they share the same climate, would be assigned the same yield in the current model. This is a problem if the question of interest is where: where to prioritize future habitat conversion; or where farming is most productive and least destructive.

Data Needs/Running the Model
============================

There are two InVEST crop production models available, a percentile based observation model that operates on 175 crops, and a regression model for exploring fertilziation rates that operates on 12 crops.  The arguments below are for both models unless otherwise specified.

 1. **Workspace Folder**  The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created.  If datasets already exist in the selected folder, they will be overwritten.

 2. **Results Suffix (Optional)**  This text will be appended to the end of the output folders to help separate outputs from multiple runs.  Please see the `Interpreting Results`_ section for an example folder structure for outputs.

 3. **Base Data (Directory)** Both the percentile and regression model require the base Monfreda Dataset which ships with the InVEST installer and can be found at ``CropProduction\model_data`` in the InVEST data installation directory.

 4. **Landcover Map (Raster)**  An integer raster where each code corresponds to a landcover type.  This raster should have a projected coordinate system with units of meters (e.g. UTM) because pixel areas are divided by 10000 in order to report some results in hectares.

 5. **Landcover to Crop Table (csv)** A table that maps a landcover ID to a crop name.  The crop name must be one of the accepted 175 crops for the percentile model, or 12 for regression.  The table must have column names `crop_name` and `lucode` corresponding to these values.  An example is given below

    ========= ======
    crop_name lucode
    ========= ======
    barley    1
    wheat     20
    soybean   1000
    ========= ======

 Accepted crop names for percentile can be found in the table at ``CropProduction\model_data\crop_nutrient.csv`` while those for regression can be found in the table at ``CropProduction\model_data\crop_fertilization_rates.csv``.

 6. **Aggregating Polygon (shapefile)** An optional polygon shapefile to aggregate results over.  If it is provided, the shapefile must have a keyfield to uniquely identify each polygon, the name of this field must also be provided in the user interface.

Additional Regression Data Needs
--------------------------------

 + **Fertilization rate per crop (CSV)** This is a CSV table that contains crop names, and application rates for nitrogen, phosphate, and potassium.  An example table is included below that is derived from the median values of observed CBI fertilization rates.  Users can explore the raw CBI data in ``CropProduction\model_data\cbi_mod_yield_use_as_check``.

.. csv-table::
  :file: crop_production/crop_fertilization_rates.csv
  :header-rows: 1
  :name: Crop Fertilization Rate Example.  Values come from the median of observed distribution of CBI fertilizer rates.


Advanced Usage
^^^^^^^^^^^^^^
These models support avoided re-computation. This means the model will detect intermediate and final results from a previous run in the specified workspace and it will avoid re-calculating any outputs that are identical to the previous run. This can save significant processing time for successive runs when only some input parameters have changed.

.. primer

Interpreting Results
====================

**Outputs Folder Structure**

1. **Result Table (CSV)** This is an aggregating table that lists all the crops modeled in the run, the area covered, percentile or modeled production, observed production, and nutrient information for each mode.  It is the primary output of the model.

2. **Crop Production Rasters** For each crop modeled, there will be a raster corresponding to that crop name, the type of modeling (observed, percentile, or regression).  The result is the production rate per pixel.

3. **Aggregate Table (CSV)** If an aggregating polygon is provided, a table is produced that summarizes total observed/percentile/modeled production and nutrient information for polygon ID.


References
==========

"Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000."" C. Monfreda N. Ramankutty, J. Foley. Biogeochemical Cycles, Vol.22, GB1022, doi:10.1029/2007GB002947. 2008

"Closing yield gaps through nutrient and water management" N Mueller, J. Gerber, M. Johnston, D. Ray, N. Ramankutty, J. Foley. Nature. 2012 Oct 11;490(7419):254-7. doi: 10.1038/nature11420. Epub 2012 Aug 29.
