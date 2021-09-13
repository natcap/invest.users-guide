.. _habitat_quality:

***************
Habitat Quality
***************

Summary
=======

Biodiversity is intimately linked to the production of ecosystem services. Patterns in biodiversity are inherently spatial, and as such, can be estimated by analyzing maps of land use and land cover (LULC) in conjunction with threats to species' habitat. InVEST models habitat quality and rarity as proxies for biodiversity, ultimately estimating the extent of habitat and vegetation types across a landscape, and their state of degradation. Habitat quality and rarity are a function of four factors: each threat's relative impact, the relative sensitivity of each habitat type to each threat, the distance between habitats and sources of threats, and the degree to which the land is legally protected. The model assumes that the legal protection of land is effective and that all threats to a landscape are additive.

Introduction
============

A primary goal of conservation is the protection of biodiversity, including the range of genes, species, populations, habitats, and ecosystems in an area of interest. While some consider biodiversity to be an ecosystem service, here we treat it as an independent attribute of natural systems, with its own intrinsic value (we do not monetize biodiversity in this model). Natural resource managers, corporations and conservation organizations are becoming increasingly interested in understanding how and where biodiversity and ecosystem services align in space and how management actions affect both.

Evidence from many sources builds an overwhelming picture of pervasive biodiversity decline worldwide (e.g., Vitousek et al. 1997; Wilcove et al 1998; Czech et. al 2000). This evidence has prompted a wide-ranging response from both governments and civil society. Through the Rio Convention on Biodiversity, 189 nations have committed themselves to preserving the biodiversity within their borders. Yet, there is scant research on the overlap between opportunities to protect biodiversity and to sustain the ecosystem services so critical to these countries' economic well-being. This is precisely the type of challenge that InVEST has been designed to address.

For managers to understand the patterns of distribution and richness across a landscape, individually and in aggregate, it is necessary to map the range or occurrences of elements (e.g. species, communities, habitats). The degree to which current land use and management affects the persistence of these elements must also be assessed in order to design appropriate conservation strategies and encourage resource management that maximizes biodiversity in those areas.

There are a variety of approaches to identifying priorities for conservation with various trade-offs among them. Each of these approaches focuses on different facets of biodiversity attributes and dynamics, including habitat or vegetation-based representation (i.e., a coarse filter), maximizing the number of species "covered" by a network of conserved sites for a given conservation budget (Ando et al. 1998), identifying patterns of richness and endemism (Conservation International hotspots), and conserving ecological processes. There is also a hybrid coarse-fine filter approach which selectively includes "fine-filter" elements such as species with unique habitat requirements who may not be adequately protected using a coarse-filter approach only (The Nature Conservancy and World Wildlife Fund ecoregional planning). The InVEST Habitat Quality model is most relevant to "coarse filter", or habitat-based approaches.

The reasons for modeling biodiversity alongside ecosystem services are simple and powerful. Doing so allows us to compare spatial patterns of biodiversity and ecosystem services, and to identify win-win areas (i.e., areas where conservation can benefit both natural systems and human economies) as well as areas where these goals are not aligned. Further, it allows us to analyze trade-offs between biodiversity and ecosystem services across differing scenarios of future land use change. Land use/land cover (LULC) patterns that generate greater ecosystem service production may not always lead to greater biodiversity conservation (Nelson et al. 2008), and modeling future options today can help identify and avoid tradeoffs.


The Model
=========

The InVEST Habitat Quality model combines information on LULC and threats to biodiversity to produce habitat quality maps. This approach generates two key sets of information that are useful in making an initial assessment of conservation needs: the relative extent and degradation of different types of habitat types in a region, and changes across time. This approach further allows rapid assessment of the status of and change in habitat as a proxy for more detailed measures of biodiversity status. If habitat changes are taken as representative of genetic, species, or ecosystem changes, the user is assuming that areas with high quality habitat will better support all levels of biodiversity and that decreases in habitat extent and quality over time means a decline in biodiversity persistence, resilience, breadth and depth in the area of decline.

The habitat rarity portion of the model indicates the extent and pattern of natural land cover types on the current or a potential future landscape vis-a-vis the extent of the same natural land cover types in some baseline period. Rarity maps allow users to create a map of the rarest habitats on the landscape relative to the baseline chosen by the user to represent the mix of habitats on the landscape that is most appropriate for the study area's native biodiversity.

The model requires basic data that are available virtually everywhere in the world, making it useful in areas for which species distribution data are poor or lacking altogether. Extensive occurrence (presence/absence) data may be available in many places for current conditions. However, modeling the change in occurrence, persistence, or vulnerability of multiple species under future conditions is often impossible or infeasible. While a habitat approach leaves out the detailed species occurrence data available for current conditions, several of its components represent 
es in functionality over many existing biodiversity conservation planning tools. The most significant is the ability to characterize the sensitivity of habitat types to various threats. Not all habitats are affected by all threats in the same way, and the InVEST model accounts for this variability. Further, the model allows users to estimate the relative impact of one threat over another so that threats that are more damaging to biodiversity persistence on the landscape can be represented as such. For example, grassland could be particularly sensitive to threats generated by urban areas yet moderately sensitive to threats generated by roads. In addition, the distance over which a threat will degrade natural systems is incorporated into the model.

