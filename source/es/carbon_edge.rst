Efecto de borde del carbono forestal
====================================

Resumen
-------

El modelo de efecto de borde del carbono de InVEST amplía el enfoque del modelo de carbono de InVEST para considerar la degradación de las reservas de carbono debida a la creación de bordes forestales. Aplica relaciones conocidas entre el almacenamiento de carbono y la distancia al borde del bosque para calcular los efectos de borde sobre el almacenamiento de carbono, y combina estas estimaciones con datos de inventarios de carbono para construir el mapa general de carbono. El modelo de efectos de borde se refiere únicamente al carbono sobre el suelo, porque no se han documentado efectos de borde para los demás depósitos de carbono (subterráneo, suelo y materia muerta). Para los demás depósitos de carbono, las clases de bosque no tropical y las ejecuciones del modelo sin efectos de borde, se sigue el enfoque de inventario del IPCC (2006) para asignar valores de almacenamiento de carbono por clase de cobertura del suelo.

Introducción
------------

Los efectos de los futuros cambios en el uso del suelo sobre el almacenamiento o el secuestro de carbono pueden modelarse aplicando estimaciones de almacenamiento de carbono encontradas en la literatura para distintos tipos de hábitat a cada hábitat presente en un paisaje (por ejemplo, Nelson et al. 2010). Sin embargo, este enfoque supone que todos los hábitats tienen la misma calidad de almacenamiento de carbono, independientemente de dónde se encuentren, a pesar de que existen numerosas evidencias de que la fragmentación puede desempeñar un papel decisivo en la modificación de las tasas de almacenamiento y secuestro de carbono en los bosques tropicales (Broadbent et al. 2008; Dantas et al. 2011; Laurance et al. 1997, 2000, 2001, 2002). Por ejemplo, se ha demostrado que los bosques interiores almacenan más de tres veces el carbono de los bosques de borde en los bosques atlánticos brasileños (Dantas et al. 2011). Chaplin-Kramer et al. (2015) investigaron este patrón en todos los trópicos mediante datos de biomasa obtenidos por sensores remotos (Baccini et al. 2012) y datos asociados de cobertura del suelo (Friedl et al. 2011), y encontraron una relación continua en la que el almacenamiento de carbono se degrada gradualmente hacia el borde del bosque, con variaciones sustanciales entre regiones. Este modelo considera estos efectos de borde documentados en los bosques tropicales y asigna el almacenamiento de carbono según la distancia de cada píxel al borde forestal más cercano. Esto puede mejorar en un 20 % la precisión general de las estimaciones de almacenamiento de carbono con respecto a los enfoques basados en inventarios forestales y representar mejor los impactos de la degradación forestal causada por la fragmentación, más allá de la mera superficie de hábitat perdida.

El modelo
---------

El modelo de efecto de borde del carbono de InVEST es una actualización del modelo de carbono de InVEST que incorpora la degradación del almacenamiento de carbono causada por los efectos de borde en los bosques tropicales. El usuario designa qué clases de cobertura del suelo corresponden a bosques y, a continuación, el modelo utiliza resultados de regresión generados previamente para predecir el carbono en toda una parcela forestal en función de su distancia al borde del bosque más cercano. Estos resultados se combinan con el carbono asignado a las clases no forestales mediante los métodos tradicionales de inventario (IPCC 2006) utilizados en el modelo de carbono de InVEST, para generar un mapa del almacenamiento de carbono sobre el suelo para todas las clases de cobertura del suelo. El modelo de efecto de borde del carbono de InVEST puede ejecutarse para calcular únicamente el carbono sobre el suelo o todos los depósitos de carbono, y con o sin efectos de borde. Es importante señalar que la regresión de los efectos de borde se refiere únicamente a las reservas de carbono sobre el suelo, porque los efectos de borde solo se han detectado en la biomasa aérea. Para incluir los otros tres depósitos de carbono (subterráneo, suelo y materia muerta en pie), debe incluirse la densidad de carbono (Mg/ha) de cada clase de cobertura del suelo en la tabla biofísica.

Tenga en cuenta también que los datos de regresión no abarcan toda la superficie terrestre. Puede ser útil comprobar si cubren su área de interés incorporando en un SIG la capa del modelo de regresión ``forest_carbon_edge_regression_model_parameters.shp`` (incluida en los datos de muestra de este modelo) y comparándola con su área de estudio. Si los datos de regresión no cubren su área de estudio, no podrá utilizar el modelo para calcular los efectos de borde.

Cómo funciona
~~~~~~~~~~~~~

