.. _roadmap:

******************************************
What's coming up for Marine InVEST models?  
******************************************

Planned modifications to InVEST 2.0 models
==========================================

Wave energy
-----------
(Tier 1)

The goals of the wave energy model in marine InVEST are to map and value wave energy and to examine potential trade-offs that might arise when siting wave energy conversion facilities. The model helps decision-makers understand where best to install a facility while balancing desires for the greatest captured wave energy and the least effect on coastal and ocean ecosystems and other human uses.

What's coming up in future releases?

+ Allowing users to provide sea state data (wave input data)
+ Providing global ports data for use with economic valuation at regional and global scales


Coastal Vulnerability 
---------------------
(Tier 0)

The Marine InVEST Coastal Vulnerability model maps the location of people living in coastal areas and the relative exposure of coastal communities and environments to erosion and flooding during large storms. In particular, it highlights the shoreline protection services provided by natural habitats. Outputs from the model can be used in a number of ways including: helping to understand what factors (natural and social) make a stretch of coastline more or less vulnerable to erosion and flooding, estimating the change in exposure that might result from a planned management action, and informing where and how coastal development might occur. The Coastal Vulnerability Model can also be run to help identify regions where the more quantitative (Tier 1) Marine InVEST Coastal Protection model might best be applied (see upcoming marine models, below).

Limitations of current model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
+ Only kelp and seagrass are taken into account in the detection of natural habitats
+ Wind-generated waves are computed from winds measured at a single location and do not capture regional variation of wind fields
+ The model does not take into account regional variation in wave climate
+ Map of tidal range is not included

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Inclusion of density of road network as a proxy for the social indicator of amount of infrastructure
+ Inclusion of nearshore relief as environmental feature to identify coastal regions that are higher than others and thus less prone to inundation
+ Inclusion of more natural habitats
+ Estimation of wind-generated waves from more than one wind input in order to better capture variation of wind field around complex and long shorelines
+ Addition of oceanic wave exposure to capture variation of oceanic wave climate along region of interest
+ Inclusion of tidal range maps


Finfish Aquaculture
-------------------
(Tier 1)

The current version of the InVEST aquaculture model analyzes the production of farmed Atlantic salmon (*Salmo salar*) based on farming practices, water temperature, and economic factors. While the current model quantifies the economic benefits of salmon aquaculture, it does not quantify the associated environmental costs. Future versions of the aquaculture model will allow users to quantify the environmental impacts of salmon aquaculture, including the release of farm wastes and the transfer of disease vectors from farmed to wild populations. These impacts may have effects on other ecosystem services, such as water quality and wild salmon fisheries. When combined with the full suite of InVEST model outputs, this added functionality will allow InVEST users to explore the environmental costs and benefits of Atlantic salmon production, as well as subsequent effects on other ecosystem services. In addition, subsequent releases will allow users to model production of shellfish and other finfish species.
 
What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Quantification of farm waste production. Outputs will include dissolved and particulate wastes generated as a byproduct of Atlantic salmon production. These outputs will be available for use in other InVEST models (e.g., water quality, habitat quality, fisheries) to assess impacts of Atlantic salmon aquaculture on other ecosystem services.
+ Quantification of impacts of parasitic sea-lice. Disease outbreaks and parasitism cause substantial financial burdens to aquaculturists (e.g., due to costs of treatment, foregone revenue due to culling of infected fish). In addition, high stocking densities of farmed fish increase the risk of transmission of sea-lice from farmed to wild salmon. This sub-module will allow users to quantify the impact of parasitic sea-lice on farmed salmon production and the risk of disease transmission to wild salmon populations.
+ Guidance for modifying the Atlantic salmon model for other cultured marine finfish.
+ A shellfish aquaculture module. This model will quantify volume, economic value, filtration and production of wastes of cultured shellfish (e.g., oyster, shrimp).
+ Other changes. The current model operates at a daily time step (requiring daily temperature data), but future iterations will allow for monthly or yearly temperature inputs.


