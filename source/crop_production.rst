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

**NOTE THE CROP PRODUCTION TOOL IS IN A ALPHA/UNSTABLE STATE.  IT SHOULD NOT BE USED IN DECISION-MAKING REPORTS UNTIL IT IS RELEASED AS A STABLE MODEL.**

Introduction
============

Expanding agricultural production and closing yield gaps is a key strategy for many governments and development agencies focused on poverty alleviation and achieving food security. However, conversion of natural habitats to agricultural production sites impacts other ecosystem services that are key to sustaining the economic benefits that agriculture provides to local communities. Intensive agricultural practices can add to pollution loads in water sources, often necessitating future costly water purification methods. Overuse of water also threatens the supply available for hydropower or other services. Still, crop production is essential to human well-being and livelihoods. The InVEST crop production model allows detailed examination of the costs and benefits of this vital human enterprise, allowing exploration of questions such as:

+ How would different arrangement or selection of cropping systems compare to current systems in terms of total production? Could switching crops yield higher economic returns or nutritional value?

+ What are the impacts of crop intensification on ecosystem services? If less land is used to produce equal amounts of food by increasing intensification, is the net result on ecosystem services production positive or negative?

+ How can we evaluate different strategies for meeting increasing food demand while minimizing impact on ecosystem services?

.. primerend

The Model
=========

The InVEST crop production model will produce estimates of crop yield, from existing data, percentile summaries, and modeled predictions.  For existing or modeled crop yields, the model can also generate estimates of crop value.

*Observed data*: The crop yield model supplies observed yields, based on FAO and sub-national datasets for 175 crops, as tons/ha (Monfreda et al. 2008). If a crop type submitted by the user is not grown in that region, the model will not return a value for those pixels; crops can be moved around within a region in which they are grown, but novel cropping systems cannot be introduced in minimum mode. The model will also return existing inputs for that crop (in that region), as percent of land irrigated (for 15 crops for which there are data), and amount of N, P, and K applied/ha (for 140 crops for which there are data). The model can provide nutrition information for all crops and economic production if additional cost information is provided for fertilizer, nutrients, labor, seed, and machinery (this information is already included in the model for 12 staple crops in 2012: barley, maize, oil palm, potato, rapeseed, rice, rye, soybean, sugar beet, sugar cane, sunflower, and wheat).

*Percentile summaries*: This option allow the user to explore yields under different management scenarios, picking from a range of “intensification” levels.  The user can supply a percentile raster, with each pixel of agricultural land coded 25, 50, 75, or 95 as a proxy for low, medium, high, or maximum productivity, presumably achieved under corresponding degrees of intensification. This will return the 25th, 50th, 75th, or 95th percentile yields, respectively, for the crop of interest in all regions of similar climate and income. The user also has an option to select a World Bank Income Classification to explore different productivity levels possible under different income conditions, with accompanying assumptions about how this would change their access to technology or other capital. This feature is optional and should be interpreted with caution (i.e., the feasibility of moving from one income category to another), and if the user does not make a selection the model will use the actual income classification for that region. Because there is no information about the actual quantities of fertilizer and irrigation needed to achieve these different percentiles of production, this option does not allow economic valuation of production, but can provide nutrition production information if desired.

*Modeled yields*: For 12 staple crops for which yields have been modeled globally by Mueller et al. (2011), the model can provide estimates of both yields and inputs (fertilizer and irrigation), in the same units as above. These crops include barley, maize, oil palm, potato, rapeseed, rice, rye, soybean, sugar beet, sugar cane, sunflower, and wheat. To run this model, the user must provide rasters of nitrogen, phosphate, and potash application rate (kg/ha) and an irrigation raster (0 for pixels that are not irrigated and 1 for pixels that are) that cover all cropped areas of interest. The model returns crop yields and economic and nutritional value.

The crop value model can use the yields and/or inputs generated by the yield model, or can be run with yield maps derived from other models or data sources (e.g., SSURGO). Crop yields can be valued in terms of economic returns or in terms of nutrition. To calculate economic returns, the model requires yield maps, as well as maps of fertilizer and irrigation rates corresponding to those yields, and combines this information with crop price and cost datasets to calculate the total expected returns (yields x area x price – inputs x input costs – area x other costs). To calculate nutrition, the model only requires yield maps of all food crops produced, and the user can select from 33 macro and micronutrients to map or summarize. This model can be combined with our nutrition demand model, which multiplies population density by recommended daily allowances of the same nutrients, to determine what proportion of nutritional requirements can be met from local food production.


