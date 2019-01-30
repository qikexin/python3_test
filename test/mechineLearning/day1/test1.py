# -*- conding:utf-8 -*-
# 2019/1/29
# Author: lpw
# Description :对字典进行数据抽取。one-hot编码

from sklearn.feature_extraction import DictVectorizer
def dictvec():
    '''
    字典数据抽取
    ;return: None
    '''
    #实例化
    data=[
    {'city':'北京','temperature':100},
    {'city':'上海','temperature':60},
    {'city':'深圳','temperature':30}
    ]
    dict = DictVectorizer(sparse=False)
    #调用fit_transform
    data = dict.fit_transform(data)
    print(dict.get_feature_names())
    print(dict.inverse_transform(data))
    print(data)
    return  None
if __name__ == '__main__':
    dictvec()
