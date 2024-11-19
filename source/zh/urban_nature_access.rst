===================
城市自然空间可达性模型
===================

总结
=======

城市地区的自然环境为娱乐提供了重要的机会。城市自然空间可达模型提供了两种供应的衡量标准城市自然和城市人口对自然的需求，最终计算供需之间的平衡。两个城市自然和种群可以选择性地分为不同的组。供应取决于城市自然的类型、大小、邻近程度和质量，供应是出于娱乐目的的人均可使用量。需求被定义为人均自然空间，符合政策的典型要求或标准。平衡量化了供应满足的个人、行政和城市层面的需求。

介绍
============

城市地区的自然环境为娱乐提供了重要的机会，对社会、心理和身体健康都有益处（布拉特曼等人，2019 年，Keeler 等人，2019 年，Remme 等人，2021 年）。正如 Liu 等人（2022）所评论的那样，评估基于自然的娱乐需要理解 i） 城市自然“供应”，这本身取决于可用性和质量，以及 ii） 城市自然“需求”，这取决于关于人们的偏好或政策要求。

该InVEST模型遵循Liu等人（2022）中描述的结构，通过评估城市自然和地方的供求关系和供需平衡，指明盈余或赤字的领域（分别为正平衡或负平衡）的城市性质，并尊重政策标准（Liu et al.， 2022）。在这样做时，模型专注于城市地区的自然通道。因为该模型能够对多种类型的城市自然的供给、需求和平衡进行建模，例如作为公园、绿地、湿地和海岸线，这里作为城市自然访问模型。由用户选择在他们的分析中包括城市自然的哪些组成部分。

默认模型评估整体城市自然供给、需求和城市总人口的平衡。此外，三个可选
核心模型的扩展可用于提供更详细的信息
结果：

- 城市自然的供给、需求和平衡可以概括为人群中的不同群体（例如，按不同年龄、群体、收入水平、种族或民族等），这可能是对公平考虑很重要。参考
    ：ref：'una-summarize-by-population-groups`

- 为了更详细地了解城市自然的供应，用户可以选择提供关于多远的更详细的信息，人们可能会通过旅行以使用不同种类的城市自然。例如，人们可能会走得更远去参观与当地口袋公园相比更大型的公园。参考
    ：ref：'una-radii-per-urban-nature-class`

- 更详细地了解城市自然对不同人群的供应，用户可以选择提供关于不同群体可
能旅行到多远到达城市自然的信息。例如，拥有汽车的人可能会比依赖公共交通的人到达更远的地方。
　　请参阅：ref：'una-radii-per-population-group`

模型
=========

该模型根据位置以及城市绿地的数量、人口的分布和数量以及人均需求或人均城市自然空间需求计算城市自然空间可达。以像素表示的城市自然区域
：math：'j' 表示为 ：math：'S_j'。：math：'S_j' 的值以正方形表示，其中被城市绿地覆盖的像素区域的比例被称为土地利用/土地覆盖（LULC）属性表。
以像素为单位的人口
：math：'i' 由 ：math：'P_i' 表示。城市绿地人均需求被指定为 ：math：'g_{cap}'，并且通常基于策略目标。
这些组件一起用于计算以下三个主要指标，在 ：ref：'una-running-the-default-model' 中更详细地描述：

-  **城市绿地供应：** 城市绿地量供应给居住在像素中的人口
-  **城市自然需求：** 按像素中的人口产生城市绿地需求量
-  **城市自然平衡：** 一个像素中的绿地供应量和人口产生需求量的差异

衰减函数
--------------

如果自然区域离他们住所更近，人们会更频繁地使用自然区域（Andkjaer&Arvidsen，2015）。该频率随着距离的增加而降低。这被称为“距离衰减”。该模型描述了城市自然与人口之间的这种距离衰减的衰减函数 ：math：'f\left（ d_{ij} \right）' 其中 ：math：'d_{ij}' 是自然和人口像素之间的距离，并且 ：math：'d_{0}' 是用户定义的搜索自然像素的搜索距离。搜索距离为欧几里得距离（像素 A 和 B之间党的直线距离） 的中心点，并假定为正方形像素。

..图：： ./urban_nature_access/decay_function_intro.png
          ：align： center
          ：figwidth：400px

该模型提供了各种距离衰减公式，供用户使用选择其中，下面将更详细地定义和说明。
**二分法**选项处理设置的搜索距离内的所有像素，像素作为平等可访问的。当
城市自然或绿地政策以在距人们住所的特定距离内一定数量的自然为目标。例如，
荷兰设定的目标至少是距离家庭 500m 以内每人有60平方米的城市绿地（Roo 等人，2011 年）。

对于考虑到城市自然服务的衰败的研究，更多真实地表示参观城市自然的概率，衰减函数应与可用的访问数据匹配。因此，三个提供额外的距离衰减函数 – **指数，高斯，**和**密度**。所有人都更加重视城市自然离人更近，反映出人们偏向于参观离他们更近的大自然。

