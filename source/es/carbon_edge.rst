Efecto de borde del carbono forestal
====================================

Resumen
-------

El modelo de efecto borde de carbono de InVEST amplía el enfoque del modelo de carbono de InVEST para tener en cuenta la degradación de las reservas forestales de carbono debido a la creación de bordes forestales. Aplica las relaciones conocidas entre el almacenamiento de carbono y la distancia al borde del bosque para calcular los efectos de borde en de carbono, y combina estas estimaciones con los datos del inventario de carbono para construir el mapa de carbono global. El modelo de efectos de borde se refiere solo al carbono sobre el suelo, porque los efectos de borde no han sido documentados para las otras reservas de carbono (bajo tierra, suelo y materia muerta). Para todas las demás reservas de carbono, y para las clases de bosques no tropicales o si el modelo se ejecuta sin efectos de borde, sigue el enfoque de inventario del IPCC (2006) para asignar valores de almacenamiento de carbono por clase de cobertura del suelo.

Introducción
------------

Los efectos del futuro cambio de uso de la tierra en el almacenamiento o secuestro de carbono pueden modelizarse aplicando las estimaciones de almacenamiento de carbono encontradas en la literatura para diferentes tipos de hábitat paisaje (por ejemplo, Nelson et al. 2010). Sin embargo, este enfoque asume que todos los hábitats son equivalentes en su calidad de almacenamiento de carbono independientemente de dónde se encuentre, a pesar de que existen pruebas sustanciales de que la fragmentación puede desempeñar un papel en alterar las tasas de almacenamiento y secuestro de carbono en los bosques tropicales (Broadbent et al. 2008, Dantas et al. 2011, Laurance et al. 1997, 2000, 2001, 2002). Por ejemplo, se ha demostrado que el bosque central almacena más de tres veces el carbono de los bosques de borde en los bosques atlánticos brasileños (Dantas et al. 2011). Chaplin-Kramer et al. (2015) investigaron este patrón para todo el pantrópico utilizando datos de teledetección sobre la biomasa (Baccini et al. 2012) y la cubierta terrestre asociada (Friedl et al. 2011) y hallaron una relación continua de degradación del almacenamiento de carbono gradualmente hacia el borde del bosque, que varía sustancialmente de una región a otra. Este modelo tiene en cuenta estos efectos de borde documentados en los bosques tropicales, asignando el almacenamiento de carbono en función de la distancia de un píxel al borde del bosque más cercano. Esto puede mejorar la precisión general de las estimaciones de almacenamiento de carbono en un 20% con respecto a los enfoques de inventario forestal, y capta mejor los impactos de la degradación de los bosques por la fragmentación, más allá del área de hábitat perdida.

El modelo
---------

El modelo de efecto de borde de carbono InVEST es una actualización del modelo de carbono InVEST que incorpora la degradación del almacenamiento de carbono que se produce debido a los efectos de borde en los bosques tropicales. Quien usa designa qué clases de cobertura terrestre de tierra son bosques, y entonces el modelo utiliza resultados de regresión para predecir el carbono en toda una parcela forestal en función de su distancia al borde forestal más cercano. Estos resultados se combinan con el carbono asignado a las clases no forestales mediante métodos tradicionales de inventario (IPCC 2006) utilizados en el modelo de carbono InVEST para generar un mapa de almacenamiento de carbono sobre el suelo para todas las clases de cobertura del suelo. El modelo de efecto de borde de carbono de InVEST puede ejecutarse para calcular solo el carbono sobre el suelo o todas las reservas de carbono, y puede correr con o sin efectos de borde. Es importante señalar que la regresión de los efectos de borde solamente se refiere a las reservas de carbono sobre el suelo porque solo se han detectado efectos de borde en las reservas de carbono sobre el suelo. Para incluir los otros tres reservorios de carbono (subterráneo, suelo y materia materia muerta en pie), la densidad de carbono (Mg/ha) debe incluirse para cada clase en la tabla biofísica.

