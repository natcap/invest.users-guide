.. _recreation:

**************************
Visitación: ocio y turismo
**************************

Resumen
=======

El ocio y el turismo son componentes importantes de muchas economías nacionales y locales y contribuyen de innumerables maneras a la calidad de vida, el sentido del lugar, la conexión social, el bienestar físico, el aprendizaje y otros aspectos intangibles. Para cuantificar el valor de los entornos naturales, el modelo de recreación InVEST predice la propagación de los días-persona de recreación, basándose en las ubicaciones de los hábitats naturales y otras características que son un factor en las decisiones de las personas sobre dónde recrearse. La herramienta estima la contribución de cada atributo a la tasa de visitas en una simple regresión lineal. A falta de datos empíricos sobre las visitas, parametrizamos el modelo utilizando un sustituto de las visitas: las fotografías geoetiquetadas publicadas en el sitio web flickr. A partir de las estimaciones de los días de uso de las fotografías, el modelo predice cómo los futuros cambios en las características naturales alterarán los índices de visitas. La herramienta produce mapas que muestran los patrones actuales de uso recreativo y mapas de los patrones futuros de uso bajo escenarios alternativos.

**El modelo de recreación está diseñado para responder a estas preguntas básicas  

1) ¿Cuáles son los índices de visita *relativos* en un paisaje o en un conjunto de lugares?  

2) ¿Qué características del entorno natural/construido influyen en el patrón espacial de las tasas de visita y cuáles son los niveles relativos de influencia de esas características?  

3) Ante un nuevo escenario en el que los patrones espaciales de las características naturales/construidas han cambiado, ¿cómo cambiarán los índices de visitas en respuesta a ello?  

Introducción
============

Las actividades recreativas y el turismo son componentes importantes de muchas economías nacionales y locales y contribuyen de innumerables maneras a la calidad de vida, el sentido del lugar, la conexión social, el bienestar físico, el aprendizaje y otros aspectos intangibles. Una razón clave para estudiar los patrones de recreación o turismo es la importancia económica de esta industria. La contribución total de los viajes y el turismo al producto interior bruto (PIB) mundial en 2011 fue de aproximadamente 6.000 millones de dólares (9% del PIB), con un crecimiento previsto de 10.000 millones de dólares para 2022 (World Travel and Tourism Council 2012). Por supuesto, las repercusiones económicas son solo una forma de medir la importancia del ocio y el turismo. Estas actividades contribuyen de forma decisiva a diversos aspectos del bienestar humano (Russell et al. 2013). Por ejemplo, las actividades recreativas al aire libre son una experiencia espiritual para muchas personas (por ejemplo, Trainor y Norgaard 1999), y las interacciones sociales en la naturaleza contribuyen a crear un sentido de lugar (por ejemplo, Willox et al. 2012).

Una parte importante y creciente de las actividades recreativas está "basada en la naturaleza", lo que implica interacciones con el entorno natural o su apreciación (Balmford et al. 2009). En este tipo de actividades, las características del entorno influyen en las decisiones de las personas sobre dónde, cuándo y cómo recrearse. Quienes bucean, por ejemplo, seleccionan los destinos en función de la claridad y la temperatura del agua y de la diversidad de la vida marina (Williams y Polunin 2000, Uyarra et al. 2009). Quienes observan aves se sienten atraídos por los mejores lugares para ver las especies objetivo (Naidoo y Adamowicz 2005), que inevitablemente son lugares en los que los sistemas naturales mantienen poblaciones de aves deseables (Puhakka et al. 2011). Algunas actividades recreativas dependen de atributos medioambientales como la riqueza de especies (Loureiro et al. 2012), la diversidad de hábitats (Neuvonen et al. 2010, Loureiro et al. 2012), las precipitaciones (Loomis y Richardson 2006) y la temperatura (Richardson y Loomis 2005), así como de otros atributos como las infraestructuras y los atractivos culturales (Mills y Westover 1987, Hill y Courtney 2006).

.. _rec-the-model:

El modelo
=========

El objetivo del modelo de recreación InVEST es predecir la propagación de los días-persona de recreación y turismo, basándose en las ubicaciones de los hábitats naturales, la accesibilidad y las características construidas que son un factor en las decisiones de las personas sobre dónde recrearse (Adamowicz et al. 2011). La herramienta produce mapas que muestran los patrones actuales de uso recreativo y, opcionalmente, mapas de uso futuro bajo escenarios alternativos.

.. _rec-how-it-works:

Cómo funciona
-------------

