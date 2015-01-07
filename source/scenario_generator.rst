.. _scenariogenerator:

.. |addbutt| image:: ./shared_images/addbutt.png
  :alt: add
	 :align: middle 
	 :height: 15px

.. |toolbox| image:: ./shared_images/toolbox.jpg
  :alt: toolbox
	 :align: middle 
	 :height: 15px

******************
Scenario Generator
******************

Summary
=======

Introduction
============

Scenarios are storylines that depict future events and states. They provide insight into the future and help shape imagination about uncertain future events. For scenarios to have the desired effects and applicability, they must be plausible, the audience must be able to relate to the possibility of such an event occurring otherwise they run the risk of being dismissed. There are several definitions of scenarios but as described in the InVEST scenario guidelines, scenarios describe a possible future, reflect important and uncertain future developments or choices, are plausible, internally consistent, and relevant to the questions being addressed. Scenarios are used in many fields and take different forms but in this context, we consider scenarios that can be expressed in a spatially explicit manner and that relates to land cover.

Land use and changes in it is an issue of global importance. Land use/Land cover change is driven by the need to provide food, shelter and the rise in economic development among many other factors that change quickly and grow complex day by day. Scenarios of land cover change are important for raising awareness on the possible consequences of land cover change that is driven by todays actions. In the context of ecosystem services, the potential change in the provision of ecosystem services under various scenarios is an important way of evaluating the impact of these alternatives and alerting decision makers on the consequences of loss. 

While land use change modeling is very important, it is complex and requires incorporation of social, political and economic factors that drive the change in land use/land cover. However, incorporating such factors is hampered by methodological difficulties and lack of spatially explicit data (Veldkamp and Lambin 2001). Due to this complexity, proxy variables, which are easier to measure (e.g. distance to roads) are used in place of the actual drivers. This approach runs the risk of obscuring causality, but provides simple direct pathways into understanding such a complex issue. 

This scenario generation tool provides a relatively simple method of generating scenarios based on land suitability. It works on the principle that changes on land occur on areas that are relatively more suitable. The tool combines stakeholder input of transition likelihood with physical factors that determine suitability to generate simple maps that depict future land cover. At the heart of it is land suitability analysis.

Land suitability analysis has developed over the years starting from the early hand drawn maps advancing to computer assisted overlay mapping, multi criteria evaluation and currently artificial intelligence methods (Collins et. al. 2001). With modern developments in Geographic Information Systems (GIS), overlay analysis is commonplace and possible with almost every GIS software. One of the main limitations of classical overlay mapping and modeling approaches is the difficulty in incorporating value judgments such as decision maker preferences and underlying policy driver influence (Malczewski 2004). Combining GIS with multi criteria evaluation – a method of evaluating various criteria in decision-making makes it easier to incorporate expert knowledge into such analyses. Others have favored artificial intelligence (AI) methods which mimic human intelligence without claiming an understanding of the underlying processes (Malczewski 2004). Such techniques include fuzzy logic, neural networks, genetic algorithms and cellula automata. These methods have been criticized for their black box nature of analysis, making them difficult to be easily accepted by decision makers. This tool uses a combination of overlay analysis, multi-criteria evaluation methods and direct application of expert knowledge to map alternative futures.

The Model
=========

How it Works
------------

Allocating land parcels to various uses is a multi-objective multi-criteria problem. There are a large number of drivers (objectives), which influence land cover change. Some of these drivers are very clear and easy to observe (e.g. mineral exploration and extraction) while others are subtle and difficult to identify (e.g. change in societal values). As a participatory process, this scenario-building tool relies on drivers that stakeholders can easily identify and estimate impacts of. At the same time, there are many factors that influence suitability of land parcels for conversion. This may include factors or constraints such as slope, soil type, distance to roads, distance to markets, rainfall distribution, and access. Dealing with multiple objectives and multiple criteria presents a challenge that this tool attempts to solve.

This tool is designed to work with data from experts/stakeholders typically in a workshop setting. The major components of the input are i) the transition likelihood, ii) the physical and environmental factors that influence change and iii) the quantity of anticipated change under a given scenario. The tool works off of a single land cover map making it useful in data poor situations. 

The following are the details of the elements needed to run the tool.

Quantity of Change
^^^^^^^^^^^^^^^^^^

