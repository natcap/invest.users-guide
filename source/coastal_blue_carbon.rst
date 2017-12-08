.. _coastal-blue-carbon:

*******************
Coastal Blue Carbon
*******************

Summary
=======

Marine and terrestrial ecosystems help regulate Earth's climate by adding and removing greenhouse gases (GHGs) such as carbon dioxide (CO\ :sub:`2`) to and from the atmosphere.  Coastal marshes, mangroves, and seagrasses, in particular, store large amounts of carbon in their sediments, leaves, and other forms of biomass.  In addition to storing carbon, marine ecosystems continually accumulate carbon in their sediments, creating large reservoirs of long-term sequestered carbon. By storing and sequestering carbon, marine ecosystems keep CO\ :sub:`2` out of the atmosphere where it would otherwise contribute to climate change.

Management activities that change the cover of coastal vegetation, such as the restoration of seagrass beds and the clearing of mangrove forests, change the ability of coastal and marine areas to store and sequester carbon.

The InVEST Coastal Blue Carbon model attempts to predict the amount of carbon stored and sequestered over a coastal zone at particular points in time due to changes in land cover. Using an estimate of the monetary social value, or where available, a market price for stored and sequestered carbon, the InVEST Coastal Blue Carbon model also quantifies the marginal value of storage and sequestration.

Results of the InVEST Coastal Blue Carbon model can be used to compare current and future scenarios of carbon stock and net sequestration, as well as identify locations within the landscape where degradation of coastal ecosystems should be avoided and restoration of coastal ecosystems should be prioritized in order to preserve and enhance these carbon storage & sequestration services.

Introduction
============

This model makes use of a variety of information, including:

- The distribution and abundance of coastal vegetation
- Habitat-specific carbon stock data
- Impact characteristics of various land-cover disturbances to biomass and soil carbon stock pools to predict carbon emission rates
- Carbon accumulation rates to estimate carbon stock, net sequestration and value across a land or seascape
- Estimates of the monetary social value or market price of carbon

To quantify the value of carbon storage and sequestration, the model focuses on changes in atmospheric carbon dioxide and other greenhouse gases as a result of changes caused by human activities that can affect marine ecosystems which store and sequester carbon.  Changes to the composition of the atmosphere have wide-ranging effects on natural systems that can result in changes to agricultural productivity, air quality, sea levels, and more.

The Model
=========

Modeling Considerations
-----------------------

Mapping and modeling changes in carbon storage and sequestration for coastal and marine habitats can present challenges.  The types of spatial inputs and available information about the carbon cycle vary by location.  Some study areas have high-quality data available for a detailed analysis while other locations do not have the information necessary to model changes in the position and function of coastal vegetation.  Salt marsh, for example, is often studied in the context of migration due to sea-level rise.  The combination of natural (e.g. sea-level rise) and anthropogenic (e.g. salt marsh migration blocked by roads) factors should be included in scenario maps and subsequent carbon modeling where possible.  When exploring future land cover scenarios, land cover map outputs produced by the SLAMM model (Sea Level Affecting Marshes Model, developed by Warren Pinnacle) can be useful inputs to the InVEST Coastal Blue Carbon model (Clougheet et al. 2010).  However, because not all sites have the detailed elevation and habitat information required to run SLAMM, this InVEST model provides a flexible approach that allows users to provide either detailed land use/land cover maps or maps indicating the presence of coastal and marine vegetation that can sequester carbon.

How it Works
------------

InVEST Coastal Blue Carbon models the carbon cycle through a bookkeeping-type approach (Houghton, 2003). This approach simplifies the carbon cycle by accounting for storage in three main pools (biomass, sediment carbon (i.e. soil), and standing dead carbon (i.e. litter) see Figure 1).  Accumulation of carbon in coastal habitats occurs primarily in sediments (Pendleton et al., 2012).  The model requires users to provide maps of coastal ecosystems that store carbon, such as mangroves and seagrasses.  Users must also provide data on the amount of carbon stored in the three carbon pools and the rate of annual carbon accumulation in the biomass and sediments. If local information is not available, users can draw upon the global database of values for carbon stocks and accumulation rates sourced from the peer-reviewed literature that is included in the model.  If data from field studies or other local sources are available, these values should be used instead of those in the global database.  The model requires land cover maps, which represent changes in human use patterns in coastal areas or changes to sea level, to estimate the amount of carbon lost or gained over a specified period of time.  The model quantifies carbon storage across the land or seascape by summing the carbon stored in these three carbon pools.

.. figure:: ./coastal_blue_carbon_images/pools.png

Figure 1. Three carbon pools for marine ecosystems included in the InVEST blue carbon model (mangrove example).


Carbon Storage
^^^^^^^^^^^^^^

The carbon stored in a grid cell :math:`x` at time :math:`t`, given by :math:`S_{xt}` and measured in Megatonnes of CO\ :sub:`2` equivalent, is equal to the sum of the carbon stored in each pool in the grid cell at any time (:math:`t`),

.. math:: S_{total} = S_{biomass} + S_{soil} + S_{litter}

where :math:`S_{biomass}`, :math:`S_{soil}`, :math:`S_{litter}` indicate the respective Megatonnes of CO\ :sub:`2` equivalent stored in the biomass, soil, and litter pools in a grid cell of a particular coastal blue carbon habitat.

Coastal blue carbon habitats can simply indicate the dominant vegetation type (e.g., eelgrass, mangrove, etc), or they can be based on details that affect pool storage values such as plant species, vegetation density, temperature regime, or vegetation age (e.g., time since restoration or last major disturbance).

