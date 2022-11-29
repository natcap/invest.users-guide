Modelo GLOBIO de InVEST
=======================

Resumen
-------

El modelo GLOBIO proporciona un índice de biodiversidad en función de la abundancia media de especies (AME o MSA), la respuesta media a nivel de población de un rango de especies, a diferentes factores de estrés, como el cambio de uso de la tierra, la fragmentación y las infraestructuras. El modelo puede utilizarse como una evaluación estática de lo lejos que está el medio ambiente actual de un estado prístinoo para estimar cómo un cambio en cualquiera de los factores de estrés conduciría a un estrés en la biodiversidad o en la integridad del ecosistema, como indica la AME.

Introducción
------------

La metodología GLOBIO fue desarrollada por el Programa de las Naciones Unidas para el Medio Ambiente (PNUMA, Alkemade et al. 2009) para modelizar el impacto humano en la biodiversidad, medido por la abundancia media de especies (AME). La abundancia media de especies es una mejora con respecto al enfoque más tradicional de la curva especie-área por dos razones. En primer lugar, ofrece estimaciones agregadas de las densidades de las especies, no solo de su presencia, lo que es importante para representar la verdadera diversidad, ya que la presencia por sí sola ofrece una información limitada sobre la viabilidad de la población (Balmford et al. 2012). En segundo lugar, relaciona más que la superficie del hábitat con los cambios en la biodiversidad al incluir información sobre el impacto de la fragmentación y las amenazas de las infraestructuras (y el cambio climático y la deposición de nitrógeno si se aplicara la versión completa de GLOBIO).

El modelo
---------

El método GLOBIO consiste en un conjunto de ecuaciones que relacionan los impulsores de impacto en la biodiversidad, tablas de parámetros para estimar las ecuaciones mencionadas, basadas en una amplia revisión de la literatura, y metodologías sugeridas para introducir y procesar los datos espaciales necesarios. Hemos ampliado la metodología de GLOBIO para reducir su enfoque global a un nivel de paisaje.

Cómo funciona
~~~~~~~~~~~~~

El enfoque de GLOBIO se basa en la abundancia media de especies (AME, véase Schwartz et al. 2003 para un ejemplo de uso de la AME). Una estimación de la AME oscila entre 0 y 1, indicando el cambio proporcional medio en abundancia de especies individuales en un lugar frente a ese mismo lugar con una vegetación prístina. Una AME de 1,0 implica que por término medio la abundancia de las especies es la misma que en un terreno prístino, mientras que una MSA de 0,0 implica que la abundancia media de especies es cero. La comparación de los valores de AME de diferentes escenarios identifica cómo los cambios antropogénicos afectan la biodiversidad (por ejemplo, pasar de un escenario con una AME media de 0,6 a una de 0,5 implica que, en promedio, la abundancia de las especies individuales disminuyó un 16,6% debido al cambio de uso del suelo). En GLOBIO, se define un valor de AME para cada celda de la cuadrícula dentro de una extensión geoespacial.

Los factores de estrés disminuyen la AME de forma multiplicativa. En el documento GLOBIO3 los factores de estrés incluían el uso y la cobertura del suelo (LU), el exceso de deposición atmosférica de nitrógeno atmosférico (N), la proximidad de infraestructuras (principalmente carreteras; I) la fragmentación (F) y el cambio climático (CC), como en la siguiente ecuación para calcular la AME por píxel (i):

.. math:: \text{MS}A_{i} = MSA_{LU_{i}} \bullet MSA_{N_{i}} \bullet MSA_{I_{i}} \bullet MSA_{F_{i}} \bullet MSA_{CC_{i}}

Para considerar los cambios en el uso de la tierra, ignoramos el término de deposición de nitrógeno y los términos del cambio climático; como ninguno de estos términos cambia con cada cambio de suelo, se anularán cuando se calcule el porcentaje de cambio en la AME total (sumado).

