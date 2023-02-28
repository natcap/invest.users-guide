.. _ufrm:

****************************************************
Modelo de mitigación del riesgo de inundación urbana
****************************************************

Introducción
============

Los riesgos de inundación provienen de diferentes fuentes, entre ellas: las inundaciones fluviales, las inundaciones costeras y las inundaciones por aguas pluviales (o urbanas), en las que se centra este modelo InVEST. Las infraestructuras naturales pueden desempeñar un papel en cada uno de estos riesgos de inundación. En relación con las inundaciones por aguas pluviales, las infraestructuras naturales actúan principalmente reduciendo la producción de escorrentía, frenando los flujos superficiales y creando espacio para el agua (en llanuras de inundación o cuencas).

El modelo InVEST calcula la reducción de la escorrentía, es decir, la cantidad de escorrentía retenida por píxel en comparación con el volumen de la tormenta. Para cada cuenca hidrográfica, también calcula los posibles daños económicos superponiendo la información sobre el potencial de extensión de las inundaciones y las infraestructuras construidas.

El modelo
=========

Cómo funciona
^^^^^^^^^^^^^

Producción de escorrentía e índice de atenuación de la escorrentía
------------------------------------------------------------------

Para cada píxel :math:`i`, definido por un tipo de uso del suelo y sus características, estimamos la escorrentía :math:`Q` (mm) con el método del Número de Curva:

.. math:: Q_{p,i} = \begin{Bmatrix}
        \frac{(P - \lambda S_{max_i})^2}{P + (1-\lambda) S_{max,i}} & if & P > \lambda \cdot S_{max,i} \\
        0 & & otherwise
        \end{Bmatrix}
    :label: runoff

Donde :math:`P` es la profundidad de la tormenta de diseño en mm, :math:`S_{max,i}` es la retención potencial en mm, y :math:`lambda \cdot S_{max}` es la profundidad de la lluvia necesaria para iniciar la escorrentía, también llamada la abstracción inicial (:math:`\lambda=0,2` para simplificar).

:math:`S_{max}` (calculado en mm) es una función del número de curva, :math:`CN`, un parámetro empírico que depende del uso de la tierra y de las características del suelo (NRCS 2004):

.. math:: S_{max,i}=\frac{25400}{CN_i}-254
    :label:

A continuación, el modelo calcula la retención de la escorrentía por píxel :math:`R_i` como:

.. math:: R_i=1-\frac{Q_{p,i}}{P}
    :label: runoff_retention

Y el volumen de retención de la escorrentía por píxel :math:`R\_m3_i` como:

.. math:: R\_m3_i=R_i\cdot P\cdot pixel.area\cdot 10^{-3}
    :label: runoff_retention_volume

Con :math:`pixel.area` en :math:`m^2`.

El volumen de escorrentía (también denominado "volumen de inundación") por píxel :math:`Q\_m3_i` también se calcula como:

.. math:: Q\_m3_i=Q_{p,i}\cdot pixel.area\cdot 10^{-3}
   :label: flood_volume

Calculo del servicio potencial (opcional)
------------------------------------------

En primer lugar, se calcula para cada cuenca hidrográfica o de alcantarillado :math:`\text{Affected.build}`, la suma de los daños potenciales en $ de las infraestructuras construidas :math:`W`:

.. math:: \text{Affected.build}_W = \sum_{b ∈ B}a(b,W)·d(b)
   :label: affected.build

donde

* :math:`b` es una huella de construcción en el conjunto de todas las infraestructuras construidas :math:`B`
* :math:`a(b,W)` es el área en :math:`m^2` de la huella de construcción :math:`b` que cruza la cuenca :math:`W`
* :math:`d(b)` es el valor de los daños en :math:`moneda/m^2` (de la tabla de pérdidas por daños) para el tipo de construcción :math:`b`'sath:`currency/m^2` (from the Damage Loss Table) for building :math:`b`'s type

A continuación, calculamos :math:`\text{Service.built`, un indicador de los daños evitados en las infraestructuras construidas, para cada cuenca hidrográfica :math:`W`:

.. math:: \text{Service.built}_W=\text{Affected.build}_W·\sum_{i ∈ W}R\_m3_i
   :label: service.built

