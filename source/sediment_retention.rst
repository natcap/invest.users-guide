.. _sediment_retention:

.. |addbutt| image:: ./shared_images/addbutt.png
             :alt: add
	     :align: middle 
	     :height: 15px

.. |toolbox| image:: ./shared_images/toolbox.jpg
             :alt: toolbox
	     :align: middle 
	     :height: 15px

***********************************************************
Sediment Retention: Avoided Dredging and Water Purification
***********************************************************

Summary
=======

.. figure:: ./sediment_retention_images/lake.jpg
   :align: right
   :figwidth: 270pt

Reservoirs are linked to a number of environmental services, including the generation of energy through reservoir hydropower production, irrigation of crops and recreational activities. Erosion and sedimentation of watersheds can lead to decreased hydropower output, structural damage to reservoirs and other water infrastructure, and flooding. InVEST estimates the capacity of a land parcel to retain sediment using data on geomorphology, climate, vegetation and management practices. These estimates are combined with data on sediment removal costs, reservoir design, and a discount rate to calculate the avoided cost of sediment removal. Limitations of the model include negligence of mass erosion, inadequate information about sediment removal costs, and simplified LULC classifications.
  
Introduction
============

Erosion and sedimentation are natural processes that contribute to healthy ecosystems, but too much may have severe consequences. Excessive erosion can reduce agricultural productivity, increase flooding and pollutant transport, and threaten bridges, railroads and power infrastructure. Erosion can lead to sediment build-up, which strains water infrastructure, such as reservoirs and flood control systems, and increases water treatment costs. Sedimentation is particularly problematic for reservoirs, which are designed to retain sediment as water is released. Regular sediment removal can avoid some of these issues, but this incurs substantial maintenance costs.

The magnitude of sediment transport in a watershed is determined by several factors. Natural variation in soil properties, precipitation patterns, and slope influence patterns of erosion and sediment runoff. Vegetation holds soil in place and captures sediment moving overland.  Accordingly, changes in land management practices that alter vegetation can change the sediment retention capacity of land.

There are many clear examples of the effects of land use and land cover (LULC) change on erosion and sedimentation. For example, forest fires that clear significant areas of vegetation are often followed by mudslides when heavy rains occur (Meyer et al. 2001). After the fire, the vegetation that once held sediment in place no longer exists and the top layers of soil can be carried downstream by overland runoff. Deforestation results in a similar process, although in some cases it may occur on longer time scales. Even in areas where land cover remains the same, a change in land use practice can alter the sediment retention capacity of the landscape. For example, moving from no-till to till agriculture has been shown to increase the rate of soil erosion. The accumulation of sediment as a result of LULC change can cause serious problems, including increased dredging costs that were not anticipated during the original budget designations of reservoir infrastructure. To reduce the damages and costs associated with sedimentation, land, water and reservoir managers require information regarding the extent to which different parts of a landscape contribute to sediment retention, and how land use changes may affect this retention. Such information can support decisions by government agencies, businesses, and NGOs. For example, a power company operating a hydropower reservoir may elect to conserve upstream forests that maintain a sediment retention service if the cost of conserving the forests is less than the costs of reduced hydropower potential, sediment removal, and dam replacement. Maps showing which forest parcels offer the greatest sediment retention benefits would help the power company maximize returns on their investment. InVEST aims to provide this type of information. The outputs from these models will allow planners and managers to consider how LULC change in one area in the watershed can affect sedimentation affecting other locations.

The Model
=========

The Sediment Retention model provides the user with a tool for calculating the average annual soil loss from each parcel of land, determining how much of that soil may arrive at a particular point of interest, estimating the ability of each parcel to retain sediment, and assessing the cost of removing the accumulated sediment on an annual basis. An important determinant of soil retention capacity is land use and land cover. To identify a land parcel's potential soil loss and sediment transport, the InVEST Avoided Reservoir Sedimentation model uses the Universal Soil Loss Equation (USLE) (Wischmeier & Smith 1978) at the pixel scale, which integrates information on LULC patterns and soil properties, as well as a digital elevation model, rainfall and climate data. The pixel-scale calculations allow us to represent the heterogeneity of key driving factors in water yield such as soil type, precipitation, vegetation type, etc. However, the theory we are using as the foundation of this set of models was developed at the subwatershed to watershed scale. We are only confident in the interpretation of these models at the subwatershed scale, so all outputs are summed and/or averaged to the subwatershed scale although the model does provide pixel-scale representations of some outputs for calibration and model-checking purposes.

