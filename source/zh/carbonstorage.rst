.. _carbonstorage:

********************************
碳储存和封存
********************************

总结
=======

陆地生态系统储存的碳比大气更多，对影响二氧化碳驱动的气候变化至关重要。InVEST碳储存和封存模型使用土地使用地图以及四个碳库(地上生物量、地下生物量、土壤和死有机质)的存量来估算景观中当前储存的碳量或随着时间推移的碳封存量。或者，可使用封存碳的市场或社会价值、其年变化率和折价率来估计这种生态系统服务对社会的价值。该模型的局限性包括过于简化的碳循环，假设碳封存随时间的线性变化，以及可能不准确的折价率。

.. note:: 这个碳模型非常简单。它只需要四个碳库和一张土地覆盖图，就能将这些碳库值映射到土地覆盖图，但不体现任何生物物理性质的变化以及时态性，如树木生长、土壤化学性质变化或随时间变化的温度或降水影响。如果您需要模拟的内容较土地覆盖图的静态碳库更复杂，则需要使用不同的碳模型。

介绍
============

生态系统通过增加和消除大气中的CO\ :sub:`2` 等温室气体(GHGs)来调节地球气候。森林、草原、泥炭沼泽和其他陆地生态系统共同“储存”的碳比大气多得多(Lal 2002)。通过将这些碳储存在木材、其他生物量和土壤中，生态系统将CO\ :sub:`2` 排除在大气之外，从而导致气候变化。除了储存碳，许多系统还随着时间的推移继续在植物和土壤中积累碳，从而每年“隔离”额外的碳。用火灾、疾病或植被转换(例如，土地利用/土地覆盖(LULC)转换)干扰这些系统会释放大量CO\ :sub:`2`。其他管理变革，如森林恢复或替代农业做法，可能导致大量CO\ :sub:`2` 的储存。因此，我们管理陆地生态系统的方式对调节气候至关重要。

陆地碳封存和储存可能是所有生态系统服务中最被广泛认可的(Stern 2007, IPCC 2006, Canadell和Raupach 2008, Capoor和Ambrosi 2008, Hamilton等人2008,Pagiola 2008)。封存一吨碳的社会价值等于不将一吨碳释放到大气中所避免的社会损害(Tol 2005, Stern 2007)。社会成本的计算是复杂和有争议的(见Weitzman 2007和Nordhaus 2007b)，但产生的价值估计从每公吨释放到大气中的CO\ :sub:`2` 的9.55美元到84.55美元不等(Nordhaus 2007a和Stern 2007)。

管理碳储存和封存的景观需要了解碳储存的数量和位置，随时间推移封存或流失的碳量，以及土地使用的变化如何影响随时间推移储存和封存的碳量。由于土地管理者必须在保护、收割或开发的地点中进行选择，绘制碳储存和封存地图是支持影响这些生态系统服务的决策的理想选择。

这样的地图可以支持政府、非政府组织和企业的一系列决策。例如，政府可以有机会利用它们来确定获得因砍伐森林和退化而减少(碳)排放(REDD)的分数。了解景观的哪些部分储存了最多的碳，将有助于政府有效地将激励措施针对土地所有者，以换取森林保护。此外，环保非政府组织可能希望投资于生物多样性和碳封存高度重叠的领域(Nelson et al. 2008)。木材公司也可能希望最大化其从木材生产和REDD碳信用分的回报(Plantinga和Birdsey 1994年)

模型
=========

一块土地上的碳储量很大程度上取决于四个碳库的大小:地上生物量、地下生物量、土壤和死有机物。InVEST碳储存和封存模型根据用户提供的土地利用地图和分类汇总这些池中储存的碳量。地上生物量包括土壤以上的所有植物活性物质(如树皮、树干、树枝、树叶)。地下生物量包括地上生物量的活根系。土壤有机质是土壤的有机成分，是最大的陆地碳库。死去的有机物包括垃圾以及横着和立着的枯木。
该模型利用LULC分类图和碳库中储存的碳量，估计了一块土地随时间推移储存的净碳量和剩余库存中封存的碳的市场价值。该模型的局限性包括碳循环过于简化，假设碳封存随时间呈线性变化，以及可能不准确的折价率。对碳封存很重要的生物物理条件，如光合作用速率和活跃土壤生物的存在，也不包括在模型中。

