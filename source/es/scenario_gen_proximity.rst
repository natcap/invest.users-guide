Generador de escenarios: basado en la proximidad
================================================

Resumen
-------

El generador de escenarios basado en la proximidad crea un conjunto de mapas de cambio de uso que convierten el hábitat en diferentes patrones espaciales. Usted determina qué hábitats se pueden convertir y en cuáles son convertidos, así como el tipo de patrón, en función de la proximidad al borde de un hábitat focal. De esta manera, puede generarse una serie de patrones de cambio de uso de la tierra, incluidos los pastos que invaden el bosque desde el borde del bosque, la expansión de la agricultura desde las áreas actualmente cultivadas, la fragmentación de bosques y muchos otros. Los mapas de uso de la tierra resultantes pueden luego ser utilizados como inputs para los modelos InVEST u otros modelos para biodiversidad o servicios ecosistémicos que responden al cambio de uso de la tierra.

Introduction
------------

Para entender el cambio en la biodiversidad y los servicios ecosistémicos (BSE) como resultado del cambio en el uso de la tierra, a menudo es útil comenzar con un escenario o un conjunto de escenarios que exhiben diferentes tipos de cambio de uso de suelo. Ya que muchas de las relaciones entre paisajes y BSE son espacialmente explícitos, un patrón diferente de conversión de hábitat para la misma área total de hábitat convertido puede conducir impactos muy diferentes en BES. Este generador de escenarios basado en la proximidad crea diferentes patrones de conversión según sus inputs designando hábitat focal y hábitat convertido, en contraste con, pero potencialmente complementando, el generador de escenarios basado en reglas de InVEST que crea mapas de cambio de uso de la tierra de acuerdo con las probabilidades asignadas por usted de que ocurrirán ciertas transiciones. Por lo tanto, la intención de este generador de escenarios basado en proximidad no es para pronosticar patrones de expansión, sino más bien para desarrollar diferentes patrones de cambio de uso de la tierra para examinar la relación entre el cambio de uso de la tierra y BSE, y cómo la relación puede diferir dependiendo de las suposiciones acerca del uso de la tierra.

El modelo
---------

La herramienta puede generar dos escenarios a la vez (el más cercano al borde y el más alejado del borde de un hábitat focal), para una conversión a tipo de hábitat particular para un área determinada. Para convertir a diferentes tipos de hábitat, diferentes cantidades de hábitat, o para designar diferentes hábitats focales o hábitats convertidos, la herramienta se puede ejecutar varias veces en secuencia.

Cómo funciona
~~~~~~~~~~~~~

Se deben definir tres tipos de cobertura del suelo: 1) *Cobertura del suelo* *focal* es la(s) cobertura(s) terrestre(s) que establece(n) las reglas de proximidad a partir de las cuales se determinarán los escenarios. El generador de escenarios convertirá el hábitat desde el borde o hacia el borde de parches de este tipo de cobertura. Esto no
significa que convertirá estas cubiertas terrestres, solo que medirá distancia hacia o desde los bordes al designar dónde sucederá la conversión. 2) *Cobertura del suelo convertible* es la(s) cobertura(s) terrestre(s) que puede(n) ser convertidas. Podrían ser las mismas que la(s) cobertura(s) terrestre(s) focal(es), un subconjunto, o completamente diferentes. 3) *Cobertura del suelo de reemplazo* es el tipo de cobertura  al que se convertirán las coberturas convertibles. Solo puede haber un tipo de cobertura del suelo por ejecución del modelo.

Se pueden ejecutar dos escenarios a la vez: 1) *Más cercano al borde* significa que los  tipos de cobertura de suelo convertibles más cercanos a los bordes de las coberturas de suelo focales se convertirán en la cobertura de reemplazo. 2) *Más alejado del borde* significa que los tipos de cobertura convertibles más alejados de los bordes de la zona focal
se convertirán a la cobertura de reemplazo. Si este escenario es elegido, usted puede designar en cuántos pasos  debe ocurrir la conversión. Esto es relevante si la cobertura terrestre focal es  igual que la cobertura convertible porque la conversión de la cobertura focal creará nuevos bordes y, por lo tanto, afectará la distancia calculada a partir del borde de esa cobertura. Si lo desea, la conversión puede ocurrir en varios pasos, cada vez convirtiendo el más alejado del borde de la cobertura terrestre focal, causando un patrón fragmentario.

