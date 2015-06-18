.. _ndr:

*************************************************
(under development) Nutrient Delivery Ratio model
*************************************************

Summary
=======

The objective of the InVEST nutrient delivery model is to map nutrient sources and their transport to the stream. This spatial information can be used to assess the service of nutrient retention by natural vegetation. The retention service is of particular interest for surface water quality issues and can be valued in economic or social terms (e.g. avoided treatment costs, improved water security through access to clean drinking water).

The main differences between the NDR model and the InVEST v3.1 Nutrient retention model are:
-   The routing of nutrient from a pixel to the stream was modified to reduce the sensitivity to grid resolution and facilitate the selection of LULC-specific retention coefficient;
-   It is possible to calibrate the model based on one (non-physical) parameter; it preserves the spatial distribution of nutrient sinks and sources, increasing confidence in spatially explicit outputs;
-   The flexible model structure allows advanced users to represent more complex processes such as direct nutrient discharges, or instream retention (work in progress)


Introduction
============

Land use change, and in particular the conversion to agricultural lands, dramatically modifies the natural nutrient cycle. Anthropogenic nutrient sources include point sources, e.g. industrial effluent or water treatment plant discharges, and non-point sources, e.g. fertilizer used in agriculture and residential areas. When it rains or snows, water flows over the landscape carrying pollutants from these surfaces into streams, rivers, lakes, and the ocean. This has consequences for people, directly affecting their health or well-being (Keeler et al., 2012), and for aquatic ecosystems that have a limited capacity to adapt to these nutrient loads.

One way to reduce non-point source pollution is to reduce the amount of anthropogenic inputs (i.e. fertilizer management). When this option fails, ecosystems can provide a purification service by retaining or degrading pollutants before they enter the stream. For instance, vegetation can remove pollutants by storing them in tissue or releasing them back to the environment in another form. Soils can also store and trap some soluble pollutants. Wetlands can slow flow long enough for pollutants to be taken up by vegetation. Riparian vegetation is particularly important in this regard, often serving as a last barrier before pollutants enter a stream.

Land-use planners from government agencies to environmental groups need information regarding the contribution of ecosystems to mitigating water pollution. Specifically, they require spatial information on nutrient export and areas with highest filtration. The nutrient delivery and retention model provides this information for non-point source pollutants. The model was designed for nutrients (nitrogen and phosphorous), but its structure can be used for other contaminants (persistent organics, pathogens etc.) if data are available on the loading rates and filtration rates of the pollutant of interest.


The Model
=========

Overview
--------

Sources of nutrient, also called nutrient loads, are first determined based on the LULC map. Nutrient loads can then be divided into sediment-bound and dissolved parts, which will be transported through surface and subsurface flow, respectively. Note that this step is optional; the user can choose to model surface flow only. In a second step, transport factors are computed for each pixel based on the properties of pixels belonging to the same flow path (in particular their slope and retention efficiency of the land use). At the watershed/subwatershed outlet, the nutrient export is computed as the sum of the pixel's contributions.

.. figure:: ./ndr_images/figure1.png

Figure 1: Conceptual representation of the NDR model. Each pixel i is characterized by its nutrient load, loadi, and its nutrient delivery ratio (NDR), a function of the upslope area, and downslope flow path (in particular the retention efficiencies of LULC types on the downslope flow path). The sediment export at the watershed level is computed the sum of pixel's nutrient exports.

Nutrient Loads
--------------

Loads are associated to LULC types, and can be divided into sediment-bound and dissolved nutrient portions. Conceptually, the former represents nutrients that are transported by surface runoff, while the latter represent nutrients transported by subsurface flow. The ratio between these two types of nutrient sources is given by the parameter *proportion_subsurface_x* (where x=n or x=p, for nitrogen or phosphorus, respectively), which quantifies the ratio of dissolved nutrients over the total amount of nutrients.

.. math:: load_{surf,i} = (1-proportion\_subsurface_i) \cdot x\_load_i

.. math:: load_{subsurf,i} = (1 - proportion\_subsurface_i) \cdot x\_load_i

