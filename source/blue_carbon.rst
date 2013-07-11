.. _blue-carbon:

*****************
Blue Carbon Model
*****************

The model
=========

How it works
------------

Given a carbon pool table :math:`P`, a transition matrix :math:`T`, a LULC at time 1 :math:`A_{t_0}`, and a LULC at time 2 :math:`A_{t_n}`.

Carbon storage
^^^^^^^^^^^^^^

.. math:: C_{aj} = P_{aj}
.. math:: C_{bj} = P_{bj}
.. math:: C_{sj} = P_{sj}
.. math:: C_{lj} = P_{lj}
.. math:: d_j = P_{dj}

.. math:: r = T_{j_0 j_n}

Initial Storage
"""""""""""""""
.. math:: C_{x, initial} = { {\sum^{J}_{j=1}} {A_{xj}(C_{aj} + C_{bj} + (C_{sj}*d_j) + C_{lj})} }

where

 * :math:`J = 1`
 * :math:`A_{xj}` is the area (for habitat :math:`j`) in cell :math:`x`
 * :math:`C_{aj}` is the above ground carbon pool for habitat :math:`j`
 * :math:`C_{bj}` is the below ground carbon pool for habitat :math:`j`
 * :math:`C_{sj}` is the soil carbon pool for habitat :math:`j`
 * :math:`d_j` is the depth of :math:`C_{sj}`
 * and :math:`C_l` is the litter carbon pool for habitat :math:`j`

Transition of Carbon in Soil
""""""""""""""""""""""""""""

.. note:: Implemented, but without any calls.

.. math:: C_{s x j_n t_n} = A_{x j_n t_n} C_{s j_n}d_{x j_n t_n} - \frac{1}{(1 + r)^t} (A_{xj_0t_0}C_{sj_0}d_{x j_0  t_0} - A_{xj_nt_n}C_{sj_n}d_{x j_n t_n})

where

 * :math:`C_{j_0} > C_{j_n}`
 * :math:`s` represents carbon stored in soil
 * :math:`x` represents the raster cell
 * :math:`j` represents the habitat
 * :math:`t` represents the time
 * :math:`A_{xjt}` is the area in raster cell :math:`x` (of habitat :math:`j` at time :math:`t`)
 * :math:`C_{sj}` is carbon store in soil for habitat :math:`j`
 * :math:`d_{xjt}` is the depth (in raster cell :math:`x` of habitat :math:`j` at time :math:`t`)
 * :math:`r` is rate of land cover conversion from :math:`j_0` to :math:`j_n`

Transition Storage
""""""""""""""""""
.. math:: C_{x, final} = { {\sum^{J}_{j=1}} {A_{xj}(C_{aj} + C_{bj} + [(C_{sj}*d_j)_{initial} * r^t] + C_{lj})} }

where

 * :math:`J=1`
 * :math:`A_{xj}` is the area in cell :math:`x` (for habitat :math:`j`)
 * :math:`C_{aj}` is the above ground carbon pool for habitat :math:`j`
 * :math:`C_{bj}` is the below ground carbon pool for habitat :math:`j`
 * :math:`(C_{sj}*d_j)_{initial}` is the initial soil carbon pool for habitat :math:`j_{initial}`
 * :math:`r` is the rate of conversion from :math:`(C_{sj}*d_j)_{initial}` for habitat :math:`j`
 * :math:`t` is the number of years between the initial and final habitats
 * and :math:`C_l` is the litter carbon pool for habitat :math:`j`

Carbon sequestration
^^^^^^^^^^^^^^^^^^^^

.. math:: \Delta C_{x} = C_{x, initial} - C_{x, final}

