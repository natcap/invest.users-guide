.. _scenic-quality:

********************************************
Calidad escénica
********************************************

Resumen
=======

Las vistas naturales y escénicas de los paisajes marinos y costeros pueden contribuir al bienestar de las comunidades locales de varias maneras. Las amenidades escénicas juegan un papel importante en el aumento de las economías locales al atraer visitantes que apoyan las empresas locales. El valor de la propiedad local depende parcialmente de los atributos de su ubicación y las vistas panorámicas a menudo aumentan el valor de la propiedad local (Sanders y Polasky 2009, Bourassa et al. 2004, Benson et al. 2004). Las comunidades locales y sus residentes a menudo se apegan mucho a los paisajes y muestran una ferviente oposición a los nuevos desarrollos que tienen el potencial de amenazar la integridad de las cuencas visuales existentes y disminuir los beneficios derivados de ellas (Ladenburg y Dubgaard 2009, Haggett 2011). El modelo InVEST de Calidad escénica permite determinar las ubicaciones desde las que se pueden ver nuevas características cercanas a la costa o en alta mar. Genera mapas de cuencas visuales que se pueden usar para identificar la huella visual del nuevo desarrollo en alta mar y calcula el valor de la visibilidad afectada. Los inputs al modelo de cuenca visual incluyen: topografía y batimetría, ubicaciones de instalaciones en alta mar de interés y ubicaciones de espectadores (por ejemplo, centros de población o áreas de interés como parques o senderos). El modelo no cuantifica los impactos económicos de alterar la cuenca visual, pero se puede adaptar para calcular las métricas de la cuenca visual para su uso en un estudio de valoración más detallado. Una limitación clave del modelo es que actualmente no tiene en cuenta las formas en que la vegetación o la infraestructura terrestre pueden limitar las áreas terrestres que se ven afectadas visualmente por el desarrollo en alta mar.

Introducción
============

Los ecosistemas costeros están cada vez más dominados por las actividades humanas. Este aumento de las actividades humanas puede comprometer las cualidades escénicas únicas asociadas a las zonas costeras y marinas. El litoral y el "paisaje marino" son un importante activo económico que atrae a visitantes para el turismo y el ocio y contribuye a la calidad de vida general de las personas que viven cerca de la costa. Los proyectos de desarrollo cercanos y en alta mar suelen suscitar una gran preocupación en las comunidades locales que valoran el paisaje marino natural por su belleza inherente. Los impactos visuales son efectos externos que, a menos que se midan y contabilicen, no entran en el cálculo de los costos y beneficios del nuevo desarrollo costero. Las aplicaciones que utilizan el análisis de las cuencas visuales van desde la ubicación de las instalaciones de acuicultura para minimizar la competencia espacial con las actividades turísticas (Pérez 2003) hasta la evaluación de la visibilidad del paisaje marino y de la línea de costa de los proyectos eólicos en alta mar (Environmental Design and Research 2006). Dado que la belleza escénica es un atributo que generalmente se considera importante para las personas que viven cerca de la costa y para quienes visitan las zonas costeras para disfrutar del océano y del medio ambiente marino, los planificadores costeros pueden incorporar medidas de atractivo y/o desagrado visual en las deliberaciones políticas y ejercicios de planificación más amplios. Dado que la mayoría de las aplicaciones del análisis de las cuencas visuales implican el examen de los impactos negativos de las nuevas instalaciones, el lenguaje dentro del modelo de calidad escénica InVEST asume que los objetos vistos tienen un impacto negativo en las vistas. Sin embargo, la interpretación positiva de la visión de estos objetos puede incluirse en la interpretación de los resultados del modelo.

El modelo de calidad escénica InVEST le ofrece una forma sencilla de proporcionar información sobre las posibles compensaciones entre las propuestas de desarrollo en la costa y en el mar y los impactos visuales de esos proyectos. Los mapas de cuancas visuales producidos por el modelo pueden utilizarse para identificar las zonas costeras que tienen más probabilidades de verse directamente afectadas por las ampliaciones del paisaje marino. Pueden servir de valiosa aportación a análisis más amplios que tengan en cuenta una serie de servicios prestados por el medio marino.

