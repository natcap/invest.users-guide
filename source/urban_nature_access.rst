.. _urban_nature_access:

*******************
Urban Nature Access
*******************

TODOS
=====

- [ ] Add recommendations for guidance on per-capita greenspace requirements.

Summary
=======

Introduction
============

Nature in urban areas provides important opportunities for recreation.  The
model for urban nature access provides a measure of both the supply of urban
nature and the demand for nature by the urban population (optionally, different
groups within the urban population), ultimately calculating the balance between
supply and demand.  Supply is determined by the quantity and size of urban
nature that is accessible per capita for recreational purposes.  The demand is
determined per capita natural space that is required by policy.  The balance is
determined by assessing to what extent supply meets demand, at the individual,
administrative and city level.

The model consists of a default model, in which the number of inhabitants and
an aggregated metric of nature in the form of overall greenspace are used.
While the model is capable of modelling different types of urban nature,
including water edges, here we focus on the use of the model for greenspace to
refer to greenspace instead of urban nature from this point on.

Three options to develop a more detailed model are also provided:

* Search radii may be defined for each greenspace classification
* Search radii may be defined for individual population groups
* Results may be summarized to individual population groups regardless of the
  search radius mode selected.

The three additions for detailed modelling are optional.

The Model
=========

Greenspace area supplied to any pixel :math:`i` in the study area is calculated
using greenspace area :math:`S_j` in a green pixel, population in pixel
:math:`i`, :math:`P_i`.

Decay Function
--------------

Service decays with distance between greenspace and population which can be
described by the decay function :math:`f(d_{ij})` where :math:`d_{ij}` is the
distance between greenspace and a population pixel.  Several functions have
been used in previous studies and are provided in the model.  The user's
selection of decay function is applied consistently throughout the model,
regardless of the search radius mode selected.  Search distance is always
euclidean distance and assumes square pixels.

Dichotomy
*********

The dichotomous kernel considers all pixels within the search distance
:math:`d_0` to be equally accessible to greenspace.  More formally:

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                1 & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}

Exponential
***********

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                e^{(-d_{ij}/d_0)} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}

Power
*****

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                d_{ij}^{(-\beta)} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}

Gaussian
********

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                \frac{e^{-\frac{1}{2}\left ( \frac{d_{ij}}{d_0} \right )^2}-e^{-\frac{1}{2}}}{1-e^{-\frac{1}{2}}} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}


Density
*******

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                \frac{3}{4}\left(1-\left(\frac{d_{ij}}{d_{0}}\right)^{2}\right) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}


Running the Core Model
----------------------

The core model assumes a uniform radius of travel ("search radius") that is
defined by the user.


Two-Step Floating Catchment Area (2SFCA)
****************************************

This method is used to calculate the greenspace supply to each pixel (Mao and
Nekorchuk, 2013; Xing et al., 2018).  Given a greenspace pixel :math:`j`, all
population pixels with the search radius :math:`d_0` are searched.  The
greenspace-population ratio :math:`R_j` for this pixel is calculated using the
greenspace pixel's area :math:`S_j` divided by the total population within the
search radius, weighted according to the selected search kernel's
distance-based weighting.  Then, centered on each pixel in the population
raster, all the greenspace pixels within its distance-weighted catchment are
searched.  All of the :math:`R_j` of these greenspace pixels are summed to
calculate the greenspace supply :math:`A_i` to every population pixel.

More formally, the greenspace/population ratio :math:`R_j` is defined as:

.. math::

        \begin{align*}
        R_j &= \left\{\begin{array}{lr}
                \frac{S_j}{\sum_{k \in \left\{d_{jk} \leq d_0  \right\}} P_k \cdot f(d_{jk})} & \text{if} P_k \cdot f(d_{jk}) >= 1 \\
                S_j & \text{otherwise} \\
        \end{array}\right\} \\
        \end{align*}

Where:

* :math:`R_j` is the greenspace/population ratio of greenspace pixel :math:`j`.
* :math:`S_j` is the area of greenspace in pixel :math:`j`
* :math:`d_0` is the search radius
* :math:`k` is the population pixel within search radius of greenspace pixel :math:`j`
* :math:`d_jk` is the distance between greenspace pixel :math:`j` and population pixel :math:`k`.
* :math:`P_k` is the population of pixel :math:`k`.
* :math:`f(d)` is the selected decay function.


Then, the greenspace/population ratio is weighted by the selected decay
function and summed within the search radius to give greenspace supply,
:math:`A_i`:

.. math::

        A_i = \sum_{j \in \left\{d_{ij} \leq d_0  \right\}} R_j \cdot f(d_{ij})

Where:

* :math:`i` is any pixel in the population raster
* :math:`A_i` is the greenspace per capita supplied to pixel :math:`i` (square meters per person)
* :math:`d_ij` is the distance between pixel :math:`i` and greenspace pixel :math:`j`.
* :math:`d_0` is the search radius


Calculate Per-Capita Greenspace Demand
**************************************

Every resident in a region should be allocated a certain amount of greenspace,
:math:`g_{cap}` which is often defined in local planning documents or urban
planning goals.  The per-capita greenspace supply/demand budget
:math:`SUP\_DEM_{i,cap}` at pixel :math:`i`, is defined by assessing the
difference between the supplied greenspace and the planning foal for greenspace
per capita per pixel:

.. math::

        SUP\_DEM_{i,cap} = A_i - g_{cap}

To determine the budget for all people in every pixel, :math:`SUP\_DEM_{i,cap}`
is multiplied by the population :math:`P_i` at pixel :math:`i`:

.. math::

        SUP\_DEM_{i} = SUP\_DEM_{i,cap} \cdot P_i

Summarizing Outputs to Administrative Units
*******************************************

The user will input a vector with administrative unit boundaries that may
represent any district level that the user is interested in.  These boundaries
are needed to obtain administrative-level measurements.

The administrative level supply/demand budget is the sum of the budget of each
pixel :math:`i` within the administrative boundary :math:`adm`:

.. math::

        SUP\_DEM_{adm} = \sum_{i \in \left\{adm \right\}} SUP\_DEM_i

:math:`SUP\_DEM_{adm}` indicates how much greenspace, in square meters, is
under- or over-supplied in ad administrative unit.

The average per-capita greenspace supply/demand budget is also calculated at
the administrative level:

.. math::

        SUP\_DEM_{adm,cap} = \frac{SUP\_DEM_{adm}}{P_{adm}}

Where :math:`P_{adm}` is the total population within the administrative boundary.

When :math:`SUP\_DEM_{i,cap} < 0` on any given pixel :math:`i`, it indicates
that people in this pixel are under-supplied with greenspace.  Summing up these
populations across all pixels within an administrative unit provides the number
of people in an administrative unit with a greenspace deficit,
:math:`Pund_{adm}`, relative to the recommended greenspace :math:`g_{cap}`:

.. math::
        Pund_{adm} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i} & \text{if} SUP\_DEM_{i,cap} < 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}

Similarly, the same rationale is applied to find the number of people with a
greenspace surplus in an administrative unit, :math:`Povr_{adm}`, relative to the
recommended greenspace :math:`g_{cap}`:

.. math::
        Povr_{adm} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i} & \text{if} SUP\_DEM_{i,cap} > 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}


Running the Model with Radii Defined Per Greenspace Class
---------------------------------------------------------

Greenspace has different types. Pocket parks provide convenient recreation
experience nearby, while municipal parks attract people from more distant
places.  If the user has data to split the types of greenspace and the
adjusted travel distance for each type of greenspace, the accessibility of
each type of greenspace to pixel :math:`i` can be calculated using the
class-specific radius. These split greenspace types and their associated
search radii are provided to the model by user input in the LULC attribute
table.  Each type of Land Use Land Cover classification marked as greenspace
will be calculated separately in order to give more detailed results concerning
the accessible greenspace of each type.  Is is up to the user to decide how to
split the greenspace.

If :math:`r` is the type of greenspace, :math:`j` is a greenspace pixel of
:math:`r` type, :math:`d_{0,r}` is the search radius for :math:`r` type of
greenspace, then the greenspace/population ratio for this greenspace type
is calculated by the area of this greenspace divided by the population within
the radius weighted by the user's selection of distance-weighted decay
function:

.. math::
        R_{j,r} = \frac{S_{j,r}}{
                        \sum_{k \in \{d_{kj} \leq d_{0,r}\}}{P_k \cdot f(d_{jk})}
                }

The accessibility of greenspace type :math:`r`, :math:`A_{i,r}` to pixel
:math:`i` is calculated by summing up the distance-weighted :math:`R_{j,r}`
within the search radius:

.. math::
        A_{i,r} = \sum_{j \in d_{ij} \leq d_{0,r}}{R_{j,r} \cdot f(d_ij)}

The total greenspace supplied to pixel :math:`i`, :math:`A_i` is calculated by
adding up the :math:`A_{i,r}` across all types of greenspaces:

.. math::
        A_i = \sum_{r=1}^{r}{A_{i,r}}

Other steps and outputs are the same as in the core model.


Running the Model with Results Summarized by Population Groups
--------------------------------------------------------------

The user has the option to provide population characteristics indicating the
proportion of the total population that belong to the given population group
within each administrative unit.  Examples of population groups might be
age or income brackets.  The user will decide how to split the population
according to data availability and the study objective.

To analyze the supply-demand balance for certain groups within the general
population, an additional calculation is done for each group :math:`gn`,
given the proportion of the group in the total population of an administrative
unit, :math:`Rp,gn`.

For the undersupplied population within group :math:`gn` and administrative
unit :math:`adm`, this is defined as:

.. math::
        Pund_{adm,gn} = Pund_{adm} \cdot Rp,gn

And for the oversupplied population within group :math:`gn` and administrative
unit :math:`adm`:

.. math::
        Povr_{adm,gn} = Povr_{adm} \cdot Rp,gn

The user may wish to conduct further correlation analysis between population
characteristics and the above outputs to see if certain groups of people are
associated with deficit or surplus greenspace supply at different levels.







Data Needs
==========
It is up to the user to decide how to split the greenspace. For example,
greenspace might be split into three types: pocket parks (small greenspace
around residential areas), municipal parks (large, well-managed parks in a city
area) and suburban greenspaces such as forest, wood, grassland and some
agricultiral landscape while provide more wild recreation experiehnce.  We can
recommend a search radius for each of these greenspace types, e.g. pocket park
within 20 minutes' walk, municipal park: within 30 minutes car drive, and
suburban greenspace within 1 hours' car drive.
