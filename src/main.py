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
        ("http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk", "bbc", "tech")
    ]

    collection = RSSCollection.RSSCollection(rss)

    feeds = collection.get_feeds_by_category("tech")

    pl = pipeline.RSSPipeline(feeds)

    m = pl.run()
    # print(m)
