"""
RSSCollection.py

Daniel Wang
May 2016
"""

import RSSFeed


class RSSCollection:
    def __init__(self, feeds):
        self.feeds = [RSSFeed.RSSFeed(feed[0], feed[1], feed[2]) for feed in feeds]

    def get_feeds_by_source(self, source):
        result = [feed for feed in self.feeds if feed.get_source() == source]
        return result

    def get_feeds_by_category(self, category):
        result = [feed for feed in self.feeds if feed.get_category() == category]
        return result
