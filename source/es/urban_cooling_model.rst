.. _ucm:

*****************************
Modelo de enfriamiento urbano
*****************************

Resumen
=======

La mitigación del calor urbano es una prioridad para muchas ciudades que han sufrido olas de calor en los últimos años. La vegetación puede ayudar a reducir el efecto de isla de calor urbano (ICU) proporcionando sombra, modificando las propiedades térmicas del tejido urbano y aumentando el enfriamiento a través de la evapotranspiración. Esto tiene consecuencias para la salud y el bienestar de la gente a través de la reducción de la mortalidad y la morbilidad, el aumento de la comodidad y la productividad, y la reducción de la necesidad de aire acondicionado (A/C). El modelo de enfriamiento urbano de InVEST calcula un índice de mitigación del calor basado en la sombra, la evapotranspiración y el albedo, así como en la distancia a las islas de enfriamiento (por ejemplo, los parques). El índice se utiliza para estimar una reducción de la temperatura por parte de la vegetación. Por último, el modelo estima el valor del servicio de mitigación del calor utilizando dos métodos de valoración (opcionales): el consumo de energía y la productividad del trabajo.

Introducción
============

Las ICU afectan a muchas ciudades de todo el mundo, con importantes consecuencias para la salud y el bienestar de las personas: alta mortalidad o morbilidad durante las olas de calor, elevado consumo de aire acondicionado y reducción de la comodidad o la productividad laboral. El efecto ICU, es decir, la diferencia entre las temperaturas rurales y urbanas, es el resultado de las características únicas de las ciudades debido a dos factores principales: las propiedades térmicas de los materiales utilizados en las zonas urbanas (por ejemplo, el hormigón, el asfalto), que almacenan más calor, y la reducción del efecto de enfriamiento (a través de la sombra y la evapotranspiración) de la vegetación.

Por lo tanto, la infraestructura natural desempeña un papel en la reducción de las ICU en las ciudades. Utilizando una literatura de rápido crecimiento sobre la modelización del calor urbano (Deilami et al. 2018), el modelo de enfriamiento urbano InVEST estima el efecto de enfriamiento de la vegetación basándose en los datos comúnmente disponibles sobre el clima, el uso del suelo/la cubierta vegetal (LULC) y (opcionalmente) el uso de A/C.

El modelo
=========

Cómo funciona
-------------

Índice de capacidad de enfriamiento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El modelo primero computa el índice de capacidad de enfriamiento (CE) para cada píxel basado en la sombra local, la evapotranspiración y el albedo. Este enfoque se basa en los índices propuestos por Zardo et al. (2017) y Kunapo et al. (2018), a los que añadimos el albedo, un factor importante para la reducción del calor.
El factor de sombra ('shade') representa la proporción de dosel arbóreo (≥2 m de altura) asociado a cada categoría de uso del suelo/cubierta vegetal (LULC). Su valor está comprendido entre 0 y 1.
El índice de evapotranspiración (IET) representa un valor normalizado de la evapotranspiración potencial, es decir, la evapotranspiración de la vegetación (o la evaporación del suelo, para las zonas sin vegetación). Se calcula para cada píxel multiplicando la evapotranspiración de referencia (:math:`ET0`, proporcionada por usted) y el coeficiente de cultivo (:math:`Kc` , asociado al tipo de LULC del píxel), y dividiéndolo por el valor máximo del ráster :math:`ET0` del área de interés, :math:`ETmax`:


.. math:: ETI = \frac{K_c \cdot ET0}{ET_{max}}
    :label: eti

Nótese que esta ecuación supone que las zonas con vegetación están suficientemente regadas (aunque los valores de Kc pueden reducirse para representar la evapotranspiración limitada por el agua).

El factor de albedo es un valor entre 0 y 1 que representa la proporción de radiación solar reflejada por el tipo de LULC (Phelan et al. 2015).

El modelo combina los tres factores en el índice CE:

.. math:: CC_i = 0.6 \cdot shade + 0.2\cdot albedo + 0.2\cdot ETI
    :label: coolingcapacity_factors

La ponderación recomendada (0,6; 0,2; 0,2) se basa en datos empíricos y refleja el mayor impacto del sombreado en comparación con la evapotranspiración. Por ejemplo, Zardo et al. 2017 informan que "en áreas menores de dos hectáreas [a la evapotranspiración] se asignó un peso de 0,2 y un sombreado de 0,8. En áreas mayores de dos hectáreas los pesos se cambiaron a 0,6 y 0,4, para [evapotranspiración] y sombreado respectivamente". En el presente modelo, proponemos desagregar los efectos de la sombra y el albedo en la ecuación (83), y dar al albedo el mismo peso que al IET, basándonos en los resultados de Phelan et al. (2015) (véase la tabla 2 de su estudio, que muestra que la vegetación y el albedo tienen coeficientes similares).

