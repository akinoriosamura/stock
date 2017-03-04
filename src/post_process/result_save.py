# -*- coding:utf-8 -*-
"""
output result for saving
(
data,
bef_time - aft_time,
predict,
real,
action(buy, sell, stay),
result(lose, swin, tab),
diff,
total(loss and gain)
)
"""

import csv


def cal_result(action, pre, real):
    if action == "STAY":
        result = ""
        diff = "-"

        return(result, diff)

    if action == "BUY":
        diff = real - pre
    elif action == "SELL":
        diff = pre - real

    if diff > 0:
        result = "Win"
    elif diff < 0:
        result = "Lose"
    elif diff == 0:
        result = "Draw"

    return(result, diff)


def cal_total(action, diff):
    if action != "STAY":
        total = diff * 100
        fee = 84
        total = total - fee

        return(total)


def cal_value(pre, predict, real):
    """calculate action(buy, sell, stay), result(lose, win, tab), diff, total(loss and gain)"""
    action = predict
    result, diff = cal_result(action, pre, real)
    total = cal_total(action, diff)

    return(action, result, diff, total)


def write_csv(output):
    f = open('result_prediction.csv', 'a')

    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(output)


def result_save(data, bef_time, aft_time, pre, predict, real):
    purchase_unit = 1
    action, result, diff, total = cal_value(pre, predict, real)
    output = [data, bef_time, aft_time, pre, real, action, result, diff, purchase_unit, total]
    write_csv(output)

    return(output)