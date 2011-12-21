.. _roadmap:

******************************************
What's coming up for Marine InVEST models?
******************************************

Planned modifications to InVEST 2.0 models
==========================================

Wave energy
-----------
(Tier 1)

The goal of the wave energy model is to provide planners with wave energy siting information for growing energy demand. The wave energy model calculates potential wave power and wave energy that can be captured by currently available technology. The model evaluates the economic feasibility of potential wave energy conversion facilities using a cost-benefit analysis. The spatially explicit model outputs allow users to examine potential conflicts with other uses of the marine environment (e.g. fishing, shipping, oil rigs, etc) that co-occur with regions suitable for wave power plants.  Thus, the model helps decision-makers understand where best to install a facility while balancing desires for the greatest captured wave energy and the least effect on other human uses in coastal and ocean ecosystems.

What's coming up in future releases?

+ Incorporating local wave input data: The current version includes global and regional wave information as base model input, which allow first approximation of wave energy anywhere in the world ocean. In future releases, the model will allow users to provide their own wave input data if desired.
+ Valuing economic feasibility at a global and local scale: The current version allows economic valuation of a wave energy conversion facility at a local scale. In future releases, the model will allow users to evaluate wave energy projects at global and regional scales using global ports data.


Coastal Vulnerability
---------------------
(Tier 0)

The Marine InVEST Coastal Vulnerability model maps the location of people living in coastal areas and the relative exposure of coastal communities and environments to erosion and flooding during large storms.  In particular, it highlights the shoreline protection services provided by natural habitats. Outputs from the model can be used in a number of ways including: helping to understand what factors (natural and social) make a stretch of coastline more or less vulnerable to erosion and flooding, estimating the change in exposure that might result from a planned management action, and informing where and how coastal development might occur.  The Coastal Vulnerability Model can also be run to help identify regions where the more quantitative (Tier 1) Marine InVEST Coastal Protection model might best be applied (see upcoming marine models, below).

Limitations of current model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
+ Wind fetch distances are only computed for 16 directions, separated by 22.5 degrees
+ Wind speed values used to estimate wind exposure and characteristics of wind-generated waves are statistics of highest wind speeds, not raw wind speed values
+ Maximum fetch distance computed by the model is 50km.  This is also the threshold to determine whether a shoreline segment is exposed to the open ocean.
+ We only use one value of water depth to compute wind-generated waves for the whole AOI.
+ Surge potential of a sheltered shoreline segment is the same as the surge potential of the closest exposed segment.
+ Effect of structures is modeled by decreasing the ranking of a cell adjacent to a structure by 1 point.  We do not estimate the length of influence of the structure. We do not model its impacts on subtidal environment.
+ Map of tidal range is not included

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Inclusion of more social indicators to link vulnerability to populations
+ Simple valuation methods
+ Allow users to define regions that are shallow in the area of interest.
+ Inclusion of tidal range maps



Finfish Aquaculture
-------------------
(Tier 1)

The current version of the InVEST aquaculture model analyzes the production of farmed Atlantic salmon (*Salmo salar*) based on farming practices, water temperature and economic factors. While the current model quantifies the economic benefits of salmon aquaculture, it does not quantify the associated environmental costs. Future versions of the aquaculture model will allow users to quantify the environmental impacts of salmon aquaculture, including the release of farm wastes and the transfer of disease vectors from farmed to wild populations. These impacts may have effects on other environmental services, such as water quality and wild salmon fisheries. When combined with the full suite of InVEST model outputs, this added functionality will allow InVEST users to explore the environmental costs and benefits of Atlantic salmon production, as well as subsequent effects on other environmental services. In addition, subsequent releases will allow users to model production of other finfish species and shellfish (see "Shellfish Production" in the "Additional Models Under Development" section). 

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Quantification of farm waste production. Outputs will include dissolved and particulate wastes generated as a byproduct of Atlantic salmon production. These outputs will be available for use in other InVEST models (e.g., water quality, habitat quality, fisheries) to assess impacts of Atlantic salmon aquaculture on other environmental services.
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
+ Additional functionality to analyze aesthetics from a viewer's perspective.  The tool will offer viewshed output maps for up to 20 different locations.  
+ Incorporation of visual quality ratings for various land use/land cover (LULC) types
+ Enabling users to map relative changes in aesthetic quality across multiple scenarios
+ Incorporation of global forest cover dataset to control for areas that are not visible because forest cover
+ Provision of higher resolution topographic base data (SRTM 3-90m resolution)