Nota: usted puede introducir manualmente ponderaciones alternativas para comprobar la sensibilidad de los resultados del modelo a este parámetro (o si se dispone de conocimientos locales).

Opcionalmente, el modelo puede considerar otro factor, la intensidad (:math:`building.intensity` para una determinada clasificación de la cobertura del suelo), que capta la dimensión vertical de la infraestructura construida. La intensidad de la construcción es un importante factor de predicción de la temperatura nocturna, ya que el calor almacenado por las construcciones y edificios durante el día se libera durante la noche. Para predecir las temperaturas nocturnas, quienes usan el modelo deben proporcionar el factor de intensidad de las construcciones para cada clase de uso del suelo en la Tabla Biofísica y el modelo cambiará la ecuación :math:numref:`coolingcapacity_factors` a:

.. math:: CC_i = 1 - building.intensity
    :label: coolingcapacity_intensity


Índice de mitigación del calor urbano (efecto de los grandes espacios verdes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para tener en cuenta el efecto de enfriamiento de los grandes espacios verdes (>2 ha) en las zonas circundantes (véase la discusión en Zardo et al. (2017) y McDonald et al. (2016)), el modelo calcula el índice HM urbano: HM es igual a CE si el píxel no está afectado por ningún espacio verde grande, pero en caso contrario se establece un promedio ponderado por la distancia de los valores de CC de los espacios verdes grandes y el píxel de interés.

Para ello, el modelo calcula primero la superficie de los espacios verdes dentro de una distancia de búsqueda :math:`d_{cool}` alrededor de cada píxel (:math:`GA_i`), y la CE que proporciona cada parque (:math:`CC_{park_i}`):

.. math:: {GA}_{i}=cell_{area}\cdot\sum_{j\in\ d\ radius\ from\ i} g_{j}
    :label: [3a]

.. math:: CC_{park_i}=\sum_{j\in\ d\ radius\ from\ i} g_j \cdot CC_j \cdot e^{\left( \frac{-d(i,j)}{d_{cool}} \right)}
    :label: [3b]

where :math:`cell_{area}` is the area of a cell in ha, :math:`g_j` is 1 if pixel :math:`j` es espacio verde o 0 si no lo es, :math:`d(i,j)` es la distancia entre los píxeles :math:`i` y :math:`j`, :math:`d_{cool}` es la distancia sobre la que un espacio verde tiene un efecto de enfriamiento, y :math:`CC_{park_i}` es la media ponderada por distancia de los valores de CC atribuibles a los espacios verdes. (Obsérvese que las clases de LULC que se califican como "espacios verdes" son determinadas por usted con el parámetro `green_area' en la tabla biofísica, véase la tabla de inputs en la sección 3). A continuación, el índice HM se calcula como

.. math:: HM_i = \begin{Bmatrix}
        CC_i & if & CC_i \geq CC_{park_i}\ or\ GA_i < 2 ha \\
        CC_{park_i} & & otherwise
        \end{Bmatrix}
    :label: [4]


Estimaciones de la temperatura del aire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para estimar la reducción del calor en toda la ciudad, el modelo utiliza la magnitud ICU (a escala de la ciudad), :math:`UHI_{max}`. Se pueden obtener los valores de la literatura local o de estudios globales: por ejemplo, el Global Surface UHI Explorer desarrollado por la Universidad de Yale, proporciona estimaciones anuales, estacionales, diurnas y nocturnas (https://yceo.users.earthengine.app/view/uhimap).
Hay que tener en cuenta que la magnitud de la ICU se define para un periodo específico (por ejemplo, el clima actual o futuro) y el tiempo (por ejemplo, las temperaturas nocturnas o diurnas). La selección del periodo y del tiempo afectará a la cuantificación y valoración del servicio.

La temperatura del aire sin mezcla de aire :math:`T_{air_{nomix}} se calcula para cada píxel como:

.. math:: T_{air_{nomix},i}=T_{air,ref} + (1-HM_i)\cdot UHI_{max}
    :label: [5]

Donde :math:`T_{air,ref}` es la temperatura rural de referencia y :math:`UHI_{max}` es la magnitud máxima del efecto ICU para la ciudad (o más precisamente, la diferencia entre :math:`T_{air,ref}` y la temperatura máxima observada en la ciudad).

Debido a la mezcla del aire, estas temperaturas se promedian espacialmente. La temperatura real del aire (con mezcla), :math:`T_{air}`, se deriva de :math:`T_{air_{nomix}} utilizando una función gaussiana con radio de núcleo :math:`r`, definido por usted.

Para cada área de interés (que es una capa SIG vectorial proporcionada por usted), calculamos la temperatura media y la anomalía de temperatura :math:`(T_{air,i} - T_{air,ref})`.

Valor del servicio de reducción de calor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El valor de la reducción de la temperatura puede evaluarse al menos de tres maneras:

    i) ahorro de energía por la reducción del consumo de electricidad del aire acondicionado
    ii) aumento de la productividad laboral en trabajos exteriores;
    iii) disminución de la morbilidad y la mortalidad relacionadas con el calor.

El modelo proporciona estimaciones de (i) ahorro energético y (ii) productividad laboral basadas en análisis de regresión globales o en datos locales.

**Ahorro de energía:** el modelo utiliza una relación entre el consumo de energía y la temperatura (por ejemplo, resumida por Santamouris et al. (2015)) para calcular el ahorro de energía y los costos asociados para una construcción :math:`b`:

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}})
    :label: energy_savings_kwh

Donde:

    * :math:`consumption.increase(b)` (kWh/° C/:math:`m^2`) es la estimación local del aumento del consumo de energía por cada grado de temperatura por metro cuadrado de la huella de construcción, para la categoría de construcción :math:`b`.
    * :math:`T_{air,MAX}` (° C) es la temperatura máxima sobre el paisaje :math:`(T_{air,ref} + UHI_{max})`;
    * :math:`overline{T_{air,MAX}` - T_{air,i}} (° C) es la diferencia media de la temperatura del aire para la construcción :math:`b`, con :math:`T_{air,i}` modelizado en los pasos anteriores.

Si se proporcionan los costos para cada categoría de construcción, la ecuación :math:numref:`energy_savings_kwh` se sustituye por la ecuación :math:numref:`energy_savings_dollars`.

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\cdot T_{air,MAX} - T_{air,i}}) \cdot cost(b)
    :label: energy_savings_dollars

Donde:

    * :math:`cost(b)` es la estimación del costo energético por kWh para la categoría de construcción :math:`b`. Tenga en cuenta que es muy probable que sea igual para todas las construcciones.

Para calcular el ahorro total de energía, sumamos los valores a nivel de píxel sobre el área de interés.

**Productividad laboral:** el modelo convierte la temperatura del aire en temperatura del globo húmedo (TGH) para calcular el impacto del calor en la productividad laboral. La TGH tiene en cuenta la humedad, y puede estimarse a partir de datos meteorológicos estándar de la siguiente manera (American College of Sports Medicine, 1984, Apéndice I):

... math:: WBGT_i = 0,567 \cdot T_{air,i} + 0,393 \cdot e_i + 3,94
    :label: [7]

Donde:

    * :math:`T_{air}` = temperatura proporcionada por el modelo (temperatura de globo seco (° C))
    * :math:`e_i` = presión de vapor de agua (hPa)

La presión de vapor se calcula a partir de la temperatura y la humedad relativa mediante la ecuación

.. math:: e_i = \frac{RH}{100} \cdot 6,105 \cdot e^{left ( 17,27 \cdot \frac{T_{air,i}}(237,7 + T_{air,i})} \cdot )}
    :label: [8]

Donde:

    * :math:`RH` = humedad relativa media (%) proporcionada por usted

Para cada píxel, el modelo calcula la pérdida estimada de productividad (%) para dos intensidades de trabajo: "trabajo ligero" y "trabajo pesado" (basado en el tiempo de descanso necesario a diferentes intensidades de trabajo, según la Tabla 2 de Kjellstrom et al. 2009):

... math:: Loss.light.work_i = \begin{Bmatrix}
        0 & si & WBGT < 31,5\\
        25 & si & 31.5 \leq WBGT < 32.0 \\\a
        50 & si & 32,0 \leq WBGT < 32,5 \\\\a
        75 y si y 32,5 WBGT \N - \N -
        \fin {Bmatrix}
    :label: [9a]

.. math:: Loss.heavy.work_i = \begin{Bmatrix}
        0 & si & WBGT < 27.5\\\\N-
        25 & si & 27.5 \leq WBGT < 29.5 \\\\a
        50 & si & 29,5 \leq WBGT < 31,5 \\\\leq
        75 y si y 31,5 WBGT \N -
        \fin {Bmatrix}
    :label: [9b]

En este caso, el "trabajo ligero" corresponde a una tasa metabólica de aproximadamente 200 vatios, es decir, el trabajo de oficina y las industrias de servicios, y el "trabajo pesado" corresponde a 400 vatios, es decir, la construcción o el trabajo agrícola.
Si no se dispone de datos específicos de la ciudad sobre la distribución de los sectores laborales brutos, usted puede estimar la población activa de la ciudad en 3 sectores (servicios, industria, agricultura) utilizando datos del Banco Mundial a nivel nacional (por ejemplo, "empleo en la industria, hombres (%)" y similares). La pérdida de tiempo de trabajo para una temperatura determinada puede calcularse utilizando los tiempos de descanso de la Tabla 2 (Kjellstrom et al. 2009) y la proporción de población trabajadora en los distintos sectores. Si se dispone de datos locales sobre los salarios medios por hora de los distintos sectores, estas pérdidas de tiempo de trabajo pueden traducirse en pérdidas monetarias.

Por último, en el caso del "trabajo ligero", hay que tener en cuenta que la prevalencia del aire acondicionado puede influir. Si la mayoría de los edificios de oficinas están equipados con A/C, usted podría querer reducir la pérdida de tiempo de trabajo para el sector de servicios en la misma proporción que la prevalencia del A/C.

    * :math:`consumption.increase(b)` (kWh/° C/:math:`m^2`) es la estimación local del aumento del consumo de energía por cada grado de temperatura por metro cuadrado de la huella de construcción, para la categoría de construcción :math:`b`.
    * :math:`T_{air,MAX}` (° C) es la temperatura máxima en el paisaje :math:`(T_{air,ref} + UHI_{max})`;
    * :math:`\overline{T_{air,MAX} - T_{air,i}}` (° C) es la diferencia media de la temperatura del aire para la construcción 
 :math:`b`, con :math:`T_{air,i}` modelizado en los pasos anteriores.

Si se facilitan los costos de cada categoría de construcción, la ecuación :math:numref:`energy_savings_kwh` se sustituye por la ecuación :math:numref:`energy_savings_dollars`.

.. math:: Energy.savings(b)= consumption.increase(b) \cdot (\overline{T_{air,MAX} - T_{air,i}}) \cdot cost(b)
    :label: energy_savings_dollars

Donde:

    * :math:`cost(b)` es la estimación del costo energético por kWh para la categoría de construcción :math:`b`. Tenga en cuenta que es muy probable que esto sea igual para todas las construcciones.

Para calcular el ahorro total de energía, sumamos los valores a nivel de píxel sobre el área de interés.

**Productividad del trabajo:** el modelo convierte la temperatura del aire en temperatura del globo húmedo (TGH) para calcular los efectos del calor en la productividad del trabajo. La TGH tiene en cuenta la humedad, y puede estimarse a partir de datos meteorológicos estándar de la siguiente manera (American College of Sports Medicine, 1984, Apéndice I):

.. math:: WBGT_i = 0.567 \cdot T_{air,i} + 0.393 \cdot e_i + 3.94
    :label: [7]

Donde:

    * :math:`T_{air}` = temperatura proporcionada por el modelo (temperatura de bulbo seco (° C))
    * :math:`e_i` = presión de vapor de agua (hPa)

La presión de vapor se calcula a partir de la temperatura y la humedad relativa mediante la ecuación:

.. math:: e_i = \frac{RH}{100} \cdot 6.105 \cdot e^{\left ( 17.27 \cdot \frac{T_{air,i}}{(237.7 + T_{air,i})} \right )}
    :label: [8]

Donde:

    * :math:`RH` = Humedad relativa media (%) proporcionada por usted

Para cada píxel, el modelo calcula la pérdida estimada de productividad (%) para dos intensidades de trabajo: "trabajo ligero" y "trabajo pesado" (basado en el tiempo de descanso necesario a diferentes intensidades de trabajo, según la Tabla 2 de Kjellstrom et al. 2009):

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

En este caso, el "trabajo ligero" corresponde a una tasa metabólica de aproximadamente 200 vatios, es decir, el trabajo de oficina y las industrias de servicios, y el "trabajo pesado" corresponde a 400 vatios, es decir, la construcción o el trabajo agrícola.
Si no se dispone de datos específicos de la ciudad sobre la distribución de los sectores laborales brutos, se puede estimar la población activa de la ciudad en 3 sectores (servicios, industria, agricultura) utilizando datos del Banco Mundial a nivel nacional (por ejemplo, "empleo en la industria, hombres (%)" y similares). La pérdida de tiempo de trabajo para una temperatura determinada puede calcularse utilizando los tiempos de descanso de la Tabla 2 (Kjellstrom et al. 2009) y la proporción de población trabajadora en los distintos sectores. Si se dispone de datos locales sobre los salarios medios por hora de los distintos sectores, estas pérdidas de tiempo de trabajo pueden traducirse en pérdidas monetarias.

Por último, en el caso del "trabajo ligero", hay que tener en cuenta que la prevalencia del aire acondicionado puede influir. Si la mayoría de los edificios de oficinas están equipados con A/C, usted podría querer reducir la pérdida de tiempo de trabajo para el sector de servicios en la misma proporción que la prevalencia del A/C.

Limitaciones y simplificaciones
==============================

Debido a las simplificaciones descritas anteriormente, el modelo presenta una serie de limitaciones que se resumen aquí.

Índice CE: el índice se basa en ponderaciones empíricas, derivadas de un número limitado de estudios de casos, que modulan el efecto de los factores clave que contribuyen al efecto de enfriamiento (ecuación (83)). Este paso de ponderación comprende altas incertidumbres, como se revisa en Zardo et al. (2017). Para caracterizar y reducir esta incertidumbre, se puede probar la sensibilidad del modelo a estos parámetros o realizar estudios experimentales que proporcionen información sobre los efectos relativos de la sombra, el albedo y la evapotranspiración.

Efecto de los grandes parques y de la mezcla de aire: dos parámetros captan el efecto de los grandes espacios verdes y de la mezcla de aire ( :math:`d_{cool}` y :math:`r`). El valor de estos parámetros es difícil de obtener a partir de la literatura, ya que varían con las propiedades de la vegetación, el clima (efecto de los grandes espacios verdes) y los patrones de viento (mezcla de aire). De forma similar a lo que ocurre con el CE, usted puede caracterizar y reducir estas incertidumbres probando la sensibilidad del modelo a estos parámetros y comparando los patrones espaciales de temperatura estimados por el modelo con los datos observados o modelizados (véanse Bartesaghi et al. 2018 y Deilami et al. 2018 para obtener información adicional sobre dichas comparaciones).

Opciones de valoración: las opciones de valoración que actualmente admite el modelo están relacionadas con el consumo de energía de A/C y la productividad del trabajo al aire libre. Para el consumo de energía de A/C, se necesita evaluar la prevalencia de A/C y reducir las estimaciones en consecuencia (es decir, reducir el consumo de energía proporcionalmente al uso real de A/C).

La valoración de los efectos del calor urbano sobre la salud no se incluye actualmente en el modelo, a pesar de su importancia (McDonald et al. 2016). Esto se debe a que estos efectos varían drásticamente entre ciudades y es difícil extrapolar los conocimientos actuales basados predominantemente en el Norte Global (Campbell et al. 2018). Las posibles opciones para obtener estimaciones del impacto en la salud incluyen:

* utilizar los datos globales de McMichael et al. (2003), que utilizan una relación lineal por encima de un umbral de temperatura para estimar la fracción anual atribuible de muertes debidas a los días calurosos o,
* para aplicaciones en los Estados Unidos, se desarrolló una metodología basada en las relaciones a escala nacional entre la mortalidad y el cambio de temperatura: véase McDonald et al. (2016).

Gasparrini et al. (2014) desglosan el aumento de la mortalidad atribuible al calor para 384 ciudades de 13 países. El resultado de :math:`T_air` del modelo InVEST podría utilizarse para determinar la fracción de mortalidad atribuible al calor (primero determinar en qué percentil cae :math:`T_{air,i}`, y luego utilizar la Tabla S3 o la Tabla S4 del apéndice).

Necesidades de datos
===================

.. note:: *Todos los inputs espaciales deben tener exactamente el mismo sistema de coordenadas proyectadas* (con unidades lineales de metros), *no* un sistema de coordenadas geográficas (con unidades de grados).

- :investspec:`urban_cooling_model workspace_dir`

- :investspec:`urban_cooling_model results_suffix`

- :investspec:`urban_cooling_model lulc_raster_path` El modelo utilizará la resolución de esta capa para remuestrear todos los resultados. La resolución debe ser lo suficientemente pequeña como para captar el efecto de los espacios verdes en el paisaje, aunque las categorías de LULC pueden comprender una mezcla de coberturas con y sin vegetación (por ejemplo, "residencial", que puede tener una cobertura de dosel del 30%).

- :investspec:`urban_cooling_model biophysical_table_path`

  Columnas:

  - :investspec:`urban_cooling_model biophysical_table_path.columns.lucode`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.kc`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.green_area` Las zonas verdes de más de 2 hectáreas tienen un efecto refrigerante adicional.
  - :investspec:`urban_cooling_model biophysical_table_path.columns.shade`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.albedo`
  - :investspec:`urban_cooling_model biophysical_table_path.columns.building_intensity`

- :investspec:`urban_cooling_model ref_eto_raster_path` Estos valores pueden ser para una fecha específica o se pueden usar valores mensuales como sustituto proxy.

- :investspec:`urban_cooling_model aoi_vector_path` La(s) ADI(s) suelen ser los límites de la ciudad o del barrio.

- :investspec:`urban_cooling_model green_area_cooling_distance` Es :math:`d_{cool}` en la ecuación :eq:`[3b]`. Valor recomendado: 450 m.

- :investspec:`urban_cooling_model t_ref` Esto es :math:`T_{air,ref}` en la ecuación :eq:`[5]`. Puede ser la temperatura nocturna o diurna, para una fecha concreta o una media de varios días. Los resultados se darán para el mismo periodo de interés.

- :investspec:`urban_cooling_model uhi_max` Esto es :math:`UHI_{max}` en la ecuación :eq:`[5]`.

- :investspec:`urban_cooling_model t_air_average_radius` Rango de valores recomendado para la ejecución inicial: 500 m a 600 m; véanse Schatz et al. (2014) y Lonsdorf et al. (2021).

- :investspec:`urban_cooling_model cc_method`

- :investspec:`urban_cooling_model building_vector_path`

  Campo:

  - :investspec:`urban_cooling_model building_vector_path.fields.type`

- :investspec:`urban_cooling_model do_energy_valuation`
- :investspec:`urban_cooling_model do_productivity_valuation`

- :investspec:`urban_cooling_model energy_consumption_table_path`

  Columnas

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.type`
  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.consumption`

    .. note::
       El valor del **consumo** es por unidad de superficie de *huella*, no de superficie de piso. Este valor debe ajustarse al número medio de pisos de las estructuras de este tipo.

  - :investspec:`urban_cooling_model energy_consumption_table_path.columns.cost` Es muy probable que los valores de esta columna sean los mismos para todos los tipos de construcciones.

- :investspec:`urban_cooling_model avg_rel_humidity`

- :investspec:`urban_cooling_model cc_weight_shade`
- :investspec:`urban_cooling_model cc_weight_albedo`
- :investspec:`urban_cooling_model cc_weight_eti`

Interpretación de los resultados
==============================

* hm_[Suffix].tif: The calculated HMI.
* uhi_results_[Suffix].shp: Una copia del vector de input "Área de interés" con los siguientes campos adicionales:
    * "avg_cc" - Valor medio de CE (-).
    * "avg_tmp_v" - Valor medio de la temperatura (gradC).
    * "avg_tmp_an" - Anomalía de la temperatura media (gradC).
    * "avd_eng_cn" - (opcional) Consumo de energía evitado (kWh o $ si la columna opcional de input de energía ``costo` se proporcionó en la tabla de consumo de energía).
    * "avg_wbgt_v" - (opcional) TGH media (gradC).
    * "avg_ltls_v" - (opcional) Pérdida de productividad en trabajos ligeros (%).
    * "avg_hvls_v" - (opcional) Pérdida de productividad en el trabajo pesado (%).
* buildings_with_stats_[Sufijo].shp: Una copia del vector de input "Huellas de construcciones" con los siguientes campos adicionales:
    * "energy_sav" - Valor de ahorro de energía (kWh o moneda si se proporcionó la columna opcional de input de energía ``costo`` en la Tabla de Consumo de Energía). El ahorro es relativo a un escenario teórico en el que la ciudad NO contiene áreas naturales ni espacios verdes; donde CE = 0 para todas las clases LULC.
    * "mean_t_air" - Valor medio de la temperatura en la construcción (gradC).

La carpeta intermedia contiene resultados adicionales del modelo:

* cc_[Sufijo].tif: Ráster de valores CE.
* T_air_[Sufijo].tif: Ráster de valores estimados de temperatura del aire.
* T_air_nomix_[Suffijo].tif: Ráster de los valores de temperatura del aire estimados antes de la mezcla del aire (es decir, antes de aplicar el algoritmo de media móvil).
* eti_[Sufijo].tif: Ráster de valores de evapotranspiración real (evapotranspiración de referencia por coeficiente de cultivo "Kc").
* wbgt_[Sufijo].tif: Ráster del TGH calculado.
* reprojected_aoi_[Sufijo].shp: El área de interés definida por usted, reproyectada a la referencia espacial del LULC.
* reprojected_buildings_[Sufijo].shp: El vector de construcciones definido por usted, reproyectado a la referencia espacial de la LULC.

Apéndice: Fuentes de datos y orientación para la selección de parámetros
=================================================================

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

:ref:`Kc <kc>`
--------------

:ref:`Reference Evapotranspiration <et0>`
-----------------------------------------

:ref:`Building Footprints <buildings>`
--------------------------------------

Albedo
------
El albedo para las infraestructuras urbanas construidas puede encontrarse en la literatura sobre el microclima local. Deilami et al. (2018) y Bartesaghi et al. (2018) proporcionan una revisión útil. Stewart y Oke (2012) proporcionan rangos de valores para las categorías típicas de LULC.

Distancia máxima de enfriamiento de la zona verde
---------------------------------------------
Distancia (metros) en la que los  parques urbanos grandes (>2 ha) tienen un efecto de enfriamiento. Véase una breve revisión en Zardo et al. (2017), que incluye un estudio que informa de un efecto de enfriamiento a una distancia cinco veces superior a la altura del árbol. En ausencia de estudios locales, se puede utilizar una estimación de 450 m.

Temperatura del aire de referencia
------------------------
La temperatura de referencia rural (°C) puede obtenerse de estaciones de temperatura locales o de datos climáticos globales.

Magnitud del efecto ICU
---------------------------
Es decir, la diferencia entre la temperatura máxima en la ciudad y la temperatura del aire de referencia rural (línea de base). A falta de estudios locales, se pueden obtener los valores de un estudio global realizado por Yale: https://yceo.users.earthengine.app/view/uhimap

Distancia de mezcla máxima de la temperatura del aire
-----------------------------------------
Radio de búsqueda (metros) utilizado en la media móvil para tener en cuenta la mezcla del aire. Se puede utilizar un rango de valores iniciales recomendados de 500 m a 600 m basado en pruebas preliminares en ciudades piloto (Minneapolis-St Paul, EE.UU. y París, Francia). Este parámetro puede utilizarse como parámetro de calibración si se dispone de datos de temperatura observados o modelizados.

:ref:`buildings`
----------------

Tabla de consumo de energía
-------------------------
El consumo de energía (kWh/°C) varía mucho entre países y ciudades. Santamouris et al. (2015) proporcionan estimaciones del consumo de energía por °C para una serie de ciudades de todo el mundo. En el caso de Estados Unidos, los datos de la EPA EnergyStar Portfolio Manager pueden proporcionar promedios categóricos, así como datos de construcciones específicas: https://www.energystar.gov/buildings/facility-owners-and-managers/existing-buildings/use-portfolio-manager/understand-metrics/what-energy. Nota: Si la prevalencia del aire acondicionado es baja, esta métrica de valoración no debería utilizarse, ya que asume que los costos energéticos aumentarán con las temperaturas más altas (y un mayor uso del aire acondicionado). Los datos de prevalencia de A/C para los EE.UU. pueden obtenerse de la encuesta American Housing Survey: https://www.census.gov/programs-surveys/ahs.html

Humedad relativa media
---------------------
La humedad relativa media (%) durante las olas de calor puede obtenerse de las estaciones de temperatura locales o de los datos climáticos globales.

Preguntas frecuentes
===================

* ¿Cuál es la resolución de salida?

    Las resultados del modelo son de dos tipos: rásteres y vectores. Los rásteres tienen la misma resolución que el input LULC (todos los demás inputs ráster se remuestrean a la misma resolución).

* ¿Por qué el modelo no calcula los impactos sobre la salud?

    Los efectos del calor en la salud humana varían enormemente entre las ciudades y es difícil desarrollar un modelo genérico de InVEST que los capte y cuantifique con precisión para todas las ciudades. Véase el punto sobre "Valoración de los efectos del calor urbano sobre la salud" en la sección de Limitaciones del modelo para obtener más detalles y vías para evaluar los impactos de la mitigación del calor urbano sobre la salud.

Referencias
==========

Allen, R. G., Pereira, L. S., Raes, D. y Smith, M. (1998). Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56. FAO, Roma, Italia.

American College of Sports Medicine (1984). Prevention of Thermal Injuries During Distance Running. Medicine and Science in Sports & Exercise, 16(5), ix-xiv. https://doi.org/10.1249/00005768-198410000-00017

Bartesaghi, C., Osmond, P. y Peters, A. (2018). Evaluating the cooling effects of green infrastructure : A systematic review of methods, indicators and data sources. Solar Energy, 166(February), 486-508. https://doi.org/10.1016/j.solener.2018.03.008

Campbell, S., Remenyi, T. A., White, C. J. y Johnston, F. H. (2018). Heatwave and health impact research: A global review. Health & Place, 53, 210-218. https://doi.org/https://doi.org/10.1016/j.healthplace.2018.08.017

Deilami, K., Kamruzzaman, M. y Liu, Y. (2018). Urban heat island effect: A systematic review of spatio-temporal factors, data, methods, and mitigation measures. International Journal of Applied Earth Observation and Geoinformation, 67, 30-42. https://doi.org/https://doi.org/10.1016/j.jag.2017.12.009

Gasparrini, A., Guo, Y., Hashizume, M., Lavigne, E., Zanobetti, A., Schwartz, J., Tobias, A., Tong, S., Rocklöv, J., Forsberg, B., Leone, M., De Sario, M., Bell, M. L., Guo, Y. L., Wu, C., Kan, H., Yi, S., Coelho, M. d., Saldiva, P. H., Honda, Y., Kim, H. y Armstrong, B. (2015). Mortality risk attributable to high and low ambient temperature: a multicountry observational study. The lancet, 386(9991), 369-375. https://doi.org/10.1016/S0140-6736(14)62114-0

Kjellstrom, T., Holmer, I. y Lemke, B. (2009). Workplace heat stress, health and productivity - an increasing challenge for low and middle-income countries during climate change. Global Health Action, 2, 10.3402/gha.v2i0.2047. https://doi.org/10.3402/gha.v2i0.2047

Kunapo, J., Fletcher, T. D., Ladson, A. R., Cunningham, L. y Burns, M. J. (2018). A spatially explicit framework for climate adaptation. Urban Water Journal, 15(2), 159-166. https://doi.org/10.1080/1573062X.2018.1424216

Lonsdorf, E.V., Nootenboom, C., Janke, B. y Horgan, B.P. (2021). Assessing urban ecosystem services provided by green infrastructure: Golf courses in the Minneapolis-St. Paul metro area. Landscape and Urban Planning, 208. https://doi.org/10.1016/j.landurbplan.2020.104022

McDonald, R. I., Kroeger, T., Boucher, T., Wang, L. y Salem, R. (2016). Planting Healthy Air: A global analysis of the role of urban trees in addressing particulate matter pollution and extreme heat. CAB International, 128-139.

McMichael, A. J., Campbell-Lendrum, D. H., Corvalán, C. F., Ebi, K. L., Githeko, A. k., Scheraga, J. D. y Woodward, A. (2003). Climate change and human health: risks and responses. World Health Organization. Ginebra, Suiza.

Phelan, P. E., Kaloush, K., Miner, M., Golden, J., Phelan, B., Iii, H. S. y Taylor, R. A. (2015). Urban Heat Island : Mechanisms , Implications , and Possible Remedies. Annual Review of Environment and Resources, 285-309. https://doi.org/10.1146/annurev-environ-102014-021155

Santamouris, M., Cartalis, C., Synnefa, A. y Kolokotsa, D. (2015). On the impact of urban heat island and global warming on the power demand and electricity consumption of buildings - A review. Energy & Buildings, 98, 119-124. https://doi.org/10.1016/j.enbuild.2014.09.052

Shatz, J. y Kucharik, C.J. (2014). Seasonality of the Urban Heat Island Effect in Madison, Wisconsin. Journal of Applied Meteorology and Climatology, 53(10), 2371-2386. https://doi.org/10.1175/JAMC-D-14-0107.1

Stewart, I. D. y Oke, T. R. (2012). Local climate zones for urban temperature studies. American Meteorological Society. https://doi.org/10.1175/BAMS-D-11-00019.1

Zardo, L., Geneletti, D., Prez-soba, M. y Eupen, M. Van. (2017). Estimating the cooling capacity of green infrastructures to support urban planning. Ecosystem Services, 26, 225-235. https://doi.org/10.1016/j.ecoser.2017.06.016
