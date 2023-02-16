.. _作物授粉:

***************************************
作物授粉（授粉者丰度）
***************************************

摘要
=======

InVEST 授粉模型侧重于将野生蜜蜂作为关键的动物授粉者。这个模型通过对蜜蜂飞行范围内的巢址和花卉资源可用性的估计，获得在景观的每个单元格上筑巢的蜜蜂丰度指数（即传粉者供应）。然后，该模型利用花卉资源、蜜蜂觅食活动和飞行范围等信息来估计每个单元格的蜜蜂丰度指数。如果需要，该模型会根据蜜蜂丰度和作物对授粉的依赖性，计算出这些野生蜜蜂对农业生产贡献的简单指数。这些结果可以用于了解作物授粉和作物产量随着土地利用和农业管理实践的变化而发生的变化。所需的输入包括土地利用/土地覆盖 (LULC) 地图、土地覆盖类型、存在的传粉者物种类型及其飞行范围。要估计野生传粉者对作物生产的贡献，需要有关农场、种植的作物以及受管理的传粉者丰富程度等信息。该模型的局限性包括没有考虑传粉者随时间的持续性或地块大小的影响。

简介
============

依靠蜜蜂和其他动物的作物授粉在许多农业和自然混合生境景观中是一种具有潜在价值的生态系统服务（Allen-Wardell等人，1998年，Free 1993年）。授粉可以提高番茄、油菜籽、西瓜、咖啡、向日葵、杏仁和可可等多种水果和种子作物的产量、质量和稳定性。事实上，Klein等人（2007年）发现全球115种重要作物中，有87种受益于动物授粉，这项服务在全球范围内每年提供的价值在数十亿到数百亿之间不等。

尽管上文提到大部分作物都需要动物传粉，但要认识到并非所有作物都需要动物授粉。一些作物是风授粉（例如，主粮，如水稻，玉米，小麦）或自花授粉（例如，扁豆和其他豆类），这些作物不需要动物授粉者就可以成功生产水果或种子。Klein等人（2007年）提供了一份作物及其授粉要求清单，这可以帮助确定感兴趣地区的作物是否得益于野生动物的授粉。

决策者可以通过多种方式运用有关作物传粉者、它们在整个景观中的丰度以及它们为作物提供的授粉服务等信息。首先，通过授粉者丰度图和需要它们授粉的作物图，土地利用规划者可以预测不同政策对授粉服务和农民收入的影响（详见Priess等人，2007年）。其次，考虑作物的授粉要求和对传粉者可用性的预测，农民可以使用这些地图智能地定位相关作物。第三，保护组织或土地信托可以使用该工具优化保护投资，使生物多样性和农民受益。最后，政府或其他提出生态系统服务付费计划的人可以利用这些结果来估计谁应该向谁支付费用，以及支付多少费用。

模型
=========

各种各样的动物都可以成为重要的传粉者（例如，鸟类、蝙蝠、飞蛾和苍蝇），但蜜蜂是大多数作物最重要的传粉群体（Free 1993）。因此，InVEST授粉模型侧重于考虑野生蜜蜂的资源需求和飞行行为。许多人在想到传粉者时会想到人工蜂巢中的蜜蜂，但野生蜜蜂也有助于作物授粉。事实上，对于几种重要的作物（例如蓝莓），本地物种比人工管理的蜜蜂效果更好（Cane 1997）。除了生活在野外的野生蜜蜂外，这些本地蜜蜂在不用人工管理蜂巢的情况下就能够为作物提供传粉。这是与栖息地保护相关的授粉服务。

该模型改编自Lonsdorf等人（2009）。为了让蜜蜂在景观区域中持续生存，它们需要两个条件：合适的筑巢地点和蜂巢附近有充足的食物（由鲜花提供）。如果提供了这些资源，传粉者就可以飞到附近的作物上，并在它们收集花蜜和花粉时为作物授粉。该模型将土地覆被转换为蜜蜂的适宜性指数 （0-1），以创建传粉者地图。分数越高，表明蜜蜂的相对丰度越高。为了计算指数，该模型假设蜜蜂需要两种类型的限制资源才能在景观上持续存在——筑巢基质和花卉资源。给定描述景观的土地覆被输入，将根据每个 LULC 类别提供的这些资源的能力分配各种适宜性值。