The quantity of change is determined indirectly by the demand for land and is estimated by stakeholders. The change value provided here is used as the goal and the tool converts all suitable pixels in order of priority until this goal is met for the cover or until all the available pixels are converted. For cover types that do not already exist in the initial landcover, the change quantity should be entered in absolute area units (Hectares). While this guide does not give explicit directions on how to estimate this quantity, users can use a variety of methods based on the level of sophistication they desire. As an example, the workshop facilitator or modeler can run an analysis of past land cover change to provide a basis of the magnitudes of change that are plausible in the landscape. However, the final values used in the tool should be determined by stakeholders and could differ from such empirical data. If taking a purely empirical modeling approach then there are other tools that may be better suited.

Transition Likelihood
^^^^^^^^^^^^^^^^^^^^^

The likelihood that a given parcel is converted from one land cover type to another (transition likelihood) is defined by the stakeholders. This exercise is preferably done in a group setting. The stakeholders should select a few well understood transitions and determine how likely they are in the period under consideration. For example, they may consider the likelihood of grassland being converted to agriculture and on a scale of 0 to 10, and assign a value of 8. It is important that when doing this exercise the stakeholders consider the drivers which influence such a change and not consider constraints such as protection because these are considered separately.

Following is an example of the transition likelihood matrix:

.. csv-table::
 :file: scenario_transition.csv
 :name: Scenario Transition Table

The absolute value of the numbers in the matrix above is not critical because they are used relatively. It is important though to have these in the range that is used when creating the suitability maps (using factors as discussed later). Reading the columns, cover A will grow and all of its growth will be from cover C; Cover B will grow due to a contribution from Cover A and a smaller contribution from Cover B. As currently written, in this case cover B will only grow into cover C after all the available parcels in cover A are exhausted. 

Priority
^^^^^^^^

This tool requires that the stakeholders rank the land cover types so that a weighting can be assigned. When multiple objectives compete for a single land parcel (or pixels as unit used in this tool), the one with the higher weight or priority wins. Priority ranking the cover types is difficult, and an optional feature is provided which utilizes a pair-wise comparison matrix in an analytic hierarchy process (AHP), such that the stakeholders only compare two cover types at a time. Using AHP is optional.

As an example, in the table below, using the 9 point continuous scale (see at end of document), Cover C is *"extremely less important"* compared to Cover A (1/9 versus 1). However, cover C is *"strongly more important"* compared to Cover B. Once the table has been filled the tool uses eigenvectors to assign weights to each of the cover types. It is recommended to use the 9 point continuous scale (Saaty 1977). Alternatively, one can derive the weights using any other tools and enter them directly. The cover type that has the highest weight will have its goal achieved before moving to the next. It is important to note that when the priorities are calculated, the input table is not updated but the calculated values are used by the tools when doing conversion.

.. csv-table::
 :file: scenario_priority.csv
 :name: Scenario Priority Table

Factors
^^^^^^^

The transition likelihood values given in table 1 are based on expert opinion and policy drivers. However, there are physical and environmental factors which determine the suitability of pixels for conversion hence determining where on the landscape the land cover changes are likely to happen. Some examples of such factors are distance from roads, soil types, distance from cities, elevation, slope and aspect. The tool allows the user to provide these factors and define their relationship with land suitability. The impact of these factors differ between objectives (cover types here) therefore the user is allowed to enter a set of factors for each of the cover types as desired. Combining these factors to determine the areas most suitable for expansion of the land cover type requires the use of multi criteria evaluation. The user creates raster layers for each of the factors, with suitability values ranging from 0 (unsuitable) to 10 (extremely suitable). There are many ways for deriving these layers and this is left to the discretion of the user. Factors are then weighted against each other (as above) and a matrix similar to the one below is created. Selection of factors is very critical to producing plausible scenario maps. Using factors in the tool is optional and it is advised that a good dataset is used otherwise the results can be inconsistent. Given the iterative nature of scenario development, users should run the tool multiple times with and without the factors to see the effects and adjust as necessary.

.. csv-table::
 :file: scenario_factors.csv
 :name: Scenario Factors Priorities Table

The matrix above is used to compute the suitability. There will be as many suitability layers as the number of cover types (objectives) being considered, with values closer to 10 showing pixels that would be converted first.

Proximity Suitability
^^^^^^^^^^^^^^^^^^^^^

Pixels close to a land cover type may be more likely to be converted to that cover type. For example, parcels close to agriculture, if suitable for agriculture may be most likely to be converted first. However, this may not be the case for all cover types therefore the user is given the option to mark a cover type as having proximity suitability. While this proximity may play an important role in improving suitability of parcels, the effect is limited capped in this tool so that it does not drive the suitability significantly. To apply the effect of proximity, the distance of each cell to the cover being analyzed is computed and made to diminish upto the maximum distance entered by the user. The cells closest to the cover are given the highest value while those farther than the maximum distance given a value of 1. When combining with the rest of the suitability layers, the effect of the proximity distance is made to slightly improve suitability.

