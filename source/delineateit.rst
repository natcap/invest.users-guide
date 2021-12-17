.. _delineateit:

***********
DelineateIt
***********

Summary
=======

.. figure:: ./delineateit/columbia_ws.png
   :align: center
   :height: 400pt

Introduction
============

Many of the freshwater models in InVEST require watershed polygons to aggregate the ecosystem service provides to beneficiaries. However, we've found the creation of watersheds with existing tools to be difficult and often requiring specific expertise and/or proprietary toolsets. To address this need, we have developed our own watershed delineation algorithm released in the PyGeoprocessing GIS package, and wrapped into a UI inside of InVEST. All DEM routing is handled by PyGeoprocessing which resolves hydrological sinks and plateaus and uses D8 to route flow directions.

Tool Inputs
===========

1. **Workspace**: This is the folder that will contain outputs from RouteDEM after it is run.

2. **Suffix**: If provided, this string will be appended to the filenames of all files created by DelineateIt.

3. **Digital Elevation Model**: A GIS digital elevation model (DEM) raster input. Hydrological sinks and flat plateau regions will be automatically resolved by PyGeoprocessing.

4. **Detect Pour Points**: If this box is checked, the model will detect pour points (watershed outlets) based on the DEM, and use these in place of the user-provided outlet features vector. There is a pour point located at the center of each pixel that flows off the edge of the raster or into a nodata pixel. Flow direction is calculated from the DEM using the D8 algorithm.

5. **Outlet Features**: A vector that is used to specify areas from which the watersheds should be delineated. These geometries may represent stream intake points, population centers, roads, municipality boundaries or other features of interest and may have geometries of any type including, but not limited to, points, lines and polygons. Any fields associated with this vector will be copied to the watershed vector as it is constructed. Required if 'Detect Pour Points' is not checked.

6. **Skip invalid geometries**: If this box is checked, the model will log a ``WARNING`` and will skip delineation for any invalid features found in the Outlet Features. If this box is unchecked and an invalid geometry if found in the outlet vector, the model will crash with an informative error. DelineateIt can only delineate watersheds from valid geometries, so it is up to the user to ensure that all geometries are valid. These may be resolved using the ArcGIS tool "Check Geometry" or QGIS tool "Fix geometries".

7. **Snap points to the nearest stream**: If selected, any point features within the outlet features will be snapped (relocated) to the nearest stream, where streams are defined by a **Threshold Flow Accumulation** value and the maximum distance to snap defined by **Pixel Distance to Snap Outlet Points**. This input will have no effect if **Detect Pour Points** is selected. **NOTE:** DelineateIt will only snap features if they are ``POINT`` or ``MULTIPOINT`` geometries with a single component point. All other geometry types will be unaltered. If a point is equally near to more than one stream pixel, the point is snapped to the stream pixel with the highest flow accumulation value.

8. **Threshold Flow Accumulation**: If an outlet feature does not lie directly on a stream, a very small watershed will be generated which is usually not correct. So DelineateIt can snap outlet features with point geometry to the nearest stream to make more robust watersheds. To do this, the tool constructs a stream layer, which includes any pixels whose flow accumulation values exceed this parameter. Smaller values of this threshold produce streams with more tributaries, larger values produce streams with fewer tributaries.

9. **Pixel Distance to Snap Outlet Points**: If an outlet point does not lie directly on a stream, a very small watershed will be generated which is usually not correct. During watershed construction, DelineateIt will search within a radius of the defined number of pixels around each outlet point to find the nearest stream pixel. Streams are defined by the threshold flow accumulation value listed above. Pixel distance is given as the number of pixels, which is unitless. It is *not* an actual distance (such as meters.) So if you give it a value of 3, DelineateIt will search within a radius of 3 pixels around each outlet point looking for a stream. Note that if the cell size is small, the actual distance searched will be small, if the cell size is large, the actual distance searched will be large. Also note that this snap distance will only be applied to point geometries. Any other geometric types provided in the outlet features vector will be used as they are.

Tool Outputs
============

All outputs can be found in the **Workspace** directory given previously. They include:

 * **watersheds.gpkg** A GeoPackage vector defining the areas that are upstream from the snapped outlet points, where upstream area is defined by the D8 flow algorithm implementation in PyGeoprocessing.

 * **snapped_outlets.gpkg** A vector that indicates where outlet points (point geometries only) were snapped to based on the values of Threshold Flow Accumulation and Pixel Distance to Snap Outlet Points. Any non-point geometries will also have been copied over to this vector, but will not have been altered.

 * **preprocessed_geometries.gpkg** A vector containing only those geometries that the model can verify are valid. The geometries appearing in this vector will be the ones passed to watershed delineation.

 * **streams.tif** The raster stream layer used to snap outlet points, produced from the DEM and Threshold Flow Accumulation value.

 * **filled_dem.tif** The DEM, but with hydrological sinks filled.

 * **flow_direction.tif** The D8 flow direction raster, created from the filled DEM.

 * **flow_accumulation.tif** The D8 flow accumulation raster, created from ``flow_direction.tif``.


References
==========

PyGeoprocessing https://github.com/natcap/pygeoprocessing
