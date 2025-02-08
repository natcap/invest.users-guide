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


The Model
=========

The InVEST crop production model is divided into a percentile based yield model, covering 175 crops worldwide, and a regression based model that accounts for fertilization rates on 10 crops. These models are deployed to the end user as the "percentile" and "regression" models.

All results are paired with observed results from the same region for quality control checks as well as nutrition information for 33 macro and micronutrients.

Percentile Model
----------------

The InVEST Crop Production Percentile model produces estimates of 175 crops' yield from existing data, percentile summaries, and observed yields. These observations are based on FAO and sub-national datasets for 175 crops, as metric tons per hectare (Monfreda et al. 2008) and nutrition information. The percentile yields are useful for exploring a range of intenstification levels, listing the yield for the 25th, 50th, 75th, and 95th percentiles, amongst observed yield data in each of the crop's climate bins.

Regression Model
----------------

For 10 staple crops for which yields have been modeled globally by Mueller et al. (2011), the Crop Production Regression model can provide estimates of yields given fertilizer inputs. These crops include barley, maize, oil palm, potato, rice, soybean, sugar beet, sugar cane, sunflower, and wheat. To run this model, the user must provide an additional table that corresponds crops with nitrogen, phosphate, and potash application rates (kg/ha) per crop. The model produces modeled and observed crop yields, as well as nutritional value.


How it Works
------------

Provided Datasets
~~~~~~~~~~~~~~~~~
The sample data contains a **model_data** directory holding the global Monfreda datasets that the model relies on:

- **climate_percentile_yield_tables** (percentile model): For each crop, a CSV listing the 25th, 50th, 75th, and 95th percentile yields in each climate bin. These percentiles are derived from the global observed yield and climate bin datasets; for example, the 95th percentile value for wheat in climate bin 1 is 3.763889. This means that 95% of areas that grow wheat in climate bin 1 produce less than 3.763889 metric tons per hectare. The 50th percentile would be an “average” yield, and the 95th percentile would be a near-optimal yield attained by improving farming practices.
- **climate_regression_yield_tables** (regression model): For each crop, a CSV of regression parameters for each climate bin.
- **crop_nutrient.csv** (percentile and regression models): A table showing the nutritional values for each crop.
- **extended_climate_bin_maps** (percentile model): For each crop, a global raster of climate bins for that crop (see the Supplementary Methods of Mueller et al. 2012 for details).
- **observed_yield** (percentile model): For each crop, a global raster of actual observed yield circa the year 2000.


Percentile Model
^^^^^^^^^^^^^^^^

The Percentile model's algorithm is as follows, for each crop type (corresponding outputs in parentheses):

