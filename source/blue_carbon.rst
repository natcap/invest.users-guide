.. _blue-carbon:

*****************
Blue Carbon Model
*****************

Summary
=======
 
Marine and terrestrial ecosystems help regulate Earth’s climate by adding and removing greenhouse gases (GHGs) such as carbon dioxide (CO\ :sub:`2`) from the atmosphere.  Coastal marine plants, mangroves and seagrasses in particular, store large amounts of carbon in their sediments, leaves and other biomass. By storing carbon, marine ecosystems keep CO\ :sub:`2` out of the atmosphere, where it would otherwise contribute to climate change.  In addition to storing carbon, marine ecosystems continually accumulate carbon in their sediments, creating large reservoirs of long-term sequestered carbon. Management activities that change the cover of coastal vegetation, such as seagrass restoration or mangrove clearing, can change carbon storage and the potential for carbon sequestration on a seascape.  With estimates of the social value, or where available, market value of carbon, the InVEST Blue Carbon model quantifies the marginal value of storage and sequestration services by comparing change in stock and accumulation of carbon between current and future scenarios.  In addition to comparisons between scenarios, the InVEST Blue Carbon model can be used to identify locations within the landscape where degradation of coastal ecosystems should be avoided in order to maintain carbon storage and sequestration services and values.  This is a "Tier 1" model.


Introduction
============

This model combines estimates of the social value of carbon with information about 1) the distribution and abundance of coastal vegetation, 2) habitat-specific carbon stock data and 3) accumulation rates to estimate carbon storage, sequestration and value across a landscape. To quantify the value of carbon storage and sequestration, the model focuses on changes in atmospheric carbon dioxide and other greenhouse gases as a result of changes caused by human activities that can affect marine ecosystems which store and sequester carbon.  Carbon-induced changes in the atmosphere have wide-ranging effects on natural systems and can thus result in changes in agricultural productivity, air quality, sea level, and more. The InVEST Blue Carbon model incorporates information about changes in the storage and sequestration capacity of the marine vegetation with economic factors into a single model which can estimate the value of incremental changes.


The model
=========
Modeling considerations
-----------------------
Mapping and modeling changes in carbon storage and sequestration for coastal and marine habitats can present challenges.  The types of spatial inputs and information about the carbon cycle often vary by site.  Some locations may have data readily available for detailed analysis while other locations may not have the information necessary to model changes in the position and function of coastal habitats.  Salt marsh, for example, is often studied in the context of migration from rising seas.  The combination of natural (e.g. rising seas) and anthropogenic (e.g. saltmarsh migration blocked by roads) factors should be included in scenario maps and subsequent carbon modeling when possible.  When exploring future land cover scenarios, land cover map outputs from the SLAMM model (Sea Level Affecting Marshes Model) developed by Warren Pinnacle can be useful inputs to the InVEST Blue Carbon model (Clougheet al. 2010).  However, because not all sites have the detailed elevation and habitat information required to run SLAMM, we have built a flexible approach that allows users to provide either detailed land use/land cover maps or qualitative risk maps of coastal and marine vegetation.

How it works
------------
The InVEST Blue Carbon model combines information about the distribution and abundance of coastal vegetation with habitat specific carbon stock data and accumulation rates to estimate carbon storage, sequestration and value across a landscape.  The model simplifies the carbon storage and sequestration process to account for storage in four main pools (aboveground biomass, belowground biomass, standing dead carbon and sediment carbon, see Figure 1).  Accumulation of carbon in coastal habitats occurs primarily in sediments.  The model requires users to provide maps of coastal ecosystems that store carbon, such as mangroves and seagrasses.  Users must also provide data on the amount of carbon stored in the four carbon pools and the rate of annual carbon accumulation in the sediments. If local information is not available, users can draw on the global database of values for carbon stocks and accumulation rates sourced from the peer-reviewed literature that is included in the model.  If data from field studies or other local sources are available, these values should be used instead of those in the global database.  The model uses vegetation maps from alternative scenarios, which represent changes in human use patterns in coastal areas or changes in sea level, to estimate the amount of carbon lost or gained over a specified period of time.  The model quantifies carbon storage across the landscape by summing the carbon stored in the biomass and sediment pools and multiplying by the area of habitat under any given human use scenario. 

[INSERT FIGURE]

Figure 1. Conceptual model of carbon sequestration and storage in marine ecosystems (Adapted from Bouillon et al. 2008)


A.  Carbon storage
^^^^^^^^^^^^^^^^^^
The carbon stored in a grid cell `x` at time `t`, given by `C_xt` and measured in tons of CO\ :sub:`2` equivalent, is equal to the sum of the carbon stored in each pool in the grid cell at any time (t),

