.. _urban_nature_access:

*****************************
Acceso a la naturaleza urbana
*****************************

Resumen
=======

La naturaleza en las zonas urbanas ofrece importantes oportunidades de ocio. El modelo de acceso a la naturaleza urbana proporciona una medida tanto de la oferta de naturaleza urbana como de la demanda de naturaleza por parte de la población urbana, calculando en última instancia el equilibrio entre oferta y demanda. Tanto la naturaleza urbana como la población pueden dividirse opcionalmente en diferentes grupos. La oferta viene determinada por el tipo, el tamaño, la proximidad y la calidad de la naturaleza urbana accesible per cápita con fines recreativos. La demanda se determina como espacio natural per cápita, tal y como suelen exigir las políticas o normas. El equilibrio cuantifica en qué medida la oferta satisface la demanda, a nivel individual, administrativo y de ciudad.

Introducción
============

La naturaleza en las zonas urbanas ofrece importantes oportunidades de recreación, junto con beneficios sociales, psicológicos y de salud física (Bratman et al. 2019, Keeler et al. 2019, Remme et al. 2021). De acuerdo con Liu et al. (2022), la evaluación de la recreación basada en la naturaleza requiere una comprensión de i) la "oferta" de naturaleza urbana, que a su vez depende de la disponibilidad y la calidad, y ii) la "demanda" de naturaleza urbana, que depende de las preferencias de las personas o de los requisitos de las políticas.

Este modelo InVEST sigue la estructura descrita en Liu et al. (2022), evaluando la oferta y la demanda de naturaleza urbana y el equilibrio local entre oferta y demanda, que identifica las zonas con excedente o déficit (equilibrio positivo o negativo, respectivamente) de naturaleza urbana, con respecto a una norma (Liu et al., 2022). De este modo, el modelo se centra en el acceso a la naturaleza en las zonas urbanas. Dado que el modelo es capaz de modelar la oferta, la demanda y el equilibrio de muchos tipos de naturaleza urbana, como parques, espacios verdes, humedales y costas, en este documento nos referiremos al modelo como modelo de acceso a la naturaleza urbana. Corresponde al usuario elegir qué componentes de la naturaleza urbana incluir en su análisis.

El modelo por defecto evalúa la oferta, la demanda y el equilibrio global de la naturaleza urbana para el total de la población urbana. Además, pueden utilizarse tres extensiones opcionales del modelo básico para obtener resultados más detallados:

* La oferta, la demanda y el equilibrio de la naturaleza urbana pueden resumirse en diferentes grupos de población (por ejemplo, según los distintos grupos de edad, niveles de renta, raza o etnia, etc.), lo que puede ser  importante para las consideraciones de equidad. Véase :ref:`una-summarize-by-population-groups`

* Para una comprensión más minuciosa de la oferta de naturaleza urbana, el usuario puede, opcionalmente, proporcionar información más detallada sobre la distancia que la gente suele recorrer para hacer uso de los diferentes tipos de naturaleza urbana. Por ejemplo, es posible que la gente se desplace más lejos para visitar grandes parques en comparación con parques locales pequeños. Véase :ref:`una-radii-per-urban-nature-class`

* Para una comprensión más detallada de la oferta de naturaleza urbana a los distintos grupos de población, el usuario puede, opcionalmente, proporcionar información sobre la distancia que probablemente deban recorrer los distintos grupos para llegar a la naturaleza urbana. Por ejemplo, las personas que tienen coche pueden desplazarse más lejos que las personas que utilizan el transporte público. Véase :ref:`una-radii-per-population-group`.

También se ofrecen tres opciones para desarrollar un modelo más detallado:

El modelo
=========

El modelo calcula el acceso a la naturaleza urbana basándose en la ubicación y la cantidad de naturaleza urbana, la ubicación y el número de personas, y la necesidad o demanda per cápita de naturaleza urbana. La superficie de naturaleza urbana en el píxel :math:`j` se representa como :math:`S_j`. Los valores de :math:`S_j` se expresan en metros cuadrados, donde la proporción de la superficie de un píxel que está cubierta por naturaleza urbana se define en la Tabla de Atributos de uso/cubierta del suelo (LULC). La población en el píxel :math:`i` está representada por :math:`P_i`. Los requisitos per cápita para la naturaleza urbana se especifican como :math:`g_{cap}`, y a menudo se basan en objetivos de políticas. Juntos, estos componentes se utilizan para calcular las siguientes tres métricas principales, descritas con más detalle en :ref:`una-running-the-default-model`:

- Demanda de naturaleza urbana:** la cantidad de naturaleza urbana requerida/demandada por la población en un píxel

- **Equilibrio de la naturaleza urbana:** la diferencia entre la naturaleza urbana suministrada a un píxel y lo que demanda la población de ese píxel

Función de decaimiento
----------------------

Las personas utilizan los espacios naturales con más frecuencia si están más cerca de sus hogares (Andkjaer y Arvidsen, 2015). Esta frecuencia disminuye a medida que aumenta la distancia. Es lo que se denomina "decaimiento de la distancia". El modelo describe este decaimiento de la distancia entre la naturaleza urbana y la población mediante la función de decaimiento :math:`f\left( d_{ij} \right)` donde :math:`d_{ij}` es la distancia entre la naturaleza y un píxel de población, y :math:`d_{0}` es una distancia de búsqueda definida por el usuario dentro de la cual buscar píxeles de naturaleza. La distancia de búsqueda es siempre la distancia euclidiana (distancia en línea recta entre los puntos centrales de los píxeles A y B) y asume píxeles cuadrados.

 .. figure:: ../en/urban_nature_access/decay_function_intro.png
          :align: center
          :figwidth: 400px

