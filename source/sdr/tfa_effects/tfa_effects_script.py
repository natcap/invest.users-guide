import os
import shutil
import sys
import tempfile

from matplotlib.cm import get_cmap
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from natcap.invest.sdr import sdr
import numpy
import pygeoprocessing


test_data_dir = sys.argv[1]
sdr_data_dir = os.path.join(test_data_dir, 'sdr', 'input')
workspace_dir = tempfile.mkdtemp()

args = {
    'biophysical_table_path': os.path.join(sdr_data_dir, 'biophysical_table.csv'),
    'dem_path': os.path.join(sdr_data_dir, 'dem.tif'),
    'erodibility_path': os.path.join(sdr_data_dir, 'erodibility_SI_clip.tif'),
    'erosivity_path': os.path.join(sdr_data_dir, 'erosivity.tif'),
    'ic_0_param': '0.5',
    'k_param': '2',
    'l_max': '122',
    'lulc_path': os.path.join(sdr_data_dir, 'landuse_90.tif'),
    'sdr_max': '0.8',
    'watersheds_path': os.path.join(sdr_data_dir, 'watersheds.shp'),
    'workspace_dir': workspace_dir,
}

for tfa_value in [100, 400, 1000]:
    args['threshold_flow_accumulation'] = tfa_value
    args['results_suffix'] = str(tfa_value)
    sdr.execute(args)

intermediate_dir = os.path.join(workspace_dir, 'intermediate_outputs')

stream_tfa_100_path = os.path.join(workspace_dir, 'stream_100.tif')
stream_tfa_400_path = os.path.join(workspace_dir, 'stream_400.tif')
stream_tfa_1000_path = os.path.join(workspace_dir, 'stream_1000.tif')
sdr_tfa_100_path = os.path.join(intermediate_dir, 'sdr_factor_100.tif')
sdr_tfa_400_path = os.path.join(intermediate_dir, 'sdr_factor_400.tif')
sdr_tfa_1000_path = os.path.join(intermediate_dir, 'sdr_factor_1000.tif')
mask_tfa_100_path = os.path.join(intermediate_dir, 'what_drains_to_stream_100.tif')
mask_tfa_400_path = os.path.join(intermediate_dir, 'what_drains_to_stream_400.tif')
mask_tfa_1000_path = os.path.join(intermediate_dir, 'what_drains_to_stream_1000.tif')

fig, (
    (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)
) = plt.subplots(3, 3, figsize=(9, 9), dpi=200)

for ax in (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9):
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_axis_off()


def plot_raster(raster, ax, colormap, nodata_color=(0, 0, 0, 0)):
    """Plot a raster as an image.

    Args:
        raster (str): path to the raster file to plot
        ax (matplotlib.axes.Axes): Axes instance to plot on
        colormap_name (str | Colormap): colormap with which to color the raster
            image. May be a Colormap object, or the name of a Colormap
            recognized by matplotlib.
        nodata_color: color to use for nodata pixels. this may be any color
            representation recognized by matplotlib (string, RGB tuple, etc)

    Returns:
        None
    """
    array = pygeoprocessing.raster_to_numpy_array(raster)
    nodata = pygeoprocessing.get_raster_info(raster)['nodata'][0]
    valid_mask = ~numpy.isclose(array, nodata, equal_nan=True)

    data_max, data_min = array[valid_mask].max(), array[valid_mask].min()
    data_range = data_max - data_min
    normalized_array = numpy.zeros(array.shape, dtype=numpy.float32)
    normalized_array[valid_mask] = (array[valid_mask] - data_min) / data_range
    masked_array = numpy.ma.array(normalized_array, mask=~valid_mask)

    if isinstance(colormap, str):
        colormap = get_cmap(colormap).copy()

    colormap.set_bad(nodata_color)  # set color to use for masked values
    ax.imshow(masked_array, cmap=colormap, origin='upper', aspect='equal',)


binary_colormap = ListedColormap(['orangered', 'limegreen'])

plot_raster(stream_tfa_100_path, ax1, 'gray')
plot_raster(stream_tfa_400_path, ax2, 'gray')
plot_raster(stream_tfa_1000_path, ax3, 'gray')
plot_raster(sdr_tfa_100_path, ax4, 'viridis')
plot_raster(sdr_tfa_400_path, ax5, 'viridis')
plot_raster(sdr_tfa_1000_path, ax6, 'viridis')
plot_raster(mask_tfa_100_path, ax7, binary_colormap)
plot_raster(mask_tfa_400_path, ax8, binary_colormap)
plot_raster(mask_tfa_1000_path, ax9, binary_colormap)

# Add labels
y_min, y_max = ax1.get_ybound()  # all the rasters have the same shape
y_center = (y_max - y_min) / 2
x_min, x_max = ax1.get_xbound()
x_center = (x_max - x_min) / 2

ax1.text(-5, y_center, 'streams', va='center', ha='right', fontsize=14)
ax4.text(-5, y_center, 'SDR', va='center', ha='right', fontsize=14)
ax7.text(-5, y_center, 'drains to\nstream?', va='center', ha='right', fontsize=14)
ax1.text(x_center, -1, 'TFA: 100', va='bottom', ha='center', fontsize=14)
ax2.text(x_center, -1, 'TFA: 400', va='bottom', ha='center', fontsize=14)
ax3.text(x_center, -1, 'TFA: 1000', va='bottom', ha='center', fontsize=14)

plt.savefig('tfa_effects.png')
plt.show()

shutil.rmtree(workspace_dir)
