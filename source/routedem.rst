.. _routedem:

********
RouteDEM
********

Summary
=======

.. figure:: ./routedem/routedem.png
   :align: center
   :width: 400pt



Introduction
============

The freshwater models in InVEST are routed across a DEM.  In the course of developing InVEST we've found existing implementations of flow direction and flow accumulation algorithms to be lacking.  To address this need, we have developed our own high performance implementations of the D8 flow direction algorithm and fractional flow ("Multiple Flow Direction"), combined with a plateau resolution algorithm to route across flat areas (Garbrecht and Martz) that outperforms TauDEM and GRASS implementations.  We feel these implementations are useful enough that we offer them as a standalone tool that can calculate:

* Filling hydrological sinks.

* Resolving flat areas in a DEM so that all regions drain to some point.

* Compute flow direction across an arbitrary DEM.

* Compute flow accumulation across a DEM.

* Stream thresholding of the flow accumulation algorithm.

After installing InVEST, this tool can be found in the start menu under the InVEST folder as a utility called *RouteDEM*.

RouteDEM will always resolve sinks and plateaus before routing flow.


Tool Inputs
===========

1. **Workspace**: This is the folder that will contain outputs from RouteDEM after it is run.

2. **Results Suffix**: If provided, this suffix will be appended to all files created by the tool.

3. **Digital Elevation Model**: A GIS DEM raster input.  Hydrological sinks and flat plateau regions will be automatically resolved by RouteDEM.

4. **Band Index**: The band index to use from the DEM raster.  If not provided, band index 1 will be used.

5. **Calculate Slope**: Whether to calculate slope from the provided DEM.  If checked, the slope raster will be written to *slope.tif* in the workspace.

6. **Routing Algorithm**: Select the routing algorithm desired.

7. **Calculate Flow Direction**: Whether to calculate flow direction from the pit-filled, plateau-resolved DEM.  If checked, the flow direction raster will be written to *flow_direction.tif* in the workspace.

8. **Calculcate Flow Accumulation**: Whether to claculate flow accumulation from the flow direction outputs.  If checked, the flow accumulation raster will be written to *flow_accumulation.tif* in the workspace.

9. **Calculate Stream Thresholds**: Whether to calculate stream thresholds from the flow accumulation output.  If checked, the flow accumulation raster will be thresholded by the limit defined by *Threshold Flow Accumulation Limit* and written to *stream_mask.tif*.

10. **Threshold Flow Accumulation Limit**: The number of pixels that must flow into a pixel before it is considered a stream.  Used when thresholding streams and creating the stream mask output.

11. **Calculate Distance to Stream**: Whether to calculate the distance to the stream.  If checked, the distance-to-stream raster will be written to *downstream_distance.tif* in the workspace.


References
==========

Garbrecht, J., Martz, L. W.,The assignment of drainage direction over flat surfaces in raster digital elevation models, Journal of Hydrology, Volume 193, Issues 1–4, 1 June 1997, Pages 204-213, ISSN 0022-1694, http://dx.doi.org/10.1016/S0022-1694(96)03138-1.
(http://www.sciencedirect.com/science/article/pii/S0022169496031381)
