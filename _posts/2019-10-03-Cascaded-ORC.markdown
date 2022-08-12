---
layout: post
title:  "So what's the deal with cascaded ORC systems?"
date:   2019-10-04 09:00:00 +0000
categories: research
image: /assets/cascaded.png
---
September marked the first month of my Royal Academy of Engineering Research Fellowship and boy has it flown by! Interspersed with two conferences, meeting with my mentor for the first time and attending the Welcome Induction event at the Academy, I have moved into my new office, started to settle into the routine of life that comes with the start of the new academic year – and, somehow, found some time to start my fellowship research.

In a busy month, the first big ticket items were two conference papers that were presented at two different conferences at the beginning of the month, as reported in my [previous post]({{site.baseurl}}{% link _posts/2019-09-13-ORC2019.markdown %}). The focus of this work was looking at cascaded organic Rankine cycles (ORC) for more effectively converting waste heat into electricity.

So, what is a cascaded organic Rankine cycle?

Hopefully, from the [ORC-101 section]({{site.baseurl}}{% link page4_ORC_101.md %}), the concept of an ORC is somewhat familiar, where we can use a heat source to drive the thermal power cycle to generate power, and then reject heat to a heat sink. Well, a cascaded ORC system is essentially two ORC systems coupled together, with the heat that is rejected from the first ORC being used as the input heat for the second.

<p></p>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/cascaded.png" alt="cascaded" style="width:400px;" />
</div>
<p></p>

If you are now starting to think that this sounds a little more complicated, you would be right. Inevitably then, cascaded systems require more components and are likely to be more expensive than a single ORC system. So, the question we are aiming to address with this current research is whether such a system can offer any benefits in performance (i.e., can we get more power output from the same heat source), and does this performance outweigh this extra complexity of the system?

In the first paper, presented at the [Compressor Conference](https://iopscience.iop.org/article/10.1088/1757-899X/604/1/012086), the work reported involved the use of computer models to assess the performance of different single and cascaded ORC systems intended for converting heat at different temperatures into electricity. In essence, we used a computer to find the best single and cascaded systems that produce the largest amount of power for a defined heat source. And the results obtained are quite promising.

**_It was found that cascaded systems could produce between 4% and 6% more power than the single ORC systems._**

In the second paper, presented at the [ORC Conference](https://www.orc2019.com/online/proceedings/display_manuscript/113.htm), the work reported moved into the realm of assessing the increase in cost. Within this work we developed additional computer models that can be used to find the best design for the heat-exchangers within the ORC systems. Specifically, we looked at how much heat-transfer area is required for the single and cascaded ORC systems, which is related to cost (heat-transfer area is related to the physical size of heat exchangers within the system; a larger heat exchanger will typically cost more). The findings from this study were perhaps less clear.

**_It was found that cascaded ORC systems require around 20% more heat-transfer area than single ORC systems._**

Thus, the answer to the first question, as it turns out, is *yes*. 

The answer to the second is not so straight forward. It would appear that larger heat exchangers are required – but to answer this question it is necessary to do a bit more research to convert this 20% increase into an increased cost. After a busy month back to doing some research it is...

<p></p>
<div style="text-align:center">
	<img src="{{site.baseurl}}/assets/cascaded_results.png" alt="cascaded_res" style="width:600px;" />
	<p><i>Change in power output and heat-exchanger size for cascaded ORC systems compared to single ORC systems.</i></p>
</div>
<p></p>

### Acknowledgement 
*This work was completed as part of the [NextORC project](https://www.city.ac.uk/nextorc), which is funded by the UK Engineering and Physical Sciences Research Council (EPSRC) [grant number: [EP/P009131/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/P009131/1)].*

*More details of this research can be found in the following links:*

*White, M., Read, M., Sayma, A., 2019, "Comparison between single and cascaded organic Rankine cycle systems accounting for the effects of expansion volume ratio on expander performance", IOP Conf Ser: Mater Sci Eng, 604, 012086. [https://doi.org/10.1088/1757-899X/604/1/012086](https://doi.org/10.1088/1757-899X/604/1/012086)*

*White, M., Read, M., Sayma, A., 2019, “A comparison between cascaded and single-stage ORC systems taken from the component perspective”, Proceedings of the 5th International Seminar on ORC Power Systems, September 9-11, 2019, Athens, Greece, ISBN: 978-90-9032038-0. [https://www.orc2019.com/online/proceedings/display_manuscript/113.htm](https://www.orc2019.com/online/proceedings/display_manuscript/113.htm)*