This model can also be used to value the landscape vis-a-vis maintaining water quality or avoiding reservoir sedimentation. In the water quality maintenance case, the model uses additional information on water quality standards and treatment costs to value the ability of each subwatershed to reduce treatment costs. In the reservoir maintenance case, the model uses additional data on reservoir location and the avoided cost of sediment removal to value a subwatershed's capacity to keep sediment out of reservoirs.

How it works
------------

The InVEST sediment retention model employs the Universal Soil Loss Equation (USLE) from Wischmeier & Smith (1978) at a grid cell scale, together with a grid cell scale sediment retention approach for sediment deposition. The basic grid cell-scale export calculation integrates information on land-use/land-cover (LULC) patterns, soil properties, elevation, rainfall and climate data to estimate soil erosion (USLE) from a grid cell :math:`i`:

.. math:: USLE_{i}=(R \cdot K \cdot L \cdot S \cdot C \cdot P)_{i}

where *R* is the rainfall erosivity, *K* is the soil erodibility factor, *LS* is the slope length-gradient factor, C is the crop-management factor and P is the support practice factor.

Calculation of Potential Soil Loss
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The InVEST model uses raster layers to represent erosivity and erodibility, and a raster layer of land cover to map *C* and *P* factors. The values for crop/vegetation and support practice are assumed equal for all grid cells of identical LULC class, and are held in the LULC parameters table. Other assumptions in the model include:

* Steady state conditions 
* Sediment that enters the channel network leaves the basin during the same year (no carry-over the years).

The *L* and *S* factors are considered to be the most critical parameters of the USLE equation and several researchers (e.g. Quinn et al., 1991; McCool et al., 1989) have made modifications to the original LS factor developed by Foster and Wischmeier (1974). We are adopting the method developed by Desmet and Govers (1996) for two-dimension surface:

.. math:: L_{i}\cdot S_{i}=S_i \frac{(A_{i}+D^2)-A^{m+1}_{i}}{D^{m+2}\cdot x^m_{i}\cdot 22.13^m}

Where

* :math:`S_i` = the slope factor for grid cell calculated as function of slope degree as follows:

 .. math:: S_i=10.8\cdot \sin(\theta)+0.03, \mathrm{where\ slope\ is\ }<9\%

 .. math:: S_i=16.8\cdot \sin(\theta)-0.50, \mathrm{where\ slope\ is\ } \geq 9\%

* :math:`Ai_{i}` = the contributing area (:math:`m^2`) at the inlet of grid cell :math:`i` that is calculated from the D-infinity flow accumulation algorithm.

* :math:`D` = the grid cell linear dimension (m)

* :math:`x_{i}` is a factor for adjusting the flow length across a cell it is equal to :math:`|\sin(\alpha_{i}) + |\cos(\alpha_{i})|` where :math:`\alpha_{i}` is the aspect direction for the grid cell.

.. csv-table::
  :file: sediment_ls_exponent_table.csv
  :header-rows: 1
  :name: The length exponent LS factor *m*
  
Empirically, it was found that the slope length factor calculated from the equations above may overestimate the hydrology on the ground. Some land uses may not generate runoff and many human modified landscapes have features that are hydrologically disconnected from their surroundings by roads, ditches, drainage systems and alike. In such heterogeneous landscapes it is recommended to independently calculate the upslope contributing area and to cap long slope lengths (Desmet and Govers, 1996). In this model we adopt a cap of 333 m as default value as recommended by McCool et al. (1997).

Calculation of upstream Retention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model assumes that the estimated soil loss from USLE is transported to downstream grid cell if the retention capacity of the receiving cell is zero. This retention is an outcome of physical filtration and slowing down of overland flow by vegetation, allowing sediment particles to deposit. Factors such as slope, soil permeability and area also play an important role in sediment transportation and deposition processes. For the InVEST sediment model we abstract this parameter into a per cell retention efficiency factor defined as a function of a landcover code in the biophysical table input.

