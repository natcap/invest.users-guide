森林碳边缘效应
==============

摘要
----

The InVEST carbon edge effect model extends the approach of the InVEST
carbon model to account for forest carbon stock degradation due to the
creation of forest edges. It applies known relationships between carbon
storage and distance from forest edge to calculate edge effects in
carbon storage, and combines these estimates with carbon inventory data
to construct the overall carbon map. The model for edge effects pertains
to above-ground carbon only, because edge effects have not been
documented for the other carbon pools (below-ground, soil and dead
matter). For all other carbon pools, and for non-tropical forest
classes, or if the model is run without edge effects, it follows the
IPCC (2006) inventory approach to assigning carbon storage values by
land cover class. InVEST碳边际效应模型扩展了InVEST碳模型的方法，以解释由于森林边缘的产生而导致的森林碳储量的退化。它应用已知的碳储存与森林边际距离之间的关系来计算碳储存的边缘效应，并将这些估计值与碳库存数据结合起来，构建总体碳地图。边缘效应的模型只涉及地上碳，因为其他碳库（地下、土壤和死物质）的边缘效应还没有记录。对于所有其他碳库，以及非热带森林类型，或者如果模型运行时没有边缘效应，则遵循IPCC（2006）的清单方法，按土地覆盖等级分配碳储存值。

引言
----

The effects of future land-use change on carbon storage or sequestration
can be modeled by applying carbon storage estimates found in the
literature for different habitat types to each habitat found in a
landscape (e.g., Nelson et al. 2010). However, this approach assumes
that all habitat is equivalent in its quality of carbon storage,
regardless of where it occurs, despite the fact that there is
substantial evidence that fragmentation can play a dramatic role in
altering carbon storage and sequestration rates in tropical forests
(Broadbent et al. 2008, Dantas et al 2011, Laurance et al. 1997, 2000,
2001, 2002). For example, core forest has been shown to store more than
three times the carbon of edge forest in Brazilian Atlantic forests
(Dantas et al. 2011). Chaplin-Kramer et al. (2015) investigated this
pattern for the entire pantropics using remotely sensed data on biomass
(Baccini et al 2012) and associated land cover (Friedl et al. 2011) and
found a continuous relationship of carbon storage degrading gradually
toward a forest edge, which varies substantially from region to region.
This model accounts for these documented edge effects in tropical
forests, assigning carbon storage based on the distance of a pixel to
the nearest forest edge. This can improve the overall accuracy of carbon
storage estimates by 20% relative to forest inventory approaches, and
better captures the impacts of forest degradation from fragmentation,
beyond merely the area of habitat lost. 未来土地利用变化对碳储存或封存的影响可以通过将文献中发现的不同生境类型的碳储存估计值应用于景观中发现的每个生境来模拟（例如，Nelson等人，2010）。然而，这种方法假设所有生境的碳储存质量都是相同的，不管它发生在哪里。尽管有大量证据表明，破碎化在改变热带森林的碳储存和固存率方面起着巨大的作用（Broadbent等人，2008；Dantas等人，2011；Laurance等人，1997、2000、2001、2002）。例如，在巴西大西洋森林中，核心林区的碳储存量是边缘林的三倍以上（Dantas等人，2011）。Chaplin-Kramer等人（2015年）利用生物量（Baccini等人2012年）和相关土地覆盖（Friedl等人2011年）的遥感数据调查了整个泛热带地区的这种模式，发现碳储存向森林边缘逐渐退化的连续关系，这在不同地区有很大差异。该模型考虑了热带森林中这些有据可查的边缘效应，根据一个像素与最近的森林边缘的距离来分配碳储存。相对于森林清查方法，这可以将碳储量估计值的总体准确性提高20%，并且更好地捕捉到森林破碎化的影响，而不仅仅是生境损失的面积。

模型
----

