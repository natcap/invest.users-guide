.. _scenic-quality:

********************************************
景区质量
********************************************

概述
=======

海洋和沿海海景的自然景观有助于在许多方面提高当地群体的福祉。通过吸引支
持本地企业的游客，景区设施在在增强本地经济方面发挥了重要作用。地方产权的价值部分取决于其位置的属性特征，景观往往增加地方产权价值(Sanders and Polasky 2009, Bourassa et al. 2004, Benson et al. 2004)。当地社区和居民常常被景观吸引，并且对威胁到现有景观、减少从景观获得好处的行为表现出强烈的反对意见 (Ladenburg and Dubgaard 2009, Haggett 2011)。InVEST景区质量模型允许用户确定可以看到近岸或离岸景观的位置。它产生的视域图可以用来识别新的离岸开发的可视化足迹，并计算受影响可见性的值。视域模型的输入包括：地形和水深、感兴趣的海上设施的位置、以及观赏者的位置（例如：人口中心、或感兴趣的领域，比如公园或小径）。 该模型不会量化视域改变的经济影响，但可以对其进行调整以计算视域指标，以用于更详细的估值研究。目前它并未考虑植被或土地基础设施限制陆地区域的可能方式，这些陆地区域会在视觉上受到离岸开发的影响。


简介
============

人类活动越来越多地控制沿海生态系统。这种逐渐增多的人类活动会危害到沿海
和海洋地区相关的独特风景质量。海岸线和'海景'是一种重要的经济资产，可以吸引游客来此旅游和休闲，为海岸附近的居民带来一定的生活质量。附近和离岸开发的项目经常引起相当大的关注，当地社区通常会评估自然海景的内在美。视觉影响属于外部影响，除非被测量或考虑，否则不会成为权衡新的沿海开发的成本和效益的计算因素。使用视域范围分析的应用程序，其范围可从水产养殖设施的选址一直到旅游活动的空间竞争的最小化 (Perez 2003)，以及海上风力项目的海景和海岸线的能见度评估(Environmental Design and Research 2006)。 由于美丽的风景通常被认为是居住在海岸附近的人们的重要属性，同时也被认为是那些在沿海地区享受海洋和海洋环境的人们的主要属性，因此，沿海规划者可以将可视化设施的措施以及（或者是）不利条件的措施整合到更广泛的政策讨论和规划执行中。因为大多数视域范围分析的应用程序均涉及到检查新设施的负面影响，因此，InVEST景区质量模型内的语言假定风景对象会对风景产生负面影响。然而，对于观察这些开发设施的积极解释可以包含在模型结果的解释中。

InVEST景区质量模型以一种简单的方式为用户提供了近岸和离岸开发建议之间
的潜在权衡信息以及这些项目的可视化影响。该模型生成的视域范围地图可以用来确定最有可能通过海景添加造成直接影响的沿海地区。它们可以作为更为广泛分析的价值投入，其中考虑了一系列的海洋环境所提供的服务。

这个模型可以用来计算成本与海外相关视觉影响，随着设施的位置离岸越来越远
这些费用可能会减少，而安装和操作的成本随与海岸线的距离增加而增加。一些估值研究,探索海外开发项目造成的视觉不舒服表现出复杂的景象。最近一项研究发现, 一个海上风力发电项目造成的视觉不舒服导致个人生活沿着海岸外部成本从27美元提高至80美元 (Krueger et al. 2010)。相比之下, Firestone et al. (2009)发现,公众接受海洋可再生能源项目的增长和争议可能低于预期。

模型
=========

景区质量模型提供了周围风景或海景的离岸对象的可见性信息。离岸和近岸开发
项目，例如，波可再生能源设施或水产养殖设施，有可能影响视觉设施，这些设施是许多沿海地区的一个重要特征。视域范围分析的结果可以帮助决策者识别哪些领域的视觉影响可能会成为规划的一个重要因素。

模型输入分为两组选项：**常规** 选项包含运行视域计算所需的所有条目，例如 DEM 的位置和用于标识导致视觉影响的地点位置的点矢量。**估值** 选项允许用户选择估值功能的功能形式及其参数。然后根据用户定义的感兴趣区域 （AOI） 计算视域分析。

该模型将创建三个输出，可用于评估添加到海洋环境中的任何类型的设施的可见影响：

    * *vshed.tif*是一个栅格，其中包含每个像素可见的视点数之和。如果在结构/视点矢量中提供了 *WEIGHT* 列，则可见性总和将加权。如果估值和权重均设置为``1``，则此栅格将减少为仅从像素可见的站点数计数。

