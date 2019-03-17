# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/17 9:53

class Property:
    def __init__(self, fget,fset= None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        if instance is not None:
            return self.fget(instance)
        return self

    def __set__(self, instance, value):
        if callable(self.fset):
            raise AttributeError("can't set attribute")
        self.fset(instance,value)

    def setter(self,fn):
        self.fn = fn
        return self


class A:
    def __init__(self,data):
        self._data = data
    @Property #data = Property(data) => data = obj 这里data就是一个Property的实例对象obj
    def data(self):
        return self._data

    @data.setter #data =  data.setter(data) => Property(data).setter(data) => data = obj（这里obj = data = Property(data)）
    def data(self,value):
        self._data = value

a = A(100)
print(a.data)
a.data = 200
print(a.data)