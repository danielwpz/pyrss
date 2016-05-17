"""
RSSFeed.py

Daniel Wang
May 2016
"""

from parser import RSSParser


# Base rss feed class providing a general parse.
# Subclass shall do specific parse according to
# different sites.
class RSSFeed:
    articles = []

    def __init__(self, link, source, category):
        self.link = link
        self.source = source
        self.category = category

    def get_source(self):
        return self.source

    def get_category(self):
        return self.category

    def update(self):
        self.articles = RSSParser.parse_link(self.source, self.link)

    def get_articles(self):
        self.update()
        return self.articles
