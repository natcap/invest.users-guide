.. _the-need-for:

***********************
The Need for a New Tool
***********************

Introduction
============

Ecosystems, if properly managed, yield a flow of services that are vital to humanity, including the production of goods (e.g., food), life support processes (e.g., water purification), and life fulfilling conditions (e.g., beauty, recreation opportunities), and the conservation of options (e.g., genetic diversity for future use). Despite its importance, this natural capital is poorly understood, scarcely monitored, and—in many cases—undergoing rapid degradation and depletion. To better align ecosystem conservation with economic forces, the Natural Capital Project is developing models that quantify and map the values of ecosystem services. The modeling suite is best suited for analyses of multiple services and multiple objectives. The current models, which require relatively little data input, can identify areas where investment may enhance human well-being and nature. We are continuing development of the models and will release new, updated versions as they become available.


Who should use InVEST?
======================

InVEST is designed to inform decisions about natural resource management. Essentially, it provides information about how changes in ecosystems are likely to lead to changes in the flows of benefits to people.  Decision-makers, from governments to non-profits to corporations, often manage lands and waters for multiple uses and inevitably must evaluate trade-offs among these uses. ; InVEST’s multi-service, modular design provides an effective tool for exploring the likely outcomes of alternative management and climate scenarios and for evaluating trade-offs among sectors and services. For example, government agencies could use InVEST to help determine how to manage lands, coasts, and marine areas to provide a desirable range of benefits to people or to help design permitting and mitigation programs that sustain nature’s benefits to society. Conservation organizations could use InVEST to better align their missions to protect biodiversity with activities that improve human livelihoods. Corporations, such as timber companies, renewable energy companies, and water utilities, could also use InVEST to decide how and where to invest in natural capital to ensure that their supply chains are preserved.

InVEST can help answer questions like:

+ Where do ecosystem services originate and where are they consumed?
+ How does a proposed forestry management plan affect timber yields, biodiversity, water quality and recreation?
+ What kinds of coastal management and fishery policies will yield the best returns for sustainable fisheries, shoreline protection and recreation?
+ Which parts of a watershed provide the greatest carbon sequestration, biodiversity, and tourism values?
+ Where would reforestation achieve the greatest downstream water quality benefits while maintaining or minimizing losses in water flows?
+ How will climate change and population growth impact ecosystem services and biodiversity?
+ What benefits does marine spatial planning provide to society in addition to food from fishing and aquaculture and secure locations for renewable energy facilities?


Introduction to InVEST
======================

InVEST is a tool for exploring how changes in ecosystems are likely to lead to changes in benefits that flow to people. 

InVEST uses a simple framework delineating “supply, service, and value.”   

"Supply" represents what benefits are potentially available from the ecosystem (ie. what the ecosystem structure and function can provide).  For example, this is the wave attenuation and subsequent reduction in erosion and flooding onshore provided by a particular location density of mangrove forest.  "Service" incorporates demand and thus uses information about beneficiaries of that service (e.g., where people live, important cultural sites, infrastructure, etc.). "Value" includes social preference and allows for the calculation of economic and social metrics (e.g., avoided damages from erosion and flooding, numbers of people affected).

The InVEST toolset described in this guide includes models for quantifying, mapping, and valuing the benefits provided by terrestrial, freshwater and marine systems.  We group models in InVEST into three primary categories: 1) supporting services, 2) final services, and 3) tools to facilitate ecosystem service analyses.  Supporting services underpin other ecosystem services, but do not directly provide benefits to people.  Final services provide direct benefits to people, and for our models we denote this distinction as Supporting Service/Supply: Final Service. 


Supporting Ecosystem Services:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+   Habitat Quality

+   Habitat Risk Assessment

+   Marine Water Quality


Final Ecosystem Services:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+	Carbon Storage and Sequestration: Climate Regulation

+	Water Yield: Reservoir Hydropower Production

+	Nutrient Retention: Water Purification

+	Sediment Retention: Avoided Dredging and Water Purification

