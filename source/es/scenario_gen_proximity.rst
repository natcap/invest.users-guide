Generador de escenarios basado en la proximidad
===============================================

Resumen
-------

El generador de escenarios basado en la proximidad crea un conjunto de mapas contrastantes de cambios en el uso del suelo que convierten el hábitat siguiendo distintos patrones espaciales. El usuario determina qué hábitat puede convertirse, en qué se convertirá y qué tipo de patrón se utilizará, en función de la proximidad al borde de un hábitat focal. De esta manera, se puede generar una variedad de patrones de cambio en el uso del suelo, entre ellos el avance de los pastizales hacia el bosque desde su borde, la expansión de la agricultura desde las áreas actualmente cultivadas, la fragmentación del bosque y muchos otros. Los mapas de uso del suelo resultantes pueden utilizarse como datos de entrada para los modelos de InVEST u otros modelos de biodiversidad o servicios ecosistémicos que respondan a los cambios en el uso del suelo.

Introducción
------------

Para comprender los cambios en la biodiversidad y los servicios ecosistémicos (BSE) que resultan de los cambios en el uso del suelo, suele ser útil partir de un escenario o de un conjunto de escenarios que representen distintos tipos de cambio. Dado que muchas de las relaciones entre los paisajes y la BSE son espacialmente explícitas, un patrón diferente de conversión del hábitat, aun cuando se convierta la misma superficie total, puede producir efectos muy distintos sobre la BSE. Este generador de escenarios basado en la proximidad crea distintos patrones de conversión a partir de los datos de entrada del usuario, que definen el hábitat focal y el hábitat que se convertirá. Se diferencia del generador de escenarios de InVEST basado en reglas, aunque puede complementarlo: este último crea mapas de cambios en el uso del suelo según las probabilidades asignadas por el usuario a determinadas transiciones. Por tanto, el propósito del generador de escenarios de InVEST basado en la proximidad no es pronosticar patrones reales de expansión, sino desarrollar distintos patrones de cambio en el uso del suelo para examinar la relación entre dichos cambios y la BSE, así como la manera en que esa relación puede variar según los supuestos sobre el cambio de uso del suelo.

El modelo
---------

La herramienta puede generar dos escenarios simultáneamente (el más cercano al borde y el más alejado del borde de un hábitat focal) para convertir una superficie determinada a un tipo particular de hábitat. Para convertir a distintos tipos de hábitat, modificar las superficies de hábitat o definir otros hábitats focales o hábitats que se convertirán, la herramienta puede ejecutarse varias veces de manera secuencial.

Cómo funciona
~~~~~~~~~~~~~

Deben definirse tres tipos de cobertura del suelo: 1) La *cobertura focal* es la cobertura (o las coberturas) que establece las reglas de proximidad a partir de las cuales se determinarán los escenarios. El generador de escenarios convertirá el hábitat desde el borde o hacia el borde de los parches de estos tipos de cobertura del suelo. Esto no significa que se convertirán estas coberturas; únicamente se medirá la distancia hacia sus bordes o desde ellos para determinar dónde tendrá lugar la conversión. 2) La *cobertura convertible* es la cobertura (o las coberturas) que puede convertirse. Puede ser la misma que la cobertura focal, un subconjunto de ella o una cobertura completamente diferente. 3) La *cobertura de reemplazo* es el tipo de cobertura del suelo al que se convertirán las coberturas convertibles. En cada ejecución del modelo solo puede especificarse un tipo de cobertura de reemplazo.

A continuación, se pueden ejecutar dos escenarios simultáneamente: 1) *Más cercano al borde* significa que los tipos de cobertura convertible más próximos a los bordes de las coberturas focales se convertirán en la cobertura de reemplazo. 2) *Más alejado del borde* significa que los tipos de cobertura convertible más distantes de los bordes de las coberturas focales se convertirán en la cobertura de reemplazo. Si se elige este escenario, el usuario puede especificar en cuántas etapas debe realizarse la conversión. Esto es importante si la cobertura focal es la misma que la cobertura convertible, porque la conversión de la cobertura focal creará nuevos bordes y, por consiguiente, afectará la distancia calculada desde el borde de esa cobertura. Si se desea, la conversión puede realizarse en varias etapas; en cada una se convierte la superficie más alejada del borde de la cobertura focal, lo que genera un patrón fragmentado.

A continuación se presentan algunos ejemplos de los tipos de escenarios que pueden generarse al modificar estos datos de entrada básicos, utilizando la cobertura del suelo incluida en los datos de muestra que acompañan al modelo. Esta cobertura proviene de MODIS y utiliza la clasificación de la UMD (Friedl et al. 2011), que sigue el siguiente esquema: 1 – Bosque de coníferas siempreverde; 2 – Bosque latifoliado siempreverde; 3 – Bosque de coníferas caducifolio; 4 – Bosque latifoliado caducifolio; 5 – Bosque mixto; 6 – Matorral cerrado; 7 – Matorral abierto; 8 – Sabana arbolada; 9 – Sabanas; 10 – Pastizales; 12 – Tierras de cultivo; 13 – Áreas urbanas y construidas; 16 – Suelo desnudo o con vegetación escasa.

**Expandir la agricultura desde el borde del bosque hacia el interior:**

códigos de cobertura focal: 1 2 3 4 5

códigos de cobertura convertible: 1 2 3 4 5

código de cobertura de reemplazo: 12

marcar "Convert Nearest to Edge"

número de etapas de conversión: 1

**Expandir la agricultura desde el núcleo del bosque hacia el exterior:**

códigos de cobertura focal: 1 2 3 4 5

códigos de cobertura convertible: 1 2 3 4 5