Constraints
^^^^^^^^^^^

Constraints are unique factors that prevent human induced land cover change. An example of a constraint is a protected area. However, protected areas have different designations which determine their ability to prevent land cover change. Even where they are gazetted as "strictly protected", on the ground implementation may vary. Therefore the tool allows the user to enter an access value that determines the extent to which the protected area would effectively prevent habitat conversion under the scenario in consideration. An access value of 0 implies that the constraint has full effect and no conversion can take place within the boundary of the constraint while a value of 1 implies that the constraint has no effect. When applied to a suitability layer, a constraint of 0 makes all the parcels with which it overlaps to have a suitability of 0 thereby not having any chance of attracting any changes. An example of another type of constraint, albeit more complex is a requirement that only parcels beyond a specific area can be converted to large scale agriculture. If such a constraint is applied, any suitable regions (group of pixels) that do not meet the minimum requirement are ignored.

Change Override
^^^^^^^^^^^^^^^

While the methods described above use computational methods to change pixels and present a probable scenario land cover, there are times when the user prefers to have an exception and to override these methods to change pixels. The tool allows the user to enter an override GIS layer, which converts pixels as stated. At the simplest, supplying a land cover dataset and an override layer can be used to change specific defined polygons, in this case the scenario tool acts as a simple GIS operation tool. Currently only one vector override layer is accepted therefore if using multiple layers they need to be combined.

Computing Transition
^^^^^^^^^^^^^^^^^^^^

The final step in the procedure is to convert the pixels (land allocation). This tool performs land cover transition by converting the suitability rasters into an array and processing each pixel converting them based on their suitability values. Starting from the cover type with the highest priority, the goal (%change) is read and pixels converted starting from the highest suitability. After each cover is processed, the converted pixels are masked so that they are not available for conversion again. Where more pixels of the same suitability are available, the tool randomly selects the available pixels from the first group (region) that it encounters.

Example
~~~~~~~

As an illustration of the procedure, consider a 5 by 5 pixel landscape undergoing agricultural expansion pressure. There are a few important transitions here: 

#. Forest -> Agriculture (very likely, 8)
#. Forest -> Urban (extremely likely, 10)
#. Grassland -> Agriculture (likely, 5)
#. Grassland -> Urban (very likely, 8)
#. Agriculture -> Urban (a little likely, 3)
#. Urban -> Agriculture (very seldom likely, 1)

At a stakeholder workshop (or other expert forum), the transitions above are discussed and the drivers that determine them are considered. The stakeholders likelihood values above are entered in a matrix as below.

.. csv-table::
 :file: scenario_likelihood.csv
 :name: Scenario Transition Likelihood Table

After considering the driving forces (drivers) and the demand, stakeholders place a goal of 40% growth of agriculture and 100% growth of urban areas. Further, they determine that agriculture has higher priority than urban development so they are assigned values of 10 and 5 respectively. Since these values are relative, the absolute values do not matter. Where a cell (parcel) is more suitable for both agriculture and urban development, the agriculture wins due to higher priority.

This simple example considers only the likelihood matrix but the tool has a provision for incorporating physical and environmental characteristics, which also determine the likelihood of land cover conversion. Even when both the likelihood matrix and the factors are applied, the tool allows adjustment of the contribution of each to the final suitability grid that is used for conversion.


.. figure:: ./scenario_generator_images/change.png
   :align: center
   :figwidth: 400pt


Process explanation:

#. The objective is growth of agriculture with a goal of 40% increase (4 pixels) and growth of urban by 100% (1 pixel)
#. Cells A1, A2, B1, B2 are protected so no changes occur. The tool allows entering intermediate values of protection to control suitability for conversion
#. Agriculture and urban cells are masked because they are not converting
#. Cells with highest suitability scores (8) are converted first followed by lower suitability until goal is met or until possible cells run out
#. Proximity suitability is applied that is cell E3 is taken before C1 even though they have the same suitability 
#. Cells D2 and E3 have the same suitability and proximity so one is picked at random
#. This procedure is repeated for each cover type (objective) starting from the highest priority to the lowest


Tool Process
~~~~~~~~~~~~