Perfeccionamos la metodología de GLOBIO para el cambio de AME debido a la infraestructura, la fragmentación y el uso de la tierra para utilizar datos de mayor resolución (píxeles de 500 m de MODIS en lugar de los de 50 km utilizados por el PNUMA) necesarios para detectar la respuesta ecológica a escala más fina que podría incluir no-linealidades. La reducción de escala requiere nuevos métodos para asignar subclases de regímenes de gestión de la tierra con mayor precisión, basados en datos de alta resolución en lugar de agregados de todo el continente, y un enfoque más sofisticado para cuantificar la fragmentación que la aplicación de medias globales del tamaño de los parches para diferentes hábitats.

Cálculo del impacto de las infraestructuras en la AME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La tabla 1 proporciona los datos de Alkemade et al. (2009) para los valores de MSA de diferentes buffers alrededor de las infraestructuras que afectan a diferentes ecosistemas. El impacto de las infraestructuras en la AME viene determinado únicamente por la distancia, no por la naturaleza de la vegetación . Una zona de de cultivo que esté a 5 km de una carretera verá reducida su AME en un factor de 0,9, independientemente de que la zona entre las tierras de cultivo y la carretera sea bosque tropical o más tierras de cultivo. Todas las fuentes de infraestructura se agregan en una clase de uso de la tierra/cobertura del suelo "artificial". Las restantes clases de cobertura del suelo, que pueden considerarse vegetativas o "naturales" se dividen en tres tipos básicos: bosque tropical, bosque templado o boreal, y pastizales o tierras de cultivo. La distancia de estas diferentes clases de hábitat de la infraestructura se utiliza para calcular la zona de impacto para determinar la AME a partir de la infraestructura, utilizando la Tabla 1.

**Tabla 1: Efecto de las zonas de impacto de las infraestructuras en la AME, fuente:**
Alkemade et al. (2009)

=============== ================================================== =================================================== ======================================================= ========= ==================
**Zona de impacto** **Distancia del bosque tropical de la infraestructura (m)** **Distancia del bosque templado de la infraestructura (m)** **Distancia de los pastizales y las tierras de cultivo de la infraestructura (m)** **MSA_I** **Error estándar**
=============== ================================================== =================================================== ======================================================= ========= ==================
Impacto alto     <1000                                              <300                                                <500                                                    0,4       0,22
Impact medio   1000-4000                                          300-1200                                            500-2000                                                0,8       0,13
Impact bajo      4000-14,000                                        1200-4200                                           2000-7000                                               0,9       0,06
Sin impacto       >14.000                                            >4200                                               >7000                                                   1,0       0,02
=============== ================================================== =================================================== ======================================================= ========= ==================


Cálculo del impacto de la fragmentación en la AME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aumentamos el enfoque estándar de GLOBIO para el análisis de la fragmentación utilizando un índice de calidad de los bosques fragmentados (FFQI). El FFQI es similar a los métodos utilizados en la literatura forestal, y se calcula considerando cuántas de las celdas vecinas de un bosque están también arboladas. En lugar de identificar el impacto esperado de la AME a partir del tamaño del parche (como en GLOBIO), el FFQI estima el efecto relativo de la fragmentación con una función de suavización gaussiana. De este modo, se tratan los parches de hábitat que están separados por pequeñas parcelas de infraestructura o de no-hábitat como menos fragmentados que los parches de hábitat separados por distancias más amplias. Convertimos los valores de FFQI de nuestro mapa en km\ :sup:`2` para que coincidan con las zonas definidas en la Tabla 2 (según Alkemade 2009) tomando la raíz cuadrada del área para convertirla en la anchura/altura del parche. Aunque el método es diferente de cómo el PNUMA definió los parches, las comparaciones con la literatura mostraron que el FFQI es una aproximación precisa del enfoque más engorroso basado en los parches.

**Tabla 2: Efecto de la fragmentación en la AME en función del tamaño de los parches, fuente:** Alkemade et al. (2009)

