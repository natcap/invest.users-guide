.. _ucm:

*******************
Urban Cooling Model
*******************

Summary
=======

Urban heat mitigation (HM) is a priority for many cities that have undergone heat waves in recent years. Vegetation can help reduce the urban heat island (UHI) effect by providing shade, modifying thermal properties of the urban fabric, and increasing cooling through evapotranspiration. This has consequences for the health and wellbeing of citizens through reduced mortality and morbidity, increased comfort and productivity, and the reduced need for air conditioning (A/C). The InVEST urban cooling model calculates an index of heat mitigation based on shade, evapotranspiration, and albedo, as well as distance from cooling islands (e.g. parks). The index is used to estimate a temperature reduction by vegetation. Finally, the model estimates the value of the heat mitigation service using two (optional) valuation methods: energy consumption and work productivity.

Introduction
============

UHIs affect many cities around the world, with major consequences for human health and wellbeing: high mortality or morbidity during heat waves, high A/C consumption, and reduced comfort or work productivity. The UHI effect, i.e. the difference between rural and urban temperatures, is a result of the unique characteristics of cities due to two main factors: the thermal properties of materials used in urban areas (e.g. concrete, asphalt), which store more heat, and the reduction of the cooling effect (through shade and evapotranspiration) of vegetation.

Natural infrastructure therefore plays a role in reducing UHIs in cities. Using the rapidly-growing literature on urban heat modeling (Deilami et al. 2018), the InVEST urban cooling model estimates the cooling effect of vegetation based on commonly available data on climate, land use/land cover (LULC), and (optionally) A/C use.

The Model
=========

How It Works
------------

Cooling Capacity Index
^^^^^^^^^^^^^^^^^^^^^^

