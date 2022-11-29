**************
Tipos de input
**************

Los modelos de InVEST aceptan muchos tipos diferentes de datos espaciales y no espaciales. Los clasificamos en 12 tipos:

.. _number:

número
------
Un valor escalar. Puede introducir números en formato entero o de punto flotante. Las fracciones no están permitidas.

Unidades
~~~~~~~~
La mayoría de inputs numéricos tienen unidades. Los modelos de InVEST utilizan, en la medida de lo posible, unidades y símbolos estándar del SI. Para las definiciones de estos símbolos, véase `SI Units <https://en.wikipedia.org/wiki/International_System_of_Units#Units_and_prefixes>`_ y `units accepted for use with SI <https://en.wikipedia.org/wiki/Non-SI_units_mentioned_in_the_SI#Units_officially_accepted_for_use_with_the_SI>`_.

InVEST también usa la unidad no SI **años**.

Cuando la unidad es **moneda**, se puede utilizar cualquier divisa, pero se debe utilizar la misma en todo el modelo.

Tenga en cuenta que **t** es el símbolo de la tonelada métrica, o 1000 kg. Asegúrese de no confundirlo con las toneladas americanas o imperiales.


.. _ratio:

tasa
----
Una proporción sin unidades en el rango 0 - 1, donde 0 representa "ninguno" y 1 representa "todos". Algunos inputs de proporción pueden ser menores que 0 o mayores que 1, mientras que otras se limitan estrictamente al rango 0-1.

.. _percent:

porcentaje
----------
Una proporción sin unidades en el rango 0 - 100, donde 0 representa "ninguno" y 100 representa "todos". Algunos inputs porcentuales pueden ser menores que 0 o mayores que 100, mientras que otras se limitan estrictamente al rango 0-100.

.. _integer:

entero
------
Un número entero (positivo o negativo). Los números enteros se utilizan a menudo para identificar algo de forma única. Dado que los rásters solo pueden almacenar datos numéricos, es habitual utilizar códigos enteros como etiquetas que se asignan a datos no numéricos (como los tipos de uso de la tierra/cubierta vegetal y los grupos de suelos).

.. _text:

texto
-----
Texto de forma libre. InVEST acepta cualquier carácter Unicode (UTF-8). Para obtener los mejores resultados, utilice conjuntos de caracteres Unicode para los alfabetos no latinos.

.. _option:

opción
------
Una elección entre un conjunto fijo de opciones. Las opciones suelen aparecer como un menú desplegable. Algunos inputs CSV tienen columnas que deben contener valores de un conjunto fijo de opciones. En ese caso, asegúrese de introducir las opciones exactamente como están escritas.

.. _truefalse:

verdadero/falso
----------
Los inputs verdadero/falso suelen aparecer como una casilla de verificación. Algunos inputs CSV tienen columnas de verdadero/falso. En ese caso, la documentación del modelo explicará exactamente cómo introducir los valores (``VERDADERO`` o ``FALSO``, ``1`` o ``0``, etc.)

.. _csv:

CSV
---
Una tabla de datos almacenada en formato .csv (valores separados por comas). Puede utilizar cualquier programa de hoja de cálculo para crear y editar una tabla, y luego exportarla al formato CSV. Los dos formatos CSV proporcionados por Excel que se sabe que funcionan son "CSV (delimitado por comas)" y "CSV UTF-8 (delimitado por comas)". Otros formatos CSV probablemente producirán un error.

.. _raster:

ráster
------
Un archivo de datos espaciales que almacena los datos en píxeles, cada uno de los cuales tiene un valor numérico. InVEST acepta todos los formatos ráster compatibles con GDAL, incluido GeoTiff (.tif) y muchos más. Para ver la lista completa, consulte https://gdal.org/drivers/raster/index.html.

Bandas
~~~~~~
Los rásters pueden tener varias bandas. Todos los modelos de InVEST analizan solo la primera banda. Si está utilizando un ráster de varias bandas, asegúrese de que el conjunto de datos correcto está en la primera banda.

