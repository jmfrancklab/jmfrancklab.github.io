---
layout: default
title: People
attribution: J. Franck
---
# {{page.title}}

{::options parse_block_html="true" /}
# Principle Investigator

<div class="mugshot">

![John](assets/JFgreytie_nobg.png)

## John M. Franck

John completed his PhD thesis under the guidance of
Prof. Alex Pines at Berkeley, studying sophisticated
methods of NMR pulse design and the development of
portable and transportable NMR instruments.
He worked as an Elings Prize Postdoctoral Fellow
(California NanoSystems Institute)
at the University of California, Santa Barbara,
under the guidance of Prof. Songi Han.
There, he developed new, sensitive technologies for investigating
the properties of water at the surfaces of proteins,
polymers, lipids, and DNA.
He completed further postdoctoral studies and served as a
research associate at the Advanced Center for the ESR
Technology Center (ACERT) at Cornell University,
under the guidance of Prof. Jack Freed.
There, he participated in studies that advanced the
forefront of high-field high-frequency pulse ESR;
techniques that provide detailed dynamic
characterizations of proteins and other biomolecular
systems.
These technologies are challenged only by difficulties
with probing samples that generated short-lived signal;
while at ACERT Prof. Franck pioneered
work that enabled detection of shorter-lived species than could
be proved previously.
After joining Syracuse as a PI and setting up his lab,
he received the NSF CAREER award (2021).

<!-- click to continue is here: https://stackoverflow.com/questions/28334540/truncate-text-in-html-with-link-to-show-more-less-and-keep-elements-inside-->

</div>

# Graduate Students

&nbsp;

{% for thisperson in site.people %}
<div class="mugshot">
## {{ thisperson.name }}
{{ thisperson.content }}
</div>
{% endfor %}

# Alumni

&nbsp; <!-- seems to be required to not gobble up next header -->

## Graduates and Postdocs 

### Alec Beaton

### Farhana Syed

## Undergraduates

| Natasha Prince | Natasha helped to refine our protocol for trans-membrane protocol expression, and worked on customized dialysis devices to precisely control the solvent environment. She graduated with distinction in chemistry, and has proceeded to graduate studies of Art Conservation and Forensics. |
| Conal Gallagher | Conal worked on the synthesis of small molecule spin labels.  After graduation, he joined a small startup in the Bay Area, followed by graduate studies in Forensics. |
| Jessica Khuc | Jessica worked with Farhana on generating multiple SDSL mutants of Ras. |
| Eldon Hard | Began our project on the simulation of microwave resonators.  Graduated and enrolled in the PhD program at USC. |
| Heta Desai (REU 2017) | Synthesized the small molecule spin label Cat-1, demonstrated its capture inside lipid vesicles, and demonstrated its saturation performance relative to aminotempo. |
| Isabela Ramirez       |  Worked briefly to initialize a project on mechanical automation of rf tuning and sample mixing. |
| Soliloquy Rhodes | Soliloquy (graduated 2019) worked on the synthesis of small molecule spin labels as well as the design of an automated temperature control system for use with saturation-level microwaves. |
| Michelle Sahagian | (Graduated 2019) worked on the synthesis of small molecule spin labels. |
