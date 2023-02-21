.. _recreation:

**********************************
参观: 休闲和旅游业
**********************************

综述
=======

休闲和旅游是许多国家和地方经济的重要组成部分，他们以多种方式积极影响着
生活质量、地域感、社会联系、身体健康、学习、和其他无形资产。 为了量化自然环境的价值，InVEST投资模型基于自然栖息地的位置和其他影响人们选择休闲地点的特性因素，预测了休闲的人员-天数的分布。该工具通过一个简单的线性回归估计了每个属性对访问率的贡献情况。如果缺少访问的历史数据，我们会使用访问代理来对模型参数化：发布在flickr网站上的地理标记图片。使用照片-用户-天数的估计模式，该模型可以预测未来的自然要素的变化将会如何改变访问率。该工具输出绘制了娱乐用途的当前模式，同时显示了选择性情景下的未来使用模式。

**娱乐模型旨在回答这些基本问题:**  

1) 穿越景观或一组站点的 *相对* 访问率是多少？

2) 自然/建筑环境的哪些特征会影响访问率的空间格局, 这些特征的相对影响水平是多少？

3) 假设自然/建筑特征的空间格局发生了改变，那么访问率将如何变化以应对？ 

简介
============

休闲和旅游是许多国家和地方经济的重要组成部分，他们以多种方式积极影响着
生活质量、地方感、社会联系、身体健康、学习、和其他无形资产。 研究休闲或旅游模式的一个关键原因是这个行业的经济意义。在2011年，旅行和旅游对全球国内生产总值(GDP)的总贡献值大约为60亿美元（占GDP的9%），预计到2022年，增长为10亿美元(World Travel and Tourism Council 2012). 当然，经济影响只是衡量休闲和旅游重要性的一种方法。这些活动也是人类福祉的不同方面的至关重要的贡献者(Russell et al. 2013)。例如，对许多人来说，户外休闲是一种精神体验(eg Trainor and Norgaard 1999), 而社会与大自然之间的互动有助于构建地域感(e.g. Willox et al. 2012)。

娱乐的一个不断增长的主要部分是它的“自然取向”，其中包括与自然环境之间的互动、或者是对自然环境的欣赏 (Balmford et al. 2009)。这些类型的活动，环境特征会影响人们对于休闲地点、休闲事件、以及休闲方式的选择。例如，潜水员会根据水的清澈度、水的温度以及海洋生物的多样性来选择地点 (Williams and Polunin 2000, Uyarra et al. 2009)。鸟类观察家会被吸引到最好的地方来观察目标物种 (Naidoo and Adamowicz 2005), 而这些地方的自然系统必然能够支撑相应的鸟类群体(Puhakka et al. 2011)。一些休闲活动会取决于环境属性，例如物种丰富度 (Loureiro et al. 2012)、栖息地的多样性(Neuvonen et al. 2010, Loureiro et al. 2012)、降水情况(Loomis and Richardson 2006)、温度(Richardson and Loomis 2005)、以及其他属性，比如基础设施和文化景点(Mills and Westover 1987, Hill and Courtney 2006)。

.. _rec-the-model:

模型
=========

InVEST模型的目的是，基于自然栖息地的位置、可达性、以及其他影响人们选择
休闲地点的建设特点，例如道路，来预测休闲的人员-天数的分布 (Adamowicz et al. 2011)。该工具输出绘制了休闲用途的当前模式，同时显示了选择性情景下的未来使用模式。

.. _rec-how-it-works:

工作原理
------------

该模型显示跨景观（格网像元）或离散区域（多边形）的访问率，并可选择构建回归模型，以使用简单的线性回归来估计景观属性对访问率的贡献情况:

.. math:: y_i = \beta_{0} + \beta_1 x_{i1} + ... + \beta_{p} x_{ip} \text{ for } i = 1 ... n,

where :math:`x_{ip}` 是每个单元或多边形（以下简称“单元格”）中每个属性的覆盖范围,:math:`i`, 该单元属于包含math:`n` 个单元的感兴趣区域 (AOI)。 如果缺少访问:math:`y_i`, 我们会使用访问代理来对模型参数化： 发布在flickr网站上的地理标记图片（更多相关信息请参考`rec-photos`）。InVEST休
闲模型会重新开始，预测该区域内的休闲的人员-天数的分布。它通过使用地方属性来完成这一步骤，例如自然特征（如：公园）、建设特征（如：道路）、以及人为使用（如：工业活动）等等。