For the sake of the carbon storage estimation, each coastal blue carbon habitat is assumed to be in storage equilibrium at any point in time (accumulation of carbon will be accounted for in the sequestration component of the model).

Carbon Accumulation
^^^^^^^^^^^^^^^^^^^

We model accumulation as the rate of carbon retained in the soil in organic form after the first year of decomposition. In relation to the annual ecosystem budget, this pool has not been remineralized, so it represents net accumulation. This carbon is usually derived from belowground production, and residence time can range from decades to millennia (Romero et al. 1994, Mateo et al. 1997). This accumulation contributes to the development of carbon "reservoirs" which are considered virtually permanent unless disturbed. Thus, even in the absence of a land-use or land-cover change, carbon continues to be sequestered naturally.

We estimate accumulation by multiplying habitat specific rates of carbon accumulation by the given cell area. The carbon accumulated in a grid cell :math:`x` at time :math:`t` in carbon pool :math:`p`, given by :math:`A_{pt}` and measured in Megatonnes of CO\ :sub:`2` equivalent per year, is equal to the rate of carbon accumulation in the sediments at time :math:`t`.

Loss of carbon from the soil pool (sediments) upon disturbance is more nuanced than sequestration because different types of human uses and/or stasis may cause varied disruption of the soils and the carbon stored below.  For example, high impact activities such as the clearing of mangroves for a shrimp pond or sediment dredging may result in a larger soil carbon disturbance than other activities such as commercial fishing or oil exploration.  The impacts from coastal development on carbon storage vary since some types of development may involve paving over the soil, which often keeps a large percentage of the carbon stored intact.  Alternatively, dredging could remove seagrasses and disturb the sediments below, releasing carbon into the atmosphere.


Carbon Emissions
^^^^^^^^^^^^^^^^

When coastal ecosystems are degraded by human activities, the carbon stored in the living plant material (above and below the ground) and the soil may be emitted to the atmosphere. The magnitude of post-conversion CO\ :sub:`2` release depends on the type of vegetation disturbed and the level of disturbance. The type of disturbance will determine the amount of aboveground biomass loss and depth to which the soil profile will be altered. The deeper the effects of the disturbance, the more soil carbon that will be exposed to oxygen, oxidized and consequently emitted in the form of CO\ :sub:`2`. Some disturbances will only disturb the top soil layers while the deeper layers remain inundated and their carbon intact.  Other disturbances may affect several meters of the soil profile. To estimate the extent of the impact of various disturbances, we classify disturbances into three categories of impact: high, medium and low.  Examples of high impact disturbances include mangrove conversion to shrimp farms and draining or diking salt marshes for conversion to agriculture.  Low impact disturbance examples include recreational boating or float home marinas.

