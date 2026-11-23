.. _croppollination:

******************************************************
Polinización de cultivos (abundancia de polinizadores)
******************************************************

Resumen
=======

El modelo de polinización de InVEST se centra en las abejas silvestres como polinizadores animales clave. Utiliza estimaciones de la disponibilidad de sitios de anidación y de recursos florales dentro del radio de vuelo de las abejas para derivar un índice de la abundancia de abejas que anidan en cada celda del paisaje (es decir, la oferta de polinizadores). Luego utiliza los recursos florales, la actividad de forrajeo de las abejas y la información sobre sus distancias de vuelo para estimar un índice de la abundancia de abejas que visitan cada celda. Si se desea, el modelo calcula después un índice sencillo de la contribución de estas abejas a la producción agrícola, basado en la abundancia de abejas y en la dependencia de los cultivos respecto de la polinización. Los resultados pueden utilizarse para comprender cómo cambian la polinización de los cultivos y el rendimiento agrícola ante modificaciones del uso del suelo y de las prácticas de manejo agrícola. Los datos de entrada obligatorios incluyen un mapa de uso y cobertura del suelo (LULC), atributos de la cobertura del suelo, los grupos o especies de polinizadores presentes y sus distancias de vuelo. Para estimar la contribución de los polinizadores silvestres a la producción agrícola se necesita información sobre las fincas de interés, los cultivos que se producen en ellas y la abundancia de polinizadores manejados. Entre las limitaciones del modelo se encuentran que no considera la persistencia de los polinizadores a lo largo del tiempo ni los efectos del tamaño de las parcelas.

Introducción
============

La polinización de cultivos por abejas y otros animales constituye un servicio ecosistémico potencialmente valioso en muchos paisajes donde se combinan hábitats agrícolas y naturales (Allen-Wardell et al. 1998, Free 1993). La polinización puede aumentar el rendimiento, la calidad y la estabilidad de cultivos de frutos y semillas tan diversos como el tomate, la canola, la sandía, el café, el girasol, la almendra y el cacao. De hecho, Klein et al. (2007) encontraron que 87 de los 115 cultivos de importancia mundial se benefician de la polinización animal; este servicio ha sido valorado en cifras que van desde miles de millones hasta decenas de miles de millones de dólares al año a escala mundial (Costanza et al. 1997, Losey y Vaughan 2006, Nabhan y Buchmann 1997, Southwick y Southwick 1992).

A pesar de estas cifras, es importante reconocer que no todos los cultivos necesitan polinización animal. Algunas plantas cultivadas son polinizadas por el viento (por ejemplo, cereales básicos como arroz, maíz y trigo) o se autop polinizan (por ejemplo, lentejas y otros frijoles), por lo que no necesitan polinizadores animales para producir frutos o semillas. Klein et al. (2007) presentan una lista de cultivos y sus requerimientos de polinización que puede ayudar a determinar si los cultivos de una región de interés podrían beneficiarse de los polinizadores animales silvestres.

Los responsables de la toma de decisiones pueden utilizar información sobre los polinizadores de cultivos, su abundancia en el paisaje y los servicios de polinización que prestan a los cultivos de varias maneras. En primer lugar, con mapas de abundancia de polinizadores y de los cultivos que los necesitan, los planificadores del uso del suelo podrían predecir las consecuencias de distintas políticas sobre los servicios de polinización y los ingresos de los agricultores (véase, por ejemplo, Priess et al. 2007). En segundo lugar, los agricultores podrían utilizar estos mapas para ubicar estratégicamente sus cultivos, considerando sus necesidades de polinización y las predicciones sobre la disponibilidad de polinizadores. En tercer lugar, las organizaciones de conservación o los fideicomisos de tierras podrían utilizar la herramienta para optimizar las inversiones en conservación que beneficien tanto a la biodiversidad como a los agricultores. Por último, los gobiernos u otras entidades que propongan esquemas de pago por servicios ecosistémicos podrían utilizar los resultados para estimar quién debería pagar a quién y cuánto.

El modelo
=========

Una amplia variedad de animales puede actuar como polinizadora (por ejemplo, aves, murciélagos, polillas y moscas), pero las abejas son el grupo más importante para la mayoría de los cultivos (Free 1993). Por ello, el modelo de Polinización de InVEST se centra en las necesidades de recursos y los comportamientos de vuelo de las abejas silvestres. Muchas personas piensan en las abejas melíferas, manejadas en colmenas artificiales, cuando se habla de polinizadores, pero las abejas silvestres también contribuyen a la polinización de los cultivos. De hecho, para varios cultivos importantes (por ejemplo, los arándanos), las especies nativas son polinizadoras más eficientes y eficaces que las abejas melíferas (Cane 1997). Estas abejas nativas, junto con las abejas melíferas asilvestradas que viven en libertad, pueden beneficiar a los cultivos sin necesidad de manejar activamente colmenas cautivas. Este es el servicio de polinización asociado con la conservación de hábitats.