Este modelo puede utilizarse para calcular los costos asociados a los impactos visuales en alta mar; es probable que estos  disminuyan a medida que la ubicación de las instalaciones se aleja de la costa, mientras que los costos de instalación y funcionamiento de las instalaciones en alta mar suelen aumentar con la distancia a la costa. Los pocos estudios de valoración que exploran la magnitud económica de las molestias visuales resultantes de los proyectos de desarrollo en alta mar muestran un panorama complejo. Un estudio reciente ha revelado que los individuos que viven en la costa tienen costos externos que oscilan entre los 27 y los 80 dólares como consecuencia de las molestias visuales de un proyecto eólico marino (Krueger et al. 2010). En cambio, Firestone et al. (2009) descubrieron que la aceptación pública de los proyectos de energía renovable en alta mar está creciendo y puede ser menos conflictiva de lo que se preveía.

El modelo
=========

El modelo de calidad escénica proporciona información sobre la visibilidad de los objetos en alta mar desde el paisaje circundante o el paisaje marino. Los proyectos de desarrollo en alta mar y cerca de la costa, como las instalaciones de energía renovable de las olas o las instalaciones de acuicultura, tienen el potencial de afectar a los servicios visuales que son una característica importante de muchas zonas costeras. Los resultados del análisis de las cuancas visuales serán útiles para los responsables de la toma de decisiones que deseen identificar las zonas en las que los impactos visuales pueden ser un factor importante a tener en cuenta en la planificación.

Los inputs del modelo se dividen en dos grupos: **General** tiene todos los inputs necesarios para ejecutar el cálculo de las c uancas visuales, como la ubicación de un MDE y un vector de puntos que identifica las ubicaciones de los sitios que contribuyen a los impactos visuales. La función de **Valoración** permite que usted seleccione la forma funcional de la función de valoración y sus parámetros. A continuación, se calcula el análisis  de las cuencas visuales en un área de interés (ADI) definida por usted.

El modelo creará tres resultados que pueden utilizarse para evaluar el impacto visible de cualquier tipo de instalación añadida al entorno marino:

    * *vshed.tif* es un ráster que contiene la suma de cuántos puntos de vista son visibles desde cada píxel. Si se proporciona una columna *PONDERACION* en el vector estructuras/puntos de vista, la suma de la visibilidad se pondera. Si la valoración y los pesos se establecen todos en ``1``, este ráster se reduce a un simple recuento del número de sitios que son visibles desde un píxel.

    * *vshed_value.tif* es la suma de todos los rásteres de valoración individuales calculados para cada sitio. Si se proporciona una columna *PONDERACION* en el vector de sitios, los valores se ponderarán en consecuencia.

    * *vshed_qual.tif* es un ráster que representa la calidad visual de un determinado píxel. Las celdas de *vshed_Value.tif* se clasifican según los siguientes percentiles:

        1. No afectado
        2. Impacto visual bajo / Calidad visual alta (< percentil 25)
        3. Impacto visual moderado / Calidad visual media (percentil 25-50)
        4. Impacto visual alto / Calidad visual baja (percentil 50-75)
        5. Impacto visual muy alto / Calidad visual mala (> percentil 75)

Se generan archivos adicionales para cada característica *X* en cada paso del cálculo:

    * *visibility_X.tif* indica qué píxeles son visibles desde la característca *X*
    * *auxiliary_X.tif* es un ráster intermedio escrito como parte del algoritmo de la cuenca vuisual. Los valores de píxeles indican la altura mínima que se debe alcanzar para que los píxeles sean vivibles. 
    * *value_X.tif* es el valor de la cuenca visual, ponderado (si se ha proporcionado una columna *PONDERACION*), y en términos de la distancia (en metros) entre los píxeles y la característica *X*.


Cómo funciona
-------------
El modelo de calidad escénica InVEST calcula el impacto visual de los elementos del paisaje en varios pasos:

1. Para cada lugar de la estructura:

   1. Calcula la visibilidad para cada característica de punto *X* (*intermediate\visibility_X.tix*) basado en el algoritmo d cuencas visuales (viewshed) del plano de referencia de Wang et al.
   2. A partir de la visibilidad, determina el valor de la amenidad/disamenidad de la visibilidad ponderando la visibilidad y aplicando la función de valoración definida en la interfaz de uso (*intermediate\\value_X.tif*).

2. Suma los rásteres de valoración para crear un agregado ponderado (*output\\vshed_value.tif*)

3. 3. Divide el ráster de valoración ponderado y agregado en cuartiles para crear un ráster que represente la calidad visual (*producto_vshed_qual.tif*)

4. Pondera y sumarlos rásters de visibilidad de todos los puntos de las estructuras para crear una suma ponderada del número de puntos visibles (*output\vshed.tif*)

La valoración puede adoptar una de estas formas

Lineal:

.. math:: f(x) = a + b \cdot x
    :name: forma lineal

Logarítmica:

.. math:: f(x) = a + b \cdot ln(x)
    :name: forma_logarítmica