=========== =============== ========= ==================
**FFQI**    **Área (km^2)** **MSA_F** **Error estándar**
=========== =============== ========= ==================
< 0,43      < 1             0,3       0,15
0,43 – 0,58 <10             0,6       0,19
0,58 – 0,90 <100            0,7       0,19
0,90 – 0,98 <1.000          0,9       0,20
0,98 – 0,99 <10.000         0,95      0,20
0,99 – 1    >10.000         1,0       0,20
=========== =============== ========= ==================

Cálculo del impacto de la AME por el cambio de uso del suelo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El aspecto más difícil de aplicar de GLOBIO es la asignación de diferentes categorías de uso y cobertura del suelo relacionadas con la intensidad de la gestión o del uso humano, ya que esta información suele estar ausente en los conjuntos de datos obtenidos por teledetección de datos globales sobre la cobertura del suelo. Para ayudar a esta clasificación, hemos desarrollado reglas sencillas para reclasificar los mapas de uso y cobertura del suelo de MODIS u otros mapas de uso y cobertura del suelo en las categorías de gestión para las que la AME cuantificada por las amplias revisiones bibliográficas de GLOBIO. La Tabla 3 presenta la categorización basada en reglas utilizada para convertir los datos MODIS en clases compatibles con GLOBIO. Los tipos de LULC que se asignan a más de un tipo GLOBIO se dividen en función de otros conjuntos de datos auxiliares que se describen a continuación.

Bosques:
''''''''

Para distinguir entre bosque primario y otros bosques, incluyendo bosques secundarios (replantados) o bosques con algún uso extractivo y de plantación, analizamos la fragmentación de la cubierta forestal mediante el FFQI y asignamos diferentes categorías de uso basadas en el FFQI, con bosque primario por encima de un determinado umbral definido por quien nusa. Este enfoque supone que es más probable que bosques prístinos se encuentren en extensiones de bosque grandes y no fragmentadas, y que los bosques secundarios o poco utilizados se encuentren en las zonas boscosas más fragmentadas. El umbral puede calibrarse de forma que la cantidad total de bosques primarios y secundarios o de uso ligero coincida con las estimaciones a escala nacional o continental (documentado en Alkemade et al. 2009).

Matorrales y pastizales:
''''''''''''''''''''''''

Para distinguir entre praderas de vegetación primaria (más prístinas), pastizales pastoreados y pastos artificiales (zonas deforestadas utilizadas para pastos), comparamos el mapa de vegetación potencial generado por Ramankutty y Foley (1999) descrito anteriormente con la vegetación real determinada por los datos de la cubierta terrestre de MODIS. Si un píxel concreto se designa como bosque según el mapa de vegetación potencial, pero aparece como como pastizal en MODIS, es probable que se trate de un bosque que ha sido desbrozado para pastoreo; en este caso el píxel se reclasifica como "pasto artificial". Si un píxel es un pastizal según el mapa de vegetación potencial y aparece como pastizal en los datos MODIS, se utiliza un conjunto de datos separado, cuantificando el área de pasto proporcional a una resolución de ~10 km desarrollada por Ramankutty et al. (2008). Este píxel se define como "pastoreo de ganado" si la proporción de la celda de la cuadrícula en los pastos es mayor que un umbral definido por quien usa. El umbral puede elegirse de forma que los totales agregados del pastoreo de ganado coincidan con los datos nacionales y provinciales, como se ha descrito anteriormente para los bosques. Si el píxel de pasto es inferior al umbral de pastoreo, se definirá como vegetación primaria.

Tierras de cultivo:
'''''''''''''''''''

