.. _data_sources:

************
Data Sources
************

This is a compilation of data sources and suggestions for common model inputs. This list is not definitive and is only meant to serve as a starting point. It is highly recommended to look for more local and accurate data (from national, state, university, literature, NGO and other sources) and only use global data for final analyses if nothing more local is available. If you know of a useful data source not listed here, please share it on the forum.

.. _dem:

Digital Elevation Model
-----------------------
A digital elevation model (DEM) is a raster map of elevation, where each pixel's value is its elevation above sea level (usually in meters). DEM data is available for any area of the world, although at varying resolutions.

Free raw global DEM data is available from:

 * The World Wildlife Fund - https://www.worldwildlife.org/pages/hydrosheds
 * NASA: https://asterweb.jpl.nasa.gov/gdem.asp (30m resolution); and easy access to SRTM data: http://dwtkns.com/srtm/
 * USGS: https://earthexplorer.usgs.gov/

The DEM resolution may be a very important parameter depending on the project’s goals. For example, if decision makers need information about impacts of roads on ecosystem services then fine resolution is needed. The hydrological aspects of the DEM used in the model must be correct. Most raw DEM data has errors, so it's likely that the DEM will need to be filled to remove sinks. Multiple passes of the ArcGIS Fill tool, or QGIS Wang & Liu Fill algorithm (SAGA library) have shown good results. 

For hydrological models that generate streams from the DEM, look closely at the stream network raster output. If streams are not continuous, but broken into pieces, the DEM still has sinks that need to be filled. If filling sinks multiple times does not create a continuous stream network, perhaps try a different DEM. If the results show an unexpected grid pattern, this may be due to reprojecting the DEM with a "nearest neighbor" interpolation method instead of "bilinear" or "cubic". In this case, go back to the raw DEM data and reproject using "bilinear" or "cubic".

Also see the Working with the DEM section of this User Guide for more details and guidance about processing DEMs.


.. _lulc:

Land Use/Land Cover
-------------------
Land use/land cover (LULC) describes the physical properties of the land and/or how people are using it (forest, wetland, water, paved, agricultural, nature preserve, etc.) In order to display the data in raster format, each LULC category is mapped to an integer code (these codes do not have to be consecutive or ordered). Unknown data gaps should be approximated where possible to avoid missing data (holes) in the output layers.

Global land use data is available from several sources including:

 * NASA: https://lpdaac.usgs.gov/products/mcd12q1v006/ (MODIS multi-year global landcover data provided in several classifications)
 * European Space Agency WorldCover at 10m resolution: https://esa-worldcover.org/
 * European Space Agency Climate Change Initiative land cover at 300m resolution: https://www.esa-landcover-cci.org/

Data for the U.S. is provided by the USGS and Department of the Interior via the National Land Cover Database: https://www.usgs.gov/centers/eros/science/national-land-cover-database

Many countries have national LULC maps that can be used, and it is recommended to look for these maps whenever possible. 

It is important to evaluate any given land cover map, to see how accurate it is in your study area. Global products in particular are often more accurate in some places (or with some land cover types) than others. 

Sometimes it is useful to separate a more general LULC class into more detailed classes. For example, agricultural land classes could be broken up into different crop types. Forest could be broken up into specific species or age categories. Where data is available, you may stratify LULC types by variables, such as rainfall, temperature, elevation, etc., known to affect the properties being modeled.

The categorization of land use types depends on the model and how much data is available for each of the land types. Typically, the biophysical table input maps certain relevant biophysical parameters to each LULC code. You should only break up a LULC type if it will provide more accuracy in modeling. For instance, only break up ‘crops’ into different crop types if you have information on the difference in relevant biophysical parameters.

*A typical LULC classification scheme - yours is likely to be different*

  ====== ===========================
  lucode Land Use/Land Cover
  ====== ===========================
  1      Evergreen Needleleaf Forest
  2      Evergreen Broadleaf Forest
  3      Deciduous Needleleaf Forest
  4      Deciduous Broadleaf Forest
  5      Mixed Cover
  6      Woodland
  7      Wooded Grassland
  8      Closed Shrubland
  9      Open Shrubland
  10     Grassland
  11     Cropland (row Crops)
  12     Bare Ground
  13     Urban and Built-Up
  14     Wetland
  15     Mixed evergreen
  16     Mixed Forest
  17     Orchards/Vineyards
  18     Pasture
  ====== ===========================

.. _carbon_pools:

Carbon Pools
------------
Carbon storage data should be set equal to the average carbon storage values for each LULC class. The ideal data source for all carbon stocks is a set of local field estimates, where carbon storage for all relevant stocks has been directly measured. These can be summarized to the LULC map, including any stratification by age or other variable. If these data are not available, however, there are several general data sources that can be used.

Note that several sources, including IPCC (2006), report in units of biomass, while InVEST uses mass of elemental carbon. To convert metric tons of biomass to metric tons of C, multiply by a conversion factor, which varies typically from 0.43 to 0.51. Conversion factors for different major tree types and climatic regions are listed in Table 4.3 on page 4.48 of IPCC (2006).

.. _aboveground_carbon:

Carbon Stored in Aboveground Biomass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A good but very general source of data for carbon storage is the Intergovernmental Panel on Climate Change's (IPCC) 2006 methodology for determining greenhouse gas inventories in the Agriculture, Forestry and Other Land Use (AFOLU) sector (https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html). To use this set of information from the IPCC, you must know your site's climate domain and region; use data from Table 4.1 on page 4.46 and a digital copy of the Food and Agriculture Organization of the United Nations' (FAO) eco-region map (http://www.fao.org/geonetwork/srv/en/main.home) to figure that out. Tables 5.1 through 5.3 (p. 5.9) of IPCC (2006) give estimates for aboveground biomass in agriculture land with perennial woody biomass (e.g., fruit orchards, agroforestry, etc.). Tables 4.7, 4.8, and 4.12 give aboveground biomass estimates for natural and plantation forest types. 

Ruesch and Gibbs (2008) mapped the IPCC (2006) aboveground biomass carbon storage data given year 2000 land cover data, which can be accessed here: https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html. These data are, unfortunately, not well documented, but "lut.zip" contains a table of carbon values for each ecoregion. The table does not list units explicitly, but the metadata .xml files indicate that values are in tons C per hectare.

Other general sources of carbon storage estimates can be found. For example, Grace et al. (2006) estimate the average aboveground carbon storage (leaf + wood) for major savanna ecosystems around the world (Table 1). Houghton (2005) gives aboveground carbon storage for natural and plantation forest types, by continent (Tables 1 and 3). Brown et al. (1989) give aboveground biomass estimates for tropical broadleaf forests as a function of land-use: undisturbed, logged and nonproductive (Table 7). Region-specific sources of carbon storage data are also available. Those we've found include:

* Latin America: Malhi et al. (2006) report aboveground biomass volumes for 227 lowland forest plots in Bolivia, Brazil, Colombia, Ecuador, French Guinea, Guyana, Panama, Peru, and Venezuela. Nascimento and Laurance (2002) estimate aboveground carbon stocks in twenty 1-ha plots of Amazonian rainforest. Tiessen et al. (1998) find aboveground carbon stocks for the Brazilian savanna types Caatingas and Cerrados.

* Africa: Zhang and Justice (2001) report aboveground carbon stocks for major forest and shrub LULC types for central African countries. Tiessen et al. (1998) estimates total aboveground biomass of degraded savanna in Senegal. Makundi (2001) reports mean annual incremental growth for three forest plantation types in Tanzania. Malimbwi et al. (1994) estimates aboveground carbon stocks in the miombo woodlands of Kitungalo Forest Reserve Tanzania. Munishi and Shear (2004) report aboveground carbon stocks in the Afromontane rain forests of the Eastern Arc Mountains of Tanzania. Glenday (2006) estimates aboveground carbon stocks for 3 forest types in the Kakamega National Forest of western Kenya.

* North America: Smith et al. (2006) estimate aboveground carbon stocks for all major forest types in the US.