Se debe tener en cuenta también que los datos de regresión no cubren toda la Tierra. Puede ser útil asegurarse de que cubren su área de interés trayendo la capa del modelo de regresión forest_carbon_edge_regression_model_parameters.shp (que se encuentra en los datos de muestra de este modelo) a un SIG y comprobándola con su área de estudio. Si los datos de regresión no cubren su área de estudio, no podrá utilizar el modelo para calcular los efectos de borde.
 
Cómo funciona
~~~~~~~~~~~~~

Este modelo sigue la metodología descrita en Chaplin-Kramer et al. (2015), que construye una serie de modelos de regresión entre la densidad  de biomasa forestal (Mg/ha) y la distancia desde el borde del bosque (km) para celdas de cuadrícula de 100 km x 100 km a lo largo del pantrópico. En las cuadrículas en las que la mayoría de los píxeles eran de biomas forestales, se consideraron tres modelos candidatos de regresión para representar la relación entre la densidad de biomasa y la distancia al borde del bosque:

1. Asintótica: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} - \theta_{2} \cdot \mathrm{\exp}( - \theta_{3} \cdot \mathrm{\text{Distance}})`

2. Logarítmica: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot ln(\mathrm{\text{Distance}})`

3. Lineal: \ :math:`\mathrm{\text{Biomass}} = \theta_{1} + \theta_{2} \cdot \mathrm{\text{Distance}}`

A continuación, para cada celda de la cuadrícula, se utiliza el candidato con el valor más alto de r\ :sup:`2` se utiliza para representar mejor la relación entre densidad y la distancia al borde del bosque.  Los modelos (2) y (3) se consideraron como alternativas adecuadas (y más simplistas) en las celdas en las donde no se observan distancias más altas y, por lo tanto, el núcleo del bosque no estaba firmemente establecido. En la gran mayoría de las cuadrículas, el modelo (1) fue óptimo.

Los resultados de estas regresiones se pueden encontrar en el shapefile de parámetros de regresión de borde de carbono (*core_data/forest_carbon_edge_regression_model_parameters.shp*) en el conjunto de datos de muestra que se proporciona para el modelo de efecto de borde de carbono de InVEST.

Para cualquier píxel de bosque dentro de la región de estudio, el modelo calcula la distancia de ese píxel al borde del bosque y luego calcula la biomasa a un número predefinido de modelos de regresión más cercanos que luego se agrega a un único resultado utilizando un esquema de interpolación lineal de la distancia. El modelo convierte la biomasa en carbono con un factor de conversión proporcionado por quien usa, que por defecto es de 0,47 (IPCC 2006). Se puede designar el número de modelos locales utilizados en el esquema de interpolación, que por defecto es de 10, pero puede ir desde 1 (solo el punto más cercano) hasta 2635 (todos los modelos de regresión del planeta). Tenga en cuenta que una selección de 1 puede dar lugar a diferencias artificialmente grandes en el carbono cuando se mueve de un píxel al siguiente cuando caen en diferentes celdas de la cuadrícula de regresión. Cuanto mayor sea el número de celdas de la cuadrícula de regresión seleccionadas, más suave será la transición de un píxel a otro. Puede seleccionarse el número de celdas de cuadrícula que se superponen a toda la región de estudio para eliminar cualquier artefacto de la selección del modelo. Esto puede determinarse  examinando la geometría *intermediate_outputs\local_carbon_shape.shp* superpuesta en el área de interés. El esquema de interpolación lineal para biomasa b en el píxel p se da más abajo