　　* *vshed_value.tif* 是为每个站点计算的所有单个评估栅格的总和。如果在站点向量中提供了 *WEIGHT* 列，则将相应地对值进行加权。
　　
　　* *vshed_qual.tif* 是表示给定像素的视觉质量的栅格。*vshed_Value.tif* 的单元格根据以下百分位数分隔符进行分类：
　　
        1.未受影响的
        2. 低视觉冲击/高视觉质量（<25%）
        3. 中等视觉冲击/中等视觉质量（25-50%）
        4. 高视觉冲击力/低视觉质量（50-75%）
        5. 非常高的视觉冲击力/较差的视觉质量（>75%）

在计算的每个步骤中为每个特征 *X* 创建附加文件：

　　* *visibility_X.tif* 表示从要素 *X* 可见的像素
　　    * *auxiliary_X.tif* 是作为视域算法的一部分编写的中间栅格。像素值表示像素可见必须达到的最小高度。
　　    * *value_X.tif* *value_X.tif* 是视域的值、加权值（如果提供了 *WEIGHT* 列）以及像素与要素 *X* 之间的距离（以米为单位）。

工作原理
------------
InVEST 景区质量模型通过以下四个步骤计算景观要素的视觉影响：

1. 对于每个结构站点:

   1. 根据Wang等人的参考-平面视域算法计算每个点要素*X* (*中间\\visibility_X.tix*)的可见性。
   2. 从可见性中，通过加权可见性并应用用户界面中定义的评估函数（*中间value_X.tif*）来确定可见性便利性/便利性的值。

2. 对评估栅格求和以创建加权聚合 （*输出\\vshed_value.tif*）

3. 将加权聚合评估栅格划分为四分位数，以创建表示视觉质量的栅格 (*输出\\vshed_qual.tif*)

4. 对所有结构点的可见性栅格进行加权和求和，以创建可见点数的加权总和 (*output\\vshed.tif*)

估值可以采用以下形式之一：

Linear:

.. math:: f(x) = a + b \cdot x

Logarithmic:

.. math:: f(x) = a + b \cdot ln(x)

Exponential:

.. math:: f(x) = a \cdot e^{(-b \cdot x)}

其中 *x* 是从像元中心到点要素的距离（以米为单位），*a* 和 *b* 是用户定义的系数。使用默认参数值 （*a=1*， *b=0*），模型将计算聚合视域。评估函数的最大评估半径最大为默认为 8000 米。

限制和简化
===============================

包含在景区质量模型中的全球DEM并未考虑树木、建筑、或其他使得视图模糊的
结构。如果用户拥有可以代表树、建筑、或其他障碍物（及其高度）的位置的栅格层，这些信息可以被纳入DEM，来创建一个更为逼真的表面来使得景观变得模糊或清晰。该模型考虑了地球曲率对视线的限制，但并没有限制默认设置中不同大小和质量的物体对人眼可见的距离。只要具有可以从特定的DEM网格单元与任何近海点之间计算得出的直线矢量，该网格单元即被视为可见。 如果使用默认设置来解释远海位置的设施的视域范围影响地图，那么应该慎重考虑以上问题。然而，用户可以提供一个外半径，从而可以在从每个离岸开发站点识别可见区域时限制搜索距离。

.. _ae-data-needs:

数据需求
==========

常规
-------

- :investspec:`scenic_quality.scenic_quality workspace_dir`

- :investspec:`scenic_quality.scenic_quality results_suffix`

- :investspec:`scenic_quality.scenic_quality aoi_path`

- :investspec:`scenic_quality.scenic_quality structure_path` 这些可能代表水产养殖网栏或波浪能设施等结构。如果要包括覆盖区较大的要素（例如明切），请将面转换为均匀分布点的格网。

该模型将单独计算每个要素的视域，并将它们聚合到组合视域中。用户最多可以指定三个字段（所有字段都是可选的），来为每个要素分配最大查看距离、视域重要性系数或视点高度。

 字段:

  - :investspec:`scenic_quality.scenic_quality structure_path.fields.radius`
  - :investspec:`scenic_quality.scenic_quality structure_path.fields.weight`
  - :investspec:`scenic_quality.scenic_quality structure_path.fields.height`

- :investspec:`scenic_quality.scenic_quality dem_path` 用于确定AOI陆地海景内可见影响景区质量特征的区域。模型以该栅格的分辨率运行。

- :investspec:`scenic_quality.scenic_quality refraction` 空气密度的变化使得光线向下弯曲，导致观察者看得更远，地球看起来不那么弯曲。虽然这种效应的大小随大气条件而变化，但标准的经验法则是，可见光的折射会使地球的视曲率降低七分之一。默认值为 0.13。

估值
---------

- :investspec:`scenic_quality.scenic_quality do_valuation`

- :investspec:`scenic_quality.scenic_quality valuation_function`

- :investspec:`scenic_quality.scenic_quality a_coef`

- :investspec:`scenic_quality.scenic_quality b_coef`

- :investspec:`scenic_quality.scenic_quality max_valuation_radius` 估值函数 ：math：`f`  在半径 ：math：`r`(:math:`f(r)>=0`)处不能为负数。