Este modelo ofrece varias funciones de decaimiento de distancia entre las que el usuario puede elegir, que se definen e ilustran con más detalle a continuación. La opción **dicotomía** trata todos los píxeles dentro de una distancia de búsqueda establecida desde un píxel como igualmente accesibles. Esta opción se recomienda cuando una política de naturaleza o espacios verdes urbanos tiene como objetivo una cierta cantidad de naturaleza a una distancia determinada de las residencias de las personas. Por ejemplo, los Países Bajos establecen un objetivo de al menos :math:`60m^2` de naturaleza urbana por persona en un radio de 500 m de los hogares (Roo et al. 2011).

Para los estudios que tienen en cuenta el decaimiento del servicio de naturaleza urbana, que representan de forma más realista la probabilidad de visitar la naturaleza urbana, la función de decaimiento debe ajustarse a los datos disponibles sobre visitas. Por lo tanto, se dispone de tres funciones adicionales de decaimiento de la distancia: **exponencial, gaussiana** y **densidad**. Todas asignan más peso a la naturaleza urbana situada más cerca de las personas, lo que refleja la mayor probabilidad de que las personas visiten la naturaleza más cercana a ellas.

Dicotomía
---------

El núcleo dicotómico considera que todos los píxeles dentro de la distancia de búsqueda :math:`d_0` son igualmente accesibles al espacio verde.  Más formalmente: :math:`d_{0}` de un píxel con naturaleza para ser igualmente accesible.

.. math::
        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                1 & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
                0 & \text{if} d_{ij} > d_0 \\
        \end{array}\right\} \\
        \end{align*}


.. figure:: ../en/urban_nature_access/kernel-dichotomy.png
        :align: center
        :figwidth: 500px


Exponencial
-----------

Una función de decaimiento exponencial ponderada por la distancia, en la que es más probable que las personas visiten la naturaleza más cercana a ellas, con una probabilidad que cae exponencialmente hasta el radio máximo :math:`d_{0}`.

Una función de decaimiento exponencial ponderada por la distancia, en la que es más probable que las personas visiten la naturaleza más cercana a ellas, con una probabilidad que cae exponencialmente hasta el radio máximo :math:`d_{0}`.

Gaussiana
---------

Una función de decaimiento ponderada por la distancia, en la que es más probable que las personas visiten la naturaleza más cercana a ellas, con una probabilidad decreciente según una distribución normal ("gaussiana") con una sigma de 3, hasta el radio máximo
:math:`d_{0}`.

.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                \frac{e^{-\frac{1}{2}\left ( \frac{d_{ij}}{d_0} \right )^2}-e^{-\frac{1}{2}}}{1-e^{-\frac{1}{2}}} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}

.. figure:: ../en/urban_nature_access/kernel-gaussian.png
        :align: center
        :figwidth: 500px

Densidad
--------

Una función de decaimiento ponderada por la distancia, en la que es más probable que la gente visite la naturaleza más cercana a ellos, con una probabilidad que disminuye más rápidamente a medida que las distancias se acercan al radio de búsqueda :math:`d_{0}`.


.. math::

        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                \frac{3}{4}\left(1-\left(\frac{d_{ij}}{d_{0}}\right)^{2}\right) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}

.. figure:: ../en/urban_nature_access/kernel-density.png
        :align: center
        :figwidth: 500px

Ejecución del modelo central
----------------------------

.. _una-running-the-default-model:

Ejecución del modelo por defecto
--------------------------------

El modelo por defecto asume un radio uniforme de desplazamiento ("radio de búsqueda") que define el usuario, es decir, solo la naturaleza situada a una distancia de X metros del domicilio de alguien contribuye al beneficio recreativo de una persona.

.. math::  

Cálculo de la oferta de naturaleza urbana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        demand_i = P_i \cdot g_{cap} 

Donde :math:`P_i` es la población en el píxel :math:`i` y :math:`g_{cap}` es la necesidad de espacio verde per cápita definida por el usuario.

Cálculo de la oferta de espacios verdes
***************************************

El cálculo del suministro de naturaleza urbana a cada píxel de población utiliza el método de área de captación flotante en dos pasos (2SFCA) (Mao y Nekorchuk, 2013; Xing et al., 2018). Dado un píxel de naturaleza urbana :math:`j`, se buscan todos los píxeles de población con el radio de búsqueda :math:`d_{0}`. La relación naturaleza urbana/población :math:`R_{j}` para este píxel se calcula utilizando el área del píxel de naturaleza :math:`S_{j}` dividida por la población total dentro del radio de búsqueda, ponderada según la ponderación basada en la distancia del núcleo de búsqueda seleccionado. A continuación, centrados en cada píxel del ráster de población, se buscan todos los píxeles naturales dentro de su cuenca ponderada por distancia. Todos los :math:`R_{j}` de estos píxeles naturales se suman para calcular la oferta de naturaleza urbana per cápita :math:`A_{i}` a cada píxel de población. Adoptamos este enfoque para la oferta, en lugar de simplemente la cantidad de naturaleza en un radio de un hogar, porque al utilizar un enfoque basado en la gravedad se tiene en cuenta la disponibilidad ponderada de la naturaleza. En otras palabras, 2SFCA tiene en cuenta el contexto de que mucha gente utiliza los espacios verdes, algo habitual en una zona urbana.

Esto puede entenderse gráficamente como:

.. figure:: ../en/urban_nature_access/2SFCA_step1_v2.png
        :align: center
        :figwidth: 400px

        Paso 1: Localización de poblaciones en el radio de búsqueda de naturaleza urbana.

.. figure:: ../en/urban_nature_access/2SFCA_step2_v2.png
	:align: center
        :figwidth: 400px

        Paso 2: Localización de naturaleza urbana en el radio de búsqueda de poblaciones.