.. math:: b_{p} = \frac{\sum_{i \in n}\frac{1}{d_{i}}{b_{i}^{'}}_{}}{\sum\frac{1}{d_{i}}}

Donde,

-  :math:`b_{p}`\ es la biomasa interpolada en el píxel p

-  n es el número de modelos más cercanos para interpolar, un valor
   proporcionado por quien usa

-  i es el i\ :sup:`th` modelo de biomasa más cercano al píxel p

-  d\ :sub:`i` es la distancia del píxel p al centroide del
   modelo de biomasa i\ :sup:`th` .

El carbono calculado para las clases no forestales sigue la metodología del modelo de carbono InVEST, asignando valores basados en los datos del inventario forestal designados en la tabla biofísica. Los mapas de carbono que siguen este enfoque de inventario y el enfoque de efectos de borde se se fusionan en el mapa de carbono final, de manera que las cubiertas forestales presenten efectos de borde y todas las demás cubiertas terrestres no.

Necesidades de datos
--------------------
Tenga en cuenta que todos los inputs espaciales deben estar en el mismo sistema de coordenadas proyectadas y en unidades de metros lineales.

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

   Matorrales cerrados, matorrales abiertos, praderas: Miranda, Sabrina do Couto, et al. Regional variations in biomass distribution in Brazilian savanna woodland. Biotropica 46.2 (2014): 125-138.

   Sabanas boscosas, sabanas: Saatchi, Susan S., et al. Distribution of aboveground live biomass in the Amazon basin. Global Change Biology 13.4 (2007): 816-837.

   Tierras de cultivo: Fearnside, Philip M. Greenhouse gases from deforestation in Brazilian Amazonia: net committed emissions. Climatic Change 35.3 (1997): 321-360.

- :investspec:`forest_carbon_edge_effect pools_to_calculate`

- :investspec:`forest_carbon_edge_effect compute_forest_edge_effects` Si se selecciona, el modelo utiliza el método Chaplin-Kramer et al. para contabilizar las reservas de carbono por encima del suelo en los tipos de bosque tropical indicados por un "1" en el campo "is_tropical_forest" de la tabla biofísica. 

- :investspec:`forest_carbon_edge_effect tropical_forest_edge_carbon_model_vector_path` Este input se proporciona en los datos de muestra y no es necesario modificarla a menos que haya realizado una regresión separada para su región y tenga información mejor o actualizada. El shapefile proporcionado se derivó de un análisis pantropical de la relación entre la biomasa forestal y la distancia al borde del bosque (Chaplin-Kramer et al. 2015). 

   Tenga en cuenta que los datos de regresión no cubren toda la Tierra. Puede ser útil asegurarse de que cubre su área de interés llevando la capa del modelo de regresión *forest_carbon_edge_regression_model_parameters.shp* (que se encuentra en los datos de muestra de este modelo) en un SIG y cotejarlo con su área de estudio. Si los datos de la regresión no cubren su zona de estudio, no podrá utilizar el modelo para calcular los efectos de borde. 

- :investspec:`forest_carbon_edge_effect n_nearest_model_points` El valor por defecto es 10. Los valores más altos suavizan en mayor medida la variación del efecto de borde detectado en las diferentes celdas de la cuadrícula (que se ve en el shapefile del parámetro de regresión de borde de carbono).

- :investspec:`forest_carbon_edge_effect biomass_to_carbon_conversion_factor` El valor por defecto es 0,47 (según el IPCC 2006). Esto se refiere solo a los parámetros de regresión de los efectos de borde; todos los valores de la tabla biofísica deberían estar ya en términos de carbono, no de biomasa.

- :investspec:`forest_carbon_edge_effect aoi_vector_path` Tenga en cuenta que los datos de regresión no cubren toda la Tierra. Puede ser útil asegurarse de que cubren su área de interés trayendo la capa del modelo de regresión *forest_carbon_edge_regression_model_parameters.shp* (que se encuentra en los datos de muestra de este modelo) al SIG y comparándola con su área de estudio. Si los datos de regresión no cubren su área de estudio, no podrá utilizar el modelo para calcular los efectos de borde.

Interpretación de resultados
----------------------------

Resultados finales
~~~~~~~~~~~~~~~~~~
-  **Registro de parámetros**. Cada vez que se ejecuta el modelo, un archivo de texto (.txt)
      aparecerá en el \ *Espacio de trabajo*. El archivo enumerará los valores de los parámetros
      para esa ejecución y se nombrará de acuerdo con el servicio,
      la fecha y la hora. Cuando se ponga en contacto con NatCap por errores en una ejecución del modelo
      de un modelo, incluya el registro de parámetros.

-  **carbon_map_[Suffix[.tif**. Un mapa de las reservas de carbono por píxel, con
      la cantidad en el bosque derivada de la regresión basada en la distancia
      al borde del bosque, y la cantidad en clases no forestales según
      la tabla biofísica. Obsérvese que, dado que el mapa muestra el carbono
      (Mg) por píxel, los mapas de resolución más gruesa deberían tener valores más altos
      para el carbono, porque las áreas de los píxeles son mayores.

-  **aggregated_carbon_stocks_[Suffix].shp**: Si las áreas de servicio de
      interés son proporcionadas por quien usa, este shapefile resultante
      resume el carbono total (columna *c_sum*) y el carbono medio por
      ha (columna *c_ha_mean*) en los polígonos de área definidos. Los valores están
      en Mg.

Resultados intermedios
~~~~~~~~~~~~~~~~~~~~~~
-  intermediate_outputs\\\ **c_above_carbon_stocks_[Suffix].tif**. El carbono almacenado en la reserva de carbono de la biomasa sobre el suelo.

-  intermediate_outputs\\\ **c_below_carbon_stocks_[Suffix].tif**. El carbono almacenado en la reserva de carbono de la biomasa subterránea.

-  intermediate_outputs\\\ **c_dead_carbon_stocks_[Suffix].tif**. El carbono almacenado en la reserva de carbono de la biomasa de la materia muerta.

-  intermediate_outputs\\\ **c_soil_carbon_stocks_[Suffix].tif**. El carbono almacenado en la reserva de carbono de la biomasa del suelo.

-  intermediate_outputs\\\ **local_carbon_shape.shp**. Los parámetros de regresión reproyectados para que coincida con su área de estudio.

-  intermediate_outputs\\\ **edge_distance_[Suffix].tif**. La distancia de cada píxel del bosque al borde del bosque más cercano.

-  intermediate_outputs\\\ **tropical_forest_edge_carbon_stocks_[Suffix].tif**. Un mapa de carbono en el bosque solo, según el método de regresión
      
Apéndice: Fuentes de datos
--------------------------

:ref:`Land Use/Land Cover <lulc>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Carbon Pools <carbon_pools>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Referencias
-----------

Baccini, A., S. J. Goetz, W. S. Walker, N. T. Laporte, M. Sun, D. Sulla-Menashe, J. Hackler, P. S. A. Beck, R. Dubayah, M. A. Friedl, S. Samanta y R. A. Houghton. 2012. Estimated carbon dioxide emissions from tropical deforestation improved by carbon-density maps. Nature Climate Change 2:182–185.

Chaplin-Kramer, R., I. Ramler, R. Sharp, N. M. Haddad, J. S. Gerber, P. C. West, L. Mandle, P. Engstrom, A. Baccini, S. Sim, C. Mueller y H. King. (2015). Degradation in carbon stocks near tropical forest edges. Nature Communications.

Dantas de Paula, M., Alves-Costa, C. y Tabarelli, M., 2011. Carbon storage in a fragmented landscape of Atlantic forest: the role played by edge-affected habitats and emergent trees. Tropical Conservation Science 4, 349–358.

Friedl, M. A., D. Sulla-Menashe, B. Tan, A. Schneider, N. Ramankutty, A. Sibley yX. Huang. 2010. MODIS Collection 5 global land cover: Algorithm refinements and characterization of new datasets. Remote Sensing of Environment 114:168–182.

Intergovernmental Panel on Climate Change (IPCC). 2006. IPCC Guidelines for National Greenhouse Gas Inventories. Volume 4: Agriculture, Forestry and Other Land Use.

Laurance, W. F., 1997. Biomass Collapse in Amazonian Forest Fragments. Science 278, 1117–1118.

Laurance, W.F., 2000. Do edge effects occur over large spatial scales? Trends in ecology & evolution 15, 134–135.

Laurance, William F. y Williamson, G.B., 2001. Positive Feedbacks among Forest Fragmentation, Drought, and Climate Change in the Amazon. Conservation Biology 15, 1529–1535.

Laurance, W., Lovejoy, T., Vasconcelos, H., Bruna, E., Didham, R., Stouffer, P., Gascon, C., Bierregaard, R., Laurance, S. y Sampaio, E., 2002. Ecosystem decay of Amazonian forest fragments: a 22-year investigation. Conservation Biology 16, 605–618.

Nelson, E. et al. 2010. Projecting global land-use change and its effect on ecosystem service provision and biodiversity with simple models. PLOS One 5: e14327
