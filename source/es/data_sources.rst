.. _data_sources:

****************
Fuentes ed datos
****************

Se trata de una recopilación de fuentes de datos y sugerencias para los inputs comunes de los modelos. Esta lista no es definitiva y solo pretende servir de punto de partida. Se recomienda encarecidamente buscar datos más locales y precisos (de fuentes nacionales, estatales, universitarias, bibliográficas, de ONG y otras) y solo utilizar datos globales para los análisis finales si no se dispone de nada más local. Si conoce alguna fuente de datos útil que no figure en esta lista, compártala en el foro.

.. _dem:

Modelo digital de elevacion
---------------------------
Un modelo digital de elevación (MDE) es un mapa ráster de elevación, donde el valor de cada píxel es su elevación sobre el nivel del mar (normalmente en metros). Los datos del MDE están disponibles para cualquier zona del mundo, aunque con distintas resoluciones.

Los datos globales en bruto de MDE están disponibles de forma gratuita en:

 * The World Wildlife Fund - https://www.worldwildlife.org/pages/hydrosheds
 * NASA: https://asterweb.jpl.nasa.gov/gdem.asp (30m resolution); y fácil acceso a los datos SRTM: http://dwtkns.com/srtm/
 * USGS: https://earthexplorer.usgs.gov/

La resolución del MDE puede ser un parámetro muy importante dependiendo de los objetivos del proyecto. Por ejemplo, si los responsables de la toma de decisiones necesitan información sobre el impacto de las carreteras en los servicios ecosistémicos, se necesita una resolución fina. Los aspectos hidrológicos del MDE utilizado en el modelo deben ser correctos. La mayoría de los datos en bruto del MDE tienen errores, por lo que es probable que haya que rellenar el MDE para eliminar los sumideros. Múltiples pasadas de la herramienta de relleno de ArcGIS, o del algoritmo de relleno de QGIS Wang & Liu (biblioteca SAGA) han dado buenos resultados. 
 
En el caso de los modelos hidrológicos que generan corrientes  a partir del MDE, hay que fijarse bien en el resultado del ráster de la red de corrientes. Si las corrientes no son continuas, sino que están divididas en trozos, el MDE todavía tiene sumideros que deben ser llenados. Si al llenar los sumideros varias veces no se crea una red de corrientes continua, tal vez haya que probar con otro MDE. Si los resultados muestran un patrón de red inesperado, puede deberse a la reproyección del MDE con un método de interpolación "vecino más cercano" en lugar de "bilineal" o "cúbico". En este caso, vuelva a los datos en bruto del MDE y reproyéctelos utilizando el método "bilineal" o "cúbico".

Consulte también la sección Trabajo con el MDE de esta guía de uso para obtener más detalles y orientación sobre el procesamiento de MDE.

.. _lulc:

Uso del suelo/cobertura del suelo
---------------------------------
El uso de la tierra/cobertura del suelo (LULC) describe las propiedades físicas de la tierra y/o el modo en que la gente la utiliza (bosque, humedal, agua, pavimentado, agrícola, reserva natural, etc.). Para mostrar los datos en formato ráster, cada categoría LULC se asigna a un código entero (estos códigos no tienen que ser consecutivos u ordenados). Las brechas de datos desconocidos deben aproximarse siempre que sea posible para evitar que falten datos (agujeros) en las capas resultantes.

Los datos globales de uso del suelo están disponibles en varias fuentes, incluyendo:

 * NASA: https://lpdaac.usgs.gov/products/mcd12q1v006/ (datos plurianuales de la cubierta terrestre mundial de MODIS proporcionados en varias clasificaciones)
 * European Space Agency WorldCover a 10m de resolución: https://esa-worldcover.org/
 * European Space Agency Climate Change Initiative land cover a 300m de resolución: https://www.esa-landcover-cci.org/

Los datos correspondientes a los Estados Unidos son proporcionados por el USGS y el Departamento del Interior a través de la base de datos nacional sobre la cubierta terrestre: https://www.usgs.gov/centers/eros/science/national-land-cover-database

La categorización más sencilla de LULC en el paisaje implica la delimitación solo por la cubierta del suelo (por ejemplo, tierras de cultivo, bosques, pastizales). Existen varias clasificaciones globales y regionales de la cubierta terrestre (por ejemplo, Anderson et al. 1976), y a menudo se ha realizado una clasificación detallada de la cubierta terrestre para el paisaje de interés. Muchos países disponen de mapas nacionales de LULC que pueden utilizarse.

Es importante evaluar cualquier mapa de ocupación del suelo para comprobar su precisión en la zona de estudio. Los productos globales, en particular, suelen ser más precisos en algunos lugares (o con algunos tipos de cobertura del suelo) que en otros. 

La categorización de los tipos de uso del suelo depende del modelo y de la cantidad de datos disponibles para cada uno de los tipos de suelo. Normalmente, el input de la tabla biofísica asigna ciertos parámetros biofísicos relevantes a cada código LULC. Solo se debería dividir un tipo de LULC si esto proporciona más precisión en la modelización. Por ejemplo, solo debe dividir los "cultivos" en diferentes tipos de cultivos si tiene información sobre la diferencia de los parámetros biofísicos relevantes.

*Ejemplo típico de tabla de uso y cobertura del suelo - la suya probablemente sea diferente*

  ====== =======================================
  lucode Uso del suelo/cobertura del suelo
  ====== =======================================
  1      Bosque perennifolio de hojas aciculares
  2      Bosque perennifolio de hoja ancha
  3      Bosque caducifolio de hojas aciculares
  4      Bosque caducifolio de hoja ancha
  5      Cubierta mixta
  6      Bosques
  7      Pastizal arbolado
  8      Matorral cerrado
  9      Matorral abierto
  10     Pastizales
  11     Tierras de cultivo (cultivos en hilera)
  12     Suelo desnudo
  13     Urbano y construido
  14     Humedal
  15     Mixto de hoja perenne
  16     Bosque mixto
  17     Huertos/Viñedos
  18     Pastos
  ====== =======================================

.. _carbon_pools:

Reservas de carbono
-------------------
Los datos de almacenamiento de carbono deben ser iguales a los valores medios de almacenamiento de carbono para cada clase de LULC. La fuente de datos ideal para todas las reservas de carbono es un conjunto de estimaciones locales sobre el terreno, en las que se haya medido directamente el almacenamiento de carbono de todas las reservas pertinentes. Estas pueden resumirse en el mapa LULC, incluyendo cualquier estratificación por edad u otra variable. Sin embargo, si estos datos no están disponibles, hay varias fuentes de datos generales que pueden utilizarse.