Más formalmente, la relación naturaleza urbana/población :math:`R_{j}` se define como:


.. math::
        \begin{align*}
        R_j &= \left\{\begin{array}{lr}
                \frac{S_j}{\sum_{k \in \left\{d_{jk} \leq d_0  \right\}} P_k \cdot f(d_{jk})} & \text{if} P_k \cdot f(d_{jk}) >= 1 \\
                S_j & \text{otherwise} \\
        \end{array}\right\} \\
        \end{align*}

Donde:

- :math:`R_{j}` es la relación naturaleza urbana/población del píxel de naturaleza :math:`j`. 
- :math:`S_{j}` es el área de naturaleza en el píxel :math:`j`
- :math:`d_{0}` es el radio de búsqueda
- :math:`k` es el píxel de población dentro del radio de búsqueda del píxel de naturaleza :math:`j`
- :math:`d_{jk}` es la distancia entre el píxel de naturaleza :math:`j` y el píxel de población :math:`k`.
- :math:`P_{k}` es la población del píxel :math:`k`.
- :math:`f(d)` es la función de decaimiento seleccionada.

A continuación, la relación naturaleza urbana/población se pondera mediante la función de descomposición seleccionada y se suma dentro del radio de búsqueda para obtener la oferta de espacios verdes, :math:`A_{i}`:

.. math::

        A_i = \sum_{j \in \left\{d_{ij} \leq d_0  \right\}} R_j \cdot f(d_{ij})

Donde:

-  :math:`i` es cualquier píxel en el ráster de población
-  :math:`A_{i}` es la naturaleza urbana per capita entregada al píxel :math:`i` (metros cuadrados por persona)
-  :math:`d_{ij}` es la distancia entre el píxel :math:`i` u el píxel natural :math:`j`.
-  :math:`d_{0}` es el radio de búsqueda

Cálculo de la demanda de naturaleza urbana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Derivada de la capa de población y de la demanda de naturaleza urbana definida por el usuario, mide la cantidad de naturaleza urbana accesible necesaria para abastecer adecuadamente a todas las personas de cada píxel.

.. math::

        demand_{i} = P_{i} \cdot g_{cap}

Donde:

-  :math:`i` es un píxel
-  :math:`demand_{i}` es la superficie de naturaleza urbana (en metros cuadrados) que necesita la población residente en el píxel :math:`i` para satisfacer plenamente sus necesidades de naturaleza urbana.
-  :math:`P_{i}` es la población (personas por píxel) en el píxel :math:`i`
-  :math:`g_{cap}` es la necesidad de naturaleza urbana per cápita definida por el usuario (metros cuadrados por persona)

Cálculo del equilibrio de la naturaleza urbana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Los documentos de planificación local o los objetivos de planificación urbana suelen establecer que cada residente de una región debe tener asignada una determinada cantidad de naturaleza, :math:`g_{cap}`. El presupuesto de oferta/demanda de naturaleza urbana per cápita :math:`SUP\_ DEM_{i,cap}` en el píxel :math:`i`, se define evaluando el equilibrio entre la naturaleza urbana suministrada y el objetivo de planificación para la naturaleza (a menudo espacio verde) per cápita por píxel:

.. math::

        SUP\_DEM_{i,cap} = A_i - g_{cap}

Para determinar el balance de todas las personas en cada píxel, :math:`SUP\_ DEM_{i,cap}` se multiplica por la población :math:`P_{i}` en el píxel :math:`i`:

.. math::

        SUP\_DEM_{i} = SUP\_DEM_{i,cap} \cdot P_i

Cálculo de la naturaleza urbana accesible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A menudo es útil hallar el área total dentro del radio de búsqueda dado, dado por:

.. math:: accessible_{i} = \sum_{j \in \left{d_{ij} \leq d_{0} \{S_j \cdot f(d_{ij})} 

Donde :math:`accessible_{i}` es la superficie total de naturaleza urbana accesible al píxel :math:`i` dentro del radio de búsqueda :math:`d_0`, ponderada por la función de decaimiento.

Resumen de los resultados para las unidades administrativas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El usuario debe proporcionar un vector con los límites de las unidades administrativas que pueden representar cualquier nivel de distrito que le interese. Estos límites son necesarios para obtener mediciones a nivel administrativo.

El balance oferta/demanda a nivel administrativo es la suma del balance de cada píxel :math:`i` dentro del límite administrativo :math:`adm`:

.. math::

        SUP\_DEM_{adm} = \sum_{i \in \left\{adm \right\}} SUP\_DEM_i

:math:`SUP\_ DEM_{adm}` indica cuánta naturaleza urbana, en metros cuadrados, falta o sobra en una unidad administrativa.

El balance medio per cápita de la oferta y la demanda de naturaleza urbana también se calcula a nivel administrativo:

.. math::

        SUP\_DEM_{adm,cap} = \frac{SUP\_DEM_{adm}}{P_{adm}}

Donde :math:`P_{adm}` es la población total dentro del límite administrativo.

Cuando :math:`SUP\_ DEM_i,cap} < 0` en cualquier píxel :math:`i`, indica que la población de este píxel tiene un déficit de naturaleza urbana. La suma de estas poblaciones en todos los píxeles dentro de una unidad administrativa proporciona el número de personas en una unidad administrativa con un déficit de naturaleza urbana, :math:`Pund_{adm}`, en relación con la naturaleza urbana recomendada :math:`g_{cap}`:

.. math::
        Pund_{adm} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i} & \text{if} SUP\_DEM_{i,cap} < 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}

De manera similar, se aplica el mismo razonamiento para hallar el número de personas con un excedente de naturaleza urbana en una unidad administrativa, :math:`Povr_{adm}`, en relación con la naturaleza urbana recomendada :math:`g_{cap}`:

.. math::
        Povr_{adm} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i} & \text{if} SUP\_DEM_{i,cap} > 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}


.. _una-radii-per-urban-nature-class:

Ejecución del modelo con radios definidos por clase de naturaleza urbana
------------------------------------------------------------------------

La naturaleza urbana es de distintos tipos. Los parques pequeños de la localidad proporcionan una cómoda experiencia recreativa en las cercanías, mientras que los parques municipales atraen a personas de lugares más lejanos. Si el usuario dispone de datos para dividir los tipos de naturaleza urbana y la distancia de desplazamiento ajustada para cada tipo de naturaleza urbana, la accesibilidad de cada tipo de naturaleza urbana al píxel :math:`i` puede calcularse utilizando el radio específico de la clase. Estos tipos de naturaleza urbana divididos y sus radios de búsqueda asociados se proporcionan al modelo mediante el input del usuario en la tabla de atributos LULC. Cada tipo de clasificación de ocupación del suelo marcado como naturaleza urbana se calculará por separado para ofrecer resultados más detallados sobre la naturaleza urbana accesible de cada tipo. Corresponde al usuario decidir cómo dividir la naturaleza urbana.

.. figure:: ../en/urban_nature_access/radii_per_nature_class.png
        :align: center
        :figwidth: 700px

La accesibilidad del tipo de naturaleza urbana :math:`r`, :math:`A_{i,r}` al píxel :math:`i` se calcula sumando la distancia ponderada
:math:`R_{j,r}` dentro del radio de búsqueda:

.. math::
        A_{i,r} = \sum_{j \in d_{ij} \leq d_{0,r}}{R_{j,r} \cdot f(d_{ij})}

La naturaleza urbana total suministrada al píxel :math:`i`, :math:`A_{i}` se calcula sumando los :math:`A_{i,r}` de todos los tipos de naturaleza urbana:

.. math::
        A_i = \sum_{r=1}^{r}{A_{i,r}}

La naturaleza urbana accesible en este modo se calcula mediante:

.. math::
        accessible_{i,r} = \sum_{j \in \left\{d_{ij} \leq d_{0,r} \right\}}{S_{j,r} \cdot f(d_{ij})}

Donde :math:`accessible_{i,r}` es la superficie total de naturaleza urbana de la clase :math:`r` accesible dentro del radio de búsqueda, ponderada por la función de decaimiento. :math:`S_{j,r}` es la superficie de naturaleza urbana en el píxel :math:`j` de la clase de naturaleza urbana :math:`r`.

Los demás pasos y resultados son los mismos que en el modelo básico.


.. _una-summarize-by-population-groups:

Ejecución del modelo con resultados resumidos por grupos de población
---------------------------------------------------------------------

El usuario tiene la opción de proporcionar las características de la población indicando la proporción de la población total que pertenece a un determinado grupo de población dentro de cada unidad administrativa. Ejemplos de grupos de población pueden ser los rangos de edad o de renta. El usuario decidirá cómo dividir la población en función de la disponibilidad de datos y del objetivo del estudio.

Para analizar el equilibrio entre la oferta y la demanda de determinados grupos dentro de la población general, se realiza un cálculo adicional para cada grupo :math:`gn`, dada la proporción del grupo en la población total de una unidad administrativa, :math:`Rp,gn`.

Para la población desabastecida dentro del grupo :math:`gn` y la unidad administrativa :math:`adm`, esto se define como:

.. math::
        Pund_{adm,gn} = Pund_{adm} \cdot Rp,gn

Y para la población sobreabastecida dentro del grupo :math:`gn` y la unidad administrativa :math:`adm`:

.. math::
        Povr_{adm,gn} = Povr_{adm} \cdot Rp,gn

Es posible que el usuario desee realizar más análisis de correlación entre las características de la población y los resultados anteriores para ver si determinados grupos de personas están asociados a una oferta de naturaleza urbana deficitaria o excedentaria a diferentes niveles.

.. _una-radii-per-population-group:

Ejecución del modelo con radios definidos por grupo de población
----------------------------------------------------------------

El radio de búsqueda tiene un impacto importante en la oferta de naturaleza urbana y las distintas poblaciones tienen radios diferentes. Por ejemplo, las personas con vehículo propio pueden desplazarse más lejos para su recreo, o las personas mayores pueden recorrer distancias más cortas (Liu et al., 2022). Este radio de búsqueda específico del grupo :math:`d_{0,gn}` es definido por el usuario para cada grupo :math:`gn` junto con la proporción de la población total dentro de una unidad administrativa que pertenece a este grupo. Con estos dos datos específicos de cada grupo se puede obtener la naturaleza urbana de cada grupo en un píxel, :math:`A_{i,gn}`.

En primer lugar, el área de naturaleza urbana se dividirá entre la población dentro de su radio de búsqueda, :math:`R_{j}`. Dado que los distintos grupos tienen radios diferentes (véase la figura siguiente), la población total servida es la suma de cada grupo dentro de sus respectivos radios de búsqueda. La población en el píxel :math:`i` está formada por diferentes grupos. El tamaño del grupo :math:`gn` en el píxel :math:`i` se calcula así:

.. math::
        P_{i,gn} = P_i \cdot Rp,gn

donde :math:`P_{i}` es la población en el píxel :math:`i`, y :math:`Rp,gn` es la proporción de este grupo en la población total dentro de cada unidad administrativa individual.

.. math::
        R_j  = \frac{S_j}{
                        \sum_{gn=1}^{gn} \left( \sum_{k \in \{d_{kj} \leq d_{0,gn} \}}{ P_{k,gn} \cdot f(d_{jk})} \right)
                }

