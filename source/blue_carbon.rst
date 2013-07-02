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
.. math:: C_{xt} = { {\sum^{J}_{j=1}} {A_{xjt}(C_{aj} + C_{bj} + (C_{sj}*d_j) + C_{lj})} }

Carbon sequestration
^^^^^^^^^^^^^^^^^^^^

.. math:: \Delta C_{xt} = { {\sum^{J}_{j=1}} A_{xjt}(\Delta C_{xj})}

Carbon loss and emissions after habitat disturbance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Magnitude of loss
"""""""""""""""""

.. math:: E_x = { {\sum^{J}_{j=1}} A_{xj}(b(C_{aj} + C_{bj})+(C_{sj}*d_j)+C_{lj})}

Timing of loss
""""""""""""""

.. math:: E_x = \sum^{J}_{j=1} 0.5^{t/\alpha_j} A_{xj}(b(C_{aj} + C_{bj})+(C_{sj}*d_j)+C_{lj})

where :math:`\alpha_j` is the halflife decay coefficient for biomass and soil carbon on habitat :math:`j`.
