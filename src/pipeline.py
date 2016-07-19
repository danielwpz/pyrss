"""
pipeline.py

Daniel Wang
May 2016
"""
import sys
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

    def __init__(self, source=None):
        if source is None:
            source = []
        self.source = source

    def run(self, pc=30):
        all_articles = []

        # get articles from all sources
        for src in self.source:
            all_articles.extend(src.get_articles())

        # get all words
        art_w = self.__get_article_words(all_articles)

        # get matrix :)
        words_matrix, features_key = feature.get_feature_matrix(art_w, weight_calculate=get_tfidf)

        self.__display_features(words_matrix, features_key)

        # extract_features
        weight_matrix, feature_matrix = nmf.factorize(words_matrix, pc=pc, it=60)
        self.__display_result(all_articles, features_key, weight_matrix, feature_matrix, k=6)

        result = self.__generate_result(all_articles, weight_matrix)

        return result

    @staticmethod
    def __generate_result(articles, weight_matrix):
        M = weight_matrix.shape[0]   # number of articles
        N = weight_matrix.shape[1]   # number of features

        result = [[(weight_matrix[m, n], articles[m]) for m in range(M)] for n in range(N)]
        return result

    @staticmethod
    def __display_features(article_features, feature_keys, k=8):
        print("Article-Word matrix (top %d Words): " % k)
        for i in range(article_features.shape[0]):
            f_vector = [(article_features[i, index], index) for index in range(feature_keys.size)]

            f_vector.sort(key=lambda x: x[0])
            f_vector.reverse()

            line = ""
            for f in f_vector[0: k]:
                line += " (%s: %2.2f) " % (feature_keys[f[1]], f[0])

            print(line)

    @staticmethod
    def __display_result(articles, words, weight_matrix, feature_matrix, k=5, l=6):
        n = numpy.shape(weight_matrix)[1]  # num of features

        print
        print("%d articles, %d features computed." % (len(articles), n))

        # for each feature, display kth most relative articles and lth most relative words
        for i in range(n):
            print("Feature %d:" % (i + 1))

            # print l most related words for each feature
            sys.stdout.write("(")
            word_vector = [(feature_matrix[i, index], index) for index in range(len(words))]
            word_vector.sort(key=lambda x: x[0])
            word_vector.reverse()

            for j in range(l):
                word_index = word_vector[j][1]
                word = words[word_index]
                sys.stdout.write("%s, " % word)
            print(')')

            # print article groups
            feature_vector = [(weight_matrix[index, i], index) for index in range(len(articles))]
            # sort feature_vector
            feature_vector.sort(key=lambda x: x[0])
            feature_vector.reverse()

            # display
            for j in range(k):
                article_index = feature_vector[j][1]
                article = articles[article_index]

                print("%2.2f - %s" % (feature_vector[j][0], article))

            print

    def __get_article_words(self, articles):
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
