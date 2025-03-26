Scenario Generator: Proximity Based
===================================

Summary
-------

The proximity-based scenario generator creates a set of contrasting land
use change maps that convert habitat in different spatial patterns. The
user determines which habitat can be converted and what they are
converted to, as well as type of pattern, based on proximity to the edge
of a focal habitat. In this manner, an array of land-use change patterns
can be generated, including pasture encroaching into forest from the
forest edge, agriculture expanding from currently cropped areas, forest
fragmentation, and many others. The resulting land-use maps can then be
used as inputs to InVEST models, or other models for biodiversity or
ecosystem services that are responsive to land use change.

Introduction
------------

In order to understand the change in biodiversity and ecosystem services
(BES) resulting from change in land-use, it is often helpful to start
with a scenario or a set of scenarios that exhibit different types of
land-use change. Because many of the relationships between landscapes
and BES are spatially-explicit, a different pattern of habitat
conversion for the same total area of habitat converted can lead to very
different impacts on BES. This proximity-based scenario generator
creates different patterns of conversion according to user inputs
designating focal habitat and converted habitat, in contrast to but
potentially complementing the InVEST rule-based scenario generator that
creates maps of land-use change according to user-assigned probabilities
that certain transitions will occur. Thus, the intent of the InVEST
proximity-based scenario generator is not to forecast actual predicted
patterns of expansion, but rather to develop different patterns of land
use change in order to examine the relationship between land-use change
and BES, and how the relationship may differ depending on land use
change assumptions.

The Model
---------

The tool can generate two scenarios at once (nearest to the edge and
farthest from the edge of a focal habitat), for a conversion to
particular habitat type for a given area. To convert to different
habitat types, different habitat amounts, or to designate different
focal habitats or converted habitats, the tool can be run multiple times
in sequence.

How it works
~~~~~~~~~~~~

Three types of landcover must be defined: 1) *Focal* *landcover* is the
landcover(s) that set the proximity rules from which the scenarios will
be determined. The scenario generator will convert habitat from the edge
or toward the edge of patches of these types of landcover. This does not
mean it will convert these land-covers, only that it will measure
distance to or from the edges in designating where the conversion will
happen. 2) *Convertible landcover* is the landcover(s) that can be
converted. These could be the same as the focal landcover(s), a subset,
or completely different. 3) *Replacement landcover* is the landcover
type to which the convertible landcovers will be converted. This can
only be one landcover type per model run.

Two scenarios can then be run at a time: 1) *Nearest to edge* means that
convertible landcover types closest to the edges of focal landcovers
will be converted to the replacement landcover. 2) *Farthest from edge*
means that convertible landcover types furthest from the edges of focal
landcover types will be converted to the replacement landcover. If this
scenario is chosen, the user can designate in how many steps the
conversion should occur. This is relevant if the focal landcover is the
same as the convertible land cover because the conversion of the focal
landcover will create new edges and hence will affect the distance
calculated from the edge of that landcover. If desired, the conversion
can occur in several steps, each time converting the farthest from the
edge of the focal landcover, causing a fragmentary pattern.

Below are some examples of the types of scenarios that can be generated
by manipulating these basic inputs, using the land-cover in the sample
data that ship with this model. This landcover is from MODIS, using the
UMD classification (Friedl et al. 2011), which follows the following
scheme: 1 – Evergreen needleleaf forest; 2 – Evergreen broadleaf forest;
3 – Deciduous needleleaf forest; 4 – Deciduous broadleaf forest; 5 –
Mixed forest; 6 – Closed shrublands; 7 – Open shrublands; 8 – Woody
savannas; 9 – Savannas; 10 – Grasslands; 12 – Croplands; 13 – Urban and
built-up; 16 – Barren or sparsely vegetated.

**Expand agriculture from forest edge inwards:**

focal landcover codes: 1 2 3 4 5

convertible landcover codes: 1 2 3 4 5

replacement landcover code: 12

check "Convert Nearest to Edge"

number of steps toward conversion: 1

**Expand agriculture from forest core outwards**:

focal landcover codes: 1 2 3 4 5

convertible landcover codes: 1 2 3 4 5

replacement landcover code: 12

check "Convert Farthest From Edge"

number of steps toward conversion: 1

**Expand agriculture by fragmenting forest:**

focal landcover codes: 1 2 3 4 5

convertible landcover codes: 1 2 3 4 5

replacement landcover code: 12

check "Convert Farthest From Edge"

number of steps toward conversion: 10 (or as many steps as desired; the
more steps, the more finely fragmented it will be and the longer the
simulation will take)

**Expand pasture into forest nearest to existing agriculture:**

focal landcover codes: 12

