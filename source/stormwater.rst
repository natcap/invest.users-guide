.. _stormwater:

***********************************************
Stormwater Retention Model
***********************************************


Overview
========
The model calculates annual stormwater retention volume and the associated water quality benefits. The value of the retention service may be calculated using a replacement cost of stormwater infrastructure.

Model description
=================

Estimate stormwater retention and infiltration 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model requires values of the annual runoff coefficients (:math:`RC`), and optionally the infiltration ratios (:math:`IR`), for each LULC type in the biophysical table (See Table 1). RCs are defined as the ratio between annual runoff and annual precipitation, a value between 0 and 1, while the infiltration ratio is the ratio between annual infiltration to groundwater and annual precipitation. See “Input guidance” for how to find these values.

For each LULC class :math:`x`, the stormwater retention coefficient :math:`R_x` is calculated as:

.. math:: R_x=1-RC_x

 
Table 1. Example of “Biophysical Table” with runoff coefficients (``RC_``), infiltration ratios(``IR_``), and event mean concentrations (``EMC_``) of phosphorus (P) and nitrogen (N) for each soil group (A,B,C,D). 


Based on the LULC and hydrologic soil group rasters, the model assigns the stormwater retention coefficients (:math:`R_i`) to each pixel :math:`i`. Next, the model computes :math:`VR` , the retained volume (:math:`m^3/yr`) for each pixel :math:`i`as:

.. math:: VR_i=0.001\cdot P_i\cdot R_i\cdot pixel.area

where :math:`P_i` is annual precipitation (:math:`mm/yr`) and :math:`pixel.area` is the pixel area in :math:`m^2`.

Optionally, if infiltration ratios have been defined by the user, the model assign these values to each pixel :math:`i` (based on the LULC and soil hydrological group rasters), and computes :math:`VI`, the infiltrated volume (:math:`m^3/yr`) for each pixel :math:`i`:

.. math:: VI_i=0.001\cdot P_i\cdot IR_i\cdot pixel.area

where :math:`IR_i` is the annual infiltration ratio (Table 1).

Optional: Adjust Retention Coefficient for (assumed) Directly-Connected Impervious
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retention on a given pixel, at least when considered at an aggregated sub-watershed scale, should be affected by retention on upstream and downstream (or at least surrounding) pixels. The current InVEST NDR model takes this into account through a flowpath delineation and retention length framework, which is not as feasible in an urban drainage network because of how storm drains alter surface flow paths. A simple modification to retention was tested in which the retention coefficient, Ri,j, for the pixel located at i,j was adjusted upwards based on the retention value of all 8 surrounding pixels. The adjustment, Ci,j,  was applied to the un-retained runoff from a given pixel, as follows:

.. math:: R^{adj}_{i} = R_{i} + (1 - R_{i})\cdot C_{i}


where :math:`R^{adj}_{i}` is the adjusted retention coefficient, and the adjustment factor :math:`C_{i}` has one of the following values:

- 0, if the pixel :math:`i` is near a directly-connected impervious area and/or near a road.

    - A pixel is "near" a directly-connected impervious area if its centerpoint is within a radius :math:`l` of the centerpoint of a pixel whose LULC class is marked as connected (has a 1 in the biophysical table ``is_connected`` column)

    - A pixel is "near" a road if the distance from its centerpoint to the nearest point of a road centerline is within the radius :math:`l`

- :math:`R_{mean,i}`, otherwise

where :math:`R_{mean,i}` is the average retention coefficient of the pixel :math:`i`' and its valid neighboring pixels. "Neighboring" pixels are those which are not further than the radius :math:`l` from :math:`i`, measured centerpoint-to-centerpoint. Nodata pixels and area within the radius that extends over the raster edge do not count towards the average.

In other words, no additional retention is provided by surrounding land if the pixel is considered directly-connected, i.e. is adjacent to dense urban land use or to roadways, which in most urban areas are directly connected to the drainage network by ditches or sub-surface pipes. Otherwise, the pixel’s retention coefficient is increased proportional to the retention provided by its neighboring pixels.