.. math:: C_{xt} = {\sum^{J}_{j=1}}A_{xjt}*(C_{aj} + C_{bj} + (C_{sj} * d{j}) + C_{lj})

where (:math:`A_xjt`) is the area of vegetation `j` in grid cell `j` at time `j`, `d` is the depth of the sediment for habitat `j`, `C_{aj}`, `C_{bj}`, `(C_{sj}`, `C_{lj}` indicate the metric tons of CO\ :sub:`2` equivalent stored per hectare in the aboveground, belowground, soil and litter pools of habitat `j` respectively, where `j= 1, 2, ...J` indexes all the habitat types in a coastal area. If the user does not have sediment depth information, the model uses a default value of 1 meter depth, a widely used value for estimating carbon stocks. Vegetation type can simply indicate the dominant vegetation type (e.g., eelgrass, mangrove etc), or it can include details that affect pool storage values such as plant species, vegetation density, temperature regime, or vegetation age (e.g., time since restoration or last major disturbance).
 
For the sake of the carbon storage estimation, each vegetation type is assumed to be in storage equilibrium at any point in time (accumulation of carbon will be accounted for in the sequestration component of the model). 
 
If data is lacking, the model can be used with any subset of the four carbon pools. To determine the tonnes of CO\ :sub:`2` equivalent stored across the whole seascape at time t, we sum all grid cell carbon storage values.

.. math:: S_x(t_0) = H_x(t_0) + M_x(t_0)

.. math:: H_x(t_0) = A_{x}*d_{sx}*C_{sx}

.. math:: M_x(t_n) = A_{x}*(C_{ax} + C_{bx} + C_{lx})

where
 * :math:`S_x(t_0)` is the carbon storage at the initial time
 * :math:`H_x(t_0)` is the carbon storage in the soil at the initial time
 * :math:`M_x(t_n)` is the carbon storage in the biomass at anytime
 * :math:`t_n \in \{t_0, ..., t_N\}` with :math:`t_n < t_{n-1}`
 * :math:`t_0` is the initial time
 * :math:`A_{x}` is the area in cell :math:`x`
 * :math:`C_{ax}` is the above ground carbon pool in cell :math:`x`
 * :math:`C_{bx}` is the below ground carbon pool in cell :math:`x`
 * :math:`d_{sx}` is the depth of :math:`C_{sx}` in cell :math:`x`
 * :math:`C_{sx}` is the soil carbon pool in cell :math:`x`
 * :math:`C_{lx}` is the litter carbon pool in cell :math:`x`



B.  Carbon sequestration
^^^^^^^^^^^^^^^^^^^^^^^^
We model sequestration as the rate of carbon accumulation in the soil that remains in organic form after the first year of decomposition. In relation to the annual ecosystem budget, this pool has not been remineralized, so it represents net accumulation. This carbon is usually derived from belowground production, and residence time can range from decades to millennia (Romero et al. 1994, Mateo et al. 1997). This accumulation contributes to the development of carbon ‘reservoirs’ which are considered virtually permanent unless disturbed.
 
We estimate accumulation by multiplying habitat specific rates of carbon accumulation by the total area of habitat. The carbon sequestered in a grid cell `x` at time `t`, given by `\Delta C_{xt}` and measured in tons of CO\ :sub:`2` equivalent per year, is equal to the rate of carbon accumulation in the sediments at time `t`, where `A_{xjt}` is the area of vegetation `j` in grid cell `x` at time `t`.

.. math:: \Delta C_{xt} = {\sum^{J}_{j=1}}A_{xjt}(\Delta C_{xj})

Loss of carbon from the sediment or soil upon disturbance is more nuanced than sequestration because different types of human uses and/or stasis may cause varied disruption of the soils and the carbon stored below.  For example, clearing mangroves for a shrimp pond may result in a high impact, while fishing or oil development may have little impact.  The impact of coastal development on carbon storage varies since some types of development may involve paving over the soil and the sediment, which would still keep the storage in those pools intact.  Alternatively, dredging could remove seagrasses and disturb the sediments below, releasing carbon into the atmosphere.  See the next section for further treatment of this issue.

.. math:: \Delta S_x(t_n) = S_x(t_{n}) - S_x(t_{n-1})

where

 * :math:`\Delta S_x(t_n)` is the carbon sequestered between time :math:`t_{n-1}` and :math:`t_n` in cell :math:`x`


