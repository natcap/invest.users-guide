.. _blue-carbon:

***********
Blue Carbon
***********

Summary
=======
 
Marine and terrestrial ecosystems help regulate Earth's climate by adding and removing greenhouse gases (GHGs) such as carbon dioxide (CO\ :sub:`2`) from the atmosphere.  Coastal marine plants, mangroves and seagrasses in particular, store large amounts of carbon in their sediments, leaves and other biomass. By storing carbon, marine ecosystems keep CO\ :sub:`2` out of the atmosphere, where it would otherwise contribute to climate change.  In addition to storing carbon, marine ecosystems continually accumulate carbon in their sediments, creating large reservoirs of long-term sequestered carbon. Management activities that change the cover of coastal vegetation, such as seagrass restoration or mangrove clearing, can change carbon storage and the potential for carbon sequestration in coastal and marine areas.  With estimates of the social value, or where available, market value of carbon, the InVEST blue carbon model quantifies the marginal value of storage and sequestration services by comparing change in stock and accumulation of carbon between current and future scenarios.  In addition to comparisons between scenarios, the InVEST blue carbon model can be used to identify locations within the landscape where degradation of coastal ecosystems should be avoided in order to maintain carbon storage and sequestration services and values.  This is a "Tier 1" model.


Introduction
============

This model combines estimates of the social value of carbon with information about 1) the distribution and abundance of coastal vegetation, 2) habitat-specific carbon stock data, 3) disturbance of biomass and soil carbon, and 4) accumulation rates to estimate carbon storage, sequestration and value across a land or seascape. To quantify the value of carbon storage and sequestration, the model focuses on changes in atmospheric carbon dioxide and other greenhouse gases as a result of changes caused by human activities that can affect marine ecosystems which store and sequester carbon.  Carbon-induced changes in the atmosphere have wide-ranging effects on natural systems and can thus result in changes in agricultural productivity, air quality, sea levels, and more. The InVEST blue carbon model incorporates information about changes in the storage and sequestration capacity of the marine vegetation with economic factors into a single model which can estimate the value of incremental changes.


The model
=========
Modeling considerations
-----------------------
Mapping and modeling changes in carbon storage and sequestration for coastal and marine habitats can present challenges.  The types of spatial inputs and available information about the carbon cycle vary by location.  Some study areas may have high quality data available for a detailed analysis while other locations may not have the information necessary to model changes in the position and function of coastal vegetation.  Salt marsh, for example, is often studied in the context of migration from rising seas.  The combination of natural (e.g. rising seas) and anthropogenic (e.g. saltmarsh migration blocked by roads) factors should be included in scenario maps and subsequent carbon modeling when possible.  When exploring future land cover scenarios, land cover map outputs produced by the SLAMM model (Sea Level Affecting Marshes Model, developed by Warren Pinnacle) can be useful inputs to the InVEST blue carbon model (Clougheet et al. 2010).  However, because not all sites have the detailed elevation and habitat information required to run SLAMM, we have built a flexible approach that allows users to provide either detailed land use/land cover maps or maps indicating the presence of coastal and marine vegetation that can sequester carbon.


How it works
------------
The InVEST blue carbon model combines information about the distribution and abundance of coastal vegetation with habitat specific carbon stock data and accumulation rates to estimate carbon storage, sequestration and value across a landscape.  The model simplifies the carbon storage and sequestration process to account for storage in four main pools (aboveground biomass, belowground biomass, standing dead carbon and sediment carbon, see Figure 1).  Accumulation of carbon in coastal habitats occurs primarily in sediments (Pendleton et al., 2012).  The model requires users to provide maps of coastal ecosystems that store carbon, such as mangroves and seagrasses.  Users must also provide data on the amount of carbon stored in the four carbon pools and the rate of annual carbon accumulation in the sediments. If local information is not available, users can draw on the global database of values for carbon stocks and accumulation rates sourced from the peer-reviewed literature that is included in the model.  If data from field studies or other local sources are available, these values should be used instead of those in the global database.  The model requires land cover maps, which represent changes in human use patterns in coastal areas or changes to sea level, to estimate the amount of carbon lost or gained over a specified period of time.  The model quantifies carbon storage across the land or seascape by summing the carbon stored in these four carbon pools. 

.. figure:: ./blue_carbon_images/pools.png

Figure 1. Four carbon pools for marine ecosystems included in the InVEST blue carbon model (mangrove example).  


.. figure:: ./blue_carbon_images/conceptual_diagram.png

Figure 2.  Conceptual diagram of the InVEST blue carbon model

A.  Carbon storage
^^^^^^^^^^^^^^^^^^
The carbon stored in a grid cell :math:`x` at time :math:`t`, given by :math:`C_xt` and measured in tons of CO\ :sub:`2` equivalent, is equal to the sum of the carbon stored in each pool in the grid cell at any time (:math:`t`),

.. math:: C_{xt} = {\sum^{J}_{j=1}}A_{xjt}(C_{aj} + C_{bj} + (C_{sj} * d{j}) + C_{lj})

where :math:`A_{xjt}` is the area of vegetation :math:`j` in grid cell :math:`x` at time :math:`t`. :math:`j= 1, 2, ...J` indexes all the habitat types in a coastal area. :math:`d` is the depth of the sediment for habitat :math:`j`. :math:`C_{aj}`, :math:`C_{bj}`, :math:`C_{sj}`, :math:`C_{lj}` indicate the metric tons of CO\ :sub:`2` equivalent stored per hectare in the aboveground, belowground, soil and litter pools of habitat :math:`j` respectively. If the user does not have sediment depth information, the model uses a default value of 1 meter depth, a widely used value for estimating carbon stocks. Vegetation type can simply indicate the dominant vegetation type (e.g., eelgrass, mangrove etc), or it can include details that affect pool storage values such as plant species, vegetation density, temperature regime, or vegetation age (e.g., time since restoration or last major disturbance).
 
