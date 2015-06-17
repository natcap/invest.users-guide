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

WRITE BIG EQUATION 3 HERE

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


[===========================]

Running the Model
=================

**General Parameters**

1. **Workspace Folder** (Required) The selected folder is used as the workspace where all intermediate and final output files will be written.  If the selected folder does not exist, it will be created.  If datasets already exist in the selected folder, they will be overwritten.

2. **Results Suffix** (Optional) Parameter that appends the given string on to every intermediate and output file for organizing sets of multiple runs in the same workspace.

3. **DEM** (Required) Raster input that contain elevation values for each cell.  The model uses this file to calculate hydrological flow and samples all other inputs to be aligned and the same cell size as this input.

4. **Land use** (Required) LULC is a GIS raster dataset, with an integer LULC code for each cell that maps biophysical values in the constant table to these pixels.

5. **Watersheds** (Required) Shapefile/Vector layer that are used to clip datasets and aggregate final results.  Requires an intger field called 'ws_id' that is used to index the final result table.

6. **Biophysical Table** (Required) CSV table that contains biophysical information about the landcovers provided in the previous raster.  Must contain the fields:
   * lucode: an integer landcover code that corresponds to a value in the **Land use** input.
   * load\_n and/or load\_p: the nitrogen or phosphorous load for the given landcover type
   * eff\_n and/or eff_\p: the maximum retention efficiency of the given land cover type for (n)itrogen or (p)hosporous.
   * crit\_len\_n and/or crit\_len\_p: the critical retention efficiency length of the given landcover type for (n)itrogen or (p)hosporous.

7. **Threshold Flow Accumulation** (Required) An integer value indicating for any pixel on the DEM, how many pixels upstream would classify that pixel as a stream.  Important since the hydrological connectivity of this model is dependent in part on the distance downstream to a stream pixel.

8. **Borselli k Parameter** (Required) This parameter is defaulted to 2 and can be adjusted for calibration.


References
==========

Breuer, L., Vaché, K.B., Julich, S., Frede, H.-G., 2008. Current concepts in nitrogen dynamics for mesoscale catchments. Hydrol. Sci. J. 53, 1059–1074.

Hamel, P., Chaplin-Kramer, R., Sim, S., Mueller, C., 2015. A new approach to modeling the sediment retention service (InVEST 3.0): Case study of the Cape Fear catchment, North Carolina, USA. Sci. Total Environ. 166–177.

Harmel, D., Potter, S., Casebolt, P., Reckhow, K., 2007. Compilation of measured nutrient load data for agricultural land uses in the United States 76502, 1163–1178.

Keeler, B.L., Polasky, S., Brauman, K.A., Johnson, K.A., Finlay, J.C., Neill, A.O., 2012. Linking water quality and well-being for improved assessment and valuation of ecosystem services 109, 18629–18624.

Lin, J.., 2004. Review of published export coefficient and event mean concentration (EMC) data, WRAP Technical Notes Collection (ERDC TN-WRAP-04-3). Vicksburg, MS.

Mayer, P.M., Reynolds, S.K., Mccutchen, M.D., Canfield, T.J., 2007. Meta-Analysis of Nitrogen Removal in Riparian Buffers 1172–1180.

Pärn, J., Pinay, G., Mander, Ü., 2012. Indicators of nutrients transport from agricultural catchments under temperate climate: A review. Ecol. Indic. 22, 4–15.

Scanlon, B.R., Jolly, I., Sophocleous, M., Zhang, L., 2007. Global impacts of conversions from natural to agricultural ecosystems on water resources : Quantity versus quality. Water Resour. Res. 43.

Tarboton, D., 1997. A new method for the determination of flow directions and upslop areas in grid digital elevation models. Water Resour. Res. 33, 309–319.

Vigiak, O., Borselli, L., Newham, L.T.H., Mcinnes, J., Roberts, A.M., 2012. Comparison of conceptual landscape metrics to define hillslope-scale sediment delivery ratio. Geomorphology 138, 74–88.

Zhang, X., Liu, X., Zhang, M., Dahlgren, R. a, Eitzel, M., 2009. A review of vegetated buffers and a meta-analysis of their mitigation efficacy in reducing nonpoint source pollution. J. Environ. Qual. 39, 76–84.