.. _datatypes:

Tipos de datos
~~~~~~~~~~~~~~
Cada ráster tiene un *tipo de datos* que determina el valor mínimo y máximo que puede tener cada píxel. Algunos tipos de datos permiten números positivos y negativos, mientras que otros solo permiten números positivos. La mayoría de las veces no necesitará cambiar el tipo de datos de su ráster, pero es importante estar al tanto.

Comprensión de los tipos de datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
El tipo de datos de un ráster se muestra como un código en los metadatos del ráster, que puede verse en su programa de SIG. Un código de tipo de datos tiene 3 componentes:

1. Marcador sin signo (**u**), opcional

   Por defecto, los tipos de datos tienen signo, lo que significa que incluyen un signo (+ o -) que indica si el número es positivo o negativo.
   Se necesita un tipo de datos con signo para almacenar datos negativos.
   Si un tipo de datos comienza con **u**, no tiene signo. Todos los datos sin signo son positivos. Si no necesita almacenar datos negativos, ahorre espacio utilizando un tipo sin signo.

   Esta distinción solo existe para los tipos de datos enteros. Los tipos flotantes siempre tienen signo.

2. Tipo (**float** o **int**)

   Los tipos de punto flotante (float) pueden almacenar dígitos después del punto decimal. No hay un límite estricto en el número de decimales que pueden almacenar, pero solamente son precisos en un número limitado de dígitos totales (antes y después del punto decimal).
   Los tipos enteros (int) solo pueden almacenar números enteros. Tienen una precisión perfecta.
   Es mejor utilizar tipos de datos enteros siempre que sea posible para datos discretos.

3. Tamaño (**8, 16, 32, 64**)

   Es el número de bits que se utilizan para almacenar el número. Determina el rango de números que pueden caber en el tipo de datos.
   Puede ahorrar espacio utilizando el tamaño más pequeño que funcione para sus datos. Por ejemplo, los grandes números disponibles en un rango **float64** rara vez son necesarios. El rango **float32** es suficiente para la mayoría de los datos del mundo real, y utiliza la mitad de espacio.
   El tipo **uint8** es suficiente para la mayoría de los datos discretos que utiliza InVEST (clases de uso/cobertura del suelo, grupos de suelos, etc.) que tienen menos de 256 valores posibles.

Aquí están todos los tipos de datos ráster estándar y sus rangos (los rangos incluyen los valores iniciales y finales):

- **byte** (**uint8**): cualquier entero de 0 a 255
- **uint16**: cualquier entero de 0 a 65,535
- **uint32**: cualquier entero de 0 a cerca de 4.2x10 :sup:`9`
- **int16**: cualquier entero de -32,768 a 32,767
- **int32**: cualquier entero de -2.1x10 :sup:`9` a 2.1x10 :sup:`9`
- **float32**: cualquier número de -3.4x10 :sup:`38` a 3.4x10 :sup:`38` (con una precisión de unos 7 dígitos)

  .. note::
     Los números más grandes tienen menos dígitos decimales. Los números mayores de 2 :sup:`23` (unos 8.000.000) utilizan las 7 cifras de la izquierda del punto decimal y no pueden tener ninguna parte decimal. La mayoría de los datos del mundo real tienen menos de 7 cifras significativas, así que esto no es un problema. Si necesita precisión decimal para números tan grandes, utilice **float64** en su lugar.

- **float64**: cualquier número entre -1,7x10 :sup:`308` y 1,7x10 :sup:`308` (precisión de unos 16 dígitos)

.. note::
   También existe un tipo de **byte con signo** (**int8**, -128 a 127). ArcGIS, en particular, puede producir rásters de bytes con signo. Como GDAL no soporta directamente el tipo **int8**, recomendamos evitarlo. InVEST enfrenta esto para permitir el tipo **int8** en algunos casos. Si tiene que utilizar un ráster **int8**, es aún más importante comprobar que sus resultados intermedios y finales tienen sentido.