Model assessment of the current landscape can be used as an input to a coarse-filter assessment of current conservation needs and opportunities. Model assessment of potential LULC futures can be used to measure potential changes in habitat extent, quality, and rarity on a landscape and conservation needs and opportunities in the future.

How it Works
------------

Habitat Quality
^^^^^^^^^^^^^^^

We define habitat as "the resources and conditions present in an area that produce occupancy -- including survival and reproduction -- by a given organism" (Hall et al. 1997:175). Habitat quality refers to the ability of the ecosystem to provide conditions appropriate for individual and population persistence, and is considered a continuous variable in the model, ranging from low to medium to high, based on resources available for survival, reproduction, and population persistence, respectively (Hall et al 1997). Habitat with high quality is relatively intact and has the structure and function within the range of historic variability. Habitat quality depends on a habitat's proximity to human land uses and the intensity of these land uses. Generally, habitat quality is degraded as the intensity of nearby land-use increases (Nelleman 2001, McKinney 2002, Forman et al. 2003).

The model runs using raster data, where each cell in the raster is assigned an LULC class, which can be a natural (unmanaged) class or a managed class. LULC types can be given at any level of classification detail. For example, grassland is a broad LULC definition that can be subdivided into pasture, restored prairie, and residential lawn types to provide much more habitat classification detail. While the user can submit up to 3 raster maps of LULC, one each for a baseline, current, and future period, at a minimum the current LULC raster map must be provided.

The user defines which LULC types can provide habitat for the conservation objective (e.g., if forest breeding birds are the conservation objective then forests are habitat and non-forest covers are not habitat). Let :math:`H_j` indicate the habitat suitability of LULC type :math:`j`.

Which LULC types should be considered habitat? If considering biodiversity generally or if data on specific biodiversity-habitat relationships are lacking, you can take a simple binary approach to assigning habitat to LULC types. A classic example would be to follow an island-ocean model and assume that the managed land matrix surrounding remnant patches of unmanaged land is unusable from the standpoint of species (e.g., MacArthur and Wilson 1967). In this case a 0 would be assigned to managed LULC types in the matrix (i.e., non-habitat) and a 1 to unmanaged types (i.e., habitat). Under this modeling scheme habitat quality scores are not a function of habitat importance, rarity, or suitability; all habitat types are treated equally. Model inputs are assumed to not be specific to any particular species or species guild, but rather apply to biodiversity generally.

More recent research suggests that the matrix of managed land that surrounds patches of unmanaged land can significantly influence the "effective isolation" of habitat patches, rendering them more or less isolated than simple distance or classic models would indicate (Ricketts 2001, Prugh et al. 2008). Modification of the matrix may provide opportunities for reducing patch isolation and thus the extinction risk of populations in fragmented landscapes (Franklin and Lindenmayer 2009). To model this, a relative habitat suitability score can be assigned to an LULC type ranging from 0 to 1 where 1 indicates the highest habitat suitability. A ranking of less than 1 indicates habitat where a species or functional group may have lower survivability. Applying this second approach greatly expands the definition of habitat from the simple and often artificial binary approach (e.g., "natural" versus "unnatural") to include a broad spectrum of both managed and unmanaged LULC types. By using a continuum of habitat suitability across LULC types, the user can assess the importance of land use management on habitat quality holistically or consider the potential importance of "working" (or managed) landscapes.