C.  Carbon loss and emissions after habitat disturbance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When coastal ecosystems are degraded by human activities, the carbon stored in the living plant material (above and belowground) and the soil may be emitted to the atmosphere. The magnitude of post-conversion CO\ :sub:`2` release depends on the type of habitat disturbed and the type of disturbance. The type of disturbance will determine the amount of aboveground biomass loss and depth to which the soil profile will be altered. The deeper the effects of the disturbance, the more soil carbon that will be exposed to oxygen, oxidized and consequently emitted in the form of CO\ :sub:`2`. Many types of disturbances will disturb only the top soil layers while the deeper layers remain inundated and their carbon intact, while other disturbances may affect several meters of the soil profile. To estimate the extent of impact of various disturbances, we classify disturbances into three categories of impact: high, medium and low. Examples of high impact disturbances include: mangrove conversion to shrimp farms of draining and diking salt marshes for conversion to agriculture. Examples of low impact disturbances include: recreational boating or float home marinas.

Magnitude of loss
"""""""""""""""""
We model the release of carbon from the biomass and soil pools in two steps. First, we estimate the carbon lost from biomass. The fraction of carbon lost from the biomass pools depends on the type of impact, level of disturbance and the type of habitat. Second, we estimate the carbon lost from the soil pool, which depends on the level of impact of disturbance and thus the depth of soil disturbance (see Table 1).

The carbon emitted post-disturbance,

. math:: E_x = {\sum^{J}_{j=1}}A_{xjt}(b(C_{aj} + C_{bj}) + (C_{sj} * d{j}) + C_{lj})

where `b` is the percentage of carbon biomass emitted and `d` is the depth of soil disturbance.

The model permits users to provide details on human uses and how they vary across scenarios and habitats.  In particular, it allows for polygons indicating where a particular stressor disturbs the carbon in the sediments of marine vegetation.  This information will allow the model to determine loss of soil carbon due to human use activities over time.


.. math:: L_x = A_{x}*(C_{ax} + C_{bx} +C_{lx}+p_{x}*d_{x}*C_{sx})

where

* :math:`L_x` is carbon that is disturbed by the transition and will be released in cell :math:`x`


Timing of loss
""""""""""""""
Carbon will be lost from the pools at different rates: most of the biomass carbon will be emitted within the first year, whereas the release of soil carbon may take much longer. We assign exponential decay functions and associated half-lives for biomass and soil carbon to each habitat type (Table 1; Murray et al. 2011).

.. math:: E_x = A_{x}[0.5^{(t_n-t_{n-1})/\alpha_{bx}} (C_{ax} + C_{bx} + C_{lx})+0.5^{(t_n-t_{n-1})/\alpha_{sx}}b_{sx} d_{sx} C_{sx}]

where

 * :math:`E_x` is the emission of carbon from time :math:`t_{n-1}` to :math:`t_n` in cell :math:`x`
 * :math:`\alpha_{bx}` is the half-life decay for biomass carbon in cell :math:`x`
 * :math:`\alpha_{sx}` is the half-life decay for soil carbon in cell :math:`x`

 
Table 1
"""""""
+--------------------------------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------+
| Rank                           | Salt marshes                                                                                       | Mangroves                                                                                                                                          | Seagrasses                                                                    | Other vegetation                     |
+================================+====================================================================================================+====================================================================================================================================================+===============================================================================+======================================+
| Emissions from biomass         | LI / MI: 50% biomass loss (1) HI: 100% biomass loss (1)                                            | LI / MI: 50% biomass loss (1) HI: 100% biomass loss (1)                                                                                            | LI / MI: 50% biomass loss (1) HI: 100% biomass loss (1)                       | Use literature / field data          |
+--------------------------------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------+
| Depth of soil carbon loss      | If no data on depth of disturbance, assume 1m depth (2) LI: top 30cm (1) MI: 1m depth HI: 1.5m (3) | If no data on depth of disturbance, assume 1m depth (2) LI: top 30cm (1) MI: top 50cm (?) HI: 100% loss from top 30cm, 35% loss from 30cm-1.5m (1) | LI / MI: ? HI: top 50cm washed away, second 50cm would decompose in place (2) | Use literature / field data          |
+--------------------------------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------+
| Rate of decay (over 25 years)  | Soil half-life: 7.5 yrs (2) Biomass half-life: 6 months (2)                                        | Soil half-life: 7.5 yrs (2) Biomass half-life:  15 yrs, but assume 75% is released immediately from burning (2)                                    | Soil half-life: 1 yr (2) Biomass half-life: 100 days (2)                      | Use literature / field data          |
+--------------------------------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------+
| Methane emissions              | 1.85 T CO\ :sub:`2`e/ha/yr (4)                                                                              | 0.4 t CO\ :sub:`2`/ha/yr                                                                                                                                    | negligible                                                                    | Use literature / field data          |
+--------------------------------+----------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------+

Table 1: Default emissions values as a result of low (LI), medium (MI) and high (HI) impact activities to salt marshes, mangroves and seagrasses
References:
(1) Donato, D. C., Kauffman, J. B., Murdiyarso, D., Kurnianto, S., Stidham, M., & Kanninen, M. (2011). Mangroves among the most carbon-rich forests in the tropics. Nature Geoscience, 4(5), 293–297. doi:10.1038/ngeo1123
(2) Murray, B., Pendleton, L., Jenkins, A., & Sifleet, S. (2011). Green Payments for Blue Carbon, 1–50.
(3) Crooks, S., D. Herr, J. Tamelander, D. Laffoley, and J. Vandever. 2011. “Mitigating Climate Change through Restoration and Management of Coastal Wetlands and Near-shore Marine Ecosystems: Challenges and Opportunities.” Environment Department Paper 121, World Bank, Washington, DC.
(4) Krithika, K., R. Purvaja, and R. Ramesh. 2008. Fluxes of methane and nitrous oxide from an Indian mangrove. Current Science 94(2): 218–224.

Transition Storage
""""""""""""""""""

Different land use / land cover maps (LULC) are the inputs that drive change in carbon from one time period to the next.  The user will need a land change model (e.g. SLAMM), a scenario assessment tool, or some other method for creating future maps of coastal and marine habitats.  The user will specify which LULC classes store carbon.   To assess change in carbon due to accumulation and loss, the user must provide land cover maps at various snapshots over the analysis time period (t1, t2,...tt).  By drawing from user-provided transition information, the model can identify when development and other stressors (dredging, sea-level rise, etc.) disturb carbon stored by coastal vegetation.  The model will count carbon stocks in the vegetation and sediments at each time period and then identify and adjust for accumulation and loss of carbon over time.

The model requires a pre-processing step in order to create a transition matrix for all the potential LULC conversions occuring during each time period.  For each pixel in the study area, the pre-processing tool will compare the LULC class present at t1 and then t2 in order to identify the entire domain of transitions.  If a transition from one LULC class to another does not occur during any of the time steps, the tool will populate the cell with "None".  For cells in the matrix where transitions occur, the tool will provide "+" or "-" as default based on general rules of thumb.  For example, if a salt marsh pixel in t1 is converted to development in t2 then the cell will contain a "-" (vegetation to development will most likely result in a loss of carbon).  On the other hand, if a mangrove remains a mangrove over this same time period then this cell will contain "+".  It is likely that a mangrove that remains a mangrove will accumulate carbon in its soils and biomass.  These assumptions of directionality by the tool can be edited by the user before running the blue carbon model.  

The pre-processor can also assist the user in providing more detail transitions result in varying degrees of accumulation or emissions.   For example, a user may only provide one development class in a LULC map.  However, certain development may disturb soil carbon more than others.  By separating out these two development types, the model will be able to more accurately quantify and map changes in carbon as a result of natural and anthropogenic factors.  Similarly, different species of mangroves may accumulate soil carbon at different rates.  If this information is known, it is important to provide this species distinction in the LULC maps and then the accumulation rate in the transition matrix.

.. math:: S_x(t_n) = H_x(t_n) + M_x(t_n)

.. math:: H_x(t_n) = A_{x}*d_{sx}*C_{sx} + R_x(t_{n-1})

.. math:: R_x(t_n) = (1-p_x)*H_x(t_n)

where
 * :math:`S_x(t_n)` is the carbon storage at anytime after :math:`t_0` in cell :math:`x`
 * :math:`H_x(t_n)` is the carbon storage in the soil at anytime after :math:`t_0` in cell :math:`x`
 * :math:`R_x(t_n)` is the residual carbon left in the soil after a transition in cell :math:`x`
 * :math:`t_n` is the current time :math:`> t_0`
 * :math:`A_{x}` is the area in cell :math:`x`
 * :math:`d_{sx}` is the depth of :math:`C_{s}` in cell :math:`x`
 * :math:`C_{sx}` is the soil carbon pool in cell :math:`x`
 * :math:`p_{x}` is the portion of soil carbon not disturbed by the transition in cell :math:`x`


.. 
	Valuation
	^^^^^^^^^
	
	[ROB, PLEASE ADD INTRO TEXT ON MARKET AND SOCIAL VALUATION]

	Private Market Discount Rate Valuation
	""""""""""""""""""""""""""""""""""""""

	.. math:: V_{x, initial} = \sum_{t=0}^{t_{final}-1} \frac{p_t \Delta C_{x,initial} R_x^t }{(1+d)^t}

	where 

	.. I feel like a lot of the awkwardness in the math in this document is due to keeping track of timing of LULC changes. I think this would be easy to address from a notation perspective.


	 * :math:`t_{final}` is the number of years between the current date and the end of the habitat change
	 * :math:`p_t` is the price of carbon at time :math:`t`
	 * :math:`C_{x,initial}` is the intial carbon stock on pixel x at time 0.
	 * :math:`R_x` is the rate at which the carbon stock decreases (or increases) per year
	 * and :math:`d` is the discount rate


	Social Market Price Schedule Valuation
	""""""""""""""""""""""""""""""""""""""

	.. math:: V_x = \sum_{t=0}^{t_{final}-1} \Delta C_{x} * s_t

	where

	 * :math:`t_{final}` is the number of years between the current date and the end of the habitat change
	 * :math:`\Delta C_{x}` is the carbon sequestration
	 * :math:`s_t` is the schedule price of carbon at time :math:`t`



Limitations and simplifications
===============================
 * We assume all storage and accumulation occurrs in the aboveground biomass and sediments.
 * We ignore increases in stock and accumulation with growth and aging of habitats.
 * We assume that carbon is stored and accumulated linearly through time between the current and future scenarios.
 * We assume that some human activities that may degrade coastal ecosystems do not disturb carbon in the sediments.
 * While the social cost of carbon estimates represent the state of the art in linking climatic factors to the global economy they are subject to an array of limitations and simplifications.

Validation
""""""""""
In the absence of detailed knowledge on the carbon dynamics in coastal and marine systems, we take the simplest accounting approach and draw on published carbon stock datasets from neighboring coastlines.  We use carbon estimates from the most extensive and up-to-date published global datasets of carbon storage and accumulation rates (e.g. Fourqurean et al. 2012 & Silfeet et al. 2012).


