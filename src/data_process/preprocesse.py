# -*- coding : utf-8 -*-

import numpy as np


def return_index(values):
    returns = values.pct_change()
    # caluculate return index
    ret_index = (1 + returns).cumprod()
    ret_index = np.array(ret_index)
    # first line is NaN, so put 1
    ret_index[0] = 1

    return ret_index