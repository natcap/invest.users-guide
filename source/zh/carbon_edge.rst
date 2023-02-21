森林碳边缘效应
==============

摘要
----

InVEST碳边际效应模型扩展了InVEST碳模型的方法，以解释由于森林边缘的产生而导致的森林碳储量的退化。它应用已知的碳储存与森林边际距离之间的关系来计算碳储存的边缘效应，并将这些估计值与碳库存数据结合起来，构建总体碳地图。边缘效应的模型只涉及地上碳，因为其他碳库（地下、土壤和死物质）的边缘效应还没有记录。对于所有其他碳库，以及非热带森林类型，或者如果模型运行时没有边缘效应，则遵循IPCC（2006）的清单方法，按土地覆盖等级分配碳储存值。

引言
----

未来土地利用变化对碳储存或封存的影响可以通过将文献中发现的不同生境类型的碳储存估计值应用于景观中发现的每个生境来模拟（例如，Nelson等人，2010）。然而，这种方法假设所有生境的碳储存质量都是相同的，不管它发生在哪里。尽管有大量证据表明，破碎化在改变热带森林的碳储存和固存率方面起着巨大的作用（Broadbent等人，2008；Dantas等人，2011；Laurance等人，1997、2000、2001、2002）。例如，在巴西大西洋森林中，核心林区的碳储存量是边缘林的三倍以上（Dantas等人，2011）。Chaplin-Kramer等人（2015年）利用生物量（Baccini等人2012年）和相关土地覆盖（Friedl等人2011年）的遥感数据调查了整个泛热带地区的这种模式，发现碳储存向森林边缘逐渐退化的连续关系，这在不同地区有很大差异。该模型考虑了热带森林中这些有据可查的边缘效应，根据一个像素与最近的森林边缘的距离来分配碳储存。相对于森林清查方法，这可以将碳储量估计值的总体准确性提高20%，并且更好地捕捉到森林破碎化的影响，而不仅仅是生境损失的面积。

模型
----

InVEST碳边缘效应模型是对InVEST碳模型的更新，它包含了由于热带森林的边缘效应而发生的碳储存的退化。用户指定哪些土地覆盖类别是森林，然后模型使用预先生成的回归结果，根据其与最近的森林边缘的距离预测整个森林地块的碳。这些结果与InVEST碳模型中使用的传统清查方法（IPCC 2006）分配给非森林类别的碳相结合，生成所有土地覆被类别的地上碳储存图层。InVEST碳边缘效应模型的运行可以只计算地上碳或所有碳库，并且可以在有或没有边缘效应的情况下运行。需要注意的是，边缘效应回归只与地上碳储量有关，因为只检测到地上生物量的边缘效应。为了包括其他三个碳库（地面以下、土壤和立地死物质），应在生物物理表中将每个土地覆盖类别的碳密度（Mg/ha）包括在内。

还要注意的是，回归数据并没有覆盖全球。将回归模型层forest_carbon_edge_regression_model_parameters.shp（可在该模型的样本数据中找到）带入GIS并与你的研究区域进行核对，以确保它覆盖你所关注的区域可能是有用的。如果回归数据没有覆盖你的研究区域，你就不能使用该模型来计算边缘效应。


工作原理
~~~~~~~~

该模型遵循Chaplin-Kramer等人（2015）描述的方法，在整个泛热带地区100公里×100公里的网格单元中，构建了森林生物量密度（Mg/ha）与森林边缘距离（km）之间的一系列回归模型。在大多数像素来自森林生物群落的网格单元中，考虑用三个候选回归模型来表示生物量密度与森林边缘距离之间的关系：

1. Asymptotic: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} - \theta_{2} \cdot \mathrm{\exp}( - \theta_{3} \cdot \mathrm{\text{Distance}})`

2. Logarithmic: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot ln(\mathrm{\text{Distance}})`

