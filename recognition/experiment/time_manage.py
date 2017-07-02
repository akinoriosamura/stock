# -*- coding:urf-8 -*-

"""
1, sleep optional term(e.g. 30m)

2, sleep in the time closing market.
"""

from time import sleep
from datetime import datetime
from datetime import date
import jholiday

def closing_market():
    while(True):
        now = datetime.now()
        youbi = date(now.year, now.month, now.day).weekday()
        target_date = date(now.year, now.month, now.day)
        holiday_name = jholiday.holiday_name(date=target_date)

        # 祝日が休日に被ってたら、月曜も休む
        if holiday_name is not None:
            if youbi == 5 or youbi == 6:
                while(True):
                    now = datetime.now()
                    youbi = date(now.year, now.month, now.day).weekday()
                    if youbi == 1 and now.hour == 8:
                        break
            while(True):
                now = datetime.now()
                youbi = date(now.year, now.month, now.day).weekday()
                if now.day == holiday.day + 1 and now.hour >= 8:
                    break
                elif now.hour == 5 and now.minute > 30:
                    continue
                elif now.hour > 5:
                    continue
                else:
                    break
        if youbi == 6:
            continue
        if youbi == 5:
            if now.hour == 5 and now.minute > 30:
                continue
            elif now.hour > 5:
                continue
            else:
                break

        target_date_Sat = date(now.year, now.month, now.day-2)
        target_date_Sun = date(now.year, now.month, now.day-1)
        holiday_name_Sat = jholiday.holiday_name(date=target_date_Sat)
        holiday_name_Sun = jholiday.holiday_name(date=target_date_Sun)
        if youbi == 0 and holiday_name_Sat is not None or holiday_name_Sun is not None:
            while(True):
                now = datetime.now()
                youbi = date(now.year, now.month, now.day).weekday()
                if youbi == 1 and now.hour >= 8:
                    break
            break
        if youbi == 0 and now.hour < 8 and holiday_name is None:
            continue
        break

def sleep_term(term):
    sleep(60)
    todaydetail = datetime.datetime.today()
    if todaydetail.minute > 30:
        stop_time = 60 - todaydetail.minute + 1
    else:
        stop_time = 30 - todaydetail.minute + 1
    stop_second = stop_time*60
    return stop_second

