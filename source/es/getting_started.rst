.. _getting-started:

************
Cómo empezar
************

.. _installing-on-win:

Instalación de InVEST Workbench en su ordenador Windows
=======================================================

Descargue el instalador de InVEST desde https://naturalcapitalproject.stanford.edu/software/invest. El ejecutable se llamará "InVEST_<versión>_Setup.exe". Haga doble clic en este .exe para ejecutar el instalador.

La primera pantalla le pide que confirme el Acuerdo de Licencia, haga clic en **Acepto** para continuar. 

Aparecerá la pantalla Opciones de instalación. Puede elegir instalar InVEST solo para usted o para todos los usuarios. Haga clic en **Siguiente**.

A continuación, elija la carpeta donde se instalará Workbench. Haga clic en **Instalar**.

Hay algunas cosas que pueden ser de particular interés en la carpeta de instalación de Workbench: 

+ Una carpeta **resources/documentation**, que contiene la Guía del usuario de InVEST en formato HTML en inglés, español y chino.
+ Una carpeta **resources/invest**, que contiene el código Python compilado que compone el conjunto de herramientas InVEST.
+ **InVEST <version> Workbench.exe**, que es el ejecutable principal utilizado para lanzar Workbench.
+ **Uninstall InVEST <version> Workbench.exe**, que desinstalará Workbench.

Además, se añadirá un acceso directo a su menú de inicio de Windows en *Todos los programas -> InVEST <versión> Workbench*.

También hay datos de muestra disponibles para todos los modelos. Para instalarlos, inicie Workbench y vaya a **Configuración** (el icono del engranaje en la esquina superior derecha) **-> Descargar datos de muestra**.
Además, los accesos directos a todas las aplicaciones independientes de InVEST se añadirán a su menú de inicio de Windows en *Todos los programas -> InVEST |versión|*.

Instalación avanzada
--------------------

El instalador de InVEST para Windows tiene una serie de opciones de instalación para varios casos de uso, incluyendo la instalación silenciosa y el uso de datos de muestra locales.  Para ver las opciones disponibles, descargue el instalador, abra un indicador CMD en el directorio que contiene el instalador descargado y escriba:


.. code-block:: text

    .\InVEST_<version>_x64_Setup.exe /?


.. _installing-on-mac:

Instalación de InVEST Workbench en su Mac
=========================================

.. note::
    En Mac OS 10.13 "High Sierra", se requiere InVEST 3.4.0 o posterior.

    En Mac OS 11 "Big Sur", se requiere InVEST 3.9.0 o posterior.

    Los resultados numéricos de los binarios de Mac pueden diferir ligeramente (normalmente dentro de 1e-4) de los resultados de los binarios de Windows.  Por esta razón, consideramos que los binarios de InVEST son "inestables", pero deberían seguir proporcionando resultados razonables.  Como siempre, si algo no parece funcionar, por favor, hágalo saber en los foros: https://community.naturalcapitalproject.org/

Descargue el archivo de imagen de disco de InVEST desde https://naturalcapitalproject.stanford.edu/software/invest.  El archivo se llamará "InVEST-<versión>.dmg".  Contiene una copia del ejecutable de InVEST. Tenga en cuenta que, a partir de la versión 3.9.0, la guía de uso
y el archivo HISTORY.rst ya no se incluyen en la distribución para Mac; acceda a estos recursos en línea.

Para instalar:

  1. Haga clic con el botón derecho del ratón en el archivo descargado ``InVEST-<versión>.dmg``, y en el menú contextual, seleccione *Abrir*.
  2. En el cuadro de diálogo que aparece, haga clic en *Abrir* una vez más.
  3. La imagen de disco se abrirá y le indicará que arrastre la aplicación InVEST a su carpeta de aplicaciones. Este paso es esencial para que InVEST funcione correctamente.
  4. Vaya a su carpeta de aplicaciones y abra la aplicación InVEST desde allí.
  5. La primera vez que abra la aplicación InVEST, tendrá que hacer lo siguiente:
       1. Haga clic con el botón derecho del ratón en ``InVEST``, y en el menú contextual, seleccione *Abrir*.
       2. En el cuadro de diálogo que aparece, haga clic en *Abrir* una vez más.
  6. En el cuadro de diálogo del lanzador, seleccione el modelo que desea ejecutar y haga clic en *Lanzar*.

También hay datos de muestra disponibles para todos los modelos. Para instalarlos, inicie Workbench y vaya a **Configuración -> Descargar datos de muestra**.

A diferencia del instalador de Windows, la distribución para Mac no incluye la guía del usuario.  Esta puede encontrarse en línea en https://naturalcapitalproject.stanford.edu/software/invest.


Tutorial de inicio rápido de InVEST
===================================

