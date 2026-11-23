.. _crop_production:

**********************
Producción de cultivos
**********************

Resumen
=======

Los modelos de percentiles de producción de cultivos y de regresión de producción de cultivos estiman el rendimiento y el valor nutricional de un conjunto fijo de cultivos, a partir de información sobre la cobertura del suelo proporcionada por el usuario. El rendimiento de los cultivos depende principalmente del clima y, si se dispone de datos sobre las tasas de fertilización, el modelo de regresión también puede tenerlos en cuenta.


Introducción
============

Ampliar la producción agrícola y reducir las brechas de rendimiento constituye una estrategia fundamental para muchos gobiernos y organismos de desarrollo que trabajan en la reducción de la pobreza y el logro de la seguridad alimentaria. Sin embargo, la conversión de hábitats naturales en tierras de producción agrícola afecta a otros servicios ecosistémicos que son esenciales para mantener los beneficios económicos que la agricultura proporciona a las comunidades locales. Las prácticas agrícolas intensivas pueden aumentar las cargas contaminantes en las fuentes de agua, lo que a menudo hace necesarios métodos de purificación del agua costosos en el futuro. El uso excesivo de agua también amenaza la disponibilidad del recurso para la generación hidroeléctrica y otros servicios. Aun así, la producción de cultivos es esencial para el bienestar y los medios de vida humanos. El modelo de producción de cultivos de InVEST permite examinar en detalle los costos y beneficios de esta actividad humana fundamental, y explorar preguntas como las siguientes:

+ ¿Cómo se compararía una distribución o selección diferente de sistemas de cultivo con los sistemas actuales en términos de producción total? ¿Cambiar de cultivo podría generar mayores rendimientos económicos o un mayor valor nutricional?

+ ¿Cuáles son los efectos de la intensificación agrícola sobre los servicios ecosistémicos? Si se utiliza menos tierra para producir la misma cantidad de alimentos mediante una mayor intensificación, ¿el resultado neto sobre la provisión de servicios ecosistémicos sería positivo o negativo?

+ ¿Cómo podemos evaluar distintas estrategias para satisfacer el aumento de la demanda de alimentos y, al mismo tiempo, minimizar los efectos sobre los servicios ecosistémicos?


El modelo
=========

El modelo de producción de cultivos de InVEST se divide en un modelo de rendimiento basado en percentiles, que abarca 172 cultivos en todo el mundo, y un modelo basado en regresión, que considera las tasas de fertilización para 10 cultivos. Estos modelos se ponen a disposición del usuario como modelos de «percentiles» y de «regresión».

Todos los resultados se comparan con los resultados observados en la misma región para realizar controles de calidad, y se acompañan de información nutricional sobre 33 macro y micronutrientes.

Modelo de percentiles
---------------------

El modelo de percentiles de producción de cultivos de InVEST genera estimaciones del rendimiento de 172 cultivos a partir de datos existentes, resúmenes de percentiles y rendimientos observados. Estas observaciones se basan en conjuntos de datos de la FAO y de escala subnacional para 172 cultivos, expresados en toneladas métricas por hectárea (Monfreda et al., 2008), así como en información nutricional. Los rendimientos por percentiles permiten explorar distintos niveles de intensificación y presentan los rendimientos correspondientes a los percentiles 25, 50, 75 y 95, junto con los datos de rendimiento observado en cada intervalo climático de cada cultivo.

Modelo de regresión
-------------------

Para 10 cultivos básicos cuyos rendimientos se han modelado a escala mundial por Mueller et al. (2011), el modelo de regresión de producción de cultivos puede estimar los rendimientos a partir de los insumos de fertilizantes. Estos cultivos son cebada, maíz, palma aceitera, papa, arroz, soya, remolacha azucarera, caña de azúcar, girasol y trigo. Para ejecutar este modelo, el usuario debe proporcionar una tabla adicional que relacione los cultivos con las tasas de aplicación de nitrógeno, fosfato y potasa (kg/ha) por cultivo. El modelo genera los rendimientos modelados y observados de los cultivos, así como su valor nutricional.


Funcionamiento
--------------

Conjuntos de datos proporcionados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los datos de muestra contienen un directorio **model_data** que almacena los conjuntos de datos globales de Monfreda en los que se basa el modelo:

