.. _recreation:

.. |openfold| image:: ./shared_images/openfolder.png
              :alt: open
	      :align: middle 
         
.. |addbutt| image:: ./shared_images/addbutt.png
             :alt: add
	     :align: middle 
	     :height: 15px

.. |okbutt| image:: ./shared_images/okbutt.png
            :alt: OK
	    :align: middle 

.. |adddata| image:: ./shared_images/adddata.png
             :alt: add
	     :align: middle 

****************
Recreation Model
****************

Summary
=======


Introduction
============


The model
=========



Limitations and Simplifications
===============================



Data Needs
==========

The model uses an interface to input all required and optional data, as outlined in this section. It outputs a vector grid and processed predictors. The grid is always produced. To compute the initial grid the user the option of selecting any or all of the predictors in :ref:'table-99' and supplying any of their own predictors.

To run the model, two steps are required:

#.	Initial Run
#.	Scenario Run 

The Initial Run tool usually takes the longest amount of time to run (this varies greatly depending on spatial resolution and extent). The most informative attribute of the output grid is usdmav_pr, the estimated user days percentage. Users should review it before running the second model to ensure that there has not been an unexpected error. The Scenario Run tool usually takes the shortest amount of time to run (this has similar dependence as the Initial Run, but is largely dependent on the scenario data). The outputs of this tool are more useful in most analyses; outputs of the Initial Run server mostly as inputs to the Scenario Run tool.

The following outlines the options presented to the user via the two interfaces, and the content and format of the required and option input data used by the model. More information on how to fill the input interface or on how to obtain data is provided in :ref:'rec-appendix-a'

.. _table-99:

Table 9.9
"""""""""

.. csv-table::
  :file: recdata.csv
  :header-rows: 1
  :name: Model data sources.


#. **INPUT NAME (required).** EXPLANATION HERE.  ::

     Name: DESCRIPTION OF THE INPUT
     Sample path: \PATH\ETC


Running the model
=================



Interpreting results
====================

Model outputs
-------------


References
==========
