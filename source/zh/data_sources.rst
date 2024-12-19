.. _data_sources:

************
数据来源
************

这是一个数据源的汇编和对常见模型输入数据的建议清单。这份清单不是确定的，只是作为一个起点。强烈建议寻找更多的本地的、准确的数据（来自国家、州、大学、文献、非政府组织和其他来源），如果没有更多的本地数据，只能使用全球数据进行最终分析。如果你知道的有用的数据来源还未在此列出，请在论坛上分享。

.. _dem:

数字高程模型
------------
数字高程模型（DEM）是一种高程栅格图，其中每个像素的值是其海拔高度（通常以米为单位）。世界上任何地区都有DEM数据，尽管分辨率不相同。

免费的全球DEM原始数据可从以下途径获得：

 * 世界野生动物基金会（WWF）- https://www.worldwildlife.org/pages/hydrosheds
 * 美国国家航空航天局（NASA）: https://asterweb.jpl.nasa.gov/gdem.asp (30m分辨率); 航天飞机雷达地形测绘使命（SRTM）数据：http://dwtkns.com/srtm/
 * 美国地质勘探局（USGS）：https://earthexplorer.usgs.gov/

根据项目目标的差异，DEM的分辨率可能是一个非常重要的参数。例如，如果决策者需要道路对生态系统服务影响的信息，那么就需要精细的分辨率。模型中使用的DEM的水文方面信息必须是正确的。大多数原始DEM数据都有误差，所以很可能需要对DEM进行填充以消除洼地（Sink）。ArcGIS的填充工具或QGIS的Wang & Liu填充算法（SAGA库）的多种处理方法都显示出良好的效果。

对于从DEM生成溪流的水文模型，请仔细观察溪流网络栅格输出。如果溪流不是连续的，而是断成了几块，那么DEM仍然有需要填充的洼地。如果多次填充洼地仍旧不能形成一个连续的溪流网络，也许可以尝试另一种DEM数据。如果结果出现意料之外的栅格模式，这可能是由于用 "近邻"插值方法而不是用"双线性"或 "立方体"方法重新投影DEM造成的。在这种情况下，回到原始DEM数据，用 "双线性 "或 "立方体 "方法进行重新投影。

关于处理DEM的更多细节和指导，请参考本用户指南的DEM工作部分。


.. _lulc:

土地利用/土地覆盖
-----------------------
土地利用/土地覆盖 （LULC） 描述了土地的物理特性和/或人们如何使用它（森林、湿地、水、铺砌、农业、自然保护区等）。为了以栅格格式显示数据，每个 LULC 类别都映射到一个整数代码（这些代码不必是连续的或有序的）。未知的数据缺口应尽可能地进行近似处理，以避免输出层中出现数据缺失（漏洞）。

全球土地利用数据可从多个来源获得，包括：

* 美国国家航空航天局: https://lpdaac.usgs.gov/products/mcd12q1v006/（MODIS多年来提供的基于几种分类的全球土地覆盖数据）
* 欧洲航天局10米分辨率的全球覆盖: https://esa-worldcover.org/
* 欧洲航天局气候变化倡议300米分辨率的土地覆盖: https://www.esa-landcover-cci.org/

美国地质调查局和内政部通过国家土地覆盖数据库提供美国的数据：https://www.usgs.gov/centers/eros/science/national-land-cover-database。

景观上最简单的土地利用/土地覆盖分类包括仅按土地覆盖物（如耕地、森林、草地）进行划分。有几种全球和区域性的土地覆被分类法（例如，Anderson等人，1976年），而且详细的土地覆被分类已被应用于相关的景观。许多国家都有可以使用的国家土地利用/土地覆盖地图。
许多国家/地区都有可以使用的国家 LULC 地图，建议尽可能寻找这些地图。

更复杂的土地利用/土地覆盖分类涉及将相关的土地利用/土地覆盖类型分成更有意义的类型。例如，农业用地类别可被分解为不同的作物类型。森林可以细分为特定的物种或年龄类别。在有数据支持的情况下，你可以按已知会影响建模属性的变量（如降雨、温度、海拔等）对土地利用/土地覆盖类型进行分层。

评估任何给定的土地覆盖图非常重要，以了解它在研究区域中的准确性。特别是全球产品在某些地方（或某些土地覆盖类型）通常比其他地方更准确。

有时，将更通用的土地利用/土地覆盖类分成更详细的类很有用。例如，农业用地类别可以分解为不同的作物类型。森林可以划分为特定的物种或年龄类别。在数据可用的情况下，您可以按已知会影响所建模属性的变量（如降雨量、温度、海拔等）对土地利用/土地覆盖类型进行分层。