For the sake of the carbon storage estimation, each vegetation type is assumed to be in storage equilibrium at any point in time (accumulation of carbon will be accounted for in the sequestration component of the model). 
 
If data is lacking, the model can be used with any subset of the four carbon pools. To determine the tonnes of CO\ :sub:`2` equivalent stored across the entire study area at time t, we sum all grid cell carbon storage values.

.. math:: S_{xt} = H_{xt} + M_{xt}

.. math:: H_{xt} = A_{x}*ds_{x}*Cs_{x}

.. math:: M_{xt} = A_{x}*(Ca_{x} + Cb_{x} + Cl_{x})

where
 * :math:`S_{xt}` is total carbon storage
 * :math:`H_{xt}` is the carbon storage in the soil
 * :math:`M_{xt}` is the carbon storage in the biomass
 * :math:`A_{x}` is the area in cell :math:`x`
 * :math:`Ca_{x}` is the above ground carbon pool in cell :math:`x`
 * :math:`Cb_{x}` is the below ground carbon pool in cell :math:`x`
 * :math:`ds_{x}` is the depth of :math:`Cs_{x}` in cell :math:`x`
 * :math:`Cs_{x}` is the soil carbon pool in cell :math:`x`
 * :math:`Cl_{x}` is the litter carbon pool in cell :math:`x`

B.  Carbon accumulation
^^^^^^^^^^^^^^^^^^^^^^^^

We model accumulation as the rate of carbon retained in the soil in organic form after the first year of decomposition. In relation to the annual ecosystem budget, this pool has not been remineralized, so it represents net accumulation. This carbon is usually derived from belowground production, and residence time can range from decades to millennia (Romero et al. 1994, Mateo et al. 1997). This accumulation contributes to the development of carbon "reservoirs" which are considered virtually permanent unless disturbed. Thus, even in the absence of a land-use or land-cover change, carbon continues to be sequestered naturally. 

We estimate accumulation by multiplying habitat specific rates of carbon accumulation by the total area of vegetation. The carbon accumulated in a grid cell :math:`x` at time :math:`t`, given by :math:`ACC_{xt}` and measured in tons of CO\ :sub:`2` equivalent per year, is equal to the rate of carbon accumulation in the sediments at time :math:`t`, where :math:`A_{xjt}` is the area of vegetation :math:`j` in grid cell :math:`x` at time :math:`t`. 

.. math:: ACC_{xt} = {\sum^{J}_{j=1}}A_{xjt}(ACC_{xjt})

Loss of carbon from the soil pool (sediments) upon disturbance is more nuanced than sequestration because different types of human uses and/or stasis may cause varied disruption of the soils and the carbon stored below.  For example, high impact activities such as clearing mangroves for a shrimp pond or sediment dredging may result in a larger soil carbon disturbance, than commercial fishing or oil exploration.  The impacts from coastal development on carbon storage varies since some types of development may involve paving over the soil, which often keeps a large percentage of the carbon stored intact.  Alternatively, dredging could remove seagrasses and disturb the sediments below, releasing carbon into the atmosphere.


C.  Carbon loss and emissions after habitat disturbance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When coastal ecosystems are degraded by human activities, the carbon stored in the living plant material (above and belowground) and the soil may be emitted to the atmosphere. The magnitude of post-conversion CO\ :sub:`2` release depends on the type of vegetation disturbed and the level of disturbance. The type of disturbance will determine the amount of aboveground biomass loss and depth to which the soil profile will be altered. The deeper the effects of the disturbance, the more soil carbon that will be exposed to oxygen, oxidized and consequently emitted in the form of CO\ :sub:`2`. Some disturbances will only disturb the top soil layers while the deeper layers remain inundated and their carbon intact.  Other disturbances may affect several meters of the soil profile. To estimate the extent of impact of various disturbances, we classify disturbances into three categories of impact: high, medium and low.  Examples of high impact disturbances include mangrove conversion to shrimp farms and draining or diking salt marshes for conversion to agriculture.  Low impact disturbance examples include recreational boating or float home marinas.

