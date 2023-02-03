.. _croppollination:

******************************************************
Polinización de cultivos (abundancia de polinizadores)
******************************************************

Resumen
=======

El modelo de polinización InVEST se centra en las abejas silvestres como animal polinizador clave. Utiliza estimaciones de la disponibilidad de lugares de anidación y recursos florales dentro de las áreas de vuelo de las abejas para obtener un índice de la abundancia de abejas que anidan en cada celda de un paisaje (es decir, la oferta de polinizadores). A continuación, utiliza los recursos florales, la actividad de forrajeo de las abejas y la información sobre la zona de vuelo para estimar un índice de la abundancia de abejas que visitan cada celda. Si se desea, el modelo calcula entonces un índice simple de la contribución de estas abejas a la producción agrícola, basado en la abundancia de abejas y la dependencia de los cultivos de la polinización. Los resultados pueden utilizarse para comprender los cambios en la polinización y el rendimiento de los cultivos con los cambios en el uso de la tierra y las prácticas de gestión agrícola. Los datos necesarios incluyen un mapa de uso y cobertura del suelo (LULC), los atributos de la cobertura del suelo, los gremios o especies de polinizadores presentes y sus áreas de vuelo. Para estimar la contribución de los polinizadores silvestres a la producción de los cultivos se requiere información sobre las fincas de interés, los cultivos que allí se producen y la abundancia de los polinizadores gestionados. Las limitaciones del modelo incluyen no tener en cuenta la persistencia de los polinizadores en el tiempo o los efectos del tamaño de las parcelas.

Introducción
============

La polinización de los cultivos por parte de las abejas y otros animales es un servicio ecosistémico potencialmente valioso en muchos paisajes de hábitats agrícolas y naturales mixtos (Allen-Wardell et al. 1998, Free 1993). La polinización puede aumentar el rendimiento, la calidad y la estabilidad de cultivos de frutas y semillas tan diversos como el tomate, la canola, la sandía, el café, el girasol, la almendra y el cacao. De hecho, Klein et al. (2007) descubrieron que 87 de los 115 cultivos de importancia mundial se benefician de la polinización animal, un servicio valorado entre miles y decenas de miles de millones al año en todo el mundo (Costanza et al. 1997, Losey y Vaughan 2006, Nabhan y Buchmann 1997, Southwick y Southwick 1992).

A pesar de estas cifras, es importante tener en cuenta que no todos los cultivos necesitan la polinización animal. Algunas plantas de cultivo son polinizadas por el viento (por ejemplo, los cereales básicos como el arroz, el maíz y el trigo) o se autopolinizan (por ejemplo, las lentejas y otros granos), sin necesidad de polinizadores animales para producir frutos o semillas con éxito. Klein et al. (2007) proporcionan una lista de cultivos y sus requisitos de polinización que pueden ayudar a identificar si los cultivos de una región de interés pueden beneficiarse de polinizadores animales silvestres.

Los responsables de la toma de decisiones pueden utilizar la información sobre los polinizadores de los cultivos, su abundancia en el paisaje y los servicios de polinización que proporcionan a los cultivos de varias maneras. En primer lugar, con mapas de la abundancia de polinizadores y de los cultivos que los necesitan, quienes planifican el uso de la tierra podrían predecir las consecuencias de diferentes políticas sobre los servicios de polinización y los ingresos de agricultores y agricultoras (para un ejemplo, véase Priess et al. 2007). En segundo lugar, estas personas podrían utilizar estos mapas para ubicar los cultivos de forma inteligente, teniendo en cuenta sus necesidades de polinización y las predicciones de disponibilidad de polinizadores. En tercer lugar, las organizaciones de conservación o los fideicomisos de tierras podrían utilizar la herramienta para optimizar las inversiones en conservación que beneficien tanto a la biodiversidad como a agricultores y agricultoras. Por último, los gobiernos u otras entidades que propongan sistemas de pago por servicios ecosistémicos podrían utilizar los resultados para estimar quién debe pagar a quién y cuánto.

El modelo
=========

Una amplia gama de animales pueden ser importantes polinizadores (por ejemplo, aves, murciélagos, polillas y moscas), pero las abejas son el grupo más importante para la mayoría de los cultivos (Free 1993). Por ello, el modelo de polinización de InVEST se centra en las necesidades de recursos y los comportamientos de vuelo de las abejas silvestres. Mucha gente piensa en las abejas melíferas, manejadas en colmenas artificiales, cuando piensa en polinizadores, pero las abejas silvestres también contribuyen a la polinización de los cultivos. De hecho, para varios cultivos importantes (por ejemplo, los arándanos), las especies autóctonas son polinizadores más eficientes y eficaces que las abejas melíferas (Cane 1997). Estas abejas nativas, además de las abejas melíferas ferales que viven en la naturaleza, pueden beneficiar a los cultivos sin necesidad de una gestión activa de las colmenas en cautividad. Este es el servicio de polinización asociado a la conservación del hábitat.