código de cobertura de reemplazo: 12

marcar "Convert Farthest From Edge"

número de etapas de conversión: 1

**Expandir la agricultura mediante la fragmentación del bosque:**

códigos de cobertura focal: 1 2 3 4 5

códigos de cobertura convertible: 1 2 3 4 5

código de cobertura de reemplazo: 12

marcar "Convert Farthest From Edge"

número de etapas de conversión: 10 (o tantas etapas como se desee; cuanto mayor sea el número de etapas, más fragmentado será el patrón y más tiempo tardará la simulación)

**Expandir los pastizales hacia el bosque, en las zonas más cercanas a las áreas agrícolas existentes:**

códigos de cobertura focal: 12

códigos de cobertura convertible: 1 2 3 4 5

código de cobertura de reemplazo: 10

marcar "Convert Nearest to Edge"

número de etapas de conversión: 1

Datos necesarios
----------------

Los únicos datos de entrada necesarios para ejecutar el generador de escenarios basado en la proximidad son un mapa base de uso/cobertura del suelo y los códigos de cobertura del suelo definidos por el usuario para ese mapa, que permitirán establecer cómo deben calcularse los escenarios.

- :investspec:`scenario_gen_proximity workspace_dir`

- :investspec:`scenario_gen_proximity results_suffix`

- :investspec:`scenario_gen_proximity base_lulc_path`

- :investspec:`scenario_gen_proximity aoi_path` Antes de generar los escenarios, el mapa se recortará a la extensión de este vector.

- :investspec:`scenario_gen_proximity area_to_convert` Se convertirán tantos píxeles como sea posible sin superar esta superficie.

- :investspec:`scenario_gen_proximity focal_landcover_codes`

- :investspec:`scenario_gen_proximity convertible_landcover_codes`

- :investspec:`scenario_gen_proximity replacement_lucode` Si hay varios tipos de uso/cobertura del suelo (LULC) que interesa convertir, esta herramienta debe ejecutarse de manera secuencial, seleccionando un tipo de conversión cada vez. Puede introducirse un código nuevo si se trata de un uso del suelo novedoso para la región o si se desea registrar el uso del suelo expandido por separado del uso histórico.

- :investspec:`scenario_gen_proximity convert_farthest_from_edge` Las coberturas convertibles y las coberturas de interés para el hábitat pueden ser las mismas, constituir un subconjunto unas de otras o ser diferentes. Si son las mismas, debe especificarse el número de etapas de conversión, porque la conversión del hábitat dentro de la cobertura focal creará nuevos bordes de hábitat. Esto dará lugar a un patrón de conversión completamente distinto según el número de etapas elegido.

- :investspec:`scenario_gen_proximity convert_nearest_to_edge` Las coberturas convertibles y las coberturas de interés para el hábitat pueden ser las mismas, constituir un subconjunto unas de otras o ser diferentes.

- :investspec:`scenario_gen_proximity n_fragmentation_steps` Introducir 1 significa que toda la conversión del hábitat tendrá lugar en el centro del parche del hábitat de interés. Introducir 10 dará lugar a una fragmentación según un patrón en el que se convertirán secuencialmente los píxeles más alejados del borde de ese hábitat, a lo largo del número de etapas especificado por el usuario.

Interpretación de los resultados
--------------------------------

Resultados finales
~~~~~~~~~~~~~~~~~~

- **InVEST….log…txt:** Cada vez que se ejecuta el modelo, aparece un archivo de texto (.txt) en la carpeta *Output*. El archivo contiene los valores de los parámetros de esa ejecución y su nombre se genera a partir del modelo, la fecha y la hora, y el sufijo.

- **nearest_to_edge_<suffix>.tif**: ráster de LULC correspondiente al escenario de conversión más cercana al borde del hábitat focal.

- **farthest_from_edge_<suffix>.tif**: ráster de LULC correspondiente al escenario de conversión más alejada del borde del hábitat focal.

- **nearest_to_edge_<suffix>.csv**: tabla que presenta la superficie (en hectáreas) y el número de píxeles de los distintos tipos de cobertura del suelo convertidos en el escenario de conversión más cercana al borde del hábitat focal. Los valores de la columna *original lucode* indican las coberturas del suelo convertidas por el modelo. La columna *replacement lucode* indica el tipo de cobertura del suelo al que se convirtió la cobertura original. Todos los valores de esta columna serán iguales, ya que en cada ejecución del modelo solo puede especificarse un código de cobertura de reemplazo.

- **farthest_from_edge_<suffix>.csv**: tabla que presenta la superficie (en hectáreas) y el número de píxeles de los distintos tipos de cobertura del suelo convertidos en el escenario de conversión más alejada del borde del hábitat focal. Los valores de la columna *original lucode* indican las coberturas del suelo convertidas por el modelo. La columna *replacement lucode* indica el tipo de cobertura del suelo al que se convirtió la cobertura original. Todos los valores de esta columna serán iguales, ya que en cada ejecución del modelo solo puede especificarse un código de cobertura de reemplazo.

Resultados intermedios
~~~~~~~~~~~~~~~~~~~~~~

- **{farthest_from_/nearest_to}_edge_distance_<suffix>.tif**: este ráster muestra la distancia (en número de píxeles) de cada píxel al borde más cercano de la cobertura focal del suelo.

- **_tmp_work_tokens:** este directorio almacena metadatos utilizados internamente para evitar volver a realizar cálculos.

Script de ejemplo
-----------------

El siguiente script muestra cómo pueden combinarse en un solo script los escenarios descritos en la sección «Cómo funciona», para ejecutarlos mediante la API de Python de InVEST::

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
