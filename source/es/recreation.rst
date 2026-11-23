.. _recreation:

*****************************
Visitas: recreación y turismo
*****************************

Resumen
=======

La recreación y el turismo son componentes importantes de muchas economías nacionales y locales, y contribuyen de innumerables maneras a la calidad de vida, el sentido de pertenencia a un lugar, la conexión social, el bienestar físico, el aprendizaje y otros aspectos intangibles. Para cuantificar el valor de los entornos naturales, el modelo de recreación de InVEST predice la distribución de los días-persona de recreación a partir de la ubicación de los hábitats naturales y de otras características que influyen en las decisiones de las personas sobre dónde realizar actividades recreativas. La herramienta estima la contribución de cada atributo a la tasa de visitas mediante una regresión lineal simple. Cuando no se dispone de datos empíricos sobre las visitas, el modelo se parametriza utilizando indicadores indirectos: fotografías georreferenciadas publicadas en Flickr y tuits georreferenciados publicados en Twitter. A partir de las estimaciones de días-usuario de fotografías (PUD) y días-usuario de Twitter (TUD), el modelo predice cómo los cambios futuros en las características naturales modificarán las tasas de visita. La herramienta genera mapas que muestran los patrones actuales de uso recreativo y mapas de los patrones futuros bajo distintos escenarios.

**El modelo de Recreación está diseñado para responder estas preguntas básicas:**

1) ¿Cuáles son las tasas *relativas* de visitas en un paisaje o en un conjunto de sitios?

2) ¿Qué características del entorno natural o construido influyen en el patrón espacial de las tasas de visita y cuál es la influencia relativa de esas características?

3) Ante un nuevo escenario en el que hayan cambiado los patrones espaciales de las características naturales o construidas, ¿cómo cambiarán las tasas de visita en respuesta a esos cambios?

Introducción
============

La recreación y el turismo son componentes importantes de muchas economías nacionales y locales, y contribuyen de innumerables maneras a la calidad de vida, el sentido de pertenencia a un lugar, la conexión social, el bienestar físico, el aprendizaje y otros aspectos intangibles. Una razón fundamental para estudiar los patrones de recreación o turismo es la importancia económica de esta industria. La contribución total de los viajes y el turismo al producto interno bruto (PIB) mundial en 2011 fue de aproximadamente USD 6 billones (9 % del PIB), y se esperaba que creciera hasta USD 10 billones para 2022 (World Travel and Tourism Council 2012). Por supuesto, los impactos económicos son solo una de las formas de medir la importancia de la recreación y el turismo. Estas actividades contribuyen de manera fundamental a diversos aspectos del bienestar humano (Russell et al. 2013). Por ejemplo, para muchas personas la recreación al aire libre constituye una experiencia espiritual (por ejemplo, Trainor y Norgaard 1999), y las interacciones sociales en la naturaleza contribuyen a construir un sentido de pertenencia a un lugar (por ejemplo, Willox et al. 2012).

Una parte importante y creciente de la recreación se basa en la naturaleza e implica interactuar con el entorno natural o apreciarlo (Balmford et al. 2009). En este tipo de actividades, las características del entorno influyen en las decisiones de las personas sobre dónde, cuándo y cómo realizar actividades recreativas. Por ejemplo, quienes practican buceo SCUBA eligen sus destinos según la claridad y temperatura del agua y la diversidad de la vida marina (Williams y Polunin 2000, Uyarra et al. 2009). Los observadores de aves se sienten atraídos por los mejores lugares para ver las especies que buscan (Naidoo y Adamowicz 2005), que inevitablemente son sitios donde los sistemas naturales sustentan poblaciones de aves deseables (Puhakka et al. 2011). Algunas actividades recreativas dependen de atributos ambientales como la riqueza de especies (Loureiro et al. 2012), la diversidad de hábitats (Neuvonen et al. 2010, Loureiro et al. 2012), la precipitación (Loomis y Richardson 2006) y la temperatura (Richardson y Loomis 2005), así como de otros atributos, como la infraestructura y las atracciones culturales (Mills y Westover 1987, Hill y Courtney 2006).

.. _rec-the-model:

El modelo
=========

