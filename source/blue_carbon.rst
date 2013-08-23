.. _blue-carbon:

*****************
Blue Carbon Model
*****************

The model
=========

How it works
------------

Carbon storage
^^^^^^^^^^^^^^

Initial Storage
"""""""""""""""

.. math:: S_x(t_0) = H_x(t_0) + M_x(t_0)

.. math:: H_x(t_0) = A_{x}*d_{sx}*C_{sx}

.. math:: M_x(t_n) = A_{x}*(C_{ax} + C_{bx} + C_{lx})

where
 * :math:`S_x(t_0)` is the carbon storage at the initial time
 * :math:`H_x(t_0)` is the carbon storage in the soil at the initial time
 * :math:`M_x(t_n)` is the carbon storage in the biomass at anytime
 * :math:`t_n \in \{t_0, ..., t_N\}` with :math:`t_n < t_{n-1}`
 * :math:`t_0` is the initial time
 * :math:`A_{x}` is the area in cell :math:`x`
 * :math:`C_{ax}` is the above ground carbon pool in cell :math:`x`
 * :math:`C_{bx}` is the below ground carbon pool in cell :math:`x`
 * :math:`d_{sx}` is the depth of :math:`C_{sx}` in cell :math:`x`
 * :math:`C_{sx}` is the soil carbon pool in cell :math:`x`
 * :math:`C_{lx}` is the litter carbon pool in cell :math:`x`

Transition Storage
""""""""""""""""""

.. math:: S_x(t_n) = H_x(t_n) + M_x(t_n)

.. math:: H_x(t_n) = A_{x}*d_{sx}*C_{sx} + R_x(t_{n-1})

.. math:: R_x(t_n) = (1-p_x)*H_x(t_n)

where
 * :math:`S_x(t_n)` is the carbon storage at anytime after :math:`t_0` in cell :math:`x`
 * :math:`H_x(t_n)` is the carbon storage in the soil at anytime after :math:`t_0` in cell :math:`x`
 * :math:`R_x(t_n)` is the residual carbon left in the soil after a transition in cell :math:`x`
 * :math:`t_n` is the current time :math:`> t_0`
 * :math:`A_{x}` is the area in cell :math:`x`
 * :math:`d_{sx}` is the depth of :math:`C_{s}` in cell :math:`x`
 * :math:`C_{sx}` is the soil carbon pool in cell :math:`x`
 * :math:`p_{x}` is the portion of soil carbon not disturbed by the transition in cell :math:`x`

Carbon sequestration
^^^^^^^^^^^^^^^^^^^^

.. math:: \Delta S_x(t_n) = S_x(t_{n}) - S_x(t_{n-1})

where

 * :math:`\Delta S_x(t_n)` is the carbon sequestered between time :math:`t_{n-1}` and :math:`t_n` in cell :math:`x`

Carbon loss and emissions after habitat disturbance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Magnitude of loss
"""""""""""""""""

.. math:: L_x = A_{x}*(C_{ax} + C_{bx} +C_{lx}+p_{x}*d_{x}*C_{sx})

where

* :math:`L_x` is carbon that is disturbed by the transition and will be released in cell :math:`x`

Timing of loss
""""""""""""""

.. math:: E_x = A_{x}[0.5^{(t_n-t_{n-1})/\alpha_{bx}} (C_{ax} + C_{bx} + C_{lx})+0.5^{(t_n-t_{n-1})/\alpha_{sx}}b_{sx} d_{sx} C_{sx}]

where

 * :math:`E_x` is the emission of carbon from time :math:`t_{n-1}` to :math:`t_n` in cell :math:`x`
 * :math:`\alpha_{bx}` is the half-life decay for biomass carbon in cell :math:`x`
 * :math:`\alpha_{sx}` is the half-life decay for soil carbon in cell :math:`x`

