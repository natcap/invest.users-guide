.. _aethetic-quality:

.. |openfold| image:: ./shared_images/openfolder.png
              :alt: open
	      :align: middle 

.. |addbutt| image:: ./shared_images/addbutt.png
             :alt: add
	     :align: middle 
	     :height: 15px

.. |okbutt| image:: ./shared_images/okbutt.png
            :alt: OK
	    :align: middle 

.. |adddata| image:: ./shared_images/adddata.png
             :alt: add
	     :align: middle 

********************************************
Unobstructed Views: Scenic Quality Provision
********************************************

Summary
=======
 
The natural and scenic views of marine and coastal seascapes can contribute to the well-being of local communities in a number of ways.  Scenic amenities play an important role in augmenting local economies by attracting visitors who support local businesses. The value of local property partially depends on attributes of its location and scenic views often increase local property values (Sanders and Polasky 2009, Bourassa et al. 2004, Benson et al. 2004).   Local communities and their residents often become strongly attached to views and show fervent opposition to new development that has the potential to threaten the integrity of existing views and diminish the benefits drawn from those views (Ladenburg and Dubgaard 2009, Haggett 2011).  The InVEST scenic quality model allows users to determine the locations from which new nearshore or offshore features can be seen. It generates viewshed maps that can be used to identify the visual footprint of new offshore development.  Inputs to the viewshed model include: topography and bathymetry, locations of offshore facilities of interest, and the locations of viewers (e.g. population centers or areas of interest such as parks or trails).  The model does not quantify economic impacts of altering the viewshed, but it can be adapted to compute viewshed metrics for use in a more detailed valuation study.  A key limitation of the model is that it does not currently account for the ways in which vegetation or land-based infrastructure may constrain land areas that are visually affected by offshore development.

Scenic Quality Standalone Beta
===============================

Currently we are working on the next generation platform of InVEST (3.0) and deploying parts of it as prototype InVEST models.  You can try out the 3.0 version of Scenic Quality by navigating to your Windows Start Menu -> All Programs -> InVEST +VERSION+ -> Scenic Quality.  The interface does not require ArcGIS and the results can be explored with any GIS tool including ArcGIS, QuantumGIS, and others.

In an earlier version of InVEST this tool didn't measure the economic impact of visual disamenities (i.e. valuation). The new 3.0 version performs valuation, and the user can notice the new *valuation* tab for the new valuation parameters besides the *general* tab that regroups all the parameters in the previous version of the model. 

Introduction
============

Coastal ecosystems are increasingly dominated by human activities.  This rise in human activities can compromise the unique scenic qualities associated with coastal and marine areas.  The coastline and 'seascape' is an important economic asset that attracts visitors for tourism and recreation and contributes to the general quality of life for people living near the coast.  Near and offshore development projects often raise considerable concern within the local communities that value the natural seascape for its inherent beauty.  Visual impacts are external effects that unless measured and accounted for, do not factor into the calculus of weighing the costs and benefits of new coastal development.  Applications using viewshed analysis range from the siting of aquaculture facilities to minimize spatial competition with tourism activities (Perez 2003) to seascape and shoreline visibility assessment of offshore wind projects (Environmental Design and Research 2006).  Because scenic beauty is an attribute generally considered to be important to people living near the coast and for those who visit coastal areas to enjoy the ocean and the marine environment, coastal planners can incorporate measures of visual amenities and/or disamenities into broader policy deliberations and planning exercises.  Because most applications of viewshed analysis involve examining the negative impacts of new facilities, language within the InVEST scenic quality model assumes the objects viewed have a negative impact on views.  However, positive interpretation of viewing these objects can be included with interpretation of model results. 

The InVEST scenic quality model provides users with a simple way to provide information about potential tradeoffs between nearshore and offshore development proposals and the visual impacts of those projects.  The viewshed maps produced by the model can be used to identify coastal areas that are most likely to be directly affected by additions to the seascape.  They can serve as valuable input into broader analyses that consider a range of services provided by the marine environment.

This model can be used to compute the costs associated with offshore visual impacts, these costs are likely to decrease as the location of facilities moves further offshore, while the costs of installing and operating offshore facilities generally increase with distance from the shoreline. The few valuation studies that explore the economic magnitude of visual disamenities resulting from offshore development projects show a complex picture. One recent study found that individuals living along the coast have external costs ranging from $27 to $80 resulting from the visual disamenity of an offshore wind project (Krueger et al. 2010). In contrast, Firestone et al. (2009) found that public acceptance for offshore renewable energy projects is growing and may be less contentious than previously anticipated.


