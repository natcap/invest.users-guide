.. primer

.. _scenariogenerator:

.. |addbutt| image:: ./shared_images/addbutt.png
  :alt: add
	 :align: middle 
	 :height: 15px

.. |toolbox| image:: ./shared_images/toolbox.jpg
  :alt: toolbox
	 :align: middle 
	 :height: 15px

******************
Scenario Hub
******************

Introduction
============
The Scenario Hub (scenariohub.net) is a web-based portal that aims to:

1.	Provide standard questionnaire to collect information and generate growth estimates (under development) from experts and stakeholders. 

2.	Help users document scenarios and prepare input data for Scenario Generator.

3.	Encourage information sharing on different projects and scenarios, and provide a case pool for Scenario Generator users.

We suggest users refer to the Scenario Generator user’s guide for the modeling part and the use of each estimate.


How it works
============

Registration
------------
Scenario Hub requires a user account to access its full function. Use the Auth Code / registration code **NATCAP2015** to create a new account. After you verified your email address, you can sign in with your account and create scenarios.

View Projects
----------------
By click on project names, you can view other people's projects. Click on the scenario name to expand the associated scenario profile.

Create A Project
----------------

Enter the name, time horizon, and general description to create a new project. You can also choose whether your project is visible to other users or not. Once a project created, you won't be able to edit the project information.

Most of the inputs in this section are not required, nor will they be used to build up your Scenario Generator input files. However, we do suggest that you post relevant information here, so that you can keep a better record of your project, and other users in the community will benefit from your case as well. 
 
Create Scenarios
----------------
You can create and edit your scenarios in your own project page. Components required to build you scenario profile include:

A. General Information:
^^^^^^^^^^^^^^^^^^^^^^^^

1. **Scenarios:** The names of scenarios you will develop for the project. You need to enter a scenario name here to expand the estimates sections (discussed later).

2. **Scenario Description (optional):** We suggest you put the detailed storyline here, which will help others (and yourself) understand the assumptions and reasons behind your estimates.


B.	Estimates: 
^^^^^^^^^^^^^^^^^^
Expand your estimates section by clicking the scenario name you wish to edit. The web interface will use the information you post in this section to build the csv tables used by Scenario Generator.
 
1. **Landcovers:** The list of landcover types that you are going to model. Including both LULCs in current status and new LULCs in your scenario. No duplicated entries. Required attributes for each entry include LULC ID (as in the raster dataset), Landcover Name, and whether the type exist in current/baseline map or not. If the cover type exists only in your scenario, check the box for “New Cover”.

2. **Drivers:** The activities/processes that contribute to or lead to future land cover change. Drivers won’t be used for the modeling purpose, but they will help you clarify the underlying process and possible linkage between current activities and future land changes. Therefore, we require user input of drivers when add a land transition to force the consideration of the process and linkage. 

3.	**Transitions:** Possible land transitions under the scenario. The information you entered here will be used to build the transition matrix. Required attributes for entries include:

    a. *From Cover:* the LULC type going to decrease in the transition. The site will provide you a drop-down list with all the landcover types you entered in step 1), so that you can select from them. However, once you put an LULC to the “From Cover” field, it will disappear from the “To Cover” drop-down list, and vice versa. That is because the Scenario Generator currently only support growth change modeling, and does not allow an LULC experiencing both growth and decrease.

    b.	*To Cover:* the LULC type going to increase in the transition.

    c.	*Driver:* the driving force of the transition. You will choose from the list of drivers entered in the previous section.
 
    d.	*Likelihood:* the likelihood for such transition to happen.

4.	**Cover Growth:**    Inputs will be used to build the land transition attribute table  

    a.	*Cover:* The cover that will grow in the scenario. The web application will automatically add “To Cover” here after you add a transition.

    b.	*Increase:* The amount of future growth of the LULC in either percentage or hectare. It will be used as the goal for land growth allocation model. (See Scenario Generator for more details.)

    c.	*Units:* the unit of the increase mentioned above. Note that if the cover is a New Cover, you need to select “ha” as the unit. Otherwise please report the increase in percentage. 

    d.	*Priority:* The relative value here will decide which landcover will have its transition modeled earlier. A larger number indicates higher priority, and the cover will be modeled before those with lower priority. Since the value is relative here, the exact number does not matter.

    e.	*Proximity (m) (optional):* The distance limit of proximity effect. Leave it blank or put in 0 if no proximity effect is expected.

    f.	*Patch (ha) (optional):* The minimum patch size required for the transition. Any suitable patches smaller than the size will not be converted.

5.	**Factors (optional):**  Environmental/physical variables that affect the physical suitability for a cover type. The information entered will be used to build the factor table for Scenario Generator.

    a.	*Factor Name.*
    b.	*Landcover:* The target landcover whose growth will be affected by the factor.
    c.	*GIS Layer:* GIS layer file name of the factor.
    d.	*Distance of influence (m):* For line and point factor features, enter the distance of influence in meters.
    e.	*Suitability Field:* For polygon factors, enter the field indicating the suitability level. The range of the value is 0~100. 
    f.	*Weight:* The relative weight of this factor comparing to other factors affecting the same target layer. 
    g.	*Data Type:* Select from point, line, or polygon.

6)	**Constraints:** Areas that land changes area restricted / discouraged. The information entered here serves as a reference. When running Scenario Generator, you will need to provide the Constraints data through the user interface. 

After filling in all the sections, you can download the attributes table and factors table by clicking the buttons at the bottom of the page. Those two tables are in csv format and suits the input requirement for the Scenario Generator. 


Tips
====
1)	If your input does not show up after you click "save" : try to refresh the page.
2)	The likelihood of transition only allows you to choose from limited options. If you want more variation, just download the attribute table and edit the csv file.
3)	For the Growth Priority, you can either enter values from 1 ~ 100, or 0.01 ~ 1. However, do not put in a priority power of 80 among a group of 0.xx, otherwise your 0.xx values might be adjusted to zeros hence showing no difference. Also, remember that higher value indicates higher priority here.

.. primerend