Este modelo está adaptado de Lonsdorf et al. (2009). Para que las abejas persistan en un paisaje, necesitan dos cosas: lugares adecuados para anidar y suficiente alimento (proporcionado por las flores) cerca de sus lugares de anidación. Si se les proporcionan estos recursos, los polinizadores están disponibles para volar a los cultivos cercanos y polinizarlos mientras recogen néctar y polen. El modelo traduce la cobertura del suelo en un índice de idoneidad (0-1) para las abejas para crear un mapa de fuentes de polinizadores. Las puntuaciones más altas indican fuentes de mayor abundancia relativa de abejas. Para calcular el índice, el modelo parte de la base de que las abejas necesitan dos tipos de recursos limitantes para persistir en un paisaje: sustratos de anidación y recursos florales. Dado un input de cobertura del suelo que describe el paisaje, se asignan varios valores de idoneidad de cada clase de LULC en función de su capacidad para proporcionar estos recursos.

El modelo de polinización utiliza entonces el índice de oferta de nidos para estimar los polinizadores que visitan los campos de cultivo. Supone que la oferta de las parcelas cercanas contribuye más que las más alejadas. Utilizamos los conocimientos de Olsson et al. (2015) y ponderamos las visitas de las abejas según la calidad floral de la parcela para reflejar el comportamiento de búsqueda de alimento en el lugar central que se sabe que manifiestan En otras palabras, las tasas de visita a dos parcelas igualmente distantes de un nido son proporcionales a las calidades florales de las parcelas.

Además, este modelo incorpora el uso potencial de las abejas manejadas en un índice de rendimiento. Con información sobre la ubicación de los cultivos y su dependencia de los polinizadores, el modelo utiliza una función de rendimiento simple para proyectar la manera en que la abundancia de polinizadores silvestres en las zonas agrícolas y el uso de abejas manejadas contribuyen a un índice de rendimiento de los cultivos. La inclusión de las abejas manejadas refleja la orientación del reciente trabajo del Proyecto de Polinización Integrada de Cultivos (icpbees.org), financiado por el USDA, para integrar los beneficios combinados de las abejas manejadas y silvestres.

Estos pasos se describen formalmente a continuación.

Cómo funciona
-------------

El modelo se basa en índices y requiere los siguientes datos biofísicos:

* un mapa LULC;
* una tabla biofísica emparejada con el ráster de LULC para asignar los tipos de LULC a la idoneidad de la nidificación y los recursos florales a lo largo de las estaciones;
* una tabla de gremios de polinizadores con propiedades sobre las estaciones activas, las preferencias de anidación, las distancias medias de vuelo y las abundancias relativas de cada especie o grupo de polinizadores silvestres
* un shapefile de las explotaciones agrícolas que indica su ubicación geoespacial, el tipo de cultivo, la dependencia de los polinizadores, la abundancia de los polinizadores gestionados, así como los lugares de anidación en la finca y los recursos florales.

Dado que las abejas son hábiles voladoras, se integran en varios elementos de un paisaje, desplazándose entre los hábitats de anidación y los de forrajeo (Ricketts et al. 2006). Las distancias que suelen volar afectan tanto a su persistencia como al nivel de servicio que prestan a las explotaciones. Por lo tanto, el modelo requiere una distancia típica de forrajeo para cada especie de polinizador. Estos datos pueden obtenerse a partir de estimaciones cuantitativas de campo (por ejemplo, Roubik y Aluja 1983), de aproximaciones como el tamaño corporal (Greenleaf et al. 2007) o de opiniones expertas.

Oferta y abundancia de polinizadores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A partir de estos datos, el modelo estima primero la oferta de polinizadores para cada celda del paisaje, basándose en los lugares de anidación disponibles en esa celda, los recursos florales (es decir, el alimento) en las celdas circundantes y la abundancia relativa de esa especie de polinizador. Los recursos florales de las celdas cercanas a los lugares de anidación tienen más peso que los de las celdas lejanas, de acuerdo con el rango medio de forrajeo de la especie.

:math:`PS(x,s)` es el índice de suministro de polinizadores en el píxel :math:`x` para la especie :math:`s` definido como:

.. math:: PS(x,s)=FR(x,s) HN(x,s) sa(s)
	:label: (pol. 1)

where :math:`FR(x,s)` es el índice de recursos florales accesibles en el píxel :math:`x` para la especie :math:`s` definido como:

.. math:: FR(x,s)=\frac{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)\sum_{j\in J}RA(l(x'),j)fa(s,j)}{\sum_{x'\in X}\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 2)

