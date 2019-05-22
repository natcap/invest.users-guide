.. primer
.. _delineateit:

***********
DelineateIT
***********

Summary
=======

.. figure:: ./delineateit_images/columbia_ws.png
   :align: center
   :height: 400pt

Introduction
============

Many of the freshwater models in InVEST require watershed polygons to aggregate the ecosystem service provides to beneficiaries.  However, we've found the creation of watersheds with existing tools to be difficult and often requiring specific expertise and/or proprietary toolsets.  To address this need, we have developed our own watershed delineation algorithm released in the PyGeoprocessing GIS package, and wrapped into a UI inside of InVEST.  All DEM routing is handled by PyGeoprocessing which resolves plateaus and uses d-infinity to route flow directions.

After installing InVEST, this tool can be found in the start menu under the InVEST folder as a utility called DelinateIT.


Tool Inputs
===========

1. **Workspace**: This is the folder that will contain outputs from RouteDEM after it is run.

2. **Digital Elevation Model**: A GIS digital elevation model (DEM) raster input.  The DEM should first be pit filled, using a GIS tool such as Wang and Liu in QGIS.  Flat plateau regions will be automatically resolved by PyGeoprocessing.

3. **Outlet Points**: A point shapefile that is used to specify areas which the watersheds should be constructed around.  These may be stream intake points, population centers, or other points of interest.  Any fields associated with this dataset will be copied to the watershed shapefile as it is constructed.

4. **Threshold Flow Accumulation**: If an outlet point does not lie directly on a stream, a very small watershed will be generated, which is usually not correct. So DelineateIT can snap outlet points to the nearest stream to make more robust watersheds.  To do this, the tool constructs a stream layer by thresholding any pixels whose flow accumulation values exceed this parameter. Smaller values of this threshold produce streams with more tributaries, larger values produce streams with fewer tributaries.

5. **Pixel Distance to Snap Outlet Points**: If an outlet point does not lie directly on a stream, a very small watershed will be generated, which is usually not correct. During watershed construction, DelineateIT will search within a radius of the defined number of pixels around each outlet point to find the nearest stream pixel. Streams are defined by the threshold flow accumulation value listed above. Pixel distance is given as the number of pixels, which is unitless. It is *not* an actual distance (such as meters.) So if you give it a value of 3, DelineateIt will search within a radius of 3 pixels around each outlet point looking for a stream. Note that if the cell size is small, the actual distance searched will be small, if the cell size is large, the actual distance searched will be large.

Tool Outputs
============

All outputs can be found in the **Workspace** directory given previously.  They include:

 * **watersheds.shp** A polygon shapefile defining the areas that are upstream from the snapped outlet points, where upstream area is defined by the d-infinity flow algorithm implementation in PyGeoprocessing.

 * **snapped_outlets.shp** A point shapefile that indicates where the outlet points were snapped to based on the values of Threshold Flow Accumulation and Pixel Distance to Snap Outlet Points.

 * **stream.tif** The raster stream layer used to snap outlet points, produced from the DEM and Threshold Flow Accumulation value.

References
==========

PyGeoprocessing https://bitbucket.org/richpsharp/pygeoprocessing
.. primerend
