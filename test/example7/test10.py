# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 20:55
from functools import partial
class StaticMethod:
    def __init__(self,fn):
        print(fn)
        self.fn = fn
    def __get__(self, instance, owner):
        print(self,instance,owner)
        return self.fn

class ClassMethod:
    def __init__(self,fn):
        print(fn)
        self.fn = fn
    def __get__(self, instance, owner):
        print(self,instance,owner)
        # return self.fn(owner)
        return partial(self.fn,owner)
class A:
    @StaticMethod
    def foo(): #foo = StaticMethod(foo)
        print('static')

    @ClassMethod
    def bar(cls):
        print(cls.__name__)
f = A.foo
print(f)
f()
#
f = A.bar
print(f)
#f(A) = A.bar(A)
f()