El modelo muestra la tasa de visitas a través de paisajes (celdas de la cuadrícula) o en áreas discretas (polígonos) y opcionalmente construye un modelo de regresión para estimar la contribución de los atributos del paisaje a la tasa de visitas, utilizando una regresión lineal simple:

... matth:: y_i = \beta_{0} + \beta_1 x_{i1} + ... + \beta_{p} x_{ip} \text{ para } i = 1 ... n,

donde :math:`x_{ip}` es la cobertura de cada atributo en cada celda o polígono (en adelante denominado "celda"), :math:`i`, dentro de un Área de Interés (ADI) que contiene :math:`n` celdas. A falta de datos empíricos sobre las visitas para :math:`y_i`, parametrizamos el modelo utilizando una medida de visitas de origen colectivo: fotografías geoetiquetadas publicadas en el sitio web flickr (véase la sección :ref:`rec-photos` para más información). Dicho otra vez, el modelo de recreación InVEST predice la propagación de los días-persona de recreación en el espacio. Para ello, utiliza los atributos de los lugares, como las características naturales (por ejemplo, la distribución de los hábitats), las características construidas (por ejemplo, las carreteras) y los usos humanos (por ejemplo, las actividades industriales), entre otros.

La herramienta comienza transformando en logaritmo todos los valores de :math:`y_i`, tomando el logaritmo natural de la media de días-foto por celda + 1. A continuación, se realiza una regresión lineal simple para estimar el efecto de cada atributo en las tasas de visita transformadas en logaritmos en todas las celdas de la cuadrícula dentro de la región de estudio. Estas estimaciones (los valores :math:`beta_{p}`) pueden utilizarse para un escenario adicional, para predecir cómo los futuros cambios en el paisaje alterarán la tasa de visitas. El modelo utiliza la regresión por mínimos cuadrados ordinarios, realizada por la función linalg.lstsq de la biblioteca numpy de Python (van der Walt et al. 2011).

.. _rec-photos:

Días de usuarios de fotos
-------------------------

Dado que los datos precisos sobre el número de visitantes a menudo solo se recogen en unos pocos lugares específicos de cualquier región de estudio, suponemos que la visitación actual puede aproximarse mediante el número total de días-persona anuales de fotografías cargadas en el sitio web para compartir fotografías `flickr <https://www.flickr.com>`_. Muchas de las fotografías de flickr se han asignado a una latitud/longitud específica. Utilizando esta ubicación, junto con el nombre de quien fotografía y la fecha en que se tomó la imagen, el modelo InVEST cuenta el total de fotos-usuarios-días para cada celda de la cuadrícula o polígono. Un fotos-usuarios-días en un lugar es un único fotógrafo que tomó al menos una fotografía en un día específico. Para cada celda, el modelo suma el número de fotos-usuarios-días para todos los días de 2005 a 2014 (o un rango definido por usted dentro de esos años), y devuelve el número medio anual de fotos-usuarios-días (PUD_YR_AVG). PUD_YR_AVG es :math:`y_i` en la ecuación anterior.

Hemos observado que el número de personas que visitan un lugar anualmente para recrearse está relacionado con el número de fotografías tomadas en la misma zona y subidas a la base de datos de flickr en 836 atracciones para visitantes de todo el mundo (Wood et al. 2013). La densidad de las fotografías varía espacialmente, lo que repercute en el tamaño de la celda que puede elegirse para el análisis (véase :ref:`rec-data-needs`: Tamaño de la celda). Los cálculos de la PUD se realizan en un servidor remoto a partir de un amplio conjunto de datos globales que el Proyecto Natural Capital se encarga de conservar y mantener.

Variables predictivas
---------------------

En la ecuación de regresión anterior, los fotos-usuario-días son la variable :math:`y_i` y todas las variables :math:`x` del lado derecho son variables predictivas. Se trata de características del Área de Interés que probablemente influyan en los patrones de visita a través del espacio. Se puede proporcionar cualquier número de variables de predicción y el modelo calculará una regresión que estima los valores de :math:`beta_{p}` para cada predictor. :math:`beta_{p}` indica la relación entre una variable predictiva y la tasa de visitación, después de tener en cuenta todas las demás variables predictivas incluidas en la regresión.

Hemos encontrado que suele ser útil considerar al menos una variable predictiva de varias categorías principales: capital natural (por ejemplo, hábitats, lagos), capital construido (por ejemplo, carreteras, hoteles), actividades industriales y acceso o costo (por ejemplo, distancia al aeropuerto principal). A menudo, las variables individuales que representan cada una de estas categorías pueden explicar la mayor parte de la variación en los fotos-usuarios-días. Esta herramienta le permite proporcionar variables predictoras en formatos SIG y procesar esas capas de diversas maneras (descritas en la sección :ref:`rec-data-needs`).