In case no information is available on the partitioning between the two types, the recommended default value of *load\_subsurface\_x* is 0 (all nutrients are reaching the stream via surface or shallow subsurface flow).

Nutrient Transport
------------------

Nutrient transport is based on the concept of nutrient delivery ratio (NDR), an approach inspired by the peer-reviewed concept of sediment delivery ratio (see InVEST sediment model user's guide and Vigiak et al., 2012). The concept is similar to the risk-based index approaches that are popular for nutrient modeling (Drewry et al., 2011), although it provides quantitative values of sediment export (e.g. the proportion of the nutrient load that will reach the stream). Two delivery ratios are computed, one for nutrient transported by surface flow, the other for subsurface flow.

Surface NDR
^^^^^^^^^^^

The surface NDR is the product of the minimum nutrient delivery, :math:`NDR_{min}`, representing the ability of downstream pixels to transport nutrient without retention, and a topographic index IC, representing the position on the landscape. For a pixel i:

.. math:: NDR_i = NDR_{min,i}\left(1 + \exp\left(\frac{IC_i-ICi}{k}\right)\right)^{-1}

where :math:`IC_0` and :math:`k` are calibration parameters explained below.

:math:`NDR_{min,i}` is based based on the maximum retention efficiency of the land between a pixel and the stream (downslope path, in Figure 1):

.. math:: NDR_{min,i} = 1 - eff'_i

Moving along a flow path, the algorithm computes the additional retention provided by each pixel, taking into account the total distance traveled across each LULC type. Each additional pixel from the same LULC type will contribute a smaller value to the total retention, until the maximum retention efficiency for the given LULC is reached (Figure 2). The total retention is capped by the maximum retention value that LULC types along the flow path can provide, :math:`eff_{LULC_i}`.

In mathematical terms:

.. math:: eff'_i =
    \begin{cases}
        eff_{LULC_i}\cdot(1-s_i) & \mathrm{if\ } down_i \mathrm{\ is\ a\ stream\ pixel}\\
        eff'_{down_i}\cdot s_i + eff_{LULC_i}\cdot (1 - s_i) & \mathrm{if\ } eff_{LULC_i} > eff'_{down_i}\\
        eff'_{down_i} & otherwise
    \end{cases}

Where:

 * :math:`eff'_{down_i}` is the effective downstream retention on the pixel directly downstream from :math:`i`,
 * :math:`eff_{LULC_i}` is the maximum retention efficiency that LULC type :math:`i` can reach, and
 * :math:`s_i` is the step factor defined as: :math:`s_i=\exp\left(\frac{-5 \ell_{i_{down}}}{\ell_{LULC_i}}\right)`

With:

 * :math:`\ell_{i_{down}}` is the length of the flow path from pixel :math:`i` to its downstream neighbor
 * :math:`\ell_{LULC_i}` is the LULC critical length of the landcover type on pixel :math:`i`

Notes:

Since :math:`eff'_i` is dependent on the pixels downstream, calculation proceeds recursively starting at pixels that flow directly into streams before upstream pixels can be calculated.

In equation [4], the factor 5 is based on the assumption that maximum efficiency is reached when 99% of its value is reached (assumption due to the exponential form of the efficiency function, which implies that the maximum value cannot be reached with a finite flow path length).

.. figure:: ./ndr_images/figure2.png

Figure 2: Illustration of the calculation of the retention efficiency along a simple flow path composed of 4 pixels of grass and 3 pixels of forest. Each additional pixel of the grass LULC contributes to a smaller percentage toward the maximum efficiency provided by grass. The shape of the exponential curves is determined by the maximum efficiency and the critical length.

IC, the index of connectivity, represents the hydrological connectivity, i.e. how likely nutrient on a pixel is likely to reach the stream. In this model, IC is a function of topography only (Figure 3):

.. math:: IC=\log_{10}\left(\frac{D_{up}}{D_{dn}}\right)

where

 * :math:`D_{up} = \overline{S}\sqrt{A}` and,
 * :math:`D_{dn} = \sum_i \frac{d_i}{S_i}`

The default values of :math:`IC_0` and :math:`k` are set to :math:`IC_0 = \frac{IC_{max}+IC_{min}}{2}` and :math:`k=2`, respectively.

This imposes that the sigmoid function relating NDR to IC is centered on the median of the IC distribution, hence that the maximum IC value gives :math:`NDR=NDR_{max}`. :math:`k` is set to a default value of 2 (cf. SDR model theory); it is an empirical factor that represents local topography.

.. figure:: ./ndr_images/figure3.png

 Figure 3: Relationship between NDR and the connectivity index IC. The maximum value of NDR is set to :math:`NDR_{min}=0.8`. The effect of the calibration is illustrated by setting :math:`k_b=1` and :math:`k_b=2` (solid and dashed line, respectively), and :math:`IC_0=0.5` and :math:`IC_0=2` (black and gray dashed lines, respectively).

Subsurface NDR
^^^^^^^^^^^^^^

The expression for the subsurface NDR is a simple exponential decay with distance to stream, plateauing at the value corresponding to the user-defined maximum subsurface nutrient retention:

.. math:: NDR_{subs,i} = 1 - eff_{subs}\left(1-e^\frac{-5\cdot\ell}{\ell_{subs}}\right)

where

 * :math:`eff_{subs}` is the maximum nutrient retention efficiency that can be reached through subsurface flow (i.e. retention due to biochemical degradation in soils),

 * :math:`\ell_{subs}` is the subsurface flow critical length, i.e. the distance after which it can be assumed that soil retains nutrient at its maximum capacity,

 * :math:`\ell_i` is the distance from the pixel to the stream.


Nutrient Transport
------------------

Nutrient export from each pixel i is calculated as the product of the load and the NDR:

.. math:: x_{exp_i} = load_{surf,i} \cdot NDR_{surf,i} + load_{subs,i} \cdot NDR_{subs,i}

Total nutrient at the outlet is the sum of the contributions from all the pixels:

.. math:: x_{exp_{tot}} = \sum_i x_{exp_i}


Limitations
-----------

The model has a small number of parameters and outputs generally show a high sensitivity to inputs. This implies that errors in the empirical load parameter values will have a large effect on predictions. Similarly, the retention efficiency values are based on empirical studies, and factors affecting these values (like slope or intra-annual variability) are averaged. These values implicitly incorporate information about the dominant nutrient dynamics, influenced by climate and soils. Finally, the effect of grid resolution on the NDR formulation has not been well studied.

Sensitivity analyses are recommended to investigate how the confidence intervals in input parameters affect the study conclusions (Hamel et al., 2015).

Also see the "Biophysical model interpretation" section for further details on model uncertainties.


Options for Valuation
---------------------

Nutrient export predictions can be used for quantitative valuation of the nutrient retention service. For example, scenario comparison can serve to evaluate the change in purification service between landscapes. The total nutrient load can be used as a reference point, assuming that the landscape has 0 retention. Comparing the current scenario export to the total nutrient load provides a quantitative measure of the retention service of the current landscape.

Data Needs
----------

This section outlines the data used by the model. Refer to the appendix for detailed information on data sources and pre-processing. For all raster inputs, the projection should be defined and the projection's linear units should be in meters.

1.  **Digital elevation model** (DEM) (required). A GIS raster dataset, with an elevation value for each cell. Make sure the DEM is corrected by filling in sinks. To ensure proper flow routing, the DEM should extend beyond the watersheds of interest, rather than being clipped to the watershed boundaries. See the Working with the DEM section of this manual for more information.

2.  **Land use/land cover** (required). A GIS raster dataset, with an integer LULC code for each pixel. The LULC code should be an integer.

3.  **Watersheds** (required). A shapefile of polygons. This is a layer of watersheds such that each watershed contributes to a point of interest where water quality will be analyzed. See the Working with the DEM section for information on creating watersheds.

4.  **Biophysical Table** (required). A .csv table of land use/land cover (LULC) classes, containing data on water quality coefficients used in this tool. These data are attributes of each LULC class rather than attributes of individual cells in the raster map. Each row in the table is an LULC class while each column contains a different attribute of each land use/land cover class. The columns must be named as:

  * *lucode* (Land use code): Unique integer for each LULC class (e.g., 1 for forest, 3 for grassland, etc.), must match the LULC raster above.
  * *LULC_desc*: Descriptive name of land use/land cover class (optional)
  * *load_n* (and/or load_p): The nutrient loading for each land use, given as decimal values with units of kg. ha-1 yr -1. Suffix _n stands for nitrogen, and _p for phosphorus, and the two compounds can be modeled at the same time or separately.
  * *eff_n* (and/or eff_p): The maximum retention efficiency for each LULC class, varying between zero and 1. The nutrient retention capacity for a given vegetation is expressed as a proportion of the amount of nutrient from upstream. For example, high values (0.6 to 0.8) may be assigned to all natural vegetation types (such as forests, natural pastures, wetlands, or prairie), indicating that 60-80% of nutrient is retained. Like above, suffix _n stands for nitrogen, and _p for phosphorus, and the two compounds can be modeled at the same time or separately.
  * *crit_len_n*: the LULC critical length (in meter): the distance after which it is assumed that a patch of LULC retains nutrient at its maximum capacity. If nutrients travel a distance smaller than the critical length, the retention efficiency will be less than the maximum value eff_x, following an exponential decay (see Nutrient transport section)
  * *proportion_subsurface_n* (optional): the proportion of dissolved nutrients over the total amount of nutrients, expressed as ratio between 0 and 1. By default, this value should be set to 0, indicating that all the nutrient transport is represented in the surface component.

  Example:

  .. csv-table::
    :file: ndr_images/ndr_biophysical_table_example.csv
    :header-rows: 1
    :name: NDR Biophysical Table Example

5. **Subsurface_max_retention_efficiency**: the maximum nutrient retention efficiency that can be reached through subsurface flow, a value between 0 and 1. This field characterizes the retention due to biochemical degradation in soils.

6. **Subsurface_critical_length**: the subsurface flow critical length (in meter): the distance after which it is assumed that soil retains nutrient at its maximum capacity. If dissolved nutrients travel a distance smaller than crit_len_sub , the retention efficiency is lower than the maximum value defined above. Setting this value to a distance smaller than the pixel size will result in the maximum retention efficiency being reached within one pixel only.

7. **Threshold flow accumulation value**: Integer value defining the number of upstream pixels that must flow into a pixel before it's considered part of a stream. This is used to generate a stream layer from the DEM (see RouteDEM documentation of the InVEST manual). The default is 1000. If the user has a map of stream lines in the watershed of interest, she should compare it with the *stream.tif* map that is output by the model. This threshold expresses where hydrologic routing is discontinued and where retention stops and the remaining pollutant will be exported to the stream.

8.  **Borselli *k* parameter**: calibration parameter that determine the shape of the relationship between hydrologic connectivity (the degree of connection from patches of land to the stream) and the sediment delivery ratio (percentage of soil loss that actually reaches the stream; cf. Figure 2). The default value is 2.


Running the Model
=================

To launch the nutrient model navigate to the Windows Start Menu -> All Programs -> InVEST +VERSION+ -> Nutrient delivery and retention. The interface does not require a GIS desktop, although the results will need to be explored with any GIS tool including ArcGIS, QGIS, and others.

Interpreting results
--------------------

Model outputs
^^^^^^^^^^^^^

The following is a short description of each of the outputs from the standalone Nutrient Delivery and retention model. These results are found within the model's workspace specified in the user interface.

 * **Parameter log**: Each time the model is run, a text (.txt) file will appear in the *Output* folder. The file will list the parameter values for that run and will be named according to the service, the date and time, and the suffix.

 * **Output folder**:

   * **output\x_export_suffix.shp**: This is a shapefile which aggregates the nutrient model results per watershed, with x being n for nitrogen, and p for phosphorus. The .dbf table contains the following information for each watershed:

      * *x_load_tot*: :math:`\mathrm{kg.yr^{-1}}`: total nutrient loads (sources) in the watershed, i.e. the sum of the nutrient contribution from all LULC without filtering from the landscape.
      * *x_exp_tot*: :math:`\mathrm{kg.yr^{-1}}`: total nutrient export from the watershed

   * **output\x_export.tif** : (kg/pixel) A pixel level map showing how much load from each pixel eventually reaches the stream.

 * **Intermediate folder**:

    * *crit_len_x*: map of the critical distance values, crit_len_x, found in the biophysical table
    * d_dn: downslope factor of the index of connectivity (Eq. 5)
    * *d_up*: distance from a pixel to the stream (following the D-infinity algorithm, see RouteDEM documentation for details)
    * *d_up*: map of the retention efficiencies, eff_x, found in the biophysical table
    * *effective_retention_x*: map of the effective retention provided by the downslope flow path for each pixel (Eq. 3)
    * *ic_factor*: map of the index of connectivity (Eq. 5)
    * *load_n*: map of loads (for surface transport) per pixel (kg,yr-1)
    * *ndr_x*: map of NDR values
    * *s_accumulation.s_bar*: slope parameters for IC equation found in the Nutrient transport section
    * *stream*: stream network computed by the RouteDEM algorithm (with 0s representing land pixels, and 1s representing stream pixels)
    * *sub_crit_len_x*: map of the critical distance value for subsurface transport, subsurface_crit_len_x (constant over the landscape)
    * *sub_eff_x*: map of the subsurface retention efficiency, subsurface_retention_eff (constant over the landscape)
    * *sub_load_x*: map of nutrient loads for subsurface transport, per pixel (kg,yr-1)
    * *sub_ndr_x*: map of subsurface NDR values




[===========================]

References
==========

Breuer, L., Vaché, K.B., Julich, S., Frede, H.-G., 2008. Current concepts in nitrogen dynamics for mesoscale catchments. Hydrol. Sci. J. 53, 1059–1074.

Hamel, P., Chaplin-Kramer, R., Sim, S., Mueller, C., 2015. A new approach to modeling the sediment retention service (InVEST 3.0): Case study of the Cape Fear catchment, North Carolina, USA. Sci. Total Environ. 166–177.

Harmel, D., Potter, S., Casebolt, P., Reckhow, K., 2007. Compilation of measured nutrient load data for agricultural land uses in the United States 76502, 1163–1178.

Keeler, B.L., Polasky, S., Brauman, K.A., Johnson, K.A., Finlay, J.C., Neill, A.O., 2012. Linking water quality and well-being for improved assessment and valuation of ecosystem services 109, 18629–18624.

Lin, J.., 2004. Review of published export coefficient and event mean concentration (EMC) data, WRAP Technical Notes Collection (ERDC TN-WRAP-04-3). Vicksburg, MS.

Mayer, P.M., Reynolds, S.K., Mccutchen, M.D., Canfield, T.J., 2007. Meta-Analysis of Nitrogen Removal in Riparian Buffers 1172–1180.

Pärn, J., Pinay, G., Mander, Ü., 2012. Indicators of nutrients transport from agricultural catchments under temperate climate: A review. Ecol. Indic. 22, 4–15.

Scanlon, B.R., Jolly, I., Sophocleous, M., Zhang, L., 2007. Global impacts of conversions from natural to agricultural ecosystems on water resources: Quantity versus quality. Water Resour. Res. 43.

Tarboton, D., 1997. A new method for the determination of flow directions and upslope areas in grid digital elevation models. Water Resour. Res. 33, 309–319.

Vigiak, O., Borselli, L., Newham, L.T.H., Mcinnes, J., Roberts, A.M., 2012. Comparison of conceptual landscape metrics to define hillslope-scale sediment delivery ratio. Geomorphology 138, 74–88.

Zhang, X., Liu, X., Zhang, M., Dahlgren, R. a, Eitzel, M., 2009. A review of vegetated buffers and a meta-analysis of their mitigation efficacy in reducing nonpoint source pollution. J. Environ. Qual. 39, 76–84.
