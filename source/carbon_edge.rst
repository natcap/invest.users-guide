Forest Carbon Edge Effect
=========================

Summary
-------

The InVEST carbon edge effect model extends the approach of the InVEST
carbon model to account for forest carbon stock degradation due to the
creation of forest edges. It applies known relationships between carbon
storage and distance from forest edge to calculate edge effects in
carbon storage, and combines these estimates with carbon inventory data
to construct the overall carbon map. The model for edge effects pertains
to above-ground carbon only, because edge effects have not been
documented for the other carbon pools (below-ground, soil and dead
matter). For all other carbon pools, and for non-tropical forest
classes, or if the model is run without edge effects, it follows the
IPCC (2006) inventory approach to assigning carbon storage values by
land cover class.

Introduction
------------

The effects of future land-use change on carbon storage or sequestration
can be modeled by applying carbon storage estimates found in the
literature for different habitat types to each habitat found in a
landscape (e.g., Nelson et al. 2010). However, this approach assumes
that all habitat is equivalent in its quality of carbon storage,
regardless of where it occurs, despite the fact that there is
substantial evidence that fragmentation can play a dramatic role in
altering carbon storage and sequestration rates in tropical forests
(Broadbent et al. 2008, Dantas et al 2011, Laurance et al. 1997, 2000,
2001, 2002). For example, core forest has been shown to store more than
three times the carbon of edge forest in Brazilian Atlantic forests
(Dantas et al. 2011). Chaplin-Kramer et al. (2015) investigated this
pattern for the entire pantropics using remotely sensed data on biomass
(Baccini et al 2012) and associated land cover (Friedl et al. 2011) and
found a continuous relationship of carbon storage degrading gradually
toward a forest edge, which varies substantially from region to region.
This model accounts for these documented edge effects in tropical
forests, assigning carbon storage based on the distance of a pixel to
the nearest forest edge. This can improve the overall accuracy of carbon
storage estimates by 20% relative to forest inventory approaches, and
better captures the impacts of forest degradation from fragmentation,
beyond merely the area of habitat lost.

The model
---------

The InVEST carbon edge effect model is an update to the InVEST carbon
model, which incorporates the degradation of carbon storage that occurs
due to edge effects in tropical forests. The user designates which land
cover classes are forest, and then the model uses pre-generated
regression results to predict the carbon throughout a forest parcel
based on its distance to the nearest forest edge. These results are
combined with the carbon assigned to non-forest classes through
traditional inventory methods (IPCC 2006) used in the InVEST carbon
model, to generate a map of above-ground carbon storage for all land
cover classes. The InVEST carbon edge effect model can be run to
calculate only above ground carbon or all carbon pools, and it can be
run with or without edge effects. It is important to note that the edge
effects regression only pertains to above-ground carbon stocks because
edge effects have only been detected for above-ground biomass. To
include the other three carbon pools (below-ground, soil, and standing
dead matter), carbon density (Mg/ha) should be included for each land
cover class in the biophysical table.

How it works
~~~~~~~~~~~~

This model follows the methodology described in Chaplin-Kramer et al.
(2015), which constructs a series of regression models between forest
biomass density (Mg/ha) and distance from forest edge (km) for 100 km x
100 km grid cells throughout the pantropics. In grid cells where the
majority of pixels were from forest biomes, three candidate regression
models are considered to represent the relationship between biomass
density and distance to forest edge:

1. Asymptotic: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} - \theta_{2} \cdot \mathrm{\exp}( - \theta_{3} \cdot \mathrm{\text{Distance}})`

2. Logarithmic: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot ln(\mathrm{\text{Distance}})`

