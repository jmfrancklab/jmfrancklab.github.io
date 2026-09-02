I received the following commentary from an expert, and want to make these updates.

*   The background should be a nice deep blue, since a lot of your research focuses on water. 

    > Done — `$background-color: #0a2540`.

    This color is good HOWEVER, for the color behind the main top/title image
    should be the same color as the rest of the background!!

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

    I disagreed with the expert here -- I liked the green glow.  You helped to
    edit the main title slide, but then you didn't adjust positioning
    appropriately, so that the title image png overlaps visually with the menu
    times underneath!!

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

*   The bottom left png image previously had an image with a gradient fade that
    was a picture of syracuse university.  Replace this instead with the ACERT
    image.  The ACERT image should also have a drop shadow (make and commmit an
    svg on your way to making the png!) generated from svg clone → black → 50%
    transparency and some blur, behind, and translate down and right