Como la intensificación de las tierras de cultivo solo se calcula en el MSA\ :sub:`LU` y no afecta a la configuración del hábitat primario y, por tanto, a la fragmentación calculada para la MSA\ :sub:`F`, no es necesario definir la ubicación espacial de la intensificación. Usted solo necesita designar la proporción de agricultura en el paisaje que está intensificada (es decir, que no se trata de agricultura de bajos insumos). Esto se puede encontrar en los conjuntos de datos regionales citados por Alkemade et al. (2009) o disponibles a través de la FAO, o puede derivarse de un conjunto de datos desarrollado por Foley et al. (2011) que mapea las brechas de rendimiento para todos los principales cultivos básicos a nivel mundial a resolución de ~10 km. Esta metodología compara la producción agrícola en climas similares (basándose en las precipitaciones y los grados-día de crecimiento) y de los cultivos en diferentes regiones según los rendimientos máximos alcanzados para su clima particular. La diferencia entre el rendimiento real y el rendimiento máximo alcanzable se define como "brecha de rendimiento". La diferencia de rendimiento puede servir como sustituto de la (falta de) intensificación, y se pueden examinar los mapas de brecha de rendimiento de su región de interés para determinar qué proporción del paisaje se encuentra por debajo de un determinado nivel de brecha de rendimiento.

**Tabla 3: Conversión de clases de cobertura de MODIS a GLOBIO y AME afectada por uso de la tierra**

+-------------------------------------+------------------------------------+----------+---------+
|**Clase de uso/cobertura del suelo MODIS**  |**¿Convertir a qué clases de GLOBIO?**|**MSA_LU**|**EE**   |
+=====================================+====================================+==========+=========+
| - 0 - Agua                         |N/A                                 |          |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 1 - Bosque perenne de hojas aciculares   | - 1 - Vegetación primaria\ :sup:`a` | - 1      |  - <0,01|
| - 2 - Bosque siempre verde latifoliado     | - 3 - Vegetación secundaria\ :sup:`a`   | - 0,5    |  - 0,03 |
| - 3 - Bosque deciduo de hojas aciculares   |                                    | - 0,2    |  - 0,04 |
| - 4 - Bosque deciduo latifoliado    |                                    |          |         |
| - 5 - Bosque mixto                  |                                    |          |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 6 - Matorrales cerrados/cerrado     | - 1 - Vegetación primaria\ :sup:`b` | - 1      | - <0,01 |
| - 7 - Matorrales abiertos               | - 5 - Pastoreo de ganado\ :sup:`c`  | - 0,7    | - 0,05  |
| - 8 - Sabanas leñosas                | - 6 - Pastos artificiales\ :sup:`b`  | - 0,1    | - 0,07  |
| - 9 - Sabanas                      |                                    |          |         |
| - 10 - Pastizales                   |                                    |          |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 12 - Tierras de cultivo/Perennes        | - 12 - Toda agricultura             | - 0,3    | - 0,12  |
|                                     |                                    | - 0,1    | - 0,08  |
+-------------------------------------+------------------------------------+----------+---------+
| - 13 - Urbano y construido           | - 10 - Zonas construidas              | - 0,05   |         |
+-------------------------------------+------------------------------------+----------+---------+
| - 16 - Estéril o con poca vegetación | - 1 - Vegetación primaria           | - 1,0    | - <0,01 |
+-------------------------------------+------------------------------------+----------+---------+

*División basada en (a)FFQ (descrita en la sección Fragmentación, arriba), (b) mapa de vegetación potencial (Foley et al. 2009), (c) superficie de pastos proporcional (Ramunkutty et al. 2009). En esta estructura de clasificación faltan las clases GLOBIO "Bosque natural poco utilizado" (clase GLOBIO 2), "bosque plantado" (clase GLOBIO 4), y "agroforestería" (clase GLOBIO 7), "Agricultura de bajos insumos" (clase 8 de GLOBIO) y "agricultura intensiva" (clase 9 de GLOBIO). Las clases de agricultura se dividen en un cálculo espacial de AME_LU según el valor de "Fracción de intensificación" establecida por quien usa.*