Magnitude of loss
"""""""""""""""""
We model the release of carbon from the biomass and soil pools in two steps. First, we estimate the carbon lost from biomass. The fraction of carbon lost from the biomass pools depends on the type of impact, level of disturbance and the type of vegetation. Second, we estimate the carbon lost from the soil pool, which depends on the level of impact of disturbance and thus the depth of soil disturbed (see Table 1).

The carbon emitted post-disturbance,

.. math:: E_x = {\sum^{J}_{j=1}}A_{xjt}(b(Ca_{j} + Cb_{j}) + (Cs_{j} * d{j}) + Cl_{j})

where :math:`b` is the percentage of carbon biomass emitted and :math:`d` is the depth of soil disturbance.

The InVEST blue carbon model allows users to provide details on factors that can result in loss of soil or biomass carbon over time.  This information can be provided to the model through a pre-processor tool (See "Transition Storage" section) and further clarified with an input transition table.  This information allows the model to determine the percent loss of soil carbon in the study area over time.

.. math:: L_x = A_{x}*(Ca_{x} + Cb_{x} +Cl_{x}+p_{x}*d_{x}*Cs_{x})

where

* :math:`L_x` is carbon that is disturbed by the transition and will be released in cell :math:`x`
* :math:`d_{x}` is the depth of the carbon soil pool

Timing of loss
""""""""""""""
Carbon will be lost from the pools at different rates: most of the biomass carbon will be emitted within the first year, whereas the release of soil carbon may take much longer. We assign exponential decay functions and associated half-lives for biomass and soil carbon to each habitat type (Table 1; Murray et al. 2011).

.. math:: E_x = A_{x}[1 - 0.5^{(t_n-t_{n-1})/\alpha_{bx}} (C_{ax} + C_{bx} + C_{lx})+0.5^{(t_n-t_{n-1})/\alpha_{sx}}b_{sx} d_{sx} C_{sx}]

where

 * :math:`E_x` is the emission of carbon from time :math:`t_{n-1}` to :math:`t_n` in cell :math:`x`
 * :math:`\alpha_{bx}` is the half-life decay for biomass carbon in cell :math:`x`
 * :math:`\alpha_{sx}` is the half-life decay for soil carbon in cell :math:`x`

 
+------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+
| Rank                               | Salt marshes                                                                                       | Mangroves                                                                                                         | Seagrasses                                                                                                                             | Other vegetation                     |
+====================================+====================================================================================================+===================================================================================================================+========================================================================================================================================+======================================+
| **% carbon loss from biomass**     | | LI / MI: 50% biomass loss (1)                                                                    | | LI / MI: 50% biomass loss (1)                                                                                   | | LI / MI: 50% biomass loss (1)                                                                                                        | Use literature / field data          |
|                                    | | HI: 100% biomass loss (1)                                                                        | | HI: 100% biomass loss (1)                                                                                       | | HI: 100% biomass loss (1)                                                                                                            |                                      |
+------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+
| **% carbon loss from soil^**       | | LI: 30% loss (1)                                                                                 | | LI: 30% loss (1)                                                                                                | | LI / MI: top 10% washes away, bottom 90% decomposes in place (2)                                                                     | Use literature / field data          |
|                                    | | MI / HI: 100% loss (3)                                                                           | | MI: 50% loss (1)                                                                                                | | HI: top 50% washes away, bottom 50% decomposes in place (2)                                                                          |                                      |
|                                    |                                                                                                    | | HI: 66% loss (up to 1.5 m depth) (1)                                                                            |                                                                                                                                        |                                      |
+------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+
| **Rate of decay (over 25 years)**  | | Biomass half-life: 6 months (2)                                                                  | | Biomass half-life: 15 years, but assume 75% is released immediately from burning (2)                            | | Biomass half-life: 100 days (2)                                                                                                      | Use literature / field data          |
|                                    | | Soil half-life: 7.5 yrs (2)                                                                      | | Soil half-life: 7.5 years (2)                                                                                   | | Soil half-life: 1 year (2)                                                                                                           |                                      |
+------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+
| **Methane emissions**              | 1.85 T  CO\ :sub:`2` e/ha/yr (4)                                                                   | 0.4 T CO\ :sub:`2`/ha/yr                                                                                          | Negligible                                                                                                                             | Use literature / field data          |
+------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+

Table 1: Percent carbon loss and vegetation-specific decay rates as a result of low (LI), medium (MI) and high (HI) impact activities disturbing salt marsh, mangrove and seagrass ecosystems.  These default values can be adjusted by modifying the input CSV tables.

^ = Model assumes 1 meter soil depth

References (numbers in parentheses above):

1. Donato, D. C., Kauffman, J. B., Murdiyarso, D., Kurnianto, S., Stidham, M., & Kanninen, M. (2011). Mangroves among the most carbon-rich forests in the tropics. Nature Geoscience, 4(5), 293-297.
2. Murray, B. C., Pendleton, L., Jenkins, W. A., & Sifleet, S. (2011). Green payments for blue carbon: Economic incentives for protecting threatened coastal habitats. Nicholas Institute for Environmental Policy Solutions, Report NI, 11, 04.
3. Crooks, S., Herr, D., Tamelander, J., Laffoley, D., & Vandever, J. (2011). Mitigating climate change through restoration and management of coastal wetlands and near-shore marine ecosystems: challenges and opportunities. Environment Department Paper, 121, 2011-009.
4. Krithika, K., Purvaja, R., & Ramesh, R. (2008). Fluxes of methane and nitrous oxide from an Indian mangrove. Current Science (00113891), 94(2).


Transition storage (Preprocessor tool)
"""""""""""""""""""""""""""""""""""""""

Multiple land use / land cover maps (LULC) at different time periods are the inputs that drive change in carbon over time.  The user will need a land change model (e.g., SLAMM), a scenario assessment tool, or manual GIS processing to produce raster maps of coastal and marine vegetation.  The user will specify which LULC classes store carbon.   To assess change in carbon due to accumulation and loss, the user must provide LULC maps at various years over the analysis period (:math:`t_{0}`, :math:`t_{1}`, ..., :math:`t_{t}`). The model will count carbon stocks in the four pools at each time period and then adjust for accumulation and loss of carbon over time.

