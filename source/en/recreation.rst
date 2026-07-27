.. _recreation:

**********************************
Visitation: Recreation and Tourism
**********************************

Summary
=======

Recreation and tourism are important components of many national and local economies and they contribute in innumerable ways to quality of life, sense of place, social connection, physical wellbeing, learning, and other intangibles. To quantify the value of natural environments, the InVEST recreation model predicts the spread of person-days of recreation, based on the locations of natural habitats and other features that factor into people's decisions about where to recreate. The tool estimates the contribution of each attribute to visitation rate in a simple linear regression. In the absence of empirical data on visitation, we parameterize the model using a proxy for visitation: geotagged photographs posted to the website Flickr and geotagged tweets posted to Twitter. Using photo-user-day (PUD) and twitter-user-day (TUD) estimates, the model predicts how future changes to natural features will alter visitation rates. The tool outputs maps showing current patterns of recreational use and maps of future patterns of use under alternate scenarios.

**The Recreation model is designed to answer these basic questions:**  

1) What are the *relative* visitation rates across a landscape or across a set of sites?  

2) Which features of the natural/built environment influence the spatial pattern of the visitation rates, and what are the relative levels of influence of those features?  

3) Given a new scenario where the spatial patterns of the natural/built features have changed, how will the visitation rates change in response?  

Introduction
============

Recreation and tourism are important components of many national and local economies and they contribute in innumerable ways to quality of life, sense of place, social connection, physical wellbeing, learning, and other intangibles. A key reason for studying patterns of recreation or tourism is the economic significance of this industry. The total contribution of travel and tourism to the world's gross domestic product (GDP) in 2011 was approximately $6 B USD (9% of GDP), with expected growth to $10 B USD by 2022 (World Travel and Tourism Council 2012). Of course, economic impacts are only one way of measuring the importance of recreation and tourism. These activities are critical contributors to diverse aspects of human wellbeing (Russell et al. 2013). For example, outdoor recreation is a spiritual experience for many people (eg Trainor and Norgaard 1999), and social interactions in nature contribute to building a sense of place (e.g. Willox et al. 2012).

A major and growing portion of recreation is "nature-based", involving interactions with or appreciation of the natural environment (Balmford et al. 2009). For these types of activities, characteristics of the environment influence people's decisions about where, when, and how to recreate. SCUBA divers, for example, select destinations based on the water clarity, water temperature, and diversity of marine life (Williams and Polunin 2000, Uyarra et al. 2009). Bird-watchers are drawn to the best places to see target species (Naidoo and Adamowicz 2005), which inevitably are places where natural systems support populations of desirable birds (Puhakka et al. 2011). Some recreation depends on environmental attributes such as species richness (Loureiro et al. 2012), the diversity of habitats (Neuvonen et al. 2010, Loureiro et al. 2012), precipitation (Loomis and Richardson 2006), and temperature (Richardson and Loomis 2005), as well as to other attributes such as infrastructure and cultural attractions (Mills and Westover 1987, Hill and Courtney 2006).

.. _rec-the-model:

The Model
=========

The purpose of the InVEST recreation model is to predict the spread of person-days of recreation and tourism, based on the locations of natural habitats, accessibility, and built features that factor into people's decisions about where to recreate (Adamowicz et al. 2011). The tool outputs maps showing current patterns of recreational use and, optionally, maps of future use under alternative scenarios.

.. _rec-how-it-works:

How it Works
------------

The model displays rate of visitation across landscapes (grid cells) or in discrete areas (polygons) and optionally builds a regression model to estimate the contribution of attributes of the landscape to the visitation rate, using a simple linear regression:

.. math:: y_i = \beta_{0} + \beta_1 x_{i1} + ... + \beta_{p} x_{ip} \text{ for } i = 1 ... n,