Limitaciones y simplificaciones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AME  es una estimación agregada, por lo que es imposible rastrear os efectos de la composición, y hay muchas posibilidades de composición ara la misma AME. Wi bien AME limita la abundancia relativa de species individuales en 1, asegurando que un aumento local de una especie o pueda encubrir un descenso de la abundancia general de las especies, una AME de 0,5 podría significar que todas las especies son la mitad de abundantes que en un estado prístino, o que una especie ha sufrido un inmenso declive mientras el resto se ha mantenido constante o en cualquier punto intermedio. Información adicional sobre la forma de la distribución de la abundancia de las especies y las probabilidades de extinción de las especies y las probabilidades de extinción relacionadas con los distintos niveles de AME podría mejorar la utilidad de este índice. Pero incluso así, la diversidad es más compleja que el número de especies y poblaciones. Algunos biólogos conservacionistas sostienen que la composición de las especies es tan importante como cualquier otra medida de diversidad, y el seguimiento de especies concretas es esencial para estimar los impactos sobre las especies amenazadas o en peligro de extinción o de las especies de valor cultural (Phalan et al. 2011 Food Policy). Para lograr este nivel de especificidad, los impactos de las diferentes estrategias de uso de la tierra tendrían que evaluarse para cada especie individualmente y luego combinarse para obtener resultados resumidos, lo que puede ser imposible en muchas regiones del mundo con escasa disponibilidad de datos y alta presión de la agricultura y otras presiones de desarrollo. En estos casos, la AME proporciona un índice de cambio de la biodiversidad rápido y fácil de utilizar en contextos de decisión.

En nuestra aplicación de GLOBIO, utilizamos los valores medios de los parámetros y sus errores estándar para estimar los impactos de la infraestructura, el uso del suelo y la fragmentación en nuevas ubicaciones, lo que supone que estos valores representan una muestra aleatoria de especies y ubicaciones geográficas. Sin embargo, la limitada disponibilidad de datos para ciertos grupos taxonómicos y regiones geográficas significa que hay sesgos potenciales en las estimaciones de los parámetros que añaden un grado de incertidumbre no cuantificable a las predicciones basadas en nuestra aplicación de GLOBIO.

Las estimaciones del impacto de las infraestructuras se basan en un meta-análisis de ~75 estudios, predominantemente de poblaciones de aves y mamíferos en Europa y Norteamérica, con alguna información sobre insectos y plantas (Alkemade et al. 2009; Benítez-López et al. 2010). Se desconoce si los impactos de las infraestructuras son similares para otros grupos taxonómicos o zonas geográficas.

Las estimaciones de los impactos del uso del suelo se basan en un número ligeramente mayor número de estudios, con 89 identificados en la publicación inicial de GLOBIO (Alkemade et al. 2009) y 195 identificados en un meta-análisis
(de Baan et al. 2013). La estimación del parámetro para todas las superficies artificiales/áreas construidas se basó en la opinión de expertos representando ciudades densamente pobladas, y sin cuantificación de incertidumbre (Alkemade et al. 2009). Los conjuntos de datos proceden en su mayoría de regiones tropicales, con menos de las regiones templadas y ninguna de las zonas boreales (de Baan et al. 2013). Se disponía de datos para 9 de los 14 biomas, y para muchos biomas la información solo estaba disponible para algunos tipos de uso de la tierra. Por ejemplo, la información sobre cultivos permanentes, agrosilvicultura y zonas artificiales solo estaba disponible en dos biomas. En tres biomas, solo se disponía de información sobre para los pastos, pero no para otros tipos de uso de la tierra. Como es habitual, los datos también estaban sesgados taxonómicamente hacia las especies de vertebrados y plantas (de Baan et al. 2013). Los artrópodos estaban infrarrepresentados, y las bacterias y los hongos no se incluyeron en absoluto en la base de datos.

Además, nuestra asignación de la cobertura del suelo por satélite (por ejemplo, bosque o pastizales) a las diferentes clases de uso del suelo de GLOBIO (por ejemplo, bosque primario frente a bosque secundario o pradera prístina vs. pradera pastada) introduce un error adicional que no se incorpora al análisis. Aunque podemos garantizar que nuestras asignaciones se suman a las estadísticas a nivel nacional o regional regional, no podemos verificar nuestro sistema de clasificación para cuantificar el nivel de precisión o incertidumbre.