The Model
=========

The scenic quality model provides information about the visibility of offshore objects from the surrounding landscape or seascape.  Offshore and nearshore development projects, such as renewable wave energy facilities or aquaculture facilities, have the potential to impact the visual amenities that are an important feature of many coastal areas.  The results of viewshed analysis will be useful for decision-makers who would like to identify areas where visual impacts may be an important factor to incorporate into planning.  

The model inputs are groupped in two tabs: the **General** tab has all the entries necessary to run the viewshed computation such as the location of a DEM and a point shapefile that identifies the locations of sites that contribute to visual impacts. The **Valuation** tab allows the user to select the functional form of the valuation function, and its parameters. The viewshed analysis is then computed over a user-defined area of interest (AOI).

The model will create as many as four outputs that can be used to assess the visible impact of any type of facility added to the marine environment. The first output, "vshed", is a valuation raster based on the visual quality at any given pixel. If the valuation is set to the constant 1 independent of the viewing distance, the raster reduces to a record of the number of sites (e.g. wave energy facilities or aquaculture farms) that are visible from a given raster cell on the land or seascape. The cells are then classified using quantiles to produce "vshed_qual" with the following class breaks:  1. Unaffected, 2. Low Visual Impact/High Visual Quality, 3. Moderate Visual Impact/Medium Visual Quality, 4. High Visual Impact/Low Visual Quality, 5. Very High Visual Impact/Poor Visual Quality.

The third output computes the resident population that falls within the viewshed of any facility. The model uses the Global Rural-Urban Mapping Project (GRUMP) gridded population of the world data (CIESIN 2004) to compute the number of residents who are unaffected by the facility (or facilities) and the number of residents who live in areas that fall within the viewshed of at least one facility. The population counts are tabulated in the "populationStats.html" file found in the output folder. Users should note that this globally available population data does not account for seasonal or daily users in an area. Alternatively, you can provide your own population raster data.

The final optional output allows for the examination of the visual impacts on areas of interest where the view is of particular concern (e.g. parks, trails, marine reserves). It utilizes a user-defined set of polygons and computes the percent area within each polygon from which at least one offshore site is visible. Each polygon is then classified by the percentage of that polygon’s area that is visually impacted by offshore developments. These results can be used to identify and rank areas according to visual impacts.

Additional files are created for each feature *X* at each step of the computation:
- *visibility_X.tif* is the visibile area raster computed from feature X.
- *distance_X.tif* is the distance in meters from feature X across the visible area in *visibility_X.tif*.
- *viewshed_X.tif* is computed from *distance_X.tif* where the valuation function is applied to the distances.
- *vshed_X.tif* is *viewshed_X.tif* scaled by the coefficient associated to feature X. If no coefficient is specified, the model assumes a coefficient of 1.0, in which case *vshed_X.tif* is identical to *viewshed_X.tif*. The file *vshed.tif* is the sum of each individual *sched_X.tif*.

How it Works
------------
The InVEST scenic quality model computes the visual impact of features in the landscape in four steps:
1. Visibility calculation: the model compute a visibility raster for each point feature *X* (*visibility_X.tif*). It implements a simple line of sight algorithm that only computes visibility along the lines originating from the viewpoint to the center of the perimeter raster cells.
2. Valuation: The model applies a valuation function (either logarithmic or third order polynomial) across the visibility raster using the distance to the point feature (*viewshed_X.tif*).
3. Weighting: Each feature in the point shapefile can have a field *coeff*, which is used to scale the values returned by the valuation function (*vshed_X.tif*).
4. Summation: The weighted rasters are summed up to produce the visual impact output raster *vshed.tif*.

The valuation function is either logarithmic:

.. math:: f(x) = a + b \cdot log(x)
   :label: logarithmic_form

or a third degree polynomial:

.. math:: f(x) = a + b \cdot x + c \cdot x^2 + d \cdot x^3
   :label: polynomial_form

