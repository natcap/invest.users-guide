InVEST GLOBIO Model InVEST GLOBIO模型
===================

Summary摘要
-------

The GLOBIO model provides an index of biodiversity according to mean
species abundance (MSA), the average population-level response across a
range of species, to different stressors, including land-use change,
fragmentation, and infrastructure. The model can be used as a static
assessment of how far below a pristine state the current environment is
or to estimate how a change in any of the stressors would lead to a
stress in biodiversity or ecosystem integrity, as indicated by MSA.
GLOBIO模型根据平均物种丰度（MSA）提供了一个生物多样性指数，MSA是指一系列物种对不同压力源的平均种群数量水平反应，压力源包括土地使用变化、破碎化和基础设施。 该模型可用于静态评估当前环境低于原始状态的程度，或估计任何压力源的变化将如何导致生物多样性或生态系统完整性的压力，如MSA所示。

Introduction引言
------------

The GLOBIO methodology was developed by the United Nations Environmental
Programme (UNEP, Alkemade et al. 2009) to model human impacts on
biodiversity, measured by mean species abundance (MSA). Mean Species
Abundance is an improvement over the more traditional species-area curve
approach for two reasons. First, it gives aggregate estimates of species
densities, not just species presence, which is important to represent
true diversity since presence alone gives limited information about
population viability (Balmford et al 2012). Second, it relates more than
habitat area to changes in biodiversity by including information about
the impact of fragmentation and threats from infrastructure (and climate
change and nitrogen deposition if the full version of GLOBIO were
implemented).
GLOBIO方法由联合国环境规划署（UNEP，Alkemade等人，2009）开发，用于模拟人类对生物多样性的影响，以平均物种丰度（MSA）作为衡量指标。 平均物种丰度是对更传统的物种-面积曲线方法的改进，原因有二。 首先，它给出了物种密度的总体估计，而不仅仅是物种的存在，这对于代表真正的多样性是很重要的，因为仅仅是物种存在给出的关于种群生存能力的信息很有限（Balmford et al 2012）。 其次，它将生境面积与生物多样性的变化联系在一起，包括关于破碎化的影响和基础设施的威胁（如果实施完整版的GLOBIO，还包括气候变化和氮沉降）的信息。

The model 模型
---------

The GLOBIO method consists of a set of equations linking environmental
drivers to biodiversity impact, tables of parameters to estimate the
above equations, based on a broad literature review, and suggested
methodologies for inputting and processing the spatial data required. We
have extended the GLOBIO methodology to downscale their global approach
to a landscape level.
GLOBIO方法包括一套将环境驱动因素与生物多样性影响联系起来的方程，根据广泛的文献回顾估算上述方程的参数表，以及输入和处理所需空间数据的建议方法。我们对GLOBIO的方法进行了扩展，将其全球方法缩小到景观尺度。

How it works 工作原理
~~~~~~~~~~~~

The GLOBIO approach is based on mean species abundance (MSA, see
Schwartz et al. 2003 for an example usage of MSA). An MSA estimation
ranges from 0 to 1, indicating the average proportional change in
abundance of individual species in a location against that same location
being pristine vegetation. An MSA of 1.0 implies that on average,
species abundances are the same as in pristine land while an MSA of 0.0
implies that average species abundance is zero. Comparing MSA values of
different scenarios identifies how anthropogenic changes affect
biodiversity (e.g., changing from a scenario with a mean MSA of 0.6 to a
new scenario with 0.5 implies that, on average, individual species’
abundances declined 16.6% due to the land use change). In GLOBIO, an MSA
value is defined for every grid-cell within a geospatial extent.
GLOBIO方法是基于平均物种丰度（MSA，见Schwartz等人2003年的MSA使用实例）。MSA的估计取值范围是0到1，表示一个地点的单个物种丰度与同一地点的原始植被的平均比例变化。1.0的MSA意味着平均而言，物种丰度与原始土地相同，而0.0的MSA意味着平均物种丰度为零。比较不同情景的MSA值，可以确定人类活动的变化对生物多样性的影响（例如，从平均MSA为0.6的情景变为0.5的新情景，意味着由于土地利用变化，单个物种的丰度平均下降了16.6%）。在GLOBIO中，MSA值是为地理空间范围内的每个网格单元定义的。

Stressors decrease MSA in a multiplicative way. In the GLOBIO3 paper,
the stressors included land use/land cover (LU), excess atmospheric
nitrogen deposition (N), proximity of infrastructure (mainly roads; I),
fragmentation (F) and climate change (CC), as in the following equation
to calculate MSA per pixel (i):
压力源以乘法方式减少MSA。在GLOBIO3论文中，压力源包括土地利用/土地覆盖（LU）、过量的大气氮沉降（N）、靠近基础设施（主要是道路；I）、破碎化（F）和气候变化（CC），可根据以下公式计算每个像素的MSA（i）：

.. math:: \text{MS}A_{i} = MSA_{LU_{i}} \bullet MSA_{N_{i}} \bullet MSA_{I_{i}} \bullet MSA_{F_{i}} \bullet MSA_{CC_{i}}

To consider changes in land-use, we ignore the nitrogen deposition term
and climate change terms; since neither of these terms change with each
land-change scenario, they will cancel out when percent change in total
(summed) MSA is calculated.
为了考虑土地利用的变化，我们忽略了氮沉降项和气候变化项；因为这些项都不随每个土地变化情况而变化，在计算总（总）MSA的百分比变化时，它们将被抵消。