The model first computes the cooling capacity (CC) index for each pixel based on local shade, evapotranspiration, and albedo. This approach is based on the indices proposed by Zardo et al. 2017 and Kunapo et al. 2018, to which we add albedo, an important factor for heat reduction.
The shade factor ('shade') represents the proportion of tree canopy (≥2 m in height) associated with each land use/land cover (LULC) category. Its value is comprised between 0 and 1.
The evapotranspiration index (ETI) represents a normalized value of potential evapotranspiration, i.e. the evapotranspiration from vegetation (or evaporation from soil, for unvegetated areas). It is calculated for each pixel by multiplying the reference evapotranspiration (:math:`ET0`, provided by the user) and the crop coefficient (:math:`Kc` , associated with the pixel's LULC type), and dividing by the maximum value of the :math:`ET0` raster in the area of interest, :math:`ETmax`.:

.. math:: ETI = \frac{K_c \cdot ET0}{ET_{max}}
    :label: eti

Note that this equation assumes that vegetated areas are sufficiently irrigated (although Kc values can be reduced to represent water-limited evapotranspiration).

The albedo factor is a value between 0 and 1 representing the proportion of solar radiation reflected by the LULC type (Phelan et al. 2015).

The model combines the three factors in the CC index:

.. math:: CC_i = 0.6 \cdot shade + 0.2\cdot albedo + 0.2\cdot ETI
    :label: coolingcapacity_factors

The recommended weighting (0.6; 0.2; 0.2) is based on empirical data and reflects the higher impact of shading compared to evapotranspiration. For example, Zardo et al. 2017 report that "in areas smaller than two hectares [evapotranspiration] was assigned a weight of 0.2 and shading of 0.8. In areas larger than two hectares the weights were changed to 0.6 and 0.4, for [evapotranspiration] and shading respectively". In the present model, we propose to disaggregate the effects of shade and albedo in equation (83), and give albedo equal weight to ETI based on the results by Phelan et al. 2015 (see Table 2 in their study showing that vegetation and albedo have similar coefficients).

Note: alternative weights can be manually entered by the user to test the sensitivity of model outputs to this parameter (or if local knowledge is available).

Optionally, the model can consider another factor, intensity (:math:`building.intensity` for a given landcover classification), which captures the vertical dimension of built infrastructure. Building intensity is an important predictor of nighttime temperature since heat stored by buildings during the day is released during the night. To predict nighttime temperatures, users need to provide the building intensity factor for each land use class in the Biophysical Table and the model will change equation :math:numref:`coolingcapacity_factors` to:

.. math:: CC_i = 1 - building.intensity
    :label: coolingcapacity_intensity


Urban Heat Mitigation Index (Effect of Large Green Spaces)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To account for the cooling effect of large green spaces (>2 ha) on surrounding areas (see discussion in Zardo et al. 2017 and McDonald et al. 2016), the model calculates the urban HM index: HM is equal to CC if the pixel is unaffected by any large green spaces, but otherwise set to a distance-weighted average of the CC values from the large green spaces and the pixel of interest.

To do so, the model first computes the area of green spaces within a search distance :math:`d_{cool}` around each pixel (:math:`GA_i`), and the CC provided by each park (:math:`CC_{park_i}`):

.. math:: {GA}_{i}=cell_{area}\cdot\sum_{j\in\ d\ radius\ from\ i} g_{j}
    :label: [3a]

.. math:: CC_{park_i}=\sum_{j\in\ d\ radius\ from\ i} g_j \cdot CC_j \cdot e^{\left( \frac{-d(i,j)}{d_{cool}} \right)}
    :label: [3b]

where :math:`cell_{area}` is the area of a cell in ha, :math:`g_j` is 1 if pixel :math:`j` is green space or 0 if it is not, :math:`d(i,j)` is the distance between pixels :math:`i` and :math:`j`, :math:`d_{cool}` is the distance over which a green space has a cooling effect, and :math:`CC_{park_i}` is the distance weighted average of the CC values attributable to green spaces. (Note that LULC classes that qualify as "green spaces" are determined by the user with the parameter 'green_area' in the Biophysical Table, see Input table in Section 3.) Next, the HM index is calculated as:

.. math:: HM_i = \begin{Bmatrix}
        CC_i & if & CC_i \geq CC_{park_i}\ or\ GA_i < 2 ha \\
        CC_{park_i} & & otherwise
        \end{Bmatrix}
    :label: [4]

Air Temperature Estimates
^^^^^^^^^^^^^^^^^^^^^^^^^

To estimate heat reduction throughout the city, the model uses the (city-scale) UHI magnitude, :math:`UHI_{max}`. Users can obtain UHI values from local literature or global studies: for example, the Global Surface UHI Explorer developed by the University of Yale, provides estimates of annual, seasonal, daytime, and nighttime UHI (https://yceo.users.earthengine.app/view/uhimap).
Note that UHI magnitude is defined for a specific period (e.g. current or future climate) and time (e.g. nighttime or daytime temperatures). The selection of period and time will affect the service quantification and valuation.

Air temperature without air mixing :math:`T_{air_{nomix}}` is calculated for each pixel as:

.. math:: T_{air_{nomix},i}=T_{air,ref} + (1-HM_i)\cdot UHI_{max}
    :label: [5]

Where :math:`T_{air,ref}` is the rural reference temperature and :math:`UHI_{max}` is the maximum magnitude of the UHI effect for the city (or more precisely, the difference between :math:`T_{air,ref}` and the maximum temperature observed in the city).

Due to air mixing, these temperatures average spatially. Actual air temperature (with mixing), :math:`T_{air}`, is derived from :math:`T_{air_{nomix}}` using a Gaussian function with kernel radius :math:`r`, defined by the user.

For each area of interest (which is a vector GIS layer provided by the user), we calculate average temperature and temperature anomaly :math:`(T_{air,i} - T_{air,ref})`.

Value of Heat Reduction Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value of temperature reduction can be assessed in at least three ways:

    i) energy savings from reduced A/C electricity consumption;
    ii) gain in work productivity for outdoor workers;
    iii) decrease in heat-related morbidity and mortality.

The model provides estimates of (i) energy savings and (ii) work productivity based on global regression analyses or local data.

**Energy savings:** the model uses a relationship between energy consumption and temperature (e.g. summarized by Santamouris et al. 2015) to calculate energy savings and associated costs for a building :math:`b`:

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}})
    :label: energy_savings_kwh

Where:

    * :math:`consumption.increase(b)` (kWh/° C/:math:`m^2`) is the local estimate of the energy consumption increase per each degree of temperature per square meter of the building footprint, for building category :math:`b`.
    * :math:`T_{air,MAX}` (° C) is the maximum temperature over the landscape :math:`(T_{air,ref} + UHI_{max})`;
    * :math:`\overline{T_{air,MAX} - T_{air,i}}` (° C) is the average difference in air temperature for building :math:`b`, with :math:`T_{air,i}` modeled in the previous steps.