Aesthetic Quality
-----------------
(Tier 0)

This model examines the production of aesthetic views by the coastal and marine environment. It can be used to examine how views are likely to be impacted by various marine and coastal activities (e.g. wave energy facilities, aquaculture facilities, coastal clear cuts, coastal development, mining, etc).

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Incorporation of global forest cover dataset to control for areas that do not have visibility because of canopy cover
+ Providing higher resolution global topography base data (SRTM 3-90m resolution)
+ Allowing users to provide two-point feature classes contributing to negative aesthetic quality (for both current conditions and future scenarios). This will enable mapping the change in aesthetic quality from current to future scenarios.


Additional models under development
===================================

Fisheries production
--------------------

Visualizing fisheries tradeoffs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Tier 0)

This tool will allow users to visualize tradeoffs between commercial fishing and other human activities such as recreation or the production of wave energy. Using data on the location and relative importance of multiple fisheries, in conjunction with the location of alternative uses, this simple tool will explore how fishing could change under a variety of management scenarios.

Simple population models
^^^^^^^^^^^^^^^^^^^^^^^^
(Tier 1)

A generic and flexible model will be included in InVEST for estimating the quantity and value of fish harvested by commercial fisheries. It will be appropriate for use with single species or groups of species. For example, one could choose to parameterize it for each of the top 3 commercially important species in a region. In its most general form, the model will estimate annual production of fish, which is the biomass in the previous year multiplied by a function that captures changes to habitat, fishing, or from climate change. We will use a matrix structure to transition fish from one year to the next. The matrix is parameterized using information on stage (or age) specific survival, fecundity, and juvenile harvest. Scenarios are represented as changes to fecundity, survival, and harvest rate. It will be possible to adjust the temporal duration of the model runs according to the life-history characteristics of the species being modeled (e.g., fast or slow turnover species).

Inputs
""""""
+ Spatial delineation of areas to include in the model
+ Age- and area-specific estimates of number of adults
+ Sector-specific catches, by area if available
+ Harvest rates (fixed or variable)
+ Proportion of age-specific returns
+ Productivity (e.g. pre-smolt/spawner; recruit/spawner)
+ Survival estimates (age- or stage-specific and/or area-specific)
+ Table describing influence of human activity or climate change on survival and productivity.
+ Cost and price information for the commercial sector.
 
Outputs
"""""""
+ Catch partitioned by sector (e.g. commercial and recreational). Area-specific if data exist.
+ Value of commercial catch

Future features
^^^^^^^^^^^^^^^
In subsequent releases of InVEST, the generic fisheries model will be extended to incorporate impacts of biogenic habitat on the survival and fecundity of different life- stages of target species. Future versions of InVEST will also facilitate the use of more complex food-web models (e.g., Ecopath with Ecosim and Atlantis). The InVEST interface will wrap around these more complex models so that parameters can be compared to outputs from other service models such as aquaculture, wave energy, and coastal protection.


Recreational fishing sub-model
------------------------------
(Tier 1)

The Marine InVEST recreational fishing submodel allows users to evaluate the recreational benefits of improving management of marine and coastal fisheries. This model is directly linked to the Marine InVEST fisheries production model and is designed to reflect changes in the output of the fisheries production model as well as simple changes in the management of the recreational sector (e.g. allocation of more fish to the recreational sector). In the event that a scenario indicates increases in fish abundance available for recreational harvest, this model predicts the amount of recreational fishing effort required to catch those additional fish. This can be thought of as a proxy measure for the potential supply of recreational opportunity in the fisheries sector. With additional local data, this potential supply of fishing opportunity can be translated into potential benefits that could be realized by recreational anglers, recreational fishing operators, and a proxy measure of expenditures in the local economy.

