---
layout: default
title: Research
attribution: J.M. Franck
---
# {{page.title}}: General

## Hydration Water

Even though water appears uniform
    on a macroscopic scale,
    it behaves quite differently
    on the nanoscale.
If we zoom in to the first few layers of water
    molecules near the surface of a protein or polymer
    (in fact, near any macromolecule or macromolecular assembly),
    we see that
    hydrogen bonds break
    and
    individual water molecules move
    at rates
    anywhere from two times
    slower to hundreds of times slower than those in the bulk
    liquid.
We know that these differently behaved "hydration waters" are
    key to determining interactions.

The future of physical and analytical chemistry
    will center on the fact that,
    while tools have been developed for
    characterizing static structures,
    we still need techniques that can study
    dynamic arrangements of molecules
    and, most urgently,
    the arrangement
    of water molecules.

Comprehensive methods for mapping out
    the structure of the hydration layer do not
    currently exist.
The future of chemistry, broadly, depends on
    techniques that will map out the structure
    of the dynamic solvent that surrounds
    macromolecules.
The resulting insight will improve our ability
    to design drugs and synthetic materials.
In particular,
    by developing technologies that can map out the
    dynamic structure of hydration water,
    we unlock an ability to design drugs that bind to
    proteins currently deemed "undruggable,"
    we can understand the energetics that cause
    signaling proteins to bind to their partners,
    and design polymer materials that conduct water in
    unique ways.

Most chemists and biologists recognize one very
    simple example of hydration water:
the layer of water surrounding oil molecules
    that drive the separation of water and oil.
    But the more general case,
    especially for macromolecules that present a
    surface with variable properties to the solvent,
    is far more interesting and far less understood.

## How do Proteins Alter Nearby Solvent?

Proteins are the molecular motors
    that drive all life,
    and most drugs are designed to interact with
    proteins.
It is increasingly clear that water molecules
    at the surface of proteins control their
    structure and function;
    while researchers have developed methods that
    can study the structure of proteins,
    there are no accessible methods to spatially
    map the hydration water.
We develop and apply magnetic-resonance-based
    spectroscopic methods for routine, robust,
    and accessible measurements of the properties
    of these key hydration water molecules.

## A fundamental example

As a fundamental example,
    consider lipid bilayers
    -- structures that make up cell membranes.
Dr. Franck and his colleagues previously developed a specialized technique to
    characterize water near the bilayer surfaces.
Our technique
    -- called Overhauser Effect Dynamic Nuclear
    Polarization (ODNP) {% cite FranckPNMRS FranckMethEnz2018 %} --
    tracks the motion of the water nuclei,
    and allows us to zoom in on the
    "hydration water" near the surface of the lipid bilayer
    (figure below).
It allowed them to
    see that the hydration water moves about 5
    times slower than bulk water {% cite Franck_crowding %}.
Furthermore, by dramatically
    changing the characteristics of the bulk
    solution,
    we learned that
    an order of magnitude change in the viscosity
    barely affects the diffusion in the hydration
    layer {% cite Franck_crowding %}.
They have also implemented this technique
    in systems with membrane proteins {% cite Hussain2013 %},
    DNA {% cite Franck2015DNA %},
    and large protein folding chaperones {% cite FranckGroES %}.
The significant variations in the properties of the
    hydration water play in important role in how these surfaces
    interact in nature.

![Hydration layer](for_website_160809_labeled.png)

*This image illustrates ODNP of water in the hydration layer of a
    lipid bilayer.
This is one example of many studies that are possible with ODNP.
A lipid bilayer (the basis for cellular membranes) consists of a
    self-organized set of molecules with hydrophilic headgroups
    and hydrophobic tails (see labels above).
One can place a spin label (typically a nitroxide group)
    at a particular location near the surface of the lipid
    bilayer (via chemical synthesis).
A combination of electron- and nuclear-spin resonance
    (i.e. ODNP)
    can selectively interrogate the motion of water molecules
    at a specific location --
    here inside the hydration layer of
    the lipid bilayer.
For example, employing the setup shown above,
    we were able to verify that the motion of water molecules
    within the hydration layer was not sensitive to the presence
    of a high concentration of large molecules
    that are not chemically disposed to disrupt the hydration layer.
This was even true when the large molecules significantly altered the
    viscosity of the bulk solution {% cite Franck_crowding %}.*

## Current Research:

In the Franck lab, we currently push the limits of the ODNP technique to
	retrieve new and more detailed information about hydration water.
Towards this end,
    we draw on expertise in spectrometer design
    {% cite FranckBarnes2015 Kaufmann2013 Demas2009 %}
    and advanced magnetic resonance methods
    {% cite FranckFreed2015 Franck2009 %}.
We have already developed a cogent explanation
	of the ODNP technique {% cite FranckMethEnz2018 %},
	as well as a new, powerful, and general scheme
	for visualizing and processing magnetic resonance data {% cite BeatonCoherence2022 %}.
We are investigating the water on the insides of reverse micelles,
	which provide controllable pockets of water,
	as well as mapping out more subtle details in the water along the surface of proteins,
	both globular signaling proteins, as well as trans-membrane proteins.

When nanoscale aggregates such as reverse micelles isolate small pockets of
water, the resulting confinement alters the hydrogen bonding network; meanwhile,
the confinement also slows down the motion of the water molecules. These
effects result in a change (respectively) of the electron cloud density and of
the lifetime of the spin states, and magnetic resonance can measure both of
these. We have developed a measurement that reads out the *correlation*
between the hydrogen bonding strength and the rotational motion in confined
water pools. By measuring this correlation as a function of the size of the
water pool, we've identified a distinct inflection point at a couple
nanometers at which the water matrix changes dramatically.

We also employ mutagenesis to attach a spin label at a series of sites on the
surface of proteins, including cancer signaling proteins (KRas) as well as
transmembrane proton pumps (proteorhodopsin). This allows us to create a set of
samples that are primed for measurement of water at a series of different
sites, so that we can watch how the translational diffusivity of the water
changes as we move from site to site along the surface.

# References (Selected Publications)

[Link to Complete List of Publications](https://scholar.google.com/citations?user=TdqiwiIAAAAJ&hl=en&oi=ao){:target="blank"}

## Independent Research (Franck Lab, Syracuse University)

{% for pub in site.data.toc_figures %}
{% assign pub_key = pub[0] %}
{% assign pub_figure = pub[1] %}
{% capture pub_reference %}{% bibliography --query @*[key={{ pub_key }}] %}{% endcapture %}
<div class="pub-card">

<img src="{{ pub_figure }}" alt="TOC figure for {{ pub_key }}">

{{ pub_reference | replace: '">1. ', '">' }}

</div>
{% endfor %}

## Earlier Publications (PhD and Postdoctoral Work)

{% assign exclude_query = "" %}
{% for pub in site.data.toc_figures %}{% unless forloop.first %}{% assign exclude_query = exclude_query | append: " && " %}{% endunless %}{% assign exclude_query = exclude_query | append: "key!=" | append: pub[0] %}{% endfor %}
{% bibliography --cited_in_order --query @*[{{ exclude_query }}] %}