二分法
---------

二分核考虑搜索距离内的所有像素。：math：'d_{0}'可被平等访问的城市绿地像素。

.. math::

\begin{对齐*}
f（d_{ij}， d_0） &= \left\{\begin{array}{lr}
1 & \text{if} d_{ij} \leq d_0 \\
0 & \text{if} d_{ij} > d_0 \\
\end{array}\right\} \\
\end{对齐*}


.. figure:: ./urban_nature_access/kernel-dichotomy.png
        :align: center
        :figwidth: 500px


指数
-----------

距离加权指数衰减函数，人们更有可能访问离他们最近的自然环境，可能性呈指数下降到最大半径：math：'d_{0}'。

.. math::
        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                e^{(-d_{ij}/d_0)} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}
.. figure:: ./urban_nature_access/kernel-exponential.png
        :align: center
        :figwidth: 500px
..
权利
*****

电源内核要求用户定义自己的衰减率，通过用户选择的参数定义:math:`\beta`.

.. math::

          \begin{align*}
          f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                  d_{ij}^{(-\beta)} & \text{if} d_{ij} \leq d_0 \\
                  0 & \text{if} d_{ij} \gt d_0 \\
          \end{array}\right\} \\
          \end{align*}

  .. figure:: ./urban_nature_access/kernel-power.png
          :align: center
          :figwidth: 500px


高斯
--------

距离加权衰减函数，人们更有可能访问离他们最近的自然，其中根据正态（“高斯”）分布，西格玛为 3，在最大半径范围内，似然递减：math：'d_{0}'。
.. math::
        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                \frac{e^{-\frac{1}{2}\left ( \frac{d_{ij}}{d_0} \right )^2}-e^{-\frac{1}{2}}}{1-e^{-\frac{1}{2}}} & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}
.. figure:: ./urban_nature_access/kernel-gaussian.png
        :align: center
        :figwidth: 500px

密度
-------

距离加权衰减函数，人们更有可能访问离他们最近的自然，其中随着距离的增加，可能性降低得更快：math：'d_{0}'。
.. math::
        \begin{align*}
        f(d_{ij}, d_0) &= \left\{\begin{array}{lr}
                \frac{3}{4}\left(1-\left(\frac{d_{ij}}{d_{0}}\right)^{2}\right) & \text{if} d_{ij} \leq d_0 \\
                0 & \text{if} d_{ij} \gt d_0 \\
        \end{array}\right\} \\
        \end{align*}
.. figure:: ./urban_nature_access/kernel-density.png
        :align: center
        :figwidth: 500px
.. _una-running-the-default-model:

运行默认模型
-------------------------

默认模型假定具有均匀的行进半径（“搜索半径”）由用户定义，即距离某人住所 X 米距离内的自然有助于一个人的娱乐。

计算城市自然供给
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

城市绿地对每个居民像素的供应的计算采用两步浮动集水区（2SFCA）方法（毛和Nekorchuk，2013;Xing 等人，2018 年）。给定一个城市自然像素 ：math：'j'，所有搜索搜索半径为 ：math：'d_{0}' 的人口像素。计算此像素的城市自然/人口比率：math：'R_{j}'使用自然像素的面积：math：'S_{j}'除以总和。搜索半径内的人口，根据所选内容进行加权搜索内核的基于距离的权重。然后，以每个像素为中心在人口栅格中，其内的所有自然像素搜索距离加权集水区。所有 ：math：'R_{j}'将这些自然像素相加，以计算每个城市自然供应capita ：math：'A_{i}' 添加到每个人口像素。我们采用这种方法进行供应，而不仅仅是房屋半径内的自然数量，因为使用基于重力的方法考虑了自然的加权可用性。换句话说，2SFCA考虑了在城市地区很常见的很多人使用绿地的背景。

这可以从图形上理解为：
.. figure:: ./urban_nature_access/2SFCA_step1_v2.png
        :align: center
        :figwidth: 400px
　　　　第 1 步：在城市自然的搜索半径内定位人口。

.. figure:: ./urban_nature_access/2SFCA_step2_v2.png
        :align: center
        :figwidth: 400px

　　　　第 2 步：在人口搜索半径内定位城市自然。


更正式地说，城市性质/人口比率：math：'R_{j}' 定义为：
.. math::
        \begin{align*}
        R_j &= \left\{\begin{array}{lr}
                \frac{S_j}{\sum_{k \in \left\{d_{jk} \leq d_0  \right\}} P_k \cdot f(d_{jk})} & \text{if} P_k \cdot f(d_{jk}) >= 1 \\
                S_j & \text{otherwise} \\
        \end{array}\right\} \\
        \end{align*}
式中：

