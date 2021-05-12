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

The freshwater models in InVEST are routed across a digital elevation model (DEM).  In the course of developing InVEST we've found existing implementations of flow direction and flow accumulation algorithms to be lacking.  To address this need, we have developed our own high performance implementations of the D8 flow direction algorithm and fractional flow ("Multiple Flow Direction" - MFD), combined with a plateau resolution algorithm to route across flat areas (Garbrecht and Martz) that outperforms TauDEM and GRASS implementations.  We feel these implementations are useful enough that we offer them as a standalone tool that can:

* Fill hydrological sinks.

* Resolve flat areas in a DEM so that all regions drain to some point.

* Compute flow direction across a DEM.

* Compute flow accumulation across a DEM.

* Create streams based on flow accumulation.

This tool may be useful when you are preparing your DEM for use in the freshwater models. For these models, you will want to create streams that are continuous (not all chopped up), and you will need to choose a Threshold Flow Accumulation value that creates a modeled stream network that is as close as possible to the real-world stream network. Using RouteDEM you can test your DEM, see how InVEST handles it, and create stream rasters to help you choose an appropriate Threshold value, without needing to run the whole freshwater model.

After installing InVEST, this tool can be found in the start menu under the InVEST folder as a utility called *RouteDEM*.

RouteDEM will always resolve sinks and plateaus before routing flow.



Tool Inputs
===========

1. **Workspace**: This is the folder that will contain outputs from RouteDEM after it is run.

2. **Results Suffix**: If provided, this text string will be appended to all file names created by the tool.

3. **Digital Elevation Model**: A GIS DEM raster input.  Hydrological sinks and flat plateau regions will be automatically resolved by RouteDEM.

4. **Band Index**: The band index to use from the DEM raster.  If not provided, band index 1 will be used.

5. **Calculate Slope**: Whether to calculate percent slope from the provided DEM.  If checked, the percent slope raster will be written to *slope.tif* in the workspace.

6. **Routing Algorithm**: Select the routing algorithm desired, either D8 or MFD.

7. **Calculate Flow Direction**: Whether to calculate flow direction from the pit-filled, plateau-resolved DEM.  If checked, the flow direction raster will be written to *flow_direction.tif* in the workspace.

8. **Calculcate Flow Accumulation**: Whether to claculate flow accumulation from the flow direction outputs.  If checked, the flow accumulation raster will be written to *flow_accumulation.tif* in the workspace.

9. **Calculate Stream Thresholds**: Whether to create streams from the flow accumulation output.  If checked, all pixels in the flow accumulation raster that have a value greater than or equal to the input *Threshold Flow Accumulation Limit* will be considered a stream. The results are written to *stream_mask.tif*.

10. **Threshold Flow Accumulation Limit**: The number of pixels that must flow into a pixel before it is considered a stream.  Used when thresholding streams and creating the stream mask output.

11. **Calculate Distance to Stream**: Whether to calculate the distance to the stream.  If checked, the distance-to-stream raster will be written to *downstream_distance.tif* in the workspace.


References
==========

Garbrecht, J., Martz, L. W.,The assignment of drainage direction over flat surfaces in raster digital elevation models, Journal of Hydrology, Volume 193, Issues 1–4, 1 June 1997, Pages 204-213, ISSN 0022-1694, http://dx.doi.org/10.1016/S0022-1694(96)03138-1.
(https://www.sciencedirect.com/science/article/abs/pii/S0022169496031381)