Este tutorial de alto nivel le da una idea de las principales actividades involucradas en la realización de un análisis de servicios e	cosistémicos utilizando InVEST. No es un recurso técnico exhaustivo paso a paso, sino que proporciona pasos, consejos y una idea general del tiempo necesario para ejecutar un modelo InVEST. Aunque los requisitos de tiempo varían mucho de un proyecto a otro, se proporciona una estimación general para cada paso: *Bajo* = generalmente requiere menos de un día; *Medio* = menos de una semana; *Alto* = una semana o más.

1. **Instale InVEST**
	- Descargue InVEST e instálelo como se detalla en las secciones :ref:`installing-on-win` o :ref:`installing-on-mac` de este capítulo.
	- Se recomienda instalar también los datos de muestra que ofrece el instalador de InVEST.
	- Tiempo necesario para instalar InVEST: Bajo
2. **Lea en la guía de uso el capítulo de cada modelo de interés**
	- Para cada modelo, la guía de uso contiene los antecedentes, las ecuaciones, los requisitos de datos, las descripciones de los resultados y las recomendaciones sobre las fuentes de datos y los métodos globales.
	- Este es el primer lugar al que hay que acudir con preguntas sobre modelos y requisitos de datos.
	- Tiempo necesario para leer un capítulo de modelo: Bajo
3. **Examine los datos de la muestra del modelo**
	- Se proporcionan datos de muestra para todos los modelos, disponibles para su instalación por medio de la configuración de Workbench de InVEST o descargables por separado.
	- Examine los datos espaciales con un software SIG y los datos tabulares con una hoja de cálculo o un editor de texto.
	- Utilice estos datos para hacerse una idea de los inputs y resultados y ejecutar el modelo.
	- Utilícelos como ejemplo para formatear sus propios datos.
	- Para más información, consulte la sección :ref:`using-sample-data` de este capítulo.
	- Tiempo necesario para probar un modelo con datos de muestra: Bajo
4. **Cree sus propios datos para el caso de línea de base**
	- Reúna los inputs espaciales y no espaciales requeridos por el modelo.
	- Procese los datos recogidos para su área de interés, de modo que cada input cumpla los requisitos de InVEST.
	- La mayor parte de este tratamiento se realizará con programas de SIG.
	- Muchos modelos también requieren una amplia búsqueda bibliográfica de determinados parámetros.
	- Consulte el capítulo de la guía de uso del modelo y los datos de muestra para conocer los requisitos y ejemplos de cómo deben ser los conjuntos de datos.
	- Consulte también la sección :ref:`formatting-data` de este capítulo para obtener consejos generales.
	- La cantidad de procesamiento variará mucho, dependiendo del input del modelo en particular y del formato de la fuente original.
	- Lo mejor es buscar fuentes de datos más locales, pero si no están disponibles, generalmente se dispone de capas y valores globales más gruesos. El Apéndice en la guía de uso para cada modelo proporciona direcciones a algunas fuentes de datos globales.
	- Tiempo necesario para crear los datos de un modelo: Alto.
5. **Crear escenarios futuros**
	- El análisis de los escenarios es opcional, pero se suele hacer.
	- Los escenarios suelen basarse en la alteración de los mapas de uso/cobertura del suelo, de los hábitats o de la gestión del suelo para reflejar los impactos de una intervención propuesta o del cambio climático.
	- La creación de escenarios puede llevar mucho tiempo si, por ejemplo, se utiliza un proceso con las partes interesadas o se requiere la elaboración de modelos climáticos.
	- Tiempo necesario para crear escenarios: Medio a alto.
6. **Ejecute el modelo**
	- Utilice la interfaz de uso de InVEST o la línea de comandos para ejecutar el modelo con sus datos.
	- Para más información, consulte la sección :ref:`running-models` de este capítulo.
	- Tiempo requerido: De bajo a medio, dependiendo del tamaño y la complejidad de los datos de input y del modelo que se ejecute. Se requiere más tiempo para los datos de alta resolución y/o áreas de interés grandes.
7. **Examine los resultados del modelo**
	- Examine críticamente los resultados utilizando el programa de  SIG: ¿tienen sentido los patrones y los valores?
	- Los patrones inexplicables o los valores anormalmente altos o bajos podrían indicar problemas con los datos de input.
	- Tiempo necesario: De bajo a medio.