Valores nodata
~~~~~~~~~~~~~~
Los rásteres pueden tener un valor *"nodata"* que indica las áreas donde no existen datos. Los píxeles con este valor se excluyen de los cálculos.
El valor nodata debe estar codificado en los metadatos del ráster (de lo contrario, InVEST no sabrá cuál es).

Seleccón de un valor nodata
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Una buena elección de valor de nodata está muy por fuera del rango de valores de los datos reales, y al mismo tiempo está dentro del rango del tipo de datos ráster.

-1 es una buena elección de valor de nodata si se cumplen estas dos condiciones

- los datos son siempre no negativos, y
- el tipo de datos del ráster es con signo

Si no se cumplen estas condiciones, el valor máximo del tipo de datos es una buena elección. El valor mínimo también puede utilizarse para
tipos de datos con signo (no utilice el valor mínimo para los tipos sin signo: es 0, que suele ser un valor de datos válido). Estas son buenas opciones porque suelen ser mucho mayores o menores que el rango de los datos válidos, por lo que no entrarán en conflicto.
Los datos discretos son la única excepción: para un ráster de números enteros como el de uso del suelo/cubierta vegetal, puede elegir cualquier valor del rango del tipo de datos que no sea un valor de datos válido.

Estas recomendaciones se resumen en la siguiente tabla.

+------------------------------------+----------------------------+-------------------------+-----------------------------------------+
| **Datos continuos (tipos de datos flotantes)**                                            | **Datos discretos(tipos de datos enteros)**  |
+====================================+============================+=========================+=========================================+
|                                    | **Signed** data type       | **Unsigned** data type  | Cualquier entero en el rango de tio de datos      |
+------------------------------------+----------------------------+-------------------------+ ue no es un valor de dato válido          |
| Todo dato válido es **no-negativo** | -1                         | Valor máximo del tipo de datos | (comúnmente 0, -1, o el máximo o       |
+------------------------------------+----------------------------+-------------------------+ mínimo del tipo de dato)                     |
| Los datos válidos pueden ser **negativos**     | Valor máximo o mínimo del        |                         |                                         |
|                                    | tipo de datos              |                         |                                         |
+------------------------------------+----------------------------+-------------------------+-----------------------------------------+


Problemas comunes
^^^^^^^^^^^^^^^^^
Los valores nodata mal configurados son una causa muy común de problemas al usar InVEST. Algunos errores comunes son:

- No establecer un valor de nodata. Es habitual utilizar un valor, como 0 o -1, para representar las áreas nodata.
  Si ese valor no se establece en los metadatos del ráster, InVEST lo tratará como datos válidos.
  Esto provocará resultados incorrectos o un error. Debe establecer un valor de nodata a menos que todos los píxeles de su ráster tengan datos válidos (esto es poco común). Puede ver y editar los metadatos de su ráster, incluyendo el valor de nodata, en su programa de SIG.

- Utilizar un valor de nodata inadecuado. Su valor de nodata debe:

  - estar dentro del rango permitido por el :ref:`data type <datatypes>` del ráster. El uso de un valor fuera de este rango puede causar resultados inesperados.
  - evitar conflicto con los datos reales. Asegúrese de que está bien por fuera del rango de valores de datos posibles.

.. _vector:

vector
------
Un archivo de datos espaciales que almacena datos en formas geométricas, cada una de las cuales puede tener múltiples atributos de datos.
InVEST acepta todos los formatos vectoriales compatibles con GDAL, incluidos GeoPackage (.gpkg), ESRI Shapefile (.shp) y muchos más.
Para ver la lista completa, consulte https://gdal.org/drivers/vector/index.html.

.. _directory:

directorio
---------
Una carpeta que puede o no contener otros archivos o carpetas utilizados por el modelo.

.. _file:

archivo
-------
Cualquier otro tipo de archivo que no figure en la lista anterior.
