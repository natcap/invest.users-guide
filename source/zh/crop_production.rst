.. _作物生产:

***************
作物生产
***************

摘要
=======

作物生产百分比和作物生产回归模型根据用户提供的土地覆盖信息估算一组固定作物的作物产量和营养价值。作物产量主要受气候驱动，如果有可用的肥料用量，回归模型也可以将其考虑在内。

简介
============

扩大农业生产和缩小产量差距是许多致力于扶贫和实现粮食安全的政府和发展机构的关键战略。然而，将自然栖息地转化为农业生产会影响其他生态系统服务，这些服务对于维持农业为当地社区提供的经济利益至关重要。集约化的农业可能会增加水源的污染负荷，这通常需要未来昂贵的水净化方法。过度用水也威胁到水力发电和其他服务的供应。尽管如此，作物生产对于人类福祉和生计而言仍至关重要。 InVEST 作物生产模型允许对这一至关重要的人类活动的成本和收益进行详细检查，有利于以下问题的探讨：

+就总产量而言，不同的种植系统安排或选择与现有系统相比如何？转换种植作物能否产生更高的经济回报或营养价值？

+作物集约化生产对生态系统服务有何影响？如果通过增加集约化来减少用于生产等量粮食的土地，那么净生态系统服务的结果是积极的还是消极的？

+我们如何评估“为满足不断增长的粮食需求，同时尽量减少对生态系统服务的影响”的不同战略？

模型
=========

InVEST作物生产模型分为基于百分位数的产量模型（涵盖全球172种作物）和基于回归的模型（考虑10种作物的施肥率）。这些模型作为“百分位数”和“回归”模型部署到最终用户。

所有结果都与来自同一地区的观察结果进行比较，以进行质量控制检查以及33种宏量和微量营养素的营养信息。

百分位模型
----------------

InVEST 作物生产百分位数模型根据现有数据、百分位数摘要和观察到的产量估算出 172 种作物的产量。这些观察结果基于粮农组织和次国家级数据集，包括 172 种作物的吨/公顷（Monfreda 等人，2008 年）和营养信息。百分位产量对于探索一系列集约化水平非常有用，在每个作物气候箱中观察到的产量数据中列出了第 25、50、75 和 95 个百分位的产量。

回归模型
----------------

对于Mueller等人（2011）已在全球范围内模拟了10种主要作物的产量，作物生产回归模型可以提供给定肥料投入的产量估计值。这些作物包括大麦、玉米、油棕、马铃薯、水稻、大豆、甜菜、甘蔗、向日葵和小麦。要运行此模型，用户必须提供一个附加表，该表对应于作物的氮、磷和钾肥施用量（kg/ha）。该模型产生建模和观察到的作物产量以及营养价值。


模型运行原理
------------

提供的数据集
~~~~~~~~~~~~~~~~~
示例数据包含一个 **model_data** 目录，其中包含模型所依赖的全局Monfreda 数据集:

- **climate_percentile_yield_tables** (百分位模型): 对于每种作物，CSV文件中列出每个气候箱中第 25、50、75 和 95百分位的产量。这些百分位数来自全球观测到的产量和气候箱数据集；例如，气候箱1中小麦的第95个百分位值为 3.763889。这意味着气候箱1中 95% 的小麦种植面积低于 3.763889 吨/公顷。第50个百分位将是“平均”产​​量，而第95个百分位将是通过改进耕作方式获得的接近最佳产量。
- **climate_regression_yield_tables** (回归模型):对于每种作物，每个气候箱的回归参数的 CSV 格式。
- **crop_nutrient.csv** (百分位数和回归模型): 显示每种作物营养价值的表格。
- **crop_to_climate_bin.csv** (percentile and regression models): A table that maps each crop name to the corresponding climate bin raster.
- **crop_to_observed_yield.csv** (percentile and regression models): A table that maps each crop name to the corresponding observed yield raster.
- **crop_to_percentile_yield.csv** (percentile model): A table that maps each crop name to the corresponding percentile yield table.
- **crop_to_regression_yield.csv** (regression model): A table that maps each crop name to the corresponding regression yield table.
- **extended_climate_bin_maps** (百分位模型):对于每种作物，该作物的气候箱的全球栅格（有关详细信息，请参阅Mueller等人2012年的补充方法）。
- **observed_yield** (百分位数模型):对于每种作物，2000年左右实际观测到的产量的全球栅格。


百分位模型
^^^^^^^^^^^^^^^^

百分位数模型的算法如下，对于每种作物类型（括号中为相应的输出）：