土地利用类型的分类取决于模型以及每种土地类型的可用数据量。通常，生物物理表输入将某些相关的生物物理参数映射到每个土地利用/土地覆盖代码。仅当土地利用/土地覆盖类型在建模中提供更高的准确性时，才应将其分解。例如，只有在您掌握了相关生物物理参数差异的信息时，才将“作物”分解为不同的作物类型。

*典型的土地利用/土地覆盖分类方案*
*典型的土地利用/土地覆盖分类方案 - 您的分类方案可能有所不同*

  ====== ===========================
  lucode 土地利用/土地覆盖
  ====== ===========================
  1      常绿针叶林（Evergreen Needleleaf Forest）
  2      常绿阔叶林（Evergreen Broadleaf Forest）
  3      落叶针叶林（Deciduous Needleleaf Forest）
  4      落叶阔叶林（Deciduous Broadleaf Forest）
  5      混合植被覆盖（Mixed Cover）
  6      林地（ Woodland）
  7      稀树草原（Wooded Grassland）
  8      封闭灌木丛（Closed Shrubland）
  9      开阔灌木丛（Open Shrubland）
  10     草原（Grassland）
  11     耕地（行栽作物）（ Cropland (row Crops)）
  12     裸地（Bare Ground）
  13     城市和建成区（Urban and Built-Up）
  14     湿地（Wetland）
  15     混合常青乔木（Mixed evergreen）
  16     混交林（Mixed Forest）
  17     果园/葡萄园（Orchards/Vineyards）
  18     牧草地/牧场（Pasture）
  ====== ===========================

.. _carbon_pools:

碳库
------------
碳储量数据应设定为等于每个土地利用/土地覆盖类型的平均碳储量值。所有碳储量的理想数据来源是一套当地的实地估计，其中所有相关储量的碳储量都已直接测量。这些数据可以汇总到土地利用/土地覆盖地图上，包括按年龄或其他变量进行分层的土地利用/土地覆盖。然而，如果没有这些实地调查数据，则可以从其他常规数据源中获取。

请注意，包括IPCC（2006）在内的一些数据源以生物量为单位报告，而InVEST则使用元素碳的质量。要将公吨的生物量转换为公吨的碳，需要乘以一个转换系数，该系数通常在0.43到0.51之间。IPCC (2006)第4.48页的表4.3中列出了各主要树木类型和气候区域的转换系数。

.. _aboveground_carbon:

地上生物量中储存的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
政府间气候变化专门委员会（IPCC）2006年确定农业、林业和其他土地利用（AFOLU）部门温室气体清单的方法是一个很好的但非常通用的碳储存数据来源（https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html）。要使用IPCC的这组信息，您必须了解您站点的气候域和区域;使用第 4.46 页表 4.1 中的数据和联合国粮食及农业组织 （FAO） 生态区域地图 （http://www.fao.org/geonetwork/srv/en/main.home） 的数字副本来计算。气专委（2006年）表5.1至表5.3（第5.9页）对多年生木本生物量（如果园、农林业等）的农业用地地上生物量进行了估计。表4.7、表4.8和表4.12给出了自然林和人工林类型的地上生物量估计数。

Ruesch 和 Gibbs （2008） 绘制了 IPCC （2006） 地上生物量碳储存数据，给出了 2000 年的土地覆盖数据，可在此处访问：https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html。不幸的是，这些数据没有得到很好的记录，但“lut.zip”包含每个生态区的碳值表。该表没有明确列出单位，但元数据.xml文件表明值以吨 C 为单位/公顷。

也可以参考其他一般的碳储存估算数据来源。例如，Grace等人（2006）估计了全球主要热带草原生态系统的平均地上碳储量（叶+木）（表1）。Houghton (2005)给出了各大洲天然和人工林类型的地上碳储量（表1和表3）。Brown等人（1989年）给出了热带阔叶林的地上生物量估算值，作为土地利用的功能：未受干扰、伐木和非生产性（表7）。特定地区的碳储存数据来源也是可用的。我们发现的数据包括：

* 拉丁美洲：Malhi等人（2006年）报告了玻利维亚、巴西、哥伦比亚、厄瓜多尔、法属几内亚、圭亚那、巴拿马、秘鲁和委内瑞拉227个低地森林地块的地上生物量。Nascimento和Laurance（2002年）估计了20个1公顷的亚马逊雨林地块的地上碳储量。Tiessen等人（1998年）发现了巴西稀树草原Caatingas和Cerrados的地上碳储量。