convertible landcover codes: 1 2 3 4 5

replacement landcover code: 10

check "Convert Nearest to Edge"

number of steps toward conversion: 1

Data Needs
----------

The only required input data to run the proximity-based scenario
generator is a base land-use/land-cover map and user-defined land cover
codes pertaining to this base map to designate how the scenarios should
be computed.

- :investspec:`scenario_gen_proximity workspace_dir`

- :investspec:`scenario_gen_proximity results_suffix`

- :investspec:`scenario_gen_proximity base_lulc_path`

- :investspec:`scenario_gen_proximity aoi_path` Prior to scenario generation, the map will be clipped to the extent of this vector.

- :investspec:`scenario_gen_proximity area_to_convert` As many pixels as possible will be converted without exceeding this area.

- :investspec:`scenario_gen_proximity focal_landcover_codes`

- :investspec:`scenario_gen_proximity convertible_landcover_codes`

- :investspec:`scenario_gen_proximity replacement_lucode` If there are multiple LULC types that are of interest for conversion, this tool should be run in sequence, choosing one type of conversion each time. A new code may be introduced if it is a novel land-use for the region or if it is desirable to track the expanded land-use as separate from historic land-use.

- :investspec:`scenario_gen_proximity convert_farthest_from_edge` Convertible land covers and habitat of interest land-covers may be the same, or a subset of one another, or they can be different. If they are the same, the number of steps for conversion should be specified, because the conversion of habitat within the focal land cover will create new habitat edge, resulting in a completely different pattern of conversion depending on how many steps are chosen.

- :investspec:`scenario_gen_proximity convert_nearest_to_edge` Convertible land covers and habitat of interest land-covers may be the same, or a subset of one another, or they can be different.

- :investspec:`scenario_gen_proximity n_fragmentation_steps` Entering a 1 means that all of the habitat conversion will occur in the center of the patch of the habitat of interest. Entering 10 will be fragmented according to a pattern of sequentially converting the pixels furthest from the edge of that habitat, over the number of steps specified by the user.

Interpreting Results
--------------------

Final Results
~~~~~~~~~~~~~

- **InVEST….log…txt:** Each time the model is run, a text (.txt) file will appear in the *Output* folder. The file will list the parameter values for that run and will be named according to the model, the date and time, and the suffix.

- **nearest_to_edge_<suffix>.tif**: LULC raster for the scenario of conversion nearest to the edge of the focal habitat.

- **farthest_from_edge_<suffix>.tif**: LULC raster for the scenario of conversion farthest from the edge of the focal habitat.

- **nearest_to_edge_<suffix>.csv**: table listing the area (in hectares) and number of pixels for different land cover types converted for the scenario of conversion nearest to the edge of the focal habitat. Values in the *original lucode* column reflect landcover(s) converted by the model. The *replacement lucode* column reflects the landcover type to which the original landcover(s) was converted. All values in this column will be the same, as only one Replacement Landcover Code can be specified per model run.

- **farthest_from_edge_<suffix>.csv**: table listing the area (in hectares) and number of pixels for different land cover types converted for the scenario of conversion farthest from the edge of the focal habitat. Values in the *original lucode* column reflect landcover(s) converted by the model. The *replacement lucode* column reflects the landcover type to which the original landcover(s) was converted. All values in this column will be the same, as only one Replacement Landcover Code can be specified per model run.

Intermediate Results
~~~~~~~~~~~~~~~~~~~~

- **{farthest_from_/nearest_to}_edge_distance_<suffix>.tif**: This raster shows the distance (in number of pixels) of each pixel to the nearest edge of the focal landcover.

- **_tmp_work_tokens:** This directory stores metadata used internally to enable avoided re-computation.

Sample Script
-------------

The following script is provided to demonstrate how the scenarios
described in Section “How It Works” can be composed into a single script
that’s callable from the InVEST Python API::

        import natcap.invest.scenario_generator_proximity_based

        edge_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': False,
            u'convert_nearest_to_edge': True,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'edge',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        core_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': True,
            u'convert_nearest_to_edge': False,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'core',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        frag_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': True,
            u'convert_nearest_to_edge': False,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'10',
            u'replacement_lucode': u'12',
            u'results_suffix': 'frag',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        ag_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': False,
            u'convert_nearest_to_edge': True,
            u'convertible_landcover_codes': u'12',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'ag',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }
        if __name__ == '__main__':
            natcap.invest.scenario_generator_proximity_based.execute(edge_args)
            natcap.invest.scenario_generator_proximity_based.execute(core_args)
            natcap.invest.scenario_generator_proximity_based.execute(frag_args)
            natcap.invest.scenario_generator_proximity_based.execute(ag_args)
