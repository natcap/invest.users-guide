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

The Model
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

Also note that the regression data does not cover all of the Earth. It may be useful to make sure that it covers your area of interest by bringing the regression model layer forest_carbon_edge_regression_model_parameters.shp (found in this model's sample data) into a GIS and checking it against your study area. If the regression data does not cover your study area, you cannot use the model to calculate edge effects.


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
examining the *intermediate_outputs/local_carbon_shape.shp* geometry
overlaid on the area of interest. The linear interpolation scheme for
biomass b on pixel p is given below:

.. math:: b_{p} = \frac{\sum_{i \in n}\frac{1}{d_{i}}{b_{i}^{'}}_{}}{\sum\frac{1}{d_{i}}}

Where

-  :math:`b_{p}` is the interpolated biomass on pixel p

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

Limitations and Simplifications
-------------------------------

Edge effect data are only provided for tropical regions. To see if it overlaps your study area, bring the sample data layer *core_data/forest_carbon_edge_regression_model_parameters.shp* into a GIS. If the regression data does not cover your study area, you cannot use the model to calculate edge effects.

Edge effect data are only provided for above-ground carbon. If you want to include below-ground, soil or dead matter in the calculations, you can provide these data per land use class in the carbon pool table.

The default edge effect data that are provided with the model are pre-generated, and have a resolution of 100 km x 100 km. If you want to use different edge effect data, or a different resolution, you will need to create these data yourself, outside of the model.


Data Needs
----------
Note that all spatial inputs must be in the same projected coordinate system and in linear meter units.

- :investspec:`forest_carbon_edge_effect workspace_dir`

- :investspec:`forest_carbon_edge_effect results_suffix`

- :investspec:`forest_carbon_edge_effect lulc_raster_path`

- :investspec:`forest_carbon_edge_effect biophysical_table_path`

   Columns:

   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.lucode`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.is_tropical_forest`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_above`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_below`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_soil`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_dead`

   **Example Biophysical Table (data for Brazil):**

   .. csv-table::
          :file: ./carbon_edge/forest_edge_carbon_lu_table.csv
          :header-rows: 1
          :widths: auto

   *Sources for c_above data*:

   Closed shrublands, open shrublands, grasslands: Miranda, Sabrina do Couto, et al. Regional variations in biomass distribution in Brazilian savanna woodland. Biotropica 46.2 (2014): 125-138.

   Woody savannas, savanna: Saatchi, Susan S., et al. Distribution of aboveground live biomass in the Amazon basin. Global Change Biology 13.4 (2007): 816-837.

   Croplands: Fearnside, Philip M. Greenhouse gases from deforestation in Brazilian Amazonia: net committed emissions. Climatic Change 35.3 (1997): 321-360.

- :investspec:`forest_carbon_edge_effect pools_to_calculate`

- :investspec:`forest_carbon_edge_effect compute_forest_edge_effects` If selected, the model uses the Chaplin-Kramer et al. method to account for above ground carbon stocks in tropical forest types indicated by a '1' in the 'is_tropical_forest' field in the biophysical table.

- :investspec:`forest_carbon_edge_effect tropical_forest_edge_carbon_model_vector_path` This input is provided in the sample data and need not be altered unless you have run a separate regression for your region and have better or updated information. The provided shapefile was derived from a pantropical analysis of the relationship between forest biomass and distance from forest edge (Chaplin-Kramer et al. 2015).

   Note that the regression data does not cover all of the Earth. It may be useful to make sure that it covers your area of interest by bringing the regression model  layer *forest_carbon_edge_regression_model_parameters.shp* (found in this model's sample data) into a GIS and checking it against your study area. If the regression data does not cover your study area, you cannot use the model to calculate edge effects.

- :investspec:`forest_carbon_edge_effect n_nearest_model_points` Default value is 10. Higher values smooth the variation in the edge effect detected in the different grid cells (seen in the carbon edge regression parameter shapefile) to a greater degree.

- :investspec:`forest_carbon_edge_effect biomass_to_carbon_conversion_factor` Default value is 0.47 (according to IPCC 2006). This pertains to the edge-effects regression parameters only; all values in the Biophysical Table should already be in terms of carbon, not biomass.

- :investspec:`forest_carbon_edge_effect aoi_vector_path` Note that the regression data does not cover all of the Earth. It may be useful to make sure that it covers your area of interest by bringing the regression model layer *forest_carbon_edge_regression_model_parameters.shp* (found in this model's sample data) into the GIS and checking it against your study area. If the regression data does not cover your study area, you cannot use the model to calculate edge effects.

Interpreting Results
--------------------

Final Results
~~~~~~~~~~~~~
-  **Parameter log**. Each time the model is run, a text (.txt) file will appear in the *Workspace*. The file will list the parameter values for that run and will be named according to the service, the date and time. When contacting NatCap about errors in a model run, please include the parameter log.

-  **carbon_map_[Suffix].tif**. A map of carbon stock, with the amount in forest derived from the regression based on distance to forest edge, and the amount in non-forest classes according to the biophysical table. Units are metric tons per hectare (Mg/ha).

-  **aggregated_carbon_stocks_[Suffix].shp**: If service areas of interest are provided by the user, this output shapefile summarizes the total carbon (column *c_sum*) and mean carbon per ha (column *c_ha_mean*) in the area polygons defined. Values are in metric tons (Mg).

Intermediate Results
~~~~~~~~~~~~~~~~~~~~
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
Stouffer, P., Gascon, C., Bierregaard, R., Laurance, S., Sampaio, E., 2002.
Ecosystem decay of Amazonian forest fragments: a 22-year
investigation. Conservation Biology 16, 605–618.

Nelson, E., et al. 2010. Projecting global land-use change and its
effect on ecosystem service provision and biodiversity with simple
models. PLOS One 5: e14327