- **climate_percentile_yield_tables** (modelo de percentiles): para cada cultivo, un archivo CSV que contiene los rendimientos de los percentiles 25, 50, 75 y 95 en cada intervalo climático. Estos percentiles se derivan de los conjuntos de datos globales de rendimiento observado y de intervalos climáticos. Por ejemplo, el valor del percentil 95 para el trigo en el intervalo climático 1 es 3.763889. Esto significa que el 95 % de las áreas donde se cultiva trigo en el intervalo climático 1 producen menos de 3.763889 toneladas métricas por hectárea. El percentil 50 representa un rendimiento «promedio», mientras que el percentil 95 representa un rendimiento cercano al óptimo, que podría alcanzarse mediante la mejora de las prácticas agrícolas.
- **climate_regression_yield_tables** (modelo de regresión): para cada cultivo, un archivo CSV con los parámetros de regresión de cada intervalo climático.
- **crop_nutrient.csv** (modelos de percentiles y de regresión): una tabla que muestra los valores nutricionales de cada cultivo.
- **crop_to_climate_bin.csv** (modelos de percentiles y de regresión): una tabla que relaciona el nombre de cada cultivo con el ráster correspondiente de intervalos climáticos.
- **crop_to_observed_yield.csv** (modelos de percentiles y de regresión): una tabla que relaciona el nombre de cada cultivo con el ráster correspondiente de rendimiento observado.
- **crop_to_percentile_yield.csv** (modelo de percentiles): una tabla que relaciona el nombre de cada cultivo con la tabla correspondiente de rendimientos por percentiles.
- **crop_to_regression_yield.csv** (modelo de regresión): una tabla que relaciona el nombre de cada cultivo con la tabla correspondiente de rendimientos de regresión.
- **extended_climate_bin_maps** (modelos de percentiles y de regresión): para cada cultivo, un ráster global de intervalos climáticos correspondientes a ese cultivo (véanse los métodos suplementarios de Mueller et al., 2012, para más detalles).
- **observed_yield** (modelos de percentiles y de regresión): para cada cultivo, un ráster global del rendimiento realmente observado alrededor del año 2000.


Modelo de percentiles
^^^^^^^^^^^^^^^^^^^^^

El algoritmo del modelo de percentiles es el siguiente, para cada tipo de cultivo (los resultados correspondientes se indican entre paréntesis):

