.. _calibration_freshwater:

**************************************************
Calibración de los modelos de agua dulce de InVEST
**************************************************

Todos los modelos son simplificaciones y aproximaciones de procesos del mundo real muy complejos. Entonces, ¿qué tan precisos son los resultados de nuestros modelos? En realidad, no lo sabemos hasta que calibramos el modelo con datos observados. La calibración es el proceso de comparar los resultados del modelo con los datos observados y ajustar uno o más de los parámetros de entrada para que produzca resultados numéricos cercanos a los valores observados. Esto nos da mayor certeza sobre los resultados, algo especialmente importante si se desea utilizar los valores absolutos que genera el modelo para tomar decisiones o asignarles un valor.

La calibración es un proceso complejo y requiere mucho tiempo. Para llevarla a cabo se necesita:

+ Una serie temporal extensa de datos observados de alta calidad.
+ Capacidad para escribir scripts de Python.
+ Conocimientos de estadística.
+ También pueden ser muy útiles los conocimientos de hidrología y el conocimiento local.

Esta guía proporciona información para ayudarle a comenzar a calibrar los modelos de agua dulce de InVEST: Nutrient Delivery Ratio (NDR), Sediment Delivery Ratio (SDR), Annual Water Yield (AWY) y Seasonal Water Yield (SWY). No abarca todos los detalles ni está adaptada a las numerosas fuentes de datos observados que existen. Consulte la sección Referencias/Recursos adicionales para encontrar artículos que ofrecen orientación complementaria sobre modelos específicos.

.. freshwater_calibration_steps:

Pasos generales de calibración
===============================

1. Busque datos observados dentro de la cuenca hidrográfica de interés. Por lo general, estos datos provienen de estaciones de aforo.
	- Los datos de las estaciones de aforo suelen proceder de organismos gubernamentales, pero también pueden ser proporcionados por empresas de servicios relacionados con el agua, como operadores hidroeléctricos, u otras fuentes. Cuantas más estaciones de aforo de su área de estudio utilice, mayor será la confianza con la que podrá calibrar el modelo para que sea aplicable a toda esa área. Sin embargo, la calibración también será más difícil, porque estará evaluando de manera más exhaustiva el ajuste del modelo a la realidad.
	- Por lo general, los datos se presentan en algún formato tabular e incluyen fechas y valores observados de las mediciones específicas de nutrientes, sedimentos o caudal de agua que le interesan.

2. Revise los datos observados para comprobar que cuenten con las mediciones requeridas y que tengan una duración y un nivel de integridad adecuados.
	- **Mediciones requeridas:** valores que correspondan a los resultados del modelo que está calibrando. Por ejemplo, si está calibrando la exportación de sedimentos del modelo SDR, los datos de la estación de aforo deben incluir valores de carga de sedimentos o una combinación de datos de concentración de sedimentos y caudal de agua que permita calcular dicha carga. Los nutrientes suelen expresarse como concentración, por lo que también necesitará datos de caudal para calcular la carga de nutrientes. El rendimiento hídrico suele ser más sencillo: normalmente se expresa en metros cúbicos por segundo o en una unidad similar que puede convertirse fácilmente a las unidades de los resultados del modelo.
	- **Duración:** lo ideal es disponer de al menos 10 años de datos diarios continuos, que correspondan al período cubierto por los datos climáticos que se utilizan como entrada del modelo InVEST.
	- **Integridad:** no debe haber grandes vacíos en los datos. Si existe un pequeño vacío en un año, pero los datos de los demás años permiten cubrir ese período, no representa un problema. Sin embargo, si en la mayoría o en todos los años faltan datos de un mes o de una estación completos, es poco probable que se obtengan buenos resultados. Si faltan muchos datos de un año determinado, lo mejor es no utilizar ningún dato de ese año.
	- Conviene averiguar si alguien ya ha procesado los datos observados y los ha convertido en valores promedio mensuales o anuales. Esto no es habitual, pero, si tiene suerte, puede ahorrarle mucho tiempo.