donde

* :math:`i` es un píxel en la cuenca :math:`W`
* :math:`R\_m3_i` es el volumen de retención de escorrentía en el píxel :math:`i`

:math:`\text{Service.built}` se expresa en :math:`currency-m^3`. Debe considerarse solo un indicador, no una medida real de ahorro.

Limitaciones y simplificaciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Producción de escorrentía:** el modelo utiliza un enfoque simple (SCS-Curve Number), que introduce elevadas incertidumbres. Sin embargo, la clasificación entre los distintos usos del suelo suele quedar bien plasmada con este enfoque, es decir, que el efecto de las infraestructuras naturales quedará cualitativamente representado en los resultados del modelo. Los trabajos futuros tendrán como objetivo incluir un trazado sobre el paisaje: las ideas incluyen TOPMODEL (existe un paquete R), UFORE (utilizado en iTree), CADDIES, etc.

**Enfoques de valoración:** En la actualidad, se aplica un enfoque simple para valorar la retención del riesgo de inundación, valorando el riesgo de inundación como el daño evitado para la infraestructura construida. Podrían aplicarse enfoques alternativos (por ejemplo, relacionados con la mortalidad, la morbilidad o los trastornos económicos). Otra métrica de servicio es la población afectada, es decir, el número de personas en riesgo de inundación. Esto podría centrarse solo en los grupos vulnerables, por ejemplo, relacionados con la edad, el idioma, etc. Arkema et al. (2017) presentan una revisión de las métricas de vulnerabilidad social. Estas pueden calcularse sumando la población en la intersección de la cuenca y la zona propensa a las inundaciones.

Necesidades de datos
====================

.. note:: Las capas espaciales para la Mitigación de Inundaciones Urbanas pueden tener diferentes sistemas de coordenadas, pero *todos deben ser sistemas de coordenadas proyectadas*, no geográficas.

.. note:: Los inputs de ráster pueden tener diferentes tamaños de celda, y se remuestrearán para que coincidan con el tamaño de celda del ráster de uso/cobertura del suelo. Por lo tanto, los resultados del modelo ráster tendrán el mismo tamaño de celda que el ráster de uso/cobertura del suelo.

- :investspec:`urban_flood_risk_mitigation workspace_dir`

- :investspec:`urban_flood_risk_mitigation results_suffix`

- :investspec:`urban_flood_risk_mitigation aoi_watersheds_path` Pueden ser límites de cuencas hidrográficas o de alcantarillado.

- :investspec:`urban_flood_risk_mitigation rainfall_depth` Esto es :math:`P` en la ecuación :eq:`runoff`.

- :investspec:`urban_flood_risk_mitigation lulc_path` Todos los resultados se producirán con la resolución de este ráster.

- :investspec:`urban_flood_risk_mitigation soils_hydrological_group_raster_path`

- :investspec:`urban_flood_risk_mitigation curve_number_table_path` tabla que contiene la información del modelo correspondiente a cada una de las clases de uso del suelo en el mapa de cobertura del suelo. Todas las clases de LULC en el ráster de cobertura del suelo TIENEN QUE tener los valores correspondientes en esta tabla. Cada fila es una clase de uso del suelo/cobertura del suelo y las columnas deben ser nombradas y definidas como sigue:

  Columnas:

  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.lucode`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_a`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_b`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_c`
  - :investspec:`urban_flood_risk_mitigation curve_number_table_path.columns.cn_d`

- :investspec:`urban_flood_risk_mitigation built_infrastructure_vector_path`

  Campo:

  - :investspec:`urban_flood_risk_mitigation built_infrastructure_vector_path.fields.type`