If costs are provided for each building category, equation :math:numref:`energy_savings_kwh` is replaced by equation :math:numref:`energy_savings_dollars`

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}}) \cdot cost(b)
    :label: energy_savings_dollars

Where:

    * :math:`cost(b)` is the estimate of energy cost per kWh for building category :math:`b`. Note that this is very likely to be equal for all buildings.

To calculate total energy savings, we sum the pixel-level values over the area of interest.

**Work Productivity:** the model converts air temperature into Wet Bulb Globe Temperature (WBGT) to calculate the impacts of heat on work productivity. WBGT takes into account humidity, and can be estimated from standard meteorological data in the following way (American College of Sports Medicine, 1984, Appendix I):

.. math:: WBGT_i = 0.567 \cdot T_{air,i} + 0.393 \cdot e_i + 3.94
    :label: [7]

Where:

    * :math:`T_{air}` = temperature provided by the model (dry bulb temperature (° C))
    * :math:`e_i` = water vapor pressure (hPa)

Vapor pressure is calculated from temperature and relative humidity using the equation:

.. math:: e_i = \frac{RH}{100} \cdot 6.105 \cdot e^{\left ( 17.27 \cdot \frac{T_{air,i}}{(237.7 + T_{air,i})} \right )}
    :label: [8]

Where:

    * :math:`RH` = average Relative Humidity (%) provided by the user

For each pixel, the model computes the estimated loss in productivity (%) for two work intensities: "light work" and "heavy work" (based on rest time needed at different work intensities, as per Table 2 in Kjellstrom et al. 2009):

.. math:: Loss.light.work_i = \begin{Bmatrix}
        0 & if & WBGT < 31.5\\
        25 & if & 31.5 \leq WBGT < 32.0 \\
        50 & if & 32.0 \leq WBGT < 32.5 \\
        75 & if & 32.5 \leq WBGT \\
        \end{Bmatrix}
    :label: [9a]

.. math:: Loss.heavy.work_i = \begin{Bmatrix}
        0 & if & WBGT < 27.5\\
        25 & if & 27.5 \leq WBGT < 29.5 \\
        50 & if & 29.5 \leq WBGT < 31.5 \\
        75 & if & 31.5 \leq WBGT \\
        \end{Bmatrix}
    :label: [9b]

Here, "light work" corresponds to approximately 200 Watts metabolic rate, i.e. office desk work and service industries, and "heavy work" corresponds to 400 W, i.e. construction or agricultural work.
If city-specific data on distribution of gross labor sectors are not available, the user can estimate the working population of the city in 3 sectors (service, industry, agriculture) using national-level World Bank data (e.g. "employment in industry, male (%)" and similar). Loss of work time for a given temperature can be calculated using the resting times in Table 2 (Kjellstrom et al. 2009) and the proportion of working population in different sectors. If local data are available on average hourly salaries for the different sectors, these losses in work time can be translated into monetary losses.

Finally, for "light work", note that A/C prevalence can play a role. If most office buildings are equipped with A/C, the user might want to reduce the loss of work time for the service sector by the same proportion as A/C prevalence.

Limitations and Simplifications
===============================

Due to the simplifications described above, the model presents a number of limitations which are summarized here.

CC index: the CC index relies on empirical weights, derived from a limited number of case studies, which modulate the effect of key factors contributing to the cooling effect (equation (83)). This weighting step comprises high uncertainties, as reviewed in Zardo et al. 2017. To characterize and reduce this uncertainty, users can test the sensitivity of the model to these parameters or conduct experimental studies that provide insights into the relative effects of shade, albedo, and evapotranspiration.

Effect of large parks and air mixing: two parameters capture the effect of large green spaces and air mixing ( :math:`d_{cool}` and :math:`r`). The value of these parameters is difficult to derive from the literature as they vary with vegetation properties, climate (effect of large green spaces), and wind patterns (air mixing). Similar to CC, users can characterize and reduce these uncertainties by testing the sensitivity of the model to these parameters and comparing spatial patterns of temperature estimated by the model with observed or modeled data (see Bartesaghi et al. 2018 and Deilami et al. 2018 for additional insights into such comparisons).