From here we state the mass balance equation which governs the transport of sediment in the InVEST sediment retention model:

.. math:: S_i = \left(\sum_{j\in\{i_{neighbors}\}}\right)(1-E_i) + USLE_i

The total retained sediment (:math:`sret_x`) is equal to the sum of the sediment retained on the pixel itself due to the :math:`C` and :math:`P` factors as well as the sediment removed through routing filtration.

Consideration of Allowed Loads in Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model provides the option to consider two services associated with the retention of sediments on the landscape; improved water quality and avoided sedimentation of reservoirs. When considering improved water quality, there may be an allowed annual amount of sediment load for the water body of interest. We subtract this annual allowed load in the service step since the benefit from retention of sediment upstream of systems that have annual loads below this threshold. We assume that each pixel on the landscape gets an equal proportion of this allowance in the following calculation:

.. math:: S'\_wq_x = S`_x-wq\_annload

where :math:`S_x` is the total retained sediment from the watershed and :math:`wq_annload` is the annual allowed sediment load.

Likewise, when considering avoided sedimentation of reservoirs, there is usually an engineered reservoir dead volume, or space built in to the reservoir to capture sediment and avoid the loss of reservoir capacity over time. Because this space is specifically constructed to catch sediment and avoid costs associated with dredging, humans do not receive benefit from the landscape's ability to slow erosion until this dead volume is filled. To account for this and avoid over-valuing this service, we subtract any engineered dead volume in the service step. This calculation is made as follows:

.. math:: S'\_dr_x = S`_x-\frac{1.26 dr\_deadvol}{dr\_time}

where :math:`dr\_deadvol` is the engineered dead volume of the reservoir, 1.26 is a constant representing the density of sediment in tons :math:`m^{-3}` and :math:`dr\_time` is the remaining lifetime of the reservoir.

Economic Valuation of Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The valuation model uses the cost of sediment removal entered by the user to determine the avoided cost of dredging and/or water quality treatment. 

The following equation is used to determine the value each subwatershed contributes to reservoir maintenance by helping to avoid erosion.

.. math:: V_x=cost(x)\cdot sret\_sm \cdot \sum^{T-1}_{t=0}\frac{1}{(1+r)^t}
 
:math:`V_x` is the present value of sediment retention on subwatershed *x* over *T* years, where *T* indicates the period of time over which the LULC pattern is constant  (for water quality valuation) or the length of the reservoir life (for dredging valuation), *sret_sm* is  is the total sediment retention adjusted for for either dredging (*sret_sm_dr*) or water quality (*sret_sm_wq*), *cost(s)* is the marginal cost of sediment removal for either the service of dredging or water quality treatment and r is the discount rate. The *cost(s)* may vary across reservoirs or water treatment facilities if different technologies are employed for sediment removal. If this is the case, the user may input reservoir- or plant-specific removal costs. The marginal cost of sediment removal should be measured in units of monetary currency per cubic meter (i.e. $ m\ :sup:`-3`\ ).

Limitations and simplifications
-------------------------------

The accuracy of the sediment retention value is limited by the quality of information of the cost of sediment removal and the user's ability to calibrate it with actual sedimentation data. The model allows for a calibration constant to be applied and adjusted via the Sediment Delivered output. This can improve the model, but only if the user has access to reliable sedimentation data for the watershed(s) of interest.

The USLE method is a standard method to calculate soil loss, but it has several limitations:

* USLE predicts erosion from sheet wash alone (erosion from plains in gentle slopes) (FAO 2002).  

* Rill, gullies and/or stream-bank erosion/deposition processes are not included in this model.  Moreover, the relationship between rainfall intensity and kinetic energy may not hold in mountainous areas because it has only been tested in the American Great Plains. Finally, the equation considers only the individual effect of each variable.

* The model relies on retention or filtration efficiency values for each LULC type. However, there are often few data available locally for filtration rates associated with local LULC types. Data from other regions may be applied in these cases, but may misrepresent filtration by local LULC types.

