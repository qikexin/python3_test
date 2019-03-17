# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/2 10:56

# class A:
#     def __init__(self):
#         print('init')
#     def show(self):
#         print('show')
# def __init__(self):
#     print('x.init')
# xclass = type('x',(object,),{'a':100,'__init_':__init__})
# # print(xclass)
# # print(type(xclass))
# print(xclass.__dict__)
# print(xclass.__name__)
# print(xclass.__init__)
# print(xclass.mro())
# print(xclass().__dict__)

class XMeta(type):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)

# print(XMeta)
# print(type(XMeta))
# print(XMeta.__dict__)
class A(metaclass=XMeta):
    pass

type(A.__mro__)