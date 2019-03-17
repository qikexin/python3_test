# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/16 20:55
from functools import wraps
import time
import inspect

def m_cache(fn):
    local_cache = {}
    def wrapper(*args,**kwargs):
        print(*args,**kwargs)

        key_dict = {}  #用storted排序
        sig = inspect.signature(fn)
        od = sig.parameters() #有序字典

        param_list = list(od.keys())
        #位置参数
        for i,v in enumerate(args):
            print(i,v)
            k = param_list[i]
            key_dict[k] = v
        #关键字参数
        # for k,v in kwargs.items():
        #     key_dict[k] = v
        key_dict.update(kwargs)

        key = tuple(sorted(key_dict.items()))

        if key not in local_cache.keys():
            ret = fn(*args,**kwargs)
            local_cache[key] = ret

        return local_cache[key]
    return wrapper

@m_cache
def add(x,y=5):
    time.sleep(3)
    ret = x  + y
    print(ret)
    return ret