Nótese que varias fuentes, incluido el IPCC (2006), informan en unidades de biomasa, mientras que InVEST utiliza la masa de carbono elemental. Para convertir toneladas métricas de biomasa en toneladas métricas de C hay que multiplicarlas por un factor de conversión, que suele variar entre 0,43 y 0,51. Los factores de conversión para los distintos tipos de árboles principales y regiones climáticas se enumeran en la Tabla 4.3 de la página 4.48 de IPCC (2006).

.. _aboveground_carbon:

Carbono almacenado en la biomasa aérea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Una buena fuente de datos, aunque muy general, para el almacenamiento de carbono es la metodología de 2006 del Grupo Intergubernamental de Expertos sobre el Cambio Climático (IPCC) para determinar los inventarios de gases de efecto invernadero en el sector de la agricultura, la silvicultura y otros usos de la tierra (https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html). Para utilizar este conjunto de información del IPCC, debe conocer el dominio climático y la región de su emplazamiento; utilice los datos de la Tabla 4.1 de la página 4.46 y una copia digital del mapa de ecorregiones de la Organización de las Naciones Unidas para la Agricultura y la Alimentación (FAO) (http://www.fao.org/geonetwork/srv/en/main.home) para averiguarlo. Las tablas 5.1 a 5.3 (p. 5.9) del IPCC (2006) ofrecen estimaciones de la biomasa aérea en tierras agrícolas con biomasa leñosa perenne (por ejemplo, huertos frutales, agrosilvicultura, etc.). Las tablas 4.7, 4.8 y 4.12 ofrecen estimaciones de biomasa aérea para tipos de bosques naturales y plantaciones. 

Ruesch y Gibbs (2008) cartografiaron los datos de almacenamiento de carbono en biomasa aérea del IPCC (2006) a partir de los datos de cobertura terrestre del año 2000, a los que se puede acceder en: https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html. Lamentablemente, estos datos no están bien documentados, pero "lut.zip" contiene una tabla de valores de carbono para cada ecorregión. La tabla no enumera las unidades explícitamente, pero los archivos .xml de metadatos indican que los valores están en toneladas de C por hectárea.

Se pueden encontrar otras fuentes generales de estimaciones de almacenamiento de carbono. Por ejemplo, Grace et al. (2006) estiman el promedio de almacenamiento de carbono por encima del suelo (hoja + madera) para los principales ecosistemas de sabana de todo el mundo (Tabla 1). Houghton (2005) da el almacenamiento de carbono por encima del suelo para los tipos de bosques naturales y de plantación, por continente (Tablas 1 y 3). Brown et al. (1989) ofrecen estimaciones de la biomasa aérea de los bosques tropicales de hoja ancha en función del uso de la tierra: no perturbado, talado y no productivo (Tabla 7). También existen fuentes de datos de almacenamiento de carbono específicas para cada región. Las que hemos encontrado incluyen:

* América Latina: Malhi et al. (2006) informan de los volúmenes de biomasa sobre el suelo de 227 parcelas de bosque de tierras bajas en Bolivia, Brasil, Colombia, Ecuador, Guayana Francesa, Guyana, Panamá, Perú y Venezuela. Nascimento y Laurance (2002) estiman las reservas de carbono sobre el suelo en veinte parcelas de 1 ha de selva amazónica. Tiessen et al. (1998) encuentran reservas de carbono sobre el suelo para los tipos de sabana brasileña Caatingas y Cerrados.

* África: Zhang y Justice (2001) informan de las reservas de carbono sobre el suelo de los principales tipos de LULC de bosques y arbustos de los países de África central. Tiessen et al. (1998) estiman la biomasa aérea total de la sabana degradada en Senegal. Makundi (2001) informa sobre el crecimiento medio anual de tres tipos de plantaciones forestales en Tanzania. Malimbwi et al. (1994) estiman las reservas de carbono sobre el suelo en los bosques de miombo de la Reserva Forestal de Kitungalo en Tanzania. Munishi y Shear (2004) informan de las reservas de carbono sobre el suelo en los bosques húmedos afromontanos de las montañas del Arco Oriental de Tanzania. Glenday (2006) calcula las reservas de carbono sobre el suelo de tres tipos de bosque en el bosque nacional de Kakamega, en el oeste de Kenia.

* América del Norte: Smith et al. (2006) estiman las reservas de carbono sobre el suelo de los principales tipos de bosques de Estados Unidos.

* El Estimador de Carbono en Línea (https://www.ncasi.org/resource/carbon-on-line-estimator-cole/) es una herramienta para calcular las características del carbono en los bosques de EE.UU. basada en los datos del Inventario y Análisis Forestal y de la Evaluación de Planificación de Recursos del Servicio Forestal del USDA. Con esta herramienta se pueden examinar las características del carbono a escala de condados. Utilizando la pestaña de variables, se pueden seleccionar los reservorios de carbono por encima del suelo, por debajo del suelo o de la madera muerta.

* Coomes et al. (2002) estiman las reservas de carbono sobre el suelo para los tipos de arbustos y bosques nativos de Nueva Zelanda.

La biomasa aérea (y, por tanto, las reservas de carbono) también puede calcularse a partir de los inventarios de madera que suelen realizar los ministerios forestales en un conjunto de parcelas. Utilice la siguiente fórmula para estimar las existencias de carbono por encima del suelo en una masa forestal que haya sido inventariada por su volumen comercializable, donde VOB es el volumen por hectárea de los árboles en metros cúbicos medido desde el tocón del árbol hasta el punto de la copa (la parte comercializable del árbol), WD es la densidad de la madera de los árboles (biomasa seca por unidad de volumen del árbol), BEF es la relación entre la biomasa seca total por encima del suelo y la biomasa seca del volumen inventariado, y CF es la relación entre el carbono elemental y la biomasa seca, en masa (Brown 1997). El factor de expansión de la biomasa (BEF) tiene en cuenta el C almacenado en todas las demás partes del árbol por encima del suelo (por ejemplo, ramas, corteza, tallos, follaje, etc.; las partes no comercializables del árbol). En la mayoría de los casos, la DT de una parcela se aproxima con los valores de las especies dominantes. Brown (1997) proporciona una tabla de valores de DAP para muchas especies arbóreas en el Apéndice 1 de la sección 3 y un método para calcular el BEF (Ecuación 3.1.4). Véase en ECCM (2007) una aplicación de este método de la FAO a los datos del inventario forestal del este de Tanzania. El IPCC (2006) también presenta estimaciones de ( ) donde los valores de BEF para las masas forestales de latifoliadas, pinos, coníferas y bosques naturales por ecorregión se dan en la Tabla 4.5 y los valores de WD para muchas especies se dan en las Tablas 4.13 y 4.14 (utilice los valores de BCEF de la Tabla 4.5 que llevan el subíndice S.) Finalmente, Brown et al. (1989) presentan el BEF para los bosques tropicales de hoja ancha bajo tres usos de la tierra: inalterados, talados y no productivos.

Brown (1997) hace varias advertencias sobre el uso de la ecuación anterior. En primer lugar, la ecuación está diseñada para rodales inventariados que son cerrados en contraposición a los abiertos (bosques con una cobertura de dosel más escasa, como la sabana de robles). En segundo lugar, las estimaciones del VOB deben ser una función de todas las especies de árboles que se encuentran en el rodal, no solo de la madera económicamente más valiosa. En tercer lugar, los árboles con diámetros tan bajos como 10 centímetros a la altura del pecho (DAP = 10) deben incluirse en el inventario para que esta ecuación del carbono de la biomasa sobre el suelo sea lo más precisa posible. Brown (2002) también señala que el uso de un único valor de BEF es una simplificación del proceso real de crecimiento de la biomasa.

Estas advertencias llevaron a que Brown (2002) recomendase el uso de ecuaciones alométricas de biomasa para estimar la biomasa leñosa sobre el suelo, si están disponibles. Estas ecuaciones dan la relación estimada entre la distribución de árboles de diferente tamaño de un rodal y su biomasa aérea. Brown (1997) y Brown y Schroeder (1999) proporcionan ecuaciones alométricas generales de la biomasa aérea para todas las ecorregiones del mundo y el este de EE.UU., respectivamente. Cairns et al. (2000) proporcionan ecuaciones alométricas de la biomasa aérea para los tipos de LULC en el sur de México. Nascimento y Laurance (2002) estiman la biomasa aérea de la selva amazónica utilizando curvas alométricas. El uso de estas ecuaciones requiere conocer la distribución del tamaño de los árboles en un rodal determinado.

Algunas investigaciones han facilitado el uso de estas ecuaciones relacionando en primer lugar la distribución de los árboles de distinto tamaño de un rodal con su edad y, a continuación, trazando la relación entre la edad y la biomasa aérea. Por ejemplo, Silver et al. (2000) han estimado la biomasa aérea en función de la edad del rodal (es decir, los años transcurridos desde la forestación/reforestación) o el LULC anterior para los tipos de bosque nativo en los ecosistemas tropicales. Smith et al. (2006) llevan la transformación de las ecuaciones alométricas un paso más allá al relacionar la edad con el carbono total de la biomasa (subterráneo más aéreo) directamente para varios bosques de Estados Unidos.

Cuando se utilizan los datos del IPCC u otras fuentes de datos amplias similares, una última cuestión que hay que considerar es cómo afecta el nivel de perturbación antropogénica a las reservas de carbono. Las reservas de C sobre el suelo de las zonas muy perturbadas serán probablemente inferiores a las de las zonas no perturbadas. No está claro qué tipo de niveles de perturbación asumen el IPCC u otras fuentes similares cuando informan de las estimaciones de biomasa aérea. Si la perturbación de los bosques es un problema en el sitio de demostración, los tipos de LULC deberían estratificarse por niveles de perturbación. Para un ejemplo de dicha estratificación, véase el Cuadro 2.5, página 14 de ECCM (2007).

Finalmente, por lo general no tratamos el material herbáceo sobre el suelo como una reserva de carbono (por ejemplo hierba, flores, cultivos no mderables). Nuestra suposición de trabajo es que este material no representa una fuente potencial a largo plazo de biomasa leñosa, biomasa bajo el suelo o suelo. En general el material herbáceo recicla su carbono demasiado rápido.

.. _belowground_biomass:

Carbono almacenado en la biomasa subterránea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para las categorías LULC dominadas por la biomasa leñosa, la biomasa subterránea se puede estimar aproximadamente con la relación "raíz a brote" de la biomasa subterránea a la aérea. Las estimaciones predeterminadas de la relación raíz a brote se dan en la Tabla 4.4 en la pág. 4.49 del IPCC (2006) por ecorregión. En la Sección 3.5 de Brown (1997) también se dan estimaciones amplias de esta relación.

Algunos tipos de LULC contienen poca o ninguna biomasa leñosa, pero sí importantes existencias de carbono subterráneo (p. ej., pastizales naturales, pastizales gestionados, estepas y áreas de matorrales/matorrales). En estos casos, no se aplica la proporción de raíces a brotes descrita anteriormente. Las estimaciones subterráneas para estos tipos de LULC se estiman mejor a nivel local, pero si los datos locales no están disponibles, se pueden usar algunas estimaciones globales. El IPCC (2006) enumera la biomasa total (superficial y subterránea) y la biomasa aérea para cada zona climática en la tabla 6.4 (pág. 6.27). La diferencia entre estos números es una estimación cruda de la biomasa subterránea. Recientemente, Ruesch y Gibbs (2008) mapearon los datos de almacenamiento de carbono de la biomasa aérea del IPCC (2006) dados los datos de cobertura terrestre del año 2000, a los que se puede acceder aquí: https://cdiac.ess-dive.lbl.gov/epubs/ndp/ global_carbon/carbon_documentation.html.

Varios estudios han recopilado estimaciones de la biomasa subterránea o de la relación raíz-brote para diferentes tipos de hábitat. Entre estos encontramos:

* Grace et al. (2006) estiman la biomasa promedio total de raíces leñosas y herbáceas para los principales ecosistemas de sabana en todo el mundo (Tabla 1). Baer et al. (2002) y Tilman et al. (2006) estiman el C almacenado en las raíces de parcelas restauradas con pastos C4 nativos en Nebraska y Minnesota, EE.UU., respectivamente, en función de los años transcurridos desde la restauración (consulte la Tabla 2 en Baer et al. (2002) y la Figura 1D en Tilman et al. (2006)).

* Cairns et al. (1997) examinan las proporciones de raíz a brote para los tipos de LULC en todo el mundo. Munishi y Shear (2004) utilizan una proporción de 0,22 para los bosques afromontanos en los bosques del arco oriental de Tanzania. Malimbwi et al. (1994) utilizan 0,20 para bosques de miombo en la misma zona de Tanzania. Coomes et al. (2002) utilizan 0,25 para matorrales en Nueva Zelanda. Gastón et al. (1998) reportan una relación raíz-vástago de 1 para sabanas africanas de pastos/arbustos.

.. _soil_carbon:

Carbono almacenado en la biomasa subterránea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si las estimaciones de C del suelo locales o regionales no están disponibles, se pueden consultar las estimaciones predeterminadas del IPCC (2006) para cultivos, pastizales y pastos manejados. La Tabla 2.3 del IPCC (2006) contiene estimaciones de las reservas de carbono del suelo por tipo de suelo, asumiendo que estas reservas están en equilibrio y no tienen una gestión activa de la tierra. Para los tipos de LULC de tierras de cultivo y pastizales, esta estimación predeterminada se puede multiplicar por los factores de gestión, enumerados en las Tablas 5.5 y 6.2 del IPCC (2006). Para todos los demás tipos de LULC y sus esquemas de gestión relacionados, el IPCC (2006) no asume factores de gestión.

Existen fuentes alternativas a nivel mundial de datos de carbono del suelo. Post et al. (1982) informan las existencias de carbono en el primer metro de suelo mediante el sistema de clasificación de zonas de vida de Holdridge (mapa SIG de estas zonas disponible en http://www.arcgis.com/home/item.html?id=f3ec7241777f4c56a69ae14d2a98e44b). Silver et al. (2000) han estimado el carbono del suelo en función de los años transcurridos desde la forestación/reforestación para tipos de bosques nativos en ecosistemas tropicales. Grace et al. (2006) estiman el carbono del suelo para los principales tipos de sabana en todo el mundo (Tabla 1). Detwiler (1986) enumera el carbono del suelo para suelos de bosques tropicales en la Tabla 2.

Varios estudios específicos por región también informan sobre las existencias de carbono en el suelo. Los que hemos encontrado incluyen:

* Norteamérica: Smith et al. (2006) calculan el C del suelo por cada incremento de 5 años hasta 125 años desde la forestación/reforestación para todos los principales tipos de bosques y prácticas de manejo forestal en cada región de los EE. UU. Otros incluyen a McLauchlan et al. (2006), Tillman et al. (2006)mç, Fargione et al. (2008), Schumann et al. (2002) y Lal (2002).

* África: Houghton y Hackler (2006) dan el C del suelo para 5 tipos LULC de bosques (bosques lluviosos, bosques secos húmedos, bosques, matorrales y bosques montanos) en el África subsahariana que han conservado su cubierta natural y para áreas forestales que se han convertido en tierras de cultivo, cultivos migratorios y pastos. Vagen et al. (2005) proporciona estimaciones de C del suelo para varios tipos de LULC en el África subsahariana.

* América del Sur: Bernoux et al. (2002) estimaron las reservas de C del suelo a una profundidad de 30 cm para diferentes asociaciones de tipo de suelo y vegetación en Brasil. Por ejemplo, las reservas de C del suelo en suelos HAC en 14 categorías diferentes de cobertura terrestre, incluidos los bosques amazónicos y el Cerrado brasileño, oscilan entre 2 y 116 kg C m-2.

Nota importante: En la mayoría de las investigaciones que estiman las tasas de almacenamiento y secuestración de carbono en un paisaje, las medidas de la reserva de suelo solo incluyen el carbono orgánico del suelo (COS) en suelos minerales (Post y Kwon 2000). Sin embargo, si el ecosistema que se está modelizando tiene muchos suelos orgánicos (por ejemplo, humedales o páramo), es fundamental agregar este componente al contenido mineral del suelo. En paisajes donde la conversión de humedales a otros usos de la tierra es común, también se debe seguir de cerca las emisiones de carbono de los suelos orgánicos (IPCC 2006).

.. _dead_carbon:

Carbono almacenado en la materia orgánica muerta
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si no se dispone de estimaciones locales o regionales del carbono almacenado en la materia orgánica muerta, se pueden asignar valores predeterminados del IPCC (2006). La Tabla 2.2 (pág. 2.27) proporciona reservas de carbono por defecto para la hojarasca en tipos de LULC boscosos. Para los tipos no boscosos, la hojarasca es cercana a 0. Grace et al. (2006) estiman el carbono promedio almacenado en la hojarasca para los principales ecosistemas de sabana de todo el mundo (Tabla 1). No está claro si sus estimaciones totales de "biomasa sobre el suelo" incluyen madera muerta o no. Las existencias de madera muerta son más difíciles de estimar en general, y no hemos localizado fuentes de datos predeterminadas.

Estimaciones regionales:

* Estados Unidos: Smith et al. (2006) estiman el almacenamiento de carbono en la hojarasca (denominada C "suelo del bosque" en el documento) y madera muerta (el conjunto de reservas de C denominadas "árboles muertos en pie" y "madera muerta caída" en el documento) para todos principales tipos de bosques y prácticas de manejo forestal en cada región de los EE.UU. en función de la edad del rodal.

* América del Sur: Delaney et al. (1998) estiman el carbono almacenado en madera muerta en pie y caída en 6 bosques tropicales de Venezuela. Según los autores, la madera muerta suele ser 1/10 de la cantidad de biomasa que la vegetación aérea.


Precipitación
-------------

.. _precipitation:

Precipitación anual y mensual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
La precipitación puede interpolarse a partir de datos puntuales de pluviómetros a largo plazo. Al considerar los datos de los pluviómetros, asegúrese de que brinden una buena cobertura sobre el área de interés, especialmente si hay grandes cambios en la elevación que hacen que las cantidades de precipitación sean heterogéneas dentro del área de estudio. Idealmente, los medidores tendrán al menos 10 años de datos continuos, sin grandes brechas, aproximadamente el mismo período de tiempo que el mapa de uso del suelo/cobertura del suelo utilizado como input. Debe incluirse la precipitación en forma de nieve.

Los conjuntos de datos globales procedentes de modelos de teledetección pueden dar cuenta de zonas remotas si no se dispone de datos de campo. Se pueden utilizar datos gruesos de los conjuntos de datos globales de libre acceso desarrollados por la Unidad de Investigación Climática: http://www.cru.uea.ac.uk o WorldClim: https://www.worldclim.org/, entre otros. Un lugar útil para buscar datos sobre precipitaciones es la Guía de Datos Climáticos del NCAR: https://climatedataguide.ucar.edu/climate-data.

Algunas fuentes (como WorldClim) proporcionan 12 rásteres de precipitaciones medias mensuales. Para utilizarlos en el modelo de rendimiento hídrico anual, los rásteres mensuales deben sumarse para calcular un mapa de precipitaciones medias anuales.

Dentro de los Estados Unidos, el grupo PRISM de la Universidad Estatal de Oregón proporciona datos de precipitación gratuitos con una resolución de 30 segundos de arco. Visite su sitio web en https://prism.oregonstate.edu/ y navegue hasta '800m Normals' para descargar datos.

.. _rain_events:

Eventos de lluvia
^^^^^^^^^^^^^^^^^
El número promedio de eventos de lluvia mensuales se puede obtener de las estadísticas climáticas locales (Oficina de Meteorología) o de los recursos en línea:

 * https://www.yr.no/
 * http://wcatlas.iwmi.org
 * El Banco Mundial también proporciona mapas con estadísticas de precipitación: https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api


Evapotranspiración
------------------

.. _et0:

Evapotranspiración de referencia
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
La evapotranspiración de referencia, ET₀, mide la cantidad de agua que se vaporiza desde la tierra hacia el aire durante un período de tiempo determinado. Es la suma de la evaporación (directamente del suelo, cuerpos de agua y otras superficies) y la transpiración (a través de las plantas). Por lo general, se expresa como una profundidad de agua en milímetros por unidad de tiempo: :math:`mm/month` para mensual, :math:`mm/year` para anual. (Nota: similar a la precipitación, la "profundidad" del agua es la que se evapora de una región dada; no es "por" píxel, metro cuadrado o cualquier otra unidad de área). Todos los modelos InVEST usan esta medida, pero algunas fuentes expresan la evapotranspiración como un volumen o energía por área. Consulte http://www.fao.org/3/x0490e/x0490e04.htm para obtener más detalles.

CGIAR proporciona un mapa global de evapotranspiración potencial, basado en datos climáticos de WorldClim, que puede usarse como ET de referencia: https://cgiarcsi.community/data/global-aridity-and-pet-database/.

Si está ejecutando un modelo que requiere tanto la precipitación como la evapotranspiración como inputs, asegúrese de que los datos de ET se basen en los mismos datos de precipitación que se utilizan como input del modelo.

La evapotranspiración de referencia varía con la elevación, la latitud, la humedad y el aspecto de la pendiente. Hay muchas metodologías, que varían en requisitos de datos y precisión.

Puede calcular la ET de referencia mediante el desarrollo de cuadrículas mensuales promedio de precipitación y temperaturas máximas y mínimas. Estos datos pueden provenir de estaciones meteorológicas, donde puede seguir el mismo proceso que el desarrollo de la cuadrícula de precipitación anual promedio, incluida la incorporación de los efectos de la elevación al interpolar entre estaciones. O bien, tanto WorldClim como CRU brindan datos de temperatura mensuales ya en formato de cuadrícula. Estas cuadrículas mensuales se pueden usar como input para las ecuaciones que se enumeran a continuación.

Puede calcular la ET de referencia mediante el desarrollo de cuadrículas mensuales promedio de precipitación y temperaturas máximas y mínimas (también disponibles en WorldClim y CRU) que deben incorporar los efectos de la elevación al interpolar desde las estaciones de observación. Los datos para desarrollar estas cuadrículas mensuales de precipitación y temperatura siguen el mismo proceso en el desarrollo de las cuadrículas de 'Precipitación mensual'.

Una forma sencilla de determinar la evapotranspiración de referencia es la ecuación "Hargreaves modificada" (Droogers y Allen, 2002), que genera resultados superiores a la Pennman-Montieth cuando la información es incierta. 

.. math:: ET_0 = 0.0013\times 0.408\times RA\times (T_{av}+17)\times (TD-0.0123 P)^{0.76}

El método "Hargreaves modificado" utiliza la media de las temperaturas máximas y mínimas medias diarias de cada mes (`Tavg` en grados Celsius), la diferencia entre las temperaturas máximas y mínimas medias diarias de cada mes (`TD`), la radiación extraterrestre (:math:`RA` en :math:`\mathrm{MJm^{-2}d^{-1}}) y la precipitación media mensual (:math:`P` en mm por mes), todo lo cual puede obtenerse con relativa facilidad.

Puede utilizar esta ecuación en datos ráster. Tenga en cuenta que calcula la ET0 media diaria, por lo que el resultado deberá multiplicarse por el número de días del mes cuyos valores de entrada esté utilizando, y deberá ejecutarse una vez para cada mes. Los rásteres ET0 mensuales resultantes pueden utilizarse en el modelo de Rendimiento Hídrico Estacional. Para el modelo de Rendimiento Hídrico Anual, sume los ráster ET0 mensuales para obtener la ET0 media anual.

Los datos de temperatura y precipitación suelen obtenerse a partir de gráficos regionales, mediciones directas o conjuntos de datos nacionales o mundiales (como WorldClim). Para los datos de radiación, por otra parte, es mucho más caro medirlos directamente, pero pueden estimarse de forma fiable a partir de herramientas, tablas o ecuaciones en línea. El documento de la FAO Irrigation Drainage Paper 56 (Allan (1998)) ofrece datos mensuales sobre radiación en el Anexo 2; para utilizarlos, seleccione los valores correspondientes a la latitud más cercana a su zona de estudio. Otra opción es utilizar una herramienta SIG para calcular la radiación solar de su zona de estudio específica y utilizar esta capa espacial como entrada para el cálculo de Hargreaves modificado. 
La evapotranspiración de referencia también se puede calcular mensual y anualmente utilizando la ecuación de Hamon (Hamon 1961, Wolock y McCabe 1999):

.. math:: PED_{Hamon} = 13.97 d D^2W_t

donde :math:`d` es el número de días en un mes, :math:`D` es el promedio mensual de horas de luz diurna calculadas para cada año (en unidades de 12 horas), y :math:`W_t` es un saturado término de densidad de vapor de agua calculado por:

.. math:: W_t = \frac{4.95e^{0.062 T}}{100}

donde :math:`T` es la temperatura media mensual en grados Celsius. La evapotranspiración de referencia se establece en cero cuando la temperatura media mensual es inferior a cero. Luego, para cada año durante el período de tiempo analizado, los valores de ETP calculados mensualmente en cada celda de la cuadrícula se suman para calcular un mapa del ETP anual para cada año.

Un método final para evaluar la ETo, cuando se dispone de datos de evaporación en bandeja, es usar la siguiente ecuación:

:math:`ETo = pan ET *0.7` (Allen et al., 1998).

.. _kc:

Coeficiente de Evapotranspiración del Cultivo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Los valores del coeficiente de evapotranspiración ( :math:`K_c`) para los cultivos están fácilmente disponibles en los manuales de riego y horticultura. La FAO tiene un recurso en línea para esto: http://www.fao.org/3/X0490E/x0490e0b.htm. Las tablas de la FAO enumeran los coeficientes por etapa de crecimiento del cultivo (:math:`K_c` ini, :math:`K_c` mid, :math:`K_c` end), que deben convertirse a un promedio anual o promedio mensual (dependiendo del modelo) :math:`K_c`. Esto requiere conocimiento sobre la fenología de la vegetación en la región de estudio (fechas promedio de reverdecimiento y extinción) y las etapas de crecimiento de los cultivos (cuándo se plantan y cosechan los cultivos anuales). El :math:`K_c` promedio anual se puede estimar en función de las características de la vegetación y la evapotranspiración de referencia mensual promedio utilizando la siguiente ecuación:

.. math:: K_c = \frac{\sum^{12}_{m=1}K_{cm}\times ET_{o_m}}{\sum^{12}_{m=1}ET_{o_m}}

donde :math:`K_{cm}` es un coeficiente de cosecha promedio del mes :math:`m` (1-12) y :math:`ET_{o_m}` es la evapotranspiración de referencia correspondiente. Estos valores también se pueden calcular utilizando la siguiente hoja de cálculo: https://github.com/natcap/invest.users-guide/raw/main/data-sources_calculator.xlsx. Los valores para :math:`K_c` deben ser decimales entre 0 y 1,5.

Los valores para otros tipos de vegetación se pueden estimar usando las relaciones del índice de área foliar (IAF). IAF caracteriza el área de hoja verde por unidad de área de superficie del suelo y se puede obtener mediante productos de imágenes satelitales derivados del análisis NDVI. Una típica relación IAF - :math:`K_c` es la siguiente(Allen et al., 1998, Chapter 6: http://www.fao.org/3/x0490e/x0490e0b.htm):

.. math:: K_c = \left\{\begin{array}{l}\frac{LAI}{3}\mathrm{\ when\ } LAI \leq 3\\ 1\end{array}\right.

:math:`K_c` las estimaciones para LULC sin vegetación se basan en (Allen et al., 1998). Tenga en cuenta que estos valores son solo aproximados, pero a menos que el LULC represente una porción significativa de la cuenca, el impacto de la aproximación en los resultados del modelo debe ser mínimo.

* Kc para <2 m en aguas abiertas se puede aproximar por Kc=1;
* Kc para >5 m en aguas abiertas está en el rango de 0,7 a 1,1;
* Kc para humedales se puede suponer en el rango de 1 a 1,2;
* Kc para suelo desnudo oscila entre 0,3 y 0,7 según el clima (en particular, la frecuencia de las lluvias). Puede estimarse en Kc=0.5 (ver Allen 1998, Capítulo 11). Se puede encontrar información adicional para determinar Kc para suelo desnudo en (Allen et al., 2005).
* Kc para áreas construidas se puede establecer en f*0.1 +(1-f)*0.6 donde f es la fracción de cubierta impermeable en el área. Aquí, se supone que la evapotranspiración de áreas permeables en entornos construidos es aproximadamente el 60 % de la evapotranspiración de referencia (es decir, el promedio entre césped y suelo desnudo). Además, se supone que la evaporación de la superficie impermeable es del 10 % del PET. Si hay datos locales disponibles, usted puede calcular una estimación promedio anual de Kc, utilizando el método descrito para los factores de cultivo.


Hidrología
----------

.. _watersheds:

Cuencas hidrográficas y alcantarillado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Para delinear cuencas hidrográficas, proporcionamos la herramienta DelineateIT de InVEST, que es relativamente simple pero rápida y tiene la ventaja de crear cuencas hidrográficas que pueden superponerse, como cuencas hidrográficas que desembocan en varias represas en el mismo río. Consulte el capítulo de la guía de uso de DelineateIt para obtener más información sobre esta herramienta. Las herramientas de creación de cuencas hidrográficas también se proporcionan con el programa de SIG, así como algunos modelos de hidrología. Se recomienda que delinee las cuencas hidrográficas utilizando el MDE con el que está modelizando, de modo que el límite de la cuenca hidrográfica se corresponda correctamente con la topografía.

Alternativamente, varios mapas de cuencas hidrográficas están disponibles en línea, p. HydroBASINS: https://hydrosheds.org/. Tenga en cuenta que si los límites de las cuencas hidrográficas no se basan en el mismo DEM que se está modelizando, es probable que los resultados agregados a estas cuencas hidrográficas sean inexactos.

Las ubicaciones exactas de estructuras específicas, como tomas de agua potable o embalses, se deben obtener de la entidad administradora o se pueden obtener en la web:

  * El Inventario Nacional de Presas de EE. UU.: https://nid.sec.usace.army.mil/

  * Base de datos de presas y embalses globales (GRanD): http://globaldamwatch.org/grand/

  * Base de datos de presas del Informe sobre el desarrollo de los recursos hídricos en el mundo II: https://wwdrii.sr.unh.edu/download.html

Algunos de estos conjuntos de datos incluyen el área de captación que drena a cada presa, que debe compararse con el área de la(s) cuenca(s) generada(s) por la herramienta de delineación para evaluar la precisión.

Los datos de la cuenca del alcantarillado pueden estar disponibles en los municipios locales.


.. _tfa:

Umbral de acumulación de flujo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
El umbral de acumulación de flujo (UAF) es un parámetro de algoritmo de delineación de flujo que especifica la cantidad de píxeles pendiente arriba que deben fluir en un píxel antes de que se clasifique como corriente. No hay un valor "correcto" para el UAF. El valor correcto para su aplicación es el valor que hace que el modelo cree una capa de corrientes que se parezca lo más posible a la red de corrientes del mundo real en la cuenca. Compare el resultado ráster de la red de corrientes con un mapa de corrientes correcto conocido y ajuste el UAF concomitantemente: valores más grandes de UAF crearán redes de corrientes con menos afluentes, valores más pequeños de UAF crearán redes de corrientes con más afluentes. Un buen valor para empezar es 1000, pero tenga en cuenta que esto puede variar mucho según la resolución del MDE, el clima local y la topografía. Tenga en cuenta que, por lo general, las corrientes delineadas de un MED no coinciden exactamente con el mundo real, así que intente acercarse lo más posible. Si las corrientes modelizadas son muy diferentes, considere probar un DEM diferente.

Se puede obtener una capa global de corrientes de HydroSHEDS: https://hydrosheds.org/, pero tenga en cuenta que generalmente son los ríos más importantes y es posible que no incluyan los de su área de estudio, especialmente si tiene pequeños afluentes. También puede intentar buscar secuencias en Google Earth si no hay más mapas localizados disponibles.

Consulte también la sección Trabajo con el DEM de esta guía de uso para obtener más información.

.. _soil_groups:

Grupos hidrológicos de suelos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Los grupos hidrológicos de suelos describen el potencial de escorrentía de diferentes tipos de suelo. Hay cuatro grupos: A, B, C, D, donde A tiene el menor potencial de escorrentía y D tiene el mayor. Consulte la publicación del Servicio de Conservación de Recursos Nacionales (NRCS) del Departamento de Agricultura de los Estados Unidos (USDA) para obtener más información: https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17757.wba

Dos capas globales de grupos hidrológicos de suelos están disponibles, 1) de FutureWater (disponible en: https://www.futurewater.eu/2015/07/soil-hydraulic-properties/) y 2) HYSOGs250m de ORNL-DAAC (disponible en https ://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html.).

**The FutureWater raster** proporciona valores de grupo numéricos 1-4 14, 24 y 34. El modelo de rendimiento de agua estacional requiere solo valores de 1/2/3/4, por lo que debe convertir cualquier valor de 14, 24 o 34 en uno de los valores permitidos.

**HYSOGs250m** proporciona valores de letras A-D, A/D, B/D, C/D y D/D. Para usar en este modelo, estos valores de letras deben traducirse a valores numéricos, donde A = 1, B = 2, C = 3 y D = 4. Nuevamente, los píxeles con valores duales como A/D, B/D, etc. deben ser convertido a un valor en el rango de 1-4.

En los Estados Unidos, los datos de suelo gratuitos están disponibles en las bases de datos NRCS gSSURGO, SSURGO y gNATSGO: https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/geo/. También proporcionan herramientas ArcGIS (Soil Data Viewer para SSURGO y Soil Data Development Toolbox para gNATSGO) que ayudan a procesar estas bases de datos en datos espaciales que pueden ser utilizados por el modelo. Soil Data Development Toolbox es la más fácil de usar y muy recomendable si usa ArcGIS y necesita procesar datos de suelos de EE.UU.

Si se desea, los grupos de suelo también se pueden determinar a partir de la conductividad hidráulica y la profundidad del suelo. El conjunto de datos de propiedades hidráulicas del suelo de FutureWater también contiene conductividad hidráulica, al igual que otras bases de datos de suelos. La Tabla 1 a continuación se puede utilizar para convertir la conductividad del suelo en grupos de suelos.

|

**Tabla 1: Criterios para la asignación de grupos hidrológicos de suelos (NRCS-USDA, 2007 Cap. 7)**

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+--------------+--------------+------------------------------------------------------------------------------+
|                                                                                                                                                              | Grupo A     | Grupo B      | Grupo C      | Grupo D                                                                      |
+==============================================================================================================================================================+=============+==============+==============+==============================================================================+
| Conductividad hidráulica saturada de la capa menos transmisiva cuando existe una capa impermeable al agua a una profundidad de entre 50 y 100 centímetros    | >40 μm/s    | [40;10] µm/s | [10;1] µm/s  | <1 μm/s (o profundidad a la capa impermeable <50 cm o nivel freático <60 cm) |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+--------------+--------------+------------------------------------------------------------------------------+
| Conductividad hidráulica saturada de la capa menos transmisiva cuando existe cualquier capa impermeable al agua a una profundidad superior a 100 centímetros | >10 μm/s    | [4;10] µm/s  | [0,4;4] µm/s | <0,4 μm/s                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+--------------+--------------+------------------------------------------------------------------------------+

.. _cn:

Número de curva
^^^^^^^^^^^^^^^
Se recomienda realizar una búsqueda bibliográfica para buscar valores de NC que sean específicos para el área en la que está trabajando. Si no están disponibles, busque valores que se correspondan lo más posible con los mismos tipos de cobertura terrestre/suelo/clima. Si ninguno de estos valores más locales está disponible, se recomiendan fuentes generales.

Los números de curva se pueden obtener del manual del USDA: (NRCS-USDA, 2007 Cap. 9)

Para cuerpos de agua y humedales que están conectados a la corriente, NC se puede configurar en 99 (es decir, suponiendo que esos píxeles transmiten rápidamente un flujo rápido).

Cuando la atención se centra en los posibles efectos de las inundaciones, se puede seleccionar CN para reflejar las condiciones de escorrentía húmeda anterior: los valores de NC se deben convertir a condiciones ARC-III, según el Capítulo 10 de las pautas de NRCA-USDA (2007).

.. _bathymetry:

Batimetría
----------
La batimetría mide la profundidad del agua. El Centro Nacional de Datos Geofísicos (NGDC) de la NOAA proporciona datos batimétricos globales con varias resoluciones espaciales en https://www.ngdc.noaa.gov/mgg/bathymetry/relief.html.

ETOPO1 es un modelo de relieve global de 1 minuto de arco de la superficie de la Tierra que integra topografía terrestre y batimetría oceánica. Se construyó a partir de numerosos conjuntos de datos globales y regionales, y está disponible en las versiones "Ice Surface" (parte superior de las capas de hielo de la Antártida y Groenlandia) y "Bedrock" (base de las capas de hielo). NGDC también proporciona conjuntos de datos batimétricos regionales y globales.

GEBCO produce datos batimétricos cuadriculados globales de dominio público: https://www.gebco.net/data_and_products/gridded_bathymetry_data/


.. _buildings:

Huellas de construcción
-----------------------
Los mapas de infraestructura construida se pueden obtener de la muncipalidad o de datos de fuente abierta como Open Street Map. https://www.openstreetmap.org


Referencias
-----------

Allen, R.G., Pereira, L.S., Raes, D. y Smith, M., 1998. "Crop evapotranspiration. Guidelines for computing crop water requirements." FAO Irrigation and Drainage Paper 56. Food and Agriculture Organization of the United Nations, Rome, Italy. Paper available at http://www.fao.org/3/x0490e/x0490e00.htm. Annex 2 available at: http://www.fao.org/3/X0490E/x0490e0j.htm.

Baer, SG, DJ Kitchen, JM Blair y CW Rice. 2002. Changes in Ecosystem Structure and Function along a Chronosequence of Restored Grasslands. Ecological Applications 12:1688-1701.

Bernoux, M., MDS Carvalho, B. Volkoff y CC Cerri. 2002. Brazil's soil carbon stocks. Soil Science Society of America Journal 66:888-896.

Brown, S. Estimating Biomass and Biomass Change of Tropical Forests: a Primer. FAO Forestry Department; 1997. Report for FAO Forestry Paper 134.

Brown, SL, PE Schroeder y JS Kern. Spatial distribution of biomass in forests of the eastern USA.Forest Ecology and Management 123 (1999) 81-90.

Brown, S. 2002. Measuring carbon in forests: current status and future challenges. Environmental Pollution 116:363-372.

Cairns, MA, S. Brown, EH Helmer y GA Baumgardner. 1997. Root biomass allocation in the world's upland forests. Oecologia 111:1-11.

Cairns, MA, PK Haggerty, R. Alvarez, BHJ De Jong y I. Olmsted. 2000. Tropical Mexico's recent land-use change: A region's contribution to the global carbon cycle. Ecological Applications 10:1426-1441.

Coomes, DA, RB Allen, NA Scott, C. Goulding y P. Beets. 2002. Designing systems to monitor carbon stocks in forests and shrublands. Forest Ecology and Management 164:89-108.

Delaney, M., S. Brown, AE Lugo, A. Torres-Lezama y NB Quintero. 1998. The quantity and turnover of dead wood in permanent forest plots in six life zones of Venezuela. Biotropica 30:2-11.

Detwiler, RP. 1986. Land Use Change and the Global Carbon Cycle: The Role of Tropical Soils. Biogeochemistry 2:67-93.

Droogers, P. y Allen, R.G. 2002. "Estimating reference evapotranspiration under inaccurate data conditions." Irrigation and Drainage Systems, vol. 16, Issue 1, February 2002, pp. 33–45

Edinburgh Centre for Carbon Management. The Establishing Mechanisms for Payments for Carbon Environmental Services in the Eastern Arc Mountains, Tanzania; 2007 May 2007.

Gaston, G., S. Brown, M. Lorenzini y KD Singh. 1998. State and change in carbon pools in the forests of tropical Africa. Global Change Biology 4:97-114.

Glenday, J. 2006. Carbon storage and emissions offset potential in an East African tropical rainforest. Forest Ecology and Management 235:72-83.

Grace, J., J. San Jose, P. Meir, HS Miranda y RA Montes. 2006. Productivity and carbon fluxes of tropical savannas. Journal of Biogeography 33:387-400.

Hamon, W. R. (1961). Estimating potential evapotranspiration. Journal of the Hydraulics Division, 87(3), 107-120.

Houghton, RA. 2005. Tropical deforestation as a source of greenhouse gas emissions. In: Tropical Deforestation and Climate Change, Moutinho and Schwartzman [eds.]. Instituto de Pesquisa Ambiental da Amazonia and Environmental Defense, Belem, Brazil.

Houghton, RA y JL Hackler. 2006. Emissions of carbon from land use change in sub-Saharan Africa. Journal of Geophysical Research 111.

"Hydrologic Soil Groups."National Engineering Handbook, United States Department of Agriculture, National Resources Conservation Service, 2007, www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063.

The Intergovernmental Panel on Climate Change (IPCC). 2006. 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use. Prepared by the National Greenhouse Gas Inventories Programme, Eggleston, HS, L. Buendia, K. Miwa, T. Ngara, and K. Tanabe (eds). Institute for Global Environmental Strategies (IGES), Hayama, Japan. <https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html>.

Makundi, WR. 2001. Carbon mitigation potential and costs in the forest sector in Tanzania. Mitigation and Adaptation Strategies for Global Change 6:335-353.

Malhi, Y., D. Wood, TR Baker et al. 2006. The regional variation of aboveground live biomass in old-growth Amazonian forests. Global Change Biology 12:1107-1138.

Malimbwi, RE, B. Solberg y E. Luoga. 1994. Estimation of biomass and volume in miombo woodland at Kitungalo Forest Reserve Tanzania. Journal of Tropical Forest Science 7:230-242.

Munishi, PKT y TH Shear. 2004. Carbon Storage in Afromontane Rain Forests of the Eastern Arc Mountains of Tanzania: their Net Contribution to Atmospheric Carbon. Journal of Tropical Forest Science 16:78-93.

Nascimento, HEM y WF Laurance. 2002. Total aboveground biomass in central Amazonian rainforests: a landscape-scale study. Forest Ecology and Management 168:311-321.

NRCS-USDA, 2007. National Engineering Handbook. United States Department of Agriculture, https://www.nrcs.usda.gov/wps/portal/nrcs/detailfull/national/water/?cid=stelprdb1043063.

Post, WM, WR Emanuel, PJ Zinke y AG Stangenberger. 1982. Soil carbon pools and world life zones. Nature 298:156-159.

Post, WM y KC Kwon. 2000. Soil carbon sequestration and land-use change: processes and potential. Global Change Biology 6:317-327.

Ruesch A y HK Gibbs. 2008. New IPCC tier-1 global biomass carbon map for the year 2000. Available:https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html.

Silver, WL, R. Ostertag y AE Lugo. 2000. The potential for carbon sequestration through reforestation of abandoned tropical agricultural and pasture lands. Restoration Ecology 8:394-407.

Tiessen, H. y C. Feller, EVSB Sampaio, and P. Garin. 1998. Carbon Sequestration and Turnover in Semiarid Savannas and Dry Forest. Climatic Change 40:105-117.

Tilman, D., J. Hill y C. Lehman. 2006. Carbon-Negative Biofuels from Low-Input High-Diversity Grassland Biomass. Science 314:1598-1600.

Vagen, TG, R Lal y BR Singh. 2005. Soil carbon sequestration in sub-Saharan Africa: A review. Land Degradation & Development 16:53-71.

Zhang, Q y CO Justice. 2001. Carbon Emissions and Sequestration Potential of Central African Ecosystems. AMBIO 30:351-355.