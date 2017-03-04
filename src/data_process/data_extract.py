# -*- coding: utf-8 -*-

import datetime
from urllib2 import Request, urlopen
import lxml.html


def get_url(agent, url):
    headers = {"User-Agent": agent, }
    request = Request(url, None, headers)
    html = urlopen(request).read().decode('utf-8')
    root = lxml.html.fromstring(html)

    return root


def adjust_price(val):
    price_one = int(str(val)[-1])
    if price_one >= 5:
        val = round(val - 5, -1) + 5
    elif price_one < 5:
        val = round(val, -1)

    return val


def get_table(root):
    start_val = root.xpath('//span[@dir="ltr"]/text()')
    high_val = root.xpath('//span[@class="inlineblock pid-8859-high"]/text()')
    low_val = root.xpath('//span[@class="inlineblock pid-8859-low"]/text()')
    fin_val = root.xpath('//span[@class="arial_26 inlineblock pid-8859-last"][@id="last_last"][@dir="ltr"]/text()')
    price_list = [start_val[4], high_val[0], low_val[0], fin_val[0]]
    price_list = [float(x.replace(',', '')) for x in price_list]
    price_list = [adjust_price(x) for x in price_list]

    return price_list


def extractor():
    """Extract stock data
       from http://jp.investing.com/indices/japan-225-futures
       in every any minutes.

       input : term
       output : extract result
    """

    user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    url = "http://jp.investing.com/indices/japan-225-futures"

    now = datetime.datetime.today()
    data_list = [now.strftime("%Y/%m/%d"), now.strftime("%H:%M")]

    # get source of target url
    root = get_url(user_agent, url)

    # get value table
    price_list = get_table(root)

    print("finish extracting data")

    data_list.extend(price_list)

    return data_list
