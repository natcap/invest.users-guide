.. primer

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

The freshwater models in InVEST are routed across a DEM.  In the course of developing InVEST we've found existing implementations of flow direction and flow accumulation algorithms to be lacking.  To address this need, we have developed our own high performance implementations of the d-infinity flow direction algorithm (Tarboton 1997), combined with a plateau resolution algorithm to route across flat areas (Garbrecht and Martz) that outperforms TauDEM and GRASS implementations.  We feel these implementations are useful enough that we offer them as a standalone tool that can calculate:

* Resolving flat areas in a DEM so that all regions, except pits, drain to some point.

* The d-infinity flow direction across an arbitrary DEM.

* The d-infinity flow accumulation algorithm across a DEM.

* Stream thresholding of the flow accumulation algorithm.

After installing InVEST, this tool can be found in the start menu under the InVEST folder as a utility called RouteDEM.


Tool Inputs
===========

1. **Workspace**: This is the folder that will contain outputs from RouteDEM after it is run.

2. **DEM**: A GIS DEM raster input.  For a good route, the DEM should first be pit filled.  Flat plateau regions will be automatically resolved by RouteDEM.

3. **Plateau Resolved DEM Filename**: This is the name of the output file that the plateau resolved dem will be saved to in the workspace.

4. **Flow Direction Filename**: This is the name of the output file that the d-infinity flow direction raster will be saved to in the workspace.

5. **Flow Accumulation Filename**: This is the name of the output file that the d-infinity flow accumulation raster will be saved to in the workspace.

6. **Threshold flow accumulation**: This is the value that will be used to threshold the flow accumulation raster to create a stream layer.  The output will be called stream_[threshold].tif in the workspace where [threshold] will be replaced by the value in this input.

7. **Calculate multiple stream thresholds**: If checked, multiple stream threshold rasters will be generated where

  7a. **Threshold Flow Accumulation Upper Limit** is the upper value of the multiple stream threshold set.

  7b. **Step size** is the number of threshold steps to take between rasters.  If the original flow accumulation raster is 1000, the threshold upper limit is 2000 and the step size is 100, RouteDEM will generate 10 stream threshold rasters of limits 1000, 1100, 1200, ..., 2000.  This can be useful to explore the space of this parameter for other InVEST inputs that require a threshold stream layer to be defined.

8. **Calculate slope**: If checked RouteDEM will also calculate the slope of the input DEM.  If selected also define **Slope Filename** as the name of the output slope raster to be placed in the workspace.

.. primerend

References
==========

Garbrecht, J., Martz, L. W.,The assignment of drainage direction over flat surfaces in raster digital elevation models, Journal of Hydrology, Volume 193, Issues 1–4, 1 June 1997, Pages 204-213, ISSN 0022-1694, http://dx.doi.org/10.1016/S0022-1694(96)03138-1.
(http://www.sciencedirect.com/science/article/pii/S0022169496031381)

Tarboton, D. G. (1997), A new method for the determination of flow directions and upslope areas in grid digital elevation models, Water Resour. Res., 33(2), 309–319, doi:10.1029/96WR03137.