3. Prepare los datos observados y resúmalos en un valor que pueda compararse directamente con los resultados del modelo.
	- Este proceso variará según la naturaleza de los datos con los que trabaje y el resultado del modelo que esté calibrando. Por ello, es difícil elaborar instrucciones detalladas o establecer generalizaciones.
	- Sea cual sea el procedimiento, deberá obtener un único valor (o, posiblemente, 12 valores mensuales para el modelo SWY) que represente la carga media anual de sedimentos, la carga de nutrientes o el rendimiento hídrico en cada estación de aforo, expresado en unidades que coincidan con las de los resultados del modelo.
		+ Los datos observados de nutrientes suelen expresarse como concentraciones (por ejemplo, mg/L). Para convertirlos a las unidades de kg/año que genera el modelo NDR, necesitará la concentración media de nutrientes y el caudal medio registrado en cada estación de aforo durante el mismo período. Luego, multiplique (*valor medio de la concentración de nutrientes x caudal medio*) y convierta el resultado a kilogramos.
		+ Los datos observados de sedimentos también pueden expresarse como concentraciones. En ese caso, puede seguir un procedimiento similar al utilizado para los nutrientes y convertirlos a las unidades de toneladas métricas/año que genera el modelo SDR. Si los datos observados corresponden a sólidos suspendidos totales (SST o TSS, por sus siglas en inglés), es posible que las unidades ya coincidan con las del modelo SDR y no sea necesaria ninguna conversión.
		+ El caudal de agua observado suele expresarse en unidades como metros cúbicos por segundo, que pueden convertirse fácilmente a valores mensuales (para el modelo SWY) o anuales (para los modelos SWY o AWY) con fines de comparación con el modelo.
		+ Para el modelo Seasonal Water Yield, podría calcular 12 promedios que representen cada mes del año para una estación de aforo determinada. Sin embargo, tendría que decidir cómo distribuir entre los meses el resultado anual del flujo base. Como el resultado del flujo base ya está concebido para utilizarse como un índice y se presenta en términos anuales, distribuirlo entre meses o estaciones es una aproximación considerable y añade otro nivel de incertidumbre. Aun así, existen varias formas de calcular el flujo base mensual:
			1. Divida el resultado anual del flujo base entre 12 y utilice el mismo valor o ráster para cada mes. Es el método más sencillo y quizá el más adecuado para lugares donde las precipitaciones no son muy estacionales.
			2. Distribuya el resultado anual del flujo base proporcionalmente a la precipitación de cada mes. Este método es algo más complejo, pero quizá sea más adecuado en lugares donde las precipitaciones presentan una marcada estacionalidad.
			3. En la página 5 del suplemento de `Mandle et al. 2025 <https://static-content.springer.com/esm/art%3A10.1038%2Fs43247-025-02254-9/MediaObjects/43247_2025_2254_MOESM2_ESM.pdf>`_ se describe un método mucho más sofisticado.

4. Compare los valores observados calculados con los resultados del modelo.
	+ Resuma los resultados del modelo dentro de la cuenca hidrográfica que drena hacia el punto donde se tomaron los datos observados. Consulte la siguiente sección, «Delimitación de cuencas hidrográficas», para obtener más información.
	+ Es poco probable que el resultado del modelo coincida con los valores observados; incluso puede ser muy diferente. Recuerde que se trata de modelos sencillos y que, en cualquier modelo —incluso en los más complejos—, suele ser necesario realizar una calibración para acercar los resultados a la realidad. La calibración es indispensable para tener confianza en los valores absolutos.

5. **Realice un análisis de sensibilidad para determinar qué parámetros del modelo tienen mayor efecto sobre los resultados.** Estos serán los parámetros que posteriormente se ajustarán durante la calibración.
	+ El análisis de sensibilidad requiere ejecutar el modelo muchas veces, por lo que resulta más eficiente hacerlo mediante scripts. Consulte la siguiente sección, «Configuración del entorno de scripting de Python de InVEST», para obtener información sobre cómo comenzar.
	+ Varíe los valores de la tabla biofísica (relacionados, por ejemplo, con el mapa de uso y cobertura del suelo, como `usle_c` en SDR o `Kc` en AWY), así como los valores de los parámetros globales del modelo (como Threshold Flow Accumulation, el parámetro `gamma` de SWY o el parámetro `IC0` de SDR), modificando un parámetro a la vez y dentro de rangos razonables, según los intervalos publicados en la literatura. Si no dispone de rangos publicados, puede comenzar variando los valores, por ejemplo, entre -50 % y +50 % del valor predeterminado, en incrementos del 10 % (véase la Tabla 1 de Hamel et al. 2015). También puede variar las capas de entrada espaciales (como la precipitación) si dispone de diferentes fuentes que cubren el área de interés y presentan diferencias significativas.
	+ Ejecute el modelo con los parámetros de referencia y, luego, con cada una de las distintas configuraciones de parámetros. Registre los resultados de todas las ejecuciones, agregados dentro de la cuenca hidrográfica que drena hacia la ubicación de cada estación de aforo que haya proporcionado datos observados. La mayoría de estos modelos realizan la agregación por usted mediante la capa de cuencas hidrográficas que proporcione como entrada.
	+ Los parámetros que tengan mayor efecto sobre los resultados del modelo (en comparación con los valores de referencia) deberán utilizarse para la calibración.

