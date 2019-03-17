# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 15:56
import time
import datetime
from functools import wraps


class TimeIt:
    def __init__(self, fn):
        self._fn = fn

    def __enter__(self):
        print('start')
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print("context {} took {}".format(self._fn.__name__, delta))
        return


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("dec {} took {}".format(fn.__name__, delta))
        return ret

    return wrapper


@logger
def add(x, y):
    time.sleep(2)
    return x + y


with TimeIt(add) as f:
    add(3, 8)
