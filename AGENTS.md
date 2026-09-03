# Working with this repo

## INSTRUCTIONS.md is the task queue

`INSTRUCTIONS.md` is a running log of feedback from the site owner. Read it
at the start of any session touching this repo, and work through unresolved
items with as little back-and-forth as possible — don't wait to be told
which item to do next.

Format convention:
- Unquoted paragraphs are the owner's requests/feedback.
- `>` blockquotes immediately following a request are **your own** past
  responses (written by a previous session), describing what was done.
- Unquoted text *after* one of those blockquotes, still under the same
  bullet, is the owner replying to that specific response — almost always
  because it wasn't satisfied (wrong result, misunderstood ask, regressed
  something else). Treat it as unresolved and fix it; don't treat the
  presence of a `>` block as proof the item is done.
- When you finish an item (including a re-try after a correction), append
  your own new `> Done — ...` blockquote right after the text you're
  responding to, in the same style as existing ones.

Keep these blockquote responses **terse** — one line, maybe two. Do not
write multi-bullet breakdowns of everything you touched; the owner reads
these as a changelog, not a report. If there's something the owner
specifically needs to know or decide (an assumption you made, a tradeoff),
say that in one sentence, not a paragraph.

## Before concluding something is "still broken"

If a fix looks correct in the source but the owner says it's not showing
up, check for these before re-editing code that's actually already right:
- **The dev server needs a restart after any `_config.yml` change.**
  `jekyll serve --watch` re-renders on file changes but does *not* reload
  `_config.yml` — it keeps using whatever `site.*` values were loaded at
  startup. If a `_config.yml` edit (e.g. `site.email`) doesn't show up
  after a rebuild, kill and restart the `jekyll serve` process.
- A generic tag-selector CSS rule (e.g. the global `img { max-width: 80% }`
  in `_sass/_base.scss`) can silently re-clamp a more specific `width` rule
  you just added, because `width` and `max-width` don't override each
  other. If a size change appears to do nothing, check computed style for
  a competing rule on the same property before assuming your change was
  wrong.
- Verify visually (screenshot or computed-style check via a headless
  browser) rather than just re-reading the CSS, when a report contradicts
  what the source says it should do.

## Verifying visually

The owner runs `bundle exec jekyll serve` (or similar) themselves and
normally leaves it running at `http://localhost:4000` throughout a session.
Don't try to start, stop, or manage that process yourself — just point a
headless browser at `http://localhost:4000` directly to check a change.
System Chromium is installed at `/usr/bin/chromium`; with `playwright`
(already installed), pass `executable_path="/usr/bin/chromium"` to
`chromium.launch()` (the bundled Playwright browser binary is not
installed, so a plain `chromium.launch()` with no args will fail).

If `http://localhost:4000` isn't responding, don't work around it (e.g. by
running your own `jekyll build`/`serve` in the background, or by reasoning
about the compiled output some other way) — stop and ask the owner to start
their dev server, then continue once it's up.

When extracting an actual image asset (e.g. a figure from a publisher's
page) rather than just checking layout, fetch the real image URL directly
(inspect the page's HTML/meta tags for it) — don't screenshot-and-crop a
rendered page section as a substitute; that produces a blurry, low-quality
result, not the actual asset.

## Branch workflow

Work happens on `try_claude_for_editing`, not `master` (see README.md
"Workflow" section). Nothing is visible on the deployed site until it's
merged into `master` and pushed — keep that in mind before assuming a
"still broken on the live site" report is about this branch's code.
