.. _calibration_freshwater:

****************************************
Calibrating the InVEST Freshwater Models
****************************************

All models are simplifications and approximations of very complex real-world processes. So then how accurate are our model results? The fact is, we don’t really know, until we calibrate the model with observed data. Calibration is the process of comparing model results to observed data and adjusting one or more of the model’s input parameters so that it produces numeric results that come close to observed values. This gives us greater certainty in the results, which is especially important if you want to use the absolute values output by the model for decision-making, or to assign value to them.

Calibration is a complex and time-consuming process that requires:

+ A long time series of high-quality observed data
+ The aility to write Python scripts
+ Statistics skills
+ Hydrology expertise and local knowledge can also be very useful.

This guide provides information to help you get started calibrating InVEST freshwater models - Nutrient Delivery Ratio (NDR), Sediment Delivery Ratio (SDR), Annual Water Yield (AWY), and Seasonal Water Yield (SWY). This does not cover every detail, nor is it tailored to all of the many observed data sources that are out there. See the References/Additional resources section for pointers to papers that give additional guidance for specific models

.. freshwater_calibration_steps:

General calibraton steps
========================

1. Find observed data within the watershed of interest. This is usually from gauge stations.
	- Gauge station data often comes from government agencies, but may also be provided by water-related utilities like hydropower operators, or other sources. The more gauge stations in your study area that you obtain data from, the more confidently you’ll be able to calibrate your model to be applicable across that entire area, but also the more difficult calibration becomes as you’re more comprehensively assessing your model’s fit with reality.
	- The data generally comes in some sort of tabular format, including dates with observed values for the specific nutrient, sediment or water flow measurement(s) that you are interested in.

2. Review the observed data for required measurements, duration, and completeness.
	- **Required measurements:** values that correspond to the output of the model you’re calibrating. For example, if you’re calibrating SDR sediment export, the gauge data must include either sediment load values, or a combination of sediment concentration and water flow data that can be used to calculate sediment load. Nutrient is often given as concentration, so you would also need water flow data to calculate nutrient load. Water yield is usually more straightforward, expressed in cubic meters per second, or a similar measurement that is easy to translate to the units of the model output.
	- **Duration:** Optimally, at least 10 years of continuous daily data, which corresponds with the time frame of the climate data you’re using as input to the InVEST model.
	- **Completeness:** No large gaps in the data. If there is a small gap in one year, but the other years’ data fill that gap, that is ok. But if most or all years are missing data for, say, a whole month or whole season, then that is unlikely to produce good results. If there is a lot of missing data for a particular year, then it is best to not use any of the data for that whole year.
	- It is worth finding out whether someone has already processed the observed data into monthly or annual average values. This isn’t common, but can save you a lot of time if you get lucky.

3. Prepare the observed data, summarizing it to a value that can be compared directly with model results.
	- This process will be different depending on the nature of the data you’re working with, and the model output that you are calibrating, so it’s hard to create a set of detailed instructions, or generalizations.
	- Whatever the process, you need to create one (or possibly 12 monthly values for the SWY model) single value that represents mean annual sediment loading, nutrient loading, or water yield at each gauge station, with units that match the model output.
		+ Observed nutrient data are often given as concentrations (for example, mg/L). To convert these to the kg/year units output by NDR, you will need the mean nutrient concentration, plus the mean stream flow rate recorded at each gauge station during the same time period. Then multiply (mean nutrient concentration value x mean stream flow rate) and convert to kg.
		+ Observed sediment data may also be given as concentrations, in which case you can follow a similar method as for nutrient to convert to the metric tons/year units output by SDR. If the observed data provides Total Suspended Solids (TSS), the units may already be the same as SDR, so no conversion may be necessary
		+ The units of observed water flow are often expressed as something like cubic meters/second, which can be easily translated to monthly (for the SWY model) or annual (SWY or AWY) values for model comparison.
		+ For the Seasonal Water Yield model, you could calculate 12 averages representing each month of the year for a given gauge station, but you would need to decide how to distribute the annual baseflow result between months. Since the baseflow result is already intended to be used as an index, and it’s given annually, distributing it between months or seasons is very approximate and adds another layer of uncertainty. That said, here are several ways of calculating monthly baseflow:
			1. Divide the annual baseflow result by 12, and use the same value or raster for each month. This is the simplest approach, and perhaps best used in places where rainfall is not very seasonal. 
			2. Divide the annual baseflow result proportionally to each month's rainfall depth. This is slightly more complex, but perhaps better in places where rainfall is very seasonal.
			3. One far more sophisticated approach is described in page 5 of the supplement from `Mandle et al. 2025 <https://static-content.springer.com/esm/art%3A10.1038%2Fs43247-025-02254-9/MediaObjects/43247_2025_2254_MOESM2_ESM.pdf>`_.