1. Clip the global climate bin map from **model_data/extended_climate_bin_maps/** to the extent of the user-provided landcover map (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**)
2. For each percentile (25th, 50th, 75th, 95th):

   a. Reclassify the clipped climate map from (1) using the values from **model_data/climate_percentile_yield_tables** to get a map of percentile yields (**intermediate_outputs/<crop>_yield_<percentile>_coarse_yield.tif**).
   b. Interpolate it to the same resolution as the landcover map, changing the large 1/12 degree pixels into a smoother gradient (**intermediate_outputs/<crop>_yield_<percentile>_interpolated_yield.tif**)
   c. Mask out the areas that are not growing that crop according to the landcover map (**<crop>_yield_<percentile>_production.tif**).

3. Clip the global observed yield map from **model_data/observed_yield/** to the extent of the landcover map, and replace nodata pixel values with zero (**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
4. Interpolate it to the same resolution as the landcover map, changing the large 1/12 degree pixels into a smoother gradient (**intermediate_outputs/<crop>_interpolated_observed_yield.tif**)
5. Mask out the areas that are not growing that crop according to the landcover map (**<crop>_observed_production.tif**).
6. Sum up yield values and nutritional values (using data from **model_data/crop_nutrient.csv**), and tabulate the results (**result_table.csv**).
7. If an aggregate polygon vector was provided, sum up values within each aggregate polygon area and tabulate them (**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


Regression Model
^^^^^^^^^^^^^^^^

The Regression model's algorithm is as follows, for each crop type (corresponding outputs in parentheses):

1. Clip the global climate bin map from **model_data/extended_climate_bin_maps/** to the extent of the user-provided landcover map (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**)
2. For each regression parameter:

   a. Reclassify the clipped climate map from (1) using the values from **model_data/climate_regression_yield_tables** to get a map of regression parameter values (**intermediate_outputs/<crop>_<parameter>_coarse_regression_parameter.tif**)
   b. Interpolate it to the same resolution as the landcover map, changing the large 1/12 degree pixels into a smoother gradient (**intermediate_outputs/<crop>_<parameter>_interpolated_regression_parameter.tif**)

3. For each fertilizer element (nitrogen, phosphorus, potassium):

   a. Calculate a raster of crop yield based on that element using the regression parameter rasters from (2) (**intermediate_outputs/<crop>_<element>_yield.tif**).

4. Calculate crop yield by taking the pixel-wise minimum of the three yield rasters from (3) (**<crop>_regression_production.tif**).
5. Clip the global observed yield map from **model_data/observed_yield/** to the extent of the landcover map, and replace nodata pixel values with zero (**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
6. Interpolate it to the same resolution as the landcover map, changing the large 1/12 degree pixels into a smoother gradient (**intermediate_outputs/<crop>_interpolated_observed_yield.tif**)
7. Mask out the areas that are not growing that crop according to the landcover map (**<crop>_observed_production.tif**).
8. Sum up yield values and nutritional values (using data from **model_data/crop_nutrient.csv**), and tabulate the results (**result_table.csv**).
9. If an aggregate polygon vector was provided, sum up values within each aggregate polygon area and tabulate them (**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


 The crop regression itself (steps 3 and 4 above) comes from Mueller et al. 2012 and has the form

 .. math:: Y_{mod_{GC}}=\min(Y_{max}(1-b_{NP}\exp(-c_N N_{GC})), Y_{max}(1-b_{NP} \exp(-c_P P_{GC})), Y_{max}(1-b_K \exp(-c_K K_{GC})))

Where :math:`N_{GC}, P_{GC}, K_{GC}` are the user supplied fertilization rates (N = nitrogen, P = phosphorus, K = potassium), and the other regression parameters are provided as global data to the model.



Limitations and Simplifications
===============================

The current version of the model is a coarse global model driven mostly by climate and optionally by management. This model is therefore not able to capture the variation in productivity that occurs across heterogeneous landscapes. A rocky hill slope and a fertile river valley, if they share the same climate, would be assigned the same yield in the current model. This is a problem if the question of interest is where to prioritize future habitat conversion, or where farming is most productive and least destructive.

Data Needs
==========

There are two InVEST crop production models available, a Percentile based observation model that operates on 175 crops, and a Regression model for exploring fertilziation rates that operates on 10 crops. The arguments below are for both models unless otherwise specified.

**Important**: You need to download the InVEST dataset for Crop Production, to get the Monfreda Dataset required as input to the models. If you choose to install the Crop Production sample data when you install InVEST, there will be a folder called ``sample_data\CropProduction`` in the installation folder for InVEST, where this data may be found. Or, you can download it from http://releases.naturalcapitalproject.org/?prefix=invest/, after going to that link, clicking on the target version, then navigating into the ``data`` directory and selecting ``CropProduction.zip``.

Please also consult the Crop Production dataset for examples of all of these data inputs. This will help with file type, folder structure and table formatting. Note that all GIS inputs must be in the same projected coordinate system and in linear meter units.

Both Models
-----------

- :investspec:`crop_production_percentile workspace_dir`

- :investspec:`crop_production_percentile results_suffix`

- :investspec:`crop_production_percentile model_data_path` Both the percentile and regression models require the base Monfreda Dataset which will be installed if you choose to install sample data along with the InVEST tools, or download the dataset directly as explained above. Once installed, the model folder is ``sample_data\CropProduction\model_data`` in the InVEST data installation directory.

- :investspec:`crop_production_percentile landcover_raster_path` This raster must have a projected coordinate system with units of meters (e.g. UTM) because pixel areas are divided by 10000 in order to report some results in hectares. There can only be one land use/land cover (LULC) class associated with each unique crop type. If you have multiple LULC classes that need to be assigned to one particular crop, you'll need to combine those multiple LULC classes into a single class in the LULC raster before using them in the model.

- :investspec:`crop_production_percentile aggregate_polygon_path`


Additional Percentile Data Needs
--------------------------------

- :investspec:`crop_production_percentile landcover_to_crop_table_path` There can only be one landcover class associated with each unique crop type. See the Land use/Land cover description above for more information.

  Columns:

  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.crop_name`

  Example:

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/landcover_to_crop_table.csv
    :header-rows: 1
    :name: Example Landcover to Crop Table

Additional Regression Data Needs
--------------------------------

- :investspec:`crop_production_regression landcover_to_crop_table_path`

  Columns:

  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.crop_name`

- :investspec:`crop_production_regression fertilization_rate_table_path` An example table is included below that is derived from the median values of observed CBI fertilization rates. Users can explore the raw CBI data in ``sample_data_\CropProduction\model_data\cbi_mod_yield_use_as_check``. (See the **Important** note above for information on obtaining these data.)

  Columns:

  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.crop_name`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.nitrogen_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.phosphorus_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.potassium_rate`

  **Example fertilizer table:**

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/crop_fertilization_rates.csv
    :header-rows: 1
    :name: Crop Fertilization Rate Example. Values come from the median of observed distribution of CBI fertilizer rates.


Interpreting Results
====================

The following is a short description of each of the outputs from the Crop Production model. Final results are found within the user defined Workspace specified for this model run. "Suffix" in the following file names refers to the optional user-defined Suffix input to the model.

- **aggregate_results_[Suffix].csv**: If an Aggregate Results Polygon shapefile is provided, a table is produced that summarizes total observed/percentile/modeled production and nutrient information within each polygon.

- **Crop Production Rasters**: For each crop modeled, there will be a raster (.tif) corresponding to that crop name and the type of modeling - "observed", "regression", or "yield" plus percentile number (25th/50th/75th/95th), and the user-supplied Suffix. These rasters represent the production rate of that crop in metric tons per hectare per year.

- **result_table_[Suffix].csv**: Table listing all of the crops modeled in the run, the area covered, percentile or modeled production, observed production, and nutrient information for each crop. It is the primary output of the model.

There is also an **intermediate_output** folder, containing many files that represent intermediate steps in the calculations of the final results. Usually, you don't need to work with these files, but they may be of interest if you are debugging a model run or want to understand the intermediate steps better. It also contains a subdirectory that stores metadata used internally to enable avoided re-computation.

The **observed yield** outputs approximate actual crop yield in the area of interest, circa the year 2000. The **percentile yield** and **regression yield** outputs are useful if the crop is not currently grown in the area of interest, or to approximate potential for increases by closing yield gaps.

References
==========

"Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000." C. Monfreda, N. Ramankutty, J. Foley. Biogeochemical Cycles, Vol.22, GB1022, doi:10.1029/2007GB002947. 2008

"Closing yield gaps through nutrient and water management" N Mueller, J. Gerber, M. Johnston, D. Ray, N. Ramankutty, J. Foley. Nature. 2012 Oct 11;490(7419):254-7. doi: 10.1038/nature11420. Epub 2012 Aug 29.