8. **Calibre el modelo**
	- Opcional, no necesariamente necesario para un análisis de selección de alto nivel y/o si los datos de campo no están disponibles para la validación.
	- Sin embargo, es importante hacer la calibración si se hace una valoración con los resultados del modelo.
	- Recoja y procese los datos observados correspondientes a los esultados del modelo InVEST de interés. Por ejemplo, la carga de sedimentos de una estación de control en la toma de un embalse.
	- Ajuste los inputs del modelo para producir una concordancia entre los resultados modelizados y los datos observados.
	- La calibración puede ir acompañada de un análisis de sensibilidad, para determinar qué parámetros tienen el mayor efecto sobre los resultados. Los parámetros más sensibles son buenas opciones para el ajuste de la calibración.
	- Tiempo requerido: Medio a alto.
9. **Incorpore a los beneficiarios**
	- Vincule los resultados del modelo a las personas o a otro tipo de beneficiario. Aquí es donde se convierte en un *servicio* ecosistémico.
	- Recoja y preprocese datos sobre la ubicación de las personas, infraestructuras u otros beneficiarios de interés.
	- Combine los resultados del modelo InVEST con los datos de los beneficiarios, lo que generalmente se hace con un programa de SIG.
	- Tiempo necesario: Medio.
10. **Valoración**
	- La valoración de los servicios ecosistémicos, ya sea monetaria o no monetaria, suele ser compleja y depende del contexto.
	- Recoja los datos económicos relacionados con el servicio y el beneficiario que esté analizando.
	- Calibre los resultados de su modelo antes de utilizarlos para la valoración.
	- Tiempo necesario: Medio a alto.
11. **Comunicación de los resultados**
	- Una vez que tenga los resultados de InVEST, creará mapas, tablas, gráficos, etc., dependiendo de lo que sea necesario para comunicar sus resultados a su audiencia.
	- También se puede hacer un posprocesamiento de los resultados. Por ejemplo, puede mostrar un mapa de áreas protegidas superpuesto a un mapa de resultados de InVEST. O combinar varios mapas de servicios ecosistémicos en un mapa de "puntos calientes" de mayor prestación de servicios combinados. O agregar los resultados dentro de un área de interés.
	- Recuerde que debe elegir los colores y los símbolos para que sean fáciles de leer por un público amplio, intuitivos de interpretar y que representen con precisión los resultados.
	- Tiempo requerido: De bajo a medio, dependiendo de la complejidad de las necesidades del proyecto.


Conocimientos de SIG
====================

**Para muchos de los pasos del análisis de InVEST se necesitan conocimientos intermedios de sistemas de información geográfica (SIG), especialmente para crear los inputs del modelo y trabajar con sus resultados.**

Esta guía da por sentado que usted tiene los conocimientos necesarios en materia de SIG, y en general no proporciona instrucciones relacionadas con la visualización o el procesamiento de datos mediante el software de SIG. Puede utilizar cualquier software geoespacial con el que se sienta cómodo, siendo QGIS y ArcGIS los más comunes. Hay muchas clases y tutoriales disponibles para aprender las habilidades y el software GIS, y recomendamos que se sienta cómodo con estos conceptos y herramientas antes de empezar a trabajar con InVEST.

A continuación se presentan algunos ejemplos de los tipos de tareas SIG que suelen formar parte de un análisis InVEST. Esta lista no es exhaustiva:

+ Ver y navegar por datos ráster, vectoriales y tabulares

+ Simbolizar datos ráster y vectoriales

+ Reproyectar capas de datos a un sistema de coordenadas común

+ Recortar capas de datos a un área de interés

+ Convertir vectores en rásters y rásters en vectores

+ Crear nuevas capas de puntos, líneas o polígonos

+ Editar tablas de atributos vectoriales

+ Realizar una variedad de matemáticas ráster

+ Reclasificar valores ráster

+ Remuestrear rásters

Véase también la sección :ref:`working-with-the-DEM` de este capítulo, que ofrece algunos detalles sobre el procesamiento SIG de los datos del modelo digital de elevación (MDE) para su uso en los modelos SDR, NDR, rendimiento hídrico estacional, calidad escénica y vulnerabilidad costera.

Herramientas independientes de InVEST
=====================================

Todos los modelos de InVEST se ejecutan en una plataforma totalmente de código abierto, mientras que históricamente el conjunto de herramientas era una colección de scripts de ArcGIS. La nueva interfaz no requiere ArcGIS y los resultados pueden explorarse con cualquier herramienta SIG, como `ArcGIS <https://www.esri.com/en-us/home>`_, `QGIS <https://qgis.org/en/site/>`_ y otras. A partir de InVEST 2.3.0, el conjunto de herramientas ha tenido versiones independientes de los modelos disponibles en el menú de inicio de Windows después de la instalación, en *Todos los programas -> InVEST |versión|*.  Las versiones independientes están actualmente disponibles para todos los modelos. Las versiones de ArcGIS de los modelos de InVEST ya no son compatibles.