Data Needs
==========

Biophysical Inputs
""""""""""""""""""

The following are the data needs for the Blue Carbon model.  The model is distributed with default arguments which are defaulted in the following parameters on the tool's first run.

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory.

 * **Maps of the distribution and risk level of nearshore marine vegetation**: for current (t1) and future (t2) (i.e. mangroves, salt marshes, seagrasses).  These maps can be either land use/land cover (LULC) or vector format.

 * **CSV or DBF file**: containing information on carbon storage in biomass (tons of CO\ :sub:`2`e/ha), sediments (tons of CO\ :sub:`2`e/ha), rate of accumulation (tons of CO\ :sub:`2`e/ha/yr) and depth (in meters) of sediments for each type of marine vegetation.  

 * **Year of current land cover map**: (t1)
 
 * **Year of future land cover map**: Model requires inputs #3 and #4 in order to determine length of time (number of years; t2 - t1) of the analysis and multiplies this value by the user-specified accumulation rates indicated by input #6.  If the user is interested in only standing stock of carbon at t1, then only inputs #1 and #2 are required.  Valuation, however, is not possible without estimates for t2 (future scenario).
 
 * **Polygons indicating the location of human uses/stressors**: (e.g. coastal development, aquaculture, etc.).  Similar to the harvest maps in the InVEST terrestrial carbon model, this model will intersect these polygons with the land cover/ habitat maps.  This information on different stressors/human activities will inform the model as to how much these activities disturb the soil which influences the loss of carbon and rate of accumulation in the sediments
 
 * **Transition matrix**: showing the accumulation and loss of carbon in the sediments based on transitions in land use/land cover (LULC) from t1 to t2.

 .. image:: blue_carbon_images/interface_biophysical.png
    :width: 450px