Where *x* is the distance from the cell center to a point feature, and *a*, *b*, *c*, and *d* are coefficients. With the default parameter values (*a=1*, *b=c=d=0*), the model computes an aggregate viewshed. The valuation function is computed up to a maximum valuation radius that defaults to 8000 meters. For short distnaces, the logarithmic and polynomial forms could degenerate to unrealistic high values. To avoid this situation, the model uses a linear function l(x):

.. math:: l(x) = A \cdot x + B
   :label: linear_form

where A = f'(1000) and B = f(1000). Since the function quantifies dollar amounts, it should be positive throughout its range. The model will test if the function is positive at the maximum radius, and return an error if not.

Limitations and Simplifications
===============================

The global DEM included with the scenic quality model does not account for trees, buildings, or other structures that can obscure the view.  If users have a raster layer that represents the locations of trees, buildings, or other obstructions (and their heights) this information can be incorporated into the DEM to create a more realistic surface to obscure or allow views.  The model does account for the curvature of the earth in limiting the line of sight but it does not limit the distance at which objects of varying size and quality may be visible to the human eye in the default settings. As long as there is a straight-line vector that can be computed from a particular DEM grid cells to any offshore point, that grid cell will be counted as visible.  This should be carefully considered when interpreting viewshed impact maps from facilities located far offshore when default settings are used.  However, users can provide an outer radius that limits the search distance when identifying areas visible from each offshore development site. 


.. _ae-data-needs:

Data Needs
==========

The model's interface is composed of two tabs, **General** and **valuation**. The former contains all the inputs necessary to run the basic viewshed analysis (without valuation), as well as additional inputs for population data and specific impacted areas. The latter tab contains the valuation-related inputs. Here we describe each option in more detail.


General Tab
-----------

1. **Workspace (required).**  Users are required to specify a workspace folder path. It is recommend that the user create a new folder for each run of the model. For example, by creating a folder called "runBC" within the "ScenicQuality" folder, the model will create "intermediate" and "output" folders within this "runBC" workspace. The "intermediate" folder will compartmentalize data from intermediate processes. The model’s final outputs will be stored in the "output" folder. ::

     Name: Path to a workspace folder. Avoid spaces. 
     Sample path: \InVEST\ScenicQuality\runBC

2. **Area of Interest (AOI) (required).**  An AOI instructs the model where to clip the input data and the extent of analysis. Users will create a polygon feature layer that defines their area of interest. The AOI must intersect the Digital Elevation Model (DEM). ::

     File type: polygon shapefile (.shp)
     Sample path: \InVEST\ScenicQuality\AOI_WCVI.shp

