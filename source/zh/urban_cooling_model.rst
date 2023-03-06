.. _ucm:

*******************
城市降温模型
*******************

总结
=======

对于近年来经历了热浪的许多城市来说，城市降温(HM)是优先考虑的问题。植被可以通过提供阴凉、改变城市肌理的热特性和通过蒸散发增加冷却，从而帮助减少城市热岛效应。通过降低死亡率和发病率，提高舒适度和生产力，以及减少对空调(A/C)的需求，这对公民的健康和福祉产生了影响。InVEST城市降温模型根据荫凉度、蒸散和反照率以及与降温岛(如公园)的距离计算了一个减热指数。该指数被用来估计植被的温度降低。最后，该模型使用两种(可选的)估值方法:能源消耗和工作生产率来估算热缓解服务的价值。

介绍
============

影响着世界各地的许多城市，对人类健康和福祉造成重大后果:热浪期间死亡率或发病率高，空调消耗高，舒适度或工作效率降低。UHI效应，即农村和城市之间的温度差异，是城市独特特性的结果，这主要是由于两个因素:在城市地区使用的材料(如混凝土、沥青)的热性能，它们储存更多的热量，以及植被的降温效应(通过遮荫和蒸散发)的降低。

因此，自然基础设施在减少城市的UHIs方面发挥了作用。利用快速增长的城市热建模文献(Deilami等人，2018年)，InVEST城市降温模型基于有关气候、土地利用/土地覆盖(LULC)和(可选)空调使用的常用数据，估算了植被的降温效应。

模型
=========

工作原理
------------

制冷量指数
^^^^^^^^^^^^^^^^^^^^^^

该模型首先基于局部阴影、蒸散发和反照率计算每个像素的制冷量(CC)指数。该方法基于Zardo等人2017年和Kunapo等人2018年提出的指数，其中我们添加了反照率，这是热量减少的一个重要因素。

荫蔽系数('shade')表示与每个土地利用/土地覆盖(LULC)类别相关的树冠层(≥2米高)的比例。取值为0 ~ 1。
蒸散发指数(ETI)是潜在蒸散发的归一化值，即植被的蒸散发(或无植被地区的土壤蒸发量)。每个像素的计算方法是:将参考蒸散发(:math:`ET0`，由用户提供)和作物系数(:math:`Kc`，与像素的LULC类型相关)相乘，并除以关注区域的:math:`ET0`栅格的最大值:math:`ETmax`.:。

.. math:: ETI = \frac{K_c \cdot ET0}{ET_{max}}
    :label: eti

注意，这个方程假设植被地区得到充分灌溉(尽管可以降低Kc值来表示水有限的蒸散发)。

反照率因子是一个介于0到1之间的值，表示被LULC类型反射的太阳辐射的比例(Phelan et al. 2015)。

该模型综合了CC指数中的三个因素:

.. math:: CC_i = 0.6 \cdot shade + 0.2\cdot albedo + 0.2\cdot ETI
    :label: coolingcapacity_factors

推荐权重(0.6;0.2;0.2)基于经验数据，反映了遮荫比蒸散发的影响更高。例如，Zardo等人2017年的报告称，“在小于2公顷的地区[蒸散量]被分配的权重为0.2，阴影为0.8。在超过2公顷的地区，[蒸散量]和遮荫量的权重分别改为0.6和0.4”。在本模型中，我们建议在式(83)中分解阴影和反照率的影响，并基于Phelan等人2015年的研究结果(见表2，植被和反照率的系数相似)将反照率的权重赋予ETI。

注意:用户可以手动输入备选权值，以测试模型输出对该参数的敏感性(或者是否有本地知识)。

该模型还可以考虑另一个因素，强度(:math:`building.intensity` 用于给定的土地覆盖分类)，它可以捕捉已建基础设施的垂直维度。建筑物的强度是夜间温度的一个重要预测指标，因为建筑物在白天储存的热量在夜间会被释放出来。为了预测夜间温度，用户需要在生物物理表中为每个土地使用类别提供建筑强度因子，模型将更改方程:math:numref:`coolingcapacity_factors` 为:

.. math:: CC_i = 1 - building.intensity
    :label: coolingcapacity_intensity


城市减热指数(大型绿地的影响)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