Este modelo sigue la metodología descrita en Chaplin-Kramer et al. (2015), que construye una serie de modelos de regresión entre la densidad de biomasa forestal (Mg/ha) y la distancia al borde del bosque (km) para celdas de una cuadrícula de 100 km x 100 km distribuidas por todos los trópicos. En las celdas donde la mayoría de los píxeles correspondían a biomas forestales, se consideraron tres modelos de regresión candidatos para representar la relación entre la densidad de biomasa y la distancia al borde del bosque:

1. Asintótico: :math:`\mathrm{\text{Biomass}} = \theta_{1} - \theta_{2} \cdot \mathrm{\exp}( - \theta_{3} \cdot \mathrm{\text{Distance}})`

2. Logarítmico: :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot ln(\mathrm{\text{Distance}})`

3. Lineal: :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot \mathrm{\text{Distance}}`

Luego, para cada celda de la cuadrícula, se utiliza el modelo candidato con el valor de r\ :sup:`2` más alto para representar de la mejor manera la relación entre la densidad y la distancia al borde del bosque. Los modelos (2) y (3) se consideraron alternativas adecuadas y más sencillas en las celdas donde, por lo general, no se observaban distancias grandes y, por consiguiente, el núcleo del bosque no estaba claramente establecido. En la gran mayoría de las celdas, el modelo (1) fue el óptimo.

Los resultados de estas regresiones se encuentran en el shapefile de parámetros de regresión de borde de carbono (*core_data/forest_carbon_edge_regression_model_parameters.shp*) incluido en el conjunto de datos de muestra proporcionado para el modelo de efecto de borde del carbono de InVEST.

Para cada píxel forestal dentro de la región de estudio, el modelo calcula la distancia de ese píxel al borde del bosque y luego calcula la biomasa a partir de un número predefinido de los modelos de regresión más cercanos. Estos valores se agregan en un único resultado mediante un esquema de interpolación lineal basado en la distancia. A continuación, el modelo convierte la biomasa en carbono mediante un factor de conversión proporcionado por el usuario, cuyo valor predeterminado es 0.47 (IPCC 2006). El usuario puede definir el número de modelos locales utilizados en el esquema de interpolación. El valor predeterminado es 10, pero puede variar entre 1 (solo el punto más cercano) y 2313 (todos los modelos de regresión del planeta). Tenga en cuenta que solo se utilizarán los modelos de regresión situados a menos de 500 km del área de estudio, por lo que el número real de modelos promediados puede ser menor. La selección de 1 modelo puede producir diferencias artificialmente grandes de carbono entre píxeles contiguos que se encuentren en distintas celdas de la cuadrícula de regresión. Cuanto mayor sea el número de celdas de regresión seleccionadas, más gradual será la transición entre un píxel y el siguiente. El usuario puede optar por seleccionar el número de celdas de la cuadrícula que se superponen a toda el área de estudio para eliminar los artefactos derivados de la selección de modelos. Esto puede determinarse examinando la geometría de *intermediate_outputs/local_carbon_shape.shp* superpuesta al área de interés. El esquema de interpolación lineal para la biomasa b en el píxel p se expresa así:

.. math:: b_{p} = \frac{\sum_{i \in n}\frac{1}{d_{i}}{b_{i}^{'}}_{}}{\sum\frac{1}{d_{i}}}

Donde:

- :math:`b_{p}` es la biomasa interpolada en el píxel p.

- n es el número de modelos más cercanos a partir de los cuales se realiza la interpolación; este valor lo proporciona el usuario.

- i es el i\ :sup:`ésimo` modelo de biomasa más cercano al píxel p.

- :math:`d_{i}` es la distancia desde el píxel p hasta el centroide del i\ :sup:`ésimo` modelo de biomasa.

El carbono calculado para las clases no forestales sigue la metodología del modelo de carbono de InVEST, que asigna valores según los datos de inventario de carbono forestal especificados en la tabla biofísica. Los mapas de carbono generados mediante este enfoque de inventario y mediante el enfoque de efectos de borde se combinan en el mapa final de carbono, de modo que las coberturas forestales presentan efectos de borde y las demás coberturas no.

Limitaciones y simplificaciones
-------------------------------

Los datos sobre efectos de borde solo se proporcionan para las regiones tropicales. Para comprobar si se superponen con su área de estudio, incorpore en un SIG la capa de datos de muestra *core_data/forest_carbon_edge_regression_model_parameters.shp*. Si los datos de regresión no cubren su área de estudio, no podrá utilizar el modelo para calcular los efectos de borde.

Los datos sobre efectos de borde solo se proporcionan para el carbono sobre el suelo. Si desea incluir el carbono subterráneo, del suelo o de la materia muerta en los cálculos, puede proporcionar esos datos por clase de uso del suelo en la tabla de depósitos de carbono.

Los datos predeterminados sobre efectos de borde que se proporcionan con el modelo se generaron previamente y tienen una resolución de 100 km x 100 km. Si desea utilizar otros datos sobre efectos de borde o una resolución diferente, deberá crear esos datos fuera del modelo.

Datos necesarios
----------------
Tenga en cuenta que todos los datos espaciales de entrada deben utilizar el mismo sistema de coordenadas proyectadas y unidades lineales en metros.

- :investspec:`forest_carbon_edge_effect workspace_dir`

- :investspec:`forest_carbon_edge_effect results_suffix`

- :investspec:`forest_carbon_edge_effect lulc_raster_path`

- :investspec:`forest_carbon_edge_effect biophysical_table_path`

   Columnas:

   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.lucode`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.is_tropical_forest`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_above`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_below`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_soil`
   - :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_dead`

   **Ejemplo de tabla biofísica (datos de Brasil):**

   .. csv-table::
          :file: ./carbon_edge/forest_edge_carbon_lu_table.csv
          :header-rows: 1
          :widths: auto

   *Fuentes de los datos de c_above*:

   Matorrales cerrados, matorrales abiertos y pastizales: Miranda, Sabrina do Couto, et al. «Regional variations in biomass distribution in Brazilian savanna woodland». *Biotropica* 46.2 (2014): 125-138.

   Sabanas arboladas y sabanas: Saatchi, Susan S., et al. «Distribution of aboveground live biomass in the Amazon basin». *Global Change Biology* 13.4 (2007): 816-837.

   Tierras de cultivo: Fearnside, Philip M. «Greenhouse gases from deforestation in Brazilian Amazonia: net committed emissions». *Climatic Change* 35.3 (1997): 321-360.

- :investspec:`forest_carbon_edge_effect pools_to_calculate`

- :investspec:`forest_carbon_edge_effect compute_forest_edge_effects` Si se selecciona esta opción, el modelo utiliza el método de Chaplin-Kramer et al. para considerar las reservas de carbono sobre el suelo en los tipos de bosque tropical indicados con un «1» en el campo ``is_tropical_forest`` de la tabla biofísica.

- :investspec:`forest_carbon_edge_effect tropical_forest_edge_carbon_model_vector_path` Este dato de entrada se proporciona en los datos de muestra y no es necesario modificarlo, a menos que haya ejecutado una regresión independiente para su región y disponga de información mejor o más actualizada. El shapefile proporcionado se obtuvo de un análisis pantropical de la relación entre la biomasa forestal y la distancia al borde del bosque (Chaplin-Kramer et al. 2015).

   Tenga en cuenta que los datos de regresión no abarcan toda la superficie terrestre. Puede ser útil comprobar si cubren su área de interés incorporando en un SIG la capa del modelo de regresión *forest_carbon_edge_regression_model_parameters.shp* (incluida en los datos de muestra de este modelo) y comparándola con su área de estudio. Si los datos de regresión no cubren su área de estudio, no podrá utilizar el modelo para calcular los efectos de borde.

- :investspec:`forest_carbon_edge_effect n_nearest_model_points` El valor predeterminado es 10. Los valores más altos suavizan en mayor medida la variación del efecto de borde detectada en las distintas celdas de la cuadrícula (visible en el shapefile de parámetros de regresión de borde de carbono).

- :investspec:`forest_carbon_edge_effect biomass_to_carbon_conversion_factor` El valor predeterminado es 0.47 (según el IPCC 2006). Este factor se aplica únicamente a los parámetros de regresión de los efectos de borde; todos los valores de la tabla biofísica ya deben expresarse como carbono, no como biomasa.

- :investspec:`forest_carbon_edge_effect aoi_vector_path` Tenga en cuenta que los datos de regresión no abarcan toda la superficie terrestre. Puede ser útil comprobar si cubren su área de interés incorporando en el SIG la capa del modelo de regresión *forest_carbon_edge_regression_model_parameters.shp* (incluida en los datos de muestra de este modelo) y comparándola con su área de estudio. Si los datos de regresión no cubren su área de estudio, no podrá utilizar el modelo para calcular los efectos de borde.

Interpretación de los resultados
--------------------------------

.. note:: A partir de InVEST 3.15.0, los resultados ráster del modelo de Efecto de borde del carbono forestal se expresan como valores *por hectárea*.

Resultados finales
~~~~~~~~~~~~~~~~~~

- **Registro de parámetros**. Cada vez que se ejecuta el modelo, aparece un archivo de texto (.txt) en el *Espacio de trabajo*. El archivo enumera los valores de los parámetros utilizados en esa ejecución y su nombre se genera a partir del servicio, la fecha y la hora. Incluya el registro de parámetros cuando se comunique con NatCap para informar de errores en la ejecución del modelo.

- **carbon_map_[Suffix].tif**. Mapa de las reservas de carbono: la cantidad correspondiente al bosque se deriva de la regresión basada en la distancia al borde forestal, mientras que la cantidad de las clases no forestales se obtiene de la tabla biofísica. Las unidades son toneladas métricas por hectárea (t/ha).

- **aggregated_carbon_stocks_[Suffix].shp**: si el usuario proporciona áreas de interés para el servicio, este shapefile de salida resume el carbono total (columna *c_sum*) y el carbono medio por hectárea (columna *c_ha_mean*) en el área definida por los polígonos. Los valores se expresan en toneladas métricas (t).

Resultados intermedios
~~~~~~~~~~~~~~~~~~~~~~

- intermediate_outputs\\ **c_above_carbon_stocks_[Suffix].tif**.
      Carbono almacenado en el depósito de carbono de la biomasa sobre el suelo.

- intermediate_outputs\\ **c_below_carbon_stocks_[Suffix].tif**.
      Carbono almacenado en el depósito de carbono de la biomasa subterránea.

- intermediate_outputs\\ **c_dead_carbon_stocks_[Suffix].tif**. Carbono
      almacenado en el depósito de carbono de la materia muerta.

- intermediate_outputs\\ **c_soil_carbon_stocks_[Suffix].tif**. Carbono
      almacenado en el depósito de carbono del suelo.

- intermediate_outputs\\ **local_carbon_shape.shp**. Los parámetros de
      regresión reproyectados para coincidir con el área de estudio.

- intermediate_outputs\\ **edge_distance_[Suffix].tif**. La distancia
      de cada píxel forestal al borde del bosque más cercano.

- intermediate_outputs\\ **tropical_forest_edge_carbon_stocks_[Suffix].tif**.
      Mapa del carbono únicamente en el bosque, según el método de regresión.

Apéndice: fuentes de datos
--------------------------

:ref:`Uso/cobertura del suelo <lulc>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Depósitos de carbono <carbon_pools>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Referencias
-----------

Baccini, A., S. J. Goetz, W. S. Walker, N. T. Laporte, M. Sun, D. Sulla-Menashe, J. Hackler, P. S. A. Beck, R. Dubayah, M. A. Friedl, S. Samanta, y R. A. Houghton. 2012. «Estimated carbon dioxide emissions from tropical deforestation improved by carbon-density maps». *Nature Climate Change* 2:182–185.

Chaplin-Kramer, R., I. Ramler, R. Sharp, N. M. Haddad, J. S. Gerber, P. C. West, L. Mandle, P. Engstrom, A. Baccini, S. Sim, C. Mueller, y H. King. (2015). «Degradation in carbon stocks near tropical forest edges». *Nature Communications*.

Dantas de Paula, M., Alves-Costa, C., Tabarelli, M., 2011. «Carbon storage in a fragmented landscape of Atlantic forest: the role played by edge-affected habitats and emergent trees». *Tropical Conservation Science* 4, 349–358.

Friedl, M. A., D. Sulla-Menashe, B. Tan, A. Schneider, N. Ramankutty, A. Sibley, y X. Huang. 2010. «MODIS Collection 5 global land cover: Algorithm refinements and characterization of new datasets». *Remote Sensing of Environment* 114:168–182.

Panel Intergubernamental sobre Cambio Climático (IPCC). 2006. *Directrices del IPCC para los inventarios nacionales de gases de efecto invernadero*. Volumen 4: Agricultura, silvicultura y otros usos de la tierra.

Laurance, W. F., 1997. «Biomass Collapse in Amazonian Forest Fragments». *Science* 278, 1117–1118.

Laurance, W.F., 2000. «Do edge effects occur over large spatial scales?» *Trends in Ecology & Evolution* 15, 134–135.

Laurance, William F., Williamson, G.B., 2001. «Positive Feedbacks among Forest Fragmentation, Drought, and Climate Change in the Amazon». *Conservation Biology* 15, 1529–1535.

Laurance, W., Lovejoy, T., Vasconcelos, H., Bruna, E., Didham, R., Stouffer, P., Gascon, C., Bierregaard, R., Laurance, S., Sampaio, E., 2002. «Ecosystem decay of Amazonian forest fragments: a 22-year investigation». *Conservation Biology* 16, 605–618.

Nelson, E., et al. 2010. «Projecting global land-use change and its effect on ecosystem service provision and biodiversity with simple models». *PLOS One* 5: e14327.