Los impactos de la fragmentación en la abundancia media de especies (AME) se basan en seis conjuntos de datos de 3 publicaciones. La proporción de especies con una población viable se utilizó como sustituto de la AME (Alkemade et al. 2009), y no está claro el grado de incertidumbre adicional en los parámetros que esto añade. Los sesgos taxonómicos y geográficos son de nuevo una limitación. Dos estudios de estudios se centran exclusivamente en los mamíferos, incluyendo ~30 especies de mamíferos en Florida (Allen et al. 2001) y 10 especies de carnívoros de todo el mundo (Woodroffe y Ginsberg 1998). El tercer estudio se limita exclusivamente a Europa, y la mitad de las 202 especies incluidas son aves (Bouwma et al. 2002).

Necesidades de datos
--------------------

**NOTA: Todos los datos espaciales deben proyectarse en metros (es decir, una proyección local, no global o lat-long), para asegurar una distancia precisa a los cálculos de la infraestructura. El modelo no se ejecutará sin una proyección definida.**

- :investspec:`globio msa_parameters_path` El ejemplo siguiente (incluido en los datos de muestra) puede utilizarse tal cual. Ofrece los valores medios y los errores estándar proporcionados en Alkemade et al. (2009). Las personas con conocimientos avanzados pueden alterar esta tabla para poner las estimaciones altas y bajas de los intervalos de confianza en la columna msa_x, para ayudar en la evaluación de la incertidumbre.

   Columnas:

   - :investspec:`globio msa_parameters_path.columns.msa_type`
   - :investspec:`globio msa_parameters_path.columns.value`
   - :investspec:`globio msa_parameters_path.columns.msa_x`

   **Ejemplo:** Este ejemplo contiene dos columnas adicionales, *Medida* y *EE*, que no son utilizadas por el modelo. *EE* es el error estándar asociado a cada valor de AME, según el meta-análisis de Alkemade et al. (2009). Estos valores se registran aquí en este conjunto de datos de muestra para que usted pueda ajustar los valores de AME_x según el intervalo de confianza. *Medición* describe la métrica con la que se mide el valor de la columna siguiente.

   .. csv-table::
      :file: ../invest-sample-data/globio/msa_parameters.csv
      :header-rows: 1
      :widths: auto


- :investspec:`globio infrastructure_dir`

   .. nota::
      A diferencia de otros inputs espaciales de InVEST, solo se admiten formatos de archivo específicos en el directorio de infraestructuras. Los archivos de infraestructura ráster deben estar en formato GeoTIFF que termina en .tif. Los archivos de infraestructura vectorial deben estar en formato ESRI Shapefile que termina en .shp. En una futura versión de InVEST, es posible que se permitan otros formatos de archivo.

- :investspec:`globio aoi_path`

- :investspec:`globio intensification_fraction` Se utiliza en el cálculo de AME\ :sub:`LU`. El resto se considera agricultura de bajos insumos.

- :investspec:`globio predefined_globio`

Hay dos opciones para los inputs de LULC:

  a. Cubierta específica para la vegetación  (no específica para la gestión). Este es
      el tipo de cobertura del suelo que se puede adquirir a partir de MODIS u otras fuentes de datos de
      teledetección. Distingue entre bosque,pastizales, sabanas, tierras de cultivo y otros tipos de  
      vegetación. NO distingue entre las diferencias de gestión definidas por GLOBIO, como la vegetación 
      primaria frente a la secundaria, o los pastizales frente a los pastos. Si se elige esta opción, varios 
      conjuntos de datos de ayuda (enumerados como los requeridos para la opción 1a, más abajo) serán 
      necesarios.

   b. La cobertura del suelo específica de la gestión, siguiendo el esquema de clasificación establecida por
      GLOBIO (véase el cuadro 3, más arriba). Si se elige esta opción opción, marque la casilla de "Mapa de 
      uso del suelo predefinido para GLOBIO" e introduzca allí el mapa. Todos los demás inputs de datos se 
      volverán grises excepto el otro conjunto de datos necesarios, el directorio, y el input opcional del 
      ADI.

Si selecciona la opción de utilizar GLOBIO LULC predefinido, solo tendrá que proporcionar el mapa GLOBIO LULC:

- :investspec:`globio globio_lulc_path`

Si utiliza un mapa LULC personalizado, debe proporcionar varios inputs adicionales:

- :investspec:`globio lulc_path`

- :investspec:`globio lulc_to_globio_table_path`

  Columnas:

  - :investspec:`globio lulc_to_globio_table_path.columns.lucode`
  - :investspec:`globio lulc_to_globio_table_path.columns.globio_lucode`

  *Ejemplo*: A la izquierda están los datos de cobertura del suelo de MODIS, utilizando la clasificación de la UMD, tal y como se define en la Tabla 3. A la derecha, la traducción de la cobertura del suelo de GLOBIO, que agrupa las clases de bosque (1-5 en MODIS) en 130, los pastizales/matorrales (6-10 en MODIS) en 131, y la agricultura (12 en MODIS) en 132. El uso de la tierra urbana (13 en MODIS) se mapea directamente sobre las tierras construidas (10 en GLOBIO). Los terrenos estériles o con poca vegetación (16 en MODIS) pueden tratarse como vegetación primaria (1 en GLOBIO). Los conjuntos de datos subsiguientes y/o sus propias aportaciones ayudarán a determinar cómo dividir los 130, 131 y 132 en vegetación primaria y secundaria, pastizales y pastos, y agricultura intensificada y no intensificada, respectivamente.

  .. csv-table::
     :file: ../invest-sample-data/globio/lulc_conversion_table.csv
     :header-rows: 1
     :widths: auto

- :investspec:`globio pasture_path` Se trata de la superficie de pastos proporcional desarrollada por Ramankutty et al. (2008). Véase la explicación en *Matorrales y pastizales* en *Cómo funciona*, más arriba.

- :investspec:`globio potential_vegetation_path` Se recomienda utilizar el mapa de vegetación potencial generado por Ramankutty y Foley (1999). Si desea utilizar sus propios datos de vegetación potencial, los códigos de clasificación de la vegetación potencial deben coincidir con los de Ramankutty y Foley. Véase la explicación en *Matorrales y pastizales* en *Cómo funciona*, más arriba.

- :investspec:`globio primary_threshold` Este valor puede ajustarse de manera que el uso del suelo agregado coincida con las estadísticas regionales.

- :investspec:`globio pasture_threshold` Este valor puede ajustarse de manera que el uso del suelo agregado coincida con las estadísticas regionales.

Interpretación de los resultados
--------------------------------

Resultados finales
~~~~~~~~~~~~~~~~~~

- **globio-log**: Cada vez que se ejecuta el modelo, un archivo de texto (.txt)
      aparecerá en la carpeta *Output*. El archivo enumerará los valores de los parámetros
      para esa ejecución y se nombrará de acuerdo con el servicio,
      la fecha y la hora, y el sufijo.

- **aoi_summary_<suffix>**: Un shapefile que resume el promedio de AME para
      cada zona definida en el área de interés.

- **msa_<suffix>.tif**: Un ráster del valor global de la AME (abundancia media de las especies)
      , definida como "la abundancia media de las especies 
      originalmente presentes en relación con su abundancia en el
      estado prístino o maduro como base". Este índice está en una escala
      de 0 a 1, siendo 1 el estado prístino, calculado como el
      producto de los índices MSA\ :sub:`LU`, MSA\ :sub:`F`, y MSA\ :sub:`I`
      que se muestran a continuación.

- **msa_lu_<suffix>.tif**: Un ráster de AME calculado para los impactos de
      del uso de la tierra solamente.

- **msa_f_<suffix>.tif**: Un ráster de MSA calculado para los impactos de
      fragmentación solamente

- **msa_i_<suffix>.tif**: Un ráster de MSA calculado para los impactos de
      de las infraestructuras solamente

Resultados intermedios
~~~~~~~~~~~~~~~~~~~~~~