Análisis de escenarios
----------------------

Si se calcula una regresión, el modelo puede estimar opcionalmente las tasas de visitación dado un conjunto de predictores modificados que representan un escenario futuro o alternativo. Los predictores del escenario deben representar las mismas características que se seleccionaron como variables predictivas, pero pueden representar versiones modificadas de esas características (por ejemplo, redes de carreteras modificadas, puntos de hotel adicionales, distribuciones de hábitat alteradas, etc.). Las predicciones de los escenarios se realizan utilizando la ecuación de regresión anterior. En primer lugar, se estiman los coeficientes de cada variable predictiva como se describe en :ref:`rec-how-it-works`, y luego se aplican esos coeficientes a los valores de cada predictor que se ha modificado para un escenario. Consulte la sección :ref:`rec-data-needs` para obtener más detalles sobre la preparación de los datos del escenario.

Limitaciones y simplificaciones
-------------------------------

El modelo no presupone que ninguna variable de predicción tenga un efecto sobre las visitas. En cambio, la herramienta estima la magnitud del efecto de cada predictor basándose en su correspondencia espacial con la visitación actual en el área de interés. Los valores de fotos-personas-días por celdas se toman como medida de la visitación y se hace una regresión contra los valores de las variables predictivas en todas las celdas. Cuando se proporciona una tabla de predicción de escenarios, la herramienta utiliza los valores :math:`beta_{p}` calculados para la tabla de predicción y los aplica a los predictores de escenarios futuros. Este paso requiere la suposición de que las respuestas de las personas a los atributos que sirven de predictores en el modelo no cambiarán con el tiempo. En otras palabras, en el futuro, las personas seguirán siendo atraídas o repelidas por los predictores de la misma manera que lo son actualmente.

.. _rec-data-needs: 

Necesidades de datos
====================

.. note:: Todos los datos del SIG a los que se hace referencia en la tabla de predicción deben estar en el mismo sistema de coordenadas *proyectado* que el shapefile del Área de Interés (ADI). Todos los cálculos de distancia, longitud y área utilizan las mismas unidades que el sistema de coordenadas del ADI.

- :investspec:`recreation.recmodel_client workspace_dir`

- :investspec:`recreation.recmodel_client results_suffix`

- :investspec:`recreation.recmodel_client aoi_path` Se recomienda proyectar este vector en unidades lineales, especialmente si se utiliza para calcular una regresión y un escenario. Los resultados se agregan a estos polígonos.

- :investspec:`recreation.recmodel_client start_year`
- :investspec:`recreation.recmodel_client end_year`

- :investspec:`recreation.recmodel_client compute_regression` Si no se selecciona, los resultados se limitarán a un mapa de las tasas de visitación actuales en los polígonos o celdas de la cuadrícula del ADI.

- :investspec:`recreation.recmodel_client predictor_table_path` These predictors are the :math:`x_{ip}` values described in :ref:`rec-how-it-works`.

    Columnas:

    - :investspec:`recreation.recmodel_client predictor_table_path.columns.id`
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.path` En el ejemplo siguiente, los archivos enumerados en la columna de la ruta se encuentran en la misma carpeta que el archivo Predictor_Table.csv. Los archivos de predictores pueden estar ubicados en otros lugares, pero se debe incluir en esta tabla la ruta completa a ellos o la ruta relativa a este archivo CSV.
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.type`

    **Ejemplo de tabla de predicción:**
    
    .. csv-table::
       :file: ../invest-sample-data/recreation/predictors.csv
       :header-rows: 1
       :widths: auto

- :investspec:`recreation.recmodel_client scenario_predictor_table_path` Esta tabla tiene las mismas columnas y el mismo formato que la Tabla de predicción descrita anteriormente.

- :investspec:`recreation.recmodel_client grid_aoi`

- :investspec:`recreation.recmodel_client grid_type`