Valuation options: the valuation options currently supported by the model are related to A/C energy consumption and outdoor work productivity. For A/C energy consumption, users need to assess A/C prevalence, and reduce estimates accordingly (i.e. reduce energy consumption proportionally to actual use of A/C).

Valuation of the health effects of urban heat is not currently included in the model, despite their importance (McDonald et al. 2016). This is because these effects vary dramatically across cities and it is difficult to extrapolate current knowledge based predominantly in the Global North (Campbell et al. 2018). Possible options to obtain health impact estimates include:

* using global data from McMichael et al. 2003, who use a linear relationship above a threshold temperature to estimate the annual attributable fraction of deaths due to hot days or,
* for applications in the US, a methodology was developed based on national-scale relationships between mortality and temperature change: see McDonald et al. 2016.

Gasparrini et al. 2014 break down the increase in mortality attributable to heat for 384 cities in 13 countries. :math:`T_air` output from the InVEST model could be used to determine the mortality fraction attributable to heat (first determine in which percentile :math:`T_{air,i}` falls, then use Table S3 or Table S4 in the appendix).

Data Needs
==========

- :investspec:`urban_cooling_model workspace_dir`

- :investspec:`urban_cooling_model results_suffix`

- :investspec:`urban_cooling_model lulc_raster_path` The model will use the resolution of this layer to resample all outputs. The resolution should be small enough to capture the effect of green spaces in the landscape, although LULC categories can comprise a mix of vegetated and non-vegetated covers (e.g. "residential", which may have 30% canopy cover).

- :investspec:`urban_cooling_model biophysical_table_path`

  Columns:

  - :investspec:`urban_cooling_model biophysical_table_path.columns.lucode`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.kc`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.green_area` Green areas larger than 2 hectares have an additional cooling effect.
  - :investspec:`urban_cooling_model biophysical_table_path.columns.shade`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.albedo`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.building_intensity`

- :investspec:`urban_cooling_model ref_eto_raster_path` These values can be for a specific date or monthly values can be used as a proxy.

- :investspec:`urban_cooling_model aoi_vector_path` The AOI(s) will typically be city or neighborhood boundaries.

- :investspec:`urban_cooling_model green_area_cooling_distance` This is :math:`d_{cool}` in equation :eq:`[3b]`. Recommended value: 450 m.

- :investspec:`urban_cooling_model t_ref` This is :math:`T_{air,ref}` in equation :eq:`[5]`. This could be nighttime or daytime temperature, for a specific date or an average over several days. The results will be given for the same period of interest.

- :investspec:`urban_cooling_model uhi_max` This is :math:`UHI_{max}` in equation :eq:`[5]`.

- :investspec:`urban_cooling_model t_air_average_radius` Recommended value range for initial run: 500 m to 600 m; see Schatz et al. 2014 and Londsdorf et al. 2021.

- :investspec:`urban_cooling_model cc_method`

- :investspec:`urban_cooling_model building_vector_path`

  Field:

  - :investspec:`urban_cooling_model building_vector_path.fields.type`

- :investspec:`urban_cooling_model do_energy_valuation`
- :investspec:`urban_cooling_model do_productivity_valuation`