El propósito del modelo de recreación de InVEST es predecir la distribución de los días-persona dedicados a la recreación y el turismo, a partir de la ubicación de los hábitats naturales, la accesibilidad y las características construidas que influyen en las decisiones de las personas sobre dónde realizar actividades recreativas (Adamowicz et al. 2011). La herramienta genera mapas que muestran los patrones actuales de uso recreativo y, de manera opcional, mapas del uso futuro bajo escenarios alternativos.

.. _rec-how-it-works:

Cómo funciona
-------------

El modelo muestra la tasa de visitas en paisajes (celdas de una cuadrícula) o en áreas discretas (polígonos) y, de manera opcional, construye un modelo de regresión para estimar la contribución de los atributos del paisaje a la tasa de visitas mediante una regresión lineal simple:

.. math:: y_i = \beta_{0} + \beta_1 x_{i1} + ... + \beta_{p} x_{ip} \text{ for } i = 1 ... n,

donde :math:`x_{ip}` representa la cobertura de cada atributo en cada celda o polígono (en adelante, «celda»), :math:`i`, dentro de un Área de Interés (AOI) que contiene :math:`n` celdas. Cuando no existen datos empíricos de visitas para :math:`y_i`, parametrizamos el modelo mediante medidas de visitas obtenidas de fuentes colaborativas: fotografías georreferenciadas publicadas en Flickr y tuits georreferenciados publicados en Twitter (consulte la sección :ref:`rec-userdays` para obtener más información). En otras palabras, el modelo de recreación de InVEST predice la distribución espacial de los días-persona dedicados a la recreación. Para ello utiliza atributos de los lugares, como características naturales (por ejemplo, distribución de hábitats), características construidas (por ejemplo, carreteras) y usos humanos (por ejemplo, actividades industriales), entre otros.

La variable de respuesta :math:`y_i` es una transformación logit de la proporción de días-usuario en cada celda (consulte :ref:`rec-userdays`). Luego se realiza una regresión lineal simple para estimar el efecto de cada atributo sobre las tasas de visita en todas las celdas de la cuadrícula de la región de estudio. Estas estimaciones (los valores :math:`\beta_{p}`) pueden utilizarse en un escenario adicional para predecir cómo los cambios futuros del paisaje modificarán las tasas de visita. El modelo utiliza una regresión por mínimos cuadrados ordinarios, ejecutada mediante la función linalg.lstsq de la biblioteca numpy de Python (van der Walt et al. 2011).

.. _rec-userdays:

Días-usuario
------------

Dado que los datos detallados sobre el número de visitantes suelen recopilarse únicamente en unos pocos lugares específicos de cada región de estudio, suponemos que las visitas actuales pueden aproximarse mediante el número total anual de días-persona representados por las fotografías subidas al sitio web para compartir fotografías `Flickr <https://www.flickr.com>`_ y por los tuits publicados en la plataforma de redes sociales Twitter (actualmente conocida como X). Muchas de las fotografías de Flickr y los tuits tienen asignadas coordenadas específicas de latitud y longitud. Mediante esta ubicación, junto con el nombre de usuario del autor y la fecha en que se tomó la fotografía o se publicó el tuit, el modelo InVEST cuenta el total de días-usuario de fotografías (PUD) y días-usuario de Twitter (TUD) para cada celda de la cuadrícula o polígono.

Un día-usuario en un lugar corresponde a una persona única que tomó al menos una fotografía o publicó un tuit en un día específico. Para cada celda, el modelo suma el número de días-usuario de fotografías y de Twitter de todos los días comprendidos entre 2012 y 2017 (o de un intervalo definido por el usuario dentro de esos años). Informa el total de PUD y TUD de cada año, así como el promedio anual de PUD y TUD (PUD_YR_AVG y TUD_YR_AVG). En la ecuación anterior, la variable de respuesta :math:`y_i` es una transformación logit de una proporción::

  # La proporción en cada celda i
  pr_PUD[i] = PUD_YR_AVG[i] / PUD_YR_AVG.sum()
  pr_TUD[i] = TUD_YR_AVG[i] / TUD_YR_AVG.sum()
  avg_pr_UD[i] = (pr_PUD[i] + pr_TUD[i]) / 2

  epsilon = avg_pr_UD[avg_pr_UD > 0].min() / 2 # la mitad del valor mínimo distinto de cero
  avg_pr_UD[avg_pr_UD == 0] = epsilon          # ajuste porque los ceros no pueden transformarse mediante logaritmos

  # Transformación logit:
  y = ln(avg_pr_UD / (1 - avg_pr_UD))