3. **Cell Size (meters) (optional).**  This determines the spatial resolution at which the model runs and at which the results are summarized. For example, if you want to run the model and see results at a 100m x 100m grid cell scale then enter "100." You can only define a resolution that is equal to or coarser than the model’s native resolution as established by the current DEM (input # 4). If you want to run the model and produce output at the current DEM’s resolution (the model’s native resolution) you can leave this input field blank. The coarser the scale (and larger the number), the faster the model runs. ::

     Type: text string (direct input to the interface)
     Sample (default): 500

4. **Features Impacting Scenic Quality (required).**  The user must specify a point feature layer that indicates locations of objects that contribute to negative scenic quality, such as aquaculture netpens or wave energy facilities. Users wish to including polygons (e.g. clear-cuts) in their analysis must convert the polygons to a grid of evenly spaced points. ::

    File type: point shapefile (.shp)
    Sample path: \InVEST\ScenicQuality\AquaWEM_points.shp

The model will compute a viewshed for each feature separately and aggregate them into a combined viewshed. The user can specify up to three fields (all fields are optional) to assign a maximum viewing distance, a viewshed importance coefficient, or a viewpoint height to each feature:

    - *Maximum viewing distance*: Integer field named either "RADIUS" (preferred, case insensitive) or "RADIUS2" (kept for backwards compatibility) specifying the maximum length of the line of sight in meters originating from a viewpoint. The value can either be positive (preferred) or negative (kept for backwards compatibility), but is converted to a positive number. The model assumes a value of 8000m (8km) if the field doesn't exist.

    - *Viewshed importance coefficient*: The user can assign an importance to each viewshed by scaling them with a real number (either positive or negative) stored in the field "coeff". The model assumes a coefficient of 1.0 if the field doesn't exist.

    - *Viewpoint height*: Each feature elevation above the ground can be specified as a positive real number in the field "height". The default value is 0.0 if the field doesn't exist.

5. **Digital Elevation Model (DEM) (required).**  A global raster layer is required to conduct viewshed analysis. Elevation data allows the model to determine areas within the AOI’s land-seascape where features from input #4 are visible. ::

     Format: standard GIS raster file (e.g., ESRI GRID or IMG), with elevation values
     Sample data set: \InVEST\ScenicQuality\Base_Data\Marine\DEMs\claybark_dem

6. **Refractivity Coefficient (required).**  The earth curvature correction option corrects for the curvature of the earth and refraction of visible light in air. Changes in air density curve the light downward causing an observer to see further and the earth to appear less curved. While the magnitude of this effect varies with atmospheric conditions, a standard rule of thumb is that refraction of visible light reduces the apparent curvature of the earth by one-seventh. By default, this model corrects for the curvature of the earth and sets the refractivity coefficient to 0.13. ::

     Format: A string of numeric text with a value between 0 and 1 
     Sample (default): 0.13

7. **Population Raster (required).**  A global raster layer is required to determine population within the AOI’s land-seascape where features from input #4 are visible and not visible. ::

     Format: standard GIS raster file (ESRI GRID) with population values
     Sample data set (default): \InVEST\Base_Data\Marine\Population\global_pop

8. **Overlap Analysis Features (optional).**  The user has the option of providing a polygon feature layer where they would like to determine the impact of points (input #4) on visual quality. This input must be a polygon and projected in meters. The model will use this layer to determine what percent of the total area of each feature can see at least one of the points from input #4. ::

     File type: polygon shapefile (.shp)
     Sample path: \InVEST\ScenicQuality\BC_parks.shp


Valuation Tab
-------------

9. **Valuation function.** Type of economic function the user wishes to use to quantify the visual impact of disamenities. The coefficients for each function can be specified in the following inputs. ::

     Format: An item selected from a drop-down menu
     Default: Polynomial

10. **'a' coefficient.** Constant value (independent of the distance *x*) used by both the logarithmic and the polynomial functions. It is set to 1.0 by default. ::

     Format: A string of numeric text (direct input to the interface)
     Default: 1.0

11. **'b' coefficient.** Coefficient used by both the logarithmic and the polynomial form. It weights the first order factor in the polynomial form, and the logarithmic factor for the logarithmic function. It is set to 0.0 by default. ::

     Format: A string of numeric text (direct input to the interface)
     Default: 0.0

12. **'c' coefficient.** Coefficient used in the polynomial form only to weight the second order term. It has no effect if the user chooses the logarithmic valuation function. It is set to 0.0 by default. ::

     Format: A string of numeric text (direct input to the interface)
     Default: 0.0

13. **'d' coefficient.** Coefficient that weights the third order factor. It is set to 0.0 by default. ::

     Format: A string of numeric text (direct input to the interface)
     Default: 0.0

14. **Maximum valuation radius.** Valuation will only be computed for cells that fall within the maximum valuation radius. The maximum radius is a positive number in meters. ::

     Format: A string of numeric text (direct input to the interface)
     Default: 8000.0


Running the Model
=================

The model is available as a standalone application accessible from the Windows start menu.  For Windows 7 or earlier, this can be found under *All Programs -> InVEST +VERSION+ -> Scenic Quality*.  The standalone can also be found directly in the InVEST install directory under the subdirectory *invest-3_x86/invest_scenic_quality.exe*.


Viewing Output from the Model
-----------------------------

Upon successful completion of the model, a file explorer window will open to the output workspace specified in the model run.  This directory contains an *output* folder holding files generated by this model.  Those files can be viewed in any GIS tool such as ArcGIS, or QGIS.  These files are described below in Section :ref:`interpreting-results`.

Final Results
-------------


Output Folder
^^^^^^^^^^^^^
+ Output\\vshed_qual

  + This raster layer contains a field that classifies based on quartiles the visual quality within the AOI. The visual quality classes include:  unaffected (no visual impact), high (low visual impact), medium (moderate visual impact), low (high visual impact), and very low (very high visual impact).

  + Additionally, the range of sites visible for each visual quality class is specified in this output's attribute table.

  + This layer can be symbolized by importing the symbology from the file "\\ScenicQuality\\Input\\vshed_qual.lyr"

+ Output\\vshed

  + This raster layer is the original output after the viewshed tool is run. It contains values ranging from 0 to the total number of points visible from each cell on the land or seascape. For example, all cells with a value of "4" would indicate that at that location four points are visible.

  + In order to compare scenario runs, use this layer rather than vshed_qual. By calculating the difference between "vshed" outputs from multiple runs, a user can assess changes in visual quality across scenarios.

+ Output\\vp_overlap.shp

  + This polygon feature layer contains a field called "AreaVShed" which expresses the percentage of area within each polygon where at least one point contributing to negative scenic quality is visible as compared to the total area of that polygon. 

  + This layer can easily be symbolized by importing the symbology from the file "\\ScenicQuality\\Input\\vp_overlap.lyr"

+ Output\\populationStats.html

  + This html file includes a table and indicates the approximate number of people within the AOI that are 1) unaffected (no sites contributing to negative scenic quality are visible) and 2) affected (one or more sites visible).

