# -*- coding:utf-8 -*-

"""
Args:
    ctf(after train model)
    now extracting data

Return:
    result.
    ex)
    0 or 1
    predict value
"""

class Randomforest_test(object):
    def __init__(self, tree_num, depth, input_term):
        self.tree_num = tree_num
        self.depth = depth
        self.input_term = input_term

    def test(self, clf, values):
        input_x = values[-self.input_term:]
        result = [clf.predict(input_x), input_x[-1]]

        return(result)