Hemos observado que el número de personas que visitan anualmente un lugar está relacionado con el número de fotografías tomadas en la misma zona y subidas a la base de datos de Flickr, según un estudio realizado en 836 atracciones turísticas de todo el mundo (Wood et al. 2013). La densidad de fotografías y tuits varía espacialmente, lo que tiene consecuencias para el tamaño de celda que puede elegirse para el análisis (consulte :ref:`rec-data-needs`: Tamaño de celda). Los cálculos de días-usuario se realizan en un servidor remoto, a partir de un extenso conjunto de datos global mantenido y actualizado por The Natural Capital Alliance.

Variables predictoras
---------------------

En la ecuación de regresión anterior, los días-usuario de fotografías constituyen la variable :math:`y_i`, y todas las variables :math:`x` del lado derecho son variables predictoras. Estas son características del Área de Interés que probablemente influyen en los patrones espaciales de las visitas. Los usuarios pueden proporcionar cualquier número de variables predictoras y el modelo calculará una regresión que estime los valores de :math:`\beta_{p}` para cada predictor. :math:`\beta_{p}` indica la relación entre una variable predictora y la tasa de visitas, después de considerar todas las demás variables predictoras incluidas en la regresión.

Con frecuencia resulta útil considerar al menos una variable predictora de varias categorías principales: capital natural (por ejemplo, hábitats y lagos), capital construido (por ejemplo, carreteras y hoteles), actividades industriales y acceso o costo (por ejemplo, distancia al aeropuerto principal). A menudo, una sola variable representativa de cada una de estas categorías puede explicar la mayor parte de la variación en los días-usuario de fotografías. Esta herramienta permite proporcionar variables predictoras en formatos SIG y procesar esas capas de diversas maneras (descritas en la sección :ref:`rec-data-needs`).

Análisis de escenarios
----------------------

Si se calcula una regresión, el modelo puede estimar opcionalmente las tasas de visita a partir de un conjunto de predictores modificados que representan un escenario futuro o alternativo. Los predictores del escenario deben representar las mismas características seleccionadas como variables predictoras, pero pueden corresponder a versiones modificadas de esas características (por ejemplo, redes viales modificadas, puntos adicionales de hoteles o distribuciones de hábitats alteradas). Las predicciones del escenario se realizan mediante la ecuación de regresión anterior. Primero se estiman los coeficientes de cada variable predictora, como se describe en :ref:`rec-how-it-works`; luego, esos coeficientes se aplican a los valores de cada predictor que se haya modificado para el escenario. Consulte la sección :ref:`rec-data-needs` para obtener más detalles sobre la preparación de los datos de escenarios.

Limitaciones y simplificaciones
===============================

El modelo no presupone que alguna variable predictora tenga un efecto sobre las visitas. En su lugar, la herramienta estima la magnitud del efecto de cada predictor a partir de su correspondencia espacial con las visitas actuales en el Área de Interés. Los valores de días-persona de fotografías por celda se consideran una medida de las visitas y se regresan frente a los valores de las variables predictoras en todas las celdas. Cuando se proporciona una Tabla de predictores de escenario, la herramienta utiliza los valores :math:`\beta_{p}` calculados para la Tabla de predictores y los aplica a los predictores del escenario futuro. Este paso supone que las respuestas de las personas a los atributos utilizados como predictores del modelo no cambiarán con el tiempo. En otras palabras, en el futuro las personas seguirán sintiéndose atraídas por los predictores —o rechazándolos— de la misma manera que lo hacen actualmente.

.. _rec-data-needs:

Datos necesarios
================

.. note:: Todos los datos SIG mencionados en la Tabla de predictores deben estar en el mismo sistema de coordenadas *proyectadas* que el vector del Área de Interés (AOI). Todos los cálculos de distancia, longitud y área utilizan las mismas unidades que el sistema de coordenadas del AOI.

- :investspec:`recreation.recmodel_client workspace_dir`