We refine the GLOBIO methodology for MSA change due to infrastructure,
fragmentation, and land-use in order to make use of higher resolution
land-use/land-cover data (500 m pixels from MODIS rather than 50 km
pixels used by UNEP) needed to detect finer-scale ecological response
that may include nonlinearities. Downscaling requires new methods for
assigning land management regime sub-classes with more precision based
on high-resolution data rather than continent-wide aggregates, and a
more sophisticated approach for quantifying fragmentation than applying
overall averages of patch size for different habitats.
我们对GLOBIO方法进行了改进，以研究基础设施、破碎化和土地利用导致的MSA变化，以便利用更高分辨率的土地利用/土地覆盖数据（来自MODIS的500米像素，而不是UNEP使用的50公里像素）来检测可能包括非线性的更精细的生态反应。降尺度要求采用新的方法，来更精确地分配土地管理制度子类型，根据高分辨率数据而不是整个大陆的总量，并采用更复杂的方法来量化破碎化，而不是对不同生境的斑块大小采用总体平均数。

Calculating MSA Impact from Infrastructure计算基础设施带来的MSA影响
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Table 1 provides the data from Alkemade et al. (2009) for MSA values of
different buffers around infrastructure that impact different
ecosystems. The impact of infrastructure on MSA is determined solely by
distance, not by the nature of the intervening vegetation. An area of
cropland that is 5 km from a road will have its MSA reduced by a factor
of 0.9 regardless of whether the area between the cropland and the road
is tropical forest or more cropland. All sources of infrastructure are
aggregated into a “man-made” land use/land cover class. The remaining
land cover classes, which can then be considered vegetative or “natural”
are split into three basic types: tropical forest, temperate or boreal
forest, and grassland or cropland. The distance of these different
habitat classes from infrastructure is used to calculate the impact zone
for determining MSA from infrastructure, using Table 1.
表1提供了Alkemade等人（2009）关于影响不同生态系统的基础设施周围不同缓冲区的MSA值的数据。基础设施对MSA的影响仅由距离决定，而不是由干预植被的性质决定。一个距离公路5公里的耕地，其MSA将减少0.9倍，无论耕地和公路之间的区域是热带森林还是更多的耕地。所有的基础设施来源都被汇总到一个 "人造 "土地利用/土地覆盖类别中。剩下的土地覆被类别可以被认为是植被或 "自然空间"，被分成三个基本类型：热带森林、温带或北方森林、以及草原或耕地。这些不同的生境类别与基础设施的距离被用来计算影响区，以确定基础设施的MSA，使用表1。

**Table 1: Effect of infrastructure impact zones on MSA, source:**
Alkemade et al. (2009) 表1：基础设施影响区对MSA的影响，来源：**Alkemade等人（2009）。

=============== ================================================== =================================================== ======================================================= ========= ==================
**Impact Zone** **Tropical Forest Distance to infrastructure (m)**
**影响区** **热带森林与基础设施的距离（米）**
**Temperate Forest Distance to infrastructure (m)** 
**温带森林与基础设施的距离（米）** 
**Grassland & Cropland Distance to infrastructure (m)** 
** 草地和耕地与基础设施的距离（米）**。
 **MSA_I** **Standard Error**
=============== ================================================== =================================================== ======================================================= ========= ==================
High Impact     <1000                                              <300                                                <500                                                    0.4       0.22
Medium Impact   1000-4000                                          300-1200                                            500-2000                                                0.8       0.13
Low Impact      4000-14,000                                        1200-4200                                           2000-7000                                               0.9       0.06
No Impact       >14,000                                            >4200                                               >7000                                                   1.0       0.02
=============== ================================================== =================================================== ======================================================= ========= ==================


Calculating MSA Impact from Fragmentation计算碎片化带来的MSA影响
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We augment the standard GLOBIO approach to fragmentation analysis by
using a fragmented forest quality index (FFQI). The FFQI is similar to
methods used in the forestry literature, and is calculated by
considering how many of a forest’s neighboring cells are also forested.
Rather than identifying the expected MSA impact from patch-size (as in
GLOBIO), the FFQI estimates the relative effect of fragmentation with a
Gaussian smoothing function. This treats habitat patches that are
separated by only very small patches of infrastructure or non-habitat as
less fragmented that habitat patches separated by wider distances. We
convert the FFQI values on our map to km\ :sup:`2` to match the zones
defined in Table 2 (according to Alkemade 2009) by taking the square
root of the area to convert it to the width/height of the patch.
Although the method is different from how UNEP defined patches,
comparisons to the literature showed FFQI to be an accurate
approximation of more cumbersome patch-based approach.
我们通过使用破碎化森林质量指数(FFQI)来增强标准的GLOBIO破碎化分析方法。FFQI类似于林业文献中使用的方法，是通过考虑一个森林的相邻单元中有多少也是森林来计算的。FFQI不是从斑块大小来确定预期的MSA影响（如GLOBIO），而是用高斯平滑函数来估计破碎化的相对影响。这将被非常小的基础设施或非生境斑块隔开的生境斑块与被较远距离隔开的生境斑块视为较不破碎。我们将地图上的FFQI值转换为km\ :sup:`2`，以匹配表2中定义的区域（根据Alkemade 2009），通过采取面积的平方根将其转换为斑块的宽度/高度。尽管该方法与UNEP定义斑块的方式不同，但与文献的比较表明，FFQI与更繁琐的基于斑块的方法是高度相似的。

