.. _marine-water-quality:

**************************
Marine Water Quality Model
**************************

Summary
=======

Management of water quality plays a critical role in human and ecosystem health in coastal and estuarine ecosystems. The lack of a predictive understanding of the dispersal and fate of contaminants is a major obstacle to the development of management strategies for water quality problems. We developed a marine water quality model consisting of physical transport and biogeochemical processes to simulate the dispersal of water quality state variables (e.g. contaminants) in response to changes in ecosystem structure driven by various management decisions and human activities. Hence, this model assesses how management and human activities influence the water quality in coastal and estuarine ecosystems. Although water quality is not an environmental service per se, the InVEST marine water quality model can be linked with other InVEST models to evaluate how changes in water quality might affect environmental services related to fisheries, aquaculture and recreation and how the exploitation of some services (e.g. aquaculture) might in turn affect water quality.


Introduction
============

The discharge of contaminants resulting from various management decisions and human activities may cause many types of water quality problems and potentially pose serious risks to both aquatic ecosystems and human health. Therefore, as human activities increase in coastal and marine ecosystems, water quality management has received increased attention in recent years. Since many processes (physical transport, biogeochemical and anthropogenic processes, etc.) affect water quality, it is difficult to determine the source of and to predict water quality problems. A numerical model based on physical and biogeochemical principals can help managers and decision makers investigate various water quality problems such as high concentrations of bacteria and toxic chemicals, hypoxia, and eutrophication (Park 1996). 

Contaminants introduced into an estuarine system are transported by water movement (i.e. physical transport) and, while being transported, their concentrations are modified by biogeochemical processes. Therefore physical and biogeochemical processes combine to determine the fate of the contaminants. We developed a marine water quality model that accounts for both physical transport and biogeochemical processes to simulate the distribution and fate of a water quality state variable (e.g. contaminant or pollutant) in a coastal and estuarine system. The model allows users to change contaminant loadings from various sources, which may include sewage treatment plants, urban runoffs, storm sewers, failing septic systems, industrial discharges, floathomes, and aquaculture farms. For example, to explore the effects of alternate management schemes, users can alter pollutant or nutrient loading by adding, removing, or changing practices at aquaculture farms. They can also define pollutant or nutrient loading due to land based management. 

The main output of the marine water quality model is a map of the concentration of a water quality state variable in response to the various management decisions under consideration. By exploring the concentration maps, users can assess—in a spatially explicit manner—how management and development strategies influence the water quality in their target area. The marine water quality model can be linked with other InVEST models to evaluate other ecosystem services related to fisheries, aquaculture, habitat quality, and recreation.

The model
=========

How it works
------------

The marine water quality model calculates the spatial distribution of water quality state variables by solving a tidal-average mass-balance equation (horizontal two-dimension).

.. math:: \frac{\partial C}{\partial t} = - \frac{\partial (UC)}{\partial x}-\frac{\partial (VC)}{\partial y}+\frac{\partial D^T_x}{\partial x}\frac{\partial C}{\partial x} + \frac{\partial E^t_y}{\partial y}\frac{\partial C}{\partial y}+S_I+S_E
   :label: eq1

Where

 * :math:`t` time 
 * :math:`x` and :math:`y` east and north coordinates, respectively 
 * :math:`C` tidal averaged concentration of a water quality state variable
 * :math:`U` and :math:`V` advective velocities (i.e., Eulerian residual current) in math:`x` and :math:`y` directions, respectively
 * :math:`E^T_x` and :math:`E^T_y` tidal dispersion coefficient in :math:`x` and :math:`y` directions, respectively
 * :math:`S_I` internal sources and sinks 
 * :math:`S_E` external and sources and sinks 

The first term in Eq. :eq:`eq1` indicates the time rate change in the concentration of a water quality state variable. We assume a steady state condition for the current version of the model so this term becomes zero. The first two terms on the right hand side represent advective transport and the following two terms indicate tidal dispersion. The advective transport accounts for mass transport due to Eulerian residual current, which is obtained by averaging velocities at a fixed point over one or more tidal cycles. The tidal dispersion accounts for the dispersion of mass due to correlation between tidal components of velocity and concentration and for the diffusion due to the turbulent fluctuations in velocity and concentration (MacCready & Geyer 2010). The tidal dispersion coefficient may be estimated by using observed salinity distribution or dye experiments. The observed tidal dispersion coefficient shows large variation ranging from 1 to 161 :math:`\mathrm{km}^2\mathrm{day}^{-1}` (Table 1) (Thomann & Mueller 1987).

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
| San Francisco Bay, northerns     | 4-161                                                                |
+----------------------------------+----------------------------------------------------------------------+
| Rio Quayas, Ecuador              | 65                                                                   |
+----------------------------------+----------------------------------------------------------------------+
| Thames River, England, low flow  | 5-7                                                                  |
+----------------------------------+----------------------------------------------------------------------+
| Thames River, England, high flow | 28                                                                   |
+----------------------------------+----------------------------------------------------------------------+