工作原理
------------

该模型将碳储存密度映射到可包括森林、牧场或农田等类别的LULC栅格。该模型将结果汇总为存储、封存和价值的栅格输出以及合计。

对于每一种LULC类型，该模型需要对上述四个基本库中至少一个的碳量作出估计，单位为每公顷公吨(t/ha)。如果您拥有多个库的数据，那么建模结果将更加完整。该模型只需将这些估计值应用到LULC图中，就可以生成包含的碳库中的碳储量图。

如果你同时提供当前和未来的LULC图，那么就可以计算出碳储量随时间的净变化(封存和损失)及其社会价值。为了估计这种碳封存随时间的变化，只需将模型应用于当前景观和未来景观的预测，并逐像素计算存储的差异。如果有多个未来场景可用，则可以比较当前和每个备选未来场景之间的差异。

此外，如果您提供REDD场景的土地覆被地图，该模型将把该栅格作为额外的未来场景，计算存储和封存，并汇总结果。

该模型的输出以每像素的碳公吨(与兆克相同)表示，如果需要，还以每像素的货币单位表示固碳值。如果您对用货币单位表示碳封存感兴趣，我们强烈建议使用碳封存的社会价值。封存一吨碳的社会价值是通过减少一吨碳排放到大气中而避免的社会损害。

该估值模型将封存(不是储存)的经济价值作为封存碳量、每单位碳的货币价值、货币折价率以及封存碳价值随时间的变化的函数进行估计。因此，只有在有未来情景的情况下，才能在碳模型中进行估值。估值适用于封存，而不是储存，因为市场价格只与碳封存有关。折价率是乘数，随着时间的推移，通常会降低碳封存的价值。第一种折价，即金融折价的标准经济程序，反映了这样一个事实:由于不确定性和假定的经济通货膨胀，人们通常更看重眼前的利益而不是未来的利益。第二个折价率随时间调整碳封存的社会价值。随着碳排放对预期的气候变化相关损害的影响的变化，该值将发生变化。如果我们期望今天吸收的碳比未来吸收的碳对减缓气候变化的影响更大，那么第二个折价率应该是正的。另一方面，如果我们期望今天吸收的碳对减缓气候变化的影响小于未来吸收的碳，那么第二个折价率应该是负的。

特定地块*x*的碳封存值随时间的变化为:

.. math:: value\_seq_x=V\frac{s_x}{q-p}\sum^{q-p-1}_{t=0}\frac{1}{\left(1+\frac{r}{100}\right)^t\left(1+\frac{c}{100}\right)^t}
   :label: 碳价值

式中

* :math:`V` 是每公吨碳的价格

* :math:`s_x` 是地块上的碳量，单位为公吨 :math:`x`

* :math:`q` 是未来的年份

* :math:`p` 是当前的年份

* :math:`r` 是碳价格的年度市场折价率

* :math:`c` 是碳价格的年变化率


REDD 场景分析 
----------------------

碳模型可以根据减少森林退化和森林砍伐排放(REDD)或REDD+框架进行情景分析。REDD是一项减排计划，根据该计划，减少森林砍伐排放的国家可以获得经济补偿。REDD+以原有的REDD框架为基础，还纳入了保护、可持续森林管理和增加现有碳储量。

要执行REDD场景分析，该模型需要三个LULC映射:一个用于当前场景，一个用于未来基线场景，一个用于REDD策略下的未来场景。未来基线情景用于计算可与REDD情景进行比较的排放参考水平。根据所需REDD框架的具体情况，可以通过许多不同的方式生成基线场景;例如，它可以基于历史森林砍伐率或预测。REDD政策情景图反映了在防止森林砍伐和加强碳封存的REDD政策下未来的最低土地利用面积。

基于这三个针对当前、基线和REDD政策情景的LULC图，碳生物物理模型生成了三个LULC图的总碳储量栅格，以及未来和REDD情景的两个封存栅格。