-  ：math：'R_{j}' 是自然像素 ：math：'j' 的城市自然/人口比率。
-  ：math：'S_{j}' 是以像素表示的自然区域 ：math：'j'
-  ：math：'d_{0}' 是搜索半径
-  ：math：'k' 是自然像素搜索半径内的人口像素 ：math：'j'
-  ：math：'d_{jk}' 是自然像素 ：math：'j' 和人口像素 ：math：'k' 之间的距离。
-  ：math：'P_{k}' 是像素 ：math：'k' 的填充。
-  ：math：'f（d）' 是选定的衰减函数。

然后，城市自然/人口比率由所选衰减函数，并在搜索半径内求和，得到绿地
供应， ：math：'A_{i}'：

.. math::
        A_i = \sum_{j \in \left\{d_{ij} \leq d_0  \right\}} R_j \cdot f(d_{ij})
式中：

-  ：math：'i' 是人口栅格中的任意像素
-  ：math：'A_{i}' 是提供给像素的人均城市性质 ：math：'i'（每人平方米）
-  ：math：'d_{ij}' 是像素 ：math：'i' 和自然像素 ：math：'j' 之间的距离。
-  ：math：'d_{0}' 是搜索半径

计算城市自然需求
源自人口图层和用户定义的城市性质
需求，这衡量了所需的可访问城市自然的数量
充分供应每个像素中的所有人。

.. math::
        demand_{i} = P_{i} \cdot g_{cap}

式中：

-  :math:`i` 是一个像素
-  :math:`demand_{i}` 是居住在 pixel ：math：'i' 的人口所需的城市自然面积（以平方米为单位），以充分满足他们的城市自然需求
-  :math:`P_{i}` 是像素 ：math：'i' 处的人口（每像素人数）
-  :math:`g_{cap}` 是用户定义的人均城市自然要求（每人平方米）


计算城市自然平衡

地方规划文件或城市规划目标通常指出，每
居住在一个地区应该被分配一定数量的自然，
：math：'g_{cap}'。人均城市自然供需预算
：math：'SUP\_ DEM_{i，cap}' 在 pixel ：math：'i' 处，通过评估来定义
提供的城市自然与规划目标之间的平衡
自然（通常是绿地）人均每像素：

.. math::
        SUP\_DEM_{i,cap} = A_i - g_{cap}

要确定每个像素中所有人的平衡,
:math:`SUP\_ DEM_{i,cap}` 乘以总体 :math:`P_{i}`
在 pixel :math:`i`:

.. math::
        SUP\_DEM_{i} = SUP\_DEM_{i,cap} \cdot P_i

计算无障碍城市自然

查找给定搜索半径内的总面积通常很有用，由下式给出：

.. math::
accessible_{i} = \sum_{j \in \left\{d_{ij} \leq d_{0} \right\}}{S_j \cdot f（d_{ij}）}

其中 ：math：'accessible_{i}' 是可访问的城市自然总面积
搜索半径内的像素 ：math：'i' ：math：'d_0'，按衰减加权
功能。


汇总给行政单位的产出

用户必须提供具有管理单元边界的向量，该向量
可以代表用户感兴趣的任何地区级别。这些
需要边界才能获得管理级别的测量值。

行政级别的供需平衡是平衡的总和
管理边界内的每个像素 ：math：'i' ：math：'adm'：

.. math::

SUP\_DEM_{adm} = \sum_{i \in \left\{adm \right\}} SUP\_DEM_i

：math：'SUP\_ DEM_{adm}' 表示多少城市自然，以平方表示
米，在行政单位中供应不足或过剩。

人均城市自然供需平衡也
在管理级别计算：

.. math::

SUP\_DEM_{adm，cap} = \frac{SUP\_DEM_{adm}}{P_{adm}}

其中 ：math：'P_{adm}' 是管理区内的总人口
边界。

当 ：math：'SUP\_ DEM_{i，cap} 在任何给定像素 ：math：'i' 上< 0' 时，它
表示此像素中的人们对城市供应不足
自然界。将
行政单位提供行政单位中的人数
具有城市自然缺陷的单位，：math：'Pund_{adm}'，相对于
推荐城市自然 ：math：'g_{cap}'：

.. math::
Pund_{adm} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i} & \text{if} SUP\_DEM_{i,cap} < 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}

同样，同样的理由也适用于查找人数
行政单位中的城市自然盈余，
：math：'Povr_{adm}'，相对于推荐的城市自然
：math：'g_{cap}'：

. math::
        Povr_{adm} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i} & \text{if} SUP\_DEM_{i,cap} > 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}


._una-radii-per-urban-nature-class：

使用每个城市自然类定义的半径运行模型
-----------------------------------------------------------

