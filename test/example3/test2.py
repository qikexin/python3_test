# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/1/5 16:41

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(2)
queue.append(3)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
