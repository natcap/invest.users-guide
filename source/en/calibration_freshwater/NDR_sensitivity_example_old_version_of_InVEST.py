#######################################################################
#
# NDR sensitivity analysis example
#
# 1/ Runs NDR a bunch of times, varying input parameters
# 2/ Compares #1 to observed data and creates output tables
#       with difference/error values
#
# We're modifying both biophysical coefficients and
#   single-value UI parameters - each coefficient/parameter
#   has its own section below. Only one parameter is changed at
#   a time, and individual coefficients for all LULC classes are 
#   changed at once 
#
# For re-using this script, look for the comments
#   # MODIFY THESE # or # MODIFY THIS # and do so to customize
#   the paths to inputs/outputs.
#
# Run this script with python -u, or you won't get the status
#   information printed out while running, it will all cache
#   until the very end. Haven't figured out how to fix this
#   programmatically and don't feel like spending time on it.
#
# All of this could surely be done more efficiently,
#   but still a useful example.
#
# Original script by Rich Sharp, modified by Stacie Wolny
#
#
#######################################################################

import os
import pygeoprocessing
import numpy
import natcap.invest.ndr.ndr
import shutil
import csv
# Pandas provides easier csv/table data processing - very useful here
import pandas
import time
# Needed for post-processing NDR results
import gdal
import ogr
import sys

#                                                                  #
# MODIFY THESE - INPUT/OUTPUT FOLDERS, NODATA AND OBSERVED VALUE   #
#                                                                  #

# Folder where input data lives
DATA_BASE_DIR = (
    r'D:\Belize\Caracol\model_inputs\NDR_inputs_CMCC_baseline_sensitivity')
# Folder where NDR outputs will be written
WORKSPACE_DIR = (
    r'C:\Temp\NDR_sensitivity_test')
# Folder where biophysical tables will be written that contain updated
#   calibration values for each run - just for a sanity/debugging check
ADJUSTED_TABLE_DIR = (
    r'C:\Temp\NDR_sensitivity_test\adjusted_coeff_tables')
# Folder where post-processing output will be written
#   - Multiplying by effective export, reaggregating, etc
POST_PROC_DIR = (
    r'C:\Temp\NDR_sensitivity_test\post_process')
# Output file name of the table where final difference/error results will be written (CSV)
OUTPUT_RESULT_TABLE_PATH = (os.path.join(POST_PROC_DIR, 'sensitivity_results_SanIgnacio_NDR.csv'))

# Effective export raster output from Rich's dam retention script
##EFFECTIVE_EXPORT_RASTER_PATH = (
##    r'D:\Stacie\US\EPA_SNEP\data\Inputs_Moshassuck_clip\nutrient_eff_export_1fill.tif')

# Set NoData value for post-processing outputs - needed for pygeoprocessing calls
NODATA_VALUE = -1

# Observed nutrient export value that we're comparing our results to
#   for calculating error
# N value is annual average for a/the San Ignacio station, 2016-2018
OBSERVED_VALUE_N = 711252


###############################################################################

