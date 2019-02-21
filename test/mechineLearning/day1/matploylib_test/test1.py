# -*- coding:utf-8 -*-
# Author:lpw
# Time: 2019/1/30 21:33
import matplotlib.pyplot as plt

x = range(2,26,2)
y = [15,13,14,5,17,20,25,26,26,24,22,18]
#设置图片大小
plt.figure(figsize=(15,8),dpi=80)

plt.plot(x,y)
#设置x轴的刻度
plt.xticks(range(2,26))
#保存图片
# plt.savefig("sig_size.png")
plt.show()