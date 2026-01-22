.. _crop_production:

**********************
Producción de cultivos
**********************

Resumen
=======

Los modelos de percentil de producción de cultivos y de regresión de producción de cultivos estiman el rendimiento de los cultivos y el valor de los nutrientes para un conjunto fijo de cultivos, derivados de la información sobre la cubierta vegetal suministrada por usted. El rendimiento de los cultivos depende principalmente del clima y, si se dispone de las tasas de fertilizantes, también pueden tenerse en cuenta con el modelo de regresión.

Introducción
============

La ampliación de la producción agrícola y la reducción de las diferencias de rendimiento son una estrategia clave para muchos gobiernos y organismos de desarrollo centrados en la mitigación de la pobreza y la consecución de la seguridad alimentaria. Sin embargo, la conversión de los hábitats naturales a la producción agrícola afecta a otros servicios ecosistémicos que son clave para mantener los beneficios económicos que la agricultura proporciona a las comunidades locales. Las prácticas agrícolas intensivas pueden aumentar la carga de contaminación de las fuentes de agua, lo que a menudo hace necesarios costosos métodos de purificación del agua en el futuro. El uso excesivo del agua también amenaza el suministro disponible para la energía hidroeléctrica u otros servicios. Aun así, la producción de cultivos es esencial para el bienestar y el sustento de las personas. El modelo de producción de cultivos de InVEST permite un examen detallado de los costos y beneficios de esta empresa humana vital, incluyendo la exploración de cuestiones como:

+ ¿Cómo se compararía una disposición o selección diferente de los sistemas de cultivo con los sistemas actuales en términos de producción total? ¿Podría el cambio de cultivos producir un mayor rendimiento económico o valor nutricional?

+ ¿Cuáles son los efectos de la intensificación de los cultivos en los servicios ecosistémicos? Si se utiliza menos tierra para producir la misma cantidad de alimentos aumentando la intensificación?, ¿es positivo o negativo el resultado neto sobre la producción de servicios ecosistémicos?

+ ¿Cómo podemos evaluar diferentes estrategias para satisfacer la creciente demanda de alimentos minimizando el impacto en los servicios ecosistémicos?

El modelo
=========

El modelo de producción de cultivos de InVEST se divide en un modelo de rendimiento basado en el percentil, que abarca 172 cultivos en todo el mundo, y un modelo basado en la regresión que tiene en cuenta las tasas de fertilización en 10 cultivos. Estos modelos se presentan al final como modelos "percentil" y "regresión".

Todos los resultados se comparan con los resultados observados en la misma región para comprobar el control de calidad, así como la información nutricional de 33 macro y micronutrientes.

Modelo percentil
----------------

El modelo de percentiles de producción de cultivos de InVEST produce estimaciones del rendimiento de 172 cultivos a partir de datos existentes, resúmenes de percentiles y rendimientos observados. Estas observaciones se basan en conjuntos de datos de la FAO y subnacionales para 172 cultivos, como toneladas/ha (Monfreda et al. 2008) e información nutricional. Los rendimientos percentiles son útiles para explorar una gama de niveles de intensificación, enumerando el rendimiento para los percentiles 25, 50, 75 y 95, entre los datos de rendimiento observados en cada uno de los tramos climáticos del cultivo.

Modelo regresión
----------------

Para 10 cultivos básicos cuyos rendimientos han sido modelizados globalmente por Mueller et al. (2011), el modelo de Regresión de la Producción de Cultivos puede proporcionar estimaciones de los rendimientos dados los aportes de fertilizantes. Estos cultivos incluyen la cebada, el maíz, la palma aceitera, la patata, el arroz, la soya, la remolacha azucarera, la caña de azúcar, el girasol y el trigo. Para ejecutar este modelo, usted debe proporcionar una tabla adicional que corresponda a los cultivos con las tasas de aplicación de nitrógeno, fosfato y potasa (kg/ha) por cultivo. El modelo produce los rendimientos de los cultivos modelizados y observados, así como el valor nutricional.


Cómo funciona
-------------

Conjuntos de datos proporcionados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Los datos de muestra contienen un directorio **model_data** que contiene los conjuntos de datos globales de Monfreda en los que se basa el modelo:

- **climate_percentile_yield_tables** (modelo percentil): para cada cultivo, un CSV con la lista de los rendimientos de los percentiles 25, 50, 75 y 95 en cada casilla climática. Estos percentiles se obtienen a partir de los conjuntos de datos de rendimiento global observado y de la franja climática; por ejemplo, el valor del percentil 95 para el trigo en la franja climática 1 es de 3,763889. Esto significa que el 95% de las zonas que cultivan trigo en la zona climática 1 producen menos de 3,763889 toneladas/hectárea. El percentil 50 sería un rendimiento "medio", y el percentil 95 sería un rendimiento casi óptimo que se conseguiría mejorando las prácticas agrícolas.
- **climate_regression_yield_tables** (modelo de regresión): para cada cultivo, un CSV de los parámetros de regresión para cada casilla climática.
- **crop_nutrient.csv** (modelos de percentil y de regresión): una tabla con los valores nutricionales de cada cultivo.
- **crop_to_climate_bin.csv** (modelos de percentil y de regresión): A table that maps each crop name to the corresponding climate bin raster.
- **crop_to_observed_yield.csv** (modelos de percentil y de regresión): A table that maps each crop name to the corresponding observed yield raster.
- **crop_to_percentile_yield.csv** (modelo percentil): A table that maps each crop name to the corresponding percentile yield table.
- **crop_to_regression_yield.csv** (modelo percentil): A table that maps each crop name to the corresponding regression yield table.
- **extended_climate_bin_maps** (modelos de percentil y de regresión): para cada cultivo, un ráster global de casillas climáticas para ese cultivo (para más detalles, ver los Métodos Suplementarios de Mueller et al. 2012).
- **observed_yield** (modelos de percentil y de regresión): para cada cultivo, un ráster global del rendimiento real observado alrededor del año 2000.


Modelo percentiles
^^^^^^^^^^^^^^^^^^

El algoritmo del modelo percentiles es el siguiente, para cada tipo de cultivo (los resultados correspondientes están entre paréntesis):

