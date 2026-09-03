I received the following commentary from an expert, and want to make these updates.

*   The background should be a nice deep blue, since a lot of your research focuses on water. 

    > Done — `$background-color: #0a2540`.

    This color is good HOWEVER, for the color behind the main top/title image
    should be the same color as the rest of the background!!

    > Done — `$top-bg-color` was a separate, slightly different navy
    > (`#071829` vs. the page's `#0a2540`); it now just aliases
    > `$background-color` so there's no seam.

-   I've edited the header_only.svg again.  You need to convert it to a png,
    and then work on positioning.  Very specifically, the dark blue top
    background should come to just under the bottom of the white letters.  In
    this way, the drop shadow of the letters, as well as a decent portion of
    the molecule on the left will hang off, and appear to shade the region
    underneath.  In particular, because the molecule is lower than the text, it
    will overlap some with the section text underneath, which is desired, and
    provides design flow as well as some z-depth to the page.

    > Done — re-rendered `header_only.png` from your edited svg (650x114,
    > up from 650x226; the new layout is much more compact). Set
    > `.decoration`'s height to 30px, which lands right under the bottom of
    > "the Franck lab" lettering — the shadow, subtitle, and the lower part
    > of the molecule icon hang off underneath and overlap the nav row, as
    > you described. This only reads cleanly because the previous fix (top
    > image background = page background) removed the seam it would
    > otherwise cut across.

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

    > Done — new `assets/acert_logo_shadow.svg`, built from your
    > `acert_logo.svg`: a cloned copy is run through an SVG filter
    > (feColorMatrix to flatten it to black at 50% alpha, then
    > feGaussianBlur), offset down-and-right, and painted behind the
    > original. Rendered to `assets/acert_logo_shadow.png` and wired into
    > the footer in place of `syracuse_campus.png` (left that file alone —
    > `basic.html`, an old unused test page, still points at it).

*   The background was supposed to have a subtle effect like a screensaver
    where equations fade lightly in and out.  This was working at some point
    (in history), then you broke it so that everything was shoved in the upper
    left, and now I don't see it at all.

    > The "shoved in the upper-left" part was already fixed (the cached
    > template equations were being kept off-screen at -9999px, and each
    > visible clone did get its own random position). The "don't see it at
    > all" part was real, though: `.fading-equation` was `#303030` — almost
    > the same darkness as the `#0a2540` background, so it was rendering,
    > just invisible. Changed it to a light, semi-transparent blue-white
    > that's actually readable against the deep blue while staying subtle.