Economic Inputs
"""""""""""""""
Data on the market or social value of sequestered carbon and its annual rate of change and a discount rate can be used in an optional model that estimates the value of this ecosystem service to society.  This should be virtually identical to the inputs required for the terrestrial carbon economic model.

The valuation model estimates the economic value of sequestration (not storage) as a function of the amount of carbon sequestered, the monetary value of each unit of carbon, a monetary discount rate, and the change in the value of carbon sequestration over time.. Thus, valuation can only be done in the carbon model if you have a future scenario. Valuation is applied to sequestration, not storage, because current market prices relate only to carbon sequestration. Discount rates are multipliers that typically reduce the value of carbon sequestration over time. The first type of discounting, the standard economic procedure of financial discounting, reflects the fact that people typically value immediate benefits more than future benefits due to impatience and uncertain economic growth. The second discount rate adjusts the social value of carbon sequestration over time. This value will change as the impact of carbon emissions on expected climate change-related damages changes. If we expect carbon sequestered today to have a greater impact on climate change mitigation than carbon sequestered in the future this second discount rate should be positive. On the other hand, if we expect carbon sequestered today to have less of an impact on climate change mitigation than carbon sequestered in the future this second discount rate should be negative.  

The value of carbon sequestration over time is given by:
 * **value of a sequestered ton of carbon**: (V in the equation below), in dollars per metric ton of elemental carbon (not CO\ :sub:`2`, which is heavier, so be careful to get units right! If the social value of CO\ :sub:`2`e is $Y per metric ton, then the social value of C is $(3.67*Y) per metric ton (Labeled “Price of carbon per metric ton (optional)” in the tool interface.) For applications interested in estimating the total value of carbon sequestration, we recommend value estimates based of damage costs associated with the release of an additional ton of carbon (the social cost of carbon (SCC).

 * **market discount rate**: (r in the equation above), which reflects society’s preference for immediate benefits over future benefits (labeled “Market discount rate (%) (optional)” in the tool interface). The default value in the interface is 7% per year, which is one of the market discount rates recommended by the U.S. government for cost-benefit evaluation of environmental projects. However, this rate will depend on the country and landscape being evaluated. Philosophical arguments have been made for using a lower discount rate when modeling climate change related dynamics, which users may consider using. If the rate is set equal to 0% then monetary values are not discounted.

 * **annual rate of change in the price of carbon**: (c in the equation below), which adjusts the value of sequestered carbon as the impact of emissions on expected climate change-related damages changes over time. The default value in the interface is 0% (labeled “The annual rate of change in the price of carbon (%) (optional)” in the tool interface). However, setting this rate greater than 0% suggests that the societal value of carbon sequestered in the future is less than the value of carbon sequestered now.

 .. image:: blue_carbon_images/interface_economic.png
    :width: 450px


Running the Model
=================

To run the marine blue carbon model double click *invest_blue_carbon.exe* located in the folder entitled *invest-3* in the InVEST installation directory.  The main interface indicates the required and optional input arguments as described in the **Data Needs** section above.  Click the *Run* button to start the model.  A successful run will be indicated in the window and a file explorer will open containing the results.

If you encounter any errors please email the output log to richsharp@stanford.edu.


Data Needs
==========

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory. To run multiple scenarios, create a new workspace for each scenario.
 
 * **LULC Time 1**: The land use land cover ratser for time 1.
 
 * **Year**: The year of ``LULC Time 1``
 
 * **LULC Time 2**: The land use land cover raster for time 2.
 
 * **Year**: The year of ``LULC Time 2``
 
 * **Carbon pools:** A table of LULC classes, containing data on carbon in metric tons per hectacre \( t ha\ :sup:`-1`\) stored in each of the four fundamental pools for each LULC class. Carbon storage data can be collected from field estimates from local plot studies, extracted from meta-analyses on specific habitat types or regions, or found in general published tables (e.g., IPCC, see Appendix). If information on some carbon pools is not available, pools can be estimated from other pools, or omitted by leaving all values for the pool equal to 0.

 Additionally, there must be columns for soil depth, 
 * **Transition matrix**: The transition matrix contains transition coefficients for the rate change in carbon from time 1 to time 2.
 
 * **Private market valuation** ``(optional -- required for private market valuation)``: 

 * **Price in term of metric tons of** ``(optional -- required for private market valuation)``: This is whether the price per metric ton is in terms of elemental carbon or CO\ :sub:`2` which is heavier.
 
 * **Value of Carbon** ``(optional -- required for private market valuation)``: The private market value for the carbon in United States dollars.
 
 * **Market discount in price of Carbon** ``(optional -- required for private market valuation)``: society's preference for immediate benefits over future benefits (labeled "Market discount rate (%) (optional)" in the tool interface). The default value in the interface is 7% per year, which is one of the market discount rates recommended by the U.S. government for cost-benefit evaluation of environmental projects. However, this rate will depend on the country and landscape being evaluated. Philosophical arguments have been made for using a lower discount rate when modeling climate change related dynamics, which users may consider using. If the rate is set equal to 0% then monetary values are not discounted.
 
 * **Annual rate of change in price of Carbon** ``(optional -- required for private market valuation)``: adjusts the value of sequestered carbon as the impact of emissions on expected climate change-related damages changes over time. The default value in the interface is 0% (labeled "The annual rate of change in the price of carbon (%) (optional)" in the tool interface). However, setting this rate greater than 0% suggests that the societal value of carbon sequestered in the future is less than the value of carbon sequestered now. It has been widely argued that GHG emissions need to be curtailed immediately to avoid crossing a GHG atmospheric concentration threshold that would lead to a 3 degree Celsius or greater change in global average temperature by 2105. Some argue that such a temperature change would lead to major disruptions in economies across the world (Stern et al. 2006). Therefore, any mitigation in GHG emissions that occurs many years from now may have no effect on whether or not this crucial concentration threshold is passed. If this is the case, C sequestration in the far future would be relatively worthless and a carbon discount rate greater than zero is warranted. Alternatively, setting the annual rate of change less than 0% (e.g., -2%) suggests that the societal value of carbon sequestered in the future is greater than the value of carbon sequestered now (this is a separate issue than the value of money in the future, a dynamic accounted for with the market discount rate). This may be the case if the damages associated with climate change in the future accelerate as the concentration of GHGs in the atmosphere increases.
 
 * **Social market valuation** ``(optional -- required for social market valuation)``:

 * **SCC Table** ``(optional -- required for social market valuation)``: value estimates based on damage costs associated with the release of an additional ton of carbon, the social cost of carbon (SCC). The default data comes from *Rob...*
 
 * **SCC field** ``(optional -- required for social market valuation)``: The field in the ``SCC Table`` that contains the value for the carbon. The default data includes rates for 5%, 3%, and 2%.

 
Interpreting Results
====================

Model Ouputs
------------

Output folder
^^^^^^^^^^^^^

 * ``carbon1_above.tif``: The output raster indicating the carbon from above ground in metric tons.
 * ``carbon1_below.tif``: The output raster indicating the carbon from below ground in metric tons.
 * ``carbon1_litter.tif``: The output raster indicating the carbon from litter in metric tons.
 * ``carbon1_soil.tif``: The output raster indicating the carbon from soil in metric tons.
 * ``carbon1_total.tif``: The output raster indicating the total carbon from all sources in metric tons.
 * ``carbon2_above.tif``: The output raster indicating the carbon from above ground in metric tons.
 * ``carbon2_below.tif``: The output raster indicating the carbon from below ground in metric tons.
 * ``carbon2_litter.tif``: The output raster indicating the carbon from litter in metric tons.
 * ``carbon2_soil.tif``: The output raster indicating the carbon from soil in metric tons.
 * ``carbon2_total.tif``: The output raster indicating the total carbon from all sources in metric tons.
 * ``depth.tif``: The output raster indicating the depth of soil in meters.
 * ``magnitude.tif``: The output raster indicating the emission of carbon in metric tons.
 * ``private_valuation.tif``: The output raster indicating the value in United States dollars.
 * ``sequestration.tif``: The output raster indicating the net carbon storage in metric tons.
 * ``social_valuation.tif``: The output raster indicating the value United States dollars.
 * ``timing.tif``: The output raster indicating the metric tons of carbon emitted over the course of the transition.
 * ``transition.tif``: The output raster indicating the transition coefficent betweeen LULC from time 1 to time 2.


Case example illustrating model inputs and results
==================================================

Freeport, Texas
"""""""""""""""