Versiones anteriores de InVEST
==============================
Las versiones más antiguas de InVEST pueden encontrarse en http://data.naturalcapitalproject.org/invest-releases/deprecated_models.html. Tenga en cuenta que muchos modelos fueron obviados debido a problemas científicos críticos no resueltos, y le recomendamos encarecidamente que utilice la última versión de InVEST.

.. _using-sample-data:

Uso de los datos de muestra
===========================

InVEST viene con datos de muestra como orientación para formatear sus datos y empezar a entender cómo funcionan los modelos. Antes de iniciar su propio análisis, le recomendamos fuertemente que descargue los datos de muestra del modelo o modelos que le interesen, examine las entradas en un SIG, ejecute el modelo utilizando los datos de muestra y examine los resultados en un SIG.

Los datos de muestra se encuentran en subcarpetas separadas dentro de la carpeta de instalación de InVEST. Por ejemplo, los conjuntos de datos de muestra para el modelo de polinización se encuentran en \\{InVEST install folder}\\sample_data\\pollination\\, y los del modelo de carbono en \\{InVEST install folder}\\sample_data\\carbon\\. Para probar los modelos, puede crear una carpeta de espacio de trabajo llamada "output" dentro de las carpetas de datos de muestra para guardar los resultados del modelo. Una vez que esté trabajando con sus propios datos, necesitará crear un espacio de trabajo y carpetas de datos de input para guardar sus propios datos y resultados. También tendrá que redirigir la herramienta para acceder a sus datos y espacio de trabajo.

Si se ejecuta en Windows, los datos de muestra pueden instalarse al mismo tiempo que se instala InVEST, o los conjuntos de datos pueden descargarse individualmente del `sitio web de InVEST <https://naturalcapitalproject.stanford.edu/software/invest>`_.

.. _formatting-data:

Formateo de los datos
=====================

Antes de ejecutar InVEST se deben formatear los datos. Si bien los capítulos siguientes de esta guía describen cómo preparar los datos de input para cada modelo, hay varias pautas de formato comunes a todos los modelos:

+ Los nombres de los archivos de datos no deben tener espacios (por ejemplo, un archivo ráster debe llamarse "landuse.tif" en lugar de "land use.tif").

+ Para los datos ráster, se prefieren los TIFF por su facilidad de uso, pero también puede utilizar IMG o ESRI GRID.

+ Si utiliza rásters en formato ESRI GRID, sus nombres de conjuntos de datos no pueden tener más de 13 caracteres y el primer carácter no puede ser un número. Los rásters TIFF e IMG no tienen la limitación de la longitud del nombre del archivo. Cuando utilice ESRI GRID como input a la interfaz del modelo, utilice el archivo "hdr.adf".

+ Los datos espaciales deben estar en un sistema de coordenadas proyectadas (como UTM), no en un sistema de coordenadas geográficas (como WGS84), y todos los datos de input para una determinada ejecución del modelo deben estar en el mismo sistema de coordenadas proyectadas. Si sus datos no están proyectados, InVEST dará errores o resultados incorrectos. (Hay excepciones a esto, como la Vulnerabilidad Costera - vea el capítulo del modelo en la guía de uso para los requisitos específicos).

+ Si bien los modelos de InVEST 3.0 son ahora muy eficientes en cuanto a manejo de memoria, el tiempo que se tarda en ejecutar los modelos sigue viéndose afectado por el tamaño de los conjuntos de datos ingresados. Si el área de interés es grande y/o utiliza rásters con un tamaño de celda pequeño, esto aumentará tanto el uso de memoria como el tiempo que se tarda en ejecutar el modelo. Si son demasiado grandes, se producirá un error de memoria. Si esto ocurre, intente reducir el tamaño de su área de interés, o utilizar datos de input de resolución más gruesa.

+ De la misma manera, la cantidad de espacio en disco que utiliza el modelo está en proporción a la resolución de los datos ingresados. Si el área de interés es grande y/o utiliza rásters con un tamaño de celda pequeño, esto aumentará la cantidad de espacio en disco necesario para almacenar los resultados intermedios y finales del modelo. Si no se dispone de suficiente espacio en disco, el modelo devolverá un error.

+ Ejecutar los modelos con los archivos de datos de input abiertos en otro programa puede causar errores. Asegúrese de que los archivos de datos no están siendo utilizados por otro programa para evitar problemas de acceso a los datos.

+ Opciones regionales y de idioma: Algunas opciones de idioma provocan errores al ejecutar los modelos.  Por ejemplo, los ajustes que utilizan la coma (,) para los decimales en lugar del punto (.) provocan errores en los modelos.  Para solucionarlo, cambie la configuración regional del ordenador al inglés.