The InVEST carbon edge effect model is an update to the InVEST carbon
model, which incorporates the degradation of carbon storage that occurs
due to edge effects in tropical forests. The user designates which land
cover classes are forest, and then the model uses pre-generated
regression results to predict the carbon throughout a forest parcel
based on its distance to the nearest forest edge. These results are
combined with the carbon assigned to non-forest classes through
traditional inventory methods (IPCC 2006) used in the InVEST carbon
model, to generate a map of above-ground carbon storage for all land
cover classes. The InVEST carbon edge effect model can be run to
calculate only above ground carbon or all carbon pools, and it can be
run with or without edge effects. It is important to note that the edge
effects regression only pertains to above-ground carbon stocks because
edge effects have only been detected for above-ground biomass. To
include the other three carbon pools (below-ground, soil, and standing
dead matter), carbon density (Mg/ha) should be included for each land
cover class in the biophysical table. InVEST碳边缘效应模型是对InVEST碳模型的更新，它包含了由于热带森林的边缘效应而发生的碳储存的退化。用户指定哪些土地覆盖类别是森林，然后模型使用预先生成的回归结果，根据其与最近的森林边缘的距离预测整个森林地块的碳。这些结果与InVEST碳模型中使用的传统清查方法（IPCC 2006）分配给非森林类别的碳相结合，生成所有土地覆被类别的地上碳储存图层。InVEST碳边缘效应模型的运行可以只计算地上碳或所有碳库，并且可以在有或没有边缘效应的情况下运行。需要注意的是，边缘效应回归只与地上碳储量有关，因为只检测到地上生物量的边缘效应。为了包括其他三个碳库（地面以下、土壤和立地死物质），应在生物物理表中将每个土地覆盖类别的碳密度（Mg/ha）包括在内。

Also note that the regression data does not cover all of the Earth. It may be useful to make sure that it covers your area of interest by bringing the regression model layer forest_carbon_edge_regression_model_parameters.shp (found in this model's sample data) into a GIS and checking it against your study area. If the regression data does not cover your study area, you cannot use the model to calculate edge effects. 还要注意的是，回归数据并没有覆盖全球。将回归模型层forest_carbon_edge_regression_model_parameters.shp（可在该模型的样本数据中找到）带入GIS并与你的研究区域进行核对，以确保它覆盖你所关注的区域可能是有用的。如果回归数据没有覆盖你的研究区域，你就不能使用该模型来计算边缘效应。


工作原理
~~~~~~~~

This model follows the methodology described in Chaplin-Kramer et al.
(2015), which constructs a series of regression models between forest
biomass density (Mg/ha) and distance from forest edge (km) for 100 km x
100 km grid cells throughout the pantropics. In grid cells where the
majority of pixels were from forest biomes, three candidate regression
models are considered to represent the relationship between biomass
density and distance to forest edge: 该模型遵循Chaplin-Kramer等人（2015）描述的方法，在整个泛热带地区100公里×100公里的网格单元中，构建了森林生物量密度（Mg/ha）与森林边缘距离（km）之间的一系列回归模型。在大多数像素来自森林生物群落的网格单元中，考虑用三个候选回归模型来表示生物量密度与森林边缘距离之间的关系：

1. Asymptotic: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} - \theta_{2} \cdot \mathrm{\exp}( - \theta_{3} \cdot \mathrm{\text{Distance}})`

2. Logarithmic: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot ln(\mathrm{\text{Distance}})`

