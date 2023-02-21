.. DEM路径:

********
DEM路径
********

总结
=======

.. figure:: ./routedem/routedem.png
   :align: center
   :width: 400pt



介绍
============

InVEST中的淡水模型通过数字高程模型(DEM)进行路由。在InVEST的开发过程中，我们发现现有的流向和流量积累算法的实现是存在不足的。为了解决这一需求，我们开发了自己的D8流向算法和分数流(“多流方向”-MFD)，结合高原分辨率算法，穿越平坦区域(Garbrecht和Martz)，其性能优于TauDEM和GRASS。我们认为这些模型的实现足够有用，所以我们将它们作为一个独立的工具提供，可以:

* 填满水文水槽。

* 解决DEM中的平坦区域，使所有区域都排水到某个点。

* 计算DEM上的水流方向。

* 计算DEM上的流量累积。

* 基于流量累积生成流。

当您准备在淡水模型中使用DEM时，此工具可能很有用。对于这些模型，您将希望创建连续的流(而不是全部分割)，并且您将需要选择一个流量积累值阈值，以创建尽可能接近真实流网络的建模流网络。使用RouteDEM，您可以测试您的DEM，查看InVEST如何处理它，并创建流栅格来帮助您选择适当的阈值，而不需要运行整个淡水模型。

安装InVEST后，可以在InVEST文件夹下的开始菜单中找到这个工具，它是一个名为*RouteDEM*的实用工具。

连接流之前，RouteDEM总能解析（识别）下沉和高原.



输入工具
===========

- :investspec:`routedem workspace_dir`

- :investspec:`routedem results_suffix`

- :investspec:`routedem dem_path` 该模型将自动解析水文汇和平坦高原地区。

- :investspec:`routedem dem_band_index` 如果没有提供，则使用频带索引1。

- :investspec:`routedem algorithm`

- :investspec:`routedem calculate_slope`

- :investspec:`routedem calculate_flow_direction` 这将被写入输出文件 *flow_direction.tif*.

- :investspec:`routedem calculate_flow_accumulation` 这将被写入输出文件*flow_accumulation.tif*.

- :investspec:`routedem calculate_stream_threshold` 这将被写入输出文件 *stream_mask.tif*. 流量累积栅格中所有值大于或等于 **Threshold Flow Accumulation Limit** 的栅格将被视为流。

- :investspec:`routedem threshold_flow_accumulation`

- :investspec:`routedem calculate_downslope_distance` 在工作区中，这将被写入输出文件 *downslope_distance.tif*. 距离以像素数表示。要将像素距离转换为线性单位，请将*downslope_distance.tif*栅格乘以像素大小。


参考文献
==========

Garbrecht, J., Martz, L. W.,The assignment of drainage direction over flat surfaces in raster digital elevation models, Journal of Hydrology, Volume 193, Issues 1–4, 1 June 1997, Pages 204-213, ISSN 0022-1694, http://dx.doi.org/10.1016/S0022-1694(96)03138-1.
(https://www.sciencedirect.com/science/article/abs/pii/S0022169496031381)
