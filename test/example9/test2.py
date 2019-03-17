# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/14 21:42
import time
import datetime

def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__  = src.__doc__
        dst.__qualname__ = src.__qualname__
        return dst
    return _copy

def logger(fn):
    @copy_properties(fn)  #推导过程：copy_properties(fn)返回的是_copy,所以@_copy => wrapper=_copy(wrapper),所以_copy(wrapper)返回的必须还是wrapper，所以在上面带参装饰器中的_copy(dst)函数返回值必须还是dst
    def wrapper(*args, **kwargs):
        """
        in wrapper
        :param args:
        :param kwargs:
        :return:
        """
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        stop = datetime.datetime.now()
        duration = (stop-start).total_seconds()
        print("function {} took {}s".format(fn.__name__,duration))
        return ret
    # copy_properties(fn,wrapper)
    return wrapper


@logger
def add(x, y):
    """
    test
    :param x:
    :param y:
    :return:
    """
    time.sleep(1)
    return x + y

print(add(10,7))
print(add.__name__,add.__doc__,add.__qualname__,sep="\n")
# print(help(add))