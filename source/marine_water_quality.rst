.. _marine-water-quality:

**************************
Marine Water Quality Model
**************************

Summary
=======

This is a preliminary user's guide for the InVEST 3.0 Marine Water Quality Model.

The model
=========

This model predicts concentration of a pollutant by solving the steady state diffusion advection equation

.. math::   \nabla\cdot \mathbf{E}\nabla s - \mathbf{U} \nabla s - Ks = 0
   :label: eq1

Where 

 * :math:`E` is the tidal dispersion coefficient in units of :math:`km^2/day`
 * :math:`U` is a two dimensional vector of advective velocity in units of :math:`m/sec`
 * :math:`K` is the decay rate of the pollutant in units of :math:`\mathrm{day}^{-1}`
 * :math:`s` is the density of the pollutant in units of
   :math:`kg/m^3`

Data inputs
===========

The following inputs are required to run the marine water quality model:

* **Output pixel size in meters** this parameter is used to determine the output resolution of the pollutant density raster.  A larger number will make the output grid coarser but the model will run faster, while a finer resolution will require more computation and memory.  Try making this number larger if a model run causes an out of memory error.

* **Workspace** The directory to hold output and intermediate results of the particular model run.  After the model is complete the output will be located in this directory.

* **Absorption Coefficient (K)** The decay rate as described in Equation :eq:`eq1`.

* **Area of Interest (AOI)** An ESRI Shapefile that contains a polygon indicating the area at which the solution should be run.  The output raster will align with the area of extents of this polygon.  The polygon itself should be projected into meters.

* **Land Polygon** An ESRI Shapefile that contains a polygon indicating where the landmass lies.

* **Source Point Centroids** An ESRI Shapefile that contains a point layer indicating the centroids of point pollutant sources that must have a field called ``Id`` that indicates the unique identification number for that point.  This file must be in the same projection as the *AOI* polygon.

* **Source Point Data Table** A csv table that contains at least the headers ``ID`` and ``WPS`` which correspond to the identification number in the *Source Point Centroids* shapefile and the amount of loading of pollutant that point source in terms of kilograms per day.

* **Tidal Diffusion Constants** An ESRI Shapefile that contains a point layer with a field named ``kh_km2_day`` indicating the tidal dispersion coefficient at that point as referenced in Equation :eq:`eq1`.  This file must be in the same projection as the *AOI* polygon.

* **Advection Vectors (UV as point data)** An ESRI Shapefile that contains a point layer with two fields named `U_m_sec_` and `V_m_sec_` which correspond to the *u* and *v* components of the 2D advective velocity vector *U* as referenced in Equation :eq:`eq1`.  This file must be in the same projection as the *AOI* polygon.


Outputs
=======

All the outputs below are relative to the workspace path specified in the input of the model.

* ``intermediate/in_water.tif`` a raster indicating the land and water points that's used in the calculation of the domain to discritize Equation :eq:`eq1`.

* ``intermediate/tide_e.tif`` a raster with the interpolated values of the *Tidal Diffusion Constants* shapefile that are used to determine the E values for each discritized grid cell.

* ``intermediate/adv_u.tif`` and ``intermediate/adv_v.tif`` a raster with the interpolated values of the *Advection Vectors (UV as point data)* shapefile that are used to determine the *u* and *v* components respectively.

* ``output/concentration.tif`` the output raster indicating the concentration of the pollutant in terms of :math:`\mathrm{kg/m^3}`.

..  LocalWords:  InVEST advection nabla cdot mathbf eq advective mathrm AOI csv
..  LocalWords:  ESRI Shapefile WPS shapefile kh
