.. _delinateit:

**********
DelinateIT
**********

Summary
=======

.. figure:: ./delineateit_images/columbia_ws.png
   :align: center
   :width: 400pt

Introduction
============

Many of the freshwater models in InVEST require watershed polygons to aggregate the ecosystem service provides to beneficiaries.  However, we've found the creation of watersheds with existing tools to be difficult and often requiring specific expertise and/or proprietary toolsets.  To address this need, we have developed our own watershed delination algorithm released in the PyGeoprocessing GIS package, and wrapped into a UI inside of InVEST.  All DEM routing is handled by PyGeoprocessing which resolves plateaus and uses d-infinity to route flow directions.

After installing InVEST, this tool can be found in the start menu under the InVEST folder as a utility called DelinateIT.

Tool Inputs
===========

1. **Workspace**: This is the folder that will contain outputs from RouteDEM after it is run.

2. **DEM**: A GIS DEM raster input.  The DEM should first be pit filled.  Flat plateau regions will be automatically resolved by PyGeoprocessing.

3. **Outlet Points**: This is a point shapefile that is used to specify areas which the watersheds should be constructed around.  These may be stream intake points, population centers, or other points of interest.  Any fields associated with this dataset will be copied to the watershed shapefile as it is constructed.

4. **Threshold flow accumulation**: DelineateIT can snap outlet points to the nearest stream to make more robust watersheds than those that are off center of a pixel.  To do this, the tool constructs a stream layer is constructed by thresholding any pixels whose flow accumulation values exceed this parameter.

5. **Pixel Distance to Snap Outlet Points**: During watershed construction, DelineateIT will search a window of this size to find the nearest stream pixel classified by the threshold flow accumulation given previously.

Tool Outputs
============

All outputs can be found in the **Workspace** directory given previously.  They include:

 * **watersheds.shp** this is a polygon shapefile defining the areas that are upstream from the snapped outlet points; upstream defined by the d-infinity flow algorithm implementation in PyGeoprocessing.

 * **snapped_outlets.shp** this is a point shapefile that indicates where the outlet points were snapped to based on the values of "threshold flow accumulation" and "pixel distance to snap".

 * **stream.tif** this is the raster stream layer used to snap outlet points.

References
==========

PyGeoprocessing https://bitbucket.org/richpsharp/pygeoprocessing