城市自然有不同的类型。口袋公园提供便利
附近有休闲体验，而市政公园则吸引着来自
更遥远的地方。如果用户有数据来拆分城市类型
自然并调整每种类型的城市自然的旅行距离，
每种类型的城市自然对 pixel ：math：'i' 的可访问性可以
使用特定于类的半径计算。这些城市自然类型和
其关联的搜索半径由用户输入提供给模型
土地利用土地覆被 （LULC） 属性表。每种类型的 LULC
标记为城市自然的分类将在
以便提供有关无障碍城市的更详细结果
每种类型的性质。由用户决定如何拆分
城市自然。

.. figure:: ./urban_nature_access/radii_per_nature_class.png
        ：align： 居中
        ：figwidth：700px

如果说：math：'r'是城市性质的类型，那么：math：'j'就是城市性质
pixel of ：math：'r' type， ：math：'d_{0，r}' 是
：math：'r'型城市自然，则城市自然/人口比值
对于这个城市性质类型，由这个城市的面积计算
自然除以半径内的人口，加权
用户选择距离加权衰减函数：

.. math::
        R_{j,r} = \frac{S_{j,r}}{
                        \sum_{k \in \{d_{kj} \leq d_{0,r}\}}{P_k \cdot f(d_{jk})}
                }

城市自然的可访问性类型：math：'r'， ：math：'A_{i，r}'
pixel ：math：'i' 是通过将距离加权相加来计算的
：math：'R_{j，r}' 在搜索半径内：

.. math::
        A_{i,r} = \sum_{j \in d_{ij} \leq d_{0,r}}{R_{j,r} \cdot f(d_ij)}
        A_{i,r} = \sum_{j \in d_{ij} \leq d_{0,r}}{R_{j,r} \cdot f(d_{ij})}

提供给像素 ：math：'i'， ：math：'A_{i}' 的总城市性质为
计算方法是将所有类型的城市中的 ：math：'A_{i，r}' 相加
自然界：

.. math::
        A_i = \sum_{r=1}^{r}{A_{i,r}}

在此模式下，可访问的城市自然的计算公式为：

.. math::
        accessible_{i,r} = \sum_{j \in \left\{d_{ij} \leq d_{0,r} \right\}}{S_{j,r} \cdot f(d_{ij})}

其中：math：'accessible_{i，r}'是类城市性质的总面积
：math：'r' 可在搜索半径内访问，由衰减函数加权。
：math：'S_{j，r}' 是城市自然像素上的城市自然区域 ：math：'j' of urban nature
类 ：math：'r'.

其他步骤和输出与核心模型中的步骤和输出相同。


.._una-summarize-by-population-groups：

运行按总体组汇总结果的模型

用户可以选择提供人口特征指示
属于给定的总人口比例
每个行政单位内的人口组。人口示例
群体可能是年龄或收入阶层。用户将决定如何
根据数据可用性和研究对人群进行划分
目的。

分析某些群体的供需平衡
一般人群，对每组进行额外的计算
：math：'gn'，给定该组在总人口中的比例
一个管理单位，：math：'Rp，gn'。

对于组内供不应求的人群：math：'gn' 和
管理单位：math：'adm'，定义为：

.. math::
        Pund_{adm,gn} = Pund_{adm} \cdot Rp,gn

对于组内供过于求的人口：math：'gn' 和
行政单位 ：math：'adm'：

.. math::
        Povr_{adm,gn} = Povr_{adm} \cdot Rp,gn

用户不妨对以下两者进行进一步的相关性分析
种群特征和以上输出来看是否确定
人群与城市性质的赤字或过剩有关
不同级别的供应。


.._una-radii-per-population-group：

使用每个种群组定义的半径运行模型

搜索半径对城市自然供应和
不同的种群具有不同的半径。例如，具有
汽车可以行驶到更远的地方进行娱乐，或者老年人可以旅行
较短的距离（Liu 等人，2022 年）。此特定于组的搜索半径
：math：'d_{0，gn}'，由用户为每个组 ：math：'gn' 定义
行政区内总人口的比例
属于该组的单位。鉴于这两个特定于组的部分
信息，以像素形式提供给每个群体的城市性质，
：math：'A_{i，gn}' 可以得到。

首先，城市自然区将在人口之间划分
它的搜索半径，：math：'R_{j}'。由于不同的群体有不同的
半径（见下图），服务的总人口是每个
在各自的搜索半径内进行分组。像素人口
：math：'i' 由不同的组组成。组的大小 ：math：'gn'
在像素中：math：'i'的计算公式为：

.. math::
        P_{i,gn} = P_i \cdot Rp,gn

其中 ：math：'P_{i}' 是像素 ：math：'i' 处的人口，并且
：math：'Rp，gn' 是该群体在总人口中的比例
在每个单独的行政单位内。

.. math::
        R_j  = \frac{S_j}{
                        \sum_{gn=1}^{gn} \left( \sum_{k \in \{d_{kj} \leq d_{0,gn} \}}{ P_{k,gn} \cdot f(d_{jk})} \right)
                }