6. Una vez seleccionados los parámetros que tienen mayor efecto, realice otra serie de ejecuciones del modelo ajustando esos parámetros dentro de un rango de valores. Modifique todos los parámetros al mismo tiempo, de manera que cada ejecución del modelo utilice una combinación diferente de valores.
	+ Nuevamente, lo más conveniente será hacerlo mediante un script, ya que puede haber muchas combinaciones de parámetros. Registre los resultados de todas las ejecuciones, agregados dentro de la cuenca hidrográfica que drena hacia la ubicación de la estación de aforo donde se realizaron las observaciones.
	+ Cuantos más lugares (es decir, observaciones de estaciones de aforo) utilice para comparar los resultados del modelo, más información tendrá sobre el grado de calibración alcanzado. Por supuesto, cuantos más lugares tenga para comparar, más difícil será la calibración, pero esto se debe únicamente a que estará evaluando de manera más exhaustiva el ajuste del modelo a la realidad.

7. Utilice métodos estadísticos para comparar los resultados del paso 6 con los datos observados. Seleccione el conjunto de parámetros del modelo que produzca resultados suficientemente cercanos a los valores observados.
	+ Esto puede ser tan sencillo como calcular el porcentaje de error mediante la siguiente fórmula: *((valor_modelado - valor_observado) / valor_observado) * 100*

	+ Los métodos estadísticos más sofisticados, como las comparaciones de R cuadrado y los valores p, pueden ofrecer comparaciones más sólidas si está familiarizado con esas técnicas.

8. El conjunto de parámetros del modelo seleccionado en el paso 7 ya puede utilizarse para evaluar escenarios, calcular valores o realizar otros procesos que se beneficien de la mayor precisión del modelo calibrado.

¿Qué ocurre si, a pesar de realizar el proceso de análisis de sensibilidad y calibración, los valores calibrados siguen siendo inaceptablemente diferentes de los datos observados?

* Revise las unidades de las entradas del modelo y las unidades de los valores observados, y asegúrese de que todas sean correctas.

* Recuerde que los modelos de agua dulce de InVEST son muy sencillos y quizá no incluyan procesos que tengan un efecto importante sobre la cantidad o la calidad del agua en su área de estudio. Revise las secciones **Cómo funciona el modelo** y **Limitaciones** del capítulo correspondiente a ese modelo en la Guía del usuario para obtener información más específica. Es posible que el modelo simplemente no sea adecuado para su área de estudio. En ese caso, puede considerar utilizar otro modelo más complejo o que incluya específicamente los procesos dominantes de su cuenca hidrográfica.


.. freshwater_calibration_watersheds:

Delimitación de cuencas hidrográficas
=====================================

Al calibrar los modelos de agua dulce con datos observados, debemos delimitar la cuenca hidrográfica que drena hacia el punto donde se encuentra la estación de aforo que registró los datos observados. Luego podemos resumir el resultado pertinente del modelo (como la exportación de sedimentos) dentro de esa cuenca y comparar ese resumen con el valor de los datos observados.

Existen muchas herramientas para delimitar cuencas hidrográficas y puede utilizar la que le resulte más cómoda. InVEST incluye la herramienta :ref:`DelineateIt <delineateit>`, que permite crear cuencas hidrográficas de manera sencilla y eficaz.

Independientemente de la herramienta que utilice, por lo general se requiere, como mínimo, un ráster de modelo digital de elevación (DEM) y una capa vectorial (por ejemplo, un shapefile o un geopackage) que contenga la ubicación de los puntos que se utilizarán como salidas de la cuenca. En este caso, la salida será la ubicación de una estación de aforo que haya recopilado los datos observados. El DEM debe ser el mismo que se utiliza como entrada del modelo de agua dulce de InVEST que está calibrando.

Después de ejecutar la herramienta de delimitación, examine cuidadosamente la cuenca hidrográfica resultante para asegurarse de que sea correcta. Un problema frecuente es que la cuenca delimitada sea muy pequeña. Esto suele deberse a que el punto de salida no está ubicado directamente sobre un cauce generado por la herramienta de delimitación. Para solucionarlo, muchas herramientas cuentan con una función de «ajuste» (*snap*), que permite especificar una distancia alrededor del punto de salida dentro de la cual la herramienta debe buscar un cauce. Si encuentra uno dentro de esa distancia, la herramienta ajusta el punto al cauce y delimita la cuenca con mayor precisión. Si la herramienta no dispone de esta función, puede mover manualmente el punto para situarlo sobre la red de drenaje generada por la herramienta.

Una vez generada correctamente la cuenca hidrográfica, se utiliza una herramienta SIG, como Estadísticas zonales (*Zonal Statistics*), para sumar el ráster del resultado pertinente del modelo (por ejemplo, la exportación de sedimentos o de nutrientes) dentro de la cuenca. Luego, este valor resumido se compara con el valor de los datos observados. Como alternativa, puede utilizar la cuenca hidrográfica generada como entrada del modelo, que realizará la agregación por usted y creará una capa vectorial cuya tabla contendrá los valores resumidos.