Marine Habitat Risk Assessment
-----------------------------
(Tier 0)

The InVEST Habitat Risk Assessment allows users to assess the risk posed to coastal and marine habitats by human activities and the potential consequences of exposure for the delivery of environmental services and biodiversity. Outputs from the model are useful for understanding the relative risk of human activities and climate change on habitats within a study region and among alternative future scenarios and for identifying which habitats are of high enough quality to provide the services people care about.

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Connectivity scoring: The current model allows users to score connectivity of habitat patches based on known dispersal distances. In future releases, the model will calculate the distance to the nearest neighboring habitat patch to improve the connectivity scoring.
+ Decay exposure: The current model assumes that exposure to stressors is uniform in space within a stressor's user-defined zone of influence. In future releases, the model will allow for the exposure to decay over space from the center of a stressor's location to the outer edge of its zone of influence. 
+ Spatial variation in intensity scores: In the current version the intensity of each stressor is scored for the whole study region.  In future versions of the model, the user will be able to input a stressor intensity layer so that stressor intensity varies within the study region.

Overlap Analysis: Fisheries (Tier O) and Recreation (Tier O)
------------------------------------------------------------
(Tier 0)

The InVEST Overlap Analysis Model was designed to produce maps that can be used to identify marine and coastal areas that are most important for human use. The model produces a map of hotspots for human activities (e.g., fishing activity/fishing grounds, various recreational activities) across as many human uses as the users chooses to include.  Outputs can be used to help decision-makers weigh potential conflicts between sectors of spatially-explicit management options that may involve new activities or infrastructure.

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Functionality for raster inputs: The current model accepts point and polygon data but not raster inputs.  We anticipate that users working with fisheries data, in particular, may have raster data that they would like to use as model inputs.  Future releases will accommodate the use of raster data.
+ Output options - absolute values:  The current model calculates an Importance Score based on inputs about where human uses occur and, optionally, their relative weighting.  Users can base these weights on a variety of metrics, including catch and revenue, but the outputs are still scaled to a score, not an absolute value.  In future releases, users will have the option to output Importance Scores and absolute values.


Additional models under development
===================================

Fisheries production
--------------------

Simple population models
^^^^^^^^^^^^^^^^^^^^^^^^
(Tier 1)

A generic and flexible model will be included in InVEST for estimating the quantity and value of fish harvested by commercial fisheries. It will be appropriate for use with single species or groups of species. For example, one could choose to parameterize it for each of the top 3 commercially important species in a region. In its most general form, the model estimates the annual production of fish, which is the biomass in the previous year multiplied by a function that captures changes to habitat, fishing, or from climate change. The model incorporates the impacts of biogenic habitat on the survival and fecundity of different life- stages of target species. We use a matrix structure to transition fish from one year to the next. The matrix is parameterized using information on stage (or age) specific survival, fecundity and harvest. Scenarios are represented as changes to fecundity, survival and harvest rate. It is possible to adjust the temporal duration of the model runs according to the life-history characteristics of the species being modeled (e.g., fast or slow turnover species).  Individual models are in development for spiny lobster in Belize, Pacific salmon in British Columbia and Dungeness crab in Washington State, and are being tested for those species in other geographies and generalized for species with similar life histories.

Inputs
""""""
+ Spatial delineation of areas to include in the model
+ Age- and area-specific estimates of number of adults
+ Sector-specific catches or catch-per-unit-effort, by area if available
+ Harvest rates (fixed or variable)
+ Proportion of age-specific returns
+ Productivity (e.g. pre-smolt/spawner; recruit/spawner)
+ Survival estimates (age- or stage-specific and/or area-specific)
+ Table describing influence of human activity or climate change on survival and productivity.
+ Cost and price information for the commercial sector   

Outputs
"""""""
+ Catch partitioned by sector (e.g. commercial and recreational)-area-specific if data exist.
+ Value of commercial catch

