# -*- coding:utf-8 -*-
# @Author:lpw
# @Time: 2018/11/25 0:56
import time
class Foo(object):
    instance = None
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Foo.instance:
            return Foo.instance
        else:
            Foo.instance = object.__new__(cls,*args,**kwargs)
            return Foo.instance


obj1 = Foo.get_instance()
obj2 = Foo.get_instance()
print(id(obj1),id(obj2))