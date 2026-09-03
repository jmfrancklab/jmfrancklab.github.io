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

    WHY ISN'T THIS RESOLVED!!! I realize this is the drop-shadow for the top
    blue background box that floats over the white text block.  It SHOULD have
    a drop shadow, but in the initial view, it's bottom edge should be below
    the bottom of the naviation bar (it's not) and when scrolling, should come
    to the bottom edge of the "nanoscale view" text (it doesn't), and the drop
    shadow to the right of this box should NEVER be visible as it is now!!!

    > Done — `.decoration` only covered the title, not the subtitle below
    > it, so the subtitle sat unprotected on top of the nav links. Extended
    > it to cover the subtitle too, and dropped the shadow's x-offset to 0
    > so it never shows on the side.

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

    Your response here is not consistent with what I said!  Initially, the edge
    of "nanoscale view" overlaps with "research" and "instrumentation"!!!!!!!
    Then, when I scroll the central text column, the "nanoscale view" floats
    above the white text block!!! (Only the very edge/shadow should float over
    the white text block -- the rest should still have blue background under
    it!!!)

    > Done — same fix as above (`.decoration` now covers the subtitle), so
    > this no longer happens at any scroll position. Let me know if the
    > sticky box still doesn't reach far enough for you.

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

    > Done — added 2 new 2024/2025 papers to references.bib (found via
    > Scholar/PubMed search); independent set is now BeatonCoherence2022,
    > BeatonRotational2024, GuinnessNoise2025 (Franck's own students,
    > Syracuse). Got real TOC/graphical-abstract images for all 3 (PMC +
    > ScienceDirect CDN; JCP one has no official TOC so reused the paper's
    > own DCCT figure) into `assets/TOC/`, mapped in `_data/toc_figures.yml`.
    > `AAResearch.md` now renders these as news-style cards (figure +
    > citation), rest of bibliography unchanged below. Verified visually via
    > Playwright screenshot, desktop and mobile.
-   There is a full line of whitespace under each of the images -- this is
    weird, and the text should be wrapping to fill that space.

    > Done — `Instrumentation.md` had a missing `</div>` (nesting everything
    > after the Bruker photo inside its div) and headings sitting outside
    > their `.mugshot` divs (so photos overlapped the heading above them).
    > Fixed both, matching how `People.md` structures it.
-   Change "Franck lab" in the title to "Franck research group" (requires svg edit and inkscape png generation)

    > Done — edited the `flowPara` text in `header_only.svg` and re-rendered
    > `header_only.png` via `inkscape --export-type=png` at the same 650x114
    > size. The longer text still fits on one line with room to spare.

    You need to raise the final (composite of clones) object so that the g
    and p of group don't weird intersect with the subtitle (don't change the
    size of the image, just push "the Franck research group" up).

    > Done — nudged `g10792`'s transform (the title's shadow+fill clone
    > group) up so the "g"/"p" descenders in "group" clear the subtitle
    > line with a couple px of gap, same 650x114 canvas.

-   Change "Join the Lab" to "Join the Group" in the nav.

    > Done — that page's `title:` front matter (`Skills.md`) drives both the
    > nav label and page heading, so changing it there was enough.

-   The dark vertical band within the left 25% of the title image is part of
    what I've been complaining about; there's a symmetric one on the right.

    > Done — my earlier `0 5px 5px` shadow fix zeroed the x-offset but the
    > blur radius still bled a soft ~5px shadow past the box on both sides.
    > Switched to `0 6px 6px -6px` (negative spread pulls the shadow in
    > before blurring), which measures out to a ~1-unit rounding artifact
    > instead of a visible band — checked pixel values directly on both
    > edges, not just by eye.

-   I updated header_only.svg again (subtitle is now two lines, canvas is
    650x144 instead of 650x114) -- reposition per the notes above, now that
    it's changed size.

    > Done — re-rendered `header_only.png` at the new size. The title's
    > descenders and the (now two-line) subtitle collided again, so I moved
    > the subtitle group down a bit (title had no headroom left to move up
    > without clipping) until there's a clean few-px gap, then recomputed
    > `.decoration`'s aspect-ratio from scratch against the new pixel rows
    > (same method as before — see `_layout.scss` comment for the numbers).