If a continuum of habitat suitability is relevant, weights with a roster of LULC on a landscape must be applied in reference to a particular species guild of group. For example, grassland songbirds may prefer a native prairie habitat above all other habitat types (the habitat score for the LULC prairie (:math:`H_{prarie}` equals 1), but will also make use of a managed hayfield or pasture if prairie is not available (the habitat score for the LULC hayfield (:math:`H_{hayfield}`) and pasture (:math:`H_{pasture}`) equals 0.5). However, mammals such as porcupines will find prairie unsuitable for breeding and feeding. Therefore, if specific data on species group-habitat relationships are used, the model output refers to habitat extent and quality for the species or group in the modeled set only.

Besides a map of LULC and data that relates LULC to habitat suitability, the model also requires data on habitat threat density and its effects on habitat quality. In general, we consider threats to be human-modified LULC types that cause habitat fragmentation, edge, and degradation in neighboring habitat. For example, the conversion of a habitat LULC to non-habitat LULC reduces the size and continuity of neighboring habitat patches. Edge effects refer to changes in the biological and physical conditions that occur at a patch boundary and within adjacent patches. For example, adjacent degraded non-habitat LULC parcels impose "edge effects" on habitat parcels and can have negative impacts within habitat parcels by, for example, facilitating entry of predators, competitors, invasive species, or toxic chemicals and other pollutants. Another example: in many developing countries roads are a threat to forest habitat quality on the landscape because of the access they provide to timber and non-timber forest harvesters.

Each threat source needs to be mapped on a raster grid. A grid cell value on a threat's map can either indicate intensity of the threat within the cell (e.g., road length in a grid cell or cultivated area in a gird cell) or simply a 1 if the grid cell contains the threat in a road or crop field cover and 0 otherwise. Let :math:`o_{ry}` indicate threat :math:`r`'s "score" in grid cell :math:`y` where :math:`r` = 1, 2, ..., :math:`R` indexes all modeled degradation sources.

All mapped threats should be measured in the same scale and metric. For example, if one threat is measured in density per grid cell then all degradation sources should be measured in density per grid cell where density is measured with the same metric unit (e.g., km and km\ :sup:`2`\). Or if one threat is measured with presence/absence (1/0) on its map then all threats should be mapped with the presence/absence scale.

The impact of threats on habitat in a grid cell is mediated by four factors.

1. The first factor is **the relative impact of each threat**. Some threats may be more damaging to habitat, all else equal, and a relative impact score accounts for this (see Table 1 for a list of possible threats). For instance, urban areas may be considered to be twice as degrading to any nearby habitats as agricultural areas. A degradation source's weight, :math:`w_r`, indicates the relative destructiveness of a degradation source to all habitats. The weight :math:`w_r` can take on any value from 0 to 1. For example, if urban area has a threat weight of 1 and the threat weight of roads is set equal to 0.5 then the urban area causes twice the disturbance, all else equal, to all habitat types. To reiterate, if we have assigned species group-specific habitat suitability scores to each LULC then the threats and their weights should be specific to the modeled species group.

2. The second mitigating factor is **the distance between habitat and the threat source and the impact of the threat across space**. In general, the impact of a threat on habitat decreases as distance from the degradation source increases, so that grid cells that are more proximate to threats will experience higher impacts. For example, assume a grid cell is 2 km from the edge of an urban area and 0.5 km from a highway. The impact of these two threat sources on habitat in the grid cell will partly depend on how quickly they decrease, or decay, over space. The user can choose either a linear or exponential distance-decay function to describe how a threat decays over space. The impact of threat :math:`r` that originates in grid cell :math:`y`, :math:`r_y`, on habitat in grid cell :math:`x` is given by :math:`i_{rxy}` and is represented by the following equations:

.. math:: i_{rxy}=1-\left( \frac{d_{xy}}{d_{r\ \mathrm{max}}}\right)\ \mathrm{if\ linear}
	:label: (hq. 1)
	
.. math:: i_{rxy}=exp\left(-\left(\frac{2.99}{d_{r\ \mathrm{max}}}\right)d_{xy}\right)\mathrm{if\ exponential}
	:label: (hq. 2)


	
where :math:`d_{xy}` is the linear distance between grid cells :math:`x` and :math:`y` and :math:`d_{r\ \mathrm{max}}` is the maximum effective distance of threat :math:`r`'s reach across space. Figure 1 illustrates the relationship between the distance-decay rate for a threat based on the maximum effective distance of the threat (linear and exponential). For example, if the user selects an exponential decline and the maximum impact distance of a threat is set at 1 km, the impact of the threat on a grid cell's habitat will decline by ~ 50% when the grid cell is 200 m from :math:`r`'s source. If :math:`i_{rxy} > 0` then grid cell :math:`x` is in degradation source :math:`ry`'s disturbance zone. (If the exponential function is used to describe the impact of degradation source :math:`r` on the landscape then the model ignores values of :math:`i_{rxy}` that are very close to 0 in order to expedite the modeling process.) To reiterate, if we have assigned species group-specific habitat suitability scores to each LULC then threat impact over space should be specific to the modeled species group.

|

.. figure:: ./habitat_quality/graph.png
   :align: center
   :figwidth: 500px

Figure 1. An example of the relationship between the distance-decay rate of a threat and the maximum effective distance of a threat.

|

3. The third landscape factor that may mitigate the impact of threats on habitat is **the level of legal / institutional / social / physical protection from disturbance in each cell**. Is the grid cell in a formal protected area? Or is it inaccessible to people due to high elevations? Or is the grid cell open to harvest and other forms of disturbance? The model assumes that the more legal / institutional / social / physical protection from degradation a cell has, the less it will be affected by nearby threats, no matter the type of threat. Let :math:`\beta_x \in [0,1]` indicate the level of accessibility in grid cell :math:`x` where 1 indicates complete accessibility. As accessibility decreases the impact that all threats will have in grid cell :math:`x` decreases linearly. It is important to note that while legal / institutional / social / physical protections often do diminish the impact of extractive activities in habitat such as hunting or fishing, it is unlikely to protect against other sources of degradation such as air or water pollution, habitat fragmentation, or edge effects. If the threats considered are not mitigated by legal / institutional / social / physical properties then you should ignore this input or set :math:`\beta_x = 1` for all grid cells :math:`x`. To reiterate, if we have assigned species group-specific habitat suitability scores to each LULC then the threats mitigation weights should be specific to the modeled species group.


4. The **relative sensitivity of each habitat type to each threat on the landscape** is the final factor used when generating the total degradation in a cell with habitat. (In Kareiva et al. (2010), habitat sensitivity is referred to by its inverse, "resistance".) Let :math:`S_{jr} \in [0,1]` indicate the sensitivity of LULC (habitat type) :math:`j` to threat :math:`r` where values closer to 1 indicate greater sensitivity. The model assumes that the more sensitive a habitat type is to a threat, the more degraded the habitat type will be by that threat. A habitat's sensitivity to threats should be based on general principles from landscape ecology for conserving biodiversity (e.g., Forman 1995; Noss 1997; Lindenmayer et al 2008). To reiterate, if we have assigned species group-specific habitat suitability scores to each LULC then habitat sensitivity to threats should be specific to the modeled species group.

Therefore, the total threat level in grid cell :math:`x` with LULC or habitat type :math:`j` is given by :math:`D_{xj}`,

.. math:: D_{xj}=\sum^R_{r=1}\sum^{Y_r}_{y=1}\left(\frac{w_r}{\sum^R_{r=1}w_r}\right)r_y i_{rxy} \beta_x S_{jr}
   :label: (hq. 3)


where :math:`y` indexes all grid cells on :math:`r`'s raster map and :math:`Y_r` indicates the set of grid cells on :math:`r`'s raster map. Note that each threat map can have a unique number of grid cells due to variation in raster resolution. If :math:`S_{jr} = 0` then :math:`D_{xj}` is not a function of threat :math:`r`. Also note that threat weights are normalized so that the sum across all threats weights equals 1.

By normalizing weights such that they sum to 1 we can think of :math:`D_{xj}` as the weighted average of all threat levels in grid cell :math:`x`. The map of :math:`D_{xj}` will change as the set of weights we use change. Please note that two sets of weights will only differ if the relative differences between the weights in each set differ. For example, set of weights of 0.1, 0.1, and 0.4 are the same as the set of weights 0.2, 0.2, and 0.8.

A grid cell's degradation score is translated into a habitat quality value using a half saturation function where the user must determine the half-saturation value. As a grid cell's degradation score increases its habitat quality decreases. Let the quality of habitat in parcel :math:`x` that is in LULC :math:`j` be given by :math:`Q_{xj}` where,

.. math:: Q_{xj} = H_j\left(1-\left(\frac{D^z_{xj}}{D^z_{xj}+k^z}\right)\right)
   :label: (hq. 4)


and :math:`z` (we hard code :math:`z = 2.5`) and :math:`k` are scaling parameters (or constants). :math:`Q_{xj}` is equal to 0 if :math:`H_{j}` = 0. :math:`Q_{xj}` increases in :math:`H_{j}` and decreases in :math:`D_{xj}`. :math:`Q_{xj}` can never be greater than 1. The :math:`k` constant is the half-saturation constant and is set by the user. The parameter :math:`k` is equal to the :math:`D` value where :math:`1-\left(\frac{D^z_{xj}}{D^z_{xj}+k^z} = 0.5\right)`. For example, if :math:`k = 5` then :math:`1-\left(\frac{D^z_{xj}}{D^z_{xj}+k^z}\right) = 0.5` when :math:`D_{xj} = 5`. By default, you can set :math:`k = 0.05` (see note in Data Needs section). If you are doing scenario analyses, whatever value you chose for :math:`k` for the first landscape you ran the model on, that same :math:`k` must be used for all alternative scenarios on the same landscape. Similarly, whatever spatial resolution you chose the first time you ran the model on a landscape use the same value for all additional model runs on the same landscape. If you want to change your choice of :math:`k` or the spatial resolution for any model run then you have to change the parameters for all model runs, if you are comparing multiple scenarios on the same landscape.

|

.. figure:: ./habitat_quality/possible_threats.png
   :align: center
   :figwidth: 500px

Table 1. Possible degradation sources based on the causes of endangerment for American species classified as threatened or endangered by the US Fish and Wildlife Service. Adapted from Czech et al. 2000. 

|

Habitat Rarity
^^^^^^^^^^^^^^

While mapping habitat quality can help to identify areas where biodiversity is likely to be most intact or imperiled, it is also critical to evaluate the relative rarity of habitats on the landscape regardless of quality. In many conservation plans, habitats that are rarer are given higher priority, simply because options and opportunities for conserving them are limited and if all such habitats are lost, so too are the species and processes associated with them.

The relative rarity of an LULC type on a current or projected landscape is evaluated vis-a-vis a baseline LULC pattern. A rare LULC type on a current or projected map that is also rare on some ideal or reference state on the landscape (the baseline) is not likely to be in critical danger of disappearance, whereas a rare LULC type on a current or projected map that was abundant in the past (baseline) is at risk.

In the first step of the rarity calculation we take the ratio between the current or projected and past (baseline) extents of each LULC type :math:`j`. Subtracting this ratio from one, the model derives an index that represents the rarity of that LULC class on the landscape of interest.

.. math:: R_j=1-\frac{N_j}{N_{j_\mathrm{baseline}}}
   :label: (hq. 5)


where :math:`N_j` is the number of grid cells of LULC :math:`j` on the current or projected map and :math:`N_{j_\mathrm{baseline}}` gives the number of grid cells of LULC :math:`j` on the baseline landscape. The calculation of :math:`R_j` requires that the baseline, current, and/or projected LULC maps are all in the same resolution. In this scoring system, the closer to 1 a LULC's :math:`R` score is, the greater the likelihood that the preservation of that LULC type on the current or future landscape is important to biodiversity conservation. If LULC :math:`j` did not appear on the baseline landscape then we set :math:`R_j = 0`.

Once we have a :math:`R_j` measure for each LULC type, we can quantify the overall rarity of habitat type in grid cell :math:`x` with:

.. math:: R_x=\sum^X_{x=1}\sigma_{xj}R_j
   :label: (hq. 6)

where :math:`\sigma_{xj}= 1` if grid cell x is in LULC :math:`j` on a current or projected landscape and equals 0 otherwise.

Limitations and Simplifications
-------------------------------

In this model all threats on the landscape are additive, although there is evidence that, in some cases, the collective impact of multiple threats is much greater than the sum of individual threat levels would suggest.

Because the chosen landscape of interest is typically nested within a larger landscape, it is important to recognize that a landscape has an artificial boundary where the habitat threats immediately outside of the study boundary have been clipped and ignored. Consequently, threat intensity will always be less on the edges of a given landscape. There are two ways to avoid this problem. One, you can choose a landscape for modeling purposes whose spatial extent is significantly beyond the boundaries of your landscape of interest. Then, after results have been generated, you can extract the results just for the interior landscape of interest. Or you can limit your analysis to landscapes where degradation sources are concentrated in the middle of the landscape.

Data Needs
==========

- :investspec:`habitat_quality workspace_dir`
- :investspec:`habitat_quality results_suffix`
- :investspec:`habitat_quality lulc_cur_path` This is used to define the geospatial extents for the corresponding threat rasters.

- :investspec:`habitat_quality lulc_fut_path` If provided, the model will generate degradation, habitat quality, and habitat rarity (if baseline map is provided) outputs.

- :investspec:`habitat_quality lulc_bas_path` The baseline LULC is required to calculate habitat rarity. When used to calculate habitat rarity corresponding threat rasters are optional for also calculating habitat quality for the baseline scenario.

  If possible, the baseline map should refer to a time when intensive management of the land was relatively rare. For example, a map of LULC in 1851 in the Willamette Valley of Oregon, USA, captures the LULC pattern on the landscape before it was severely modified by massive agricultural production. Granted, this landscape had been modified by American Indian land clearing practices such as controlled fires as well.

- :investspec:`habitat_quality threats_table_path`
  
  Columns:

  - :investspec:`habitat_quality threats_table_path.columns.threat`
  - :investspec:`habitat_quality threats_table_path.columns.max_dist`
  - :investspec:`habitat_quality threats_table_path.columns.weight`
  - :investspec:`habitat_quality threats_table_path.columns.decay`
  - :investspec:`habitat_quality threats_table_path.columns.cur_path`
  - :investspec:`habitat_quality threats_table_path.columns.base_path`
  - :investspec:`habitat_quality threats_table_path.columns.fut_path`

  **Example Study**
  
  Hypothetical study with three threats for both current and future scenarios. Agriculture (*Agric* in the table) degrades habitat over a larger distance than roads do, and has a greater overall magnitude of impact. Further, paved roads (*Paved_rd*) attract more traffic than dirt roads (*Dirt_rd*) and thus are more destructive to nearby habitat than dirt roads. Filepaths are relative to the Threat data table, so in this instance the current threats are found in the same directory as the table and the future threats are found in a sub directory adjacent to the Threat data table called *future*. Baseline threat filepaths are left blank because we do not have threat rasters for that scenario OR we have not included the baseline LULC in our model run altogether.

  ========   ========  ======  =========== ============ =================  =======================
  THREAT     MAX_DIST  WEIGHT  DECAY        BASE_PATH     CUR_PATH         FUT_PATH
  ========   ========  ======  =========== ============ =================  =======================
  Dirt_rd    2         0.1     linear                   dirt_rd.tif        future/dirt_rd_fut.tif
  Paved_rd   4         0.4     exponential              paved_rd.tif       future/paved_rd_fut.tif
  Agric      8         1       linear                   agric_rd.tif       future/agric_rd_fut.tif
  ========   ========  ======  =========== ============ =================  =======================

  **Threat Rasters Information**
  
  GIS raster files of the distribution and intensity of each individual threat, with values between 0 and 1. You will have as many of these maps as you have threats and the raster filepath should be defined in the **Threats data** table. The extent and resolution of these raster datasets does not need to be identical to that of the input LULC maps. In cases where the threats and LULC map resolutions vary, the model will use the resolution and extent of the LULC map. Each cell in the raster contains a value that indicates the density or presence of a threat within it (e.g., area of agriculture, length of roads, or simply a 1 if the grid cell is a road or crop field and 0 otherwise). All threats should be measured in the same scale and units (i.e., all measured in density terms or all measured in presence/absence terms) and not some combination of metrics. Do not leave any area on the threat maps as 'No Data'. If pixels do not contain that threat set the pixels' threat level equal to 0.
	
  InVEST will not prompt you for these rasters in the tool interface but will instead look for their filepaths in the **Threats data** table under the corresponding scenario columns. The paths should be **relative** to the **Threats data** table path.
  
  Finally, note that we assume that the relative weights of threats and sensitivity of habitat to threats do not change over time, so we only submit one Threat data table and one Habitat sensitivity data table. If you want to change these over time then you will have to run the model multiple times.
	
  In the sample datasets, threat rasters are stored in the same directory as the Threats data table and are defined in the Threat data table under the appropriate column name as follows: **CUR_PATH**: crops_c.tif; railroad_c.tif; urban_c.tif; timber_c.tif; roads1_c.tif; roads2_c.tif; roads3_c.tif; **FUT_PATH**: crops_f.tif; railroad_f.tif; urban_f.tif; timber_f.tif; roads1_f.tif; roads2_f.tif; roads3_f.tif. When inputting the the baseline and future scenario LULC files found in the sample dataset we are running a habitat quality analysis for the current and future LULC scenario maps. A habitat quality map will not be generated for the baseline map because we have not provided any threat layers for the baseline map and left those columns blank in the Threat data table. The name 'crops' refers to cropland, 'railroad' to train rails, 'urban' to urban, 'timber' to rotation forestry, 'roads1' to primary roads, 'roads2' to secondary roads, and 'roads3' to light roads.

- :investspec:`habitat_quality sensitivity_table_path`

  Columns:

  - :investspec:`habitat_quality sensitivity_table_path.columns.lulc`
  - :investspec:`habitat_quality sensitivity_table_path.columns.habitat` This is :math:`H_j` in the equations above. If you want to simply classify each LULC as habitat or not without reference to any particular species group then use 0s and 1s where a 1 indicates habitat. Otherwise, if sufficient information is available on a species group's habitat preferences, assign the LULC a relative habitat suitability score between 0 and 1 where 1 indicates the highest habitat suitability. For example, a grassland songbird may prefer a native prairie habitat above all other habitat types (prairie is given a "HABITAT" score of 1 for grassland birds), but will also use a managed hayfield or pasture if prairie is not available (managed hayfield and pasture are given a "HABITAT" score of 0.5 for grassland birds).

  - :investspec:`habitat_quality sensitivity_table_path.columns.[THREAT]` Even if the LULC is not considered habitat, do not leave its sensitivity to each threat as Null or blank, instead enter a 0.

  *Example:* A hypothetical study with four LULC types and three threats. In this example we treat Closed Woodland and Forest Mosaic as (absolute) habitat and Bare Soil and Cultivation as (absolute) non-habitat. Forest mosaic is the most sensitive (least resistant) habitat type, and is more sensitive to dirt roads (DIRT_RD, value 0.9) than paved roads (PAVED_RD, value 0.5) or agriculture (AGRIC value 0.8). We enter 0s across all threats for the two developed land covers, Bare Soil and Cultivation, since they are not habitat.

  ====    =============== ======= ======= ==========  =========
  LULC    NAME            HABITAT AGRIC   PAVED_RD    DIRT_RD
  ====    =============== ======= ======= ==========  =========
  1       Bare Soil       0       0       0           0
  2       Closed Woodland 1       0.5     0.2         0.4
  3       Cultivation     0       0       0           0
  4       Forest Mosaic   1       0.8     0.8         0.5
  ====    =============== ======= ======= ==========  =========

- :investspec:`habitat_quality access_vector_path` Polygons with minimum accessibility (e.g., strict nature reserves, well protected private lands) are assigned some number less than 1, while polygons with maximum accessibility (e.g., extractive reserves) are assigned a value 1. These polygons can be land management units or a regular array or hexagons or grid squares.
  
  This vector has one required field:
  - :investspec:`habitat_quality access_vector_path.fields.access`


- :investspec:`habitat_quality half_saturation_constant` This is :math:`k` in equation :eq:`(hq. 4)`. The default value is 0.05. In general, you want to set :math:`k` to half of the highest grid cell degradation value on the landscape. To perform this model calibration you will have to the run the model once to find the highest degradation value and set :math:`k` for your landscape. For example, if a preliminary run of the model generates a degradation map where the highest grid-cell degradation level is 1 then setting :math:`k` at 0.5 will produce habitat quality maps with the greatest variation on the 0 to 1 scale (this helps with visual representation of heterogeneity in quality across the landscape). It is important to note that the rank order of grid cells on the habitat quality metric is invariant to your choice of :math:`k`. The choice of :math:`k` only determines the spread and central tendency of habitat quality scores. It is important to use the same value of :math:`k` for all runs that involve the same landscape. If you want to change your choice of :math:`k` for any model run then you must change the parameters for all model runs.

.. _hq-interpreting-results:

Interpreting Results
--------------------

**Degradation and Habitat Quality Edge Effects**
  Habitat quality and degradation values near the edges of the output rasters may be inflated because they do not account for threats that may exist beyond the extent of the land cover rasters. All input threat data are clipped to the extent of the LULC raster, so users should restrict interpretation of the results by disregarding values that are within the maximum threat distance of the edge of the output rasters.

* **[Workspace]** folder:

  * **Parameter log**: Each time the model is run, a text (.txt) file will be created in the Workspace. The file will list the parameter values and output messages for that run and will be named according to the service, the date and time. When contacting NatCap about errors in a model run, please include the parameter log.

* **[Workspace]\\output** folder:

  * **deg_sum_out_c_[Suffix].tif** -- Relative level of habitat degradation on the current landscape. A high score in a grid cell means habitat degradation in the cell is high relative to other cells. Grid cells with non-habitat land cover (LULC with :math:`H_j` = 0) get a degradation score of 0. This is a mapping of degradation scores calculated with equation (3).
	
  * **deg_sum_out_f_[Suffix].tif** -- Relative level of habitat degradation on the future landscape. A high score in a grid cell means habitat degradation in the cell is high relative to other cells. This output is only created if a future LULC map is given as input. Grid cells with non-habitat land cover (LULC with :math:`H_j` = 0) get a degradation score of 0. This is a mapping of degradation scores calculated with equation (3).

  * **quality_out_c_[Suffix].tif** -- Relative level of habitat quality on the current landscape. Higher numbers indicate better habitat quality vis-a-vis the distribution of habitat quality across the rest of the landscape. Areas on the landscape that are not habitat get a quality score of 0. This quality score is unitless and does not refer to any particular biodiversity measure. This is a mapping of habitat qulaity scores calculated with equation (4).
	
  * **quality_out_f_[Suffix].tif** -- Relative level of habitat quality on the future landscape. Higher numbers indicate better habitat quality vis-a-vis the distribution of habitat quality across the rest of the landscape. This output is only created if a future LULC map is given as input. Areas on the landscape that are not habitat get a quality score of 0. This quality score is unitless and does not refer to any particular biodiversity measure. This is a mapping of habitat qulaity scores calculated with equation (4).

  * **rarity_c_[Suffix].tif** -- Relative habitat rarity on the current landscape vis-a-vis the baseline map. This output is only created if a baseline LULC map is given as input. This map gives each grid cell's value of :math:`R_x` (see equation (6)). The rarer the habitat type in a grid cell is vis-a-vis its abundance on the baseline landscape, the higher the grid cell's value in rarity_c.tif.
	
  * **rarity_f_[Suffix].tif** -- Relative habitat rarity on the future landscape vis-a-vis the baseline map. This output is only created if both baseline and future LULC maps are given as input. This map gives each grid cell's value of :math:`R_x` (see equation (6)). The rarer the habitat type in a grid cell is vis-a-vis its abundance on the baseline landscape, the higher the grid cell's value in rarity_f.tif.

* **[Workspace]\\intermediate** folder:

	This folder contains some of the intermediate files created during the model run. Usually you do not need to work with these files, unless you are trying to better understand how the model works, or debugging a model run. They include maps of habitats (**habitat__[b,c,f].tif**), threats layers processed with Threats data table attributes (**[threat]_filtered_[b,c,f].tif**), sensitivity applied to different threats (**sens_[threat]_[b,c,f].tif**), and a rasterized version of the Access input (**access_layer.tif**).

Modifying Output and Creating a Landscape Biodiversity Score
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The model output does not provide landscape-level quality and rarity scores for comparing the baseline, current, and future LULC scenarios. Instead the user must summarize habitat extent and quality and rarity scores for each landscape. At the simplest level, a habitat quality landscape score for an LULC scenario is simply the aggregate of all grid cell-level scores under the scenario. In other words, we can sum all grid-level quality scores from the *quality_out_c.tif*, *quality_out_b.tif* (if available), and *quality_out_f.tif* (if available) maps and then compare scores. A map may have a higher aggregate quality score for several reasons. For one, it may just have more habitat area. However, if the amount of habitat across any two scenarios is approximately the same then a higher landscape quality score is indicative of better overall quality habitat.

Scores for certain areas on a landscape could also be compared. For example, we could compare aggregate habitat quality scores in areas of the landscape that are known to be in the geographic ranges of species of interest. For example, suppose we have geographic range maps of 9 species and have provided current and future LULC scenario maps to the Habitat Quality model. In this case we would determine 18 aggregate habitat quality scores, once for each modeled species under each scenario (current and future). Let :math:`G_{s_{\mathrm{cur}}}` indicate the set of grid cells on the current landscape that are in :math:`s`' range. Then the average habitat quality score in species :math:`s`' range on the current landscape is given by,

.. math:: Q_{s_{\mathrm{cur}}}=\frac{\sum^{G^{s_{\mathrm{cur}}}}_{x=1}Q_{xj_{\mathrm{cur}}}}{G^{s_{\mathrm{cur}}}}
  :label: (hq. 9)

where :math:`Q_{xj_{cur}}` indicates the habitat quality score on pixel :math:`x` in LULC :math:`j` on the current landscape and :math:`Q_{xj_{cur}} = 0` if quality_out.tif for pixel :math:`x` is "No Data". The average range-normalized habitat quality score for all 9 species on the current landscape would be given by,


.. math:: R_x = \sum^X_{x=1}\sigma_{xj}R_j
  :label: (hq. 10)

Then we would repeat for the future landscape with the grid cells in set :math:`G_{s_{\mathrm{fut}}}` for each species :math:`s` and the set of :math:`Q_{xj_{fut}}`.


References
==========

Ando, A, J. Camm, S. Polasky, and A. Solow. 1998. Species distributions, land values, and efficient conservation. Science 279:2126-2128.

Czech, B., P. R. Krausman, and P. K. Devers. 2000. Economic Associations among Causes of Species Endangerment in the United States. Bioscience 50:593-601.

Forman, R. 1995. Land Mosaics: The Ecology of landscapes and regions. Cambridge Univ Press. New York.

Forman, R. 2003. Road ecology: science and solutions. Island Press. New York, New York.

Franklin, J.F. and D. B. Lindenmayer. 2009. Importance of matrix habitats in maintaining biological diversity. Proceedings of the National Academy of Sciences 106:349-350.

Hall, L.S., Krausman, P.R. and Morrison, M.L. 1997. The habitat concept and a plea for standard terminology. Wildlife Society Bulletin 25(1):173-182.

Lindenmayer, D., Hobbs, R., Montague-Drake, R., Alexandra, J., Bennett, A., Burgman, M., Cae, P., Calhoun, A., Cramer, V., Cullen, P. 2008. A checklist for ecological management of landscapes for conservation. Ecology Letters 11:78-91.

MacArthur, R., E. 0. Wilson. 1967. The theory of island biogeography. Princeton University Press, Princeton, NJ.

Mckinney, M.L. 2002. Urbanization, biodiversity, and conservation. BioScience 52:883-890.

Nelleman C, Kullered L, Vistnes I, Forbes B, Foresman T, Husby E, Kofinas G, Kaltenborn B, Rouaud J, Magomedova M, Bobiwash R, Lambrechts C, Schei P, Tveitdal S, Gron O, Larsen T. 2001. GLOBIO. Global methodology for mapping human impacts on the biosphere. UNEP/DEWA/TR.01-3.

Nelson, E., S. Polasky, D. J. Lewis, A. J. Plantinga, E. Lonsdorf, D. White, D. Bael & J. J. Lawler. 2008. Efficiency of incentives to jointly increase carbon sequestration and species conservation on a landscape. Proc. Nat. Acad. Sci. 105: 9471-9476.

Noss, R. F., M. A. Connell, and D. D. Murphy. 1997. The science of conservation planning: habitat conservation under the endangered species act. Island Press. Prugh, L., K. Hodges, A. Sinclair, and J. Brashares. 2008. Effect of habitat area and isolation on fragmented animal populations. Proceedings of the National Academy of Sciences 105:20770.

Ricketts, T. H. 2001. The Matrix Matters: Effective Isolation in Fragmented Landscapes. American Naturalist 158:87-99.

Vitousek, P. M., H. A. Mooney, J. Lubchenco, and J. M. Melillo. 1997. Human Domination of Earth's Ecosystems. Science 277:494.

Wilcove, D. S., D. Rothstein, J. Dubow, A. Phillips, and E. Losos. 1998. Quantifying Threats to Imperiled Species in the United States. Bioscience 48:607-615.