Exponencial:

.. math:: f(x) = a \cdot e^{(-b \cdot x)}
    :name: forma exponencial 

Donde *x* es la distancia en metros desde el centro de la celda a una característica puntual, y *a* y *b* son coeficientes definidos por usted. Con los valores de los parámetros por defecto (*a=1*, *b=0*), el modelo calcula una cuanca visual agregada. La función de valoración se calcula hasta un radio de valoración máximo que por defecto es de 8000 metros.


Limitaciones y simplificaciones
===============================

El MDE global incluido en el modelo de calidad escénica no tiene en cuenta los árboles, edificios u otras estructuras que pueden oscurecer la vista. Si se dispone de una capa ráster que represente la ubicación de árboles, edificios u otros obstáculos (y sus alturas), esta información puede incorporarse al MDE para crear una superficie más realista que oscurezca o permita las vistas. El modelo tiene en cuenta la curvatura de la tierra a la hora de limitar la visibilidad, pero no limita la distancia a la que objetos de distinto tamaño y calidad pueden ser visibles para el ojo humano en la configuración por defecto. Siempre que exista un vector rectilíneo que pueda calcularse desde una determinada celda de la cuadrícula del MDE hasta cualquier punto de la costa, esa celda de la cuadrícula se considerará visible. Esto debe tenerse en cuenta al interpretar los mapas de impacto de las vistas de las instalaciones situadas lejos de la costa cuando se utilizan los ajustes por defecto. Sin embargo, usted puede proporcionar un radio exterior que limite la distancia de búsqueda al identificar las áreas visibles desde cada lugar de desarrollo en alta mar.


.. _ae-data-needs:

Necesidades de datos
====================

General
-------

- :investspec:`scenic_quality.scenic_quality workspace_dir`

- :investspec:`scenic_quality.scenic_quality results_suffix`

- :investspec:`scenic_quality.scenic_quality aoi_path`

- :investspec:`scenic_quality.scenic_quality structure_path` Pueden representar estructuras como corrales de acuicultura o instalaciones de energía de las olas. Si desea incluir elementos con una huella mayor, como los desmontes, convierta los polígonos en una cuadrícula de puntos uniformemente espaciados.

  El modelo calculará una cuenca visual para cada característica por separado y las agregará en una cuanca visual combinada. Usted puede especificar hasta tres campos (todos los campos son opcionales) para asignar una distancia de visión máxima, un coeficiente de importancia de la cuenca visual o una altura de punto de vista a cada característica.

  Campos:

  - :investspec:`scenic_quality.scenic_quality structure_path.fields.radius`
  - :investspec:`scenic_quality.scenic_quality structure_path.fields.weight`
  - :investspec:`scenic_quality.scenic_quality structure_path.fields.height`

- :investspec:`scenic_quality.scenic_quality dem_path` Se utiliza para determinar las zonas del paisaje terrestre del ADI en las que son visibles las características que afectan a la calidad del paisaje. El modelo se ejecuta con la resolución de este ráster.

- :investspec:`scenic_quality.scenic_quality refraction` Los cambios en la densidad del aire curvan la luz hacia abajo, lo que hace que se vean más lejos y que la Tierra parezca menos curvada. Aunque la magnitud de este efecto varía con las condiciones atmosféricas, una regla general es que la refracción de la luz visible reduce la curvatura aparente de la Tierra en una séptima parte. El valor por defecto es 0,13.


Valoración
----------

- :investspec:`scenic_quality.scenic_quality do_valuation`

- :investspec:`scenic_quality.scenic_quality valuation_function`

- :investspec:`scenic_quality.scenic_quality a_coef`

- :investspec:`scenic_quality.scenic_quality b_coef`

- :investspec:`scenic_quality.scenic_quality max_valuation_radius` La función de valoración :math:`f` no puede ser negativa en el radio :math:`r` (:math:`f(r)>=0`).


Resultados finales
------------------

Carpeta de resultados
^^^^^^^^^^^^^^^^^^^^^
* **Output\\vshed_qual.tif**

    * Esta capa ráster contiene un campo que clasifica por cuartiles la calidad visual dentro del ADI. Las clases de calidad visual incluyen: no afectada (sin impacto visual), alta (impacto visual bajo), media (impacto visual moderado), baja (impacto visual alto) y muy baja (impacto visual muy alto).