- :investspec:`recreation.recmodel_client cell_size` El tamaño de la celda está **en las mismas unidades lineales que el ADI**. Por ejemplo, si el ADI está en una proyección UTM con unidades de metros, el parámetro del tamaño de la celda también estará en metros.

   .. note:: El número de celdas de la cuadrícula afecta en gran medida al tiempo de procesamiento. Si no está seguro del tamaño de las celdas que debe especificar, elija un tamaño muy grande la primera vez (10 km o más), y luego vuelva a ejecutar el modelo con tamaños más pequeños si es necesario. El tamaño y el número de celdas adecuados dependen de varios factores, como los objetivos del estudio y la densidad de las fotografías, que varía de una región a otra. Para que el modelo calcule los efectos de las variables predictivas (tal y como se describe en la sección :ref:`rec-how-it-works`), se debe seleccionar un tamaño de celda lo suficientemente grande como para que la mayoría de las celdas contengan fotografías. Le recomendamos que empiece a ejecutar el modelo con tamaños de celda que oscilen entre 10 y 100 km, en función de la superficie total del ADI. A continuación, evalúe de forma iterativa los resultados del modelo (descritos en :ref:`rec-interpreting-results`) y vuelva a ejecutar el modelo para determinar un tamaño de celda adecuado.

.. _rec-running-model:

Ejecución del modelo
====================

.. warning:: Este modelo requiere una conexión a Internet.

El modelo utiliza una interfaz para introducir todos los datos necesarios y opcionales (véase :ref:`rec-data-needs`). El shapefile del ADI se envía a un servidor manejado por el Proyecto Natural Capital , donde se realizan los cálculos de fotos-usuarios-días. Por consiguiente, este modelo requiere una conexión a Internet. El modelo puede ejecutarse con tres configuraciones:

#. Obtenga un mapa de las tasas de visita en su Área de Interés. Proporcione un "Espacio de trabajo" y un "Área de interés", no marque "Calcular regresión". Los resultados incluyen "pud_results.shp" (:ref:`rec-interpreting-results`).
#. Obtenga un mapa de tasas de visitas y calcule una regresión con un conjunto de predictores. Proporcione un "Espacio de trabajo" y un "Área de interés", marque "Calcular regresión" y proporcione la "Tabla de predictores" :ref:`rec-data-needs`. Los resultados incluyen "pud_results.shp", "predictor_data.shp" y "regression_coefficients.txt" (:ref:`rec-interpreting-results`).
#. Estime las tasas de visitación para un Escenario. Proporcione un "Espacio de trabajo" y un "Área de interés", marque "Calcular regresión" y proporcione una "Tabla de predictores" y una "Tabla de predictores del escenario" (:ref:`rec-data-needs`). Los resultados incluyen "pud_results.shp", "predictor_data.shp", "regression_coefficients.txt" y "scenario_results.shp" (:ref:`rec-interpreting-results`).

El tiempo necesario para ejecutar el modelo varía en función de la extensión del ADI, el número de celdas de la cuadrícula y el número y tamaño de las capas de predicción. Le aconsejamos que ejecute el modelo primero sin calcular una regresión, y que empiece con un tamaño de celda grande si cuadricula el ADI.

Tenga en cuenta que el servidor que realiza el análisis también registra la dirección IP de cada usuario/a.

.. _rec-interpreting-results:

Interpretación de los resultados
================================

Resultados del modelo
---------------------

+ **pud_results.shp**: Las características de este shapefile de polígonos coinciden con el shapefile original del ADI, o con la versión cuadriculada del ADI si se ha seleccionado la opción "Cuadricular el ADI". Los atributos incluyen todas las columnas de atributos presentes en el shapefile del ADI original, junto con estos:

  + **PUD_YR_AVG** es el promedio de fotos-usuaruos-días por año (:ref:`rec-photos`). Corresponde a la media de *PUD* descrita en Wood et al. (2013).

  + **PUD_JAN**, PUD_FEB, .... PUD_DEC es el promedio de fotos-usuarios-días de cada mes. Por ejemplo, si el intervalo de fechas es el predeterminado 2005-2014, entonces PUD_JAN es la media de los diez foto-días de enero.

+ **monthly_table.csv**:  

  + Esta tabla contiene el total de fotos-usuarios-días contabilizados en cada celda para cada mes del intervalo de fechas elegido. Cada fila de esta tabla es una única celda o polígono de la cuadrícula ADI. Las columnas representan los meses ("2005-1" es enero de 2005, "2014-12" es diciembre de 2014).

+ **predictor_data.shp** (resultado si se selecciona Calcular regresión):

  + Este shapefile tiene polígonos que coinciden con los de "pud_results.shp" y tiene campos definidos por los ids dados en la Tabla de predictores. Los valores de esos campos son la métrica calculada por la característica de respuesta (:ref:`rec-data-needs`: Predictor Table).

