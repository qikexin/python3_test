# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/1/5 16:54


class Node(object):
    def __init__(self,item=None):
        self.item = item
        self.next = None
head = Node()
head.next = Node(20)
head.next.next = Node(30)

def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.item)
        curNode = curNode.next

traversal(head)

class Node(object):
    def __init__(self,item=None):
        self.item = item
        self.next = None
        self.prior = None