**Table 2: Fragmentation effect on MSA under varying patch sizes,
source:** Alkemade et al. (2009) **表2: 不同斑块大小下的碎片化对MSA的影响。资料来源：**Alkemade等人(2009)

=========== =============== ========= ==================
**FFQI**    **Area (km^2)** **MSA_F** **Standard Error**
=========== =============== ========= ==================
< 0.43      < 1             0.3       0.15
0.43 – 0.58 <10             0.6       0.19
0.58 – 0.90 <100            0.7       0.19
0.90 – 0.98 <1,000          0.9       0.20
0.98 – 0.99 <10,000         0.95      0.20
0.99 – 1    >10,000         1.0       0.20
=========== =============== ========= ==================

Calculating MSA Impact from Land Use Change计算土地利用变化带来的MSA影响
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most difficult aspect of GLOBIO to implement is assigning different
land-use/land-cover categories that relate to intensity of management or
human use, since this information is often absent in remotely-sensed
global land-cover datasets. To assist with this classification, we
developed simple rules for reclassifying the MODIS or other satellite
land-use/land-cover maps into the management categories for which MSA is
quantified by GLOBIO’s broad literature reviews. Table 3 presents the
rule-based categorization used to convert MODIS data to
GLOBIO-compatible classes. LULC types that are mapped to more than one
GLOBIO type are then split according to other auxiliary datasets
described below.
GLOBIO最难实施的方面是指定与管理或人类使用强度有关的不同的土地使用/土地覆盖类别，因为在基于遥感的全球土地覆盖数据集中往往缺乏这种信息。为了帮助这种分类，我们制定了简单的规则，基于广泛的文献审查，将MODIS或其他卫星土地利用/土地覆盖图重新分类到新的管理类别。表3列出了用于将MODIS数据转换为GLOBIO兼容类型的基于规则的分类方法。映射到一个以上GLOBIO类型的LULC类型，然后根据下面描述的其他辅助数据集进行分割。

Forests:森林
'''''''''

To distinguish between primary forest and other forest, including
secondary (replanted) forests or forests with some extractive use and
plantation forests, we analyze fragmentation in forest cover using FFQI
and assign different use categories based on FFQI, with primary forest
above a certain user-defined threshold. This approach assumes that
pristine forests are more likely to be found in large, unfragmented
tracts of forest, and that secondary or lightly used forests are more
likely to be found in the most highly fragmented patches of forest. The
threshold can be calibrated such that the aggregate amount of primary
and secondary or lightly-used forests match estimates at the national or
continental scale (documented in Alkemade et al. 2009).
为了区分原始森林和其他森林，包括次生(再植)森林或有一些采伐用途的森林和人工林，我们用FFQI分析森林覆盖的破碎化，并根据FFQI分配不同的使用类别，其中原始森林高于用户定义的某个阈值。这种方法假设原始森林更可能出现在大面积的、未被分割的森林中，而次生林或轻度使用的森林更可能出现在最高度分割的森林斑块中。 可以对阈值进行校准，使原始森林和次生林或轻度使用的森林总量与国家或大陆范围内的估计数相匹配（见Alkemade等人2009年的记录）。

Shrubland and Grassland:灌丛和草地
'''''''''''''''''''''''''

To distinguish between primary vegetation (more pristine) grasslands,
grazed grasslands, and man-made pastures (deforested areas used for
pasture), we compare the potential vegetation map generated by
Ramankutty and Foley (1999) described above to actual vegetation
determined by MODIS land-cover data. If a particular pixel is designated
forest according to the potential vegetation map, but is listed as
grassland in MODIS, it has likely forest that has been cleared for
grazing, in this case the pixel is reclassified as “man-made pasture.”
If a pixel is grassland according to the potential vegetation map and is
listed as grassland in the MODIS data, a separate dataset is utilized,
quantifying the proportional pasture area at ~10 km resolution developed
by Ramankutty et al. (2008). This pixel is defined as “livestock
grazing” if the proportion of the grid-cell in pasture is greater than a
user-defined threshold. The threshold can be chosen such that aggregate
totals of livestock grazing match national and provincial data, as
described above for forests. If the grassland pixel is lower than the
grazing threshold, it will be defined as primary vegetation.
为了区分原始植被（更原始的）草原、放牧草原和人造牧场（用于放牧的毁林区），我们将上述Ramankutty和Foley（1999）生成的潜在植被图与由MODIS土地覆盖数据确定的实际植被进行比较。如果一个特定的像素根据潜在植被图被指定为森林，但在MODIS中却被列为草地，那么它很可能是被清理出来放牧的森林，在这种情况下，该像素被重新归类为 "人造牧场"。 如果根据潜在植被图，一个像素是草原，且在MODIS数据中也被列为草原，则利用一个单独的数据集，以Ramankutty等人（2008）开发的约10公里分辨率量化牧场面积的比例。如果像素中牧草的比例大于用户定义的阈值，则该像素被定义为 "牲畜放牧"。 阈值的选择可以使牲畜放牧的总和与国家和省的数据相匹配，如上文对森林的描述。 如果草场像素低于放牧阈值，它将被定义为原始植被。

Cropland: 耕地
''''''''''