限制和简化
===============================

该模型简化了碳循环，这使得它可以在相对较少的信息下运行，但也导致了重要的限制。例如，该模型假设景观中的任何一种LULC类型都不会随着时间的推移而增加或减少碳。相反，假设所有的LULC类型都处于某个固定的存储级别，等于该LULC类型中测量的存储级别的平均值。根据这一假设，随着时间的推移，碳储量的唯一变化是由于从一种LULC类型到另一种类型的变化。因此，随着时间的推移，任何不改变其LULC类型的像素的封存值都将为0。事实上，许多地区正在从过去的土地使用中恢复过来，或正在进行自然继承。这个问题可以通过将LULC类型划分为年龄类(本质上是添加更多的LULC类型)来解决，例如森林的三个年龄。然后，地块可以在场景中从一个年龄层移动到另一个年龄层，并因此改变其碳储量值。

第二个限制是，由于该模型依赖于对每种LULC类型的碳储量估算，因此其结果仅与使用的LULC分类和提供的碳库值一样详细和可靠。碳储量在不同的LULC类型(例如，热带森林与开放林地)之间存在明显的差异，但在一个LULC类型中也常常存在显著的差异。例如，“热带湿润森林”内的碳储量受到温度、海拔、降雨和重大扰动(例如，森林火灾)以来的年数的影响。通过使用LULC分类系统和相关碳库表，可以部分恢复粗略定义的LULC类型与相关环境和管理变量之间的碳储量变化。例如，森林LULC类型可以根据海拔、气候带或重大扰动后的时间间隔进行分层。当然，这种更详细的方法需要数据描述每个更精细的LULC类的每个碳库中存储的碳量。

该模型的另一个局限性是它不能捕获从一个碳库转移到另一个碳库的碳。例如，如果森林中的树木因疾病死亡，储存在地上生物量中的大部分碳就会变成储存在其他(死亡的)有机物质中的碳。此外，当树木从森林中采伐时，树枝、茎、树皮等被遗留在地上。该模型假设木材中的碳“立即”进入大气。

最后，虽然大多数碳封存遵循非线性路径，即碳封存在最初几年以较高的速率封存，在随后几年以较低的速率封存，但该模型对碳封存的估值假设碳封存随时间的线性变化。由于折价率的存在，假设变化速率恒定往往会低估封存碳的价值，因为非线性封存路径比线性封存路径更具社会价值(图1)。

.. figure:: ../en/carbon_storage/carbon_envelope.jpg
   :align: center
   :figwidth: 500px

*图1:模型假设碳储量呈线性变化(实线)，而到达T年碳储量水平的实际路径可能是非线性的(如虚线)。在这种情况下，“t”表示当前景观的年份，“T”表示未来景观的年份。在正折现情况下，建模路径(实线)的值比实际路径的值小。因此，如果固碳路径趋向于虚线，该模型将低估固碳价值*

数据需求
==========

.. note:: 所有空间输入必须在相同的投影坐标系和线性米单位。

.. note:: 如果要包括未来的 LULC 和/或 REDD LULC，则这些栅格的像素大小必须与当前 LULC 栅格*完全相同*。

.. note:: 所有的碳数据应该是元素碳，而不是CO\ :sub:`2`。

- :investspec:`carbon lulc_cur_path`

- :investspec:`carbon lulc_cur_year`

- :investspec:`carbon calc_sequestration`

- :investspec:`carbon lulc_fut_path`

- :investspec:`carbon lulc_fut_year`

- :investspec:`carbon do_redd`

- :investspec:`carbon lulc_redd_path`

