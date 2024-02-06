---
layout: page
title: Archive
permalink: /Archive/
---

<div class="post">
	  {% for post in site.posts %}
	    {% unless post.next %}
	      <h4>{{ post.date | date: '%Y %b' }}</h4>
	    {% else %}
	      {% capture year %}{{ post.date | date: '%Y %b' }}{% endcapture %}
	      {% capture nyear %}{{ post.next.date | date: '%Y %b' }}{% endcapture %}
	      {% if year != nyear %}
	        <h4>{{ post.date | date: '%Y %b' }}</h4>
	      {% endif %}
	    {% endunless %}
	    <ul><a href="{{ post.url }}">{{ post.title }}</a></ul>
	  {% endfor %}
</div>