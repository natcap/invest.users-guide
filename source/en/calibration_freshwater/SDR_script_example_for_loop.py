import logging
import sys
import os
import glob # Load mandatory Python libraries

import natcap.invest.sdr.sdr
import natcap.invest.utils # Load InVEST SDR model

LOGGER = logging.getLogger(__name__)
root_logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt=natcap.invest.utils.LOG_FMT,
    datefmt='%m/%d/%Y %H:%M:%S ')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler]) # Setup human-readable logging information and format

args = {
    'dem_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\DEM_SRTM_Luzon_90m.tif',
    'drainage_path': '',
    'erodibility_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\soil_erodibility_ISRIC_Luzon.tif',
    'erosivity_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\rainfall_erosivity_WorldClim_Luzon.tif',
    'ic_0_param': 0.5,
    'k_param': 2,
    'l_max': 122,
    'lulc_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\LULC_2020_Luzon.tif',
    'sdr_max': 0.8,
    'threshold_flow_accumulation': 1000,
    'watersheds_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\Luzon_AOI.shp',
    'workspace_dir': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\Calibration\\SDR_results', # Filepaths to each model input
} # UPDATE these filepaths to reflect the absolute paths on your computer

inputs_directory = r'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\' # Set "inputs_directory" to input data directory path for use in loop below

if __name__ == '__main__':
    for biophysical_table in glob.glob(os.path.join(inputs_directory, 'biophys*.csv')): # Assign files named "biophys*.csv" at path "inputs_directory" to "biophysical_table"
        args['biophysical_table_path'] = biophysical_table # Set the 'biophysical_table_path' InVEST input to "biophysical_table"
        args['results_suffix'] = 'Luzon_example_' + os.path.splitext(os.path.basename(biophysical_table))[0] # Set the 'results_suffix' InVEST input to "Luzon_example_[biophys*.csv]"
        natcap.invest.sdr.sdr.execute(args) # Run InVEST SDR model with this loop