+ **regression_coefficients.txt** (resultado si se selecciona Calcular regresión):

  + Se trata de un archivo de texto resultante del análisis de regresión. Incluye las estimaciones de :math:`beta_p` para cada variable predictiva (véase :ref:`rec-how-it-works`). También contiene un valor "server id hash" que puede utilizarse para correlacionar el resultado del PUD con los datos disponibles en el servidor PUD. Si estos resultados se utilizan en la publicación, este hash debe incluirse con los resultados para su reproducibilidad.

+ **scenario_results.shp** (resultado si se proporciona la Tabla de predicción de escenarios):

  + Este shapefile coincide con "predictor_data.shp", pero sus campos provienen de los predictores definidos en la Tabla de predicción de escenarios y hay un campo adicional "PUD_EST" que es el PUD_YR_AVG estimado por polígono.

+ **natcap.invest...client-log...txt** 

  + Este archivo de texto es el registro que se produce automáticamente cada vez que se ejecuta el modelo. Puede ser útil para solucionar errores. En la parte superior del registro también se encuentra un registro de todos los valores de input seleccionados para esa ejecución del modelo.

.. _rec-references:

Referencias
===========

Adamowicz, WL, R Naidoo, E Nelson, S Polasky, J Zhang. 2011. Nature-based tourism and recreation. In: Kareiva P, G Daily, T Ricketts, H Tallis, S Polasky (eds) Natural Capital: Theory and Practice of Mapping Ecosystem Services. Oxford University Press, Nueva York.

Balmford, A, J Beresford, J Green, R Naidoo, M Walpole, A Manica. 2009. A global perspective on trends in nature-based tourism. PLoS Biology 7: e1000144.

Hill, GW, PR Courtney. 2006. Demand analysis projections for recreational visits to countryside woodlands in Great Britain. Forestry 79: 18-200.

Loomis, JB, RB Richardson. 2006. An external validity test of intended behavior: comparing revealed preference and intended visitation in response to climate change. Journal of Environmental Planning and Management 49: 621-630.

Loureiro, ML, F Macagno, PA Nunes, R Tol. 2012. Assessing the impact of biodiversity on tourism flows: an econometric model for tourist behaviour with implications for conservation policy. Journal of Environmental Economics and Policy 1: 174-194.

Mills, AS, TN Westover. 1987. Structural differentiation: a determinant of park popularity. Annals of Tourism Research 14: 486-498.

Naidoo, R, WL Adamowicz. 2005. Biodiversity and nature-based tourism at forest reserves in Uganda. Environment and Development Economics 10: 159-178.

Neuvonen, M, E Pouta, J Puustinen, T Sievänen. 2010. Visits to national parks: effects of park characteristics and spatial demand. Journal for Nature Conservation 18: 224-229.

Puhakka, L, M Salo, IE Sääksjärvi. 2011. Bird diversity, birdwatching tourism and conservation in Peru: a geographic analysis. PLoS One 6: e26786.

Richardson, R, JB Loomis. 2005. Climate change and recreation benefits in an alpine national park. Journal of Leisure Research 37: 307-320.

Russell, R, AD Guerry, P Balvanera, RK Gould, X Basurto, KM Chan, S Klain, J Levine, J Tam. 2013. Humans and nature: how knowing and experiencing nature affect well-being. Annual Review of Environment and Resources 38: en prensa.

Trainor, SF, RB Norgaard. 1999. Recreation fees in the context of wilderness values. Journal of Park and Recreation Administration 17: 100-115.

Uyarra, MC, AR Watkinson, IM Côté. 2009. Managing dive tourism for the sustainable use of coral reefs: validating diver perceptions of attractive site features. Environmental Management 43: 1-16.

van der Walt, Stéfan, S. Chris Colbert, and Gaël Varoquaux. 2011. The NumPy Array: A Structure for Efficient Numerical Computation. Computing in Science & Engineering 13 (2): 22–30. 

Williams, ID, NV Polunin. 2000. Differences between protected and unprotected reefs of the western Caribbean in attributes preferred by dive tourists. Environmental Conservation 27: 382-391.

Willox, AC, SL Harper, JD Ford, K Landman, K Houle, V Edge. 2012. "From this place and of this place:" climate change, sense of place, and health in Nunatsiavut, Canada. Social Science and Medicine 75: 538-547.

Wood, SA, AD Guerry, JM Silver, M Lacayo. 2013. `Using social media to quantify nature-based tourism and recreation <https://www.nature.com/articles/srep02976>`_. Scientific Reports 3: 2976.

World Travel and Tourism Council. 2012. `Travel and Tourism: Economic Impact <http://www.ontit.it/opencms/export/sites/default/ont/it/documenti/files/ONT_2012-03-23_02800.pdf>`_.