Este modelo está adaptado de Lonsdorf et al. (2009). Para persistir en un paisaje, las abejas necesitan dos elementos: lugares adecuados para anidar y suficiente alimento (proporcionado por las flores) cerca de sus sitios de anidación. Si cuentan con estos recursos, los polinizadores pueden volar hacia los cultivos cercanos y polinizarlos mientras recolectan néctar y polen. El modelo convierte la cobertura del suelo en un índice de idoneidad (0-1) para las abejas, con el fin de crear un mapa de fuentes de polinizadores. Las puntuaciones más altas indican fuentes con mayor abundancia relativa de abejas. Para calcular el índice, el modelo supone que las abejas necesitan dos tipos de recursos limitantes para persistir en un paisaje: sustratos de anidación y recursos florales. A partir de la cobertura del suelo proporcionada como entrada, se asignan valores de idoneidad a cada clase LULC según su capacidad para ofrecer estos recursos.

Luego, el modelo de Polinización utiliza el índice de oferta de sitios de anidación para estimar los polinizadores que visitan los campos de cultivo. Supone que la oferta procedente de parcelas cercanas contribuye más que la de parcelas lejanas. Utilizamos los aportes de Olsson et al. (2015) y ponderamos la visita de las abejas según la calidad floral de la parcela, para reflejar el comportamiento de forrajeo desde un sitio central que se sabe que siguen las abejas. En otras palabras, las tasas de visita a dos parcelas que se encuentran a la misma distancia de un nido son proporcionales a la calidad floral de cada parcela.

Además, este modelo incorpora el posible uso de abejas manejadas en un índice de rendimiento. Con información sobre la ubicación de los cultivos y su dependencia de los polinizadores, el modelo utiliza una función sencilla de rendimiento para proyectar cómo la abundancia de polinizadores silvestres en las áreas agrícolas y el uso de abejas manejadas contribuyen a un índice de rendimiento de los cultivos. La inclusión de abejas manejadas refleja las recomendaciones de trabajos recientes del proyecto Integrated Crop Pollination, financiado por el USDA (icpbees.org), para integrar los beneficios conjuntos de las abejas manejadas y silvestres.

Estos pasos se describen formalmente a continuación.

Cómo funciona
-------------

El modelo se basa en índices y requiere los siguientes datos biofísicos:

* un mapa LULC;
* una tabla biofísica asociada con el ráster LULC, que permita relacionar los tipos de LULC con la idoneidad para la anidación y los recursos florales en las distintas estaciones;
* una tabla de grupos de polinizadores con información sobre las estaciones de actividad, las preferencias de anidación, las distancias medias de vuelo y las abundancias relativas de cada especie o grupo de polinizadores silvestres;
* un shapefile de fincas que indique su ubicación geoespacial, el tipo de cultivo, la dependencia de los polinizadores, la abundancia de polinizadores manejados y la disponibilidad de sitios de anidación y recursos florales dentro de las fincas.

Debido a que las abejas vuelan con facilidad, integran varios elementos del paisaje y se desplazan entre hábitats de anidación y hábitats de alimentación (Ricketts et al. 2006). Las distancias que suelen recorrer afectan tanto su persistencia como el nivel de servicio que proporcionan a las fincas. Por ello, el modelo requiere una distancia típica de forrajeo para cada especie de polinizador. Estos datos pueden obtenerse mediante estimaciones cuantitativas de campo (por ejemplo, Roubik y Aluja 1983), indicadores indirectos como el tamaño corporal (Greenleaf et al. 2007) o el criterio de expertos.

Oferta y abundancia de polinizadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con estos datos, el modelo estima primero la oferta de polinizadores para cada celda del paisaje, a partir de los sitios de anidación disponibles en esa celda, los recursos florales (es decir, el alimento) de las celdas circundantes y la abundancia relativa de esa especie de polinizador. Los recursos florales de las celdas cercanas a los sitios de anidación reciben una ponderación mayor que los de las celdas lejanas, de acuerdo con el radio medio de forrajeo de la especie.

:math:`PS(x,s)` es el índice de oferta de polinizadores en el píxel :math:`x` para la especie :math:`s`, definido como:

.. math:: PS(x,s)=FR(x,s) HN(x,s) sa(s)
	:label: (pol. 1)

donde :math:`FR(x,s)` es el índice de recursos florales accesibles en el píxel :math:`x` para la especie :math:`s`, definido como:

.. math:: FR(x,s)=\frac{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)\sum_{j\in J}RA(l(x'),j)fa(s,j)}{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 2)

:math:`HN(x,s)` es la idoneidad del hábitat para la anidación en el píxel :math:`x` para la especie :math:`s`:

.. math:: HN(x,s)=\max_{n\in N}\left[N(l(x),n) ns(s,n)\right]
	:label: (pol. 3)

y donde:

* :math:`sa(s)` es el índice de abundancia relativa de la especie :math:`s`, en el intervalo :math:`[0.0, 1.0]`; :math:`\sum_{s\in S} sa(s) = 1`, y :math:`S` es el conjunto de todas las especies;
* :math:`N(l,n)` es el índice del sustrato de anidación para el tipo de cobertura del suelo :math:`l` y el tipo de sustrato :math:`n`, en el intervalo :math:`[0.0, 1.0]`;
* :math:`l(x)` es el tipo de cobertura del suelo en el píxel :math:`x`;
* :math:`j` es la estación;
* :math:`RA(l, j)` es el índice de abundancia relativa de recursos florales en la cobertura del suelo :math:`l` durante la estación :math:`j`;
* :math:`fa(s,j)` es la actividad relativa de forrajeo de la especie de polinizador :math:`s` durante la estación :math:`j`;
* :math:`D(x,x')` es la distancia euclidiana entre las celdas :math:`x` y :math:`x'`;
* :math:`ns(s,n)` es la preferencia de idoneidad de anidación de la especie :math:`s` por el tipo de anidación :math:`n` (y :math:`N` es el conjunto de todos los tipos de anidación);
* y :math:`\alpha_s` es la distancia de forrajeo esperada para el polinizador :math:`s` (Greenleaf et al. 2007).

La oferta de polinizadores indica de qué lugares del paisaje proceden los polinizadores. La abundancia de polinizadores indica dónde están activos en el paisaje. Esta abundancia depende de los recursos florales que atraen a los polinizadores hacia una celda y de la oferta de polinizadores que puede acceder a ella. El índice de abundancia de polinizadores de la especie :math:`s` en la celda :math:`x`, durante la estación :math:`j`, :math:`PA(x,s,j)`, es el producto de los recursos florales disponibles en una celda durante una estación determinada, ponderados por la actividad relativa del polinizador en esa estación, y de la oferta de polinizadores, normalizado por el índice de recursos florales de las celdas circundantes, de modo que:

.. math:: PA(x,s,j)=\left(\frac{RA(l(x),j) fa(s,j)}{FR(x,s)}\right)\frac{\sum_{x'\in X}PS(x',s) \exp(-D(x,x')/\alpha_s)}{\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 4)


Consulte el Apéndice de la tabla de variables para conocer las definiciones y propiedades de todas las variables.

Abundancia y rendimiento en las fincas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, mediante los índices de abundancia de polinizadores en el paisaje, la ubicación de las fincas y la información sobre cada finca (disponibilidad de polinizadores manejados y dependencia del cultivo respecto de la polinización), el modelo calcula un índice del rendimiento total alcanzado y de la contribución de los polinizadores silvestres a ese rendimiento.

En primer lugar, el modelo calcula un índice de abundancia total de polinizadores por estación en las áreas agrícolas que podrían beneficiarse de los servicios de polinización. La abundancia de polinizadores dentro de las fincas se expresa como:

.. math:: PAT(x,j)=\sum_{s\in S}PA(x,s,j)
	:label: (pol. 5)

La contribución potencial de la abundancia de polinizadores dentro de las fincas al rendimiento de los cultivos dependientes de la polinización se calcula mediante una función sigmoide de media curva ajustable:

.. math:: FP(x)=\frac{PAT(x,j(f(x)))(1-h(f(x)))}{h(f(x))(1-2PAT(x,j(f(x)))+PAT(x,j(f(x))}
	:label: (pol. 6)

donde :math:`h(f(x))` es la constante de semisaturación de la finca :math:`f` en el píxel :math:`x`, que indica la abundancia de polinizadores silvestres necesaria para alcanzar la mitad del rendimiento potencial total dependiente de la polinización.

La contribución real de los polinizadores silvestres al rendimiento de los cultivos dependientes de la polinización depende del grado en que las necesidades de polinización ya estén cubiertas por los polinizadores manejados. El rendimiento total dependiente de la polinización, aportado tanto por polinizadores silvestres como manejados, se expresa como:

.. math:: PYT(x)=\min(mp(f(x))+FP(x),1)
	:label: (pol. 7)

suponiendo que un valor de 0 indica que se alcanza el 0 % del rendimiento dependiente de la polinización y que 1,0 indica que se alcanza el 100 %. La notación de máximo/mínimo restringe el valor de :math:`PYT` al intervalo de 0 a 1, donde :math:`mp(f(x))` es la proporción de las necesidades de polinización cubierta por los polinizadores manejados disponibles en el píxel :math:`x` dentro del polígono de la finca :math:`f`.

La proporción del rendimiento dependiente de la polinización atribuible a los polinizadores silvestres se expresa como:

.. math:: PYW(x)=\max(0, PYT(x)-mp(f(x)))
	:label: (pol. 8)

Así, cuando los polinizadores manejados son suficientemente abundantes, es decir, cuando :math:`mp(f(x))=1`, no existe un rendimiento adicional atribuible a los polinizadores silvestres.

El rendimiento total de los cultivos es función de la dependencia del cultivo respecto de la polinización y del grado en que se satisfacen sus necesidades de polinización. Algunas especies cultivadas son autocompatibles o polinizadas por el viento y su rendimiento depende menos de los polinizadores animales, mientras que otras requieren obligatoriamente polinizadores para producir cualquier rendimiento (Klein et al. 2007). El rendimiento total de los cultivos se calcula para cada finca como:

.. math:: YT(f)=1-\nu(f)\left(1-\sum_{x\in X(f)}PYT(x)/|X(f)|\right)
	:label: (pol. 9)

donde :math:`f` es una finca determinada, :math:`X(f)` es el conjunto de píxeles que cubren la finca :math:`f`, y :math:`|X(f)|` es el número de píxeles que cubren la finca :math:`f`. La función :math:`\nu(f)` es un escalar :math:`\in [0,1]` que representa la proporción del rendimiento del cultivo producido en la finca :math:`f` que depende de los polinizadores.

La proporción del rendimiento total de los cultivos atribuible a los polinizadores silvestres se expresa como:

.. math:: YW(f)=\nu(f)\left(\sum_{x\in X(f)}PYW(x)/|X(f)|\right)
	:label: (pol. 10)

Limitaciones y simplificaciones
===============================

Este modelo se basa en índices y solo estima patrones relativos de abundancia de polinizadores y de contribución de la polinización al rendimiento de los cultivos. Esto se debe a que rara vez se dispone de estimaciones absolutas de la densidad de nidos, la disponibilidad de recursos y la abundancia de polinizadores, y las funciones de rendimiento (incluida la abundancia de polinizadores) de muchos cultivos están poco definidas. El uso de índices relativos limita nuestra capacidad para estimar valores económicos absolutos que permitan fundamentar mejor las decisiones de planificación del uso del suelo, que a menudo se basan en análisis de costo-beneficio.

El uso del forrajeo desde un sitio central en el índice de abundancia de polinizadores del modelo todavía no se ha probado empíricamente, por lo que recomendamos cautela al utilizar el modelo para realizar proyecciones económicas sin verificación empírica. Lo mismo se aplica a la integración de las abejas manejadas en la función de rendimiento.

Como modelo basado en índices, resulta adecuado para realizar comparaciones cualitativas entre escenarios que representan cambios marginales en LULC, prácticas de manejo de las fincas o tipos de cultivos. La abundancia de polinizadores en las fincas :math:`PAF(x,j)` se verá afectada por el número de grupos de polinizadores que se modelen y, por tanto, no puede utilizarse para comparar comunidades de polinizadores diferentes, incluso en un mismo paisaje. De manera similar, dado que los índices de abundancia relativa de las especies :math:`sa(s)` se especifican como datos de entrada, el modelo no producirá resultados precisos para escenarios en los que una especie rara se vuelva común, o viceversa, como consecuencia de grandes cambios en el hábitat de anidación o en la disponibilidad de recursos florales.

El modelo no incluye la dinámica de las poblaciones de abejas a lo largo del tiempo y, por tanto, no puede evaluar si estas poblaciones son sostenibles dadas las condiciones actuales del paisaje. En su lugar, proporciona una instantánea estática del número de polinizadores en cada celda del paisaje, a partir de estimaciones sencillas de los sitios de anidación y los recursos alimentarios disponibles. No se consideran algunos factores que influyen en las poblaciones de abejas, como las perturbaciones del hábitat y las fluctuaciones poblacionales habituales. Además, el modelo calcula la oferta de polinizadores a partir del promedio de los recursos florales disponibles, ponderados por la actividad de los polinizadores durante las estaciones en las que están activos. No considera el orden de las estaciones ni la dependencia de la abundancia de polinizadores en una estación respecto de los recursos disponibles en la estación inmediatamente anterior. El modelo tampoco considera las diferencias en la eficacia de las distintas especies o grupos de polinizadores para polinizar diferentes tipos de cultivos. Se supone que todas las especies contribuyen por igual, en función de su abundancia relativa y de la constante de semisaturación especificada para cada finca o cultivo.

El modelo no considera el tamaño de las manchas de hábitat al estimar la abundancia. Para muchas especies existe un tamaño mínimo de mancha por debajo del cual un hábitat no puede sostener a esa especie a largo plazo. Hay evidencia de que las manchas pequeñas albergan menos especies de abejas (Kremen et al. 2004), aunque las abejas también pueden sobrevivir en áreas pequeñas de hábitat adecuado (Ricketts 2004).

Es probable que los polinizadores respondan a características del paisaje a escala muy fina, difíciles de captar con los datos habituales de cobertura del suelo, que suelen tener resoluciones de 30 m. Por ejemplo, pequeñas manchas con recursos florales dentro de un hábitat que, en general, resulta hostil para las abejas pueden proporcionar recursos alimentarios importantes, pero no serán detectadas por los mapas habituales de cobertura del suelo. Algunas abejas también pueden anidar en áreas pequeñas pero adecuadas (un tramo de carretera apropiado o una cavidad en un árbol). Por tanto, el uso de valores promedio de disponibilidad de sitios de anidación o flores para cada clase LULC, junto con píxeles de 30 m o más, no permitirá captar estas áreas de recursos importantes, aunque sean de pequeña escala.

Datos necesarios
================

.. note:: *Todas las entradas espaciales deben tener exactamente el mismo sistema de coordenadas proyectadas* (con unidades lineales en metros), *no* un sistema de coordenadas geográficas (con unidades en grados).

- :investspec:`pollination workspace_dir`

- :investspec:`pollination results_suffix`

- :investspec:`pollination landcover_raster_path` Se utiliza para asignar una distribución espacial a las propiedades biofísicas relacionadas con el hábitat y los recursos florales de los tipos de cobertura del suelo. Debe tener una resolución suficientemente fina para captar los movimientos de las abejas en el paisaje. Si las abejas vuelan en promedio 800 metros y las celdas tienen 1000 metros de lado, el modelo no captará por completo el desplazamiento de las abejas desde sus sitios de anidación hacia las fincas vecinas.

- :investspec:`pollination landcover_biophysical_table_path` Los datos pueden resumirse a partir de estudios de campo u obtenerse mediante evaluaciones de expertos si no se dispone de datos de campo.

	Columnas:

	- :investspec:`pollination landcover_biophysical_table_path.columns.lucode`

	- :investspec:`pollination landcover_biophysical_table_path.columns.nesting_[SUBSTRATE]_availability_index`

	- :investspec:`pollination landcover_biophysical_table_path.columns.floral_resources_[SEASON]_index` Por ejemplo, una clase LULC compuesta en un 100 % por un cultivo de floración masiva que florece durante toda la estación y tiene una cobertura floral del 80 % recibiría un valor de idoneidad de 0,80. Una clase LULC que florece solo durante la mitad de la estación y tiene una cobertura floral del 80 % recibiría un valor de idoneidad floral de 0,40. El nombre de *SEASON* debe coincidir exactamente con una de las estaciones indicadas en la Tabla de grupos.

    **Ejemplo de tabla biofísica:**

    .. csv-table::
       :file: ../../invest-sample-data/pollination/landcover_biophysical_table_modified.csv
       :header-rows: 1
       :widths: auto

- :investspec:`pollination guild_table_path` «Grupo» (*guild*) se refiere a un conjunto de especies de abejas que presentan el mismo comportamiento de anidación, ya sea porque prefieren construir sus nidos en el suelo, en cavidades de árboles u otras características del hábitat. Si se sabe que varias especies son polinizadoras importantes y difieren en cuanto a la estación de vuelo, los requerimientos de anidación o la distancia de vuelo, proporcione datos separados para cada una. Si se dispone de pocos datos o de ninguno, cree un único «protopolinizador» con datos basados en valores promedio o en el criterio de expertos sobre toda la comunidad de polinizadores. Cada fila corresponde a una especie o grupo único de polinizadores, y las columnas deben tener los siguientes nombres y definiciones:

	Columnas:

	- :investspec:`pollination guild_table_path.columns.species`
	- :investspec:`pollination guild_table_path.columns.nesting_suitability_[SUBSTRATE]_index` Los sustratos son definidos por el usuario, pero podrían incluir nidos en el suelo, cavidades de árboles, etc.
	- :investspec:`pollination guild_table_path.columns.foraging_activity_[SEASON]_index` Las estaciones son definidas por el usuario, pero podrían incluir primavera, verano y otoño; o estación húmeda y seca, etc.
	- :investspec:`pollination guild_table_path.columns.alpha` El modelo utiliza esta distancia estimada para definir el entorno de flores disponibles alrededor de una celda determinada y ponderar las sumas de recursos florales y abundancias de polinizadores en las fincas. Este valor puede determinarse a partir de la distancia típica de forrajeo de una especie de abeja, según una relación alométrica (véase Greenleaf et al. 2007).
	- :investspec:`pollination guild_table_path.columns.relative_abundance` Asignar el mismo valor a cada especie hará que todas tengan la misma ponderación.

   *Ejemplo:* una Tabla de grupos hipotética con dos especies. Existen dos tipos principales de SUSTRATO: «cavidad» y «suelo». La especie «Apis» utiliza ambos tipos de anidación, mientras que «Bombus» solo utiliza nidos en cavidades. Hay dos ESTACIONES: «primavera» y «verano». Las distancias típicas de vuelo, especificadas en metros (alpha), varían ampliamente entre las especies. La abundancia relativa de Bombus es mayor que la de Apis, lo que indica que hay más polinizadores Bombus que Apis.

   **Ejemplo de tabla de grupos:**

   .. csv-table::
      :file: ../../invest-sample-data/pollination/guild_table.csv
      :header-rows: 1
      :widths: auto

- :investspec:`pollination farm_vector_path`

    .. note::
       El vector opcional de fincas sobrescribirá los valores estacionales de recursos florales y de idoneidad de los sustratos de anidación en todas las áreas que se superpongan con el ráster LULC.

    Campos:

    - :investspec:`pollination farm_vector_path.fields.crop_type` Para las fincas que cultivan varios productos superpuestos o cultivos en distintas estaciones, debe incluirse un polígono superpuesto separado para cada cultivo.
    - :investspec:`pollination farm_vector_path.fields.half_sat` Es un parámetro ajustable que puede resultar más útil modificar después de una primera ejecución del modelo y de examinar sus resultados. Corresponde a :math:`h` en la ecuación :eq:`(pol. 6)`. Puede utilizarse 0,05 como valor predeterminado, con un intervalo estimado entre 0,05 y 0,1.
    - :investspec:`pollination farm_vector_path.fields.season`
    - :investspec:`pollination farm_vector_path.fields.fr_[SEASON]`
    - :investspec:`pollination farm_vector_path.fields.n_[SUBSTRATE]`
    - :investspec:`pollination farm_vector_path.fields.p_dep` Consulte Klein et al. (2007) para obtener estimaciones de cultivos comunes.
    - :investspec:`pollination farm_vector_path.fields.p_managed` Puede estimarse como la proporción de la densidad de colmenas o tasa de carga recomendada. Consulte Delaplane y Mayer (2000) para conocer las tasas de carga recomendadas en Estados Unidos. Las oficinas de extensión agrícola también son una buena fuente de esta información.

.. _interpreting-results:

Interpretación de los resultados
================================

Resultados finales
------------------

* **Registro de parámetros:** cada vez que se ejecuta el modelo, se crea un archivo de texto (.txt) en el espacio de trabajo. El archivo enumera los valores de los parámetros y los mensajes de salida de esa ejecución, y se nombra de acuerdo con el servicio, la fecha y la hora. Cuando se comunique con NatCap por errores en la ejecución de un modelo, incluya el registro de parámetros.

* **farm_results_[Suffix].shp**: (solo se genera si se proporciona un vector de fincas) copia del archivo vectorial de polígonos de fincas de entrada, con los siguientes campos adicionales:

  * *p_abund*: abundancia promedio de polinizadores en la finca durante la estación activa.
  * *y_tot*: índice de rendimiento total, que incluye polinizadores silvestres y manejados, así como el rendimiento independiente de la polinización.
  * *pdep_y_w*: índice del rendimiento potencial dependiente de la polinización atribuible a los polinizadores silvestres.
  * *y_wild*: índice del rendimiento total atribuible a los polinizadores silvestres.

* **farm_pollinators_[Suffix].tif**: (solo se genera si se proporciona un vector de fincas) abundancia total de polinizadores por píxel, considerando todas las especies y cada estación, recortada a la geometría de los polígonos del vector de fincas.

* **pollinator_abundance_[SPECIES]_[SEASON]_[Suffix].tif**: abundancia por píxel de la especie de polinizador SPECIES durante la estación SEASON.

* **pollinator_supply_[SPECIES]_[Suffix].tif**: índice por píxel de la oferta de polinizadores de la especie SPECIES que podría encontrarse en un píxel, dado su factor arbitrario de abundancia de la tabla, multiplicado por la idoneidad del hábitat para esa especie en el píxel y por los recursos florales disponibles a los que el polinizador podría volar desde ese píxel (ecuación 1).

* **total_pollinator_abundance_[SEASON]_[Suffix].tif**: (solo se genera si se proporciona un vector de fincas) abundancia total de polinizadores por píxel, considerando todas las especies durante cada estación.

* **total_pollinator_yield_[Suffix].tif**: (solo se genera si se proporciona un vector de fincas) índice de rendimiento total de polinizadores por píxel para los píxeles que se superponen con las fincas, incluidos los polinizadores silvestres y manejados.

* **wild_pollinator_yield_[Suffix].tif**: (solo se genera si se proporciona un vector de fincas) índice de rendimiento de polinizadores por píxel para los píxeles que se superponen con las fincas, considerando únicamente los polinizadores silvestres.

Resultados intermedios
^^^^^^^^^^^^^^^^^^^^^^

También puede examinar los resultados intermedios. Estos archivos ayudan a determinar las razones de los patrones observados en los resultados finales, permiten comprender mejor el modelo y facilitan la solución de problemas. Se encuentran en la carpeta *intermediate_outputs* dentro del directorio del espacio de trabajo definido para la ejecución del modelo, y la mayoría tiene nombres que indican claramente qué representa cada capa.

Apéndice 1: Tabla de variables
==============================

* :math:`x`: coordenada de un píxel.
* :math:`X`: conjunto de todos los píxeles del mapa de cobertura del suelo.
* :math:`f(x)`: finca ubicada en el píxel x.
* :math:`F`: conjunto de todos los píxeles que se encuentran dentro de fincas.
* :math:`s`: especie de abeja.
* :math:`n`: tipo de anidación (suelo, cavidad).
* :math:`N`: conjunto de todos los tipos de anidación.
* :math:`j`: estación (otoño, primavera, etc.).
* :math:`J`: conjunto de todas las estaciones (por ejemplo, {otoño, primavera}).
* :math:`fj(f, x)`: estación activa de polinización para la finca :math:`f` en el píxel :math:`x`.
* :math:`\alpha_s`: distancia media de forrajeo de la especie s.
* :math:`ns(s,n)`: preferencia de idoneidad de anidación de la especie :math:`s` por el tipo de anidación :math:`n`.
* :math:`HN(x,s)`: idoneidad del hábitat para la anidación en el píxel :math:`x` para la especie :math:`s` [0.0, 1.0].
* :math:`N(l,n)`: índice del sustrato de anidación para el tipo de cobertura del suelo :math:`l` y el tipo de sustrato :math:`n`, en el intervalo :math:`[0.0, 1.0]`.
* :math:`RA(l,j)`: índice de abundancia relativa de recursos florales en el tipo de cobertura del suelo :math:`l` durante la estación :math:`j`, :math:`[0.0, 1.0]`.
* :math:`fa(s,j)`: actividad relativa de forrajeo de la especie :math:`s` durante la estación :math:`j`.
* :math:`FR(x,s)`: índice de recursos florales accesibles en el píxel :math:`x` para la especie :math:`s`.
* :math:`D(x,x')`: distancia euclidiana entre los centroides de los píxeles :math:`x` y :math:`x'`.
* :math:`PS(x,s)`: índice de oferta de polinizadores en el píxel :math:`x` para la especie :math:`s`.
* :math:`PA(x,s,j)`: abundancia de polinizadores en el píxel :math:`x` para la especie :math:`s` durante la estación :math:`j`.
* :math:`PAT(x,j)`: abundancia total de polinizadores en la finca en el píxel :math:`x` durante la estación :math:`j`, considerando todas las especies.
* :math:`FP(x)`: contribución potencial de la abundancia de polinizadores dentro de la finca al rendimiento de cultivos dependientes de la polinización en un píxel de la finca durante la estación en que se necesita la polinización.
* :math:`mp(f)`: abundancia de polinizadores manejados en la finca :math:`f`, relativa a la tasa de carga recomendada.
* :math:`h(f)`: coeficiente de semisaturación para la finca :math:`f`.
* :math:`PYT(x)`: rendimiento total atribuible a los polinizadores en el píxel x durante la estación :math:`j`, considerando polinizadores silvestres y manejados.
* :math:`PYW(x)`: rendimiento atribuible a los polinizadores silvestres en el píxel x durante la estación :math:`j`.
* :math:`sa(s)`: índice de abundancia relativa de la especie :math:`s`.
* :math:`YT(f)`: rendimiento promedio de la finca :math:`f`, considerando la dependencia del cultivo respecto de los polinizadores.
* :math:`YW(f)`: proporción del rendimiento promedio de la finca :math:`f` atribuible a los polinizadores silvestres, considerando la dependencia del cultivo respecto de los polinizadores.
* :math:`\nu(f)`: proporción del rendimiento del cultivo que depende de la polinización.

Apéndice 2: Fuentes de datos
============================

.. note:: Los datos de muestra solo tienen como finalidad ilustrar la estructura de los datos y no deben utilizarse como fuente de datos.

Dependencia de los cultivos respecto de los polinizadores
---------------------------------------------------------

Consulte Klein et al. 2007 para obtener una lista de cultivos de importancia mundial y su dependencia de los polinizadores animales.

Idoneidad para la anidación y disponibilidad de recursos florales
-----------------------------------------------------------------

Koh et al. 2016 contiene datos de idoneidad para la anidación y disponibilidad de recursos florales para 45 categorías de uso del suelo.

:ref:`Uso y cobertura del suelo <lulc>`
---------------------------------------

Referencias
===========

Allen-Wardell, G., P. Bernhardt, R. Bitner, A. Burquez, S. Buchmann, J. Cane, PA Cox, V. Dalton, P. Feinsinger, M. Ingram, D. Inouye, CE Jones, K. Kennedy, P. Kevan, and H. Koopowitz. 1998. The potential consequences of pollinator declines on the conservation of biodiversity and stability of food crop yields. Conservation Biology 12: 8-17.

Cane, JH. 1997. Lifetime monetary value of individual pollinators: the bee habropoda laboriosa at rabbiteye blueberry (vaccinium ashei reade). Acta Horticulturae 446: 67-70.

Costanza, R., R. d'Arge, R. de Groot, S. Farber, M. Grasso, B. Hannon, K. Limburg, S. Naeem, RV O'Neill, J. Paruelo, RG Raskin, P. Sutton, and M. van den Belt. 1997. The value of the world's ecosystem services and natural capital. Nature 387: 253-260.

Delaplane, KS, and DF Mayer. 2000. Crop pollination by bees. CABI Publishing, New York.

Free, JB. 1993. Insect pollination of crops. Academic Press, London.

Greenleaf, SS, NM Williams, R. Winfree, and C. Kremen. 2007. Bee foraging ranges and their relationship to body size. Oecologia 153: 589-596.

Greenleaf, SS, and C. Kremen. 2006. Wild bee species increase tomato production and respond differently to surrounding land use in Northern California. Biological Conservation 133:81-87.

Klein, AM, BE Vaissiere, JH Cane, I. Steffan-Dewenter, SA Cunningham, C. Kremen, and T. Tscharntke. 2007. Importance of pollinators in changing landscapes for world crops. Proceedings of the Royal Society B-Biological Sciences 274: 303-313.

Koh, I., E. Lonsdorf, N. Williams, C. Brittain, R. Isaacs, J. Gibbs, and T. Ricketts. 2016. Modeling the status, trends, and impacts of wild bee abundance in the United States. Proceedings of the National Academy of Sciences 113 (1) 140-145; DOI: 10.1073/pnas.1517685113

Kremen, C., NM Williams, RL Bugg, JP Fay, and RW Thorp. 2004. The area requirements of an ecosystem service: crop pollination by native bee communities in California. Ecology Letters 7: 1109-1119.

Lonsdorf, E., C. Kremen, T. Ricketts, R. Winfree, N. Williams, and SS Greenleaf. 2009. Modelling pollination services across agricultural landscapes. Annals of Botany 1: 12. online [https://pubmed.ncbi.nlm.nih.gov/19324897/]

Lonsdorf, E., TH Ricketts, CM Kremen, NM Williams, and S. Greenleaf. in press. Pollination services in P. Kareiva, TH Ricketts, GC Daily, H. Tallis, and S. Polasky, eds. The theory and practice of ecosystem service valuation.

Losey, JE, and M. Vaughan. 2006. The economic value of ecological services provided by insects. Bioscience 56: 311-323.

Nabhan, GP, and SL Buchmann. 1997. Services provided by pollinators. Pages 133-150 in GC Daily, ed. Nature's services. Island Press, Washington, D.C.

Olsson, O. A. Bolin, H. Smith, and E. Lonsdorf. 2015. Modeling pollinating bee visitation rates in heterogeneous landscapes from foraging theory. Ecological Modelling 316: 133-143.

Priess, JA, M. Mimler, AM Klein, S. Schwarze, T. Tscharntke, and I. Steffan-Dewenter. 2007. Linking deforestation scenarios to pollination services and economic returns in coffee agroforestry systems. Ecological Applications 17: 407-417.

Ricketts, TH. 2004. Tropical forest fragments enhance pollinator activity in nearby coffee crops. Conservation Biology 18: 1262-1271.

Ricketts, TH, NM Williams, and MM Mayfield. 2006. Connectivity and ecosystem services: crop pollination in agricultural landscapes. Pages 255-289 in M. Sanjayan and K. Crooks, eds. Connectivity for Conservation. Cambridge University Press, Cambridge, UK.

Roubik, DW, and M. Aluja. 1983. Flight ranges of Melipona and Trigona in tropical forest. Journal of the Kansas Entomological Society 56: 217-222.

Southwick, EE, and L. Southwick. 1992. Estimating the economic value of honey-bees (Hymenoptera; Apidae) as agricultural pollinators in the United States. Journal of Economic Entomology 85: 621-633.

Winfree, R., J. Dushoff, EE Crone, CB Schultz, RV Budny, NM Williams, and C. Kremen. 2005. Testing simple indices of habitat proximity. American Naturalist 165(6): 707-717.