def main():

    # Keep track of how long it takes to run the script
    start_time = time.time()
    

    #                                           #
    # MODIFY THESE - BASE DATA INPUTS TO NDR    #
    #                                           #
    args = {
        'biophysical_table_path': os.path.join(
            DATA_BASE_DIR, 'Biophysical_table_Belize_base_sensitivity.csv'),
        'dem_path': os.path.join(
            DATA_BASE_DIR, 'DEM_D8_burn_CMCC.tif'),
        'runoff_proxy_path': os.path.join(
            DATA_BASE_DIR, 'Nut_runoff_proxy.tif'),
        'lulc_path': os.path.join(
            DATA_BASE_DIR, 'LULC_CMCC_baseline_v2.tif'),
        'watersheds_path': os.path.join(
            DATA_BASE_DIR, 'serviceshed_SanIgnacio_station.shp'),
        'calc_n': True,
        'calc_p': False,
        'k_param': '2',
        'subsurface_critical_length_n': '150',
        'subsurface_critical_length_p': '150',
        'subsurface_eff_n': '0.05',
        'subsurface_eff_p': '0.01',
        'threshold_flow_accumulation': '500',
        'workspace_dir': WORKSPACE_DIR,
    }

    # Create output folders if they don't exist
    if not os.path.exists(WORKSPACE_DIR):
        os.makedirs(WORKSPACE_DIR)
        print("Created output folder " + str(WORKSPACE_DIR))
    if not os.path.exists(POST_PROC_DIR):
        os.makedirs(POST_PROC_DIR)
        print("Created output folder " + str(POST_PROC_DIR))
    if not os.path.exists(ADJUSTED_TABLE_DIR):
        os.makedirs(ADJUSTED_TABLE_DIR)
        print("Created output folder " + str(ADJUSTED_TABLE_DIR))


    # Open final output sensitivity table
    #   - will be written to as each NDR run is done and post-processed
    results_file = open(OUTPUT_RESULT_TABLE_PATH, 'w')
    results_file.write("ws_id, param, param_value, modeled_n_export, observed_n, percent_error\n")
    

    ##############################################################################
    #
    # Tweaking UI parameters - Kb, Threshold flow accumulation,
    #   subsurface critical length and subsurface max retention efficiency
    #
    # ##############################################################################
    
    #
    # Runs changing Kb
    #

    print("\n********************************************************")
    print("*** Processing Kb")
    print("********************************************************")

    # Do runs with Kb = 0.5 through Kb = 3.5 in increments of 0.5
    KB_SAMPLE_SPACE = numpy.linspace(0.5, 3.5, num=7, endpoint=True)
    
    for k_param in KB_SAMPLE_SPACE:
        local_args = args.copy()
        local_args['k_param'] = k_param
        
        # Run NDR
        # MODIFY THIS #
        local_args['results_suffix'] = "SanIgnacio_Kb_" + str(k_param)
        print("Running NDR with Kb = " + str(k_param))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with Kb = " + str(k_param))


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "Kb", k_param, modeled_n, OBSERVED_VALUE_N, error_n))
        
        print("Done post-processing\n")
        

    #
    # Runs changing threshold flow accumulation
    #

    print("\n********************************************************")
    print("*** Processing threshold flow accumulation")
    print("********************************************************")
    
    # Do runs with Threshold Flow Accumulation = 100 through 800 in increments of 100
    TFA_SAMPLE_SPACE = numpy.linspace(100, 800, num=8, dtype=int, endpoint=True)
    
    for tfa_param in TFA_SAMPLE_SPACE:
        local_args = args.copy()
        local_args['threshold_flow_accumulation'] = tfa_param
        
        # Run NDR
        # MODIFY THIS #
        local_args['results_suffix'] = "SanIgnacio_TFA_" + str(tfa_param)
        print("\nRunning NDR with TFA = " + str(tfa_param))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with TFA = " + str(tfa_param))


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "TFA", tfa_param, modeled_n, OBSERVED_VALUE_N, error_n))
            
        print("Done post-processing\n")

    #
    # Runs changing subsurface critical length N
    #

    print("\n********************************************************")
    print("*** Processing subsurface critical length N ")
    print("********************************************************")

    # Do runs with subsurface critical length = 100 through 1000 in increments of 100
    sub_critlen_sample_space = numpy.linspace(30, 300, num=10, dtype=int, endpoint=True)
    
    for critlen in sub_critlen_sample_space:
        local_args = args.copy()
        local_args['subsurface_critical_length_n'] = critlen
        
        # Run NDR
        # MODIFY THIS #
        local_args['results_suffix'] = "SanIgnacio_sub_critlen_n_" + str(critlen)
        print("\nRunning NDR with subsurface critical length N = " + str(critlen))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with subsurface critical length N = " + str(critlen))


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "subsurface critical length", critlen, modeled_n, OBSERVED_VALUE_N, error_n))
            
        print("Done post-processing\n")

        
    #
    # Runs changing subsurface max retention efficiency N
    #

    print("\n********************************************************")
    print("*** Processing subsurface max retention efficiency N")
    print("********************************************************")
    
    # Do runs with max retention efficiency set from 0.05 to 0.95 in increments of 0.1
    sub_maxret_sample_space = numpy.linspace(.05, .95, num=9, endpoint=True)
    
    for maxret in sub_maxret_sample_space:
    
        local_args = args.copy()
        local_args['subsurface_eff_n'] = maxret
        
        # Run NDR
        # MODIFY THIS #
        local_args['results_suffix'] = "SanIgnacio_sub_eff_n_" + str(maxret)
        print("\nRunning NDR with subsurface max retention efficiency N = " + str(maxret))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with subsurface max retention efficiency N = " + str(maxret))


        print("Post-processing...")

        
        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "subsurface max retention efficiency N", maxret, modeled_n, OBSERVED_VALUE_N, error_n))
            
        print("Done post-processing\n")


        

    #############################################################################
    
    ### Tweaking biophysical table parameters, one at a time
    
    #############################################################################
    
    
    # Read in original biophysical table 
    orig_biophys_table = os.path.join(
            # MODIFY THIS #
            DATA_BASE_DIR, 'Biophysical_table_Belize_base_sensitivity.csv')
    # Copy the original table into the Workspace to work with subsequently, just in case
    shutil.copy(orig_biophys_table, WORKSPACE_DIR)
    # MODIFY THIS #
    orig_table_path = os.path.join(WORKSPACE_DIR, 'Biophysical_table_Belize_base_sensitivity.csv')   

    

    print("\n********************************************************")
    print("*** Processing load_n")
    print("********************************************************")

    # Multipliers applied to load_n, eff_n
    #   (.5x default value) -> (2x default value), in increments of .25x
    multiplier_sample_space = numpy.linspace(0.5, 2, num=7, endpoint=True)
    
    
    # Multipliers are applied across all LULC classes at once
    for mult in multiplier_sample_space:

        # Try pandas for table/data manipulation
        working_biophys_table = open(orig_table_path, 'r')
        df_biophys = pandas.read_csv(working_biophys_table)

        # Change biophysical table values for load_n
        df_biophys['load_n'] *= mult

        # Write updated table to a new CSV, which will be used to run NDR
        new_biophys_table_path = (
            os.path.join(ADJUSTED_TABLE_DIR, 'new_biophys_table_SanIgnacio_load_n_' + str(mult)+ '.csv'))
        new_biophys_table = open(new_biophys_table_path, 'w')
        df_biophys.to_csv(new_biophys_table)
        new_biophys_table.close()
       
        # Run NDR
        # MODIFY THIS #
        local_args = args.copy()
        local_args['results_suffix'] = "SanIgnacio_load_n_" + str(mult)
        local_args['biophysical_table_path'] = new_biophys_table_path
        print("\nRunning NDR with load_n * " + str(mult))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with load_n * " + str(mult))


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "load_n (mult)", mult, modeled_n, OBSERVED_VALUE_N, error_n))
            
        print("Done post-processing\n")


    #
    # Runs changing eff_n
    #

    print("\n********************************************************")
    print("*** Processing eff_n")
    print("********************************************************")

    # Multipliers applied to load_n, eff_n
    #   (.5x default value) -> (2x default value), in increments of .25x
    multiplier_sample_space = numpy.linspace(0.5, 2, num=7, endpoint=True)
    
    # Multipliers are applied across all LULC classes at once
    for mult in multiplier_sample_space:

        # Try pandas for table/data manipulation
        working_biophys_table = open(orig_table_path, 'r')
        df_biophys = pandas.read_csv(working_biophys_table)

        # Change biophysical table values for eff_n
        #   multiplying each LULC class' eff_n value by the multiplier
        df_biophys['eff_n'] *= mult

        # If resulting efficiency is > 1.0, limit it to 1.0
        #   (can't have > 100% efficiency)
        df_biophys.loc[df_biophys['eff_n'] > 1.0, 'eff_n'] = 1.0

        # Write updated table to a new CSV, which will be used to run NDR
        new_biophys_table_path = (
            os.path.join(ADJUSTED_TABLE_DIR, 'new_biophys_table_SanIgnacio_eff_n_' + str(mult)+ '.csv'))
        new_biophys_table = open(new_biophys_table_path, 'w')
        df_biophys.to_csv(new_biophys_table)
        new_biophys_table.close()

        # Run NDR
        # MODIFY THIS #
        local_args = args.copy()
        local_args['results_suffix'] = "SanIgnacio_eff_n_" + str(mult)
        local_args['biophysical_table_path'] = new_biophys_table_path
        print("\nRunning NDR with eff_n * " + str(mult))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with eff_n * " + str(mult))                               


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "eff_n (mult)", mult, modeled_n, OBSERVED_VALUE_N, error_n))
                    
        print("Done post-processing\n")



    #
    # Runs changing crit_len_n
    #

    print("\n********************************************************")
    print("*** Processing crit_len_n")
    print("********************************************************")

    # Increment for adjusting (surface) crit_len_n
    #   min 30, max 300 in increments of 30
    # Increment is applied across all LULC classes at once

    # Start with crit_len value of 30
    critlen = 30
    
    while critlen <= 300:

        # Try pandas for table/data manipulation
        working_biophys_table = open(orig_table_path, 'r')
        df_biophys = pandas.read_csv(working_biophys_table)

        df_biophys['crit_len_n'] = critlen

        # Write updated table to a new CSV, which will be used to run NDR
        # MODIFY THIS #
        new_biophys_table_path = (
            os.path.join(ADJUSTED_TABLE_DIR, 'new_biophys_table_SanIgnacio_surf_critlen_' + str(critlen)+ '.csv'))
        new_biophys_table = open(new_biophys_table_path, 'w')
        df_biophys.to_csv(new_biophys_table)
        new_biophys_table.close()

        # Run NDR
        # MODIFY THIS #
        local_args = args.copy()
        local_args['results_suffix'] = "SanIgnacio_surf_critlen" + str(critlen)
        local_args['biophysical_table_path'] = new_biophys_table_path
        print("\nRunning NDR with crit_len_n = " + str(critlen))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with crit_len_n = " + str(critlen))


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "crit_len_n", critlen, modeled_n, OBSERVED_VALUE_N, error_n))
            
        print("Done post-processing\n")


        # Increment critlen by 100 for the next run
        critlen += 30

    

    print("\n********************************************************")
    print("*** Processing proportion_subsurface_n")
    print("********************************************************")


    # Do runs with proportion_subsurface_n set from 0 to 1 in increments of 0.2
    psubn_sample_space = numpy.linspace(0, 1.0, num=6, endpoint=True)

    # Multipliers are applied across all LULC classes at once
    for psubn in psubn_sample_space:
    
        # Try pandas for table/data manipulation
        working_biophys_table = open(orig_table_path, 'r')
        df_biophys = pandas.read_csv(working_biophys_table)

        # Change biophysical table values for proportion_subsurface_n
        df_biophys['proportion_subsurface_n'] = psubn

        # Write updated table to a new CSV, which will be used to run NDR
        # MODIFY THIS #
        new_biophys_table_path = (
            os.path.join(ADJUSTED_TABLE_DIR, 'new_biophys_table_SanIgnacio_prop_sub_n_' + str(mult)+ '.csv'))
        new_biophys_table = open(new_biophys_table_path, 'w')
        df_biophys.to_csv(new_biophys_table)
        new_biophys_table.close()

        # Run NDR
        # MODIFY THIS #
        local_args = args.copy()
        local_args['results_suffix'] = "SanIgnacio_prop_sub_n_" + str(mult)
        local_args['biophysical_table_path'] = new_biophys_table_path
        print("\nRunning NDR with proportion_subsurface_n * " + str(mult))
        natcap.invest.ndr.ndr.execute(local_args)
        print("Done running NDR with proportion_subsurface_n * " + str(mult))         


        print("Post-processing...")

        N_EXPORT_SHAPEFILE_PATH = os.path.join(WORKSPACE_DIR, 'watershed_results_ndr_' + str(local_args['results_suffix']) + '.shp')

        # Extract aggregated data from the aggregate output shapefile for N
        watershed_vector = ogr.Open(N_EXPORT_SHAPEFILE_PATH)
        watershed_layer = watershed_vector.GetLayer()
        watershed_feature = watershed_layer.GetFeature(0)
        ws_id = watershed_feature.GetField('ws_id')
        modeled_n = float(watershed_feature.GetField('n_exp_tot'))
        error_n = ((modeled_n - OBSERVED_VALUE_N) / float(OBSERVED_VALUE_N)) * 100

        del watershed_layer
        del watershed_vector
        
        # Write data to the output sensitivity table
        results_file.write('%s,%s,%f,%f,%f,%f\n' % (ws_id, "proportion_subsurface_n (mult)", psubn, modeled_n, OBSERVED_VALUE_N, error_n))

        print("Done post-processing\n")
         

    ###############################################################################

    #
    # Finish things up
    #

    # Close output sensivity table file
    results_file.close()
    
    # How long did it take to run all of this?
    elapsed_time = (time.time() - start_time)/60
    print("\nelapsed time: " + str(elapsed_time) + " minutes")
    
#####################################################################################


if __name__ == '__main__':
    main()

#####################################################################################
