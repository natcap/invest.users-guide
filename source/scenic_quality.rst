.. _scenic-quality:

********************************************
Unobstructed Views: Scenic Quality Provision
********************************************

Summary
=======
 
The natural and scenic views of marine and coastal seascapes can contribute to the well-being of local communities in a number of ways. Scenic amenities play an important role in augmenting local economies by attracting visitors who support local businesses. The value of local property partially depends on attributes of its location and scenic views often increase local property values (Sanders and Polasky 2009, Bourassa et al. 2004, Benson et al. 2004).   Local communities and their residents often become strongly attached to views and show fervent opposition to new development that has the potential to threaten the integrity of existing views and diminish the benefits drawn from those views (Ladenburg and Dubgaard 2009, Haggett 2011). The InVEST scenic quality model allows users to determine the locations from which new nearshore or offshore features can be seen. It generates viewshed maps that can be used to identify the visual footprint of new offshore development and calculates the value of the impacted visibility. Inputs to the viewshed model include: topography and bathymetry, locations of offshore facilities of interest, and the locations of viewers (e.g. population centers or areas of interest such as parks or trails). The model does not quantify economic impacts of altering the viewshed, but it can be adapted to compute viewshed metrics for use in a more detailed valuation study. A key limitation of the model is that it does not currently account for the ways in which vegetation or land-based infrastructure may constrain land areas that are visually affected by offshore development.


Introduction
============

Coastal ecosystems are increasingly dominated by human activities. This rise in human activities can compromise the unique scenic qualities associated with coastal and marine areas. The coastline and 'seascape' is an important economic asset that attracts visitors for tourism and recreation and contributes to the general quality of life for people living near the coast. Near and offshore development projects often raise considerable concern within the local communities that value the natural seascape for its inherent beauty. Visual impacts are external effects that unless measured and accounted for, do not factor into the calculus of weighing the costs and benefits of new coastal development. Applications using viewshed analysis range from the siting of aquaculture facilities to minimize spatial competition with tourism activities (Perez 2003) to seascape and shoreline visibility assessment of offshore wind projects (Environmental Design and Research 2006). Because scenic beauty is an attribute generally considered to be important to people living near the coast and for those who visit coastal areas to enjoy the ocean and the marine environment, coastal planners can incorporate measures of visual amenities and/or disamenities into broader policy deliberations and planning exercises. Because most applications of viewshed analysis involve examining the negative impacts of new facilities, language within the InVEST scenic quality model assumes the objects viewed have a negative impact on views. However, positive interpretation of viewing these objects can be included with interpretation of model results.

The InVEST scenic quality model provides users with a simple way to provide information about potential tradeoffs between nearshore and offshore development proposals and the visual impacts of those projects. The viewshed maps produced by the model can be used to identify coastal areas that are most likely to be directly affected by additions to the seascape. They can serve as valuable input into broader analyses that consider a range of services provided by the marine environment.

This model can be used to compute the costs associated with offshore visual impacts, these costs are likely to decrease as the location of facilities moves further offshore, while the costs of installing and operating offshore facilities generally increase with distance from the shoreline. The few valuation studies that explore the economic magnitude of visual disamenities resulting from offshore development projects show a complex picture. One recent study found that individuals living along the coast have external costs ranging from $27 to $80 resulting from the visual disamenity of an offshore wind project (Krueger et al. 2010). In contrast, Firestone et al. (2009) found that public acceptance for offshore renewable energy projects is growing and may be less contentious than previously anticipated.


The Model
=========

The scenic quality model provides information about the visibility of offshore objects from the surrounding landscape or seascape. Offshore and nearshore development projects, such as renewable wave energy facilities or aquaculture facilities, have the potential to impact the visual amenities that are an important feature of many coastal areas. The results of viewshed analysis will be useful for decision-makers who would like to identify areas where visual impacts may be an important factor to incorporate into planning.

The model inputs are divided into two groups: **General** has all the entries necessary to run the viewshed computation such as the location of a DEM and a point vector that identifies the locations of sites that contribute to visual impacts. **Valuation** allows the user to select the functional form of the valuation function and its parameters. The viewshed analysis is then computed over a user-defined area of interest (AOI).

The model will create three outputs that can be used to assess the visible impact of any type of facility added to the marine environment:

    * *vshed.tif* is a raster containing the sum of how many viewpoints are visible from each pixel. If a *WEIGHT* column is provided in the structures/viewpoints vector, the visibility sum is weighted. If the valuation and weights are all set to ``1``, this raster reduces to merely a count of the number of sites that are visible from a pixel.

    * *vshed_value.tif* is the sum of all individual valuation rasters calculated for each site. If a *WEIGHT* column is provided in the sites vector, the values will be weighted accordingly.

    * *vshed_qual.tif* is a raster representing the visual quality of a given pixel. The cells of *vshed_Value.tif* are classified according to the following percentile breaks:

        1. Unaffected
        2. Low visual impact / High visual quality (< 25th percentile)
        3. Moderate visual impact / Medium visual quality (25-50th percentile)
        4. High visual impact / Low visual quality (50-75th percentile)
        5. Very high visual impact / Poor visual quality (> 75th percentile)

