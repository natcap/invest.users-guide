.. _using_invest:

Using InVEST
============

Opening the Model
-----------------

On MacOS, all InVEST models are contained within one application. Navigate to your Applications and open InVEST from there, then select the model from the list that appears.

On Windows, each InVEST model appears as its own program. Navigate to the Start Menu -> All Programs, then open the model from there.

Running the Model
-----------------
The model interface consists of a form with one field for each model input. For input files, you may type out the path or use the file selector button to navigate to the file. Once all inputs are entered and valid, click the Run button.

Resources for Finding and Formatting Data
-----------------------------------------
Each model's page in this guide contains a **Data Needs** section that describes the format for each input. The :ref:`data_sources` page has guidance on finding data for common model inputs. Many models also have an **Appendix** with guidance on finding data specific to the model. The **sample data** provides examples of each input.

.. warning::
   The sample data exists only to illustrate the data structure. Sample data values may be completely made-up or modified from an old study. They are not generic or default values and they should not be used with or in place of your own data.

Validation
----------
InVEST validates all inputs as you enter them to make sure that the format is correct. This checks things like:
- a CSV contains all the expected columns
- a numeric input is within the allowed range
- all the spatial inputs overlap
You cannot run the model until all inputs pass validation. On the left side, a green checkmark indicates the input looks correct, while a red X indicates a problem. Click on the red X to see a description of the problem.


Viewing Output from the Model
-----------------------------
All model output is stored in files in the workspace directory. Most outputs are spatial files (vectors or rasters), but some models also produce CSVs, HTML files, etc. See the "Interpreting Results" section in each model's page for details on each output.

When the model completes, click the "Open workspace" button to open a file explorer window in the model workspace directory.
Alternatively, while the model is running you may check the "Open workspace after success" button to automatically open the file explorer window when the model finishes.

Final Outputs
^^^^^^^^^^^^^
The final outputs are located in the top level of the workspace directory.

Intermediate Outputs
^^^^^^^^^^^^^^^^^^^^
Intermediate outputs are files that are produced in the process of making the final outputs. These intermediate outputs may be of interest for some applications, and they are useful for identifying the origin of output patterns and debugging. They are found in a directory within the workspace, usually called something like "intermediate" or "intermediate_dir".

Log File
^^^^^^^^
In the top level of the workspace directory, the model produces a log file. It includes all of the parameters and their values, information about the run, and any errors. The log file is named ``InVEST-[model name]-log-[date]-[time].txt``.

Cache
^^^^^
The workspace also contains a directory that is used to cache past runs of the model as described in :ref:`avoided recomputation`. It is usually called something like "cache" or "cache_dir". It does not contain any human-readable data and you may ignore it.


Advanced Features
-----------------

.. _avoided recomputation:

Avoided recomputation
^^^^^^^^^^^^^^^^^^^^^
All InVEST models support avoided re-computation. This means that the model will detect intermediate and final results from a previous run in the specified workspace and it will avoid re-calculating any outputs that are identical to the previous run. This can save significant processing time for successive runs when only some input parameters have changed.
Note that this only works within a workspace and with the same suffix. If you delete or change the workspace directory, or change the results suffix, no re-computation is avoided.

Parallel processing
^^^^^^^^^^^^^^^^^^^
InVEST models also supports parallel processing. If multiple CPUs are available, users can select the number to use in the dropdown menu at *File > Settings > taskgraph_n_workers_parameter*. Not all model operations can run in parallel, and the optimal number of CPUs to use is dependent on the input datasets.
