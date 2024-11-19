.. _ufrm:

****************
城市洪水风险缓解
****************

引言
============

洪水灾害来自不同的来源，包括:河边(或河流)洪水、沿海洪水和暴雨(或城市)洪水——这是InVEST模型的重点。自然基础设施对每一种洪水灾害都有影响。与暴雨洪水有关，自然基础设施的作用主要是通过减少径流产生、减缓地表流动和创造蓄水的空间(在积洪平原或盆地)。

InVEST模型计算径流减少量，即每个像素保留的径流量与暴雨量的比较。对于每个流域，它还通过叠加潜在的洪水范围、和已建成基础设施来计算潜在的经济损失。

模型
=========

工作原理
^^^^^^^^^^^^

产流和径流衰减系数
----------------------------------------------

对于每个栅格单元：math:`i`，根据土地使用类型和土壤特征，我们使用曲线编号法估算了径流：math:`Q` (mm)


.. math:: Q_{p,i} = \begin{Bmatrix}
        \frac{(P - \lambda S_{max_i})^2}{P + (1-\lambda) S_{max,i}} & if & P > \lambda \cdot S_{max,i} \\
        0 & & otherwise
        \end{Bmatrix}
    :label: runoff

式中：math:`P` 表示暴雨设计深度（单位：mm）
:math:`S_{max,i}`表示潜在保水率（单位：mm）
:math:`\lambda \cdot S_{max}`表示启动径流的降雨深度，也称为初始损失(简化式:math:`\lambda=0.2`).

:math:`S_{max}` 表示曲线编号的函数（单位：mm）
:math:`CN` 表示一个取决于土地利用和土壤特性的经验参数


.. math:: S_{max,i}=\frac{25400}{CN_i}-254
   :label:

然后，模型计算每栅格单元的径流保留率:math:`R_i` 为:

.. math:: R_i=1-\frac{Q_{p,i}}{P}
   :label: runoff_retention
　　

以及每栅格单元的径流保留量 :math:`R\_m3_i` as:

.. math:: R\_m3_i=R_i\cdot P\cdot pixel.area\cdot 10^{-3}
   :label: runoff_retention_volume

With :math:`pixel.area` in :math:`m^2`.

Runoff volume (also referred to as "flood volume") per 
径流量（也代指“洪水量”）每栅格单元 :math:`Q\_m3_i` 也可被计算为

.. math:: Q\_m3_i=Q_{p,i}\cdot pixel.area\cdot 10^{-3}
   :label: flood_volume

计算潜在的服务（可选）
--------------------------------------

首先，:math:`\text{Affected.build}` 建筑基础设施的潜在损失总和，以美元计，

.. math:: \text{Affected.build}_W = \sum_{b ∈ B}a(b,W)·d(b)
   :label: affected build

式中

* :math:`b`是所有已建成基础设施集合中的建筑足迹:math:`B`
* :math:`a(b,W)`:是 :math:`m^2` 中建筑物占地面积，:math:`b` 与:math:`W` 流域相交
* :math:`d(b)` 是:math:`currency/m^2`（来自伤害损失表）中建筑:math:`b` 类型的伤害值

然后计算:math:`\text{Service.built}`是每个流域已建成基础设施避免破坏的指标:math:`W`:

.. math:: \text{Service.built}_W=\text{Affected.build}_W·\sum_{i ∈ W}R\_m3_i
   :label: service.built

式中

* :math:`i` 是流域:math:`W` 中的一个栅格单元
* :math:`R\_m3_i` 是栅格单元:math:`i` 上的径流保持体积

:math:`\text{Service.built}` 表示为:math:`currency·m^3`。它只应被视为一项指标，而不是实际的储蓄指标。

局限性和简化
============

**径流产量:** 该模型使用了一个简单的方法(scs -曲线编号)，引入了很高的不确定性。然而，这种方法通常可以很好地捕捉不同土地利用之间的排序，即自然基础设施的影响将在模型输出中定性地表示。未来的工作将旨在包括景观路径:观点包括TOPMODEL(有一个R包)，UFORE(在iTree中使用)，CADDIES等

**评估方法:** 目前采用了一种简单的洪水风险保留价值评估方法，将洪水风险评估为已建基础设施所避免的破坏。可以实施其他方法(例如，与死亡率、发病率或经济混乱有关的方法)。另一个服务指标是受影响人口，即面临洪水风险的人数。这可以只针对弱势群体，例如与年龄、语言等有关的群体。参见Arkema等人，2017年，对社会脆弱性指标的综述。这一指标可以通过把十字路口的人口加起来来计算

数据需求
========

.. note:: 城市防洪的空间层可能有不同的坐标系，但*它们必须都是投影坐标系*，而不是地理坐标系。

.. note:: 栅格输入可能有不同的单元大小，它们将被重新采样以匹配土地利用/土地覆盖栅格的单元大小。因此，栅格模型结果将具有与土地利用/土地覆盖栅格相同的单元大小。