Because cropland intensification is only calculated in the
MSA\ :sub:`LU` and does not affect the configuration of primary habitat
and thus the fragmentation calculated for MSA\ :sub:`F`, the spatial
location of intensification is not necessary to define. The user only
needs to designate the proportion of agriculture in the landscape that
is intensified (i.e., not low-input agriculture). This can be found in
the regional datasets cited by Alkemade et al. (2009) or available
through FAO, or can be derived a dataset developed by Foley et al.
(2011) that maps yield gaps for all major commodity crops globally at
~10 km resolution. This methodology compares agricultural production in
similar climates (based on precipitation and growing degree days) and
rates crop yield in different regions according to the maximum yields
attained for its particular climate. The difference between actual and
maximum attainable yield is defined as the “yield gap.” The yield gap
can serve as a surrogate for (lack of) intensification, and the user can
examine the yield gap maps for their region of interest to determine
what proportion of the landscape falls below a certain level of yield
gap.
因为耕地集约化只在MSA\ :sub:`LU`中计算，不影响原始生境的配置，因此也不影响为MSA\ :sub:`F`计算的破碎化，所以集约化的空间位置没有必要定义。用户只需指定景观中集约化农业的比例（即不是低投入农业）。 这可以在 Alkemade 等人（2009）引用的区域数据集中找到，也可以通过FAO获得，或者可以从 Foley 等人（2011）开发的数据集中获得，该数据集以约 10 公里的分辨率绘制了全球所有主要商品作物的产量差距。这种方法比较了类似气候下的农业生产（基于降水和生长度日），并根据其特定气候下达到的最大产量来评定不同地区的作物产量。  实际产量和可达到的最大产量之间的差异被定义为 "产量差距"。  产量差距可以作为集约化的替代物（如数据缺乏），用户可以检查他们感兴趣的地区的产量差距图，以确定有多大比例的景观低于一定水平的产量差距。

**Table 3: MODIS to GLOBIO cover class conversion and MSA affected by
land use**
**表3：MODIS到GLOBIO覆盖类型转换和受土地使用影响的MSA**。

+-------------------------------------+------------------------------------+----------+---------+
|**MODIS Land Use/Land Cover Class**  |**Convert to which GLOBIO classes?**|**MSA_LU**|**SE**   |
+=====================================+====================================+==========+=========+
| - 0 - Water                         |N/A                                 |          |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 1 - Evergreen needleleaf forest   | - 1 - Primary vegetation\ :sup:`a` | - 1      |  - <0.01|
| - 2 - Evergreen broadleaf forest    | - 3 - Secondary forest\ :sup:`a`   | - 0.5    |  - 0.03 |
| - 3 - Deciduous needleleaf forest   |                                    | - 0.2    |  - 0.04 |
| - 4 - Deciduous broadleaf forest    |                                    |          |         |
| - 5 - Mixed forest                  |                                    |          |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 6 - Closed shrublands/cerrado     | - 1 - Primary vegetation\ :sup:`b` | - 1      | - <0.01 |
| - 7 - Open shrublands               | - 5 - Livestock grazing\ :sup:`c`  | - 0.7    | - 0.05  |
| - 8 - Woody savannas                | - 6 - Man-made pastures\ :sup:`b`  | - 0.1    | - 0.07  |
| - 9 - Savannas                      |                                    |          |         |
| - 10 - Grasslands                   |                                    |          |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 12 - Croplands/Perennial          | - 12 - All agriculture             | - 0.3    | - 0.12  |
|                                     |                                    | - 0.1    | - 0.08  |
+-------------------------------------+------------------------------------+----------+---------+
| - 13 - Urban and built-up           | - 10 - Built-up areas              | - 0.05   |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 16 - Barren or sparsely vegetated | - 1 - Primary vegetation           | - 1.0    | - <0.01 |
+-------------------------------------+------------------------------------+----------+---------+

*Split based on (a)FFQ (described in Fragmentation section, above), (b)
potential vegetation map (Foley et al. 2009), (c) proportional pasture
area (Ramunkutty et al. 2009). Missing from this classification
structure is GLOBIO classes “Lightly used natural forest” (GLOBIO class
2), “Plantation forest” (GLOBIO class 4), and “agroforestry” (GLOBIO
class 7), “Low-input agriculture” (GLOBIO class 8), and “Intensive
agriculture” (GLOBIO class 9). The agriculture classes are split in an
aspatial calculation of MSA_LU according to the “Fraction of
intensification” value set by the user.*
*根据(a)FFQ(如上文破碎化部分所述)，(b)潜在植被图(Foley等人，2009)，(c)牧场面积比例(Ramunkutty等人，2009)进行分割。这个分类结构中缺少GLOBIO等级 "轻度使用的天然林"（GLOBIO等级2）、"人工林"（GLOBIO等级4）和 "农林业"（GLOBIO等级7）、"低投入农业"（GLOBIO等级8）和 "密集型农业"（GLOBIO等级9）。在MSA_LU的非空间计算中，根据用户设定的 "集约化比例 "值，对农业等级进行分割。

