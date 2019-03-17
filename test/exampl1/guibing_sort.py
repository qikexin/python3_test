# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2018/12/9 11:03

#一次归并（归并:假如将一个列表从中间分成两个有序的子列表，然后分别对两个子列表中元素进行比较，添加到临时列表）
def merge(li,low,mid,high):
    '''
    li表示完整的列表
    low表示指向列表的第一个元素的指针
    mid表示将完整列表从mid指针处分为两个有序子列表的位置
    hight表示指向列表的最后一个元素的指针
    i,j 分别表示前后两个移动的指针
    '''
    i = low
    j = mid+1
    temp = []
    #最开始比较，只要左子列表和右子列表中都存在元素，就进行比较
    while i <= mid and j<= high:
        if li[i] < li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1
    #当右子列表率先没有可比较的元素，而左子列表还剩下元素时，将左子列表剩下元素依次添加到临时列表
    #上一个while之心完后，只剩下左子列表或者右子列表，i或j表示的是剩下的子列表的一个元素的指针
    while i <= mid:
        temp.append(li[i])
        i += 1
    #当左子列表率先没有可比较的元素，而右子列表还剩下元素时，将右子列表剩下的元素依次添加到临时列表
    while j <= high:
        temp.append(li[j])
        j += 1

    #第二个while和第三个while只会执行其中的一个
    li[low:high+1] = temp

def mergesort(li,low,high):
    if low < high:
        mid = (low+high)//2
        mergesort(li,low,mid)
        mergesort(li,mid+1,high)
        merge(li,low,mid,high)

def shell_sort(li):
    gap = len(li)//2
    while gap >= 1:
        for i in range(gap,len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]
                li[j + gap] = li[j]
                j -= gap
            li[i - gap] = tmp
        gap /= 2
def func3(x):
    if x >0:
        print(x)
        func3(x-1)
def func4(x):
    if x > 0:
        func4(x-1)
        print(x)
func3(3)
func4(3)