Considerations: This approach produces additional retention in large pervious areas such as agriculture, parks, golf courses, and cemeteries, and should provide improved accuracy in more developed watersheds, where the assumption of direct connectedness of roadways is more probable due to the prevalence of piped, curb-and-gutter roadways. However, the approach may “over-correct” (under-predict) retention for more rural watersheds, especially those with primarily ditched roadways, where the assumption of direct connection of roadways may fall short due to additional retention that might occur in ditches due to increased residence time and/or infiltration. Further, this approach will be affected by the resolution of the input rasters, as it only considers adjacent cells rather than a distance (the latter approach being used by NDR). A simple test of the adjustment for gauged watersheds in the Minneapolis-St. Paul, MN metropolitan area is shown in Section 2.5.


Calculate water quality benefits of stormwater retention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The potential water quality impact of stormwater retention is determined as the pollutant mass associated with retained stormwater, i.e. the amount of pollutant load avoided. The annual avoided pollutant load, in :math:`kg/yr`, is calculated for each pixel :math:`i` as the product of runoff volume (:math:`m3/yr`) and the event mean concentration (EMC) of a pollutant, in :math:`mg/L`:

.. math:: Load_i=1000\cdot V_{R,i}\cdot EMC

EMCs for N and P are assigned to land use classes using the biophysical look-up table (Table 1). 

It should also be noted that users may add other stormwater pollutants (such as sediment, metals, or organic compounds) to the model by providing EMC values for those pollutants in the biophysical table.  

