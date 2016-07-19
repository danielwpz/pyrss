"""
Article.py

Daniel Wang
May 2016
"""


class Article:
    title = ""
    description = ""
    content = ""
    src = ""
    link = None

    def __init__(self, link=None, title="", description="", content="", src=""):
        self.title = title
        self.link = link
        self.description = description
        self.content = content
        self.src = src

    def __str__(self):
        str = "%s[%s] - %s" % (self.src, self.title, self.description)
        return str.replace("\n", "")

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

    def set_title(self, title):
        self.title = title

    def set_description(self, desc):
        self.description = desc

    def set_link(self, link):
        self.link = link

    def set_content(self, content):
        self.content = content