Magnitude and Timing of Loss
""""""""""""""""""""""""""""

We model the release of carbon from the biomass and soil pools by estimating the fraction of carbon lost from each pool's total stock at the time of disturbance.  The fraction of carbon lost is determined by the original coastal blue carbon habitat and the level of impact resulting from the disturbance (see Table 1).

The InVEST Coastal Blue Carbon model allows users to provide details on the level of disturbance that occurs during a transition from a coastal blue carbon habitat to a non-coastal blue carbon habitat.  This information can be provided to the model through a pre-processor tool (See "Transition Storage" section) and further clarified with an input transition table.

In general, carbon stock pools emit carbon at different rates: most emissions from the biomass pool take place within the first year, whereas emissions from the soil pool may take much longer. The model assigns exponential decay functions and half-life values to the biomass and soil carbon pools of each habitat type (Table 1; Murray et al. 2011).

Carbon emitted at time :math:`t` due to a disturbance:

.. math:: E_{p} = D_{p} \cdot ({ 0.5 }^{ \frac { t-(r+1) }{ H_{p} } } - { 0.5 }^{ \frac { t-r }{ H_{p} } })

where :math:`p` is the carbon pool (biomass and soil), :math:`D_{p}` represents the amount of carbon stock disturbed as time approaches infinity, :math:`H_{p}` represents the half-life of the disturbance event, and :math:`E_{p}` represents the share of carbon released from the total disturbed carbon stock at time :math:`t`.


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
| **Methane emissions**              | 1.85 T  CO\ :sub:`2`/ha/yr (4)                                                                     | 0.4 T CO\ :sub:`2`/ha/yr                                                                                          | Negligible                                                                                                                             | Use literature / field data          |
+------------------------------------+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+

Table 1: Percent carbon loss and habitat-specific decay rates as a result of low (LI), medium (MI) and high (HI) impact activities disturbing salt marsh, mangrove, and seagrass ecosystems.  These default values can be adjusted by modifying the input CSV tables.

References (numbers in parentheses above):

1. Donato, D. C., Kauffman, J. B., Murdiyarso, D., Kurnianto, S., Stidham, M., & Kanninen, M. (2011). Mangroves among the most carbon-rich forests in the tropics. Nature Geoscience, 4(5), 293-297.
2. Murray, B. C., Pendleton, L., Jenkins, W. A., & Sifleet, S. (2011). Green payments for blue carbon: Economic incentives for protecting threatened coastal habitats. Nicholas Institute for Environmental Policy Solutions, Report NI, 11, 04.
3. Crooks, S., Herr, D., Tamelander, J., Laffoley, D., & Vandever, J. (2011). Mitigating climate change through restoration and management of coastal wetlands and near-shore marine ecosystems: challenges and opportunities. Environment Department Paper, 121, 2011-009.
4. Krithika, K., Purvaja, R., & Ramesh, R. (2008). Fluxes of methane and nitrous oxide from an Indian mangrove. Current Science (00113891), 94(2).


Valuation of Net Sequestered Carbon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The valuation option for the blue carbon model estimates the economic value of sequestration (not storage) as a function of the amount of carbon sequestered, the monetary value of each ton of sequestered carbon, a discount rate, and the change in the value of carbon sequestration over time. The value of sequestered carbon is dependent on who is making the decision to change carbon emissions and falls into two categories: social and private. If changes in carbon emissions are due to public policy, such as zoning coastal areas for development, then decision-makers should weigh the benefits of development against the social losses from carbon emissions. Because local carbon emissions affect the atmosphere on a global scale, the social cost of carbon (SCC) is commonly calculated at a global scale (USIWGSCC, 2010). Efforts to calculate the social cost of carbon have relied on multiple integrated assessment models such as FUND (http://www.fund-model.org/), PAGE (Hope, 2011), DICE and RICE (http://www.econ.yale.edu/~nordhaus/homepage/dicemodels.htm). The US Interagency Working Group on the Social Cost of Carbon has synthesized the results of some of these models and gives guidance for the appropriate SCC through time for three different discount rates (USIWGSCC, 2010; 2013). If your research questions lead you to a social cost of carbon approach, it is strongly recommended to consult this guidance. The most relevant considerations for applying SCC valuation based on the USIWGSCC approach in InVEST are the following:

 * The discount rate that you choose for your application must be one of the three options in the report (2.5%, 3%, or 5%). In the context of policy analysis, discount rates reflect society's time preferences. For a primer on social discount rates, see Baumol (1968).
 * Since the damages incurred from carbon emissions occur beyond the date of their initial release into the atmosphere, the damages from emissions in any one period are the sum of future damages, discounted back to that point. For example, to calculate the SCC for emissions in 2030, the present value (in 2030) of the sum of future damages (2030 onward) is needed. This means that the SCC in any future period is a function of the discount rate, and therefore, a consistent discount rate should be used throughout the analysis. There are different SCC schedules (price list) for different discount rates. Your choice of an appropriate discount rate for your context will, therefore, determine the appropriate SCC schedule choice.

An alternative to SCC is the market value of carbon credits approach. If the decision-maker is a private entity, such as an individual or a corporation, they may be able to monetize their land use decisions via carbon credits. Markets for carbon are currently operating across several geographies and new markets are taking hold in Australia, California, and Quebec (World Bank, 2012). These markets set a cap on total emissions of carbon and require that emitters purchase carbon credits to offset any emissions. Conservation efforts that increase sequestration can be leveraged as a means to offset carbon emissions and therefore sequestered carbon can potentially be monetized at the price established in a carbon credit market. The means for monetizing carbon offsets depends critically on the specific rules of each market, and therefore it is important to determine whether or not your research context allows for the sale of sequestration credits into a carbon market. It is also important to note that the idiosyncrasies of market design drive carbon credit prices observed in the market and therefore prices do not necessarily reflect the social damages from carbon.

Net Present Value of Sequestration
""""""""""""""""""""""""""""""""""

.. math:: V_{x} = \sum_{t=0}^{T} \frac{p_t (C_{t,x} - C_{t-1,x})}{(1+d)^t}

where

 * :math:`T` is the number of years between the current date and the end of the habitat change
 * :math:`p_t` is the price per ton of carbon at time :math:`t`
 * :math:`C_{t,x}` is the carbon stock on pixel :math:`x` at time :math:`t`
 * and :math:`d` is the discount rate


Identifying LULC Transitions with the Preprocessor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The land use / land cover (LULC) maps provide snapshots of a changing landscape and are the inputs that drive carbon accumulation and emissions in the model.  The user must first produce a set of coastal and marine habitat maps via a land change model (e.g., SLAMM), a scenario assessment tool, or manual GIS processing.  The user must then input the LULC maps into the model in chronological order (:math:`s_{0}`, :math:`s_{1}`, ..., :math:`s_{n}`).

The preprocessor tool compares LULC classes across the maps to identify the set of all LULC transitions that occur.  The preprocessor tool then generates a transition matrix that indicates whether a transition occurs between two habitats (e.g. salt marsh to developed dry land) and whether carbon accumulates, is disturbed, or remains unchanged once that transition occurs.

Land Cover Transition Types:

- Other LULC Class :math:`\Rightarrow` Coastal Blue Carbon Habitat (*Carbon Accumulation* in Succeeding Years of Transition Event Until Next Bounding Year)

- Coastal Blue Carbon Habitat :math:`\Rightarrow` Coastal Blue Carbon Habitat (*Carbon Accumulation* in Succeeding Years of Transition Event Until Next Bounding Year)

- Coastal Blue Carbon Habitat :math:`\Rightarrow` Other LULC Class (*Carbon Disturbance* in Succeeding Years of Transition Event Until End of Time Series Forecast)

- Other LULC Class :math:`\Rightarrow` Other LULC Class (*No Carbon Change* in Succeeding Years of Transition Event Until Next Bounding Year)

