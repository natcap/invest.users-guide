.. _croppollination:

***************************************
Crop Pollination (Pollinator Abundance)
***************************************

Summary
=======

The InVEST pollination model focuses on wild bees as a key animal pollinator. It uses estimates of the availability of nest sites and floral resources within bee flight ranges to derive an index of the abundance of bees nesting on each cell on a landscape (i.e., pollinator supply). It then uses floral resources, and bee foraging activity and flight range information to estimate an index of the abundance of bees visiting each cell. If desired, the model then calculates a simple index of the contribution of these bees to agricultural production, based on bee abundance and crop dependence on pollination. The results can be used to understand changes in crop pollination and crop yield with changes in land use and agricultural management practices. Required inputs include a land use/land cover (LULC) map, land cover attributes, guilds or species of pollinators present, and their flight ranges. To estimate wild pollinator contributions to crop production requires information on farms of interest, the crops grown there, and the abundance of managed pollinators. The model's limitations include not accounting for pollinator persistence over time or the effects of land parcel size.

Introduction
============

Crop pollination by bees and other animals is a potentially valuable ecosystem service in many landscapes of mixed agricultural and natural habitats (Allen-Wardell et al. 1998, Free 1993). Pollination can increase the yield, quality, and stability of fruit and seed crops as diverse as tomato, canola, watermelon, coffee, sunflower, almond, and cacao. Indeed, Klein et al. (2007) found that 87 of 115 globally important crops benefit from animal pollination, a service valued variously in the billions to tens of billions per year globally (Costanza et al. 1997, Losey and Vaughan 2006, Nabhan and Buchmann 1997, Southwick and Southwick 1992).

Despite these numbers, it is important to realize that not all crops need animal pollination. Some crop plants are wind pollinated (e.g., staple grains such as rice, corn, wheat) or self pollinated (e.g., lentils and other beans), needing no animal pollinators to successfully produce fruits or seeds. Klein et al. (2007) provides a list of crops and their pollination requirements that can help identify whether crops in a region of interest may benefit from wild animal pollinators.

Decision-makers can use information on crop pollinators, their abundance across a landscape, and the pollination services they provide to crops in several ways. First, with maps of pollinator abundance and crops that need them, land use planners could predict consequences of different policies on pollination services and income to farmers (for an example, see Priess et al. 2007). Second, farmers could use these maps to locate crops intelligently, given their pollination requirements and predictions of pollinator availability. Third, conservation organizations or land trusts could use the tool to optimize conservation investments that benefit both biodiversity and farmers. Finally, governments or others proposing payment schemes for ecosystem services could use the results to estimate who should pay whom, and how much.

The Model
=========

A wide range of animals can be important pollinators (e.g., birds, bats, moths and flies), but bees are the most important group for most crops (Free 1993). As a result, the InVEST Pollination model focuses on the resource needs and flight behaviors of wild bees. Many people think of honeybees, managed in artificial hives, when they think of pollinators, but wild bees also contribute to crop pollination. In fact, for several important crops (e.g., blueberries), native species are more efficient and effective pollinators than honeybees (Cane 1997). These native bees, in addition to feral honeybees living in the wild, can benefit crops without active management of captive hives. This is the pollination service associated with habitat conservation.

This model is adapted from Lonsdorf et al. (2009). For bees to persist on a landscape, they need two things: suitable places to nest, and sufficient food (provided by flowers) near their nesting sites. If provided these resources, pollinators are available to fly to nearby crops and pollinate them as they collect nectar and pollen. The model translates land cover into an index of suitability (0-1) for bees to create a pollinator source map. Higher scores indicate sources of greater relative bee abundance. To calculate the index, the model assumes that bees require two types of limiting resources to persist on a landscape - nesting substrates and floral resources. Given an input of land cover that describes the landscape, various suitability values of each LULC class are assigned based on their ability to provide these resources.

The Pollination model then uses the nest supply index to estimate the pollinators visiting crop fields. It assumes the supply from nearby parcels contributes more than those farther away. We use insights from Olsson et al. (2015) and weight bee visitation by the floral quality of the parcel to reflect the central place foraging behavior that bees are known to follow. In other words, the visitation rates to two parcels equally distant from a nest are proportional to the floral qualities of the parcels.