* 非洲：Zhang和Justice（2001年）报告了中非国家主要森林和灌木LULC类型的地上碳储量。Tiessen等人（1998年）估计了塞内加尔退化稀树草原的地上生物量总量。Makundi（2001年）的报告表明，坦桑尼亚三种人工林类型的年增长率均为增长。Malimbwi等人（1994年）估计了坦桑尼亚Kitungalo森林保护区miombo林地的地上碳储量。Munishi和Shear（2004年）报告了坦桑尼亚东弧山脉Afromontane雨林的地上碳储量。Glenday（2006年）估计了肯尼亚西部卡卡梅加国家森林中3种森林类型的地上碳储量。

* 北美：Smith等人（2006年）估计了美国所有主要森林类型的地上碳储量。

* 碳在线估算器（https://www.ncasi.org/resource/carbon-on-line-estimator-cole/）是一种基于美国农业部林务局森林清查与分析以及资源规划评估数据计算美国森林碳特征的工具。使用此工具，可以在县级尺度上检查碳特征。使用变量选项卡，可以选择地上、地下、土壤或枯木碳库。

* Coomes等人（2002年）估计了新西兰原生灌木丛和森林类型的地上碳储量。

地上生物量（以及碳储量）也可以从木材清单中计算出来，这通常由林业部在一组地块上完成。使用以下公式估算已清查的林分的地上碳储量，其中 VOB 是从树桩到树冠点（树木的可销售部分）测量的每公顷树木体积，以立方米为单位，WD 是树木的木材密度（每单位树木体积的干生物量）， BEF是地上总干生物量与干生物量的比值，CF是元素碳与干生物质的质量比值（Brown 1997）。生物量膨胀因子 （BEF） 考虑了储存在树地上所有其他部分（例如，树枝、树皮、茎、叶子等;树木的不可销售部分）的 C。在大多数情况下，样地的 WD 与优势物种的值近似。Brown（1997）在第3节附录1中提供了许多树种的WD值表和计算BEF的方法（公式3.1.4）。见ECCM （2007）关于粮农组织方法在坦桑尼亚东部森林清查数据中的应用。IPCC（2006年）还提出了（ ）的估计值，其中按生态区域划分的硬木、松树、针叶树和天然林的BEF值在表4.5中给出，表4.13和4.14中给出了许多物种的WD值。（使用表 4.5 中由 S 下标的 BCEF 值。最后，Brown等人（1989）给出了三种土地利用下的热带阔叶林的BEF：未受干扰、伐木和非生产性。

Brown（1997）对上述方程式的使用提出了一些警告。首先，该方程式是针对封闭而不是开放的清查林分（树冠覆盖稀疏的森林，如橡树稀树草原）设计的。其次，VOB估计应该是林分中发现的所有树种的函数，而不仅仅是经济上最有价值的木材。第三，如果地上生物量碳方程要尽可能准确，则需要将胸高直径低至10厘米（胸径=10）的树木包括在清单中。Brown（2002）还指出，使用单一BEF值是对实际生物质生长过程的简化。

这些警告导致Brown（2002）建议使用异速生长生物量方程来估计木质地上生物量（如果有的话）。这些方程给出了林分不同大小树木的分布与林分地上生物量之间的估计关系。Brown（1997）和Brown和Schroeder（1999）分别提供了全球所有生态区和美国东部的一般地上生物量异速生长方程。Cairns等人（2000年）提供了墨西哥南部LULC类型的地上生物量异速生长方程。Nascimento和Laurance（2002年）使用异速曲线估计亚马逊雨林地上生物量。使用这些方程需要了解给定林分中树木大小的分布。

一些研究人员使这些方程的使用更容易一些，他们首先将一个林分的不同大小的树木分布与它的年龄联系起来，然后绘制出年龄和地上生物量之间的关系。例如，Silver等人(2000)估计了地上生物量与林分年龄(即造林/重新再造林以来的年份)或热带生态系统中原生森林类型的原有土地利用/土地覆盖的关系。Smith等人(2006)通过将美国各种森林的年龄与总生物量碳(地下和地上)直接联系起来，使异速运动方程的转换更进一步。

在使用IPCC数据或其他类似的广泛数据来源时，需要考虑的最后一个问题是人为干扰的程度如何影响碳储量。高度扰动地区的地面碳储量可能会低于未扰动地区的储量。目前还不清楚IPCC或其他此类资料来源在给出地上生物量估计值时假设的干扰水平是什么类型。如果森林干扰是示范点的一个问题，土地利用/土地覆盖类型应按干扰程度进行分层。这种分层的例子见 ECCM (2007) 第 14 页的表 2.5。

