# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 11:43

class Point:
    def __init__(self):
        print('init')
    def __enter__(self):
        print(self.__class__)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.__class__.__name__)
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True

p = Point()
with p as f:
    raise  Exception('ERRO1234')
    print(f == p)
    print(f is p)
    print(p)
    print(f)

print("outer")