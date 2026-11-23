*************************
Tipos de datos de entrada
*************************

Los modelos de InVEST aceptan muchos tipos diferentes de datos espaciales y no espaciales. Los clasificamos en 12 tipos:

.. _number:

número
------
Un valor escalar. Puede introducir números en formato entero o de punto flotante. No se permiten fracciones.

Unidades
~~~~~~~~
La mayoría de los datos numéricos de entrada tienen unidades. Los modelos de InVEST utilizan, en la medida de lo posible, las unidades y los símbolos estándar del SI. Para consultar las definiciones de estos símbolos, véanse las `unidades del SI <https://en.wikipedia.org/wiki/International_System_of_Units#Units_and_prefixes>`_ y las `unidades aceptadas para su uso con el SI <https://en.wikipedia.org/wiki/Non-SI_units_mentioned_in_the_SI#Units_officially_accepted_for_use_with_the_SI>`_.

InVEST también utiliza la unidad no perteneciente al SI **años**.

Cuando la unidad es **moneda**, puede utilizarse cualquier moneda, pero debe emplearse la misma en todo el modelo.

Tenga en cuenta que **t** es el símbolo de la tonelada métrica, equivalente a 1000 kg. No la confunda con las toneladas estadounidenses o imperiales.


.. _ratio:

proporción
----------
Una proporción sin unidades dentro del intervalo de 0 a 1, donde 0 representa «nada» y 1 representa «todo».
Algunos datos de entrada de tipo proporción pueden ser inferiores a 0 o superiores a 1, mientras que otros están estrictamente limitados al intervalo de 0 a 1.

.. _percent:

porcentaje
----------
Una proporción sin unidades dentro del intervalo de 0 a 100, donde 0 representa «nada» y 100 representa «todo».
Algunos datos de entrada de tipo porcentaje pueden ser inferiores a 0 o superiores a 100, mientras que otros están estrictamente limitados al intervalo de 0 a 100.

.. _integer:

entero
------
Un número entero (positivo o negativo). Los números enteros suelen utilizarse para identificar algo de manera única.
Como los rásteres solo pueden almacenar datos numéricos, es habitual utilizar códigos enteros como etiquetas que se vinculan con datos no numéricos
(como los tipos de uso/cobertura del suelo y los grupos de suelos).

.. _text:

texto
-----
Texto libre. InVEST acepta cualquier carácter Unicode (UTF-8). Para obtener mejores resultados, utilice conjuntos de caracteres Unicode para alfabetos no latinos.

.. _option:

opción
------
Una selección de un conjunto fijo de opciones. Por lo general, las opciones se muestran en un menú desplegable. Algunos datos de entrada CSV tienen columnas que deben contener valores de un conjunto fijo de opciones. En ese caso, asegúrese de introducir las opciones exactamente como están escritas.


.. _truefalse:

verdadero/falso
---------------
Los datos de entrada de tipo verdadero/falso suelen mostrarse como una casilla de verificación. Algunos datos de entrada CSV tienen columnas de verdadero/falso. En ese caso, la documentación del modelo explicará exactamente cómo introducir los valores (``TRUE`` o ``FALSE``, ``1`` o ``0``, etc.).


.. _csv:

CSV
---
Una tabla de datos almacenada en formato .csv (valores separados por comas). Aunque la coma es el separador estándar, pueden utilizarse otros delimitadores, como el punto y coma. Puede utilizar cualquier programa de hojas de cálculo para crear y editar una tabla y luego exportarla al formato CSV. Los dos formatos CSV de Excel que se sabe que funcionan son «CSV (delimitado por comas)» y «CSV UTF-8 (delimitado por comas)». Es probable que otros formatos CSV produzcan un error.

.. _raster:

ráster
------
Un archivo de datos espaciales que almacena datos en píxeles, cada uno de los cuales tiene un valor numérico.
InVEST acepta todos los formatos ráster compatibles con GDAL, incluido GeoTIFF (.tif) y muchos más.
Para consultar la lista completa, visite https://gdal.org/drivers/raster/index.html.