- :investspec:`carbon carbon_pools_path` 必须为所有的碳库提供值，对于所有的LULC类，不可以为空。如果关于某些碳库的信息不可用，则可以从其他碳库中估计碳库，或者通过使碳库的所有值都等于0而忽略碳库。
   列:

   - :investspec:`carbon carbon_pools_path.columns.lucode`
   - :investspec:`carbon carbon_pools_path.columns.c_above`
   - :investspec:`carbon carbon_pools_path.columns.c_below`
   - :investspec:`carbon carbon_pools_path.columns.c_soil`
   - :investspec:`carbon carbon_pools_path.columns.c_dead`

   *例:* 假设研究5个LULC类型。第1类(森林)在所有库中含有最多的碳。在这个例子中，地上和地下生物量中储存的碳在不同的土地利用类别中差异很大，但土壤中储存的碳变化不太明显。价值单位为公吨/公顷(t/ha)。

   ====== ================== ======= ======= ====== ======
   lucode LULC_name          C_above C_below C_soil C_dead
   ====== ================== ======= ======= ====== ======
   1      Forest              140     70      35     12
   2      Coffee              65      40      25     6
   3      Pasture/grass       15      35      30     4
   4      Shrub/undergrowth   30      30      30     13
   5      Open/urban          5       5       15     2
   ====== ================== ======= ======= ====== ======

- :investspec:`carbon do_valuation`

- :investspec:`carbon price_per_metric_ton_of_c` 这是:math:`V` 在等式:eq:`carbon_value`。以货币(任何货币)表示的每公吨元素碳的价格(不是CO\ :sub:`2`)。对于有兴趣估算碳封存的总价值的应用，我们建议基于每额外释放一吨碳所带来的破坏成本估算价值——碳的社会成本(SCC)。Stern (2007)， Tol(2009)和Nordhaus (2007a)提出了SCC的估计。例如，我们从Tol(2009)中得到的两个SCC估算值分别是66美元和130美元(以2010年美元计算)(Polasky等人，2010年)。

- :investspec:`carbon discount_rate`。这是方程:eq:`carbon_value`中的:math:`r`。其中一个默认值是每年7%，这是美国政府推荐的环境项目成本效益评估的市场折价率之一。然而，这一比率将取决于被评估的国家和景观，并应根据当地的要求进行选择。在对与气候变化相关的动力学建模时，使用较低的折价率是有哲学依据的，用户可以考虑使用这种方法。如果利率设置为0%，那么货币价值不折价。

- :investspec:`carbon rate_change` 这是方程:eq:`carbon_value`中的:math:`c`。随着排放对预期的气候变化相关损害的影响随着时间的推移而变化，这将调整封存碳的价值。

  将这一比率设置大于0%意味着未来封存的碳的社会价值小于现在封存的碳的价值。人们普遍认为，需要立即减少温室气体排放，以避免超过温室气体大气浓度阈值，从而导致到2105年全球平均气温升高3摄氏度或更高。一些人认为，这样的温度变化将导致全球经济的重大破坏(Stern et al. 2006)。因此，从现在起许多年后发生的任何温室气体排放减少可能对是否通过这一关键浓度阈值都没有影响。如果是这样的话，在遥远的未来，碳封存将是相对没有价值的，而大于零的碳折价率是有保证的。


解释结果
==================== 

* **[Workspace]** folder:

	* **Parameter log**: 每当模型运行时，将在工作区中创建一个文本(.txt)文件。该文件将列出该运行的参数值和输出消息，并将根据服务、日期和时间命名。当与NatCap联系关于模型运行中的错误时，请包括参数日志。

	* **report_[Suffix].html:** 该文件给出模型计算的所有数据的摘要。它还包括模型生成的所有其他输出文件的描述，因此它是开始探索和理解模型结果的好地方。因为这是一个HTML文件，它可以用任何浏览器打开。

	* **tot_c_cur_[Suffix].tif/tot_c_fut_[Suffix].tif/tot_c_redd_[Suffix].tif**: 栅格显示当前、未来和REDD方案中每个像素中储存的碳量。它是生物物理表提供的所有碳库的总和。单位是公吨每像素。

	* **delta_cur_fut_[Suffix].tif**/**delta_cur_redd_[Suffix].tif**: 栅格显示未来/REDD景观与当前景观之间的碳储存差异。数值以公吨/像素为单位。在这个映射中，有些值可能是负数，有些可能是正数。正值表示封存的碳，负值表示流失的碳。

	* **npv_fut_[Suffix].tif**/**npv_redd_[Suffix].tif**:** 栅格显示当前和未来/REDD景观日期之间封存的碳的经济价值。单位是每像素的货币。