This transition matrix produced by the coastal blue carbon preprocessor, and subsequently edited by the user, allows the model to identify where human activities and natural events disturb carbon stored by vegetation.   If a transition from one LULC class to another does not occur during any of the time steps, the cell will be left blank.  For cells in the matrix where transitions occur, the tool will populate a cell with 'accum' in the cases where a non-coastal blue carbon habitat transitions to a coastal blue carbon habitat or a coastal blue carbon habitat transitions to another coastal blue carbon habitat, 'disturb' in the case where a coastal blue carbon habitat transitions to a non-coastal blue carbon habitat, or 'NCC' (for no carbon change) in the case where a non-coastal blue carbon habitat transitions to another non-coastal blue carbon habitat.  For example, if a salt marsh pixel in :math:`t_{0}` is converted to developed dry land in :math:`t_{1}` then the cell will be populated with 'disturb'.  On the other hand, if a mangrove remains a mangrove over this same time period then this cell in the matrix will be populated with 'accum'.  It is likely that a mangrove that remains a mangrove will accumulate carbon in its soil and biomass.

The user will then need to modify the 'disturb' cells with either 'low-impact-disturb', 'med-impact-disturb' or 'high-impact-disturb' depending on the level of disturbance that occurs as the transition occurs between LULC types. This gives the user more fine-grained control over emissions due to disturbance.   For example, rather than provide only one development type in an LULC map, a user can separate out the type into two development types and update the transition matrix accordingly so that the model can more accurately quantify and map changes in carbon as a result of natural and anthropogenic factors.  Similarly, different species of mangroves may accumulate soil carbon at different rates.  If this information is known, it can improve the accuracy of the model to provide this species distinction (two different classes in the LULC input maps) and then the associated accumulation rates in the Carbon Pool Transient Values CSV table.


Model Math
----------

Dimensions
^^^^^^^^^^

- :math:`x, y`: Position
- :math:`t`: Timestep (*Years Ahead of Baseline Year*)
- :math:`s`: Snapshot Year (*Year in which a Snapshot is Provided*)
- :math:`r`: Transition Year (*Year in which a Transition Event Begins*)
- :math:`a`: Analysis Year (*Final Year of the Time Series Forecast*)
- :math:`b`: Bounding Year (*Year that Bounds a Transition Event*)
- :math:`p`: Carbon Pool

Multidimensional Matrices
^^^^^^^^^^^^^^^^^^^^^^^^^

- :math:`C_{s,x,y}`: LULC Map (*unitless*)
- :math:`S_{b,p,x,y}`: Carbon Stock for Biomass and Soil Pools (*Megatonnes CO2e*)
- :math:`L_{s,x,y}`: Litter Pool Carbon Stock (*Megatonnes CO2e*)
- :math:`T_{b,x,y}`: Total Carbon Stock (*Megatonnes CO2e*)
- :math:`Y_{r,p,x,y}`: Yearly Accumulated Carbon (*Megatonnes CO2e / Year*)
- :math:`A_{t,p,x,y}`: Accumulated Carbon (*Megatonnes CO2e / Year*)
- :math:`A_{r,p,x,y}`: Accumulated Carbon (*Megatonnes CO2e / Transition*)
- :math:`D_{r,p,x,y}`: Carbon Stock Disturbed (*Megatonnes CO2e*)
- :math:`H_{r,p,x,y}`: Disturbed Carbon Stock Emissions Half-life (*Years*)
- :math:`E_{t,p,x,y}`: Emitted Carbon (*Megatonnes CO2e / Year*)
- :math:`E_{r,p,x,y}`: Emitted Carbon (*Megatonnes CO2e / Transition*)
- :math:`N_{t,x,y}`: Net Sequestered Carbon (*Megatonnes CO2e / Year*)
- :math:`N_{r,x,y}`: Net Sequestered Carbon (*Megatonnes CO2e / Transition*)
- :math:`V_{x,y}`: Net Present Value of Net Sequestered Carbon (*$ at Baseline Year*)

Initial Conditions
^^^^^^^^^^^^^^^^^^

- :math:`S_{0,p,x,y}, L_{0,x,y}, T_{0,x,y}` :math:`\Leftarrow` reclass(:math:`C_{0,x,y}`, cell_size, lulc_carbon_stock_initial_conditions)

Time Series Forecast
^^^^^^^^^^^^^^^^^^^^

- :math:`Y_{r,p,x,y}, D_{r,p,x,y}, H_{r,p,x,y}, L_{s,x,y}` :math:`\Leftarrow` reclass(:math:`C_{s,x,y}`, :math:`S_{b,x,y}` cell_size, lulc_carbon_stock_transient_conditions)
- :math:`A_{t,p,x,y}` :math:`\Leftarrow` compute_timestep_accumulation(:math:`Y_{r,p,x,y}`, :math:`t`)
- :math:`E_{t,p,x,y}` :math:`\Leftarrow` compute_timestep_emissions(:math:`D_{r,p,x,y}`, :math:`H_{r,p,x,y}`, :math:`t`)
- :math:`N_{t,p,x,y}` :math:`\Leftarrow` compute_timestep_net_sequestration(:math:`A_{t,p,x,y}`, :math:`E_{t,p,x,y}`, :math:`t`)
- :math:`A_{r,p,x,y}` :math:`\Leftarrow` compute_transition_period_total_accumulation(:math:`Y_{r,p,x,y}`, :math:`r`)
- :math:`E_{r,p,x,y}` :math:`\Leftarrow` compute_transition_period_total_emissions(:math:`E_{t,p,x,y}`, :math:`r`)
- :math:`N_{r,p,x,y}` :math:`\Leftarrow` compute_transition_period_net_sequestration(:math:`A_{r,p,x,y}`, :math:`E_{r,p,x,y}`, :math:`r`)
- :math:`S_{b,p,x,y}` :math:`\Leftarrow` compute_carbon_stock(:math:`S_{b,p,x,y}`, :math:`N_{r,p,x,y}`, :math:`b`)
- :math:`T_{b,x,y}` :math:`\Leftarrow` compute_carbon_stock_with_litter(:math:`S_{b,p,x,y}`, :math:`L_{s,x,y}`, :math:`b`)
- :math:`V_{x,y}` :math:`\Leftarrow` compute_net_present_value(:math:`N_{t,p,x,y}`, :math:`price_t`, :math:`discount\_rate`)