.. figure:: ../en/urban_nature_access/travel-distance-pop-groups.png
   :width: 5.18229in
   :height: 2.56746in

   La naturaleza urbana presta servicio a los adultos mayores dentro de d0, g1 (el radio para este grupo de población), y presta servicio a los adultos más jóvenes dentro de d0, g2 (el radio para ese grupo de población).

La oferta de naturaleza urbana al grupo :math:`gn` por píxel :math:`i` se calcula mediante (y se ejemplifica conceptualmente en la Figura siguiente):

.. math::
        A_{i,gn} = \sum_{j \in \{d_{ij} \leq d_{0,gn}\}} R_j \cdot f(d_{ij})

.. figure:: ../en/urban_nature_access/travel-distance-pop-groups-detail.png
   :width: 6.5in
   :height: 2.125in

   La población de mayor edad solo recibe servicios de los espacios verdes situados en d0, g1, es decir, el espacio verde A; los adultos más jóvenes reciben servicios de los espacios verdes situados en d0, g2, es decir, el espacio verde A y el espacio verde B.
   dentro de d0, g2, es decir, el espacio verde A y el espacio verde B.

La oferta media de naturaleza urbana per cápita para el píxel :math:`i` se calcula mediante una suma ponderada de :math:`A_{i,gn}`:

.. math::
        A_i = \sum_{n=1}^{n}{A_{i,gn} \cdot Rp,gn}

El equilibrio de la naturaleza urbana per cápita en el píxel :math:`i`, :math:`SUP\_ DEM_{i,cap}` se define evaluando la diferencia entre la naturaleza urbana suministrada al píxel :math:`i` y el objetivo de planificación definido por el usuario para la naturaleza urbana per cápita, :math:`g_{cap}`:

.. math::
        SUP\_DEM_{i,cap} = A_i - g_{cap}

El balance de naturaleza urbana per cápita del grupo :math:`gn` en el píxel :math:`i` (:math:`SUP\_ DEM_{i,cap,gn}`) se define evaluando la diferencia entre la naturaleza urbana suministrada al grupo :math:`gn` en el píxel :math:`i` y el objetivo de planificación para la naturaleza urbana per cápita, :math:`g_{cap}`:

.. math::
        SUP\_DEM_{i,cap,gn} = A_{i,gn} - g_{cap}

:math:`P_{i,gn}` es la población del grupo :math:`gn` en el píxel :math:`i`. La población del grupo :math:`gn` en el píxel :math:`i` multiplicada por el balance de naturaleza urbana per cápita del mismo grupo, (:math:`SUP\_ DEM_{i,cap,gn}`), dará el balance oferta-demanda de área de naturaleza urbana de ese grupo en el píxel :math:`i`. La suma del balance oferta-demanda de todos los grupos en el píxel *i* generará el balance oferta-demanda de todas las personas en el píxel *i* (:math:`SUP\_ DEM_{i}`).


.. math::
        SUP\_DEM_i = \sum_{gn=1}^{gn}{SUP\_DEM_{i,cap,gn} \cdot P_{i,gn}}

Para obtener un balance oferta-demanda de naturaleza urbana per cápita a nivel administrativo, el balance oferta-demanda de naturaleza urbana a nivel administrativo :math:`SUP\_ DEM_{adm}` se divide por la población total de la unidad administrativa :math:`P_{adm}`:

.. math::
        SUP\_DEM_{adm,cap} = \frac{SUP\_DEM_{adm}}{P_{adm}}

Para calcular el balance medio per cápita de oferta y demanda del grupo :math:`gn` con una unidad administrativa :math:`adm`, el modelo multiplica el balance de espacios verdes :math:`SUP\_ DEM_{i,cap,gn}` por la población del grupo :math:`gn` en el píxel :math:`i`, y luego se suma para todos los píxeles en :math:`adm` y se divide por la población del grupo :math:`gn` dentro de :math:`adm`.

.. math::
        SUP\_DEM_{adm,cap,gn} = \frac{
                        \sum_{i \in \{adm\}}{SUP\_DEM_{i,cap,gn} \cdot P_{i,gn}}
                }{
                        P_{adm,gn}
                }

Para analizar el equilibrio entre la oferta y la demanda de determinados grupos dentro de la población general, se realiza un cálculo adicional.

La población del grupo :math:`gn` que tiene un déficit de naturaleza urbana dentro de la unidad administrativa :math:`adm` viene dada por:

.. math::
        Pund_{adm,gn} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i,gn} & \text{if} SUP\_DEM_{i,cap,gn} < 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}


La población subabastecida total dentro de la unidad administrativa :math:`adm` viene dada por:

.. math::
        Pund_{adm} = \sum_{gn=1}^{gn}{Pund_{adm,gn}}

La población del grupo :math:`gn` que tiene un excedente de naturaleza urbana dentro de la unidad administrativa :math:`adm` viene dada por:

.. math::
        Povr_{adm,gn} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i,gn} & \text{if} SUP\_DEM_{i,cap,gn} > 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}

La población total sobreabastecida dentro de la unidad administrativa :math:`adm` viene dada por:

.. math::
        Povr_{adm} = \sum_{gn=1}^{gn}{Povr_{adm,gn}}

La naturaleza urbana accesible en este modo se calcula mediante:

.. math::
        accessible_{i,gn} = \sum_{j \in \left\{d_{ij} \leq d_0 \right\}} S_{j,gn} \cdot f(d_{ij})

Donde :math:`accessible_{i,gn}` es la superficie total de naturaleza urbana accesible al grupo de población :math:`gn` dentro del radio de búsqueda, ponderada por la función de decaimiento. :math:`S_{j,gn}` es la superficie de naturaleza urbana en el píxel :math:`j` accesible al grupo :math:`gn`.

Limitaciones y simplificaciones
===============================

Las distancias de búsqueda (radios) son euclidianas (en línea recta), el modelo no tiene en cuenta las carreteras ni otras limitaciones de desplazamiento a pie/en transporte del mundo real.

