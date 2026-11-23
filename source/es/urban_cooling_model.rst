.. _ucm:

*******************
Enfriamiento urbano
*******************

Resumen
=======

La mitigación del calor urbano es una prioridad para muchas ciudades que han experimentado olas de calor en los últimos años. La vegetación puede ayudar a reducir el efecto de isla de calor urbana (ICU) al proporcionar sombra, modificar las propiedades térmicas del tejido urbano y aumentar el enfriamiento mediante la evapotranspiración. Esto tiene consecuencias para la salud y el bienestar de la población, pues reduce la mortalidad y la morbilidad, aumenta el confort y la productividad y disminuye la necesidad de utilizar aire acondicionado (A/C). El modelo de Enfriamiento Urbano de InVEST calcula un índice de mitigación del calor basado en la sombra, la evapotranspiración y el albedo, así como en la distancia respecto de las islas de enfriamiento (por ejemplo, los parques). Este índice se utiliza para estimar la reducción de temperatura atribuible a la vegetación. Por último, el modelo estima el valor del servicio de mitigación del calor mediante dos métodos de valoración opcionales: el consumo de energía y la productividad laboral.

Introducción
============

Las islas de calor urbanas afectan a muchas ciudades del mundo y tienen consecuencias importantes para la salud y el bienestar de las personas: elevada mortalidad o morbilidad durante las olas de calor, alto consumo de A/C y reducción del confort o de la productividad laboral. El efecto de isla de calor urbana, es decir, la diferencia entre las temperaturas rurales y urbanas, es resultado de las características particulares de las ciudades y se debe principalmente a dos factores: las propiedades térmicas de los materiales utilizados en las áreas urbanas (por ejemplo, concreto y asfalto), que almacenan más calor, y la reducción del efecto de enfriamiento de la vegetación (mediante la sombra y la evapotranspiración).

Por tanto, la infraestructura natural desempeña un papel en la reducción de las islas de calor urbanas. A partir de la literatura, en rápido crecimiento, sobre la modelización del calor urbano (Deilami et al. 2018), el modelo de Enfriamiento Urbano de InVEST estima el efecto de enfriamiento de la vegetación utilizando datos de disponibilidad habitual sobre clima, uso y cobertura del suelo (LULC) y, opcionalmente, uso de aire acondicionado.

El modelo
=========

Cómo funciona
-------------

Índice de capacidad de enfriamiento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En primer lugar, el modelo calcula el índice de capacidad de enfriamiento (CC) de cada píxel a partir de la sombra local, la evapotranspiración y el albedo. Este enfoque se basa en los índices propuestos por Zardo et al. (2017) y Kunapo et al. (2018), a los que se añade el albedo, un factor importante para la reducción del calor.

El factor de sombra (`shade`) representa la proporción de cobertura de copa de los árboles (≥2 m de altura) asociada con cada categoría de uso y cobertura del suelo (LULC). Su valor se encuentra entre 0 y 1.

El índice de evapotranspiración (ETI) representa un valor normalizado de la evapotranspiración potencial, es decir, la evapotranspiración de la vegetación (o la evaporación del suelo en las áreas sin vegetación). Se calcula para cada píxel multiplicando la evapotranspiración de referencia (:math:`ETo`, proporcionada por el usuario) por el coeficiente de cultivo (:math:`Kc`, asociado al tipo de LULC del píxel) y dividiendo el resultado por el valor máximo del ráster de :math:`ETo` en el área de interés, :math:`ETmax`:

.. math:: ETI = \frac{K_c \cdot ETo}{ET_{max}}
    :label: eti

Tenga en cuenta que esta ecuación supone que las áreas con vegetación reciben suficiente riego (aunque los valores de Kc pueden reducirse para representar una evapotranspiración limitada por la disponibilidad de agua).

El factor de albedo es un valor entre 0 y 1 que representa la proporción de radiación solar reflejada por el tipo de LULC (Phelan et al. 2015).

El modelo combina los tres factores en el índice CC:

.. math:: CC_i = 0.6 \cdot shade + 0.2\cdot albedo + 0.2\cdot ETI
    :label: coolingcapacity_factors