Time Series Forecast Functions in Detail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

compute_timestep_accumulation(:math:`Y_{r,p,x,y}`, :math:`t`)

- :math:`A_{t,p,x,y}` :math:`\Leftarrow` :math:`Y_{r,p,x,y}`

compute_timestep_emissions(:math:`D_{r,p,x,y}`, :math:`H_{r,p,x,y}`, :math:`t`)

- :math:`E_{t,p,x,y}` :math:`\Leftarrow` :math:`\sum_{r_{prev}} \left( D_{r,p,x,y} \cdot ({ 0.5 }^{ \frac { t-(r+1) }{ H_{r,p,x,y} } } - { 0.5 }^{ \frac { t-r }{ H_{r,p,x,y} } }) \right)`

compute_timestep_net_sequestration(:math:`A_{t,p,x,y}`, :math:`E_{t,p,x,y}`, :math:`t`)

- :math:`N_{t,x,y}` :math:`\Leftarrow` :math:`A_{t,x,y} - E_{t,x,y}`

compute_transition_period_total_accumulation(:math:`Y_{r,p,x,y}`, :math:`r`)

- :math:`A_{r,p,x,y}` :math:`\Leftarrow` :math:`(t_{b\_next} - t_{b\_prev}) \cdot Y_{r,p,x,y}`

compute_transition_period_total_emissions(:math:`E_{t,p,x,y}`, :math:`r`)

- :math:`E_{r,p,x,y}` :math:`\Leftarrow` :math:`\sum_{t_{b\_prev}}^{t_{b\_next}} E_{t,p,x,y}`

compute_transition_period_net_sequestration(:math:`A_{r,p,x,y}`, :math:`E_{r,p,x,y}`, :math:`r`)

- :math:`N_{r,p,x,y}` :math:`\Leftarrow` :math:`A_{r,p,x,y} - E_{r,p,x,y}`

compute_carbon_stock(:math:`S_{b,p,x,y}`, :math:`N_{r,p,x,y}`, :math:`b`)

- :math:`S_{b_{next},p,x,y}` :math:`\Leftarrow` :math:`S_{b_{prev},p,x,y} + N_{r,p,x,y}`

compute_carbon_stock_with_litter(:math:`S_{b,p,x,y}`, :math:`L_{s,x,y}` :math:`b`)

- :math:`T_{b,x,y}` :math:`\Leftarrow` :math:`L_{s,x,y} + \sum_{p} S_{b,p,x,y}`

compute_net_present_value(:math:`N_{t,p,x,y}`, :math:`price_t`, :math:`discount\_rate`)

- :math:`V_{x,y}` :math:`\Leftarrow` :math:`\sum _{ t }{ \left( \frac { price_{ t } }{ { (1+discount\_rate) }^{ t } } \cdot N_{t,x,y} \right)}`

Results
^^^^^^^

- :math:`T_{b,x,y}`: Total Carbon Stock (*Megatonnes CO2e per Hectare*)
- :math:`A_{r,x,y}`: Carbon Accumulation (*Megatonnes CO2e per Hectare*)
- :math:`E_{r,x,y}`: Carbon Emissions (*Megatonnes CO2e per Hectare*)
- :math:`N_{r,x,y}`: Net Carbon Sequestration (*Megatonnes CO2e per Hectare*)
- :math:`V_{x,y}`: Net Present Value at Baseline Year (*$ per Hectare*)


Limitations and Simplifications
===============================

In the absence of detailed knowledge on the dynamics of the carbon cycle in coastal and marine systems, we take the simplest accounting approach and draw on published carbon stock datasets from neighboring coastlines.  We use carbon estimates from the most extensive and up-to-date published global datasets of carbon storage and accumulation rates (e.g., Fourqurean et al. 2012 & Silfeet et al. 2011).

 * We assume all storage and accumulation occurs in the biomass and soil pools.
 * We ignore increases in stock and accumulation with growth and aging of habitats.
 * We assume that carbon is stored and accumulated linearly through time between the current and future scenarios.
 * We assume that, after a disturbance event occurs, the disturbed carbon is emitted over time at an exponential decay rate.
 * We assume that some human activities that may degrade coastal ecosystems do not disturb carbon in the sediments.

Data Needs
==========

Biophysical Inputs
------------------

