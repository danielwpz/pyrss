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

        if is_empty_content(title) or is_empty_content(desc):
            continue

        article = Article(link, title, desc, src=src)
        result.append(article)

    return result


def is_empty_content(t):
    return 0 == len(t.replace(" ", ""))