- :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path`

  Columnas:

  - :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path.columns.type`
  - :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path.columns.damage` Se puede usar cualquier moneda.

Interpretación de los resultados
================================

 * **Registro de parámetros**: Cada vez que se ejecute el modelo, se creará un archivo de texto (.txt) en el Espacio de Trabajo. El archivo enumerará los valores de los parámetros y los mensajes de salida para esa ejecución y se nombrará según el servicio, la fecha y la hora. Cuando se ponga en contacto con NatCap sobre los errores de una ejecución del modelo, incluya el registro de parámetros.

 * **Runoff_retention.tif**: ráster con los valores de retención de la escorrentía (sin unidad, relativo al volumen de precipitación).  Calculado a partir de la ecuación :eq:`runoff_retention`.

 * Runoff_retention_m3.tif**: ráster con valores de retención de escorrentía (en :math:`m^3`). Calculado a partir de la ecuación :eq:`runoff_retention_volume`.

 **Q_mm.tif**: ráster con valores de escorrentía (mm). Calculado a partir de la ecuación :eq:`runoff`.

 **flood_risk_service.shp**: Shapefile con resultados en la tabla de atributos:

    * **rnf_rt_idx**: media de los valores de retención de la escorrentía (:math:`R_i`) por cuenca hidrográfica

    * **rnf_rt_m3**: suma de los volúmenes de retención de escorrentía (:math:`R\_m3_i`), en :math:`m^3`, por cuenca hidrográfica

    * **flood_vol**: El volumen de inundación (``Q_m3``, equation :eq:`flood_volume`) por cuenca hidrográfica.

    **aff_bld**: daños potenciales a las infraestructuras construidas en unidades monetarias, por cuenca hidrográfica.  Solo se calcula cuando se proporciona el vector de infraestructuras construidas.

    * **serv_blt**: valores de :math:`Service.built` para esta cuenca (véase la ecuación :eq:`service.built`). Indicador del servicio de retención de la escorrentía para la cuenca. Solo se calcula cuando se proporciona el input Vector de infraestructura construida.

Apéndice: Fuentes de datos y orientación para la selección de parámetros
========================================================================

:ref:`LULC <lulc>`
^^^^^^^^^^^^^^^^^^

:ref:`Watersheds <watersheds>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Profundidad de la precipitación para la tormenta de diseño
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una tormenta de diseño es un temporal de lluvia hipotético que se utiliza con fines de modelización. El valor de la precipitación de la tormenta de diseño debe elegirse en función de la zona y los objetivos. Por ejemplo, podría ser la precipitación media por evento de lluvia, la precipitación en un determinado percentil o la precipitación máxima que se espera que ocurra una vez cada 100 años.

Para calcular la tormenta de diseño se pueden consultar las tablas de intensidad-frecuencia-duración (IFD) disponibles para su ciudad. La duración de la tormenta es igual al tiempo medio de concentración de las cuencas estudiadas. El tiempo de concentración puede derivarse de estudios existentes o de herramientas web: por ejemplo, https://www.lmnoeng.com/Hydrology/TimeConc.php. Véase Balbi et al. (2017) para una descripción detallada de estos métodos.

:ref:`Soil Groups <soil_groups>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Curve Number <cn>`
^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Built Infrastructure <buildings>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pérdida potencial de daños para cada tipo de construcción
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En Estados Unidos, HAZUS proporciona datos sobre los daños. A nivel mundial, un reciente informe de la Comisión Europea ofrece datos útiles: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC105688/global_flood_depth-damage_functions__10042017.pdf

Referencias
===========

Arkema, K. K., Griffin, R., Maldonado, S., Silver, J., Suckale, J. y Guerry, A. D. (2017). Linking social , ecological , and physical science to advance natural and nature-based protection for coastal communities. https://doi.org/10.1111/nyas.13322

Balbi, M., Lallemant, D. y Hamel, P. (2017). A flood risk framework for ecosystem services valuation: a proof-of-concept.

NRCS-USDA. (2004). Chapter 10. Estimation of Direct Runoff from Storm Rainfall. In United States Department of Agriculture (Ed.), Part 630 Hydrology. National Engineering Handbook. Retrieved from http://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063

NRCS-USDA Part 630 Hydrology National Engineering Handbook, Chapter 7 Hydrologic Soil Groups. 2007.

NRCS-USDA Part 630 Hydrology National Engineering Handbook, Chapter 9 Hydrologic Soil-Cover Complexes. 2004.

Sahl, J. (2015). Economic Valuation Approaches for Ecosystem Services: a literature review to support the development of a modeling framework for valuing urban stormwater management services.
