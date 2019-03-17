# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 15:35

import datetime, time


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        time.sleep(2)
        stop = datetime.datetime.now()
        print("消耗了{}时间".format(stop - start))
        return func

    return wrapper


@timer  # add=timer(add)
def add(x, y):
    print("x+y={}".format(x + y))
    return x + y


add(1, 2)