A continuación se muestran algunos ejemplos de los tipos de escenarios que se pueden generar manipulando estos inputs básicos, utilizando la cobertura terrestre en los datos de
muestra que se envían con este modelo. Esta cobertura terrestre es de MODIS, utilizando la Clasificación UMD (Friedl et al. 2011), que sigue el siguiente esquema: 1 – Bosque siempreverde de hojas aciculares; 2 – Bosque siempreverde latifoliado; 3 – Bosque caducifolio de hojas aciculares; 4 – Bosque caducifolio latifoliado; 5 - bosque mixto; 6 – Matorrales cerrados; 7 – Matorrales abiertos; 8 – Sabanas leñosas; 9 – Sabanas; 10 – Pastizales; 12 – Tierras de cultivo; 13 – Urbano y construido; 16 – Estéril o con escasa vegetación.

**Expansión de la agricultura desde el borde del bosque hacia adentro:**

códigos de cobertura del suelo focal: 1 2 3 4 5

códigos de cobertura del suelo convertible: 1 2 3 4 5

código de cobertura del suelo de reemplazo: 12

marque "Convertir más cercano al borde"

número de pasos hacia la conversión: 1

**Expandir la agricultura desde el núcleo del bosque hacia el exterior**:

códigos de cobertura del suelo focal: 1 2 3 4 5

códigos de cobertura del suelo convertible: 1 2 3 4 5

código de cobertura del suelo de reemplazo: 12

marque "Convertir más lejos del borde"

número de pasos hacia la conversión: 1

**Expandir la agricultura fragmentando el bosque:**

códigos de cobertura del suelo focal: 1 2 3 4 5

códigos de cobertura del suelo convertible: 1 2 3 4 5

código de cobertura del suelo de reemplazo: 12

marque "Convertir más lejos del borde"

número de pasos hacia la conversión: 10 (o tantos pasos como se desee; mientras más pasos, más finamente fragmentado será y más tiempo tomará la simulación)

**Expandir los pastos al bosque más cercano a la agricultura existente:**

códigos de cobertura del suelo focal: 12

códigos de cobertura del suelo convertible: 1 2 3 4 5

código de cobertura del suelo de reemplazo: 10

marque "Convertir más cercano al borde"

número de pasos hacia la conversión: 1


Necesidades de datos
--------------------

Los únicos datos de input necesarios para ejecutar el generador de escenarios basado en la proximidad es un mapa base de uso del suelo/cobertura del suelo y códigos de cobertura definidos por usted pertenecientes a este mapa base para designar cómo calcular los escenarios.

- :investspec:`scenario_gen_proximity workspace_dir`

- :investspec:`scenario_gen_proximity results_suffix`

- :investspec:`scenario_gen_proximity base_lulc_path`

- :investspec:`scenario_gen_proximity aoi_path` Antes de la generación del escenario, el mapa se recortará en la medida de este vector.

- :investspec:`scenario_gen_proximity area_to_convert` Se convertirán tantos píxeles como sea posible sin exceder esta área.

- :investspec:`scenario_gen_proximity focal_landcover_codes`

- :investspec:`scenario_gen_proximity convertible_landcover_codes`

- :investspec:`scenario_gen_proximity replacement_lucode` Si hay varios tipos de LULC que son de interés para la conversión, esta herramienta debe ejecutarse en secuencia, eligiendo un tipo de conversión cada vez. Se puede introducir un nuevo código si se trata de un uso de suelo novedoso para la región o si es deseable rastrear el uso de suelo ampliado como algo separado del uso de suelo histórico.

- :investspec:`scenario_gen_proximity convert_farthest_from_edge` Las coberturas convertibles y las coberturas del hábitat de interés pueden ser las mismas, o un subconjunto de ellas, o pueden ser diferentes. Si son iguales, se debe especificar el número de pasos para la conversión, porque la conversión del hábitat dentro de la cobertura focal creará un nuevo límite de hábitat, lo que resultará en un patrón de conversión completamente diferente dependiendo de cuántos pasos se elijan.

