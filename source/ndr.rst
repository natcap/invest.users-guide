.. _ndr:

*************************************************
(under development) Nutrient Delivery Ratio model
*************************************************

Model
=====

Surface NDR
-----------

Surface NDR is constructed pixel by pixel and accounts for variations in critical flow lengths due to landcover, and non-linear effects due to saturation of downstream nutrient retention along the flowpath to the stream. First we calculate ::math:`eff_i`, the effective downstream nutrient retention for any pixel :math:`i`,

.. math::
    \begin{dcases*}
    eff'_{LULC_i}\cdot (1-s_i) & if down_i is a stream pixel\\
    eff'_{down_i}\cdot s_i + eff_{LULC_i}\cdot (1-s_i) & if eff_{LULC-i} > eff'_{down_i} \\
    eff'_{down_i} & otherwise
    \end{dcases*}


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

Drewry, J.J., Newham, L.T.H., Greene, R.S.B., 2011. Index models to evaluate the risk of phosphorus and nitrogen loss at catchment scales. Journal of Environmental Management 92(3): 639-649. http://dx.doi.org/10.1016/j.jenvman.2010.10.001

Elliott, H.A., Brandt, R.C., Kleinman, P.J., Sharpley, A.N., Beegle, D.B., 2006. Estimating source coefficients for phosphorus site indices. J Environ Qual 35(6): 2195-201. 10.2134/jeq2006.0014

Harmel, D., Potter, S., Casebolt, P., Reckhow, K., Rossi, C., Haney, R., 2006. Compilation of measured nutrient load data for agricultural land uses in the United States Journal of the American Water Resources Association 42(5): 1163-1178.

Newham, L.T.H., Letcher, R.A., Jakeman, A.J., Kobayashi, T., 2004. A framework for integrated hydrologic, sediment and nutrient export modelling for catchment-scale management. Environmental Modelling & Software 19(11): 1029-1038. http://dx.doi.org/10.1016/j.envsoft.2003.11.006

Newham, L.T.H., Drewry, J.J., Fu, B., 2008. Catchment-Scale Water Quality Modelling and Integration of Collateral Information. In: M. Sànchez-Marrè, J.B., J. Comas, A. Rizzoli and G. Guariso (Ed.), iEMSs 2008: International Congress on Environmental Modelling and Software. International Environmental Modelling and Software Society (iEMSs).

Pan, Y., Hom, J., Birdsey, R., McCullough, K., 2004. Impacts of Rising Nitrogen Deposition on N Exports from Forests to Surface Waters in the Chesapeake Bay Watershed. Environmental Management 33(1): S120-S131. 10.1007/s00267-003-9122-5

Pärn, J., Pinay, G., Mander, Ü., 2012. Indicators of nutrients transport from agricultural catchments under temperate climate: A review. Ecological Indicators 22(0): 4-15. http://dx.doi.org/10.1016/j.ecolind.2011.10.002

Vigiak, O., Borselli, L., Newham, L.T.H., McInnes, J., Roberts, A.M., 2012. Comparison of conceptual landscape metrics to define hillslope-scale sediment delivery ratio. Geomorphology 138(1): 74-88. http://dx.doi.org/10.1016/j.geomorph.2011.08.026
