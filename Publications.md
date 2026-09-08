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

{% assign independent_pubs = site.data.pub_toc | where: "category", "independent" %}
{% assign independent_query = "" %}
{% for pub in independent_pubs %}
  {% unless forloop.first %}{% assign independent_query = independent_query | append: " || " %}{% endunless %}
  {% assign independent_query = independent_query | append: "key=" | append: pub.key %}
{% endfor %}
{% bibliography --template bibliography_card --query @*[{{ independent_query }}] %}

## Preprints

{% assign preprint_pubs = site.data.pub_toc | where: "category", "preprint" %}
{% assign preprint_query = "" %}
{% for pub in preprint_pubs %}
  {% unless forloop.first %}{% assign preprint_query = preprint_query | append: " || " %}{% endunless %}
  {% assign preprint_query = preprint_query | append: "key=" | append: pub.key %}
{% endfor %}
{% bibliography --template bibliography_card --query @*[{{ preprint_query }}] %}

## Collaborative Independent Work

Ongoing collaborations that apply our magnetic resonance expertise to other
groups' materials systems.

{% assign collab_pubs = site.data.pub_toc | where: "category", "collab" %}
{% assign collab_query = "" %}
{% for pub in collab_pubs %}
  {% unless forloop.first %}{% assign collab_query = collab_query | append: " || " %}{% endunless %}
  {% assign collab_query = collab_query | append: "key=" | append: pub.key %}
{% endfor %}
{% bibliography --template bibliography_card --query @*[{{ collab_query }}] %}

## Earlier Publications (PhD and Postdoctoral Work)

{% assign exclude_query = "" %}
{% for pub in site.data.pub_toc %}
  {% unless forloop.first %}{% assign exclude_query = exclude_query | append: " && " %}{% endunless %}
  {% assign exclude_query = exclude_query | append: "key!=" | append: pub.key %}
{% endfor %}
{% bibliography --query @*[{{ exclude_query }}] %}
