# -*- conding:utf-8 -*-
# 2018/11/22
# Author: lpw
# Description : 冒泡排序
import time
def cale_time(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__,t2 - t1))
    return wrapper

@cale_time
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

@cale_time
def bubble_sort_1(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if not exchange:
            break

if __name__ == '__main__':
    data = list(range(1000))
    bubble_sort(data)
    bubble_sort_1(data)