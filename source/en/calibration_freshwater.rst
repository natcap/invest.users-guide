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

Summary
=======
