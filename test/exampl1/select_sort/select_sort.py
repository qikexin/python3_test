# -*- conding:utf-8 -*-
# 2018/11/22
# Author: lpw
# Description :
import time
def cale_time(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__,t2 - t1))
    return wrapper
@cale_time
def select_sort(li):
    for i in range(len(li)-1):
        min_location = i
        for j in range(i+1,len(li)):
            if li[j] <li[min_location]:
                min_location = j
            li[i],li[min_location] = li[min_location],li[i]
if __name__ == '__main__':
    data = list(range(1000))
    select_sort(data)
    print(data)
    # print("test")