where :math:`x_{ip}` is the coverage of each attribute in each cell or polygon (hereafter called 'cell'), :math:`i`, within an Area of Interest (AOI) containing :math:`n` cells. In the absence of empirical data on visitation for :math:`y_i`, we parameterize the model using crowdsourced measures of visitation: geotagged photographs posted to the website Flickr and geotagged tweets posted to Twitter (see :ref:`rec-userdays` section for more information). Stated again, the InVEST recreation model predicts the spread of person-days of recreation in space. It does this using attributes of places, such as natural features (eg habitat distributions), built features (eg roads), and human uses (eg industrial activities), among others.

The response variable :math:`y_i` is a logit-transformation of the proportion of userdays in each cell (see :ref:`rec-userdays`). Then, a simple linear regression is performed to estimate the effect of each attribute on visitation rates across all grid cells within the study region. These estimates (the :math:`\beta_{p}` values) can be used for an additional scenario, to predict how future changes to the landscape will alter visitation rate. The model uses ordinary least squares regression, performed by the linalg.lstsq function in python's numpy library (van der Walt et al. 2011).

.. _rec-userdays:

User Days
---------

Since fine-scale data on numbers of visitors is often only collected at a few specific locations in any study region, we assume that current visitation can be approximated by the total number of annual person-days represented by photographs uploaded to the photo-sharing website `Flickr <https://www.flickr.com>`_ and tweets shared on the Twitter social media platform (currently known as X). Many of the photographs in Flickr and tweets have been assigned to a specific latitude/longitude. Using this location, along with the author's user-name and date that the image/tweet was made, the InVEST model counts the total photo-user-days (PUD) and twitter-user-days (TUD) for each grid cell or polygon.

One user-day at a location is one unique person who took at least one photo/tweet on a specific day. For each cell, the model sums the number of photo-user-days and twitter-user-days for all days from 2012-2017 (or a user-defined range within those years). It reports the total PUD and TUD for each year, and the average annual PUD and TUD (PUD_YR_AVG and TUD_YR_AVG). In the equation above, the response variable, :math:`y_i`, is a logit transformation of a proportion::

  # The proportion in each cell i
  pr_PUD[i] = PUD_YR_AVG[i] / PUD_YR_AVG.sum()
  pr_TUD[i] = TUD_YR_AVG[i] / TUD_YR_AVG.sum()
  avg_pr_UD[i] = (pr_PUD[i] + pr_TUD[i]) / 2

  epsilon = avg_pr_UD[avg_pr_UD > 0].min() / 2 # half the minimum non-zero value
  avg_pr_UD[avg_pr_UD == 0] = epsilon          # adjust because zeros cannot be log-transformed
  
  # Logit-transform:
  y = ln(avg_pr_UD / (1 - avg_pr_UD))

We have observed that the number of recreators who visit a location annually is related to the number of photographs taken in the same area and uploaded to the Flickr database at 836 visitor attractions worldwide (Wood et al. 2013). The density of photographs and tweets varies spatially, and this has ramifications for the cell-size that can be chosen for analysis (see :ref:`rec-data-needs`: Cell size). User-day calculations are computed on a remote server on an extensive global dataset curated and maintained by The Natural Capital Alliance.


Predictor Variables
-------------------

In the regression equation above, photo-user-days are the :math:`y_i` variable and all the :math:`x` variables on the right side are predictor variables. These are features in the Area of Interest that are likely to influence the visitation patterns across space. Users may provide any number of predictor variables and the model will compute a regression that estimates :math:`\beta_{p}` values for each predictor. :math:`\beta_{p}` indicates the relationship between a predictor variable and the visitation rate, after accounting for all other predictor variables included in the regression.

We find that it often helps to consider at least one predictor variable from several main categories: natural capital (eg habitats, lakes), built capital (eg roads, hotels), industrial activities, and access or cost (eg distance to major airport). Often, single variables representing each of these categories can explain the majority of variation in photo-user-days. This tool allows users to provide predictor variables in GIS formats and to process those layers in a variety of ways (described in the :ref:`rec-data-needs` section).

Scenario Analysis
-----------------

