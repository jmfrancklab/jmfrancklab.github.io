I received the following commentary from an expert, and want to make these updates.

*   The background should be a nice deep blue, since a lot of your research focuses on water. 

    > Done — `$background-color: #0a2540`.

*   Homepage - The name would look better without the green outline and you
    need to make the nanoscale view more prominent. I am not sure what image
    there, but maybe a larger one that shows a water molecule? Also, labels to
    explain each slide in the slideshow would be useful.

    > Slide labels: done. Nanoscale-more-prominent: done, properly this time
    > — you hand-edited `header_only.svg` to wrap the subtitle into a
    > justified two-line block, I fixed a hidden-background-layer bug, wired
    > up the two missing raster images (`nitroxide.png`/`water.png`, now in
    > `assets/`), re-rendered the PNG, and resized the CSS to match. Green
    > outline on "The Franck Lab": now done too — the title was 4 stacked
    > colored copies of the same text (black shadow, cyan, yellow, white);
    > the cyan+yellow layers together are what read as green. Removed just
    > those two, kept the black drop-shadow + white text. Subtitle's own
    > glow left as-is.

*   You should keep things brief on the homepage and just make a quick summary
    of research and opportunities on this page. You can then link it your other
    pages where you go into more detail.

    > Done — `welcome.md` is now a couple short paragraphs plus links out to
    > Research/Join the Lab/People.

*   Research page - You explanations for what you do are really good and easy
    to understand for someone not familiar with this. I would include more
    visuals. The one you have is good, but you might want to label the bulk
    layer for people.

    > Bulk-water label: done, added directly to the existing figure. I also
    > tried adding two new figures (reverse micelle, KRas) for the newly-
    > relocated homepage paragraphs — you flagged you didn't want those, so
    > I removed them; the paragraphs are still there, just text-only now.

*   Instrumentation - You might not need this page since I assume these will part of ACERT 2.

    > Kept, per your answer.

*   People - I would make the photos larger and have people include info about themselves. 

    > Photos: done (90px to 180px). Bios: not expanded — I didn't want to
    > invent personal details about real people. If you or the students want
    > to send a couple sentences each, I'll add them.

*   Skills - I would change this to your recruitment page. The Franck Lab is looking for . . . . 
    Could list the different skills involved in the lab and types of research offered for undergrads and grads.

    > Done — retitled "Join the Lab," lists skills/opportunities for grad +
    > undergrad, uses your "open to working with talented graduate students,
    > undergraduate researchers, and postdocs" phrasing (no specific term).

*   Lab News - Maybe improve the layout to highlight things better.

    > Done — card layout with title/date/excerpt per post instead of a flat
    > dump of full post content.

Also, it's supposed to pull the list of publications from a bib (or yaml, I
forget) file (built by Jekyll) and the formatting currently doesn't work
correctly.

> It's a `.bib` file (`references.bib`) — there's no yaml, and Jekyll was
> never actually building this (no plugin/gem for it ever existed in this
> repo's history). The real pipeline: `apply_citations.sh` runs pandoc
> against `references.bib` and commits a static, pre-expanded `AAResearch.md`
> — Jekyll just renders that file like any other page. The formatting bug
> was pandoc emitting its own span-attribute syntax that kramdown (Jekyll's
> markdown engine) doesn't understand, so it printed literal brackets/braces
> instead of a formatted list. Fixed the actual bug (converts to real HTML
> spans now) and verified it renders as a proper hanging-indent numbered
> list with working DOI/PMID links. You separately asked to go further and
> have Jekyll genuinely build this from the `.bib` on every deploy via
> GitHub Actions + jekyll-scholar — that infra work (Gemfile, workflow file,
> `_config.yml` scholar block, converting `citeproc_src` to live `{% cite %}`
> tags) is still pending; want me to proceed with it, or is the current
> (now-working) pandoc pipeline good enough?

Finally, change all of the Syracuse branding to ACERT branding (including changing the syracuse to ACERT 501(c)3).
I have supplied acert_logo.svg that you can use to replace the syracuse logo,
and you're encouraged to convert this to png if you think it would give better
display/faster rendering.

> Done — footer's Syracuse Seal replaced with `acert_logo.png` (converted
> from your svg), and the nav/link accent color changed from Syracuse orange
> to ACERT red (`#df0909`, pulled from the logo). Left the "JMF Faculty Page"
> footer link and the Syracuse campus photo alone — those read as factual/
> institutional rather than decorative branding to me. Flag if you want
> those changed too.
