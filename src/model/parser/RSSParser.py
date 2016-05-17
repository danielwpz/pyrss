"""
RSSParser.py

Daniel Wang
May 2016
"""


from CNNRSSParser import parse as cnn_parse


def __default_parse(link, src):
    return cnn_parse(link, src)


__parser_map = [
    ("", __default_parse),
    ("cnn", cnn_parse)
]


def parse_link(source, link):
    for item in __parser_map:
        if item[0] == source.lower():
            return item[1](link, source)

    return __parser_map[0][1](link, source)


def strip_html(h):
    p = ''
    s = 0
    for c in h:
        if c == '<': s = 1
        elif c == '>':
            s = 0
            p += " "
        elif s == 0: p += c

    return p
