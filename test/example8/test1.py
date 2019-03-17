# -*- coding:utf-8 -*-
class Person:
    def normal_method():
        print('normal')
    def method(self):
        print('{}'.format(self))
    @classmethod
    def class_method(cls):
        print('{0}'.format(cls.__name__))
        print('{0}'.format(cls))
        cls.HEIGHT= 170
    @staticmethod
    def static_methd():
        print(Person.HEIGHT)

print(1,Person.normal_method())
print(2,Person().method())
print(3,Person.class_method())
print(4,Person.static_methd())
print(Person.__dict__)