+   Pollinator Abundance: Crop Pollination

+	Unobstructed Views: Scenic Quality Provision

+	Visitation: Recreation and Tourism 

+	Wave Attenuation & Erosion Reduction: Coastal Protection (*only in ArcGIS version)

+	Blue Carbon Storage and Sequestration: Climate Regulation (*coming soon)

+	Managed Timber Production

+ 	Wave Energy Production

+	Offshore Wind Energy Production

+	Marine Finfish Aquacultural Production

+	Marine Fisheries Production (*coming soon)


Tools to Facilitate Ecosystem Service Analyses:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+   Overlap Analysis

+   Coastal Exposure and Vulnerability



InVEST is most effectively used within a decision-making process that starts with a series of stakeholder consultations (illustrated in Figure 1). Through discussion, questions of interest to policy makers, communities and conservation groups are identified. These questions may concern service delivery on a landscape today and how these services may be affected by new programs, policies, and conditions in the future. For questions regarding the future, stakeholders develop “scenarios” to explore the consequences of expected changes on natural resources. These scenarios typically include a map of future land use and land cover or, for the marine models, a map of future coastal and ocean uses and coastal/marine habitats.

.. figure:: ./the_need_for_images/applying_invest.jpg
   :alt: schematic
   :align: center

   Schematic of the decision-making process in which InVEST is embedded. Stakeholders create scenarios that are assessed for ecosystem service value by biophysical and economic models that produce several types of outputs.

Following stakeholder consultations and scenario development, InVEST can estimate the amount and value of ecosystem services that are provided on the current landscape or under future scenarios. InVEST models are spatially-explicit, using maps as information sources and producing maps as outputs. InVEST returns results in either biophysical terms (e.g., tons of carbon sequestered) or economic terms (e.g., net present value of that sequestered carbon). The spatial resolution of analyses is also flexible, allowing users to address questions at the local, regional or global scale. InVEST results can be shared with the stakeholders and decision-makers who created the scenarios to inform upcoming decisions. Using InVEST in an iterative process, these stakeholders may choose to create new scenarios based on the information revealed by the models until suitable solutions for management action are identified.



A work in progress
==================

InVEST is a free of cost software product licensed under the BSD open source license.

The development of InVEST is an ongoing effort of the Natural Capital Project. We release updated versions of the toolkit approximately every three months that can include updated science, performance and feature enhancements, bug fixes, and/or new models.  As a historical note, the original InVEST models were built within ArcGIS but now almost all models exist in a standalone form directly launchable from the Windows Operating system with no other software dependencies.  The exception is the "Wave Attenuation & Erosion Reduction: Coastal Protection" model which exists as an ArcGIS toolbox; this tool will be converted to the standalone platform.

A note on InVEST versioning: Integer changes will reflect major changes like the transition from 2.6.0 to 3.0.0 indicates a transition from the Arc-GIS modules to standalone version.  An increment in the digit after the primary decimal indicates major new features (e.g, the addition of a new model) or major revisions. The third decimal reflects minor feature revisions or bug fixes with no new functionality. 


This guide
==========

This guide will help you understand the basics of the InVEST models and start using them. The next chapter leads you through the installation process and provides general information about the tool and interface.

The remaining chapters present the ecosystem service models.  Each chapter:

+ briefly introduces a service and suggests the possible uses for InVEST results;

+ explains intuitively how the model works, including important simplifications, assumptions, and limitations;

+ describes the data needed to run the model, which is crucial because the meaning and value of InVEST results depend on the input data;

+ provides step-by-step instructions for how to input data and interact with the tool;

+ offers guidance on interpreting InVEST results;

+ includes an appendix of information on relevant data sources and data preparation advice (this section is variable among chapters, and will improve over time from user input).

This guide does not include detailed theoretical discussions of the scientific foundation of the models.  For the terrestrial and freshwater models, these can be found in the new book *Natural Capital: The Theory & Practice of Mapping Ecosystem Services* (Oxford University Press).