.. figure:: ./scenario_generator_images/process.png
   :align: center
   :width: 400pt


Tool Flow
~~~~~~~~~


.. figure:: ./scenario_generator_images/transition.png
   :align: center
   :width: 400pt


Limitations and Simplifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Land cover change analysis is complex and most methods only try to approximate possible futures. This model captures expert knowledge and makes an attempt at representing plausible land cover change as realistically as possible but does not predict the future land cover. One of the aims of the tool is to make it easy for stakeholders to understand how the decisions they make in building the scenarios are reflected in the map produced.

Following are some limitations/assumptions:

#. This model assumes that a cover type is either growing or shrinking but not both. In reality, conversion takes place in both directions but for simplicity, only one direction is assumed.
#. This tool assumes a single step transition from the beginning landcover to the scenario landcover. In reality these changes could be stepwise with different patterns at each step.
#. Stakeholder values are likely to be more reliable for near future scenarios but not for longer term ones. Therefore, it is advisable to stay with near future.
#. Currently this tool only processes covers that are growing and disregards the shrinking covers. For example, even though a percentage change may be entered as -5%, the pressure of the growing covers always override. In a future revision this will be addressed.

Data Needs
==========

#. **Base Land cover:** Land cover data in raster format.  While the number of land cover classes can be unlimited, for this analysis it gets confusing for stakeholders and becomes problematic to process a large number of land cover classes.  Its preferable to keep them under 20. Stakeholders should be able to describe each of the covers especially those that are transitioning.
#. **Landcover transition table:** The land cover transition table contains the transition likelihoods on a scale of 0 to 10 where 0 indicates no likelihood of change and 10 indicates full likelihood of change.  The rows indicate the land cover types.  For each land cover type in the row, there is a matching field named <cover id> where the cover id matches the id in the row as shown in the example below.  This currently supports csv format.  This table has two additional fields:
  #. Priority (weight): If the user has priority for the cover types, they should be entered here otherwise the optional Compute Priority option should be used to populate this field. The cover types with higher weight will be allocated pixels before those with lower weight.
  #. Percent Change: This shows the quantity of change and should be a positive or negative integer.  Cover types that will lose area should have negative values while those gaining should have positive values.  The negative values are only used to check the balance of the change and not used in computing the transition.  This is a limitation.
  #. Proximity: If proximity suitability is to be applied to this cover type, enter the proximity distance else leave it as 0. The proximity distance is a value in meters that indicates how far the effect of self proximity goes.  For example, fields that are within 10km of small scale agriculture may be likely to be converted to agriculture if they are suitable but after this distance the effect of proximity disappears. In this case a value of 10000 should be entered.
  #. Area Change (optional): For cover types that do not already exist, percentage change cannot be used. To introduce a new cover, enter the new quantity in hectares.
  #. Patch ha (optional): This is an optional value that indicates the minimum size of a patch that is suitable for the cover to be allocated the parcel.  If not entered, a default value of 1 pixel is used.

.. csv-table::
 :file: scenario_transition_example.csv
 :name: Scenario Transition Table Example

In the table above, there is growth in agriculture and bare land at the expense of grassland and tropical forest.  The likelihood of tropical forest transitioning to agriculture is rated 8 while grassland to agriculture is rated 4 therefore when converting pixels to agriculture, the forest pixels are converted before grassland pixels (see assumptions). Similarly, when converting pixels, the goal of agriculture is satisfied before bare land because it has higher weight.

3. **Land suitability factors (optional):** This table lists the factors that determine suitability of the land cover for change.  Each factor lists a layer, which defines the suitability.  Given that the same factor can have different implications for different objectives, users can enter more than one layer for each cover (objective).  If this table is not provided, these factors will not be used and only the transition likelihood table above will be used. It is strongly advised to include factors. The following are the required fields:
  #. Factorname: The name of the factor.  This should be a single short name for identifying the factor and unique for the factor.  No spaces allowed
  #. Layer: The name of the GIS feature class with the features of the factor.  For example roads.shp.  Area (as opposed to lines and points) datasets can be given an features (eg shapefile) or raster.  If given as feature (vector) then the suitfield (with values in the range 0-100) must be specified.  If given as raster then the value of the raster should indicate the suitability (0 -100 where 100 means very suitable for the particular cover and 0 means unsuitable)
  #. Dist: The distance of influence of the factor e.g. the distance from the roads.  This tool uses just one distance for all the features.  The polygon features do not use this field.  Distance should be in the units of the landcover dataset (assumed meters).
  #. Suitfield: This identifies the field in the polygon layer that contains the suitability value.  The field values should be integers number between 0 and 100 with 0 being unsuitable and 100 being very suitable. This does not apply for non polygon datasets.
  #. Wt: This is the weight of the factor.  When factors are combined, this weighting is applied.  
  #. Cover: The factors apply to specific land cover types.  This field is used to specify the cover to which the factor applies.