- :investspec:`urban_cooling_model energy_consumption_table_path`

  Columns

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.type`
  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.consumption`

    .. note::
       The **consumption** value is per unit of *footprint* area, not floor area. This value must be adjusted for the average number of stories for structures of this type.

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.cost` The values in this column are very likely to be the same for all building types.

- :investspec:`urban_cooling_model avg_rel_humidity`

- :investspec:`urban_cooling_model cc_weight_shade`
- :investspec:`urban_cooling_model cc_weight_albedo`
- :investspec:`urban_cooling_model cc_weight_eti`

Interpreting Results
====================

* hm_[Suffix].tif: The calculated HMI.
* uhi_results_[Suffix].shp: A copy of the input vector "Area of Interest" with the following additional fields:
    * "avg_cc" - Average CC value (-).
    * "avg_tmp_v" - Average temperature value (degC).
    * "avg_tmp_an" - Average temperature anomaly (degC).
    * "avd_eng_cn" - (optional) Avoided energy consumption (kWh or $ if optional energy ``cost`` input column was provided in the Energy Consumption Table).
    * "avg_wbgt_v" - (optional) Average WBGT (degC).
    * "avg_ltls_v" - (optional) Light work productivity loss (%).
    * "avg_hvls_v" - (optional) Heavy work productivity loss (%).
* buildings_with_stats_[Suffix].shp: A copy of the input vector "Building Footprints" with the following additional fields:
    * "energy_sav" - Energy savings value (kWh or $ if optional energy ``cost`` input column was provided in the Energy Consumption Table). Savings are relative to a theoretical scenario where the city contains NO natural areas nor green spaces; where CC = 0 for all LULC classes.
    * "mean_t_air" - Average temperature value in building (degC).

The intermediate folder contains additional model outputs:

* cc_[Suffix].tif: Raster of CC values.
* T_air_[Suffix].tif: Raster of estimated air temperature values.
* T_air_nomix_[Suffix].tif: Raster of estimated air temperature values prior to air mixing (i.e. before applying the moving average algorithm).
* eti_[Suffix].tif: Raster of values of actual evapotranspiration (reference evapotranspiration times crop coefficient "Kc").
* wbgt_[Suffix].tif: Raster of the calculated WBGT.
* reprojected_aoi_[Suffix].shp: The user-defined Area of Interest, reprojected to the Spatial Reference of the LULC.
* reprojected_buildings_[Suffix].shp: The user-defined buildings vector, reprojected to the Spatial Reference of the LULC.

Appendix: Data Sources and Guidance for Parameter Selection
===========================================================

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

:ref:`Kc <kc>`
--------------

:ref:`Reference Evapotranspiration <et0>`
-----------------------------------------

:ref:`Building Footprints <buildings>`
--------------------------------------

Albedo
------
Albedo for urban built infrastructure can be found in local microclimate literature. Deilami et al. 2018 and Bartesaghi et al. 2018 provide a useful review. Stewart and Oke (2012) provide value ranges for typical LULC categories.

Green Area Maximum Cooling Distance
-----------------------------------
Distance (meters) over which large urban parks (>2 ha) have a cooling effect. See a short review in Zardo et al. 2017, including a study that reports a cooling effect at a distance five times tree height. In the absence of local studies, an estimate of 450m can be used.

Baseline Air Temperature
------------------------
Rural reference temperature (°C) can be obtained from local temperature stations or global climate data.

Magnitude of the UHI Effect
---------------------------
i.e. the difference between the maximum temperature in the city and the rural reference (baseline) air temperature. In the absence of local studies, users can obtain values from a global study conducted by Yale: https://yceo.users.earthengine.app/view/uhimap

Air Temperature Maximum Blending Distance
-----------------------------------------
Search radius (meters) used in the moving average to account for air mixing. A recommended initial value range of 500m to 600m can be used based on preliminary tests in pilot cities (Minneapolis-St Paul, USA and Paris, France). This parameter can be used as a calibration parameter if observed or modeled temperature data are available.

:ref:`buildings`
----------------

Energy Consumption Table
------------------------
Energy consumption (kWh/°C) varies widely across countries and cities. Santamouris et al. 2015 provide estimates of the energy consumption per °C for a number of cities worldwide. For the United States (US), EPA EnergyStar Portfolio Manager data may provide categorical averages as well as data for specific buildings: https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/understand-metrics/what-energy Note: If A/C prevalence is low, this valuation metric should not be used as it assumes that energy costs will increase with higher temperatures (and greater A/C use). A/C prevalence data for the US can be obtained from the American Housing Survey: https://www.census.gov/programs-surveys/ahs.html

Average Relative Humidity
-------------------------
Average relative humidity (%) during heat waves can be obtained from local temperature stations or global climate data


FAQs
====

* What is the output resolution?

    Model outputs are of two types: rasters and vectors. Rasters have the same resolution as the LULC input (all other raster inputs are resampled to the same resolution).

* Why aren't the health impacts calculated by the model?

    The effects of heat on human health vary dramatically across cities and it is difficult to develop a generic InVEST model that accurately captures and quantifies these for all cities. See the point about "Valuation of the health effects of urban heat" in the model Limitations section for additional details and pathways to assess the health impacts of urban heat mitigation.

References
==========

Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56. FAO, Rome, Italy.

American College of Sports Medicine (1984). Prevention of Thermal Injuries During Distance Running. Medicine and Science in Sports & Exercise, 16(5), ix-xiv. https://doi.org/10.1249/00005768-198410000-00017

Bartesaghi, C., Osmond, P., & Peters, A. (2018). Evaluating the cooling effects of green infrastructure : A systematic review of methods, indicators and data sources. Solar Energy, 166(February), 486-508. https://doi.org/10.1016/j.solener.2018.03.008

Campbell, S., Remenyi, T. A., White, C. J., & Johnston, F. H. (2018). Heatwave and health impact research: A global review. Health & Place, 53, 210-218. https://doi.org/https://doi.org/10.1016/j.healthplace.2018.08.017

Deilami, K., Kamruzzaman, M., & Liu, Y. (2018). Urban heat island effect: A systematic review of spatio-temporal factors, data, methods, and mitigation measures. International Journal of Applied Earth Observation and Geoinformation, 67, 30-42. https://doi.org/https://doi.org/10.1016/j.jag.2017.12.009

Gasparrini, A., Guo, Y., Hashizume, M., Lavigne, E., Zanobetti, A., Schwartz, J., Tobias, A., Tong, S., Rocklöv, J., Forsberg, B., Leone, M., De Sario, M., Bell, M. L., Guo, Y. L., Wu, C., Kan, H., Yi, S., Coelho, M. d., Saldiva, P. H., Honda, Y., Kim, H., & Armstrong, B. (2015). Mortality risk attributable to high and low ambient temperature: a multicountry observational study. The lancet, 386(9991), 369-375. https://doi.org/10.1016/S0140-6736(14)62114-0

Kjellstrom, T., Holmer, I., & Lemke, B. (2009). Workplace heat stress, health and productivity - an increasing challenge for low and middle-income countries during climate change. Global Health Action, 2, 10.3402/gha.v2i0.2047. https://doi.org/10.3402/gha.v2i0.2047

Kunapo, J., Fletcher, T. D., Ladson, A. R., Cunningham, L., & Burns, M. J. (2018). A spatially explicit framework for climate adaptation. Urban Water Journal, 15(2), 159-166. https://doi.org/10.1080/1573062X.2018.1424216

Londsdorf, E.V., Nootenboom, C., Janke, B., & Horgan, B.P. (2021). Assessing urban ecosystem services provided by green infrastructure: Golf courses in the Minneapolis-St. Paul metro area. Landscape and Urban Planning, 208. https://doi.org/10.1016/j.landurbplan.2020.104022

McDonald, R. I., Kroeger, T., Boucher, T., Wang, L., & Salem, R. (2016). Planting Healthy Air: A global analysis of the role of urban trees in addressing particulate matter pollution and extreme heat. CAB International, 128-139.

McMichael, A. J., Campbell-Lendrum, D. H., Corvalán, C. F., Ebi, K. L., Githeko, A. k., Scheraga, J. D., & Woodward, A. (2003). Climate change and human health: risks and responses. World Health Organization. Geneva, Switzerland.

Phelan, P. E., Kaloush, K., Miner, M., Golden, J., Phelan, B., Iii, H. S., & Taylor, R. A. (2015). Urban Heat Island : Mechanisms , Implications , and Possible Remedies. Annual Review of Environment and Resources, 285-309. https://doi.org/10.1146/annurev-environ-102014-021155

Santamouris, M., Cartalis, C., Synnefa, A., & Kolokotsa, D. (2015). On the impact of urban heat island and global warming on the power demand and electricity consumption of buildings - A review. Energy & Buildings, 98, 119-124. https://doi.org/10.1016/j.enbuild.2014.09.052

Shatz, J. & Kucharik, C.J. (2014). Seasonality of the Urban Heat Island Effect in Madison, Wisconsin. Journal of Applied Meterology and Climatology, 53(10), 2371-2386. https://doi.org/10.1175/JAMC-D-14-0107.1

Stewart, I. D., & Oke, T. R. (2012). Local climate zones for urban temperature studies. American Meteorological Society. https://doi.org/10.1175/BAMS-D-11-00019.1

Zardo, L., Geneletti, D., Prez-soba, M., & Eupen, M. Van. (2017). Estimating the cooling capacity of green infrastructures to support urban planning. Ecosystem Services, 26, 225-235. https://doi.org/10.1016/j.ecoser.2017.06.016