* The model may not accurately depict the sedimentation process in the watershed of interest since the model is based on parametrization of several different equations and each parameter describes a stochastic process. Due to the uncertainty inherent in the processes being modelled, it is not recommended to make large-scale area decisions based on a single run of the model. Rather, the model functions best as an indicator of how land use changes may affect the cost of sediment removal, and, like any model, is only as accurate as the available input data. A more extensive study may be required for managers to calculate a detailed cost-benefit analysis for each reservoir site.


Data needs
==========

This section outlines the specific data used by the model. See the Appendix for detailed information on data sources and pre-processing.  Note that all GIS inputs must be in the same projection and in linear meter units for accurate results.  Additionally, on a first run or default run of the model, the user interface will be populated with sample datasets for all the following parameters.

1.  **Digital elevation model (DEM) (required)**.  A GIS raster dataset with an elevation value for each cell. Make sure the DEM is corrected by filling in sinks, and if necessary 'burning' hydrographic features into the elevation model (recommended when you see unusual streams.) To ensure proper flow routing, the DEM should extend beyond the watersheds of interest, rather than being clipped to the watershed edge.
 
2. **Rainfall erosivity index (R) (required)**. R is a GIS raster dataset, with an erosivity index value for each cell. This variable depends on the intensity and duration of rainfall in the area of interest. The greater the intensity and duration of the rain storm, the higher the erosion potential. The erosivity index is widely used, but in case of its absence, there are methods and equations to help generate a grid using climatic data.  The unites on the index values are MJ*mm*(ha*h*yr)\ :sup:`-1`\. 

3. **Soil erodibility (K) (required)**. K is a GIS raster dataset, with a soil erodibility value for each cell. Soil erodibility, K, is a measure of the susceptibility of soil particles to detachment and transport by rainfall and runoff.

4. **Land use/land cover (LULC) (required)**. LULC is a GIS raster dataset, with an integer LULC code for each cell.

5. **Watersheds (required)**. A shapefile of polygons. This is a layer of watersheds such that each watershed contributes to a point of interest where water quality will be analysed.

6. **Biophysical table (required)**. A .csv table containing model information corresponding to each of the land use classes. Each row is a land use/land cover class and columns should be named and defined as follows:

	a. *lucode (Land use code)*: Unique integer for each LULC class (e.g., 1 for forest, 3 for grassland, etc.), must match the LULC raster input.
	
	b. *LULC_desc*: Descriptive name of land use/land cover class (optional) 
	
	c. *usle_c*: Cover-management factor for the USLE, a floating point value between 0 and 1.

	d. *usle_p*: Support practice factor for the USLE, a floating point value between 0 and 1.
	
	e. *sedret_eff*: The sediment retention value for each LULC class, as a floating point value 0 and 1.  This value is a percent per pixel area.

7. **Threshold flow accumulation (required)**. The number of upstream cells that must flow into a cell before it's considered part of a stream which is used to classify streams in the DEM.  This value also needs to be well estimated in watersheds where ditches are present. This threshold expresses where hydraulic routing is discontinued, retention stops, and the remaining pollutant will be exported to the stream.

8. **Sediment threshold table (required)** A .csv table containing annual sediment load threshold information for each of the reservoirs. There must be one row for each watershed in the Watersheds layer. Each row is a reservoir or structure that corresponds to the watersheds layer and each column contains a different attribute of each reservoir and must be named as follows:

	a. *ws_id (watershed ID)*: Unique integer value for each reservoir, which must correspond to values in the Watersheds layer. 
	
	b. *dr_time*: Integer time period corresponding to the remaining designed lifetime of the reservoir (if assessing avoided sedimentation) or the expected time period over which the land use will remain relatively constant. For reservoir sedimentation, if you are using an LULC map for the year 2000 and a reservoir of interest was designed in 1950 for a 100-year lifetime, the time period entered here should be 50 years. 
	
	c. *dr_deadvol*: The volume of water below the turbine. It is a design dimension below which water is not available for any use and it's designed to store (deposit) sediment without hindering turbine and reservoir hydropower functions. Used for calculating service in biophysical terms and valuing retention for dredging.  Given in cubic meters. 
	
	d. *wq_annload*: Allowed annual sediment loading, used for valuing sediment retention for water quality.  This could be set by national or local water quality standards. Given in metric tons.

