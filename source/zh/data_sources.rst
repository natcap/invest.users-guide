.. _data_sources: 数据来源。

************
Data Sources数据来源
************

This is a compilation of data sources and suggestions for common model inputs. This list is not definitive and is only meant to serve as a starting point. It is highly recommended to look for more local and accurate data (from national, state, university, literature, NGO and other sources) and only use global data for final analyses if nothing more local is available. If you know of a useful data source not listed here, please share it on the forum. 这是一个数据来源的汇编和对常见模型输入数据的建议清单。这份清单不是确定的，只是作为一个起点。强烈建议寻找更多的本地的、准确的数据（来自国家、州、大学、文献、非政府组织和其他来源），如果没有更多的本地化数据，只能使用全球数据进行最终分析。如果你知道的有用的数据来源还未在这里列出，请在论坛上分享。

.. _dem:

Digital Elevation Model数字高程模型
-----------------------
A digital elevation model (DEM) is a raster map of elevation, where each pixel's value is its elevation above sea level (usually in meters). DEM data is available for any area of the world, although at varying resolutions. 数字高程模型（DEM）是一种高程栅格图，其中每个像素的值是其距离海平面以上的高程（通常以米为单位）。世界上任何地区都有DEM数据，尽管分辨率各不相同。

Free raw global DEM data is available from: 免费的全球DEM原始数据可从以下途径获得：

 * The World Wildlife Fund - https://www.worldwildlife.org/pages/hydrosheds世界野生动物基金会- https://www.worldwildlife.org/pages/hydrosheds
 * NASA: https://asterweb.jpl.nasa.gov/gdem.asp (30m resolution) 美国国家航空航天局: https://asterweb.jpl.nasa.gov/gdem.asp (30m分辨率); and easy access to SRTM data: http://dwtkns.com/srtm/航天飞机雷达地形测绘使命数据：http://dwtkns.com/srtm/
 * USGS: https://earthexplorer.usgs.gov/美国地质勘探局：https://earthexplorer.usgs.gov/

The DEM resolution may be a very important parameter depending on the project’s goals. For example, if decision makers need information about impacts of roads on ecosystem services then fine resolution is needed. The hydrological aspects of the DEM used in the model must be correct. Most raw DEM data has errors, so it's likely that the DEM will need to be filled to remove sinks. Multiple passes of the ArcGIS Fill tool, or QGIS Wang & Liu Fill algorithm (SAGA library) have shown good results. 根据项目目标的不同，DEM的分辨率可能是一个非常重要的参数。例如，如果决策者需要有关道路对生态系统服务影响的信息，那么就需要精细的分辨率。模型中使用的DEM的水文方面信息必须是正确的。大多数原始DEM数据都有误差，所以很可能需要对DEM进行填充以消除汇。ArcGIS的填充工具或QGIS的Wang & Liu填充算法（SAGA库）的多种处理方法都显示出良好的效果。 

For hydrological models that generate streams from the DEM, look closely at the stream network raster output. If streams are not continuous, but broken into pieces, the DEM still has sinks that need to be filled. If filling sinks multiple times does not create a continuous stream network, perhaps try a different DEM. If the results show an unexpected grid pattern, this may be due to reprojecting the DEM with a "nearest neighbor" interpolation method instead of "bilinear" or "cubic". In this case, go back to the raw DEM data and reproject using "bilinear" or "cubic".对于从DEM生成溪流的水文模型，仔细观察溪流网络栅格输出。如果溪流不是连续的，而是断成了几块，那么DEM仍然有需要填充的汇。如果多次填充汇不能形成一个连续的溪流网络，也许可以尝试另一种DEM。如果结果出现意料之外的栅格模式，这可能是由于用 "近邻 "插值方法而不是 用"双线性 "或 "立方体 "方法重新投影DEM造成的。在这种情况下，回到原始DEM数据，用 "双线性 "或 "立方体 "方法进行重新投影。

Also see the Working with the DEM section of this User Guide for more details and guidance about processing DEMs. 关于处理DEM的更多细节和指导，也请参考本用户指南的DEM工作部分。


.. _lulc:土地利用/土地覆盖

Land Use/Land Cover土地利用/土地覆盖
-------------------
Land use/land cover (LULC) describes the physical properties of the land and/or how people are using it (forest, wetland, water, paved, agricultural, nature preserve, etc.) In order to display the data in raster format, each LULC category is mapped to an integer code (these codes do not have to be consecutive or ordered). Unknown data gaps should be approximated where possible to avoid missing data (holes) in the output layers. 土地利用/土地覆盖（LULC）描述了土地的物理属性或人们的使用方式（森林、湿地、水、铺装、农业、自然保护区等）。为了以栅格格式显示数据，每个LULC类别被映射为一个整数代码（这些代码不必连续或有序）。未知的数据缺口应尽可能地进行近似处理，以避免输出层中出现数据缺失（漏洞）。

Global land use data is available from: 全球土地使用数据可从以下渠道获得：

 * NASA: https://lpdaac.usgs.gov/products/mcd12q1v006/ (MODIS multi-year global landcover data provided in several classifications) 美国国家航空航天局: https://lpdaac.usgs.gov/products/mcd12q1v006/（MODIS多年来提供的基于几种分类的全球土地覆盖数据）
 * The European Space Agency: http://www.esa-landcover-cci.org/ (Three global maps for the 2000, 2005 and 2010 epochs) 欧洲航天局：http://www.esa-landcover-cci.org/（2000年、2005年和2010年三个时期的全球土地覆盖地图）

Data for the U.S. is provided by the USGS and Department of the Interior via the National Land Cover Database: https://www.usgs.gov/centers/eros/science/national-land-cover-database 美国的数据是由美国地质调查局和内政部通过国家土地覆盖数据库提供的：https://www.usgs.gov/centers/eros/science/national-land-cover-database。

The simplest categorization of LULCs on the landscape involves delineation by land cover only (e.g., cropland, forest, grassland). Several global and regional land cover classifications are available (e.g., Anderson et al. 1976), and often detailed land cover classification has been done for the landscape of interest. Many countries have national LULC maps that can be used. 景观上最简单的土地利用/土地覆盖分类包括仅按土地覆盖物（例如，耕地、森林、草地）进行划分。有几种全球和区域性的土地覆被分类法（例如，Anderson等人，1976年），而且详细的土地覆被分类已被应用于相关的景观。许多国家都有可以使用的国家土地利用/土地覆盖地图。

A more sophisticated LULC classification involves breaking relevant LULC types into more meaningful types. For example, agricultural land classes could be broken up into different crop types. Forest could be broken up into specific species or age categories. Where data is available, you may stratify LULC types by variables, such as rainfall, temperature, elevation, etc., known to affect the properties being modeled. 一个更复杂的土地利用/土地覆盖分类是指将相关的土地利用/土地覆盖类型分成更有意义的类型。例如，农业用地类别可被分解为不同的作物类型。森林可以细分为特定的物种或年龄类别。在有数据支持的情况下，你可以按已知的影响建模属性的变量，如降雨、温度、海拔等，对土地利用/土地覆盖类型进行分层。

The categorization of land use types depends on the model and how much data is available for each of the land types. Typically, the biophysical table input maps certain relevant biophysical parameters to each LULC code. You should only break up a LULC type if it will provide more accuracy in modeling. For instance, only break up ‘crops’ into different crop types if you have information on the difference in relevant biophysical parameters. 土地利用类型的分类取决于使用的模型，以及每种土地类型的可用数据有多少。通常情况下，生物物理表输入将某些相关的生物物理参数映射到每个土地利用/土地覆盖代码。只有当一个土地利用/土地覆盖类型能够提供更高的建模精度时，你才应该将其分解。例如，只有在你有相关生物物理参数差异的信息时，才将 "农作物 "分解为不同的农作物类型。