为了考虑大型绿地(>2 ha)对周边地区的降温效应(见Zardo等人2017年和McDonald等人2016年的讨论)，该模型计算了城市HM指数:如果像素不受任何大型绿地的影响，则HM等于CC，否则设置为大型绿地和感兴趣像素的CC值的距离加权平均值。

为此，模型首先计算搜索距离内的绿地面积:math:`d_{cool}`围绕每个像素(:math:`GA_i`)，以及每个公园(:math:`CC_{park_i}`)提供的CC:

.. math:: {GA}_{i}=cell_{area}\cdot\sum_{j\in\ d\ radius\ from\ i} g_{j}
    :label: [3a]

.. math:: CC_{park_i}=\sum_{j\in\ d\ radius\ from\ i} g_j \cdot CC_j \cdot e^{\left( \frac{-d(i,j)}{d_{cool}} \right)}
    :label: [3b]

其中:math:`cell_{area}` 是ha单元格的面积，:math:`g_j` 是1，如果像素:math:`j` 是绿色空间，如果不是0，:math:`d(i,j)` 是像素之间的距离:math:`i` 和:math:`j`，:math:`d_{cool}` 是绿色空间具有冷却效果的距离，和:math:`CC_{park_i}` 是可归结为绿色空间的CC值的距离加权平均。(注意，符合“绿色空间”条件的LULC类是由用户在生物物理表中使用参数"green spaces"来确定的，参见第3节的输入表。)接下来，计算HM指数为:

.. math:: HM_i = \begin{Bmatrix}
        CC_i & if & CC_i \geq CC_{park_i}\ or\ GA_i < 2 ha \\
        CC_{park_i} & & otherwise
        \end{Bmatrix}
    :label: [4]

空气温度估计
^^^^^^^^^^^^^^^^^^^^^^^^^

为了估计整个城市的热量减少，该模型使用(城市尺度)UHI量级:math:`UHI_{max}`。用户可以从当地文献或全球研究中获得UHI值:例如，由耶鲁大学开发的全球地表UHI Explorer提供了年度、季节、白天和夜间UHI的估计数(https://yceo.users.earthengine.app/view/uhimap)。
注意，UHI量级是根据特定时期(例如当前或未来气候)和时间(例如夜间或白天温度)定义的。期间和时间的选择会影响到服务的量化和估值。

没有空气混合的空气温度:math:`T_{air_{nomix}}` 为每个像素计算如下:

.. math:: T_{air_{nomix},i}=T_{air,ref} + (1-HM_i)\cdot UHI_{max}
    :label: [5]

式中:math:`T_{air,ref}` 是农村参考温度，:math:`UHI_{max}` 是城市UHI效应的最大幅度(或者更准确地说，是:math:`T_{air,ref}` 与城市观测到的最高温度之间的差值)。

由于空气混合，这些温度在空间上是平均的。实际空气温度(含混合) :math:`T_{air}`由:math:`T_{air_{nomix}}`推导而来，使用的是一个高斯函数，其核半径为:math:`r`，由用户定义。

对于每个感兴趣的区域(这是用户提供的矢量GIS层)，我们计算平均温度和温度异常:math:`(T_{air,i} - T_{air,ref})`。
	
减热服务的价值
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

降温的价值至少可以用三种方法来评估:

    i)空调耗电量减少所节省的能源;
    ii) 提高户外工作者的工作效率;
    iii) 减少与高温有关的发病率和死亡率。

该模型提供了(i)能源节约和(ii)基于全球回归分析或本地数据的工作生产率的估计。

**节能:** 该模型利用能耗和温度之间的关系(如Santamouris等人在2015年总结的)来计算建筑的节能和相关成本:math:`b`:

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}})
    :label: energy_savings_kwh

式中：

    * :math:`consumption.increase(b)` (kWh/° C/:math:`m^2`)是当地对每平方米建筑面积每一度温度的能耗增加的估计，建筑类别:math:`b`。
    * :math:`T_{air,MAX}` (° C)是景观上的最高温度:math:`(T_{air,ref} + UHI_{max})`;
    * :math:`\overline{T_{air,MAX} - T_{air,i}}` (° C)是建筑的平均气温差:math:`b`，与:math:`T_{air,i}` 在前面的步骤建模。