+ A medida que se ejecutan los modelos, puede ser necesario cambiar los valores de las tablas de inputs. Esto se suele hacer con un programa de hoja de cálculo como Excel o un editor de texto como Notepad++. Las tablas de inputs deben estar en formato CSV. Si trabaja en Excel, asegúrese de guardar el archivo en formato CSV. Asegúrese de hacerlo utilizando una de las siguientes codificaciones: ASCII, UTF-8 o Signed UTF-8.  El uso de cualquier otra codificación (como Latin-1) dará lugar a una representación incorrecta del texto en los archivos de resultadosy podría hacer que los modelos fallaran con un error.

+ Algunos modelos requieren directrices específicas para la denominación de los archivos de datos (por ejemplo, el modelo de Calidad del Hábitat) y los nombres de los campos (columnas), que se definen en el capítulo para cada modelo en la guía de uso. Siga estas pautas cuidadosamente para asegurarse de que su conjunto de datos es válido, o el modelo dará un error.

+ Recuerde *utilizar los conjuntos de datos de muestra como orientación para formatear sus datos*.

.. _running-models:

Ejecute los modelos
===================

Estará listo para ejecutar un modelo de InVEST cuando haya preparado sus datos según las instrucciones del capítulo del modelo correspondiente y haya instalado la última versión de InVEST.

Para comenzar:

+ Revise los datos introducidos. Visualice los datos espaciales en un SIG, asegúrese de que los valores parecen correctos, de que no faltan datos donde deberían rellenarse, de que todas las capas están en el mismo sistema de coordenadas proyectado, etc. Vea los datos de la tabla en una hoja de cálculo o editor de texto, asegúrese de que los valores parecen correctos, los nombres de las columnas son correctos y que se guardan en formato CSV.

+ Inicie el modelo que desea ejecutar (por ejemplo, Carbono), y añada sus datos de input a cada campo de la interfaz de usuario. Puede arrastrar y soltar las capas en el campo, o hacer clic en el icono de Archivo a la derecha de cada campo para navegar hasta sus datos.

+ Las entradas cuya ruta conduzca a un archivo inexistente o a un archivo con formato incorrecto se marcarán con una "X" roja a la derecha del nombre de la entrada y el cuadro de entrada se marcará en rojo. Debajo de la entrada habrá una breve descripción del problema. Por ejemplo, "La entrada es obligatoria pero no tiene valor" significa que esta entrada es obligatoria, pero aún no la ha rellenado con información válida. El modelo no se ejecutará si hay alguna X roja.

+ Tenga en cuenta que cada herramienta tiene un lugar para introducir un Sufijo, que es una cadena que se añadirá a los nombres de archivo de resultado como *<nombre de archivo>_Sufijo*. La adición de un sufijo único evita que se sobrescriban los archivos producidos en iteraciones anteriores. Esto es particularmente útil si está ejecutando múltiples escenarios, de modo que cada nombre de archivo puede indicar el nombre del escenario.

+ Cuando todos los campos requeridos estén rellenados y no haya ninguna X roja, haga clic en el botón **Ejecutar** de la interfaz.

+ El tiempo de procesamiento variará en función del script y de la resolución y extensión de sus conjuntos de datos de entrada.  Cada modelo abrirá una ventana que mostrará el progreso del script. Asegúrese de examinar la ventana de salida en busca de mensajes útiles y errores. Esta información de progreso también se escribirá en un archivo en el Espacio de Trabajo llamado *InVEST-natcap.invest.<model name>-log-<timestamp>.txt*. Si necesita ponerse en contacto con NatCap para obtener ayuda en caso de error, envíe siempre este archivo de registro ya que ayudará con la depuración. Consulte también la sección :ref:`support-and-error-reporting` de este capítulo para obtener más información.

+ Los resultados del modelo se encuentran en la carpeta **Espacio de trabajo**. Los resultados principales están generalmente en el nivel superior del Espacio de Trabajo. También hay una carpeta "intermedia" que contiene algunos de los archivos adicionales generados al realizar los cálculos. Aunque normalmente no es necesario mirar los resultados intermedios, a veces es útil cuando se está depurando un problema o tratando de entender mejor cómo funciona el modelo. Leer el capítulo del modelo y mirar los archivos intermedios correspondientes puede ser una buena manera de entender y criticar sus resultados. Los capítulos correspondientes a cada modelo en esta guía proporcionan una descripción de estos archivos resultantes.

Una vez completado el script con éxito, puede ver los resultados espaciales añadiéndolos desde el Espacio de trabajo a su SIG. Es importante examinar los resultados con detenimiento y críticamente. ¿Tienen sentido los valores? ¿Tienen sentido los patrones? ¿Comprende por qué algunos lugares tienen valores más altos y otros más bajos? ¿Cómo influyen las capas de entrada y los parámetros en los resultados? Si le preocupan los resultados y quiere preguntar en el foro de usuarios, revise primero estas preguntas. Muy a menudo, los valores inesperadamente altos o bajos, o las áreas en las que faltan datos, pueden explicarse fácilmente observando las unidades, los valores o los datos que faltan en sus capas de entrada.