Tidal dispersion coefficient may also be parameterized as a function of tidal flow and length scale of an estuarine system (MacCready & Geyer 2010).

.. math::  E^T = 0.035 U_T B
   :label: eq2

where

 * :math:`U_T` amplitude of depth-averaged tidal flow

 * :math:`B` the length scale of an estuarine system, which is the smaller of channel width or tidal
excursion.

If users have tidal flow information, Eq. :eq:`eq2` is a practical option to estimate spatially explicit tidal dispersion coefficient in their study area. Advective transport and tidal dispersion combine to determine physical transport of a water quality state variable. Physical transport processes take the same mathematical forms for all water quality state variables. That is, physical transport processes do not depend on the nature of the substances as long as the substances do not affect the water movement.

The last two terms in Eq. :eq:`eq1` represent material-specific biogeochemical processes consisting of internal sources/sinks (SI) and external sources/sinks (SE). SI is primarily due to the kinetic processes and SE includes pollutant loading into and removal from a water body. Different water quality state variables are affected by different biogeochemical processes and require appropriate kinetic formulations for each of the source and sink terms (Park 1996).

Boundary Condition
------------------

We need to define ocean and land boundary conditions to solve Eq. :eq:`eq1` numerically. The ocean boundary (i.e., open boundary) indicates the outer boundary of the modeling domain adjacent to oceans. We assume the horizontal pollutant profile (e.g. C) is advected out of the modeling domain as a “frozen pattern”. That is

.. math::  \frac{\partial C}{\partial x} = 0 \mathrm{\ on\ the\ left/right\ boundaries}
   :label: eq3

.. math::  \frac{\partial C}{\partial y} = 0 \mathrm{\ on\ the\ top/bottom\ boundaries}
   :label: eq4

Additionally, no transport of :math:`C` is allowed from or into the land.

Numerical Solution
------------------

RICH FILL IN

Biogeochemical Processes
------------------------

Unlike physical transport processes, each water quality state variable is determined by different biogeochemical processes and requires appropriate kinetic formulations (Park 1996). The kinetic formulations are mostly empirical and thus have to be refined with the advances in our understanding of the representing kinetic processes. The InVEST marine water quality model provides users a flexible framework to update or add biogeochemical processes for their target materials. An example of biogeochemical processes for pathogen simulation is given below.

Pathogens
^^^^^^^^^

Pathogens are disease-causing microorganisms that include bacteria, viruses, and protozoa, and can originate from many sources including sewage treatment plants, urban runoff, storm sewers, failing septic systems, industrial discharges, and contaminated sediments. Contaminated water by pathogens is responsible for the spread of many contagious diseases, and understanding the dispersal and fate of pathogens is one of main concerns for water quality management. The studies of pathogens in surface water usually focus on indicator organisms such as fecal coliforms, E. coli or enterococci, and often consider a simple decay for the biogeochemical processes (Thomann & Mueller 1987):

.. math:: S_l+S_E = K_B C + \frac{W}{VOL}
   :label: eq5

where

 * :math:`C` concentration of indicator organism (:math:`\mathrm{organism\ count}/\mathrm{m}^{-3}`)

 * :math:`K_B` decay rate (:math:`\mathrm{day}^{-1}`)

 * :math:`W` external load of indicator organism (organism :math:`\mathrm{count/day}^{-1}`)

 * :math:`VOL` volume of water cell (:math:`\mathrm{m}^3`)

As shown in Table 2, the average decay rate of total coliform bacteria is about 1.4 :math:`\mathrm{day}^{-1}` in freshwater (20C) and 48 :math:`\mathrm{day}^{-1}` in seawater, but the maximum decay rate can be as large as 84 :math:`\mathrm{day}^{-1}` under optimal environmental conditions.

