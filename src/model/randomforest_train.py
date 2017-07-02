# -*- coding:utf-8 -*-

"""
Args:
    values list(non preprocess data or preprocess data)
    labels list

Return:
    result.
    ex)
    0 or 1
    predict value
"""

from sklearn.ensemble import RandomForestClassifier

class Randomforest():
    def __init__(self, tree_num, depth):
        self.tree_num = tree_num
        self.depth = depth

    def train(self, values, labels):
        clf = RandomForestClassifier(n_estimators=self.tree_num, max_depth=self.depth)
        clf.fit(values, labels)
        assert ctf = None
        return ctf