Additional files are created for each feature *X* at each step of the computation:

    * *visibility_X.tif* indicates which pixels are visible from feature *X*
    * *auxiliary_X.tif* is an intermediate raster written as part of the viewshed algorithm. Pixel values indicate the minimum height that must be reached for a pixel to be visible.
    * *value_X.tif* is the value of the viewshed, weighted (if a *WEIGHT* column is provided), and in terms of the distance (in meters) between pixels and feature *X*.


How it Works
------------
The InVEST scenic quality model computes the visual impact of features in the landscape in several steps:

1. For each structure site:

   1. Calculate the visibility for each point feature *X* (*intermediate\\visibility_X.tix*) based on the Wang et al reference-plane viewshed algorithm.
   2. From the visibility, determine the value of the visibility amenity/disamenity by weighting the visibility and applying the valuation function defined in the user interface (*intermediate\\value_X.tif*).

2. Sum the valuation rasters to create a weighted aggregate (*output\\vshed_value.tif*)

3. Divide the weighted, aggregate valuation raster into quartiles to create a raster representing visual quality (*output\\vshed_qual.tif*)

4. Weight and sum the visibility rasters from all structures points to create a weighted sum of the number of visible points (*output\\vshed.tif*)

Valuation can take one of these forms:

Linear:

.. math:: f(x) = a + b \cdot x
    :name: linear form

Logarithmic:

.. math:: f(x) = a + b \cdot ln(x)
    :name: logarithmic_form

Exponential:

.. math:: f(x) = a \cdot e^{(-b \cdot x)}
    :name: exponential form 

Where *x* is the distance in meters from the cell center to a point feature, and *a* and *b* are user-defined coefficients. With the default parameter values (*a=1*, *b=0*), the model computes an aggregate viewshed. The valuation function is computed up to a maximum valuation radius that defaults to 8000 meters.


Limitations and Simplifications
===============================

The global DEM included with the scenic quality model does not account for trees, buildings, or other structures that can obscure the view. If users have a raster layer that represents the locations of trees, buildings, or other obstructions (and their heights) this information can be incorporated into the DEM to create a more realistic surface to obscure or allow views. The model accounts for the curvature of the earth in limiting visibility but it does not limit the distance at which objects of varying size and quality may be visible to the human eye in the default settings. As long as there is a straight-line vector that can be computed from a particular DEM grid cells to any offshore point, that grid cell will be counted as visible. This should be carefully considered when interpreting viewshed impact maps from facilities located far offshore when default settings are used. However, users can provide an outer radius that limits the search distance when identifying areas visible from each offshore development site.


.. _ae-data-needs:

Data Needs
==========

General
-------

- :investspec:`scenic_quality.scenic_quality workspace_dir`

- :investspec:`scenic_quality.scenic_quality results_suffix`

- :investspec:`scenic_quality.scenic_quality aoi_path`

- :investspec:`scenic_quality.scenic_quality structure_path` These may represent structures such as aquaculture netpens or wave energy facilities. If you wish to include features with a larger footprint, such as clear-cuts, convert polygons to a grid of evenly spaced points.

  The model will compute a viewshed for each feature separately and aggregate them into a combined viewshed. The user can specify up to three fields (all fields are optional) to assign a maximum viewing distance, a viewshed importance coefficient, or a viewpoint height to each feature.

  Fields:

  - :investspec:`scenic_quality.scenic_quality structure_path.fields.radius`
  - :investspec:`scenic_quality.scenic_quality structure_path.fields.weight`
  - :investspec:`scenic_quality.scenic_quality structure_path.fields.height`

- :investspec:`scenic_quality.scenic_quality dem_path` Used to determine areas within the AOI’s land-seascape where features impacting scenic quality are visible. The model runs at the resolution of this raster.

- :investspec:`scenic_quality.scenic_quality refraction` Changes in air density curve the light downward causing an observer to see further and the earth to appear less curved. While the magnitude of this effect varies with atmospheric conditions, a standard rule of thumb is that refraction of visible light reduces the apparent curvature of the earth by one-seventh. The default value is 0.13.


Valuation
---------

- :investspec:`scenic_quality.scenic_quality do_valuation`

- :investspec:`scenic_quality.scenic_quality valuation_function`

- :investspec:`scenic_quality.scenic_quality a_coef`

- :investspec:`scenic_quality.scenic_quality b_coef`

