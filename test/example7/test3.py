# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 15:45
import time
import datetime


class TimeIt:
    def __enter__(self):
        print('enter')
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print(delta)
        return


def add(x, y):
    time.sleep(2)
    return x + y


with TimeIt() as f:
    add(1, 3)
