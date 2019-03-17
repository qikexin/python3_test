# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/14 20:37
import time
import datetime

def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__  = src.__doc__
        dst.__qualname__ = src.__qualname__
        return dst
    return _copy
def logger(t):
    def _logger(fn):
        @copy_properties(fn)
        def wrapper(*args,**kwargs):
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            durateion = (datetime.datetime.now()-start).total_seconds()
            if durateion > 5:
                print("funtion {} took {}s".format(wrapper.__name__,durateion))
            return ret
        return wrapper
    return _logger

@logger(4)   #add = logger(4)(add)
def add(x,y):
    """
    add
    :param x:
    :param y:
    :return:
    """
    time.sleep(5)
    return x+y

print(add(1,4))
print(add.__name__,add.__doc__,add.__qualname__,sep="\n")