La ponderación recomendada (0,6; 0,2; 0,2) se basa en datos empíricos y refleja el mayor impacto de la sombra en comparación con la evapotranspiración. Por ejemplo, Zardo et al. (2017) señalan que «en áreas menores de dos hectáreas [la evapotranspiración] recibió una ponderación de 0,2 y la sombra de 0,8. En áreas mayores de dos hectáreas, las ponderaciones cambiaron a 0,6 y 0,4 para [la evapotranspiración] y la sombra, respectivamente». En el presente modelo proponemos desagregar los efectos de la sombra y el albedo en la ecuación (83), y asignar al albedo una ponderación igual a la del ETI, con base en los resultados de Phelan et al. (2015) (véase la Tabla 2 de su estudio, que muestra que la vegetación y el albedo tienen coeficientes similares).

Nota: el usuario puede introducir manualmente ponderaciones alternativas para probar la sensibilidad de los resultados del modelo a este parámetro (o cuando se disponga de conocimiento local).

Opcionalmente, el modelo puede considerar otro factor, la intensidad de la edificación (:math:`building.intensity` para una clasificación determinada de cobertura del suelo), que representa la dimensión vertical de la infraestructura construida. La intensidad de la edificación es un predictor importante de la temperatura nocturna, ya que el calor almacenado por los edificios durante el día se libera durante la noche. Para predecir las temperaturas nocturnas, los usuarios deben proporcionar el factor de intensidad de la edificación para cada clase de uso del suelo en la Tabla biofísica; el modelo modificará entonces la ecuación :math:numref:`coolingcapacity_factors` de la siguiente manera:

.. math:: CC_i = 1 - building.intensity
    :label: coolingcapacity_intensity


Índice de mitigación del calor urbano (efecto de los grandes espacios verdes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para tener en cuenta el efecto de enfriamiento de los grandes espacios verdes (>2 ha) sobre las áreas circundantes (véase el análisis de Zardo et al. 2017 y McDonald et al. 2016), el modelo calcula el índice de mitigación del calor urbano (HM). El valor de HM es igual a CC si el píxel no se ve afectado por ningún espacio verde grande; de lo contrario, se establece como un promedio ponderado por la distancia de los valores de CC de los grandes espacios verdes y del píxel de interés.

.. note::
   El modelo no comprueba si los espacios verdes son contiguos. Por tanto,
   varios espacios verdes pequeños dentro de la distancia de búsqueda tendrán
   el mismo efecto sobre la mitigación del calor urbano que un único espacio
   verde grande de la misma superficie dentro de esa distancia.

Para ello, el modelo calcula primero la superficie de espacios verdes dentro de una distancia de búsqueda :math:`d_{cool}` alrededor de cada píxel (:math:`GA_i`) y la capacidad de enfriamiento aportada por cada parque (:math:`CC_{park_i}`):

.. math:: {GA}_{i}=cell_{area}\cdot\sum_{j\in\ d\ radius\ from\ i} g_{j}
    :label: [3a]

.. math:: CC_{park_i}=\sum_{j\in\ d\ radius\ from\ i} g_j \cdot CC_j \cdot e^{\left( \frac{-d(i,j)}{d_{cool}} \right)}
    :label: [3b]

donde :math:`cell_{area}` es la superficie de una celda en hectáreas, :math:`g_j` vale 1 si el píxel :math:`j` corresponde a un espacio verde y 0 si no corresponde a uno, :math:`d(i,j)` es la distancia entre los píxeles :math:`i` y :math:`j`, :math:`d_{cool}` es la distancia a la que un espacio verde ejerce un efecto de enfriamiento, y :math:`CC_{park_i}` es el promedio ponderado por la distancia de los valores de CC atribuibles a los espacios verdes. (Tenga en cuenta que las clases LULC que califican como «espacios verdes» las determina el usuario mediante el parámetro `green_area` de la Tabla biofísica; véase la tabla de entradas en la sección 3). A continuación, el índice HM se calcula así:

.. math:: HM_i = \begin{Bmatrix}
        CC_i & if & CC_i \geq CC_{park_i}\ or\ GA_i < 2 ha \\
        CC_{park_i} & & otherwise
        \end{Bmatrix}
    :label: [4]

Estimaciones de la temperatura del aire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para estimar la reducción del calor en toda la ciudad, el modelo utiliza la magnitud de la ICU a escala de ciudad, :math:`UHI_{max}`. Los usuarios pueden obtener valores de ICU de la literatura local o de estudios mundiales. Por ejemplo, el Explorador Mundial de ICU de Superficie, desarrollado por la Universidad de Yale, proporciona estimaciones anuales, estacionales, diurnas y nocturnas de la ICU (https://yceo.users.earthengine.app/view/uhimap).

Tenga en cuenta que la magnitud de la ICU se define para un período específico (por ejemplo, el clima actual o futuro) y un momento determinado (por ejemplo, temperaturas nocturnas o diurnas). La selección del período y del momento afectará la cuantificación y la valoración del servicio.

La temperatura del aire sin mezcla de aire, :math:`T_{air_{nomix}}`, se calcula para cada píxel de la siguiente manera:

.. math:: T_{air_{nomix},i}=T_{air,ref} + (1-HM_i)\cdot UHI_{max}
    :label: [5]

Donde :math:`T_{air,ref}` es la temperatura del aire de referencia rural y :math:`UHI_{max}` es la magnitud máxima del efecto de ICU en la ciudad (o, más precisamente, la diferencia entre :math:`T_{air,ref}` y la temperatura máxima observada en la ciudad).

Debido a la mezcla del aire, estas temperaturas se promedian espacialmente. La temperatura real del aire (con mezcla), :math:`T_{air}`, se obtiene a partir de :math:`T_{air_{nomix}}` mediante una función gaussiana con un radio de kernel :math:`r`, definido por el usuario.

Para cada área de interés (que corresponde a una capa SIG vectorial proporcionada por el usuario), calculamos la temperatura media y la anomalía de temperatura :math:`(T_{air,i} - T_{air,ref})`.

Valor del servicio de reducción del calor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El valor de la reducción de temperatura puede evaluarse al menos de tres maneras:

    i) ahorro de energía por la reducción del consumo de electricidad del A/C;
    ii) aumento de la productividad laboral de los trabajadores al aire libre;
    iii) disminución de la morbilidad y mortalidad relacionadas con el calor.