The model requires the use of a pre-processing tool in order to create a transition matrix that indicates either accumulation or disturbances as a result of different LULC transitions (e.g. salt marsh to developed dry land).  For each pixel in the study area, the pre-processing tool will compare the LULC class present at :math:`t_{0}` and then :math:`t_{1}` in order to identify the entire domain of transitions.   This transition matrix produced by the blue carbon pre-processor and then edited by the user will allow the model to identify where human activities and natural events disturb carbon stored by vegetation.   If a transition from one LULC class to another does not occur during any of the time steps, the tool will populate the cell with "None".  For cells in the matrix where transitions occur, the tool will populate "Accumulation" or "Distrubance" in each cell of the table.  For example, if a salt marsh pixel in :math:`t_{0}` is converted to developed dry land in :math:`t_{1}` then the cell will contain the text "Disturbance".  On the other hand, if a mangrove remains a mangrove over this same time period then this cell in the matrix will contain the text "Accumulation".  It is likely that a mangrove that remains a mangrove will accumulate carbon in its soils and biomass.  These rules of thumb built into the tool can always be overidden by the user before running the core blue carbon model

The pre-processor can also assist the user in providing more detailed transitions that result in varying degrees of accumulation or emissions.   For example, a user may only provide one development class in a LULC map.  However, some development may disturb soil carbon more than others.  By separating out these two development types, the model will be able to more accurately quantify and map changes in carbon as a result of natural and anthropogenic factors.  Similarly, different species of mangroves may accumulate soil carbon at different rates.  If this information is known, it is important to provide this species distinction (two different classes in the LULC input maps) and then the associated accumulation rates in the carbon CSV input table.

.. math:: S_{xt} = H_{xt} + M_{xt}

.. math:: H_{xt} = A_{x}*d_{sx}*C_{sx} + R_{xt}

.. math:: R_{xt} = (1-p_x)*H_{xt}

where
 * :math:`S_{xt}` is the carbon storage at time :math:`t` in cell :math:`x`
 * :math:`H_{xt}` is the carbon storage at the soil in time :math:`t` in cell :math:`x`
 * :math:`R_{xt}` is the residual carbon left in the soil after a transition in cell :math:`x`
 * :math:`A_{x}` is the area in cell :math:`x`
 * :math:`ds_{x}` is the depth of :math:`C_{s}` in cell :math:`x`
 * :math:`Cs_{x}` is the soil carbon pool in cell :math:`x`
 * :math:`p_{x}` is the portion of soil carbon not disturbed by the transition in cell :math:`x`


D.  Valuation
^^^^^^^^^^^^^

