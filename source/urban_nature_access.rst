.. _urban_nature_access:

*******************
Urban Nature Access
*******************

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

* additional greenspace types and adjusted search radii
* additional population characteristics (such as age, income, etc.)
* adjusted search radii for different groups within the population.

The three additions for detailed modelling are optional.

The Model
=========

Greenspace area supplied to any pixel :math:`i` in the study area is calculated
using greenspace area :math:`S_j` in a green pixel, population in pixel
:math:`i`, :math:`P_i`

Decay Function
--------------

Service decays with distance between greenspace and population which can be
described by the decay function :math:`f(d_{ij})` where :math:`d_{ij}` is the
distance between greenspace and a population pixel.  Several functions have
been used in previous studies and are provided in the model.

Dichotomy
*********

The dichotomous kernel considers all pixels within the search distance
:math:`d_0` to be equally accessible to greenspace.  More formally:

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                1 & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Exponential
***********

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                e^(-d_{ij}/d_0) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Power
*****

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                d_{ij}^(-\beta) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Gaussian
********

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                \frac{e^{-\frac{1}{2}\left ( \frac{d_{ij}}{d_0} \right )^2}-e^{-\frac{1}{2}}}{1-e^{-\frac{1}{2}}} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

- [ ] TODO: compare this to our existing gaussian kernel

Kernel Density
**************

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                \frac{3}{4}\left(1-\left(\frac{d_{ij}}{d_{0}}\right)^{2}\right) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Two-Step Floating Catchment Area (2SFCA)
----------------------------------------

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

.. math::

        \begin{align*}
        R_j &= \left\{\begin{array}{lr} \\
                \frac{S_j}{\sum_{k \in \left\{d_{jk} \leq d_0  \right\}} P_k \cdot f(d_{jk})} & \text{if} P_k \cdot f(d_{jk}) >= 1 \\
                S_j & \text{otherwise} \\
        \end{array}\right\{ \\
        \end{align*}


.. math::

        A_i = \sum_{j \in \left\{d_{ij} \leq d_0  \right\}} R_j \cdot f(d_{ij})


Where:

* :math:`i` is any pixel in the population raster
* :math:`A_i` is the greenspace per capita supplied to pixel i (square meters per person)
* :math:`R_j` is the greenspace/population ratio of greenspace pixel :math:`j`
* :math:`S_j` is the area of greenspace in pixel :math:`j`
* :math:`d_0` is the search radius
* :math:`k` is the population pixel within search radius of greenspace pixel :math:`j`
* :math:`d_jk` is the distance between greenspace pixel :math:`j` and population pixel :math:`k`.
* :math:`P_k` is the population of pixel :math:`k`.
* :math:`f(d)` is the selected decay function.
