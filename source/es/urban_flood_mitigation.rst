.. _ufrm:

*********************************************
Mitigación del riesgo de inundaciones urbanas
*********************************************

Introducción
============

Las amenazas de inundación tienen distintas fuentes, entre ellas las inundaciones fluviales (o ribereñas), las inundaciones costeras y las inundaciones por aguas pluviales (o urbanas), que constituyen el foco de este modelo de InVEST. La infraestructura natural puede desempeñar un papel en la mitigación de cada una de estas amenazas. En el caso de las inundaciones por aguas pluviales, la infraestructura natural actúa principalmente al reducir la generación de escorrentía, ralentizar los flujos superficiales y crear espacio para el agua (en llanuras de inundación o cuencas).

El modelo de InVEST utiliza un enfoque sencillo basado en el número de curva para calcular la reducción de la escorrentía de lluvia debido al uso/cobertura del suelo y a las características del suelo. La reducción de la escorrentía también puede entenderse como la cantidad de escorrentía retenida por píxel en comparación con el volumen de la tormenta. Para cada cuenca hidrográfica, el modelo también estima el daño económico potencial a la infraestructura construida y el servicio ecosistémico que esta recibe.

El modelo
=========

Cómo funciona
^^^^^^^^^^^^^

Producción de escorrentía e índice de atenuación de la escorrentía
------------------------------------------------------------------

Para cada píxel :math:`i`, definido por un tipo de uso del suelo y las características del suelo, estimamos la escorrentía :math:`Q` (mm) mediante el método del número de curva:

.. math:: Q_{p,i} = \begin{Bmatrix}
        \frac{(P - \lambda S_{max_i})^2}{P + (1-\lambda) S_{max,i}} & if & P > \lambda \cdot S_{max,i} \\
        0 & & otherwise
        \end{Bmatrix}
    :label: runoff

Donde :math:`P` es la profundidad de la tormenta de diseño en mm, :math:`S_{max,i}` es la retención potencial en mm y :math:`\lambda \cdot S_{max}` es la profundidad de lluvia necesaria para iniciar la escorrentía, también denominada abstracción inicial (:math:`\lambda=0.2` para simplificar).

:math:`S_{max}` (calculado en mm) es una función del número de curva, :math:`CN`, un parámetro empírico que depende del uso del suelo y de las características del suelo (NRCS 2004):

.. math:: S_{max,i}=\frac{25400}{CN_i}-254
    :label:

A continuación, el modelo calcula la fracción de retención de escorrentía por píxel :math:`R_i`:

.. math:: R_i=1-\frac{Q_{p,i}}{P}
    :label: runoff_retention

Y el volumen de escorrentía retenido por píxel :math:`R\_m3_i`:

.. math:: R\_m3_i=R_i\cdot P\cdot pixel.area\cdot 10^{-3}
    :label: runoff_retention_volume

Donde :math:`pixel.area` se expresa en :math:`m^2`.

También se calcula el volumen de escorrentía (denominado asimismo «volumen de inundación») por píxel :math:`Q\_m3_i`:

.. math:: Q\_m3_i=Q_{p,i}\cdot pixel.area\cdot 10^{-3}
   :label: flood_volume

Calcular el servicio potencial (opcional)
-----------------------------------------

El servicio ecosistémico de retención de inundaciones solo constituye realmente un servicio si alguien se beneficia de una reducción de las inundaciones. Dado que este modelo no cuantifica la extensión ni la profundidad de las inundaciones reales, no podemos determinar qué edificios se inundan ni en qué medida. Por ello, ofrecemos dos medidas que pueden utilizarse como indicadores para comprender: 1) qué cuencas hidrográficas tienen el potencial de presentar costos por daños más altos o más bajos; y 2) cuánto beneficio proporciona la retención de escorrentía en cada cuenca, en relación con los costos potenciales por daños.

En primer lugar, :math:`\text{Affected.build}`, la suma de los daños potenciales a la infraestructura construida, expresada en unidades monetarias, se calcula para cada cuenca hidrográfica o cuenca de drenaje :math:`W`:

.. math:: \text{Affected.build}_W = \sum_{b ∈ B}a(b,W)·d(b)
   :label: affected.build

Donde:

* :math:`b` es la huella de un edificio perteneciente al conjunto de toda la infraestructura construida :math:`B`.
* :math:`a(b,W)` es el área, en :math:`m^2`, de la huella del edificio :math:`b` que se superpone con la cuenca hidrográfica :math:`W`.
* :math:`d(b)` es el valor del daño en :math:`currency/m^2` (procedente de la tabla de pérdidas por daños proporcionada por el usuario) para el tipo de edificio :math:`b`.

Esta medida es simplemente la suma, dentro de cada cuenca, del área de los edificios multiplicada por el costo de los daños correspondiente a cada tipo de edificio. Las unidades corresponden a la moneda que se utilice para expresar los costos por daños.

En segundo lugar, calculamos :math:`\text{Service.built}`, un indicador de la retención de inundaciones por parte del paisaje que puede contribuir a evitar daños a la infraestructura construida. Para cada cuenca hidrográfica :math:`W`:

.. math:: \text{Service.built}_W=\text{Affected.build}_W·\sum_{i ∈ W}R\_m3_i
   :label: service.built

Donde:

* :math:`i` es un píxel de la cuenca hidrográfica :math:`W`.
* :math:`R\_m3_i` es el volumen de escorrentía retenido en el píxel :math:`i`.

:math:`\text{Service.built}` se expresa en :math:`currency·m^3`, una unidad que, por sí misma, carece de significado. Sin embargo, los valores relativos de :math:`\text{Service.built}` pueden utilizarse para indicar el servicio ecosistémico de retención de inundaciones que proporciona el paisaje en cada cuenca hidrográfica, en términos de retención del agua que, de otro modo, causaría daños a la infraestructura. Dada la simplicidad del modelo, debe considerarse únicamente como un indicador del servicio, no como una medida real de los daños o los ahorros.

Limitaciones y simplificaciones
===============================

**Producción de escorrentía:** el modelo utiliza un enfoque sencillo (número de curva del SCS), que introduce un alto grado de incertidumbre. Sin embargo, este enfoque suele representar adecuadamente la clasificación relativa entre distintos usos del suelo; es decir, el efecto de la infraestructura natural se reflejará cualitativamente en los resultados del modelo. En el futuro se buscará incorporar el enrutamiento del flujo a través del paisaje. Entre las opciones consideradas se encuentran TOPMODEL (existe un paquete de R), UFORE (utilizado en iTree), CADDIES, entre otras.

**Enfoques de valoración:** actualmente se implementa un enfoque sencillo para valorar la retención del riesgo de inundación, que considera el riesgo como el daño *potencial* que se evita en la infraestructura construida. Este valor puede ser útil para comparar el riesgo entre cuencas hidrográficas cercanas y representar las distintas cantidades de infraestructura expuesta en cada una. Sin embargo, dado que el modelo no produce mapas de inundación, no hay manera de confirmar que la infraestructura esté realmente expuesta. Por tanto, el resultado sigue representando un beneficio potencial. Podrían implementarse enfoques alternativos (por ejemplo, relacionados con la mortalidad, la morbilidad o la alteración de la actividad económica). Otra métrica del servicio es la población afectada, es decir, el número de personas en riesgo de sufrir inundaciones. Esta métrica podría centrarse únicamente en grupos vulnerables, por ejemplo, según la edad o el idioma. Véase Arkema et al. (2017) para una revisión de las métricas de vulnerabilidad social. Esta métrica puede calcularse sumando la población en la intersección entre la cuenca hidrográfica y el área propensa a inundaciones.

Datos necesarios
================

.. note:: Las capas espaciales del modelo de Mitigación de inundaciones urbanas pueden tener distintos sistemas de coordenadas, pero *todos deben ser sistemas de coordenadas proyectadas*, no geográficas.

.. note:: Los rásteres de entrada pueden tener distintos tamaños de celda; se remuestrearán para que coincidan con el tamaño de celda del ráster de uso/cobertura del suelo. Por tanto, los resultados ráster del modelo tendrán el mismo tamaño de celda que el ráster de uso/cobertura del suelo.

- :investspec:`urban_flood_risk_mitigation workspace_dir`

- :investspec:`urban_flood_risk_mitigation results_suffix`

- :investspec:`urban_flood_risk_mitigation aoi_watersheds_path` Pueden ser límites de cuencas hidrográficas o de cuencas de drenaje.

- :investspec:`urban_flood_risk_mitigation rainfall_depth` Corresponde a :math:`P` en la ecuación :eq:`runoff`.

- :investspec:`urban_flood_risk_mitigation lulc_path` Todos los resultados se generarán con la resolución de este ráster.

- :investspec:`urban_flood_risk_mitigation soils_hydrological_group_raster_path` Tenga en cuenta que no se aceptan valores distintos de 1, 2, 3 y 4 (como 13 y 14). Consulte el apéndice de Fuentes de datos de este capítulo para obtener más información.

- :investspec:`urban_flood_risk_mitigation curve_number_table_path` Tabla que contiene la información del modelo correspondiente a cada una de las clases de uso del suelo del mapa de cobertura del suelo. TODAS las clases de uso/cobertura del suelo del ráster de cobertura del suelo DEBEN tener valores correspondientes en esta tabla. Cada fila representa una clase de uso/cobertura del suelo y las columnas deben denominarse y definirse de la siguiente manera:

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
  - :investspec:`urban_flood_risk_mitigation infrastructure_damage_loss_table_path.columns.damage` Puede utilizarse cualquier moneda.

Interpretación de los resultados
================================

* **Registro de parámetros**: cada vez que se ejecuta el modelo, se crea un archivo de texto (.txt) en el Espacio de trabajo. El archivo enumera los valores de los parámetros y los mensajes de salida de esa ejecución, y su nombre se genera a partir del servicio, la fecha y la hora. Cuando se comunique con NatCap para informar de errores en una ejecución del modelo, incluya el registro de parámetros.