:math:`HN(x,s)` es la idoneidad de anidación del hábitat en el píxel :math:`x` para la especie :math:`s`

.. math:: HN(x,s)=\max_{n\in N}\left[N(l(x),n) ns(s,n)\right]
	:label: (pol. 3)

y donde

* :math:`sa(s)` es el índice de abundancia relativa de la especie :math:`s` en el rango :math:`[0.0, 1.0]`, :math:`\sum_{s\in S} sa(s) = 1`, y :math:`S` es el conjunto de todas las especies,
* :math:`N(l,n)` es el índice de sustrato de anidación para el tipo de cobertura vegetal :math:`l` para el tipo de sustrato :math:`n` en el rango :math:`[0.0, 1.0]`,
* :math:`l(x)` es el tipo de cobertura vegetal en el píxel :math:`x`,
* :math:`j` es la estación,
* :math:`RA(l, j)` índice de abundancia relativa de recursos florales en la cobertura vegetal :math:`l` durante la estación :math:`j`,
* :math:`fa(s,j)` es la actividad relativa de forrajeo de las especies de polinizadores :math:`s` durante la estacuón :math:`j`.
* :math:`D(x,x')` es la distancia euclidiana entre las celdas :math:`x` y :math:`x'`,
* :math:`ns(s,n)` es la preferencia de idoneidad para la nidificación de la especie :math:`s` en el tipo de anidación :math:`n` (y :math:`N` es el conjunto de todos los tipos de anidamiento),
* y :math:`\alpha_s` es la distancia de forrajeo prevista para el polinizador :math:`s` (Greenleaf et al. 2007).

La oferta de polinizadores es un indicador de la procedencia de los polinizadores en el paisaje. La abundancia de polinizadores indica dónde están activos los polinizadores en el paisaje. La abundancia de polinizadores depende de los recursos florales que atraen a los polinizadores a una celda y del suministro de polinizadores que pueden acceder a esa celda. La abundancia de polinizadores para el índice de especies :math:`s` en la celda :math:`x`, durante la estación :math:`j`, :math:`PA(x,s,j)`, es el producto de los recursos florales disponibles en una celda durante una estación determinada, ponderado por la actividad relativa de un polinizador durante esa estación con la oferta de polinizadores y normalizado por el índice de recursos florales en las celdas circundantes, de forma que:

.. math:: PA(x,s,j)=\left(\frac{RA(l(x),j) fa(s,j)}{FR(x,s)}\right)\frac{\sum_{x'\in X}PS(x',s) \exp(-D(x,x')/\alpha_s)}{\exp(-D(x,x')/\alpha_s)}
	:label: (pol. 4)


Consulte el Apéndice de la Tabla de Variables para ver todas las definiciones y propiedades de las variables.

Abundancia y rendimiento en la finca
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, utilizando los índices de abundancia de polinizadores en el paisaje, la ubicación de las explotaciones y la información sobre cada una de ellas (disponibilidad de polinizadores manejados, dependencia de los cultivos de la polinización), el modelo puede calcular un índice del rendimiento total alcanzado y la contribución de los polinizadores silvestres a ese rendimiento.

En primer lugar, el modelo calcula un índice de abundancia total de polinizadores por temporada en las zonas agrícolas que podrían beneficiarse de los servicios de polinización. La abundancia de polinizadores en las explotaciones agrícolas se da como:

.. math:: PAT(x,j)=\sum_{s\in S}PA(x,s,j)
	:label: (pol. 5)

La contribución potencial de la abundancia de polinizadores en la granja al rendimiento del cultivo dependiente de los polinizadores se calcula utilizando una función medio-sigmoide ajustable como:

.. math:: FP(x)=\frac{PAT(x,j(f(x)))(1-h(f(x)))}{h(f(x))(1-2PAT(x,j(f(x)))+PAT(x,j(f(x))}
	:label: (pol. 6)

donde :math:`h(f(x))` es la constante de media saturación para la granja :math:`f` en el píxel :math:`x` que indica la abundancia de polinizadores silvestres necesaria para alcanzar la mitad del rendimiento total potencial dependiente de los polinizadores.

La contribución real de los polinizadores silvestres al rendimiento dependiente de los polinizadores depende del grado en que las necesidades de polinización ya están cubiertas por los polinizadores manejados. El rendimiento total dependiente de los polinizadores, tanto de los silvestres como de los manejados, se da como:

.. math:: PYT(x)=\min(mp(f(x))+FP(x),1)
	:label: (pol. 7)

asumiendo que un valor de 0 indica que se alcanza el 0% del rendimiento dependiente de los polinizadores, y 1,0 indica que se alcanza el 100% del rendimiento dependiente de los polinizadores. Obsérvese que la notación max/min restringe el valor de :math:`PYT` a 0..1 donde :math:`mp(f(x))` es la proporción de necesidades de polinización satisfechas por polinizadores manejados disponibles en el píxel :math:`x` dentro del polígono de la finca :math:`f`.

La proporción del rendimiento dependiente de los polinizadores atribuible a los polinizadores silvestres se da como

.. math:: PYW(x)=\max(0, PYT(x)-mp(f(x)))
	:label: (pol. 8)

Así, en los casos en los que los polinizadores manejados son suficientemente abundantes, es decir, :math:`mp(f(x))=1`, no hay rendimiento adicional atribuible a los polinizadores silvestres.

El rendimiento total de los cultivos depende de su dependencia de la polinización y del grado en que se satisfagan sus necesidades de polinización. Algunas especies de cultivos son autocompatibles o se polinizan con el viento y su rendimiento depende menos de los polinizadores animales, mientras que otras especies necesitan obligatoriamente de estos polinizadores para generar cualquier rendimiento (Klein et al. 2007). El rendimiento total de los cultivos se calcula por finca como

.. math:: YT(f)=1-\nu(f)\left(1-\sum_{x\in X(f)}PYT(x)/|X(f)|\right)
	:label: (pol. 9)

donde :math:`f` es una finca particular, :math:`X(f)` es el conjunto de píxeles que cubren la finca :math:`f`, y :math:`|X(f)|` es el conteo de los píxeles cubiertos por la finca :math:`f`. La función :math:`\nu(f)` es un escalar :math:`\in [0,1]` que representa quñe proporción del rendimiento del cultivo en la finca :math:`f` depende de los polinizadores.

La proporción del rendimiento total de los cultivos atribuible a los polinizadores silvestres viene dada por

.. math:: YW(f)=\nu(f)\left(\sum_{x\in X(f)}PYW(x)/|X(f)|\right)
	:label: (pol. 10)

Limitaciones y simplificaciones
-------------------------------

Este modelo es un modelo basado en índices y solo estima los patrones relativos de abundancia de polinizadores y la contribución de la polinización al rendimiento de los cultivos. Esto se debe a que rara vez se dispone de estimaciones absolutas de la densidad de nidos, la disponibilidad de recursos y la abundancia de polinizadores, y a que las funciones de rendimiento (incluida la abundancia de polinizadores) para muchos cultivos están mal definidas. El hecho de basarse en índices relativos limita nuestra capacidad de estimar valores económicos absolutos para fundamentar mejor la toma de decisiones sobre la planificación del uso de la tierra, a menudo basada en análisis de costos y beneficios.

El uso del forrajeo en el lugar central en el índice de abundancia de polinizadores del modelo aún no se ha probado empíricamente, por lo que advertimos que no se debe utilizar el modelo para hacer proyecciones económicas sin verificación empírica. Lo mismo ocurre con la integración de las abejas manejadas en la función de rendimiento.

Al ser un modelo basado en índices, es muy adecuado para realizar comparaciones cualitativas entre escenarios que representan cambios marginales en LULC, prácticas de gestión agrícola o tipos de cultivo. La abundancia de polinizadores en la explotación :math:`PAF(x,j)` se verá afectada por el número de gremios de polinizadores que se modelicen, por lo que no puede utilizarse para comparar diferentes comunidades de polinizadores incluso en el mismo paisaje. Del mismo modo, dado que los índices de abundancia relativa de especies :math:`sa(s)` se especifican como input, el modelo no arrojará resultados precisos para escenarios en los que una especie rara se convierte en común o viceversa debido a grandes cambios en el hábitat de anidación o en la disponibilidad de recursos florales.

El modelo no incluye la dinámica de las poblaciones de abejas a lo largo del tiempo y, por tanto, no puede evaluar si estas poblaciones son sostenibles dado el paisaje actual. En su lugar, el modelo se limita a proporcionar una instantánea estática del número de polinizadores en cada celda del paisaje, dadas unas simples estimaciones de los lugares de anidación y los recursos alimenticios. Algunos de los factores que influyen en las poblaciones de abejas, como las perturbaciones del hábitat y las fluctuaciones típicas de la población, no se captan. Además, el modelo calcula la oferta de polinizadores basándose en la media de los recursos florales disponibles ponderada por la actividad de los polinizadores en las estaciones en las que están activos. No tiene en cuenta el orden de las estaciones ni la dependencia de la abundancia de polinizadores en una estación de los recursos disponibles en la estación inmediatamente anterior. El modelo no tiene en cuenta la variación de la eficacia de las diferentes especies o gremios de polinizadores en la polinización de diferentes tipos de cultivos. Se supone que todas las especies contribuyen por igual en función de su abundancia relativa y de la constante de semisaturación especificada para cada explotación/cultivo.

El modelo no tiene en cuenta el tamaño de las parcelas del hábitat a la hora de estimar la abundancia. Para muchas especies, existe un tamaño mínimo de parcela, por debajo del cual una parcela no puede mantener a esa especie a largo plazo. Hay algunas pruebas de que las parcelas pequeñas sustentan menos especies de abejas (Kremen et al. 2004), pero las abejas también pueden sobrevivir en pequeñas áreas de hábitat adecuado (Ricketts 2004).

Es probable que los polinizadores se vean influenciados por las características del paisaje a pequeña escala, que son difíciles de captar en los datos típicos de la cobertura del suelo con resoluciones típicas de 30 m. Por ejemplo, pequeños parches de flores en un hábitat hostil para las abejas pueden proporcionar importantes recursos alimenticios, pero no serán detectados por los típicos mapas de cobertura del suelo. Algunas abejas también son capaces de anidar en zonas pequeñas pero adecuadas (un solo borde de carretera o un hueco de árbol adecuados). Por lo tanto, el uso de valores medios de disponibilidad de lugares de anidación o de flores para cada clase de LULC, junto con píxeles de 30 m o más, no captará estas importante áreas de recursos de fina escala.

Necesidades de datos
====================

.. note:: *Todos los inputs espaciales deben tener exactamente el mismo sistema de coordenadas proyectadas* (con unidades lineales en metros), *no* un sistema de coordenadas geográficas (con unidades en grados).

- :investspec:`pollination workspace_dir`

- :investspec:`pollination results_suffix`

- :investspec:`pollination landcover_raster_path` Se utiliza para mapear las propiedades biofísicas sobre el hábitat y los recursos florales de los tipos de cubierta vegetal en un esquema espacial. Este debe tener una resolución lo suficientemente fina como para captar los movimientos de las abejas en un paisaje. Si las abejas vuelan una media de 800 metros y las celdas tienen 1000 metros de ancho, el modelo no captará completamente el movimiento de las abejas desde sus lugares de anidación hasta las fincas vecinas.

- :investspec:`pollination landcover_biophysical_table_path` Los datos pueden resumirse a partir de estudios de campo u obtenerse mediante una evaluación de personas expertas si no se dispone de datos de campo.

	Columnas:

	- :investspec:`pollination landcover_biophysical_table_path.columns.lucode`

	- :investspec:`pollination landcover_biophysical_table_path.columns.nesting_[SUBSTRATE]_availability_index`

	- :investspec:`pollination landcover_biophysical_table_path.columns.floral_resources_[SEASON]_index` Por ejemplo, una clase LULC compuesta al 100% por un cultivo de floración masiva que florece toda la estación con una cobertura de abundancia del 80% recibiría un valor de idoneidad de 0,80. Una clase LULC que florezca solo la mitad de la temporada con una cobertura de abundancia del 80% recibiría un valor de idoneidad floral de 0,40. El nombre *ESTACIÓN* debe coincidir exactamente con una estación dada en la Tabla de Gremios.

    **Ejemplo de tabla biofísica:**

    .. csv-table::
       :file: ../../invest-sample-data/pollination/landcover_biophysical_table_modified.csv
       :header-rows: 1
       :widths: auto

- :investspec:`pollination guild_table_path` El término "gremio" se refiere a un grupo de especies de abejas que muestran el mismo comportamiento de anidación, ya sea prefiriendo construir nidos en el suelo, en cavidades de árboles o en otras características del hábitat. Si se sabe que varias especies son polinizadoras importantes, y si difieren en términos de temporada de vuelo, requisitos de anidación o distancia de vuelo, proporcione datos sobre cada una por separado. Si se dispone de pocos datos o ninguno, cree un único "protopolinizador" con datos tomados de los valores medios o de la opinión de personal experto sobre toda la comunidad de polinizadores. Cada fila es una única especie o gremio de polinizadores y las columnas deben ser nombradas y definidas como sigue:

	Columnas:

	- :investspec:`pollination guild_table_path.columns.species`
	- :investspec:`pollination guild_table_path.columns.nesting_suitability_[SUBSTRATE]_index` Los sustratos son definidos por usted, pero pueden incluir nidos en el suelo, cavidades de árboles, etc.
	- :investspec:`pollination guild_table_path.columns.foraging_activity_[SEASON]_index` Las estaciones son definidas por usted, pero pueden incluir la primavera, el verano, el otoño; húmedo, seco, etc.
	- :investspec:`pollination guild_table_path.columns.alpha` El modelo utiliza esta distancia estimada para definir el vecindario de flores disponibles alrededor de una celda determinada, y para ponderar las sumas de recursos florales y la abundancia de polinizadores en las fincas. Este valor puede determinarse mediante la distancia de forrajeo típica de una especie de abeja basada en una relación alométrica (véase Greenleaf et al. 2007).
	- :investspec:`pollination guild_table_path.columns.relative_abundance` Si se establece el mismo valor para cada especie, cada una de ellas tendrá la misma ponderación.

   *Ejemplo:* Una hipotética Tabla de Gremios con dos especies. Hay dos SUBESTRUCTURAS principales, "cavidad" y "suelo". La especie "Apis" utiliza tanto el tipo de nido de cavidad como el de suelo, y la especie "Bombus" solo utiliza los nidos de cavidad. Hay dos ESTACIONes, "primavera" y "verano". Las distancias típicas de vuelo, especificadas en metros (alfa), varían mucho entre especies. La abundancia_relativa de Bombus es mayor que la de Apis, lo que indica que hay más polinizadores Bombus que Apis.

   **Ejemplo de Tabla de gremios:**

   .. csv-table::
      :file: ../../invest-sample-data/pollination/guild_table.csv
      :header-rows: 1
      :widths: auto

- :investspec:`pollination farm_vector_path`

    .. note::
       El vector opcional de las explotaciones agrícolas sobrescribirá los valores de los recursos florales estacionales y los valores de idoneidad del sustrato de nidificación en las zonas que se superpongan al ráster LULC.

    Campos:

    - :investspec:`pollination farm_vector_path.fields.crop_type` En el caso de las fincas en las que se producen varios cultivos superpuestos, o cultivos en varias estaciones, debe incluirse un polígono de superposición separado para cada cultivo.
    - :investspec:`pollination farm_vector_path.fields.half_sat` Se trata de un parámetro ajustable que puede ser muy útil modificar tras una ejecución inicial del modelo y un examen de los resultados. Es :math:`h` en la ecuación :eq:`(pol. 6)`.
    - :investspec:`pollination farm_vector_path.fields.season`
    - :investspec:`pollination farm_vector_path.fields.fr_[SEASON]`
    - :investspec:`pollination farm_vector_path.fields.n_[SUBSTRATE]`
    - :investspec:`pollination farm_vector_path.fields.p_dep` Véase Klein et al. (2007) para las estimaciones de cultivos comunes.
    - :investspec:`pollination farm_vector_path.fields.p_managed` Se puede estimar como la proporción de la densidad de colmenas o la tasa de población recomendada. Véase Delaplane y Mayer (2000) para conocer las tasas de población recomendadas en Estados Unidos. Las oficinas de extensión agraria son también una buena fuente de información.

.. _interpreting-results:

Interpretación de los resultados
================================

Resultados finales
------------------

* **Registro de parámetros**: Cada vez que se ejecute el modelo, se creará un archivo de texto (.txt) en el Espacio de trabajo. El archivo enumerará los valores de los parámetros y los mensajes resultantes para esa ejecución y se nombrará según el servicio, la fecha y la hora. Cuando se ponga en contacto con NatCap por errores en una ejecución del modelo, incluya el registro de parámetros.

* **farm_results_[Suffix].shp**: (Solo se genera si se proporciona un vector de finca). Una copia del archivo de vectores de polígonos de la granja de input con los siguientes campos adicionales:

  * *p_abund*: abundancia media de polinizadores en la finca durante la temporada activa
  * *y_tot*: índice de rendimiento total, incluyendo los polinizadores silvestres y manejados y el rendimiento independiente de los polinizadores.
  * *pdep_y_w*: índice de rendimiento potencial dependiente de la polinización atribuible a los polinizadores silvestres.
  * *y_wild*: índice del rendimiento total atribuible a los polinizadores silvestres.
  
* **farm_pollinators_[Suffix].tif**: (Solo se genera si se proporciona un vector de finca). Abundancia total de polinizadores por píxel en todas las especies por temporada, recortada a la geometría de los polígonos del vector de finca.

* **pollinator_abundance_[SPECIES]_[SEASON]_[Suffix].tif**: Abundancia por píxel de las ESPECIES de polinizadores en la temporada ESTACIÓN.

* **pollinator_supply_[SPECIES]_[Suffix].tif**: Índice por píxel de las ESPECIES de polinizadores que podrían estar en un píxel dado su factor de abundancia arbitrario de la tabla, multiplicado por la idoneidad del hábitat para esa especie en ese píxel, multiplicado por los recursos florales disponibles a los que un polinizador podría volar desde ese píxel. (Ecuación 1)

* **total_pollinator_abundance_[SEASON]_[Suffix].tif**: (Solo se genera si se proporciona un vector de finca). Abundancia total de polinizadores por píxel en todas las especies por temporada.

* **total_pollinator_yield_[Suffix].tif**: (Solo se genera si se proporciona un vector de finca). Índice de rendimiento total de polinizadores por píxel para los píxeles que se superponen a las fincas, incluidos los polinizadores silvestres y los manejados.

* **wild_pollinator_yield_[Suffix].tif**: (Solo se genera si se proporciona un vector de finca). Índice de rendimiento de los polinizadores por píxel para los píxeles que se superponen a las fincas, solo para los polinizadores silvestres.

Resultados intermedios
^^^^^^^^^^^^^^^^^^^^^^

También puede examinar los resultados intermedios. Estos archivos pueden ayudar a determinar las razones de los patrones en los resultados finales, y también pueden ser utilizados para entender mejor el modelo, y solucionar problemas. Se encuentran en la carpeta *resultados_intermedios* (*intermediate_outputs*) dentro del directorio del espacio de trabajo definido para la ejecución del modelo, y la mayoría de ellos tienen nombres de archivo que dan una buena idea de lo que representa la capa.

Apéndice: Tabla de variables
============================

* :math:`x` - una coordenada de píxel.
* :math:`X` - conjunto de todos los píxeles del mapa de la cobertura del suelo.
* :math:`f(x)` - finca en el píxel x.
* :math:`F` - conjunto de todos los píxeles que se encuentran en las fincas.
* :math:`s` - especie de abeja.
* :math:`n` - tipo de nido (suelo, cavidad).
* :math:`N` - conjunto de todos los tipos de nidos.
* :math:`j` - estación (otoño, primavera, etc.).
* :math:`J` - conjunto de todas las estaciones (por ejemplo: {otoño, primavera}).
* :math:`fj(f, x)` - estación de polinización activa para la finca :math:`f` en el píxel :math:`x`.
* :math:`\alpha_s` - distancia media de forrajeo para la especie s.
* :math:`ns(s,n)` - preferencia de idoneidad de anidación para la especie :math:`s` en el tipo de anidación :math:`n`.
* :math:`HN(x,s)` - idoneidad de anidación del hábitat en el píxel :math:`x` para la especie :math:`s` [0,0, 1,0].
* :math:`N(l,n)` - índice de anidamiento del sustrato para el tipo de cobertura  vegetal :math:`l` para el tipo de sustrato :math:`n` en el rango :math:`[0.0, 1.0]`.
* :math:`RA(l,j)` - índice de abundancia relativa de recursos florales en el tipo de cobertura del suelo :math:`l` durante la estación :math:`j`. :math:`[0,0, 1,0]`.
* :math:`fa(s,j)` - actividad relativa de búsqueda de alimento para las especies :math:`s` durante la estación :math:`j`.
* :math:`FR(x,s)` - índice de recursos florales accesibles en el píxel :math:`x` para la especie :math:`s`.
* :math:`D(x,x')` - distancia euclidiana entre el centroide del píxel :math:`x` y :math:`x'`.
* :math:`PS(x,s)` - índice de suministro de polinizadores en el píxel :math:`x` para la especie :math:`s`.
* :math:`PA(x,s,j)` - abundancia de polinizadores en el píxel :math:`s` para la especie :math:`s`.
* :math:`PAT(x,j)` - abundancia total de polinizadores en la finca en el píxel :math:`x` en la estación :math:`j`, considerando todas las especies
* :math:`FP(x)` - la contribución potencial de la abundancia de polinizadores en la finca al rendimiento del cultivo dependiente de los polinizadores en un píxel de la finca durante la temporada en la que se necesita la polinización para esa finca.
* :math:`mp(f)` - abundancia de polinizadores manejados en la finca :math:`f` en relación con la tasa de carga recomendada.
* :math:`h(f)` - coeficiente de media saturación para la finca :math:`f`.
* :math:`PYT(x)` - rendimiento total atribuible a los polinizadores en el píxel x para la temporada :math:`j`, teniendo en cuenta los polinizadores silvestres y manejados.
* :math:`PYW(x)` - rendimiento atribuible a los polinizadores silvestres en el píxel x para la estación :math:`j`.
* :math:`sa(s)` - índice de abundancia relativa de las especies :math:`s`.
* :math:`YT(f)` - rendimiento medio de la finca para la parcela :math:`f` considerando la dependencia de los polinizadores del cultivo.
* :math:`YW(f)` - proporción del rendimiento medio de la finca para la parcela :math:`f` atribuible a los polinizadores silvestres, considerando la dependencia de los polinizadores del cultivo.
* :math:`\nu(f)` - proporción del rendimiento del cultivo que depende de la polinización.

Apéndice: Fuentes de datos
==========================

.. note:: Los datos de muestra solo sirven para ilustrar la estructura de datos y no deben utilizarse como fuente de datos.

Dependencia de los cultivos de los polinizadores
------------------------------------------------
Véase Klein et al. 2007 para una lista de cultivos de importancia mundial y su dependencia de los polinizadores animales.

Idoneidad de la anidación y disponibilidad de recursos florales
---------------------------------------------------------------
Koh et al. 2016 presentan datos de idoneidad de anidación y disponibilidad de recursos florales para 45 categorías de uso del suelo.

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

Referencias
===========

Allen-Wardell, G., P. Bernhardt, R. Bitner, A. Burquez, S. Buchmann, J. Cane, PA Cox, V. Dalton, P. Feinsinger, M. Ingram, D. Inouye, CE Jones, K. Kennedy, P. Kevan y . Koopowitz. 1998. The potential consequences of pollinator declines on the conservation of biodiversity and stability of food crop yields. Conservation Biology 12: 8-17.

Cane, JH. 1997. Lifetime monetary value of individual pollinators: the bee habropoda laboriosa at rabbiteye blueberry (vaccinium ashei reade). Acta Horticulturae 446: 67-70.

Costanza, R., R. d'Arge, R. de Groot, S. Farber, M. Grasso, B. Hannon, K. Limburg, S. Naeem, RV O'Neill, J. Paruelo, RG Raskin, P. Sutton y T. van den Belt. 1997. The value of the world's ecosystem services and natural capital. Nature 387: 253-260.

Delaplane, KS y F Mayer. 2000. Crop pollination by bees. CABI Publishing, Nueva York.

Free, JB. 1993. Insect pollination of crops. Academic Press, Londres.

Greenleaf, SS, NM Williams, R. Winfree y C. Kremen. 2007. Bee foraging ranges and their relationship to body size. Oecologia 153: 589-596.

Greenleaf, SS y C. Kremen. 2006. Wild bee species increase tomato production and respond differently to surrounding land use in Northern California. Biological Conservation 133:81-87.

Klein, AM, BE Vaissiere, JH Cane, I. Steffan-Dewenter, SA Cunningham, C. Kremen y T. Tscharntke. 2007. Importance of pollinators in changing landscapes for world crops. Proceedings of the Royal Society B-Biological Sciences 274: 303-313.

Koh, I., E. Lonsdorf, N. Williams, C. Brittain, R. Isaacs, J. Gibbs y T. Ricketts. 2016. Modeling the status, trends, and impacts of wild bee abundance in the United States. Proceedings of the National Academy of Sciences 113 (1) 140-145; DOI: 10.1073/pnas.1517685113

Kremen, C., NM Williams, RL Bugg, JP Fay y RW Thorp. 2004. The area requirements of an ecosystem service: crop pollination by native bee communities in California. Ecology Letters 7: 1109-1119.

Lonsdorf, E., C. Kremen, T. Ricketts, R. Winfree, N. Williams y SS Greenleaf. 2009. Modelling pollination services across agricultural landscapes. Annals of Botany 1: 12. en línea [https://pubmed.ncbi.nlm.nih.gov/19324897/]

Lonsdorf, E., TH Ricketts, CM Kremen, NM Williams y S. Greenleaf. en prensa. Pollination services in P. Kareiva, TH Ricketts, GC Daily, H. Tallis y S. Polasky, eds. The theory and practice of ecosystem service valuation.

Losey, JE y M. Vaughan. 2006. The economic value of ecological services provided by insects. Bioscience 56: 311-323.

Nabhan, GP y SL Buchmann. 1997. Services provided by pollinators. Pages 133-150 in GC Daily, ed. Nature's services. Island Press, Washington, D.C.

Olsson, O. A. Bolin, H. Smith y E. Lonsdorf. 2015. Modeling pollinating bee visitation rates in heterogeneous landscapes from foraging theory. Ecological Modelling 316: 133-143.

Priess, JA, M. Mimler, AM Klein, S. Schwarze, T. Tscharntke y I. Steffan-Dewenter. 2007. Linking deforestation scenarios to pollination services and economic returns in coffee agroforestry systems. Ecological Applications 17: 407-417.

Ricketts, TH. 2004. Tropical forest fragments enhance pollinator activity in nearby coffee crops. Conservation Biology 18: 1262-1271.

Ricketts, TH, NM Williams y MM Mayfield. 2006. Connectivity and ecosystem services: crop pollination in agricultural landscapes. Pages 255-289 in M. Sanjayan y K. Crooks, eds. Connectivity for Conservation. Cambridge University Press, Cambridge, RU.

Roubik, DW y M. Aluja. 1983. Flight ranges of Melipona and Trigona in tropical forest. Journal of the Kansas Entomological Society 56: 217-222.

Southwick, EE y L. Southwick. 1992. Estimating the economic value of honey-bees (Hymenoptera; Apidae) as agricultural pollinators in the United States. Journal of Economic Entomology 85: 621-633.

Winfree, R., J. Dushoff, EE Crone, CB Schultz, RV Budny, NM Williams y C. Kremen. 2005. Testing simple indices of habitat proximity. American Naturalist 165(6): 707-717.
