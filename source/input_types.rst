***********
Input Types
***********

InVEST models accept many different types of spatial and non-spatial data. We categorize them into 12 types:

.. _number:

number
------
A scalar value. You may enter numbers in integer or floating-point format. Fractions are not allowed.

Units
~~~~~
Most numeric inputs have units. InVEST models use standard SI units and symbols as much as possible. For definitions of these symbols, see `SI Units <https://en.wikipedia.org/wiki/International_System_of_Units#Units_and_prefixes>`_ and `units accepted for use with SI <https://en.wikipedia.org/wiki/Non-SI_units_mentioned_in_the_SI#Units_officially_accepted_for_use_with_the_SI>`_.

InVEST also uses the non-SI unit *years*.

When the unit is *currency*, any currency may be used, but the same currency must be used throughout the model.


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

.. _integer:

integer
-------
A whole number (positive or negative). Integers are often used to uniquely identify something.
Because rasters can only store numeric data, it is common to use integer codes as labels that map to non-numeric data
(such as land use/landcover types and soil groups).

.. _text:

text
----
Freeform text. InVEST accepts any Unicode character. For best results, use Unicode character sets for non-Latin alphabets.

.. _option:

option
------
A choice from a fixed set of options. Options are usually displayed as a dropdown menu. Some CSV inputs have columns that must contain values from a fixed set of options. In that case, be sure to enter the options exactly as they are written.


.. _truefalse:

true/false
----------
True/false inputs are usually displayed as a checkbox. Some CSV inputs have true/false columns. In that case, the model's documentation will explain exactly how to enter the values (``TRUE`` or ``FALSE``, ``1`` or ``0``, etc.)


.. _csv:

CSV
---
A table of data stored in a .csv (comma-separated value) format. You may use any spreadsheet software to create and edit a table, and then export it to CSV format.


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


.. _datatypes:

Data types
~~~~~~~~~~
Every raster has a *data type* which determines the minimum and maximum value that each pixel can have. Some data types allow positive and negative numbers, while others only allow positive numbers. Most of the time you will not need to change your raster's data type, but it is important to be aware of.

Understanding data types
^^^^^^^^^^^^^^^^^^^^^^^^
A raster's data type is displayed as a code in the raster metadata, which may be viewed in your GIS software. A data type code has 3 components:

1. Unsigned marker (**u**), optional

   By default, data types are signed, meaning that they include a sign (+ or -) indicating whether the number is positive or negative.
   You need a signed data type to store negative data.
   If a data type begins with a **u**, that means it is unsigned. All unsigned data is positive. If you do not need to store negative data,myou can save space by using an unsigned type.

   This distinction only exists for integer data types. Float types are always signed.

2. Type (**float** or **int**)

   Floating-point (float) types can store digits after the decimal point. There is no hard limit on how many decimal places they can store, but they are only accurate to a limited number of total digits (before and after the decimal point).
   Integer (int) types can only store whole numbers. They have perfect accuracy.
   It is best to use integer data types when possible for discrete data.

3. Size (**8, 16, 32, 64**)

   This is how many bits are used to store the number. It determines the range of numbers that can fit into the data type.
   You can save space by using the smallest size that works for your data. For example, the large numbers available in a **float64** raster are rarely needed. The **float32** range is sufficient for most real-world data, and it uses half as much space.
   The **uint8** type is sufficient for most discrete data that InVEST uses (land use/land cover classes, soil groups, and so on) which have fewer than 256 possible values.

Here are all the standard raster data types and their ranges (ranges include the starting and ending values):

- **byte** (**uint8**): any integer from 0 to 255
- **uint16**: any integer from 0 to 65,535
- **uint32**: any integer from 0 to 4.2x10 :sup:`9`
- **int16**: any integer from -32,768 to 32,767
- **int32**: any integer from -2.1x10 :sup:`9` to 2.1x10 :sup:`9`
- **float32**: any number from -3.4x10 :sup:`38` to 3.4x10 :sup:`38` (accurate to about 7 digits)

  .. note::
     Larger numbers are accurate to fewer decimal digits. Numbers larger than 2 :sup:`23` (about 8,000,000) use all 7 digits on the left side of the decimal point and cannot have any decimal part at all. Most real-world data has fewer than 7 significant figures so this is not a problem. If you do need decimal precision for such large numbers, use **float64** instead.

- **float64**: any number from -1.7x10 :sup:`308` to 1.7x10 :sup:`308` (accurate to about 16 digits)

.. note::
   A **signed byte** type (**int8**, -128 to 127) also exists. ArcGIS in particular may produce signed byte rasters. Because GDAL does not directly support the **int8** type, we recommend avoiding it. InVEST works around this to allow the **int8** type in some cases. If you must use an **int8** raster, it is even more important to check that your intermediate and final results make sense.


Nodata values
~~~~~~~~~~~~~
Rasters may have a *nodata* value that indicates areas where no data exists. Pixels with this value are excluded from calculations.
The nodata value must be encoded in the raster's metadata (otherwise, InVEST won't know what it is).

Choosing a nodata value
^^^^^^^^^^^^^^^^^^^^^^^
A good choice of nodata value is well outside the range of real data values, while still being within the raster data type's range.

-1 is a good choice of nodata value if both of these conditions are met:

- the data is always non-negative, and
- the raster's data type is signed

If these conditions are not met, the maximum value for the data type is a good choice. The minimum value may also be used for
signed data types (do not use the minimum value for unsigned types: it is 0, which is usually a valid data value). These are good choices because they are usually much larger or smaller than the range of the valid data, so they will not conflict.
Discrete data is the only exception: for an integer raster such as land use/land cover, you may choose any value in the data type's range that is not a valid data value.

These recommendations are summarized in the table below.

+------------------------------------+----------------------------+-------------------------+-----------------------------------------+
| **Continuous data (float data types)**                                                    | **Discrete data (integer data types)**  |
+====================================+============================+=========================+=========================================+
|                                    | **Signed** data type       | **Unsigned** data type  | Any integer in the data type range      |
+------------------------------------+----------------------------+-------------------------+ that is not a valid data value          |
| All valid data is **non-negative** | -1                         | Data type maximum value | (commonly 0, -1, or the data type       |
+------------------------------------+----------------------------+-------------------------+ maximum or minimum)                     |
| Valid data may be **negative**     | Data type maximum or       |                         |                                         |
|                                    | minimum value              |                         |                                         |
+------------------------------------+----------------------------+-------------------------+-----------------------------------------+


Common problems
^^^^^^^^^^^^^^^
Incorrectly set nodata values are a very common cause of user problems with InVEST. Some common mistakes are:

- Not setting a nodata value. It is common to use a value, like 0 or -1, to represent nodata areas.
  If that value is not set in the raster metadata, InVEST will treat it like valid data.
  This will cause incorrect results or an error. You must set a nodata value unless every pixel in your raster has valid data (this is uncommon). You can view and edit your raster's metadata, including the nodata value, in your GIS software.

- Using an unsuitable nodata value. Your nodata value must:

  - be within the range allowed by the raster's :ref:`data type <datatypes>`. Using a value outside this range can cause unexpected results.
  - not conflict with real data. Make sure it is well outside the range of possible data values.


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