* **Runoff_retention_index.tif**: ráster con los valores del índice de retención de escorrentía (sin unidades; valores de 0 a 1, relativos al volumen de precipitación). Se calcula mediante la ecuación :eq:`runoff_retention`.

* **Runoff_retention_m3.tif**: ráster con los valores del volumen de escorrentía retenido (en :math:`m^3`). Se calcula mediante la ecuación :eq:`runoff_retention_volume`.

* **Q_mm.tif**: ráster con los valores de escorrentía (mm). Se calcula mediante la ecuación :eq:`runoff`.

* **flood_risk_service.shp**: shapefile con los resultados en la tabla de atributos:

  * **rnf_rt_idx**: promedio de los valores del índice de retención de escorrentía (:math:`R_i`) por cuenca hidrográfica.

  * **rnf_rt_m3**: suma de los volúmenes de escorrentía retenidos (:math:`R\_m3_i`), en :math:`m^3`, por cuenca hidrográfica.

  * **flood_vol**: volumen de inundación (``Q_m3``, ecuación :eq:`flood_volume`) por cuenca hidrográfica.

  * **aff_bld**: daño potencial a la infraestructura construida por cuenca hidrográfica, calculado como la suma del área de los edificios multiplicada por el costo de los daños, agrupada por cuenca. Las unidades corresponden a la moneda utilizada como dato de entrada para el costo de los daños. Solo se calcula cuando se proporciona el dato de entrada del vector de infraestructura construida. Tenga en cuenta que no considera la profundidad ni la extensión reales de la inundación, por lo que debe utilizarse únicamente como indicador.

  * **serv_blt**: valores de :math:`Service.built` para esta cuenca hidrográfica (consulte la ecuación :eq:`service.built` para obtener más información), en unidades de :math:`currency·m^3`. Es un indicador relativo del servicio ecosistémico de retención de escorrentía de la cuenca, que tiene el potencial de reducir las inundaciones que afectan a la infraestructura construida. Solo se calcula cuando se proporciona el dato de entrada del vector de infraestructura construida. Tenga en cuenta que no considera la profundidad ni la extensión reales de la inundación, por lo que debe utilizarse únicamente como indicador.

Apéndice: fuentes de datos y orientaciones para seleccionar parámetros
======================================================================

:ref:`Uso/cobertura del suelo <lulc>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Cuencas hidrográficas <watersheds>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Profundidad de lluvia para la tormenta de diseño
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una tormenta de diseño es una tormenta hipotética utilizada con fines de modelación. El valor de precipitación de la tormenta de diseño debe elegirse de acuerdo con el área y los objetivos del estudio. Por ejemplo, puede corresponder a la precipitación media por evento de lluvia, a la precipitación de un percentil determinado o a la precipitación máxima que se espera que ocurra una vez cada 100 años.

Para calcular la tormenta de diseño, los usuarios pueden consultar las tablas de intensidad-frecuencia-duración (IFD) disponibles para su ciudad. La duración de la tormenta equivale al tiempo de concentración promedio de las cuencas hidrográficas estudiadas. El tiempo de concentración puede obtenerse de estudios existentes o mediante herramientas web; por ejemplo: https://www.lmnoeng.com/Hydrology/TimeConc.php. Véase Balbi et al. (2017) para una descripción detallada de estos métodos.

:ref:`Grupos de suelos <soil_groups>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Número de curva <cn>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Infraestructura construida <buildings>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pérdida potencial por daños para cada tipo de edificio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En Estados Unidos, HAZUS proporciona datos sobre daños. A escala mundial, un informe reciente de la Comisión Europea ofrece datos útiles: https://publications.jrc.ec.europa.eu/repository/bitstream/JRC105688/global_flood_depth-damage_functions__10042017.pdf

Referencias
===========

Arkema, K. K., Griffin, R., Maldonado, S., Silver, J., Suckale, J., y Guerry, A. D. (2017). «Linking social, ecological, and physical science to advance natural and nature-based protection for coastal communities». https://doi.org/10.1111/nyas.13322

Balbi, M., Lallemant, D., y Hamel, P. (2017). «A flood risk framework for ecosystem services valuation: a proof-of-concept».

NRCS-USDA. (2004). Capítulo 10. Estimación de la escorrentía directa a partir de la lluvia de una tormenta. En Departamento de Agricultura de Estados Unidos (ed.), *Parte 630: Hidrología. Manual de Ingeniería Nacional*. Recuperado de http://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063

NRCS-USDA. Parte 630: Hidrología. *Manual de Ingeniería Nacional*, capítulo 7: Grupos hidrológicos de suelos. 2007.

NRCS-USDA. Parte 630: Hidrología. *Manual de Ingeniería Nacional*, capítulo 9: Complejos hidrológicos de suelo y cobertura. 2004.

Sahl, J. (2015). «Economic Valuation Approaches for Ecosystem Services: a literature review to support the development of a modeling framework for valuing urban stormwater management services».