.. figure:: ./urban_nature_access/travel-distance-pop-groups.png
宽度： 5.18229in
   ：高度： 2.56746in

城市自然为d0，g1内的老年人提供服务
（该人群的半径），并为年轻人提供服务
D0、G2（该人群的半径）内的成年人。

按像素 ：math：'i' 计算组 ：math：'gn' 的城市自然供应量
通过（并在下图中概念上举例说明）：

.. math::
        A_{i,gn} = \sum_{j \in \{d_{ij} \leq d_{0,gn}\}} R_j \cdot f(d_{ij})

.. figure:: ./urban_nature_access/travel-distance-pop-groups-detail.png
   ：宽度： 6.5in
   ：高度： 2.125in

老年人口仅在 d0 内从绿地获得服务，
g1，即绿地A;年轻人从绿地获得服务
在 d0、g2 内，即绿地 A 和绿地 B。

人均城市自然供给量（像素：math：'i'）为：
由 ：math：'A_{i，gn}' 的加权和计算：

.. math::
        A_i = \sum_{n=1}^{n}{A_{i,gn} \cdot Rp,gn}

pixel ：math：'i' 的人均城市自然平衡，
：math：'SUP\_ DEM_{i，cap}' 是通过评估
提供给 pixel ：math：'i' 的城市性质和用户定义的
人均城市自然规划目标，：math：'g_{cap}'：

.. math::
        SUP\_DEM_{i,cap} = A_i - g_{cap}

群体：math：'gn'在像素上的人均城市自然平衡
：math：'i' （：math：'SUP\_ DEM_{i，cap，gn}'） 通过评估
提供的城市自然与组的区别 ：math：'gn' at
pixel ：math：'i' 和人均城市自然规划目标，
：math：'g_{cap}'：

.. math::
        SUP\_DEM_{i,cap,gn} = A_{i,gn} - g_{cap}

：math：'P_{i，gn}' 是 pixel 上 group ：math：'gn' 的人口
：math：'i'。组的人口 ：math：'gn' in pixel ：math：'i'
乘以同一组群的人均城市自然平衡，
(：math：'SUP\_ DEM_{i，cap，gn}'），将给出城市自然区
该组的供需平衡为 pixel ：math：'i'。求和
像素 *i* 处所有组的供需平衡将产生
Pixel *i 所有人的供需平衡*
(：math：'SUP\_ DEM_{i}'）。

.. math::
        SUP\_DEM_i = \sum_{gn=1}^{gn}{SUP\_DEM_{i,cap,gn} \cdot P_{i,gn}}

对管理中每个像素的供需平衡求和
单位将导致行政层面的供需平衡。

.. math::
        SUP\_DEM_{adm} = \sum_{i=1}^{i}{SUP\_DEM_i}

给出人均城市自然供求的行政级别
平衡，行政层面城市自然  供需平衡
：math：'SUP\_ DEM_{adm}' 除以
管理单位：math：'P_{adm}'：

.. math::
        SUP\_DEM_{adm,cap} = \frac{SUP\_DEM_{adm}}{P_{adm}}

计算集团人均供求平衡
：math：'gn' 与管理单元 ：math：'adm'，则模型相乘
绿地平衡：math：'SUP\_ DEM_{i，cap，gn}' 按
group ：math：'gn' 在 pixel ：math：'i' 处，然后对所有像素进行求和
在 ：math：'adm' 中除以组 ：math：'gn' 的总体
：math：'adm'。

.. math::
        SUP\_DEM_{adm,cap,gn} = \frac{
                        \sum_{i \in \{adm\}}{SUP\_DEM_{i,cap,gn} \cdot P_{i,gn}}
                }{
                        P_{adm,gn}
                }

分析某些群体的供需平衡
一般人群，进行额外的计算。

群体：math：'gn'的人口，他们在城市自然赤字内
管理单位：math：'adm'由下式给出：

.. math::
        Pund_{adm,gn} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i,gn} & \text{if} SUP\_DEM_{i,cap,gn} < 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}

行政单位内供不应求的总人口
：math：'adm' 由下式给出：

.. math::
        Pund_{adm} = \sum_{gn=1}^{gn}{Pund_{adm,gn}}

在城市自然盈余范围内具有城市自然盈余的组 ：math：'gn' 的人口

.. math::
        Povr_{adm,gn} = \sum_{i \in \{adm\}}
                \left\{
                        \begin{array}{lr}
                        P_{i,gn} & \text{if} SUP\_DEM_{i,cap,gn} > 0 \\
                        0 & \text{otherwise} \\
                        \end{array}
                \right\}

行政单位内供过于求的总人口
：math：'adm' 由下式给出：

.. math::
        Povr_{adm} = \sum_{gn=1}^{gn}{Povr_{adm,gn}}

在此模式下，可访问的城市自然的计算公式为：

