---
layout: post
title:  "Axial turbines for power cycles operating with supercritical carbon dioxide blends"
date:   2023-05-16 00:00:00 +0000
image: /assets/stage_number_efficiency.png
---

Back in 2021, I introduced [supercritical carbon dioxide power cycles](https://martintwhite.github.io/research/2021/02/04/What-is-sCO2.html) and [CO<sub>2</sub> blends](https://martintwhite.github.io/research/2021/03/18/CO2-blends.html) on this blog. This was in the context of the [SCARABEUS project](https://www.scarabeusproject.eu/), and the work that was getting started at City to design an axial turbine for a power cycle operating with CO<sub>2</sub> blends. A couple years on, and the hard work of last few years is starting to pay off.

Before talking about the research, let’s start with some basics.

<br/>
# What is a turbine?

Well, in a power cycle, the turbine is the component responsible for generating power. In the simplest sense, a turbine can be thought of as a bladed rotating device. The blades form channels through which the fluid flows. A fluid at a high temperature and high pressure enters the turbine, and, as it passes through these channels, power is extracted from the fluid and transferred to the rotating shaft. The power transmitted to the shaft can then be converted into electricity using a generator. Subsequently, the fluid leaving the turbine has a lower temperature and lower pressure than when it entered, and the corresponding change in temperature and pressure can be used to determine the power produced.

OK, but what is an *axial* turbine?

Good question. The term axial here relates to the general direction of the flow as it passes through the turbine. Here, axial means the flow is travelling in-line with the axis of rotation. Other types of turbines include the 90° radial in-flow, radial out-flow and mixed flow configurations. The 90° radial in-flow configuration is the most common of the three and generally when people refer to a radial turbine they probably mean a 90° radial in-flow turbine. In this machine, the flow enters the turbine in the radial direction, flowing inwards towards the axis of rotation, and is turned through 90° which means the flow leaves in the axial direction.

<br/>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/turbine_flowpath_schematics.png" alt="turbine-flowpaths" style="width:900px;" />
</div>
<br/>
*Cross-sectional view of an axial turbine and a 90° radial in-flow turbine. The green arrows show the direction of the flow relative to the axis of rotation. The red and blue regions correspond to the stator and rotor passages respectively. Here the axial turbine has four stages.*
<br/><br/>

The choice between axial or radial is generally a question of scale. It is hard to draw a precise line in the sand as it depends on many factors including the fluid it operates with, the operating conditions, and the intended application amongst many others. But in a general sense, for small-scale applications where power is generated for a small number of users it is likely a radial turbine will be used, whilst for utility-scale power plants most likely an axial turbine will be used.

<br/>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/axial_turbine_example.jpg" alt="axial-turbine" style="height:400px;" />
	<img src="{{site.baseurl}}/assets/radial_turbine_example.jpg" alt="radial-turbine" style="height:400px;" />
</div>
<br/>
*The left figure shows the rotor of a multi-stage axial turbine The right shows the rotor of a 90° radial in-flow turbine. (Left image: from Siemens Pressebild, [http://www.siemens.com/](http://www.siemens.com/), CC BY-SA 3.0 [http://creativecommons.org/licenses/by-sa/3.0](http://creativecommons.org/licenses/by-sa/3.0), via Wikimedia Commons; right image: Royonx, CC0, via Wikimedia Common).*
<br/><br/>

# Axial turbine design for supercritical CO<sub>2</sub> turbines

In the SCARABEUS project, the City team were tasked with carrying out the aerodynamic design of a turbine for a 100 MW<sub>e</sub> power plant for a concentrated-solar power plant. More importantly, the turbine needs to be designed to operate with a supercritical CO<sub>2</sub> blend. 

Axial turbines for power plants in order of 100 MW<sub>e</sub> are an established technology, but for operation with air or steam. Such turbines find application in conventional power generation systems including gas turbines and steam power plants. 

However, for operation with both pure supercritical CO<sub>2</sub> and CO<sub>2</sub> blends such turbine designs are not readily available. Supercritical CO<sub>2</sub> turbine design is an evolving field, and experimental prototypes have been developed, and some remain under development. These all operate with pure CO<sub>2</sub> and have lower power ratings than being considered in SCARABEUS. Many of these have also been radial turbines.

Therefore, the research at City has been an exciting opportunity to design an axial turbine for a 100 MW<sub>e</sub> power plant. Open questions that we aimed to address include *“what might an axial turbine for this application look like?”*, *“what performance might we expect from a turbine designed for this application?”*, and *“what is the influence of the selected CO2<sub>2</sub> blend on the resulting turbine design?”*.

To date, our team have done pretty well, and we have published a number of papers on the topic. In our most recent works, we have carried out a design activity to assess the achievable performance of axial turbines operating with CO2<sub>2</sub> blends when varying the number of turbine stages. This led to proposal of a 14-stage axial turbine design for the SCARABEUS project for which more detailed design activities have been carried out.

<br/>
# Welcome to the *stage* number

When we talk about axial turbines, you may often hear about multi-stage machines. And the number of stages is an important design parameter. But what is a turbine stage?

Well, any turbine is composed of stationary parts and rotating parts. The stationary part is referred to as a stator row, and the rotor is referred to as a rotor row. Each stator or rotor row is composed of multiple blades mounted in a circle around the central axis of the turbine. You can see this in the photos of the axial and radial turbine rotors that were introduced earlier.

The purpose of a stator blade row is to effectively increase the speed of the flow and to change its direction. The purpose of the rotor blade row is to do a similar thing, but in the process extract energy. This is achieved by effectively changing the direction of the flow, which reduces its momentum. 

A turbine stage is composed of one stator row, and one rotor row Therefore, if you had a single-stage turbine design, you would simply have one stator row and one rotor row. A multi-stage turbine simply means you have multiple turbine stages which are placed in series. So if you had a two-stage turbine would have one pair of stator and rotor rows, followed by another pair of rotor and stator rows (i.e., rotor-stator-rotor-stator). And so on for an increasing number of stages.

So, why is this a benefit?

In essence, a multi-stage design enables the expansion process to be divided across the stages. So, if you wanted to expand CO<sub>2</sub> from a pressure of 200 bar to a pressure of 50 bar, a single stage design would have to reduce the pressure by 150 bar over a single stage. However, if you used four stages, each stage would only need to reduce the pressure by 50 bar. Principally, this has benefits in terms of performance, but the number of stages does also influence other factors such as size, cost and mechanical integrity.

You can find out more about our latest work in the publications linked below. But for now here are a few sneak peaks of some of the results.

<br/>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/four_stage_flowpaths.png" alt="blend-flowpaths" style="width:700px;" />
</div>
<br/>
*This image shows the effect of the selected blend on the resulting size and shape of the flow path, assuming a four-stage axial turbine. The blends are sulphur dioxide (SO<sub>2</sub>), hexafluorobenzene (C<sub>6</sub>F<sub>6</sub> and titanium tetrachloride (TiCl<sub>4</sub>). As we can see, different blends require a different flow path design.*
	
<br/>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/stage_number_efficiency.png" alt="stage-efficiency" style="width:400px;" />
</div>
<br/>
*This image shows how increasing the number of stages can improve the efficiency of the turbine. The turbine efficiency is essentially the ratio of the power produced by the turbine to the maximum theoretical power that it could generate. So, a higher efficiency, means more power!*
<br/><br/>

# References
More information about the work mentioned here can be found in the following publications:

- [Axial turbine flow path design for concentrated solar power plants operating with CO<sub>2</sub> blends](https://doi.org/10.1016/j.applthermaleng.2023.120612)

- [Design of a 130 MW axial turbine operating with a supercritical carbon dioxide mixture for the SCARABEUS project](https://www.researchgate.net/publication/370419868_DESIGN_OF_A_130_MW_AXIAL_TURBINE_OPERATING_WITH_A_SUPERCRITICAL_CARBON_DIOXIDE_MIXTURE_FOR_THE_SCARABEUS_PROJECT)

Other publications from the City team on supercritical CO<sub>2</sub> turbines:

- [A modified loss breakdown approach for axial turbines operating with blended supercritical carbon dioxide](https://doi.org/10.1115/1.4062478)

- [A comparison of axial turbine loss models for air, sCO<sub>2</sub> and ORC turbines across a range of scales](https://dx.doi.org/10.1016/j.ijft.2022.100156)

- [Integrated aerodynamic and structural blade shape optimisation of axial turbines operating with supercritical carbon dioxide blended with dopants](https://dx.doi.org/10.1115/1.4055232)

- [Sensitivity of transcritical cycle and turbine design to dopant fraction in CO<sub>2</sub>-based working fluids](https://dx.doi.org/10.1016/j.applthermaleng.2021.116796)


