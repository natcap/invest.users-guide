.. _marine-water-quality:

*********
SDR model
*********

Summary
=======

The objective of the InVEST sediment delivery model is to map overland sediment generation and delivery to the stream. In a context of global change, such information can be used to study the service of sediment retention in a catchment. This is of particular interest for reservoir management and instream water quality, both of which may be economically valued.

The main differences between the InVEST SDR model and the InVEST Sediment retention model found in InVEST v3.0.1 and earlier are:

 * The routing of sediment from a cell to the stream was modified to remove the sensitivity to grid resolution and facilitate the selection of LULC-specific retention coefficient;

 * (Optional) calibration is based on one non-physical parameter that preserves the spatial distribution of sediment sinks and sources, facilitating the interpretation of spatially explicit outputs;

 * The increased flexibility in model structure allows advanced users to represent more complex processes such as gully erosion or instream retention (work is in progress to facilitate the representation of these processes for InVEST users)



Introduction
============

Erosion and overland sediment retention are natural processes that govern the sediment concentration in streams. Sediment dynamics at the catchment scale are mainly determined by climate (in particular the rain intensity), soil properties, topography, and vegetation; and anthropogenic factors such as agricultural activities or dam construction and operation. Main sediment sources include overland erosion (soil particles detached and transported by rain and overland flow), gullies (channels that concentrate flow), bank erosion, and mass erosion (or landslides; see Merrit 2003 for a review). Sinks include on-slope, floodplain or instream deposition, and reservoir retention, as summarized in Figure 1. Conversion of land use and changes in land management practices may dramatically modify the amount of sediment running off a catchment. The magnitude of this effect is primarily governed by: i) the main sediment sources (land use change will have a smaller effect in catchments where sediments are not primarily coming from overland flow); and ii) the spatial distribution of sediment sources and sinks (for example, land use change will have a smaller effect if the sediment sources are buffered by vegetation). 

Increases in sediment yield are observed in many places of the world, dramatically affecting water quality and reservoir management (UNESCO 2009). The sediment retention service provided by natural landscapes is of great interest to water managers. Understanding where the sediments are produced and delivered allow them to design improved strategies for reducing sediment loads. Changes in sediment load can have impacts on downstream irrigation, water treatment, recreation and reservoir performance. 

The outputs from the sediment model include the sediment load delivered to the stream at an annual time scale, as well as the amount of sediment eroded in the catchment and retained by vegetation and topographic features. The model provides two options for valuation of the sediment retention service, though appropriate valuation approaches will be highly dependent on the particular application and context, and may need to be implemented independent of InVEST.



.. figure:: ./sdr_images/sediment_budget.png

    Figure 1. General catchment sediment budget. The relative size of the arrows changes depending on the environment. The InVEST model focuses on the overland processes.



The model
=========

Biphysical Model
----------------

Sediment Delivery
^^^^^^^^^^^^^^^^^

The sediment delivery module is a spatially-explicit model working at the spatial resolution of the input DEM raster. For each cell, the model first computes the amount of eroded sediment, then the sediment delivery ratio (SDR), which is the proportion of soil loss actually reaching the catchment outlet. This approach was proposed by Borselli et al. (2008) and has received increasing interest in recent years (Cavalli et al., 2013; López-vicente et al., 2013; Sougnez et al., 2011). See Advantages and limitations for further discussion.