Carbon loss and emissions after habitat disturbance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Magnitude of loss
"""""""""""""""""

.. math:: E_x = { {\sum^{J}_{j=1}} A_{xj}[b_j(C_{aj} + C_{bj})+(C_{sj}*d_j)+C_{lj}]}

where

 * :math:`J=1`

Timing of loss
""""""""""""""

.. math:: E_x = \sum^{J}_{j=1} A_{xj}\{0.5^{t/\alpha_{j, biomass}} [b_j(C_{aj} + C_{bj}) + C_{lj}]+0.5^{t/\alpha_{j, soil}}(C_{sj}*d_j)\}

where

 * :math:`J=1`
 * :math:`\alpha_j,biomass` is the half-life decay for biomass carbon on habitat :math:`j`
 * :math:`\alpha_j,soil` is the half-life decay for soil carbon on habitat :math:`j`.

Valuation
^^^^^^^^^

Private Market Discount Rate Valuation
""""""""""""""""""""""""""""""""""""""

.. math:: V_{x, initial} = \sum_{t=0}^{t_{final}-1} \frac{p_t \Delta C_{x,initial} R_x^t }{(1+d)^t}

where 

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
 * **LULC Time 1**:
 * **Year**:
 * **LULC Time 2**:
 * **Year**:
 * **Carbon pools:** A table of LULC classes, containing data on carbon stored in each of the four fundamental pools for each LULC class. Carbon storage data can be collected from field estimates from local plot studies, extracted from meta-analyses on specific habitat types or regions, or found in general published tables (e.g., IPCC, see Appendix). If information on some carbon pools is not available, pools can be estimated from other pools, or omitted by leaving all values for the pool equal to 0.
 * **Transition matrix**:
 * **Private market valuation** ``(optional -- required for private market valuation)``: 

   * **Price in term of metric tons of** ``(optional -- required for private market valuation)``:
   * **Value of Carbon** ``(optional -- required for private market valuation)``: in dollars per metric ton of elemental carbon (not CO\ :sub:`2`, which is heavier, so be careful to get units right! If the social value of CO\ :sub:`2`\ e is $Y per metric ton, then the social value of C is $(3.67*Y) per metric ton (Labeled "Price of carbon per metric ton (optional)" in the tool interface.) For applications interested in estimating the total value of carbon sequestration, we recommend value estimates based of damage costs associated with the release of an additional ton of carbon (the social cost of carbon (SCC).  Stern (2007), Tol (2009), and Nordhaus (2007a) present estimates of SCC.  For example, two SCC estimates we have used from Tol (2009) are $66 and $130 (in 2010 US dollars) (Polasky et al. 2010). For applications interested in estimating the value that could be gained by trading carbon credits in the current markets, the value can be taken from the current market prices on the Chicago or European Climate Exchanges.
   * **Market discount in price of Carbon** ``(optional -- required for private market valuation)``: society's preference for immediate benefits over future benefits (labeled "Market discount rate (%) (optional)" in the tool interface). The default value in the interface is 7% per year, which is one of the market discount rates recommended by the U.S. government for cost-benefit evaluation of environmental projects. However, this rate will depend on the country and landscape being evaluated. Philosophical arguments have been made for using a lower discount rate when modeling climate change related dynamics, which users may consider using. If the rate is set equal to 0% then monetary values are not discounted.
   * **Annual rate of change in price of Carbon** ``(optional -- required for private market valuation)``: adjusts the value of sequestered carbon as the impact of emissions on expected climate change-related damages changes over time. The default value in the interface is 0% (labeled "The annual rate of change in the price of carbon (%) (optional)" in the tool interface). However, settingthis rate greater than 0% suggests that the societal value of carbon sequestered in the future is less than the value of carbon sequestered now. It has been widely argued that GHG emissions need to be curtailed immediately to avoid crossing a GHG atmospheric concentration threshold that would lead to a 3 degree Celsius or greater change in global average temperature by 2105.Some argue that such a temperature change would lead to major disruptions in economies across the world (Stern et al. 2006). Therefore, any mitigation in GHG emissions that occurs many years from now may have no effect on whether or not this crucial concentration threshold is passed. If this is the case, C sequestration in the far future would be relatively worthless and a carbon discount rate greater than zero is warranted. Alternatively, setting the annual rate of change less than 0% (e.g., -2%) suggests that the societal value of carbon sequestered in the future is greater than the value of carbon sequestered now (this is a separate issue than the value of money in the future, a dynamic accounted for with the market discount rate). This may be the case if the damages associated with climate change in the future accelerate as the concentration of GHGs in the atmosphere increases.
 * **Social market valuation** ``(optional -- required for social market valuation)``:

   * **SCC Table** ``(optional -- required for social market valuation)``:
   * **SCC field** ``(optional -- required for social market valuation)``:

Interpreting Results
====================

Model Ouputs
------------

Output folder
^^^^^^^^^^^^^

 * ``carbon1_above.tif``: The output raster indicating the carbon from above ground in metric tons per square meter.
 * ``carbon1_below.tif``: The output raster indicating the carbon from below ground in metric tons per square meter.
 * ``carbon1_litter.tif``: The output raster indicating the carbon from litter in metric tons per square meter.
 * ``carbon1_soil.tif``: The output raster indicating the carbon from soil in metric tons per square meter.
 * ``carbon1_total.tif``: The output raster indicating the total carbon from all sources in metric tons per square meter.
 * ``carbon2_above.tif``: The output raster indicating the carbon from above ground in metric tons per square meter.
 * ``carbon2_below.tif``: The output raster indicating the carbon from below ground in metric tons per square meter.
 * ``carbon2_litter.tif``: The output raster indicating the carbon from litter in metric tons per square meter.
 * ``carbon2_soil.tif``: The output raster indicating the carbon from soil in metric tons per square meter.
 * ``carbon2_total.tif``: The output raster indicating the total carbon from all sources in metric tons per square meter.
 * ``depth.tif``: The output raster indicating the depth of soil in meters.
 * ``magnitude.tif``: The output raster indicating the emission of carbon in metric tons per square meter.
 * ``private_valuation.tif``: The output raster indicating the United States dollars per square meter.
 * ``sequestration.tif``: The outout raster indicating the net carbon storage in metric tons per square meter
 * ``social_valuation.tif``: The output raster indicating the United States dollars per square meter.
 * ``timing.tif``: The output raster indicating the metric tons per square meter of carbon emitted over the course of the transition.
 * ``transition.tif``: The ouput raster indicating the transition coefficent betweeen LULC from time 1 to time 2.