El modelo proporciona estimaciones de (i) ahorro de energía y (ii) productividad laboral, basadas en análisis de regresión mundiales o en datos locales.

**Ahorro de energía:** el modelo utiliza una relación entre el consumo de energía y la temperatura (por ejemplo, resumida por Santamouris et al. 2015) para calcular el ahorro energético y los costos asociados para un edificio :math:`b`:

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}})
    :label: energy_savings_kwh

Donde:

    * :math:`consumption.increase(b)` (kWh/° C/:math:`m^2`) es la estimación local del aumento del consumo de energía por cada grado de temperatura y por metro cuadrado de huella del edificio, para la categoría de edificios :math:`b`.
    * :math:`T_{air,MAX}` (° C) es la temperatura máxima del paisaje (:math:`T_{air,ref} + UHI_{max}`);
    * :math:`\overline{T_{air,MAX} - T_{air,i}}` (° C) es la diferencia media de temperatura del aire para el edificio :math:`b`, donde :math:`T_{air,i}` se modeló en los pasos anteriores.

Si se proporcionan costos para cada categoría de edificios, la ecuación :math:numref:`energy_savings_kwh` se sustituye por la ecuación :math:numref:`energy_savings_dollars`:

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}}) \cdot cost(b)
    :label: energy_savings_dollars

Donde:

    * :math:`cost(b)` es la estimación del costo de la energía por kWh para la categoría de edificios :math:`b`. Tenga en cuenta que es muy probable que este valor sea igual para todos los edificios.

Para calcular el ahorro total de energía, sumamos los valores a escala de píxel dentro del área de interés.

**Productividad laboral:** el modelo convierte la temperatura del aire en temperatura de globo y bulbo húmedo (WBGT, por sus siglas en inglés) para calcular los efectos del calor sobre la productividad laboral. La WBGT tiene en cuenta la humedad y puede estimarse a partir de datos meteorológicos estándar de la siguiente manera (American College of Sports Medicine, 1984, Apéndice I):

.. math:: WBGT_i = 0.567 \cdot T_{air,i} + 0.393 \cdot e_i + 3.94
    :label: [7]

Donde:

    * :math:`T_{air}` = temperatura proporcionada por el modelo (temperatura de bulbo seco (° C))
    * :math:`e_i` = presión de vapor de agua (hPa)

La presión de vapor se calcula a partir de la temperatura y la humedad relativa mediante la ecuación:

.. math:: e_i = \frac{RH}{100} \cdot 6.105 \cdot e^{\left ( 17.27 \cdot \frac{T_{air,i}}{(237.7 + T_{air,i})} \right )}
    :label: [8]

Donde:

    * :math:`RH` = humedad relativa media (%) proporcionada por el usuario.