4. Compare the calculated observed values with modeled results.
	+ Summarize the modeled results within the watershed that drains into the point where the observed data was taken. See the following section “Delineating watersheds” for more information.
	+ The modeled result is unlikely to match the observed values, and may be very different. Remember that these are simple models, and for any model (even complex ones) calibration is usually necessary to bring the modeled results close to reality, and calibration is necessary to have confidence in the absolute values.

5. **Do a sensitivity analysis to determine which model parameters have the greatest effect on results.** These are the parameters that will later be adjusted for calibration.
	+ Sensitivity analysis requires doing many model runs, which is most efficiently done by scripting. See the following section “Setting up the InVEST python scripting environment” for more information about how to get started.
	+ Vary biophysical table values (related to the land use/land cover map, for example SDR’s usle_c, or AWY’s Kc), as well as global model parameter values (like Threshold Flow Accumulation, SWY’s gamma parameter, or SDR’s IC0 parameter), one parameter at a time, within reasonable ranges, based on ranges reported in the literature. If you do not have literature ranges, you can start with varying the values between, say, -50% and +50% of the default value, in increments of 10% (See Table 1 in Hamel et al. 2015). You can also vary spatial input layers (like precipitation), if you have different sources covering the area of interest that are significantly different from each other.
	+ Run the model for the baseline parameters, then run the model for each different parameter setting. Record the results for all runs, aggregated within the watershed flowing to the location of each gauge station that has provided observed data. Most of these models will do the aggregation for you using the Watershed input that you provide.
	+ The parameters that have the greatest effect on model results (compared with baseline) should be used for calibration.

6. Once you’ve chosen the parameters that have the greatest effect, do another set of model runs that adjusts these parameters across a range of values, changing all of the parameters at the same time, such that a different set of parameter values is used for each model run.
	+ Again, you’ll really want to do this with a script, since there can be many combinations of parameters. Record the results for all runs, aggregated within the watershed flowing to the location of the gauge station that made the observations.
	+ The more locations (gauge stations’ observations) where you compare against modeled results, the more information you’ll have about how well calibrated your model is. Of course, the more locations you have to compare, the more difficult calibration becomes, but that’s only because you’re more comprehensively assessing your model’s fit with reality.

7. Use statistical methods to compare the results from step 6 with the observed data. Select the set of model parameters that create results that come satisfactorily close to the observed data value.
	+ This can be as simple as calculating the percent error as follows: **((modeled_value - observed_value) / observed_value) * 100**

	+ More sophisticated statistical approaches, such as comparisons of R-squared and p-values, can yield more robust comparisons if you’re comfortable with those techniques.
	
8. The set of model parameters selected in Step 7 can now be used to evaluate scenarios, calculate value, and/or other processes that benefit from the increased accuracy of the calibrated model.

What if, despite doing the sensitivity/calibration process, the calibrated values are still unacceptably different from observed data?

* Review the units of your model inputs, and units of observed values, and make sure they're all correct.

* Remember that the InVEST freshwater models are very simple, and may not include processes that have a large impact on water quantity and/or quality in your study area. Review the **How the Model Works** and **Limitations** sections of the model's User Guide chapter for more specific information. It may be that the model is simply not a good match for your study area, in which case you can consider using a different model that is more complex and/or specifically includes the dominant processes in your watershed.


.. freshwater_calibration_watersheds:

Delineating watersheds
======================

When calibrating freshwater models with observed data, we need to delineate the watershed that flows into the point where the observed data gauge is located. Then we can summarize the relevant model result (such as sediment export) within that watershed, and compare that summary with the observed data value. 

Many different tools are available to create watersheds, and you can use whichever one you’re comfortable with. InVEST includes the tool :ref:`DelineateIt <delineateit>` as a simple, effective way of creating watersheds.

Whichever tool you use, they generally require, at a minimum, a digital elevation model (DEM) raster, and a vector (like a shapefile or geopackage) containing the point location(s) to be used as outlets. In this case, the outlet will be the location of a gauge station that collected the observed data. The DEM must be the same one that is used as input to the InVEST freshwater model you’re calibrating.

