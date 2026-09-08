---
layout: default
title: Publications
attribution: J.M. Franck
scholar:
  sort_by: year
  order: descending
---
# {{page.title}}

- [Independent Research](#independent-research-franck-lab-syracuse-university)
  -- peer-reviewed papers from the Franck Lab at Syracuse/ACERT.
- [Preprints](#preprints) -- work posted ahead of peer review.
- [Collaborative Independent Work](#collaborative-independent-work) --
  ongoing collaborations applying our magnetic resonance expertise to other
  groups' materials systems.
- [Earlier Publications](#earlier-publications-phd-and-postdoctoral-work) --
  publications from PhD and postdoctoral work.

[Link to Complete List of Publications](https://scholar.google.com/citations?user=TdqiwiIAAAAJ&hl=en&oi=ao){:target="blank"}

## Independent Research (Franck Lab, Syracuse University)

{% assign independent_pubs = site.data.pub_toc | where: "category", "independent" | sort: "year" | reverse %}
{% for pub in independent_pubs %}
{% capture pub_reference %}{% bibliography --query @*[key={{ pub.key }}] %}{% endcapture %}
<div class="pub-card">

<img src="{{ pub.image }}" alt="TOC figure for {{ pub.key }}">

{{ pub_reference | replace: '">1. ', '">' }}

</div>
{% endfor %}

## Preprints

{% assign preprint_pubs = site.data.pub_toc | where: "category", "preprint" | sort: "year" | reverse %}
{% for pub in preprint_pubs %}
  {% if pub.image %}
<div class="pub-card">

<img src="{{ pub.image }}" alt="TOC figure for {{ pub.key }}">

{% capture pub_reference %}{% bibliography --query @*[key={{ pub.key }}] %}{% endcapture %}
{{ pub_reference | replace: '">1. ', '">' }}

</div>
  {% else %}
{% bibliography --query @*[key={{ pub.key }}] %}
  {% endif %}
{% endfor %}

## Collaborative Independent Work

Ongoing collaborations that apply our magnetic resonance expertise to other
groups' materials systems.

{% assign collab_pubs = site.data.pub_toc | where: "category", "collab" | sort: "year" | reverse %}
{% for pub in collab_pubs %}
  {% if pub.image %}
<div class="pub-card">

<img src="{{ pub.image }}" alt="TOC figure for {{ pub.key }}">

{% capture pub_reference %}{% bibliography --query @*[key={{ pub.key }}] %}{% endcapture %}
{{ pub_reference | replace: '">1. ', '">' }}

</div>
  {% else %}
{% bibliography --query @*[key={{ pub.key }}] %}
  {% endif %}
{% endfor %}

## Earlier Publications (PhD and Postdoctoral Work)

{% assign exclude_query = "" %}
{% for pub in site.data.pub_toc %}
  {% unless forloop.first %}{% assign exclude_query = exclude_query | append: " && " %}{% endunless %}
  {% assign exclude_query = exclude_query | append: "key!=" | append: pub.key %}
{% endfor %}
{% bibliography --query @*[{{ exclude_query }}] %}
