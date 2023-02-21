.. _delineateit:

***********
划定IT
***********

概述
=======

.. figure:: ./delineateit/columbia_ws.png
   :align: center
   :height: 400pt

简介
============

在InVEST中，许多淡水模型需要流域多边形来聚集提供给受益人的生态系统服务。
然而，我们发现使用现有的工具建立流域是困难的，他往往需要特定的专业知识和/或专有工具集。为了满足这一需求，我们开发了在PyGeoprocessing GIS包中发布的流域划分算法，并包装成InVEST内部的一个UI。所有DEM路径都由PyGeoprocessing处理，这解析了水文汇流和高原，并使用D8来规划流向的路径

另请参阅本用户指南的**使用DEM** 部分，了解有关准备 DEM 以在 Invest 中使用以及使用它创建流域和分水岭的更多信息。

模型步骤
===========

填充 坑
^^^^^^^^^
首先，模型填充 DEM 中的任何坑（水文汇流）。此步骤有助于确保所有像素从栅格的定义区域流出

计算流向
^^^^^^^^^^^^^^^^^^^^^^^^
该模型将 D8 路径算法应用于填充的 DEM，以计算水从每个像素流出的方向。

检测倾点
^^^^^^^^^^^^^^^^^^
倾泻点是水流流向地图定义区域的点，水流为从栅格边缘流出或流入无数据像素。
如果您选择了检测倾点选项，则模型将在栅格边缘流出或流入无数据像素的每个像素中心放置一个倾点。或者，您也可以通过*流域出口*输入提供自己的倾点图层。


捕捉最近的水流
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
如果出口要素不直接位于溪流上，则会生成一个非常小的分水岭，这通常是不正确的。划定IT可以将点出口要素捕捉到最近的溪流，以形成更强大的流域。为此，该工具将构建河流地图，然后将分水岭出口点重新定位到作为模型输入*捕捉距离*内的最近河流。

计算累计流量
---------------------------
该模型使用 D8 算法计算流向栅格的流量累积。这表示从上坡区域流到像素上的相对水量。

阈值流量累积 (TFA)
---------------------------------
该模型通过按 TFA 值对流量累积栅格进行阈值化来识别河流。流量累积大于或等于TFA值的区域被视为河流。

划定流域
^^^^^^^^^^^^^^^^^^^^
该模型使用 D8 算法根据流向栅格和流域出口几何（如果提供）或检测到的倾泻点（如果选择了检测倾泻点）生成流域的面矢量。

工具输入
===========

- :investspec:`delineateit.delineateit workspace_dir`

- :investspec:`delineateit.delineateit results_suffix`

- :investspec:`delineateit.delineateit dem_path` 水文汇流和平坦高原区域将通过PyGeoprocessing处理自动求解。

- :investspec:`delineateit.delineateit detect_pour_points` 每个像素的中心都有一个倾点，该倾点从栅格边缘流出或流入无数据像素。流向是对DEM使用 D8 算法计算得来。

- :investspec:`delineateit.delineateit outlet_vector_path` 这些几何可以表示为河流进水点、人口中心、道路、自治市边界或其他感兴趣的要素，并且可以是任何几何类型，包括点、线或面。与此矢量关联的任何字段都将复制到输出流域矢量。

- :investspec:`delineateit.delineateit skip_invalid_geometry` 如果跳过任何几何图形，日志文件将包含警告消息。描绘它只能从有效的几何中描绘分水岭，因此用户有责任确保所有几何都有效。可以使用 ArcGIS 工具"检查几何"或 QGIS 工具"修复几何"解决这些问题。

- :investspec:`delineateit.delineateit snap_points` 只有``点``几何图形或具有单个组件点的``多点``几何图形将被重新定位。所有其他几何类型将保持不变。如果选择了**检测倾点**，则此输入将不起作用。

- :investspec:`delineateit.delineateit flow_threshold` 此阈值的值越小，产生的支流越多，值越大，支流越少。

- :investspec:`delineateit.delineateit snap_distance` 请注意，这是以像素为单位距离，而不是米，因此请根据您的像素大小进行缩放。


工具输出
============

所有输出都可以在前面给出的 **工作区** 目录中找到。它们包括：

 * **watersheds.gpkg** 一个 GeoPackage 矢量，用于定义捕捉出口点上游的区域，其中上游区域由 PyGeoprocessing 中的 D8 算法实现划分。

 * **snapped_outlets.gpkg** ，一个矢量，其根据“阈值流量累积”和“像素距捕捉出口点”的值捕捉的出口点（仅限点几何）的位置。任何非点几何也将复制到此矢量，但不会更改

 * **preprocessed_geometries.gpkg** 其仅包含模型可以验证的几何图形是否为有效的矢量。此矢量中显示的几何将是传递给流域描绘的几何。

 * **streams.tif** 用于捕捉出口点的栅格流图层，由DEM和阈值流量累积值生成。

 * **filled_dem.tif** DEM数据,且水文汇流点已经被填充。

 * **flow_direction.tif** 根据填充的DEM创建D8流向栅格。

 * **flow_accumulation.tif** 根据``flow_direction.tif``创建的 D8 流量累积栅格。


参考
==========

PyGeoprocessing https://github.com/natcap/pygeoprocessing
