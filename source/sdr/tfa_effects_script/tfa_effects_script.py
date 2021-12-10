from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt
import pygeoprocessing
import numpy


stream_tfa_100_path = 'stream_100.tif'
stream_tfa_400_path = 'stream_400.tif'
stream_tfa_1000_path = 'stream_1000.tif'
sdr_tfa_100_path = 'sdr_factor_100.tif'
sdr_tfa_400_path = 'sdr_factor_400.tif'
sdr_tfa_1000_path = 'sdr_factor_1000.tif'
# mask_tfa_100_path = 'mask_100.tif'
# mask_tfa_400_path = 'mask_400.tif'
# mask_tfa_1000_path = 'mask_1000.tif'

fig, (
    (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)
) = plt.subplots(3, 3, figsize=(9, 9), dpi=200)

for ax in (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9):
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_axis_off()


def plot_raster(raster, ax, colormap_name, nodata_color='white'):
    """Plot a raster as an image.

    Args:
        raster (str): path to the raster file to plot
        ax (matplotlib.axes.Axes): Axes instance to plot on
        colormap_name (str): name of a colormap recognized by matplotlib
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

    colormap = get_cmap(colormap_name).copy()
    colormap.set_bad(nodata_color)  # set color to use for masked values
    ax.imshow(masked_array, cmap=colormap, origin='upper', aspect='equal',)


plot_raster(stream_tfa_100_path, ax1, 'gray')
plot_raster(stream_tfa_400_path, ax2, 'gray')
plot_raster(stream_tfa_1000_path, ax3, 'gray')
plot_raster(sdr_tfa_100_path, ax4, 'viridis')
plot_raster(sdr_tfa_400_path, ax5, 'viridis')
plot_raster(sdr_tfa_1000_path, ax6, 'viridis')
# plot_raster(mask_tfa_100_path, ax7, 'gray')
# plot_raster(mask_tfa_400_path, ax8, 'gray')
# plot_raster(mask_tfa_1000_path, ax9, 'gray')

# Add labels
y_min, y_max = ax1.get_ybound()  # all the rasters have the same shape
y_center = (y_max - y_min) / 2
x_min, x_max = ax1.get_xbound()
x_center = (x_max - x_min) / 2

ax1.text(-5, y_center, 'streams', va='center', ha='right', fontsize=14)
ax4.text(-5, y_center, 'SDR', va='center', ha='right', fontsize=14)
# ax7.text(-5, y_center, 'mask', va='center', ha='right', fontsize=14)
ax1.text(x_center, -1, 'TFA: 100', va='bottom', ha='center', fontsize=14)
ax2.text(x_center, -1, 'TFA: 400', va='bottom', ha='center', fontsize=14)
ax3.text(x_center, -1, 'TFA: 1000', va='bottom', ha='center', fontsize=14)

plt.savefig('tfa_effects.png')