The valuation option for the blue carbon model estimates the economic value of sequestration (not storage) as a function of the amount of carbon sequestered, the monetary value of each unit of carbon, a discount rate, and the change in the value of carbon sequestration over time. The value of sequestered carbon is dependent on who is making the decision to change carbon emissions, and falls into two categories: social and private. If changes in carbon emissions are due to public policy, such as zoning coastal areas for development, then decision-makers should weigh the benefits of development against the social losses from carbon emissions. Because local carbon emissions affect the atmosphere at a global scale, the social cost of carbon (SCC) is commonly calculated at a global scale (USIWGSCC, 2010). Efforts to calculate the social cost of carbon have relied on multiple integrated assessment models such as FUND (http://www.fund-model.org/), PAGE (Hope, 2011), DICE and RICE (http://www.econ.yale.edu/~nordhaus/homepage/dicemodels.htm). The US Interagency Working Group on the Social Cost of Carbon has synthesized the results of some of these models and gives guidance for the appropriate SCC through time for three different discount rates (USIWGSCC, 2010; 2013). If your research questions lead you to a social cost of carbon approach, it is strongly recommended to consult this guidance. The most relevant considerations for applying SCC valuation based on the USIWGSCC approach in InVEST are the following:

 * The discount rate that you choose for your application must be one of the three options in the report (2.5%, 3%, or 5%). In the context of policy analysis, discount rates reflect society's time preferences. For a primer on social discount rates, see Baumol (1968).
 * Since the damages incurred from carbon emissions occur beyond the date of their initial release into the atmosphere, the damages from emissions in any one period are the sum of future damages, discounted back to that point. I.e. to calculate the SCC for emissions in 2030, the present value (in 2030) of the sum of future damages (2030 onward) is needed. This means that the SCC in any future period is a function of the discount rate, and therefore there are different SCC schedules (price list) for different discount rates. Your choice of an appropriate discount rate for your context will therefore determine the appropriate SCC schedule choice. 
 * The InVEST model does not currently allow you to import a price schedule, but rather asks for a current SCC and a rate of inflation. Since the USIWGSCC report lists prices at different time points in the future, you could perform a simple linear interpolation of prices to establish the inflation rate.    

An alternative to SCC is the market value of carbon credits approach. If the decision-maker is a private entity, such as an individual or a corporation, they may be able to monetize their land use decisions via carbon credits. Markets for carbon are currently operating across several geographies and new markets are taking hold in Australia, California, and Quebec (World Bank, 2012). These markets set a cap of total emissions of carbon and require that emitters purchase carbon credits to offset any emissions. Conservations efforts that increase sequestration can be leveraged as a means to offset carbon emissions and therefore sequestered carbon can potentially be monetized at the price established in a carbon credit market. The means for monetizing carbon offsets depends critically on the specific rules of each market, and therefore it is important to determine whether or not your research context allows for the sale of sequestration credits into a carbon market. It is also important to note that the idiosyncrasies of market design drive carbon credit prices observed in the market and therefore prices do not necessarily reflect the social damages from carbon. 

  
Valuation function 
""""""""""""""""""

.. math:: V_{x} = \sum_{t=0}^{T} \frac{p_t (C_{t,x} - C_{t-1,x}}{(1+d)^t})

where 

 * :math:`T` is the number of years between the current date and the end of the habitat change
 * :math:`p_t` is the price of carbon at time :math:`t`
 * :math:`C_{t,x}` is the carbon stock on pixel :math:`x` at time :math:`t`
 * and :math:`d` is the discount rate

 
Limitations and simplifications
===============================
In the absence of detailed knowledge on the carbon dynamics in coastal and marine systems, we take the simplest accounting approach and draw on published carbon stock datasets from neighboring coastlines.  We use carbon estimates from the most extensive and up-to-date published global datasets of carbon storage and accumulation rates (e.g., Fourqurean et al. 2012 & Silfeet et al. 2011).

 * We assume all storage and accumulation occurrs in the aboveground biomass and sediments.
 * We ignore increases in stock and accumulation with growth and aging of habitats.
 * We assume that carbon is stored and accumulated linearly through time between the current and future scenarios.
 * We assume that some human activities that may degrade coastal ecosystems do not disturb carbon in the sediments.
 * While the social cost of carbon estimates represent the state of the art in linking climatic factors to the global economy they are subject to an array of limitations and simplifications.


Data Needs
==========

Biophysical inputs
------------------

The following are the data needs for the biophysical portion of the InVEST blue carbon model:

 * **Land use / land cover (LULC) maps**: Maps of current (:math:`t_{1}`) and future (:math:`t_{t}`) LULC (e.g., developed dry land, shrimp aquaculture, mangrove forest, salt marsh, etc).

 * **Carbon pools and storage table by LULC type**: A table containing values of carbon storage in biomass (tons of CO\ :sub:`2` e/ha), sediments (tons of CO\ :sub:`2` e/ha) and accumulation rates (tons of CO\ :sub:`2` e/ha/yr).  In order to link these values with the biomass and soil disturbance CSV tables, use the "Veg Type" column to indicate "1" for marsh, "2" for mangrove, "3" for seagrass and "0" for other LULC types.

 * **Year of current LULC map**: (:math:`t_{1}`), the start year of the analysis.
 
 * **Year of one or more future LULC map**: (:math:`t_{t}`), model uses this and the previous input to determine length of time (number of years; (:math:`t_{2}` - :math:`t_{1}`) of the analysis and multiplies this value by the user-specified accumulation rates (tons of CO\ :sub:`2` e/ha/yr).  If the user is only interested in the standing stock of carbon at :math:`t_{1}`, then this input is optional.  Valuation, however, is not possible without estimates for at least :math:`t_{2}` (future LULC map).
 
 * **Transition matrix**: A table is produced by the pre-processor tool and indicates either disturbance or accumulation of carbon based on pre-programmed logic for LULC transitions from :math:`t_{1}` to :math:`t_{2}`.  These defaults produced by the pre-processor can be overriden by the user.
 
 * **Biomass disturbance**: A default table indicating the percent of biomass carbon disturbance by level of impact and vegetation type.  Defaults are based on based on a global literature review.
 
 * **Soil disturbance**: A default table indicating the rate of soil carbon disturbance by level of impact and vegetation type.  Defaults are based on based on a global literature review.

 * **Carbon half-lives**: A default table containing vegetation/disturbance-specific carbon decay rates based on a global literature review. 
 
Economic inputs
---------------

Data on the market or social value of sequestered carbon and its annual rate of change and a discount rate can be used in an optional model that estimates the value of this ecosystem service. 

The value of carbon sequestration over time is given by:

 * **Value of a sequestered ton of carbon**: (:math:`V` in the equation above), in dollars per metric ton of elemental carbon (not CO\ :sub:`2`, which is heavier, so be careful to get units right! If the social value of CO\ :sub:`2` e is $Y per metric ton, then the SCC is $(3.67*Y) per metric ton.

 * **Discount rate**: (:math:`r` in the equation above), which reflects time preferences for immediate benefits over future benefits. If the rate is set equal to 0% then monetary values are not discounted.

 * **Annual rate of change in the price of carbon**: (:math:`c` in the equation below), which adjusts the value of sequestered carbon as the impact of emissions on expected climate change-related damages changes over time.


Running the Model
=================

Pre-Processor
-------------
To run the InVEST blue carbon pre-processor tool click the Windows Start Menu >> All Programs >> InVEST >> Blue Carbon >> Blue Carbon Preprocessor.  Click the *Run* button to start the model.  A successful run will be indicated in the window and a file explorer will open containing the results.

 * **Workspace**: The directory to hold output and intermediate results from the tool. After the run is completed the output will be located in this directory.
 
 * **Preprocessor key**: This is the default key for ranking different degrees of accumulation and decay as a result of LULC transitions.  It should be left as is.
 
 * **Labels**: Using the carpon pools file (carbon.csv), the pre-processor will parse the label information including LULC ID, name and vegetation type.
 
 * **LULC maps**: Provide all the available LULC maps during the analysis time period.   These maps must be in raster format (ESRI grid or geoTIF).
 
.. figure:: ./blue_carbon_images/interface_preprocessor.png
 

Core Model
----------
To run the InVEST blue carbon pre-processor tool click the Windows Start Menu >> All Programs >> InVEST >> Blue Carbon >> Blue Carbon Calculator. The main interface indicates the required and optional input arguments as described in the **Data Needs** section above.  Click the *Run* button to start the model.  A successful run will be indicated in the window and a file explorer will open containing the results.

If you encounter any errors please post to the user's support forum at http://ncp-yamato.stanford.edu/natcapforums.

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory.
 
 * **LULC Year 1**: The LULC raster map for year 1.
 
 * **Year 1**: The date of LULC Year 1 map
 
 * **LULC Year 2**: The land use land cover raster for time 1 ``(optional -- required for valuation)``.
 
 * **Year 2**: The date of LULC Time 1 ``(optional -- required for valuation)``
 
 * **Analysis End Year**: The date of the final year of the analysis.  The model can calculate carbon accumulation and loss beyond the year of the latest LULC input map.  This functionality can be useful when future LULC maps do not exist or for estimating the market or social cost of carbon to a later date.
 
 * **Soil Disturbance CSV**: A table indicating the percentage of carbon loss in the soil pool by vegetation type.  The model will select the appropriate percentage value based on the disturbance level (low, medium, high) indicated in transition matrix table input.  Do not change any of the column headings in this table.
 
 * **Biomass Disturbance CSV**: A table indicating the percentage of carbon loss in the biomass pools by vegetation type.  The model will select the appropriate percentage value based on the disturbance level (low, medium, high) indicated in transition matrix table input.  Do not change any of the column headings in this table.
 
 * **Carbon Pools CSV:** A table of LULC classes, containing data on carbon in metric tons per hectacre \( t ha\ :sup:`-1`\) stored in each of the four fundamental pools for each LULC class. Carbon storage data can be collected from field estimates from local plot studies, extracted from meta-analyses on specific habitat types or regions, or found in general published tables (e.g., IPCC, see Appendix). If information on some carbon pools is not available, pools can be estimated from other pools, or omitted by leaving all values for the pool equal to 0.  For vegetation types that accumulates carbon in biomass and soil, the last two columns indicate the accumulation rates in tons of CO\ :sub:`2` e/ha/yr.  Do not change any of the column headings in this table.
  
 * **Carbon Half-Lives CSV**: A table containing vegetation/disturbance-specific carbon decay rates based on a global literature review.  These half-life should only be modified when site-specific information exists. Do not change any of the column headings in this table.
 
 * **Transition Matrix CSV**: A table called "transition.csv" produced by the pre-processor that can be found in the "Output" folder of the tool's workspace.  This table must be modified before it can be an input for the core blue carbon model.  For all cells within the matrix containing the values "Disturbance", change to either "Low Disturbance", "Medium Disturbance", or "High Disturbance" based on the intensity of impact on carbon for that specific transition.  When completed, save the edits and point to this file in the interface for this input.   

 * **Price in term of metric tons of** ``(optional -- required for valuation)``: This is whether the price per metric ton is in terms of elemental carbon or CO\ :sub:`2` which is heavier.
 
 * **Value of Carbon (USD/metric ton)** ``(optional -- required for valuation)``: The social cost of carbon or private market value for carbon in United States dollars.
 
 * **Market discount price of Carbon (%)** ``(optional -- required for valuation)``: The discount rate reflects time preferences for immediate benefits over future benefits. If the rate is set equal to 0% then monetary values are not discounted.
 
 * **Annual rate of change in price of Carbon (%)** ``(optional -- required for valuation)``: This adjusts the value of sequestered carbon as the impact of emissions on expected climate change-related damages changes over time. 

.. figure:: ./blue_carbon_images/interface_core.png
 
 
Interpreting Results
====================

Model Ouputs
------------

Output folder
^^^^^^^^^^^^^
 * ``extent.shp``: A shapefile indicating the bounding area of all the input LULC maps.
 * ``preprocessor_report.htm``: An HTML document with summary tables produced by the pre-processor tool.
 * ``core_report.htm``: An HTML document with summary tables produced by the core model.
 * ``gain_[time t-1]_[time t].tif``: A raster map indicating areas where carbon is gained from time t-1 to time t (in Mg per pixel).
 * ``loss_[time t-1]_[time t].tif``: A raster map indicating areas where carbon is lost from time t-1 to time t (in Mg per pixel).
 * ``sequest_[time t-1]_[time t].tif``: A raster map of carbon sequestration (gain minus loss) from time t-1 to time t (in Mg per pixel).
 * ``stock_[time t].tif``: A raster map of the total stock of carbon in all four pools at time t (in Mg per pixel). 
 * ``[time t-1]_[time t]_npv.tif``: A raster map indicating the net present value of carbon sequestered per pixel. 
 
intermediate folder
^^^^^^^^^^^^^^^^^^^ 
 * ``[time 0]_veg_[veg ID]_stock_biomass.tif``: For each vegetation type, the carbon stock in the biomass pools at time 0.
 * ``[time 0]_veg_[veg ID]_stock_soil.tif``: For each vegetation type, the carbon stock in the soil pool at time 0.
 * ``[time t]_veg_[veg ID]_litter.tif``: Carbon stock in the litter/dead pool at time t.
 * ``[time t-1]_[time t]_bio_acc.tif``: Total carbon accumulation in the biomass pools from time t-1 to time t.
 * ``[time t-1]_[time t]_bio_dis.tif``: Total carbon disturbance in the biomass pools from time t-1 to time t.
 * ``[time t-1]_[time t]_soil_acc.tif``: Total carbon accumulation in the soil pool from time t-1 to time t.
 * ``[time t-1]_[time t]_soil_dis.tif``: Total carbon disturbance in the soil pool from time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_acc_bio.tif``: For each vegetation type, the total carbon accumulation in the biomass pools from time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_acc_soil.tif``: For each vegetation type, the total carbon accumulation in the soil pool from time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_dis_bio.tif``: For each vegetation type, the total carbon disturbance of the biomass pools from time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_dis_soil.tif``: For each vegetation type, the total carbon disturbance of the soil pool from time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_adj_dis_bio.tif``: For each vegetation type, the cumulative carbon disturbance of the biomass pools from time 0 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_adj_dis_soil.tif``: For each vegetation type, the cumulative carbon disturbance of the soil pool from time 0 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_adj_acc_bio.tif``: For each vegetation type, the total carbon stock in the biomass pools at time t-1 adjusted for accumulation (+) and disturbance (-) occuring between time t-1 and time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_adj_acc_soil.tif``: For each vegetation type, the total carbon stock in the soil pool at time t-1 adjusted for accumulation (+) and disturbance (-) occuring between time t-1 and time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_em_bio.tif``:  For each vegetation type, the amount of carbon in the biomass pools emitted between time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_em_soil.tif``: For each vegetation type, the amount of carbon in the soil pool emitted between time t-1 to time t.
 * ``[time t-1]_[time t]_veg_[veg ID]_adj_em_dis_bio.tif``: For each vegetation type, the cumulative carbon disturbance of the biomass pools from time 0 to time t adjusted for emissions.
 * ``[time t-1]_[time t]_veg_[veg ID]_adj_em_dis_soil.tif``: For each vegetation type, the cumulative carbon disturbance of the soil pool from time 0 to time t adjusted for emissions.
 
 
Case example illustrating results
=================================

Freeport, Texas
---------------

Summary
^^^^^^^

Over the next 100 years, the US Gulf coast has been identified as susceptible to rising sea levels.  The use of the InVEST blue carbon model serves to identify potential changes in the standing stock of carbon in coastal vegetation that sequester carbon.  This approach in Freeport, TX was made possible with rich and resolute elevation and LULC data sets.  We used a 10-meter DEM with sub-meter vertical accuracy to model marsh migration and loss over time as a result of sea level rise using Warren Pinnacle's SLAMM (Sea Level Affected Marsh Model).  Outputs from SLAMM serve as inputs to the InVEST blue carbon model which permits the tool to map, measure and value carbon sequestration and emissions resulting from coastal land cover change over a 94-year period.
 
The Sea Level Affecting Marshes Model (SLAMM: http://www.warrenpinnacle.com/prof/SLAMM/) models changes in the distribution of 27 different coastal wetland habitat types in response to sea-level rise.  The model relies on the relationship between tidal elevation and coastal wetland habitat type, coupled with information on slope, land use, erosion and accretion to predict changes or loss of habitat.  SLAMM outputs future habitat maps for user-defined time steps and sea-level rise scenarios. These future habitat maps can be utilized with InVEST service models to evaluate resultant changes in ecosystem services under various sea-level rise scenarios (e.g. 1 m SLR by 2100).
 
For example, SLAMM was used to quantify differences in carbon sequestration over a range of sea-level rise projections in Galveston Bay, Texas, USA.  First, SLAMM was used to map changes in the distribution of coastal wetland habitat over time under different sea-level rise projections.  Then, the InVEST blue carbon model was used to evaluate changes in carbon sequestration associated with predicted changes in habitat type.  The 27 land-cover classes modeled by SLAMM were condensed into a subset relevant to carbon sequestration and converted from ASCII to raster format for use with InVEST.  SLAMM results produced LULC maps of future alternative scenarios over 25-year time slices beginning in 2006 and ending in 2100.  The following figure depicts 2006 LULC and a table of disaggregated land class types.

[INSERT FIGURE 1]

Figure CS1. Current (2006) LULC map for Freeport, Texas

Carbon stored in the sediment ('soil' pool) was the focus of the biophysical analysis.  The vast majority of carbon is sequestered in this pool by coastal and marine vegetation.  See the case study limitations for additional information.  To produce maps of carbon storage at the different 25-year time steps, we used the model to perform a simple "look-up" to determine the amount of carbon per 10-by-10 meter pixel based on known storage rates from sampling in the Freeport area (Chmura et al. 2003).
 
Next, we provide the InVEST model with a transition matrix in order to identify the amount of carbon gained or lost over each 25-year tiume step.  Annual accumulation rates in salt marsh were also obtained from Chmura et al. (2003).  When analyzing the time period from 2025 to 2050, we assume :math:`t_{2}` = 2025 and :math:`t_{3}` = 2050.  We identify all the possible transitions that will result in either accumulation or loss of carbon.  The model compares the two LULC maps (:math:`t_{2}` and :math:`t_{3}`) to identify any pixel transitions from one land cover type to another.  We apply these transformations to the standing stock of carbon which is the running carbon tally at :math:`t_{2}` (2025).  Once these adjustments are complete, we have a new map of standing carbon for :math:`t_{3}` (2050).  We repeat this step for the next time period where :math:`t_{3}` = 2050 and :math:`t_{4}` = 2075.  This process was repeated until 2100.  The model produces spatially explicit depictions of net sequestration over time as well as summaries of net gain/emission of carbon for the two scenarios at each 25-year time step.  This information was used to determine during which time period for each scenario the rising seas and resulting marsh migration led to net emissions for the study site and the entire Freeport area.

+------------------------------------------+----------------------------+-------------------------+
| Time Period                              | Scenario #1: No Management | Scenario #2: High Green |
+==========================================+============================+=========================+
|  2006-2025 (:math:`t_{1}`-:math:`t_{2}`) | +4,031,180                 | +4,172,370              |
+------------------------------------------+----------------------------+-------------------------+
|  2025-2050 (:math:`t_{2}`-:math:`t_{3}`) | -1,170,580                 | +684,276                |
+------------------------------------------+----------------------------+-------------------------+
|  2050-2075 (:math:`t_{3}`-:math:`t_{4}`) | -7,403,690                 | -5,525,100              |
+------------------------------------------+----------------------------+-------------------------+
|  2075-2100 (:math:`t_{4}`-:math:`t_{5}`) | -7,609,020                 | -8,663,600              |
+------------------------------------------+----------------------------+-------------------------+
|  100-Year Total:                         | -12,152,100                | -9,332,050              |
+------------------------------------------+----------------------------+-------------------------+

Table CS1. Net carbon sequestration and emissions for each 25-year time period for the two scenarios of the entire Freeport study area.


[INSERT FIGURE 2]


Figure CS2. Carbon emissions (red) and sequestration (blue) from 2006 to 2100 for the two scenarios of the entire Freeport study area.

The following is table summarizing how the main inputs, where they were obtained and how they were used in the model:

+--------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input                                      | Source                                           | Use in the InVEST blue carbon model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+============================================+==================================================+===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| DEM                                        | USGS                                             | DEM was needed to produce the future LULC maps using the SLAMM tool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Land use / land cover (LULC)               | USGS/NOAA                                        | Salt marshes store carbon in biomass and soils.  We utilized maps showing the current distribution of salt marshes to establish a baseline coverage of marshes from which we estimate aboveground biomass and soil carbon.                                                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Carbon stock in salt marsh systems         | Natural Capital Project literature review        | Carbon storage was calculated by summing the carbon stored in biomass and sediments.  Carbon stocks were calculated for all of the areas of functional salt marsh in the study region (Chmura et al. 2003).                                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Social value of carbon in 2006 US $        | USIWGSCC 2010                                    | The "social cost of carbon" (SCC) is an estimate of the monetized damages associated with an incremental increase in carbon emissions in a given year.  It is intended to include (but is not limited to) changes in net agricultural productivity, human health, property damages from increased flood risk, and the value of ecosystem services.  The social cost of carbon is useful for allowing institutions to incorporate the social benefits of reducing carbon dioxide (CO\ :sub:`2`) emissions into cost benefit analyses of management actions that have small, or "marginal," impacts on cumulative global emissions. |
+--------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Discount rate                              | USIWGSCC 2010                                    | This discount rate reflects society's preferences for short run versus long term consumption.  Since carbon dioxide emissions are long-lived, subsequent damages occur over many years.  We use the discount rate to adjust the stream of future damages to its present value in the year when the emissions were changed.                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Table CS2. Input summary table for using InVEST blue carbon model in Freeport, Texas

Limitations
^^^^^^^^^^^
 * This analysis did not model change in carbon resulting from growth or loss of aboveground biomass of coastal and marine vegetation.
 * While the spatial resolution of the LULC maps produced by SLAMM was very high (10 meters), the temporal resolution provided by SLAMM was quite coarse (25-year time steps).  The carbon cycle is a dynamic process.  By analyzing change over 25-year time periods, we ignore any changes that are not present at the start and end of each time step.

 
References
==========

Baumol, W. J. (1968). On the social rate of discount. The American Economic Review, 788-802. 

Bouillon, S., Borges, A. V., Castañeda-Moya, E., Diele, K., Dittmar, T., Duke, N. C., ... & Twilley, R. R. (2008). Mangrove production and carbon sinks: a revision of global budget estimates. Global Biogeochemical Cycles, 22(2).

Chmura, G. L., Anisfeld, S. C., Cahoon, D. R., & Lynch, J. C. (2003). Global carbon sequestration in tidal, saline wetland soils. Global biogeochemical cycles, 17(4). 

Clough, J. S., Park, R., and Fuller, R. (2010). "SLAMM 6 beta Technical Documentation."  Available
at http://warrenpinnacle.com/prof/SLAMM. 

Fourqurean, J. W., Duarte, C. M., Kennedy, H., Marbà, N., Holmer, M., Mateo, M. A., ... & Serrano, O. (2012). Seagrass ecosystems as a globally significant carbon stock. Nature Geoscience, 5(7), 505-509.

Hope, Chris. (2011) "The PAGE09 Integrated Assessment Model: A Technical Description." Cambridge Judge Business School Working Paper No. 4/2011 (April). Available at http://www.jbs.cam.ac.uk/research/working_papers/2011/wp1104.pdf.

Pendleton, L., Donato, D. C., Murray, B. C., Crooks, S., Jenkins, W. A., Sifleet, S., ... & Baldera, A. (2012). Estimating global “blue carbon” emissions from conversion and degradation of vegetated coastal ecosystems. PLoS One, 7(9), e43542.

Rosenthal, A., Arkema, K., Verutes, G., Bood, N., Cantor, D., Fish, M., Griffin, R., and Panuncio, M. (In press). Identification and valuation of adaptation options in coastal-marine ecosystems: Test case from Placencia, Belize. Washington, DC: InterAmerican Development Bank. Technical Report. 

Sifleet, S., Pendleton, L., and B. Murray. (2011). State of the Science on Coastal Blue Carbon. Nicholas Institute Report, 1-43.

United States, Interagency Working Group on Social Costs of Carbon. (2010) "Technical Support Document: Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866." Available at http://www.epa.gov/otaq/climate/regulations/scc-tsd.pdf.

United States, Interagency Working Group on Social Costs of Carbon. (2013) "Technical Update of the Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866." Available at http://www.whitehouse.gov/sites/default/files/omb/inforeg/social_cost_of_carbon_for_ria_2013_update.pdf.

World Bank. (2012). State and Trends of the Carbon Market 2012. Washington DC: The World Bank, 133.