Future features
^^^^^^^^^^^^^^^
Future versions of InVEST will also facilitate the use of more complex food-web models (e.g., Ecopath with Ecosim and Atlantis). The InVEST interface will wrap around these more complex models so that parameters can be compared to outputs from other service models such as aquaculture, wave energy, and coastal protection.


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


Coastal Protection
------------------
(Tier 1)

The InVEST Coastal Protection model quantifies the protective benefits that natural habitats provide against erosion and inundation in nearshore environments. It is composed of two sub-models: a Profile Generator and a Nearshore Wave and Erosion model. In the absence of local data detailing the profile of the shoreline, the Profile Generator model helps users combine information about the local bathymetry and backshore to generate a 1-Dimensional (1D) cross-shore (perpendicular to the shoreline) beach profile. The Nearshore Waves and Erosion model uses the shoreline profile to compute summaries of nearshore wave information and outputs the total water level and the amount of shoreline erosion in the presence and absence of nearshore marine habitats (e.g., coral or oyster reefs, vegetation, sand dunes).

Limitations of current model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
+ It is a 1D model based on linear wave theory. We ignore any wave processes that occur over a complex bathymetry.  We also ignore any non-linear wave processes, especially when they encounter natural habitats.
+ We model wave attenuation over coral and oyster reef in a simple way, using empirical methods.
+ We assume that habitats are not affected (e.g., uprooted or broken) by a storm.  Also, we assume that they have a constant friction and drag coefficient, and is independent of the level of turbulence in the water column.
+ We use simple beach and consolidated sediment erosion models that ignore any dynamic feedback between waves and bed.

What's coming up in future releases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+ Valuation of the role of natural habitats.
+ Guidance on how to model marsh profiles.
+ Estimation of marsh edge erosion.
+ Better estimation of erosion of muddy substrates.
+ Inclusion of diffration effects in estimation of wave heights leeward of oyster reefs.
+ Inclusion of structures in the model and indication of their impacts on subtidal habitats and adjacent properties, as well as quantification of amount overtopping that occurs during storms.
+ Inclusion of more friction and drag coefficient that are a function of turbulence level in the water column.
+ Option to batch process Nearshore Wave and Erosion model to run it for multiple locations at once.
+ Visual representation of outputs of the Nearshore Wave and Erosion model in map form.
+ Inclusion of stand-alone tools to model wave evolution in the presence or absence of specific natural habitats.
+ Inclusion of wind-wave generation tool to estimate wave height and wave period based on fetch distance and wind speed.


Water quality
-------------
(Tier 1)

Although water quality is not an environmental service per se, it is an important intermediate output that can connect other InVEST models. The water quality (WQ) model simulates the movement and fate of water quality variables (state-variables) in response to changes in ecosystem structure driven by various management decisions and human activities. Hence, this model assesses how management and human activities influence the water quality in coastal and estuarine ecosystems. The model can be used for diagnosing the type of WQ problems (e.g., hypoxia, eutrophication, high concentrations of bacteria and toxic chemicals) expected, identifying environmental control aspects for water quality, and setting water quality standards. The WQ model can be linked with other Marine InVEST models to evaluate environmental services relating to fisheries, aquaculture, habitat quality, and recreation. Consequently, the WQ model can help decision-makers establish management strategies for the desirable use of a water body.

WQ Model Tier 1a
^^^^^^^^^^^^^^^^
Initial development is underway of a simplified physical transport model that will give decision-makers a qualitative assessment of where water quality issues may arise in an estuarine system. The model will output residence time, which when coupled with river and nutrient inputs, will allow a general look at where water quality issues such as hypoxia or eutrophication may occur. The model will be based on a one- or two- dimensional finite segment configuration (the choice is set by the characteristics of the estuarine system) that incorporates physical transport processes driven by river discharge and tidal dispersion. The model will simulate mass transport along the main channel of a system.

WQ Model Tier 1b
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

+ Assesses areas in an estuary that are at-risk to water quality issues

The WQ Model Tier 1b:

+ Produces spatially explicit concentration maps of water quality state variables
+ Evaluates watershed/coastal management strategies to maintain desirable water quality standards


Carbon storage and sequestration
--------------------------------
(Tier 1)