工具首先通过获取每个单元格平均照片-用户-天数+1的自然对数，来对所有math:`y_i` 值进行对数转换。taking the natural log of average photo-user-days per cell + 1. 然后，通过简单线性回归来估计研究区域内的所有网格单元的每个属性对对数转换访问率的影响。这些估计(the :math:`\beta_{p}` 值)可以用于其他的模型运行，进而预测景观的未来变化将会如何改变访问率。模型通过python库的科学计算基础包（numpy）中的线性最小二乘函数来执行普通最小二乘回归(van der Walt et al. 2011)。

.. _rec-photos:

照片 用户 天数
--------------------

由于访问者数量的精细数据是以任何研究地区的一些特定地点为基础进行收集的， 因此我们假设可以通过上传照片至照片分享网站`flickr <https://www.flickr.com>`_ 的年度工作量的总数来近似得出当前的访问情况。在flickr上的许多照片已经包含了一个特定的纬度/经度。使用这个位置信息、以及摄影师的用户名和照片拍摄日期， InVEST 模型计算每个网格单元或多边形的总工作量（照片-用户-天数）。 一个地点的工作量（照片-用户-天数）代表一个特定摄影师在特定日期至少拍摄了一张照片。对于每个单元格，模型对 2005-2014 年所有天数（或这些年份内用户定义的范围）的照片-用户-天数求和，并返回平均年照片-用户-天数(PUD_YR_AVG)。PUD_YR_AVG 是 在上面等式中的:math:`y_i` 。

我们已经观察到，每年访问一个地点的人数与在相同区域拍摄的照片的数量有关，同时也与在836个世界游客景点中上传至flickr数据库的照片数量相关(Wood et al. 2013)。照片的密度会在空间上有所变化，它影响了可以用于分析的
单元大小（参考初始工具：单元大小）。 (see :ref:`rec-data-needs`: 像元大小)。PUD 计算是在由自然资本项目策划和维护的广泛全球数据集上的远程服务器上计算的。

预测变量
-------------------

在上面的回归方程中, 照片-用户-天数 是 :math:`y_i` 的变量和所有:math:`x` 变量为预测变量。这些是感兴趣区域中的要素，可能会影响整个空间的访问模式。用户可以提供任意数量的预测变量，模型将进行回归计算，该回归估计每个预测变量的math：'beta_{p}' 值。 :math:`\beta_{p}` 表示在考虑回归中包含的所有其他预测变量后，预测变量与访问率之间的关系。

我们发现，经常考虑以下几大类中至少一个变量是非常有帮助的：自然资本（如
栖息地、湖泊）、建设资本（如道路、酒店）、工业活动以及访问或成本（如：与主要机场之间的距离）。通常，代表每一类的单一变量可以解释照片-用户-天数中的大部分的变动原因。此工具允许用户提供 GIS 格式的预测变量，并以多种方式处理这些图层 (详见:ref:`rec-data-needs` 部分).

情景分析
-----------------

如果计算回归，则模型可以选择在给定一组表示未来或备选方案的修改预测变量的情况下估计访问率。方案预测变量应表示被选为预测变量的相同特征，但可以表示这些特征的修改版本 (例如修改道路网络、增加酒店点、改变栖息地分布等)。场景预测是使用上文的回归方程进行的。首先，按照 :ref:`rec-how-it-works` 中所述估计每个预测变量的系数，然后将这些系数应用于已针对方案修改的每个预测变量的值。有关准备方案数据的更多详细信息，请参阅:ref:`rec-data-needs` 部分。

限制和简化
-------------------------------

该模型并未预先假定任何预测变量会对访问情况有所影响。相反，该工具根据感
兴趣地区的当前访问情况的空间因素，估计了每个预测变量的影响程度。 每个单元的照片-人员-天数的值均可作为访问的代理测量，并且相对于所有单元的预测变量值有所退化。在随后的模型运行中，基于预测因素的空间配置，该工具使用在初始模型运行中计算得出的:math:`\beta_{p}` 值来预测未来情景下的访问情况。这一步需要假定人们对模型中作为预测因素的属性的反应不会随着时间而改变。换句话说，在未来，人们将继续像当下的情况一样，因这些属性而吸引或排斥。


.. _rec-data-needs: 

数据需求
==========

.. note:: 预测变量表中引用的所有 GIS 数据必须与感兴趣区域 （AOI） 面矢文件位于相同的*投影* 坐标系中。所有距离、长度和面积计算都使用与 AOI 坐标系相同的单位。

- :investspec:`recreation.recmodel_client workspace_dir`

- :investspec:`recreation.recmodel_client results_suffix`

- :investspec:`recreation.recmodel_client aoi_path` 建议以线性单位投影此向量，尤其是在用于计算回归和场景时。结果将聚合到这些面。

- :investspec:`recreation.recmodel_client start_year`
- :investspec:`recreation.recmodel_client end_year`

- :investspec:`recreation.recmodel_client compute_regression` 如果未选择此选项，则结果将仅限于 AOI 面或网格像元中当前访问率的地图。

