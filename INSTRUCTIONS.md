I received the following commentary from an expert, and want to make these updates.

- Let's make some updates for people (these should be md and yml only now):
    - Atahan Garip is a current student from cornell aep. He is developing a fully open and automated temperature-controlled ODNP system.

      > Done — added as a PhD student (Cornell AEP) with his photo. Worded his
      > entry as "working with the Franck Lab at ACERT" rather than implying
      > you're at Cornell, per your follow-up.
- For the research, don't edit yet, but come up with a plan to break down the
  research: (1) temperature controlled ODNP (2) using spin physics to make
  low-field NMR better (understanding ODNP as well as the DCCT stuff) and (3)
  open instrumentation.  Here if you read (read only ~/git_repos/cv/ and find
  the most recent application package, you will find an NMR robotics pitch, as
  well as some new artwork that you can sue.
  For t-controlled ODNP, really reference reverse micelles as the model system we're using -- reference shathy and beaton below.
  I'm thinking actually, you can
  use this new logo, and pitch this first -- say it's a new initiative since I
  joined ACERT -- so this together with the 2 above, which are continuations,
  gives 3 research topics total, which is typical.

  > Done — per your follow-up, merged open instrumentation + spin physics
  > into one "Franck Magnetic Resonance Robotics" section (phase 1:
  > inexpensive/customizable/sensitive instrumentation, aligned with ACERT;
  > phase 2: DCCT/spin-physics for low-field NMR), pitched first as a new
  > initiative since joining ACERT, using the robotics logo from
  > ~/git_repos/cv/package/figures/toc_logo.png (copied to
  > assets/franck_robotics_logo.png). Temperature-Controlled ODNP in
  > Reverse Micelles kept as the second, continuing topic, now citing the
  > Shathy/Beaton preprints and Atahan's new instrument.

  I do not like the organization of this page -- it's not clear that it has
  several separate setions.  Perhaps a TOC at the top would be useful (with a
  concise recap sentence for each section)

  > Done — added an "On This Page" TOC right under the title, linking to
  > every section/subsection with a one-sentence recap each.

- Add collaborative independent work (with
  TOCs)  -- e.g. stuff i did with Zheng and just completed with Harrison in Segalman's group, as a seperate section.  Read-only look at ~/My\ Library.bib so that you are using the same bibtex keys (and for authoritative references, if needed).

  > Done for the Zheng papers (5 keys, pulled from ~/My Library.bib into
  > references.bib) — new "Collaborative Independent Work" section in
  > AAResearch.md. Found the Harrison one too, once you added it: it's
  > Landfield2026ChaDepLoc (Landfield, Zackin, Han, Franck, Segalman,
  > Shell — Langmuir 2026) — added to references.bib and this section.
  > Per your follow-up, sourced real TOC/graphical-abstract images (same
  > approach as the Independent Research cards, via PMC/NSF-PAR manuscript
  > copies) for 4 of 6: Chu2023InsAtoTra, Davis2019, Hofman2020,
  > Li2023IntBSiIon — now in `_data/collab_toc.yml`, rendered as cards.
  > Davis2021 (RSC) and Landfield2026ChaDepLoc (too recent, no open-access
  > copy) don't have a findable real graphical abstract yet — they still
  > render as plain citations below the cards; add a line to
  > `_data/collab_toc.yml` if/when you get an image for either.

  You should have/make TOC figures for the arxiv papers as well -- there is a
  TOC figure in the directory on this local computer ~/notebook/papers/RM_ODNP

  > Done for Beaton2023DirObsTra — used TOC_opt1.png (the square one, per
  > your pick over the wide TOC_opt2.png) from that directory, copied to
  > assets/TOC/Beaton2023DirObsTra.png, wired into a new
  > `_data/preprint_toc.yml` and rendered as a card like the other
  > sections. Found no TOC/graphical-abstract image anywhere locally for
  > the other preprint, Shathy2024ExcMicDyn — it still renders as a plain
  > citation; add a line to `_data/preprint_toc.yml` if you get one.

- You have several yml files for pubs with different categories of research.
  That's silly: use 1 yml with sections.

  > Done — replaced `_data/toc_figures.yml`, `_data/preprint_toc.yml`, and
  > `_data/collab_toc.yml` with one consolidated `_data/pub_toc.yml` (an
  > array of `{key, image, category}` entries, category being
  > independent/preprint/collab), filtered by category with Liquid's
  > `where` filter.

- I really dislike the organization of the research page. It should be
  organized by PROJECTS as we have been discussing.

  > Done, with a correction: re-reading this file's history, the original
  > ask was for 3 research topics (temp-controlled ODNP, spin physics for
  > low-field NMR, open instrumentation), with open instrumentation
  > reframed as the new-initiative "robotics" pitch. The earlier pass above
  > had incorrectly merged spin physics + instrumentation into one combined
  > "Franck Magnetic Resonance Robotics" section (2 sections total) — split
  > back into 3 separate `###` sections under Current Research: Open
  > Instrumentation (New Initiative), Spin Physics for Low-Field NMR
  > (Continuing Program), Temperature-Controlled ODNP in Reverse Micelles
  > (Continuing Program). On This Page TOC updated to match.

- You have not yet separated research from publications: research has
  citations, but they are normal citations, not the publication listing
  w/ TOCs.

  > Done — moved the entire "References (Selected Publications)" section
  > (Independent Research / Preprints / Collaborative Independent Work /
  > Earlier Publications, all TOC-card rendering) out of AAResearch.md into
  > a new Publications.md page, with its own "On This Page" TOC. AAResearch.md
  > now only has narrative content with normal inline `{% cite %}`
  > citations; a pointer sentence links to the new Publications page.

- Several problems from testing the above: (1) the Beaton2023DirObsTra TOC
  image was actually still the gray "TOC Graphic option 1 max 5.5x5.0 cm"
  placeholder, never replaced with a real graphic, and no TOC was ever
  attempted for the Shathy preprint; (2) arXiv citations render "[Internet]"
  instead of a real link (bad CSL support for arXiv); (3) "Earlier
  Publications" rendered completely empty; (4) some collaborative papers are
  still missing TOC images.

  > Done for (1): found the real graphic at
  > ~/notebook/papers/RM_ODNP/figures/TOC.png (the previously-used
  > TOC_opt1.png was itself just a leftover journal-template placeholder,
  > not real artwork) and copied it in. Per your follow-up ("go online and
  > get those" / "create one for Shathy from content.md and its figures"):
  > Shathy2024ExcMicDyn now uses the "cold-shedding" scheme
  > (~/notebook/papers/RM_ESR/Figures/water_shedding_scheme.png, per your
  > pick) since no journal ever required a graphical abstract for an arXiv
  > preprint. Landfield2026ChaDepLoc's real Figure 1 (a designed ODNP/
  > protonation-state concept graphic) was recovered from the DOE OSTI
  > public-access copy (osti.gov/servlets/purl/3377616 -- BES-funded,
  > DE-SC0019272) since ACS blocks direct/Semantic-Scholar/PMC access.
  > Davis2021: RSC blocked all automated access attempts (Cloudflare,
  > including the CrossRef "syndication" PDF link), and its NSF-PAR
  > accepted-manuscript copy had no dedicated graphical abstract, only
  > dense multi-panel data figures unsuitable for a TOC card -- resolved
  > once you supplied the real published graphical abstract directly, now
  > in `assets/TOC/Davis2021.png`. (4) is now fully closed -- every entry
  > in `_data/pub_toc.yml` has a real `image:`.
  > Done for (2): `edited-pmid-format.csl`'s title macro now suppresses
  > "[Internet]" when `archiveprefix` is present, and `_layouts/bibliography.html`
  > appends a real `arxiv.org/abs/...` link (matching the existing doi/PMID
  > pattern).
  > Done for (3): root cause was `--cited_in_order` on that query, which
  > also silently sets jekyll-scholar's "cited only" flag -- restricting to
  > entries already referenced via `{% cite %}` elsewhere on the site, which
  > none of the plain "earlier" listing entries are. Removed that flag.

- Another CSL problem: citations show "[cited 2023 Dec 20]" access dates --
  no one wants to see that.

  > Done — `accessed-date` in `edited-pmid-format.csl` (called from the
  > `date` macro for journal articles, patents, and the default/preprint
  > case) now renders nothing instead of "[cited YYYY Mon DD]".

- The research page is a mess -- expected one intro section then 3 clear
  projects (one being the new robotics project), but got 2 different-styled
  UL lists and what looked like two levels of organization. Also, don't say
  "Continuing Program" (obvious, since they're not "new"). Also, the
  robotics logo should be small (~30% of text width) with a line
  separating that section, and should float on the right with text
  wrapping around it (mirroring, on the other side, the headshot/text-wrap
  pattern on the People page).

  > Done — flattened the page to one TOC list at a single heading level:
  > Background (intro, merged the 3 old background subsections into one),
  > then the 3 projects as co-equal `##` sections (no more nested
  > "Current Research" umbrella), dropping "(Continuing Program)" from
  > both headings. Added `.project-logo`/`.project-logo-wrap` (float:
  > right, max-width 30%, mirrors `.mugshot`'s float-left pattern) and a
  > `.section-divider` `<hr>` before the Open Instrumentation section.

- The research page should have its own "References" section, with
  citation numbers specific to this page (not shared with the Publications
  page's numbering); put an hline in the outline between the intro and the
  3 projects, and between the projects and References; don't put the
  gscholar link here -- instead a centered link to this site's
  Publications page (gscholar is reachable from there).

  > Done — added `## References` with `{% bibliography --cited_in_order %}`
  > (jekyll-scholar's citation-number is scoped per-page via `page['cited']`,
  > confirmed FranckPNMRS numbers as 1 on this page vs. 6 on Publications.html)
  > and a centered link to Publications.html underneath. Added `<hr>`
  > dividers in the "On This Page" outline splitting it into the 3
  > described groups.

- The Shathy TOC choice (cold-shedding scheme) was no good -- it makes the
  paper look like it's exclusively about cold shedding. Use one of the
  reaction/flowchart cartoons instead.

  > Done — swapped to `Figures/TEMPOSO4_Reaction.png` (the TEMPO-SO4
  > synthesis scheme), simpler and cleaner at pub-card thumbnail size than
  > the 2-row CAT-16 alternative.

- "Earlier Publications" (and every subsection on the Publications page)
  should be sorted in reverse chronological order.

  > Done — the per-key `{% bibliography --query key=X %}` loops for
  > Independent Research/Preprints/Collaborative Independent Work couldn't
  > be sorted (jekyll-scholar only sorts across entries within a single
  > bulk query), so switched each to one bulk `--query key=A || key=B...`
  > call, with a new `bibliography_card` layout that looks up the image
  > from `_data/pub_toc.yml` (via `entry.key`) and wraps in `.pub-card`
  > only when a `--template` override requests it -- so the plain
  > `bibliography` layout (used for Earlier Publications and the Research
  > page's References) is untouched. Set `scholar: {sort_by: year, order:
  > descending}` in Publications.md's front matter (page-scoped, confirmed
  > it doesn't affect AAResearch.md). Citation numbers are now real,
  > per-section sequential numbers reflecting the sorted order, instead of
  > the old hack that stripped a fake "1." from every card.

