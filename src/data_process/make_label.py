# -*- coding:utf-8 -*-

"""
create labels(up:1 or down:0)
Args:
    value(previous and now data)

Return:
    cal_label: label between i and i+1
    cal_labels: all labels list
"""


class Make_label(object):
    def __init__(self):
        pass

    def cal_label(self, value, aft_value):
        diff = value - pre_value
        if diff > 0:
            label = 1
        elif diff < 0:
            label = -1
        else:
            label = 0
        return(label)

    def cal_lables(self, values):
        labels = [self.cal_label(values[i], values[i+1]) for i in range(len(values) - 1)]

        return(labels)