9. **Sediment valuation table (required for valuation)**. A .csv table containing valuation information for each of the reservoirs. There must be one row for each watershed in the Watersheds layer. Each row in the table is a reservoir or structure that corresponds to the watersheds shapefile and each column contains a different attribute of each reservoir and must be named as follows:

	a. *ws_id (watershed ID)*: Unique integer value for each reservoir, which must correspond to values in the Watersheds layer. 
	
	b. *dr_cost*: Cost of sediment dredging in $ (Currency) / m\ :sup:`3`\  removed.  Floating point value.  Used for valuing sediment retention for dredging. 
	
	c. *dr_time*: Integer time period to be used in calculating Present Value (PV) of removal costs.  This time period should be the remaining designed lifetime of the structure.  For instance, if you are using an LULC map for the year  2000 and a reservoir of interest was designed in 1950 for a 100-year lifetime, the time period entered here 	should be 50 years.  Used for valuing sediment retention for dredging. 
	
	d. *dr_disc*: The rate of discount over the time span, used in net present value calculations.  Used for valuing sediment retention for dredging. Floating point value. 
	
	e. *wq_cost*: Cost of  removing sediment for water quality in $ (Currency) / m\ :sup:`3`\  removed.  Floating point value.  Used for valuing sediment retention for water quality. 
	
	f. *wq_time*: Integer time period to be used in calculating Present Value (PV) of removal costs.  This time period should be the remaining designed lifetime of the structure.  For instance, if you are using an LULC map for the year  2000 and a reservoir of interest was designed in 1950 for a 100-year lifetime, the time period entered here should be 50 years.  Used for valuing sediment retention for water quality. 
	
	g. *wq_disc*: The rate of discount over the time span, used in net present value calculations.  Used for valuing sediment retention for water quality. Floating point value.

 
Running the Model
=================

To launch the Sediment model navigate to the Windows Start Menu -> All Programs -> InVEST +VERSION+ -> Sediment Retention.  The interface does not require a GIS desktop, although the results will need to be explored with any GIS tool including ArcGIS, QuantumGIS, and others.

Interpreting Results
=====================

The following is a short description of each of the outputs from the Sediment Retention model.  Final results are found in the *output*  folders within the user defined *Workspace* specified for this model.

* **Parameter log**: Each time the model is run, a text (.txt) file will appear in the *Output* folder. The file will list the parameter values for that run and will be named according to the service, the date and time, and the suffix. 

* **output\\usle.tif** (tons/pixel): Total potential soil loss per pixel in the original land cover calculated from the USLE equation.

* **output\\rkls.tif** (tons/pixel): Total potential soil loss per pixel in the original land cover without the C or P factors applied from the RKLS equation.

* **output\\on_pixel_retention.tif** (tons/pixel): Total sediment retained due to the direct effect of landcover.  Effectively RKLS-USLE.

* **output\\upstream_on_pixel_retention.tif** (tons/pixel): Total sediment retained on the landscape due to sediment filtration through landcover.  Effectively the downstream filtered value of USLE.

* **output\\sed_export.tif** (tons/pixel): The total amount of sediment exported from each pixel that reaches the stream.

* **output\\v_stream.tif** (pixel mask): The pixel level mask of the calculated stream network, useful for interpreting and debugging pixel level output.

* **output\\watershed_outputs.shp**: Table containing biophysical values for each watershed, with fields as follows:

	* *sed_export* (tons/watershed): Total amount of sediment exported to the stream per watershed. This should be compared to any observed sediment loading at the outlet of the watershed. Knowledge of the hydrologic regime in the watershed and the contribution of the sheetwash yield into total sediment yield help adjust and calibrate this model.
	
	* *sed_ret_dr/sed_ret_wq* (tons/watershed): Effective amount of sediment retained by the landscape in each watershed adjusted for the allowed load of dredging (dr) or water quality (wq).
    
    * *upret_tot* (tons/watershed): Amount of sediment retained by the landscape in each watershed.
    
    * *usle_tot* (tons/watershed): Total amount of potential soil loss in each watershed calculated by the USLE equation.
    
    * *sed_val_dr/sed_val_wq* (currency/timespan): This is the value of the sediment retention service in the watershed.  These values only exist if valuation has been selected for the model run.  It is adjusted for the allowed load in dredging (dr) or water quality (wq).