Marine and terrestrial ecosystems help regulate Earth’s climate by adding and removing greenhouse gases (GHGs) such as carbon dioxide (CO2) from the atmosphere. Coastal marine plants such as mangroves and seagrasses store large amounts of carbon in their sediments, leaves and other biomass. By storing carbon in their standing stocks, marine ecosystems keep CO2 out of the atmosphere, where it would otherwise contribute to climate change. In addition to storing carbon, marine ecosystems accumulate carbon in their sediments continually, creating large reservoirs of long-term carbon sequestration. Management strategies that change the cover of marine vegetation, such as seagrass restoration or mangrove clearing, can change carbon storage and the potential for carbon sequestration on seascape. The InVEST Carbon Model estimates how much carbon is stored in coastal vegetation, how much carbon is sequestered in the sediments, and the economic value of storage and sequestration. The approach is very similar to that of the terrestrial carbon model.

Inputs
^^^^^^
+ Maps of the distribution of nearshore marine vegetation (i.e. mangroves, salt marshes)
+ Data on the amount of carbon stored in four carbon ‘pools’: aboveground biomass, belowground biomass, sediments, and dead organic matter.
+ Data on the rate of carbon accumulation in the sediments for each type of marine vegetation.
+ Additional data on the market or social value of sequestered carbon and its annual rate of change, and a discount rate can be used in an optional model that estimates the value of this environmental service to society.

Outputs
^^^^^^^
+ Carbon storage (Mg C/ha).
+ Carbon sequestration (Mg C/ha/yr).
+ Economic value of carbon storage and sequestration.

Shellfish Production (wild and aquacultured)
---------------------
(Tier 1)

In this model, we map how incremental changes in ecosystem structure (e.g., water quality attributes including temperature, salinity, nutrient availability), changes to wild harvest or operations at specific aquaculture facilities affect shellfish production and commercial value and nutrient filtration.  We use a framework similar to the Farm Aquaculture Resource Management model (FARM; J. G. Ferreira, A.J.S. Hawkins, S.B. Bricker, 2007. Management of productivity, environmental effects and profitability of shellfish aquaculture – the Farm Aquaculture Resource Management (FARM) model. Aquaculture, 264, 160-174), which has been developed for assessment of individual coastal and offshore shellfish aquaculture farms.

The model contains two linked sub-models that represent 1) shellfish individual growth and 2) shellfish population dynamics.

Inputs
^^^^^^
+ shellfish growing area dimension (e.g., width, length, depth – if suspended)
+ shellfish cultivation (e.g., species, size at outplanting for aquaculture or settlement for wild stock, target harvest size or weight, density of individuals)
+ (optional for commercial valuation) product (e.g., half shell or shucked oyster), market price of product, harvesting and processing costs, facility operation costs (aquaculture facilities)
+ environmental variables (e.g., water temperature and current speed; available food as concentration of Chlorophyll a, dissolved inorganic nitrogen - DIN, particulate organic matter - POM); these can be from local data or, when available, from the InVEST Water Quality models.

Outputs
^^^^^^^
+ harvestable biomass
+ harvestable number of animals
+ filtration of Chlorophyll a, DIN and POM
+ (optional for commercial valuation) net revenue of product

Recreation
----------
(Tier 1)

The forthcoming InVEST recreation model predicts where people go to recreate (or, more specifically, the spread of person-days of recreation in space).  It does this using attributes of places, such as natural features (e.g., parks), built features (e.g., roads) and human uses (e.g., industrial activities) among others.  Because these attributes are often good predictors of visitation rates, the recreation model will come pre-loaded with data about these and other attributes that are linked to attractiveness.  We will also allow users to upload their own spatial data if they have information about additional attributes that might be correlated to people's decisions about where to recreate.  Then, armed with these estimates, users will be able to use the model to predict how future changes to the landscape will alter visitation rate.  The tool will output maps showing current patterns of recreational use and, optionally, maps of future use under different scenarios.

Inputs
^^^^^^
+ area of interest

Outputs
^^^^^^^
+ person-days of recreation in grid cells within the area of interest


.. rubric:: Footnotes

.. [#f1] The model provides guidance to replace missing data with approximations in data poor regions, and on how to prepare the inputs.




