# -*- coding:utf-8 -*-
import  functools
import inspect
def add(x,y):
    return x + y

print(inspect.signature(add))
newadd = functools.partial(add,y=6)
print(newadd(4))
print(inspect.signature(newadd))