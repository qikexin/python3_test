# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 8:50
class Person:
    age =3
    height = 170
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age
    def growp(self,incr=1):
        if 0 < incr < 150:
            self.__age += incr
    def getage(self):
        return self.__age
tom = Person("tom")
tom.growp(2)
print(tom.age)
tom._Person__age =200
print(tom.getage())

print(Person.__dict__)
print(tom.__dict__)
