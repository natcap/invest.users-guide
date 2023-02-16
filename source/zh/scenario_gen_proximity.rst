方案生成器：基于邻近感应
===================================

概述
-------

基于邻近度的方案生成器可创建一组对比鲜明的土地利用变化地图，用于转换不同空间模式中的栖息地。用户根据与焦点栖息地边缘的接近程度来确定可以转换的栖息地、转换的内容以及模式类型。通过这种方式，可以产生一系列土地利用变化模式，包括牧场从森林边缘侵占森林，农业从当前耕种地区扩张，森林破碎化等等。然后，生成的土地利用图可以用作InVEST模型的输入，或响应土地利用变化的生物多样性或生态系统服务的其他模型。

简介
------------

为了了解土地利用变化导致的生物多样性和生态系统服务 (BES) 的变化，从一个或一组展示不同类型土地利用变化的情景开始通常是有帮助的。由于景观和BES 之间的许多关系在空间上是明确的，因此对于相同的栖息地转换总面积，不同的栖息地转换模式可能会对 BES 产生不同的影响。这种基于邻近度的情景生成器根据用户输入的指定焦点栖息地和转化栖息地创建不同的转换模式，与 InVEST 基于规则的情景生成器相反，它可能是对根据用户分配的某些转换将发生的概率创建土地利用变化图的情景生成器的补充。因此，基于InVEST邻近度的情景生成器的目的不是预测实际的扩张模式，而是开发不同的土地利用变化模式，以检查土地利用变化与 BES 之间的关系，以及这种关系如何可能因土地利用变化假设而有所不同。

模型
---------

该工具可以同时生成两个方案（最靠近焦点栖息地的边缘和最远的边缘），以便转换为给定区域的特定栖息地类型。要转换为不同的栖息地类型、不同的栖息地数量、或者指定不同的焦点栖息地或转换后的栖息地，可以按顺序多次运行该工具。

工作原理
~~~~~~~~~~~~

必须定义三种类型的土地覆被：1）*Focal* *landcover*是设置邻域规则的土地覆被，从中确定情景。场景生成器会将栖息地从这些类型土地覆被的斑块的边缘或边缘转换。这并不意味着它将转换这些土地覆被，只是测量与边缘的距离，以指定转换发生的位置。2）*Convertible landcover*是可以转换的土地覆被物。这些可能与焦点土地覆盖相同、部分相同或完全不同。3）*Replacement landcover*是可转换土地覆被将转换为的土地覆被类型。每次模型运行只能使用一种土地覆被类型。

可以一次运行两种方案：1）*Nearest to edge*表示最接近焦点土地覆被边缘的可转换土地覆被类型将转换为替换土地覆被。2） *Farthest from edge*表示距离焦点土地覆被类型边缘最远的可转换土地覆被类型将转换为替换地被。如果选择此方案，用户可以指定应进行转换的步骤数。如果焦点土地覆被与可转换土地覆被相同，则这一点很重要，因为焦点土地覆被的转换将创建新的边，从而影响从该土地覆被边缘计算的距离。如果需要，转换可以分几个步骤进行，每次转换距离焦点土地覆被边缘最远的地方就会导致碎片模式。

下面是一些方案类型的示例，这些方案类型可以通过使用此模型附带的示例数据中的土地覆被这些基本输入来生成。该土地覆盖来自MODIS，使用UMD分类（Friedl等人，2011年），遵循以下方案：1-常绿针叶林;2–常绿阔叶林;3–落叶针叶林;4–落叶阔叶林;5–混交林;6–封闭的灌木丛;7–开阔的灌木丛;8–热带稀树草原;9–热带大草原;10–草原;12–耕地;13–城市和建成建筑;16–贫瘠或植被稀疏。

**从森林边缘向内扩展农业：**

焦点土地覆盖代码: 1 2 3 4 5

可转换土地覆盖代码: 1 2 3 4 5

替代土地覆被代码: 12

选中“转换为最接近边缘”

转换步骤数: 1

**从森林核心向外扩展农业**:

焦点土地覆盖代码: 1 2 3 4 5

可转换土地覆盖代码: 1 2 3 4 5

替代土地覆被代码: 12

选中“转换为最远离边缘”

转换步骤数: 1

**通过分割森林来扩大农业：**

焦点土地覆盖代码: 1 2 3 4 5

可转换土地覆盖代码: 1 2 3 4 5

替代土地覆被代码: 12

选中“转换最远离边缘”