Limitations and simplifications局限性和简化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MSA is an aggregate estimate, making it impossible to track
compositional effects, and there are many different compositional
possibilities for the same MSA. While MSA caps relative abundance of
individual species at 1, ensuring that a local rise in one species
cannot disguise a fall in overall species abundance, an MSA of 0.5 could
mean that all species are half as abundant as in a pristine state, or
that one species has suffered immense decline while the rest have
remained constant, or anywhere in between. Additional information about
the shape of the distribution of species abundances and extinction
probabilities related to different levels of MSA could improve the
usefulness of this index. But even then, diversity is more complex than
numbers of species and population numbers. Some conservation biologists
argue that species composition is as important as any other measure of
diversity, and tracking specific species is essential to estimating
impacts on threatened or endangered species or culturally valuable
species (Phalan et al. 2011 Food Policy). To achieve this level of
specificity, the impacts of different land-use strategies would need to
be evaluated for each species individually and then combined across
species for summary results, which may not be possible in many regions
of the world with low data availability and high agricultural and other
development pressure. In such cases, MSA provides a quick and easy to
use index for biodiversity change in decision contexts.
MSA是一个总的估计值，使得它不可能跟踪组分的影响，而且同一MSA有许多不同组分的可能性。虽然MSA将单个物种的相对丰度限制在1，确保一个物种的局部上升不能掩盖整体物种丰度的下降，但MSA为0.5可能意味着所有物种的丰度只有原始状态下的一半，或者一个物种遭受了巨大的下降而其他物种保持不变，或者介于两者之间。关于与不同水平的MSA相关的物种丰度和灭绝概率的分布形状的额外信息可以提高该指数的有用性。但即使如此，多样性也比物种数量和种群数量更复杂。一些保护生物学家认为，物种组成与任何其他多样性的衡量标准一样重要，追踪特定的物种对于估计对受威胁或濒危物种或有文化价值的物种的影响至关重要（Phalan等人，2011年食品政策）。为了达到这种具体水平，需要对每个物种单独评估不同的土地利用战略的影响，然后将不同的物种结合起来进行汇总，这在世界许多数据可用性低、农业和其他发展压力大的地区可能无法实现。在这种情况下，MSA为决策背景下的生物多样性变化提供了一个快速和易于使用的指数。

In our application of GLOBIO, we use the mean parameter values and their
standard errors to estimate the impacts of infrastructure, land-use, and
fragmentation at new locations, which assumes that these values
represent a random sample of species and geographic locations. However,
limited data availability for certain taxonomic groups and geographic
regions mean that there are potential biases in the parameter estimates
that add an unquantifiable degree of uncertainty to predictions based on
our application of GLOBIO. 在我们应用GLOBIO的过程中，我们使用平均参数值及其标准误差来估计基础设施、土地利用和新地点的破碎化的影响，这就假设这些值代表了物种和地理位置的随机样本。然而，某些分类群和地理区域的数据有限，这意味着参数估计存在潜在的偏差，这给我们基于GLOBIO的应用的预测增加了无法量化的不确定性。

The estimates of the impact of infrastructure are based on a
meta-analysis of ~75 studies, predominately of bird and mammal
populations in Europe and North America, with some information on
insects and plants (Alkemade et al. 2009; Benítez-López et al 2010).
Whether the impacts of infrastructure are similar for other taxonomic
groups or geographic areas is unknown. 对基础设施影响的估计是基于对约75项研究的meta分析，主要是对欧洲和北美的鸟类和哺乳动物种群的研究，还有一些关于昆虫和植物的信息（Alkemade等人，2009；Benítez-López等人，2010）。基础设施对其他分类群或地理区域的影响是否类似尚不清楚。

Estimates of the impacts of land use are based on a slightly greater
number of studies, with 89 identified in the initial publication of
GLOBIO (Alkemade et al. 2009) and 195 identified in a final published
meta-analysis (de Baan et al. 2013). The parameter estimate for all
artificial surfaces/built-up areas was based on expert opinion,
representing densely populated cities, and without quantification of
uncertainty (Alkemade et al. 2009). Datasets come largely from tropical
regions, with fewer from temperate regions and none from boreal zones
(de Baan et al. 2013). Data were available for 9 out of 14 biomes, and
for many biomes, information was only available for some land use types.
For example, information on permanent crops, agroforestry and artificial
areas came only from two biomes. For three biomes, information was only
available for pastures, but not for other land use types. As is common,
data were also taxonomically biased towards vertebrate and plant species
(de Baan et al. 2013). Arthropods were under-represented, and bacteria
and fungi were not included at all in the database. 对土地利用影响的估计是基于大量的已有研究，GLOBIO最初出版时确定了89项（Alkemade等人，2009年），最后出版的meta分析中确定了195项（de Baan等人，2013年）。所有人工地面/建筑区的参数估计值是基于专家意见，代表了人口稠密的城市，并且没有量化不确定性（Alkemade等人，2009）。数据集主要来自热带地区，温带地区较少，寒带地区没有（de Baan等人，2013）。14个生物群落中有9个有数据，而对于许多生物群落，只有某些土地利用类型的信息可用。例如，关于永久性作物、农林业和人工区的信息只来自两个生物群落。对于三个生物群落，只有牧场的信息，而没有其他土地利用类型的信息。常见的是，数据在分类学上也偏向于脊椎动物和植物物种（de Baan等人，2013）。节肢动物的代表性不足，细菌和真菌根本没有包括在数据库中。

