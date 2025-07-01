import logging
import sys # Load mandatory Python libraries

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
    'biophysical_table_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\biophysical_table_SDR_Yang2003_Luzon.csv',
    'dem_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\DEM_SRTM_Luzon_90m.tif',
    'drainage_path': '',
    'erodibility_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\soil_erodibility_ISRIC_Luzon.tif',
    'erosivity_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\rainfall_erosivity_WorldClim_Luzon.tif',
    'ic_0_param': 0.5,
    'k_param': 2,
    'l_max': 122,
    'lulc_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\LULC_2020_Luzon.tif',
    'results_suffix': 'Luzon_example',
    'sdr_max': 0.8,
    'threshold_flow_accumulation': 1000,
    'watersheds_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\Luzon_AOI.shp',
    'workspace_dir': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\Calibration\\SDR_results', # Filepaths to each baseline model input
} # UPDATE these filepaths to reflect the absolute paths on your computer

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args) # Run InVEST SDR model

args = {
    'biophysical_table_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\biophysical_table_SDR_Yang2003_Luzon.csv',
    'dem_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\DEM_SRTM_Luzon_90m.tif',
    'drainage_path': '',
    'erodibility_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\soil_erodibility_ISRIC_Luzon.tif',
    'erosivity_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\rainfall_erosivity_WorldClim_Luzon.tif',
    'ic_0_param': 0.5,
    'k_param': 1.8, # parameter value changed from run above
    'l_max': 122,
    'lulc_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\LULC_2020_Luzon.tif',
    'results_suffix': 'Luzon_example_kb1_8', # results filenames adjusted to reflect parameter change from baseline value
    'sdr_max': 0.8,
    'threshold_flow_accumulation': 1000,
    'watersheds_path': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\SDR_Luzon_example_inputs\\Luzon_AOI.shp',
    'workspace_dir': 'G:\\Shared drives\\GEF_GreenFin\\Pilot_Countries\\Philippines\\DENR_Stanford_sharing\\Calibration\\SDR_results', # Filepaths to each model input for adjusted parameter run
} # UPDATE these filepaths to reflect the absolute paths on your computer

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args) # Run InVEST SDR model