Over the next 100 years, the US Gulf coast has been identified as susceptible to rising sea levels.  The use of the InVEST Blue Carbon model serves to identify potential changes in the standing stock of carbon in coastal vegetation that sequester carbon.  This approach in Freeport, TX was made possible with rich elevation (DEM) and land use / land cover (LULC) data sets.  We used a 10-meter DEM with floating point accuracy to parameterize Warren Pinnacle’s SLAMM (Sea Level Affected Marsh Model).  This allowed us to model coastal land cover change over a 94 year period, including marsh migration and loss over time.
 
SLAMM results produced LULC maps of future alternative scenarios over 25-year time slices beginning in 2006 and ending in 2100.  The following figure depicts 2006 LULC and a table of disaggregated land class types.

 .. image:: blue_carbon_images/freeportcase_fig_1.png
    :width: 450px

Figure 1. Current (2006) LULC map for Freeport, Texas

Carbon stored in the sediment (‘soil’ pool) was the focus of the biophysical analysis since the vast majority of carbon is sequestered in this pool by coastal and marine vegetation.  To produce maps of carbon storage at the different 25-year time slices, we performed a simple look-up to determine the amount of carbon per 10-by-10 meter pixel based on known storage rates from sampling in the Freeport area (Chmura et al.).
 
Next, we provided the model with a transition matrix in order to identify the amount of carbon gained or lost over each 25-year period of time.  Annual accumulation rates in salt marsh were obtained from Chmura et al. 2003.  The following is the transition matrix used in this analysis.