然后，授粉模型使用巢穴供应指数来估计访问农田的传粉者。它假设附近宗地的供应比远处的宗地贡献更多。我们使用Olsson等人（2015）的见解和宗地的花质来衡量蜜蜂的访问量，以反映蜜蜂已知遵循的中心位置觅食行为。换句话说，距离巢穴同样远的两个宗地的访问率与宗地的花卉品质成正比。

此外，该模型将养殖蜜蜂的潜在用途纳入产量指数。借助有关作物位置及其对传粉者的依赖等信息，该模型使用简单的产量函数来预测农业地区的野生传粉者丰度和养殖蜜蜂对作物产量指数的贡献。养殖蜜蜂的纳入反映了美国农业部资助的综合作物授粉项目 (icpbees.org) 最近工作的指导，以整合人工养殖的蜜蜂和野生蜜蜂的综合效益。

下面正式描述这些步骤。

工作原理
------------

该模型是基于指数的模型，需要以下生物物理数据： 

*LULC 地图;
*与LULC栅格配对的生物物理表，用于将LULC类型映射到不同季节的筑巢适宜性和花卉资源;
*传粉者信息表格，其中包含有关每个物种或野生传粉者群体的活跃季节、筑巢偏好、平均飞行距离和相对丰度的属性;
*农场的矢量文件，表明农场的地理空间位置、作物类型、对传粉者的依赖、养殖的传粉者的丰度以及农场筑巢地点和花卉资源。

因为蜜蜂是熟练的飞行者，它们在筑巢栖息地和觅食地之间来回运动，整个景观区域的多种自然要素都成为它们的活动范围（Ricketts et al. 2006）。它们特定的飞行距离会影响它们的持久性和它们为农场提供的服务水平。因此，该模型需要了解不同传粉物种的特定觅食距离。这些数据可以从定量的田间试验估计（例如，Roubik和Aluja 1983）、代表性指数如个体大小（Greenleaf等人，2007）或专家意见中获得。

授粉者供应和丰度
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

利用这些数据，该模型首先根据研究单元中可用的筑巢地点、周围单元中的花卉资源（即食物）以及该传粉者物种的相对丰度，估计景观中每个单元的传粉者供应。根据该物种的平均觅食范围，筑巢地点附近栅格中的花卉资源比远处栅格更重要。

:math:`PS(x,s)` 是物种`s` 在栅格`x`处的传粉者供应指数，定义为:

.. math:: PS(x,s)=FR(x,s) HN(x,s) sa(s)
	:label: (pol. 1)

其中 :math:`FR(x,s)`是物种`s`在栅格`x`处的可访问花卉资源指数，定义为： 