.. math::
        accessible_{i,gn} = \sum_{j \in \left\{d_{ij} \leq d_0 \right\}} S_{j,gn} \cdot f(d_{ij})

其中：math：'accessible_{i，gn}'是可访问的城市自然总面积
到搜索半径内的人口组 ：math：'gn'，按衰减加权
功能。：math：'S_{j，gn}' 是像素上的城市自然区域 ：math：'j'
可访问组 ：math：'gn'。


限制和简化
===============================

搜索距离（半径）为欧几里得（直线），模型不考虑道路或其他实际步行/交通约束。

该模型不考虑绿地斑块的总大小，它只评估不同的绿地类别及其每个像素的属性。解决方法是根据大小定义不同的土地利用类别，例如“小型公园”和“大型公园”。然后，您可以为每个尺寸等级定义不同的访问半径。

需求使用通用计算（人均 m2），而城市通常采用不同的方法来量化需求。此外，没有可以轻松应用的官方国际需求指标，因此需要本地知识。

模型输出可以用作娱乐和健康益处的代理，但它不是人与自然关系复杂性的理想指标。


数据需求

..注意：：
提供示例数据以提供需求示例和
格式。

..注意：：
所有空间输入必须位于同一投影坐标系中，并且
以线性计量单位。输出将被重新采样以匹配
LULC 的平方分辨率和空间投影。

-  ：investspec：'urban_nature_access workspace_dir`

-  ：investspec：'urban_nature_access results_suffix`

-  ：investspec：'urban_nature_access lulc_raster_path`

-  ：investspec：'urban_nature_access lulc_attribute_table`

列：

   -  ：investspec：'urban_nature_access lulc_attribute_table.columns.lucode`
   -  ：investspec：'urban_nature_access lulc_attribute_table.columns.urban_nature`
   -  ：investspec：'urban_nature_access lulc_attribute_table.columns.search_radius_m`

-  ：investspec：'urban_nature_access population_raster_path`

-  ：investspec：'urban_nature_access admin_boundaries_vector_path`

  领域：

      -  ：investspec：'urban_nature_access admin_boundaries_vector_path.fields.pop_[POP_GROUP]`

管理边界向量的示例属性表
具有 3 种几何形状：

+--------------+----------------+
 |**pop_male** | **pop_female** |
      +==============+================+
 |0.56 | 0.44 |
      +--------------+----------------+
 |0.42 | 0.58 |
      +--------------+----------------+
 |0.38 | 0.62 |
      +--------------+----------------+

-  ：investspec：'urban_nature_access urban_nature_demand`

-  ：investspec：'urban_nature_access decay_function`

-  ：investspec：'urban_nature_access aggregate_by_pop_group`

-  ：investspec：'urban_nature_access search_radius`

-  ：investspec：'urban_nature_access population_group_radii_table`

列：

    -  ：investspec：'urban_nature_access population_group_radii_table.columns.pop_group`

    -  ：investspec：'urban_nature_access population_group_radii_table.columns.search_radius_m`

与管理中的组匹配的表的示例
上面的边界向量：

    +---------------+---------------------+
 |**pop_group** | **search_radius_m** |
    +===============+=====================+
 |pop_male | 900 |
    +---------------+---------------------+
 |pop_female | 1200 |
    +---------------+---------------------+

..
- ：investspec：'urban_nature_access decay_function_power_beta'

解释结果
====================

输出文件夹

-  **产出/urban_nature_supply_percapita.tif** 计算出的城市供应量
自然界。单位：人均城市自然供应给像素 i（平方
米/人）。

-  **产出/urban_nature_demand.tif** 城市自然所需的面积
居住每个像素的人口需要充分
满足他们的城市自然需求。值越大表示越大
对周边地区无障碍城市自然的需求。
单位：平方米每像素城市自然。

-  **output/urban_nature_balance_percapita.tif** 像素级值
人均城市自然平衡。正像素值表示
相对于所述的城市性质，城市性质供过于求
需求。负值表示城市自然供应不足
相对于所述的城市自然需求。此输出为
特别感兴趣的解释个人最自然的地方
剥夺。单位：平方米的城市自然赤字或
人均供过于求。

-  **产出/urban_nature_balance_totalpop.tif** 城市自然平衡
以像素为单位的总人口。正像素值
表明相对于所述城市自然供过于求
城市自然需求。负值表示
城市自然相对于所述的城市自然需求。这
产出与了解总量特别相关
特定像素中人口的自然赤字。单位：
每像素城市自然赤字或供过于求的平方米。

-  **output/admin_boundaries.gpkg** 用户管理的副本
具有单个图层的边界向量。

- SUP_DEMadm_cap - 平均城市自然供需平衡
在此行政单位内每人可用。

- Pund_adm - 行政单位内的总人口
城市自然供应不足。

- Povr_adm - 行政单位内的总人口
城市自然供过于求。

