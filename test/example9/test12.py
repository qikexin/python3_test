# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/17 8:56
class Typed:
    def __init__(self,Type):
        self.Type = Type
    def __set__(self, instance, value):
        print(self,instance,value)
        if not isinstance(value,self.Type):
            raise TypeError("{} is not {} ".format(value,self.Type))
import  inspect
class TypeAssert:
    def __init__(self,cls):
        self.cls = cls
    def __call__(self, *args, **kwargs):
        params = inspect.signature(self.cls).parameters  #parameters返回的是一个有序字典
        print(params)
        for name,param in params.items():
            # print(name,param)
            print(name,param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls,name,Typed(param.annotation))
@TypeAssert #Persion = TypeAssert(Persion)
class Persion:
    # name = Typed(str)
    # age = Typed(int)
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

# a = Persion("aaa",18)
# print(a)