- :investspec:`recreation.recmodel_client predictor_table_path` 这些预测因子是:ref:`rec-how-it-works` 中描述的:math:`x_{ip}` 值。

    列:

    - :investspec:`recreation.recmodel_client predictor_table_path.columns.id`
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.path` 在下面的示例中，路径序列中列出的文件与Predictor_Table.csv文件位于同一文件夹中。预测器文件可能位于其他位置，但此表中必须包含它们的完整路径或相对于此 CSV 文件的路径。
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.type`

    **示例预测变量表:**
    
    .. csv-table::
       :file: ../../invest-sample-data/recreation/predictors.csv
       :header-rows: 1
       :widths: auto

- :investspec:`recreation.recmodel_client scenario_predictor_table_path` 此表与上述预测变量表具有相同的列和格式。

- :investspec:`recreation.recmodel_client grid_aoi`

- :investspec:`recreation.recmodel_client grid_type`

- :investspec:`recreation.recmodel_client cell_size` 像元大小和 **与AOI的线性单位相同**。例如, 如果 AOI 位于以米为单位的 UTM 投影中，则像元大小参数也将以米为单位。

   .. note:: 网格像元的数量会极大地影响处理时间。 如果不确定要指定哪个像元大小，请在第一次选择非常大的像元大小（10 km 或更大），然后根据需要以较小的像元大小重新运行模型。像元的适当大小和数量取决于几个因素，包括研究的目标和照片的密度，这些因素因地区而异。为了使模型能够计算预测变量的影响（如:ref:`rec-how-it-works` 部分所述），用户必须选择足够大的像元大小，以便大多数像元包含照片。我们建议用户首先运行像元大小在 10-100 km 之间的模型，具体取决于 AOI 的总面积。然后，迭代评估模型输出（在:ref:`rec-interpreting-results` 中描述）并重新运行模型以确定适当的像元大小。


.. _rec-running-model:

模型运行
=================

.. warning:: 娱乐模型需要连接到互联网。

该模型使用接口输入所有必需和可选数据（参见：:ref:`rec-data-needs`）。 AOI面矢量文件文件被发送到由自然资本项目管理的服务器，在那里执行照片-用户-天数计算。因此，此模型需要连接到互联网。该模型可以使用三种配置运行：

#. 获取您感兴趣区域的访问率地图. 提供"工作区"和"感兴趣区域", 不要选中"计算回归"。结果包括 "pud_results.shp" (:ref:`rec-interpreting-results`)。
#. 获取访问率地图并使用一组预测变量计算回归。提供"工作区" 和"感兴趣区域"，选中 "计算回归" 并且提供 "预测变量表" :ref:`rec-data-needs`. 结果包括"pud_results.shp", "predictor_data.shp", 和 "regression_coefficients.txt" (:ref:`rec-interpreting-results`).
#. 估计方案的访问率。提供 "工作区" 和"感兴趣区域"， 选中 "计算回归" 并且提供 "预测变量表" 和 "情景预测变量表" (:ref:`rec-data-needs`). 结果包括"pud_results.shp", "predictor_data.shp", "regression_coefficients.txt", 和 "scenario_results.shp" (:ref:`rec-interpreting-results`).

运行模型所需的时间因 AOI 的范围、格网像元的数量以及预测变量图层的数量和大小而异。我们建议用户先运行模型而不计算回归，如果网格化AOI，则从较大的像元大小开始。

请注意，执行分析的服务器还会记录每个用户的 IP 地址。

.. _rec-interpreting-results:

解释结果
====================

模型输出
-------------

+ **pud_results.shp**: 此多边形面矢量文件的特征与原始 AOI 面矢量文件匹配，如果选择了“网格化 AOI”选项，则与 AOI 的网格化版本匹配。这些属性包括原始 AOI 形状文件中存在的所有属性列，以及：

  + **PUD_YR_AVG** 是每年的平均照片-用户-天数 (:ref:`rec-photos`)。这对应于伍德等人（Wood et al.2013）描述的平均*PUD*。

  + **PUD_JAN**, PUD_FEB, .... PUD_DEC是每个月的平均照片用户天数。例如，如果日期范围是默认的 2005-2014，则PUD_JAN是 所有10个1 月照片-用户-天数的平均值。

+ **monthly_table.csv**:  

  + 此表包含所选日期范围内每个月在每个单元格中计算的总-照片-用户-天数。此表中的每一行都是唯一的 AOI 格网像元或多边形。列表示月份("2005-1" 表示2005年1月, "2014-12" 表示2014年12月).

