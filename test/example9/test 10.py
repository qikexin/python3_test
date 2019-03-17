# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/16 22:09
class A:
    def __init__(self):
        print('A.init')
        self.a1 = 'a1'
    def __get__(self, instance, owner):
        print('A.__get__',self,instance,owner)
        return self
class B:
    x = A()
    def __init__(self):
        print('B.init')
        # self.x = A()

print(B.x.a1)
# print(B.x.a1)
# b = B()
# print(b.x)
# print(b.x.a1)
# b = B()