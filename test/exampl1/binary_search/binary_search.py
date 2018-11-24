# -*- conding:utf-8 -*-
# 2018/11/21
# Author: lpw
# Description : 二分算法

def erferfa(list,key):
    low = 0
    hegh = len(list)-1
    while low <= hegh:
        mid = (low+hegh) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid + 1
        else:
            hegh = mid - 1
    return
if __name__ == '__main__':
    list = [1,2,4,6,8,9,]
    index = erferfa(list, 7)
    if index == None:
        print("没有找到元素")
    else:
        print("被查找的元素的索引为：%d" % index)