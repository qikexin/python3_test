# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/14 23:32
import inspect
from functools import wraps
def check(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        # print("line 8|",args,kwargs)
        sig = inspect.signature(fn)
        params = sig.parameters #有序字典
        values = list(params.values())
        #位置参数处理
        for i,p in enumerate(args): #enumerate把一个可迭代对象变成顺序字典
            param = values[i]
            if param.annotation is not param.empty and not isinstance(p,param.annotation):
                print(p,"!==",values[i].annotation)
        #关键字传惨处理
        for k,v in kwargs.items():
            if params[k].annotation is not inspect._empty and not isinstance(v,params[k].annotation):
                print(k,v,"!===",params[k].annotation)
        ret = fn(*args,**kwargs)
        return  ret
    return wrapper
@check
def add(x:int,y:int = 8)->int:
    return x + y

# print(add(5,8))
# print("-----")
print(add(x=5,y=8))