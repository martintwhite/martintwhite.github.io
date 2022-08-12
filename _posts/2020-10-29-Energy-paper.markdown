---
layout: post
title:  "New paper: Making the case for cascaded ORC systems"
date:   2020-10-29 09:00:00 +0000
categories: research
image: /assets/cascaded.png
---
It is a little over a year ago that I presented at [ORC2019 and the Compressor Conference]({{site.baseurl}}{% link _posts/2019-09-13-ORC2019.markdown %}), and subsequently introduced you to the topic of a cascaded ORC system [on this blog]({{site.baseurl}}{% link _posts/2019-10-03-Cascaded-ORC.markdown %}). Fast forward a year, and my latest paper published in the Energy journal has further confirmed that cascaded ORC systems can outperform single-stage ORC systems.

The topic of this latest paper once again focusses on using [organic Rankine cycle (ORC)]({{site.baseurl}}{% link page4_ORC_101.md %}) technology for the generation of power from waste heat, with a focus on cascaded systems. As a quick recap, a cascaded ORC system is essentially two ORC systems coupled together, with the heat that is rejected from the first ORC being used as the input heat for the second.

<p></p>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/cascaded.png" alt="cascaded" style="width:400px;" />
</div>
<p></p>

In the latest paper, optimal single-stage and cascaded cycles have been identified that can maximise performance, and the heat exchangers (which can represent a significant portion of the cost of an ORC system) were designed.  As a general rule of thumb, the better the performance, the larger and more costly the heat exchangers, so there is a trade-off between performance and cost to be had here.

This trade-off can be explored through optimisation and the generation of what is called a ‘Pareto front’. So, what’s a Pareto front?

A Pareto front is essentially a collection of optimal solutions that considers the trade-off between two things. So, let’s say I asked you to design a system and I was interested in two things – performance and cost. Well, there are few different systems that you could come up with:
* if you were to design a system that had the highest possible performance, it is logical to assume that that system is going to be very expensive
* likewise, if you were to design a system that was cheap it would follow that that system would not perform very well
* and, if you wanted a compromise, you would design a system that cost more and performed better than the cheap solution but wouldn’t cost as much or perform as well as the most expensive solution
* and in between the two extremes there would be a whole range of solutions depending upon which of those your objectives you prioritised

If you were to express that graphically, it would look something like the picture below, with the cheap solution (circle), expensive solution (triangle) and trade-off solutions (stars) making up the Pareto front (solid line).

<p></p>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/Pareto_front.png" alt="Pareto" style="width:350px;" />
</div>
<p></p>

So, what do the Pareto fronts from this latest study tell us? Well, take a look for yourself.

<p></p>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/Energy2020_pareto.png" alt="Egy_Pareto" style="width:500px;" />
</div>
<p></p>

In this figure, the red and black markers correspond to the Pareto fronts generated for the two different systems, and these tell us a few interesting points. Firstly, if I could afford quite large heat exchangers (in this specific case, greater than around 200 m<sup>2</sup>), then for that amount of area I could generate more power with a cascaded system than a single-stage system. On the other hand, if the size of the heat exchangers was restricted, you would probably be better off with a single-stage system.

So there you have it, these results suggest that in applications where maximising performance is not the primary objective, single-stage ORC systems remain the best option. However, in applications where you want to maximise performance cascaded systems can produce more power for the same size heat exchangers.

### Acknowledgement
This work was completed as part of the [NextORC project](https://researchcentres.city.ac.uk/thermo-fluids/nextorc), which is funded by the UK Engineering and Physical Sciences Research Council (EPSRC) [grant number: [EP/P009131/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/P009131/1)].

[You can read the full paper for free here.](https://doi.org/10.1016/j.energy.2020.118912)

Citation details:

White, M., Read, M., Sayma, A., 2020, “Making the case for cascaded organic Rankine cycles for waste-heat recovery", Energy, 211, 118912. [doi: 10.1016/j.energy.2020.118912](https://doi.org/10.1016/j.energy.2020.118912)