* **[Workspace]\\intermediate_outputs** folder:

	* **c_above_[Suffix].tif**:地上碳值的栅格，从碳库表映射到LULC。单位是公吨每像素。
	* **c_below_[Suffix].tif**: 地下碳值的栅格，从碳库表映射到LULC。单位是公吨每像素。
	* **c_dead_[Suffix].tif**: 死物碳值的栅格，从碳库表映射到LULC。单位是公吨每像素。
	* **c_soil_[Suffix].tif**: 土壤碳值的栅格，从碳库表映射到LULC。单位是公吨每像素。
	* **_tmp_work_tokens**: 此目录存储内部使用的元数据，以避免重新计算。这里没有存储模型结果。

附录: 数据源
======================

:ref:`Land Use/Land Cover <lulc>`
---------------------------------

:ref:`Carbon Pools <carbon_pools>`
----------------------------------

碳价格和折价率
-------------------------------

最近的估计表明，以2010年美元计算，碳的社会成本(SCC)，或与额外释放到大气中的一吨碳相关的边际损害，从每公吨碳32美元(Nordhaus 2007a)到每公吨碳326美元(Stern 2007)不等。这种损失的价值也可以被认为是避免释放的金钱利益。Tol(2009)对SCC估值进行了全面调查，报告了按2010年美元计算的每公吨66美元和130美元的中值(由于对时间折价的假设不同，值有所不同)。其他估计可在Murphy等人(2004)、Stainforth等人(2005)和Hope(2006)中找到。

衡量一吨碳排放成本的另一种方法是将成本设为封存该吨碳的最低成本。目前的次优选择是捕获和存储公用事业工厂排放的C。根据Socolow(2005)和Socolow和Pacala(2007)的研究，该技术捕获和储存每公吨的成本约为100美元。

最后，虽然我们不推荐这种方法，但可以用市场价格来设定封存碳的价格。我们不建议使用市场价格，因为它们通常只适用于“额外的”碳封存;削减高于或超过一些基线削减率。此外，碳市场的碳信用价值很大程度上是各种碳信用市场规则和法规的功能，并不一定反映封存一吨碳给社会带来的好处。因此，正确使用市场价格将需要估算利息领域的基准利率，绘制额外的封存，然后根据市场规则和规章确定哪些额外封存有资格获得信贷。


我们对未来碳封存支付的价值进行了折价，以反映社会对尽早支付的偏好。The U.S. Office of Management and Budget (OMB, 1992)建议美国项目的年市场折价率为7%。世界各地的折扣率各不相同。加拿大和新西兰为他们的项目推荐10% (Abusah和de Bruyn 2007)。最好是寻找您所在国家/地区推荐的折价率。

一些经济学家认为，在进行气候变化分析时，7%到12%的市场或消费折价率过高。由于气候变化有可能严重破坏未来的经济，社会倾向于以牺牲未来的气候稳定和后代的经济机会为代价来消费今天的消费，被一些人认为是不道德的(Cline 1992, Stern 2007)。根据这一论点，对气候变化对社会的影响的分析和旨在减少气候变化的政策应采用低折价率，以鼓励更多地减少温室气体排放，从而补偿后代可能遭受的严重损害(例如，Stern (2007年)的r = 0.014)。一些国家最近的政府政策支持对某些长期项目使用非常低的折价率(Abusah和de Bruyn, 2007年)。

碳折价率反映了当前碳封存比未来碳封存对气候的更大影响，在Adams等人(1999)、Plantinga等人(1999)、Feng 2005和Nelson等人(2008)中进行了讨论。

参考文献
==========

Abusah, Sam and Bruyn, Clinton de. 2007. Getting Auckland on Track: Public Transport and New Zealand's Economic. Ministry of Economic Development Working Paper. Accessed at <http://s3.amazonaws.com/zanran_storage/www.med.govt.nz/ContentPages/4013253.pdf>.