Annual soil loss
""""""""""""""""

The amount of annual soil loss on pixel :math:`i`, :math:`usle_i` :math:`(ton ha^1 yr^1)`, is given by the revised universal soil loss equation (RUSLE1):

.. math:: usle_i=R_i\cdot K_i\cdot LS_i\cdot C_i\cdot P_i,

where 

 * :math:`R_i` is the rainfall erosivity (:math:`MJ\cdot mm (ha\cdot hr)^1)`, 

 * :math:`K_i` is the soil erodibility (:math:`ton\cdot ha\cdot hr (MJ\cdot ha\cdot mm)^1`), 

 * :math:`LS_i` is the slope length-gradient factor

 * :math:`C_i` is the crop-management factor 

 * and :math:`P_i` is the support practice factor (Renard et al., 1997). (cf. also in (Bhattarai and Dutta, 2006)). 

and :math:`LS_i` factor is given from the method developed by Desmet and Govers (1996) for two-dimension surface:

.. math:: L_i=S_i \frac{(A_{i-in}+D^2}^{m+1}-A_{i-in}^{m+1}}/{D^{m+2}\cdot x_i^m\cdot (22.13)^m}

where

 * :math:`S_i` the slope factor for grid cell calculated as function of slope degree :math:`\theta`

  - :math:`S=10.8\cdot \sin⁡(\theta)+0.03` where :math:`\theta < 5.14`
  - :math:`S=16.8\cdot \sin⁡(\theta) - 0.50` ,where :math:`\thea \geq 5.14`

 * :math:`A_{i-in}` the contributing area (:math:`m^2`) at the inlet of a grid cell which is computed from the d-infinity flow direction method

 * :math:`D` the grid cell linear dimension (:math:`m`)

 * :math:`x_i=|sin \alpha_i| + |\cos \alpha_i|` where :math:`\alpha_i` is the aspect direction for grid cell :math:`i`

 * :math:`m` is the RUSLE length exponent factor.


To avoid overestimation of the LS factor in heterogeneous landscapes, long slope lengths are capped to a value of 333m (Desmet and Govers, 1996; Renard et al., 1997)

The value of :math:`m`, the length exponent of LS factor, is based on the classical USLE, as discussed in (Oliveira et al., 2013):

 * :math:`m = 0.2` for slope <= 1%: 
 * :math:`m = 0.3` for 1% < slope <= 3.5%
 * :math:`m = 0.4` for 3.5% < slope <= 5%
 * :math:`m = 0.5` for 5% < slope <= 9%
 * :math:`m = \beta / (1 + \beta)` where :math:`\beta=\sin\theta / 0.0986 / (3\sin (\theta(^0.8 + 0.56)) for slope >= 9%


Sediment Deliverty Ratio
""""""""""""""""""""""""



Table 1. Length exponent for the LS factor

+---+---------------------------+
| m   slope (%)
0.2 slope ≤ 1%
0.3 1% ≤ slope ≤ 3.5% 
0.4 3.5% ≤ slope ≤ 5%
0.5 5% ≤ slope ≤ 9%
β/(1+β)  ,where β=(sin⁡(θ)/0.0896))/(3〖sin⁡(θ)〗^0.8+0.56)   slope ≥ 9%



Example math:

.. math:: E^T \left(\frac{\partial^2 C}{\partial x^2} + \frac{\partial^2 C}{\partial y^2}\right) - \left(U\frac{\partial C}{\partial x} + V\frac{\partial C}{\partial y}\right) + S = 0
   :label: eq1

Reference to above equation: :eq:`eq1`

Where

 * :math:`x` and :math:`y` east and north coordinates, respectively 
 * :math:`C` tidal averaged concentration of a water quality state variable
 * :math:`U` and :math:`V` advective velocities (i.e., Eulerian residual current) in :math:`x` and :math:`y` directions, respectively
 * :math:`E^T` tidal dispersion coefficient
 * :math:`S` term to account for sources and sinks of pollutant

Table Example:

Table 1. Tidal dispersion coefficient (:math:`E^T`) in various estuarine systems (modified from Table 3.3 in Thomann & Mueller 1987).

+----------------------------------+----------------------------------------------------------------------+
| Estuaries                        | Tidal dispersion coefficient (:math:`\mathrm{km}^2\mathrm{day}^{-1}`)|
+==================================+======================================================================+
| Hudson River, NY                 | 52                                                                   |
+----------------------------------+----------------------------------------------------------------------+
| East River, NY                   | 26                                                                   |
+----------------------------------+----------------------------------------------------------------------+
| Wappinger and Fishkill Creek, NY | 1-3                                                                  |
+----------------------------------+----------------------------------------------------------------------+
| Delaware River, upper            | 5-18                                                                 |
+----------------------------------+----------------------------------------------------------------------+
| Delaware River, lower            | 18-28                                                                |
+----------------------------------+----------------------------------------------------------------------+
| San Francisco Bay, southern      | 2-16                                                                 |
+----------------------------------+----------------------------------------------------------------------+
| San Francisco Bay, northern      | 4-161                                                                |
+----------------------------------+----------------------------------------------------------------------+
| Rio Quayas, Ecuador              | 65                                                                   |
+----------------------------------+----------------------------------------------------------------------+
| Thames River, England, low flow  | 5-7                                                                  |
+----------------------------------+----------------------------------------------------------------------+
| Thames River, England, high flow | 28                                                                   |
+----------------------------------+----------------------------------------------------------------------+



Limitations and simplifications
===============================


Data Needs
==========

The following are the data needs for the Sediment Delivery Ratio Model.  The model is distributed with default arguments which are defaulted in the following parameters on the tool's first run.

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory.

 * **Results suffix (optional)**: This text will be appended to all the intermediate and output files.

 * **DEM Raster**: A digital elevantion model raster that is used for calculating the flow paths and hydrological connectivity across the landscape.

 * **Erosivity Raster**: A GIS raster dataset, with an erosivity index value for each cell. This variable depends on the intensity and duration of rainfall in the area of interest. The greater the intensity and duration of the rain storm, the higher the erosion potential. The erosivity index is widely used, but in case of its absence, there are methods and equations to help generate a grid using climatic data. The units are :math:`MJ*mm/(ha*h*yr)`.

 * **Erodability Raster**: This is a GIS raster dataset, with a soil erodibility value for each cell which is a measure of the susceptibility of soil particles to detachment and transport by rainfall and runoff.  Units are in :math:`T*ha*h/(ha*MJ*mm)`.

 * **LULC Raster**: A GIS raster dataset, with an integer LULC code for each cell.  These codes are referenced in the biophysical table input.

 * **Watershed Polygons**: This is a layer of watersheds such that each watershed contributes to a point of interest where water quality will be analyzed.  It must have the integer field 'ws_id' where the values uniquely identify each watershed.

 * **Biophysical Table**: A table containing model information corresponding to each of the land use classes in the LULC raster input. It must contain the fields 'lucode', 'usle_c', and 'usle_p'. ::

    * lucode: an integer code corresponding to a value in the LULC Raster input

    * usle_c: a number between 0 and 1 

    * usle_p: 

 * **Area of Interest (AOI)**: An ESRI Shapefile that contains a polygon indicating the target area. The output raster will align with the area of extents of this polygon. The polygon should be projected.

 * **Land Polygon**: An ESRI Shapefile that contains a polygon indicating where the landmass lies.  It should be in the same projection as the AOI polygon.

 * **Output pixel size in meters**: Horizontal grid size, which determines the output resolution of the pollutant density raster. A larger number will make the output grid coarser but the model will run faster, while a finer resolution will require more computation and memory. Try making this number larger if a model run encounters an out of memory error.

 * **Grid Cell Depth**: Grid size in a vertical direction (:math:`m`), which is the layer thickness of the horizontal grid system.

 * **Source Point Centroids**: An ESRI Shapefile that contains a point layer indicating the centroids of point pollutant sources that must have a field called Id that indicates the unique identification number for that point. This file must be in the same projection as the AOI polygon.

 * **Source Point Loading Table**: Point source loading (:math:`\mathrm{g\ day}^{-1}` or :math:`\mathrm{organism\ count\ day}^{-1}`) at the loading points that contains at least the headers ID and WPS which correspond to the identification number in the Source Point Centroids shapefile and the loading of pollutant at that point source.

 * **Decay Coefficient (KB)**: Decay rate in the unit of :math:`\mathrm{day}^{-1}`. Users may consult Table 2 or use Equation :eq:`eq6` to estimate :math:`K_B`.

 * **Dispersion Coefficients (** :math:`E^T` **):** An ESRI Shapefile that contains a point layer with a field named ``E_km2_day`` indicating the dispersion coefficient (:math:`\mathrm{km}^2\mathrm{day}^{-1}`) at that point as referenced in Equation :eq:`eq1`. This file must be in the same projection as the AOI polygon.  In a future release of this model this parameter will have :math:`x` and :math:`y` components.

 * **(Optional) Advection Vectors (UV as point data):** An ESRI Shapefile that contains a point layer with two fields named ``U_m_sec_`` and ``V_m_sec_`` which correspond to the U and V components (:math:`\mathrm{m\ s}^{-1}`) of the 2D advective velocity vector as referenced in Equation :eq:`eq1`. This file must be in the same projection as the AOI polygon.


Running the Model
=================

To run the marine water quality model double click *invest_marine_water_quality_biophysical.exe* located in the folder entitled *invest-3* in the InVEST installation directory. The main interface indicates the required and optional input arguments as described in the **Data Needs** section above.  Click the *Run* button to start the model.  A successful run will be indicated in the window and a file explorer will open containing the results.

If you encounter any issues please post to the user's support forum at http://ncp-yamato.stanford.edu/natcapforums.

Interpreting Results
====================

Model Outputs
-------------

Each of model output files is saved in the ``Output`` and ``Intermediate`` folders that are saved within the user-specified workspace.

**Output folder**

 * ``Output\concentration.tif``: The output raster indicating the concentration of the water quality state variable (e.g. pollutant). The units of the loading determine the units of output concentration. If the loading is expressed as the number (mass) of a targeted organism, the concentration unit is the number of organisms (mass) per volume.

**Intermediate folder**

 * ``Intermediate\in_water.tif``: This is a raster file indicating the land and water points that’s used in the calculation of the domain to discritize Equation :eq:`eq1`.

 * ``Intermediate\tide_e.tif``: This is a raster file with the interpolated values of the Tidal Dispersion Coefficients shapefile that are used to determine the ET values for each discritized grid cell.

 * ``Intermediate\adv_u.tif`` and ``intermediate\adv_v.tif``: This is a raster with the interpolated values of the Advection Vectors (:math:`UV` as point data) shapefile that are used to determine the :math:`U` and :math:`V` components respectively.


Case example illustrating model inputs and results
==================================================

Managers and stakeholders want to estimate the distribution of fecal-coliform bacteria released from floathomes (recreational floating cabins, usually with untreated wastes) in sheltered areas along the west coast of Vancouver Island, BC, Canada. We have explored scenarios involving different levels of treatment (removal of fecal-coliform and thus a decreased loading) and different spatial arrangements of floathomes. Figs. 1  and 2 show a status quo arrangement of floathomes in Lemmens Inlet (and, in the case of Fig. 1, the surrounding area). We used an initial assumption that the loading of the untreated wastes from the floathomes of 1 million bacteria per day. In another scenario assumption, we modeled the effects of secondary treatment of waste from two floathomes (the 23rd and 24th in Fig. 2), assuming 95% removal (thus the initial loading is 50,000 bacteria per day). Model results, i.e. the distribution of fecal-coliform bacteria given the location of floathomes shown in Fig. 2 and the modeled treatment of waste described above, are shown in Fig. 3.

 .. image:: marine_water_quality_images/fig_1.png
    :width: 450px

Figure 1. A map of Clayoquot Sound, BC, Canada showing a status quo arrangement of floathomes (red dots). The dotted box indicates Lemmens Inlet, the region of interest for potentially rearranging floathomes and/or exploring the effects of treating wastes. Background colors indicate tidal dispersion coefficients for the region, a key model input.

 .. image:: marine_water_quality_images/fig_2.png
    :width: 450px
    :align: center


Figure 2. Enlarged map of Lemmens Inlet, showing the location of floathomes. Source point centroids are shown with red x’s and red circles indicate treated wastes (23 and 24) assuming 95% removal of bacteria.

 .. image:: marine_water_quality_images/fig_3.png
    :width: 450px
    :align: center

Figure 3. Map of modeled concentration of fecal coliform bacteria in Lemmens Inlet. Red circles indicate treated wastes. The results are for demonstration purposes only.

References
==========

Park, K. 1996. Concept of surface water quality modeling in tidal rivers and estuaries. Environ. Eng. Res.
1:1-13.

MacCready, P., and W. R. Geyer 2010. Advances in estuarine physics. The Annual Review of Marine
Science 2:35-58.

Thomann, R. V., and J. A. Mueller. 1987. Principles of surface water quality modeling and control.
Prentice-Hall, NY.

Ji Z-G (2008) Hydrodynamics and water quality: Modeling rivers, lakes, and estuaries. New Jersey: John Wiley & Sons, Inc.

..  LocalWords:  InVEST advection nabla cdot mathbf eq advective mathrm AOI csv
..  LocalWords:  ESRI Shapefile WPS shapefile kh biogeochemical se floathomes
..  LocalWords:  eutrophication frac UC VC Eulerian MacCready Geyer Thomann eqx
..  LocalWords:  Wappinger Fishkill northerns Quayas advected Nicolson coli kx
..  LocalWords:  coliforms enterococci coliform Indictor Stormwater lookup exe
..  LocalWords:  resuspension tif discritize discritized quo Lemmens th px
..  LocalWords:  Clayoquot Maccready
