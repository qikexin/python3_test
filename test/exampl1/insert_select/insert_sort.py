# -*- conding:utf-8 -*-
# 2018/11/23
# Author: lpw
# Description : 插入排序
import time
def cale_time(fun):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = fun(*args,**kwargs)
        t2 = time.time()
        print("消耗了 %s 秒" % (t2-t1) )
    return  wrapper

@cale_time
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j >=0 and tmp< li[j]:
            li[j+1]=li[j]
            j=j-1
        li[j+1]=tmp



if __name__ == '__main__':
    data = list(range(1000))
    insert_sort(data)
    print(data)