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

.. math:: C_{x, initial} = { {\sum^{J}_{j=1}} {A_{xj}(C_{aj} + C_{bj} + (C_{sj}*d_j) + C_{lj})} }

where

 * :math:`A_{xj}` is the area for habitat :math:`j` in cell :math:`x`
 * :math:`C_{aj}` is the above ground carbon pool for habitat :math:`j`
 * :math:`C_{bj}` is the below ground carbon pool for habitat :math:`j`
 * :math:`C_{sj}` is the soil carbon pool for habitat :math:`j`
 * :math:`d_j` is the depth of :math:`C_{sj}`
 * and :math:`C_l` is the litter carbon pool for habitat :math:`j`

.. math:: C_{x, final} = { {\sum^{J}_{j=1}} {A_{xj}(C_{aj} + C_{bj} + [(C_{sj}*d_j)_{initial} * r^t] + C_{lj})} }

where

 * :math:`A_{xj}` is the area for habitat :math:`j` in cell :math:`x`
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

Timing of loss
""""""""""""""

.. math:: E_x = \sum^{J}_{j=1} A_{xj}\{0.5^{t/\alpha_{j, biomass}} [b_j(C_{aj} + C_{bj}) + C_{lj}]+0.5^{t/\alpha_{j, soil}}(C_{sj}*d_j)\}

where :math:`\alpha_j` is the halflife decay coefficient for biomass and soil carbon on habitat :math:`j`.

Valuation
^^^^^^^^^

Two valuation components

 * Private market discount rate
 * Social market price schedule

Two sections for valuation.

Valuation for initial habitat loss:

.. math:: V_{x, initial} = \sum_{t=0}^{t_{final}-1} \frac{p_t C_{x,initial} R_x^t }{(1+d)^t}

where 

 * :math:`t_{final}` is the number of years between the current date and the end of the habitat change
 * :math:`p_t` is the price of carbon at time :math:`t`
 * :math:`C_{x,initial}` is the intial carbon stock on pixel x at time 0.
 * :math:`R_x` is the rate at which the carbon stock decreases (or increases) per year
 * and :math:`d` is the discount rate


Social Market Valuation
"""""""""""""""""""""""


.. math:: V_x = \sum_{t=0}^{t_{final}-1} \Delta C_{x} * s_t

where

 * :math:`t_{final}` is the number of years between the current date and the end of the habitat change
 * :math:`\Delta C_{x}` is the carbon sequestration
 * :math:`s_t` is the schedule price of carbon at time :math:`t`