Valuation of stormwater retention service (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A review of the most common valuation methods for the stormwater retention service can be found in a working paper by Sahl et al. (2015). If stormwater regulations exist, the user can assess the value of stormwater retention with the target retention volume as a reference. The economic value can be assessed if the average value of retention device (:math:`$/m^3`) is available:

.. math:: Retention.cost=PR\cdot VR

where :math:`PR` is the replacement cost of stormwater retention (:math:`$/m^3`). For example, Simpson and McPherson (2007) estimate this to be :math:`$1.59/m^3` for urban areas in the San Francisco Bay area.
 
The model can output potential groundwater recharge volume (:math:`VI` from Eq. 2-3), which may also serve as a valuation of retention. However, the model does not currently estimate the pollutant load associated with this recharge volume, as sub-surface transport and transformation of pollutants is not implemented in the model.

Aggregation at the watershed scale (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users may provide a polygon vector file outlining areas over which to aggregate data (typically watersheds or sewersheds). The model will aggregate the output rasters to compute:

- Average stormwater retention ratio (average of :math:`R` values, [Eq. 2-1])
- Total retention volume, :math:`m^3` (sum of :math:`VR` values, [Eq. 2-2])
- Total retained pollutant load for each pollutant, :math:`kg/yr` (sum of retained loads, [Eq. 2-5])
- Total potential recharge volume, :math:`m^3` (sum of :math:`VI`, [Eq. 2-3]) (if infiltration data provided)
- Total Replacement Cost, currency units (sum of retention costs, Eq. 2.5) (if value data provided)


Data Needs
==========

- **Workspace** (required). Folder where model outputs will be written. Make sure that there is ample disk space, and write permissions are correct.

- **Suffix** (optional). Text string that will be appended to the end of output file names, as "_Suffix". Use a Suffix to differentiate model runs, for example by providing a short name for each scenario. If a Suffix is not provided, or changed between model runs, the tool will overwrite previous results.

- **Land use/land cover (LULC)** (required). Raster map of LULC codes. Each pixel has integer LULC code indicating the landcover type. *All values in this raster MUST have corresponding entries in the Biophysical table.*

- **Soil hydrologic group** (required): Raster map of soil hydrologic groups. Each pixel's value is 1, 2, 3, or 4, corresponding to hydrologic soil groups A, B, C, and D respectively.

- **Precipitation** (required). Raster map of annual precipitation in :math:`mm/yr`

- **Biophysical table** (required). A .csv (Comma Separated Value) table containing model information corresponding to each of the land use classes in the LULC raster. *All LULC classes in the LULC raster MUST have corresponding values in this table.* Each row is a land use/land cover class and columns must be named and defined as follows:

    - **lucode**: Unique integer for each LULC class (e.g., 1 for forest, 3 for grassland, etc.) *Every value in the LULC map MUST have a corresponding lucode value in this column.*

    - **is_impervious** (only required if **Adjust retention ratios** is checked: Binary value indicating whether each LULC class is directly-connected impervious (enter 1 for yes, 0 for no). This is used to adjust the retention coefficients for nearby pixels.

    For each soil group :math:`x` in **A, B, C, D**:

    - **RC_x**: Runoff coefficient for this combination of LULC class and soil group. These are ratios between 0 and 1 representing the fraction of precipitation that leaves the area as runoff.
    - **IR_x**: Infiltration coefficient for this combination of LULC class and soil group. These are ratios between 0 and 1 representing the fraction of precipitation that infiltrates the soil and becomes groundwater.

    For each pollutant :math:`p` of interest (there may be any number of pollutants in the table):

    - **EMC_p**: Event mean concentration of this pollutant in :math:`mg/L`.


- **Adjust retention ratios** (true/false): If this box is checked, adjust retention ratios as described above. 

- **Retention radius** (required if **Adjust retention ratios** is checked): Length in meters to use as the radius for the adjustment algorithm above

- **Road centerlines** (optional): Linestring vector map of road centerlines, used to adjust retention coefficient for nearby pixels

- **Replacement cost** (optional): Average cost of a stormwater retention device, such as a retention pond, in :math:`$/m^3` (any currency units may be used).

- **Aggregate areas** (optional): Polygon vector map of area(s) over which to aggregate the output data. These are typically watersheds or sewersheds. Watersheds can be obtained with the DelineateIt model.



Default values for Nitrogen and Phosphorus are specified from the U.S. NSQD (bmpdatabase.org/nsqd.html) and other references (see Section 2.5)

Potential source: https://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html
Replacement cost, PR (optional)
Decimal
Average cost of a stormwater retention device (e.g. retention pond), in $/m3. Available from national or regional studies (e.g. EPA report for the US: https://www3.epa.gov/npdes/pubs/usw_d.pdf)
Representative value of $1.59 USD/m3 from Simpson and McPherson (2007). 



Interpreting Results
====================

- **retention_ratio.tif**: Raster map of retention ratios derived by cross-referencing the LULC and soil group rasters with the biophysical table

- **retention_volume.tif**: Raster map of retention volumes in :math:`m^3/yr`

- **infiltration_ratio.tif**: (if infiltration data provided) Raster map of infiltration ratios derived by cross-referencing the LULC and soil group rasters with the biophysical table

- **infiltration_volume.tif**: (if infiltration data provided) Raster map of infiltration volumes in :math:`m^3/yr`

- **retention_value.tif**: (if value data provided) Raster map of the value of retained water on each pixel in :math:`currency/yr`

- **aggregate.gpkg**: (if aggregate vector provided) Vector map of aggregate data. This is identical to the aggregate areas input vector, but each polygon is given additional fields with the aggregate data:
    
    - **RR_mean**: Average retention ratio over this polygon

    - **RV_sum**: Total retention volume over this polygon in :math:`m^3/yr`

    - **IR_mean** (if infiltration data provided): Average infiltration ratio over this polygon

    - **IV_sum** (if infiltration data provided): Total infiltration volume over this polygon in :math:`m^3/yr`

    - **avoided_p** (for each pollutant :math:`p`): Total avoided amount of pollutant over this polygon in :math:`kg/yr`

    - **val_sum** (if value data provided): Total value of the retained volume of water over this polygon in :math:`currency/yr`



Input Guidance
==============

Runoff coefficients
^^^^^^^^^^^^^^^^^^^

Runoff coefficients for each LULC type may not be known from previous studies. We propose a runoff coefficient calculator that requires as inputs runoff coefficients for 5 general land cover (LC) classes (see table 2 below). Such runoff coefficients can be obtained from:

- the EPA stormwater runoff calculator in the US (https://swcweb.epa.gov/stormwatercalculator/);

- any (monthly or daily time scale) rainfall-runoff model that calculates stormwater runoff and actual evapotranspiration (in mm/yr) for general LC classes (e.g. SWMM software)

- the monthly model developed by Guswa et al. (2018). The model requires monthly precipitation and ET values for a representative site in the landscape, as well as CN values for the SCS-Curve Number method (NRCS-USDA 2004).

Note that runoff coefficients for pervious LCs and bare soil should be defined for each soil hydrologic group (HSG A, B, C, D; see Table 2 for illustration). RC for water is set to 1.

After populating the RC table (and optionally IR table), the user needs to categorize each LULC (Table 1) as one (or a combination) of the general LC classes in the column “SW_Type” (Table 2). For example, the land use classes “scrub/shrub”, “grassland”, and “pasture/hay” are assigned the runoff coefficients for “pervious without tree canopy” (SW_Type=3). Some land use classes such as the “developed” categories can be assigned a combination of LC classes, and the model will compute the area-weighted average of the LC classes’ values. As an example, the “high-intensity urban” NLCD class (US classification; Table 1) represents urban areas with 80 - 100% total impervious area (nominal value 90%): it is assigned a retention coefficient that is weighted 90% “impervious without canopy”, and 10% “pervious with canopy”. Infiltration ratios (IR) are assigned to land use classes using the same approach.
Table 2. Example of Runoff coefficient and infiltration ratio table with values specified by general land cover class and soil hydrologic group (for pervious and bare soil). Values derived from SWMM simulations using 10 years of hourly weather data (2008 - 2017) at Minneapolis-St. Paul Airport, MN, USA.

SW_Type
Description
RC_A
RC_B
RC_C
RC_D
IR_A
IR_B
IR_C
IR_D
1
Impervious      
0.87
0.87
0.87
0.87
0
0
0
0
2
Impervious w/Tree Canopy 
0.82
0.82
0.82
0.82
0
0
0
0
3
Pervious        
0.00
0.09
0.16
0.30
0.110
0.057
0.028
0.007
4
Pervious w/Tree Canopy
0.00
0.08
0.15
0.28
0.110
0.062
0.032
0.008
5
Bare Land
0.00
0.10
0.19
0.35
0.110
0.049
0.021
0.007



Pollutant Event Mean Concentrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pollutant event mean concentrations (EMC) may be specified by the user for any pollutant of interest. Default values for nitrogen and phosphorus for the urban-specific NLCD land use classes can be obtained from the US National Stormwater Quality Database (bmpdatabase.org/nsqd.html), which includes data for over 7,000 samples collected from 500+ sites over the past 30 years across the U.S., as well as from some previous summaries on less-developed land uses (Lin 2004; King and Balogh. 2011). Note: Pitt et al. (2018) found that EMCs in this database were significantly affected by land use, region, and season. Note that these data are reported with generic land use classifications (e.g. “residential”, “commercial”, “industrial”) and need to be adapted to the LULC types provided by the user. Often, a subset of these data with information on total imperviousness of the monitored watersheds can be used to aggregate sites by imperviousness. Nitrogen and phosphorus concentrations for non-urban classes can be obtained from literature summaries, e.g. Line et al. 2002, Maestre and Pitt 2005, Lin 2004, Tetra Tech 2010, and King et al. 2011; these were used along with the U.S. NSQD to determine the EMCs in Table 1. 
Users are encouraged to use results from local studies or other relevant literature values as appropriate, e.g., http://dcstormwaterplan.org/wp-content/uploads/AppD_EMCs_FinalCBA_12222014.pdf).

Representing stormwater retention techniques

Individual stormwater retention techniques like biofilters, bioretention cells, or swales can be represented by a unique LULC category, with a negative runoff coefficient, corresponding to the depth of catchment runoff they capture divided by the precipitation depth on the pixel. This requires the catchment area for the techniques to be known. 


Appendix 1: Assessing the Retention Coefficient Adjustment
==========================================================

Rationale: A primary concern with a grid-based approach to runoff modeling is that when aggregating results at a watershed or study site-scale, the runoff and retention loads are calculated as the sum of loads generated on every pixel – i.e. the runoff generated on each pixel is assumed to enter the drainage network of the watershed, with no chance to be retained as it moves through the network. This is a fair assumption in highly developed areas, where flow path length (i.e., distance surface runoff travels before entering a storm drain) is likely not greater than the size of the pixels (30m in U.S. NLCD/C-CAP). This was also the assumption inherent in the SWMM model as implemented to estimate runoff coefficients (Table 2), in which all runoff was routed directly to the outlet. However, in areas with substantial greenspace such as parks, cemeteries, and golf courses, and potentially outside the urban core where residential development might be less dense, “direct connection” of all constituent grid cells would lead to over-predicted loads and volumes, as additional runoff retention could be provided by infiltration in pervious areas located between pervious pixels and the storm drain network.
Further, the lack of routing also prevents any context analysis in the stormwater model; runoff being generated on a pixel (or a collection of pixels making up a parcel of interest, such as a golf course in the case of our work) is not affected by its surrounding land, nor does it have any effect on its downstream or neighboring pixels. The configuration or location of land uses within the watershed of interest have no bearing on the output, only the total amount of each land use.

Discharge data for 18 watersheds located across the metropolitan area of Minneapolis-St. Paul MN, USA (“Twin Cities” Metro Area, or TCMA) were used for testing the Runoff Retention model. These data were collected by a number of state agencies, and were publicly available. The sites could be roughly categorized by the flow regime and type of system being monitored: 
Large storm drains monitored by several watershed management organizations (Mississippi Watershed Management Organization, www.mwmo.org; Capitol Region Watershed District, www.capitolregionwd.org/monitoring-research/data/; South Washington Watershed District, wq.swwdmn.org), in which discharge was monitored annually, and for which mean annual stormflow volumes had already been determined [n=10 sites, plus 1 stream site monitored as part of stormwater permitting];
Stream gauging sites, monitored by the Metropolitan Council Environmental Services (https://eims.metc.state.mn.us) and maintained by several local watershed districts, in which annual total (baseflow + stormflow) discharge were determined for periods of 10+ years [n = 6 sites].
For the stream gauging sites (Group 2), in which year-round monitoring has been done for 6-30 years (depending on site/constituent), data are generally of high quality, and drainage areas are known. However, the flow volumes include baseflow, which does not allow for direct comparison to Runoff Retention model, though the sites were still tested as a case study. Only the past 10 years of data were included so that the land use classification used to run the Runoff Retention model (U.S. NLCD, derived in 2013) was roughly contemporary with the gauging data; some of the watersheds have undergone substantial development over the previous 20-30 years.

Input data included 30-m U.S. NLCD land cover classification, HSG from the NRCS-USDA Soil Survey, road lines from the state of Minnesota (gisdata.mn.gov), drainage delineations and rainfall from Metropolitan Council and respective watershed districts, with additional rainfall data from Minneapolis-St. Paul Airport (retrieved from Midwest Regional Climate Center, mrcc.illinois.edu).

Results: Results of application of the Runoff Retention model to the 18 TCMA gauging sites, both with and without the retention adjustment (Eq. 2-4), are shown in Figure 1 below. Overall, the base version of the Runoff Retention model tended to over-predict observed runoff volumes for both streams and storm drain sites. Accuracy in simulation of runoff volumes was greatly improved overall when using the retention adjustment, though this was driven primarily by improvements for the storm drain sites. As these sites were generally more urban (developed), the adjusted retention appears to be an effective method to improve simulation of relatively complex connectedness in urban watersheds -- a primary purpose of the development of the Runoff Retention model as an alternative to the NDR model. 

In less developed watersheds (i.e. the streams sites), it was anticipated that under-prediction of retention (over-prediction of runoff) might have resulted from the assumption of direct connection of roadways; instead, the model seems to have over-predicted retention (under-predicted runoff) in the rural watersheds. Two factors may have led to this issue: (1) stream data included baseflow, which is not predicted by the Runoff Retention model, so the simulated volumes are expected to be less than the observed volumes; and (2) the presence of drain tile in agricultural (or golf course) land use might cause some pervious land cover to be more “directly connected” than the coarse retention adjustment would predict.


 
All Sites
Storm Drains
Streams
 
(Group 1)
(Group 2)
Root-Mean Squared Error (RMSE)
Base Model
7.1 cm
7.6 cm
7.8 cm
With Adjusted Retention
3.9 cm
3.9 cm
7.8 cm
Mean Absolute Error (MAE)
Base Model
5.6 cm
6.9 cm
6.9 cm
With Adjusted Retention
3.2 cm
3.2 cm
5.8 cm

Figure 1. Upper Left: Comparison of Modeled vs. Observed Water Yield (cm) for Twin Cities Metro Area stream and storm drain sites using the default retention coefficients; Upper Right: Comparison of Modeled vs. Observed Water Yield (cm) for Twin Cities Metro Area stream and storm drain sites using the adjusted retention coefficient (Eq. 2-4); Lower Table shows RMSE and MAE parameters for the base and adjusted models, overall and as a function of site type (Streams vs. Storm Drains).

Appendix 2: Differences between InVEST and other models

In contrast to the existing InVEST Water Yield and Nutrient Delivery Ratio models, the proposed runoff retention model is concerned primarily with surface runoff, rather than total runoff (surface and sub-surface), and designed to be implemented in urban and developing watersheds. The model uses widely available satellite-derived raster datasets, such as land cover and elevation, along with user inputs in the form of target sub-watersheds or jurisdictional boundaries for aggregation of metrics (spatial data) and, optionally, location-specific runoff and water quality parameters (tabular data). In this respect, the model is very similar to other tools, including iTree and OpenNSPECT.

OpenNSPECT (Open-source Nonpoint Source Pollution and Erosion Comparison Tool; https://coast.noaa.gov/digitalcoast/tools/opennspect.html) is a water quality scenario tool developed in 2014 by the U.S. National Oceanic and Atmospheric Administration (NOAA). 
It was designed to rapidly assess scenarios of land use and climate change impacts to water, nutrient, and sediment loading in developing watersheds. Inputs are primarily in raster format, and include C-CAP or NLCD land cover (30-m resolution), elevation (up to 1m resolution), and soil hydrologic group (USDA soil surveys), as well as event- or annual-scale precipitation (gridded or station-based). Runoff is generated on each pixel using the SCS Curve Number method, taking into account land cover and soil type (hydrologic group) and including a modification for annual runoff. Mass of nutrients (load) exported from each pixel is determined as the product of this runoff volume and a mean nutrient runoff concentration (nitrogen or phosphorus) characteristic of the pixel’s land cover type. A flow direction raster is derived from the elevation data, and used to produce flow paths and drainage basin delineations over which runoff volumes and nutrient loads are routed and aggregated.

The general approach to modeling runoff and water quality in the proposed model is nearly identical to OpenNSPECT, with the following differences:
Runoff is generated on each pixel based on runoff coefficients (runoff depth divided by rainfall depth) rather than curve number. Runoff coefficients are a function of land cover and soil hydrologic group, and are prescribed by the model but can be modified by the user based on output of other models (e.g. SWMM), local hydrology data, modified curve numbers, etc.;
The model estimates potential groundwater recharge through use of an infiltration ratio parameter, which is also prescribed by the model based on SWMM simulations in test watersheds but can be modified by the user.

Note: add comparison between InVEST and iTree (copy from SF working paper)

Additional resources for further hydrologic studies:
LTER model: https://www.sciencedirect.com/science/article/pii/S0301479717301111
https://swtelr.2nform.com/


References
==========

Arkema, K. K., Griffin, R., Maldonado, S., Silver, J., Suckale, J., & Guerry, A. D. (2017). Linking social , ecological , and physical science to advance natural and nature-based protection for coastal communities. https://doi.org/10.1111/nyas.13322

Balbi, M., Lallemant, D., & Hamel, P. (2017). A flood risk framework for ecosystem services valuation: a proof-of-concept.

King, K.W. and Balogh, J. (2011). Stream water nutrient enrichment in a mixed-use watershed. J. Environ. Monit, 13: 721-731.
Lin, J.P. (2004). Review of published export coefficient and event mean concentration (emc) data. Wetlands Regulatory Assistance Program. ERDC TN-WRAP-04-3. Sep 2004.

Line, D.E., White, N.M., Osmond, D.L., Jennings, G.D. and Mojonnier, C.B. (2002). Water Environment Research, 74(1): 100-110.

Maestre, A. and Pitt, R. (2005). The National Stormwater Quality Database, Version 1.1: A Compilation and Analysis of NPDES Stormwater Monitoring Information. Center for Watershed Protection; Ellicott City, MD. Sep 4, 2005.

NRCS-USDA. (2004). Chapter 10. Estimation of Direct Runoff from Storm Rainfall. In United States Department of Agriculture (Ed.), Part 630 Hydrology. National Engineering Handbook. Retrieved from http://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063

Pitt, R., Maestre, A. & Clary, J. (2018). The National Stormwater Quality Database (NSQD), Ver 4.02. Retrieved from http://www.bmpdatabase.org/Docs/NSQD_ver_4_brief_Feb_18_2018.pdf

Sahl, J. (2015). Economic Valuation Approaches for Ecosystem Services: a literature review to support the development of a modeling framework for valuing urban stormwater management services.

Simpson, J.R. and McPherson, E.G. (2007). San Francisco Bay Area State of the Urban Forest Final Report. Center for Urban Forest Research, USDA Forest Service Pacific Southwest Research Station. Davis, CA. Dec 2007: 92 pp. 

Tetra Tech, Inc. (2010). Stormwater Best Management Practices (BMP) Performance Analysis. Prepared for U.S. E.P.A. Region 1. Fairfax, VA. 232 pp.