Table 2. Observed decay rates of indicator organisms (Modified from Table 5.9 in Thomann & Mueller 1987).

+--------------------+---------------------------------+----------------------------------------------+
| Indictor organisms | :math:`K_B (\mathrm{day}^{-1}`) | Note                                         |
+====================+=================================+==============================================+
| Total coliform     | 0.7-3.0 (avg. 1.4)              | Average freshwater (20C)                     |
+--------------------+---------------------------------+----------------------------------------------+
|                    | 8.0-84.0 (avg. 48.0)            | Seawater (20C) (variable temperature)        |
+--------------------+---------------------------------+----------------------------------------------+
| Total or fecal     | 0.0-2.4                         | New York Harbor Salinity: 2-18 0/00 (dark)   |
+--------------------+---------------------------------+----------------------------------------------+
|                    | 2.5-6.1                         | New York Harbor Salinity: 15 0/00 (sunlight) |
+--------------------+---------------------------------+----------------------------------------------+
| Fecal coliform     | 37.0-110.0                      | Seawater (sunlight)                          |
+--------------------+---------------------------------+----------------------------------------------+
| E-Coli             | 0.08-2.0                        | Seawater, 10-30 0/00                         |
+--------------------+---------------------------------+----------------------------------------------+
| Salmonella         | 0.1 - 3.0                       | Stormwater (20C), Hamilton Bay (18C)         |
+--------------------+---------------------------------+----------------------------------------------+


Mancini (1978) made an equation to estimate decay rates of indicator bacteria as a function of salinity, temperature, sunlight and sink/resuspension.  

.. math:: K_B = [0.8 + 0.006(\% \mathrm{\ sea\ water})] 1.07^{(T-20)} + \frac{\alpha I_0}{K_e H} [1 - exp(-K_e H)]\pm \frac{v_s}{H}
   :label: eq6

Where

 * :math:`T` water temperature (C)
 * :math:`\alpha` sunlight coefficient
 * :math:`I_0` average solar radiaton (:math:`\mathrm{cal\ cm}^{-2}`)
 * :math:`K_e` light extinction coefficient (:math:`m^{-1}`)
 * :math:`H` average depth (:math:`m`)
 * :math:`v_s` sink or resuspension rate (:math:`m \mathrm{day}^{-1}`)

Users may use Table 2 as a lookup table to find an appropriate :math:`K_B` for their application. If users have enough data for the environmental conditions (water temperature, salinity, light information, etc.), Eq. :eq:`eq6` may be applied to estimate :math:`K_B`. 


This model predicts concentration of a pollutant by solving the steady state diffusion advection equation

.. math::   \nabla\cdot \mathbf{E}\nabla s - \mathbf{U} \nabla s - Ks = 0
   :label: eqx

Where 

 * :math:`E` is the tidal dispersion coefficient in units of :math:`km^2/day`
 * :math:`U` is a two dimensional vector of advective velocity in units of :math:`m/sec`
 * :math:`K` is the decay rate of the pollutant in units of :math:`\mathrm{day}^{-1}`
 * :math:`s` is the loading of the pollutant in units of
   :math:`kg/m^3`

Limitations and simplifications
===============================

1. **Assumes a steady state condition (no time variation of model results)**: The current version assumes a steady state condition and cannot produce time varying model outputs. So, users should be aware that the model produces a distribution of a water quality state variable once it reaches an equilibrium status under defined conditions.      

2. **Grid size of a water cell**: A finer grid size better resolves spatial differences in model outputs. However, it requires more computation and memory. Too many grid cells may cause an out of memory error.

3. **The quality of physical transport**: Reliable information on physical transport processes is critical for reasonable model results. 

4. **No vertical transport**: The governing mass balance equation of the model considers only horizontal transport of mass; it assumes no vertical transport. 

5. **Size of the modeling domain**: If the ocean boundary is too close to the pollutant loading points, inaccurate boundary values may artificially affect the model results. We therefore recommend users to prepare the grid system such that the ocean boundary is not too close to the loading locations.  

Data Needs
==========