如果为每个建筑类别提供成本，则将:math:numref:`energy_savings_kwh` 替换为equation :math:numref:`energy_savings_dollars`

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}}) \cdot cost(b)
    :label: energy_savings_dollars

式中:

    * :math:`cost(b)` Note that this is very likely to be equal for all buildings. 是建筑类别:math:`b` 的每千瓦时能源成本估算。注意，这对所有建筑来说都是一样的。

为了计算总节能，我们将感关注区域的像素级值相加。

**工作效率:** 该模型将空气温度转换为湿球球温度(WBGT)，计算热量对工作效率的影响。WBGT考虑了湿度，可以通过以下方法从标准气象数据中估算(美国运动医学学院，1984，附录I):

.. math:: WBGT_i = 0.567 \cdot T_{air,i} + 0.393 \cdot e_i + 3.94
    :label: [7]

式中:

　　* :math:`T_{air}` = 模型提供的温度(干球温度(°C))
　　    * :math:`e_i` = 水汽压(hPa)

蒸汽压由温度和相对湿度计算，公式如下:

.. math:: e_i = \frac{RH}{100} \cdot 6.105 \cdot e^{\left ( 17.27 \cdot \frac{T_{air,i}}{(237.7 + T_{air,i})} \right )}
    :label: [8]

式中:

　　* :math:`RH` = 用户提供的平均相对湿度(%)
　　
对于每个像素，模型计算两种工作强度下的生产力损失(%):“轻工作”和“重工作”(基于不同工作强度下所需的休息时间，如Kjellstrom et al. 2009的表2):

.. math:: Loss.light.work_i = \begin{Bmatrix}
        0 & if & WBGT < 31.5\\
        25 & if & 31.5 \leq WBGT < 32.0 \\
        50 & if & 32.0 \leq WBGT < 32.5 \\
        75 & if & 32.5 \leq WBGT \\
        \end{Bmatrix}
    :label: [9a]

.. math:: Loss.heavy.work_i = \begin{Bmatrix}
        0 & if & WBGT < 27.5\\
        25 & if & 27.5 \leq WBGT < 29.5 \\
        50 & if & 29.5 \leq WBGT < 31.5 \\
        75 & if & 31.5 \leq WBGT \\
        \end{Bmatrix}
    :label: [9b]

这里，“轻工作”对应的代谢率约为200瓦，即办公室伏案工作和服务行业，而“重工作”对应的代谢率为400瓦，即建筑或农业工作。如果无法获得有关总劳动力部门分布的特定城市数据，用户可以利用世界银行国家一级的数据(例如世界银行数据)估计该城市在3个部门(服务、工业、农业)的工作人口。“在工业界工作，男性(%)”及类似情况)。根据表2 (Kjellstrom et al. 2009)中的休息时间和不同部门的工作人口比例，可以计算给定温度下的工作时间损失。如果有关于不同部门的平均时薪的当地数据，这些工作时间上的损失就可以转化为金钱上的损失。

最后，对于“轻工作”，请注意空调的流行也可以发挥作用。如果大多数办公楼都配备了空调，用户可能希望减少服务部门的工作时间损失，减少的比例与空调普及的比例相同。

限制和简化
===============================

由于上面描述的简化，该模型存在一些限制，在这里总结。

CC指数:CC指数依赖于经验权重，来自有限数量的案例研究，它调节了有助于冷却效应的关键因素的影响(式(83))。正如Zardo等人在2017年所述，该加权步骤包含高度不确定性。为了描述和减少这种不确定性，用户可以测试模型对这些参数的敏感性，或进行实验研究，从而深入了解阴影、反照率和蒸散发的相对影响。

大型公园和空气混合的效果:两个参数捕捉大型绿地和空气混合的效果(:math:`d_{cool}`和:math:`r`)。这些参数的值很难从文献中推导出来，因为它们随植被特性、气候(大型绿地的影响)和风模式(空气混合)而变化。与CC类似，用户可以通过测试模型对这些参数的敏感性，并将模型估计的温度空间模式与观测或建模数据进行比较，来表征和减少这些不确定性(见Bartesaghi等人，2018年和Deilami等人2018年了解更多关于这种比较的见解)

估值选项:目前模型支持的估值选项与A/C空调能耗和室外作业生产率相关。对于A/C空调的能耗，用户需要评估A/C空调的普及程度，并相应地降低估算值(即按A/C空调的实际使用比例降低能耗)。