如果用户已选择按总体组聚合结果，或者
已选择运行搜索半径的模型，搜索半径为
population 组，则将创建以下附加字段：

- SUP_DEMadm_cap_[POP_GROUP] - 平均城市自然供需
人口组POP_GROUP每人可利用的余额
在此行政单位内。

- Pund_adm_[POP_GROUP] - 属于
人口组 POP_GROUP 在该行政单位内
城市自然供应不足。

- Povr_adm_[POP_GROUP] - 属于
人口组 POP_GROUP 在该行政单位内
城市自然供过于求。

输出目录中的其他文件因所选搜索而异
半径模式：

统一搜索半径
~~~~~~~~~~~~~~~~~~~~~

- **output/accessible_urban_nature.tif** - 可进入的城市自然区域
在提供的搜索半径内，由衰减函数加权。
单位：平方米。

搜索半径按城市自然类定义
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **output/accessible_urban_nature_lucode_[LUCODE].tif** - 城市面积
在为该 lucode 提供的搜索半径内，类 LUCODE 的性质，
由衰减函数加权。单位：平方米。

按人口组定义的搜索半径
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **output/accessible_urban_nature_to_[POP_GROUP].tif** - 城市面积
在进行搜索POP_GROUP，人口群体可进入的自然环境
总体组的半径，由衰减函数加权。单位：
平方米。


中间文件夹

这些文件将在每种搜索半径模式下生成：

-  **中级/aligned_lulc.tif** 用户土地使用土地的副本
覆盖栅格。如果用户提供的 LULC 具有非方形像素，
它们将被重新采样为方形像素。

-  **中级/aligned_population.tif** 用户的人口栅格，
与对齐的 LULC 具有相同的分辨率和尺寸。
单位：每像素人。

-  **中级/undersupplied_population.tif** 每个像素代表
总人口中正在经历
城市自然赤字。单位：每像素人。

-  **中级/oversupplied_population.tif** 每个像素代表
总人口中正在经历
城市自然盈余。单位：每像素人。

在中间目录中找到的其他文件因
选定的搜索半径模式：

统一搜索半径
~~~~~~~~~~~~~~~~~~~~~

-  **中级/distance_weighted_population_within_[SEARCH_RADIUS].tif**
给定搜索半径内的总和SEARCH_RADIUS，
由用户的衰减函数加权。单位：每像素人。

-  **intermediate/urban_nature_area.tif** 像素值表示
城市自然面积（以平方米为单位）以每个像素表示。
单位：平方米。

-  **中级/urban_nature_population_ratio.tif** 计算
城市自然/人口比率。

搜索半径按城市自然类定义
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **中级/distance_weighted_population_within_[SEARCH_RADIUS].tif**
给定搜索半径内的总和SEARCH_RADIUS，
由用户的衰减函数加权。单位：每像素人。

-  **intermediate/urban_nature_area_[LUCODE].tif** 像素值
代表城市自然面积（以平方米为单位）
在每个像素中，由土地表示的城市自然类
使用土地覆被代码 LUCODE。单位：平方米。

-  **中级/urban_nature_population_ratio_lucode_[LUCODE].tif**
计算出的城市自然/人口比率
以土地利用土地覆盖代码为代表的城市自然类别
LUCODE的。单位：平方米/人

-  **中级/urban_nature_supply_percapita_lucode_[LUCODE].tif** 城市
由于土地利用土地覆盖类别而提供给人口的自然
LUCODE的。单位：平方米/人

按人口组定义的搜索半径
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **output/urban_nature_balance_[POP_GROUP].tif** 正像素值
表明相对于所述城市自然供过于求
城市自然需求对人口群体POP_GROUP。阴性
值表示城市自然相对于
陈述了对人口群体POP_GROUP的城市自然需求。
单位：每人城市自然平方米。

-  **intermediate/urban_nature_area.tif** 像素值表示
以每个像素表示的绿地面积（以平方米为单位）。
单位：平方米。

-  **中级/population_in_[POP_GROUP].tif** 每个像素代表
属于
人口组POP_GROUP。单位：每像素人。

-  **中级/proportion_of_population_in_[POP_GROUP].tif** 每个
pixel 表示
属于人口组POP_GROUP。单位：比例
介于 0 和 1 之间。

-  **中级/distance_weighted_population_in_[POP_GROUP].tif** 每个像素
表示搜索半径内的总人数
此总体组POP_GROUP，按用户选择加权
衰减函数。单位：每像素人。

-  **中级/distance_weighted_population_all_groups.tif** 合计
种群，由适当的衰减函数加权。单位：
每像素人数。

-  **中级/urban_nature_supply_percapita_to_[POP_GROUP].tif** 城市
对人口群体的自然供应POP_GROUP。单位：平方米/平方米
人。

-  **中级/undersupplied_population_[POP_GROUP].tif** 每个像素
表示人口组 POP_GROUP 中的人口，即
经历城市自然赤字。单位：每像素人。