- :investspec:`recreation.recmodel_client results_suffix`

- :investspec:`recreation.recmodel_client aoi_path` Se recomienda que este vector esté proyectado en unidades lineales, especialmente si se utiliza para calcular una regresión y un escenario. Los resultados se agregan a estos polígonos.

- :investspec:`recreation.recmodel_client start_year`
- :investspec:`recreation.recmodel_client end_year`

- :investspec:`recreation.recmodel_client compute_regression` Si no se selecciona esta opción, los resultados se limitarán a un mapa de las tasas actuales de visitas en los polígonos o las celdas de la cuadrícula del AOI.

- :investspec:`recreation.recmodel_client predictor_table_path` Estos predictores son los valores :math:`x_{ip}` descritos en :ref:`rec-how-it-works`.

    Columnas:

    - :investspec:`recreation.recmodel_client predictor_table_path.columns.id`
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.path` En el ejemplo siguiente, los archivos indicados en la columna path se encuentran en la misma carpeta que el archivo Predictor_Table.csv. Los archivos de predictores pueden estar en otros lugares, pero en esta tabla debe incluirse su ruta completa o la ruta relativa a este archivo CSV.
    - :investspec:`recreation.recmodel_client predictor_table_path.columns.type`

    **Ejemplo de tabla de predictores:**

    .. csv-table::
       :file: ../../invest-sample-data/recreation/predictors.csv
       :header-rows: 1
       :widths: auto

- :investspec:`recreation.recmodel_client scenario_predictor_table_path` Esta tabla tiene las mismas columnas y el mismo formato que la Tabla de predictores descrita anteriormente.

- :investspec:`recreation.recmodel_client grid_aoi`

- :investspec:`recreation.recmodel_client grid_type`

- :investspec:`recreation.recmodel_client cell_size` El tamaño de celda se expresa **en las mismas unidades lineales que el AOI**. Por ejemplo, si el AOI utiliza una proyección UTM cuyas unidades son metros, el parámetro de tamaño de celda también se expresará en metros.

   .. note:: El número de celdas de la cuadrícula afecta considerablemente el tiempo de procesamiento. Si no sabe qué tamaño de celda especificar, elija inicialmente un tamaño muy grande (10 km o más) y vuelva a ejecutar el modelo con tamaños menores si es necesario. El tamaño y el número de celdas adecuados dependen de varios factores, incluidos los objetivos del estudio y la densidad de fotografías, que varía de una región a otra. Para que el modelo calcule los efectos de las variables predictoras (como se describe en la sección :ref:`rec-how-it-works`), los usuarios deben seleccionar un tamaño de celda suficientemente grande para que la mayoría de las celdas contengan fotografías. Recomendamos comenzar ejecutando el modelo con tamaños de celda de entre 10 y 100 km, según la extensión total del AOI. Luego, evalúe iterativamente los resultados del modelo (descritos en :ref:`rec-interpreting-results`) y vuelva a ejecutarlo para determinar un tamaño de celda adecuado.

.. _rec-running-model:

Ejecución del modelo
====================

.. warning:: Tenga en cuenta que el modelo de recreación requiere conexión a Internet.

El modelo utiliza una interfaz para introducir todos los datos obligatorios y opcionales (consulte :ref:`rec-data-needs`). El AOI se envía a un servidor administrado por Natural Capital Alliance, donde se realizan los cálculos de PUD y TUD. Por consiguiente, este modelo requiere conexión a Internet. El modelo puede ejecutarse con tres configuraciones:

#. Obtener un mapa de las tasas de visita en el Área de Interés. Proporcione un «Workspace» y un «Area of Interest», y no marque «Compute Regression». Los resultados incluyen «pud_results.gpkg», «tud_results.gpkg» y «regression_data.gpkg» (:ref:`rec-interpreting-results`).
#. Obtener un mapa de las tasas de visita y calcular una regresión con un conjunto de predictores. Proporcione un «Workspace» y un «Area of Interest», marque «Compute Regression» y proporcione la «Predictors Table» (:ref:`rec-data-needs`). Los resultados adicionales incluyen «regression_data.gpkg», «regression_coefficients.csv» y «regression_summary.txt» (:ref:`rec-interpreting-results`).
#. Estimar las tasas de visita para un escenario. Proporcione un «Workspace» y un «Area of Interest», marque «Compute Regression» y proporcione la «Predictors Table» y la «Scenario Predictors Table» (:ref:`rec-data-needs`). Los resultados adicionales incluyen «scenario_results.gpkg» (:ref:`rec-interpreting-results`).

El tiempo necesario para ejecutar el modelo varía según la extensión del AOI, el número de celdas de la cuadrícula y el número y tamaño de las capas de predictores. Recomendamos ejecutar primero el modelo sin calcular una regresión y comenzar con un tamaño de celda grande si se utiliza una cuadrícula para el AOI.

Tenga en cuenta que el servidor que realiza el análisis también registra la dirección IP de cada usuario.

.. _rec-interpreting-results:

Interpretación de los resultados
================================

Nuevos resultados del modelo
----------------------------
- :investspec:`recreation.recmodel_client workspace_dir`

Resultados del modelo
---------------------

+ **PUD_results.gpkg**: Las entidades de este geopackage de polígonos coinciden con el AOI original o con la versión del AOI dividida en cuadrícula, si se seleccionó la opción «Grid the AOI». Los atributos incluyen:

  + **PUD_YR_AVG** es el promedio de días-usuario de fotografías por año (:ref:`rec-userdays`). Corresponde al promedio de *PUD* descrito en Wood et al. (2013).

  + **PUD_JAN**, PUD_FEB, .... PUD_DEC es el promedio de días-usuario de fotografías para cada mes. Por ejemplo, si el intervalo de fechas es el predeterminado (2012-2017), PUD_JAN es el promedio de los días-usuario de fotografías de los seis meses de enero.

+ **PUD_monthly_table.csv**:

  + Esta tabla contiene el total de días-usuario de fotografías contabilizados en cada celda para cada mes del intervalo de fechas elegido. Cada fila de la tabla corresponde a una celda única de la cuadrícula del AOI o a un polígono. Las columnas representan los meses («2012-1» es enero de 2012 y «2017-12» es diciembre de 2017).

+ **TUD_results.gpkg**: Consulte la descripción de **PUD_results.gpkg**; sin embargo, en lugar de días-usuario de fotografías, este archivo contiene los recuentos de días-usuario de Twitter.

+ **TUD_monthly_table.csv**: Consulte la descripción de **PUD_monthly_table.csv**; sin embargo, en lugar de días-usuario de fotografías, este archivo contiene los recuentos de días-usuario de Twitter.

+ **regression_data.gpkg**: Polígonos del AOI con todas las variables necesarias para calcular una regresión, incluidos los atributos predictores y la variable de respuesta de días-usuario. Los campos incluyen:

    + **pr_PUD**: proporción de la suma de PUD_YR_AVG correspondiente a todas las entidades.

    + **pr_TUD**: proporción de la suma de TUD_YR_AVG correspondiente a todas las entidades.

    + **avg_pr_UD**: promedio de pr_PUD y pr_TUD. Esta variable se transforma mediante logit y luego se utiliza como variable de respuesta en el modelo de regresión.

    + Si se selecciona Compute Regression, habrá un campo para cada predictor definido en la Tabla de predictores. Los valores de esos campos se basan en la métrica definida en dicha tabla. (:ref:`rec-data-needs`: Tabla de predictores).

+ **regression_summary.txt** (resultado generado si se selecciona Compute Regression):

  + Este archivo de texto contiene los resultados del análisis de regresión. Incluye las estimaciones de :math:`\beta_p` para cada variable predictora (consulte :ref:`rec-how-it-works`). También contiene un valor «server id hash» que puede utilizarse para relacionar los resultados de PUD y TUD con los datos disponibles en el servidor. Si estos resultados se utilizan en una publicación, este hash debe incluirse para garantizar la reproducibilidad.

+ **regression_coefficients.csv** (resultado generado si se selecciona Compute Regression):

  + Resultado tabular de las estimaciones de los coeficientes, que también se incluyen en «regression_summary.txt».

+ **scenario_results.gpkg** (resultado generado si se proporciona una Tabla de predictores de escenario):

  + Este geopackage coincide con «regression_data.gpkg», pero sus campos proceden de los predictores definidos en la Tabla de predictores de escenario e incluye un campo adicional:

  + **pr_UD_est**: valor estimado de **avg_pr_UD** para cada polígono. Se estima utilizando los coeficientes de regresión de cada predictor incluidos en **regression_coefficients.csv**.

+ **natcap.invest...client-log...txt**

  + Este archivo de texto es el registro (*log*) que se genera automáticamente cada vez que se ejecuta el modelo. Puede ser útil para solucionar errores. En la parte superior del registro también se incluye un resumen de todos los valores de entrada seleccionados para esa ejecución del modelo.

.. _rec-references:

Referencias
===========

Adamowicz, WL, R Naidoo, E Nelson, S Polasky, J Zhang. 2011. Nature-based tourism and recreation. In: Kareiva P, G Daily, T Ricketts, H Tallis, S Polasky (eds) Natural Capital: Theory and Practice of Mapping Ecosystem Services. Oxford University Press, New York.

Balmford, A, J Beresford, J Green, R Naidoo, M Walpole, A Manica. 2009. A global perspective on trends in nature-based tourism. PLoS Biology 7: e1000144.

Hill, GW, PR Courtney. 2006. Demand analysis projections for recreational visits to countryside woodlands in Great Britain. Forestry 79: 18-200.

Loomis, JB, RB Richardson. 2006. An external validity test of intended behavior: comparing revealed preference and intended visitation in response to climate change. Journal of Environmental Planning and Management 49: 621-630.

Loureiro, ML, F Macagno, PA Nunes, R Tol. 2012. Assessing the impact of biodiversity on tourism flows: an econometric model for tourist behaviour with implications for conservation policy. Journal of Environmental Economics and Policy 1: 174-194.

Mills, AS, TN Westover. 1987. Structural differentiation: a determinant of park popularity. Annals of Tourism Research 14: 486-498.

Naidoo, R, WL Adamowicz. 2005. Biodiversity and nature-based tourism at forest reserves in Uganda. Environment and Development Economics 10: 159-178.

Neuvonen, M, E Pouta, J Puustinen, T Sievänen. 2010. Visits to national parks: effects of park characteristics and spatial demand. Journal for Nature Conservation 18: 224-229.

Puhakka, L, M Salo, IE Sääksjärvi. 2011. Bird diversity, birdwatching tourism and conservation in Peru: a geographic analysis. PLoS One 6: e26786.

Richardson, R, JB Loomis. 2005. Climate change and recreation benefits in an alpine national park. Journal of Leisure Research 37: 307-320.

Russell, R, AD Guerry, P Balvanera, RK Gould, X Basurto, KM Chan, S Klain, J Levine, J Tam. 2013. Humans and nature: how knowing and experiencing nature affect well-being. Annual Review of Environment and Resources 38: in press.

Trainor, SF, RB Norgaard. 1999. Recreation fees in the context of wilderness values. Journal of Park and Recreation Administration 17: 100-115.

Uyarra, MC, AR Watkinson, IM Côté. 2009. Managing dive tourism for the sustainable use of coral reefs: validating diver perceptions of attractive site features. Environmental Management 43: 1-16.

van der Walt, Stéfan, S. Chris Colbert, and Gaël Varoquaux. 2011. The NumPy Array: A Structure for Efficient Numerical Computation. Computing in Science & Engineering 13 (2): 22–30.

Williams, ID, NV Polunin. 2000. Differences between protected and unprotected reefs of the western Caribbean in attributes preferred by dive tourists. Environmental Conservation 27: 382-391.

Willox, AC, SL Harper, JD Ford, K Landman, K Houle, V Edge. 2012. "From this place and of this place:" climate change, sense of place, and health in Nunatsiavut, Canada. Social Science and Medicine 75: 538-547.

Wood, SA, AD Guerry, JM Silver, M Lacayo. 2013. `Using social media to quantify nature-based tourism and recreation <https://www.nature.com/articles/srep02976>`_. Scientific Reports 3: 2976.

World Travel and Tourism Council. 2012. `Travel and Tourism: Economic Impact <http://www.ontit.it/opencms/export/sites/default/ont/it/documenti/files/ONT_2012-03-23_02800.pdf>`_.