最终结果
-------------

输出文件夹
^^^^^^^^^^^^^
* **输出\\vshed_qual.tif**

　　* 此栅格图层包含一个字段，该字段根据四分位数对 AOI 中的视觉质量进行分类。视觉质量等级包括：不受影响（无视觉冲击）、高（低视觉冲击）、中（中等视觉冲击）、低（高视觉冲击）和非常低（非常高的视觉冲击）。
　　
* **输出\\vshed.tif**

   * 此栅格图层包含所有可见性栅格的加权总和。如果结构点矢量中未提供权重列，则此栅格将表示每个像素可见的结构点数的计数。

   * 要比较方案运行，请使用此图层而不是vshed_qual。通过计算多次运行的"vshed"输出之间的差异，用户可以评估不同场景的视觉质量变化。

* **输出\\vshed_value.tif**

   * 此栅格图层包含为每个点创建的估值栅格的加权总和。

中间文件夹
^^^^^^^^^^^^^^^^^^^

* **intermediate\\dem_clipped.tif**

    * 此栅格图层是按掩膜提取到 AOI 并切片的 DEM 版本。这是用于视域分析的 DEM 文件。

* **intermediate\\aoi_reprojected.shp**

　　* 此矢量是 AOI，重新投影到 DEM 的空间参考和投影。
　　
* **intermediate\\structures_clipped.shp**

    * 此矢量包含与 AOI 相交的所有视点。

* **intermediate\\structures_reprojected.shp**

　　* 这是结构矢量，重新投影到 DEM 的空间参考和投影。
　　
* **intermediate\\visibility_*.tif**

　　* 给定结构视点的可见性栅格。此栅格的像素值为 0（不可见）、1（可见）或无数据（其中 DEM 为 nodata）。
　　
* **intermediate\\auxiliary_*.tif**

　　* 在计算给定结构视点的视域时创建的中间栅格。此栅格的值表示 DEM 必须具有的最小高度，以使地形在该像素处可见。
　　
* **intermediate\\value_*.tif**

    * 视域便利设施/不便利设施的计算值，给定与结构视点的像素距离（以米为单位）、视点的权重、估值函数以及 *a* 和 *b* 系数。仅针对可见像素评估视域的值。如果基础 DEM 像素未定义（具有 nodata 值），则评估栅格也不会定义。

参考
==========

Benson E., Hansen, J., Schwartz, A., and Smersh, G., 1998. Pricing residential amenities: the value of a view. Journal of Real Estate Research, 16: 55-73.

Bourassa, S., Hoesli, M. and Sun, J. 2004. What’s in a view? Environment and Planning A. 36(8): 1427-1450.

Center for International Earth Science Information Network (CIESIN), Columbia University; International Food Policy Research Institute (IFPRI); The World Bank; and Centro Internacional de Agricultura Tropical (CIAT). 2004. Global Rural-Urban Mapping Project (GRUMP), Alpha Version: Population Grids. Palisades, NY: Socioeconomic Data and Applications Center (SEDAC), Columbia University. Available at permanently to https://sedac.ciesin.columbia.edu/data/collection/gpw-v4. (downloaded on 1/6/2011).

Environmental Design and Research, P.C. 2006. Seascape and shoreline visibility assessment. Cape Wind Energy Project. Cape Cod, Martha’s Vineyard, and Nantucket, Massachusetts. Prepared for Cape Wind Associates, L.L.C. Boston, Mass. Syracuse, N.Y. July 2006.

Firestone, J., Kempton, W. & Krueger, A., 2009. Public acceptance of offshore wind power projects in the USA. Wind Energy, 12(2):183-202. 

Haggett, C. 2011. Understanding public responses to offshore wind power. Energy Policy. 39: 503-510.

Krueger, A., Parson, G., and Firestone, J., 2010. Valuing the visual disamenity of offshore wind power at varying distances from the shore: An application of on the Delaware shoreline. Working paper. Available at: https://works.bepress.com/george_parsons/.

Ladenburg, J. & Dubgaard, A., 2009. Preferences of coastal zone user groups regarding the siting of offshore wind farms. Ocean & Coastal Management, 52(5): 233-242. 

Perez, O.M., Telfer, T.C. & Ross, L.G., 2005. Geographical information systems-based models for offshore floating marine fish cage aquaculture site selection in Tenerife, Canary Islands. Aquaculture Research, 36(10):946-961. 

Sander, H.A. & Polasky, S., 2009. The value of views and open space: Estimates from a hedonic pricing model for Ramsey County, Minnesota, USA. Land Use Policy, 26(3):837-845. 

Wang, J., Robertson, G.J., White, K., 2000. Generating viewsheds without using sightlines. Photogrammetric Engineering & REmote Sensing, 66(1):87-90