*Sample Land Use/Land Cover Table*土地利用/土地覆盖样表

  ====== ===========================
  lucode Land Use/Land Cover lucode土地利用/土地覆盖
  ====== ===========================
  1      Evergreen Needleleaf Forest常绿针叶林
  2      Evergreen Broadleaf Forest常绿阔叶林
  3      Deciduous Needleleaf Forest落叶针叶林
  4      Deciduous Broadleaf Forest落叶阔叶林
  5      Mixed Cover ？？？
  6      Woodland林地
  7      Wooded Grassland ？？？
  8      Closed Shrubland封闭灌木丛
  9      Open Shrubland开阔灌木丛
  10     Grassland草原
  11     Cropland (row Crops)耕地（行栽作物）
  12     Bare Ground裸地
  13     Urban and Built-Up城市和建成区
  14     Wetland湿地
  15     Mixed evergreen ？？？
  16     Mixed Forest混交林
  17     Orchards/Vineyards果园/葡萄园
  18     Pasture牧草地
  ====== ===========================

.. _carbon_pools: 碳库：

Carbon Pools碳库
------------
Carbon storage data should be set equal to the average carbon storage values for each LULC class. The ideal data source for all carbon stocks is a set of local field estimates, where carbon storage for all relevant stocks has been directly measured. These can be summarized to the LULC map, including any stratification by age or other variable. If these data are not available, however, there are several general data sources that can be used. 碳储量数据应设定为等于每个土地利用/土地覆盖类型的平均碳储量值。所有碳储量的理想数据来源是一套当地的实地估计，其中所有相关储量的碳储量都已直接测量。这些数据可以汇总到土地利用/土地覆盖地图上，包括按年龄或其他变量进行分层的土地利用/土地覆盖。然而，如果没有这些数据，有几个一般的数据来源可以使用。

Note that several sources, including IPCC (2006), report in units of biomass, while InVEST uses mass of elemental carbon. To convert metric tons of biomass to metric tons of C, multiply by a conversion factor, which varies typically from 0.43 to 0.51. Conversion factors for different major tree types and climatic regions are listed in Table 4.3 on page 4.48 of IPCC (2006). 请注意，包括IPCC（2006）在内的一些数据来源是以生物量为单位进行报告的，而InVEST则使用元素碳的质量。要将公吨的生物量转换为公吨的碳，需要乘以一个转换系数，该系数通常在0.43到0.51之间变化。IPCC (2006)第4.48页的表4.3中列出了不同主要树木类型和气候区域的转换系数。

.. _aboveground_carbon: 地上碳

Carbon Stored in Aboveground Biomass地上生物量中储存的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A good but very general source of data for carbon storage is the Intergovernmental Panel on Climate Change's (IPCC) 2006 methodology for determining greenhouse gas inventories in the Agriculture, Forestry and Other Land Use (AFOLU) sector (https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html). To use this set of information from the IPCC, you must know your site's climate domain and region; use data from Table 4.1 on page 4.46 and a digital copy of the Food and Agriculture Organization of the United Nations' (FAO) eco-region map (http://www.fao.org/geonetwork/srv/en/main.home) to figure that out. Tables 5.1 through 5.3 (p. 5.9) of IPCC (2006) give estimates for aboveground biomass in agriculture land with perennial woody biomass (e.g., fruit orchards, agroforestry, etc.). Tables 4.7, 4.8, and 4.12 give aboveground biomass estimates for natural and plantation forest types. Ruesch and Gibbs (2008) mapped the IPCC (2006) aboveground biomass carbon storage data given year 2000 land cover data, which can be accessed here: https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html. 政府间气候变化专门委员会（IPCC）2006年确定的农业、林业和其他土地利用（AFOLU）部门温室气体清单的方法（https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html）是一个很好但非常普遍的碳储存数据来源。要使用IPCC的这组信息，你必须知道你所在地的气候区和区域；使用第4.46页表4.1的数据和联合国粮食及农业组织（FAO）生态区域图的数字拷贝（http://www.fao.org/geonetwork/srv/en/main.home）来计算。IPCC (2006)的表5.1至5.3 (第5.9页)给出了具有多年木质生物量的农业用地(如果园、农林业等)的地上生物量估算值。表4.7、4.8和4.12给出了天然林和人工林类型的地上生物量估算值。Ruesch和Gibbs（2008）根据2000年的土地覆盖数据，绘制了IPCC（2006）地上生物量碳储存数据，可在以下地址访问获取：https://cdiac.essdive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html。

Other general sources of carbon storage estimates can be found. For example, Grace et al. (2006) estimate the average aboveground carbon storage (leaf + wood) for major savanna ecosystems around the world (Table 1). Houghton (2005) gives aboveground carbon storage for natural and plantation forest types, by continent (Tables 1 and 3). Brown et al. (1989) give aboveground biomass estimates for tropical broadleaf forests as a function of land-use: undisturbed, logged and nonproductive (Table 7). Region-specific sources of carbon storage data are also available. Those we've found include: 也可以参考其他一般的碳储存估算数据来源。例如，Grace等人（2006）估计了全球主要热带草原生态系统的平均地上碳储量（叶+木）（表1）。Houghton (2005)给出了各大洲天然和人工林类型的地上碳储量（表1和表3）。Brown等人（1989年）给出了热带阔叶林的地上生物量估算值，作为土地利用的功能：未受干扰、伐木和非生产性（表7）。特定地区的碳储存数据来源也是可用的。我们发现的数据包括：

* Latin America: Malhi et al. (2006) report aboveground biomass volumes for 227 lowland forest plots in Bolivia, Brazil, Colombia, Ecuador, French Guinea, Guyana, Panama, Peru, and Venezuela. Nascimento and Laurance (2002) estimate aboveground carbon stocks in twenty 1-ha plots of Amazonian rainforest. Tiessen et al. (1998) find aboveground carbon stocks for the Brazilian savanna types Caatingas and Cerrados. 拉丁美洲：Malhi等人（2006）报告了玻利维亚、巴西、哥伦比亚、厄瓜多尔、法属几内亚、圭亚那、巴拿马、秘鲁和委内瑞拉227块低地森林的地上生物量。Nascimento和Laurance(2002)估计了亚马逊雨林中20个1公顷地块的地上碳储量。Tiessen等人（1998年）发现巴西热带雨林类型卡廷加群落和塞拉多群落的地上碳储量。

* Africa: Zhang and Justice (2001) report aboveground carbon stocks for major forest and shrub LULC types for central African countries. Tiessen et al. (1998) estimates total aboveground biomass of degraded savanna in Senegal. Makundi (2001) reports mean annual incremental growth for three forest plantation types in Tanzania. Malimbwi et al. (1994) estimates aboveground carbon stocks in the miombo woodlands of Kitungalo Forest Reserve Tanzania. Munishi and Shear (2004) report aboveground carbon stocks in the Afromontane rain forests of the Eastern Arc Mountains of Tanzania. Glenday (2006) estimates aboveground carbon stocks for 3 forest types in the Kakamega National Forest of western Kenya.非洲：Zhang和Justice (2001) 报告了中部非洲国家主要森林和灌木土地利用/土地覆盖类型的地上碳储量。Tiessen等人(1998)估计了塞内加尔退化的热带稀树草原的地上生物量总量。Makundi (2001) 报告了坦桑尼亚三种森林种植类型的平均年增量。Malimbwi等人(1994)估计了坦桑尼亚Kitungalo森林保护区的miombo林地的地上碳储量。Munishi和Shear (2004)报告了坦桑尼亚东弧形山的非洲山地雨林的地上碳储量。Glenday (2006)估计了肯尼亚西部Kakamega国家森林的三种森林类型的地上碳储量。

* North America: Smith et al. (2006) estimate aboveground carbon stocks for all major forest types in the US. 北美洲：Smith等人(2006)估计美国所有主要森林类型的地上碳储量。

