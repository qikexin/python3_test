# -*- coding:utf-8 -*-
# @Author:lpw
# @Time: 2018/11/25 0:10

import os

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.basename(os.path.abspath(__file__)))
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.relpath(__file__))