El modelo no tiene en cuenta el tamaño total de las zonas verdes, solo evalúa las distintas clases de zonas verdes y sus atributos por píxel. Una solución para esto es definir diferentes clases de uso del suelo basadas en el tamaño, como "parques pequeños" y "parques grandes". A continuación, se puede definir un radio de visitas diferente para cada clase de tamaño.

La demanda utiliza un cálculo genérico (m2 per cápita), mientras que las ciudades suelen adoptar distintos enfoques para cuantificarla. Además, no existe una métrica internacional oficial de la demanda que pueda aplicarse fácilmente, por lo que es necesario el conocimiento local.

El resultado del modelo puede utilizarse como indicador de los beneficios recreativos y para la salud, pero no es un indicador ideal de la complejidad de las relaciones entre el ser humano y la naturaleza.

Necesidades de datos
====================

.. note::
    Los datos de muestra se suministran para proporcionar ejemplos de requisitos y formato.

Todos los inputs espaciales deben estar en el mismo sistema de coordenadas proyectado y en unidades de metros lineales. Las salidas se remuestrearán para que coincidan con la resolución cuadrada y la proyección espacial del LULC.

-  :investspec:`urban_nature_access workspace_dir`
-  :investspec:`urban_nature_access results_suffix`
-  :investspec:`urban_nature_access lulc_raster_path`
-  :investspec:`urban_nature_access lulc_attribute_table`

   Columnas:

   -  :investspec:`urban_nature_access lulc_attribute_table.columns.lucode`
   -  :investspec:`urban_nature_access lulc_attribute_table.columns.urban_nature`
   -  :investspec:`urban_nature_access lulc_attribute_table.columns.search_radius_m`

-  :investspec:`urban_nature_access population_raster_path`

-  :investspec:`urban_nature_access admin_boundaries_vector_path`

      Fields:

      -  :investspec:`urban_nature_access admin_boundaries_vector_path.fields.pop_[POP_GROUP]`

 Ejemplo de tabla de atributos para un vector de límites administrativos con 3 geometrías:

      +--------------+----------------+
      | **pop_male** | **pop_female** |
      +==============+================+
      | 0.56         | 0.44           |
      +--------------+----------------+
      | 0.42         | 0.58           |
      +--------------+----------------+
      | 0.38         | 0.62           |
      +--------------+----------------+

-  :investspec:`urban_nature_access urban_nature_demand`

-  :investspec:`urban_nature_access search_radius_mode`

-  :investspec:`urban_nature_access search_radius`

-  :investspec:`urban_nature_access population_group_radii_table`

    Columnas:

    -  :investspec:`urban_nature_access population_group_radii_table.columns.pop_group`

    -  :investspec:`urban_nature_access population_group_radii_table.columns.search_radius_m`

    Ejemplo de tabla de correspondencia de los grupos en el vector de límites administrativos presentado antes:

    +---------------+---------------------+
    | **pop_group** | **search_radius_m** |
    +===============+=====================+
    | pop_male      | 900                 |
    +---------------+---------------------+
    | pop_female    | 1200                |
    +---------------+---------------------+


..
    -  :investspec:`urban_nature_access decay_function_power_beta`

Interpretación de los resultados
================================

Carpeta de resultados
---------------------

-  **output/urban_nature_supply_percapita.tif** Suministro calculado de naturaleza urbana. Unidades: naturaleza urbana per cápita suministrada al píxel i (metros cuadrados por persona).

-  **outputs/urban_nature_demand.tif** Superficie de naturaleza urbana que necesita la población residente en cada píxel para satisfacer plenamente sus necesidades de naturaleza urbana. Los valores más altos indican una mayor demanda de naturaleza urbana accesible desde el área circundante. Unidades: metros cuadrados de naturaleza urbana por píxel.

- output/urban_nature_balance_percapita.tif** Valor a nivel de píxel del equilibrio de la naturaleza urbana per cápita. Los valores de píxel positivos indican un exceso de oferta de naturaleza urbana en relación con la demanda de naturaleza urbana declarada. Los valores negativos indican una oferta insuficiente de naturaleza urbana en relación con la demanda declarada de naturaleza urbana. Este resultado es de especial interés para interpretar dónde los individuos están más privados de naturaleza. Unidades: Metros cuadrados de déficit de naturaleza urbana por persona.

-  **outputs/urban_nature_balance_totalpop.tif** El balance de naturaleza urbana para la población total en un píxel. Los valores positivos del píxel indican un exceso de oferta de naturaleza urbana en relación con la demanda declarada de naturaleza urbana. Los valores negativos indican una oferta insuficiente de naturaleza urbana en relación con la demanda declarada de naturaleza urbana. Este resultado es de especial relevancia para comprender la cantidad total de déficit de naturaleza para la población en un píxel concreto. Unidades: metros cuadrados de déficit o exceso de naturaleza urbana por píxel.

-  **output/admin_boundaries.gpkg** Una copia del vector de límites administrativos del usuario con una sola capa.

-  SUP_DEMadm_cap - el balance medio oferta/demanda de naturaleza urbana disponible por persona dentro de esta unidad administrativa.

-  Pund_adm - la población total dentro de la unidad administrativa que está subabastecida de naturaleza urbana.

   -  Povr_adm - la población total dentro de la unidad administrativa que tiene un exceso de naturaleza urbana.

   Si el usuario ha seleccionado agregar los resultados por grupo de población o ha elegido ejecutar el modelo con radios de búsqueda definidos por grupo de población, se crearán estos campos adicionales:

  -  SUP_DEMadm_cap_[POP_GROUP] - el balance medio de oferta/demanda de naturaleza urbana disponible por persona en el grupo de población POP_GROUP dentro de esta unidad administrativa.

   -  Pund_adm_[POP_GROUP] - la población total perteneciente al grupo de población POP_GROUP dentro de esta unidad administrativa que está subabastecida de naturaleza urbana.

   -  Povr_adm_[POP_GROUP] - la población total perteneciente al grupo de población POP_GROUP dentro de esta unidad administrativa que tiene un exceso de naturaleza urbana.