Adams, DM, RJ Alig, BA McCarl, et al. 1999. Minimum cost strategies for sequestering carbon in forests. Land Econ 75: 360-374.

Anderson, JR, EE Hardy, JT Roach, RE Witmer. A Land Use and Land Cover Classification System for Use with Remote Sensor Data. Washington, DC: United States Government 	Printing Office; 1976. Geological Survey Professional Paper 964.

Antle, JM, and B. Diagana. 2003. Creating Incentives for the Adoption of Sustainable Agricultural Practices in Developing Countries: The Role of Soil Carbon Sequestration.	American Journal of Agricultural Economics 85:1178-1184.

Baer, SG, DJ Kitchen, JM Blair, and CW Rice. 2002. Changes in Ecosystem Structure and Function along a Chronosequence of Restored Grasslands. Ecological Applications 12:1688-1701.

Bernoux, M., MDS Carvalho, B. Volkoff, and CC Cerri. 2002. Brazil's soil carbon stocks. Soil Science Society of America Journal 66:888-896.

Brown, SL, PE Schroeder and JS Kern. Spatial distribution of biomass in forests of the eastern	USA.Forest Ecology and Management 123 (1999) 81-90.

Brown, S. 2002. Measuring carbon in forests: current status and future challenges. Environmental Pollution 116:363-372.

Brown, S. Estimating Biomass and Biomass Change of Tropical Forests: a Primer. FAO Forestry Department; 1997. Report for FAO Forestry Paper 134.

Brown, S. and PE Schroeder. 1999. Spatial patterns of aboveground production and mortality of woody biomass for eastern US forests. Ecological Applications 9:968-980.

Cairns, MA, PK Haggerty, R. Alvarez, BHJ De Jong, and I. Olmsted. 2000. Tropical Mexico's recent land-use change: A region's contribution to the global carbon cycle. Ecological Applications 10:1426-1441.

Cairns, MA, S. Brown, EH Helmer, and GA Baumgardner. 1997. Root biomass allocation in the world's upland forests. Oecologia 111:1-11.

Canadell, JG and MR Raupach. 2008. Managing Forests for Climate Change Mitigation. Science 320:1456-1457.

Cline, WR. 1992. The economics of global warming. Instuitute for International Economics, Washington, D.C.

Coomes, DA, RB Allen, NA Scott, C. Goulding, and P. Beets. 2002. Designing systems to monitor carbon stocks in forests and shrublands. Forest Ecology and Management 164:89-108.

Conte, MN and MJ Kotchen. 2010. Explaining the price of voluntary carbon offsets. Climate Change Economics 1 (2):93-111.

Capoor, K., and P. Ambrosi. State and Trends of the Carbon Market 2008. Washington, D.C.: World Bank Institute, 2008 May.

Delaney, M., S. Brown, AE Lugo, A. Torres-Lezama, and NB Quintero. 1998. The quantity and turnover of dead wood in permanent forest plots in six life zones of Venezuela. Biotropica 30:2-11.

Detwiler, RP. 1986. Land Use Change and the Global Carbon Cycle: The Role of Tropical Soils. Biogeochemistry 2:67-93.

Edinburgh Centre for Carbon Management. The Establishing Mechanisms for Payments for Carbon Environmental Services in the Eastern Arc Mountains, Tanzania; 2007 May 2007.

Fargione, J., J. Hill, D. Tilman, S. Polasky, and P. Hawthorne. 2008. Land Clearing and the Biofuel Carbon Debt. Science 319:1235-1238.

Feng, H. 2005. The dynamics of carbon sequestration and alternative carbon accounting, with an application to the upper Mississippi River Basin. Ecological Economics 54:23-35.

Gaston, G., S. Brown, M. Lorenzini, and KD Singh. 1998. State and change in carbon pools in the forests of tropical Africa. Global Change Biology 4:97-114.

Glenday, J. 2006. Carbon storage and emissions offset potential in an East African tropical rainforest. Forest Ecology and Management 235:72-83.

Grace, J., J. San Jose, P. Meir, HS Miranda, and RA Montes. 2006. Productivity and carbon fluxes of tropical savannas. Journal of Biogeography 33:387-400.

