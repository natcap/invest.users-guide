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

.. math:: C_x = { {\sum^{J}_{j=1}} {A_{xj}(C_{aj} + C_{bj} + (C_{sj}*d_j) + C_{lj})} }

Carbon sequestration
^^^^^^^^^^^^^^^^^^^^

.. math:: \Delta C_x = { {\sum^{J}_{j=1}} A_{xj}(\Delta C_{xj})}

Carbon loss and emissions after habitat disturbance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Magnitude of loss
"""""""""""""""""

.. math:: E_x = { {\sum^{J}_{j=1}} A_{xj}(b(C_{aj} + C_{bj})+(C_{sj}*d_j)+C_{lj})}

Timing of loss
""""""""""""""

.. math:: E_x = \sum^{J}_{j=1} 0.5^{t/\alpha_j} A_{xj}(b(C_{aj} + C_{bj})+(C_{sj}*d_j)+C_{lj})

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