.. _support-and-error-reporting:

Asistencia y notificación de errores
====================================

Si se encuentra con algún problema al ejecutar los modelos o tiene alguna pregunta sobre su teoría, datos o aplicación que la Guía del usuario no cubra, visite el foro de ayuda al usuario en https://community.naturalcapitalproject.org/. *En primer lugar, utilice la función de búsqueda para comprobar si ya se ha planteado una pregunta similar.* Esto es especialmente cierto en el caso de los mensajes de error: puede buscar algunas palabras clave en el mensaje de error y, a menudo, encontrará mensajes que le ayudarán a solucionar el error.

Si informa de un error al ejecutar un modelo, incluya la siguiente información en el mensaje del foro:

+ Modelo de InVEST por el que pregunta

+ Versión de InVEST que está utilizando

+ Lo que ya ha intentado para resolver el problema, y no ha funcionado

+ El archivo de registro completo producido por el modelo, ubicado en la carpeta Workspace de salida - *InVEST-natcap.invest.<nombredelmodelo>-log-<timestamp>.txt*.

Capacitación
------------

Es posible que se ofrezcan varios talleres de capacitación sobre InVEST al año, en función de la financiación y la demanda.  La información sobre estos se anunciará en la página de apoyo y puede encontrarse en el sitio web del `Natural Capital Project <https://naturalcapitalproject.stanford.edu/>`_. Este sitio es también una buena fuente de información general sobre InVEST, publicaciones y casos de uso relacionados y otras actividades del Natural Capital Project.

Está disponible un Curso Online Masivo y Abierto (MOOC) gratuito `En inglés <https://www.edx.org/course/introduction-to-the-natural-capital-project-approach/>`_ y `en español <https://www.edx.org/course/una-introduccion-al-enfoque-de-capital-natural-ver-2/>`_, que proporciona:

- Una introducción a los métodos del Natural Capital Project

- Introducción a InVEST

- Los modelos SDR, Vulnerabilidad Costera y Enfriamiento Urbano se presentan con cierto detalle (aunque ya están todos desactualizados ante las recientes actualizaciones de estos modelos).

- Una visión general de otros temas de análisis de los servicios ecosistémicos, incluidos los escenarios, los beneficiarios y las fuentes de datos

- Varios estudios de caso.

También hay una lista de reproducción en YouTube <https://www.youtube.com/playlist?list=PLSFk2iLV3UfNqRZGwfcgyoZZZqZDnj2V7/>`_ con tutoriales de formación en vídeo, entre ellos:

- Serie de verano: Introducción a InVEST (breve introducción a InVEST, SDR, vulnerabilidad costera y comunicación de resultados)

- Serie de verano: Calidad del agua dulce (se presentan con más detalle el NDR y el SDR)

- Serie de verano: InVEST urbano  (se presenta con más detalle el enfriamiento urbano)

- Introducción a: Producción de pastizales

- Introducción a: Calidad del hábitat

- Introducción a: Almacenamiento de carbono

- Introducción a: Rendimiento hídrico estacional

- Introducción a: Mitigación del riesgo de inundaciones urbanas

Asimismo disponemos de una serie de vídeos `SIG para InVEST <https://naturalcapitalproject.stanford.edu/software/virtual-training/gis-invest>`_ que ofrece instrucciones prácticas sobre algunas de las tareas SIG necesarias para trabajar con modelos InVEST. Se ofrecen tanto para QGIS como para ArcGIS.


.. _working-with-the-DEM:

Trabajo con el MDE
==================

Para los modelos de agua dulce SDR, NDR y rendimiento hídrico estacional es fundamental disponer de un modelo digital de elevación (MDE) bien preparado. No deben faltar datos (agujeros de valores NoData), y deben representarse correctamente los patrones de flujo de agua superficial sobre el área de interés para obtener resultados precisos.

Utilice el MDE de mayor calidad y mejor resolución que sea apropiado para su aplicación. Esto reducirá las posibilidades de que haya sumideros y datos que falten, y representará con mayor precisión el flujo de agua superficial del terreno, proporcionando la cantidad de detalles que se requiere para tomar decisiones informadas a su escala de interés. 

