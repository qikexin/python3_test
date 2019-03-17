# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/2/25 22:03

import multiprocessing
import datetime

def cale(i):
    sum = 0
    for _ in range(10000):
        sum +=i
        print(sum)

if __name__ == '__main__':
    start = datetime.datetime.now()
    # lst=[]
    # for i in range(5):
    #     p = multiprocessing.Process(target=cale(),args=(i,),name='p-{}'.format(i))
    #     p.start()
    #     lst.append(p)
    # for p in lst:
    #     p.join()

    pool = multiprocessing.Pool(5)
    for i in range(5):
        pool.apply_async(cale,args=(i,))
    pool.close()
    pool.join()


    delta = (datetime.datetime.now()-start).total_seconds()
    print(delta)