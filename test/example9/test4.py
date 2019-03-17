# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/14 22:46
import time
import functools
def logger(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        ret = fn(*args,**kwargs)
        print("after")
        return ret
    functools.update_wrapper(wrapper,fn)
    return wrapper

@logger  #add = logger(add) ,logger(add) 返回的是_logger,所以此时就相当于add == _logger
def add(x,y):
    """
    test add
    :param x:
    :param y:
    :return:
    """
    time.sleep(1)
    return x+y

print(add(1,4))
print(add.__wrapped__,add.__doc__,sep="\n")