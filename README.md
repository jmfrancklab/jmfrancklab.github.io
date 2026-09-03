# jmfrancklab.github.io

Source for the Franck Lab website (Jekyll, deployed via GitHub Pages).

## Editable content

Where to make day-to-day content edits, without touching layout/CSS:

| What | Where |
| --- | --- |
| Site title, contact email, description | `_config.yml` |
| PI bio (John Franck's own section) | `People.md` (hand-written, at the top) |
| Everyone else on the People page (grad students, alumni, undergrads) | `_data/people.yml` — one entry per person: `name`, `status` (`active`/`alumnus`), `level` (`PhD`/`Masters`/`postdoc`/`undergrad`), optional `photo` (path under `assets/`), and `description` (a YAML `\|` block for the bio paragraph(s)) |
| Research / Instrumentation / Software / Join the Lab pages | `AAResearch.md`, `Instrumentation.md`, `Software.md`, `Skills.md` (each is Markdown with a `title:` in its front matter — that's what shows in the nav bar and page heading) |
| Lab News posts | `_posts/` — one file per post, named `YYYY-MM-DD-slug.md` |
| Publications | `references.bib` (the library that's actually rendered on the Software/Research bibliography section via jekyll-scholar) — `library_abbrev_utf8.bib` is a separate, larger personal reference library, not the one the site renders |
| Photos, logos, and other images | `assets/` |
| Ongoing feedback / to-do log from site reviews | `INSTRUCTIONS.md` — running log of requested changes and what's been done for each |

## 1. Switch GitHub Pages to build via Actions

The site now needs jekyll-scholar to build the publications page, which
isn't in GitHub Pages' default-build plugin whitelist. A GitHub Actions
workflow (`.github/workflows/pages.yml`) builds and deploys instead — this
one-time switch has to be done in the GitHub web UI:

1. Go to the repo on github.com.
2. **Settings** → **Pages** (left sidebar, under "Code and automation").
3. Under **Build and deployment** → **Source**, change it from
   **"Deploy from a branch"** to **"GitHub Actions"**.
4. That's it — no branch/folder picker needed after that. The workflow
   triggers automatically on every push to `master`, and the "Actions" tab
   shows build/deploy progress and any failures.

## 2. Build and review locally before publishing

### One-time setup

Requires Ruby with headers to compile native gems (`ruby-dev` on
Debian/Ubuntu — `sudo apt install ruby-dev`).

`gem install --user-install` puts executables in a per-user directory that's
usually *not* on your `PATH` yet, so add it first — otherwise the `bundle`
command below won't be found. Add this line to your shell profile
(`~/.bashrc` etc.):

```bash
export PATH="$HOME/.local/share/gem/ruby/<ruby-version>/bin:$PATH"
```

(check the exact path with `gem environment | grep 'USER INSTALLATION DIRECTORY'`),
then either open a new terminal or run `source ~/.bashrc` so the current one
picks it up too. Then:

```bash
gem install --user-install bundler
bundle config set --local path 'vendor/bundle'
bundle install
```

(`vendor/bundle` and `.bundle/` are gitignored — this installs gems locally
into the repo without touching the system Ruby.)

### Build and serve

```bash
bundle exec jekyll serve
```

Then open **http://localhost:4000** in a browser. `jekyll serve` watches
the source and rebuilds automatically as you edit (refresh the browser
tab to see changes — no live-reload).

For a one-off build without serving (e.g. to just check it compiles
cleanly, or to inspect the generated HTML in `_site/`):

```bash
bundle exec jekyll build
```

Sass emits some `DEPRECATION WARNING` noise on every build — that's just
this project's SCSS using older syntax the current Dart Sass will
eventually stop supporting; it's not an error and doesn't affect output.

### Workflow

This repo is currently being edited on the `try_claude_for_editing` branch,
separate from `master` (what's actually deployed). To review and publish a
round of changes:

1. `git checkout try_claude_for_editing`, then build/serve locally as above
   and review in the browser.
2. When you're happy with it, merge into `master`
   (`git checkout master && git merge try_claude_for_editing`) and push.
3. The Actions workflow picks up the push to `master` automatically and
   deploys — check the **Actions** tab on GitHub for build status.