.. csv-table::
 :file: scenario_suitability_factors.csv
 :name: Suitability Factors


4. **Priority (weight) matrix(optional):** The weights of factors are calculated using the multi criteria evaluation approach, applying pairwise comparison with the analytic hierarchy process.  This approach is used for:
  #. Ranking the cover types for conversion 
  #. Assigning weights to the factors for each cover

If the user does not want to use this approach they can manually enter the priority and the weights into the respective tables.  The matrix should follow the format below, the matrix values are entered from column 3.  The first two columns are reserved for descriptive values (Record number and the item) and the last column is reserved for the PRIORITY or weight.  The tool computes the weights and populates this column.  Only the lower half of the diagonal should be filled and the diagonal cells should contain 1s.  The names of the items are not crucial but they must be in the same order as they are in the rows.  If using this for the factors, these should be factors for a single cover(objective).  For example, these may be factors that determine growth of agriculture (a cover, and an objective in this tool).

.. csv-table::
 :file: scenario_pairwise_matrix.csv
 :name: Pairwise Comparison Matrix

5. **Change override layer (optional):** This is a vector (polygon) layer with land cover types in the same scale and projection as the input land cover.  This layer is used to override all the changes and is applied after the rule conversion is complete. 
#. **Constraints Layer (optional):** This is a vector layer which indicates the parts of the landscape that are protected of have constraints to land cover change.  The layer should have one field named ‘protlevel’ with a value between 0 and 1 where 0 means its fully protected and 1 means its fully open to change.
#. **Factor weight:** The factor weight is a value between 0 and 1 which determines the weight given to the factors vs. the expert opinion likelihood rasters.  For example, if a weight of 0.3 is entered then 30% of the final suitability is contributed by the factors and the likelihood matrix contributes 70%.  This value is entered on the tool interface.
#. **Specify transitions:** This is an option that determines whether the likelihood probability matrix should be used.  If this is not checked the probability matrix is ignored. This value is entered on the interface.
#. **Use factors:** This is an option that determines whether the factors should be used.  If this is not checked the factors are ignored. This value is entered on the interface.
#. **Result suffix (optional):** The value entered here will be used as a suffix for your results. Only one character is allowed. Adding a unique suffix will avoid overwriting previous results files.
#. **Downsampling (optional):** The resolution at which you would like the model to run. The landcover map will have a "native" resolution (i.e., the size of each cell in the raster, such as 30m x 30m). If you want to make this resolution coarser (i.e., bigger cells) to speed up run time or keep file sizes low, input a different (bigger) cell size and the model will automatically resample to the new resolution. You cannot define a new resolution which is finer than the native resolution of the raster dataset.


Interpreting Results
====================

Final Results
-------------

Final results are found in the "output" folder of the workspace for this module. Typically the tool is run several times changing the values until and acceptable scenario map is produced.

scenario.tif - This is the new landcover data created. Load this data and compare with the original landcover.

scenario-output-summary.html - a html file which shows the land cover transitions and a graphical representation of the changes.

Intermediate results
--------------------

The intermediate folder contains the intermediate files used in the model run.

References
==========

#. Carver, S. J. (1991) Integrating multi-criteria evaluation with geographical information systems International Journal of Information Systems 5 (3) 321-339
#. Collins, M.G., Steiner, F.R. and Rushman, M. J. (2001) Environmental Management 28 (5) 611-621
#. Malczewski, J. (2004) GIS-based land-use suitability analysis: a critical overview Progress in Planning 62 3-65
#. Saaty, T.L (1977) A Scaling Method for Priorities in Hierarchical Structures Journal of Mathematical Psychology 15, 234-281
#. Saaty, T. L. (2008) Decision Making with the analytic hierarchy process International Journal of Services Sciences 1(1) 83-98
#. Veldkamp, A. and Lambin, E.F. (2001) Predicting Land-Use change Agriculture Ecosystems and Environment.

Appendix
========

The Saaty 9 Point Continous Scale
---------------------------------

.. csv-table::
 :file: scenario_saaty.csv
 :name: Saaty 9 Point Continous Scale