Los demás archivos del directorio de salida varían en función del modo de radio de búsqueda seleccionado:

Radio de búsqueda uniforme
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **output/accessible_urban_nature.tif** - la superficie de naturaleza urbana accesible dentro del radio de búsqueda proporcionado, ponderada por la función de decaimiento. Unidades: metros cuadrados.

Radios de búsqueda definidos por clase de naturaleza urbana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **output/accessible_urban_nature_lucode_[LUCODE].tif** - el área de naturaleza urbana de la clase LUCODE dentro del radio de búsqueda proporcionado para este lucode, ponderado por la función de decaimiento.  Unidades: metros cuadrados.

Radios de búsqueda definidos por grupo de población
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **output/accessible_urban_nature_to_[POP_GROUP].tif** - superficie de naturaleza urbana accesible al grupo de población POP_GROUP dado el radio de búsqueda del grupo de población, ponderado por la función de decaimiento. Unidades: metros cuadrados.

Carpeta intermedia
------------------

Estos archivos se producirán en cada modo de radio de búsqueda:

-  **intermediate/aligned_lulc.tif** Una copia del ráster de uso del suelo del usuario. Si el LULC proporcionado por el usuario tiene píxeles no cuadrados, se volverán a muestrear a píxeles cuadrados.

-  **intermediate/aligned_population.tif** El ráster de población del usuario, alineado con la misma resolución y dimensiones que el ráster LULC alineado. Unidades: personas por píxel.

-  **intermediate/undersupplied_population.tif** Cada píxel representa la población del total de la población que experimenta un déficit de naturaleza urbana. Unidades: personas por píxel.

-  **intermediate/oversupplied_population.tif** Cada píxel representa la población total que experimenta un excedente de naturaleza urbana. Unidades: personas por píxel.

Los demás archivos encontrados en el directorio intermedio varían en función del modo de radio de búsqueda seleccionado:

Radio de búsqueda uniforme
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **intermediate/distance_weighted_population_within_[SEARCH_RADIUS].tif**
      A sum of the population within the given search radius SEARCH_RADIUS,
      weighted by the user's decay function. Units: people per pixel.

-  **intermediate/urban_nature_area.tif** Pixels values represent the
      area of urban nature(in square meters) represented in each pixel.
      Units: square meters.

-  **intermediate/urban_nature_population_ratio.tif** The calculated
      urban nature/population ratio.

Radios de búsqueda definidos por clase de naturaleza urbana
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **intermediate/distance_weighted_population_within_[SEARCH_RADIUS].tif** Suma de la población dentro del radio de búsqueda SEARCH_RADIUS dado, ponderada por la función de decaimiento del usuario. Unidades: personas por píxel.

-  **intermediate/urban_nature_area_[LUCODE].tif** Los valores de píxel representan el área de naturaleza urbana (en metros cuadrados) representada en cada píxel para la clase de naturaleza urbana representada por el código de uso del suelo LUCODE. Unidades: metros cuadrados.

-  **intermediate/urban_nature_population_ratio_lucode_[LUCODE].tif** Relación naturaleza urbana/población calculada para la clase de naturaleza urbana representada por el código de ocupación del suelo LUCODE. Unidades: metros cuadrados por persona.

-  **intermediate/urban_nature_supply_percapita_lucode_[LUCODE].tif** La naturaleza urbana suministrada a las poblaciones debido a la clase de uso del suelo LUCODE. Unidades: metros cuadrados por persona.

Radios de búsqueda definidos por grupo de población
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **output/urban_nature_balance_[POP_GROUP].tif** Los valores positivos de píxeles indican un exceso de oferta de naturaleza urbana en relación con la demanda declarada de naturaleza urbana para el grupo de población POP_GROUP. Los valores negativos indican una oferta insuficiente de naturaleza urbana en relación con la demanda declarada de naturaleza urbana para el grupo de población POP_GROUP. Unidades: metros cuadrados de naturaleza urbana por persona.

-  **intermediate/urban_nature_area.tif** Los valores de los píxeles representan la superficie de naturaleza urbana (en metros cuadrados) representada en cada píxel. Unidades: metros cuadrados.

-  **intermediate/population_in_[POP_GROUP].tif** Cada píxel representa la población de un píxel perteneciente a la población del grupo de población POP_GROUP. Unidades: personas por píxel.

-  **intermediate/proportion_of_population_in_[POP_GROUP].tif** Cada píxel representa la proporción de la población total que pertenece al grupo de población POP_GROUP. Unidades: proporción entre 0 y 1.

-  **intermediate/distance_weighted_population_in_[POP_GROUP].tif** Cada píxel representa el número total de personas dentro del radio de búsqueda para este grupo de población POP_GROUP, ponderado por la selección del usuario de la función de decaimiento. Unidades: personas por píxel.

-  **intermediate/distance_weighted_population_all_groups.tif** La población total, ponderada por la función de decaimiento apropiada. Unidades: personas por píxel.

-  **intermediate/urban_nature_supply_percapita_to_[POP_GROUP].tif** La oferta de naturaleza urbana al grupo de población POP_GROUP. Unidades: metros cuadrados por persona.

-  **intermediate/undersupplied_population_[POP_GROUP].tif** Cada píxel representa la población del grupo de población POP_GROUP que experimenta un déficit de naturaleza urbana. Unidades: personas por píxel.

