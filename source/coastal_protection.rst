.. _coastal-protection:

.. |openfold| image:: ./shared_images/openfolder.png
              :alt: open
	      :align: middle 

.. |addbutt| image:: ./shared_images/addbutt.png
             :alt: add
	     :align: middle 
	     :height: 15px

.. |okbutt| image:: ./shared_images/okbutt.png
            :alt: OK
	    :align: middle 

.. |adddata| image:: ./shared_images/adddata.png
             :alt: add
	     :align: middle 

***************************
Coastal Protection Model
***************************

Summary
=======

Intro 

Model inputs, which serve as proxies for various complex shoreline processes that influence exposure to erosion and inundation, include: a map of global population distribution, maps of local coastal geomorphology, location of natural habitats (e.g., seagrass, kelps, wetlands, etc.), rates of net sea-level change, a depth contour that can be used as an indicator for surge level (default contour is the edge of the continental shelf), and values of highest observed wind speed and wave power.  The model outputs maps of coastal human populations and of coastal exposure to erosion and inundation.  Outputs can be used to better understand the relative contributions of different variables to coastal exposure, and to highlight the protective services offered by natural habitats to coastal populations.  This information can help coastal managers, planners, landowners, and other stakeholders identify regions of greater risk to coastal hazards, which can in turn inform development strategies and permitting.  This is a "Tier 0" model.


Introduction
============
Intro paragraph descr. I/O

  

.. _cp-Model:

The model
=========

The InVEST Coastal Protection model is a 1-Dimensional (1D) process-based tool that produces an estimate of wave and near-bed water velocity attenuation caused by the presence of natural habitats.  It also estimates the amount of avoided sandy beach erosion and avoided consolidated bed scour due to the presence of those natural habitats.  Results of this model can be used as a first step to value the protective role provided by natural habitats.


How it works
------------

As waves travel from the deep ocean to coastal regions with shallower waters, they start to interact with the bed.  They first increase in height before breaking and dissipating most of their energy in the surf zone and the beach face.  Natural habitats play an important role in protecting shorelines against wave action because they increase the amount of wave dissipation, or, in the case of sand dune, serve as a physical barrier. 

To estimate the profile of wave height that one would expect at a certain region it is imperative to have three types of information: 
1.	Offshore wave characteristics: Wave height and wave period far away from the shoreline, where waves do not interact with the bottom yet.
2.	Nearshore bathymetry and backshore characteristics: Elevation of the submerged and emerged portions of the cross-shore profile relative to Mean Sea Level.
3.	Location and physical characteristics of natural habitats.
In this section, we will present information on how the model helps you figure out how to enter this information in the CP model.

The model is composed of two sub-models.  The first model, which is called Profile Generator, helps you obtain cross-shore (perpendicular to the shoreline) nearshore bathymetry and topography information at your site.  Using this cross-shore profile, the second model, which is called Wave and Erosion, computes profiles of wave height and wave-induced mean water level in the presence and absence of seagrass, marshes, mangroves or coastal forests, coral reefs, and oyster reefs.  When your site is a sandy beach, the model computes the amount of erosion in the presence and absence of subtidal, intertidal and supratidal (e.g., sand-dunes) habitats.  When your site is composed of consolidated sediments (e.g., mud), the model estimates in a very simple way the amount of scour that you could expect.  In the remainder of this section, we will describe how each of these two models works.

Bathymetry and Backshore
^^^^^^^^^^^^^^^^^^^^^^^^

In order to run the Wave and Erosion model, it is necessary to have nearshore bathymetry and topography information at your site of interest.  Bathymetry information can be prepared in three different ways in the Profile Generator model by answering the question *Do you have nearshore bathymetry GIS layer*.  A first answer is *Yes*, and from a Digital Elevation Model (DEM) that can be imported into GIS and contains bathymetry information, the Profile Generator draws a transect perpendicular to the shoreline where your site is located, and read the (X, Z) bathymetry and topographic information below that transect.  

Another option is to answer *No, but I will upload a cross-shore profile*, and from that uploaded profile with a minimum of two (X,Z) coordinate points, you can specify regions where you want to add linear depth profiles.  Lastly, if you do not have any bathymetric information at your site of interest, you can choose the third option *No, please create a theoretical profile for me*, and the model will generate, **for sandy systems only**, a theoretical bathymetric profile, based on the average sand size at your site.  The depth profile follows the following equation (Dean and Dalrymple, 2003):