* **Output\\vshed.tif**

    * Esta capa ráster contiene la suma ponderada de todos los rásters de visibilidad. Si no se proporciona ninguna columna de peso en el vector de puntos de estructuras, este ráster representará un recuento del número de puntos de estructuras que son visibles desde cada píxel.

    * Para comparar las ejecuciones de los escenarios, utilice esta capa en lugar de vshed_qual. A través del cálculo de la diferencia entre los resultados de "vshed" de múltiples ejecuciones, se pueden evaluar los cambios en la calidad visual a través de los escenarios.

* **Output\\vshed_value.tif**

    * Esta capa ráster contiene la suma ponderada de los rásters de valoración creados para cada punto.

Carpeta intermedia
^^^^^^^^^^^^^^^^^^

* **intermediate\\dem_clipped.tif**

    * Esta capa ráster es una versión del MDE que ha sido recortada y enmascarada en el ADI y teselada. Este es el archivo DEM que se utiliza para el análisis de las cuencas  visuales.

* **intermediate\\aoi_reprojected.shp**

    * Este vector es el ADI, reproyectada a la referencia espacial y proyección del MDE.

* **intermediate\\structures_clipped.shp**

    * Este vector contiene todos los puntos de vista que se cruzan con el ADI.

* **intermediate\\structures_reprojected.shp**

    * Es el vector de estructuras, reproyectado a la referencia espacial y proyección del MDE.

* **intermediate\\visibility_*.tif**

    * El ráster de visibilidad para un punto de vista de estructuras determinado. Este ráster tiene valores de píxel de 0 (no visible), 1 (visible), o nodata (donde el DEM es nodata).

* **intermediate\\auxiliary_*.tif**

    * Un ráster intermedio creado mientras se calcula la cuenca visual para el punto de vista de las estructuras dadas. Los valores de este ráster representan la altura mínima que debe tener el MDE para que el terreno sea visible en ese píxel.

* **intermediate\\value_*.tif**

    * El valor calculado de la amenidad/desamenidad de la cuanca visual dadas las distancias (en metros) de los píxeles desde el punto de vista de las estructuras, el peso del punto de vista, la función de valoración y los coeficientes *a* y *b*. El valor de la cuanca vuisual solo se evalúa para los píxeles visibles. Si un píxel del MDE subyacente no está definido (tiene un valor nodata), también lo está el ráster de valoración.

Referencias
===========

Benson E., Hansen, J., Schwartz, A. y Smersh, G., 1998. Pricing residential amenities: the value of a view. Journal of Real Estate Research, 16: 55-73.

Bourassa, S., Hoesli, M. y Sun, J. 2004. What’s in a view? Environment and Planning A. 36(8): 1427-1450.

Center for International Earth Science Information Network (CIESIN), Columbia University; International Food Policy Research Institute (IFPRI); The World Bank y Centro Internacional de Agricultura Tropical (CIAT). 2004. Global Rural-Urban Mapping Project (GRUMP), Alpha Version: Population Grids. Palisades, NY: Socioeconomic Data and Applications Center (SEDAC), Columbia University. Disponible de forma permanente en https://sedac.ciesin.columbia.edu/data/collection/gpw-v4. (descargado el 1/6/2011).

Environmental Design and Research, P.C. 2006. Seascape and shoreline visibility assessment. Cape Wind Energy Project. Cape Cod, Martha’s Vineyard, and Nantucket, Massachusetts. Prepared for Cape Wind Associates, L.L.C. Boston, Mass. Syracuse, N.Y. July 2006.

Firestone, J., Kempton, W. y Krueger, A., 2009. Public acceptance of offshore wind power projects in the USA. Wind Energy, 12(2):183-202. 

Haggett, C. 2011. Understanding public responses to offshore wind power. Energy Policy. 39: 503-510.

Krueger, A., Parson, G. y Firestone, J., 2010. Valuing the visual disamenity of offshore wind power at varying distances from the shore: An application of on the Delaware shoreline. Working paper. Available at: https://works.bepress.com/george_parsons/.

Ladenburg, J. y Dubgaard, A., 2009. Preferences of coastal zone user groups regarding the siting of offshore wind farms. Ocean & Coastal Management, 52(5): 233-242. 

Perez, O.M., Telfer, T.C. y Ross, L.G., 2005. Geographical information systems-based models for offshore floating marine fish cage aquaculture site selection in Tenerife, Canary Islands. Aquaculture Research, 36(10):946-961. 

Sander, H.A. y Polasky, S., 2009. The value of views and open space: Estimates from a hedonic pricing model for Ramsey County, Minnesota, USA. Land Use Policy, 26(3):837-845. 

Wang, J., Robertson, G.J., White, K., 2000. Generating viewsheds without using sightlines. Photogrammetric Engineering & Remote Sensing, 66(1):87-90