Para cada píxel, el modelo calcula la pérdida estimada de productividad (%) para dos intensidades de trabajo: «trabajo ligero» y «trabajo pesado» (según el tiempo de descanso necesario para distintas intensidades de trabajo, de acuerdo con la Tabla 2 de Kjellstrom et al. 2009):

.. math:: Loss.light.work_i = \begin{Bmatrix}
        0 & if & WBGT < 31.5\\
        25 & if & 31.5 \leq WBGT < 32.0 \\
        50 & if & 32.0 \leq WBGT < 32.5 \\
        75 & if & 32.5 \leq WBGT \\
        \end{Bmatrix}
    :label: [9a]

.. math:: Loss.heavy.work_i = \begin{Bmatrix}
        0 & if & WBGT < 27.5\\
        25 & if & 27.5 \leq WBGT < 29.5 \\
        50 & if & 29.5 \leq WBGT < 31.5 \\
        75 & if & 31.5 \leq WBGT \\
        \end{Bmatrix}
    :label: [9b]

Aquí, «trabajo ligero» corresponde aproximadamente a una tasa metabólica de 200 vatios, es decir, trabajo de oficina y actividades del sector servicios; «trabajo pesado» corresponde a 400 W, por ejemplo, trabajos de construcción o agrícolas.

Si no se dispone de datos específicos de la ciudad sobre la distribución de los sectores laborales, el usuario puede estimar la población trabajadora de la ciudad en tres sectores (servicios, industria y agricultura) utilizando datos nacionales del Banco Mundial (por ejemplo, «empleo en la industria, hombres (%)» y otros indicadores similares). La pérdida de tiempo de trabajo para una temperatura determinada puede calcularse utilizando los tiempos de descanso de la Tabla 2 (Kjellstrom et al. 2009) y la proporción de la población trabajadora en los distintos sectores. Si se dispone de datos locales sobre los salarios medios por hora de los diferentes sectores, estas pérdidas de tiempo de trabajo pueden traducirse en pérdidas monetarias.

Por último, para el «trabajo ligero», tenga en cuenta que la prevalencia del A/C puede desempeñar un papel. Si la mayoría de los edificios de oficinas cuentan con A/C, el usuario podría reducir la pérdida de tiempo de trabajo del sector servicios en la misma proporción que la prevalencia del A/C.

Limitaciones y simplificaciones
===============================

Debido a las simplificaciones descritas anteriormente, el modelo presenta varias limitaciones, que se resumen a continuación.

**Índice CC:** el índice CC se basa en ponderaciones empíricas derivadas de un número limitado de estudios de caso, que modulan el efecto de los factores clave que contribuyen al enfriamiento (ecuación (83)). Este paso de ponderación implica un alto grado de incertidumbre, como se analiza en Zardo et al. (2017). Para caracterizar y reducir esta incertidumbre, los usuarios pueden probar la sensibilidad del modelo a estos parámetros o realizar estudios experimentales que permitan comprender mejor los efectos relativos de la sombra, el albedo y la evapotranspiración.

**Efecto de los grandes parques y mezcla del aire:** dos parámetros representan el efecto de los grandes espacios verdes y de la mezcla del aire (:math:`d_{cool}` y :math:`r`). Es difícil derivar sus valores de la literatura, ya que varían según las propiedades de la vegetación, el clima (efecto de los grandes espacios verdes) y los patrones de viento (mezcla del aire). Al igual que con CC, los usuarios pueden caracterizar y reducir estas incertidumbres probando la sensibilidad del modelo a estos parámetros y comparando los patrones espaciales de temperatura estimados por el modelo con datos observados o modelados (véanse Bartesaghi et al. 2018 y Deilami et al. 2018 para obtener más información sobre este tipo de comparaciones).

**Opciones de valoración:** las opciones de valoración que admite actualmente el modelo se relacionan con el consumo energético del A/C y la productividad laboral al aire libre. Para el consumo de energía del A/C, los usuarios deben evaluar la prevalencia del A/C y ajustar las estimaciones en consecuencia (es decir, reducir el consumo de energía proporcionalmente al uso real del A/C).

La valoración de los efectos del calor urbano sobre la salud no está incluida actualmente en el modelo, a pesar de su importancia (McDonald et al. 2016). Esto se debe a que dichos efectos varían considerablemente entre ciudades y resulta difícil extrapolar los conocimientos actuales, basados predominantemente en el Norte Global (Campbell et al. 2018). Entre las opciones posibles para obtener estimaciones de los impactos sobre la salud se incluyen:

* utilizar los datos mundiales de McMichael et al. (2003), quienes emplean una relación lineal por encima de un umbral de temperatura para estimar la fracción anual de muertes atribuibles a los días calurosos; o
* para aplicaciones en Estados Unidos, utilizar la metodología desarrollada a partir de relaciones a escala nacional entre la mortalidad y los cambios de temperatura; véase McDonald et al. (2016).

Gasparrini et al. (2014) desglosan el aumento de la mortalidad atribuible al calor para 384 ciudades de 13 países. La salida :math:`T_air` del modelo InVEST puede utilizarse para determinar la fracción de mortalidad atribuible al calor (primero se determina en qué percentil se encuentra :math:`T_{air,i}` y luego se utiliza la Tabla S3 o la Tabla S4 del apéndice).

Datos necesarios
================

- :investspec:`urban_cooling_model workspace_dir`

- :investspec:`urban_cooling_model results_suffix`

- :investspec:`urban_cooling_model lulc_raster_path` El modelo utilizará la resolución y la proyección de esta capa para remuestrear y reproyectar todas las salidas. La resolución debe ser suficientemente pequeña para captar el efecto de los espacios verdes en el paisaje, aunque las categorías LULC pueden comprender una mezcla de coberturas vegetadas y no vegetadas (por ejemplo, «residencial», que puede tener un 30 % de cobertura de copa).

- :investspec:`urban_cooling_model biophysical_table_path`

  Columnas:

  - :investspec:`urban_cooling_model biophysical_table_path.columns.lucode`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.kc`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.green_area` Las áreas verdes de más de 2 hectáreas tienen un efecto de enfriamiento adicional.
  - :investspec:`urban_cooling_model biophysical_table_path.columns.shade`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.albedo`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.building_intensity`

- :investspec:`urban_cooling_model ref_eto_raster_path` Estos valores pueden corresponder a una fecha específica o pueden utilizarse valores mensuales como aproximación.

- :investspec:`urban_cooling_model aoi_vector_path` Las áreas de interés (AOI) suelen corresponder a límites de ciudades o barrios.

- :investspec:`urban_cooling_model green_area_cooling_distance` Corresponde a :math:`d_{cool}` en la ecuación :eq:`[3b]`. Valor recomendado: 450 m.

- :investspec:`urban_cooling_model t_ref` Corresponde a :math:`T_{air,ref}` en la ecuación :eq:`[5]`. Puede tratarse de la temperatura nocturna o diurna, para una fecha específica o un promedio de varios días. Los resultados corresponderán al mismo período de interés.

- :investspec:`urban_cooling_model uhi_max` Corresponde a :math:`UHI_{max}` en la ecuación :eq:`[5]`.

- :investspec:`urban_cooling_model t_air_average_radius` Intervalo de valores recomendado para la ejecución inicial: de 500 m a 600 m; véanse Schatz et al. (2014) y Lonsdorf et al. (2021).

- :investspec:`urban_cooling_model cc_method`

- :investspec:`urban_cooling_model building_vector_path`

  Campo:

  - :investspec:`urban_cooling_model building_vector_path.fields.type`

- :investspec:`urban_cooling_model do_energy_valuation`
- :investspec:`urban_cooling_model do_productivity_valuation`