3. Linear: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot \mathrm{\text{Distance}}`

Then, for each grid cell, the candidate with the highest
r\ :sup:`2` value is used to best represent the relationship between
density and distance to forest edge.  Models (2) and (3) were deemed as
suitable (and more simplistic) alternatives in cells where higher
distances were generally not observed and as a result the forest core
was not firmly established. In the vast majority of grid cells, model
(1) was optimal.

The results of these regressions can be found in the carbon edge
regression parameter shapefile
(*core_data/forest_carbon_edge_regression_model_parameters.shp*) in the
sample dataset that is provided for the InVEST carbon edge effect model.
For any forest pixel within the study region, the model calculates the
distance of that pixel from forest edge then calculates biomass to a
predefined number of nearest regression models which is then aggregated
to a single result using a distance linear interpolation scheme. The
model then converts biomass to carbon with a user provided conversion
factor, defaulted to 0.47 (IPCC 2006). The user can designate the number
of local models used in the interpolation scheme which is defaulted to
10 but can range anywhere from 1 (only closest point) to 2635 (every
regression model on the planet). Note that a selection of 1 may result
in artificially large differences in carbon when moving from one pixel
to the next where they fall in different regression grid cells. The
higher the number of regression grid cells selected, the smoother the
transition from one pixel to the next. The user may wish to select the
number of grid cells overlapping the entire study region in order to
eliminate any artifacts of model selection. This can be determined by
examining the *intermediate_outputs\local_carbon_shape.shp* geometry
overlaid on the area of interest. The linear interpolation scheme for
biomass b on pixel p is given below

.. math:: b_{p} = \frac{\sum_{i \in n}\frac{1}{d_{i}}{b_{i}^{'}}_{}}{\sum\frac{1}{d_{i}}}

Where,

-  :math:`b_{p}`\ is the interpolated biomass on pixel p

-  n is the number of nearest models to interpolate from, a value
   provided by the user

-  i is the i\ :sup:`th` nearest biomass model from pixel p

-  d\ :sub:`i` is the distance from pixel p to the centroid of the
   i\ :sup:`th` biomass model.

The carbon calculated for non-forest classes follows the methodology
from the InVEST carbon model, assigning values based on forest carbon
inventory data designated in the biophysical table. The carbon maps
following this inventory approach and the edge effects approach are
merged into the final carbon map, such that the forest land covers
exhibit edge effects and all other land covers will not.

Data needs
----------
Note that all spatial inputs must be in the same projected coordinate system and in linear meter units.

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

   **Example Biophysical Table (data for Brazil):**

   .. csv-table::
          :file: ./carbon_edge/forest_edge_carbon_lu_table.csv
          :header-rows: 1
          :widths: auto

   *Sources for c_above data*:

   Closed shrublands, open shrublands, grasslands: Miranda, Sabrina do Couto, et al. Regional variations in biomass distribution in Brazilian savanna woodland. Biotropica 46.2 (2014): 125-138.

   Woody savannas, savanna: Saatchi, Susan S., et al. Distribution of aboveground live biomass in the Amazon basin. Global Change Biology 13.4 (2007): 816-837.

   Croplands: Fearnside, Philip M. Greenhouse gases from deforestation in Brazilian Amazonia: net committed emissions. Climatic Change 35.3 (1997): 321-360.

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

Interpreting Results
--------------------

The following is a short description of each of the outputs from the
Forest carbon edge effects model. Final results are found within the
user defined Workspace specified for this model run. "Suffix" in the
following file names refers to the optional user-defined Suffix input to
the model.

-  **Parameter log**. Each time the model is run, a text (.txt) file
      will appear in the \ *Workspace*. The file will list the parameter
      values for that run and will be named according to the service,
      the date and time. When contacting NatCap about errors in a model
      run, please include the parameter log.

-  **carbon_map_[Suffix[.tif**. A map of carbon stock per pixel, with
      the amount in forest derived from the regression based on distance
      to forest edge, and the amount in non-forest classes according to
      the biophysical table. Note that because the map displays carbon
      (Mg) per pixel, coarser resolution maps should have higher values
      for carbon, because the pixel areas are larger.

-  **aggregated_carbon_stocks_[Suffix].shp**: If service areas of
      interest are provided by the user, this output shapefile
      summarizes the total carbon (column *c_sum*) and mean carbon per
      ha (column *c_ha_mean*) in the area polygons defined. Values are
      in Mg.

Intermediate Results
~~~~~~~~~~~~~~~~~~~~

You may also want to examine the intermediate results. These files can
help determine the reasons for the patterns in the final results. They
are found in the intermediate_outputs folder within the
*Workspace* specified for this module.

-  intermediate_outputs\\\ **c_above_carbon_stocks_[Suffix].tif**.
      Carbon stored in the aboveground biomass carbon pool.

-  intermediate_outputs\\\ **c_below_carbon_stocks_[Suffix].tif**.
      Carbon stored in the belowground biomass carbon pool.

-  intermediate_outputs\\\ **c_dead_carbon_stocks_[Suffix].tif**. Carbon
      stored in the dead matter biomass carbon pool.

-  intermediate_outputs\\\ **c_soil_carbon_stocks_[Suffix].tif**. Carbon
      stored in the soil biomass carbon pool.

-  intermediate_outputs\\\ **local_carbon_shape.shp**. The regression
      parameters reprojected to match your study area.

-  intermediate_outputs\\\ **edge_distance_[Suffix].tif**. The distance
      of each forest pixel to the nearest forest edge

-  intermediate_outputs\\\ **tropical_forest_edge_carbon_stocks_[Suffix].tif**.
      A map of carbon in the forest only, according to the regression
      method

Appendix: Data Sources
----------------------

:ref:`Land Use/Land Cover <lulc>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Carbon Pools <carbon_pools>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References
----------