Inputs
^^^^^^
+ Change in fish abundance (predicted by InVEST fisheries model)
+ Estimate of catch per unit effort for each target species in the recreational sector
+ Coefficient that determines the number of fish that will be available for catch by recreational anglers. This parameter can be changed to reflect alternative management scenarios or it can be based on current management policy.
+ Site-appropriate estimate of consumer surplus per day of fishing
+ Site-appropriate measure of angler expenditures per trip.
+ Site-appropriate measures of operating costs (fuel costs, labor costs, docking, etc.).

Outputs
^^^^^^^
The primary output from the recreational fishing sub-model is an estimate of the amount of effort (number of trips) that would be required to catch the number of fish allocated to the recreational sector as predicted by the InVEST fisheries production model. The estimated effort required to catch these fish represents an upper bound on effort and could be much lower given constraints on fleet capacity and the number of anglers visiting the area to participate in recreational fishing. In additional to estimating an upper bound on fishing effort, the model also generates estimates of the economic benefits accruing to:

+ Recreational anglers (Consumer surplus per trip scaled by the number of trips).
+ Recreational fishing operators (net revenue per trip)
+ Expenditures introduced to the local economy

Recreation
----------
(Tier 0)

The first step in evaluating the benefits from marine and coastal recreation activities is to identify the areas that are used for different recreational activities. The Marine InVEST Tier 0 recreation model provides users with a simple framework that will help to visualize and rank marine and coastal areas that are used for recreational activities. The basic mapping tool aggregates existing data on current usage patterns and ranks areas according to the number of recreational activities occurring in a given area. The approach also provides users with the option to weight the importance of different areas as a factor of the distance from a given area to the nearest population center or access point. This distance-based weighting factor is intended to account for situations in which two areas are identical in terms of the number of recreational activities taking place in each area, but one area is more accessible due to its proximity to a population center or access point. By ‘discounting’ more remote areas, users can account for the importance of accessibility in determining a particulars site’s ranking. In situations where more detailed spatially explicit data on the intensity of human usage or the quality of sites is available, the mapping tool allows for their incorporation into the rankings of sites.

Inputs
^^^^^^
+ The only *required input* for the recreational mapping tool is a set of GIS layers of recreation use. (Examples: Areas used for recreational fishing; surfspots; divespots; beaches; sea kayaking routes; wildlife viewing areas) The user is prompted to identify an ‘area of interest’ to run the analysis and these recreational layers should fall within this area of interest.
+ To weight areas according to distance-based accessibility, a GIS layer of major populations centers and/or marine access points is used to compute the weighting factor that is based on the distance from these ‘origins’ to the marine and coastal areas where a set of recreational activities occurs. 
+ If users have additional data on the intensity of usage or quality of sites for the included recreational activities, this information can be included to inform site rankings (or weights).

Outputs
^^^^^^^
The primary output is a map highlighting the relative importance of various areas for the set of recreation activities included by the user. These maps can be used to highlight areas of relative importance to the recreational sector. With this knowledge, users can then use these maps in conjunction with additional maps derived from other InVEST modules to begin to create a larger picture of marine use activities and to assist in the design of marine protected areas or marine spatial plans. If information about the intensity of use or quality of sites is included and is changed by scenarios, these maps can show change in recreational importance scores as a function of alternative scenarios.


Coastal protection from erosion and inundation
----------------------------------------------
(Tier 1)

This model values the role that is played by vegetation and dunes in mitigating coastal flooding and erosion. It computes and values the amount of erosion and flooding that was avoided because of the presence of natural habitats. The model also simulates the stability and impacts of seawalls on the shoreline. Outputs from the model are useful for understanding how marine vegetation and sand dunes protect coastal property. We recommend running this model after the Coastal Vulnerability model (“Tier 0” model released with InVEST 2.0), since the inputs are similar and the Coastal Vulnerability model helps understand the general wave and wind field near a site of interest. However, these models can be run separately.

Inputs
^^^^^^
Model inputs consist of information about the:

+ Shoreline profile [#f1]_ (sediment size, nearshore bathymetry, foreshore slope, sand dune profile)
+ Locations of biogenic habitats (coral reefs, marshes, seagrass beds, …) and/or artificial structures (like seawalls)
+ Description of a single large storm event [#f1]_ (100-yr wave height, typical large windstorm, ...)
+ Tide level during storm and any water surface elevation change from baseline (because of sea-level rise or El Niño/La Niña-Southern Oscillations).

Outputs
^^^^^^^
From these inputs, the model:

+ Plots the wind and wave field during the storm event
+ Estimates total water level at the shoreline caused by the action of waves and winds
+ Estimates the amount of avoided shoreline retreat (meters eroded), area flooded, property damage ($), and numbers of people affected because of the presence of natural habitats.
+ Simulates the extent of long-term erosion on either side of seawalls and estimates the stability as well as the amount of overtopping and type of damage that might be expected landward of that structure.


Water quality
-------------
(Tier 1)

Although water quality is not an ecosystem service per se, it is an important intermediate output that can connect other InVEST models. The water quality (WQ) model simulates the movement and fate of water quality variables (state-variables) in response to changes in ecosystem structure driven by various management decisions and human activities. Hence, this model assesses how management and human activities influence the water quality in coastal and estuarine ecosystems. The model can be used for diagnosing the type of WQ problems (e.g., hypoxia, eutrophication, high concentrations of bacteria and toxic chemicals) expected, identifying environmental control aspects for water quality, and setting water quality standards. The WQ model can be linked with other Marine InVEST models to evaluate ecosystem services relating to fisheries, aquaculture, habitat quality, and recreation. Consequently, the WQ model can help decision-makers establish management strategies for the desirable use of a water body.

WQ Model Tier 1a
^^^^^^^^^^^^^^^^
Initial development is underway of a simplified physical transport model that will give decision-makers a qualitative assessment of where water quality issues may arise in an estuarine system. The model will output residence time, which when coupled with river and nutrient inputs, will allow a general look at where water quality issues such as hypoxia or eutrophication may occur. The model will be based on a one- or two- dimensional finite segment configuration (the choice is set by the characteristics of the estuarine system) that incorporates physical transport processes driven by river discharge and tidal dispersion. The model will simulate mass transport along the main channel of a system.

WQ Model Tier 1a
^^^^^^^^^^^^^^^^
The second development underway will tie the water quality variables (e.g., nutrients or dissolved oxygen) to the physical transport model. Although the targeted time scale is monthly to seasonal, we will first produce annual-average distributions of water quality state variables. Box modeling approaches are also being considered to accommodate more flexible applications across multiple scales in coastal and estuarine systems, which may be appropriate for data rich areas.

Inputs
""""""
The WQ model requires:

+ Estuarine coefficient tables

  + Geomorphology (e.g., depth, width, and length of an estuarine system)
  + River discharge input at the upstream boundary
  + Tidal dispersion coefficient, which can be estimated using salinity distribution. We will also provide a lookup table or an empirical equation using tidal strength to estimate tidal dispersion coefficient in places with limited data.

+ WQ state variables (e.g., nutrients, metals, viruses, toxic chemicals, dissolved oxygen, etc.). Nitrogen and Phosphorus would be the first target variables.

+ Loading

  + Point sources, loading from discharge pipes, sewage treatment outfall, aquaculture farms, etc.
  + Non-point sources, loading from agricultural, urban and suburban runoff, groundwater, etc.
  + Watershed models can be used to estimate both point and non-point source loading from land.

+ Kinetic coefficients

Outputs
"""""""
The WQ Model Tier 1a:

+ Produces spatially explicit maps of residence time in an estuary
+ Assesses areas in an estuary that are at-risk to water quality issues

The WQ Model Tier 1b:

+ Produces spatially explicit concentration maps of water quality state variables
+ Evaluates watershed/coastal management strategies to maintain desirable water quality standards


Habitat quality
---------------
(Tier 0)

Like water quality, habitat quality is not a service per se, but rather an important component of systems that links to various ecosystem services. This model is very similar to the terrestrial InVEST biodiversity model. In fact, the terrestrial InVEST biodiversity model can currently be used in marine systems. This model assesses how human activities, climate change, and associated stressors affect the quality of coastal and marine habitats for biodiversity and ecosystem services. Impacts of activities (e.g., aquaculture, coastal development, etc.) on habitats (e.g., eelgrass, mangroves, etc.) is a function of the exposure and the sensitivity of each habitat to each activity and related stressor. Exposure depends on the extent of geographic overlap between habitats and human activities, the duration of time that the activity and habitat overlap, and the degree to which management strategies mitigate impacts. Sensitivity depends on the effects of activities on habitat area and density, and the ability of habitats to recover from these effects (i.e., through life history traits such as recruitment and regeneration rates). Outputs from the model are useful for understanding the relative impact of human activities and climate change on habitats within a study region and among alternative future scenarios, and to identify which habitats are of high enough quality to provide the services people care about. The model will help to prioritize areas for conservation and restoration and inform the design and configuration of marine spatial plans.

Inputs
^^^^^^
+ Maps of the distribution and abundance of coastal and marine habitats of interest (e.g., eelgrass beds, kelp and mangrove forests, rocky intertidal reefs, soft bottom).
+ Maps of distribution and intensity of human activities (e.g., numbers and types of finfish aquaculture pens, length of coastal hardening) and climate stressors (e.g., water temperature, sea-level rise).
+ Information about temporal variability in human activities and climate stressors.
+ Sensitivity matrix of each habitat to each stressor. These values can be generated based on expert opinion, or on information in the literature about the effects activities and climate change on habitats.
+ Information about current management approaches used to mitigate impact of human activities.

Outputs
^^^^^^^
From these inputs, the model will produce:

+ A map of the relative impact of each activity or climate change on each habitat type.
+ A map of the total impact of all activities and climate change on each habitat type.
+ A map of change in habitat quality for biodiversity (on a relative scale) and for ecosystem services (in terms of change in key parameters for service delivery, such as density of eelgrass shoots or mangrove trunks).


Carbon storage and sequestration
--------------------------------

Marine and terrestrial ecosystems help regulate Earth’s climate by adding and removing greenhouse gases (GHGs) such as carbon dioxide (CO2) from the atmosphere. Coastal marine plants such as mangroves and seagrasses store large amounts of carbon in their sediments, leaves and other biomass. By storing carbon in their standing stocks, marine ecosystems keep CO2 out of the atmosphere, where it would otherwise contribute to climate change. In addition to storing carbon, marine ecosystems accumulate carbon in their sediments continually, creating large reservoirs of long-term carbon sequestration. Management strategies that change the cover of marine vegetation, such as seagrass restoration or mangrove clearing, can change carbon storage and the potential for carbon sequestration on seascape. The InVEST Carbon Model estimates how much carbon is stored in coastal vegetation, how much carbon is sequestered in the sediments, and the economic value of storage and sequestration. The approach is very similar to that of the terrestrial carbon model.

Inputs
^^^^^^
+ Maps of the distribution of nearshore marine vegetation (i.e. mangroves, salt marshes)
+ Data on the amount of carbon stored in four carbon ‘pools’: aboveground biomass, belowground biomass, sediments, and dead organic matter.
+ Data on the rate of carbon accumulation in the sediments for each type of marine vegetation.
+ Additional data on the market or social value of sequestered carbon and its annual rate of change, and a discount rate can be used in an optional model that estimates the value of this ecosystem service to society.

Outputs
^^^^^^^
+ Carbon storage (Mg C/ha).
+ Carbon sequestration (Mg C/ha/yr).
+ Economic value of carbon storage and sequestration.



.. rubric:: Footnotes

.. [#f1] The model provides guidance to replace missing data with approximations in data poor regions, and on how to prepare the inputs.