Additionally, this model incorporates the potential use of managed bees into a yield index. With information on the location of crops and their dependence on pollinators, the model uses a simple yield function to project how wild pollinator abundance in agricultural areas and the use of managed bees contributes to an index of crop yields. The inclusion of managed bees reflects guidance from recent work by the USDA-Funded Integrated Crop Pollination Project (icpbees.org) to integrate the combined benefits of managed and wild bees.

These steps are described formally below.

How it Works
------------

The model is an index-based model, and requires the following biophysical data:

* an LULC map;
* a biophysical table paired with the LULC raster to map LULC types to nesting suitability and floral resources across seasons;
* a pollinator guild table with properties about active seasons, nesting preferences, mean flight distances, and relative abundances for each species or group of wild pollinators;
* a farm shapefile indicating the geospatial location of farms, crop type, dependence on pollinators, abundance of managed pollinators, as well as on-farm nesting sites and floral resources.

Because bees are proficient fliers, they integrate over several elements of a landscape, moving between nesting habitats and foraging habitats (Ricketts et al. 2006). The distances they typically fly affect both their persistence and the level of service they deliver to farms. The model therefore requires a typical foraging distance for each pollinator species. These data can be supplied from quantitative field estimates (e.g., Roubik and Aluja 1983), proxies such as body size (Greenleaf et al. 2007), or from expert opinion.

Pollinator Supply and Abundance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using these data, the model first estimates pollinator supply for every cell in the landscape, based on the available nesting sites in that cell, the floral resources (i.e., food) in surrounding cells, and the relative abundance of that pollinator species. Floral resources in cells near nesting sites are given more weight than distant cells, according to the species' average foraging range.

:math:`PS(x,s)` is the pollinator supply index at pixel :math:`x` for species :math:`s` defined as:

.. math:: PS(x,s)=FR(x,s) HN(x,s) sa(s)
	:label: (pol. 1)

where :math:`FR(x,s)` is the accessible floral resources index at pixel :math:`x` for species :math:`s` defined as:

.. math:: FR(x,s)=\frac{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)\sum_{j\in J}RA(l(x'),j)fa(s,j)}{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 2)

:math:`HN(x,s)` is the habitat nesting suitability at pixel :math:`x` for species :math:`s`

.. math:: HN(x,s)=\max_{n\in N}\left[N(l(x),n) ns(s,n)\right]
	:label: (pol. 3)

and where

* :math:`sa(s)` is the relative species abundance index for species :math:`s` in the range :math:`[0.0, 1.0]`, :math:`\sum_{s\in S} sa(s) = 1`, and :math:`S` is the set of all species,
* :math:`N(l,n)` is the nesting substrate index for landcover type :math:`l` for substrate type :math:`n` in the range :math:`[0.0, 1.0]`,
* :math:`l(x)` is the landcover type at pixel :math:`x`,
* :math:`j` is the season,
* :math:`RA(l, j)` index of relative abundance of floral resources on landcover :math:`l` during season :math:`j`,
* :math:`fa(s,j)` is the relative foraging activity for pollinator species :math:`s` during season :math:`j`.
* :math:`D(x,x')` is the Euclidean distance between cells :math:`x` and :math:`x'`,
* :math:`ns(s,n)` is the nesting suitability preference for species :math:`s` in nesting type :math:`n` (and :math:`N` is the set of all nesting types),
* and :math:`\alpha_s` is the expected foraging distance for the pollinator :math:`s` (Greenleaf et al. 2007).

Pollinator supply is an indicator of where pollinators originate from on the landscape. Pollinator abundance indicates where pollinators are active on the landscape. Pollinator abundance depends on the floral resources that attract pollinators to a cell, and the supply of pollinators that can access that cell. The pollinator abundance for species :math:`s` index on cell :math:`x`, during season :math:`j`, :math:`PA(x,s,j)`, is the product of available floral resources on a cell during a given season, weighted by a pollinator's relative activity during that season with the pollinator supply and normalized by the floral resources index in surrounding cells such that:

.. math:: PA(x,s,j)=\left(\frac{RA(l(x),j) fa(s,j)}{FR(x,s)}\right)\frac{\sum_{x'\in X}PS(x',s) \exp(-D(x,x')/\alpha_s)}{\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 4)


See the Table of Variables Appendix for all variable definitions and properties.

On-Farm Abundance and Yield
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, using the indices of pollinator abundance across the landscape, the location of farms, and information about each farm (availability of managed pollinators, crop dependence on pollination), the model can calculate an index of total yield attained and the contribution of wild pollinators to that yield.

First, the model calculates an index of total pollinator abundance by season in agricultural areas that might benefit from pollination services. On-farm pollinator abundance is given as:

.. math:: PAT(x,j)=\sum_{s\in S}PA(x,s,j)
	:label: (pol. 5)

The potential contribution of on-farm pollinator abundance to pollinator-dependent crop yield is calculated using a tunable half-sigmoid function as:

.. math:: FP(x)=\frac{PAT(x,j(f(x)))(1-h(f(x)))}{h(f(x))(1-2PAT(x,j(f(x)))+PAT(x,j(f(x))}
	:label: (pol. 6)

where :math:`h(f(x))` is the half saturation constant for farm :math:`f` at pixel :math:`x` indicating the abundance of wild pollinators needed to reach half of the total potential pollinator-dependent yield.

The actual contribution of wild pollinators to pollinator-dependent yield depends on the degree to which pollination needs are already being met by managed pollinators. The total pollinator-dependent yield, from both wild and managed pollinators, is given as:

.. math:: PYT(x)=\min(mp(f(x))+FP(x),1)
	:label: (pol. 7)

assuming a value of 0 indicates 0% of pollinator-dependent yield is achieved, and 1.0 indicates 100% of pollinator-dependent yield is achieved. Note the max/min notation constrains the value of :math:`PYT` to 0..1 where :math:`mp(f(x))` is the proportion of pollination needs met by managed pollinators available at pixel :math:`x` within farm polygon :math:`f`.

The proportion of pollinator-dependent yield attributable to wild pollinators is given as

.. math:: PYW(x)=\max(0, PYT(x)-mp(f(x)))
	:label: (pol. 8)

Thus, in cases where managed pollinators are sufficiently abundant, i.e, :math:`mp(f(x))=1`, there is no additional yield attributable to wild pollinators.

Total crop yield attained is a function of the crop's dependence on pollination and the degree to which its pollination needs are met. Some crop species are self-compatible or wind-pollinated and yield is less dependent on animal pollinators while other species obligately require pollinators to generate any yield (Klein et al. 2007). Total crop yield is calculated per farm as

.. math:: YT(f)=1-\nu(f)\left(1-\sum_{x\in X(f)}PYT(x)/|X(f)|\right)
	:label: (pol. 9)

where :math:`f` is a particular farm, :math:`X(f)` are the set of pixels covering farm :math:`f`, and :math:`|X(f)|` is the count of pixels covered by farm :math:`f`. The function :math:`\nu(f)` is a scalar :math:`\in [0,1]` representing what proportion of yield for the crop grown on farm :math:`f` is dependent on pollinators.

The proportion of total crop yield attributable to wild pollinators is given as

.. math:: YW(f)=\nu(f)\left(\sum_{x\in X(f)}PYW(x)/|X(f)|\right)
	:label: (pol. 10)

Limitations and Simplifications
-------------------------------

This model is an index-based model and only estimates relative patterns of pollinator abundance and pollination contribution to crop yields. This is because absolute estimates of nest density, resource availability, and pollinator abundance are rarely available, and yield functions (including pollinator abundance) for many crops are poorly defined. Relying on relative indices limits our ability to estimate absolute economic values to better inform land-use planning decision-making, often based on cost-benefit analyses.

The use of central place foraging in the model's pollinator abundance index has yet to be tested empirically, so we caution against using the model to make economic projections without empirical verification. The same applies to the integration of managed bees in the yield function.

As an index-based model, it is well-suited for making qualitative comparisons among scenarios representing marginal changes in LULC, farm management practices or crop types. On-farm pollinator abundance :math:`PAF(x,j)` will be affected by the number of pollinator guilds being modeled and so cannot be used to compare different pollinator communities even on the same landscape. Similarly, because relative species abundance indices :math:`sa(s)` are specified as an input, the model will not yield accurate results for scenarios in which a rare species becomes common or vice versa due to large changes in nesting habitat or floral resource availability.

The model does not include the dynamics of bee populations over time, and therefore cannot evaluate whether these populations are sustainable given the current landscape. Instead, the model simply provides a static snapshot of the number of pollinators on each cell in the landscape, given simple estimates of nesting sites and food resources. Some of the factors that influence bee populations, like habitat disturbances and typical population fluctuations, are not captured. In addition, the model calculates pollinator supply based on the average of available floral resources weighted by pollinator activity across seasons during which the pollinator is active. It does not account for the order of seasons or the dependence of pollinator abundance in one season on the resources available in the season directly prior. The model does not account for variation in the effectiveness of different pollinator species or guilds at pollinating different crop types. All species are assumed to contribute equally based on their relative abundance and the half-saturation constant specified for each farm/crop.

The model does not account for the sizes of habitat patches in estimating abundance. For many species, there is a minimum patch size, under which a patch cannot support that species over the long term. There is some evidence that small patches support fewer species of bees (Kremen et al. 2004), but bees can also survive in small areas of suitable habitat (Ricketts 2004).

Pollinators are likely to be influenced by fine-scale features in the landscape, which are difficult to capture in typical land-cover data with typical resolutions of 30m. For example, small patches of flower resources in an otherwise hostile habitat for bees can provide important food resources, but will not be detected by typical land cover maps. Some bees are also able to nest in small but suitable areas (a single suitable roadside or tree hollow). Using average values of nesting site or flower availability for each LULC class, along with 30m pixels or larger, will therefore not capture these fine scale but important areas of resources.

Data Needs
==========

- :investspec:`pollination workspace_dir`

- :investspec:`pollination results_suffix`

- :investspec:`pollination landcover_raster_path` Used to map biophysical properties about habitat and floral resources of landcover types to a spatial layout. This must be of fine enough resolution to capture the movements of bees on a landscape. If bees fly 800 meters on average and cells are 1000 meters across, the model will not fully capture the movement of bees from their nesting sites to neighboring farms.

- :investspec:`pollination landcover_biophysical_table_path` Data can be summarized from field surveys, or obtained by expert assessment if field data is unavailable.

	Columns:

	- :investspec:`pollination landcover_biophysical_table_path.columns.lucode`

	- :investspec:`pollination landcover_biophysical_table_path.columns.nesting_[SUBSTRATE]_availability_index`

	- :investspec:`pollination landcover_biophysical_table_path.columns.floral_resources_[SEASON]_index` For example, an LULC class comprised 100% of a mass flowering crop that flowers the entire season with an abundance cover of 80% would be given a suitability value of 0.80. An LULC class that flowers only half of the season at 80% floral coverage would be given a floral suitability value of 0.40. The *SEASON* name must exactly match a season given in the Guild Table.


    **Example Biophysical Table:**

    .. csv-table::
       :file: ../invest-sample-data/pollination/landcover_biophysical_table_modified.csv
       :header-rows: 1
       :widths: auto

- :investspec:`pollination guild_table_path` 'Guild' refers to a group of bee species that show the same nesting behavior, whether preferring to build nests in the ground, in tree cavities, or other habitat features. If multiple species are known to be important pollinators, and if they differ in terms of flight season, nesting requirements, or flight distance, provide data on each separately. If little or no data are available, create a single 'proto-pollinator' with data taken from average values or expert opinion about the whole pollinator community. Each row is a unique species or guild of pollinator and columns must be named and defined as follows:

	Columns:

	- :investspec:`pollination guild_table_path.columns.species`
	- :investspec:`pollination guild_table_path.columns.nesting_suitability_[SUBSTRATE]_index` Substrates are user defined, but might include ground nests, tree cavities, etc.
	- :investspec:`pollination guild_table_path.columns.foraging_activity_[SEASON]_index` Seasons are user defined but might include spring, summer, fall; wet, dry, etc.
	- :investspec:`pollination guild_table_path.columns.alpha` The model uses this estimated distance to define the neighborhood of available flowers around a given cell, and to weight the sums of floral resources and pollinator abundances on farms. This value can be determined by typical foraging distance of a bee species based on an allometric relationship (see Greenleaf et al. 2007).
	- :investspec:`pollination guild_table_path.columns.relative_abundance` Setting this value to the same value for each species will result in each species being weighted equally.

   *Example:* A hypothetical Guild Table with two species. There are two main SUBSTRATEs, "cavity" and "ground." Species "Apis" uses both cavity and ground nesting types, and species "Bombus" only uses cavity nests. There are two SEASONs, "spring" and "summer". Typical flight distances, specified in meters (alpha), vary widely between species. The relative_abundance of Bombus is higher than Apis, indicating that there are more Bombus pollinators than Apis.

   **Example Guild Table:**

   .. csv-table::
      :file: ../invest-sample-data/pollination/guild_table.csv
      :header-rows: 1
      :widths: auto

- :investspec:`pollination farm_vector_path`

    .. note::
       The optional farms vector will overwrite seasonal floral resource values and nesting substrate suitability values in any areas that overlap the LULC raster.

    Fields:

    - :investspec:`pollination farm_vector_path.fields.crop_type` For farms growing multiple overlapping crops, or crops in multiple seasons, a separate overlapping polygon must be included for each crop.
    - :investspec:`pollination farm_vector_path.fields.half_sat` This is a tunable parameter that may be most useful to adjust following an initial run of the model and an examination of the results. This is :math:`h` in equation :eq:`(pol. 6)`.
    - :investspec:`pollination farm_vector_path.fields.season`
    - :investspec:`pollination farm_vector_path.fields.fr_[SEASON]`
    - :investspec:`pollination farm_vector_path.fields.n_[SUBSTRATE]`
    - :investspec:`pollination farm_vector_path.fields.p_dep` See Klein et al. (2007) for estimates for common crfarm_vector_path
    - :investspec:`pollination farm_vector_path.fields.p_managed` This can be estimated as the proportion of the recommended hive density or stocking rate. See Delaplane & Mayer (2000) for recommended stocking rates in the United States. Agricultural extension offices are also a good source of this information.

.. _interpreting-results:

Interpreting Results
====================

Final Results
-------------

* **Parameter log**: Each time the model is run, a text (.txt) file will be created in the Workspace. The file will list the parameter values and output messages for that run and will be named according to the service, the date and time. When contacting NatCap about errors in a model run, please include the parameter log.

* **farm_results_[Suffix].shp**: (Only generated if a farm vector is provided) A copy of the input farm polygon vector file with the following additional fields:

  * *p_abund*: average pollinator abundance on the farm for the active season
  * *y_tot*: total yield index, including wild and managed pollinators and pollinator independent yield.
  * *pdep_y_w*: index of potential pollination dependent yield attributable to wild pollinators.
  * *y_wild*: index of the total yield attributable to wild pollinators.
  
* **farm_pollinators_[Suffix].tif**: (Only generated if a farm vector is provided) Per-pixel total pollinator abundance across all species per season, clipped to the geometry of the farm vector's polygons.

* **pollinator_abundance_[SPECIES]_[SEASON]_[Suffix].tif**: Per-pixel abundance of pollinator SPECIES in season SEASON.

* **pollinator_supply_[SPECIES]_[Suffix].tif**: Per-pixel index of pollinator SPECIES that could be on a pixel given its arbitrary abundance factor from the table, multiplied by the habitat suitability for that species at that pixel, multiplied by the available floral resources that a pollinator could fly to from that pixel. (Eqn. 1)

* **total_pollinator_abundance_[SEASON]_[Suffix].tif**: (Only generated if a farm vector is provided) Per-pixel total pollinator abundance across all species per season.

* **total_pollinator_yield_[Suffix].tif**: (Only generated if a farm vector is provided) Per-pixel total pollinator yield index for pixels that overlap farms, including wild and managed pollinators.

* **wild_pollinator_yield_[Suffix].tif**: (Only generated if a farm vector is provided) Per-pixel pollinator yield index for pixels that overlap farms, for wild-pollinators only.

Intermediate Results
^^^^^^^^^^^^^^^^^^^^

You may also want to examine the intermediate results. These files can help determine the reasons for the patterns in the final results, and can also be used to better understand the model, and troubleshoot. They are found in the *intermediate_outputs* folder within the Workspace directory defined for the model run, and most of them have file names that give a good idea of what the layer represents.

Appendix: Table of Variables
============================

* :math:`x` - a pixel coordinate.
* :math:`X` - set of all pixels in the landcover map.
* :math:`f(x)` - farm at pixel x.
* :math:`F` - set of all pixels that are located in farms.
* :math:`s` - bee species.
* :math:`n` - nesting type (ground, cavity).
* :math:`N` - set of all nesting types.
* :math:`j` - season (fall, spring, etc).
* :math:`J` - set of all seasons (ex: {fall, spring}).
* :math:`fj(f, x)` - active pollination season for farm :math:`f` at pixel :math:`x`.
* :math:`\alpha_s` - mean foraging distance for species s.
* :math:`ns(s,n)` - nesting suitability preference for species :math:`s` in nesting type :math:`n`.
* :math:`HN(x,s)` - habitat nesting suitability at pixel :math:`x` for species :math:`s` [0.0, 1.0].
* :math:`N(l,n)` - the nesting substrate index for landcover type :math:`l` for substrate type :math:`n` in the range :math:`[0.0, 1.0]`.
* :math:`RA(l,j)` - index of relative abundance of floral resources on landcover type :math:`l` during season :math:`j`. :math:`[0.0, 1.0]`
* :math:`fa(s,j)` - relative foraging activity for species :math:`s` during season :math:`j`.
* :math:`FR(x,s)` - accessible floral resources index at pixel :math:`x` for species :math:`s`.
* :math:`D(x,x')` - euclidean distance between the centroid of pixel :math:`x` and :math:`x'`.
* :math:`PS(x,s)` - pollinator supply index at pixel :math:`x` for species :math:`s`.
* :math:`PA(x,s,j)` - pollinator abundance at pixel :math:`s` for species :math:`s`.
* :math:`PAT(x,j)` - total on-farm pollinator abundance at pixel :math:`x` in season :math:`j`, accounting for all species
* :math:`FP(x)` - the potential contribution of on-farm pollinator abundance to pollinator-dependent crop yield at a farm pixel during the season in which pollination is needed for that farm.
* :math:`mp(f)` - abundance of managed pollinators on farm :math:`f` relative to the recommended stocking rate.
* :math:`h(f)` - half saturation coefficient for farm :math:`f`.
* :math:`PYT(x)` - total pollinator-attributable yield at pixel x for season :math:`j`, accounting for wild and managed pollinators.
* :math:`PYW(x)` - wild-pollinator-attributable yield at pixel x for season :math:`j`.
* :math:`sa(s)` - relative species abundance index for species :math:`s`.
* :math:`YT(f)` - average farm yield for farm parcel :math:`f` accounting for pollinator dependency of crop.
* :math:`YW(f)` - proportion of average farm yield for farm parcel :math:`f` attributable to wild pollinators, accounting for pollinator dependency of crop.
* :math:`\nu(f)` - proportion of crop yield dependent on pollination.

Appendix: Data Sources
======================

.. note:: The sample data is only meant to illustrate the data structure and should not be used as a data source.

Crop Dependence on Pollinators
------------------------------
See Klein et al. 2007 for a list of globally important crops and their dependence on animal pollinators.

Nesting Suitability and Floral Resource Availability
----------------------------------------------------
Koh et al. 2016 contains nesting suitability and floral resource availability data for 45 land use categories.

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

References
==========

Allen-Wardell, G., P. Bernhardt, R. Bitner, A. Burquez, S. Buchmann, J. Cane, PA Cox, V. Dalton, P. Feinsinger, M. Ingram, D. Inouye, CE Jones, K. Kennedy, P. Kevan, and H. Koopowitz. 1998. The potential consequences of pollinator declines on the conservation of biodiversity and stability of food crop yields. Conservation Biology 12: 8-17.

Cane, JH. 1997. Lifetime monetary value of individual pollinators: the bee habropoda laboriosa at rabbiteye blueberry (vaccinium ashei reade). Acta Horticulturae 446: 67-70.

Costanza, R., R. d'Arge, R. de Groot, S. Farber, M. Grasso, B. Hannon, K. Limburg, S. Naeem, RV O'Neill, J. Paruelo, RG Raskin, P. Sutton, and M. van den Belt. 1997. The value of the world's ecosystem services and natural capital. Nature 387: 253-260.

Delaplane, KS, and DF Mayer. 2000. Crop pollination by bees. CABI Publishing, New York.

Free, JB. 1993. Insect pollination of crops. Academic Press, London.

Greenleaf, SS, NM Williams, R. Winfree, and C. Kremen. 2007. Bee foraging ranges and their relationship to body size. Oecologia 153: 589-596.

Greenleaf, SS, and C. Kremen. 2006. Wild bee species increase tomato production and respond differently to surrounding land use in Northern California. Biological Conservation 133:81-87.

Klein, AM, BE Vaissiere, JH Cane, I. Steffan-Dewenter, SA Cunningham, C. Kremen, and T. Tscharntke. 2007. Importance of pollinators in changing landscapes for world crops. Proceedings of the Royal Society B-Biological Sciences 274: 303-313.

Koh, I., E. Lonsdorf, N. Williams, C. Brittain, R. Isaacs, J. Gibbs, and T. Ricketts. 2016. Modeling the status, trends, and impacts of wild bee abundance in the United States. Proceedings of the National Academy of Sciences 113 (1) 140-145; DOI: 10.1073/pnas.1517685113

Kremen, C., NM Williams, RL Bugg, JP Fay, and RW Thorp. 2004. The area requirements of an ecosystem service: crop pollination by native bee communities in California. Ecology Letters 7: 1109-1119.

Lonsdorf, E., C. Kremen, T. Ricketts, R. Winfree, N. Williams, and SS Greenleaf. 2009. Modelling pollination services across agricultural landscapes. Annals of Botany 1: 12. online [https://pubmed.ncbi.nlm.nih.gov/19324897/]

Lonsdorf, E., TH Ricketts, CM Kremen, NM Williams, and S. Greenleaf. in press. Pollination services in P. Kareiva, TH Ricketts, GC Daily, H. Tallis, and S. Polasky, eds. The theory and practice of ecosystem service valuation.

Losey, JE, and M. Vaughan. 2006. The economic value of ecological services provided by insects. Bioscience 56: 311-323.

Nabhan, GP, and SL Buchmann. 1997. Services provided by pollinators. Pages 133-150 in GC Daily, ed. Nature's services. Island Press, Washington, D.C.

Olsson, O. A. Bolin, H. Smith, and E. Lonsdorf. 2015. Modeling pollinating bee visitation rates in heterogeneous landscapes from foraging theory. Ecological Modelling 316: 133-143.

Priess, JA, M. Mimler, AM Klein, S. Schwarze, T. Tscharntke, and I. Steffan-Dewenter. 2007. Linking deforestation scenarios to pollination services and economic returns in coffee agroforestry systems. Ecological Applications 17: 407-417.

Ricketts, TH. 2004. Tropical forest fragments enhance pollinator activity in nearby coffee crops. Conservation Biology 18: 1262-1271.

Ricketts, TH, NM Williams, and MM Mayfield. 2006. Connectivity and ecosystem services: crop pollination in agricultural landscapes. Pages 255-289 in M. Sanjayan and K. Crooks, eds. Connectivity for Conservation. Cambridge University Press, Cambridge, UK.

Roubik, DW, and M. Aluja. 1983. Flight ranges of Melipona and Trigona in tropical forest. Journal of the Kansas Entomological Society 56: 217-222.

Southwick, EE, and L. Southwick. 1992. Estimating the economic value of honey-bees (Hymenoptera; Apidae) as agricultural pollinators in the United States. Journal of Economic Entomology 85: 621-633.

Winfree, R., J. Dushoff, EE Crone, CB Schultz, RV Budny, NM Williams, and C. Kremen. 2005. Testing simple indices of habitat proximity. American Naturalist 165(6): 707-717.