Bandas
~~~~~~
Los rásteres pueden tener varias bandas. Todos los modelos de InVEST utilizan únicamente la primera banda. Si utiliza un ráster multibanda,
asegúrese de que el conjunto de datos correcto se encuentre en la primera banda.


.. _datatypes:

Tipos de datos
~~~~~~~~~~~~~~
Cada ráster tiene un *tipo de dato* que determina el valor mínimo y máximo que puede tener cada píxel. Algunos tipos de datos permiten números positivos y negativos, mientras que otros solo permiten números positivos. La mayoría de las veces no necesitará cambiar el tipo de dato de su ráster, pero es importante conocerlo.

Cómo entender los tipos de datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
El tipo de dato de un ráster se muestra como un código en sus metadatos, que pueden consultarse en el programa SIG que utilice. El código de tipo de dato tiene 3 componentes:

1. Indicador de signo (**u**), opcional

   De manera predeterminada, los tipos de datos tienen signo; es decir, incluyen un signo (+ o -) que indica si el número es positivo o negativo.
   Se necesita un tipo de dato con signo para almacenar datos negativos.
   Si un tipo de dato comienza con **u**, significa que no tiene signo. Todos los datos sin signo son positivos. Si no necesita almacenar datos negativos, puede ahorrar espacio utilizando un tipo sin signo.

   Esta distinción solo existe para los tipos de datos enteros. Los tipos float siempre tienen signo.

2. Tipo (**float** o **int**)

   Los tipos de punto flotante (float) pueden almacenar dígitos después del punto decimal. No existe un límite estricto para la cantidad de decimales que pueden almacenar, pero solo tienen precisión para una cantidad limitada de dígitos totales (antes y después del punto decimal).
   Los tipos enteros (int) solo pueden almacenar números enteros. Su precisión es exacta.
   Para datos discretos, es preferible utilizar tipos de datos enteros siempre que sea posible.

3. Tamaño (**8, 16, 32, 64**)

   Es la cantidad de bits utilizados para almacenar el número. Determina el intervalo de números que puede contener el tipo de dato.
   Puede ahorrar espacio utilizando el tamaño más pequeño que funcione para sus datos. Por ejemplo, rara vez se necesitan los números grandes que permite almacenar un ráster **float64**. El intervalo de **float32** es suficiente para la mayoría de los datos del mundo real y utiliza la mitad del espacio.
   El tipo **uint8** es suficiente para la mayoría de los datos discretos que utiliza InVEST (clases de uso/cobertura del suelo, grupos de suelos, etc.), que tienen menos de 256 valores posibles.

A continuación se presentan todos los tipos de datos ráster estándar y sus intervalos (los intervalos incluyen los valores inicial y final):

- **byte** (**uint8**): cualquier número entero de 0 a 255
- **uint16**: cualquier número entero de 0 a 65 535
- **uint32**: cualquier número entero de -? a aproximadamente 4.2x10 :sup:`9`
- **int16**: cualquier número entero de -32 768 a 32 767
- **int32**: cualquier número entero de -2.1x10 :sup:`9` a 2.1x10 :sup:`9`
- **float32**: cualquier número de -3.4x10 :sup:`38` a 3.4x10 :sup:`38` (con una precisión aproximada de 7 dígitos)

  .. note::
     Los números más grandes tienen menos dígitos decimales de precisión. Los números mayores que 2 :sup:`23` (aproximadamente 8 000 000) utilizan los 7 dígitos a la izquierda del punto decimal y no pueden tener ninguna parte decimal. La mayoría de los datos del mundo real tienen menos de 7 cifras significativas, por lo que esto no representa un problema. Si necesita precisión decimal para números tan grandes, utilice **float64**.

- **float64**: cualquier número de -1.7x10 :sup:`308` a 1.7x10 :sup:`308` (con una precisión aproximada de 16 dígitos)

.. note::
   También existe un tipo **byte con signo** (**int8**, de -128 a 127). ArcGIS, en particular, puede generar rásteres byte con signo. Como GDAL no admite directamente el tipo **int8**, recomendamos evitarlo. InVEST aplica una solución alternativa para permitir el tipo **int8** en algunos casos. Si debe utilizar un ráster **int8**, es aún más importante comprobar que los resultados intermedios y finales sean coherentes.