+ scenic_quality_log-[yr-mon-day-hour-min-sec].txt

  + Each time the model is run a text file will appear in the workspace folder. The file will list the parameter values for that run and be named according to the date and time.

Intermediate Folder
^^^^^^^^^^^^^^^^^^^
+ intermediate\\aoi_dem

  + Reprojected AOI to match the DEM's projection. Used for clipping the DEM to the AOI.

+ intermediate\\dem_vs

  + DEM clipped with the AOI using aoi_dem.

+ intermediate\\dem_vs_re

  + Raster similar to DEM, with negative heights set to zero.

+ intermediate\\vshed_bool

  + Raster where only the pixels spanned by the viewsheds are set to 1, and the others are 0.

+ intermediate\\aoi_pop

  + Reprojected AOI to match the population layer's projection. Used for clipping the population layer to the AOI.

+ intermediate\\pop_clip

  + Population raster clipped to the AOI.

+ intermediate\\pop_prj

  + Clipped population raster reprojected to the original population layer.

+ intermediate\\pop_vs

  + Population raster resampled to the user-defined cell size and aligned to the AOI.


References
==========

Benson E., Hansen, J.,  Schwartz, A., and Smersh, G., 1998. Pricing residential amenities: the value of a view. Journal of Real Estate Research, 16: 55-73.

Bourassa, S., Hoesli, M. and Sun, J. 2004. What’s in a view? Environment and Planning A. 36(8): 1427-1450.

Center for International Earth Science Information Network (CIESIN), Columbia University; International Food Policy Research Institute (IFPRI); The World Bank; and Centro Internacional de Agricultura Tropical (CIAT). 2004. Global Rural-Urban Mapping Project (GRUMP), Alpha Version: Population Grids. Palisades, NY: Socioeconomic Data and Applications Center (SEDAC), Columbia University. Available at http://sedac.ciesin.columbia.edu/gpw. (downloaded on 1/6/2011).

Environmental Design and Research, P.C. 2006. Seascape and shoreline visibility assessment. Cape Wind Energy Project. Cape Cod, Martha’s Vineyard, and Nantucket, Massachusetts. Prepared for Cape Wind Associates, L.L.C. Boston, Mass. Syracuse, N.Y. July 2006.

Firestone, J., Kempton, W. & Krueger, A., 2009. Public acceptance of offshore wind power projects in the USA. Wind Energy, 12(2):183-202. 

Haggett, C. 2011. Understanding public responses to offshore wind power. Energy Policy. 39: 503-510.

Krueger, A., Parson, G., and Firestone, J., 2010. Valuing the visual disamenity of offshore wind power at varying distances from the shore: An application of on the Delaware shoreline. Working paper. Available at: http://works.bepress.com/george_parsons/doctype.html.

Ladenburg, J. & Dubgaard, A., 2009. Preferences of coastal zone user groups regarding the siting of offshore wind farms. Ocean & Coastal Management, 52(5): 233-242. 

Perez, O.M., Telfer, T.C. & Ross, L.G., 2005. Geographical information systems-based models for offshore floating marine fish cage aquaculture site selection in Tenerife, Canary Islands. Aquaculture Research, 36(10):946-961. 

Sander, H.A. & Polasky, S., 2009. The value of views and open space: Estimates from a hedonic pricing model for Ramsey County, Minnesota, USA. Land Use Policy, 26(3):837-845. 