尽管城市高温对健康的影响非常重要(McDonald等，2016年)，但目前模型中未包括对城市高温对健康影响的估值。这是因为这些影响在不同城市之间差异巨大，很难推断目前主要基于全球北部的知识(Campbell et al. 2018)。获得健康影响估计的可能办法包括:

* 使用McMichael等人2003年的全球数据，他们使用阈值温度以上的线性关系来估计每年可归因于高温天气的死亡比例，
* 在美国的应用中，基于全国范围内死亡率和温度变化之间的关系开发了一种方法:见McDonald等人，2016。

Gasparrini等人2014年分析了13个国家384个城市因高温导致的死亡率上升。InVEST模型的:math:`T_{air,i}`输出可用于确定归因于热的死亡率比例(首先确定哪个百分位数:math:`T_{air,i}`，然后使用附录中的表S3或表S4)。


数据需求
========

.. note:: *所有空间输入必须具有完全相同的投影坐标系* (以米为线性单位)，*而不是* 地理坐标系(以度为单位)。

- :investspec:`urban_cooling_model workspace_dir`

- :investspec:`urban_cooling_model results_suffix`

- :investspec:`urban_cooling_model lulc_raster_path` 该模型将使用该层的分辨率重新采样所有输出。分辨率应该足够小，以捕捉景观中绿色空间的效果，尽管LULC类别可以包括植被和非植被覆盖的混合(例如。“住宅”，树冠盖度可达30%)。

- :investspec:`urban_cooling_model biophysical_table_path`

  列:

  - :investspec:`urban_cooling_model biophysical_table_path.columns.lucode`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.kc`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.green_area` Green areas larger than 2 hectares have an additional cooling effect.
  - :investspec:`urban_cooling_model biophysical_table_path.columns.shade`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.albedo`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.building_intensity`

- :investspec:`urban_cooling_model ref_eto_raster_path` These values can be for a specific date or monthly values can be used as a proxy.

- :investspec:`urban_cooling_model aoi_vector_path` The AOI(s) will typically be city or neighborhood boundaries.

- :investspec:`urban_cooling_model green_area_cooling_distance` This is :math:`d_{cool}` in equation :eq:`[3b]`. Recommended value: 450 m.

- :investspec:`urban_cooling_model t_ref` This is :math:`T_{air,ref}` in equation :eq:`[5]`.这可能是某个特定日期的夜间或白天温度，也可能是几天的平均温度。结果将给出相同的兴趣期。

- :investspec:`urban_cooling_model uhi_max` This is :math:`UHI_{max}` in equation :eq:`[5]`.

- :investspec:`urban_cooling_model t_air_average_radius` 初始运行建议取值范围:500m ~ 600m;参见Schatz等人2014年和Lonsdorf等人2021年。

- :investspec:`urban_cooling_model cc_method`

- :investspec:`urban_cooling_model building_vector_path`

  字段:

  - :investspec:`urban_cooling_model building_vector_path.fields.type`

- :investspec:`urban_cooling_model do_energy_valuation`
- :investspec:`urban_cooling_model do_productivity_valuation`

