"""
feature.py

Daniel Wang
May 2016

'feature' is a list contains each feature and its weight in every item.

e.g.
feature = [
    {'A': 1.0, 'B': 2.9, 'C': 0.0},
    {'B': 1.1, 'C': 2.7, 'D': 3.3}
    ]
"""


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
    return the corresponding feature matrix
    :param items: items with features of each one
    :param weight_calculate: weight calculate function
    :return: a MxN matrix
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

    return matrix, all_features_key
