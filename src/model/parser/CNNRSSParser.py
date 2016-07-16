"""
CNNRSSParser.py

Daniel Wang
May 2016
"""

from ..Article import Article
import RSSParser
import feedparser


def parse(link, src, enc='utf-8'):
    rss = feedparser.parse(link)
    result = []

    for entry in rss.entries:
        title = entry.title.encode(enc)
        desc = RSSParser.strip_html(entry.description.encode(enc))

        # remove 'Sponsored' in CNN sources
        spon_index = desc.find("Sponsored")
        if spon_index >= 0:
            desc = desc[0: spon_index]

        if is_empty_content(title) or is_empty_content(desc):
            continue

        article = Article(link, title, desc, src=src)
        result.append(article)

    return result


def is_empty_content(t):
    return 0 == len(t.replace(" ", ""))