- :investspec:`urban_cooling_model energy_consumption_table_path`

  列

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.type`
  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.consumption`

    .. note::
      **消耗** 值是每单位 *占地* 面积，而不是建筑面积。此值必须根据这种类型的结构的平均层数进行调整。

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.cost` 对于所有的建筑类型，这一列中的值很可能是相同的。

- :investspec:`urban_cooling_model avg_rel_humidity`

- :investspec:`urban_cooling_model cc_weight_shade`
- :investspec:`urban_cooling_model cc_weight_albedo`
- :investspec:`urban_cooling_model cc_weight_eti`

解释结果
====================

* hm_[Suffix].tif: 计算的HMI。
* uhi_results_[Suffix].shp:输入向量“Area of Interest”的副本，包含以下附加字段:
    * "avg_cc" - 平均CC值 (-).
    * "avg_tmp_v" - 平均温度值 (degC).
    * "avg_tmp_an" - 平均温度异常 (degC).
    * "avd_eng_cn" - (可选)避免能源消耗(如在能源消耗表中提供可选能源“成本”输入栏，则为千瓦时或$)。
    * "avg_wbgt_v" - (可选)平均体重(degC).
    * "avg_ltls_v" - (可选)轻工作效率损失(%)。
        * "avg_hvls_v" -.(可选)工作效率损失严重(%)。

* buildings_with_stats_[Suffix].shp: 输入向量"Building Footprints"的副本，包含以下附加字段:
    * "energy_sav" -能源节约价值(如能源消耗表中提供可选的能源“成本”输入栏，则以千瓦时或货币计算)。节省是相对于一个理论场景，即城市不包含自然区域和绿地;其中CC = 0适用于所有的LULC类。
    * "mean_t_air" -建筑物平均温度值（degC).

中间文件夹包含额外的模型输出:

* cc_[Suffix].tif: CC值的栅格。
* T_air_[Suffix].tif: 估计空气温度值的栅格。
* T_air_nomix_[Suffix].tif: 在空气混合之前(即在应用移动平均算法之前)估计空气温度值的栅格。
* eti_[Suffix].tif:实际蒸散发值的栅格(参考蒸散发乘以作物系数"Kc")。
* wbgt_[Suffix].tif: 计算WBGT的栅格。
* reprojected_aoi_[Suffix].shp: 用户定义的兴趣区域，重新投影到LULC的空间参考。
* reprojected_buildings_[Suffix].shp: 用户定义的建筑矢量，重新投影到LULC的空间参考。

附录:数据来源和参数选择指南
===========================================================

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

:ref:`Kc <kc>`
--------------

:ref:`Reference Evapotranspiration <et0>`
-----------------------------------------

:ref:`Building Footprints <buildings>`
--------------------------------------

反照率
------
城市已建成基础设施的反照率可以在当地的小气候文献中找到。Deilami等人2018和Bartesaghi等人2018提供了有用的回顾。Stewart和Oke(2012)提供了典型LULC类别的值范围。

绿地最大冷却距离
-----------------------------------
大型城市公园(2公顷)有降温效果的距离(米)。参见Zardo等人2017年的一篇短文，其中包括一项研究，报告了在五倍于树高的距离上的降温效应。在缺乏当地研究的情况下，估计可以使用4.5亿美元。

基准空气温度
------------------------
农村参考温度(°C)可从当地温度站或全球气候数据获得。

城市热岛效应的量级
---------------------------
即城市最高气温与乡村参考(基线)气温之差。在缺乏本地研究的情况下，用户可以从耶鲁大学进行的一项全球研究中获得值:https://yceo.users.earthengine.app/view/uhimap

最大混合距离
-----------------------------------------
搜索半径(米)用于移动平均线，以说明空气混合。根据试点城市(美国明尼阿波利斯-圣保罗和法国巴黎)的初步测试，推荐的初始值范围为500米至600米。如果有观测到的或模拟的温度数据，这个参数可以用作校准参数。

:ref:`buildings`
----------------

能源消耗表
------------------------
能源消耗(千瓦时/°C)在不同国家和城市之间差异很大。Santamouris等人2015年提供了全球一些城市每摄氏度的能源消耗估算。对于美国，EPA EnergyStar Portfolio Manager数据可以提供分类平均值以及特定建筑的数据:https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/understand-metrics/what-energy注:如果A/C空调普及率较低，则不应使用此估值指标，因为它假定能源成本将随着温度升高(以及A/C空调使用量增加)而增加。美国A/C空调流行率数据可从美国住房调查网站https://www.census.gov/programs-surveys/ahs.html获得

平均相对湿度
-------------------------
热浪期间的平均相对湿度(%)可从当地温度站或全球气候数据中获得

FAQs
====

* 输出分辨率是多少?

    模型输出有两种类型:光栅和向量。栅格具有与LULC输入相同的分辨率(所有其他栅格输入都被重新采样到相同的分辨率)。

* 为什么该模型没有计算健康影响?

　　高温对人体健康的影响在不同城市之间差异巨大，很难开发出一个通用的InVEST模型，准确地捕捉和量化所有城市的这些影响。有关评估城市热缓解对健康影响的更多细节和途径，请参阅模型限制部分关于“城市热对健康影响的估值”的观点。
　　
参考文献
==========

Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56. FAO, Rome, Italy.

American College of Sports Medicine (1984). Prevention of Thermal Injuries During Distance Running. Medicine and Science in Sports & Exercise, 16(5), ix-xiv. https://doi.org/10.1249/00005768-198410000-00017

Bartesaghi, C., Osmond, P., & Peters, A. (2018). Evaluating the cooling effects of green infrastructure : A systematic review of methods, indicators and data sources. Solar Energy, 166(February), 486-508. https://doi.org/10.1016/j.solener.2018.03.008

Campbell, S., Remenyi, T. A., White, C. J., & Johnston, F. H. (2018). Heatwave and health impact research: A global review. Health & Place, 53, 210-218. https://doi.org/https://doi.org/10.1016/j.healthplace.2018.08.017

Deilami, K., Kamruzzaman, M., & Liu, Y. (2018). Urban heat island effect: A systematic review of spatio-temporal factors, data, methods, and mitigation measures. International Journal of Applied Earth Observation and Geoinformation, 67, 30-42. https://doi.org/https://doi.org/10.1016/j.jag.2017.12.009

Gasparrini, A., Guo, Y., Hashizume, M., Lavigne, E., Zanobetti, A., Schwartz, J., Tobias, A., Tong, S., Rocklöv, J., Forsberg, B., Leone, M., De Sario, M., Bell, M. L., Guo, Y. L., Wu, C., Kan, H., Yi, S., Coelho, M. d., Saldiva, P. H., Honda, Y., Kim, H., & Armstrong, B. (2015). Mortality risk attributable to high and low ambient temperature: a multicountry observational study. The lancet, 386(9991), 369-375. https://doi.org/10.1016/S0140-6736(14)62114-0

Kjellstrom, T., Holmer, I., & Lemke, B. (2009). Workplace heat stress, health and productivity - an increasing challenge for low and middle-income countries during climate change. Global Health Action, 2, 10.3402/gha.v2i0.2047. https://doi.org/10.3402/gha.v2i0.2047

Kunapo, J., Fletcher, T. D., Ladson, A. R., Cunningham, L., & Burns, M. J. (2018). A spatially explicit framework for climate adaptation. Urban Water Journal, 15(2), 159-166. https://doi.org/10.1080/1573062X.2018.1424216

Lonsdorf, E.V., Nootenboom, C., Janke, B., & Horgan, B.P. (2021). Assessing urban ecosystem services provided by green infrastructure: Golf courses in the Minneapolis-St. Paul metro area. Landscape and Urban Planning, 208. https://doi.org/10.1016/j.landurbplan.2020.104022

McDonald, R. I., Kroeger, T., Boucher, T., Wang, L., & Salem, R. (2016). Planting Healthy Air: A global analysis of the role of urban trees in addressing particulate matter pollution and extreme heat. CAB International, 128-139.

McMichael, A. J., Campbell-Lendrum, D. H., Corvalán, C. F., Ebi, K. L., Githeko, A. k., Scheraga, J. D., & Woodward, A. (2003). Climate change and human health: risks and responses. World Health Organization. Geneva, Switzerland.

Phelan, P. E., Kaloush, K., Miner, M., Golden, J., Phelan, B., Iii, H. S., & Taylor, R. A. (2015). Urban Heat Island : Mechanisms , Implications , and Possible Remedies. Annual Review of Environment and Resources, 285-309. https://doi.org/10.1146/annurev-environ-102014-021155

Santamouris, M., Cartalis, C., Synnefa, A., & Kolokotsa, D. (2015). On the impact of urban heat island and global warming on the power demand and electricity consumption of buildings - A review. Energy & Buildings, 98, 119-124. https://doi.org/10.1016/j.enbuild.2014.09.052

Shatz, J. & Kucharik, C.J. (2014). Seasonality of the Urban Heat Island Effect in Madison, Wisconsin. Journal of Applied Meterology and Climatology, 53(10), 2371-2386. https://doi.org/10.1175/JAMC-D-14-0107.1

Stewart, I. D., & Oke, T. R. (2012). Local climate zones for urban temperature studies. American Meteorological Society. https://doi.org/10.1175/BAMS-D-11-00019.1

Zardo, L., Geneletti, D., Prez-soba, M., & Eupen, M. Van. (2017). Estimating the cooling capacity of green infrastructures to support urban planning. Ecosystem Services, 26, 225-235. https://doi.org/10.1016/j.ecoser.2017.06.016
