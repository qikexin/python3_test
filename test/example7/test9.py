# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 19:13
class A:
    def __init__(self):
        print('A.init')
        self.a1 = 'al'
    def __get__(self, instance, owner):
        print('A.__get__',self,instance,owner)
        return  self

class B:
    x = A()
    def __init__(self):
        print('B.init')
        # self.x = A()

# print(B.x.a1)
print(B.x)

b = B()
# print(B.x.a1)
# print(B.x)
print("=========")
# print(b.x.a1)
print(b.x)