Aunque cada fuente de MDE es diferente, al igual que la extensión de cada zona de estudio y los requisitos de cada proyecto, hay varios pasos generales que solemos tener que hacer para preparar un MDE que se ejecute en un modelo InVEST. Cada uno de estos pasos se describe a continuación, incluyendo información sobre el uso de las funciones incorporadas de ArcGIS y QGIS. También existen otras opciones para el procesamiento de MDE, como ArcHydro, ArcSWAT, AGWA y BASINS, que no se tratan aquí.  Esto solo pretende ser una breve visión general de los problemas y los métodos relacionados con la preparación de MDE, no un tutorial de SIG.

1. **Mosaico de datos DEM en bruto y en mosaico**

   Si ha descargado datos de MDE para su área que se encuentran en múltiples teselas adyacentes, primero tendrán que ser unidas en un mosaico para crear un único ráster de MDE.  En ArcToolbox, utilice Herramientas de gestión de datos -> Raster -> Raster Dataset -> Mosaic to New Raster.  Observe detenidamente el ráster resultante para asegurarse de que los valores son correctos a lo largo de los bordes donde se unieron los mosaicos.  Si no lo son, pruebe con diferentes valores para el parámetro Método de mosaico de la herramienta Mosaico a nuevo ráster.

   En QGIS puede utilizar la función Raster -> Miscellaneous -> Merge para combinar los mosaicos.

2. **Reproyección al sistema de coordenadas de su proyecto**

   Al reproyectar un MDE en ArcGIS (herramienta Ráster de proyecto) o en QGIS (herramienta Warp), es importante seleccionar BILINEAR o CÚBICA para la "Técnica de remuestreo" en ArcGIS o "Método de remuestreo" en QGIS. Si se selecciona NEAREST (o Near en QGIS) se obtendrá un MDE con un patrón de cuadrícula incorrecto en toda el área de interés, que solo puede ser obvio cuando se amplía el zoom o después de que se haya ejecutado Dirección del flujo. Esto creará una red de corrientes y un patrón de flujo incorrectos, y conducirá a malos resultados del modelo.

3. **Comprobación de falta de datos**

   Observe detenidamente el ráster del MDE para asegurarse de que no faltan datos, representados por las celdas NoData dentro del área de interés.  Si hay celdas NoData, hay que asignarles valores.

   Para los agujeros pequeños, una forma de hacerlo es utilizar la función ArcGIS Focal Mean dentro de Raster Calculator (o Conditional -> CON).  Por ejemplo, en ArcGIS 10.x::

	Con(IsNull("theDEM"),FocalStatistics("theDEM",NbrRectangle(3,3),"MEAN"),"theDEM")

   También se puede utilizar la interpolación, que puede funcionar mejor para agujeros más grandes. Convierta el MDE a puntos utilizando Herramientas de Conversión -> De Ráster -> Ráster a Punto, interpole utilizando las herramientas de Interpolación de Spatial Analyst, luego utilice CON para asignar los valores interpolados al MDE original::

        Con(isnull([theDEM]), [interpolated_grid], [theDEM])

   En QGIS, pruebe la herramienta Fill Nodata, o la herramienta r.neighbors de GRASS. r.neighbors proporciona diferentes tipos de estadísticas, incluyendo la Media.

4. **Identificación y llenado de los sumideros en el MDE**
  
   Este paso es casi siempre necesario.
  
   De la ayuda de ESRI sobre "Cómo funciona el sumidero": "Un sumidero es una celda o conjunto de celdas conectadas espacialmente cuya dirección de flujo no puede ser asignada a uno de los ocho valores válidos en un ráster de dirección de flujo. Esto puede ocurrir cuando todas las celdas vecinas son más altas que la celda de procesamiento o cuando dos celdas fluyen una hacia la otra, creando un bucle de dos celdas".

   Los sumideros suelen estar causados por errores en el MDE, y pueden producir un ráster de dirección de flujo incorrecto.  Esto puede dar lugar a varios problemas en el procesamiento de la hidrología, incluida la creación de una red de corrientes discontinua. Al rellenar los sumideros se asignan nuevos valores a las celdas de procesamiento anómalas, de forma que se alinean mejor con sus vecinas. Pero este proceso puede crear nuevos sumideros, por lo que puede ser necesario un proceso iterativo.

   Hemos comprobado que la herramienta QGIS Wang and Liu Fill hace un buen trabajo de relleno de sumideros, y se recomienda (incluso para quienes usan ArcGIS). También se puede utilizar ArcGIS mediante la herramienta Hidrología -> Relleno. Pueden ser necesarias varias ejecuciones de Fill.

5. **Verificación de la red de corrientes**
  
   En este punto, el MDE debería estar listo para ser probado. Lo más importante es comprobar la calidad de la generación de las corrientes, por lo que necesitará un mapa de corrientes del mundo real para comparar, que puede ser geoespacial o no, siempre que pueda compararlo visualmente.
  