If a regression is computed, the model can optionally estimate visitation rates given a set of modified predictors that represent a future or alternative scenario. Scenario predictors should represent the same features that were selected as Predictor Variables, but may represent modified versions of those features (e.g. modified road networks, additional hotel points, altered habitat distributions, etc). Scenario predictions are made using the regression equation above. First, coefficients for each predictor variable are estimated as described in :ref:`rec-how-it-works`, then those coefficients are applied to the values of each predictor that has been modified for a scenario. See :ref:`rec-data-needs` section for more details on preparing scenario data.


Limitations and Simplifications
===============================

The model does not presuppose that any predictor variable has an effect on visitation. Instead, the tool estimates the magnitude of each predictor's effect based on its spatial correspondence with current visitation in the area of interest. The values of photo-person-days per cells are taken as a measure of visitation and are regressed against the values of the predictor variables across all cells. When a Scenario Predictor Table is provided, the tool uses the :math:`\beta_{p}` values computed for the Predictor Table, and applies them to the future scenario predictors. This step requires the assumption that people's responses to attributes that serve as predictors in the model will not change over time. In other words, in the future, people will continue to be attracted to, or repelled by, the predictors in the same way they are currently.


.. _rec-data-needs: 

Data Needs
==========

.. note:: All GIS data referenced in the Predictor Table must be in the same *projected* coordinate system as the Area of Interest (AOI) vector. All distance, length, and area calculations use the same units as the AOI coordinate system.

- :investspec:`recreation.recmodel_client workspace_dir`

- :investspec:`recreation.recmodel_client results_suffix`

- :investspec:`recreation.recmodel_client aoi_path` It is recommended that this vector be projected in linear units, especially if it is used to calculate a regression and scenario. Results are aggregated to these polygons.

- :investspec:`recreation.recmodel_client start_year`
- :investspec:`recreation.recmodel_client end_year`

- :investspec:`recreation.recmodel_client compute_regression` If this is not selected, the results will be limited to a map of current visitation rates in the AOI polygons or grid cells.

- :investspec:`recreation.recmodel_client predictor_table_path` These predictors are the :math:`x_{ip}` values described in :ref:`rec-how-it-works`.

    Columns:

    - :investspec:`recreation.recmodel_client predictor_table_path.columns.id`
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.path` In the example below, the files listed in the path column are located in the same folder as the Predictor_Table.csv file. Predictor files may be located in other places, but either the full path to them must be included in this table or the path relative to this CSV file.
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.type`

    **Example Predictor Table:**
    
    .. csv-table::
       :file: ../../invest-sample-data/recreation/predictors.csv
       :header-rows: 1
       :widths: auto

- :investspec:`recreation.recmodel_client scenario_predictor_table_path` This table has the same columns and format as the Predictor Table described above.

- :investspec:`recreation.recmodel_client grid_aoi`

- :investspec:`recreation.recmodel_client grid_type`

- :investspec:`recreation.recmodel_client cell_size` The cell size is **in the same linear units as the AOI**. For example, if the AOI is in a UTM projection with units of meters, the cell size parameter will also be in meters.

   .. note:: The number of grid cells greatly affects processing time. If you are unsure what cell size to specify, choose a very large size the first time (10 km or more), and then re-run the model with smaller sizes if necessary. The appropriate size and number of cells depends on several factors, including the goals of the study and the density of photographs, which varies from region to region. In order for the model to compute the effects of predictor variables (as described in the :ref:`rec-how-it-works` section), users must select a sufficiently large cell size such that the majority of cells contain photographs. We recommend that users begin by running the model with cell sizes ranging between 10-100 km, depending on the total area of the AOI. Then, iteratively assess the model outputs (described in :ref:`rec-interpreting-results`) and re-run the model to determine an appropriate cell size.


.. _rec-running-model:

Running the Model
=================

.. warning:: The recreation model requires a connection to the internet.

The model uses an interface to input all required and optional data (see :ref:`rec-data-needs`). The AOI is sent to a server managed by the Natural Capital Alliance, where PUD and TUD computations are performed. Consequently, this model requires a connection to the internet. The model may be run with three configurations:

#. Get a map of visitation rates in your Area of Interest. Provide a "Workspace" and "Area of Interest", do not check "Compute Regression". Results include "pud_results.gpkg", "tud_results.gpkg", and "regression_data.gpkg" (:ref:`rec-interpreting-results`).
#. Get a map of visitation rates and compute a regression with one set of predictors. Provide a "Workspace" and "Area of Interest", check "Compute Regression" and provide "Predictors Table" :ref:`rec-data-needs`. Additional results include "regression_data.gpkg", "regression_coefficients.csv" and "regression_summary.txt" (:ref:`rec-interpreting-results`).
#. Estimate visitation rates for a Scenario. Provide a "Workspace" and "Area of Interest", check "Compute Regression" and provide "Predictors Table" and "Scenario Predictors Table" (:ref:`rec-data-needs`). Additional results include "scenario_results.gpkg" (:ref:`rec-interpreting-results`).

The time required to run the model varies depending on the extent of the AOI, the number grid cells, and the number and size of predictor layers. We advise users to run the model first without computing a regression, and to start with a large cell size if gridding the AOI.

Please note, the server performing the analysis also records the IP address of each user.


.. _rec-interpreting-results:

Interpreting Results
====================

Model Outputs New
-----------------
- :investspec:`recreation.recmodel_client workspace_dir`

Model Outputs
-------------

+ **PUD_results.gpkg**: The features of this polygon geopackage match the original AOI, or the gridded version of the AOI if the "Grid the AOI" option was selected. The attributes include:

  + **PUD_YR_AVG** is the average photo-user-days per year (:ref:`rec-userdays`). This corresponds to the average *PUD* described in Wood et al. (2013).

  + **PUD_JAN**, PUD_FEB, .... PUD_DEC is the average photo-user-days for each month. For example, if the date range is the default 2012-2017, then PUD_JAN is the average of all six January's photo-user-days.

+ **PUD_monthly_table.csv**:  

  + This table contains the total photo-user-days counted in each cell for each month of the chosen date range. Each row in this table is a unique AOI grid cell or polygon. Columns represent months ("2012-1" is January 2012, "2017-12" is December 2017).

+ **TUD_results.gpkg**: See the description of **PUD_results.gpkg**, but instead of photo-user-days, this file contains counts of twitter-user-days.

+ **TUD_monthly_table.csv**: See the description of **PUD_monthly_table.csv**, but instead of photo-user-days, this file contains counts of twitter-user-days.

+ **regression_data.gpkg**: AOI polygons with all the variables needed to compute a regression, including predictor attributes and the user-days response variable. The fields include:
    
    + **pr_PUD**: the proportion of the sum of PUD_YR_AVG across all features

    + **pr_TUD**: the proportion of the sum of TUD_YR_AVG across all features

    + **avg_pr_UD**: average of pr_PUD and pr_TUD. This variable is logit-transformed and then used as the response variable in the regression model.
    
    + If Compute Regression is selected, there will be one field for each predictor defined in the Predictor Table. The values of those fields are based on the metric defined in the Predictor Table. (:ref:`rec-data-needs`: Predictor Table).

+ **regression_summary.txt** (output if Compute Regression is selected):

  + This is a text file output of the regression analysis. It includes :math:`\beta_p` estimates for each predictor variable (see :ref:`rec-how-it-works`). It also contains a “server id hash” value which can be used to correlate the PUD and TUD result with the data available on the server. If these results are used in publication this hash should be included with the results for reproducibility.

+ **regression_coefficients.csv** (output if Compute Regression is selected):
  
  + Tabular output of the coefficient estimates also included in "regression_summary.txt"

+ **scenario_results.gpkg** (output if Scenario Predictor Table is provided):

  + This geopackage matches "regression_data.gpkg", but its fields come from the predictors defined in the Scenario Predictor Table and there is an additional field:

  + **pr_UD_est**: The estimated **avg_pr_UD** for each polygon. Estimated using the regression coefficients for each predictor in **regression_coefficients.csv**