.. math:: Z=-AX^{2/3} 

where :math:`(X,Z)` represent the cross-shore distance and depth, with :math:`X=0` where :math:`Z` is greatest (deepest point).  The coefficient : math:`A` is a profile scale factor and is a function of sediment size (Dean and Dalrymple, p.162 and CEM).  For simplicity sake, the profile extends from the water line down to -20 meters.  Please remember that this option is only valid for sandy systems, for which sediment size varies between 0.1 to 1.09 mm.

Once you have decided on the method that will be used to create an initial bathymetry, you have the option of adding or modifying the information contained in that profile.  Four different options are available:
1.	Add backshore to a sandy beach
As shown in Figure xx, shoreward of the surf zone, a typical sandy beach profile usually has foreshore and backshore regions.  The foreshore is usually between the Mean Lower Low and Mean Higher High water marks, and the backshore (the region above Mean High Water) consists of a berm and, in temperate regions mostly, a sand dune.  Berms can sometimes have a very small or no width, as shown in Figure xxy.  In general, foreshore and backshore information can not be obtained during standard hydrographic surveys and have to be obtained via special land-surveying techniques.  For this reason, assuming that this information is not contained in the cross-shore profile that we cut for you or you uploaded, we help you guess what foreshore slope, berm height and dune height might be for your site, based on simple rules of thumb.  Please bear in mind that we use rules of thumb developed from site-specific information, and conditions at your site quite differ quite drastically from these rules.

As mentioned earlier, the foreshore is the intertidal region of the beach profile, and we assume that it is linear in our model.  To provide you with guidance on what that slope might be, we provide you with five different values of slope, which are a function of sediment size.  The first three are derived from observations by REFF at beaches that are protected, moderately exposed or fully exposed to the open ocean, in the U.S.  The fourth value is derived from observations by REFF at various beaches around the world.  The fifth value is the average of the four previous values.

Berm height, and foreshore slope, often changes as a function of seasonal wave climate.  After a storm, the profile is flatter and the berm is lower than during fair weathers conditions.  However, in case you do not have any information about berm height at your site, we recommend that you place the berm at least at the same elevation as the Mean High Water mark.  Finally, if your site has sand dunes, which are fairly common in temperate climates (see Fig xx), we provide height estimates based on observations made by XX in Australia.  

XX estimated sand dune height based on modal wave height and period as well as tidal range values.   

2.	Add a backshore to a mangrove or mash
Mangrove and marsh beds are different from sandy beaches because they consist, in general, of consolidated materials, do not have dunes, and their profile is in general fairly linear.  In general, mangrove bed slopes vary between 1V:400H and 1V:600H xxxx.  We did not find any specific guidelines for marsh profiles.

If you choose this option, you will have to enter a maximum of three linear profiles that can be added to the bathymetry profile that was cut/created for you or that you uploaded.  

3.	Modify a profile uploaded in the GIS interface
As mentioned earlier, if you upload a profile with a minimum of two (X, Z) points, you can modify it or add to it by creating linear xx between fixed distances.  This option is especially useful in cases when you are not fully satisfied with the profile that was cut in GIS and want to modify it, when you want to create a depth profile from scratch, or when you want to add intertidal and backshore regions to depth profiles.
  
4.	Nothing, I don’t want to add any additional information
You can use this last option if you just want the model cut and smooth a profile for you or to just smooth a profile that you uploaded.

The last functionality of the profile generator is to locate the presence of natural habitats along your cross-section.  When you choose Option 1 *Yes* to the question *Do you have nearshore bathymetry GIS layer*, you can also indicate the types of natural habitats that are present in your region, and the model will locate and plot where those habitats fall onto the cross-shore bathymetry.  

To estimate the amount of shoreline erosion, the model computes the total water level at the shoreline during a given (user-input) storm duration.  This storm can be accompanied with strong winds.  The total water level at the shoreline is composed of the sum of tide, amount of sea-level rise, any water surface elevation anomaly (e.g., super-elevation during an El Niño), storm surge, and wave runup.



Wave Evolution Model
^^^^^^^^^^^^^^^^^^^^
To quantify the protective services provided by natural habitats, the CP model computes the amount of attenuation of waves, wave-induced mean water level and near bottom water velocity caused by submerged vegetation and reefs.  Assuming that waves have a deep water height of :math:`H_o` and a period :math:`T`, it is possible to compute the evolution of wave height from offshore to the shoreline along the x-axis of the user defined cross-shore transect with the following wave energy equation:

.. math:: \frac{1}{8}\rho g \frac{\partial C_g H^2}{\partial x}=-\textit{D}

where :math:`\rho` is the density of seawater, taken as :math:`1,024 kg/m^{3}`, :math:`g=9.81 m/s^2` is the gravitational acceleration, :math:`H` is the wave height representative of the random wave field, :math:`C_g` is the speed at which wave energy travels, and :math:` \textit{D}` is the dissipation of wave energy.  The role of dissipation is to decrease the amount of wave energy as it propagates through or over different media.  It is the sum of dissipation caused by wave breaking :math: `\textit{D_{Break}}`, bottom friction :math: `\textit{D_{Bot}}`, and submerged vegetation :math: `\textit{D_{Veg}}`: 

.. math::\mathfrak{D}=\mathfrak{D}_{Break}+\mathfrak{D}_{Bot}+\mathfrak{D}_{Veg}

Dissipation due breaking is modeled using the formulation and default parameters presented by Alsina and Baldock (2007):

.. math:: \mathfrak{D}_{Break}=A\frac{H^3}{h}\left [ \left ( \left (\frac{H_b}{H}  \right )^3+\frac{3H_b}{2H} \right )) \exp \left ( -\left (\frac{H_b}{H}  \right )^2 \right )+\frac{3\sqrt\pi}{4}\left ( 1-erf\left ( \frac{H_b}{H} \right ) \right ) \right ]

where :math:`erf` is the Gauss error function, :math:`h` is the local water depth, :math:`A` is the sediment scale factor (see Section Xx), and :math:`H_b` is the maximum wave height prior to breaking:

.. math:: H_b=\frac{0.88}{k}tanh\left ( \gamma \frac{kh}{0.88} \right )

where :math:`k` is the wavenumber, the ratio of length between two wave crests (called wavelength) :math:`L` to :math:`2\pi`, and :math:`\gamma` is a calibration parameter called the breaking index.  In our model, we take the default :math:`\gamma` value proposed by Battjes and Stive (1985):

.. math:: \gamma=0.5+0.4 \tanh\left ( 33\frac{H_o}{L_o} \right )

where :math:`H_o` and :math:`L_o` are the deepwater wave height and wavelength, respectively.

Dissipation due to bottom friction is initiated when waves are in shallow enough water to “feel” the bottom, and is higher for coarser bed material than smoother ones.  In our model, it is triggered when waves travel over sandy bottoms, but also coral reefs, which are rougher than sand beds.  Following Thornton and Guza (1983), we modeled dissipation due to bottom friction by:

..math:\mathfrak{D}_{Bot}=\rho C_f \frac{1}{16\sqrt\pi} \left[ \frac{\sigma H}{\sinh kh} \right]^3

where :math:`C_f` is the bed friction coefficient, which is a function of the roughness (or dimensions) of the bed (the bed can be plain sand, or a coral reef, or a bed of oysters, etc.), and :math:`\sigma` is the wave frequency, the ratio of wave period :math:`T` to :math:`2 \pi`.  In our model, we assumed the following default friction coefficients:

- For bare beds, :math:`C_f=0.001`, 
- For live corals, :math:`Cf=0.2`,
- For dead (smooth) corals, :`Cf=0.1`

Finally, dissipation due to the presence of vegetation is expressed by (Mendez and Losada, 2004):

.. math:: \mathfrak{D}_{Veg}=\frac{1}{2\sqrt\pi} \rho N d C_d \left(\frac{kg}{2 \sigma} \right ) ^3 \frac{\sinh ^3 k \alpha h +3 \sinh k \alpha h}{3k \cosh ^3 kh} H^3

where :math:`N` is the density of vegetation stems per unit area, :math:`d` is the frontal width or diameter of vegetation stems, and :math:`\alpha` represents the fraction of the water depth :math:`h` occupied by vegetation elements of average stem height :math:`h_c`: :math: `\alpha=h_c\h`.  In the case of submerged vegetation, :math:`\alpha<1`, and in the case of emergent vegetation (:math:`h_c>h`), :math:`\alpha=1`.  Finally, :math:`C_d` is a taxa-specific (e.g., eelgrass, marsh, mangroves) drag coefficient.  In our model, we assumed default values of drag coefficient based on observations:

- For seagrass beds and marshes, :math:`C_d=0.01`
- For trees, including mangroves, :math:`C_d=1`