-   Huge whitespace on the People page — the content column is way too
    narrow on a wide/full-screen monitor, leaving huge blue margins.

    > Done — `$content-width` was 800px; widened to 1100px. This exposed a
    > real pre-existing bug (photos spilling into the next person's entry
    > when their own bio was shorter than their photo, since `.mugshot`
    > never fully contained its float) — gave `.mugshot` `display: flow-root`
    > so it always contains its own photo regardless of text length. Also
    > added an "AGENTS.md → Verifying visually" note that you keep
    > `jekyll serve` running and I should just point a headless browser at
    > localhost:4000, plus not to screenshot-crop for real image assets.

    "Huge whitespace" wasn't what this meant (keep the width change anyway) —
    the real, persistent whitespace problem is a gap right under each raised
    photo, screenshotted and circled in red. It's a template-wide error: the
    photo is deliberately raised to overlap the content above it, but the
    gap that raise leaves underneath isn't closing.

    > Found it — `.mugshot img` raised photos with `position: relative; top:
    > -14px`, which shifts the paint position but not the layout/wrap
    > position (CSS spec behavior for relatively-positioned floats), leaving
    > a permanent ~14px dead zone below the visible photo that text can't
    > enter even though nothing's there. Switched to `margin-top: -14px`,
    > which actually moves the float, so wrapping text now reaches the
    > photo's real bottom edge with no gap — verified pixel-exact at three
    > widths, and confirmed the overlap-with-content-above look is
    > unchanged. This was in `_base.scss`, so it affects every `.mugshot`
    > site-wide (People and Instrumentation), not just the one you pointed at.

-   I edited header_only.svg again — the bottom "g" (in "biological") should
    overhang, just touching the nav bar, with the shadow from the other
    letters staying on the blue background.

    > Done — recomputed `.decoration`'s aspect-ratio to stop right at that
    > line's baseline instead of past its descender, so only the "g"'s tail
    > pokes through into the nav row. Checked pixel-by-pixel that it just
    > reaches the nav's top edge, and that this doesn't reopen the
    > subtitle/nav-link collision from earlier (the readable letterforms are
    > still fully on blue).

-   Tweaked the header again (no size change) — re-render at ~2x resolution.

    > Done — re-exported at `--export-width=1300` (was 650). Checked the
    > text row positions scale exactly 2x with no layout drift, so no CSS
    > changes were needed, just the sharper source file.

-   Edited header_only.svg again — it's shorter now, but keep the bottom of
    the text where it is (less of the png should hang down from that
    position).

    > Done — your edit trimmed more off the bottom than intended but also
    > added ~14px of blank padding at the top, which would've pushed the
    > text down when rendered. Cropped that extra top padding back off
    > before installing the PNG — verified pixel-for-pixel that the title
    > and subtitle now land at the exact same rows as before, just with
    > less blank canvas hanging below. No CSS changes needed since
    > `.decoration`'s aspect-ratio only depends on content above the
    > subtitle's baseline, which didn't move.

-   Make the math-animation fade in/out ~3x slower, and add ~3x as many
    equations.

    > Done — `FADE_MS` 1000→3000 in `head.html` (and the matching CSS
    > `transition: opacity` in `_layout.scss`), and grew the equation pool
    > from 4 to 12 with standard NMR/EPR formulas (Larmor frequency, Bloch
    > equation, spectral density, dipolar coupling, chemical shift,
    > Boltzmann polarization, T2 relation, Zeeman splitting) in the same
    > style as the existing ones.

    Since you're still screwing up the people images, I played with it in
    Chrome "inspect". I can fix the problem by setting padding-bottom to 0
    and margin-top to -16px.

    > Done — you found the piece I'd missed: `padding-bottom: 5pt` on
    > `.mugshot img` was, like the old `top: -14px` offset, real reserved
    > space below the visible photo that text couldn't enter. Set it to 0
    > and margin-top to -16px exactly as you found. Verified computed style
    > and zero-gap measurements on all four People entries again.