* The Carbon On Line Estimator (https://www.ncasi.org/resource/carbon-on-line-estimator-cole/) is a tool for calculating carbon characteristics in U.S. forests based on USDA Forest Service Forest Inventory & Analysis and Resource Planning Assessment data. With this tool, carbon characteristics can be examined at the scale of counties. Using the variables tab, aboveground, belowground, soil, or dead wood carbon pools can be selected.

* Coomes et al. (2002) estimate aboveground carbon stocks for native shrubland and forest types in New Zealand.

Aboveground biomass (and therefore carbon stocks) can also be calculated from timber inventories, which are often done by forestry ministries on a set of plots. Use the following formula to estimate the aboveground carbon stock in a forest stand that has been inventoried for its merchantable volume where VOB is the per-hectare volume of trees in cubic meters measured from tree stump to crown point (the merchantable portion of the tree), WD is the wood density of trees (dry biomass per unit of tree volume), BEF is the ratio of total aboveground dry biomass to dry biomass of inventoried volume, and CF is the ratio of elemental carbon to dry biomass, by mass (Brown 1997). The biomass expansion factor (BEF) accounts for C stored in all other portions of the tree aboveground (e.g., branches, bark, stems, foliage, etc; the non-merchantable portions of the tree). In most cases WD for a plot is approximated with values for dominant species. Brown (1997) provides a table of WD values for many tree species in Appendix 1 of section 3 and a method for calculating BEF (Equation 3.1.4). See ECCM (2007) for an application of this FAO method to forest inventory data from eastern Tanzania. IPCC (2006) also presents estimates of ( ) where BEF values for hardwood, pine, conifer, and natural forest stands by eco-region are given in Table 4.5 and WD values for many species are given in Tables 4.13 and 4.14. (Use the BCEF values in Table 4.5 that are subscripted by S.) Finally, Brown et al. (1989) give BEF for tropical broadleaf forests under three land uses: undisturbed, logged, and nonproductive.

Brown (1997) attaches several caveats to the use of the above equation. First, the equation is designed for inventoried stands that are closed as opposed to open (forests with sparser canopy coverage such as oak savanna). Second, VOB estimates should be a function of all tree species found in the stand, not just the economically most valuable wood. Third, trees with diameters as low as 10 centimeters at breast height (DBH = 10) need to be included in the inventory if this aboveground biomass carbon equation is to be as accurate as possible. Brown (2002) also notes that the use of a single BEF value is a simplification of the actual biomass growth process.

These caveats lead Brown (2002) to recommend the use of allometric biomass equations to estimate woody aboveground biomass if available. These equations give the estimated relationship between a stand's distribution of different-sized trees and the stand's aboveground biomass. Brown (1997) and Brown and Schroeder (1999) provide general aboveground biomass allometric equations for all global eco-regions and the eastern US, respectively. Cairns et al. (2000) provide aboveground biomass allometric equations for LULC types in southern Mexico. Nascimento and Laurance (2002) estimate Amazonian rainforest aboveground biomass using allometric curves. The use of these equations requires knowledge of the distribution of tree size in a given stand.

Some researchers have made use of these equations a bit easier by first relating a stand's distribution of different-sized trees to its age and then mapping the relationship between age and aboveground biomass (i.e., ). For example, Silver et al. (2000) have estimated aboveground biomass as a function of stand age (i.e., years since afforestation/reforestation) or previous LULC for native forest types in tropical ecosystems. Smith et al. (2006) take the transformation of allometric equations one step further by relating age to total biomass carbon (belowground plus aboveground) directly for various US forests.

When using IPCC data or other similar broad data sources, one final issue to consider is how the level of anthropogenic disturbance affects carbon stocks. The aboveground C stock of highly disturbed areas will likely be lower than the stocks of undisturbed areas. It is not clear what type of disturbance levels IPCC or other such sources assume when reporting aboveground biomass estimates. If forest disturbance is an issue in the demonstration site, LULC types should be stratified by levels of disturbance. For an example of such stratification see Table 2.5, page 14 of ECCM (2007).

Finally, we generally do not treat aboveground herbaceous material as a carbon pool (e.g., grass, flowers, non-woody crops). Our working assumption is that this material does not represent a potential source of long-term storage like woody biomass, belowground biomass, and soil. Herbaceous material in general recycles its carbon too quickly.

.. _belowground_biomass:

Carbon Stored in Belowground Biomass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For LULC categories dominated by woody biomass, belowground biomass can be estimated roughly with the "root to shoot" ratio of belowground to aboveground biomass. Default estimates of the root to shoot ratio are given in Table 4.4 on p. 4.49 of IPCC (2006) by eco-region. Broad estimates of this ratio are also given in Section 3.5 of Brown (1997).

Some LULC types contain little to no woody biomass but substantial belowground carbon stocks (e.g., natural grasslands, managed grasslands, steppes, and scrub/shrub areas). In these cases the root to shoot ratio described above does not apply. Belowground estimates for these LULC types are best estimated locally, but if local data are not available some global estimates can be used. The IPCC (2006) lists total biomass (aboveground plus belowground) and aboveground biomass for each climate zone in table 6.4 (p. 6.27). The difference between these numbers is a crude estimate of belowground biomass. . Recently, Ruesch and Gibbs (2008) mapped the IPCC (2006) aboveground biomass carbon storage data given year 2000 land cover data, which can be accessed here: https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html.

Several studies have compiled estimates of belowground biomass or root-to-shoot ratios for different habitat types. Among those we found:

* Grace et al. (2006) estimate the total average woody and herbaceous root biomass for major savanna ecosystems around the world (Table 1). Baer et al. (2002) and Tilman et al. (2006) estimate the C stored in the roots of plots restored to native C4 grasses in Nebraska and Minnesota, U.S. respectively, as a function of years since restoration (see Table 2 in Baer et al. (2002) and Figure 1D in Tilman et al. (2006)).

* Cairns et al. (1997) survey root-to-shoot ratios for LULC types across the world. Munishi and Shear (2004) use a ratio of 0.22 for Afromontane forests in the Eastern Arc forests of Tanzania. Malimbwi et al. (1994) use 0.20 for miombo woodlands in the same area of Tanzania. Coomes et al. (2002) use 0.25 for shrublands in New Zealand. Gaston et al. (1998) report a root-to-shoot ratio of 1 for African grass / shrub savannas.

.. _soil_carbon:

Carbon Stored in Soil
^^^^^^^^^^^^^^^^^^^^^

If local or regional soil C estimates are not available, default estimates can be looked up from IPCC (2006) for agricultural, pasture, and managed grasslands. Table 2.3 of IPCC (2006) contains estimates of soil carbon stocks by soil type, assuming these stocks are at equilibrium and have no active land management. For cropland and grassland LULC types, this default estimate can be multiplied by management factors, listed in Tables 5.5 and 6.2 of IPCC (2006). For all other LULC types and their related management schemes, the IPCC (2006) assumes no management factors.

There are alternative global-level sources of soil carbon data. Post et al. (1982) report carbon stocks in the first meter of soil by Holdridge Life Zone Classification System (GIS map of these Zones available at http://www.arcgis.com/home/item.html?id=f3ec7241777f4c56a69ae14d2a98e44b). Silver et al. (2000) have estimated soil carbon as a function of years since afforestation/reforestation for native forest types in tropical ecosystems. Grace et al. (2006) estimate the soil carbon for major savanna types around the world (Table 1). Detwiler (1986) lists soil carbon for tropical forest soils in Table 2.

Soil carbon spatial data is often provided as part of soil property maps, such as those provided by ISRIC Soil Grids (https://soilgrids.org/). If you have such a layer, you can use the Carbon model to sum up only the aboveground, belowground and litter carbon pools (setting c_soil to 0 for all land cover classes), then add the soil carbon layer to the Carbon Storage model output in post-processing.

Several region-specific studies also report soil carbon stocks. Those we've found include:

* North America: Smith et al. (2006) estimate soil C for every 5-year increment up to 125 years since afforestation/reforestation for all major forest types and forest management practices in each region of the U.S. Others include McLauchlan et al. (2006); Tilman et al. (2006); Fargione et al (2008); Schuman et al. (2002); and Lal (2002).

* Africa: Houghton and Hackler (2006) give soil C for 5 LULC forest types (Rain Forest; Moist Forest Dry; Forest; Shrubland; and Montane Forest) in sub-Saharan Africa that have retained their natural cover and for forest areas that have been converted to croplands, shifting cultivation, and pasture. Vagen et al. (2005) provides soil C estimates for various LULC types in sub-Saharan Africa.

* South America: Bernoux et al. (2002) estimated soil C stocks to a depth of 30 cm for different soil type-vegetation associations in Brazil. For example, the soil C stock in HAC soils under 14 different land cover categories, including Amazon forest and Brazilian Cerrado, range from 2 to 116 kg C m-2.

Important Note: In most research that estimates carbon storage and sequestration rates on a landscape, soil pool measures only include soil organic carbon (SOC) in mineral soils (Post and Kwon 2000). However, if the ecosystem being modeled has a lot of organic soils (e.g. wetlands or paramo), it is critical to add this component to the mineral soil content. In landscapes where the conversion of wetlands into other land uses is common, carbon releases from organic soils should also be tracked closely (IPCC 2006).

.. _dead_carbon:

Carbon Stored in Dead Organic Matter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If local or regional estimates of carbon stored in dead organic matter aren't available, default values from the IPCC (2006) can be assigned. Table 2.2 (p. 2.27) gives default carbon stocks for leaf litter in forested LULC types. For non-forested types, litter is close to 0. Grace et al. (2006) estimate the average carbon stored in litter for major savanna ecosystems around the world (Table 1). It is not clear if their total "above-ground biomass" estimates include deadwood or not. Deadwood stocks are more difficult to estimate in general, and we have located no default data sources.

Regional estimates:

* United States: Smith et al. (2006) estimate carbon storage in litter (referred to as "Forest Floor" C in the document) and dead wood (the aggregate of C pools referred to as "Standing Dead Trees" and "Down Dead Wood" in the document) for all major forest types and forest management practices in each region of the U.S. as a function of stand age.

* South America: Delaney et al. (1998) estimate carbon stored in standing and down dead wood in 6 tropical forests of Venezuela. According to the authors, deadwood is typically 1/10 the amount of biomass as aboveground vegetation.



Precipitation
-------------

.. _precipitation:

Annual & Monthly Precipitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Precipitation may be interpolated from long-term rain gauge point data. When considering rain gauge data, make sure that they provide good coverage over the area of interest, especially if there are large changes in elevation that cause precipitation amounts to be heterogeneous within the study area. Ideally, the gauges will have at least 10 years of continuous data, with no large gaps, around the same time period as the land use/land cover map used as input. Precipitation as snow should be included.

Global data sets from remote sensing models can account for remote areas if field data are not available. You can use coarse data from the freely available global data sets developed by the Climatic Research Unit: http://www.cru.uea.ac.uk or WorldClim: https://www.worldclim.org/, among others. One useful place to search for precipitation data is NCAR's Climate Data Guide: https://climatedataguide.ucar.edu/climate-data.

Some sources (such as WorldClim) provide 12 rasters of monthly average precipitation. To use these in the Annual Water Yield model, the monthly rasters must be added together (summed) to calculate an average annual precipitation map.

Within the United States, the PRISM group at Oregon State University provides free precipitation data at a 30-arcsecond resolution. See their website at https://prism.oregonstate.edu/ and navigate to '800m Normals' to download data.

.. _rain_events:

Rain Events
^^^^^^^^^^^
The average number of monthly rain events can be obtained from local climate statistics (Bureau of Meteorology) or online resources:

 * https://www.yr.no/
 * The World Bank also provides maps with precipitation statistics: https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api


Evapotranspiration
------------------

.. _et0:

Reference Evapotranspiration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Reference evapotranspiration, ET₀, measures the amount of water that vaporizes from land into the air over a given period of time. It is the sum of evaporation (directly off of soil, bodies of water, and other surfaces) and transpiration (through plants). It is typically expressed as a depth of water in millimeters per unit time: :math:`mm/month` for monthly, :math:`mm/year` for annual. (Note: similar to precipitation, this is the "depth" of water that evapotranspirates from a given region; it is not "per" pixel, square meter, or any other area unit). InVEST models all use this measure, but some sources express evapotranspiration as a volume or energy per area. See http://www.fao.org/3/x0490e/x0490e04.htm for more details.

CGIAR provides a global map of potential evapotranspiration, based on WorldClim climate data, which may be used for reference ET: https://cgiarcsi.community/data/global-aridity-and-pet-database/.

One useful place to search for evapotranspiration data (or precipitation and temperature data that can be used to calculate ET) is NCAR's Climate Data Guide: https://climatedataguide.ucar.edu/climate-data.

If you are running a model that requires both precipitation and evapotranspiration as inputs, make sure that the ET data is based on the same precipitation data that is being used as a model input. 

Reference evapotranspiration varies with elevation, latitude, humidity, and slope aspect. There are many methodologies, which range in data requirements and precision. 
You can calculate reference ET by developing monthly average grids of precipitation, and maximum and minimum temperatures. These data can come from weather stations, where you can follow the same process as the development of the average annual precipitation grid, including incorporating the effects of elevation when interpolating between stations. Or, both WorldClim and CRU provide monthly temperature data already in grid format. These monthly grids can be used as input to the equations listed below.
You can calculate reference ET by developing monthly average grids of precipitation, and maximum and minimum temperatures (also available from WorldClim and CRU) which need to incorporate the effects of elevation when interpolating from observation stations. Data to develop these monthly precipitation and temperature grids follow the same process in the development of the 'Monthly Precipitation' grids.

A simple way to determine reference evapotranspiration is the 'modified Hargreaves' equation (Droogers and Allen, 2002), which generates superior results than the Pennman-Montieth when information is uncertain. 

.. math:: ET_0 = 0.0013\times 0.408\times RA\times (T_{av}+17)\times (TD-0.0123 P)^{0.76}

The 'modified Hargreaves' method uses the average of the mean daily maximum and mean daily minimum temperatures for each month (`Tavg` in degrees Celsius), the difference between mean daily maximum and mean daily minimums for each month (`TD`), extraterrestrial radiation (:math:`RA` in :math:`\mathrm{MJm^{-2}d^{-1}}`) and average monthly precipitation (:math:`P` in mm per month), all of which can be relatively easily obtained.

You can use this equation on raster data. Note that it calculates average daily ET0, so the result will need to be multiplied by the number of days in the month whose input values you're using, and it must be run once for each month. The resulting monthly ET0 rasters can be used in the Seasonal Water Yield model. For the Annual Water Yield model, add together the monthly ET0 rasters to get annual average ET0.

Temperature and precipitation data are often available from regional charts, direct measurement or national or global datasets (such as WorldClim). Radiation data, on the other hand, is far more expensive to measure directly but can be reliably estimated from online tools, tables or equations. FAO Irrigation Drainage Paper 56 (Allan (1998)) provides monthly radiation data in Annex 2; to use this, select values for the latitude closest to your area of study. Another option is to use a GIS tool to calculate solar radiation for your specific study area, and use this spatial layer as input to the Modified Hargreaves calculation. 

The reference evapotranspiration can also be calculated monthly and annually using the Hamon equation (Hamon 1961, Wolock and McCabe 1999):

.. math:: PED_{Hamon} = 13.97 d D^2W_t

where :math:`d` is the number of days in a month, :math:`D` is the mean monthly hours of daylight calculated for each year (in units of 12 hours), and :math:`W_t` is a saturated water vapor density term calculated by:

.. math:: W_t = \frac{4.95e^{0.062 T}}{100}

where :math:`T` is the monthly mean temperature in degrees Celsius. Reference evapotranspiration is set to zero when mean monthly temperature is below zero. Then for each year during the time period analyzed, the monthly calculated PET values at each grid cell are summed to calculate a map of the annual PET for each year.

A final method to assess ETo, when pan evaporation data are available, is to use the following equation:
:math:`ETo = pan ET *0.7` (Allen et al., 1998)

.. _kc:

Crop Evapotranspiration Coefficient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Evapotranspiration coefficient ( :math:`K_c`) values for crops are readily available from irrigation and horticulture handbooks. FAO has an online resource for this: http://www.fao.org/3/X0490E/x0490e0b.htm. The FAO tables list coefficients by crop growth stage (:math:`K_c` ini, :math:`K_c` mid, :math:`K_c` end), which need to be converted to an annual average or monthly average (depending on the model) :math:`K_c`. This requires knowledge about the phenology of the vegetation in the study region (average green-up, die-down dates) and crop growth stages (when annual crops are planted and harvested). Annual average :math:`K_c` can be estimated as a function of vegetation characteristics and average monthly reference evapotranspiration using the following equation:

.. math:: K_c = \frac{\sum^{12}_{m=1}K_{cm}\times ET_{o_m}}{\sum^{12}_{m=1}ET_{o_m}}

where :math:`K_{cm}` is an average crop coefficient of month :math:`m` (1-12) and :math:`ET_{o_m}` is the corresponding reference evapotranspiration. These values can also be calculated using the following spreadsheet: https://github.com/natcap/invest.users-guide/raw/main/data-sources/kc_calculator.xlsx. Values for :math:`K_c` should be decimals between 0-1.5.

Values for other vegetation types can be estimated using Leaf Area Index (LAI) relationships. LAI characterizes the area of green leaf per unit area of ground surface and can be obtained by satellite imagery products derived from NDVI analysis. A typical LAI - :math:`K_c` relationship is as follows (Allen et al., 1998, Chapter 6: http://www.fao.org/3/x0490e/x0490e0b.htm):

.. math:: K_c = \left\{\begin{array}{l}\frac{LAI}{3}\mathrm{\ when\ } LAI \leq 3\\ 1\end{array}\right.

:math:`K_c` estimates for non-vegetated LULC are based on (Allen et al., 1998). Note that these values are only approximate, but unless the LULC represents a significant portion of the watershed, the impact of the approximation on model results should be minimal.

* Kc for <2m open water can be approximated by Kc=1;
* Kc for >5m open water is in the range of 0.7 to 1.1;
* Kc for wetlands can be assumed in the range of 1 to 1.2;
* Kc for bare soil ranges from 0.3 to 0.7 depending on climate (in particular rainfall frequency). It can be estimated at Kc=0.5 (see Allen 1998, Chapter 11). Additional information for determining Kc for bare soil can be found in (Allen et al., 2005).
* Kc for built areas can be set to f*0.1 +(1-f)*0.6 where f is the fraction of impervious cover in the area. Here, evapotranspiration from pervious areas in built environments is assumed to be approximately 60% of reference evapotranspiration (i.e. the average between lawn grass and bare soil). In addition, evaporation from impervious surface is assumed at 10% of PET. Should local data be available, the user may compute an annual average estimate of Kc, using the method described for crop factors.


Hydrology
---------

.. _watersheds:

Watersheds and Sewersheds
^^^^^^^^^^^^^^^^^^^^^^^^^
To delineate watersheds, we provide the InVEST tool DelineateIT, which is relatively simple yet fast and has the advantage of creating watersheds that might overlap, such as watersheds draining to several dams on the same river. See the User Guide chapter for DelineateIt for more information on this tool. Watershed creation tools are also provided with GIS software, as well as some hydrology models. It is recommended that you delineate watersheds using the DEM that you are modeling with, so the watershed boundary corresponds correctly to the topography.

Alternatively, a number of watershed maps are available online, e.g. HydroBASINS: https://hydrosheds.org/. Note that if watershed boundaries are not based on the same DEM that is being modeled, results that are aggregated to these watersheds are likely to be inaccurate.

Exact locations of specific structures, such as drinking water facility intakes or reservoirs, should be obtained from the managing entity or may be obtained on the web:

 * The U.S. National Inventory of Dams: https://nid.sec.usace.army.mil/

 * Global Reservoir and Dam (GRanD) Database: http://globaldamwatch.org/grand/

 * World Water Development Report II dam database: https://wwdrii.sr.unh.edu/download.html

Some of these datasets include the catchment area draining to each dam, which should be compared with the area of the watershed(s) generated by the delineation tool to assess accuracy.

Sewershed data may be available from local municipalities.


.. _tfa:

Threshold Flow Accumulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The threshold flow accumulation (TFA) is a stream delineation algorithm parameter that specifies the number of upstream pixels that must flow into a pixel before it is classified as a stream. There is no one "correct" value for the TFA. The correct value for your application is the value that causes the model to create a stream layer that looks as close as possible to the real-world stream network in the watershed. Compare the stream network raster output with a known correct stream map, and adjust the TFA accordingly - larger values of TFA will create a stream network with fewer tributaries, smaller values of TFA will create a stream network with more tributaries. A good value to start with is 1000, but note that this can vary widely depending on the resolution of the DEM, local climate and topography. Note that generally streams delineated from a DEM do not exactly match the real world, so just try to come as close as possible. If the modeled streams are very different, then consider trying a different DEM.

A global layer of streams can be obtained from HydroSHEDS: https://hydrosheds.org/, but note that they are generally more major rivers and may not include those in your study area, especially if it has small tributaries. You can also try looking at streams in Google Earth if no more localized maps are available.

Also see the Working with the DEM section of this User Guide for more information.

.. _soil_groups:

Soil Hydrologic Groups
^^^^^^^^^^^^^^^^^^^^^^
Soil hydrologic groups describe the runoff potential of different types of soil. There are four groups: A, B, C, D, where A has the least runoff potential and D has the most. See the United States Department of Agriculture (USDA) National Resources Conservation Service (NRCS) publication for more information: https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17757.wba

Two global layers of hydrologic soil group are available, 1) from FutureWater (available at: https://www.futurewater.eu/2015/07/soil-hydraulic-properties/) and 2) ORNL-DAAC’s HYSOGs250m (available at https://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html.)

**The FutureWater raster** provides numeric group values 1-4 14, 24 and 34. The Seasonal Water Yield model requires only values of 1/2/3/4, so you need to convert any values of 14, 24 or 34 into one of the allowed values.

**HYSOGs250m** provides letter values A-D, A/D, B/D, C/D and D/D. For use in this model, these letter values must be translated into numeric values, where A = 1, B = 2, C = 3 and D = 4. Again, pixels with dual values like A/D, B/D etc must be converted to a value in the range of 1-4.

In the United States, free soil data is available from the NRCS gSSURGO, SSURGO and gNATSGO databases: https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/geo/. They also provide ArcGIS tools (Soil Data Viewer for SSURGO and Soil Data Development Toolbox for gNATSGO) that help with processing these databases into spatial data that can be used by the model. The Soil Data Development Toolbox (available at https://www.nrcs.usda.gov/resources/data-and-reports/gridded-soil-survey-geographic-gssurgo-database) is easiest to use, and highly recommended if you use ArcGIS Desktop (it does not work in ArcGIS Pro or QGIS) and need to process U.S. soil data. Another option is SSURGO Portal (https://www.nrcs.usda.gov/resources/data-and-reports/ssurgo-portal), which is a new (beta) application independent from ArcGIS.

If desired, soil groups may also be determined from hydraulic conductivity and soil depths. FutureWater’s Soil Hydraulic Properties dataset also contains hydraulic conductivity, as may other soil databases. Table 1 below can be used to convert soil conductivity into soil groups.

|

**Table 1: Criteria for assignment of hydrologic soil groups (NRCS-USDA,
2007 Chap. 7)**

+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+
|                                                                                                                                                    | Group A     | Group B        | Group C        | Group D                                                               |
+====================================================================================================================================================+=============+================+================+=======================================================================+
| Saturated hydraulic conductivity of the least transmissive layer when a water impermeable layer exists at a depth between 50 and 100 centimeters   | >40 μm/s    | [40;10] μm/s   | [10;1] μm/s    | <1 μm/s (or depth to impermeable layer<50cm or water table<60cm)      |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+
| Saturated hydraulic conductivity of the least transmissive layer when any water impermeable layer exists at a depth greater than 100 centimeters   | >10 μm/s    | [4;10] μm/s    | [0.4;4] μm/s   | <0.4 μm/s                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+

.. _cn:

Curve Number
^^^^^^^^^^^^
It is recommended to do a literature search to look for values for CN that are specific to the area you're working in. If these are not available, look for values that correspond as closely as possible to the same types of land cover/soil/climate. If none of these more local values are available, general sources are recommended.

General curve numbers can be obtained from the SCS (now NRCS) report Urban hydrology for small watersheds (NRCS TR-55 1999). This report is commonly known as TR-55. Note that it was developed in the United States, so the values are a good place to start, but it is recommended to look for values more specific to your study area. The tables provide estimates of the curve number (CN) as a function of hydrologic soil group (HSG), cover type, treatment, hydrologic condition, antecedent runoff condition (ARC), and impervious area in the catchment.

For water bodies and wetlands that are connected to the stream, CN can be set to 99 (i.e. assuming that those pixels rapidly convey quickflow.)

When the focus is on potential flood effects, CN may be selected to reflect wet antecedent runoff conditions: CN values should then be converted to ARC-III conditions, as per Chapter 10 in NRCA-USDA guidelines (2007).


.. _bathymetry:

Bathymetry
----------
Bathymetry measures water depth. NOAA’s National Geophysical Data Center (NGDC) provides global bathymetry data with various spatial resolutions at https://www.ngdc.noaa.gov/mgg/bathymetry/relief.html.

ETOPO1 is a 1 arc-minute global relief model of Earth’s surface that integrates land topography and ocean bathymetry. It was built from numerous global and regional data sets, and is available in “Ice Surface” (top of Antarctic and Greenland ice sheets) and “Bedrock” (base of the ice sheets) versions. NGDC also provides regional and other global bathymetry datasets.

GEBCO produces public-domain global, gridded bathymetry data: https://www.gebco.net/data_and_products/gridded_bathymetry_data/


.. _buildings:

Building Footprints
-------------------
Maps of built infrastructure may be obtained from the city or open source data such as Open Street Map. https://www.openstreetmap.org


References
----------

Allen, R.G., Pereira, L.S., Raes, D. and Smith, M., 1998. "Crop evapotranspiration. Guidelines for computing crop water requirements." FAO Irrigation and Drainage Paper 56. Food and Agriculture Organization of the United Nations, Rome, Italy. Paper available at http://www.fao.org/3/x0490e/x0490e00.htm. Annex 2 available at: http://www.fao.org/3/X0490E/x0490e0j.htm.

Baer, SG, DJ Kitchen, JM Blair, and CW Rice. 2002. Changes in Ecosystem Structure and Function along a Chronosequence of Restored Grasslands. Ecological Applications 12:1688-1701.

Bernoux, M., MDS Carvalho, B. Volkoff, and CC Cerri. 2002. Brazil's soil carbon stocks. Soil Science Society of America Journal 66:888-896.

Brown, S. Estimating Biomass and Biomass Change of Tropical Forests: a Primer. FAO Forestry Department; 1997. Report for FAO Forestry Paper 134.

Brown, SL, PE Schroeder and JS Kern. Spatial distribution of biomass in forests of the eastern USA.Forest Ecology and Management 123 (1999) 81-90.

Brown, S. 2002. Measuring carbon in forests: current status and future challenges. Environmental Pollution 116:363-372.

Cairns, MA, S. Brown, EH Helmer, and GA Baumgardner. 1997. Root biomass allocation in the world's upland forests. Oecologia 111:1-11.

Cairns, MA, PK Haggerty, R. Alvarez, BHJ De Jong, and I. Olmsted. 2000. Tropical Mexico's recent land-use change: A region's contribution to the global carbon cycle. Ecological Applications 10:1426-1441.

Coomes, DA, RB Allen, NA Scott, C. Goulding, and P. Beets. 2002. Designing systems to monitor carbon stocks in forests and shrublands. Forest Ecology and Management 164:89-108.

Delaney, M., S. Brown, AE Lugo, A. Torres-Lezama, and NB Quintero. 1998. The quantity and turnover of dead wood in permanent forest plots in six life zones of Venezuela. Biotropica 30:2-11.

Detwiler, RP. 1986. Land Use Change and the Global Carbon Cycle: The Role of Tropical Soils. Biogeochemistry 2:67-93.

Droogers, P. & Allen, R.G. 2002. "Estimating reference evapotranspiration under inaccurate data conditions." Irrigation and Drainage Systems, vol. 16, Issue 1, February 2002, pp. 33–45

Edinburgh Centre for Carbon Management. The Establishing Mechanisms for Payments for Carbon Environmental Services in the Eastern Arc Mountains, Tanzania; 2007 May 2007.

Gaston, G., S. Brown, M. Lorenzini, and KD Singh. 1998. State and change in carbon pools in the forests of tropical Africa. Global Change Biology 4:97-114.

Glenday, J. 2006. Carbon storage and emissions offset potential in an East African tropical rainforest. Forest Ecology and Management 235:72-83.

Grace, J., J. San Jose, P. Meir, HS Miranda, and RA Montes. 2006. Productivity and carbon fluxes of tropical savannas. Journal of Biogeography 33:387-400.

Hamon, W. R. (1961). Estimating potential evapotranspiration. Journal of the Hydraulics Division, 87(3), 107-120.

Houghton, RA. 2005. Tropical deforestation as a source of greenhouse gas emissions. In: Tropical Deforestation and Climate Change, Moutinho and Schwartzman [eds.]. Instituto de Pesquisa Ambiental da Amazonia and Environmental Defense, Belem, Brazil.

Houghton, RA, and JL Hackler. 2006. Emissions of carbon from land use change in sub-Saharan Africa. Journal of Geophysical Research 111.

"Hydrologic Soil Groups."National Engineering Handbook, United States Department of Agriculture, National Resources Conservation Service, 2007, www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063.

The Intergovernmental Panel on Climate Change (IPCC). 2006. 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use. Prepared by the National Greenhouse Gas Inventories Programme, Eggleston, HS, L. Buendia, K. Miwa, T. Ngara, and K. Tanabe (eds). Institute for Global Environmental Strategies (IGES), Hayama, Japan. <https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html>.

Makundi, WR. 2001. Carbon mitigation potential and costs in the forest sector in Tanzania. Mitigation and Adaptation Strategies for Global Change 6:335-353.

Malhi, Y., D. Wood, TR Baker, et al. 2006. The regional variation of aboveground live biomass in old-growth Amazonian forests. Global Change Biology 12:1107-1138.

Malimbwi, RE, B. Solberg, and E. Luoga. 1994. Estimation of biomass and volume in miombo woodland at Kitungalo Forest Reserve Tanzania. Journal of Tropical Forest Science 7:230-242.

Munishi, PKT and TH Shear. 2004. Carbon Storage in Afromontane Rain Forests of the Eastern Arc Mountains of Tanzania: their Net Contribution to Atmospheric Carbon. Journal of Tropical Forest Science 16:78-93.

Nascimento, HEM, and WF Laurance. 2002. Total aboveground biomass in central Amazonian rainforests: a landscape-scale study. Forest Ecology and Management 168:311-321.

NRCS TR-55. 1999. Urban Hydrology for Small Watersheds. https://www.nrc.gov/docs/ML1421/ML14219A437.pdf. Extracted CN tables also at https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/cn-tables.

Post, WM, WR Emanuel, PJ Zinke, and AG Stangenberger. 1982. Soil carbon pools and world life zones. Nature 298:156-159.

Post, WM, KC Kwon. 2000. Soil carbon sequestration and land-use change: processes and potential. Global Change Biology 6:317-327.

Ruesch A, and HK Gibbs. 2008. New IPCC tier-1 global biomass carbon map for the year 2000. Available:https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html.

Silver, WL, R. Ostertag, and AE Lugo. 2000. The potential for carbon sequestration through reforestation of abandoned tropical agricultural and pasture lands. Restoration Ecology 8:394-407.

Tiessen, H., C. Feller, EVSB Sampaio, and P. Garin. 1998. Carbon Sequestration and Turnover in Semiarid Savannas and Dry Forest. Climatic Change 40:105-117.

Tilman, D., J. Hill, and C. Lehman. 2006. Carbon-Negative Biofuels from Low-Input High-Diversity Grassland Biomass. Science 314:1598-1600.

Vagen, TG, R Lal, and BR Singh. 2005. Soil carbon sequestration in sub-Saharan Africa: A review. Land Degradation & Development 16:53-71.

Zhang, Q, and CO Justice. 2001. Carbon Emissions and Sequestration Potential of Central African Ecosystems. AMBIO 30:351-355.