* The Carbon On Line Estimator (https://www.ncasi.org/resource/carbon-on-line-estimator-cole/) is a tool for calculating carbon characteristics in U.S. forests based on USDA Forest Service Forest Inventory & Analysis and Resource Planning Assessment data. With this tool, carbon characteristics can be examined at the scale of counties. Using the variables tab, aboveground, belowground, soil, or dead wood carbon pools can be selected. 碳在线评估器（https://www.ncasi.org/resource/carbon-on-line-estimator-cole/）是一个基于美国农业部森林局森林资源清查与分析数据和资源规划评估数据的计算美国森林碳特征的工具。通过这个工具，可以在县的尺度范围内检验碳特征。使用变量标签，可以选择地上、地下、土壤或枯木碳库。

* Coomes et al. (2002) estimate aboveground carbon stocks for native shrubland and forest types in New Zealand. Coomes等人(2002)估计了新西兰本地灌木丛和森林类型的地上碳储量。

Aboveground biomass (and therefore carbon stocks) can also be calculated from timber inventories, which are often done by forestry ministries on a set of plots. Use the following formula to estimate the aboveground carbon stock in a forest stand that has been inventoried for its merchantable volume where VOB is the per-hectare volume of trees in cubic meters measured from tree stump to crown point (the merchantable portion of the tree), WD is the wood density of trees (dry biomass per unit of tree volume), BEF is the ratio of total aboveground dry biomass to dry biomass of inventoried volume, and CF is the ratio of elemental carbon to dry biomass, by mass (Brown 1997). The biomass expansion factor (BEF) accounts for C stored in all other portions of the tree aboveground (e.g., branches, bark, stems, foliage, etc; the non-merchantable portions of the tree). In most cases WD for a plot is approximated with values for dominant species. Brown (1997) provides a table of WD values for many tree species in Appendix 1 of section 3 and a method for calculating BEF (Equation 3.1.4). See ECCM (2007) for an application of this FAO method to forest inventory data from eastern Tanzania. IPCC (2006) also presents estimates of ( ) where BEF values for hardwood, pine, conifer, and natural forest stands by eco-region are given in Table 4.5 and WD values for many species are given in Tables 4.13 and 4.14. (Use the BCEF values in Table 4.5 that are subscripted by S.) Finally, Brown et al. (1989) give BEF for tropical broadleaf forests under three land uses: undisturbed, logged, and nonproductive. 地上生物量（也就是碳储量）也可以通过木材清查来计算，这通常是由林业部门在一组地块上进行的。使用下面的公式来估计已经清查了可销售量的林分的地上碳储量，其中VOB是指从树桩到树冠点（树木的可销售部分）测量的每公顷树木体积，单位为立方米；WD是树木的木材密度（每单位树木体积的干生物量）；BEF是地上干生物量总量与清查量的干生物量的比率；CF是元素碳与干生物量的比率，按质量计算（Brown 1997）。生物量扩展因子（BEF）考虑了储存在树木地上所有其他部分（如树枝、树皮、树茎、树叶等；树木的非商业部分）的碳。在大多数情况下，一个小区的WD是用优势物种的数值来近似计算的。Brown (1997) 在第3节的附录1中提供了许多树种的WD值表，以及计算BEF的方法(公式3.1.4)。参考ECCM (2007)，了解粮农组织这一方法在坦桑尼亚东部森林库存数据中的应用。IPCC (2006) 还提出了( )的估计值，其中表4.5给出了按生态区域划分的硬木、松树、针叶树和天然林的BEF值，表4.13和4.14给出了许多物种的WD值。(使用表4.5中以S为下标的BCEF值）最后，Brown等人（1989年）给出了热带阔叶林在三种土地利用类型下的BEF：未受干扰、伐木和非生产性。

Brown (1997) attaches several caveats to the use of the above equation. First, the equation is designed for inventoried stands that are closed as opposed to open (forests with sparser canopy coverage such as oak savanna). Second, VOB estimates should be a function of all tree species found in the stand, not just the economically most valuable wood. Third, trees with diameters as low as 10 centimeters at breast height (DBH = 10) need to be included in the inventory if this aboveground biomass carbon equation is to be as accurate as possible. Brown (2002) also notes that the use of a single BEF value is a simplification of the actual biomass growth process. 布朗(1997)对使用上述公式提出了一些建议。首先，该等式是为封闭式而非开放式(树冠覆盖较稀疏的森林，如橡树草原)的库存林分设计的。第二，VOB估算应该是林分中所有树种的函数，而不仅仅是经济上最有价值的木材。第三，如果要使这个地上生物量碳方程尽可能准确，胸高低至10厘米（DBH=10）的树木需要包括在清单中。Brown (2002) 还指出，使用单一的BEF值是对实际生物量增长过程的简化。

These caveats lead Brown (2002) to recommend the use of allometric biomass equations to estimate woody aboveground biomass if available. These equations give the estimated relationship between a stand's distribution of different-sized trees and the stand's aboveground biomass. Brown (1997) and Brown and Schroeder (1999) provide general aboveground biomass allometric equations for all global eco-regions and the eastern US, respectively. Cairns et al. (2000) provide aboveground biomass allometric equations for LULC types in southern Mexico. Nascimento and Laurance (2002) estimate Amazonian rainforest aboveground biomass using allometric curves. The use of these equations requires knowledge of the distribution of tree size in a given stand. 基于以上的这些注意事项，Brown(2002)建议如果可以则使用异速生物量方程来估计木质地上生物量。这些方程给出了一个林分不同大小的树木分布与林分地上生物量之间的估计关系。Brown(1997)和Brown和Schroeder(1999)分别为全球所有生态区域和美国东部提供了一般的地上生物量异速方程。Cairns等人(2000)提供墨西哥南部土地利用/土地覆盖类型的地上生物量异速方程。Nascimento和Laurance(2002)使用异速曲线估计亚马逊雨林的地上生物量。使用这些方程需要了解特定林分中的树木大小分布。

Some researchers have made use of these equations a bit easier by first relating a stand's distribution of different-sized trees to its age and then mapping the relationship between age and aboveground biomass (i.e., ). For example, Silver et al. (2000) have estimated aboveground biomass as a function of stand age (i.e., years since afforestation/reforestation) or previous LULC for native forest types in tropical ecosystems. Smith et al. (2006) take the transformation of allometric equations one step further by relating age to total biomass carbon (belowground plus aboveground) directly for various US forests. 一些研究人员使这些方程的使用更容易一些，他们首先将一个林分的不同大小的树木分布与它的年龄联系起来，然后绘制出年龄和地上生物量（即）之间的关系。例如，Silver等人(2000)估计了地上生物量与林分年龄(即造林/重新再造林以来的年份)或热带生态系统中原生森林类型的原有土地利用/土地覆盖的关系。Smith等人(2006)通过将美国各种森林的年龄与总生物量碳(地下加地上)直接联系起来，使异速运动方程的转换更进一步。

When using IPCC data or other similar broad data sources, one final issue to consider is how the level of anthropogenic disturbance affects carbon stocks. The aboveground C stock of highly disturbed areas will likely be lower than the stocks of undisturbed areas. It is not clear what type of disturbance levels IPCC or other such sources assume when reporting aboveground biomass estimates. If forest disturbance is an issue in the demonstration site, LULC types should be stratified by levels of disturbance. For an example of such stratification see Table 2.5, page 14 of ECCM (2007). 在使用IPCC数据或其他类似的广泛数据来源时，需要考虑的最后一个问题是人为干扰的程度如何影响碳储量。高度扰动地区的地面碳储量可能会低于未扰动地区的储量。目前还不清楚IPCC或其他此类资料来源在给出地上生物量估计值时假设的干扰水平是什么类型。如果森林干扰是示范点的一个问题，土地利用/土地覆盖类型应按干扰程度进行分层。这种分层的例子见 ECCM (2007) 第 14 页的表 2.5。

Finally, we generally do not treat aboveground herbaceous material as a carbon pool (e.g., grass, flowers, non-woody crops). Our working assumption is that this material does not represent a potential source of long-term storage like woody biomass, belowground biomass, and soil. Herbaceous material in general recycles its carbon too quickly. 最后，我们一般不把地上的草本材料作为一个碳库（如草、花、非木质作物）。我们的工作认为，这种材料并不像木质生物量、地下生物量和土壤那样是长期储存的潜在来源。一般来说，草质材料的碳循环速度太快。

.. _belowground_biomass:地下生物量

Carbon Stored in Belowground Biomass地下生物量中储存的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For LULC categories dominated by woody biomass, belowground biomass can be estimated roughly with the "root to shoot" ratio of belowground to aboveground biomass. Default estimates of the root to shoot ratio are given in Table 4.4 on p. 4.49 of IPCC (2006) by eco-region. Broad estimates of this ratio are also given in Section 3.5 of Brown (1997). 对于以木质生物量为主的土地利用/土地覆盖类别，地下生物量可通过地下生物量与地上生物量的 "根茎比"来大致估算。IPCC (2006)第4.49页的表4.4按生态区域给出了"根茎比"的默认估计。Brown (1997)的第3.5节中也给出了这一比率的大致估计。

Some LULC types contain little to no woody biomass but substantial belowground carbon stocks (e.g., natural grasslands, managed grasslands, steppes, and scrub/shrub areas). In these cases the root to shoot ratio described above does not apply. Belowground estimates for these LULC types are best estimated locally, but if local data are not available some global estimates can be used. The IPCC (2006) lists total biomass (aboveground plus belowground) and aboveground biomass for each climate zone in table 6.4 (p. 6.27). The difference between these numbers is a crude estimate of belowground biomass. . Recently, Ruesch and Gibbs (2008) mapped the IPCC (2006) aboveground biomass carbon storage data given year 2000 land cover data, which can be accessed here: https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html. 一些土地利用/土地覆盖类型几乎不包含木质生物量，但包含大量的地下碳储量（如天然草原、人工管理草原、大草原和灌丛/灌木丛区）。在这些情况下，上述的"根茎比"并不适用。这些土地利用与土地覆盖类型的地下估算值最好采用当地数据，但如果当地数据不可用，可以使用一些全球估算值。IPCC（2006）在表6.4（第6.27页）中列出了每个气候区的总生物量（地上加地下）和地上生物量。这些数字之间的差异是对地下生物量的粗略估计。最近，Ruesch和Gibbs（2008年）根据2000年的土地覆盖数据，绘制了IPCC（2006年）的地上生物量碳储存数据，可以通过以下链接访问：https://cdiac.essdive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html。

Several studies have compiled estimates of belowground biomass or root-to-shoot ratios for different habitat types. Among those we found: 一些研究对不同生境类型的地下生物量或根茎比的估计进行了总结。在这些研究中，我们发现：

* Grace et al. (2006) estimate the total average woody and herbaceous root biomass for major savanna ecosystems around the world (Table 1). Baer et al. (2002) and Tilman et al. (2006) estimate the C stored in the roots of plots restored to native C4 grasses in Nebraska and Minnesota, U.S. respectively, as a function of years since restoration (see Table 2 in Baer et al. (2002) and Figure 1D in Tilman et al. (2006)). Grace等人(2006)估计了全世界主要热带草原生态系统的平均木质和草质根系生物量总量(表1)。Baer等人(2002)和Tilman等人(2006)分别估计了在美国内布拉斯加州和明尼苏达州恢复为本地C4草的地块根部储存的C，作为植被恢复后的变量(见Baer等人(2002)的表2和Tilman等人(2006)的图1D)。

* Cairns et al. (1997) survey root-to-shoot ratios for LULC types across the world. Munishi and Shear (2004) use a ratio of 0.22 for Afromontane forests in the Eastern Arc forests of Tanzania. Malimbwi et al. (1994) use 0.20 for miombo woodlands in the same area of Tanzania. Coomes et al. (2002) use 0.25 for shrublands in New Zealand. Gaston et al. (1998) report a root-to-shoot ratio of 1 for African grass / shrub savannas. Cairns等人(1997)调查了世界各地土地利用/土地覆盖类型的根茎比率。Munishi和Shear(2004)在对坦桑尼亚东弧形森林的非洲山地森林的研究中使用了0.22的根茎比率。Malimbwi等人(1994)对坦桑尼亚同一地区的miombo林地进行研究时使用0.20的根茎比率。Coomes等人(2002)对新西兰的灌木地使用0.25的根茎比率。Gaston等人(1998)报告中发现，非洲草/灌木稀树草原的根茎比率为1。

.. _soil_carbon:土壤碳

Carbon Stored in Soil土壤中存储的碳
^^^^^^^^^^^^^^^^^^^^^

If local or regional soil C estimates are not available, default estimates can be looked up from IPCC (2006) for agricultural, pasture, and managed grasslands. Table 2.3 of IPCC (2006) contains estimates of soil carbon stocks by soil type, assuming these stocks are at equilibrium and have no active land management. For cropland and grassland LULC types, this default estimate can be multiplied by management factors, listed in Tables 5.5 and 6.2 of IPCC (2006). For all other LULC types and their related management schemes, the IPCC (2006) assumes no management factors. 如果没有当地或地区的土壤碳估计值，可以从IPCC（2006）中查询农业、牧场和人工管理草原的默认估计值。IPCC（2006）的表2.3包含了按土壤类型划分的土壤碳储量估计值，假设这些储量处于平衡状态，没有积极的土地管理。对于耕地和草地土地利用/土地覆盖类型，这一默认估计值可乘以IPCC（2006）表5.5和6.2所列的管理因素。对于所有其他土地利用/土地覆盖类型及其相关管理方案，IPCC (2006) 假设没有管理因素。

There are alternative global-level sources of soil carbon data. Post et al. (1982) report carbon stocks in the first meter of soil by Holdridge Life Zone Classification System (GIS map of these Zones available at http://www.arcgis.com/home/item.html?id=f3ec7241777f4c56a69ae14d2a98e44b). Silver et al. (2000) have estimated soil carbon as a function of years since afforestation/reforestation for native forest types in tropical ecosystems. Grace et al. (2006) estimate the soil carbon for major savanna types around the world (Table 1). Detwiler (1986) lists soil carbon for tropical forest soils in Table 2. 也有其他的全球层面的土壤碳数据来源。Post等人（1982年）按照Holdridge生命区分类系统报告了土壤1m深中的碳储量（这些生命区的GIS地图可在以下链接中获取：http://www.arcgis.com/home/item.html?id=f3ec7241777f4c56a69ae14d2a98e44b）。Silver等人(2000)估计了热带生态系统中原生森林类型的土壤碳与造林/再造林后年限的关系。Grace等人（2006）估计了世界各地主要热带草原类型的土壤碳（表1）。Detwiler（1986）在表2中列出了热带森林土壤的土壤碳。

Several region-specific studies also report soil carbon stocks. Those we've found include: 一些针对特定区域的研究也报告了土壤碳储量。我们发现的这些研究包括：

* North America: Smith et al. (2006) estimate soil C for every 5-year increment up to 125 years since afforestation/reforestation for all major forest types and forest management practices in each region of the U.S. Others include McLauchlan et al. (2006); Tilman et al. (2006); Fargione et al (2008); Schuman et al. (2002); and Lal (2002). 北美洲：Smith等人(2006)对美国各地区所有主要森林类型和森林管理方法的造林/再造林以来每5年的增量进行了土壤碳的估算，最长可达125年。其他包括McLauchlan等人（2006）；Tilman等人（2006）；Fargione等人（2008）；Schuman等人（2002）；和Lal（2002）。

* Africa: Houghton and Hackler (2006) give soil C for 5 LULC forest types (Rain Forest; Moist Forest Dry; Forest; Shrubland; and Montane Forest) in sub-Saharan Africa that have retained their natural cover and for forest areas that have been converted to croplands, shifting cultivation, and pasture. Vagen et al. (2005) provides soil C estimates for various LULC types in sub-Saharan Africa. 非洲：Houghton 和 Hackler (2006) 提供了撒哈拉以南非洲 5 种土地利用/土地覆盖森林类型（雨林、湿润森林、森林、灌木丛和山地森林）的土壤碳，这些森林类型保留了其自然覆盖，而森林地区则被转化为耕地、轮垦和牧场。Vagen等人（2005）提供了撒哈拉以南非洲各种土地利用/土地覆盖类型的土壤碳估算值。

* South America: Bernoux et al. (2002) estimated soil C stocks to a depth of 30 cm for different soil type-vegetation associations in Brazil. For example, the soil C stock in HAC soils under 14 different land cover categories, including Amazon forest and Brazilian Cerrado, range from 2 to 116 kg C m-2. 南美洲。Bernoux等人（2002年）估计了巴西不同土壤类型-植被搭配下30厘米深处的土壤碳储量。例如，在14个不同的土地覆盖类别下，包括亚马逊森林和巴西塞拉多，HAC土壤的土壤C储量从2到116kgCm-2不等。

Important Note: In most research that estimates carbon storage and sequestration rates on a landscape, soil pool measures only include soil organic carbon (SOC) in mineral soils (Post and Kwon 2000). However, if the ecosystem being modeled has a lot of organic soils (e.g. wetlands or paramo), it is critical to add this component to the mineral soil content. In landscapes where the conversion of wetlands into other land uses is common, carbon releases from organic soils should also be tracked closely (IPCC 2006). 重要提示：在大多数估计景观上的碳储存和封存率的研究中，土壤库的测量只包括矿物土壤中的土壤有机碳（SOC）（Post 和 Kwon，2000）。然而，如果被模拟的生态系统有大量的有机土壤（如湿地或帕拉莫），那么将这部分内容加入到矿物土壤的含量中是至关重要的。在湿地转化为其它土地用途很常见的景观中，也应密切跟踪有机土壤的碳释放（IPCC 2006）。

.. _dead_carbon:死碳

Carbon Stored in Dead Organic Matter储存在死亡有机物中的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If local or regional estimates of carbon stored in dead organic matter aren't available, default values from the IPCC (2006) can be assigned. Table 2.2 (p. 2.27) gives default carbon stocks for leaf litter in forested LULC types. For non-forested types, litter is close to 0. Grace et al. (2006) estimate the average carbon stored in litter for major savanna ecosystems around the world (Table 1). It is not clear if their total "above-ground biomass" estimates include deadwood or not. Deadwood stocks are more difficult to estimate in general, and we have located no default data sources. 如果当地或区域对死亡有机物中储存的碳没有估计值，则可以参考IPCC（2006）中的默认值。表2.2（第2.27页）给出了森林土地利用/土地覆盖类型中落叶的默认碳储量。对于非林地类型，枯落物接近于0。Grace等人(2006)估计了世界上主要热带草原生态系统的平均碳储存量(表1)。目前还不清楚他们对 "地上生物量 "的总估计值是否包括枯木。一般来说，枯木碳库存更难估计，我们没有找到默认的数据来源。

Regional estimates:区域性的估算值

* United States: Smith et al. (2006) estimate carbon storage in litter (referred to as "Forest Floor" C in the document) and dead wood (the aggregate of C pools referred to as "Standing Dead Trees" and "Down Dead Wood" in the document) for all major forest types and forest management practices in each region of the U.S. as a function of stand age. 美国：Smith等人(2006)估计了美国各地区所有主要森林类型和森林经营方式的落叶(文件中称为 "森林地面 "碳)和枯木(文件中称为 "立枯树 "和 "倒枯木 "的碳库总量)中的碳储存量，作为林分年龄的函数。

* South America: Delaney et al. (1998) estimate carbon stored in standing and down dead wood in 6 tropical forests of Venezuela. According to the authors, deadwood is typically 1/10 the amount of biomass as aboveground vegetation. 南美洲。Delaney等人(1998)估计了委内瑞拉6个热带森林的立木和枯木中的碳储存量。据作者估算，枯木的生物量通常是地上植被的1/10。



Precipitation降水量
-------------

.. _precipitation:降水量

Annual & Monthly Precipitation年度和月度降水量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Precipitation may be interpolated from long-term rain gauge point data. When considering rain gauge data, make sure that they provide good coverage over the area of interest, especially if there are large changes in elevation that cause precipitation amounts to be heterogeneous within the study area. Ideally, the gauges will have at least 10 years of continuous data, with no large gaps, around the same time period as the land use/land cover map used as input. Precipitation as snow should be included. 降水量可以从长期的雨量计点数据中插值d得到。在考虑雨量计数据时，要确保它们能很好地覆盖案例地区，特别是如果有很大的海拔变化，导致研究区域内的降水量不均一时。理想的情况是，测量仪至少有10年的连续数据，且没有大的差距，并与作为输入数据的土地利用/土地覆盖图的时间段相同。降水为雪的情况也应考虑在内。

Global data sets from remote sensing models can account for remote areas if field data are not available. You can use coarse data from the freely available global data sets developed by the Climatic Research Unit: http://www.cru.uea.ac.uk or WorldClim: https://www.worldclim.org/.如果没有实地监测数据，来自遥感模型的全球数据集也可以反映偏远地区的情况。你可以使用由气候研究室开发的免费提供的全球数据集的粗略数据：http://www.cru.uea.ac.uk 或WorldClim：https://www.worldclim.org/。

Within the United States, the PRISM group at Oregon State University provides free precipitation data at a 30-arcsecond resolution. See their website at https://prism.oregonstate.edu/ and navigate to '800m Normals' to download data. 在美国，俄勒冈州立大学的PRISM小组免费提供30弧度的降水数据。可登录他们的网站https://prism.oregonstate.edu/，并导航到 "800米正常值 "来下载数据。

.. _rain_events:降雨事件

Rain Events降雨事件
^^^^^^^^^^^
The average number of monthly rain events can be obtained from local climate statistics (Bureau of Meteorology) or online resources: 每月的平均雨量可以从当地的气候统计部门（气象局）或网上资源获得：

 * https://www.yr.no/
 * http://wcatlas.iwmi.org
 * The World Bank also provides maps with precipitation statistics: https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api世界银行还提供了带有降水统计数据的地图：https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api


Evapotranspiration蒸散量
------------------

.. _et0: 蒸散量

Reference Evapotranspiration参考蒸散量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Reference evapotranspiration, ET₀, measures the amount of water that vaporizes from land into the air over a given period of time. It is the sum of evaporation (directly off of soil, bodies of water, and other surfaces) and transpiration (through plants). It is typically expressed as a depth of water in millimeters per unit time: :math:`mm/month` for monthly, :math:`mm/year` for annual. (Note: similar to precipitation, this is the "depth" of water that evapotranspirates from a given region; it is not "per" pixel, square meter, or any other area unit). InVEST models all use this measure, but some sources express evapotranspiration as a volume or energy per area. See http://www.fao.org/3/x0490e/x0490e04.htm for more details. 参考蒸发量，ET₀，是衡量在一定时期内从土地上蒸发到空气中的水量。它是蒸发（直接从土壤、水体和其他表面）和蒸腾（通过植物）的总和。它通常表示为单位时间内水的深度，单位是毫米。math:`mm/month`代表月度，:math:`mm/year`代表年度。(注意：与降水类似，这是从特定区域蒸发的水的 "深度"；它不是 "每 "像素、平方米或任何其他面积单位）。InVEST模型都使用这种测量方法，但有些数据将蒸发量表示为每面积的体积或能量。

CGIAR provides a global map of potential evapotranspiration, based on WorldClim climate data, which may be used for reference ET: https://cgiarcsi.community/data/global-aridity-and-pet-database/.国际农业研究磋商组织CGIAR提供了基于WorldClim气候数据的全球潜在蒸散量图，可用于参考蒸发量：https://cgiarcsi.community/data/global-aridity-and-pet-database/。

If you are running a model that requires both precipitation and evapotranspiration as inputs, make sure that the ET data is based on the same precipitation data that is being used as a model input. 如果你正在运行一个同时需要降水和蒸散量作为输入数据的模型，请确保蒸散量数据是基于被用作模型输入数据的同一降水数据。

Reference evapotranspiration varies with elevation, latitude, humidity, and slope aspect. There are many methodologies, which range in data requirements and precision. 参考蒸散量随海拔高度、纬度、湿度和坡度的变化而变化。有许多计算方法，这些方法在数据要求和精度上有差异。
You can calculate reference ET by developing monthly average grids of precipitation, and maximum and minimum temperatures. These data can come from weather stations, where you can follow the same process as the development of the average annual precipitation grid, including incorporating the effects of elevation when interpolating between stations. Or, both WorldClim and CRU provide monthly temperature data already in grid format. These monthly grids can be used as input to the equations listed below. 你可以利用月平均降水、最高和最低温度的栅格数据来计算参考蒸散量。这些数据可以来自气象站，在那里你可以遵循与开发年平均降水栅格相同的过程，包括在站点之间内插时考虑海拔的影响。或者，WorldClim和CRU都提供已经是栅格格式的月度温度数据。这些月度栅格可以作为下面列出的方程式的输入数据。
You can calculate reference ET by developing monthly average grids of precipitation, and maximum and minimum temperatures (also available from WorldClim and CRU) which need to incorporate the effects of elevation when interpolating from observation stations. Data to develop these monthly precipitation and temperature grids follow the same process in the development of the 'Monthly Precipitation' grids. 你可以利用月平均降水、最高和最低温度（也可从WorldClim和CRU获得）的栅格数据来计算参考蒸散量，在从观测站点之间内插时需要考虑海拔的影响。制作这些月度降水和温度栅格的数据，与制作 "月度降水 "栅格的过程相同。

A simple way to determine reference evapotranspiration is the 'modified Hargreaves' equation (Droogers and Allen, 2002), which generates superior results than the Pennman-Montieth when information is uncertain. 确定参考蒸散量的一个简单方法是 "修正的哈格里夫斯 "方程（Droogers和Allen，2002），当信息不确定时，它产生的结果比Pennman-Montieth更优。

.. math:: ET_0 = 0.0013\times 0.408\times RA\times (T_{av}+17)\times (TD-0.0123 P)^{0.76}

The 'modified Hargreaves' method uses the average of the mean daily maximum and mean daily minimum temperatures for each month (`Tavg` in degrees Celsius), the difference between mean daily maximum and mean daily minimums for each month (`TD`), extraterrestrial radiation (:math:`RA` in :math:`\mathrm{MJm^{-2}d^{-1}}`) and precipitation (:math:`P` in mm per month), all of which can be relatively easily obtained. Temperature and precipitation data are often available from regional charts, direct measurement or national or global datasets. Radiation data, on the other hand, is far more expensive to measure directly but can be reliably estimated from online tools, tables or equations. FAO Irrigation Drainage Paper 56 (Allan (1998)) provides monthly radiation data in Annex 2. Select values for the latitude closest to your area of study. Another option is to use a GIS tool to calculate solar radiation for your specific study area, and use this spatial layer as input to the Modified Hargreaves calculation. 修改后的哈格里夫斯方法使用每个月的平均每日最高温度和平均每日最低温度的平均值（`Tavg`，摄氏度），每个月的平均每日最高温度和平均每日最低温度之差（`TD`），地外辐射(:math:`RA` in :math:`\mathrm{MJm^{-2}d^{-1}}`)和降水(:math:`P` in mm per month)，所有这些数据都可以比较容易获得。温度和降水数据通常可以从区域图表、直接测量或国家或全球数据集中获得。另一方面，辐射数据的直接测量成本要高得多，但可以通过在线工具、表格或方程式进行可靠的估算。粮农组织第56号灌溉排水文件（Allan（1998））在附件2中提供了月度辐射数据。选择与你的研究区域最接近的纬度的数值。另一个选择是使用GIS工具来计算你的特定研究区域的太阳辐射，并使用该空间图层作为修正哈格里夫斯计算的输入数据。

The reference evapotranspiration can also be calculated monthly and annually using the Hamon equation (Hamon 1961, Wolock and McCabe 1999): 参考蒸散量也可以用Hamon方程按月和按年计算（Hamon 1961, Wolock and McCabe 1999）：

.. math:: PED_{Hamon} = 13.97 d D^2W_t

where :math:`d` is the number of days in a month, :math:`D` is the mean monthly hours of daylight calculated for each year (in units of 12 hours), and :math:`W_t` is a saturated water vapor density term calculated by:式中：math:`d`是一个月的天数，:math:`D`是每年计算的月平均日照时间（单位为12小时），:math:`W_t`是饱和水蒸气密度，计算方法如下：

.. math:: W_t = \frac{4.95e^{0.062 T}}{100}

where :math:`T` is the monthly mean temperature in degrees Celsius. Reference evapotranspiration is set to zero when mean monthly temperature is below zero. Then for each year during the time period analyzed, the monthly calculated PET values at each grid cell are summed to calculate a map of the annual PET for each year.式中：:math:`T`是月平均温度，摄氏度。当月平均温度低于零时，参考蒸散量被设置为零。然后对于分析的时间段内的每一年，将每个栅格像元的月度计算PET值相加，计算出每一年的年度PET图层。

A final method to assess ETo, when pan evaporation data are available, is to use the following equation: 在有pan evaporation数据的情况下，评估参考蒸散量的最后一种方法是使用以下公式：
:math:`ETo = pan ET *0.7` (Allen et al., 1998)

.. _kc:

Crop Evapotranspiration Coefficient农作物蒸散系数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Evapotranspiration coefficient ( :math:`K_c`) values for crops are readily available from irrigation and horticulture handbooks. FAO has an online resource for this: http://www.fao.org/3/X0490E/x0490e0b.htm. The FAO tables list coefficients by crop growth stage (:math:`K_c` ini, :math:`K_c` mid, :math:`K_c` end), which need to be converted to an annual average or monthly average (depending on the model) :math:`K_c`. This requires knowledge about the phenology of the vegetation in the study region (average green-up, die-down dates) and crop growth stages (when annual crops are planted and harvested). Annual average :math:`K_c` can be estimated as a function of vegetation characteristics and average monthly reference evapotranspiration using the following equation: 农作物的蒸散系数（ :math:`K_c`）值很容易从灌溉和园艺手册中获得。粮农组织对此有一个在线资源：http://www.fao.org/3/X0490E/x0490e0b.htm。粮农组织的表格按作物生长阶段列出了系数(:math:`K_c` ini, :math:`K_c` mid, :math:`K_c` end)，需要转换为年平均或月平均（取决于模型）:math:`K_c`。这需要了解研究区域植被的物候学（平均绿化、枯萎日期）和作物生长阶段（每年作物的种植和收获时间）。

.. math:: K_c = \frac{\sum^{12}_{m=1}K_{cm}\times ET_{o_m}}{\sum^{12}_{m=1}ET_{o_m}}

where :math:`K_{cm}` is an average crop coefficient of month :math:`m` (1-12) and :math:`ET_{o_m}` is the corresponding reference evapotranspiration. These values can also be calculated using the following spreadsheet: https://naturalcapitalproject.stanford.edu/sites/g/files/sbiybj9321/f/kc_calculator.xlsx. Values for :math:`K_c` should be decimals between 0-1.5. 式中 : math:`K_{cm}`是:math:`m`（1-12）月份的平均作物系数，: math:`ET_{o_m}`是相应的参考蒸散量。这些数值也可以用以下电子表格来计算：https://naturalcapitalproject.stanford.edu/sites/g/files/sbiybj9321/f/kc_calculator.xlsx。:math:`K_c`的值应该是0-1.5之间的小数。

Values for other vegetation types can be estimated using Leaf Area Index (LAI) relationships. LAI characterizes the area of green leaf per unit area of ground surface and can be obtained by satellite imagery products derived from NDVI analysis. A typical LAI - :math:`K_c` relationship is as follows (Allen et al., 1998, Chapter 6: http://www.fao.org/3/x0490e/x0490e0b.htm): 其他植被类型的数值可以用叶面积指数（LAI）关系来估计。LAI表征每单位面积地表的绿叶面积，可以通过NDVI分析得出的卫星图像产品获得。一个典型的 LAI - :math:`K_c`关系如下（Allen等人，1998，第6章：http://www.fao.org/3/x0490e/x0490e0b.htm）：

.. math:: K_c = \left\{\begin{array}{l}\frac{LAI}{3}\mathrm{\ when\ } LAI \leq 3\\ 1\end{array}\right.

:math:`K_c` estimates for non-vegetated LULC are based on (Allen et al., 1998). Note that these values are only approximate, but unless the LULC represents a significant portion of the watershed, the impact of the approximation on model results should be minimal. math:`K_c`对非植被LULC的估计是基于Allen等人在1998年的研究成果。请注意，这些数值只是近似值，但除非LULC代表流域的重要部分，否则近似值对模型结果的影响应该是最小的。

* Kc for <2m open water can be approximated by Kc=1; 对于<2米的开放水域，Kc可近似为Kc=1。
* Kc for >5m open water is in the range of 0.7 to 1.1; >5米的开放水域的Kc在0.7至1.1之间。
* Kc for wetlands can be assumed in the range of 1 to 1.2; 湿地的Kc可以假设在1到1.2的范围内。
* Kc for bare soil ranges from 0.3 to 0.7 depending on climate (in particular rainfall frequency). It can be estimated at Kc=0.5 (see Allen 1998, Chapter 11). Additional information for determining Kc for bare soil can be found in (Allen et al., 2005). 裸露土壤的Kc在0.3至0.7之间，取决于气候（特别是降雨频率）。它的估计值可以为0.5（见Allen 1998，第11章）。确定裸露土壤的Kc的其他信息可以在（Allen等人，2005）中找到。
* Kc for built areas can be set to f*0.1 +(1-f)*0.6 where f is the fraction of impervious cover in the area. Here, evapotranspiration from pervious areas in built environments is assumed to be approximately 60% of reference evapotranspiration (i.e. the average between lawn grass and bare soil). In addition, evaporation from impervious surface is assumed at 10% of PET. Should local data be available, the user may compute an annual average estimate of Kc, using the method described for crop factors. 建筑区的Kc可以设定为f*0.1+(1-f)*0.6，其中f是该地区不透水覆盖的比例。这里，假设建筑环境中透水区域的蒸发量约为参考蒸发量的60%（即草坪和裸土之间的平均值）。此外，不透水表面的蒸发量被假定为PET的10%。如果本地化数据可用，用户可以使用作物因子所描述的方法，计算出Kc的年平均估计值。


Hydrology水文
---------

.. _watersheds:流域

Watersheds and Sewersheds流域和下水道
^^^^^^^^^^^^^^^^^^^^^^^^^
To delineate watersheds, we provide the InVEST tool DelineateIT, which is relatively simple yet fast and has the advantage of creating watersheds that might overlap, such as watersheds draining to several dams on the same river. See the User Guide chapter for DelineateIt for more information on this tool. Watershed creation tools are also provided with GIS software, as well as some hydrology models. It is recommended that you delineate watersheds using the DEM that you are modeling with, so the watershed boundary corresponds correctly to the topography. 为了划定流域，我们提供了InVEST工具DelineateIT，该工具相对简单而快速，并且具有创建可能重叠的流域的优势，例如流向同一河流上几个水坝的流域。关于这个工具的更多信息，请参见DelineateIt的用户指南章节。GIS 软件以及一些水文模型也提供了流域创建工具。建议你使用你正在建模的 DEM 划分流域，这样流域的边界就能与地形正确对应。

Alternatively, a number of watershed maps are available online, e.g. HydroBASINS: https://hydrosheds.org/. Note that if watershed boundaries are not based on the same DEM that is being modeled, results that are aggregated to these watersheds are likely to be inaccurate. 另外，网上也有一些流域地图，如HydroBASINS: https://hydrosheds.org/。请注意，如果流域的边界不是基于正在建模的同一DEM，则汇总到这些流域的结果可能是不准确的。

Exact locations of specific structures, such as drinking water facility intakes or reservoirs, should be obtained from the managing entity or may be obtained on the web: 具体结构的确切位置，如饮用水设施进水口或水库，应从管理单位获得，或可在网上获得：

 * The U.S. National Inventory of Dams: https://nid.sec.usace.army.mil/美国国家大坝目录：https://nid.sec.usace.army.mil/

 * Global Reservoir and Dam (GRanD) Database: http://globaldamwatch.org/grand/全球水库和大坝（GRanD）数据库：http://globaldamwatch.org/grand/

 * World Water Development Report II dam database: https://wwdrii.sr.unh.edu/download.html世界水资源开发报告II大坝数据库：https://wwdrii.sr.unh.edu/download.html

Some of these datasets include the catchment area draining to each dam, which should be compared with the area of the watershed(s) generated by the delineation tool to assess accuracy. 其中一些数据集包括流向每个大坝的集水区，应与划定工具生成的流域面积进行对比，以评估准确性。

Sewershed data may be available from local municipalities. 下水道数据可从当地市政当局获得。


.. _tfa: 阈值流量累积

Threshold Flow Accumulation阈值流量累积
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The threshold flow accumulation (TFA) is a stream delineation algorithm parameter that specifies the number of upstream pixels that must flow into a pixel before it is classified as a stream. There is no one "correct" value for the TFA. The correct value for your application is the value that causes the model to create a stream layer that looks as close as possible to the real-world stream network in the watershed. Compare the stream network raster output with a known correct stream map, and adjust the TFA accordingly - larger values of TFA will create a stream network with fewer tributaries, smaller values of TFA will create a stream network with more tributaries. A good value to start with is 1000, but note that this can vary widely depending on the resolution of the DEM, local climate and topography. Note that generally streams delineated from a DEM do not exactly match the real world, so just try to come as close as possible. If the modeled streams are very different, then consider trying a different DEM. 阈值流量累积（TFA）是一个流划定算法参数，它规定了在将一个像素归类为流之前必须流入该像素的上游像素的数量。TFA没有一个 "正确 "的值。对你的实际应用来说，正确的值是使模型创建的流层看起来尽可能地接近流域内的真实流网。将河流网络栅格输出结果与已知的正确河流地图进行比较，并相应地调整TFA--较大的TFA值将创建一个支流较少的河流网络，较小的TFA值将创建一个有较多支流的河流网络。一般初始值设置为1000较好，但要注意，这个值会因DEM的分辨率、当地气候和地形的不同而变化很大。请注意，一般来说，从DEM划定的溪流与现实世界并不完全吻合，所以要尽量接近。如果模型中的溪流非常不同，那么可以考虑尝试不同的DEM。

A global layer of streams can be obtained from HydroSHEDS: https://hydrosheds.org/, but note that they are generally more major rivers and may not include those in your study area, especially if it has small tributaries. You can also try looking at streams in Google Earth if no more localized maps are available. 可以从HydroSHEDS: https://hydrosheds.org/ 获得一个全球的溪流图层数据，但要注意的是，它们一般都是比较主要的河流，可能不包括你研究区域的河流，特别是如果研究区内有小的支流。如果没有更多的本地化图层，你也可以尝试在谷歌地球中查看溪流。

Also see the Working with the DEM section of this User Guide for more information. 更多信息请参见本用户指南中的 "与DEM合作 "部分。

.. _soil_groups:土壤分组

Soil Hydrologic Groups土壤水分组
^^^^^^^^^^^^^^^^^^^^^^
Soil hydrologic groups describe the runoff potential of different types of soil. There are four groups: A, B, C, D, where A has the least runoff potential and D has the most. See the United States Department of Agriculture (USDA) National Resources Conservation Service (NRCS) publication for more information: https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17757.wba土壤水文分组描述了不同类型土壤的径流潜力。有四个组。A、B、C、D，其中A的径流潜力最小，D的潜力最大。更多信息见美国农业部（USDA）国家资源保护局（NRCS）出版物：https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17757.wba

Two global layers of hydrologic soil group are available, 1) from FutureWater (available at: https://www.futurewater.eu/2015/07/soil-hydraulic-properties/) and 2) ORNL-DAAC’s HYSOGs250m (available at https://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html.) 有两个全球水文土壤群层，1）来自FutureWater（见链接：https://www.futurewater.eu/2015/07/soil-hydraulic-properties/）；2）ORNL-DAAC的HYSOGs250m（见链接：https://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html。）

**The FutureWater raster** provides numeric group values 1-4 14, 24 and 34. The Seasonal Water Yield model requires only values of 1/2/3/4, so you need to convert any values of 14, 24 or 34 into one of the allowed values. FutureWater栅格**提供数字组值1-4 14、24和34。季节性产水量模型只需要1/2/3/4的数值，所以你需要将任何14、24或34的数值转换成允许的数值之一。

**HYSOGs250m** provides letter values A-D, A/D, B/D, C/D and D/D. For use in this model, these letter values must be translated into numeric values, where A = 1, B = 2, C = 3 and D = 4. Again, pixels with dual values like A/D, B/D etc must be converted to a value in the range of 1-4. **HYSOGs250m**提供字母值A-D、A/D、B/D、C/D和D/D。为了在这个模型中使用，这些字母值必须转换为数字值，其中A=1，B=2，C=3，D=4。同样，像A/D、B/D等双值的像素必须转换为1-4范围内的数值。

In the United States, free soil data is available from the NRCS gSSURGO, SSURGO and gNATSGO databases: https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/geo/. They also provide ArcGIS tools (Soil Data Viewer for SSURGO and Soil Data Development Toolbox for gNATSGO) that help with processing these databases into spatial data that can be used by the model. The Soil Data Development Toolbox is easiest to use, and highly recommended if you use ArcGIS and need to process U.S. soil data. 在美国，可以从NRCS的gSSURGO、SSURGO和gNATSGO数据库中免费获得土壤数据：https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/geo/。他们还提供ArcGIS工具（SSURGO的土壤数据查看器和gNATSGO的土壤数据开发工具箱），帮助将这些数据库处理成模型可以使用的空间数据。土壤数据开发工具箱最容易使用，如果你使用ArcGIS并需要处理美国的土壤数据，强烈推荐使用。

If desired, soil groups may also be determined from hydraulic conductivity and soil depths. FutureWater’s Soil Hydraulic Properties dataset also contains hydraulic conductivity, as may other soil databases. Table 1 below can be used to convert soil conductivity into soil groups. 如果需要，也可以通过导水率和土壤深度来确定土壤组别。FutureWater的土壤水力特性数据集也包含导水率，其他土壤数据库也是如此。下面的表1可以用来将土壤导水率转换成土壤组。

|

**Table 1: Criteria for assignment of hydrologic soil groups (NRCS-USDA,
2007 Chap. 7) 水文土壤组的分配标准（NRCS-USDA，2007年第7章）。**

+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+
|                                                                                                                                                    | Group A     | Group B        | Group C        | Group D                                                               |
+====================================================================================================================================================+=============+================+================+=======================================================================+
| Saturated hydraulic conductivity of the least transmissive layer when a water impermeable layer exists at a depth between 50 and 100 centimeters当不透水层存在于50至100厘米的深度时，最小透水层的饱和导水率   | >40 μm/s    | [40;10] μm/s   | [10;1] μm/s    | <1 μm/s (or depth to impermeable layer<50cm or water table<60cm或防渗层深度<50厘米或地下水位<60厘米)      |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+
| Saturated hydraulic conductivity of the least transmissive layer when any water impermeable layer exists at a depth greater than 100 centimeters当任何不透水层的存在深度大于100厘米时，最小透水层的饱和导水率   | >10 μm/s    | [4;10] μm/s    | [0.4;4] μm/s   | <0.4 μm/s                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+

.. _cn: CN值

Curve Number CN值
^^^^^^^^^^^^
It is recommended to do a literature search to look for values for CN that are specific to the area you're working in. If these are not available, look for values that correspond as closely as possible to the same types of land cover/soil/climate. If none of these more local values are available, general sources are recommended. 建议进行文献检索，寻找你所研究地区特有的CN值。如果没有这些数值，则寻找尽可能接近相同类型的土地覆盖/土壤/气候的数值。如果没有这些更多的本地化数值，建议使用一般来源数据。

Curve numbers can be obtained from the USDA handbook: (NRCS-USDA, 2007 Chap. 9) CN值可以从美国农业部的手册中获得：（NRCS-USDA，2007年第9章）。

For water bodies and wetlands that are connected to the stream, CN can be set to 99 (i.e. assuming that those pixels rapidly convey quickflow.) 对于与溪流相连的水体和湿地，CN可以设置为99（即假设这些像素快速输送快速流）。

When the focus is on potential flood effects, CN may be selected to reflect wet antecedent runoff conditions: CN values should then be converted to ARC-III conditions, as per Chapter 10 in NRCA-USDA guidelines (2007). 当研究重点为潜在的洪水影响时，可以选择CN来反映湿润的先兆径流条件。根据 NRCA-USDA 指南（2007）第 10 章，CN 值应转换为 ARC-III 条件。


.. _bathymetry: 深度测量法

Bathymetry深度测量法
----------
Bathymetry measures water depth. NOAA’s National Geophysical Data Center (NGDC) provides global bathymetry data with various spatial resolutions at https://www.ngdc.noaa.gov/mgg/bathymetry/relief.html. 深度测量法测量水深。NOAA的国家地球物理数据中心（NGDC）提供不同空间分辨率的全球水深测量数据，https://www.ngdc.noaa.gov/mgg/bathymetry/relief.html。

ETOPO1 is a 1 arc-minute global relief model of Earth’s surface that integrates land topography and ocean bathymetry. It was built from numerous global and regional data sets, and is available in “Ice Surface” (top of Antarctic and Greenland ice sheets) and “Bedrock” (base of the ice sheets) versions. NGDC also provides regional and other global bathymetry datasets. ETOPO1是一个1弧分的地球表面全球地形模型，整合了陆地地形和海洋测深。它是由许多全球和区域数据集共同建立的，有 "冰面"（南极洲和格陵兰岛冰盖顶部）和 "基岩"（冰盖底部）版本。NGDC还提供区域和其他全球水深测量数据集。

GEBCO produces public-domain global, gridded bathymetry data: https://www.gebco.net/data_and_products/gridded_bathymetry_data/ GEBCO生产公共领域的全球网格化测深数据：https://www.gebco.net/data_and_products/gridded_bathymetry_data/


.. _buildings:建筑

Building Footprints建筑足迹
-------------------
Maps of built infrastructure may be obtained from the city or open source data such as Open Street Map. https://www.openstreetmap.org已建基础设施的地图可以从城市或开放源码数据（如开放街道地图）中获得。https://www.openstreetmap.org。


References参考文献
----------

Allan, Richard & Pereira, L. & Smith, Martin. (1998). Crop evapotranspiration-Guidelines for computing crop water requirements-FAO Irrigation and drainage paper 56. 

"Hydrologic Soil Groups."National Engineering Handbook, United States Department of Agriculture, National Resources Conservation Service, 2007, www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063.

Ruesch A, and HK Gibbs. 2008. New IPCC tier-1 global biomass carbon map for the year 2000. Available:https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html.