Furthermore, our assignment of satellite land-cover (e.g., forest or
grassland) to the different GLOBIO land-use classes (e.g., primary vs.
secondary forest or pristine vs. grazed grassland) introduce additional
error that is not incorporated into the analysis. While we can ensure
that our assignments aggregate up to national or regional level
statistics, we cannot ground-truth our classification system to quantify
the level of accuracy or uncertainty. 此外，我们将卫星土地覆盖物（如森林或草地）分配给不同的GLOBIO土地利用等级（如原始森林与次生林或原始草地与放牧草地），会带来额外的误差，而这些误差没有被纳入分析中。虽然我们可以确保我们的分配汇总到国家或区域一级的统计数据，但我们无法对我们的分类系统进行实地验证，以量化准确性或不确定性的水平。

The impacts of fragmentation on mean species abundance (MSA) are based
on six datasets from 3 publications. The proportion of species with a
viable population was used as a proxy for MSA (Alkemade et al. 2009),
and it is unclear how much additional uncertainty in the parameters that
adds. Taxonomic and geographic biases are again a limitation. Two
studies focus exclusively on mammals, including ~30 mammal species in
Florida (Allen et al. 2001) and 10 species of carnivores from around the
world (Woodroffe & Ginsberg 1998). The third study is limited
exclusively to Europe, of which half of the 202 species included are
birds (Bouwma et al. 2002). 破碎化对平均物种丰度（MSA）的影响是基于3个出版物的6个数据集。具有存活种群的物种比例被用作MSA的替代值（Alkemade等人，2009），目前还不清楚该参数增加了多少不确定性。分类学和地理上的偏差也是一个局限性。有两项研究专门关注哺乳动物，包括佛罗里达州的约30种哺乳动物（Allen等人，2001年）和世界各地的10种食肉动物（Woodroffe & Ginsberg，1998年）。第三项研究只限于欧洲，其中包括的202个物种中，有一半是鸟类（Bouwma等人，2002）。

Data needs 数据需求
----------

**NOTE: All spatial data must be projected in meters (i.e., a
local, not a global or lat-long projection), to ensure accurate distance
to infrastructure calculations. The model will not execute without a
defined projection.**
注意：所有的空间数据都必须以米为单位进行投影（即本地投影，而不是全球或长纬度投影），以确保准确计算与基础设施的距离。如果没有定义的投影，该模型将不会运行。


- :investspec:`globio msa_parameters_path` The example below (included in the sample data) may be used as-is. It gives the mean values and standard errors provided in Alkemade et al. (2009). Advanced users may with to alter this table to put high and low estimates from confidence intervals in the msa_x column, to aid in uncertainty assessment.
- :investspec:`globio msa_parameters_path`下面的样例（包括在样本数据中）可以按原样使用。它给出了Alkemade等人（2009）提供的均值和标准误差。高级用户可以修改此表，将置信区间的高低估计值放在msa_x列中，以帮助进行不确定性评估。

   Columns:

   - :investspec:`globio msa_parameters_path.columns.msa_type`
   - :investspec:`globio msa_parameters_path.columns.value`
   - :investspec:`globio msa_parameters_path.columns.msa_x`

   **Example:** This example contains two extra columns, *Measurement* and *SE*, which are not used by the model. *SE* is the standard error associated with each MSA value, according to the meta-analysis in Alkemade et al. (2009). These values are recorded here in this sample data set so that the user can adjust the MSA_x values according to the confidence interval. *Measurement* describes the metric by which the value in the subsequent column is measured. **样例：**这个例子包含两个额外的列，*Measurement*和*SE*，这两列模型没有使用。根据Alkemade等人（2009）的meta分析，*SE*是与每个MSA值相关的标准误差。在这个样本数据集中，这些值被记录在这里，以便用户可以根据置信区间调整MSA_x值。*Measuremen描述了测量后续列中数值的指标。

   .. csv-table::
      :file: ../invest-sample-data/globio/msa_parameters.csv
      :header-rows: 1
      :widths: auto


- :investspec:`globio infrastructure_dir`

   .. note::注意：
      Unlike other spatial inputs to InVEST, only specific file formats are supported in the infrastructure directory. Raster infrastructure files must be in GeoTIFF format ending in .tif. Vector infrastructure files must be in ESRI Shapefile format ending in .shp. In a future InVEST version, other file formats may be allowed. 与InVEST的其他空间输入不同，基础设施目录中只支持特定的文件格式。栅格基础设施文件必须是以.tif结尾的GeoTIFF格式。矢量基础设施文件必须是以.shp结尾的ESRI Shapefile格式。在未来的InVEST版本中，可能会允许其他文件格式。

- :investspec:`globio aoi_path`

- :investspec:`globio intensification_fraction` Used in the computation of MSA\ :sub:`LU`. The rest is considered to be low-input agriculture.

- :investspec:`globio predefined_globio`

There are two options for the LULC input: 土地利用/土地覆盖LULC输入有两个选项。

  a. Vegetation-specific (not management-specific) land-cover. This is
      the type of land-cover you may acquire from MODIS or other
      remotely-sensed data sources. It distinguishes between forest,
      grassland, savanna, cropland, and other vegetation types. It does
      NOT distinguish between the differences in management defined by
      GLOBIO, such as primary vs. secondary vegetation, or grassland vs.
      pasture. If this option is chosen, several helper datasets (listed
      as required for option 1a, below) will be required. 特定植被（非特定管理）的土地覆盖。这是你可能从MODIS或其他遥感数据源获得的土地覆盖类型。它区分了森林、草原、稀树草原、耕地和其他植被类型。它不区分GLOBIO定义的管理差异，如原始植被与次生植被，或草原与牧场。如果选择这个选项，将需要几个辅助数据集（如下文选项1a所要求的那样列出）。

   b. Management-specific land-cover, following the classification
      scheme established by GLOBIO (see Table 3, above). If this option
      is chosen, tick the box for “Predefined land use map for GLOBIO”
      and enter the map there. All other data inputs will turn grey
      except for the other required data set, the infrastructure
      directory, and the optional AOI input. 遵循GLOBIO制定的分类方案，管理特定的土地覆盖物（见上面的表3）。如果选择了这个选项，请勾选 "Predefined land use map for GLOBIO"，并在此输入图层。除了其他所需的数据集、基础设施目录和可选的 AOI 输入，其他所有的数据输入都将变成灰色。