Gibbs, HK, S Brown, JO Niles, and JA Foley. 2007. Monitoring and estimating tropical forest carbon stocks: making REDD a reality. Environmental Research Letters 2:045023.

Hamilton, K., M Sjardin, T Marcello, and G Xu. Forging a Frontier: State of the Voluntary Carbon Markets 2008. Washington, D.C.: Ecosystem Marketplace and New Carbon Finance; 2008.

Hope, CW. 2006. The social cost of carbon: what does it actually depend on? Climate Policy 6: 565--572

Houghton, RA. 2005. Tropical deforestation as a source of greenhouse gas emissions. In: Tropical Deforestation and Climate Change, Moutinho and Schwartzman [eds.]. Instituto de Pesquisa Ambiental da Amazonia and Environmental Defense, Belem, Brazil.

Houghton, RA, and JL Hackler. 2006. Emissions of carbon from land use change in sub-Saharan Africa. Journal of Geophysical Research 111.

The Intergovernmental Panel on Climate Change (IPCC). 2006. 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use. Prepared by the National Greenhouse Gas Inventories Programme, Eggleston, HS, L. Buendia, K. Miwa, T. Ngara, and K. Tanabe (eds). Institute for Global Environmental Strategies (IGES), Hayama, Japan. <https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html>.

Jenny, H. 1980. The Soil Resource. Springer, New York.

Lal, R. 2004. Soil Carbon Sequestration Impacts on Global Climate Change and Food Security. Science 304:1623-1627.

Mackey, B, Keith H, Berry S.L, Lindenmayer DB. Green carbon: the role of natural forests in carbon storage. Part 1, A green carbon account of Australia's Southeastern Eucalypt forest, and policy implications. Canberra, Australia: ANU E Press, 2008.

Makundi, WR. 2001. Carbon mitigation potential and costs in the forest sector in Tanzania. Mitigation and Adaptation Strategies for Global Change 6:335-353.

Malhi, Y., D. Wood, TR Baker, et al. 2006. The regional variation of aboveground live biomass in old-growth Amazonian forests. Global Change Biology 12:1107-1138.

Malimbwi, RE, B. Solberg, and E. Luoga. 1994. Estimation of biomass and volume in miombo woodland at Kitungalo Forest Reserve Tanzania. Journal of Tropical Forest Science 7:230-242.

McLauchlan, KK., SE Hobbie, and WM Post. 2006. Conversion From Agriculture To Grassland Builds Soil Organic Matter On Decadal Timescales. Ecological Applications 16:143-153.

Mollicone D., F. Achard, S. Federici, H. Eva, G. Grassi, A. Belward, F. Raes, G. Seufert, H. Stibig, G. Matteucci, and E. Schulze. 2007. An incentive mechanism for reducing emissions from conversion of intact and non-intact forests. Climatic Change 83:477-493.

Munishi, PKT and TH Shear. 2004. Carbon Storage in Afromontane Rain Forests of the Eastern Arc Mountains of Tanzania: their Net Contribution to Atmospheric Carbon. Journal of Tropical Forest Science 16:78-93.

Murphy, JM et al. 2004. Quantification of modelling uncertainties in a large ensemble of climate change simulations. Nature 430, 768-772.

Murray, B., B. Sohngen, and M. Ross. 2007. Economic consequences of consideration of permanence, leakage and additionality for soil carbon sequestration projects. Climatic Change 80:127-143.

Nascimento, HEM, and WF Laurance. 2002. Total aboveground biomass in central Amazonian rainforests: a landscape-scale study. Forest Ecology and Management 168:311-321.

Nelson, E., G. Mendoza, J. Regetz, S. Polasky, H. Tallis, D. Cameron, K. Chan, G. Daily, J. Goldstein, P. Kareiva, E. Lonsdorf, R. Naidoo, TH Ricketts, and R. Shaw. 2009. Modeling multiple ecosystem services, biodiversity conservation, commodity production, and tradeoffs at landscape scales. Frontiers in Ecology and the Environment.