1. Recortar el mapa global de intervalos climáticos de **model_data/extended_climate_bin_maps/** a la extensión del mapa de cobertura del suelo proporcionado por el usuario (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**).
2. Para cada percentil (25, 50, 75 y 95):

   a. Reclasificar el mapa climático recortado del paso (1), utilizando los valores de **model_data/climate_percentile_yield_tables**, para obtener un mapa de rendimientos por percentil (**intermediate_outputs/<crop>_yield_<percentile>_coarse_yield.tif**).
   b. Interpolar el mapa a la misma resolución que el mapa de cobertura del suelo, transformando los píxeles grandes de 1/12 de grado en un gradiente más suave (**intermediate_outputs/<crop>_yield_<percentile>_interpolated_yield.tif**).
   c. Enmascarar las áreas donde, según el mapa de cobertura del suelo, no se cultiva ese cultivo (**<crop>_yield_<percentile>_production.tif**).

3. Recortar el mapa global de rendimiento observado de **model_data/observed_yield/** a la extensión del mapa de cobertura del suelo y sustituir por cero los valores de los píxeles nodata (**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
4. Interpolar el mapa a la misma resolución que el mapa de cobertura del suelo, transformando los píxeles grandes de 1/12 de grado en un gradiente más suave (**intermediate_outputs/<crop>_interpolated_observed_yield.tif**).
5. Enmascarar las áreas donde, según el mapa de cobertura del suelo, no se cultiva ese cultivo (**<crop>_observed_production.tif**).
6. Sumar los valores de rendimiento y los valores nutricionales (utilizando los datos de **model_data/crop_nutrient.csv**) y tabular los resultados (**result_table.csv**).
7. Si se proporcionó un vector de polígonos de agregación, sumar los valores dentro de cada polígono de agregación y tabularlos (**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


Modelo de regresión
^^^^^^^^^^^^^^^^^^^

El algoritmo del modelo de regresión es el siguiente, para cada tipo de cultivo (los resultados correspondientes se indican entre paréntesis):

1. Recortar el mapa global de intervalos climáticos de **model_data/extended_climate_bin_maps/** a la extensión del mapa de cobertura del suelo proporcionado por el usuario (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**).
2. Para cada parámetro de regresión:

   a. Reclasificar el mapa climático recortado del paso (1), utilizando los valores de **model_data/climate_regression_yield_tables**, para obtener un mapa de valores de los parámetros de regresión (**intermediate_outputs/<crop>_<parameter>_coarse_regression_parameter.tif**).
   b. Interpolar el mapa a la misma resolución que el mapa de cobertura del suelo, transformando los píxeles grandes de 1/12 de grado en un gradiente más suave (**intermediate_outputs/<crop>_<parameter>_interpolated_regression_parameter.tif**).

3. Para cada elemento fertilizante (nitrógeno, fósforo y potasio):

   a. Calcular un ráster del rendimiento del cultivo en función de ese elemento, utilizando los rásteres de parámetros de regresión del paso (2) (**intermediate_outputs/<crop>_<element>_yield.tif**).

4. Calcular el rendimiento del cultivo tomando el mínimo de los valores de cada píxel de los tres rásteres de rendimiento del paso (3) (**<crop>_regression_production.tif**).
5. Recortar el mapa global de rendimiento observado de **model_data/observed_yield/** a la extensión del mapa de cobertura del suelo y sustituir por cero los valores de los píxeles nodata (**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
6. Interpolar el mapa a la misma resolución que el mapa de cobertura del suelo, transformando los píxeles grandes de 1/12 de grado en un gradiente más suave (**intermediate_outputs/<crop>_interpolated_observed_yield.tif**).
7. Enmascarar las áreas donde, según el mapa de cobertura del suelo, no se cultiva ese cultivo (**<crop>_observed_production.tif**).
8. Sumar los valores de rendimiento y los valores nutricionales (utilizando los datos de **model_data/crop_nutrient.csv**) y tabular los resultados (**result_table.csv**).
9. Si se proporcionó un vector de polígonos de agregación, sumar los valores dentro de cada polígono de agregación y tabularlos (**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


La propia regresión del cultivo (pasos 3 y 4 anteriores) proviene de Mueller et al. (2012) y tiene la siguiente forma:

.. math:: Y_{mod_{GC}}=\min(Y_{max}(1-b_{NP}\exp(-c_N N_{GC})), Y_{max}(1-b_{NP} \exp(-c_P P_{GC})), Y_{max}(1-b_K \exp(-c_K K_{GC})))

Donde :math:`N_{GC}, P_{GC}, K_{GC}` son las tasas de fertilización proporcionadas por el usuario (N = nitrógeno, P = fósforo, K = potasio), y los demás parámetros de regresión se proporcionan como datos globales del modelo.



Limitaciones y simplificaciones
===============================

La versión actual del modelo es un modelo global de resolución gruesa, impulsado principalmente por el clima y, de manera opcional, por el manejo agrícola. Por lo tanto, no puede representar la variación de productividad que se produce en paisajes heterogéneos. En el modelo actual, una ladera rocosa y un valle fluvial fértil recibirían el mismo valor de rendimiento si comparten las mismas condiciones climáticas. Esto representa un problema si la pregunta de interés es dónde priorizar la conversión futura de hábitats o dónde la agricultura es más productiva y menos destructiva.

Datos necesarios
================

Hay dos modelos de producción de cultivos de InVEST disponibles: un modelo de observaciones basado en percentiles, que funciona con 172 cultivos, y un modelo de regresión para explorar las tasas de fertilización, que funciona con 10 cultivos. Los argumentos que se presentan a continuación corresponden a ambos modelos, salvo que se indique lo contrario.

**Importante**: debe descargar los datos de muestra de InVEST para Producción de cultivos a fin de obtener el conjunto de datos de Monfreda, necesario como dato de entrada de los modelos. Puede descargar estos datos desde InVEST Workbench: abra el menú de navegación de la aplicación, seleccione ``Download Sample Data`` y luego ``Crop Production``. También puede descargar los datos desde la página `Descargas, guías del usuario y fuentes de datos de InVEST <https://naturalcapitalalliance.stanford.edu/software/invest/invest-downloads-data>`_: siga el enlace a ``Individual Sample Datasets for InVEST`` y luego seleccione ``CropProduction.zip``.

Consulte también los datos de muestra de Producción de cultivos para ver ejemplos de todos estos datos de entrada. Esto le ayudará a identificar los tipos de archivo, la estructura de las carpetas y el formato de las tablas. Tenga en cuenta que todos los datos SIG de entrada deben utilizar el mismo sistema de coordenadas proyectadas y unidades lineales en metros.

Para ambos modelos
------------------

- :investspec:`crop_production_percentile workspace_dir`

- :investspec:`crop_production_percentile results_suffix`

- :investspec:`crop_production_percentile climate_bin_raster_table`

- :investspec:`crop_production_percentile observed_yield_raster_table`

- :investspec:`crop_production_percentile crop_nutrient_table`

- :investspec:`crop_production_percentile landcover_raster_path` Este ráster debe tener un sistema de coordenadas proyectadas con unidades en metros (por ejemplo, UTM), porque las áreas de los píxeles se dividen por 10 000 para expresar algunos resultados en hectáreas. Solo puede haber una clase de uso/cobertura del suelo (LULC) asociada a cada tipo de cultivo. Si tiene varias clases LULC que deben asignarse a un cultivo determinado, tendrá que combinar esas clases en una sola clase en el ráster LULC antes de utilizarlo en el modelo.

- :investspec:`crop_production_percentile aggregate_polygon_path`


Datos adicionales necesarios para el modelo de percentiles
----------------------------------------------------------

- :investspec:`crop_production_percentile percentile_yield_csv_table`

- :investspec:`crop_production_percentile landcover_to_crop_table_path` Solo puede haber una clase de cobertura del suelo asociada a cada tipo de cultivo. Consulte la descripción de uso/cobertura del suelo anterior para obtener más información.

  Columnas:

  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.crop_name`

  Ejemplo:

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/landcover_to_crop_table.csv
    :header-rows: 1
    :name: Ejemplo de tabla de cobertura del suelo y cultivos

Datos adicionales necesarios para el modelo de regresión
--------------------------------------------------------

- :investspec:`crop_production_regression regression_yield_csv_table`

- :investspec:`crop_production_regression landcover_to_crop_table_path`

  Columnas:

  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.crop_name`

- :investspec:`crop_production_regression fertilization_rate_table_path` A continuación se incluye una tabla de ejemplo derivada de los valores medianos de las tasas de fertilización observadas en CBI. Los usuarios pueden explorar los datos CBI sin procesar en los datos de muestra: ``CropProduction/sample_user_data/CBI mod yield_USE AS CHECK``. (Consulte la nota **Importante** anterior para obtener información sobre cómo conseguir estos datos).

  Columnas:

  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.crop_name`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.nitrogen_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.phosphorus_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.potassium_rate`

  **Ejemplo de tabla de fertilización:**

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/crop_fertilization_rates.csv
    :header-rows: 1
    :name: Ejemplo de tasas de fertilización de cultivos. Los valores provienen de la mediana de la distribución observada de las tasas de fertilización de CBI.


Interpretación de los resultados
================================

.. note:: A partir de InVEST 3.15.0, los resultados ráster de los modelos de Producción de cultivos (tanto de percentiles como de regresión) se expresan como valores *por hectárea*.

A continuación se presenta una breve descripción de cada uno de los resultados del modelo de Producción de cultivos. Los resultados finales se encuentran en el espacio de trabajo definido por el usuario para esta ejecución del modelo. «Suffix» en los siguientes nombres de archivo se refiere al dato de entrada opcional de sufijo definido por el usuario.

- **aggregate_results_[Suffix].csv**: si se proporciona un archivo shapefile de polígonos de resultados agregados, se genera una tabla que resume la producción total observada, por percentiles o modelada, y la información nutricional dentro de cada polígono.

- **Rásteres de producción de cultivos**: para cada cultivo modelado, se genera un ráster (.tif) cuyo nombre corresponde al cultivo y al tipo de modelado —«observed», «regression» o «yield», seguido del número de percentil (25, 50, 75 o 95)— y al sufijo proporcionado por el usuario. Estos rásteres representan la tasa de producción de ese cultivo en toneladas métricas por hectárea por año.

- **result_table_[Suffix].csv**: tabla que enumera todos los cultivos modelados en la ejecución, la superficie cubierta, la producción por percentil o modelada, la producción observada y la información nutricional de cada cultivo. Es el principal resultado del modelo.

También hay una carpeta **intermediate_output** que contiene numerosos archivos correspondientes a las etapas intermedias de los cálculos de los resultados finales. Por lo general, no es necesario trabajar con estos archivos, pero pueden resultar útiles para depurar una ejecución del modelo o comprender mejor sus pasos intermedios. La carpeta también contiene un subdirectorio donde se almacenan metadatos utilizados internamente para evitar repetir cálculos.

Los resultados de **rendimiento observado** aproximan el rendimiento real de los cultivos en el área de interés alrededor del año 2000. Los resultados de **rendimiento por percentiles** y **rendimiento de regresión** son útiles si el cultivo no se produce actualmente en el área de interés o si se desea aproximar el potencial de aumento de la producción mediante la reducción de las brechas de rendimiento.


Referencias
===========

«Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000». C. Monfreda, N. Ramankutty, J. Foley. *Biogeochemical Cycles*, vol. 22, GB1022, doi:10.1029/2007GB002947. 2008.

«Closing yield gaps through nutrient and water management». N. Mueller, J. Gerber, M. Johnston, D. Ray, N. Ramankutty, J. Foley. *Nature*. 11 de octubre de 2012; 490(7419):254-257. doi: 10.1038/nature11420. Publicación electrónica: 29 de agosto de 2012.
