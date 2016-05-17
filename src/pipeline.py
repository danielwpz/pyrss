"""
pipeline.py

Daniel Wang
May 2016
"""

from model import Splitter
import math
from ml import feature
from ml import nmf
import numpy


def get_tfidf(word, article_words, i):
    tf = article_words[i][word] * 1.0 if article_words[i].get(word) is not None else 0.0

    art_cnt = len([a for a in article_words if a.get(word) is not None])
    n = len(article_words)
    idf = math.log(1.0 * n / art_cnt)

    return tf * idf


class RSSPipeline:
    source = []  # RSSFeed sources
    engine = None  # Context-free clustering engine

    # default values
    word_splitter = Splitter  # word splitter

    def __init__(self, source=[], engine=None):
        self.source = source
        self.engine = engine

    def run(self):
        all_articles = []

        # get articles from all sources
        for src in self.source:
            all_articles.extend(src.get_articles())

        # get all words
        art_w = self.get_article_words(all_articles)

        """
        ## test
        k = 0
        print(all_articles[k].title, all_articles[k].description)
        for wd in art_w[k].keys():
            print("tfidf(%s) = %f" % (wd, get_tfidf(wd, art_w, k)))
        """

        # get matrix :)
        words_matrix, features_key = feature.get_feature_matrix(art_w, get_tfidf)

        # extract_features
        weight_matrix, feature_matrix = nmf.factorize(numpy.matrix(words_matrix), pc=20, it=50)

        # test
        """
        print("Weight Matrix:")
        print(weight_matrix)
        print("Feature Matrix")
        print(feature_matrix)
        """
        self.display_result(all_articles, weight_matrix)

        return words_matrix


    def display_result(self, articles, weight_matrix, k=5):
        n = numpy.shape(weight_matrix)[1]  # num of features

        # for each feature, display kth most relative articles
        for i in range(n):
            print("Feature %d:" % (i + 1))

            feature_vector = [(weight_matrix[index, i], index) for index in range(len(articles))]
            # sort feature_vector
            feature_vector.sort(key=lambda x: x[0])

            # display
            for j in range(k):
                article_index = feature_vector[j][1]
                article = articles[article_index]

                print("%d - %s" % (j, article))

            print


    def get_article_words(self, articles):
        article_words = []  # occurrence of words in each article

        for a in articles:
            words = self.word_splitter.split(a.title) \
                    + self.word_splitter.split(a.description) \
                    + self.word_splitter.split(a.content)

            ar_word = {}

            for word in words:
                ar_word.setdefault(word, 0)
                ar_word[word] += 1

            article_words.append(ar_word)

        return article_words

