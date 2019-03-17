# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 21:31
class Typed:
    def __init__(self,type):
        self.type = type
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        print('T.set',self,instance,value)
        if not isinstance(value,self.type):
            raise ValueError(value)

import inspect

class TypeAssert:
    def __init__(self,cls):
        self.cls = cls

    def __call__(self,name, age):
        params = inspect.signatura(self.cls).parameters
        print(params)
        for name,param in params.items():
            print(name,param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls,name,Typed(param.annotation))
@TypeAssert
class Person:
    name = Typed(str)
    age = Typed(int)
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

p1 = Person('tom',18)