-  **中级/oversupplied_population_[POP_GROUP].tif** 每个像素
表示人口组 POP_GROUP 中的人口，即
体验城市自然盈余。单位：每像素人。

附录：数据源
======================

：ref：'土地利用/土地覆被 <lulc>`
---------------------------------

人口栅格

存在多个区域和全球数据集来估计人口
高分辨率下的尺寸和密度，例如：

- WorldPop全球人口数据：
https://www.worldpop.org/methods/populations/

- Meta/CIESIN全球人口密度数据：
https://dataforgood.facebook.com/dfg/tools/high-resolution-population-density-maps

- 欧洲100米人口数据：
https://www.eea.europa.eu/data-and-maps/data/population-density-disaggregated-with-corine-land-cover-2000-2

城市绿地数据
---------------------

存在多个区域和全球数据集，这些数据集（帮助）定义城市
性质，包括以下内容：

- 拉丁美洲城市：
https://www.nature.com/articles/s41597-022-01701-y

- 欧洲城市：https:// land.copernicus.eu/local/urban-atlas

- 全球数据：

- http://data.ess.tsinghua.edu.cn/
- https://www.openstreetmap.org/

（有关比较，请参阅：https://www.sciencedirect.com/science/article/abs/pii/S1618866722001819）

城市自然需求
-------------------

对于城市自然需求，没有固定的全球标准。一个常见的
建议值为 9m2，这经常被错误地记入 WHO
（见
https://www.researchgate.net/post/I-see-many-studies-citing-WHO-for-their-international-minimum-standard-for-green-space-9m2-per-capita-But-where-is-the-actual-study/4
以讨论此值）。提供需求概述的论文
价值观和围绕这些价值观的讨论包括 Liu et al. （2022）， Liu
等人（2021 年）和 Badiu 等人（2016 年）。

引用
==========

Andkjaer S.， Arvidsen J. 2015.户外休闲活动场所
范围界定审查。户外休闲与旅游杂志， *12*， 25-46.
https://doi.org/10.1016/j.jort.2015.10.001

巴迪乌， D.L.， Ioja， C.I.， Patroescu， M.， Breuste， J.， Artmann， M.， Nita，
M.R.， Gradinaru， S.R.， Hossu， C.A.， Onose， D.A. 2016.城市是绿色的吗
人均空间是实现城市可持续发展的重要目标
目标？罗马尼亚作为案例研究。生态指标*70*，53-66。
https://doi.org/10.1016/j.ecolind.2016.05.044

布拉特曼，GN，安德森，CB，伯曼，MG，科克伦，B.，德弗里斯，
S.， 佛兰德斯， J.， ...& Daily， G. C. 2019.自然与心理健康：一个
生态系统服务视角。科学进展， *5*\ （7）， eaax0903.
https://doi.org/10.1126/sciadv.aax0903

基勒， BL， 哈默尔， P.， 麦克菲尔森， T.， 哈曼， MH， 多纳休， ML，
梅扎·普拉多（Meza Prado），KA，...& Wood， S. A. 2019 年。社会生态和
技术因素缓和了城市自然的价值。自然界
可持续性， *2*\ （1）， 29-38.
https://doi.org/10.1038/s41893-018-0202-1

刘， H.， 雷姆， R.P.， 哈默尔， P.， 侬， H.， 任， H.， 2020.供应和
城市康乐服务需求评估及其启示
绿地规划——以广州为例.兰德斯。城市规划。203,
103898. https://doi.org/10.1016/j.landurbplan.2020.103898

Liu H., Hamel P., Tardieu L., Remme R.P., Han B., Ren H., 2022. A
geospatial model of nature-based recreation for urban planning: Case
study of Paris, France. Land Use Policy,
https://doi.org/10.1016/j.landusepol.2022.106107.

Mao L. and Nekorchuk D., 2013. Measuring spatial accessibility to health
care for populations with multiple transportation modes. Health & Place
24, 115–122. https://doi.org/10.1016/j.healthplace.2013.08.008

Remme, R. P., Frumkin, H., Guerry, A. D., King, A. C., Mandle, L.,
Sarabu, C., ... & Daily, G. C. 2021. An ecosystem service perspective on
urban nature, physical activity, and health. Proceedings of the National
Academy of Sciences, *118*\ (22), e2018472118.
https://doi.org/10.1073/pnas.2018472118

Roo, M. D., Kuypers, V. H. M., & Lenzholzer, S. 2011. *The green city
guidelines: techniques for a healthy liveable city*. The Green City.
http://library.wur.nl/WebQuery/wurpubs/fulltext/178666

邢 L.J， 刘 Y.F， 刘 X.J.， 2018.衡量空间差异
基于公园绿地的多模式方法的可达性
中国武汉的分类。应用地理学94,251-261。
https://doi.org/10.1016/j.apgeog.2018.03.014
