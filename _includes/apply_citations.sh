#!/bin/bash
pandoc welcome_citations.md -f markdown -t markdown-citations --csl=../edited-pmid-format.csl --bibliography ../library_abbrev_utf8.bib -o welcome.md
sed -i 's/\^\([0-9,\\-]\+\)\^/<sup>\1<\/sup>/g' welcome.md
sed -i 's/~\([^~]\{0,10\}\)~/<sub>\1<\/sub>/g' welcome.md
sed -i '/^::: *$/d' welcome.md
sed -i '/^::: {#ref/d' welcome.md
sed -i 's/{#references-[^}]*}//' welcome.md
