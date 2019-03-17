# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/17 12:08
import importlib
def plugin_load(plugin_name:str,sep=":"):
    m,x,c = plugin_name.partition(sep)
    # print(m,x,c)
    # mod = __import__(m)
    mod = importlib.import_module(m)
    cls = getattr(mod,c)
    return cls

if __name__ == '__main__':
    cls = plugin_load("test1:A")
    print(cls)