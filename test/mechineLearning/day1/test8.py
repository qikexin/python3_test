# -*- conding:utf-8 -*-
# 2019/1/31
# Author: lpw
# Description :条形图

from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队", "情圣", "新木乃伊"]

b=[56.01,26.94,17.53,16.49,15.45,14.11,12.96,12.02,11.8,11.61,11.28,11.12,10.38,8.74,7.67,7.55,7.32,6.99,6.88,6.86] #单位：亿

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\STFANGSO.TTF")
# print(len(a))
# print(len(b))
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘制竖向条形图---
# plt.bar(range(len(a)),b,width=0.3)
# plt.xticks(range(len(a)),a,fontproperties=my_font,rotation=45)
#---

#绘制横向条形图---
plt.barh(range(len(a)),b,height=0.8)
plt.yticks(range(len(a)),a,fontproperties=my_font)
#---
plt.grid(alpha=10)
plt.show()