Valores nodata
~~~~~~~~~~~~~~
Los rásteres pueden tener un valor *nodata* que indica las áreas donde no existen datos. Los píxeles que tienen este valor se excluyen de los cálculos.
El valor nodata debe estar codificado en los metadatos del ráster (de lo contrario, InVEST no sabrá cuál es).

Cómo elegir un valor nodata
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Una buena elección de valor nodata se encuentra muy fuera del intervalo de los valores reales de los datos, pero dentro del intervalo permitido por el tipo de dato del ráster.

-1 es una buena opción como valor nodata si se cumplen ambas condiciones:

- los datos siempre son no negativos; y
- el tipo de dato del ráster tiene signo.

Si no se cumplen estas condiciones, una buena opción es el valor máximo del tipo de dato. También puede utilizarse el valor mínimo para los tipos de datos con signo (no utilice el valor mínimo para los tipos sin signo: es 0, que suele ser un valor válido de los datos). Estas son buenas opciones porque suelen ser mucho mayores o menores que el intervalo de los datos válidos, por lo que no entrarán en conflicto.
Los datos discretos son la única excepción: para un ráster entero, como uno de uso/cobertura del suelo, puede elegir cualquier valor dentro del intervalo del tipo de dato que no sea un valor válido de los datos.

Estas recomendaciones se resumen en la siguiente tabla.

+----------------------------------------------+--------------------------------+-------------------------------+--------------------------------------------------------+
| **Datos continuos (tipos de datos float)**                                                                    | **Datos discretos (tipos de datos enteros)**           |
+==============================================+================================+===============================+========================================================+
|                                              | Tipo de dato **con signo**     | Tipo de dato **sin signo**    | Cualquier entero dentro del intervalo del tipo         |
+----------------------------------------------+--------------------------------+-------------------------------+ que no sea un valor válido de los datos                |
| Todos los datos válidos son **no negativos** | -1                             | Valor máximo del tipo de dato | (comúnmente 0, -1 o el valor máximo o mínimo del tipo) |
+----------------------------------------------+--------------------------------+-------------------------------+--------------------------------------------------------+
| Los datos válidos pueden ser **negativos**   | Valor máximo o mínimo del tipo |                               |                                                        |
+----------------------------------------------+--------------------------------+-------------------------------+--------------------------------------------------------+


Problemas frecuentes
^^^^^^^^^^^^^^^^^^^^
La configuración incorrecta de los valores nodata es una causa muy común de problemas para los usuarios de InVEST. Algunos errores frecuentes son:

- No establecer un valor nodata. Es habitual utilizar un valor, como 0 o -1, para representar las áreas sin datos.
  Si ese valor no se establece en los metadatos del ráster, InVEST lo tratará como un dato válido.
  Esto producirá resultados incorrectos o un error. Debe establecer un valor nodata, a menos que todos los píxeles de su ráster contengan datos válidos (lo cual no es habitual). Puede consultar y editar los metadatos del ráster, incluido el valor nodata, en su programa SIG.

- Utilizar un valor nodata inadecuado. El valor nodata debe:

  - encontrarse dentro del intervalo permitido por el :ref:`tipo de dato <datatypes>` del ráster. Utilizar un valor fuera de este intervalo puede producir resultados inesperados.
  - no entrar en conflicto con los datos reales. Asegúrese de que esté muy fuera del intervalo de los valores posibles de los datos.


.. _vector:

vector
------
Un archivo de datos espaciales que almacena datos en formas geométricas, cada una de las cuales puede tener varios atributos.
InVEST acepta todos los formatos vectoriales compatibles con GDAL, incluido GeoPackage (.gpkg), ESRI Shapefile (.shp) y muchos más.
Para consultar la lista completa, visite https://gdal.org/drivers/vector/index.html.

.. _workspace:

directorio del espacio de trabajo
---------------------------------
El directorio donde se escriben los resultados del modelo. Debe tener permisos de lectura y escritura en este directorio.

.. _file:

archivo
-------
Cualquier otro tipo de archivo que no esté incluido en las categorías anteriores.
