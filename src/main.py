"""
main.py

Daniel Wang
May 2016
"""

import pipeline
from model import RSSCollection

if __name__ == "__main__":
    rss = [
        ("http://rss.cnn.com/rss/cnn_tech.rss", "cnn", "tech"),
        ("http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk", "bbc", "tech"),
        ("http://rss.cnn.com/rss/cnn_world.rss", "cnn", "world"),
        ("http://feeds.bbci.co.uk/news/world/rss.xml?edition=uk", "bbc", "world"),
        ("http://feeds.abcnews.com/abcnews/usheadlines", "abc", "us"),
        ("http://rss.cnn.com/rss/cnn_us.rss", "cnn", "us"),
        ("http://rss.nytimes.com/services/xml/rss/nyt/US.xml", "nyt", "us"),
        ("http://rss.cnn.com/rss/cnn_tech.rss", "test1", "t"),
        ("http://rss.cnn.com/rss/cnn_tech.rss", "test2", "t"),
        ("http://rss.cnn.com/rss/cnn_tech.rss", "test3", "t")
    ]

    collection = RSSCollection.RSSCollection(rss)

    feeds = collection.get_feeds_by_category("tech")

    pl = pipeline.RSSPipeline(feeds)

    m = pl.run()

    print(m)