3. Linear: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot \mathrm{\text{Distance}}`

然后，对于每个网格单元，使用具有最高r\ :sup:`2` 值的候选者，以最好地代表密度与森林边缘距离之间的关系。在那些没有观察到更高距离的单元中，模型（2）和（3）被认为是合适的（和更简单的）替代方案，作为结果，森林核心区没有牢固地建立起来。在绝大多数的网格单元中，模型（1）是最佳的。

这些回归的结果可以在为InVEST碳边缘效应模型提供的样本数据集中的碳边缘回归参数shapefile（*core_data/forest_carbon_edge_regression_model_parameters.shp*）中找到。

对于研究区域内的任何森林像素，该模型计算该像素与森林边缘的距离，然后将生物量计算到预定数量的最近回归模型，再通过距离线性插值方案汇总为一个结果。然后，该模型用用户提供的转换系数将生物量转换为碳，默认系数为0.47（IPCC 2006）。用户可以指定插值方案中使用的局部模型的数量，默认为10个，但范围可以从1（只有最近的点）到2635（地球上的每个回归模型）。请注意，选择1可能会导致从一个像素到下一个像素时，在不同的回归网格单元中出现人为的巨大碳差异。选择的回归网格单元的数量越多，从一个像素到下一个像素的过渡就越平滑。用户可能希望选择覆盖整个研究区域的网格单元的数量，以消除模型选择的任何伪影。这可以通过检查*intermediate_outputs/local_carbon_shape.shp*几何图形覆盖在感兴趣的区域上来确定。生物量b在像素p上的线性内插方案如下：

.. math:: b_{p} = \frac{\sum_{i \in n}\frac{1}{d_{i}}{b_{i}^{'}}_{}}{\sum\frac{1}{d_{i}}}

式中：

-  :math:`b_{p}`\是像素p上的内插生物量
- n是要插值的最近模型的数量，由用户提供。
- i是离像素p最近的i\ :sup:`th` 生物量模型。
- d\ :sub:`i`是像素p到i\ :sup:`th` 生物量模型中心点的距离。

非森林类的碳计算遵循InVEST碳模型的方法，根据生物物理表中指定的森林碳库存数据进行赋值。按照这种清查方法和边缘效应方法绘制的碳图层被合并到最终的碳图层中，这样，森林土地覆盖物就会表现出边缘效应，而所有其他土地覆盖物则不会。

数据需求
--------
请注意，所有的空间输入必须在同一个投影坐标系中，并以线性米为单位。

- :investspec:`forest_carbon_edge_effect workspace_dir`

- :investspec:`forest_carbon_edge_effect results_suffix`

- :investspec:`forest_carbon_edge_effect lulc_raster_path`

- :investspec:`forest_carbon_edge_effect biophysical_table_path`

   Columns:

   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.lucode`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.is_tropical_forest`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_above`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_below`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_soil`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_dead`

   **生物物理表示例（巴西的数据）**

   .. csv-table::
          :file: ./carbon_edge/forest_edge_carbon_lu_table.csv
          :header-rows: 1
          :widths: auto

   *地上碳数据的来源*

   Closed shrublands, open shrublands, grasslands: Miranda, Sabrina do Couto, et al. Regional variations in biomass distribution in Brazilian savanna woodland. Biotropica 46.2 (2014): 125-138.

   Woody savannas, savanna: Saatchi, Susan S., et al. Distribution of aboveground live biomass in the Amazon basin. Global Change Biology 13.4 (2007): 816-837.

   Croplands: Fearnside, Philip M. Greenhouse gases from deforestation in Brazilian Amazonia: net committed emissions. Climatic Change 35.3 (1997): 321-360.

- :investspec:`forest_carbon_edge_effect pools_to_calculate`

- :investspec:`forest_carbon_edge_effect compute_forest_edge_effects` 如果选择该方法，模型将使用Chaplin-Kramer等人的方法来计算热带森林类型的地面碳储量，该方法在生物物理表中的 "is_tropical_forest "字段中以 "1 "表示。

- :investspec:`forest_carbon_edge_effect tropical_forest_edge_carbon_model_vector_path` 这个输入是在样本数据中提供的，不需要改变，除非你对你的研究区域进行了单独的回归模拟，并且有更好或更新的信息。所提供的shapefile来自对森林生物量与森林边缘距离关系的泛热带分析（Chaplin-Kramer等人，2015）。

   请注意，回归数据并没有覆盖全球。将回归模型层*forest_carbon_edge_regression_model_parameters.shp*（可在该模型的样本数据中找到）带入 GIS，并与你的研究区域进行核对，以确保其覆盖你所关注的区域可能是有用的。如果回归数据没有覆盖你的研究区域，你就不能使用该模型来计算边缘效应。

- :investspec:`forest_carbon_edge_effect n_nearest_model_points` 默认值为10。更高的值可以在更大程度上平滑不同网格单元中检测到的边缘效应的变化（可在碳边缘回归参数shapefile中看到）。

- :investspec:`forest_carbon_edge_effect biomass_to_carbon_conversion_factor` 默认值为0.47（参考IPCC 2006）。这只涉及到边缘效应的回归参数；生物物理表中的所有数值都应该是以碳为单位，而不是以生物量为单位。

- :investspec:`forest_carbon_edge_effect aoi_vector_path`。请注意，回归数据并没有覆盖全球。将回归模型层*forest_carbon_edge_regression_model_parameters.shp*（可在该模型的样本数据中找到）带入 GIS，并与你的研究区域进行核对，以确保其覆盖你所关注的区域可能是有用的。如果回归数据没有覆盖你的研究区域，你就不能使用该模型来计算边缘效应。

解读结果
--------

最终结果
~~~~~~~~

- **参数日志**。每次模型运行时，一个文本（.txt）文件将出现在\ *Workspace*。该文件将列出该次运行的参数值，并将根据服务、日期和时间来命名。当与NatCap联系有关模型运行中的错误时，请附上参数日志。

-  **carbon_map_[Suffix].tif**.每个像素的碳储量地图，其中森林中的数量是根据与森林边缘的距离回归得出的，而非森林类的数量是根据生物物理表得出的。请注意，由于该地图显示的是每个像素的碳（Mg），较粗的分辨率地图的碳值应该更高，因为像素面积更大。

-  **aggregated_carbon_stocks_[Suffix].shp**:如果用户提供了感兴趣的服务区域，该输出shapefile总结了定义的区域多边形中的总碳（column *c_sum*）和每公顷平均碳（column *c_ha_mean*）。数值的单位是Mg。

中间结果
~~~~~~~~
-  intermediate_outputs\\\ **c_above_carbon_stocks_[Suffix].tif**.
      储存在地上生物量碳库中的碳。

-  intermediate_outputs\\\ **c_below_carbon_stocks_[Suffix].tif**.
      储存在地下生物量碳库中的碳。

-  intermediate_outputs\\\ **c_dead_carbon_stocks_[Suffix].tif**. 储存在死亡物质生物量碳库中的碳。

-  intermediate_outputs\\\ **c_soil_carbon_stocks_[Suffix].tif**. 储存在土壤生物量碳库中的碳。

-  intermediate_outputs\\\ **local_carbon_shape.shp**. 重新预测的与研究区域相匹配的回归参数。

-  intermediate_outputs\\\ **edge_distance_[Suffix].tif**. 每个森林像素到最近的森林边缘的距离。

-  intermediate_outputs\\\ **tropical_forest_edge_carbon_stocks_[Suffix].tif**.
      根据回归法，仅有森林区域的碳地图。

附录：数据来源
--------------

:ref:`土地利用/土地覆盖 <lulc>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`碳库 <carbon_pools>`
~~~~~~~~~~~~~~~~~~~~~~~~~~

