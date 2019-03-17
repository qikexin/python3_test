# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/3/10 17:14
from functools import total_ordering


@total_ordering
class A:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        self.x == other.x

    def __lt__(self, other):
        self.x < other.x


print(A(5) > A(6))
print(A(5) < A(6))
print(A(5) == A(6))