The following are the data needs for the Marine Water Quality Model.  This model ships with default arguments which are defaulted in on the tool's first run.

 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory.

 * **Area of Interest (AOI)**: An ESRI Shapefile that contains a polygon indicating the target area. The output raster will align with the area of extents of this polygon. The polygon itself should be projected.

 * **Land Polygon**: An ESRI Shapefile that contains a polygon indicating where the landmass lies.  It should be in the same projection as the AOI polygon.

 * **Output pixel size in meters**: Horizontal grid size, which determines the output resolution of the pollutant density raster. A larger number will make the output grid coarser but the model will run faster, while a finer resolution will require more computation and memory. Try making this number larger if a model run causes an out of memory error.

 * **Grid Cell Depth**: Grid size in a vertical direction :math:`m`, which is the layer thickness of the horizontal grid system.

 * **Source Point Centroids**: An ESRI Shapefile that contains a point layer indicating the centroids of point pollutant sources that must have a field called Id that indicates the unique identification number for that point. This file must be in the same projection as the AOI polygon.

 * **Source Point Loading Table**: Point source loading (:math:`\mathrm{g\ day}^{-1}` or :math:`\mathrm{organism\ # day-1) at the loading points that contains at least the headers ID and WPS which correspond to the identification number in the Source Point Centroids shapefile and the loading of pollutant at that point source.

 * **Decay Coefficient (KB)**: Decay rate in the unit of :math:`\mathrm{day}^{-1}`. Users may consult Table 2 or use Eq. :eq:`eq6` to estimate :math:`K_B`.

 * **Dispersion Coefficients (:math:`E^T_x` and :math:`E^T_y`):** An ESRI Shapefile that contains a point layer with a field named kx_km2_day indicating the dispersion coefficients (:math:`\mathrm{km}^2\mathrm{day}^{-1}`) at that point as referenced in Equation :eq:`eq1`. The current model assumes thatare the same and requires only one of them. This file must be in the same projection as the AOI polygon.

 * **(Optional) Advection Vectors (UV as point data):** An ESRI Shapefile that contains a point layer with two fields named *U_m_sec_* and *V_m_sec_* which correspond to the U and V components (:math:`\mathrm{m}/\mathrm{s}`) of the 2D advective velocity vector as referenced in Equation :eq:`eq1`. This file must be in the same projection as the AOI polygon.

Data inputs
===========

The following inputs are required to run the marine water quality model:

* **Output pixel size in meters** this parameter is used to determine the output resolution of the pollutant density raster.  A larger number will make the output grid coarser but the model will run faster, while a finer resolution will require more computation and memory.  Try making this number larger if a model run causes an out of memory error.

* **Workspace** The directory to hold output and intermediate results of the particular model run.  After the model is complete the output will be located in this directory.

* **Absorption Coefficient (K)** The decay rate as described in Equation :eq:`eqx`.

* **Area of Interest (AOI)** An ESRI Shapefile that contains a polygon indicating the area at which the solution should be run.  The output raster will align with the area of extents of this polygon.  The polygon itself should be projected into meters.

* **Land Polygon** An ESRI Shapefile that contains a polygon indicating where the landmass lies.

* **Source Point Centroids** An ESRI Shapefile that contains a point layer indicating the centroids of point pollutant sources that must have a field called ``Id`` that indicates the unique identification number for that point.  This file must be in the same projection as the *AOI* polygon.

* **Source Point Data Table** A csv table that contains at least the headers ``ID`` and ``WPS`` which correspond to the identification number in the *Source Point Centroids* shapefile and the amount of loading of pollutant that point source in terms of kilograms per day.

* **Tidal Diffusion Constants** An ESRI Shapefile that contains a point layer with a field named ``kh_km2_day`` indicating the tidal dispersion coefficient at that point as referenced in Equation :eq:`eqx`.  This file must be in the same projection as the *AOI* polygon.

* **Advection Vectors (UV as point data)** An ESRI Shapefile that contains a point layer with two fields named `U_m_sec_` and `V_m_sec_` which correspond to the *u* and *v* components of the 2D advective velocity vector *U* as referenced in Equation :eq:`eqx`.  This file must be in the same projection as the *AOI* polygon.

Running the Model
=================

To run the marine water quality model double click *invest_marine_water_quality_biophysical.exe* located in the folder entitled *invest-3* in the InVEST installation directory. The main interface indicates the required and optional input arguments as described in the **Data Inputs** section above.  Click the *Run* button to start the model.  A successful run will be indicated in the window and a file explorer will open containing the results.

If you encounter any errors please email the log to the lead software developer at richsharp@stanford.edu.

Interpreting Results
====================

Model Outputs
-------------

Each of model output files is saved in the ``Output`` and ``Intermediate`` folders that are saved within the user-specified workspace.

**Output folder**

 * ``Output\\concentration.tif``: The output raster indicating the concentration of the water quality state variable (e.g. pollutant). The units of the loading determine the units of output concentration. If the loading is expressed as the number (g) of a targeted organism, the concentration unit is the number of organisms (g) per volume.

**Intermediate folder**

 * ``Intermediate\\in_water.tif``: This is a raster file indicating the land and water points that’s used in the calculation of the domain to discritize Equation :eq:`eq1`.

 * ``Intermediate\\tide_e.tif``: This is a raster file with the interpolated values of the Tidal Dispersion Coefficients shapefile that are used to determine the ET values for each discritized grid cell.

 * ``Intermediate\\adv_u.tif`` and ``intermediate\\adv_v.tif``: This is a raster with the interpolated values of the Advection Vectors (:math:`UV` as point data) shapefile that are used to determine the :math:`U` and :math:`V` components respectively.


Case example illustrating model inputs and results
==================================================

Managers and stakeholders want to estimate the distribution of fecal-coliform bacteria released from floathomes (recreational floating cabins, usually with untreated wastes) in sheltered areas along the west coast of Vancouver Island, BC, Canada. We have explored scenarios involving different levels of treatment (removal of fecal-coliform and thus a decreased loading) and different spatial arrangements of floathomes. Figures :ref:`figure1` and :ref:`figure2` show a status quo arrangement of floathomes in Lemmens Inlet (and, in the case of Fig. :ref:`figure3`, the surrounding area). We used an initial assumption that the loading of the untreated wastes from the floathomes of 1 million bacteria per day. In another scenario assumption, we modeled the effects of secondary treatment of waste from two floathomes (the 23rd and 24th in Fig. :ref:`figure2`), assuming 95% removal (thus the initial loading is 50,000 bacteria per day). Model results, i.e. the distribution of fecal-coliform bacteria given the location of floathomes shown in Fig. :ref:`figure2` and the modeled treatment of waste described above, are shown in Fig. :ref:`figure3`.

 .. _figure1:

 .. figure:: marine_water_quality_images/fig_1.png
    :width: 400px

    A map of Clayoquot Sound, BC, Canada showing a status quo arrangement of floathomes (red dots). The dotted box indicates Lemmens Inlet, the region of interest for potentially rearranging floathomes and/or exploring the effects of treating wastes. Background colors indicate tidal dispersion coefficients for the region, a key model input.

 .. _figure2:

 .. figure:: marine_water_quality_images/fig_2.png
    :width: 400px

    Enlarged map of Lemmens Inlet, showing the location of floathomes. Source point centroids are shown with red x’s and red circles indicate treated wastes (23 and 24) assuming 95% removal of bacteria.

 .. _figure3:

 .. figure:: marine_water_quality_images/fig_3.png
    :width: 400px

    Map of modeled concentration of fecal coliform bacteria in Lemmens Inlet. Red circles indicate treated wastes. The results are for demonstration purposes only.

References
==========

Maccready, P., and W. R. Geyer 2010. Advances in estuarine physics. The Annual Review of Marine
Science 2:35-58.

Park, K. 1996. Concept of surface water quality modeling in tidal rivers and estuaries. Environ. Eng. Res.
1:1-13.

Thomann, R. V., and J. A. Mueller. 1987. Principles of surface water quality modeling and control.
Prentice-Hall, NY.


Outputs
=======

All the outputs below are relative to the workspace path specified in the input of the model.

* ``intermediate/in_water.tif`` a raster indicating the land and water points that's used in the calculation of the domain to discritize Equation :eq:`eqx`.

* ``intermediate/tide_e.tif`` a raster with the interpolated values of the *Tidal Diffusion Constants* shapefile that are used to determine the E values for each discritized grid cell.

* ``intermediate/adv_u.tif`` and ``intermediate/adv_v.tif`` a raster with the interpolated values of the *Advection Vectors (UV as point data)* shapefile that are used to determine the *u* and *v* components respectively.

* ``output/concentration.tif`` the output raster indicating the concentration of the pollutant in terms of :math:`\mathrm{kg/m^3}`.

..  LocalWords:  InVEST advection nabla cdot mathbf eq advective mathrm AOI csv
..  LocalWords:  ESRI Shapefile WPS shapefile kh