[GV TO INSERT FINAL TRANSITION MATRIX]

When analyzing the time period from 2025 to 2050, we assume t1 = 2025 and t2 = 2050.  We identify all the possible transitions that will result in either accumulation or loss of carbon.  The model compares the two LULC maps (t1 and t2) to identify which pixels transitioned.  We apply these transformations to the standing stock of carbon which is the running carbon tally at t1 (2025).  Once these adjustments are complete, we have a new map of standing carbon for t2 (2050).  We repeat this step for the next time period where t1 = 2050 and t2 = 2075.  This process was repeated until 2100.  We produce spatially explicit maps of net sequestration over time as well as total carbon summaries for the two scenarios at each 25-year period.  This information was used to determine at what time period during each scenario the marsh migration was resulting in emissions for the study site as well as over the entire area.


+------------------+----------------------------+-------------------------+
| Time Period      | Scenario #1: No Management | Scenario #2: High Green |
+==================+============================+=========================+
|  2006-2025       | +4,031,180                 | +4,172,370              |
+------------------+----------------------------+-------------------------+
|  2025-2050       | -1,170,580                 | +684,276                |
+------------------+----------------------------+-------------------------+
|  2050-2075       | -7,403,690                 | -5,525,100              |
+------------------+----------------------------+-------------------------+
|  2075-2100       | -7,609,020                 | -8,663,600              |
+------------------+----------------------------+-------------------------+
|  100-Year Total: | -12,152,100                | -9,332,050              |
+------------------+----------------------------+-------------------------+


 .. image:: blue_carbon_images/freeportcase_fig_2.png
    :width: 450px
    :align: center

