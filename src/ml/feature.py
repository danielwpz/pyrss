"""
feature.py

Daniel Wang
May 2016

'feature' is a list contains each feature and its weight in every item.

e.g.
feature = [
    {'feature_1': 1.0, 'feature_2': 2.9, 'feature_3': 0.0, 'feature_4': 0.0},
    {'feature_1': 0.0, 'feature_2': 1.1, 'feature_3': 2.7, 'feature_4': 3.3},
    ....
    ]

Which could be written as an item-feature matrix:

===========================================================
            feature_1  feature_2  feature_3  ...  feature_m
item_1        1.0         2.9        0.0

item_2        0.0         1.1        2.7

...

item_n
===========================================================

, in which an element (i,j) indicates the weight of feature_j
in item_i. And 0 means the item doesn't contain that feature.
"""

import numpy


def default_weight_calculate(f, items, k):
    """
    if items[k] has feature f, return the origin value.
    else return 0
    :param f: the feature to be calculated
    :param items: all feature items
    :param k: calculate weight for the kth item in items
    :return: double
    """
    if items[k].get(f) is not None:
        return items[k].get(f)
    else:
        return 0.0


def get_feature_matrix(items, weight_calculate=default_weight_calculate):
    """
    Give the features for a list of items,
    return the corresponding item-feature matrix
    (see previous feature definition)

    :param items: items with features of each one
    :param weight_calculate: weight calculating function,
                             be responsible to calculate each element in result matrix
                             from original features
    :return:
        - a MxN numpy matrix, which is the item-feature above
        - a 1xN numpy array, which serves as the column names
    """
    # reduce features to get all_features
    all_features = {}

    for f in items:
        keys = f.keys()
        for k in keys:
            all_features.setdefault(k, 0)
            all_features[k] += f[k]

    all_features_key = all_features.keys()  # this will serve as column name of matrix

    # generate matrix (M x N)
    # M: number of items
    # N: number of features
    matrix = []
    M = len(items)
    N = len(all_features_key)
    for m in range(M):
        vector = [0] * N
        for i in range(N):
            vector[i] = weight_calculate(all_features_key[i], items, m)
        matrix.append(vector)

    return numpy.matrix(matrix), numpy.array(all_features_key)