+ **natcap.invest...client-log...txt** 

  + This text file is the log automatically produced any time the model is run. It can be useful for troubleshooting errors. At the top of the log is also a record of all the input values selected for that model run.


.. _rec-references:

References
==========

Adamowicz, WL, R Naidoo, E Nelson, S Polasky, J Zhang. 2011. Nature-based tourism and recreation. In: Kareiva P, G Daily, T Ricketts, H Tallis, S Polasky (eds) Natural Capital: Theory and Practice of Mapping Ecosystem Services. Oxford University Press, New York.

Balmford, A, J Beresford, J Green, R Naidoo, M Walpole, A Manica. 2009. A global perspective on trends in nature-based tourism. PLoS Biology 7: e1000144.

Hill, GW, PR Courtney. 2006. Demand analysis projections for recreational visits to countryside woodlands in Great Britain. Forestry 79: 18-200.

Loomis, JB, RB Richardson. 2006. An external validity test of intended behavior: comparing revealed preference and intended visitation in response to climate change. Journal of Environmental Planning and Management 49: 621-630.

Loureiro, ML, F Macagno, PA Nunes, R Tol. 2012. Assessing the impact of biodiversity on tourism flows: an econometric model for tourist behaviour with implications for conservation policy. Journal of Environmental Economics and Policy 1: 174-194.

Mills, AS, TN Westover. 1987. Structural differentiation: a determinant of park popularity. Annals of Tourism Research 14: 486-498.

Naidoo, R, WL Adamowicz. 2005. Biodiversity and nature-based tourism at forest reserves in Uganda. Environment and Development Economics 10: 159-178.

Neuvonen, M, E Pouta, J Puustinen, T Sievänen. 2010. Visits to national parks: effects of park characteristics and spatial demand. Journal for Nature Conservation 18: 224-229.

Puhakka, L, M Salo, IE Sääksjärvi. 2011. Bird diversity, birdwatching tourism and conservation in Peru: a geographic analysis. PLoS One 6: e26786.

Richardson, R, JB Loomis. 2005. Climate change and recreation benefits in an alpine national park. Journal of Leisure Research 37: 307-320.

Russell, R, AD Guerry, P Balvanera, RK Gould, X Basurto, KM Chan, S Klain, J Levine, J Tam. 2013. Humans and nature: how knowing and experiencing nature affect well-being. Annual Review of Environment and Resources 38: in press.

Trainor, SF, RB Norgaard. 1999. Recreation fees in the context of wilderness values. Journal of Park and Recreation Administration 17: 100-115.

Uyarra, MC, AR Watkinson, IM Côté. 2009. Managing dive tourism for the sustainable use of coral reefs: validating diver perceptions of attractive site features. Environmental Management 43: 1-16.

van der Walt, Stéfan, S. Chris Colbert, and Gaël Varoquaux. 2011. The NumPy Array: A Structure for Efficient Numerical Computation. Computing in Science & Engineering 13 (2): 22–30. 

Williams, ID, NV Polunin. 2000. Differences between protected and unprotected reefs of the western Caribbean in attributes preferred by dive tourists. Environmental Conservation 27: 382-391.

Willox, AC, SL Harper, JD Ford, K Landman, K Houle, V Edge. 2012. "From this place and of this place:" climate change, sense of place, and health in Nunatsiavut, Canada. Social Science and Medicine 75: 538-547.

Wood, SA, AD Guerry, JM Silver, M Lacayo. 2013. `Using social media to quantify nature-based tourism and recreation <https://www.nature.com/articles/srep02976>`_. Scientific Reports 3: 2976.

World Travel and Tourism Council. 2012. `Travel and Tourism: Economic Impact <http://www.ontit.it/opencms/export/sites/default/ont/it/documenti/files/ONT_2012-03-23_02800.pdf>`_.