Figure 2. Carbon emissions (red) and sequestration (blue) from 2006 to 2100 for the two scenarios.

+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input                               | Source                                    | How the data were used in the model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+=====================================+===========================================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| DEM                                 | USGS                                      | DEM was needed to produce the future LULC maps using the SLAMM tool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Land use / land cover (LULC)        | USGS/NOAA                                 | Salt marshes store carbon in biomass and soils.  We utilized maps showing the current distribution of salt marshes to establish a baseline coverage of marshes from which we estimate aboveground biomass and soil carbon.                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Carbon stock in salt marsh systems  | Natural Capital Project literature review | Carbon storage was calculated by summing the carbon stored in biomass and sediments.  Carbon stocks were calculated for all of the areas of functional salt marsh in the study region (Chmura et al. 2003).                                                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Social value of carbon in 2006 US $ | USIWG 2010                                | The “social cost of carbon” (SCC) is an estimate of the monetized damages associated with an incremental increase in carbon emissions in a given year.  It is intended to include (but is not limited to) changes in net agricultural productivity, human health, property damages from increased flood risk, and the value of ecosystem services.  The social cost of carbon is useful for allowing institutions to incorporate the social benefits of reducing carbon dioxide (CO\ :sub:`2`) emissions into cost benefit analyses of management actions that have small, or “marginal,” impacts on cumulative global emissions. |
+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Discount rate                       | USIWG 2010                                | Since carbon dioxide emissions are long-lived, subsequent damages occur over many years.  We use the discount rate to adjust the stream of future damages to its present value in the year when the emissions were changed (e.g., the climate adaptation scenarios were implemented).  This discount rate reflects society’s preferences for short run versus long term consumption                                                                                                                                                                                                                                      |
+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Table 1. Summary of data inputs, source and how these data were used in the InVEST Blue Carbon model


Limitations
"""""""""""
 * This analysis did not account for aboveground biomass stored in coastal and marine vegetation.
 
 * While the LULC maps were quite detailed (10 meters), we only had temporal resolution of 25 year to model carbon sequestration and emissions.  The carbon cycle is a dynamic process.  By only analyzing change over 26-year time slices, we are losing detail within this time frame.

 
References
==========

Bouillon et al. 2008

Chmura, G. L., S. C. Anisfeld, et al. (2003). "Global carbon sequestration in tidal, saline wetland soils." Global Biogeochemical Cycles 17(4): 1-12. 

Clough, J. S., Park, R., and Fuller, R. (2010). “SLAMM 6 beta Technical Documentation.” Available
at http://warrenpinnacle.com/prof/SLAMM. 

Fourqurean et al. 2012

Sifleet, Pendleton, & Murray. (2011). State of the Science on Coastal Blue Carbon. Nicolas Institute Report, 1–43.

Silfeet et al. 2012

United States, Interagency Working Group on Social Costs of Carbon. 2010. Technical Support Document: Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866.

[Add link to IDB report]