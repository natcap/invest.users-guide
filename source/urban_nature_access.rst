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

..math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                1 & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Exponential
***********

..math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                e^(-d_{ij}/d_0) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Power
*****

..math ::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                d_{ij}^(-\beta) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

Gaussian
********

..math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                \frac{e^{-\frac{1}{2}\left ( \frac{d_{ij}}{d_0} \right )^2}-e^{-\frac{1}{2}}}{1-e^{-\frac{1}{2}}} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}

- [ ] TODO: compare this to our existing gaussian kernel

Kernel Density
**************

..math ::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr} \\
                \frac{3}{4}\left(1-\left(\frac{d_{ij}}{d_{0}}\right)^{2}\right) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\{ \\
        \end{align*}


