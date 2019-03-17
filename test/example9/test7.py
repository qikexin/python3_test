# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/16 20:10
import functools
import  time
@functools.lru_cache()
def add(x,y=5):
    time.sleep(3)
    ret = x + y
    return  ret

print(add(4))
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)

print([fib(x) for x in range(35)])