After running the delineation tool, look at the resulting watershed carefully to make sure that it appears correct. One common problem is that the delineated watershed is very tiny. This is usually caused by the outlet point not being located directly on a stream created by the delineation tool. To fix this, many delineation tools have a “snap” function, where you can specify a distance around the outlet point that the tool should look for a stream, and if one is found within that distance, the tool “snaps” the point to the stream, and delineates the watershed more accurately. If the tool does not have a snap feature, you can manually move the point to lie on the stream network generated by the delineation tool.

Once the watershed is correctly generated, a GIS tool like Zonal Statistics is used to sum the relevant model result raster (such as sediment export or nutrient export) within the watershed. This summarized value is then compared with the observed data value. Alternatively, you can use the generated watershed as an input to the model, which will do the summarizing for you, creating a vector layer whose table contains the summarized values.

Setting up the InVEST Python scripting environment
==================================================

Guides are available for installing the natcap.invest Python package and running Python scripts for modeling:

+ Installing natcap.invest: https://invest.readthedocs.io/en/latest/installing.html
+ Setting up the Python environment and running scripts: https://invest.readthedocs.io/en/latest/scripting.html#setting-up-your-python-environment


Example scripts
===============

InVEST Workbench can create a basic python script for any model. The script imports the necessary libraries, sets up logging, defines the model’s inputs and calls the model with those inputs. It is useful to start with this script, and build on it to create your sensitivity/calibration workflow. To create the script, within Workbench, go to an open model tab, select **Save as…** in the left toolbar, then select **Python script**. 

+ `Basic script for SDR <./calibration_freshwater/basic_SDR_script_example.py>`_, as generated by InVEST workbench.
+ `Script of multiple runs with different biophysical tables <./calibration_freshwater/SDR_script_example_for_loop.py>`_, executed within a for loop.
+ `Another example script <./calibration_freshwater/NDR_sensitivity_example_old_version_of_InVEST.py>`_ that loops through running NDR with different values of kb, Threshold Flow Accumulation, and other global model values, as well as changing the values in the biophysical table. It calculates errors for each run, and writes the results to a table. Note that this is for an older version of InVEST, but it’s still a useful example of setting up the sensitivity parameter runs. 

A detailed study of NDR model calibration and validation was done by `Valladares-Castellanos et al. 2024 <https://doi.org/10.1016/j.scitotenv.2024.175111>`_ in Puerto Rico using open source monitoring data. In the referenced paper, they provide their framework, workflow and R code, which can be adapted to other locations.

References/Additional resources
===============================

**General guidance about uncertainty assessment in ecosystem service analysis:**

Hamel, P. & Bryant, B. 2017. Uncertainty assessment in ecosystem services analyses: Seven challenges and practical responses. Ecosystem Services, Volume 24. https://doi.org/10.1016/j.ecoser.2016.12.008

**Calibrating the NDR model:**

Hamel, P., Guswa, A.J. 2015. Uncertainty Analysis of the InVEST 3.0 Nutrient Model: Case Study of the Cape Fear Catchment, NC. Hydrology and Earth System Sciences Discussion 11:11001-11036. https://doi.org/10.5194/hess-19-839-2015

Valladares-Castellanos, M., de Jesús Crespo, R., Xu, Y. J., Douthat, T. H. 2024. A framework for validating watershed ecosystem service models in the United States using long-term water quality data: Applications with the InVEST Nutrient Delivery (NDR) model in Puerto Rico, Science of The Total Environment, Volume 949, 2024, 175111, ISSN 0048-9697. https://doi.org/10.1016/j.scitotenv.2024.175111

**Calibrating the SDR model:**

Hamel, P., Chaplin-Kramer, R., Sim, S., Mueller, C. 2015. A new approach to modeling the sediment retention service (InVEST 3.0): Case study of the Cape Fear catchment, North Carolina, USA. Science of the Total Environment 524–525 (2015) 166–177. https://doi.org/10.1016/j.scitotenv.2015.04.027

Mandle, L., Angarita, H., Moreno, J., Goldstein, J.A., Melo L., S.F., Echeverri, A., Rojas, N., Villalba, F.D. 2025. Natural capital accounting reveals ecosystems' role in water and energy security in Colombia's Sinú Basin, Communications Earth & Environment (2025). https://doi.org/10.1038/s43247-025-02254-9

**Calibrating the SWY model:**

Hamel, P., Valencia, J., Schmitt, R., Shrestha, M., Piman, T., Sharp, R.P., Francesconi, W., Guswa, A.J., 2020. Modeling seasonal water yield for landscape management: Applications in Peru and Myanmar. Journal of Environmental Management 270, 110792. https://doi.org/10.1016/j.jenvman.2020.110792