If you select the option to use predefined GLOBIO LULC, you only need to provide the GLOBIO LULC map: 如果你选择使用预定义的GLOBIO LULC选项，你只需要提供GLOBIO LULC图层。

- :investspec:`globio globio_lulc_path`

If you use a custom LULC map, you must provide several additional inputs: 如果你使用一个自定义的LULC地图，你必须提供几个额外的输入数据：

- :investspec:`globio lulc_path`

- :investspec:`globio lulc_to_globio_table_path`

  Columns:列：

  - :investspec:`globio lulc_to_globio_table_path.columns.lucode`
  - :investspec:`globio lulc_to_globio_table_path.columns.globio_lucode`

  *Example*: On the left is MODIS land-cover data, using the UMD classification, as defined in Table 3. On the right is the GLOBIO land-cover translation, which lumps the forest classes (1-5 in MODIS) into 130, grassland/shrubland (6-10 in MODIS) into 131, and agriculture (12 in MODIS) into 132. Urban land-use (13 in MODIS) maps directly onto built-up lands (10 in GLOBIO). Barren or sparsely vegetated (16 in MODIS) can be treated primary vegetation (1 in GLOBIO). The subsequent datasets and/or user inputs will help determine how to split up the 130, 131, and 132 into primary and secondary vegetation, rangelands and pasture, and intensified and unintensified agriculture, respectively. *样例*。左边是MODIS土地覆盖数据，使用UMD分类，如表3所定义。右边是GLOBIO土地覆盖物转换，将森林类（MODIS中的1-5）归入130，草地/灌木林地（MODIS中的6-10）归入131，农业（MODIS中的12）归入132。城市土地利用（MODIS中的13）直接映射到已建成的土地（GLOBIO中的10）。贫瘠或稀疏的植被（MODIS中的16个）可被视为初级植被（GLOBIO中的1个）。随后的数据集和/或用户输入将有助于确定如何将130、131和132分别分割成原始和次生植被、牧场和草场，以及集约化和非集约化农业。

  .. csv-table::
     :file: ../invest-sample-data/globio/lulc_conversion_table.csv
     :header-rows: 1
     :widths: auto

- :investspec:`globio pasture_path` This is the proportional pasture area as developed by Ramankutty et al. (2008). See explanation in *Shrubland and grassland* under *How it Works*, above. 这是由Ramankutty等人（2008）制定的牧场面积比例。见上文*工作原理*下*灌丛和草地*的解释。

- :investspec:`globio potential_vegetation_path` Using the potential vegetation map generated by Ramankutty and Foley (1999) is recommended. If you wish to use your own potential vegetation data, the potential vegetation classification codes must match those from Ramankutty and Foley. See explanation in *Shrubland and grassland* under *How it Works*, above. 建议使用Ramankutty和Foley（1999）生成的潜在植被图。如果你想使用自己的潜在植被数据，潜在植被分类代码必须与Ramankutty和Foley的代码一致。见上文*工作原理*下*灌丛和草地*的解释。

- :investspec:`globio primary_threshold` This value can be adjusted such that the aggregate land-use matches regional statistics. 这个值可以进行调整，以便使土地使用类型的总量与区域统计数据相匹配。

- :investspec:`globio pasture_threshold` This value can be adjusted such that the aggregate land-use matches regional statistics. 这个值可以进行调整，以便使土地使用类型的总量与区域统计数据相匹配。


Interpreting Results结果解释
--------------------

Final Results最终结果
~~~~~~~~~~~~~

- **globio-log**: Each time the model is run, a text (.txt) file will
      appear in the *Output* folder. The file will list the parameter
      values for that run and will be named according to the service,
      the date and time, and the suffix. 每次模型运行时，一个文本（.txt）文件将出现在*Output*文件夹中。该文件将列出该次运行的参数值，并将根据服务、日期和时间以及后缀来命名。

- **aoi_summary_<suffix>**: A shapefile summarizing the average MSA for
      each zone defined in the area of interest. 总结感兴趣地区所定义的每个区域的平均MSA的shapefile。

- **msa_<suffix>.tif**: A raster of the overall MSA (mean species
      abundance) value, defined as “the average abundances of originally
      occurring species relative to their abundance in the original,
      pristine or mature state as the basis.” This index is on a scale
      of 0 to 1, with 1 being the pristine condition, calculated as the
      product of the MSA\ :sub:`LU`, MSA\ :sub:`F`, and MSA\ :sub:`I`
      below. 整体MSA（平均物种丰度）值的栅格，定义为 "相对于作为基础的原始、原始或成熟状态下的丰度，最初出现的物种的平均丰度"。这个指数在0到1的范围内，1是原始状态，以下MSA\ :sub:`LU`, MSA\ :sub:`F`, 和MSA\ :sub:`I`相乘得到。

