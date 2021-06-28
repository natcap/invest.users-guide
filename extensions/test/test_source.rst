Data needs
----------

This section outlines the specific data used by the model. See the
Appendix for the Carbon Storage model for additional information on data
sources and pre-processing of non-forest or non-tropical LULC classes.
Please consult the InVEST sample data (located in the folder where
InVEST is installed, if you also chose to install sample data) for
examples of all of these data inputs. This will help with file type,
folder structure and table formatting. Note that all GIS inputs must be
in the same projected coordinate system and in linear meter units.

-  **Workspace** (required). Folder where model outputs will be written.
   Make sure that there is ample disk space, and write permissions are
   correct.

-  **Suffix** (optional). Text string that will be appended to the end
   of output file names, as "_Suffix". Use a Suffix to differentiate
   model runs, for example by providing a short name for each scenario.
   If a Suffix is not provided, or changed between model runs, the tool
   will overwrite previous results.

-  **Land use/land cover** (required). A GIS raster dataset, with an
   integer LULC code for each cell. These LULC codes must match *lucode*
   values in the **Biophysical table**.

-  **Biophysical table** (required). A CSV (Comma-Separated Value) table
   providing information about which classes in the land-use/land-cover
   map are considered forest and should have the edge effect regression
   applied, and carbon density (Mg per hectare) for the land cover
   classes that are not forest. If “all carbon pools” is selected for
   “carbon pools to calculate” in the user interface for the model,
   columns 3-6 must be included (although 0’s can be placed for any
   pools that you do not wish to calculate); if “above ground only” is
   selected, columns 4-6 can be excluded.

The biophysical table columns must be named as follows:

1. **lucode** (required). Unique integer for each LULC class. *Every
   value in the LULC raster MUST have a corresponding lucode value in
   the Biophysical table.*

2. **is_tropical_forest** (required). Integer value of 1 if the LULC
   class is tropical forest, 0 if it is not tropical forest.

3. **c_above** (required for non-tropical forest). Carbon density value
   for the aboveground carbon pool. Units: megagrams per hectare
   (Mg/ha). See the Carbon Storage model chapter for more information.

4. **c_below** (optional). Carbon density value for the belowground
   carbon pool. Units: megagrams per hectare (Mg/ha). See the Carbon
   Storage model chapter for more information.

5. **c_soil** (optional). Carbon density value for the soil carbon pool.
   Units: megagrams per hectare (Mg/ha). See the Carbon Storage model
   chapter for more information.

6. **c_dead** (optional). Carbon density value for the dead matter
   carbon pool. Units: megagrams per hectare (Mg/ha). See the Carbon
   Storage model chapter for more information.

7. **Description** (optional). Text description of each LULC class.

-  **Carbon Pools to Calculate** (required, select from menu). Select
   either “all carbon pools” or “above ground only”.

-  **Compute forest edge effects** (optional). Check this box if edge
   effects on above-ground biomass should be included.

-  **Global forest carbon edge regression models** (required if
   computing forest edge effects, included in sample data). This
   shapefile was derived from a pantropical analysis of the relationship
   between forest biomass and distance from forest edge (Chaplin-Kramer
   et al. 2015). The rows contain the coefficients of the unique
   parameters for each 100 x 100 km subregion across the tropics. This
   information need not be altered unless you have run a separate
   regression for your region and have better or updated information.

-  **Number of nearest model point to average** (required if computing
   forest edge effects). Integer number used when calculating the
   biomass in a pixel. This value determines the number of closest
   regression models that are used when calculating the total biomass.
   Each local model is linearly weighted by distance such that the
   biomass in the pixel is a function of each of these points with the
   closest point having the highest effect. Default value is 10. Higher
   values smooth the variation in the edge effect detected in the
   different grid cells (seen in the carbon edge regression parameter
   shapefile) to a greater degree.

-  **Forest Edge Biomass to Carbon Conversion Factor** (required if
   computing forest edge effects). The floating point number by which to
   multiply forest above-ground biomass to convert to carbon. Default
   value is 0.47 (according to IPCC 2006). This pertains to the
   edge-effects regression parameters only; all values in the
   Biophysical Table should already be in terms of carbon, not biomass.

-  **Service areas of interest** (optional). If a summary of the carbon
   value is desired, a shapefile containing the area(s) of interest,
   either as a region area or partitioned into subregions (e.g.,
   ecoregions, districts, etc.) can be included. Carbon values will be
   aggregated within these region/subregion polygons and a single value
   will be output for each.
