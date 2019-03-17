# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 11:26
class SingleNode:
    '''
    代表一个节点
    '''
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class LinkedList:
    '''
    节点的容器，多个节点构成的链表
    '''
    def __init__(self):
        self.nodes = []
        self.head = None
        self.tail = None
    def append(self,val):
        node = SingleNode(val)
        prev = self.tail
        if prev is None:
            self.head = node

        self.nodes.append(val)
        self.tail  = node