- :investspec:`scenic_quality.scenic_quality max_valuation_radius` The valuation function :math:`f` cannot be negative at the radius :math:`r` (:math:`f(r)>=0`).


Final Results
-------------

Output Folder
^^^^^^^^^^^^^
* **Output\\vshed_qual.tif**

    * This raster layer contains a field that classifies based on quartiles the visual quality within the AOI. The visual quality classes include: unaffected (no visual impact), high (low visual impact), medium (moderate visual impact), low (high visual impact), and very low (very high visual impact).

* **Output\\vshed.tif**

    * This raster layer contains the weighted sum of all visibility rasters. If no weight column is provided in the structures point vector, this raster will represent a count of the number of structure points that are visible from each pixel.

    * In order to compare scenario runs, use this layer rather than vshed_qual. By calculating the difference between "vshed" outputs from multiple runs, a user can assess changes in visual quality across scenarios.

* **Output\\vshed_value.tif**

    * This raster layer contains the weighted sum of the valuation rasters created for each point.

Intermediate Folder
^^^^^^^^^^^^^^^^^^^

* **intermediate\\dem_clipped.tif**

    * This raster layer is a version of the DEM that has been clipped and masked to the AOI and tiled. This is the DEM file that is used for the viewshed analysis.

* **intermediate\\aoi_reprojected.shp**

    * This vector is the AOI, reprojected to the DEM's spatial reference and projection.

* **intermediate\\structures_clipped.shp**

    * This vector contains all viewpoints that intersect with the AOI.

* **intermediate\\structures_reprojected.shp**

    * This is the structures vector, reprojected to the DEM's spatial reference and projection.

* **intermediate\\visibility_*.tif**

    * The visibility raster for a given structures viewpoint. This raster has pixel values of 0 (not visible), 1 (visible), or nodata (where the DEM is nodata).

* **intermediate\\auxiliary_*.tif**

    * An intermediate raster created while calculating the viewshed for the given structures viewpoint. The values of this raster represent the minimum height that the DEM must have in order for the terrain to be visible at that pixel.

* **intermediate\\value_*.tif**

    * The calculated value of the viewshed amenity/disamenity given the distances (in meters) of pixels from the structures viewpoint, the weight of the viewpoint, the valuation function, and the *a* and *b* coefficients. The viewshed's value is only evaluated for visible pixels. If an underlying DEM pixel is undefined (has a nodata value), so does the valuation raster.


References
==========

Benson E., Hansen, J., Schwartz, A., and Smersh, G., 1998. Pricing residential amenities: the value of a view. Journal of Real Estate Research, 16: 55-73.

Bourassa, S., Hoesli, M. and Sun, J. 2004. What’s in a view? Environment and Planning A. 36(8): 1427-1450.

Center for International Earth Science Information Network (CIESIN), Columbia University; International Food Policy Research Institute (IFPRI); The World Bank; and Centro Internacional de Agricultura Tropical (CIAT). 2004. Global Rural-Urban Mapping Project (GRUMP), Alpha Version: Population Grids. Palisades, NY: Socioeconomic Data and Applications Center (SEDAC), Columbia University. Available at permanently to https://sedac.ciesin.columbia.edu/data/collection/gpw-v4. (downloaded on 1/6/2011).

Environmental Design and Research, P.C. 2006. Seascape and shoreline visibility assessment. Cape Wind Energy Project. Cape Cod, Martha’s Vineyard, and Nantucket, Massachusetts. Prepared for Cape Wind Associates, L.L.C. Boston, Mass. Syracuse, N.Y. July 2006.

Firestone, J., Kempton, W. & Krueger, A., 2009. Public acceptance of offshore wind power projects in the USA. Wind Energy, 12(2):183-202. 

Haggett, C. 2011. Understanding public responses to offshore wind power. Energy Policy. 39: 503-510.

Krueger, A., Parson, G., and Firestone, J., 2010. Valuing the visual disamenity of offshore wind power at varying distances from the shore: An application of on the Delaware shoreline. Working paper. Available at: https://works.bepress.com/george_parsons/.

Ladenburg, J. & Dubgaard, A., 2009. Preferences of coastal zone user groups regarding the siting of offshore wind farms. Ocean & Coastal Management, 52(5): 233-242. 

Perez, O.M., Telfer, T.C. & Ross, L.G., 2005. Geographical information systems-based models for offshore floating marine fish cage aquaculture site selection in Tenerife, Canary Islands. Aquaculture Research, 36(10):946-961. 

Sander, H.A. & Polasky, S., 2009. The value of views and open space: Estimates from a hedonic pricing model for Ramsey County, Minnesota, USA. Land Use Policy, 26(3):837-845. 

Wang, J., Robertson, G.J., White, K., 2000. Generating viewsheds without using sightlines. Photogrammetric Engineering & REmote Sensing, 66(1):87-90
