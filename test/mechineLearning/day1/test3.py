# -*- conding:utf-8 -*-
# 2019/1/30
# Author: lpw
# Description :

import jieba

data = jieba.cut("我是中国人")
print(type(data))
for i in data:
    print(i)