Configuración del entorno de scripting de Python de InVEST
==========================================================

Hay guías disponibles para instalar el paquete de Python `natcap.invest` y ejecutar scripts para los modelos:

+ Instalación de natcap.invest: https://invest.readthedocs.io/en/latest/installing.html
+ Configuración del entorno de Python y ejecución de scripts: https://invest.readthedocs.io/en/latest/scripting.html#setting-up-your-python-environment


Scripts de ejemplo
==================

InVEST Workbench puede crear un script básico de Python para cualquier modelo. El script importa las bibliotecas necesarias, configura el registro de eventos (*logging*), define las entradas del modelo y lo ejecuta con esas entradas. Es útil comenzar con este script y ampliarlo para crear su flujo de trabajo de análisis de sensibilidad y calibración. Para crear el script, abra una pestaña de un modelo en Workbench, seleccione **Save as…** en la barra de herramientas de la izquierda y, a continuación, seleccione **Python script**.

+ `Script básico para SDR <https://gist.github.com/newtpatrol/07dbc0b689ad510db3a94dcdad728814>`_, generado por InVEST Workbench.
+ `Script para ejecutar varias veces SDR con distintas tablas biofísicas <https://gist.github.com/newtpatrol/707ee70acb012e5e8b8450ec59283d50>`_, ejecutado dentro de un bucle `for`.
+ `Otro script de ejemplo <https://gist.github.com/newtpatrol/e983e35805cec27ad36f6570f1623ba7>`_ que ejecuta NDR en un bucle con distintos valores de `kb`, Threshold Flow Accumulation y otros valores globales del modelo, además de modificar los valores de la tabla biofísica. Calcula los errores de cada ejecución y escribe los resultados en una tabla. Tenga en cuenta que corresponde a una versión anterior de InVEST, pero sigue siendo un ejemplo útil para configurar las ejecuciones de parámetros del análisis de sensibilidad.

Valladares-Castellanos et al. 2024 realizaron un estudio detallado de calibración y validación del modelo NDR en Puerto Rico, utilizando datos de monitoreo de acceso abierto. En el artículo citado presentan su marco metodológico, flujo de trabajo y código R, que pueden adaptarse a otros lugares: `Valladares-Castellanos et al. 2024 <https://doi.org/10.1016/j.scitotenv.2024.175111>`_.

Referencias/Recursos adicionales
================================

**Orientación general sobre la evaluación de la incertidumbre en el análisis de los servicios ecosistémicos:**

Hamel, P. & Bryant, B. 2017. Uncertainty assessment in ecosystem services analyses: Seven challenges and practical responses. Ecosystem Services, Volume 24. https://doi.org/10.1016/j.ecoser.2016.12.008

**Calibración del modelo NDR:**

Hamel, P., Guswa, A.J. 2015. Uncertainty Analysis of the InVEST 3.0 Nutrient Model: Case Study of the Cape Fear Catchment, NC. Hydrology and Earth System Sciences Discussion 11:11001-11036. https://doi.org/10.5194/hess-19-839-2015

Valladares-Castellanos, M., de Jesús Crespo, R., Xu, Y. J., Douthat, T. H. 2024. A framework for validating watershed ecosystem service models in the United States using long-term water quality data: Applications with the InVEST Nutrient Delivery (NDR) model in Puerto Rico, Science of The Total Environment, Volume 949, 2024, 175111, ISSN 0048-9697. https://doi.org/10.1016/j.scitotenv.2024.175111

**Calibración del modelo SDR:**

Hamel, P., Chaplin-Kramer, R., Sim, S., Mueller, C. 2015. A new approach to modeling the sediment retention service (InVEST 3.0): Case study of the Cape Fear catchment, North Carolina, USA. Science of the Total Environment 524–525 (2015) 166–177. https://doi.org/10.1016/j.scitotenv.2015.04.027

Mandle, L., Angarita, H., Moreno, J., Goldstein, J.A., Melo L., S.F., Echeverri, A., Rojas, N., Villalba, F.D. 2025. Natural capital accounting reveals ecosystems' role in water and energy security in Colombia's Sinú Basin, Communications Earth & Environment (2025). https://doi.org/10.1038/s43247-025-02254-9

**Calibración del modelo SWY:**

Hamel, P., Valencia, J., Schmitt, R., Shrestha, M., Piman, T., Sharp, R.P., Francesconi, W., Guswa, A.J., 2020. Modeling seasonal water yield for landscape management: Applications in Peru and Myanmar. Journal of Environmental Management 270, 110792. https://doi.org/10.1016/j.jenvman.2020.110792