.. 
	Valuation
	^^^^^^^^^

	Private Market Discount Rate Valuation
	""""""""""""""""""""""""""""""""""""""

	.. math:: V_{x, initial} = \sum_{t=0}^{t_{final}-1} \frac{p_t \Delta C_{x,initial} R_x^t }{(1+d)^t}

	where 

	.. I feel like a lot of the awkwardness in the math in this document is due to keeping track of timing of LULC changes. I think this would be easy to address from a notation perspective.


	 * :math:`t_{final}` is the number of years between the current date and the end of the habitat change
	 * :math:`p_t` is the price of carbon at time :math:`t`
	 * :math:`C_{x,initial}` is the intial carbon stock on pixel x at time 0.
	 * :math:`R_x` is the rate at which the carbon stock decreases (or increases) per year
	 * and :math:`d` is the discount rate


	Social Market Price Schedule Valuation
	""""""""""""""""""""""""""""""""""""""

	.. math:: V_x = \sum_{t=0}^{t_{final}-1} \Delta C_{x} * s_t

	where

	 * :math:`t_{final}` is the number of years between the current date and the end of the habitat change
	 * :math:`\Delta C_{x}` is the carbon sequestration
	 * :math:`s_t` is the schedule price of carbon at time :math:`t`


	Data Needs
	==========

	 * **Workspace**: The directory to hold output and intermediate results of the particular model run. After the model run is completed the output will be located in this directory. To run multiple scenarios, create a new workspace for each scenario.
	 * **LULC Time 1**: The land use land cover ratser for time 1.
	 * **Year**: The year of ``LULC Time 1``
	 * **LULC Time 2**: The land use land cover raster for time 2.
	 * **Year**: The year of ``LULC Time 2``
	 * **Carbon pools:** A table of LULC classes, containing data on carbon in metric tons per hectacre \( t ha\ :sup:`-1`\) stored in each of the four fundamental pools for each LULC class. Carbon storage data can be collected from field estimates from local plot studies, extracted from meta-analyses on specific habitat types or regions, or found in general published tables (e.g., IPCC, see Appendix). If information on some carbon pools is not available, pools can be estimated from other pools, or omitted by leaving all values for the pool equal to 0. Additionally, there must be columns for soil depth, 
	 * **Transition matrix**: The transition matrix contains transition coefficients for the rate change in carbon from time 1 to time 2.
	 * **Private market valuation** ``(optional -- required for private market valuation)``: 

		 * **Price in term of metric tons of** ``(optional -- required for private market valuation)``: This is whether the price per metric ton is in terms of elemental carbon or CO\ :sub:`2` which is heavier.
		 * **Value of Carbon** ``(optional -- required for private market valuation)``: The private market value for the carbon in United States dollars.
		 * **Market discount in price of Carbon** ``(optional -- required for private market valuation)``: society's preference for immediate benefits over future benefits (labeled "Market discount rate (%) (optional)" in the tool interface). The default value in the interface is 7% per year, which is one of the market discount rates recommended by the U.S. government for cost-benefit evaluation of environmental projects. However, this rate will depend on the country and landscape being evaluated. Philosophical arguments have been made for using a lower discount rate when modeling climate change related dynamics, which users may consider using. If the rate is set equal to 0% then monetary values are not discounted.
		 * **Annual rate of change in price of Carbon** ``(optional -- required for private market valuation)``: adjusts the value of sequestered carbon as the impact of emissions on expected climate change-related damages changes over time. The default value in the interface is 0% (labeled "The annual rate of change in the price of carbon (%) (optional)" in the tool interface). However, setting this rate greater than 0% suggests that the societal value of carbon sequestered in the future is less than the value of carbon sequestered now. It has been widely argued that GHG emissions need to be curtailed immediately to avoid crossing a GHG atmospheric concentration threshold that would lead to a 3 degree Celsius or greater change in global average temperature by 2105. Some argue that such a temperature change would lead to major disruptions in economies across the world (Stern et al. 2006). Therefore, any mitigation in GHG emissions that occurs many years from now may have no effect on whether or not this crucial concentration threshold is passed. If this is the case, C sequestration in the far future would be relatively worthless and a carbon discount rate greater than zero is warranted. Alternatively, setting the annual rate of change less than 0% (e.g., -2%) suggests that the societal value of carbon sequestered in the future is greater than the value of carbon sequestered now (this is a separate issue than the value of money in the future, a dynamic accounted for with the market discount rate). This may be the case if the damages associated with climate change in the future accelerate as the concentration of GHGs in the atmosphere increases.
	 * **Social market valuation** ``(optional -- required for social market valuation)``:

		 * **SCC Table** ``(optional -- required for social market valuation)``: value estimates based on damage costs associated with the release of an additional ton of carbon, the social cost of carbon (SCC). The default data comes from *Rob...*
		 * **SCC field** ``(optional -- required for social market valuation)``: The field in the ``SCC Table`` that contains the value for the carbon. The default data includes rates for 5%, 3%, and 2%.

	Interpreting Results
	====================

	Model Ouputs
	------------

	Output folder
	^^^^^^^^^^^^^

	 * ``carbon1_above.tif``: The output raster indicating the carbon from above ground in metric tons.
	 * ``carbon1_below.tif``: The output raster indicating the carbon from below ground in metric tons.
	 * ``carbon1_litter.tif``: The output raster indicating the carbon from litter in metric tons.
	 * ``carbon1_soil.tif``: The output raster indicating the carbon from soil in metric tons.
	 * ``carbon1_total.tif``: The output raster indicating the total carbon from all sources in metric tons.
	 * ``carbon2_above.tif``: The output raster indicating the carbon from above ground in metric tons.
	 * ``carbon2_below.tif``: The output raster indicating the carbon from below ground in metric tons.
	 * ``carbon2_litter.tif``: The output raster indicating the carbon from litter in metric tons.
	 * ``carbon2_soil.tif``: The output raster indicating the carbon from soil in metric tons.
	 * ``carbon2_total.tif``: The output raster indicating the total carbon from all sources in metric tons.
	 * ``depth.tif``: The output raster indicating the depth of soil in meters.
	 * ``magnitude.tif``: The output raster indicating the emission of carbon in metric tons.
	 * ``private_valuation.tif``: The output raster indicating the value in United States dollars.
	 * ``sequestration.tif``: The output raster indicating the net carbon storage in metric tons.
	 * ``social_valuation.tif``: The output raster indicating the value United States dollars.
	 * ``timing.tif``: The output raster indicating the metric tons of carbon emitted over the course of the transition.
	 * ``transition.tif``: The output raster indicating the transition coefficent betweeen LULC from time 1 to time 2.