For trees, and mangroves in particular, we assumed that roots, trunk and canopy contribute independently to the total dissipation caused by vegetation, and :math:`\mathfrak{D}_{Veg}` becomes: :math:`\mathfrak{D}_{Veg}=\mathfrak{D}_{Roots}+\mathfrak{D}_{Trunk}+\mathfrak{D}_{Canopy}`.  More information on how we treat mangroves is presented in Appendix XX.

The wave-evolution equation presented above (Equation xx) is valid when the bottom slope is relatively flat.  When waves encounter steep barriers such as coral and oyster reefs, we do not estimate directly the profile of wave height during breaking, but we estimate the broken wave height following two different methods.  For coral reefs with a steep face, or when we do not have a precise measured profile, we estimate the broken wave height on the reef top :math:`H_r` assuming that wave height is controlled by water depth :math:`h_{top}` (Gourlay, 1996a, b) : :math:`H_r=0.46h_{top}`, where :math:`h_{top}=h_r+\overline{\eta}_r+h_+` is the total water depth on top of the reef.  

The total water depth is the sum of the depth on the reef top referenced to Mean Sea Level :math:`h_r`, the wave setup on the reef caused by breaking waves :math:` \overline{\eta}_r`, and any additional super-elevation of the water level, which can be caused by tides, pressure anomalies, etc.  The wave setup on the reef top is caused by the release of wave energy during breaking, and it is computed using the empirical equation proposed by Goulay (1996a,b; 1997):

.. math:: \overline{\eta}_r=\frac{3}{64\pi}K_p \frac{\sqrt g H_i^2T}{\left(\overline{\eta}_r+h_r \right )^{3/2}}

where :math:`H_i` is the incident wave height, or the wave height at the offshore edge of the coral reef.  The coefficient :math:`K_p` is the reef profile shape factor, and is a function of the reef face slope :math:`\alpha_f` or the reef rim slope :math:`\alpha_r`, depending on whether waves break on the reef face or rim.  Once the broken wave height is established following the equation presented above, we determine the profile of wave height over the reef top following Equation xx, with :math:`\mathfrak{D}_{Break}=\mathfrak{D}_{Veg}=0`, and :math: \mathfrak{D}_{Bot}` is computed with a friction coefficient representing live or dead coral.

In the case of oyster reefs, we estimate the wave height :math:`H_t` shoreward of the reef with the following equations based on the incident wave height :math:`H_i`:

.. math::H_t=K_tH_i

where :math:`K_t` is a transmission coefficient.  In the case of trapezoidal-shaped reefs, the transmission coefficient is computed with an empirical formula developed for low-crested breakwaters (van der Meer et al., 2005):

.. math:: K_t=\begin{cases}
          -0.4\frac{R_c}{H_i}+0.64\left(\frac{B}{H_i} \right )^{-0.31} \left(1-e^{-0.5\xi} \right) & \text{ if } B/H_i<8 \\ 
          -0.35\frac{R_c}{H_i}+0.51\left(\frac{B}{H_i} \right )^{-0.65} \left(1-e^{-0.41\xi} \right)& \text{ if } B/H_i>12 
          \end{cases}

where :math:`B` is the crest width of the reef, and :math:`R_c=h_c-h` is the crest freeboard, the difference between the structure height :math:`h_c` and the water depth :math:`h`.  The breaker parameter :math:`\xi` is computed as :math:`\xi=\tan \alpha/\left(S_i \right)^{0.5}` where the seaward slope of the structure :math:` \tan \alpha` is computed as a function of the structure crest and base width, :math:`B` and :math:`W`, respectively: :math:`\tan \alpha=2h_c/\left(W-B \right)`.  Finally, :math:`S_i` is the incident wave steepness: :math:`S_i=2\pi H_i/\left(g T_p \right).  In the above equation, when :math:`8<B/H_i<12`, we estimate :math:`K_t` by linearly approximation.  

If the oyster reef is a ball resembling the Reef Ball:sup:`TM`, we follow the empirical equation proposed by Refxx:

.. math:: K_t=1.616-4.292\frac{H_i}{T^2}-1.099\frac{h_c}{h}+0.265\frac{h}{W}

Once waves have travelled past the coral and oyster reefs, we model their evolution in the remaining portion of the bathymetry using Equation xx, assuming that their peak period :math:`T` hasn’t changed.