1. Recorte el mapa global de casillas climáticas de **model_data/extended_climate_bin_maps/** a la extensión del mapa de la cubierta vegetal proporcionado por usted (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**)
2. Para cada percentil (25, 50, 75, 95):

   a. Reclasifique el mapa climático recortado de (1) utilizando los valores de **model_data/climate_percentile_yield_tables** para obtener un mapa de rendimientos por percentil (**intermediate_outputs/<crop>_yield_<percentile>_coarse_yield.tif**).
   b. Interpólela a la misma resolución que el mapa de la cobertura vegetal, cambiando los píxeles de 1/12 grados grandes por un gradiente más suave (**intermediate_outputs/<crop>_yield_<percentile>_interpolated_yield.tif**)
   c. Enmascare las zonas que no tienen ese cultivo según el mapa de la cubierta vegetal (**<crop>_yield_<percentile>_production.tif**).

3. Recorte el mapa de rendimiento global observado de **model_data/observed_yield/** a la extensión del mapa de la cubierta vegetal, y sustituya los valores de los píxeles nodata por cero (**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
4. Interpólela a la misma resolución que el mapa de la cobertura vegetal, cambiando los píxeles de 1/12 grados grandes por un gradiente más suave (**intermediate_outputs/<crop>_interpolated_observed_yield.tif**)
5. Enmascare las zonas que no tienen ese cultivo según el mapa de la cubierta vegetal (**<crop>_observed_production.tif**).
6. Sume los valores de rendimiento y los valores nutricionales (utilizando los datos de **model_data/crop_nutrient.csv**), y tabule los resultados (**result_table.csv**).
7. Si se proporcionó un vector de polígonos agregados, sume los valores dentro de cada área de polígono agregado y tabúlelos (**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).


Modelo regresión
^^^^^^^^^^^^^^^^

El algoritmo del modelo regresión es el siguiente, para cada tipo de cultivo (los resultados correspondientes figuran entre paréntesis):

1. Recorte el mapa global de casillas climáticas de **model_data/extended_climate_bin_maps/** a la extensión del mapa de la cobertura del suelo proporcionado por usted  (**intermediate_outputs/clipped_<crop>_climate_bin_map.tif**)
2. Para cada parámetro de regresión:

   a. Reclasifique el mapa climático recortado de (1) utilizando los valores de **model_data/climate_regression_yield_tables** para obtener un mapa de los valores de los parámetros de regresión (**intermediate_outputs/<crop>_<parameter>_coarse_regression_parameter.tif**)
   b. Interpólela a la misma resolución que el mapa de la cobertura del suelo, cambiando los píxeles de 1/12 grados grandes por un gradiente más suave (**intermediate_outputs/<crop>_<parameter>_interpolated_regression_parameter.tif**)

3. Para cada elemento fertilizante (nitrógeno, fósforo, potasio):

   a. Calcule un ráster de rendimiento de los cultivos basado en ese elemento utilizando los rásters de parámetros de regresión de (2) (**intermediate_outputs/<crop>_<element>_yield.tif**).

4. Calcule el rendimiento de los cultivos tomando el mínimo en píxeles de los tres rásters de rendimiento de (3) (**<crop>_regression_production.tif**).
5. Recorte el mapa de rendimiento global observado de **model_data/observed_yield/** a la extensión del mapa de la cubierta vegetal, y sustituir los valores de los píxeles nodata por cero (**intermediate_outputs/<crop>_clipped_observed_yield.tif**, **intermediate_outputs/<crop>_zeroed_observed_yield.tif**).
6. Interpólela a la misma resolución que el mapa de la cobertura del suelo, cambiando los píxeles de 1/12 grados grandes por un gradiente más suave (**intermediate_outputs/<crop>_interpolated_observed_yield.tif**)
7. Enmascare las zonas que no tienen ese cultivo según el mapa de la cobertura vegetal (**<crop>_observed_production.tif**).
8. Sume los valores de rendimiento y los valores nutricionales (utilizando los datos de **model_data/crop_nutrient.csv**), y tabule los resultados (**result_table.csv**).
9. Si se proporcionó un vector de polígonos agregados, sume los valores dentro de cada área de polígono agregado y tabúlelos (**intermediate_outputs/aggregate_vector.shp**, **aggregate_results.csv**).

 La regresión del cultivo en sí (pasos 3 y 4 anteriores) proviene de Mueller et al. 2012 y tiene la forma

 .. math:: Y_{mod_{GC}}=\min(Y_{max}(1-b_{NP}\exp(-c_N N_{GC})), Y_{max}(1-b_{NP} \exp(-c_P P_{GC})), Y_{max}(1-b_K \exp(-c_K K_{GC})))

Donde :math:`N_{GC}, P_{GC}, K_{GC}` son las tasas de fertilización suministradas por usted (N = nitrógeno, P = fósforo, K = potasio), y los demás parámetros de regresión se proporcionan como datos globales al modelo.

Limitaciones y simplificaciones
===============================

La versión actual del modelo es un modelo global grueso conducido principalmente por el clima y opcionalmente por la gestión. Por tanto, este modelo no es capaz de captar la variación de la productividad que se produce en paisajes heterogéneos. Una ladera rocosa y un valle fluvial fértil, si comparten el mismo clima, tendrían el mismo rendimiento en el modelo actual. Esto es un problema si la cuestión de interés es dónde priorizar la futura conversión del hábitat, o dónde la agricultura es más productiva y menos destructiva.

Necesidades de datos
====================

Hay dos modelos de producción de cultivos de InVEST disponibles, un modelo de observación basado en percentiles que opera en 172 cultivos, y un modelo de regresión para explorar las tasas de fertilización que opera en 10 cultivos. Los argumentos que se exponen a continuación se refieren a ambos modelos, a menos que se especifique lo contrario.

**Importante**: Es necesario descargar el conjunto de datos de InVEST para la producción de cultivos, para obtener el conjunto de datos de Monfreda necesario como input para los modelos. Si elige instalar los datos de muestra de Producción de Cultivos cuando instale InVEST, habrá una carpeta llamada ``sample_data\CropProduction`` en la carpeta de instalación de InVEST, donde pueden encontrarse estos datos. O bien, puede descargarlos de http://releases.naturalcapitalalliance.org/?prefix=invest/, después de ir a ese enlace, hacer clic en la versión de destino, luego navegar en el directorio ``data`` y seleccionar ``CropProduction.zip``.

Consulte también el conjunto de datos de producción de cultivos para ver ejemplos de todos estos inputs de datos. Esto le ayudará con el tipo de archivo, la estructura de la carpeta y el formato de la tabla. Tenga en cuenta que todos los inputs para el SIG deben estar en el mismo sistema de coordenadas proyectadas y en unidades de metros lineales.

Ambos modelos
-------------

- :investspec:`crop_production_percentile workspace_dir`

- :investspec:`crop_production_percentile results_suffix`

- :investspec:`crop_production_percentile climate_bin_raster_table`

- :investspec:`crop_production_percentile observed_yield_raster_table`

- :investspec:`crop_production_percentile crop_nutrient_table`

- :investspec:`crop_production_percentile landcover_raster_path` Este ráster debe tener un sistema de coordenadas proyectado con unidades de metros (por ejemplo, UTM) porque las áreas de los píxeles se dividen por 10000 para presentar algunos resultados en hectáreas. Solo puede haber una clase de uso/cobertura del suelo (LULC) asociada a cada tipo de cultivo único. Si tiene varias clases LULC que deben asignarse a un cultivo concreto, tendrá que combinar esas clases LULC múltiples en una sola clase en el ráster LULC antes de utilizarlas en el modelo.

- :investspec:`crop_production_percentile aggregate_polygon_path`

Necesidades adicionales de datos percentiles
--------------------------------------------

- :investspec:`crop_production_percentile percentile_yield_csv_table`

- :investspec:`crop_production_percentile landcover_to_crop_table_path` Solo puede haber una clase de cobertura del suelo asociada a cada tipo de cultivo único. Para más información, véase la descripción del uso del suelo/cobertura del suelo más arriba.

  Columnas:

  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_percentile landcover_to_crop_table_path.columns.crop_name`

  Ejemplo:

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/landcover_to_crop_table.csv
    :header-rows: 1
    :name: Example Landcover to Crop Table

Necesidades adicionales de datos de regresión
---------------------------------------------

- :investspec:`crop_production_regression regression_yield_csv_table`

- :investspec:`crop_production_regression landcover_to_crop_table_path`

  Columnas:

  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.lucode`
  - :investspec:`crop_production_regression landcover_to_crop_table_path.columns.crop_name`

- :investspec:`crop_production_regression fertilization_rate_table_path` A continuación se incluye una tabla de ejemplo derivada de los valores medios de las tasas de fertilización CBI observadas. Se pueden explorar los datos CBI en bruto en ``sample_data_\CropProduction\model_data\cbi_mod_yield_use_as_check``. (Véase la nota **Importante** anterior para obtener información sobre la obtención de estos datos).

  Columnas:

  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.crop_name`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.nitrogen_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.phosphorus_rate`
  - :investspec:`crop_production_regression fertilization_rate_table_path.columns.potassium_rate`

  **Ejemplo de tabla de fertilizantes:**

  .. csv-table::
    :file: ../../invest-sample-data/CropProduction/sample_user_data/crop_fertilization_rates.csv
    :header-rows: 1
    :name: Ejemplo de tasa de fertilización del cultivo. Los valores provienen de la mediana de la distribución observada de las tasas de fertilización CBI.


Interpretación de los resultados
================================

A continuación se describe brevemente cada uno de los resultados del modelo de producción de cultivos. Los resultados finales se encuentran en el espacio de trabajo definido por usted y especificado para esta ejecución del modelo. "Sufijo" en los siguientes nombres de archivos se refiere al Sufijo opcional definido por usted y que se introduce en el modelo.

- **aggregate_results_[Suffix].csv**: Si se proporciona un shapefile de polígono de resultados agregados, se produce una tabla que resume la producción total observada/percentil/modelizada y la información sobre nutrientes dentro de cada polígono.

- **Rásters de producción de cultivos**: Para cada cultivo modelizado, habrá un ráster (.tif) correspondiente a ese nombre de cultivo y al tipo de modelización - "observado", "regresión", o "rendimiento", más el número de percentil (25º/50º/75º/95º), y el sufijo proporcionado por usted. Estos rásters representan la tasa de producción de ese cultivo por píxel en toneladas métricas por píxel y por año.

- **result_table_[Suffix].csv**: Tabla en la que se enumeran todos los cultivos modelizados en la ejecución, la superficie cubierta, el percentil o la producción modelizada, la producción observada y la información sobre los nutrientes de cada cultivo. Es el principal resultado del modelo.

También hay una carpeta **intermediate_output**, que contiene muchos archivos que representan pasos intermedios en los cálculos de los resultados finales. Normalmente, no es necesario trabajar con estos archivos, pero pueden ser de interés si se está depurando una ejecución del modelo o se quieren entender mejor los pasos intermedios. También contiene un subdirectorio que almacena los metadatos que se utilizan internamente para poder evitar el recálculo.

Los resultados del **rendimiento observado** se aproximan al rendimiento real del cultivo en el área de interés, alrededor del año 2000. Los resultados del **rendimiento percentil** y del **rendimiento por regresión** son útiles si el cultivo no se cultiva actualmente en el área de interés, o para aproximar el potencial de aumento al cerrar las brechas de rendimiento.

Referencias
===========

"Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000."" C. Monfreda N. Ramankutty, J. Foley. Biogeochemical Cycles, Vol.22, GB1022, doi:10.1029/2007GB002947. 2008

"Closing yield gaps through nutrient and water management" N Mueller, J. Gerber, M. Johnston, D. Ray, N. Ramankutty, J. Foley. Nature. 2012 Oct 11;490(7419):254-7. doi: 10.1038/nature11420. Epub 2012 Aug 29.
