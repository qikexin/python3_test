# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/2 11:45
import sqlalchemy
class Field:
    def __init__(self,name,fieldname=None,pk=False,unique=False,default=None,nullable=True,index=False):
        self.name = name
        if fieldname is None:
            self.fieldname=fieldname
        self.pk =pk
        self.unique=unique
        self.default=default
        self.nullable=nullable
        self.index=index
    def validate(self):
        raise NotImplementedError()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return

    def __set__(self, instance, value):
        self.name = instance.name
        instance.__dict__[]
    def __str__(self):
        return "".format(self.__class__.__name__,self.name)

class IntFiled(Field):
    def __init__(self,name,fieldname=None,pk=False,unique=False,default=None,nullable=True,index=False,auto_increment=False):
        self.auto_increment = auto_increment
        super().__init__(name,fieldname,pk,unique,default,nullable,index)
    def validate(self): #auto_increment
        pass
class StringFiled(Field):
    def __init__(self,name,fieldname=None,pk=False,unique=False,default=None,nullable=True,index=False,length=32):
        self.length = length
        super().__init__(name,fieldname,pk,unique,default,nullable,index)
    def validate(self):
        pass
class Studen:
    id = 1 #描述器 来描述字段的各种特征
    name = 'tom'
    def __init__(self):
        self.id = 1
        self.name = 'tom'