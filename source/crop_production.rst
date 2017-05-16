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

Data Needs
==========

 + Both the percentile and regression model require the base Monfreda Dataset which ships with the InVEST installer and can be found at `CropProduction\model_data` in the InVEST data installation directory.

 + A landcover raster used to map pixel values to crop types.

 + A table that maps a crop name to a landcover value.  The crop name must be one of the accepted 175 crops for the percentile model, or 12 for regression.  The table must have column names `crop_name` and `lucode` corresponding to these values.  An example is given below

    ========= ======
    crop_name lucode
    ========= ======
    barley    1
    wheat     20
    soybean   1000
    ========= ======

 Accepted crop names for percentile can be found in the table at `CropProduction\model_data\crop_nutrient.csv` while those for regression can be found in the table at `CropProduction\model_data\crop_fertilization_rates.csv`.

 + An optional polygon shapefile to aggregate results over.  If it is provded, the shapefile must have a keyfield to uniquely identify each polygon, the name of this field must also be provided in the user interface.

Additional Regression Data Needs
--------------------------------

 + Fertilization rate per crop.   This is a CSV table that contains crop names, and application rates for nitrogen, phosphate, and potassium.  An example table is included below

.. csv-table::
  :file: crop_production/crop_fertilization_rates.csv
  :header-rows: 1
  :name: Crop Fertilization Rate Example



Running the Model
=================

**General Parameters**

1. **Workspace Folder**  The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created.  If datasets already exist in the selected folder, they will be overwritten.

2. **Results Suffix (Optional)**  This text will be appended to the end of the output folders to help separate outputs from multiple runs.  Please see the `Interpreting Results`_ section for an example folder structure for outputs.

3. **Lookup Table (CSV)**  The table should contain three columns: a 'name' column, a 'code' column, and an 'is_crop' column.

  =======  ====  =======
  name     code  is_crop
  =======  ====  =======
  other    0     false
  maize    1     true
  soybean  2     true
  rice     3     true
  ...      ...
  =======  ====  =======

4. **Crop Management Scenario Map (Raster)**  A GDAL-supported raster representing a crop management scenario. Each cell value in the raster should be a valid integer code that corresponds to a lulc-class in the Lookup Table file.  The NoData value should be set to a number not existing in the LULC Lookup Table.

  +---+---+
  |int|int|
  +---+---+
  |int|int|
  +---+---+

5. **Global Dataset Folder**  A directory of raster datasets and CSV tables representing climate bins, yields and regressions developed by the Foley lab for this model.  These data are not currently distributed with the InVEST installer and must be downloaded from: http://data.naturalcapitalproject.org/invest_crop_production/

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

    **Crop Climate-Bin Maps (Rasters)**  A set of GDAL-supported rasters representing the climate-bin that a given area of land is located within for each particular crop.  Each raster contains a set of values between 0 and 100.  Zero-values represent areas that do not exist within a climate-bin, such as an ocean.  Values 1 through 100 correspond to particular climate-bins.  The climate-bin maps reside in the 'climate_bin_maps' folder of the provided spatial dataset.

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

6. **Yield Function**  Determines how yield is estimated in the model.

7. **Percentile Column**  Required for Percentile Yield Function.  This input is used to select the column of yield values from the tables in the climate_percentile_yield folder of the global dataset.

8. **Fertilizer Folder (Rasters)**  Required for Regression Yield Function. A set of GDAL-supported rasters representing the amount of Nitrogen (N), Phosphorus (P2O5), and Potash (K2O) applied to each area of land. These maps are required for the regression model yield function and are an optional input for all yield functions when calculating economic returns. Each cell value in the raster should be a non-negative float value representing the amount of fertilizer applied in units of kilograms per hectare (kgs/ha). Each file must be named by their fertilizer (nitrogen, phosphorus, potash) in lowercase, followed by the '.tif' file extension.  The Fertilizer Maps should have the same dimensions and projection as the provided Crop Management Scenario Map.  Global fertilizer datasets are available for download from http://data.naturalcapitalproject.org/invest_crop_production/

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

  **Folder Structure**

  .. code-block:: none

    .
    |-- fertilizer_maps_folder
        |-- nitrogen.tif
        |-- phosphorus.tif
        |-- potash.tif

9. **Irrigation Map (Raster)**  Required for Regression Yield Function. A GDAL-supported raster representing whether irrigation occurs or not. A zero value indicates that no irrigation occurs.  A one value indicates that irrigation occurs.  The Irrigation Map should have the same dimensions and projection as the provided Crop Management Scenario Map.

  +---+---+
  |int|int|
  +---+---+
  |int|int|
  +---+---+

**Parameters for Calculating Nutritional Contents from Production**

10. **Nutrient Contents Table (CSV)**  A CSV table containing information about the nutrient contents of each crop.  The values provided are assumed to be given in relation to one ton of harvest crop biomass.  The 'crop' and 'fraction_refuse' columns must be provided in the table.  The 'fraction_refuse' column is expected to contain a value between 0 and 1 representing the fraction of the harvested crop that is considered refuse and does not contain any nutritional value.

  =======  ===============  ========  ========  ========  ========  ========  ===
  crop     fraction_refuse  protein   lipid     energy    ca        ph        ...
  =======  ===============  ========  ========  ========  ========  ========  ===
  maize     <float>         <float>   <float>   <float>   <float>   <float>   ...
  soybean   <float>         <float>   <float>   <float>   <float>   <float>   ...
  ...       ...             ...       ...       ...       ...       ...       ...
  =======  ===============  ========  ========  ========  ========  ========  ===

**Parameters for Calculating Economic Returns**

11. **Economics Table (CSV)**  A CSV table containing information related to the market price of a given crop and the costs involved with producing that crop.

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
      |-- yield.tif
      |-- nutritional_contents.csv
      |-- financial_analysis.csv

**Outputs**

1. **Crop Yield Map (Raster)** A set of GDAL-supported rasters spatially representing the per-cell yield.  Each cell value in the raster shall be a non-negative float value representing the yield area under the given scenario in units of tons.

  +-----+-----+
  |float|float|
  +-----+-----+
  |float|float|
  +-----+-----+

2. **Nutritional Contents Table (CSV)**

  =======  ===========  ============  ============  ======
  crop     total_yield  (nutrient_a)  (nutrient_b)  (etc.)
  =======  ===========  ============  ============  ======
  maize    <float>      <float>       <float>       ...
  soybean  <float>      <float>       <float>       ...
  ...      ...          ...           ...           ...
  =======  ===========  ============  ============  ======

3. **Financial Analysis Table (CSV)**

  =======  ===========  =======  =======  ========
  crop     total_yield  costs    returns  revenues
  =======  ===========  =======  =======  ========
  maize    <float>      <float>  <float>  <float>
  soybean  <float>      <float>  <float>  <float>
  ...      ...          ...      ...      ...
  =======  ===========  =======  =======  ========

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
