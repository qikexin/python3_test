# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 18:38

class Base:
    n = 5

class A(Base):
    m = 6
    def __getattribute__(self, item):
        print(item)
    def __init__(self,x):
        self.x = x
    def __getattr__(self, item):
        print("__getattr__",item)
    def __setattr__(self, key, value):
        print("__setattr__",key,value)