-  **intermediate/oversupplied_population_[POP_GROUP].tif** Cada píxel representa la población en el grupo de población POP_GROUP que está experimentando un excedente de naturaleza urbana. Unidades: personas por píxel.

Apéndice: Fuentes de datos
==========================

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

Ráster de población
-------------------

Existen múltiples conjuntos de datos regionales y mundiales que estiman el tamaño y la densidad de la población a alta resolución, como:

   - Datos de población mundial de WorldPop:
     https://www.worldpop.org/methods/populations/

   - Datos de densidad de población mundial de Meta/CIESIN:
     https://dataforgood.facebook.com/dfg/tools/high-resolution-population-density-maps

   - Datos de la población europea de 100 m:
     https://www.eea.europa.eu/data-and-maps/data/population-density-disaggregated-with-corine-land-cover-2000-2

Datos sobre espacios verdes urbanos
-----------------------------------

Existen múltiples conjuntos de datos regionales y mundiales que definen o ayudan a definir la naturaleza urbana, entre ellos los siguientes:

Liu H., Hamel P., Tardieu L., Remme R.P., Han B., Ren H., 2022. A geospatial model of nature-based recreation for urban planning: Case study of Paris, France. Land Use Policy, https://doi.org/10.1016/j.landusepol.2022.106107.
   - ciudades latinioamericanas:
     https://www.nature.com/articles/s41597-022-01701-y

Mao L. and Nekorchuk D., 2013. Measuring spatial accessibility to health care for populations with multiple transportation modes. Health &Place 24, 115–122. https://doi.org/10.1016/j.healthplace.2013.08.008
   - ciudades europeas: 
	https://land.copernicus.eu/local/urban-atlas

Xing L.J, Liu Y.F, Liu X.J., 2018. Measuring spatial disparity in accessibility with a multi-mode method based on park green spaces classification in Wuhan, China. Applied Geography 94, 251–261. https://doi.org/10.1016/j.apgeog.2018.03.014
   - Datos globales:

       -  http://data.ess.tsinghua.edu.cn/
       - https://www.openstreetmap.org/

   (Para comparar, véase: https://www.sciencedirect.com/science/article/abs/pii/S1618866722001819)

Demanda de naturaleza urbana
----------------------------

No existe una norma mundial para la demanda de naturaleza urbana. Un valor comúnmente sugerido es 9m2, que a menudo se atribuye incorrectamente a la OMS (véase https://www.researchgate.net/post/I-see-many-studies-citing-WHO-for-their-international-minimum-standard-for-green-space-9m2-per-capita-But-where-is-the-actual-study/4 para el debate sobre este valor). Liu et al. (2022), Liu et al. (2021) y Badiu et al. (2016) son algunos de los trabajos que ofrecen una visión general de los valores de demanda y un debate en torno a ellos.

Referencias
===========

Andkjaer S., Arvidsen J. 2015. Places for active outdoor recreation - a
scoping review. Journal of Outdoor Recreation and Tourism, *12*, 25-46.
https://doi.org/10.1016/j.jort.2015.10.001

Badiu, D.L., Ioja, C.I., Patroescu, M., Breuste, J., Artmann, M., Nita,
M.R., Gradinaru, S.R., Hossu, C.A., Onose, D.A. 2016. Is urban green
space per capita a valuable target to achieve cities’ sustainability
goals? Romania as a case study. Ecological Indicators *70*, 53-66.
https://doi.org/10.1016/j.ecolind.2016.05.044

Bratman, G. N., Anderson, C. B., Berman, M. G., Cochran, B., De Vries,
S., Flanders, J., ... y Daily, G. C. 2019. Nature and mental health: An
ecosystem service perspective. Science advances, *5*\ (7), eaax0903.
https://doi.org/10.1126/sciadv.aax0903

Keeler, B. L., Hamel, P., McPhearson, T., Hamann, M. H., Donahue, M. L.,
Meza Prado, K. A., ... y Wood, S. A. 2019. Social-ecological and
technological factors moderate the value of urban nature. Nature
Sustainability, *2*\ (1), 29-38.
https://doi.org/10.1038/s41893-018-0202-1

Liu, H., Remme, R.P., Hamel, P., Nong, H., Ren, H., 2020. Supply and
demand assessment of urban recreation service and its implication for
greenspace planning-A case study on Guangzhou. Landsc. Urban Plan. 203,
103898. https://doi.org/10.1016/j.landurbplan.2020.103898

Liu H., Hamel P., Tardieu L., Remme R.P., Han B., Ren H., 2022. A
geospatial model of nature-based recreation for urban planning: Case
study of Paris, France. Land Use Policy,
https://doi.org/10.1016/j.landusepol.2022.106107.

Mao L. y Nekorchuk D., 2013. Measuring spatial accessibility to health
care for populations with multiple transportation modes. Health & Place
24, 115–122. https://doi.org/10.1016/j.healthplace.2013.08.008

Remme, R. P., Frumkin, H., Guerry, A. D., King, A. C., Mandle, L.,
Sarabu, C., ... y Daily, G. C. 2021. An ecosystem service perspective on
urban nature, physical activity, and health. Proceedings of the National
Academy of Sciences, *118*\ (22), e2018472118.
https://doi.org/10.1073/pnas.2018472118

Roo, M. D., Kuypers, V. H. M. y Lenzholzer, S. 2011. *The green city
guidelines: techniques for a healthy liveable city*. The Green City.
http://library.wur.nl/WebQuery/wurpubs/fulltext/178666

Xing L.J, Liu Y.F, Liu X.J., 2018. Measuring spatial disparity in
accessibility with a multi-mode method based on park green spaces
classification in Wuhan, China. Applied Geography 94, 251–261.
https://doi.org/10.1016/j.apgeog.2018.03.014