+ **predictor_data.shp** (选择计算回归时的输出):

  + 此 shapefile 具有与"pud_results.shp"中匹配的多边形，并且具有由预测器表中给出的 id 定义的字段。这些字段的值是每个响应要素计算的指标(:ref:`rec-data-needs`:预测变量表).

+ **regression_coefficients.txt** (选择计算回归时的输出):

  + 这是回归分析的文本文件输出。它包括每个预测变量的 :math:`\beta_p`估计值（参见:ref:`rec-how-it-works`）。它还包含一个“服务器 ID 哈希”值，可用于将 PUD 结果与 PUD 服务器上可用的数据相关联。如果在发布中使用这些结果，则应将此哈希包含在结果中，以实现可重现性。

+ **scenario_results.shp** (如果提供了情景预测变量表，则输出):

  + 此shapefile 与"predictor_data.shp"匹配，但其字段来自方案预测器表中定义的预测变量，并且还有一个附加字段“PUD_EST”，它是每个面的估计PUD_YR_AVG。

+ **natcap.invest...client-log...txt** 

  + 此文本文件是每次运行模型时自动生成的日志。它可用于解决错误问题。日志顶部还记录了为该模型运行选择的所有输入值。

.. _rec-references:

参考
==========

Adamowicz, WL, R Naidoo, E Nelson, S Polasky, J Zhang. 2011. Nature-based tourism and recreation. In: Kareiva P, G Daily, T Ricketts, H Tallis, S Polasky (eds) Natural Capital: Theory and Practice of Mapping Ecosystem Services. Oxford University Press, New York.

Balmford, A, J Beresford, J Green, R Naidoo, M Walpole, A Manica. 2009. A global perspective on trends in nature-based tourism. PLoS Biology 7: e1000144.

Hill, GW, PR Courtney. 2006. Demand analysis projections for recreational visits to countryside woodlands in Great Britain. Forestry 79: 18-200.

Loomis, JB, RB Richardson. 2006. An external validity test of intended behavior: comparing revealed preference and intended visitation in response to climate change. Journal of Environmental Planning and Management 49: 621-630.

Loureiro, ML, F Macagno, PA Nunes, R Tol. 2012. Assessing the impact of biodiversity on tourism flows: an econometric model for tourist behaviour with implications for conservation policy. Journal of Environmental Economics and Policy 1: 174-194.

Mills, AS, TN Westover. 1987. Structural differentiation: a determinant of park popularity. Annals of Tourism Research 14: 486-498.

Naidoo, R, WL Adamowicz. 2005. Biodiversity and nature-based tourism at forest reserves in Uganda. Environment and Development Economics 10: 159-178.

Neuvonen, M, E Pouta, J Puustinen, T Sievänen. 2010. Visits to national parks: effects of park characteristics and spatial demand. Journal for Nature Conservation 18: 224-229.

Puhakka, L, M Salo, IE Sääksjärvi. 2011. Bird diversity, birdwatching tourism and conservation in Peru: a geographic analysis. PLoS One 6: e26786.

Richardson, R, JB Loomis. 2005. Climate change and recreation benefits in an alpine national park. Journal of Leisure Research 37: 307-320.

Russell, R, AD Guerry, P Balvanera, RK Gould, X Basurto, KM Chan, S Klain, J Levine, J Tam. 2013. Humans and nature: how knowing and experiencing nature affect well-being. Annual Review of Environment and Resources 38: in press.

Trainor, SF, RB Norgaard. 1999. Recreation fees in the context of wilderness values. Journal of Park and Recreation Administration 17: 100-115.

Uyarra, MC, AR Watkinson, IM Côté. 2009. Managing dive tourism for the sustainable use of coral reefs: validating diver perceptions of attractive site features. Environmental Management 43: 1-16.

van der Walt, Stéfan, S. Chris Colbert, and Gaël Varoquaux. 2011. The NumPy Array: A Structure for Efficient Numerical Computation. Computing in Science & Engineering 13 (2): 22–30. 

Williams, ID, NV Polunin. 2000. Differences between protected and unprotected reefs of the western Caribbean in attributes preferred by dive tourists. Environmental Conservation 27: 382-391.

Willox, AC, SL Harper, JD Ford, K Landman, K Houle, V Edge. 2012. "From this place and of this place:" climate change, sense of place, and health in Nunatsiavut, Canada. Social Science and Medicine 75: 538-547.

Wood, SA, AD Guerry, JM Silver, M Lacayo. 2013. `Using social media to quantify nature-based tourism and recreation <https://www.nature.com/articles/srep02976>`_. Scientific Reports 3: 2976.

World Travel and Tourism Council. 2012. `Travel and Tourism: Economic Impact <http://www.ontit.it/opencms/export/sites/default/ont/it/documenti/files/ONT_2012-03-23_02800.pdf>`_.