- **msa_lu_<suffix>.tif**: A raster of MSA calculated for impacts of
      land-use only. 仅为土地使用的影响而计算的MSA栅格。

- **msa_f_<suffix>.tif**: A raster of MSA calculated for impacts of
      fragmentation only. 仅针对破碎化的影响而计算的MSA栅格。

- **msa_i_<suffix>.tif**: A raster of MSA calculated for impacts of
      infrastructure only. 仅为基础设施的影响而计算的MSA栅格。

Intermediate Results中间结果
~~~~~~~~~~~~~~~~~~~~

- **distance_to_infrastructure_<suffix>.tif**: A map coding each pixel by
      its distance to the nearest infrastructure, used to compute
      MSA\ I. Distance in this raster is measured as number of pixels,
      which is converted to meters in the model using the defined
      projection. 这张地图按照每个像素与最近的基础设施的距离进行编码，用于计算MSA/I。这个栅格中的距离以像素数来衡量，在模型中使用定义的投影将其转换为米。

- **globio_lulc_<suffix>.tif**: The final land use map converted to
      GLOBIO classification, as outlined in Table 3. If desired, this
      map (or any altered version of this map) could be used to run the
      model using option 1b, above. This is used to compute MSA\ LU. 最终的土地利用图转换为GLOBIO分类，如表3中所述。如果需要，该地图（或该地图的任何改变版本）可用于使用上述选项1b运行模型。这被用来计算MSA/LU。

- **primary_veg_smooth_<suffix>.tif**: A Gaussian-filtered (“smoothed”)
      map of primary vegetation (identified in globio_lulc), used to
      compute MSA\ F. 经过高斯过滤（"平滑"）的原始植被图（在globio_lulc中识别），用于计算MSA/F。

- **tmp/ffqi_<suffix>.tif**: A map of the forest fragmentation quality
      index (ffqi), used to differentiate between primary and secondary
      forest in the GLOBIO land use classification. 森林破碎化质量指数（ffqi）的地图，用于区分GLOBIO土地利用分类中的原始森林和次生森林。

- **tmp/combined_infrastructure_<suffix>.tif**: A map joining all the
      infrastructure files in the infrastructure directory (input 2
      above). If there is only one file in that directory, it should be
      identical to that file. 一个连接基础设施目录中所有基础设施文件的地图（上面的输入2）。如果该目录中只有一个文件，它应该与该文件相同。

- **tmp/**: Other files in this directory represent intermediate steps in
      calculations of the final data in the output folder. 该目录中的其他文件代表了输出文件夹中最终数据的计算的中间步骤。

- **\_taskgraph_working_dir:** This directory stores metadata used
      internally to enable avoided re-computation. 这个目录存储了内部使用的元数据，以便能够避免重新计算。

References参考文献
----------

Alkemade, Rob, Mark van Oorschot, Lera Miles, Christian Nellemann,
Michel Bakkenes, and Ben ten Brink. "GLOBIO3: a framework to investigate
options for reducing global terrestrial biodiversity loss." *Ecosystems*
12, no. 3 (2009): 374-390.

Allen, C. R., Pearlstine, L. G., & Kitchens, W. M. (2001). Modeling
viable mammal populations in gap analyses. Biological Conservation,
99(2), 135–144. doi:10.1016/S0006-3207(00)00084-7

Balmford A., R. Green, B. Phalan. 2012 What conservationists need to
know about farming. Proc. R. Soc. B 279: 2714–2724.

Benítez-López, A., Alkemade, R., & Verweij, P. a. (2010). The impacts of
roads and other infrastructure on mammal and bird populations: A
meta-analysis. Biological Conservation, 143(6), 1307–1316.
doi:10.1016/j.biocon.2010.02.009

Bouwma, I. M., Jongman, R. H. G., & Butovsky, R. O. (2002). Indicative
map of the Pan-European Ecological Network - technical background
document. Tilburg, The Netherlands/Budapest, Hungary.

de Baan, L., Alkemade, R., & Koellner, T. (2013). Land use impacts on
biodiversity in LCA: a global approach. International Journal of Life
Cycle Assessment, 18, 1216–1230. doi:10.1007/s11367-012-0412-0

Foley , J.A., et al. 2005. Global consequences of land use. Science 305:
570-574.

Foley, J.A., et al. 2011. Solutions for a cultivated planet. Nature 478:
337-342.

Mueller, N., et al. 2012. Closing yield gaps through nutrient and water
management. Nature 490: 254-257.

Phalan, B., A. Balmford, R.E. Green, J.P.W. Scharlemann. 2011.
Minimising the harm to biodiversity of producing more food globally.
Food Policy 36: S62-S71.

Ramankutty, N. and J.A. Foley. 1999. Estimating Historical Changes in
Global Land Cover: Croplands from 1700 to 1992, Global Biogeochemical
Cycles, 13 (4), 997-1027

Ramankutty, N., et al. 2008. Farming the planet: 1. Geographic
distribution of global agricultural lands in the year 2000. Global
Biogeochemical Cycles, Vol. 22, GB1003

Woodroffe, R., & Ginsberg, J. R. (1998). Edge Effects and the Extinction
of Populations Inside Protected Areas. Science, 280(5372), 2126–2128.
doi:10.1126/science.280.5372.2126