Baccini, A., S. J. Goetz, W. S. Walker, N. T. Laporte, M. Sun, D.
Sulla-Menashe, J. Hackler, P. S. A. Beck, R. Dubayah, M. A. Friedl, S.
Samanta, and R. A. Houghton. 2012. Estimated carbon dioxide emissions
from tropical deforestation improved by carbon-density maps. Nature
Climate Change 2:182–185.

Chaplin-Kramer, R., I. Ramler, R. Sharp, N. M. Haddad, J. S. Gerber, P.
C. West, L. Mandle, P. Engstrom, A. Baccini, S. Sim, C. Mueller, and H.
King. (2015). Degradation in carbon stocks near tropical forest edges.
Nature Communications.

Dantas de Paula, M., Alves-Costa, C., Tabarelli, M., 2011. Carbon
storage in a fragmented landscape of Atlantic forest: the role played by
edge-affected habitats and emergent trees. Tropical Conservation Science
4, 349–358.

Friedl, M. A., D. Sulla-Menashe, B. Tan, A. Schneider, N. Ramankutty, A.
Sibley, and X. Huang. 2010. MODIS Collection 5 global land cover:
Algorithm refinements and characterization of new datasets. Remote
Sensing of Environment 114:168–182.

Intergovernmental Panel on Climate Change (IPCC). 2006. IPCC Guidelines
for National Greenhouse Gas Inventories. Volume 4: Agriculture, Forestry
and Other Land Use.

Laurance, W. F., 1997. Biomass Collapse in Amazonian Forest Fragments.
Science 278, 1117–1118.

Laurance, W.F., 2000. Do edge effects occur over large spatial scales?
Trends in ecology & evolution 15, 134–135.

Laurance, William F., Williamson, G.B., 2001. Positive Feedbacks among
Forest Fragmentation, Drought, and Climate Change in the Amazon.
Conservation Biology 15, 1529–1535.

Laurance, W., Lovejoy, T., Vasconcelos, H., Bruna, E., Didham, R.,
Stouffer, P., Gascon, C., Bierregaard, R., Laurance, S., Sampaio, E.,
2002. Ecosystem decay of Amazonian forest fragments: a 22-year
investigation. Conservation Biology 16, 605–618.

Nelson, E., et al. 2010. Projecting global land-use change and its
effect on ecosystem service provision and biodiversity with simple
models. PLOS One 5: e14327