参考文献
--------

Baccini, A., S. J. Goetz, W. S. Walker, N. T. Laporte, M. Sun, D.
Sulla-Menashe, J. Hackler, P. S. A. Beck, R. Dubayah, M. A. Friedl, S.
Samanta, and R. A. Houghton. 2012. Estimated carbon dioxide emissions
from tropical deforestation improved by carbon-density maps. Nature
Climate Change 2:182–185.

Chaplin-Kramer, R., I. Ramler, R. Sharp, N. M. Haddad, J. S. Gerber, P.
C. West, L. Mandle, P. Engstrom, A. Baccini, S. Sim, C. Mueller, and H.
King. (2015). Degradation in carbon stocks near tropical forest edges.
Nature Communications.

Dantas de Paula, M., Alves-Costa, C., Tabarelli, M., 2011. Carbon
storage in a fragmented landscape of Atlantic forest: the role played by
edge-affected habitats and emergent trees. Tropical Conservation Science
4, 349–358.

Friedl, M. A., D. Sulla-Menashe, B. Tan, A. Schneider, N. Ramankutty, A.
Sibley, and X. Huang. 2010. MODIS Collection 5 global land cover:
Algorithm refinements and characterization of new datasets. Remote
Sensing of Environment 114:168–182.

Intergovernmental Panel on Climate Change (IPCC). 2006. IPCC Guidelines
for National Greenhouse Gas Inventories. Volume 4: Agriculture, Forestry
and Other Land Use.

Laurance, W. F., 1997. Biomass Collapse in Amazonian Forest Fragments.
Science 278, 1117–1118.

Laurance, W.F., 2000. Do edge effects occur over large spatial scales?
Trends in ecology & evolution 15, 134–135.

Laurance, William F., Williamson, G.B., 2001. Positive Feedbacks among
Forest Fragmentation, Drought, and Climate Change in the Amazon.
Conservation Biology 15, 1529–1535.

Laurance, W., Lovejoy, T., Vasconcelos, H., Bruna, E., Didham, R.,
Stouffer, P., Gascon, C., Bierregaard, R., Laurance, S., Sampaio, E.,
2002. Ecosystem decay of Amazonian forest fragments: a 22-year
investigation. Conservation Biology 16, 605–618.

Nelson, E., et al. 2010. Projecting global land-use change and its
effect on ecosystem service provision and biodiversity with simple
models. PLOS One 5: e14327