- :investspec:`urban_flood_risk_mitigation workspace_dir`

- :investspec:`urban_flood_risk_mitigation results_suffix`

- :investspec:`urban_flood_risk_mitigation aoi_watersheds_path` 这些路径可能是流域或污水渠边界。

- :investspec:`urban_flood_risk_mitigation soils_hydrological_group_raster_path`

- :investspec:`urban_flood_risk_mitigation lulc_path` 所有输出都将根据该栅格的分辨率产生。

- :investspec:`urban_flood_risk_mitigation soils_hydrological_group_raster_path`


- :investspec:` 城市洪水风险缓解曲线编号表路径` 表中包含与土地覆盖图中每个土地用途类别对应的模型信息。土地覆盖光栅中的所有LULC类必须在该表中有相应的值。每一行是一个土地利用/土地覆盖类别，列的命名和定义必须如下:

Columns:

  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.lucode`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_a`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_b`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_c`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_d`

- :investspec:`urban_flood_risk_mitigation built_infrastructure_vector_path`

  Field:

  - :investspec:`urban_flood_risk_mitigation built_infrastructure_vector_path.fields.type`

- :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path`

  Columns:

  - :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path.columns.type`
  - :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path.columns.damage` 任何货币都可以使用

结果解释
========

 * **Parameter log**:每当模型运行时，将在工作区中创建一个文本(.txt)文件。该文件将列出该运行的参数值和输出消息，并将根据服务、日期和时间命名。当遇到NatCap关于模型运行中的错误时，请包括参数日志。

 * **Runoff_retention.tif**:带有径流保留值的栅格 (无单位，相对于降水量). 计算公式:eq:`runoff_retention`.

 * **Runoff_retention_m3.tif**:带有径流保留值的栅格(in :math:`m^3`). 计算公式:eq:`runoff_retention_volume`.

 * **Q_mm.tif**:带有径流值的栅格(毫米)。由公式计算:eq:`runoff`.

 * **flood_risk_service.shp**: Shapefile属性表中的结果。

    * **rnf_rt_idx**:每个流域的径流保留值的平均值 (:math:`R_i`)。

    * **rnf_rt_m3**:每个流域的径流留水量总和 (:math:`R\_m3_i`), in :math:`m^3`。

    * **flood_vol**:每个流域的洪水量(``Q_m3``, equation :eq:`flood_volume`)。

    * **aff_bld**:对已建基础设施的潜在损害，以货币单位计算，按流域计算。仅在提供已建基础设施向量输入时计算。

    * **serv_blt**: :math:`Service.built`为这个流域构建的值(see equation :eq:`service.built`)。流域径流截留服务指标。仅在提供已建基础设施向量输入时计算。

附录:数据来源和参数选择指南
===========================================================

:ref:`土地利用土地覆盖 <lulc>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`流域 <watersheds>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设计暴雨的降雨深度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

设计暴雨是一种用于建模目的的假想暴雨。设计暴雨降水值应根据区域和目标进行选择。例如，它可以是每次降雨事件的平均降水量，某个百分位数的降水量，或100年预计出现一次的最大降水量。

为了计算设计暴雨，用户可以查询他们所在城市的强度-频率-持续时间(IFD)表。暴雨持续时间等于所研究流域的平均集中时间。集中注意力的时间可以从现有的研究或网络工具中得出。https://www.lmnoeng.com/Hydrology/TimeConc.php。参见Balbi等人(2017)对这些方法的详细描述。

:ref:`土壤分组 <soil_groups>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`曲线编号 <cn>`
^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`建筑设施 <buildings>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

每种建筑类型的潜在损害损失
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
在美国，HAZUS提供损害数据。在全球范围内，欧盟委员会最近的一份报告提供了有用的数据：https://publications.jrc.ec.europa.eu/repository/bitstream/JRC105688/global_flood_depth-damage_functions__10042017.pdf


参考文献
==========

Arkema, K. K., Griffin, R., Maldonado, S., Silver, J., Suckale, J., & Guerry, A. D. (2017). 结合社会、生态和自然科学，推进对沿海社区的自然和基于自然的保护。https://doi.org/10.1111/nyas.13322

Balbi, M., Lallemant, D., & Hamel, P. (2017). 生态系统服务评估的洪水风险框架:概念验证。

NRCS-USDA。(2004)。第十章。暴雨直接径流的估算。在美国农业部(编)，第630部分水文。国家工程手册。检索自http://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063

NRCS-USDA Part 630水文国家工程手册，第7章水文土壤组。2007

NRCS-USDA Part 630水文国家工程手册，第9章水文土壤复盖体，2004。
 
Sahl，J.(2015)。生态系统服务的经济评估方法:文献综述，以支持城市雨水管理服务评估建模框架的发展。
