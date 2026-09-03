I received the following commentary from an expert, and want to make these updates.

*   The background should be a nice deep blue, since a lot of your research focuses on water. 

    > Done — `$background-color: #0a2540`.

    This color is good HOWEVER, for the color behind the main top/title image
    should be the same color as the rest of the background!!

    > Done — `$top-bg-color` was a separate, slightly different navy
    > (`#071829` vs. the page's `#0a2540`); it now just aliases
    > `$background-color` so there's no seam.

    After adjustment, there is a problem where there's a weirdly darker band
    above and below the subheader bar -- this darker region wraps around the
    right side of the title.  See the next point -- you want to resolve
    together with this.

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

    Now the header is TINY.  It should be 80% of the main white text area.
    When the view is very narrow, as on some mobile screens, then it should
    fill 100% of the width (and of course should scale down to match as the
    screen is made even more narrow).

    > Done — `.title-image` is now 80% of `.decoration`'s width (100% below
    > the `$on-palm` breakpoint), taken out of normal flow (`position:
    > absolute`) so it can still overflow `.decoration`'s bottom edge
    > without stretching that box; `.decoration`'s height now tracks its own
    > width via `aspect-ratio` instead of a fixed px value, so the "stops
    > just under the lettering" alignment holds at every width. Also had to
    > override `max-width` on `.title-image` directly -- the global `img {
    > max-width: 80% }` rule was otherwise clamping it back down regardless
    > of the `width` set here.

    Now, you've violated the earlier instructions about where the lettering
    should fall.  The lettering overlaps the naviation bar underneath!!!

    > Measured this in a fresh browser at 320–1400px — letters stay inside
    > the box at every width I can reproduce. The dev server was stale (see
    > note below) — please hard-refresh and let me know if it's still wrong,
    > ideally with the viewport width/browser where you see it.

*   Research page - You explanations for what you do are really good and easy
    to understand for someone not familiar with this. I would include more
    visuals. The one you have is good, but you might want to label the bulk
    layer for people.

    > Bulk-water label: done, added directly to the existing figure. I also
    > tried adding two new figures (reverse micelle, KRas) for the newly-
    > relocated homepage paragraphs — you flagged you didn't want those, so
    > I removed them; the paragraphs are still there, just text-only now.

*   People - I would make the photos larger and have people include info about themselves. 

    > Photos: done (90px to 180px). Bios: not expanded — I didn't want to
    > invent personal details about real people. If you or the students want
    > to send a couple sentences each, I'll add them.

    Now, the photos are too large! Go for 120 px

    > Done — 180px → 120px.

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

    You should now remove the central acert logo, which is redundant also
    rescale the left logo to 70% of its current size.

    > Done — removed the `<td class="middle">` cell (and its now-unused
    > `.middle` CSS) from the footer. `.left-image` is 70% of its previous
    > size (`max-width: 56%`, i.e. 70% of the global `img` rule's 80%).

    You didn't resize the remaining ACERT logo like I asked! 50% of its current
    size!!

    > It was actually at 56% (verified via computed style) — sizing it
    > further to 28%, i.e. 50% of that.

-   Throughout, replace jmfranck@syr.edu (or [at] ) with
    john.m.franck@acertcenter.org

    > Done — `_config.yml`'s `site.email` (the only place it was defined;
    > `footer.html` already just references `{{ site.email }}`).

    This is not true! It's still a problem on the bottom right of all the pages!!!
    Also, remove the ref to my faculty page!!

    > The site.email config value was actually fixed — the running dev
    > server just hadn't reloaded `_config.yml` since (it only reloads on
    > source-file changes, not config changes), so it kept serving the old
    > email. Restarted it. Faculty page link removed from the footer.

-   Under People.md, it's OK to have me in my own section, but everyone else
    (including the undergrads in the table) should be in the same yaml file,
    with the full name (also the figure caption), description paragraph (pipe-continued-string-like), and
    photo, all structured as dict-like attributes under one header.
    The current status (active vs. alumnus) and level (PhD, Masters, undergrad,
    postdoc -- note that active converts to current XXX student) should all be
    attributes, as well.

    > Done — new `_data/people.yml`, one dict per person (`name`, `status`,
    > `level`, optional `photo`, `description` as a `|` block). Replaced the
    > old `_people/*.md` collection (deleted those 3 files and the
    > `collections: people:` entry in `_config.yml`) and the hardcoded
    > undergrad table. `People.md` now loops over `site.data.people`,
    > filtered by `status`/`level` into the same three sections as before
    > (Graduate Students / Graduates and Postdocs / Undergraduates), and
    > derives the displayed label from status+level ("current PhD student"
    > for active, "PhD"/"MS"/"Postdoc" for alumnus). I did not have a
    > reliable source for Alexandria Guinness's, Romana Shathy's, or Warren
    > Kincaid's exact degree program, so I defaulted all three current
    > graduate students' `level` to `PhD` in the data file — please correct
    > any that should be `Masters`. Also noticed while testing: the
    > `.mugshot` float layout lets a photo visually spill into the next
    > person's entry when the bio text is shorter than the photo (pre-
    > existing, not something this change introduced — same div/float
    > structure as before) — flagging in case you want it fixed separately.

    I'm not reading your very verbose description above!

    Before, the undergrads were in a nice table, and you ruined this!
    I do want the info in a yaml, bu thte undergrads should still be in a table!

    > Done — undergrads are back in a table, generated from
    > `_data/people.yml` instead of hardcoded.

-   The readme should have a section dedicated to listing the important editable data and text sources.

    > Done — added an "Editable content" section near the top of
    > `README.md` with a table of what to edit for common changes (site
    > config, People page, other content pages, Lab News posts,
    > publications, images, and the `INSTRUCTIONS.md` feedback log).

-   We want to sort the publications into independent vs. not, and I want you
    to go get the TOC figures for all the independent publications, put them in
    a TOC subfolder of assets, and have a yaml file that associates them with
    the relevant key so they can be used.
    Arrange the citation and the TOC figure together in a format similar to how
    you have done the news items.
    This is complicated enough that you should handle this request in its own
    turn -- explicitly say you're waiting to do this if there are other
    unresolved things in this document.
-   There is a full line of whitespace under each of the images -- this is
    weird, and the text should be wrapping to fill that space.