3. Linear: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot \mathrm{\text{Distance}}`

Then, for each grid cell, the candidate with the highest
r\ :sup:`2` value is used to best represent the relationship between
density and distance to forest edge.  Models (2) and (3) were deemed as
suitable (and more simplistic) alternatives in cells where higher
distances were generally not observed and as a result the forest core
was not firmly established. In the vast majority of grid cells, model
(1) was optimal. 然后，对于每个网格单元，使用具有最高r\ :sup:`2` 值的候选者，以最好地代表密度与森林边缘距离之间的关系。在那些没有观察到更高距离的单元中，模型（2）和（3）被认为是合适的（和更简单的）替代方案，作为结果，森林核心区没有牢固地建立起来。在绝大多数的网格单元中，模型（1）是最佳的。

The results of these regressions can be found in the carbon edge
regression parameter shapefile
(*core_data/forest_carbon_edge_regression_model_parameters.shp*) in the
sample dataset that is provided for the InVEST carbon edge effect model. 这些回归的结果可以在为InVEST碳边缘效应模型提供的样本数据集中的碳边缘回归参数shapefile（*core_data/forest_carbon_edge_regression_model_parameters.shp*）中找到。

For any forest pixel within the study region, the model calculates the
distance of that pixel from forest edge then calculates biomass to a
predefined number of nearest regression models which is then aggregated
to a single result using a distance linear interpolation scheme. The
model then converts biomass to carbon with a user provided conversion
factor, defaulted to 0.47 (IPCC 2006). The user can designate the number
of local models used in the interpolation scheme which is defaulted to
10 but can range anywhere from 1 (only closest point) to 2635 (every
regression model on the planet). Note that a selection of 1 may result
in artificially large differences in carbon when moving from one pixel
to the next where they fall in different regression grid cells. The
higher the number of regression grid cells selected, the smoother the
transition from one pixel to the next. The user may wish to select the
number of grid cells overlapping the entire study region in order to
eliminate any artifacts of model selection. This can be determined by
examining the *intermediate_outputs\local_carbon_shape.shp* geometry
overlaid on the area of interest. The linear interpolation scheme for
biomass b on pixel p is given below对于研究区域内的任何森林像素，该模型计算该像素与森林边缘的距离，然后将生物量计算到预定数量的最近回归模型，再通过距离线性插值方案汇总为一个结果。然后，该模型用用户提供的转换系数将生物量转换为碳，默认系数为0.47（IPCC 2006）。用户可以指定插值方案中使用的局部模型的数量，默认为10个，但范围可以从1（只有最近的点）到2635（地球上的每个回归模型）。请注意，选择1可能会导致从一个像素到下一个像素时，在不同的回归网格单元中出现人为的巨大碳差异。选择的回归网格单元的数量越多，从一个像素到下一个像素的过渡就越平滑。用户可能希望选择覆盖整个研究区域的网格单元的数量，以消除模型选择的任何伪影。这可以通过检查*intermediate_outputs/local_carbon_shape.shp*几何图形覆盖在感兴趣的区域上来确定。生物量b在像素p上的线性内插方案如下：

.. math:: b_{p} = \frac{\sum_{i \in n}\frac{1}{d_{i}}{b_{i}^{'}}_{}}{\sum\frac{1}{d_{i}}}

Where,式中：

-  :math:`b_{p}`\ is the interpolated biomass on pixel p
-  :math:`b_{p}`\是像素p上的内插生物量
-  n is the number of nearest models to interpolate from, a value
   provided by the user
- n是要插值的最近模型的数量，由用户提供。
-  i is the i\ :sup:`th` nearest biomass model from pixel p
- i是离像素p最近的i\ :sup:`th` 生物量模型。
-  d\ :sub:`i` is the distance from pixel p to the centroid of the
   i\ :sup:`th` biomass model.
- d\ :sub:`i`是像素p到i\ :sup:`th` 生物量模型中心点的距离。

The carbon calculated for non-forest classes follows the methodology
from the InVEST carbon model, assigning values based on forest carbon
inventory data designated in the biophysical table. The carbon maps
following this inventory approach and the edge effects approach are
merged into the final carbon map, such that the forest land covers
exhibit edge effects and all other land covers will not. 非森林类的碳计算遵循InVEST碳模型的方法，根据生物物理表中指定的森林碳库存数据进行赋值。按照这种清查方法和边缘效应方法绘制的碳图层被合并到最终的碳图层中，这样，森林土地覆盖物就会表现出边缘效应，而所有其他土地覆盖物则不会。

数据需求
--------
Note that all spatial inputs must be in the same projected coordinate system and in linear meter units. 请注意，所有的空间输入必须在同一个投影坐标系中，并以线性米为单位。

.. - :investspec:`forest_carbon_edge_effect workspace_dir`

.. - :investspec:`forest_carbon_edge_effect results_suffix`

.. - :investspec:`forest_carbon_edge_effect lulc_raster_path`

.. - :investspec:`forest_carbon_edge_effect biophysical_table_path`

..    Columns:

..    - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.lucode`
..    - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.is_tropical_forest`
..    - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_above`
..    - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_below`
..    - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_soil`
..    - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_dead`

..    **Example Biophysical Table (data for Brazil):** 生物物理表示例（巴西的数据）

..    .. csv-table::
..           :file: ./carbon_edge/forest_edge_carbon_lu_table.csv
..           :header-rows: 1
..           :widths: auto

..    *Sources for c_above data*:地上碳数据的来源

..    Closed shrublands, open shrublands, grasslands: Miranda, Sabrina do Couto, et al. Regional variations in biomass distribution in Brazilian savanna woodland. Biotropica 46.2 (2014): 125-138.

..    Woody savannas, savanna: Saatchi, Susan S., et al. Distribution of aboveground live biomass in the Amazon basin. Global Change Biology 13.4 (2007): 816-837.

..    Croplands: Fearnside, Philip M. Greenhouse gases from deforestation in Brazilian Amazonia: net committed emissions. Climatic Change 35.3 (1997): 321-360.

.. - :investspec:`forest_carbon_edge_effect pools_to_calculate`

.. - :investspec:`forest_carbon_edge_effect compute_forest_edge_effects` If selected, the model uses the Chaplin-Kramer et al. method to account for above ground carbon stocks in tropical forest types indicated by a '1' in the 'is_tropical_forest' field in the biophysical table. 如果选择该方法，模型将使用Chaplin-Kramer等人的方法来计算热带森林类型的地面碳储量，该方法在生物物理表中的 "is_tropical_forest "字段中以 "1 "表示。

.. - :investspec:`forest_carbon_edge_effect tropical_forest_edge_carbon_model_vector_path` This input is provided in the sample data and need not be altered unless you have run a separate regression for your region and have better or updated information. The provided shapefile was derived from a pantropical analysis of the relationship between forest biomass and distance from forest edge (Chaplin-Kramer et al. 2015). 这个输入是在样本数据中提供的，不需要改变，除非你对你的研究区域进行了单独的回归模拟，并且有更好或更新的信息。所提供的shapefile来自对森林生物量与森林边缘距离关系的泛热带分析（Chaplin-Kramer等人，2015）。

..    Note that the regression data does not cover all of the Earth. It may be useful to make sure that it covers your area of interest by bringing the regression model  layer *forest_carbon_edge_regression_model_parameters.shp* (found in this model's sample data) into a GIS and checking it against your study area. If the regression data does not cover your study area, you cannot use the model to calculate edge effects. 请注意，回归数据并没有覆盖全球。将回归模型层*forest_carbon_edge_regression_model_parameters.shp*（可在该模型的样本数据中找到）带入 GIS，并与你的研究区域进行核对，以确保其覆盖你所关注的区域可能是有用的。如果回归数据没有覆盖你的研究区域，你就不能使用该模型来计算边缘效应。

.. - :investspec:`forest_carbon_edge_effect n_nearest_model_points` Default value is 10. Higher values smooth the variation in the edge effect detected in the different grid cells (seen in the carbon edge regression parameter shapefile) to a greater degree. - :investspec:`forest_carbon_edge_effect n_nearest_model_points` 默认值为10。更高的值可以在更大程度上平滑不同网格单元中检测到的边缘效应的变化（可在碳边缘回归参数shapefile中看到）。

.. - :investspec:`forest_carbon_edge_effect biomass_to_carbon_conversion_factor` Default value is 0.47 (according to IPCC 2006). This pertains to the edge-effects regression parameters only; all values in the Biophysical Table should already be in terms of carbon, not biomass.
.. - :investspec:`forest_carbon_edge_effect biomass_to_carbon_conversion_factor` 默认值为0.47（参考IPCC 2006）。这只涉及到边缘效应的回归参数；生物物理表中的所有数值都应该是以碳为单位，而不是以生物量为单位。

.. - :investspec:`forest_carbon_edge_effect aoi_vector_path` Note that the regression data does not cover all of the Earth. It may be useful to make sure that it covers your area of interest by bringing the regression model layer *forest_carbon_edge_regression_model_parameters.shp* (found in this model's sample data) into the GIS and checking it against your study area. If the regression data does not cover your study area, you cannot use the model to calculate edge effects.
.. - :investspec:`forest_carbon_edge_effect aoi_vector_path`。请注意，回归数据并没有覆盖全球。将回归模型层*forest_carbon_edge_regression_model_parameters.shp*（可在该模型的样本数据中找到）带入 GIS，并与你的研究区域进行核对，以确保其覆盖你所关注的区域可能是有用的。如果回归数据没有覆盖你的研究区域，你就不能使用该模型来计算边缘效应。

解读结果
--------

最终结果
~~~~~~~~
-  **Parameter log**. Each time the model is run, a text (.txt) file
      will appear in the \ *Workspace*. The file will list the parameter
      values for that run and will be named according to the service,
      the date and time. When contacting NatCap about errors in a model
      run, please include the parameter log.
- **参数日志**。每次模型运行时，一个文本（.txt）文件将出现在\ *Workspace*。该文件将列出该次运行的参数值，并将根据服务、日期和时间来命名。当与NatCap联系有关模型运行中的错误时，请附上参数日志。

-  **carbon_map_[Suffix[.tif**. A map of carbon stock per pixel, with
      the amount in forest derived from the regression based on distance
      to forest edge, and the amount in non-forest classes according to
      the biophysical table. Note that because the map displays carbon
      (Mg) per pixel, coarser resolution maps should have higher values
      for carbon, because the pixel areas are larger.
-  **carbon_map_[Suffix[.tif**.每个像素的碳储量地图，其中森林中的数量是根据与森林边缘的距离回归得出的，而非森林类的数量是根据生物物理表得出的。请注意，由于该地图显示的是每个像素的碳（Mg），较粗的分辨率地图的碳值应该更高，因为像素面积更大。

-  **aggregated_carbon_stocks_[Suffix].shp**: If service areas of
      interest are provided by the user, this output shapefile
      summarizes the total carbon (column *c_sum*) and mean carbon per
      ha (column *c_ha_mean*) in the area polygons defined. Values are
      in Mg.
-  **aggregated_carbon_stocks_[Suffix].shp**:如果用户提供了感兴趣的服务区域，该输出shapefile总结了定义的区域多边形中的总碳（column *c_sum*）和每公顷平均碳（column *c_ha_mean*）。数值的单位是Mg。

中间结果
~~~~~~~~
-  intermediate_outputs\\\ **c_above_carbon_stocks_[Suffix].tif**.
      Carbon stored in the aboveground biomass carbon pool. 储存在地上生物量碳库中的碳。

-  intermediate_outputs\\\ **c_below_carbon_stocks_[Suffix].tif**.
      Carbon stored in the belowground biomass carbon pool. 储存在地下生物量碳库中的碳。

-  intermediate_outputs\\\ **c_dead_carbon_stocks_[Suffix].tif**. Carbon
      stored in the dead matter biomass carbon pool. 储存在死亡物质生物量碳库中的碳。

-  intermediate_outputs\\\ **c_soil_carbon_stocks_[Suffix].tif**. Carbon
      stored in the soil biomass carbon pool. 储存在土壤生物量碳库中的碳。

-  intermediate_outputs\\\ **local_carbon_shape.shp**. The regression
      parameters reprojected to match your study area. 重新预测的与研究区域相匹配的回归参数。

-  intermediate_outputs\\\ **edge_distance_[Suffix].tif**. The distance
      of each forest pixel to the nearest forest edge每个森林像素到最近的森林边缘的距离。

-  intermediate_outputs\\\ **tropical_forest_edge_carbon_stocks_[Suffix].tif**.
      A map of carbon in the forest only, according to the regression
      method根据回归法，仅有森林区域的碳地图。

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