1. 将全球气候箱地图从**model_data/extended_climate_bin_maps/**裁剪到用户提供的土地覆盖地图的范围(**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**)
2. 对于每个百分位数(25th, 50th, 75th, 95th):

   a. 使用**model_data/climate_percentile_yield_tables**中的值对(1)中的裁剪气候地图进行重分类，以获得百分位数产量地图 (**intermediate_outputs/<crop>_yield_<percentile>_coarse_yield.tif**).
   b. 将其插值为与土地覆被地图相同的分辨率，将大的1/12度栅格更改为更平滑的渐变(**intermediate_outputs/<crop>_yield_<percentile>_interpolated_yield.tif**)
   c. 根据土地覆被地图遮盖未种植该作物的区域 (**<crop>_yield_<percentile>_production.tif**).

3. 将全球观测到的产量图**model_data/observed_yield/**剪裁到土地覆被地图的延伸，并将nodata栅格替换为零(**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
4. 将其插值为与土地覆被地图相同的分辨率，将大的 1/12 度栅格更改为更平滑的渐变(**intermediate_outputs/<crop>_interpolated_observed_yield.tif**)
5. 根据土地覆被地图遮盖未种植该作物的区域(**<crop>_observed_production.tif**).
6. 汇总产量值和营养值（使用**model_data/crop_nutrient.csv**中的数据),并将结果制成表格(**result_table.csv**).
7. 如果提供了聚合多边形向量，则对每个聚合多边形区域内的值求和并将它们制成表格(**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


回归模型
^^^^^^^^^^^^^^^^

回归模型的算法如下，对于每种作物类型（括号中为相应的输出）:

1. 将全球气候箱地图从**model_data/extended_climate_bin_maps/** 剪裁到用户提供的土地覆被地图的范围 (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**)
2. 对于每个回归参数:

   a. 使用**model_data/climate_regression_yield_tables** 中的值对(1)中的剪裁气候地图进行重分类，以获取回归参数值的地图(**intermediate_outputs/<crop>_<parameter>_coarse_regression_parameter.tif**)
   b. 将其插值为与土地覆被地图相同的分辨率，将大的1/12度栅格更改为更平滑的渐变(**intermediate_outputs/<crop>_<parameter>_interpolated_regression_parameter.tif**)

3. 对于每种肥料元素（氮、磷、钾）:

   a. 使用来自(2) 的回归参数栅格，基于该元素计算作物产量栅格 (**intermediate_outputs/<crop>_<element>_yield.tif**).

4. 通过从(3)中获取三个产量栅格的像素最小值来计算作物产量 (**<crop>_regression_production.tif**).
5. 将全球观测到的产量图从**model_data/observed_yield/** 裁剪到土地覆被地图的延伸部分，并将nodata栅格值替换为零(**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
6. 将其插值为与土地覆被地图相同的分辨率，将大的1/12度栅格更改为更平滑的渐变(**intermediate_outputs/<crop>_interpolated_observed_yield.tif**)
7. 根据土地覆被地图遮盖未种植该作物的区域(**<crop>_observed_production.tif**).
8. 汇总产量值和营养值（使用**model_data/crop_nutrient.csv**中的数据),并将结果制成表格(**result_table.csv**).
9. 如果提供了聚合多边形向量，则对每个聚合多边形区域内的值求和并将它们制成表格(**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


 作物回归本身(上面的步骤3和4) 来自Mueller et al. 2012 ，其形式为：

 .. math:: Y_{mod_{GC}}=\min(Y_{max}(1-b_{NP}\exp(-c_N N_{GC})), Y_{max}(1-b_{NP} \exp(-c_P P_{GC})), Y_{max}(1-b_K \exp(-c_K K_{GC})))

其中:math:`N_{GC}, P_{GC}, K_{GC}` 是用户提供的施肥率 (N=氮, P=磷, K= 钾), 其他回归参数作为全局数据提供给模型。



局限和简化
===============================

该模型当前版本主要由气候驱动和可选择管理驱动的一个粗略的全球模型，因此该模型无法捕捉到异构景观中发生的生产力变化。如果岩石山坡和肥沃的河谷具有相同的气候，则在当前模型中将分配相同的产量。这将产生一个问题，如果所关注的点在于：哪里可以优先考虑未来的栖息地转换；或者哪里的农业开发是最具有生产力和最具破坏性的。

数据需求
==========

有两种InVEST作物生产模型可用，一个基于百分位数的观察模型，用于对 172 种作物进行操作；另一个回归模型用于探索对 10 种作物的施肥率。除非另有说明，否则以下参数适用于这两种模型。

**Important**: 您需要下载用于作物生产的InVEST数据集，以获取所需的Monfreda数据集作为模型的输入。如果在安装 Invest 时选择安装作物生产示例数据，则Invest的安装文件夹中将有一个名为 ``sample_data\CropProduction`` 的文件夹，可以在其中找到此数据。或者，您可以从http://releases.naturalcapitalproject.org/?prefix=invest/下载, 转到该链接，单击目标版本，然后导航到``data`` 目录并选择``CropProduction.zip``.

另请参阅作物生产数据集，了解所有这些数据输入的示例。这将有助于了解文件类型、文件夹结构和表格格式。请注意，所有 GIS 输入必须采用相同的投影坐标系和线性单位米。

两个模型
--------

- :investspec:`crop_production_percentile workspace_dir`

- :investspec:`crop_production_percentile results_suffix`

- :investspec:`crop_production_percentile climate_bin_raster_table`

- :investspec:`crop_production_percentile observed_yield_raster_table`

- :investspec:`crop_production_percentile crop_nutrient_table`

- :investspec:`crop_production_percentile landcover_raster_path` 此栅格必须具有以米为单位的投影坐标系（例如 UTM），因为像素面积除以 10000 才能报告一些以公顷为单位的结果。只能有一个与每种独特作物类型关联的土地利用/土地覆被 （LULC） 类型。如果需要将多个 LULC 类分配给一个特定裁剪，则需要先将这些多个 LULC 类合并到 LULC 栅格中的单个类中，然后再在模型中使用它们。

- :investspec:`crop_production_percentile aggregate_polygon_path`


其他百分位数据需求
------------------

- :investspec:`crop_production_percentile percentile_yield_csv_table`

- :investspec:`crop_production_percentile landcover_to_crop_table_path` 每个唯一的作物类型只能有一个与土地覆被类相关联。有关详细信息，请参阅上面的土地利用/土地覆被说明。

  Columns:

  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.crop_name`

  Example:

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/landcover_to_crop_table.csv
    :header-rows: 1
    :name: Example Landcover to Crop Table

其他回归数据需求
--------------------------------

- :investspec:`crop_production_regression regression_yield_csv_table`

- :investspec:`crop_production_regression landcover_to_crop_table_path`

  Columns:

  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.crop_name`

- :investspec:`crop_production_regression fertilization_rate_table_path` 下面包括一个示例表，该表来自观察到的CBI施肥率的中值。用户可以在``sample_data_\CropProduction\model_data\cbi_mod_yield_use_as_check``中探索原始CBI数据。（有关获取这些数据的信息，请参阅上面的**重要**注释。.

  Columns:

  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.crop_name`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.nitrogen_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.phosphorus_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.potassium_rate`

  **Example fertilizer table:**

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/crop_fertilization_rates.csv
    :header-rows: 1
    :name: 作物施肥率示例。该值来自观测到的CBI肥料施肥率分布的中位数。


结果解释
====================

以下是作物生产模型每个输出的简短说明。最终结果可在为此模型运行指定的用户定义的工作区中找到。以下文件名中的"Suffix"是指模型的可选用户定义后缀输入。

- **aggregate_results_[Suffix].csv**: 如果提供了聚合结果多边形形状文件，则会生成一个表格，汇总每个多边形内的总观测/百分位数/建模产量和营养信息。

- **Crop Production Rasters**: 对于建模的每个作物，都有一个栅格 （.tif） 对应于该作物名称和建模类型 - “观测”、“回归”或“产量”加上百分位数（第 25 位/第 50 位/第 75 位/第 95 位）和用户提供的后缀。这些栅格表示该作物每个栅格的生产率，单位为公吨/像素每年。

- **result_table_[Suffix].csv**: 表格列出了运行中建模的所有作物、覆盖面积、百分位数或模拟产量、观察到的产量以及每种作物的营养信息。它是模型的主要输出。

还有一个**intermediate_output** 文件夹，其中包含许多表示最终结果计算中的中间步骤的文件。通常，不需要使用这些文件，但如果要调试模型运行或想要更好地了解中间步骤，可能会对它们感兴趣。它还包含一个子目录，该子目录存储内部使用的元数据，以避免重新计算。

**观察到的产量** 产出近似于2000年感兴趣地区的实际作物产量。如果作物目前不在感兴趣的地区种植，则**百分位数产量** 和**回归产量** 输出很有用，或者通过缩小产量差距来近似增加的潜力。

参考文献
==========

"Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000."" C. Monfreda N. Ramankutty, J. Foley. Biogeochemical Cycles, Vol.22, GB1022, doi:10.1029/2007GB002947. 2008

"Closing yield gaps through nutrient and water management" N Mueller, J. Gerber, M. Johnston, D. Ray, N. Ramankutty, J. Foley. Nature. 2012 Oct 11;490(7419):254-7. doi: 10.1038/nature11420. Epub 2012 Aug 29.
