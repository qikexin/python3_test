# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/14 20:37
# import functools
# def logger(fn):
#     def _logger(*args,**kwargs):
#         ret = fn(*args,**kwargs)
#         print("after")
#         return ret
#     return _logger
#
# @logger  #add = logger(add) ,logger(add) 返回的是_logger,所以此时就相当于add == _logger
# def add(x,y):
#     return x+y
#
# print(add(1,4)) #这里调用的add已经不是原来的add，而是相当于内层函数_logger,

class A:
    pass