Nordhaus, W. 2007a. Critical Assumptions in the Stern Review on Climate Change. Science 317 (5835): 201--202.

Nordhaus, W. 2007b. A Review of the Stern Review on the Economics of Global Warming. Journal of Economic Literature 45: 686-702.

Pagiola, S. 2008. Payments for environmental services in Costa Rica. Ecological Economics 65 (4): 712-724.

Plantinga, AJ, and RA Birdsey. 1994. Optimal Forest Stand Management When Benefits are Derived from Carbon. Natural Resource Modeling 8(4): 373-387.

Polasky, S, E Nelson, D Pennington, and K Johnson. 2010. The Impact of Land-Use Change on Ecosystem Services, Biodiversity and Returns to Landowners: A Case Study in the State of Minnesota. Environmental and Resource Economics 48:219-242

Post, WM, WR Emanuel, PJ Zinke, and AG Stangenberger. 1982. Soil carbon pools and world life zones. Nature 298:156-159.

Post, WM, KC Kwon. 2000. Soil carbon sequestration and land-use change: processes and potential. Global Change Biology 6:317-327.

Raich, JW, AE Russell, K. Kitayama, WJ Parton, and PM Vitousek. 2006. Temperature influences carbon accumulation in moist tropical forests. Ecology 87:76-87.

Ruesch A, and HK Gibbs. 2008. New IPCC tier-1 global biomass carbon map for the year 2000. Available:https://cdiac.ess-dive.lbl.gov/epubs/ndp/global_carbon/carbon_documentation.html.

Schuman, GE, HH Janzen, and JE Herrick. 2002. Soil carbon dynamics and potential carbon sequestration by rangelands. Environmental Pollution, 116:391-396.

Sedjo, RA and B. Sohngen. Carbon Credits for Avoided Deforestation. Washington, DC: Resources for the Future; 2007 October 2007. Report for RFF DP 07-47.

Silver, WL, R. Ostertag, and AE Lugo. 2000. The potential for carbon sequestration through reforestation of abandoned tropical agricultural and pasture lands. Restoration Ecology 8:394-407.

Socolow, RH. 2005. Can We Bury Global Warming? Scientific American 293: 49-55.

Socolow, RH and SW Pacala. 2006. A Plan to Keep Carbon in Check. Scientific American 295: 50-57.

Sohngen, Brent, RH Beach, and Kenneth Andrasko. 2008. Avoided Deforestation as a Greenhouse Gas Mitigation Tool: Economic Issues. Journal of Environmental Quality 37: 1368-1375.

Stainforth, DA et al., 2005. Uncertainty in predictions of the climate response to rising levels of greenhouse gases. Nature 433, 403--406.

Stern, N. 2007. The Economics of Climate Change: The Stern Review. Cambridge and New York: Cambridge University Press.

Tiessen, H., C. Feller, EVSB Sampaio, and P. Garin. 1998. Carbon Sequestration and Turnover in Semiarid Savannas and Dry Forest. Climatic Change 40:105-117.

Tilman, D., J. Hill, and C. Lehman. 2006. Carbon-Negative Biofuels from Low-Input High-Diversity Grassland Biomass. Science 314:1598-1600.

Tol, RSJ. 2005. The marginal damage costs of carbon dioxide emissions: an assessment of the uncertainties. Energy Policy 33:2064-2074.

Tol, RSJ. 2009. The Economic Effects of Climate Change.Journal of Economic Perspectives 23:29-51.

USOMB (US Office of Management and Budget). 1992. Guidelines and Discount Rates for Benefit-Cost Analysis of Federal Programs Circular No. A-94 (Revised). Transmittal Memo No. 64. Washington DC: US Office of Management and Budget.

Vagen, TG, R Lal, and BR Singh. 2005. Soil carbon sequestration in sub-Saharan Africa: A review. Land Degradation & Development 16:53-71.

Weitzman, ML. 2007. A review of the Stern Review on the Economics of Climate Change. Journal of Economic Literature 45:703-724.

Zhang, Q, and CO Justice. 2001. Carbon Emissions and Sequestration Potential of Central African Ecosystems. AMBIO 30:351-355.