- **distance_to_infrastructure_<suffix>.tif**: Un mapa que codifica cada píxel por
      su distancia a la infraestructura más cercana, utilizada para calcular
      MSA\ I. La distancia en este ráster se mide como número de píxeles
      que se convierte en metros en el modelo utilizando la proyección
      definida.

- **globio_lulc_<suffix>.tif**: TEl mapa final de uso del suelo convertido a
      clasificación GLOBIO, como se indica en el cuadro 3. Si se desea, este
      mapa (o cualquier versión modificada de este mapa) podría utilizarse para ejecutar el
      modelo utilizando la opción 1b, arriba. Esto se utiliza para calcular MSA\ LU.

- **primary_veg_smooth_<suffix>.tif**: Un mapa filtro con Gauss("suavizado")
       de vegetación primaria (identificado en globio_lulc), utilizado para
       calcular MSA\ F.

- **tmp/ffqi_<suffix>.tif**: Un mapa del índice de calidad de fragmentación forestal
       (ffqi), utilizado para diferenciar entre bosque primario y 
       secundario en la clasificación de uso de suelo GLOBIO.

- **tmp/combined_infrastructure_<suffix>.tif**: Un mapa que une todos los
       archivos de infraestructura en el directorio de infraestructura (input 2
       arriba). Si solo hay un archivo en ese directorio, debe ser
       idéntico a ese archivo.

- **tmp/**: Otros archivos en este directorio representan pasos intermedios en
       los cálculos de los datos finales en la carpeta de resutados.

- **\_taskgraph_working_dir:** Este directorio almacena los metadatos utilizados
       internamente para permitir el recálculo evitado.

Referencias
-----------

Alkemade, Rob, Mark van Oorschot, Lera Miles, Christian Nellemann, Michel Bakkenes y Ben ten Brink. "GLOBIO3: a framework to investigate options for reducing global terrestrial biodiversity loss." *Ecosystems* 12, no. 3 (2009): 374-390.

Allen, C. R., Pearlstine, L. G., y Kitchens, W. M. (2001). Modeling viable mammal populations in gap analyses. Biological Conservation, 99(2), 135–144. doi:10.1016/S0006-3207(00)00084-7

Balmford A., R. Green, B. Phalan. 2012 What conservationists need to know about farming. Proc. R. Soc. B 279: 2714–2724.

Benítez-López, A., Alkemade, R. y Verweij, P. a. (2010). The impacts of roads and other infrastructure on mammal and bird populations: A meta-analysis. Biological Conservation, 143(6), 1307–1316. doi:10.1016/j.biocon.2010.02.009 

Bouwma, I. M., Jongman, R. H. G. y Butovsky, R. O. (2002). Indicative map of the Pan-European Ecological Network - technical background document. Tilburg, Países Bajos/Budapest, Hungría.

de Baan, L., Alkemade, R. y Koellner, T. (2013). Land use impacts on biodiversity in LCA: a global approach. International Journal of Life Cyce Assessment, 18, 1216–1230. doi:10.1007/s11367-012-0412-0

Foley , J.A. et al. 2005. Global consequences of land use. Science 305: 570-574.

Foley, J.A. et al. 2011. Solutions for a cultivated planet. Nature 478: 337-342.

Mueller, N. et al. 2012. Closing yield gaps through nutrient and water management. Nature 490: 254-257.

Phalan, B., A. Balmford, R.E. Green, J.P.W. Scharlemann. 2011. Minimising the harm to biodiversity of producing more food globally. Food Policy 36: S62-S71.

Ramankutty, N. y J.A. Foley. 1999. Estimating Historical Changes in Global Land Cover: Croplands from 1700 to 1992, Global Biogeochemical Cycles, 13 (4), 997-1027

Ramankutty, N. et al. 2008. Farming the planet: 1. Geographic distribution of global agricultural lands in the year 2000. Global Biogeochemical Cycles, Vol. 22, GB1003

Woodroffe, R. y Ginsberg, J. R. (1998). Edge Effects and the Extinction of Populations Inside Protected Areas. Science, 280(5372), 2126–2128. doi:10.1126/science.280.5372.2126