最后，我们一般不把地上的草本材料作为碳库（如草、花、非木质作物）。我们的工作认为，这种材料并不像木质生物量、地下生物量和土壤那样是长期储存的潜在来源。一般来说，草质材料的碳循环速度太快。

.. _belowground_biomass:

地下生物量中储存的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

对于以木质生物量为主的土地利用/土地覆盖类别，地下生物量可通过地下生物量与地上生物量的 "根茎比"来大致估算。IPCC (2006)第4.49页的表4.4按生态区域给出了"根茎比"的默认估计。Brown (1997)的第3.5节中也给出了这一比率的大致估计。

一些土地利用/土地覆盖类型几乎不包含木质生物量，但包含大量的地下碳储量（如天然草原、人工管理草原、大草原和灌丛/灌木丛区）。在这些情况下，上述的"根茎比"并不适用。这些土地利用与土地覆盖类型的地下估算值最好采用当地数据，但如果当地数据不可用，可以使用一些全球估算值。IPCC（2006）在表6.4（第6.27页）中列出了每个气候区的总生物量（地上加地下）和地上生物量。这些数字之间的差异是对地下生物量的粗略估计。最近，Ruesch和Gibbs（2008年）根据2000年的土地覆盖数据，绘制了IPCC（2006年）的地上生物量碳储存数据，可以通过以下链接访问：https://cdiac.essdive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html。

一些研究对不同生境类型的地下生物量或根茎比的估计进行了总结。在这些研究中，我们发现：

* Grace等人(2006)估计了全世界主要热带草原生态系统的平均木质和草质根系生物量总量(表1)。Baer等人(2002)和Tilman等人(2006)分别估计了在美国内布拉斯加州和明尼苏达州恢复为本地C4草的地块根部储存的C，作为植被恢复后的变量(见Baer等人(2002)的表2和Tilman等人(2006)的图1D)。

* Cairns等人(1997)调查了世界各地土地利用/土地覆盖类型的根茎比率。Munishi和Shear(2004)在对坦桑尼亚东弧形森林的非洲山地森林的研究中使用了0.22的根茎比率。Malimbwi等人(1994)对坦桑尼亚同一地区的miombo林地进行研究时使用0.20的根茎比率。Coomes等人(2002)对新西兰的灌木地使用0.25的根茎比率。Gaston等人(1998)报告中发现，非洲草/灌木稀树草原的根茎比率为1。

.. _soil_carbon:

土壤中存储的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果没有当地或地区的土壤碳估计值，可以从IPCC（2006）中查询农业、牧场和人工管理草原的默认估计值。IPCC（2006）的表2.3包含了按土壤类型划分的土壤碳储量估计值，假设这些储量处于平衡状态，没有积极的土地管理。对于耕地和草地土地利用/土地覆盖类型，这一默认估计值可乘以IPCC（2006）表5.5和6.2所列的管理因素。对于所有其他土地利用/土地覆盖类型及其相关管理方案，IPCC (2006) 假设没有管理因素。

全球土壤碳数据还有其他来源。Post等人（1982年）按照Holdridge生命区分类系统报告了土壤1m深中的碳储量（这些生命区的GIS地图可在以下链接中获取：http://www.arcgis.com/home/item.html?id=f3ec7241777f4c56a69ae14d2a98e44b）。Silver等人(2000)估计了热带生态系统中原生森林类型的土壤碳与造林/再造林后年限的关系。Grace等人（2006）估计了世界各地主要热带草原类型的土壤碳（表1）。Detwiler（1986）在表2中列出了热带森林土壤的土壤碳。

一些针对特定区域的研究也报告了土壤碳储量。我们发现的这些研究包括：

* 北美洲：Smith等人(2006)对美国各地区所有主要森林类型和森林管理方法的造林/再造林以来每5年的增量进行了土壤碳的估算，最长可达125年。其他包括McLauchlan等人（2006）；Tilman等人（2006）；Fargione等人（2008）；Schuman等人（2002）；和Lal（2002）。

* 非洲：Houghton 和 Hackler (2006) 提供了撒哈拉以南非洲 5 种土地利用/土地覆盖森林类型（雨林、湿润森林、森林、灌木丛和山地森林）的土壤碳，这些森林类型保留了其自然覆盖，而森林地区则被转化为耕地、轮垦和牧场。Vagen等人（2005）提供了撒哈拉以南非洲各种土地利用/土地覆盖类型的土壤碳估计值。

* 南美洲。Bernoux等人（2002年）估计了巴西不同土壤类型-植被搭配下30厘米深处的土壤碳储量。例如，包括亚马逊森林和巴西塞拉多在内的14个不同土地覆盖类别下的HAC土壤中的土壤碳储量从2到116千克碳m-2不等