Appendix: data sources
======================

This is a rough compilation of data sources and suggestions about finding, compiling, and formatting data. This section should be used for ideas and suggestions only. We will continue to update this section as we learn about new data sources and methods.

1. **Digital elevation model (DEM)**

 DEM data is available for any area of the world, although at varying resolutions. 
 
 Free raw global DEM data is available on the internet from the World Wildlife Fund - http://worldwildlife.org/pages/hydrosheds
 
 NASA provides free global 30m DEM data at http://asterweb.jpl.nasa.gov/gdem-wist.asp 
 
 As does the USGS - http://eros.usgs.gov/#/Find_Data/Products_and_Data_Available/Elevation_Products and http://hydrosheds.cr.usgs.gov/.   
 
 Or, it may be purchased relatively inexpensively at sites such as MapMart (www.mapmart.com).  
 
 The DEM resolution is a very important parameter depending on the project's goals. For example, if decision makers need information about impacts of roads on ecosystem services then fine resolution is needed. And the hydrological aspects of the DEM used in the model must be correct. Please see the Working with the DEM section of this manual for more information. 

2. **Rainfall erosivity index (R)**

 R should be obtained from published values, as calculation is very tedious. For calculation, R equals E (the kinetic energy of rainfall) times I30 (maximum intensity of rain in 30 minutes in cm/hr). Roose (1996) found that for Western Africa R = a * precipitation where a = 0.5 in most cases, 0.6 near the sea, 0.3 to 0.2 in tropical mountain areas, and 0.1 in Mediterranean mountain areas.

 The following equation is widely used to calculate the R index (http://www.fao.org/docrep/t1765e/t1765e0e.htm):

 .. math:: R = E\cdot I30 = (210 + 89 \log_{10}I30)*I30

 *E:* kinetic energy of rainfall expressed in metric MJ ``*`` m/ha/cm of rainfall.

 *I30:* maximum intensity of rain in 30 minutes expressed in cm per hour.

 In the United States, national maps of the erosivity index can be found through the United States Department of Agriculture (USDA) and Environmental Protection Agency (EPA) websites. The USDA published a loss handbook (http://www.epa.gov/npdes/pubs/ruslech2.pdf ) that contains a hard copy map of the erosivity index for each region. Using these maps requires creating a new line feature class in GIS and converting to raster. Please note that conversion of units is also required (multiply by 17.02). We provide a raster version of this map on the InVEST support site http://invest.ecoinformatics.org/shared. The EPA has created a digital map that is available at http://www.epa.gov/esd/land-sci/emap_west_browser/pages/wemap_mm_sl_rusle_r_qt.htm . The map is in a shapefile format that needs to be converted to raster, along with an adjustment in units.

3. **Soil erodibility (K)**

 Texture is the principal factor affecting K, but soil profile, organic matter and permeability also contribute. It varies from 70/100 for the most fragile soil and 1/100 for the most stable soil. It is measured on bare reference plots 22.2 m long on 9% slopes, tilled in the direction of the slope and having received no organic matter for three years. Values of 0 -- 0.6 are reasonable, while higher values should be given a critical look. K is sometimes found as part of standard soil data maps, or can be calculated from soil properties.

 The FAO provides global soil data in their Harmonized World Soil Database: http://www.iiasa.ac.at/Research/LUC/External-World-soil-database/HTML/. Soil data for many parts of the world are also available from the Soil and Terrain Database (SOTER) Programme (http://www.isric.org/projects/soil-and-terrain-database-soter-programme).

 In the United States free soil data is available from the U.S. Department of Agriculture's NRCS in the form of two datasets: SSURGO http://soils.usda.gov/survey/geography/ssurgo/ and STATSGO http://soils.usda.gov/survey/geography/statsgo/ . Where available SSURGO data should be used, as it is much more detailed than STATSGO. Where gaps occur in the SSURGO data, STATSGO can be used to fill in the blanks.

 The soil erodibility should be calculated for the surface soil horizon of each soil component and then a weighted average of the components should be estimated for the soil class. This can be a tricky GIS analysis: In the US soil categories, each soil property polygon can contain a number of soil type components with unique properties, and each component may have different soil horizon layers, also with unique properties. Processing requires careful weighting across components and horizons. The Soil Data Viewer (http://soildataviewer.nrcs.usda.gov/), a free ArcMap extension from the NRCS, does this soil data processing for the user and should be used whenever possible.

 The following equation can be used to calculate K (Wischmeier and Smith 1978):

 .. math:: K= 27.66\cdot m^{1.14}\cdot 10^{-8}\cdot(12-a)+(0.0043\cdot(b-2))+(0.0033\cdot(c-3))

 In which K = soil erodibility factor (t*ha/MJ*mm) m = (silt (%) + very fine sand (%))(100-clay (%)) a = organic matter (%) b = structure code: (1) very structured or particulate, (2) fairly structured, (3) slightly structured and (4) solid c = profile permeability code: (1) rapid, (2) moderate to rapid, (3) moderate, (4) moderate to slow, (5) slow and (6) very slow.
 
 When profile permeability and structure are not available, as is often the case outside the U.S., soil erodibility can be estimated based on soil texture and organic matter content with the following table based on Fig. 21 in Roose (1996):
 
 .. figure:: ./sediment_retention_images/soil_erodibility_table.png

4. **Land use/land cover**

 A key component for all water models is a spatially continuous landuse / land cover raster grid. That is, within a watershed, all landuse / land cover categories should be defined. Gaps in data will create errors. Unknown data gaps should be approximated.  Global land use data is available from the University of Maryland's Global Land Cover Facility: http://glcf.umiacs.umd.edu/data/landcover/.  This data is available in 1 degree, 8km and 1km resolutions.  Data for the U.S. for 1992 and 2001 is provided by the EPA in their National Land Cover Data product: http://www.epa.gov/mrlc/.

 The simplest categorization of LULCs on the landscape involves delineation by land cover only (e.g., cropland, temperate conifer forest, prairie). Several global and regional land cover classifications are available (e.g., Anderson et al. 1976), and often detailed land cover classification has been done for the landscape of interest.

 A slightly more sophisticated LULC classification could involve breaking relevant LULC types into more meaningful types. For example, agricultural land classes could be broken up into different crop types or forest could be broken up into specific species. The categorization of land use types depends on the model and how much data is available for each of the land types. The user should only break up a land use type if it will provide more accuracy in modeling. For instance, for the sediment model the user should only break up 'crops' into different crop types if they have information on the difference in soil characteristics between crop management values.

5. **P and C coefficients**

 The support practice factor, P, accounts for the effects of contour plowing, strip-cropping or terracing relative to straight-row farming up and down the slope. The cover-management factor, C, accounts for the specified crop and management relative to tilled continuous fallow. Several references on estimating these factors can be found online:

 * U.S. Department of Agriculture soil erosion handbook http://topsoil.nserl.purdue.edu/usle/AH_537.pdf

 * USLE Fact Sheet http://www.omafra.gov.on.ca/english/engineer/facts/00-001.htm

 * U.N. Food and Agriculture Organization http://www.fao.org/docrep/T1765E/t1765e0c.htm

6. **Vegetation retention efficiencies**

 These values are used to incorporate the effects of natural vegetation that buffer potential water quality impairment downhill from sources. To develop these values, all land class pixels that contain natural vegetation (such as forests, natural pastures, wetlands, or prairie) are assigned high values and vegetation that has no or little filtering value receives a value of zero. All values should fall between 0 and 100. Consult with a hydrologist if not certain about assignment of specific values.

7. **Watersheds / subwatersheds**

 Watersheds should be delineated by the user, based on the location of reservoirs or other points of interest. Exact locations of specific structures, such as reservoirs, should be obtained from the managing entity or may be obtained on the web at sites such as the National Inventory of Dams (http://nid.usace.army.mil/).

 Watersheds that contribute to the points of interest must be generated.  If known correct watershed maps exist, they should be used.  Otherwise, watersheds and subwatersheds can be generated in ArcMap using a hydrologically-correct digital elevation model. Due to limitations in ArcMap geoprocessing, the maximum size of a subwatershed that can be processed by the Nutrient Retention tool is approximately the equivalent of 4000x4000 cells, at the smallest cell size of all input grids. See the Working with the DEM section of this manual for more information on generating watersheds and subwatersheds.

8. **Sediment table**

 The estimated sediment removal cost from the reservoirs will ideally be based on the characteristics of each reservoir and regional cost data. The user should consult managers at the individual reservoirs or a local sediment removal expert. The technology available at each location may vary, and the applicability of the specific technologies depends on the storage capacity/mean annual runoff ratio and the storage capacity/annual sediment yield ratio.

 Once a range of possible technologies has been established for each reservoir, the model user should investigate past sediment removal projects to determine appropriate costing. This may require calculating to present day value and taking into account that the technology may have improved, reducing the relative cost.

 If local information is not available, pricing must be estimated using published information. Adjust costs to specific requirements, location, and present day value as needed.

9. **Slope Threshold**

 The threshold was introduced, along with the alternative LS equation, after application of our model in China in a very steep region of the Upper Yangtze River basin. There, the model performed well when we used a slope threshold of 75% which indicates that agriculture extended into very steep sloping areas, which was the case. In an application in the Cauca Valley, Colombia (in the high Andes), we have used a slope threshold of 90%, basically turning off the alternative slope equation, and the model has performed well there with this approach. If you are unsure of the value to use here, we recommend running the model at least twice, once with the default 75% value and once with 90% and comparing results. If the results are very different (e.g. the model is very sensitive to this input in your region) we recommend finding at least one observation to compare outputs to to guide the decision on the value to use here.

10. **Dredging and Water Quality annual loading thresholds**

 Gathering information on water quality standards or targets should be part of the formulation of modeling objectives. If the target to be met is a drinking water target, standards may be set by the federal, state or local level (whichever standard is the most stringent).

 These standards are set for point of use, meaning that the standard at the point of interest, where water supply will be drawn, may be more relaxed than these standards if water treatment is in place. In-situ water quality standards (for rivers, lakes and streams) may also be set at the national, state and local level. They may be the same across all water bodies of the same type (in rivers, for example) or they may vary depending on the established use of the water body or the presence of endangered species. In the U.S. Total Maximum Daily Loads of sediment are typically established by state regulatory agencies in compliance with the Clean Water Act. States report information on TMDLs to the U.S. EPA on specific waterways http://www2.ctic.purdue.edu/kyw/tmdl/statetmdllists.html .


References
==========

Anderson, J.R., Hardy E., Roach, J., and Witmer, R. 1976. A Land Use and Land Cover Classification System For Use with Remote Sensor Data: Geological Survey Professional Paper 964. Edited by NJDEP, OIRM, BGIA, 1998, 2000, 2001, 2002, 2005.

Desmet, P., and G. Govers (1996) A GIS procedure for automatically calculating the USLE LS factor on topographically complex landscape units. Journal of Soil and Water Conservation, vol. 51, no. 5, pp. 427-433.

FAO. 2002., FAOSTAT Homepage of Food and Agriculture Organization of the United Nations, Online 2008, 9/11.

Huang Yanhe and Lu Chenglong. 1993. Advances in the application of the Universal Soil Loss Equation (USLE) in China. Journal of Fujian Agricultural College (Natural Science Edition) 22 (1): 73 ~ 77.

Roose, E. 1996, Land Husbandry -Components and strategy. 70 FAO Soils Bulletin, Food & Agriculture Organization of the UN, Rome, Italy.

Wischmeier, W.H. & Smith, D. 1978, Predicting rainfall erosion losses: a guide to conservation planning. USDA-ARS Agriculture Handbook , Washington DC.
