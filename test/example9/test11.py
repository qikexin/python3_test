# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/17 8:35
class StaticMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        print(self,instance,owner)
        return self.fn
from functools import partial
class ClassMethod:
    def __init__(self,fn):
        self.fn = fn
    def __get__(self, instance, owner):
        print(self,instance,owner)
        return partial(self.fn,owner)

class A:
    # @StaticMethod  #foo=StaticMethod(foo)
    @staticmethod
    def foo():
        print('static')
    @ClassMethod #bar=ClassMethod(bar)
    def bar(cls):
        print(cls.__class__)
# f = A.foo
# print(f)
# f()

f = A.bar
print(f)
f()