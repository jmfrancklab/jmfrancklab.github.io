#!/bin/bash
pandoc AAResearch_citations.md -f markdown -t markdown-citations --csl=edited-pmid-format.csl --bibliography library_abbrev_utf8.bib -o AAResearch.md
# add the header, which gets omitted
{ head -5 AAResearch_citations.md; cat AAResearch.md; } > AAResearch.md.new
mv AAResearch.md.new AAResearch.md
sed -i 's/\^\([0-9,\\-]\+\)\^/<sup>\1<\/sup>/g' AAResearch.md
sed -i 's/~\([^~]\{0,10\}\)~/<sub>\1<\/sub>/g' AAResearch.md
sed -i '/^::: *$/d' AAResearch.md
sed -i '/^::: {#ref/d' AAResearch.md
sed -i 's/{#references-[^}]*}//' AAResearch.md