重要提示：在大多数估计景观上的碳储存和封存率的研究中，土壤库的测量只包括矿物土壤中的土壤有机碳（SOC）（Post 和 Kwon，2000）。然而，如果被模拟的生态系统有大量的有机土壤（如湿地或帕拉莫），那么将这部分内容加入到矿物土壤的含量中是至关重要的。在湿地转化为其它土地用途很常见的景观中，也应密切跟踪有机土壤的碳释放（IPCC 2006）。

.. _dead_carbon:

储存在死亡有机物中的碳
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果当地或区域对死亡有机物中储存的碳没有估计值，则可以参考IPCC（2006）中的默认值。表2.2（第2.27页）给出了森林土地利用/土地覆盖类型中落叶的默认碳储量。对于非林地类型，枯落物接近于0。Grace等人(2006)估计了世界上主要热带草原生态系统的平均碳储存量(表1)。目前还不清楚他们对 "地上生物量 "的总估计值是否包括枯木。一般来说，枯木碳库存更难估计，我们没有找到默认数据源。

区域性的估算值

* 美国：Smith等人(2006)估计了美国各地区所有主要森林类型和森林经营方式的落叶(文件中称为 "森林地面 "碳)和枯木(文件中称为 "立枯树 "和 "倒枯木 "的碳库总量)中的碳储存量，作为林分年龄的函数。

* 南美洲。Delaney等人(1998)估计了委内瑞拉6个热带森林的立木和枯木中的碳储存量。据作者估算，枯木的生物量通常是地上植被的1/10。



降水量
-------------

.. _precipitation:

年度和月度降水量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
降水量可以从长期的雨量计点数据中插值得到。在考虑雨量计数据时，要确保它们能很好地覆盖案例地区，特别是如果有很大的海拔变化，导致研究区域内的降水量不均一时。理想的情况是，测量仪至少有10年的连续数据，且没有大的差距，并与作为输入数据的土地利用/土地覆盖图的时间段相同。降水为雪的情况也应考虑在内。

如果没有外业数据，遥感模型的全球数据集可以考虑偏远地区。您可以使用由气候研究单位：http://www.cru.uea.ac.uk 或WorldClim：https://www.worldclim.org/ 等免费提供的全球数据集中的粗略数据。搜索降水数据的一个有用地方是NCAR的气候数据指南：https://climatedataguide.ucar.edu/climate-data。

一些来源（例如 WorldClim）提供了 12 个月平均降水量栅格。要在年产水量模型中使用这些栅格，必须将月栅格相加（求和）以计算年平均降水量地图。

在美国，俄勒冈州立大学的PRISM小组免费提供30弧度的降水数据。可登录他们的网站https://prism.oregonstate.edu/，并导航到 "800米正常值 "来下载数据。

.. _rain_events:

降雨事件
^^^^^^^^^^^
每月的平均雨量可以从当地的气候统计部门（气象局）或网上资源获得：

 *  https://www.yr.no/
 *  http://wcatlas.iwmi.org
 * 世界银行还提供了带有降水统计数据的地图：https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api


蒸散量
-----------------

.. _et0:

参考蒸散量
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
参考蒸发量，ET₀，是衡量在一定时期内从土地上蒸发到空气中的水量。它是蒸发（直接从土壤、水体和其他表面）和蒸腾（通过植物）的总和。它通常表示为单位时间内水的深度，单位是毫米。math:`mm/month`代表月度，:math:`mm/year` 代表年度。(注意：与降水类似，这是从特定区域蒸发的水的 "深度"；它不是 "每 "像素、平方米或任何其他面积单位）。InVEST模型都使用这种测量方法，但有些数据将蒸发量表示为每面积的体积或能量。有关详细信息，请参阅 http://www.fao.org/3/x0490e/x0490e04.htm。

国际农业研究磋商组织CGIAR提供了基于WorldClim气候数据的全球潜在蒸散量图，可用于参考蒸发量：https://cgiarcsi.community/data/global-aridity-and-pet-database/。

搜索蒸散数据（或可用于计算ET的降水和温度数据）的一个有效地址是美国大气研究中心（NCAR）的气候数据指南：https://climatedataguide.ucar.edu/climate-data。

如果正在运行一个同时需要降水和蒸散量作为输入数据的模型，请确保蒸散量数据是基于被用作模型输入数据的同一降水数据。

参考蒸散量随海拔高度、纬度、湿度和坡度的变化而变化。有许多计算方法，这些方法在数据要求和精度上有差异。
可以利用月平均降水、最高和最低温度的栅格数据来计算参考蒸散量。这些数据可能来自气象站，可以遵循相关过程来开发年平均降水栅格数据，包括在站点之间内插时考虑海拔的影响。或者，WorldClim和CRU都提供已经是栅格格式的月度温度数据。这些月度栅格可以作为下面列出的方程式的输入数据。
可以利用月平均降水、最高和最低温度（也可从WorldClim和CRU获得）的栅格数据来计算参考蒸散量，在从观测站点之间内插时需要考虑海拔的影响。制作这些月度降水和温度栅格的数据，与制作"月度降水"栅格的过程相同。

确定参考蒸散量的一个简单方法是 "修正的哈格里夫斯 "方程（Droogers和Allen，2002），当信息不确定时，它产生的结果比Pennman-Montieth更优。

.. math:: ET_0 = 0.0013\times 0.408\times RA\times (T_{av}+17)\times (TD-0.0123 P)^{0.76}

“修正的哈格里夫斯”方法使用每个月的平均日最高温度和平均日最低温度（以摄氏度为单位的“Tavg”）、每个月的平均日最高温和平均日最低温之间的差值（“TD”）、地外辐射（:math:`RA` in :math:`\mathrm{MJm^{-2}d^{-1}}`）和平均月降水量（:math:`P`，单位为每月毫米），所有这些数据可以相对容易地获得。

可对栅格数据使用此方程。请注意，它计算的是日均蒸散量，因此结果需要乘以对应月份的天数，并且每个月必须运行一次。生成的月度蒸散量栅格可用于季节性产水量模型。对于年产水量模型，将每月蒸散量栅格数据相加得到年平均蒸散量。

温度和降水数据通常来自区域图表、直接测量或国家或全球数据集（如WorldClim）。另一方面，直接测量辐射数据的成本要高得多，但可以通过在线工具、表格或方程式可靠地估计。粮农组织（FAO）灌溉排水文件56（Allan（1998））在附件2中提供了月度辐射数据;要使用它，请选择最接近研究区域的纬度值。另一种选择是使用 GIS 工具计算特定研究区域的太阳辐射，并将此空间图层用作修正的哈格里夫斯方程的输入。

参考蒸散量也可以用Hamon方程按月和按年计算（Hamon 1961, Wolock and McCabe 1999）：

.. math:: PED_{Hamon} = 13.97 d D^2W_t

式中:math:`d`是一个月的天数，:math:`D` 是每年计算的月平均日照时间（单位为12小时），:math:`W_t` 是饱和水蒸气密度，计算方法如下：

.. math:: W_t = \frac{4.95e^{0.062 T}}{100}

式中：:math:`T` 是月平均温度，摄氏度。当月平均温度低于零时，参考蒸散量被设置为零。然后对于分析的时间段内的每一年，将每个栅格像元的月度计算潜在蒸散发（PET）值相加，计算出每一年的年度潜在蒸散发图层。

在有pan evaporation数据的情况下，评估参考蒸散量的最后一种方法是使用以下公式：
:math:`ETo = pan ET *0.7` (Allen et al., 1998)

.. _kc:

农作物蒸散系数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
农作物的蒸散系数（:math:`K_c`）可以从灌溉和园艺手册中获得。粮农组织有相关在线资源：http://www.fao.org/3/X0490E/x0490e0b.htm。粮农组织的表格按作物生长阶段列出了系数(:math:`K_c` ini, :math:`K_c` mid, :math:`K_c` end)，这些系数需要转换为年平均或月平均（取决于模型）:math:`K_c` 。这需要了解研究区域植被的物候学（平均绿化、枯萎日期）和作物生长阶段（每年作物的种植和收获时间）。年平均值:math:`K_c` 可以使用以下公式估算为植被特征和平均月参考蒸散量的函数：

.. math:: K_c = \frac{\sum^{12}_{m=1}K_{cm}\times ET_{o_m}}{\sum^{12}_{m=1}ET_{o_m}}

式中 : math:`K_{cm}`是:math:`m`（1-12）月份的平均作物系数，: math:`ET_{o_m}` 是相应的参考蒸散量。这些数值也可以用以下电子表格来计算：https:// github.com/natcap/invest.users-guide/raw/main/data-sources/kc_calculator.xlsx。:math:`K_c` 的值应该是0-1.5之间的小数。

其他植被类型的数值可以用叶面积指数（LAI）关系来估计。LAI表征每单位面积地表的绿叶面积，可以通过NDVI分析得出的卫星图像产品获得。一个典型的 LAI - :math:`K_c` 关系如下（Allen等人，1998，第6章：http://www.fao.org/3/x0490e/x0490e0b.htm）：

.. math:: K_c = \left\{\begin{array}{l}\frac{LAI}{3}\mathrm{\ when\ } LAI \leq 3\\ 1\end{array}\right.

:math:`K_c` 对非植被LULC的估计是基于Allen等人在1998年的研究成果。请注意，这些数值只是近似值，但除非LULC代表流域的重要部分，否则近似值对模型结果的影响应该是最小的。

* 对于<2米的开放水域，Kc可近似为Kc=1。
* >5米的开放水域的Kc在0.7至1.1之间。
* 湿地的Kc可以假设在1到1.2的范围内。
* 裸露土壤的Kc在0.3至0.7之间，取决于气候（特别是降雨频率）。它的估计值可以为0.5（见Allen 1998，第11章）。确定裸露土壤的Kc的其他信息可以在（Allen等人，2005）中找到。
* 建筑区的Kc可以设定为f*0.1+(1-f)*0.6，其中f是该地区不透水覆盖的比例。这里，假设建筑环境中透水区域的蒸发量约为参考蒸发量的60%（即草坪和裸土之间的平均值）。此外，不透水表面的蒸发量被假定为PET的10%。如果本地化数据可用，用户可以使用作物因子所描述的方法，计算出Kc的年平均估计值。


水文
---------

.. _watersheds:

流域和下水道
^^^^^^^^^^^^^^^^^^^^^^^^^
为了划定流域，我们提供了InVEST工具DelineateIT，该工具相对简单而快速，并且具有创建可能重叠的流域的优势，例如流向同一河流上几个水坝的流域。关于这个工具的更多信息，请参见DelineateIt的用户指南章节。GIS 软件以及一些水文模型也提供了流域创建工具。建议你使用你正在建模的 DEM 划分流域，这样流域的边界就能与地形正确对应。

另外，网上也有一些流域地图，如HydroBASINS: https://hydrosheds.org/。请注意，如果流域的边界不是基于正在建模的同一DEM，则汇总到这些流域的结果可能是不准确的。

具体结构的确切位置，如饮用水设施进水口或水库，应从管理单位获得，或在网上获得：

 * 美国国家大坝目录：https://nid.sec.usace.army.mil/

 * 全球水库和大坝（GRanD）数据库：http://globaldamwatch.org/grand/

 * 《世界水资源开发报告II》大坝数据库：https://wwdrii.sr.unh.edu/download.html

其中一些数据集包括流向每个大坝的集水区，应与划定工具生成的流域面积进行对比，以评估准确性。

下水道数据可从当地市政当局获得。


.. _TFA:

阈值流量累积
^^^^^^^^^^^^^^^^^^^^^^
阈值流量累积（TFA）是一个流划定算法参数，它规定了在将一个像素归类为流之前必须流入该像素的上游像素的数量。TFA没有一个 "正确 "的值。对你的实际应用来说，正确的值是使模型创建的流层看起来尽可能地接近流域内的真实流网。将河流网络栅格输出结果与已知的正确河流地图进行比较，并相应地调整TFA--较大的TFA值将创建一个支流较少的河流网络，较小的TFA值将创建一个有较多支流的河流网络。一般初始值设置为1000较好，但要注意，这个值会因DEM的分辨率、当地气候和地形的不同而变化很大。请注意，一般来说，从DEM划定的溪流与现实世界并不完全吻合，所以要尽量接近。如果模型中的溪流非常不同，那么可以考虑尝试不同的DEM。

可以从HydroSHEDS: https://hydrosheds.org/ 获得一个全球的溪流图层数据，但要注意的是，它们一般都是比较主要的河流，可能不包括你研究区域的河流，特别是如果研究区内有小的支流。如果没有更多的本地化图层，也可以尝试在谷歌地球中查看溪流。

更多信息请参见本用户指南中的 "DEM使用"部分。

.. _soil_groups:

土壤水文组
^^^^^^^^^^^^^^^^^^^^^^
土壤水文组描述了不同类型土壤的径流潜力。有四个组。A、B、C、D，其中A的径流潜力最小，D的潜力最大。更多信息见美国农业部（USDA）国家资源保护局（NRCS）出版物：https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17757.wba

两个全球土壤水文组如下。1）FutureWater（见链接：https://www.futurewater.eu/2015/07/soil-hydraulic-properties/）；2）ORNL-DAAC的HYSOGs250m（见链接：https://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html。）

FutureWater栅格**提供数字组值1-4 14、24和34。季节性产水量模型只需要1/2/3/4的数值，所以你需要将任何14、24或34的数值转换成允许的数值之一。

**HYSOGs250m** 提供字母值A-D、A/D、B/D、C/D和D/D。为了在这个模型中使用，这些字母值必须转换为数字值，其中A=1，B=2，C=3，D=4。同样，像A/D、B/D等双值的像素必须转换为1-4范围内的数值。

在美国，可以从NRCS的gSSURGO、SSURGO和gNATSGO数据库中免费获得土壤数据：https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/geo/。他们还提供ArcGIS工具（SSURGO的土壤数据查看器和gNATSGO的土壤数据开发工具箱），帮助将这些数据库处理成模型可以使用的空间数据。土壤数据开发工具箱最容易使用，如果你使用ArcGIS并需要处理美国的土壤数据，强烈推荐使用。

如果需要，也可以通过导水率和土壤深度来确定土壤组别。FutureWater的土壤水力特性数据集也包含导水率，其他土壤数据库也是如此。下面的表1可以用来将土壤导水率转换成土壤组。

|

**表1：水文土壤组的分配标准（NRCS-USDA，2007年第7章）。**

+-----------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+
|                                                                 | Group A     | Group B        | Group C        | Group D                                                               |
+=================================================================+=============+================+================+=======================================================================+
| 当不透水层存在于50至100厘米的深度时，最小透水层的饱和导水率     | >40 μm/s    | [40;10] μm/s   | [10;1] μm/s    | <1 μm/s 或防渗层深度<50厘米或地下水位<60厘米                          |
+-----------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+
| 当任何不透水层的存在深度大于100厘米时，最小透水层的饱和导水率   | >10 μm/s    | [4;10] μm/s    | [0.4;4] μm/s   | <0.4 μm/s                                                             |
+-----------------------------------------------------------------+-------------+----------------+----------------+-----------------------------------------------------------------------+

.. _cn:

CN值
^^^^^^^^^^^^
建议进行文献检索，寻找你所研究地区特有的CN值。如果没有这些数值，则寻找尽可能接近相同类型的土地覆盖/土壤/气候的数值。如果没有这些更多的本地化数值，建议使用一般来源数据。

CN值可以从美国农业部的手册中获得：（NRCS-USDA，2007年第9章）。

对于与溪流相连的水体和湿地，CN可以设置为99（即假设这些像素快速输送快速流）。

当研究重点为潜在的洪水影响时，可以选择CN来反映湿润的先兆径流条件。根据 NRCA-USDA 指南（2007）第 10 章，CN 值应转换为 ARC-III 条件。


.. _bathymetry:

深度测量法
----------
深度测量法测量水深。NOAA的国家地球物理数据中心（NGDC）提供不同空间分辨率的全球水深测量数据，https://www.ngdc.noaa.gov/mgg/bathymetry/relief.html。

ETOPO1是一个1弧分的地球表面全球地形模型，整合了陆地地形和海洋测深。它是由许多全球和区域数据集共同建立的，有 "冰面"（南极洲和格陵兰岛冰盖顶部）和 "基岩"（冰盖底部）版本。NGDC还提供区域和其他全球水深测量数据集。

GEBCO生产公共领域的全球网格化测深数据：https://www.gebco.net/data_and_products/gridded_bathymetry_data/


.. _buildings:

建筑足迹
----------------
已建基础设施的地图可以从城市或开放源码数据（如开放街道地图）中获得。https://www.openstreetmap.org。


参考文献
------------

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

NRCS-USDA, 2007. National Engineering Handbook. United States Department of Agriculture, https://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063.

Post, WM, WR Emanuel, PJ Zinke, and AG Stangenberger. 1982. Soil carbon pools and world life zones. Nature 298:156-159.

Post, WM, KC Kwon. 2000. Soil carbon sequestration and land-use change: processes and potential. Global Change Biology 6:317-327.

Ruesch A, and HK Gibbs. 2008. New IPCC tier-1 global biomass carbon map for the year 2000. Available:https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html.

Silver, WL, R. Ostertag, and AE Lugo. 2000. The potential for carbon sequestration through reforestation of abandoned tropical agricultural and pasture lands. Restoration Ecology 8:394-407.

Tiessen, H., C. Feller, EVSB Sampaio, and P. Garin. 1998. Carbon Sequestration and Turnover in Semiarid Savannas and Dry Forest. Climatic Change 40:105-117.

Tilman, D., J. Hill, and C. Lehman. 2006. Carbon-Negative Biofuels from Low-Input High-Diversity Grassland Biomass. Science 314:1598-1600.

Vagen, TG, R Lal, and BR Singh. 2005. Soil carbon sequestration in sub-Saharan Africa: A review. Land Degradation & Development 16:53-71.

Zhang, Q, and CO Justice. 2001. Carbon Emissions and Sequestration Potential of Central African Ecosystems. AMBIO 30:351-355.