- :investspec:`scenario_gen_proximity convert_nearest_to_edge` Las coberturas terrestres convertibles y las coberturas terrestres del hábitat de interés pueden ser las mismas, o un subconjunto de ellas, o pueden ser diferentes.

- :investspec:`scenario_gen_proximity n_fragmentation_steps` Ingresar un 1 significa que toda la conversión de hábitat ocurrirá en el centro del parche del hábitat de interés. Al ingresar 10, se fragmentará de acuerdo con un patrón de conversión secuencial de los píxeles más alejados del borde de ese hábitat, en la cantidad de pasos especificados por usted.

Interpretación de los resultados
--------------------------------

Resultados finales
~~~~~~~~~~~~~~~~~~

- **InVEST….log…txt:** Cada vez que se ejecuta el modelo, aparecerá un archivo de texto (.txt) en la carpeta *Resultado*. El archivo enumerará los valores de los parámetros para esa ejecución y se nombrará de acuerdo con el modelo, la fecha y la hora, y el sufijo.

- **nearest_to_edge \_<suffix>.tif**: Ráster LULC para el escenario de conversión más cercano al borde del hábitat focal.

- **farthest_from_edge_<suffix>.tif**: Ráster LULC para el escenario de conversión más alejado del borde del hábitat focal.

- **nearest_to__edge_<suffix>.csv**: tabla que enumera el área (en hectáreas) y el número de píxeles para diferentes tipos de cobertura del suelo convertidos para el escenario de conversión más cercano al borde del hábitat focal.

- **farthest_from_edge \_<suffix>.csv**: tabla que enumera el área (en hectáreas) y el número de píxeles para diferentes tipos de cobertura del suelo convertidos para el escenario de conversión más cercano al borde del hábitat focal.

Resultados intermedios
~~~~~~~~~~~~~~~~~~~~~~

- **{farthest_from_/nearest_to}_edge_distance_<suffix>.tif**: Este ráster muestra la distancia (en número de píxeles) de cada píxel al borde más cercano de la cobertura focal.

- **_tmp_work_tokens:** Este directorio almacena metadatos que se utilizan internamente para evitar que se vuelvan a calcular.

Script de muestra
-----------------

El siguiente script se proporciona para demostrar cómo los escenarios
descrito en la sección "Cómo funciona" se puede componer en un solo script
que se puede llamar desde la API de Python de InVEST::

        import natcap.invest.scenario_generator_proximity_based

        edge_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': False,
            u'convert_nearest_to_edge': True,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'edge',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        core_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': True,
            u'convert_nearest_to_edge': False,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'core',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        frag_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': True,
            u'convert_nearest_to_edge': False,
            u'convertible_landcover_codes': u'1 2 3 4 5',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'10',
            u'replacement_lucode': u'12',
            u'results_suffix': 'frag',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }

        ag_args = {
            u'aoi_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_aoi.shp',
            u'area_to_convert': u'20000.0',
            u'base_lulc_path': u'C:/Users/Rich/Documents/svn_repos/invest-sample-data/scenario_proximity/scenario_proximity_lulc.tif',
            u'convert_farthest_from_edge': False,
            u'convert_nearest_to_edge': True,
            u'convertible_landcover_codes': u'12',
            u'focal_landcover_codes': u'1 2 3 4 5',
            u'n_fragmentation_steps': u'1',
            u'replacement_lucode': u'12',
            u'results_suffix': 'ag',
            u'workspace_dir': u'C:\\Users\\Rich/Documents/scenario_proximity_workspace',
        }
        if __name__ == '__main__':
            natcap.invest.scenario_generator_proximity_based.execute(edge_args)
            natcap.invest.scenario_generator_proximity_based.execute(core_args)
            natcap.invest.scenario_generator_proximity_based.execute(frag_args)
            natcap.invest.scenario_generator_proximity_based.execute(ag_args)