- :investspec:`urban_cooling_model energy_consumption_table_path`

  Columnas:

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.type`
  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.consumption`

    .. note::
       El valor de **consumption** corresponde a la unidad de superficie de la *huella* del edificio, no a la superficie de los pisos. Este valor debe ajustarse según el número promedio de pisos de las estructuras de este tipo.

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.cost` Es muy probable que los valores de esta columna sean iguales para todos los tipos de edificios.

- :investspec:`urban_cooling_model avg_rel_humidity`

- :investspec:`urban_cooling_model cc_weight_shade`
- :investspec:`urban_cooling_model cc_weight_albedo`
- :investspec:`urban_cooling_model cc_weight_eti`

Interpretación de los resultados
================================

* **InVEST-urban_cooling_model-log-....txt**: archivo de registro (*log*) que se genera durante cada ejecución de InVEST. Detalla los parámetros de entrada utilizados y registra todos los errores que puedan haberse producido. Si publica una consulta sobre la ejecución de un modelo en community.naturalcapitalalliance.org, asegúrese de adjuntar este archivo de registro a su publicación.

* **urban_cooling_model_report_[Suffix].html:** resumen de la ejecución del modelo, que incluye visualizaciones de los principales resultados, tablas de resultados calculados e información sobre los datos de entrada. El informe puede consultarse en Workbench o abrirse con cualquier navegador web. Como ejemplo, consulte el `Informe de muestra de Enfriamiento Urbano <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-reports/latest/urban_cooling_model_report.html>`_, generado al ejecutar el modelo de Enfriamiento Urbano con los datos de muestra correspondientes.

* **T_air_[Suffix].tif**: ráster de los valores estimados de temperatura del aire.

* **hm_[Suffix].tif**: índice HMI calculado.

* **cc_[Suffix].tif**: ráster de los valores de CC.

* **uhi_results_[Suffix].shp**: copia del vector de entrada «Área de interés», con los siguientes campos adicionales:
    * **avg_cc**: valor medio de CC (sin unidades).
    * **avg_tmp_v**: valor medio de temperatura (°C).
    * **avg_tmp_an**: anomalía media de temperatura (°C).
    * **avd_eng_cn** (opcional): consumo de energía evitado (kWh o moneda, si se proporcionó la columna opcional ``cost`` en la Tabla de consumo de energía).
    * **avg_wbgt_v** (opcional): WBGT media (°C).
    * **avg_ltls_v** (opcional): pérdida de productividad en trabajos ligeros (%).
    * **avg_hvls_v** (opcional): pérdida de productividad en trabajos pesados (%).

* **buildings_with_stats_[Suffix].shp**: copia del vector de entrada «Huella de los edificios», con los siguientes campos adicionales:
    * **energy_sav**: valor del ahorro de energía (kWh o moneda, si se proporcionó la columna opcional ``cost`` en la Tabla de consumo de energía). El ahorro se calcula en relación con un escenario teórico en el que la ciudad no contiene áreas naturales ni espacios verdes y CC = 0 para todas las clases LULC.
    * **mean_t_air**: valor medio de temperatura en el edificio (°C).

La carpeta ``intermediate`` contiene resultados adicionales del modelo:

* **albedo_[Suffix].tif**: ráster de albedo.
* **area_kernel_[Suffix].tif**: kernel de superficie para la convolución de áreas verdes.
* **building_intensity_[Suffix].tif**: mapa de intensidad de la edificación.
* **cc_masked_green_areas_[Suffix].tif**: ráster de valores CC enmascarados por las áreas que no son verdes.
* **cc_park_[Suffix].tif**: mapa de la capacidad de enfriamiento atenuada según la proximidad a espacios verdes.
* **cc_ref_aoi_stats.pickle**: estadísticas zonales serializadas del ráster CC dentro del AOI.
* **eti_[Suffix].tif**: ráster del índice de evapotranspiración (evapotranspiración de referencia (ETo) multiplicada por el coeficiente de cultivo (Kc) y dividida por ETmax).
* **green_area_sum_[Suffix].tif**: ráster de la superficie total de espacios verdes dentro de una distancia de búsqueda alrededor de cada píxel.
* **green_area_[Suffix].tif**: mapa de áreas verdes.
* **heavy_loss_stats.pickle**: estadísticas zonales serializadas de la pérdida de productividad en trabajos pesados.
* **heavy_work_loss_percent_[Suffix].tif**: mapa del porcentaje de pérdida de productividad laboral en trabajos pesados.
* **kc_[Suffix].tif**: ráster de coeficientes de cultivo.
* **light_loss_stats.pickle**: estadísticas zonales serializadas de la pérdida de productividad en trabajos ligeros.
* **light_work_loss_percent_[Suffix].tif**: mapa del porcentaje de pérdida de productividad laboral en trabajos ligeros.
* **lulc_[Suffix].tif**: ráster de uso y cobertura del suelo alineado con la intersección del AOI, ET0 y LULC.
* **ref_eto_[Suffix].tif**: ráster de evapotranspiración de referencia, reproyectado y alineado con la intersección del AOI, ET0 y LULC.
* **reprojected_aoi_[Suffix].shp**: área de interés definida por el usuario, reproyectada al sistema de referencia espacial del LULC.
* **reprojected_buildings_[Suffix].shp**: vector de edificios definido por el usuario, reproyectado al sistema de referencia espacial del LULC.
* **shade_[Suffix].tif**: ráster de sombra.
* **t_air_aoi_stats.pickle**: estadísticas zonales serializadas de la temperatura del aire dentro del AOI.
* **T_air_nomix_[Suffix].tif**: ráster de los valores estimados de temperatura del aire antes de considerar la mezcla del aire (es decir, antes de aplicar el algoritmo de promedio móvil).
* **wbgt_stats.pickle**: estadísticas zonales serializadas de WBGT.
* **wbgt_[Suffix].tif**: ráster de la WBGT calculada.

Apéndice: fuentes de datos y orientación para seleccionar parámetros
====================================================================

:ref:`Uso y cobertura del suelo <lulc>`
---------------------------------------

:ref:`Kc <kc>`
--------------

:ref:`Evapotranspiración de referencia <et0>`
---------------------------------------------

:ref:`Huella de los edificios <buildings>`
------------------------------------------

Albedo
------
El albedo de la infraestructura urbana construida puede encontrarse en la literatura local sobre microclima. Deilami et al. (2018) y Bartesaghi et al. (2018) ofrecen una revisión útil. Stewart y Oke (2012) presentan rangos de valores para categorías habituales de LULC.

Distancia máxima de enfriamiento de las áreas verdes
----------------------------------------------------
Distancia (metros) a la que los grandes parques urbanos (>2 ha) ejercen un efecto de enfriamiento. Véase una breve revisión en Zardo et al. (2017), que incluye un estudio que informa de un efecto de enfriamiento a una distancia equivalente a cinco veces la altura de los árboles. En ausencia de estudios locales, puede utilizarse una estimación de 450 m.

Temperatura de referencia del aire
----------------------------------
La temperatura del aire de referencia rural (°C) puede obtenerse de estaciones locales de medición de temperatura o de datos climáticos mundiales.

Magnitud del efecto de isla de calor urbana
-------------------------------------------
Es decir, la diferencia entre la temperatura máxima de la ciudad y la temperatura del aire de referencia (de referencia rural). En ausencia de estudios locales, los usuarios pueden obtener valores de un estudio mundial realizado por Yale: https://yceo.users.earthengine.app/view/uhimap

Distancia máxima de mezcla de la temperatura del aire
-----------------------------------------------------
Radio de búsqueda (metros) utilizado en el promedio móvil para tener en cuenta la mezcla del aire. Puede utilizarse un rango inicial recomendado de 500 m a 600 m, basado en pruebas preliminares realizadas en ciudades piloto (Minneapolis-St. Paul, Estados Unidos, y París, Francia). Este parámetro puede utilizarse como parámetro de calibración si se dispone de datos de temperatura observados o modelados.

:ref:`buildings`
----------------

Tabla de consumo de energía
---------------------------
El consumo de energía (kWh/°C) varía considerablemente entre países y ciudades. Santamouris et al. (2015) proporcionan estimaciones del consumo de energía por °C para varias ciudades del mundo. Para Estados Unidos, los datos de EPA EnergyStar Portfolio Manager pueden proporcionar promedios por categoría y datos de edificios específicos: https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/understand-metrics/what-energy

Nota: si la prevalencia del A/C es baja, no debe utilizarse esta métrica de valoración, ya que supone que los costos de energía aumentarán con temperaturas más altas (y un mayor uso del A/C). Los datos sobre la prevalencia del A/C en Estados Unidos pueden obtenerse de la American Housing Survey: https://www.census.gov/programs-surveys/ahs.html

Humedad relativa media
----------------------
La humedad relativa media (%) durante las olas de calor puede obtenerse de estaciones locales de medición de temperatura o de datos climáticos mundiales.


Preguntas frecuentes
====================

* ¿Cuál es la resolución de salida?

    Las salidas del modelo son de dos tipos: rásteres y vectores. Los rásteres tienen la misma resolución que la entrada LULC (todas las demás entradas ráster se remuestrean a esa misma resolución).

* ¿Por qué el modelo no calcula los impactos sobre la salud?

    Los efectos del calor sobre la salud humana varían considerablemente entre ciudades y es difícil desarrollar un modelo InVEST genérico que los represente y cuantifique con precisión para todas ellas. Consulte el apartado «Valoración de los efectos del calor urbano sobre la salud» de la sección Limitaciones del modelo para obtener más detalles y conocer posibles vías para evaluar los impactos del calor urbano sobre la salud.

Referencias
===========

Allen, R. G., Pereira, L. S., Raes, D., & Smith, M. (1998). Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56. FAO, Rome, Italy.

American College of Sports Medicine (1984). Prevention of Thermal Injuries During Distance Running. Medicine and Science in Sports & Exercise, 16(5), ix-xiv. https://doi.org/10.1249/00005768-198410000-00017

Bartesaghi, C., Osmond, P., & Peters, A. (2018). Evaluating the cooling effects of green infrastructure: A systematic review of methods, indicators and data sources. Solar Energy, 166(February), 486-508. https://doi.org/10.1016/j.solener.2018.03.008

Campbell, S., Remenyi, T. A., White, C. J., & Johnston, F. H. (2018). Heatwave and health impact research: A global review. Health & Place, 53, 210-218. https://doi.org/10.1016/j.healthplace.2018.08.017

Deilami, K., Kamruzzaman, M., & Liu, Y. (2018). Urban heat island effect: A systematic review of spatio-temporal factors, data, methods, and mitigation measures. International Journal of Applied Earth Observation and Geoinformation, 67, 30-42. https://doi.org/10.1016/j.jag.2017.12.009

Gasparrini, A., Guo, Y., Hashizume, M., Lavigne, E., Zanobetti, A., Schwartz, J., Tobias, A., Tong, S., Rocklöv, J., Forsberg, B., Leone, M., De Sario, M., Bell, M. L., Guo, Y. L., Wu, C., Kan, H., Yi, S., Coelho, M. d., Saldiva, P. H., Honda, Y., Kim, H., & Armstrong, B. (2015). Mortality risk attributable to high and low ambient temperature: a multicountry observational study. The lancet, 386(9991), 369-375. https://doi.org/10.1016/S0140-6736(14)62114-0

Kjellstrom, T., Holmer, I., & Lemke, B. (2009). Workplace heat stress, health and productivity - an increasing challenge for low and middle-income countries during climate change. Global Health Action, 2, 10.3402/gha.v2i0.2047. https://doi.org/10.3402/gha.v2i0.2047

Kunapo, J., Fletcher, T. D., Ladson, A. R., Cunningham, L., & Burns, M. J. (2018). A spatially explicit framework for climate adaptation. Urban Water Journal, 15(2), 159-166. https://doi.org/10.1080/1573062X.2018.1424216

Lonsdorf, E.V., Nootenboom, C., Janke, B., & Horgan, B.P. (2021). Assessing urban ecosystem services provided by green infrastructure: Golf courses in the Minneapolis-St. Paul metro area. Landscape and Urban Planning, 208. https://doi.org/10.1016/j.landurbplan.2020.104022

McDonald, R. I., Kroeger, T., Boucher, T., Wang, L., & Salem, R. (2016). Planting Healthy Air: A global analysis of the role of urban trees in addressing particulate matter pollution and extreme heat. CAB International, 128-139.

McMichael, A. J., Campbell-Lendrum, D. H., Corvalán, C. F., Ebi, K. L., Githeko, A. k., Scheraga, J. D., & Woodward, A. (2003). Climate change and human health: risks and responses. World Health Organization. Geneva, Switzerland.

Phelan, P. E., Kaloush, K., Miner, M., Golden, J., Phelan, B., Iii, H. S., & Taylor, R. A. (2015). Urban Heat Island: Mechanisms, Implications, and Possible Remedies. Annual Review of Environment and Resources, 285-309. https://doi.org/10.1146/annurev-environ-102014-021155

Santamouris, M., Cartalis, C., Synnefa, A., & Kolokotsa, D. (2015). On the impact of urban heat island and global warming on the power demand and electricity consumption of buildings - A review. Energy & Buildings, 98, 119-124. https://doi.org/10.1016/j.enbuild.2014.09.052

Shatz, J. & Kucharik, C.J. (2014). Seasonality of the Urban Heat Island Effect in Madison, Wisconsin. Journal of Applied Meterology and Climatology, 53(10), 2371-2386. https://doi.org/10.1175/JAMC-D-14-0107.1

Stewart, I. D., & Oke, T. R. (2012). Local climate zones for urban temperature studies. American Meteorological Society. https://doi.org/10.1175/BAMS-D-11-00019.1

Zardo, L., Geneletti, D., Prez-soba, M., & Eupen, M. Van. (2017). Estimating the cooling capacity of green infrastructures to support urban planning. Ecosystem Services, 26, 225-235. https://doi.org/10.1016/j.ecoser.2017.06.016