转换步骤数: 10 (或根据需要设置任意步骤;步骤越多，碎片化越精细，模拟所需的时间就越长)

**将牧场扩大到离现有农业最近的森林：**

焦点土地覆被代码: 12

可转换土地覆盖代码: 1 2 3 4 5

替换土地覆盖代码: 10

选中“转换为最接近边缘”

转换步骤数: 1

数据需求
----------

运行基于邻近的方案生成器唯一需要的输入数据是基础土地利用/土地覆被地图和与此底图相关的用户定义的土地覆被代码，以指定应如何计算方案。

- :investspec:`scenario_gen_proximity workspace_dir`

- :investspec:`scenario_gen_proximity results_suffix`

- :investspec:`scenario_gen_proximity base_lulc_path`

- :investspec:`scenario_gen_proximity aoi_path` 在场景生成之前，地图将被裁剪到此矢量的范围。

- :investspec:`scenario_gen_proximity area_to_convert` 将在不超过此区域的情况下转换尽可能多的像素。

- :investspec:`scenario_gen_proximity focal_landcover_codes`

- :investspec:`scenario_gen_proximity convertible_landcover_codes`

- :investspec:`scenario_gen_proximity replacement_lucode` 如果有多个 LULC 类型需要转换，则应按顺序运行此工具，每次选择一种转换类型。如果这是该地区的新土地利用，或者如果希望将扩大的土地利用与历史土地利用分开进行跟踪，则可以引入新的代码。

- :investspec:`scenario_gen_proximity convert_farthest_from_edge` 可转换土地覆被和感兴趣的栖息地土地覆被可能是相同的，也可能是彼此的子集，也可以是不同的。如果它们相同，则应指定转换步骤的数目，因为焦点土地覆盖内生境的转换将创建新的栖息地边缘，根据选择的步骤数会导致完全不同的转换模式。

- :investspec:`scenario_gen_proximity convert_nearest_to_edge` 可转换土地覆被和感兴趣的栖息地土地覆被可能是相同的，或者是彼此的子集，也可以是不同的。

- :investspec:`scenario_gen_proximity n_fragmentation_steps` 输入 1 表示所有栖息地转换都将发生在感兴趣栖息地斑块的中心。输入 10 将根据顺序转换离该栖息地边缘最远的像素的模式进行分段，超过用户指定的步数。

结果解释
--------------------

最终结果
~~~~~~~~~~~~~

- **InVEST….log…txt:** 每次运行模型时，*输出*文件夹中都会显示一个文本（.txt）文件。该文件将列出该运行的参数值，并根据模型、日期和时间以及后缀进行命名。

- **nearest_to_edge \_<suffix>.tif**:最接近焦点栖息地边缘的转换方案的LULC 栅格。

- **farthest_from_edge_<suffix>.tif**:最远离焦点栖息地边缘的转换方案的LULC 栅格。

- **nearest_to__edge_<suffix>.csv**: 列出针对最接近焦点生境边缘的转换方案转换的不同土地覆被类型的面积（以公顷为单位）和栅格数的表格。

- **farthest_from_edge \_<suffix>.csv**: 列出针对最接近焦点生境边缘的转换方案转换的不同土地覆被类型的面积（以公顷为单位）和栅格数的表格。

中间结果
~~~~~~~~~~~~~~~~~~~~

- **{farthest_from_/nearest_to}_edge_distance_<suffix>.tif**: 此栅格显示每个像素到焦点陆地覆被最近边的距离（以栅格数为单位）。

- **_tmp_work_tokens:** 此目录存储内部使用的元数据，以避免重新计算。

示例脚本
-------------

提供以下脚本来演示如何将“工作原理”部分中描述的方案组合成可从 InVEST Python API 调用的单个脚本:

        import natcap.invest.scenario_generator_proximity_based

        edge_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': False,
            u'convert_nearest_to_edge': True,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'edge',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        core_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': True,
            u'convert_nearest_to_edge': False,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'core',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        frag_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': True,
            u'convert_nearest_to_edge': False,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'10',
            u'replacement_lucode': u'12',
            u'results_suffix': 'frag',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        ag_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': False,
            u'convert_nearest_to_edge': True,
            u'convertible_landcover_codes': u'12',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'ag',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }
        if __name__ == '__main__':
            natcap.invest.scenario_generator_proximity_based.execute(edge_args)
            natcap.invest.scenario_generator_proximity_based.execute(core_args)
            natcap.invest.scenario_generator_proximity_based.execute(frag_args)
            natcap.invest.scenario_generator_proximity_based.execute(ag_args)