La red de corrientes generada por el modelo a partir del MDE debería coincidir con las corrientes de un mapa de corrientes conocido y correcto. Varias de los modelos hidrológicos de InVEST y la herramienta de apoyo de InVEST, RouteDEM, generan una red de corrientes (normalmente llamada *stream.tif*). Estas herramientas crean las corrientes generando primero los rásters de Dirección de Flujo y Acumulación de Flujo (que debería comprobar como parte de este paso), y luego aplicando el valor de "umbral de acumulación de flujo" (UAF) introducido por quien usa para seleccionar los píxeles que deberían formar parte de la red de corrientes. Por ejemplo, si se da un valor UAF de 1000, entonces 1000 píxeles deben drenar en un píxel particular antes de que se considere parte de una corriente. Esto equivale a decir que las corrientes se definen por tener un valor de acumulación de flujo >= 1000.

   Utilice estos resultados de *stream.tif* para evaluar si las corrientes modelizadas se ajustan a la realidad, y ajuste el umbral de acumulación de flujo en consecuencia. Valores mayores de UAF producirán redes más gruesas con menos afluentes, valores menores de UAF producirán más afluentes. No hay un valor "correcto" para el UAF, será diferente para cada área de interés y MDE. Un buen valor para empezar a probar es 1000. Al comparar *stream.tif* con un mapa de corrientes del mundo real, compruebe que tiene la granularidad adecuada de los afluentes, y asegúrese de que las corrientes de *stream.tif* son continuas, no cortadas en segmentos desconectados o píxeles individuales. Tenga en cuenta que las corrientes modelizadas rara vez, o nunca, son exactamente iguales a la realidad, por lo que no pretende la perfección, sino que se acerque razonablemente. Si las corrientes modelizadas son discontinuas, intente hacer otro Relleno en el MDE, y asegúrese de que ha utilizado el método de remuestreo BILINEAR o CÚBICO para la reproyección. Si un MDE no hace corrientes continuas sin importar lo que intente, entonces aconsejamos probar otra fuente de datos de elevación. Hay varias fuentes disponibles a nivel mundial, y cada una de ellas tiene un rendimiento diferente en distintos lugares del mundo. 

   Para crear mapas de acumulación de caudales y corrientes sin necesidad de ejecutar un modelo hidrológico completo, puede utilizar la herramienta RouteDEM de InVEST, que es específica para procesar el MDE. Consulte la página :ref:`RouteDEM <routedem>` para obtener más información.

6. **Creación de cuencas**
  
   Se recomienda crear las cuencas hidrográficas a partir del MDE que se vaya a utilizar en el análisis. Si se obtiene una capa vectorial de cuencas hidrográficas de otro lugar, los límites de la(s) cuenca(s) podrían no alinearse correctamente con la hidrología creada a partir del MDE que se está utilizando para el modelizado, lo que llevaría a resultados agregados incorrectos.

  Hay una variedad de herramientas que pueden crear cuencas hidrográficas, incluyendo la herramienta ArcGIS Watershed y QGIS Watershed basins o r.basins.fill. InVEST también proporciona una herramienta llamada DelineateIt, que funciona bien, es sencilla de utilizar y se recomienda. Tiene la ventaja de poder crear cuencas que se solapan, como cuando hay varias presas a lo largo del mismo río. La página :ref:`DelineateIt <delineateit>` posee más información.

   Una vez generadas las cuencas hidrográficas, verifique que representan las cuencas correctamente y que a cada cuenca se le asigna un ID entero único en el campo "ws_id" (o "subws_id", dependiendo del modelo - vea la sección de Necesidades de Datos del modelo hidrológico que esté utilizando para saber qué se requiere).
  
7. **Recorte del MDE a su área de estudio**
  
   Por lo general, recomendamos que el MDE se recorte a un área ligeramente mayor que su área de interés (que suele ser una cuenca hidrográfica). Esto es para asegurar que la hidrología alrededor del borde de la cuenca sea capturada. Esto es particularmente importante si el MDE (y/u otros datos de input del modelo) son de resolución gruesa, ya que al recortar el polígono de la cuenca se producirán grandes áreas de datos perdidos alrededor del borde. Para ello, cree un búfer o amortiguamiento alrededor del polígono de la cuenca y recorte el MDE a ese polígono con búfer. Asegúrese de que el búfer tiene al menos la anchura del tamaño de la celda de su modelo de input más grueso. Por ejemplo, si sus datos de precipitación son los más gruesos, con una resolución de 1km, cree un buffer alrededor del polígono de la cuenca que tenga al menos 1km de ancho, y utilice esa cuenca con buffer para recortar todos sus inputs del modelo, incluyendo el MDE. A continuación, utilice la cuenca no amortiguada como input al modelo.

