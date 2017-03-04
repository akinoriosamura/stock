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

class Randomforest():
    def __init__(self, tree_num, depth):
        self.tree_num = tree_num
        self.depth = depth

    def test(self, ctf, values, test_term):
        input_x = values[-test_term:-1]
        result = [clf.predict(input_x), input_x[-1]]

        return result

