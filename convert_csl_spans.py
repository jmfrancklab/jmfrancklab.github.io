#!/usr/bin/env python3
"""Convert pandoc's markdown span-IAL syntax (``[text]{.class}``, no colon)
into literal HTML ``<span class="class">text</span>`` tags.

kramdown -- the markdown processor Jekyll uses for this site (see
_config.yml) -- does not understand pandoc's IAL dialect (kramdown's own
span-IAL syntax requires a colon: ``[text]{: .class}``). Left as pandoc
emits them, these spans show up as literal, unrendered bracket/brace text
on the published Research page. Converting to raw HTML sidesteps the
dialect mismatch entirely, since both pandoc and kramdown pass raw HTML
spans through untouched, and kramdown continues to parse markdown
(links, italics, etc.) inside span-level HTML such as <span>.

Only whole paragraphs that exactly match the citeproc reference-entry
shape (``[N. ]{.csl-left-margin}[... ]{.csl-right-inline}``) are touched,
so this can't accidentally swallow unrelated text elsewhere in the file.
"""
import re
import sys

REF_PATTERN = re.compile(
    r'^\[(?P<num>[^\[\]]*)\]\{\.csl-left-margin\}'
    r'\[(?P<body>.*)\]\{\.csl-right-inline\}$',
    re.DOTALL,
)
NOCASE_PATTERN = re.compile(r'\[([^\[\]]*)\]\{\.nocase\}')


def convert_paragraph(paragraph):
    match = REF_PATTERN.match(paragraph.strip())
    if not match:
        return paragraph
    body = NOCASE_PATTERN.sub(r'<span class="nocase">\1</span>', match.group('body'))
    return (
        f'<span class="csl-left-margin">{match.group("num")}</span>'
        f'<span class="csl-right-inline">{body}</span>'
    )


def main(path):
    with open(path) as f:
        text = f.read()
    paragraphs = text.split('\n\n')
    paragraphs = [convert_paragraph(p) for p in paragraphs]
    with open(path, 'w') as f:
        f.write('\n\n'.join(paragraphs))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'AAResearch.md')
