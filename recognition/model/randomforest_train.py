# -*- coding:utf-8 -*-

"""
Args:
    values list(non preprocess data or preprocess data)
    labels list

Return:
    clf
"""

from sklearn.ensemble import RandomForestClassifier

class Randomforest(object):
    def __init__(self, tree_num, depth, input_term):
        self.tree_num = tree_num
        self.depth = depth
        self.input_term = input_term

    def create_input_value(self, values):
        input_values = [values[i:i+self.input_term] for i in range(len(values) - self.input_term)]

        return(input_values)

    def train(self, values, labels):
        input_values = self.create_input_value(values)
        clf = RandomForestClassifier(n_estimators=self.tree_num, max_depth=self.depth)
        clf.fit(input_values, labels)

        return(clf)