Once the profile of wave height has been computed, we estimate the amount of wave runup at the shoreline.  Indeed, in addition to storm-generated surges, wind-generated waves contribute to the super-elevation of the water level observed during storms.  At the shoreline, this super-elevation is called wave runup (:math:`R_2`; see CEM, Chap. xx), and we compute it based on the empirical equation proposed by Stockdon et al. (2006):

.. math:: R_2=1.1 \left(0.35 m \sqrt {H_o L_o} +0.5\sqrt{0.563m^2H_o L_o+0.004H_o L_o } \right )

where :math:`m` is the foreshore slope, or the average cross-shore slope at the shoreline.  In the above equation, the first term in the parenthesis represents the wave setup, and it can be influenced by the presence of the vegetation.  The second term represents the wave swash, and it is composed of two terms.  The first term, which is a factor of the foreshore slope :math:`m` is called incident wave swash, and it can also be influenced by the presence of the vegetation.  The second term is the called the infragravity swash, and we assumed that it is not affected by the presence of vegetation elements because vegetation does not affect long-period waves as much as it does short period waves.  In the absence of biogenic features, the CP model only requires information on the characteristics of offshore waves and foreshore slope to compute wave runup.  If intertidal or subtidal biogenic features are present, we estimate wave runup by using the following procedure.

First, we estimate, in the absence and in the presence of vegetation, the profile of wave height following the procedure outlined above, and the wave setup :math:`\overline{\eta}` at the shoreline by solving the following force balance equation:

.. math:: \frac{\partial S_{xx}}{\partial x}+\rho g \left(h+\overline{\eta} \right )\frac{\partial \overline{\eta}}{\partial x}-f_x=0

where :math:`S_{xx}` is the force per unit length generated by the waves on the water column, and :math:`f_x` is the force per unit area due to the presence of vegetation elements:

.. math:: f_x=-\alpha F_x

where the force :math:`F_x` is computed following Dean and Bender (2006):

.. math::F_x=\rho g \frac{1}{12 \pi}NdC_d \frac{k}{\tanh kh}H^3

Neglecting non-linear processes associated with wave propagation, this equation is only valid for emergent vegetation.  Consequently, we added the coefficient :math:`\alpha` to the approximate the effects of vegetation on the wave setup when it is submerged.  This approximation over-estimates the reduction in wave setup caused by submerged vegetation compared to what we would obtained if we had adopted a non-linear wave theory to estimate :math:`F_x`.  However, for our intent and purposes, this approximation is much faster and simpler to adopt. 
Once we have obtained values of wave setup in the absence of vegetation, we estimate a proportionality coefficient :math:`\beta` between the empirical estimate of wave setup and the value of the modeled wave setup at the shoreline :math:`\overline{\eta}_{Shore}` :

.. math:: \beta=\frac{\overline{\eta}_{shore}}{0.35m\sqrt{H_oL_o}}

Based on the modeled value of the wave setup at the shoreline in the presence of vegetation, :math:`\overline{\eta}_{Shore}^{v}`, we estimate the hypothetical offshore wave height :math:`H_p` that would have achieved the same modeled setup, assuming that the value of the coefficient :math:`\beta` is the same:

.. math:: H_p=\frac{1}{L_o}\left (\frac{\overline{\eta}_{Shore}^{v}}{0.35m}  \right )^2

In cases when the effects of vegetation are so pronounced that :math:`\overline{\eta}_{Shore}^{v}` is negative, we assume that :math:`H_p=0`.

Finally, to estimate the amount of runup at the shoreline in the presence of natural habitats, we replace :math:`H_o` in Equation Xx by the value of the hypothetical offshore wave height :math:`H_p` in the wave setup and wave-induced swash terms:

.. math:: R_2=1.1 \left(0.35 m \sqrt {H_p L_o} +0.5\sqrt{0.563m^2H_p L_o+0.004H_o L_o } \right )

where the last term is left untouched because, as mentioned earlier, we assumed that long waves are not affected by the presence of natural habitats.  Similarly, we did not change the value of the offshore wavelength :math:`L_o` because we assumed that peak wave period is not affected by the presence of natural habitats.

Shoreline Response
^^^^^^^^^^^^^^^^^^

The model estimates two types of shoreline response to wave attack.  In case of sandy beach systems, we compute the amount of shoreline erosion that takes place after a storm based on the value of storm surge and wave runup computed by the wave evolution model.  In cases when the shoreline is composed of consolidated sediments (mangroves, marshes), we compute the amount of bed scour that one could expect.  In both cases, we use empirical equations that ignore the dynamic response of the system.