.. math:: FR(x,s)=\frac{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)\sum_{j\in J}RA(l(x'),j)fa(s,j)}{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 2)

:math:`HN(x,s)` 是物种`s`在栅格`x`处的栖息地筑巢适宜性。

.. math:: HN(x,s)=\max_{n\in N}\left[N(l(x),n) ns(s,n)\right]
	:label: (pol. 3)

其中

* :math:`sa(s)` 是物种`s`在`[0.0, 1.0]`范围内的相对物种丰度指数，:math:`\sum_{s\in S} sa(s) = 1`, and :math:`S` 是所有物种的集合,
* :math:`N(l,n)`是`n`型基质在`l`型土地覆被的筑巢基质指数，范围为`[0.0, 1.0]`,
* :math:`l(x)`是栅格`x`处的土地覆盖类型，
* :math:`j` 是季节,
* :math:`RA(l, j)` 是在季节`j`时土地覆被`l`的花卉资源相对丰度指数，
* :math:`fa(s,j)` 是传粉者物种`s`在季节`j`时的相对觅食活动.
* :math:`D(x,x')` 是栅格`x`和`x'`之间的欧氏距离,
* :math:`ns(s,n)` 是筑巢类型`n`中物种`s`的筑巢首选项 (:math:`N` 是所有筑巢类型的集合),
* :math:`\alpha_s` 是传粉者`s`的预期觅食距离 (Greenleaf et al. 2007).

授粉者供应是授粉者在景观上起源的指标。传粉者丰度表明传粉者在景观中活跃的位置。传粉者的丰度取决于吸引传粉者进入单元的花卉资源，以及可以进入该单元的传粉者的供应。:math:`PA(x,s,j)`是指在季节`j`期间，栅格`x`上的物种`s`的授粉者丰度指数，是给定季节单元上可用花卉资源的乘积，由授粉者在该季节与传粉者供应的相对活动加权，并通过周围单元中的花卉资源指数归一化，例如:

.. math:: PA(x,s,j)=\left(\frac{RA(l(x),j) fa(s,j)}{FR(x,s)}\right)\frac{\sum_{x'\in X}PS(x',s) \exp(-D(x,x')/\alpha_s)}{\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 4)


有关所有变量定义和属性，请参阅变量表附录。

农场丰度和产量
^^^^^^^^^^^^^^^^^^^^^^^^^^^

接下来，使用整个景观中传粉者丰度指数、农场位置以及每个农场的信息（管理授粉者的可用性、作物对授粉的依赖），该模型可以计算获得的总产量指数以及野生授粉者对该产量的贡献。

首先，该模型按季节计算可能受益于授粉服务的农业地区授粉者总丰度指数。农场传粉者丰度为:

.. math:: PAT(x,j)=\sum_{s\in S}PA(x,s,j)
	:label: (pol. 5)

农场授粉者丰度对依赖授粉者的作物产量的潜在贡献是使用可调半sigmoid函数计算的：

.. math:: FP(x)=\frac{PAT(x,j(f(x)))(1-h(f(x)))}{h(f(x))(1-2PAT(x,j(f(x)))+PAT(x,j(f(x))}
	:label: (pol. 6)

其中，:math:`h(f(x))`是农场`f`在栅格`x`处的半饱和常数，表示达到潜在授粉者依赖性总产量的一半所需的野生授粉者丰度。

野生授粉者对依赖授粉者的农田产量的实际贡献取决于管理授粉者已经满足授粉需求的程度。野生授粉者和管理授粉者依赖性的总产量为:

.. math:: PYT(x)=\min(mp(f(x))+FP(x),1)
	:label: (pol. 7)

假设值为0表示实现了0%的授粉者依赖性产量，1.0表示实现了100%的授粉者依赖性产量。请注意，最大/最小表示法将:math:`PYT`的值限制为 0..1，其中:math:`mp(f(x))`是农场多边形`f`内栅格`x`处可用的管理授粉者满足的授粉需求的比例。

依赖野生授粉者的产量比例为

.. math:: PYW(x)=\max(0, PYT(x)-mp(f(x)))
	:label: (pol. 8)

因此，在受管理的授粉者足够丰富的情况下，即：:math:`mp(f(x))=1`，没有额外的产量可归因于野生传粉者。

作物总产量是作物对授粉的依赖程度及其授粉需求得到满足程度的函数。一些作物物种是自相容的或风授粉的，产量对动物传粉者的依赖性较低，而其他作物物种则有义务要求授粉者产生任何产量（Klein等人，2007年）。每个农场的作物总产量计算为

.. math:: YT(f)=1-\nu(f)\left(1-\sum_{x\in X(f)}PYT(x)/|X(f)|\right)
	:label: (pol. 9)

其中，:math:`f` 是一个特定的农场，:math:`X(f)` 是覆盖农场`f`的栅格集，:math:`|X(f)|`是农场`f`覆盖的栅格计数。函数:math:`\nu(f)` 是一个标量，:math:`\in [0,1]` 表示农场`f`种植的作物产量比例取决于传粉者。

野生授粉者占作物总产量的比例为

.. math:: YW(f)=\nu(f)\left(\sum_{x\in X(f)}PYW(x)/|X(f)|\right)
	:label: (pol. 10)

局限和简化
-------------------------------

该模型是一个基于指数的模型，仅估计授粉者丰度和授粉者对作物产量的贡献的相对模式。这是因为巢密度、资源可用性和传粉者丰度的绝对估计值很难获取，并且许多作物的产量函数（包括传粉者丰度）定义不明确。依赖相对指数限制了我们估计绝对经济价值的能力，以更好地为土地使用规划决策提供信息，这些通常根据成本效益分析。

在模型的传粉者丰度指数中使用中心位置觅食尚未进行实证测试，因此我们警告不要在没有经验验证的情况下使用该模型进行经济预测。在产量函数中集成管理蜜蜂也同样如此。

作为一个基于指数的模型，它非常适合在代表LULC、农场管理实践或作物类型边际变化的情景之间进行定性比较。农场授粉者丰度:math:`PAF(x,j)`将受到正在建模的传粉者种类数量的影响，因此即使在相同的景观上也不能用于比较不同的传粉者群落。同样，由于相对物种丰度指数:math:`sa(s)`被指定为输入，因此对于稀有物种因筑巢栖息地或花卉资源可用性发生较大变化而变得常见或反之亦然的情况，该模型将无法产生准确的结果。

该模型不包括蜜蜂种群随时间变化的动态，因此无法评估这些种群是否适合目前的景观区域。相反，该模型只是简单地提供了景观区域每个栅格单元中静态瞬时的传粉者数量，从而给出对筑巢地点和食物资源的简单估计。一些影响蜜蜂种群的因素，如栖息地干扰和典型的种群数量波动，没有考虑在内。此外，该模型根据可用花卉资源的平均值计算传粉者的供应量，这些资源在传粉者活跃的各个季节按传粉者活动加权。这没有考虑季节的顺序或一个季节中传粉者的丰度对前一个季节可用资源的依赖性。该模型也没有考虑不同传粉者物种在为不同作物类型授粉时的有效性的变化，而是假设所有物种根据其相对丰度和为每个农场/作物指定的半饱和常数做出同等贡献。

该模型在估计丰度时没有考虑栖息地斑块的大小。对于许多物种来说，有最小斑块面积的限制，小于该面积的斑块不能支持该种类长期生存。实践证明，小斑块支撑较少的蜜蜂种类（Kremen et al. 2004），但是蜜蜂也可以在相当小但条件适宜的生境中生存（Ricketts 2004）。

授粉者可能会受到景观中小尺度特征的影响，这些特征很难在典型分辨率为30米的土地覆盖数据中捕获。例如，在另一个不同生境中的小块花卉资源可以给蜜蜂提供重要的食物资源，但利用标准土地覆被图并不能识别出来。一些蜜蜂也可以在面积很小但是条件合适的区域筑巢（一个合适的路边或树洞）。因此，使用每个LULC类的筑巢地点或花卉可用性的平均值以及30m或更大的栅格的土地覆被类型，将无法捕获这些精细但重要的资源区域。

数据需求
==========

.. 注:: *所有空间输入必须具有完全相同的投影坐标系* (线性米单位), *不是* 地理坐标系（以度为单位）.

- :investspec:`pollination workspace_dir`

- :investspec:`pollination results_suffix`

- :investspec:`pollination landcover_raster_path` 用于将有关土地覆被类型的栖息地和花卉资源的生物物理属性映射到空间布局。这必须具有足够精细的分辨率，以捕捉蜜蜂在景观上的运动信息。如果蜜蜂平均飞行 800 米，而栅格直径为 1000 米，则模型将无法完全捕获蜜蜂从筑巢地点到邻近农场的运动信息。

- :investspec:`pollination landcover_biophysical_table_path` 数据可以从实地调查中汇总，如果没有实地数据，则通过专家评估获得。

	列:

	- :investspec:`pollination landcover_biophysical_table_path.columns.lucode`

	- :investspec:`pollination landcover_biophysical_table_path.columns.nesting_[SUBSTRATE]_availability_index`

	- :investspec:`pollination landcover_biophysical_table_path.columns.floral_resources_[SEASON]_index` 例如，LULC 类包含 100% 的大规模开花作物，该作物在整个季节开花，丰度覆盖率为 80%，适宜性值为 0.80。在80%的花朵覆盖率下只开花一半的LULC类将被赋予0.40的花卉适宜性值。*SEASON*名称必须与属性表中给出的季节完全匹配。


    **生物物理表示例:**

    .. csv-table::
       :file: ../invest-sample-data/pollination/landcover_biophysical_table_modified.csv
       :header-rows: 1
       :widths: auto

- :investspec:`pollination guild_table_path` 'Guild'是指一组表现出相同筑巢行为的蜜蜂物种，无论是喜欢在地面、树洞还是其他栖息地特征中筑巢。如果已知多个物种是重要的传粉者，并且它们在飞行季节、筑巢要求或飞行距离方面有所不同，那么请分别提供每个物种的数据。如果可用数据很少或没有可用数据，则创建一个单一的“原始授粉者”，其数据取自整个授粉者群落的平均值或专家意见。每一行都是一个独特的传粉者物种或功能团，列的命名和定义必须如下:

	列:

	- :investspec:`pollination guild_table_path.columns.species`
	- :investspec:`pollination guild_table_path.columns.nesting_suitability_[SUBSTRATE]_index` 筑巢类型是用户定义的，可能包括地面巢穴、树洞等。
	- :investspec:`pollination guild_table_path.columns.foraging_activity_[SEASON]_index` 季节由用户定义，但可能包括春季、夏季、秋季；雨季、旱季等等.
	- :investspec:`pollination guild_table_path.columns.alpha` 该模型使用此估计距离来定义给定栅格单元周围可用花卉的邻域，并加权农场花卉资源和传粉者丰度的总和。该值可以通过基于异速生长关系的蜜蜂物种的典型觅食距离来确定（见Greenleaf等人，2007年）。
	- :investspec:`pollination guild_table_path.columns.relative_abundance` 将每个物种的此值设置为相同的值将导致每个物种的权重相等。

   *示例:* 假设研究一个功能团表有两个物种。有两种主要的筑巢类型，“洞穴”和“地面”。物种A同时有洞穴和地面筑巢类型，物种B仅有洞穴筑巢。这里全年有两个开花季节，“春天”和“夏天”。典型的飞行距离以米为单位，因物种而异。B的相对丰度高于A，表明B传粉者比A多。

   **功能团表示例:**

   .. csv-table::
      :file: ../invest-sample-data/pollination/guild_table.csv
      :header-rows: 1
      :widths: auto

- :investspec:`pollination farm_vector_path`

    .. 注::
       可选的农场矢量将覆盖与 LULC 栅格重叠的任何区域中的季节性花卉资源值和筑巢适宜性值。

    区域:

    - :investspec:`pollination farm_vector_path.fields.crop_type` 对于种植多个重叠作物或多个季节作物的农场，必须为每个作物包含单独的重叠面。
    - :investspec:`pollination farm_vector_path.fields.half_sat` 这是一个可调参数，在模型的初始运行和结果检查后进行调整可能最有用。这是等式:eq:`(pol. 6)` 中的:math:`h`.
    - :investspec:`pollination farm_vector_path.fields.season`
    - :investspec:`pollination farm_vector_path.fields.fr_[SEASON]`
    - :investspec:`pollination farm_vector_path.fields.n_[SUBSTRATE]`
    - :investspec:`pollination farm_vector_path.fields.p_dep` 见Klein等人（2007年）对普通作物的估计数。
    - :investspec:`pollination farm_vector_path.fields.p_managed` 这可以估计为推荐的蜂巢密度或放养率的比例。参见Delaplane & Mayer （2000），了解美国的建议库存率。农业推广办公室也是这一信息的良好来源。

.. _解释结果:

结果解释
====================

最终结果
-------------

* ** Parameter log**:参数日志。每次运行模型时，都会在工作区中创建一个文本（.txt）文件。该文件将列出该运行的参数值和输出消息，并根据服务、日期和时间命名。当联系NatCap关于模型运行中的错误时，请包括参数日志。

* **farm_results_[Suffix].shp**: (仅在提供农场矢量时生成) 具有以下附加字段的输入农场多边形矢量文件的副本:

  * *p_abund*: 活跃季节时农场的平均授粉者丰度。
  * *y_tot*: 总产量指数，包括野生和受管理授粉者的联合产量以及授粉者独立产量。
  * *pdep_y_w*: 野生授粉者潜在授粉依赖性产量指数。
  * *y_wild*: 野生授粉者总产量指数。
  
* **farm_pollinators_[Suffix].tif**: (仅在提供农场矢量时生成) 每个季节所有物种的每栅格传粉者总丰度，裁剪到农场矢量多边形的几何形状。

* **pollinator_abundance_[SPECIES]_[SEASON]_[Suffix].tif**: 季节中每栅格的传粉者物种丰度。.

* **pollinator_supply_[SPECIES]_[Suffix].tif**: 授粉者物种的每栅格指数，考虑到表中的任意丰度因子，可以在一个栅格上，乘以该栅格上该物种的栖息地适宜性，乘以传粉者可以从该栅格飞到的可用花卉资源。（公式1）

* **total_pollinator_abundance_[SEASON]_[Suffix].tif**: (仅在提供农场矢量时生成) 每个季节所有物种的每栅格总传粉者丰度。

* **total_pollinator_yield_[Suffix].tif**: (仅在提供农场矢量时生成) 与农场重叠的栅格的每栅格总传粉者产量指数，包括野生传粉者和管理传粉者。

* **wild_pollinator_yield_[Suffix].tif**: (仅在提供农场矢量时生成)与农场重叠的栅格的每栅格传粉者产量指数，仅适用于野生传粉者。

中间结果
^^^^^^^^^^^^^^^^^^^^

您可能还需要检查中间结果。这些文件可以帮助明确最终结果中分布模式的原因，还可用于更好地了解模型和进行故障排除。它们位于为模型运行定义的 Workspace 目录中的 *intermediate_outputs* 文件夹中，并且其中大多数具有文件名，可以很好地了解图层所代表的内容。

附录：变量表
============================

* :math:`x` - 栅格坐标。
* :math:`X` - 土地覆被地图中所有栅格的集合。
* :math:`f(x)` - 栅格x上的农场。
* :math:`F` - 位于农场中的所有栅格的集合。
* :math:`s` - 蜜蜂种类。
* :math:`n` - 筑巢类型(地面，洞穴)。
* :math:`N` - 所有筑巢类型的集合。
* :math:`j` - 季节（秋季、春季等）。
* :math:`J` - 所有季节的集合（例如：{秋季，春季}）。
* :math:`fj(f, x)` - f农场在栅格x处的的活跃授粉季节。
* :math:`\alpha_s` - 物种s的平均觅食距离。
* :math:`ns(s,n)` - 筑巢类型n中物种s的筑巢适宜性偏好。
* :math:`HN(x,s)` - 物种s在栅格x处的栖息地筑巢适宜性 [0.0，1.0]。
* :math:`N(l,n)` - 土地覆被类型l对于基质类型n的筑巢基质指数，范围为`[0.0, 1.0]`。
* :math:`RA(l,j)` - 季节j期间土地覆盖类型l上花卉资源相对丰度指数。范围是`[0.0, 1.0]`。
* :math:`fa(s,j)` - 季节j期间物种s的相对觅食活动。
* :math:`FR(x,s)` - 物种s在栅格x处的可访问花卉资源指数。
* :math:`D(x,x')` - 栅格x和x’的质心之间的欧氏距离。
* :math:`PS(x,s)` - 物种s在栅格x处的授粉者供应指数。
* :math:`PA(x,s,j)` - 物种s的栅格x处的传粉者丰度。
* :math:`PAT(x,j)` - 季节j时栅格x处所有物种的农场授粉者总丰度。
* :math:`FP(x)` - 在农场需要授粉的季节，农场传粉者丰度对农场栅格中依赖授粉者的作物产量的潜在贡献。
* :math:`mp(f)` - 相对于建议放养率的农场f上受管理的授粉者丰度.
* :math:`h(f)` - 农场f的半饱和系数.
* :math:`PYT(x)` - 季节j时栅格x处的野生和受管理的传粉者产量，占传粉者贡献总产量。
* :math:`PYW(x)` - 季节j时栅格x的野生传粉者可归因产量。
* :math:`sa(s)` - 物种s的相对物种多度指数.
* :math:`YT(f)` - 考虑到作物对传粉者依赖性的“f”地块的平均农场产量.
* :math:`YW(f)` - 可归因于野生传粉者的农场“f”地块平均农场产量的比例，占作物对传粉者依赖的比例.
* :math:`\nu(f)` - 作物产量占授粉的比例.

附录：数据源
======================

.. 注意：示例数据仅用于说明数据结构，不应用作数据源。

作物对传粉者的依赖
------------------------------
参见Klein等人，2007年。列出了全球重要作物及其对动物传粉者的依赖。

筑巢适宜性和花卉资源可用性
----------------------------------------------------
Koh et al. 2016 包含 45 个土地利用类别的筑巢适宜性和花卉资源可用性数据。

:参考:` 土地利用/土地覆盖 <lulc>`
---------------------------------

参考文献
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
