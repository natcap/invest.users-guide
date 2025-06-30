.. calibration_freshwater:

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

General calibraton steps
========================

1. **Find observed data within the watershed of interest.** This is usually from gauge stations.
	- Gauge station data often comes from government agencies, but may also be provided by water-related utilities like hydropower operators, or other sources. The more gauge stations in your study area that you obtain data from, the more confidently you’ll be able to calibrate your model to be applicable across that entire area, but also the more difficult calibration becomes as you’re more comprehensively assessing your model’s fit with reality.
	- The data generally comes in some sort of tabular format, including dates with observed values for the specific nutrient, sediment or water flow measurement(s) that you are interested in.

2. **Review the observed data for required measurements, duration, and completeness.**
	- **Required measurements:** values that correspond to the output of the model you’re calibrating. For example, if you’re calibrating SDR sediment export, the gauge data must include either sediment load values, or a combination of sediment concentration and water flow data that can be used to calculate sediment load. Nutrient is often given as concentration, so you would also need water flow data to calculate nutrient load. Water yield is usually more straightforward, expressed in cubic meters per second, or a similar measurement that is easy to translate to the units of the model output.
	- **Duration:** Optimally, at least 10 years of continuous daily data, which corresponds with the time frame of the climate data you’re using as input to the InVEST model.
	- **Completeness:** No large gaps in the data. If there is a small gap in one year, but the other years’ data fill that gap, that is ok. But if most or all years are missing data for, say, a whole month or whole season, then that is unlikely to produce good results. If there is a lot of missing data for a particular year, then it is best to not use any of the data for that whole year.
	- It is worth finding out whether someone has already processed the observed data into monthly or annual average values. This isn’t common, but can save you a lot of time if you get lucky.

3. **Prepare the observed data, summarizing it to a value that can be compared directly with model results.**
	- This process will be different depending on the nature of the data you’re working with, and the model output that you are calibrating, so it’s hard to create a set of detailed instructions, or generalizations.
	- Whatever the process, you need to create one (or possibly 12 monthly values for the SWY model) single value that represents mean annual sediment loading, nutrient loading, or water yield at each gauge station, with units that match the model output.
		+ Observed nutrient data are often given as concentrations (for example, mg/L). To convert these to the kg/year units output by NDR, you will need the mean nutrient concentration, plus the mean stream flow rate recorded at each gauge station during the same time period. Then multiply (mean nutrient concentration value x mean stream flow rate) and convert to kg.
		+ Observed sediment data may also be given as concentrations, in which case you can follow a similar method as for nutrient to convert to the metric tons/year units output by SDR. If the observed data provides Total Suspended Solids (TSS), the units may already be the same as SDR, so no conversion may be necessary
		+ The units of observed water flow are often expressed as something like cubic meters/second, which can be easily translated to monthly (for the SWY model) or annual (SWY or AWY) values for model comparison.
		+ For the Seasonal Water Yield model, you could calculate 12 averages representing each month of the year for a given gauge station, but you would need to decide how to distribute the annual baseflow result between months. Since the baseflow result is already intended to be used as an index, and it’s given annually, distributing it between months or seasons is very approximate and adds another layer of uncertainty. That said, here are two very simple ways of calculating monthly baseflow:
			1. Divide the annual baseflow result by 12, and use the same value or raster for each month.
			2. Divide the annual baseflow result proportionally to each month's rainfall depth
		  One far more sophisticated approach is described in page 5 of the supplement from `Mandle et al. 2025 <https://static-content.springer.com/esm/art%3A10.1038%2Fs43247-025-02254-9/MediaObjects/43247_2025_2254_MOESM2_ESM.pdf`_.



:ref:`installing-on-mac` sections of this chapter.