How it Works
------------

Calculating Yield and Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Method 1: Observed Regional Yields (Observed)
"""""""""""""""""""""""""""""""""""""""""""""

  :math:`ProductionPerCell_{crop,x,y} = { ObservedLocalYieldPerHectare_{crop,x,y} * HectaresPerCell }`

  :math:`ProductionTotal_{crop} = \sum_{x,y}{ ProductionPerCell_{crop,x,y} }`

Method 2: Climate-specific Distribution of Observed Yields (Percentile)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  :math:`YieldPerHectare_{crop,percentile,x,y} = \left( ObservedClimateBinYield_{crop, precentile, climatebin} \mid ClimateBin_{x, y} \right)`

  :math:`ProductionPerCell_{crop,percentile,x,y} = YieldPerHectare_{crop,percentile,x,y} * HectaresPerCell`

  :math:`ProductionTotal_{crop,percentile} = \sum_{x,y}{ ProductionPerCell_{crop,percentile,x,y} }`

Method 3: Yield Regression Model with Climate-specific Parameters (Modeled)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  :math:`PercentMaxYieldNitrogen_{x,y} = \left( 1 - Bnp_{crop,climatebin} * e^{-Cn_{crop,climatebin} * NitrogenAppRate_{x,y}} \mid ClimateBin_{x, y} \right)`

  :math:`PercentMaxYieldPhosphorus_{x,y} = \left( 1 - Bnp_{crop,climatebin} * e^{-Cp_{crop,climatebin} * PhosphorusAppRate_{x,y}} \mid ClimateBin_{x, y} \right)`

  :math:`PercentMaxYieldPotassium_{x,y} = \left( 1 - Bk_{crop,climatebin} * e^{-Ck_{crop,climatebin} * PotassiumAppRate_{x,y}} \mid ClimateBin_{x, y} \right)`

  :math:`MaxYieldNitrogen_{x,y} = MaxYield_{crop,climatebin} * PercentMaxYieldNitrogen_{x,y}`

  :math:`MaxYieldPhosphorus_{x,y} = MaxYield_{crop,climatebin} * PercentMaxYieldPhosphorus_{x,y}`

  :math:`MaxYieldPotassium_{x,y} = MaxYield_{crop,climatebin} * PercentMaxYieldPotassium_{x,y}`

  :math:`YieldPerHectare_{crop,x,y} = \left\{ \begin{matrix} min\left( MaxYieldNitrogen, MaxYieldPhosphorus, MaxYieldPotassium \right) & if & irrigated \\ min\left( MaxYieldNitrogen, MaxYieldPhosphorus, MaxYieldPotassium, MaxYieldRainfed  \right) & if & rainfed \end{matrix} \right\}`

  :math:`ProductionPerCell_{crop,x,y} = YieldPerHectare_{crop,x,y} * HectaresPerCell_{x,y}`

  :math:`ProductionTotal_{crop} = \sum_{x,y}{ ProductionPerCell_{crop,x,y} }`

Calculating Nutritional Contents from Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  :math:`NutrientAmount_{crop, nutrient} = NutrientAmountPerTonCrop_{crop, nutrient} * ProductionTotal_{crop} * (1 - FractionRefuse)`

  :math:`NutrientAmountTotal_{nutrient} = \sum_{crops}{ NutrientAmount_{crop, nutrient} }`

Calculating Economic Returns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  :math:`KilogramInputTotalCosts_{crop, x, y} = \sum_{fertilizer} \left( { FertKgPerHectare_{fertilizer,x,y} * CostPerKg_{crop, fertilizer} * HectaresPerCell } \right)`

  :math:`HectareInputTotalCosts_{crop, x, y} = { \sum_{inputs}{ CostPerHectare_{input,x,y}} * HectaresPerCell }`

  :math:`Cost_{crop, x, y} = KilogramInputTotalCosts_{crop, x, y} + HectareInputTotalCosts_{crop, x, y}`

  :math:`Revenue_{crop, x, y} = Production_{crop, x, y} * Price_{crop}`

  :math:`Returns_{crop, x, y} = Revenue_{crop, x, y} - Cost_{crop, x, y}`

  :math:`ReturnsTotal_{crop} = \sum_{x, y} Returns_{crop, x, y}`


Limitations and Simplifications
-------------------------------

The current version of the model is a coarse global model driven mostly by climate and optionally by management. This model is therefore not able to capture the variation in productivity that occurs across heterogeneous landscapes. A rocky hill slope and a fertile river valley, if they share the same climate, would be assigned the same yield in the current model. This is a problem if the question of interest is where: where to prioritize future habitat conversion; or where farming is most productive and least destructive.

Spatial downscaling of the current coarse global model is necessary to make the crop model more useful in local land-use decisions. Our approach will be to acquire local yield data that can be compared to the regression model yields to determine where the model is overestimating yields and where it is underestimating. The resulting differences can be related to other variables such as slope, aspect, elevation, soil fertility, and soil depth, and any significant relationships can be used to refine the current model. The coarse model will still be used to arrive at the general magnitude of yield for a given climate and intensification level, and the finer-scale differences will essentially tune the coarse model up or down. To do this we need:

+	Field-level (or better) yield data across a wide representation of soils, topographies and climates

+	Soil and topographic data at the same level of resolution as the yield data

If you have or intend to take such data and are interested in collaborating with us, please contact Becky Chaplin-Kramer at bchaplin@stanford.edu



Data Needs
==========

+ Monfreda Dataset

  + Observed Crop Yields (provided in units of tons per harvested hectare (growing season))

+ Foley Lab Datasets

  + Climate-bin Based Tables

  + Regression Model Parameters


Running the Model
=================

**General Parameters**

1. **Workspace Folder**  The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created.  If datasets already exist in the selected folder, they will be overwritten.

2. **Results Suffix (Optional)**  This text will be appended to the end of the output folders to help separate outputs from multiple runs.  Please see the `Interpreting Results`_ section for an example folder structure for outputs.

3. **LULC Lookup Table (CSV)**  A CSV table used to manage the relationship between the lulc codes and the crop dataset.  The provided CSV file should contain a table with two columns: a 'lulc-class' column, a 'code' column, and a 'is_crop' column.  The 'lulc-class' column contains the names of each lulc-class used in the model, the 'code' column contains the associated code used to represent that lulc-class in the LULC Map, and the 'is_crop' column contains a boolean value indicating whether the given lulc-class is a crop. If 'is_crop' is set to True, the Spatial Dataset must contain tables and maps associated with that crop. Any non-negative integer value can be used as a 'code' value.

  ==========  ====  =======
  lulc-class  code  is_crop
  ==========  ====  =======
  other       0     False
  maize       1     True
  soybean     2     True
  rice        3     True
  ...         ...
  ==========  ====  =======

4. **LULC Map (Raster)**  A GDAL-supported raster representing a crop management scenario. Each cell value in the raster should be a valid integer code that corresponds to a lulc-class in the LULC Lookup Table file.  The NoData value should be set to a number not existing in the LULC Lookup Table.

  +---+---+
  |int|int|
  +---+---+
  |int|int|
  +---+---+

5. **Fertilizer Application Rate Maps (Rasters)**  A set of GDAL-supported rasters representing the amount of Nitrogen (N), Phosphorus (P2O5), and Potash (K2O) applied to each area of land. These maps are required for the regression model yield function and are an optional input for all yield functions when calculating economic returns. Each cell value in the raster should be a non-negative float value representing the amount of fertilizer applied in units of kilograms per hectare (kgs/ha). Each file should be prepended with the name of the fertilizer (nitrogen, phosphorus, potash) in lowercase, followed by an underscore to help the program search for the matching file.  The Fertilizer Maps should have the same dimensions and projection as the provided LULC Map.

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

  **Folder Structure**

  .. code-block:: none

    .
    |-- fertilizer_maps_folder
        |-- nitrogen_application_map.tif
        |-- phosphorus_application_map.tif
        |-- potash_application_map.tif

6. **Crop Production Model Spatial Dataset Folder**

  **Folder Structure**

  .. code-block:: none

    .
    |-- spatial_dataset_folder
        |-- climate_bin_maps
        |   |-- [crop]_climate_bin_map (*.tif)
        |-- climate_percentile_yield
        |   |-- [crop]_percentile_yield_table.csv
        |-- climate_regression_yield
        |   |-- [crop]_regression_yield_table.csv
        |-- observed_yield
            |-- [crop]_yield_map (*.tif)

  **Embedded Data for Functions Based on Climate (Percentile and Regression Functions)**

    **Crop Climate-Bin Maps (Rasters)**  A set of GDAL-supported rasters representing the climate-bin that a given area of land is located within for each particular crop.  Each raster contains a set of values between 0 and 100.  Zero-values represent areas that do not exist within a climate-bin, such as an ocean.  Values 1 through 100 correspond to a particular climate-bin.  The climate-bin maps reside in the 'climate_bin_maps' folder of the provided spatial dataset.

      +---+---+
      |int|int|
      +---+---+
      |int|int|
      +---+---+

  **Embedded Data for Observed Regional Yields**

    **Observed Crop Yield Maps (Rasters)**  A set of GDAL-supported rasters representing the observed regional crop yield.  Each cell value in the raster should be a non-negative float value representing the amount of crop produced in units of tons per hectare (tons/hectare).  The observed yield maps reside in the 'observed_yield' folder of the provided spatial dataset.

      +-----+-----+
      |float|float|
      +-----+-----+
      |float|float|
      +-----+-----+

  **Embedded Data for Climate-specific Distribution of Observed Yields**

    **Percentile Yield Table (CSV)**  The provided CSV tables should contain information about the average crop yield occurring within each climate-bin across several income levels for each crop in units of tons per hectare (tons/ha).  The table must have a 'climate_bin' column containing values 0 through 100.  The table must have at least one additional column representing a percentile yield within the given climate-bin for a particular crop - an example set of columns could be: 'yield_25th', 'yield_50th', 'yield_75th', 'yield_95th'.  So, this example table would have the following columns: 'crop', 'climate_bin', 'yield_25th', 'yield_50th', 'yield_75th', 'yield_95th'. Each file should be prepended with the name of the crop in lowercase, followed by an underscore to help the program parse the file.   The tables reside in the 'climate_percentile_yield' folder of the provided spatial dataset.

      ===========  ==========  ==========  ==========  ==========  ===
      climate_bin  yield_25th  yield_50th  yield_75th  yield_95th  ...
      ===========  ==========  ==========  ==========  ==========  ===
      1            <float>     <float>     <float>     <float>     ...
      2            <float>     <float>     <float>     <float>     ...
      3            <float>     <float>     <float>     <float>     ...
      ...          ...         ...         ...         ...         ...
      ===========  ==========  ==========  ==========  ==========  ===

      e.g. 'maize_percentile_yield_table.csv'

  **Embedded Data for Yield Regression Model with Climate-specific Parameters**

    **Regression Model Yield Table (CSV)**  The provided CSV tables should contain information useful for calculating the yield of a crop located in a particular climate-bin based on the limiting factor.  The table must have the following columns: 'climate_bin', 'yield_ceiling', 'yield_ceiling_rf', 'b_nut', 'b_K2O', 'c_N', 'c_P2O5', and 'c_K2O'. Each file should be prepended with the name of the crop in lowercase, followed by an underscore to help the program search for the matching file. Currently, the regression model yield function is useful to a small subset of the crops provided in the dataset.  The tables reside in the 'climate_regression_yield' folder of the provided spatial dataset.

      ===========  =============  ================  =======  =======  =======  =======  =======
      climate_bin  yield_ceiling  yield_ceiling_rf  b_nut    b_K2O    c_N      c_P2O5   c_K2O
      ===========  =============  ================  =======  =======  =======  =======  =======
      1            <float>        <float>           <float>  <float>  <float>  <float>  <float>
      2            <float>        <float>           <float>  <float>  <float>  <float>  <float>
      3            <float>        <float>           <float>  <float>  <float>  <float>  <float>
      ...          ...            ...               ...      ...      ...      ...      ...
      ===========  =============  ================  =======  =======  =======  =======  =======

      e.g. 'maize_regression_yield_table.csv'

**Parameters for Yield Regression Model with Climate-specific Parameters**

7. **Irrigation Map (Raster)**  A GDAL-supported raster representing whether irrigation occurs or not. A zero value indicates that no irrigation occurs.  A one value indicates that irrigation occurs.  The Irrigation Map should have the same dimensions and projection as the provided LULC Map.

  +---+---+
  |int|int|
  +---+---+
  |int|int|
  +---+---+

.. note::

  The regression yield function also requires the 'Fertilizer Application Rate Maps' as an input.

**Parameters for Calculating Nutritional Contents from Production**

8. **Nutrient Contents Table (CSV)**  A CSV table containing information about the nutrient contents of each crop.  The values provided are assumed to be given in relation to one ton of harvest crop biomass.  The 'crop' and 'fraction_refuse' columns must be provided in the table.  The 'fraction_refuse' column is expected to contain a value between 0 and 1 representing the fraction of the harvested crop that is considered refuse and does not contain nutritional value.

  =======  ===============  ========  ========  ========  ========  ========  ===
  crop     fraction_refuse  protein   lipid     energy    ca        ph        ...
  =======  ===============  ========  ========  ========  ========  ========  ===
  maize     <float>          <float>   <float>   <float>   <float>   <float>   ...
  soybean   <float>          <float>   <float>   <float>   <float>   <float>   ...
  ...       ...              ...       ...       ...       ...       ...       ...
  =======  ===============  ========  ========  ========  ========  ========  ===

**Parameters for Calculating Economic Returns**

9. **Economics Table (CSV)**  A CSV table containing information related to market price of a given crop and the costs involved with producing that crop.

  ========  =============  ====================  ======================  ==================  =================  ===================  ================  ======================
  crop      price_per_ton  cost_nitrogen_per_kg  cost_phosphorus_per_kg  cost_potash_per_kg  cost_labor_per_ha  cost_machine_per_ha  cost_seed_per_ha  cost_irrigation_per_ha
  ========  =============  ====================  ======================  ==================  =================  ===================  ================  ======================
  maize     <float>        <float>               <float>                 <float>             <float>            <float>              <float>           <float>
  soybean   <float>        <float>               <float>                 <float>             <float>            <float>              <float>           <float>
  ...       ...            ...                   ...                     ...                 ...                ...                  ...               ...
  ========  =============  ====================  ======================  ==================  =================  ===================  ================  ======================

.. primer

Interpreting Results
====================

**Outputs Folder Structure**

A unique set of outputs shall be created for each yield function that is run such that the folder structure may look as follows:

.. code-block:: none

  .
  |-- outputs
      |-- climate_percentile_yield_[results suffix]
      |   |-- results_table (.csv)
      |   |-- yield_map (.tif)
      |   |-- production_map (.tif)
      |   |-- cost_map (.tif)
      |   |-- revenue_map (.tif)
      |   |-- returns_map (.tif)
      |-- climate_regression_yield_[results suffix]
      |   |-- results_table (.csv)
      |   |-- yield_map (.tif)
      |   |-- production_map (.tif)
      |   |-- cost_map (.tif)
      |   |-- revenue_map (.tif)
      |   |-- returns_map (.tif)
      |-- observed_yield_[results suffix]
          |-- results_table (.csv)
          |-- yield_map (.tif)
          |-- production_map (.tif)
          |-- cost_map (.tif)
          |-- revenue_map (.tif)
          |-- returns_map (.tif)

**Outputs**

1. **Results Table (CSV)**

  =======  ==========  ============  =========  =========  =======  ============  ============  ======
  crop     production  (percentile)  (return)   (revenue)  (cost)   (nutrient_a)  (nutrient_b)  (etc.)
  =======  ==========  ============  =========  =========  =======  ============  ============  ======
  maize    <float>     <str>         <float>    <float>    <float>  <float>       <float>       ...
  soybean  <float>     <str>         <float>    <float>    <float>  <float>       <float>       ...
  ...      ...         ...           ...        ...        ...      ...           ...           ...
  =======  ==========  ============  =========  =========  =======  ============  ============  ======

2. **Crop Yield Map (Raster)** A set of GDAL-supported rasters spatially representing the per-hectare yield for a given crop in each cell.  Each cell value in the raster shall be a non-negative float value representing the yield area under the given scenario in units of tons per hectare (tons/ha).

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

3. **Crop Production Map (Raster)** A GDAL-supported raster spatially representing the total production for a given crop in each cell.  Each cell value in the raster shall be a non-negative float value representing the total production over the cell's area under the given scenario in units of tons.

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

4. **Economic Cost Map (Raster) (Optional)**  A GDAL-supported raster representing the economic cost associated with the crops.  Each cell value in the raster shall be a float value representing the cost generated under the given scenario in units of the currency from the user-provided Economics Table. If insufficient data is provided within a given cell, the cell will contain a NoData value.

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

5. **Economic Revenue Map (Raster) (Optional)**  A GDAL-supported raster representing the economic revenue generated by the crops.  Each cell value in the raster shall be a float value representing the revenue generated under the given scenario in units of the currency from the user-provided Economics Table. If insufficient data is provided within a given cell, the cell will contain a NoData value.

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

6. **Economic Returns Map (Raster) (Optional)**  A GDAL-supported raster representing the economic returns generated by the crops.  Each cell value in the raster shall be a float value representing the return (revenue minus cost) generated under the given scenario in units of the currency from the user-provided Economics Table. If insufficient data is provided within a given cell, the cell will contain a NoData value.

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

.. primerend

References
==========

Monfreda et al. 2008

Mueller et al. 2012



Appendix I
==========

Available Crop Data within Global Dataset
-----------------------------------------

.. csv-table::

  Crop,Observed Model,Percentile Model,Regression Model
  Abaca,Yes,Yes,No
  Agave,Yes,Yes,No
  Alfalfa,Yes,Yes,No
  Almond,Yes,Yes,No
  Aniseetc,Yes,Yes,No
  Apple,Yes,Yes,No
  Apricot,Yes,Yes,No
  Areca,Yes,Yes,No
  Artichoke,Yes,Yes,No
  Asparagus,Yes,Yes,No
  Avacado,Yes,Yes,No
  Bambara,Yes,Yes,No
  Banana,Yes,Yes,No
  Barley,Yes,Yes,Yes
  Bean,Yes,Yes,No
  Beetfor,Yes,Yes,No
  Berrynes,Yes,Yes,No
  Blueberry,Yes,Yes,No
  Brazil,Yes,Yes,No
  Broadbean,Yes,Yes,No
  Buckwheat,Yes,Yes,No
  Cabbage,Yes,Yes,No
  Cabbagefor,Yes,Yes,No
  Canaryseed,Yes,Yes,No
  Carob,Yes,Yes,No
  Carrot,Yes,Yes,No
  Carrotfor,Yes,Yes,No
  Cashew,Yes,Yes,No
  Cashewapple,Yes,Yes,No
  Cassava,Yes,Yes,No
  Castor,Yes,Yes,No
  Cauliflower,Yes,Yes,No
  Cerealnes,Yes,Yes,No
  Cherry,Yes,Yes,No
  Chestnut,Yes,Yes,No
  Chickpea,Yes,Yes,No
  Chicory,Yes,Yes,No
  Chilleetc,Yes,Yes,No
  Cinnamon,Yes,Yes,No
  Citrusnes,Yes,Yes,No
  Clove,Yes,Yes,No
  Clover,Yes,Yes,No
  Cocoa,Yes,Yes,No
  Coconut,Yes,Yes,No
  Coffee,Yes,Yes,No
  Coir,Yes,No,No
  Cotton,Yes,Yes,No
  Cowpea,Yes,Yes,No
  Cranberry,Yes,Yes,No
  Cucumberetc,Yes,Yes,No
  Currant,Yes,Yes,No
  Date,Yes,Yes,No
  Eggplant,Yes,Yes,No
  Fibrenes,Yes,Yes,No
  Fig,Yes,Yes,No
  Flax,Yes,Yes,No
  Fonio,Yes,Yes,No
  Fornes,Yes,Yes,No
  Fruitnes,Yes,Yes,No
  Garlic,Yes,Yes,No
  Ginger,Yes,Yes,No
  Gooseberry,Yes,Yes,No
  Grape,Yes,Yes,No
  Grapefruitetc,Yes,Yes,No
  Grassnes,Yes,Yes,No
  Greenbean,Yes,Yes,No
  Greenbroadbean,Yes,Yes,No
  Greencorn,Yes,Yes,No
  Greenonion,Yes,Yes,No
  Greenpea,Yes,Yes,No
  Groundnut,Yes,Yes,No
  Gums,Yes,No,No
  Hazelnut,Yes,Yes,No
  Hemp,Yes,Yes,No
  Hempseed,Yes,Yes,No
  Hop,Yes,Yes,No
  Jute,Yes,Yes,No
  Jutelikefiber,Yes,Yes,No
  Kapokfiber,Yes,Yes,No
  Kapokseed,Yes,Yes,No
  Karite,Yes,Yes,No
  Kiwi,Yes,Yes,No
  Kolant,Yes,Yes,No
  Legumenes,Yes,Yes,No
  Lemonlime,Yes,Yes,No
  Lentil,Yes,Yes,No
  Lettuce,Yes,Yes,No
  Linseed,Yes,Yes,No
  Lupin,Yes,Yes,No
  Maize,Yes,Yes,Yes
  Maizefor,Yes,Yes,No
  Mango,Yes,Yes,No
  Mate,Yes,Yes,No
  Melonetc,Yes,Yes,No
  Melonseed,Yes,Yes,No
  Millet,Yes,Yes,No
  Mixedgrain,Yes,Yes,No
  Mixedgrass,Yes,Yes,No
  Mushroom,Yes,Yes,No
  Mustard,Yes,Yes,No
  Nutmeg,Yes,Yes,No
  Nutnes,Yes,Yes,No
  Oats,Yes,Yes,No
  Oilpalm,Yes,Yes,Yes
  Oilseedfor,Yes,Yes,No
  Oilseednes,Yes,Yes,No
  Okra,Yes,Yes,No
  Olive,Yes,Yes,No
  Onion,Yes,Yes,No
  Orange,Yes,Yes,No
  Papaya,Yes,Yes,No
  Pea,Yes,Yes,No
  Peachetc,Yes,Yes,No
  Pear,Yes,Yes,No
  Pepper,Yes,Yes,No
  Peppermint,Yes,Yes,No
  Persimmon,Yes,Yes,No
  Pigeonpea,Yes,Yes,No
  Pimento,Yes,Yes,No
  Pineapple,Yes,Yes,No
  Pistachio,Yes,Yes,No
  Plantain,Yes,Yes,No
  Plum,Yes,Yes,No
  Popcorn,Yes,Yes,No
  Poppy,Yes,Yes,No
  Potato,Yes,Yes,Yes
  Pulsenes,Yes,Yes,No
  Pumpkinetc,Yes,Yes,No
  Pyrethrum,Yes,Yes,No
  Quince,Yes,Yes,No
  Quinoa,Yes,Yes,No
  Ramie,Yes,Yes,No
  Rapeseed,Yes,Yes,No
  Raspberry,Yes,Yes,No
  Rice,Yes,Yes,Yes
  Rootnes,Yes,Yes,No
  Rubber,Yes,Yes,No
  Rye,Yes,Yes,No
  Ryefor,Yes,Yes,No
  Safflower,Yes,Yes,No
  Sesame,Yes,Yes,No
  Sisal,Yes,Yes,No
  Sorghum,Yes,Yes,No
  Sorghumfor,Yes,Yes,No
  Soybean,Yes,Yes,Yes
  Sourcherry,Yes,Yes,No
  Spicenes,Yes,Yes,No
  Spinach,Yes,Yes,No
  Stonefruitnes,Yes,Yes,No
  Strawberry,Yes,Yes,No
  Stringbean,Yes,Yes,No
  Sugarbeet,Yes,Yes,Yes
  Sugarcane,Yes,Yes,Yes
  Sugarnes,Yes,Yes,No
  Sunflower,Yes,Yes,Yes
  Swedefor,Yes,Yes,No
  Sweetpotato,Yes,Yes,No
  Tangetc,Yes,Yes,No
  Taro,Yes,Yes,No
  Tea,Yes,Yes,No
  Tobacco,Yes,Yes,No
  Tomato,Yes,Yes,No
  Triticale,Yes,Yes,No
  Tropicalnes,Yes,Yes,No
  Tung,Yes,Yes,No
  Turnipfor,Yes,Yes,No
  Vanilla,Yes,Yes,No
  Vegetablenes,Yes,Yes,No
  Vegfor,Yes,Yes,No
  Vetch,Yes,Yes,No
  Walnut,Yes,Yes,No
  Watermelon,Yes,Yes,No
  Wheat,Yes,Yes,Yes
  Yam,Yes,Yes,No
  Yautia,Yes,Yes,No

Fertilizer Units
----------------

Band 1: Kg/ha

Band 2: Precision

* any previous number + .25 = any one of the previous data types but scaling of application rates was maxed out at a doubling when trying to match the FAO consumption


Appendix II - Statistics
========================

Climate Bin Fertilizer
----------------------


Climate Bin Correlation Coefficient
-----------------------------------