The following are the data needs for the biophysical portion of the InVEST Coastal Blue Carbon model:

 * **Land Use/Land Cover (LULC) maps**: Maps of initial (:math:`t_{1}`) and future (:math:`t_{2}`) LULC (e.g., developed dry land, shrimp aquaculture, mangrove forest, salt marsh, etc).

 * **Years of provided LULC maps**: (:math:`t_{1}`, :math:`t_{2}`, ...), the model uses these years to determine length of time (number of years; (:math:`t_{2}` - :math:`t_{1}`) of the analysis and multiplies this value by the user-specified accumulation rates (Megatonnes of CO\ :sub:`2` e/ha/yr).  If the user is only interested in the standing stock of carbon at :math:`t_{1}`, then this input is optional.

 * **Carbon pool initial values by LULC class**: A collection of values of carbon storage in biomass (Megatonnes of CO\ :sub:`2` e/ha), soil (Megatonnes of CO\ :sub:`2` e/ha), and litter (tonnes of CO\ :sub:`2`/ha) for each LULC class.

 * **Transition matrix**: A table produced by the preprocessor tool that indicates either disturbance or accumulation of carbon based on preprogrammed logic for LULC transitions from :math:`t_{n}` to :math:`t_{n+1}`.  Disturbance values must be modified by the user.

 * **Carbon pool transient values by LULC class**: A collection of values on the accumulation rate (Megatonnes of CO\ :sub:`2` e/ha-yr), percent disturbance and half-lives of carbon emitted over time within the biomass and soil pools of each LULC class.

Economic Inputs
---------------

Users have a choice to model carbon sequestration value using a price schedule, or by supplying a base year carbon price and an annual rate of inflation. In both cases, an appropriate discount rate is necessary.

The value of carbon sequestration over time is given by:

 * **Value of a sequestered ton of carbon**: This user's guide assumes carbon is measured in tons of CO\ :sub:`2`. If you have prices in terms of tons of elemental carbon, these need to be converted to prices per ton of CO\ :sub:`2`. This requires dividing the price by a factor of 3.67 to reflect the difference in the atomic mass between CO\ :sub:`2` and elemental carbon. Again, this value can be input using a price schedule over the appropriate time horizon, or by supplying a base year carbon price and an annual rate of inflation.

 * **Discount rate**: (:math:`d` in the net present value equation), which reflects time preferences for immediate benefits over future benefits. If the rate is set equal to 0% then monetary values are not discounted.


Running the InVEST Model
========================

Step 1. The Preprocessor
------------------------

Inputs
^^^^^^

1. **Workspace Folder**:  The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created.  If datasets already exist in the selected folder, they will be overwritten.

2. **Results Suffix (Optional)**:  This text will be appended to the end of the yield function output folders to help separate outputs from multiple runs.  Please see the `Interpreting Results`_ section for an example folder structure for outputs.

3. **LULC Lookup Table (CSV)**:  A CSV table used to map LULC classes to their values in a raster, as well as to indicate whether or not the LULC class is a coastal blue carbon habitat.

 ==========  =====  ==============================
 lulc-class  code   is_coastal_blue_carbon_habitat
 ==========  =====  ==============================
 <str>       <int>  <bool>
 ...         ...    ...
 ==========  =====  ==============================

4. **LULC Snapshots (Rasters)**:  A set of GDAL-supported rasters representing the land/seascape at particular points in time.  Provided in chronological order.

  +---+---+
  |int|int|
  +---+---+
  |int|int|
  +---+---+


Outputs
^^^^^^^

**Output Folder Structure**

.. code-block:: none

  .
  |-- outputs
      |-- transitions.csv
      |-- carbon_pool_initial_template.csv
      |-- carbon_pool_transient_template.csv

**Outputs**

1. **LULC Transition Effect on Carbon Emissions (CSV)**: This transition matrix indicates whether disturbance or accumulation occurs in a transition from one LULC class to another.  If the cell is left blank, then no transition of that kind occurs between snapshots.  The left-most column represents the source LULC class, and the top row represents the destination LULC class. Depending on the transition type, a cell will be pre-populated with one of the following: (empty), 'NCC' (for no carbon change), 'accum', 'disturb'. It is up to the user to edit the 'disturb' cells with the degree to which distance occurs due to the change.  This is done by changing 'disturb' to either 'low-impact-disturb', 'med-impact-disturb', or 'high-impact-disturb'.

  ==========  =======  =======  ===
  lulc-class  <lulc1>  <lulc2>  ...
  ==========  =======  =======  ===
  <lulc1>     <str>    <str>    ...
  <lulc2>     <str>    <str>    ...
  ...         ...      ...      ...
  ==========  =======  =======  ===

2. **Carbon Pool Initial Variables Table (CSV)**: The user must fill in the 'biomass', 'soil', and 'litter' columns with an amount of carbon initially stored in each pool of a lulc-class in terms of Megatonnes CO\ :sub:`2` e/ hectare. See `Step 2. The Main Model`_ for more information.

  =====  ==========  =======  =======  =======
  code   lulc-class  biomass  soil     litter
  =====  ==========  =======  =======  =======
  <int>  <str>
  ...    ...
  =====  ==========  =======  =======  =======

3. **Carbon Accumulation/Disturbance Transient Variables Table (CSV)**: The user must fill in all columns except the 'lulc-class' and 'pool' columns. See `Step 2. The Main Model`_ for more information.

  ==========  ==========  =================  ==========================  ==========================  ===========================  ===========================  ==============  =======================  =======================  ========================  ========================
  code        lulc-class  biomass-half-life  biomass-low-impact-disturb  biomass-med-impact-disturb  biomass-high-impact-disturb  biomass-yearly-accumulation  soil-half-life  soil-low-impact-disturb  soil-med-impact-disturb  soil-high-impact-disturb  soil-yearly-accumulation
  ==========  ==========  =================  ==========================  ==========================  ===========================  ===========================  ==============  =======================  =======================  ========================  ========================
  <int>       <lulc1>
  <int>       <lulc2>
  ...         ...
  ==========  ==========  =================  ==========================  ==========================  ===========================  ===========================  ==============  =======================  =======================  ========================  ========================


Step 2. The Main Model
----------------------

Inputs
^^^^^^

**Workspace Folder**:  The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created.  If datasets already exist in the selected folder, they will be overwritten.

**Results Suffix (Optional)**:  This text will be appended to the end of the yield function output folders to help separate outputs from multiple runs.  Please see the `Interpreting Results`_ section for an example folder structure of the outputs.

**LULC Lookup Table (CSV)**:  A CSV table used to map LULC classes to their values in a raster and to indicate whether or not the LULC class is a coastal blue carbon habitat.

  ==========  =====  ==============================
  lulc-class  code   is_coastal_blue_carbon_habitat
  ==========  =====  ==============================
  <str>       <int>  <bool>
  ...         ...    ...
  ==========  =====  ==============================

**LULC Snapshots (Rasters)**:  A set of GDAL-supported rasters representing the landscape/seascape at particular points in time.  Provided in chronological order.

**LULC Snapshot Years**: A set of years that respectively correspond to the provided LULC snapshot rasters. Provided in chronological order.

**LULC Transition Effect on Carbon Emissions (CSV)**: Generated by the preprocessor.  This file must be edited before it can be used by the main model.  The left-most column represents the source LULC class, and the top row represents the destination LULC class.

  ==========  =======  =======  ===
  lulc-class  <lulc1>  <lulc2>  ...
  ==========  =======  =======  ===
  <lulc1>     <str>    <str>    ...
  <lulc2>     <str>    <str>    ...
  ...         ...      ...      ...
  ==========  =======  =======  ===

**Carbon Pool Initial Variables Table (CSV)**: The provided CSV table contains information related to the initial conditions of the carbon stock within each of the three pools of a habitat. Biomass includes carbon stored above and below ground.  All non-coastal blue carbon habitat LULC classes are assumed to contain no carbon. The values for 'biomass', 'soil', and 'litter' should be given in terms of Megatonnes CO\ :sub:`2` e/ ha.

  =====  ==========  =======  =======  =======
  code   lulc-class  biomass  soil     litter
  =====  ==========  =======  =======  =======
  <int>  <str>
  ...    ...
  =====  ==========  =======  =======  =======

**Carbon Accumulation/Disturbance Transient Variables Table (CSV)**: The provided CSV table contains information related to the transition of carbon into and out of coastal blue carbon pools.  All non-coastal blue carbon habitat LULC classes are assumed to neither sequester nor emit carbon as a result of change.  The 'yearly-accumulation' values should be given in terms of Megatonnes of CO\ :sub:`2` e/ha-yr.  The 'half-life' values must be given in terms of years.  The 'disturbance' values must be given as a decimal percentage of stock disturbed given a transition occurs away from a particular lulc-class.

  ==========  ==========  =================  ==========================  ==========================  ===========================  ===========================  ==============  =======================  =======================  ========================  ========================
  code        lulc-class  biomass-half-life  biomass-low-impact-disturb  biomass-med-impact-disturb  biomass-high-impact-disturb  biomass-yearly-accumulation  soil-half-life  soil-low-impact-disturb  soil-med-impact-disturb  soil-high-impact-disturb  soil-yearly-accumulation
  ==========  ==========  =================  ==========================  ==========================  ===========================  ===========================  ==============  =======================  =======================  ========================  ========================
  <int>       <lulc1>
  <int>       <lulc2>
  ...         ...
  ==========  ==========  =================  ==========================  ==========================  ===========================  ===========================  ==============  =======================  =======================  ========================  ========================

**Price**:  The price per Megatonne CO\ :sub:`2` e at the base year.

**Interest Rate**:  The interest rate on the price per Megatonne CO\ :sub:`2` e, compounded yearly.

**Price Table (CSV)**:  Can be used in place of price and interest rate inputs.  The provided CSV table contains the price per Megatonne CO\ :sub:`2` e sequestered for a given year, for all years from the original snapshot to the analysis year, if provided.

  ====  =====
  year  price
  ====  =====
  ...   ...
  ====  =====

**Discount Rate**:  The discount rate on future valuations of sequestered carbon, compounded yearly.

Outputs
^^^^^^^

**Output Folder Structure**

.. code-block:: none

  .
  |-- intermediate
  |   |-- aligned_lulc_[year].tif
  |   |-- aligned_transition_[year].tif
  |-- outputs_core
      |-- carbon_stock_at_[year].tif
      |-- carbon_accumulation_between_[year]_and_[year].tif
      |-- carbon_emissions_between_[year]_and_[year].tif
      |-- net_carbon_sequestion_between_[year]_and_[year].tif
      |-- total_net_carbon_sequestration.tif
      |-- net_present_value.tif

**Outputs**

0. **Aligned lulc and transition rasters**
- These rasters are all resampled and aligned to the same bounding box as part
  of the preparations for computing the model.

1. **Carbon Stock Rasters**

- Units: Megatonnes CO\ :sub:`2` e per Hectare 

2. **Carbon Accumulation Rasters**

- Units: Megatonnes CO\ :sub:`2` e per Hectare

3. **Carbon Emissions Rasters**

- Units: Megatonnes CO\ :sub:`2` e per Hectare

4. **Net Carbon Sequestration Rasters**

- Units: Megatonnes CO\ :sub:`2` e per Hectare

5. **Net Present Value Raster**

- Units: (Currency of Provided Price Table) per Hectare

Example Use-Case
================

Freeport, Texas
---------------

Summary
^^^^^^^

Over the next 100 years, the US Gulf coast has been identified as susceptible to rising sea levels.  The use of the InVEST blue carbon model serves to identify potential changes in the standing stock of carbon in coastal vegetation that sequester carbon.  This approach in Freeport, TX was made possible with rich and resolute elevation and LULC datasets.  We used a 10-meter DEM with sub-meter vertical accuracy to model marsh migration and loss over time as a result of sea level rise using Warren Pinnacle's SLAMM (Sea Level Affected Marsh Model).  Outputs from SLAMM serve as inputs to the InVEST Coastal Blue Carbon model which permits the tool to map, measure, and value carbon sequestration and emissions resulting from changes to coastal land cover over a 94-year period.

The Sea Level Affecting Marshes Model (SLAMM: http://www.warrenpinnacle.com/prof/SLAMM/) models changes in the distribution of 27 different coastal wetland habitat types in response to sea-level rise.  The model relies on the relationship between tidal elevation and coastal wetland habitat type, coupled with information on slope, land use, erosion and accretion to predict changes or loss of habitat.  SLAMM outputs future habitat maps for user-defined time steps and sea-level rise scenarios. These future habitat maps can be utilized with InVEST service models to evaluate resultant changes in ecosystem services under various sea-level rise scenarios (e.g. 1 meter SLR by 2100).

For example, SLAMM was used to quantify differences in carbon sequestration over a range of sea-level rise projections in Galveston Bay, Texas, USA.  First, SLAMM was used to map changes in the distribution of coastal wetland habitat over time under different sea-level rise projections.  Then, the InVEST blue carbon model was used to evaluate changes in carbon sequestration associated with predicted changes in habitat type.  The 27 land-cover classes modeled by SLAMM were condensed into a subset relevant to carbon sequestration and converted from ASCII to raster format for use with InVEST.  SLAMM results produced LULC maps of future alternative scenarios over 25-year time slices beginning in 2006 and ending in 2100.  The following figure depicts 2006 LULC and a table of disaggregated land class types.

.. figure:: ./blue_carbon_images/freeport_LULC_2006.png

Figure CS1. Current (2006) LULC map of Freeport, Texas

Carbon stored in the sediment ('soil' pool) was the focus of this analysis.  The vast majority of carbon is sequestered in this pool by coastal and marine vegetation.  See the case study limitations for additional information.  To produce maps of carbon storage at the different 25-year time steps, we used the model to perform a simple "look-up" to determine the amount of carbon per 10-by-10 meter pixel based on known storage rates from sampling in the Freeport area (Chmura et al. 2003).

Next, we provide the InVEST model with a transition matrix in order to identify the amount of carbon gained or lost over each 25-year time step.  Annual accumulation rates in the salt marsh were also obtained from Chmura et al. (2003).  When analyzing the time period from 2025 to 2050, we assume :math:`t_{2}` = 2025 and :math:`t_{3}` = 2050.  We identify all the possible transitions that will result in either accumulation or loss of carbon.  The model compares the two LULC maps (:math:`t_{2}` and :math:`t_{3}`) to identify any pixel transitions from one land cover type to another.  We apply these transformations to the standing stock of carbon which is the running carbon tally at :math:`t_{2}` (2025).  Once these adjustments are complete, we have a new map of standing carbon for :math:`t_{3}` (2050).  We repeat this step for the next time period where :math:`t_{3}` = 2050 and :math:`t_{4}` = 2075.  This process was repeated until 2100.  The model produces spatially explicit depictions of net sequestration over time as well as summaries of net gain/emission of carbon for the two scenarios at each 25-year time step.  This information was used to determine during which time period for each scenario the rising seas and resulting marsh migration led to net emissions for the study site and the entire Freeport area.

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

Table CS1. Carbon sequestration and emissions for each 25-year time period for the two scenarios of the entire Freeport study area.


.. figure:: ./blue_carbon_images/freeport_2006_2010.png

Figure CS2. Carbon emissions (red) and sequestration (blue) from 2006 to 2100 for the two scenarios and a subset of the Freeport study area.

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

Houghton, R. A. (2003). Revised estimates of the annual net flux of carbon to the atmosphere from changes in land use and land management 1850–2000. Tellus B, 55(2), 378-390.

Pendleton, L., Donato, D. C., Murray, B. C., Crooks, S., Jenkins, W. A., Sifleet, S., ... & Baldera, A. (2012). Estimating global “blue carbon” emissions from conversion and degradation of vegetated coastal ecosystems. PLoS One, 7(9), e43542.

Rosenthal, A., Arkema, K., Verutes, G., Bood, N., Cantor, D., Fish, M., Griffin, R., and Panuncio, M. (In press). Identification and valuation of adaptation options in coastal-marine ecosystems: Test case from Placencia, Belize. Washington, DC: InterAmerican Development Bank. Technical Report.

Sifleet, S., Pendleton, L., and B. Murray. (2011). State of the Science on Coastal Blue Carbon. Nicholas Institute Report, 1-43.

United States, Interagency Working Group on Social Costs of Carbon. (2010) "Technical Support Document: Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866." Available at http://www.epa.gov/otaq/climate/regulations/scc-tsd.pdf.

United States, Interagency Working Group on Social Costs of Carbon. (2013) "Technical Update of the Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866." Available at http://www.whitehouse.gov/sites/default/files/omb/inforeg/social_cost_of_carbon_for_ria_2013_update.pdf.

World Bank. (2012). State and Trends of the Carbon Market 2012. Washington DC: The World Bank, 133.
