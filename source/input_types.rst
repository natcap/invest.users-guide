***********
Input Types
***********

InVEST models accept many different types of spatial and non-spatial data. We categorize them into 12 types:

.. _number:

number
------
A scalar value. You may enter numbers in integer or floating-point format. Fractions are not allowed.

.. _ratio:

ratio
-----
A unitless proportion in the range 0 - 1, where 0 represents "none" and 1 represents "all".
Some ratio inputs may be less than 0 or greater than 1, while others are strictly limited to the 0-1 range.

.. _percent:

percent
-------
A unitless proportion in the range 0 - 100, where 0 represents "none" and 100 represents "all".
Some percent inputs may be less than 0 or greater than 100, while others are strictly limited to the 0-100 range.

.. _code:

code
----
An integer that serves to uniquely identify something.
Because rasters can only store numeric data, it is common to use integer codes as labels that map to non-numeric data
(such as land use/landcover types and soil groups).

.. _text:

text
----

.. _option:

option
------
A choice from a fixed set of options.


.. _truefalse:

true/false
----------


.. _csv:

csv
---
A table of data stored in a .csv (Comma-Separated Value) format. You may use any spreadsheet software to create and edit a table, and then export it to CSV format.


.. _raster:

raster
------
A spatial data file that stores data in pixels, which each have a numeric value.
InVEST accepts all GDAL-supported raster formats, including GeoTiff (.tif) and many more.
For the complete list, see https://gdal.org/drivers/raster/index.html.

Bands
~~~~~
Rasters may have multiple bands. All InVEST models look at the first band only. If you are using a multi-band raster,
please be sure that the correct dataset is in the first band.

Nodata values
~~~~~~~~~~~~~
Rasters may have a *nodata* value that indicates areas where no data exists. Pixels with this value are excluded from calculations.
The nodata value must be encoded in the raster's metadata (otherwise, InVEST won't know what it is).

Incorrectly set nodata values are a very common cause of user problems with InVEST. Some common mistakes:

- Not setting a nodata value. It is common to use a value, like 0 or -1, to represent nodata areas.
  If that value is not set in the raster metadata, InVEST won't know that, and will treat them as valid data.
  This will cause incorrect results or an error. It is only acceptable not to set a nodata value if every pixel
  in your raster has valid data.

- Setting the nodata value incorrectly. It is strongly recommended to double-check that the nodata value is as expected.
  You can view your raster's metadata, including the nodata value, in your GIS software.

- Using an unsuitable nodata value. It is important to make sure that (1) the nodata value works with the raster's data type
  and (2) the nodata value will never conflict with real data.

  Every raster has a *data type* which determines the minimum and maximum value that each pixel can have. Some data types allow positive and negative numbers, while others only allow positive numbers. If your raster data type only allows positive numbers,
  make sure that your nodata value is not negative. Using a negative nodata value in an unsigned (positive-only) raster will cause unexpected results: for example, using -1 in an *unsigned 8-bit integer* raster will make those values "wrap around" to 255, the maximum 8-bit integer value.

-1 is a good choice of nodata value if both of these conditions are met:
    1. the data is always non-negative, and
    2. the raster's data type is signed (meaning it allows negative values)

If these conditions are not met, the maximum value for the data type is a good choice. The minimum value may also be used for
signed data types (do not use the minimum value for unsigned types: it is 0, which is usually a valid data value). These are good choices because they are usually much larger or smaller than the range of the valid data, so they will not conflict.

Discrete data is the only exception: for a raster of integer codes such as an LULC raster, you may choose any value in the data type's range that is not a valid code.


.. _vector:

vector
------
A spatial data file that stores data in geometric shapes, which each may have multiple data attributes.
InVEST accepts all GDAL-supported vector formats, including GeoPackage (.gpkg), ESRI Shapefile (.shp), and many more.
For the complete list, see https://gdal.org/drivers/vector/index.html.

.. _directory:

directory
---------
A folder that may or may not need to contain other files or folders used by the model.

.. _file:

file
----
Any other type of file not listed above.


