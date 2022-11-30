.. _using_invest:

Uso de InVEST
=============

Inicio del modelo
-------------------

En MacOS, todos los modelos de InVEST están contenidos en una aplicación. Vaya a sus Aplicaciones y abra InVEST desde allí, luego seleccione el modelo de la lista que aparece.

En Windows, cada modelo de InVEST aparece como un programa propio. Vaya al menú de inicio -> Todos los programas, y abra el modelo desde allí.

Ejecución del modelo
--------------------
La interfaz del modelo consiste en un formulario con un campo para cada input del modelo. Para los archivos de input, puede escribir la ruta o utilizar el botón de selección de archivos para navegar hasta el archivo. Una vez que todos los inputs han sido  introducidos y sean válidos, haga clic en el botón Ejecutar.

Recursos para buscar y formatear datos
--------------------------------------
La página de cada modelo en esta guía contiene una sección de **Necesidades de datos** que describe el formato de cada input. La página :ref:`data_sources` ofrece orientación sobre cómo encontrar datos para lons inputs comunes del modelo. Muchos modelos también tienen un **Apéndice** con orientación para encontrar datos específicos del modelo. Los **datos de muestra** proporcionan ejemplos de cada input.

.. advertencia::
   Los datos de muestra existen solo para ilustrar la estructura de los datos. Los valores de los datos de muestra pueden ser completamente inventados o haber siso modificados a partir de un estudio antiguo. No son valores genéricos o por defecto y no deben utilizarse con, o en lugar de, sus propios datos.

Validación
----------
InVEST valida todos los inputs a medida que los introduce para asegurarse de que el formato es correcto. Esto comprueba cosas como que
- un CSV contiene todas las columnas esperadas
- un input numérico está dentro del rango permitido
- todos los inputs espaciales se solapan.
No puede ejecutar el modelo hasta que todos los inputs pasen la validación. En el lado izquierdo, una marca de verificación verde indica que el input se ve correcto, mientras que una X roja indica un problema. Haga clic en la X roja para ver una descripción del problema.

Visualización de los resultados del modelo
------------------------------------------
Todos los resultados del modelo se almacenan en archivos en el directorio del espacio de trabajo. La mayoría de los resultados son archivos espaciales (vectores o rásters), pero algunos modelos también producen archivos CSV, HTML, etc. Consulte la sección "Interpretación de los resultados" en la página de cada modelo para conocer los detalles de cada resultado.

Cuando el modelo finalice, haga clic en el botón "Abrir espacio de trabajo" para abrir una ventana del explorador de archivos en el directorio del espacio de trabajo del modelo.

Alternativamente, mientras el modelo se está ejecutando, puede marcar el botón "Abrir espacio de trabajo después del éxito" para abrir automáticamente la ventana del explorador de archivos cuando el modelo termine.

Resultados finales
^^^^^^^^^^^^^^^^^^
Los resultados finales se encuentran en el nivel superior del directorio del espacio de trabajo.

Resultados intermedios
^^^^^^^^^^^^^^^^^^^^^^
Los resultados intermedios son archivos que se producen en el proceso de elaboración de los resultados finales. Pueden ser de interés para algunas aplicaciones, y son útiles para identificar el origen de los patrones resultantes y la depuración. Se encuentran en un directorio dentro del espacio de trabajo, normalmente llamado algo así como "intermediate" o "intermediate_dir".

Archivo de registro
^^^^^^^^^^^^^^^^^^^
En el nivel superior del directorio del espacio de trabajo, el modelo produce un archivo de registro. Incluye todos los parámetros y sus valores, información sobre la ejecución y cualquier error. El archivo de registro se llama ``InVEST-[model name]-log-[date]-[time].txt``.

Memoria caché
^^^^^^^^^^^^^
El espacio de trabajo también contiene un directorio que se utiliza para almacenar en caché las ejecuciones anteriores del modelo, como se describe en :ref:`avoided recomputation`. Normalmente se llama algo así como "cache" o "cache_dir". No contiene ningún dato legible para el ser humano y puede ignorarlo.

Funciones avanzadas
-------------------

.. _avoided recomputation:

Recálculo evitado
^^^^^^^^^^^^^^^^^
Todos los modelos de InVEST admiten el recálculo evitado. Esto significa que el modelo detectará los resultados intermedios y finales de una ejecución anterior en el espacio de trabajo especificado y evitará volver a calcular cualquier resultado que sea idéntico a la ejecución anterior. Esto puede ahorrar un tiempo de procesamiento significativo para las ejecuciones sucesivas cuando solo han cambiado algunos parámetros de input.
Tenga en cuenta que esto solo funciona dentro de un espacio de trabajo y con el mismo sufijo. Si elimina o cambia el directorio del espacio de trabajo, o cambia el sufijo de los resultados, no se evita el recálculo.

Procesamiento paralelo
^^^^^^^^^^^^^^^^^^^^^^
Los modelos de InVEST también admiten el procesamiento en paralelo. Si se dispone de varias CPU, se puede seleccionar el número a utilizar en el menú desplegable en *Archivo > Configuración > parámetro taskgraph_n_workers*. No todas las operaciones del modelo pueden ejecutarse en paralelo y el número óptimo de CPU a utilizar depende de los conjuntos de datos de input.

